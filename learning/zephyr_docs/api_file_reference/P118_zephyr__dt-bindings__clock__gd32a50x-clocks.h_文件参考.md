---
id: learning.zephyr-docs.api-file-reference.page-118
title: zephyr__dt-bindings__clock__gd32a50x-clocks.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gd32a50x-clocks_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第118章\_zephyr\_\_dt-bindings\_\_clock\_\_gd32a50x-clocks.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gd32a50x-clocks_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include "gd32-clocks-common.h"
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 118.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 寄存器偏移量（Register offsets）

<a id="r_a510e385774abf879310b061273eb4068"></a>

```c
#define GD32_AHBEN_OFFSET 0x14U
```

相关声明：[GD32_AHBEN_OFFSET](#a510e385774abf879310b061273eb4068)。

<a id="r_a4b2aa082b4b2200b7f2b1663c30f205c"></a>

```c
#define GD32_APB1EN_OFFSET 0x1CU
```

相关声明：[GD32_APB1EN_OFFSET](#a4b2aa082b4b2200b7f2b1663c30f205c)。

<a id="r_a9d794746eea796b39b3ae55b1614d9d9"></a>

```c
#define GD32_APB2EN_OFFSET 0x18U
```

相关声明：[GD32_APB2EN_OFFSET](#a9d794746eea796b39b3ae55b1614d9d9)。

<a id="define-members-1"></a>

### 外设时钟使能/禁用定义（Clock enable/disable definitions for peripherals）

<a id="r_a7728f090fb52201d3d1162881b80dc3e"></a>

```c
#define GD32_CLOCK_DMA0 GD32_CLOCK_CONFIG(AHBEN, 0U)
```

相关声明：[GD32_CLOCK_DMA0](#a7728f090fb52201d3d1162881b80dc3e)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_af6c6eb89797f088a78722ce007ae47e5"></a>

```c
#define GD32_CLOCK_DMA1 GD32_CLOCK_CONFIG(AHBEN, 1U)
```

相关声明：[GD32_CLOCK_DMA1](#af6c6eb89797f088a78722ce007ae47e5)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a7f201b05f8c284e62be5bf9290a84a67"></a>

```c
#define GD32_CLOCK_SRAMSP GD32_CLOCK_CONFIG(AHBEN, 2U)
```

相关声明：[GD32_CLOCK_SRAMSP](#a7f201b05f8c284e62be5bf9290a84a67)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_aea9030f004dabd02eb16900856aa9af9"></a>

```c
#define GD32_CLOCK_DMAMUX GD32_CLOCK_CONFIG(AHBEN, 3U)
```

相关声明：[GD32_CLOCK_DMAMUX](#aea9030f004dabd02eb16900856aa9af9)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_acdbf40a9d897a38daca0d8bd5f81fc1a"></a>

```c
#define GD32_CLOCK_FMCSP GD32_CLOCK_CONFIG(AHBEN, 4U)
```

相关声明：[GD32_CLOCK_FMCSP](#acdbf40a9d897a38daca0d8bd5f81fc1a)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a0971986459094517a13221629cc89e95"></a>

```c
#define GD32_CLOCK_CRC GD32_CLOCK_CONFIG(AHBEN, 6U)
```

相关声明：[GD32_CLOCK_CRC](#a0971986459094517a13221629cc89e95)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_afdf4211f39bca3cd6b14ac7a6d9cd5a9"></a>

```c
#define GD32_CLOCK_MFCOM GD32_CLOCK_CONFIG(AHBEN, 14U)
```

相关声明：[GD32_CLOCK_MFCOM](#afdf4211f39bca3cd6b14ac7a6d9cd5a9)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a6d7de29e854deaa62412e302566efd23"></a>

```c
#define GD32_CLOCK_GPIOA GD32_CLOCK_CONFIG(AHBEN, 17U)
```

相关声明：[GD32_CLOCK_GPIOA](#a6d7de29e854deaa62412e302566efd23)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a4272044e59f7e6935b5fc231d7da4a3e"></a>

```c
#define GD32_CLOCK_GPIOB GD32_CLOCK_CONFIG(AHBEN, 18U)
```

相关声明：[GD32_CLOCK_GPIOB](#a4272044e59f7e6935b5fc231d7da4a3e)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a8a415ead74c233d769ac7649bbc678ee"></a>

```c
#define GD32_CLOCK_GPIOC GD32_CLOCK_CONFIG(AHBEN, 19U)
```

相关声明：[GD32_CLOCK_GPIOC](#a8a415ead74c233d769ac7649bbc678ee)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a6e674cc73448d4c7487fb05a9368a5b0"></a>

```c
#define GD32_CLOCK_GPIOD GD32_CLOCK_CONFIG(AHBEN, 20U)
```

相关声明：[GD32_CLOCK_GPIOD](#a6e674cc73448d4c7487fb05a9368a5b0)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a77e5bd38cfd6018f8a5e518b388e764d"></a>

```c
#define GD32_CLOCK_GPIOE GD32_CLOCK_CONFIG(AHBEN, 21U)
```

相关声明：[GD32_CLOCK_GPIOE](#a77e5bd38cfd6018f8a5e518b388e764d)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a8eaec3ec9ef667aaad9553f9a24fbbfe"></a>

```c
#define GD32_CLOCK_GPIOF GD32_CLOCK_CONFIG(AHBEN, 22U)
```

相关声明：[GD32_CLOCK_GPIOF](#a8eaec3ec9ef667aaad9553f9a24fbbfe)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_af084c2bf11ddfe04c80c3fac272c30e7"></a>

```c
#define GD32_CLOCK_TIMER1 GD32_CLOCK_CONFIG(APB1EN, 0U)
```

相关声明：[GD32_CLOCK_TIMER1](#af084c2bf11ddfe04c80c3fac272c30e7)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_aae8d2c65bc590e7147407099e8a938b7"></a>

```c
#define GD32_CLOCK_TIMER5 GD32_CLOCK_CONFIG(APB1EN, 4U)
```

相关声明：[GD32_CLOCK_TIMER5](#aae8d2c65bc590e7147407099e8a938b7)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a0e1b450d86f9e5b08a5738116742b429"></a>

```c
#define GD32_CLOCK_TIMER6 GD32_CLOCK_CONFIG(APB1EN, 5U)
```

相关声明：[GD32_CLOCK_TIMER6](#a0e1b450d86f9e5b08a5738116742b429)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_acd4e6949e5fb08e13129174ddd6f2e70"></a>

```c
#define GD32_CLOCK_WWDGT GD32_CLOCK_CONFIG(APB1EN, 11U)
```

相关声明：[GD32_CLOCK_WWDGT](#acd4e6949e5fb08e13129174ddd6f2e70)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a61a4d4edd729635d5fcdd200a13a0b9b"></a>

```c
#define GD32_CLOCK_SPI1 GD32_CLOCK_CONFIG(APB1EN, 14U)
```

相关声明：[GD32_CLOCK_SPI1](#a61a4d4edd729635d5fcdd200a13a0b9b)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a0f4528cfba6c9b129cc3aeae8220a178"></a>

```c
#define GD32_CLOCK_USART1 GD32_CLOCK_CONFIG(APB1EN, 17U)
```

相关声明：[GD32_CLOCK_USART1](#a0f4528cfba6c9b129cc3aeae8220a178)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a477baf1c1a265b4c86019a5f52820622"></a>

```c
#define GD32_CLOCK_USART2 GD32_CLOCK_CONFIG(APB1EN, 18U)
```

相关声明：[GD32_CLOCK_USART2](#a477baf1c1a265b4c86019a5f52820622)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a7aa5531ee97403c9ab9152c3fa9e4b47"></a>

```c
#define GD32_CLOCK_I2C0 GD32_CLOCK_CONFIG(APB1EN, 21U)
```

相关声明：[GD32_CLOCK_I2C0](#a7aa5531ee97403c9ab9152c3fa9e4b47)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a15d339475004b458aa5aa4a4a0692355"></a>

```c
#define GD32_CLOCK_I2C1 GD32_CLOCK_CONFIG(APB1EN, 22U)
```

相关声明：[GD32_CLOCK_I2C1](#a15d339475004b458aa5aa4a4a0692355)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a45f1e755993e4ccdda57966c147309dc"></a>

```c
#define GD32_CLOCK_BKP GD32_CLOCK_CONFIG(APB1EN, 26U)
```

相关声明：[GD32_CLOCK_BKP](#a45f1e755993e4ccdda57966c147309dc)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a58267ff23e872483b53ff7e6bb64d69f"></a>

```c
#define GD32_CLOCK_PMU GD32_CLOCK_CONFIG(APB1EN, 28U)
```

相关声明：[GD32_CLOCK_PMU](#a58267ff23e872483b53ff7e6bb64d69f)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_aaef5ffeb0d314adf6faf2a9d8158763b"></a>

```c
#define GD32_CLOCK_DAC GD32_CLOCK_CONFIG(APB1EN, 29U)
```

相关声明：[GD32_CLOCK_DAC](#aaef5ffeb0d314adf6faf2a9d8158763b)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a82d39e45cb7402ed96ab29953f8e131f"></a>

```c
#define GD32_CLOCK_SYSCFG GD32_CLOCK_CONFIG(APB2EN, 0U)
```

相关声明：[GD32_CLOCK_SYSCFG](#a82d39e45cb7402ed96ab29953f8e131f)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a86ba69950ab9daffa9c98d898a8b1186"></a>

```c
#define GD32_CLOCK_CMP GD32_CLOCK_CONFIG(APB2EN, 1U)
```

相关声明：[GD32_CLOCK_CMP](#a86ba69950ab9daffa9c98d898a8b1186)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a59b782811760bb907d00801305564c94"></a>

```c
#define GD32_CLOCK_ADC0 GD32_CLOCK_CONFIG(APB2EN, 9U)
```

相关声明：[GD32_CLOCK_ADC0](#a59b782811760bb907d00801305564c94)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a2ee53a1088b6dc17320d3d35ffdb1848"></a>

```c
#define GD32_CLOCK_ADC1 GD32_CLOCK_CONFIG(APB2EN, 10U)
```

相关声明：[GD32_CLOCK_ADC1](#a2ee53a1088b6dc17320d3d35ffdb1848)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_afa309eb7291fd4416d3a5d0184991212"></a>

```c
#define GD32_CLOCK_TIMER0 GD32_CLOCK_CONFIG(APB2EN, 11U)
```

相关声明：[GD32_CLOCK_TIMER0](#afa309eb7291fd4416d3a5d0184991212)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_aa1284de659aca3a7b279c4f691147fb7"></a>

```c
#define GD32_CLOCK_SPI0 GD32_CLOCK_CONFIG(APB2EN, 12U)
```

相关声明：[GD32_CLOCK_SPI0](#aa1284de659aca3a7b279c4f691147fb7)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_abb3f432fa2ef4e6c69a4c252493c0606"></a>

```c
#define GD32_CLOCK_TIMER7 GD32_CLOCK_CONFIG(APB2EN, 13U)
```

相关声明：[GD32_CLOCK_TIMER7](#abb3f432fa2ef4e6c69a4c252493c0606)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_ac1599e50ad14746470268bc14aa04318"></a>

```c
#define GD32_CLOCK_USART0 GD32_CLOCK_CONFIG(APB2EN, 14U)
```

相关声明：[GD32_CLOCK_USART0](#ac1599e50ad14746470268bc14aa04318)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_aee2b9b1293285875fe904aae8438eaa9"></a>

```c
#define GD32_CLOCK_TIMER19 GD32_CLOCK_CONFIG(APB2EN, 20U)
```

相关声明：[GD32_CLOCK_TIMER19](#aee2b9b1293285875fe904aae8438eaa9)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a3e2aebbea35b4c351a7b022cb854d09e"></a>

```c
#define GD32_CLOCK_TIMER20 GD32_CLOCK_CONFIG(APB2EN, 21U)
```

相关声明：[GD32_CLOCK_TIMER20](#a3e2aebbea35b4c351a7b022cb854d09e)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a0a9f433ec3cf8073a486d12936fab6ea"></a>

```c
#define GD32_CLOCK_TRIGSEL GD32_CLOCK_CONFIG(APB2EN, 29U)
```

相关声明：[GD32_CLOCK_TRIGSEL](#a0a9f433ec3cf8073a486d12936fab6ea)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a567dfd2f603a04594ab82aeac7339655"></a>

```c
#define GD32_CLOCK_CAN0 GD32_CLOCK_CONFIG(APB2EN, 30U)
```

相关声明：[GD32_CLOCK_CAN0](#a567dfd2f603a04594ab82aeac7339655)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a73858e2f6a1654e6114790c9dea80cd0"></a>

```c
#define GD32_CLOCK_CAN1 GD32_CLOCK_CONFIG(APB2EN, 31U)
```

相关声明：[GD32_CLOCK_CAN1](#a73858e2f6a1654e6114790c9dea80cd0)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

## 118.2\_详细说明（Detailed Documentation）

<a id="a510e385774abf879310b061273eb4068"></a>

### `GD32_AHBEN_OFFSET`

```c
#define GD32_AHBEN_OFFSET 0x14U
```

<a id="a4b2aa082b4b2200b7f2b1663c30f205c"></a>

### `GD32_APB1EN_OFFSET`

```c
#define GD32_APB1EN_OFFSET 0x1CU
```

<a id="a9d794746eea796b39b3ae55b1614d9d9"></a>

### `GD32_APB2EN_OFFSET`

```c
#define GD32_APB2EN_OFFSET 0x18U
```

<a id="a59b782811760bb907d00801305564c94"></a>

### `GD32_CLOCK_ADC0`

```c
#define GD32_CLOCK_ADC0 GD32_CLOCK_CONFIG(APB2EN, 9U)
```

<a id="a2ee53a1088b6dc17320d3d35ffdb1848"></a>

### `GD32_CLOCK_ADC1`

```c
#define GD32_CLOCK_ADC1 GD32_CLOCK_CONFIG(APB2EN, 10U)
```

<a id="a45f1e755993e4ccdda57966c147309dc"></a>

### `GD32_CLOCK_BKP`

```c
#define GD32_CLOCK_BKP GD32_CLOCK_CONFIG(APB1EN, 26U)
```

<a id="a567dfd2f603a04594ab82aeac7339655"></a>

### `GD32_CLOCK_CAN0`

```c
#define GD32_CLOCK_CAN0 GD32_CLOCK_CONFIG(APB2EN, 30U)
```

<a id="a73858e2f6a1654e6114790c9dea80cd0"></a>

### `GD32_CLOCK_CAN1`

```c
#define GD32_CLOCK_CAN1 GD32_CLOCK_CONFIG(APB2EN, 31U)
```

<a id="a86ba69950ab9daffa9c98d898a8b1186"></a>

### `GD32_CLOCK_CMP`

```c
#define GD32_CLOCK_CMP GD32_CLOCK_CONFIG(APB2EN, 1U)
```

<a id="a0971986459094517a13221629cc89e95"></a>

### `GD32_CLOCK_CRC`

```c
#define GD32_CLOCK_CRC GD32_CLOCK_CONFIG(AHBEN, 6U)
```

<a id="aaef5ffeb0d314adf6faf2a9d8158763b"></a>

### `GD32_CLOCK_DAC`

```c
#define GD32_CLOCK_DAC GD32_CLOCK_CONFIG(APB1EN, 29U)
```

<a id="a7728f090fb52201d3d1162881b80dc3e"></a>

### `GD32_CLOCK_DMA0`

```c
#define GD32_CLOCK_DMA0 GD32_CLOCK_CONFIG(AHBEN, 0U)
```

<a id="af6c6eb89797f088a78722ce007ae47e5"></a>

### `GD32_CLOCK_DMA1`

```c
#define GD32_CLOCK_DMA1 GD32_CLOCK_CONFIG(AHBEN, 1U)
```

<a id="aea9030f004dabd02eb16900856aa9af9"></a>

### `GD32_CLOCK_DMAMUX`

```c
#define GD32_CLOCK_DMAMUX GD32_CLOCK_CONFIG(AHBEN, 3U)
```

<a id="acdbf40a9d897a38daca0d8bd5f81fc1a"></a>

### `GD32_CLOCK_FMCSP`

```c
#define GD32_CLOCK_FMCSP GD32_CLOCK_CONFIG(AHBEN, 4U)
```

<a id="a6d7de29e854deaa62412e302566efd23"></a>

### `GD32_CLOCK_GPIOA`

```c
#define GD32_CLOCK_GPIOA GD32_CLOCK_CONFIG(AHBEN, 17U)
```

<a id="a4272044e59f7e6935b5fc231d7da4a3e"></a>

### `GD32_CLOCK_GPIOB`

```c
#define GD32_CLOCK_GPIOB GD32_CLOCK_CONFIG(AHBEN, 18U)
```

<a id="a8a415ead74c233d769ac7649bbc678ee"></a>

### `GD32_CLOCK_GPIOC`

```c
#define GD32_CLOCK_GPIOC GD32_CLOCK_CONFIG(AHBEN, 19U)
```

<a id="a6e674cc73448d4c7487fb05a9368a5b0"></a>

### `GD32_CLOCK_GPIOD`

```c
#define GD32_CLOCK_GPIOD GD32_CLOCK_CONFIG(AHBEN, 20U)
```

<a id="a77e5bd38cfd6018f8a5e518b388e764d"></a>

### `GD32_CLOCK_GPIOE`

```c
#define GD32_CLOCK_GPIOE GD32_CLOCK_CONFIG(AHBEN, 21U)
```

<a id="a8eaec3ec9ef667aaad9553f9a24fbbfe"></a>

### `GD32_CLOCK_GPIOF`

```c
#define GD32_CLOCK_GPIOF GD32_CLOCK_CONFIG(AHBEN, 22U)
```

<a id="a7aa5531ee97403c9ab9152c3fa9e4b47"></a>

### `GD32_CLOCK_I2C0`

```c
#define GD32_CLOCK_I2C0 GD32_CLOCK_CONFIG(APB1EN, 21U)
```

<a id="a15d339475004b458aa5aa4a4a0692355"></a>

### `GD32_CLOCK_I2C1`

```c
#define GD32_CLOCK_I2C1 GD32_CLOCK_CONFIG(APB1EN, 22U)
```

<a id="afdf4211f39bca3cd6b14ac7a6d9cd5a9"></a>

### `GD32_CLOCK_MFCOM`

```c
#define GD32_CLOCK_MFCOM GD32_CLOCK_CONFIG(AHBEN, 14U)
```

<a id="a58267ff23e872483b53ff7e6bb64d69f"></a>

### `GD32_CLOCK_PMU`

```c
#define GD32_CLOCK_PMU GD32_CLOCK_CONFIG(APB1EN, 28U)
```

<a id="aa1284de659aca3a7b279c4f691147fb7"></a>

### `GD32_CLOCK_SPI0`

```c
#define GD32_CLOCK_SPI0 GD32_CLOCK_CONFIG(APB2EN, 12U)
```

<a id="a61a4d4edd729635d5fcdd200a13a0b9b"></a>

### `GD32_CLOCK_SPI1`

```c
#define GD32_CLOCK_SPI1 GD32_CLOCK_CONFIG(APB1EN, 14U)
```

<a id="a7f201b05f8c284e62be5bf9290a84a67"></a>

### `GD32_CLOCK_SRAMSP`

```c
#define GD32_CLOCK_SRAMSP GD32_CLOCK_CONFIG(AHBEN, 2U)
```

<a id="a82d39e45cb7402ed96ab29953f8e131f"></a>

### `GD32_CLOCK_SYSCFG`

```c
#define GD32_CLOCK_SYSCFG GD32_CLOCK_CONFIG(APB2EN, 0U)
```

<a id="afa309eb7291fd4416d3a5d0184991212"></a>

### `GD32_CLOCK_TIMER0`

```c
#define GD32_CLOCK_TIMER0 GD32_CLOCK_CONFIG(APB2EN, 11U)
```

<a id="af084c2bf11ddfe04c80c3fac272c30e7"></a>

### `GD32_CLOCK_TIMER1`

```c
#define GD32_CLOCK_TIMER1 GD32_CLOCK_CONFIG(APB1EN, 0U)
```

<a id="aee2b9b1293285875fe904aae8438eaa9"></a>

### `GD32_CLOCK_TIMER19`

```c
#define GD32_CLOCK_TIMER19 GD32_CLOCK_CONFIG(APB2EN, 20U)
```

<a id="a3e2aebbea35b4c351a7b022cb854d09e"></a>

### `GD32_CLOCK_TIMER20`

```c
#define GD32_CLOCK_TIMER20 GD32_CLOCK_CONFIG(APB2EN, 21U)
```

<a id="aae8d2c65bc590e7147407099e8a938b7"></a>

### `GD32_CLOCK_TIMER5`

```c
#define GD32_CLOCK_TIMER5 GD32_CLOCK_CONFIG(APB1EN, 4U)
```

<a id="a0e1b450d86f9e5b08a5738116742b429"></a>

### `GD32_CLOCK_TIMER6`

```c
#define GD32_CLOCK_TIMER6 GD32_CLOCK_CONFIG(APB1EN, 5U)
```

<a id="abb3f432fa2ef4e6c69a4c252493c0606"></a>

### `GD32_CLOCK_TIMER7`

```c
#define GD32_CLOCK_TIMER7 GD32_CLOCK_CONFIG(APB2EN, 13U)
```

<a id="a0a9f433ec3cf8073a486d12936fab6ea"></a>

### `GD32_CLOCK_TRIGSEL`

```c
#define GD32_CLOCK_TRIGSEL GD32_CLOCK_CONFIG(APB2EN, 29U)
```

<a id="ac1599e50ad14746470268bc14aa04318"></a>

### `GD32_CLOCK_USART0`

```c
#define GD32_CLOCK_USART0 GD32_CLOCK_CONFIG(APB2EN, 14U)
```

<a id="a0f4528cfba6c9b129cc3aeae8220a178"></a>

### `GD32_CLOCK_USART1`

```c
#define GD32_CLOCK_USART1 GD32_CLOCK_CONFIG(APB1EN, 17U)
```

<a id="a477baf1c1a265b4c86019a5f52820622"></a>

### `GD32_CLOCK_USART2`

```c
#define GD32_CLOCK_USART2 GD32_CLOCK_CONFIG(APB1EN, 18U)
```

<a id="acd4e6949e5fb08e13129174ddd6f2e70"></a>

### `GD32_CLOCK_WWDGT`

```c
#define GD32_CLOCK_WWDGT GD32_CLOCK_CONFIG(APB1EN, 11U)
```


## 118.3\_原页交叉引用（Cross References）

- [gd32-clocks-common.h](../api_source_reference/P285_gd32-clocks-common.h_源码浏览.md)
- [查看此文件的源码。](../api_source_runtime_reference/P022_gd32a50x-clocks.h_源码浏览.md)
- [GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P117_zephyr__dt-bindings__dma__gd32_dma.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P119_zephyr__dt-bindings__reset__gd32a50x.h_文件参考.md)
