---
id: learning.zephyr-docs.api-file-clock-network-reference.page-11
title: zephyr__dt-bindings__clock__gd32c2x1-clocks.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gd32c2x1-clocks_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_zephyr\_\_dt-bindings\_\_clock\_\_gd32c2x1-clocks.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gd32c2x1-clocks_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于设备树绑定（Device Tree Bindings）的GD32C2X1时钟定义。

<a id="details"></a>

```c
#include "gd32-clocks-common.h"
```

查看此文件的源码。

用于设备树绑定（Device Tree Bindings）的GD32C2X1时钟定义。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 寄存器偏移量（Register offsets）

<a id="r_a339c9d51e00c124e8c3fcb3f60d4ab11"></a>

```c
#define GD32_AHB1EN_OFFSET 0x30U
```

相关声明：[GD32_AHB1EN_OFFSET](#a339c9d51e00c124e8c3fcb3f60d4ab11)。

AHB1 外设时钟使能寄存器偏移量（Peripheral Clock Enable Register Offset）。

<a id="r_a6e31d435e5f43b51f733ff72654e3028"></a>

```c
#define GD32_AHB2EN_OFFSET 0x34U
```

相关声明：[GD32_AHB2EN_OFFSET](#a6e31d435e5f43b51f733ff72654e3028)。

AHB2 外设时钟使能寄存器偏移量（Peripheral Clock Enable Register Offset）。

<a id="r_a808e10486d75c8980a59dc7d78c5e606"></a>

```c
#define GD32_APBEN_OFFSET 0x44U
```

相关声明：[GD32_APBEN_OFFSET](#a808e10486d75c8980a59dc7d78c5e606)。

APB 外设时钟使能寄存器偏移量（Peripheral Clock Enable Register Offset）。

<a id="define-members-1"></a>

### 外设时钟使能/禁用定义（Clock enable/disable definitions for peripherals）

<a id="r_a695eb7a95fa6b5d57b763629757bf1b1"></a>

```c
#define GD32_CLOCK_FMC GD32_CLOCK_CONFIG(AHB1EN, 4U)
```

相关声明：[GD32_CLOCK_FMC](#a695eb7a95fa6b5d57b763629757bf1b1)、[GD32_CLOCK_CONFIG](../api_file_management_reference/P019_zephyr__dt-bindings__clock__gd32-clocks-common.h_文件参考.md#a8b1e411caae3c88322d85671558b2bbc)。

FMC 时钟（Clock）。

<a id="r_a0971986459094517a13221629cc89e95"></a>

```c
#define GD32_CLOCK_CRC GD32_CLOCK_CONFIG(AHB1EN, 12U)
```

相关声明：[GD32_CLOCK_CRC](#a0971986459094517a13221629cc89e95)、[GD32_CLOCK_CONFIG](../api_file_management_reference/P019_zephyr__dt-bindings__clock__gd32-clocks-common.h_文件参考.md#a8b1e411caae3c88322d85671558b2bbc)。

CRC 时钟（Clock）。

<a id="r_aa4a3b682dbd3877c0e505f89ce572729"></a>

```c
#define GD32_CLOCK_DMA GD32_CLOCK_CONFIG(AHB1EN, 21U)
```

相关声明：[GD32_CLOCK_DMA](#aa4a3b682dbd3877c0e505f89ce572729)、[GD32_CLOCK_CONFIG](../api_file_management_reference/P019_zephyr__dt-bindings__clock__gd32-clocks-common.h_文件参考.md#a8b1e411caae3c88322d85671558b2bbc)。

DMA 时钟（Clock）。

<a id="r_aea9030f004dabd02eb16900856aa9af9"></a>

```c
#define GD32_CLOCK_DMAMUX GD32_CLOCK_CONFIG(AHB1EN, 23U)
```

相关声明：[GD32_CLOCK_DMAMUX](#aea9030f004dabd02eb16900856aa9af9)、[GD32_CLOCK_CONFIG](../api_file_management_reference/P019_zephyr__dt-bindings__clock__gd32-clocks-common.h_文件参考.md#a8b1e411caae3c88322d85671558b2bbc)。

DMAMUX 时钟（Clock）。

<a id="r_a6d7de29e854deaa62412e302566efd23"></a>

```c
#define GD32_CLOCK_GPIOA GD32_CLOCK_CONFIG(AHB2EN, 17U)
```

相关声明：[GD32_CLOCK_GPIOA](#a6d7de29e854deaa62412e302566efd23)、[GD32_CLOCK_CONFIG](../api_file_management_reference/P019_zephyr__dt-bindings__clock__gd32-clocks-common.h_文件参考.md#a8b1e411caae3c88322d85671558b2bbc)。

GPIOA 时钟（Clock）。

<a id="r_a4272044e59f7e6935b5fc231d7da4a3e"></a>

```c
#define GD32_CLOCK_GPIOB GD32_CLOCK_CONFIG(AHB2EN, 18U)
```

相关声明：[GD32_CLOCK_GPIOB](#a4272044e59f7e6935b5fc231d7da4a3e)、[GD32_CLOCK_CONFIG](../api_file_management_reference/P019_zephyr__dt-bindings__clock__gd32-clocks-common.h_文件参考.md#a8b1e411caae3c88322d85671558b2bbc)。

GPIOB 时钟（Clock）。

<a id="r_a8a415ead74c233d769ac7649bbc678ee"></a>

```c
#define GD32_CLOCK_GPIOC GD32_CLOCK_CONFIG(AHB2EN, 19U)
```

相关声明：[GD32_CLOCK_GPIOC](#a8a415ead74c233d769ac7649bbc678ee)、[GD32_CLOCK_CONFIG](../api_file_management_reference/P019_zephyr__dt-bindings__clock__gd32-clocks-common.h_文件参考.md#a8b1e411caae3c88322d85671558b2bbc)。

GPIOC 时钟（Clock）。

<a id="r_a6e674cc73448d4c7487fb05a9368a5b0"></a>

```c
#define GD32_CLOCK_GPIOD GD32_CLOCK_CONFIG(AHB2EN, 20U)
```

相关声明：[GD32_CLOCK_GPIOD](#a6e674cc73448d4c7487fb05a9368a5b0)、[GD32_CLOCK_CONFIG](../api_file_management_reference/P019_zephyr__dt-bindings__clock__gd32-clocks-common.h_文件参考.md#a8b1e411caae3c88322d85671558b2bbc)。

GPIOD 时钟（Clock）。

<a id="r_a8eaec3ec9ef667aaad9553f9a24fbbfe"></a>

```c
#define GD32_CLOCK_GPIOF GD32_CLOCK_CONFIG(AHB2EN, 22U)
```

相关声明：[GD32_CLOCK_GPIOF](#a8eaec3ec9ef667aaad9553f9a24fbbfe)、[GD32_CLOCK_CONFIG](../api_file_management_reference/P019_zephyr__dt-bindings__clock__gd32-clocks-common.h_文件参考.md#a8b1e411caae3c88322d85671558b2bbc)。

GPIOF 时钟（Clock）。

<a id="r_a82d39e45cb7402ed96ab29953f8e131f"></a>

```c
#define GD32_CLOCK_SYSCFG GD32_CLOCK_CONFIG(APBEN, 0U)
```

相关声明：[GD32_CLOCK_SYSCFG](#a82d39e45cb7402ed96ab29953f8e131f)、[GD32_CLOCK_CONFIG](../api_file_management_reference/P019_zephyr__dt-bindings__clock__gd32-clocks-common.h_文件参考.md#a8b1e411caae3c88322d85671558b2bbc)。

SYSCFG 时钟（Clock）。

<a id="r_a86ba69950ab9daffa9c98d898a8b1186"></a>

```c
#define GD32_CLOCK_CMP GD32_CLOCK_CONFIG(APBEN, 1U)
```

相关声明：[GD32_CLOCK_CMP](#a86ba69950ab9daffa9c98d898a8b1186)、[GD32_CLOCK_CONFIG](../api_file_management_reference/P019_zephyr__dt-bindings__clock__gd32-clocks-common.h_文件参考.md#a8b1e411caae3c88322d85671558b2bbc)。

比较器（Comparator） 时钟（Clock）。

<a id="r_acd4e6949e5fb08e13129174ddd6f2e70"></a>

```c
#define GD32_CLOCK_WWDGT GD32_CLOCK_CONFIG(APBEN, 8U)
```

相关声明：[GD32_CLOCK_WWDGT](#acd4e6949e5fb08e13129174ddd6f2e70)、[GD32_CLOCK_CONFIG](../api_file_management_reference/P019_zephyr__dt-bindings__clock__gd32-clocks-common.h_文件参考.md#a8b1e411caae3c88322d85671558b2bbc)。

窗口看门狗（Window Watchdog） 时钟（Clock）。

<a id="r_a49fb3dfb6cb0c66ed5ee81185896f2ab"></a>

```c
#define GD32_CLOCK_ADC GD32_CLOCK_CONFIG(APBEN, 9U)
```

相关声明：[GD32_CLOCK_ADC](#a49fb3dfb6cb0c66ed5ee81185896f2ab)、[GD32_CLOCK_CONFIG](../api_file_management_reference/P019_zephyr__dt-bindings__clock__gd32-clocks-common.h_文件参考.md#a8b1e411caae3c88322d85671558b2bbc)。

ADC 时钟（Clock）。

<a id="r_afa309eb7291fd4416d3a5d0184991212"></a>

```c
#define GD32_CLOCK_TIMER0 GD32_CLOCK_CONFIG(APBEN, 10U)
```

相关声明：[GD32_CLOCK_TIMER0](#afa309eb7291fd4416d3a5d0184991212)、[GD32_CLOCK_CONFIG](../api_file_management_reference/P019_zephyr__dt-bindings__clock__gd32-clocks-common.h_文件参考.md#a8b1e411caae3c88322d85671558b2bbc)。

TIMER0 时钟（Clock）。

<a id="r_a41623cb4499589163c0697a7a669ac25"></a>

```c
#define GD32_CLOCK_TIMER2 GD32_CLOCK_CONFIG(APBEN, 11U)
```

相关声明：[GD32_CLOCK_TIMER2](#a41623cb4499589163c0697a7a669ac25)、[GD32_CLOCK_CONFIG](../api_file_management_reference/P019_zephyr__dt-bindings__clock__gd32-clocks-common.h_文件参考.md#a8b1e411caae3c88322d85671558b2bbc)。

TIMER2 时钟（Clock）。

<a id="r_aa1284de659aca3a7b279c4f691147fb7"></a>

```c
#define GD32_CLOCK_SPI0 GD32_CLOCK_CONFIG(APBEN, 12U)
```

相关声明：[GD32_CLOCK_SPI0](#aa1284de659aca3a7b279c4f691147fb7)、[GD32_CLOCK_CONFIG](../api_file_management_reference/P019_zephyr__dt-bindings__clock__gd32-clocks-common.h_文件参考.md#a8b1e411caae3c88322d85671558b2bbc)。

SPI0 时钟（Clock）。

<a id="r_a61a4d4edd729635d5fcdd200a13a0b9b"></a>

```c
#define GD32_CLOCK_SPI1 GD32_CLOCK_CONFIG(APBEN, 13U)
```

相关声明：[GD32_CLOCK_SPI1](#a61a4d4edd729635d5fcdd200a13a0b9b)、[GD32_CLOCK_CONFIG](../api_file_management_reference/P019_zephyr__dt-bindings__clock__gd32-clocks-common.h_文件参考.md#a8b1e411caae3c88322d85671558b2bbc)。

SPI1 时钟（Clock）。

<a id="r_ac1599e50ad14746470268bc14aa04318"></a>

```c
#define GD32_CLOCK_USART0 GD32_CLOCK_CONFIG(APBEN, 14U)
```

相关声明：[GD32_CLOCK_USART0](#ac1599e50ad14746470268bc14aa04318)、[GD32_CLOCK_CONFIG](../api_file_management_reference/P019_zephyr__dt-bindings__clock__gd32-clocks-common.h_文件参考.md#a8b1e411caae3c88322d85671558b2bbc)。

USART0 时钟（Clock）。

<a id="r_a0f4528cfba6c9b129cc3aeae8220a178"></a>

```c
#define GD32_CLOCK_USART1 GD32_CLOCK_CONFIG(APBEN, 15U)
```

相关声明：[GD32_CLOCK_USART1](#a0f4528cfba6c9b129cc3aeae8220a178)、[GD32_CLOCK_CONFIG](../api_file_management_reference/P019_zephyr__dt-bindings__clock__gd32-clocks-common.h_文件参考.md#a8b1e411caae3c88322d85671558b2bbc)。

USART1 时钟（Clock）。

<a id="r_a60bfa7bc6aafc012fa45b395d4d22c00"></a>

```c
#define GD32_CLOCK_TIMER13 GD32_CLOCK_CONFIG(APBEN, 16U)
```

相关声明：[GD32_CLOCK_TIMER13](#a60bfa7bc6aafc012fa45b395d4d22c00)、[GD32_CLOCK_CONFIG](../api_file_management_reference/P019_zephyr__dt-bindings__clock__gd32-clocks-common.h_文件参考.md#a8b1e411caae3c88322d85671558b2bbc)。

TIMER13 时钟（Clock）。

<a id="r_a36e688b72edf92678346f5a6371b33dd"></a>

```c
#define GD32_CLOCK_TIMER15 GD32_CLOCK_CONFIG(APBEN, 17U)
```

相关声明：[GD32_CLOCK_TIMER15](#a36e688b72edf92678346f5a6371b33dd)、[GD32_CLOCK_CONFIG](../api_file_management_reference/P019_zephyr__dt-bindings__clock__gd32-clocks-common.h_文件参考.md#a8b1e411caae3c88322d85671558b2bbc)。

TIMER15 时钟（Clock）。

<a id="r_a3e6797f4cc3c3dd54a9fc3ca1088ec63"></a>

```c
#define GD32_CLOCK_TIMER16 GD32_CLOCK_CONFIG(APBEN, 18U)
```

相关声明：[GD32_CLOCK_TIMER16](#a3e6797f4cc3c3dd54a9fc3ca1088ec63)、[GD32_CLOCK_CONFIG](../api_file_management_reference/P019_zephyr__dt-bindings__clock__gd32-clocks-common.h_文件参考.md#a8b1e411caae3c88322d85671558b2bbc)。

TIMER16 时钟（Clock）。

<a id="r_a477baf1c1a265b4c86019a5f52820622"></a>

```c
#define GD32_CLOCK_USART2 GD32_CLOCK_CONFIG(APBEN, 19U)
```

相关声明：[GD32_CLOCK_USART2](#a477baf1c1a265b4c86019a5f52820622)、[GD32_CLOCK_CONFIG](../api_file_management_reference/P019_zephyr__dt-bindings__clock__gd32-clocks-common.h_文件参考.md#a8b1e411caae3c88322d85671558b2bbc)。

USART2 时钟（Clock）。

<a id="r_a7aa5531ee97403c9ab9152c3fa9e4b47"></a>

```c
#define GD32_CLOCK_I2C0 GD32_CLOCK_CONFIG(APBEN, 21U)
```

相关声明：[GD32_CLOCK_I2C0](#a7aa5531ee97403c9ab9152c3fa9e4b47)、[GD32_CLOCK_CONFIG](../api_file_management_reference/P019_zephyr__dt-bindings__clock__gd32-clocks-common.h_文件参考.md#a8b1e411caae3c88322d85671558b2bbc)。

I2C0 时钟（Clock）。

<a id="r_a15d339475004b458aa5aa4a4a0692355"></a>

```c
#define GD32_CLOCK_I2C1 GD32_CLOCK_CONFIG(APBEN, 22U)
```

相关声明：[GD32_CLOCK_I2C1](#a15d339475004b458aa5aa4a4a0692355)、[GD32_CLOCK_CONFIG](../api_file_management_reference/P019_zephyr__dt-bindings__clock__gd32-clocks-common.h_文件参考.md#a8b1e411caae3c88322d85671558b2bbc)。

I2C1 时钟（Clock）。

<a id="r_a9037888fc509ae5128c12ad6ed3a90e1"></a>

```c
#define GD32_CLOCK_DBG GD32_CLOCK_CONFIG(APBEN, 27U)
```

相关声明：[GD32_CLOCK_DBG](#a9037888fc509ae5128c12ad6ed3a90e1)、[GD32_CLOCK_CONFIG](../api_file_management_reference/P019_zephyr__dt-bindings__clock__gd32-clocks-common.h_文件参考.md#a8b1e411caae3c88322d85671558b2bbc)。

调试模块（Debug Module） 时钟（Clock）。

<a id="r_a58267ff23e872483b53ff7e6bb64d69f"></a>

```c
#define GD32_CLOCK_PMU GD32_CLOCK_CONFIG(APBEN, 28U)
```

相关声明：[GD32_CLOCK_PMU](#a58267ff23e872483b53ff7e6bb64d69f)、[GD32_CLOCK_CONFIG](../api_file_management_reference/P019_zephyr__dt-bindings__clock__gd32-clocks-common.h_文件参考.md#a8b1e411caae3c88322d85671558b2bbc)。

PMU 时钟（Clock）。

## 11.2\_详细说明（Detailed Documentation）

<a id="a339c9d51e00c124e8c3fcb3f60d4ab11"></a>

### `GD32_AHB1EN_OFFSET`

```c
#define GD32_AHB1EN_OFFSET 0x30U
```

AHB1 外设时钟使能寄存器偏移量（Peripheral Clock Enable Register Offset）。

<a id="a6e31d435e5f43b51f733ff72654e3028"></a>

### `GD32_AHB2EN_OFFSET`

```c
#define GD32_AHB2EN_OFFSET 0x34U
```

AHB2 外设时钟使能寄存器偏移量（Peripheral Clock Enable Register Offset）。

<a id="a808e10486d75c8980a59dc7d78c5e606"></a>

### `GD32_APBEN_OFFSET`

```c
#define GD32_APBEN_OFFSET 0x44U
```

APB 外设时钟使能寄存器偏移量（Peripheral Clock Enable Register Offset）。

<a id="a49fb3dfb6cb0c66ed5ee81185896f2ab"></a>

### `GD32_CLOCK_ADC`

```c
#define GD32_CLOCK_ADC GD32_CLOCK_CONFIG(APBEN, 9U)
```

ADC 时钟（Clock）。

<a id="a86ba69950ab9daffa9c98d898a8b1186"></a>

### `GD32_CLOCK_CMP`

```c
#define GD32_CLOCK_CMP GD32_CLOCK_CONFIG(APBEN, 1U)
```

比较器（Comparator） 时钟（Clock）。

<a id="a0971986459094517a13221629cc89e95"></a>

### `GD32_CLOCK_CRC`

```c
#define GD32_CLOCK_CRC GD32_CLOCK_CONFIG(AHB1EN, 12U)
```

CRC 时钟（Clock）。

<a id="a9037888fc509ae5128c12ad6ed3a90e1"></a>

### `GD32_CLOCK_DBG`

```c
#define GD32_CLOCK_DBG GD32_CLOCK_CONFIG(APBEN, 27U)
```

调试模块（Debug Module） 时钟（Clock）。

<a id="aa4a3b682dbd3877c0e505f89ce572729"></a>

### `GD32_CLOCK_DMA`

```c
#define GD32_CLOCK_DMA GD32_CLOCK_CONFIG(AHB1EN, 21U)
```

DMA 时钟（Clock）。

<a id="aea9030f004dabd02eb16900856aa9af9"></a>

### `GD32_CLOCK_DMAMUX`

```c
#define GD32_CLOCK_DMAMUX GD32_CLOCK_CONFIG(AHB1EN, 23U)
```

DMAMUX 时钟（Clock）。

<a id="a695eb7a95fa6b5d57b763629757bf1b1"></a>

### `GD32_CLOCK_FMC`

```c
#define GD32_CLOCK_FMC GD32_CLOCK_CONFIG(AHB1EN, 4U)
```

FMC 时钟（Clock）。

<a id="a6d7de29e854deaa62412e302566efd23"></a>

### `GD32_CLOCK_GPIOA`

```c
#define GD32_CLOCK_GPIOA GD32_CLOCK_CONFIG(AHB2EN, 17U)
```

GPIOA 时钟（Clock）。

<a id="a4272044e59f7e6935b5fc231d7da4a3e"></a>

### `GD32_CLOCK_GPIOB`

```c
#define GD32_CLOCK_GPIOB GD32_CLOCK_CONFIG(AHB2EN, 18U)
```

GPIOB 时钟（Clock）。

<a id="a8a415ead74c233d769ac7649bbc678ee"></a>

### `GD32_CLOCK_GPIOC`

```c
#define GD32_CLOCK_GPIOC GD32_CLOCK_CONFIG(AHB2EN, 19U)
```

GPIOC 时钟（Clock）。

<a id="a6e674cc73448d4c7487fb05a9368a5b0"></a>

### `GD32_CLOCK_GPIOD`

```c
#define GD32_CLOCK_GPIOD GD32_CLOCK_CONFIG(AHB2EN, 20U)
```

GPIOD 时钟（Clock）。

<a id="a8eaec3ec9ef667aaad9553f9a24fbbfe"></a>

### `GD32_CLOCK_GPIOF`

```c
#define GD32_CLOCK_GPIOF GD32_CLOCK_CONFIG(AHB2EN, 22U)
```

GPIOF 时钟（Clock）。

<a id="a7aa5531ee97403c9ab9152c3fa9e4b47"></a>

### `GD32_CLOCK_I2C0`

```c
#define GD32_CLOCK_I2C0 GD32_CLOCK_CONFIG(APBEN, 21U)
```

I2C0 时钟（Clock）。

<a id="a15d339475004b458aa5aa4a4a0692355"></a>

### `GD32_CLOCK_I2C1`

```c
#define GD32_CLOCK_I2C1 GD32_CLOCK_CONFIG(APBEN, 22U)
```

I2C1 时钟（Clock）。

<a id="a58267ff23e872483b53ff7e6bb64d69f"></a>

### `GD32_CLOCK_PMU`

```c
#define GD32_CLOCK_PMU GD32_CLOCK_CONFIG(APBEN, 28U)
```

PMU 时钟（Clock）。

<a id="aa1284de659aca3a7b279c4f691147fb7"></a>

### `GD32_CLOCK_SPI0`

```c
#define GD32_CLOCK_SPI0 GD32_CLOCK_CONFIG(APBEN, 12U)
```

SPI0 时钟（Clock）。

<a id="a61a4d4edd729635d5fcdd200a13a0b9b"></a>

### `GD32_CLOCK_SPI1`

```c
#define GD32_CLOCK_SPI1 GD32_CLOCK_CONFIG(APBEN, 13U)
```

SPI1 时钟（Clock）。

<a id="a82d39e45cb7402ed96ab29953f8e131f"></a>

### `GD32_CLOCK_SYSCFG`

```c
#define GD32_CLOCK_SYSCFG GD32_CLOCK_CONFIG(APBEN, 0U)
```

SYSCFG 时钟（Clock）。

<a id="afa309eb7291fd4416d3a5d0184991212"></a>

### `GD32_CLOCK_TIMER0`

```c
#define GD32_CLOCK_TIMER0 GD32_CLOCK_CONFIG(APBEN, 10U)
```

TIMER0 时钟（Clock）。

<a id="a60bfa7bc6aafc012fa45b395d4d22c00"></a>

### `GD32_CLOCK_TIMER13`

```c
#define GD32_CLOCK_TIMER13 GD32_CLOCK_CONFIG(APBEN, 16U)
```

TIMER13 时钟（Clock）。

<a id="a36e688b72edf92678346f5a6371b33dd"></a>

### `GD32_CLOCK_TIMER15`

```c
#define GD32_CLOCK_TIMER15 GD32_CLOCK_CONFIG(APBEN, 17U)
```

TIMER15 时钟（Clock）。

<a id="a3e6797f4cc3c3dd54a9fc3ca1088ec63"></a>

### `GD32_CLOCK_TIMER16`

```c
#define GD32_CLOCK_TIMER16 GD32_CLOCK_CONFIG(APBEN, 18U)
```

TIMER16 时钟（Clock）。

<a id="a41623cb4499589163c0697a7a669ac25"></a>

### `GD32_CLOCK_TIMER2`

```c
#define GD32_CLOCK_TIMER2 GD32_CLOCK_CONFIG(APBEN, 11U)
```

TIMER2 时钟（Clock）。

<a id="ac1599e50ad14746470268bc14aa04318"></a>

### `GD32_CLOCK_USART0`

```c
#define GD32_CLOCK_USART0 GD32_CLOCK_CONFIG(APBEN, 14U)
```

USART0 时钟（Clock）。

<a id="a0f4528cfba6c9b129cc3aeae8220a178"></a>

### `GD32_CLOCK_USART1`

```c
#define GD32_CLOCK_USART1 GD32_CLOCK_CONFIG(APBEN, 15U)
```

USART1 时钟（Clock）。

<a id="a477baf1c1a265b4c86019a5f52820622"></a>

### `GD32_CLOCK_USART2`

```c
#define GD32_CLOCK_USART2 GD32_CLOCK_CONFIG(APBEN, 19U)
```

USART2 时钟（Clock）。

<a id="acd4e6949e5fb08e13129174ddd6f2e70"></a>

### `GD32_CLOCK_WWDGT`

```c
#define GD32_CLOCK_WWDGT GD32_CLOCK_CONFIG(APBEN, 8U)
```

窗口看门狗（Window Watchdog） 时钟（Clock）。


## 11.3\_原页交叉引用（Cross References）

- [gd32-clocks-common.h](../api_source_reference/P285_gd32-clocks-common.h_源码浏览.md)
- [查看此文件的源码。](../api_source_runtime_reference/P024_gd32c2x1-clocks.h_源码浏览.md)
- [GD32_CLOCK_CONFIG](../api_file_management_reference/P019_zephyr__dt-bindings__clock__gd32-clocks-common.h_文件参考.md#a8b1e411caae3c88322d85671558b2bbc)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P010_zephyr__bluetooth__services__ets.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P012_zephyr__bluetooth__classic__hfp_ag.h_文件参考.md)
