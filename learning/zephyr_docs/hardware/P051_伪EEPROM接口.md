---
id: learning.zephyr-docs.hardware.backend-5
title: 伪EEPROM接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__eeprom__fake.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第51章\_伪EEPROM接口

原文：[group__eeprom__fake](https://docs.zephyrproject.org/latest/doxygen/html/group__eeprom__fake.html)。读取日期：2026-10-13，`latest`。

<a id="agroup__device__model_html_ga9a65996ce21f43acb7db061e23b48ec7"></a>
<a id="agroup__devicetree-generic-id_html_gab7d23294a6bf7fd44a98b48ec47d8a79"></a>
<a id="agroup__eeprom__interface_html_ga1973e8982de88f53e49154dc73461e56"></a>
<a id="agroup__ztest__assert_html_gacd075c7ee4dc2d64701bd3098a31b673"></a>
<a id="agroup__ztest__assert_html_gade40e2ec78ec813739e7725524fae7f0"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="details"></a>
<a id="doc-func-members"></a>
<a id="files"></a>
<a id="func-members"></a>
<a id="header-details"></a>
<a id="header-doc-func-members"></a>
<a id="header-files"></a>
<a id="header-func-members"></a>
<a id="r_eeprom_5Ffake_2Eh"></a>

## 51.1\_用于测试的伪EEPROM

这是 **电可擦可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）** **应用程序编程接口（Application Programming Interface，API）**的 **伪函数框架（Fake Function Framework，FFF）**实现，用于测试。它通过Kconfig配置项 [`CONFIG_EEPROM_FAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EEPROM_FAKE) 启用，并从设备树 `zephyr,fake-eeprom` 节点实例化。官方接口头文件为 `zephyr/drivers/eeprom/eeprom_fake.h`。

每个伪函数都配有一个FFF控制结构，名字是在函数名后加 `_fake`。测试借助该结构设置返回值、安装自定义伪函数，或者检查调用次数和捕获的参数。原页没有列出这些控制结构的独立定义，细节指向[通过FFF模拟（Mocking via FFF）](https://docs.zephyrproject.org/latest/develop/test/ztest.html#mocking-fff)。

## 51.2\_返回值、输出参数与重置

只报告状态的伪函数可以使用 `return_val` 设置返回值。**存在输出参数时，必须通过 `custom_fake` 提供自定义伪函数来驱动输出**，因为只设置 `return_val` 不会触碰输出参数。例如，让读取函数返回成功并不会自动把所需测试数据写入调用者缓冲区。

启用Kconfig配置项 [`CONFIG_ZTEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST) 时，Zephyr测试框架ztest会通过测试规则在每个测试用例之前重置全部伪函数。

[`fake_eeprom_read()`](https://docs.zephyrproject.org/latest/doxygen/html/group__eeprom__fake.html#ga6238da3c648ca23d4be16853feee071d) 和 [`fake_eeprom_size()`](https://docs.zephyrproject.org/latest/doxygen/html/group__eeprom__fake.html#ga0afb1c3d28fe1f0883c7a7c744edc5d8) 默认安装了自定义伪函数：遵守设备树中的容量设置，并将读出的数据填零。每次重置后都会重新安装这些默认实现；需要改变报告结果或读取内容时，应在当前测试用例中安装自己的 `custom_fake`。

## 51.3\_检查写入调用

> 译注——默认实现的验证范围：本次核对的官方 `eeprom_fake.c` 中，默认读取只检查 `len` 是否大于设备树容量，然后将输出填零；它没有检查 `offset`、`offset + len` 或数据指针。默认写入也不维护可以再次读出的存储内容。验证越界、写后读或实际存储行为时，应设置针对该场景的 `custom_fake`；仅观察返回成功不构成这些行为已验证的证据。相对源码见 [eeprom_fake.c](../../../drivers/eeprom/eeprom_fake.c)，本次官方快照及说明见[伪EEPROM头文件参考](../flash_reference/P023_伪EEPROM头文件参考.md)。

下面是官方测试代码片段，仅清理HTML代码展示中的行末空格，悬浮定义说明移至代码后的正文。它通过设备树节点标签 `fake_eeprom` 取得设备，调用公共写入接口，再检查调用次数和捕获参数。这是测试用例内部的C代码，不是终端命令，也不表示对真实EEPROM写入。

```c
const struct device *dev = DEVICE_DT_GET(DT_NODELABEL(fake_eeprom));
const uint8_t data[] = {0x01, 0x02};

zassert_ok(eeprom_write(dev, 8, data, sizeof(data)));

zassert_equal(1, fake_eeprom_write_fake.call_count);
zassert_equal(dev, fake_eeprom_write_fake.arg0_val);
zassert_equal(8, fake_eeprom_write_fake.arg1_val);
zassert_equal(sizeof(data), fake_eeprom_write_fake.arg3_val);
```

代码从偏移8写入两字节数据，随后验证 `fake_eeprom_write_fake.call_count` 为1，`arg0_val` 为设备，`arg1_val` 为偏移，`arg3_val` 为写入长度。参数编号从0开始；原代码没有在这里检查第三个参数所指数据内容，不能把这几项断言解释成全部数据均已验证。

其中 [`DEVICE_DT_GET()`](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7) 从设备树节点标识取得设备引用，[`DT_NODELABEL()`](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79) 根据节点标签取得节点标识；[`zassert_ok()`](P503_ZTest断言宏.md) 断言返回值为0，[`zassert_equal()`](P503_ZTest断言宏.md) 断言两值相等。[`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) 是8位无符号整数类型，`struct device` 是每个驱动实例位于 **只读存储器（Read-Only Memory，ROM）**中的运行时设备结构，其 [`data`](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e) 字段指向设备实例私有数据。上述说明对应原页代码辅助提示中的定义。

## 51.4\_伪函数参考

以下声明按原页保留匿名参数，参数位置与[EEPROM公共接口](P040_EEPROM接口参考.md)一致。

<a id="ga6238da3c648ca23d4be16853feee071d"></a>
<a id="r_ga6238da3c648ca23d4be16853feee071d"></a>
<a id="ga0afb1c3d28fe1f0883c7a7c744edc5d8"></a>
<a id="r_ga0afb1c3d28fe1f0883c7a7c744edc5d8"></a>
<a id="ga2484447bd0c4d5d43a56fd42a893de61"></a>
<a id="r_ga2484447bd0c4d5d43a56fd42a893de61"></a>

```c
int fake_eeprom_read(const struct device *, off_t, void *, size_t);
int fake_eeprom_write(const struct device *, off_t, const void *, size_t);
size_t fake_eeprom_size(const struct device *);
```

| 函数 | 对应的驱动操作 |
| --- | --- |
| [`fake_eeprom_read()`](https://docs.zephyrproject.org/latest/doxygen/html/group__eeprom__fake.html#ga6238da3c648ca23d4be16853feee071d) | [`eeprom_driver_api::read`](P054_EEPROM驱动操作结构.md) 的伪实现。 |
| [`fake_eeprom_write()`](https://docs.zephyrproject.org/latest/doxygen/html/group__eeprom__fake.html#ga2484447bd0c4d5d43a56fd42a893de61) | [`eeprom_driver_api::write`](P054_EEPROM驱动操作结构.md) 的伪实现。 |
| [`fake_eeprom_size()`](https://docs.zephyrproject.org/latest/doxygen/html/group__eeprom__fake.html#ga0afb1c3d28fe1f0883c7a7c744edc5d8) | [`eeprom_driver_api::size`](P054_EEPROM驱动操作结构.md) 的伪实现。 |

本章翻译没有执行这些测试、修改伪函数状态或访问实际存储硬件。

[上一章：CAN收发器驱动后端接口](P050_CAN收发器驱动后端接口.md) · [下一章：CRC驱动操作结构](P052_CRC驱动操作结构.md) · [返回大纲](大纲.md)
