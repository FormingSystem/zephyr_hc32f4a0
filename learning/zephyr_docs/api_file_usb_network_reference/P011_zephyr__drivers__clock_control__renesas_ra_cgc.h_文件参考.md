---
id: learning.zephyr-docs.api-file-usb-network-reference.page-11
title: zephyr__drivers__clock_control__renesas_ra_cgc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas__ra__cgc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_zephyr\_\_drivers\_\_clock\_control\_\_renesas\_ra\_cgc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/renesas__ra__cgc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Renesas RA时钟发生电路（Clock Generator Circuit，CGC）的头文件。

<a id="details"></a>

```c
#include <zephyr/drivers/clock_control.h>
#include <zephyr/dt-bindings/clock/ra_clock.h>
```

查看此文件的源码。

Renesas RA时钟发生电路（Clock Generator Circuit，CGC）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 11.1\_数据结构（Data Structures）

<a id="r_clock_5Fcontrol_5Fra_5Fpclk_5Fcfg"></a>

```c
struct clock_control_ra_pclk_cfg
```

相关声明：[clock_control_ra_pclk_cfg](../clock_cmsis_model_reference/P001_clock_control_ra_pclk_cfg_结构体.md)。

外设时钟配置（Peripheral Clock Configuration）。

<a id="r_clock_5Fcontrol_5Fra_5Fsubsys_5Fcfg"></a>

```c
struct clock_control_ra_subsys_cfg
```

相关声明：[clock_control_ra_subsys_cfg](../clock_cmsis_model_reference/P002_clock_control_ra_subsys_cfg_结构体.md)。

子系统时钟控制配置（Subsystem Clock Control Configuration）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.2\_宏定义（Macros）

<a id="r_ga69f75bb6ad2e7c3d22936754ba3bf5b5"></a>

```c
#define RA_CGC_PROP_HAS_STATUS_OKAY_OR(node_id, prop, default_value)
```

