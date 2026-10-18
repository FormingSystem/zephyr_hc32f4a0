---
id: learning.zephyr-docs.qspi-ospi-xspi-binding-reference.page-6
title: nxp_s32-qspi-sfp-mdad
kind: reference
status: maintained
domains: [zephyr, devicetree, qspi, ospi, xspi]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/qspi/nxp,s32-qspi-sfp-mdad.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第6章\_nxp_s32-qspi-sfp-mdad

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/qspi/nxp,s32-qspi-sfp-mdad.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nxp-s32-qspi-sfp-mdad"></a>
<a id="dtbinding-nxp-s32-qspi-sfp-mdad"></a>
<a id="std-dtcompatible-nxp-s32-qspi-sfp-mdad"></a>

兼容字符串（Compatible String）：`nxp,s32-qspi-sfp-mdad`。厂商：[ NXP ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nxp)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nxp,s32-qspi-sfp-mdad)。

<a id="description"></a>

NXP S32 QSPI安全闪存保护（SFP）的MDAD。

MDAD根据每次输入事务的安全属性及关联的MGID执行第一级检查。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 6.1\_节点专用属性

这些属性不继承自基础绑定文件。

本页没有节点专用属性。

本页没有已弃用的节点专用属性。

<a id="child-node-properties"></a>

## 子节点属性

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `secure-attribute` | `int` | **必需**。选择安全属性（Secure Attribute），定义在`dt-bindings/qspi/nxp-s32-qspi.h`：`NXP_S32_QSPI_NON_SECURE`允许该主设备使用非安全总线属性；`NXP_S32_QSPI_SECURE`允许安全属性。允许组合：`NXP_S32_QSPI_NON_SECURE`；`NXP_S32_QSPI_SECURE`；`NXP_S32_QSPI_NON_SECURE | NXP_S32_QSPI_SECURE`。 |
| `mask-type` | `string` | 选择掩码类型（Mask Type）：`AND`为按位与掩码，`OR`为按位或掩码；默认值对应寄存器字段复位值。；默认值：`AND`；合法值：`AND, OR` |
| `mask` | `int` | ID匹配（ID-Match）比较的掩码值，范围0至63；默认值对应寄存器字段复位值。；默认值：`0` |
| `domain-id` | `int` | **必需**。MID比较所用的域ID（Domain-ID，MID）参考值，范围0至63。 |

---

[上一章](P005_nxp_s32-qspi-sfp-frad.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P007_nxp_s32-qspi.md)
