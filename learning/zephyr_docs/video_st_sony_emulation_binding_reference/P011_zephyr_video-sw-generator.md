---
id: learning.zephyr-docs.video-st-sony-emulation-binding-reference.page-11
title: zephyr_video-sw-generator
kind: reference
status: maintained
domains: [zephyr, devicetree, video]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/video/zephyr,video-sw-generator.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第11章\_zephyr_video-sw-generator

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/video/zephyr,video-sw-generator.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="zephyr-video-sw-generator"></a>
<a id="dtbinding-zephyr-video-sw-generator"></a>
<a id="std-dtcompatible-zephyr-video-sw-generator"></a>

兼容字符串（Compatible String）：`zephyr,video-sw-generator`。厂商：[ Zephyr Project ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,video-sw-generator)。

驱动源码（Driver Source）：[drivers/video/video_sw_generator.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/video_sw_generator.c)。

<a id="description"></a>

仿真视频测试图案生成器（Emulated Video Test Pattern Generator）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 11.1\_节点专用属性

这些属性不继承自基础绑定文件。

本页没有节点专用属性。

本页没有已弃用的节点专用属性。

---

[上一章](P010_zephyr_video-emul-rx.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md)
