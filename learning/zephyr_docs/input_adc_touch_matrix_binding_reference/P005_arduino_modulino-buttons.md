---
id: learning.zephyr-docs.input-adc-touch-matrix-binding-reference.page-5
title: arduino_modulino-buttons
kind: reference
status: maintained
domains: [zephyr, devicetree, input]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/input/arduino,modulino-buttons.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第5章\_arduino_modulino-buttons

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/input/arduino,modulino-buttons.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="arduino-modulino-buttons"></a>
<a id="dtbinding-arduino-modulino-buttons"></a>
<a id="std-dtcompatible-arduino-modulino-buttons"></a>

兼容字符串（Compatible String）：`arduino,modulino-buttons`。厂商：[ Arduino ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-arduino)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=arduino,modulino-buttons)。

驱动源码（Driver Source）：[drivers/input/input_modulino_buttons.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/input_modulino_buttons.c)。

<a id="description"></a>

Arduino Modulino按键模块（Buttons）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 5.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `zephyr,codes` | `array` | **必需**。要上报的按键码（Key Codes）。模块有三个按键，因此必须指定三个按键码。；范围：`0 to 65535`；长度范围：`3 to 3` |
| `poll-period-ms` | `int` | 通过I²C总线轮询按键的间隔（Poll Interval），默认为50 ms。；默认值：`50` |

本页没有已弃用的节点专用属性。

---

[上一章](P004_analog-axis.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P006_bflb_irx.md)
