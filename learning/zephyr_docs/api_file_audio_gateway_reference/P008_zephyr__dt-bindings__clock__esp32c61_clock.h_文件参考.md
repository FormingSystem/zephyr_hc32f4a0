---
id: learning.zephyr-docs.api-file-audio-gateway-reference.page-8
title: zephyr__dt-bindings__clock__esp32c61_clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/esp32c61__clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_zephyr\_\_dt-bindings\_\_clock\_\_esp32c61\_clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/esp32c61__clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于设备树绑定（Device Tree Bindings）的ESP32-C61时钟定义。

查看此文件的源码。

<a id="details"></a>

用于设备树绑定（Device Tree Bindings）的ESP32-C61时钟定义。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 8.1\_宏定义（Macros）

<a id="r_a44ee3670c3168dd0ffbc79a563a7f074"></a>

```c
#define ESP32_CPU_CLK_SRC_XTAL 0U
```

相关声明：[ESP32_CPU_CLK_SRC_XTAL](#a44ee3670c3168dd0ffbc79a563a7f074)。

CPU 时钟源（Clock Source）：晶体振荡器（XTAL）。

<a id="r_a7a723b6353a23b55ef44d720297fe26f"></a>

```c
#define ESP32_CPU_CLK_SRC_PLL 1U
```

相关声明：[ESP32_CPU_CLK_SRC_PLL](#a7a723b6353a23b55ef44d720297fe26f)。

CPU 时钟源（Clock Source）：锁相环（PLL）。

<a id="r_a1962dad90f737a51fcc70cea1931b236"></a>

```c
#define ESP32_CLK_SRC_RC_FAST 2U
```

相关声明：[ESP32_CLK_SRC_RC_FAST](#a1962dad90f737a51fcc70cea1931b236)。

CPU 时钟源（Clock Source）：高速 RC（RC Fast）。

<a id="r_a61275f95111fb2a6bdbe446c0228f877"></a>

```c
#define ESP32_CLK_CPU_PLL_80M 80000000
```

相关声明：[ESP32_CLK_CPU_PLL_80M](#a61275f95111fb2a6bdbe446c0228f877)。

CPU 锁相环时钟（PLL Clock）：80 MHz。

<a id="r_ad80a59287e6a2f3771fd448982be9555"></a>

```c
#define ESP32_CLK_CPU_PLL_160M 160000000
```

相关声明：[ESP32_CLK_CPU_PLL_160M](#ad80a59287e6a2f3771fd448982be9555)。

CPU 锁相环时钟（PLL Clock）：160 MHz。

<a id="r_ab779f427209fda571ec4d229b8ef8bfc"></a>

```c
#define ESP32_CLK_CPU_RC_FAST_FREQ 17500000
```

相关声明：[ESP32_CLK_CPU_RC_FAST_FREQ](#ab779f427209fda571ec4d229b8ef8bfc)。

CPU 高速 RC 时钟（RC Fast Clock）：17.5 MHz。

<a id="r_a6afe38f9f9c44a1bd2e5279163523a98"></a>

```c
#define ESP32_CLK_XTAL_40M 40000000
```

相关声明：[ESP32_CLK_XTAL_40M](#a6afe38f9f9c44a1bd2e5279163523a98)。

晶体时钟（XTAL Clock）：40 MHz。

<a id="r_aae48d9f1288771e11c11d6177ecf3af7"></a>

```c
#define ESP32_RTC_FAST_CLK_SRC_RC_FAST 0
```

相关声明：[ESP32_RTC_FAST_CLK_SRC_RC_FAST](#aae48d9f1288771e11c11d6177ecf3af7)。

RTC 高速时钟源（Fast Clock Source）：高速 RC（RC Fast）。

<a id="r_a725193bf445b7f8f2c1058a6735ca476"></a>

```c
#define ESP32_RTC_FAST_CLK_SRC_XTAL_D2 1
```

相关声明：[ESP32_RTC_FAST_CLK_SRC_XTAL_D2](#a725193bf445b7f8f2c1058a6735ca476)。

RTC 高速时钟源（Fast Clock Source）：XTAL/2。

<a id="r_ae82f4db340753c2e771fad5184d83800"></a>

```c
#define ESP32_RTC_FAST_CLK_SRC_XTAL 2
```

相关声明：[ESP32_RTC_FAST_CLK_SRC_XTAL](#ae82f4db340753c2e771fad5184d83800)。

RTC 高速时钟源（Fast Clock Source）：晶体振荡器（XTAL）。

<a id="r_ad1d90df80dee3040dbe8c968cd774443"></a>

```c
#define ESP32_RTC_SLOW_CLK_SRC_RC_SLOW 0
```

相关声明：[ESP32_RTC_SLOW_CLK_SRC_RC_SLOW](#ad1d90df80dee3040dbe8c968cd774443)。

RTC 低速时钟源（Slow Clock Source）：低速 RC（RC Slow）。

<a id="r_aeaccf7695cab85cd7523c6ebc21704c4"></a>

```c
#define ESP32_RTC_SLOW_CLK_SRC_XTAL32K 1
```

相关声明：[ESP32_RTC_SLOW_CLK_SRC_XTAL32K](#aeaccf7695cab85cd7523c6ebc21704c4)。

RTC 低速时钟源（Slow Clock Source）：32 kHz 晶体（XTAL）。

<a id="r_a0c9ed1e9c69731554227e93ddd086e9e"></a>

```c
#define ESP32_RTC_SLOW_CLK_SRC_OSC_SLOW 3
```

相关声明：[ESP32_RTC_SLOW_CLK_SRC_OSC_SLOW](#a0c9ed1e9c69731554227e93ddd086e9e)。

RTC 低速时钟源（Slow Clock Source）：低速振荡器（OSC Slow）。

<a id="r_aa5d6a46de7da027832aa02489c062069"></a>

```c
#define ESP32_RTC_SLOW_CLK_32K_EXT_OSC 9
```

相关声明：[ESP32_RTC_SLOW_CLK_32K_EXT_OSC](#aa5d6a46de7da027832aa02489c062069)。

RTC 低速时钟源（Slow Clock Source）：外部 32 kHz 振荡器（External OSC）。

<a id="r_af5cdcfa17e680ceda2f90e375eded6e6"></a>

```c
#define ESP32_RTC_SLOW_CLK_SRC_RC_SLOW_FREQ 136000
```

相关声明：[ESP32_RTC_SLOW_CLK_SRC_RC_SLOW_FREQ](#af5cdcfa17e680ceda2f90e375eded6e6)。

低速 RC 时钟频率（RC Slow Clock Frequency）：136 kHz。

<a id="r_ab63ec0973bfb87f7f09c5614ab66deb8"></a>

```c
#define ESP32_RTC_SLOW_CLK_SRC_XTAL32K_FREQ 32768
```

相关声明：[ESP32_RTC_SLOW_CLK_SRC_XTAL32K_FREQ](#ab63ec0973bfb87f7f09c5614ab66deb8)。

32 kHz 晶体时钟频率（XTAL Clock Frequency）。

<a id="r_ab3d6d4b49e506dac9b7812b9abd30a82"></a>

```c
#define ESP32_RTC_SLOW_CLK_SRC_OSC_SLOW_FREQ 32768
```

相关声明：[ESP32_RTC_SLOW_CLK_SRC_OSC_SLOW_FREQ](#ab3d6d4b49e506dac9b7812b9abd30a82)。

低速振荡器时钟频率（OSC Slow Clock Frequency）：32.768 kHz。

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

<a id="r_aaf8e1de1e86906ba539863b9009ebe37"></a>

```c
#define ESP32_SYSTIMER_MODULE 2
```

相关声明：[ESP32_SYSTIMER_MODULE](#aaf8e1de1e86906ba539863b9009ebe37)。

系统定时器（System Timer）模块（Module）。

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

<a id="r_adf10ec1f34cbc43fb1e896da892c677d"></a>

```c
#define ESP32_IEEE802154_MODULE 5
```

相关声明：[ESP32_IEEE802154_MODULE](#adf10ec1f34cbc43fb1e896da892c677d)。

IEEE 802.15.4模块（Module）。

<a id="r_afe4f89e4a6712cc76536ea1b6a769a2d"></a>

```c
#define ESP32_COEX_MODULE 6
```

相关声明：[ESP32_COEX_MODULE](#afe4f89e4a6712cc76536ea1b6a769a2d)。

共存（Coexistence）模块（Module）。

<a id="r_ae77d17fb45b7464a1ae16cc8e95ad6a2"></a>

```c
#define ESP32_PHY_MODULE 7
```

相关声明：[ESP32_PHY_MODULE](#ae77d17fb45b7464a1ae16cc8e95ad6a2)。

PHY模块（Module）。

<a id="r_aa7706ddf6ed1aeddc3e49e0cf50e9d67"></a>

```c
#define ESP32_ANA_I2C_MASTER_MODULE 8
```

相关声明：[ESP32_ANA_I2C_MASTER_MODULE](#aa7706ddf6ed1aeddc3e49e0cf50e9d67)。

模拟 I2C 主设备（Analog I2C Master）模块（Module）。

<a id="r_a81c2b97c61c9d54f884475556a5c919f"></a>

```c
#define ESP32_MODEM_ETM_MODULE 9
```

相关声明：[ESP32_MODEM_ETM_MODULE](#a81c2b97c61c9d54f884475556a5c919f)。

调制解调器 ETM（Modem ETM）模块（Module）。

<a id="r_a063e6c8b4187177feeb1a13dd8b09742"></a>

```c
#define ESP32_MODEM_ADC_COMMON_FE_MODULE 10
```

相关声明：[ESP32_MODEM_ADC_COMMON_FE_MODULE](#a063e6c8b4187177feeb1a13dd8b09742)。

调制解调器 ADC 共用前端（Modem ADC Common FE）模块（Module）。

<a id="r_ade25c42235583c47d9abf29f66c00ed2"></a>

```c
#define ESP32_PHY_CALIBRATION_MODULE 11
```

相关声明：[ESP32_PHY_CALIBRATION_MODULE](#ade25c42235583c47d9abf29f66c00ed2)。

物理层校准（PHY Calibration）模块（Module）。

<a id="r_ac380a7ff843ee465763a355cb01ef295"></a>

```c
#define ESP32_MODULE_MAX 12
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

<a id="r_a975be76987c86a84903dcc626bdc1478"></a>

```c
#define ESP32_UART2_MODULE 103
```

相关声明：[ESP32_UART2_MODULE](#a975be76987c86a84903dcc626bdc1478)。

UART2模块（Module）。

<a id="r_afcf8170a750f4dc35326010b52f4e082"></a>

```c
#define ESP32_USB_MODULE 104
```

相关声明：[ESP32_USB_MODULE](#afcf8170a750f4dc35326010b52f4e082)。

USB模块（Module）。

<a id="r_a7331ffa2ec41896d05f1f86c4d30f758"></a>

```c
#define ESP32_I2C0_MODULE 105
```

相关声明：[ESP32_I2C0_MODULE](#a7331ffa2ec41896d05f1f86c4d30f758)。

I2C0模块（Module）。

<a id="r_a21c262b775f6d533621d4ba8e8d6c9aa"></a>

```c
#define ESP32_I2S0_MODULE 106
```

相关声明：[ESP32_I2S0_MODULE](#a21c262b775f6d533621d4ba8e8d6c9aa)。

I2S0模块（Module）。

<a id="r_a5652d0e2b1fc766dde13b84294d4576b"></a>

```c
#define ESP32_SPI_MODULE 107
```

相关声明：[ESP32_SPI_MODULE](#a5652d0e2b1fc766dde13b84294d4576b)。

SPI1模块（Module）。

<a id="r_a5e5283c23811e9c4f30980f1d865773b"></a>

```c
#define ESP32_SPI2_MODULE 108
```

相关声明：[ESP32_SPI2_MODULE](#a5e5283c23811e9c4f30980f1d865773b)。

SPI2模块（Module）。

<a id="r_ad5423ca02819aab6b3fe63c11b3cf998"></a>

```c
#define ESP32_RNG_MODULE 109
```

相关声明：[ESP32_RNG_MODULE](#ad5423ca02819aab6b3fe63c11b3cf998)。

RNG模块（Module）。

<a id="r_a701fec66fac239e66a19389ea153ff75"></a>

```c
#define ESP32_GDMA_MODULE 110
```

相关声明：[ESP32_GDMA_MODULE](#a701fec66fac239e66a19389ea153ff75)。

GDMA模块（Module）。

<a id="r_a991c820648c7ef77b5aff2cecefee45d"></a>

```c
#define ESP32_ETM_MODULE 111
```

相关声明：[ESP32_ETM_MODULE](#a991c820648c7ef77b5aff2cecefee45d)。

ETM模块（Module）。

<a id="r_a488d6d32cf66e81a27f0999f837fe39a"></a>

```c
#define ESP32_TEMPSENSOR_MODULE 112
```

相关声明：[ESP32_TEMPSENSOR_MODULE](#a488d6d32cf66e81a27f0999f837fe39a)。

温度传感器（Temperature Sensor）模块（Module）。

<a id="r_abe244da38fbe794e93094feef9b188fe"></a>

```c
#define ESP32_SARADC_MODULE 113
```

相关声明：[ESP32_SARADC_MODULE](#abe244da38fbe794e93094feef9b188fe)。

SAR ADC模块（Module）。

<a id="r_a683dd8814bf170018b63b57268c0fde9"></a>

```c
#define ESP32_SHA_MODULE 116
```

相关声明：[ESP32_SHA_MODULE](#a683dd8814bf170018b63b57268c0fde9)。

SHA模块（Module）。

<a id="r_a27bd450bf21c8b7502d1f32d9536129f"></a>

```c
#define ESP32_ECC_MODULE 117
```

相关声明：[ESP32_ECC_MODULE](#a27bd450bf21c8b7502d1f32d9536129f)。

ECC模块（Module）。

<a id="r_a83b43d5f4d6373a5bb437de5ee5c091f"></a>

```c
#define ESP32_SDIO_SLAVE_MODULE 120
```

相关声明：[ESP32_SDIO_SLAVE_MODULE](#a83b43d5f4d6373a5bb437de5ee5c091f)。

SDIO 从设备（Slave）模块（Module）。

<a id="r_a4ff487b01c5240b09197ecf59d794975"></a>

```c
#define ESP32_ASSIST_DEBUG_MODULE 121
```

相关声明：[ESP32_ASSIST_DEBUG_MODULE](#a4ff487b01c5240b09197ecf59d794975)。

辅助调试（Assist Debug）模块（Module）。

## 8.2\_详细说明（Detailed Documentation）

<a id="aa7706ddf6ed1aeddc3e49e0cf50e9d67"></a>

### `ESP32_ANA_I2C_MASTER_MODULE`

```c
#define ESP32_ANA_I2C_MASTER_MODULE 8
```

模拟 I2C 主设备（Analog I2C Master）模块（Module）。

<a id="a4ff487b01c5240b09197ecf59d794975"></a>

### `ESP32_ASSIST_DEBUG_MODULE`

```c
#define ESP32_ASSIST_DEBUG_MODULE 121
```

辅助调试（Assist Debug）模块（Module）。

<a id="ad180ebcea5567ce6c3145998f3761584"></a>

### `ESP32_BT_MODULE`

```c
#define ESP32_BT_MODULE 4
```

蓝牙（Bluetooth）模块（Module）。

<a id="ad80a59287e6a2f3771fd448982be9555"></a>

### `ESP32_CLK_CPU_PLL_160M`

```c
#define ESP32_CLK_CPU_PLL_160M 160000000
```

CPU 锁相环时钟（PLL Clock）：160 MHz。

<a id="a61275f95111fb2a6bdbe446c0228f877"></a>

### `ESP32_CLK_CPU_PLL_80M`

```c
#define ESP32_CLK_CPU_PLL_80M 80000000
```

CPU 锁相环时钟（PLL Clock）：80 MHz。

<a id="ab779f427209fda571ec4d229b8ef8bfc"></a>

### `ESP32_CLK_CPU_RC_FAST_FREQ`

```c
#define ESP32_CLK_CPU_RC_FAST_FREQ 17500000
```

CPU 高速 RC 时钟（RC Fast Clock）：17.5 MHz。

<a id="a1962dad90f737a51fcc70cea1931b236"></a>

### `ESP32_CLK_SRC_RC_FAST`

```c
#define ESP32_CLK_SRC_RC_FAST 2U
```

CPU 时钟源（Clock Source）：高速 RC（RC Fast）。

<a id="a6afe38f9f9c44a1bd2e5279163523a98"></a>

### `ESP32_CLK_XTAL_40M`

```c
#define ESP32_CLK_XTAL_40M 40000000
```

晶体时钟（XTAL Clock）：40 MHz。

<a id="afe4f89e4a6712cc76536ea1b6a769a2d"></a>

### `ESP32_COEX_MODULE`

```c
#define ESP32_COEX_MODULE 6
```

共存（Coexistence）模块（Module）。

<a id="a7a723b6353a23b55ef44d720297fe26f"></a>

### `ESP32_CPU_CLK_SRC_PLL`

```c
#define ESP32_CPU_CLK_SRC_PLL 1U
```

CPU 时钟源（Clock Source）：锁相环（PLL）。

<a id="a44ee3670c3168dd0ffbc79a563a7f074"></a>

### `ESP32_CPU_CLK_SRC_XTAL`

```c
#define ESP32_CPU_CLK_SRC_XTAL 0U
```

CPU 时钟源（Clock Source）：晶体振荡器（XTAL）。

<a id="a27bd450bf21c8b7502d1f32d9536129f"></a>

### `ESP32_ECC_MODULE`

```c
#define ESP32_ECC_MODULE 117
```

ECC模块（Module）。

<a id="a991c820648c7ef77b5aff2cecefee45d"></a>

### `ESP32_ETM_MODULE`

```c
#define ESP32_ETM_MODULE 111
```

ETM模块（Module）。

<a id="a701fec66fac239e66a19389ea153ff75"></a>

### `ESP32_GDMA_MODULE`

```c
#define ESP32_GDMA_MODULE 110
```

GDMA模块（Module）。

<a id="a7331ffa2ec41896d05f1f86c4d30f758"></a>

### `ESP32_I2C0_MODULE`

```c
#define ESP32_I2C0_MODULE 105
```

I2C0模块（Module）。

<a id="a21c262b775f6d533621d4ba8e8d6c9aa"></a>

### `ESP32_I2S0_MODULE`

```c
#define ESP32_I2S0_MODULE 106
```

I2S0模块（Module）。

<a id="adf10ec1f34cbc43fb1e896da892c677d"></a>

### `ESP32_IEEE802154_MODULE`

```c
#define ESP32_IEEE802154_MODULE 5
```

IEEE 802.15.4模块（Module）。

<a id="a60f4f5ee56d788f2161b52ebbc2aa510"></a>

### `ESP32_LEDC_MODULE`

```c
#define ESP32_LEDC_MODULE 100
```

LEDC模块（Module）。

<a id="a063e6c8b4187177feeb1a13dd8b09742"></a>

### `ESP32_MODEM_ADC_COMMON_FE_MODULE`

```c
#define ESP32_MODEM_ADC_COMMON_FE_MODULE 10
```

调制解调器 ADC 共用前端（Modem ADC Common FE）模块（Module）。

<a id="a81c2b97c61c9d54f884475556a5c919f"></a>

### `ESP32_MODEM_ETM_MODULE`

```c
#define ESP32_MODEM_ETM_MODULE 9
```

调制解调器 ETM（Modem ETM）模块（Module）。

<a id="ac380a7ff843ee465763a355cb01ef295"></a>

### `ESP32_MODULE_MAX`

```c
#define ESP32_MODULE_MAX 12
```

模块数量（Module Count）。

<a id="ade25c42235583c47d9abf29f66c00ed2"></a>

### `ESP32_PHY_CALIBRATION_MODULE`

```c
#define ESP32_PHY_CALIBRATION_MODULE 11
```

物理层校准（PHY Calibration）模块（Module）。

<a id="ae77d17fb45b7464a1ae16cc8e95ad6a2"></a>

### `ESP32_PHY_MODULE`

```c
#define ESP32_PHY_MODULE 7
```

PHY模块（Module）。

<a id="ad5423ca02819aab6b3fe63c11b3cf998"></a>

### `ESP32_RNG_MODULE`

```c
#define ESP32_RNG_MODULE 109
```

RNG模块（Module）。

<a id="aae48d9f1288771e11c11d6177ecf3af7"></a>

### `ESP32_RTC_FAST_CLK_SRC_RC_FAST`

```c
#define ESP32_RTC_FAST_CLK_SRC_RC_FAST 0
```

RTC 高速时钟源（Fast Clock Source）：高速 RC（RC Fast）。

<a id="ae82f4db340753c2e771fad5184d83800"></a>

### `ESP32_RTC_FAST_CLK_SRC_XTAL`

```c
#define ESP32_RTC_FAST_CLK_SRC_XTAL 2
```

RTC 高速时钟源（Fast Clock Source）：晶体振荡器（XTAL）。

<a id="a725193bf445b7f8f2c1058a6735ca476"></a>

### `ESP32_RTC_FAST_CLK_SRC_XTAL_D2`

```c
#define ESP32_RTC_FAST_CLK_SRC_XTAL_D2 1
```

RTC 高速时钟源（Fast Clock Source）：XTAL/2。

<a id="aa5d6a46de7da027832aa02489c062069"></a>

### `ESP32_RTC_SLOW_CLK_32K_EXT_OSC`

```c
#define ESP32_RTC_SLOW_CLK_32K_EXT_OSC 9
```

RTC 低速时钟源（Slow Clock Source）：外部 32 kHz 振荡器（External OSC）。

<a id="a0c9ed1e9c69731554227e93ddd086e9e"></a>

### `ESP32_RTC_SLOW_CLK_SRC_OSC_SLOW`

```c
#define ESP32_RTC_SLOW_CLK_SRC_OSC_SLOW 3
```

RTC 低速时钟源（Slow Clock Source）：低速振荡器（OSC Slow）。

<a id="ab3d6d4b49e506dac9b7812b9abd30a82"></a>

### `ESP32_RTC_SLOW_CLK_SRC_OSC_SLOW_FREQ`

```c
#define ESP32_RTC_SLOW_CLK_SRC_OSC_SLOW_FREQ 32768
```

低速振荡器时钟频率（OSC Slow Clock Frequency）：32.768 kHz。

<a id="ad1d90df80dee3040dbe8c968cd774443"></a>

### `ESP32_RTC_SLOW_CLK_SRC_RC_SLOW`

```c
#define ESP32_RTC_SLOW_CLK_SRC_RC_SLOW 0
```

RTC 低速时钟源（Slow Clock Source）：低速 RC（RC Slow）。

<a id="af5cdcfa17e680ceda2f90e375eded6e6"></a>

### `ESP32_RTC_SLOW_CLK_SRC_RC_SLOW_FREQ`

```c
#define ESP32_RTC_SLOW_CLK_SRC_RC_SLOW_FREQ 136000
```

低速 RC 时钟频率（RC Slow Clock Frequency）：136 kHz。

<a id="aeaccf7695cab85cd7523c6ebc21704c4"></a>

### `ESP32_RTC_SLOW_CLK_SRC_XTAL32K`

```c
#define ESP32_RTC_SLOW_CLK_SRC_XTAL32K 1
```

RTC 低速时钟源（Slow Clock Source）：32 kHz 晶体（XTAL）。

<a id="ab63ec0973bfb87f7f09c5614ab66deb8"></a>

### `ESP32_RTC_SLOW_CLK_SRC_XTAL32K_FREQ`

```c
#define ESP32_RTC_SLOW_CLK_SRC_XTAL32K_FREQ 32768
```

32 kHz 晶体时钟频率（XTAL Clock Frequency）。

<a id="abe244da38fbe794e93094feef9b188fe"></a>

### `ESP32_SARADC_MODULE`

```c
#define ESP32_SARADC_MODULE 113
```

SAR ADC模块（Module）。

<a id="a83b43d5f4d6373a5bb437de5ee5c091f"></a>

### `ESP32_SDIO_SLAVE_MODULE`

```c
#define ESP32_SDIO_SLAVE_MODULE 120
```

SDIO 从设备（Slave）模块（Module）。

<a id="a683dd8814bf170018b63b57268c0fde9"></a>

### `ESP32_SHA_MODULE`

```c
#define ESP32_SHA_MODULE 116
```

SHA模块（Module）。

<a id="a5e5283c23811e9c4f30980f1d865773b"></a>

### `ESP32_SPI2_MODULE`

```c
#define ESP32_SPI2_MODULE 108
```

SPI2模块（Module）。

<a id="a5652d0e2b1fc766dde13b84294d4576b"></a>

### `ESP32_SPI_MODULE`

```c
#define ESP32_SPI_MODULE 107
```

SPI1模块（Module）。

<a id="aaf8e1de1e86906ba539863b9009ebe37"></a>

### `ESP32_SYSTIMER_MODULE`

```c
#define ESP32_SYSTIMER_MODULE 2
```

系统定时器（System Timer）模块（Module）。

<a id="a488d6d32cf66e81a27f0999f837fe39a"></a>

### `ESP32_TEMPSENSOR_MODULE`

```c
#define ESP32_TEMPSENSOR_MODULE 112
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

<a id="a975be76987c86a84903dcc626bdc1478"></a>

### `ESP32_UART2_MODULE`

```c
#define ESP32_UART2_MODULE 103
```

UART2模块（Module）。

<a id="afcf8170a750f4dc35326010b52f4e082"></a>

### `ESP32_USB_MODULE`

```c
#define ESP32_USB_MODULE 104
```

USB模块（Module）。

<a id="a4013c1fc7538bf46d5c1771f837a8b21"></a>

### `ESP32_WIFI_MODULE`

```c
#define ESP32_WIFI_MODULE 3
```

Wi-Fi模块（Module）。


## 8.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_transport_clock_reference/P011_esp32c61_clock.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P007_zephyr__dt-bindings__clock__esp32c3_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P009_zephyr__dt-bindings__clock__esp32c6_clock.h_文件参考.md)
