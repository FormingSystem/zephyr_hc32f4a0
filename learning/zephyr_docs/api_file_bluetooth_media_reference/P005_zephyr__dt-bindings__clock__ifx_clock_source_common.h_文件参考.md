---
id: learning.zephyr-docs.api-file-bluetooth-media-reference.page-5
title: zephyr__dt-bindings__clock__ifx_clock_source_common.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ifx__clock__source__common_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_dt-bindings\_\_clock\_\_ifx\_clock\_source\_common.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ifx__clock__source__common_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.1\_宏定义（Macros）

<a id="r_aa7e0a35b9b7f5c90d0b2219eba034535"></a>

```c
#define CLK_SOURCE_IHO
```

相关声明：[CLK_SOURCE_IHO](#aa7e0a35b9b7f5c90d0b2219eba034535)。

<a id="r_a0d94d3c9bace1fd8d01ef24ffb7ce054"></a>

```c
#define CLK_SOURCE_PILO
```

相关声明：[CLK_SOURCE_PILO](#a0d94d3c9bace1fd8d01ef24ffb7ce054)。

<a id="r_aa315d0f29d56dcaa2e269acd72f94f6e"></a>

```c
#define IFX_IHO 1
```

相关声明：[IFX_IHO](#aa315d0f29d56dcaa2e269acd72f94f6e)。

内部高速振荡器输入时钟（Internal High Speed Oscillator Input Clock）。

<a id="r_ad91e918e9d8832918e338ee0d932eca2"></a>

```c
#define IFX_IMO 2
```

相关声明：[IFX_IMO](#ad91e918e9d8832918e338ee0d932eca2)。

内部主振荡器输入时钟（Internal Main Oscillator Input Clock）。

<a id="r_add35b90080781e8214d8a6e42b596357"></a>

```c
#define IFX_ECO 3
```

相关声明：[IFX_ECO](#add35b90080781e8214d8a6e42b596357)。

外部晶体振荡器输入时钟（External Crystal Oscillator Input Clock）。

<a id="r_a0732d901f72ef098547c253a39ffb7fc"></a>

```c
#define IFX_EXT 4
```

相关声明：[IFX_EXT](#a0732d901f72ef098547c253a39ffb7fc)。

外部输入时钟（External Input Clock）。

<a id="r_aacf4257c7f77ca37ee9f88af68a290d0"></a>

```c
#define IFX_ALTHF 5
```

相关声明：[IFX_ALTHF](#aacf4257c7f77ca37ee9f88af68a290d0)。

备用高频输入时钟（Alternate High Frequency Input Clock）。

<a id="r_a0d7f68bb0c80aaf9f9af80fcef93000f"></a>

```c
#define IFX_ALTLF 6
```

相关声明：[IFX_ALTLF](#a0d7f68bb0c80aaf9f9af80fcef93000f)。

备用低频输入时钟（Alternate Low Frequency Input Clock）。

<a id="r_a8f4d9bccb15b7e30be213445f6a52942"></a>

```c
#define IFX_ILO 7
```

相关声明：[IFX_ILO](#a8f4d9bccb15b7e30be213445f6a52942)。

内部低速振荡器输入时钟（Internal Low Speed Oscillator Input Clock）。

<a id="r_a1a42be76091c654e98ae49ea5613f552"></a>

```c
#define IFX_PILO 8
```

相关声明：[IFX_PILO](#a1a42be76091c654e98ae49ea5613f552)。

精密内部低速振荡器输入时钟（Precision ILO Input Clock）。

<a id="r_acd56b092f7a5bf486be47471884016d4"></a>

```c
#define IFX_WCO 9
```

相关声明：[IFX_WCO](#acd56b092f7a5bf486be47471884016d4)。

钟表晶体振荡器输入时钟（Watch Crystal Oscillator Input Clock）。

<a id="r_adcfe0437bcfd3066970858a7001f348d"></a>

```c
#define IFX_MFO 10
```

相关声明：[IFX_MFO](#adcfe0437bcfd3066970858a7001f348d)。

中频振荡器时钟（Medium Frequency Oscillator Clock）。

<a id="r_a4dc7db5c4d08c2c0441296c0e5887201"></a>

```c
#define IFX_PATHMUX 11
```

相关声明：[IFX_PATHMUX](#a4dc7db5c4d08c2c0441296c0e5887201)。

FLL／PLL 输入的路径选择多路复用器（Path Selection Mux）。

<a id="r_ac9eefaa7728fa6cf3c93b4f3876a5207"></a>

```c
#define IFX_FLL 12
```

相关声明：[IFX_FLL](#ac9eefaa7728fa6cf3c93b4f3876a5207)。

锁频环时钟（Frequency-Locked Loop Clock）。

<a id="r_ae3d0dd2c94d0b8c1c52c9d9a044e26d7"></a>

```c
#define IFX_PLL200 13
```

相关声明：[IFX_PLL200](#ae3d0dd2c94d0b8c1c52c9d9a044e26d7)。

200 MHz 锁相环时钟（Phase-Locked Loop Clock）。

<a id="r_ad2b34fff09debe25b12c59ddae66b8ea"></a>

```c
#define IFX_PLL400 14
```

相关声明：[IFX_PLL400](#ad2b34fff09debe25b12c59ddae66b8ea)。

400 MHz 锁相环时钟（Phase-Locked Loop Clock）。

<a id="r_ae9ff69341c23a2a343d1e8100899a10b"></a>

```c
#define IFX_ECO_PRESCALER 15
```

相关声明：[IFX_ECO_PRESCALER](#ae9ff69341c23a2a343d1e8100899a10b)。

ECO 预分频器（Prescaler Divider）。

<a id="r_a535be3b20328c21862a5cd555caef943"></a>

```c
#define IFX_LF 16
```

相关声明：[IFX_LF](#a535be3b20328c21862a5cd555caef943)。

低频时钟（Low Frequency Clock）。

<a id="r_ac77c21b36967d2b4e02113f280d280bb"></a>

```c
#define IFX_MF 17
```

相关声明：[IFX_MF](#ac77c21b36967d2b4e02113f280d280bb)。

中频时钟（Medium Frequency Clock）。

<a id="r_a12860926bf5ecc84c7a616934e31281d"></a>

```c
#define IFX_HF 18
```

相关声明：[IFX_HF](#a12860926bf5ecc84c7a616934e31281d)。

高频时钟（High Frequency Clock）。

<a id="r_aa6f99fee380cdd367dc727d422717754"></a>

```c
#define IFX_PUMP 19
```

相关声明：[IFX_PUMP](#aa6f99fee380cdd367dc727d422717754)。

模拟泵时钟（Analog Pump Clock）。

<a id="r_a13c3737f1df2b3b07aeb3ce626d51077"></a>

```c
#define IFX_BAK 20
```

相关声明：[IFX_BAK](#a13c3737f1df2b3b07aeb3ce626d51077)。

备份电源域时钟（Backup Power Domain Clock）。

<a id="r_a17fab77216c09df141a7ef22204d4d52"></a>

```c
#define IFX_ALT_SYS_TICK 21
```

相关声明：[IFX_ALT_SYS_TICK](#a17fab77216c09df141a7ef22204d4d52)。

备用 SysTick 时钟（Alternative SysTick Clock）。

<a id="r_ae558d9e17464ae21609aa20c496362a9"></a>

```c
#define IFX_PERI 22
```

相关声明：[IFX_PERI](#ae558d9e17464ae21609aa20c496362a9)。

外设时钟组（Peripheral Clock Group）。

<a id="r_aa410e1f3f4ce4da3b94da1753dded7a0"></a>

```c
#define IFX_DPLL250_0 23
```

相关声明：[IFX_DPLL250_0](#aa410e1f3f4ce4da3b94da1753dded7a0)。

250 MHz 数字锁相环时钟（Digital Phase-Locked Loop Clock）0。

<a id="r_a996a0bfee8b89b7a03005a0aa13deb6c"></a>

```c
#define IFX_DPLL250_1 24
```

相关声明：[IFX_DPLL250_1](#a996a0bfee8b89b7a03005a0aa13deb6c)。

250 MHz 数字锁相环时钟（Digital Phase-Locked Loop Clock）1。

<a id="r_a9a0775cea1ab8b3fb1a59a8d4d8fb9a1"></a>

```c
#define IFX_DPLL500 25
```

相关声明：[IFX_DPLL500](#a9a0775cea1ab8b3fb1a59a8d4d8fb9a1)。

500 MHz 数字锁相环时钟（Digital Phase-Locked Loop Clock）。

<a id="r_a8e8256e246b0b6bdfc547b29bd858e39"></a>

```c
#define IFX_CLK_HF_NO_DIVIDE 0
```

相关声明：[IFX_CLK_HF_NO_DIVIDE](#a8e8256e246b0b6bdfc547b29bd858e39)。

不对 clkHf 分频（Don't Divide）。

<a id="r_ac114b01616b9a42be97dc91c8e076e3c"></a>

```c
#define IFX_CLK_HF_DIVIDE_BY_2 1
```

相关声明：[IFX_CLK_HF_DIVIDE_BY_2](#ac114b01616b9a42be97dc91c8e076e3c)。

对 clkHf 进行 2 分频（Divide）。

<a id="r_a90368d9af6f4b88fe712f5dec6825e51"></a>

```c
#define IFX_CLK_HF_DIVIDE_BY_3 2
```

相关声明：[IFX_CLK_HF_DIVIDE_BY_3](#a90368d9af6f4b88fe712f5dec6825e51)。

对 clkHf 进行 3 分频（Divide）。

<a id="r_a50a4eb76c91ffb9d8897b8c74cfbe89c"></a>

```c
#define IFX_CLK_HF_DIVIDE_BY_4 3
```

相关声明：[IFX_CLK_HF_DIVIDE_BY_4](#a50a4eb76c91ffb9d8897b8c74cfbe89c)。

对 clkHf 进行 4 分频（Divide）。

<a id="r_aa775c7352b91713bd32431a5ce94aef7"></a>

```c
#define IFX_CLK_HF_DIVIDE_BY_5 4
```

相关声明：[IFX_CLK_HF_DIVIDE_BY_5](#aa775c7352b91713bd32431a5ce94aef7)。

对 clkHf 进行 5 分频（Divide）。

<a id="r_ae9b2f34ffe8068803d72df3a14b65585"></a>

```c
#define IFX_CLK_HF_DIVIDE_BY_6 5
```

相关声明：[IFX_CLK_HF_DIVIDE_BY_6](#ae9b2f34ffe8068803d72df3a14b65585)。

对 clkHf 进行 6 分频（Divide）。

<a id="r_a5841a8ad50fad2fdda18e580a086fbe8"></a>

```c
#define IFX_CLK_HF_DIVIDE_BY_7 6
```

相关声明：[IFX_CLK_HF_DIVIDE_BY_7](#a5841a8ad50fad2fdda18e580a086fbe8)。

对 clkHf 进行 7 分频（Divide）。

<a id="r_a2ac1176aac2a454cd46cd749afd51f38"></a>

```c
#define IFX_CLK_HF_DIVIDE_BY_8 7
```

相关声明：[IFX_CLK_HF_DIVIDE_BY_8](#a2ac1176aac2a454cd46cd749afd51f38)。

对 clkHf 进行 8 分频（Divide）。

<a id="r_a9ac427b54d06959a9d0757995fca7748"></a>

```c
#define IFX_CLK_HF_DIVIDE_BY_9 8
```

相关声明：[IFX_CLK_HF_DIVIDE_BY_9](#a9ac427b54d06959a9d0757995fca7748)。

对 clkHf 进行 9 分频（Divide）。

<a id="r_a127df887b725f586b652db5b318ad85d"></a>

```c
#define IFX_CLK_HF_DIVIDE_BY_10 9
```

相关声明：[IFX_CLK_HF_DIVIDE_BY_10](#a127df887b725f586b652db5b318ad85d)。

对 clkHf 进行 10 分频（Divide）。

<a id="r_af4e389c8fda028b87c05680271a88d81"></a>

```c
#define IFX_CLK_HF_DIVIDE_BY_11 10
```

相关声明：[IFX_CLK_HF_DIVIDE_BY_11](#af4e389c8fda028b87c05680271a88d81)。

对 clkHf 进行 11 分频（Divide）。

<a id="r_a1dea7ec244b65878790bec7f045b1659"></a>

```c
#define IFX_CLK_HF_DIVIDE_BY_12 11
```

相关声明：[IFX_CLK_HF_DIVIDE_BY_12](#a1dea7ec244b65878790bec7f045b1659)。

对 clkHf 进行 12 分频（Divide）。

<a id="r_aa9031a287c3b36a2a594699a62234950"></a>

```c
#define IFX_CLK_HF_DIVIDE_BY_13 12
```

相关声明：[IFX_CLK_HF_DIVIDE_BY_13](#aa9031a287c3b36a2a594699a62234950)。

对 clkHf 进行 13 分频（Divide）。

<a id="r_af25bd9a1e157dcd847aace3d89d0c27c"></a>

```c
#define IFX_CLK_HF_DIVIDE_BY_14 13
```

相关声明：[IFX_CLK_HF_DIVIDE_BY_14](#af25bd9a1e157dcd847aace3d89d0c27c)。

对 clkHf 进行 14 分频（Divide）。

<a id="r_af62f613a4572d32c9eb88437c0f858cc"></a>

```c
#define IFX_CLK_HF_DIVIDE_BY_15 14
```

相关声明：[IFX_CLK_HF_DIVIDE_BY_15](#af62f613a4572d32c9eb88437c0f858cc)。

对 clkHf 进行 15 分频（Divide）。

<a id="r_ae0e3bbd6837bb0f188c84f980686f4f5"></a>

```c
#define IFX_CLK_HF_DIVIDE_BY_16 15
```

相关声明：[IFX_CLK_HF_DIVIDE_BY_16](#ae0e3bbd6837bb0f188c84f980686f4f5)。

对 clkHf 进行 16 分频（Divide）。

<a id="r_a4a491df909271cca9d94c236fb8aa023"></a>

```c
#define IFX_CLK_HF_MAX_DIVIDER
```

相关声明：[IFX_CLK_HF_MAX_DIVIDER](#a4a491df909271cca9d94c236fb8aa023)。

最大分频值（Max Divider）。

<a id="r_af97fc461523235af01c1b7a679f24779"></a>

```c
#define IFX_CLK_HF_IN_CLKPATH0 0
```

相关声明：[IFX_CLK_HF_IN_CLKPATH0](#af97fc461523235af01c1b7a679f24779)。

clkHf 输入为时钟路径（Clock Path）0。

<a id="r_a2af552cd6bc57510084f3d3c5cf4ff77"></a>

```c
#define IFX_CLK_HF_IN_CLKPATH1 1
```

相关声明：[IFX_CLK_HF_IN_CLKPATH1](#a2af552cd6bc57510084f3d3c5cf4ff77)。

clkHf 输入为时钟路径（Clock Path）1。

<a id="r_afdbce4bc2914f753b3c1676ee57631cf"></a>

```c
#define IFX_CLK_HF_IN_CLKPATH2 2
```

相关声明：[IFX_CLK_HF_IN_CLKPATH2](#afdbce4bc2914f753b3c1676ee57631cf)。

clkHf 输入为时钟路径（Clock Path）2。

<a id="r_a14c19d3d33a0b0b69aa126c930d0b925"></a>

```c
#define IFX_CLK_HF_IN_CLKPATH3 3
```

相关声明：[IFX_CLK_HF_IN_CLKPATH3](#a14c19d3d33a0b0b69aa126c930d0b925)。

clkHf 输入为时钟路径（Clock Path）3。

<a id="r_a44e73293a38c21756b0a1d3e2f306784"></a>

```c
#define IFX_CLK_HF_IN_CLKPATH4 4
```

相关声明：[IFX_CLK_HF_IN_CLKPATH4](#a44e73293a38c21756b0a1d3e2f306784)。

clkHf 输入为时钟路径（Clock Path）4。

<a id="r_a9e6e7de3ca92a56813b3386a815f3302"></a>

```c
#define IFX_CLK_HF_IN_CLKPATH5 5
```

相关声明：[IFX_CLK_HF_IN_CLKPATH5](#a9e6e7de3ca92a56813b3386a815f3302)。

clkHf 输入为时钟路径（Clock Path）5。

<a id="r_a9422b8731269576895683a08de8761bd"></a>

```c
#define IFX_CLK_HF_IN_CLKPATH6 6
```

相关声明：[IFX_CLK_HF_IN_CLKPATH6](#a9422b8731269576895683a08de8761bd)。

clkHf 输入为时钟路径（Clock Path）6。

<a id="r_a9a9f309bbda54573d284cf827b5a8431"></a>

```c
#define IFX_CLK_HF_IN_CLKPATH7 7
```

相关声明：[IFX_CLK_HF_IN_CLKPATH7](#a9a9f309bbda54573d284cf827b5a8431)。

clkHf 输入为时钟路径（Clock Path）7。

<a id="r_a42d31daafb7edd119917b2d64fed7d13"></a>

```c
#define IFX_CLK_HF_IN_CLKPATH8 8
```

相关声明：[IFX_CLK_HF_IN_CLKPATH8](#a42d31daafb7edd119917b2d64fed7d13)。

clkHf 输入为时钟路径（Clock Path）8。

<a id="r_a30e1d352340f3260780a5ecb41c271d8"></a>

```c
#define IFX_CLK_HF_IN_CLKPATH9 9
```

相关声明：[IFX_CLK_HF_IN_CLKPATH9](#a30e1d352340f3260780a5ecb41c271d8)。

clkHf 输入为时钟路径（Clock Path）9。

<a id="r_afb88718549e2d3bd819c193b22b595ef"></a>

```c
#define IFX_CLK_HF_IN_CLKPATH10 10
```

相关声明：[IFX_CLK_HF_IN_CLKPATH10](#afb88718549e2d3bd819c193b22b595ef)。

clkHf 输入为时钟路径（Clock Path）10。

<a id="r_aceb482f9abf62c39dfa6c493d7b35214"></a>

```c
#define IFX_CLK_HF_IN_CLKPATH11 11
```

相关声明：[IFX_CLK_HF_IN_CLKPATH11](#aceb482f9abf62c39dfa6c493d7b35214)。

clkHf 输入为时钟路径（Clock Path）11。

<a id="r_ab78be9ee95bb8ef670fadcbe510143df"></a>

```c
#define IFX_CLK_HF_IN_CLKPATH12 12
```

相关声明：[IFX_CLK_HF_IN_CLKPATH12](#ab78be9ee95bb8ef670fadcbe510143df)。

clkHf 输入为时钟路径（Clock Path）12。

<a id="r_aaf0ffc5fc2430509009d9be5caa993e0"></a>

```c
#define IFX_CLK_HF_IN_CLKPATH13 13
```

相关声明：[IFX_CLK_HF_IN_CLKPATH13](#aaf0ffc5fc2430509009d9be5caa993e0)。

clkHf 输入为时钟路径（Clock Path）13。

<a id="r_a775de46989fda63e39c373d98d33cdd4"></a>

```c
#define IFX_CLK_HF_IN_CLKPATH14 14
```

相关声明：[IFX_CLK_HF_IN_CLKPATH14](#a775de46989fda63e39c373d98d33cdd4)。

clkHf 输入为时钟路径（Clock Path）14。

<a id="r_ad0f4130f6f16e483e6ad25c86d69c73a"></a>

```c
#define IFX_CLK_HF_IN_CLKPATH15 15
```

相关声明：[IFX_CLK_HF_IN_CLKPATH15](#ad0f4130f6f16e483e6ad25c86d69c73a)。

clkHf 输入为时钟路径（Clock Path）15。

<a id="r_a2e4170dfe8857dc1a6dcb4c24339ad58"></a>

```c
#define IFX_RSC_ADC 0
```

相关声明：[IFX_RSC_ADC](#a2e4170dfe8857dc1a6dcb4c24339ad58)。

模数转换器（Analog to Digital Converter）。

<a id="r_ad99213da9ea7aca696b4afcc962fcfc1"></a>

```c
#define IFX_RSC_ADCMIC 1
```

相关声明：[IFX_RSC_ADCMIC](#ad99213da9ea7aca696b4afcc962fcfc1)。

支持模拟麦克风（Analog Mic）的模数转换器（Analog to Digital Converter）。

<a id="r_a47ca5784064e3067e25cc96cf7fe4545"></a>

```c
#define IFX_RSC_BLESS 2
```

相关声明：[IFX_RSC_BLESS](#a47ca5784064e3067e25cc96cf7fe4545)。

蓝牙通信模块（Bluetooth Communications Block）。

<a id="r_a082980609d7da0740b2aebbe4ebb01c8"></a>

```c
#define IFX_RSC_CAN 3
```

相关声明：[IFX_RSC_CAN](#a082980609d7da0740b2aebbe4ebb01c8)。

CAN 通信模块（CAN Communication Block）。

<a id="r_abc920e3e2a59b28c9eb5dcca3dfa6753"></a>

```c
#define IFX_RSC_CLKPATH 4
```

相关声明：[IFX_RSC_CLKPATH](#abc920e3e2a59b28c9eb5dcca3dfa6753)。

时钟路径（Clock Path）。

<a id="r_a158dc83a8646125c1973dd1e138a2c34"></a>

```c
#define IFX_RSC_CLOCK 5
```

相关声明：[IFX_RSC_CLOCK](#a158dc83a8646125c1973dd1e138a2c34)。

时钟（Clock）。

<a id="r_ad48fa2184edbe314494c522693ba4d03"></a>

```c
#define IFX_RSC_CRYPTO 6
```

相关声明：[IFX_RSC_CRYPTO](#ad48fa2184edbe314494c522693ba4d03)。

密码运算硬件加速器（Crypto Hardware Accelerator）。

<a id="r_a0a1cb2f3bf6015595db3d0454fb3fba8"></a>

```c
#define IFX_RSC_DAC 7
```

相关声明：[IFX_RSC_DAC](#a0a1cb2f3bf6015595db3d0454fb3fba8)。

数模转换器（Digital to Analog Converter）。

<a id="r_a079a703a1306ffc478d5b16672599530"></a>

```c
#define IFX_RSC_DMA 8
```

相关声明：[IFX_RSC_DMA](#a079a703a1306ffc478d5b16672599530)。

DMA 控制器。

<a id="r_a8209bb0d30f5a4b6cec049caf01c24cb"></a>

```c
#define IFX_RSC_DW 9
```

相关声明：[IFX_RSC_DW](#a8209bb0d30f5a4b6cec049caf01c24cb)。

Datawire 直接存储器访问控制器（DMA Controller）。

<a id="r_acfdb9528a17469787119d41f363a3574"></a>

```c
#define IFX_RSC_ETH 10
```

相关声明：[IFX_RSC_ETH](#acfdb9528a17469787119d41f363a3574)。

以太网通信模块（Ethernet Communications Block）。

<a id="r_a64da74bea090de80048e0ff74b2b7b49"></a>

```c
#define IFX_RSC_GPIO 11
```

相关声明：[IFX_RSC_GPIO](#a64da74bea090de80048e0ff74b2b7b49)。

通用输入输出引脚（General Purpose I/O Pin）。

<a id="r_a7bf2840430923510e26ba2a5112bf57a"></a>

```c
#define IFX_RSC_I2S 12
```

相关声明：[IFX_RSC_I2S](#a7bf2840430923510e26ba2a5112bf57a)。

I2S 通信模块（I2S Communications Block）。

<a id="r_a6818a423d2ba6e14f6d68de0d043f056"></a>

```c
#define IFX_RSC_I3C 13
```

相关声明：[IFX_RSC_I3C](#a6818a423d2ba6e14f6d68de0d043f056)。

I3C 通信模块（I3C Communications Block）。

<a id="r_a7c19933d8d4b74d4f9d465ae84ae662f"></a>

```c
#define IFX_RSC_KEYSCAN 14
```

相关声明：[IFX_RSC_KEYSCAN](#a7c19933d8d4b74d4f9d465ae84ae662f)。

按键扫描模块（KeyScan Block）。

<a id="r_a6b384a0a278754542c7b4252c9f4f32e"></a>

```c
#define IFX_RSC_LCD 15
```

相关声明：[IFX_RSC_LCD](#a6b384a0a278754542c7b4252c9f4f32e)。

段式液晶显示控制器（Segment LCD Controller）。

<a id="r_af6bff078b29e69de557d8f05c6715631"></a>

```c
#define IFX_RSC_LIN 16
```

相关声明：[IFX_RSC_LIN](#af6bff078b29e69de557d8f05c6715631)。

LIN 通信模块（LIN Communications Block）。

<a id="r_abe0fa5eca8da40654655e0edade97def"></a>

```c
#define IFX_RSC_LPCOMP 17
```

相关声明：[IFX_RSC_LPCOMP](#abe0fa5eca8da40654655e0edade97def)。

低功耗比较器（Low Power Comparator）。

<a id="r_a820fa8ed2801050c0692e4d61b19f48a"></a>

```c
#define IFX_RSC_LPTIMER 18
```

相关声明：[IFX_RSC_LPTIMER](#a820fa8ed2801050c0692e4d61b19f48a)。

低功耗定时器（Low Power Timer）。

<a id="r_a7a99c7818d475e46b674cfcefcbe72c9"></a>

```c
#define IFX_RSC_OPAMP 19
```

相关声明：[IFX_RSC_OPAMP](#a7a99c7818d475e46b674cfcefcbe72c9)。

运算放大器（Opamp）。

<a id="r_ad9787dd7db77fe434ef22f3c40bd160c"></a>

```c
#define IFX_RSC_PDM 20
```

相关声明：[IFX_RSC_PDM](#ad9787dd7db77fe434ef22f3c40bd160c)。

PCM／PDM 通信模块（PCM/PDM Communications Block）。

<a id="r_a5bb46ffc627b5a436b8744e85e558cf0"></a>

```c
#define IFX_RSC_PTC 21
```

相关声明：[IFX_RSC_PTC](#a5bb46ffc627b5a436b8744e85e558cf0)。

可编程阈值比较器（Programmable Threshold Comparator）。

<a id="r_a43d0f062d4fee74dca569ffaabdef027"></a>

```c
#define IFX_RSC_SMIF 22
```

相关声明：[IFX_RSC_SMIF](#a43d0f062d4fee74dca569ffaabdef027)。

四线 SPI 通信模块（Quad-SPI Communications Block）。

<a id="r_a153379132b3cb02186560435e49236d7"></a>

```c
#define IFX_RSC_RTC 23
```

相关声明：[IFX_RSC_RTC](#a153379132b3cb02186560435e49236d7)。

实时时钟（Real Time Clock）。

<a id="r_a3751fafc8748b4e7e5369fac26abc8db"></a>

```c
#define IFX_RSC_SCB 24
```

相关声明：[IFX_RSC_SCB](#a3751fafc8748b4e7e5369fac26abc8db)。

串行通信模块（Serial Communications Block）。

<a id="r_ae825a884d1e02ade21a382fa09dde0dd"></a>

```c
#define IFX_RSC_SDHC 25
```

相关声明：[IFX_RSC_SDHC](#ae825a884d1e02ade21a382fa09dde0dd)。

SD 主机控制器（SD Host Controller）。

<a id="r_a4db1afb4bfa749be038eabc494fca7be"></a>

```c
#define IFX_RSC_SDIODEV 26
```

相关声明：[IFX_RSC_SDIODEV](#a4db1afb4bfa749be038eabc494fca7be)。

SDIO 设备模块（SDIO Device Block）。

<a id="r_ace4fb390b9200de639bb03c4f3acb2ae"></a>

```c
#define IFX_RSC_TCPWM 27
```

相关声明：[IFX_RSC_TCPWM](#ace4fb390b9200de639bb03c4f3acb2ae)。

定时器／计数器／脉宽调制模块（Timer/Counter/PWM Block）。

<a id="r_aa16d4d123204657f4e244101cfcabac9"></a>

```c
#define IFX_RSC_TDM 28
```

相关声明：[IFX_RSC_TDM](#aa16d4d123204657f4e244101cfcabac9)。

时分复用模块（TDM Block）。

<a id="r_ae8244fb817e9eff19699be7c00bcff91"></a>

```c
#define IFX_RSC_UDB 29
```

相关声明：[IFX_RSC_UDB](#ae8244fb817e9eff19699be7c00bcff91)。

通用数字模块阵列（UDB Array）。

<a id="r_ae30ac1e48cb64cbec1c73914af56ce67"></a>

```c
#define IFX_RSC_USB 30
```

相关声明：[IFX_RSC_USB](#ae30ac1e48cb64cbec1c73914af56ce67)。

USB 通信模块（USB Communication Block）。

<a id="r_a578d999bf58c60fa222699302f1c3bc7"></a>

```c
#define IFX_RSC_INVALID 31
```

相关声明：[IFX_RSC_INVALID](#a578d999bf58c60fa222699302f1c3bc7)。

无效类型占位符（Placeholder for Invalid Type）。

## 5.2\_详细说明（Detailed Documentation）

<a id="aa7e0a35b9b7f5c90d0b2219eba034535"></a>

### `CLK_SOURCE_IHO`

```c
#define CLK_SOURCE_IHO
```

<a id="a0d94d3c9bace1fd8d01ef24ffb7ce054"></a>

### `CLK_SOURCE_PILO`

```c
#define CLK_SOURCE_PILO
```

<a id="a17fab77216c09df141a7ef22204d4d52"></a>

### `IFX_ALT_SYS_TICK`

```c
#define IFX_ALT_SYS_TICK 21
```

备用 SysTick 时钟（Alternative SysTick Clock）。

<a id="aacf4257c7f77ca37ee9f88af68a290d0"></a>

### `IFX_ALTHF`

```c
#define IFX_ALTHF 5
```

备用高频输入时钟（Alternate High Frequency Input Clock）。

<a id="a0d7f68bb0c80aaf9f9af80fcef93000f"></a>

### `IFX_ALTLF`

```c
#define IFX_ALTLF 6
```

备用低频输入时钟（Alternate Low Frequency Input Clock）。

<a id="a13c3737f1df2b3b07aeb3ce626d51077"></a>

### `IFX_BAK`

```c
#define IFX_BAK 20
```

备份电源域时钟（Backup Power Domain Clock）。

<a id="a127df887b725f586b652db5b318ad85d"></a>

### `IFX_CLK_HF_DIVIDE_BY_10`

```c
#define IFX_CLK_HF_DIVIDE_BY_10 9
```

对 clkHf 进行 10 分频（Divide）。

<a id="af4e389c8fda028b87c05680271a88d81"></a>

### `IFX_CLK_HF_DIVIDE_BY_11`

```c
#define IFX_CLK_HF_DIVIDE_BY_11 10
```

对 clkHf 进行 11 分频（Divide）。

<a id="a1dea7ec244b65878790bec7f045b1659"></a>

### `IFX_CLK_HF_DIVIDE_BY_12`

```c
#define IFX_CLK_HF_DIVIDE_BY_12 11
```

对 clkHf 进行 12 分频（Divide）。

<a id="aa9031a287c3b36a2a594699a62234950"></a>

### `IFX_CLK_HF_DIVIDE_BY_13`

```c
#define IFX_CLK_HF_DIVIDE_BY_13 12
```

对 clkHf 进行 13 分频（Divide）。

<a id="af25bd9a1e157dcd847aace3d89d0c27c"></a>

### `IFX_CLK_HF_DIVIDE_BY_14`

```c
#define IFX_CLK_HF_DIVIDE_BY_14 13
```

对 clkHf 进行 14 分频（Divide）。

<a id="af62f613a4572d32c9eb88437c0f858cc"></a>

### `IFX_CLK_HF_DIVIDE_BY_15`

```c
#define IFX_CLK_HF_DIVIDE_BY_15 14
```

对 clkHf 进行 15 分频（Divide）。

<a id="ae0e3bbd6837bb0f188c84f980686f4f5"></a>

### `IFX_CLK_HF_DIVIDE_BY_16`

```c
#define IFX_CLK_HF_DIVIDE_BY_16 15
```

对 clkHf 进行 16 分频（Divide）。

<a id="ac114b01616b9a42be97dc91c8e076e3c"></a>

### `IFX_CLK_HF_DIVIDE_BY_2`

```c
#define IFX_CLK_HF_DIVIDE_BY_2 1
```

对 clkHf 进行 2 分频（Divide）。

<a id="a90368d9af6f4b88fe712f5dec6825e51"></a>

### `IFX_CLK_HF_DIVIDE_BY_3`

```c
#define IFX_CLK_HF_DIVIDE_BY_3 2
```

对 clkHf 进行 3 分频（Divide）。

<a id="a50a4eb76c91ffb9d8897b8c74cfbe89c"></a>

### `IFX_CLK_HF_DIVIDE_BY_4`

```c
#define IFX_CLK_HF_DIVIDE_BY_4 3
```

对 clkHf 进行 4 分频（Divide）。

<a id="aa775c7352b91713bd32431a5ce94aef7"></a>

### `IFX_CLK_HF_DIVIDE_BY_5`

```c
#define IFX_CLK_HF_DIVIDE_BY_5 4
```

对 clkHf 进行 5 分频（Divide）。

<a id="ae9b2f34ffe8068803d72df3a14b65585"></a>

### `IFX_CLK_HF_DIVIDE_BY_6`

```c
#define IFX_CLK_HF_DIVIDE_BY_6 5
```

对 clkHf 进行 6 分频（Divide）。

<a id="a5841a8ad50fad2fdda18e580a086fbe8"></a>

### `IFX_CLK_HF_DIVIDE_BY_7`

```c
#define IFX_CLK_HF_DIVIDE_BY_7 6
```

对 clkHf 进行 7 分频（Divide）。

<a id="a2ac1176aac2a454cd46cd749afd51f38"></a>

### `IFX_CLK_HF_DIVIDE_BY_8`

```c
#define IFX_CLK_HF_DIVIDE_BY_8 7
```

对 clkHf 进行 8 分频（Divide）。

<a id="a9ac427b54d06959a9d0757995fca7748"></a>

### `IFX_CLK_HF_DIVIDE_BY_9`

```c
#define IFX_CLK_HF_DIVIDE_BY_9 8
```

对 clkHf 进行 9 分频（Divide）。

<a id="af97fc461523235af01c1b7a679f24779"></a>

### `IFX_CLK_HF_IN_CLKPATH0`

```c
#define IFX_CLK_HF_IN_CLKPATH0 0
```

clkHf 输入为时钟路径（Clock Path）0。

<a id="a2af552cd6bc57510084f3d3c5cf4ff77"></a>

### `IFX_CLK_HF_IN_CLKPATH1`

```c
#define IFX_CLK_HF_IN_CLKPATH1 1
```

clkHf 输入为时钟路径（Clock Path）1。

<a id="afb88718549e2d3bd819c193b22b595ef"></a>

### `IFX_CLK_HF_IN_CLKPATH10`

```c
#define IFX_CLK_HF_IN_CLKPATH10 10
```

clkHf 输入为时钟路径（Clock Path）10。

<a id="aceb482f9abf62c39dfa6c493d7b35214"></a>

### `IFX_CLK_HF_IN_CLKPATH11`

```c
#define IFX_CLK_HF_IN_CLKPATH11 11
```

clkHf 输入为时钟路径（Clock Path）11。

<a id="ab78be9ee95bb8ef670fadcbe510143df"></a>

### `IFX_CLK_HF_IN_CLKPATH12`

```c
#define IFX_CLK_HF_IN_CLKPATH12 12
```

clkHf 输入为时钟路径（Clock Path）12。

<a id="aaf0ffc5fc2430509009d9be5caa993e0"></a>

### `IFX_CLK_HF_IN_CLKPATH13`

```c
#define IFX_CLK_HF_IN_CLKPATH13 13
```

clkHf 输入为时钟路径（Clock Path）13。

<a id="a775de46989fda63e39c373d98d33cdd4"></a>

### `IFX_CLK_HF_IN_CLKPATH14`

```c
#define IFX_CLK_HF_IN_CLKPATH14 14
```

clkHf 输入为时钟路径（Clock Path）14。

<a id="ad0f4130f6f16e483e6ad25c86d69c73a"></a>

### `IFX_CLK_HF_IN_CLKPATH15`

```c
#define IFX_CLK_HF_IN_CLKPATH15 15
```

clkHf 输入为时钟路径（Clock Path）15。

<a id="afdbce4bc2914f753b3c1676ee57631cf"></a>

### `IFX_CLK_HF_IN_CLKPATH2`

```c
#define IFX_CLK_HF_IN_CLKPATH2 2
```

clkHf 输入为时钟路径（Clock Path）2。

<a id="a14c19d3d33a0b0b69aa126c930d0b925"></a>

### `IFX_CLK_HF_IN_CLKPATH3`

```c
#define IFX_CLK_HF_IN_CLKPATH3 3
```

clkHf 输入为时钟路径（Clock Path）3。

<a id="a44e73293a38c21756b0a1d3e2f306784"></a>

### `IFX_CLK_HF_IN_CLKPATH4`

```c
#define IFX_CLK_HF_IN_CLKPATH4 4
```

clkHf 输入为时钟路径（Clock Path）4。

<a id="a9e6e7de3ca92a56813b3386a815f3302"></a>

### `IFX_CLK_HF_IN_CLKPATH5`

```c
#define IFX_CLK_HF_IN_CLKPATH5 5
```

clkHf 输入为时钟路径（Clock Path）5。

<a id="a9422b8731269576895683a08de8761bd"></a>

### `IFX_CLK_HF_IN_CLKPATH6`

```c
#define IFX_CLK_HF_IN_CLKPATH6 6
```

clkHf 输入为时钟路径（Clock Path）6。

<a id="a9a9f309bbda54573d284cf827b5a8431"></a>

### `IFX_CLK_HF_IN_CLKPATH7`

```c
#define IFX_CLK_HF_IN_CLKPATH7 7
```

clkHf 输入为时钟路径（Clock Path）7。

<a id="a42d31daafb7edd119917b2d64fed7d13"></a>

### `IFX_CLK_HF_IN_CLKPATH8`

```c
#define IFX_CLK_HF_IN_CLKPATH8 8
```

clkHf 输入为时钟路径（Clock Path）8。

<a id="a30e1d352340f3260780a5ecb41c271d8"></a>

### `IFX_CLK_HF_IN_CLKPATH9`

```c
#define IFX_CLK_HF_IN_CLKPATH9 9
```

clkHf 输入为时钟路径（Clock Path）9。

<a id="a4a491df909271cca9d94c236fb8aa023"></a>

### `IFX_CLK_HF_MAX_DIVIDER`

```c
#define IFX_CLK_HF_MAX_DIVIDER
```

最大分频值（Max Divider）。

<a id="a8e8256e246b0b6bdfc547b29bd858e39"></a>

### `IFX_CLK_HF_NO_DIVIDE`

```c
#define IFX_CLK_HF_NO_DIVIDE 0
```

不对 clkHf 分频（Don't Divide）。

<a id="aa410e1f3f4ce4da3b94da1753dded7a0"></a>

### `IFX_DPLL250_0`

```c
#define IFX_DPLL250_0 23
```

250 MHz 数字锁相环时钟（Digital Phase-Locked Loop Clock）0。

<a id="a996a0bfee8b89b7a03005a0aa13deb6c"></a>

### `IFX_DPLL250_1`

```c
#define IFX_DPLL250_1 24
```

250 MHz 数字锁相环时钟（Digital Phase-Locked Loop Clock）1。

<a id="a9a0775cea1ab8b3fb1a59a8d4d8fb9a1"></a>

### `IFX_DPLL500`

```c
#define IFX_DPLL500 25
```

500 MHz 数字锁相环时钟（Digital Phase-Locked Loop Clock）。

<a id="add35b90080781e8214d8a6e42b596357"></a>

### `IFX_ECO`

```c
#define IFX_ECO 3
```

外部晶体振荡器输入时钟（External Crystal Oscillator Input Clock）。

<a id="ae9ff69341c23a2a343d1e8100899a10b"></a>

### `IFX_ECO_PRESCALER`

```c
#define IFX_ECO_PRESCALER 15
```

ECO 预分频器（Prescaler Divider）。

<a id="a0732d901f72ef098547c253a39ffb7fc"></a>

### `IFX_EXT`

```c
#define IFX_EXT 4
```

外部输入时钟（External Input Clock）。

<a id="ac9eefaa7728fa6cf3c93b4f3876a5207"></a>

### `IFX_FLL`

```c
#define IFX_FLL 12
```

锁频环时钟（Frequency-Locked Loop Clock）。

<a id="a12860926bf5ecc84c7a616934e31281d"></a>

### `IFX_HF`

```c
#define IFX_HF 18
```

高频时钟（High Frequency Clock）。

<a id="aa315d0f29d56dcaa2e269acd72f94f6e"></a>

### `IFX_IHO`

```c
#define IFX_IHO 1
```

内部高速振荡器输入时钟（Internal High Speed Oscillator Input Clock）。

<a id="a8f4d9bccb15b7e30be213445f6a52942"></a>

### `IFX_ILO`

```c
#define IFX_ILO 7
```

内部低速振荡器输入时钟（Internal Low Speed Oscillator Input Clock）。

<a id="ad91e918e9d8832918e338ee0d932eca2"></a>

### `IFX_IMO`

```c
#define IFX_IMO 2
```

内部主振荡器输入时钟（Internal Main Oscillator Input Clock）。

<a id="a535be3b20328c21862a5cd555caef943"></a>

### `IFX_LF`

```c
#define IFX_LF 16
```

低频时钟（Low Frequency Clock）。

<a id="ac77c21b36967d2b4e02113f280d280bb"></a>

### `IFX_MF`

```c
#define IFX_MF 17
```

中频时钟（Medium Frequency Clock）。

<a id="adcfe0437bcfd3066970858a7001f348d"></a>

### `IFX_MFO`

```c
#define IFX_MFO 10
```

中频振荡器时钟（Medium Frequency Oscillator Clock）。

<a id="a4dc7db5c4d08c2c0441296c0e5887201"></a>

### `IFX_PATHMUX`

```c
#define IFX_PATHMUX 11
```

FLL／PLL 输入的路径选择多路复用器（Path Selection Mux）。

<a id="ae558d9e17464ae21609aa20c496362a9"></a>

### `IFX_PERI`

```c
#define IFX_PERI 22
```

外设时钟组（Peripheral Clock Group）。

<a id="a1a42be76091c654e98ae49ea5613f552"></a>

### `IFX_PILO`

```c
#define IFX_PILO 8
```

精密内部低速振荡器输入时钟（Precision ILO Input Clock）。

<a id="ae3d0dd2c94d0b8c1c52c9d9a044e26d7"></a>

### `IFX_PLL200`

```c
#define IFX_PLL200 13
```

200 MHz 锁相环时钟（Phase-Locked Loop Clock）。

<a id="ad2b34fff09debe25b12c59ddae66b8ea"></a>

### `IFX_PLL400`

```c
#define IFX_PLL400 14
```

400 MHz 锁相环时钟（Phase-Locked Loop Clock）。

<a id="aa6f99fee380cdd367dc727d422717754"></a>

### `IFX_PUMP`

```c
#define IFX_PUMP 19
```

模拟泵时钟（Analog Pump Clock）。

<a id="a2e4170dfe8857dc1a6dcb4c24339ad58"></a>

### `IFX_RSC_ADC`

```c
#define IFX_RSC_ADC 0
```

模数转换器（Analog to Digital Converter）。

<a id="ad99213da9ea7aca696b4afcc962fcfc1"></a>

### `IFX_RSC_ADCMIC`

```c
#define IFX_RSC_ADCMIC 1
```

支持模拟麦克风（Analog Mic）的模数转换器（Analog to Digital Converter）。

<a id="a47ca5784064e3067e25cc96cf7fe4545"></a>

### `IFX_RSC_BLESS`

```c
#define IFX_RSC_BLESS 2
```

蓝牙通信模块（Bluetooth Communications Block）。

<a id="a082980609d7da0740b2aebbe4ebb01c8"></a>

### `IFX_RSC_CAN`

```c
#define IFX_RSC_CAN 3
```

CAN 通信模块（CAN Communication Block）。

<a id="abc920e3e2a59b28c9eb5dcca3dfa6753"></a>

### `IFX_RSC_CLKPATH`

```c
#define IFX_RSC_CLKPATH 4
```

时钟路径（Clock Path）。

已弃用（DEPRECATED）。

<a id="a158dc83a8646125c1973dd1e138a2c34"></a>

### `IFX_RSC_CLOCK`

```c
#define IFX_RSC_CLOCK 5
```

时钟（Clock）。

<a id="ad48fa2184edbe314494c522693ba4d03"></a>

### `IFX_RSC_CRYPTO`

```c
#define IFX_RSC_CRYPTO 6
```

密码运算硬件加速器（Crypto Hardware Accelerator）。

<a id="a0a1cb2f3bf6015595db3d0454fb3fba8"></a>

### `IFX_RSC_DAC`

```c
#define IFX_RSC_DAC 7
```

数模转换器（Digital to Analog Converter）。

<a id="a079a703a1306ffc478d5b16672599530"></a>

### `IFX_RSC_DMA`

```c
#define IFX_RSC_DMA 8
```

DMA 控制器。

<a id="a8209bb0d30f5a4b6cec049caf01c24cb"></a>

### `IFX_RSC_DW`

```c
#define IFX_RSC_DW 9
```

Datawire 直接存储器访问控制器（DMA Controller）。

<a id="acfdb9528a17469787119d41f363a3574"></a>

### `IFX_RSC_ETH`

```c
#define IFX_RSC_ETH 10
```

以太网通信模块（Ethernet Communications Block）。

<a id="a64da74bea090de80048e0ff74b2b7b49"></a>

### `IFX_RSC_GPIO`

```c
#define IFX_RSC_GPIO 11
```

通用输入输出引脚（General Purpose I/O Pin）。

<a id="a7bf2840430923510e26ba2a5112bf57a"></a>

### `IFX_RSC_I2S`

```c
#define IFX_RSC_I2S 12
```

I2S 通信模块（I2S Communications Block）。

<a id="a6818a423d2ba6e14f6d68de0d043f056"></a>

### `IFX_RSC_I3C`

```c
#define IFX_RSC_I3C 13
```

I3C 通信模块（I3C Communications Block）。

<a id="a578d999bf58c60fa222699302f1c3bc7"></a>

### `IFX_RSC_INVALID`

```c
#define IFX_RSC_INVALID 31
```

无效类型占位符（Placeholder for Invalid Type）。

<a id="a7c19933d8d4b74d4f9d465ae84ae662f"></a>

### `IFX_RSC_KEYSCAN`

```c
#define IFX_RSC_KEYSCAN 14
```

按键扫描模块（KeyScan Block）。

<a id="a6b384a0a278754542c7b4252c9f4f32e"></a>

### `IFX_RSC_LCD`

```c
#define IFX_RSC_LCD 15
```

段式液晶显示控制器（Segment LCD Controller）。

<a id="af6bff078b29e69de557d8f05c6715631"></a>

### `IFX_RSC_LIN`

```c
#define IFX_RSC_LIN 16
```

LIN 通信模块（LIN Communications Block）。

<a id="abe0fa5eca8da40654655e0edade97def"></a>

### `IFX_RSC_LPCOMP`

```c
#define IFX_RSC_LPCOMP 17
```

低功耗比较器（Low Power Comparator）。

<a id="a820fa8ed2801050c0692e4d61b19f48a"></a>

### `IFX_RSC_LPTIMER`

```c
#define IFX_RSC_LPTIMER 18
```

低功耗定时器（Low Power Timer）。

<a id="a7a99c7818d475e46b674cfcefcbe72c9"></a>

### `IFX_RSC_OPAMP`

```c
#define IFX_RSC_OPAMP 19
```

运算放大器（Opamp）。

<a id="ad9787dd7db77fe434ef22f3c40bd160c"></a>

### `IFX_RSC_PDM`

```c
#define IFX_RSC_PDM 20
```

PCM／PDM 通信模块（PCM/PDM Communications Block）。

<a id="a5bb46ffc627b5a436b8744e85e558cf0"></a>

### `IFX_RSC_PTC`

```c
#define IFX_RSC_PTC 21
```

可编程阈值比较器（Programmable Threshold Comparator）。

<a id="a153379132b3cb02186560435e49236d7"></a>

### `IFX_RSC_RTC`

```c
#define IFX_RSC_RTC 23
```

实时时钟（Real Time Clock）。

<a id="a3751fafc8748b4e7e5369fac26abc8db"></a>

### `IFX_RSC_SCB`

```c
#define IFX_RSC_SCB 24
```

串行通信模块（Serial Communications Block）。

<a id="ae825a884d1e02ade21a382fa09dde0dd"></a>

### `IFX_RSC_SDHC`

```c
#define IFX_RSC_SDHC 25
```

SD 主机控制器（SD Host Controller）。

<a id="a4db1afb4bfa749be038eabc494fca7be"></a>

### `IFX_RSC_SDIODEV`

```c
#define IFX_RSC_SDIODEV 26
```

SDIO 设备模块（SDIO Device Block）。

<a id="a43d0f062d4fee74dca569ffaabdef027"></a>

### `IFX_RSC_SMIF`

```c
#define IFX_RSC_SMIF 22
```

四线 SPI 通信模块（Quad-SPI Communications Block）。

<a id="ace4fb390b9200de639bb03c4f3acb2ae"></a>

### `IFX_RSC_TCPWM`

```c
#define IFX_RSC_TCPWM 27
```

定时器／计数器／脉宽调制模块（Timer/Counter/PWM Block）。

<a id="aa16d4d123204657f4e244101cfcabac9"></a>

### `IFX_RSC_TDM`

```c
#define IFX_RSC_TDM 28
```

时分复用模块（TDM Block）。

<a id="ae8244fb817e9eff19699be7c00bcff91"></a>

### `IFX_RSC_UDB`

```c
#define IFX_RSC_UDB 29
```

通用数字模块阵列（UDB Array）。

<a id="ae30ac1e48cb64cbec1c73914af56ce67"></a>

### `IFX_RSC_USB`

```c
#define IFX_RSC_USB 30
```

USB 通信模块（USB Communication Block）。

<a id="acd56b092f7a5bf486be47471884016d4"></a>

### `IFX_WCO`

```c
#define IFX_WCO 9
```

钟表晶体振荡器输入时钟（Watch Crystal Oscillator Input Clock）。


## 5.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_supplement_reference/P090_ifx_clock_source_common.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P004_zephyr__bluetooth__gatt.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__bluetooth__audio__mcs.h_文件参考.md)
