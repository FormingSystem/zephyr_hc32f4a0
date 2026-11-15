---
id: learning.zephyr-docs.api-file-flash-test-reference.page-13
title: zephyr__dt-bindings__clock__silabs__siwx91x-clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/siwx91x-clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_zephyr\_\_dt-bindings\_\_clock\_\_silabs\_\_siwx91x-clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/siwx91x-clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Silicon Labs SiWx91x设备的时钟标识符（Clock Identifiers）。

查看此文件的源码。

<a id="details"></a>

Silicon Labs SiWx91x设备的时钟标识符（Clock Identifiers）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 13.1\_宏定义（Macros）

<a id="r_gaa994575e4e81c3c7abc88f87d1ce2018"></a>

```c
#define SIWX91X_CLK_GATED 47
```

相关声明：[SIWX91X_CLK_GATED](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gaa994575e4e81c3c7abc88f87d1ce2018)。

已门控／禁用的时钟源（Gated/Disabled Clock Source）。

<a id="define-members-0"></a>

### 高功率域时钟（HP / High Power Clocks）

<a id="r_gaa73343f38c9b08dc13b3a907a757abf3"></a>

```c
#define SIWX91X_CLK_UART0 0
```

相关声明：[SIWX91X_CLK_UART0](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gaa73343f38c9b08dc13b3a907a757abf3)。

UART0 时钟（Clock）。

<a id="r_ga22c3da15ca23aa0cf14eae47ecf68e1c"></a>

```c
#define SIWX91X_CLK_UART1 1
```

相关声明：[SIWX91X_CLK_UART1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga22c3da15ca23aa0cf14eae47ecf68e1c)。

UART1 时钟（Clock）。

<a id="r_gabf6e7add31fdd04634edcc9ce2e7a424"></a>

```c
#define SIWX91X_CLK_I2C0 2
```

相关声明：[SIWX91X_CLK_I2C0](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gabf6e7add31fdd04634edcc9ce2e7a424)。

I2C0 时钟（Clock）。

<a id="r_gafcacbbd065793805e6b947373fa34b98"></a>

```c
#define SIWX91X_CLK_I2C1 3
```

相关声明：[SIWX91X_CLK_I2C1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gafcacbbd065793805e6b947373fa34b98)。

I2C1 时钟（Clock）。

<a id="r_ga156fadba39a730250b319d5866357d2f"></a>

```c
#define SIWX91X_CLK_UDMA 4
```

相关声明：[SIWX91X_CLK_UDMA](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga156fadba39a730250b319d5866357d2f)。

UDMA 时钟（Clock）。

<a id="r_ga3fe9ef6574ed9ced3082bc889aaf3215"></a>

```c
#define SIWX91X_CLK_PWM 5
```

相关声明：[SIWX91X_CLK_PWM](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga3fe9ef6574ed9ced3082bc889aaf3215)。

PWM 时钟（Clock）。

<a id="r_gaf44b544d40037b7264cb10e4e392d0e8"></a>

```c
#define SIWX91X_CLK_GSPI 6
```

相关声明：[SIWX91X_CLK_GSPI](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gaf44b544d40037b7264cb10e4e392d0e8)。

GSPI 时钟（Clock）。

<a id="r_ga440d4643be3eee9bf8948d8edf18ad06"></a>

```c
#define SIWX91X_CLK_QSPI 7
```

相关声明：[SIWX91X_CLK_QSPI](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga440d4643be3eee9bf8948d8edf18ad06)。

QSPI 时钟（Clock）。

<a id="r_ga25d1b9e39822fc1f9c87e97ae2532887"></a>

```c
#define SIWX91X_CLK_QSPI2 8
```

相关声明：[SIWX91X_CLK_QSPI2](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga25d1b9e39822fc1f9c87e97ae2532887)。

QSPI2 时钟（Clock）。

<a id="r_ga686cd422cd784493a68d160e76c1cc69"></a>

```c
#define SIWX91X_CLK_I2S 9
```

相关声明：[SIWX91X_CLK_I2S](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga686cd422cd784493a68d160e76c1cc69)。

I2S 时钟（Clock）。

<a id="r_ga70dc54120ac5e1684de3ffc8e62c4cea"></a>

```c
#define SIWX91X_CLK_STATIC_I2S 10
```

相关声明：[SIWX91X_CLK_STATIC_I2S](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga70dc54120ac5e1684de3ffc8e62c4cea)。

静态 I2S 外部主时钟输入（Static I2S External Master-clock Input）。

<a id="r_ga47c4f4859be28d1d55e9c362963c0c05"></a>

