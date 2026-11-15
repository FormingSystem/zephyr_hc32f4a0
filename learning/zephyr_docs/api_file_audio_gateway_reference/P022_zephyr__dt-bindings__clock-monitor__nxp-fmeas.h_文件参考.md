---
id: learning.zephyr-docs.api-file-audio-gateway-reference.page-22
title: zephyr__dt-bindings__clock-monitor__nxp-fmeas.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nxp-fmeas_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_zephyr\_\_dt-bindings\_\_clock-monitor\_\_nxp-fmeas.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/nxp-fmeas_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

NXP BASIC FREQME（fmeas）输入使用的INPUTMUX连接标记（Connection Cookies）。

查看此文件的源码。

<a id="details"></a>

用于 NXP BASIC FREQME（fmeas）输入的 INPUTMUX 连接标识值（Connection Cookies）。这些值对应各 SoC 的 fsl_inputmux_connections.h 中的 `kINPUTMUX_<source>ToFreqmeas` 枚举项。标识值将 FMEASURE 目标多路复用器 ID（0x700）按 INPUTMUX PMUX_SHIFT（20）左移，再与各输入源的选择器值按位或组合。在设备树中，reference-sources 和 target-sources 子节点内的 mux-states = <&inputmux channel connection> 使用这些标识值作为 connection 说明符。channel 单元选择 FMEASURE_CH_SEL 槽位（0 为参考源，1 为目标源）；同一连接标识值对两个通道均有效。此连接标识值同时也是运行时 clock_monitor_set_source() 选择参考源或目标源时使用的选择器。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 22.1\_宏定义（Macros）

<a id="r_ab96238e8880faa8d5019afa50ca86b21"></a>

```c
#define NXP_FMEAS_PMUX_ID 0x700U
```

