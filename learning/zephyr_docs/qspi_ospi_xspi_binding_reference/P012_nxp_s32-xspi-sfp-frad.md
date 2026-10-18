---
id: learning.zephyr-docs.qspi-ospi-xspi-binding-reference.page-12
title: nxp_s32-xspi-sfp-frad
kind: reference
status: maintained
domains: [zephyr, devicetree, qspi, ospi, xspi]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/xspi/nxp,s32-xspi-sfp-frad.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第12章\_nxp_s32-xspi-sfp-frad

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/xspi/nxp,s32-xspi-sfp-frad.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nxp-s32-xspi-sfp-frad"></a>
<a id="dtbinding-nxp-s32-xspi-sfp-frad"></a>
<a id="std-dtcompatible-nxp-s32-xspi-sfp-frad"></a>

兼容字符串（Compatible String）：`nxp,s32-xspi-sfp-frad`。厂商：[ NXP ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nxp)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nxp,s32-xspi-sfp-frad)。

<a id="description"></a>

NXP S32扩展串行外设接口（eXpanded Serial Peripheral Interface，XSPI）安全闪存保护（SFP）的FRAD。

FRAD根据每次事务的地址范围，对输入闪存写入及擦除事务执行第二级检查。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 12.1\_节点专用属性

这些属性不继承自基础绑定文件。

本页没有节点专用属性。

本页没有已弃用的节点专用属性。

<a id="child-node-properties"></a>

## 子节点属性

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。原文没有提供文字说明 |
| `master-domain-acp-policy` | `int` | **必需**。选择主域访问控制策略（Master Domain Access Control Policy），定义在`dt-bindings/xspi/nxp-s32-xspi.h`。`NXP_S32_XSPI_NON_SECURE`选择非安全策略；`NXP_S32_XSPI_SECURE`选择安全策略；`NXP_S32_XSPI_PRIVILEGE`选择特权策略。允许组合：`NXP_S32_XSPI_SECURE`；`NXP_S32_XSPI_SECURE | NXP_S32_XSPI_PRIVILEGE`；`NXP_S32_XSPI_NON_SECURE | NXP_S32_XSPI_PRIVILEGE`；`NXP_S32_XSPI_NON_SECURE | NXP_S32_XSPI_SECURE | NXP_S32_XSPI_PRIVILEGE`。 |

`reg`的相关说明见[设备树重要属性](../devicetree/P003_语法与结构.md#dt-important-props)。

---

[上一章](P011_st_stm32-qspi.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P013_nxp_s32-xspi-sfp-mdad.md)
