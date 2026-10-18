---
id: learning.zephyr-docs.api-file-reference.page-124
title: zephyr__dt-bindings__clock__gd32f3x0-clocks.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gd32f3x0-clocks_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第124章\_zephyr\_\_dt-bindings\_\_clock\_\_gd32f3x0-clocks.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gd32f3x0-clocks_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include "gd32-clocks-common.h"
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 124.1\_宏定义（Macros）

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

<a id="r_a4202c14a67ad78724b05175ede3aaa99"></a>

```c
#define GD32_ADDAPB1EN_OFFSET 0xF8U
```

相关声明：[GD32_ADDAPB1EN_OFFSET](#a4202c14a67ad78724b05175ede3aaa99)。

<a id="define-members-1"></a>

### 外设时钟使能/禁用定义（Clock enable/disable definitions for peripherals）

<a id="r_aa4a3b682dbd3877c0e505f89ce572729"></a>

```c
#define GD32_CLOCK_DMA GD32_CLOCK_CONFIG(AHBEN, 0U)
```

相关声明：[GD32_CLOCK_DMA](#aa4a3b682dbd3877c0e505f89ce572729)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a7f201b05f8c284e62be5bf9290a84a67"></a>

```c
#define GD32_CLOCK_SRAMSP GD32_CLOCK_CONFIG(AHBEN, 2U)
```

相关声明：[GD32_CLOCK_SRAMSP](#a7f201b05f8c284e62be5bf9290a84a67)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

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

<a id="r_ae11c1f5ccf256d32377eb9a6f07026f2"></a>

```c
#define GD32_CLOCK_USBFS GD32_CLOCK_CONFIG(AHBEN, 12U)
```

相关声明：[GD32_CLOCK_USBFS](#ae11c1f5ccf256d32377eb9a6f07026f2)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

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

<a id="r_a8eaec3ec9ef667aaad9553f9a24fbbfe"></a>

```c
#define GD32_CLOCK_GPIOF GD32_CLOCK_CONFIG(AHBEN, 22U)
```

相关声明：[GD32_CLOCK_GPIOF](#a8eaec3ec9ef667aaad9553f9a24fbbfe)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a2d044ca898ee3b1909c1de4411c139c2"></a>

```c
#define GD32_CLOCK_TSI GD32_CLOCK_CONFIG(AHBEN, 24U)
```

相关声明：[GD32_CLOCK_TSI](#a2d044ca898ee3b1909c1de4411c139c2)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

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

<a id="r_a60bfa7bc6aafc012fa45b395d4d22c00"></a>

```c
#define GD32_CLOCK_TIMER13 GD32_CLOCK_CONFIG(APB1EN, 8U)
```

相关声明：[GD32_CLOCK_TIMER13](#a60bfa7bc6aafc012fa45b395d4d22c00)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

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

<a id="r_a8f2a7136ffb5e7065bc28bd4782ab696"></a>

```c
#define GD32_CLOCK_CEC GD32_CLOCK_CONFIG(APB1EN, 30U)
```

相关声明：[GD32_CLOCK_CEC](#a8f2a7136ffb5e7065bc28bd4782ab696)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a795715aba6d275407e6237b06cb6e6df"></a>

```c
#define GD32_CLOCK_CFGCMP GD32_CLOCK_CONFIG(APB2EN, 0U)
```

相关声明：[GD32_CLOCK_CFGCMP](#a795715aba6d275407e6237b06cb6e6df)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a49fb3dfb6cb0c66ed5ee81185896f2ab"></a>

```c
#define GD32_CLOCK_ADC GD32_CLOCK_CONFIG(APB2EN, 9U)
```

相关声明：[GD32_CLOCK_ADC](#a49fb3dfb6cb0c66ed5ee81185896f2ab)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

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

<a id="r_ac1599e50ad14746470268bc14aa04318"></a>

```c
#define GD32_CLOCK_USART0 GD32_CLOCK_CONFIG(APB2EN, 14U)
```

相关声明：[GD32_CLOCK_USART0](#ac1599e50ad14746470268bc14aa04318)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_aa7ef737a5e522950f2ed231e987c208d"></a>

```c
#define GD32_CLOCK_TIMER14 GD32_CLOCK_CONFIG(APB2EN, 16U)
```

相关声明：[GD32_CLOCK_TIMER14](#aa7ef737a5e522950f2ed231e987c208d)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a36e688b72edf92678346f5a6371b33dd"></a>

```c
#define GD32_CLOCK_TIMER15 GD32_CLOCK_CONFIG(APB2EN, 17U)
```

相关声明：[GD32_CLOCK_TIMER15](#a36e688b72edf92678346f5a6371b33dd)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a3e6797f4cc3c3dd54a9fc3ca1088ec63"></a>

```c
#define GD32_CLOCK_TIMER16 GD32_CLOCK_CONFIG(APB2EN, 18U)
```

相关声明：[GD32_CLOCK_TIMER16](#a3e6797f4cc3c3dd54a9fc3ca1088ec63)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a886d3e4e09c70277b45f6afd5ae77eae"></a>

```c
#define GD32_CLOCK_CTC GD32_CLOCK_CONFIG(ADDAPB1EN, 27U)
```

相关声明：[GD32_CLOCK_CTC](#a886d3e4e09c70277b45f6afd5ae77eae)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

## 124.2\_详细说明（Detailed Documentation）

<a id="a4202c14a67ad78724b05175ede3aaa99"></a>

### `GD32_ADDAPB1EN_OFFSET`

```c
#define GD32_ADDAPB1EN_OFFSET 0xF8U
```

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

<a id="a49fb3dfb6cb0c66ed5ee81185896f2ab"></a>

### `GD32_CLOCK_ADC`

```c
#define GD32_CLOCK_ADC GD32_CLOCK_CONFIG(APB2EN, 9U)
```

<a id="a8f2a7136ffb5e7065bc28bd4782ab696"></a>

### `GD32_CLOCK_CEC`

```c
#define GD32_CLOCK_CEC GD32_CLOCK_CONFIG(APB1EN, 30U)
```

<a id="a795715aba6d275407e6237b06cb6e6df"></a>

### `GD32_CLOCK_CFGCMP`

```c
#define GD32_CLOCK_CFGCMP GD32_CLOCK_CONFIG(APB2EN, 0U)
```

<a id="a0971986459094517a13221629cc89e95"></a>

### `GD32_CLOCK_CRC`

```c
#define GD32_CLOCK_CRC GD32_CLOCK_CONFIG(AHBEN, 6U)
```

<a id="a886d3e4e09c70277b45f6afd5ae77eae"></a>

### `GD32_CLOCK_CTC`

```c
#define GD32_CLOCK_CTC GD32_CLOCK_CONFIG(ADDAPB1EN, 27U)
```

<a id="aaef5ffeb0d314adf6faf2a9d8158763b"></a>

### `GD32_CLOCK_DAC`

```c
#define GD32_CLOCK_DAC GD32_CLOCK_CONFIG(APB1EN, 29U)
```

<a id="aa4a3b682dbd3877c0e505f89ce572729"></a>

### `GD32_CLOCK_DMA`

```c
#define GD32_CLOCK_DMA GD32_CLOCK_CONFIG(AHBEN, 0U)
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

<a id="a60bfa7bc6aafc012fa45b395d4d22c00"></a>

### `GD32_CLOCK_TIMER13`

```c
#define GD32_CLOCK_TIMER13 GD32_CLOCK_CONFIG(APB1EN, 8U)
```

<a id="aa7ef737a5e522950f2ed231e987c208d"></a>

### `GD32_CLOCK_TIMER14`

```c
#define GD32_CLOCK_TIMER14 GD32_CLOCK_CONFIG(APB2EN, 16U)
```

<a id="a36e688b72edf92678346f5a6371b33dd"></a>

### `GD32_CLOCK_TIMER15`

```c
#define GD32_CLOCK_TIMER15 GD32_CLOCK_CONFIG(APB2EN, 17U)
```

<a id="a3e6797f4cc3c3dd54a9fc3ca1088ec63"></a>

### `GD32_CLOCK_TIMER16`

```c
#define GD32_CLOCK_TIMER16 GD32_CLOCK_CONFIG(APB2EN, 18U)
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

<a id="a2d044ca898ee3b1909c1de4411c139c2"></a>

### `GD32_CLOCK_TSI`

```c
#define GD32_CLOCK_TSI GD32_CLOCK_CONFIG(AHBEN, 24U)
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

<a id="ae11c1f5ccf256d32377eb9a6f07026f2"></a>

### `GD32_CLOCK_USBFS`

```c
#define GD32_CLOCK_USBFS GD32_CLOCK_CONFIG(AHBEN, 12U)
```

<a id="acd4e6949e5fb08e13129174ddd6f2e70"></a>

### `GD32_CLOCK_WWDGT`

```c
#define GD32_CLOCK_WWDGT GD32_CLOCK_CONFIG(APB1EN, 11U)
```


## 124.3\_原页交叉引用（Cross References）

- [gd32-clocks-common.h](../api_source_reference/P285_gd32-clocks-common.h_源码浏览.md)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/gd32f3x0-clocks_8h_source.html)
- [GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P123_zephyr__dt-bindings__reset__gd32e50x.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P125_zephyr__dt-bindings__clock__gd32f403-clocks.h_文件参考.md)
