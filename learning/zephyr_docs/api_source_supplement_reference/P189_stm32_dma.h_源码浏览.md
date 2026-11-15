---
id: learning.zephyr-docs.api-source-supplement-reference.page-189
title: stm32_dma.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32__dma_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第189章\_stm32\_dma.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32__dma_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/stm32__dma_8h.html)。

## 189.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
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
<a id="l00073"></a>
<a id="l00074"></a>

```c
/*
 * Copyright (c) 2023 STMicroelectronics
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_DMA_STM32_DMA_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_DMA_STM32_DMA_H_

#define STM32_DMA_CH_CFG_MODE(val)              ((val & 0x1) << 5)
#define STM32_DMA_MODE_NORMAL                   STM32_DMA_CH_CFG_MODE(0)
#define STM32_DMA_MODE_CYCLIC                   STM32_DMA_CH_CFG_MODE(1)

#define STM32_DMA_CH_CFG_DIRECTION(val)         ((val & 0x3) << 6)
#define STM32_DMA_MEMORY_TO_MEMORY              STM32_DMA_CH_CFG_DIRECTION(0)
#define STM32_DMA_MEMORY_TO_PERIPH              STM32_DMA_CH_CFG_DIRECTION(1)
#define STM32_DMA_PERIPH_TO_MEMORY              STM32_DMA_CH_CFG_DIRECTION(2)
#define STM32_DMA_PERIPH_TO_PERIPH              STM32_DMA_CH_CFG_DIRECTION(3)

#define STM32_DMA_CH_CFG_PERIPH_ADDR_INC(val)   ((val & 0x1) << 9)
#define STM32_DMA_PERIPH_NO_INC                 STM32_DMA_CH_CFG_PERIPH_ADDR_INC(0)
#define STM32_DMA_PERIPH_INC                    STM32_DMA_CH_CFG_PERIPH_ADDR_INC(1)

#define STM32_DMA_CH_CFG_MEM_ADDR_INC(val)      ((val & 0x1) << 10)
#define STM32_DMA_MEM_NO_INC                    STM32_DMA_CH_CFG_MEM_ADDR_INC(0)
#define STM32_DMA_MEM_INC                       STM32_DMA_CH_CFG_MEM_ADDR_INC(1)

#define STM32_DMA_CH_CFG_PERIPH_WIDTH(val)      ((val & 0x3) << 11)
#define STM32_DMA_PERIPH_8BITS                  STM32_DMA_CH_CFG_PERIPH_WIDTH(0)
#define STM32_DMA_PERIPH_16BITS                 STM32_DMA_CH_CFG_PERIPH_WIDTH(1)
#define STM32_DMA_PERIPH_32BITS                 STM32_DMA_CH_CFG_PERIPH_WIDTH(2)

#define STM32_DMA_CH_CFG_MEM_WIDTH(val)         ((val & 0x3) << 13)
#define STM32_DMA_MEM_8BITS                     STM32_DMA_CH_CFG_MEM_WIDTH(0)
#define STM32_DMA_MEM_16BITS                    STM32_DMA_CH_CFG_MEM_WIDTH(1)
#define STM32_DMA_MEM_32BITS                    STM32_DMA_CH_CFG_MEM_WIDTH(2)

#define STM32_DMA_CH_CFG_PERIPH_INC_FIXED(val)  ((val & 0x1) << 15)
#define STM32_DMA_OFFSET_LINKED_BUS             STM32_DMA_CH_CFG_PERIPH_INC_FIXED(0)
#define STM32_DMA_OFFSET_FIXED_4                STM32_DMA_CH_CFG_PERIPH_INC_FIXED(1)

#define STM32_DMA_CH_CFG_PRIORITY(val)          ((val & 0x3) << 16)
#define STM32_DMA_PRIORITY_LOW                  STM32_DMA_CH_CFG_PRIORITY(0)
#define STM32_DMA_PRIORITY_MEDIUM               STM32_DMA_CH_CFG_PRIORITY(1)
#define STM32_DMA_PRIORITY_HIGH                 STM32_DMA_CH_CFG_PRIORITY(2)
#define STM32_DMA_PRIORITY_VERY_HIGH            STM32_DMA_CH_CFG_PRIORITY(3)

#define STM32_DMA_FIFO_1_4                      0U
#define STM32_DMA_FIFO_HALF                     1U
#define STM32_DMA_FIFO_3_4                      2U
#define STM32_DMA_FIFO_FULL                     3U

/* DMA  usual combination for peripheral transfer */
#define STM32_DMA_PERIPH_TX     (STM32_DMA_MEMORY_TO_PERIPH | STM32_DMA_MEM_INC)
#define STM32_DMA_PERIPH_RX     (STM32_DMA_PERIPH_TO_MEMORY | STM32_DMA_MEM_INC)

#define STM32_DMA_16BITS        (STM32_DMA_PERIPH_16BITS | STM32_DMA_MEM_16BITS)
#define STM32_DMA_32BITS        (STM32_DMA_PERIPH_32BITS | STM32_DMA_MEM_32BITS)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_DMA_STM32_DMA_H_ */
```

## 189.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 STMicroelectronics。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 65 行

外设传输常用的 DMA 组合。

### 注释 3：原第 74 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_DMA_STM32_DMA_H_`。

## 189.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/stm32__dma_8h.html)

---

[上一章](P188_stm32_dcmipp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P190_stm32_pwr.h_源码浏览.md)
