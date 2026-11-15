---
id: learning.zephyr-docs.api-source-reference.page-137
title: dma_esp32.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dma__esp32_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第137章\_dma\_esp32.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dma__esp32_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dma__esp32_8h.html)。

## 137.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="foldopen00010"></a>
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
<a id="foldopen00028"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="foldopen00033"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="adma__esp32_8h_html_a45ccc721bb7cd992658cc180f34cf327"></a>
<a id="adma__esp32_8h_html_a45ccc721bb7cd992658cc180f34cf327a0445fd580e2f953978c59756b6d3f663"></a>
<a id="adma__esp32_8h_html_a45ccc721bb7cd992658cc180f34cf327a2510728ddf6355787f9ad566f3e9c65a"></a>
<a id="adma__esp32_8h_html_a45ccc721bb7cd992658cc180f34cf327a38744227c79336f2db9e6fd14d8c805c"></a>
<a id="adma__esp32_8h_html_a45ccc721bb7cd992658cc180f34cf327a3cd1f282d8c5eeb69d5dc396a638f51a"></a>
<a id="adma__esp32_8h_html_a45ccc721bb7cd992658cc180f34cf327a4499557060bcd39e13bb9273133de6f2"></a>
<a id="adma__esp32_8h_html_a45ccc721bb7cd992658cc180f34cf327a52ce4370e4d1ab49ac75d36ef369ed7b"></a>
<a id="adma__esp32_8h_html_a45ccc721bb7cd992658cc180f34cf327a7708a6f78ebeffeb1339a3f3fc46805b"></a>
<a id="adma__esp32_8h_html_a45ccc721bb7cd992658cc180f34cf327a7901089e4ae68dd2b40a6bacadf77c5e"></a>
<a id="adma__esp32_8h_html_a45ccc721bb7cd992658cc180f34cf327a8c184ff1753827aaf1977acce3610459"></a>
<a id="adma__esp32_8h_html_a45ccc721bb7cd992658cc180f34cf327ab2c7701395a9d82a0ed9c4bb4e8253e3"></a>
<a id="adma__esp32_8h_html_a45ccc721bb7cd992658cc180f34cf327abf4d4ff0fa74f8b37f080cb39b1b7b0d"></a>
<a id="adma__esp32_8h_html_a45ccc721bb7cd992658cc180f34cf327acc572dc1c473a5906c780727da2e2250"></a>
<a id="adma__esp32_8h_html_a45ccc721bb7cd992658cc180f34cf327add6f1747f2a83c9d3aa5ce964f2f778c"></a>
<a id="adma__esp32_8h_html_a45ccc721bb7cd992658cc180f34cf327aedc593bcb0a7a3b45421236ac949016a"></a>
<a id="adma__esp32_8h_html_a45ccc721bb7cd992658cc180f34cf327af3875d4400d233efa891515e4304fdde"></a>

```c
/*
 * Copyright (c) 2022 Espressif Systems (Shanghai) Co., Ltd.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_ESP32_H_
#define ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_ESP32_H_

enum gdma_trigger_peripheral {
        ESP_GDMA_TRIG_PERIPH_M2M = -1,
        ESP_GDMA_TRIG_PERIPH_SPI2 = 0,
        ESP_GDMA_TRIG_PERIPH_SPI3 = 1,
        ESP_GDMA_TRIG_PERIPH_UHCI0 = 2,
        ESP_GDMA_TRIG_PERIPH_I2S0 = 3,
        ESP_GDMA_TRIG_PERIPH_I2S1 = 4,
        ESP_GDMA_TRIG_PERIPH_I2S2 = 5,
        ESP_GDMA_TRIG_PERIPH_LCD0 = 5,
        ESP_GDMA_TRIG_PERIPH_CAM0 = 5,
        ESP_GDMA_TRIG_PERIPH_AES = 6,
        ESP_GDMA_TRIG_PERIPH_SHA = 7,
        ESP_GDMA_TRIG_PERIPH_ADC0 = 8,
        ESP_GDMA_TRIG_PERIPH_DAC0 = 8,
        ESP_GDMA_TRIG_PERIPH_RMT = 9,
        ESP_GDMA_TRIG_PERIPH_INVALID = 0x3F,
};

#define ESP32_DT_INST_DMA_CTLR(n, name)                 \
        COND_CODE_1(DT_INST_NODE_HAS_PROP(n, dmas),             \
                    (DEVICE_DT_GET(DT_INST_DMAS_CTLR_BY_NAME(n, name))),        \
                    (NULL))

#define ESP32_DT_INST_DMA_CELL(n, name, cell)           \
        COND_CODE_1(DT_INST_NODE_HAS_PROP(n, dmas),             \
                    (DT_INST_DMAS_CELL_BY_NAME(n, name, cell)), \
                    (0xff))


#endif /* ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_ESP32_H_ */
```

