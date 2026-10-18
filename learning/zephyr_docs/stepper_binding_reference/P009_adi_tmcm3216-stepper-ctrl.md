---
id: learning.zephyr-docs.stepper-binding-reference.page-9
title: adi_tmcm3216-stepper-ctrl
kind: reference
status: maintained
domains: [zephyr, devicetree, stepper]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/stepper/adi/adi,tmcm3216-stepper-ctrl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第9章\_adi_tmcm3216-stepper-ctrl

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/stepper/adi/adi,tmcm3216-stepper-ctrl.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="adi-tmcm3216-stepper-ctrl"></a>
<a id="dtbinding-adi-tmcm3216-stepper-ctrl"></a>
<a id="std-dtcompatible-adi-tmcm3216-stepper-ctrl"></a>

兼容字符串（Compatible String）：`adi,tmcm3216-stepper-ctrl`。厂商：[ Analog Devices ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-adi)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=adi,tmcm3216-stepper-ctrl)。

驱动源码（Driver Source）：[drivers/stepper/adi_tmc/tmcm3216/tmcm3216_stepper_ctrl.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/adi_tmc/tmcm3216/tmcm3216_stepper_ctrl.c)。

<a id="description"></a>

ADI TMCM-3216步进电机控制器（Stepper Motor Controller）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 9.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `idx` | `int` | **必需**。电机索引（Motor Index），取0、1或2。 |

本页没有已弃用的节点专用属性。

---

[上一章](P008_adi_tmc51xx-uart.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P010_adi_tmcm3216-stepper-driver.md)
