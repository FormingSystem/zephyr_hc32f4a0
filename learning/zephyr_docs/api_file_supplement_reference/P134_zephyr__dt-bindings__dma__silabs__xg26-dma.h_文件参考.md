---
id: learning.zephyr-docs.api-file-supplement-reference.page-134
title: zephyr__dt-bindings__dma__silabs__xg26-dma.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/xg26-dma_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第134章\_zephyr\_\_dt-bindings\_\_dma\_\_silabs\_\_xg26-dma.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/xg26-dma_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/dt-bindings/dt-util.h>
#include "common-dma.h"
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 134.1\_宏定义（Macros）

<a id="r_a3b04d98c82d29396f8e688db8d5c5de9"></a>

```c
#define DMA_REQSEL_NONE (FIELD_PREP(DMA_SRC_MASK, 0) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_NONE](#a3b04d98c82d29396f8e688db8d5c5de9)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

Silabs 链接式 DMA 请求信号（LDMA Request Signal）的定义。

<a id="r_ac27c323faa6e0db8d8e6439fdd277181"></a>

```c
#define DMA_REQSEL_LDMAXBARPRSREQ0 (FIELD_PREP(DMA_SRC_MASK, 1) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_LDMAXBARPRSREQ0](#ac27c323faa6e0db8d8e6439fdd277181)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_ac20515cf65e2ca19ee0ad5f92403c6f1"></a>

```c
#define DMA_REQSEL_LDMAXBARPRSREQ1 (FIELD_PREP(DMA_SRC_MASK, 1) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_LDMAXBARPRSREQ1](#ac20515cf65e2ca19ee0ad5f92403c6f1)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a6fc80a2f87eb37f53c77fff13ba28c85"></a>

```c
#define DMA_REQSEL_TIMER0CC0 (FIELD_PREP(DMA_SRC_MASK, 2) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_TIMER0CC0](#a6fc80a2f87eb37f53c77fff13ba28c85)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a310cc4350ec3f721a3ce4055ad8a1110"></a>

```c
#define DMA_REQSEL_TIMER0CC1 (FIELD_PREP(DMA_SRC_MASK, 2) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_TIMER0CC1](#a310cc4350ec3f721a3ce4055ad8a1110)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a2d02b538557c468e47cad0aef76952ef"></a>

```c
#define DMA_REQSEL_TIMER0CC2 (FIELD_PREP(DMA_SRC_MASK, 2) | FIELD_PREP(DMA_SIG_MASK, 2))
```

相关声明：[DMA_REQSEL_TIMER0CC2](#a2d02b538557c468e47cad0aef76952ef)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a1862b04a508e5c89a565040f2b20ad0b"></a>

```c
#define DMA_REQSEL_TIMER0UFOF (FIELD_PREP(DMA_SRC_MASK, 2) | FIELD_PREP(DMA_SIG_MASK, 3))
```

相关声明：[DMA_REQSEL_TIMER0UFOF](#a1862b04a508e5c89a565040f2b20ad0b)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_ab6c754dbaa545bda3ebe376825958008"></a>

```c
#define DMA_REQSEL_TIMER1CC0 (FIELD_PREP(DMA_SRC_MASK, 3) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_TIMER1CC0](#ab6c754dbaa545bda3ebe376825958008)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a909e0705fd68b7e79f6d07e5c9e7d9e9"></a>

```c
#define DMA_REQSEL_TIMER1CC1 (FIELD_PREP(DMA_SRC_MASK, 3) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_TIMER1CC1](#a909e0705fd68b7e79f6d07e5c9e7d9e9)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a7299498af9580ac0236dfd776394e4f1"></a>

```c
#define DMA_REQSEL_TIMER1CC2 (FIELD_PREP(DMA_SRC_MASK, 3) | FIELD_PREP(DMA_SIG_MASK, 2))
```

相关声明：[DMA_REQSEL_TIMER1CC2](#a7299498af9580ac0236dfd776394e4f1)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a13f9bb1b7de6061b0eebca52e4349c71"></a>

```c
#define DMA_REQSEL_TIMER1UFOF (FIELD_PREP(DMA_SRC_MASK, 3) | FIELD_PREP(DMA_SIG_MASK, 3))
```

相关声明：[DMA_REQSEL_TIMER1UFOF](#a13f9bb1b7de6061b0eebca52e4349c71)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a4d8e451527281f0292c491fd1f40f709"></a>

```c
#define DMA_REQSEL_USART0RXDATAV (FIELD_PREP(DMA_SRC_MASK, 4) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_USART0RXDATAV](#a4d8e451527281f0292c491fd1f40f709)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a17598696e9a520ac6adea3920eff6900"></a>

```c
#define DMA_REQSEL_USART0RXDATAVRIGHT (FIELD_PREP(DMA_SRC_MASK, 4) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_USART0RXDATAVRIGHT](#a17598696e9a520ac6adea3920eff6900)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_ae691ddb9858cbd5205c2d62ea54a2797"></a>

```c
#define DMA_REQSEL_USART0TXBL (FIELD_PREP(DMA_SRC_MASK, 4) | FIELD_PREP(DMA_SIG_MASK, 2))
```

相关声明：[DMA_REQSEL_USART0TXBL](#ae691ddb9858cbd5205c2d62ea54a2797)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_adf8abf7448fea14cbc7dcd946a1dfd91"></a>

```c
#define DMA_REQSEL_USART0TXBLRIGHT (FIELD_PREP(DMA_SRC_MASK, 4) | FIELD_PREP(DMA_SIG_MASK, 3))
```

相关声明：[DMA_REQSEL_USART0TXBLRIGHT](#adf8abf7448fea14cbc7dcd946a1dfd91)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a180469c6cace2af0e91336b25d18ece1"></a>

```c
#define DMA_REQSEL_USART0TXEMPTY (FIELD_PREP(DMA_SRC_MASK, 4) | FIELD_PREP(DMA_SIG_MASK, 4))
```

相关声明：[DMA_REQSEL_USART0TXEMPTY](#a180469c6cace2af0e91336b25d18ece1)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a27f66bf3557d8f7f3b34251f03334926"></a>

```c
#define DMA_REQSEL_I2C0RXDATAV (FIELD_PREP(DMA_SRC_MASK, 5) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_I2C0RXDATAV](#a27f66bf3557d8f7f3b34251f03334926)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a724a2e12ee165d026039df6a016d043e"></a>

