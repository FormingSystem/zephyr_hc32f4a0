---
id: learning.zephyr-docs.api-vector-pipeline-topic-reference.page-8
title: ARITHRSTCR 复位控制（Reset Control）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__arithrstcr__resets.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_ARITHRSTCR 复位控制（Reset Control）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__arithrstcr__resets.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

算法复位控制寄存器（Algorithm Reset Control Register）对应的外设。

<a id="details"></a>

算法复位控制寄存器（Algorithm Reset Control Register）对应的外设。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 8.1\_宏定义（Macros）

<a id="r_ga429695ee2f576fc6a3357241aa38c215"></a>

```c
#define FOCALTECH_RESET_AES FOCALTECH_RESET_CONFIG(ARITHRSTCR, 1U)
```

相关声明：[FOCALTECH_RESET_AES](#ga429695ee2f576fc6a3357241aa38c215)。

AES 复位（Reset）。

<a id="r_ga7524cad266f64ab27830a8deb266bedd"></a>

```c
#define FOCALTECH_RESET_SM4 FOCALTECH_RESET_CONFIG(ARITHRSTCR, 2U)
```

相关声明：[FOCALTECH_RESET_SM4](#ga7524cad266f64ab27830a8deb266bedd)。

SM4 复位（Reset）。

<a id="r_ga1034fb963eb617815f8028bff5e5bcc7"></a>

```c
#define FOCALTECH_RESET_RF_AES_SM4 FOCALTECH_RESET_CONFIG(ARITHRSTCR, 4U)
```

相关声明：[FOCALTECH_RESET_RF_AES_SM4](#ga1034fb963eb617815f8028bff5e5bcc7)。

RF AES SM4 复位（Reset）。

<a id="r_ga1e3477301447a988b3f2ce831172b4a8"></a>

```c
#define FOCALTECH_RESET_CRYPTO FOCALTECH_RESET_CONFIG(ARITHRSTCR, 5U)
```

相关声明：[FOCALTECH_RESET_CRYPTO](#ga1e3477301447a988b3f2ce831172b4a8)。

加密模块（Crypto）复位。

<a id="r_gaf3941bb54a85acdd59b995844b21bd42"></a>

```c
#define FOCALTECH_RESET_SHA FOCALTECH_RESET_CONFIG(ARITHRSTCR, 6U)
```

相关声明：[FOCALTECH_RESET_SHA](#gaf3941bb54a85acdd59b995844b21bd42)。

SHA 复位（Reset）。

<a id="r_ga8766e97447e1418adc43ad93cef51ba6"></a>

```c
#define FOCALTECH_RESET_EDMAC0 FOCALTECH_RESET_CONFIG(ARITHRSTCR, 7U)
```

相关声明：[FOCALTECH_RESET_EDMAC0](#ga8766e97447e1418adc43ad93cef51ba6)。

EDMAC0 复位（Reset）。

<a id="r_gadf9a12c842552043611970bf7f657df3"></a>

```c
#define FOCALTECH_RESET_DES FOCALTECH_RESET_CONFIG(ARITHRSTCR, 8U)
```

相关声明：[FOCALTECH_RESET_DES](#gadf9a12c842552043611970bf7f657df3)。

DES 复位（Reset）。

<a id="r_ga23e239f9738c819a2fe24016768c6995"></a>

```c
#define FOCALTECH_RESET_ZUC FOCALTECH_RESET_CONFIG(ARITHRSTCR, 9U)
```

相关声明：[FOCALTECH_RESET_ZUC](#ga23e239f9738c819a2fe24016768c6995)。

ZUC 复位（Reset）。

<a id="r_gad5e83816e598adb358d726c941892fa7"></a>

```c
#define FOCALTECH_RESET_AHB2MLB FOCALTECH_RESET_CONFIG(ARITHRSTCR, 10U)
```

相关声明：[FOCALTECH_RESET_AHB2MLB](#gad5e83816e598adb358d726c941892fa7)。

AHB2MLB 复位（Reset）。

<a id="r_gad54c36e48530d8cf63b8d83a5e536ae5"></a>

```c
#define FOCALTECH_RESET_AHB2IPS2 FOCALTECH_RESET_CONFIG(ARITHRSTCR, 11U)
```

相关声明：[FOCALTECH_RESET_AHB2IPS2](#gad54c36e48530d8cf63b8d83a5e536ae5)。

AHB2IPS2 复位（Reset）。

<a id="r_gaa9011c2f1c02ea6b256155ef5fde3e05"></a>

```c
#define FOCALTECH_RESET_TRNG FOCALTECH_RESET_CONFIG(ARITHRSTCR, 12U)
```

相关声明：[FOCALTECH_RESET_TRNG](#gaa9011c2f1c02ea6b256155ef5fde3e05)。

真随机数发生器（True Random Number Generator，TRNG）复位。

## 8.2\_详细说明（Detailed Documentation）

<a id="ga429695ee2f576fc6a3357241aa38c215"></a>

### `FOCALTECH_RESET_AES`

```c
#define FOCALTECH_RESET_AES FOCALTECH_RESET_CONFIG(ARITHRSTCR, 1U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

AES 复位（Reset）。

<a id="gad54c36e48530d8cf63b8d83a5e536ae5"></a>

### `FOCALTECH_RESET_AHB2IPS2`

```c
#define FOCALTECH_RESET_AHB2IPS2 FOCALTECH_RESET_CONFIG(ARITHRSTCR, 11U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

AHB2IPS2 复位（Reset）。

<a id="gad5e83816e598adb358d726c941892fa7"></a>

### `FOCALTECH_RESET_AHB2MLB`

```c
#define FOCALTECH_RESET_AHB2MLB FOCALTECH_RESET_CONFIG(ARITHRSTCR, 10U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

AHB2MLB 复位（Reset）。

<a id="ga1e3477301447a988b3f2ce831172b4a8"></a>

### `FOCALTECH_RESET_CRYPTO`

```c
#define FOCALTECH_RESET_CRYPTO FOCALTECH_RESET_CONFIG(ARITHRSTCR, 5U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

加密模块（Crypto）复位。

<a id="gadf9a12c842552043611970bf7f657df3"></a>

### `FOCALTECH_RESET_DES`

```c
#define FOCALTECH_RESET_DES FOCALTECH_RESET_CONFIG(ARITHRSTCR, 8U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

DES 复位（Reset）。

<a id="ga8766e97447e1418adc43ad93cef51ba6"></a>

### `FOCALTECH_RESET_EDMAC0`

```c
#define FOCALTECH_RESET_EDMAC0 FOCALTECH_RESET_CONFIG(ARITHRSTCR, 7U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

EDMAC0 复位（Reset）。

<a id="ga1034fb963eb617815f8028bff5e5bcc7"></a>

### `FOCALTECH_RESET_RF_AES_SM4`

```c
#define FOCALTECH_RESET_RF_AES_SM4 FOCALTECH_RESET_CONFIG(ARITHRSTCR, 4U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

RF AES SM4 复位（Reset）。

<a id="gaf3941bb54a85acdd59b995844b21bd42"></a>

### `FOCALTECH_RESET_SHA`

```c
#define FOCALTECH_RESET_SHA FOCALTECH_RESET_CONFIG(ARITHRSTCR, 6U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

SHA 复位（Reset）。

<a id="ga7524cad266f64ab27830a8deb266bedd"></a>

### `FOCALTECH_RESET_SM4`

```c
#define FOCALTECH_RESET_SM4 FOCALTECH_RESET_CONFIG(ARITHRSTCR, 2U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

SM4 复位（Reset）。

<a id="gaa9011c2f1c02ea6b256155ef5fde3e05"></a>

### `FOCALTECH_RESET_TRNG`

```c
#define FOCALTECH_RESET_TRNG FOCALTECH_RESET_CONFIG(ARITHRSTCR, 12U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

真随机数发生器（True Random Number Generator，TRNG）复位。

<a id="ga23e239f9738c819a2fe24016768c6995"></a>

### `FOCALTECH_RESET_ZUC`

```c
#define FOCALTECH_RESET_ZUC FOCALTECH_RESET_CONFIG(ARITHRSTCR, 9U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

ZUC 复位（Reset）。


## 8.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/reset/focaltech_ft9001_reset.h](https://docs.zephyrproject.org/latest/doxygen/html/focaltech__ft9001__reset_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P007_Arm通用中断控制器（GIC Interrupt Controller）.md) · [返回大纲](大纲.md) · [下一章](P009_电量计驱动后端 API（Fuel Gauge Driver Backend API）.md)
