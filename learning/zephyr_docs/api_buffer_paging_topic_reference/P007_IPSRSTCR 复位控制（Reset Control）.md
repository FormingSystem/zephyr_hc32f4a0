---
id: learning.zephyr-docs.api-buffer-paging-topic-reference.page-7
title: IPSRSTCR 复位控制（Reset Control）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__ipsrstcr__resets.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_IPSRSTCR 复位控制（Reset Control）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__ipsrstcr__resets.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IPS 复位控制寄存器对应的外设。

<a id="details"></a>

IPS 复位控制寄存器对应的外设。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.1\_宏定义（Macros）

<a id="r_ga60a6a9f5ef12bdb1ad5909c992234faa"></a>

```c
#define FOCALTECH_RESET_IO_CTRL FOCALTECH_RESET_CONFIG(IPSRSTCR, 0U)
```

相关声明：[FOCALTECH_RESET_IO_CTRL](#ga60a6a9f5ef12bdb1ad5909c992234faa)。

I/O 控制器复位（IO Controller Reset）。

<a id="r_ga23196071f4d02b825b2e40fbc648b97a"></a>

```c
#define FOCALTECH_RESET_WDT FOCALTECH_RESET_CONFIG(IPSRSTCR, 1U)
```

相关声明：[FOCALTECH_RESET_WDT](#ga23196071f4d02b825b2e40fbc648b97a)。

看门狗定时器复位（Watchdog Timer Reset）。

<a id="r_ga4875113ccb459b1e6e264de54c2ffc0a"></a>

```c
#define FOCALTECH_RESET_RTC FOCALTECH_RESET_CONFIG(IPSRSTCR, 2U)
```

相关声明：[FOCALTECH_RESET_RTC](#ga4875113ccb459b1e6e264de54c2ffc0a)。

RTC 复位（Reset）。

<a id="r_gad973fbc73a970d07d6ad470f1b309ca4"></a>

```c
#define FOCALTECH_RESET_PIT1 FOCALTECH_RESET_CONFIG(IPSRSTCR, 3U)
```

相关声明：[FOCALTECH_RESET_PIT1](#gad973fbc73a970d07d6ad470f1b309ca4)。

PIT1 复位（Reset）。

<a id="r_ga38943fdef6b7ee8417576078f85cf382"></a>

```c
#define FOCALTECH_RESET_PIT2 FOCALTECH_RESET_CONFIG(IPSRSTCR, 4U)
```

相关声明：[FOCALTECH_RESET_PIT2](#ga38943fdef6b7ee8417576078f85cf382)。

PIT2 复位（Reset）。

<a id="r_ga3ba939af141dff4f65cda43668ae8888"></a>

```c
#define FOCALTECH_RESET_USI1 FOCALTECH_RESET_CONFIG(IPSRSTCR, 5U)
```

相关声明：[FOCALTECH_RESET_USI1](#ga3ba939af141dff4f65cda43668ae8888)。

USI1 复位（Reset）。

<a id="r_gacf9093e53fb0385eb90e66ef0f65f8de"></a>

```c
#define FOCALTECH_RESET_EDMAC1 FOCALTECH_RESET_CONFIG(IPSRSTCR, 6U)
```

相关声明：[FOCALTECH_RESET_EDMAC1](#gacf9093e53fb0385eb90e66ef0f65f8de)。

EDMAC1 复位（Reset）。

<a id="r_gadbced14265c08f7f8e234531d6e0abf7"></a>

```c
#define FOCALTECH_RESET_SPI1 FOCALTECH_RESET_CONFIG(IPSRSTCR, 7U)
```

相关声明：[FOCALTECH_RESET_SPI1](#gadbced14265c08f7f8e234531d6e0abf7)。

SPI1 复位（Reset）。

<a id="r_gabbe5f32ac775072810f02e779499462b"></a>

```c
#define FOCALTECH_RESET_SPI2 FOCALTECH_RESET_CONFIG(IPSRSTCR, 8U)
```

相关声明：[FOCALTECH_RESET_SPI2](#gabbe5f32ac775072810f02e779499462b)。

SPI2 复位（Reset）。

<a id="r_ga7281304a265cfd95b48fd7420f9f2027"></a>

```c
#define FOCALTECH_RESET_SPI3 FOCALTECH_RESET_CONFIG(IPSRSTCR, 9U)
```

相关声明：[FOCALTECH_RESET_SPI3](#ga7281304a265cfd95b48fd7420f9f2027)。

SPI3 复位（Reset）。

<a id="r_ga64d3fe882d3dbeb6ccd8218538a99fbf"></a>

```c
#define FOCALTECH_RESET_SCI1 FOCALTECH_RESET_CONFIG(IPSRSTCR, 10U)
```

相关声明：[FOCALTECH_RESET_SCI1](#ga64d3fe882d3dbeb6ccd8218538a99fbf)。

SCI1 复位（Reset）。

<a id="r_ga31b2bc4472d7455de72217216b9c068f"></a>

```c
#define FOCALTECH_RESET_SCI2 FOCALTECH_RESET_CONFIG(IPSRSTCR, 11U)
```

相关声明：[FOCALTECH_RESET_SCI2](#ga31b2bc4472d7455de72217216b9c068f)。

SCI2 复位（Reset）。

<a id="r_ga75c151a5750135c086893af842fe167d"></a>

```c
#define FOCALTECH_RESET_USI2 FOCALTECH_RESET_CONFIG(IPSRSTCR, 12U)
```

相关声明：[FOCALTECH_RESET_USI2](#ga75c151a5750135c086893af842fe167d)。

USI2 复位（Reset）。

<a id="r_ga27413ec5515407960d47d4942e21e3e7"></a>

```c
#define FOCALTECH_RESET_CAN1 FOCALTECH_RESET_CONFIG(IPSRSTCR, 13U)
```

相关声明：[FOCALTECH_RESET_CAN1](#ga27413ec5515407960d47d4942e21e3e7)。

CAN1 复位（Reset）。

<a id="r_ga721c4e8eaad920f3990547280a51de46"></a>

```c
#define FOCALTECH_RESET_I2C1 FOCALTECH_RESET_CONFIG(IPSRSTCR, 14U)
```

相关声明：[FOCALTECH_RESET_I2C1](#ga721c4e8eaad920f3990547280a51de46)。

I2C1 复位（Reset）。

<a id="r_ga60d731d5f1b8f2219c842a94002fa14c"></a>

```c
#define FOCALTECH_RESET_PWM0 FOCALTECH_RESET_CONFIG(IPSRSTCR, 15U)
```

相关声明：[FOCALTECH_RESET_PWM0](#ga60d731d5f1b8f2219c842a94002fa14c)。

PWM0 复位（Reset）。

<a id="r_gad3af6cad5d8ae27b40d0bb8a319e3d31"></a>

```c
#define FOCALTECH_RESET_I2C2 FOCALTECH_RESET_CONFIG(IPSRSTCR, 16U)
```

相关声明：[FOCALTECH_RESET_I2C2](#gad3af6cad5d8ae27b40d0bb8a319e3d31)。

I2C2 复位（Reset）。

<a id="r_ga1a390c4c955ad9a7889b4106e31c7c03"></a>

```c
#define FOCALTECH_RESET_CAN2 FOCALTECH_RESET_CONFIG(IPSRSTCR, 17U)
```

相关声明：[FOCALTECH_RESET_CAN2](#ga1a390c4c955ad9a7889b4106e31c7c03)。

CAN2 复位（Reset）。

<a id="r_ga3b1fdc9f2d6f32ca105ccfd78d193cad"></a>

```c
#define FOCALTECH_RESET_SCI3 FOCALTECH_RESET_CONFIG(IPSRSTCR, 18U)
```

相关声明：[FOCALTECH_RESET_SCI3](#ga3b1fdc9f2d6f32ca105ccfd78d193cad)。

SCI3 复位（Reset）。

<a id="r_ga5fc20fe7b8c04946b5e98da6e10c3225"></a>

```c
#define FOCALTECH_RESET_QADC FOCALTECH_RESET_CONFIG(IPSRSTCR, 20U)
```

相关声明：[FOCALTECH_RESET_QADC](#ga5fc20fe7b8c04946b5e98da6e10c3225)。

QADC 复位（Reset）。

<a id="r_gae919d9192d4e02630de012bfb2bac18c"></a>

```c
#define FOCALTECH_RESET_DAC FOCALTECH_RESET_CONFIG(IPSRSTCR, 21U)
```

相关声明：[FOCALTECH_RESET_DAC](#gae919d9192d4e02630de012bfb2bac18c)。

DAC 复位（Reset）。

<a id="r_gac467218bae41cd35bb93335deb6197f8"></a>

```c
#define FOCALTECH_RESET_MCC_IPS FOCALTECH_RESET_CONFIG(IPSRSTCR, 22U)
```

相关声明：[FOCALTECH_RESET_MCC_IPS](#gac467218bae41cd35bb93335deb6197f8)。

MCC IPS 复位（Reset）。

<a id="r_ga49d792f2fff8f95d671689279b9e8b11"></a>

```c
#define FOCALTECH_RESET_PWMT1 FOCALTECH_RESET_CONFIG(IPSRSTCR, 23U)
```

相关声明：[FOCALTECH_RESET_PWMT1](#ga49d792f2fff8f95d671689279b9e8b11)。

PWMT1 复位（Reset）。

<a id="r_ga48331ab9690d7499fd8cfbcffb9705a9"></a>

```c
#define FOCALTECH_RESET_LD FOCALTECH_RESET_CONFIG(IPSRSTCR, 24U)
```

相关声明：[FOCALTECH_RESET_LD](#ga48331ab9690d7499fd8cfbcffb9705a9)。

LD 复位（Reset）。

<a id="r_gac45d20a806ae571f15c120ddf30cb91c"></a>

```c
#define FOCALTECH_RESET_PWMT2 FOCALTECH_RESET_CONFIG(IPSRSTCR, 25U)
```

相关声明：[FOCALTECH_RESET_PWMT2](#gac45d20a806ae571f15c120ddf30cb91c)。

PWMT2 复位（Reset）。

<a id="r_gaa4d9885a8d24489bd4dfab44ee62eeed"></a>

```c
#define FOCALTECH_RESET_PGD FOCALTECH_RESET_CONFIG(IPSRSTCR, 26U)
```

相关声明：[FOCALTECH_RESET_PGD](#gaa4d9885a8d24489bd4dfab44ee62eeed)。

PGD 复位（Reset）。

<a id="r_ga8dd114e35b6b12f157d5338b608a885f"></a>

```c
#define FOCALTECH_RESET_SEC_DET FOCALTECH_RESET_CONFIG(IPSRSTCR, 27U)
```

相关声明：[FOCALTECH_RESET_SEC_DET](#ga8dd114e35b6b12f157d5338b608a885f)。

安全检测器复位（Security Detector Reset）。

<a id="r_gabf7202867a4dc81cb164e3e11a9497d3"></a>

```c
#define FOCALTECH_RESET_PCI FOCALTECH_RESET_CONFIG(IPSRSTCR, 28U)
```

相关声明：[FOCALTECH_RESET_PCI](#gabf7202867a4dc81cb164e3e11a9497d3)。

PCI 复位（Reset）。

<a id="r_ga6e2d8cd9384878ec751c01ca376c1396"></a>

```c
#define FOCALTECH_RESET_PMURTC FOCALTECH_RESET_CONFIG(IPSRSTCR, 29U)
```

相关声明：[FOCALTECH_RESET_PMURTC](#ga6e2d8cd9384878ec751c01ca376c1396)。

PMU RTC 复位（Reset）。

<a id="r_gab80962f564341a6bee51a9ef9f324602"></a>

```c
#define FOCALTECH_RESET_AHB2IPS FOCALTECH_RESET_CONFIG(IPSRSTCR, 30U)
```

相关声明：[FOCALTECH_RESET_AHB2IPS](#gab80962f564341a6bee51a9ef9f324602)。

AHB2IPS 复位（Reset）。

<a id="r_gacf8695dc4f1041d436a6d79ea3115eb5"></a>

```c
#define FOCALTECH_RESET_PWMT3 FOCALTECH_RESET_CONFIG(IPSRSTCR, 31U)
```

相关声明：[FOCALTECH_RESET_PWMT3](#gacf8695dc4f1041d436a6d79ea3115eb5)。

PWMT3 复位（Reset）。

## 7.2\_详细说明（Detailed Documentation）

<a id="gab80962f564341a6bee51a9ef9f324602"></a>

### `FOCALTECH_RESET_AHB2IPS`

```c
#define FOCALTECH_RESET_AHB2IPS FOCALTECH_RESET_CONFIG(IPSRSTCR, 30U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

AHB2IPS 复位（Reset）。

<a id="ga27413ec5515407960d47d4942e21e3e7"></a>

### `FOCALTECH_RESET_CAN1`

```c
#define FOCALTECH_RESET_CAN1 FOCALTECH_RESET_CONFIG(IPSRSTCR, 13U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

CAN1 复位（Reset）。

<a id="ga1a390c4c955ad9a7889b4106e31c7c03"></a>

### `FOCALTECH_RESET_CAN2`

```c
#define FOCALTECH_RESET_CAN2 FOCALTECH_RESET_CONFIG(IPSRSTCR, 17U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

CAN2 复位（Reset）。

<a id="gae919d9192d4e02630de012bfb2bac18c"></a>

### `FOCALTECH_RESET_DAC`

```c
#define FOCALTECH_RESET_DAC FOCALTECH_RESET_CONFIG(IPSRSTCR, 21U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

DAC 复位（Reset）。

<a id="gacf9093e53fb0385eb90e66ef0f65f8de"></a>

### `FOCALTECH_RESET_EDMAC1`

```c
#define FOCALTECH_RESET_EDMAC1 FOCALTECH_RESET_CONFIG(IPSRSTCR, 6U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

EDMAC1 复位（Reset）。

<a id="ga721c4e8eaad920f3990547280a51de46"></a>

### `FOCALTECH_RESET_I2C1`

```c
#define FOCALTECH_RESET_I2C1 FOCALTECH_RESET_CONFIG(IPSRSTCR, 14U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

I2C1 复位（Reset）。

<a id="gad3af6cad5d8ae27b40d0bb8a319e3d31"></a>

### `FOCALTECH_RESET_I2C2`

```c
#define FOCALTECH_RESET_I2C2 FOCALTECH_RESET_CONFIG(IPSRSTCR, 16U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

I2C2 复位（Reset）。

<a id="ga60a6a9f5ef12bdb1ad5909c992234faa"></a>

### `FOCALTECH_RESET_IO_CTRL`

```c
#define FOCALTECH_RESET_IO_CTRL FOCALTECH_RESET_CONFIG(IPSRSTCR, 0U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

I/O 控制器复位（IO Controller Reset）。

<a id="ga48331ab9690d7499fd8cfbcffb9705a9"></a>

### `FOCALTECH_RESET_LD`

```c
#define FOCALTECH_RESET_LD FOCALTECH_RESET_CONFIG(IPSRSTCR, 24U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

LD 复位（Reset）。

<a id="gac467218bae41cd35bb93335deb6197f8"></a>

### `FOCALTECH_RESET_MCC_IPS`

```c
#define FOCALTECH_RESET_MCC_IPS FOCALTECH_RESET_CONFIG(IPSRSTCR, 22U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

MCC IPS 复位（Reset）。

<a id="gabf7202867a4dc81cb164e3e11a9497d3"></a>

### `FOCALTECH_RESET_PCI`

```c
#define FOCALTECH_RESET_PCI FOCALTECH_RESET_CONFIG(IPSRSTCR, 28U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

PCI 复位（Reset）。

<a id="gaa4d9885a8d24489bd4dfab44ee62eeed"></a>

### `FOCALTECH_RESET_PGD`

```c
#define FOCALTECH_RESET_PGD FOCALTECH_RESET_CONFIG(IPSRSTCR, 26U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

PGD 复位（Reset）。

<a id="gad973fbc73a970d07d6ad470f1b309ca4"></a>

### `FOCALTECH_RESET_PIT1`

```c
#define FOCALTECH_RESET_PIT1 FOCALTECH_RESET_CONFIG(IPSRSTCR, 3U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

PIT1 复位（Reset）。

<a id="ga38943fdef6b7ee8417576078f85cf382"></a>

### `FOCALTECH_RESET_PIT2`

```c
#define FOCALTECH_RESET_PIT2 FOCALTECH_RESET_CONFIG(IPSRSTCR, 4U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

PIT2 复位（Reset）。

<a id="ga6e2d8cd9384878ec751c01ca376c1396"></a>

### `FOCALTECH_RESET_PMURTC`

```c
#define FOCALTECH_RESET_PMURTC FOCALTECH_RESET_CONFIG(IPSRSTCR, 29U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

PMU RTC 复位（Reset）。

<a id="ga60d731d5f1b8f2219c842a94002fa14c"></a>

### `FOCALTECH_RESET_PWM0`

```c
#define FOCALTECH_RESET_PWM0 FOCALTECH_RESET_CONFIG(IPSRSTCR, 15U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

PWM0 复位（Reset）。

<a id="ga49d792f2fff8f95d671689279b9e8b11"></a>

### `FOCALTECH_RESET_PWMT1`

```c
#define FOCALTECH_RESET_PWMT1 FOCALTECH_RESET_CONFIG(IPSRSTCR, 23U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

PWMT1 复位（Reset）。

<a id="gac45d20a806ae571f15c120ddf30cb91c"></a>

### `FOCALTECH_RESET_PWMT2`

```c
#define FOCALTECH_RESET_PWMT2 FOCALTECH_RESET_CONFIG(IPSRSTCR, 25U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

PWMT2 复位（Reset）。

<a id="gacf8695dc4f1041d436a6d79ea3115eb5"></a>

### `FOCALTECH_RESET_PWMT3`

```c
#define FOCALTECH_RESET_PWMT3 FOCALTECH_RESET_CONFIG(IPSRSTCR, 31U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

PWMT3 复位（Reset）。

<a id="ga5fc20fe7b8c04946b5e98da6e10c3225"></a>

### `FOCALTECH_RESET_QADC`

```c
#define FOCALTECH_RESET_QADC FOCALTECH_RESET_CONFIG(IPSRSTCR, 20U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

QADC 复位（Reset）。

<a id="ga4875113ccb459b1e6e264de54c2ffc0a"></a>

### `FOCALTECH_RESET_RTC`

```c
#define FOCALTECH_RESET_RTC FOCALTECH_RESET_CONFIG(IPSRSTCR, 2U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

RTC 复位（Reset）。

<a id="ga64d3fe882d3dbeb6ccd8218538a99fbf"></a>

### `FOCALTECH_RESET_SCI1`

```c
#define FOCALTECH_RESET_SCI1 FOCALTECH_RESET_CONFIG(IPSRSTCR, 10U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

SCI1 复位（Reset）。

<a id="ga31b2bc4472d7455de72217216b9c068f"></a>

### `FOCALTECH_RESET_SCI2`

```c
#define FOCALTECH_RESET_SCI2 FOCALTECH_RESET_CONFIG(IPSRSTCR, 11U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

SCI2 复位（Reset）。

<a id="ga3b1fdc9f2d6f32ca105ccfd78d193cad"></a>

### `FOCALTECH_RESET_SCI3`

```c
#define FOCALTECH_RESET_SCI3 FOCALTECH_RESET_CONFIG(IPSRSTCR, 18U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

SCI3 复位（Reset）。

<a id="ga8dd114e35b6b12f157d5338b608a885f"></a>

### `FOCALTECH_RESET_SEC_DET`

```c
#define FOCALTECH_RESET_SEC_DET FOCALTECH_RESET_CONFIG(IPSRSTCR, 27U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

安全检测器复位（Security Detector Reset）。

<a id="gadbced14265c08f7f8e234531d6e0abf7"></a>

### `FOCALTECH_RESET_SPI1`

```c
#define FOCALTECH_RESET_SPI1 FOCALTECH_RESET_CONFIG(IPSRSTCR, 7U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

SPI1 复位（Reset）。

<a id="gabbe5f32ac775072810f02e779499462b"></a>

### `FOCALTECH_RESET_SPI2`

```c
#define FOCALTECH_RESET_SPI2 FOCALTECH_RESET_CONFIG(IPSRSTCR, 8U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

SPI2 复位（Reset）。

<a id="ga7281304a265cfd95b48fd7420f9f2027"></a>

### `FOCALTECH_RESET_SPI3`

```c
#define FOCALTECH_RESET_SPI3 FOCALTECH_RESET_CONFIG(IPSRSTCR, 9U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

SPI3 复位（Reset）。

<a id="ga3ba939af141dff4f65cda43668ae8888"></a>

### `FOCALTECH_RESET_USI1`

```c
#define FOCALTECH_RESET_USI1 FOCALTECH_RESET_CONFIG(IPSRSTCR, 5U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

USI1 复位（Reset）。

<a id="ga75c151a5750135c086893af842fe167d"></a>

### `FOCALTECH_RESET_USI2`

```c
#define FOCALTECH_RESET_USI2 FOCALTECH_RESET_CONFIG(IPSRSTCR, 12U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

USI2 复位（Reset）。

<a id="ga23196071f4d02b825b2e40fbc648b97a"></a>

### `FOCALTECH_RESET_WDT`

```c
#define FOCALTECH_RESET_WDT FOCALTECH_RESET_CONFIG(IPSRSTCR, 1U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

看门狗定时器复位（Watchdog Timer Reset）。


## 7.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/reset/focaltech_ft9001_reset.h](https://docs.zephyrproject.org/latest/doxygen/html/focaltech__ft9001__reset_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P006_错误检测与纠正（EDAC）.md) · [返回大纲](大纲.md) · [下一章](P008_HTTP服务器（Server）API。.md)
