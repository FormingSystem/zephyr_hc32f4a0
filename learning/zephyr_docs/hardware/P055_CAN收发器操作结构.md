---
id: learning.zephyr-docs.hardware.ops-3
title: CAN收发器操作结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcan__transceiver__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第55章\_CAN收发器操作结构

原文：[structcan__transceiver__driver__api](https://docs.zephyrproject.org/latest/doxygen/html/structcan__transceiver__driver__api.html)。读取日期：2026-10-13，`latest`。

## 55.1\_驱动操作结构

`struct can_transceiver_driver_api` 是**控制器局域网（Controller Area Network，CAN）** **收发器（Transceiver）**驱动必须定义的 **应用程序编程接口（Application Programming Interface，API）**结构。它保存指向驱动已实现操作的函数指针，以及驱动特定的其他常量数据。官方声明所在头文件为 `zephyr/drivers/can/transceiver.h`，本页参考由该文件生成。

原文以 **必需项（Required，REQ）**与 **可选项（Optional，OPT）**标记字段。标为REQ的成员**必须由驱动设置**；标为OPT的成员可以不实现。下表保留每个字段实际标记，而非把所有操作统一视为可选。

## 55.2\_操作字段

| 字段 | 函数指针类型 | 要求 | 作用 |
| --- | --- | --- | --- |
| <a id="afbf86ddecfcc818a9c84dd6fd0807505"></a>[`enable`](P055_CAN收发器操作结构.md) | [`can_transceiver_enable_t`](P050_CAN收发器驱动后端接口.md) | REQ | 启用CAN收发器。 |
| <a id="ab28e2f8f1bbf96942349e1ae0b352d68"></a>[`disable`](P055_CAN收发器操作结构.md) | [`can_transceiver_disable_t`](P050_CAN收发器驱动后端接口.md) | REQ | 禁用CAN收发器。 |

两个操作均为必需项。上层公共接口仍遵守由CAN控制器驱动管理收发器的约束，见[CAN收发器接口参考](P041_CAN收发器接口参考.md)；操作表的存在不意味着应用应绕过控制器直接修改收发器。

这些字段的参数签名与公共接口的对应关系，见[驱动后端接口](P050_CAN收发器驱动后端接口.md)。原页的逐字段参考与上表一致，没有另外给出字段默认值。

## 55.3\_相关设备定义入口

原页还指向 [`DEVICE_DT_INST_DEFINE()`](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)、[`DEVICE_DT_DEFINE()`](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1) 与 [`DEVICE_API()`](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)。前两个宏用于依据设备树定义设备实例，后一个宏用于定义驱动API对象；它们把设备实例与操作结构关联起来。这里保留官方精确链接，具体参数以对应宏参考为准。

[上一章：EEPROM驱动操作结构](P054_EEPROM驱动操作结构.md) · [下一章：存储外设入口](P056_存储外设入口.md) · [返回大纲](大纲.md)
