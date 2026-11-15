---
id: learning.zephyr-docs.api-file-reference.page-398
title: zephyr__dt-bindings__dma__silabs__six301-dma.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/six301-dma_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第398章\_zephyr\_\_dt-bindings\_\_dma\_\_silabs\_\_six301-dma.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/six301-dma_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/dt-bindings/dt-util.h>
#include "common-dma.h"
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 398.1\_宏定义（Macros）

<a id="r_a3b04d98c82d29396f8e688db8d5c5de9"></a>

```c
#define DMA_REQSEL_NONE (FIELD_PREP(DMA_SRC_MASK, 0) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_NONE](#a3b04d98c82d29396f8e688db8d5c5de9)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_abb2f7d71f28c62f1616ca9c42368b5bf"></a>

```c
#define DMA_REQSEL_LDMAXBAR0PRSREQ0 (FIELD_PREP(DMA_SRC_MASK, 1) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_LDMAXBAR0PRSREQ0](#abb2f7d71f28c62f1616ca9c42368b5bf)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_ae19ab9dccb4288c4c251bf8eb1f5a002"></a>

```c
#define DMA_REQSEL_LDMAXBAR0PRSREQ1 (FIELD_PREP(DMA_SRC_MASK, 1) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_LDMAXBAR0PRSREQ1](#ae19ab9dccb4288c4c251bf8eb1f5a002)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a6fc80a2f87eb37f53c77fff13ba28c85"></a>

```c
#define DMA_REQSEL_TIMER0CC0 (FIELD_PREP(DMA_SRC_MASK, 2) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_TIMER0CC0](#a6fc80a2f87eb37f53c77fff13ba28c85)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a310cc4350ec3f721a3ce4055ad8a1110"></a>

```c
#define DMA_REQSEL_TIMER0CC1 (FIELD_PREP(DMA_SRC_MASK, 2) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_TIMER0CC1](#a310cc4350ec3f721a3ce4055ad8a1110)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a2d02b538557c468e47cad0aef76952ef"></a>

```c
#define DMA_REQSEL_TIMER0CC2 (FIELD_PREP(DMA_SRC_MASK, 2) | FIELD_PREP(DMA_SIG_MASK, 2))
```

相关声明：[DMA_REQSEL_TIMER0CC2](#a2d02b538557c468e47cad0aef76952ef)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a1862b04a508e5c89a565040f2b20ad0b"></a>

```c
#define DMA_REQSEL_TIMER0UFOF (FIELD_PREP(DMA_SRC_MASK, 2) | FIELD_PREP(DMA_SIG_MASK, 3))
```

相关声明：[DMA_REQSEL_TIMER0UFOF](#a1862b04a508e5c89a565040f2b20ad0b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_ab6c754dbaa545bda3ebe376825958008"></a>

```c
#define DMA_REQSEL_TIMER1CC0 (FIELD_PREP(DMA_SRC_MASK, 3) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_TIMER1CC0](#ab6c754dbaa545bda3ebe376825958008)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a909e0705fd68b7e79f6d07e5c9e7d9e9"></a>

```c
#define DMA_REQSEL_TIMER1CC1 (FIELD_PREP(DMA_SRC_MASK, 3) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_TIMER1CC1](#a909e0705fd68b7e79f6d07e5c9e7d9e9)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a7299498af9580ac0236dfd776394e4f1"></a>

```c
#define DMA_REQSEL_TIMER1CC2 (FIELD_PREP(DMA_SRC_MASK, 3) | FIELD_PREP(DMA_SIG_MASK, 2))
```

相关声明：[DMA_REQSEL_TIMER1CC2](#a7299498af9580ac0236dfd776394e4f1)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a13f9bb1b7de6061b0eebca52e4349c71"></a>

```c
#define DMA_REQSEL_TIMER1UFOF (FIELD_PREP(DMA_SRC_MASK, 3) | FIELD_PREP(DMA_SIG_MASK, 3))
```

相关声明：[DMA_REQSEL_TIMER1UFOF](#a13f9bb1b7de6061b0eebca52e4349c71)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a27f66bf3557d8f7f3b34251f03334926"></a>

```c
#define DMA_REQSEL_I2C0RXDATAV (FIELD_PREP(DMA_SRC_MASK, 4) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_I2C0RXDATAV](#a27f66bf3557d8f7f3b34251f03334926)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a724a2e12ee165d026039df6a016d043e"></a>

