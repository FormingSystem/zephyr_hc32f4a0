---
id: learning.zephyr-docs.stepper-binding-reference.page-3
title: adi_tmc50xx-stepper-driver
kind: reference
status: maintained
domains: [zephyr, devicetree, stepper]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/stepper/adi/adi,tmc50xx-stepper-driver.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第3章\_adi_tmc50xx-stepper-driver

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/stepper/adi/adi,tmc50xx-stepper-driver.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="adi-tmc50xx-stepper-driver"></a>
<a id="dtbinding-adi-tmc50xx-stepper-driver"></a>
<a id="std-dtcompatible-adi-tmc50xx-stepper-driver"></a>

兼容字符串（Compatible String）：`adi,tmc50xx-stepper-driver`。厂商：[ Analog Devices ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-adi)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=adi,tmc50xx-stepper-driver)。

驱动源码（Driver Source）：[drivers/stepper/adi_tmc/tmc50xx/tmc50xx_stepper_driver.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/adi_tmc/tmc50xx/tmc50xx_stepper_driver.c)。

<a id="description"></a>

步进驱动器（Stepper Driver）属性集合。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 3.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `idx` | `int` | **必需**。原文没有提供文字说明 |
| `micro-step-res` | `int` | 初始化设备驱动时设置的微步分辨率（Microstep Resolution）。；默认值：`1`；合法值：`1, 2, 4, 8, 16, 32, 64, 128, 256` |
| `en-gpios` | `phandle-array` | 控制电机驱动器使能信号（Enable Signal）的GPIO引脚。 |
| `m0-gpios` | `phandle-array` | 微步配置引脚（Microstep Configuration Pin）0。 |
| `m1-gpios` | `phandle-array` | 微步配置引脚（Microstep Configuration Pin）1。 |
| `stallguard2-threshold` | `int` | 有符号值，控制堵转输出使用的StallGuard2等级，并设置读取的最佳测量范围。值越低，灵敏度越高；0是适用于大多数电机的初始值。范围为−64至+63：值越高，StallGuard2越不敏感，需要更大转矩才会指示堵转（Stall）。；默认值：`0`；范围：`-64 to 63` |

本页没有已弃用的节点专用属性。

---

[上一章](P002_adi_tmc50xx-stepper-ctrl.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P004_adi_tmc50xx.md)
