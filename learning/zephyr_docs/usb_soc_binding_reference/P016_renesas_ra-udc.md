---
id: learning.zephyr-docs.usb-soc-binding-reference.page-16
title: renesas_ra-udc
kind: reference
status: maintained
domains: [zephyr, devicetree, usb]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/usb/renesas/renesas,ra-udc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第16章\_renesas_ra-udc

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/usb/renesas/renesas,ra-udc.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="renesas-ra-udc"></a>
<a id="dtbinding-renesas-ra-udc"></a>
<a id="std-dtcompatible-renesas-ra-udc"></a>

兼容字符串（Compatible String）：`renesas,ra-udc`。厂商：[ Renesas Electronics Corporation ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-renesas)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=renesas,ra-udc)。

驱动源码（Driver Source）：[drivers/usb/udc/udc_renesas_ra.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/udc_renesas_ra.c)。

<a id="description"></a>

Renesas RA USB设备控制器（USB Device Controller）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 16.1\_节点专用属性

这些属性不继承自基础绑定文件。

本页没有节点专用属性。

本页没有已弃用的节点专用属性。

---

[上一章](P015_renesas_smartbond-usbd.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P017_renesas_ra-uhc.md)
