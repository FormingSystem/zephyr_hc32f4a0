---
id: learning.zephyr-docs.espi-binding-reference.page-10
title: nuvoton_npcx-espi-vw-conf
kind: reference
status: maintained
domains: [zephyr, devicetree, espi]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/espi/nuvoton,npcx-espi-vw-conf.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第10章\_nuvoton_npcx-espi-vw-conf

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/espi/nuvoton,npcx-espi-vw-conf.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nuvoton-npcx-espi-vw-conf"></a>
<a id="dtbinding-nuvoton-npcx-espi-vw-conf"></a>
<a id="std-dtcompatible-nuvoton-npcx-espi-vw-conf"></a>

兼容字符串（Compatible String）：`nuvoton,npcx-espi-vw-conf`。厂商：[ Nuvoton ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nuvoton)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nuvoton,npcx-espi-vw-conf)。

<a id="description"></a>

Nuvoton NPCX eSPI虚拟线（Virtual Wire，VW）映射子节点。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 10.1\_节点专用属性

这些属性不继承自基础绑定文件。

本页没有节点专用属性。

本页没有已弃用的节点专用属性。

<a id="child-node-properties"></a>

## 子节点属性

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `vw-reg` | `array` | **必需**。VW信号的寄存器索引与VW位掩码。 |
| `vw-wui` | `phandle` | 唤醒输入（Wake-Up Input，WUI）与VW输入信号之间的映射。下方原例为NPCX7上`VW_SLP5`的WUI映射。 |

## 唤醒映射原例

```dts
   vw-wui = <&wui_vw_slp_s5>;
```

---

[上一章](P009_nuvoton_npcx-espi-taf.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P011_nuvoton_npcx-espi.md)
