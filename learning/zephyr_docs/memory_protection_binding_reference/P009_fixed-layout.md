---
id: learning.zephyr-docs.memory-protection-binding-reference.page-9
title: fixed-layout
kind: reference
status: maintained
domains: [zephyr, devicetree, memory]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/nvmem/fixed-layout.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第9章\_fixed-layout

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/nvmem/fixed-layout.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="fixed-layout"></a>
<a id="dtbinding-fixed-layout"></a>
<a id="std-dtcompatible-fixed-layout"></a>

兼容字符串（Compatible String）：`fixed-layout`。厂商：[ 无厂商 ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-no-vendor)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=fixed-layout)。

<a id="description"></a>

非易失存储器（Non-Volatile Memory）的固定布局（Fixed Layout）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 9.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `#address-cells` | `int` | 表示子节点reg属性地址所需的单元（Cell）数量；固定值：`1` |
| `#size-cells` | `int` | 表示子节点大小所需的单元数量；固定值：`1` |

本页没有已弃用的节点专用属性。

<a id="child-node-properties"></a>

## 9.2\_子节点属性

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。格式应为 `<OFFSET SIZE>`，OFFSET是NVMEM单元相对于父存储器基地址的偏移，SIZE是单元大小，单位字节 |
| `read-only` | `boolean` | 该单元为只读（Read-only）时设置本属性 |

---

[上一章](P008_nxp_sysmpu.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P010_nordic_owned-memory.md)
