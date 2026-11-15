---
id: learning.zephyr-docs.api-file-audio-gateway-reference.page-16
title: zephyr__dt-bindings__reset__gd32c2x1.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gd32c2x1_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_zephyr\_\_dt-bindings\_\_reset\_\_gd32c2x1.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gd32c2x1_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

GD32C2X1设备树绑定（Device Tree Bindings）的复位控制器定义。

<a id="details"></a>

```c
#include "gd32-common.h"
```

查看此文件的源码。

GD32C2X1设备树绑定（Device Tree Bindings）的复位控制器定义。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 16.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 寄存器偏移量（Register offsets）

<a id="r_a4f5347051ef3b9897ce80d198ebe69ff"></a>

```c
#define GD32_AHB1RST_OFFSET 0x10U
```

相关声明：[GD32_AHB1RST_OFFSET](#a4f5347051ef3b9897ce80d198ebe69ff)。

AHB1 外设复位寄存器偏移量（Peripheral Reset Register Offset）。

<a id="r_a8146ab0bff8395c1ae44f72bcac06f60"></a>

```c
#define GD32_AHB2RST_OFFSET 0x14U
```

相关声明：[GD32_AHB2RST_OFFSET](#a8146ab0bff8395c1ae44f72bcac06f60)。

AHB2 外设复位寄存器偏移量（Peripheral Reset Register Offset）。

<a id="r_a156f3e3c31b03c81f225cb9c3cab9a45"></a>

```c
#define GD32_APBRST_OFFSET 0x24U
```

相关声明：[GD32_APBRST_OFFSET](#a156f3e3c31b03c81f225cb9c3cab9a45)。

APB 外设复位寄存器偏移量（Peripheral Reset Register Offset）。

<a id="define-members-1"></a>

### 外设复位定义（Reset Definitions for Peripherals）

<a id="r_af47b6e0af43b63f4ee07bafa70290a38"></a>

```c
#define GD32_RESET_CRC GD32_RESET_CONFIG(AHB1RST, 12U)
```

相关声明：[GD32_RESET_CRC](#af47b6e0af43b63f4ee07bafa70290a38)。

CRC 复位（Reset）。

<a id="r_af57270b020dc88eff8b6a1ef7fac10ff"></a>

```c
#define GD32_RESET_DMA GD32_RESET_CONFIG(AHB1RST, 21U)
```

相关声明：[GD32_RESET_DMA](#af57270b020dc88eff8b6a1ef7fac10ff)。

DMA 复位（Reset）。

<a id="r_a3757cebbf6f3557b95ad38f58eeeec6f"></a>

```c
#define GD32_RESET_GPIOA GD32_RESET_CONFIG(AHB2RST, 17U)
```

相关声明：[GD32_RESET_GPIOA](#a3757cebbf6f3557b95ad38f58eeeec6f)。

GPIOA 复位（Reset）。

<a id="r_af5961280a760bba841a7d9f2ba1b4e2f"></a>

```c
#define GD32_RESET_GPIOB GD32_RESET_CONFIG(AHB2RST, 18U)
```

相关声明：[GD32_RESET_GPIOB](#af5961280a760bba841a7d9f2ba1b4e2f)。

GPIOB 复位（Reset）。

<a id="r_a5a20c0f1febc4709b3038cb0c5ef55bc"></a>

```c
#define GD32_RESET_GPIOC GD32_RESET_CONFIG(AHB2RST, 19U)
```

相关声明：[GD32_RESET_GPIOC](#a5a20c0f1febc4709b3038cb0c5ef55bc)。

GPIOC 复位（Reset）。

<a id="r_ab9da13b274d377bdce3b3cce159c0cd4"></a>

```c
#define GD32_RESET_GPIOD GD32_RESET_CONFIG(AHB2RST, 20U)
```

相关声明：[GD32_RESET_GPIOD](#ab9da13b274d377bdce3b3cce159c0cd4)。

GPIOD 复位（Reset）。

<a id="r_a8cac628be929c7303ca2017b0e2a2798"></a>

```c
#define GD32_RESET_GPIOF GD32_RESET_CONFIG(AHB2RST, 22U)
```

相关声明：[GD32_RESET_GPIOF](#a8cac628be929c7303ca2017b0e2a2798)。

GPIOF 复位（Reset）。

<a id="r_afd91e374f836fdf42970966e9d4677c4"></a>

```c
#define GD32_RESET_SYSCFG GD32_RESET_CONFIG(APBRST, 0U)
```

相关声明：[GD32_RESET_SYSCFG](#afd91e374f836fdf42970966e9d4677c4)。

SYSCFG 复位（Reset）。

<a id="r_a492c3d07d5e6280710cefe442cb0d951"></a>

```c
#define GD32_RESET_CMP GD32_RESET_CONFIG(APBRST, 1U)
```

相关声明：[GD32_RESET_CMP](#a492c3d07d5e6280710cefe442cb0d951)。

比较器复位（Comparator Reset）。

<a id="r_a8aac1c0ab090d8568076f6d8556e5c7a"></a>

```c
#define GD32_RESET_WWDGT GD32_RESET_CONFIG(APBRST, 8U)
```

相关声明：[GD32_RESET_WWDGT](#a8aac1c0ab090d8568076f6d8556e5c7a)。

窗口看门狗复位（Window Watchdog Reset）。

<a id="r_aec7a7c37bfacf340a8e73b4f63d9bb8f"></a>

```c
#define GD32_RESET_ADC GD32_RESET_CONFIG(APBRST, 9U)
```

相关声明：[GD32_RESET_ADC](#aec7a7c37bfacf340a8e73b4f63d9bb8f)。

ADC 复位（Reset）。

<a id="r_a2a7fd67d22598a774386a49ded2a9c72"></a>

```c
#define GD32_RESET_TIMER0 GD32_RESET_CONFIG(APBRST, 10U)
```

相关声明：[GD32_RESET_TIMER0](#a2a7fd67d22598a774386a49ded2a9c72)。

TIMER0 复位（Reset）。

<a id="r_a113cfc98af5cb46151d0545cf54fe5aa"></a>

```c
#define GD32_RESET_TIMER2 GD32_RESET_CONFIG(APBRST, 11U)
```

相关声明：[GD32_RESET_TIMER2](#a113cfc98af5cb46151d0545cf54fe5aa)。

TIMER2 复位（Reset）。

<a id="r_a64f740c7f65d696deb5f617654be9c5d"></a>

```c
#define GD32_RESET_SPI0 GD32_RESET_CONFIG(APBRST, 12U)
```

相关声明：[GD32_RESET_SPI0](#a64f740c7f65d696deb5f617654be9c5d)。

SPI0 复位（Reset）。

<a id="r_a27ae8979a4889e95867ed833d9843d07"></a>

```c
#define GD32_RESET_SPI1 GD32_RESET_CONFIG(APBRST, 13U)
```

相关声明：[GD32_RESET_SPI1](#a27ae8979a4889e95867ed833d9843d07)。

SPI1 复位（Reset）。

<a id="r_a6a03a7368d1e153ddf89547962711d35"></a>

```c
#define GD32_RESET_USART0 GD32_RESET_CONFIG(APBRST, 14U)
```

相关声明：[GD32_RESET_USART0](#a6a03a7368d1e153ddf89547962711d35)。

USART0 复位（Reset）。

<a id="r_aeb24e0ab9ae6be1c82593220c9719117"></a>

```c
#define GD32_RESET_USART1 GD32_RESET_CONFIG(APBRST, 15U)
```

相关声明：[GD32_RESET_USART1](#aeb24e0ab9ae6be1c82593220c9719117)。

USART1 复位（Reset）。

<a id="r_a012ec5ec4ff3dca4b788f9839be1c2f6"></a>

```c
#define GD32_RESET_TIMER13 GD32_RESET_CONFIG(APBRST, 16U)
```

相关声明：[GD32_RESET_TIMER13](#a012ec5ec4ff3dca4b788f9839be1c2f6)。

TIMER13 复位（Reset）。

<a id="r_ae1f1c4a1aa517935b9f76bc136a76809"></a>

```c
#define GD32_RESET_TIMER15 GD32_RESET_CONFIG(APBRST, 17U)
```

相关声明：[GD32_RESET_TIMER15](#ae1f1c4a1aa517935b9f76bc136a76809)。

TIMER15 复位（Reset）。

<a id="r_afe50a4990f8267250bd0b454ddfe2b73"></a>

```c
#define GD32_RESET_TIMER16 GD32_RESET_CONFIG(APBRST, 18U)
```

相关声明：[GD32_RESET_TIMER16](#afe50a4990f8267250bd0b454ddfe2b73)。

TIMER16 复位（Reset）。

<a id="r_a362e90b2303107bd5ec1cd57662e986a"></a>

```c
#define GD32_RESET_USART2 GD32_RESET_CONFIG(APBRST, 19U)
```

相关声明：[GD32_RESET_USART2](#a362e90b2303107bd5ec1cd57662e986a)。

USART2 复位（Reset）。

<a id="r_a12b532298a73feed3aa42ad53cf6ca79"></a>

```c
#define GD32_RESET_I2C0 GD32_RESET_CONFIG(APBRST, 21U)
```

相关声明：[GD32_RESET_I2C0](#a12b532298a73feed3aa42ad53cf6ca79)。

I2C0 复位（Reset）。

<a id="r_a9b9bec0c724fce490ba57090fe5329cc"></a>

```c
#define GD32_RESET_I2C1 GD32_RESET_CONFIG(APBRST, 22U)
```

相关声明：[GD32_RESET_I2C1](#a9b9bec0c724fce490ba57090fe5329cc)。

I2C1 复位（Reset）。

<a id="r_a02b6250ebdbfa5de5f39f49c6d81f1ef"></a>

```c
#define GD32_RESET_PMU GD32_RESET_CONFIG(APBRST, 28U)
```

相关声明：[GD32_RESET_PMU](#a02b6250ebdbfa5de5f39f49c6d81f1ef)。

PMU 复位（Reset）。

## 16.2\_详细说明（Detailed Documentation）

<a id="a4f5347051ef3b9897ce80d198ebe69ff"></a>

### `GD32_AHB1RST_OFFSET`

```c
#define GD32_AHB1RST_OFFSET 0x10U
```

AHB1 外设复位寄存器偏移量（Peripheral Reset Register Offset）。

<a id="a8146ab0bff8395c1ae44f72bcac06f60"></a>

### `GD32_AHB2RST_OFFSET`

```c
#define GD32_AHB2RST_OFFSET 0x14U
```

AHB2 外设复位寄存器偏移量（Peripheral Reset Register Offset）。

<a id="a156f3e3c31b03c81f225cb9c3cab9a45"></a>

### `GD32_APBRST_OFFSET`

```c
#define GD32_APBRST_OFFSET 0x24U
```

APB 外设复位寄存器偏移量（Peripheral Reset Register Offset）。

<a id="aec7a7c37bfacf340a8e73b4f63d9bb8f"></a>

### `GD32_RESET_ADC`

```c
#define GD32_RESET_ADC GD32_RESET_CONFIG(APBRST, 9U)
```

ADC 复位（Reset）。

<a id="a492c3d07d5e6280710cefe442cb0d951"></a>

### `GD32_RESET_CMP`

```c
#define GD32_RESET_CMP GD32_RESET_CONFIG(APBRST, 1U)
```

比较器复位（Comparator Reset）。

<a id="af47b6e0af43b63f4ee07bafa70290a38"></a>

### `GD32_RESET_CRC`

```c
#define GD32_RESET_CRC GD32_RESET_CONFIG(AHB1RST, 12U)
```

CRC 复位（Reset）。

<a id="af57270b020dc88eff8b6a1ef7fac10ff"></a>

### `GD32_RESET_DMA`

```c
#define GD32_RESET_DMA GD32_RESET_CONFIG(AHB1RST, 21U)
```

DMA 复位（Reset）。

<a id="a3757cebbf6f3557b95ad38f58eeeec6f"></a>

### `GD32_RESET_GPIOA`

```c
#define GD32_RESET_GPIOA GD32_RESET_CONFIG(AHB2RST, 17U)
```

GPIOA 复位（Reset）。

<a id="af5961280a760bba841a7d9f2ba1b4e2f"></a>

### `GD32_RESET_GPIOB`

```c
#define GD32_RESET_GPIOB GD32_RESET_CONFIG(AHB2RST, 18U)
```

GPIOB 复位（Reset）。

<a id="a5a20c0f1febc4709b3038cb0c5ef55bc"></a>

### `GD32_RESET_GPIOC`

```c
#define GD32_RESET_GPIOC GD32_RESET_CONFIG(AHB2RST, 19U)
```

GPIOC 复位（Reset）。

<a id="ab9da13b274d377bdce3b3cce159c0cd4"></a>

### `GD32_RESET_GPIOD`

```c
#define GD32_RESET_GPIOD GD32_RESET_CONFIG(AHB2RST, 20U)
```

GPIOD 复位（Reset）。

<a id="a8cac628be929c7303ca2017b0e2a2798"></a>

### `GD32_RESET_GPIOF`

```c
#define GD32_RESET_GPIOF GD32_RESET_CONFIG(AHB2RST, 22U)
```

GPIOF 复位（Reset）。

<a id="a12b532298a73feed3aa42ad53cf6ca79"></a>

### `GD32_RESET_I2C0`

```c
#define GD32_RESET_I2C0 GD32_RESET_CONFIG(APBRST, 21U)
```

I2C0 复位（Reset）。

<a id="a9b9bec0c724fce490ba57090fe5329cc"></a>

### `GD32_RESET_I2C1`

```c
#define GD32_RESET_I2C1 GD32_RESET_CONFIG(APBRST, 22U)
```

I2C1 复位（Reset）。

<a id="a02b6250ebdbfa5de5f39f49c6d81f1ef"></a>

### `GD32_RESET_PMU`

```c
#define GD32_RESET_PMU GD32_RESET_CONFIG(APBRST, 28U)
```

PMU 复位（Reset）。

<a id="a64f740c7f65d696deb5f617654be9c5d"></a>

### `GD32_RESET_SPI0`

```c
#define GD32_RESET_SPI0 GD32_RESET_CONFIG(APBRST, 12U)
```

SPI0 复位（Reset）。

<a id="a27ae8979a4889e95867ed833d9843d07"></a>

### `GD32_RESET_SPI1`

```c
#define GD32_RESET_SPI1 GD32_RESET_CONFIG(APBRST, 13U)
```

SPI1 复位（Reset）。

<a id="afd91e374f836fdf42970966e9d4677c4"></a>

### `GD32_RESET_SYSCFG`

```c
#define GD32_RESET_SYSCFG GD32_RESET_CONFIG(APBRST, 0U)
```

SYSCFG 复位（Reset）。

<a id="a2a7fd67d22598a774386a49ded2a9c72"></a>

### `GD32_RESET_TIMER0`

```c
#define GD32_RESET_TIMER0 GD32_RESET_CONFIG(APBRST, 10U)
```

TIMER0 复位（Reset）。

<a id="a012ec5ec4ff3dca4b788f9839be1c2f6"></a>

### `GD32_RESET_TIMER13`

```c
#define GD32_RESET_TIMER13 GD32_RESET_CONFIG(APBRST, 16U)
```

TIMER13 复位（Reset）。

<a id="ae1f1c4a1aa517935b9f76bc136a76809"></a>

### `GD32_RESET_TIMER15`

```c
#define GD32_RESET_TIMER15 GD32_RESET_CONFIG(APBRST, 17U)
```

TIMER15 复位（Reset）。

<a id="afe50a4990f8267250bd0b454ddfe2b73"></a>

### `GD32_RESET_TIMER16`

```c
#define GD32_RESET_TIMER16 GD32_RESET_CONFIG(APBRST, 18U)
```

TIMER16 复位（Reset）。

<a id="a113cfc98af5cb46151d0545cf54fe5aa"></a>

### `GD32_RESET_TIMER2`

```c
#define GD32_RESET_TIMER2 GD32_RESET_CONFIG(APBRST, 11U)
```

TIMER2 复位（Reset）。

<a id="a6a03a7368d1e153ddf89547962711d35"></a>

### `GD32_RESET_USART0`

```c
#define GD32_RESET_USART0 GD32_RESET_CONFIG(APBRST, 14U)
```

USART0 复位（Reset）。

<a id="aeb24e0ab9ae6be1c82593220c9719117"></a>

### `GD32_RESET_USART1`

```c
#define GD32_RESET_USART1 GD32_RESET_CONFIG(APBRST, 15U)
```

USART1 复位（Reset）。

<a id="a362e90b2303107bd5ec1cd57662e986a"></a>

### `GD32_RESET_USART2`

```c
#define GD32_RESET_USART2 GD32_RESET_CONFIG(APBRST, 19U)
```

USART2 复位（Reset）。

<a id="a8aac1c0ab090d8568076f6d8556e5c7a"></a>

### `GD32_RESET_WWDGT`

```c
#define GD32_RESET_WWDGT GD32_RESET_CONFIG(APBRST, 8U)
```

窗口看门狗复位（Window Watchdog Reset）。


## 16.3\_原页交叉引用（Cross References）

- [gd32-common.h](../api_source_reference/P286_gd32-common.h_源码浏览.md)
- [查看此文件的源码。](../api_source_runtime_reference/P025_gd32c2x1.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P015_zephyr__drivers__misc__ft8xx__ft8xx_reference_api.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P017_zephyr__bluetooth__audio__has.h_文件参考.md)
