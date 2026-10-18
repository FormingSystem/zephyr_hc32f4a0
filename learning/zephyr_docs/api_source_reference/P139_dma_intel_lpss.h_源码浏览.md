---
id: learning.zephyr-docs.api-source-reference.page-139
title: dma_intel_lpss.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dma__intel__lpss_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第139章\_dma\_intel\_lpss.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dma__intel__lpss_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dma__intel__lpss_8h.html)。

## 139.1\_原始可见代码（Source Code）

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
<a id="adma__intel__lpss_8h_html_a4a5438ab5a164e80c0564fc73e8b9764"></a>
<a id="adma__intel__lpss_8h_html_a769db0413f8ca5fe4c03d1701581edfa"></a>
<a id="adma__intel__lpss_8h_html_aaf5eefbe0476083a87e5c2724a99a73d"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2023 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_INTEL_LPSS_H_
#define ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_INTEL_LPSS_H_

#define DMA_INTEL_LPSS_OFFSET           0x800
#define DMA_INTEL_LPSS_REMAP_LOW        0x240
#define DMA_INTEL_LPSS_REMAP_HI         0x244
#define DMA_INTEL_LPSS_TX_CHAN          0
#define DMA_INTEL_LPSS_RX_CHAN          1
#define DMA_INTEL_LPSS_ADDR_RIGHT_SHIFT 32

void dma_intel_lpss_isr(const struct device *dev);
int dma_intel_lpss_setup(const struct device *dev);
void dma_intel_lpss_set_base(const struct device *dev, uintptr_t base);

#endif /* ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_INTEL_LPSS_H_ */
```

## 139.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 21 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_INTEL_LPSS_H_`。

## 139.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dma__intel__lpss_8h.html)
- [dma_intel_lpss_isr](https://docs.zephyrproject.org/latest/doxygen/html/dma__intel__lpss_8h.html#a769db0413f8ca5fe4c03d1701581edfa)
- [device](../device_reference/P002_设备对象结构.md)
- [dma_intel_lpss_setup](https://docs.zephyrproject.org/latest/doxygen/html/dma__intel__lpss_8h.html#a4a5438ab5a164e80c0564fc73e8b9764)
- [dma_intel_lpss_set_base](https://docs.zephyrproject.org/latest/doxygen/html/dma__intel__lpss_8h.html#aaf5eefbe0476083a87e5c2724a99a73d)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)

---

[上一章](P138_dma_gd32.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P140_dma_mcux_smartdma.h_源码浏览.md)
