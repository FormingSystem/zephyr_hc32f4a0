---
id: learning.zephyr-docs.api-file-pic-clock-reference.page-1
title: zephyr__dt-bindings__clock__imx952_clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/imx952__clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_dt-bindings\_\_clock\_\_imx952\_clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/imx952__clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

NXP i.MX952片上系统（SoC）的时钟树定义。

查看此文件的源码。

<a id="details"></a>

NXP i.MX952片上系统（SoC）的时钟树定义。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.1\_宏定义（Macros）

<a id="r_gaf6037059e31f2eee0505c05fd73a32e0"></a>

```c
#define IMX952_CLK_EXT 0
```

相关声明：[IMX952_CLK_EXT](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gaf6037059e31f2eee0505c05fd73a32e0)。

外部时钟源（External Clock Source）。

<a id="r_ga6a0a68d908a84c4a93edf0c9981445ae"></a>

```c
#define IMX952_CLK_32K 1
```

相关声明：[IMX952_CLK_32K](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga6a0a68d908a84c4a93edf0c9981445ae)。

32 kHz 时钟源（Clock Source）。

<a id="r_ga56d5ac81125d5666e24c7f59de010bb7"></a>

```c
#define IMX952_CLK_24M 2
```

相关声明：[IMX952_CLK_24M](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga56d5ac81125d5666e24c7f59de010bb7)。

24 MHz 时钟源（Clock Source）。

<a id="r_ga67e879f454af3931cae68730e99301b1"></a>

```c
#define IMX952_CLK_FRO 3
```

相关声明：[IMX952_CLK_FRO](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga67e879f454af3931cae68730e99301b1)。

自由运行振荡器时钟（Free-running Oscillator Clock）。

<a id="r_gacd648fefd08ae73e3923413835c416c6"></a>

```c
#define IMX952_CLK_SYSPLL1_VCO 4
```

相关声明：[IMX952_CLK_SYSPLL1_VCO](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gacd648fefd08ae73e3923413835c416c6)。

系统 PLL1（System PLL1） 压控振荡器（VCO）。

<a id="r_ga1ebae6761620d16a0a4b09a727d4657c"></a>

```c
#define IMX952_CLK_SYSPLL1_PFD0_UNGATED 5
```

相关声明：[IMX952_CLK_SYSPLL1_PFD0_UNGATED](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga1ebae6761620d16a0a4b09a727d4657c)。

系统 PLL1（System PLL1） PFD0，未门控（Ungated）。

<a id="r_gab12511de8338393da87eb0cbf5164f20"></a>

```c
#define IMX952_CLK_SYSPLL1_PFD0 6
```

相关声明：[IMX952_CLK_SYSPLL1_PFD0](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gab12511de8338393da87eb0cbf5164f20)。

系统 PLL1（System PLL1） PFD0。

<a id="r_ga9cb16f591e68a767fcabc96f542a8266"></a>

```c
#define IMX952_CLK_SYSPLL1_PFD0_DIV2 7
```

相关声明：[IMX952_CLK_SYSPLL1_PFD0_DIV2](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga9cb16f591e68a767fcabc96f542a8266)。

系统 PLL1（System PLL1） PFD0，2 分频（Divided by 2）。

<a id="r_ga186d814b34520d4bf89390618eb6a27a"></a>

```c
#define IMX952_CLK_SYSPLL1_PFD1_UNGATED 8
```

相关声明：[IMX952_CLK_SYSPLL1_PFD1_UNGATED](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga186d814b34520d4bf89390618eb6a27a)。

系统 PLL1（System PLL1） PFD1，未门控（Ungated）。

<a id="r_gad3f665c2a498de5e6b8c4a6820f865ac"></a>

```c
#define IMX952_CLK_SYSPLL1_PFD1 9
```

相关声明：[IMX952_CLK_SYSPLL1_PFD1](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gad3f665c2a498de5e6b8c4a6820f865ac)。

系统 PLL1（System PLL1） PFD1。

<a id="r_ga84d02ee3a62f72a0c68a47e7dac9080c"></a>

```c
#define IMX952_CLK_SYSPLL1_PFD1_DIV2 10
```

相关声明：[IMX952_CLK_SYSPLL1_PFD1_DIV2](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga84d02ee3a62f72a0c68a47e7dac9080c)。

系统 PLL1（System PLL1） PFD1，2 分频（Divided by 2）。

<a id="r_ga34175ac1a860b439816d52e49f8e2775"></a>

```c
#define IMX952_CLK_SYSPLL1_PFD2_UNGATED 11
```

相关声明：[IMX952_CLK_SYSPLL1_PFD2_UNGATED](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga34175ac1a860b439816d52e49f8e2775)。

系统 PLL1（System PLL1） PFD2，未门控（Ungated）。

<a id="r_gade8ab32b729d75b9bad66609651f787c"></a>

```c
#define IMX952_CLK_SYSPLL1_PFD2 12
```

相关声明：[IMX952_CLK_SYSPLL1_PFD2](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gade8ab32b729d75b9bad66609651f787c)。

系统 PLL1（System PLL1） PFD2。

<a id="r_ga01c4fc3c9e7c4a4a6a4142b58cbd7f9f"></a>

```c
#define IMX952_CLK_SYSPLL1_PFD2_DIV2 13
```

相关声明：[IMX952_CLK_SYSPLL1_PFD2_DIV2](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga01c4fc3c9e7c4a4a6a4142b58cbd7f9f)。

系统 PLL1（System PLL1） PFD2，2 分频（Divided by 2）。

<a id="r_ga542a45e1b3de20841ce7fea1389059b8"></a>

```c
#define IMX952_CLK_AUDIOPLL1_VCO 14
```

相关声明：[IMX952_CLK_AUDIOPLL1_VCO](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga542a45e1b3de20841ce7fea1389059b8)。

音频 PLL1（Audio PLL1） 压控振荡器（VCO）。

<a id="r_gacf08c6f206a4e5c4cdc1de1d7baf352f"></a>

```c
#define IMX952_CLK_AUDIOPLL1 15
```

相关声明：[IMX952_CLK_AUDIOPLL1](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gacf08c6f206a4e5c4cdc1de1d7baf352f)。

音频 PLL1（Audio PLL1） 输出（Output）。

<a id="r_ga73dd94bba5f17a67cc2da01c99467002"></a>

```c
#define IMX952_CLK_AUDIOPLL2_VCO 16
```

相关声明：[IMX952_CLK_AUDIOPLL2_VCO](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga73dd94bba5f17a67cc2da01c99467002)。

音频 PLL2（Audio PLL2） 压控振荡器（VCO）。

<a id="r_gad254dbac425c8abde24e624e5c7cbea8"></a>

```c
#define IMX952_CLK_AUDIOPLL2 17
```

相关声明：[IMX952_CLK_AUDIOPLL2](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gad254dbac425c8abde24e624e5c7cbea8)。

音频 PLL2（Audio PLL2） 输出（Output）。

<a id="r_gad4f4063de4dd7be35c2cbfbcf793a4ae"></a>

```c
#define IMX952_CLK_VIDEOPLL1_VCO 18
```

相关声明：[IMX952_CLK_VIDEOPLL1_VCO](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gad4f4063de4dd7be35c2cbfbcf793a4ae)。

视频 PLL1（Video PLL1） 压控振荡器（VCO）。

<a id="r_gab6665fdf4aae031f4df8001c92d114d5"></a>

```c
#define IMX952_CLK_VIDEOPLL1 19
```

相关声明：[IMX952_CLK_VIDEOPLL1](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gab6665fdf4aae031f4df8001c92d114d5)。

视频 PLL1（Video PLL1） 输出（Output）。

<a id="r_ga0b9ca70e5d4bdd12c7bb70e685e22869"></a>

```c
#define IMX952_CLK_SRC_RESERVED20 20
```

相关声明：[IMX952_CLK_SRC_RESERVED20](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga0b9ca70e5d4bdd12c7bb70e685e22869)。

保留的源时钟（Reserved Source Clock）20。

<a id="r_gaba96133add3fa0476e75715cbe07b0b9"></a>

```c
#define IMX952_CLK_SYSPLL1_PFD3_UNGATED 21
```

相关声明：[IMX952_CLK_SYSPLL1_PFD3_UNGATED](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gaba96133add3fa0476e75715cbe07b0b9)。

系统 PLL1（System PLL1） PFD3，未门控（Ungated）。

<a id="r_gacbc5d6bc23e87545b805af3a74ada9be"></a>

```c
#define IMX952_CLK_SYSPLL1_PFD3 22
```

相关声明：[IMX952_CLK_SYSPLL1_PFD3](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gacbc5d6bc23e87545b805af3a74ada9be)。

系统 PLL1（System PLL1） PFD3。

<a id="r_gab7c7b531d6d2dd1dd0e96778c050eaf2"></a>

```c
#define IMX952_CLK_SYSPLL1_PFD3_DIV2 23
```

相关声明：[IMX952_CLK_SYSPLL1_PFD3_DIV2](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gab7c7b531d6d2dd1dd0e96778c050eaf2)。

系统 PLL1（System PLL1） PFD3，2 分频（Divided by 2）。

<a id="r_gaf17de78b0c59f399eec5faab0fe872c9"></a>

```c
#define IMX952_CLK_ARMPLL_VCO 24
```

相关声明：[IMX952_CLK_ARMPLL_VCO](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gaf17de78b0c59f399eec5faab0fe872c9)。

ARM PLL 压控振荡器（VCO）。

<a id="r_ga10e77fb38ce506eda46379865e46c784"></a>

```c
#define IMX952_CLK_ARMPLL_PFD0_UNGATED 25
```

相关声明：[IMX952_CLK_ARMPLL_PFD0_UNGATED](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga10e77fb38ce506eda46379865e46c784)。

ARM PLL PFD0，未门控（Ungated）。

<a id="r_ga8c53d9cb1cde130305ad5fdbe2984eb3"></a>

```c
#define IMX952_CLK_ARMPLL_PFD0 26
```

相关声明：[IMX952_CLK_ARMPLL_PFD0](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga8c53d9cb1cde130305ad5fdbe2984eb3)。

ARM PLL PFD0。

<a id="r_ga87480c6ce8b50db5b75c16d10f97c0cd"></a>

```c
#define IMX952_CLK_ARMPLL_PFD1_UNGATED 27
```

相关声明：[IMX952_CLK_ARMPLL_PFD1_UNGATED](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga87480c6ce8b50db5b75c16d10f97c0cd)。

ARM PLL PFD1，未门控（Ungated）。

<a id="r_gaffaac3c31b37079c1f873c53583158e5"></a>

