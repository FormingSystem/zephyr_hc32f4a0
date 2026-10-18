---
id: learning.zephyr-docs.stepper-binding-reference.page-10
title: adi_tmcm3216-stepper-driver
kind: reference
status: maintained
domains: [zephyr, devicetree, stepper]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/stepper/adi/adi,tmcm3216-stepper-driver.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第10章\_adi_tmcm3216-stepper-driver

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/stepper/adi/adi,tmcm3216-stepper-driver.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="adi-tmcm3216-stepper-driver"></a>
<a id="dtbinding-adi-tmcm3216-stepper-driver"></a>
<a id="std-dtcompatible-adi-tmcm3216-stepper-driver"></a>

兼容字符串（Compatible String）：`adi,tmcm3216-stepper-driver`。厂商：[ Analog Devices ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-adi)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=adi,tmcm3216-stepper-driver)。

驱动源码（Driver Source）：[drivers/stepper/adi_tmc/tmcm3216/tmcm3216_stepper_driver.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/adi_tmc/tmcm3216/tmcm3216_stepper_driver.c)。

<a id="description"></a>

ADI TMCM-3216步进电机驱动器（Stepper Motor Driver）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 10.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `idx` | `int` | **必需**。电机索引（Motor Index），取0、1或2。 |
| `micro-step-res` | `int` | **必需**。默认微步分辨率（Microstep Resolution），合法值为1、2、4、8、16、32、64、128、256。 |

本页没有已弃用的节点专用属性。

---

[上一章](P009_adi_tmcm3216-stepper-ctrl.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P011_adi_tmcm3216.md)
