---
id: learning.zephyr-docs.api-source-reference.page-28
title: ameba_dma.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ameba__dma_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_ameba\_dma.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ameba__dma_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ameba__dma_8h.html)。

## 28.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00017"></a>
<a id="l00022"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="foldopen00194"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="foldopen00202"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00206"></a>
<a id="l00207"></a>

```c
/*
 * Copyright (c) 2026 Realtek Semiconductor Corp.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_DMA_AMEBA_DMA_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_DMA_AMEBA_DMA_H_



#define AMEBA_DMA_CH_DIR_SET(val) ((val & 0x3) << 0)

#define AMEBA_DMA_MEMORY_TO_MEMORY AMEBA_DMA_CH_DIR_SET(0)

#define AMEBA_DMA_MEMORY_TO_PERIPH AMEBA_DMA_CH_DIR_SET(1)

#define AMEBA_DMA_PERIPH_TO_MEMORY AMEBA_DMA_CH_DIR_SET(2)

#define AMEBA_DMA_PERIPH_TO_PERIPH AMEBA_DMA_CH_DIR_SET(3)

#define AMEBA_DMA_SRC_ADDR_ADJ_SET(val) ((val & 0x3) << 2)

#define AMEBA_DMA_SRC_ADDR_ADJ_INC AMEBA_DMA_SRC_ADDR_ADJ_SET(0)

#define AMEBA_DMA_SRC_ADDR_ADJ_NO_CHANGE AMEBA_DMA_SRC_ADDR_ADJ_SET(2)

#define AMEBA_DMA_DST_ADDR_ADJ_SET(val) ((val & 0x3) << 4)

#define AMEBA_DMA_DST_ADDR_ADJ_INC AMEBA_DMA_DST_ADDR_ADJ_SET(0)

#define AMEBA_DMA_DST_ADDR_ADJ_NO_CHANGE AMEBA_DMA_DST_ADDR_ADJ_SET(2)

#define AMEBA_DMA_SRC_DATA_SIZE_SET(val) ((val & 0x7) << 6)

#define AMEBA_DMA_SRC_WIDTH_8BITS AMEBA_DMA_SRC_DATA_SIZE_SET(0)

#define AMEBA_DMA_SRC_WIDTH_16BITS AMEBA_DMA_SRC_DATA_SIZE_SET(1)

#define AMEBA_DMA_SRC_WIDTH_32BITS AMEBA_DMA_SRC_DATA_SIZE_SET(2)

#define AMEBA_DMA_DST_DATA_SIZE_SET(val) ((val & 0x7) << 9)

#define AMEBA_DMA_DST_WIDTH_8BITS AMEBA_DMA_DST_DATA_SIZE_SET(0)

#define AMEBA_DMA_DST_WIDTH_16BITS AMEBA_DMA_DST_DATA_SIZE_SET(1)

#define AMEBA_DMA_DST_WIDTH_32BITS AMEBA_DMA_DST_DATA_SIZE_SET(2)

#define AMEBA_DMA_SRC_BURST_SET(val) ((val & 0x1F) << 12)

#define AMEBA_DMA_SRC_BURST_ONE AMEBA_DMA_SRC_BURST_SET(0)

#define AMEBA_DMA_SRC_BURST_FOUR AMEBA_DMA_SRC_BURST_SET(1)

#define AMEBA_DMA_SRC_BURST_EIGHT AMEBA_DMA_SRC_BURST_SET(2)

#define AMEBA_DMA_SRC_BURST_SIXTEEN AMEBA_DMA_SRC_BURST_SET(3)

#define AMEBA_DMA_DST_BURST_SET(val) ((val & 0x1F) << 17)

#define AMEBA_DMA_DST_BURST_ONE AMEBA_DMA_DST_BURST_SET(0)

#define AMEBA_DMA_DST_BURST_FOUR AMEBA_DMA_DST_BURST_SET(1)

#define AMEBA_DMA_DST_BURST_EIGHT AMEBA_DMA_DST_BURST_SET(2)

#define AMEBA_DMA_DST_BURST_SIXTEEN AMEBA_DMA_DST_BURST_SET(3)

#define AMEBA_DMA_CH_PRIORITY_SET(val) ((val & 0x7) << 22)

#define AMEBA_DMA_PERIPH_TX                                                                        \
        (AMEBA_DMA_MEMORY_TO_PERIPH | AMEBA_DMA_SRC_ADDR_ADJ_INC | AMEBA_DMA_DST_ADDR_ADJ_NO_CHANGE)

#define AMEBA_DMA_PERIPH_RX                                                                        \
        (AMEBA_DMA_PERIPH_TO_MEMORY | AMEBA_DMA_SRC_ADDR_ADJ_NO_CHANGE | AMEBA_DMA_DST_ADDR_ADJ_INC)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_DMA_AMEBA_DMA_H_ */
```

## 28.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Realtek Semiconductor Corp.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 207 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_DMA_AMEBA_DMA_H_`。

## 28.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ameba__dma_8h.html)

---

[上一章](P027_ambiq-apollo5-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P029_amebag2-pinctrl.h_源码浏览.md)
