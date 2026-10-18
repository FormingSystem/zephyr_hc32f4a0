---
id: learning.zephyr-docs.api-source-reference.page-141
title: dma_silabs_ldma.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dma__silabs__ldma_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第141章\_dma\_silabs\_ldma.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dma__silabs__ldma_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dma__silabs__ldma_8h.html)。

## 141.1\_原始可见代码（Source Code）

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
<a id="foldopen00018"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="foldopen00022"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="adma__silabs__ldma_8h_html_a5f6501ec9e73cb8a3be76c418ebf1456"></a>
<a id="adrivers_2dma_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructdevice_html"></a>
<a id="astructdma__config_html"></a>

```c
/*
 * Copyright (c) 2025 Silicon Laboratories Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_SILABS_LDMA_H_
#define ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_SILABS_LDMA_H_

#include <zephyr/drivers/dma.h>

#define SILABS_LDMA_SOURCE_MASK  GENMASK(21, 16)
#define SILABS_LDMA_SIG_MASK     GENMASK(3, 0)

#define SILABS_DMA_SLOT_SOURCE_MASK  GENMASK(7, 3)
#define SILABS_DMA_SLOT_SIG_MASK     GENMASK(2, 0)

#define SILABS_LDMA_REQSEL_TO_SLOT(signal)             \
        FIELD_PREP(SILABS_DMA_SLOT_SOURCE_MASK, FIELD_GET(SILABS_LDMA_SOURCE_MASK, signal)) | \
        FIELD_PREP(SILABS_DMA_SLOT_SIG_MASK, FIELD_GET(SILABS_LDMA_SIG_MASK, signal))

#define SILABS_LDMA_SLOT_TO_REQSEL(slot)     \
        FIELD_PREP(SILABS_LDMA_SOURCE_MASK, FIELD_GET(SILABS_DMA_SLOT_SOURCE_MASK, slot)) | \
        FIELD_PREP(SILABS_LDMA_SIG_MASK, FIELD_GET(SILABS_DMA_SLOT_SIG_MASK, slot))

int silabs_ldma_append_block(const struct device *dev, uint32_t channel,
                                        struct dma_config *config);

#endif /* ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_SILABS_LDMA_H_ */
```

## 141.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Silicon Laboratories Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 46 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_SILABS_LDMA_H_`。

## 141.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dma__silabs__ldma_8h.html)
- [zephyr/drivers/dma.h](../dma_reference/P009_DMA驱动头文件参考.md)
- [silabs_ldma_append_block](https://docs.zephyrproject.org/latest/doxygen/html/dma__silabs__ldma_8h.html#a5f6501ec9e73cb8a3be76c418ebf1456)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [dma_config](../dma_reference/P004_DMA通道配置.md)
- [dma.h](../dma_reference/P009_DMA驱动头文件参考.md)

---

[上一章](P140_dma_mcux_smartdma.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P142_dma_xilinx_adma.h_源码浏览.md)
