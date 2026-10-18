---
id: learning.zephyr-docs.wakeup-interrupt-binding-reference.page-9
title: nuvoton_npcx-miwu-wui-map
kind: reference
status: maintained
domains: [zephyr, devicetree, interrupts, timer]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/interrupt-controller/nuvoton,npcx-miwu-wui-map.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第9章\_nuvoton_npcx-miwu-wui-map

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/interrupt-controller/nuvoton,npcx-miwu-wui-map.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nuvoton-npcx-miwu-wui-map"></a>
<a id="dtbinding-nuvoton-npcx-miwu-wui-map"></a>
<a id="std-dtcompatible-nuvoton-npcx-miwu-wui-map"></a>

兼容字符串（Compatible String）：`nuvoton,npcx-miwu-wui-map`。厂商：[ Nuvoton Technology Corporation ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nuvoton)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nuvoton,npcx-miwu-wui-map)。

<a id="description"></a>

NPCX-MIWU唤醒单元输入（Wake-Up Unit Input，WUI）的映射子节点（Mapping Child Node）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 9.1\_顶层属性

没有顶层属性（No Top-level Properties）。

<a id="child-node-properties"></a>

## 9.2\_子节点属性

以下属性放在子节点（Child Node）中。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `miwus` | `phandle-array` | **必需**。原文没有提供文字说明，类型与必需标记按原表保留 |

---

[上一章](P008_nuvoton_npcx-miwu-int-map.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P010_nuvoton_npcx-miwu.md)