```c
#define DMA_REQSEL_I2C0TXBL (FIELD_PREP(DMA_SRC_MASK, 4) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_I2C0TXBL](#a724a2e12ee165d026039df6a016d043e)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a02e993bfd9d57d946257bc34d6538347"></a>

```c
#define DMA_REQSEL_I2C1RXDATAV (FIELD_PREP(DMA_SRC_MASK, 5) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_I2C1RXDATAV](#a02e993bfd9d57d946257bc34d6538347)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_af2f468e4d0dc9fce4cc54810e739f11d"></a>

```c
#define DMA_REQSEL_I2C1TXBL (FIELD_PREP(DMA_SRC_MASK, 5) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_I2C1TXBL](#af2f468e4d0dc9fce4cc54810e739f11d)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a8503415586264bbbc2c17560dfa36325"></a>

```c
#define DMA_REQSEL_TIMER2CC0 (FIELD_PREP(DMA_SRC_MASK, 6) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_TIMER2CC0](#a8503415586264bbbc2c17560dfa36325)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_aed70ea120b2a199163c46f028aec4538"></a>

```c
#define DMA_REQSEL_TIMER2CC1 (FIELD_PREP(DMA_SRC_MASK, 6) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_TIMER2CC1](#aed70ea120b2a199163c46f028aec4538)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_aff76df3b43b1ce7ff7cf36dad62914b5"></a>

```c
#define DMA_REQSEL_TIMER2CC2 (FIELD_PREP(DMA_SRC_MASK, 6) | FIELD_PREP(DMA_SIG_MASK, 2))
```

相关声明：[DMA_REQSEL_TIMER2CC2](#aff76df3b43b1ce7ff7cf36dad62914b5)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a359eec69c4e20a62fda0382318777ca2"></a>

```c
#define DMA_REQSEL_TIMER2UFOF (FIELD_PREP(DMA_SRC_MASK, 6) | FIELD_PREP(DMA_SIG_MASK, 3))
```

相关声明：[DMA_REQSEL_TIMER2UFOF](#a359eec69c4e20a62fda0382318777ca2)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a1381c6c857dc7d9c0f0078369fb63052"></a>

```c
#define DMA_REQSEL_TIMER2CC3 (FIELD_PREP(DMA_SRC_MASK, 6) | FIELD_PREP(DMA_SIG_MASK, 4))
```

相关声明：[DMA_REQSEL_TIMER2CC3](#a1381c6c857dc7d9c0f0078369fb63052)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_ad5e5b9d61676e95c0865d9051574f46c"></a>

```c
#define DMA_REQSEL_TIMER2CC4 (FIELD_PREP(DMA_SRC_MASK, 6) | FIELD_PREP(DMA_SIG_MASK, 5))
```

相关声明：[DMA_REQSEL_TIMER2CC4](#ad5e5b9d61676e95c0865d9051574f46c)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a5e501f1be583a0f0b70167c3d75e7673"></a>

```c
#define DMA_REQSEL_TIMER2CC5 (FIELD_PREP(DMA_SRC_MASK, 6) | FIELD_PREP(DMA_SIG_MASK, 6))
```

相关声明：[DMA_REQSEL_TIMER2CC5](#a5e501f1be583a0f0b70167c3d75e7673)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_abaf6c71d249d869af3507418f873bbe8"></a>

```c
#define DMA_REQSEL_TIMER2CC6 (FIELD_PREP(DMA_SRC_MASK, 6) | FIELD_PREP(DMA_SIG_MASK, 7))
```

相关声明：[DMA_REQSEL_TIMER2CC6](#abaf6c71d249d869af3507418f873bbe8)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_acd2b7ad92fa2c7fe11b0410760e431d0"></a>

```c
#define DMA_REQSEL_TIMER3CC0 (FIELD_PREP(DMA_SRC_MASK, 7) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_TIMER3CC0](#acd2b7ad92fa2c7fe11b0410760e431d0)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_ac875ac8e9ee74e79df2e9a7e7f7d47bc"></a>

