---
id: learning.zephyr-docs.api-file-clock-network-reference.page-23
title: zephyr__dt-bindings__clock__rtl87x2g-clocks.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rtl87x2g-clocks_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_zephyr\_\_dt-bindings\_\_clock\_\_rtl87x2g-clocks.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/rtl87x2g-clocks_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Realtek RTL87x2G时钟控制器（Clock Controller）的设备树绑定。

查看此文件的源码。

<a id="details"></a>

Realtek RTL87x2G时钟控制器（Clock Controller）的设备树绑定。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 23.1\_宏定义（Macros）

<a id="r_ad55bd03e176f93e3732af365ac55f585"></a>

```c
#define APB_CLK(peri)
```

相关声明：[APB_CLK](#ad55bd03e176f93e3732af365ac55f585)。

引用 APB 外设时钟（Peripheral Clock）的辅助宏。

<a id="define-members-0"></a>

### APB 外设时钟标识符（Peripheral Clock IDs）

APB 外设的时钟标识符（Clock Identifiers）。

<a id="r_a39eb12fde9b1e3b06172576e42156c72"></a>

```c
#define APB_PERIPH_SPIC0_CLOCK 0U
```

相关声明：[APB_PERIPH_SPIC0_CLOCK](#a39eb12fde9b1e3b06172576e42156c72)。

SPIC0 时钟（Clock）。

<a id="r_a32e5b770e7f37829ef5eb859c10f9e4c"></a>

```c
#define APB_PERIPH_SPIC1_CLOCK 1U
```

相关声明：[APB_PERIPH_SPIC1_CLOCK](#a32e5b770e7f37829ef5eb859c10f9e4c)。

SPIC1 时钟（Clock）。

<a id="r_ace494a5c9b9df1792acbba4ee8b652e9"></a>

```c
#define APB_PERIPH_SPIC2_CLOCK 2U
```

相关声明：[APB_PERIPH_SPIC2_CLOCK](#ace494a5c9b9df1792acbba4ee8b652e9)。

SPIC2 时钟（Clock）。

<a id="r_a90a6f41b4204d319e3451d149be66a5a"></a>

```c
#define APB_PERIPH_GDMA_CLOCK 3U
```

相关声明：[APB_PERIPH_GDMA_CLOCK](#a90a6f41b4204d319e3451d149be66a5a)。

GDMA 时钟（Clock）。

<a id="r_a435222bc8fc4d801f20323f728e42997"></a>

```c
#define APB_PERIPH_SPI0_SLAVE_CLOCK 4U
```

相关声明：[APB_PERIPH_SPI0_SLAVE_CLOCK](#a435222bc8fc4d801f20323f728e42997)。

SPI0_SLAVE 时钟（Clock）。

<a id="r_a54bbbfda564bd51403d3504abfc9f2d4"></a>

```c
#define APB_PERIPH_SPI1_CLOCK 5U
```

相关声明：[APB_PERIPH_SPI1_CLOCK](#a54bbbfda564bd51403d3504abfc9f2d4)。

SPI1 时钟（Clock）。

<a id="r_a9e14717faadb8f42ce6b92e8fd4d57e1"></a>

```c
#define APB_PERIPH_SPI0_CLOCK 6U
```

相关声明：[APB_PERIPH_SPI0_CLOCK](#a9e14717faadb8f42ce6b92e8fd4d57e1)。

SPI0 时钟（Clock）。

<a id="r_a7b1cf618efa111d318cd1b612d6c3c35"></a>

```c
#define APB_PERIPH_I2C3_CLOCK 7U
```

相关声明：[APB_PERIPH_I2C3_CLOCK](#a7b1cf618efa111d318cd1b612d6c3c35)。

I2C3 时钟（Clock）。

<a id="r_ae53d31ce9636f65b8da419dad4911ef9"></a>

```c
#define APB_PERIPH_I2C2_CLOCK 8U
```

相关声明：[APB_PERIPH_I2C2_CLOCK](#ae53d31ce9636f65b8da419dad4911ef9)。

I2C2 时钟（Clock）。

<a id="r_a2e596e5558f5723a4e87a0cc7e2a6b0e"></a>

```c
#define APB_PERIPH_I2C1_CLOCK 9U
```

相关声明：[APB_PERIPH_I2C1_CLOCK](#a2e596e5558f5723a4e87a0cc7e2a6b0e)。

I2C1 时钟（Clock）。

<a id="r_a4ec16e183666fc580101231ee47ac0cc"></a>

```c
#define APB_PERIPH_I2C0_CLOCK 10U
```

相关声明：[APB_PERIPH_I2C0_CLOCK](#a4ec16e183666fc580101231ee47ac0cc)。

I2C0 时钟（Clock）。

<a id="r_a1447dcf66b9b094542436c345b1c32dc"></a>

```c
#define APB_PERIPH_UART3_CLOCK 11U
```

相关声明：[APB_PERIPH_UART3_CLOCK](#a1447dcf66b9b094542436c345b1c32dc)。

UART3 时钟（Clock）。

<a id="r_a54a67ebfb34dd2069141245d3c0cddf1"></a>

```c
#define APB_PERIPH_UART2_CLOCK 12U
```

相关声明：[APB_PERIPH_UART2_CLOCK](#a54a67ebfb34dd2069141245d3c0cddf1)。

UART2 时钟（Clock）。

<a id="r_a41c6b4ceaa6c13e9baea45a070007c8e"></a>

```c
#define APB_PERIPH_UART1_CLOCK 13U
```

相关声明：[APB_PERIPH_UART1_CLOCK](#a41c6b4ceaa6c13e9baea45a070007c8e)。

UART1 时钟（Clock）。

<a id="r_a65239a50059424b4fe63aab426b96c43"></a>

```c
#define APB_PERIPH_UART0_CLOCK 14U
```

相关声明：[APB_PERIPH_UART0_CLOCK](#a65239a50059424b4fe63aab426b96c43)。

UART0 时钟（Clock）。

<a id="r_ade57aa90414beeaa60cceb2abba28097"></a>

```c
#define APB_PERIPH_ACCXTAL_CLOCK 15U
```

相关声明：[APB_PERIPH_ACCXTAL_CLOCK](#ade57aa90414beeaa60cceb2abba28097)。

ACCXTAL 时钟（Clock）。

<a id="r_a94235f06e73da67f3b5d6e8fcb8c15a3"></a>

```c
#define APB_PERIPH_PDCK_CLOCK 16U
```

相关声明：[APB_PERIPH_PDCK_CLOCK](#a94235f06e73da67f3b5d6e8fcb8c15a3)。

PDCK 时钟（Clock）。

<a id="r_afb1ad159cc096e4162918e6e4a67be68"></a>

```c
#define APB_PERIPH_ZBMAC_CLOCK 17U
```

相关声明：[APB_PERIPH_ZBMAC_CLOCK](#afb1ad159cc096e4162918e6e4a67be68)。

ZBMAC 时钟（Clock）。

<a id="r_afd981bb5cae1b95a7f41fe85c1f0ef3c"></a>

```c
#define APB_PERIPH_BTPHY_CLOCK 18U
```

相关声明：[APB_PERIPH_BTPHY_CLOCK](#afd981bb5cae1b95a7f41fe85c1f0ef3c)。

BTPHY 时钟（Clock）。

<a id="r_aa0d99d0040d2ceea5af8806a339f6f17"></a>

```c
#define APB_PERIPH_BTMAC_CLOCK 19U
```

相关声明：[APB_PERIPH_BTMAC_CLOCK](#aa0d99d0040d2ceea5af8806a339f6f17)。

BTMAC 时钟（Clock）。

<a id="r_aeb97999462697a70e152dea688f3001a"></a>

```c
#define APB_PERIPH_SEGCOM_CLOCK 20U
```

相关声明：[APB_PERIPH_SEGCOM_CLOCK](#aeb97999462697a70e152dea688f3001a)。

SEGCOM 时钟（Clock）。

<a id="r_ad4c7ac280712717ae659930909d093ea"></a>

```c
#define APB_PERIPH_SPI3W_CLOCK 21U
```

相关声明：[APB_PERIPH_SPI3W_CLOCK](#ad4c7ac280712717ae659930909d093ea)。

SPI3W 时钟（Clock）。

<a id="r_acd1979a3a56c161e4d3070969b7ffabb"></a>

```c
#define APB_PERIPH_ETH_CLOCK 22U
```

相关声明：[APB_PERIPH_ETH_CLOCK](#acd1979a3a56c161e4d3070969b7ffabb)。

ETH 时钟（Clock）。

<a id="r_aacca727cfa865d0f7b0c71a13ba88dfa"></a>

```c
#define APB_PERIPH_PPE_CLOCK 23U
```

相关声明：[APB_PERIPH_PPE_CLOCK](#aacca727cfa865d0f7b0c71a13ba88dfa)。

PPE 时钟（Clock）。

<a id="r_a08c425744f6044f9641578402a4f7751"></a>

```c
#define APB_PERIPH_KEYSCAN_CLOCK 24U
```

相关声明：[APB_PERIPH_KEYSCAN_CLOCK](#a08c425744f6044f9641578402a4f7751)。

KEYSCAN 时钟（Clock）。

<a id="r_abcff84540d681f1c70f999ba95bc634d"></a>

```c
#define APB_PERIPH_24BADC_CLOCK 25U
```

相关声明：[APB_PERIPH_24BADC_CLOCK](#abcff84540d681f1c70f999ba95bc634d)。

24BADC 时钟（Clock）。

<a id="r_a184c8c279a4bd9ee6cb6b47d662108b1"></a>

```c
#define APB_PERIPH_ADC_CLOCK 26U
```

相关声明：[APB_PERIPH_ADC_CLOCK](#a184c8c279a4bd9ee6cb6b47d662108b1)。

ADC 时钟（Clock）。

<a id="r_a8f1d40271edaaf685b87162b37e9c5f0"></a>

```c
#define APB_PERIPH_A2C_CLOCK 27U
```

相关声明：[APB_PERIPH_A2C_CLOCK](#a8f1d40271edaaf685b87162b37e9c5f0)。

A2C 时钟（Clock）。

<a id="r_ae4114dd3818d5cee94db5998806b2db3"></a>

```c
#define APB_PERIPH_IR_CLOCK 28U
```

相关声明：[APB_PERIPH_IR_CLOCK](#ae4114dd3818d5cee94db5998806b2db3)。

IR 时钟（Clock）。

<a id="r_a572ece6736d9507ff1467be0851d5988"></a>

```c
#define APB_PERIPH_ISO7816_CLOCK 29U
```

相关声明：[APB_PERIPH_ISO7816_CLOCK](#a572ece6736d9507ff1467be0851d5988)。

ISO7816 时钟（Clock）。

<a id="r_ab1d1f56ba7c23da1d7564c94c2275832"></a>

```c
#define APB_PERIPH_GPIOB_CLOCK 30U
```

相关声明：[APB_PERIPH_GPIOB_CLOCK](#ab1d1f56ba7c23da1d7564c94c2275832)。

GPIOB 时钟（Clock）。

<a id="r_a4719b55f485bc02c7ca32301703ad78c"></a>

```c
#define APB_PERIPH_GPIOA_CLOCK 31U
```

相关声明：[APB_PERIPH_GPIOA_CLOCK](#a4719b55f485bc02c7ca32301703ad78c)。

GPIOA 时钟（Clock）。

<a id="r_a55505f5d38f12d6a7487226b0d23dfed"></a>

```c
#define APB_PERIPH_DISP_CLOCK 32U
```

相关声明：[APB_PERIPH_DISP_CLOCK](#a55505f5d38f12d6a7487226b0d23dfed)。

DISP 时钟（Clock）。

<a id="r_aee828547f6e0f24fc2f39aa6d6627f4c"></a>

```c
#define APB_PERIPH_IMDC_CLOCK 33U
```

相关声明：[APB_PERIPH_IMDC_CLOCK](#aee828547f6e0f24fc2f39aa6d6627f4c)。

IMDC 时钟（Clock）。

<a id="r_ad0939b3f96dfd6838c1bce2bc9abc245"></a>

```c
#define APB_PERIPH_TIMER_CLOCK 34U
```

相关声明：[APB_PERIPH_TIMER_CLOCK](#ad0939b3f96dfd6838c1bce2bc9abc245)。

TIMER 时钟（Clock）。

<a id="r_aa63f1195dd67f8d5339fc330bdf9266f"></a>

```c
#define APB_PERIPH_ENHTIMER_CLOCK 35U
```

相关声明：[APB_PERIPH_ENHTIMER_CLOCK](#aa63f1195dd67f8d5339fc330bdf9266f)。

ENHTIMER 时钟（Clock）。

<a id="r_aec7dfb6b92936605dfa4cf47fcb49acb"></a>

```c
#define APB_PERIPH_ENHTIMER_PWM1_CLOCK 36U
```

相关声明：[APB_PERIPH_ENHTIMER_PWM1_CLOCK](#aec7dfb6b92936605dfa4cf47fcb49acb)。

ENHTIMER_PWM1 时钟（Clock）。

<a id="r_aa44acfe1d85804e81a90f63970a9f253"></a>

```c
#define APB_PERIPH_ENHTIMER_PWM0_CLOCK 37U
```

相关声明：[APB_PERIPH_ENHTIMER_PWM0_CLOCK](#aa44acfe1d85804e81a90f63970a9f253)。

ENHTIMER_PWM0 时钟（Clock）。

<a id="r_ace37cf07dce76b64f86ed493c94d822e"></a>

```c
#define APB_PERIPH_ENHTIMER_PWM3_CLOCK 38U
```

相关声明：[APB_PERIPH_ENHTIMER_PWM3_CLOCK](#ace37cf07dce76b64f86ed493c94d822e)。

ENHTIMER_PWM3 时钟（Clock）。

<a id="r_a8a12aa817f048cc49d481a0afc907fb9"></a>

```c
#define APB_PERIPH_ENHTIMER_PWM2_CLOCK 39U
```

相关声明：[APB_PERIPH_ENHTIMER_PWM2_CLOCK](#a8a12aa817f048cc49d481a0afc907fb9)。

ENHTIMER_PWM2 时钟（Clock）。

<a id="r_ada9eaa67f548a63a52fbaa8c2799aea2"></a>

```c
#define APB_PERIPH_SDHC_CLOCK 40U
```

相关声明：[APB_PERIPH_SDHC_CLOCK](#ada9eaa67f548a63a52fbaa8c2799aea2)。

SDHC 时钟（Clock）。

<a id="r_a7feeeafdc5b3e5667b139c924b2d6fd5"></a>

```c
#define APB_PERIPH_UART5_CLOCK 41U
```

相关声明：[APB_PERIPH_UART5_CLOCK](#a7feeeafdc5b3e5667b139c924b2d6fd5)。

UART5 时钟（Clock）。

<a id="r_a7d72eef00cc2b2c4b44fdd2169676d2f"></a>

```c
#define APB_PERIPH_UART4_CLOCK 42U
```

相关声明：[APB_PERIPH_UART4_CLOCK](#a7d72eef00cc2b2c4b44fdd2169676d2f)。

UART4 时钟（Clock）。

<a id="r_a9ac6830c64830ad357310dc57979ce3e"></a>

```c
#define APB_PERIPH_CODEC_CLOCK 43U
```

相关声明：[APB_PERIPH_CODEC_CLOCK](#a9ac6830c64830ad357310dc57979ce3e)。

CODEC 时钟（Clock）。

<a id="r_ac6534636af673dd9ec0bb86b9ea2b8c5"></a>

```c
#define APB_PERIPH_I2S1_CLOCK 44U
```

相关声明：[APB_PERIPH_I2S1_CLOCK](#ac6534636af673dd9ec0bb86b9ea2b8c5)。

I2S1 时钟（Clock）。

<a id="r_a92725eabd4435f5fae5c298b6529add9"></a>

```c
#define APB_PERIPH_I2S0_CLOCK 45U
```

相关声明：[APB_PERIPH_I2S0_CLOCK](#a92725eabd4435f5fae5c298b6529add9)。

I2S0 时钟（Clock）。

## 23.2\_详细说明（Detailed Documentation）

<a id="ad55bd03e176f93e3732af365ac55f585"></a>

### `APB_CLK`

```c
#define APB_CLK ( peri)
```

展开值（Value）：

```c
APB_PERIPH_##peri##_CLOCK
```

引用 APB 外设时钟（Peripheral Clock）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `peri` | 外设名称（Peripheral Name）。此宏自动展开为 `APB_PERIPH_<peri>_CLOCK`。 |

<a id="abcff84540d681f1c70f999ba95bc634d"></a>

### `APB_PERIPH_24BADC_CLOCK`

```c
#define APB_PERIPH_24BADC_CLOCK 25U
```

24BADC 时钟（Clock）。

<a id="a8f1d40271edaaf685b87162b37e9c5f0"></a>

### `APB_PERIPH_A2C_CLOCK`

```c
#define APB_PERIPH_A2C_CLOCK 27U
```

A2C 时钟（Clock）。

<a id="ade57aa90414beeaa60cceb2abba28097"></a>

### `APB_PERIPH_ACCXTAL_CLOCK`

```c
#define APB_PERIPH_ACCXTAL_CLOCK 15U
```

ACCXTAL 时钟（Clock）。

<a id="a184c8c279a4bd9ee6cb6b47d662108b1"></a>

### `APB_PERIPH_ADC_CLOCK`

```c
#define APB_PERIPH_ADC_CLOCK 26U
```

ADC 时钟（Clock）。

<a id="aa0d99d0040d2ceea5af8806a339f6f17"></a>

### `APB_PERIPH_BTMAC_CLOCK`

```c
#define APB_PERIPH_BTMAC_CLOCK 19U
```

BTMAC 时钟（Clock）。

<a id="afd981bb5cae1b95a7f41fe85c1f0ef3c"></a>

### `APB_PERIPH_BTPHY_CLOCK`

```c
#define APB_PERIPH_BTPHY_CLOCK 18U
```

BTPHY 时钟（Clock）。

<a id="a9ac6830c64830ad357310dc57979ce3e"></a>

### `APB_PERIPH_CODEC_CLOCK`

```c
#define APB_PERIPH_CODEC_CLOCK 43U
```

CODEC 时钟（Clock）。

<a id="a55505f5d38f12d6a7487226b0d23dfed"></a>

### `APB_PERIPH_DISP_CLOCK`

```c
#define APB_PERIPH_DISP_CLOCK 32U
```

DISP 时钟（Clock）。

<a id="aa63f1195dd67f8d5339fc330bdf9266f"></a>

### `APB_PERIPH_ENHTIMER_CLOCK`

```c
#define APB_PERIPH_ENHTIMER_CLOCK 35U
```

ENHTIMER 时钟（Clock）。

<a id="aa44acfe1d85804e81a90f63970a9f253"></a>

### `APB_PERIPH_ENHTIMER_PWM0_CLOCK`

```c
#define APB_PERIPH_ENHTIMER_PWM0_CLOCK 37U
```

ENHTIMER_PWM0 时钟（Clock）。

<a id="aec7dfb6b92936605dfa4cf47fcb49acb"></a>

### `APB_PERIPH_ENHTIMER_PWM1_CLOCK`

```c
#define APB_PERIPH_ENHTIMER_PWM1_CLOCK 36U
```

ENHTIMER_PWM1 时钟（Clock）。

<a id="a8a12aa817f048cc49d481a0afc907fb9"></a>

### `APB_PERIPH_ENHTIMER_PWM2_CLOCK`

```c
#define APB_PERIPH_ENHTIMER_PWM2_CLOCK 39U
```

ENHTIMER_PWM2 时钟（Clock）。

<a id="ace37cf07dce76b64f86ed493c94d822e"></a>

### `APB_PERIPH_ENHTIMER_PWM3_CLOCK`

```c
#define APB_PERIPH_ENHTIMER_PWM3_CLOCK 38U
```

ENHTIMER_PWM3 时钟（Clock）。

<a id="acd1979a3a56c161e4d3070969b7ffabb"></a>

### `APB_PERIPH_ETH_CLOCK`

```c
#define APB_PERIPH_ETH_CLOCK 22U
```

ETH 时钟（Clock）。

<a id="a90a6f41b4204d319e3451d149be66a5a"></a>

### `APB_PERIPH_GDMA_CLOCK`

```c
#define APB_PERIPH_GDMA_CLOCK 3U
```

GDMA 时钟（Clock）。

<a id="a4719b55f485bc02c7ca32301703ad78c"></a>

### `APB_PERIPH_GPIOA_CLOCK`

```c
#define APB_PERIPH_GPIOA_CLOCK 31U
```

GPIOA 时钟（Clock）。

<a id="ab1d1f56ba7c23da1d7564c94c2275832"></a>

### `APB_PERIPH_GPIOB_CLOCK`

```c
#define APB_PERIPH_GPIOB_CLOCK 30U
```

GPIOB 时钟（Clock）。

<a id="a4ec16e183666fc580101231ee47ac0cc"></a>

### `APB_PERIPH_I2C0_CLOCK`

```c
#define APB_PERIPH_I2C0_CLOCK 10U
```

I2C0 时钟（Clock）。

<a id="a2e596e5558f5723a4e87a0cc7e2a6b0e"></a>

### `APB_PERIPH_I2C1_CLOCK`

```c
#define APB_PERIPH_I2C1_CLOCK 9U
```

I2C1 时钟（Clock）。

<a id="ae53d31ce9636f65b8da419dad4911ef9"></a>

### `APB_PERIPH_I2C2_CLOCK`

```c
#define APB_PERIPH_I2C2_CLOCK 8U
```

I2C2 时钟（Clock）。

<a id="a7b1cf618efa111d318cd1b612d6c3c35"></a>

### `APB_PERIPH_I2C3_CLOCK`

```c
#define APB_PERIPH_I2C3_CLOCK 7U
```

I2C3 时钟（Clock）。

<a id="a92725eabd4435f5fae5c298b6529add9"></a>

### `APB_PERIPH_I2S0_CLOCK`

```c
#define APB_PERIPH_I2S0_CLOCK 45U
```

I2S0 时钟（Clock）。

<a id="ac6534636af673dd9ec0bb86b9ea2b8c5"></a>

### `APB_PERIPH_I2S1_CLOCK`

```c
#define APB_PERIPH_I2S1_CLOCK 44U
```

I2S1 时钟（Clock）。

<a id="aee828547f6e0f24fc2f39aa6d6627f4c"></a>

### `APB_PERIPH_IMDC_CLOCK`

```c
#define APB_PERIPH_IMDC_CLOCK 33U
```

IMDC 时钟（Clock）。

<a id="ae4114dd3818d5cee94db5998806b2db3"></a>

### `APB_PERIPH_IR_CLOCK`

```c
#define APB_PERIPH_IR_CLOCK 28U
```

IR 时钟（Clock）。

<a id="a572ece6736d9507ff1467be0851d5988"></a>

### `APB_PERIPH_ISO7816_CLOCK`

```c
#define APB_PERIPH_ISO7816_CLOCK 29U
```

ISO7816 时钟（Clock）。

<a id="a08c425744f6044f9641578402a4f7751"></a>

### `APB_PERIPH_KEYSCAN_CLOCK`

```c
#define APB_PERIPH_KEYSCAN_CLOCK 24U
```

KEYSCAN 时钟（Clock）。

<a id="a94235f06e73da67f3b5d6e8fcb8c15a3"></a>

### `APB_PERIPH_PDCK_CLOCK`

```c
#define APB_PERIPH_PDCK_CLOCK 16U
```

PDCK 时钟（Clock）。

<a id="aacca727cfa865d0f7b0c71a13ba88dfa"></a>

### `APB_PERIPH_PPE_CLOCK`

```c
#define APB_PERIPH_PPE_CLOCK 23U
```

PPE 时钟（Clock）。

<a id="ada9eaa67f548a63a52fbaa8c2799aea2"></a>

### `APB_PERIPH_SDHC_CLOCK`

```c
#define APB_PERIPH_SDHC_CLOCK 40U
```

SDHC 时钟（Clock）。

<a id="aeb97999462697a70e152dea688f3001a"></a>

### `APB_PERIPH_SEGCOM_CLOCK`

```c
#define APB_PERIPH_SEGCOM_CLOCK 20U
```

SEGCOM 时钟（Clock）。

<a id="a9e14717faadb8f42ce6b92e8fd4d57e1"></a>

### `APB_PERIPH_SPI0_CLOCK`

```c
#define APB_PERIPH_SPI0_CLOCK 6U
```

SPI0 时钟（Clock）。

<a id="a435222bc8fc4d801f20323f728e42997"></a>

### `APB_PERIPH_SPI0_SLAVE_CLOCK`

```c
#define APB_PERIPH_SPI0_SLAVE_CLOCK 4U
```

SPI0_SLAVE 时钟（Clock）。

<a id="a54bbbfda564bd51403d3504abfc9f2d4"></a>

### `APB_PERIPH_SPI1_CLOCK`

```c
#define APB_PERIPH_SPI1_CLOCK 5U
```

SPI1 时钟（Clock）。

<a id="ad4c7ac280712717ae659930909d093ea"></a>

### `APB_PERIPH_SPI3W_CLOCK`

```c
#define APB_PERIPH_SPI3W_CLOCK 21U
```

SPI3W 时钟（Clock）。

<a id="a39eb12fde9b1e3b06172576e42156c72"></a>

### `APB_PERIPH_SPIC0_CLOCK`

```c
#define APB_PERIPH_SPIC0_CLOCK 0U
```

SPIC0 时钟（Clock）。

<a id="a32e5b770e7f37829ef5eb859c10f9e4c"></a>

### `APB_PERIPH_SPIC1_CLOCK`

```c
#define APB_PERIPH_SPIC1_CLOCK 1U
```

SPIC1 时钟（Clock）。

<a id="ace494a5c9b9df1792acbba4ee8b652e9"></a>

### `APB_PERIPH_SPIC2_CLOCK`

```c
#define APB_PERIPH_SPIC2_CLOCK 2U
```

SPIC2 时钟（Clock）。

<a id="ad0939b3f96dfd6838c1bce2bc9abc245"></a>

### `APB_PERIPH_TIMER_CLOCK`

```c
#define APB_PERIPH_TIMER_CLOCK 34U
```

TIMER 时钟（Clock）。

<a id="a65239a50059424b4fe63aab426b96c43"></a>

### `APB_PERIPH_UART0_CLOCK`

```c
#define APB_PERIPH_UART0_CLOCK 14U
```

UART0 时钟（Clock）。

<a id="a41c6b4ceaa6c13e9baea45a070007c8e"></a>

### `APB_PERIPH_UART1_CLOCK`

```c
#define APB_PERIPH_UART1_CLOCK 13U
```

UART1 时钟（Clock）。

<a id="a54a67ebfb34dd2069141245d3c0cddf1"></a>

### `APB_PERIPH_UART2_CLOCK`

```c
#define APB_PERIPH_UART2_CLOCK 12U
```

UART2 时钟（Clock）。

<a id="a1447dcf66b9b094542436c345b1c32dc"></a>

### `APB_PERIPH_UART3_CLOCK`

```c
#define APB_PERIPH_UART3_CLOCK 11U
```

UART3 时钟（Clock）。

<a id="a7d72eef00cc2b2c4b44fdd2169676d2f"></a>

### `APB_PERIPH_UART4_CLOCK`

```c
#define APB_PERIPH_UART4_CLOCK 42U
```

UART4 时钟（Clock）。

<a id="a7feeeafdc5b3e5667b139c924b2d6fd5"></a>

### `APB_PERIPH_UART5_CLOCK`

```c
#define APB_PERIPH_UART5_CLOCK 41U
```

UART5 时钟（Clock）。

<a id="afb1ad159cc096e4162918e6e4a67be68"></a>

### `APB_PERIPH_ZBMAC_CLOCK`

```c
#define APB_PERIPH_ZBMAC_CLOCK 17U
```

ZBMAC 时钟（Clock）。


## 23.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P735_rtl87x2g-clocks.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P022_zephyr__dt-bindings__clock__rtl8752h-clocks.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P024_zephyr__stats__stats.h_文件参考.md)
