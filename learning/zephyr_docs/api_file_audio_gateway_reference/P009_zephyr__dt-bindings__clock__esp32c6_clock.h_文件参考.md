---
id: learning.zephyr-docs.api-file-audio-gateway-reference.page-9
title: zephyr__dt-bindings__clock__esp32c6_clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/esp32c6__clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_zephyr\_\_dt-bindings\_\_clock\_\_esp32c6\_clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/esp32c6__clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.1\_宏定义（Macros）

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

<a id="r_ab779f427209fda571ec4d229b8ef8bfc"></a>

```c
#define ESP32_CLK_CPU_RC_FAST_FREQ 17500000
```

相关声明：[ESP32_CLK_CPU_RC_FAST_FREQ](#ab779f427209fda571ec4d229b8ef8bfc)。

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

<a id="r_aae48d9f1288771e11c11d6177ecf3af7"></a>

```c
#define ESP32_RTC_FAST_CLK_SRC_RC_FAST 0
```

相关声明：[ESP32_RTC_FAST_CLK_SRC_RC_FAST](#aae48d9f1288771e11c11d6177ecf3af7)。

<a id="r_a725193bf445b7f8f2c1058a6735ca476"></a>

```c
#define ESP32_RTC_FAST_CLK_SRC_XTAL_D2 1
```

相关声明：[ESP32_RTC_FAST_CLK_SRC_XTAL_D2](#a725193bf445b7f8f2c1058a6735ca476)。

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

<a id="r_ad2816af571c412c39237c7e2f5f18c04"></a>

```c
#define ESP32_RTC_SLOW_CLK_SRC_RC32K 2
```

相关声明：[ESP32_RTC_SLOW_CLK_SRC_RC32K](#ad2816af571c412c39237c7e2f5f18c04)。

<a id="r_aa5d6a46de7da027832aa02489c062069"></a>

```c
#define ESP32_RTC_SLOW_CLK_32K_EXT_OSC 9
```

相关声明：[ESP32_RTC_SLOW_CLK_32K_EXT_OSC](#aa5d6a46de7da027832aa02489c062069)。

<a id="r_af5cdcfa17e680ceda2f90e375eded6e6"></a>

```c
#define ESP32_RTC_SLOW_CLK_SRC_RC_SLOW_FREQ 136000
```

相关声明：[ESP32_RTC_SLOW_CLK_SRC_RC_SLOW_FREQ](#af5cdcfa17e680ceda2f90e375eded6e6)。

<a id="r_ab63ec0973bfb87f7f09c5614ab66deb8"></a>

```c
#define ESP32_RTC_SLOW_CLK_SRC_XTAL32K_FREQ 32768
```

相关声明：[ESP32_RTC_SLOW_CLK_SRC_XTAL32K_FREQ](#ab63ec0973bfb87f7f09c5614ab66deb8)。

<a id="r_a3b18cdc509424e2249c7f4c3f1d93107"></a>

```c
#define ESP32_RTC_SLOW_CLK_SRC_RC32K_FREQ 32768
```

相关声明：[ESP32_RTC_SLOW_CLK_SRC_RC32K_FREQ](#a3b18cdc509424e2249c7f4c3f1d93107)。

<a id="r_a88ae2c1bafdc6e78258ada5cbb9368f9"></a>

```c
#define ESP32_TIMG0_MODULE 0
```

相关声明：[ESP32_TIMG0_MODULE](#a88ae2c1bafdc6e78258ada5cbb9368f9)。

定时器组 0（Timer Group 0）模块（Module）。

<a id="r_a251462caa49fc6fe0ae1c8fe99a87caa"></a>

```c
#define ESP32_TIMG1_MODULE 1
```

相关声明：[ESP32_TIMG1_MODULE](#a251462caa49fc6fe0ae1c8fe99a87caa)。

定时器组 1（Timer Group 1）模块（Module）。

<a id="r_af5ef985d4eaf1ffe565e2662493178c6"></a>

```c
#define ESP32_UHCI0_MODULE 2
```

相关声明：[ESP32_UHCI0_MODULE](#af5ef985d4eaf1ffe565e2662493178c6)。

UHCI0模块（Module）。

<a id="r_aaf8e1de1e86906ba539863b9009ebe37"></a>

```c
#define ESP32_SYSTIMER_MODULE 3
```

相关声明：[ESP32_SYSTIMER_MODULE](#aaf8e1de1e86906ba539863b9009ebe37)。

系统定时器（System Timer）模块（Module）。

<a id="r_a4013c1fc7538bf46d5c1771f837a8b21"></a>

```c
#define ESP32_WIFI_MODULE 4
```

相关声明：[ESP32_WIFI_MODULE](#a4013c1fc7538bf46d5c1771f837a8b21)。

Wi-Fi模块（Module）。

<a id="r_ad180ebcea5567ce6c3145998f3761584"></a>

```c
#define ESP32_BT_MODULE 5
```

相关声明：[ESP32_BT_MODULE](#ad180ebcea5567ce6c3145998f3761584)。

蓝牙（Bluetooth）模块（Module）。

<a id="r_adf10ec1f34cbc43fb1e896da892c677d"></a>

```c
#define ESP32_IEEE802154_MODULE 6
```

相关声明：[ESP32_IEEE802154_MODULE](#adf10ec1f34cbc43fb1e896da892c677d)。

IEEE 802.15.4模块（Module）。

<a id="r_afe4f89e4a6712cc76536ea1b6a769a2d"></a>

```c
#define ESP32_COEX_MODULE 7
```

相关声明：[ESP32_COEX_MODULE](#afe4f89e4a6712cc76536ea1b6a769a2d)。

共存（Coexistence）模块（Module）。

<a id="r_ae77d17fb45b7464a1ae16cc8e95ad6a2"></a>

```c
#define ESP32_PHY_MODULE 8
```

相关声明：[ESP32_PHY_MODULE](#ae77d17fb45b7464a1ae16cc8e95ad6a2)。

PHY模块（Module）。

<a id="r_aa7706ddf6ed1aeddc3e49e0cf50e9d67"></a>

```c
#define ESP32_ANA_I2C_MASTER_MODULE 9
```

相关声明：[ESP32_ANA_I2C_MASTER_MODULE](#aa7706ddf6ed1aeddc3e49e0cf50e9d67)。

模拟 I2C 主设备（Analog I2C Master）模块（Module）。

<a id="r_a81c2b97c61c9d54f884475556a5c919f"></a>

```c
#define ESP32_MODEM_ETM_MODULE 10
```

相关声明：[ESP32_MODEM_ETM_MODULE](#a81c2b97c61c9d54f884475556a5c919f)。

调制解调器 ETM（Modem ETM）模块（Module）。

<a id="r_a063e6c8b4187177feeb1a13dd8b09742"></a>

```c
#define ESP32_MODEM_ADC_COMMON_FE_MODULE 11
```

相关声明：[ESP32_MODEM_ADC_COMMON_FE_MODULE](#a063e6c8b4187177feeb1a13dd8b09742)。

调制解调器 ADC 共用前端（Modem ADC Common FE）模块（Module）。

<a id="r_ade25c42235583c47d9abf29f66c00ed2"></a>

```c
#define ESP32_PHY_CALIBRATION_MODULE 12
```

相关声明：[ESP32_PHY_CALIBRATION_MODULE](#ade25c42235583c47d9abf29f66c00ed2)。

物理层校准（PHY Calibration）模块（Module）。

<a id="r_ac380a7ff843ee465763a355cb01ef295"></a>

```c
#define ESP32_MODULE_MAX 13
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

<a id="r_afcf8170a750f4dc35326010b52f4e082"></a>

```c
#define ESP32_USB_MODULE 103
```

相关声明：[ESP32_USB_MODULE](#afcf8170a750f4dc35326010b52f4e082)。

USB模块（Module）。

<a id="r_a7331ffa2ec41896d05f1f86c4d30f758"></a>

```c
#define ESP32_I2C0_MODULE 104
```

相关声明：[ESP32_I2C0_MODULE](#a7331ffa2ec41896d05f1f86c4d30f758)。

I2C0模块（Module）。

<a id="r_a1cc05bfada949af9e9265abaadb1b6bc"></a>

```c
#define ESP32_I2S1_MODULE 105
```

相关声明：[ESP32_I2S1_MODULE](#a1cc05bfada949af9e9265abaadb1b6bc)。

I2S1模块（Module）。

<a id="r_a4a2d8ca15cd619022c02f97842d54159"></a>

```c
#define ESP32_RMT_MODULE 106
```

相关声明：[ESP32_RMT_MODULE](#a4a2d8ca15cd619022c02f97842d54159)。

RMT模块（Module）。

<a id="r_ac0d8fb4397baaac7ff45dee8f4e1cb7c"></a>

```c
#define ESP32_PCNT_MODULE 107
```

相关声明：[ESP32_PCNT_MODULE](#ac0d8fb4397baaac7ff45dee8f4e1cb7c)。

PCNT模块（Module）。

<a id="r_a5652d0e2b1fc766dde13b84294d4576b"></a>

```c
#define ESP32_SPI_MODULE 108
```

相关声明：[ESP32_SPI_MODULE](#a5652d0e2b1fc766dde13b84294d4576b)。

SPI1模块（Module）。

<a id="r_a5e5283c23811e9c4f30980f1d865773b"></a>

```c
#define ESP32_SPI2_MODULE 109
```

相关声明：[ESP32_SPI2_MODULE](#a5e5283c23811e9c4f30980f1d865773b)。

SPI2模块（Module）。

<a id="r_ad6847f96f663ae04ca4d2c324b793d16"></a>

```c
#define ESP32_TWAI0_MODULE 110
```

相关声明：[ESP32_TWAI0_MODULE](#ad6847f96f663ae04ca4d2c324b793d16)。

TWAI0模块（Module）。

<a id="r_a0f0617f973ff3de27881f36957cd7cf2"></a>

```c
#define ESP32_TWAI1_MODULE 111
```

相关声明：[ESP32_TWAI1_MODULE](#a0f0617f973ff3de27881f36957cd7cf2)。

TWAI1模块（Module）。

<a id="r_ad5423ca02819aab6b3fe63c11b3cf998"></a>

```c
#define ESP32_RNG_MODULE 112
```

相关声明：[ESP32_RNG_MODULE](#ad5423ca02819aab6b3fe63c11b3cf998)。

RNG模块（Module）。

<a id="r_a701fec66fac239e66a19389ea153ff75"></a>

```c
#define ESP32_GDMA_MODULE 113
```

相关声明：[ESP32_GDMA_MODULE](#a701fec66fac239e66a19389ea153ff75)。

GDMA模块（Module）。

<a id="r_a13e722b2a08b3ea2da2ba3b40d794697"></a>

```c
#define ESP32_MCPWM0_MODULE 114
```

相关声明：[ESP32_MCPWM0_MODULE](#a13e722b2a08b3ea2da2ba3b40d794697)。

MCPWM0模块（Module）。

<a id="r_a991c820648c7ef77b5aff2cecefee45d"></a>

```c
#define ESP32_ETM_MODULE 115
```

相关声明：[ESP32_ETM_MODULE](#a991c820648c7ef77b5aff2cecefee45d)。

ETM模块（Module）。

<a id="r_ada34a774bc3ec003c91cfe7c89939763"></a>

```c
#define ESP32_PARLIO_MODULE 116
```

相关声明：[ESP32_PARLIO_MODULE](#ada34a774bc3ec003c91cfe7c89939763)。

并行 I/O（Parallel IO）模块（Module）。

<a id="r_a488d6d32cf66e81a27f0999f837fe39a"></a>

```c
#define ESP32_TEMPSENSOR_MODULE 117
```

相关声明：[ESP32_TEMPSENSOR_MODULE](#a488d6d32cf66e81a27f0999f837fe39a)。

温度传感器（Temperature Sensor）模块（Module）。

<a id="r_abe244da38fbe794e93094feef9b188fe"></a>

```c
#define ESP32_SARADC_MODULE 118
```

相关声明：[ESP32_SARADC_MODULE](#abe244da38fbe794e93094feef9b188fe)。

SAR ADC模块（Module）。

<a id="r_a5261565b59c0a5b75794014b80692b33"></a>

```c
#define ESP32_RSA_MODULE 119
```

相关声明：[ESP32_RSA_MODULE](#a5261565b59c0a5b75794014b80692b33)。

RSA模块（Module）。

<a id="r_a290ac6ab6c5de2e8d84a911e389e1cfc"></a>

```c
#define ESP32_AES_MODULE 120
```

相关声明：[ESP32_AES_MODULE](#a290ac6ab6c5de2e8d84a911e389e1cfc)。

AES模块（Module）。

<a id="r_a683dd8814bf170018b63b57268c0fde9"></a>

```c
#define ESP32_SHA_MODULE 121
```

相关声明：[ESP32_SHA_MODULE](#a683dd8814bf170018b63b57268c0fde9)。

SHA模块（Module）。

<a id="r_a27bd450bf21c8b7502d1f32d9536129f"></a>

```c
#define ESP32_ECC_MODULE 122
```

相关声明：[ESP32_ECC_MODULE](#a27bd450bf21c8b7502d1f32d9536129f)。

ECC模块（Module）。

<a id="r_ae17c59442b576d1b9aade6019850e6f8"></a>

```c
#define ESP32_HMAC_MODULE 123
```

相关声明：[ESP32_HMAC_MODULE](#ae17c59442b576d1b9aade6019850e6f8)。

HMAC模块（Module）。

<a id="r_aaea0a7a0e789019e4ddfd38365e83688"></a>

```c
#define ESP32_DS_MODULE 124
```

相关声明：[ESP32_DS_MODULE](#aaea0a7a0e789019e4ddfd38365e83688)。

数字签名（Digital Signature）模块（Module）。

<a id="r_a83b43d5f4d6373a5bb437de5ee5c091f"></a>

```c
#define ESP32_SDIO_SLAVE_MODULE 125
```

相关声明：[ESP32_SDIO_SLAVE_MODULE](#a83b43d5f4d6373a5bb437de5ee5c091f)。

SDIO 从设备（Slave）模块（Module）。

<a id="r_a4ff487b01c5240b09197ecf59d794975"></a>

```c
#define ESP32_ASSIST_DEBUG_MODULE 126
```

相关声明：[ESP32_ASSIST_DEBUG_MODULE](#a4ff487b01c5240b09197ecf59d794975)。

辅助调试（Assist Debug）模块（Module）。

<a id="r_a5ccf92c28d468d746c24d34453ff1caa"></a>

```c
#define ESP32_LP_I2C0_MODULE 127
```

相关声明：[ESP32_LP_I2C0_MODULE](#a5ccf92c28d468d746c24d34453ff1caa)。

LP I2C0模块（Module）。

<a id="r_a4355b5840ff4f0c4940a713c06e46326"></a>

```c
#define ESP32_LP_UART0_MODULE 128
```

相关声明：[ESP32_LP_UART0_MODULE](#a4355b5840ff4f0c4940a713c06e46326)。

LP UART0模块（Module）。

## 9.2\_详细说明（Detailed Documentation）

<a id="a290ac6ab6c5de2e8d84a911e389e1cfc"></a>

### `ESP32_AES_MODULE`

```c
#define ESP32_AES_MODULE 120
```

AES模块（Module）。

<a id="aa7706ddf6ed1aeddc3e49e0cf50e9d67"></a>

### `ESP32_ANA_I2C_MASTER_MODULE`

```c
#define ESP32_ANA_I2C_MASTER_MODULE 9
```

模拟 I2C 主设备（Analog I2C Master）模块（Module）。

<a id="a4ff487b01c5240b09197ecf59d794975"></a>

### `ESP32_ASSIST_DEBUG_MODULE`

```c
#define ESP32_ASSIST_DEBUG_MODULE 126
```

辅助调试（Assist Debug）模块（Module）。

<a id="ad180ebcea5567ce6c3145998f3761584"></a>

### `ESP32_BT_MODULE`

```c
#define ESP32_BT_MODULE 5
```

蓝牙（Bluetooth）模块（Module）。

<a id="ad80a59287e6a2f3771fd448982be9555"></a>

### `ESP32_CLK_CPU_PLL_160M`

```c
#define ESP32_CLK_CPU_PLL_160M 160000000
```

<a id="a61275f95111fb2a6bdbe446c0228f877"></a>

### `ESP32_CLK_CPU_PLL_80M`

```c
#define ESP32_CLK_CPU_PLL_80M 80000000
```

<a id="ab779f427209fda571ec4d229b8ef8bfc"></a>

### `ESP32_CLK_CPU_RC_FAST_FREQ`

```c
#define ESP32_CLK_CPU_RC_FAST_FREQ 17500000
```

<a id="a1962dad90f737a51fcc70cea1931b236"></a>

### `ESP32_CLK_SRC_RC_FAST`

```c
#define ESP32_CLK_SRC_RC_FAST 2U
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
#define ESP32_COEX_MODULE 7
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

<a id="aaea0a7a0e789019e4ddfd38365e83688"></a>

### `ESP32_DS_MODULE`

```c
#define ESP32_DS_MODULE 124
```

数字签名（Digital Signature）模块（Module）。

<a id="a27bd450bf21c8b7502d1f32d9536129f"></a>

### `ESP32_ECC_MODULE`

```c
#define ESP32_ECC_MODULE 122
```

ECC模块（Module）。

<a id="a991c820648c7ef77b5aff2cecefee45d"></a>

### `ESP32_ETM_MODULE`

```c
#define ESP32_ETM_MODULE 115
```

ETM模块（Module）。

<a id="a701fec66fac239e66a19389ea153ff75"></a>

### `ESP32_GDMA_MODULE`

```c
#define ESP32_GDMA_MODULE 113
```

GDMA模块（Module）。

<a id="ae17c59442b576d1b9aade6019850e6f8"></a>

### `ESP32_HMAC_MODULE`

```c
#define ESP32_HMAC_MODULE 123
```

HMAC模块（Module）。

<a id="a7331ffa2ec41896d05f1f86c4d30f758"></a>

### `ESP32_I2C0_MODULE`

```c
#define ESP32_I2C0_MODULE 104
```

I2C0模块（Module）。

<a id="a1cc05bfada949af9e9265abaadb1b6bc"></a>

### `ESP32_I2S1_MODULE`

```c
#define ESP32_I2S1_MODULE 105
```

I2S1模块（Module）。

<a id="adf10ec1f34cbc43fb1e896da892c677d"></a>

### `ESP32_IEEE802154_MODULE`

```c
#define ESP32_IEEE802154_MODULE 6
```

IEEE 802.15.4模块（Module）。

<a id="a60f4f5ee56d788f2161b52ebbc2aa510"></a>

### `ESP32_LEDC_MODULE`

```c
#define ESP32_LEDC_MODULE 100
```

LEDC模块（Module）。

<a id="a5ccf92c28d468d746c24d34453ff1caa"></a>

### `ESP32_LP_I2C0_MODULE`

```c
#define ESP32_LP_I2C0_MODULE 127
```

LP I2C0模块（Module）。

<a id="a4355b5840ff4f0c4940a713c06e46326"></a>

### `ESP32_LP_UART0_MODULE`

```c
#define ESP32_LP_UART0_MODULE 128
```

LP UART0模块（Module）。

<a id="a13e722b2a08b3ea2da2ba3b40d794697"></a>

### `ESP32_MCPWM0_MODULE`

```c
#define ESP32_MCPWM0_MODULE 114
```

MCPWM0模块（Module）。

<a id="a063e6c8b4187177feeb1a13dd8b09742"></a>

### `ESP32_MODEM_ADC_COMMON_FE_MODULE`

```c
#define ESP32_MODEM_ADC_COMMON_FE_MODULE 11
```

调制解调器 ADC 共用前端（Modem ADC Common FE）模块（Module）。

<a id="a81c2b97c61c9d54f884475556a5c919f"></a>

### `ESP32_MODEM_ETM_MODULE`

```c
#define ESP32_MODEM_ETM_MODULE 10
```

调制解调器 ETM（Modem ETM）模块（Module）。

<a id="ac380a7ff843ee465763a355cb01ef295"></a>

### `ESP32_MODULE_MAX`

```c
#define ESP32_MODULE_MAX 13
```

模块数量（Module Count）。

<a id="ada34a774bc3ec003c91cfe7c89939763"></a>

### `ESP32_PARLIO_MODULE`

```c
#define ESP32_PARLIO_MODULE 116
```

并行 I/O（Parallel IO）模块（Module）。

<a id="ac0d8fb4397baaac7ff45dee8f4e1cb7c"></a>

### `ESP32_PCNT_MODULE`

```c
#define ESP32_PCNT_MODULE 107
```

PCNT模块（Module）。

<a id="ade25c42235583c47d9abf29f66c00ed2"></a>

### `ESP32_PHY_CALIBRATION_MODULE`

```c
#define ESP32_PHY_CALIBRATION_MODULE 12
```

物理层校准（PHY Calibration）模块（Module）。

<a id="ae77d17fb45b7464a1ae16cc8e95ad6a2"></a>

### `ESP32_PHY_MODULE`

```c
#define ESP32_PHY_MODULE 8
```

PHY模块（Module）。

<a id="a4a2d8ca15cd619022c02f97842d54159"></a>

### `ESP32_RMT_MODULE`

```c
#define ESP32_RMT_MODULE 106
```

RMT模块（Module）。

<a id="ad5423ca02819aab6b3fe63c11b3cf998"></a>

### `ESP32_RNG_MODULE`

```c
#define ESP32_RNG_MODULE 112
```

RNG模块（Module）。

<a id="a5261565b59c0a5b75794014b80692b33"></a>

### `ESP32_RSA_MODULE`

```c
#define ESP32_RSA_MODULE 119
```

RSA模块（Module）。

<a id="aae48d9f1288771e11c11d6177ecf3af7"></a>

### `ESP32_RTC_FAST_CLK_SRC_RC_FAST`

```c
#define ESP32_RTC_FAST_CLK_SRC_RC_FAST 0
```

<a id="a725193bf445b7f8f2c1058a6735ca476"></a>

### `ESP32_RTC_FAST_CLK_SRC_XTAL_D2`

```c
#define ESP32_RTC_FAST_CLK_SRC_XTAL_D2 1
```

<a id="aa5d6a46de7da027832aa02489c062069"></a>

### `ESP32_RTC_SLOW_CLK_32K_EXT_OSC`

```c
#define ESP32_RTC_SLOW_CLK_32K_EXT_OSC 9
```

<a id="ad2816af571c412c39237c7e2f5f18c04"></a>

### `ESP32_RTC_SLOW_CLK_SRC_RC32K`

```c
#define ESP32_RTC_SLOW_CLK_SRC_RC32K 2
```

<a id="a3b18cdc509424e2249c7f4c3f1d93107"></a>

### `ESP32_RTC_SLOW_CLK_SRC_RC32K_FREQ`

```c
#define ESP32_RTC_SLOW_CLK_SRC_RC32K_FREQ 32768
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
#define ESP32_SDIO_SLAVE_MODULE 125
```

SDIO 从设备（Slave）模块（Module）。

<a id="a683dd8814bf170018b63b57268c0fde9"></a>

### `ESP32_SHA_MODULE`

```c
#define ESP32_SHA_MODULE 121
```

SHA模块（Module）。

<a id="a5e5283c23811e9c4f30980f1d865773b"></a>

### `ESP32_SPI2_MODULE`

```c
#define ESP32_SPI2_MODULE 109
```

SPI2模块（Module）。

<a id="a5652d0e2b1fc766dde13b84294d4576b"></a>

### `ESP32_SPI_MODULE`

```c
#define ESP32_SPI_MODULE 108
```

SPI1模块（Module）。

<a id="aaf8e1de1e86906ba539863b9009ebe37"></a>

### `ESP32_SYSTIMER_MODULE`

```c
#define ESP32_SYSTIMER_MODULE 3
```

系统定时器（System Timer）模块（Module）。

<a id="a488d6d32cf66e81a27f0999f837fe39a"></a>

### `ESP32_TEMPSENSOR_MODULE`

```c
#define ESP32_TEMPSENSOR_MODULE 117
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
#define ESP32_TIMG1_MODULE 1
```

定时器组 1（Timer Group 1）模块（Module）。

<a id="ad6847f96f663ae04ca4d2c324b793d16"></a>

### `ESP32_TWAI0_MODULE`

```c
#define ESP32_TWAI0_MODULE 110
```

TWAI0模块（Module）。

<a id="a0f0617f973ff3de27881f36957cd7cf2"></a>

### `ESP32_TWAI1_MODULE`

```c
#define ESP32_TWAI1_MODULE 111
```

TWAI1模块（Module）。

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
#define ESP32_UHCI0_MODULE 2
```

UHCI0模块（Module）。

<a id="afcf8170a750f4dc35326010b52f4e082"></a>

### `ESP32_USB_MODULE`

```c
#define ESP32_USB_MODULE 103
```

USB模块（Module）。

<a id="a4013c1fc7538bf46d5c1771f837a8b21"></a>

### `ESP32_WIFI_MODULE`

```c
#define ESP32_WIFI_MODULE 4
```

Wi-Fi模块（Module）。


## 9.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_transport_clock_reference/P012_esp32c6_clock.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P008_zephyr__dt-bindings__clock__esp32c61_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_zephyr__dt-bindings__clock__esp32h2_clock.h_文件参考.md)
