---
id: learning.zephyr-docs.api-memory-timer-topic-reference.page-4
title: EM32 时钟门控标识符（Clock Gating IDs）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__em32__clock__gating__ids.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_EM32 时钟门控标识符（Clock Gating IDs）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__em32__clock__gating__ids.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

EM32平台外设的时钟门控（Clock Gating）ID。

<a id="details"></a>

EM32 平台外设的时钟门控标识符（Clock Gating IDs）。这些标识符在设备树源文件（Device Tree Source，DTS）中使用，定义哪些外设启用时钟门控以进行电源管理。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.1\_宏定义（Macros）

<a id="r_gaa6631f5332e2cac5760d8777c926364b"></a>

```c
#define EM32_GATE_HCLKG_DMA 0x00
```

相关声明：[EM32_GATE_HCLKG_DMA](#gaa6631f5332e2cac5760d8777c926364b)。

DMA HCLK 门控标识符（Gating ID）。

<a id="r_ga09d0f8b523942e2853f231d0f3fd8a8a"></a>

```c
#define EM32_GATE_HCLKG_GPIOA 0x01
```

相关声明：[EM32_GATE_HCLKG_GPIOA](#ga09d0f8b523942e2853f231d0f3fd8a8a)。

GPIO 端口 A（Port A） HCLK 门控标识符（Gating ID）。

<a id="r_ga5dcefe39f8f0da9e2fc716eea9ad58b2"></a>

```c
#define EM32_GATE_HCLKG_GPIOB 0x02
```

相关声明：[EM32_GATE_HCLKG_GPIOB](#ga5dcefe39f8f0da9e2fc716eea9ad58b2)。

GPIO 端口 B（Port B） HCLK 门控标识符（Gating ID）。

<a id="r_gacb7d01c973b81acf0734a1ef780961d1"></a>

```c
#define EM32_GATE_HCLKG_7816_1 0x04
```

相关声明：[EM32_GATE_HCLKG_7816_1](#gacb7d01c973b81acf0734a1ef780961d1)。

ISO7816-1 接口（Interface） HCLK 门控标识符（Gating ID）。

<a id="r_gaa0ce3ed1baf733f7fe63ce51fa66f126"></a>

```c
#define EM32_GATE_HCLKG_7816_2 0x05
```

相关声明：[EM32_GATE_HCLKG_7816_2](#gaa0ce3ed1baf733f7fe63ce51fa66f126)。

ISO7816-2 接口（Interface） HCLK 门控标识符（Gating ID）。

<a id="r_gaea0609987f1ae855aae2c1a852dc3bc5"></a>

```c
#define EM32_GATE_HCLKG_ENCRYPT 0x06
```

相关声明：[EM32_GATE_HCLKG_ENCRYPT](#gaea0609987f1ae855aae2c1a852dc3bc5)。

加密引擎（Encryption Engine） HCLK 门控标识符（Gating ID）。

<a id="r_ga90173502b30d536cb9f63685e72da987"></a>

```c
#define EM32_GATE_HCLKG_ESPI1 0x0F
```

相关声明：[EM32_GATE_HCLKG_ESPI1](#ga90173502b30d536cb9f63685e72da987)。

eSPI 接口（Interface） HCLK 门控标识符（Gating ID）。

<a id="r_gaeaa8487d5abca96c392cdf4a0cc46882"></a>

```c
#define EM32_GATE_HCLKG_EXTSPI 0x1F
```

相关声明：[EM32_GATE_HCLKG_EXTSPI](#gaeaa8487d5abca96c392cdf4a0cc46882)。

外部 SPI 接口（External SPI Interface） HCLK 门控标识符（Gating ID）。

<a id="r_ga659b0100e1496fdd1dd61a607f4bfc73"></a>

```c
#define EM32_GATE_HCLKG_GHM_ACC1 0x20
```

相关声明：[EM32_GATE_HCLKG_GHM_ACC1](#ga659b0100e1496fdd1dd61a607f4bfc73)。

GHM 加速器 1（Accelerator 1） HCLK 门控标识符（Gating ID）。

<a id="r_gae8b5bb26c78af8c834aaabb7f435ecb9"></a>

```c
#define EM32_GATE_HCLKG_GHM_ACC2 0x21
```

相关声明：[EM32_GATE_HCLKG_GHM_ACC2](#gae8b5bb26c78af8c834aaabb7f435ecb9)。

GHM 加速器 2（Accelerator 2） HCLK 门控标识符（Gating ID）。

<a id="r_gabe926fcbadc439134e281868f076208f"></a>

```c
#define EM32_GATE_HCLKG_GHM_ACC3 0x22
```

相关声明：[EM32_GATE_HCLKG_GHM_ACC3](#gabe926fcbadc439134e281868f076208f)。

GHM 加速器 3（Accelerator 3） HCLK 门控标识符（Gating ID）。

<a id="r_gaf9d24e4ebbf04f2d8de1e834a2451d18"></a>

```c
#define EM32_GATE_HCLKF_GHM_IP 0x23
```

相关声明：[EM32_GATE_HCLKF_GHM_IP](#gaf9d24e4ebbf04f2d8de1e834a2451d18)。

GHM IP HCLKF 门控标识符（Gating ID）。

<a id="r_ga6475504e996a6dd301beefa223a14532"></a>

```c
#define EM32_GATE_HCLKF_FLASH_BIST 0x24
```

相关声明：[EM32_GATE_HCLKF_FLASH_BIST](#ga6475504e996a6dd301beefa223a14532)。

闪存内建自测试（Flash BIST） HCLKF 门控标识符（Gating ID）。

<a id="r_gab09517e1bc0cccaf6cd72341fa52d487"></a>

```c
#define EM32_GATE_HCLKF_GHM_RANSAC 0x25
```

相关声明：[EM32_GATE_HCLKF_GHM_RANSAC](#gab09517e1bc0cccaf6cd72341fa52d487)。

GHM RANSAC HCLKF 门控标识符（Gating ID）。

<a id="r_ga7b0b741948553a047da31238b18ff3a4"></a>

```c
#define EM32_GATE_HCLKF_SWSPI 0x26
```

相关声明：[EM32_GATE_HCLKF_SWSPI](#ga7b0b741948553a047da31238b18ff3a4)。

软件 SPI（Software SPI） HCLKF 门控标识符（Gating ID）。

<a id="r_ga0a07355dce535f249f3eba3d8d60ba5a"></a>

```c
#define EM32_GATE_HCLKF_GHM_DOUBLE 0x27
```

相关声明：[EM32_GATE_HCLKF_GHM_DOUBLE](#ga0a07355dce535f249f3eba3d8d60ba5a)。

GHM 双重处理（Double Processing） HCLKF 门控标识符（Gating ID）。

<a id="r_gae207bff319a29cb7533f50cfcc6f91f4"></a>

```c
#define EM32_GATE_HCLKF_GHM_DISTINGUISH 0x28
```

相关声明：[EM32_GATE_HCLKF_GHM_DISTINGUISH](#gae207bff319a29cb7533f50cfcc6f91f4)。

GHM 辨别（Distinguish） HCLKF 门控标识符（Gating ID）。

<a id="r_ga72cd668ff5fa65c79e745c961a1f6bbb"></a>

```c
#define EM32_GATE_HCLKF_GHM_LSE 0x29
```

相关声明：[EM32_GATE_HCLKF_GHM_LSE](#ga72cd668ff5fa65c79e745c961a1f6bbb)。

GHM 最小二乘估计（Least Squares Estimation） HCLKF 门控标识符（Gating ID）。

<a id="r_ga8b3a03e15a15572dcf74d814ae35c71b"></a>

```c
#define EM32_GATE_HCLKF_GHM_SAD 0x2A
```

相关声明：[EM32_GATE_HCLKF_GHM_SAD](#ga8b3a03e15a15572dcf74d814ae35c71b)。

GHM 绝对差之和（Sum of Absolute Differences） HCLKF 门控标识符（Gating ID）。

<a id="r_ga2f51d573ca1105d33c556207d6ce0803"></a>

```c
#define EM32_GATE_HCLKF_GHM_M2D 0x2B
```

相关声明：[EM32_GATE_HCLKF_GHM_M2D](#ga2f51d573ca1105d33c556207d6ce0803)。

GHM 运动到深度转换（Motion-to-Depth） HCLKF 门控标识符（Gating ID）。

<a id="r_ga0a7eadff118ba3bb0ebac94d6b6d101d"></a>

```c
#define EM32_GATE_PCLKG_LPC 0x03
```

相关声明：[EM32_GATE_PCLKG_LPC](#ga0a7eadff118ba3bb0ebac94d6b6d101d)。

LPC 控制器（Controller） PCLK 门控标识符（Gating ID）。

<a id="r_ga6df81c8b6f60db5caa7cf2bb32c0d88d"></a>

```c
#define EM32_GATE_PCLKG_USART 0x07
```

相关声明：[EM32_GATE_PCLKG_USART](#ga6df81c8b6f60db5caa7cf2bb32c0d88d)。

USART PCLK 门控标识符（Gating ID）。

<a id="r_ga946d4ccf991ff5c3241f49c134c51a02"></a>

```c
#define EM32_GATE_PCLKG_TMR1 0x08
```

相关声明：[EM32_GATE_PCLKG_TMR1](#ga946d4ccf991ff5c3241f49c134c51a02)。

定时器 1（Timer 1） PCLK 门控标识符（Gating ID）。

<a id="r_ga71cec22352a6a73a593f289d0d1bb595"></a>

```c
#define EM32_GATE_PCLKG_TMR2 0x09
```

相关声明：[EM32_GATE_PCLKG_TMR2](#ga71cec22352a6a73a593f289d0d1bb595)。

定时器 2（Timer 2） PCLK 门控标识符（Gating ID）。

<a id="r_ga6aac7561c106495f16cace7b35b70f8a"></a>

```c
#define EM32_GATE_PCLKG_TMR3 0x0A
```

相关声明：[EM32_GATE_PCLKG_TMR3](#ga6aac7561c106495f16cace7b35b70f8a)。

定时器 3（Timer 3） PCLK 门控标识符（Gating ID）。

<a id="r_ga94484d902adec94dc6b175dc73d5d9f4"></a>

```c
#define EM32_GATE_PCLKG_TMR4 0x0B
```

相关声明：[EM32_GATE_PCLKG_TMR4](#ga94484d902adec94dc6b175dc73d5d9f4)。

定时器 4（Timer 4） PCLK 门控标识符（Gating ID）。

<a id="r_ga6524b6025d755e09896719d8f273cac9"></a>

```c
#define EM32_GATE_PCLKG_UART1 0x0C
```

相关声明：[EM32_GATE_PCLKG_UART1](#ga6524b6025d755e09896719d8f273cac9)。

UART 1 PCLK 门控标识符（Gating ID）。

<a id="r_ga859496f4765125f857d5f626a6295abb"></a>

```c
#define EM32_GATE_PCLKG_UART2 0x0D
```

相关声明：[EM32_GATE_PCLKG_UART2](#ga859496f4765125f857d5f626a6295abb)。

UART 2 PCLK 门控标识符（Gating ID）。

<a id="r_ga479c87528d9893d8e208913b729b6479"></a>

```c
#define EM32_GATE_PCLKG_RVD1 0x0E
```

相关声明：[EM32_GATE_PCLKG_RVD1](#ga479c87528d9893d8e208913b729b6479)。

RVD 1 PCLK 门控标识符（Gating ID）。

<a id="r_ga7bead3cecf9953767cf63b41571025f1"></a>

```c
#define EM32_GATE_PCLKG_SSP2 0x10
```

相关声明：[EM32_GATE_PCLKG_SSP2](#ga7bead3cecf9953767cf63b41571025f1)。

SSP 2 PCLK 门控标识符（Gating ID）。

<a id="r_ga111f67b19af2726bedfab6424d9d3c9b"></a>

```c
#define EM32_GATE_PCLKG_I2C1 0x11
```

相关声明：[EM32_GATE_PCLKG_I2C1](#ga111f67b19af2726bedfab6424d9d3c9b)。

I2C 1 PCLK 门控标识符（Gating ID）。

<a id="r_gaec3c910d11156e9176a927f71557c4cb"></a>

```c
#define EM32_GATE_PCLKG_I2C2 0x12
```

相关声明：[EM32_GATE_PCLKG_I2C2](#gaec3c910d11156e9176a927f71557c4cb)。

I2C 2 PCLK 门控标识符（Gating ID）。

<a id="r_ga50d66a8e2f5248a9e26a4658a1c22fd5"></a>

```c
#define EM32_GATE_PCLKG_PWM 0x13
```

相关声明：[EM32_GATE_PCLKG_PWM](#ga50d66a8e2f5248a9e26a4658a1c22fd5)。

PWM PCLK 门控标识符（Gating ID）。

<a id="r_ga265b1ab300137258bc79f64b4896f455"></a>

```c
#define EM32_GATE_PCLKG_RVD2 0x14
```

相关声明：[EM32_GATE_PCLKG_RVD2](#ga265b1ab300137258bc79f64b4896f455)。

RVD 2 PCLK 门控标识符（Gating ID）。

<a id="r_ga93771066e451b1742d909432524c389e"></a>

```c
#define EM32_GATE_PCLKG_UDC 0x15
```

相关声明：[EM32_GATE_PCLKG_UDC](#ga93771066e451b1742d909432524c389e)。

USB 设备控制器（Device Controller） PCLK 门控标识符（Gating ID）。

<a id="r_ga5b7ad8552dbb1211e1bab8f11a4dd4ad"></a>

```c
#define EM32_GATE_PCLKG_ATRIM 0x16
```

相关声明：[EM32_GATE_PCLKG_ATRIM](#ga5b7ad8552dbb1211e1bab8f11a4dd4ad)。

模拟微调（Analog Trim） PCLK 门控标识符（Gating ID）。

<a id="r_gaf8a3a28717a159099be2659e23c1838b"></a>

```c
#define EM32_GATE_PCLKG_RTC 0x17
```

相关声明：[EM32_GATE_PCLKG_RTC](#gaf8a3a28717a159099be2659e23c1838b)。

RTC PCLK 门控标识符（Gating ID）。

<a id="r_ga1b0fee9bf270af13db52660cef00573a"></a>

```c
#define EM32_GATE_PCLKG_BKP 0x18
```

相关声明：[EM32_GATE_PCLKG_BKP](#ga1b0fee9bf270af13db52660cef00573a)。

备份寄存器（Backup Register） PCLK 门控标识符（Gating ID）。

<a id="r_ga108ab488de4442ca2bdb769babc69eb8"></a>

```c
#define EM32_GATE_PCLKG_DWG 0x19
```

相关声明：[EM32_GATE_PCLKG_DWG](#ga108ab488de4442ca2bdb769babc69eb8)。

调试／看门狗（Debug/Watch Dog） PCLK 门控标识符（Gating ID）。

<a id="r_gabc45b2128f782d088d375d16c23512a7"></a>

```c
#define EM32_GATE_PCLKG_PWR 0x1A
```

相关声明：[EM32_GATE_PCLKG_PWR](#gabc45b2128f782d088d375d16c23512a7)。

电源管理（Power Management） PCLK 门控标识符（Gating ID）。

<a id="r_ga8919e9519dab18241e48deaae5a6c61c"></a>

```c
#define EM32_GATE_PCLKG_CACHE 0x1B
```

相关声明：[EM32_GATE_PCLKG_CACHE](#ga8919e9519dab18241e48deaae5a6c61c)。

缓存控制器（Cache Controller） PCLK 门控标识符（Gating ID）。

<a id="r_ga841ce937ed11889d86a908d96be053a9"></a>

```c
#define EM32_GATE_PCLKG_AIP 0x1C
```

相关声明：[EM32_GATE_PCLKG_AIP](#ga841ce937ed11889d86a908d96be053a9)。

AES IP PCLK 门控标识符（Gating ID）。

<a id="r_ga93b783902cfc53c33aece4aa9e446d7b"></a>

```c
#define EM32_GATE_PCLKG_ECC 0x1D
```

相关声明：[EM32_GATE_PCLKG_ECC](#ga93b783902cfc53c33aece4aa9e446d7b)。

ECC 引擎（Engine） PCLK 门控标识符（Gating ID）。

<a id="r_ga6e71986c6ee72e432e0f68077dd4592c"></a>

```c
#define EM32_GATE_PCLKG_TRNG 0x1E
```

相关声明：[EM32_GATE_PCLKG_TRNG](#ga6e71986c6ee72e432e0f68077dd4592c)。

TRNG PCLK 门控标识符（Gating ID）。

<a id="r_gab05ef71cc11a805f67da48c37c1541e1"></a>

```c
#define EM32_GATE_PCLKG_SSP1 0x30
```

相关声明：[EM32_GATE_PCLKG_SSP1](#gab05ef71cc11a805f67da48c37c1541e1)。

SSP 1 PCLK 门控标识符（Gating ID）。

<a id="r_gacf5bbd55b9045e9b88b5cb828e94ab3d"></a>

```c
#define EM32_GATE_NONE 0xFFFE
```

相关声明：[EM32_GATE_NONE](#gacf5bbd55b9045e9b88b5cb828e94ab3d)。

不进行时钟门控（Clock Gating），标识符无效或保留（Invalid/Reserved ID）。

<a id="r_ga6be245738976727a76be9fbf03151372"></a>

```c
#define EM32_GATE_PCLKG_ALL 0xFFFF
```

相关声明：[EM32_GATE_PCLKG_ALL](#ga6be245738976727a76be9fbf03151372)。

启用全部外设 PCLK 门控（Peripheral PCLK Gates）。

## 4.2\_详细说明（Detailed Documentation）

<a id="ga6475504e996a6dd301beefa223a14532"></a>

### `EM32_GATE_HCLKF_FLASH_BIST`

```c
#define EM32_GATE_HCLKF_FLASH_BIST 0x24
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

闪存内建自测试（Flash BIST） HCLKF 门控标识符（Gating ID）。

<a id="gae207bff319a29cb7533f50cfcc6f91f4"></a>

### `EM32_GATE_HCLKF_GHM_DISTINGUISH`

```c
#define EM32_GATE_HCLKF_GHM_DISTINGUISH 0x28
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

GHM 辨别（Distinguish） HCLKF 门控标识符（Gating ID）。

<a id="ga0a07355dce535f249f3eba3d8d60ba5a"></a>

### `EM32_GATE_HCLKF_GHM_DOUBLE`

```c
#define EM32_GATE_HCLKF_GHM_DOUBLE 0x27
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

GHM 双重处理（Double Processing） HCLKF 门控标识符（Gating ID）。

<a id="gaf9d24e4ebbf04f2d8de1e834a2451d18"></a>

### `EM32_GATE_HCLKF_GHM_IP`

```c
#define EM32_GATE_HCLKF_GHM_IP 0x23
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

GHM IP HCLKF 门控标识符（Gating ID）。

<a id="ga72cd668ff5fa65c79e745c961a1f6bbb"></a>

### `EM32_GATE_HCLKF_GHM_LSE`

```c
#define EM32_GATE_HCLKF_GHM_LSE 0x29
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

GHM 最小二乘估计（Least Squares Estimation） HCLKF 门控标识符（Gating ID）。

<a id="ga2f51d573ca1105d33c556207d6ce0803"></a>

### `EM32_GATE_HCLKF_GHM_M2D`

```c
#define EM32_GATE_HCLKF_GHM_M2D 0x2B
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

GHM 运动到深度转换（Motion-to-Depth） HCLKF 门控标识符（Gating ID）。

<a id="gab09517e1bc0cccaf6cd72341fa52d487"></a>

### `EM32_GATE_HCLKF_GHM_RANSAC`

```c
#define EM32_GATE_HCLKF_GHM_RANSAC 0x25
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

GHM RANSAC HCLKF 门控标识符（Gating ID）。

<a id="ga8b3a03e15a15572dcf74d814ae35c71b"></a>

### `EM32_GATE_HCLKF_GHM_SAD`

```c
#define EM32_GATE_HCLKF_GHM_SAD 0x2A
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

GHM 绝对差之和（Sum of Absolute Differences） HCLKF 门控标识符（Gating ID）。

<a id="ga7b0b741948553a047da31238b18ff3a4"></a>

### `EM32_GATE_HCLKF_SWSPI`

```c
#define EM32_GATE_HCLKF_SWSPI 0x26
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

软件 SPI（Software SPI） HCLKF 门控标识符（Gating ID）。

<a id="gacb7d01c973b81acf0734a1ef780961d1"></a>

### `EM32_GATE_HCLKG_7816_1`

```c
#define EM32_GATE_HCLKG_7816_1 0x04
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

ISO7816-1 接口（Interface） HCLK 门控标识符（Gating ID）。

<a id="gaa0ce3ed1baf733f7fe63ce51fa66f126"></a>

### `EM32_GATE_HCLKG_7816_2`

```c
#define EM32_GATE_HCLKG_7816_2 0x05
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

ISO7816-2 接口（Interface） HCLK 门控标识符（Gating ID）。

<a id="gaa6631f5332e2cac5760d8777c926364b"></a>

### `EM32_GATE_HCLKG_DMA`

```c
#define EM32_GATE_HCLKG_DMA 0x00
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

DMA HCLK 门控标识符（Gating ID）。

<a id="gaea0609987f1ae855aae2c1a852dc3bc5"></a>

### `EM32_GATE_HCLKG_ENCRYPT`

```c
#define EM32_GATE_HCLKG_ENCRYPT 0x06
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

加密引擎（Encryption Engine） HCLK 门控标识符（Gating ID）。

<a id="ga90173502b30d536cb9f63685e72da987"></a>

### `EM32_GATE_HCLKG_ESPI1`

```c
#define EM32_GATE_HCLKG_ESPI1 0x0F
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

eSPI 接口（Interface） HCLK 门控标识符（Gating ID）。

<a id="gaeaa8487d5abca96c392cdf4a0cc46882"></a>

### `EM32_GATE_HCLKG_EXTSPI`

```c
#define EM32_GATE_HCLKG_EXTSPI 0x1F
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

外部 SPI 接口（External SPI Interface） HCLK 门控标识符（Gating ID）。

<a id="ga659b0100e1496fdd1dd61a607f4bfc73"></a>

### `EM32_GATE_HCLKG_GHM_ACC1`

```c
#define EM32_GATE_HCLKG_GHM_ACC1 0x20
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

GHM 加速器 1（Accelerator 1） HCLK 门控标识符（Gating ID）。

<a id="gae8b5bb26c78af8c834aaabb7f435ecb9"></a>

### `EM32_GATE_HCLKG_GHM_ACC2`

```c
#define EM32_GATE_HCLKG_GHM_ACC2 0x21
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

GHM 加速器 2（Accelerator 2） HCLK 门控标识符（Gating ID）。

<a id="gabe926fcbadc439134e281868f076208f"></a>

### `EM32_GATE_HCLKG_GHM_ACC3`

```c
#define EM32_GATE_HCLKG_GHM_ACC3 0x22
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

GHM 加速器 3（Accelerator 3） HCLK 门控标识符（Gating ID）。

<a id="ga09d0f8b523942e2853f231d0f3fd8a8a"></a>

### `EM32_GATE_HCLKG_GPIOA`

```c
#define EM32_GATE_HCLKG_GPIOA 0x01
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

GPIO 端口 A（Port A） HCLK 门控标识符（Gating ID）。

<a id="ga5dcefe39f8f0da9e2fc716eea9ad58b2"></a>

### `EM32_GATE_HCLKG_GPIOB`

```c
#define EM32_GATE_HCLKG_GPIOB 0x02
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

GPIO 端口 B（Port B） HCLK 门控标识符（Gating ID）。

<a id="gacf5bbd55b9045e9b88b5cb828e94ab3d"></a>

### `EM32_GATE_NONE`

```c
#define EM32_GATE_NONE 0xFFFE
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

不进行时钟门控（Clock Gating），标识符无效或保留（Invalid/Reserved ID）。

<a id="ga841ce937ed11889d86a908d96be053a9"></a>

### `EM32_GATE_PCLKG_AIP`

```c
#define EM32_GATE_PCLKG_AIP 0x1C
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

AES IP PCLK 门控标识符（Gating ID）。

<a id="ga6be245738976727a76be9fbf03151372"></a>

### `EM32_GATE_PCLKG_ALL`

```c
#define EM32_GATE_PCLKG_ALL 0xFFFF
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

启用全部外设 PCLK 门控（Peripheral PCLK Gates）。

<a id="ga5b7ad8552dbb1211e1bab8f11a4dd4ad"></a>

### `EM32_GATE_PCLKG_ATRIM`

```c
#define EM32_GATE_PCLKG_ATRIM 0x16
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

模拟微调（Analog Trim） PCLK 门控标识符（Gating ID）。

<a id="ga1b0fee9bf270af13db52660cef00573a"></a>

### `EM32_GATE_PCLKG_BKP`

```c
#define EM32_GATE_PCLKG_BKP 0x18
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

备份寄存器（Backup Register） PCLK 门控标识符（Gating ID）。

<a id="ga8919e9519dab18241e48deaae5a6c61c"></a>

### `EM32_GATE_PCLKG_CACHE`

```c
#define EM32_GATE_PCLKG_CACHE 0x1B
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

缓存控制器（Cache Controller） PCLK 门控标识符（Gating ID）。

<a id="ga108ab488de4442ca2bdb769babc69eb8"></a>

### `EM32_GATE_PCLKG_DWG`

```c
#define EM32_GATE_PCLKG_DWG 0x19
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

调试／看门狗（Debug/Watch Dog） PCLK 门控标识符（Gating ID）。

<a id="ga93b783902cfc53c33aece4aa9e446d7b"></a>

### `EM32_GATE_PCLKG_ECC`

```c
#define EM32_GATE_PCLKG_ECC 0x1D
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

ECC 引擎（Engine） PCLK 门控标识符（Gating ID）。

<a id="ga111f67b19af2726bedfab6424d9d3c9b"></a>

### `EM32_GATE_PCLKG_I2C1`

```c
#define EM32_GATE_PCLKG_I2C1 0x11
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

I2C 1 PCLK 门控标识符（Gating ID）。

<a id="gaec3c910d11156e9176a927f71557c4cb"></a>

### `EM32_GATE_PCLKG_I2C2`

```c
#define EM32_GATE_PCLKG_I2C2 0x12
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

I2C 2 PCLK 门控标识符（Gating ID）。

<a id="ga0a7eadff118ba3bb0ebac94d6b6d101d"></a>

### `EM32_GATE_PCLKG_LPC`

```c
#define EM32_GATE_PCLKG_LPC 0x03
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

LPC 控制器（Controller） PCLK 门控标识符（Gating ID）。

<a id="ga50d66a8e2f5248a9e26a4658a1c22fd5"></a>

### `EM32_GATE_PCLKG_PWM`

```c
#define EM32_GATE_PCLKG_PWM 0x13
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

PWM PCLK 门控标识符（Gating ID）。

<a id="gabc45b2128f782d088d375d16c23512a7"></a>

### `EM32_GATE_PCLKG_PWR`

```c
#define EM32_GATE_PCLKG_PWR 0x1A
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

电源管理（Power Management） PCLK 门控标识符（Gating ID）。

<a id="gaf8a3a28717a159099be2659e23c1838b"></a>

### `EM32_GATE_PCLKG_RTC`

```c
#define EM32_GATE_PCLKG_RTC 0x17
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

RTC PCLK 门控标识符（Gating ID）。

<a id="ga479c87528d9893d8e208913b729b6479"></a>

### `EM32_GATE_PCLKG_RVD1`

```c
#define EM32_GATE_PCLKG_RVD1 0x0E
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

RVD 1 PCLK 门控标识符（Gating ID）。

<a id="ga265b1ab300137258bc79f64b4896f455"></a>

### `EM32_GATE_PCLKG_RVD2`

```c
#define EM32_GATE_PCLKG_RVD2 0x14
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

RVD 2 PCLK 门控标识符（Gating ID）。

<a id="gab05ef71cc11a805f67da48c37c1541e1"></a>

### `EM32_GATE_PCLKG_SSP1`

```c
#define EM32_GATE_PCLKG_SSP1 0x30
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

SSP 1 PCLK 门控标识符（Gating ID）。

<a id="ga7bead3cecf9953767cf63b41571025f1"></a>

### `EM32_GATE_PCLKG_SSP2`

```c
#define EM32_GATE_PCLKG_SSP2 0x10
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

SSP 2 PCLK 门控标识符（Gating ID）。

<a id="ga946d4ccf991ff5c3241f49c134c51a02"></a>

### `EM32_GATE_PCLKG_TMR1`

```c
#define EM32_GATE_PCLKG_TMR1 0x08
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

定时器 1（Timer 1） PCLK 门控标识符（Gating ID）。

<a id="ga71cec22352a6a73a593f289d0d1bb595"></a>

### `EM32_GATE_PCLKG_TMR2`

```c
#define EM32_GATE_PCLKG_TMR2 0x09
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

定时器 2（Timer 2） PCLK 门控标识符（Gating ID）。

<a id="ga6aac7561c106495f16cace7b35b70f8a"></a>

### `EM32_GATE_PCLKG_TMR3`

```c
#define EM32_GATE_PCLKG_TMR3 0x0A
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

定时器 3（Timer 3） PCLK 门控标识符（Gating ID）。

<a id="ga94484d902adec94dc6b175dc73d5d9f4"></a>

### `EM32_GATE_PCLKG_TMR4`

```c
#define EM32_GATE_PCLKG_TMR4 0x0B
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

定时器 4（Timer 4） PCLK 门控标识符（Gating ID）。

<a id="ga6e71986c6ee72e432e0f68077dd4592c"></a>

### `EM32_GATE_PCLKG_TRNG`

```c
#define EM32_GATE_PCLKG_TRNG 0x1E
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

TRNG PCLK 门控标识符（Gating ID）。

<a id="ga6524b6025d755e09896719d8f273cac9"></a>

### `EM32_GATE_PCLKG_UART1`

```c
#define EM32_GATE_PCLKG_UART1 0x0C
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

UART 1 PCLK 门控标识符（Gating ID）。

<a id="ga859496f4765125f857d5f626a6295abb"></a>

### `EM32_GATE_PCLKG_UART2`

```c
#define EM32_GATE_PCLKG_UART2 0x0D
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

UART 2 PCLK 门控标识符（Gating ID）。

<a id="ga93771066e451b1742d909432524c389e"></a>

### `EM32_GATE_PCLKG_UDC`

```c
#define EM32_GATE_PCLKG_UDC 0x15
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

USB 设备控制器（Device Controller） PCLK 门控标识符（Gating ID）。

<a id="ga6df81c8b6f60db5caa7cf2bb32c0d88d"></a>

### `EM32_GATE_PCLKG_USART`

```c
#define EM32_GATE_PCLKG_USART 0x07
```

```c
#include <zephyr/dt-bindings/clock/em32_clock.h>
```

USART PCLK 门控标识符（Gating ID）。


## 4.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/clock/em32_clock.h](../api_file_audio_test_reference/P006_zephyr__dt-bindings__clock__em32_clock.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md) · [返回大纲](大纲.md) · [下一章](P005_MAX32664C API主题.md)
