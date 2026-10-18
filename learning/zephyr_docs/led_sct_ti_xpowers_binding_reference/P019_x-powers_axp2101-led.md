---
id: learning.zephyr-docs.led-sct-ti-xpowers-binding-reference.page-19
title: x-powers_axp2101-led
kind: reference
status: maintained
domains: [zephyr, devicetree, led]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/led/x-powers,axp2101-led.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第19章\_x-powers_axp2101-led

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/led/x-powers,axp2101-led.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="x-powers-axp2101-led-on-axp2101-bus"></a>
<a id="dtbinding-x-powers-axp2101-led"></a>
<a id="std-dtcompatible-x-powers-axp2101-led"></a>

兼容字符串（Compatible String）：`x-powers,axp2101-led`。厂商：[ X-Powers ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-x-powers)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=x-powers,axp2101-led)。

<a id="description"></a>

AXP2101 LED控制器（LED Controller）。

AXP2101有一个LED，可自动显示错误或充电状态，也可由软件控制。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 19.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `x-powers,mode` | `string` | 选择LED控制方式（Control Method）。选择 `by-reg` 时可通过软件控制；`type-a` 和 `type-b` 的详情请参阅数据手册（Datasheet）。；合法值：`type-a, type-b, by-reg` |

本页没有已弃用的节点专用属性。

---

[上一章](P018_x-powers_axp192-led.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P020_zephyr_native-linux-leds.md)
