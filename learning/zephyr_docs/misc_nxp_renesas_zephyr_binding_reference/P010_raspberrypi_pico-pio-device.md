---
id: learning.zephyr-docs.misc-nxp-renesas-zephyr-binding-reference.page-10
title: raspberrypi_pico-pio-device
kind: reference
status: maintained
domains: [zephyr, devicetree, peripherals]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/misc/raspberrypi,pico-pio-device.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第10章\_raspberrypi_pico-pio-device

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/misc/raspberrypi,pico-pio-device.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="raspberrypi-pico-pio-device"></a>
<a id="dtbinding-raspberrypi-pico-pio-device"></a>
<a id="std-dtcompatible-raspberrypi-pico-pio-device"></a>

兼容字符串（Compatible String）：`raspberrypi,pico-pio-device`。厂商：[ Raspberry Pi Foundation ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-raspberrypi)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=raspberrypi,pico-pio-device)。

<a id="description"></a>

Raspberry Pi Pico可编程I/O设备（Programmable I/O，PIO Device）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 10.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `pinctrl-0` | `phandles` | 第一个状态（State）的引脚配置（Pin Configuration），具体内容取决于所选引脚控制器驱动（Pin Controller Driver）的实现 |
| `pinctrl-1` | `phandles` | 第二个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-2` | `phandles` | 第三个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-3` | `phandles` | 第四个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-4` | `phandles` | 第五个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-names` | `string-array` | 所提供状态的名称，名称数量必须与状态数量一致 |

本页没有已弃用的节点专用属性。

---

[上一章](P009_nxp_s32-trgmux.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P011_raspberrypi_pico-pio.md)
