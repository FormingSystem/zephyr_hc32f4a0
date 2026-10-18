---
id: learning.zephyr-docs.reset-controller-binding-reference.page-16
title: sifli_sf32lb-rcc-rctl
kind: reference
status: maintained
domains: [zephyr, devicetree, reset]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/reset/sifli,sf32lb-rcc-rctl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第16章\_sifli_sf32lb-rcc-rctl

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/reset/sifli,sf32lb-rcc-rctl.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="sifli-sf32lb-rcc-rctl"></a>
<a id="dtbinding-sifli-sf32lb-rcc-rctl"></a>
<a id="std-dtcompatible-sifli-sf32lb-rcc-rctl"></a>

兼容字符串（Compatible String）：`sifli,sf32lb-rcc-rctl`。厂商：[ SiFli Technologies ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-sifli)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=sifli,sf32lb-rcc-rctl)。

驱动源码（Driver Source）：[drivers/reset/reset_sf32lb.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/reset/reset_sf32lb.c)。

<a id="description"></a>

SiFli SF32LB复位控制器（Reset Controller）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 16.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `#reset-cells` | `int` | **必需**。复位属性中的说明符单元（Specifier Cell）数量。若要使用 `reset_dt_spec` 宏，必须有一个名为 `id` 的单元；固定值：`1` |

本页没有已弃用的节点专用属性。

本页没有继承的基础属性（Base Properties）。

<a id="specifier-cell-names"></a>

## 16.2\_说明符单元名称

复位说明符单元（Reset Specifier Cells）按原文顺序为：`id`。

名称对照：`id` 为复位标识。

---

[上一章](P015_rockchip_rk3588-cru-rst.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P017_st_stm32-rcc-rctl.md)
