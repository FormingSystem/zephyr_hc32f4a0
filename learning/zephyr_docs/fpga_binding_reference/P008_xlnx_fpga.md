---
id: learning.zephyr-docs.fpga-binding-reference.page-8
title: xlnx_fpga
kind: reference
status: maintained
domains: [zephyr, devicetree, fpga]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/fpga/xlnx,fpga.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第8章\_xlnx_fpga

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/fpga/xlnx,fpga.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="xlnx-fpga"></a>
<a id="dtbinding-xlnx-fpga"></a>
<a id="std-dtcompatible-xlnx-fpga"></a>

兼容字符串（Compatible String）：`xlnx,fpga`。厂商：[ Xilinx ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-xlnx)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=xlnx,fpga)。

驱动源码（Driver Source）：[drivers/fpga/fpga_zynqmp.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fpga/fpga_zynqmp.c)。

<a id="description"></a>

Xilinx ZynqMP FPGA驱动。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 8.1\_节点专用属性

这些属性不继承自基础绑定文件。

本页没有节点专用属性。

本页没有已弃用的节点专用属性。

---

[上一章](P007_renesas_slg47910.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md)
