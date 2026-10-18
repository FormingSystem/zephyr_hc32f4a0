---
id: learning.zephyr-docs.clock-esp-infineon-microchip-binding-reference.page-18
title: mediatek_mt8195_cpuclk
kind: reference
status: maintained
domains: [zephyr, devicetree, clock]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/mediatek,mt8195_cpuclk.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第18章\_mediatek_mt8195_cpuclk

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/mediatek,mt8195_cpuclk.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="mediatek-mt8195-cpuclk"></a>
<a id="dtbinding-mediatek-mt8195-cpuclk"></a>
<a id="std-dtcompatible-mediatek-mt8195_cpuclk"></a>

兼容字符串（Compatible String）：`mediatek,mt8195_cpuclk`。厂商：[ MediaTek Inc. ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-mediatek)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=mediatek,mt8195_cpuclk)。

<a id="description"></a>

MediaTek音频DSP处理器频率控制（CPU Frequency Control）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 18.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `freqs-mhz` | `array` | **必需**。按升序排列的可用频率（Available Frequencies）。 |
| `cg-reg` | `int` | 原文没有提供文字说明 |
| `pll-ctrl-reg` | `int` | 原文没有提供文字说明 |

本页没有已弃用的节点专用属性。

## 18.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | 原文没有提供文字说明 |

属性说明中的“重要属性”参见[设备树语法与结构](../devicetree/P003_语法与结构.md#dt-important-props)。

---

[上一章](P017_mediatek_mt818x_cpuclk.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P019_microchip_sam-pmc.md)
