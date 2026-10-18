---
id: learning.zephyr-docs.clock-renesas-rockchip-sifli-silabs-binding-reference.page-20
title: renesas_smartbond-lp-osc
kind: reference
status: maintained
domains: [zephyr, devicetree, clock]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/renesas,smartbond-lp-osc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第20章\_renesas_smartbond-lp-osc

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/renesas,smartbond-lp-osc.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="renesas-smartbond-lp-osc"></a>
<a id="dtbinding-renesas-smartbond-lp-osc"></a>
<a id="std-dtcompatible-renesas-smartbond-lp-osc"></a>

兼容字符串（Compatible String）：`renesas,smartbond-lp-osc`。厂商：[ Renesas Electronics Corporation ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-renesas)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=renesas,smartbond-lp-osc)。

<a id="description"></a>

Smartbond低功耗振荡器（Low Power Oscillator）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 20.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `settle-time` | `int` | 仅适用于XTAL32K：其达到稳定（Settle）所需时间，单位毫秒。；默认值：`8000` |
| `calibration-interval` | `int` | 振荡器校准（Oscillator Calibration）之间的时间间隔，单位毫秒。设为0完全禁用校准。仅应在要求严格线程调度的测试中禁用，因为这些测试可能因校准产生的微小、非预期CPU占用而失败。；默认值：`1000` |
| `clock-frequency` | `int` | **必需**。输出时钟频率（Output Clock Frequency），单位Hz。 |

本页没有已弃用的节点专用属性。

## 20.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |

属性说明中的“重要属性”参见[设备树语法与结构](../devicetree/P003_语法与结构.md#dt-important-props)。

---

[上一章](P019_renesas_smartbond-lp-clk.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P021_renesas_smartbond-sys-clk.md)