```c
#define DMA_REQSEL_I2C0TXBL (FIELD_PREP(DMA_SRC_MASK, 5) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_I2C0TXBL](#a724a2e12ee165d026039df6a016d043e)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a02e993bfd9d57d946257bc34d6538347"></a>

```c
#define DMA_REQSEL_I2C1RXDATAV (FIELD_PREP(DMA_SRC_MASK, 6) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_I2C1RXDATAV](#a02e993bfd9d57d946257bc34d6538347)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_af2f468e4d0dc9fce4cc54810e739f11d"></a>

```c
#define DMA_REQSEL_I2C1TXBL (FIELD_PREP(DMA_SRC_MASK, 6) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_I2C1TXBL](#af2f468e4d0dc9fce4cc54810e739f11d)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a8940bc48310aad0e3c9cab0e5eb95742"></a>

```c
#define DMA_REQSEL_IADC0IADC_SCAN (FIELD_PREP(DMA_SRC_MASK, 10) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_IADC0IADC_SCAN](#a8940bc48310aad0e3c9cab0e5eb95742)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_ae8a09e6ec4fd8da57e5b568380afee64"></a>

```c
#define DMA_REQSEL_IADC0IADC_SINGLE (FIELD_PREP(DMA_SRC_MASK, 10) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_IADC0IADC_SINGLE](#ae8a09e6ec4fd8da57e5b568380afee64)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a296a10558a0bb7c76d3fd9eab80fff91"></a>

```c
#define DMA_REQSEL_MSCWDATA (FIELD_PREP(DMA_SRC_MASK, 11) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_MSCWDATA](#a296a10558a0bb7c76d3fd9eab80fff91)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a8503415586264bbbc2c17560dfa36325"></a>

```c
#define DMA_REQSEL_TIMER2CC0 (FIELD_PREP(DMA_SRC_MASK, 12) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_TIMER2CC0](#a8503415586264bbbc2c17560dfa36325)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_aed70ea120b2a199163c46f028aec4538"></a>

```c
#define DMA_REQSEL_TIMER2CC1 (FIELD_PREP(DMA_SRC_MASK, 12) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_TIMER2CC1](#aed70ea120b2a199163c46f028aec4538)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_aff76df3b43b1ce7ff7cf36dad62914b5"></a>

```c
#define DMA_REQSEL_TIMER2CC2 (FIELD_PREP(DMA_SRC_MASK, 12) | FIELD_PREP(DMA_SIG_MASK, 2))
```

