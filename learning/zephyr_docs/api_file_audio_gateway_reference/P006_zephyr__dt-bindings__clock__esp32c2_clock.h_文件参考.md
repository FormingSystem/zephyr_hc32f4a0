---
id: learning.zephyr-docs.api-file-audio-gateway-reference.page-6
title: zephyr__dt-bindings__clock__esp32c2_clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/esp32c2__clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_dt-bindings\_\_clock\_\_esp32c2\_clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/esp32c2__clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.1\_宏定义（Macros）

<a id="r_a44ee3670c3168dd0ffbc79a563a7f074"></a>

```c
#define ESP32_CPU_CLK_SRC_XTAL 0U
```

相关声明：[ESP32_CPU_CLK_SRC_XTAL](#a44ee3670c3168dd0ffbc79a563a7f074)。

<a id="r_a7a723b6353a23b55ef44d720297fe26f"></a>

```c
#define ESP32_CPU_CLK_SRC_PLL 1U
```

相关声明：[ESP32_CPU_CLK_SRC_PLL](#a7a723b6353a23b55ef44d720297fe26f)。

<a id="r_a1962dad90f737a51fcc70cea1931b236"></a>

```c
#define ESP32_CLK_SRC_RC_FAST 2U
```

相关声明：[ESP32_CLK_SRC_RC_FAST](#a1962dad90f737a51fcc70cea1931b236)。

<a id="r_aa61a2254926bfec49b2eb959f307ff30"></a>

```c
#define ESP32_CLK_CPU_PLL_40M 40000000
```

相关声明：[ESP32_CLK_CPU_PLL_40M](#aa61a2254926bfec49b2eb959f307ff30)。

<a id="r_af817a387d83b343413616ee4eaa73bc4"></a>

```c
#define ESP32_CLK_CPU_PLL_60M 60000000
```

相关声明：[ESP32_CLK_CPU_PLL_60M](#af817a387d83b343413616ee4eaa73bc4)。

<a id="r_a61275f95111fb2a6bdbe446c0228f877"></a>

```c
#define ESP32_CLK_CPU_PLL_80M 80000000
```

相关声明：[ESP32_CLK_CPU_PLL_80M](#a61275f95111fb2a6bdbe446c0228f877)。

<a id="r_a31d4aba38136e01b31ff34c81b08256e"></a>

```c
#define ESP32_CLK_CPU_PLL_120M 120000000
```

相关声明：[ESP32_CLK_CPU_PLL_120M](#a31d4aba38136e01b31ff34c81b08256e)。

<a id="r_ab779f427209fda571ec4d229b8ef8bfc"></a>

```c
#define ESP32_CLK_CPU_RC_FAST_FREQ 8750000
```

相关声明：[ESP32_CLK_CPU_RC_FAST_FREQ](#ab779f427209fda571ec4d229b8ef8bfc)。

<a id="r_a06efe791ed749209eb07de5066c6eddc"></a>

```c
#define ESP32_CLK_XTAL_26M 26000000
```

相关声明：[ESP32_CLK_XTAL_26M](#a06efe791ed749209eb07de5066c6eddc)。

<a id="r_aeb5c606e77a85fa858ab7af6061c7949"></a>

```c
#define ESP32_CLK_XTAL_32M 32000000
```

相关声明：[ESP32_CLK_XTAL_32M](#aeb5c606e77a85fa858ab7af6061c7949)。

<a id="r_a6afe38f9f9c44a1bd2e5279163523a98"></a>

```c
#define ESP32_CLK_XTAL_40M 40000000
```

相关声明：[ESP32_CLK_XTAL_40M](#a6afe38f9f9c44a1bd2e5279163523a98)。

<a id="r_a725193bf445b7f8f2c1058a6735ca476"></a>

```c
#define ESP32_RTC_FAST_CLK_SRC_XTAL_D2 0
```

相关声明：[ESP32_RTC_FAST_CLK_SRC_XTAL_D2](#a725193bf445b7f8f2c1058a6735ca476)。

<a id="r_aae48d9f1288771e11c11d6177ecf3af7"></a>

```c
#define ESP32_RTC_FAST_CLK_SRC_RC_FAST 1
```

相关声明：[ESP32_RTC_FAST_CLK_SRC_RC_FAST](#aae48d9f1288771e11c11d6177ecf3af7)。

<a id="r_ad1d90df80dee3040dbe8c968cd774443"></a>

```c
#define ESP32_RTC_SLOW_CLK_SRC_RC_SLOW 0
```

相关声明：[ESP32_RTC_SLOW_CLK_SRC_RC_SLOW](#ad1d90df80dee3040dbe8c968cd774443)。

<a id="r_a0c9ed1e9c69731554227e93ddd086e9e"></a>

```c
#define ESP32_RTC_SLOW_CLK_SRC_OSC_SLOW 1
```

相关声明：[ESP32_RTC_SLOW_CLK_SRC_OSC_SLOW](#a0c9ed1e9c69731554227e93ddd086e9e)。

<a id="r_aaec50946dbdaabaf2199e795a389634e"></a>

```c
#define ESP32_RTC_SLOW_CLK_SRC_RC_FAST_D256 2
```

相关声明：[ESP32_RTC_SLOW_CLK_SRC_RC_FAST_D256](#aaec50946dbdaabaf2199e795a389634e)。

<a id="r_af5cdcfa17e680ceda2f90e375eded6e6"></a>

```c
#define ESP32_RTC_SLOW_CLK_SRC_RC_SLOW_FREQ 136000
```

相关声明：[ESP32_RTC_SLOW_CLK_SRC_RC_SLOW_FREQ](#af5cdcfa17e680ceda2f90e375eded6e6)。

<a id="r_ab3d6d4b49e506dac9b7812b9abd30a82"></a>

```c
#define ESP32_RTC_SLOW_CLK_SRC_OSC_SLOW_FREQ 32768
```

相关声明：[ESP32_RTC_SLOW_CLK_SRC_OSC_SLOW_FREQ](#ab3d6d4b49e506dac9b7812b9abd30a82)。

<a id="r_a8531ee06161cae4ea8516d00825c32c8"></a>

```c
#define ESP32_RTC_SLOW_CLK_SRC_RC_FAST_D256_FREQ 68359
```

相关声明：[ESP32_RTC_SLOW_CLK_SRC_RC_FAST_D256_FREQ](#a8531ee06161cae4ea8516d00825c32c8)。

<a id="r_a88ae2c1bafdc6e78258ada5cbb9368f9"></a>

```c
#define ESP32_TIMG0_MODULE 0
```

相关声明：[ESP32_TIMG0_MODULE](#a88ae2c1bafdc6e78258ada5cbb9368f9)。

定时器组 0（Timer Group 0）模块（Module）。

<a id="r_af5ef985d4eaf1ffe565e2662493178c6"></a>

```c
#define ESP32_UHCI0_MODULE 1
```

相关声明：[ESP32_UHCI0_MODULE](#af5ef985d4eaf1ffe565e2662493178c6)。

UHCI0模块（Module）。

<a id="r_ad5423ca02819aab6b3fe63c11b3cf998"></a>

```c
#define ESP32_RNG_MODULE 2
```

相关声明：[ESP32_RNG_MODULE](#ad5423ca02819aab6b3fe63c11b3cf998)。

RNG模块（Module）。

<a id="r_a4013c1fc7538bf46d5c1771f837a8b21"></a>

```c
#define ESP32_WIFI_MODULE 3
```

相关声明：[ESP32_WIFI_MODULE](#a4013c1fc7538bf46d5c1771f837a8b21)。

Wi-Fi模块（Module）。

<a id="r_ad180ebcea5567ce6c3145998f3761584"></a>

```c
#define ESP32_BT_MODULE 4
```

相关声明：[ESP32_BT_MODULE](#ad180ebcea5567ce6c3145998f3761584)。

蓝牙（Bluetooth）模块（Module）。

<a id="r_aba1295479849f8b4dc44245e330e3020"></a>

```c
#define ESP32_WIFI_BT_COMMON_MODULE 5
```

相关声明：[ESP32_WIFI_BT_COMMON_MODULE](#aba1295479849f8b4dc44245e330e3020)。

Wi-Fi／蓝牙共用（Wi-Fi/BT Common）模块（Module）。

<a id="r_aaf8e1de1e86906ba539863b9009ebe37"></a>

```c
#define ESP32_SYSTIMER_MODULE 6
```

相关声明：[ESP32_SYSTIMER_MODULE](#aaf8e1de1e86906ba539863b9009ebe37)。

系统定时器（System Timer）模块（Module）。

<a id="r_ade25c42235583c47d9abf29f66c00ed2"></a>

```c
#define ESP32_PHY_CALIBRATION_MODULE 7
```

相关声明：[ESP32_PHY_CALIBRATION_MODULE](#ade25c42235583c47d9abf29f66c00ed2)。

物理层校准（PHY Calibration）模块（Module）。

<a id="r_afe4f89e4a6712cc76536ea1b6a769a2d"></a>

```c
#define ESP32_COEX_MODULE 8
```

相关声明：[ESP32_COEX_MODULE](#afe4f89e4a6712cc76536ea1b6a769a2d)。

共存（Coexistence）模块（Module）。

<a id="r_ac380a7ff843ee465763a355cb01ef295"></a>

```c
#define ESP32_MODULE_MAX 9
```

相关声明：[ESP32_MODULE_MAX](#ac380a7ff843ee465763a355cb01ef295)。

模块数量（Module Count）。

<a id="r_a60f4f5ee56d788f2161b52ebbc2aa510"></a>

```c
#define ESP32_LEDC_MODULE 100
```

相关声明：[ESP32_LEDC_MODULE](#a60f4f5ee56d788f2161b52ebbc2aa510)。

LEDC模块（Module）。

<a id="r_a9708d046fbadfb7ccbc5df3e0ae57844"></a>

```c
#define ESP32_UART0_MODULE 101
```

相关声明：[ESP32_UART0_MODULE](#a9708d046fbadfb7ccbc5df3e0ae57844)。

UART0模块（Module）。

<a id="r_a480803130ef80df04527f4dd12525d48"></a>

```c
#define ESP32_UART1_MODULE 102
```

相关声明：[ESP32_UART1_MODULE](#a480803130ef80df04527f4dd12525d48)。

UART1模块（Module）。

<a id="r_a7331ffa2ec41896d05f1f86c4d30f758"></a>

```c
#define ESP32_I2C0_MODULE 103
```

相关声明：[ESP32_I2C0_MODULE](#a7331ffa2ec41896d05f1f86c4d30f758)。

I2C0模块（Module）。

<a id="r_a251462caa49fc6fe0ae1c8fe99a87caa"></a>

```c
#define ESP32_TIMG1_MODULE 104
```

相关声明：[ESP32_TIMG1_MODULE](#a251462caa49fc6fe0ae1c8fe99a87caa)。

定时器组 1（Timer Group 1）模块（Module）。

<a id="r_a5652d0e2b1fc766dde13b84294d4576b"></a>

```c
#define ESP32_SPI_MODULE 105
```

相关声明：[ESP32_SPI_MODULE](#a5652d0e2b1fc766dde13b84294d4576b)。

SPI1模块（Module）。

<a id="r_a5e5283c23811e9c4f30980f1d865773b"></a>

```c
#define ESP32_SPI2_MODULE 106
```

相关声明：[ESP32_SPI2_MODULE](#a5e5283c23811e9c4f30980f1d865773b)。

SPI2模块（Module）。

<a id="r_a653e6d1f91c532b3ba313be27a97c2af"></a>

```c
#define ESP32_BT_BASEBAND_MODULE 107
```

相关声明：[ESP32_BT_BASEBAND_MODULE](#a653e6d1f91c532b3ba313be27a97c2af)。

蓝牙基带（BT Baseband）模块（Module）。

<a id="r_a8e27f45346390d8909f9424f13280b76"></a>

```c
#define ESP32_BT_LC_MODULE 108
```

相关声明：[ESP32_BT_LC_MODULE](#a8e27f45346390d8909f9424f13280b76)。

蓝牙链路控制器（BT Link Controller）模块（Module）。

<a id="r_a290ac6ab6c5de2e8d84a911e389e1cfc"></a>

```c
#define ESP32_AES_MODULE 109
```

相关声明：[ESP32_AES_MODULE](#a290ac6ab6c5de2e8d84a911e389e1cfc)。

AES模块（Module）。

<a id="r_a683dd8814bf170018b63b57268c0fde9"></a>

```c
#define ESP32_SHA_MODULE 110
```

相关声明：[ESP32_SHA_MODULE](#a683dd8814bf170018b63b57268c0fde9)。

SHA模块（Module）。

<a id="r_a27bd450bf21c8b7502d1f32d9536129f"></a>

```c
#define ESP32_ECC_MODULE 111
```

相关声明：[ESP32_ECC_MODULE](#a27bd450bf21c8b7502d1f32d9536129f)。

ECC模块（Module）。

<a id="r_a701fec66fac239e66a19389ea153ff75"></a>

```c
#define ESP32_GDMA_MODULE 112
```

相关声明：[ESP32_GDMA_MODULE](#a701fec66fac239e66a19389ea153ff75)。

GDMA模块（Module）。

<a id="r_abe244da38fbe794e93094feef9b188fe"></a>

```c
#define ESP32_SARADC_MODULE 113
```

相关声明：[ESP32_SARADC_MODULE](#abe244da38fbe794e93094feef9b188fe)。

SAR ADC模块（Module）。

<a id="r_a488d6d32cf66e81a27f0999f837fe39a"></a>

```c
#define ESP32_TEMPSENSOR_MODULE 114
```

相关声明：[ESP32_TEMPSENSOR_MODULE](#a488d6d32cf66e81a27f0999f837fe39a)。

温度传感器（Temperature Sensor）模块（Module）。

<a id="r_a65f83f03cf7bdda167c25d3bb283f99b"></a>

```c
#define ESP32_MODEM_RPA_MODULE 115
```

相关声明：[ESP32_MODEM_RPA_MODULE](#a65f83f03cf7bdda167c25d3bb283f99b)。

调制解调器 RPA（Modem RPA）模块（Module）。

## 6.2\_详细说明（Detailed Documentation）

<a id="a290ac6ab6c5de2e8d84a911e389e1cfc"></a>

### `ESP32_AES_MODULE`

```c
#define ESP32_AES_MODULE 109
```

AES模块（Module）。

<a id="a653e6d1f91c532b3ba313be27a97c2af"></a>

### `ESP32_BT_BASEBAND_MODULE`

```c
#define ESP32_BT_BASEBAND_MODULE 107
```

蓝牙基带（BT Baseband）模块（Module）。

<a id="a8e27f45346390d8909f9424f13280b76"></a>

### `ESP32_BT_LC_MODULE`

```c
#define ESP32_BT_LC_MODULE 108
```

蓝牙链路控制器（BT Link Controller）模块（Module）。

<a id="ad180ebcea5567ce6c3145998f3761584"></a>

### `ESP32_BT_MODULE`

```c
#define ESP32_BT_MODULE 4
```

蓝牙（Bluetooth）模块（Module）。

<a id="a31d4aba38136e01b31ff34c81b08256e"></a>

### `ESP32_CLK_CPU_PLL_120M`

```c
#define ESP32_CLK_CPU_PLL_120M 120000000
```

<a id="aa61a2254926bfec49b2eb959f307ff30"></a>

### `ESP32_CLK_CPU_PLL_40M`

```c
#define ESP32_CLK_CPU_PLL_40M 40000000
```

<a id="af817a387d83b343413616ee4eaa73bc4"></a>

### `ESP32_CLK_CPU_PLL_60M`

```c
#define ESP32_CLK_CPU_PLL_60M 60000000
```

<a id="a61275f95111fb2a6bdbe446c0228f877"></a>

### `ESP32_CLK_CPU_PLL_80M`

```c
#define ESP32_CLK_CPU_PLL_80M 80000000
```

<a id="ab779f427209fda571ec4d229b8ef8bfc"></a>

### `ESP32_CLK_CPU_RC_FAST_FREQ`

```c
#define ESP32_CLK_CPU_RC_FAST_FREQ 8750000
```

<a id="a1962dad90f737a51fcc70cea1931b236"></a>

### `ESP32_CLK_SRC_RC_FAST`

```c
#define ESP32_CLK_SRC_RC_FAST 2U
```

<a id="a06efe791ed749209eb07de5066c6eddc"></a>

### `ESP32_CLK_XTAL_26M`

```c
#define ESP32_CLK_XTAL_26M 26000000
```

<a id="aeb5c606e77a85fa858ab7af6061c7949"></a>

### `ESP32_CLK_XTAL_32M`

```c
#define ESP32_CLK_XTAL_32M 32000000
```

<a id="a6afe38f9f9c44a1bd2e5279163523a98"></a>

### `ESP32_CLK_XTAL_40M`

```c
#define ESP32_CLK_XTAL_40M 40000000
```

<a id="afe4f89e4a6712cc76536ea1b6a769a2d"></a>

### `ESP32_COEX_MODULE`

```c
#define ESP32_COEX_MODULE 8
```

共存（Coexistence）模块（Module）。

<a id="a7a723b6353a23b55ef44d720297fe26f"></a>

### `ESP32_CPU_CLK_SRC_PLL`

```c
#define ESP32_CPU_CLK_SRC_PLL 1U
```

<a id="a44ee3670c3168dd0ffbc79a563a7f074"></a>

### `ESP32_CPU_CLK_SRC_XTAL`

```c
#define ESP32_CPU_CLK_SRC_XTAL 0U
```

<a id="a27bd450bf21c8b7502d1f32d9536129f"></a>

### `ESP32_ECC_MODULE`

```c
#define ESP32_ECC_MODULE 111
```

ECC模块（Module）。

<a id="a701fec66fac239e66a19389ea153ff75"></a>

### `ESP32_GDMA_MODULE`

```c
#define ESP32_GDMA_MODULE 112
```

GDMA模块（Module）。

<a id="a7331ffa2ec41896d05f1f86c4d30f758"></a>

### `ESP32_I2C0_MODULE`

```c
#define ESP32_I2C0_MODULE 103
```

I2C0模块（Module）。

<a id="a60f4f5ee56d788f2161b52ebbc2aa510"></a>

### `ESP32_LEDC_MODULE`

```c
#define ESP32_LEDC_MODULE 100
```

LEDC模块（Module）。

<a id="a65f83f03cf7bdda167c25d3bb283f99b"></a>

### `ESP32_MODEM_RPA_MODULE`

```c
#define ESP32_MODEM_RPA_MODULE 115
```

调制解调器 RPA（Modem RPA）模块（Module）。

<a id="ac380a7ff843ee465763a355cb01ef295"></a>

### `ESP32_MODULE_MAX`

```c
#define ESP32_MODULE_MAX 9
```

模块数量（Module Count）。

<a id="ade25c42235583c47d9abf29f66c00ed2"></a>

### `ESP32_PHY_CALIBRATION_MODULE`

```c
#define ESP32_PHY_CALIBRATION_MODULE 7
```

物理层校准（PHY Calibration）模块（Module）。

<a id="ad5423ca02819aab6b3fe63c11b3cf998"></a>

### `ESP32_RNG_MODULE`

```c
#define ESP32_RNG_MODULE 2
```

RNG模块（Module）。

<a id="aae48d9f1288771e11c11d6177ecf3af7"></a>

### `ESP32_RTC_FAST_CLK_SRC_RC_FAST`

```c
#define ESP32_RTC_FAST_CLK_SRC_RC_FAST 1
```

<a id="a725193bf445b7f8f2c1058a6735ca476"></a>

### `ESP32_RTC_FAST_CLK_SRC_XTAL_D2`

```c
#define ESP32_RTC_FAST_CLK_SRC_XTAL_D2 0
```

<a id="a0c9ed1e9c69731554227e93ddd086e9e"></a>

### `ESP32_RTC_SLOW_CLK_SRC_OSC_SLOW`

```c
#define ESP32_RTC_SLOW_CLK_SRC_OSC_SLOW 1
```

<a id="ab3d6d4b49e506dac9b7812b9abd30a82"></a>

### `ESP32_RTC_SLOW_CLK_SRC_OSC_SLOW_FREQ`

```c
#define ESP32_RTC_SLOW_CLK_SRC_OSC_SLOW_FREQ 32768
```

<a id="aaec50946dbdaabaf2199e795a389634e"></a>

### `ESP32_RTC_SLOW_CLK_SRC_RC_FAST_D256`

```c
#define ESP32_RTC_SLOW_CLK_SRC_RC_FAST_D256 2
```

<a id="a8531ee06161cae4ea8516d00825c32c8"></a>

### `ESP32_RTC_SLOW_CLK_SRC_RC_FAST_D256_FREQ`

```c
#define ESP32_RTC_SLOW_CLK_SRC_RC_FAST_D256_FREQ 68359
```

<a id="ad1d90df80dee3040dbe8c968cd774443"></a>

### `ESP32_RTC_SLOW_CLK_SRC_RC_SLOW`

```c
#define ESP32_RTC_SLOW_CLK_SRC_RC_SLOW 0
```

<a id="af5cdcfa17e680ceda2f90e375eded6e6"></a>

### `ESP32_RTC_SLOW_CLK_SRC_RC_SLOW_FREQ`

```c
#define ESP32_RTC_SLOW_CLK_SRC_RC_SLOW_FREQ 136000
```

<a id="abe244da38fbe794e93094feef9b188fe"></a>

### `ESP32_SARADC_MODULE`

```c
#define ESP32_SARADC_MODULE 113
```

SAR ADC模块（Module）。

<a id="a683dd8814bf170018b63b57268c0fde9"></a>

### `ESP32_SHA_MODULE`

```c
#define ESP32_SHA_MODULE 110
```

SHA模块（Module）。

<a id="a5e5283c23811e9c4f30980f1d865773b"></a>

### `ESP32_SPI2_MODULE`

```c
#define ESP32_SPI2_MODULE 106
```

SPI2模块（Module）。

<a id="a5652d0e2b1fc766dde13b84294d4576b"></a>

### `ESP32_SPI_MODULE`

```c
#define ESP32_SPI_MODULE 105
```

SPI1模块（Module）。

<a id="aaf8e1de1e86906ba539863b9009ebe37"></a>

### `ESP32_SYSTIMER_MODULE`

```c
#define ESP32_SYSTIMER_MODULE 6
```

系统定时器（System Timer）模块（Module）。

<a id="a488d6d32cf66e81a27f0999f837fe39a"></a>

### `ESP32_TEMPSENSOR_MODULE`

```c
#define ESP32_TEMPSENSOR_MODULE 114
```

温度传感器（Temperature Sensor）模块（Module）。

<a id="a88ae2c1bafdc6e78258ada5cbb9368f9"></a>

### `ESP32_TIMG0_MODULE`

```c
#define ESP32_TIMG0_MODULE 0
```

定时器组 0（Timer Group 0）模块（Module）。

<a id="a251462caa49fc6fe0ae1c8fe99a87caa"></a>

### `ESP32_TIMG1_MODULE`

```c
#define ESP32_TIMG1_MODULE 104
```

定时器组 1（Timer Group 1）模块（Module）。

<a id="a9708d046fbadfb7ccbc5df3e0ae57844"></a>

### `ESP32_UART0_MODULE`

```c
#define ESP32_UART0_MODULE 101
```

UART0模块（Module）。

<a id="a480803130ef80df04527f4dd12525d48"></a>

### `ESP32_UART1_MODULE`

```c
#define ESP32_UART1_MODULE 102
```

UART1模块（Module）。

<a id="af5ef985d4eaf1ffe565e2662493178c6"></a>

### `ESP32_UHCI0_MODULE`

```c
#define ESP32_UHCI0_MODULE 1
```

UHCI0模块（Module）。

<a id="aba1295479849f8b4dc44245e330e3020"></a>

### `ESP32_WIFI_BT_COMMON_MODULE`

```c
#define ESP32_WIFI_BT_COMMON_MODULE 5
```

Wi-Fi／蓝牙共用（Wi-Fi/BT Common）模块（Module）。

<a id="a4013c1fc7538bf46d5c1771f837a8b21"></a>

### `ESP32_WIFI_MODULE`

```c
#define ESP32_WIFI_MODULE 3
```

Wi-Fi模块（Module）。


## 6.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_compiler_device_reference/P007_esp32c2_clock.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P005_zephyr__dt-bindings__clock__esp32_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__dt-bindings__clock__esp32c3_clock.h_文件参考.md)
