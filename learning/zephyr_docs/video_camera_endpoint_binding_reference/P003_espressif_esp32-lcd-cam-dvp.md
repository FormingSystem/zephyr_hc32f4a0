---
id: learning.zephyr-docs.video-camera-endpoint-binding-reference.page-3
title: espressif_esp32-lcd-cam-dvp
kind: reference
status: maintained
domains: [zephyr, devicetree, video]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/video/espressif,esp32-lcd-cam-dvp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第3章\_espressif_esp32-lcd-cam-dvp

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/video/espressif,esp32-lcd-cam-dvp.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="espressif-esp32-lcd-cam-dvp"></a>
<a id="dtbinding-espressif-esp32-lcd-cam-dvp"></a>
<a id="std-dtcompatible-espressif-esp32-lcd-cam-dvp"></a>

兼容字符串（Compatible String）：`espressif,esp32-lcd-cam-dvp`。厂商：[ Espressif Systems ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-espressif)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=espressif,esp32-lcd-cam-dvp)。

驱动源码（Driver Source）：[drivers/video/video_esp32_dvp.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/video_esp32_dvp.c)。

<a id="description"></a>

ESP32 LCD-CAM摄像头接口（Camera Interface）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 3.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `source` | `phandle` | **必需**。连接的源设备（Source Device），即摄像头传感器。 |
| `data-width` | `int` | 摄像头输入数据宽度（Input Data Width），8位或16位。；合法值：`8, 16` |
| `invert-byte-order` | `boolean` | 在16位模式下反转字节顺序（Byte Order）。 |
| `invert-bit-order` | `boolean` | 反转位顺序（Bit Order）。 |
| `invert-pclk` | `boolean` | 反转像素时钟信号（Pixel Clock Signal）。 |
| `invert-de` | `boolean` | 反转数据使能信号（Data Enable Signal）。 |
| `invert-hsync` | `boolean` | 反转水平同步信号（HSYNC Signal）。 |
| `invert-vsync` | `boolean` | 反转垂直同步信号（VSYNC Signal）。 |
| `cam-clk` | `int` | 摄像头时钟频率（Camera Clock Frequency）。 |

本页没有已弃用的节点专用属性。

---

[上一章](P002_arducam_mega.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P004_galaxycore_gc2145.md)
