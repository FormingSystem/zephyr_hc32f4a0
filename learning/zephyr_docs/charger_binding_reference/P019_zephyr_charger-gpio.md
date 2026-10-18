---
id: learning.zephyr-docs.charger-binding-reference.page-19
title: zephyr_charger-gpio
kind: reference
status: maintained
domains: [zephyr, devicetree, power]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/charger/zephyr,charger-gpio.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第19章\_zephyr_charger-gpio

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/charger/zephyr,charger-gpio.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="zephyr-charger-gpio"></a>
<a id="dtbinding-zephyr-charger-gpio"></a>
<a id="std-dtcompatible-zephyr-charger-gpio"></a>

兼容字符串（Compatible String）：`zephyr,charger-gpio`。厂商：[ Zephyr ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,charger-gpio)。

驱动源码（Driver Source）：[drivers/charger/charger_gpio.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/charger/charger_gpio.c)。

<a id="description"></a>

由GPIO控制的充电状态（Charging State）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 19.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `ctrl-gpios` | `phandle-array` | 控制充电状态的引脚，处于有效状态时使能充电 |

本页没有已弃用的节点专用属性。

---

[上一章](P018_x-powers_axp2101-charger.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md)
