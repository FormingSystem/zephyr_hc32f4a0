---
id: learning.zephyr-docs.api-file-clock-network-reference.page-9
title: zephyr__dt-bindings__clock__esp32p4_clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/esp32p4__clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_zephyr\_\_dt-bindings\_\_clock\_\_esp32p4\_clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/esp32p4__clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Espressif ESP32-P4的时钟模块标识符（Clock Module Identifiers）。

查看此文件的源码。

<a id="details"></a>

乐鑫 ESP32-P4 的时钟模块标识符（Clock Module Identifiers）。定义用于设备树时钟绑定（Devicetree Clock Bindings）的时钟源及外设模块 ID。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.1\_宏定义（Macros）

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

<a id="r_a89f74c5aac4ea4279b158faa18825ddf"></a>

```c
#define ESP32_CLK_CPU_PLL_100M 100000000
```

相关声明：[ESP32_CLK_CPU_PLL_100M](#a89f74c5aac4ea4279b158faa18825ddf)。

CPU 锁相环时钟（PLL Clock）：100 MHz。

<a id="r_a9233c5e62f6173181eec34e2690a4e6f"></a>

```c
#define ESP32_CLK_CPU_PLL_200M 200000000
```

相关声明：[ESP32_CLK_CPU_PLL_200M](#a9233c5e62f6173181eec34e2690a4e6f)。

CPU 锁相环时钟（PLL Clock）：200 MHz。

<a id="r_af962d7c379ba6b7b7c5eed2b9370e3cb"></a>

```c
#define ESP32_CLK_CPU_PLL_400M 400000000
```

相关声明：[ESP32_CLK_CPU_PLL_400M](#af962d7c379ba6b7b7c5eed2b9370e3cb)。

CPU 锁相环时钟（PLL Clock）：400 MHz。

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

<a id="r_ae82f4db340753c2e771fad5184d83800"></a>

```c
#define ESP32_RTC_FAST_CLK_SRC_XTAL 1
```

相关声明：[ESP32_RTC_FAST_CLK_SRC_XTAL](#ae82f4db340753c2e771fad5184d83800)。

RTC 高速时钟源（Fast Clock Source）：晶体振荡器（XTAL）。

<a id="r_a7bd20a93e37b5b7b356058bdd878f181"></a>

```c
#define ESP32_RTC_FAST_CLK_SRC_LP_PLL 2
```

相关声明：[ESP32_RTC_FAST_CLK_SRC_LP_PLL](#a7bd20a93e37b5b7b356058bdd878f181)。

RTC 高速时钟源（Fast Clock Source）：低功耗锁相环（LP PLL）。

<a id="r_aa01463cb65a93ac131d3a4213ee70991"></a>

```c
#define ESP32_RTC_FAST_CLK_SRC_LP_PLL_FREQ 8000000
```

相关声明：[ESP32_RTC_FAST_CLK_SRC_LP_PLL_FREQ](#aa01463cb65a93ac131d3a4213ee70991)。

低功耗锁相环时钟频率（LP PLL Clock Frequency）：8 MHz。

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

<a id="r_ad2816af571c412c39237c7e2f5f18c04"></a>

```c
#define ESP32_RTC_SLOW_CLK_SRC_RC32K 2
```

相关声明：[ESP32_RTC_SLOW_CLK_SRC_RC32K](#ad2816af571c412c39237c7e2f5f18c04)。

RTC 低速时钟源（Slow Clock Source）：32 kHz RC。

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

<a id="r_a3b18cdc509424e2249c7f4c3f1d93107"></a>

```c
#define ESP32_RTC_SLOW_CLK_SRC_RC32K_FREQ 32768
```

相关声明：[ESP32_RTC_SLOW_CLK_SRC_RC32K_FREQ](#a3b18cdc509424e2249c7f4c3f1d93107)。

32 kHz RC 时钟频率（Clock Frequency）。

<a id="r_a88ae2c1bafdc6e78258ada5cbb9368f9"></a>

```c
#define ESP32_TIMG0_MODULE 1
```

相关声明：[ESP32_TIMG0_MODULE](#a88ae2c1bafdc6e78258ada5cbb9368f9)。

定时器组 0（Timer Group 0）模块（Module）。

<a id="r_a251462caa49fc6fe0ae1c8fe99a87caa"></a>

```c
#define ESP32_TIMG1_MODULE 2
```

相关声明：[ESP32_TIMG1_MODULE](#a251462caa49fc6fe0ae1c8fe99a87caa)。

定时器组 1（Timer Group 1）模块（Module）。

<a id="r_aaf8e1de1e86906ba539863b9009ebe37"></a>

```c
#define ESP32_SYSTIMER_MODULE 3
```

相关声明：[ESP32_SYSTIMER_MODULE](#aaf8e1de1e86906ba539863b9009ebe37)。

系统定时器（System Timer）模块（Module）。

<a id="r_ac380a7ff843ee465763a355cb01ef295"></a>

```c
#define ESP32_MODULE_MAX 4
```

相关声明：[ESP32_MODULE_MAX](#ac380a7ff843ee465763a355cb01ef295)。

共享模块数量（Shared Module Count）。

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

<a id="r_a4ae4d6f5c7457a86f05e65f0c6b4984d"></a>

```c
#define ESP32_UART3_MODULE 104
```

相关声明：[ESP32_UART3_MODULE](#a4ae4d6f5c7457a86f05e65f0c6b4984d)。

UART3 模块（Module）。

<a id="r_adc5383d20b5f16b5468173be7ca8e83c"></a>

```c
#define ESP32_UART4_MODULE 105
```

相关声明：[ESP32_UART4_MODULE](#adc5383d20b5f16b5468173be7ca8e83c)。

UART4 模块（Module）。

<a id="r_afcf8170a750f4dc35326010b52f4e082"></a>

```c
#define ESP32_USB_MODULE 106
```

相关声明：[ESP32_USB_MODULE](#afcf8170a750f4dc35326010b52f4e082)。

USB模块（Module）。

<a id="r_a7331ffa2ec41896d05f1f86c4d30f758"></a>

```c
#define ESP32_I2C0_MODULE 107
```

相关声明：[ESP32_I2C0_MODULE](#a7331ffa2ec41896d05f1f86c4d30f758)。

I2C0模块（Module）。

<a id="r_a5068c510487e0ce3002e4bf7082601cd"></a>

```c
#define ESP32_I2C1_MODULE 108
```

相关声明：[ESP32_I2C1_MODULE](#a5068c510487e0ce3002e4bf7082601cd)。

I2C1模块（Module）。

<a id="r_a21c262b775f6d533621d4ba8e8d6c9aa"></a>

```c
#define ESP32_I2S0_MODULE 109
```

相关声明：[ESP32_I2S0_MODULE](#a21c262b775f6d533621d4ba8e8d6c9aa)。

I2S0模块（Module）。

<a id="r_a1cc05bfada949af9e9265abaadb1b6bc"></a>

```c
#define ESP32_I2S1_MODULE 110
```

相关声明：[ESP32_I2S1_MODULE](#a1cc05bfada949af9e9265abaadb1b6bc)。

I2S1模块（Module）。

<a id="r_a9d53e5b58186411179b621f19cb05e58"></a>

```c
#define ESP32_I2S2_MODULE 111
```

相关声明：[ESP32_I2S2_MODULE](#a9d53e5b58186411179b621f19cb05e58)。

I2S2 模块（Module）。

<a id="r_a4a2d8ca15cd619022c02f97842d54159"></a>

```c
#define ESP32_RMT_MODULE 112
```

相关声明：[ESP32_RMT_MODULE](#a4a2d8ca15cd619022c02f97842d54159)。

RMT模块（Module）。

<a id="r_ac0d8fb4397baaac7ff45dee8f4e1cb7c"></a>

```c
#define ESP32_PCNT_MODULE 113
```

相关声明：[ESP32_PCNT_MODULE](#ac0d8fb4397baaac7ff45dee8f4e1cb7c)。

PCNT模块（Module）。

<a id="r_a5e5283c23811e9c4f30980f1d865773b"></a>

```c
#define ESP32_SPI2_MODULE 114
```

相关声明：[ESP32_SPI2_MODULE](#a5e5283c23811e9c4f30980f1d865773b)。

SPI2模块（Module）。

<a id="r_aaaa2f3fbdc6e647799666e1885d4b4ff"></a>

```c
#define ESP32_SPI3_MODULE 115
```

相关声明：[ESP32_SPI3_MODULE](#aaaa2f3fbdc6e647799666e1885d4b4ff)。

SPI3模块（Module）。

<a id="r_ad6847f96f663ae04ca4d2c324b793d16"></a>

```c
#define ESP32_TWAI0_MODULE 116
```

相关声明：[ESP32_TWAI0_MODULE](#ad6847f96f663ae04ca4d2c324b793d16)。

TWAI0模块（Module）。

<a id="r_a0f0617f973ff3de27881f36957cd7cf2"></a>

```c
#define ESP32_TWAI1_MODULE 117
```

相关声明：[ESP32_TWAI1_MODULE](#a0f0617f973ff3de27881f36957cd7cf2)。

TWAI1模块（Module）。

<a id="r_ae0fa5212fce4504a30cb17a6d22abc94"></a>

```c
#define ESP32_TWAI2_MODULE 118
```

相关声明：[ESP32_TWAI2_MODULE](#ae0fa5212fce4504a30cb17a6d22abc94)。

TWAI2 模块（Module）。

<a id="r_ad5423ca02819aab6b3fe63c11b3cf998"></a>

```c
#define ESP32_RNG_MODULE 119
```

相关声明：[ESP32_RNG_MODULE](#ad5423ca02819aab6b3fe63c11b3cf998)。

RNG模块（Module）。

<a id="r_a701fec66fac239e66a19389ea153ff75"></a>

```c
#define ESP32_GDMA_MODULE 120
```

相关声明：[ESP32_GDMA_MODULE](#a701fec66fac239e66a19389ea153ff75)。

GDMA模块（Module）。

<a id="r_a13e722b2a08b3ea2da2ba3b40d794697"></a>

```c
#define ESP32_MCPWM0_MODULE 121
```

相关声明：[ESP32_MCPWM0_MODULE](#a13e722b2a08b3ea2da2ba3b40d794697)。

MCPWM0模块（Module）。

<a id="r_af85d74dfaeaa675aeb59443a93f69c98"></a>

```c
#define ESP32_MCPWM1_MODULE 122
```

相关声明：[ESP32_MCPWM1_MODULE](#af85d74dfaeaa675aeb59443a93f69c98)。

MCPWM1 模块（Module）。

<a id="r_a991c820648c7ef77b5aff2cecefee45d"></a>

```c
#define ESP32_ETM_MODULE 123
```

相关声明：[ESP32_ETM_MODULE](#a991c820648c7ef77b5aff2cecefee45d)。

ETM模块（Module）。

<a id="r_ada34a774bc3ec003c91cfe7c89939763"></a>

```c
#define ESP32_PARLIO_MODULE 124
```

相关声明：[ESP32_PARLIO_MODULE](#ada34a774bc3ec003c91cfe7c89939763)。

并行 I/O（Parallel IO）模块（Module）。

<a id="r_a488d6d32cf66e81a27f0999f837fe39a"></a>

```c
#define ESP32_TEMPSENSOR_MODULE 125
```

相关声明：[ESP32_TEMPSENSOR_MODULE](#a488d6d32cf66e81a27f0999f837fe39a)。

温度传感器（Temperature Sensor）模块（Module）。

<a id="r_abe244da38fbe794e93094feef9b188fe"></a>

```c
#define ESP32_SARADC_MODULE 126
```

相关声明：[ESP32_SARADC_MODULE](#abe244da38fbe794e93094feef9b188fe)。

SAR ADC模块（Module）。

<a id="r_a5261565b59c0a5b75794014b80692b33"></a>

```c
#define ESP32_RSA_MODULE 127
```

相关声明：[ESP32_RSA_MODULE](#a5261565b59c0a5b75794014b80692b33)。

RSA模块（Module）。

<a id="r_a290ac6ab6c5de2e8d84a911e389e1cfc"></a>

```c
#define ESP32_AES_MODULE 128
```

相关声明：[ESP32_AES_MODULE](#a290ac6ab6c5de2e8d84a911e389e1cfc)。

AES模块（Module）。

<a id="r_a683dd8814bf170018b63b57268c0fde9"></a>

```c
#define ESP32_SHA_MODULE 129
```

相关声明：[ESP32_SHA_MODULE](#a683dd8814bf170018b63b57268c0fde9)。

SHA模块（Module）。

<a id="r_a27bd450bf21c8b7502d1f32d9536129f"></a>

```c
#define ESP32_ECC_MODULE 130
```

相关声明：[ESP32_ECC_MODULE](#a27bd450bf21c8b7502d1f32d9536129f)。

ECC模块（Module）。

<a id="r_ae17c59442b576d1b9aade6019850e6f8"></a>

```c
#define ESP32_HMAC_MODULE 131
```

相关声明：[ESP32_HMAC_MODULE](#ae17c59442b576d1b9aade6019850e6f8)。

HMAC模块（Module）。

<a id="r_aaea0a7a0e789019e4ddfd38365e83688"></a>

```c
#define ESP32_DS_MODULE 132
```

相关声明：[ESP32_DS_MODULE](#aaea0a7a0e789019e4ddfd38365e83688)。

数字签名（Digital Signature）模块（Module）。

<a id="r_a4ff487b01c5240b09197ecf59d794975"></a>

```c
#define ESP32_ASSIST_DEBUG_MODULE 133
```

相关声明：[ESP32_ASSIST_DEBUG_MODULE](#a4ff487b01c5240b09197ecf59d794975)。

辅助调试（Assist Debug）模块（Module）。

<a id="r_a1360ddff70c3a29ce4a0b93199e4292e"></a>

```c
#define ESP32_EMAC_MODULE 134
```

相关声明：[ESP32_EMAC_MODULE](#a1360ddff70c3a29ce4a0b93199e4292e)。

以太网 MAC（Ethernet MAC） 模块（Module）。

<a id="r_a021a9bf63c87b8c6bd36378bca3e2198"></a>

```c
#define ESP32_USB_OTG_MODULE 135
```

相关声明：[ESP32_USB_OTG_MODULE](#a021a9bf63c87b8c6bd36378bca3e2198)。

USB OTG 模块（Module）。

<a id="r_a72052a75b3541623f59063260c4dbc32"></a>

```c
#define ESP32_SDMMC_MODULE 136
```

相关声明：[ESP32_SDMMC_MODULE](#a72052a75b3541623f59063260c4dbc32)。

SDMMC模块（Module）。

<a id="r_a5ccf92c28d468d746c24d34453ff1caa"></a>

```c
#define ESP32_LP_I2C0_MODULE 137
```

相关声明：[ESP32_LP_I2C0_MODULE](#a5ccf92c28d468d746c24d34453ff1caa)。

LP I2C0模块（Module）。

<a id="r_a4355b5840ff4f0c4940a713c06e46326"></a>

```c
#define ESP32_LP_UART0_MODULE 138
```

相关声明：[ESP32_LP_UART0_MODULE](#a4355b5840ff4f0c4940a713c06e46326)。

LP UART0模块（Module）。

<a id="r_ade9682150db421bc1c9f884868976e80"></a>

```c
#define ESP32_EMAC_PTP_MODULE 139
```

相关声明：[ESP32_EMAC_PTP_MODULE](#ade9682150db421bc1c9f884868976e80)。

以太网 MAC 精确时间协议参考时钟（Ethernet MAC PTP Reference Clock）。

## 9.2\_详细说明（Detailed Documentation）

<a id="a290ac6ab6c5de2e8d84a911e389e1cfc"></a>

### `ESP32_AES_MODULE`

```c
#define ESP32_AES_MODULE 128
```

AES模块（Module）。

<a id="a4ff487b01c5240b09197ecf59d794975"></a>

### `ESP32_ASSIST_DEBUG_MODULE`

```c
#define ESP32_ASSIST_DEBUG_MODULE 133
```

辅助调试（Assist Debug）模块（Module）。

<a id="a89f74c5aac4ea4279b158faa18825ddf"></a>

### `ESP32_CLK_CPU_PLL_100M`

```c
#define ESP32_CLK_CPU_PLL_100M 100000000
```

CPU 锁相环时钟（PLL Clock）：100 MHz。

<a id="a9233c5e62f6173181eec34e2690a4e6f"></a>

### `ESP32_CLK_CPU_PLL_200M`

```c
#define ESP32_CLK_CPU_PLL_200M 200000000
```

CPU 锁相环时钟（PLL Clock）：200 MHz。

<a id="af962d7c379ba6b7b7c5eed2b9370e3cb"></a>

### `ESP32_CLK_CPU_PLL_400M`

```c
#define ESP32_CLK_CPU_PLL_400M 400000000
```

CPU 锁相环时钟（PLL Clock）：400 MHz。

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

<a id="aaea0a7a0e789019e4ddfd38365e83688"></a>

### `ESP32_DS_MODULE`

```c
#define ESP32_DS_MODULE 132
```

数字签名（Digital Signature）模块（Module）。

<a id="a27bd450bf21c8b7502d1f32d9536129f"></a>

### `ESP32_ECC_MODULE`

```c
#define ESP32_ECC_MODULE 130
```

ECC模块（Module）。

<a id="a1360ddff70c3a29ce4a0b93199e4292e"></a>

### `ESP32_EMAC_MODULE`

```c
#define ESP32_EMAC_MODULE 134
```

以太网 MAC（Ethernet MAC） 模块（Module）。

<a id="ade9682150db421bc1c9f884868976e80"></a>

### `ESP32_EMAC_PTP_MODULE`

```c
#define ESP32_EMAC_PTP_MODULE 139
```

以太网 MAC 精确时间协议参考时钟（Ethernet MAC PTP Reference Clock）。

<a id="a991c820648c7ef77b5aff2cecefee45d"></a>

### `ESP32_ETM_MODULE`

```c
#define ESP32_ETM_MODULE 123
```

ETM模块（Module）。

<a id="a701fec66fac239e66a19389ea153ff75"></a>

### `ESP32_GDMA_MODULE`

```c
#define ESP32_GDMA_MODULE 120
```

GDMA模块（Module）。

<a id="ae17c59442b576d1b9aade6019850e6f8"></a>

### `ESP32_HMAC_MODULE`

```c
#define ESP32_HMAC_MODULE 131
```

HMAC模块（Module）。

<a id="a7331ffa2ec41896d05f1f86c4d30f758"></a>

### `ESP32_I2C0_MODULE`

```c
#define ESP32_I2C0_MODULE 107
```

I2C0模块（Module）。

<a id="a5068c510487e0ce3002e4bf7082601cd"></a>

### `ESP32_I2C1_MODULE`

```c
#define ESP32_I2C1_MODULE 108
```

I2C1模块（Module）。

<a id="a21c262b775f6d533621d4ba8e8d6c9aa"></a>

### `ESP32_I2S0_MODULE`

```c
#define ESP32_I2S0_MODULE 109
```

I2S0模块（Module）。

<a id="a1cc05bfada949af9e9265abaadb1b6bc"></a>

### `ESP32_I2S1_MODULE`

```c
#define ESP32_I2S1_MODULE 110
```

I2S1模块（Module）。

<a id="a9d53e5b58186411179b621f19cb05e58"></a>

### `ESP32_I2S2_MODULE`

```c
#define ESP32_I2S2_MODULE 111
```

I2S2 模块（Module）。

<a id="a60f4f5ee56d788f2161b52ebbc2aa510"></a>

### `ESP32_LEDC_MODULE`

```c
#define ESP32_LEDC_MODULE 100
```

LEDC模块（Module）。

<a id="a5ccf92c28d468d746c24d34453ff1caa"></a>

### `ESP32_LP_I2C0_MODULE`

```c
#define ESP32_LP_I2C0_MODULE 137
```

LP I2C0模块（Module）。

<a id="a4355b5840ff4f0c4940a713c06e46326"></a>

### `ESP32_LP_UART0_MODULE`

```c
#define ESP32_LP_UART0_MODULE 138
```

LP UART0模块（Module）。

<a id="a13e722b2a08b3ea2da2ba3b40d794697"></a>

### `ESP32_MCPWM0_MODULE`

```c
#define ESP32_MCPWM0_MODULE 121
```

MCPWM0模块（Module）。

<a id="af85d74dfaeaa675aeb59443a93f69c98"></a>

### `ESP32_MCPWM1_MODULE`

```c
#define ESP32_MCPWM1_MODULE 122
```

MCPWM1 模块（Module）。

<a id="ac380a7ff843ee465763a355cb01ef295"></a>

### `ESP32_MODULE_MAX`

```c
#define ESP32_MODULE_MAX 4
```

共享模块数量（Shared Module Count）。

<a id="ada34a774bc3ec003c91cfe7c89939763"></a>

### `ESP32_PARLIO_MODULE`

```c
#define ESP32_PARLIO_MODULE 124
```

并行 I/O（Parallel IO）模块（Module）。

<a id="ac0d8fb4397baaac7ff45dee8f4e1cb7c"></a>

### `ESP32_PCNT_MODULE`

```c
#define ESP32_PCNT_MODULE 113
```

PCNT模块（Module）。

<a id="a4a2d8ca15cd619022c02f97842d54159"></a>

### `ESP32_RMT_MODULE`

```c
#define ESP32_RMT_MODULE 112
```

RMT模块（Module）。

<a id="ad5423ca02819aab6b3fe63c11b3cf998"></a>

### `ESP32_RNG_MODULE`

```c
#define ESP32_RNG_MODULE 119
```

RNG模块（Module）。

<a id="a5261565b59c0a5b75794014b80692b33"></a>

### `ESP32_RSA_MODULE`

```c
#define ESP32_RSA_MODULE 127
```

RSA模块（Module）。

<a id="a7bd20a93e37b5b7b356058bdd878f181"></a>

### `ESP32_RTC_FAST_CLK_SRC_LP_PLL`

```c
#define ESP32_RTC_FAST_CLK_SRC_LP_PLL 2
```

RTC 高速时钟源（Fast Clock Source）：低功耗锁相环（LP PLL）。

<a id="aa01463cb65a93ac131d3a4213ee70991"></a>

### `ESP32_RTC_FAST_CLK_SRC_LP_PLL_FREQ`

```c
#define ESP32_RTC_FAST_CLK_SRC_LP_PLL_FREQ 8000000
```

低功耗锁相环时钟频率（LP PLL Clock Frequency）：8 MHz。

<a id="aae48d9f1288771e11c11d6177ecf3af7"></a>

### `ESP32_RTC_FAST_CLK_SRC_RC_FAST`

```c
#define ESP32_RTC_FAST_CLK_SRC_RC_FAST 0
```

RTC 高速时钟源（Fast Clock Source）：高速 RC（RC Fast）。

<a id="ae82f4db340753c2e771fad5184d83800"></a>

### `ESP32_RTC_FAST_CLK_SRC_XTAL`

```c
#define ESP32_RTC_FAST_CLK_SRC_XTAL 1
```

RTC 高速时钟源（Fast Clock Source）：晶体振荡器（XTAL）。

<a id="aa5d6a46de7da027832aa02489c062069"></a>

### `ESP32_RTC_SLOW_CLK_32K_EXT_OSC`

```c
#define ESP32_RTC_SLOW_CLK_32K_EXT_OSC 9
```

RTC 低速时钟源（Slow Clock Source）：外部 32 kHz 振荡器（External OSC）。

<a id="ad2816af571c412c39237c7e2f5f18c04"></a>

### `ESP32_RTC_SLOW_CLK_SRC_RC32K`

```c
#define ESP32_RTC_SLOW_CLK_SRC_RC32K 2
```

RTC 低速时钟源（Slow Clock Source）：32 kHz RC。

<a id="a3b18cdc509424e2249c7f4c3f1d93107"></a>

### `ESP32_RTC_SLOW_CLK_SRC_RC32K_FREQ`

```c
#define ESP32_RTC_SLOW_CLK_SRC_RC32K_FREQ 32768
```

32 kHz RC 时钟频率（Clock Frequency）。

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
#define ESP32_SARADC_MODULE 126
```

SAR ADC模块（Module）。

<a id="a72052a75b3541623f59063260c4dbc32"></a>

### `ESP32_SDMMC_MODULE`

```c
#define ESP32_SDMMC_MODULE 136
```

SDMMC模块（Module）。

<a id="a683dd8814bf170018b63b57268c0fde9"></a>

### `ESP32_SHA_MODULE`

```c
#define ESP32_SHA_MODULE 129
```

SHA模块（Module）。

<a id="a5e5283c23811e9c4f30980f1d865773b"></a>

### `ESP32_SPI2_MODULE`

```c
#define ESP32_SPI2_MODULE 114
```

SPI2模块（Module）。

<a id="aaaa2f3fbdc6e647799666e1885d4b4ff"></a>

### `ESP32_SPI3_MODULE`

```c
#define ESP32_SPI3_MODULE 115
```

SPI3模块（Module）。

<a id="aaf8e1de1e86906ba539863b9009ebe37"></a>

### `ESP32_SYSTIMER_MODULE`

```c
#define ESP32_SYSTIMER_MODULE 3
```

系统定时器（System Timer）模块（Module）。

<a id="a488d6d32cf66e81a27f0999f837fe39a"></a>

### `ESP32_TEMPSENSOR_MODULE`

```c
#define ESP32_TEMPSENSOR_MODULE 125
```

温度传感器（Temperature Sensor）模块（Module）。

<a id="a88ae2c1bafdc6e78258ada5cbb9368f9"></a>

### `ESP32_TIMG0_MODULE`

```c
#define ESP32_TIMG0_MODULE 1
```

定时器组 0（Timer Group 0）模块（Module）。

<a id="a251462caa49fc6fe0ae1c8fe99a87caa"></a>

### `ESP32_TIMG1_MODULE`

```c
#define ESP32_TIMG1_MODULE 2
```

定时器组 1（Timer Group 1）模块（Module）。

<a id="ad6847f96f663ae04ca4d2c324b793d16"></a>

### `ESP32_TWAI0_MODULE`

```c
#define ESP32_TWAI0_MODULE 116
```

TWAI0模块（Module）。

<a id="a0f0617f973ff3de27881f36957cd7cf2"></a>

### `ESP32_TWAI1_MODULE`

```c
#define ESP32_TWAI1_MODULE 117
```

TWAI1模块（Module）。

<a id="ae0fa5212fce4504a30cb17a6d22abc94"></a>

### `ESP32_TWAI2_MODULE`

```c
#define ESP32_TWAI2_MODULE 118
```

TWAI2 模块（Module）。

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

<a id="a4ae4d6f5c7457a86f05e65f0c6b4984d"></a>

### `ESP32_UART3_MODULE`

```c
#define ESP32_UART3_MODULE 104
```

UART3 模块（Module）。

<a id="adc5383d20b5f16b5468173be7ca8e83c"></a>

### `ESP32_UART4_MODULE`

```c
#define ESP32_UART4_MODULE 105
```

UART4 模块（Module）。

<a id="afcf8170a750f4dc35326010b52f4e082"></a>

### `ESP32_USB_MODULE`

```c
#define ESP32_USB_MODULE 106
```

USB模块（Module）。

<a id="a021a9bf63c87b8c6bd36378bca3e2198"></a>

### `ESP32_USB_OTG_MODULE`

```c
#define ESP32_USB_OTG_MODULE 135
```

USB OTG 模块（Module）。


## 9.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_transport_clock_reference/P014_esp32p4_clock.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P008_zephyr__dt-bindings__clock__esp32c5_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_zephyr__bluetooth__services__ets.h_文件参考.md)
