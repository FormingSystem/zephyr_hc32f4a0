---
id: learning.zephyr-docs.api-file-reference.page-127
title: zephyr__dt-bindings__clock__gd32f4xx-clocks.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gd32f4xx-clocks_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第127章\_zephyr\_\_dt-bindings\_\_clock\_\_gd32f4xx-clocks.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gd32f4xx-clocks_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include "gd32-clocks-common.h"
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 127.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 寄存器偏移量（Register offsets）

<a id="r_a339c9d51e00c124e8c3fcb3f60d4ab11"></a>

```c
#define GD32_AHB1EN_OFFSET 0x30U
```

相关声明：[GD32_AHB1EN_OFFSET](#a339c9d51e00c124e8c3fcb3f60d4ab11)。

<a id="r_a6e31d435e5f43b51f733ff72654e3028"></a>

```c
#define GD32_AHB2EN_OFFSET 0x34U
```

相关声明：[GD32_AHB2EN_OFFSET](#a6e31d435e5f43b51f733ff72654e3028)。

<a id="r_a124c1f305697766c2e616b4102469a08"></a>

```c
#define GD32_AHB3EN_OFFSET 0x38U
```

相关声明：[GD32_AHB3EN_OFFSET](#a124c1f305697766c2e616b4102469a08)。

<a id="r_a4b2aa082b4b2200b7f2b1663c30f205c"></a>

```c
#define GD32_APB1EN_OFFSET 0x40U
```

相关声明：[GD32_APB1EN_OFFSET](#a4b2aa082b4b2200b7f2b1663c30f205c)。

<a id="r_a9d794746eea796b39b3ae55b1614d9d9"></a>

```c
#define GD32_APB2EN_OFFSET 0x44U
```

相关声明：[GD32_APB2EN_OFFSET](#a9d794746eea796b39b3ae55b1614d9d9)。

<a id="r_a4202c14a67ad78724b05175ede3aaa99"></a>

```c
#define GD32_ADDAPB1EN_OFFSET 0xE4U
```

相关声明：[GD32_ADDAPB1EN_OFFSET](#a4202c14a67ad78724b05175ede3aaa99)。

<a id="define-members-1"></a>

### 外设时钟使能/禁用定义（Clock enable/disable definitions for peripherals）

<a id="r_a6d7de29e854deaa62412e302566efd23"></a>

```c
#define GD32_CLOCK_GPIOA GD32_CLOCK_CONFIG(AHB1EN, 0U)
```

相关声明：[GD32_CLOCK_GPIOA](#a6d7de29e854deaa62412e302566efd23)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a4272044e59f7e6935b5fc231d7da4a3e"></a>

```c
#define GD32_CLOCK_GPIOB GD32_CLOCK_CONFIG(AHB1EN, 1U)
```

相关声明：[GD32_CLOCK_GPIOB](#a4272044e59f7e6935b5fc231d7da4a3e)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a8a415ead74c233d769ac7649bbc678ee"></a>

```c
#define GD32_CLOCK_GPIOC GD32_CLOCK_CONFIG(AHB1EN, 2U)
```

相关声明：[GD32_CLOCK_GPIOC](#a8a415ead74c233d769ac7649bbc678ee)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a6e674cc73448d4c7487fb05a9368a5b0"></a>

```c
#define GD32_CLOCK_GPIOD GD32_CLOCK_CONFIG(AHB1EN, 3U)
```

相关声明：[GD32_CLOCK_GPIOD](#a6e674cc73448d4c7487fb05a9368a5b0)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a77e5bd38cfd6018f8a5e518b388e764d"></a>

```c
#define GD32_CLOCK_GPIOE GD32_CLOCK_CONFIG(AHB1EN, 4U)
```

相关声明：[GD32_CLOCK_GPIOE](#a77e5bd38cfd6018f8a5e518b388e764d)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a8eaec3ec9ef667aaad9553f9a24fbbfe"></a>

```c
#define GD32_CLOCK_GPIOF GD32_CLOCK_CONFIG(AHB1EN, 5U)
```

相关声明：[GD32_CLOCK_GPIOF](#a8eaec3ec9ef667aaad9553f9a24fbbfe)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a2f91cac90de074a5478c73392c107027"></a>

```c
#define GD32_CLOCK_GPIOG GD32_CLOCK_CONFIG(AHB1EN, 6U)
```

相关声明：[GD32_CLOCK_GPIOG](#a2f91cac90de074a5478c73392c107027)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_aa61dad33dbaa553cdaff7c5e6d674758"></a>

```c
#define GD32_CLOCK_GPIOH GD32_CLOCK_CONFIG(AHB1EN, 7U)
```

相关声明：[GD32_CLOCK_GPIOH](#aa61dad33dbaa553cdaff7c5e6d674758)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_ac48646b69241ec518c12f5c92c982a4e"></a>

```c
#define GD32_CLOCK_GPIOI GD32_CLOCK_CONFIG(AHB1EN, 8U)
```

相关声明：[GD32_CLOCK_GPIOI](#ac48646b69241ec518c12f5c92c982a4e)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a0971986459094517a13221629cc89e95"></a>

```c
#define GD32_CLOCK_CRC GD32_CLOCK_CONFIG(AHB1EN, 12U)
```

相关声明：[GD32_CLOCK_CRC](#a0971986459094517a13221629cc89e95)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a07ab9ef3cb3d81f90c7363712725b55a"></a>

```c
#define GD32_CLOCK_BKPSRAM GD32_CLOCK_CONFIG(AHB1EN, 18U)
```

相关声明：[GD32_CLOCK_BKPSRAM](#a07ab9ef3cb3d81f90c7363712725b55a)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a035e6888de8ffcd4793928015996cebf"></a>

```c
#define GD32_CLOCK_TCMSRAM GD32_CLOCK_CONFIG(AHB1EN, 20U)
```

相关声明：[GD32_CLOCK_TCMSRAM](#a035e6888de8ffcd4793928015996cebf)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a7728f090fb52201d3d1162881b80dc3e"></a>

```c
#define GD32_CLOCK_DMA0 GD32_CLOCK_CONFIG(AHB1EN, 21U)
```

相关声明：[GD32_CLOCK_DMA0](#a7728f090fb52201d3d1162881b80dc3e)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_af6c6eb89797f088a78722ce007ae47e5"></a>

```c
#define GD32_CLOCK_DMA1 GD32_CLOCK_CONFIG(AHB1EN, 22U)
```

相关声明：[GD32_CLOCK_DMA1](#af6c6eb89797f088a78722ce007ae47e5)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_ad37a43a7c3bafef7f5af454d9311607e"></a>

```c
#define GD32_CLOCK_IPA GD32_CLOCK_CONFIG(AHB1EN, 23U)
```

相关声明：[GD32_CLOCK_IPA](#ad37a43a7c3bafef7f5af454d9311607e)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a824f638811c4469fedc65a1e29aac8d0"></a>

```c
#define GD32_CLOCK_ENET GD32_CLOCK_CONFIG(AHB1EN, 25U)
```

相关声明：[GD32_CLOCK_ENET](#a824f638811c4469fedc65a1e29aac8d0)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a6b14717b0c1cf864f1fe63b8ca42a439"></a>

```c
#define GD32_CLOCK_ENETTX GD32_CLOCK_CONFIG(AHB1EN, 26U)
```

相关声明：[GD32_CLOCK_ENETTX](#a6b14717b0c1cf864f1fe63b8ca42a439)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a05dce9f9343146d02a71a50b1f9416f7"></a>

```c
#define GD32_CLOCK_ENETRX GD32_CLOCK_CONFIG(AHB1EN, 27U)
```

相关声明：[GD32_CLOCK_ENETRX](#a05dce9f9343146d02a71a50b1f9416f7)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_afb7f99d35b7c726a99a7da0d1288697c"></a>

```c
#define GD32_CLOCK_ENETPTP GD32_CLOCK_CONFIG(AHB1EN, 28U)
```

相关声明：[GD32_CLOCK_ENETPTP](#afb7f99d35b7c726a99a7da0d1288697c)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a9bb9a4af2877fa954bda83bb8fbc39a6"></a>

```c
#define GD32_CLOCK_USBHS GD32_CLOCK_CONFIG(AHB1EN, 29U)
```

相关声明：[GD32_CLOCK_USBHS](#a9bb9a4af2877fa954bda83bb8fbc39a6)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a921ac30c07db5ab957c001cc0cbbdd0d"></a>

```c
#define GD32_CLOCK_USBHSULPI GD32_CLOCK_CONFIG(AHB1EN, 30U)
```

相关声明：[GD32_CLOCK_USBHSULPI](#a921ac30c07db5ab957c001cc0cbbdd0d)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a992085b45325f4ece017ca26d754b217"></a>

```c
#define GD32_CLOCK_DCI GD32_CLOCK_CONFIG(AHB2EN, 0U)
```

相关声明：[GD32_CLOCK_DCI](#a992085b45325f4ece017ca26d754b217)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_ad7e9e9d34e7acca03e2538e1d5f52c0e"></a>

```c
#define GD32_CLOCK_TRNG GD32_CLOCK_CONFIG(AHB2EN, 6U)
```

相关声明：[GD32_CLOCK_TRNG](#ad7e9e9d34e7acca03e2538e1d5f52c0e)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_ae11c1f5ccf256d32377eb9a6f07026f2"></a>

```c
#define GD32_CLOCK_USBFS GD32_CLOCK_CONFIG(AHB2EN, 7U)
```

相关声明：[GD32_CLOCK_USBFS](#ae11c1f5ccf256d32377eb9a6f07026f2)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_af4ca0b77d98d8825493b868d19d7759a"></a>

```c
#define GD32_CLOCK_EXMC GD32_CLOCK_CONFIG(AHB3EN, 0U)
```

相关声明：[GD32_CLOCK_EXMC](#af4ca0b77d98d8825493b868d19d7759a)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

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

<a id="r_afb5aa7f1705febd51a92f9370bd03d14"></a>

```c
#define GD32_CLOCK_TIMER3 GD32_CLOCK_CONFIG(APB1EN, 2U)
```

相关声明：[GD32_CLOCK_TIMER3](#afb5aa7f1705febd51a92f9370bd03d14)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a9d52a01572ab9309c5ebd3a0def8542f"></a>

```c
#define GD32_CLOCK_TIMER4 GD32_CLOCK_CONFIG(APB1EN, 3U)
```

相关声明：[GD32_CLOCK_TIMER4](#a9d52a01572ab9309c5ebd3a0def8542f)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

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
#define GD32_CLOCK_TIMER11 GD32_CLOCK_CONFIG(APB1EN, 6U)
```

相关声明：[GD32_CLOCK_TIMER11](#afffce8951164061ccedc46edad527cf8)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a285a372dc49a8df0888813b08c8804ef"></a>

```c
#define GD32_CLOCK_TIMER12 GD32_CLOCK_CONFIG(APB1EN, 7U)
```

相关声明：[GD32_CLOCK_TIMER12](#a285a372dc49a8df0888813b08c8804ef)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

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

<a id="r_a4bb28caf86a54e343c75a597b0bddc20"></a>

```c
#define GD32_CLOCK_SPI2 GD32_CLOCK_CONFIG(APB1EN, 15U)
```

相关声明：[GD32_CLOCK_SPI2](#a4bb28caf86a54e343c75a597b0bddc20)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

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

<a id="r_a9e36e327a61c6867c787d6648b8ec2ac"></a>

```c
#define GD32_CLOCK_I2C2 GD32_CLOCK_CONFIG(APB1EN, 23U)
```

相关声明：[GD32_CLOCK_I2C2](#a9e36e327a61c6867c787d6648b8ec2ac)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a567dfd2f603a04594ab82aeac7339655"></a>

```c
#define GD32_CLOCK_CAN0 GD32_CLOCK_CONFIG(APB1EN, 25U)
```

相关声明：[GD32_CLOCK_CAN0](#a567dfd2f603a04594ab82aeac7339655)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a73858e2f6a1654e6114790c9dea80cd0"></a>

```c
#define GD32_CLOCK_CAN1 GD32_CLOCK_CONFIG(APB1EN, 26U)
```

相关声明：[GD32_CLOCK_CAN1](#a73858e2f6a1654e6114790c9dea80cd0)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

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

<a id="r_a8ec6e1dfab01b3652183c38eac160288"></a>

```c
#define GD32_CLOCK_UART6 GD32_CLOCK_CONFIG(APB1EN, 30U)
```

相关声明：[GD32_CLOCK_UART6](#a8ec6e1dfab01b3652183c38eac160288)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a683cb88b874a2b6802bba5f99b85163e"></a>

```c
#define GD32_CLOCK_UART7 GD32_CLOCK_CONFIG(APB1EN, 31U)
```

相关声明：[GD32_CLOCK_UART7](#a683cb88b874a2b6802bba5f99b85163e)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a1f8cfe3ba991c9773b21c1e417bd3421"></a>

```c
#define GD32_CLOCK_RTC GD32_CLOCK_CONFIG(BDCTL, 15U)
```

相关声明：[GD32_CLOCK_RTC](#a1f8cfe3ba991c9773b21c1e417bd3421)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_afa309eb7291fd4416d3a5d0184991212"></a>

```c
#define GD32_CLOCK_TIMER0 GD32_CLOCK_CONFIG(APB2EN, 0U)
```

相关声明：[GD32_CLOCK_TIMER0](#afa309eb7291fd4416d3a5d0184991212)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_abb3f432fa2ef4e6c69a4c252493c0606"></a>

```c
#define GD32_CLOCK_TIMER7 GD32_CLOCK_CONFIG(APB2EN, 1U)
```

相关声明：[GD32_CLOCK_TIMER7](#abb3f432fa2ef4e6c69a4c252493c0606)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_ac1599e50ad14746470268bc14aa04318"></a>

```c
#define GD32_CLOCK_USART0 GD32_CLOCK_CONFIG(APB2EN, 4U)
```

相关声明：[GD32_CLOCK_USART0](#ac1599e50ad14746470268bc14aa04318)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a736a4d8ae51d88226f8baeec49be4dc5"></a>

```c
#define GD32_CLOCK_USART5 GD32_CLOCK_CONFIG(APB2EN, 5U)
```

相关声明：[GD32_CLOCK_USART5](#a736a4d8ae51d88226f8baeec49be4dc5)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a59b782811760bb907d00801305564c94"></a>

```c
#define GD32_CLOCK_ADC0 GD32_CLOCK_CONFIG(APB2EN, 8U)
```

相关声明：[GD32_CLOCK_ADC0](#a59b782811760bb907d00801305564c94)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a2ee53a1088b6dc17320d3d35ffdb1848"></a>

```c
#define GD32_CLOCK_ADC1 GD32_CLOCK_CONFIG(APB2EN, 9U)
```

相关声明：[GD32_CLOCK_ADC1](#a2ee53a1088b6dc17320d3d35ffdb1848)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a5710e96c011ed3c8dc90f63b842751cc"></a>

```c
#define GD32_CLOCK_ADC2 GD32_CLOCK_CONFIG(APB2EN, 10U)
```

相关声明：[GD32_CLOCK_ADC2](#a5710e96c011ed3c8dc90f63b842751cc)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_ad1ba647a10df2ea0bd81676cb5f46064"></a>

```c
#define GD32_CLOCK_SDIO GD32_CLOCK_CONFIG(APB2EN, 11U)
```

相关声明：[GD32_CLOCK_SDIO](#ad1ba647a10df2ea0bd81676cb5f46064)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_aa1284de659aca3a7b279c4f691147fb7"></a>

```c
#define GD32_CLOCK_SPI0 GD32_CLOCK_CONFIG(APB2EN, 12U)
```

相关声明：[GD32_CLOCK_SPI0](#aa1284de659aca3a7b279c4f691147fb7)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_adc1fc8ab68a58bc412e4560cdd56c25e"></a>

```c
#define GD32_CLOCK_SPI3 GD32_CLOCK_CONFIG(APB2EN, 13U)
```

相关声明：[GD32_CLOCK_SPI3](#adc1fc8ab68a58bc412e4560cdd56c25e)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a82d39e45cb7402ed96ab29953f8e131f"></a>

```c
#define GD32_CLOCK_SYSCFG GD32_CLOCK_CONFIG(APB2EN, 14U)
```

相关声明：[GD32_CLOCK_SYSCFG](#a82d39e45cb7402ed96ab29953f8e131f)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_adbac39fc1c001fbb14036f08c81810ef"></a>

```c
#define GD32_CLOCK_TIMER8 GD32_CLOCK_CONFIG(APB2EN, 16U)
```

相关声明：[GD32_CLOCK_TIMER8](#adbac39fc1c001fbb14036f08c81810ef)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a3981da513ef2eb351b403f6dc11a2c6b"></a>

```c
#define GD32_CLOCK_TIMER9 GD32_CLOCK_CONFIG(APB2EN, 17U)
```

相关声明：[GD32_CLOCK_TIMER9](#a3981da513ef2eb351b403f6dc11a2c6b)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a7c3b4d23aac8844faac79f458cc5e07b"></a>

```c
#define GD32_CLOCK_TIMER10 GD32_CLOCK_CONFIG(APB2EN, 18U)
```

相关声明：[GD32_CLOCK_TIMER10](#a7c3b4d23aac8844faac79f458cc5e07b)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a0fa21a935cec395aab91ba0394572d2c"></a>

```c
#define GD32_CLOCK_SPI4 GD32_CLOCK_CONFIG(APB2EN, 20U)
```

相关声明：[GD32_CLOCK_SPI4](#a0fa21a935cec395aab91ba0394572d2c)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_adfe3187c5b24e430f5071e1855a51108"></a>

```c
#define GD32_CLOCK_SPI5 GD32_CLOCK_CONFIG(APB2EN, 21U)
```

相关声明：[GD32_CLOCK_SPI5](#adfe3187c5b24e430f5071e1855a51108)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_ab04cbf84abb9f4923b6e9381c22bdae1"></a>

```c
#define GD32_CLOCK_TLI GD32_CLOCK_CONFIG(APB2EN, 26U)
```

相关声明：[GD32_CLOCK_TLI](#ab04cbf84abb9f4923b6e9381c22bdae1)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_a886d3e4e09c70277b45f6afd5ae77eae"></a>

```c
#define GD32_CLOCK_CTC GD32_CLOCK_CONFIG(ADDAPB1EN, 27U)
```

相关声明：[GD32_CLOCK_CTC](#a886d3e4e09c70277b45f6afd5ae77eae)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

<a id="r_ab2207ccb1c350c57aa19963285bf5470"></a>

```c
#define GD32_CLOCK_IREF GD32_CLOCK_CONFIG(ADDAPB1EN, 31U)
```

相关声明：[GD32_CLOCK_IREF](#ab2207ccb1c350c57aa19963285bf5470)、[GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)。

## 127.2\_详细说明（Detailed Documentation）

<a id="a4202c14a67ad78724b05175ede3aaa99"></a>

### `GD32_ADDAPB1EN_OFFSET`

```c
#define GD32_ADDAPB1EN_OFFSET 0xE4U
```

<a id="a339c9d51e00c124e8c3fcb3f60d4ab11"></a>

### `GD32_AHB1EN_OFFSET`

```c
#define GD32_AHB1EN_OFFSET 0x30U
```

<a id="a6e31d435e5f43b51f733ff72654e3028"></a>

### `GD32_AHB2EN_OFFSET`

```c
#define GD32_AHB2EN_OFFSET 0x34U
```

<a id="a124c1f305697766c2e616b4102469a08"></a>

### `GD32_AHB3EN_OFFSET`

```c
#define GD32_AHB3EN_OFFSET 0x38U
```

<a id="a4b2aa082b4b2200b7f2b1663c30f205c"></a>

### `GD32_APB1EN_OFFSET`

```c
#define GD32_APB1EN_OFFSET 0x40U
```

<a id="a9d794746eea796b39b3ae55b1614d9d9"></a>

### `GD32_APB2EN_OFFSET`

```c
#define GD32_APB2EN_OFFSET 0x44U
```

<a id="a59b782811760bb907d00801305564c94"></a>

### `GD32_CLOCK_ADC0`

```c
#define GD32_CLOCK_ADC0 GD32_CLOCK_CONFIG(APB2EN, 8U)
```

<a id="a2ee53a1088b6dc17320d3d35ffdb1848"></a>

### `GD32_CLOCK_ADC1`

```c
#define GD32_CLOCK_ADC1 GD32_CLOCK_CONFIG(APB2EN, 9U)
```

<a id="a5710e96c011ed3c8dc90f63b842751cc"></a>

### `GD32_CLOCK_ADC2`

```c
#define GD32_CLOCK_ADC2 GD32_CLOCK_CONFIG(APB2EN, 10U)
```

<a id="a07ab9ef3cb3d81f90c7363712725b55a"></a>

### `GD32_CLOCK_BKPSRAM`

```c
#define GD32_CLOCK_BKPSRAM GD32_CLOCK_CONFIG(AHB1EN, 18U)
```

<a id="a567dfd2f603a04594ab82aeac7339655"></a>

### `GD32_CLOCK_CAN0`

```c
#define GD32_CLOCK_CAN0 GD32_CLOCK_CONFIG(APB1EN, 25U)
```

<a id="a73858e2f6a1654e6114790c9dea80cd0"></a>

### `GD32_CLOCK_CAN1`

```c
#define GD32_CLOCK_CAN1 GD32_CLOCK_CONFIG(APB1EN, 26U)
```

<a id="a0971986459094517a13221629cc89e95"></a>

### `GD32_CLOCK_CRC`

```c
#define GD32_CLOCK_CRC GD32_CLOCK_CONFIG(AHB1EN, 12U)
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

<a id="a992085b45325f4ece017ca26d754b217"></a>

### `GD32_CLOCK_DCI`

```c
#define GD32_CLOCK_DCI GD32_CLOCK_CONFIG(AHB2EN, 0U)
```

<a id="a7728f090fb52201d3d1162881b80dc3e"></a>

### `GD32_CLOCK_DMA0`

```c
#define GD32_CLOCK_DMA0 GD32_CLOCK_CONFIG(AHB1EN, 21U)
```

<a id="af6c6eb89797f088a78722ce007ae47e5"></a>

### `GD32_CLOCK_DMA1`

```c
#define GD32_CLOCK_DMA1 GD32_CLOCK_CONFIG(AHB1EN, 22U)
```

<a id="a824f638811c4469fedc65a1e29aac8d0"></a>

### `GD32_CLOCK_ENET`

```c
#define GD32_CLOCK_ENET GD32_CLOCK_CONFIG(AHB1EN, 25U)
```

<a id="afb7f99d35b7c726a99a7da0d1288697c"></a>

### `GD32_CLOCK_ENETPTP`

```c
#define GD32_CLOCK_ENETPTP GD32_CLOCK_CONFIG(AHB1EN, 28U)
```

<a id="a05dce9f9343146d02a71a50b1f9416f7"></a>

### `GD32_CLOCK_ENETRX`

```c
#define GD32_CLOCK_ENETRX GD32_CLOCK_CONFIG(AHB1EN, 27U)
```

<a id="a6b14717b0c1cf864f1fe63b8ca42a439"></a>

### `GD32_CLOCK_ENETTX`

```c
#define GD32_CLOCK_ENETTX GD32_CLOCK_CONFIG(AHB1EN, 26U)
```

<a id="af4ca0b77d98d8825493b868d19d7759a"></a>

### `GD32_CLOCK_EXMC`

```c
#define GD32_CLOCK_EXMC GD32_CLOCK_CONFIG(AHB3EN, 0U)
```

<a id="a6d7de29e854deaa62412e302566efd23"></a>

### `GD32_CLOCK_GPIOA`

```c
#define GD32_CLOCK_GPIOA GD32_CLOCK_CONFIG(AHB1EN, 0U)
```

<a id="a4272044e59f7e6935b5fc231d7da4a3e"></a>

### `GD32_CLOCK_GPIOB`

```c
#define GD32_CLOCK_GPIOB GD32_CLOCK_CONFIG(AHB1EN, 1U)
```

<a id="a8a415ead74c233d769ac7649bbc678ee"></a>

### `GD32_CLOCK_GPIOC`

```c
#define GD32_CLOCK_GPIOC GD32_CLOCK_CONFIG(AHB1EN, 2U)
```

<a id="a6e674cc73448d4c7487fb05a9368a5b0"></a>

### `GD32_CLOCK_GPIOD`

```c
#define GD32_CLOCK_GPIOD GD32_CLOCK_CONFIG(AHB1EN, 3U)
```

<a id="a77e5bd38cfd6018f8a5e518b388e764d"></a>

### `GD32_CLOCK_GPIOE`

```c
#define GD32_CLOCK_GPIOE GD32_CLOCK_CONFIG(AHB1EN, 4U)
```

<a id="a8eaec3ec9ef667aaad9553f9a24fbbfe"></a>

### `GD32_CLOCK_GPIOF`

```c
#define GD32_CLOCK_GPIOF GD32_CLOCK_CONFIG(AHB1EN, 5U)
```

<a id="a2f91cac90de074a5478c73392c107027"></a>

### `GD32_CLOCK_GPIOG`

```c
#define GD32_CLOCK_GPIOG GD32_CLOCK_CONFIG(AHB1EN, 6U)
```

<a id="aa61dad33dbaa553cdaff7c5e6d674758"></a>

### `GD32_CLOCK_GPIOH`

```c
#define GD32_CLOCK_GPIOH GD32_CLOCK_CONFIG(AHB1EN, 7U)
```

<a id="ac48646b69241ec518c12f5c92c982a4e"></a>

### `GD32_CLOCK_GPIOI`

```c
#define GD32_CLOCK_GPIOI GD32_CLOCK_CONFIG(AHB1EN, 8U)
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
#define GD32_CLOCK_I2C2 GD32_CLOCK_CONFIG(APB1EN, 23U)
```

<a id="ad37a43a7c3bafef7f5af454d9311607e"></a>

### `GD32_CLOCK_IPA`

```c
#define GD32_CLOCK_IPA GD32_CLOCK_CONFIG(AHB1EN, 23U)
```

<a id="ab2207ccb1c350c57aa19963285bf5470"></a>

### `GD32_CLOCK_IREF`

```c
#define GD32_CLOCK_IREF GD32_CLOCK_CONFIG(ADDAPB1EN, 31U)
```

<a id="a58267ff23e872483b53ff7e6bb64d69f"></a>

### `GD32_CLOCK_PMU`

```c
#define GD32_CLOCK_PMU GD32_CLOCK_CONFIG(APB1EN, 28U)
```

<a id="a1f8cfe3ba991c9773b21c1e417bd3421"></a>

### `GD32_CLOCK_RTC`

```c
#define GD32_CLOCK_RTC GD32_CLOCK_CONFIG(BDCTL, 15U)
```

<a id="ad1ba647a10df2ea0bd81676cb5f46064"></a>

### `GD32_CLOCK_SDIO`

```c
#define GD32_CLOCK_SDIO GD32_CLOCK_CONFIG(APB2EN, 11U)
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

<a id="a4bb28caf86a54e343c75a597b0bddc20"></a>

### `GD32_CLOCK_SPI2`

```c
#define GD32_CLOCK_SPI2 GD32_CLOCK_CONFIG(APB1EN, 15U)
```

<a id="adc1fc8ab68a58bc412e4560cdd56c25e"></a>

### `GD32_CLOCK_SPI3`

```c
#define GD32_CLOCK_SPI3 GD32_CLOCK_CONFIG(APB2EN, 13U)
```

<a id="a0fa21a935cec395aab91ba0394572d2c"></a>

### `GD32_CLOCK_SPI4`

```c
#define GD32_CLOCK_SPI4 GD32_CLOCK_CONFIG(APB2EN, 20U)
```

<a id="adfe3187c5b24e430f5071e1855a51108"></a>

### `GD32_CLOCK_SPI5`

```c
#define GD32_CLOCK_SPI5 GD32_CLOCK_CONFIG(APB2EN, 21U)
```

<a id="a82d39e45cb7402ed96ab29953f8e131f"></a>

### `GD32_CLOCK_SYSCFG`

```c
#define GD32_CLOCK_SYSCFG GD32_CLOCK_CONFIG(APB2EN, 14U)
```

<a id="a035e6888de8ffcd4793928015996cebf"></a>

### `GD32_CLOCK_TCMSRAM`

```c
#define GD32_CLOCK_TCMSRAM GD32_CLOCK_CONFIG(AHB1EN, 20U)
```

<a id="afa309eb7291fd4416d3a5d0184991212"></a>

### `GD32_CLOCK_TIMER0`

```c
#define GD32_CLOCK_TIMER0 GD32_CLOCK_CONFIG(APB2EN, 0U)
```

<a id="af084c2bf11ddfe04c80c3fac272c30e7"></a>

### `GD32_CLOCK_TIMER1`

```c
#define GD32_CLOCK_TIMER1 GD32_CLOCK_CONFIG(APB1EN, 0U)
```

<a id="a7c3b4d23aac8844faac79f458cc5e07b"></a>

### `GD32_CLOCK_TIMER10`

```c
#define GD32_CLOCK_TIMER10 GD32_CLOCK_CONFIG(APB2EN, 18U)
```

<a id="afffce8951164061ccedc46edad527cf8"></a>

### `GD32_CLOCK_TIMER11`

```c
#define GD32_CLOCK_TIMER11 GD32_CLOCK_CONFIG(APB1EN, 6U)
```

<a id="a285a372dc49a8df0888813b08c8804ef"></a>

### `GD32_CLOCK_TIMER12`

```c
#define GD32_CLOCK_TIMER12 GD32_CLOCK_CONFIG(APB1EN, 7U)
```

<a id="a60bfa7bc6aafc012fa45b395d4d22c00"></a>

### `GD32_CLOCK_TIMER13`

```c
#define GD32_CLOCK_TIMER13 GD32_CLOCK_CONFIG(APB1EN, 8U)
```

<a id="a41623cb4499589163c0697a7a669ac25"></a>

### `GD32_CLOCK_TIMER2`

```c
#define GD32_CLOCK_TIMER2 GD32_CLOCK_CONFIG(APB1EN, 1U)
```

<a id="afb5aa7f1705febd51a92f9370bd03d14"></a>

### `GD32_CLOCK_TIMER3`

```c
#define GD32_CLOCK_TIMER3 GD32_CLOCK_CONFIG(APB1EN, 2U)
```

<a id="a9d52a01572ab9309c5ebd3a0def8542f"></a>

### `GD32_CLOCK_TIMER4`

```c
#define GD32_CLOCK_TIMER4 GD32_CLOCK_CONFIG(APB1EN, 3U)
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
#define GD32_CLOCK_TIMER7 GD32_CLOCK_CONFIG(APB2EN, 1U)
```

<a id="adbac39fc1c001fbb14036f08c81810ef"></a>

### `GD32_CLOCK_TIMER8`

```c
#define GD32_CLOCK_TIMER8 GD32_CLOCK_CONFIG(APB2EN, 16U)
```

<a id="a3981da513ef2eb351b403f6dc11a2c6b"></a>

### `GD32_CLOCK_TIMER9`

```c
#define GD32_CLOCK_TIMER9 GD32_CLOCK_CONFIG(APB2EN, 17U)
```

<a id="ab04cbf84abb9f4923b6e9381c22bdae1"></a>

### `GD32_CLOCK_TLI`

```c
#define GD32_CLOCK_TLI GD32_CLOCK_CONFIG(APB2EN, 26U)
```

<a id="ad7e9e9d34e7acca03e2538e1d5f52c0e"></a>

### `GD32_CLOCK_TRNG`

```c
#define GD32_CLOCK_TRNG GD32_CLOCK_CONFIG(AHB2EN, 6U)
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

<a id="a8ec6e1dfab01b3652183c38eac160288"></a>

### `GD32_CLOCK_UART6`

```c
#define GD32_CLOCK_UART6 GD32_CLOCK_CONFIG(APB1EN, 30U)
```

<a id="a683cb88b874a2b6802bba5f99b85163e"></a>

### `GD32_CLOCK_UART7`

```c
#define GD32_CLOCK_UART7 GD32_CLOCK_CONFIG(APB1EN, 31U)
```

<a id="ac1599e50ad14746470268bc14aa04318"></a>

### `GD32_CLOCK_USART0`

```c
#define GD32_CLOCK_USART0 GD32_CLOCK_CONFIG(APB2EN, 4U)
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

<a id="a736a4d8ae51d88226f8baeec49be4dc5"></a>

### `GD32_CLOCK_USART5`

```c
#define GD32_CLOCK_USART5 GD32_CLOCK_CONFIG(APB2EN, 5U)
```

<a id="ae11c1f5ccf256d32377eb9a6f07026f2"></a>

### `GD32_CLOCK_USBFS`

```c
#define GD32_CLOCK_USBFS GD32_CLOCK_CONFIG(AHB2EN, 7U)
```

<a id="a9bb9a4af2877fa954bda83bb8fbc39a6"></a>

### `GD32_CLOCK_USBHS`

```c
#define GD32_CLOCK_USBHS GD32_CLOCK_CONFIG(AHB1EN, 29U)
```

<a id="a921ac30c07db5ab957c001cc0cbbdd0d"></a>

### `GD32_CLOCK_USBHSULPI`

```c
#define GD32_CLOCK_USBHSULPI GD32_CLOCK_CONFIG(AHB1EN, 30U)
```

<a id="acd4e6949e5fb08e13129174ddd6f2e70"></a>

### `GD32_CLOCK_WWDGT`

```c
#define GD32_CLOCK_WWDGT GD32_CLOCK_CONFIG(APB1EN, 11U)
```


## 127.3\_原页交叉引用（Cross References）

- [gd32-clocks-common.h](../api_source_reference/P285_gd32-clocks-common.h_源码浏览.md)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/gd32f4xx-clocks_8h_source.html)
- [GD32_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html#a8b1e411caae3c88322d85671558b2bbc)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P126_zephyr__dt-bindings__reset__gd32f403.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P128_zephyr__dt-bindings__reset__gd32f4xx.h_文件参考.md)
