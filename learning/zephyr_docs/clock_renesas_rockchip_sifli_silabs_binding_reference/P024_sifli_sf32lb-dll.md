---
id: learning.zephyr-docs.clock-renesas-rockchip-sifli-silabs-binding-reference.page-24
title: sifli_sf32lb-dll
kind: reference
status: maintained
domains: [zephyr, devicetree, clock]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/sifli,sf32lb-dll.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第24章\_sifli_sf32lb-dll

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/sifli,sf32lb-dll.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="sifli-sf32lb-dll"></a>
<a id="dtbinding-sifli-sf32lb-dll"></a>
<a id="std-dtcompatible-sifli-sf32lb-dll"></a>

兼容字符串（Compatible String）：`sifli,sf32lb-dll`。厂商：[ SiFli Technologies ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-sifli)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=sifli,sf32lb-dll)。

<a id="description"></a>

SiFli DLL是由RCC控制的数字锁相环外设（Digital Phase-Locked Loop），可作为系统及外设的时钟源。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 24.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `clock-frequency` | `int` | **必需**。时钟输出频率（Clock Output Frequency），单位Hz。 |

本页没有已弃用的节点专用属性。

---

[上一章](P023_rockchip_rk3588-cru.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P025_sifli_sf32lb-hxt48.md)
