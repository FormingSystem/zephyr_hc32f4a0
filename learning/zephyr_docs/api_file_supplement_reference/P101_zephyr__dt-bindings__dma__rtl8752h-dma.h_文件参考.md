---
id: learning.zephyr-docs.api-file-supplement-reference.page-101
title: zephyr__dt-bindings__dma__rtl8752h-dma.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rtl8752h-dma_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第101章\_zephyr\_\_dt-bindings\_\_dma\_\_rtl8752h-dma.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/rtl8752h-dma_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

RTL8752H DMA的设备树绑定（Devicetree Bindings）。

<a id="details"></a>

```c
#include "bee-dma.h"
```

查看此文件的源码。

RTL8752H DMA 设备树绑定（Devicetree Bindings）。RTL8752H 通用 DMA 控制器（GDMA Controller）的握手槽位标识（Handshake / Slot IDs）。取值与硬件抽象层（HAL）的 `rtl876x_gdma.h` 中的 `GDMA_Handshake_*` 定义一致。请在 `slot` 单元中使用这些标识，并搭配 `<dt-bindings/dma/bee-dma.h>` 中的 `config` 单元宏。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 101.1\_宏定义（Macros）

<a id="r_a3c2e0f845b446f2992f4c319ef37a73e"></a>

```c
#define BEE_DMA_HANDSHAKE_UART1_TX 0
```

