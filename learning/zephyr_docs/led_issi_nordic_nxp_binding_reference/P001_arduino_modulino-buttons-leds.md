---
id: learning.zephyr-docs.led-issi-nordic-nxp-binding-reference.page-1
title: arduino_modulino-buttons-leds
kind: reference
status: maintained
domains: [zephyr, devicetree, led]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/led/arduino,modulino-buttons-leds.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第1章\_arduino_modulino-buttons-leds

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/led/arduino,modulino-buttons-leds.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="arduino-modulino-buttons-leds"></a>
<a id="dtbinding-arduino-modulino-buttons-leds"></a>
<a id="std-dtcompatible-arduino-modulino-buttons-leds"></a>

兼容字符串（Compatible String）：`arduino,modulino-buttons-leds`。厂商：[ Arduino ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-arduino)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=arduino,modulino-buttons-leds)。

驱动源码（Driver Source）：[drivers/led/modulino_buttons_leds.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/modulino_buttons_leds.c)。

<a id="description"></a>

Arduino Modulino按键模块的发光二极管（Light-Emitting Diode，LED）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 1.1\_节点专用属性

这些属性不继承自基础绑定文件。

本页没有节点专用属性。

本页没有已弃用的节点专用属性。

---

[本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P002_awinic_aw9523b-led.md)
