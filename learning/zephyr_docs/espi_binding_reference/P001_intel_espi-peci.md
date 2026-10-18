---
id: learning.zephyr-docs.espi-binding-reference.page-1
title: intel_espi-peci
kind: reference
status: maintained
domains: [zephyr, devicetree, espi]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/espi/intel,espi-peci.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第1章\_intel_espi-peci

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/espi/intel,espi-peci.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="intel-espi-peci-on-espi-bus"></a>
<a id="dtbinding-intel-espi-peci"></a>
<a id="std-dtcompatible-intel-espi-peci"></a>

兼容字符串（Compatible String）：`intel,espi-peci`。厂商：[ Intel ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-intel)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=intel,espi-peci)。

驱动源码（Driver Source）：[drivers/peci/espi_peci.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/peci/espi_peci.c)。

<a id="description"></a>

关联到此增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线的平台环境控制接口（Platform Environment Control Interface，PECI）节点。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 1.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `peci-addr` | `int` | 通过eSPI总线公开的PECI控制器的I²C／PECI地址；主机用此地址与PECI设备通信。；默认值：`0x7` |

本页没有已弃用的节点专用属性。

---

[本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P002_ite_it8xxx2-espi.md)