```c
#define SIWX91X_CLK_GPDMA 11
```

相关声明：[SIWX91X_CLK_GPDMA](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga47c4f4859be28d1d55e9c362963c0c05)。

GPDMA 时钟（Clock）。

<a id="r_gad6832ece2f138df8cba192084b8886aa"></a>

```c
#define SIWX91X_CLK_RNG 12
```

相关声明：[SIWX91X_CLK_RNG](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gad6832ece2f138df8cba192084b8886aa)。

RNG 时钟（Clock）。

<a id="r_ga6e24d8b833c882777c352ff653ee98a2"></a>

```c
#define SIWX91X_CLK_GPIO 13
```

相关声明：[SIWX91X_CLK_GPIO](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga6e24d8b833c882777c352ff653ee98a2)。

GPIO 时钟（Clock）。

<a id="r_ga7d75a6726e0b708c99f6a60ea25e8f33"></a>

```c
#define SIWX91X_CLK_SSI 14
```

相关声明：[SIWX91X_CLK_SSI](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga7d75a6726e0b708c99f6a60ea25e8f33)。

SSI 时钟（Clock）。

<a id="r_ga58be24bef62c94f02d7edbd6c927d6a8"></a>

```c
#define SIWX91X_CLK_PIN_OUT 15
```

相关声明：[SIWX91X_CLK_PIN_OUT](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga58be24bef62c94f02d7edbd6c927d6a8)。

引脚时钟输出（Pin Clock Output，OUT_CLK）。

<a id="r_ga9512edf3d45357b740b6a723ff60e0d9"></a>

```c
#define SIWX91X_CLK_ICACHE 16
```

相关声明：[SIWX91X_CLK_ICACHE](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga9512edf3d45357b740b6a723ff60e0d9)。

指令缓存时钟（Instruction Cache Clock）。

<a id="r_gae05159b5f02584c2ca6c84d1f714deb2"></a>

```c
#define SIWX91X_CLK_CPU 17
```

相关声明：[SIWX91X_CLK_CPU](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gae05159b5f02584c2ca6c84d1f714deb2)。

CPU／处理器时钟（Processor Clock，PROC）。

<a id="r_gad4b861be1920bb84b2557bda775dbcc9"></a>

```c
#define SIWX91X_CLK_CPU_LP 18
```

相关声明：[SIWX91X_CLK_CPU_LP](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gad4b861be1920bb84b2557bda775dbcc9)。

CPU 低功耗时钟（Low-power Clock，MCU_LP），不受支持。

<a id="r_ga598b2599c45a49bc04201f16c434a4f6"></a>

```c
#define SIWX91X_CLK_HP_REF_ULP 19
```

相关声明：[SIWX91X_CLK_HP_REF_ULP](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga598b2599c45a49bc04201f16c434a4f6)。

来自高功率域（HP Domain）的超低功耗参考时钟（ULP Reference，HP_ULP）。

<a id="r_ga642d1132e759af66971509acd36b88d4"></a>

```c
#define SIWX91X_CLK_HP_REF_PLL 20
```

相关声明：[SIWX91X_CLK_HP_REF_PLL](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga642d1132e759af66971509acd36b88d4)。

锁相环参考时钟（PLL Reference Clock，PLL_REF）。

<a id="r_ga763c234cb482057f8a22184bf5fd3d64"></a>

```c
#define SIWX91X_CLK_PLL_SOC 21
```

相关声明：[SIWX91X_CLK_PLL_SOC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga763c234cb482057f8a22184bf5fd3d64)。

SoC 锁相环（PLL，SOC_PLL）。

<a id="r_ga31b39a23904212b738f598be5bc68f1e"></a>

```c
#define SIWX91X_CLK_PLL_INTF 22
```

相关声明：[SIWX91X_CLK_PLL_INTF](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga31b39a23904212b738f598be5bc68f1e)。

接口锁相环（Interface PLL，INTF_PLL）。

<a id="r_gaade542d0564ba0c8df00c09eb96b7af7"></a>

```c
#define SIWX91X_CLK_PLL_I2S 23
```

相关声明：[SIWX91X_CLK_PLL_I2S](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gaade542d0564ba0c8df00c09eb96b7af7)。

I2S 锁相环（PLL，I2S_PLL）。

<a id="define-members-1"></a>

### 超低功耗域时钟（ULP / Ultra Low Power Clocks）

<a id="r_ga13540e36cfdfa08d3366a8b950baaf9b"></a>

```c
#define SIWX91X_CLK_ULP_UART 24
```