相关声明：[BEE_DMA_HANDSHAKE_UART1_TX](#a3c2e0f845b446f2992f4c319ef37a73e)。

<a id="r_aba1f436a24daafa2b29d33464c11a87c"></a>

```c
#define BEE_DMA_HANDSHAKE_UART1_RX 1
```

相关声明：[BEE_DMA_HANDSHAKE_UART1_RX](#aba1f436a24daafa2b29d33464c11a87c)。

<a id="r_a4c7617163f6d4a6621295c92aa402162"></a>

```c
#define BEE_DMA_HANDSHAKE_ENH_TIM0 2
```

相关声明：[BEE_DMA_HANDSHAKE_ENH_TIM0](#a4c7617163f6d4a6621295c92aa402162)。

<a id="r_aacb722354a323c5111c963eee20362f9"></a>

```c
#define BEE_DMA_HANDSHAKE_ENH_TIM1 3
```

相关声明：[BEE_DMA_HANDSHAKE_ENH_TIM1](#aacb722354a323c5111c963eee20362f9)。

<a id="r_a3374f6ce3ad11f81574e879a12e18ad6"></a>

```c
#define BEE_DMA_HANDSHAKE_SPI0_TX 4
```

相关声明：[BEE_DMA_HANDSHAKE_SPI0_TX](#a3374f6ce3ad11f81574e879a12e18ad6)。

<a id="r_abba2dba81a7a9de51542ebd3477433b7"></a>

```c
#define BEE_DMA_HANDSHAKE_SPI0_RX 5
```

相关声明：[BEE_DMA_HANDSHAKE_SPI0_RX](#abba2dba81a7a9de51542ebd3477433b7)。

<a id="r_a36dd9c37f902e1a8645f65025669a865"></a>

```c
#define BEE_DMA_HANDSHAKE_SPI1_TX 6
```

相关声明：[BEE_DMA_HANDSHAKE_SPI1_TX](#a36dd9c37f902e1a8645f65025669a865)。

<a id="r_a52f8b93db8e706525041e886864c8d18"></a>

```c
#define BEE_DMA_HANDSHAKE_SPI1_RX 7
```

相关声明：[BEE_DMA_HANDSHAKE_SPI1_RX](#a52f8b93db8e706525041e886864c8d18)。

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

<a id="r_a0b53b47743db4439f63e3ff80fcf4283"></a>

```c
#define BEE_DMA_HANDSHAKE_ADC 12
```

相关声明：[BEE_DMA_HANDSHAKE_ADC](#a0b53b47743db4439f63e3ff80fcf4283)。

<a id="r_a675b77d5fbc83426774372c7e5bc5326"></a>

```c
#define BEE_DMA_HANDSHAKE_AES_TX 13
```

相关声明：[BEE_DMA_HANDSHAKE_AES_TX](#a675b77d5fbc83426774372c7e5bc5326)。

<a id="r_a6088046bfb66874b5a25ae3b8ec7103e"></a>

```c
#define BEE_DMA_HANDSHAKE_AES_RX 14
```

相关声明：[BEE_DMA_HANDSHAKE_AES_RX](#a6088046bfb66874b5a25ae3b8ec7103e)。

<a id="r_a0d0dff917b561c89b56aa7bd65a0fc29"></a>

```c
#define BEE_DMA_HANDSHAKE_UART0_TX 15
```

相关声明：[BEE_DMA_HANDSHAKE_UART0_TX](#a0d0dff917b561c89b56aa7bd65a0fc29)。

<a id="r_a96cbbfcfcdd3880706fa716602b105da"></a>

```c
#define BEE_DMA_HANDSHAKE_I2S0_TX 16
```

相关声明：[BEE_DMA_HANDSHAKE_I2S0_TX](#a96cbbfcfcdd3880706fa716602b105da)。

<a id="r_a4af7975dcb7e6a869600a4a98f72167d"></a>

```c
#define BEE_DMA_HANDSHAKE_I2S0_RX 17
```

相关声明：[BEE_DMA_HANDSHAKE_I2S0_RX](#a4af7975dcb7e6a869600a4a98f72167d)。

<a id="r_ae2490513dad456ea021f36b9ac9a14ed"></a>

```c
#define BEE_DMA_HANDSHAKE_UART2_TX 18
```

相关声明：[BEE_DMA_HANDSHAKE_UART2_TX](#ae2490513dad456ea021f36b9ac9a14ed)。

<a id="r_afc4d11ad22bb1d7dc558ebb381a14b70"></a>

```c
#define BEE_DMA_HANDSHAKE_UART2_RX 19
```

相关声明：[BEE_DMA_HANDSHAKE_UART2_RX](#afc4d11ad22bb1d7dc558ebb381a14b70)。

<a id="r_ad90e978b32dc8825eb3fb265eeef446c"></a>

```c
#define BEE_DMA_HANDSHAKE_SPIC0_TX 20
```

相关声明：[BEE_DMA_HANDSHAKE_SPIC0_TX](#ad90e978b32dc8825eb3fb265eeef446c)。

<a id="r_abfff852e7f9ce88693d78c0ab71e0f97"></a>

```c
#define BEE_DMA_HANDSHAKE_SPIC0_RX 21
```

相关声明：[BEE_DMA_HANDSHAKE_SPIC0_RX](#abfff852e7f9ce88693d78c0ab71e0f97)。

<a id="r_adaf6958348e43da9754fc16663ed489e"></a>

```c
#define BEE_DMA_HANDSHAKE_I8080_RX 22
```

相关声明：[BEE_DMA_HANDSHAKE_I8080_RX](#adaf6958348e43da9754fc16663ed489e)。

<a id="r_a22dbbef8ff428ff33b5a25cdd9722c20"></a>

```c
#define BEE_DMA_HANDSHAKE_UART0_RX 23
```

相关声明：[BEE_DMA_HANDSHAKE_UART0_RX](#a22dbbef8ff428ff33b5a25cdd9722c20)。

<a id="r_ace4178dd542fe34fde7e14d3a1f38021"></a>

```c
#define BEE_DMA_HANDSHAKE_TIM0 24
```

相关声明：[BEE_DMA_HANDSHAKE_TIM0](#ace4178dd542fe34fde7e14d3a1f38021)。

<a id="r_a565de9864ec164494dd1185c2a4fc600"></a>

```c
#define BEE_DMA_HANDSHAKE_TIM1 25
```

相关声明：[BEE_DMA_HANDSHAKE_TIM1](#a565de9864ec164494dd1185c2a4fc600)。

<a id="r_a4038507acbe3c66ddeca91d74dc8490a"></a>

```c
#define BEE_DMA_HANDSHAKE_TIM2 26
```

相关声明：[BEE_DMA_HANDSHAKE_TIM2](#a4038507acbe3c66ddeca91d74dc8490a)。

<a id="r_a55fb1eee56cdfece146fe830727b6b74"></a>

```c
#define BEE_DMA_HANDSHAKE_IR_TX 27
```

相关声明：[BEE_DMA_HANDSHAKE_IR_TX](#a55fb1eee56cdfece146fe830727b6b74)。

<a id="r_a817500f56cc164220e316b328b70522d"></a>

```c
#define BEE_DMA_HANDSHAKE_IR_RX 28
```

相关声明：[BEE_DMA_HANDSHAKE_IR_RX](#a817500f56cc164220e316b328b70522d)。

<a id="r_a131318edd6f94afed3fc9d4916bb9001"></a>

```c
#define BEE_DMA_HANDSHAKE_TIM3 29
```

相关声明：[BEE_DMA_HANDSHAKE_TIM3](#a131318edd6f94afed3fc9d4916bb9001)。

<a id="r_a40c4fc985e5f3ee76a2a91d83f8768c2"></a>

```c
#define BEE_DMA_HANDSHAKE_TIM4 30
```

相关声明：[BEE_DMA_HANDSHAKE_TIM4](#a40c4fc985e5f3ee76a2a91d83f8768c2)。

<a id="r_aec47cd5538f9fc57a3a19956807d5cbb"></a>

```c
#define BEE_DMA_HANDSHAKE_TIM5 31
```

相关声明：[BEE_DMA_HANDSHAKE_TIM5](#aec47cd5538f9fc57a3a19956807d5cbb)。

<a id="r_a983fa4d96793585a416aebacd0d04c07"></a>

```c
#define BEE_DMA_HANDSHAKE_SPIC1_TX 32
```

相关声明：[BEE_DMA_HANDSHAKE_SPIC1_TX](#a983fa4d96793585a416aebacd0d04c07)。

<a id="r_a2b42833e6b685a4415f3c96ccf038e71"></a>

```c
#define BEE_DMA_HANDSHAKE_SPIC1_RX 33
```

相关声明：[BEE_DMA_HANDSHAKE_SPIC1_RX](#a2b42833e6b685a4415f3c96ccf038e71)。

<a id="r_af068f66f49e230ef003db06d321c7b31"></a>

```c
#define BEE_DMA_HANDSHAKE_SHA256_TX 35
```

相关声明：[BEE_DMA_HANDSHAKE_SHA256_TX](#af068f66f49e230ef003db06d321c7b31)。

## 101.2\_详细说明（Detailed Documentation）

<a id="a0b53b47743db4439f63e3ff80fcf4283"></a>

### `BEE_DMA_HANDSHAKE_ADC`

```c
#define BEE_DMA_HANDSHAKE_ADC 12
```

<a id="a6088046bfb66874b5a25ae3b8ec7103e"></a>

### `BEE_DMA_HANDSHAKE_AES_RX`

```c
#define BEE_DMA_HANDSHAKE_AES_RX 14
```

<a id="a675b77d5fbc83426774372c7e5bc5326"></a>

### `BEE_DMA_HANDSHAKE_AES_TX`

```c
#define BEE_DMA_HANDSHAKE_AES_TX 13
```

<a id="a4c7617163f6d4a6621295c92aa402162"></a>

### `BEE_DMA_HANDSHAKE_ENH_TIM0`

```c
#define BEE_DMA_HANDSHAKE_ENH_TIM0 2
```

<a id="aacb722354a323c5111c963eee20362f9"></a>

### `BEE_DMA_HANDSHAKE_ENH_TIM1`

```c
#define BEE_DMA_HANDSHAKE_ENH_TIM1 3
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

<a id="a4af7975dcb7e6a869600a4a98f72167d"></a>

### `BEE_DMA_HANDSHAKE_I2S0_RX`

```c
#define BEE_DMA_HANDSHAKE_I2S0_RX 17
```

<a id="a96cbbfcfcdd3880706fa716602b105da"></a>

### `BEE_DMA_HANDSHAKE_I2S0_TX`

```c
#define BEE_DMA_HANDSHAKE_I2S0_TX 16
```

<a id="adaf6958348e43da9754fc16663ed489e"></a>

### `BEE_DMA_HANDSHAKE_I8080_RX`

```c
#define BEE_DMA_HANDSHAKE_I8080_RX 22
```

<a id="a817500f56cc164220e316b328b70522d"></a>

### `BEE_DMA_HANDSHAKE_IR_RX`

```c
#define BEE_DMA_HANDSHAKE_IR_RX 28
```

<a id="a55fb1eee56cdfece146fe830727b6b74"></a>

### `BEE_DMA_HANDSHAKE_IR_TX`

```c
#define BEE_DMA_HANDSHAKE_IR_TX 27
```

<a id="af068f66f49e230ef003db06d321c7b31"></a>

### `BEE_DMA_HANDSHAKE_SHA256_TX`

```c
#define BEE_DMA_HANDSHAKE_SHA256_TX 35
```

<a id="abba2dba81a7a9de51542ebd3477433b7"></a>

### `BEE_DMA_HANDSHAKE_SPI0_RX`

```c
#define BEE_DMA_HANDSHAKE_SPI0_RX 5
```

<a id="a3374f6ce3ad11f81574e879a12e18ad6"></a>

### `BEE_DMA_HANDSHAKE_SPI0_TX`

```c
#define BEE_DMA_HANDSHAKE_SPI0_TX 4
```

<a id="a52f8b93db8e706525041e886864c8d18"></a>

### `BEE_DMA_HANDSHAKE_SPI1_RX`

```c
#define BEE_DMA_HANDSHAKE_SPI1_RX 7
```

<a id="a36dd9c37f902e1a8645f65025669a865"></a>

### `BEE_DMA_HANDSHAKE_SPI1_TX`

```c
#define BEE_DMA_HANDSHAKE_SPI1_TX 6
```

<a id="abfff852e7f9ce88693d78c0ab71e0f97"></a>

### `BEE_DMA_HANDSHAKE_SPIC0_RX`

```c
#define BEE_DMA_HANDSHAKE_SPIC0_RX 21
```

<a id="ad90e978b32dc8825eb3fb265eeef446c"></a>

### `BEE_DMA_HANDSHAKE_SPIC0_TX`

```c
#define BEE_DMA_HANDSHAKE_SPIC0_TX 20
```

<a id="a2b42833e6b685a4415f3c96ccf038e71"></a>

### `BEE_DMA_HANDSHAKE_SPIC1_RX`

```c
#define BEE_DMA_HANDSHAKE_SPIC1_RX 33
```

<a id="a983fa4d96793585a416aebacd0d04c07"></a>

### `BEE_DMA_HANDSHAKE_SPIC1_TX`

```c
#define BEE_DMA_HANDSHAKE_SPIC1_TX 32
```

<a id="ace4178dd542fe34fde7e14d3a1f38021"></a>

### `BEE_DMA_HANDSHAKE_TIM0`

```c
#define BEE_DMA_HANDSHAKE_TIM0 24
```

<a id="a565de9864ec164494dd1185c2a4fc600"></a>

### `BEE_DMA_HANDSHAKE_TIM1`

```c
#define BEE_DMA_HANDSHAKE_TIM1 25
```

<a id="a4038507acbe3c66ddeca91d74dc8490a"></a>

### `BEE_DMA_HANDSHAKE_TIM2`

```c
#define BEE_DMA_HANDSHAKE_TIM2 26
```

<a id="a131318edd6f94afed3fc9d4916bb9001"></a>

### `BEE_DMA_HANDSHAKE_TIM3`

```c
#define BEE_DMA_HANDSHAKE_TIM3 29
```

<a id="a40c4fc985e5f3ee76a2a91d83f8768c2"></a>

### `BEE_DMA_HANDSHAKE_TIM4`

```c
#define BEE_DMA_HANDSHAKE_TIM4 30
```

<a id="aec47cd5538f9fc57a3a19956807d5cbb"></a>

### `BEE_DMA_HANDSHAKE_TIM5`

```c
#define BEE_DMA_HANDSHAKE_TIM5 31
```

<a id="a22dbbef8ff428ff33b5a25cdd9722c20"></a>

### `BEE_DMA_HANDSHAKE_UART0_RX`

```c
#define BEE_DMA_HANDSHAKE_UART0_RX 23
```

<a id="a0d0dff917b561c89b56aa7bd65a0fc29"></a>

### `BEE_DMA_HANDSHAKE_UART0_TX`

```c
#define BEE_DMA_HANDSHAKE_UART0_TX 15
```

<a id="aba1f436a24daafa2b29d33464c11a87c"></a>

### `BEE_DMA_HANDSHAKE_UART1_RX`

```c
#define BEE_DMA_HANDSHAKE_UART1_RX 1
```

<a id="a3c2e0f845b446f2992f4c319ef37a73e"></a>

### `BEE_DMA_HANDSHAKE_UART1_TX`

```c
#define BEE_DMA_HANDSHAKE_UART1_TX 0
```

<a id="afc4d11ad22bb1d7dc558ebb381a14b70"></a>

### `BEE_DMA_HANDSHAKE_UART2_RX`

```c
#define BEE_DMA_HANDSHAKE_UART2_RX 19
```

<a id="ae2490513dad456ea021f36b9ac9a14ed"></a>

### `BEE_DMA_HANDSHAKE_UART2_TX`

```c
#define BEE_DMA_HANDSHAKE_UART2_TX 18
```


## 101.3\_原页交叉引用（Cross References）

- [bee-dma.h](https://docs.zephyrproject.org/latest/doxygen/html/bee-dma_8h_source.html)
- [查看此文件的源码。](../api_source_supplement_reference/P171_rtl8752h-dma.h_源码浏览.md)
- [dt-bindings/dma/bee-dma.h](P006_zephyr__dt-bindings__dma__bee-dma.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P100_zephyr__bluetooth__mesh__rpr_srv.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P102_zephyr__dt-bindings__dma__rtl87x2g-dma.h_文件参考.md)
