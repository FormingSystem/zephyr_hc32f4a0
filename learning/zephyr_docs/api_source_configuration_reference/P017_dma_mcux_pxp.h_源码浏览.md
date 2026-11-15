---
id: learning.zephyr-docs.api-source-configuration-reference.page-17
title: dma_mcux_pxp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dma__mcux__pxp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_dma\_mcux\_pxp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dma__mcux__pxp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dma__mcux__pxp_8h.html)。

## 17.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>

```c
/*
 * Copyright 2023-2024 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_MCUX_PXP_H_
#define ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_MCUX_PXP_H_

#define DMA_MCUX_PXP_CMD_MASK  0xE0
#define DMA_MCUX_PXP_CMD_SHIFT 0x5

#define DMA_MCUX_PXP_FMT_MASK  0x1F
#define DMA_MCUX_PXP_FMT_SHIFT 0x0

/*
 * In order to configure the PXP for rotation, the user should
 * supply a format and command as the DMA slot parameter, like so:
 * dma_slot = (DMA_MCUX_PXP_FTM(DMA_MCUX_PXP_FMT_RGB565) |
 *            DMA_MCUX_PXP_CMD(DMA_MCUX_PXP_CMD_ROTATE_90))
 * head block source address: input buffer address
 * head block destination address: output buffer address
 * source data size: input buffer size in bytes
 * source burst length: height of source buffer in pixels
 * dest data size: output buffer size in bytes
 * dest burst length: height of destination buffer in pixels
 */

#define DMA_MCUX_PXP_FMT(x) ((x << DMA_MCUX_PXP_FMT_SHIFT) & DMA_MCUX_PXP_FMT_MASK)
#define DMA_MCUX_PXP_CMD(x) ((x << DMA_MCUX_PXP_CMD_SHIFT) & DMA_MCUX_PXP_CMD_MASK)

#define DMA_MCUX_PXP_CMD_ROTATE_0   0
#define DMA_MCUX_PXP_CMD_ROTATE_90  1
#define DMA_MCUX_PXP_CMD_ROTATE_180 2
#define DMA_MCUX_PXP_CMD_ROTATE_270 3

#define DMA_MCUX_PXP_FMT_RGB565   0
#define DMA_MCUX_PXP_FMT_RGB888   1
#define DMA_MCUX_PXP_FMT_ARGB8888 2

#define DMA_MCUX_PXP_FLIP_MASK  0x3
#define DMA_MCUX_PXP_FLIP_SHIFT 0x0

/*
 * In order to configure the PXP to flip, the user should
 * supply a flip setting as the DMA linked_channel parameter, like so:
 * linked_channel |= DMA_MCUX_PXP_FLIP(DMA_MCUX_PXP_FLIP_HORIZONTAL)
 */

#define DMA_MCUX_PXP_FLIP(x) ((x << DMA_MCUX_PXP_FLIP_SHIFT) & DMA_MCUX_PXP_FLIP_MASK)

#define DMA_MCUX_PXP_FLIP_DISABLE    0
#define DMA_MCUX_PXP_FLIP_HORIZONTAL 1
#define DMA_MCUX_PXP_FLIP_VERTICAL   2
#define DMA_MCUX_PXP_FLIP_BOTH       3

#endif /* ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_MCUX_PXP_H_ */
```

## 17.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2023-2024 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 16 行

要配置像素处理流水线（PXP）进行旋转，用户应将格式和命令作为 DMA 的 `slot` 参数提供，例如：

```c
dma_slot = (DMA_MCUX_PXP_FTM(DMA_MCUX_PXP_FMT_RGB565) |
DMA_MCUX_PXP_CMD(DMA_MCUX_PXP_CMD_ROTATE_90))
```

- 首块源地址（Head block source address）：输入缓冲区地址。
- 首块目标地址（Head block destination address）：输出缓冲区地址。
- 源数据大小（Source data size）：输入缓冲区大小，单位为字节。
- 源突发长度（Source burst length）：源缓冲区高度，单位为像素。
- 目标数据大小（Dest data size）：输出缓冲区大小，单位为字节。
- 目标突发长度（Dest burst length）：目标缓冲区高度，单位为像素。

### 注释 3：原第 44 行

要配置 PXP 进行翻转，用户应将翻转设置作为 DMA 的 `linked_channel` 参数提供，例如：

```c
linked_channel |= DMA_MCUX_PXP_FLIP(DMA_MCUX_PXP_FLIP_HORIZONTAL)
```

### 注释 4：原第 57 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_MCUX_PXP_H_`。

## 17.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dma__mcux__pxp_8h.html)

---

[上一章](P016_dfu_srv.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P018_dma_npcx_gdma.h_源码浏览.md)
