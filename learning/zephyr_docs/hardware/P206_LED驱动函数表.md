---
id: learning.zephyr-docs.hardware.ledbackend-1
title: LED驱动函数表
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第206章\_LED驱动函数表

原文：[structled__driver__api](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html)。读取日期：2026-10-13，`latest`。

## 206.1\_用途与最低实现要求

[`led_driver_api`](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html) 是 **发光二极管（Light-Emitting Diode，LED）**驱动必须定义的 **驱动操作（Driver Operations）**结构。它保存驱动已实现操作的函数指针，以及驱动接口需要的其他特定常量数据；定义来自官方头文件 `zephyr/drivers/led.h`。

原文的标记约定为：**必需（Required，REQ）**成员必须由驱动设置，**可选（Optional，OPT）**成员按需要提供。本结构的七个字段都标为 OPT，但存在以下最低实现要求：

- 实现 [`set_brightness`](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#a9c3e3c4d40c4b8219755df6df96b0058)；或者
- 同时实现 [`on`](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#a9ce7322282f8c525256d3c16a514ecc4) 和 [`off`](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#a19ad736a130da2aff6bd5b299d8c33a7)。

子系统会利用已提供的操作模拟缺少的对应操作。因此，没有亮度设置时，点亮和关闭都必须实现；没有实现开关操作时，必须提供亮度设置。

## 206.2\_数据字段（Data Fields）

| 字段 | 函数指针类型 | 标记 | 操作及条件 |
| --- | --- | --- | --- |
| `on` | [`led_api_on`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#gad13f55702668133575658d2ccc295339) | OPT | 点亮 LED；未实现 `set_brightness` 时必须提供。 |
| `off` | [`led_api_off`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#ga5ae67fe64f97b0e716f9eb2f3a34f1fd) | OPT | 关闭 LED；未实现 `set_brightness` 时必须提供。 |
| `set_brightness` | [`led_api_set_brightness`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#gae24caa14f6aa41c2a509d2eaf468463f) | OPT | 设置亮度；没有实现 `on` 和 `off` 时必须提供。 |
| [`blink`](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#af1974c5cc20c818e0e387b34cd14ac3b) | [`led_api_blink`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#gad3c655794f58045459cbd910592d2cdd) | OPT | 闪烁 LED。 |
| [`get_info`](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#a7c68219e44bcf6e766e64fd3967ecf7e) | [`led_api_get_info`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#ga3828b1e544a2f64378d5c3bfbbaa0c77) | OPT | 获取 LED 信息。 |
| [`set_color`](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#a336f30f2c1bd3d99213cae66911c142a) | [`led_api_set_color`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#ga977317f3208d5336463edf9979def4ae) | OPT | 设置 LED 颜色。 |
| [`write_channels`](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#ada1dfb1830b48afb020c7e60dbd92337) | [`led_api_write_channels`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#ga66dac12510c3a2281378d532ba6db2ae) | OPT | 写入或更新一段连续 LED 通道（Channel）。 |

各类型的完整签名见[LED驱动后端接口](P205_LED驱动后端接口.md)。

## 206.3\_相关定义宏

原页关联的设备及接口定义宏包括 [`DEVICE_DT_INST_DEFINE()`](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)、[`DEVICE_DT_DEFINE()`](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1) 和 [`DEVICE_API()`](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)。

[上一章：LED驱动后端接口](P205_LED驱动后端接口.md) · [下一章：模拟LED控制器](P207_模拟LED控制器.md) · [返回大纲](大纲.md)