相关声明：[SIWX91X_CLK_ULP_UART](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga13540e36cfdfa08d3366a8b950baaf9b)。

ULP UART 时钟（Clock）。

<a id="r_ga11659ca1dacf850b679bc35e7e042a71"></a>

```c
#define SIWX91X_CLK_ULP_I2C 25
```

相关声明：[SIWX91X_CLK_ULP_I2C](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga11659ca1dacf850b679bc35e7e042a71)。

ULP I2C 时钟（Clock）。

<a id="r_gaab46a3e48482a427d2444939ab0b1510"></a>

```c
#define SIWX91X_CLK_ULP_UDMA 26
```

相关声明：[SIWX91X_CLK_ULP_UDMA](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gaab46a3e48482a427d2444939ab0b1510)。

ULP UDMA 时钟（Clock）。

<a id="r_ga3ce737e8d3b039ceab2fc756a054b0a7"></a>

```c
#define SIWX91X_CLK_ULP_I2S 27
```

相关声明：[SIWX91X_CLK_ULP_I2S](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga3ce737e8d3b039ceab2fc756a054b0a7)。

ULP I2S 时钟（Clock）。

<a id="r_gace8cbc4cdf2e52d7e7795fb01bdaed46"></a>

```c
#define SIWX91X_CLK_ULP_STATIC_I2S 28
```

相关声明：[SIWX91X_CLK_ULP_STATIC_I2S](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gace8cbc4cdf2e52d7e7795fb01bdaed46)。

超低功耗（ULP）静态 I2S 外部主时钟输入（External Master-clock Input）。

<a id="r_gacfcaed1f3be6524a86451293bc1614bf"></a>

```c
#define SIWX91X_CLK_ULP_ADC 29
```

相关声明：[SIWX91X_CLK_ULP_ADC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gacfcaed1f3be6524a86451293bc1614bf)。

ULP ADC 时钟（Clock）。

<a id="r_gabea4ada219e62d94a8dad1647e3a8ca5"></a>

```c
#define SIWX91X_CLK_ULP_SSI 30
```

相关声明：[SIWX91X_CLK_ULP_SSI](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gabea4ada219e62d94a8dad1647e3a8ca5)。

ULP SSI 时钟（Clock）。

<a id="r_gaa7f3b36033754a6e755033906dafff3e"></a>

```c
#define SIWX91X_CLK_ULP_TIMER 31
```

相关声明：[SIWX91X_CLK_ULP_TIMER](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gaa7f3b36033754a6e755033906dafff3e)。

超低功耗定时器时钟（ULP Timer Clock）。

<a id="r_ga4838311ae7753d444dfc739bec992aae"></a>

```c
#define SIWX91X_CLK_ULP_GPIO 32
```

相关声明：[SIWX91X_CLK_ULP_GPIO](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga4838311ae7753d444dfc739bec992aae)。

ULP GPIO 时钟（Clock）。

<a id="r_ga1f873ad6c8b234b4f9ad0cc76eb08439"></a>

```c
#define SIWX91X_CLK_ULP_REF_AON 33
```

相关声明：[SIWX91X_CLK_ULP_REF_AON](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga1f873ad6c8b234b4f9ad0cc76eb08439)。

来自超低功耗域（ULP Domain）的常开域参考时钟（AON Reference，SLP_SENSOR）。

<a id="r_ga6198bf110638c795ea5078b657fab8c5"></a>

```c
#define SIWX91X_CLK_ULP_REF_CPU 34
```

相关声明：[SIWX91X_CLK_ULP_REF_CPU](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga6198bf110638c795ea5078b657fab8c5)。

来自超低功耗域（ULP Domain）的 CPU 参考时钟（CPU Reference，ULP_PROC）。

<a id="define-members-2"></a>

### 常开域时钟（AON / Always-On Clocks）

<a id="r_gab469502645c214bcab0a7629c072e3ed"></a>

```c
#define SIWX91X_CLK_XTAL_MHZ 35
```

相关声明：[SIWX91X_CLK_XTAL_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gab469502645c214bcab0a7629c072e3ed)。

高频晶体振荡器（High-frequency Crystal Oscillator）。

<a id="r_ga6c54a1d47730fb10d1915633a6d6e805"></a>

```c
#define SIWX91X_CLK_XTAL_KHZ 36
```

相关声明：[SIWX91X_CLK_XTAL_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga6c54a1d47730fb10d1915633a6d6e805)。

低频晶体振荡器（Low-frequency Crystal Oscillator）。

