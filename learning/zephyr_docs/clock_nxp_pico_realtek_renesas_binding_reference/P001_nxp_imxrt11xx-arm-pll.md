---
id: learning.zephyr-docs.clock-nxp-pico-realtek-renesas-binding-reference.page-1
title: nxp_imxrt11xx-arm-pll
kind: reference
status: maintained
domains: [zephyr, devicetree, clock]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/nxp,imxrt11xx-arm-pll.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第1章\_nxp_imxrt11xx-arm-pll

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/nxp,imxrt11xx-arm-pll.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nxp-imxrt11xx-arm-pll"></a>
<a id="dtbinding-nxp-imxrt11xx-arm-pll"></a>
<a id="std-dtcompatible-nxp-imxrt11xx-arm-pll"></a>

兼容字符串（Compatible String）：`nxp,imxrt11xx-arm-pll`。厂商：[ NXP Semiconductors ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nxp)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nxp,imxrt11xx-arm-pll)。

<a id="description"></a>

i.MX RT11xx ARM锁相环（PLL）时钟提供者（Clock Provider）。新设备树应通过loop-div和post-div配置ARM PLL。旧属性clock-mult和clock-div仍为兼容性保留，但已弃用（Deprecated）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 1.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `#clock-cells` | `int` | **必需**。时钟说明符（Clock Specifier）中预期的条目数量。；固定值：`0` |
| `loop-div` | `int` | ARM PLL环路分频器（Loop Divider）。；范围：`104 to 208` |
| `post-div` | `int` | ARM PLL后分频器（Post Divider）。；合法值：`1, 2, 4, 8` |

### 已弃用的节点专用属性（Deprecated Properties）

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `clock-div` | `int` | 已弃用（Deprecated），改用post-div。 |
| `clock-mult` | `int` | 已弃用（Deprecated），改用loop-div。旧属性表示硬件环路分频值的一半，因此 `loop-div = clock-mult * 2`。 |

---

[本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P002_nxp_kinetis-ke1xf-sim.md)
