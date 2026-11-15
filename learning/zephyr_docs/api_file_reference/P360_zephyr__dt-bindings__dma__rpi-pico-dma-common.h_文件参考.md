---
id: learning.zephyr-docs.api-file-reference.page-360
title: zephyr__dt-bindings__dma__rpi-pico-dma-common.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rpi-pico-dma-common_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第360章\_zephyr\_\_dt-bindings\_\_dma\_\_rpi-pico-dma-common.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/rpi-pico-dma-common_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 360.1\_宏定义（Macros）

<a id="r_af17a4ab6d1b744cb7ba78185681f464b"></a>

```c
#define RPI_PICO_DMA_SLOT_TO_DREQ(s)
```

相关声明：[RPI_PICO_DMA_SLOT_TO_DREQ](#af17a4ab6d1b744cb7ba78185681f464b)。

<a id="r_a108c9650b4eb398c9994d7c1683beaa8"></a>

```c
#define RPI_PICO_DMA_DREQ_TO_SLOT RPI_PICO_DMA_SLOT_TO_DREQ
```

相关声明：[RPI_PICO_DMA_DREQ_TO_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)、[RPI_PICO_DMA_SLOT_TO_DREQ](#af17a4ab6d1b744cb7ba78185681f464b)。

<a id="r_ab4efb501d7d6acf7c4e320a992a736c9"></a>

```c
#define RPI_PICO_DMA_SLOT_PIO0_TX0 RPI_PICO_DMA_DREQ_TO_SLOT(0x00)
```

相关声明：[RPI_PICO_DMA_SLOT_PIO0_TX0](#ab4efb501d7d6acf7c4e320a992a736c9)、[RPI_PICO_DMA_DREQ_TO_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_ac83bcbc6b3716d947051d785f60447c1"></a>

```c
#define RPI_PICO_DMA_SLOT_PIO0_TX1 RPI_PICO_DMA_DREQ_TO_SLOT(0x01)
```

相关声明：[RPI_PICO_DMA_SLOT_PIO0_TX1](#ac83bcbc6b3716d947051d785f60447c1)、[RPI_PICO_DMA_DREQ_TO_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_ad2452d29f952c828fc38036d3fc8f7c7"></a>

```c
#define RPI_PICO_DMA_SLOT_PIO0_TX2 RPI_PICO_DMA_DREQ_TO_SLOT(0x02)
```

相关声明：[RPI_PICO_DMA_SLOT_PIO0_TX2](#ad2452d29f952c828fc38036d3fc8f7c7)、[RPI_PICO_DMA_DREQ_TO_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_a3be36155cb5c9faff83951e46e1ce6eb"></a>

```c
#define RPI_PICO_DMA_SLOT_PIO0_TX3 RPI_PICO_DMA_DREQ_TO_SLOT(0x03)
```

相关声明：[RPI_PICO_DMA_SLOT_PIO0_TX3](#a3be36155cb5c9faff83951e46e1ce6eb)、[RPI_PICO_DMA_DREQ_TO_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_a4931c164398407d3365d600d17110f95"></a>

```c
#define RPI_PICO_DMA_SLOT_PIO0_RX0 RPI_PICO_DMA_DREQ_TO_SLOT(0x04)
```

相关声明：[RPI_PICO_DMA_SLOT_PIO0_RX0](#a4931c164398407d3365d600d17110f95)、[RPI_PICO_DMA_DREQ_TO_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_a84583ff2852ec17e709f44cfe85a21d1"></a>

```c
#define RPI_PICO_DMA_SLOT_PIO0_RX1 RPI_PICO_DMA_DREQ_TO_SLOT(0x05)
```

相关声明：[RPI_PICO_DMA_SLOT_PIO0_RX1](#a84583ff2852ec17e709f44cfe85a21d1)、[RPI_PICO_DMA_DREQ_TO_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_a7a30cab865790b3ff4c873cec1ae39a4"></a>

```c
#define RPI_PICO_DMA_SLOT_PIO0_RX2 RPI_PICO_DMA_DREQ_TO_SLOT(0x06)
```

相关声明：[RPI_PICO_DMA_SLOT_PIO0_RX2](#a7a30cab865790b3ff4c873cec1ae39a4)、[RPI_PICO_DMA_DREQ_TO_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_a131cdd1941010a43bebcda6fffd98016"></a>

```c
#define RPI_PICO_DMA_SLOT_PIO0_RX3 RPI_PICO_DMA_DREQ_TO_SLOT(0x07)
```

相关声明：[RPI_PICO_DMA_SLOT_PIO0_RX3](#a131cdd1941010a43bebcda6fffd98016)、[RPI_PICO_DMA_DREQ_TO_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_a17f1642461493cde7e832a1ab78d9f69"></a>

```c
#define RPI_PICO_DMA_SLOT_PIO1_TX0 RPI_PICO_DMA_DREQ_TO_SLOT(0x08)
```

相关声明：[RPI_PICO_DMA_SLOT_PIO1_TX0](#a17f1642461493cde7e832a1ab78d9f69)、[RPI_PICO_DMA_DREQ_TO_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_a7a19561e334931146de9a56ce3214680"></a>

```c
#define RPI_PICO_DMA_SLOT_PIO1_TX1 RPI_PICO_DMA_DREQ_TO_SLOT(0x09)
```

相关声明：[RPI_PICO_DMA_SLOT_PIO1_TX1](#a7a19561e334931146de9a56ce3214680)、[RPI_PICO_DMA_DREQ_TO_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_ae6f04b3ecc7adfa5bb4e070f6cc29780"></a>

```c
#define RPI_PICO_DMA_SLOT_PIO1_TX2 RPI_PICO_DMA_DREQ_TO_SLOT(0x0A)
```

相关声明：[RPI_PICO_DMA_SLOT_PIO1_TX2](#ae6f04b3ecc7adfa5bb4e070f6cc29780)、[RPI_PICO_DMA_DREQ_TO_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_ab39ac333962fe0debca583061ba1b6cb"></a>

```c
#define RPI_PICO_DMA_SLOT_PIO1_TX3 RPI_PICO_DMA_DREQ_TO_SLOT(0x0B)
```

相关声明：[RPI_PICO_DMA_SLOT_PIO1_TX3](#ab39ac333962fe0debca583061ba1b6cb)、[RPI_PICO_DMA_DREQ_TO_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_a7eaaa6b0e6f80021364a66fd75450c0d"></a>

```c
#define RPI_PICO_DMA_SLOT_PIO1_RX0 RPI_PICO_DMA_DREQ_TO_SLOT(0x0C)
```

相关声明：[RPI_PICO_DMA_SLOT_PIO1_RX0](#a7eaaa6b0e6f80021364a66fd75450c0d)、[RPI_PICO_DMA_DREQ_TO_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_a9963f9b698a5ffde3e3bcf9b4b43ed22"></a>

```c
#define RPI_PICO_DMA_SLOT_PIO1_RX1 RPI_PICO_DMA_DREQ_TO_SLOT(0x0D)
```

相关声明：[RPI_PICO_DMA_SLOT_PIO1_RX1](#a9963f9b698a5ffde3e3bcf9b4b43ed22)、[RPI_PICO_DMA_DREQ_TO_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_ad1a63c332b00cf4442907a3a11d155d1"></a>

```c
#define RPI_PICO_DMA_SLOT_PIO1_RX2 RPI_PICO_DMA_DREQ_TO_SLOT(0x0E)
```

相关声明：[RPI_PICO_DMA_SLOT_PIO1_RX2](#ad1a63c332b00cf4442907a3a11d155d1)、[RPI_PICO_DMA_DREQ_TO_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_a07eab28aade43838cf5580e0c0ea3bde"></a>

```c
#define RPI_PICO_DMA_SLOT_PIO1_RX3 RPI_PICO_DMA_DREQ_TO_SLOT(0x0F)
```

相关声明：[RPI_PICO_DMA_SLOT_PIO1_RX3](#a07eab28aade43838cf5580e0c0ea3bde)、[RPI_PICO_DMA_DREQ_TO_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_aac94fe3f6411cd4bad422974be560d92"></a>

```c
#define RPI_PICO_DMA_SLOT_DMA_TIMER0 RPI_PICO_DMA_DREQ_TO_SLOT(0x3B)
```

相关声明：[RPI_PICO_DMA_SLOT_DMA_TIMER0](#aac94fe3f6411cd4bad422974be560d92)、[RPI_PICO_DMA_DREQ_TO_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_a864c5126bab363926d43b8d2a951a935"></a>

```c
#define RPI_PICO_DMA_SLOT_DMA_TIMER1 RPI_PICO_DMA_DREQ_TO_SLOT(0x3C)
```

相关声明：[RPI_PICO_DMA_SLOT_DMA_TIMER1](#a864c5126bab363926d43b8d2a951a935)、[RPI_PICO_DMA_DREQ_TO_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_a0b8c6347ccfe168d06851fdac5bfe470"></a>

```c
#define RPI_PICO_DMA_SLOT_DMA_TIMER2 RPI_PICO_DMA_DREQ_TO_SLOT(0x3D)
```

相关声明：[RPI_PICO_DMA_SLOT_DMA_TIMER2](#a0b8c6347ccfe168d06851fdac5bfe470)、[RPI_PICO_DMA_DREQ_TO_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_aa4cf3c65b88cf11aaadd685363695262"></a>

```c
#define RPI_PICO_DMA_SLOT_DMA_TIMER3 RPI_PICO_DMA_DREQ_TO_SLOT(0x3E)
```

相关声明：[RPI_PICO_DMA_SLOT_DMA_TIMER3](#aa4cf3c65b88cf11aaadd685363695262)、[RPI_PICO_DMA_DREQ_TO_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_a6571b7502d26dcb0011fa9c38f64f793"></a>

```c
#define RPI_PICO_DMA_SLOT_FORCE RPI_PICO_DMA_DREQ_TO_SLOT(0x3F)
```

相关声明：[RPI_PICO_DMA_SLOT_FORCE](#a6571b7502d26dcb0011fa9c38f64f793)、[RPI_PICO_DMA_DREQ_TO_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)。

## 360.2\_详细说明（Detailed Documentation）

<a id="a108c9650b4eb398c9994d7c1683beaa8"></a>

### `RPI_PICO_DMA_DREQ_TO_SLOT`

```c
#define RPI_PICO_DMA_DREQ_TO_SLOT RPI_PICO_DMA_SLOT_TO_DREQ
```

<a id="aac94fe3f6411cd4bad422974be560d92"></a>

### `RPI_PICO_DMA_SLOT_DMA_TIMER0`

```c
#define RPI_PICO_DMA_SLOT_DMA_TIMER0 RPI_PICO_DMA_DREQ_TO_SLOT(0x3B)
```

<a id="a864c5126bab363926d43b8d2a951a935"></a>

### `RPI_PICO_DMA_SLOT_DMA_TIMER1`

```c
#define RPI_PICO_DMA_SLOT_DMA_TIMER1 RPI_PICO_DMA_DREQ_TO_SLOT(0x3C)
```

<a id="a0b8c6347ccfe168d06851fdac5bfe470"></a>

### `RPI_PICO_DMA_SLOT_DMA_TIMER2`

```c
#define RPI_PICO_DMA_SLOT_DMA_TIMER2 RPI_PICO_DMA_DREQ_TO_SLOT(0x3D)
```

<a id="aa4cf3c65b88cf11aaadd685363695262"></a>

### `RPI_PICO_DMA_SLOT_DMA_TIMER3`

```c
#define RPI_PICO_DMA_SLOT_DMA_TIMER3 RPI_PICO_DMA_DREQ_TO_SLOT(0x3E)
```

<a id="a6571b7502d26dcb0011fa9c38f64f793"></a>

### `RPI_PICO_DMA_SLOT_FORCE`

```c
#define RPI_PICO_DMA_SLOT_FORCE RPI_PICO_DMA_DREQ_TO_SLOT(0x3F)
```

<a id="a4931c164398407d3365d600d17110f95"></a>

### `RPI_PICO_DMA_SLOT_PIO0_RX0`

```c
#define RPI_PICO_DMA_SLOT_PIO0_RX0 RPI_PICO_DMA_DREQ_TO_SLOT(0x04)
```

<a id="a84583ff2852ec17e709f44cfe85a21d1"></a>

### `RPI_PICO_DMA_SLOT_PIO0_RX1`

```c
#define RPI_PICO_DMA_SLOT_PIO0_RX1 RPI_PICO_DMA_DREQ_TO_SLOT(0x05)
```

<a id="a7a30cab865790b3ff4c873cec1ae39a4"></a>

### `RPI_PICO_DMA_SLOT_PIO0_RX2`

```c
#define RPI_PICO_DMA_SLOT_PIO0_RX2 RPI_PICO_DMA_DREQ_TO_SLOT(0x06)
```

<a id="a131cdd1941010a43bebcda6fffd98016"></a>

### `RPI_PICO_DMA_SLOT_PIO0_RX3`

```c
#define RPI_PICO_DMA_SLOT_PIO0_RX3 RPI_PICO_DMA_DREQ_TO_SLOT(0x07)
```

<a id="ab4efb501d7d6acf7c4e320a992a736c9"></a>

### `RPI_PICO_DMA_SLOT_PIO0_TX0`

```c
#define RPI_PICO_DMA_SLOT_PIO0_TX0 RPI_PICO_DMA_DREQ_TO_SLOT(0x00)
```

<a id="ac83bcbc6b3716d947051d785f60447c1"></a>

### `RPI_PICO_DMA_SLOT_PIO0_TX1`

```c
#define RPI_PICO_DMA_SLOT_PIO0_TX1 RPI_PICO_DMA_DREQ_TO_SLOT(0x01)
```

<a id="ad2452d29f952c828fc38036d3fc8f7c7"></a>

### `RPI_PICO_DMA_SLOT_PIO0_TX2`

```c
#define RPI_PICO_DMA_SLOT_PIO0_TX2 RPI_PICO_DMA_DREQ_TO_SLOT(0x02)
```

<a id="a3be36155cb5c9faff83951e46e1ce6eb"></a>

### `RPI_PICO_DMA_SLOT_PIO0_TX3`

```c
#define RPI_PICO_DMA_SLOT_PIO0_TX3 RPI_PICO_DMA_DREQ_TO_SLOT(0x03)
```

<a id="a7eaaa6b0e6f80021364a66fd75450c0d"></a>

### `RPI_PICO_DMA_SLOT_PIO1_RX0`

```c
#define RPI_PICO_DMA_SLOT_PIO1_RX0 RPI_PICO_DMA_DREQ_TO_SLOT(0x0C)
```

<a id="a9963f9b698a5ffde3e3bcf9b4b43ed22"></a>

### `RPI_PICO_DMA_SLOT_PIO1_RX1`

```c
#define RPI_PICO_DMA_SLOT_PIO1_RX1 RPI_PICO_DMA_DREQ_TO_SLOT(0x0D)
```

<a id="ad1a63c332b00cf4442907a3a11d155d1"></a>

### `RPI_PICO_DMA_SLOT_PIO1_RX2`

```c
#define RPI_PICO_DMA_SLOT_PIO1_RX2 RPI_PICO_DMA_DREQ_TO_SLOT(0x0E)
```

<a id="a07eab28aade43838cf5580e0c0ea3bde"></a>

### `RPI_PICO_DMA_SLOT_PIO1_RX3`

```c
#define RPI_PICO_DMA_SLOT_PIO1_RX3 RPI_PICO_DMA_DREQ_TO_SLOT(0x0F)
```

<a id="a17f1642461493cde7e832a1ab78d9f69"></a>

### `RPI_PICO_DMA_SLOT_PIO1_TX0`

```c
#define RPI_PICO_DMA_SLOT_PIO1_TX0 RPI_PICO_DMA_DREQ_TO_SLOT(0x08)
```

<a id="a7a19561e334931146de9a56ce3214680"></a>

### `RPI_PICO_DMA_SLOT_PIO1_TX1`

```c
#define RPI_PICO_DMA_SLOT_PIO1_TX1 RPI_PICO_DMA_DREQ_TO_SLOT(0x09)
```

<a id="ae6f04b3ecc7adfa5bb4e070f6cc29780"></a>

### `RPI_PICO_DMA_SLOT_PIO1_TX2`

```c
#define RPI_PICO_DMA_SLOT_PIO1_TX2 RPI_PICO_DMA_DREQ_TO_SLOT(0x0A)
```

<a id="ab39ac333962fe0debca583061ba1b6cb"></a>

### `RPI_PICO_DMA_SLOT_PIO1_TX3`

```c
#define RPI_PICO_DMA_SLOT_PIO1_TX3 RPI_PICO_DMA_DREQ_TO_SLOT(0x0B)
```

<a id="af17a4ab6d1b744cb7ba78185681f464b"></a>

### `RPI_PICO_DMA_SLOT_TO_DREQ`

```c
#define RPI_PICO_DMA_SLOT_TO_DREQ ( s)
```

展开值（Value）：

```c
(~(s)&0x3F)
```


## 360.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_supplement_reference/P166_rpi-pico-dma-common.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P359_zephyr__dt-bindings__reset__rp2350_reset.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P361_zephyr__dt-bindings__dma__rpi-pico-dma-rp2040.h_文件参考.md)
