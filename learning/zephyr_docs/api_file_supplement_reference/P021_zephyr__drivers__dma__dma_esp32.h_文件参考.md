---
id: learning.zephyr-docs.api-file-supplement-reference.page-21
title: zephyr__drivers__dma__dma_esp32.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dma__esp32_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_zephyr\_\_drivers\_\_dma\_\_dma\_esp32.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dma__esp32_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 21.1\_宏定义（Macros）

<a id="r_a73e77297acdb4b1f73e2ad5e0f74d472"></a>

```c
#define ESP32_DT_INST_DMA_CTLR(n, name)
```

相关声明：[ESP32_DT_INST_DMA_CTLR](#a73e77297acdb4b1f73e2ad5e0f74d472)。

<a id="r_a9ec5b758fb8c44f3e0e1005e9534beb5"></a>

```c
#define ESP32_DT_INST_DMA_CELL(n, name, cell)
```

相关声明：[ESP32_DT_INST_DMA_CELL](#a9ec5b758fb8c44f3e0e1005e9534beb5)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 21.2\_枚举（Enumerations）

<a id="r_a45ccc721bb7cd992658cc180f34cf327"></a>

```c
enum gdma_trigger_peripheral { ESP_GDMA_TRIG_PERIPH_M2M = -1 , ESP_GDMA_TRIG_PERIPH_SPI2 = 0 , ESP_GDMA_TRIG_PERIPH_SPI3 = 1 , ESP_GDMA_TRIG_PERIPH_UHCI0 = 2 , ESP_GDMA_TRIG_PERIPH_I2S0 = 3 , ESP_GDMA_TRIG_PERIPH_I2S1 = 4 , ESP_GDMA_TRIG_PERIPH_I2S2 = 5 , ESP_GDMA_TRIG_PERIPH_LCD0 = 5 , ESP_GDMA_TRIG_PERIPH_CAM0 = 5 , ESP_GDMA_TRIG_PERIPH_AES = 6 , ESP_GDMA_TRIG_PERIPH_SHA = 7 , ESP_GDMA_TRIG_PERIPH_ADC0 = 8 , ESP_GDMA_TRIG_PERIPH_DAC0 = 8 , ESP_GDMA_TRIG_PERIPH_RMT = 9 , ESP_GDMA_TRIG_PERIPH_INVALID = 0x3F }
```

相关声明：[gdma_trigger_peripheral](#a45ccc721bb7cd992658cc180f34cf327)、[ESP_GDMA_TRIG_PERIPH_M2M](#a45ccc721bb7cd992658cc180f34cf327a52ce4370e4d1ab49ac75d36ef369ed7b)、[ESP_GDMA_TRIG_PERIPH_SPI2](#a45ccc721bb7cd992658cc180f34cf327af3875d4400d233efa891515e4304fdde)、[ESP_GDMA_TRIG_PERIPH_SPI3](#a45ccc721bb7cd992658cc180f34cf327acc572dc1c473a5906c780727da2e2250)、[ESP_GDMA_TRIG_PERIPH_UHCI0](#a45ccc721bb7cd992658cc180f34cf327a7708a6f78ebeffeb1339a3f3fc46805b)、[ESP_GDMA_TRIG_PERIPH_I2S0](#a45ccc721bb7cd992658cc180f34cf327add6f1747f2a83c9d3aa5ce964f2f778c)、[ESP_GDMA_TRIG_PERIPH_I2S1](#a45ccc721bb7cd992658cc180f34cf327a2510728ddf6355787f9ad566f3e9c65a)、[ESP_GDMA_TRIG_PERIPH_I2S2](#a45ccc721bb7cd992658cc180f34cf327abf4d4ff0fa74f8b37f080cb39b1b7b0d)、[ESP_GDMA_TRIG_PERIPH_LCD0](#a45ccc721bb7cd992658cc180f34cf327a4499557060bcd39e13bb9273133de6f2)、[ESP_GDMA_TRIG_PERIPH_CAM0](#a45ccc721bb7cd992658cc180f34cf327ab2c7701395a9d82a0ed9c4bb4e8253e3)、[ESP_GDMA_TRIG_PERIPH_AES](#a45ccc721bb7cd992658cc180f34cf327a7901089e4ae68dd2b40a6bacadf77c5e)、[ESP_GDMA_TRIG_PERIPH_SHA](#a45ccc721bb7cd992658cc180f34cf327a0445fd580e2f953978c59756b6d3f663)、[ESP_GDMA_TRIG_PERIPH_ADC0](#a45ccc721bb7cd992658cc180f34cf327a38744227c79336f2db9e6fd14d8c805c)、[ESP_GDMA_TRIG_PERIPH_DAC0](#a45ccc721bb7cd992658cc180f34cf327aedc593bcb0a7a3b45421236ac949016a)、[ESP_GDMA_TRIG_PERIPH_RMT](#a45ccc721bb7cd992658cc180f34cf327a3cd1f282d8c5eeb69d5dc396a638f51a)、[ESP_GDMA_TRIG_PERIPH_INVALID](#a45ccc721bb7cd992658cc180f34cf327a8c184ff1753827aaf1977acce3610459)。

## 21.3\_详细说明（Detailed Documentation）

<a id="a9ec5b758fb8c44f3e0e1005e9534beb5"></a>

### `ESP32_DT_INST_DMA_CELL`

```c
#define ESP32_DT_INST_DMA_CELL ( n, name, cell )
```

展开值（Value）：

```c
COND_CODE_1(DT_INST_NODE_HAS_PROP(n, dmas),             \
            (DT_INST_DMAS_CELL_BY_NAME(n, name, cell)), \
            (0xff))
```

<a id="a73e77297acdb4b1f73e2ad5e0f74d472"></a>

### `ESP32_DT_INST_DMA_CTLR`

```c
#define ESP32_DT_INST_DMA_CTLR ( n, name )
```

展开值（Value）：

```c
COND_CODE_1(DT_INST_NODE_HAS_PROP(n, dmas),             \
            (DEVICE_DT_GET(DT_INST_DMAS_CTLR_BY_NAME(n, name))),        \
            (NULL))
```

<a id="a45ccc721bb7cd992658cc180f34cf327"></a>

### `gdma_trigger_peripheral`

```c
enum gdma_trigger_peripheral
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `ESP_GDMA_TRIG_PERIPH_M2M` |  |
| `ESP_GDMA_TRIG_PERIPH_SPI2` |  |
| `ESP_GDMA_TRIG_PERIPH_SPI3` |  |
| `ESP_GDMA_TRIG_PERIPH_UHCI0` |  |
| `ESP_GDMA_TRIG_PERIPH_I2S0` |  |
| `ESP_GDMA_TRIG_PERIPH_I2S1` |  |
| `ESP_GDMA_TRIG_PERIPH_I2S2` | 与 LCD0 和 CAM0 共享触发源 5（Trigger 5）。 |
| `ESP_GDMA_TRIG_PERIPH_LCD0` |  |
| `ESP_GDMA_TRIG_PERIPH_CAM0` |  |
| `ESP_GDMA_TRIG_PERIPH_AES` |  |
| `ESP_GDMA_TRIG_PERIPH_SHA` |  |
| `ESP_GDMA_TRIG_PERIPH_ADC0` |  |
| `ESP_GDMA_TRIG_PERIPH_DAC0` |  |
| `ESP_GDMA_TRIG_PERIPH_RMT` |  |
| `ESP_GDMA_TRIG_PERIPH_INVALID` |  |


## 21.4\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P137_dma_esp32.h_源码浏览.md)
- [COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)
- [DT_INST_NODE_HAS_PROP](../dt_instance_reference/P001_设备树驱动实例宏.md#gaa03419e2d9c887a81e16e96b5947bccb)
- [DT_INST_DMAS_CELL_BY_NAME](../dma_reference/P008_DMA设备树宏.md#ga2cc0124a66cf3b9f1c4c506b7f978d30)
- [DEVICE_DT_GET](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7)
- [DT_INST_DMAS_CTLR_BY_NAME](../dma_reference/P008_DMA设备树宏.md#gad098f0b51ee1f629c1259ca346f49303)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__devicetree-dmas_html_ga2cc0124a66cf3b9f1c4c506b7f978d30"></a>
<a id="agroup__devicetree-inst_html_gaa03419e2d9c887a81e16e96b5947bccb"></a>
<a id="agroup__sys-util_html_ga358bc3e7669c860a98839a51cd526b20"></a>
<a id="agroup__device__model_html_ga9a65996ce21f43acb7db061e23b48ec7"></a>
<a id="agroup__devicetree-dmas_html_gad098f0b51ee1f629c1259ca346f49303"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a45ccc721bb7cd992658cc180f34cf327a52ce4370e4d1ab49ac75d36ef369ed7b"></a>
<a id="a45ccc721bb7cd992658cc180f34cf327af3875d4400d233efa891515e4304fdde"></a>
<a id="a45ccc721bb7cd992658cc180f34cf327acc572dc1c473a5906c780727da2e2250"></a>
<a id="a45ccc721bb7cd992658cc180f34cf327a7708a6f78ebeffeb1339a3f3fc46805b"></a>
<a id="a45ccc721bb7cd992658cc180f34cf327add6f1747f2a83c9d3aa5ce964f2f778c"></a>
<a id="a45ccc721bb7cd992658cc180f34cf327a2510728ddf6355787f9ad566f3e9c65a"></a>
<a id="a45ccc721bb7cd992658cc180f34cf327abf4d4ff0fa74f8b37f080cb39b1b7b0d"></a>
<a id="a45ccc721bb7cd992658cc180f34cf327a4499557060bcd39e13bb9273133de6f2"></a>
<a id="a45ccc721bb7cd992658cc180f34cf327ab2c7701395a9d82a0ed9c4bb4e8253e3"></a>
<a id="a45ccc721bb7cd992658cc180f34cf327a7901089e4ae68dd2b40a6bacadf77c5e"></a>
<a id="a45ccc721bb7cd992658cc180f34cf327a0445fd580e2f953978c59756b6d3f663"></a>
<a id="a45ccc721bb7cd992658cc180f34cf327a38744227c79336f2db9e6fd14d8c805c"></a>
<a id="a45ccc721bb7cd992658cc180f34cf327aedc593bcb0a7a3b45421236ac949016a"></a>
<a id="a45ccc721bb7cd992658cc180f34cf327a3cd1f282d8c5eeb69d5dc396a638f51a"></a>
<a id="a45ccc721bb7cd992658cc180f34cf327a8c184ff1753827aaf1977acce3610459"></a>

---

[上一章](P020_zephyr__drivers__audio__cs35l5x.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P022_zephyr__drivers__dma__dma_xilinx_adma.h_文件参考.md)