相关声明：[RA_CGC_PROP_HAS_STATUS_OKAY_OR](../api_protocol_topic_reference/P012_瑞萨（Renesas）RA 时钟生成电路（CGC）.md#ga69f75bb6ad2e7c3d22936754ba3bf5b5)。

根据设备树状态（devicetree status）有条件地获取属性的辅助宏。

<a id="r_ga45ba53a59830676d22f80b29165ae399"></a>

```c
#define RA_CGC_CLK_SRC(node_id)
```

相关声明：[RA_CGC_CLK_SRC](../api_protocol_topic_reference/P012_瑞萨（Renesas）RA 时钟生成电路（CGC）.md#ga45ba53a59830676d22f80b29165ae399)。

从设备树获取时钟源（clock source）的辅助宏。

<a id="r_gaf54cadef83174db1f2180c65fb436c28"></a>

```c
#define RA_CGC_CLK_DIV(clk, prop, default_value)
```

相关声明：[RA_CGC_CLK_DIV](../api_protocol_topic_reference/P012_瑞萨（Renesas）RA 时钟生成电路（CGC）.md#gaf54cadef83174db1f2180c65fb436c28)。

用于计算时钟分频值（clock divider）的辅助宏。

<a id="r_gac836d0409da1193de27a8c61510d06c5"></a>

```c
#define RA_CGC_DIV_BCLK(n)
```

相关声明：[RA_CGC_DIV_BCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gac836d0409da1193de27a8c61510d06c5)。

BCLK 分频器（Divider）。

<a id="r_gaa6e8ba963160224076dacac43db705d7"></a>

```c
#define RA_CGC_DIV_CANFDCLK(n)
```

相关声明：[RA_CGC_DIV_CANFDCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gaa6e8ba963160224076dacac43db705d7)。

CANFD 分频器（Divider）。

<a id="r_gaae1620e152c33e3d4a95b5cac0cb1c76"></a>

```c
#define RA_CGC_DIV_CECCLK(n)
```

相关声明：[RA_CGC_DIV_CECCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gaae1620e152c33e3d4a95b5cac0cb1c76)。

CEC 分频器（Divider）。

<a id="r_ga8b169aba21f7e00cb80ffa0229cf0ca7"></a>

```c
#define RA_CGC_DIV_CLKOUT(n)
```

相关声明：[RA_CGC_DIV_CLKOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga8b169aba21f7e00cb80ffa0229cf0ca7)。

CLKOUT 分频器（Divider）。

<a id="r_ga5d01387282e98e3c1836cc18098726ec"></a>

```c
#define RA_CGC_DIV_CPUCLK0(n)
```

相关声明：[RA_CGC_DIV_CPUCLK0](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga5d01387282e98e3c1836cc18098726ec)。

CPUCLK0 分频器（Divider）。

<a id="r_ga04c6195e596c187ec77ed5ebc8cd735b"></a>

```c
#define RA_CGC_DIV_CPUCLK1(n)
```

相关声明：[RA_CGC_DIV_CPUCLK1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga04c6195e596c187ec77ed5ebc8cd735b)。

CPUCLK1 分频器（Divider）。

<a id="r_gaa38d17ba1d228ca66ef1f21720bc05b4"></a>

```c
#define RA_CGC_DIV_MRPCLK(n)
```

相关声明：[RA_CGC_DIV_MRPCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gaa38d17ba1d228ca66ef1f21720bc05b4)。

MRPCLK 分频器（Divider）。

<a id="r_gabf6b0bc9229f7b9b667662d5e7287af3"></a>

```c
#define RA_CGC_DIV_CPUCLK(n)
```

相关声明：[RA_CGC_DIV_CPUCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gabf6b0bc9229f7b9b667662d5e7287af3)。

CPUCLK 分频器（Divider）。

<a id="r_ga8006ac020337b43c9039290de93b237c"></a>

```c
#define RA_CGC_DIV_FCLK(n)
```

相关声明：[RA_CGC_DIV_FCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga8006ac020337b43c9039290de93b237c)。

FCLK 分频器（Divider）。

<a id="r_gae414f33fc622f1eea25ed38b4e48b284"></a>

```c
#define RA_CGC_DIV_I3CCLK(n)
```

相关声明：[RA_CGC_DIV_I3CCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gae414f33fc622f1eea25ed38b4e48b284)。

I3C 分频器（Divider）。

<a id="r_ga152905c07ac6744e4dbcaa88cc44b7b0"></a>

```c
#define RA_CGC_DIV_ICLK(n)
```

相关声明：[RA_CGC_DIV_ICLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga152905c07ac6744e4dbcaa88cc44b7b0)。

ICLK 分频器（Divider）。

<a id="r_gade972ca4dc22a1438ae0ee8a7f0b1c86"></a>

```c
#define RA_CGC_DIV_LCDCLK(n)
```

相关声明：[RA_CGC_DIV_LCDCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gade972ca4dc22a1438ae0ee8a7f0b1c86)。

LCDCLK 分频器（Divider）。

<a id="r_ga6e21efeff2e4b079ba56bf33524517d5"></a>

```c
#define RA_CGC_DIV_OCTASPICLK(n)
```

相关声明：[RA_CGC_DIV_OCTASPICLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga6e21efeff2e4b079ba56bf33524517d5)。

OCTASPI 分频器（Divider）。

<a id="r_ga40a2d9224061ee4b25e98407ee60eecc"></a>

```c
#define RA_CGC_DIV_PCLKA(n)
```

相关声明：[RA_CGC_DIV_PCLKA](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga40a2d9224061ee4b25e98407ee60eecc)。

PCLKA 分频器（Divider）。

<a id="r_gad3881c28b08b0775b6596f7e1932f2ff"></a>

```c
#define RA_CGC_DIV_PCLKB(n)
```

相关声明：[RA_CGC_DIV_PCLKB](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gad3881c28b08b0775b6596f7e1932f2ff)。

PCLKB 分频器（Divider）。

<a id="r_ga38799ae63c6aef7b8f637826fe5de9fd"></a>

```c
#define RA_CGC_DIV_PCLKC(n)
```

相关声明：[RA_CGC_DIV_PCLKC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga38799ae63c6aef7b8f637826fe5de9fd)。

PCLKC 分频器（Divider）。

<a id="r_ga775ccb80b8d68022e8e4a3e93f2d347c"></a>

```c
#define RA_CGC_DIV_PCLKD(n)
```

相关声明：[RA_CGC_DIV_PCLKD](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga775ccb80b8d68022e8e4a3e93f2d347c)。

PCLKD 分频器（Divider）。

<a id="r_gaa8cde7ee7535ddd404a05ae72f598b28"></a>

```c
#define RA_CGC_DIV_PCLKE(n)
```

相关声明：[RA_CGC_DIV_PCLKE](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gaa8cde7ee7535ddd404a05ae72f598b28)。

PCLKE 分频器（Divider）。

<a id="r_ga0f6bd3b07d9c1c4e07daa28443c8148e"></a>

```c
#define RA_CGC_DIV_PLL(n)
```

相关声明：[RA_CGC_DIV_PLL](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga0f6bd3b07d9c1c4e07daa28443c8148e)。

PLL 分频器（Divider）。

<a id="r_gaa5fd2b712624e2c73aac2574a5ea6512"></a>

```c
#define RA_CGC_DIV_PLLP(n)
```

相关声明：[RA_CGC_DIV_PLLP](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gaa5fd2b712624e2c73aac2574a5ea6512)。

PLLP 分频器（Divider）。

<a id="r_ga255f1f50393cf7f3396e1890b7728f49"></a>

```c
#define RA_CGC_DIV_PLLQ(n)
```

相关声明：[RA_CGC_DIV_PLLQ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga255f1f50393cf7f3396e1890b7728f49)。

PLLQ 分频器（Divider）。

<a id="r_gab1ea3ce0335620c286430c0af2de0b89"></a>

```c
#define RA_CGC_DIV_PLLR(n)
```

相关声明：[RA_CGC_DIV_PLLR](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gab1ea3ce0335620c286430c0af2de0b89)。

PLLR 分频器（Divider）。

<a id="r_gace4275eba4a646416ef6e0ffad3efafb"></a>

```c
#define RA_CGC_DIV_PLL2(n)
```

相关声明：[RA_CGC_DIV_PLL2](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gace4275eba4a646416ef6e0ffad3efafb)。

PLL2 分频器（Divider）。

<a id="r_ga11dbb86891568e5f75f9666107aac1bc"></a>

```c
#define RA_CGC_DIV_PLL2P(n)
```

相关声明：[RA_CGC_DIV_PLL2P](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga11dbb86891568e5f75f9666107aac1bc)。

PLL2P 分频器（Divider）。

<a id="r_ga1dc330555e762496bb90f9d623c6bbfb"></a>

```c
#define RA_CGC_DIV_PLL2Q(n)
```

相关声明：[RA_CGC_DIV_PLL2Q](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga1dc330555e762496bb90f9d623c6bbfb)。

PLL2Q 分频器（Divider）。

<a id="r_ga9e61fda937cc02e1484c64c0dbeb6dd5"></a>

```c
#define RA_CGC_DIV_PLL2R(n)
```

相关声明：[RA_CGC_DIV_PLL2R](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga9e61fda937cc02e1484c64c0dbeb6dd5)。

PLL2R 分频器（Divider）。

<a id="r_gaf20a6aa81df58686419d3163430aa59f"></a>

```c
#define RA_CGC_DIV_SCICLK(n)
```

相关声明：[RA_CGC_DIV_SCICLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gaf20a6aa81df58686419d3163430aa59f)。

SCICLK 分频器（Divider）。

<a id="r_ga28b424f22f72071af6fbe8351ad72101"></a>

```c
#define RA_CGC_DIV_SPICLK(n)
```

相关声明：[RA_CGC_DIV_SPICLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga28b424f22f72071af6fbe8351ad72101)。

SPICLK 分频器（Divider）。

<a id="r_ga944584d8d7372fad12f8e13bab00e7ae"></a>

```c
#define RA_CGC_DIV_U60CLK(n)
```

相关声明：[RA_CGC_DIV_U60CLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga944584d8d7372fad12f8e13bab00e7ae)。

U60CLK 分频器（Divider）。

<a id="r_ga90a5ab20631fff89d39980a144ec2ea0"></a>

```c
#define RA_CGC_DIV_UCLK(n)
```

相关声明：[RA_CGC_DIV_UCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga90a5ab20631fff89d39980a144ec2ea0)。

UCLK 分频器（Divider）。

<a id="r_ga602dbf5f7d734c7cb202fb88f92aadc7"></a>

```c
#define RA_CGC_DIV_SCISPICLK(n)
```

相关声明：[RA_CGC_DIV_SCISPICLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga602dbf5f7d734c7cb202fb88f92aadc7)。

SCISPI 分频器（Divider）。

<a id="r_gaa4b71829a1a84d1d80b4056fa138384a"></a>

```c
#define RA_CGC_DIV_GPTCLK(n)
```

相关声明：[RA_CGC_DIV_GPTCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gaa4b71829a1a84d1d80b4056fa138384a)。

GPTCLK 分频器（Divider）。

<a id="r_ga192f3830fa2ca7e21999a09a49d5aa91"></a>

```c
#define RA_CGC_DIV_IICCLK(n)
```

相关声明：[RA_CGC_DIV_IICCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga192f3830fa2ca7e21999a09a49d5aa91)。

IICCLK 分频器（Divider）。

<a id="r_gae079778c09cf9b2cb94a797cc7c7c2c2"></a>

```c
#define RA_CGC_DIV_ADCCLK(n)
```

相关声明：[RA_CGC_DIV_ADCCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gae079778c09cf9b2cb94a797cc7c7c2c2)。

ADCCLK 分频器（Divider）。

<a id="r_gacf26a8ec3df98acf72563383e4d11a32"></a>

```c
#define RA_CGC_DIV_MRICLK(n)
```

相关声明：[RA_CGC_DIV_MRICLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gacf26a8ec3df98acf72563383e4d11a32)。

MRICLK 分频器（Divider）。

<a id="r_ga86ba99da1338772f789e8f9f3d584b57"></a>

```c
#define RA_CGC_DIV_NPUCLK(n)
```

相关声明：[RA_CGC_DIV_NPUCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga86ba99da1338772f789e8f9f3d584b57)。

NPUCLK 分频器（Divider）。

<a id="r_ga9accde0e281cef734b4755708f1c6cb6"></a>

```c
#define RA_CGC_DIV_BCLKA(n)
```

相关声明：[RA_CGC_DIV_BCLKA](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga9accde0e281cef734b4755708f1c6cb6)。

BCLKA 分频器（Divider）。

<a id="r_ga2894aade41c703b8ec1c947809bec49c"></a>

```c
#define RA_CGC_DIV_ESWCLK(n)
```

相关声明：[RA_CGC_DIV_ESWCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga2894aade41c703b8ec1c947809bec49c)。

ESWCLK 分频器（Divider）。

<a id="r_ga91bbe885dbe96bf64327cd3df85d0cd0"></a>

```c
#define RA_CGC_DIV_ESWPHYCLK(n)
```

相关声明：[RA_CGC_DIV_ESWPHYCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga91bbe885dbe96bf64327cd3df85d0cd0)。

ESWPHYCLK 分频器（Divider）。

<a id="r_ga2197a3da41a74b99404fbe665644f3b5"></a>

```c
#define RA_CGC_DIV_ETHPHYCLK(n)
```

相关声明：[RA_CGC_DIV_ETHPHYCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga2197a3da41a74b99404fbe665644f3b5)。

ETHPHY 分频器（Divider）。

<a id="r_ga8db2d1551894c727a5104b0e075a2eff"></a>

```c
#define RA_CGC_DIV_ESCCLK(n)
```

相关声明：[RA_CGC_DIV_ESCCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga8db2d1551894c727a5104b0e075a2eff)。

ESCCLK 分频器（Divider）。

<a id="r_gac479a6ad6cb28be1843e9021943cd6f1"></a>

```c
#define RA_CGC_DIV_DSMIFCLK(n)
```

相关声明：[RA_CGC_DIV_DSMIFCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gac479a6ad6cb28be1843e9021943cd6f1)。

DSMIFCLK 分频器（Divider）。

<a id="r_ga259a31fc288b1a8b7c8e0747afefabb8"></a>

```c
#define RA_CGC_DIV_XTALDIV_CLK(n)
```

相关声明：[RA_CGC_DIV_XTALDIV_CLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga259a31fc288b1a8b7c8e0747afefabb8)。

XTALDIV_CLK 分频器（Divider）。

<a id="r_ga300a739f16f545beb56683001057530c"></a>

```c
#define RA_CGC_DIV_HOCODIV_CLK(n)
```

相关声明：[RA_CGC_DIV_HOCODIV_CLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga300a739f16f545beb56683001057530c)。

HOCODIV_CLK 分频器（Divider）。

<a id="r_ga190f2ab8379eb5e75124d3bbbdc53e16"></a>

```c
#define RA_CGC_DIV_MOCODIV_CLK(n)
```

相关声明：[RA_CGC_DIV_MOCODIV_CLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga190f2ab8379eb5e75124d3bbbdc53e16)。

MOCODIV_CLK 分频器（Divider）。

<a id="r_ga8c8e5f9e5b7ec9e9ef286dd3f612fa65"></a>

```c
#define RA_CGC_DIV_SAU_CK00(n)
```

相关声明：[RA_CGC_DIV_SAU_CK00](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga8c8e5f9e5b7ec9e9ef286dd3f612fa65)。

SAU_CK00 分频器（Divider）。

<a id="r_ga7e85115ada319f740aff0d4fe20ad52f"></a>

```c
#define RA_CGC_DIV_SAU_CK01(n)
```

相关声明：[RA_CGC_DIV_SAU_CK01](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga7e85115ada319f740aff0d4fe20ad52f)。

SAU_CK01 分频器（Divider）。

<a id="r_ga35cb6e55a71bfd7298f77101260114a0"></a>

```c
#define RA_CGC_DIV_SAU_CK10(n)
```

相关声明：[RA_CGC_DIV_SAU_CK10](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga35cb6e55a71bfd7298f77101260114a0)。

SAU_CK10 分频器（Divider）。

<a id="r_ga066b916171efb57e73f6ce1a955204fa"></a>

```c
#define RA_CGC_DIV_SAU_CK11(n)
```

相关声明：[RA_CGC_DIV_SAU_CK11](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga066b916171efb57e73f6ce1a955204fa)。

SAU_CK11 分频器（Divider）。

<a id="r_ga1cfc8d2b14bff3e747bd2d0d5c8c600b"></a>

```c
#define RA_CGC_DIV_TAU_CK01(n)
```

相关声明：[RA_CGC_DIV_TAU_CK01](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga1cfc8d2b14bff3e747bd2d0d5c8c600b)。

TAU_CK01 分频器（Divider）。

<a id="r_ga665dd9cac9446a549960b07b40b739a0"></a>

```c
#define RA_CGC_DIV_TAU_CK02(n)
```

相关声明：[RA_CGC_DIV_TAU_CK02](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga665dd9cac9446a549960b07b40b739a0)。

TAU_CK02 分频器（Divider）。

<a id="r_gace75be507e1d26345d8e9eb85c2d1a6a"></a>

```c
#define RA_CGC_DIV_TAU_CK03(n)
```

相关声明：[RA_CGC_DIV_TAU_CK03](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gace75be507e1d26345d8e9eb85c2d1a6a)。

TAU_CK03 分频器（Divider）。

<a id="r_ga5e8e48984f6be7ae8fca08667a2dfd87"></a>

```c
#define RA_CGC_DIV_TAU_CK04(n)
```

相关声明：[RA_CGC_DIV_TAU_CK04](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga5e8e48984f6be7ae8fca08667a2dfd87)。

TAU_CK04 分频器（Divider）。

<a id="r_gac6d940bf68229ce58e586d99e88021ad"></a>

```c
#define BSP_CLOCKS_SOURCE_PLL BSP_CLOCKS_SOURCE_CLOCK_PLL
```

相关声明：[BSP_CLOCKS_SOURCE_PLL](../api_vector_pipeline_topic_reference/P006_瑞萨 RA BSP 时钟源常量（Clock Source Constants）.md#gac6d940bf68229ce58e586d99e88021ad)。

PLL 锁相环时钟源（Clock Source）。

<a id="r_ga80b3c5e721364e07c795d759e56bef5f"></a>

```c
#define BSP_CLOCKS_SOURCE_PLLP BSP_CLOCKS_SOURCE_CLOCK_PLL
```

相关声明：[BSP_CLOCKS_SOURCE_PLLP](../api_vector_pipeline_topic_reference/P006_瑞萨 RA BSP 时钟源常量（Clock Source Constants）.md#ga80b3c5e721364e07c795d759e56bef5f)。

PLLP 时钟源（Clock Source）。

<a id="r_ga198180ae8a259e478c13cb667efdc036"></a>

```c
#define BSP_CLOCKS_SOURCE_PLLQ BSP_CLOCKS_SOURCE_CLOCK_PLL1Q
```

相关声明：[BSP_CLOCKS_SOURCE_PLLQ](../api_vector_pipeline_topic_reference/P006_瑞萨 RA BSP 时钟源常量（Clock Source Constants）.md#ga198180ae8a259e478c13cb667efdc036)。

PLLQ 时钟源（Clock Source）。

<a id="r_ga9cf8b84320ad1c418e554c44d0ae324c"></a>

```c
#define BSP_CLOCKS_SOURCE_PLLR BSP_CLOCKS_SOURCE_CLOCK_PLL1R
```

相关声明：[BSP_CLOCKS_SOURCE_PLLR](../api_vector_pipeline_topic_reference/P006_瑞萨 RA BSP 时钟源常量（Clock Source Constants）.md#ga9cf8b84320ad1c418e554c44d0ae324c)。

PLLR 时钟源（Clock Source）。

<a id="r_ga526d6007889c727bc820b23a8bd57eb1"></a>

```c
#define BSP_CLOCKS_SOURCE_PLL2 BSP_CLOCKS_SOURCE_CLOCK_PLL2
```

相关声明：[BSP_CLOCKS_SOURCE_PLL2](../api_vector_pipeline_topic_reference/P006_瑞萨 RA BSP 时钟源常量（Clock Source Constants）.md#ga526d6007889c727bc820b23a8bd57eb1)。

PLL2 时钟源（Clock Source）。

<a id="r_ga7d74f3dc378453283c5a2752d261a635"></a>

```c
#define BSP_CLOCKS_SOURCE_PLL2P BSP_CLOCKS_SOURCE_CLOCK_PLL2
```

相关声明：[BSP_CLOCKS_SOURCE_PLL2P](../api_vector_pipeline_topic_reference/P006_瑞萨 RA BSP 时钟源常量（Clock Source Constants）.md#ga7d74f3dc378453283c5a2752d261a635)。

PLL2P 时钟源（Clock Source）。

<a id="r_gae21c8ebb5bfd4160ced33343517cf755"></a>

```c
#define BSP_CLOCKS_SOURCE_PLL2Q BSP_CLOCKS_SOURCE_CLOCK_PLL2Q
```

相关声明：[BSP_CLOCKS_SOURCE_PLL2Q](../api_vector_pipeline_topic_reference/P006_瑞萨 RA BSP 时钟源常量（Clock Source Constants）.md#gae21c8ebb5bfd4160ced33343517cf755)。

PLL2Q 时钟源（Clock Source）。

<a id="r_ga2c9eb4860dc00767ec81567b7e1ef915"></a>

```c
#define BSP_CLOCKS_SOURCE_PLL2R BSP_CLOCKS_SOURCE_CLOCK_PLL2R
```

相关声明：[BSP_CLOCKS_SOURCE_PLL2R](../api_vector_pipeline_topic_reference/P006_瑞萨 RA BSP 时钟源常量（Clock Source Constants）.md#ga2c9eb4860dc00767ec81567b7e1ef915)。

PLL2R 时钟源（Clock Source）。

<a id="r_ga6e88996a2dba7df510f6f9c37d921abb"></a>

```c
#define BSP_CLOCKS_SOURCE_XTALDIV_CLK BSP_CLOCKS_SOURCE_CLOCK_MAIN_OSC
```

相关声明：[BSP_CLOCKS_SOURCE_XTALDIV_CLK](../api_vector_pipeline_topic_reference/P006_瑞萨 RA BSP 时钟源常量（Clock Source Constants）.md#ga6e88996a2dba7df510f6f9c37d921abb)。

XTALDIV_CLK 时钟源（Clock Source）。

<a id="r_ga54275c8fca9740aeb84a78a9df958977"></a>

```c
#define BSP_CLOCKS_SOURCE_HOCODIV_CLK BSP_CLOCKS_SOURCE_CLOCK_HOCO
```

相关声明：[BSP_CLOCKS_SOURCE_HOCODIV_CLK](../api_vector_pipeline_topic_reference/P006_瑞萨 RA BSP 时钟源常量（Clock Source Constants）.md#ga54275c8fca9740aeb84a78a9df958977)。

HOCODIV_CLK 时钟源（Clock Source）。

<a id="r_gafeb5b968b14bba1968899d01fc73ac60"></a>

```c
#define BSP_CLOCKS_SOURCE_MOCODIV_CLK BSP_CLOCKS_SOURCE_CLOCK_MOCO
```

相关声明：[BSP_CLOCKS_SOURCE_MOCODIV_CLK](../api_vector_pipeline_topic_reference/P006_瑞萨 RA BSP 时钟源常量（Clock Source Constants）.md#gafeb5b968b14bba1968899d01fc73ac60)。

MOCODIV_CLK 时钟源（Clock Source）。

<a id="r_gad56dead80f923b0b8840b3c84bdf65fa"></a>

```c
#define BSP_CLOCKS_CLKOUT_DIV_1 (0)
```

相关声明：[BSP_CLOCKS_CLKOUT_DIV_1](../api_connection_topic_reference/P007_瑞萨 RA BSP 时钟输出分频常量（Clock Clkout Divider Constants）.md#gad56dead80f923b0b8840b3c84bdf65fa)。

时钟输出（Clkout）1 分频。

<a id="r_ga46ed6e2dc58841f0b112003ed9f4a5db"></a>

```c
#define BSP_CLOCKS_CLKOUT_DIV_2 (1)
```

相关声明：[BSP_CLOCKS_CLKOUT_DIV_2](../api_connection_topic_reference/P007_瑞萨 RA BSP 时钟输出分频常量（Clock Clkout Divider Constants）.md#ga46ed6e2dc58841f0b112003ed9f4a5db)。

时钟输出 2 分频。

<a id="r_ga2ef0885ff687beeb8c5ec867bb97424b"></a>

```c
#define BSP_CLOCKS_CLKOUT_DIV_4 (2)
```

相关声明：[BSP_CLOCKS_CLKOUT_DIV_4](../api_connection_topic_reference/P007_瑞萨 RA BSP 时钟输出分频常量（Clock Clkout Divider Constants）.md#ga2ef0885ff687beeb8c5ec867bb97424b)。

时钟输出 4 分频。

<a id="r_ga79d6afda43cf5f9f6246fdb28285fd8e"></a>

```c
#define BSP_CLOCKS_CLKOUT_DIV_8 (3)
```

相关声明：[BSP_CLOCKS_CLKOUT_DIV_8](../api_connection_topic_reference/P007_瑞萨 RA BSP 时钟输出分频常量（Clock Clkout Divider Constants）.md#ga79d6afda43cf5f9f6246fdb28285fd8e)。

时钟输出 8 分频。

<a id="r_gac15fa2c5d5533746dd002636063bbf17"></a>

```c
#define BSP_CLOCKS_CLKOUT_DIV_16 (4)
```

相关声明：[BSP_CLOCKS_CLKOUT_DIV_16](../api_connection_topic_reference/P007_瑞萨 RA BSP 时钟输出分频常量（Clock Clkout Divider Constants）.md#gac15fa2c5d5533746dd002636063bbf17)。

时钟输出 16 分频。

<a id="r_ga58684d2331eb5cd218bbfc58254b27e7"></a>

```c
#define BSP_CLOCKS_CLKOUT_DIV_32 (5)
```

相关声明：[BSP_CLOCKS_CLKOUT_DIV_32](../api_connection_topic_reference/P007_瑞萨 RA BSP 时钟输出分频常量（Clock Clkout Divider Constants）.md#ga58684d2331eb5cd218bbfc58254b27e7)。

时钟输出 32 分频。

<a id="r_gaae419122d7da67d550e5d93e8108c237"></a>

```c
#define BSP_CLOCKS_CLKOUT_DIV_64 (6)
```

相关声明：[BSP_CLOCKS_CLKOUT_DIV_64](../api_connection_topic_reference/P007_瑞萨 RA BSP 时钟输出分频常量（Clock Clkout Divider Constants）.md#gaae419122d7da67d550e5d93e8108c237)。

时钟输出 64 分频。

<a id="r_ga1541a9c2e367cea7a96da0d522d2c7eb"></a>

```c
#define BSP_CLOCKS_CLKOUT_DIV_128 (7)
```

相关声明：[BSP_CLOCKS_CLKOUT_DIV_128](../api_connection_topic_reference/P007_瑞萨 RA BSP 时钟输出分频常量（Clock Clkout Divider Constants）.md#ga1541a9c2e367cea7a96da0d522d2c7eb)。

时钟输出 128 分频。


## 11.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control.h](../timer_reference/P096_时钟控制完整头文件.md)
- [zephyr/dt-bindings/clock/ra_clock.h](../api_source_reference/P693_ra_clock.h_源码浏览.md)
- [查看此文件的源码。](../api_source_runtime_reference/P052_renesas_ra_cgc.h_源码浏览.md)
- [clock_control_ra_pclk_cfg](../clock_cmsis_model_reference/P001_clock_control_ra_pclk_cfg_结构体.md)
- [clock_control_ra_subsys_cfg](../clock_cmsis_model_reference/P002_clock_control_ra_subsys_cfg_结构体.md)
- [RA_CGC_PROP_HAS_STATUS_OKAY_OR](../api_protocol_topic_reference/P012_瑞萨（Renesas）RA 时钟生成电路（CGC）.md#ga69f75bb6ad2e7c3d22936754ba3bf5b5)
- [RA_CGC_CLK_SRC](../api_protocol_topic_reference/P012_瑞萨（Renesas）RA 时钟生成电路（CGC）.md#ga45ba53a59830676d22f80b29165ae399)
- [RA_CGC_CLK_DIV](../api_protocol_topic_reference/P012_瑞萨（Renesas）RA 时钟生成电路（CGC）.md#gaf54cadef83174db1f2180c65fb436c28)
- [RA_CGC_DIV_BCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gac836d0409da1193de27a8c61510d06c5)
- [RA_CGC_DIV_CANFDCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gaa6e8ba963160224076dacac43db705d7)
- [RA_CGC_DIV_CECCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gaae1620e152c33e3d4a95b5cac0cb1c76)
- [RA_CGC_DIV_CLKOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga8b169aba21f7e00cb80ffa0229cf0ca7)
- [RA_CGC_DIV_CPUCLK0](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga5d01387282e98e3c1836cc18098726ec)
- [RA_CGC_DIV_CPUCLK1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga04c6195e596c187ec77ed5ebc8cd735b)
- [RA_CGC_DIV_MRPCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gaa38d17ba1d228ca66ef1f21720bc05b4)
- [RA_CGC_DIV_CPUCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gabf6b0bc9229f7b9b667662d5e7287af3)
- [RA_CGC_DIV_FCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga8006ac020337b43c9039290de93b237c)
- [RA_CGC_DIV_I3CCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gae414f33fc622f1eea25ed38b4e48b284)
- [RA_CGC_DIV_ICLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga152905c07ac6744e4dbcaa88cc44b7b0)
- [RA_CGC_DIV_LCDCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gade972ca4dc22a1438ae0ee8a7f0b1c86)
- [RA_CGC_DIV_OCTASPICLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga6e21efeff2e4b079ba56bf33524517d5)
- [RA_CGC_DIV_PCLKA](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga40a2d9224061ee4b25e98407ee60eecc)
- [RA_CGC_DIV_PCLKB](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gad3881c28b08b0775b6596f7e1932f2ff)
- [RA_CGC_DIV_PCLKC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga38799ae63c6aef7b8f637826fe5de9fd)
- [RA_CGC_DIV_PCLKD](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga775ccb80b8d68022e8e4a3e93f2d347c)
- [RA_CGC_DIV_PCLKE](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gaa8cde7ee7535ddd404a05ae72f598b28)
- [RA_CGC_DIV_PLL](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga0f6bd3b07d9c1c4e07daa28443c8148e)
- [RA_CGC_DIV_PLLP](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gaa5fd2b712624e2c73aac2574a5ea6512)
- [RA_CGC_DIV_PLLQ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga255f1f50393cf7f3396e1890b7728f49)
- [RA_CGC_DIV_PLLR](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gab1ea3ce0335620c286430c0af2de0b89)
- [RA_CGC_DIV_PLL2](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gace4275eba4a646416ef6e0ffad3efafb)
- [RA_CGC_DIV_PLL2P](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga11dbb86891568e5f75f9666107aac1bc)
- [RA_CGC_DIV_PLL2Q](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga1dc330555e762496bb90f9d623c6bbfb)
- [RA_CGC_DIV_PLL2R](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga9e61fda937cc02e1484c64c0dbeb6dd5)
- [RA_CGC_DIV_SCICLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gaf20a6aa81df58686419d3163430aa59f)
- [RA_CGC_DIV_SPICLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga28b424f22f72071af6fbe8351ad72101)
- [RA_CGC_DIV_U60CLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga944584d8d7372fad12f8e13bab00e7ae)
- [RA_CGC_DIV_UCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga90a5ab20631fff89d39980a144ec2ea0)
- [RA_CGC_DIV_SCISPICLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga602dbf5f7d734c7cb202fb88f92aadc7)
- [RA_CGC_DIV_GPTCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gaa4b71829a1a84d1d80b4056fa138384a)
- [RA_CGC_DIV_IICCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga192f3830fa2ca7e21999a09a49d5aa91)
- [RA_CGC_DIV_ADCCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gae079778c09cf9b2cb94a797cc7c7c2c2)
- [RA_CGC_DIV_MRICLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gacf26a8ec3df98acf72563383e4d11a32)
- [RA_CGC_DIV_NPUCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga86ba99da1338772f789e8f9f3d584b57)
- [RA_CGC_DIV_BCLKA](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga9accde0e281cef734b4755708f1c6cb6)
- [RA_CGC_DIV_ESWCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga2894aade41c703b8ec1c947809bec49c)
- [RA_CGC_DIV_ESWPHYCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga91bbe885dbe96bf64327cd3df85d0cd0)
- [RA_CGC_DIV_ETHPHYCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga2197a3da41a74b99404fbe665644f3b5)
- [RA_CGC_DIV_ESCCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga8db2d1551894c727a5104b0e075a2eff)
- [RA_CGC_DIV_DSMIFCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gac479a6ad6cb28be1843e9021943cd6f1)
- [RA_CGC_DIV_XTALDIV_CLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga259a31fc288b1a8b7c8e0747afefabb8)
- [RA_CGC_DIV_HOCODIV_CLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga300a739f16f545beb56683001057530c)
- [RA_CGC_DIV_MOCODIV_CLK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga190f2ab8379eb5e75124d3bbbdc53e16)
- [RA_CGC_DIV_SAU_CK00](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga8c8e5f9e5b7ec9e9ef286dd3f612fa65)
- [RA_CGC_DIV_SAU_CK01](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga7e85115ada319f740aff0d4fe20ad52f)
- [RA_CGC_DIV_SAU_CK10](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga35cb6e55a71bfd7298f77101260114a0)
- [RA_CGC_DIV_SAU_CK11](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga066b916171efb57e73f6ce1a955204fa)
- [RA_CGC_DIV_TAU_CK01](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga1cfc8d2b14bff3e747bd2d0d5c8c600b)
- [RA_CGC_DIV_TAU_CK02](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga665dd9cac9446a549960b07b40b739a0)
- [RA_CGC_DIV_TAU_CK03](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#gace75be507e1d26345d8e9eb85c2d1a6a)
- [RA_CGC_DIV_TAU_CK04](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html#ga5e8e48984f6be7ae8fca08667a2dfd87)
- [BSP_CLOCKS_SOURCE_PLL](../api_vector_pipeline_topic_reference/P006_瑞萨 RA BSP 时钟源常量（Clock Source Constants）.md#gac6d940bf68229ce58e586d99e88021ad)
- [BSP_CLOCKS_SOURCE_PLLP](../api_vector_pipeline_topic_reference/P006_瑞萨 RA BSP 时钟源常量（Clock Source Constants）.md#ga80b3c5e721364e07c795d759e56bef5f)
- [BSP_CLOCKS_SOURCE_PLLQ](../api_vector_pipeline_topic_reference/P006_瑞萨 RA BSP 时钟源常量（Clock Source Constants）.md#ga198180ae8a259e478c13cb667efdc036)
- [BSP_CLOCKS_SOURCE_PLLR](../api_vector_pipeline_topic_reference/P006_瑞萨 RA BSP 时钟源常量（Clock Source Constants）.md#ga9cf8b84320ad1c418e554c44d0ae324c)
- [BSP_CLOCKS_SOURCE_PLL2](../api_vector_pipeline_topic_reference/P006_瑞萨 RA BSP 时钟源常量（Clock Source Constants）.md#ga526d6007889c727bc820b23a8bd57eb1)
- [BSP_CLOCKS_SOURCE_PLL2P](../api_vector_pipeline_topic_reference/P006_瑞萨 RA BSP 时钟源常量（Clock Source Constants）.md#ga7d74f3dc378453283c5a2752d261a635)
- [BSP_CLOCKS_SOURCE_PLL2Q](../api_vector_pipeline_topic_reference/P006_瑞萨 RA BSP 时钟源常量（Clock Source Constants）.md#gae21c8ebb5bfd4160ced33343517cf755)
- [BSP_CLOCKS_SOURCE_PLL2R](../api_vector_pipeline_topic_reference/P006_瑞萨 RA BSP 时钟源常量（Clock Source Constants）.md#ga2c9eb4860dc00767ec81567b7e1ef915)
- [BSP_CLOCKS_SOURCE_XTALDIV_CLK](../api_vector_pipeline_topic_reference/P006_瑞萨 RA BSP 时钟源常量（Clock Source Constants）.md#ga6e88996a2dba7df510f6f9c37d921abb)
- [BSP_CLOCKS_SOURCE_HOCODIV_CLK](../api_vector_pipeline_topic_reference/P006_瑞萨 RA BSP 时钟源常量（Clock Source Constants）.md#ga54275c8fca9740aeb84a78a9df958977)
- [BSP_CLOCKS_SOURCE_MOCODIV_CLK](../api_vector_pipeline_topic_reference/P006_瑞萨 RA BSP 时钟源常量（Clock Source Constants）.md#gafeb5b968b14bba1968899d01fc73ac60)
- [BSP_CLOCKS_CLKOUT_DIV_1](../api_connection_topic_reference/P007_瑞萨 RA BSP 时钟输出分频常量（Clock Clkout Divider Constants）.md#gad56dead80f923b0b8840b3c84bdf65fa)
- [BSP_CLOCKS_CLKOUT_DIV_2](../api_connection_topic_reference/P007_瑞萨 RA BSP 时钟输出分频常量（Clock Clkout Divider Constants）.md#ga46ed6e2dc58841f0b112003ed9f4a5db)
- [BSP_CLOCKS_CLKOUT_DIV_4](../api_connection_topic_reference/P007_瑞萨 RA BSP 时钟输出分频常量（Clock Clkout Divider Constants）.md#ga2ef0885ff687beeb8c5ec867bb97424b)
- [BSP_CLOCKS_CLKOUT_DIV_8](../api_connection_topic_reference/P007_瑞萨 RA BSP 时钟输出分频常量（Clock Clkout Divider Constants）.md#ga79d6afda43cf5f9f6246fdb28285fd8e)
- [BSP_CLOCKS_CLKOUT_DIV_16](../api_connection_topic_reference/P007_瑞萨 RA BSP 时钟输出分频常量（Clock Clkout Divider Constants）.md#gac15fa2c5d5533746dd002636063bbf17)
- [BSP_CLOCKS_CLKOUT_DIV_32](../api_connection_topic_reference/P007_瑞萨 RA BSP 时钟输出分频常量（Clock Clkout Divider Constants）.md#ga58684d2331eb5cd218bbfc58254b27e7)
- [BSP_CLOCKS_CLKOUT_DIV_64](../api_connection_topic_reference/P007_瑞萨 RA BSP 时钟输出分频常量（Clock Clkout Divider Constants）.md#gaae419122d7da67d550e5d93e8108c237)
- [BSP_CLOCKS_CLKOUT_DIV_128](../api_connection_topic_reference/P007_瑞萨 RA BSP 时钟输出分频常量（Clock Clkout Divider Constants）.md#ga1541a9c2e367cea7a96da0d522d2c7eb)

<a id="header-details"></a>

---

[上一章](P010_zephyr__bluetooth__mesh__health_faults.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P012_zephyr__sd__sdio.h_文件参考.md)
