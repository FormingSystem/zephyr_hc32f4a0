---
id: learning.zephyr-docs.api-scoped-clock-topic-reference.page-7
title: Silicon Labs SiWx91x 时钟标识符（Clock identifiers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_Silicon Labs SiWx91x 时钟标识符（Clock identifiers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

供 SiWx91x 常开域／高功率域／超低功耗域（AON/HP/ULP）时钟管理器使用的时钟标识符（Clock Identifiers）。例如 HP_REF_ULP 这样的参考时钟名称，表示来自 HP 域的 ULP 参考时钟。

<a id="header-files"></a>
<a id="files"></a>

## 7.1\_文件（Files）

<a id="r_siwx91x-clock_2Eh"></a>

```c
file siwx91x-clock.h
```

相关声明：[siwx91x-clock.h](../api_file_flash_test_reference/P013_zephyr__dt-bindings__clock__silabs__siwx91x-clock.h_文件参考.md)。

Silicon Labs SiWx91x设备的时钟标识符（Clock Identifiers）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.2\_宏定义（Macros）

<a id="r_gaa994575e4e81c3c7abc88f87d1ce2018"></a>

```c
#define SIWX91X_CLK_GATED 47
```

相关声明：[SIWX91X_CLK_GATED](#gaa994575e4e81c3c7abc88f87d1ce2018)。

已门控／禁用的时钟源（Gated/Disabled Clock Source）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 7.3\_高功率域时钟（HP / High Power Clocks）

<a id="r_gaa73343f38c9b08dc13b3a907a757abf3"></a>

```c
#define SIWX91X_CLK_UART0 0
```

相关声明：[SIWX91X_CLK_UART0](#gaa73343f38c9b08dc13b3a907a757abf3)。

UART0 时钟（Clock）。

<a id="r_ga22c3da15ca23aa0cf14eae47ecf68e1c"></a>

```c
#define SIWX91X_CLK_UART1 1
```

相关声明：[SIWX91X_CLK_UART1](#ga22c3da15ca23aa0cf14eae47ecf68e1c)。

UART1 时钟（Clock）。

<a id="r_gabf6e7add31fdd04634edcc9ce2e7a424"></a>

```c
#define SIWX91X_CLK_I2C0 2
```

相关声明：[SIWX91X_CLK_I2C0](#gabf6e7add31fdd04634edcc9ce2e7a424)。

I2C0 时钟（Clock）。

<a id="r_gafcacbbd065793805e6b947373fa34b98"></a>

```c
#define SIWX91X_CLK_I2C1 3
```

相关声明：[SIWX91X_CLK_I2C1](#gafcacbbd065793805e6b947373fa34b98)。

I2C1 时钟（Clock）。

<a id="r_ga156fadba39a730250b319d5866357d2f"></a>

```c
#define SIWX91X_CLK_UDMA 4
```

相关声明：[SIWX91X_CLK_UDMA](#ga156fadba39a730250b319d5866357d2f)。

UDMA 时钟（Clock）。

<a id="r_ga3fe9ef6574ed9ced3082bc889aaf3215"></a>

```c
#define SIWX91X_CLK_PWM 5
```

相关声明：[SIWX91X_CLK_PWM](#ga3fe9ef6574ed9ced3082bc889aaf3215)。

PWM 时钟（Clock）。

<a id="r_gaf44b544d40037b7264cb10e4e392d0e8"></a>

```c
#define SIWX91X_CLK_GSPI 6
```

相关声明：[SIWX91X_CLK_GSPI](#gaf44b544d40037b7264cb10e4e392d0e8)。

GSPI 时钟（Clock）。

<a id="r_ga440d4643be3eee9bf8948d8edf18ad06"></a>

```c
#define SIWX91X_CLK_QSPI 7
```

相关声明：[SIWX91X_CLK_QSPI](#ga440d4643be3eee9bf8948d8edf18ad06)。

QSPI 时钟（Clock）。

<a id="r_ga25d1b9e39822fc1f9c87e97ae2532887"></a>

```c
#define SIWX91X_CLK_QSPI2 8
```

相关声明：[SIWX91X_CLK_QSPI2](#ga25d1b9e39822fc1f9c87e97ae2532887)。

QSPI2 时钟（Clock）。

<a id="r_ga686cd422cd784493a68d160e76c1cc69"></a>

```c
#define SIWX91X_CLK_I2S 9
```

相关声明：[SIWX91X_CLK_I2S](#ga686cd422cd784493a68d160e76c1cc69)。

I2S 时钟（Clock）。

<a id="r_ga70dc54120ac5e1684de3ffc8e62c4cea"></a>

```c
#define SIWX91X_CLK_STATIC_I2S 10
```

相关声明：[SIWX91X_CLK_STATIC_I2S](#ga70dc54120ac5e1684de3ffc8e62c4cea)。

静态 I2S 外部主时钟输入（Static I2S External Master-clock Input）。

<a id="r_ga47c4f4859be28d1d55e9c362963c0c05"></a>

```c
#define SIWX91X_CLK_GPDMA 11
```

相关声明：[SIWX91X_CLK_GPDMA](#ga47c4f4859be28d1d55e9c362963c0c05)。

GPDMA 时钟（Clock）。

<a id="r_gad6832ece2f138df8cba192084b8886aa"></a>

```c
#define SIWX91X_CLK_RNG 12
```

相关声明：[SIWX91X_CLK_RNG](#gad6832ece2f138df8cba192084b8886aa)。

RNG 时钟（Clock）。

<a id="r_ga6e24d8b833c882777c352ff653ee98a2"></a>

```c
#define SIWX91X_CLK_GPIO 13
```

相关声明：[SIWX91X_CLK_GPIO](#ga6e24d8b833c882777c352ff653ee98a2)。

GPIO 时钟（Clock）。

<a id="r_ga7d75a6726e0b708c99f6a60ea25e8f33"></a>

```c
#define SIWX91X_CLK_SSI 14
```

相关声明：[SIWX91X_CLK_SSI](#ga7d75a6726e0b708c99f6a60ea25e8f33)。

SSI 时钟（Clock）。

<a id="r_ga58be24bef62c94f02d7edbd6c927d6a8"></a>

```c
#define SIWX91X_CLK_PIN_OUT 15
```

相关声明：[SIWX91X_CLK_PIN_OUT](#ga58be24bef62c94f02d7edbd6c927d6a8)。

引脚时钟输出（Pin Clock Output，OUT_CLK）。

<a id="r_ga9512edf3d45357b740b6a723ff60e0d9"></a>

```c
#define SIWX91X_CLK_ICACHE 16
```

相关声明：[SIWX91X_CLK_ICACHE](#ga9512edf3d45357b740b6a723ff60e0d9)。

指令缓存时钟（Instruction Cache Clock）。

<a id="r_gae05159b5f02584c2ca6c84d1f714deb2"></a>

```c
#define SIWX91X_CLK_CPU 17
```

相关声明：[SIWX91X_CLK_CPU](#gae05159b5f02584c2ca6c84d1f714deb2)。

CPU／处理器时钟（Processor Clock，PROC）。

<a id="r_gad4b861be1920bb84b2557bda775dbcc9"></a>

```c
#define SIWX91X_CLK_CPU_LP 18
```

相关声明：[SIWX91X_CLK_CPU_LP](#gad4b861be1920bb84b2557bda775dbcc9)。

CPU 低功耗时钟（Low-power Clock，MCU_LP），不受支持。

<a id="r_ga598b2599c45a49bc04201f16c434a4f6"></a>

```c
#define SIWX91X_CLK_HP_REF_ULP 19
```

相关声明：[SIWX91X_CLK_HP_REF_ULP](#ga598b2599c45a49bc04201f16c434a4f6)。

来自高功率域（HP Domain）的超低功耗参考时钟（ULP Reference，HP_ULP）。

<a id="r_ga642d1132e759af66971509acd36b88d4"></a>

```c
#define SIWX91X_CLK_HP_REF_PLL 20
```

相关声明：[SIWX91X_CLK_HP_REF_PLL](#ga642d1132e759af66971509acd36b88d4)。

锁相环参考时钟（PLL Reference Clock，PLL_REF）。

<a id="r_ga763c234cb482057f8a22184bf5fd3d64"></a>

```c
#define SIWX91X_CLK_PLL_SOC 21
```

相关声明：[SIWX91X_CLK_PLL_SOC](#ga763c234cb482057f8a22184bf5fd3d64)。

SoC 锁相环（PLL，SOC_PLL）。

<a id="r_ga31b39a23904212b738f598be5bc68f1e"></a>

```c
#define SIWX91X_CLK_PLL_INTF 22
```

相关声明：[SIWX91X_CLK_PLL_INTF](#ga31b39a23904212b738f598be5bc68f1e)。

接口锁相环（Interface PLL，INTF_PLL）。

<a id="r_gaade542d0564ba0c8df00c09eb96b7af7"></a>

```c
#define SIWX91X_CLK_PLL_I2S 23
```

相关声明：[SIWX91X_CLK_PLL_I2S](#gaade542d0564ba0c8df00c09eb96b7af7)。

I2S 锁相环（PLL，I2S_PLL）。

## 7.4\_超低功耗域时钟（ULP / Ultra Low Power Clocks）

<a id="r_ga13540e36cfdfa08d3366a8b950baaf9b"></a>

```c
#define SIWX91X_CLK_ULP_UART 24
```

相关声明：[SIWX91X_CLK_ULP_UART](#ga13540e36cfdfa08d3366a8b950baaf9b)。

ULP UART 时钟（Clock）。

<a id="r_ga11659ca1dacf850b679bc35e7e042a71"></a>

```c
#define SIWX91X_CLK_ULP_I2C 25
```

相关声明：[SIWX91X_CLK_ULP_I2C](#ga11659ca1dacf850b679bc35e7e042a71)。

ULP I2C 时钟（Clock）。

<a id="r_gaab46a3e48482a427d2444939ab0b1510"></a>

```c
#define SIWX91X_CLK_ULP_UDMA 26
```

相关声明：[SIWX91X_CLK_ULP_UDMA](#gaab46a3e48482a427d2444939ab0b1510)。

ULP UDMA 时钟（Clock）。

<a id="r_ga3ce737e8d3b039ceab2fc756a054b0a7"></a>

```c
#define SIWX91X_CLK_ULP_I2S 27
```

相关声明：[SIWX91X_CLK_ULP_I2S](#ga3ce737e8d3b039ceab2fc756a054b0a7)。

ULP I2S 时钟（Clock）。

<a id="r_gace8cbc4cdf2e52d7e7795fb01bdaed46"></a>

```c
#define SIWX91X_CLK_ULP_STATIC_I2S 28
```

相关声明：[SIWX91X_CLK_ULP_STATIC_I2S](#gace8cbc4cdf2e52d7e7795fb01bdaed46)。

超低功耗（ULP）静态 I2S 外部主时钟输入（External Master-clock Input）。

<a id="r_gacfcaed1f3be6524a86451293bc1614bf"></a>

```c
#define SIWX91X_CLK_ULP_ADC 29
```

相关声明：[SIWX91X_CLK_ULP_ADC](#gacfcaed1f3be6524a86451293bc1614bf)。

ULP ADC 时钟（Clock）。

<a id="r_gabea4ada219e62d94a8dad1647e3a8ca5"></a>

```c
#define SIWX91X_CLK_ULP_SSI 30
```

相关声明：[SIWX91X_CLK_ULP_SSI](#gabea4ada219e62d94a8dad1647e3a8ca5)。

ULP SSI 时钟（Clock）。

<a id="r_gaa7f3b36033754a6e755033906dafff3e"></a>

```c
#define SIWX91X_CLK_ULP_TIMER 31
```

相关声明：[SIWX91X_CLK_ULP_TIMER](#gaa7f3b36033754a6e755033906dafff3e)。

超低功耗定时器时钟（ULP Timer Clock）。

<a id="r_ga4838311ae7753d444dfc739bec992aae"></a>

```c
#define SIWX91X_CLK_ULP_GPIO 32
```

相关声明：[SIWX91X_CLK_ULP_GPIO](#ga4838311ae7753d444dfc739bec992aae)。

ULP GPIO 时钟（Clock）。

<a id="r_ga1f873ad6c8b234b4f9ad0cc76eb08439"></a>

```c
#define SIWX91X_CLK_ULP_REF_AON 33
```

相关声明：[SIWX91X_CLK_ULP_REF_AON](#ga1f873ad6c8b234b4f9ad0cc76eb08439)。

来自超低功耗域（ULP Domain）的常开域参考时钟（AON Reference，SLP_SENSOR）。

<a id="r_ga6198bf110638c795ea5078b657fab8c5"></a>

```c
#define SIWX91X_CLK_ULP_REF_CPU 34
```

相关声明：[SIWX91X_CLK_ULP_REF_CPU](#ga6198bf110638c795ea5078b657fab8c5)。

来自超低功耗域（ULP Domain）的 CPU 参考时钟（CPU Reference，ULP_PROC）。

## 7.5\_常开域时钟（AON / Always-On Clocks）

<a id="r_gab469502645c214bcab0a7629c072e3ed"></a>

```c
#define SIWX91X_CLK_XTAL_MHZ 35
```

相关声明：[SIWX91X_CLK_XTAL_MHZ](#gab469502645c214bcab0a7629c072e3ed)。

高频晶体振荡器（High-frequency Crystal Oscillator）。

<a id="r_ga6c54a1d47730fb10d1915633a6d6e805"></a>

```c
#define SIWX91X_CLK_XTAL_KHZ 36
```

相关声明：[SIWX91X_CLK_XTAL_KHZ](#ga6c54a1d47730fb10d1915633a6d6e805)。

低频晶体振荡器（Low-frequency Crystal Oscillator）。

<a id="r_gaa2d8c618017ba3bbd7fbe22e57ffcc68"></a>

```c
#define SIWX91X_CLK_RC_MHZ 37
```

相关声明：[SIWX91X_CLK_RC_MHZ](#gaa2d8c618017ba3bbd7fbe22e57ffcc68)。

高频 RC 振荡器（High-frequency RC Oscillator）。

<a id="r_ga0f6262d3448237d6198d25172a5444c0"></a>

```c
#define SIWX91X_CLK_RC_KHZ 38
```

相关声明：[SIWX91X_CLK_RC_KHZ](#ga0f6262d3448237d6198d25172a5444c0)。

低频 RC 振荡器（Low-frequency RC Oscillator）。

<a id="r_gac7ea9290ed9f4162a187d900aaec9c9d"></a>

```c
#define SIWX91X_CLK_WATCHDOG 39
```

相关声明：[SIWX91X_CLK_WATCHDOG](#gac7ea9290ed9f4162a187d900aaec9c9d)。

看门狗时钟（Watchdog Clock）。

<a id="r_ga48441517f818774b29f83c96d3997609"></a>

```c
#define SIWX91X_CLK_RTC 40
```

相关声明：[SIWX91X_CLK_RTC](#ga48441517f818774b29f83c96d3997609)。

RTC 时钟（Clock）。

<a id="r_gab25836573ca2aa32fdcc169a7eab567c"></a>

```c
#define SIWX91X_CLK_SYSRTC 41
```

相关声明：[SIWX91X_CLK_SYSRTC](#gab25836573ca2aa32fdcc169a7eab567c)。

SYSRTC 时钟（Clock）。

<a id="r_ga228e1b2c0f4b7f3d5a024a311f7eccf2"></a>

```c
#define SIWX91X_CLK_UULP_GPIO 42
```

相关声明：[SIWX91X_CLK_UULP_GPIO](#ga228e1b2c0f4b7f3d5a024a311f7eccf2)。

UULP GPIO 时钟（Clock）。

<a id="r_ga3d584b157813a867e4828d47598ad00e"></a>

```c
#define SIWX91X_CLK_REF_HP 43
```

相关声明：[SIWX91X_CLK_REF_HP](#ga3d584b157813a867e4828d47598ad00e)。

高功率域参考时钟（HP Domain Reference，HP_REF）。

<a id="r_ga32d7900a5874721769eb6dcd4adef636"></a>

```c
#define SIWX91X_CLK_REF_ULP 44
```

相关声明：[SIWX91X_CLK_REF_ULP](#ga32d7900a5874721769eb6dcd4adef636)。

超低功耗域参考时钟（ULP Domain Reference，ULP_REF）。

<a id="r_gaba5a4438dfedba689d67a852d5fed09e"></a>

```c
#define SIWX91X_CLK_AON_REF_HF 45
```

相关声明：[SIWX91X_CLK_AON_REF_HF](#gaba5a4438dfedba689d67a852d5fed09e)。

常开域高频参考时钟（AON High-frequency Reference，UULP_HF_REF）。

<a id="r_gae72c5285844d7d5a370d60f32a837ba0"></a>

```c
#define SIWX91X_CLK_AON_REF_LF 46
```

相关声明：[SIWX91X_CLK_AON_REF_LF](#gae72c5285844d7d5a370d60f32a837ba0)。

常开域低频参考时钟（AON Low-frequency Reference，UULP_LF_REF）。

## 7.6\_详细说明（Detailed Documentation）

<a id="gaba5a4438dfedba689d67a852d5fed09e"></a>

### `SIWX91X_CLK_AON_REF_HF`

```c
#define SIWX91X_CLK_AON_REF_HF 45
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

常开域高频参考时钟（AON High-frequency Reference，UULP_HF_REF）。

<a id="gae72c5285844d7d5a370d60f32a837ba0"></a>

### `SIWX91X_CLK_AON_REF_LF`

```c
#define SIWX91X_CLK_AON_REF_LF 46
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

常开域低频参考时钟（AON Low-frequency Reference，UULP_LF_REF）。

<a id="gae05159b5f02584c2ca6c84d1f714deb2"></a>

### `SIWX91X_CLK_CPU`

```c
#define SIWX91X_CLK_CPU 17
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

CPU／处理器时钟（Processor Clock，PROC）。

<a id="gad4b861be1920bb84b2557bda775dbcc9"></a>

### `SIWX91X_CLK_CPU_LP`

```c
#define SIWX91X_CLK_CPU_LP 18
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

CPU 低功耗时钟（Low-power Clock，MCU_LP），不受支持。

<a id="gaa994575e4e81c3c7abc88f87d1ce2018"></a>

### `SIWX91X_CLK_GATED`

```c
#define SIWX91X_CLK_GATED 47
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

已门控／禁用的时钟源（Gated/Disabled Clock Source）。

<a id="ga47c4f4859be28d1d55e9c362963c0c05"></a>

### `SIWX91X_CLK_GPDMA`

```c
#define SIWX91X_CLK_GPDMA 11
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

GPDMA 时钟（Clock）。

<a id="ga6e24d8b833c882777c352ff653ee98a2"></a>

### `SIWX91X_CLK_GPIO`

```c
#define SIWX91X_CLK_GPIO 13
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

GPIO 时钟（Clock）。

<a id="gaf44b544d40037b7264cb10e4e392d0e8"></a>

### `SIWX91X_CLK_GSPI`

```c
#define SIWX91X_CLK_GSPI 6
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

GSPI 时钟（Clock）。

<a id="ga642d1132e759af66971509acd36b88d4"></a>

### `SIWX91X_CLK_HP_REF_PLL`

```c
#define SIWX91X_CLK_HP_REF_PLL 20
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

锁相环参考时钟（PLL Reference Clock，PLL_REF）。

<a id="ga598b2599c45a49bc04201f16c434a4f6"></a>

### `SIWX91X_CLK_HP_REF_ULP`

```c
#define SIWX91X_CLK_HP_REF_ULP 19
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

来自高功率域（HP Domain）的超低功耗参考时钟（ULP Reference，HP_ULP）。

<a id="gabf6e7add31fdd04634edcc9ce2e7a424"></a>

### `SIWX91X_CLK_I2C0`

```c
#define SIWX91X_CLK_I2C0 2
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

I2C0 时钟（Clock）。

<a id="gafcacbbd065793805e6b947373fa34b98"></a>

### `SIWX91X_CLK_I2C1`

```c
#define SIWX91X_CLK_I2C1 3
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

I2C1 时钟（Clock）。

<a id="ga686cd422cd784493a68d160e76c1cc69"></a>

### `SIWX91X_CLK_I2S`

```c
#define SIWX91X_CLK_I2S 9
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

I2S 时钟（Clock）。

<a id="ga9512edf3d45357b740b6a723ff60e0d9"></a>

### `SIWX91X_CLK_ICACHE`

```c
#define SIWX91X_CLK_ICACHE 16
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

指令缓存时钟（Instruction Cache Clock）。

<a id="ga58be24bef62c94f02d7edbd6c927d6a8"></a>

### `SIWX91X_CLK_PIN_OUT`

```c
#define SIWX91X_CLK_PIN_OUT 15
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

引脚时钟输出（Pin Clock Output，OUT_CLK）。

<a id="gaade542d0564ba0c8df00c09eb96b7af7"></a>

### `SIWX91X_CLK_PLL_I2S`

```c
#define SIWX91X_CLK_PLL_I2S 23
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

I2S 锁相环（PLL，I2S_PLL）。

<a id="ga31b39a23904212b738f598be5bc68f1e"></a>

### `SIWX91X_CLK_PLL_INTF`

```c
#define SIWX91X_CLK_PLL_INTF 22
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

接口锁相环（Interface PLL，INTF_PLL）。

<a id="ga763c234cb482057f8a22184bf5fd3d64"></a>

### `SIWX91X_CLK_PLL_SOC`

```c
#define SIWX91X_CLK_PLL_SOC 21
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

SoC 锁相环（PLL，SOC_PLL）。

<a id="ga3fe9ef6574ed9ced3082bc889aaf3215"></a>

### `SIWX91X_CLK_PWM`

```c
#define SIWX91X_CLK_PWM 5
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

PWM 时钟（Clock）。

<a id="ga440d4643be3eee9bf8948d8edf18ad06"></a>

### `SIWX91X_CLK_QSPI`

```c
#define SIWX91X_CLK_QSPI 7
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

QSPI 时钟（Clock）。

<a id="ga25d1b9e39822fc1f9c87e97ae2532887"></a>

### `SIWX91X_CLK_QSPI2`

```c
#define SIWX91X_CLK_QSPI2 8
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

QSPI2 时钟（Clock）。

<a id="ga0f6262d3448237d6198d25172a5444c0"></a>

### `SIWX91X_CLK_RC_KHZ`

```c
#define SIWX91X_CLK_RC_KHZ 38
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

低频 RC 振荡器（Low-frequency RC Oscillator）。

<a id="gaa2d8c618017ba3bbd7fbe22e57ffcc68"></a>

### `SIWX91X_CLK_RC_MHZ`

```c
#define SIWX91X_CLK_RC_MHZ 37
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

高频 RC 振荡器（High-frequency RC Oscillator）。

<a id="ga3d584b157813a867e4828d47598ad00e"></a>

### `SIWX91X_CLK_REF_HP`

```c
#define SIWX91X_CLK_REF_HP 43
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

高功率域参考时钟（HP Domain Reference，HP_REF）。

<a id="ga32d7900a5874721769eb6dcd4adef636"></a>

### `SIWX91X_CLK_REF_ULP`

```c
#define SIWX91X_CLK_REF_ULP 44
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

超低功耗域参考时钟（ULP Domain Reference，ULP_REF）。

<a id="gad6832ece2f138df8cba192084b8886aa"></a>

### `SIWX91X_CLK_RNG`

```c
#define SIWX91X_CLK_RNG 12
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

RNG 时钟（Clock）。

<a id="ga48441517f818774b29f83c96d3997609"></a>

### `SIWX91X_CLK_RTC`

```c
#define SIWX91X_CLK_RTC 40
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

RTC 时钟（Clock）。

<a id="ga7d75a6726e0b708c99f6a60ea25e8f33"></a>

### `SIWX91X_CLK_SSI`

```c
#define SIWX91X_CLK_SSI 14
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

SSI 时钟（Clock）。

<a id="ga70dc54120ac5e1684de3ffc8e62c4cea"></a>

### `SIWX91X_CLK_STATIC_I2S`

```c
#define SIWX91X_CLK_STATIC_I2S 10
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

静态 I2S 外部主时钟输入（Static I2S External Master-clock Input）。

<a id="gab25836573ca2aa32fdcc169a7eab567c"></a>

### `SIWX91X_CLK_SYSRTC`

```c
#define SIWX91X_CLK_SYSRTC 41
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

SYSRTC 时钟（Clock）。

<a id="gaa73343f38c9b08dc13b3a907a757abf3"></a>

### `SIWX91X_CLK_UART0`

```c
#define SIWX91X_CLK_UART0 0
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

UART0 时钟（Clock）。

<a id="ga22c3da15ca23aa0cf14eae47ecf68e1c"></a>

### `SIWX91X_CLK_UART1`

```c
#define SIWX91X_CLK_UART1 1
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

UART1 时钟（Clock）。

<a id="ga156fadba39a730250b319d5866357d2f"></a>

### `SIWX91X_CLK_UDMA`

```c
#define SIWX91X_CLK_UDMA 4
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

UDMA 时钟（Clock）。

<a id="gacfcaed1f3be6524a86451293bc1614bf"></a>

### `SIWX91X_CLK_ULP_ADC`

```c
#define SIWX91X_CLK_ULP_ADC 29
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

ULP ADC 时钟（Clock）。

<a id="ga4838311ae7753d444dfc739bec992aae"></a>

### `SIWX91X_CLK_ULP_GPIO`

```c
#define SIWX91X_CLK_ULP_GPIO 32
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

ULP GPIO 时钟（Clock）。

<a id="ga11659ca1dacf850b679bc35e7e042a71"></a>

### `SIWX91X_CLK_ULP_I2C`

```c
#define SIWX91X_CLK_ULP_I2C 25
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

ULP I2C 时钟（Clock）。

<a id="ga3ce737e8d3b039ceab2fc756a054b0a7"></a>

### `SIWX91X_CLK_ULP_I2S`

```c
#define SIWX91X_CLK_ULP_I2S 27
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

ULP I2S 时钟（Clock）。

<a id="ga1f873ad6c8b234b4f9ad0cc76eb08439"></a>

### `SIWX91X_CLK_ULP_REF_AON`

```c
#define SIWX91X_CLK_ULP_REF_AON 33
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

来自超低功耗域（ULP Domain）的常开域参考时钟（AON Reference，SLP_SENSOR）。

<a id="ga6198bf110638c795ea5078b657fab8c5"></a>

### `SIWX91X_CLK_ULP_REF_CPU`

```c
#define SIWX91X_CLK_ULP_REF_CPU 34
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

来自超低功耗域（ULP Domain）的 CPU 参考时钟（CPU Reference，ULP_PROC）。

<a id="gabea4ada219e62d94a8dad1647e3a8ca5"></a>

### `SIWX91X_CLK_ULP_SSI`

```c
#define SIWX91X_CLK_ULP_SSI 30
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

ULP SSI 时钟（Clock）。

<a id="gace8cbc4cdf2e52d7e7795fb01bdaed46"></a>

### `SIWX91X_CLK_ULP_STATIC_I2S`

```c
#define SIWX91X_CLK_ULP_STATIC_I2S 28
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

超低功耗（ULP）静态 I2S 外部主时钟输入（External Master-clock Input）。

<a id="gaa7f3b36033754a6e755033906dafff3e"></a>

### `SIWX91X_CLK_ULP_TIMER`

```c
#define SIWX91X_CLK_ULP_TIMER 31
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

超低功耗定时器时钟（ULP Timer Clock）。

<a id="ga13540e36cfdfa08d3366a8b950baaf9b"></a>

### `SIWX91X_CLK_ULP_UART`

```c
#define SIWX91X_CLK_ULP_UART 24
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

ULP UART 时钟（Clock）。

<a id="gaab46a3e48482a427d2444939ab0b1510"></a>

### `SIWX91X_CLK_ULP_UDMA`

```c
#define SIWX91X_CLK_ULP_UDMA 26
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

ULP UDMA 时钟（Clock）。

<a id="ga228e1b2c0f4b7f3d5a024a311f7eccf2"></a>

### `SIWX91X_CLK_UULP_GPIO`

```c
#define SIWX91X_CLK_UULP_GPIO 42
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

UULP GPIO 时钟（Clock）。

<a id="gac7ea9290ed9f4162a187d900aaec9c9d"></a>

### `SIWX91X_CLK_WATCHDOG`

```c
#define SIWX91X_CLK_WATCHDOG 39
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

看门狗时钟（Watchdog Clock）。

<a id="ga6c54a1d47730fb10d1915633a6d6e805"></a>

### `SIWX91X_CLK_XTAL_KHZ`

```c
#define SIWX91X_CLK_XTAL_KHZ 36
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

低频晶体振荡器（Low-frequency Crystal Oscillator）。

<a id="gab469502645c214bcab0a7629c072e3ed"></a>

### `SIWX91X_CLK_XTAL_MHZ`

```c
#define SIWX91X_CLK_XTAL_MHZ 35
```

```c
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>
```

高频晶体振荡器（High-frequency Crystal Oscillator）。


## 7.7\_原页交叉引用（Cross References）

- [siwx91x-clock.h](../api_file_flash_test_reference/P013_zephyr__dt-bindings__clock__silabs__siwx91x-clock.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P006_清理辅助接口（Cleanup Helper Interface）.md) · [返回大纲](大纲.md) · [下一章](P008_Nordic nRF API主题.md)
