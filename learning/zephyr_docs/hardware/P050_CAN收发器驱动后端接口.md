---
id: learning.zephyr-docs.hardware.backend-4
title: CAN收发器驱动后端接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__can__transceiver__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第50章\_CAN收发器驱动后端接口

原文：[group__can__transceiver__backend](https://docs.zephyrproject.org/latest/doxygen/html/group__can__transceiver__backend.html)。读取日期：2026-10-13，`latest`。

## 50.1\_收发器驱动操作

本组提供实现 **控制器局域网（Controller Area Network，CAN）** **收发器（Transceiver）**驱动所需的 **应用程序编程接口（Application Programming Interface，API）**类型、回调签名和辅助内容。官方头文件为 `zephyr/drivers/can/transceiver.h`。

`struct can_transceiver_driver_api` 是CAN收发器驱动操作结构，见[结构参考](P055_CAN收发器操作结构.md)。驱动提供下述 **回调函数（Callback Function）**，分别实现启用与禁用动作。

## 50.2\_启用和禁用回调

```c
typedef int (*can_transceiver_enable_t)(const struct device *dev,
                                        can_mode_t mode);
typedef int (*can_transceiver_disable_t)(const struct device *dev);
```

| 回调类型 | 作用 | 原文参数说明入口 |
| --- | --- | --- |
| <a id="gac9de770d729b6427979d83b2904f07cf"></a>[`can_transceiver_enable_t`](P050_CAN收发器驱动后端接口.md) | 启用CAN收发器。 | [`can_transceiver_enable()`](P041_CAN收发器接口参考.md)。 |
| <a id="gacc56ddc312a7205bfadb9b612372b89c"></a>[`can_transceiver_disable_t`](P050_CAN收发器驱动后端接口.md) | 禁用CAN收发器。 | [`can_transceiver_disable()`](P041_CAN收发器接口参考.md)。 |

两者的 `dev` 均指向驱动实例的设备结构；启用回调的 `mode` 表示工作模式。公共接口成功返回0，一般输入／输出故障返回 `-EIO`，见[CAN收发器接口参考](P041_CAN收发器接口参考.md)。

该公共接口文档还说明：收发器通常由CAN控制器驱动管理，应用不应直接控制。实现后端回调并不会取消这一调用关系。

[上一章：EEPROM驱动后端接口](P049_EEPROM驱动后端接口.md) · [下一章：伪EEPROM接口](P051_伪EEPROM接口.md) · [返回大纲](大纲.md)
