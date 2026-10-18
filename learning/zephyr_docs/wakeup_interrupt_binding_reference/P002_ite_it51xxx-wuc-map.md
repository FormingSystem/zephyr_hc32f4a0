---
id: learning.zephyr-docs.wakeup-interrupt-binding-reference.page-2
title: ite_it51xxx-wuc-map
kind: reference
status: maintained
domains: [zephyr, devicetree, interrupts, timer]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/interrupt-controller/ite,it51xxx-wuc-map.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第2章\_ite_it51xxx-wuc-map

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/interrupt-controller/ite,it51xxx-wuc-map.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="ite-it51xxx-wuc-map"></a>
<a id="dtbinding-ite-it51xxx-wuc-map"></a>
<a id="std-dtcompatible-ite-it51xxx-wuc-map"></a>

兼容字符串（Compatible String）：`ite,it51xxx-wuc-map`。厂商：[ ITE Tech. Inc. ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-ite)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=ite,it51xxx-wuc-map)。

<a id="description"></a>

ITE唤醒控制器（Wake-Up Controller，WUC）的映射子节点（Mapping Child Node）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 2.1\_顶层属性

没有顶层属性（No Top-level Properties）。

<a id="child-node-properties"></a>

## 2.2\_子节点属性

以下属性放在子节点（Child Node）中。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `wucs` | `phandle-array` | **必需**。原文没有提供文字说明，类型与必需标记按原表保留 |

---

[上一章](P001_ite_it51xxx-intc.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P003_ite_it51xxx-wuc.md)
