---
id: learning.zephyr-docs.wakeup-interrupt-binding-reference.page-8
title: nuvoton_npcx-miwu-int-map
kind: reference
status: maintained
domains: [zephyr, devicetree, interrupts, timer]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/interrupt-controller/nuvoton,npcx-miwu-int-map.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第8章\_nuvoton_npcx-miwu-int-map

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/interrupt-controller/nuvoton,npcx-miwu-int-map.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nuvoton-npcx-miwu-int-map"></a>
<a id="dtbinding-nuvoton-npcx-miwu-int-map"></a>
<a id="std-dtcompatible-nuvoton-npcx-miwu-int-map"></a>

兼容字符串（Compatible String）：`nuvoton,npcx-miwu-int-map`。厂商：[ Nuvoton Technology Corporation ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nuvoton)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nuvoton,npcx-miwu-int-map)。

<a id="description"></a>

NPCX多输入唤醒单元（Multi-Input Wake-Up Unit，MIWU）的组中断映射子节点（Group-interrupt Mapping Child Node）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 8.1\_顶层属性

以下属性用于 `nuvoton,npcx-miwu-int-map` 节点本身。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `parent` | `phandle` | **必需**。MIWU组的父设备节点（Parent Device Node） |

本页没有已弃用的节点专用属性，也没有继承的基础属性。

<a id="child-node-properties"></a>

## 8.2\_子节点属性

以下属性放在子节点（Child Node）中。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `irq` | `int` | **必需**。MIWU组的中断请求（IRQ） |
| `irq-prio` | `int` | **必需**。MIWU组的IRQ优先级（Priority），有效数值为0至7 |
| `group-mask` | `int` | **必需**。MIWU中断的组位掩码（Group Bitmask） |
| `groups` | `array` | 共享同一个中断的组（Group） |

---

[上一章](P007_ite_it8xxx2-wuc.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P009_nuvoton_npcx-miwu-wui-map.md)
