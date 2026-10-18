---
id: learning.zephyr-docs.api-file-supplement-reference.page-102
title: zephyr__dt-bindings__dma__rtl87x2g-dma.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rtl87x2g-dma_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第102章\_zephyr\_\_dt-bindings\_\_dma\_\_rtl87x2g-dma.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/rtl87x2g-dma_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

RTL87X2G DMA的设备树绑定（Devicetree Bindings）。

<a id="details"></a>

```c
#include "bee-dma.h"
```

查看此文件的源码。

RTL87X2G DMA 设备树绑定（Devicetree Bindings）。RTL87X2G 通用 DMA 控制器（GDMA Controller）的握手槽位标识（Handshake / Slot IDs）。取值与硬件抽象层（HAL）的 `rtl_gdma_def.h` 中的 `GDMA_Handshake_*` 定义一致。请在 `slot` 单元中使用这些标识，并搭配 `<dt-bindings/dma/bee-dma.h>` 中的 `config` 单元宏。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 102.1\_宏定义（Macros）

<a id="r_a0d0dff917b561c89b56aa7bd65a0fc29"></a>

```c
#define BEE_DMA_HANDSHAKE_UART0_TX 0
```

相关声明：[BEE_DMA_HANDSHAKE_UART0_TX](#a0d0dff917b561c89b56aa7bd65a0fc29)。

<a id="r_a22dbbef8ff428ff33b5a25cdd9722c20"></a>

```c
#define BEE_DMA_HANDSHAKE_UART0_RX 1
```

相关声明：[BEE_DMA_HANDSHAKE_UART0_RX](#a22dbbef8ff428ff33b5a25cdd9722c20)。

<a id="r_a3c2e0f845b446f2992f4c319ef37a73e"></a>

```c
#define BEE_DMA_HANDSHAKE_UART1_TX 2
```

相关声明：[BEE_DMA_HANDSHAKE_UART1_TX](#a3c2e0f845b446f2992f4c319ef37a73e)。

<a id="r_aba1f436a24daafa2b29d33464c11a87c"></a>

```c
#define BEE_DMA_HANDSHAKE_UART1_RX 3
```

相关声明：[BEE_DMA_HANDSHAKE_UART1_RX](#aba1f436a24daafa2b29d33464c11a87c)。

<a id="r_ae2490513dad456ea021f36b9ac9a14ed"></a>

```c
#define BEE_DMA_HANDSHAKE_UART2_TX 4
```

相关声明：[BEE_DMA_HANDSHAKE_UART2_TX](#ae2490513dad456ea021f36b9ac9a14ed)。

<a id="r_afc4d11ad22bb1d7dc558ebb381a14b70"></a>

```c
#define BEE_DMA_HANDSHAKE_UART2_RX 5
```

相关声明：[BEE_DMA_HANDSHAKE_UART2_RX](#afc4d11ad22bb1d7dc558ebb381a14b70)。

<a id="r_a0480c2867cc1e3f2ed28a45a420f8107"></a>

```c
#define BEE_DMA_HANDSHAKE_UART3_TX 6
```

相关声明：[BEE_DMA_HANDSHAKE_UART3_TX](#a0480c2867cc1e3f2ed28a45a420f8107)。

<a id="r_aa32d4c957a1cab2b2609300d4ccc59dc"></a>

```c
#define BEE_DMA_HANDSHAKE_UART3_RX 7
```

相关声明：[BEE_DMA_HANDSHAKE_UART3_RX](#aa32d4c957a1cab2b2609300d4ccc59dc)。

<a id="r_a3e0eedc6abbae8f9eb81ecdb3a7985da"></a>

```c
#define BEE_DMA_HANDSHAKE_I2C0_TX 8
```

相关声明：[BEE_DMA_HANDSHAKE_I2C0_TX](#a3e0eedc6abbae8f9eb81ecdb3a7985da)。

<a id="r_ab63670f57fc58b2b322179f1707136ce"></a>

```c
#define BEE_DMA_HANDSHAKE_I2C0_RX 9
```

相关声明：[BEE_DMA_HANDSHAKE_I2C0_RX](#ab63670f57fc58b2b322179f1707136ce)。

<a id="r_a774cfd73cabe18833d493542ec3191e5"></a>

```c
#define BEE_DMA_HANDSHAKE_I2C1_TX 10
```

相关声明：[BEE_DMA_HANDSHAKE_I2C1_TX](#a774cfd73cabe18833d493542ec3191e5)。

<a id="r_acf107d641c2ec0a3bdfd3fa7f0ecaf14"></a>

```c
#define BEE_DMA_HANDSHAKE_I2C1_RX 11
```

相关声明：[BEE_DMA_HANDSHAKE_I2C1_RX](#acf107d641c2ec0a3bdfd3fa7f0ecaf14)。

<a id="r_a56c359885d64a68f4c79fac82c2bd85e"></a>

```c
#define BEE_DMA_HANDSHAKE_I2C2_TX 12
```

相关声明：[BEE_DMA_HANDSHAKE_I2C2_TX](#a56c359885d64a68f4c79fac82c2bd85e)。

<a id="r_a2febb54f5238dea1b19b5c741263bcef"></a>

```c
#define BEE_DMA_HANDSHAKE_I2C2_RX 13
```

相关声明：[BEE_DMA_HANDSHAKE_I2C2_RX](#a2febb54f5238dea1b19b5c741263bcef)。

<a id="r_a00536d1ff6ea4fd1a7c40614f7062e2a"></a>

```c
#define BEE_DMA_HANDSHAKE_I2C3_TX 14
```

相关声明：[BEE_DMA_HANDSHAKE_I2C3_TX](#a00536d1ff6ea4fd1a7c40614f7062e2a)。

<a id="r_a88a79b5ed66050a559bf1f2eecd58276"></a>

```c
#define BEE_DMA_HANDSHAKE_I2C3_RX 15
```

相关声明：[BEE_DMA_HANDSHAKE_I2C3_RX](#a88a79b5ed66050a559bf1f2eecd58276)。

<a id="r_a3374f6ce3ad11f81574e879a12e18ad6"></a>

```c
#define BEE_DMA_HANDSHAKE_SPI0_TX 16
```

相关声明：[BEE_DMA_HANDSHAKE_SPI0_TX](#a3374f6ce3ad11f81574e879a12e18ad6)。

<a id="r_abba2dba81a7a9de51542ebd3477433b7"></a>

```c
#define BEE_DMA_HANDSHAKE_SPI0_RX 17
```

相关声明：[BEE_DMA_HANDSHAKE_SPI0_RX](#abba2dba81a7a9de51542ebd3477433b7)。

<a id="r_a36dd9c37f902e1a8645f65025669a865"></a>

```c
#define BEE_DMA_HANDSHAKE_SPI1_TX 18
```

相关声明：[BEE_DMA_HANDSHAKE_SPI1_TX](#a36dd9c37f902e1a8645f65025669a865)。

<a id="r_a52f8b93db8e706525041e886864c8d18"></a>

```c
#define BEE_DMA_HANDSHAKE_SPI1_RX 19
```

相关声明：[BEE_DMA_HANDSHAKE_SPI1_RX](#a52f8b93db8e706525041e886864c8d18)。

<a id="r_a51a2ae048f2305a7c847a7f7c3cf7a47"></a>

```c
#define BEE_DMA_HANDSHAKE_SPI_SLAVE_TX 20
```

相关声明：[BEE_DMA_HANDSHAKE_SPI_SLAVE_TX](#a51a2ae048f2305a7c847a7f7c3cf7a47)。

<a id="r_a78907f940c34441814c7fb87983845ef"></a>

```c
#define BEE_DMA_HANDSHAKE_SPI_SLAVE_RX 21
```

相关声明：[BEE_DMA_HANDSHAKE_SPI_SLAVE_RX](#a78907f940c34441814c7fb87983845ef)。

<a id="r_a4c7617163f6d4a6621295c92aa402162"></a>

```c
#define BEE_DMA_HANDSHAKE_ENH_TIM0 22
```

相关声明：[BEE_DMA_HANDSHAKE_ENH_TIM0](#a4c7617163f6d4a6621295c92aa402162)。

<a id="r_aacb722354a323c5111c963eee20362f9"></a>

```c
#define BEE_DMA_HANDSHAKE_ENH_TIM1 23
```

相关声明：[BEE_DMA_HANDSHAKE_ENH_TIM1](#aacb722354a323c5111c963eee20362f9)。

<a id="r_ad87c3ad701ab3cb4453a7be6f8c003b0"></a>

```c
#define BEE_DMA_HANDSHAKE_ENH_TIM2 24
```

相关声明：[BEE_DMA_HANDSHAKE_ENH_TIM2](#ad87c3ad701ab3cb4453a7be6f8c003b0)。

<a id="r_ac26f391e25e280e87fd75f9c4792e35a"></a>

```c
#define BEE_DMA_HANDSHAKE_ENH_TIM3 25
```

相关声明：[BEE_DMA_HANDSHAKE_ENH_TIM3](#ac26f391e25e280e87fd75f9c4792e35a)。

<a id="r_a3487b01f029dfb76c7bfdce7686463b7"></a>

```c
#define BEE_DMA_HANDSHAKE_ADC_RX 26
```

相关声明：[BEE_DMA_HANDSHAKE_ADC_RX](#a3487b01f029dfb76c7bfdce7686463b7)。

<a id="r_ae32e33d0e98fc3a403c3ac7d0e942334"></a>

```c
#define BEE_DMA_HANDSHAKE_IDU_RX 27
```

相关声明：[BEE_DMA_HANDSHAKE_IDU_RX](#ae32e33d0e98fc3a403c3ac7d0e942334)。

<a id="r_a54ba59226123fa5d52d851d7e39eefeb"></a>

```c
#define BEE_DMA_HANDSHAKE_IDU_TX 28
```

相关声明：[BEE_DMA_HANDSHAKE_IDU_TX](#a54ba59226123fa5d52d851d7e39eefeb)。

<a id="r_aec47cd5538f9fc57a3a19956807d5cbb"></a>

```c
#define BEE_DMA_HANDSHAKE_TIM5 29
```

相关声明：[BEE_DMA_HANDSHAKE_TIM5](#aec47cd5538f9fc57a3a19956807d5cbb)。

<a id="r_a5170abd32ff447827cea0b47973d5e41"></a>

```c
#define BEE_DMA_HANDSHAKE_TIM6 30
```

相关声明：[BEE_DMA_HANDSHAKE_TIM6](#a5170abd32ff447827cea0b47973d5e41)。

<a id="r_aefafec8ed627f094f65841e91fdd4326"></a>

```c
#define BEE_DMA_HANDSHAKE_TIM7 31
```

相关声明：[BEE_DMA_HANDSHAKE_TIM7](#aefafec8ed627f094f65841e91fdd4326)。

<a id="r_a14bec568e9617b8c10dac9b7e95ee8ae"></a>

```c
#define BEE_DMA_HANDSHAKE_CAN_BUS_RX 32
```

相关声明：[BEE_DMA_HANDSHAKE_CAN_BUS_RX](#a14bec568e9617b8c10dac9b7e95ee8ae)。

<a id="r_ad90e978b32dc8825eb3fb265eeef446c"></a>

```c
#define BEE_DMA_HANDSHAKE_SPIC0_TX 33
```

相关声明：[BEE_DMA_HANDSHAKE_SPIC0_TX](#ad90e978b32dc8825eb3fb265eeef446c)。

<a id="r_abfff852e7f9ce88693d78c0ab71e0f97"></a>

```c
#define BEE_DMA_HANDSHAKE_SPIC0_RX 34
```

相关声明：[BEE_DMA_HANDSHAKE_SPIC0_RX](#abfff852e7f9ce88693d78c0ab71e0f97)。

<a id="r_a983fa4d96793585a416aebacd0d04c07"></a>

```c
#define BEE_DMA_HANDSHAKE_SPIC1_TX 35
```

相关声明：[BEE_DMA_HANDSHAKE_SPIC1_TX](#a983fa4d96793585a416aebacd0d04c07)。

<a id="r_a2b42833e6b685a4415f3c96ccf038e71"></a>

```c
#define BEE_DMA_HANDSHAKE_SPIC1_RX 36
```

相关声明：[BEE_DMA_HANDSHAKE_SPIC1_RX](#a2b42833e6b685a4415f3c96ccf038e71)。

<a id="r_a866d3ccc7095de5da4ded14d8279660d"></a>

```c
#define BEE_DMA_HANDSHAKE_SPIC2_TX 37
```

相关声明：[BEE_DMA_HANDSHAKE_SPIC2_TX](#a866d3ccc7095de5da4ded14d8279660d)。

<a id="r_a7bffecab9a08289a4a5a4268e7b87e20"></a>

```c
#define BEE_DMA_HANDSHAKE_SPIC2_RX 38
```

相关声明：[BEE_DMA_HANDSHAKE_SPIC2_RX](#a7bffecab9a08289a4a5a4268e7b87e20)。

<a id="r_a55fb1eee56cdfece146fe830727b6b74"></a>

```c
#define BEE_DMA_HANDSHAKE_IR_TX 39
```

相关声明：[BEE_DMA_HANDSHAKE_IR_TX](#a55fb1eee56cdfece146fe830727b6b74)。

<a id="r_a817500f56cc164220e316b328b70522d"></a>

```c
#define BEE_DMA_HANDSHAKE_IR_RX 40
```

相关声明：[BEE_DMA_HANDSHAKE_IR_RX](#a817500f56cc164220e316b328b70522d)。

<a id="r_a582c518e837e1158037e81f22f4e3cdb"></a>

```c
#define BEE_DMA_HANDSHAKE_I2S0_TDM0_TX 41
```

相关声明：[BEE_DMA_HANDSHAKE_I2S0_TDM0_TX](#a582c518e837e1158037e81f22f4e3cdb)。

<a id="r_a832e442254b13a16b1e062a32537c7c5"></a>

```c
#define BEE_DMA_HANDSHAKE_I2S0_TDM0_RX 42
```

相关声明：[BEE_DMA_HANDSHAKE_I2S0_TDM0_RX](#a832e442254b13a16b1e062a32537c7c5)。

<a id="r_a76270806808cf7a104b1e9237049e540"></a>

```c
#define BEE_DMA_HANDSHAKE_I2S1_TDM0_TX 43
```

相关声明：[BEE_DMA_HANDSHAKE_I2S1_TDM0_TX](#a76270806808cf7a104b1e9237049e540)。

<a id="r_a506e476489771d524f31e3cabb49b8a5"></a>

```c
#define BEE_DMA_HANDSHAKE_I2S1_TDM0_RX 44
```

相关声明：[BEE_DMA_HANDSHAKE_I2S1_TDM0_RX](#a506e476489771d524f31e3cabb49b8a5)。

<a id="r_af068f66f49e230ef003db06d321c7b31"></a>

```c
#define BEE_DMA_HANDSHAKE_SHA256_TX 45
```

相关声明：[BEE_DMA_HANDSHAKE_SHA256_TX](#af068f66f49e230ef003db06d321c7b31)。

<a id="r_a675b77d5fbc83426774372c7e5bc5326"></a>

```c
#define BEE_DMA_HANDSHAKE_AES_TX 47
```

相关声明：[BEE_DMA_HANDSHAKE_AES_TX](#a675b77d5fbc83426774372c7e5bc5326)。

<a id="r_a6088046bfb66874b5a25ae3b8ec7103e"></a>

```c
#define BEE_DMA_HANDSHAKE_AES_RX 48
```

相关声明：[BEE_DMA_HANDSHAKE_AES_RX](#a6088046bfb66874b5a25ae3b8ec7103e)。

<a id="r_a62b7e0985a99a1f616e8bf8d035248f1"></a>

```c
#define BEE_DMA_HANDSHAKE_PUB_KEY_TX 49
```

相关声明：[BEE_DMA_HANDSHAKE_PUB_KEY_TX](#a62b7e0985a99a1f616e8bf8d035248f1)。

<a id="r_a6fb2531f99d489a35901cf1147fd2269"></a>

```c
#define BEE_DMA_HANDSHAKE_PUB_KEY_RX 50
```

相关声明：[BEE_DMA_HANDSHAKE_PUB_KEY_RX](#a6fb2531f99d489a35901cf1147fd2269)。

<a id="r_a455448968440e3f4c18187d5c7229ef1"></a>

```c
#define BEE_DMA_HANDSHAKE_24BIT_ADC_RX 51
```

相关声明：[BEE_DMA_HANDSHAKE_24BIT_ADC_RX](#a455448968440e3f4c18187d5c7229ef1)。

<a id="r_a44b1678113587fc4ebaab28311cf6037"></a>

```c
#define BEE_DMA_HANDSHAKE_UART4_TX 52
```

相关声明：[BEE_DMA_HANDSHAKE_UART4_TX](#a44b1678113587fc4ebaab28311cf6037)。

<a id="r_aab8e42445c3f5244f158970cf8358f4f"></a>

```c
#define BEE_DMA_HANDSHAKE_UART4_RX 53
```

相关声明：[BEE_DMA_HANDSHAKE_UART4_RX](#aab8e42445c3f5244f158970cf8358f4f)。

<a id="r_a5a238593f285b16cbcfe612038c1bdfa"></a>

```c
#define BEE_DMA_HANDSHAKE_UART5_TX 54
```

相关声明：[BEE_DMA_HANDSHAKE_UART5_TX](#a5a238593f285b16cbcfe612038c1bdfa)。

<a id="r_ae9f8c55be1d2780571a7b1dcc127f2ae"></a>

```c
#define BEE_DMA_HANDSHAKE_UART5_RX 55
```

相关声明：[BEE_DMA_HANDSHAKE_UART5_RX](#ae9f8c55be1d2780571a7b1dcc127f2ae)。

## 102.2\_详细说明（Detailed Documentation）

<a id="a455448968440e3f4c18187d5c7229ef1"></a>

### `BEE_DMA_HANDSHAKE_24BIT_ADC_RX`

```c
#define BEE_DMA_HANDSHAKE_24BIT_ADC_RX 51
```

<a id="a3487b01f029dfb76c7bfdce7686463b7"></a>

### `BEE_DMA_HANDSHAKE_ADC_RX`

```c
#define BEE_DMA_HANDSHAKE_ADC_RX 26
```

<a id="a6088046bfb66874b5a25ae3b8ec7103e"></a>

### `BEE_DMA_HANDSHAKE_AES_RX`

```c
#define BEE_DMA_HANDSHAKE_AES_RX 48
```

<a id="a675b77d5fbc83426774372c7e5bc5326"></a>

### `BEE_DMA_HANDSHAKE_AES_TX`

```c
#define BEE_DMA_HANDSHAKE_AES_TX 47
```

<a id="a14bec568e9617b8c10dac9b7e95ee8ae"></a>

### `BEE_DMA_HANDSHAKE_CAN_BUS_RX`

```c
#define BEE_DMA_HANDSHAKE_CAN_BUS_RX 32
```

<a id="a4c7617163f6d4a6621295c92aa402162"></a>

### `BEE_DMA_HANDSHAKE_ENH_TIM0`

```c
#define BEE_DMA_HANDSHAKE_ENH_TIM0 22
```

<a id="aacb722354a323c5111c963eee20362f9"></a>

### `BEE_DMA_HANDSHAKE_ENH_TIM1`

```c
#define BEE_DMA_HANDSHAKE_ENH_TIM1 23
```

<a id="ad87c3ad701ab3cb4453a7be6f8c003b0"></a>

### `BEE_DMA_HANDSHAKE_ENH_TIM2`

```c
#define BEE_DMA_HANDSHAKE_ENH_TIM2 24
```

<a id="ac26f391e25e280e87fd75f9c4792e35a"></a>

### `BEE_DMA_HANDSHAKE_ENH_TIM3`

```c
#define BEE_DMA_HANDSHAKE_ENH_TIM3 25
```

<a id="ab63670f57fc58b2b322179f1707136ce"></a>

### `BEE_DMA_HANDSHAKE_I2C0_RX`

```c
#define BEE_DMA_HANDSHAKE_I2C0_RX 9
```

<a id="a3e0eedc6abbae8f9eb81ecdb3a7985da"></a>

### `BEE_DMA_HANDSHAKE_I2C0_TX`

```c
#define BEE_DMA_HANDSHAKE_I2C0_TX 8
```

<a id="acf107d641c2ec0a3bdfd3fa7f0ecaf14"></a>

### `BEE_DMA_HANDSHAKE_I2C1_RX`

```c
#define BEE_DMA_HANDSHAKE_I2C1_RX 11
```

<a id="a774cfd73cabe18833d493542ec3191e5"></a>

### `BEE_DMA_HANDSHAKE_I2C1_TX`

```c
#define BEE_DMA_HANDSHAKE_I2C1_TX 10
```

<a id="a2febb54f5238dea1b19b5c741263bcef"></a>

### `BEE_DMA_HANDSHAKE_I2C2_RX`

```c
#define BEE_DMA_HANDSHAKE_I2C2_RX 13
```

<a id="a56c359885d64a68f4c79fac82c2bd85e"></a>

### `BEE_DMA_HANDSHAKE_I2C2_TX`

```c
#define BEE_DMA_HANDSHAKE_I2C2_TX 12
```

<a id="a88a79b5ed66050a559bf1f2eecd58276"></a>

### `BEE_DMA_HANDSHAKE_I2C3_RX`

```c
#define BEE_DMA_HANDSHAKE_I2C3_RX 15
```

<a id="a00536d1ff6ea4fd1a7c40614f7062e2a"></a>

### `BEE_DMA_HANDSHAKE_I2C3_TX`

```c
#define BEE_DMA_HANDSHAKE_I2C3_TX 14
```

<a id="a832e442254b13a16b1e062a32537c7c5"></a>

### `BEE_DMA_HANDSHAKE_I2S0_TDM0_RX`

```c
#define BEE_DMA_HANDSHAKE_I2S0_TDM0_RX 42
```

<a id="a582c518e837e1158037e81f22f4e3cdb"></a>

### `BEE_DMA_HANDSHAKE_I2S0_TDM0_TX`

```c
#define BEE_DMA_HANDSHAKE_I2S0_TDM0_TX 41
```

<a id="a506e476489771d524f31e3cabb49b8a5"></a>

### `BEE_DMA_HANDSHAKE_I2S1_TDM0_RX`

```c
#define BEE_DMA_HANDSHAKE_I2S1_TDM0_RX 44
```

<a id="a76270806808cf7a104b1e9237049e540"></a>

### `BEE_DMA_HANDSHAKE_I2S1_TDM0_TX`

```c
#define BEE_DMA_HANDSHAKE_I2S1_TDM0_TX 43
```

<a id="ae32e33d0e98fc3a403c3ac7d0e942334"></a>

### `BEE_DMA_HANDSHAKE_IDU_RX`

```c
#define BEE_DMA_HANDSHAKE_IDU_RX 27
```

<a id="a54ba59226123fa5d52d851d7e39eefeb"></a>

### `BEE_DMA_HANDSHAKE_IDU_TX`

```c
#define BEE_DMA_HANDSHAKE_IDU_TX 28
```

<a id="a817500f56cc164220e316b328b70522d"></a>

### `BEE_DMA_HANDSHAKE_IR_RX`

```c
#define BEE_DMA_HANDSHAKE_IR_RX 40
```

<a id="a55fb1eee56cdfece146fe830727b6b74"></a>

### `BEE_DMA_HANDSHAKE_IR_TX`

```c
#define BEE_DMA_HANDSHAKE_IR_TX 39
```

<a id="a6fb2531f99d489a35901cf1147fd2269"></a>

### `BEE_DMA_HANDSHAKE_PUB_KEY_RX`

```c
#define BEE_DMA_HANDSHAKE_PUB_KEY_RX 50
```

<a id="a62b7e0985a99a1f616e8bf8d035248f1"></a>

### `BEE_DMA_HANDSHAKE_PUB_KEY_TX`

```c
#define BEE_DMA_HANDSHAKE_PUB_KEY_TX 49
```

<a id="af068f66f49e230ef003db06d321c7b31"></a>

### `BEE_DMA_HANDSHAKE_SHA256_TX`

```c
#define BEE_DMA_HANDSHAKE_SHA256_TX 45
```

<a id="abba2dba81a7a9de51542ebd3477433b7"></a>

### `BEE_DMA_HANDSHAKE_SPI0_RX`

```c
#define BEE_DMA_HANDSHAKE_SPI0_RX 17
```

<a id="a3374f6ce3ad11f81574e879a12e18ad6"></a>

### `BEE_DMA_HANDSHAKE_SPI0_TX`

```c
#define BEE_DMA_HANDSHAKE_SPI0_TX 16
```

<a id="a52f8b93db8e706525041e886864c8d18"></a>

### `BEE_DMA_HANDSHAKE_SPI1_RX`

```c
#define BEE_DMA_HANDSHAKE_SPI1_RX 19
```

<a id="a36dd9c37f902e1a8645f65025669a865"></a>

### `BEE_DMA_HANDSHAKE_SPI1_TX`

```c
#define BEE_DMA_HANDSHAKE_SPI1_TX 18
```

<a id="a78907f940c34441814c7fb87983845ef"></a>

### `BEE_DMA_HANDSHAKE_SPI_SLAVE_RX`

```c
#define BEE_DMA_HANDSHAKE_SPI_SLAVE_RX 21
```

<a id="a51a2ae048f2305a7c847a7f7c3cf7a47"></a>

### `BEE_DMA_HANDSHAKE_SPI_SLAVE_TX`

```c
#define BEE_DMA_HANDSHAKE_SPI_SLAVE_TX 20
```

<a id="abfff852e7f9ce88693d78c0ab71e0f97"></a>

### `BEE_DMA_HANDSHAKE_SPIC0_RX`

```c
#define BEE_DMA_HANDSHAKE_SPIC0_RX 34
```

<a id="ad90e978b32dc8825eb3fb265eeef446c"></a>

### `BEE_DMA_HANDSHAKE_SPIC0_TX`

```c
#define BEE_DMA_HANDSHAKE_SPIC0_TX 33
```

<a id="a2b42833e6b685a4415f3c96ccf038e71"></a>

### `BEE_DMA_HANDSHAKE_SPIC1_RX`

```c
#define BEE_DMA_HANDSHAKE_SPIC1_RX 36
```

<a id="a983fa4d96793585a416aebacd0d04c07"></a>

### `BEE_DMA_HANDSHAKE_SPIC1_TX`

```c
#define BEE_DMA_HANDSHAKE_SPIC1_TX 35
```

<a id="a7bffecab9a08289a4a5a4268e7b87e20"></a>

### `BEE_DMA_HANDSHAKE_SPIC2_RX`

```c
#define BEE_DMA_HANDSHAKE_SPIC2_RX 38
```

<a id="a866d3ccc7095de5da4ded14d8279660d"></a>

### `BEE_DMA_HANDSHAKE_SPIC2_TX`

```c
#define BEE_DMA_HANDSHAKE_SPIC2_TX 37
```

<a id="aec47cd5538f9fc57a3a19956807d5cbb"></a>

### `BEE_DMA_HANDSHAKE_TIM5`

```c
#define BEE_DMA_HANDSHAKE_TIM5 29
```

<a id="a5170abd32ff447827cea0b47973d5e41"></a>

### `BEE_DMA_HANDSHAKE_TIM6`

```c
#define BEE_DMA_HANDSHAKE_TIM6 30
```

<a id="aefafec8ed627f094f65841e91fdd4326"></a>

### `BEE_DMA_HANDSHAKE_TIM7`

```c
#define BEE_DMA_HANDSHAKE_TIM7 31
```

<a id="a22dbbef8ff428ff33b5a25cdd9722c20"></a>

### `BEE_DMA_HANDSHAKE_UART0_RX`

```c
#define BEE_DMA_HANDSHAKE_UART0_RX 1
```

<a id="a0d0dff917b561c89b56aa7bd65a0fc29"></a>

### `BEE_DMA_HANDSHAKE_UART0_TX`

```c
#define BEE_DMA_HANDSHAKE_UART0_TX 0
```

<a id="aba1f436a24daafa2b29d33464c11a87c"></a>

### `BEE_DMA_HANDSHAKE_UART1_RX`

```c
#define BEE_DMA_HANDSHAKE_UART1_RX 3
```

<a id="a3c2e0f845b446f2992f4c319ef37a73e"></a>

### `BEE_DMA_HANDSHAKE_UART1_TX`

```c
#define BEE_DMA_HANDSHAKE_UART1_TX 2
```

<a id="afc4d11ad22bb1d7dc558ebb381a14b70"></a>

### `BEE_DMA_HANDSHAKE_UART2_RX`

```c
#define BEE_DMA_HANDSHAKE_UART2_RX 5
```

<a id="ae2490513dad456ea021f36b9ac9a14ed"></a>

### `BEE_DMA_HANDSHAKE_UART2_TX`

```c
#define BEE_DMA_HANDSHAKE_UART2_TX 4
```

<a id="aa32d4c957a1cab2b2609300d4ccc59dc"></a>

### `BEE_DMA_HANDSHAKE_UART3_RX`

```c
#define BEE_DMA_HANDSHAKE_UART3_RX 7
```

<a id="a0480c2867cc1e3f2ed28a45a420f8107"></a>

### `BEE_DMA_HANDSHAKE_UART3_TX`

```c
#define BEE_DMA_HANDSHAKE_UART3_TX 6
```

<a id="aab8e42445c3f5244f158970cf8358f4f"></a>

### `BEE_DMA_HANDSHAKE_UART4_RX`

```c
#define BEE_DMA_HANDSHAKE_UART4_RX 53
```

<a id="a44b1678113587fc4ebaab28311cf6037"></a>

### `BEE_DMA_HANDSHAKE_UART4_TX`

```c
#define BEE_DMA_HANDSHAKE_UART4_TX 52
```

<a id="ae9f8c55be1d2780571a7b1dcc127f2ae"></a>

### `BEE_DMA_HANDSHAKE_UART5_RX`

```c
#define BEE_DMA_HANDSHAKE_UART5_RX 55
```

<a id="a5a238593f285b16cbcfe612038c1bdfa"></a>

### `BEE_DMA_HANDSHAKE_UART5_TX`

```c
#define BEE_DMA_HANDSHAKE_UART5_TX 54
```


## 102.3\_原页交叉引用（Cross References）

- [bee-dma.h](https://docs.zephyrproject.org/latest/doxygen/html/bee-dma_8h_source.html)
- [查看此文件的源码。](../api_source_supplement_reference/P172_rtl87x2g-dma.h_源码浏览.md)
- [dt-bindings/dma/bee-dma.h](P006_zephyr__dt-bindings__dma__bee-dma.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P101_zephyr__dt-bindings__dma__rtl8752h-dma.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P103_zephyr__drivers__flash__rts5912_flash_api_ex.h_文件参考.md)
