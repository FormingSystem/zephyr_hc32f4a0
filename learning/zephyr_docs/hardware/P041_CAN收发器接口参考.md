---
id: learning.zephyr-docs.hardware.hwapi-can-transceiver
title: CAN收发器接口参考
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__can__transceiver.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第41章\_CAN收发器接口参考

原文：[group__can__transceiver](https://docs.zephyrproject.org/latest/doxygen/html/group__can__transceiver.html)。读取日期：2026-10-13，`latest`。

## 41.1\_接口职责与版本

**控制器局域网（Controller Area Network，CAN）**的 **收发器（Transceiver）**负责连接控制器逻辑信号与物理总线，原理见[CAN收发器](P031_CAN收发器.md)。本页是其 **应用程序编程接口（Application Programming Interface，API）**参考，接口自Zephyr 3.1引入，版本为0.1.0；官方头文件为 `zephyr/drivers/can/transceiver.h`。驱动实现者还可阅读[CAN收发器驱动后端API](P050_CAN收发器驱动后端接口.md)。

**收发器应由CAN控制器驱动管理，应用程序通常不应直接控制它。** 原文在启用和禁用两个函数下均强调这一点，并分别指向控制器的 [`can_start()`](P362_CAN控制器接口.md) 与 [`can_stop()`](P362_CAN控制器接口.md)。应用层调用关系见[CAN控制器](P030_CAN控制器.md)。

## 41.2\_启用收发器

<a id="ga0d0e87150b49198c41e2782a17cfd694"></a>

[`can_transceiver_enable()`](P041_CAN收发器接口参考.md) 启用收发器：

```c
static inline int can_transceiver_enable(const struct device *dev,
                                         can_mode_t mode);
```

`dev` 为CAN收发器驱动实例指针，`mode` 为CAN工作模式。成功返回0；一般 **输入／输出（Input/Output，I/O）**故障返回 `-EIO`。普通应用应通过 `can_start()` 启动控制器，由控制器驱动协调收发器。

## 41.3\_禁用收发器

<a id="ga7509ca0b6ece81b4038b7d128af961be"></a>

[`can_transceiver_disable()`](P041_CAN收发器接口参考.md) 禁用收发器：

```c
static inline int can_transceiver_disable(const struct device *dev);
```

`dev` 为CAN收发器驱动实例指针。成功返回0；禁用时的一般I/O故障返回 `-EIO`。普通应用应通过 `can_stop()` 停止控制器，由控制器驱动处理收发器状态。

[上一章：EEPROM接口参考](P040_EEPROM接口参考.md) · [下一章：CRC校验示例](P042_CRC校验示例.md) · [返回大纲](大纲.md)
