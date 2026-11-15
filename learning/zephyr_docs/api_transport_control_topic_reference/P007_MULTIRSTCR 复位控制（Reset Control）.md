---
id: learning.zephyr-docs.api-transport-control-topic-reference.page-7
title: MULTIRSTCR 复位控制（Reset Control）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__multirstcr__resets.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_MULTIRSTCR 复位控制（Reset Control）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__multirstcr__resets.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

多重复位控制寄存器（Multi Reset Control Register）对应的外设。

<a id="details"></a>

多重复位控制寄存器（Multi Reset Control Register）对应的外设。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.1\_宏定义（Macros）

<a id="r_ga46bbd9e1b3d0b62f61fabbaa8c334adc"></a>

```c
#define FOCALTECH_RESET_OTP_AHB FOCALTECH_RESET_CONFIG(MULTIRSTCR, 0U)
```

相关声明：[FOCALTECH_RESET_OTP_AHB](#ga46bbd9e1b3d0b62f61fabbaa8c334adc)。

OTP AHB 复位（Reset）。

<a id="r_gaeee18837dae2087428921fcfcb556675"></a>

```c
#define FOCALTECH_RESET_MCC FOCALTECH_RESET_CONFIG(MULTIRSTCR, 1U)
```

相关声明：[FOCALTECH_RESET_MCC](#gaeee18837dae2087428921fcfcb556675)。

MCC 复位（Reset）。

<a id="r_ga0983a1b5886dfb370dbf9e2f705e441f"></a>

```c
#define FOCALTECH_RESET_MCCADR FOCALTECH_RESET_CONFIG(MULTIRSTCR, 2U)
```

相关声明：[FOCALTECH_RESET_MCCADR](#ga0983a1b5886dfb370dbf9e2f705e441f)。

MCC 地址（Address） 复位（Reset）。

<a id="r_ga912e26cdf2b90bd075e1a69b425c97b2"></a>

```c
#define FOCALTECH_RESET_ADC FOCALTECH_RESET_CONFIG(MULTIRSTCR, 3U)
```

相关声明：[FOCALTECH_RESET_ADC](#ga912e26cdf2b90bd075e1a69b425c97b2)。

ADC 复位（Reset）。

<a id="r_ga7ed484674341a911a948cff1d4594c9a"></a>

```c
#define FOCALTECH_RESET_MESH FOCALTECH_RESET_CONFIG(MULTIRSTCR, 4U)
```

相关声明：[FOCALTECH_RESET_MESH](#ga7ed484674341a911a948cff1d4594c9a)。

MESH 复位（Reset）。

<a id="r_gab46b7e24dfde17907d3ebeb640afcdb9"></a>

```c
#define FOCALTECH_RESET_TC FOCALTECH_RESET_CONFIG(MULTIRSTCR, 5U)
```

相关声明：[FOCALTECH_RESET_TC](#gab46b7e24dfde17907d3ebeb640afcdb9)。

TC 复位（Reset）。

<a id="r_gad58737d782cc2495d5bc173b6f02a0ff"></a>

```c
#define FOCALTECH_RESET_CLKOUT FOCALTECH_RESET_CONFIG(MULTIRSTCR, 6U)
```

相关声明：[FOCALTECH_RESET_CLKOUT](#gad58737d782cc2495d5bc173b6f02a0ff)。

时钟输出（Clock Output） 复位（Reset）。

<a id="r_ga5536cbd12d63c541b93b3afc8b7279ad"></a>

```c
#define FOCALTECH_RESET_KEY_CTRL FOCALTECH_RESET_CONFIG(MULTIRSTCR, 7U)
```

相关声明：[FOCALTECH_RESET_KEY_CTRL](#ga5536cbd12d63c541b93b3afc8b7279ad)。

Key 控制器（Key Controller） 复位（Reset）。

<a id="r_gac2740388f9e13c9a41dbf519f4d81b1e"></a>

```c
#define FOCALTECH_RESET_CCM_RESET FOCALTECH_RESET_CONFIG(MULTIRSTCR, 8U)
```

相关声明：[FOCALTECH_RESET_CCM_RESET](#gac2740388f9e13c9a41dbf519f4d81b1e)。

CCM 复位（Reset）。

<a id="r_ga19ea0b41ff1d420fdd621231bc7f5620"></a>

```c
#define FOCALTECH_RESET_OTP_IPS FOCALTECH_RESET_CONFIG(MULTIRSTCR, 9U)
```

相关声明：[FOCALTECH_RESET_OTP_IPS](#ga19ea0b41ff1d420fdd621231bc7f5620)。

OTP IPS 复位（Reset）。

<a id="r_ga82036818a156d4e471c4292382ebf4b4"></a>

```c
#define FOCALTECH_RESET_CPM_IPS FOCALTECH_RESET_CONFIG(MULTIRSTCR, 10U)
```

相关声明：[FOCALTECH_RESET_CPM_IPS](#ga82036818a156d4e471c4292382ebf4b4)。

CPM IPS 复位（Reset）。

<a id="r_ga2089134755b7e42d06d75959cb630520"></a>

```c
#define FOCALTECH_RESET_TRACE FOCALTECH_RESET_CONFIG(MULTIRSTCR, 11U)
```

相关声明：[FOCALTECH_RESET_TRACE](#ga2089134755b7e42d06d75959cb630520)。

跟踪（Trace） 复位（Reset）。

<a id="r_gad5f1147d63f910091e73a2963dc34849"></a>

```c
#define FOCALTECH_RESET_I2S_M FOCALTECH_RESET_CONFIG(MULTIRSTCR, 12U)
```

相关声明：[FOCALTECH_RESET_I2S_M](#gad5f1147d63f910091e73a2963dc34849)。

I2S 主设备（Master） 复位（Reset）。

<a id="r_ga3f74b242e0fa83ed8e80e38dc11847ff"></a>

```c
#define FOCALTECH_RESET_I2S_S FOCALTECH_RESET_CONFIG(MULTIRSTCR, 13U)
```

相关声明：[FOCALTECH_RESET_I2S_S](#ga3f74b242e0fa83ed8e80e38dc11847ff)。

I2S 从设备（Slave） 复位（Reset）。

<a id="r_gab704c34447390a3a45a959175026f201"></a>

```c
#define FOCALTECH_RESET_CRC0 FOCALTECH_RESET_CONFIG(MULTIRSTCR, 14U)
```

相关声明：[FOCALTECH_RESET_CRC0](#gab704c34447390a3a45a959175026f201)。

CRC0 复位（Reset）。

<a id="r_gaa05b6ae8e4720ff54d0a6586534496c9"></a>

```c
#define FOCALTECH_RESET_CRC1 FOCALTECH_RESET_CONFIG(MULTIRSTCR, 15U)
```

相关声明：[FOCALTECH_RESET_CRC1](#gaa05b6ae8e4720ff54d0a6586534496c9)。

CRC1 复位（Reset）。

## 7.2\_详细说明（Detailed Documentation）

<a id="ga912e26cdf2b90bd075e1a69b425c97b2"></a>

### `FOCALTECH_RESET_ADC`

```c
#define FOCALTECH_RESET_ADC FOCALTECH_RESET_CONFIG(MULTIRSTCR, 3U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

ADC 复位（Reset）。

<a id="gac2740388f9e13c9a41dbf519f4d81b1e"></a>

### `FOCALTECH_RESET_CCM_RESET`

```c
#define FOCALTECH_RESET_CCM_RESET FOCALTECH_RESET_CONFIG(MULTIRSTCR, 8U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

CCM 复位（Reset）。

<a id="gad58737d782cc2495d5bc173b6f02a0ff"></a>

### `FOCALTECH_RESET_CLKOUT`

```c
#define FOCALTECH_RESET_CLKOUT FOCALTECH_RESET_CONFIG(MULTIRSTCR, 6U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

时钟输出（Clock Output） 复位（Reset）。

<a id="ga82036818a156d4e471c4292382ebf4b4"></a>

### `FOCALTECH_RESET_CPM_IPS`

```c
#define FOCALTECH_RESET_CPM_IPS FOCALTECH_RESET_CONFIG(MULTIRSTCR, 10U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

CPM IPS 复位（Reset）。

<a id="gab704c34447390a3a45a959175026f201"></a>

### `FOCALTECH_RESET_CRC0`

```c
#define FOCALTECH_RESET_CRC0 FOCALTECH_RESET_CONFIG(MULTIRSTCR, 14U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

CRC0 复位（Reset）。

<a id="gaa05b6ae8e4720ff54d0a6586534496c9"></a>

### `FOCALTECH_RESET_CRC1`

```c
#define FOCALTECH_RESET_CRC1 FOCALTECH_RESET_CONFIG(MULTIRSTCR, 15U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

CRC1 复位（Reset）。

<a id="gad5f1147d63f910091e73a2963dc34849"></a>

### `FOCALTECH_RESET_I2S_M`

```c
#define FOCALTECH_RESET_I2S_M FOCALTECH_RESET_CONFIG(MULTIRSTCR, 12U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

I2S 主设备（Master） 复位（Reset）。

<a id="ga3f74b242e0fa83ed8e80e38dc11847ff"></a>

### `FOCALTECH_RESET_I2S_S`

```c
#define FOCALTECH_RESET_I2S_S FOCALTECH_RESET_CONFIG(MULTIRSTCR, 13U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

I2S 从设备（Slave） 复位（Reset）。

<a id="ga5536cbd12d63c541b93b3afc8b7279ad"></a>

### `FOCALTECH_RESET_KEY_CTRL`

```c
#define FOCALTECH_RESET_KEY_CTRL FOCALTECH_RESET_CONFIG(MULTIRSTCR, 7U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

Key 控制器（Key Controller） 复位（Reset）。

<a id="gaeee18837dae2087428921fcfcb556675"></a>

### `FOCALTECH_RESET_MCC`

```c
#define FOCALTECH_RESET_MCC FOCALTECH_RESET_CONFIG(MULTIRSTCR, 1U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

MCC 复位（Reset）。

<a id="ga0983a1b5886dfb370dbf9e2f705e441f"></a>

### `FOCALTECH_RESET_MCCADR`

```c
#define FOCALTECH_RESET_MCCADR FOCALTECH_RESET_CONFIG(MULTIRSTCR, 2U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

MCC 地址（Address） 复位（Reset）。

<a id="ga7ed484674341a911a948cff1d4594c9a"></a>

### `FOCALTECH_RESET_MESH`

```c
#define FOCALTECH_RESET_MESH FOCALTECH_RESET_CONFIG(MULTIRSTCR, 4U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

MESH 复位（Reset）。

<a id="ga46bbd9e1b3d0b62f61fabbaa8c334adc"></a>

### `FOCALTECH_RESET_OTP_AHB`

```c
#define FOCALTECH_RESET_OTP_AHB FOCALTECH_RESET_CONFIG(MULTIRSTCR, 0U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

OTP AHB 复位（Reset）。

<a id="ga19ea0b41ff1d420fdd621231bc7f5620"></a>

### `FOCALTECH_RESET_OTP_IPS`

```c
#define FOCALTECH_RESET_OTP_IPS FOCALTECH_RESET_CONFIG(MULTIRSTCR, 9U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

OTP IPS 复位（Reset）。

<a id="gab46b7e24dfde17907d3ebeb640afcdb9"></a>

### `FOCALTECH_RESET_TC`

```c
#define FOCALTECH_RESET_TC FOCALTECH_RESET_CONFIG(MULTIRSTCR, 5U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

TC 复位（Reset）。

<a id="ga2089134755b7e42d06d75959cb630520"></a>

### `FOCALTECH_RESET_TRACE`

```c
#define FOCALTECH_RESET_TRACE FOCALTECH_RESET_CONFIG(MULTIRSTCR, 11U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

跟踪（Trace） 复位（Reset）。


## 7.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/reset/focaltech_ft9001_reset.h](https://docs.zephyrproject.org/latest/doxygen/html/focaltech__ft9001__reset_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P006_eSPI 驱动后端 API（Driver Backend API）.md) · [返回大纲](大纲.md) · [下一章](P008_ICM4268X API主题.md)
