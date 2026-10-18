---
id: learning.zephyr-docs.clock-esp-infineon-microchip-binding-reference.page-10
title: intel_adsp-shim-clkctl
kind: reference
status: maintained
domains: [zephyr, devicetree, clock]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/intel,adsp-shim-clkctl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第10章\_intel_adsp-shim-clkctl

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/intel,adsp-shim-clkctl.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="intel-adsp-shim-clkctl"></a>
<a id="dtbinding-intel-adsp-shim-clkctl"></a>
<a id="std-dtcompatible-intel-adsp-shim-clkctl"></a>

兼容字符串（Compatible String）：`intel,adsp-shim-clkctl`。厂商：[ Intel Corporation ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-intel)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=intel,adsp-shim-clkctl)。

<a id="description"></a>

Intel音频DSP时钟控制（Clock Control）相关常量。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 10.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `adsp-clkctl-clk-wovcro` | `int` | 编码数组中WOVCRO时钟编码的索引，仅当 `wovcro-supported` 为真时使用。 |
| `adsp-clkctl-clk-lpro` | `int` | 编码数组中低功耗环形振荡器（Low-Power Ring Oscillator，LPRO）时钟编码的索引。 |
| `adsp-clkctl-clk-hpro` | `int` | 编码数组中高功率环形振荡器（High-Power Ring Oscillator，HPRO）时钟编码的索引。 |
| `adsp-clkctl-clk-ipll` | `int` | 编码数组中ACE集成PLL时钟编码的索引。 |
| `adsp-clkctl-freq-enc` | `array` | **必需**。编码各时钟启用所需值的数组（Encoding Array）。 |
| `adsp-clkctl-freq-mask` | `array` | 编码各时钟启用所需掩码的数组（Mask Array）。 |
| `adsp-clkctl-freq-default` | `int` | **必需**。默认时钟索引（Default Clock Index）。 |
| `adsp-clkctl-freq-lowest` | `int` | **必需**。最低频率时钟索引（Lowest-Frequency Clock Index）。 |
| `wovcro-supported` | `boolean` | 是否支持语音唤醒（Wake on Voice，WoV）时钟环形振荡器。 |

本页没有已弃用的节点专用属性。

---

[上一章](P009_infineon_peri-div.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P011_intel_agilex-clock.md)
