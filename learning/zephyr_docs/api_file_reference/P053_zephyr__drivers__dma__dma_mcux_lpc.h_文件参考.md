---
id: learning.zephyr-docs.api-file-reference.page-53
title: zephyr__drivers__dma__dma_mcux_lpc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dma__mcux__lpc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第53章\_zephyr\_\_drivers\_\_dma\_\_dma\_mcux\_lpc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dma__mcux__lpc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 53.1\_宏定义（Macros）

<a id="r_a4d1f2a9bd076336bce0fd5e535cfc580"></a>

```c
#define LPC_DMA_PERIPH_REQ_EN BIT(0)
```

相关声明：[LPC_DMA_PERIPH_REQ_EN](#a4d1f2a9bd076336bce0fd5e535cfc580)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a738b7a640e92bd64a95172b236f10544"></a>

```c
#define LPC_DMA_HWTRIG_EN BIT(1)
```

相关声明：[LPC_DMA_HWTRIG_EN](#a738b7a640e92bd64a95172b236f10544)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a6c9492c7479a678b11a54e28f7bc3df8"></a>

```c
#define LPC_DMA_TRIGPOL_HIGH_RISING BIT(2)
```

相关声明：[LPC_DMA_TRIGPOL_HIGH_RISING](#a6c9492c7479a678b11a54e28f7bc3df8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a0f5ed8f5fbe87d13e4f21e0a3018ab64"></a>

```c
#define LPC_DMA_TRIGTYPE_LEVEL BIT(3)
```

相关声明：[LPC_DMA_TRIGTYPE_LEVEL](#a0f5ed8f5fbe87d13e4f21e0a3018ab64)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a4d9e1928d741d1950384f7ab83600ee2"></a>

```c
#define LPC_DMA_TRIGBURST BIT(4)
```

相关声明：[LPC_DMA_TRIGBURST](#a4d9e1928d741d1950384f7ab83600ee2)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_acfa31048d38fa62b9cb3681886472609"></a>

```c
#define LPC_DMA_BURSTPOWER(pwr)
```

相关声明：[LPC_DMA_BURSTPOWER](#acfa31048d38fa62b9cb3681886472609)。

<a id="r_a0e9624882342df7556aa29a8f7ee74f3"></a>

```c
#define LPC_DMA_GET_BURSTPOWER(slot)
```

相关声明：[LPC_DMA_GET_BURSTPOWER](#a0e9624882342df7556aa29a8f7ee74f3)。

<a id="r_a8ce25c65bd1dcf87b1b688e271872b3c"></a>

```c
#define LPC_DMA_SPI_MCUX_FLEXCOMM_TX (DMA_CHANNEL_DIRECTION_PRIV_START)
```

相关声明：[LPC_DMA_SPI_MCUX_FLEXCOMM_TX](#a8ce25c65bd1dcf87b1b688e271872b3c)、[DMA_CHANNEL_DIRECTION_PRIV_START](../dma_reference/P001_DMA公共接口.md#ggae442d8ba73be7e53b68165647b0ea402a273f9cdcc2af613375cb3e235bfda037)。

## 53.2\_详细说明（Detailed Documentation）

<a id="acfa31048d38fa62b9cb3681886472609"></a>

### `LPC_DMA_BURSTPOWER`

```c
#define LPC_DMA_BURSTPOWER ( pwr)
```

展开值（Value）：

```c
(((pwr) & 0x7) << 5)
```

<a id="a0e9624882342df7556aa29a8f7ee74f3"></a>

### `LPC_DMA_GET_BURSTPOWER`

```c
#define LPC_DMA_GET_BURSTPOWER ( slot)
```

展开值（Value）：

```c
(((slot) & 0xE0) >> 5)
```

<a id="a738b7a640e92bd64a95172b236f10544"></a>

### `LPC_DMA_HWTRIG_EN`

```c
#define LPC_DMA_HWTRIG_EN BIT(1)
```

<a id="a4d1f2a9bd076336bce0fd5e535cfc580"></a>

### `LPC_DMA_PERIPH_REQ_EN`

```c
#define LPC_DMA_PERIPH_REQ_EN BIT(0)
```

<a id="a8ce25c65bd1dcf87b1b688e271872b3c"></a>

### `LPC_DMA_SPI_MCUX_FLEXCOMM_TX`

```c
#define LPC_DMA_SPI_MCUX_FLEXCOMM_TX (DMA_CHANNEL_DIRECTION_PRIV_START)
```

<a id="a4d9e1928d741d1950384f7ab83600ee2"></a>

### `LPC_DMA_TRIGBURST`

```c
#define LPC_DMA_TRIGBURST BIT(4)
```

<a id="a6c9492c7479a678b11a54e28f7bc3df8"></a>

### `LPC_DMA_TRIGPOL_HIGH_RISING`

```c
#define LPC_DMA_TRIGPOL_HIGH_RISING BIT(2)
```

<a id="a0f5ed8f5fbe87d13e4f21e0a3018ab64"></a>

### `LPC_DMA_TRIGTYPE_LEVEL`

```c
#define LPC_DMA_TRIGTYPE_LEVEL BIT(3)
```


## 53.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/dma__mcux__lpc_8h_source.html)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [DMA_CHANNEL_DIRECTION_PRIV_START](../dma_reference/P001_DMA公共接口.md#ggae442d8ba73be7e53b68165647b0ea402a273f9cdcc2af613375cb3e235bfda037)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P052_zephyr__drivers__dma__dma_intel_lpss.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P054_zephyr__drivers__dma__dma_mcux_pxp.h_文件参考.md)
