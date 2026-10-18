---
id: learning.zephyr-docs.api-auxiliary-topic-reference.page-8
title: AHB3RSTCR 复位控制（Reset Control）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__ahb3rstcr__resets.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_AHB3RSTCR 复位控制（Reset Control）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__ahb3rstcr__resets.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

AHB3 复位控制寄存器对应的外设。

<a id="details"></a>

AHB3 复位控制寄存器对应的外设。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 8.1\_宏定义（Macros）

<a id="r_ga447851fbf278af65b38904e30045fc19"></a>

```c
#define FOCALTECH_RESET_ROM FOCALTECH_RESET_CONFIG(AHB3RSTCR, 0U)
```

相关声明：[FOCALTECH_RESET_ROM](#ga447851fbf278af65b38904e30045fc19)。

ROM 复位（reset）。

<a id="r_gab429b3964b5c228cce44c270c964e0ee"></a>

```c
#define FOCALTECH_RESET_ROM_OTP_MUX FOCALTECH_RESET_CONFIG(AHB3RSTCR, 1U)
```

相关声明：[FOCALTECH_RESET_ROM_OTP_MUX](#gab429b3964b5c228cce44c270c964e0ee)。

ROM OTP 多路复用器（MUX）复位。

<a id="r_gaf33f88c4f792b7529f075fbd83b01e71"></a>

```c
#define FOCALTECH_RESET_AHB3_MUX FOCALTECH_RESET_CONFIG(AHB3RSTCR, 2U)
```

相关声明：[FOCALTECH_RESET_AHB3_MUX](#gaf33f88c4f792b7529f075fbd83b01e71)。

AHB3 多路复用器（MUX）复位。

<a id="r_ga743a6041380923309cc652cddab980a8"></a>

```c
#define FOCALTECH_RESET_USBC FOCALTECH_RESET_CONFIG(AHB3RSTCR, 3U)
```

相关声明：[FOCALTECH_RESET_USBC](#ga743a6041380923309cc652cddab980a8)。

USB 控制器复位。

<a id="r_gad76e8b42e772894a25fff56c91e46b08"></a>

```c
#define FOCALTECH_RESET_PXLP1_APB FOCALTECH_RESET_CONFIG(AHB3RSTCR, 4U)
```

相关声明：[FOCALTECH_RESET_PXLP1_APB](#gad76e8b42e772894a25fff56c91e46b08)。

PXLP1 APB 复位。

<a id="r_gaa3710eb031f196eb13d98b9a34c6813c"></a>

```c
#define FOCALTECH_RESET_PXLP2_APB FOCALTECH_RESET_CONFIG(AHB3RSTCR, 5U)
```

相关声明：[FOCALTECH_RESET_PXLP2_APB](#gaa3710eb031f196eb13d98b9a34c6813c)。

PXLP2 APB 复位。

<a id="r_ga03a88cdec31ee479b648d16609f3f1de"></a>

```c
#define FOCALTECH_RESET_I2S1 FOCALTECH_RESET_CONFIG(AHB3RSTCR, 6U)
```

相关声明：[FOCALTECH_RESET_I2S1](#ga03a88cdec31ee479b648d16609f3f1de)。

I2S1 复位。

<a id="r_ga9472bf1174ae07a3b1bb0fbda422742e"></a>

```c
#define FOCALTECH_RESET_I2S2 FOCALTECH_RESET_CONFIG(AHB3RSTCR, 7U)
```

相关声明：[FOCALTECH_RESET_I2S2](#ga9472bf1174ae07a3b1bb0fbda422742e)。

I2S2 复位。

## 8.2\_详细说明（Detailed Documentation）

<a id="gaf33f88c4f792b7529f075fbd83b01e71"></a>

### `FOCALTECH_RESET_AHB3_MUX`

```c
#define FOCALTECH_RESET_AHB3_MUX FOCALTECH_RESET_CONFIG(AHB3RSTCR, 2U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

AHB3 多路复用器（MUX）复位。

<a id="ga03a88cdec31ee479b648d16609f3f1de"></a>

### `FOCALTECH_RESET_I2S1`

```c
#define FOCALTECH_RESET_I2S1 FOCALTECH_RESET_CONFIG(AHB3RSTCR, 6U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

I2S1 复位。

<a id="ga9472bf1174ae07a3b1bb0fbda422742e"></a>

### `FOCALTECH_RESET_I2S2`

```c
#define FOCALTECH_RESET_I2S2 FOCALTECH_RESET_CONFIG(AHB3RSTCR, 7U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

I2S2 复位。

<a id="gad76e8b42e772894a25fff56c91e46b08"></a>

### `FOCALTECH_RESET_PXLP1_APB`

```c
#define FOCALTECH_RESET_PXLP1_APB FOCALTECH_RESET_CONFIG(AHB3RSTCR, 4U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

PXLP1 APB 复位。

<a id="gaa3710eb031f196eb13d98b9a34c6813c"></a>

### `FOCALTECH_RESET_PXLP2_APB`

```c
#define FOCALTECH_RESET_PXLP2_APB FOCALTECH_RESET_CONFIG(AHB3RSTCR, 5U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

PXLP2 APB 复位。

<a id="ga447851fbf278af65b38904e30045fc19"></a>

### `FOCALTECH_RESET_ROM`

```c
#define FOCALTECH_RESET_ROM FOCALTECH_RESET_CONFIG(AHB3RSTCR, 0U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

ROM 复位（reset）。

<a id="gab429b3964b5c228cce44c270c964e0ee"></a>

### `FOCALTECH_RESET_ROM_OTP_MUX`

```c
#define FOCALTECH_RESET_ROM_OTP_MUX FOCALTECH_RESET_CONFIG(AHB3RSTCR, 1U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

ROM OTP 多路复用器（MUX）复位。

<a id="ga743a6041380923309cc652cddab980a8"></a>

### `FOCALTECH_RESET_USBC`

```c
#define FOCALTECH_RESET_USBC FOCALTECH_RESET_CONFIG(AHB3RSTCR, 3U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

USB 控制器复位。


## 8.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/reset/focaltech_ft9001_reset.h](https://docs.zephyrproject.org/latest/doxygen/html/focaltech__ft9001__reset_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P007_FDC2X1X API主题.md) · [返回大纲](大纲.md) · [下一章](P009_数字信号处理（Digital Signal Processing，DSP）.md)
