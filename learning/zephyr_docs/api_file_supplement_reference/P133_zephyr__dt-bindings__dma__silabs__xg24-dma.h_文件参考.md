---
id: learning.zephyr-docs.api-file-supplement-reference.page-133
title: zephyr__dt-bindings__dma__silabs__xg24-dma.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/xg24-dma_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第133章\_zephyr\_\_dt-bindings\_\_dma\_\_silabs\_\_xg24-dma.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/xg24-dma_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/dt-bindings/dt-util.h>
#include "common-dma.h"
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 133.1\_宏定义（Macros）

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

## 133.2\_详细说明（Detailed Documentation）

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


## 133.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P006_设备树绑定工具头文件源码.md)
- [common-dma.h](../api_source_reference/P110_common-dma.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P936_xg24-dma.h_源码浏览.md)
- [FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)
- [DMA_SRC_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)
- [DMA_SIG_MASK](../api_file_reference/P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P132_zephyr__dt-bindings__dma__silabs__xg23-dma.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P134_zephyr__dt-bindings__dma__silabs__xg26-dma.h_文件参考.md)