```c
#define DMA_REQSEL_TIMER3CC1 (FIELD_PREP(DMA_SRC_MASK, 7) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_TIMER3CC1](#ac875ac8e9ee74e79df2e9a7e7f7d47bc)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a84068b2390c9db03e234e8ebf7dd844e"></a>

```c
#define DMA_REQSEL_TIMER3CC2 (FIELD_PREP(DMA_SRC_MASK, 7) | FIELD_PREP(DMA_SIG_MASK, 2))
```

相关声明：[DMA_REQSEL_TIMER3CC2](#a84068b2390c9db03e234e8ebf7dd844e)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a0b099b82ec5b12e2da5d9fcafeb6feb4"></a>

```c
#define DMA_REQSEL_TIMER3UFOF (FIELD_PREP(DMA_SRC_MASK, 7) | FIELD_PREP(DMA_SIG_MASK, 3))
```

相关声明：[DMA_REQSEL_TIMER3UFOF](#a0b099b82ec5b12e2da5d9fcafeb6feb4)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_adf86873e038d26d178cf3c1ccb22a4d4"></a>

```c
#define DMA_REQSEL_TIMER3CC3 (FIELD_PREP(DMA_SRC_MASK, 7) | FIELD_PREP(DMA_SIG_MASK, 4))
```

相关声明：[DMA_REQSEL_TIMER3CC3](#adf86873e038d26d178cf3c1ccb22a4d4)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_adad81e665fbfbc456b3f3744863cc6bc"></a>

```c
#define DMA_REQSEL_TIMER3CC4 (FIELD_PREP(DMA_SRC_MASK, 7) | FIELD_PREP(DMA_SIG_MASK, 5))
```

相关声明：[DMA_REQSEL_TIMER3CC4](#adad81e665fbfbc456b3f3744863cc6bc)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a3635d73b218da5379408924c679e6538"></a>

```c
#define DMA_REQSEL_TIMER3CC5 (FIELD_PREP(DMA_SRC_MASK, 7) | FIELD_PREP(DMA_SIG_MASK, 6))
```

相关声明：[DMA_REQSEL_TIMER3CC5](#a3635d73b218da5379408924c679e6538)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a5a1164ef2515a577d28fdee53a0fc949"></a>

```c
#define DMA_REQSEL_TIMER3CC6 (FIELD_PREP(DMA_SRC_MASK, 7) | FIELD_PREP(DMA_SIG_MASK, 7))
```

相关声明：[DMA_REQSEL_TIMER3CC6](#a5a1164ef2515a577d28fdee53a0fc949)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_ae7962cdc63fac178d0e43dd85a5ec4c4"></a>

```c
#define DMA_REQSEL_EUSART1RXFL (FIELD_PREP(DMA_SRC_MASK, 8) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_EUSART1RXFL](#ae7962cdc63fac178d0e43dd85a5ec4c4)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a13d651b0c01c1370cb0b9806d5ce59cd"></a>

```c
#define DMA_REQSEL_EUSART1TXFL (FIELD_PREP(DMA_SRC_MASK, 8) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_EUSART1TXFL](#a13d651b0c01c1370cb0b9806d5ce59cd)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a1e7d7594318c137d147918cb045ac5e9"></a>

```c
#define DMA_REQSEL_EUSART0RXFL (FIELD_PREP(DMA_SRC_MASK, 9) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_EUSART0RXFL](#a1e7d7594318c137d147918cb045ac5e9)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a5ba224acfec4569865731d9af8a4ea26"></a>

```c
#define DMA_REQSEL_EUSART0TXFL (FIELD_PREP(DMA_SRC_MASK, 9) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_EUSART0TXFL](#a5ba224acfec4569865731d9af8a4ea26)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a9c8d588ed1276c5da3479ce7fec33749"></a>

```c
#define DMA_REQSEL_ADC0SCAN (FIELD_PREP(DMA_SRC_MASK, 13) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_ADC0SCAN](#a9c8d588ed1276c5da3479ce7fec33749)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a5c445181f71322b2554dbb25e780e18e"></a>

