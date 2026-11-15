---
id: learning.zephyr-docs.api-file-input-wake-protocol-reference.page-4
title: zephyr__dt-bindings__pinctrl__lpc84x-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lpc84x-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_lpc84x-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/lpc84x-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

NXP LPC84x引脚控制（Pinctrl）的定义。

查看此文件的源码。

<a id="details"></a>

NXP LPC84x引脚控制（Pinctrl）的定义。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.1\_宏定义（Macros）

<a id="r_acaaf1d2ee32fb366037c7e7e22836f45"></a>

```c
#define LPC84X_PINMUX_M(func, pin)
```

相关声明：[LPC84X_PINMUX_M](#acaaf1d2ee32fb366037c7e7e22836f45)。

将可移动开关矩阵（SWM）功能与引脚值一起编码。

<a id="r_ab0727a736c6bc193fab9e2871e95dea7"></a>

```c
#define LPC84X_PINMUX_F(func, pin)
```

相关声明：[LPC84X_PINMUX_F](#ab0727a736c6bc193fab9e2871e95dea7)。

将固定开关矩阵（SWM）功能与引脚值一起编码。

<a id="r_a508b8cd868aa00345e56cda9448dcc1b"></a>

```c
#define LPC84X_SWM_USART0_TXD 0U
```

相关声明：[LPC84X_SWM_USART0_TXD](#a508b8cd868aa00345e56cda9448dcc1b)。

开关矩阵（SWM）可移动功能索引（Movable Function Indices）。

<a id="r_a6a1f0f6e22ecf53ec38adee7339d732f"></a>

```c
#define LPC84X_SWM_USART0_RXD 1U
```

相关声明：[LPC84X_SWM_USART0_RXD](#a6a1f0f6e22ecf53ec38adee7339d732f)。

USART0 的接收数据信号（RXD）。

<a id="r_a4c6ee732ce8bebdc7783277954fbfa1e"></a>

```c
#define LPC84X_SWM_USART0_RTS 2U
```

相关声明：[LPC84X_SWM_USART0_RTS](#a4c6ee732ce8bebdc7783277954fbfa1e)。

USART0 的请求发送信号（RTS）。

<a id="r_ac03e223d75d42c754079bf6c23efebdc"></a>

```c
#define LPC84X_SWM_USART0_CTS 3U
```

相关声明：[LPC84X_SWM_USART0_CTS](#ac03e223d75d42c754079bf6c23efebdc)。

USART0 的清除发送信号（CTS）。

<a id="r_aa3b6565df20cdceab2454eecc76cf5d6"></a>

```c
#define LPC84X_SWM_USART0_SCLK 4U
```

相关声明：[LPC84X_SWM_USART0_SCLK](#aa3b6565df20cdceab2454eecc76cf5d6)。

USART0 的串行时钟信号（SCLK）。

<a id="r_a468f03e189e270f1468dbfd462c5d66f"></a>

```c
#define LPC84X_SWM_USART1_TXD 5U
```

相关声明：[LPC84X_SWM_USART1_TXD](#a468f03e189e270f1468dbfd462c5d66f)。

USART1 的发送数据信号（TXD）。

<a id="r_a28bd505d91afc679432412aa88087d3a"></a>

```c
#define LPC84X_SWM_USART1_RXD 6U
```

相关声明：[LPC84X_SWM_USART1_RXD](#a28bd505d91afc679432412aa88087d3a)。

USART1 的接收数据信号（RXD）。

<a id="r_a1c1485775ee41d9cb97f128702cfa0d0"></a>

```c
#define LPC84X_SWM_USART1_RTS 7U
```

相关声明：[LPC84X_SWM_USART1_RTS](#a1c1485775ee41d9cb97f128702cfa0d0)。

USART1 的请求发送信号（RTS）。

<a id="r_a7abe086056ab632c7d6035cc158a9d03"></a>

```c
#define LPC84X_SWM_USART1_CTS 8U
```

相关声明：[LPC84X_SWM_USART1_CTS](#a7abe086056ab632c7d6035cc158a9d03)。

USART1 的清除发送信号（CTS）。

<a id="r_a4ad65a41da1576f1981e9e842fbb91ec"></a>

```c
#define LPC84X_SWM_USART1_SCLK 9U
```

相关声明：[LPC84X_SWM_USART1_SCLK](#a4ad65a41da1576f1981e9e842fbb91ec)。

USART1 的串行时钟信号（SCLK）。

<a id="r_a521f5d5f7762f936161b939673a3676c"></a>

```c
#define LPC84X_SWM_USART2_TXD 10U
```

相关声明：[LPC84X_SWM_USART2_TXD](#a521f5d5f7762f936161b939673a3676c)。

USART2 的发送数据信号（TXD）。

<a id="r_ab8ce4361b5345aa7f7105a3b632e4d08"></a>

```c
#define LPC84X_SWM_USART2_RXD 11U
```

相关声明：[LPC84X_SWM_USART2_RXD](#ab8ce4361b5345aa7f7105a3b632e4d08)。

USART2 的接收数据信号（RXD）。

<a id="r_ad4e1c3427722ef9ab2a804cbdb631fc2"></a>

```c
#define LPC84X_SWM_USART2_RTS 12U
```

相关声明：[LPC84X_SWM_USART2_RTS](#ad4e1c3427722ef9ab2a804cbdb631fc2)。

USART2 的请求发送信号（RTS）。

<a id="r_adf1cf0986e84433ea45c759daaa1fa06"></a>

```c
#define LPC84X_SWM_USART2_CTS 13U
```

相关声明：[LPC84X_SWM_USART2_CTS](#adf1cf0986e84433ea45c759daaa1fa06)。

USART2 的清除发送信号（CTS）。

<a id="r_a6076959a65f0755b00d232b83e3dabe9"></a>

```c
#define LPC84X_SWM_USART2_SCLK 14U
```

相关声明：[LPC84X_SWM_USART2_SCLK](#a6076959a65f0755b00d232b83e3dabe9)。

USART2 的串行时钟信号（SCLK）。

<a id="r_aaa2d03ad1e4b76d8500c2d27665b5db4"></a>

```c
#define LPC84X_SWM_SPI0_SCK 15U
```

相关声明：[LPC84X_SWM_SPI0_SCK](#aaa2d03ad1e4b76d8500c2d27665b5db4)。

SPI0 的串行时钟信号（SCK）。

<a id="r_a31954d21676c226f6b7ed6859ce8d34a"></a>

```c
#define LPC84X_SWM_SPI0_MOSI 16U
```

相关声明：[LPC84X_SWM_SPI0_MOSI](#a31954d21676c226f6b7ed6859ce8d34a)。

SPI0 的主出从入数据信号（MOSI）。

<a id="r_a55d59b546c19be6efae2eb48c14418ae"></a>

```c
#define LPC84X_SWM_SPI0_MISO 17U
```

相关声明：[LPC84X_SWM_SPI0_MISO](#a55d59b546c19be6efae2eb48c14418ae)。

SPI0 的主入从出数据信号（MISO）。

<a id="r_ace44f6aafb6ea2fc42790a64baa3109a"></a>

```c
#define LPC84X_SWM_SPI0_SSEL0 18U
```

相关声明：[LPC84X_SWM_SPI0_SSEL0](#ace44f6aafb6ea2fc42790a64baa3109a)。

SPI0 的片选信号（SSEL0）。

<a id="r_a7a2db53a850fe6d2217912dcf594faa1"></a>

```c
#define LPC84X_SWM_SPI0_SSEL1 19U
```

相关声明：[LPC84X_SWM_SPI0_SSEL1](#a7a2db53a850fe6d2217912dcf594faa1)。

SPI0 的片选信号（SSEL1）。

<a id="r_a3081ab35e4015d6474402773f27af6a4"></a>

```c
#define LPC84X_SWM_SPI0_SSEL2 20U
```

相关声明：[LPC84X_SWM_SPI0_SSEL2](#a3081ab35e4015d6474402773f27af6a4)。

SPI0 的片选信号（SSEL2）。

<a id="r_ae1fe002f0e962a79105ba02c9426fdd3"></a>

```c
#define LPC84X_SWM_SPI0_SSEL3 21U
```

相关声明：[LPC84X_SWM_SPI0_SSEL3](#ae1fe002f0e962a79105ba02c9426fdd3)。

SPI0 的片选信号（SSEL3）。

<a id="r_ab2a4cd8a4f16ad11c67fb1e9a197e3a8"></a>

```c
#define LPC84X_SWM_SPI1_SCK 22U
```

相关声明：[LPC84X_SWM_SPI1_SCK](#ab2a4cd8a4f16ad11c67fb1e9a197e3a8)。

SPI1 的串行时钟信号（SCK）。

<a id="r_a6dc30ddc49ed74964718fef7c0f745eb"></a>

```c
#define LPC84X_SWM_SPI1_MOSI 23U
```

相关声明：[LPC84X_SWM_SPI1_MOSI](#a6dc30ddc49ed74964718fef7c0f745eb)。

SPI1 的主出从入数据信号（MOSI）。

<a id="r_a2fbef230d681d84953d32559b8d015d9"></a>

```c
#define LPC84X_SWM_SPI1_MISO 24U
```

相关声明：[LPC84X_SWM_SPI1_MISO](#a2fbef230d681d84953d32559b8d015d9)。

SPI1 的主入从出数据信号（MISO）。

<a id="r_ad48a83fc99a5ddc3c0b6e8253990bcaf"></a>

```c
#define LPC84X_SWM_SPI1_SSEL0 25U
```

相关声明：[LPC84X_SWM_SPI1_SSEL0](#ad48a83fc99a5ddc3c0b6e8253990bcaf)。

SPI1 的片选信号（SSEL0）。

<a id="r_ad77983e61d9cf35872279c167aacb58c"></a>

```c
#define LPC84X_SWM_SPI1_SSEL1 26U
```

相关声明：[LPC84X_SWM_SPI1_SSEL1](#ad77983e61d9cf35872279c167aacb58c)。

SPI1 的片选信号（SSEL1）。

<a id="r_aabf9d14936713e5b2192ae46e305c1e9"></a>

```c
#define LPC84X_SWM_SCT_PIN0 27U
```

相关声明：[LPC84X_SWM_SCT_PIN0](#aabf9d14936713e5b2192ae46e305c1e9)。

状态可配置定时器（SCT）的引脚 0（PIN0）。

<a id="r_a8f14ef73fedcc5ce674deb2a50182347"></a>

```c
#define LPC84X_SWM_SCT_PIN1 28U
```

相关声明：[LPC84X_SWM_SCT_PIN1](#a8f14ef73fedcc5ce674deb2a50182347)。

状态可配置定时器（SCT）的引脚 1（PIN1）。

<a id="r_acbcb5ba8dd26803fc5debb7f17a8654a"></a>

```c
#define LPC84X_SWM_SCT_PIN2 29U
```

相关声明：[LPC84X_SWM_SCT_PIN2](#acbcb5ba8dd26803fc5debb7f17a8654a)。

状态可配置定时器（SCT）的引脚 2（PIN2）。

<a id="r_a25e6a6f60a2fb014126746d13fea26ed"></a>

```c
#define LPC84X_SWM_SCT_PIN3 30U
```

相关声明：[LPC84X_SWM_SCT_PIN3](#a25e6a6f60a2fb014126746d13fea26ed)。

状态可配置定时器（SCT）的引脚 3（PIN3）。

<a id="r_a8f25d84116452559701f0a8f7e8fc469"></a>

```c
#define LPC84X_SWM_SCT_OUT0 31U
```

相关声明：[LPC84X_SWM_SCT_OUT0](#a8f25d84116452559701f0a8f7e8fc469)。

状态可配置定时器（SCT）的输出 0（OUT0）。

<a id="r_a719762d810ae379081c73337225a1ce5"></a>

```c
#define LPC84X_SWM_SCT_OUT1 32U
```

相关声明：[LPC84X_SWM_SCT_OUT1](#a719762d810ae379081c73337225a1ce5)。

状态可配置定时器（SCT）的输出 1（OUT1）。

<a id="r_ab16d0577efabf7f7c8efdd13d437519a"></a>

```c
#define LPC84X_SWM_SCT_OUT2 33U
```

相关声明：[LPC84X_SWM_SCT_OUT2](#ab16d0577efabf7f7c8efdd13d437519a)。

状态可配置定时器（SCT）的输出 2（OUT2）。

<a id="r_afe1c01eaea889033cc72ed7534d972bb"></a>

```c
#define LPC84X_SWM_SCT_OUT3 34U
```

相关声明：[LPC84X_SWM_SCT_OUT3](#afe1c01eaea889033cc72ed7534d972bb)。

状态可配置定时器（SCT）的输出 3（OUT3）。

<a id="r_a2406226706b1e3b658c76490def32da7"></a>

```c
#define LPC84X_SWM_SCT_OUT4 35U
```

相关声明：[LPC84X_SWM_SCT_OUT4](#a2406226706b1e3b658c76490def32da7)。

状态可配置定时器（SCT）的输出 4（OUT4）。

<a id="r_a24f81a0daa4ee314283ec2f70a5b8d09"></a>

```c
#define LPC84X_SWM_SCT_OUT5 36U
```

相关声明：[LPC84X_SWM_SCT_OUT5](#a24f81a0daa4ee314283ec2f70a5b8d09)。

状态可配置定时器（SCT）的输出 5（OUT5）。

<a id="r_afa8f56a7eb135d37ebc0579d890ba0a6"></a>

```c
#define LPC84X_SWM_SCT_OUT6 37U
```

相关声明：[LPC84X_SWM_SCT_OUT6](#afa8f56a7eb135d37ebc0579d890ba0a6)。

状态可配置定时器（SCT）的输出 6（OUT6）。

<a id="r_ac4550602c05f5cc2ac09b4866499c9fc"></a>

```c
#define LPC84X_SWM_I2C1_SDA 38U
```

相关声明：[LPC84X_SWM_I2C1_SDA](#ac4550602c05f5cc2ac09b4866499c9fc)。

I2C1 串行数据线（SDA）。

<a id="r_a8e6ae90b31d83731fb142e09625a8448"></a>

```c
#define LPC84X_SWM_I2C1_SCL 39U
```

相关声明：[LPC84X_SWM_I2C1_SCL](#a8e6ae90b31d83731fb142e09625a8448)。

I2C1 串行时钟线（SCL）。

<a id="r_ab4b95de9de86e27aa220bf3a149435c5"></a>

```c
#define LPC84X_SWM_I2C2_SDA 40U
```

相关声明：[LPC84X_SWM_I2C2_SDA](#ab4b95de9de86e27aa220bf3a149435c5)。

I2C2 串行数据线（SDA）。

<a id="r_a76fc0a0b65e3304795ccb4a98f1dc5b3"></a>

```c
#define LPC84X_SWM_I2C2_SCL 41U
```

相关声明：[LPC84X_SWM_I2C2_SCL](#a76fc0a0b65e3304795ccb4a98f1dc5b3)。

I2C2 串行时钟线（SCL）。

<a id="r_a70c640997c6a8abfb92970acc5ff8393"></a>

```c
#define LPC84X_SWM_I2C3_SDA 42U
```

相关声明：[LPC84X_SWM_I2C3_SDA](#a70c640997c6a8abfb92970acc5ff8393)。

I2C3 的串行数据信号（SDA）。

<a id="r_a6d2a0b0cda64d31e14dd58cee1a732d9"></a>

```c
#define LPC84X_SWM_I2C3_SCL 43U
```

相关声明：[LPC84X_SWM_I2C3_SCL](#a6d2a0b0cda64d31e14dd58cee1a732d9)。

I2C3 的串行时钟信号（SCL）。

<a id="r_ab37fb81e230d909ec8ee2cd9ebc20d17"></a>

```c
#define LPC84X_SWM_ACMP_OUT 44U
```

相关声明：[LPC84X_SWM_ACMP_OUT](#ab37fb81e230d909ec8ee2cd9ebc20d17)。

模拟比较器输出（ACMP OUT）。

<a id="r_a52d5aa18eace1d91ba21f9e9368c40a1"></a>

```c
#define LPC84X_SWM_CLKOUT 45U
```

相关声明：[LPC84X_SWM_CLKOUT](#a52d5aa18eace1d91ba21f9e9368c40a1)。

时钟输出（CLKOUT）。

<a id="r_ae53624c1e12af319476ed6a7df25d538"></a>

```c
#define LPC84X_SWM_GPIO_INT_BMAT 46U
```

相关声明：[LPC84X_SWM_GPIO_INT_BMAT](#ae53624c1e12af319476ed6a7df25d538)。

GPIO 中断位模式匹配（GPIO INT BMAT）。

<a id="r_ac51f611b848f8a7203023f2655f3bc52"></a>

```c
#define LPC84X_SWM_USART3_TXD 47U
```

相关声明：[LPC84X_SWM_USART3_TXD](#ac51f611b848f8a7203023f2655f3bc52)。

USART3 的发送数据信号（TXD）。

<a id="r_a909ea5af237942b81bda335c4c7600aa"></a>

```c
#define LPC84X_SWM_USART3_RXD 48U
```

相关声明：[LPC84X_SWM_USART3_RXD](#a909ea5af237942b81bda335c4c7600aa)。

USART3 的接收数据信号（RXD）。

<a id="r_ad94acec3a054b3a0281c43d079646fc6"></a>

```c
#define LPC84X_SWM_USART3_SCLK 49U
```

相关声明：[LPC84X_SWM_USART3_SCLK](#ad94acec3a054b3a0281c43d079646fc6)。

USART3 的串行时钟信号（SCLK）。

<a id="r_a8dcdadf178907a318c60a6c4bdf3de88"></a>

```c
#define LPC84X_SWM_USART4_TXD 50U
```

相关声明：[LPC84X_SWM_USART4_TXD](#a8dcdadf178907a318c60a6c4bdf3de88)。

USART4 的发送数据信号（TXD）。

<a id="r_a194aad29c2be2a49a5b2a75e288b3a29"></a>

```c
#define LPC84X_SWM_USART4_RXD 51U
```

相关声明：[LPC84X_SWM_USART4_RXD](#a194aad29c2be2a49a5b2a75e288b3a29)。

USART4 的接收数据信号（RXD）。

<a id="r_a04b6e0be7923662fcfed6aca3d465db1"></a>

```c
#define LPC84X_SWM_USART4_SCLK 52U
```

相关声明：[LPC84X_SWM_USART4_SCLK](#a04b6e0be7923662fcfed6aca3d465db1)。

USART4 的串行时钟信号（SCLK）。

<a id="r_a83a2626de3b6e698af987f890d709d7a"></a>

```c
#define LPC84X_SWM_T0_MAT_CHN0 53U
```

相关声明：[LPC84X_SWM_T0_MAT_CHN0](#a83a2626de3b6e698af987f890d709d7a)。

定时器 0（T0）的匹配通道 0（MAT CHN0）。

<a id="r_acb7ff85727e9c21249aa583ae22ab230"></a>

```c
#define LPC84X_SWM_T0_MAT_CHN1 54U
```

相关声明：[LPC84X_SWM_T0_MAT_CHN1](#acb7ff85727e9c21249aa583ae22ab230)。

定时器 0（T0）的匹配通道 1（MAT CHN1）。

<a id="r_a53c5a056e5a7bb070984db672ac98aa6"></a>

```c
#define LPC84X_SWM_T0_MAT_CHN2 55U
```

相关声明：[LPC84X_SWM_T0_MAT_CHN2](#a53c5a056e5a7bb070984db672ac98aa6)。

定时器 0（T0）的匹配通道 2（MAT CHN2）。

<a id="r_a7a6d47a782ed3218158e4f143f62e330"></a>

```c
#define LPC84X_SWM_T0_MAT_CHN3 56U
```

相关声明：[LPC84X_SWM_T0_MAT_CHN3](#a7a6d47a782ed3218158e4f143f62e330)。

定时器 0（T0）的匹配通道 3（MAT CHN3）。

<a id="r_adb226381e190df2edcc4c3bac6abe45e"></a>

```c
#define LPC84X_SWM_T0_CAP_CHN0 57U
```

相关声明：[LPC84X_SWM_T0_CAP_CHN0](#adb226381e190df2edcc4c3bac6abe45e)。

定时器 0（T0）的捕获通道 0（CAP CHN0）。

<a id="r_a96262593f6641a13890394cfcdb470ff"></a>

```c
#define LPC84X_SWM_T0_CAP_CHN1 58U
```

相关声明：[LPC84X_SWM_T0_CAP_CHN1](#a96262593f6641a13890394cfcdb470ff)。

定时器 0（T0）的捕获通道 1（CAP CHN1）。

<a id="r_a9da4cf6bf15135cf254e2c92b93c7b22"></a>

```c
#define LPC84X_SWM_T0_CAP_CHN2 59U
```

相关声明：[LPC84X_SWM_T0_CAP_CHN2](#a9da4cf6bf15135cf254e2c92b93c7b22)。

定时器 0（T0）的捕获通道 2（CAP CHN2）。

<a id="r_a7691b60528e0d62c707b5720ca1f9b78"></a>

```c
#define LPC84X_SWM_ACMP_INPUT1 0U
```

相关声明：[LPC84X_SWM_ACMP_INPUT1](#a7691b60528e0d62c707b5720ca1f9b78)。

模拟比较器（ACMP）输入 1（INPUT1）。

<a id="r_abc7d67d7558ff10226a7b86cd00fd52e"></a>

```c
#define LPC84X_SWM_ACMP_INPUT2 1U
```

相关声明：[LPC84X_SWM_ACMP_INPUT2](#abc7d67d7558ff10226a7b86cd00fd52e)。

模拟比较器（ACMP）输入 2（INPUT2）。

<a id="r_accbb115933ceb9f22d841a6572f545e5"></a>

```c
#define LPC84X_SWM_ACMP_INPUT3 2U
```

相关声明：[LPC84X_SWM_ACMP_INPUT3](#accbb115933ceb9f22d841a6572f545e5)。

模拟比较器（ACMP）输入 3（INPUT3）。

<a id="r_a20afafa92b39c750dd534659da25576c"></a>

```c
#define LPC84X_SWM_ACMP_INPUT4 3U
```

相关声明：[LPC84X_SWM_ACMP_INPUT4](#a20afafa92b39c750dd534659da25576c)。

模拟比较器（ACMP）输入 4（INPUT4）。

<a id="r_a64a026241812aa372402fdf9ea8e2a76"></a>

```c
#define LPC84X_SWM_ACMP_INPUT5 4U
```

相关声明：[LPC84X_SWM_ACMP_INPUT5](#a64a026241812aa372402fdf9ea8e2a76)。

模拟比较器（ACMP）输入 5（INPUT5）。

<a id="r_a01acde3232b115b03d5d758a5844df7a"></a>

```c
#define LPC84X_SWM_SWCLK 5U
```

相关声明：[LPC84X_SWM_SWCLK](#a01acde3232b115b03d5d758a5844df7a)。

串行线调试时钟（SWCLK）。

<a id="r_acc70eaa6551bd0d63ea76d03a2ed4e19"></a>

```c
#define LPC84X_SWM_SWDIO 6U
```

相关声明：[LPC84X_SWM_SWDIO](#acc70eaa6551bd0d63ea76d03a2ed4e19)。

串行线调试数据 I/O（SWDIO）。

<a id="r_a63552edb1b6563c5e6bbbc6edf14cd7e"></a>

```c
#define LPC84X_SWM_XTALIN 7U
```

相关声明：[LPC84X_SWM_XTALIN](#a63552edb1b6563c5e6bbbc6edf14cd7e)。

晶体输入（XTALIN）。

<a id="r_a7efda9e24b5c3abb92d477fc473a1de6"></a>

```c
#define LPC84X_SWM_XTALOUT 8U
```

相关声明：[LPC84X_SWM_XTALOUT](#a7efda9e24b5c3abb92d477fc473a1de6)。

晶体输出（XTALOUT）。

<a id="r_a54f521185623827ea4d1bc8c214694f9"></a>

```c
#define LPC84X_SWM_RESETN 9U
```

相关声明：[LPC84X_SWM_RESETN](#a54f521185623827ea4d1bc8c214694f9)。

低电平有效复位（RESETN）。

<a id="r_ae83b0c2582e5e44c46920dd92eecbee0"></a>

```c
#define LPC84X_SWM_CLKIN 10U
```

相关声明：[LPC84X_SWM_CLKIN](#ae83b0c2582e5e44c46920dd92eecbee0)。

时钟输入（CLKIN）。

<a id="r_aa09d0c97ae4cd35c0d7039061cd98028"></a>

```c
#define LPC84X_SWM_VDDCMP 11U
```

相关声明：[LPC84X_SWM_VDDCMP](#aa09d0c97ae4cd35c0d7039061cd98028)。

VDD 比较器信号（VDDCMP）。

<a id="r_a90cde2f1d850711c114ba9bdcf6f00ba"></a>

```c
#define LPC84X_SWM_I2C0_SDA 12U
```

相关声明：[LPC84X_SWM_I2C0_SDA](#a90cde2f1d850711c114ba9bdcf6f00ba)。

I2C0 的串行数据信号（SDA）。

<a id="r_a4a3c86b11b8aefc3e7a5551f4f67691e"></a>

```c
#define LPC84X_SWM_I2C0_SCL 13U
```

相关声明：[LPC84X_SWM_I2C0_SCL](#a4a3c86b11b8aefc3e7a5551f4f67691e)。

I2C0 的串行时钟信号（SCL）。

<a id="r_a5c0bf8dff9776a4307314b65226acd14"></a>

```c
#define LPC84X_SWM_ADC_CHN0 14U
```

相关声明：[LPC84X_SWM_ADC_CHN0](#a5c0bf8dff9776a4307314b65226acd14)。

模数转换器（ADC）通道 0（CHN0）。

<a id="r_a465895d878192fd981b4c0578ac790e1"></a>

```c
#define LPC84X_SWM_ADC_CHN1 15U
```

相关声明：[LPC84X_SWM_ADC_CHN1](#a465895d878192fd981b4c0578ac790e1)。

模数转换器（ADC）通道 1（CHN1）。

<a id="r_a62af44fdbffd4a9266ff02e0993fcead"></a>

```c
#define LPC84X_SWM_ADC_CHN2 16U
```

相关声明：[LPC84X_SWM_ADC_CHN2](#a62af44fdbffd4a9266ff02e0993fcead)。

模数转换器（ADC）通道 2（CHN2）。

<a id="r_a8ba1befda57559d57f29a0ba20e76a73"></a>

```c
#define LPC84X_SWM_ADC_CHN3 17U
```

相关声明：[LPC84X_SWM_ADC_CHN3](#a8ba1befda57559d57f29a0ba20e76a73)。

模数转换器（ADC）通道 3（CHN3）。

<a id="r_a74b73703d7cd4c1eb47af5840080887b"></a>

```c
#define LPC84X_SWM_ADC_CHN4 18U
```

相关声明：[LPC84X_SWM_ADC_CHN4](#a74b73703d7cd4c1eb47af5840080887b)。

模数转换器（ADC）通道 4（CHN4）。

<a id="r_a9d6dfa425b4c122b3550d255eaaffb5a"></a>

```c
#define LPC84X_SWM_ADC_CHN5 19U
```

相关声明：[LPC84X_SWM_ADC_CHN5](#a9d6dfa425b4c122b3550d255eaaffb5a)。

模数转换器（ADC）通道 5（CHN5）。

<a id="r_a453724b82e0f480a4af2928dca3e8adb"></a>

```c
#define LPC84X_SWM_ADC_CHN6 20U
```

相关声明：[LPC84X_SWM_ADC_CHN6](#a453724b82e0f480a4af2928dca3e8adb)。

模数转换器（ADC）通道 6（CHN6）。

<a id="r_a8f0415ee862278497ebaf3cdb3fd5db6"></a>

```c
#define LPC84X_SWM_ADC_CHN7 21U
```

相关声明：[LPC84X_SWM_ADC_CHN7](#a8f0415ee862278497ebaf3cdb3fd5db6)。

模数转换器（ADC）通道 7（CHN7）。

<a id="r_a7930d56a3cc2464a6d701fc332be143e"></a>

```c
#define LPC84X_SWM_ADC_CHN8 22U
```

相关声明：[LPC84X_SWM_ADC_CHN8](#a7930d56a3cc2464a6d701fc332be143e)。

模数转换器（ADC）通道 8（CHN8）。

<a id="r_acd4d965df7a821edfe312cec56b16178"></a>

```c
#define LPC84X_SWM_ADC_CHN9 23U
```

相关声明：[LPC84X_SWM_ADC_CHN9](#acd4d965df7a821edfe312cec56b16178)。

模数转换器（ADC）通道 9（CHN9）。

<a id="r_aea71ceb94feb7d17038ea2ab2470d845"></a>

```c
#define LPC84X_SWM_ADC_CHN10 24U
```

相关声明：[LPC84X_SWM_ADC_CHN10](#aea71ceb94feb7d17038ea2ab2470d845)。

模数转换器（ADC）通道 10（CHN10）。

<a id="r_a9d216af07271614bb072abc4662efabb"></a>

```c
#define LPC84X_SWM_ADC_CHN11 25U
```

相关声明：[LPC84X_SWM_ADC_CHN11](#a9d216af07271614bb072abc4662efabb)。

模数转换器（ADC）通道 11（CHN11）。

<a id="r_afd739ffe20ac16e04dedfd93761f1451"></a>

```c
#define LPC84X_SWM_DAC_OUT0 26U
```

相关声明：[LPC84X_SWM_DAC_OUT0](#afd739ffe20ac16e04dedfd93761f1451)。

数模转换器（DAC）输出 0（DACOUT0）。

<a id="r_a229765f5da8c78db4a1b10249eec39a3"></a>

```c
#define LPC84X_SWM_DAC_OUT1 27U
```

相关声明：[LPC84X_SWM_DAC_OUT1](#a229765f5da8c78db4a1b10249eec39a3)。

数模转换器（DAC）输出 1（DACOUT1）。

<a id="r_a8c91d228709a955c363ae548460f90f4"></a>

```c
#define LPC84X_SWM_CAPT_X0 28U
```

相关声明：[LPC84X_SWM_CAPT_X0](#a8c91d228709a955c363ae548460f90f4)。

`CAPT_X0`，互电容触摸传感器（Mutual Capacitance Touch Sensor）信号。

<a id="r_ad3e8d0c824f18b3788f3acdb0e69d8eb"></a>

```c
#define LPC84X_SWM_CAPT_X1 29U
```

相关声明：[LPC84X_SWM_CAPT_X1](#ad3e8d0c824f18b3788f3acdb0e69d8eb)。

电容触摸（CAPT）X1 信号。

<a id="r_ade79d2747b4e20c5d4ae7768b964d80b"></a>

```c
#define LPC84X_SWM_CAPT_X2 30U
```

相关声明：[LPC84X_SWM_CAPT_X2](#ade79d2747b4e20c5d4ae7768b964d80b)。

电容触摸（CAPT）X2 信号。

<a id="r_a61c135bd890c11bdaf7e81ed0fed324c"></a>

```c
#define LPC84X_SWM_CAPT_X3 31U
```

相关声明：[LPC84X_SWM_CAPT_X3](#a61c135bd890c11bdaf7e81ed0fed324c)。

电容触摸（CAPT）X3 信号。

<a id="r_a48e869dffcb2c6ef9d2e87f5b9b78064"></a>

```c
#define LPC84X_SWM_CAPT_X4 32U
```

相关声明：[LPC84X_SWM_CAPT_X4](#a48e869dffcb2c6ef9d2e87f5b9b78064)。

`CAPT_X4`，从此处开始进入 `PINENABLE1` 范围。

<a id="r_a56d9487bcc018f294448e79a757f02eb"></a>

```c
#define LPC84X_SWM_CAPT_X5 33U
```

相关声明：[LPC84X_SWM_CAPT_X5](#a56d9487bcc018f294448e79a757f02eb)。

电容触摸（CAPT）X5 信号。

<a id="r_a9dd7c7191485b22f8c26517113c7a2a6"></a>

```c
#define LPC84X_SWM_CAPT_X6 34U
```

相关声明：[LPC84X_SWM_CAPT_X6](#a9dd7c7191485b22f8c26517113c7a2a6)。

电容触摸（CAPT）X6 信号。

<a id="r_a1157debd93302c3e8a33784134bf5a0e"></a>

```c
#define LPC84X_SWM_CAPT_X7 35U
```

相关声明：[LPC84X_SWM_CAPT_X7](#a1157debd93302c3e8a33784134bf5a0e)。

电容触摸（CAPT）X7 信号。

<a id="r_aa872037286dc99a4ab53a6177ad5ffed"></a>

```c
#define LPC84X_SWM_CAPT_X8 36U
```

相关声明：[LPC84X_SWM_CAPT_X8](#aa872037286dc99a4ab53a6177ad5ffed)。

电容触摸（CAPT）X8 信号。

<a id="r_af103b906a18d9105ae80b62030790faf"></a>

```c
#define LPC84X_SWM_CAPT_YL 37U
```

相关声明：[LPC84X_SWM_CAPT_YL](#af103b906a18d9105ae80b62030790faf)。

`CAPT_YL`，测量电容（Measurement Capacitor）信号。

<a id="r_a30467b5eedcf2517d7e31b39936f463c"></a>

```c
#define LPC84X_SWM_CAPT_YH 38U
```

相关声明：[LPC84X_SWM_CAPT_YH](#a30467b5eedcf2517d7e31b39936f463c)。

电容触摸（CAPT）的 `YH` 信号。

<a id="r_ad1db232d88079d3dc03d37d804202f6d"></a>

```c
#define LPC84X_PIN_P0_0 0U
```

相关声明：[LPC84X_PIN_P0_0](#ad1db232d88079d3dc03d37d804202f6d)。

开关矩阵（SWM）使用的物理端口引脚标识符（Physical Port Pin Identifiers）。

<a id="r_a9c5d720377518adb657a21daa4cd4f48"></a>

```c
#define LPC84X_PIN_P0_1 1U
```

相关声明：[LPC84X_PIN_P0_1](#a9c5d720377518adb657a21daa4cd4f48)。

物理端口 0 的引脚 1（P0.1）。

<a id="r_adac57525cb318956d67bd5f11200a5cc"></a>

```c
#define LPC84X_PIN_P0_2 2U
```

相关声明：[LPC84X_PIN_P0_2](#adac57525cb318956d67bd5f11200a5cc)。

物理端口 0 的引脚 2（P0.2）。

<a id="r_a53b0780c5a66ddbd1475d069218e7395"></a>

```c
#define LPC84X_PIN_P0_3 3U
```

相关声明：[LPC84X_PIN_P0_3](#a53b0780c5a66ddbd1475d069218e7395)。

物理端口 0 的引脚 3（P0.3）。

<a id="r_a4b8030696a58d736aa33d92d1d6b0a73"></a>

```c
#define LPC84X_PIN_P0_4 4U
```

相关声明：[LPC84X_PIN_P0_4](#a4b8030696a58d736aa33d92d1d6b0a73)。

物理端口 0 的引脚 4（P0.4）。

<a id="r_ae413bbd918fefa03f8b9c8f068876ab5"></a>

```c
#define LPC84X_PIN_P0_5 5U
```

相关声明：[LPC84X_PIN_P0_5](#ae413bbd918fefa03f8b9c8f068876ab5)。

物理端口 0 的引脚 5（P0.5）。

<a id="r_ae276bc41e9f9549d4a0907ebe2393e50"></a>

```c
#define LPC84X_PIN_P0_6 6U
```

相关声明：[LPC84X_PIN_P0_6](#ae276bc41e9f9549d4a0907ebe2393e50)。

物理端口 0 的引脚 6（P0.6）。

<a id="r_a6e979a3752bdc314a3e9571ac483a315"></a>

```c
#define LPC84X_PIN_P0_7 7U
```

相关声明：[LPC84X_PIN_P0_7](#a6e979a3752bdc314a3e9571ac483a315)。

物理端口 0 的引脚 7（P0.7）。

<a id="r_a2e5a4cb414a855564b08d9ae84b4d353"></a>

```c
#define LPC84X_PIN_P0_8 8U
```

相关声明：[LPC84X_PIN_P0_8](#a2e5a4cb414a855564b08d9ae84b4d353)。

物理端口 0 的引脚 8（P0.8）。

<a id="r_a06e1bbecaea97298ae05b11222e79d81"></a>

```c
#define LPC84X_PIN_P0_9 9U
```

相关声明：[LPC84X_PIN_P0_9](#a06e1bbecaea97298ae05b11222e79d81)。

物理端口 0 的引脚 9（P0.9）。

<a id="r_a50a2252ad3383cf9661d63bcaf7ecaa0"></a>

```c
#define LPC84X_PIN_P0_10 10U
```

相关声明：[LPC84X_PIN_P0_10](#a50a2252ad3383cf9661d63bcaf7ecaa0)。

物理端口 0 的引脚 10（P0.10）。

<a id="r_a86ee0bb5a00aa6a5a59cd7b4e7a5caa7"></a>

```c
#define LPC84X_PIN_P0_11 11U
```

相关声明：[LPC84X_PIN_P0_11](#a86ee0bb5a00aa6a5a59cd7b4e7a5caa7)。

物理端口 0 的引脚 11（P0.11）。

<a id="r_add1c1b6463517c45f9f6ac3a8eeab50c"></a>

```c
#define LPC84X_PIN_P0_12 12U
```

相关声明：[LPC84X_PIN_P0_12](#add1c1b6463517c45f9f6ac3a8eeab50c)。

物理端口 0 的引脚 12（P0.12）。

<a id="r_a954de42869f3990c3ea795c918f2731a"></a>

```c
#define LPC84X_PIN_P0_13 13U
```

相关声明：[LPC84X_PIN_P0_13](#a954de42869f3990c3ea795c918f2731a)。

物理端口 0 的引脚 13（P0.13）。

<a id="r_ad496e70ef5c3c10792d40db26e254595"></a>

```c
#define LPC84X_PIN_P0_14 14U
```

相关声明：[LPC84X_PIN_P0_14](#ad496e70ef5c3c10792d40db26e254595)。

物理端口 0 的引脚 14（P0.14）。

<a id="r_a939675ff4fde16f666f4042459af8d5c"></a>

```c
#define LPC84X_PIN_P0_15 15U
```

相关声明：[LPC84X_PIN_P0_15](#a939675ff4fde16f666f4042459af8d5c)。

物理端口 0 的引脚 15（P0.15）。

<a id="r_ae8b87af4800075e0aab2ffb2ad2c8403"></a>

```c
#define LPC84X_PIN_P0_16 16U
```

相关声明：[LPC84X_PIN_P0_16](#ae8b87af4800075e0aab2ffb2ad2c8403)。

物理端口 0 的引脚 16（P0.16）。

<a id="r_ae2fafc086e64954c7a67e7835642b4e0"></a>

```c
#define LPC84X_PIN_P0_17 17U
```

相关声明：[LPC84X_PIN_P0_17](#ae2fafc086e64954c7a67e7835642b4e0)。

物理端口 0 的引脚 17（P0.17）。

<a id="r_aed5527e15df460a7fb11b1090eed3dd4"></a>

```c
#define LPC84X_PIN_P0_18 18U
```

相关声明：[LPC84X_PIN_P0_18](#aed5527e15df460a7fb11b1090eed3dd4)。

物理端口 0 的引脚 18（P0.18）。

<a id="r_ab81e06da645e790a33b1a3b2e841694b"></a>

```c
#define LPC84X_PIN_P0_19 19U
```

相关声明：[LPC84X_PIN_P0_19](#ab81e06da645e790a33b1a3b2e841694b)。

物理端口 0 的引脚 19（P0.19）。

<a id="r_adf53e74fc9566608db9f135dac2c950b"></a>

```c
#define LPC84X_PIN_P0_20 20U
```

相关声明：[LPC84X_PIN_P0_20](#adf53e74fc9566608db9f135dac2c950b)。

物理端口 0 的引脚 20（P0.20）。

<a id="r_a7b39f7f1db0490e8d6c802d18a00cb56"></a>

```c
#define LPC84X_PIN_P0_21 21U
```

相关声明：[LPC84X_PIN_P0_21](#a7b39f7f1db0490e8d6c802d18a00cb56)。

物理端口 0 的引脚 21（P0.21）。

<a id="r_aeafae23924726cba2f97b4ba85b50bdf"></a>

```c
#define LPC84X_PIN_P0_22 22U
```

相关声明：[LPC84X_PIN_P0_22](#aeafae23924726cba2f97b4ba85b50bdf)。

物理端口 0 的引脚 22（P0.22）。

<a id="r_a7fc3556913c5bbdcc4f7a5604a965b60"></a>

```c
#define LPC84X_PIN_P0_23 23U
```

相关声明：[LPC84X_PIN_P0_23](#a7fc3556913c5bbdcc4f7a5604a965b60)。

物理端口 0 的引脚 23（P0.23）。

<a id="r_a8e99f41a7c871ec0713a2e50bc1cd18b"></a>

```c
#define LPC84X_PIN_P0_24 24U
```

相关声明：[LPC84X_PIN_P0_24](#a8e99f41a7c871ec0713a2e50bc1cd18b)。

物理端口 0 的引脚 24（P0.24）。

<a id="r_a492660c4bc270ca4ceee05f68c0044ac"></a>

```c
#define LPC84X_PIN_P0_25 25U
```

相关声明：[LPC84X_PIN_P0_25](#a492660c4bc270ca4ceee05f68c0044ac)。

物理端口 0 的引脚 25（P0.25）。

<a id="r_a24cee95c6b1f7d963b19f5050804eb84"></a>

```c
#define LPC84X_PIN_P0_26 26U
```

相关声明：[LPC84X_PIN_P0_26](#a24cee95c6b1f7d963b19f5050804eb84)。

物理端口 0 的引脚 26（P0.26）。

<a id="r_a64338dd7064270a6d57082ea500bce90"></a>

```c
#define LPC84X_PIN_P0_27 27U
```

相关声明：[LPC84X_PIN_P0_27](#a64338dd7064270a6d57082ea500bce90)。

物理端口 0 的引脚 27（P0.27）。

<a id="r_af99fd2bde296a1714ab8571916751249"></a>

```c
#define LPC84X_PIN_P0_28 28U
```

相关声明：[LPC84X_PIN_P0_28](#af99fd2bde296a1714ab8571916751249)。

物理端口 0 的引脚 28（P0.28）。

<a id="r_a8e6fa11cf07b3cc86c662170daa59027"></a>

```c
#define LPC84X_PIN_P0_29 29U
```

相关声明：[LPC84X_PIN_P0_29](#a8e6fa11cf07b3cc86c662170daa59027)。

物理端口 0 的引脚 29（P0.29）。

<a id="r_ae8e0097f15e14f7a4b5b6e8fb61e9fd5"></a>

```c
#define LPC84X_PIN_P0_30 30U
```

相关声明：[LPC84X_PIN_P0_30](#ae8e0097f15e14f7a4b5b6e8fb61e9fd5)。

物理端口 0 的引脚 30（P0.30）。

<a id="r_a252678b971ff6a6feaff2d64c32c4b62"></a>

```c
#define LPC84X_PIN_P0_31 31U
```

相关声明：[LPC84X_PIN_P0_31](#a252678b971ff6a6feaff2d64c32c4b62)。

物理端口 0 的引脚 31（P0.31）。

<a id="r_aee84abb418d835a5e4808572e5dc44cb"></a>

```c
#define LPC84X_PIN_P1_0 32U
```

相关声明：[LPC84X_PIN_P1_0](#aee84abb418d835a5e4808572e5dc44cb)。

物理端口 1 的引脚 0（P1.0）。

<a id="r_a93344eccc237d561bc99fad742fc56a8"></a>

```c
#define LPC84X_PIN_P1_1 33U
```

相关声明：[LPC84X_PIN_P1_1](#a93344eccc237d561bc99fad742fc56a8)。

物理端口 1 的引脚 1（P1.1）。

<a id="r_a8fbd1e8c148b573ef70b724bdc52ab4b"></a>

```c
#define LPC84X_PIN_P1_2 34U
```

相关声明：[LPC84X_PIN_P1_2](#a8fbd1e8c148b573ef70b724bdc52ab4b)。

物理端口 1 的引脚 2（P1.2）。

<a id="r_a790372b446722ed6d0fa4e106c707c36"></a>

```c
#define LPC84X_PIN_P1_3 35U
```

相关声明：[LPC84X_PIN_P1_3](#a790372b446722ed6d0fa4e106c707c36)。

物理端口 1 的引脚 3（P1.3）。

<a id="r_ab006b7e3e68307fc36a062a8a7f20be4"></a>

```c
#define LPC84X_PIN_P1_4 36U
```

相关声明：[LPC84X_PIN_P1_4](#ab006b7e3e68307fc36a062a8a7f20be4)。

物理端口 1 的引脚 4（P1.4）。

<a id="r_aa0f7020d52e0bbb93c5acd058259fe44"></a>

```c
#define LPC84X_PIN_P1_5 37U
```

相关声明：[LPC84X_PIN_P1_5](#aa0f7020d52e0bbb93c5acd058259fe44)。

物理端口 1 的引脚 5（P1.5）。

<a id="r_a6608806c2def3a62d368801af5e26544"></a>

```c
#define LPC84X_PIN_P1_6 38U
```

相关声明：[LPC84X_PIN_P1_6](#a6608806c2def3a62d368801af5e26544)。

物理端口 1 的引脚 6（P1.6）。

<a id="r_a29e5093202be45edf212e64d405e5503"></a>

```c
#define LPC84X_PIN_P1_7 39U
```

相关声明：[LPC84X_PIN_P1_7](#a29e5093202be45edf212e64d405e5503)。

物理端口 1 的引脚 7（P1.7）。

<a id="r_afa72534a3bb1d644096c1b8f219db3b2"></a>

```c
#define LPC84X_PIN_P1_8 40U
```

相关声明：[LPC84X_PIN_P1_8](#afa72534a3bb1d644096c1b8f219db3b2)。

物理端口 1 的引脚 8（P1.8）。

<a id="r_aa55a1e578517a4d29570bc4fa21e2fd7"></a>

```c
#define LPC84X_PIN_P1_9 41U
```

相关声明：[LPC84X_PIN_P1_9](#aa55a1e578517a4d29570bc4fa21e2fd7)。

物理端口 1 的引脚 9（P1.9）。

<a id="r_aaaa008010a094f6d95ffa4fbdd0af0d9"></a>

```c
#define LPC84X_PIN_P1_10 42U
```

相关声明：[LPC84X_PIN_P1_10](#aaaa008010a094f6d95ffa4fbdd0af0d9)。

物理端口 1 的引脚 10（P1.10）。

<a id="r_a34bbe8474ebe8adc19f1c9614e633fcf"></a>

```c
#define LPC84X_PIN_P1_11 43U
```

相关声明：[LPC84X_PIN_P1_11](#a34bbe8474ebe8adc19f1c9614e633fcf)。

物理端口 1 的引脚 11（P1.11）。

<a id="r_a8161771007830581048f4e2a00c8f1ee"></a>

```c
#define LPC84X_PIN_P1_12 44U
```

相关声明：[LPC84X_PIN_P1_12](#a8161771007830581048f4e2a00c8f1ee)。

物理端口 1 的引脚 12（P1.12）。

<a id="r_a36e78c38a197f6cb62c7d772cccce5ee"></a>

```c
#define LPC84X_PIN_P1_13 45U
```

相关声明：[LPC84X_PIN_P1_13](#a36e78c38a197f6cb62c7d772cccce5ee)。

物理端口 1 的引脚 13（P1.13）。

<a id="r_aa151529a09ad8c8bea887035e327fcba"></a>

```c
#define LPC84X_PIN_P1_14 46U
```

相关声明：[LPC84X_PIN_P1_14](#aa151529a09ad8c8bea887035e327fcba)。

物理端口 1 的引脚 14（P1.14）。

<a id="r_acdfb1a7fd999f47af355165da0d3f409"></a>

```c
#define LPC84X_PIN_P1_15 47U
```

相关声明：[LPC84X_PIN_P1_15](#acdfb1a7fd999f47af355165da0d3f409)。

物理端口 1 的引脚 15（P1.15）。

<a id="r_a2a617a3f8d0aa25d59376877ffcd4eb4"></a>

```c
#define LPC84X_PIN_P1_16 48U
```

相关声明：[LPC84X_PIN_P1_16](#a2a617a3f8d0aa25d59376877ffcd4eb4)。

物理端口 1 的引脚 16（P1.16）。

<a id="r_a002faae4383ef826041a62e21b6829ec"></a>

```c
#define LPC84X_PIN_P1_17 49U
```

相关声明：[LPC84X_PIN_P1_17](#a002faae4383ef826041a62e21b6829ec)。

物理端口 1 的引脚 17（P1.17）。

<a id="r_a855bcacd31749728c846bf82f67b7092"></a>

```c
#define LPC84X_PIN_P1_18 50U
```

相关声明：[LPC84X_PIN_P1_18](#a855bcacd31749728c846bf82f67b7092)。

物理端口 1 的引脚 18（P1.18）。

<a id="r_acda3cbfed8a5a620e8123b3a7d18504e"></a>

```c
#define LPC84X_PIN_P1_19 51U
```

相关声明：[LPC84X_PIN_P1_19](#acda3cbfed8a5a620e8123b3a7d18504e)。

物理端口 1 的引脚 19（P1.19）。

<a id="r_a353fa50280a90834a1b65f88952e9dbe"></a>

```c
#define LPC84X_PIN_P1_20 52U
```

相关声明：[LPC84X_PIN_P1_20](#a353fa50280a90834a1b65f88952e9dbe)。

物理端口 1 的引脚 20（P1.20）。

<a id="r_a8a0eb588bea92a849fc7831ad0d4c7ee"></a>

```c
#define LPC84X_PIN_P1_21 53U
```

相关声明：[LPC84X_PIN_P1_21](#a8a0eb588bea92a849fc7831ad0d4c7ee)。

物理端口 1 的引脚 21（P1.21）。

<a id="r_a812f7f0c3e5fd4c4f6008b3acc8545ec"></a>

```c
#define IOCON_INDEX_PIO0_17 0U
```

相关声明：[IOCON_INDEX_PIO0_17](#a812f7f0c3e5fd4c4f6008b3acc8545ec)。

各个 PIO 引脚的 I/O 配置寄存器索引（IOCON Register Indices）。

<a id="r_aa8fae44b1a4eb04c413acff8c6e3fa53"></a>

```c
#define IOCON_INDEX_PIO0_13 1U
```

相关声明：[IOCON_INDEX_PIO0_13](#aa8fae44b1a4eb04c413acff8c6e3fa53)。

`PIO0_13` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_ab8132dff3d1740acf63d3d3a77daaa01"></a>

```c
#define IOCON_INDEX_PIO0_12 2U
```

相关声明：[IOCON_INDEX_PIO0_12](#ab8132dff3d1740acf63d3d3a77daaa01)。

`PIO0_12` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a4c5f119685abb8924e0afd61b014a22f"></a>

```c
#define IOCON_INDEX_PIO0_5 3U
```

相关声明：[IOCON_INDEX_PIO0_5](#a4c5f119685abb8924e0afd61b014a22f)。

`PIO0_5` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a0182178b00ef4bdbf7ff06361d18bd25"></a>

```c
#define IOCON_INDEX_PIO0_4 4U
```

相关声明：[IOCON_INDEX_PIO0_4](#a0182178b00ef4bdbf7ff06361d18bd25)。

`PIO0_4` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_ad970910091aec2eeba6898bab250e5e8"></a>

```c
#define IOCON_INDEX_PIO0_3 5U
```

相关声明：[IOCON_INDEX_PIO0_3](#ad970910091aec2eeba6898bab250e5e8)。

`PIO0_3` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_aa8a70f51d8cbf6e3c3bb71a15136dd4b"></a>

```c
#define IOCON_INDEX_PIO0_2 6U
```

相关声明：[IOCON_INDEX_PIO0_2](#aa8a70f51d8cbf6e3c3bb71a15136dd4b)。

`PIO0_2` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a8701f5b4a3e1541d05b91891b3dc6008"></a>

```c
#define IOCON_INDEX_PIO0_11 7U
```

相关声明：[IOCON_INDEX_PIO0_11](#a8701f5b4a3e1541d05b91891b3dc6008)。

`PIO0_11` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a95b0b1f5ba94efdccb48d50765449ffd"></a>

```c
#define IOCON_INDEX_PIO0_10 8U
```

相关声明：[IOCON_INDEX_PIO0_10](#a95b0b1f5ba94efdccb48d50765449ffd)。

`PIO0_10` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_ae93fca701eac78d0fc01bf572d6235e7"></a>

```c
#define IOCON_INDEX_PIO0_16 9U
```

相关声明：[IOCON_INDEX_PIO0_16](#ae93fca701eac78d0fc01bf572d6235e7)。

`PIO0_16` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a714a6dbfe29e20a5e49a6161d1ecd65a"></a>

```c
#define IOCON_INDEX_PIO0_15 10U
```

相关声明：[IOCON_INDEX_PIO0_15](#a714a6dbfe29e20a5e49a6161d1ecd65a)。

`PIO0_15` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_ac7212fca24c63173ec6b8f3f2a3c872d"></a>

```c
#define IOCON_INDEX_PIO0_1 11U
```

相关声明：[IOCON_INDEX_PIO0_1](#ac7212fca24c63173ec6b8f3f2a3c872d)。

`PIO0_1` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a4d6795d619fdadc07a892f0ea0c7b59b"></a>

```c
#define IOCON_INDEX_PIO0_9 13U
```

相关声明：[IOCON_INDEX_PIO0_9](#a4d6795d619fdadc07a892f0ea0c7b59b)。

`PIO0_9` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a5a646d435da4e16eefcfb7ec589a8f2f"></a>

```c
#define IOCON_INDEX_PIO0_8 14U
```

相关声明：[IOCON_INDEX_PIO0_8](#a5a646d435da4e16eefcfb7ec589a8f2f)。

`PIO0_8` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_ae3fd1aadc876363556e5104670208e67"></a>

```c
#define IOCON_INDEX_PIO0_7 15U
```

相关声明：[IOCON_INDEX_PIO0_7](#ae3fd1aadc876363556e5104670208e67)。

`PIO0_7` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_afd4e4d9f4f3b44b055f76a92af9dacb1"></a>

```c
#define IOCON_INDEX_PIO0_6 16U
```

相关声明：[IOCON_INDEX_PIO0_6](#afd4e4d9f4f3b44b055f76a92af9dacb1)。

`PIO0_6` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_af590d3cdf4c00bb210c4b787bdebac2f"></a>

```c
#define IOCON_INDEX_PIO0_0 17U
```

相关声明：[IOCON_INDEX_PIO0_0](#af590d3cdf4c00bb210c4b787bdebac2f)。

`PIO0_0` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a5591b72823931380f275ced24a88680e"></a>

```c
#define IOCON_INDEX_PIO0_14 18U
```

相关声明：[IOCON_INDEX_PIO0_14](#a5591b72823931380f275ced24a88680e)。

`PIO0_14` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a58338a9d9ec1b0a0d985627f824aea56"></a>

```c
#define IOCON_INDEX_PIO0_28 20U
```

相关声明：[IOCON_INDEX_PIO0_28](#a58338a9d9ec1b0a0d985627f824aea56)。

`PIO0_28` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a06c05877b9033538a32575d0a66e5a4f"></a>

```c
#define IOCON_INDEX_PIO0_27 21U
```

相关声明：[IOCON_INDEX_PIO0_27](#a06c05877b9033538a32575d0a66e5a4f)。

`PIO0_27` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a134a7f3d9318c9448a4dcee62235c645"></a>

```c
#define IOCON_INDEX_PIO0_26 22U
```

相关声明：[IOCON_INDEX_PIO0_26](#a134a7f3d9318c9448a4dcee62235c645)。

`PIO0_26` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a5f38f18d95a17db2f078ef65a18acb8a"></a>

```c
#define IOCON_INDEX_PIO0_25 23U
```

相关声明：[IOCON_INDEX_PIO0_25](#a5f38f18d95a17db2f078ef65a18acb8a)。

`PIO0_25` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_ac6d0f09cd357c98ad1099aeb6f31a68c"></a>

```c
#define IOCON_INDEX_PIO0_24 24U
```

相关声明：[IOCON_INDEX_PIO0_24](#ac6d0f09cd357c98ad1099aeb6f31a68c)。

`PIO0_24` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_ab74d912ebd2193df3569ebc0ab92ea63"></a>

```c
#define IOCON_INDEX_PIO0_23 25U
```

相关声明：[IOCON_INDEX_PIO0_23](#ab74d912ebd2193df3569ebc0ab92ea63)。

`PIO0_23` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a96133f3494e1234dd623c19b06f0e671"></a>

```c
#define IOCON_INDEX_PIO0_22 26U
```

相关声明：[IOCON_INDEX_PIO0_22](#a96133f3494e1234dd623c19b06f0e671)。

`PIO0_22` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a939739de8e85dcd42d15d27521c21d42"></a>

```c
#define IOCON_INDEX_PIO0_21 27U
```

相关声明：[IOCON_INDEX_PIO0_21](#a939739de8e85dcd42d15d27521c21d42)。

`PIO0_21` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a844ff895b8ce20c058d7426b27fff258"></a>

```c
#define IOCON_INDEX_PIO0_20 28U
```

相关声明：[IOCON_INDEX_PIO0_20](#a844ff895b8ce20c058d7426b27fff258)。

`PIO0_20` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_aaa9552c40eefbe868885ead9ac0b0d6d"></a>

```c
#define IOCON_INDEX_PIO0_19 29U
```

相关声明：[IOCON_INDEX_PIO0_19](#aaa9552c40eefbe868885ead9ac0b0d6d)。

`PIO0_19` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_ae87a8df1d5dbee171c87a5b2e027692e"></a>

```c
#define IOCON_INDEX_PIO0_18 30U
```

相关声明：[IOCON_INDEX_PIO0_18](#ae87a8df1d5dbee171c87a5b2e027692e)。

`PIO0_18` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_af44de783a68a52a8b2c11b8fff5faa21"></a>

```c
#define IOCON_INDEX_PIO1_8 31U
```

相关声明：[IOCON_INDEX_PIO1_8](#af44de783a68a52a8b2c11b8fff5faa21)。

`PIO1_8` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a47304bfe7384a074b1c80da21fc38454"></a>

```c
#define IOCON_INDEX_PIO1_9 32U
```

相关声明：[IOCON_INDEX_PIO1_9](#a47304bfe7384a074b1c80da21fc38454)。

`PIO1_9` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a849ccc703bb8fe6cb247e71bec25eb31"></a>

```c
#define IOCON_INDEX_PIO1_12 33U
```

相关声明：[IOCON_INDEX_PIO1_12](#a849ccc703bb8fe6cb247e71bec25eb31)。

`PIO1_12` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a97946b31c966d422c4d65505d17eb005"></a>

```c
#define IOCON_INDEX_PIO1_13 34U
```

相关声明：[IOCON_INDEX_PIO1_13](#a97946b31c966d422c4d65505d17eb005)。

`PIO1_13` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a0e206c7900cf7a59f02721879e01c4af"></a>

```c
#define IOCON_INDEX_PIO0_31 35U
```

相关声明：[IOCON_INDEX_PIO0_31](#a0e206c7900cf7a59f02721879e01c4af)。

`PIO0_31` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_af379aa275eb85f091ece4aea39e02db4"></a>

```c
#define IOCON_INDEX_PIO1_0 36U
```

相关声明：[IOCON_INDEX_PIO1_0](#af379aa275eb85f091ece4aea39e02db4)。

`PIO1_0` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_ae75433b3291dc9a506a90519127ad0d6"></a>

```c
#define IOCON_INDEX_PIO1_1 37U
```

相关声明：[IOCON_INDEX_PIO1_1](#ae75433b3291dc9a506a90519127ad0d6)。

`PIO1_1` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_af25e594edb962c83d5ef395a460a3515"></a>

```c
#define IOCON_INDEX_PIO1_2 38U
```

相关声明：[IOCON_INDEX_PIO1_2](#af25e594edb962c83d5ef395a460a3515)。

`PIO1_2` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a41c8de9c20bfde59577ca85f116fa0c4"></a>

```c
#define IOCON_INDEX_PIO1_14 39U
```

相关声明：[IOCON_INDEX_PIO1_14](#a41c8de9c20bfde59577ca85f116fa0c4)。

`PIO1_14` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_ac5c6d1976ebf3497a0afee4b65d0f9df"></a>

```c
#define IOCON_INDEX_PIO1_15 40U
```

相关声明：[IOCON_INDEX_PIO1_15](#ac5c6d1976ebf3497a0afee4b65d0f9df)。

`PIO1_15` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_afba39be87ed475934fc9f53a0cb60a7b"></a>

```c
#define IOCON_INDEX_PIO1_3 41U
```

相关声明：[IOCON_INDEX_PIO1_3](#afba39be87ed475934fc9f53a0cb60a7b)。

`PIO1_3` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a0b99a3ccdfcd666763d3af17ce5fc952"></a>

```c
#define IOCON_INDEX_PIO1_4 42U
```

相关声明：[IOCON_INDEX_PIO1_4](#a0b99a3ccdfcd666763d3af17ce5fc952)。

`PIO1_4` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a23fe120736e0ac3f0cc285a70d4867ba"></a>

```c
#define IOCON_INDEX_PIO1_5 43U
```

相关声明：[IOCON_INDEX_PIO1_5](#a23fe120736e0ac3f0cc285a70d4867ba)。

`PIO1_5` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_add4d86d2f1b70b0b812f20b07835e5d6"></a>

```c
#define IOCON_INDEX_PIO1_16 44U
```

相关声明：[IOCON_INDEX_PIO1_16](#add4d86d2f1b70b0b812f20b07835e5d6)。

`PIO1_16` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a68096db7c329d2e428afb7aef3b8f741"></a>

```c
#define IOCON_INDEX_PIO1_17 45U
```

相关声明：[IOCON_INDEX_PIO1_17](#a68096db7c329d2e428afb7aef3b8f741)。

`PIO1_17` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a152e2c9bfaa506dcc40b03d7ad3d312c"></a>

```c
#define IOCON_INDEX_PIO1_6 46U
```

相关声明：[IOCON_INDEX_PIO1_6](#a152e2c9bfaa506dcc40b03d7ad3d312c)。

`PIO1_6` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a4c15e46e445b96e42a748e3841c80905"></a>

```c
#define IOCON_INDEX_PIO1_18 47U
```

相关声明：[IOCON_INDEX_PIO1_18](#a4c15e46e445b96e42a748e3841c80905)。

`PIO1_18` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a36930c4c2a9e11c8b93700d34e3d014a"></a>

```c
#define IOCON_INDEX_PIO1_19 48U
```

相关声明：[IOCON_INDEX_PIO1_19](#a36930c4c2a9e11c8b93700d34e3d014a)。

`PIO1_19` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a0c26e1fe920bbe065464664850423908"></a>

```c
#define IOCON_INDEX_PIO1_7 49U
```

相关声明：[IOCON_INDEX_PIO1_7](#a0c26e1fe920bbe065464664850423908)。

`PIO1_7` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a6e2783040ea48a5d2d35db26fdcf9f62"></a>

```c
#define IOCON_INDEX_PIO0_29 50U
```

相关声明：[IOCON_INDEX_PIO0_29](#a6e2783040ea48a5d2d35db26fdcf9f62)。

`PIO0_29` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a8853f1c47d0d1834e798cb50aa1eadc3"></a>

```c
#define IOCON_INDEX_PIO0_30 51U
```

相关声明：[IOCON_INDEX_PIO0_30](#a8853f1c47d0d1834e798cb50aa1eadc3)。

`PIO0_30` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a1e2353b87dcfa461edcfc65591531f9a"></a>

```c
#define IOCON_INDEX_PIO1_20 52U
```

相关声明：[IOCON_INDEX_PIO1_20](#a1e2353b87dcfa461edcfc65591531f9a)。

`PIO1_20` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_ab1087f12fcbc3e33026333b0d95486ab"></a>

```c
#define IOCON_INDEX_PIO1_21 53U
```

相关声明：[IOCON_INDEX_PIO1_21](#ab1087f12fcbc3e33026333b0d95486ab)。

`PIO1_21` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a9d3e24edf0c7ce480b47d9b394f18652"></a>

```c
#define IOCON_INDEX_PIO1_11 54U
```

相关声明：[IOCON_INDEX_PIO1_11](#a9d3e24edf0c7ce480b47d9b394f18652)。

`PIO1_11` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_ae23a124c69b44d2f20dd19cf635bf6f5"></a>

```c
#define IOCON_INDEX_PIO1_10 55U
```

相关声明：[IOCON_INDEX_PIO1_10](#ae23a124c69b44d2f20dd19cf635bf6f5)。

`PIO1_10` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="r_a667b43fb3d023097f21f1e518a46487b"></a>

```c
#define LPC84X_PIN_DEFINE(swm, iocon)
```

相关声明：[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)。

将开关矩阵（SWM）功能和 IOCON 索引编码为单个 16 位值。

<a id="r_a188735bd8812ee242324075c9cae4e0e"></a>

```c
#define P0_0 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_0, IOCON_INDEX_PIO0_0)
```

相关声明：[P0_0](#a188735bd8812ee242324075c9cae4e0e)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_0](#ad1db232d88079d3dc03d37d804202f6d)、[IOCON_INDEX_PIO0_0](#af590d3cdf4c00bb210c4b787bdebac2f)。

编码后的引脚定义（Encoded Pin Definitions），组合了物理端口引脚标识符与对应 IOCON 索引。

<a id="r_a6e605c856305ec72ac000d8cc45ab0b9"></a>

```c
#define P0_1 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_1, IOCON_INDEX_PIO0_1)
```

相关声明：[P0_1](#a6e605c856305ec72ac000d8cc45ab0b9)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_1](#a9c5d720377518adb657a21daa4cd4f48)、[IOCON_INDEX_PIO0_1](#ac7212fca24c63173ec6b8f3f2a3c872d)。

端口 0、引脚 1 的编码定义（P0_1）。

<a id="r_a876e3d0917cea9d0a75b2f6df2c3f1d4"></a>

```c
#define P0_2 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_2, IOCON_INDEX_PIO0_2)
```

相关声明：[P0_2](#a876e3d0917cea9d0a75b2f6df2c3f1d4)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_2](#adac57525cb318956d67bd5f11200a5cc)、[IOCON_INDEX_PIO0_2](#aa8a70f51d8cbf6e3c3bb71a15136dd4b)。

端口 0、引脚 2 的编码定义（P0_2）。

<a id="r_ab73f15237a6f8860438ba0359b283686"></a>

```c
#define P0_3 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_3, IOCON_INDEX_PIO0_3)
```

相关声明：[P0_3](#ab73f15237a6f8860438ba0359b283686)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_3](#a53b0780c5a66ddbd1475d069218e7395)、[IOCON_INDEX_PIO0_3](#ad970910091aec2eeba6898bab250e5e8)。

端口 0、引脚 3 的编码定义（P0_3）。

<a id="r_a3218b7341a4f084375bade756f108940"></a>

```c
#define P0_4 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_4, IOCON_INDEX_PIO0_4)
```

相关声明：[P0_4](#a3218b7341a4f084375bade756f108940)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_4](#a4b8030696a58d736aa33d92d1d6b0a73)、[IOCON_INDEX_PIO0_4](#a0182178b00ef4bdbf7ff06361d18bd25)。

端口 0、引脚 4 的编码定义（P0_4）。

<a id="r_aa1681f3dab52db87cd32f77b20352770"></a>

```c
#define P0_5 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_5, IOCON_INDEX_PIO0_5)
```

相关声明：[P0_5](#aa1681f3dab52db87cd32f77b20352770)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_5](#ae413bbd918fefa03f8b9c8f068876ab5)、[IOCON_INDEX_PIO0_5](#a4c5f119685abb8924e0afd61b014a22f)。

端口 0、引脚 5 的编码定义（P0_5）。

<a id="r_a990dc4ba08ec342d0bfa50f99d9e1868"></a>

```c
#define P0_6 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_6, IOCON_INDEX_PIO0_6)
```

相关声明：[P0_6](#a990dc4ba08ec342d0bfa50f99d9e1868)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_6](#ae276bc41e9f9549d4a0907ebe2393e50)、[IOCON_INDEX_PIO0_6](#afd4e4d9f4f3b44b055f76a92af9dacb1)。

端口 0、引脚 6 的编码定义（P0_6）。

<a id="r_a34087bca5283adcf7cc7c810f30eab80"></a>

```c
#define P0_7 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_7, IOCON_INDEX_PIO0_7)
```

相关声明：[P0_7](#a34087bca5283adcf7cc7c810f30eab80)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_7](#a6e979a3752bdc314a3e9571ac483a315)、[IOCON_INDEX_PIO0_7](#ae3fd1aadc876363556e5104670208e67)。

端口 0、引脚 7 的编码定义（P0_7）。

<a id="r_a5cfe193b59c3ee005dabe75f1a5b7162"></a>

```c
#define P0_8 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_8, IOCON_INDEX_PIO0_8)
```

相关声明：[P0_8](#a5cfe193b59c3ee005dabe75f1a5b7162)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_8](#a2e5a4cb414a855564b08d9ae84b4d353)、[IOCON_INDEX_PIO0_8](#a5a646d435da4e16eefcfb7ec589a8f2f)。

端口 0、引脚 8 的编码定义（P0_8）。

<a id="r_aae8e5c3d453e5a1acc12299784627b35"></a>

```c
#define P0_9 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_9, IOCON_INDEX_PIO0_9)
```

相关声明：[P0_9](#aae8e5c3d453e5a1acc12299784627b35)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_9](#a06e1bbecaea97298ae05b11222e79d81)、[IOCON_INDEX_PIO0_9](#a4d6795d619fdadc07a892f0ea0c7b59b)。

端口 0、引脚 9 的编码定义（P0_9）。

<a id="r_a6e0975575d630a24aab56aa9b4e1772d"></a>

```c
#define P0_10 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_10, IOCON_INDEX_PIO0_10)
```

相关声明：[P0_10](#a6e0975575d630a24aab56aa9b4e1772d)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_10](#a50a2252ad3383cf9661d63bcaf7ecaa0)、[IOCON_INDEX_PIO0_10](#a95b0b1f5ba94efdccb48d50765449ffd)。

端口 0、引脚 10 的编码定义（P0_10）。

<a id="r_a96018d9c4e5b359ef920a5af36cfb7aa"></a>

```c
#define P0_11 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_11, IOCON_INDEX_PIO0_11)
```

相关声明：[P0_11](#a96018d9c4e5b359ef920a5af36cfb7aa)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_11](#a86ee0bb5a00aa6a5a59cd7b4e7a5caa7)、[IOCON_INDEX_PIO0_11](#a8701f5b4a3e1541d05b91891b3dc6008)。

端口 0、引脚 11 的编码定义（P0_11）。

<a id="r_a240b3b6e91a2eaf160635c27888c1e19"></a>

```c
#define P0_12 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_12, IOCON_INDEX_PIO0_12)
```

相关声明：[P0_12](#a240b3b6e91a2eaf160635c27888c1e19)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_12](#add1c1b6463517c45f9f6ac3a8eeab50c)、[IOCON_INDEX_PIO0_12](#ab8132dff3d1740acf63d3d3a77daaa01)。

端口 0、引脚 12 的编码定义（P0_12）。

<a id="r_ae46d0fe9ff37262c0ce77c1dced2566b"></a>

```c
#define P0_13 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_13, IOCON_INDEX_PIO0_13)
```

相关声明：[P0_13](#ae46d0fe9ff37262c0ce77c1dced2566b)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_13](#a954de42869f3990c3ea795c918f2731a)、[IOCON_INDEX_PIO0_13](#aa8fae44b1a4eb04c413acff8c6e3fa53)。

端口 0、引脚 13 的编码定义（P0_13）。

<a id="r_abd51c64b559f19da0c8fb9f755194ca2"></a>

```c
#define P0_14 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_14, IOCON_INDEX_PIO0_14)
```

相关声明：[P0_14](#abd51c64b559f19da0c8fb9f755194ca2)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_14](#ad496e70ef5c3c10792d40db26e254595)、[IOCON_INDEX_PIO0_14](#a5591b72823931380f275ced24a88680e)。

端口 0、引脚 14 的编码定义（P0_14）。

<a id="r_a41c82eba7d677c4dd0b8af602a76284f"></a>

```c
#define P0_15 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_15, IOCON_INDEX_PIO0_15)
```

相关声明：[P0_15](#a41c82eba7d677c4dd0b8af602a76284f)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_15](#a939675ff4fde16f666f4042459af8d5c)、[IOCON_INDEX_PIO0_15](#a714a6dbfe29e20a5e49a6161d1ecd65a)。

端口 0、引脚 15 的编码定义（P0_15）。

<a id="r_a7f81f059c79120054cebb5fbcd383034"></a>

```c
#define P0_16 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_16, IOCON_INDEX_PIO0_16)
```

相关声明：[P0_16](#a7f81f059c79120054cebb5fbcd383034)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_16](#ae8b87af4800075e0aab2ffb2ad2c8403)、[IOCON_INDEX_PIO0_16](#ae93fca701eac78d0fc01bf572d6235e7)。

端口 0、引脚 16 的编码定义（P0_16）。

<a id="r_a2897768ad1f6566030af4a704ec02012"></a>

```c
#define P0_17 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_17, IOCON_INDEX_PIO0_17)
```

相关声明：[P0_17](#a2897768ad1f6566030af4a704ec02012)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_17](#ae2fafc086e64954c7a67e7835642b4e0)、[IOCON_INDEX_PIO0_17](#a812f7f0c3e5fd4c4f6008b3acc8545ec)。

端口 0、引脚 17 的编码定义（P0_17）。

<a id="r_a757921d7eed356cb0964aadbb028211f"></a>

```c
#define P0_18 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_18, IOCON_INDEX_PIO0_18)
```

相关声明：[P0_18](#a757921d7eed356cb0964aadbb028211f)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_18](#aed5527e15df460a7fb11b1090eed3dd4)、[IOCON_INDEX_PIO0_18](#ae87a8df1d5dbee171c87a5b2e027692e)。

端口 0、引脚 18 的编码定义（P0_18）。

<a id="r_a2187a967a9777b4fbf2b0635716d09d7"></a>

```c
#define P0_19 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_19, IOCON_INDEX_PIO0_19)
```

相关声明：[P0_19](#a2187a967a9777b4fbf2b0635716d09d7)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_19](#ab81e06da645e790a33b1a3b2e841694b)、[IOCON_INDEX_PIO0_19](#aaa9552c40eefbe868885ead9ac0b0d6d)。

端口 0、引脚 19 的编码定义（P0_19）。

<a id="r_a16283fe59fbca32579fef70b891d0262"></a>

```c
#define P0_20 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_20, IOCON_INDEX_PIO0_20)
```

相关声明：[P0_20](#a16283fe59fbca32579fef70b891d0262)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_20](#adf53e74fc9566608db9f135dac2c950b)、[IOCON_INDEX_PIO0_20](#a844ff895b8ce20c058d7426b27fff258)。

端口 0、引脚 20 的编码定义（P0_20）。

<a id="r_ace0737416a27f4f8413b4c74a19f69f1"></a>

```c
#define P0_21 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_21, IOCON_INDEX_PIO0_21)
```

相关声明：[P0_21](#ace0737416a27f4f8413b4c74a19f69f1)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_21](#a7b39f7f1db0490e8d6c802d18a00cb56)、[IOCON_INDEX_PIO0_21](#a939739de8e85dcd42d15d27521c21d42)。

端口 0、引脚 21 的编码定义（P0_21）。

<a id="r_a1e834f8c45c4a1ffd4abeb174ff79732"></a>

```c
#define P0_22 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_22, IOCON_INDEX_PIO0_22)
```

相关声明：[P0_22](#a1e834f8c45c4a1ffd4abeb174ff79732)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_22](#aeafae23924726cba2f97b4ba85b50bdf)、[IOCON_INDEX_PIO0_22](#a96133f3494e1234dd623c19b06f0e671)。

端口 0、引脚 22 的编码定义（P0_22）。

<a id="r_adc11371e625a7dc71e732a973ecfde3e"></a>

```c
#define P0_23 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_23, IOCON_INDEX_PIO0_23)
```

相关声明：[P0_23](#adc11371e625a7dc71e732a973ecfde3e)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_23](#a7fc3556913c5bbdcc4f7a5604a965b60)、[IOCON_INDEX_PIO0_23](#ab74d912ebd2193df3569ebc0ab92ea63)。

端口 0、引脚 23 的编码定义（P0_23）。

<a id="r_abaf804f6456d35f8322e8137d2ad725b"></a>

```c
#define P0_24 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_24, IOCON_INDEX_PIO0_24)
```

相关声明：[P0_24](#abaf804f6456d35f8322e8137d2ad725b)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_24](#a8e99f41a7c871ec0713a2e50bc1cd18b)、[IOCON_INDEX_PIO0_24](#ac6d0f09cd357c98ad1099aeb6f31a68c)。

端口 0、引脚 24 的编码定义（P0_24）。

<a id="r_a3285a6bb0cc206b249470bfc54ebd3e8"></a>

```c
#define P0_25 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_25, IOCON_INDEX_PIO0_25)
```

相关声明：[P0_25](#a3285a6bb0cc206b249470bfc54ebd3e8)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_25](#a492660c4bc270ca4ceee05f68c0044ac)、[IOCON_INDEX_PIO0_25](#a5f38f18d95a17db2f078ef65a18acb8a)。

端口 0、引脚 25 的编码定义（P0_25）。

<a id="r_ae9ff8d68608904f1fd48b0cdcc6a1943"></a>

```c
#define P0_26 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_26, IOCON_INDEX_PIO0_26)
```

相关声明：[P0_26](#ae9ff8d68608904f1fd48b0cdcc6a1943)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_26](#a24cee95c6b1f7d963b19f5050804eb84)、[IOCON_INDEX_PIO0_26](#a134a7f3d9318c9448a4dcee62235c645)。

端口 0、引脚 26 的编码定义（P0_26）。

<a id="r_ab382318857300a74bfe96533334c5622"></a>

```c
#define P0_27 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_27, IOCON_INDEX_PIO0_27)
```

相关声明：[P0_27](#ab382318857300a74bfe96533334c5622)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_27](#a64338dd7064270a6d57082ea500bce90)、[IOCON_INDEX_PIO0_27](#a06c05877b9033538a32575d0a66e5a4f)。

端口 0、引脚 27 的编码定义（P0_27）。

<a id="r_ac7b207aae62b35a54bc701b1a1d129f6"></a>

```c
#define P0_28 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_28, IOCON_INDEX_PIO0_28)
```

相关声明：[P0_28](#ac7b207aae62b35a54bc701b1a1d129f6)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_28](#af99fd2bde296a1714ab8571916751249)、[IOCON_INDEX_PIO0_28](#a58338a9d9ec1b0a0d985627f824aea56)。

端口 0、引脚 28 的编码定义（P0_28）。

<a id="r_adb961beba9ded7ce72e3d8edbb0cc5fe"></a>

```c
#define P0_29 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_29, IOCON_INDEX_PIO0_29)
```

相关声明：[P0_29](#adb961beba9ded7ce72e3d8edbb0cc5fe)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_29](#a8e6fa11cf07b3cc86c662170daa59027)、[IOCON_INDEX_PIO0_29](#a6e2783040ea48a5d2d35db26fdcf9f62)。

端口 0、引脚 29 的编码定义（P0_29）。

<a id="r_a1fa3927c6765a474ff77d13c87aa8ccf"></a>

```c
#define P0_30 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_30, IOCON_INDEX_PIO0_30)
```

相关声明：[P0_30](#a1fa3927c6765a474ff77d13c87aa8ccf)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_30](#ae8e0097f15e14f7a4b5b6e8fb61e9fd5)、[IOCON_INDEX_PIO0_30](#a8853f1c47d0d1834e798cb50aa1eadc3)。

端口 0、引脚 30 的编码定义（P0_30）。

<a id="r_a420dc619975be8d13b83c6ab7c364c41"></a>

```c
#define P0_31 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_31, IOCON_INDEX_PIO0_31)
```

相关声明：[P0_31](#a420dc619975be8d13b83c6ab7c364c41)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P0_31](#a252678b971ff6a6feaff2d64c32c4b62)、[IOCON_INDEX_PIO0_31](#a0e206c7900cf7a59f02721879e01c4af)。

端口 0、引脚 31 的编码定义（P0_31）。

<a id="r_a0a5c0ef038f9728173ca136eed5c9cd2"></a>

```c
#define P1_0 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_0, IOCON_INDEX_PIO1_0)
```

相关声明：[P1_0](#a0a5c0ef038f9728173ca136eed5c9cd2)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P1_0](#aee84abb418d835a5e4808572e5dc44cb)、[IOCON_INDEX_PIO1_0](#af379aa275eb85f091ece4aea39e02db4)。

端口 1、引脚 0 的编码定义（P1_0）。

<a id="r_aa7c3cebcd9dc4598bb69e51ecee85bd0"></a>

```c
#define P1_1 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_1, IOCON_INDEX_PIO1_1)
```

相关声明：[P1_1](#aa7c3cebcd9dc4598bb69e51ecee85bd0)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P1_1](#a93344eccc237d561bc99fad742fc56a8)、[IOCON_INDEX_PIO1_1](#ae75433b3291dc9a506a90519127ad0d6)。

端口 1、引脚 1 的编码定义（P1_1）。

<a id="r_a071e0091581eba3bdf70559d215cda5d"></a>

```c
#define P1_2 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_2, IOCON_INDEX_PIO1_2)
```

相关声明：[P1_2](#a071e0091581eba3bdf70559d215cda5d)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P1_2](#a8fbd1e8c148b573ef70b724bdc52ab4b)、[IOCON_INDEX_PIO1_2](#af25e594edb962c83d5ef395a460a3515)。

端口 1、引脚 2 的编码定义（P1_2）。

<a id="r_ad2a4d881a3a72ead238fcf2a4aea88bf"></a>

```c
#define P1_3 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_3, IOCON_INDEX_PIO1_3)
```

相关声明：[P1_3](#ad2a4d881a3a72ead238fcf2a4aea88bf)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P1_3](#a790372b446722ed6d0fa4e106c707c36)、[IOCON_INDEX_PIO1_3](#afba39be87ed475934fc9f53a0cb60a7b)。

端口 1、引脚 3 的编码定义（P1_3）。

<a id="r_ab65ddc9251137261c8c17b03a415e831"></a>

```c
#define P1_4 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_4, IOCON_INDEX_PIO1_4)
```

相关声明：[P1_4](#ab65ddc9251137261c8c17b03a415e831)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P1_4](#ab006b7e3e68307fc36a062a8a7f20be4)、[IOCON_INDEX_PIO1_4](#a0b99a3ccdfcd666763d3af17ce5fc952)。

端口 1、引脚 4 的编码定义（P1_4）。

<a id="r_af610a6265a7bc9f5c44efa18219c5e96"></a>

```c
#define P1_5 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_5, IOCON_INDEX_PIO1_5)
```

相关声明：[P1_5](#af610a6265a7bc9f5c44efa18219c5e96)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P1_5](#aa0f7020d52e0bbb93c5acd058259fe44)、[IOCON_INDEX_PIO1_5](#a23fe120736e0ac3f0cc285a70d4867ba)。

端口 1、引脚 5 的编码定义（P1_5）。

<a id="r_a9e219f75c65aa5b19d59bd1596b3e548"></a>

```c
#define P1_6 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_6, IOCON_INDEX_PIO1_6)
```

相关声明：[P1_6](#a9e219f75c65aa5b19d59bd1596b3e548)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P1_6](#a6608806c2def3a62d368801af5e26544)、[IOCON_INDEX_PIO1_6](#a152e2c9bfaa506dcc40b03d7ad3d312c)。

端口 1、引脚 6 的编码定义（P1_6）。

<a id="r_a59e6507c1874213b84ae809c24c3a76e"></a>

```c
#define P1_7 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_7, IOCON_INDEX_PIO1_7)
```

相关声明：[P1_7](#a59e6507c1874213b84ae809c24c3a76e)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P1_7](#a29e5093202be45edf212e64d405e5503)、[IOCON_INDEX_PIO1_7](#a0c26e1fe920bbe065464664850423908)。

端口 1、引脚 7 的编码定义（P1_7）。

<a id="r_acb31070df6aa10c8d25fba9a5c2a5c0d"></a>

```c
#define P1_8 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_8, IOCON_INDEX_PIO1_8)
```

相关声明：[P1_8](#acb31070df6aa10c8d25fba9a5c2a5c0d)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P1_8](#afa72534a3bb1d644096c1b8f219db3b2)、[IOCON_INDEX_PIO1_8](#af44de783a68a52a8b2c11b8fff5faa21)。

端口 1、引脚 8 的编码定义（P1_8）。

<a id="r_a3e359fe9dc553fe39543a35bc59fdb1d"></a>

```c
#define P1_9 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_9, IOCON_INDEX_PIO1_9)
```

相关声明：[P1_9](#a3e359fe9dc553fe39543a35bc59fdb1d)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P1_9](#aa55a1e578517a4d29570bc4fa21e2fd7)、[IOCON_INDEX_PIO1_9](#a47304bfe7384a074b1c80da21fc38454)。

端口 1、引脚 9 的编码定义（P1_9）。

<a id="r_a4319c5e3ed329de7acf55d50c10121f0"></a>

```c
#define P1_10 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_10, IOCON_INDEX_PIO1_10)
```

相关声明：[P1_10](#a4319c5e3ed329de7acf55d50c10121f0)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P1_10](#aaaa008010a094f6d95ffa4fbdd0af0d9)、[IOCON_INDEX_PIO1_10](#ae23a124c69b44d2f20dd19cf635bf6f5)。

端口 1、引脚 10 的编码定义（P1_10）。

<a id="r_a4a6d764dfc72b9a8c9c808d3065a1843"></a>

```c
#define P1_11 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_11, IOCON_INDEX_PIO1_11)
```

相关声明：[P1_11](#a4a6d764dfc72b9a8c9c808d3065a1843)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P1_11](#a34bbe8474ebe8adc19f1c9614e633fcf)、[IOCON_INDEX_PIO1_11](#a9d3e24edf0c7ce480b47d9b394f18652)。

端口 1、引脚 11 的编码定义（P1_11）。

<a id="r_a7e7591732365fa663a17fb738e2945a2"></a>

```c
#define P1_12 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_12, IOCON_INDEX_PIO1_12)
```

相关声明：[P1_12](#a7e7591732365fa663a17fb738e2945a2)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P1_12](#a8161771007830581048f4e2a00c8f1ee)、[IOCON_INDEX_PIO1_12](#a849ccc703bb8fe6cb247e71bec25eb31)。

端口 1、引脚 12 的编码定义（P1_12）。

<a id="r_a570652df2d7482326f11660c22e2dc28"></a>

```c
#define P1_13 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_13, IOCON_INDEX_PIO1_13)
```

相关声明：[P1_13](#a570652df2d7482326f11660c22e2dc28)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P1_13](#a36e78c38a197f6cb62c7d772cccce5ee)、[IOCON_INDEX_PIO1_13](#a97946b31c966d422c4d65505d17eb005)。

端口 1、引脚 13 的编码定义（P1_13）。

<a id="r_af273b3bb179cfc9082e8a70848592883"></a>

```c
#define P1_14 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_14, IOCON_INDEX_PIO1_14)
```

相关声明：[P1_14](#af273b3bb179cfc9082e8a70848592883)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P1_14](#aa151529a09ad8c8bea887035e327fcba)、[IOCON_INDEX_PIO1_14](#a41c8de9c20bfde59577ca85f116fa0c4)。

端口 1、引脚 14 的编码定义（P1_14）。

<a id="r_ae5aa504f54ca4e7aead6e0af6f4e2a2b"></a>

```c
#define P1_15 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_15, IOCON_INDEX_PIO1_15)
```

相关声明：[P1_15](#ae5aa504f54ca4e7aead6e0af6f4e2a2b)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P1_15](#acdfb1a7fd999f47af355165da0d3f409)、[IOCON_INDEX_PIO1_15](#ac5c6d1976ebf3497a0afee4b65d0f9df)。

端口 1、引脚 15 的编码定义（P1_15）。

<a id="r_a68ec273c755729a01891115ab5371192"></a>

```c
#define P1_16 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_16, IOCON_INDEX_PIO1_16)
```

相关声明：[P1_16](#a68ec273c755729a01891115ab5371192)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P1_16](#a2a617a3f8d0aa25d59376877ffcd4eb4)、[IOCON_INDEX_PIO1_16](#add4d86d2f1b70b0b812f20b07835e5d6)。

端口 1、引脚 16 的编码定义（P1_16）。

<a id="r_a6058a5071b9b013c16fd14a332c7362a"></a>

```c
#define P1_17 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_17, IOCON_INDEX_PIO1_17)
```

相关声明：[P1_17](#a6058a5071b9b013c16fd14a332c7362a)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P1_17](#a002faae4383ef826041a62e21b6829ec)、[IOCON_INDEX_PIO1_17](#a68096db7c329d2e428afb7aef3b8f741)。

端口 1、引脚 17 的编码定义（P1_17）。

<a id="r_a4dc67e818b0aca5796d09f38167c80d4"></a>

```c
#define P1_18 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_18, IOCON_INDEX_PIO1_18)
```

相关声明：[P1_18](#a4dc67e818b0aca5796d09f38167c80d4)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P1_18](#a855bcacd31749728c846bf82f67b7092)、[IOCON_INDEX_PIO1_18](#a4c15e46e445b96e42a748e3841c80905)。

端口 1、引脚 18 的编码定义（P1_18）。

<a id="r_af0657880bb6b8f7c1fe4bfeb1a882636"></a>

```c
#define P1_19 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_19, IOCON_INDEX_PIO1_19)
```

相关声明：[P1_19](#af0657880bb6b8f7c1fe4bfeb1a882636)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P1_19](#acda3cbfed8a5a620e8123b3a7d18504e)、[IOCON_INDEX_PIO1_19](#a36930c4c2a9e11c8b93700d34e3d014a)。

端口 1、引脚 19 的编码定义（P1_19）。

<a id="r_a7559fc173a9ea1f713f1a0f47c273e84"></a>

```c
#define P1_20 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_20, IOCON_INDEX_PIO1_20)
```

相关声明：[P1_20](#a7559fc173a9ea1f713f1a0f47c273e84)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P1_20](#a353fa50280a90834a1b65f88952e9dbe)、[IOCON_INDEX_PIO1_20](#a1e2353b87dcfa461edcfc65591531f9a)。

端口 1、引脚 20 的编码定义（P1_20）。

<a id="r_a10f3670e885fcc7435cc8321a0b1bc77"></a>

```c
#define P1_21 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_21, IOCON_INDEX_PIO1_21)
```

相关声明：[P1_21](#a10f3670e885fcc7435cc8321a0b1bc77)、[LPC84X_PIN_DEFINE](#a667b43fb3d023097f21f1e518a46487b)、[LPC84X_PIN_P1_21](#a8a0eb588bea92a849fc7831ad0d4c7ee)、[IOCON_INDEX_PIO1_21](#ab1087f12fcbc3e33026333b0d95486ab)。

端口 1、引脚 21 的编码定义（P1_21）。

## 4.2\_详细说明（Detailed Documentation）

<a id="af590d3cdf4c00bb210c4b787bdebac2f"></a>

### `IOCON_INDEX_PIO0_0`

```c
#define IOCON_INDEX_PIO0_0 17U
```

`PIO0_0` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="ac7212fca24c63173ec6b8f3f2a3c872d"></a>

### `IOCON_INDEX_PIO0_1`

```c
#define IOCON_INDEX_PIO0_1 11U
```

`PIO0_1` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a95b0b1f5ba94efdccb48d50765449ffd"></a>

### `IOCON_INDEX_PIO0_10`

```c
#define IOCON_INDEX_PIO0_10 8U
```

`PIO0_10` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a8701f5b4a3e1541d05b91891b3dc6008"></a>

### `IOCON_INDEX_PIO0_11`

```c
#define IOCON_INDEX_PIO0_11 7U
```

`PIO0_11` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="ab8132dff3d1740acf63d3d3a77daaa01"></a>

### `IOCON_INDEX_PIO0_12`

```c
#define IOCON_INDEX_PIO0_12 2U
```

`PIO0_12` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="aa8fae44b1a4eb04c413acff8c6e3fa53"></a>

### `IOCON_INDEX_PIO0_13`

```c
#define IOCON_INDEX_PIO0_13 1U
```

`PIO0_13` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a5591b72823931380f275ced24a88680e"></a>

### `IOCON_INDEX_PIO0_14`

```c
#define IOCON_INDEX_PIO0_14 18U
```

`PIO0_14` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a714a6dbfe29e20a5e49a6161d1ecd65a"></a>

### `IOCON_INDEX_PIO0_15`

```c
#define IOCON_INDEX_PIO0_15 10U
```

`PIO0_15` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="ae93fca701eac78d0fc01bf572d6235e7"></a>

### `IOCON_INDEX_PIO0_16`

```c
#define IOCON_INDEX_PIO0_16 9U
```

`PIO0_16` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a812f7f0c3e5fd4c4f6008b3acc8545ec"></a>

### `IOCON_INDEX_PIO0_17`

```c
#define IOCON_INDEX_PIO0_17 0U
```

各个 PIO 引脚的 I/O 配置寄存器索引（IOCON Register Indices）。

编号反映硬件 IOCON 寄存器的排列顺序，并不严格按照端口／引脚的数值顺序排列。此项为 `PIO0_17` 的 IOCON 索引（Index）。

<a id="ae87a8df1d5dbee171c87a5b2e027692e"></a>

### `IOCON_INDEX_PIO0_18`

```c
#define IOCON_INDEX_PIO0_18 30U
```

`PIO0_18` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="aaa9552c40eefbe868885ead9ac0b0d6d"></a>

### `IOCON_INDEX_PIO0_19`

```c
#define IOCON_INDEX_PIO0_19 29U
```

`PIO0_19` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="aa8a70f51d8cbf6e3c3bb71a15136dd4b"></a>

### `IOCON_INDEX_PIO0_2`

```c
#define IOCON_INDEX_PIO0_2 6U
```

`PIO0_2` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a844ff895b8ce20c058d7426b27fff258"></a>

### `IOCON_INDEX_PIO0_20`

```c
#define IOCON_INDEX_PIO0_20 28U
```

`PIO0_20` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a939739de8e85dcd42d15d27521c21d42"></a>

### `IOCON_INDEX_PIO0_21`

```c
#define IOCON_INDEX_PIO0_21 27U
```

`PIO0_21` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a96133f3494e1234dd623c19b06f0e671"></a>

### `IOCON_INDEX_PIO0_22`

```c
#define IOCON_INDEX_PIO0_22 26U
```

`PIO0_22` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="ab74d912ebd2193df3569ebc0ab92ea63"></a>

### `IOCON_INDEX_PIO0_23`

```c
#define IOCON_INDEX_PIO0_23 25U
```

`PIO0_23` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="ac6d0f09cd357c98ad1099aeb6f31a68c"></a>

### `IOCON_INDEX_PIO0_24`

```c
#define IOCON_INDEX_PIO0_24 24U
```

`PIO0_24` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a5f38f18d95a17db2f078ef65a18acb8a"></a>

### `IOCON_INDEX_PIO0_25`

```c
#define IOCON_INDEX_PIO0_25 23U
```

`PIO0_25` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a134a7f3d9318c9448a4dcee62235c645"></a>

### `IOCON_INDEX_PIO0_26`

```c
#define IOCON_INDEX_PIO0_26 22U
```

`PIO0_26` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a06c05877b9033538a32575d0a66e5a4f"></a>

### `IOCON_INDEX_PIO0_27`

```c
#define IOCON_INDEX_PIO0_27 21U
```

`PIO0_27` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a58338a9d9ec1b0a0d985627f824aea56"></a>

### `IOCON_INDEX_PIO0_28`

```c
#define IOCON_INDEX_PIO0_28 20U
```

`PIO0_28` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a6e2783040ea48a5d2d35db26fdcf9f62"></a>

### `IOCON_INDEX_PIO0_29`

```c
#define IOCON_INDEX_PIO0_29 50U
```

`PIO0_29` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="ad970910091aec2eeba6898bab250e5e8"></a>

### `IOCON_INDEX_PIO0_3`

```c
#define IOCON_INDEX_PIO0_3 5U
```

`PIO0_3` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a8853f1c47d0d1834e798cb50aa1eadc3"></a>

### `IOCON_INDEX_PIO0_30`

```c
#define IOCON_INDEX_PIO0_30 51U
```

`PIO0_30` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a0e206c7900cf7a59f02721879e01c4af"></a>

### `IOCON_INDEX_PIO0_31`

```c
#define IOCON_INDEX_PIO0_31 35U
```

`PIO0_31` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a0182178b00ef4bdbf7ff06361d18bd25"></a>

### `IOCON_INDEX_PIO0_4`

```c
#define IOCON_INDEX_PIO0_4 4U
```

`PIO0_4` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a4c5f119685abb8924e0afd61b014a22f"></a>

### `IOCON_INDEX_PIO0_5`

```c
#define IOCON_INDEX_PIO0_5 3U
```

`PIO0_5` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="afd4e4d9f4f3b44b055f76a92af9dacb1"></a>

### `IOCON_INDEX_PIO0_6`

```c
#define IOCON_INDEX_PIO0_6 16U
```

`PIO0_6` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="ae3fd1aadc876363556e5104670208e67"></a>

### `IOCON_INDEX_PIO0_7`

```c
#define IOCON_INDEX_PIO0_7 15U
```

`PIO0_7` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a5a646d435da4e16eefcfb7ec589a8f2f"></a>

### `IOCON_INDEX_PIO0_8`

```c
#define IOCON_INDEX_PIO0_8 14U
```

`PIO0_8` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a4d6795d619fdadc07a892f0ea0c7b59b"></a>

### `IOCON_INDEX_PIO0_9`

```c
#define IOCON_INDEX_PIO0_9 13U
```

`PIO0_9` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="af379aa275eb85f091ece4aea39e02db4"></a>

### `IOCON_INDEX_PIO1_0`

```c
#define IOCON_INDEX_PIO1_0 36U
```

`PIO1_0` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="ae75433b3291dc9a506a90519127ad0d6"></a>

### `IOCON_INDEX_PIO1_1`

```c
#define IOCON_INDEX_PIO1_1 37U
```

`PIO1_1` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="ae23a124c69b44d2f20dd19cf635bf6f5"></a>

### `IOCON_INDEX_PIO1_10`

```c
#define IOCON_INDEX_PIO1_10 55U
```

`PIO1_10` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a9d3e24edf0c7ce480b47d9b394f18652"></a>

### `IOCON_INDEX_PIO1_11`

```c
#define IOCON_INDEX_PIO1_11 54U
```

`PIO1_11` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a849ccc703bb8fe6cb247e71bec25eb31"></a>

### `IOCON_INDEX_PIO1_12`

```c
#define IOCON_INDEX_PIO1_12 33U
```

`PIO1_12` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a97946b31c966d422c4d65505d17eb005"></a>

### `IOCON_INDEX_PIO1_13`

```c
#define IOCON_INDEX_PIO1_13 34U
```

`PIO1_13` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a41c8de9c20bfde59577ca85f116fa0c4"></a>

### `IOCON_INDEX_PIO1_14`

```c
#define IOCON_INDEX_PIO1_14 39U
```

`PIO1_14` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="ac5c6d1976ebf3497a0afee4b65d0f9df"></a>

### `IOCON_INDEX_PIO1_15`

```c
#define IOCON_INDEX_PIO1_15 40U
```

`PIO1_15` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="add4d86d2f1b70b0b812f20b07835e5d6"></a>

### `IOCON_INDEX_PIO1_16`

```c
#define IOCON_INDEX_PIO1_16 44U
```

`PIO1_16` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a68096db7c329d2e428afb7aef3b8f741"></a>

### `IOCON_INDEX_PIO1_17`

```c
#define IOCON_INDEX_PIO1_17 45U
```

`PIO1_17` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a4c15e46e445b96e42a748e3841c80905"></a>

### `IOCON_INDEX_PIO1_18`

```c
#define IOCON_INDEX_PIO1_18 47U
```

`PIO1_18` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a36930c4c2a9e11c8b93700d34e3d014a"></a>

### `IOCON_INDEX_PIO1_19`

```c
#define IOCON_INDEX_PIO1_19 48U
```

`PIO1_19` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="af25e594edb962c83d5ef395a460a3515"></a>

### `IOCON_INDEX_PIO1_2`

```c
#define IOCON_INDEX_PIO1_2 38U
```

`PIO1_2` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a1e2353b87dcfa461edcfc65591531f9a"></a>

### `IOCON_INDEX_PIO1_20`

```c
#define IOCON_INDEX_PIO1_20 52U
```

`PIO1_20` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="ab1087f12fcbc3e33026333b0d95486ab"></a>

### `IOCON_INDEX_PIO1_21`

```c
#define IOCON_INDEX_PIO1_21 53U
```

`PIO1_21` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="afba39be87ed475934fc9f53a0cb60a7b"></a>

### `IOCON_INDEX_PIO1_3`

```c
#define IOCON_INDEX_PIO1_3 41U
```

`PIO1_3` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a0b99a3ccdfcd666763d3af17ce5fc952"></a>

### `IOCON_INDEX_PIO1_4`

```c
#define IOCON_INDEX_PIO1_4 42U
```

`PIO1_4` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a23fe120736e0ac3f0cc285a70d4867ba"></a>

### `IOCON_INDEX_PIO1_5`

```c
#define IOCON_INDEX_PIO1_5 43U
```

`PIO1_5` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a152e2c9bfaa506dcc40b03d7ad3d312c"></a>

### `IOCON_INDEX_PIO1_6`

```c
#define IOCON_INDEX_PIO1_6 46U
```

`PIO1_6` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a0c26e1fe920bbe065464664850423908"></a>

### `IOCON_INDEX_PIO1_7`

```c
#define IOCON_INDEX_PIO1_7 49U
```

`PIO1_7` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="af44de783a68a52a8b2c11b8fff5faa21"></a>

### `IOCON_INDEX_PIO1_8`

```c
#define IOCON_INDEX_PIO1_8 31U
```

`PIO1_8` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a47304bfe7384a074b1c80da21fc38454"></a>

### `IOCON_INDEX_PIO1_9`

```c
#define IOCON_INDEX_PIO1_9 32U
```

`PIO1_9` 的 I/O 配置寄存器索引（IOCON Index）。

<a id="a667b43fb3d023097f21f1e518a46487b"></a>

### `LPC84X_PIN_DEFINE`

```c
#define LPC84X_PIN_DEFINE ( swm, iocon )
```

展开值（Value）：

```c
((((swm) & 0xFF) << 8) | ((iocon) & 0xFF))
```

将开关矩阵（SWM）功能和 IOCON 索引编码为单个 16 位值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `swm` | 开关矩阵（SWM）功能或端口引脚标识符（Port Pin Identifier）。 |
| `iocon` | I/O 配置寄存器索引（IOCON Register Index）。 |

<a id="ad1db232d88079d3dc03d37d804202f6d"></a>

### `LPC84X_PIN_P0_0`

```c
#define LPC84X_PIN_P0_0 0U
```

开关矩阵（SWM）使用的物理端口引脚标识符（Physical Port Pin Identifiers）。

端口 0 的引脚范围为 0～31，端口 1 的引脚继续顺序编号。此项为 `P0.0`。

<a id="a9c5d720377518adb657a21daa4cd4f48"></a>

### `LPC84X_PIN_P0_1`

```c
#define LPC84X_PIN_P0_1 1U
```

物理端口 0 的引脚 1（P0.1）。

<a id="a50a2252ad3383cf9661d63bcaf7ecaa0"></a>

### `LPC84X_PIN_P0_10`

```c
#define LPC84X_PIN_P0_10 10U
```

物理端口 0 的引脚 10（P0.10）。

<a id="a86ee0bb5a00aa6a5a59cd7b4e7a5caa7"></a>

### `LPC84X_PIN_P0_11`

```c
#define LPC84X_PIN_P0_11 11U
```

物理端口 0 的引脚 11（P0.11）。

<a id="add1c1b6463517c45f9f6ac3a8eeab50c"></a>

### `LPC84X_PIN_P0_12`

```c
#define LPC84X_PIN_P0_12 12U
```

物理端口 0 的引脚 12（P0.12）。

<a id="a954de42869f3990c3ea795c918f2731a"></a>

### `LPC84X_PIN_P0_13`

```c
#define LPC84X_PIN_P0_13 13U
```

物理端口 0 的引脚 13（P0.13）。

<a id="ad496e70ef5c3c10792d40db26e254595"></a>

### `LPC84X_PIN_P0_14`

```c
#define LPC84X_PIN_P0_14 14U
```

物理端口 0 的引脚 14（P0.14）。

<a id="a939675ff4fde16f666f4042459af8d5c"></a>

### `LPC84X_PIN_P0_15`

```c
#define LPC84X_PIN_P0_15 15U
```

物理端口 0 的引脚 15（P0.15）。

<a id="ae8b87af4800075e0aab2ffb2ad2c8403"></a>

### `LPC84X_PIN_P0_16`

```c
#define LPC84X_PIN_P0_16 16U
```

物理端口 0 的引脚 16（P0.16）。

<a id="ae2fafc086e64954c7a67e7835642b4e0"></a>

### `LPC84X_PIN_P0_17`

```c
#define LPC84X_PIN_P0_17 17U
```

物理端口 0 的引脚 17（P0.17）。

<a id="aed5527e15df460a7fb11b1090eed3dd4"></a>

### `LPC84X_PIN_P0_18`

```c
#define LPC84X_PIN_P0_18 18U
```

物理端口 0 的引脚 18（P0.18）。

<a id="ab81e06da645e790a33b1a3b2e841694b"></a>

### `LPC84X_PIN_P0_19`

```c
#define LPC84X_PIN_P0_19 19U
```

物理端口 0 的引脚 19（P0.19）。

<a id="adac57525cb318956d67bd5f11200a5cc"></a>

### `LPC84X_PIN_P0_2`

```c
#define LPC84X_PIN_P0_2 2U
```

物理端口 0 的引脚 2（P0.2）。

<a id="adf53e74fc9566608db9f135dac2c950b"></a>

### `LPC84X_PIN_P0_20`

```c
#define LPC84X_PIN_P0_20 20U
```

物理端口 0 的引脚 20（P0.20）。

<a id="a7b39f7f1db0490e8d6c802d18a00cb56"></a>

### `LPC84X_PIN_P0_21`

```c
#define LPC84X_PIN_P0_21 21U
```

物理端口 0 的引脚 21（P0.21）。

<a id="aeafae23924726cba2f97b4ba85b50bdf"></a>

### `LPC84X_PIN_P0_22`

```c
#define LPC84X_PIN_P0_22 22U
```

物理端口 0 的引脚 22（P0.22）。

<a id="a7fc3556913c5bbdcc4f7a5604a965b60"></a>

### `LPC84X_PIN_P0_23`

```c
#define LPC84X_PIN_P0_23 23U
```

物理端口 0 的引脚 23（P0.23）。

<a id="a8e99f41a7c871ec0713a2e50bc1cd18b"></a>

### `LPC84X_PIN_P0_24`

```c
#define LPC84X_PIN_P0_24 24U
```

物理端口 0 的引脚 24（P0.24）。

<a id="a492660c4bc270ca4ceee05f68c0044ac"></a>

### `LPC84X_PIN_P0_25`

```c
#define LPC84X_PIN_P0_25 25U
```

物理端口 0 的引脚 25（P0.25）。

<a id="a24cee95c6b1f7d963b19f5050804eb84"></a>

### `LPC84X_PIN_P0_26`

```c
#define LPC84X_PIN_P0_26 26U
```

物理端口 0 的引脚 26（P0.26）。

<a id="a64338dd7064270a6d57082ea500bce90"></a>

### `LPC84X_PIN_P0_27`

```c
#define LPC84X_PIN_P0_27 27U
```

物理端口 0 的引脚 27（P0.27）。

<a id="af99fd2bde296a1714ab8571916751249"></a>

### `LPC84X_PIN_P0_28`

```c
#define LPC84X_PIN_P0_28 28U
```

物理端口 0 的引脚 28（P0.28）。

<a id="a8e6fa11cf07b3cc86c662170daa59027"></a>

### `LPC84X_PIN_P0_29`

```c
#define LPC84X_PIN_P0_29 29U
```

物理端口 0 的引脚 29（P0.29）。

<a id="a53b0780c5a66ddbd1475d069218e7395"></a>

### `LPC84X_PIN_P0_3`

```c
#define LPC84X_PIN_P0_3 3U
```

物理端口 0 的引脚 3（P0.3）。

<a id="ae8e0097f15e14f7a4b5b6e8fb61e9fd5"></a>

### `LPC84X_PIN_P0_30`

```c
#define LPC84X_PIN_P0_30 30U
```

物理端口 0 的引脚 30（P0.30）。

<a id="a252678b971ff6a6feaff2d64c32c4b62"></a>

### `LPC84X_PIN_P0_31`

```c
#define LPC84X_PIN_P0_31 31U
```

物理端口 0 的引脚 31（P0.31）。

<a id="a4b8030696a58d736aa33d92d1d6b0a73"></a>

### `LPC84X_PIN_P0_4`

```c
#define LPC84X_PIN_P0_4 4U
```

物理端口 0 的引脚 4（P0.4）。

<a id="ae413bbd918fefa03f8b9c8f068876ab5"></a>

### `LPC84X_PIN_P0_5`

```c
#define LPC84X_PIN_P0_5 5U
```

物理端口 0 的引脚 5（P0.5）。

<a id="ae276bc41e9f9549d4a0907ebe2393e50"></a>

### `LPC84X_PIN_P0_6`

```c
#define LPC84X_PIN_P0_6 6U
```

物理端口 0 的引脚 6（P0.6）。

<a id="a6e979a3752bdc314a3e9571ac483a315"></a>

### `LPC84X_PIN_P0_7`

```c
#define LPC84X_PIN_P0_7 7U
```

物理端口 0 的引脚 7（P0.7）。

<a id="a2e5a4cb414a855564b08d9ae84b4d353"></a>

### `LPC84X_PIN_P0_8`

```c
#define LPC84X_PIN_P0_8 8U
```

物理端口 0 的引脚 8（P0.8）。

<a id="a06e1bbecaea97298ae05b11222e79d81"></a>

### `LPC84X_PIN_P0_9`

```c
#define LPC84X_PIN_P0_9 9U
```

物理端口 0 的引脚 9（P0.9）。

<a id="aee84abb418d835a5e4808572e5dc44cb"></a>

### `LPC84X_PIN_P1_0`

```c
#define LPC84X_PIN_P1_0 32U
```

物理端口 1 的引脚 0（P1.0）。

<a id="a93344eccc237d561bc99fad742fc56a8"></a>

### `LPC84X_PIN_P1_1`

```c
#define LPC84X_PIN_P1_1 33U
```

物理端口 1 的引脚 1（P1.1）。

<a id="aaaa008010a094f6d95ffa4fbdd0af0d9"></a>

### `LPC84X_PIN_P1_10`

```c
#define LPC84X_PIN_P1_10 42U
```

物理端口 1 的引脚 10（P1.10）。

<a id="a34bbe8474ebe8adc19f1c9614e633fcf"></a>

### `LPC84X_PIN_P1_11`

```c
#define LPC84X_PIN_P1_11 43U
```

物理端口 1 的引脚 11（P1.11）。

<a id="a8161771007830581048f4e2a00c8f1ee"></a>

### `LPC84X_PIN_P1_12`

```c
#define LPC84X_PIN_P1_12 44U
```

物理端口 1 的引脚 12（P1.12）。

<a id="a36e78c38a197f6cb62c7d772cccce5ee"></a>

### `LPC84X_PIN_P1_13`

```c
#define LPC84X_PIN_P1_13 45U
```

物理端口 1 的引脚 13（P1.13）。

<a id="aa151529a09ad8c8bea887035e327fcba"></a>

### `LPC84X_PIN_P1_14`

```c
#define LPC84X_PIN_P1_14 46U
```

物理端口 1 的引脚 14（P1.14）。

<a id="acdfb1a7fd999f47af355165da0d3f409"></a>

### `LPC84X_PIN_P1_15`

```c
#define LPC84X_PIN_P1_15 47U
```

物理端口 1 的引脚 15（P1.15）。

<a id="a2a617a3f8d0aa25d59376877ffcd4eb4"></a>

### `LPC84X_PIN_P1_16`

```c
#define LPC84X_PIN_P1_16 48U
```

物理端口 1 的引脚 16（P1.16）。

<a id="a002faae4383ef826041a62e21b6829ec"></a>

### `LPC84X_PIN_P1_17`

```c
#define LPC84X_PIN_P1_17 49U
```

物理端口 1 的引脚 17（P1.17）。

<a id="a855bcacd31749728c846bf82f67b7092"></a>

### `LPC84X_PIN_P1_18`

```c
#define LPC84X_PIN_P1_18 50U
```

物理端口 1 的引脚 18（P1.18）。

<a id="acda3cbfed8a5a620e8123b3a7d18504e"></a>

### `LPC84X_PIN_P1_19`

```c
#define LPC84X_PIN_P1_19 51U
```

物理端口 1 的引脚 19（P1.19）。

<a id="a8fbd1e8c148b573ef70b724bdc52ab4b"></a>

### `LPC84X_PIN_P1_2`

```c
#define LPC84X_PIN_P1_2 34U
```

物理端口 1 的引脚 2（P1.2）。

<a id="a353fa50280a90834a1b65f88952e9dbe"></a>

### `LPC84X_PIN_P1_20`

```c
#define LPC84X_PIN_P1_20 52U
```

物理端口 1 的引脚 20（P1.20）。

<a id="a8a0eb588bea92a849fc7831ad0d4c7ee"></a>

### `LPC84X_PIN_P1_21`

```c
#define LPC84X_PIN_P1_21 53U
```

物理端口 1 的引脚 21（P1.21）。

<a id="a790372b446722ed6d0fa4e106c707c36"></a>

### `LPC84X_PIN_P1_3`

```c
#define LPC84X_PIN_P1_3 35U
```

物理端口 1 的引脚 3（P1.3）。

<a id="ab006b7e3e68307fc36a062a8a7f20be4"></a>

### `LPC84X_PIN_P1_4`

```c
#define LPC84X_PIN_P1_4 36U
```

物理端口 1 的引脚 4（P1.4）。

<a id="aa0f7020d52e0bbb93c5acd058259fe44"></a>

### `LPC84X_PIN_P1_5`

```c
#define LPC84X_PIN_P1_5 37U
```

物理端口 1 的引脚 5（P1.5）。

<a id="a6608806c2def3a62d368801af5e26544"></a>

### `LPC84X_PIN_P1_6`

```c
#define LPC84X_PIN_P1_6 38U
```

物理端口 1 的引脚 6（P1.6）。

<a id="a29e5093202be45edf212e64d405e5503"></a>

### `LPC84X_PIN_P1_7`

```c
#define LPC84X_PIN_P1_7 39U
```

物理端口 1 的引脚 7（P1.7）。

<a id="afa72534a3bb1d644096c1b8f219db3b2"></a>

### `LPC84X_PIN_P1_8`

```c
#define LPC84X_PIN_P1_8 40U
```

物理端口 1 的引脚 8（P1.8）。

<a id="aa55a1e578517a4d29570bc4fa21e2fd7"></a>

### `LPC84X_PIN_P1_9`

```c
#define LPC84X_PIN_P1_9 41U
```

物理端口 1 的引脚 9（P1.9）。

<a id="ab0727a736c6bc193fab9e2871e95dea7"></a>

### `LPC84X_PINMUX_F`

```c
#define LPC84X_PINMUX_F ( func, pin )
```

展开值（Value）：

```c
((1U << 23) | ((func) << 16) | (pin))
```

将固定开关矩阵（SWM）功能与引脚值一起编码。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `func` | 开关矩阵功能编号（Switch Matrix Function Number）。 |
| `pin` | 物理端口引脚编号（Physical Port Pin Number）。固定引脚复用编码器（Fixed Pinmux Encoder）。译注：原文两部分之间的 `<` 是注释标记残留。 |

<a id="acaaf1d2ee32fb366037c7e7e22836f45"></a>

### `LPC84X_PINMUX_M`

```c
#define LPC84X_PINMUX_M ( func, pin )
```

展开值（Value）：

```c
(((func) << 16) | (pin))
```

将可移动开关矩阵（SWM）功能与引脚值一起编码。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `func` | 开关矩阵功能编号（Switch Matrix Function Number）。 |
| `pin` | 物理端口引脚编号（Physical Port Pin Number）。可移动引脚复用编码器（Movable Pinmux Encoder）。译注：原文两部分之间的 `<` 是注释标记残留。 |

<a id="a7691b60528e0d62c707b5720ca1f9b78"></a>

### `LPC84X_SWM_ACMP_INPUT1`

```c
#define LPC84X_SWM_ACMP_INPUT1 0U
```

模拟比较器（ACMP）输入 1（INPUT1）。

<a id="abc7d67d7558ff10226a7b86cd00fd52e"></a>

### `LPC84X_SWM_ACMP_INPUT2`

```c
#define LPC84X_SWM_ACMP_INPUT2 1U
```

模拟比较器（ACMP）输入 2（INPUT2）。

<a id="accbb115933ceb9f22d841a6572f545e5"></a>

### `LPC84X_SWM_ACMP_INPUT3`

```c
#define LPC84X_SWM_ACMP_INPUT3 2U
```

模拟比较器（ACMP）输入 3（INPUT3）。

<a id="a20afafa92b39c750dd534659da25576c"></a>

### `LPC84X_SWM_ACMP_INPUT4`

```c
#define LPC84X_SWM_ACMP_INPUT4 3U
```

模拟比较器（ACMP）输入 4（INPUT4）。

<a id="a64a026241812aa372402fdf9ea8e2a76"></a>

### `LPC84X_SWM_ACMP_INPUT5`

```c
#define LPC84X_SWM_ACMP_INPUT5 4U
```

模拟比较器（ACMP）输入 5（INPUT5）。

<a id="ab37fb81e230d909ec8ee2cd9ebc20d17"></a>

### `LPC84X_SWM_ACMP_OUT`

```c
#define LPC84X_SWM_ACMP_OUT 44U
```

模拟比较器输出（ACMP OUT）。

<a id="a5c0bf8dff9776a4307314b65226acd14"></a>

### `LPC84X_SWM_ADC_CHN0`

```c
#define LPC84X_SWM_ADC_CHN0 14U
```

模数转换器（ADC）通道 0（CHN0）。

<a id="a465895d878192fd981b4c0578ac790e1"></a>

### `LPC84X_SWM_ADC_CHN1`

```c
#define LPC84X_SWM_ADC_CHN1 15U
```

模数转换器（ADC）通道 1（CHN1）。

<a id="aea71ceb94feb7d17038ea2ab2470d845"></a>

### `LPC84X_SWM_ADC_CHN10`

```c
#define LPC84X_SWM_ADC_CHN10 24U
```

模数转换器（ADC）通道 10（CHN10）。

<a id="a9d216af07271614bb072abc4662efabb"></a>

### `LPC84X_SWM_ADC_CHN11`

```c
#define LPC84X_SWM_ADC_CHN11 25U
```

模数转换器（ADC）通道 11（CHN11）。

<a id="a62af44fdbffd4a9266ff02e0993fcead"></a>

### `LPC84X_SWM_ADC_CHN2`

```c
#define LPC84X_SWM_ADC_CHN2 16U
```

模数转换器（ADC）通道 2（CHN2）。

<a id="a8ba1befda57559d57f29a0ba20e76a73"></a>

### `LPC84X_SWM_ADC_CHN3`

```c
#define LPC84X_SWM_ADC_CHN3 17U
```

模数转换器（ADC）通道 3（CHN3）。

<a id="a74b73703d7cd4c1eb47af5840080887b"></a>

### `LPC84X_SWM_ADC_CHN4`

```c
#define LPC84X_SWM_ADC_CHN4 18U
```

模数转换器（ADC）通道 4（CHN4）。

<a id="a9d6dfa425b4c122b3550d255eaaffb5a"></a>

### `LPC84X_SWM_ADC_CHN5`

```c
#define LPC84X_SWM_ADC_CHN5 19U
```

模数转换器（ADC）通道 5（CHN5）。

<a id="a453724b82e0f480a4af2928dca3e8adb"></a>

### `LPC84X_SWM_ADC_CHN6`

```c
#define LPC84X_SWM_ADC_CHN6 20U
```

模数转换器（ADC）通道 6（CHN6）。

<a id="a8f0415ee862278497ebaf3cdb3fd5db6"></a>

### `LPC84X_SWM_ADC_CHN7`

```c
#define LPC84X_SWM_ADC_CHN7 21U
```

模数转换器（ADC）通道 7（CHN7）。

<a id="a7930d56a3cc2464a6d701fc332be143e"></a>

### `LPC84X_SWM_ADC_CHN8`

```c
#define LPC84X_SWM_ADC_CHN8 22U
```

模数转换器（ADC）通道 8（CHN8）。

<a id="acd4d965df7a821edfe312cec56b16178"></a>

### `LPC84X_SWM_ADC_CHN9`

```c
#define LPC84X_SWM_ADC_CHN9 23U
```

模数转换器（ADC）通道 9（CHN9）。

<a id="a8c91d228709a955c363ae548460f90f4"></a>

### `LPC84X_SWM_CAPT_X0`

```c
#define LPC84X_SWM_CAPT_X0 28U
```

`CAPT_X0`，互电容触摸传感器（Mutual Capacitance Touch Sensor）信号。

<a id="ad3e8d0c824f18b3788f3acdb0e69d8eb"></a>

### `LPC84X_SWM_CAPT_X1`

```c
#define LPC84X_SWM_CAPT_X1 29U
```

电容触摸（CAPT）X1 信号。

<a id="ade79d2747b4e20c5d4ae7768b964d80b"></a>

### `LPC84X_SWM_CAPT_X2`

```c
#define LPC84X_SWM_CAPT_X2 30U
```

电容触摸（CAPT）X2 信号。

<a id="a61c135bd890c11bdaf7e81ed0fed324c"></a>

### `LPC84X_SWM_CAPT_X3`

```c
#define LPC84X_SWM_CAPT_X3 31U
```

电容触摸（CAPT）X3 信号。

<a id="a48e869dffcb2c6ef9d2e87f5b9b78064"></a>

### `LPC84X_SWM_CAPT_X4`

```c
#define LPC84X_SWM_CAPT_X4 32U
```

`CAPT_X4`，从此处开始进入 `PINENABLE1` 范围。

<a id="a56d9487bcc018f294448e79a757f02eb"></a>

### `LPC84X_SWM_CAPT_X5`

```c
#define LPC84X_SWM_CAPT_X5 33U
```

电容触摸（CAPT）X5 信号。

<a id="a9dd7c7191485b22f8c26517113c7a2a6"></a>

### `LPC84X_SWM_CAPT_X6`

```c
#define LPC84X_SWM_CAPT_X6 34U
```

电容触摸（CAPT）X6 信号。

<a id="a1157debd93302c3e8a33784134bf5a0e"></a>

### `LPC84X_SWM_CAPT_X7`

```c
#define LPC84X_SWM_CAPT_X7 35U
```

电容触摸（CAPT）X7 信号。

<a id="aa872037286dc99a4ab53a6177ad5ffed"></a>

### `LPC84X_SWM_CAPT_X8`

```c
#define LPC84X_SWM_CAPT_X8 36U
```

电容触摸（CAPT）X8 信号。

<a id="a30467b5eedcf2517d7e31b39936f463c"></a>

### `LPC84X_SWM_CAPT_YH`

```c
#define LPC84X_SWM_CAPT_YH 38U
```

电容触摸（CAPT）的 `YH` 信号。

<a id="af103b906a18d9105ae80b62030790faf"></a>

### `LPC84X_SWM_CAPT_YL`

```c
#define LPC84X_SWM_CAPT_YL 37U
```

`CAPT_YL`，测量电容（Measurement Capacitor）信号。

<a id="ae83b0c2582e5e44c46920dd92eecbee0"></a>

### `LPC84X_SWM_CLKIN`

```c
#define LPC84X_SWM_CLKIN 10U
```

时钟输入（CLKIN）。

<a id="a52d5aa18eace1d91ba21f9e9368c40a1"></a>

### `LPC84X_SWM_CLKOUT`

```c
#define LPC84X_SWM_CLKOUT 45U
```

时钟输出（CLKOUT）。

<a id="afd739ffe20ac16e04dedfd93761f1451"></a>

### `LPC84X_SWM_DAC_OUT0`

```c
#define LPC84X_SWM_DAC_OUT0 26U
```

数模转换器（DAC）输出 0（DACOUT0）。

<a id="a229765f5da8c78db4a1b10249eec39a3"></a>

### `LPC84X_SWM_DAC_OUT1`

```c
#define LPC84X_SWM_DAC_OUT1 27U
```

数模转换器（DAC）输出 1（DACOUT1）。

<a id="ae53624c1e12af319476ed6a7df25d538"></a>

### `LPC84X_SWM_GPIO_INT_BMAT`

```c
#define LPC84X_SWM_GPIO_INT_BMAT 46U
```

GPIO 中断位模式匹配（GPIO INT BMAT）。

<a id="a4a3c86b11b8aefc3e7a5551f4f67691e"></a>

### `LPC84X_SWM_I2C0_SCL`

```c
#define LPC84X_SWM_I2C0_SCL 13U
```

I2C0 的串行时钟信号（SCL）。

<a id="a90cde2f1d850711c114ba9bdcf6f00ba"></a>

### `LPC84X_SWM_I2C0_SDA`

```c
#define LPC84X_SWM_I2C0_SDA 12U
```

I2C0 的串行数据信号（SDA）。

<a id="a8e6ae90b31d83731fb142e09625a8448"></a>

### `LPC84X_SWM_I2C1_SCL`

```c
#define LPC84X_SWM_I2C1_SCL 39U
```

I2C1 串行时钟线（SCL）。

<a id="ac4550602c05f5cc2ac09b4866499c9fc"></a>

### `LPC84X_SWM_I2C1_SDA`

```c
#define LPC84X_SWM_I2C1_SDA 38U
```

I2C1 串行数据线（SDA）。

<a id="a76fc0a0b65e3304795ccb4a98f1dc5b3"></a>

### `LPC84X_SWM_I2C2_SCL`

```c
#define LPC84X_SWM_I2C2_SCL 41U
```

I2C2 串行时钟线（SCL）。

<a id="ab4b95de9de86e27aa220bf3a149435c5"></a>

### `LPC84X_SWM_I2C2_SDA`

```c
#define LPC84X_SWM_I2C2_SDA 40U
```

I2C2 串行数据线（SDA）。

<a id="a6d2a0b0cda64d31e14dd58cee1a732d9"></a>

### `LPC84X_SWM_I2C3_SCL`

```c
#define LPC84X_SWM_I2C3_SCL 43U
```

I2C3 的串行时钟信号（SCL）。

<a id="a70c640997c6a8abfb92970acc5ff8393"></a>

### `LPC84X_SWM_I2C3_SDA`

```c
#define LPC84X_SWM_I2C3_SDA 42U
```

I2C3 的串行数据信号（SDA）。

<a id="a54f521185623827ea4d1bc8c214694f9"></a>

### `LPC84X_SWM_RESETN`

```c
#define LPC84X_SWM_RESETN 9U
```

低电平有效复位（RESETN）。

<a id="a8f25d84116452559701f0a8f7e8fc469"></a>

### `LPC84X_SWM_SCT_OUT0`

```c
#define LPC84X_SWM_SCT_OUT0 31U
```

状态可配置定时器（SCT）的输出 0（OUT0）。

<a id="a719762d810ae379081c73337225a1ce5"></a>

### `LPC84X_SWM_SCT_OUT1`

```c
#define LPC84X_SWM_SCT_OUT1 32U
```

状态可配置定时器（SCT）的输出 1（OUT1）。

<a id="ab16d0577efabf7f7c8efdd13d437519a"></a>

### `LPC84X_SWM_SCT_OUT2`

```c
#define LPC84X_SWM_SCT_OUT2 33U
```

状态可配置定时器（SCT）的输出 2（OUT2）。

<a id="afe1c01eaea889033cc72ed7534d972bb"></a>

### `LPC84X_SWM_SCT_OUT3`

```c
#define LPC84X_SWM_SCT_OUT3 34U
```

状态可配置定时器（SCT）的输出 3（OUT3）。

<a id="a2406226706b1e3b658c76490def32da7"></a>

### `LPC84X_SWM_SCT_OUT4`

```c
#define LPC84X_SWM_SCT_OUT4 35U
```

状态可配置定时器（SCT）的输出 4（OUT4）。

<a id="a24f81a0daa4ee314283ec2f70a5b8d09"></a>

### `LPC84X_SWM_SCT_OUT5`

```c
#define LPC84X_SWM_SCT_OUT5 36U
```

状态可配置定时器（SCT）的输出 5（OUT5）。

<a id="afa8f56a7eb135d37ebc0579d890ba0a6"></a>

### `LPC84X_SWM_SCT_OUT6`

```c
#define LPC84X_SWM_SCT_OUT6 37U
```

状态可配置定时器（SCT）的输出 6（OUT6）。

<a id="aabf9d14936713e5b2192ae46e305c1e9"></a>

### `LPC84X_SWM_SCT_PIN0`

```c
#define LPC84X_SWM_SCT_PIN0 27U
```

状态可配置定时器（SCT）的引脚 0（PIN0）。

<a id="a8f14ef73fedcc5ce674deb2a50182347"></a>

### `LPC84X_SWM_SCT_PIN1`

```c
#define LPC84X_SWM_SCT_PIN1 28U
```

状态可配置定时器（SCT）的引脚 1（PIN1）。

<a id="acbcb5ba8dd26803fc5debb7f17a8654a"></a>

### `LPC84X_SWM_SCT_PIN2`

```c
#define LPC84X_SWM_SCT_PIN2 29U
```

状态可配置定时器（SCT）的引脚 2（PIN2）。

<a id="a25e6a6f60a2fb014126746d13fea26ed"></a>

### `LPC84X_SWM_SCT_PIN3`

```c
#define LPC84X_SWM_SCT_PIN3 30U
```

状态可配置定时器（SCT）的引脚 3（PIN3）。

<a id="a55d59b546c19be6efae2eb48c14418ae"></a>

### `LPC84X_SWM_SPI0_MISO`

```c
#define LPC84X_SWM_SPI0_MISO 17U
```

SPI0 的主入从出数据信号（MISO）。

<a id="a31954d21676c226f6b7ed6859ce8d34a"></a>

### `LPC84X_SWM_SPI0_MOSI`

```c
#define LPC84X_SWM_SPI0_MOSI 16U
```

SPI0 的主出从入数据信号（MOSI）。

<a id="aaa2d03ad1e4b76d8500c2d27665b5db4"></a>

### `LPC84X_SWM_SPI0_SCK`

```c
#define LPC84X_SWM_SPI0_SCK 15U
```

SPI0 的串行时钟信号（SCK）。

<a id="ace44f6aafb6ea2fc42790a64baa3109a"></a>

### `LPC84X_SWM_SPI0_SSEL0`

```c
#define LPC84X_SWM_SPI0_SSEL0 18U
```

SPI0 的片选信号（SSEL0）。

<a id="a7a2db53a850fe6d2217912dcf594faa1"></a>

### `LPC84X_SWM_SPI0_SSEL1`

```c
#define LPC84X_SWM_SPI0_SSEL1 19U
```

SPI0 的片选信号（SSEL1）。

<a id="a3081ab35e4015d6474402773f27af6a4"></a>

### `LPC84X_SWM_SPI0_SSEL2`

```c
#define LPC84X_SWM_SPI0_SSEL2 20U
```

SPI0 的片选信号（SSEL2）。

<a id="ae1fe002f0e962a79105ba02c9426fdd3"></a>

### `LPC84X_SWM_SPI0_SSEL3`

```c
#define LPC84X_SWM_SPI0_SSEL3 21U
```

SPI0 的片选信号（SSEL3）。

<a id="a2fbef230d681d84953d32559b8d015d9"></a>

### `LPC84X_SWM_SPI1_MISO`

```c
#define LPC84X_SWM_SPI1_MISO 24U
```

SPI1 的主入从出数据信号（MISO）。

<a id="a6dc30ddc49ed74964718fef7c0f745eb"></a>

### `LPC84X_SWM_SPI1_MOSI`

```c
#define LPC84X_SWM_SPI1_MOSI 23U
```

SPI1 的主出从入数据信号（MOSI）。

<a id="ab2a4cd8a4f16ad11c67fb1e9a197e3a8"></a>

### `LPC84X_SWM_SPI1_SCK`

```c
#define LPC84X_SWM_SPI1_SCK 22U
```

SPI1 的串行时钟信号（SCK）。

<a id="ad48a83fc99a5ddc3c0b6e8253990bcaf"></a>

### `LPC84X_SWM_SPI1_SSEL0`

```c
#define LPC84X_SWM_SPI1_SSEL0 25U
```

SPI1 的片选信号（SSEL0）。

<a id="ad77983e61d9cf35872279c167aacb58c"></a>

### `LPC84X_SWM_SPI1_SSEL1`

```c
#define LPC84X_SWM_SPI1_SSEL1 26U
```

SPI1 的片选信号（SSEL1）。

<a id="a01acde3232b115b03d5d758a5844df7a"></a>

### `LPC84X_SWM_SWCLK`

```c
#define LPC84X_SWM_SWCLK 5U
```

串行线调试时钟（SWCLK）。

<a id="acc70eaa6551bd0d63ea76d03a2ed4e19"></a>

### `LPC84X_SWM_SWDIO`

```c
#define LPC84X_SWM_SWDIO 6U
```

串行线调试数据 I/O（SWDIO）。

<a id="adb226381e190df2edcc4c3bac6abe45e"></a>

### `LPC84X_SWM_T0_CAP_CHN0`

```c
#define LPC84X_SWM_T0_CAP_CHN0 57U
```

定时器 0（T0）的捕获通道 0（CAP CHN0）。

<a id="a96262593f6641a13890394cfcdb470ff"></a>

### `LPC84X_SWM_T0_CAP_CHN1`

```c
#define LPC84X_SWM_T0_CAP_CHN1 58U
```

定时器 0（T0）的捕获通道 1（CAP CHN1）。

<a id="a9da4cf6bf15135cf254e2c92b93c7b22"></a>

### `LPC84X_SWM_T0_CAP_CHN2`

```c
#define LPC84X_SWM_T0_CAP_CHN2 59U
```

定时器 0（T0）的捕获通道 2（CAP CHN2）。

<a id="a83a2626de3b6e698af987f890d709d7a"></a>

### `LPC84X_SWM_T0_MAT_CHN0`

```c
#define LPC84X_SWM_T0_MAT_CHN0 53U
```

定时器 0（T0）的匹配通道 0（MAT CHN0）。

<a id="acb7ff85727e9c21249aa583ae22ab230"></a>

### `LPC84X_SWM_T0_MAT_CHN1`

```c
#define LPC84X_SWM_T0_MAT_CHN1 54U
```

定时器 0（T0）的匹配通道 1（MAT CHN1）。

<a id="a53c5a056e5a7bb070984db672ac98aa6"></a>

### `LPC84X_SWM_T0_MAT_CHN2`

```c
#define LPC84X_SWM_T0_MAT_CHN2 55U
```

定时器 0（T0）的匹配通道 2（MAT CHN2）。

<a id="a7a6d47a782ed3218158e4f143f62e330"></a>

### `LPC84X_SWM_T0_MAT_CHN3`

```c
#define LPC84X_SWM_T0_MAT_CHN3 56U
```

定时器 0（T0）的匹配通道 3（MAT CHN3）。

<a id="ac03e223d75d42c754079bf6c23efebdc"></a>

### `LPC84X_SWM_USART0_CTS`

```c
#define LPC84X_SWM_USART0_CTS 3U
```

USART0 的清除发送信号（CTS）。

<a id="a4c6ee732ce8bebdc7783277954fbfa1e"></a>

### `LPC84X_SWM_USART0_RTS`

```c
#define LPC84X_SWM_USART0_RTS 2U
```

USART0 的请求发送信号（RTS）。

<a id="a6a1f0f6e22ecf53ec38adee7339d732f"></a>

### `LPC84X_SWM_USART0_RXD`

```c
#define LPC84X_SWM_USART0_RXD 1U
```

USART0 的接收数据信号（RXD）。

<a id="aa3b6565df20cdceab2454eecc76cf5d6"></a>

### `LPC84X_SWM_USART0_SCLK`

```c
#define LPC84X_SWM_USART0_SCLK 4U
```

USART0 的串行时钟信号（SCLK）。

<a id="a508b8cd868aa00345e56cda9448dcc1b"></a>

### `LPC84X_SWM_USART0_TXD`

```c
#define LPC84X_SWM_USART0_TXD 0U
```

开关矩阵（SWM）可移动功能索引（Movable Function Indices）。

USART0 的发送数据信号（TXD）。

<a id="a7abe086056ab632c7d6035cc158a9d03"></a>

### `LPC84X_SWM_USART1_CTS`

```c
#define LPC84X_SWM_USART1_CTS 8U
```

USART1 的清除发送信号（CTS）。

<a id="a1c1485775ee41d9cb97f128702cfa0d0"></a>

### `LPC84X_SWM_USART1_RTS`

```c
#define LPC84X_SWM_USART1_RTS 7U
```

USART1 的请求发送信号（RTS）。

<a id="a28bd505d91afc679432412aa88087d3a"></a>

### `LPC84X_SWM_USART1_RXD`

```c
#define LPC84X_SWM_USART1_RXD 6U
```

USART1 的接收数据信号（RXD）。

<a id="a4ad65a41da1576f1981e9e842fbb91ec"></a>

### `LPC84X_SWM_USART1_SCLK`

```c
#define LPC84X_SWM_USART1_SCLK 9U
```

USART1 的串行时钟信号（SCLK）。

<a id="a468f03e189e270f1468dbfd462c5d66f"></a>

### `LPC84X_SWM_USART1_TXD`

```c
#define LPC84X_SWM_USART1_TXD 5U
```

USART1 的发送数据信号（TXD）。

<a id="adf1cf0986e84433ea45c759daaa1fa06"></a>

### `LPC84X_SWM_USART2_CTS`

```c
#define LPC84X_SWM_USART2_CTS 13U
```

USART2 的清除发送信号（CTS）。

<a id="ad4e1c3427722ef9ab2a804cbdb631fc2"></a>

### `LPC84X_SWM_USART2_RTS`

```c
#define LPC84X_SWM_USART2_RTS 12U
```

USART2 的请求发送信号（RTS）。

<a id="ab8ce4361b5345aa7f7105a3b632e4d08"></a>

### `LPC84X_SWM_USART2_RXD`

```c
#define LPC84X_SWM_USART2_RXD 11U
```

USART2 的接收数据信号（RXD）。

<a id="a6076959a65f0755b00d232b83e3dabe9"></a>

### `LPC84X_SWM_USART2_SCLK`

```c
#define LPC84X_SWM_USART2_SCLK 14U
```

USART2 的串行时钟信号（SCLK）。

<a id="a521f5d5f7762f936161b939673a3676c"></a>

### `LPC84X_SWM_USART2_TXD`

```c
#define LPC84X_SWM_USART2_TXD 10U
```

USART2 的发送数据信号（TXD）。

<a id="a909ea5af237942b81bda335c4c7600aa"></a>

### `LPC84X_SWM_USART3_RXD`

```c
#define LPC84X_SWM_USART3_RXD 48U
```

USART3 的接收数据信号（RXD）。

<a id="ad94acec3a054b3a0281c43d079646fc6"></a>

### `LPC84X_SWM_USART3_SCLK`

```c
#define LPC84X_SWM_USART3_SCLK 49U
```

USART3 的串行时钟信号（SCLK）。

<a id="ac51f611b848f8a7203023f2655f3bc52"></a>

### `LPC84X_SWM_USART3_TXD`

```c
#define LPC84X_SWM_USART3_TXD 47U
```

USART3 的发送数据信号（TXD）。

<a id="a194aad29c2be2a49a5b2a75e288b3a29"></a>

### `LPC84X_SWM_USART4_RXD`

```c
#define LPC84X_SWM_USART4_RXD 51U
```

USART4 的接收数据信号（RXD）。

<a id="a04b6e0be7923662fcfed6aca3d465db1"></a>

### `LPC84X_SWM_USART4_SCLK`

```c
#define LPC84X_SWM_USART4_SCLK 52U
```

USART4 的串行时钟信号（SCLK）。

<a id="a8dcdadf178907a318c60a6c4bdf3de88"></a>

### `LPC84X_SWM_USART4_TXD`

```c
#define LPC84X_SWM_USART4_TXD 50U
```

USART4 的发送数据信号（TXD）。

<a id="aa09d0c97ae4cd35c0d7039061cd98028"></a>

### `LPC84X_SWM_VDDCMP`

```c
#define LPC84X_SWM_VDDCMP 11U
```

VDD 比较器信号（VDDCMP）。

<a id="a63552edb1b6563c5e6bbbc6edf14cd7e"></a>

### `LPC84X_SWM_XTALIN`

```c
#define LPC84X_SWM_XTALIN 7U
```

晶体输入（XTALIN）。

<a id="a7efda9e24b5c3abb92d477fc473a1de6"></a>

### `LPC84X_SWM_XTALOUT`

```c
#define LPC84X_SWM_XTALOUT 8U
```

晶体输出（XTALOUT）。

<a id="a188735bd8812ee242324075c9cae4e0e"></a>

### `P0_0`

```c
#define P0_0 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_0, IOCON_INDEX_PIO0_0)
```

编码后的引脚定义（Encoded Pin Definitions），组合了物理端口引脚标识符与对应 IOCON 索引。

供设备树引脚控制节点（Devicetree Pinctrl Nodes）使用。此项为 `P0_0`。

<a id="a6e605c856305ec72ac000d8cc45ab0b9"></a>

### `P0_1`

```c
#define P0_1 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_1, IOCON_INDEX_PIO0_1)
```

端口 0、引脚 1 的编码定义（P0_1）。

<a id="a6e0975575d630a24aab56aa9b4e1772d"></a>

### `P0_10`

```c
#define P0_10 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_10, IOCON_INDEX_PIO0_10)
```

端口 0、引脚 10 的编码定义（P0_10）。

<a id="a96018d9c4e5b359ef920a5af36cfb7aa"></a>

### `P0_11`

```c
#define P0_11 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_11, IOCON_INDEX_PIO0_11)
```

端口 0、引脚 11 的编码定义（P0_11）。

<a id="a240b3b6e91a2eaf160635c27888c1e19"></a>

### `P0_12`

```c
#define P0_12 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_12, IOCON_INDEX_PIO0_12)
```

端口 0、引脚 12 的编码定义（P0_12）。

<a id="ae46d0fe9ff37262c0ce77c1dced2566b"></a>

### `P0_13`

```c
#define P0_13 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_13, IOCON_INDEX_PIO0_13)
```

端口 0、引脚 13 的编码定义（P0_13）。

<a id="abd51c64b559f19da0c8fb9f755194ca2"></a>

### `P0_14`

```c
#define P0_14 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_14, IOCON_INDEX_PIO0_14)
```

端口 0、引脚 14 的编码定义（P0_14）。

<a id="a41c82eba7d677c4dd0b8af602a76284f"></a>

### `P0_15`

```c
#define P0_15 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_15, IOCON_INDEX_PIO0_15)
```

端口 0、引脚 15 的编码定义（P0_15）。

<a id="a7f81f059c79120054cebb5fbcd383034"></a>

### `P0_16`

```c
#define P0_16 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_16, IOCON_INDEX_PIO0_16)
```

端口 0、引脚 16 的编码定义（P0_16）。

<a id="a2897768ad1f6566030af4a704ec02012"></a>

### `P0_17`

```c
#define P0_17 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_17, IOCON_INDEX_PIO0_17)
```

端口 0、引脚 17 的编码定义（P0_17）。

<a id="a757921d7eed356cb0964aadbb028211f"></a>

### `P0_18`

```c
#define P0_18 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_18, IOCON_INDEX_PIO0_18)
```

端口 0、引脚 18 的编码定义（P0_18）。

<a id="a2187a967a9777b4fbf2b0635716d09d7"></a>

### `P0_19`

```c
#define P0_19 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_19, IOCON_INDEX_PIO0_19)
```

端口 0、引脚 19 的编码定义（P0_19）。

<a id="a876e3d0917cea9d0a75b2f6df2c3f1d4"></a>

### `P0_2`

```c
#define P0_2 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_2, IOCON_INDEX_PIO0_2)
```

端口 0、引脚 2 的编码定义（P0_2）。

<a id="a16283fe59fbca32579fef70b891d0262"></a>

### `P0_20`

```c
#define P0_20 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_20, IOCON_INDEX_PIO0_20)
```

端口 0、引脚 20 的编码定义（P0_20）。

<a id="ace0737416a27f4f8413b4c74a19f69f1"></a>

### `P0_21`

```c
#define P0_21 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_21, IOCON_INDEX_PIO0_21)
```

端口 0、引脚 21 的编码定义（P0_21）。

<a id="a1e834f8c45c4a1ffd4abeb174ff79732"></a>

### `P0_22`

```c
#define P0_22 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_22, IOCON_INDEX_PIO0_22)
```

端口 0、引脚 22 的编码定义（P0_22）。

<a id="adc11371e625a7dc71e732a973ecfde3e"></a>

### `P0_23`

```c
#define P0_23 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_23, IOCON_INDEX_PIO0_23)
```

端口 0、引脚 23 的编码定义（P0_23）。

<a id="abaf804f6456d35f8322e8137d2ad725b"></a>

### `P0_24`

```c
#define P0_24 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_24, IOCON_INDEX_PIO0_24)
```

端口 0、引脚 24 的编码定义（P0_24）。

<a id="a3285a6bb0cc206b249470bfc54ebd3e8"></a>

### `P0_25`

```c
#define P0_25 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_25, IOCON_INDEX_PIO0_25)
```

端口 0、引脚 25 的编码定义（P0_25）。

<a id="ae9ff8d68608904f1fd48b0cdcc6a1943"></a>

### `P0_26`

```c
#define P0_26 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_26, IOCON_INDEX_PIO0_26)
```

端口 0、引脚 26 的编码定义（P0_26）。

<a id="ab382318857300a74bfe96533334c5622"></a>

### `P0_27`

```c
#define P0_27 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_27, IOCON_INDEX_PIO0_27)
```

端口 0、引脚 27 的编码定义（P0_27）。

<a id="ac7b207aae62b35a54bc701b1a1d129f6"></a>

### `P0_28`

```c
#define P0_28 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_28, IOCON_INDEX_PIO0_28)
```

端口 0、引脚 28 的编码定义（P0_28）。

<a id="adb961beba9ded7ce72e3d8edbb0cc5fe"></a>

### `P0_29`

```c
#define P0_29 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_29, IOCON_INDEX_PIO0_29)
```

端口 0、引脚 29 的编码定义（P0_29）。

<a id="ab73f15237a6f8860438ba0359b283686"></a>

### `P0_3`

```c
#define P0_3 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_3, IOCON_INDEX_PIO0_3)
```

端口 0、引脚 3 的编码定义（P0_3）。

<a id="a1fa3927c6765a474ff77d13c87aa8ccf"></a>

### `P0_30`

```c
#define P0_30 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_30, IOCON_INDEX_PIO0_30)
```

端口 0、引脚 30 的编码定义（P0_30）。

<a id="a420dc619975be8d13b83c6ab7c364c41"></a>

### `P0_31`

```c
#define P0_31 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_31, IOCON_INDEX_PIO0_31)
```

端口 0、引脚 31 的编码定义（P0_31）。

<a id="a3218b7341a4f084375bade756f108940"></a>

### `P0_4`

```c
#define P0_4 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_4, IOCON_INDEX_PIO0_4)
```

端口 0、引脚 4 的编码定义（P0_4）。

<a id="aa1681f3dab52db87cd32f77b20352770"></a>

### `P0_5`

```c
#define P0_5 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_5, IOCON_INDEX_PIO0_5)
```

端口 0、引脚 5 的编码定义（P0_5）。

<a id="a990dc4ba08ec342d0bfa50f99d9e1868"></a>

### `P0_6`

```c
#define P0_6 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_6, IOCON_INDEX_PIO0_6)
```

端口 0、引脚 6 的编码定义（P0_6）。

<a id="a34087bca5283adcf7cc7c810f30eab80"></a>

### `P0_7`

```c
#define P0_7 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_7, IOCON_INDEX_PIO0_7)
```

端口 0、引脚 7 的编码定义（P0_7）。

<a id="a5cfe193b59c3ee005dabe75f1a5b7162"></a>

### `P0_8`

```c
#define P0_8 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_8, IOCON_INDEX_PIO0_8)
```

端口 0、引脚 8 的编码定义（P0_8）。

<a id="aae8e5c3d453e5a1acc12299784627b35"></a>

### `P0_9`

```c
#define P0_9 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_9, IOCON_INDEX_PIO0_9)
```

端口 0、引脚 9 的编码定义（P0_9）。

<a id="a0a5c0ef038f9728173ca136eed5c9cd2"></a>

### `P1_0`

```c
#define P1_0 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_0, IOCON_INDEX_PIO1_0)
```

端口 1、引脚 0 的编码定义（P1_0）。

<a id="aa7c3cebcd9dc4598bb69e51ecee85bd0"></a>

### `P1_1`

```c
#define P1_1 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_1, IOCON_INDEX_PIO1_1)
```

端口 1、引脚 1 的编码定义（P1_1）。

<a id="a4319c5e3ed329de7acf55d50c10121f0"></a>

### `P1_10`

```c
#define P1_10 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_10, IOCON_INDEX_PIO1_10)
```

端口 1、引脚 10 的编码定义（P1_10）。

<a id="a4a6d764dfc72b9a8c9c808d3065a1843"></a>

### `P1_11`

```c
#define P1_11 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_11, IOCON_INDEX_PIO1_11)
```

端口 1、引脚 11 的编码定义（P1_11）。

<a id="a7e7591732365fa663a17fb738e2945a2"></a>

### `P1_12`

```c
#define P1_12 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_12, IOCON_INDEX_PIO1_12)
```

端口 1、引脚 12 的编码定义（P1_12）。

<a id="a570652df2d7482326f11660c22e2dc28"></a>

### `P1_13`

```c
#define P1_13 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_13, IOCON_INDEX_PIO1_13)
```

端口 1、引脚 13 的编码定义（P1_13）。

<a id="af273b3bb179cfc9082e8a70848592883"></a>

### `P1_14`

```c
#define P1_14 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_14, IOCON_INDEX_PIO1_14)
```

端口 1、引脚 14 的编码定义（P1_14）。

<a id="ae5aa504f54ca4e7aead6e0af6f4e2a2b"></a>

### `P1_15`

```c
#define P1_15 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_15, IOCON_INDEX_PIO1_15)
```

端口 1、引脚 15 的编码定义（P1_15）。

<a id="a68ec273c755729a01891115ab5371192"></a>

### `P1_16`

```c
#define P1_16 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_16, IOCON_INDEX_PIO1_16)
```

端口 1、引脚 16 的编码定义（P1_16）。

<a id="a6058a5071b9b013c16fd14a332c7362a"></a>

### `P1_17`

```c
#define P1_17 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_17, IOCON_INDEX_PIO1_17)
```

端口 1、引脚 17 的编码定义（P1_17）。

<a id="a4dc67e818b0aca5796d09f38167c80d4"></a>

### `P1_18`

```c
#define P1_18 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_18, IOCON_INDEX_PIO1_18)
```

端口 1、引脚 18 的编码定义（P1_18）。

<a id="af0657880bb6b8f7c1fe4bfeb1a882636"></a>

### `P1_19`

```c
#define P1_19 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_19, IOCON_INDEX_PIO1_19)
```

端口 1、引脚 19 的编码定义（P1_19）。

<a id="a071e0091581eba3bdf70559d215cda5d"></a>

### `P1_2`

```c
#define P1_2 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_2, IOCON_INDEX_PIO1_2)
```

端口 1、引脚 2 的编码定义（P1_2）。

<a id="a7559fc173a9ea1f713f1a0f47c273e84"></a>

### `P1_20`

```c
#define P1_20 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_20, IOCON_INDEX_PIO1_20)
```

端口 1、引脚 20 的编码定义（P1_20）。

<a id="a10f3670e885fcc7435cc8321a0b1bc77"></a>

### `P1_21`

```c
#define P1_21 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_21, IOCON_INDEX_PIO1_21)
```

端口 1、引脚 21 的编码定义（P1_21）。

<a id="ad2a4d881a3a72ead238fcf2a4aea88bf"></a>

### `P1_3`

```c
#define P1_3 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_3, IOCON_INDEX_PIO1_3)
```

端口 1、引脚 3 的编码定义（P1_3）。

<a id="ab65ddc9251137261c8c17b03a415e831"></a>

### `P1_4`

```c
#define P1_4 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_4, IOCON_INDEX_PIO1_4)
```

端口 1、引脚 4 的编码定义（P1_4）。

<a id="af610a6265a7bc9f5c44efa18219c5e96"></a>

### `P1_5`

```c
#define P1_5 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_5, IOCON_INDEX_PIO1_5)
```

端口 1、引脚 5 的编码定义（P1_5）。

<a id="a9e219f75c65aa5b19d59bd1596b3e548"></a>

### `P1_6`

```c
#define P1_6 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_6, IOCON_INDEX_PIO1_6)
```

端口 1、引脚 6 的编码定义（P1_6）。

<a id="a59e6507c1874213b84ae809c24c3a76e"></a>

### `P1_7`

```c
#define P1_7 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_7, IOCON_INDEX_PIO1_7)
```

端口 1、引脚 7 的编码定义（P1_7）。

<a id="acb31070df6aa10c8d25fba9a5c2a5c0d"></a>

### `P1_8`

```c
#define P1_8 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_8, IOCON_INDEX_PIO1_8)
```

端口 1、引脚 8 的编码定义（P1_8）。

<a id="a3e359fe9dc553fe39543a35bc59fdb1d"></a>

### `P1_9`

```c
#define P1_9 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_9, IOCON_INDEX_PIO1_9)
```

端口 1、引脚 9 的编码定义（P1_9）。


## 4.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_device_reference/P024_lpc84x-pinctrl.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P003_zephyr__dt-bindings__input__input-event-codes.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__bluetooth__classic__sdp.h_文件参考.md)
