---
id: learning.zephyr-docs.api-protocol-topic-reference.page-19
title: FocalTech 复位控制模块寄存器（Reset Control Module Registers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__reset__regs.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_FocalTech 复位控制模块寄存器（Reset Control Module Registers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__reset__regs.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

复位控制模块寄存器的偏移量。

<a id="details"></a>

复位控制模块寄存器的偏移量。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 19.1\_宏定义（Macros）

<a id="r_ga14b208f0a5eb8e54f8cccb622896f367"></a>

```c
#define FOCALTECH_EPORTRSTCR_OFFSET 0x88U
```

相关声明：[FOCALTECH_EPORTRSTCR_OFFSET](#ga14b208f0a5eb8e54f8cccb622896f367)。

EPORT 复位控制寄存器（Reset Control Register）。

<a id="r_gabfd52f09e8021a6a4a88ea9545edd4ac"></a>

```c
#define FOCALTECH_MULTIRSTCR_OFFSET 0xACU
```

相关声明：[FOCALTECH_MULTIRSTCR_OFFSET](#gabfd52f09e8021a6a4a88ea9545edd4ac)。

多模块复位控制寄存器（Multi Reset Control Register）。

<a id="r_ga943200e23ff31dce4a36b68b0664def7"></a>

```c
#define FOCALTECH_SYSRSTCR_OFFSET 0xB0U
```

相关声明：[FOCALTECH_SYSRSTCR_OFFSET](#ga943200e23ff31dce4a36b68b0664def7)。

系统复位控制寄存器（System Reset Control Register）。

<a id="r_gaa62d0bb8b7627d258095ef599ea803d0"></a>

```c
#define FOCALTECH_AHB3RSTCR_OFFSET 0xB4U
```

相关声明：[FOCALTECH_AHB3RSTCR_OFFSET](#gaa62d0bb8b7627d258095ef599ea803d0)。

AHB3 复位控制寄存器（Reset Control Register）。

<a id="r_ga386d01a7838235774815997a33f77577"></a>

```c
#define FOCALTECH_ARITHRSTCR_OFFSET 0xB8U
```

相关声明：[FOCALTECH_ARITHRSTCR_OFFSET](#ga386d01a7838235774815997a33f77577)。

算法复位控制寄存器（Algorithm Reset Control Register）。

<a id="r_gaa9c609bd1da838111513b2c5e78588ca"></a>

```c
#define FOCALTECH_IPSRSTCR_OFFSET 0xBCU
```

相关声明：[FOCALTECH_IPSRSTCR_OFFSET](#gaa9c609bd1da838111513b2c5e78588ca)。

IPS 复位控制寄存器（Reset Control Register）。

## 19.2\_详细说明（Detailed Documentation）

<a id="gaa62d0bb8b7627d258095ef599ea803d0"></a>

### `FOCALTECH_AHB3RSTCR_OFFSET`

```c
#define FOCALTECH_AHB3RSTCR_OFFSET 0xB4U
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

AHB3 复位控制寄存器（Reset Control Register）。

<a id="ga386d01a7838235774815997a33f77577"></a>

### `FOCALTECH_ARITHRSTCR_OFFSET`

```c
#define FOCALTECH_ARITHRSTCR_OFFSET 0xB8U
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

算法复位控制寄存器（Algorithm Reset Control Register）。

<a id="ga14b208f0a5eb8e54f8cccb622896f367"></a>

### `FOCALTECH_EPORTRSTCR_OFFSET`

```c
#define FOCALTECH_EPORTRSTCR_OFFSET 0x88U
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

EPORT 复位控制寄存器（Reset Control Register）。

<a id="gaa9c609bd1da838111513b2c5e78588ca"></a>

### `FOCALTECH_IPSRSTCR_OFFSET`

```c
#define FOCALTECH_IPSRSTCR_OFFSET 0xBCU
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

IPS 复位控制寄存器（Reset Control Register）。

<a id="gabfd52f09e8021a6a4a88ea9545edd4ac"></a>

### `FOCALTECH_MULTIRSTCR_OFFSET`

```c
#define FOCALTECH_MULTIRSTCR_OFFSET 0xACU
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

多模块复位控制寄存器（Multi Reset Control Register）。

<a id="ga943200e23ff31dce4a36b68b0664def7"></a>

### `FOCALTECH_SYSRSTCR_OFFSET`

```c
#define FOCALTECH_SYSRSTCR_OFFSET 0xB0U
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

系统复位控制寄存器（System Reset Control Register）。


## 19.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/reset/focaltech_ft9001_reset.h](https://docs.zephyrproject.org/latest/doxygen/html/focaltech__ft9001__reset_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P018_ITE IT51XXX中断控制器（Interrupt Controller）.md) · [返回大纲](大纲.md) · [下一章](P020_HCI 原始通道（RAW channel）.md)
