---
id: learning.zephyr-docs.dma-binding-reference.page-5
title: amd_acp-sdw-dma
kind: reference
status: maintained
domains: [zephyr, devicetree, dma]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/dma/amd,acp-sdw-dma.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第5章\_amd_acp-sdw-dma

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/dma/amd,acp-sdw-dma.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="amd-acp-sdw-dma"></a>
<a id="dtbinding-amd-acp-sdw-dma"></a>
<a id="std-dtcompatible-amd-acp-sdw-dma"></a>

兼容字符串（Compatible String）：`amd,acp-sdw-dma`。厂商：[ Advanced Micro Devices (AMD), Inc. ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-amd)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=amd,acp-sdw-dma)。

驱动源码（Driver Source）：[drivers/dma/dma_amd_acp_sdw.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/dma_amd_acp_sdw.c)。

<a id="description"></a>

AMD SOF SoundWire DMA节点。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 5.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `dma-channels` | `int` | 支持的DMA通道数量 |
| `dma-requests` | `int` | 支持的DMA请求数量 |
| `reg` | `array` | DMA控制器的寄存器地址和大小（Register Address and Size） |
| `interrupts` | `array` | DMA控制器的中断说明符（Interrupt Specifier） |
| `clocks` | `phandle-array` | DMA控制器的时钟（Clock） |

本页没有已弃用的节点专用属性。

---

[上一章](P004_amd_acp-host-dma.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P006_amd_acp-tdm-dma.md)
