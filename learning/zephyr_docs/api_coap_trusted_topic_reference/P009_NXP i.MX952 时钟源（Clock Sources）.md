---
id: learning.zephyr-docs.api-coap-trusted-topic-reference.page-9
title: NXP i.MX952 时钟源（Clock Sources）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__clock__sources.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_NXP i.MX952 时钟源（Clock Sources）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__clock__sources.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

i.MX952 SoC 的根时钟源（Root clock sources）。

<a id="details"></a>

i.MX952 SoC 的根时钟源（Root clock sources）。

<a id="header-groups"></a>
<a id="groups"></a>

## 9.1\_主题（Topics）

<a id="r_imx952_5Fperipheral_5Fclocks"></a>

相关声明：[外设时钟（Peripheral Clocks），编号 41–163](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html)。

基于 MIMX9529 `fsl_clock.h` 的外设时钟定义。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.2\_宏定义（Macros）

<a id="r_gaf6037059e31f2eee0505c05fd73a32e0"></a>

```c
#define IMX952_CLK_EXT 0
```

相关声明：[IMX952_CLK_EXT](#gaf6037059e31f2eee0505c05fd73a32e0)。

外部时钟源（External Clock Source）。

<a id="r_ga6a0a68d908a84c4a93edf0c9981445ae"></a>

```c
#define IMX952_CLK_32K 1
```

相关声明：[IMX952_CLK_32K](#ga6a0a68d908a84c4a93edf0c9981445ae)。

32 kHz 时钟源（Clock Source）。

<a id="r_ga56d5ac81125d5666e24c7f59de010bb7"></a>

```c
#define IMX952_CLK_24M 2
```

相关声明：[IMX952_CLK_24M](#ga56d5ac81125d5666e24c7f59de010bb7)。

24 MHz 时钟源（Clock Source）。

<a id="r_ga67e879f454af3931cae68730e99301b1"></a>

```c
#define IMX952_CLK_FRO 3
```

相关声明：[IMX952_CLK_FRO](#ga67e879f454af3931cae68730e99301b1)。

自由运行振荡器时钟（Free-running Oscillator Clock）。

<a id="r_gacd648fefd08ae73e3923413835c416c6"></a>

```c
#define IMX952_CLK_SYSPLL1_VCO 4
```

相关声明：[IMX952_CLK_SYSPLL1_VCO](#gacd648fefd08ae73e3923413835c416c6)。

系统 PLL1（System PLL1） 压控振荡器（VCO）。

<a id="r_ga1ebae6761620d16a0a4b09a727d4657c"></a>

```c
#define IMX952_CLK_SYSPLL1_PFD0_UNGATED 5
```

相关声明：[IMX952_CLK_SYSPLL1_PFD0_UNGATED](#ga1ebae6761620d16a0a4b09a727d4657c)。

系统 PLL1（System PLL1） PFD0，未门控（Ungated）。

<a id="r_gab12511de8338393da87eb0cbf5164f20"></a>

```c
#define IMX952_CLK_SYSPLL1_PFD0 6
```

相关声明：[IMX952_CLK_SYSPLL1_PFD0](#gab12511de8338393da87eb0cbf5164f20)。

系统 PLL1（System PLL1） PFD0。

<a id="r_ga9cb16f591e68a767fcabc96f542a8266"></a>

```c
#define IMX952_CLK_SYSPLL1_PFD0_DIV2 7
```

相关声明：[IMX952_CLK_SYSPLL1_PFD0_DIV2](#ga9cb16f591e68a767fcabc96f542a8266)。

系统 PLL1（System PLL1） PFD0，2 分频（Divided by 2）。

<a id="r_ga186d814b34520d4bf89390618eb6a27a"></a>

```c
#define IMX952_CLK_SYSPLL1_PFD1_UNGATED 8
```

相关声明：[IMX952_CLK_SYSPLL1_PFD1_UNGATED](#ga186d814b34520d4bf89390618eb6a27a)。

系统 PLL1（System PLL1） PFD1，未门控（Ungated）。

<a id="r_gad3f665c2a498de5e6b8c4a6820f865ac"></a>

```c
#define IMX952_CLK_SYSPLL1_PFD1 9
```

相关声明：[IMX952_CLK_SYSPLL1_PFD1](#gad3f665c2a498de5e6b8c4a6820f865ac)。

系统 PLL1（System PLL1） PFD1。

<a id="r_ga84d02ee3a62f72a0c68a47e7dac9080c"></a>

```c
#define IMX952_CLK_SYSPLL1_PFD1_DIV2 10
```

相关声明：[IMX952_CLK_SYSPLL1_PFD1_DIV2](#ga84d02ee3a62f72a0c68a47e7dac9080c)。

系统 PLL1（System PLL1） PFD1，2 分频（Divided by 2）。

<a id="r_ga34175ac1a860b439816d52e49f8e2775"></a>

```c
#define IMX952_CLK_SYSPLL1_PFD2_UNGATED 11
```

相关声明：[IMX952_CLK_SYSPLL1_PFD2_UNGATED](#ga34175ac1a860b439816d52e49f8e2775)。

系统 PLL1（System PLL1） PFD2，未门控（Ungated）。

<a id="r_gade8ab32b729d75b9bad66609651f787c"></a>

```c
#define IMX952_CLK_SYSPLL1_PFD2 12
```

相关声明：[IMX952_CLK_SYSPLL1_PFD2](#gade8ab32b729d75b9bad66609651f787c)。

系统 PLL1（System PLL1） PFD2。

<a id="r_ga01c4fc3c9e7c4a4a6a4142b58cbd7f9f"></a>

```c
#define IMX952_CLK_SYSPLL1_PFD2_DIV2 13
```

相关声明：[IMX952_CLK_SYSPLL1_PFD2_DIV2](#ga01c4fc3c9e7c4a4a6a4142b58cbd7f9f)。

系统 PLL1（System PLL1） PFD2，2 分频（Divided by 2）。

<a id="r_ga542a45e1b3de20841ce7fea1389059b8"></a>

```c
#define IMX952_CLK_AUDIOPLL1_VCO 14
```

相关声明：[IMX952_CLK_AUDIOPLL1_VCO](#ga542a45e1b3de20841ce7fea1389059b8)。

音频 PLL1（Audio PLL1） 压控振荡器（VCO）。

<a id="r_gacf08c6f206a4e5c4cdc1de1d7baf352f"></a>

```c
#define IMX952_CLK_AUDIOPLL1 15
```

相关声明：[IMX952_CLK_AUDIOPLL1](#gacf08c6f206a4e5c4cdc1de1d7baf352f)。

音频 PLL1（Audio PLL1） 输出（Output）。

<a id="r_ga73dd94bba5f17a67cc2da01c99467002"></a>

```c
#define IMX952_CLK_AUDIOPLL2_VCO 16
```

相关声明：[IMX952_CLK_AUDIOPLL2_VCO](#ga73dd94bba5f17a67cc2da01c99467002)。

音频 PLL2（Audio PLL2） 压控振荡器（VCO）。

<a id="r_gad254dbac425c8abde24e624e5c7cbea8"></a>

```c
#define IMX952_CLK_AUDIOPLL2 17
```

相关声明：[IMX952_CLK_AUDIOPLL2](#gad254dbac425c8abde24e624e5c7cbea8)。

音频 PLL2（Audio PLL2） 输出（Output）。

<a id="r_gad4f4063de4dd7be35c2cbfbcf793a4ae"></a>

```c
#define IMX952_CLK_VIDEOPLL1_VCO 18
```

相关声明：[IMX952_CLK_VIDEOPLL1_VCO](#gad4f4063de4dd7be35c2cbfbcf793a4ae)。

视频 PLL1（Video PLL1） 压控振荡器（VCO）。

<a id="r_gab6665fdf4aae031f4df8001c92d114d5"></a>

```c
#define IMX952_CLK_VIDEOPLL1 19
```

相关声明：[IMX952_CLK_VIDEOPLL1](#gab6665fdf4aae031f4df8001c92d114d5)。

视频 PLL1（Video PLL1） 输出（Output）。

<a id="r_ga0b9ca70e5d4bdd12c7bb70e685e22869"></a>

```c
#define IMX952_CLK_SRC_RESERVED20 20
```

相关声明：[IMX952_CLK_SRC_RESERVED20](#ga0b9ca70e5d4bdd12c7bb70e685e22869)。

保留的源时钟（Reserved Source Clock）20。

<a id="r_gaba96133add3fa0476e75715cbe07b0b9"></a>

```c
#define IMX952_CLK_SYSPLL1_PFD3_UNGATED 21
```

相关声明：[IMX952_CLK_SYSPLL1_PFD3_UNGATED](#gaba96133add3fa0476e75715cbe07b0b9)。

系统 PLL1（System PLL1） PFD3，未门控（Ungated）。

<a id="r_gacbc5d6bc23e87545b805af3a74ada9be"></a>

```c
#define IMX952_CLK_SYSPLL1_PFD3 22
```

相关声明：[IMX952_CLK_SYSPLL1_PFD3](#gacbc5d6bc23e87545b805af3a74ada9be)。

系统 PLL1（System PLL1） PFD3。

<a id="r_gab7c7b531d6d2dd1dd0e96778c050eaf2"></a>

```c
#define IMX952_CLK_SYSPLL1_PFD3_DIV2 23
```

相关声明：[IMX952_CLK_SYSPLL1_PFD3_DIV2](#gab7c7b531d6d2dd1dd0e96778c050eaf2)。

系统 PLL1（System PLL1） PFD3，2 分频（Divided by 2）。

<a id="r_gaf17de78b0c59f399eec5faab0fe872c9"></a>

```c
#define IMX952_CLK_ARMPLL_VCO 24
```

相关声明：[IMX952_CLK_ARMPLL_VCO](#gaf17de78b0c59f399eec5faab0fe872c9)。

ARM PLL 压控振荡器（VCO）。

<a id="r_ga10e77fb38ce506eda46379865e46c784"></a>

```c
#define IMX952_CLK_ARMPLL_PFD0_UNGATED 25
```

相关声明：[IMX952_CLK_ARMPLL_PFD0_UNGATED](#ga10e77fb38ce506eda46379865e46c784)。

ARM PLL PFD0，未门控（Ungated）。

<a id="r_ga8c53d9cb1cde130305ad5fdbe2984eb3"></a>

```c
#define IMX952_CLK_ARMPLL_PFD0 26
```

相关声明：[IMX952_CLK_ARMPLL_PFD0](#ga8c53d9cb1cde130305ad5fdbe2984eb3)。

ARM PLL PFD0。

<a id="r_ga87480c6ce8b50db5b75c16d10f97c0cd"></a>

```c
#define IMX952_CLK_ARMPLL_PFD1_UNGATED 27
```

相关声明：[IMX952_CLK_ARMPLL_PFD1_UNGATED](#ga87480c6ce8b50db5b75c16d10f97c0cd)。

ARM PLL PFD1，未门控（Ungated）。

<a id="r_gaffaac3c31b37079c1f873c53583158e5"></a>

```c
#define IMX952_CLK_ARMPLL_PFD1 28
```

相关声明：[IMX952_CLK_ARMPLL_PFD1](#gaffaac3c31b37079c1f873c53583158e5)。

ARM PLL PFD1。

<a id="r_ga4896537b4d1948eb4155fef172984452"></a>

```c
#define IMX952_CLK_ARMPLL_PFD2_UNGATED 29
```

相关声明：[IMX952_CLK_ARMPLL_PFD2_UNGATED](#ga4896537b4d1948eb4155fef172984452)。

ARM PLL PFD2，未门控（Ungated）。

<a id="r_ga1d8c6d7c7b1485cf9c8a0919dede47a0"></a>

```c
#define IMX952_CLK_ARMPLL_PFD2 30
```

相关声明：[IMX952_CLK_ARMPLL_PFD2](#ga1d8c6d7c7b1485cf9c8a0919dede47a0)。

ARM PLL PFD2。

<a id="r_gae91ffcb10da54e26aab5c81bb908d322"></a>

```c
#define IMX952_CLK_ARMPLL_PFD3_UNGATED 31
```

相关声明：[IMX952_CLK_ARMPLL_PFD3_UNGATED](#gae91ffcb10da54e26aab5c81bb908d322)。

ARM PLL PFD3，未门控（Ungated）。

<a id="r_ga42e8f7465fd70ff8f9752297c836d3b9"></a>

```c
#define IMX952_CLK_ARMPLL_PFD3 32
```

相关声明：[IMX952_CLK_ARMPLL_PFD3](#ga42e8f7465fd70ff8f9752297c836d3b9)。

ARM PLL PFD3。

<a id="r_ga68beaaa7c75b9bed7ed6bf0c38620a2a"></a>

```c
#define IMX952_CLK_DRAMPLL_VCO 33
```

相关声明：[IMX952_CLK_DRAMPLL_VCO](#ga68beaaa7c75b9bed7ed6bf0c38620a2a)。

DRAM PLL 压控振荡器（VCO）。

<a id="r_gab843821fa6441f9edcb5be1b774383f7"></a>

```c
#define IMX952_CLK_DRAMPLL 34
```

相关声明：[IMX952_CLK_DRAMPLL](#gab843821fa6441f9edcb5be1b774383f7)。

DRAM PLL 输出（Output）。

<a id="r_gac23033e983a469be2d4e4f90a272ede2"></a>

```c
#define IMX952_CLK_HSIOPLL_VCO 35
```

相关声明：[IMX952_CLK_HSIOPLL_VCO](#gac23033e983a469be2d4e4f90a272ede2)。

HSIO PLL 压控振荡器（VCO）。

<a id="r_ga699f4715ec324b2d598c3dd87e5401f2"></a>

```c
#define IMX952_CLK_HSIOPLL 36
```

相关声明：[IMX952_CLK_HSIOPLL](#ga699f4715ec324b2d598c3dd87e5401f2)。

HSIO PLL 输出（Output）。

<a id="r_ga6dbecdd20f5073eedd6959b5251d995e"></a>

```c
#define IMX952_CLK_LDBPLL_VCO 37
```

相关声明：[IMX952_CLK_LDBPLL_VCO](#ga6dbecdd20f5073eedd6959b5251d995e)。

LDB PLL 压控振荡器（VCO）。

<a id="r_gaf6edfa1d415c823899837459813d0213"></a>

```c
#define IMX952_CLK_LDBPLL 38
```

相关声明：[IMX952_CLK_LDBPLL](#gaf6edfa1d415c823899837459813d0213)。

LDB PLL 输出（Output）。

<a id="r_gab5c7237c02398f2b58ac0231d5db059d"></a>

```c
#define IMX952_CLK_EXT1 39
```

相关声明：[IMX952_CLK_EXT1](#gab5c7237c02398f2b58ac0231d5db059d)。

外部时钟源（External Clock Source）1。

<a id="r_ga4fa9a6ba981ce6a53ece7ab5b9a19424"></a>

```c
#define IMX952_CLK_EXT2 40
```

相关声明：[IMX952_CLK_EXT2](#ga4fa9a6ba981ce6a53ece7ab5b9a19424)。

外部时钟源（External Clock Source）2。

## 9.3\_详细说明（Detailed Documentation）

<a id="ga56d5ac81125d5666e24c7f59de010bb7"></a>

### `IMX952_CLK_24M`

```c
#define IMX952_CLK_24M 2
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

24 MHz 时钟源（Clock Source）。

<a id="ga6a0a68d908a84c4a93edf0c9981445ae"></a>

### `IMX952_CLK_32K`

```c
#define IMX952_CLK_32K 1
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

32 kHz 时钟源（Clock Source）。

<a id="ga8c53d9cb1cde130305ad5fdbe2984eb3"></a>

### `IMX952_CLK_ARMPLL_PFD0`

```c
#define IMX952_CLK_ARMPLL_PFD0 26
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

ARM PLL PFD0。

<a id="ga10e77fb38ce506eda46379865e46c784"></a>

### `IMX952_CLK_ARMPLL_PFD0_UNGATED`

```c
#define IMX952_CLK_ARMPLL_PFD0_UNGATED 25
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

ARM PLL PFD0，未门控（Ungated）。

<a id="gaffaac3c31b37079c1f873c53583158e5"></a>

### `IMX952_CLK_ARMPLL_PFD1`

```c
#define IMX952_CLK_ARMPLL_PFD1 28
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

ARM PLL PFD1。

<a id="ga87480c6ce8b50db5b75c16d10f97c0cd"></a>

### `IMX952_CLK_ARMPLL_PFD1_UNGATED`

```c
#define IMX952_CLK_ARMPLL_PFD1_UNGATED 27
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

ARM PLL PFD1，未门控（Ungated）。

<a id="ga1d8c6d7c7b1485cf9c8a0919dede47a0"></a>

### `IMX952_CLK_ARMPLL_PFD2`

```c
#define IMX952_CLK_ARMPLL_PFD2 30
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

ARM PLL PFD2。

<a id="ga4896537b4d1948eb4155fef172984452"></a>

### `IMX952_CLK_ARMPLL_PFD2_UNGATED`

```c
#define IMX952_CLK_ARMPLL_PFD2_UNGATED 29
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

ARM PLL PFD2，未门控（Ungated）。

<a id="ga42e8f7465fd70ff8f9752297c836d3b9"></a>

### `IMX952_CLK_ARMPLL_PFD3`

```c
#define IMX952_CLK_ARMPLL_PFD3 32
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

ARM PLL PFD3。

<a id="gae91ffcb10da54e26aab5c81bb908d322"></a>

### `IMX952_CLK_ARMPLL_PFD3_UNGATED`

```c
#define IMX952_CLK_ARMPLL_PFD3_UNGATED 31
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

ARM PLL PFD3，未门控（Ungated）。

<a id="gaf17de78b0c59f399eec5faab0fe872c9"></a>

### `IMX952_CLK_ARMPLL_VCO`

```c
#define IMX952_CLK_ARMPLL_VCO 24
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

ARM PLL 压控振荡器（VCO）。

<a id="gacf08c6f206a4e5c4cdc1de1d7baf352f"></a>

### `IMX952_CLK_AUDIOPLL1`

```c
#define IMX952_CLK_AUDIOPLL1 15
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

音频 PLL1（Audio PLL1） 输出（Output）。

<a id="ga542a45e1b3de20841ce7fea1389059b8"></a>

### `IMX952_CLK_AUDIOPLL1_VCO`

```c
#define IMX952_CLK_AUDIOPLL1_VCO 14
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

音频 PLL1（Audio PLL1） 压控振荡器（VCO）。

<a id="gad254dbac425c8abde24e624e5c7cbea8"></a>

### `IMX952_CLK_AUDIOPLL2`

```c
#define IMX952_CLK_AUDIOPLL2 17
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

音频 PLL2（Audio PLL2） 输出（Output）。

<a id="ga73dd94bba5f17a67cc2da01c99467002"></a>

### `IMX952_CLK_AUDIOPLL2_VCO`

```c
#define IMX952_CLK_AUDIOPLL2_VCO 16
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

音频 PLL2（Audio PLL2） 压控振荡器（VCO）。

<a id="gab843821fa6441f9edcb5be1b774383f7"></a>

### `IMX952_CLK_DRAMPLL`

```c
#define IMX952_CLK_DRAMPLL 34
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

DRAM PLL 输出（Output）。

<a id="ga68beaaa7c75b9bed7ed6bf0c38620a2a"></a>

### `IMX952_CLK_DRAMPLL_VCO`

```c
#define IMX952_CLK_DRAMPLL_VCO 33
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

DRAM PLL 压控振荡器（VCO）。

<a id="gaf6037059e31f2eee0505c05fd73a32e0"></a>

### `IMX952_CLK_EXT`

```c
#define IMX952_CLK_EXT 0
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

外部时钟源（External Clock Source）。

<a id="gab5c7237c02398f2b58ac0231d5db059d"></a>

### `IMX952_CLK_EXT1`

```c
#define IMX952_CLK_EXT1 39
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

外部时钟源（External Clock Source）1。

<a id="ga4fa9a6ba981ce6a53ece7ab5b9a19424"></a>

### `IMX952_CLK_EXT2`

```c
#define IMX952_CLK_EXT2 40
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

外部时钟源（External Clock Source）2。

<a id="ga67e879f454af3931cae68730e99301b1"></a>

### `IMX952_CLK_FRO`

```c
#define IMX952_CLK_FRO 3
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

自由运行振荡器时钟（Free-running Oscillator Clock）。

<a id="ga699f4715ec324b2d598c3dd87e5401f2"></a>

### `IMX952_CLK_HSIOPLL`

```c
#define IMX952_CLK_HSIOPLL 36
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

HSIO PLL 输出（Output）。

<a id="gac23033e983a469be2d4e4f90a272ede2"></a>

### `IMX952_CLK_HSIOPLL_VCO`

```c
#define IMX952_CLK_HSIOPLL_VCO 35
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

HSIO PLL 压控振荡器（VCO）。

<a id="gaf6edfa1d415c823899837459813d0213"></a>

### `IMX952_CLK_LDBPLL`

```c
#define IMX952_CLK_LDBPLL 38
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

LDB PLL 输出（Output）。

<a id="ga6dbecdd20f5073eedd6959b5251d995e"></a>

### `IMX952_CLK_LDBPLL_VCO`

```c
#define IMX952_CLK_LDBPLL_VCO 37
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

LDB PLL 压控振荡器（VCO）。

<a id="ga0b9ca70e5d4bdd12c7bb70e685e22869"></a>

### `IMX952_CLK_SRC_RESERVED20`

```c
#define IMX952_CLK_SRC_RESERVED20 20
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

保留的源时钟（Reserved Source Clock）20。

<a id="gab12511de8338393da87eb0cbf5164f20"></a>

### `IMX952_CLK_SYSPLL1_PFD0`

```c
#define IMX952_CLK_SYSPLL1_PFD0 6
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

系统 PLL1（System PLL1） PFD0。

<a id="ga9cb16f591e68a767fcabc96f542a8266"></a>

### `IMX952_CLK_SYSPLL1_PFD0_DIV2`

```c
#define IMX952_CLK_SYSPLL1_PFD0_DIV2 7
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

系统 PLL1（System PLL1） PFD0，2 分频（Divided by 2）。

<a id="ga1ebae6761620d16a0a4b09a727d4657c"></a>

### `IMX952_CLK_SYSPLL1_PFD0_UNGATED`

```c
#define IMX952_CLK_SYSPLL1_PFD0_UNGATED 5
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

系统 PLL1（System PLL1） PFD0，未门控（Ungated）。

<a id="gad3f665c2a498de5e6b8c4a6820f865ac"></a>

### `IMX952_CLK_SYSPLL1_PFD1`

```c
#define IMX952_CLK_SYSPLL1_PFD1 9
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

系统 PLL1（System PLL1） PFD1。

<a id="ga84d02ee3a62f72a0c68a47e7dac9080c"></a>

### `IMX952_CLK_SYSPLL1_PFD1_DIV2`

```c
#define IMX952_CLK_SYSPLL1_PFD1_DIV2 10
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

系统 PLL1（System PLL1） PFD1，2 分频（Divided by 2）。

<a id="ga186d814b34520d4bf89390618eb6a27a"></a>

### `IMX952_CLK_SYSPLL1_PFD1_UNGATED`

```c
#define IMX952_CLK_SYSPLL1_PFD1_UNGATED 8
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

系统 PLL1（System PLL1） PFD1，未门控（Ungated）。

<a id="gade8ab32b729d75b9bad66609651f787c"></a>

### `IMX952_CLK_SYSPLL1_PFD2`

```c
#define IMX952_CLK_SYSPLL1_PFD2 12
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

系统 PLL1（System PLL1） PFD2。

<a id="ga01c4fc3c9e7c4a4a6a4142b58cbd7f9f"></a>

### `IMX952_CLK_SYSPLL1_PFD2_DIV2`

```c
#define IMX952_CLK_SYSPLL1_PFD2_DIV2 13
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

系统 PLL1（System PLL1） PFD2，2 分频（Divided by 2）。

<a id="ga34175ac1a860b439816d52e49f8e2775"></a>

### `IMX952_CLK_SYSPLL1_PFD2_UNGATED`

```c
#define IMX952_CLK_SYSPLL1_PFD2_UNGATED 11
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

系统 PLL1（System PLL1） PFD2，未门控（Ungated）。

<a id="gacbc5d6bc23e87545b805af3a74ada9be"></a>

### `IMX952_CLK_SYSPLL1_PFD3`

```c
#define IMX952_CLK_SYSPLL1_PFD3 22
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

系统 PLL1（System PLL1） PFD3。

<a id="gab7c7b531d6d2dd1dd0e96778c050eaf2"></a>

### `IMX952_CLK_SYSPLL1_PFD3_DIV2`

```c
#define IMX952_CLK_SYSPLL1_PFD3_DIV2 23
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

系统 PLL1（System PLL1） PFD3，2 分频（Divided by 2）。

<a id="gaba96133add3fa0476e75715cbe07b0b9"></a>

### `IMX952_CLK_SYSPLL1_PFD3_UNGATED`

```c
#define IMX952_CLK_SYSPLL1_PFD3_UNGATED 21
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

系统 PLL1（System PLL1） PFD3，未门控（Ungated）。

<a id="gacd648fefd08ae73e3923413835c416c6"></a>

### `IMX952_CLK_SYSPLL1_VCO`

```c
#define IMX952_CLK_SYSPLL1_VCO 4
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

系统 PLL1（System PLL1） 压控振荡器（VCO）。

<a id="gab6665fdf4aae031f4df8001c92d114d5"></a>

### `IMX952_CLK_VIDEOPLL1`

```c
#define IMX952_CLK_VIDEOPLL1 19
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

视频 PLL1（Video PLL1） 输出（Output）。

<a id="gad4f4063de4dd7be35c2cbfbcf793a4ae"></a>

### `IMX952_CLK_VIDEOPLL1_VCO`

```c
#define IMX952_CLK_VIDEOPLL1_VCO 18
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

视频 PLL1（Video PLL1） 压控振荡器（VCO）。


## 9.4\_原页交叉引用（Cross References）

- [外设时钟（Peripheral Clocks），编号 41–163](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html)
- [zephyr/dt-bindings/clock/imx952_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/imx952__clock_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P008_CoAP 服务 API.md) · [返回大纲](大纲.md) · [下一章](P010_传输管理（Transport management）.md)
