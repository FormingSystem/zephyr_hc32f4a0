---
id: learning.zephyr-docs.audio-stm32-ti-wolfson-binding-reference.page-16
title: zephyr_pdm-dmic
kind: reference
status: maintained
domains: [zephyr, devicetree, audio]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/audio/zephyr,pdm-dmic.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第16章\_zephyr_pdm-dmic

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/audio/zephyr,pdm-dmic.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="zephyr-pdm-dmic"></a>
<a id="dtbinding-zephyr-pdm-dmic"></a>
<a id="std-dtcompatible-zephyr-pdm-dmic"></a>

兼容字符串（Compatible String）：`zephyr,pdm-dmic`。厂商：[ Zephyr ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,pdm-dmic)。

<a id="description"></a>

通用数字麦克风（Generic Digital Microphone）配置。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 16.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `clk-frequency-min` | `int` | **必需**。PDM时钟引脚的最低频率（Minimum Frequency） |
| `clk-frequency-max` | `int` | **必需**。PDM时钟引脚的最高频率（Maximum Frequency） |
| `clk-duty-cycle-min` | `int` | **必需**。PDM时钟引脚的最小占空比（Minimum Duty Cycle） |
| `clk-duty-cycle-max` | `int` | **必需**。PDM时钟引脚的最大占空比（Maximum Duty Cycle） |
| `channel-left` | `boolean` | 存在左PDM通道（Left PDM Channel） |
| `channel-right` | `boolean` | 存在右PDM通道（Right PDM Channel） |

本页没有已弃用的节点专用属性。

---

[上一章](P015_zephyr_native-sim-dmic.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md)
