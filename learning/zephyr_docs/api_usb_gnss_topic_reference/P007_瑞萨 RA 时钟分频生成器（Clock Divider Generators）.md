---
id: learning.zephyr-docs.api-usb-gnss-topic-reference.page-7
title: 瑞萨 RA 时钟分频生成器（Clock Divider Generators）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_瑞萨 RA 时钟分频生成器（Clock Divider Generators）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

面向多个时钟域（Clock domains）的分频生成宏。

<a id="details"></a>

面向多个时钟域（Clock domains）的分频生成宏。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.1\_宏定义（Macros）

<a id="r_gac836d0409da1193de27a8c61510d06c5"></a>

```c
#define RA_CGC_DIV_BCLK(n)
```

相关声明：[RA_CGC_DIV_BCLK](#gac836d0409da1193de27a8c61510d06c5)。

BCLK 分频器（Divider）。

<a id="r_gaa6e8ba963160224076dacac43db705d7"></a>

```c
#define RA_CGC_DIV_CANFDCLK(n)
```

相关声明：[RA_CGC_DIV_CANFDCLK](#gaa6e8ba963160224076dacac43db705d7)。

CANFD 分频器（Divider）。

<a id="r_gaae1620e152c33e3d4a95b5cac0cb1c76"></a>

```c
#define RA_CGC_DIV_CECCLK(n)
```

相关声明：[RA_CGC_DIV_CECCLK](#gaae1620e152c33e3d4a95b5cac0cb1c76)。

CEC 分频器（Divider）。

<a id="r_ga8b169aba21f7e00cb80ffa0229cf0ca7"></a>

```c
#define RA_CGC_DIV_CLKOUT(n)
```

相关声明：[RA_CGC_DIV_CLKOUT](#ga8b169aba21f7e00cb80ffa0229cf0ca7)。

CLKOUT 分频器（Divider）。

<a id="r_ga5d01387282e98e3c1836cc18098726ec"></a>

```c
#define RA_CGC_DIV_CPUCLK0(n)
```

相关声明：[RA_CGC_DIV_CPUCLK0](#ga5d01387282e98e3c1836cc18098726ec)。

CPUCLK0 分频器（Divider）。

<a id="r_ga04c6195e596c187ec77ed5ebc8cd735b"></a>

```c
#define RA_CGC_DIV_CPUCLK1(n)
```

相关声明：[RA_CGC_DIV_CPUCLK1](#ga04c6195e596c187ec77ed5ebc8cd735b)。

CPUCLK1 分频器（Divider）。

<a id="r_gaa38d17ba1d228ca66ef1f21720bc05b4"></a>

```c
#define RA_CGC_DIV_MRPCLK(n)
```

相关声明：[RA_CGC_DIV_MRPCLK](#gaa38d17ba1d228ca66ef1f21720bc05b4)。

MRPCLK 分频器（Divider）。

<a id="r_gabf6b0bc9229f7b9b667662d5e7287af3"></a>

```c
#define RA_CGC_DIV_CPUCLK(n)
```

相关声明：[RA_CGC_DIV_CPUCLK](#gabf6b0bc9229f7b9b667662d5e7287af3)。

CPUCLK 分频器（Divider）。

<a id="r_ga8006ac020337b43c9039290de93b237c"></a>

```c
#define RA_CGC_DIV_FCLK(n)
```

相关声明：[RA_CGC_DIV_FCLK](#ga8006ac020337b43c9039290de93b237c)。

FCLK 分频器（Divider）。

<a id="r_gae414f33fc622f1eea25ed38b4e48b284"></a>

```c
#define RA_CGC_DIV_I3CCLK(n)
```

相关声明：[RA_CGC_DIV_I3CCLK](#gae414f33fc622f1eea25ed38b4e48b284)。

I3C 分频器（Divider）。

<a id="r_ga152905c07ac6744e4dbcaa88cc44b7b0"></a>

```c
#define RA_CGC_DIV_ICLK(n)
```

相关声明：[RA_CGC_DIV_ICLK](#ga152905c07ac6744e4dbcaa88cc44b7b0)。

ICLK 分频器（Divider）。

<a id="r_gade972ca4dc22a1438ae0ee8a7f0b1c86"></a>

```c
#define RA_CGC_DIV_LCDCLK(n)
```

相关声明：[RA_CGC_DIV_LCDCLK](#gade972ca4dc22a1438ae0ee8a7f0b1c86)。

LCDCLK 分频器（Divider）。

<a id="r_ga6e21efeff2e4b079ba56bf33524517d5"></a>

```c
#define RA_CGC_DIV_OCTASPICLK(n)
```

相关声明：[RA_CGC_DIV_OCTASPICLK](#ga6e21efeff2e4b079ba56bf33524517d5)。

OCTASPI 分频器（Divider）。

<a id="r_ga40a2d9224061ee4b25e98407ee60eecc"></a>

```c
#define RA_CGC_DIV_PCLKA(n)
```

相关声明：[RA_CGC_DIV_PCLKA](#ga40a2d9224061ee4b25e98407ee60eecc)。

PCLKA 分频器（Divider）。

<a id="r_gad3881c28b08b0775b6596f7e1932f2ff"></a>

```c
#define RA_CGC_DIV_PCLKB(n)
```

相关声明：[RA_CGC_DIV_PCLKB](#gad3881c28b08b0775b6596f7e1932f2ff)。

PCLKB 分频器（Divider）。

<a id="r_ga38799ae63c6aef7b8f637826fe5de9fd"></a>

```c
#define RA_CGC_DIV_PCLKC(n)
```

相关声明：[RA_CGC_DIV_PCLKC](#ga38799ae63c6aef7b8f637826fe5de9fd)。

PCLKC 分频器（Divider）。

<a id="r_ga775ccb80b8d68022e8e4a3e93f2d347c"></a>

```c
#define RA_CGC_DIV_PCLKD(n)
```

相关声明：[RA_CGC_DIV_PCLKD](#ga775ccb80b8d68022e8e4a3e93f2d347c)。

PCLKD 分频器（Divider）。

<a id="r_gaa8cde7ee7535ddd404a05ae72f598b28"></a>

```c
#define RA_CGC_DIV_PCLKE(n)
```

相关声明：[RA_CGC_DIV_PCLKE](#gaa8cde7ee7535ddd404a05ae72f598b28)。

PCLKE 分频器（Divider）。

<a id="r_ga0f6bd3b07d9c1c4e07daa28443c8148e"></a>

```c
#define RA_CGC_DIV_PLL(n)
```

相关声明：[RA_CGC_DIV_PLL](#ga0f6bd3b07d9c1c4e07daa28443c8148e)。

PLL 分频器（Divider）。

<a id="r_gaa5fd2b712624e2c73aac2574a5ea6512"></a>

```c
#define RA_CGC_DIV_PLLP(n)
```

相关声明：[RA_CGC_DIV_PLLP](#gaa5fd2b712624e2c73aac2574a5ea6512)。

PLLP 分频器（Divider）。

<a id="r_ga255f1f50393cf7f3396e1890b7728f49"></a>

```c
#define RA_CGC_DIV_PLLQ(n)
```

相关声明：[RA_CGC_DIV_PLLQ](#ga255f1f50393cf7f3396e1890b7728f49)。

PLLQ 分频器（Divider）。

<a id="r_gab1ea3ce0335620c286430c0af2de0b89"></a>

```c
#define RA_CGC_DIV_PLLR(n)
```

相关声明：[RA_CGC_DIV_PLLR](#gab1ea3ce0335620c286430c0af2de0b89)。

PLLR 分频器（Divider）。

<a id="r_gace4275eba4a646416ef6e0ffad3efafb"></a>

```c
#define RA_CGC_DIV_PLL2(n)
```

相关声明：[RA_CGC_DIV_PLL2](#gace4275eba4a646416ef6e0ffad3efafb)。

PLL2 分频器（Divider）。

<a id="r_ga11dbb86891568e5f75f9666107aac1bc"></a>

```c
#define RA_CGC_DIV_PLL2P(n)
```

相关声明：[RA_CGC_DIV_PLL2P](#ga11dbb86891568e5f75f9666107aac1bc)。

PLL2P 分频器（Divider）。

<a id="r_ga1dc330555e762496bb90f9d623c6bbfb"></a>

```c
#define RA_CGC_DIV_PLL2Q(n)
```

相关声明：[RA_CGC_DIV_PLL2Q](#ga1dc330555e762496bb90f9d623c6bbfb)。

PLL2Q 分频器（Divider）。

<a id="r_ga9e61fda937cc02e1484c64c0dbeb6dd5"></a>

```c
#define RA_CGC_DIV_PLL2R(n)
```

相关声明：[RA_CGC_DIV_PLL2R](#ga9e61fda937cc02e1484c64c0dbeb6dd5)。

PLL2R 分频器（Divider）。

<a id="r_gaf20a6aa81df58686419d3163430aa59f"></a>

```c
#define RA_CGC_DIV_SCICLK(n)
```

相关声明：[RA_CGC_DIV_SCICLK](#gaf20a6aa81df58686419d3163430aa59f)。

SCICLK 分频器（Divider）。

<a id="r_ga28b424f22f72071af6fbe8351ad72101"></a>

```c
#define RA_CGC_DIV_SPICLK(n)
```

相关声明：[RA_CGC_DIV_SPICLK](#ga28b424f22f72071af6fbe8351ad72101)。

SPICLK 分频器（Divider）。

<a id="r_ga944584d8d7372fad12f8e13bab00e7ae"></a>

```c
#define RA_CGC_DIV_U60CLK(n)
```

相关声明：[RA_CGC_DIV_U60CLK](#ga944584d8d7372fad12f8e13bab00e7ae)。

U60CLK 分频器（Divider）。

<a id="r_ga90a5ab20631fff89d39980a144ec2ea0"></a>

```c
#define RA_CGC_DIV_UCLK(n)
```

相关声明：[RA_CGC_DIV_UCLK](#ga90a5ab20631fff89d39980a144ec2ea0)。

UCLK 分频器（Divider）。

<a id="r_ga602dbf5f7d734c7cb202fb88f92aadc7"></a>

```c
#define RA_CGC_DIV_SCISPICLK(n)
```

相关声明：[RA_CGC_DIV_SCISPICLK](#ga602dbf5f7d734c7cb202fb88f92aadc7)。

SCISPI 分频器（Divider）。

<a id="r_gaa4b71829a1a84d1d80b4056fa138384a"></a>

```c
#define RA_CGC_DIV_GPTCLK(n)
```

相关声明：[RA_CGC_DIV_GPTCLK](#gaa4b71829a1a84d1d80b4056fa138384a)。

GPTCLK 分频器（Divider）。

<a id="r_ga192f3830fa2ca7e21999a09a49d5aa91"></a>

```c
#define RA_CGC_DIV_IICCLK(n)
```

相关声明：[RA_CGC_DIV_IICCLK](#ga192f3830fa2ca7e21999a09a49d5aa91)。

IICCLK 分频器（Divider）。

<a id="r_gae079778c09cf9b2cb94a797cc7c7c2c2"></a>

```c
#define RA_CGC_DIV_ADCCLK(n)
```

相关声明：[RA_CGC_DIV_ADCCLK](#gae079778c09cf9b2cb94a797cc7c7c2c2)。

ADCCLK 分频器（Divider）。

<a id="r_gacf26a8ec3df98acf72563383e4d11a32"></a>

```c
#define RA_CGC_DIV_MRICLK(n)
```

相关声明：[RA_CGC_DIV_MRICLK](#gacf26a8ec3df98acf72563383e4d11a32)。

MRICLK 分频器（Divider）。

<a id="r_ga86ba99da1338772f789e8f9f3d584b57"></a>

```c
#define RA_CGC_DIV_NPUCLK(n)
```

相关声明：[RA_CGC_DIV_NPUCLK](#ga86ba99da1338772f789e8f9f3d584b57)。

NPUCLK 分频器（Divider）。

<a id="r_ga9accde0e281cef734b4755708f1c6cb6"></a>

```c
#define RA_CGC_DIV_BCLKA(n)
```

相关声明：[RA_CGC_DIV_BCLKA](#ga9accde0e281cef734b4755708f1c6cb6)。

BCLKA 分频器（Divider）。

<a id="r_ga2894aade41c703b8ec1c947809bec49c"></a>

```c
#define RA_CGC_DIV_ESWCLK(n)
```

相关声明：[RA_CGC_DIV_ESWCLK](#ga2894aade41c703b8ec1c947809bec49c)。

ESWCLK 分频器（Divider）。

<a id="r_ga91bbe885dbe96bf64327cd3df85d0cd0"></a>

```c
#define RA_CGC_DIV_ESWPHYCLK(n)
```

相关声明：[RA_CGC_DIV_ESWPHYCLK](#ga91bbe885dbe96bf64327cd3df85d0cd0)。

ESWPHYCLK 分频器（Divider）。

<a id="r_ga2197a3da41a74b99404fbe665644f3b5"></a>

```c
#define RA_CGC_DIV_ETHPHYCLK(n)
```

相关声明：[RA_CGC_DIV_ETHPHYCLK](#ga2197a3da41a74b99404fbe665644f3b5)。

ETHPHY 分频器（Divider）。

<a id="r_ga8db2d1551894c727a5104b0e075a2eff"></a>

```c
#define RA_CGC_DIV_ESCCLK(n)
```

相关声明：[RA_CGC_DIV_ESCCLK](#ga8db2d1551894c727a5104b0e075a2eff)。

ESCCLK 分频器（Divider）。

<a id="r_gac479a6ad6cb28be1843e9021943cd6f1"></a>

```c
#define RA_CGC_DIV_DSMIFCLK(n)
```

相关声明：[RA_CGC_DIV_DSMIFCLK](#gac479a6ad6cb28be1843e9021943cd6f1)。

DSMIFCLK 分频器（Divider）。

<a id="r_ga259a31fc288b1a8b7c8e0747afefabb8"></a>

```c
#define RA_CGC_DIV_XTALDIV_CLK(n)
```

相关声明：[RA_CGC_DIV_XTALDIV_CLK](#ga259a31fc288b1a8b7c8e0747afefabb8)。

XTALDIV_CLK 分频器（Divider）。

<a id="r_ga300a739f16f545beb56683001057530c"></a>

```c
#define RA_CGC_DIV_HOCODIV_CLK(n)
```

相关声明：[RA_CGC_DIV_HOCODIV_CLK](#ga300a739f16f545beb56683001057530c)。

HOCODIV_CLK 分频器（Divider）。

<a id="r_ga190f2ab8379eb5e75124d3bbbdc53e16"></a>

```c
#define RA_CGC_DIV_MOCODIV_CLK(n)
```

相关声明：[RA_CGC_DIV_MOCODIV_CLK](#ga190f2ab8379eb5e75124d3bbbdc53e16)。

MOCODIV_CLK 分频器（Divider）。

<a id="r_ga8c8e5f9e5b7ec9e9ef286dd3f612fa65"></a>

```c
#define RA_CGC_DIV_SAU_CK00(n)
```

相关声明：[RA_CGC_DIV_SAU_CK00](#ga8c8e5f9e5b7ec9e9ef286dd3f612fa65)。

SAU_CK00 分频器（Divider）。

<a id="r_ga7e85115ada319f740aff0d4fe20ad52f"></a>

```c
#define RA_CGC_DIV_SAU_CK01(n)
```

相关声明：[RA_CGC_DIV_SAU_CK01](#ga7e85115ada319f740aff0d4fe20ad52f)。

SAU_CK01 分频器（Divider）。

<a id="r_ga35cb6e55a71bfd7298f77101260114a0"></a>

```c
#define RA_CGC_DIV_SAU_CK10(n)
```

相关声明：[RA_CGC_DIV_SAU_CK10](#ga35cb6e55a71bfd7298f77101260114a0)。

SAU_CK10 分频器（Divider）。

<a id="r_ga066b916171efb57e73f6ce1a955204fa"></a>

```c
#define RA_CGC_DIV_SAU_CK11(n)
```

相关声明：[RA_CGC_DIV_SAU_CK11](#ga066b916171efb57e73f6ce1a955204fa)。

SAU_CK11 分频器（Divider）。

<a id="r_ga1cfc8d2b14bff3e747bd2d0d5c8c600b"></a>

```c
#define RA_CGC_DIV_TAU_CK01(n)
```

相关声明：[RA_CGC_DIV_TAU_CK01](#ga1cfc8d2b14bff3e747bd2d0d5c8c600b)。

TAU_CK01 分频器（Divider）。

<a id="r_ga665dd9cac9446a549960b07b40b739a0"></a>

```c
#define RA_CGC_DIV_TAU_CK02(n)
```

相关声明：[RA_CGC_DIV_TAU_CK02](#ga665dd9cac9446a549960b07b40b739a0)。

TAU_CK02 分频器（Divider）。

<a id="r_gace75be507e1d26345d8e9eb85c2d1a6a"></a>

```c
#define RA_CGC_DIV_TAU_CK03(n)
```

相关声明：[RA_CGC_DIV_TAU_CK03](#gace75be507e1d26345d8e9eb85c2d1a6a)。

TAU_CK03 分频器（Divider）。

<a id="r_ga5e8e48984f6be7ae8fca08667a2dfd87"></a>

```c
#define RA_CGC_DIV_TAU_CK04(n)
```

相关声明：[RA_CGC_DIV_TAU_CK04](#ga5e8e48984f6be7ae8fca08667a2dfd87)。

TAU_CK04 分频器（Divider）。

## 7.2\_详细说明（Detailed Documentation）

<a id="gae079778c09cf9b2cb94a797cc7c7c2c2"></a>

### `RA_CGC_DIV_ADCCLK`

```c
#define RA_CGC_DIV_ADCCLK ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_ADC_CLOCK_DIV_, n)
```

ADCCLK 分频器（Divider）。

<a id="gac836d0409da1193de27a8c61510d06c5"></a>

### `RA_CGC_DIV_BCLK`

```c
#define RA_CGC_DIV_BCLK ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
```

BCLK 分频器（Divider）。

<a id="ga9accde0e281cef734b4755708f1c6cb6"></a>

### `RA_CGC_DIV_BCLKA`

```c
#define RA_CGC_DIV_BCLKA ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_BCLKA_CLOCK_DIV_, n)
```

BCLKA 分频器（Divider）。

<a id="gaa6e8ba963160224076dacac43db705d7"></a>

### `RA_CGC_DIV_CANFDCLK`

```c
#define RA_CGC_DIV_CANFDCLK ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_CANFD_CLOCK_DIV_, n)
```

CANFD 分频器（Divider）。

<a id="gaae1620e152c33e3d4a95b5cac0cb1c76"></a>

### `RA_CGC_DIV_CECCLK`

```c
#define RA_CGC_DIV_CECCLK ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_CEC_CLOCK_DIV_, n)
```

CEC 分频器（Divider）。

<a id="ga8b169aba21f7e00cb80ffa0229cf0ca7"></a>

### `RA_CGC_DIV_CLKOUT`

```c
#define RA_CGC_DIV_CLKOUT ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_CLKOUT_DIV_, n)
```

CLKOUT 分频器（Divider）。

<a id="gabf6b0bc9229f7b9b667662d5e7287af3"></a>

### `RA_CGC_DIV_CPUCLK`

```c
#define RA_CGC_DIV_CPUCLK ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
```

CPUCLK 分频器（Divider）。

<a id="ga5d01387282e98e3c1836cc18098726ec"></a>

### `RA_CGC_DIV_CPUCLK0`

```c
#define RA_CGC_DIV_CPUCLK0 ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
```

CPUCLK0 分频器（Divider）。

<a id="ga04c6195e596c187ec77ed5ebc8cd735b"></a>

### `RA_CGC_DIV_CPUCLK1`

```c
#define RA_CGC_DIV_CPUCLK1 ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
```

CPUCLK1 分频器（Divider）。

<a id="gac479a6ad6cb28be1843e9021943cd6f1"></a>

### `RA_CGC_DIV_DSMIFCLK`

```c
#define RA_CGC_DIV_DSMIFCLK ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_DSMIF_CLOCK_DIV_, n)
```

DSMIFCLK 分频器（Divider）。

<a id="ga8db2d1551894c727a5104b0e075a2eff"></a>

### `RA_CGC_DIV_ESCCLK`

```c
#define RA_CGC_DIV_ESCCLK ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_ESC_CLOCK_DIV_, n)
```

ESCCLK 分频器（Divider）。

<a id="ga2894aade41c703b8ec1c947809bec49c"></a>

### `RA_CGC_DIV_ESWCLK`

```c
#define RA_CGC_DIV_ESWCLK ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_ESW_CLOCK_DIV_, n)
```

ESWCLK 分频器（Divider）。

<a id="ga91bbe885dbe96bf64327cd3df85d0cd0"></a>

### `RA_CGC_DIV_ESWPHYCLK`

```c
#define RA_CGC_DIV_ESWPHYCLK ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_ESWPHY_CLOCK_DIV_, n)
```

ESWPHYCLK 分频器（Divider）。

<a id="ga2197a3da41a74b99404fbe665644f3b5"></a>

### `RA_CGC_DIV_ETHPHYCLK`

```c
#define RA_CGC_DIV_ETHPHYCLK ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_ETHPHY_CLOCK_DIV_, n)
```

ETHPHY 分频器（Divider）。

<a id="ga8006ac020337b43c9039290de93b237c"></a>

### `RA_CGC_DIV_FCLK`

```c
#define RA_CGC_DIV_FCLK ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
```

FCLK 分频器（Divider）。

<a id="gaa4b71829a1a84d1d80b4056fa138384a"></a>

### `RA_CGC_DIV_GPTCLK`

```c
#define RA_CGC_DIV_GPTCLK ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_GPT_CLOCK_DIV_, n)
```

GPTCLK 分频器（Divider）。

<a id="ga300a739f16f545beb56683001057530c"></a>

### `RA_CGC_DIV_HOCODIV_CLK`

```c
#define RA_CGC_DIV_HOCODIV_CLK ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
```

HOCODIV_CLK 分频器（Divider）。

<a id="gae414f33fc622f1eea25ed38b4e48b284"></a>

### `RA_CGC_DIV_I3CCLK`

```c
#define RA_CGC_DIV_I3CCLK ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_I3C_CLOCK_DIV_, n)
```

I3C 分频器（Divider）。

<a id="ga152905c07ac6744e4dbcaa88cc44b7b0"></a>

### `RA_CGC_DIV_ICLK`

```c
#define RA_CGC_DIV_ICLK ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
```

ICLK 分频器（Divider）。

<a id="ga192f3830fa2ca7e21999a09a49d5aa91"></a>

### `RA_CGC_DIV_IICCLK`

```c
#define RA_CGC_DIV_IICCLK ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_IIC_CLOCK_DIV_, n)
```

IICCLK 分频器（Divider）。

<a id="gade972ca4dc22a1438ae0ee8a7f0b1c86"></a>

### `RA_CGC_DIV_LCDCLK`

```c
#define RA_CGC_DIV_LCDCLK ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_LCD_CLOCK_DIV_, n)
```

LCDCLK 分频器（Divider）。

<a id="ga190f2ab8379eb5e75124d3bbbdc53e16"></a>

### `RA_CGC_DIV_MOCODIV_CLK`

```c
#define RA_CGC_DIV_MOCODIV_CLK ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
```

MOCODIV_CLK 分频器（Divider）。

<a id="gacf26a8ec3df98acf72563383e4d11a32"></a>

### `RA_CGC_DIV_MRICLK`

```c
#define RA_CGC_DIV_MRICLK ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
```

MRICLK 分频器（Divider）。

<a id="gaa38d17ba1d228ca66ef1f21720bc05b4"></a>

### `RA_CGC_DIV_MRPCLK`

```c
#define RA_CGC_DIV_MRPCLK ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
```

MRPCLK 分频器（Divider）。

<a id="ga86ba99da1338772f789e8f9f3d584b57"></a>

### `RA_CGC_DIV_NPUCLK`

```c
#define RA_CGC_DIV_NPUCLK ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
```

NPUCLK 分频器（Divider）。

<a id="ga6e21efeff2e4b079ba56bf33524517d5"></a>

### `RA_CGC_DIV_OCTASPICLK`

```c
#define RA_CGC_DIV_OCTASPICLK ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_OCTA_CLOCK_DIV_, n)
```

OCTASPI 分频器（Divider）。

<a id="ga40a2d9224061ee4b25e98407ee60eecc"></a>

### `RA_CGC_DIV_PCLKA`

```c
#define RA_CGC_DIV_PCLKA ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
```

PCLKA 分频器（Divider）。

<a id="gad3881c28b08b0775b6596f7e1932f2ff"></a>

### `RA_CGC_DIV_PCLKB`

```c
#define RA_CGC_DIV_PCLKB ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
```

PCLKB 分频器（Divider）。

<a id="ga38799ae63c6aef7b8f637826fe5de9fd"></a>

### `RA_CGC_DIV_PCLKC`

```c
#define RA_CGC_DIV_PCLKC ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
```

PCLKC 分频器（Divider）。

<a id="ga775ccb80b8d68022e8e4a3e93f2d347c"></a>

### `RA_CGC_DIV_PCLKD`

```c
#define RA_CGC_DIV_PCLKD ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
```

PCLKD 分频器（Divider）。

<a id="gaa8cde7ee7535ddd404a05ae72f598b28"></a>

### `RA_CGC_DIV_PCLKE`

```c
#define RA_CGC_DIV_PCLKE ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
```

PCLKE 分频器（Divider）。

<a id="ga0f6bd3b07d9c1c4e07daa28443c8148e"></a>

### `RA_CGC_DIV_PLL`

```c
#define RA_CGC_DIV_PLL ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_PLL_DIV_, n)
```

PLL 分频器（Divider）。

<a id="gace4275eba4a646416ef6e0ffad3efafb"></a>

### `RA_CGC_DIV_PLL2`

```c
#define RA_CGC_DIV_PLL2 ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_PLL_DIV_, n)
```

PLL2 分频器（Divider）。

<a id="ga11dbb86891568e5f75f9666107aac1bc"></a>

### `RA_CGC_DIV_PLL2P`

```c
#define RA_CGC_DIV_PLL2P ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_PLL_DIV_, n)
```

PLL2P 分频器（Divider）。

<a id="ga1dc330555e762496bb90f9d623c6bbfb"></a>

### `RA_CGC_DIV_PLL2Q`

```c
#define RA_CGC_DIV_PLL2Q ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_PLL_DIV_, n)
```

PLL2Q 分频器（Divider）。

<a id="ga9e61fda937cc02e1484c64c0dbeb6dd5"></a>

### `RA_CGC_DIV_PLL2R`

```c
#define RA_CGC_DIV_PLL2R ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_PLL_DIV_, n)
```

PLL2R 分频器（Divider）。

<a id="gaa5fd2b712624e2c73aac2574a5ea6512"></a>

### `RA_CGC_DIV_PLLP`

```c
#define RA_CGC_DIV_PLLP ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_PLL_DIV_, n)
```

PLLP 分频器（Divider）。

<a id="ga255f1f50393cf7f3396e1890b7728f49"></a>

### `RA_CGC_DIV_PLLQ`

```c
#define RA_CGC_DIV_PLLQ ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_PLL_DIV_, n)
```

PLLQ 分频器（Divider）。

<a id="gab1ea3ce0335620c286430c0af2de0b89"></a>

### `RA_CGC_DIV_PLLR`

```c
#define RA_CGC_DIV_PLLR ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_PLL_DIV_, n)
```

PLLR 分频器（Divider）。

<a id="ga8c8e5f9e5b7ec9e9ef286dd3f612fa65"></a>

### `RA_CGC_DIV_SAU_CK00`

```c
#define RA_CGC_DIV_SAU_CK00 ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_SAU_CLOCK_DIV_, n)
```

SAU_CK00 分频器（Divider）。

<a id="ga7e85115ada319f740aff0d4fe20ad52f"></a>

### `RA_CGC_DIV_SAU_CK01`

```c
#define RA_CGC_DIV_SAU_CK01 ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_SAU_CLOCK_DIV_, n)
```

SAU_CK01 分频器（Divider）。

<a id="ga35cb6e55a71bfd7298f77101260114a0"></a>

### `RA_CGC_DIV_SAU_CK10`

```c
#define RA_CGC_DIV_SAU_CK10 ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_SAU_CLOCK_DIV_, n)
```

SAU_CK10 分频器（Divider）。

<a id="ga066b916171efb57e73f6ce1a955204fa"></a>

### `RA_CGC_DIV_SAU_CK11`

```c
#define RA_CGC_DIV_SAU_CK11 ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_SAU_CLOCK_DIV_, n)
```

SAU_CK11 分频器（Divider）。

<a id="gaf20a6aa81df58686419d3163430aa59f"></a>

### `RA_CGC_DIV_SCICLK`

```c
#define RA_CGC_DIV_SCICLK ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_SCI_CLOCK_DIV_, n)
```

SCICLK 分频器（Divider）。

<a id="ga602dbf5f7d734c7cb202fb88f92aadc7"></a>

### `RA_CGC_DIV_SCISPICLK`

```c
#define RA_CGC_DIV_SCISPICLK ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_SCISPI_CLOCK_DIV_, n)
```

SCISPI 分频器（Divider）。

<a id="ga28b424f22f72071af6fbe8351ad72101"></a>

### `RA_CGC_DIV_SPICLK`

```c
#define RA_CGC_DIV_SPICLK ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_SPI_CLOCK_DIV_, n)
```

SPICLK 分频器（Divider）。

<a id="ga1cfc8d2b14bff3e747bd2d0d5c8c600b"></a>

### `RA_CGC_DIV_TAU_CK01`

```c
#define RA_CGC_DIV_TAU_CK01 ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(TIMER_SOURCE_DIV_, n)
```

TAU_CK01 分频器（Divider）。

<a id="ga665dd9cac9446a549960b07b40b739a0"></a>

### `RA_CGC_DIV_TAU_CK02`

```c
#define RA_CGC_DIV_TAU_CK02 ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(TIMER_SOURCE_DIV_, n)
```

TAU_CK02 分频器（Divider）。

<a id="gace75be507e1d26345d8e9eb85c2d1a6a"></a>

### `RA_CGC_DIV_TAU_CK03`

```c
#define RA_CGC_DIV_TAU_CK03 ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(TIMER_SOURCE_DIV_, n)
```

TAU_CK03 分频器（Divider）。

<a id="ga5e8e48984f6be7ae8fca08667a2dfd87"></a>

### `RA_CGC_DIV_TAU_CK04`

```c
#define RA_CGC_DIV_TAU_CK04 ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(TIMER_SOURCE_DIV_, n)
```

TAU_CK04 分频器（Divider）。

<a id="ga944584d8d7372fad12f8e13bab00e7ae"></a>

### `RA_CGC_DIV_U60CLK`

```c
#define RA_CGC_DIV_U60CLK ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_USB60_CLOCK_DIV_, n)
```

U60CLK 分频器（Divider）。

<a id="ga90a5ab20631fff89d39980a144ec2ea0"></a>

### `RA_CGC_DIV_UCLK`

```c
#define RA_CGC_DIV_UCLK ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_USB_CLOCK_DIV_, n)
```

UCLK 分频器（Divider）。

<a id="ga259a31fc288b1a8b7c8e0747afefabb8"></a>

### `RA_CGC_DIV_XTALDIV_CLK`

```c
#define RA_CGC_DIV_XTALDIV_CLK ( n)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
```

XTALDIV_CLK 分频器（Divider）。


## 7.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/renesas_ra_cgc.h](../api_file_usb_network_reference/P011_zephyr__drivers__clock_control__renesas_ra_cgc.h_文件参考.md)
- [UTIL_CAT](../util_reference/P006_内部宏工具头文件参考.md#a7e7766e792d1638bfbbc9d0f328d3d0d)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="autil__internal_8h_html_a7e7766e792d1638bfbbc9d0f328d3d0d"></a>

---

[上一章](P006_健康故障（Health Faults）。.md) · [返回大纲](大纲.md) · [下一章](P008_ESP32 Wi-Fi 网状网络（Wi-Fi Mesh）.md)