```c
#define IMX952_CLK_ARMPLL_PFD1 28
```

相关声明：[IMX952_CLK_ARMPLL_PFD1](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gaffaac3c31b37079c1f873c53583158e5)。

ARM PLL PFD1。

<a id="r_ga4896537b4d1948eb4155fef172984452"></a>

```c
#define IMX952_CLK_ARMPLL_PFD2_UNGATED 29
```

相关声明：[IMX952_CLK_ARMPLL_PFD2_UNGATED](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga4896537b4d1948eb4155fef172984452)。

ARM PLL PFD2，未门控（Ungated）。

<a id="r_ga1d8c6d7c7b1485cf9c8a0919dede47a0"></a>

```c
#define IMX952_CLK_ARMPLL_PFD2 30
```

相关声明：[IMX952_CLK_ARMPLL_PFD2](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga1d8c6d7c7b1485cf9c8a0919dede47a0)。

ARM PLL PFD2。

<a id="r_gae91ffcb10da54e26aab5c81bb908d322"></a>

```c
#define IMX952_CLK_ARMPLL_PFD3_UNGATED 31
```

相关声明：[IMX952_CLK_ARMPLL_PFD3_UNGATED](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gae91ffcb10da54e26aab5c81bb908d322)。

ARM PLL PFD3，未门控（Ungated）。

<a id="r_ga42e8f7465fd70ff8f9752297c836d3b9"></a>

```c
#define IMX952_CLK_ARMPLL_PFD3 32
```

相关声明：[IMX952_CLK_ARMPLL_PFD3](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga42e8f7465fd70ff8f9752297c836d3b9)。

ARM PLL PFD3。

<a id="r_ga68beaaa7c75b9bed7ed6bf0c38620a2a"></a>

```c
#define IMX952_CLK_DRAMPLL_VCO 33
```

相关声明：[IMX952_CLK_DRAMPLL_VCO](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga68beaaa7c75b9bed7ed6bf0c38620a2a)。

DRAM PLL 压控振荡器（VCO）。

<a id="r_gab843821fa6441f9edcb5be1b774383f7"></a>

```c
#define IMX952_CLK_DRAMPLL 34
```

相关声明：[IMX952_CLK_DRAMPLL](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gab843821fa6441f9edcb5be1b774383f7)。

DRAM PLL 输出（Output）。

<a id="r_gac23033e983a469be2d4e4f90a272ede2"></a>

```c
#define IMX952_CLK_HSIOPLL_VCO 35
```

相关声明：[IMX952_CLK_HSIOPLL_VCO](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gac23033e983a469be2d4e4f90a272ede2)。

HSIO PLL 压控振荡器（VCO）。

<a id="r_ga699f4715ec324b2d598c3dd87e5401f2"></a>

```c
#define IMX952_CLK_HSIOPLL 36
```

相关声明：[IMX952_CLK_HSIOPLL](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga699f4715ec324b2d598c3dd87e5401f2)。

HSIO PLL 输出（Output）。

<a id="r_ga6dbecdd20f5073eedd6959b5251d995e"></a>

```c
#define IMX952_CLK_LDBPLL_VCO 37
```

相关声明：[IMX952_CLK_LDBPLL_VCO](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga6dbecdd20f5073eedd6959b5251d995e)。

LDB PLL 压控振荡器（VCO）。

<a id="r_gaf6edfa1d415c823899837459813d0213"></a>

```c
#define IMX952_CLK_LDBPLL 38
```

相关声明：[IMX952_CLK_LDBPLL](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gaf6edfa1d415c823899837459813d0213)。

LDB PLL 输出（Output）。

<a id="r_gab5c7237c02398f2b58ac0231d5db059d"></a>

```c
#define IMX952_CLK_EXT1 39
```

相关声明：[IMX952_CLK_EXT1](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gab5c7237c02398f2b58ac0231d5db059d)。

外部时钟源（External Clock Source）1。

<a id="r_ga4fa9a6ba981ce6a53ece7ab5b9a19424"></a>

```c
#define IMX952_CLK_EXT2 40
```

相关声明：[IMX952_CLK_EXT2](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga4fa9a6ba981ce6a53ece7ab5b9a19424)。

外部时钟源（External Clock Source）2。

<a id="r_a03330ea5d5d6cb6c5d0cbde5cc2bb8e6"></a>

```c
#define IMX952_CCM_NUM_CLK_SRC 41
```

