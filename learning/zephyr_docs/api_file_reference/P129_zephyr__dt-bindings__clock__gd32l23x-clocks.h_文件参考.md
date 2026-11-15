---
id: learning.zephyr-docs.api-file-reference.page-129
title: zephyr__dt-bindings__clock__gd32l23x-clocks.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gd32l23x-clocks_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第129章\_zephyr\_\_dt-bindings\_\_clock\_\_gd32l23x-clocks.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gd32l23x-clocks_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include "gd32-clocks-common.h"
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 129.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 寄存器偏移量（Register offsets）

<a id="r_a339c9d51e00c124e8c3fcb3f60d4ab11"></a>

```c
#define GD32_AHB1EN_OFFSET 0x14U
```

相关声明：[GD32_AHB1EN_OFFSET](#a339c9d51e00c124e8c3fcb3f60d4ab11)。

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

<a id="r_aa4a3b682dbd3877c0e505f89ce572729"></a>

```c
#define GD32_CLOCK_DMA GD32_CLOCK_CONFIG(AHB1EN, 0U)
```

相关声明：[GD32_CLOCK_DMA](#aa4a3b682dbd3877c0e505f89ce572729)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_aa492c4ed7ca62ad488bd34a9c39f7ee7"></a>

```c
#define GD32_CLOCK_SRAM0 GD32_CLOCK_CONFIG(AHB1EN, 2U)
```

相关声明：[GD32_CLOCK_SRAM0](#aa492c4ed7ca62ad488bd34a9c39f7ee7)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a695eb7a95fa6b5d57b763629757bf1b1"></a>

```c
#define GD32_CLOCK_FMC GD32_CLOCK_CONFIG(AHB1EN, 4U)
```

相关声明：[GD32_CLOCK_FMC](#a695eb7a95fa6b5d57b763629757bf1b1)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a0971986459094517a13221629cc89e95"></a>

```c
#define GD32_CLOCK_CRC GD32_CLOCK_CONFIG(AHB1EN, 6U)
```

相关声明：[GD32_CLOCK_CRC](#a0971986459094517a13221629cc89e95)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_aa72ff0249d857ac302e3b247cc08d8c8"></a>

```c
#define GD32_CLOCK_SRAM1 GD32_CLOCK_CONFIG(AHB1EN, 7U)
```

相关声明：[GD32_CLOCK_SRAM1](#aa72ff0249d857ac302e3b247cc08d8c8)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a6d7de29e854deaa62412e302566efd23"></a>

```c
#define GD32_CLOCK_GPIOA GD32_CLOCK_CONFIG(AHB1EN, 17U)
```

相关声明：[GD32_CLOCK_GPIOA](#a6d7de29e854deaa62412e302566efd23)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a4272044e59f7e6935b5fc231d7da4a3e"></a>

```c
#define GD32_CLOCK_GPIOB GD32_CLOCK_CONFIG(AHB1EN, 18U)
```

相关声明：[GD32_CLOCK_GPIOB](#a4272044e59f7e6935b5fc231d7da4a3e)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a8a415ead74c233d769ac7649bbc678ee"></a>

```c
#define GD32_CLOCK_GPIOC GD32_CLOCK_CONFIG(AHB1EN, 19U)
```

相关声明：[GD32_CLOCK_GPIOC](#a8a415ead74c233d769ac7649bbc678ee)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a6e674cc73448d4c7487fb05a9368a5b0"></a>

```c
#define GD32_CLOCK_GPIOD GD32_CLOCK_CONFIG(AHB1EN, 20U)
```

相关声明：[GD32_CLOCK_GPIOD](#a6e674cc73448d4c7487fb05a9368a5b0)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a8eaec3ec9ef667aaad9553f9a24fbbfe"></a>

```c
#define GD32_CLOCK_GPIOF GD32_CLOCK_CONFIG(AHB1EN, 22U)
```

相关声明：[GD32_CLOCK_GPIOF](#a8eaec3ec9ef667aaad9553f9a24fbbfe)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a0654988b7208162ddcdf649167734784"></a>

```c
#define GD32_CLOCK_CAU GD32_CLOCK_CONFIG(AHB2EN, 1U)
```

相关声明：[GD32_CLOCK_CAU](#a0654988b7208162ddcdf649167734784)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_ad7e9e9d34e7acca03e2538e1d5f52c0e"></a>

```c
#define GD32_CLOCK_TRNG GD32_CLOCK_CONFIG(AHB2EN, 3U)
```

相关声明：[GD32_CLOCK_TRNG](#ad7e9e9d34e7acca03e2538e1d5f52c0e)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_af084c2bf11ddfe04c80c3fac272c30e7"></a>

```c
#define GD32_CLOCK_TIMER1 GD32_CLOCK_CONFIG(APB1EN, 0U)
```

相关声明：[GD32_CLOCK_TIMER1](#af084c2bf11ddfe04c80c3fac272c30e7)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a41623cb4499589163c0697a7a669ac25"></a>

```c
#define GD32_CLOCK_TIMER2 GD32_CLOCK_CONFIG(APB1EN, 1U)
```

相关声明：[GD32_CLOCK_TIMER2](#a41623cb4499589163c0697a7a669ac25)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

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

<a id="r_afffce8951164061ccedc46edad527cf8"></a>

```c
#define GD32_CLOCK_TIMER11 GD32_CLOCK_CONFIG(APB1EN, 8U)
```

相关声明：[GD32_CLOCK_TIMER11](#afffce8951164061ccedc46edad527cf8)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_af2dcccd27d498112f102c9148abb42f7"></a>

```c
#define GD32_CLOCK_LPTIMER GD32_CLOCK_CONFIG(APB1EN, 9U)
```

相关声明：[GD32_CLOCK_LPTIMER](#af2dcccd27d498112f102c9148abb42f7)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_ae41c4f96dae0097b82ff22932f90aefe"></a>

```c
#define GD32_CLOCK_SLCD GD32_CLOCK_CONFIG(APB1EN, 10U)
```

相关声明：[GD32_CLOCK_SLCD](#ae41c4f96dae0097b82ff22932f90aefe)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

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

<a id="r_a6bc2e3226c496d0c1f754dac515fe568"></a>

```c
#define GD32_CLOCK_LPUART GD32_CLOCK_CONFIG(APB1EN, 18U)
```

相关声明：[GD32_CLOCK_LPUART](#a6bc2e3226c496d0c1f754dac515fe568)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a149bc461b6b4f81cafe38f9c7f40c8cd"></a>

```c
#define GD32_CLOCK_UART3 GD32_CLOCK_CONFIG(APB1EN, 19U)
```

相关声明：[GD32_CLOCK_UART3](#a149bc461b6b4f81cafe38f9c7f40c8cd)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a82468e78744e139664daeb68f8f181da"></a>

```c
#define GD32_CLOCK_UART4 GD32_CLOCK_CONFIG(APB1EN, 20U)
```

相关声明：[GD32_CLOCK_UART4](#a82468e78744e139664daeb68f8f181da)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

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

<a id="r_a0e6ade78ea2b16517f960f4dd9de12f3"></a>

```c
#define GD32_CLOCK_USBD GD32_CLOCK_CONFIG(APB1EN, 23U)
```

相关声明：[GD32_CLOCK_USBD](#a0e6ade78ea2b16517f960f4dd9de12f3)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a9e36e327a61c6867c787d6648b8ec2ac"></a>

```c
#define GD32_CLOCK_I2C2 GD32_CLOCK_CONFIG(APB1EN, 24U)
```

相关声明：[GD32_CLOCK_I2C2](#a9e36e327a61c6867c787d6648b8ec2ac)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

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

<a id="r_a886d3e4e09c70277b45f6afd5ae77eae"></a>

```c
#define GD32_CLOCK_CTC GD32_CLOCK_CONFIG(APB1EN, 30U)
```

相关声明：[GD32_CLOCK_CTC](#a886d3e4e09c70277b45f6afd5ae77eae)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a45f1e755993e4ccdda57966c147309dc"></a>

```c
#define GD32_CLOCK_BKP GD32_CLOCK_CONFIG(APB1EN, 31U)
```

相关声明：[GD32_CLOCK_BKP](#a45f1e755993e4ccdda57966c147309dc)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

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

<a id="r_a49fb3dfb6cb0c66ed5ee81185896f2ab"></a>

```c
#define GD32_CLOCK_ADC GD32_CLOCK_CONFIG(APB2EN, 9U)
```

相关声明：[GD32_CLOCK_ADC](#a49fb3dfb6cb0c66ed5ee81185896f2ab)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_adbac39fc1c001fbb14036f08c81810ef"></a>

```c
#define GD32_CLOCK_TIMER8 GD32_CLOCK_CONFIG(APB2EN, 11U)
```

相关声明：[GD32_CLOCK_TIMER8](#adbac39fc1c001fbb14036f08c81810ef)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_aa1284de659aca3a7b279c4f691147fb7"></a>

```c
#define GD32_CLOCK_SPI0 GD32_CLOCK_CONFIG(APB2EN, 12U)
```

相关声明：[GD32_CLOCK_SPI0](#aa1284de659aca3a7b279c4f691147fb7)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_ac1599e50ad14746470268bc14aa04318"></a>

```c
#define GD32_CLOCK_USART0 GD32_CLOCK_CONFIG(APB2EN, 14U)
```

相关声明：[GD32_CLOCK_USART0](#ac1599e50ad14746470268bc14aa04318)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a8d82d9131757c46462c8d983a919b94b"></a>

```c
#define GD32_CLOCK_DBGMCU GD32_CLOCK_CONFIG(APB2EN, 22U)
```

相关声明：[GD32_CLOCK_DBGMCU](#a8d82d9131757c46462c8d983a919b94b)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

## 129.2\_详细说明（Detailed Documentation）

<a id="a339c9d51e00c124e8c3fcb3f60d4ab11"></a>

### `GD32_AHB1EN_OFFSET`

```c
#define GD32_AHB1EN_OFFSET 0x14U
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

<a id="a49fb3dfb6cb0c66ed5ee81185896f2ab"></a>

### `GD32_CLOCK_ADC`

```c
#define GD32_CLOCK_ADC GD32_CLOCK_CONFIG(APB2EN, 9U)
```

<a id="a45f1e755993e4ccdda57966c147309dc"></a>

### `GD32_CLOCK_BKP`

```c
#define GD32_CLOCK_BKP GD32_CLOCK_CONFIG(APB1EN, 31U)
```

<a id="a0654988b7208162ddcdf649167734784"></a>

### `GD32_CLOCK_CAU`

```c
#define GD32_CLOCK_CAU GD32_CLOCK_CONFIG(AHB2EN, 1U)
```

<a id="a86ba69950ab9daffa9c98d898a8b1186"></a>

### `GD32_CLOCK_CMP`

```c
#define GD32_CLOCK_CMP GD32_CLOCK_CONFIG(APB2EN, 1U)
```

<a id="a0971986459094517a13221629cc89e95"></a>

### `GD32_CLOCK_CRC`

```c
#define GD32_CLOCK_CRC GD32_CLOCK_CONFIG(AHB1EN, 6U)
```

<a id="a886d3e4e09c70277b45f6afd5ae77eae"></a>

### `GD32_CLOCK_CTC`

```c
#define GD32_CLOCK_CTC GD32_CLOCK_CONFIG(APB1EN, 30U)
```

<a id="aaef5ffeb0d314adf6faf2a9d8158763b"></a>

### `GD32_CLOCK_DAC`

```c
#define GD32_CLOCK_DAC GD32_CLOCK_CONFIG(APB1EN, 29U)
```

<a id="a8d82d9131757c46462c8d983a919b94b"></a>

### `GD32_CLOCK_DBGMCU`

```c
#define GD32_CLOCK_DBGMCU GD32_CLOCK_CONFIG(APB2EN, 22U)
```

<a id="aa4a3b682dbd3877c0e505f89ce572729"></a>

### `GD32_CLOCK_DMA`

```c
#define GD32_CLOCK_DMA GD32_CLOCK_CONFIG(AHB1EN, 0U)
```

<a id="a695eb7a95fa6b5d57b763629757bf1b1"></a>

### `GD32_CLOCK_FMC`

```c
#define GD32_CLOCK_FMC GD32_CLOCK_CONFIG(AHB1EN, 4U)
```

<a id="a6d7de29e854deaa62412e302566efd23"></a>

### `GD32_CLOCK_GPIOA`

```c
#define GD32_CLOCK_GPIOA GD32_CLOCK_CONFIG(AHB1EN, 17U)
```

<a id="a4272044e59f7e6935b5fc231d7da4a3e"></a>

### `GD32_CLOCK_GPIOB`

```c
#define GD32_CLOCK_GPIOB GD32_CLOCK_CONFIG(AHB1EN, 18U)
```

<a id="a8a415ead74c233d769ac7649bbc678ee"></a>

### `GD32_CLOCK_GPIOC`

```c
#define GD32_CLOCK_GPIOC GD32_CLOCK_CONFIG(AHB1EN, 19U)
```

<a id="a6e674cc73448d4c7487fb05a9368a5b0"></a>

### `GD32_CLOCK_GPIOD`

```c
#define GD32_CLOCK_GPIOD GD32_CLOCK_CONFIG(AHB1EN, 20U)
```

<a id="a8eaec3ec9ef667aaad9553f9a24fbbfe"></a>

### `GD32_CLOCK_GPIOF`

```c
#define GD32_CLOCK_GPIOF GD32_CLOCK_CONFIG(AHB1EN, 22U)
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

<a id="a9e36e327a61c6867c787d6648b8ec2ac"></a>

### `GD32_CLOCK_I2C2`

```c
#define GD32_CLOCK_I2C2 GD32_CLOCK_CONFIG(APB1EN, 24U)
```

<a id="af2dcccd27d498112f102c9148abb42f7"></a>

### `GD32_CLOCK_LPTIMER`

```c
#define GD32_CLOCK_LPTIMER GD32_CLOCK_CONFIG(APB1EN, 9U)
```

<a id="a6bc2e3226c496d0c1f754dac515fe568"></a>

### `GD32_CLOCK_LPUART`

```c
#define GD32_CLOCK_LPUART GD32_CLOCK_CONFIG(APB1EN, 18U)
```

<a id="a58267ff23e872483b53ff7e6bb64d69f"></a>

### `GD32_CLOCK_PMU`

```c
#define GD32_CLOCK_PMU GD32_CLOCK_CONFIG(APB1EN, 28U)
```

<a id="ae41c4f96dae0097b82ff22932f90aefe"></a>

### `GD32_CLOCK_SLCD`

```c
#define GD32_CLOCK_SLCD GD32_CLOCK_CONFIG(APB1EN, 10U)
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

<a id="aa492c4ed7ca62ad488bd34a9c39f7ee7"></a>

### `GD32_CLOCK_SRAM0`

```c
#define GD32_CLOCK_SRAM0 GD32_CLOCK_CONFIG(AHB1EN, 2U)
```

<a id="aa72ff0249d857ac302e3b247cc08d8c8"></a>

### `GD32_CLOCK_SRAM1`

```c
#define GD32_CLOCK_SRAM1 GD32_CLOCK_CONFIG(AHB1EN, 7U)
```

<a id="a82d39e45cb7402ed96ab29953f8e131f"></a>

### `GD32_CLOCK_SYSCFG`

```c
#define GD32_CLOCK_SYSCFG GD32_CLOCK_CONFIG(APB2EN, 0U)
```

<a id="af084c2bf11ddfe04c80c3fac272c30e7"></a>

### `GD32_CLOCK_TIMER1`

```c
#define GD32_CLOCK_TIMER1 GD32_CLOCK_CONFIG(APB1EN, 0U)
```

<a id="afffce8951164061ccedc46edad527cf8"></a>

### `GD32_CLOCK_TIMER11`

```c
#define GD32_CLOCK_TIMER11 GD32_CLOCK_CONFIG(APB1EN, 8U)
```

<a id="a41623cb4499589163c0697a7a669ac25"></a>

### `GD32_CLOCK_TIMER2`

```c
#define GD32_CLOCK_TIMER2 GD32_CLOCK_CONFIG(APB1EN, 1U)
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

<a id="adbac39fc1c001fbb14036f08c81810ef"></a>

### `GD32_CLOCK_TIMER8`

```c
#define GD32_CLOCK_TIMER8 GD32_CLOCK_CONFIG(APB2EN, 11U)
```

<a id="ad7e9e9d34e7acca03e2538e1d5f52c0e"></a>

### `GD32_CLOCK_TRNG`

```c
#define GD32_CLOCK_TRNG GD32_CLOCK_CONFIG(AHB2EN, 3U)
```

<a id="a149bc461b6b4f81cafe38f9c7f40c8cd"></a>

### `GD32_CLOCK_UART3`

```c
#define GD32_CLOCK_UART3 GD32_CLOCK_CONFIG(APB1EN, 19U)
```

<a id="a82468e78744e139664daeb68f8f181da"></a>

### `GD32_CLOCK_UART4`

```c
#define GD32_CLOCK_UART4 GD32_CLOCK_CONFIG(APB1EN, 20U)
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

<a id="a0e6ade78ea2b16517f960f4dd9de12f3"></a>

### `GD32_CLOCK_USBD`

```c
#define GD32_CLOCK_USBD GD32_CLOCK_CONFIG(APB1EN, 23U)
```

<a id="acd4e6949e5fb08e13129174ddd6f2e70"></a>

### `GD32_CLOCK_WWDGT`

```c
#define GD32_CLOCK_WWDGT GD32_CLOCK_CONFIG(APB1EN, 11U)
```


## 129.3\_原页交叉引用（Cross References）

- [gd32-clocks-common.h](../api_source_reference/P285_gd32-clocks-common.h_源码浏览.md)
- [查看此文件的源码。](../api_source_runtime_reference/P026_gd32l23x-clocks.h_源码浏览.md)
- [GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P128_zephyr__dt-bindings__reset__gd32f4xx.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P130_zephyr__dt-bindings__reset__gd32l23x.h_文件参考.md)
