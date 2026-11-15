---
id: learning.zephyr-docs.api-source-transport-clock-reference.page-22
title: renesas_rz_dma.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas__rz__dma_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_renesas\_rz\_dma.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rz__dma_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P351_zephyr__dt-bindings__dma__renesas_rz_dma.h_文件参考.md)。

## 22.1\_原始可见代码（Source Code）

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
<a id="foldopen00051"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="foldopen00054"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>

```c
/*
 * Copyright (c) 2024 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_DMA_RENESAS_RZ_DMA_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_DMA_RENESAS_RZ_DMA_H_

/* mode:                bit 0 (0: Normal, 1: Block) */
/* source data size:    bit 1, 2, 3 (0b000 -> 0b111) */
/* dest data size:      bit 4, 5, 6 (0b000 -> 0b111) */
/* source addr mode:    bit 7 (0: incremented, 1: fixed) */
/* dest addr mode:      bit 8 (0: incremented, 1: fixed) */

#define RZ_DMA_MODE_NORMAL (0U)
#define RZ_DMA_MODE_BLOCK  (1U)

/* DMA source data size config on bits 1, 2, 3 */
#define RZ_DMA_CFG_SRC_DATA_SIZE(val) ((val & 0x7) << 1)
#define RZ_DMA_SRC_1_BYTE             RZ_DMA_CFG_SRC_DATA_SIZE(0)
#define RZ_DMA_SRC_2_BYTE             RZ_DMA_CFG_SRC_DATA_SIZE(1)
#define RZ_DMA_SRC_4_BYTE             RZ_DMA_CFG_SRC_DATA_SIZE(2)
#define RZ_DMA_SRC_8_BYTE             RZ_DMA_CFG_SRC_DATA_SIZE(3)
#define RZ_DMA_SRC_16_BYTE            RZ_DMA_CFG_SRC_DATA_SIZE(4)
#define RZ_DMA_SRC_32_BYTE            RZ_DMA_CFG_SRC_DATA_SIZE(5)
#define RZ_DMA_SRC_64_BYTE            RZ_DMA_CFG_SRC_DATA_SIZE(6)
#define RZ_DMA_SRC_128_BYTE           RZ_DMA_CFG_SRC_DATA_SIZE(7)

/* DMA destination data size config on bits 4, 5, 6 */
#define RZ_DMA_CFG_DEST_DATA_SIZE(val) ((val & 0x7) << 4)
#define RZ_DMA_DEST_1_BYTE             RZ_DMA_CFG_DEST_DATA_SIZE(0)
#define RZ_DMA_DEST_2_BYTE             RZ_DMA_CFG_DEST_DATA_SIZE(1)
#define RZ_DMA_DEST_4_BYTE             RZ_DMA_CFG_DEST_DATA_SIZE(2)
#define RZ_DMA_DEST_8_BYTE             RZ_DMA_CFG_DEST_DATA_SIZE(3)
#define RZ_DMA_DEST_16_BYTE            RZ_DMA_CFG_DEST_DATA_SIZE(4)
#define RZ_DMA_DEST_32_BYTE            RZ_DMA_CFG_DEST_DATA_SIZE(5)
#define RZ_DMA_DEST_64_BYTE            RZ_DMA_CFG_DEST_DATA_SIZE(6)
#define RZ_DMA_DEST_128_BYTE           RZ_DMA_CFG_DEST_DATA_SIZE(7)

/* DMA source address mode config on bit 7 */
#define RZ_DMA_CFG_SRC_ADDR_MODE(val) ((val & 0x1) << 7)
#define RZ_DMA_SRC_INCREMENTED        RZ_DMA_CFG_SRC_ADDR_MODE(0)
#define RZ_DMA_SRC_FIXED              RZ_DMA_CFG_SRC_ADDR_MODE(1)

/* DMA source address mode config on bit 8 */
#define RZ_DMA_CFG_DEST_ADDR_MODE(val) ((val & 0x1) << 8)
#define RZ_DMA_DEST_INCREMENTED        RZ_DMA_CFG_DEST_ADDR_MODE(0)
#define RZ_DMA_DEST_FIXED              RZ_DMA_CFG_DEST_ADDR_MODE(1)

/* DMA usual combination for peripheral transfer */
#define RZ_DMA_MEM_TO_PERIPH                                                                       \
        (RZ_DMA_MODE_NORMAL | RZ_DMA_SRC_INCREMENTED | RZ_DMA_DEST_FIXED | RZ_DMA_SRC_1_BYTE |     \
         RZ_DMA_DEST_1_BYTE)
#define RZ_DMA_PERIPH_TO_MEM                                                                       \
        (RZ_DMA_MODE_NORMAL | RZ_DMA_SRC_FIXED | RZ_DMA_DEST_INCREMENTED | RZ_DMA_SRC_1_BYTE |     \
         RZ_DMA_DEST_1_BYTE)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_DMA_RENESAS_RZ_DMA_H_ */
```

## 22.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 9 行

模式（mode）：位 0，0 为普通模式（Normal），1 为块模式（Block）。

### 注释 3：原第 10 行

源数据大小（source data size）：位 1、2、3，取值从 `0b000` 到 `0b111`。

### 注释 4：原第 11 行

目标数据大小（destination data size）：位 4、5、6，取值从 `0b000` 到 `0b111`。

### 注释 5：原第 12 行

源地址模式（source address mode）：位 7，0 为递增（incremented），1 为固定（fixed）。

### 注释 6：原第 13 行

目标地址模式（destination address mode）：位 8，0 为递增，1 为固定。

### 注释 7：原第 18 行

DMA 源数据大小配置位于位 1、2、3。

### 注释 8：原第 29 行

DMA 目标数据大小配置位于位 4、5、6。

### 注释 9：原第 40 行

DMA 源地址模式配置位于位 7。

### 注释 10：原第 45 行

DMA 源地址模式配置位于位 8。译注：原文此处写作 source；上方模式位说明将位 8 标为目标地址模式，具体含义请结合原始宏定义阅读。

### 注释 11：原第 50 行

外设传输常用的 DMA 组合。

### 注释 12：原第 58 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_DMA_RENESAS_RZ_DMA_H_`。

## 22.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P351_zephyr__dt-bindings__dma__renesas_rz_dma.h_文件参考.md)

---

[上一章](P021_ots.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P023_riscv_imsic.h_源码浏览.md)
