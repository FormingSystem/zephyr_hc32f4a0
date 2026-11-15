---
id: learning.zephyr-docs.api-source-runtime-reference.page-12
title: dma_bee.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dma__bee_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_dma\_bee.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dma__bee_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dma__bee_8h.html)。

## 12.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00026"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="foldopen00131"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="foldopen00151"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00167"></a>

```c
/*
 * Copyright (c) 2026, Realtek Semiconductor Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_BEE_H_
#define ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_BEE_H_


#define BEE_DMA_CTLR(id, dir)           DT_INST_DMAS_CTLR_BY_NAME(id, dir)

#define BEE_DMA_CHANNEL_CONFIG(id, dir) DT_INST_DMAS_CELL_BY_NAME(id, dir, config)

/* -------------------------------------------------------------------------- */
/* Channel Configuration Extraction Macros                                    */
/* -------------------------------------------------------------------------- */

#define BEE_DMA_CONFIG_DIRECTION(config) ((config >> 0) & 0x3)

#define BEE_DMA_CONFIG_SOURCE_ADDR_INC(config) ((config >> 2) & 0x3)

#define BEE_DMA_CONFIG_DESTINATION_ADDR_INC(config) ((config >> 4) & 0x3)

#define BEE_DMA_CONFIG_SOURCE_DATA_SIZE(config) (1 << ((config >> 6) & 0x3))

#define BEE_DMA_CONFIG_DESTINATION_DATA_SIZE(config) (1 << ((config >> 8) & 0x3))

#define BEE_DMA_CONFIG_SOURCE_MSIZE(config)                                                        \
        ((1 << (((config >> 10) & 0x7) + 1)) - (((config >> 10) & 0x7) == 0 ? 1 : 0))

#define BEE_DMA_CONFIG_DESTINATION_MSIZE(config)                                                   \
        ((1 << (((config >> 13) & 0x7) + 1)) - (((config >> 13) & 0x7) == 0 ? 1 : 0))

#define BEE_DMA_CONFIG_PRIORITY(config) ((config >> 16) & 0x1f)
 /* End of dma_bee_macros group */

#endif /* ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_BEE_H_ */
```

## 12.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026, Realtek Semiconductor Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 45 行

分隔线（Separator）。

### 注释 3：原第 46 行

通道配置提取宏（Channel Configuration Extraction Macros）。

### 注释 4：原第 47 行

分隔线（Separator）。

### 注释 5：原第 164 行

`dma_bee_macros` 分组结束。

### 注释 6：原第 167 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_BEE_H_`。

## 12.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dma__bee_8h.html)

---

[上一章](P011_conn_mgr_connectivity_impl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P013_emul.h_源码浏览.md)
