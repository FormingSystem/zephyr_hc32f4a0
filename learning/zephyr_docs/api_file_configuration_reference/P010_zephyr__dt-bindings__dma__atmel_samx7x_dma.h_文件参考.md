---
id: learning.zephyr-docs.api-file-configuration-reference.page-10
title: zephyr__dt-bindings__dma__atmel_samx7x_dma.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/atmel__samx7x__dma_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_zephyr\_\_dt-bindings\_\_dma\_\_atmel\_samx7x\_dma.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/atmel__samx7x__dma_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 10.1\_宏定义（Macros）

<a id="r_a16b9db1626b4418e0774654c8e261f64"></a>

```c
#define DMA_PERID_HSMCI_TX_RX 0
```

相关声明：[DMA_PERID_HSMCI_TX_RX](#a16b9db1626b4418e0774654c8e261f64)。

Atmel SAMx7x 外设硬件请求接口编号（Peripheral Hardware Request HW Interface Number，`XDMAC_CC.PERID`）。

<a id="r_a2f87d5b1454bedeb193a2f1fe7dc4cfe"></a>

```c
#define DMA_PERID_SPI0_TX 1
```

相关声明：[DMA_PERID_SPI0_TX](#a2f87d5b1454bedeb193a2f1fe7dc4cfe)。

<a id="r_a31d146fb80a3a2cf2555cf23c1e76200"></a>

```c
#define DMA_PERID_SPI0_RX 2
```

相关声明：[DMA_PERID_SPI0_RX](#a31d146fb80a3a2cf2555cf23c1e76200)。

<a id="r_a35c0ef0b43ac8c255a1e604f178fb902"></a>

```c
#define DMA_PERID_SPI1_TX 3
```

相关声明：[DMA_PERID_SPI1_TX](#a35c0ef0b43ac8c255a1e604f178fb902)。

<a id="r_a5f31ebe4c7df32c83c80edf4d5a80f44"></a>

```c
#define DMA_PERID_SPI1_RX 4
```

相关声明：[DMA_PERID_SPI1_RX](#a5f31ebe4c7df32c83c80edf4d5a80f44)。

<a id="r_a8a7c3f53823d8b3522cbdbac0de7d329"></a>

```c
#define DMA_PERID_QSPI_TX 5
```

相关声明：[DMA_PERID_QSPI_TX](#a8a7c3f53823d8b3522cbdbac0de7d329)。

<a id="r_ac6df1a66062601ea550f7ede74bacc42"></a>

```c
#define DMA_PERID_QSPI_RX 6
```

相关声明：[DMA_PERID_QSPI_RX](#ac6df1a66062601ea550f7ede74bacc42)。

<a id="r_ab42cb0cfbf34517f6419594b80347887"></a>

```c
#define DMA_PERID_USART0_TX 7
```

相关声明：[DMA_PERID_USART0_TX](#ab42cb0cfbf34517f6419594b80347887)。

<a id="r_ab19aafb19b352c6568f5980afdbe51c1"></a>

```c
#define DMA_PERID_USART0_RX 8
```

相关声明：[DMA_PERID_USART0_RX](#ab19aafb19b352c6568f5980afdbe51c1)。

<a id="r_ad0101a8a5c7bef36f742d0990f7f478a"></a>

```c
#define DMA_PERID_USART1_TX 9
```

相关声明：[DMA_PERID_USART1_TX](#ad0101a8a5c7bef36f742d0990f7f478a)。

<a id="r_a2d57240e7a8aa6f0fcd72272fb7d7aa5"></a>

```c
#define DMA_PERID_USART1_RX 10
```

相关声明：[DMA_PERID_USART1_RX](#a2d57240e7a8aa6f0fcd72272fb7d7aa5)。

<a id="r_a46f5b9b287b14852470eb6a0bfa9d290"></a>

```c
#define DMA_PERID_USART2_TX 11
```

相关声明：[DMA_PERID_USART2_TX](#a46f5b9b287b14852470eb6a0bfa9d290)。

<a id="r_a81598c830b204221143c2639dea45e5b"></a>

```c
#define DMA_PERID_USART2_RX 12
```

相关声明：[DMA_PERID_USART2_RX](#a81598c830b204221143c2639dea45e5b)。

<a id="r_a21a595d27913d4eda1596f68746c4b0f"></a>

```c
#define DMA_PERID_PWM0_TX 13
```

相关声明：[DMA_PERID_PWM0_TX](#a21a595d27913d4eda1596f68746c4b0f)。

<a id="r_a318c47d196be9c19d2ddb812c4ec3498"></a>

```c
#define DMA_PERID_TWIHS0_TX 14
```

相关声明：[DMA_PERID_TWIHS0_TX](#a318c47d196be9c19d2ddb812c4ec3498)。

<a id="r_a7b9a87a4999796fb4c400f310a269230"></a>

```c
#define DMA_PERID_TWIHS0_RX 15
```

相关声明：[DMA_PERID_TWIHS0_RX](#a7b9a87a4999796fb4c400f310a269230)。

<a id="r_a352930e4210499b7e54156a2d801a0ef"></a>

```c
#define DMA_PERID_TWIHS1_TX 16
```

相关声明：[DMA_PERID_TWIHS1_TX](#a352930e4210499b7e54156a2d801a0ef)。

<a id="r_a6f8be5d3b2e8905e1b347e1d32a8398b"></a>

```c
#define DMA_PERID_TWIHS1_RX 17
```

相关声明：[DMA_PERID_TWIHS1_RX](#a6f8be5d3b2e8905e1b347e1d32a8398b)。

<a id="r_a9844a87e669d8262dfe2bec5849808fa"></a>

```c
#define DMA_PERID_TWIHS2_TX 18
```

相关声明：[DMA_PERID_TWIHS2_TX](#a9844a87e669d8262dfe2bec5849808fa)。

<a id="r_a7442891a0d70641ccf2a758a43a139bf"></a>

```c
#define DMA_PERID_TWIHS2_RX 19
```

相关声明：[DMA_PERID_TWIHS2_RX](#a7442891a0d70641ccf2a758a43a139bf)。

<a id="r_a18b3089708ac30eed659c2b5d92750d2"></a>

```c
#define DMA_PERID_UART0_TX 20
```

相关声明：[DMA_PERID_UART0_TX](#a18b3089708ac30eed659c2b5d92750d2)。

<a id="r_ab3d7a4ba7f32af80e912b4725e4dde46"></a>

```c
#define DMA_PERID_UART0_RX 21
```

相关声明：[DMA_PERID_UART0_RX](#ab3d7a4ba7f32af80e912b4725e4dde46)。

<a id="r_a4c8e41936578a3a31d26b35a0e7aaabd"></a>

```c
#define DMA_PERID_UART1_TX 22
```

相关声明：[DMA_PERID_UART1_TX](#a4c8e41936578a3a31d26b35a0e7aaabd)。

<a id="r_aaee887dbaed83e0a2941f49c70055d11"></a>

```c
#define DMA_PERID_UART1_RX 23
```

相关声明：[DMA_PERID_UART1_RX](#aaee887dbaed83e0a2941f49c70055d11)。

<a id="r_ad95ff1702d73c3037996e4f67a4c6fe9"></a>

```c
#define DMA_PERID_UART2_TX 24
```

相关声明：[DMA_PERID_UART2_TX](#ad95ff1702d73c3037996e4f67a4c6fe9)。

<a id="r_a627cb308b8a264cae72de25b660e227a"></a>

```c
#define DMA_PERID_UART2_RX 25
```

相关声明：[DMA_PERID_UART2_RX](#a627cb308b8a264cae72de25b660e227a)。

<a id="r_a64e1c5cb19554e0503c3da0be1d3f4bd"></a>

```c
#define DMA_PERID_UART3_TX 26
```

相关声明：[DMA_PERID_UART3_TX](#a64e1c5cb19554e0503c3da0be1d3f4bd)。

<a id="r_ae1baa3ad5ea51d2ce29bb6451fe3ab44"></a>

```c
#define DMA_PERID_UART3_RX 27
```

相关声明：[DMA_PERID_UART3_RX](#ae1baa3ad5ea51d2ce29bb6451fe3ab44)。

<a id="r_a3cfd9eac3ca3e7f4698464d6eb415594"></a>

```c
#define DMA_PERID_UART4_TX 28
```

相关声明：[DMA_PERID_UART4_TX](#a3cfd9eac3ca3e7f4698464d6eb415594)。

<a id="r_ad271c0d6a58e2228624b5d3ede5e4567"></a>

```c
#define DMA_PERID_UART4_RX 29
```

相关声明：[DMA_PERID_UART4_RX](#ad271c0d6a58e2228624b5d3ede5e4567)。

<a id="r_a82778d2873c0caa278d415ff43ec1793"></a>

```c
#define DMA_PERID_DACC0_TX 30
```

相关声明：[DMA_PERID_DACC0_TX](#a82778d2873c0caa278d415ff43ec1793)。

<a id="r_a54f9ae36524cd8c627467b86ec18d9a7"></a>

```c
#define DMA_PERID_DACC1_TX 31
```

相关声明：[DMA_PERID_DACC1_TX](#a54f9ae36524cd8c627467b86ec18d9a7)。

<a id="r_a49b223e1003aaeb74f48d78ea0ea4eba"></a>

```c
#define DMA_PERID_SSC_TX 32
```

相关声明：[DMA_PERID_SSC_TX](#a49b223e1003aaeb74f48d78ea0ea4eba)。

<a id="r_a4846fd126b4dddb9f8bff16235212b9d"></a>

```c
#define DMA_PERID_SSC_RX 33
```

相关声明：[DMA_PERID_SSC_RX](#a4846fd126b4dddb9f8bff16235212b9d)。

<a id="r_a171d85b6ef14e6ade18095920a1dc2e6"></a>

```c
#define DMA_PERID_PIOA_RX 34
```

相关声明：[DMA_PERID_PIOA_RX](#a171d85b6ef14e6ade18095920a1dc2e6)。

<a id="r_a6c861baaeac3fc444ad910dc164bed6d"></a>

```c
#define DMA_PERID_AFEC0_RX 35
```

相关声明：[DMA_PERID_AFEC0_RX](#a6c861baaeac3fc444ad910dc164bed6d)。

<a id="r_abdfa1c39e23390d4e3b4cc8f96c59aa7"></a>

```c
#define DMA_PERID_AFEC1_RX 36
```

相关声明：[DMA_PERID_AFEC1_RX](#abdfa1c39e23390d4e3b4cc8f96c59aa7)。

<a id="r_a0a1c2d866f4ff93fc2bb0ae30bdb3b68"></a>

```c
#define DMA_PERID_AES_TX 37
```

相关声明：[DMA_PERID_AES_TX](#a0a1c2d866f4ff93fc2bb0ae30bdb3b68)。

<a id="r_a356fac72c01bdb8e54801b9c5e823f24"></a>

```c
#define DMA_PERID_AES_RX 38
```

相关声明：[DMA_PERID_AES_RX](#a356fac72c01bdb8e54801b9c5e823f24)。

<a id="r_a398615ec6af12d0cae7a28ce994b7d8c"></a>

```c
#define DMA_PERID_PWM1_TX 39
```

相关声明：[DMA_PERID_PWM1_TX](#a398615ec6af12d0cae7a28ce994b7d8c)。

<a id="r_a1cb3a2a18f35cb3696a290e11c0dd509"></a>

```c
#define DMA_PERID_TC0_RX 40
```

相关声明：[DMA_PERID_TC0_RX](#a1cb3a2a18f35cb3696a290e11c0dd509)。

<a id="r_a164b686731864358c6b261de0d9d54d2"></a>

```c
#define DMA_PERID_TC1_RX 41
```

相关声明：[DMA_PERID_TC1_RX](#a164b686731864358c6b261de0d9d54d2)。

<a id="r_ab9f6c37c8c74e1bdaff88ddd759bd63b"></a>

```c
#define DMA_PERID_TC2_RX 42
```

相关声明：[DMA_PERID_TC2_RX](#ab9f6c37c8c74e1bdaff88ddd759bd63b)。

<a id="r_a2b65b2d22441cd584e0a6050721794b4"></a>

```c
#define DMA_PERID_TC3_RX 43
```

相关声明：[DMA_PERID_TC3_RX](#a2b65b2d22441cd584e0a6050721794b4)。

<a id="r_a87bd80dfa6786745ce059d27ad092eed"></a>

```c
#define DMA_PERID_I2SC0_TX_L 44
```

相关声明：[DMA_PERID_I2SC0_TX_L](#a87bd80dfa6786745ce059d27ad092eed)。

<a id="r_ae839fe5acfd05bb968080e6ac09f7310"></a>

```c
#define DMA_PERID_I2SC0_RX_L 45
```

相关声明：[DMA_PERID_I2SC0_RX_L](#ae839fe5acfd05bb968080e6ac09f7310)。

<a id="r_ae0c680dfe9170a6f3e1bff2ac4c2a0a2"></a>

```c
#define DMA_PERID_I2SC1_TX_L 46
```

相关声明：[DMA_PERID_I2SC1_TX_L](#ae0c680dfe9170a6f3e1bff2ac4c2a0a2)。

<a id="r_a750f991645276c40f01d243718cc3e91"></a>

```c
#define DMA_PERID_I2SC1_RX_L 47
```

相关声明：[DMA_PERID_I2SC1_RX_L](#a750f991645276c40f01d243718cc3e91)。

<a id="r_a3f82e5ff16160265557fb465420c3692"></a>

```c
#define DMA_PERID_I2SC0_TX_R 48
```

相关声明：[DMA_PERID_I2SC0_TX_R](#a3f82e5ff16160265557fb465420c3692)。

<a id="r_a55e59763d73f4cb0007537f7878d700c"></a>

```c
#define DMA_PERID_I2SC0_RX_R 49
```

相关声明：[DMA_PERID_I2SC0_RX_R](#a55e59763d73f4cb0007537f7878d700c)。

<a id="r_a258877cef3fafb77e0ad645ee0ecdc26"></a>

```c
#define DMA_PERID_I2SC1_TX_R 50
```

相关声明：[DMA_PERID_I2SC1_TX_R](#a258877cef3fafb77e0ad645ee0ecdc26)。

<a id="r_ae16dcc6df4f58f3c15fd502b9a6ea731"></a>

```c
#define DMA_PERID_I2SC1_RX_R 51
```

相关声明：[DMA_PERID_I2SC1_RX_R](#ae16dcc6df4f58f3c15fd502b9a6ea731)。

## 10.2\_详细说明（Detailed Documentation）

<a id="a356fac72c01bdb8e54801b9c5e823f24"></a>

### `DMA_PERID_AES_RX`

```c
#define DMA_PERID_AES_RX 38
```

<a id="a0a1c2d866f4ff93fc2bb0ae30bdb3b68"></a>

### `DMA_PERID_AES_TX`

```c
#define DMA_PERID_AES_TX 37
```

<a id="a6c861baaeac3fc444ad910dc164bed6d"></a>

### `DMA_PERID_AFEC0_RX`

```c
#define DMA_PERID_AFEC0_RX 35
```

<a id="abdfa1c39e23390d4e3b4cc8f96c59aa7"></a>

### `DMA_PERID_AFEC1_RX`

```c
#define DMA_PERID_AFEC1_RX 36
```

<a id="a82778d2873c0caa278d415ff43ec1793"></a>

### `DMA_PERID_DACC0_TX`

```c
#define DMA_PERID_DACC0_TX 30
```

<a id="a54f9ae36524cd8c627467b86ec18d9a7"></a>

### `DMA_PERID_DACC1_TX`

```c
#define DMA_PERID_DACC1_TX 31
```

<a id="a16b9db1626b4418e0774654c8e261f64"></a>

### `DMA_PERID_HSMCI_TX_RX`

```c
#define DMA_PERID_HSMCI_TX_RX 0
```

Atmel SAMx7x 外设硬件请求接口编号（Peripheral Hardware Request HW Interface Number，`XDMAC_CC.PERID`）。

参见 SAM E70/S70/V70/V71 数据手册中的表 35-1“外设硬件请求（Peripheral Hardware Requests）”。

<a id="ae839fe5acfd05bb968080e6ac09f7310"></a>

### `DMA_PERID_I2SC0_RX_L`

```c
#define DMA_PERID_I2SC0_RX_L 45
```

<a id="a55e59763d73f4cb0007537f7878d700c"></a>

### `DMA_PERID_I2SC0_RX_R`

```c
#define DMA_PERID_I2SC0_RX_R 49
```

<a id="a87bd80dfa6786745ce059d27ad092eed"></a>

### `DMA_PERID_I2SC0_TX_L`

```c
#define DMA_PERID_I2SC0_TX_L 44
```

<a id="a3f82e5ff16160265557fb465420c3692"></a>

### `DMA_PERID_I2SC0_TX_R`

```c
#define DMA_PERID_I2SC0_TX_R 48
```

<a id="a750f991645276c40f01d243718cc3e91"></a>

### `DMA_PERID_I2SC1_RX_L`

```c
#define DMA_PERID_I2SC1_RX_L 47
```

<a id="ae16dcc6df4f58f3c15fd502b9a6ea731"></a>

### `DMA_PERID_I2SC1_RX_R`

```c
#define DMA_PERID_I2SC1_RX_R 51
```

<a id="ae0c680dfe9170a6f3e1bff2ac4c2a0a2"></a>

### `DMA_PERID_I2SC1_TX_L`

```c
#define DMA_PERID_I2SC1_TX_L 46
```

<a id="a258877cef3fafb77e0ad645ee0ecdc26"></a>

### `DMA_PERID_I2SC1_TX_R`

```c
#define DMA_PERID_I2SC1_TX_R 50
```

<a id="a171d85b6ef14e6ade18095920a1dc2e6"></a>

### `DMA_PERID_PIOA_RX`

```c
#define DMA_PERID_PIOA_RX 34
```

<a id="a21a595d27913d4eda1596f68746c4b0f"></a>

### `DMA_PERID_PWM0_TX`

```c
#define DMA_PERID_PWM0_TX 13
```

<a id="a398615ec6af12d0cae7a28ce994b7d8c"></a>

### `DMA_PERID_PWM1_TX`

```c
#define DMA_PERID_PWM1_TX 39
```

<a id="ac6df1a66062601ea550f7ede74bacc42"></a>

### `DMA_PERID_QSPI_RX`

```c
#define DMA_PERID_QSPI_RX 6
```

<a id="a8a7c3f53823d8b3522cbdbac0de7d329"></a>

### `DMA_PERID_QSPI_TX`

```c
#define DMA_PERID_QSPI_TX 5
```

<a id="a31d146fb80a3a2cf2555cf23c1e76200"></a>

### `DMA_PERID_SPI0_RX`

```c
#define DMA_PERID_SPI0_RX 2
```

<a id="a2f87d5b1454bedeb193a2f1fe7dc4cfe"></a>

### `DMA_PERID_SPI0_TX`

```c
#define DMA_PERID_SPI0_TX 1
```

<a id="a5f31ebe4c7df32c83c80edf4d5a80f44"></a>

### `DMA_PERID_SPI1_RX`

```c
#define DMA_PERID_SPI1_RX 4
```

<a id="a35c0ef0b43ac8c255a1e604f178fb902"></a>

### `DMA_PERID_SPI1_TX`

```c
#define DMA_PERID_SPI1_TX 3
```

<a id="a4846fd126b4dddb9f8bff16235212b9d"></a>

### `DMA_PERID_SSC_RX`

```c
#define DMA_PERID_SSC_RX 33
```

<a id="a49b223e1003aaeb74f48d78ea0ea4eba"></a>

### `DMA_PERID_SSC_TX`

```c
#define DMA_PERID_SSC_TX 32
```

<a id="a1cb3a2a18f35cb3696a290e11c0dd509"></a>

### `DMA_PERID_TC0_RX`

```c
#define DMA_PERID_TC0_RX 40
```

<a id="a164b686731864358c6b261de0d9d54d2"></a>

### `DMA_PERID_TC1_RX`

```c
#define DMA_PERID_TC1_RX 41
```

<a id="ab9f6c37c8c74e1bdaff88ddd759bd63b"></a>

### `DMA_PERID_TC2_RX`

```c
#define DMA_PERID_TC2_RX 42
```

<a id="a2b65b2d22441cd584e0a6050721794b4"></a>

### `DMA_PERID_TC3_RX`

```c
#define DMA_PERID_TC3_RX 43
```

<a id="a7b9a87a4999796fb4c400f310a269230"></a>

### `DMA_PERID_TWIHS0_RX`

```c
#define DMA_PERID_TWIHS0_RX 15
```

<a id="a318c47d196be9c19d2ddb812c4ec3498"></a>

### `DMA_PERID_TWIHS0_TX`

```c
#define DMA_PERID_TWIHS0_TX 14
```

<a id="a6f8be5d3b2e8905e1b347e1d32a8398b"></a>

### `DMA_PERID_TWIHS1_RX`

```c
#define DMA_PERID_TWIHS1_RX 17
```

<a id="a352930e4210499b7e54156a2d801a0ef"></a>

### `DMA_PERID_TWIHS1_TX`

```c
#define DMA_PERID_TWIHS1_TX 16
```

<a id="a7442891a0d70641ccf2a758a43a139bf"></a>

### `DMA_PERID_TWIHS2_RX`

```c
#define DMA_PERID_TWIHS2_RX 19
```

<a id="a9844a87e669d8262dfe2bec5849808fa"></a>

### `DMA_PERID_TWIHS2_TX`

```c
#define DMA_PERID_TWIHS2_TX 18
```

<a id="ab3d7a4ba7f32af80e912b4725e4dde46"></a>

### `DMA_PERID_UART0_RX`

```c
#define DMA_PERID_UART0_RX 21
```

<a id="a18b3089708ac30eed659c2b5d92750d2"></a>

### `DMA_PERID_UART0_TX`

```c
#define DMA_PERID_UART0_TX 20
```

<a id="aaee887dbaed83e0a2941f49c70055d11"></a>

### `DMA_PERID_UART1_RX`

```c
#define DMA_PERID_UART1_RX 23
```

<a id="a4c8e41936578a3a31d26b35a0e7aaabd"></a>

### `DMA_PERID_UART1_TX`

```c
#define DMA_PERID_UART1_TX 22
```

<a id="a627cb308b8a264cae72de25b660e227a"></a>

### `DMA_PERID_UART2_RX`

```c
#define DMA_PERID_UART2_RX 25
```

<a id="ad95ff1702d73c3037996e4f67a4c6fe9"></a>

### `DMA_PERID_UART2_TX`

```c
#define DMA_PERID_UART2_TX 24
```

<a id="ae1baa3ad5ea51d2ce29bb6451fe3ab44"></a>

### `DMA_PERID_UART3_RX`

```c
#define DMA_PERID_UART3_RX 27
```

<a id="a64e1c5cb19554e0503c3da0be1d3f4bd"></a>

### `DMA_PERID_UART3_TX`

```c
#define DMA_PERID_UART3_TX 26
```

<a id="ad271c0d6a58e2228624b5d3ede5e4567"></a>

### `DMA_PERID_UART4_RX`

```c
#define DMA_PERID_UART4_RX 29
```

<a id="a3cfd9eac3ca3e7f4698464d6eb415594"></a>

### `DMA_PERID_UART4_TX`

```c
#define DMA_PERID_UART4_TX 28
```

<a id="ab19aafb19b352c6568f5980afdbe51c1"></a>

### `DMA_PERID_USART0_RX`

```c
#define DMA_PERID_USART0_RX 8
```

<a id="ab42cb0cfbf34517f6419594b80347887"></a>

### `DMA_PERID_USART0_TX`

```c
#define DMA_PERID_USART0_TX 7
```

<a id="a2d57240e7a8aa6f0fcd72272fb7d7aa5"></a>

### `DMA_PERID_USART1_RX`

```c
#define DMA_PERID_USART1_RX 10
```

<a id="ad0101a8a5c7bef36f742d0990f7f478a"></a>

### `DMA_PERID_USART1_TX`

```c
#define DMA_PERID_USART1_TX 9
```

<a id="a81598c830b204221143c2639dea45e5b"></a>

### `DMA_PERID_USART2_RX`

```c
#define DMA_PERID_USART2_RX 12
```

<a id="a46f5b9b287b14852470eb6a0bfa9d290"></a>

### `DMA_PERID_USART2_TX`

```c
#define DMA_PERID_USART2_TX 11
```


## 10.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P045_atmel_samx7x_dma.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P009_zephyr__dt-bindings__gpio__atmel-sam-gpio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P011_zephyr__drivers__sensor__bmm350.h_文件参考.md)
