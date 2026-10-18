---
id: learning.zephyr-docs.api-file-reference.page-52
title: zephyr__drivers__dma__dma_intel_lpss.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dma__intel__lpss_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第52章\_zephyr\_\_drivers\_\_dma\_\_dma\_intel\_lpss.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dma__intel__lpss_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 52.1\_宏定义（Macros）

<a id="r_a30a9efb6d3b728e258083d8c9abb617f"></a>

```c
#define DMA_INTEL_LPSS_OFFSET 0x800
```

相关声明：[DMA_INTEL_LPSS_OFFSET](#a30a9efb6d3b728e258083d8c9abb617f)。

<a id="r_abc9f1a6bfba312cf78ab7800d3b8c589"></a>

```c
#define DMA_INTEL_LPSS_REMAP_LOW 0x240
```

相关声明：[DMA_INTEL_LPSS_REMAP_LOW](#abc9f1a6bfba312cf78ab7800d3b8c589)。

<a id="r_a2fa4dfb43c0fc5223d0e17932d6c97ee"></a>

```c
#define DMA_INTEL_LPSS_REMAP_HI 0x244
```

相关声明：[DMA_INTEL_LPSS_REMAP_HI](#a2fa4dfb43c0fc5223d0e17932d6c97ee)。

<a id="r_a1dd74ce0e651a2fad8abf337ac0bf1aa"></a>

```c
#define DMA_INTEL_LPSS_TX_CHAN 0
```

相关声明：[DMA_INTEL_LPSS_TX_CHAN](#a1dd74ce0e651a2fad8abf337ac0bf1aa)。

<a id="r_a3797b7de5ebf86a3c722e7667239cb3f"></a>

```c
#define DMA_INTEL_LPSS_RX_CHAN 1
```

相关声明：[DMA_INTEL_LPSS_RX_CHAN](#a3797b7de5ebf86a3c722e7667239cb3f)。

<a id="r_a93cbdc5d852735e260d4b767cc591977"></a>

```c
#define DMA_INTEL_LPSS_ADDR_RIGHT_SHIFT 32
```

相关声明：[DMA_INTEL_LPSS_ADDR_RIGHT_SHIFT](#a93cbdc5d852735e260d4b767cc591977)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 52.2\_函数（Functions）

<a id="r_a769db0413f8ca5fe4c03d1701581edfa"></a>

```c
void dma_intel_lpss_isr (const struct device *dev)
```

相关声明：[dma_intel_lpss_isr](#a769db0413f8ca5fe4c03d1701581edfa)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_a4a5438ab5a164e80c0564fc73e8b9764"></a>

```c
int dma_intel_lpss_setup (const struct device *dev)
```

相关声明：[dma_intel_lpss_setup](#a4a5438ab5a164e80c0564fc73e8b9764)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_aaf5eefbe0476083a87e5c2724a99a73d"></a>

```c
void dma_intel_lpss_set_base (const struct device *dev, uintptr_t base)
```

相关声明：[dma_intel_lpss_set_base](#aaf5eefbe0476083a87e5c2724a99a73d)、[device](../device_reference/P002_设备对象结构.md)、[uintptr_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

## 52.3\_详细说明（Detailed Documentation）

<a id="a93cbdc5d852735e260d4b767cc591977"></a>

### `DMA_INTEL_LPSS_ADDR_RIGHT_SHIFT`

```c
#define DMA_INTEL_LPSS_ADDR_RIGHT_SHIFT 32
```

<a id="a30a9efb6d3b728e258083d8c9abb617f"></a>

### `DMA_INTEL_LPSS_OFFSET`

```c
#define DMA_INTEL_LPSS_OFFSET 0x800
```

<a id="a2fa4dfb43c0fc5223d0e17932d6c97ee"></a>

### `DMA_INTEL_LPSS_REMAP_HI`

```c
#define DMA_INTEL_LPSS_REMAP_HI 0x244
```

<a id="abc9f1a6bfba312cf78ab7800d3b8c589"></a>

### `DMA_INTEL_LPSS_REMAP_LOW`

```c
#define DMA_INTEL_LPSS_REMAP_LOW 0x240
```

<a id="a3797b7de5ebf86a3c722e7667239cb3f"></a>

### `DMA_INTEL_LPSS_RX_CHAN`

```c
#define DMA_INTEL_LPSS_RX_CHAN 1
```

<a id="a1dd74ce0e651a2fad8abf337ac0bf1aa"></a>

### `DMA_INTEL_LPSS_TX_CHAN`

```c
#define DMA_INTEL_LPSS_TX_CHAN 0
```

<a id="a769db0413f8ca5fe4c03d1701581edfa"></a>

### `dma_intel_lpss_isr()`

```c
void dma_intel_lpss_isr ( const struct device * dev)
```

<a id="aaf5eefbe0476083a87e5c2724a99a73d"></a>

### `dma_intel_lpss_set_base()`

```c
void dma_intel_lpss_set_base ( const struct device * dev, uintptr_t base )
```

<a id="a4a5438ab5a164e80c0564fc73e8b9764"></a>

### `dma_intel_lpss_setup()`

```c
int dma_intel_lpss_setup ( const struct device * dev)
```


## 52.4\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P139_dma_intel_lpss.h_源码浏览.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uintptr_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P051_zephyr__drivers__dma__dma_gd32.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P053_zephyr__drivers__dma__dma_mcux_lpc.h_文件参考.md)