```c
#define DMA_REQSEL_PIXELRZ0REQ_TXF (FIELD_PREP(DMA_SRC_MASK, 14) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_PIXELRZ0REQ_TXF](#a5c445181f71322b2554dbb25e780e18e)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a552a4ca6aefae8d8de9b66b8ee08e77b"></a>

```c
#define DMA_REQSEL_EUSART2RXFL (FIELD_PREP(DMA_SRC_MASK, 15) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_EUSART2RXFL](#a552a4ca6aefae8d8de9b66b8ee08e77b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a94434f3457448e8aa8ca308b3f66ada5"></a>

```c
#define DMA_REQSEL_EUSART2TXFL (FIELD_PREP(DMA_SRC_MASK, 15) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_EUSART2TXFL](#a94434f3457448e8aa8ca308b3f66ada5)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a4e870a3b8a8926a3d853b611487299e6"></a>

```c
#define DMA_REQSEL_PIXELRZ1REQ_TXF (FIELD_PREP(DMA_SRC_MASK, 16) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_PIXELRZ1REQ_TXF](#a4e870a3b8a8926a3d853b611487299e6)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_aa5ce60834351f372fb134cbac1a892a2"></a>

```c
#define DMA_REQSEL_I2C2RXDATAV (FIELD_PREP(DMA_SRC_MASK, 17) | FIELD_PREP(DMA_SIG_MASK, 0))
```