相关声明：[NXP_FMEAS_PMUX_ID](#ab96238e8880faa8d5019afa50ca86b21)。

INPUTMUX PMUX 编码中的 FMEASURE 目标多路复用器 ID（Destination Mux ID）。

<a id="r_add988805308edfadd65bb2a879d2cc4f"></a>

```c
#define NXP_FMEAS_PMUX_SHIFT 20U
```

相关声明：[NXP_FMEAS_PMUX_SHIFT](#add988805308edfadd65bb2a879d2cc4f)。

INPUTMUX 连接标识值（Cookie）中应用于 NXP_FMEAS_PMUX_ID 的移位量。

<a id="r_a5d74f0050fc7e4c3f60866eb357f0cec"></a>

```c
#define NXP_FMEAS_CONNECTION(sel)
```

相关声明：[NXP_FMEAS_CONNECTION](#a5d74f0050fc7e4c3f60866eb357f0cec)。

根据各输入源选择器 sel 构建 INPUTMUX FMEASURE 连接标识值（Cookie）。

<a id="r_a4786b637a270914245f51cabc3e97bac"></a>

```c
#define NXP_FMEAS_RT6XX_XTALIN NXP_FMEAS_CONNECTION(0)
```

相关声明：[NXP_FMEAS_RT6XX_XTALIN](#a4786b637a270914245f51cabc3e97bac)、[NXP_FMEAS_CONNECTION](#a5d74f0050fc7e4c3f60866eb357f0cec)。

RT6xx FREQME 时钟源（Source）：晶体振荡器输入（Crystal Oscillator Input，XTALIN）。

<a id="r_a02da62ca559fad494ffdbef7b64cfc0d"></a>

```c
#define NXP_FMEAS_RT6XX_SFRO NXP_FMEAS_CONNECTION(1)
```

相关声明：[NXP_FMEAS_RT6XX_SFRO](#a02da62ca559fad494ffdbef7b64cfc0d)、[NXP_FMEAS_CONNECTION](#a5d74f0050fc7e4c3f60866eb357f0cec)。

RT6xx FREQME 时钟源（Source）：低速内部 FRO（Slow Internal FRO，SFRO）。

<a id="r_ab25300603e27ac35daa28ed7ce81d146"></a>

```c
#define NXP_FMEAS_RT6XX_FFRO NXP_FMEAS_CONNECTION(2)
```

相关声明：[NXP_FMEAS_RT6XX_FFRO](#ab25300603e27ac35daa28ed7ce81d146)、[NXP_FMEAS_CONNECTION](#a5d74f0050fc7e4c3f60866eb357f0cec)。

RT6xx FREQME 时钟源（Source）：高速内部 FRO（Fast Internal FRO，FFRO）。

<a id="r_a9f42ac77b6d0f13bd9162b4f95b7fee0"></a>

```c
#define NXP_FMEAS_RT6XX_LPOSC NXP_FMEAS_CONNECTION(3)
```

相关声明：[NXP_FMEAS_RT6XX_LPOSC](#a9f42ac77b6d0f13bd9162b4f95b7fee0)、[NXP_FMEAS_CONNECTION](#a5d74f0050fc7e4c3f60866eb357f0cec)。

RT6xx FREQME 时钟源（Source）：低功耗振荡器（Low-power Oscillator，LPOSC）。

<a id="r_a679aafa6bf7960b725be79817e67b0c4"></a>

```c
#define NXP_FMEAS_RT6XX_RTC_32KHZ NXP_FMEAS_CONNECTION(4)
```

相关声明：[NXP_FMEAS_RT6XX_RTC_32KHZ](#a679aafa6bf7960b725be79817e67b0c4)、[NXP_FMEAS_CONNECTION](#a5d74f0050fc7e4c3f60866eb357f0cec)。

RT6xx FREQME 时钟源（Source）：32 kHz RTC 振荡器（Oscillator）。

<a id="r_a9b16992173eca7e0bebe2adf11eb2b32"></a>

```c
#define NXP_FMEAS_RT6XX_MAIN_SYS_CLK NXP_FMEAS_CONNECTION(5)
```

相关声明：[NXP_FMEAS_RT6XX_MAIN_SYS_CLK](#a9b16992173eca7e0bebe2adf11eb2b32)、[NXP_FMEAS_CONNECTION](#a5d74f0050fc7e4c3f60866eb357f0cec)。

RT6xx FREQME 时钟源（Source）：主系统时钟（Main System Clock）。

<a id="r_a2b5fc580ecc71519d883d12192faef84"></a>

```c
#define NXP_FMEAS_RT6XX_FREQME_GPIO_CLK NXP_FMEAS_CONNECTION(6)
```

相关声明：[NXP_FMEAS_RT6XX_FREQME_GPIO_CLK](#a2b5fc580ecc71519d883d12192faef84)、[NXP_FMEAS_CONNECTION](#a5d74f0050fc7e4c3f60866eb357f0cec)。

RT6xx FREQME 时钟源（Source）：通过 GPIO 路由的外部时钟（External Clock，FREQME_GPIO_CLK）。

<a id="r_a64aaa4f65294c66ef9833edd0e18132c"></a>

```c
#define NXP_FMEAS_RT5XX_XTALIN NXP_FMEAS_CONNECTION(0)
```

相关声明：[NXP_FMEAS_RT5XX_XTALIN](#a64aaa4f65294c66ef9833edd0e18132c)、[NXP_FMEAS_CONNECTION](#a5d74f0050fc7e4c3f60866eb357f0cec)。

RT5xx FREQME 时钟源（Source）：晶体振荡器输入（Crystal Oscillator Input，XTALIN）。

<a id="r_aca9626b1e9c76c79d219313d187b8b82"></a>

```c
#define NXP_FMEAS_RT5XX_FRO_12M NXP_FMEAS_CONNECTION(1)
```

相关声明：[NXP_FMEAS_RT5XX_FRO_12M](#aca9626b1e9c76c79d219313d187b8b82)、[NXP_FMEAS_CONNECTION](#a5d74f0050fc7e4c3f60866eb357f0cec)。

RT5xx FREQME 时钟源（Source）：12 MHz FRO。

<a id="r_a5e9af8a1241b6dd2631df6e8e0b49d40"></a>

```c
#define NXP_FMEAS_RT5XX_FRO_192M NXP_FMEAS_CONNECTION(2)
```

相关声明：[NXP_FMEAS_RT5XX_FRO_192M](#a5e9af8a1241b6dd2631df6e8e0b49d40)、[NXP_FMEAS_CONNECTION](#a5d74f0050fc7e4c3f60866eb357f0cec)。

RT5xx FREQME 时钟源（Source）：192 MHz FRO。

<a id="r_a5cc7ba765b45b8dc084e11f3171a36d5"></a>

```c
#define NXP_FMEAS_RT5XX_LPOSC NXP_FMEAS_CONNECTION(3)
```

相关声明：[NXP_FMEAS_RT5XX_LPOSC](#a5cc7ba765b45b8dc084e11f3171a36d5)、[NXP_FMEAS_CONNECTION](#a5d74f0050fc7e4c3f60866eb357f0cec)。

RT5xx FREQME 时钟源（Source）：低功耗振荡器（Low-power Oscillator，LPOSC）。

<a id="r_abfbd16b3ca09bbee30679d4a4373836e"></a>

```c
#define NXP_FMEAS_RT5XX_OSC_32KHZ NXP_FMEAS_CONNECTION(4)
```

相关声明：[NXP_FMEAS_RT5XX_OSC_32KHZ](#abfbd16b3ca09bbee30679d4a4373836e)、[NXP_FMEAS_CONNECTION](#a5d74f0050fc7e4c3f60866eb357f0cec)。

RT5xx FREQME 时钟源（Source）：32 kHz 振荡器（Oscillator）。

<a id="r_a27fb175d4c3d793d93d471c1250c3ba4"></a>

```c
#define NXP_FMEAS_RT5XX_MAIN_SYS_CLK NXP_FMEAS_CONNECTION(5)
```

相关声明：[NXP_FMEAS_RT5XX_MAIN_SYS_CLK](#a27fb175d4c3d793d93d471c1250c3ba4)、[NXP_FMEAS_CONNECTION](#a5d74f0050fc7e4c3f60866eb357f0cec)。

RT5xx FREQME 时钟源（Source）：主系统时钟（Main System Clock）。

<a id="r_abb11aec20074c3ce9d1a8ae217788e77"></a>

```c
#define NXP_FMEAS_RT5XX_FREQME_GPIO_CLK NXP_FMEAS_CONNECTION(6)
```

相关声明：[NXP_FMEAS_RT5XX_FREQME_GPIO_CLK](#abb11aec20074c3ce9d1a8ae217788e77)、[NXP_FMEAS_CONNECTION](#a5d74f0050fc7e4c3f60866eb357f0cec)。

RT5xx FREQME 时钟源（Source）：通过 GPIO 路由的外部时钟（External Clock，FREQME_GPIO_CLK）。

<a id="r_a194f18921ce4c938e58f2a1e80fbf7bd"></a>

```c
#define NXP_FMEAS_RT5XX_CLOCK_OUT NXP_FMEAS_CONNECTION(11)
```

相关声明：[NXP_FMEAS_RT5XX_CLOCK_OUT](#a194f18921ce4c938e58f2a1e80fbf7bd)、[NXP_FMEAS_CONNECTION](#a5d74f0050fc7e4c3f60866eb357f0cec)。

RT5xx FREQME 时钟源（Source）：CLKOUT。

<a id="r_a29b528eee4fae260d49c5a00cfa4c03c"></a>

```c
#define NXP_FMEAS_RW6XX_SYSOSC NXP_FMEAS_CONNECTION(0)
```

相关声明：[NXP_FMEAS_RW6XX_SYSOSC](#a29b528eee4fae260d49c5a00cfa4c03c)、[NXP_FMEAS_CONNECTION](#a5d74f0050fc7e4c3f60866eb357f0cec)。

RW6xx FREQME 时钟源（Source）：系统振荡器（System Oscillator，SYSOSC）。

<a id="r_ac83337895a8cc8ee2bca1206d80fbfd6"></a>

```c
#define NXP_FMEAS_RW6XX_SFRO NXP_FMEAS_CONNECTION(1)
```

相关声明：[NXP_FMEAS_RW6XX_SFRO](#ac83337895a8cc8ee2bca1206d80fbfd6)、[NXP_FMEAS_CONNECTION](#a5d74f0050fc7e4c3f60866eb357f0cec)。

RW6xx FREQME 时钟源（Source）：低速内部 FRO（Slow Internal FRO，SFRO）。

<a id="r_a756f1e814280e3fd44d02743de77bfe6"></a>

```c
#define NXP_FMEAS_RW6XX_FFRO NXP_FMEAS_CONNECTION(2)
```

相关声明：[NXP_FMEAS_RW6XX_FFRO](#a756f1e814280e3fd44d02743de77bfe6)、[NXP_FMEAS_CONNECTION](#a5d74f0050fc7e4c3f60866eb357f0cec)。

RW6xx FREQME 时钟源（Source）：高速内部 FRO（Fast Internal FRO，FFRO）。

<a id="r_aada1ce5f5b44eff8ffbb25642fda46f6"></a>

```c
#define NXP_FMEAS_RW6XX_LPOSC NXP_FMEAS_CONNECTION(3)
```

相关声明：[NXP_FMEAS_RW6XX_LPOSC](#aada1ce5f5b44eff8ffbb25642fda46f6)、[NXP_FMEAS_CONNECTION](#a5d74f0050fc7e4c3f60866eb357f0cec)。

RW6xx FREQME 时钟源（Source）：低功耗振荡器（Low-power Oscillator，LPOSC）。

<a id="r_a64024144ad312244def5a5efa27e692a"></a>

```c
#define NXP_FMEAS_RW6XX_XTAL_32K NXP_FMEAS_CONNECTION(4)
```

相关声明：[NXP_FMEAS_RW6XX_XTAL_32K](#a64024144ad312244def5a5efa27e692a)、[NXP_FMEAS_CONNECTION](#a5d74f0050fc7e4c3f60866eb357f0cec)。

RW6xx FREQME 时钟源（Source）：32 kHz 晶体（Crystal）。

<a id="r_a594792713d8b3dce6e304f3361eeba61"></a>

```c
#define NXP_FMEAS_RW6XX_C0_FR_HCLK NXP_FMEAS_CONNECTION(5)
```

相关声明：[NXP_FMEAS_RW6XX_C0_FR_HCLK](#a594792713d8b3dce6e304f3361eeba61)、[NXP_FMEAS_CONNECTION](#a5d74f0050fc7e4c3f60866eb357f0cec)。

RW6xx FREQME 时钟源（Source）：CPU0 自由运行 HCLK（Free-running HCLK，即主系统时钟）。

<a id="r_aeca8b24ca24476bf690cdfcbd71a051f"></a>

```c
#define NXP_FMEAS_RW6XX_FREQME_GPIO_CLK NXP_FMEAS_CONNECTION(6)
```

相关声明：[NXP_FMEAS_RW6XX_FREQME_GPIO_CLK](#aeca8b24ca24476bf690cdfcbd71a051f)、[NXP_FMEAS_CONNECTION](#a5d74f0050fc7e4c3f60866eb357f0cec)。

RW6xx FREQME 时钟源（Source）：通过 GPIO 路由的外部时钟（External Clock，FREQME_GPIO_CLK）。

## 22.2\_详细说明（Detailed Documentation）

<a id="a5d74f0050fc7e4c3f60866eb357f0cec"></a>

### `NXP_FMEAS_CONNECTION`

```c
#define NXP_FMEAS_CONNECTION ( sel)
```

展开值（Value）：

```c
(((sel) & ((1U << NXP_FMEAS_PMUX_SHIFT) - 1U)) | \
 (NXP_FMEAS_PMUX_ID << NXP_FMEAS_PMUX_SHIFT))
```

根据各输入源选择器 sel 构建 INPUTMUX FMEASURE 连接标识值（Cookie）。

<a id="ab96238e8880faa8d5019afa50ca86b21"></a>

### `NXP_FMEAS_PMUX_ID`

```c
#define NXP_FMEAS_PMUX_ID 0x700U
```

INPUTMUX PMUX 编码中的 FMEASURE 目标多路复用器 ID（Destination Mux ID）。

<a id="add988805308edfadd65bb2a879d2cc4f"></a>

### `NXP_FMEAS_PMUX_SHIFT`

```c
#define NXP_FMEAS_PMUX_SHIFT 20U
```

INPUTMUX 连接标识值（Cookie）中应用于 NXP_FMEAS_PMUX_ID 的移位量。

<a id="a194f18921ce4c938e58f2a1e80fbf7bd"></a>

### `NXP_FMEAS_RT5XX_CLOCK_OUT`

```c
#define NXP_FMEAS_RT5XX_CLOCK_OUT NXP_FMEAS_CONNECTION(11)
```

RT5xx FREQME 时钟源（Source）：CLKOUT。

<a id="abb11aec20074c3ce9d1a8ae217788e77"></a>

### `NXP_FMEAS_RT5XX_FREQME_GPIO_CLK`

```c
#define NXP_FMEAS_RT5XX_FREQME_GPIO_CLK NXP_FMEAS_CONNECTION(6)
```

RT5xx FREQME 时钟源（Source）：通过 GPIO 路由的外部时钟（External Clock，FREQME_GPIO_CLK）。

<a id="aca9626b1e9c76c79d219313d187b8b82"></a>

### `NXP_FMEAS_RT5XX_FRO_12M`

```c
#define NXP_FMEAS_RT5XX_FRO_12M NXP_FMEAS_CONNECTION(1)
```

RT5xx FREQME 时钟源（Source）：12 MHz FRO。

<a id="a5e9af8a1241b6dd2631df6e8e0b49d40"></a>

### `NXP_FMEAS_RT5XX_FRO_192M`

```c
#define NXP_FMEAS_RT5XX_FRO_192M NXP_FMEAS_CONNECTION(2)
```

RT5xx FREQME 时钟源（Source）：192 MHz FRO。

<a id="a5cc7ba765b45b8dc084e11f3171a36d5"></a>

### `NXP_FMEAS_RT5XX_LPOSC`

```c
#define NXP_FMEAS_RT5XX_LPOSC NXP_FMEAS_CONNECTION(3)
```

RT5xx FREQME 时钟源（Source）：低功耗振荡器（Low-power Oscillator，LPOSC）。

<a id="a27fb175d4c3d793d93d471c1250c3ba4"></a>

### `NXP_FMEAS_RT5XX_MAIN_SYS_CLK`

```c
#define NXP_FMEAS_RT5XX_MAIN_SYS_CLK NXP_FMEAS_CONNECTION(5)
```

RT5xx FREQME 时钟源（Source）：主系统时钟（Main System Clock）。

<a id="abfbd16b3ca09bbee30679d4a4373836e"></a>

### `NXP_FMEAS_RT5XX_OSC_32KHZ`

```c
#define NXP_FMEAS_RT5XX_OSC_32KHZ NXP_FMEAS_CONNECTION(4)
```

RT5xx FREQME 时钟源（Source）：32 kHz 振荡器（Oscillator）。

<a id="a64aaa4f65294c66ef9833edd0e18132c"></a>

### `NXP_FMEAS_RT5XX_XTALIN`

```c
#define NXP_FMEAS_RT5XX_XTALIN NXP_FMEAS_CONNECTION(0)
```

RT5xx FREQME 时钟源（Source）：晶体振荡器输入（Crystal Oscillator Input，XTALIN）。

<a id="ab25300603e27ac35daa28ed7ce81d146"></a>

### `NXP_FMEAS_RT6XX_FFRO`

```c
#define NXP_FMEAS_RT6XX_FFRO NXP_FMEAS_CONNECTION(2)
```

RT6xx FREQME 时钟源（Source）：高速内部 FRO（Fast Internal FRO，FFRO）。

<a id="a2b5fc580ecc71519d883d12192faef84"></a>

### `NXP_FMEAS_RT6XX_FREQME_GPIO_CLK`

```c
#define NXP_FMEAS_RT6XX_FREQME_GPIO_CLK NXP_FMEAS_CONNECTION(6)
```

RT6xx FREQME 时钟源（Source）：通过 GPIO 路由的外部时钟（External Clock，FREQME_GPIO_CLK）。

<a id="a9f42ac77b6d0f13bd9162b4f95b7fee0"></a>

### `NXP_FMEAS_RT6XX_LPOSC`

```c
#define NXP_FMEAS_RT6XX_LPOSC NXP_FMEAS_CONNECTION(3)
```

RT6xx FREQME 时钟源（Source）：低功耗振荡器（Low-power Oscillator，LPOSC）。

<a id="a9b16992173eca7e0bebe2adf11eb2b32"></a>

### `NXP_FMEAS_RT6XX_MAIN_SYS_CLK`

```c
#define NXP_FMEAS_RT6XX_MAIN_SYS_CLK NXP_FMEAS_CONNECTION(5)
```

RT6xx FREQME 时钟源（Source）：主系统时钟（Main System Clock）。

<a id="a679aafa6bf7960b725be79817e67b0c4"></a>

### `NXP_FMEAS_RT6XX_RTC_32KHZ`

```c
#define NXP_FMEAS_RT6XX_RTC_32KHZ NXP_FMEAS_CONNECTION(4)
```

RT6xx FREQME 时钟源（Source）：32 kHz RTC 振荡器（Oscillator）。

<a id="a02da62ca559fad494ffdbef7b64cfc0d"></a>

### `NXP_FMEAS_RT6XX_SFRO`

```c
#define NXP_FMEAS_RT6XX_SFRO NXP_FMEAS_CONNECTION(1)
```

RT6xx FREQME 时钟源（Source）：低速内部 FRO（Slow Internal FRO，SFRO）。

<a id="a4786b637a270914245f51cabc3e97bac"></a>

### `NXP_FMEAS_RT6XX_XTALIN`

```c
#define NXP_FMEAS_RT6XX_XTALIN NXP_FMEAS_CONNECTION(0)
```

RT6xx FREQME 时钟源（Source）：晶体振荡器输入（Crystal Oscillator Input，XTALIN）。

<a id="a594792713d8b3dce6e304f3361eeba61"></a>

### `NXP_FMEAS_RW6XX_C0_FR_HCLK`

```c
#define NXP_FMEAS_RW6XX_C0_FR_HCLK NXP_FMEAS_CONNECTION(5)
```

RW6xx FREQME 时钟源（Source）：CPU0 自由运行 HCLK（Free-running HCLK，即主系统时钟）。

<a id="a756f1e814280e3fd44d02743de77bfe6"></a>

### `NXP_FMEAS_RW6XX_FFRO`

```c
#define NXP_FMEAS_RW6XX_FFRO NXP_FMEAS_CONNECTION(2)
```

RW6xx FREQME 时钟源（Source）：高速内部 FRO（Fast Internal FRO，FFRO）。

<a id="aeca8b24ca24476bf690cdfcbd71a051f"></a>

### `NXP_FMEAS_RW6XX_FREQME_GPIO_CLK`

```c
#define NXP_FMEAS_RW6XX_FREQME_GPIO_CLK NXP_FMEAS_CONNECTION(6)
```

RW6xx FREQME 时钟源（Source）：通过 GPIO 路由的外部时钟（External Clock，FREQME_GPIO_CLK）。

<a id="aada1ce5f5b44eff8ffbb25642fda46f6"></a>

### `NXP_FMEAS_RW6XX_LPOSC`

```c
#define NXP_FMEAS_RW6XX_LPOSC NXP_FMEAS_CONNECTION(3)
```

RW6xx FREQME 时钟源（Source）：低功耗振荡器（Low-power Oscillator，LPOSC）。

<a id="ac83337895a8cc8ee2bca1206d80fbfd6"></a>

### `NXP_FMEAS_RW6XX_SFRO`

```c
#define NXP_FMEAS_RW6XX_SFRO NXP_FMEAS_CONNECTION(1)
```

RW6xx FREQME 时钟源（Source）：低速内部 FRO（Slow Internal FRO，SFRO）。

<a id="a29b528eee4fae260d49c5a00cfa4c03c"></a>

### `NXP_FMEAS_RW6XX_SYSOSC`

```c
#define NXP_FMEAS_RW6XX_SYSOSC NXP_FMEAS_CONNECTION(0)
```

RW6xx FREQME 时钟源（Source）：系统振荡器（System Oscillator，SYSOSC）。

<a id="a64024144ad312244def5a5efa27e692a"></a>

### `NXP_FMEAS_RW6XX_XTAL_32K`

```c
#define NXP_FMEAS_RW6XX_XTAL_32K NXP_FMEAS_CONNECTION(4)
```

RW6xx FREQME 时钟源（Source）：32 kHz 晶体（Crystal）。


## 22.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_runtime_reference/P046_nxp-fmeas.h_源码浏览.md)
- [clock_monitor_set_source()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__monitor__interface.html#ga60d5aefa9429cafce872c8f3be40c100)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="anxp-fmeas_8h_html_ab96238e8880faa8d5019afa50ca86b21"></a>
<a id="anxp-fmeas_8h_html_add988805308edfadd65bb2a879d2cc4f"></a>

---

[上一章](P021_zephyr__net__mqtt_sn.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P023_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rx-pfs.h_文件参考.md)