<a id="r_gaa2d8c618017ba3bbd7fbe22e57ffcc68"></a>

```c
#define SIWX91X_CLK_RC_MHZ 37
```

相关声明：[SIWX91X_CLK_RC_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gaa2d8c618017ba3bbd7fbe22e57ffcc68)。

高频 RC 振荡器（High-frequency RC Oscillator）。

<a id="r_ga0f6262d3448237d6198d25172a5444c0"></a>

```c
#define SIWX91X_CLK_RC_KHZ 38
```

相关声明：[SIWX91X_CLK_RC_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga0f6262d3448237d6198d25172a5444c0)。

低频 RC 振荡器（Low-frequency RC Oscillator）。

<a id="r_gac7ea9290ed9f4162a187d900aaec9c9d"></a>

```c
#define SIWX91X_CLK_WATCHDOG 39
```

相关声明：[SIWX91X_CLK_WATCHDOG](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gac7ea9290ed9f4162a187d900aaec9c9d)。

看门狗时钟（Watchdog Clock）。

<a id="r_ga48441517f818774b29f83c96d3997609"></a>

```c
#define SIWX91X_CLK_RTC 40
```

相关声明：[SIWX91X_CLK_RTC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga48441517f818774b29f83c96d3997609)。

RTC 时钟（Clock）。

<a id="r_gab25836573ca2aa32fdcc169a7eab567c"></a>

```c
#define SIWX91X_CLK_SYSRTC 41
```

相关声明：[SIWX91X_CLK_SYSRTC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gab25836573ca2aa32fdcc169a7eab567c)。

SYSRTC 时钟（Clock）。

<a id="r_ga228e1b2c0f4b7f3d5a024a311f7eccf2"></a>

```c
#define SIWX91X_CLK_UULP_GPIO 42
```

相关声明：[SIWX91X_CLK_UULP_GPIO](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga228e1b2c0f4b7f3d5a024a311f7eccf2)。

UULP GPIO 时钟（Clock）。

<a id="r_ga3d584b157813a867e4828d47598ad00e"></a>

```c
#define SIWX91X_CLK_REF_HP 43
```

相关声明：[SIWX91X_CLK_REF_HP](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga3d584b157813a867e4828d47598ad00e)。

高功率域参考时钟（HP Domain Reference，HP_REF）。

<a id="r_ga32d7900a5874721769eb6dcd4adef636"></a>

```c
#define SIWX91X_CLK_REF_ULP 44
```

相关声明：[SIWX91X_CLK_REF_ULP](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga32d7900a5874721769eb6dcd4adef636)。

超低功耗域参考时钟（ULP Domain Reference，ULP_REF）。

<a id="r_gaba5a4438dfedba689d67a852d5fed09e"></a>

```c
#define SIWX91X_CLK_AON_REF_HF 45
```

相关声明：[SIWX91X_CLK_AON_REF_HF](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gaba5a4438dfedba689d67a852d5fed09e)。

常开域高频参考时钟（AON High-frequency Reference，UULP_HF_REF）。

<a id="r_gae72c5285844d7d5a370d60f32a837ba0"></a>

```c
#define SIWX91X_CLK_AON_REF_LF 46
```

相关声明：[SIWX91X_CLK_AON_REF_LF](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gae72c5285844d7d5a370d60f32a837ba0)。

常开域低频参考时钟（AON Low-frequency Reference，UULP_LF_REF）。