相关声明：[DMA_REQSEL_I2C2RXDATAV](#aa5ce60834351f372fb134cbac1a892a2)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

<a id="r_a96cdf95c5760a3a8833eff9036a4ec8d"></a>

```c
#define DMA_REQSEL_I2C2TXBL (FIELD_PREP(DMA_SRC_MASK, 17) | FIELD_PREP(DMA_SIG_MASK, 1))
```

相关声明：[DMA_REQSEL_I2C2TXBL](#a96cdf95c5760a3a8833eff9036a4ec8d)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)。

## 398.2\_详细说明（Detailed Documentation）

<a id="a9c8d588ed1276c5da3479ce7fec33749"></a>

### `DMA_REQSEL_ADC0SCAN`

```c
#define DMA_REQSEL_ADC0SCAN (FIELD_PREP(DMA_SRC_MASK, 13) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="a1e7d7594318c137d147918cb045ac5e9"></a>

### `DMA_REQSEL_EUSART0RXFL`

```c
#define DMA_REQSEL_EUSART0RXFL (FIELD_PREP(DMA_SRC_MASK, 9) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="a5ba224acfec4569865731d9af8a4ea26"></a>

### `DMA_REQSEL_EUSART0TXFL`

```c
#define DMA_REQSEL_EUSART0TXFL (FIELD_PREP(DMA_SRC_MASK, 9) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="ae7962cdc63fac178d0e43dd85a5ec4c4"></a>

### `DMA_REQSEL_EUSART1RXFL`

```c
#define DMA_REQSEL_EUSART1RXFL (FIELD_PREP(DMA_SRC_MASK, 8) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="a13d651b0c01c1370cb0b9806d5ce59cd"></a>

### `DMA_REQSEL_EUSART1TXFL`

```c
#define DMA_REQSEL_EUSART1TXFL (FIELD_PREP(DMA_SRC_MASK, 8) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="a552a4ca6aefae8d8de9b66b8ee08e77b"></a>

### `DMA_REQSEL_EUSART2RXFL`

```c
#define DMA_REQSEL_EUSART2RXFL (FIELD_PREP(DMA_SRC_MASK, 15) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="a94434f3457448e8aa8ca308b3f66ada5"></a>

### `DMA_REQSEL_EUSART2TXFL`

```c
#define DMA_REQSEL_EUSART2TXFL (FIELD_PREP(DMA_SRC_MASK, 15) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="a27f66bf3557d8f7f3b34251f03334926"></a>

### `DMA_REQSEL_I2C0RXDATAV`

```c
#define DMA_REQSEL_I2C0RXDATAV (FIELD_PREP(DMA_SRC_MASK, 4) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="a724a2e12ee165d026039df6a016d043e"></a>

### `DMA_REQSEL_I2C0TXBL`

```c
#define DMA_REQSEL_I2C0TXBL (FIELD_PREP(DMA_SRC_MASK, 4) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="a02e993bfd9d57d946257bc34d6538347"></a>

### `DMA_REQSEL_I2C1RXDATAV`

```c
#define DMA_REQSEL_I2C1RXDATAV (FIELD_PREP(DMA_SRC_MASK, 5) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="af2f468e4d0dc9fce4cc54810e739f11d"></a>

### `DMA_REQSEL_I2C1TXBL`

```c
#define DMA_REQSEL_I2C1TXBL (FIELD_PREP(DMA_SRC_MASK, 5) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="aa5ce60834351f372fb134cbac1a892a2"></a>

### `DMA_REQSEL_I2C2RXDATAV`

```c
#define DMA_REQSEL_I2C2RXDATAV (FIELD_PREP(DMA_SRC_MASK, 17) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="a96cdf95c5760a3a8833eff9036a4ec8d"></a>

### `DMA_REQSEL_I2C2TXBL`

```c
#define DMA_REQSEL_I2C2TXBL (FIELD_PREP(DMA_SRC_MASK, 17) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="abb2f7d71f28c62f1616ca9c42368b5bf"></a>

### `DMA_REQSEL_LDMAXBAR0PRSREQ0`

```c
#define DMA_REQSEL_LDMAXBAR0PRSREQ0 (FIELD_PREP(DMA_SRC_MASK, 1) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="ae19ab9dccb4288c4c251bf8eb1f5a002"></a>

### `DMA_REQSEL_LDMAXBAR0PRSREQ1`

```c
#define DMA_REQSEL_LDMAXBAR0PRSREQ1 (FIELD_PREP(DMA_SRC_MASK, 1) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="a3b04d98c82d29396f8e688db8d5c5de9"></a>

### `DMA_REQSEL_NONE`

```c
#define DMA_REQSEL_NONE (FIELD_PREP(DMA_SRC_MASK, 0) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="a5c445181f71322b2554dbb25e780e18e"></a>

### `DMA_REQSEL_PIXELRZ0REQ_TXF`

```c
#define DMA_REQSEL_PIXELRZ0REQ_TXF (FIELD_PREP(DMA_SRC_MASK, 14) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="a4e870a3b8a8926a3d853b611487299e6"></a>

### `DMA_REQSEL_PIXELRZ1REQ_TXF`

```c
#define DMA_REQSEL_PIXELRZ1REQ_TXF (FIELD_PREP(DMA_SRC_MASK, 16) | FIELD_PREP(DMA_SIG_MASK, 0))
```

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
#define DMA_REQSEL_TIMER2CC0 (FIELD_PREP(DMA_SRC_MASK, 6) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="aed70ea120b2a199163c46f028aec4538"></a>

### `DMA_REQSEL_TIMER2CC1`

```c
#define DMA_REQSEL_TIMER2CC1 (FIELD_PREP(DMA_SRC_MASK, 6) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="aff76df3b43b1ce7ff7cf36dad62914b5"></a>

### `DMA_REQSEL_TIMER2CC2`

```c
#define DMA_REQSEL_TIMER2CC2 (FIELD_PREP(DMA_SRC_MASK, 6) | FIELD_PREP(DMA_SIG_MASK, 2))
```

<a id="a1381c6c857dc7d9c0f0078369fb63052"></a>

### `DMA_REQSEL_TIMER2CC3`

```c
#define DMA_REQSEL_TIMER2CC3 (FIELD_PREP(DMA_SRC_MASK, 6) | FIELD_PREP(DMA_SIG_MASK, 4))
```

<a id="ad5e5b9d61676e95c0865d9051574f46c"></a>

### `DMA_REQSEL_TIMER2CC4`

```c
#define DMA_REQSEL_TIMER2CC4 (FIELD_PREP(DMA_SRC_MASK, 6) | FIELD_PREP(DMA_SIG_MASK, 5))
```

<a id="a5e501f1be583a0f0b70167c3d75e7673"></a>

### `DMA_REQSEL_TIMER2CC5`

```c
#define DMA_REQSEL_TIMER2CC5 (FIELD_PREP(DMA_SRC_MASK, 6) | FIELD_PREP(DMA_SIG_MASK, 6))
```

<a id="abaf6c71d249d869af3507418f873bbe8"></a>

### `DMA_REQSEL_TIMER2CC6`

```c
#define DMA_REQSEL_TIMER2CC6 (FIELD_PREP(DMA_SRC_MASK, 6) | FIELD_PREP(DMA_SIG_MASK, 7))
```

<a id="a359eec69c4e20a62fda0382318777ca2"></a>

### `DMA_REQSEL_TIMER2UFOF`

```c
#define DMA_REQSEL_TIMER2UFOF (FIELD_PREP(DMA_SRC_MASK, 6) | FIELD_PREP(DMA_SIG_MASK, 3))
```

<a id="acd2b7ad92fa2c7fe11b0410760e431d0"></a>

### `DMA_REQSEL_TIMER3CC0`

```c
#define DMA_REQSEL_TIMER3CC0 (FIELD_PREP(DMA_SRC_MASK, 7) | FIELD_PREP(DMA_SIG_MASK, 0))
```

<a id="ac875ac8e9ee74e79df2e9a7e7f7d47bc"></a>

### `DMA_REQSEL_TIMER3CC1`

```c
#define DMA_REQSEL_TIMER3CC1 (FIELD_PREP(DMA_SRC_MASK, 7) | FIELD_PREP(DMA_SIG_MASK, 1))
```

<a id="a84068b2390c9db03e234e8ebf7dd844e"></a>

### `DMA_REQSEL_TIMER3CC2`

```c
#define DMA_REQSEL_TIMER3CC2 (FIELD_PREP(DMA_SRC_MASK, 7) | FIELD_PREP(DMA_SIG_MASK, 2))
```

<a id="adf86873e038d26d178cf3c1ccb22a4d4"></a>

### `DMA_REQSEL_TIMER3CC3`

```c
#define DMA_REQSEL_TIMER3CC3 (FIELD_PREP(DMA_SRC_MASK, 7) | FIELD_PREP(DMA_SIG_MASK, 4))
```

<a id="adad81e665fbfbc456b3f3744863cc6bc"></a>

### `DMA_REQSEL_TIMER3CC4`

```c
#define DMA_REQSEL_TIMER3CC4 (FIELD_PREP(DMA_SRC_MASK, 7) | FIELD_PREP(DMA_SIG_MASK, 5))
```

<a id="a3635d73b218da5379408924c679e6538"></a>

### `DMA_REQSEL_TIMER3CC5`

```c
#define DMA_REQSEL_TIMER3CC5 (FIELD_PREP(DMA_SRC_MASK, 7) | FIELD_PREP(DMA_SIG_MASK, 6))
```

<a id="a5a1164ef2515a577d28fdee53a0fc949"></a>

### `DMA_REQSEL_TIMER3CC6`

```c
#define DMA_REQSEL_TIMER3CC6 (FIELD_PREP(DMA_SRC_MASK, 7) | FIELD_PREP(DMA_SIG_MASK, 7))
```

<a id="a0b099b82ec5b12e2da5d9fcafeb6feb4"></a>

### `DMA_REQSEL_TIMER3UFOF`

```c
#define DMA_REQSEL_TIMER3UFOF (FIELD_PREP(DMA_SRC_MASK, 7) | FIELD_PREP(DMA_SIG_MASK, 3))
```


## 398.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P006_设备树绑定工具头文件源码.md)
- [common-dma.h](../api_source_reference/P110_common-dma.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P181_six301-dma.h_源码浏览.md)
- [FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)
- [DMA_SRC_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#a0e9e5febc44f1450a524ec73c9649d20)
- [DMA_SIG_MASK](P045_zephyr__dt-bindings__dma__silabs__common-dma.h_文件参考.md#afe1c8630fc69f691df9bdcfb8f4ebb67)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P397_zephyr__dt-bindings__clock__silabs__six301-clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P399_zephyr__dt-bindings__pinctrl__silabs__six301-pinctrl.h_文件参考.md)
