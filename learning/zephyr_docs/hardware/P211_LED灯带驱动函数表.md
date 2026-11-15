---
id: learning.zephyr-docs.hardware.stripapi-3
title: LED灯带驱动函数表
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structled__strip__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第211章\_LED灯带驱动函数表

原文：[structled__strip__driver__api](https://docs.zephyrproject.org/latest/doxygen/html/structled__strip__driver__api.html)。读取日期：2026-10-13，`latest`。

## 211.1\_用途与成员要求

[`led_strip_driver_api`](https://docs.zephyrproject.org/latest/doxygen/html/structled__strip__driver__api.html) 是所有 **发光二极管灯带（Light-Emitting Diode Strip，LED Strip）**驱动都需要定义的 **驱动操作（Driver Operations）**结构。它包含驱动已实现操作的函数指针，以及驱动接口需要的其他特定常量数据，定义来自官方头文件 `zephyr/drivers/led_strip.h`。

标为 **必需（Required，REQ）**的成员必须由驱动设置；标为 **可选（Optional，OPT）**的成员按需要提供。RGB 表示红、绿、蓝（Red, Green, Blue）。

## 211.2\_数据字段（Data Fields）

| 字段 | 类型 | 要求 | 含义 |
| --- | --- | --- | --- |
| [`update_rgb`](https://docs.zephyrproject.org/latest/doxygen/html/structled__strip__driver__api.html#af0f7a73d61589355b520f76073013425) | [`led_api_update_rgb`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface__backend.html#gaa36be40a962173021a547192d0d39151) | REQ | 用给定 RGB 数组更新灯带。 |
| [`length`](https://docs.zephyrproject.org/latest/doxygen/html/structled__strip__driver__api.html#a083406f6a5b5ce034268315b7075d671) | [`led_api_length`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface__backend.html#ga3487e5d4a339898f88a225bb3678776b) | REQ | 返回灯带级联长度（Chain Length），单位为像素。 |
| [`update_channels`](https://docs.zephyrproject.org/latest/doxygen/html/structled__strip__driver__api.html#ad5969b78c4b77d570669abd5143ec228) | [`led_api_update_channels`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface__backend.html#gab11579a7b5b7febfd48fa12560254501) | OPT | 用给定通道数组更新灯带。 |

各回调签名见[灯带后端接口](P210_LED灯带后端接口.md)。

## 211.3\_相关定义宏

原页关联的设备及接口定义宏包括 [`DEVICE_DT_INST_DEFINE()`](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)、[`DEVICE_DT_DEFINE()`](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1) 和 [`DEVICE_API()`](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)。


---

[上一章：LED灯带后端接口](P210_LED灯带后端接口.md) · [下一章：LED灯带扩展接口目录](P212_LED灯带扩展接口目录.md) · [返回大纲](大纲.md)
