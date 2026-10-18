---
id: learning.zephyr-docs.misc-adi-nordic-binding-reference.page-22
title: nuvoton_npcx-booter-variant
kind: reference
status: maintained
domains: [zephyr, devicetree, peripherals]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/misc/nuvoton,npcx-booter-variant.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第22章\_nuvoton_npcx-booter-variant

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/misc/nuvoton,npcx-booter-variant.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nuvoton-npcx-booter-variant"></a>
<a id="dtbinding-nuvoton-npcx-booter-variant"></a>
<a id="std-dtcompatible-nuvoton-npcx-booter-variant"></a>

兼容字符串（Compatible String）：`nuvoton,npcx-booter-variant`。厂商：[ Nuvoton Technology Corporation ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nuvoton)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nuvoton,npcx-booter-variant)。

<a id="description"></a>

Nuvoton NPCX启动程序变体选项（Booter Variant Options）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 22.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `hif-type-auto` | `boolean` | 为真时，由启动程序（Booter）配置主机接口类型（LPC/eSPI/SHI）；否则应由固件（Firmware）配置。 |

本页没有已弃用的节点专用属性。

---

[上一章](P021_nordic_nrf-ppib.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P023_nuvoton_npcx-soc-id.md)
