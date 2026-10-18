---
id: learning.zephyr-docs.api-source-compiler-device-reference.page-11
title: gd32_dma.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gd32__dma_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_gd32\_dma.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/gd32__dma_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P117_zephyr__dt-bindings__dma__gd32_dma.h_文件参考.md)。

## 11.1\_原始可见代码（Source Code）

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

```c
/*
 * Copyright (c) 2022 TOKITA Hiroshi <tokita.hiroshi@gmail.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_DMA_GD32_DMA_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_DMA_GD32_DMA_H_

/* macros for channel-cfg */

/* direction defined on bits 6-7 */
#define GD32_DMA_CH_CFG_DIRECTION(val) ((val & 0x3) << 6)
#define GD32_DMA_MEMORY_TO_MEMORY      GD32_DMA_CH_CFG_DIRECTION(0)
#define GD32_DMA_MEMORY_TO_PERIPH      GD32_DMA_CH_CFG_DIRECTION(1)
#define GD32_DMA_PERIPH_TO_MEMORY      GD32_DMA_CH_CFG_DIRECTION(2)

/* periph increase defined on bit 9 as true/false */
#define GD32_DMA_CH_CFG_PERIPH_ADDR_INC(val) ((val & 0x1) << 9)
#define GD32_DMA_NO_PERIPH_ADDR_INC          GD32_DMA_CH_CFG_PERIPH_ADDR_INC(0)
#define GD32_DMA_PERIPH_ADDR_INC             GD32_DMA_CH_CFG_PERIPH_ADDR_INC(1)

/* memory increase defined on bit 10 as true/false */
#define GD32_DMA_CH_CFG_MEMORY_ADDR_INC(val) ((val & 0x1) << 10)
#define GD32_DMA_NO_MEMORY_ADDR_INC          GD32_DMA_CH_CFG_MEMORY_ADDR_INC(0)
#define GD32_DMA_MEMORY_ADDR_INC             GD32_DMA_CH_CFG_MEMORY_ADDR_INC(1)

/* periph data size defined on bits 11-12 */
#define GD32_DMA_CH_CFG_PERIPH_WIDTH(val) ((val & 0x3) << 11)
#define GD32_DMA_PERIPH_WIDTH_8BIT        GD32_DMA_CH_CFG_PERIPH_WIDTH(0)
#define GD32_DMA_PERIPH_WIDTH_16BIT       GD32_DMA_CH_CFG_PERIPH_WIDTH(1)
#define GD32_DMA_PERIPH_WIDTH_32BIT       GD32_DMA_CH_CFG_PERIPH_WIDTH(2)

/* memory data size defined on bits 13-14 */
#define GD32_DMA_CH_CFG_MEMORY_WIDTH(val) ((val & 0x3) << 13)
#define GD32_DMA_MEMORY_WIDTH_8BIT        GD32_DMA_CH_CFG_PERIPH_WIDTH(0)
#define GD32_DMA_MEMORY_WIDTH_16BIT       GD32_DMA_CH_CFG_PERIPH_WIDTH(1)
#define GD32_DMA_MEMORY_WIDTH_32BIT       GD32_DMA_CH_CFG_PERIPH_WIDTH(2)

/* priority increment offset defined on bit 15 */
#define GD32_DMA_CH_CFG_PERIPH_INC_FIXED(val) ((val & 0x1) << 15)

/* priority defined on bits 16-17 as 0, 1, 2, 3 */
#define GD32_DMA_CH_CFG_PRIORITY(val) ((val & 0x3) << 16)
#define GD32_DMA_PRIORITY_LOW         GD32_DMA_CH_CFG_PRIORITY(0)
#define GD32_DMA_PRIORITY_MEDIUM      GD32_DMA_CH_CFG_PRIORITY(1)
#define GD32_DMA_PRIORITY_HIGH        GD32_DMA_CH_CFG_PRIORITY(2)
#define GD32_DMA_PRIORITY_VERY_HIGH   GD32_DMA_CH_CFG_PRIORITY(3)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_DMA_GD32_DMA_H_ */
```

## 11.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 TOKITA Hiroshi <tokita.hiroshi@gmail.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

用于 `channel-cfg` 的宏。

### 注释 3：原第 12 行

方向（direction）定义在位 6–7 中。

### 注释 4：原第 18 行

外设地址递增（peripheral increment）定义在位 9 中，以 true/false 表示。

### 注释 5：原第 23 行

内存地址递增（memory increment）定义在位 10 中，以 true/false 表示。

### 注释 6：原第 28 行

外设数据大小（peripheral data size）定义在位 11–12 中。

### 注释 7：原第 34 行

内存数据大小（memory data size）定义在位 13–14 中。

### 注释 8：原第 40 行

优先级增量偏移（priority increment offset）定义在位 15 中。

### 注释 9：原第 43 行

优先级（priority）定义在位 16–17 中，取值为 0、1、2、3。

### 注释 10：原第 50 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_DMA_GD32_DMA_H_`。

## 11.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P117_zephyr__dt-bindings__dma__gd32_dma.h_文件参考.md)

---

[上一章](P010_esp32s3_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P012_imx8qm-pinctrl.h_源码浏览.md)
