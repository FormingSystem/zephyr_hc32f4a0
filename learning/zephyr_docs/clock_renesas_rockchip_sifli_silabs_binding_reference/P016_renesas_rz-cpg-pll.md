---
id: learning.zephyr-docs.clock-renesas-rockchip-sifli-silabs-binding-reference.page-16
title: renesas_rz-cpg-pll
kind: reference
status: maintained
domains: [zephyr, devicetree, clock]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/renesas,rz-cpg-pll.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第16章\_renesas_rz-cpg-pll

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/renesas,rz-cpg-pll.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="renesas-rz-cpg-pll"></a>
<a id="dtbinding-renesas-rz-cpg-pll"></a>
<a id="std-dtcompatible-renesas-rz-cpg-pll"></a>

兼容字符串（Compatible String）：`renesas,rz-cpg-pll`。厂商：[ Renesas Electronics Corporation ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-renesas)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=renesas,rz-cpg-pll)。

<a id="description"></a>

Renesas RZ时钟脉冲发生器（Clock Pulse Generator）的PLL输出。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 16.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `clock-frequency` | `int` | **必需**。PLL输出时钟频率（Output Clock Frequency），单位Hz。 |
| `#clock-cells` | `int` | **必需**。时钟说明符（Clock Specifier）中预期的条目数量。；固定值：`1` |

本页没有已弃用的节点专用属性。

<a id="specifier-cell-names"></a>

## 说明符单元名称

clock cells：`postscaler`。依次为后分频器。

---

[上一章](P015_renesas_rz-cpg-clock.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P017_renesas_rz-cpg.md)
