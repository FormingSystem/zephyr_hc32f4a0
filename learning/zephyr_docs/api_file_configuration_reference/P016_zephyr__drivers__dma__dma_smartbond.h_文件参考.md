---
id: learning.zephyr-docs.api-file-configuration-reference.page-16
title: zephyr__drivers__dma__dma_smartbond.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2dma_2dma__smartbond_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_zephyr\_\_drivers\_\_dma\_\_dma\_smartbond.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2dma_2dma__smartbond_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 16.1\_枚举（Enumerations）

<a id="r_a82ef8a416596bd147cea250945dc6136"></a>

```c
enum dma_smartbond_trig_mux { DMA_SMARTBOND_TRIG_MUX_SPI = 0x0 , DMA_SMARTBOND_TRIG_MUX_SPI2 = 0x1 , DMA_SMARTBOND_TRIG_MUX_UART = 0x2 , DMA_SMARTBOND_TRIG_MUX_UART2 = 0x3 , DMA_SMARTBOND_TRIG_MUX_I2C = 0x4 , DMA_SMARTBOND_TRIG_MUX_I2C2 = 0x5 , DMA_SMARTBOND_TRIG_MUX_USB = 0x6 , DMA_SMARTBOND_TRIG_MUX_UART3 = 0x7 , DMA_SMARTBOND_TRIG_MUX_PCM = 0x8 , DMA_SMARTBOND_TRIG_MUX_SRC = 0x9 , DMA_SMARTBOND_TRIG_MUX_GPADC = 0xC , DMA_SMARTBOND_TRIG_MUX_SDADC = 0xD , DMA_SMARTBOND_TRIG_MUX_NONE = 0xF }
```

相关声明：[dma_smartbond_trig_mux](#a82ef8a416596bd147cea250945dc6136)、[DMA_SMARTBOND_TRIG_MUX_SPI](#a82ef8a416596bd147cea250945dc6136afaf3c2577a95e306db93baa987d68f8f)、[DMA_SMARTBOND_TRIG_MUX_SPI2](#a82ef8a416596bd147cea250945dc6136ac36c296af5ee6ca8625fe9d9988bcaf6)、[DMA_SMARTBOND_TRIG_MUX_UART](#a82ef8a416596bd147cea250945dc6136af8a02b7a018fdc550d9f9aec6486815e)、[DMA_SMARTBOND_TRIG_MUX_UART2](#a82ef8a416596bd147cea250945dc6136a57a6a0f375a2f347562f0f131bbb4aef)、[DMA_SMARTBOND_TRIG_MUX_I2C](#a82ef8a416596bd147cea250945dc6136a4123d0b00586145b5a490ef77a8f49eb)、[DMA_SMARTBOND_TRIG_MUX_I2C2](#a82ef8a416596bd147cea250945dc6136a08c27af5011f2efa6617d46009cd52f9)、[DMA_SMARTBOND_TRIG_MUX_USB](#a82ef8a416596bd147cea250945dc6136a7de5184361a3d494c144d968c696b42e)、[DMA_SMARTBOND_TRIG_MUX_UART3](#a82ef8a416596bd147cea250945dc6136ae0a75a1957c1147ead700bb0132526eb)、[DMA_SMARTBOND_TRIG_MUX_PCM](#a82ef8a416596bd147cea250945dc6136ab8c5550e628eec592369100aa4b28fd1)、[DMA_SMARTBOND_TRIG_MUX_SRC](#a82ef8a416596bd147cea250945dc6136a082f64dec61621f93ae6066917d3751d)、[DMA_SMARTBOND_TRIG_MUX_GPADC](#a82ef8a416596bd147cea250945dc6136a2a60d9a63af958a3cd66818e83a97286)、[DMA_SMARTBOND_TRIG_MUX_SDADC](#a82ef8a416596bd147cea250945dc6136a4a01f6631dc9050c65121bb5fd5b7b66)、[DMA_SMARTBOND_TRIG_MUX_NONE](#a82ef8a416596bd147cea250945dc6136a72a2552fde29d6d2c6dff01afb9363c4)。

厂商特定的 DMA 外设触发源（Vendor-Specific DMA Peripheral Triggering Sources）。

## 16.2\_详细说明（Detailed Documentation）

<a id="a82ef8a416596bd147cea250945dc6136"></a>

### `dma_smartbond_trig_mux`

```c
enum dma_smartbond_trig_mux
```

厂商特定的 DMA 外设触发源（Vendor-Specific DMA Peripheral Triggering Sources）。

将 DMA 配置为外设到外设（Peripheral-to-Peripheral）或内存到外设（Memory-to-Peripheral）传输时，应提供有效的触发源（Triggering Source）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `DMA_SMARTBOND_TRIG_MUX_SPI` |  |
| `DMA_SMARTBOND_TRIG_MUX_SPI2` |  |
| `DMA_SMARTBOND_TRIG_MUX_UART` |  |
| `DMA_SMARTBOND_TRIG_MUX_UART2` |  |
| `DMA_SMARTBOND_TRIG_MUX_I2C` |  |
| `DMA_SMARTBOND_TRIG_MUX_I2C2` |  |
| `DMA_SMARTBOND_TRIG_MUX_USB` |  |
| `DMA_SMARTBOND_TRIG_MUX_UART3` |  |
| `DMA_SMARTBOND_TRIG_MUX_PCM` |  |
| `DMA_SMARTBOND_TRIG_MUX_SRC` |  |
| `DMA_SMARTBOND_TRIG_MUX_GPADC` |  |
| `DMA_SMARTBOND_TRIG_MUX_SDADC` |  |
| `DMA_SMARTBOND_TRIG_MUX_NONE` |  |


## 16.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P153_dma_smartbond.h_源码浏览.md)

<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a82ef8a416596bd147cea250945dc6136afaf3c2577a95e306db93baa987d68f8f"></a>
<a id="a82ef8a416596bd147cea250945dc6136ac36c296af5ee6ca8625fe9d9988bcaf6"></a>
<a id="a82ef8a416596bd147cea250945dc6136af8a02b7a018fdc550d9f9aec6486815e"></a>
<a id="a82ef8a416596bd147cea250945dc6136a57a6a0f375a2f347562f0f131bbb4aef"></a>
<a id="a82ef8a416596bd147cea250945dc6136a4123d0b00586145b5a490ef77a8f49eb"></a>
<a id="a82ef8a416596bd147cea250945dc6136a08c27af5011f2efa6617d46009cd52f9"></a>
<a id="a82ef8a416596bd147cea250945dc6136a7de5184361a3d494c144d968c696b42e"></a>
<a id="a82ef8a416596bd147cea250945dc6136ae0a75a1957c1147ead700bb0132526eb"></a>
<a id="a82ef8a416596bd147cea250945dc6136ab8c5550e628eec592369100aa4b28fd1"></a>
<a id="a82ef8a416596bd147cea250945dc6136a082f64dec61621f93ae6066917d3751d"></a>
<a id="a82ef8a416596bd147cea250945dc6136a2a60d9a63af958a3cd66818e83a97286"></a>
<a id="a82ef8a416596bd147cea250945dc6136a4a01f6631dc9050c65121bb5fd5b7b66"></a>
<a id="a82ef8a416596bd147cea250945dc6136a72a2552fde29d6d2c6dff01afb9363c4"></a>

---

[上一章](P015_zephyr__bluetooth__mesh__dfd_srv.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P017_zephyr__drivers__sensor__afbr_s50.h_文件参考.md)
