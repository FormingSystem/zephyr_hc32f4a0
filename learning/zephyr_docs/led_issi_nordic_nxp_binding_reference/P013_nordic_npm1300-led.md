---
id: learning.zephyr-docs.led-issi-nordic-nxp-binding-reference.page-13
title: nordic_npm1300-led
kind: reference
status: maintained
domains: [zephyr, devicetree, led]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/led/nordic,npm1300-led.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第13章\_nordic_npm1300-led

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/led/nordic,npm1300-led.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nordic-npm1300-led"></a>
<a id="dtbinding-nordic-npm1300-led"></a>
<a id="std-dtcompatible-nordic-npm1300-led"></a>

兼容字符串（Compatible String）：`nordic,npm1300-led`。厂商：[ Nordic Semiconductor ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nordic)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nordic,npm1300-led)。

驱动源码（Driver Source）：[drivers/led/led_npm13xx.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/led_npm13xx.c)。

<a id="description"></a>

Nordic nPM1300 LED控制器（LED Controller）。

nPM1300提供三个LED输出。每个LED都可以自动显示错误或充电状态，也可以由软件控制。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 13.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `nordic,led0-mode` | `string` | **必需**。LED 0工作模式（Mode）。；合法值：`error, charging, host` |
| `nordic,led1-mode` | `string` | **必需**。LED 1工作模式（Mode）。；合法值：`error, charging, host` |
| `nordic,led2-mode` | `string` | **必需**。LED 2工作模式（Mode）。；合法值：`error, charging, host` |

本页没有已弃用的节点专用属性。

---

[上一章](P012_nordic_npm10xx-led.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P014_nordic_npm1304-led.md)
