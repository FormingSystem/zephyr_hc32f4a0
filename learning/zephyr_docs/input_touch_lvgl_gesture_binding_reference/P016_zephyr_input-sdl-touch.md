---
id: learning.zephyr-docs.input-touch-lvgl-gesture-binding-reference.page-16
title: zephyr_input-sdl-touch
kind: reference
status: maintained
domains: [zephyr, devicetree, input]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/input/zephyr,input-sdl-touch.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第16章\_zephyr_input-sdl-touch

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/input/zephyr,input-sdl-touch.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="zephyr-input-sdl-touch"></a>
<a id="dtbinding-zephyr-input-sdl-touch"></a>
<a id="std-dtcompatible-zephyr-input-sdl-touch"></a>

兼容字符串（Compatible String）：`zephyr,input-sdl-touch`。厂商：[ Zephyr Project ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,input-sdl-touch)。

驱动源码（Driver Source）：[drivers/input/input_sdl_touch.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/input_sdl_touch.c)。

<a id="description"></a>

基于SDL的仿真触摸面板（Emulated Touch Panel）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 16.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `display` | `phandle` | 输入事件所属显示器的句柄（Display Handle）。 |

本页没有已弃用的节点专用属性。

---

[上一章](P015_zephyr_input-longpress.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P017_zephyr_lvgl-button-input.md)
