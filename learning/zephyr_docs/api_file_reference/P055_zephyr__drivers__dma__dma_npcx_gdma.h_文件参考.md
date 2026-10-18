---
id: learning.zephyr-docs.api-file-reference.page-55
title: zephyr__drivers__dma__dma_npcx_gdma.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dma__npcx__gdma_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第55章\_zephyr\_\_drivers\_\_dma\_\_dma\_npcx\_gdma.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dma__npcx__gdma_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 55.1\_宏定义（Macros）

<a id="r_aab6807cbd48e8c266b594cb018024232"></a>

```c
#define NPCX_DMA_ADDR_16B_ALIGN 16U
```

相关声明：[NPCX_DMA_ADDR_16B_ALIGN](#aab6807cbd48e8c266b594cb018024232)。

<a id="r_a0a0ab91aea05636b96de9c7ed0e96c74"></a>

```c
#define DMA_NPCX_CONFIG_DIR FIELD(6, 2)
```

相关声明：[DMA_NPCX_CONFIG_DIR](#a0a0ab91aea05636b96de9c7ed0e96c74)。

<a id="r_a3d726dc5c3f286ec4182120754eb4961"></a>

```c
#define DMA_NPCX_CONFIG_TWS FIELD(8, 2)
```

相关声明：[DMA_NPCX_CONFIG_TWS](#a3d726dc5c3f286ec4182120754eb4961)。

<a id="r_a0ab16e2c2455e3dbcd37a21d49e1e9b3"></a>

```c
#define DMA_NPCX_CONFIG_BME 10
```

相关声明：[DMA_NPCX_CONFIG_BME](#a0ab16e2c2455e3dbcd37a21d49e1e9b3)。

<a id="r_a4b8903b8075e8dee1f38b4f277c6acc9"></a>

```c
#define DMA_NPCX_CONFIG_DADIR FIELD(11, 1)
```

相关声明：[DMA_NPCX_CONFIG_DADIR](#a4b8903b8075e8dee1f38b4f277c6acc9)。

<a id="r_afe7b73c405f52c577de35a5fa9203e5e"></a>

```c
#define DMA_NPCX_CONFIG_SADIR FIELD(12, 1)
```

相关声明：[DMA_NPCX_CONFIG_SADIR](#afe7b73c405f52c577de35a5fa9203e5e)。

<a id="r_ad12f9fba70d93bd97fe2d9b9fe224121"></a>

```c
#define DMA_NPCX_CONFIG_DAFIX 13
```

相关声明：[DMA_NPCX_CONFIG_DAFIX](#ad12f9fba70d93bd97fe2d9b9fe224121)。

<a id="r_acea39139e5a456ac48f7ab96a81db277"></a>

```c
#define DMA_NPCX_CONFIG_SAFIX 14
```

相关声明：[DMA_NPCX_CONFIG_SAFIX](#acea39139e5a456ac48f7ab96a81db277)。

<a id="r_a711f65bac0207306f4c8b6bda79d8ff7"></a>

```c
#define NPCX_GDMA_CHANNEL_CONFIG(inst, name)
```

相关声明：[NPCX_GDMA_CHANNEL_CONFIG](#a711f65bac0207306f4c8b6bda79d8ff7)。

<a id="r_a107a3514df0b0fadda6a6a4d7bd00f4f"></a>

```c
#define NPCX_GDMA_CONFIG_DIRECTION(config)
```

相关声明：[NPCX_GDMA_CONFIG_DIRECTION](#a107a3514df0b0fadda6a6a4d7bd00f4f)。

<a id="r_ab4e3929d4979540250cca87896a63bca"></a>

```c
#define NPCX_GDMA_CONFIG_BURST_LENGTH(config)
```

相关声明：[NPCX_GDMA_CONFIG_BURST_LENGTH](#ab4e3929d4979540250cca87896a63bca)。

<a id="r_a53522d55fa9bbdee9aff6942e8810fbb"></a>

```c
#define NPCX_GDMA_CONFIG_DSTADDR_ADJ(config)
```

相关声明：[NPCX_GDMA_CONFIG_DSTADDR_ADJ](#a53522d55fa9bbdee9aff6942e8810fbb)。

<a id="r_a5e6bd95ca738aab2f23084fef9a6cb1e"></a>

```c
#define NPCX_GDMA_CONFIG_SRCADDR_ADJ(config)
```

相关声明：[NPCX_GDMA_CONFIG_SRCADDR_ADJ](#a5e6bd95ca738aab2f23084fef9a6cb1e)。

## 55.2\_详细说明（Detailed Documentation）

<a id="a0ab16e2c2455e3dbcd37a21d49e1e9b3"></a>

### `DMA_NPCX_CONFIG_BME`

```c
#define DMA_NPCX_CONFIG_BME 10
```

<a id="a4b8903b8075e8dee1f38b4f277c6acc9"></a>

### `DMA_NPCX_CONFIG_DADIR`

```c
#define DMA_NPCX_CONFIG_DADIR FIELD(11, 1)
```

<a id="ad12f9fba70d93bd97fe2d9b9fe224121"></a>

### `DMA_NPCX_CONFIG_DAFIX`

```c
#define DMA_NPCX_CONFIG_DAFIX 13
```

<a id="a0a0ab91aea05636b96de9c7ed0e96c74"></a>

### `DMA_NPCX_CONFIG_DIR`

```c
#define DMA_NPCX_CONFIG_DIR FIELD(6, 2)
```

<a id="afe7b73c405f52c577de35a5fa9203e5e"></a>

### `DMA_NPCX_CONFIG_SADIR`

```c
#define DMA_NPCX_CONFIG_SADIR FIELD(12, 1)
```

<a id="acea39139e5a456ac48f7ab96a81db277"></a>

### `DMA_NPCX_CONFIG_SAFIX`

```c
#define DMA_NPCX_CONFIG_SAFIX 14
```

<a id="a3d726dc5c3f286ec4182120754eb4961"></a>

### `DMA_NPCX_CONFIG_TWS`

```c
#define DMA_NPCX_CONFIG_TWS FIELD(8, 2)
```

<a id="aab6807cbd48e8c266b594cb018024232"></a>

### `NPCX_DMA_ADDR_16B_ALIGN`

```c
#define NPCX_DMA_ADDR_16B_ALIGN 16U
```

<a id="a711f65bac0207306f4c8b6bda79d8ff7"></a>

### `NPCX_GDMA_CHANNEL_CONFIG`

```c
#define NPCX_GDMA_CHANNEL_CONFIG ( inst, name )
```

展开值（Value）：

```c
DT_INST_DMAS_CELL_BY_NAME(inst, name, config)
```

<a id="ab4e3929d4979540250cca87896a63bca"></a>

### `NPCX_GDMA_CONFIG_BURST_LENGTH`

```c
#define NPCX_GDMA_CONFIG_BURST_LENGTH ( config)
```

展开值（Value）：

```c
((1 << GET_FIELD(config, DMA_NPCX_CONFIG_TWS))                                             \
 << (IS_BIT_SET(config, DMA_NPCX_CONFIG_BME) ? 0x2 : 0x0))
```

<a id="a107a3514df0b0fadda6a6a4d7bd00f4f"></a>

### `NPCX_GDMA_CONFIG_DIRECTION`

```c
#define NPCX_GDMA_CONFIG_DIRECTION ( config)
```

展开值（Value）：

```c
GET_FIELD(config, DMA_NPCX_CONFIG_DIR)
```

<a id="a53522d55fa9bbdee9aff6942e8810fbb"></a>

### `NPCX_GDMA_CONFIG_DSTADDR_ADJ`

```c
#define NPCX_GDMA_CONFIG_DSTADDR_ADJ ( config)
```

展开值（Value）：

```c
(IS_BIT_SET(config, DMA_NPCX_CONFIG_DAFIX)) ? DMA_ADDR_ADJ_NO_CHANGE                       \
                                            : GET_FIELD(config, DMA_NPCX_CONFIG_DADIR)
```

<a id="a5e6bd95ca738aab2f23084fef9a6cb1e"></a>

### `NPCX_GDMA_CONFIG_SRCADDR_ADJ`

```c
#define NPCX_GDMA_CONFIG_SRCADDR_ADJ ( config)
```

展开值（Value）：

```c
(IS_BIT_SET(config, DMA_NPCX_CONFIG_SAFIX)) ? DMA_ADDR_ADJ_NO_CHANGE                       \
                                            : GET_FIELD(config, DMA_NPCX_CONFIG_SADIR)
```


## 55.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_configuration_reference/P018_dma_npcx_gdma.h_源码浏览.md)
- [DT_INST_DMAS_CELL_BY_NAME](../dma_reference/P008_DMA设备树宏.md#ga2cc0124a66cf3b9f1c4c506b7f978d30)
- [IS_BIT_SET](../util_reference/P001_通用工具公共接口.md#ga93abc3834bcb58b15c819e68d694ed20)
- [DMA_ADDR_ADJ_NO_CHANGE](../dma_reference/P001_DMA公共接口.md#ggafe0877ef4bd7790a4bcd46052088231cafeb870c1a6f9db8238a97f3ac9c6da4f)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__devicetree-dmas_html_ga2cc0124a66cf3b9f1c4c506b7f978d30"></a>
<a id="adma__npcx__gdma_8h_html_a0ab16e2c2455e3dbcd37a21d49e1e9b3"></a>
<a id="adma__npcx__gdma_8h_html_a3d726dc5c3f286ec4182120754eb4961"></a>
<a id="agroup__sys-util_html_ga93abc3834bcb58b15c819e68d694ed20"></a>
<a id="adma__npcx__gdma_8h_html_a0a0ab91aea05636b96de9c7ed0e96c74"></a>
<a id="adma__npcx__gdma_8h_html_a4b8903b8075e8dee1f38b4f277c6acc9"></a>
<a id="adma__npcx__gdma_8h_html_ad12f9fba70d93bd97fe2d9b9fe224121"></a>
<a id="agroup__dma__interface_html_ggafe0877ef4bd7790a4bcd46052088231cafeb870c1a6f9db8238a97f3ac9c6da4f"></a>
<a id="adma__npcx__gdma_8h_html_acea39139e5a456ac48f7ab96a81db277"></a>
<a id="adma__npcx__gdma_8h_html_afe7b73c405f52c577de35a5fa9203e5e"></a>

---

[上一章](P054_zephyr__drivers__dma__dma_mcux_pxp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P056_zephyr__drivers__dma__dma_stm32.h_文件参考.md)
