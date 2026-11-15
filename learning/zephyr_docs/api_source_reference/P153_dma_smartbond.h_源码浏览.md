---
id: learning.zephyr-docs.api-source-reference.page-153
title: dma_smartbond.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2dma_2dma__smartbond_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第153章\_dma\_smartbond.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2dma_2dma__smartbond_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2dma_2dma__smartbond_8h.html)。

## 153.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="foldopen00017"></a>
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
<a id="adrivers_2dma_2dma__smartbond_8h_html_a82ef8a416596bd147cea250945dc6136"></a>
<a id="adt-bindings_2dma_2dma__smartbond_8h_html_a0cf51e3db0f0472b36341156544bb218"></a>
<a id="adt-bindings_2dma_2dma__smartbond_8h_html_a1965f7b0abbebba2b44416f9c93ce793"></a>
<a id="adt-bindings_2dma_2dma__smartbond_8h_html_a4aa0cf2a75acd5ca0359cdbddc94c2f0"></a>
<a id="adt-bindings_2dma_2dma__smartbond_8h_html_a59c1d5957912ee64584e4894b4c40c11"></a>
<a id="adt-bindings_2dma_2dma__smartbond_8h_html_a6ea3dfcb21bff83188ddb328a6e8bdb0"></a>
<a id="adt-bindings_2dma_2dma__smartbond_8h_html_a732d794d46d67f039d3b88e172f447e7"></a>
<a id="adt-bindings_2dma_2dma__smartbond_8h_html_a792383e4160b8256a28b4c98508e082a"></a>
<a id="adt-bindings_2dma_2dma__smartbond_8h_html_ab2553e825d7559636ba33894a4744bf6"></a>
<a id="adt-bindings_2dma_2dma__smartbond_8h_html_abb1a1462a91080511fc9d94bba685a2b"></a>
<a id="adt-bindings_2dma_2dma__smartbond_8h_html_abcd3ac0c66ee89f6cdec303f8e1bfe39"></a>
<a id="adt-bindings_2dma_2dma__smartbond_8h_html_ad5762fefff49d30ec23932af767ced7f"></a>
<a id="adt-bindings_2dma_2dma__smartbond_8h_html_ae4b382b67096e708e0b57ee6ec52a9f0"></a>
<a id="adt-bindings_2dma_2dma__smartbond_8h_html_af46b07be1f5058057addc6b574caf5d8"></a>

```c
/*
 * Copyright (c) 2023 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_SMARTBOND_H_
#define ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_SMARTBOND_H_

enum dma_smartbond_trig_mux {
        DMA_SMARTBOND_TRIG_MUX_SPI   = 0x0,
        DMA_SMARTBOND_TRIG_MUX_SPI2  = 0x1,
        DMA_SMARTBOND_TRIG_MUX_UART  = 0x2,
        DMA_SMARTBOND_TRIG_MUX_UART2 = 0x3,
        DMA_SMARTBOND_TRIG_MUX_I2C   = 0x4,
        DMA_SMARTBOND_TRIG_MUX_I2C2  = 0x5,
        DMA_SMARTBOND_TRIG_MUX_USB   = 0x6,
        DMA_SMARTBOND_TRIG_MUX_UART3 = 0x7,
        DMA_SMARTBOND_TRIG_MUX_PCM   = 0x8,
        DMA_SMARTBOND_TRIG_MUX_SRC   = 0x9,
        DMA_SMARTBOND_TRIG_MUX_GPADC = 0xC,
        DMA_SMARTBOND_TRIG_MUX_SDADC = 0xD,
        DMA_SMARTBOND_TRIG_MUX_NONE  = 0xF
};

#endif /* ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_SMARTBOND_H_ */
```

## 153.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 33 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_SMARTBOND_H_`。

## 153.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2dma_2dma__smartbond_8h.html)
- [dma_smartbond_trig_mux](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2dma_2dma__smartbond_8h.html#a82ef8a416596bd147cea250945dc6136)
- [DMA_SMARTBOND_TRIG_MUX_SPI](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2dma_2dma__smartbond_8h.html#af46b07be1f5058057addc6b574caf5d8)
- [DMA_SMARTBOND_TRIG_MUX_SPI2](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2dma_2dma__smartbond_8h.html#a1965f7b0abbebba2b44416f9c93ce793)
- [DMA_SMARTBOND_TRIG_MUX_UART](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2dma_2dma__smartbond_8h.html#a732d794d46d67f039d3b88e172f447e7)
- [DMA_SMARTBOND_TRIG_MUX_UART2](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2dma_2dma__smartbond_8h.html#ad5762fefff49d30ec23932af767ced7f)
- [DMA_SMARTBOND_TRIG_MUX_I2C](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2dma_2dma__smartbond_8h.html#a59c1d5957912ee64584e4894b4c40c11)
- [DMA_SMARTBOND_TRIG_MUX_I2C2](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2dma_2dma__smartbond_8h.html#a0cf51e3db0f0472b36341156544bb218)
- [DMA_SMARTBOND_TRIG_MUX_USB](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2dma_2dma__smartbond_8h.html#ae4b382b67096e708e0b57ee6ec52a9f0)
- [DMA_SMARTBOND_TRIG_MUX_UART3](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2dma_2dma__smartbond_8h.html#abcd3ac0c66ee89f6cdec303f8e1bfe39)
- [DMA_SMARTBOND_TRIG_MUX_PCM](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2dma_2dma__smartbond_8h.html#ab2553e825d7559636ba33894a4744bf6)
- [DMA_SMARTBOND_TRIG_MUX_SRC](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2dma_2dma__smartbond_8h.html#a6ea3dfcb21bff83188ddb328a6e8bdb0)
- [DMA_SMARTBOND_TRIG_MUX_GPADC](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2dma_2dma__smartbond_8h.html#a4aa0cf2a75acd5ca0359cdbddc94c2f0)
- [DMA_SMARTBOND_TRIG_MUX_SDADC](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2dma_2dma__smartbond_8h.html#a792383e4160b8256a28b4c98508e082a)
- [DMA_SMARTBOND_TRIG_MUX_NONE](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2dma_2dma__smartbond_8h.html#abb1a1462a91080511fc9d94bba685a2b)

---

[上一章](P152_crc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P154_cpu.h_源码浏览.md)
