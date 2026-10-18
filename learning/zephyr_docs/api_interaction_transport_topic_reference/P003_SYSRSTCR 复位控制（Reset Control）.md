---
id: learning.zephyr-docs.api-interaction-transport-topic-reference.page-3
title: SYSRSTCR 复位控制（Reset Control）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__sysrstcr__resets.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_SYSRSTCR 复位控制（Reset Control）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__sysrstcr__resets.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

系统复位控制寄存器（System Reset Control Register）对应的外设。

<a id="details"></a>

系统复位控制寄存器（System Reset Control Register）对应的外设。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.1\_宏定义（Macros）

<a id="r_ga59d4227c9bf1489f8677cc93acb9c51c"></a>

```c
#define FOCALTECH_RESET_SSISLV1 FOCALTECH_RESET_CONFIG(SYSRSTCR, 0U)
```

相关声明：[FOCALTECH_RESET_SSISLV1](#ga59d4227c9bf1489f8677cc93acb9c51c)。

SSI 从机 1（Slave 1）复位。

<a id="r_gadf58c3c5d2308e7c65f6b76985344f1a"></a>

```c
#define FOCALTECH_RESET_DMAC1 FOCALTECH_RESET_CONFIG(SYSRSTCR, 1U)
```

相关声明：[FOCALTECH_RESET_DMAC1](#gadf58c3c5d2308e7c65f6b76985344f1a)。

DMAC1 复位（Reset）。

<a id="r_gaf267ed4b27b192b8f33070b946814643"></a>

```c
#define FOCALTECH_RESET_DMAC2 FOCALTECH_RESET_CONFIG(SYSRSTCR, 2U)
```

相关声明：[FOCALTECH_RESET_DMAC2](#gaf267ed4b27b192b8f33070b946814643)。

DMAC2 复位（Reset）。

<a id="r_ga7efb131ead62ca3029a5bd160b38e781"></a>

```c
#define FOCALTECH_RESET_AHB2_MUX FOCALTECH_RESET_CONFIG(SYSRSTCR, 3U)
```

相关声明：[FOCALTECH_RESET_AHB2_MUX](#ga7efb131ead62ca3029a5bd160b38e781)。

AHB2 多路复用器（MUX）复位。

<a id="r_ga5c79ce9cd726c2350ed604294657c825"></a>

```c
#define FOCALTECH_RESET_PXLP1_AHB FOCALTECH_RESET_CONFIG(SYSRSTCR, 10U)
```

相关声明：[FOCALTECH_RESET_PXLP1_AHB](#ga5c79ce9cd726c2350ed604294657c825)。

PXLP1 AHB 复位（Reset）。

<a id="r_ga41b21e2f451c2e8defd1ebb7badca937"></a>

```c
#define FOCALTECH_RESET_PXLP2_AHB FOCALTECH_RESET_CONFIG(SYSRSTCR, 11U)
```

相关声明：[FOCALTECH_RESET_PXLP2_AHB](#ga41b21e2f451c2e8defd1ebb7badca937)。

PXLP2 AHB 复位（Reset）。

<a id="r_ga783ae3aa688eb9abe2d457051f35bb83"></a>

```c
#define FOCALTECH_RESET_SRAMD FOCALTECH_RESET_CONFIG(SYSRSTCR, 12U)
```

相关声明：[FOCALTECH_RESET_SRAMD](#ga783ae3aa688eb9abe2d457051f35bb83)。

SRAM 数据复位（Data Reset）。

<a id="r_ga5101183f616716b3266d03b6d03c0d7c"></a>

```c
#define FOCALTECH_RESET_SRAM0 FOCALTECH_RESET_CONFIG(SYSRSTCR, 13U)
```

相关声明：[FOCALTECH_RESET_SRAM0](#ga5101183f616716b3266d03b6d03c0d7c)。

SRAM0 复位（Reset）。

<a id="r_ga4cae816aba6332bf0cbf0adb38d618f1"></a>

```c
#define FOCALTECH_RESET_SRAM1 FOCALTECH_RESET_CONFIG(SYSRSTCR, 14U)
```

相关声明：[FOCALTECH_RESET_SRAM1](#ga4cae816aba6332bf0cbf0adb38d618f1)。

SRAM1 复位（Reset）。

<a id="r_ga70ac8466cce6411a8e159d6dded280e5"></a>

```c
#define FOCALTECH_RESET_SRAM2 FOCALTECH_RESET_CONFIG(SYSRSTCR, 15U)
```

相关声明：[FOCALTECH_RESET_SRAM2](#ga70ac8466cce6411a8e159d6dded280e5)。

SRAM2 复位（Reset）。

<a id="r_gaa8b5763ee7e1ac184a28ec21d63e0d09"></a>

```c
#define FOCALTECH_RESET_SRAM3_4 FOCALTECH_RESET_CONFIG(SYSRSTCR, 16U)
```

相关声明：[FOCALTECH_RESET_SRAM3_4](#gaa8b5763ee7e1ac184a28ec21d63e0d09)。

SRAM3/4 复位（Reset）。

<a id="r_ga484a4ec976b714c56db3bd6fa2fce500"></a>

```c
#define FOCALTECH_RESET_SSI4 FOCALTECH_RESET_CONFIG(SYSRSTCR, 17U)
```

相关声明：[FOCALTECH_RESET_SSI4](#ga484a4ec976b714c56db3bd6fa2fce500)。

SSI4 复位（Reset）。

<a id="r_ga4a40dfcde87bf329e95d75960f40cb17"></a>

```c
#define FOCALTECH_RESET_SSI5 FOCALTECH_RESET_CONFIG(SYSRSTCR, 18U)
```

相关声明：[FOCALTECH_RESET_SSI5](#ga4a40dfcde87bf329e95d75960f40cb17)。

SSI5 复位（Reset）。

<a id="r_ga61a5a9485deb12d5b4df72bd7e9ed4fd"></a>

```c
#define FOCALTECH_RESET_SSI6 FOCALTECH_RESET_CONFIG(SYSRSTCR, 19U)
```

相关声明：[FOCALTECH_RESET_SSI6](#ga61a5a9485deb12d5b4df72bd7e9ed4fd)。

SSI6 复位（Reset）。

## 3.2\_详细说明（Detailed Documentation）

<a id="ga7efb131ead62ca3029a5bd160b38e781"></a>

### `FOCALTECH_RESET_AHB2_MUX`

```c
#define FOCALTECH_RESET_AHB2_MUX FOCALTECH_RESET_CONFIG(SYSRSTCR, 3U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

AHB2 多路复用器（MUX）复位。

<a id="gadf58c3c5d2308e7c65f6b76985344f1a"></a>

### `FOCALTECH_RESET_DMAC1`

```c
#define FOCALTECH_RESET_DMAC1 FOCALTECH_RESET_CONFIG(SYSRSTCR, 1U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

DMAC1 复位（Reset）。

<a id="gaf267ed4b27b192b8f33070b946814643"></a>

### `FOCALTECH_RESET_DMAC2`

```c
#define FOCALTECH_RESET_DMAC2 FOCALTECH_RESET_CONFIG(SYSRSTCR, 2U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

DMAC2 复位（Reset）。

<a id="ga5c79ce9cd726c2350ed604294657c825"></a>

### `FOCALTECH_RESET_PXLP1_AHB`

```c
#define FOCALTECH_RESET_PXLP1_AHB FOCALTECH_RESET_CONFIG(SYSRSTCR, 10U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

PXLP1 AHB 复位（Reset）。

<a id="ga41b21e2f451c2e8defd1ebb7badca937"></a>

### `FOCALTECH_RESET_PXLP2_AHB`

```c
#define FOCALTECH_RESET_PXLP2_AHB FOCALTECH_RESET_CONFIG(SYSRSTCR, 11U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

PXLP2 AHB 复位（Reset）。

<a id="ga5101183f616716b3266d03b6d03c0d7c"></a>

### `FOCALTECH_RESET_SRAM0`

```c
#define FOCALTECH_RESET_SRAM0 FOCALTECH_RESET_CONFIG(SYSRSTCR, 13U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

SRAM0 复位（Reset）。

<a id="ga4cae816aba6332bf0cbf0adb38d618f1"></a>

### `FOCALTECH_RESET_SRAM1`

```c
#define FOCALTECH_RESET_SRAM1 FOCALTECH_RESET_CONFIG(SYSRSTCR, 14U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

SRAM1 复位（Reset）。

<a id="ga70ac8466cce6411a8e159d6dded280e5"></a>

### `FOCALTECH_RESET_SRAM2`

```c
#define FOCALTECH_RESET_SRAM2 FOCALTECH_RESET_CONFIG(SYSRSTCR, 15U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

SRAM2 复位（Reset）。

<a id="gaa8b5763ee7e1ac184a28ec21d63e0d09"></a>

### `FOCALTECH_RESET_SRAM3_4`

```c
#define FOCALTECH_RESET_SRAM3_4 FOCALTECH_RESET_CONFIG(SYSRSTCR, 16U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

SRAM3/4 复位（Reset）。

<a id="ga783ae3aa688eb9abe2d457051f35bb83"></a>

### `FOCALTECH_RESET_SRAMD`

```c
#define FOCALTECH_RESET_SRAMD FOCALTECH_RESET_CONFIG(SYSRSTCR, 12U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

SRAM 数据复位（Data Reset）。

<a id="ga484a4ec976b714c56db3bd6fa2fce500"></a>

### `FOCALTECH_RESET_SSI4`

```c
#define FOCALTECH_RESET_SSI4 FOCALTECH_RESET_CONFIG(SYSRSTCR, 17U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

SSI4 复位（Reset）。

<a id="ga4a40dfcde87bf329e95d75960f40cb17"></a>

### `FOCALTECH_RESET_SSI5`

```c
#define FOCALTECH_RESET_SSI5 FOCALTECH_RESET_CONFIG(SYSRSTCR, 18U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

SSI5 复位（Reset）。

<a id="ga61a5a9485deb12d5b4df72bd7e9ed4fd"></a>

### `FOCALTECH_RESET_SSI6`

```c
#define FOCALTECH_RESET_SSI6 FOCALTECH_RESET_CONFIG(SYSRSTCR, 19U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

SSI6 复位（Reset）。

<a id="ga59d4227c9bf1489f8677cc93acb9c51c"></a>

### `FOCALTECH_RESET_SSISLV1`

```c
#define FOCALTECH_RESET_SSISLV1 FOCALTECH_RESET_CONFIG(SYSRSTCR, 0U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

SSI 从机 1（Slave 1）复位。


## 3.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/reset/focaltech_ft9001_reset.h](https://docs.zephyrproject.org/latest/doxygen/html/focaltech__ft9001__reset_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P002_FT9001 IOCTRL 寄存器偏移量（Register offsets）.md) · [返回大纲](大纲.md) · [下一章](P004_FTDI FT8xx API主题.md)