相关声明：[DMA_REQSEL_TIMER2CC2](#aff76df3b43b1ce7ff7cf36dad62914b5)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a359eec69c4e20a62fda0382318777ca2"></a>

```c
#define DMA_REQSEL_TIMER2UFOF (FIELD_PREP(DMA_SRC_MASK, 12) | FIELD_PREP(DMA_SIG_MASK, 3))
```

相关声明：[DMA_REQSEL_TIMER2UFOF](#a359eec69c4e20a62fda0382318777ca2)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_acd2b7ad92fa2c7fe11b0410760e431d0"></a>

```c
#define DMA_REQSEL_TIMER3CC0 (FIELD_PREP(DMA_SRC_MASK, 13) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_TIMER3CC0](#acd2b7ad92fa2c7fe11b0410760e431d0)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_ac875ac8e9ee74e79df2e9a7e7f7d47bc"></a>

```c
#define DMA_REQSEL_TIMER3CC1 (FIELD_PREP(DMA_SRC_MASK, 13) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_TIMER3CC1](#ac875ac8e9ee74e79df2e9a7e7f7d47bc)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a84068b2390c9db03e234e8ebf7dd844e"></a>

```c
#define DMA_REQSEL_TIMER3CC2 (FIELD_PREP(DMA_SRC_MASK, 13) | FIELD_PREP(DMA_SIG_MASK, 2))
```

相关声明：[DMA_REQSEL_TIMER3CC2](#a84068b2390c9db03e234e8ebf7dd844e)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a0b099b82ec5b12e2da5d9fcafeb6feb4"></a>

```c
#define DMA_REQSEL_TIMER3UFOF (FIELD_PREP(DMA_SRC_MASK, 13) | FIELD_PREP(DMA_SIG_MASK, 3))
```

相关声明：[DMA_REQSEL_TIMER3UFOF](#a0b099b82ec5b12e2da5d9fcafeb6feb4)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a91a9946b6909ffb54bd69df41c5d9907"></a>

```c
#define DMA_REQSEL_TIMER4CC0 (FIELD_PREP(DMA_SRC_MASK, 14) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_TIMER4CC0](#a91a9946b6909ffb54bd69df41c5d9907)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a3a12807722a1716c6bb6e58143441870"></a>

```c
#define DMA_REQSEL_TIMER4CC1 (FIELD_PREP(DMA_SRC_MASK, 14) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_TIMER4CC1](#a3a12807722a1716c6bb6e58143441870)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a3af0824dce9be11286d8521bb051554c"></a>

```c
#define DMA_REQSEL_TIMER4CC2 (FIELD_PREP(DMA_SRC_MASK, 14) | FIELD_PREP(DMA_SIG_MASK, 2))
```

相关声明：[DMA_REQSEL_TIMER4CC2](#a3af0824dce9be11286d8521bb051554c)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a48480c7b2b8319598e5d609acc6852cd"></a>

```c
#define DMA_REQSEL_TIMER4UFOF (FIELD_PREP(DMA_SRC_MASK, 14) | FIELD_PREP(DMA_SIG_MASK, 3))
```

相关声明：[DMA_REQSEL_TIMER4UFOF](#a48480c7b2b8319598e5d609acc6852cd)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a1e7d7594318c137d147918cb045ac5e9"></a>

```c
#define DMA_REQSEL_EUSART0RXFL (FIELD_PREP(DMA_SRC_MASK, 15) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_EUSART0RXFL](#a1e7d7594318c137d147918cb045ac5e9)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a5ba224acfec4569865731d9af8a4ea26"></a>

```c
#define DMA_REQSEL_EUSART0TXFL (FIELD_PREP(DMA_SRC_MASK, 15) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_EUSART0TXFL](#a5ba224acfec4569865731d9af8a4ea26)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_ae7962cdc63fac178d0e43dd85a5ec4c4"></a>

```c
#define DMA_REQSEL_EUSART1RXFL (FIELD_PREP(DMA_SRC_MASK, 16) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_EUSART1RXFL](#ae7962cdc63fac178d0e43dd85a5ec4c4)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a13d651b0c01c1370cb0b9806d5ce59cd"></a>

```c
#define DMA_REQSEL_EUSART1TXFL (FIELD_PREP(DMA_SRC_MASK, 16) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_EUSART1TXFL](#a13d651b0c01c1370cb0b9806d5ce59cd)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a5f302ab520d5f8260d8762ff70573875"></a>

```c
#define DMA_REQSEL_VDAC0CH0_REQ (FIELD_PREP(DMA_SRC_MASK, 17) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_VDAC0CH0_REQ](#a5f302ab520d5f8260d8762ff70573875)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a52b1969d55b83fa6113cbb996ece990f"></a>

```c
#define DMA_REQSEL_VDAC0CH1_REQ (FIELD_PREP(DMA_SRC_MASK, 17) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_VDAC0CH1_REQ](#a52b1969d55b83fa6113cbb996ece990f)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a3683966624835d3694c321177fb369ac"></a>

```c
#define DMA_REQSEL_VDAC1CH0_REQ (FIELD_PREP(DMA_SRC_MASK, 18) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_VDAC1CH0_REQ](#a3683966624835d3694c321177fb369ac)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_abc67fb24fa2f96b52f325b68974b2244"></a>

```c
#define DMA_REQSEL_VDAC1CH1_REQ (FIELD_PREP(DMA_SRC_MASK, 18) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_VDAC1CH1_REQ](#abc67fb24fa2f96b52f325b68974b2244)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a552a4ca6aefae8d8de9b66b8ee08e77b"></a>

```c
#define DMA_REQSEL_EUSART2RXFL (FIELD_PREP(DMA_SRC_MASK, 19) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_EUSART2RXFL](#a552a4ca6aefae8d8de9b66b8ee08e77b)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a94434f3457448e8aa8ca308b3f66ada5"></a>

```c
#define DMA_REQSEL_EUSART2TXFL (FIELD_PREP(DMA_SRC_MASK, 19) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_EUSART2TXFL](#a94434f3457448e8aa8ca308b3f66ada5)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a3226e4f7c1fb809190621e0787b12a01"></a>

```c
#define DMA_REQSEL_EUSART3RXFL (FIELD_PREP(DMA_SRC_MASK, 20) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_EUSART3RXFL](#a3226e4f7c1fb809190621e0787b12a01)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a0b56ad73e2d60e9b7e57922be8cd23d4"></a>

```c
#define DMA_REQSEL_EUSART3TXFL (FIELD_PREP(DMA_SRC_MASK, 20) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_EUSART3TXFL](#a0b56ad73e2d60e9b7e57922be8cd23d4)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_af3a58d9f0d3770d966077a57a4943c9d"></a>

```c
#define DMA_REQSEL_USART1RXDATAV (FIELD_PREP(DMA_SRC_MASK, 21) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_USART1RXDATAV](#af3a58d9f0d3770d966077a57a4943c9d)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a00a5c899f86f2df43b1d0d118a87eabf"></a>

```c
#define DMA_REQSEL_USART1RXDATAVRIGHT (FIELD_PREP(DMA_SRC_MASK, 21) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_USART1RXDATAVRIGHT](#a00a5c899f86f2df43b1d0d118a87eabf)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a40c0cf3975a32bd1ccede07dd7fad334"></a>

```c
#define DMA_REQSEL_USART1TXBL (FIELD_PREP(DMA_SRC_MASK, 21) | FIELD_PREP(DMA_SIG_MASK, 2))
```

相关声明：[DMA_REQSEL_USART1TXBL](#a40c0cf3975a32bd1ccede07dd7fad334)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a590b79286b632dc9fc12cf402d746d17"></a>

```c
#define DMA_REQSEL_USART1TXBLRIGHT (FIELD_PREP(DMA_SRC_MASK, 21) | FIELD_PREP(DMA_SIG_MASK, 3))
```

相关声明：[DMA_REQSEL_USART1TXBLRIGHT](#a590b79286b632dc9fc12cf402d746d17)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_ab94d4e0857f9400f93a51ee1201f6bb7"></a>

```c
#define DMA_REQSEL_USART1TXEMPTY (FIELD_PREP(DMA_SRC_MASK, 21) | FIELD_PREP(DMA_SIG_MASK, 4))
```

相关声明：[DMA_REQSEL_USART1TXEMPTY](#ab94d4e0857f9400f93a51ee1201f6bb7)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a9a6b856f36ea434d7fb1c771bf9e5b68"></a>

```c
#define DMA_REQSEL_USART2RXDATAV (FIELD_PREP(DMA_SRC_MASK, 22) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_USART2RXDATAV](#a9a6b856f36ea434d7fb1c771bf9e5b68)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a6ca7c10d705d1313b79c228df8a720f6"></a>

```c
#define DMA_REQSEL_USART2RXDATAVRIGHT (FIELD_PREP(DMA_SRC_MASK, 22) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_USART2RXDATAVRIGHT](#a6ca7c10d705d1313b79c228df8a720f6)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a1e0a363ff93f370d2731a116b5a53148"></a>

```c
#define DMA_REQSEL_USART2TXBL (FIELD_PREP(DMA_SRC_MASK, 22) | FIELD_PREP(DMA_SIG_MASK, 2))
```

相关声明：[DMA_REQSEL_USART2TXBL](#a1e0a363ff93f370d2731a116b5a53148)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a552d14b03c3974a9ec7edc2962c50119"></a>

```c
#define DMA_REQSEL_USART2TXBLRIGHT (FIELD_PREP(DMA_SRC_MASK, 22) | FIELD_PREP(DMA_SIG_MASK, 3))
```

相关声明：[DMA_REQSEL_USART2TXBLRIGHT](#a552d14b03c3974a9ec7edc2962c50119)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a315f45b4138fe8f09fff2772acbef060"></a>

```c
#define DMA_REQSEL_USART2TXEMPTY (FIELD_PREP(DMA_SRC_MASK, 22) | FIELD_PREP(DMA_SIG_MASK, 4))
```

相关声明：[DMA_REQSEL_USART2TXEMPTY](#a315f45b4138fe8f09fff2772acbef060)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a4e5807541c93205df3234f3b8e67ec60"></a>

```c
#define DMA_REQSEL_TIMER5CC0 (FIELD_PREP(DMA_SRC_MASK, 23) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_TIMER5CC0](#a4e5807541c93205df3234f3b8e67ec60)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_acd2d2bfeaf2421b05ffc5f7a89f774e2"></a>

```c
#define DMA_REQSEL_TIMER5CC1 (FIELD_PREP(DMA_SRC_MASK, 23) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_TIMER5CC1](#acd2d2bfeaf2421b05ffc5f7a89f774e2)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_adeb54b00ceb45c771523278062f80bed"></a>

```c
#define DMA_REQSEL_TIMER5CC2 (FIELD_PREP(DMA_SRC_MASK, 23) | FIELD_PREP(DMA_SIG_MASK, 2))
```

相关声明：[DMA_REQSEL_TIMER5CC2](#adeb54b00ceb45c771523278062f80bed)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_aaac9bf4ad41c4d416d299015ab193b15"></a>

```c
#define DMA_REQSEL_TIMER5UFOF (FIELD_PREP(DMA_SRC_MASK, 23) | FIELD_PREP(DMA_SIG_MASK, 3))
```

相关声明：[DMA_REQSEL_TIMER5UFOF](#aaac9bf4ad41c4d416d299015ab193b15)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a3ef91b2f24de93ab4265c36497ee4191"></a>

```c
#define DMA_REQSEL_TIMER6CC0 (FIELD_PREP(DMA_SRC_MASK, 24) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_TIMER6CC0](#a3ef91b2f24de93ab4265c36497ee4191)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_adba6558ec438ee5396ee2d5d3bbe6474"></a>

```c
#define DMA_REQSEL_TIMER6CC1 (FIELD_PREP(DMA_SRC_MASK, 24) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_TIMER6CC1](#adba6558ec438ee5396ee2d5d3bbe6474)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a177d828d1c5848ed445846d026fb1067"></a>

```c
#define DMA_REQSEL_TIMER6CC2 (FIELD_PREP(DMA_SRC_MASK, 24) | FIELD_PREP(DMA_SIG_MASK, 2))
```

相关声明：[DMA_REQSEL_TIMER6CC2](#a177d828d1c5848ed445846d026fb1067)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a595c9ed84534848d9057541dd79d2b3f"></a>

```c
#define DMA_REQSEL_TIMER6UFOF (FIELD_PREP(DMA_SRC_MASK, 24) | FIELD_PREP(DMA_SIG_MASK, 3))
```

相关声明：[DMA_REQSEL_TIMER6UFOF](#a595c9ed84534848d9057541dd79d2b3f)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a82976e0f4cc9b439fd31a54792d55a68"></a>

```c
#define DMA_REQSEL_TIMER7CC0 (FIELD_PREP(DMA_SRC_MASK, 25) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_TIMER7CC0](#a82976e0f4cc9b439fd31a54792d55a68)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a3aa023e46760d455118cfb36acfbfa5b"></a>

```c
#define DMA_REQSEL_TIMER7CC1 (FIELD_PREP(DMA_SRC_MASK, 25) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_TIMER7CC1](#a3aa023e46760d455118cfb36acfbfa5b)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a7f64819777953308a50247e1b637d7c3"></a>

```c
#define DMA_REQSEL_TIMER7CC2 (FIELD_PREP(DMA_SRC_MASK, 25) | FIELD_PREP(DMA_SIG_MASK, 2))
```

相关声明：[DMA_REQSEL_TIMER7CC2](#a7f64819777953308a50247e1b637d7c3)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a193abfab8485c33397bedb778d3e3628"></a>

```c
#define DMA_REQSEL_TIMER7UFOF (FIELD_PREP(DMA_SRC_MASK, 25) | FIELD_PREP(DMA_SIG_MASK, 3))
```

相关声明：[DMA_REQSEL_TIMER7UFOF](#a193abfab8485c33397bedb778d3e3628)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a24fc8cc95bdd57d3e8cb1c0ac51b431e"></a>

```c
#define DMA_REQSEL_TIMER8CC0 (FIELD_PREP(DMA_SRC_MASK, 26) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_TIMER8CC0](#a24fc8cc95bdd57d3e8cb1c0ac51b431e)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_abf8fcd733b9ecfca8f1cacc1b8845484"></a>

```c
#define DMA_REQSEL_TIMER8CC1 (FIELD_PREP(DMA_SRC_MASK, 26) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_TIMER8CC1](#abf8fcd733b9ecfca8f1cacc1b8845484)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a09601a37f599e612a36dc1a82b03df35"></a>

```c
#define DMA_REQSEL_TIMER8CC2 (FIELD_PREP(DMA_SRC_MASK, 26) | FIELD_PREP(DMA_SIG_MASK, 2))
```

相关声明：[DMA_REQSEL_TIMER8CC2](#a09601a37f599e612a36dc1a82b03df35)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_ae4473ba47ed73367d975a41c99bb1808"></a>

```c
#define DMA_REQSEL_TIMER8UFOF (FIELD_PREP(DMA_SRC_MASK, 26) | FIELD_PREP(DMA_SIG_MASK, 3))
```

相关声明：[DMA_REQSEL_TIMER8UFOF](#ae4473ba47ed73367d975a41c99bb1808)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_ad7a3e2a59419377805ab6b5f97f4d1f4"></a>

```c
#define DMA_REQSEL_TIMER9CC0 (FIELD_PREP(DMA_SRC_MASK, 27) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_TIMER9CC0](#ad7a3e2a59419377805ab6b5f97f4d1f4)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_aef4775c21b674eb749fc486f16ad87ae"></a>

```c
#define DMA_REQSEL_TIMER9CC1 (FIELD_PREP(DMA_SRC_MASK, 27) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_TIMER9CC1](#aef4775c21b674eb749fc486f16ad87ae)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a780f26c9efcc3e525a6c00d629a03686"></a>

```c
#define DMA_REQSEL_TIMER9CC2 (FIELD_PREP(DMA_SRC_MASK, 27) | FIELD_PREP(DMA_SIG_MASK, 2))
```

相关声明：[DMA_REQSEL_TIMER9CC2](#a780f26c9efcc3e525a6c00d629a03686)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_aaff37afd7ba3ee8407a9ebb709cb994a"></a>

```c
#define DMA_REQSEL_TIMER9UFOF (FIELD_PREP(DMA_SRC_MASK, 27) | FIELD_PREP(DMA_SIG_MASK, 3))
```

相关声明：[DMA_REQSEL_TIMER9UFOF](#aaff37afd7ba3ee8407a9ebb709cb994a)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_aa5ce60834351f372fb134cbac1a892a2"></a>

```c
#define DMA_REQSEL_I2C2RXDATAV (FIELD_PREP(DMA_SRC_MASK, 28) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_I2C2RXDATAV](#aa5ce60834351f372fb134cbac1a892a2)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a96cdf95c5760a3a8833eff9036a4ec8d"></a>

```c
#define DMA_REQSEL_I2C2TXBL (FIELD_PREP(DMA_SRC_MASK, 28) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_I2C2TXBL](#a96cdf95c5760a3a8833eff9036a4ec8d)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_ac8efe7e617c06df2f38e711e2a8b0308"></a>

```c
#define DMA_REQSEL_I2C3RXDATAV (FIELD_PREP(DMA_SRC_MASK, 29) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_I2C3RXDATAV](#ac8efe7e617c06df2f38e711e2a8b0308)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_afea7d1696b85ea1d80d80590f8a62c51"></a>

```c
#define DMA_REQSEL_I2C3TXBL (FIELD_PREP(DMA_SRC_MASK, 29) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_I2C3TXBL](#afea7d1696b85ea1d80d80590f8a62c51)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a34882387c47f04c312d46fa355d39d85"></a>

```c
#define DMA_REQSEL_LCD (FIELD_PREP(DMA_SRC_MASK, 30) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_LCD](#a34882387c47f04c312d46fa355d39d85)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_ad3c0178553c21a836e2c884335027825"></a>

```c
#define DMA_REQSEL_MVPREQ (FIELD_PREP(DMA_SRC_MASK, 31) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_MVPREQ](#ad3c0178553c21a836e2c884335027825)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

## 134.2\_详细说明（Detailed Documentation）

<a id="a1e7d7594318c137d147918cb045ac5e9"></a>

### `DMA_REQSEL_EUSART0RXFL`

```c
#define DMA_REQSEL_EUSART0RXFL (FIELD_PREP(DMA_SRC_MASK, 15) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="a5ba224acfec4569865731d9af8a4ea26"></a>

### `DMA_REQSEL_EUSART0TXFL`

```c
#define DMA_REQSEL_EUSART0TXFL (FIELD_PREP(DMA_SRC_MASK, 15) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="ae7962cdc63fac178d0e43dd85a5ec4c4"></a>

### `DMA_REQSEL_EUSART1RXFL`

```c
#define DMA_REQSEL_EUSART1RXFL (FIELD_PREP(DMA_SRC_MASK, 16) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="a13d651b0c01c1370cb0b9806d5ce59cd"></a>

### `DMA_REQSEL_EUSART1TXFL`

```c
#define DMA_REQSEL_EUSART1TXFL (FIELD_PREP(DMA_SRC_MASK, 16) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="a552a4ca6aefae8d8de9b66b8ee08e77b"></a>

### `DMA_REQSEL_EUSART2RXFL`

```c
#define DMA_REQSEL_EUSART2RXFL (FIELD_PREP(DMA_SRC_MASK, 19) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="a94434f3457448e8aa8ca308b3f66ada5"></a>

### `DMA_REQSEL_EUSART2TXFL`

```c
#define DMA_REQSEL_EUSART2TXFL (FIELD_PREP(DMA_SRC_MASK, 19) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="a3226e4f7c1fb809190621e0787b12a01"></a>

### `DMA_REQSEL_EUSART3RXFL`

```c
#define DMA_REQSEL_EUSART3RXFL (FIELD_PREP(DMA_SRC_MASK, 20) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="a0b56ad73e2d60e9b7e57922be8cd23d4"></a>

### `DMA_REQSEL_EUSART3TXFL`

```c
#define DMA_REQSEL_EUSART3TXFL (FIELD_PREP(DMA_SRC_MASK, 20) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="a27f66bf3557d8f7f3b34251f03334926"></a>

### `DMA_REQSEL_I2C0RXDATAV`

```c
#define DMA_REQSEL_I2C0RXDATAV (FIELD_PREP(DMA_SRC_MASK, 5) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="a724a2e12ee165d026039df6a016d043e"></a>

### `DMA_REQSEL_I2C0TXBL`

```c
#define DMA_REQSEL_I2C0TXBL (FIELD_PREP(DMA_SRC_MASK, 5) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="a02e993bfd9d57d946257bc34d6538347"></a>

### `DMA_REQSEL_I2C1RXDATAV`

```c
#define DMA_REQSEL_I2C1RXDATAV (FIELD_PREP(DMA_SRC_MASK, 6) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="af2f468e4d0dc9fce4cc54810e739f11d"></a>

### `DMA_REQSEL_I2C1TXBL`

```c
#define DMA_REQSEL_I2C1TXBL (FIELD_PREP(DMA_SRC_MASK, 6) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="aa5ce60834351f372fb134cbac1a892a2"></a>

### `DMA_REQSEL_I2C2RXDATAV`

```c
#define DMA_REQSEL_I2C2RXDATAV (FIELD_PREP(DMA_SRC_MASK, 28) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="a96cdf95c5760a3a8833eff9036a4ec8d"></a>

### `DMA_REQSEL_I2C2TXBL`

```c
#define DMA_REQSEL_I2C2TXBL (FIELD_PREP(DMA_SRC_MASK, 28) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="ac8efe7e617c06df2f38e711e2a8b0308"></a>

### `DMA_REQSEL_I2C3RXDATAV`

```c
#define DMA_REQSEL_I2C3RXDATAV (FIELD_PREP(DMA_SRC_MASK, 29) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="afea7d1696b85ea1d80d80590f8a62c51"></a>

### `DMA_REQSEL_I2C3TXBL`

```c
#define DMA_REQSEL_I2C3TXBL (FIELD_PREP(DMA_SRC_MASK, 29) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="a8940bc48310aad0e3c9cab0e5eb95742"></a>

### `DMA_REQSEL_IADC0IADC_SCAN`

```c
#define DMA_REQSEL_IADC0IADC_SCAN (FIELD_PREP(DMA_SRC_MASK, 10) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="ae8a09e6ec4fd8da57e5b568380afee64"></a>

### `DMA_REQSEL_IADC0IADC_SINGLE`

```c
#define DMA_REQSEL_IADC0IADC_SINGLE (FIELD_PREP(DMA_SRC_MASK, 10) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="a34882387c47f04c312d46fa355d39d85"></a>

### `DMA_REQSEL_LCD`

```c
#define DMA_REQSEL_LCD (FIELD_PREP(DMA_SRC_MASK, 30) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="ac27c323faa6e0db8d8e6439fdd277181"></a>

### `DMA_REQSEL_LDMAXBARPRSREQ0`

```c
#define DMA_REQSEL_LDMAXBARPRSREQ0 (FIELD_PREP(DMA_SRC_MASK, 1) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="ac20515cf65e2ca19ee0ad5f92403c6f1"></a>

### `DMA_REQSEL_LDMAXBARPRSREQ1`

```c
#define DMA_REQSEL_LDMAXBARPRSREQ1 (FIELD_PREP(DMA_SRC_MASK, 1) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="a296a10558a0bb7c76d3fd9eab80fff91"></a>

### `DMA_REQSEL_MSCWDATA`

```c
#define DMA_REQSEL_MSCWDATA (FIELD_PREP(DMA_SRC_MASK, 11) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="ad3c0178553c21a836e2c884335027825"></a>

### `DMA_REQSEL_MVPREQ`

```c
#define DMA_REQSEL_MVPREQ (FIELD_PREP(DMA_SRC_MASK, 31) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="a3b04d98c82d29396f8e688db8d5c5de9"></a>

### `DMA_REQSEL_NONE`

```c
#define DMA_REQSEL_NONE (FIELD_PREP(DMA_SRC_MASK, 0) | FIELD_PREP(DMA_SIG_MASK, 0))
```

Silabs 链接式 DMA 请求信号（LDMA Request Signal）的定义。

<a id="a6fc80a2f87eb37f53c77fff13ba28c85"></a>

### `DMA_REQSEL_TIMER0CC0`

```c
#define DMA_REQSEL_TIMER0CC0 (FIELD_PREP(DMA_SRC_MASK, 2) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="a310cc4350ec3f721a3ce4055ad8a1110"></a>

### `DMA_REQSEL_TIMER0CC1`

```c
#define DMA_REQSEL_TIMER0CC1 (FIELD_PREP(DMA_SRC_MASK, 2) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="a2d02b538557c468e47cad0aef76952ef"></a>

### `DMA_REQSEL_TIMER0CC2`

```c
#define DMA_REQSEL_TIMER0CC2 (FIELD_PREP(DMA_SRC_MASK, 2) | FIELD_PREP(DMA_SIG_MASK, 2))
```

<a id="a1862b04a508e5c89a565040f2b20ad0b"></a>

### `DMA_REQSEL_TIMER0UFOF`

```c
#define DMA_REQSEL_TIMER0UFOF (FIELD_PREP(DMA_SRC_MASK, 2) | FIELD_PREP(DMA_SIG_MASK, 3))
```

<a id="ab6c754dbaa545bda3ebe376825958008"></a>

### `DMA_REQSEL_TIMER1CC0`

```c
#define DMA_REQSEL_TIMER1CC0 (FIELD_PREP(DMA_SRC_MASK, 3) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="a909e0705fd68b7e79f6d07e5c9e7d9e9"></a>

### `DMA_REQSEL_TIMER1CC1`

```c
#define DMA_REQSEL_TIMER1CC1 (FIELD_PREP(DMA_SRC_MASK, 3) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="a7299498af9580ac0236dfd776394e4f1"></a>

### `DMA_REQSEL_TIMER1CC2`

```c
#define DMA_REQSEL_TIMER1CC2 (FIELD_PREP(DMA_SRC_MASK, 3) | FIELD_PREP(DMA_SIG_MASK, 2))
```

<a id="a13f9bb1b7de6061b0eebca52e4349c71"></a>

### `DMA_REQSEL_TIMER1UFOF`

```c
#define DMA_REQSEL_TIMER1UFOF (FIELD_PREP(DMA_SRC_MASK, 3) | FIELD_PREP(DMA_SIG_MASK, 3))
```

<a id="a8503415586264bbbc2c17560dfa36325"></a>

### `DMA_REQSEL_TIMER2CC0`

```c
#define DMA_REQSEL_TIMER2CC0 (FIELD_PREP(DMA_SRC_MASK, 12) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="aed70ea120b2a199163c46f028aec4538"></a>

### `DMA_REQSEL_TIMER2CC1`

```c
#define DMA_REQSEL_TIMER2CC1 (FIELD_PREP(DMA_SRC_MASK, 12) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="aff76df3b43b1ce7ff7cf36dad62914b5"></a>

### `DMA_REQSEL_TIMER2CC2`

```c
#define DMA_REQSEL_TIMER2CC2 (FIELD_PREP(DMA_SRC_MASK, 12) | FIELD_PREP(DMA_SIG_MASK, 2))
```

<a id="a359eec69c4e20a62fda0382318777ca2"></a>

### `DMA_REQSEL_TIMER2UFOF`

```c
#define DMA_REQSEL_TIMER2UFOF (FIELD_PREP(DMA_SRC_MASK, 12) | FIELD_PREP(DMA_SIG_MASK, 3))
```

<a id="acd2b7ad92fa2c7fe11b0410760e431d0"></a>

### `DMA_REQSEL_TIMER3CC0`

```c
#define DMA_REQSEL_TIMER3CC0 (FIELD_PREP(DMA_SRC_MASK, 13) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="ac875ac8e9ee74e79df2e9a7e7f7d47bc"></a>

### `DMA_REQSEL_TIMER3CC1`

```c
#define DMA_REQSEL_TIMER3CC1 (FIELD_PREP(DMA_SRC_MASK, 13) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="a84068b2390c9db03e234e8ebf7dd844e"></a>

### `DMA_REQSEL_TIMER3CC2`

```c
#define DMA_REQSEL_TIMER3CC2 (FIELD_PREP(DMA_SRC_MASK, 13) | FIELD_PREP(DMA_SIG_MASK, 2))
```

<a id="a0b099b82ec5b12e2da5d9fcafeb6feb4"></a>

### `DMA_REQSEL_TIMER3UFOF`

```c
#define DMA_REQSEL_TIMER3UFOF (FIELD_PREP(DMA_SRC_MASK, 13) | FIELD_PREP(DMA_SIG_MASK, 3))
```

<a id="a91a9946b6909ffb54bd69df41c5d9907"></a>

### `DMA_REQSEL_TIMER4CC0`

```c
#define DMA_REQSEL_TIMER4CC0 (FIELD_PREP(DMA_SRC_MASK, 14) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="a3a12807722a1716c6bb6e58143441870"></a>

### `DMA_REQSEL_TIMER4CC1`

```c
#define DMA_REQSEL_TIMER4CC1 (FIELD_PREP(DMA_SRC_MASK, 14) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="a3af0824dce9be11286d8521bb051554c"></a>

### `DMA_REQSEL_TIMER4CC2`

```c
#define DMA_REQSEL_TIMER4CC2 (FIELD_PREP(DMA_SRC_MASK, 14) | FIELD_PREP(DMA_SIG_MASK, 2))
```

<a id="a48480c7b2b8319598e5d609acc6852cd"></a>

### `DMA_REQSEL_TIMER4UFOF`

```c
#define DMA_REQSEL_TIMER4UFOF (FIELD_PREP(DMA_SRC_MASK, 14) | FIELD_PREP(DMA_SIG_MASK, 3))
```

<a id="a4e5807541c93205df3234f3b8e67ec60"></a>

### `DMA_REQSEL_TIMER5CC0`

```c
#define DMA_REQSEL_TIMER5CC0 (FIELD_PREP(DMA_SRC_MASK, 23) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="acd2d2bfeaf2421b05ffc5f7a89f774e2"></a>

### `DMA_REQSEL_TIMER5CC1`

```c
#define DMA_REQSEL_TIMER5CC1 (FIELD_PREP(DMA_SRC_MASK, 23) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="adeb54b00ceb45c771523278062f80bed"></a>

### `DMA_REQSEL_TIMER5CC2`

```c
#define DMA_REQSEL_TIMER5CC2 (FIELD_PREP(DMA_SRC_MASK, 23) | FIELD_PREP(DMA_SIG_MASK, 2))
```

<a id="aaac9bf4ad41c4d416d299015ab193b15"></a>

### `DMA_REQSEL_TIMER5UFOF`

```c
#define DMA_REQSEL_TIMER5UFOF (FIELD_PREP(DMA_SRC_MASK, 23) | FIELD_PREP(DMA_SIG_MASK, 3))
```

<a id="a3ef91b2f24de93ab4265c36497ee4191"></a>

### `DMA_REQSEL_TIMER6CC0`

```c
#define DMA_REQSEL_TIMER6CC0 (FIELD_PREP(DMA_SRC_MASK, 24) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="adba6558ec438ee5396ee2d5d3bbe6474"></a>

### `DMA_REQSEL_TIMER6CC1`

```c
#define DMA_REQSEL_TIMER6CC1 (FIELD_PREP(DMA_SRC_MASK, 24) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="a177d828d1c5848ed445846d026fb1067"></a>

### `DMA_REQSEL_TIMER6CC2`

```c
#define DMA_REQSEL_TIMER6CC2 (FIELD_PREP(DMA_SRC_MASK, 24) | FIELD_PREP(DMA_SIG_MASK, 2))
```

<a id="a595c9ed84534848d9057541dd79d2b3f"></a>

### `DMA_REQSEL_TIMER6UFOF`

```c
#define DMA_REQSEL_TIMER6UFOF (FIELD_PREP(DMA_SRC_MASK, 24) | FIELD_PREP(DMA_SIG_MASK, 3))
```

<a id="a82976e0f4cc9b439fd31a54792d55a68"></a>

### `DMA_REQSEL_TIMER7CC0`

```c
#define DMA_REQSEL_TIMER7CC0 (FIELD_PREP(DMA_SRC_MASK, 25) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="a3aa023e46760d455118cfb36acfbfa5b"></a>

### `DMA_REQSEL_TIMER7CC1`

```c
#define DMA_REQSEL_TIMER7CC1 (FIELD_PREP(DMA_SRC_MASK, 25) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="a7f64819777953308a50247e1b637d7c3"></a>

### `DMA_REQSEL_TIMER7CC2`

```c
#define DMA_REQSEL_TIMER7CC2 (FIELD_PREP(DMA_SRC_MASK, 25) | FIELD_PREP(DMA_SIG_MASK, 2))
```

<a id="a193abfab8485c33397bedb778d3e3628"></a>

### `DMA_REQSEL_TIMER7UFOF`

```c
#define DMA_REQSEL_TIMER7UFOF (FIELD_PREP(DMA_SRC_MASK, 25) | FIELD_PREP(DMA_SIG_MASK, 3))
```

<a id="a24fc8cc95bdd57d3e8cb1c0ac51b431e"></a>

### `DMA_REQSEL_TIMER8CC0`

```c
#define DMA_REQSEL_TIMER8CC0 (FIELD_PREP(DMA_SRC_MASK, 26) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="abf8fcd733b9ecfca8f1cacc1b8845484"></a>

### `DMA_REQSEL_TIMER8CC1`

```c
#define DMA_REQSEL_TIMER8CC1 (FIELD_PREP(DMA_SRC_MASK, 26) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="a09601a37f599e612a36dc1a82b03df35"></a>

### `DMA_REQSEL_TIMER8CC2`

```c
#define DMA_REQSEL_TIMER8CC2 (FIELD_PREP(DMA_SRC_MASK, 26) | FIELD_PREP(DMA_SIG_MASK, 2))
```

<a id="ae4473ba47ed73367d975a41c99bb1808"></a>

### `DMA_REQSEL_TIMER8UFOF`

```c
#define DMA_REQSEL_TIMER8UFOF (FIELD_PREP(DMA_SRC_MASK, 26) | FIELD_PREP(DMA_SIG_MASK, 3))
```

<a id="ad7a3e2a59419377805ab6b5f97f4d1f4"></a>

### `DMA_REQSEL_TIMER9CC0`

```c
#define DMA_REQSEL_TIMER9CC0 (FIELD_PREP(DMA_SRC_MASK, 27) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="aef4775c21b674eb749fc486f16ad87ae"></a>

### `DMA_REQSEL_TIMER9CC1`

```c
#define DMA_REQSEL_TIMER9CC1 (FIELD_PREP(DMA_SRC_MASK, 27) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="a780f26c9efcc3e525a6c00d629a03686"></a>

### `DMA_REQSEL_TIMER9CC2`

```c
#define DMA_REQSEL_TIMER9CC2 (FIELD_PREP(DMA_SRC_MASK, 27) | FIELD_PREP(DMA_SIG_MASK, 2))
```

<a id="aaff37afd7ba3ee8407a9ebb709cb994a"></a>

### `DMA_REQSEL_TIMER9UFOF`

```c
#define DMA_REQSEL_TIMER9UFOF (FIELD_PREP(DMA_SRC_MASK, 27) | FIELD_PREP(DMA_SIG_MASK, 3))
```

<a id="a4d8e451527281f0292c491fd1f40f709"></a>

### `DMA_REQSEL_USART0RXDATAV`

```c
#define DMA_REQSEL_USART0RXDATAV (FIELD_PREP(DMA_SRC_MASK, 4) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="a17598696e9a520ac6adea3920eff6900"></a>

### `DMA_REQSEL_USART0RXDATAVRIGHT`

```c
#define DMA_REQSEL_USART0RXDATAVRIGHT (FIELD_PREP(DMA_SRC_MASK, 4) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="ae691ddb9858cbd5205c2d62ea54a2797"></a>

### `DMA_REQSEL_USART0TXBL`

```c
#define DMA_REQSEL_USART0TXBL (FIELD_PREP(DMA_SRC_MASK, 4) | FIELD_PREP(DMA_SIG_MASK, 2))
```

<a id="adf8abf7448fea14cbc7dcd946a1dfd91"></a>

### `DMA_REQSEL_USART0TXBLRIGHT`

```c
#define DMA_REQSEL_USART0TXBLRIGHT (FIELD_PREP(DMA_SRC_MASK, 4) | FIELD_PREP(DMA_SIG_MASK, 3))
```

<a id="a180469c6cace2af0e91336b25d18ece1"></a>

### `DMA_REQSEL_USART0TXEMPTY`

```c
#define DMA_REQSEL_USART0TXEMPTY (FIELD_PREP(DMA_SRC_MASK, 4) | FIELD_PREP(DMA_SIG_MASK, 4))
```

<a id="af3a58d9f0d3770d966077a57a4943c9d"></a>

### `DMA_REQSEL_USART1RXDATAV`

```c
#define DMA_REQSEL_USART1RXDATAV (FIELD_PREP(DMA_SRC_MASK, 21) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="a00a5c899f86f2df43b1d0d118a87eabf"></a>

### `DMA_REQSEL_USART1RXDATAVRIGHT`

```c
#define DMA_REQSEL_USART1RXDATAVRIGHT (FIELD_PREP(DMA_SRC_MASK, 21) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="a40c0cf3975a32bd1ccede07dd7fad334"></a>

### `DMA_REQSEL_USART1TXBL`

```c
#define DMA_REQSEL_USART1TXBL (FIELD_PREP(DMA_SRC_MASK, 21) | FIELD_PREP(DMA_SIG_MASK, 2))
```

<a id="a590b79286b632dc9fc12cf402d746d17"></a>

### `DMA_REQSEL_USART1TXBLRIGHT`

```c
#define DMA_REQSEL_USART1TXBLRIGHT (FIELD_PREP(DMA_SRC_MASK, 21) | FIELD_PREP(DMA_SIG_MASK, 3))
```

<a id="ab94d4e0857f9400f93a51ee1201f6bb7"></a>

### `DMA_REQSEL_USART1TXEMPTY`

```c
#define DMA_REQSEL_USART1TXEMPTY (FIELD_PREP(DMA_SRC_MASK, 21) | FIELD_PREP(DMA_SIG_MASK, 4))
```

<a id="a9a6b856f36ea434d7fb1c771bf9e5b68"></a>

### `DMA_REQSEL_USART2RXDATAV`

```c
#define DMA_REQSEL_USART2RXDATAV (FIELD_PREP(DMA_SRC_MASK, 22) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="a6ca7c10d705d1313b79c228df8a720f6"></a>

### `DMA_REQSEL_USART2RXDATAVRIGHT`

```c
#define DMA_REQSEL_USART2RXDATAVRIGHT (FIELD_PREP(DMA_SRC_MASK, 22) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="a1e0a363ff93f370d2731a116b5a53148"></a>

### `DMA_REQSEL_USART2TXBL`

```c
#define DMA_REQSEL_USART2TXBL (FIELD_PREP(DMA_SRC_MASK, 22) | FIELD_PREP(DMA_SIG_MASK, 2))
```

<a id="a552d14b03c3974a9ec7edc2962c50119"></a>

### `DMA_REQSEL_USART2TXBLRIGHT`

```c
#define DMA_REQSEL_USART2TXBLRIGHT (FIELD_PREP(DMA_SRC_MASK, 22) | FIELD_PREP(DMA_SIG_MASK, 3))
```

<a id="a315f45b4138fe8f09fff2772acbef060"></a>

### `DMA_REQSEL_USART2TXEMPTY`

```c
#define DMA_REQSEL_USART2TXEMPTY (FIELD_PREP(DMA_SRC_MASK, 22) | FIELD_PREP(DMA_SIG_MASK, 4))
```

<a id="a5f302ab520d5f8260d8762ff70573875"></a>

### `DMA_REQSEL_VDAC0CH0_REQ`

```c
#define DMA_REQSEL_VDAC0CH0_REQ (FIELD_PREP(DMA_SRC_MASK, 17) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="a52b1969d55b83fa6113cbb996ece990f"></a>

### `DMA_REQSEL_VDAC0CH1_REQ`

```c
#define DMA_REQSEL_VDAC0CH1_REQ (FIELD_PREP(DMA_SRC_MASK, 17) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="a3683966624835d3694c321177fb369ac"></a>

### `DMA_REQSEL_VDAC1CH0_REQ`

```c
#define DMA_REQSEL_VDAC1CH0_REQ (FIELD_PREP(DMA_SRC_MASK, 18) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="abc67fb24fa2f96b52f325b68974b2244"></a>

### `DMA_REQSEL_VDAC1CH1_REQ`

```c
#define DMA_REQSEL_VDAC1CH1_REQ (FIELD_PREP(DMA_SRC_MASK, 18) | FIELD_PREP(DMA_SIG_MASK, 1))
```


## 134.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P006_设备树绑定工具头文件源码.md)
- [common-dma.h](../api_source_reference/P110_common-dma.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P937_xg26-dma.h_源码浏览.md)
- [FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)
- [DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)
- [DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P133_zephyr__dt-bindings__dma__silabs__xg24-dma.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P135_zephyr__dt-bindings__dma__silabs__xg27-dma.h_文件参考.md)