## 13.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P791_siwx91x-clock.h_源码浏览.md)
- [SIWX91X_CLK_GATED](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gaa994575e4e81c3c7abc88f87d1ce2018)
- [SIWX91X_CLK_UART0](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gaa73343f38c9b08dc13b3a907a757abf3)
- [SIWX91X_CLK_UART1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga22c3da15ca23aa0cf14eae47ecf68e1c)
- [SIWX91X_CLK_I2C0](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gabf6e7add31fdd04634edcc9ce2e7a424)
- [SIWX91X_CLK_I2C1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gafcacbbd065793805e6b947373fa34b98)
- [SIWX91X_CLK_UDMA](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga156fadba39a730250b319d5866357d2f)
- [SIWX91X_CLK_PWM](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga3fe9ef6574ed9ced3082bc889aaf3215)
- [SIWX91X_CLK_GSPI](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gaf44b544d40037b7264cb10e4e392d0e8)
- [SIWX91X_CLK_QSPI](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga440d4643be3eee9bf8948d8edf18ad06)
- [SIWX91X_CLK_QSPI2](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga25d1b9e39822fc1f9c87e97ae2532887)
- [SIWX91X_CLK_I2S](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga686cd422cd784493a68d160e76c1cc69)
- [SIWX91X_CLK_STATIC_I2S](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga70dc54120ac5e1684de3ffc8e62c4cea)
- [SIWX91X_CLK_GPDMA](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga47c4f4859be28d1d55e9c362963c0c05)
- [SIWX91X_CLK_RNG](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gad6832ece2f138df8cba192084b8886aa)
- [SIWX91X_CLK_GPIO](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga6e24d8b833c882777c352ff653ee98a2)
- [SIWX91X_CLK_SSI](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga7d75a6726e0b708c99f6a60ea25e8f33)
- [SIWX91X_CLK_PIN_OUT](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga58be24bef62c94f02d7edbd6c927d6a8)
- [SIWX91X_CLK_ICACHE](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga9512edf3d45357b740b6a723ff60e0d9)
- [SIWX91X_CLK_CPU](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gae05159b5f02584c2ca6c84d1f714deb2)
- [SIWX91X_CLK_CPU_LP](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gad4b861be1920bb84b2557bda775dbcc9)
- [SIWX91X_CLK_HP_REF_ULP](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga598b2599c45a49bc04201f16c434a4f6)
- [SIWX91X_CLK_HP_REF_PLL](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga642d1132e759af66971509acd36b88d4)
- [SIWX91X_CLK_PLL_SOC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga763c234cb482057f8a22184bf5fd3d64)
- [SIWX91X_CLK_PLL_INTF](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga31b39a23904212b738f598be5bc68f1e)
- [SIWX91X_CLK_PLL_I2S](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gaade542d0564ba0c8df00c09eb96b7af7)
- [SIWX91X_CLK_ULP_UART](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga13540e36cfdfa08d3366a8b950baaf9b)
- [SIWX91X_CLK_ULP_I2C](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga11659ca1dacf850b679bc35e7e042a71)
- [SIWX91X_CLK_ULP_UDMA](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gaab46a3e48482a427d2444939ab0b1510)
- [SIWX91X_CLK_ULP_I2S](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga3ce737e8d3b039ceab2fc756a054b0a7)
- [SIWX91X_CLK_ULP_STATIC_I2S](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gace8cbc4cdf2e52d7e7795fb01bdaed46)
- [SIWX91X_CLK_ULP_ADC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gacfcaed1f3be6524a86451293bc1614bf)
- [SIWX91X_CLK_ULP_SSI](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gabea4ada219e62d94a8dad1647e3a8ca5)
- [SIWX91X_CLK_ULP_TIMER](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gaa7f3b36033754a6e755033906dafff3e)
- [SIWX91X_CLK_ULP_GPIO](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga4838311ae7753d444dfc739bec992aae)
- [SIWX91X_CLK_ULP_REF_AON](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga1f873ad6c8b234b4f9ad0cc76eb08439)
- [SIWX91X_CLK_ULP_REF_CPU](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga6198bf110638c795ea5078b657fab8c5)
- [SIWX91X_CLK_XTAL_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gab469502645c214bcab0a7629c072e3ed)
- [SIWX91X_CLK_XTAL_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga6c54a1d47730fb10d1915633a6d6e805)
- [SIWX91X_CLK_RC_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gaa2d8c618017ba3bbd7fbe22e57ffcc68)
- [SIWX91X_CLK_RC_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga0f6262d3448237d6198d25172a5444c0)
- [SIWX91X_CLK_WATCHDOG](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gac7ea9290ed9f4162a187d900aaec9c9d)
- [SIWX91X_CLK_RTC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga48441517f818774b29f83c96d3997609)
- [SIWX91X_CLK_SYSRTC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gab25836573ca2aa32fdcc169a7eab567c)
- [SIWX91X_CLK_UULP_GPIO](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga228e1b2c0f4b7f3d5a024a311f7eccf2)
- [SIWX91X_CLK_REF_HP](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga3d584b157813a867e4828d47598ad00e)
- [SIWX91X_CLK_REF_ULP](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#ga32d7900a5874721769eb6dcd4adef636)
- [SIWX91X_CLK_AON_REF_HF](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gaba5a4438dfedba689d67a852d5fed09e)
- [SIWX91X_CLK_AON_REF_LF](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__dt__silabs__siwx91x.html#gae72c5285844d7d5a370d60f32a837ba0)

<a id="header-details"></a>

---

[上一章](P012_zephyr__net__rtp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P014_zephyr__dt-bindings__pinctrl__syna-sr100-pinctrl.h_文件参考.md)
