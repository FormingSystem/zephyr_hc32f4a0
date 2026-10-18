---
id: learning.zephyr-docs.api-file-reference.page-353
title: zephyr__dt-bindings__clock__renesas_rztn_clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas__rztn__clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第353章\_zephyr\_\_dt-bindings\_\_clock\_\_renesas\_rztn\_clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rztn__clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 353.1\_宏定义（Macros）

<a id="r_af22fb58317528ced8ad8cdfc399ad2ac"></a>

```c
#define RZ_IP_MASK 0xFF0000UL
```

相关声明：[RZ_IP_MASK](#af22fb58317528ced8ad8cdfc399ad2ac)。

<a id="r_a0bfeafa5676753c0e6750a9c3c2f18f1"></a>

```c
#define RZ_IP_SHIFT 16UL
```

相关声明：[RZ_IP_SHIFT](#a0bfeafa5676753c0e6750a9c3c2f18f1)。

<a id="r_a73baaadd858826d7b7e613120a9e4509"></a>

```c
#define RZ_IP_CH_MASK 0xFF00UL
```

相关声明：[RZ_IP_CH_MASK](#a73baaadd858826d7b7e613120a9e4509)。

<a id="r_a4854f76eb8144726dcc49da30bb49494"></a>

```c
#define RZ_IP_CH_SHIFT 8UL
```

相关声明：[RZ_IP_CH_SHIFT](#a4854f76eb8144726dcc49da30bb49494)。

<a id="r_a9712059a7005130fbeb48f2ce7f45f66"></a>

```c
#define RZ_CLOCK_MASK 0xFFUL
```

相关声明：[RZ_CLOCK_MASK](#a9712059a7005130fbeb48f2ce7f45f66)。

<a id="r_a0f4444cd8f843699d43be43968a76f60"></a>

```c
#define RZ_CLOCK_SHIFT 0UL
```

相关声明：[RZ_CLOCK_SHIFT](#a0f4444cd8f843699d43be43968a76f60)。

<a id="r_a91c871d1e31de6ca2b909855bb8e0e97"></a>

```c
#define RZ_IP_BSC 0UL /* Bus State Controller */
```

相关声明：[RZ_IP_BSC](#a91c871d1e31de6ca2b909855bb8e0e97)。

<a id="r_a8fb0c098b586ea0696813fc5988e70b7"></a>

```c
#define RZ_IP_XSPI 1UL /* Expanded Serial Peripheral Interface */
```

相关声明：[RZ_IP_XSPI](#a8fb0c098b586ea0696813fc5988e70b7)。

<a id="r_a55ab8413b73bfe6a7de0b5eef4c9575f"></a>

```c
#define RZ_IP_SCI 2UL /* Serial Communications Interface */
```

相关声明：[RZ_IP_SCI](#a55ab8413b73bfe6a7de0b5eef4c9575f)。

<a id="r_ae26e6a19b9874cdf48dba7f3940c717e"></a>

```c
#define RZ_IP_IIC 3UL /* I2C Bus Interface */
```

相关声明：[RZ_IP_IIC](#ae26e6a19b9874cdf48dba7f3940c717e)。

<a id="r_a962042132501ac383ac3c83ddb708e12"></a>

```c
#define RZ_IP_SPI 4UL /* Serial Peripheral Interface */
```

相关声明：[RZ_IP_SPI](#a962042132501ac383ac3c83ddb708e12)。

<a id="r_a258d150ad8458cb580f823296dd4b863"></a>

```c
#define RZ_IP_GPT 5UL /* General PWM Timer */
```

相关声明：[RZ_IP_GPT](#a258d150ad8458cb580f823296dd4b863)。

<a id="r_ac5286aa047cc19375a976b3ba920d7d2"></a>

```c
#define RZ_IP_ADC12 6UL /* 12-Bit A/D Converter */
```

相关声明：[RZ_IP_ADC12](#ac5286aa047cc19375a976b3ba920d7d2)。

<a id="r_a773a2337fb3ada02b5f001cde2fbef1e"></a>

```c
#define RZ_IP_CMT 7UL /* Compare Match Timer */
```

相关声明：[RZ_IP_CMT](#a773a2337fb3ada02b5f001cde2fbef1e)。

<a id="r_a497266119761395773587dd03fb7224a"></a>

```c
#define RZ_IP_CMTW 8UL /* Compare Match Timer W */
```

相关声明：[RZ_IP_CMTW](#a497266119761395773587dd03fb7224a)。

<a id="r_a2a5b46c7954d9931d05ba9b78b6bfa92"></a>

```c
#define RZ_IP_CANFD 9UL /* Controller Area Network with Flexible Data Rate */
```

相关声明：[RZ_IP_CANFD](#a2a5b46c7954d9931d05ba9b78b6bfa92)。

<a id="r_ae7b8b535feda190b5e2ccc42540f5e12"></a>

```c
#define RZ_IP_GMAC 10UL /* Ethernet MAC */
```

相关声明：[RZ_IP_GMAC](#ae7b8b535feda190b5e2ccc42540f5e12)。

<a id="r_a6fd42b0ffe65ebdcb08dce4a04cd6495"></a>

```c
#define RZ_IP_ETHSW 11UL /* Ethernet Switch */
```

相关声明：[RZ_IP_ETHSW](#a6fd42b0ffe65ebdcb08dce4a04cd6495)。

<a id="r_af878d4d2101e50fabe4f9a383a320941"></a>

```c
#define RZ_IP_USBHS 12UL /* USB High Speed */
```

相关声明：[RZ_IP_USBHS](#af878d4d2101e50fabe4f9a383a320941)。

<a id="r_abdc91564fb2128777f35acfc18b00381"></a>

```c
#define RZ_IP_RTC 13UL /* Real Time Clock */
```

相关声明：[RZ_IP_RTC](#abdc91564fb2128777f35acfc18b00381)。

<a id="r_acc33b854201c1951b5534980ba564d36"></a>

```c
#define RZ_CLOCK_CPU0 0UL
```

相关声明：[RZ_CLOCK_CPU0](#acc33b854201c1951b5534980ba564d36)。

<a id="r_a329f711adc6d19ea3b6c89ced543d8b8"></a>

```c
#define RZ_CLOCK_CPU1 1UL
```

相关声明：[RZ_CLOCK_CPU1](#a329f711adc6d19ea3b6c89ced543d8b8)。

<a id="r_ae1e0140035db269b0c15f11703cda080"></a>

```c
#define RZ_CLOCK_CA55C0 2UL
```

相关声明：[RZ_CLOCK_CA55C0](#ae1e0140035db269b0c15f11703cda080)。

<a id="r_a1f470d91b9408f39212eb40160735bd1"></a>

```c
#define RZ_CLOCK_CA55C1 3UL
```

相关声明：[RZ_CLOCK_CA55C1](#a1f470d91b9408f39212eb40160735bd1)。

<a id="r_a0c4f35a6b9363d31420acf98961e059c"></a>

```c
#define RZ_CLOCK_CA55C2 4UL
```

相关声明：[RZ_CLOCK_CA55C2](#a0c4f35a6b9363d31420acf98961e059c)。

<a id="r_a4f4111149c632ee2963608ea6edf3276"></a>

```c
#define RZ_CLOCK_CA55C3 5UL
```

相关声明：[RZ_CLOCK_CA55C3](#a4f4111149c632ee2963608ea6edf3276)。

<a id="r_ac7bdc55a778921460c6db5a9c80572ac"></a>

```c
#define RZ_CLOCK_CA55SCLK 6UL
```

相关声明：[RZ_CLOCK_CA55SCLK](#ac7bdc55a778921460c6db5a9c80572ac)。

<a id="r_a244252c9570d2ce5142a1dacb71aca93"></a>

```c
#define RZ_CLOCK_ICLK 7UL
```

相关声明：[RZ_CLOCK_ICLK](#a244252c9570d2ce5142a1dacb71aca93)。

<a id="r_af0fa2e160de5dad74810b664af883e70"></a>

```c
#define RZ_CLOCK_PCLKH 8UL
```

相关声明：[RZ_CLOCK_PCLKH](#af0fa2e160de5dad74810b664af883e70)。

<a id="r_ab9b7e7f0b422a9af426c1992efa3cd83"></a>

```c
#define RZ_CLOCK_PCLKM 9UL
```

相关声明：[RZ_CLOCK_PCLKM](#ab9b7e7f0b422a9af426c1992efa3cd83)。

<a id="r_aade991a73b4ee5a5ee8794028ed3d56b"></a>

```c
#define RZ_CLOCK_PCLKL 10UL
```

相关声明：[RZ_CLOCK_PCLKL](#aade991a73b4ee5a5ee8794028ed3d56b)。

<a id="r_af9f63991d415890baef866a59ccf93a9"></a>

```c
#define RZ_CLOCK_PCLKADC 11UL
```

相关声明：[RZ_CLOCK_PCLKADC](#af9f63991d415890baef866a59ccf93a9)。

<a id="r_aa12c594f91b8cbb48603e76ca65d1fcd"></a>

```c
#define RZ_CLOCK_PCLKGPTL 12UL
```

相关声明：[RZ_CLOCK_PCLKGPTL](#aa12c594f91b8cbb48603e76ca65d1fcd)。

<a id="r_a6beef6c4580cf90ba9926917b2eabf82"></a>

```c
#define RZ_CLOCK_PCLKENCO 13UL
```

相关声明：[RZ_CLOCK_PCLKENCO](#a6beef6c4580cf90ba9926917b2eabf82)。

<a id="r_a6169e7e612ad536fcbfa7540ab539bbc"></a>

```c
#define RZ_CLOCK_PCLKSPI0 14UL
```

相关声明：[RZ_CLOCK_PCLKSPI0](#a6169e7e612ad536fcbfa7540ab539bbc)。

<a id="r_ab61df153046de85c1928a01ed264001d"></a>

```c
#define RZ_CLOCK_PCLKSPI1 15UL
```

相关声明：[RZ_CLOCK_PCLKSPI1](#ab61df153046de85c1928a01ed264001d)。

<a id="r_ad349058746955b709abb4173c7d1c91d"></a>

```c
#define RZ_CLOCK_PCLKSPI2 16UL
```

相关声明：[RZ_CLOCK_PCLKSPI2](#ad349058746955b709abb4173c7d1c91d)。

<a id="r_aa9e3ed64f80f175706a983601dacc231"></a>

```c
#define RZ_CLOCK_PCLKSPI3 17UL
```

相关声明：[RZ_CLOCK_PCLKSPI3](#aa9e3ed64f80f175706a983601dacc231)。

<a id="r_a8beb57b962482d7d7e27d53257ebc5cf"></a>

```c
#define RZ_CLOCK_PCLKSCI0 18UL
```

相关声明：[RZ_CLOCK_PCLKSCI0](#a8beb57b962482d7d7e27d53257ebc5cf)。

<a id="r_a4df8585ee595b7513f11c0af5330742e"></a>

```c
#define RZ_CLOCK_PCLKSCI1 19UL
```

相关声明：[RZ_CLOCK_PCLKSCI1](#a4df8585ee595b7513f11c0af5330742e)。

<a id="r_a5c6230ef0616f4836b8555c686e89b2e"></a>

```c
#define RZ_CLOCK_PCLKSCI2 20UL
```

相关声明：[RZ_CLOCK_PCLKSCI2](#a5c6230ef0616f4836b8555c686e89b2e)。

<a id="r_a6ef47f4cdb838561183280cbce27283f"></a>

```c
#define RZ_CLOCK_PCLKSCI3 21UL
```

相关声明：[RZ_CLOCK_PCLKSCI3](#a6ef47f4cdb838561183280cbce27283f)。

<a id="r_ada90ef536bf0aba81ee545f72253502b"></a>

```c
#define RZ_CLOCK_PCLKSCI4 22UL
```

相关声明：[RZ_CLOCK_PCLKSCI4](#ada90ef536bf0aba81ee545f72253502b)。

<a id="r_a5b49d7f7749f34b9d59415347b7c7e65"></a>

```c
#define RZ_CLOCK_PCLKSCI5 23UL
```

相关声明：[RZ_CLOCK_PCLKSCI5](#a5b49d7f7749f34b9d59415347b7c7e65)。

<a id="r_a55911d99d3d304626b069dce0e92f66c"></a>

```c
#define RZ_CLOCK_PCLKSCIE0 24UL
```

相关声明：[RZ_CLOCK_PCLKSCIE0](#a55911d99d3d304626b069dce0e92f66c)。

<a id="r_ab3ad630bfbefa6868e0e1c4926b5327b"></a>

```c
#define RZ_CLOCK_PCLKSCIE1 25UL
```

相关声明：[RZ_CLOCK_PCLKSCIE1](#ab3ad630bfbefa6868e0e1c4926b5327b)。

<a id="r_a3d23da62a624da121b5828c34d95496c"></a>

```c
#define RZ_CLOCK_PCLKSCIE2 26UL
```

相关声明：[RZ_CLOCK_PCLKSCIE2](#a3d23da62a624da121b5828c34d95496c)。

<a id="r_a0de9e5c0199b421445d8a150a37f4fc6"></a>

```c
#define RZ_CLOCK_PCLKSCIE3 27UL
```

相关声明：[RZ_CLOCK_PCLKSCIE3](#a0de9e5c0199b421445d8a150a37f4fc6)。

<a id="r_ab9167e2775a2e8a9d4a01752e52f713f"></a>

```c
#define RZ_CLOCK_PCLKSCIE4 28UL
```

相关声明：[RZ_CLOCK_PCLKSCIE4](#ab9167e2775a2e8a9d4a01752e52f713f)。

<a id="r_ae6ee5caddca3729e9211862967c7652e"></a>

```c
#define RZ_CLOCK_PCLKSCIE5 29UL
```

相关声明：[RZ_CLOCK_PCLKSCIE5](#ae6ee5caddca3729e9211862967c7652e)。

<a id="r_a7f614472154843efe3c741aea030a078"></a>

```c
#define RZ_CLOCK_PCLKSCIE6 30UL
```

相关声明：[RZ_CLOCK_PCLKSCIE6](#a7f614472154843efe3c741aea030a078)。

<a id="r_adcd9e1a23c9c9fa857f93dca2c6fb2dc"></a>

```c
#define RZ_CLOCK_PCLKSCIE7 31UL
```

相关声明：[RZ_CLOCK_PCLKSCIE7](#adcd9e1a23c9c9fa857f93dca2c6fb2dc)。

<a id="r_a37b44481923eedef4d00398d128c7896"></a>

```c
#define RZ_CLOCK_PCLKSCIE8 32UL
```

相关声明：[RZ_CLOCK_PCLKSCIE8](#a37b44481923eedef4d00398d128c7896)。

<a id="r_acb0c67c8ccf4f350fa9e593be41b5e4c"></a>

```c
#define RZ_CLOCK_PCLKSCIE9 33UL
```

相关声明：[RZ_CLOCK_PCLKSCIE9](#acb0c67c8ccf4f350fa9e593be41b5e4c)。

<a id="r_a972cc3ba3a0819e821e1ff5de71f1909"></a>

```c
#define RZ_CLOCK_PCLKSCIE10 34UL
```

相关声明：[RZ_CLOCK_PCLKSCIE10](#a972cc3ba3a0819e821e1ff5de71f1909)。

<a id="r_ad6f3f46c9f89d2a038a6eab2e529320b"></a>

```c
#define RZ_CLOCK_PCLKSCIE11 35UL
```

相关声明：[RZ_CLOCK_PCLKSCIE11](#ad6f3f46c9f89d2a038a6eab2e529320b)。

<a id="r_a52bbf129fbe949ef3158e59e10be1aab"></a>

```c
#define RZ_CLOCK_PCLKCAN 36UL
```

相关声明：[RZ_CLOCK_PCLKCAN](#a52bbf129fbe949ef3158e59e10be1aab)。

<a id="r_a588dcee0a18bddbb41a1f97460315065"></a>

```c
#define RZ_CLOCK_CKIO 37UL
```

相关声明：[RZ_CLOCK_CKIO](#a588dcee0a18bddbb41a1f97460315065)。

<a id="r_a08b86025717489597433457eb54f5d3d"></a>

```c
#define RZ_CLOCK_XSPI0_CLK 38UL
```

相关声明：[RZ_CLOCK_XSPI0_CLK](#a08b86025717489597433457eb54f5d3d)。

<a id="r_a98c6a2060edddfd8d667d52ff65183de"></a>

```c
#define RZ_CLOCK_XSPI1_CLK 39UL
```

相关声明：[RZ_CLOCK_XSPI1_CLK](#a98c6a2060edddfd8d667d52ff65183de)。

<a id="r_ac7432d44afb38887d5c89dc8c455b287"></a>

```c
#define RZ_CLOCK(IP, ch, clk)
```

相关声明：[RZ_CLOCK](#ac7432d44afb38887d5c89dc8c455b287)。

## 353.2\_详细说明（Detailed Documentation）

<a id="ac7432d44afb38887d5c89dc8c455b287"></a>

### `RZ_CLOCK`

```c
#define RZ_CLOCK ( IP, ch, clk )
```

展开值（Value）：

```c
((IP << RZ_IP_SHIFT) | ((ch) << RZ_IP_CH_SHIFT) | ((clk) << RZ_CLOCK_SHIFT))
```

<a id="ae1e0140035db269b0c15f11703cda080"></a>

### `RZ_CLOCK_CA55C0`

```c
#define RZ_CLOCK_CA55C0 2UL
```

<a id="a1f470d91b9408f39212eb40160735bd1"></a>

### `RZ_CLOCK_CA55C1`

```c
#define RZ_CLOCK_CA55C1 3UL
```

<a id="a0c4f35a6b9363d31420acf98961e059c"></a>

### `RZ_CLOCK_CA55C2`

```c
#define RZ_CLOCK_CA55C2 4UL
```

<a id="a4f4111149c632ee2963608ea6edf3276"></a>

### `RZ_CLOCK_CA55C3`

```c
#define RZ_CLOCK_CA55C3 5UL
```

<a id="ac7bdc55a778921460c6db5a9c80572ac"></a>

### `RZ_CLOCK_CA55SCLK`

```c
#define RZ_CLOCK_CA55SCLK 6UL
```

<a id="a588dcee0a18bddbb41a1f97460315065"></a>

### `RZ_CLOCK_CKIO`

```c
#define RZ_CLOCK_CKIO 37UL
```

<a id="acc33b854201c1951b5534980ba564d36"></a>

### `RZ_CLOCK_CPU0`

```c
#define RZ_CLOCK_CPU0 0UL
```

<a id="a329f711adc6d19ea3b6c89ced543d8b8"></a>

### `RZ_CLOCK_CPU1`

```c
#define RZ_CLOCK_CPU1 1UL
```

<a id="a244252c9570d2ce5142a1dacb71aca93"></a>

### `RZ_CLOCK_ICLK`

```c
#define RZ_CLOCK_ICLK 7UL
```

<a id="a9712059a7005130fbeb48f2ce7f45f66"></a>

### `RZ_CLOCK_MASK`

```c
#define RZ_CLOCK_MASK 0xFFUL
```

<a id="af9f63991d415890baef866a59ccf93a9"></a>

### `RZ_CLOCK_PCLKADC`

```c
#define RZ_CLOCK_PCLKADC 11UL
```

<a id="a52bbf129fbe949ef3158e59e10be1aab"></a>

### `RZ_CLOCK_PCLKCAN`

```c
#define RZ_CLOCK_PCLKCAN 36UL
```

<a id="a6beef6c4580cf90ba9926917b2eabf82"></a>

### `RZ_CLOCK_PCLKENCO`

```c
#define RZ_CLOCK_PCLKENCO 13UL
```

<a id="aa12c594f91b8cbb48603e76ca65d1fcd"></a>

### `RZ_CLOCK_PCLKGPTL`

```c
#define RZ_CLOCK_PCLKGPTL 12UL
```

<a id="af0fa2e160de5dad74810b664af883e70"></a>

### `RZ_CLOCK_PCLKH`

```c
#define RZ_CLOCK_PCLKH 8UL
```

<a id="aade991a73b4ee5a5ee8794028ed3d56b"></a>

### `RZ_CLOCK_PCLKL`

```c
#define RZ_CLOCK_PCLKL 10UL
```

<a id="ab9b7e7f0b422a9af426c1992efa3cd83"></a>

### `RZ_CLOCK_PCLKM`

```c
#define RZ_CLOCK_PCLKM 9UL
```

<a id="a8beb57b962482d7d7e27d53257ebc5cf"></a>

### `RZ_CLOCK_PCLKSCI0`

```c
#define RZ_CLOCK_PCLKSCI0 18UL
```

<a id="a4df8585ee595b7513f11c0af5330742e"></a>

### `RZ_CLOCK_PCLKSCI1`

```c
#define RZ_CLOCK_PCLKSCI1 19UL
```

<a id="a5c6230ef0616f4836b8555c686e89b2e"></a>

### `RZ_CLOCK_PCLKSCI2`

```c
#define RZ_CLOCK_PCLKSCI2 20UL
```

<a id="a6ef47f4cdb838561183280cbce27283f"></a>

### `RZ_CLOCK_PCLKSCI3`

```c
#define RZ_CLOCK_PCLKSCI3 21UL
```

<a id="ada90ef536bf0aba81ee545f72253502b"></a>

### `RZ_CLOCK_PCLKSCI4`

```c
#define RZ_CLOCK_PCLKSCI4 22UL
```

<a id="a5b49d7f7749f34b9d59415347b7c7e65"></a>

### `RZ_CLOCK_PCLKSCI5`

```c
#define RZ_CLOCK_PCLKSCI5 23UL
```

<a id="a55911d99d3d304626b069dce0e92f66c"></a>

### `RZ_CLOCK_PCLKSCIE0`

```c
#define RZ_CLOCK_PCLKSCIE0 24UL
```

<a id="ab3ad630bfbefa6868e0e1c4926b5327b"></a>

### `RZ_CLOCK_PCLKSCIE1`

```c
#define RZ_CLOCK_PCLKSCIE1 25UL
```

<a id="a972cc3ba3a0819e821e1ff5de71f1909"></a>

### `RZ_CLOCK_PCLKSCIE10`

```c
#define RZ_CLOCK_PCLKSCIE10 34UL
```

<a id="ad6f3f46c9f89d2a038a6eab2e529320b"></a>

### `RZ_CLOCK_PCLKSCIE11`

```c
#define RZ_CLOCK_PCLKSCIE11 35UL
```

<a id="a3d23da62a624da121b5828c34d95496c"></a>

### `RZ_CLOCK_PCLKSCIE2`

```c
#define RZ_CLOCK_PCLKSCIE2 26UL
```

<a id="a0de9e5c0199b421445d8a150a37f4fc6"></a>

### `RZ_CLOCK_PCLKSCIE3`

```c
#define RZ_CLOCK_PCLKSCIE3 27UL
```

<a id="ab9167e2775a2e8a9d4a01752e52f713f"></a>

### `RZ_CLOCK_PCLKSCIE4`

```c
#define RZ_CLOCK_PCLKSCIE4 28UL
```

<a id="ae6ee5caddca3729e9211862967c7652e"></a>

### `RZ_CLOCK_PCLKSCIE5`

```c
#define RZ_CLOCK_PCLKSCIE5 29UL
```

<a id="a7f614472154843efe3c741aea030a078"></a>

### `RZ_CLOCK_PCLKSCIE6`

```c
#define RZ_CLOCK_PCLKSCIE6 30UL
```

<a id="adcd9e1a23c9c9fa857f93dca2c6fb2dc"></a>

### `RZ_CLOCK_PCLKSCIE7`

```c
#define RZ_CLOCK_PCLKSCIE7 31UL
```

<a id="a37b44481923eedef4d00398d128c7896"></a>

### `RZ_CLOCK_PCLKSCIE8`

```c
#define RZ_CLOCK_PCLKSCIE8 32UL
```

<a id="acb0c67c8ccf4f350fa9e593be41b5e4c"></a>

### `RZ_CLOCK_PCLKSCIE9`

```c
#define RZ_CLOCK_PCLKSCIE9 33UL
```

<a id="a6169e7e612ad536fcbfa7540ab539bbc"></a>

### `RZ_CLOCK_PCLKSPI0`

```c
#define RZ_CLOCK_PCLKSPI0 14UL
```

<a id="ab61df153046de85c1928a01ed264001d"></a>

### `RZ_CLOCK_PCLKSPI1`

```c
#define RZ_CLOCK_PCLKSPI1 15UL
```

<a id="ad349058746955b709abb4173c7d1c91d"></a>

### `RZ_CLOCK_PCLKSPI2`

```c
#define RZ_CLOCK_PCLKSPI2 16UL
```

<a id="aa9e3ed64f80f175706a983601dacc231"></a>

### `RZ_CLOCK_PCLKSPI3`

```c
#define RZ_CLOCK_PCLKSPI3 17UL
```

<a id="a0f4444cd8f843699d43be43968a76f60"></a>

### `RZ_CLOCK_SHIFT`

```c
#define RZ_CLOCK_SHIFT 0UL
```

<a id="a08b86025717489597433457eb54f5d3d"></a>

### `RZ_CLOCK_XSPI0_CLK`

```c
#define RZ_CLOCK_XSPI0_CLK 38UL
```

<a id="a98c6a2060edddfd8d667d52ff65183de"></a>

### `RZ_CLOCK_XSPI1_CLK`

```c
#define RZ_CLOCK_XSPI1_CLK 39UL
```

<a id="ac5286aa047cc19375a976b3ba920d7d2"></a>

### `RZ_IP_ADC12`

```c
#define RZ_IP_ADC12 6UL /* 12-Bit A/D Converter */
```

<a id="a91c871d1e31de6ca2b909855bb8e0e97"></a>

### `RZ_IP_BSC`

```c
#define RZ_IP_BSC 0UL /* Bus State Controller */
```

<a id="a2a5b46c7954d9931d05ba9b78b6bfa92"></a>

### `RZ_IP_CANFD`

```c
#define RZ_IP_CANFD 9UL /* Controller Area Network with Flexible Data Rate */
```

<a id="a73baaadd858826d7b7e613120a9e4509"></a>

### `RZ_IP_CH_MASK`

```c
#define RZ_IP_CH_MASK 0xFF00UL
```

<a id="a4854f76eb8144726dcc49da30bb49494"></a>

### `RZ_IP_CH_SHIFT`

```c
#define RZ_IP_CH_SHIFT 8UL
```

<a id="a773a2337fb3ada02b5f001cde2fbef1e"></a>

### `RZ_IP_CMT`

```c
#define RZ_IP_CMT 7UL /* Compare Match Timer */
```

<a id="a497266119761395773587dd03fb7224a"></a>

### `RZ_IP_CMTW`

```c
#define RZ_IP_CMTW 8UL /* Compare Match Timer W */
```

<a id="a6fd42b0ffe65ebdcb08dce4a04cd6495"></a>

### `RZ_IP_ETHSW`

```c
#define RZ_IP_ETHSW 11UL /* Ethernet Switch */
```

<a id="ae7b8b535feda190b5e2ccc42540f5e12"></a>

### `RZ_IP_GMAC`

```c
#define RZ_IP_GMAC 10UL /* Ethernet MAC */
```

<a id="a258d150ad8458cb580f823296dd4b863"></a>

### `RZ_IP_GPT`

```c
#define RZ_IP_GPT 5UL /* General PWM Timer */
```

<a id="ae26e6a19b9874cdf48dba7f3940c717e"></a>

### `RZ_IP_IIC`

```c
#define RZ_IP_IIC 3UL /* I2C Bus Interface */
```

<a id="af22fb58317528ced8ad8cdfc399ad2ac"></a>

### `RZ_IP_MASK`

```c
#define RZ_IP_MASK 0xFF0000UL
```

<a id="abdc91564fb2128777f35acfc18b00381"></a>

### `RZ_IP_RTC`

```c
#define RZ_IP_RTC 13UL /* Real Time Clock */
```

<a id="a55ab8413b73bfe6a7de0b5eef4c9575f"></a>

### `RZ_IP_SCI`

```c
#define RZ_IP_SCI 2UL /* Serial Communications Interface */
```

<a id="a0bfeafa5676753c0e6750a9c3c2f18f1"></a>

### `RZ_IP_SHIFT`

```c
#define RZ_IP_SHIFT 16UL
```

<a id="a962042132501ac383ac3c83ddb708e12"></a>

### `RZ_IP_SPI`

```c
#define RZ_IP_SPI 4UL /* Serial Peripheral Interface */
```

<a id="af878d4d2101e50fabe4f9a383a320941"></a>

### `RZ_IP_USBHS`

```c
#define RZ_IP_USBHS 12UL /* USB High Speed */
```

<a id="a8fb0c098b586ea0696813fc5988e70b7"></a>

### `RZ_IP_XSPI`

```c
#define RZ_IP_XSPI 1UL /* Expanded Serial Peripheral Interface */
```


## 353.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rztn__clock_8h_source.html)
- [RZ_IP_SHIFT](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rza__clock_8h.html#a0bfeafa5676753c0e6750a9c3c2f18f1)
- [RZ_IP_CH_SHIFT](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rza__clock_8h.html#a4854f76eb8144726dcc49da30bb49494)
- [RZ_CLOCK_SHIFT](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rza__clock_8h.html#a0f4444cd8f843699d43be43968a76f60)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="arenesas__rza__clock_8h_html_a0bfeafa5676753c0e6750a9c3c2f18f1"></a>
<a id="arenesas__rza__clock_8h_html_a0f4444cd8f843699d43be43968a76f60"></a>
<a id="arenesas__rza__clock_8h_html_a4854f76eb8144726dcc49da30bb49494"></a>

---

[上一章](P352_zephyr__dt-bindings__pwm__renesas_rz_pwm.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P354_zephyr__dt-bindings__reset__gd32f3x0.h_文件参考.md)
