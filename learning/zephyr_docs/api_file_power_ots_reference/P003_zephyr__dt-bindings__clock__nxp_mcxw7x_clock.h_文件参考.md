---
id: learning.zephyr-docs.api-file-power-ots-reference.page-3
title: zephyr__dt-bindings__clock__nxp_mcxw7x_clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nxp__mcxw7x__clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_dt-bindings\_\_clock\_\_nxp\_mcxw7x\_clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/nxp__mcxw7x__clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

NXP MCXW7x时钟控制器（Clock Controller）的设备树绑定宏。

查看此文件的源码。

<a id="details"></a>

NXP MCXW7x 时钟控制器的设备树绑定宏（DT Binding Macros）。设备树时钟绑定属性使用这些宏来描述 MCXW 设备的时钟模式、时钟源、分频器和控制标志。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.1\_宏定义（Macros）

<a id="define-members-0"></a>

### OSC32K振荡器模式（OSC32K Mode）

<a id="r_a76617c20053432fbbf9a3b514612672a"></a>

```c
#define MCXW_CLK_OSC32K_DISABLE 0
```

相关声明：[MCXW_CLK_OSC32K_DISABLE](#a76617c20053432fbbf9a3b514612672a)。

禁用 32K 振荡器模式（Oscillator Mode）。

<a id="r_a1f5fb1d0ef7661acd08daff786e69784"></a>

```c
#define MCXW_CLK_OSC32K_ENABLE 1
```

相关声明：[MCXW_CLK_OSC32K_ENABLE](#a1f5fb1d0ef7661acd08daff786e69784)。

启用 32K 振荡器模式（Oscillator Mode）。

<a id="r_a49e1a94c972d6b16322a368c16641676"></a>

```c
#define MCXW_CLK_OSC32K_BYPASS 3
```

相关声明：[MCXW_CLK_OSC32K_BYPASS](#a49e1a94c972d6b16322a368c16641676)。

旁路 32K 振荡器（Bypass），使用外部时钟（External Clock）。

<a id="define-members-1"></a>

### OSC32K XTAL／EXTAL内部负载电容（OSC32K XTAL/EXTAL internal load capacitance）

选择由 OSC32K 电容组（Cap Bank）接入的内部电容（Internal Capacitance）。

取值 `N` 对应 `2*N` pF，范围为 0–30 pF。

<a id="r_a260db29cde74f0226ebfec58486a49b4"></a>

```c
#define MCXW_CLK_OSC32K_CAP_0PF 0
```

相关声明：[MCXW_CLK_OSC32K_CAP_0PF](#a260db29cde74f0226ebfec58486a49b4)。

内部电容（Internal Capacitance）为 0 pF。

<a id="r_aada508e5912d82cf8bcf71c9258bf460"></a>

```c
#define MCXW_CLK_OSC32K_CAP_2PF 1
```

相关声明：[MCXW_CLK_OSC32K_CAP_2PF](#aada508e5912d82cf8bcf71c9258bf460)。

内部电容（Internal Capacitance）为 2 pF。

<a id="r_a7a03c8af2b88437d75b812decd5d7c39"></a>

```c
#define MCXW_CLK_OSC32K_CAP_4PF 2
```

相关声明：[MCXW_CLK_OSC32K_CAP_4PF](#a7a03c8af2b88437d75b812decd5d7c39)。

内部电容（Internal Capacitance）为 4 pF。

<a id="r_a88528c7784dcd0d418e04ebf4ca17eee"></a>

```c
#define MCXW_CLK_OSC32K_CAP_6PF 3
```

相关声明：[MCXW_CLK_OSC32K_CAP_6PF](#a88528c7784dcd0d418e04ebf4ca17eee)。

内部电容（Internal Capacitance）为 6 pF。

<a id="r_abe321a1905411b9f706966c5061d50b3"></a>

```c
#define MCXW_CLK_OSC32K_CAP_8PF 4
```

相关声明：[MCXW_CLK_OSC32K_CAP_8PF](#abe321a1905411b9f706966c5061d50b3)。

内部电容（Internal Capacitance）为 8 pF。

<a id="r_a04df19a313ddc6f2d5bdfbd1ee00c8cf"></a>

```c
#define MCXW_CLK_OSC32K_CAP_10PF 5
```

相关声明：[MCXW_CLK_OSC32K_CAP_10PF](#a04df19a313ddc6f2d5bdfbd1ee00c8cf)。

内部电容（Internal Capacitance）为 10 pF。

<a id="r_a054becc9e2c3355e59cf6afc1f1a2216"></a>

```c
#define MCXW_CLK_OSC32K_CAP_12PF 6
```

相关声明：[MCXW_CLK_OSC32K_CAP_12PF](#a054becc9e2c3355e59cf6afc1f1a2216)。

内部电容（Internal Capacitance）为 12 pF。

<a id="r_a82219a0b4235dda30fd098f9e1d772c9"></a>

```c
#define MCXW_CLK_OSC32K_CAP_14PF 7
```

相关声明：[MCXW_CLK_OSC32K_CAP_14PF](#a82219a0b4235dda30fd098f9e1d772c9)。

内部电容（Internal Capacitance）为 14 pF。

<a id="r_a10e5d75da66b5e3c3447a32ba7968e74"></a>

```c
#define MCXW_CLK_OSC32K_CAP_16PF 8
```

相关声明：[MCXW_CLK_OSC32K_CAP_16PF](#a10e5d75da66b5e3c3447a32ba7968e74)。

内部电容（Internal Capacitance）为 16 pF。

<a id="r_a43c0106192089d39266def8ba62b1999"></a>

```c
#define MCXW_CLK_OSC32K_CAP_18PF 9
```

相关声明：[MCXW_CLK_OSC32K_CAP_18PF](#a43c0106192089d39266def8ba62b1999)。

内部电容（Internal Capacitance）为 18 pF。

<a id="r_a722c71f3f1d715aee1123cbbfdefddaa"></a>

```c
#define MCXW_CLK_OSC32K_CAP_20PF 10
```

相关声明：[MCXW_CLK_OSC32K_CAP_20PF](#a722c71f3f1d715aee1123cbbfdefddaa)。

内部电容（Internal Capacitance）为 20 pF。

<a id="r_a7b0b4b82806eda2c24f7dfd7c3035b82"></a>

```c
#define MCXW_CLK_OSC32K_CAP_22PF 11
```

相关声明：[MCXW_CLK_OSC32K_CAP_22PF](#a7b0b4b82806eda2c24f7dfd7c3035b82)。

内部电容（Internal Capacitance）为 22 pF。

<a id="r_a65964ab3f92482b9ec8f115f1273bac1"></a>

```c
#define MCXW_CLK_OSC32K_CAP_24PF 12
```

相关声明：[MCXW_CLK_OSC32K_CAP_24PF](#a65964ab3f92482b9ec8f115f1273bac1)。

内部电容（Internal Capacitance）为 24 pF。

<a id="r_a22f279ceb7e4902eedb39bf0651e1981"></a>

```c
#define MCXW_CLK_OSC32K_CAP_26PF 13
```

相关声明：[MCXW_CLK_OSC32K_CAP_26PF](#a22f279ceb7e4902eedb39bf0651e1981)。

内部电容（Internal Capacitance）为 26 pF。

<a id="r_a18903ab29f3d2641d7664beb48510818"></a>

```c
#define MCXW_CLK_OSC32K_CAP_28PF 14
```

相关声明：[MCXW_CLK_OSC32K_CAP_28PF](#a18903ab29f3d2641d7664beb48510818)。

内部电容（Internal Capacitance）为 28 pF。

<a id="r_a82533cb21bc8a71815e4b6d03d15758d"></a>

```c
#define MCXW_CLK_OSC32K_CAP_30PF 15
```

相关声明：[MCXW_CLK_OSC32K_CAP_30PF](#a82533cb21bc8a71815e4b6d03d15758d)。

内部电容（Internal Capacitance）为 30 pF。

<a id="define-members-2"></a>

### OSC32K放大器粗调增益调整（OSC32K coarse amplifier gain adjustment）

选择 32 kHz 晶体振荡器放大器的粗调增益（Coarse Gain），用于匹配外部晶体的等效串联电阻（ESR）范围。

<a id="r_a2c64d094664c3e775dd09a0aa288a91d"></a>

```c
#define MCXW_CLK_OSC32K_COARSE_RANGE0 0
```

相关声明：[MCXW_CLK_OSC32K_COARSE_RANGE0](#a2c64d094664c3e775dd09a0aa288a91d)。

放大器粗调增益（Coarse Amplifier Gain）范围 0。

<a id="r_aa11e25f4c50d193b13aa0398eb67ca3b"></a>

```c
#define MCXW_CLK_OSC32K_COARSE_RANGE1 1
```

相关声明：[MCXW_CLK_OSC32K_COARSE_RANGE1](#aa11e25f4c50d193b13aa0398eb67ca3b)。

放大器粗调增益（Coarse Amplifier Gain）范围 1。

<a id="r_a555c3721c4aa3132d01e58e46ddce177"></a>

```c
#define MCXW_CLK_OSC32K_COARSE_RANGE2 2
```

相关声明：[MCXW_CLK_OSC32K_COARSE_RANGE2](#a555c3721c4aa3132d01e58e46ddce177)。

放大器粗调增益（Coarse Amplifier Gain）范围 2。

<a id="r_a4e97219d6e9027ad3169348cecad8920"></a>

```c
#define MCXW_CLK_OSC32K_COARSE_RANGE3 3
```

相关声明：[MCXW_CLK_OSC32K_COARSE_RANGE3](#a4e97219d6e9027ad3169348cecad8920)。

放大器粗调增益（Coarse Amplifier Gain）范围 3。

<a id="define-members-3"></a>

### 快速内部RC振荡器模式（FIRC Mode）

<a id="r_a575dcc55e7aaeff512b21a85a290005c"></a>

```c
#define MCXW_CLK_FIRC_DISABLE 0
```

相关声明：[MCXW_CLK_FIRC_DISABLE](#a575dcc55e7aaeff512b21a85a290005c)。

禁用快速内部 RC 振荡器（FIRC）。

<a id="r_ad0936d3984812dcdcb6673ba2b71a680"></a>

```c
#define MCXW_CLK_FIRC_ENABLE 1
```

相关声明：[MCXW_CLK_FIRC_ENABLE](#ad0936d3984812dcdcb6673ba2b71a680)。

启用快速内部 RC 振荡器（FIRC）。

<a id="r_a41e2a2852ae3fb5e1bd8eddc0471c93d"></a>

```c
#define MCXW_CLK_FIRC_ENABLE_IN_LP 2
```

相关声明：[MCXW_CLK_FIRC_ENABLE_IN_LP](#a41e2a2852ae3fb5e1bd8eddc0471c93d)。

在低功耗模式（Low-Power Mode）下启用快速内部 RC 振荡器（FIRC）。

<a id="define-members-4"></a>

### 快速内部RC振荡器范围（FIRC Range）

<a id="r_aceaaa53b2ef24965b87980d82ccd1d71"></a>

```c
#define MCXW_CLK_FIRC_RANGE_48MHZ 0
```

相关声明：[MCXW_CLK_FIRC_RANGE_48MHZ](#aceaaa53b2ef24965b87980d82ccd1d71)。

快速内部 RC 振荡器（FIRC）范围：48 MHz。

<a id="r_ae942bd0c3ac7cdaea097f92c65b33c0c"></a>

```c
#define MCXW_CLK_FIRC_RANGE_64MHZ 1
```

相关声明：[MCXW_CLK_FIRC_RANGE_64MHZ](#ae942bd0c3ac7cdaea097f92c65b33c0c)。

快速内部 RC 振荡器（FIRC）范围：64 MHz。

<a id="r_a30c8090495abf07e0e26fc89ca2e5593"></a>

```c
#define MCXW_CLK_FIRC_RANGE_96MHZ 2
```

相关声明：[MCXW_CLK_FIRC_RANGE_96MHZ](#a30c8090495abf07e0e26fc89ca2e5593)。

快速内部 RC 振荡器（FIRC）范围：96 MHz。

<a id="r_a5e32c9d70f8fb8f57fbdec1cafacb183"></a>

```c
#define MCXW_CLK_FIRC_RANGE_192MHZ 3
```

相关声明：[MCXW_CLK_FIRC_RANGE_192MHZ](#a5e32c9d70f8fb8f57fbdec1cafacb183)。

快速内部 RC 振荡器（FIRC）范围：192 MHz。

<a id="define-members-5"></a>

### 系统时钟源（System clock source）

<a id="r_ad3fd21e228934ab0b9fe990b7df4eb2d"></a>

```c
#define MCXW_CLK_SYSTEM_CLK_SRC_SOSC 1
```

相关声明：[MCXW_CLK_SYSTEM_CLK_SRC_SOSC](#ad3fd21e228934ab0b9fe990b7df4eb2d)。

系统时钟：SOSC，外部振荡器（External Oscillator）。

<a id="r_a8122561ce50e3dc728ad1a50989eb6be"></a>

```c
#define MCXW_CLK_SYSTEM_CLK_SRC_SIRC 2
```

相关声明：[MCXW_CLK_SYSTEM_CLK_SRC_SIRC](#a8122561ce50e3dc728ad1a50989eb6be)。

系统时钟：SIRC，内部慢速 RC 振荡器（Internal Slow RC）。

<a id="r_a051a2a0932ac96f438363497dc56092b"></a>

```c
#define MCXW_CLK_SYSTEM_CLK_SRC_FIRC 3
```

相关声明：[MCXW_CLK_SYSTEM_CLK_SRC_FIRC](#a051a2a0932ac96f438363497dc56092b)。

系统时钟：FIRC，快速内部 RC 振荡器（Fast Internal RC）。

<a id="r_af86b46afe036b31cc8d551a3e72c1896"></a>

```c
#define MCXW_CLK_SYSTEM_CLK_SRC_ROSC 4
```

相关声明：[MCXW_CLK_SYSTEM_CLK_SRC_ROSC](#af86b46afe036b31cc8d551a3e72c1896)。

系统时钟：ROSC，环形振荡器（Ring Oscillator）。

<a id="define-members-6"></a>

### 系统时钟分频器（System clock dividers）

这些值对应 MCXW 平台代码使用的 `kSCG_SysClkDivByX` 定义。

<a id="r_a08a00775e88b21ddedf139d9b21bf18e"></a>

```c
#define MCXW_CLK_DIV_NONE 0
```

相关声明：[MCXW_CLK_DIV_NONE](#a08a00775e88b21ddedf139d9b21bf18e)。

不改变分频（Divider），等同于 `MCXW_CLK_DIV_BY_1`。

<a id="r_a2642f3b762f8f981e40fa46cf3bf5354"></a>

```c
#define MCXW_CLK_DIV_BY_1 0
```

相关声明：[MCXW_CLK_DIV_BY_1](#a2642f3b762f8f981e40fa46cf3bf5354)。

1 分频（Divide by 1）。

<a id="r_a1a5e445e26dd9acfd313af91b46a3bd4"></a>

```c
#define MCXW_CLK_DIV_BY_2 1
```

相关声明：[MCXW_CLK_DIV_BY_2](#a1a5e445e26dd9acfd313af91b46a3bd4)。

2 分频（Divide by 2）。

<a id="r_ad67ab40b6b903d1b790cfdb223fe9ba0"></a>

```c
#define MCXW_CLK_DIV_BY_3 2
```

相关声明：[MCXW_CLK_DIV_BY_3](#ad67ab40b6b903d1b790cfdb223fe9ba0)。

3 分频（Divide by 3）。

<a id="r_a6d1bcc656dfaf86e32f0ec7e47c91fbf"></a>

```c
#define MCXW_CLK_DIV_BY_4 3
```

相关声明：[MCXW_CLK_DIV_BY_4](#a6d1bcc656dfaf86e32f0ec7e47c91fbf)。

4 分频（Divide by 4）。

<a id="r_ac001bad69869ab50ec1e019c46e3b52c"></a>

```c
#define MCXW_CLK_DIV_BY_5 4
```

相关声明：[MCXW_CLK_DIV_BY_5](#ac001bad69869ab50ec1e019c46e3b52c)。

5 分频（Divide by 5）。

<a id="r_af6d3d08aa4245bc1f946ddb4b06f1b40"></a>

```c
#define MCXW_CLK_DIV_BY_6 5
```

相关声明：[MCXW_CLK_DIV_BY_6](#af6d3d08aa4245bc1f946ddb4b06f1b40)。

6 分频（Divide by 6）。

<a id="r_acc61c7a4b274638ac02acea373f345dd"></a>

```c
#define MCXW_CLK_DIV_BY_7 6
```

相关声明：[MCXW_CLK_DIV_BY_7](#acc61c7a4b274638ac02acea373f345dd)。

7 分频（Divide by 7）。

<a id="r_a15df301cd186a8b348e8da9c41577f3a"></a>

```c
#define MCXW_CLK_DIV_BY_8 7
```

相关声明：[MCXW_CLK_DIV_BY_8](#a15df301cd186a8b348e8da9c41577f3a)。

8 分频（Divide by 8）。

<a id="r_af11117da4f77390f374a74ad5d8aa4ad"></a>

```c
#define MCXW_CLK_DIV_BY_10 9
```

相关声明：[MCXW_CLK_DIV_BY_10](#af11117da4f77390f374a74ad5d8aa4ad)。

10 分频（Divide by 10）。

<a id="r_ab4d4d8694061a1035755359aa7362dc5"></a>

```c
#define MCXW_CLK_DIV_BY_11 10
```

相关声明：[MCXW_CLK_DIV_BY_11](#ab4d4d8694061a1035755359aa7362dc5)。

11 分频（Divide by 11）。

<a id="r_ae5183adcfc16c8951708f9f4ed9ef544"></a>

```c
#define MCXW_CLK_DIV_BY_12 11
```

相关声明：[MCXW_CLK_DIV_BY_12](#ae5183adcfc16c8951708f9f4ed9ef544)。

12 分频（Divide by 12）。

<a id="r_a7ace4ae8f7a6cdd194c14d768de3d6dc"></a>

```c
#define MCXW_CLK_DIV_BY_13 12
```

相关声明：[MCXW_CLK_DIV_BY_13](#a7ace4ae8f7a6cdd194c14d768de3d6dc)。

13 分频（Divide by 13）。

<a id="r_a38aaeee7732478e365d5e401ab321d64"></a>

```c
#define MCXW_CLK_DIV_BY_14 13
```

相关声明：[MCXW_CLK_DIV_BY_14](#a38aaeee7732478e365d5e401ab321d64)。

14 分频（Divide by 14）。

<a id="r_ae5eda5611801b12370e21f209bbaa282"></a>

```c
#define MCXW_CLK_DIV_BY_15 14
```

相关声明：[MCXW_CLK_DIV_BY_15](#ae5eda5611801b12370e21f209bbaa282)。

15 分频（Divide by 15）。

<a id="r_ab17b8449c5f4c683b6503ea3d00bb163"></a>

```c
#define MCXW_CLK_DIV_BY_16 15
```

相关声明：[MCXW_CLK_DIV_BY_16](#ab17b8449c5f4c683b6503ea3d00bb163)。

16 分频（Divide by 16）。

<a id="define-members-7"></a>

### 外设IP多路复用时钟源（IP mux clock sources）

通过 IP 多路复用选择（IP Mux Selection）选择外设时钟源的值。

<a id="r_a3b4a0a8d639d80c336d805d46af5ac33"></a>

```c
#define MCXW_CLK_IP_MUX_SLOW_CLK 1
```

相关声明：[MCXW_CLK_IP_MUX_SLOW_CLK](#a3b4a0a8d639d80c336d805d46af5ac33)。

慢速时钟源（Slow Clock Source）。

<a id="r_a0cc00d635bbdce56db9ce9335726c1d5"></a>

```c
#define MCXW_CLK_IP_MUX_FRO_6M 2
```

相关声明：[MCXW_CLK_IP_MUX_FRO_6M](#a0cc00d635bbdce56db9ce9335726c1d5)。

自由运行振荡器（FRO）6 MHz 时钟，`kCLOCK_IpSrcFro6M`。

<a id="r_a2d558dab24029d7ed08aa5c791a1be49"></a>

```c
#define MCXW_CLK_IP_MUX_FRO_192M_DIV 3
```

相关声明：[MCXW_CLK_IP_MUX_FRO_192M_DIV](#a2d558dab24029d7ed08aa5c791a1be49)。

自由运行振荡器（FRO）192 MHz 分频时钟，频率取决于范围设置。

<a id="r_aabed45808ee538aebfec10df0034d20a"></a>

```c
#define MCXW_CLK_IP_MUX_SOSC 4
```

相关声明：[MCXW_CLK_IP_MUX_SOSC](#aabed45808ee538aebfec10df0034d20a)。

SOSC：射频振荡器时钟（RF Oscillator Clock），`kCLOCK_IpSrcSoscClk`。

<a id="r_abb0f0c933ce8376753666aa7211e7c24"></a>

```c
#define MCXW_CLK_IP_MUX_32K 5
```

相关声明：[MCXW_CLK_IP_MUX_32K](#abb0f0c933ce8376753666aa7211e7c24)。

32 kHz 时钟（Clock），`kCLOCK_IpSrc32kClk`。

<a id="r_aeca4e40941dee1717fa357501d6c8410"></a>

```c
#define MCXW_CLK_IP_MUX_FRO_200M_DIV 6
```

相关声明：[MCXW_CLK_IP_MUX_FRO_200M_DIV](#aeca4e40941dee1717fa357501d6c8410)。

自由运行振荡器（FRO）200 MHz，用于 CAN；仅 MCXW70 支持。

<a id="r_a2b5ce49932aa4aaa775fe80d6b2ee656"></a>

```c
#define MCXW_CLK_IP_MUX_1M 7
```

相关声明：[MCXW_CLK_IP_MUX_1M](#a2b5ce49932aa4aaa775fe80d6b2ee656)。

由 FRO6M 派生的 1 MHz 时钟；仅 MCXW70 支持。

<a id="r_a079ba179088bdda8a053e8163a9ecebf"></a>

```c
#define MCXW_CLK_IP_MUX_NONE 0xFF
```

相关声明：[MCXW_CLK_IP_MUX_NONE](#a079ba179088bdda8a053e8163a9ecebf)。

无外设 IP 多路复用选择（IP Mux Selection）／无效值。

<a id="define-members-8"></a>

### 时钟控制标志（Clock control flags）

这些标志与驱动使用的 `kCLOCK_IpClkControl_xxx` 值一致。

<a id="r_af54c3318538fda656e7b07be1807b1bd"></a>

```c
#define MCXW_CLK_CTRL_DISABLED 0
```

相关声明：[MCXW_CLK_CTRL_DISABLED](#af54c3318538fda656e7b07be1807b1bd)。

时钟禁用（Clock Disabled），`kCLOCK_IpClkControl_fun0`。

<a id="r_a18f0255e4fb2047bbfffdc542fbd52da"></a>

```c
#define MCXW_CLK_CTRL_ENABLED 1U
```

相关声明：[MCXW_CLK_CTRL_ENABLED](#a18f0255e4fb2047bbfffdc542fbd52da)。

时钟启用（Clock Enabled），`kCLOCK_IpClkControl_fun1`。

<a id="define-members-9"></a>

### 低功耗行为标志（Low power behavior flags）

<a id="r_a487ca0a3e7ddf59139b9981198b1fb4a"></a>

```c
#define MCXW_CLK_LP_STALL_ALLOWED 0U
```

相关声明：[MCXW_CLK_LP_STALL_ALLOWED](#a487ca0a3e7ddf59139b9981198b1fb4a)。

时钟可阻止进入低功耗状态（Low-Power Entry），会使其等待（Stall）。

<a id="r_a5d6b4be6587c741d96c2492c6f334ec9"></a>

```c
#define MCXW_CLK_LP_NO_STALL 2U
```

相关声明：[MCXW_CLK_LP_NO_STALL](#a5d6b4be6587c741d96c2492c6f334ec9)。

时钟不会阻止进入低功耗状态（Low-Power Entry），不会使其等待（No Stall）。

<a id="define-members-10"></a>

### 组合控制模式（Combined control modes）

<a id="r_aac8723ce4534f2f1041281bdbc41e994"></a>

```c
#define MCXW_CLK_MODE_DISABLED (MCXW_CLK_CTRL_DISABLED)
```

相关声明：[MCXW_CLK_MODE_DISABLED](#aac8723ce4534f2f1041281bdbc41e994)、[MCXW_CLK_CTRL_DISABLED](#af54c3318538fda656e7b07be1807b1bd)。

禁用模式（Disabled Mode）。

<a id="r_ad8f488bad33a11b2fed3c8b0cda959bb"></a>

```c
#define MCXW_CLK_MODE_ENABLED_LP_STALL (MCXW_CLK_CTRL_ENABLED | MCXW_CLK_LP_STALL_ALLOWED)
```

相关声明：[MCXW_CLK_MODE_ENABLED_LP_STALL](#ad8f488bad33a11b2fed3c8b0cda959bb)、[MCXW_CLK_CTRL_ENABLED](#a18f0255e4fb2047bbfffdc542fbd52da)、[MCXW_CLK_LP_STALL_ALLOWED](#a487ca0a3e7ddf59139b9981198b1fb4a)。

已启用；可能使低功耗进入流程等待（Stall LP）。

<a id="r_a6a81d1a5a76fe0d67a8af1a1011031fe"></a>

```c
#define MCXW_CLK_MODE_ENABLED_LP_NO_STALL (MCXW_CLK_CTRL_ENABLED | MCXW_CLK_LP_NO_STALL)
```

相关声明：[MCXW_CLK_MODE_ENABLED_LP_NO_STALL](#a6a81d1a5a76fe0d67a8af1a1011031fe)、[MCXW_CLK_CTRL_ENABLED](#a18f0255e4fb2047bbfffdc542fbd52da)、[MCXW_CLK_LP_NO_STALL](#a5d6b4be6587c741d96c2492c6f334ec9)。

已启用；不会使低功耗进入流程等待（Won't Stall LP）。

<a id="r_ace217387a298100d7e0ef9fb24ed5d08"></a>

```c
#define MCXW_CLOCK(mrcc_offset, clk_mux, clk_div, flag)
```

相关声明：[MCXW_CLOCK](#ace217387a298100d7e0ef9fb24ed5d08)。

用于将时钟配置（Clock Configuration）编码为设备树绑定所用 32 位整数的辅助宏。

## 3.2\_详细说明（Detailed Documentation）

<a id="af54c3318538fda656e7b07be1807b1bd"></a>

### `MCXW_CLK_CTRL_DISABLED`

```c
#define MCXW_CLK_CTRL_DISABLED 0
```

时钟禁用（Clock Disabled），`kCLOCK_IpClkControl_fun0`。

<a id="a18f0255e4fb2047bbfffdc542fbd52da"></a>

### `MCXW_CLK_CTRL_ENABLED`

```c
#define MCXW_CLK_CTRL_ENABLED 1U
```

时钟启用（Clock Enabled），`kCLOCK_IpClkControl_fun1`。

<a id="a2642f3b762f8f981e40fa46cf3bf5354"></a>

### `MCXW_CLK_DIV_BY_1`

```c
#define MCXW_CLK_DIV_BY_1 0
```

1 分频（Divide by 1）。

<a id="af11117da4f77390f374a74ad5d8aa4ad"></a>

### `MCXW_CLK_DIV_BY_10`

```c
#define MCXW_CLK_DIV_BY_10 9
```

10 分频（Divide by 10）。

<a id="ab4d4d8694061a1035755359aa7362dc5"></a>

### `MCXW_CLK_DIV_BY_11`

```c
#define MCXW_CLK_DIV_BY_11 10
```

11 分频（Divide by 11）。

<a id="ae5183adcfc16c8951708f9f4ed9ef544"></a>

### `MCXW_CLK_DIV_BY_12`

```c
#define MCXW_CLK_DIV_BY_12 11
```

12 分频（Divide by 12）。

<a id="a7ace4ae8f7a6cdd194c14d768de3d6dc"></a>

### `MCXW_CLK_DIV_BY_13`

```c
#define MCXW_CLK_DIV_BY_13 12
```

13 分频（Divide by 13）。

<a id="a38aaeee7732478e365d5e401ab321d64"></a>

### `MCXW_CLK_DIV_BY_14`

```c
#define MCXW_CLK_DIV_BY_14 13
```

14 分频（Divide by 14）。

<a id="ae5eda5611801b12370e21f209bbaa282"></a>

### `MCXW_CLK_DIV_BY_15`

```c
#define MCXW_CLK_DIV_BY_15 14
```

15 分频（Divide by 15）。

<a id="ab17b8449c5f4c683b6503ea3d00bb163"></a>

### `MCXW_CLK_DIV_BY_16`

```c
#define MCXW_CLK_DIV_BY_16 15
```

16 分频（Divide by 16）。

<a id="a1a5e445e26dd9acfd313af91b46a3bd4"></a>

### `MCXW_CLK_DIV_BY_2`

```c
#define MCXW_CLK_DIV_BY_2 1
```

2 分频（Divide by 2）。

<a id="ad67ab40b6b903d1b790cfdb223fe9ba0"></a>

### `MCXW_CLK_DIV_BY_3`

```c
#define MCXW_CLK_DIV_BY_3 2
```

3 分频（Divide by 3）。

<a id="a6d1bcc656dfaf86e32f0ec7e47c91fbf"></a>

### `MCXW_CLK_DIV_BY_4`

```c
#define MCXW_CLK_DIV_BY_4 3
```

4 分频（Divide by 4）。

<a id="ac001bad69869ab50ec1e019c46e3b52c"></a>

### `MCXW_CLK_DIV_BY_5`

```c
#define MCXW_CLK_DIV_BY_5 4
```

5 分频（Divide by 5）。

<a id="af6d3d08aa4245bc1f946ddb4b06f1b40"></a>

### `MCXW_CLK_DIV_BY_6`

```c
#define MCXW_CLK_DIV_BY_6 5
```

6 分频（Divide by 6）。

<a id="acc61c7a4b274638ac02acea373f345dd"></a>

### `MCXW_CLK_DIV_BY_7`

```c
#define MCXW_CLK_DIV_BY_7 6
```

7 分频（Divide by 7）。

<a id="a15df301cd186a8b348e8da9c41577f3a"></a>

### `MCXW_CLK_DIV_BY_8`

```c
#define MCXW_CLK_DIV_BY_8 7
```

8 分频（Divide by 8）。

<a id="a08a00775e88b21ddedf139d9b21bf18e"></a>

### `MCXW_CLK_DIV_NONE`

```c
#define MCXW_CLK_DIV_NONE 0
```

不改变分频（Divider），等同于 `MCXW_CLK_DIV_BY_1`。

<a id="a575dcc55e7aaeff512b21a85a290005c"></a>

### `MCXW_CLK_FIRC_DISABLE`

```c
#define MCXW_CLK_FIRC_DISABLE 0
```

禁用快速内部 RC 振荡器（FIRC）。

<a id="ad0936d3984812dcdcb6673ba2b71a680"></a>

### `MCXW_CLK_FIRC_ENABLE`

```c
#define MCXW_CLK_FIRC_ENABLE 1
```

启用快速内部 RC 振荡器（FIRC）。

<a id="a41e2a2852ae3fb5e1bd8eddc0471c93d"></a>

### `MCXW_CLK_FIRC_ENABLE_IN_LP`

```c
#define MCXW_CLK_FIRC_ENABLE_IN_LP 2
```

在低功耗模式（Low-Power Mode）下启用快速内部 RC 振荡器（FIRC）。

<a id="a5e32c9d70f8fb8f57fbdec1cafacb183"></a>

### `MCXW_CLK_FIRC_RANGE_192MHZ`

```c
#define MCXW_CLK_FIRC_RANGE_192MHZ 3
```

快速内部 RC 振荡器（FIRC）范围：192 MHz。

<a id="aceaaa53b2ef24965b87980d82ccd1d71"></a>

### `MCXW_CLK_FIRC_RANGE_48MHZ`

```c
#define MCXW_CLK_FIRC_RANGE_48MHZ 0
```

快速内部 RC 振荡器（FIRC）范围：48 MHz。

<a id="ae942bd0c3ac7cdaea097f92c65b33c0c"></a>

### `MCXW_CLK_FIRC_RANGE_64MHZ`

```c
#define MCXW_CLK_FIRC_RANGE_64MHZ 1
```

快速内部 RC 振荡器（FIRC）范围：64 MHz。

<a id="a30c8090495abf07e0e26fc89ca2e5593"></a>

### `MCXW_CLK_FIRC_RANGE_96MHZ`

```c
#define MCXW_CLK_FIRC_RANGE_96MHZ 2
```

快速内部 RC 振荡器（FIRC）范围：96 MHz。

<a id="a2b5ce49932aa4aaa775fe80d6b2ee656"></a>

### `MCXW_CLK_IP_MUX_1M`

```c
#define MCXW_CLK_IP_MUX_1M 7
```

由 FRO6M 派生的 1 MHz 时钟；仅 MCXW70 支持。

<a id="abb0f0c933ce8376753666aa7211e7c24"></a>

### `MCXW_CLK_IP_MUX_32K`

```c
#define MCXW_CLK_IP_MUX_32K 5
```

32 kHz 时钟（Clock），`kCLOCK_IpSrc32kClk`。

<a id="a2d558dab24029d7ed08aa5c791a1be49"></a>

### `MCXW_CLK_IP_MUX_FRO_192M_DIV`

```c
#define MCXW_CLK_IP_MUX_FRO_192M_DIV 3
```

自由运行振荡器（FRO）192 MHz 分频时钟，频率取决于范围设置。

<a id="aeca4e40941dee1717fa357501d6c8410"></a>

### `MCXW_CLK_IP_MUX_FRO_200M_DIV`

```c
#define MCXW_CLK_IP_MUX_FRO_200M_DIV 6
```

自由运行振荡器（FRO）200 MHz，用于 CAN；仅 MCXW70 支持。

<a id="a0cc00d635bbdce56db9ce9335726c1d5"></a>

### `MCXW_CLK_IP_MUX_FRO_6M`

```c
#define MCXW_CLK_IP_MUX_FRO_6M 2
```

自由运行振荡器（FRO）6 MHz 时钟，`kCLOCK_IpSrcFro6M`。

**说明（Note）**：注（Note）：勘误 ERR052742——某些芯片上的 FRO6M 时钟（`kCLOCK_IpSrcFro6M`）可能不稳定：复位或低功耗唤醒后，输出频率可能低于预期。在要求稳定性的场合应避免使用 FRO6M；条件允许时优先选择更高频率的 FRO 时钟源。

<a id="a079ba179088bdda8a053e8163a9ecebf"></a>

### `MCXW_CLK_IP_MUX_NONE`

```c
#define MCXW_CLK_IP_MUX_NONE 0xFF
```

无外设 IP 多路复用选择（IP Mux Selection）／无效值。

<a id="a3b4a0a8d639d80c336d805d46af5ac33"></a>

### `MCXW_CLK_IP_MUX_SLOW_CLK`

```c
#define MCXW_CLK_IP_MUX_SLOW_CLK 1
```

慢速时钟源（Slow Clock Source）。

<a id="aabed45808ee538aebfec10df0034d20a"></a>

### `MCXW_CLK_IP_MUX_SOSC`

```c
#define MCXW_CLK_IP_MUX_SOSC 4
```

SOSC：射频振荡器时钟（RF Oscillator Clock），`kCLOCK_IpSrcSoscClk`。

<a id="a5d6b4be6587c741d96c2492c6f334ec9"></a>

### `MCXW_CLK_LP_NO_STALL`

```c
#define MCXW_CLK_LP_NO_STALL 2U
```

时钟不会阻止进入低功耗状态（Low-Power Entry），不会使其等待（No Stall）。

<a id="a487ca0a3e7ddf59139b9981198b1fb4a"></a>

### `MCXW_CLK_LP_STALL_ALLOWED`

```c
#define MCXW_CLK_LP_STALL_ALLOWED 0U
```

时钟可阻止进入低功耗状态（Low-Power Entry），会使其等待（Stall）。

<a id="aac8723ce4534f2f1041281bdbc41e994"></a>

### `MCXW_CLK_MODE_DISABLED`

```c
#define MCXW_CLK_MODE_DISABLED (MCXW_CLK_CTRL_DISABLED)
```

禁用模式（Disabled Mode）。

<a id="a6a81d1a5a76fe0d67a8af1a1011031fe"></a>

### `MCXW_CLK_MODE_ENABLED_LP_NO_STALL`

```c
#define MCXW_CLK_MODE_ENABLED_LP_NO_STALL (MCXW_CLK_CTRL_ENABLED | MCXW_CLK_LP_NO_STALL)
```

已启用；不会使低功耗进入流程等待（Won't Stall LP）。

<a id="ad8f488bad33a11b2fed3c8b0cda959bb"></a>

### `MCXW_CLK_MODE_ENABLED_LP_STALL`

```c
#define MCXW_CLK_MODE_ENABLED_LP_STALL (MCXW_CLK_CTRL_ENABLED | MCXW_CLK_LP_STALL_ALLOWED)
```

已启用；可能使低功耗进入流程等待（Stall LP）。

<a id="a49e1a94c972d6b16322a368c16641676"></a>

### `MCXW_CLK_OSC32K_BYPASS`

```c
#define MCXW_CLK_OSC32K_BYPASS 3
```

旁路 32K 振荡器（Bypass），使用外部时钟（External Clock）。

<a id="a260db29cde74f0226ebfec58486a49b4"></a>

### `MCXW_CLK_OSC32K_CAP_0PF`

```c
#define MCXW_CLK_OSC32K_CAP_0PF 0
```

内部电容（Internal Capacitance）为 0 pF。

<a id="a04df19a313ddc6f2d5bdfbd1ee00c8cf"></a>

### `MCXW_CLK_OSC32K_CAP_10PF`

```c
#define MCXW_CLK_OSC32K_CAP_10PF 5
```

内部电容（Internal Capacitance）为 10 pF。

<a id="a054becc9e2c3355e59cf6afc1f1a2216"></a>

### `MCXW_CLK_OSC32K_CAP_12PF`

```c
#define MCXW_CLK_OSC32K_CAP_12PF 6
```

内部电容（Internal Capacitance）为 12 pF。

<a id="a82219a0b4235dda30fd098f9e1d772c9"></a>

### `MCXW_CLK_OSC32K_CAP_14PF`

```c
#define MCXW_CLK_OSC32K_CAP_14PF 7
```

内部电容（Internal Capacitance）为 14 pF。

<a id="a10e5d75da66b5e3c3447a32ba7968e74"></a>

### `MCXW_CLK_OSC32K_CAP_16PF`

```c
#define MCXW_CLK_OSC32K_CAP_16PF 8
```

内部电容（Internal Capacitance）为 16 pF。

<a id="a43c0106192089d39266def8ba62b1999"></a>

### `MCXW_CLK_OSC32K_CAP_18PF`

```c
#define MCXW_CLK_OSC32K_CAP_18PF 9
```

内部电容（Internal Capacitance）为 18 pF。

<a id="a722c71f3f1d715aee1123cbbfdefddaa"></a>

### `MCXW_CLK_OSC32K_CAP_20PF`

```c
#define MCXW_CLK_OSC32K_CAP_20PF 10
```

内部电容（Internal Capacitance）为 20 pF。

<a id="a7b0b4b82806eda2c24f7dfd7c3035b82"></a>

### `MCXW_CLK_OSC32K_CAP_22PF`

```c
#define MCXW_CLK_OSC32K_CAP_22PF 11
```

内部电容（Internal Capacitance）为 22 pF。

<a id="a65964ab3f92482b9ec8f115f1273bac1"></a>

### `MCXW_CLK_OSC32K_CAP_24PF`

```c
#define MCXW_CLK_OSC32K_CAP_24PF 12
```

内部电容（Internal Capacitance）为 24 pF。

<a id="a22f279ceb7e4902eedb39bf0651e1981"></a>

### `MCXW_CLK_OSC32K_CAP_26PF`

```c
#define MCXW_CLK_OSC32K_CAP_26PF 13
```

内部电容（Internal Capacitance）为 26 pF。

<a id="a18903ab29f3d2641d7664beb48510818"></a>

### `MCXW_CLK_OSC32K_CAP_28PF`

```c
#define MCXW_CLK_OSC32K_CAP_28PF 14
```

内部电容（Internal Capacitance）为 28 pF。

<a id="aada508e5912d82cf8bcf71c9258bf460"></a>

### `MCXW_CLK_OSC32K_CAP_2PF`

```c
#define MCXW_CLK_OSC32K_CAP_2PF 1
```

内部电容（Internal Capacitance）为 2 pF。

<a id="a82533cb21bc8a71815e4b6d03d15758d"></a>

### `MCXW_CLK_OSC32K_CAP_30PF`

```c
#define MCXW_CLK_OSC32K_CAP_30PF 15
```

内部电容（Internal Capacitance）为 30 pF。

<a id="a7a03c8af2b88437d75b812decd5d7c39"></a>

### `MCXW_CLK_OSC32K_CAP_4PF`

```c
#define MCXW_CLK_OSC32K_CAP_4PF 2
```

内部电容（Internal Capacitance）为 4 pF。

<a id="a88528c7784dcd0d418e04ebf4ca17eee"></a>

### `MCXW_CLK_OSC32K_CAP_6PF`

```c
#define MCXW_CLK_OSC32K_CAP_6PF 3
```

内部电容（Internal Capacitance）为 6 pF。

<a id="abe321a1905411b9f706966c5061d50b3"></a>

### `MCXW_CLK_OSC32K_CAP_8PF`

```c
#define MCXW_CLK_OSC32K_CAP_8PF 4
```

内部电容（Internal Capacitance）为 8 pF。

<a id="a2c64d094664c3e775dd09a0aa288a91d"></a>

### `MCXW_CLK_OSC32K_COARSE_RANGE0`

```c
#define MCXW_CLK_OSC32K_COARSE_RANGE0 0
```

放大器粗调增益（Coarse Amplifier Gain）范围 0。

<a id="aa11e25f4c50d193b13aa0398eb67ca3b"></a>

### `MCXW_CLK_OSC32K_COARSE_RANGE1`

```c
#define MCXW_CLK_OSC32K_COARSE_RANGE1 1
```

放大器粗调增益（Coarse Amplifier Gain）范围 1。

<a id="a555c3721c4aa3132d01e58e46ddce177"></a>

### `MCXW_CLK_OSC32K_COARSE_RANGE2`

```c
#define MCXW_CLK_OSC32K_COARSE_RANGE2 2
```

放大器粗调增益（Coarse Amplifier Gain）范围 2。

<a id="a4e97219d6e9027ad3169348cecad8920"></a>

### `MCXW_CLK_OSC32K_COARSE_RANGE3`

```c
#define MCXW_CLK_OSC32K_COARSE_RANGE3 3
```

放大器粗调增益（Coarse Amplifier Gain）范围 3。

<a id="a76617c20053432fbbf9a3b514612672a"></a>

### `MCXW_CLK_OSC32K_DISABLE`

```c
#define MCXW_CLK_OSC32K_DISABLE 0
```

禁用 32K 振荡器模式（Oscillator Mode）。

<a id="a1f5fb1d0ef7661acd08daff786e69784"></a>

### `MCXW_CLK_OSC32K_ENABLE`

```c
#define MCXW_CLK_OSC32K_ENABLE 1
```

启用 32K 振荡器模式（Oscillator Mode）。

<a id="a051a2a0932ac96f438363497dc56092b"></a>

### `MCXW_CLK_SYSTEM_CLK_SRC_FIRC`

```c
#define MCXW_CLK_SYSTEM_CLK_SRC_FIRC 3
```

系统时钟：FIRC，快速内部 RC 振荡器（Fast Internal RC）。

<a id="af86b46afe036b31cc8d551a3e72c1896"></a>

### `MCXW_CLK_SYSTEM_CLK_SRC_ROSC`

```c
#define MCXW_CLK_SYSTEM_CLK_SRC_ROSC 4
```

系统时钟：ROSC，环形振荡器（Ring Oscillator）。

<a id="a8122561ce50e3dc728ad1a50989eb6be"></a>

### `MCXW_CLK_SYSTEM_CLK_SRC_SIRC`

```c
#define MCXW_CLK_SYSTEM_CLK_SRC_SIRC 2
```

系统时钟：SIRC，内部慢速 RC 振荡器（Internal Slow RC）。

<a id="ad3fd21e228934ab0b9fe990b7df4eb2d"></a>

### `MCXW_CLK_SYSTEM_CLK_SRC_SOSC`

```c
#define MCXW_CLK_SYSTEM_CLK_SRC_SOSC 1
```

系统时钟：SOSC，外部振荡器（External Oscillator）。

<a id="ace217387a298100d7e0ef9fb24ed5d08"></a>

### `MCXW_CLOCK`

```c
#define MCXW_CLOCK ( mrcc_offset, clk_mux, clk_div, flag )
```

展开值（Value）：

```c
((((mrcc_offset) & 0xFFFF) << 16) | (((clk_mux) & 0xFF) << 8) | (((clk_div) & 0xF) << 4) | \
 (((flag) & 0xF)))
```

用于将时钟配置（Clock Configuration）编码为设备树绑定所用 32 位整数的辅助宏。

位布局（Bit Layout），从最高有效位（MSB）到最低有效位（LSB）：

- `[31:16]`：`mrcc_offset`，16 位（Bits）。
- `[15:8]`：`clk_mux`，8 位（Bits）。
- `[7:4]`：`clk_div`，4 位（Bits）。
- `[3:0]`：`flag`，4 位（Bits）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mrcc_offset` | MRCC 寄存器偏移（Register Offset），16 位。 |
| `clk_mux` | 时钟多路复用选择（Clock Multiplexer Selection），8 位。 |
| `clk_div` | 时钟分频值（Clock Divider Value），4 位。 |
| `flag` | 控制／行为标志（Control/Behavior Flags），4 位。 |


## 3.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P622_nxp_mcxw7x_clock.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P002_zephyr__drivers__mfd__max2221x.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__bluetooth__services__ots.h_文件参考.md)
