---
id: learning.zephyr-docs.api-file-audio-gateway-reference.page-5
title: zephyr__dt-bindings__clock__esp32_clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/esp32__clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_dt-bindings\_\_clock\_\_esp32\_clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/esp32__clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.1\_宏定义（Macros）

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

<a id="r_ab5e4881ee7bff8e6fa001714f95a806d"></a>

```c
#define ESP32_CLK_SRC_APLL_CLK 3U
```

相关声明：[ESP32_CLK_SRC_APLL_CLK](#ab5e4881ee7bff8e6fa001714f95a806d)。

<a id="r_a61275f95111fb2a6bdbe446c0228f877"></a>

```c
#define ESP32_CLK_CPU_PLL_80M 80000000
```

相关声明：[ESP32_CLK_CPU_PLL_80M](#a61275f95111fb2a6bdbe446c0228f877)。

<a id="r_ad80a59287e6a2f3771fd448982be9555"></a>

```c
#define ESP32_CLK_CPU_PLL_160M 160000000
```

相关声明：[ESP32_CLK_CPU_PLL_160M](#ad80a59287e6a2f3771fd448982be9555)。

<a id="r_ae0cca31853cf16bf9fa85508bbf9347f"></a>

```c
#define ESP32_CLK_CPU_PLL_240M 240000000
```

相关声明：[ESP32_CLK_CPU_PLL_240M](#ae0cca31853cf16bf9fa85508bbf9347f)。

<a id="r_ab779f427209fda571ec4d229b8ef8bfc"></a>

```c
#define ESP32_CLK_CPU_RC_FAST_FREQ 1062500
```

相关声明：[ESP32_CLK_CPU_RC_FAST_FREQ](#ab779f427209fda571ec4d229b8ef8bfc)。

<a id="r_a85c15a3031e661eb41db77782e231316"></a>

```c
#define ESP32_CLK_XTAL_24M 24000000
```

相关声明：[ESP32_CLK_XTAL_24M](#a85c15a3031e661eb41db77782e231316)。

<a id="r_a06efe791ed749209eb07de5066c6eddc"></a>

```c
#define ESP32_CLK_XTAL_26M 26000000
```

相关声明：[ESP32_CLK_XTAL_26M](#a06efe791ed749209eb07de5066c6eddc)。

<a id="r_a6afe38f9f9c44a1bd2e5279163523a98"></a>

```c
#define ESP32_CLK_XTAL_40M 40000000
```

相关声明：[ESP32_CLK_XTAL_40M](#a6afe38f9f9c44a1bd2e5279163523a98)。

<a id="r_a5348c66760f7e577484c46d05d549193"></a>

```c
#define ESP32_RTC_FAST_CLK_SRC_XTAL_D4 0
```

相关声明：[ESP32_RTC_FAST_CLK_SRC_XTAL_D4](#a5348c66760f7e577484c46d05d549193)。

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

<a id="r_aeaccf7695cab85cd7523c6ebc21704c4"></a>

```c
#define ESP32_RTC_SLOW_CLK_SRC_XTAL32K 1
```

相关声明：[ESP32_RTC_SLOW_CLK_SRC_XTAL32K](#aeaccf7695cab85cd7523c6ebc21704c4)。

<a id="r_aaec50946dbdaabaf2199e795a389634e"></a>

```c
#define ESP32_RTC_SLOW_CLK_SRC_RC_FAST_D256 2
```

相关声明：[ESP32_RTC_SLOW_CLK_SRC_RC_FAST_D256](#aaec50946dbdaabaf2199e795a389634e)。

<a id="r_aa5d6a46de7da027832aa02489c062069"></a>

```c
#define ESP32_RTC_SLOW_CLK_32K_EXT_OSC 9
```

相关声明：[ESP32_RTC_SLOW_CLK_32K_EXT_OSC](#aa5d6a46de7da027832aa02489c062069)。

<a id="r_af5cdcfa17e680ceda2f90e375eded6e6"></a>

```c
#define ESP32_RTC_SLOW_CLK_SRC_RC_SLOW_FREQ 150000
```

相关声明：[ESP32_RTC_SLOW_CLK_SRC_RC_SLOW_FREQ](#af5cdcfa17e680ceda2f90e375eded6e6)。

<a id="r_ab63ec0973bfb87f7f09c5614ab66deb8"></a>

```c
#define ESP32_RTC_SLOW_CLK_SRC_XTAL32K_FREQ 32768
```

相关声明：[ESP32_RTC_SLOW_CLK_SRC_XTAL32K_FREQ](#ab63ec0973bfb87f7f09c5614ab66deb8)。

<a id="r_a8531ee06161cae4ea8516d00825c32c8"></a>

```c
#define ESP32_RTC_SLOW_CLK_SRC_RC_FAST_D256_FREQ 33203
```

相关声明：[ESP32_RTC_SLOW_CLK_SRC_RC_FAST_D256_FREQ](#a8531ee06161cae4ea8516d00825c32c8)。

<a id="r_a480803130ef80df04527f4dd12525d48"></a>

```c
#define ESP32_UART1_MODULE 0
```

相关声明：[ESP32_UART1_MODULE](#a480803130ef80df04527f4dd12525d48)。

UART1模块（Module）。

<a id="r_a975be76987c86a84903dcc626bdc1478"></a>

```c
#define ESP32_UART2_MODULE 1
```

相关声明：[ESP32_UART2_MODULE](#a975be76987c86a84903dcc626bdc1478)。

UART2模块（Module）。

<a id="r_a21c262b775f6d533621d4ba8e8d6c9aa"></a>

```c
#define ESP32_I2S0_MODULE 2
```

相关声明：[ESP32_I2S0_MODULE](#a21c262b775f6d533621d4ba8e8d6c9aa)。

I2S0模块（Module）。

<a id="r_a88ae2c1bafdc6e78258ada5cbb9368f9"></a>

```c
#define ESP32_TIMG0_MODULE 3
```

相关声明：[ESP32_TIMG0_MODULE](#a88ae2c1bafdc6e78258ada5cbb9368f9)。

定时器组 0（Timer Group 0）模块（Module）。

<a id="r_a251462caa49fc6fe0ae1c8fe99a87caa"></a>

```c
#define ESP32_TIMG1_MODULE 4
```

相关声明：[ESP32_TIMG1_MODULE](#a251462caa49fc6fe0ae1c8fe99a87caa)。

定时器组 1（Timer Group 1）模块（Module）。

<a id="r_af5ef985d4eaf1ffe565e2662493178c6"></a>

```c
#define ESP32_UHCI0_MODULE 5
```

相关声明：[ESP32_UHCI0_MODULE](#af5ef985d4eaf1ffe565e2662493178c6)。

UHCI0模块（Module）。

<a id="r_a5652d0e2b1fc766dde13b84294d4576b"></a>

```c
#define ESP32_SPI_MODULE 6
```

相关声明：[ESP32_SPI_MODULE](#a5652d0e2b1fc766dde13b84294d4576b)。

SPI1模块（Module）。

<a id="r_af9492b3e7cf5282eff0a4ee342eac278"></a>

```c
#define ESP32_HSPI_MODULE 7
```

相关声明：[ESP32_HSPI_MODULE](#af9492b3e7cf5282eff0a4ee342eac278)。

HSPI模块（Module）。

<a id="r_a982e8ce4deccacd4d020cdfed8771cac"></a>

```c
#define ESP32_VSPI_MODULE 8
```

相关声明：[ESP32_VSPI_MODULE](#a982e8ce4deccacd4d020cdfed8771cac)。

VSPI模块（Module）。

<a id="r_ad5423ca02819aab6b3fe63c11b3cf998"></a>

```c
#define ESP32_RNG_MODULE 9
```

相关声明：[ESP32_RNG_MODULE](#ad5423ca02819aab6b3fe63c11b3cf998)。

RNG模块（Module）。

<a id="r_a4013c1fc7538bf46d5c1771f837a8b21"></a>

```c
#define ESP32_WIFI_MODULE 10
```

相关声明：[ESP32_WIFI_MODULE](#a4013c1fc7538bf46d5c1771f837a8b21)。

Wi-Fi模块（Module）。

<a id="r_ad180ebcea5567ce6c3145998f3761584"></a>

```c
#define ESP32_BT_MODULE 11
```

相关声明：[ESP32_BT_MODULE](#ad180ebcea5567ce6c3145998f3761584)。

蓝牙（Bluetooth）模块（Module）。

<a id="r_aba1295479849f8b4dc44245e330e3020"></a>

```c
#define ESP32_WIFI_BT_COMMON_MODULE 12
```

相关声明：[ESP32_WIFI_BT_COMMON_MODULE](#aba1295479849f8b4dc44245e330e3020)。

Wi-Fi／蓝牙共用（Wi-Fi/BT Common）模块（Module）。

<a id="r_a653e6d1f91c532b3ba313be27a97c2af"></a>

```c
#define ESP32_BT_BASEBAND_MODULE 13
```

相关声明：[ESP32_BT_BASEBAND_MODULE](#a653e6d1f91c532b3ba313be27a97c2af)。

蓝牙基带（BT Baseband）模块（Module）。

<a id="r_ade25c42235583c47d9abf29f66c00ed2"></a>

```c
#define ESP32_PHY_CALIBRATION_MODULE 14
```

相关声明：[ESP32_PHY_CALIBRATION_MODULE](#ade25c42235583c47d9abf29f66c00ed2)。

物理层校准（PHY Calibration）模块（Module）。

<a id="r_ac380a7ff843ee465763a355cb01ef295"></a>

```c
#define ESP32_MODULE_MAX 15
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

<a id="r_a7331ffa2ec41896d05f1f86c4d30f758"></a>

```c
#define ESP32_I2C0_MODULE 102
```

相关声明：[ESP32_I2C0_MODULE](#a7331ffa2ec41896d05f1f86c4d30f758)。

I2C0模块（Module）。

<a id="r_a5068c510487e0ce3002e4bf7082601cd"></a>

```c
#define ESP32_I2C1_MODULE 103
```

相关声明：[ESP32_I2C1_MODULE](#a5068c510487e0ce3002e4bf7082601cd)。

I2C1模块（Module）。

<a id="r_a1cc05bfada949af9e9265abaadb1b6bc"></a>

```c
#define ESP32_I2S1_MODULE 104
```

相关声明：[ESP32_I2S1_MODULE](#a1cc05bfada949af9e9265abaadb1b6bc)。

I2S1模块（Module）。

<a id="r_a8f939663db0f14133c2beb6dfc7dc3b7"></a>

```c
#define ESP32_PWM0_MODULE 105
```

相关声明：[ESP32_PWM0_MODULE](#a8f939663db0f14133c2beb6dfc7dc3b7)。

PWM0模块（Module）。

<a id="r_aa5690cffa8770c3e2d0457557e52f300"></a>

```c
#define ESP32_PWM1_MODULE 106
```

相关声明：[ESP32_PWM1_MODULE](#aa5690cffa8770c3e2d0457557e52f300)。

PWM1模块（Module）。

<a id="r_aa2c199cff85bcf8e5a306a056e71f1f5"></a>

```c
#define ESP32_UHCI1_MODULE 107
```

相关声明：[ESP32_UHCI1_MODULE](#aa2c199cff85bcf8e5a306a056e71f1f5)。

UHCI1模块（Module）。

<a id="r_a4a2d8ca15cd619022c02f97842d54159"></a>

```c
#define ESP32_RMT_MODULE 108
```

相关声明：[ESP32_RMT_MODULE](#a4a2d8ca15cd619022c02f97842d54159)。

RMT模块（Module）。

<a id="r_ac0d8fb4397baaac7ff45dee8f4e1cb7c"></a>

```c
#define ESP32_PCNT_MODULE 109
```

相关声明：[ESP32_PCNT_MODULE](#ac0d8fb4397baaac7ff45dee8f4e1cb7c)。

PCNT模块（Module）。

<a id="r_ac44ad6537fde43047aa04ba8ee35586e"></a>

```c
#define ESP32_SPI_DMA_MODULE 110
```

相关声明：[ESP32_SPI_DMA_MODULE](#ac44ad6537fde43047aa04ba8ee35586e)。

SPI DMA模块（Module）。

<a id="r_a72052a75b3541623f59063260c4dbc32"></a>

```c
#define ESP32_SDMMC_MODULE 111
```

相关声明：[ESP32_SDMMC_MODULE](#a72052a75b3541623f59063260c4dbc32)。

SDMMC模块（Module）。

<a id="r_a83b43d5f4d6373a5bb437de5ee5c091f"></a>

```c
#define ESP32_SDIO_SLAVE_MODULE 112
```

相关声明：[ESP32_SDIO_SLAVE_MODULE](#a83b43d5f4d6373a5bb437de5ee5c091f)。

SDIO 从设备（Slave）模块（Module）。

<a id="r_aba65cf1082c8422cc1e91c710bb702cc"></a>

```c
#define ESP32_TWAI_MODULE 113
```

相关声明：[ESP32_TWAI_MODULE](#aba65cf1082c8422cc1e91c710bb702cc)。

TWAI模块（Module）。

<a id="r_a411f896c814f629db94562be1c55e108"></a>

```c
#define ESP32_CAN_MODULE ESP32_TWAI_MODULE
```

相关声明：[ESP32_CAN_MODULE](#a411f896c814f629db94562be1c55e108)、[ESP32_TWAI_MODULE](#aba65cf1082c8422cc1e91c710bb702cc)。

CAN 模块（Module，别名）。

<a id="r_a1360ddff70c3a29ce4a0b93199e4292e"></a>

```c
#define ESP32_EMAC_MODULE 114
```

相关声明：[ESP32_EMAC_MODULE](#a1360ddff70c3a29ce4a0b93199e4292e)。

EMAC模块（Module）。

<a id="r_a290ac6ab6c5de2e8d84a911e389e1cfc"></a>

```c
#define ESP32_AES_MODULE 115
```

相关声明：[ESP32_AES_MODULE](#a290ac6ab6c5de2e8d84a911e389e1cfc)。

AES模块（Module）。

<a id="r_a683dd8814bf170018b63b57268c0fde9"></a>

```c
#define ESP32_SHA_MODULE 116
```

相关声明：[ESP32_SHA_MODULE](#a683dd8814bf170018b63b57268c0fde9)。

SHA模块（Module）。

<a id="r_a5261565b59c0a5b75794014b80692b33"></a>

```c
#define ESP32_RSA_MODULE 117
```

相关声明：[ESP32_RSA_MODULE](#a5261565b59c0a5b75794014b80692b33)。

RSA模块（Module）。

<a id="r_abe244da38fbe794e93094feef9b188fe"></a>

```c
#define ESP32_SARADC_MODULE 118
```

相关声明：[ESP32_SARADC_MODULE](#abe244da38fbe794e93094feef9b188fe)。

SAR ADC模块（Module）。

<a id="r_a8e27f45346390d8909f9424f13280b76"></a>

```c
#define ESP32_BT_LC_MODULE 119
```

相关声明：[ESP32_BT_LC_MODULE](#a8e27f45346390d8909f9424f13280b76)。

蓝牙链路控制器（BT Link Controller）模块（Module）。

## 5.2\_详细说明（Detailed Documentation）

<a id="a290ac6ab6c5de2e8d84a911e389e1cfc"></a>

### `ESP32_AES_MODULE`

```c
#define ESP32_AES_MODULE 115
```

AES模块（Module）。

<a id="a653e6d1f91c532b3ba313be27a97c2af"></a>

### `ESP32_BT_BASEBAND_MODULE`

```c
#define ESP32_BT_BASEBAND_MODULE 13
```

蓝牙基带（BT Baseband）模块（Module）。

<a id="a8e27f45346390d8909f9424f13280b76"></a>

### `ESP32_BT_LC_MODULE`

```c
#define ESP32_BT_LC_MODULE 119
```

蓝牙链路控制器（BT Link Controller）模块（Module）。

<a id="ad180ebcea5567ce6c3145998f3761584"></a>

### `ESP32_BT_MODULE`

```c
#define ESP32_BT_MODULE 11
```

蓝牙（Bluetooth）模块（Module）。

<a id="a411f896c814f629db94562be1c55e108"></a>

### `ESP32_CAN_MODULE`

```c
#define ESP32_CAN_MODULE ESP32_TWAI_MODULE
```

CAN 模块（Module，别名）。

<a id="ad80a59287e6a2f3771fd448982be9555"></a>

### `ESP32_CLK_CPU_PLL_160M`

```c
#define ESP32_CLK_CPU_PLL_160M 160000000
```

<a id="ae0cca31853cf16bf9fa85508bbf9347f"></a>

### `ESP32_CLK_CPU_PLL_240M`

```c
#define ESP32_CLK_CPU_PLL_240M 240000000
```

<a id="a61275f95111fb2a6bdbe446c0228f877"></a>

### `ESP32_CLK_CPU_PLL_80M`

```c
#define ESP32_CLK_CPU_PLL_80M 80000000
```

<a id="ab779f427209fda571ec4d229b8ef8bfc"></a>

### `ESP32_CLK_CPU_RC_FAST_FREQ`

```c
#define ESP32_CLK_CPU_RC_FAST_FREQ 1062500
```

<a id="ab5e4881ee7bff8e6fa001714f95a806d"></a>

### `ESP32_CLK_SRC_APLL_CLK`

```c
#define ESP32_CLK_SRC_APLL_CLK 3U
```

<a id="a1962dad90f737a51fcc70cea1931b236"></a>

### `ESP32_CLK_SRC_RC_FAST`

```c
#define ESP32_CLK_SRC_RC_FAST 2U
```

<a id="a85c15a3031e661eb41db77782e231316"></a>

### `ESP32_CLK_XTAL_24M`

```c
#define ESP32_CLK_XTAL_24M 24000000
```

<a id="a06efe791ed749209eb07de5066c6eddc"></a>

### `ESP32_CLK_XTAL_26M`

```c
#define ESP32_CLK_XTAL_26M 26000000
```

<a id="a6afe38f9f9c44a1bd2e5279163523a98"></a>

### `ESP32_CLK_XTAL_40M`

```c
#define ESP32_CLK_XTAL_40M 40000000
```

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

<a id="a1360ddff70c3a29ce4a0b93199e4292e"></a>

### `ESP32_EMAC_MODULE`

```c
#define ESP32_EMAC_MODULE 114
```

EMAC模块（Module）。

<a id="af9492b3e7cf5282eff0a4ee342eac278"></a>

### `ESP32_HSPI_MODULE`

```c
#define ESP32_HSPI_MODULE 7
```

HSPI模块（Module）。

<a id="a7331ffa2ec41896d05f1f86c4d30f758"></a>

### `ESP32_I2C0_MODULE`

```c
#define ESP32_I2C0_MODULE 102
```

I2C0模块（Module）。

<a id="a5068c510487e0ce3002e4bf7082601cd"></a>

### `ESP32_I2C1_MODULE`

```c
#define ESP32_I2C1_MODULE 103
```

I2C1模块（Module）。

<a id="a21c262b775f6d533621d4ba8e8d6c9aa"></a>

### `ESP32_I2S0_MODULE`

```c
#define ESP32_I2S0_MODULE 2
```

I2S0模块（Module）。

<a id="a1cc05bfada949af9e9265abaadb1b6bc"></a>

### `ESP32_I2S1_MODULE`

```c
#define ESP32_I2S1_MODULE 104
```

I2S1模块（Module）。

<a id="a60f4f5ee56d788f2161b52ebbc2aa510"></a>

### `ESP32_LEDC_MODULE`

```c
#define ESP32_LEDC_MODULE 100
```

LEDC模块（Module）。

<a id="ac380a7ff843ee465763a355cb01ef295"></a>

### `ESP32_MODULE_MAX`

```c
#define ESP32_MODULE_MAX 15
```

模块数量（Module Count）。

<a id="ac0d8fb4397baaac7ff45dee8f4e1cb7c"></a>

### `ESP32_PCNT_MODULE`

```c
#define ESP32_PCNT_MODULE 109
```

PCNT模块（Module）。

<a id="ade25c42235583c47d9abf29f66c00ed2"></a>

### `ESP32_PHY_CALIBRATION_MODULE`

```c
#define ESP32_PHY_CALIBRATION_MODULE 14
```

物理层校准（PHY Calibration）模块（Module）。

<a id="a8f939663db0f14133c2beb6dfc7dc3b7"></a>

### `ESP32_PWM0_MODULE`

```c
#define ESP32_PWM0_MODULE 105
```

PWM0模块（Module）。

<a id="aa5690cffa8770c3e2d0457557e52f300"></a>

### `ESP32_PWM1_MODULE`

```c
#define ESP32_PWM1_MODULE 106
```

PWM1模块（Module）。

<a id="a4a2d8ca15cd619022c02f97842d54159"></a>

### `ESP32_RMT_MODULE`

```c
#define ESP32_RMT_MODULE 108
```

RMT模块（Module）。

<a id="ad5423ca02819aab6b3fe63c11b3cf998"></a>

### `ESP32_RNG_MODULE`

```c
#define ESP32_RNG_MODULE 9
```

RNG模块（Module）。

<a id="a5261565b59c0a5b75794014b80692b33"></a>

### `ESP32_RSA_MODULE`

```c
#define ESP32_RSA_MODULE 117
```

RSA模块（Module）。

<a id="aae48d9f1288771e11c11d6177ecf3af7"></a>

### `ESP32_RTC_FAST_CLK_SRC_RC_FAST`

```c
#define ESP32_RTC_FAST_CLK_SRC_RC_FAST 1
```

<a id="a5348c66760f7e577484c46d05d549193"></a>

### `ESP32_RTC_FAST_CLK_SRC_XTAL_D4`

```c
#define ESP32_RTC_FAST_CLK_SRC_XTAL_D4 0
```

<a id="aa5d6a46de7da027832aa02489c062069"></a>

### `ESP32_RTC_SLOW_CLK_32K_EXT_OSC`

```c
#define ESP32_RTC_SLOW_CLK_32K_EXT_OSC 9
```

<a id="aaec50946dbdaabaf2199e795a389634e"></a>

### `ESP32_RTC_SLOW_CLK_SRC_RC_FAST_D256`

```c
#define ESP32_RTC_SLOW_CLK_SRC_RC_FAST_D256 2
```

<a id="a8531ee06161cae4ea8516d00825c32c8"></a>

### `ESP32_RTC_SLOW_CLK_SRC_RC_FAST_D256_FREQ`

```c
#define ESP32_RTC_SLOW_CLK_SRC_RC_FAST_D256_FREQ 33203
```

<a id="ad1d90df80dee3040dbe8c968cd774443"></a>

### `ESP32_RTC_SLOW_CLK_SRC_RC_SLOW`

```c
#define ESP32_RTC_SLOW_CLK_SRC_RC_SLOW 0
```

<a id="af5cdcfa17e680ceda2f90e375eded6e6"></a>

### `ESP32_RTC_SLOW_CLK_SRC_RC_SLOW_FREQ`

```c
#define ESP32_RTC_SLOW_CLK_SRC_RC_SLOW_FREQ 150000
```

<a id="aeaccf7695cab85cd7523c6ebc21704c4"></a>

### `ESP32_RTC_SLOW_CLK_SRC_XTAL32K`

```c
#define ESP32_RTC_SLOW_CLK_SRC_XTAL32K 1
```

<a id="ab63ec0973bfb87f7f09c5614ab66deb8"></a>

### `ESP32_RTC_SLOW_CLK_SRC_XTAL32K_FREQ`

```c
#define ESP32_RTC_SLOW_CLK_SRC_XTAL32K_FREQ 32768
```

<a id="abe244da38fbe794e93094feef9b188fe"></a>

### `ESP32_SARADC_MODULE`

```c
#define ESP32_SARADC_MODULE 118
```

SAR ADC模块（Module）。

<a id="a83b43d5f4d6373a5bb437de5ee5c091f"></a>

### `ESP32_SDIO_SLAVE_MODULE`

```c
#define ESP32_SDIO_SLAVE_MODULE 112
```

SDIO 从设备（Slave）模块（Module）。

<a id="a72052a75b3541623f59063260c4dbc32"></a>

### `ESP32_SDMMC_MODULE`

```c
#define ESP32_SDMMC_MODULE 111
```

SDMMC模块（Module）。

<a id="a683dd8814bf170018b63b57268c0fde9"></a>

### `ESP32_SHA_MODULE`

```c
#define ESP32_SHA_MODULE 116
```

SHA模块（Module）。

<a id="ac44ad6537fde43047aa04ba8ee35586e"></a>

### `ESP32_SPI_DMA_MODULE`

```c
#define ESP32_SPI_DMA_MODULE 110
```

SPI DMA模块（Module）。

<a id="a5652d0e2b1fc766dde13b84294d4576b"></a>

### `ESP32_SPI_MODULE`

```c
#define ESP32_SPI_MODULE 6
```

SPI1模块（Module）。

<a id="a88ae2c1bafdc6e78258ada5cbb9368f9"></a>

### `ESP32_TIMG0_MODULE`

```c
#define ESP32_TIMG0_MODULE 3
```

定时器组 0（Timer Group 0）模块（Module）。

<a id="a251462caa49fc6fe0ae1c8fe99a87caa"></a>

### `ESP32_TIMG1_MODULE`

```c
#define ESP32_TIMG1_MODULE 4
```

定时器组 1（Timer Group 1）模块（Module）。

<a id="aba65cf1082c8422cc1e91c710bb702cc"></a>

### `ESP32_TWAI_MODULE`

```c
#define ESP32_TWAI_MODULE 113
```

TWAI模块（Module）。

<a id="a9708d046fbadfb7ccbc5df3e0ae57844"></a>

### `ESP32_UART0_MODULE`

```c
#define ESP32_UART0_MODULE 101
```

UART0模块（Module）。

<a id="a480803130ef80df04527f4dd12525d48"></a>

### `ESP32_UART1_MODULE`

```c
#define ESP32_UART1_MODULE 0
```

UART1模块（Module）。

<a id="a975be76987c86a84903dcc626bdc1478"></a>

### `ESP32_UART2_MODULE`

```c
#define ESP32_UART2_MODULE 1
```

UART2模块（Module）。

<a id="af5ef985d4eaf1ffe565e2662493178c6"></a>

### `ESP32_UHCI0_MODULE`

```c
#define ESP32_UHCI0_MODULE 5
```

UHCI0模块（Module）。

<a id="aa2c199cff85bcf8e5a306a056e71f1f5"></a>

### `ESP32_UHCI1_MODULE`

```c
#define ESP32_UHCI1_MODULE 107
```

UHCI1模块（Module）。

<a id="a982e8ce4deccacd4d020cdfed8771cac"></a>

### `ESP32_VSPI_MODULE`

```c
#define ESP32_VSPI_MODULE 8
```

VSPI模块（Module）。

<a id="aba1295479849f8b4dc44245e330e3020"></a>

### `ESP32_WIFI_BT_COMMON_MODULE`

```c
#define ESP32_WIFI_BT_COMMON_MODULE 12
```

Wi-Fi／蓝牙共用（Wi-Fi/BT Common）模块（Module）。

<a id="a4013c1fc7538bf46d5c1771f837a8b21"></a>

### `ESP32_WIFI_MODULE`

```c
#define ESP32_WIFI_MODULE 10
```

Wi-Fi模块（Module）。


## 5.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_compiler_device_reference/P006_esp32_clock.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P004_zephyr__drivers__led.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__dt-bindings__clock__esp32c2_clock.h_文件参考.md)