相关声明：[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

时钟源（Clock Sources）的总数量。

<a id="r_gadd6d1896e8c854ea655c6149753054b2"></a>

```c
#define IMX952_CLK_ADC (IMX952_CCM_NUM_CLK_SRC + 0)
```

相关声明：[IMX952_CLK_ADC](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gadd6d1896e8c854ea655c6149753054b2)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

ADC 时钟（Clock）。

<a id="r_gabfebcfad721ae0c19c0fdab927890cc9"></a>

```c
#define IMX952_CLK_RESERVED1 (IMX952_CCM_NUM_CLK_SRC + 1)
```

相关声明：[IMX952_CLK_RESERVED1](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gabfebcfad721ae0c19c0fdab927890cc9)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

保留外设 时钟 1（Reserved peripheral clock 1）。

<a id="r_ga3c9d2874480a9a3742b81aa64657d5a0"></a>

```c
#define IMX952_CLK_BUSAON (IMX952_CCM_NUM_CLK_SRC + 2)
```

相关声明：[IMX952_CLK_BUSAON](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga3c9d2874480a9a3742b81aa64657d5a0)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

AON 总线 时钟（AON bus clock）。

<a id="r_gafe7b5204c752fa2dfc45abbe9ef56b1b"></a>

```c
#define IMX952_CLK_CAN1 (IMX952_CCM_NUM_CLK_SRC + 3)
```

相关声明：[IMX952_CLK_CAN1](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gafe7b5204c752fa2dfc45abbe9ef56b1b)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

CAN1 时钟（CAN1 clock）。

<a id="r_gaa2bec9707b9dca1d91c5473ef1640ca2"></a>

```c
#define IMX952_CLK_RESERVED4 (IMX952_CCM_NUM_CLK_SRC + 4)
```

相关声明：[IMX952_CLK_RESERVED4](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gaa2bec9707b9dca1d91c5473ef1640ca2)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

保留外设 时钟 4（Reserved peripheral clock 4）。

<a id="r_gad356191a96c27cb2c84bb54fded38075"></a>

```c
#define IMX952_CLK_I3C1SLOW (IMX952_CCM_NUM_CLK_SRC + 5)
```

相关声明：[IMX952_CLK_I3C1SLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gad356191a96c27cb2c84bb54fded38075)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

I3C1 慢速 时钟（I3C1 slow clock）。

<a id="r_gad2e8978ebfc8b671c2b0ad9d404be7d4"></a>

```c
#define IMX952_CLK_LPI2C1 (IMX952_CCM_NUM_CLK_SRC + 6)
```

相关声明：[IMX952_CLK_LPI2C1](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gad2e8978ebfc8b671c2b0ad9d404be7d4)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPI2C1 时钟（LPI2C1 clock）。

<a id="r_ga41460f3425b5258f3936a4c05f9774ed"></a>

```c
#define IMX952_CLK_LPI2C2 (IMX952_CCM_NUM_CLK_SRC + 7)
```

相关声明：[IMX952_CLK_LPI2C2](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga41460f3425b5258f3936a4c05f9774ed)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPI2C2 时钟（LPI2C2 clock）。

<a id="r_ga03ef430f1aa454c4a765f540064045d4"></a>

```c
#define IMX952_CLK_LPSPI1 (IMX952_CCM_NUM_CLK_SRC + 8)
```

相关声明：[IMX952_CLK_LPSPI1](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga03ef430f1aa454c4a765f540064045d4)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPSPI1 时钟（LPSPI1 clock）。

<a id="r_ga72914bea56dffea39955b80a363aea68"></a>

```c
#define IMX952_CLK_LPSPI2 (IMX952_CCM_NUM_CLK_SRC + 9)
```

相关声明：[IMX952_CLK_LPSPI2](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga72914bea56dffea39955b80a363aea68)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPSPI2 时钟（LPSPI2 clock）。

<a id="r_gacb1ebcf043e321e0db27c5f191799529"></a>

```c
#define IMX952_CLK_LPTMR1 (IMX952_CCM_NUM_CLK_SRC + 10)
```

相关声明：[IMX952_CLK_LPTMR1](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gacb1ebcf043e321e0db27c5f191799529)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPTMR1 时钟（LPTMR1 clock）。

<a id="r_ga8436c0cf30cd588c6455d0321baec0dc"></a>

```c
#define IMX952_CLK_LPUART1 (IMX952_CCM_NUM_CLK_SRC + 11)
```

相关声明：[IMX952_CLK_LPUART1](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga8436c0cf30cd588c6455d0321baec0dc)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPUART1 时钟（LPUART1 clock）。

<a id="r_ga79f9479bcd1aa7e6fcc69063391f4b14"></a>

```c
#define IMX952_CLK_LPUART2 (IMX952_CCM_NUM_CLK_SRC + 12)
```

相关声明：[IMX952_CLK_LPUART2](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga79f9479bcd1aa7e6fcc69063391f4b14)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPUART2 时钟（LPUART2 clock）。

<a id="r_ga5659948ecd9b48807e051734ea707738"></a>

```c
#define IMX952_CLK_M33 (IMX952_CCM_NUM_CLK_SRC + 13)
```

相关声明：[IMX952_CLK_M33](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga5659948ecd9b48807e051734ea707738)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

Cortex-M33 核心 时钟（Cortex-M33 core clock）。

<a id="r_ga2d428ca57850519a072c844cd6af195c"></a>

```c
#define IMX952_CLK_M33SYSTICK (IMX952_CCM_NUM_CLK_SRC + 14)
```

相关声明：[IMX952_CLK_M33SYSTICK](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga2d428ca57850519a072c844cd6af195c)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

Cortex-M33 SysTick 时钟（Cortex-M33 SysTick clock）。

<a id="r_ga63ee8489512d404515a7c0a93f709461"></a>

```c
#define IMX952_CLK_RESERVED15 (IMX952_CCM_NUM_CLK_SRC + 15)
```

相关声明：[IMX952_CLK_RESERVED15](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga63ee8489512d404515a7c0a93f709461)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

保留外设 时钟 15（Reserved peripheral clock 15）。

<a id="r_ga67b66c12811be5bed864d37a25653e2d"></a>

```c
#define IMX952_CLK_PDM (IMX952_CCM_NUM_CLK_SRC + 16)
```

相关声明：[IMX952_CLK_PDM](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga67b66c12811be5bed864d37a25653e2d)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

PDM 时钟（PDM clock）。

<a id="r_gad6bb83d2d46f67c39716ec744909e1f6"></a>

```c
#define IMX952_CLK_SAI1 (IMX952_CCM_NUM_CLK_SRC + 17)
```

相关声明：[IMX952_CLK_SAI1](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gad6bb83d2d46f67c39716ec744909e1f6)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

SAI1 时钟（SAI1 clock）。

<a id="r_ga651989292cdcf481380a884d4c0e5aef"></a>

```c
#define IMX952_CLK_RESERVED18 (IMX952_CCM_NUM_CLK_SRC + 18)
```

相关声明：[IMX952_CLK_RESERVED18](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga651989292cdcf481380a884d4c0e5aef)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

保留外设 时钟 18（Reserved peripheral clock 18）。

<a id="r_ga54de19acf040cef42d3e40ffce9412eb"></a>

```c
#define IMX952_CLK_TPM2 (IMX952_CCM_NUM_CLK_SRC + 19)
```

相关声明：[IMX952_CLK_TPM2](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga54de19acf040cef42d3e40ffce9412eb)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

TPM2 时钟（TPM2 clock）。

<a id="r_gae8433b2b0ba8c3daf76216a994a2d353"></a>

```c
#define IMX952_CLK_RESERVED20 (IMX952_CCM_NUM_CLK_SRC + 20)
```

相关声明：[IMX952_CLK_RESERVED20](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gae8433b2b0ba8c3daf76216a994a2d353)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

保留外设 时钟 20（Reserved peripheral clock 20）。

<a id="r_ga04d79491636ed5a37b9b4ae801066574"></a>

```c
#define IMX952_CLK_CAMAPB (IMX952_CCM_NUM_CLK_SRC + 21)
```

相关声明：[IMX952_CLK_CAMAPB](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga04d79491636ed5a37b9b4ae801066574)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

摄像头 APB 时钟（Camera APB clock）。

<a id="r_ga09fffe1b5527547c20667290b422e7de"></a>

```c
#define IMX952_CLK_CAMAXI (IMX952_CCM_NUM_CLK_SRC + 22)
```

相关声明：[IMX952_CLK_CAMAXI](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga09fffe1b5527547c20667290b422e7de)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

摄像头 AXI 时钟（Camera AXI clock）。

<a id="r_ga3dbac1b1a9e7e6c644ee140c96bbf81f"></a>

```c
#define IMX952_CLK_CAMCM0 (IMX952_CCM_NUM_CLK_SRC + 23)
```

相关声明：[IMX952_CLK_CAMCM0](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga3dbac1b1a9e7e6c644ee140c96bbf81f)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

摄像头 CM0 时钟（Camera CM0 clock）。

<a id="r_ga19837041e27ed67e9e6df73716fc9d54"></a>

```c
#define IMX952_CLK_CAMISI (IMX952_CCM_NUM_CLK_SRC + 24)
```

相关声明：[IMX952_CLK_CAMISI](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga19837041e27ed67e9e6df73716fc9d54)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

摄像头 ISI 时钟（Camera ISI clock）。

<a id="r_ga586eb4045847dbe332d8575acf99f3be"></a>

```c
#define IMX952_CLK_CAMPHYCFG (IMX952_CCM_NUM_CLK_SRC + 25)
```

相关声明：[IMX952_CLK_CAMPHYCFG](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga586eb4045847dbe332d8575acf99f3be)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

摄像头 PHY 配置 时钟（Camera PHY configuration clock）。

<a id="r_ga831a26f60a7116f4131bf77a8e5f66c9"></a>

```c
#define IMX952_CLK_MIPIPHYPLLBYPASS (IMX952_CCM_NUM_CLK_SRC + 26)
```

相关声明：[IMX952_CLK_MIPIPHYPLLBYPASS](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga831a26f60a7116f4131bf77a8e5f66c9)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

MIPI PHY PLL 旁路 时钟（MIPI PHY PLL bypass clock）。

<a id="r_ga3db8105a07f2ce87e006a2b9f758bd8f"></a>

```c
#define IMX952_CLK_RESERVED27 (IMX952_CCM_NUM_CLK_SRC + 27)
```

相关声明：[IMX952_CLK_RESERVED27](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga3db8105a07f2ce87e006a2b9f758bd8f)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

保留外设 时钟 27（Reserved peripheral clock 27）。

<a id="r_ga59bed80ccf3b29c8a1f92f2a265e02b1"></a>

```c
#define IMX952_CLK_MIPITESTBYTE (IMX952_CCM_NUM_CLK_SRC + 28)
```

相关声明：[IMX952_CLK_MIPITESTBYTE](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga59bed80ccf3b29c8a1f92f2a265e02b1)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

MIPI 测试 字节 时钟（MIPI test byte clock）。

<a id="r_gae927a53c34c5d1fcb6c4e7d6f5a2dbf2"></a>

```c
#define IMX952_CLK_A55 (IMX952_CCM_NUM_CLK_SRC + 29)
```

相关声明：[IMX952_CLK_A55](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gae927a53c34c5d1fcb6c4e7d6f5a2dbf2)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

Cortex-A55 核心 时钟（Cortex-A55 core clock）。

<a id="r_gaf97b4deb07b00e3d70b1ac3cf6604486"></a>

```c
#define IMX952_CLK_A55MTRBUS (IMX952_CCM_NUM_CLK_SRC + 30)
```

相关声明：[IMX952_CLK_A55MTRBUS](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gaf97b4deb07b00e3d70b1ac3cf6604486)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

Cortex-A55 MTR 总线 时钟（Cortex-A55 MTR bus clock）。

<a id="r_gad07cd50a19b3edea126a948af250e0e0"></a>

```c
#define IMX952_CLK_A55PERIPH (IMX952_CCM_NUM_CLK_SRC + 31)
```

相关声明：[IMX952_CLK_A55PERIPH](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gad07cd50a19b3edea126a948af250e0e0)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

Cortex-A55 外设 时钟（Cortex-A55 peripheral clock）。

<a id="r_ga1de7bf9d1d6864c6d7f5b09de6d742c5"></a>

```c
#define IMX952_CLK_DRAMALT (IMX952_CCM_NUM_CLK_SRC + 32)
```

相关声明：[IMX952_CLK_DRAMALT](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga1de7bf9d1d6864c6d7f5b09de6d742c5)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

DRAM 备用 时钟（DRAM alternate clock）。

<a id="r_ga4fc0088507462042656a34a6bf430dfb"></a>

```c
#define IMX952_CLK_DRAMAPB (IMX952_CCM_NUM_CLK_SRC + 33)
```

相关声明：[IMX952_CLK_DRAMAPB](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga4fc0088507462042656a34a6bf430dfb)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

DRAM APB 时钟（DRAM APB clock）。

<a id="r_ga0439a95f09f1f498b45f4cf51ceb8983"></a>

```c
#define IMX952_CLK_DISPAPB (IMX952_CCM_NUM_CLK_SRC + 34)
```

相关声明：[IMX952_CLK_DISPAPB](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga0439a95f09f1f498b45f4cf51ceb8983)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

显示 APB 时钟（Display APB clock）。

<a id="r_gae7bdf479b9aea05d0c99afa3e08c56ee"></a>

```c
#define IMX952_CLK_DISPAXI (IMX952_CCM_NUM_CLK_SRC + 35)
```

相关声明：[IMX952_CLK_DISPAXI](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gae7bdf479b9aea05d0c99afa3e08c56ee)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

显示 AXI 时钟（Display AXI clock）。

<a id="r_ga5a19ad3418eea5aedbbf72aa1b073a4b"></a>

```c
#define IMX952_CLK_DISPLPSPI (IMX952_CCM_NUM_CLK_SRC + 36)
```

相关声明：[IMX952_CLK_DISPLPSPI](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga5a19ad3418eea5aedbbf72aa1b073a4b)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

显示 LPSPI 时钟（Display LPSPI clock）。

<a id="r_ga5cce1fd12ca390ad1b345813797d51bb"></a>

```c
#define IMX952_CLK_DISPOCRAM (IMX952_CCM_NUM_CLK_SRC + 37)
```

相关声明：[IMX952_CLK_DISPOCRAM](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga5cce1fd12ca390ad1b345813797d51bb)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

显示 OCRAM 时钟（Display OCRAM clock）。

<a id="r_gad866759ea1a19d4b38335a722dc36bb1"></a>

```c
#define IMX952_CLK_DISPHYCFG (IMX952_CCM_NUM_CLK_SRC + 38)
```

相关声明：[IMX952_CLK_DISPHYCFG](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gad866759ea1a19d4b38335a722dc36bb1)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

显示 PHY 配置 时钟（Display PHY configuration clock）。

<a id="r_gabde7224b0230770740576871301f72a4"></a>

```c
#define IMX952_CLK_DISP1PIX (IMX952_CCM_NUM_CLK_SRC + 39)
```

相关声明：[IMX952_CLK_DISP1PIX](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gabde7224b0230770740576871301f72a4)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

显示 1 像素 时钟（Display 1 pixel clock）。

<a id="r_ga4885eba2f05bd15129c8d732d06195b6"></a>

```c
#define IMX952_CLK_DISPCDPHYAPB (IMX952_CCM_NUM_CLK_SRC + 40)
```

相关声明：[IMX952_CLK_DISPCDPHYAPB](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga4885eba2f05bd15129c8d732d06195b6)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

显示 CD PHY APB 时钟（Display CD PHY APB clock）。

<a id="r_ga17655f965e3128b63c8a3abf3c34768a"></a>

```c
#define IMX952_CLK_RESERVED41 (IMX952_CCM_NUM_CLK_SRC + 41)
```

相关声明：[IMX952_CLK_RESERVED41](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga17655f965e3128b63c8a3abf3c34768a)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

保留外设 时钟 41（Reserved peripheral clock 41）。

<a id="r_ga8b41919d03a6d77af5f4997b63899159"></a>

```c
#define IMX952_CLK_GPUAPB (IMX952_CCM_NUM_CLK_SRC + 42)
```

相关声明：[IMX952_CLK_GPUAPB](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga8b41919d03a6d77af5f4997b63899159)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

GPU APB 时钟（GPU APB clock）。

<a id="r_ga24c41790fa58c6bf9b2170e23e0c56f0"></a>

```c
#define IMX952_CLK_GPU (IMX952_CCM_NUM_CLK_SRC + 43)
```

相关声明：[IMX952_CLK_GPU](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga24c41790fa58c6bf9b2170e23e0c56f0)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

GPU 核心 时钟（GPU core clock）。

<a id="r_ga20f1a2162bf9ce0b5e0b2fe2db0075c5"></a>

```c
#define IMX952_CLK_HSIOACSCAN480M (IMX952_CCM_NUM_CLK_SRC + 44)
```

相关声明：[IMX952_CLK_HSIOACSCAN480M](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga20f1a2162bf9ce0b5e0b2fe2db0075c5)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

HSIO AC 扫描 480MHz 时钟（HSIO AC scan 480MHz clock）。

<a id="r_ga1b77d6c93474b9bee9cf2691c2e38d91"></a>

```c
#define IMX952_CLK_HSIOACSCAN80M (IMX952_CCM_NUM_CLK_SRC + 45)
```

相关声明：[IMX952_CLK_HSIOACSCAN80M](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga1b77d6c93474b9bee9cf2691c2e38d91)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

HSIO AC 扫描 80MHz 时钟（HSIO AC scan 80MHz clock）。

<a id="r_gaa79e6a0b67c4c3d2059821cf6304f94b"></a>

```c
#define IMX952_CLK_HSIO (IMX952_CCM_NUM_CLK_SRC + 46)
```

相关声明：[IMX952_CLK_HSIO](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gaa79e6a0b67c4c3d2059821cf6304f94b)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

HSIO 总线 时钟（HSIO bus clock）。

<a id="r_gae3c37de19e68fc80164646d9f18aca67"></a>

```c
#define IMX952_CLK_HSIOPCIEAUX (IMX952_CCM_NUM_CLK_SRC + 47)
```

相关声明：[IMX952_CLK_HSIOPCIEAUX](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gae3c37de19e68fc80164646d9f18aca67)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

HSIO PCIe 辅助 时钟（HSIO PCIe auxiliary clock）。

<a id="r_gaf9f80c9df9203ac548d36c2eef2e074b"></a>

```c
#define IMX952_CLK_HSIOPCIETEST160M (IMX952_CCM_NUM_CLK_SRC + 48)
```

相关声明：[IMX952_CLK_HSIOPCIETEST160M](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gaf9f80c9df9203ac548d36c2eef2e074b)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

HSIO PCIe 测试 160MHz 时钟（HSIO PCIe test 160MHz clock）。

<a id="r_ga656c3a598cc01dd56074ba178f4dd564"></a>

```c
#define IMX952_CLK_HSIOPCIETEST400M (IMX952_CCM_NUM_CLK_SRC + 49)
```

相关声明：[IMX952_CLK_HSIOPCIETEST400M](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga656c3a598cc01dd56074ba178f4dd564)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

HSIO PCIe 测试 400MHz 时钟（HSIO PCIe test 400MHz clock）。

<a id="r_gaf090ef87122451cc2c235950be7e7b86"></a>

```c
#define IMX952_CLK_HSIOPCIETEST500M (IMX952_CCM_NUM_CLK_SRC + 50)
```

相关声明：[IMX952_CLK_HSIOPCIETEST500M](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gaf090ef87122451cc2c235950be7e7b86)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

HSIO PCIe 测试 500MHz 时钟（HSIO PCIe test 500MHz clock）。

<a id="r_gafecfa87e99167f088cc489dae90a4173"></a>

```c
#define IMX952_CLK_HSIOUSBTEST50M (IMX952_CCM_NUM_CLK_SRC + 51)
```

相关声明：[IMX952_CLK_HSIOUSBTEST50M](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gafecfa87e99167f088cc489dae90a4173)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

HSIO USB 测试 50MHz 时钟（HSIO USB test 50MHz clock）。

<a id="r_gafadaf0326bf74a16cb1f58060fe3ce03"></a>

```c
#define IMX952_CLK_HSIOUSBTEST60M (IMX952_CCM_NUM_CLK_SRC + 52)
```

相关声明：[IMX952_CLK_HSIOUSBTEST60M](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gafadaf0326bf74a16cb1f58060fe3ce03)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

HSIO USB 测试 60MHz 时钟（HSIO USB test 60MHz clock）。

<a id="r_ga400485d6af68996afc3a86eabb9074f8"></a>

```c
#define IMX952_CLK_BUSM7 (IMX952_CCM_NUM_CLK_SRC + 53)
```

相关声明：[IMX952_CLK_BUSM7](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga400485d6af68996afc3a86eabb9074f8)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

M7 总线 时钟（M7 bus clock）。

<a id="r_ga71d063d87af2e021db96f44c72d9e611"></a>

```c
#define IMX952_CLK_M7 (IMX952_CCM_NUM_CLK_SRC + 54)
```

相关声明：[IMX952_CLK_M7](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga71d063d87af2e021db96f44c72d9e611)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

Cortex-M7 核心 时钟（Cortex-M7 core clock）。

<a id="r_ga4d4326b4f31df95619493a267b0faf4c"></a>

```c
#define IMX952_CLK_M7SYSTICK (IMX952_CCM_NUM_CLK_SRC + 55)
```

相关声明：[IMX952_CLK_M7SYSTICK](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga4d4326b4f31df95619493a267b0faf4c)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

Cortex-M7 SysTick 时钟（Cortex-M7 SysTick clock）。

<a id="r_gae52a0cc48000d0865742b08f072c7370"></a>

```c
#define IMX952_CLK_BUSNETCMIX (IMX952_CCM_NUM_CLK_SRC + 56)
```

相关声明：[IMX952_CLK_BUSNETCMIX](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gae52a0cc48000d0865742b08f072c7370)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

网络混合域 总线 时钟（Network mix bus clock）。

<a id="r_gab1af306d9110ef72fa5fdf25883da79b"></a>

```c
#define IMX952_CLK_ENET (IMX952_CCM_NUM_CLK_SRC + 57)
```

相关声明：[IMX952_CLK_ENET](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gab1af306d9110ef72fa5fdf25883da79b)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

以太网 时钟（Ethernet clock）。

<a id="r_gacc5632392213d34c342965af3f709463"></a>

```c
#define IMX952_CLK_ENETPHYTEST200M (IMX952_CCM_NUM_CLK_SRC + 58)
```

相关声明：[IMX952_CLK_ENETPHYTEST200M](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gacc5632392213d34c342965af3f709463)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

以太网 PHY 测试 200MHz 时钟（Ethernet PHY test 200MHz clock）。

<a id="r_ga5e18a17bbd01819729fbbd9f980b9c4a"></a>

```c
#define IMX952_CLK_ENETPHYTEST500M (IMX952_CCM_NUM_CLK_SRC + 59)
```

相关声明：[IMX952_CLK_ENETPHYTEST500M](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga5e18a17bbd01819729fbbd9f980b9c4a)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

以太网 PHY 测试 500MHz 时钟（Ethernet PHY test 500MHz clock）。

<a id="r_gadcf309e71ba8699ab9473fc0f6472afb"></a>

```c
#define IMX952_CLK_ENETPHYTEST667M (IMX952_CCM_NUM_CLK_SRC + 60)
```

相关声明：[IMX952_CLK_ENETPHYTEST667M](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gadcf309e71ba8699ab9473fc0f6472afb)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

以太网 PHY 测试 667MHz 时钟（Ethernet PHY test 667MHz clock）。

<a id="r_ga9fe95e36aa8fb3bac76a22bed8d6e968"></a>

```c
#define IMX952_CLK_ENETREF (IMX952_CCM_NUM_CLK_SRC + 61)
```

相关声明：[IMX952_CLK_ENETREF](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga9fe95e36aa8fb3bac76a22bed8d6e968)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

以太网 参考 时钟（Ethernet reference clock）。

<a id="r_ga93e85bbc5951f6908f956f5c8d95e4d7"></a>

```c
#define IMX952_CLK_ENETTIMER1 (IMX952_CCM_NUM_CLK_SRC + 62)
```

相关声明：[IMX952_CLK_ENETTIMER1](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga93e85bbc5951f6908f956f5c8d95e4d7)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

以太网 定时器 1 时钟（Ethernet timer 1 clock）。

<a id="r_ga58a267768b3191c2e01e7a18042950d8"></a>

```c
#define IMX952_CLK_RESERVED63 (IMX952_CCM_NUM_CLK_SRC + 63)
```

相关声明：[IMX952_CLK_RESERVED63](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga58a267768b3191c2e01e7a18042950d8)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

保留外设 时钟 63（Reserved peripheral clock 63）。

<a id="r_ga8f13732951eed83cecdac72b7180c4fa"></a>

```c
#define IMX952_CLK_SAI2 (IMX952_CCM_NUM_CLK_SRC + 64)
```

相关声明：[IMX952_CLK_SAI2](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga8f13732951eed83cecdac72b7180c4fa)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

SAI2 时钟（SAI2 clock）。

<a id="r_gadf0655cea3322c98c299982bb3a72b10"></a>

```c
#define IMX952_CLK_NOCAPB (IMX952_CCM_NUM_CLK_SRC + 65)
```

相关声明：[IMX952_CLK_NOCAPB](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gadf0655cea3322c98c299982bb3a72b10)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

NOC APB 时钟（NOC APB clock）。

<a id="r_gaf0b14b642cc622e4118566f980b2711b"></a>

```c
#define IMX952_CLK_NOC (IMX952_CCM_NUM_CLK_SRC + 66)
```

相关声明：[IMX952_CLK_NOC](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gaf0b14b642cc622e4118566f980b2711b)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

片上网络 时钟（Network-on-chip clock）。

<a id="r_ga7679466832c15b9007ccbfd89f29399b"></a>

```c
#define IMX952_CLK_NPUAPB (IMX952_CCM_NUM_CLK_SRC + 67)
```

相关声明：[IMX952_CLK_NPUAPB](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga7679466832c15b9007ccbfd89f29399b)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

NPU APB 时钟（NPU APB clock）。

<a id="r_ga6c0826297d389a194d9c347e1dec2f3c"></a>

```c
#define IMX952_CLK_NPU (IMX952_CCM_NUM_CLK_SRC + 68)
```

相关声明：[IMX952_CLK_NPU](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga6c0826297d389a194d9c347e1dec2f3c)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

神经网络处理单元 时钟（Neural processing unit clock）。

<a id="r_ga9e7e982eafba4ef8f087e86f09388dd1"></a>

```c
#define IMX952_CLK_CCMCKO1 (IMX952_CCM_NUM_CLK_SRC + 69)
```

相关声明：[IMX952_CLK_CCMCKO1](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga9e7e982eafba4ef8f087e86f09388dd1)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

CCM 时钟 输出 1（CCM clock output 1）。

<a id="r_ga0796739931db4bf6ca285dc9cef6442e"></a>

```c
#define IMX952_CLK_CCMCKO2 (IMX952_CCM_NUM_CLK_SRC + 70)
```

相关声明：[IMX952_CLK_CCMCKO2](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga0796739931db4bf6ca285dc9cef6442e)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

CCM 时钟 输出 2（CCM clock output 2）。

<a id="r_ga7e163c133a4c737f00350698e800ced9"></a>

```c
#define IMX952_CLK_CCMCKO3 (IMX952_CCM_NUM_CLK_SRC + 71)
```

相关声明：[IMX952_CLK_CCMCKO3](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga7e163c133a4c737f00350698e800ced9)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

CCM 时钟 输出 3（CCM clock output 3）。

<a id="r_ga690093bbcb23e642d84b02b2a584db96"></a>

```c
#define IMX952_CLK_CCMCKO4 (IMX952_CCM_NUM_CLK_SRC + 72)
```

相关声明：[IMX952_CLK_CCMCKO4](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga690093bbcb23e642d84b02b2a584db96)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

CCM 时钟 输出 4（CCM clock output 4）。

<a id="r_ga06e617b155e10bead692b6681e06ce77"></a>

```c
#define IMX952_CLK_VPUAPB (IMX952_CCM_NUM_CLK_SRC + 73)
```

相关声明：[IMX952_CLK_VPUAPB](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga06e617b155e10bead692b6681e06ce77)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

VPU APB 时钟（VPU APB clock）。

<a id="r_ga96a440ad719c4016207d3fefbeabbf6e"></a>

```c
#define IMX952_CLK_VPU (IMX952_CCM_NUM_CLK_SRC + 74)
```

相关声明：[IMX952_CLK_VPU](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga96a440ad719c4016207d3fefbeabbf6e)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

视频处理单元 时钟（Video processing unit clock）。

<a id="r_gae2d0ef4dcebbb0438c4a53856becc422"></a>

```c
#define IMX952_CLK_RESERVED75 (IMX952_CCM_NUM_CLK_SRC + 75)
```

相关声明：[IMX952_CLK_RESERVED75](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gae2d0ef4dcebbb0438c4a53856becc422)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

保留外设 时钟 75（Reserved peripheral clock 75）。

<a id="r_gab9ce1f7a67d35b9aa91e4ccc0b221753"></a>

```c
#define IMX952_CLK_RESERVED76 (IMX952_CCM_NUM_CLK_SRC + 76)
```

相关声明：[IMX952_CLK_RESERVED76](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gab9ce1f7a67d35b9aa91e4ccc0b221753)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

保留外设 时钟 76（Reserved peripheral clock 76）。

<a id="r_ga06b9b945d709ee18aaac219bc00c00b5"></a>

```c
#define IMX952_CLK_AUDIOXCVR (IMX952_CCM_NUM_CLK_SRC + 77)
```

相关声明：[IMX952_CLK_AUDIOXCVR](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga06b9b945d709ee18aaac219bc00c00b5)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

音频收发器 时钟（Audio transceiver clock）。

<a id="r_gae001be70f9ee9e5dd3034168ac997357"></a>

```c
#define IMX952_CLK_BUSWAKEUP (IMX952_CCM_NUM_CLK_SRC + 78)
```

相关声明：[IMX952_CLK_BUSWAKEUP](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gae001be70f9ee9e5dd3034168ac997357)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

唤醒 总线 时钟（Wakeup bus clock）。

<a id="r_gad3cd5b7a2b34c6888809a8bf5588a9fe"></a>

```c
#define IMX952_CLK_CAN2 (IMX952_CCM_NUM_CLK_SRC + 79)
```

相关声明：[IMX952_CLK_CAN2](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gad3cd5b7a2b34c6888809a8bf5588a9fe)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

CAN2 时钟（CAN2 clock）。

<a id="r_ga3965f0ca49447cef4bd6266baa4f203b"></a>

```c
#define IMX952_CLK_CAN3 (IMX952_CCM_NUM_CLK_SRC + 80)
```

相关声明：[IMX952_CLK_CAN3](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga3965f0ca49447cef4bd6266baa4f203b)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

CAN3 时钟（CAN3 clock）。

<a id="r_ga56ae00ef8a1ba6dab63a9f7cdd5a3d6d"></a>

```c
#define IMX952_CLK_CAN4 (IMX952_CCM_NUM_CLK_SRC + 81)
```

相关声明：[IMX952_CLK_CAN4](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga56ae00ef8a1ba6dab63a9f7cdd5a3d6d)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

CAN4 时钟（CAN4 clock）。

<a id="r_ga69c2d985644db8881a344d4d131ea4c8"></a>

```c
#define IMX952_CLK_CAN5 (IMX952_CCM_NUM_CLK_SRC + 82)
```

相关声明：[IMX952_CLK_CAN5](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga69c2d985644db8881a344d4d131ea4c8)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

CAN5 时钟（CAN5 clock）。

<a id="r_ga1fcb9ea2063f15bf883bdec8c02e16b8"></a>

```c
#define IMX952_CLK_FLEXIO1 (IMX952_CCM_NUM_CLK_SRC + 83)
```

相关声明：[IMX952_CLK_FLEXIO1](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga1fcb9ea2063f15bf883bdec8c02e16b8)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

FlexIO1 时钟（FlexIO1 clock）。

<a id="r_ga5dbb816f835529ef98f6a686294de54c"></a>

```c
#define IMX952_CLK_FLEXIO2 (IMX952_CCM_NUM_CLK_SRC + 84)
```

相关声明：[IMX952_CLK_FLEXIO2](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga5dbb816f835529ef98f6a686294de54c)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

FlexIO2 时钟（FlexIO2 clock）。

<a id="r_gad9334abd1606ef0aaaf99220e69162e5"></a>

```c
#define IMX952_CLK_XSPI1 (IMX952_CCM_NUM_CLK_SRC + 85)
```

相关声明：[IMX952_CLK_XSPI1](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gad9334abd1606ef0aaaf99220e69162e5)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

就地执行 SPI 1 时钟（eXecute-in-place SPI 1 clock）。

<a id="r_ga48a75f83239ad51a9e9900d28a74f32d"></a>

```c
#define IMX952_CLK_RESERVED86 (IMX952_CCM_NUM_CLK_SRC + 86)
```

相关声明：[IMX952_CLK_RESERVED86](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga48a75f83239ad51a9e9900d28a74f32d)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

保留外设 时钟 86（Reserved peripheral clock 86）。

<a id="r_ga40f266412cf80cb111bd5b62089c74ac"></a>

```c
#define IMX952_CLK_I3C2SLOW (IMX952_CCM_NUM_CLK_SRC + 87)
```

相关声明：[IMX952_CLK_I3C2SLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga40f266412cf80cb111bd5b62089c74ac)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

I3C2 慢速 时钟（I3C2 slow clock）。

<a id="r_ga9927f113303645c1413f35382147b5a6"></a>

```c
#define IMX952_CLK_LPI2C3 (IMX952_CCM_NUM_CLK_SRC + 88)
```

相关声明：[IMX952_CLK_LPI2C3](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga9927f113303645c1413f35382147b5a6)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPI2C3 时钟（LPI2C3 clock）。

<a id="r_ga4b145aea4cf3032a42831d1c2a2a016b"></a>

```c
#define IMX952_CLK_LPI2C4 (IMX952_CCM_NUM_CLK_SRC + 89)
```

相关声明：[IMX952_CLK_LPI2C4](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga4b145aea4cf3032a42831d1c2a2a016b)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPI2C4 时钟（LPI2C4 clock）。

<a id="r_ga340244c90568c62fa824ca8db2702b2e"></a>

```c
#define IMX952_CLK_LPI2C5 (IMX952_CCM_NUM_CLK_SRC + 90)
```

相关声明：[IMX952_CLK_LPI2C5](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga340244c90568c62fa824ca8db2702b2e)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPI2C5 时钟（LPI2C5 clock）。

<a id="r_gae066026bf708d6ac46263a0a7ca23d24"></a>

```c
#define IMX952_CLK_LPI2C6 (IMX952_CCM_NUM_CLK_SRC + 91)
```

相关声明：[IMX952_CLK_LPI2C6](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gae066026bf708d6ac46263a0a7ca23d24)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPI2C6 时钟（LPI2C6 clock）。

<a id="r_gae00eff47c6398a00f256caa56efa55f3"></a>

```c
#define IMX952_CLK_LPI2C7 (IMX952_CCM_NUM_CLK_SRC + 92)
```

相关声明：[IMX952_CLK_LPI2C7](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gae00eff47c6398a00f256caa56efa55f3)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPI2C7 时钟（LPI2C7 clock）。

<a id="r_ga7a200fa7987ac930c8a5f3dbd1e74c81"></a>

```c
#define IMX952_CLK_LPI2C8 (IMX952_CCM_NUM_CLK_SRC + 93)
```

相关声明：[IMX952_CLK_LPI2C8](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga7a200fa7987ac930c8a5f3dbd1e74c81)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPI2C8 时钟（LPI2C8 clock）。

<a id="r_ga3ab3fe70ad0fdd8c80069fc17867972b"></a>

```c
#define IMX952_CLK_LPSPI3 (IMX952_CCM_NUM_CLK_SRC + 94)
```

相关声明：[IMX952_CLK_LPSPI3](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga3ab3fe70ad0fdd8c80069fc17867972b)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPSPI3 时钟（LPSPI3 clock）。

<a id="r_ga76b045cd9c12e41886306964791f46ec"></a>

```c
#define IMX952_CLK_LPSPI4 (IMX952_CCM_NUM_CLK_SRC + 95)
```

相关声明：[IMX952_CLK_LPSPI4](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga76b045cd9c12e41886306964791f46ec)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPSPI4 时钟（LPSPI4 clock）。

<a id="r_ga13516d021d6a4062fb31f124e3ee72a4"></a>

```c
#define IMX952_CLK_LPSPI5 (IMX952_CCM_NUM_CLK_SRC + 96)
```

相关声明：[IMX952_CLK_LPSPI5](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga13516d021d6a4062fb31f124e3ee72a4)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPSPI5 时钟（LPSPI5 clock）。

<a id="r_ga30dac0d2cb4c13dc914d950678ae7ff4"></a>

```c
#define IMX952_CLK_LPSPI6 (IMX952_CCM_NUM_CLK_SRC + 97)
```

相关声明：[IMX952_CLK_LPSPI6](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga30dac0d2cb4c13dc914d950678ae7ff4)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPSPI6 时钟（LPSPI6 clock）。

<a id="r_gac4f02540f9cf0a12dfe94ddfbdb2bfc3"></a>

```c
#define IMX952_CLK_LPSPI7 (IMX952_CCM_NUM_CLK_SRC + 98)
```

相关声明：[IMX952_CLK_LPSPI7](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gac4f02540f9cf0a12dfe94ddfbdb2bfc3)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPSPI7 时钟（LPSPI7 clock）。

<a id="r_ga7e0f66376ddfa8d14689be5b1cc2f58d"></a>

```c
#define IMX952_CLK_LPSPI8 (IMX952_CCM_NUM_CLK_SRC + 99)
```

相关声明：[IMX952_CLK_LPSPI8](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga7e0f66376ddfa8d14689be5b1cc2f58d)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPSPI8 时钟（LPSPI8 clock）。

<a id="r_ga5a20f1157eb6e8204a4d0ada3aa82c89"></a>

```c
#define IMX952_CLK_LPTMR2 (IMX952_CCM_NUM_CLK_SRC + 100)
```

相关声明：[IMX952_CLK_LPTMR2](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga5a20f1157eb6e8204a4d0ada3aa82c89)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPTMR2 时钟（LPTMR2 clock）。

<a id="r_gae58fc80ca785f07f5495230941815f7a"></a>

```c
#define IMX952_CLK_LPUART3 (IMX952_CCM_NUM_CLK_SRC + 101)
```

相关声明：[IMX952_CLK_LPUART3](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gae58fc80ca785f07f5495230941815f7a)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPUART3 时钟（LPUART3 clock）。

<a id="r_ga5653005f43f816acfa66ded30325a562"></a>

```c
#define IMX952_CLK_LPUART4 (IMX952_CCM_NUM_CLK_SRC + 102)
```

相关声明：[IMX952_CLK_LPUART4](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga5653005f43f816acfa66ded30325a562)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPUART4 时钟（LPUART4 clock）。

<a id="r_gaeb992d7eaf2505cede034795536bdf37"></a>

```c
#define IMX952_CLK_LPUART5 (IMX952_CCM_NUM_CLK_SRC + 103)
```

相关声明：[IMX952_CLK_LPUART5](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gaeb992d7eaf2505cede034795536bdf37)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPUART5 时钟（LPUART5 clock）。

<a id="r_gae23f66d12251642ef39b1641b261f3af"></a>

```c
#define IMX952_CLK_LPUART6 (IMX952_CCM_NUM_CLK_SRC + 104)
```

相关声明：[IMX952_CLK_LPUART6](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gae23f66d12251642ef39b1641b261f3af)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPUART6 时钟（LPUART6 clock）。

<a id="r_ga270a616ad346393cc4c45a0645f2219d"></a>

```c
#define IMX952_CLK_LPUART7 (IMX952_CCM_NUM_CLK_SRC + 105)
```

相关声明：[IMX952_CLK_LPUART7](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga270a616ad346393cc4c45a0645f2219d)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPUART7 时钟（LPUART7 clock）。

<a id="r_gaff08699e35d25bd1dc758fcae970fc3e"></a>

```c
#define IMX952_CLK_LPUART8 (IMX952_CCM_NUM_CLK_SRC + 106)
```

相关声明：[IMX952_CLK_LPUART8](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gaff08699e35d25bd1dc758fcae970fc3e)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPUART8 时钟（LPUART8 clock）。

<a id="r_gab86838fbcfa36a15bfb30241e811d4df"></a>

```c
#define IMX952_CLK_SAI3 (IMX952_CCM_NUM_CLK_SRC + 107)
```

相关声明：[IMX952_CLK_SAI3](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gab86838fbcfa36a15bfb30241e811d4df)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

SAI3 时钟（SAI3 clock）。

<a id="r_ga4ec095c742bfdcc954b83d8c13aa1f95"></a>

```c
#define IMX952_CLK_SAI4 (IMX952_CCM_NUM_CLK_SRC + 108)
```

相关声明：[IMX952_CLK_SAI4](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga4ec095c742bfdcc954b83d8c13aa1f95)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

SAI4 时钟（SAI4 clock）。

<a id="r_gada66056d7a864b3a7fb73758d1f401e2"></a>

```c
#define IMX952_CLK_SAI5 (IMX952_CCM_NUM_CLK_SRC + 109)
```

相关声明：[IMX952_CLK_SAI5](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gada66056d7a864b3a7fb73758d1f401e2)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

SAI5 时钟（SAI5 clock）。

<a id="r_ga879119b0739e90c08dfb21d89c58be8e"></a>

```c
#define IMX952_CLK_SPDIF (IMX952_CCM_NUM_CLK_SRC + 110)
```

相关声明：[IMX952_CLK_SPDIF](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga879119b0739e90c08dfb21d89c58be8e)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

S/PDIF 时钟（S/PDIF clock）。

<a id="r_ga743096ff4fa6975b7dac8f10584643ad"></a>

```c
#define IMX952_CLK_SWOTRACE (IMX952_CCM_NUM_CLK_SRC + 111)
```

相关声明：[IMX952_CLK_SWOTRACE](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga743096ff4fa6975b7dac8f10584643ad)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

SWO 跟踪 时钟（SWO trace clock）。

<a id="r_gaef0ff808e6b781fa505dab10bc4fa51b"></a>

```c
#define IMX952_CLK_TPM4 (IMX952_CCM_NUM_CLK_SRC + 112)
```

相关声明：[IMX952_CLK_TPM4](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gaef0ff808e6b781fa505dab10bc4fa51b)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

TPM4 时钟（TPM4 clock）。

<a id="r_gadd0bb62c169c44e38fffed5c08e66914"></a>

```c
#define IMX952_CLK_TPM5 (IMX952_CCM_NUM_CLK_SRC + 113)
```

相关声明：[IMX952_CLK_TPM5](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gadd0bb62c169c44e38fffed5c08e66914)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

TPM5 时钟（TPM5 clock）。

<a id="r_ga263cf3ea860bfb247fdb40d8db63fcc3"></a>

```c
#define IMX952_CLK_TPM6 (IMX952_CCM_NUM_CLK_SRC + 114)
```

相关声明：[IMX952_CLK_TPM6](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga263cf3ea860bfb247fdb40d8db63fcc3)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

TPM6 时钟（TPM6 clock）。

<a id="r_ga682869be4456f0e4502e2035e8dc9903"></a>

```c
#define IMX952_CLK_TSTMR2 (IMX952_CCM_NUM_CLK_SRC + 115)
```

相关声明：[IMX952_CLK_TSTMR2](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga682869be4456f0e4502e2035e8dc9903)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

Timestamp 定时器 2 时钟（Timestamp timer 2 clock）。

<a id="r_gaa073d854720457424d9c59efa414c998"></a>

```c
#define IMX952_CLK_USBPHYBURUNIN (IMX952_CCM_NUM_CLK_SRC + 116)
```

相关声明：[IMX952_CLK_USBPHYBURUNIN](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gaa073d854720457424d9c59efa414c998)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

USB PHY 老化测试 时钟（USB PHY burn-in clock）。

<a id="r_ga708f630fb04d80884836308c55e7478f"></a>

```c
#define IMX952_CLK_USDHC1 (IMX952_CCM_NUM_CLK_SRC + 117)
```

相关声明：[IMX952_CLK_USDHC1](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga708f630fb04d80884836308c55e7478f)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

uSDHC1 时钟（uSDHC1 clock）。

<a id="r_ga55b06e78fcbeda0b95541b9c75e43fac"></a>

```c
#define IMX952_CLK_USDHC2 (IMX952_CCM_NUM_CLK_SRC + 118)
```

相关声明：[IMX952_CLK_USDHC2](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga55b06e78fcbeda0b95541b9c75e43fac)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

uSDHC2 时钟（uSDHC2 clock）。

<a id="r_ga2c9789e768474a24203d85e0dfc4a43a"></a>

```c
#define IMX952_CLK_USDHC3 (IMX952_CCM_NUM_CLK_SRC + 119)
```

相关声明：[IMX952_CLK_USDHC3](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga2c9789e768474a24203d85e0dfc4a43a)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

uSDHC3 时钟（uSDHC3 clock）。

<a id="r_ga79ee5f43bbd83b132a8d5a072a92aa14"></a>

```c
#define IMX952_CLK_V2XPK (IMX952_CCM_NUM_CLK_SRC + 120)
```

相关声明：[IMX952_CLK_V2XPK](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga79ee5f43bbd83b132a8d5a072a92aa14)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

V2X 数据包引擎 时钟（V2X packet engine clock）。

<a id="r_ga34a721794435930c4491b4dea37fd8a3"></a>

```c
#define IMX952_CLK_WAKEUPAXI (IMX952_CCM_NUM_CLK_SRC + 121)
```

相关声明：[IMX952_CLK_WAKEUPAXI](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga34a721794435930c4491b4dea37fd8a3)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

唤醒 AXI 时钟（Wakeup AXI clock）。

<a id="r_gacfb4422e38d4b3b1a28d06d7779264db"></a>

```c
#define IMX952_CLK_XSPISLVROOT (IMX952_CCM_NUM_CLK_SRC + 122)
```

相关声明：[IMX952_CLK_XSPISLVROOT](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gacfb4422e38d4b3b1a28d06d7779264db)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

XPI slave root 时钟（XPI slave root clock）。

<a id="r_gafb3ba58ee46ab0e69b617626f083c332"></a>

```c
#define IMX952_CLK_AUDMIX1 (IMX952_CCM_NUM_CLK_SRC + 123)
```

相关声明：[IMX952_CLK_AUDMIX1](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gafb3ba58ee46ab0e69b617626f083c332)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

Audio Mixer 1 时钟（Audio Mixer 1 clock）。

<a id="r_ga4accc64cecdd4ea562951b65e0fbc813"></a>

```c
#define IMX952_CLK_ASRC1 (IMX952_CCM_NUM_CLK_SRC + 124)
```

相关声明：[IMX952_CLK_ASRC1](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga4accc64cecdd4ea562951b65e0fbc813)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

Asynchronous Sample Rate Converter 1 时钟（Asynchronous Sample Rate Converter 1 clock）。

<a id="r_gaeaa32e8ac4c23850897e39599db1efe9"></a>

```c
#define IMX952_CLK_ASRC2 (IMX952_CCM_NUM_CLK_SRC + 125)
```

相关声明：[IMX952_CLK_ASRC2](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gaeaa32e8ac4c23850897e39599db1efe9)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

Asynchronous Sample Rate Converter 2 时钟（Asynchronous Sample Rate Converter 2 clock）。

<a id="r_ga982ed68fc9c8f3fbe1615d6005870c55"></a>

```c
#define IMX952_CLK_GPT2 (IMX952_CCM_NUM_CLK_SRC + 126)
```

相关声明：[IMX952_CLK_GPT2](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga982ed68fc9c8f3fbe1615d6005870c55)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

General Purpose Timer 2 时钟（General Purpose Timer 2 clock）。

<a id="r_ga01dea83a9c18afc152aae5701c07d20d"></a>

```c
#define IMX952_CLK_GPT3 (IMX952_CCM_NUM_CLK_SRC + 127)
```

相关声明：[IMX952_CLK_GPT3](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga01dea83a9c18afc152aae5701c07d20d)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

General Purpose Timer 3 时钟（General Purpose Timer 3 clock）。

<a id="r_ga303d0f829e212027c9875fa3e7803a6e"></a>

```c
#define IMX952_CLK_GPT4 (IMX952_CCM_NUM_CLK_SRC + 128)
```

相关声明：[IMX952_CLK_GPT4](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga303d0f829e212027c9875fa3e7803a6e)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

General Purpose Timer 4 时钟（General Purpose Timer 4 clock）。

<a id="r_gad5de7aa86c7849e87978870e642e765e"></a>

```c
#define IMX952_CLK_GPT5 (IMX952_CCM_NUM_CLK_SRC + 129)
```

相关声明：[IMX952_CLK_GPT5](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gad5de7aa86c7849e87978870e642e765e)、[IMX952_CCM_NUM_CLK_SRC](#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

General Purpose Timer 5 时钟（General Purpose Timer 5 clock）。

## 1.2\_详细说明（Detailed Documentation）

<a id="a03330ea5d5d6cb6c5d0cbde5cc2bb8e6"></a>

### `IMX952_CCM_NUM_CLK_SRC`

```c
#define IMX952_CCM_NUM_CLK_SRC 41
```

时钟源（Clock Sources）的总数量。


## 1.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P351_imx952_clock.h_源码浏览.md)
- [IMX952_CLK_EXT](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gaf6037059e31f2eee0505c05fd73a32e0)
- [IMX952_CLK_32K](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga6a0a68d908a84c4a93edf0c9981445ae)
- [IMX952_CLK_24M](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga56d5ac81125d5666e24c7f59de010bb7)
- [IMX952_CLK_FRO](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga67e879f454af3931cae68730e99301b1)
- [IMX952_CLK_SYSPLL1_VCO](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gacd648fefd08ae73e3923413835c416c6)
- [IMX952_CLK_SYSPLL1_PFD0_UNGATED](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga1ebae6761620d16a0a4b09a727d4657c)
- [IMX952_CLK_SYSPLL1_PFD0](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gab12511de8338393da87eb0cbf5164f20)
- [IMX952_CLK_SYSPLL1_PFD0_DIV2](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga9cb16f591e68a767fcabc96f542a8266)
- [IMX952_CLK_SYSPLL1_PFD1_UNGATED](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga186d814b34520d4bf89390618eb6a27a)
- [IMX952_CLK_SYSPLL1_PFD1](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gad3f665c2a498de5e6b8c4a6820f865ac)
- [IMX952_CLK_SYSPLL1_PFD1_DIV2](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga84d02ee3a62f72a0c68a47e7dac9080c)
- [IMX952_CLK_SYSPLL1_PFD2_UNGATED](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga34175ac1a860b439816d52e49f8e2775)
- [IMX952_CLK_SYSPLL1_PFD2](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gade8ab32b729d75b9bad66609651f787c)
- [IMX952_CLK_SYSPLL1_PFD2_DIV2](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga01c4fc3c9e7c4a4a6a4142b58cbd7f9f)
- [IMX952_CLK_AUDIOPLL1_VCO](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga542a45e1b3de20841ce7fea1389059b8)
- [IMX952_CLK_AUDIOPLL1](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gacf08c6f206a4e5c4cdc1de1d7baf352f)
- [IMX952_CLK_AUDIOPLL2_VCO](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga73dd94bba5f17a67cc2da01c99467002)
- [IMX952_CLK_AUDIOPLL2](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gad254dbac425c8abde24e624e5c7cbea8)
- [IMX952_CLK_VIDEOPLL1_VCO](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gad4f4063de4dd7be35c2cbfbcf793a4ae)
- [IMX952_CLK_VIDEOPLL1](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gab6665fdf4aae031f4df8001c92d114d5)
- [IMX952_CLK_SRC_RESERVED20](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga0b9ca70e5d4bdd12c7bb70e685e22869)
- [IMX952_CLK_SYSPLL1_PFD3_UNGATED](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gaba96133add3fa0476e75715cbe07b0b9)
- [IMX952_CLK_SYSPLL1_PFD3](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gacbc5d6bc23e87545b805af3a74ada9be)
- [IMX952_CLK_SYSPLL1_PFD3_DIV2](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gab7c7b531d6d2dd1dd0e96778c050eaf2)
- [IMX952_CLK_ARMPLL_VCO](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gaf17de78b0c59f399eec5faab0fe872c9)
- [IMX952_CLK_ARMPLL_PFD0_UNGATED](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga10e77fb38ce506eda46379865e46c784)
- [IMX952_CLK_ARMPLL_PFD0](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga8c53d9cb1cde130305ad5fdbe2984eb3)
- [IMX952_CLK_ARMPLL_PFD1_UNGATED](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga87480c6ce8b50db5b75c16d10f97c0cd)
- [IMX952_CLK_ARMPLL_PFD1](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gaffaac3c31b37079c1f873c53583158e5)
- [IMX952_CLK_ARMPLL_PFD2_UNGATED](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga4896537b4d1948eb4155fef172984452)
- [IMX952_CLK_ARMPLL_PFD2](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga1d8c6d7c7b1485cf9c8a0919dede47a0)
- [IMX952_CLK_ARMPLL_PFD3_UNGATED](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gae91ffcb10da54e26aab5c81bb908d322)
- [IMX952_CLK_ARMPLL_PFD3](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga42e8f7465fd70ff8f9752297c836d3b9)
- [IMX952_CLK_DRAMPLL_VCO](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga68beaaa7c75b9bed7ed6bf0c38620a2a)
- [IMX952_CLK_DRAMPLL](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gab843821fa6441f9edcb5be1b774383f7)
- [IMX952_CLK_HSIOPLL_VCO](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gac23033e983a469be2d4e4f90a272ede2)
- [IMX952_CLK_HSIOPLL](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga699f4715ec324b2d598c3dd87e5401f2)
- [IMX952_CLK_LDBPLL_VCO](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga6dbecdd20f5073eedd6959b5251d995e)
- [IMX952_CLK_LDBPLL](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gaf6edfa1d415c823899837459813d0213)
- [IMX952_CLK_EXT1](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#gab5c7237c02398f2b58ac0231d5db059d)
- [IMX952_CLK_EXT2](../api_coap_trusted_topic_reference/P009_NXP i.MX952 时钟源（Clock Sources）.md#ga4fa9a6ba981ce6a53ece7ab5b9a19424)
- [IMX952_CLK_ADC](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gadd6d1896e8c854ea655c6149753054b2)
- [IMX952_CLK_RESERVED1](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gabfebcfad721ae0c19c0fdab927890cc9)
- [IMX952_CLK_BUSAON](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga3c9d2874480a9a3742b81aa64657d5a0)
- [IMX952_CLK_CAN1](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gafe7b5204c752fa2dfc45abbe9ef56b1b)
- [IMX952_CLK_RESERVED4](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gaa2bec9707b9dca1d91c5473ef1640ca2)
- [IMX952_CLK_I3C1SLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gad356191a96c27cb2c84bb54fded38075)
- [IMX952_CLK_LPI2C1](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gad2e8978ebfc8b671c2b0ad9d404be7d4)
- [IMX952_CLK_LPI2C2](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga41460f3425b5258f3936a4c05f9774ed)
- [IMX952_CLK_LPSPI1](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga03ef430f1aa454c4a765f540064045d4)
- [IMX952_CLK_LPSPI2](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga72914bea56dffea39955b80a363aea68)
- [IMX952_CLK_LPTMR1](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gacb1ebcf043e321e0db27c5f191799529)
- [IMX952_CLK_LPUART1](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga8436c0cf30cd588c6455d0321baec0dc)
- [IMX952_CLK_LPUART2](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga79f9479bcd1aa7e6fcc69063391f4b14)
- [IMX952_CLK_M33](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga5659948ecd9b48807e051734ea707738)
- [IMX952_CLK_M33SYSTICK](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga2d428ca57850519a072c844cd6af195c)
- [IMX952_CLK_RESERVED15](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga63ee8489512d404515a7c0a93f709461)
- [IMX952_CLK_PDM](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga67b66c12811be5bed864d37a25653e2d)
- [IMX952_CLK_SAI1](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gad6bb83d2d46f67c39716ec744909e1f6)
- [IMX952_CLK_RESERVED18](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga651989292cdcf481380a884d4c0e5aef)
- [IMX952_CLK_TPM2](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga54de19acf040cef42d3e40ffce9412eb)
- [IMX952_CLK_RESERVED20](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gae8433b2b0ba8c3daf76216a994a2d353)
- [IMX952_CLK_CAMAPB](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga04d79491636ed5a37b9b4ae801066574)
- [IMX952_CLK_CAMAXI](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga09fffe1b5527547c20667290b422e7de)
- [IMX952_CLK_CAMCM0](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga3dbac1b1a9e7e6c644ee140c96bbf81f)
- [IMX952_CLK_CAMISI](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga19837041e27ed67e9e6df73716fc9d54)
- [IMX952_CLK_CAMPHYCFG](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga586eb4045847dbe332d8575acf99f3be)
- [IMX952_CLK_MIPIPHYPLLBYPASS](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga831a26f60a7116f4131bf77a8e5f66c9)
- [IMX952_CLK_RESERVED27](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga3db8105a07f2ce87e006a2b9f758bd8f)
- [IMX952_CLK_MIPITESTBYTE](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga59bed80ccf3b29c8a1f92f2a265e02b1)
- [IMX952_CLK_A55](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gae927a53c34c5d1fcb6c4e7d6f5a2dbf2)
- [IMX952_CLK_A55MTRBUS](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gaf97b4deb07b00e3d70b1ac3cf6604486)
- [IMX952_CLK_A55PERIPH](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gad07cd50a19b3edea126a948af250e0e0)
- [IMX952_CLK_DRAMALT](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga1de7bf9d1d6864c6d7f5b09de6d742c5)
- [IMX952_CLK_DRAMAPB](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga4fc0088507462042656a34a6bf430dfb)
- [IMX952_CLK_DISPAPB](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga0439a95f09f1f498b45f4cf51ceb8983)
- [IMX952_CLK_DISPAXI](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gae7bdf479b9aea05d0c99afa3e08c56ee)
- [IMX952_CLK_DISPLPSPI](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga5a19ad3418eea5aedbbf72aa1b073a4b)
- [IMX952_CLK_DISPOCRAM](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga5cce1fd12ca390ad1b345813797d51bb)
- [IMX952_CLK_DISPHYCFG](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gad866759ea1a19d4b38335a722dc36bb1)
- [IMX952_CLK_DISP1PIX](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gabde7224b0230770740576871301f72a4)
- [IMX952_CLK_DISPCDPHYAPB](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga4885eba2f05bd15129c8d732d06195b6)
- [IMX952_CLK_RESERVED41](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga17655f965e3128b63c8a3abf3c34768a)
- [IMX952_CLK_GPUAPB](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga8b41919d03a6d77af5f4997b63899159)
- [IMX952_CLK_GPU](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga24c41790fa58c6bf9b2170e23e0c56f0)
- [IMX952_CLK_HSIOACSCAN480M](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga20f1a2162bf9ce0b5e0b2fe2db0075c5)
- [IMX952_CLK_HSIOACSCAN80M](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga1b77d6c93474b9bee9cf2691c2e38d91)
- [IMX952_CLK_HSIO](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gaa79e6a0b67c4c3d2059821cf6304f94b)
- [IMX952_CLK_HSIOPCIEAUX](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gae3c37de19e68fc80164646d9f18aca67)
- [IMX952_CLK_HSIOPCIETEST160M](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gaf9f80c9df9203ac548d36c2eef2e074b)
- [IMX952_CLK_HSIOPCIETEST400M](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga656c3a598cc01dd56074ba178f4dd564)
- [IMX952_CLK_HSIOPCIETEST500M](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gaf090ef87122451cc2c235950be7e7b86)
- [IMX952_CLK_HSIOUSBTEST50M](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gafecfa87e99167f088cc489dae90a4173)
- [IMX952_CLK_HSIOUSBTEST60M](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gafadaf0326bf74a16cb1f58060fe3ce03)
- [IMX952_CLK_BUSM7](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga400485d6af68996afc3a86eabb9074f8)
- [IMX952_CLK_M7](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga71d063d87af2e021db96f44c72d9e611)
- [IMX952_CLK_M7SYSTICK](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga4d4326b4f31df95619493a267b0faf4c)
- [IMX952_CLK_BUSNETCMIX](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gae52a0cc48000d0865742b08f072c7370)
- [IMX952_CLK_ENET](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gab1af306d9110ef72fa5fdf25883da79b)
- [IMX952_CLK_ENETPHYTEST200M](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gacc5632392213d34c342965af3f709463)
- [IMX952_CLK_ENETPHYTEST500M](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga5e18a17bbd01819729fbbd9f980b9c4a)
- [IMX952_CLK_ENETPHYTEST667M](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gadcf309e71ba8699ab9473fc0f6472afb)
- [IMX952_CLK_ENETREF](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga9fe95e36aa8fb3bac76a22bed8d6e968)
- [IMX952_CLK_ENETTIMER1](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga93e85bbc5951f6908f956f5c8d95e4d7)
- [IMX952_CLK_RESERVED63](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga58a267768b3191c2e01e7a18042950d8)
- [IMX952_CLK_SAI2](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga8f13732951eed83cecdac72b7180c4fa)
- [IMX952_CLK_NOCAPB](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gadf0655cea3322c98c299982bb3a72b10)
- [IMX952_CLK_NOC](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gaf0b14b642cc622e4118566f980b2711b)
- [IMX952_CLK_NPUAPB](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga7679466832c15b9007ccbfd89f29399b)
- [IMX952_CLK_NPU](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga6c0826297d389a194d9c347e1dec2f3c)
- [IMX952_CLK_CCMCKO1](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga9e7e982eafba4ef8f087e86f09388dd1)
- [IMX952_CLK_CCMCKO2](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga0796739931db4bf6ca285dc9cef6442e)
- [IMX952_CLK_CCMCKO3](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga7e163c133a4c737f00350698e800ced9)
- [IMX952_CLK_CCMCKO4](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga690093bbcb23e642d84b02b2a584db96)
- [IMX952_CLK_VPUAPB](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga06e617b155e10bead692b6681e06ce77)
- [IMX952_CLK_VPU](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga96a440ad719c4016207d3fefbeabbf6e)
- [IMX952_CLK_RESERVED75](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gae2d0ef4dcebbb0438c4a53856becc422)
- [IMX952_CLK_RESERVED76](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gab9ce1f7a67d35b9aa91e4ccc0b221753)
- [IMX952_CLK_AUDIOXCVR](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga06b9b945d709ee18aaac219bc00c00b5)
- [IMX952_CLK_BUSWAKEUP](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gae001be70f9ee9e5dd3034168ac997357)
- [IMX952_CLK_CAN2](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gad3cd5b7a2b34c6888809a8bf5588a9fe)
- [IMX952_CLK_CAN3](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga3965f0ca49447cef4bd6266baa4f203b)
- [IMX952_CLK_CAN4](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga56ae00ef8a1ba6dab63a9f7cdd5a3d6d)
- [IMX952_CLK_CAN5](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga69c2d985644db8881a344d4d131ea4c8)
- [IMX952_CLK_FLEXIO1](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga1fcb9ea2063f15bf883bdec8c02e16b8)
- [IMX952_CLK_FLEXIO2](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga5dbb816f835529ef98f6a686294de54c)
- [IMX952_CLK_XSPI1](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gad9334abd1606ef0aaaf99220e69162e5)
- [IMX952_CLK_RESERVED86](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga48a75f83239ad51a9e9900d28a74f32d)
- [IMX952_CLK_I3C2SLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga40f266412cf80cb111bd5b62089c74ac)
- [IMX952_CLK_LPI2C3](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga9927f113303645c1413f35382147b5a6)
- [IMX952_CLK_LPI2C4](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga4b145aea4cf3032a42831d1c2a2a016b)
- [IMX952_CLK_LPI2C5](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga340244c90568c62fa824ca8db2702b2e)
- [IMX952_CLK_LPI2C6](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gae066026bf708d6ac46263a0a7ca23d24)
- [IMX952_CLK_LPI2C7](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gae00eff47c6398a00f256caa56efa55f3)
- [IMX952_CLK_LPI2C8](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga7a200fa7987ac930c8a5f3dbd1e74c81)
- [IMX952_CLK_LPSPI3](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga3ab3fe70ad0fdd8c80069fc17867972b)
- [IMX952_CLK_LPSPI4](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga76b045cd9c12e41886306964791f46ec)
- [IMX952_CLK_LPSPI5](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga13516d021d6a4062fb31f124e3ee72a4)
- [IMX952_CLK_LPSPI6](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga30dac0d2cb4c13dc914d950678ae7ff4)
- [IMX952_CLK_LPSPI7](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gac4f02540f9cf0a12dfe94ddfbdb2bfc3)
- [IMX952_CLK_LPSPI8](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga7e0f66376ddfa8d14689be5b1cc2f58d)
- [IMX952_CLK_LPTMR2](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga5a20f1157eb6e8204a4d0ada3aa82c89)
- [IMX952_CLK_LPUART3](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gae58fc80ca785f07f5495230941815f7a)
- [IMX952_CLK_LPUART4](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga5653005f43f816acfa66ded30325a562)
- [IMX952_CLK_LPUART5](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gaeb992d7eaf2505cede034795536bdf37)
- [IMX952_CLK_LPUART6](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gae23f66d12251642ef39b1641b261f3af)
- [IMX952_CLK_LPUART7](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga270a616ad346393cc4c45a0645f2219d)
- [IMX952_CLK_LPUART8](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gaff08699e35d25bd1dc758fcae970fc3e)
- [IMX952_CLK_SAI3](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gab86838fbcfa36a15bfb30241e811d4df)
- [IMX952_CLK_SAI4](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga4ec095c742bfdcc954b83d8c13aa1f95)
- [IMX952_CLK_SAI5](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gada66056d7a864b3a7fb73758d1f401e2)
- [IMX952_CLK_SPDIF](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga879119b0739e90c08dfb21d89c58be8e)
- [IMX952_CLK_SWOTRACE](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga743096ff4fa6975b7dac8f10584643ad)
- [IMX952_CLK_TPM4](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gaef0ff808e6b781fa505dab10bc4fa51b)
- [IMX952_CLK_TPM5](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gadd0bb62c169c44e38fffed5c08e66914)
- [IMX952_CLK_TPM6](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga263cf3ea860bfb247fdb40d8db63fcc3)
- [IMX952_CLK_TSTMR2](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga682869be4456f0e4502e2035e8dc9903)
- [IMX952_CLK_USBPHYBURUNIN](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gaa073d854720457424d9c59efa414c998)
- [IMX952_CLK_USDHC1](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga708f630fb04d80884836308c55e7478f)
- [IMX952_CLK_USDHC2](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga55b06e78fcbeda0b95541b9c75e43fac)
- [IMX952_CLK_USDHC3](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga2c9789e768474a24203d85e0dfc4a43a)
- [IMX952_CLK_V2XPK](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga79ee5f43bbd83b132a8d5a072a92aa14)
- [IMX952_CLK_WAKEUPAXI](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga34a721794435930c4491b4dea37fd8a3)
- [IMX952_CLK_XSPISLVROOT](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gacfb4422e38d4b3b1a28d06d7779264db)
- [IMX952_CLK_AUDMIX1](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gafb3ba58ee46ab0e69b617626f083c332)
- [IMX952_CLK_ASRC1](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga4accc64cecdd4ea562951b65e0fbc813)
- [IMX952_CLK_ASRC2](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gaeaa32e8ac4c23850897e39599db1efe9)
- [IMX952_CLK_GPT2](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga982ed68fc9c8f3fbe1615d6005870c55)
- [IMX952_CLK_GPT3](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga01dea83a9c18afc152aae5701c07d20d)
- [IMX952_CLK_GPT4](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#ga303d0f829e212027c9875fa3e7803a6e)
- [IMX952_CLK_GPT5](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html#gad5de7aa86c7849e87978870e642e765e)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__dt-bindings__clock__mchp_pic32ck_sg_gc_clock.h_文件参考.md)
