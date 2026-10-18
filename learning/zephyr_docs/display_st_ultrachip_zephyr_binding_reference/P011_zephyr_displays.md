---
id: learning.zephyr-docs.display-st-ultrachip-zephyr-binding-reference.page-11
title: zephyr_displays
kind: reference
status: maintained
domains: [zephyr, devicetree, display]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/display/zephyr,displays.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第11章\_zephyr_displays

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/display/zephyr,displays.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="zephyr-displays"></a>
<a id="dtbinding-zephyr-displays"></a>
<a id="std-dtcompatible-zephyr-displays"></a>

兼容字符串（Compatible String）：`zephyr,displays`。厂商：[ Zephyr Project ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,displays)。

<a id="description"></a>

提供给LVGL等图形库（Graphics Library）的显示控制器集合。设备树（Devicetree）中只允许有一个使用此兼容字符串的节点。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 11.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `displays` | `phandles` | **必需**。供图形库（Graphics Library）使用的显示控制器节点。 |

本页没有已弃用的节点专用属性。

---

[上一章](P010_waveshare_dsi2dpi.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P012_zephyr_dummy-dc.md)
