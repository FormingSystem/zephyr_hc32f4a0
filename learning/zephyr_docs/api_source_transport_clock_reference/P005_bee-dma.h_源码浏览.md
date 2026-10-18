---
id: learning.zephyr-docs.api-source-transport-clock-reference.page-5
title: bee-dma.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bee-dma_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_bee-dma.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/bee-dma_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_supplement_reference/P006_zephyr__dt-bindings__dma__bee-dma.h_文件参考.md)。

## 5.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
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
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>

```c
/*
 * Copyright (c) 2026, Realtek Semiconductor Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_DMA_BEE_DMA_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_DMA_BEE_DMA_H_


/* Direction, bits [1:0] */
#define BEE_DMA_M2M 0
#define BEE_DMA_M2P 1
#define BEE_DMA_P2M 2

/* Source address adjustment, bits [3:2] */
#define BEE_DMA_SRC_INC   (0 << 2)
#define BEE_DMA_SRC_DEC   (1 << 2)
#define BEE_DMA_SRC_FIXED (2 << 2)

/* Destination address adjustment, bits [5:4] */
#define BEE_DMA_DST_INC   (0 << 4)
#define BEE_DMA_DST_DEC   (1 << 4)
#define BEE_DMA_DST_FIXED (2 << 4)

/* Source data width, bits [7:6] */
#define BEE_DMA_SRC_WIDTH_8BIT  (0 << 6)
#define BEE_DMA_SRC_WIDTH_16BIT (1 << 6)
#define BEE_DMA_SRC_WIDTH_32BIT (2 << 6)

/* Destination data width, bits [9:8] */
#define BEE_DMA_DST_WIDTH_8BIT  (0 << 8)
#define BEE_DMA_DST_WIDTH_16BIT (1 << 8)
#define BEE_DMA_DST_WIDTH_32BIT (2 << 8)

/* Source burst size (msize), bits [12:10] */
#define BEE_DMA_SRC_MSIZE(n) ((n) << 10)
/* Destination burst size (msize), bits [15:13] */
#define BEE_DMA_DST_MSIZE(n) ((n) << 13)

/* Named burst-size values for use with BEE_DMA_SRC_MSIZE / BEE_DMA_DST_MSIZE */
#define BEE_DMA_MSIZE_1   0
#define BEE_DMA_MSIZE_4   1
#define BEE_DMA_MSIZE_8   2
#define BEE_DMA_MSIZE_16  3
#define BEE_DMA_MSIZE_32  4
#define BEE_DMA_MSIZE_64  5
#define BEE_DMA_MSIZE_128 6
#define BEE_DMA_MSIZE_256 7

/* Channel priority, bits [20:16]. Bee supports 0 to 9. */
#define BEE_DMA_PRIORITY(n) ((n) << 16)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_DMA_BEE_DMA_H_ */
```

## 5.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026, Realtek Semiconductor Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 42 行

方向（direction），位 `[1:0]`。

### 注释 3：原第 47 行

源地址调整（source address adjustment），位 `[3:2]`。

### 注释 4：原第 52 行

目标地址调整（destination address adjustment），位 `[5:4]`。

### 注释 5：原第 57 行

源数据宽度（source data width），位 `[7:6]`。

### 注释 6：原第 62 行

目标数据宽度（destination data width），位 `[9:8]`。

### 注释 7：原第 67 行

源突发大小（source burst size，`msize`），位 `[12:10]`。

### 注释 8：原第 69 行

目标突发大小（destination burst size，`msize`），位 `[15:13]`。

### 注释 9：原第 72 行

用于 `BEE_DMA_SRC_MSIZE`／`BEE_DMA_DST_MSIZE` 的具名突发大小取值（named burst-size values）。

### 注释 10：原第 82 行

通道优先级（channel priority），位 `[20:16]`。Bee 支持 0–9。

### 注释 11：原第 85 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_DMA_BEE_DMA_H_`。

## 5.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_supplement_reference/P006_zephyr__dt-bindings__dma__bee-dma.h_文件参考.md)

---

[上一章](P004_bcm2836-l1.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P006_coap.h_源码浏览.md)
