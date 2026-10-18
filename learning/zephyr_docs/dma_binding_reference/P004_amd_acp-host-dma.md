---
id: learning.zephyr-docs.dma-binding-reference.page-4
title: amd_acp-host-dma
kind: reference
status: maintained
domains: [zephyr, devicetree, dma]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/dma/amd,acp-host-dma.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第4章\_amd_acp-host-dma

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/dma/amd,acp-host-dma.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="amd-acp-host-dma"></a>
<a id="dtbinding-amd-acp-host-dma"></a>
<a id="std-dtcompatible-amd-acp-host-dma"></a>

兼容字符串（Compatible String）：`amd,acp-host-dma`。厂商：[ Advanced Micro Devices (AMD), Inc. ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-amd)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=amd,acp-host-dma)。

驱动源码（Driver Source）：[drivers/dma/dma_amd_acp_host.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/dma_amd_acp_host.c)。

<a id="description"></a>

AMD SOF主机DMA节点（Host DMA Node）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 4.1\_节点专用属性

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

[上一章](P003_altr_msgdma.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P005_amd_acp-sdw-dma.md)
