---
id: learning.zephyr-docs.misc-adi-nordic-binding-reference.page-23
title: nuvoton_npcx-soc-id
kind: reference
status: maintained
domains: [zephyr, devicetree, peripherals]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/misc/nuvoton,npcx-soc-id.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第23章\_nuvoton_npcx-soc-id

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/misc/nuvoton,npcx-soc-id.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nuvoton-npcx-soc-id"></a>
<a id="dtbinding-nuvoton-npcx-soc-id"></a>
<a id="std-dtcompatible-nuvoton-npcx-soc-id"></a>

兼容字符串（Compatible String）：`nuvoton,npcx-soc-id`。厂商：[ Nuvoton Technology Corporation ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nuvoton)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nuvoton,npcx-soc-id)。

<a id="description"></a>

Nuvoton NPCX片上系统标识（SoC ID）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 23.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `family-id` | `int` | **必需**。NPCX系列标识（Family ID）。 |
| `chip-id` | `int` | **必需**。NPCX芯片标识（Chip ID）。 |
| `device-id` | `int` | **必需**。NPCX器件标识（Device ID）。 |
| `revision-reg` | `array` | **必需**。NPCX修订版本寄存器（Revision Register）的地址与长度，长度单位为字节。 |

本页没有已弃用的节点专用属性。

---

[上一章](P022_nuvoton_npcx-booter-variant.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P024_nxp_flexio.md)
