---
id: learning.zephyr-docs.api-file-media-sensor-reference.page-6
title: zephyr__dt-bindings__clock__rx_clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rx__clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_dt-bindings\_\_clock\_\_rx\_clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/rx__clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Zephyr使用的Renesas RX时钟发生电路（Clock Generator Circuit，CGC）的定义。

查看此文件的源码。

<a id="details"></a>

用于 Zephyr 的 Renesas RX 时钟生成电路定义（Clock Generator Circuit，CGC）。本头文件提供 Renesas RX SoC 的时钟源选择（Clock Source Selection）和倍频／分频（Multiplier/Divider）宏常量。设备树时钟控制子系统（Devicetree Clock Control Subsystem）使用这些取值描述时钟配置。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.1\_宏定义（Macros）

<a id="define-members-0"></a>

### Renesas RX 时钟源选择定义（Clock Source Selection Definitions）

<a id="r_a34ad5578be7c44989dbc9550e44a8a4b"></a>

```c
#define RX_CLOCKS_SOURCE_CLOCK_LOCO 0
```

相关声明：[RX_CLOCKS_SOURCE_CLOCK_LOCO](#a34ad5578be7c44989dbc9550e44a8a4b)。

LOCO 时钟源（Clock Source）。

<a id="r_a7f9df4a65ff2bb13f28f5d9a56ca6458"></a>

```c
#define RX_CLOCKS_SOURCE_CLOCK_HOCO 1
```

相关声明：[RX_CLOCKS_SOURCE_CLOCK_HOCO](#a7f9df4a65ff2bb13f28f5d9a56ca6458)。

HOCO 时钟源（Clock Source）。

<a id="r_af9048c9274b0d9c0b6d02d00efdb5dc5"></a>

```c
#define RX_CLOCKS_SOURCE_CLOCK_MAIN_OSC 2
```

相关声明：[RX_CLOCKS_SOURCE_CLOCK_MAIN_OSC](#af9048c9274b0d9c0b6d02d00efdb5dc5)。

主振荡器（Main Oscillator）。

<a id="r_aa9fd49a8b6282bbe853e8b9c5a3c07a4"></a>

```c
#define RX_CLOCKS_SOURCE_CLOCK_SUBCLOCK 3
```

相关声明：[RX_CLOCKS_SOURCE_CLOCK_SUBCLOCK](#aa9fd49a8b6282bbe853e8b9c5a3c07a4)。

子时钟振荡器（Sub-clock Oscillator）。

<a id="r_ac0090ad354eef53450b78b1347d197d5"></a>

```c
#define RX_CLOCKS_SOURCE_PLL 4
```

相关声明：[RX_CLOCKS_SOURCE_PLL](#ac0090ad354eef53450b78b1347d197d5)。

PLL 锁相环时钟源（Clock Source）。

<a id="r_aeb9f49621a1b1694f921b8368db7f2d3"></a>

```c
#define RX_CLOCKS_SOURCE_CLOCK_DISABLE 0xff
```

相关声明：[RX_CLOCKS_SOURCE_CLOCK_DISABLE](#aeb9f49621a1b1694f921b8368db7f2d3)。

时钟源已禁用（Clock Source Disabled）。

<a id="define-members-1"></a>

### Renesas RX 部分外设选择用时钟源定义（Peripheral Clock Source Selection Definitions）

某些外设使用的编码时钟源值（Encoded Clock Source Values）。

<a id="r_aff3d236b7e518544e5c0d13f2709dd11"></a>

```c
#define RX_IF_CLOCKS_SOURCE_CLOCK_HOCO 0
```

相关声明：[RX_IF_CLOCKS_SOURCE_CLOCK_HOCO](#aff3d236b7e518544e5c0d13f2709dd11)。

HOCO 时钟源（Clock Source）。

<a id="r_af8f57f080fa51f53e524edac7fbe1733"></a>

```c
#define RX_IF_CLOCKS_SOURCE_CLOCK_LOCO 2
```

相关声明：[RX_IF_CLOCKS_SOURCE_CLOCK_LOCO](#af8f57f080fa51f53e524edac7fbe1733)。

LOCO 时钟源（Clock Source）。

<a id="r_a4738f24d7981a80e79db26523136fc1a"></a>

```c
#define RX_IF_CLOCKS_SOURCE_PLL 5
```

相关声明：[RX_IF_CLOCKS_SOURCE_PLL](#a4738f24d7981a80e79db26523136fc1a)。

PLL 锁相环时钟源（Clock Source）。

<a id="r_adf63d79b98346792fc79af7726ef97c3"></a>

```c
#define RX_IF_CLOCKS_SOURCE_PLL2 6
```

相关声明：[RX_IF_CLOCKS_SOURCE_PLL2](#adf63d79b98346792fc79af7726ef97c3)。

PLL2 时钟源（Clock Source）。

<a id="define-members-2"></a>

### Renesas RX 低功耗定时器时钟源选择定义（Low-power Timer，LPT）

<a id="r_a495ead7f1ca66e5c1812ee906bb8607b"></a>

```c
#define RX_LPT_CLOCKS_SOURCE_CLOCK_SUBCLOCK 0
```

相关声明：[RX_LPT_CLOCKS_SOURCE_CLOCK_SUBCLOCK](#a495ead7f1ca66e5c1812ee906bb8607b)。

子时钟振荡器（Sub-clock Oscillator）。

<a id="r_a6f87bb7b7dc555ab28358a86b28a5a25"></a>

```c
#define RX_LPT_CLOCKS_SOURCE_CLOCK_IWDT_LOW_SPEED 1
```

相关声明：[RX_LPT_CLOCKS_SOURCE_CLOCK_IWDT_LOW_SPEED](#a6f87bb7b7dc555ab28358a86b28a5a25)。

IWDT 低速时钟（Low Speed）。

<a id="r_a7fd495dac366a61bfe65314a616982d5"></a>

```c
#define RX_LPT_CLOCKS_NON_USE 2
```

相关声明：[RX_LPT_CLOCKS_NON_USE](#a7fd495dac366a61bfe65314a616982d5)。

不使用（Not Used）。

<a id="r_a8e49ec555856053be1f2b666df17bc10"></a>

```c
#define RX_LPT_CLOCKS_SOURCE_CLOCK_LOCO 3
```

相关声明：[RX_LPT_CLOCKS_SOURCE_CLOCK_LOCO](#a8e49ec555856053be1f2b666df17bc10)。

LOCO 时钟源（Clock Source）。

<a id="define-members-3"></a>

### Renesas RX 锁相环倍频系数定义（PLL Multiplier Definitions）

<a id="r_a95484b87b3b8dd928ee44fadbe62c34c"></a>

```c
#define RX_PLL_MUL_4 7
```

相关声明：[RX_PLL_MUL_4](#a95484b87b3b8dd928ee44fadbe62c34c)。

锁相环倍频系数（PLL Multiplier）：×4。

<a id="r_a8a46183046ada00e547fab490bcdf7f5"></a>

```c
#define RX_PLL_MUL_4_5 8
```

相关声明：[RX_PLL_MUL_4_5](#a8a46183046ada00e547fab490bcdf7f5)。

锁相环倍频系数（PLL Multiplier）：×4.5。

<a id="r_a5522650769528743cfbf50285520863c"></a>

```c
#define RX_PLL_MUL_5 9
```

相关声明：[RX_PLL_MUL_5](#a5522650769528743cfbf50285520863c)。

锁相环倍频系数（PLL Multiplier）：×5。

<a id="r_afad555c1cf1b15100676ce8187b3d894"></a>

```c
#define RX_PLL_MUL_5_5 10
```

相关声明：[RX_PLL_MUL_5_5](#afad555c1cf1b15100676ce8187b3d894)。

锁相环倍频系数（PLL Multiplier）：×5.5。

<a id="r_af741a56149f610c9e8ee2d707a008d31"></a>

```c
#define RX_PLL_MUL_6 11
```

相关声明：[RX_PLL_MUL_6](#af741a56149f610c9e8ee2d707a008d31)。

锁相环倍频系数（PLL Multiplier）：×6。

<a id="r_a095cbc195164157ef62bd029327903ef"></a>

```c
#define RX_PLL_MUL_6_5 12
```

相关声明：[RX_PLL_MUL_6_5](#a095cbc195164157ef62bd029327903ef)。

锁相环倍频系数（PLL Multiplier）：×6.5。

<a id="r_a27858908d3a7b4cef172c7d3c3f8d1d1"></a>

```c
#define RX_PLL_MUL_7 13
```

相关声明：[RX_PLL_MUL_7](#a27858908d3a7b4cef172c7d3c3f8d1d1)。

锁相环倍频系数（PLL Multiplier）：×7。

<a id="r_a800235cba53e4e6ce97e0461cd2e245f"></a>

```c
#define RX_PLL_MUL_7_5 14
```

相关声明：[RX_PLL_MUL_7_5](#a800235cba53e4e6ce97e0461cd2e245f)。

锁相环倍频系数（PLL Multiplier）：×7.5。

<a id="r_a7d62c1cec0ae721da1f24ba43f194921"></a>

```c
#define RX_PLL_MUL_8 15
```

相关声明：[RX_PLL_MUL_8](#a7d62c1cec0ae721da1f24ba43f194921)。

锁相环倍频系数（PLL Multiplier）：×7。

<a id="r_a53a7199aeb036f3c69246f5d401ecb44"></a>

```c
#define RX_PLL_MUL_10 19
```

相关声明：[RX_PLL_MUL_10](#a53a7199aeb036f3c69246f5d401ecb44)。

锁相环倍频系数（PLL Multiplier）：×10。

<a id="r_ae30b2994f96c0c11ad7bf9b82e8ec878"></a>

```c
#define RX_PLL_MUL_10_5 20
```

相关声明：[RX_PLL_MUL_10_5](#ae30b2994f96c0c11ad7bf9b82e8ec878)。

锁相环倍频系数（PLL Multiplier）：×10.5。

<a id="r_aabccdf9ad6ed1d061a2c18f0f6bda74a"></a>

```c
#define RX_PLL_MUL_11 21
```

相关声明：[RX_PLL_MUL_11](#aabccdf9ad6ed1d061a2c18f0f6bda74a)。

锁相环倍频系数（PLL Multiplier）：×11。

<a id="r_ae8c6a56b6c36162b3a2437e910081b71"></a>

```c
#define RX_PLL_MUL_11_5 22
```

相关声明：[RX_PLL_MUL_11_5](#ae8c6a56b6c36162b3a2437e910081b71)。

锁相环倍频系数（PLL Multiplier）：×11.5。

<a id="r_ad2a43b638a929d90e6e8ee4cd0b832d1"></a>

```c
#define RX_PLL_MUL_12 23
```

相关声明：[RX_PLL_MUL_12](#ad2a43b638a929d90e6e8ee4cd0b832d1)。

锁相环倍频系数（PLL Multiplier）：×12。

<a id="r_a60908985689fbc116c0afd7b31335387"></a>

```c
#define RX_PLL_MUL_12_5 24
```

相关声明：[RX_PLL_MUL_12_5](#a60908985689fbc116c0afd7b31335387)。

锁相环倍频系数（PLL Multiplier）：×12.5。

<a id="r_a3111b7eab33f06dd9fd4770204310795"></a>

```c
#define RX_PLL_MUL_13 25
```

相关声明：[RX_PLL_MUL_13](#a3111b7eab33f06dd9fd4770204310795)。

锁相环倍频系数（PLL Multiplier）：×13。

<a id="r_a11ebe02501f0f0bbc9b06a42443ee21e"></a>

```c
#define RX_PLL_MUL_13_5 26
```

相关声明：[RX_PLL_MUL_13_5](#a11ebe02501f0f0bbc9b06a42443ee21e)。

锁相环倍频系数（PLL Multiplier）：×13.5。

<a id="r_a4550ac72ea50526624e2e6ad74dee570"></a>

```c
#define RX_PLL_MUL_14 27
```

相关声明：[RX_PLL_MUL_14](#a4550ac72ea50526624e2e6ad74dee570)。

锁相环倍频系数（PLL Multiplier）：×14。

<a id="r_a07242f5a11126e195ec1858c254a1715"></a>

```c
#define RX_PLL_MUL_14_5 28
```

相关声明：[RX_PLL_MUL_14_5](#a07242f5a11126e195ec1858c254a1715)。

锁相环倍频系数（PLL Multiplier）：×14.5。

<a id="r_ac253de151c3f4435ad5d7c5947d51a01"></a>

```c
#define RX_PLL_MUL_15 29
```

相关声明：[RX_PLL_MUL_15](#ac253de151c3f4435ad5d7c5947d51a01)。

锁相环倍频系数（PLL Multiplier）：×15。

<a id="r_a8dbf6f3546d10db88f29c00a2736eaf8"></a>

```c
#define RX_PLL_MUL_15_5 30
```

相关声明：[RX_PLL_MUL_15_5](#a8dbf6f3546d10db88f29c00a2736eaf8)。

锁相环倍频系数（PLL Multiplier）：×15.5。

<a id="r_afbca80ae99fdc8b5c7ba18187ca7009e"></a>

```c
#define RX_PLL_MUL_16 31
```

相关声明：[RX_PLL_MUL_16](#afbca80ae99fdc8b5c7ba18187ca7009e)。

锁相环倍频系数（PLL Multiplier）：×16。

<a id="r_a4eeeb6b6eb6e62d6ce6e5621bdd45a09"></a>

```c
#define RX_PLL_MUL_16_5 32
```

相关声明：[RX_PLL_MUL_16_5](#a4eeeb6b6eb6e62d6ce6e5621bdd45a09)。

锁相环倍频系数（PLL Multiplier）：×16.5。

<a id="r_adf52f9b8cc2a450681b9ca2ad9eb83ca"></a>

```c
#define RX_PLL_MUL_17 33
```

相关声明：[RX_PLL_MUL_17](#adf52f9b8cc2a450681b9ca2ad9eb83ca)。

锁相环倍频系数（PLL Multiplier）：×17。

<a id="r_a34beac4a3f4a14c2fea81ab551f9585a"></a>

```c
#define RX_PLL_MUL_17_5 34
```

相关声明：[RX_PLL_MUL_17_5](#a34beac4a3f4a14c2fea81ab551f9585a)。

锁相环倍频系数（PLL Multiplier）：×17.5。

<a id="r_a88bf8153f561bd731b6c2deaf69aa15a"></a>

```c
#define RX_PLL_MUL_18 35
```

相关声明：[RX_PLL_MUL_18](#a88bf8153f561bd731b6c2deaf69aa15a)。

锁相环倍频系数（PLL Multiplier）：×18。

<a id="r_accc6e94b5c3a3e628368277a16b6c695"></a>

```c
#define RX_PLL_MUL_18_5 36
```

相关声明：[RX_PLL_MUL_18_5](#accc6e94b5c3a3e628368277a16b6c695)。

锁相环倍频系数（PLL Multiplier）：×18.5。

<a id="r_a2540da688a8d0572b750e7ba7d19ccd3"></a>

```c
#define RX_PLL_MUL_19 37
```

相关声明：[RX_PLL_MUL_19](#a2540da688a8d0572b750e7ba7d19ccd3)。

锁相环倍频系数（PLL Multiplier）：×19。

<a id="r_aebcfa6fe35d480997273794d1914b931"></a>

```c
#define RX_PLL_MUL_19_5 38
```

相关声明：[RX_PLL_MUL_19_5](#aebcfa6fe35d480997273794d1914b931)。

锁相环倍频系数（PLL Multiplier）：×19.5。

<a id="r_a4d67a33beb30e1a0d02fd22725acc07d"></a>

```c
#define RX_PLL_MUL_20 39
```

相关声明：[RX_PLL_MUL_20](#a4d67a33beb30e1a0d02fd22725acc07d)。

锁相环倍频系数（PLL Multiplier）：×20。

<a id="r_a7a9df8e20986eb4f2079a9ece45fc32d"></a>

```c
#define RX_PLL_MUL_20_5 40
```

相关声明：[RX_PLL_MUL_20_5](#a7a9df8e20986eb4f2079a9ece45fc32d)。

锁相环倍频系数（PLL Multiplier）：×20.5。

<a id="r_adb2149a1c4249b01b651900f4fa071a7"></a>

```c
#define RX_PLL_MUL_21 41
```

相关声明：[RX_PLL_MUL_21](#adb2149a1c4249b01b651900f4fa071a7)。

锁相环倍频系数（PLL Multiplier）：×21。

<a id="r_a2edf822bc2001ae5de56b5d7d12eea34"></a>

```c
#define RX_PLL_MUL_21_5 42
```

相关声明：[RX_PLL_MUL_21_5](#a2edf822bc2001ae5de56b5d7d12eea34)。

锁相环倍频系数（PLL Multiplier）：×21.5。

<a id="r_a0bf5fbd23b50ca9601c36d576c3f7373"></a>

```c
#define RX_PLL_MUL_22 43
```

相关声明：[RX_PLL_MUL_22](#a0bf5fbd23b50ca9601c36d576c3f7373)。

锁相环倍频系数（PLL Multiplier）：×22。

<a id="r_ac56ec80f02cd1e4112207512fa25745b"></a>

```c
#define RX_PLL_MUL_22_5 44
```

相关声明：[RX_PLL_MUL_22_5](#ac56ec80f02cd1e4112207512fa25745b)。

锁相环倍频系数（PLL Multiplier）：×22.5。

<a id="r_a93f3b8f16495658cb7d75a3e038ee8db"></a>

```c
#define RX_PLL_MUL_23 45
```

相关声明：[RX_PLL_MUL_23](#a93f3b8f16495658cb7d75a3e038ee8db)。

锁相环倍频系数（PLL Multiplier）：×23。

<a id="r_a1c7ec81c528ac8c937d7656f79a6201e"></a>

```c
#define RX_PLL_MUL_23_5 46
```

相关声明：[RX_PLL_MUL_23_5](#a1c7ec81c528ac8c937d7656f79a6201e)。

锁相环倍频系数（PLL Multiplier）：×23.5。

<a id="r_a1f56253d1ef4643268032fed16796d74"></a>

```c
#define RX_PLL_MUL_24 47
```

相关声明：[RX_PLL_MUL_24](#a1f56253d1ef4643268032fed16796d74)。

锁相环倍频系数（PLL Multiplier）：×24。

<a id="r_aecec3ca42c067ca5fcfbde987dea9c9d"></a>

```c
#define RX_PLL_MUL_24_5 48
```

相关声明：[RX_PLL_MUL_24_5](#aecec3ca42c067ca5fcfbde987dea9c9d)。

锁相环倍频系数（PLL Multiplier）：×24.5。

<a id="r_af3ff2efcf8a50f3e2bd7dca00600c56e"></a>

```c
#define RX_PLL_MUL_25 49
```

相关声明：[RX_PLL_MUL_25](#af3ff2efcf8a50f3e2bd7dca00600c56e)。

锁相环倍频系数（PLL Multiplier）：×25。

<a id="r_ad0f9f987323b7b62aaeba5cf19813ab9"></a>

```c
#define RX_PLL_MUL_25_5 50
```

相关声明：[RX_PLL_MUL_25_5](#ad0f9f987323b7b62aaeba5cf19813ab9)。

锁相环倍频系数（PLL Multiplier）：×25.5。

<a id="r_a564630ed58a71bb1d4eecd5fc5ba859b"></a>

```c
#define RX_PLL_MUL_26 51
```

相关声明：[RX_PLL_MUL_26](#a564630ed58a71bb1d4eecd5fc5ba859b)。

锁相环倍频系数（PLL Multiplier）：×26。

<a id="r_ac51b99bc6e3039b50ba85d9f74e4a1d8"></a>

```c
#define RX_PLL_MUL_26_5 52
```

相关声明：[RX_PLL_MUL_26_5](#ac51b99bc6e3039b50ba85d9f74e4a1d8)。

锁相环倍频系数（PLL Multiplier）：×26.5。

<a id="r_a3b946ef3c493c9c33f29358cd6243508"></a>

```c
#define RX_PLL_MUL_27 53
```

相关声明：[RX_PLL_MUL_27](#a3b946ef3c493c9c33f29358cd6243508)。

锁相环倍频系数（PLL Multiplier）：×27。

<a id="r_a59c63d9d6e9cc192f608a758f8c93635"></a>

```c
#define RX_PLL_MUL_27_5 54
```

相关声明：[RX_PLL_MUL_27_5](#a59c63d9d6e9cc192f608a758f8c93635)。

锁相环倍频系数（PLL Multiplier）：×27.5。

<a id="r_afcb0633863584cc0a1912c5102a7690e"></a>

```c
#define RX_PLL_MUL_28 55
```

相关声明：[RX_PLL_MUL_28](#afcb0633863584cc0a1912c5102a7690e)。

锁相环倍频系数（PLL Multiplier）：×28。

<a id="r_a407bfdaee25bc58ee4fa3a53b15bf717"></a>

```c
#define RX_PLL_MUL_28_5 56
```

相关声明：[RX_PLL_MUL_28_5](#a407bfdaee25bc58ee4fa3a53b15bf717)。

锁相环倍频系数（PLL Multiplier）：×28.5。

<a id="r_a44ccce817f2e8695bd93061743acef6f"></a>

```c
#define RX_PLL_MUL_29 57
```

相关声明：[RX_PLL_MUL_29](#a44ccce817f2e8695bd93061743acef6f)。

锁相环倍频系数（PLL Multiplier）：×29。

<a id="r_a136f1127661e85dc8cf41d6ba3d1f1ea"></a>

```c
#define RX_PLL_MUL_29_5 58
```

相关声明：[RX_PLL_MUL_29_5](#a136f1127661e85dc8cf41d6ba3d1f1ea)。

锁相环倍频系数（PLL Multiplier）：×29.5。

<a id="r_a1dd0358c897adeb4754c7f732c9b2aef"></a>

```c
#define RX_PLL_MUL_30 59
```

相关声明：[RX_PLL_MUL_30](#a1dd0358c897adeb4754c7f732c9b2aef)。

锁相环倍频系数（PLL Multiplier）：×30。

<a id="define-members-4"></a>

### Renesas RX 模块停止控制寄存器定义（Module Stop Control Register，MSTP）

<a id="r_ad42c8389fe2748e158a84e350bb7f685"></a>

```c
#define MSTPA 0
```

相关声明：[MSTPA](#ad42c8389fe2748e158a84e350bb7f685)。

模块停止控制寄存器（Module stop control register）A。

<a id="r_ad111ad00f435e6cdc148aea67829d9da"></a>

```c
#define MSTPB 1
```

相关声明：[MSTPB](#ad111ad00f435e6cdc148aea67829d9da)。

模块停止控制寄存器 B。

<a id="r_aafb615973639ad154a74e3cf9f65e8c2"></a>

```c
#define MSTPC 2
```

相关声明：[MSTPC](#aafb615973639ad154a74e3cf9f65e8c2)。

模块停止控制寄存器 C。

<a id="r_aecaea293ebf408aec8a4af4b2e5c6809"></a>

```c
#define MSTPD 3
```

相关声明：[MSTPD](#aecaea293ebf408aec8a4af4b2e5c6809)。

模块停止控制寄存器 D。

<a id="r_a2463bde8d3692a83f030cd9df04c2e39"></a>

```c
#define MSTPE 4
```

相关声明：[MSTPE](#a2463bde8d3692a83f030cd9df04c2e39)。

模块停止控制寄存器 E。

<a id="r_afbcf3f815105ea456cc45c8a44e676c6"></a>

```c
#define MSTPF 5
```

相关声明：[MSTPF](#afbcf3f815105ea456cc45c8a44e676c6)。

模块停止控制寄存器 F（Module Stop Control Register F）。

## 6.2\_详细说明（Detailed Documentation）

<a id="ad42c8389fe2748e158a84e350bb7f685"></a>

### `MSTPA`

```c
#define MSTPA 0
```

模块停止控制寄存器（Module stop control register）A。

<a id="ad111ad00f435e6cdc148aea67829d9da"></a>

### `MSTPB`

```c
#define MSTPB 1
```

模块停止控制寄存器 B。

<a id="aafb615973639ad154a74e3cf9f65e8c2"></a>

### `MSTPC`

```c
#define MSTPC 2
```

模块停止控制寄存器 C。

<a id="aecaea293ebf408aec8a4af4b2e5c6809"></a>

### `MSTPD`

```c
#define MSTPD 3
```

模块停止控制寄存器 D。

<a id="a2463bde8d3692a83f030cd9df04c2e39"></a>

### `MSTPE`

```c
#define MSTPE 4
```

模块停止控制寄存器 E。

<a id="afbcf3f815105ea456cc45c8a44e676c6"></a>

### `MSTPF`

```c
#define MSTPF 5
```

模块停止控制寄存器 F（Module Stop Control Register F）。

<a id="aeb9f49621a1b1694f921b8368db7f2d3"></a>

### `RX_CLOCKS_SOURCE_CLOCK_DISABLE`

```c
#define RX_CLOCKS_SOURCE_CLOCK_DISABLE 0xff
```

时钟源已禁用（Clock Source Disabled）。

<a id="a7f9df4a65ff2bb13f28f5d9a56ca6458"></a>

### `RX_CLOCKS_SOURCE_CLOCK_HOCO`

```c
#define RX_CLOCKS_SOURCE_CLOCK_HOCO 1
```

HOCO 时钟源（Clock Source）。

<a id="a34ad5578be7c44989dbc9550e44a8a4b"></a>

### `RX_CLOCKS_SOURCE_CLOCK_LOCO`

```c
#define RX_CLOCKS_SOURCE_CLOCK_LOCO 0
```

LOCO 时钟源（Clock Source）。

<a id="af9048c9274b0d9c0b6d02d00efdb5dc5"></a>

### `RX_CLOCKS_SOURCE_CLOCK_MAIN_OSC`

```c
#define RX_CLOCKS_SOURCE_CLOCK_MAIN_OSC 2
```

主振荡器（Main Oscillator）。

<a id="aa9fd49a8b6282bbe853e8b9c5a3c07a4"></a>

### `RX_CLOCKS_SOURCE_CLOCK_SUBCLOCK`

```c
#define RX_CLOCKS_SOURCE_CLOCK_SUBCLOCK 3
```

子时钟振荡器（Sub-clock Oscillator）。

<a id="ac0090ad354eef53450b78b1347d197d5"></a>

### `RX_CLOCKS_SOURCE_PLL`

```c
#define RX_CLOCKS_SOURCE_PLL 4
```

PLL 锁相环时钟源（Clock Source）。

<a id="aff3d236b7e518544e5c0d13f2709dd11"></a>

### `RX_IF_CLOCKS_SOURCE_CLOCK_HOCO`

```c
#define RX_IF_CLOCKS_SOURCE_CLOCK_HOCO 0
```

HOCO 时钟源（Clock Source）。

<a id="af8f57f080fa51f53e524edac7fbe1733"></a>

### `RX_IF_CLOCKS_SOURCE_CLOCK_LOCO`

```c
#define RX_IF_CLOCKS_SOURCE_CLOCK_LOCO 2
```

LOCO 时钟源（Clock Source）。

<a id="a4738f24d7981a80e79db26523136fc1a"></a>

### `RX_IF_CLOCKS_SOURCE_PLL`

```c
#define RX_IF_CLOCKS_SOURCE_PLL 5
```

PLL 锁相环时钟源（Clock Source）。

<a id="adf63d79b98346792fc79af7726ef97c3"></a>

### `RX_IF_CLOCKS_SOURCE_PLL2`

```c
#define RX_IF_CLOCKS_SOURCE_PLL2 6
```

PLL2 时钟源（Clock Source）。

<a id="a7fd495dac366a61bfe65314a616982d5"></a>

### `RX_LPT_CLOCKS_NON_USE`

```c
#define RX_LPT_CLOCKS_NON_USE 2
```

不使用（Not Used）。

<a id="a6f87bb7b7dc555ab28358a86b28a5a25"></a>

### `RX_LPT_CLOCKS_SOURCE_CLOCK_IWDT_LOW_SPEED`

```c
#define RX_LPT_CLOCKS_SOURCE_CLOCK_IWDT_LOW_SPEED 1
```

IWDT 低速时钟（Low Speed）。

<a id="a8e49ec555856053be1f2b666df17bc10"></a>

### `RX_LPT_CLOCKS_SOURCE_CLOCK_LOCO`

```c
#define RX_LPT_CLOCKS_SOURCE_CLOCK_LOCO 3
```

LOCO 时钟源（Clock Source）。

<a id="a495ead7f1ca66e5c1812ee906bb8607b"></a>

### `RX_LPT_CLOCKS_SOURCE_CLOCK_SUBCLOCK`

```c
#define RX_LPT_CLOCKS_SOURCE_CLOCK_SUBCLOCK 0
```

子时钟振荡器（Sub-clock Oscillator）。

<a id="a53a7199aeb036f3c69246f5d401ecb44"></a>

### `RX_PLL_MUL_10`

```c
#define RX_PLL_MUL_10 19
```

锁相环倍频系数（PLL Multiplier）：×10。

<a id="ae30b2994f96c0c11ad7bf9b82e8ec878"></a>

### `RX_PLL_MUL_10_5`

```c
#define RX_PLL_MUL_10_5 20
```

锁相环倍频系数（PLL Multiplier）：×10.5。

<a id="aabccdf9ad6ed1d061a2c18f0f6bda74a"></a>

### `RX_PLL_MUL_11`

```c
#define RX_PLL_MUL_11 21
```

锁相环倍频系数（PLL Multiplier）：×11。

<a id="ae8c6a56b6c36162b3a2437e910081b71"></a>

### `RX_PLL_MUL_11_5`

```c
#define RX_PLL_MUL_11_5 22
```

锁相环倍频系数（PLL Multiplier）：×11.5。

<a id="ad2a43b638a929d90e6e8ee4cd0b832d1"></a>

### `RX_PLL_MUL_12`

```c
#define RX_PLL_MUL_12 23
```

锁相环倍频系数（PLL Multiplier）：×12。

<a id="a60908985689fbc116c0afd7b31335387"></a>

### `RX_PLL_MUL_12_5`

```c
#define RX_PLL_MUL_12_5 24
```

锁相环倍频系数（PLL Multiplier）：×12.5。

<a id="a3111b7eab33f06dd9fd4770204310795"></a>

### `RX_PLL_MUL_13`

```c
#define RX_PLL_MUL_13 25
```

锁相环倍频系数（PLL Multiplier）：×13。

<a id="a11ebe02501f0f0bbc9b06a42443ee21e"></a>

### `RX_PLL_MUL_13_5`

```c
#define RX_PLL_MUL_13_5 26
```

锁相环倍频系数（PLL Multiplier）：×13.5。

<a id="a4550ac72ea50526624e2e6ad74dee570"></a>

### `RX_PLL_MUL_14`

```c
#define RX_PLL_MUL_14 27
```

锁相环倍频系数（PLL Multiplier）：×14。

<a id="a07242f5a11126e195ec1858c254a1715"></a>

### `RX_PLL_MUL_14_5`

```c
#define RX_PLL_MUL_14_5 28
```

锁相环倍频系数（PLL Multiplier）：×14.5。

<a id="ac253de151c3f4435ad5d7c5947d51a01"></a>

### `RX_PLL_MUL_15`

```c
#define RX_PLL_MUL_15 29
```

锁相环倍频系数（PLL Multiplier）：×15。

<a id="a8dbf6f3546d10db88f29c00a2736eaf8"></a>

### `RX_PLL_MUL_15_5`

```c
#define RX_PLL_MUL_15_5 30
```

锁相环倍频系数（PLL Multiplier）：×15.5。

<a id="afbca80ae99fdc8b5c7ba18187ca7009e"></a>

### `RX_PLL_MUL_16`

```c
#define RX_PLL_MUL_16 31
```

锁相环倍频系数（PLL Multiplier）：×16。

<a id="a4eeeb6b6eb6e62d6ce6e5621bdd45a09"></a>

### `RX_PLL_MUL_16_5`

```c
#define RX_PLL_MUL_16_5 32
```

锁相环倍频系数（PLL Multiplier）：×16.5。

<a id="adf52f9b8cc2a450681b9ca2ad9eb83ca"></a>

### `RX_PLL_MUL_17`

```c
#define RX_PLL_MUL_17 33
```

锁相环倍频系数（PLL Multiplier）：×17。

<a id="a34beac4a3f4a14c2fea81ab551f9585a"></a>

### `RX_PLL_MUL_17_5`

```c
#define RX_PLL_MUL_17_5 34
```

锁相环倍频系数（PLL Multiplier）：×17.5。

<a id="a88bf8153f561bd731b6c2deaf69aa15a"></a>

### `RX_PLL_MUL_18`

```c
#define RX_PLL_MUL_18 35
```

锁相环倍频系数（PLL Multiplier）：×18。

<a id="accc6e94b5c3a3e628368277a16b6c695"></a>

### `RX_PLL_MUL_18_5`

```c
#define RX_PLL_MUL_18_5 36
```

锁相环倍频系数（PLL Multiplier）：×18.5。

<a id="a2540da688a8d0572b750e7ba7d19ccd3"></a>

### `RX_PLL_MUL_19`

```c
#define RX_PLL_MUL_19 37
```

锁相环倍频系数（PLL Multiplier）：×19。

<a id="aebcfa6fe35d480997273794d1914b931"></a>

### `RX_PLL_MUL_19_5`

```c
#define RX_PLL_MUL_19_5 38
```

锁相环倍频系数（PLL Multiplier）：×19.5。

<a id="a4d67a33beb30e1a0d02fd22725acc07d"></a>

### `RX_PLL_MUL_20`

```c
#define RX_PLL_MUL_20 39
```

锁相环倍频系数（PLL Multiplier）：×20。

<a id="a7a9df8e20986eb4f2079a9ece45fc32d"></a>

### `RX_PLL_MUL_20_5`

```c
#define RX_PLL_MUL_20_5 40
```

锁相环倍频系数（PLL Multiplier）：×20.5。

<a id="adb2149a1c4249b01b651900f4fa071a7"></a>

### `RX_PLL_MUL_21`

```c
#define RX_PLL_MUL_21 41
```

锁相环倍频系数（PLL Multiplier）：×21。

<a id="a2edf822bc2001ae5de56b5d7d12eea34"></a>

### `RX_PLL_MUL_21_5`

```c
#define RX_PLL_MUL_21_5 42
```

锁相环倍频系数（PLL Multiplier）：×21.5。

<a id="a0bf5fbd23b50ca9601c36d576c3f7373"></a>

### `RX_PLL_MUL_22`

```c
#define RX_PLL_MUL_22 43
```

锁相环倍频系数（PLL Multiplier）：×22。

<a id="ac56ec80f02cd1e4112207512fa25745b"></a>

### `RX_PLL_MUL_22_5`

```c
#define RX_PLL_MUL_22_5 44
```

锁相环倍频系数（PLL Multiplier）：×22.5。

<a id="a93f3b8f16495658cb7d75a3e038ee8db"></a>

### `RX_PLL_MUL_23`

```c
#define RX_PLL_MUL_23 45
```

锁相环倍频系数（PLL Multiplier）：×23。

<a id="a1c7ec81c528ac8c937d7656f79a6201e"></a>

### `RX_PLL_MUL_23_5`

```c
#define RX_PLL_MUL_23_5 46
```

锁相环倍频系数（PLL Multiplier）：×23.5。

<a id="a1f56253d1ef4643268032fed16796d74"></a>

### `RX_PLL_MUL_24`

```c
#define RX_PLL_MUL_24 47
```

锁相环倍频系数（PLL Multiplier）：×24。

<a id="aecec3ca42c067ca5fcfbde987dea9c9d"></a>

### `RX_PLL_MUL_24_5`

```c
#define RX_PLL_MUL_24_5 48
```

锁相环倍频系数（PLL Multiplier）：×24.5。

<a id="af3ff2efcf8a50f3e2bd7dca00600c56e"></a>

### `RX_PLL_MUL_25`

```c
#define RX_PLL_MUL_25 49
```

锁相环倍频系数（PLL Multiplier）：×25。

<a id="ad0f9f987323b7b62aaeba5cf19813ab9"></a>

### `RX_PLL_MUL_25_5`

```c
#define RX_PLL_MUL_25_5 50
```

锁相环倍频系数（PLL Multiplier）：×25.5。

<a id="a564630ed58a71bb1d4eecd5fc5ba859b"></a>

### `RX_PLL_MUL_26`

```c
#define RX_PLL_MUL_26 51
```

锁相环倍频系数（PLL Multiplier）：×26。

<a id="ac51b99bc6e3039b50ba85d9f74e4a1d8"></a>

### `RX_PLL_MUL_26_5`

```c
#define RX_PLL_MUL_26_5 52
```

锁相环倍频系数（PLL Multiplier）：×26.5。

<a id="a3b946ef3c493c9c33f29358cd6243508"></a>

### `RX_PLL_MUL_27`

```c
#define RX_PLL_MUL_27 53
```

锁相环倍频系数（PLL Multiplier）：×27。

<a id="a59c63d9d6e9cc192f608a758f8c93635"></a>

### `RX_PLL_MUL_27_5`

```c
#define RX_PLL_MUL_27_5 54
```

锁相环倍频系数（PLL Multiplier）：×27.5。

<a id="afcb0633863584cc0a1912c5102a7690e"></a>

### `RX_PLL_MUL_28`

```c
#define RX_PLL_MUL_28 55
```

锁相环倍频系数（PLL Multiplier）：×28。

<a id="a407bfdaee25bc58ee4fa3a53b15bf717"></a>

### `RX_PLL_MUL_28_5`

```c
#define RX_PLL_MUL_28_5 56
```

锁相环倍频系数（PLL Multiplier）：×28.5。

<a id="a44ccce817f2e8695bd93061743acef6f"></a>

### `RX_PLL_MUL_29`

```c
#define RX_PLL_MUL_29 57
```

锁相环倍频系数（PLL Multiplier）：×29。

<a id="a136f1127661e85dc8cf41d6ba3d1f1ea"></a>

### `RX_PLL_MUL_29_5`

```c
#define RX_PLL_MUL_29_5 58
```

锁相环倍频系数（PLL Multiplier）：×29.5。

<a id="a1dd0358c897adeb4754c7f732c9b2aef"></a>

### `RX_PLL_MUL_30`

```c
#define RX_PLL_MUL_30 59
```

锁相环倍频系数（PLL Multiplier）：×30。

<a id="a95484b87b3b8dd928ee44fadbe62c34c"></a>

### `RX_PLL_MUL_4`

```c
#define RX_PLL_MUL_4 7
```

锁相环倍频系数（PLL Multiplier）：×4。

<a id="a8a46183046ada00e547fab490bcdf7f5"></a>

### `RX_PLL_MUL_4_5`

```c
#define RX_PLL_MUL_4_5 8
```

锁相环倍频系数（PLL Multiplier）：×4.5。

<a id="a5522650769528743cfbf50285520863c"></a>

### `RX_PLL_MUL_5`

```c
#define RX_PLL_MUL_5 9
```

锁相环倍频系数（PLL Multiplier）：×5。

<a id="afad555c1cf1b15100676ce8187b3d894"></a>

### `RX_PLL_MUL_5_5`

```c
#define RX_PLL_MUL_5_5 10
```

锁相环倍频系数（PLL Multiplier）：×5.5。

<a id="af741a56149f610c9e8ee2d707a008d31"></a>

### `RX_PLL_MUL_6`

```c
#define RX_PLL_MUL_6 11
```

锁相环倍频系数（PLL Multiplier）：×6。

<a id="a095cbc195164157ef62bd029327903ef"></a>

### `RX_PLL_MUL_6_5`

```c
#define RX_PLL_MUL_6_5 12
```

锁相环倍频系数（PLL Multiplier）：×6.5。

<a id="a27858908d3a7b4cef172c7d3c3f8d1d1"></a>

### `RX_PLL_MUL_7`

```c
#define RX_PLL_MUL_7 13
```

锁相环倍频系数（PLL Multiplier）：×7。

<a id="a800235cba53e4e6ce97e0461cd2e245f"></a>

### `RX_PLL_MUL_7_5`

```c
#define RX_PLL_MUL_7_5 14
```

锁相环倍频系数（PLL Multiplier）：×7.5。

<a id="a7d62c1cec0ae721da1f24ba43f194921"></a>

### `RX_PLL_MUL_8`

```c
#define RX_PLL_MUL_8 15
```

锁相环倍频系数（PLL Multiplier）：×7。


## 6.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P743_rx_clock.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P005_zephyr__bluetooth__audio__mcc.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__drivers__sensor.h_文件参考.md)