## 137.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Espressif Systems (Shanghai) Co., Ltd.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 39 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_ESP32_H_`。

## 137.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dma__esp32_8h.html)
- [gdma_trigger_peripheral](https://docs.zephyrproject.org/latest/doxygen/html/dma__esp32_8h.html#a45ccc721bb7cd992658cc180f34cf327)
- [ESP_GDMA_TRIG_PERIPH_M2M](https://docs.zephyrproject.org/latest/doxygen/html/dma__esp32_8h.html#a45ccc721bb7cd992658cc180f34cf327a52ce4370e4d1ab49ac75d36ef369ed7b)
- [ESP_GDMA_TRIG_PERIPH_SPI2](https://docs.zephyrproject.org/latest/doxygen/html/dma__esp32_8h.html#a45ccc721bb7cd992658cc180f34cf327af3875d4400d233efa891515e4304fdde)
- [ESP_GDMA_TRIG_PERIPH_SPI3](https://docs.zephyrproject.org/latest/doxygen/html/dma__esp32_8h.html#a45ccc721bb7cd992658cc180f34cf327acc572dc1c473a5906c780727da2e2250)
- [ESP_GDMA_TRIG_PERIPH_UHCI0](https://docs.zephyrproject.org/latest/doxygen/html/dma__esp32_8h.html#a45ccc721bb7cd992658cc180f34cf327a7708a6f78ebeffeb1339a3f3fc46805b)
- [ESP_GDMA_TRIG_PERIPH_I2S0](https://docs.zephyrproject.org/latest/doxygen/html/dma__esp32_8h.html#a45ccc721bb7cd992658cc180f34cf327add6f1747f2a83c9d3aa5ce964f2f778c)
- [ESP_GDMA_TRIG_PERIPH_I2S1](https://docs.zephyrproject.org/latest/doxygen/html/dma__esp32_8h.html#a45ccc721bb7cd992658cc180f34cf327a2510728ddf6355787f9ad566f3e9c65a)
- [ESP_GDMA_TRIG_PERIPH_I2S2](https://docs.zephyrproject.org/latest/doxygen/html/dma__esp32_8h.html#a45ccc721bb7cd992658cc180f34cf327abf4d4ff0fa74f8b37f080cb39b1b7b0d)
- [ESP_GDMA_TRIG_PERIPH_LCD0](https://docs.zephyrproject.org/latest/doxygen/html/dma__esp32_8h.html#a45ccc721bb7cd992658cc180f34cf327a4499557060bcd39e13bb9273133de6f2)
- [ESP_GDMA_TRIG_PERIPH_CAM0](https://docs.zephyrproject.org/latest/doxygen/html/dma__esp32_8h.html#a45ccc721bb7cd992658cc180f34cf327ab2c7701395a9d82a0ed9c4bb4e8253e3)
- [ESP_GDMA_TRIG_PERIPH_AES](https://docs.zephyrproject.org/latest/doxygen/html/dma__esp32_8h.html#a45ccc721bb7cd992658cc180f34cf327a7901089e4ae68dd2b40a6bacadf77c5e)
- [ESP_GDMA_TRIG_PERIPH_SHA](https://docs.zephyrproject.org/latest/doxygen/html/dma__esp32_8h.html#a45ccc721bb7cd992658cc180f34cf327a0445fd580e2f953978c59756b6d3f663)
- [ESP_GDMA_TRIG_PERIPH_ADC0](https://docs.zephyrproject.org/latest/doxygen/html/dma__esp32_8h.html#a45ccc721bb7cd992658cc180f34cf327a38744227c79336f2db9e6fd14d8c805c)
- [ESP_GDMA_TRIG_PERIPH_DAC0](https://docs.zephyrproject.org/latest/doxygen/html/dma__esp32_8h.html#a45ccc721bb7cd992658cc180f34cf327aedc593bcb0a7a3b45421236ac949016a)
- [ESP_GDMA_TRIG_PERIPH_RMT](https://docs.zephyrproject.org/latest/doxygen/html/dma__esp32_8h.html#a45ccc721bb7cd992658cc180f34cf327a3cd1f282d8c5eeb69d5dc396a638f51a)
- [ESP_GDMA_TRIG_PERIPH_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/dma__esp32_8h.html#a45ccc721bb7cd992658cc180f34cf327a8c184ff1753827aaf1977acce3610459)

---

[上一章](P136_sf32lb.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P138_dma_gd32.h_源码浏览.md)
