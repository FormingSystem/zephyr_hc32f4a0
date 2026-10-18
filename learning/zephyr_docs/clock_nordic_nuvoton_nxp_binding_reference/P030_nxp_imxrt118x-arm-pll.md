---
id: learning.zephyr-docs.clock-nordic-nuvoton-nxp-binding-reference.page-30
title: nxp_imxrt118x-arm-pll
kind: reference
status: maintained
domains: [zephyr, devicetree, clock]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/nxp,imxrt118x-arm-pll.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第30章\_nxp_imxrt118x-arm-pll

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/nxp,imxrt118x-arm-pll.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nxp-imxrt118x-arm-pll"></a>
<a id="dtbinding-nxp-imxrt118x-arm-pll"></a>
<a id="std-dtcompatible-nxp-imxrt118x-arm-pll"></a>

兼容字符串（Compatible String）：`nxp,imxrt118x-arm-pll`。厂商：[ NXP Semiconductors ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nxp)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nxp,imxrt118x-arm-pll)。

<a id="description"></a>

i.MX RT118x ARM锁相环（PLL）时钟提供者（Clock Provider）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 30.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `loop-div` | `int` | **必需**。ARM PLL环路分频器（Loop Divider）。；范围：`104 to 208` |
| `post-div` | `int` | **必需**。ARM PLL后分频器（Post Divider）。；合法值：`1, 2, 4, 8` |
| `#clock-cells` | `int` | **必需**。时钟说明符（Clock Specifier）中预期的条目数量。；固定值：`0` |

本页没有已弃用的节点专用属性。

---

[上一章](P029_nxp_imx9-pll.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md)
