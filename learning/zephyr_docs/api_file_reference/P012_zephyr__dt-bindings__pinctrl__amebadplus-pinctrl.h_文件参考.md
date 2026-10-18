---
id: learning.zephyr-docs.api-file-reference.page-12
title: zephyr__dt-bindings__pinctrl__amebadplus-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/amebadplus-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_amebadplus-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/amebadplus-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 12.1\_宏定义（Macros）

<a id="r_a1a770820da1c7f81c4925cd6a6fab8f4"></a>

```c
#define AMEBA_GPIO 0
```

相关声明：[AMEBA_GPIO](#a1a770820da1c7f81c4925cd6a6fab8f4)。

<a id="r_a43b82c67e7ed46c4d7504354b89766a2"></a>

```c
#define AMEBA_LOG_UART 1
```

相关声明：[AMEBA_LOG_UART](#a43b82c67e7ed46c4d7504354b89766a2)。

<a id="r_a741c7c7e636536003ed508abd2d47d97"></a>

```c
#define AMEBA_UART 1
```

相关声明：[AMEBA_UART](#a741c7c7e636536003ed508abd2d47d97)。

<a id="r_add660cc0a513fed62fe5d5e2ec12e5a7"></a>

```c
#define AMEBA_SPIC0_FLASH 2
```

相关声明：[AMEBA_SPIC0_FLASH](#add660cc0a513fed62fe5d5e2ec12e5a7)。

<a id="r_a5eb4f7828f8f9aab06d02ba35f4daf6f"></a>

```c
#define AMEBA_SPIC1_FLASH 3
```

相关声明：[AMEBA_SPIC1_FLASH](#a5eb4f7828f8f9aab06d02ba35f4daf6f)。

<a id="r_a97aa1778f7670f03bc30a9cc156c3da1"></a>

```c
#define AMEBA_SPIC1_PSRAM 4
```

相关声明：[AMEBA_SPIC1_PSRAM](#a97aa1778f7670f03bc30a9cc156c3da1)。

<a id="r_ad8ded7699c9503bf9e0f89ef27460de0"></a>

```c
#define AMEBA_OSPI 5
```

相关声明：[AMEBA_OSPI](#ad8ded7699c9503bf9e0f89ef27460de0)。

<a id="r_a47e10b04eb5bfc28b3f0ceb9b75afffd"></a>

```c
#define AMEBA_QSPI 5
```

相关声明：[AMEBA_QSPI](#a47e10b04eb5bfc28b3f0ceb9b75afffd)。

<a id="r_acb023403125750639b0d02171607c2ad"></a>

```c
#define AMEBA_ADC 6
```

相关声明：[AMEBA_ADC](#acb023403125750639b0d02171607c2ad)。

<a id="r_a1eeebd2f73559939b681db6e912def28"></a>

```c
#define AMEBA_CAP_TOUCH 6
```

相关声明：[AMEBA_CAP_TOUCH](#a1eeebd2f73559939b681db6e912def28)。

<a id="r_aafdc733867a4ab1a0d16429679b19cba"></a>

```c
#define AMEBA_SIC 7
```

相关声明：[AMEBA_SIC](#aafdc733867a4ab1a0d16429679b19cba)。

<a id="r_abda4dcf809ca676e918866ddd7ddd097"></a>

```c
#define AMEBA_SPI 8
```

相关声明：[AMEBA_SPI](#abda4dcf809ca676e918866ddd7ddd097)。

<a id="r_a0d8fdf8ef3539a8cfe2b6e57f8e5db8d"></a>

```c
#define AMEBA_SWD 9
```

相关声明：[AMEBA_SWD](#a0d8fdf8ef3539a8cfe2b6e57f8e5db8d)。

<a id="r_aafa0395014ea6191b12b50b89ed01bc8"></a>

```c
#define AMEBA_SDIO 10
```

相关声明：[AMEBA_SDIO](#aafa0395014ea6191b12b50b89ed01bc8)。

<a id="r_a072577fb2011f0f6a0dc4048330b7c5a"></a>

```c
#define AMEBA_ANT_DIV 11
```

相关声明：[AMEBA_ANT_DIV](#a072577fb2011f0f6a0dc4048330b7c5a)。

<a id="r_aba46fb715417b3528ed7ce89eed810c6"></a>

```c
#define AMEBA_EXT_BT 12
```

相关声明：[AMEBA_EXT_BT](#aba46fb715417b3528ed7ce89eed810c6)。

<a id="r_a6808b0d69603d73741df35aa2ccf9166"></a>

```c
#define AMEBA_BT_IO 13
```

相关声明：[AMEBA_BT_IO](#a6808b0d69603d73741df35aa2ccf9166)。

<a id="r_a71f0921f7c7ccd5e272cb66733dfa994"></a>

```c
#define AMEBA_BT 14
```

相关声明：[AMEBA_BT](#a71f0921f7c7ccd5e272cb66733dfa994)。

<a id="r_a1d895d64cb1e0661dd94732ca50e7724"></a>

```c
#define AMEBA_EXT_ZIGBEE 15
```

相关声明：[AMEBA_EXT_ZIGBEE](#a1d895d64cb1e0661dd94732ca50e7724)。

<a id="r_a01e0fb61666dcce90f9e23573f180f00"></a>

```c
#define AMEBA_TIMER 16
```

相关声明：[AMEBA_TIMER](#a01e0fb61666dcce90f9e23573f180f00)。

<a id="r_adfeeeb74cd0157b09992ec5e5f4e5397"></a>

```c
#define AMEBA_USB 17
```

相关声明：[AMEBA_USB](#adfeeeb74cd0157b09992ec5e5f4e5397)。

<a id="r_a98d7af9e28bf21c740207cffde3550db"></a>

```c
#define AMEBA_DEBUG 18
```

相关声明：[AMEBA_DEBUG](#a98d7af9e28bf21c740207cffde3550db)。

<a id="r_a74d6af9b061345287512018abbe6cdc0"></a>

```c
#define AMEBA_UART0_TXD 19
```

相关声明：[AMEBA_UART0_TXD](#a74d6af9b061345287512018abbe6cdc0)。

<a id="r_aa93af39fe6c222c908a7642f5a4349a8"></a>

```c
#define AMEBA_UART0_RXD 20
```

相关声明：[AMEBA_UART0_RXD](#aa93af39fe6c222c908a7642f5a4349a8)。

<a id="r_aec676f180cd6c8ebde85b78984953106"></a>

```c
#define AMEBA_UART0_CTS 21
```

相关声明：[AMEBA_UART0_CTS](#aec676f180cd6c8ebde85b78984953106)。

<a id="r_aa6ee6a2d6312b5a92db53caf4424490e"></a>

```c
#define AMEBA_UART0_RTS 22
```

相关声明：[AMEBA_UART0_RTS](#aa6ee6a2d6312b5a92db53caf4424490e)。

<a id="r_a5264a7b7b4e1dc4e66abf649d6fbf398"></a>

```c
#define AMEBA_UART1_TXD 23
```

相关声明：[AMEBA_UART1_TXD](#a5264a7b7b4e1dc4e66abf649d6fbf398)。

<a id="r_a76f722879ffac4f94f543ebfc514fb7f"></a>

```c
#define AMEBA_UART1_RXD 24
```

相关声明：[AMEBA_UART1_RXD](#a76f722879ffac4f94f543ebfc514fb7f)。

<a id="r_a8eb069f61c95598413fb9cda6304b287"></a>

```c
#define AMEBA_UART2_TXD 25
```

相关声明：[AMEBA_UART2_TXD](#a8eb069f61c95598413fb9cda6304b287)。

<a id="r_a8b9308171579c28194d890a90cdf68be"></a>

```c
#define AMEBA_UART2_RXD 26
```

相关声明：[AMEBA_UART2_RXD](#a8b9308171579c28194d890a90cdf68be)。

<a id="r_a8a504db1a6c395a5fc694dd092f4ab1c"></a>

```c
#define AMEBA_UART2_CTS 27
```

相关声明：[AMEBA_UART2_CTS](#a8a504db1a6c395a5fc694dd092f4ab1c)。

<a id="r_a224062161ec641f0cf26551562e3cd3e"></a>

```c
#define AMEBA_UART2_RTS 28
```

相关声明：[AMEBA_UART2_RTS](#a224062161ec641f0cf26551562e3cd3e)。

<a id="r_a1997336af677a35e15d1402aed065ee6"></a>

```c
#define AMEBA_SPI1_CLK 29
```

相关声明：[AMEBA_SPI1_CLK](#a1997336af677a35e15d1402aed065ee6)。

<a id="r_ab40628d9a44f82362da70ab685c41cee"></a>

```c
#define AMEBA_SPI1_MISO 30
```

相关声明：[AMEBA_SPI1_MISO](#ab40628d9a44f82362da70ab685c41cee)。

<a id="r_ab9a8e9f5f8c3160a04998960c61e8b4d"></a>

```c
#define AMEBA_SPI1_MOSI 31
```

相关声明：[AMEBA_SPI1_MOSI](#ab9a8e9f5f8c3160a04998960c61e8b4d)。

<a id="r_a9113912d0b976fd5539fbd003e83d85f"></a>

```c
#define AMEBA_SPI1_CS 32
```

相关声明：[AMEBA_SPI1_CS](#a9113912d0b976fd5539fbd003e83d85f)。

<a id="r_aa117a91002cec5d0421c0b9958f90d5e"></a>

```c
#define AMEBA_LEDC 33
```

相关声明：[AMEBA_LEDC](#aa117a91002cec5d0421c0b9958f90d5e)。

<a id="r_a712d64cdb749070056bd158553370eae"></a>

```c
#define AMEBA_I2S0_MCLK 34
```

相关声明：[AMEBA_I2S0_MCLK](#a712d64cdb749070056bd158553370eae)。

<a id="r_a24a9be29f490ac4b2425b8f0c96fd0f9"></a>

```c
#define AMEBA_I2S0_BCLK 35
```

相关声明：[AMEBA_I2S0_BCLK](#a24a9be29f490ac4b2425b8f0c96fd0f9)。

<a id="r_a51d16562267051569c14c05358115cb4"></a>

```c
#define AMEBA_I2S0_WS 36
```

相关声明：[AMEBA_I2S0_WS](#a51d16562267051569c14c05358115cb4)。

<a id="r_ac224c5d98fcda932f1dd56e119ea8c8f"></a>

```c
#define AMEBA_I2S0_DIO0 37
```

相关声明：[AMEBA_I2S0_DIO0](#ac224c5d98fcda932f1dd56e119ea8c8f)。

<a id="r_a6d15583c82ed66abfd8879cd1b83bc85"></a>

```c
#define AMEBA_I2S0_DIO1 38
```

相关声明：[AMEBA_I2S0_DIO1](#a6d15583c82ed66abfd8879cd1b83bc85)。

<a id="r_a167ee959e13888da0a0a6aff7620f756"></a>

```c
#define AMEBA_I2S0_DIO2 39
```

相关声明：[AMEBA_I2S0_DIO2](#a167ee959e13888da0a0a6aff7620f756)。

<a id="r_a430fc7f6f6e9703f7fb425b173d5fd6c"></a>

```c
#define AMEBA_I2S0_DIO3 40
```

相关声明：[AMEBA_I2S0_DIO3](#a430fc7f6f6e9703f7fb425b173d5fd6c)。

<a id="r_a86d74374cae2183f23a846c59d62f4c1"></a>

```c
#define AMEBA_I2S1_MCLK 41
```

相关声明：[AMEBA_I2S1_MCLK](#a86d74374cae2183f23a846c59d62f4c1)。

<a id="r_a69c9fa8a5e8e28d98c15db2b23313ed0"></a>

```c
#define AMEBA_I2S1_BCLK 42
```

相关声明：[AMEBA_I2S1_BCLK](#a69c9fa8a5e8e28d98c15db2b23313ed0)。

<a id="r_a19d475b5bd11ad9be6ebd2069e57e101"></a>

```c
#define AMEBA_I2S1_WS 43
```

相关声明：[AMEBA_I2S1_WS](#a19d475b5bd11ad9be6ebd2069e57e101)。

<a id="r_af16f318833191b80fd8fcca7588eb1ba"></a>

```c
#define AMEBA_I2S1_DIO0 44
```

相关声明：[AMEBA_I2S1_DIO0](#af16f318833191b80fd8fcca7588eb1ba)。

<a id="r_a85abd63379f4aeb698756d9d6986eaf2"></a>

```c
#define AMEBA_I2S1_DIO1 45
```

相关声明：[AMEBA_I2S1_DIO1](#a85abd63379f4aeb698756d9d6986eaf2)。

<a id="r_a3cf886fb16acdddf003f8afb9eec1927"></a>

```c
#define AMEBA_I2S1_DIO2 46
```

相关声明：[AMEBA_I2S1_DIO2](#a3cf886fb16acdddf003f8afb9eec1927)。

<a id="r_a0b1d1fff7294382dafca7a49f850cdff"></a>

```c
#define AMEBA_I2S1_DIO3 47
```

相关声明：[AMEBA_I2S1_DIO3](#a0b1d1fff7294382dafca7a49f850cdff)。

<a id="r_a45b715ce9be8df9c8693cb4349b7f0da"></a>

```c
#define AMEBA_I2C0_SCL 48
```

相关声明：[AMEBA_I2C0_SCL](#a45b715ce9be8df9c8693cb4349b7f0da)。

<a id="r_a1adbe2f3d191e115cd29c73b8d726272"></a>

```c
#define AMEBA_I2C0_SDA 49
```

相关声明：[AMEBA_I2C0_SDA](#a1adbe2f3d191e115cd29c73b8d726272)。

<a id="r_a6cd3bf525d23b4224b1238d3b0c5fcde"></a>

```c
#define AMEBA_I2C1_SCL 50
```

相关声明：[AMEBA_I2C1_SCL](#a6cd3bf525d23b4224b1238d3b0c5fcde)。

<a id="r_a88e9123211493809fdd23078928905de"></a>

```c
#define AMEBA_I2C1_SDA 51
```

相关声明：[AMEBA_I2C1_SDA](#a88e9123211493809fdd23078928905de)。

<a id="r_a5c38d8038284dab2ffdc4b8e6f7750b3"></a>

```c
#define AMEBA_PWM0 52
```

相关声明：[AMEBA_PWM0](#a5c38d8038284dab2ffdc4b8e6f7750b3)。

<a id="r_a86aaa57f39ca21f312d0d0ca338ddec8"></a>

```c
#define AMEBA_PWM1 53
```

相关声明：[AMEBA_PWM1](#a86aaa57f39ca21f312d0d0ca338ddec8)。

<a id="r_ae79456baaa4aec51c69f000937401eac"></a>

```c
#define AMEBA_PWM2 54
```

相关声明：[AMEBA_PWM2](#ae79456baaa4aec51c69f000937401eac)。

<a id="r_ac2c77f1b466e0b3d9c8b7b1c5086c9ee"></a>

```c
#define AMEBA_PWM3 55
```

相关声明：[AMEBA_PWM3](#ac2c77f1b466e0b3d9c8b7b1c5086c9ee)。

<a id="r_a244a6609f273fa3bc80f889ccb6592ba"></a>

```c
#define AMEBA_PWM4 56
```

相关声明：[AMEBA_PWM4](#a244a6609f273fa3bc80f889ccb6592ba)。

<a id="r_a71d62bc7ff0d9606132b453da0bd43b8"></a>

```c
#define AMEBA_PWM5 57
```

相关声明：[AMEBA_PWM5](#a71d62bc7ff0d9606132b453da0bd43b8)。

<a id="r_ad2e2672cf5229610ccac83fb9602046a"></a>

```c
#define AMEBA_PWM6 58
```

相关声明：[AMEBA_PWM6](#ad2e2672cf5229610ccac83fb9602046a)。

<a id="r_a522f21781b09e9f2f60500dad5912dce"></a>

```c
#define AMEBA_PWM7 59
```

相关声明：[AMEBA_PWM7](#a522f21781b09e9f2f60500dad5912dce)。

<a id="r_aaba22ba54603e2ba9da38f0e2e97f724"></a>

```c
#define AMEBA_BT_UART_TXD 60
```

相关声明：[AMEBA_BT_UART_TXD](#aaba22ba54603e2ba9da38f0e2e97f724)。

<a id="r_acf5dcb7179aeaca2f4a2ad4b685d3fef"></a>

```c
#define AMEBA_BT_UART_RTS 61
```

相关声明：[AMEBA_BT_UART_RTS](#acf5dcb7179aeaca2f4a2ad4b685d3fef)。

<a id="r_a5544c01a480ae8ab721f846aedeac3a2"></a>

```c
#define AMEBA_DMIC_CLK 62
```

相关声明：[AMEBA_DMIC_CLK](#a5544c01a480ae8ab721f846aedeac3a2)。

<a id="r_ac8a69ac2c1bfea15838a8a5da7ea3d1b"></a>

```c
#define AMEBA_DMIC_DATA 63
```

相关声明：[AMEBA_DMIC_DATA](#ac8a69ac2c1bfea15838a8a5da7ea3d1b)。

<a id="r_a654f82f22bb941b39469479e968bc8b0"></a>

```c
#define AMEBA_IR_TX 64
```

相关声明：[AMEBA_IR_TX](#a654f82f22bb941b39469479e968bc8b0)。

<a id="r_a3136f2fc775bb63f80203ca8859627b2"></a>

```c
#define AMEBA_IR_RX 65
```

相关声明：[AMEBA_IR_RX](#a3136f2fc775bb63f80203ca8859627b2)。

<a id="r_a85a9f78d1ffd075bc5266baf4ed774f0"></a>

```c
#define AMEBA_KEY_ROW0 66
```

相关声明：[AMEBA_KEY_ROW0](#a85a9f78d1ffd075bc5266baf4ed774f0)。

<a id="r_a005046634079b69a462c87d23ca93f4e"></a>

```c
#define AMEBA_KEY_ROW1 67
```

相关声明：[AMEBA_KEY_ROW1](#a005046634079b69a462c87d23ca93f4e)。

<a id="r_a2d56cc79fad59e8514ef9a0b478ec687"></a>

```c
#define AMEBA_KEY_ROW2 68
```

相关声明：[AMEBA_KEY_ROW2](#a2d56cc79fad59e8514ef9a0b478ec687)。

<a id="r_a158da1991effcddbf38de5fc76e475ec"></a>

```c
#define AMEBA_KEY_ROW3 69
```

相关声明：[AMEBA_KEY_ROW3](#a158da1991effcddbf38de5fc76e475ec)。

<a id="r_ae9df5b1c30ec6a7c538e26eb7ab69930"></a>

```c
#define AMEBA_KEY_ROW4 70
```

相关声明：[AMEBA_KEY_ROW4](#ae9df5b1c30ec6a7c538e26eb7ab69930)。

<a id="r_ac63dacaee881249d2d9b6c4ca8002c48"></a>

```c
#define AMEBA_KEY_ROW5 71
```

相关声明：[AMEBA_KEY_ROW5](#ac63dacaee881249d2d9b6c4ca8002c48)。

<a id="r_a34fab16293055315512bc9b41eec2166"></a>

```c
#define AMEBA_KEY_ROW6 72
```

相关声明：[AMEBA_KEY_ROW6](#a34fab16293055315512bc9b41eec2166)。

<a id="r_a6f86c3dfe508a5d7904ef018942dba28"></a>

```c
#define AMEBA_KEY_ROW7 73
```

相关声明：[AMEBA_KEY_ROW7](#a6f86c3dfe508a5d7904ef018942dba28)。

<a id="r_a264ddf441d53174b4d1704766c1949a9"></a>

```c
#define AMEBA_KEY_COL0 74
```

相关声明：[AMEBA_KEY_COL0](#a264ddf441d53174b4d1704766c1949a9)。

<a id="r_a73d6054f140bce50d34ff44bb67a9b84"></a>

```c
#define AMEBA_KEY_COL1 75
```

相关声明：[AMEBA_KEY_COL1](#a73d6054f140bce50d34ff44bb67a9b84)。

<a id="r_a92056df7355db7d9ef9dfe6e7fbf9a05"></a>

```c
#define AMEBA_KEY_COL2 76
```

相关声明：[AMEBA_KEY_COL2](#a92056df7355db7d9ef9dfe6e7fbf9a05)。

<a id="r_a29595b16e0b733884cf5e6fe17506829"></a>

```c
#define AMEBA_KEY_COL3 77
```

相关声明：[AMEBA_KEY_COL3](#a29595b16e0b733884cf5e6fe17506829)。

<a id="r_aa9a62b2e36f920095d41750a19e37376"></a>

```c
#define AMEBA_KEY_COL4 78
```

相关声明：[AMEBA_KEY_COL4](#aa9a62b2e36f920095d41750a19e37376)。

<a id="r_afb0ffaf9f21faf3f8a7c124b1eec5a16"></a>

```c
#define AMEBA_KEY_COL5 79
```

相关声明：[AMEBA_KEY_COL5](#afb0ffaf9f21faf3f8a7c124b1eec5a16)。

<a id="r_aa481e74a6f56e8602e196176c0d5d270"></a>

```c
#define AMEBA_KEY_COL6 80
```

相关声明：[AMEBA_KEY_COL6](#aa481e74a6f56e8602e196176c0d5d270)。

<a id="r_a3e2bf6dbf31fd769b7159f18361b1443"></a>

```c
#define AMEBA_KEY_COL7 81
```

相关声明：[AMEBA_KEY_COL7](#a3e2bf6dbf31fd769b7159f18361b1443)。

<a id="r_a01f0e522a7c41526681b766c7ac7ce1f"></a>

```c
#define AMEBA_PORT_PIN(port, line)
```

相关声明：[AMEBA_PORT_PIN](#a01f0e522a7c41526681b766c7ac7ce1f)。

<a id="r_a71d265adf87eb5aa7e991bf0dd6c142f"></a>

```c
#define AMEBA_PINMUX(port, line, funcid)
```

相关声明：[AMEBA_PINMUX](#a71d265adf87eb5aa7e991bf0dd6c142f)。

## 12.2\_详细说明（Detailed Documentation）

<a id="acb023403125750639b0d02171607c2ad"></a>

### `AMEBA_ADC`

```c
#define AMEBA_ADC 6
```

<a id="a072577fb2011f0f6a0dc4048330b7c5a"></a>

### `AMEBA_ANT_DIV`

```c
#define AMEBA_ANT_DIV 11
```

<a id="a71f0921f7c7ccd5e272cb66733dfa994"></a>

### `AMEBA_BT`

```c
#define AMEBA_BT 14
```

<a id="a6808b0d69603d73741df35aa2ccf9166"></a>

### `AMEBA_BT_IO`

```c
#define AMEBA_BT_IO 13
```

<a id="acf5dcb7179aeaca2f4a2ad4b685d3fef"></a>

### `AMEBA_BT_UART_RTS`

```c
#define AMEBA_BT_UART_RTS 61
```

<a id="aaba22ba54603e2ba9da38f0e2e97f724"></a>

### `AMEBA_BT_UART_TXD`

```c
#define AMEBA_BT_UART_TXD 60
```

<a id="a1eeebd2f73559939b681db6e912def28"></a>

### `AMEBA_CAP_TOUCH`

```c
#define AMEBA_CAP_TOUCH 6
```

<a id="a98d7af9e28bf21c740207cffde3550db"></a>

### `AMEBA_DEBUG`

```c
#define AMEBA_DEBUG 18
```

<a id="a5544c01a480ae8ab721f846aedeac3a2"></a>

### `AMEBA_DMIC_CLK`

```c
#define AMEBA_DMIC_CLK 62
```

<a id="ac8a69ac2c1bfea15838a8a5da7ea3d1b"></a>

### `AMEBA_DMIC_DATA`

```c
#define AMEBA_DMIC_DATA 63
```

<a id="aba46fb715417b3528ed7ce89eed810c6"></a>

### `AMEBA_EXT_BT`

```c
#define AMEBA_EXT_BT 12
```

<a id="a1d895d64cb1e0661dd94732ca50e7724"></a>

### `AMEBA_EXT_ZIGBEE`

```c
#define AMEBA_EXT_ZIGBEE 15
```

<a id="a1a770820da1c7f81c4925cd6a6fab8f4"></a>

### `AMEBA_GPIO`

```c
#define AMEBA_GPIO 0
```

<a id="a45b715ce9be8df9c8693cb4349b7f0da"></a>

### `AMEBA_I2C0_SCL`

```c
#define AMEBA_I2C0_SCL 48
```

<a id="a1adbe2f3d191e115cd29c73b8d726272"></a>

### `AMEBA_I2C0_SDA`

```c
#define AMEBA_I2C0_SDA 49
```

<a id="a6cd3bf525d23b4224b1238d3b0c5fcde"></a>

### `AMEBA_I2C1_SCL`

```c
#define AMEBA_I2C1_SCL 50
```

<a id="a88e9123211493809fdd23078928905de"></a>

### `AMEBA_I2C1_SDA`

```c
#define AMEBA_I2C1_SDA 51
```

<a id="a24a9be29f490ac4b2425b8f0c96fd0f9"></a>

### `AMEBA_I2S0_BCLK`

```c
#define AMEBA_I2S0_BCLK 35
```

<a id="ac224c5d98fcda932f1dd56e119ea8c8f"></a>

### `AMEBA_I2S0_DIO0`

```c
#define AMEBA_I2S0_DIO0 37
```

<a id="a6d15583c82ed66abfd8879cd1b83bc85"></a>

### `AMEBA_I2S0_DIO1`

```c
#define AMEBA_I2S0_DIO1 38
```

<a id="a167ee959e13888da0a0a6aff7620f756"></a>

### `AMEBA_I2S0_DIO2`

```c
#define AMEBA_I2S0_DIO2 39
```

<a id="a430fc7f6f6e9703f7fb425b173d5fd6c"></a>

### `AMEBA_I2S0_DIO3`

```c
#define AMEBA_I2S0_DIO3 40
```

<a id="a712d64cdb749070056bd158553370eae"></a>

### `AMEBA_I2S0_MCLK`

```c
#define AMEBA_I2S0_MCLK 34
```

<a id="a51d16562267051569c14c05358115cb4"></a>

### `AMEBA_I2S0_WS`

```c
#define AMEBA_I2S0_WS 36
```

<a id="a69c9fa8a5e8e28d98c15db2b23313ed0"></a>

### `AMEBA_I2S1_BCLK`

```c
#define AMEBA_I2S1_BCLK 42
```

<a id="af16f318833191b80fd8fcca7588eb1ba"></a>

### `AMEBA_I2S1_DIO0`

```c
#define AMEBA_I2S1_DIO0 44
```

<a id="a85abd63379f4aeb698756d9d6986eaf2"></a>

### `AMEBA_I2S1_DIO1`

```c
#define AMEBA_I2S1_DIO1 45
```

<a id="a3cf886fb16acdddf003f8afb9eec1927"></a>

### `AMEBA_I2S1_DIO2`

```c
#define AMEBA_I2S1_DIO2 46
```

<a id="a0b1d1fff7294382dafca7a49f850cdff"></a>

### `AMEBA_I2S1_DIO3`

```c
#define AMEBA_I2S1_DIO3 47
```

<a id="a86d74374cae2183f23a846c59d62f4c1"></a>

### `AMEBA_I2S1_MCLK`

```c
#define AMEBA_I2S1_MCLK 41
```

<a id="a19d475b5bd11ad9be6ebd2069e57e101"></a>

### `AMEBA_I2S1_WS`

```c
#define AMEBA_I2S1_WS 43
```

<a id="a3136f2fc775bb63f80203ca8859627b2"></a>

### `AMEBA_IR_RX`

```c
#define AMEBA_IR_RX 65
```

<a id="a654f82f22bb941b39469479e968bc8b0"></a>

### `AMEBA_IR_TX`

```c
#define AMEBA_IR_TX 64
```

<a id="a264ddf441d53174b4d1704766c1949a9"></a>

### `AMEBA_KEY_COL0`

```c
#define AMEBA_KEY_COL0 74
```

<a id="a73d6054f140bce50d34ff44bb67a9b84"></a>

### `AMEBA_KEY_COL1`

```c
#define AMEBA_KEY_COL1 75
```

<a id="a92056df7355db7d9ef9dfe6e7fbf9a05"></a>

### `AMEBA_KEY_COL2`

```c
#define AMEBA_KEY_COL2 76
```

<a id="a29595b16e0b733884cf5e6fe17506829"></a>

### `AMEBA_KEY_COL3`

```c
#define AMEBA_KEY_COL3 77
```

<a id="aa9a62b2e36f920095d41750a19e37376"></a>

### `AMEBA_KEY_COL4`

```c
#define AMEBA_KEY_COL4 78
```

<a id="afb0ffaf9f21faf3f8a7c124b1eec5a16"></a>

### `AMEBA_KEY_COL5`

```c
#define AMEBA_KEY_COL5 79
```

<a id="aa481e74a6f56e8602e196176c0d5d270"></a>

### `AMEBA_KEY_COL6`

```c
#define AMEBA_KEY_COL6 80
```

<a id="a3e2bf6dbf31fd769b7159f18361b1443"></a>

### `AMEBA_KEY_COL7`

```c
#define AMEBA_KEY_COL7 81
```

<a id="a85a9f78d1ffd075bc5266baf4ed774f0"></a>

### `AMEBA_KEY_ROW0`

```c
#define AMEBA_KEY_ROW0 66
```

<a id="a005046634079b69a462c87d23ca93f4e"></a>

### `AMEBA_KEY_ROW1`

```c
#define AMEBA_KEY_ROW1 67
```

<a id="a2d56cc79fad59e8514ef9a0b478ec687"></a>

### `AMEBA_KEY_ROW2`

```c
#define AMEBA_KEY_ROW2 68
```

<a id="a158da1991effcddbf38de5fc76e475ec"></a>

### `AMEBA_KEY_ROW3`

```c
#define AMEBA_KEY_ROW3 69
```

<a id="ae9df5b1c30ec6a7c538e26eb7ab69930"></a>

### `AMEBA_KEY_ROW4`

```c
#define AMEBA_KEY_ROW4 70
```

<a id="ac63dacaee881249d2d9b6c4ca8002c48"></a>

### `AMEBA_KEY_ROW5`

```c
#define AMEBA_KEY_ROW5 71
```

<a id="a34fab16293055315512bc9b41eec2166"></a>

### `AMEBA_KEY_ROW6`

```c
#define AMEBA_KEY_ROW6 72
```

<a id="a6f86c3dfe508a5d7904ef018942dba28"></a>

### `AMEBA_KEY_ROW7`

```c
#define AMEBA_KEY_ROW7 73
```

<a id="aa117a91002cec5d0421c0b9958f90d5e"></a>

### `AMEBA_LEDC`

```c
#define AMEBA_LEDC 33
```

<a id="a43b82c67e7ed46c4d7504354b89766a2"></a>

### `AMEBA_LOG_UART`

```c
#define AMEBA_LOG_UART 1
```

<a id="ad8ded7699c9503bf9e0f89ef27460de0"></a>

### `AMEBA_OSPI`

```c
#define AMEBA_OSPI 5
```

<a id="a71d265adf87eb5aa7e991bf0dd6c142f"></a>

### `AMEBA_PINMUX`

```c
#define AMEBA_PINMUX ( port, line, funcid )
```

展开值（Value）：

```c
(((AMEBA_PORT_PIN(port, line)) << 8) | (funcid))
```

<a id="a01f0e522a7c41526681b766c7ac7ce1f"></a>

### `AMEBA_PORT_PIN`

```c
#define AMEBA_PORT_PIN ( port, line )
```

展开值（Value）：

```c
((((port) - 'A') << 5) + (line))
```

<a id="a5c38d8038284dab2ffdc4b8e6f7750b3"></a>

### `AMEBA_PWM0`

```c
#define AMEBA_PWM0 52
```

<a id="a86aaa57f39ca21f312d0d0ca338ddec8"></a>

### `AMEBA_PWM1`

```c
#define AMEBA_PWM1 53
```

<a id="ae79456baaa4aec51c69f000937401eac"></a>

### `AMEBA_PWM2`

```c
#define AMEBA_PWM2 54
```

<a id="ac2c77f1b466e0b3d9c8b7b1c5086c9ee"></a>

### `AMEBA_PWM3`

```c
#define AMEBA_PWM3 55
```

<a id="a244a6609f273fa3bc80f889ccb6592ba"></a>

### `AMEBA_PWM4`

```c
#define AMEBA_PWM4 56
```

<a id="a71d62bc7ff0d9606132b453da0bd43b8"></a>

### `AMEBA_PWM5`

```c
#define AMEBA_PWM5 57
```

<a id="ad2e2672cf5229610ccac83fb9602046a"></a>

### `AMEBA_PWM6`

```c
#define AMEBA_PWM6 58
```

<a id="a522f21781b09e9f2f60500dad5912dce"></a>

### `AMEBA_PWM7`

```c
#define AMEBA_PWM7 59
```

<a id="a47e10b04eb5bfc28b3f0ceb9b75afffd"></a>

### `AMEBA_QSPI`

```c
#define AMEBA_QSPI 5
```

<a id="aafa0395014ea6191b12b50b89ed01bc8"></a>

### `AMEBA_SDIO`

```c
#define AMEBA_SDIO 10
```

<a id="aafdc733867a4ab1a0d16429679b19cba"></a>

### `AMEBA_SIC`

```c
#define AMEBA_SIC 7
```

<a id="abda4dcf809ca676e918866ddd7ddd097"></a>

### `AMEBA_SPI`

```c
#define AMEBA_SPI 8
```

<a id="a1997336af677a35e15d1402aed065ee6"></a>

### `AMEBA_SPI1_CLK`

```c
#define AMEBA_SPI1_CLK 29
```

<a id="a9113912d0b976fd5539fbd003e83d85f"></a>

### `AMEBA_SPI1_CS`

```c
#define AMEBA_SPI1_CS 32
```

<a id="ab40628d9a44f82362da70ab685c41cee"></a>

### `AMEBA_SPI1_MISO`

```c
#define AMEBA_SPI1_MISO 30
```

<a id="ab9a8e9f5f8c3160a04998960c61e8b4d"></a>

### `AMEBA_SPI1_MOSI`

```c
#define AMEBA_SPI1_MOSI 31
```

<a id="add660cc0a513fed62fe5d5e2ec12e5a7"></a>

### `AMEBA_SPIC0_FLASH`

```c
#define AMEBA_SPIC0_FLASH 2
```

<a id="a5eb4f7828f8f9aab06d02ba35f4daf6f"></a>

### `AMEBA_SPIC1_FLASH`

```c
#define AMEBA_SPIC1_FLASH 3
```

<a id="a97aa1778f7670f03bc30a9cc156c3da1"></a>

### `AMEBA_SPIC1_PSRAM`

```c
#define AMEBA_SPIC1_PSRAM 4
```

<a id="a0d8fdf8ef3539a8cfe2b6e57f8e5db8d"></a>

### `AMEBA_SWD`

```c
#define AMEBA_SWD 9
```

<a id="a01e0fb61666dcce90f9e23573f180f00"></a>

### `AMEBA_TIMER`

```c
#define AMEBA_TIMER 16
```

<a id="a741c7c7e636536003ed508abd2d47d97"></a>

### `AMEBA_UART`

```c
#define AMEBA_UART 1
```

<a id="aec676f180cd6c8ebde85b78984953106"></a>

### `AMEBA_UART0_CTS`

```c
#define AMEBA_UART0_CTS 21
```

<a id="aa6ee6a2d6312b5a92db53caf4424490e"></a>

### `AMEBA_UART0_RTS`

```c
#define AMEBA_UART0_RTS 22
```

<a id="aa93af39fe6c222c908a7642f5a4349a8"></a>

### `AMEBA_UART0_RXD`

```c
#define AMEBA_UART0_RXD 20
```

<a id="a74d6af9b061345287512018abbe6cdc0"></a>

### `AMEBA_UART0_TXD`

```c
#define AMEBA_UART0_TXD 19
```

<a id="a76f722879ffac4f94f543ebfc514fb7f"></a>

### `AMEBA_UART1_RXD`

```c
#define AMEBA_UART1_RXD 24
```

<a id="a5264a7b7b4e1dc4e66abf649d6fbf398"></a>

### `AMEBA_UART1_TXD`

```c
#define AMEBA_UART1_TXD 23
```

<a id="a8a504db1a6c395a5fc694dd092f4ab1c"></a>

### `AMEBA_UART2_CTS`

```c
#define AMEBA_UART2_CTS 27
```

<a id="a224062161ec641f0cf26551562e3cd3e"></a>

### `AMEBA_UART2_RTS`

```c
#define AMEBA_UART2_RTS 28
```

<a id="a8b9308171579c28194d890a90cdf68be"></a>

### `AMEBA_UART2_RXD`

```c
#define AMEBA_UART2_RXD 26
```

<a id="a8eb069f61c95598413fb9cda6304b287"></a>

### `AMEBA_UART2_TXD`

```c
#define AMEBA_UART2_TXD 25
```

<a id="adfeeeb74cd0157b09992ec5e5f4e5397"></a>

### `AMEBA_USB`

```c
#define AMEBA_USB 17
```


## 12.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_configuration_reference/P004_amebadplus-pinctrl.h_源码浏览.md)
- [AMEBA_PORT_PIN](P011_zephyr__dt-bindings__pinctrl__amebad-pinctrl.h_文件参考.md#a01f0e522a7c41526681b766c7ac7ce1f)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="aamebad-pinctrl_8h_html_a01f0e522a7c41526681b766c7ac7ce1f"></a>

---

[上一章](P011_zephyr__dt-bindings__pinctrl__amebad-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P013_zephyr__arch__cpu.h_文件参考.md)
