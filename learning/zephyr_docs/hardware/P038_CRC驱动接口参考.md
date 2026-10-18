---
id: learning.zephyr-docs.hardware.hwapi-crc
title: CRC驱动接口参考
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第38章\_CRC驱动接口参考

原文：[group__crc__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html)。读取日期：2026-10-13，`latest`。

## 38.1\_接口、上下文与版本

本页给出 **循环冗余校验（Cyclic Redundancy Check，CRC）**设备的 **应用程序编程接口（Application Programming Interface，API）**。接口自Zephyr 4.3引入，版本为0.1.0；公共头文件为官方源码中的 `zephyr/drivers/crc.h`。使用场景和配置入口见[CRC循环冗余校验](P033_CRC循环冗余校验.md)。

`crc_ctx` 是CRC **上下文（Context）**结构，用于在计算调用之间传递状态。其字段在独立的[CRC上下文参考](P046_CRC上下文结构.md)中说明。驱动实现者还可参阅[CRC驱动后端API](P047_CRC驱动后端接口.md)。

## 38.2\_类型、状态与反转标志

以下三个别名都以 [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) 为基础，分别表达初始值、多项式和结果，不能仅因底层类型相同就混淆用途。

| 类型 | 声明 | 含义 |
| --- | --- | --- |
| [`crc_init_val_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#ga45ff64f03c4bfadd47ba66ce944c09bf) | `typedef uint32_t crc_init_val_t;` | 保存CRC初始种子值。 |
| [`crc_poly_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#ga938a05769aa6a61c22217611fb375218) | `typedef uint32_t crc_poly_t;` | 保存CRC多项式值；原文指出预定义多项式值见 `CRC_POLYNOMIAL`。 |
| [`crc_result_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#ga7c6663d361406882a73e8ba171840adc) | `typedef uint32_t crc_result_t;` | 保存CRC结果值。 |

**状态枚举（State Enumeration）** `enum crc_state` 包括：

| 枚举项 | 含义 |
| --- | --- |
| `CRC_STATE_IDLE = 0` | CRC设备空闲。 |
| [`CRC_STATE_IN_PROGRESS`](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#ggab463a891df58c677e5cafb160dfdb9a3a2b46dc7210559c77073ad46d5757c7a2) | CRC计算正在进行。 |

输入、输出数据串的反转标志如下。`BIT(n)` 是位掩码宏，表示仅第n位为1的值。

| 宏 | 值 | 含义 |
| --- | --- | --- |
| [`CRC_FLAG_REVERSE_INPUT`](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#ga9686f52f45a6023d7e7c144732ab9202) | `BIT(0)` | 反转输入数据串。 |
| [`CRC_FLAG_REVERSE_OUTPUT`](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#gad2413454ab20a446fdc53f08ddd85a4e) | `BIT(1)` | 反转输出数据串。 |

> 译注：原文使用“Reverse input/output string”。这是CRC数据处理标志，不能按普通文本倒序理解，也不能据此断言其粒度是逐字节、逐字或整个缓冲区；具体支持方式应结合所用驱动说明。

## 38.3\_开始、更新与结束计算

下面是原页声明表中三个函数的C声明。[`crc_begin()`](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#gae6f2adfd858b18765b2e58d8135c28fa) 为计算配置CRC单元，[`crc_update()`](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#gaf5e71e99b5838e4b21f30e4b2fb4a684) 对输入缓冲区执行CRC计算并取得结果，[`crc_finish()`](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#gab144200cba95d6cc08c85cf9c5c1dd91) 完成计算收尾。

```c
int crc_begin(const struct device *dev, struct crc_ctx *ctx);
int crc_update(const struct device *dev, struct crc_ctx *ctx,
               const void *buffer, size_t bufsize);
int crc_finish(const struct device *dev, struct crc_ctx *ctx);
```

三个函数的 `dev` 都指向设备结构，`ctx` 都指向CRC上下文结构。更新函数另外接收 `buffer`，即输入数据缓冲区指针，以及 `bufsize`，即该缓冲区中的字节数。

三个函数成功都返回0；函数未实现时返回 `-ENOSYS`；其他失败返回相应错误码，原页将这一类返回值写为 [`errno`](../error_reference/P003_系统错误号公共接口.md#gab03f640d90fbc5bcb75285d08a0f25ed)。调用顺序中的配置、更新和收尾各有独立结果，调用方应在继续下一步前处理失败。

## 38.4\_核对预期结果

[`crc_verify()`](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#gaed8caf868b83c4ea1271a9f5ab6abd35) 将上下文中的CRC结果与预期值比较：

```c
static inline int crc_verify(struct crc_ctx *ctx, crc_result_t expected);
```

`ctx` 是CRC上下文指针，`expected` 是预期CRC结果。校验成功返回0；计算尚未完成返回 `-EBUSY`；校验失败返回 `-EPERM`。这里的校验失败是计算结果不符合预期，不能把它当作“计算已经完成并且数据正确”。可继续阅读[CRC校验示例](P042_CRC校验示例.md)。

[上一章：EEPROM命令行](P037_EEPROM命令行.md) · [下一章：熵源接口参考](P039_熵源接口参考.md) · [返回大纲](大纲.md)
