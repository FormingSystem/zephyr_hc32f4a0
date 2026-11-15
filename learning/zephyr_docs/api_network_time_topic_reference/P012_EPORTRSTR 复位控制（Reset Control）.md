---
id: learning.zephyr-docs.api-network-time-topic-reference.page-12
title: EPORTRSTR 复位控制（Reset Control）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__eportrstr__resets.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_EPORTRSTR 复位控制（Reset Control）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__eportrstr__resets.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

EPORT 复位控制寄存器对应的外设。

<a id="details"></a>

EPORT 复位控制寄存器对应的外设。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 12.1\_宏定义（Macros）

<a id="r_gac1532022c40bd7d071e3597d70e7d0f4"></a>

```c
#define FOCALTECH_RESET_EPORT0 FOCALTECH_RESET_CONFIG(EPORTRSTCR, 0U)
```

相关声明：[FOCALTECH_RESET_EPORT0](#gac1532022c40bd7d071e3597d70e7d0f4)。

EPORT0 复位（reset）。

<a id="r_ga9bdbff48cb55369a4b194785a9dd14a1"></a>

```c
#define FOCALTECH_RESET_EPORT1 FOCALTECH_RESET_CONFIG(EPORTRSTCR, 1U)
```

相关声明：[FOCALTECH_RESET_EPORT1](#ga9bdbff48cb55369a4b194785a9dd14a1)。

EPORT1 复位。

<a id="r_ga1c731760579999f96687b8a81c61dc3e"></a>

```c
#define FOCALTECH_RESET_EPORT2 FOCALTECH_RESET_CONFIG(EPORTRSTCR, 2U)
```

相关声明：[FOCALTECH_RESET_EPORT2](#ga1c731760579999f96687b8a81c61dc3e)。

EPORT2 复位。

<a id="r_gac2c04d30326e36e4e7b284e9852803a3"></a>

```c
#define FOCALTECH_RESET_EPORT3 FOCALTECH_RESET_CONFIG(EPORTRSTCR, 3U)
```

相关声明：[FOCALTECH_RESET_EPORT3](#gac2c04d30326e36e4e7b284e9852803a3)。

EPORT3 复位。

<a id="r_ga15510335513f34201b7acb6239063d93"></a>

```c
#define FOCALTECH_RESET_EPORT4 FOCALTECH_RESET_CONFIG(EPORTRSTCR, 4U)
```

相关声明：[FOCALTECH_RESET_EPORT4](#ga15510335513f34201b7acb6239063d93)。

EPORT4 复位。

<a id="r_gaa72200eab0c7dc5daf7750c425a5c5a2"></a>

```c
#define FOCALTECH_RESET_EPORT5 FOCALTECH_RESET_CONFIG(EPORTRSTCR, 5U)
```

相关声明：[FOCALTECH_RESET_EPORT5](#gaa72200eab0c7dc5daf7750c425a5c5a2)。

EPORT5 复位。

<a id="r_ga661d0cbcdff6e303f0c155c7fe7fe232"></a>

```c
#define FOCALTECH_RESET_EPORT6 FOCALTECH_RESET_CONFIG(EPORTRSTCR, 6U)
```

相关声明：[FOCALTECH_RESET_EPORT6](#ga661d0cbcdff6e303f0c155c7fe7fe232)。

EPORT6 复位。

<a id="r_gab608960b531c74daff4e6816ce8e4abf"></a>

```c
#define FOCALTECH_RESET_EPORT7 FOCALTECH_RESET_CONFIG(EPORTRSTCR, 7U)
```

相关声明：[FOCALTECH_RESET_EPORT7](#gab608960b531c74daff4e6816ce8e4abf)。

EPORT7 复位。

<a id="r_ga66e82f86157f87b7c1e6a417bc5ac73d"></a>

```c
#define FOCALTECH_RESET_ACMP1 FOCALTECH_RESET_CONFIG(EPORTRSTCR, 8U)
```

相关声明：[FOCALTECH_RESET_ACMP1](#ga66e82f86157f87b7c1e6a417bc5ac73d)。

ACMP1 复位。

<a id="r_gafa0d499c4c67e8a7028383d3d67a8c75"></a>

```c
#define FOCALTECH_RESET_ACMP2 FOCALTECH_RESET_CONFIG(EPORTRSTCR, 9U)
```

相关声明：[FOCALTECH_RESET_ACMP2](#gafa0d499c4c67e8a7028383d3d67a8c75)。

ACMP2 复位。

## 12.2\_详细说明（Detailed Documentation）

<a id="ga66e82f86157f87b7c1e6a417bc5ac73d"></a>

### `FOCALTECH_RESET_ACMP1`

```c
#define FOCALTECH_RESET_ACMP1 FOCALTECH_RESET_CONFIG(EPORTRSTCR, 8U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

ACMP1 复位。

<a id="gafa0d499c4c67e8a7028383d3d67a8c75"></a>

### `FOCALTECH_RESET_ACMP2`

```c
#define FOCALTECH_RESET_ACMP2 FOCALTECH_RESET_CONFIG(EPORTRSTCR, 9U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

ACMP2 复位。

<a id="gac1532022c40bd7d071e3597d70e7d0f4"></a>

### `FOCALTECH_RESET_EPORT0`

```c
#define FOCALTECH_RESET_EPORT0 FOCALTECH_RESET_CONFIG(EPORTRSTCR, 0U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

EPORT0 复位（reset）。

<a id="ga9bdbff48cb55369a4b194785a9dd14a1"></a>

### `FOCALTECH_RESET_EPORT1`

```c
#define FOCALTECH_RESET_EPORT1 FOCALTECH_RESET_CONFIG(EPORTRSTCR, 1U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

EPORT1 复位。

<a id="ga1c731760579999f96687b8a81c61dc3e"></a>

### `FOCALTECH_RESET_EPORT2`

```c
#define FOCALTECH_RESET_EPORT2 FOCALTECH_RESET_CONFIG(EPORTRSTCR, 2U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

EPORT2 复位。

<a id="gac2c04d30326e36e4e7b284e9852803a3"></a>

### `FOCALTECH_RESET_EPORT3`

```c
#define FOCALTECH_RESET_EPORT3 FOCALTECH_RESET_CONFIG(EPORTRSTCR, 3U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

EPORT3 复位。

<a id="ga15510335513f34201b7acb6239063d93"></a>

### `FOCALTECH_RESET_EPORT4`

```c
#define FOCALTECH_RESET_EPORT4 FOCALTECH_RESET_CONFIG(EPORTRSTCR, 4U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

EPORT4 复位。

<a id="gaa72200eab0c7dc5daf7750c425a5c5a2"></a>

### `FOCALTECH_RESET_EPORT5`

```c
#define FOCALTECH_RESET_EPORT5 FOCALTECH_RESET_CONFIG(EPORTRSTCR, 5U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

EPORT5 复位。

<a id="ga661d0cbcdff6e303f0c155c7fe7fe232"></a>

### `FOCALTECH_RESET_EPORT6`

```c
#define FOCALTECH_RESET_EPORT6 FOCALTECH_RESET_CONFIG(EPORTRSTCR, 6U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

EPORT6 复位。

<a id="gab608960b531c74daff4e6816ce8e4abf"></a>

### `FOCALTECH_RESET_EPORT7`

```c
#define FOCALTECH_RESET_EPORT7 FOCALTECH_RESET_CONFIG(EPORTRSTCR, 7U)
```

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>
```

EPORT7 复位。


## 12.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/reset/focaltech_ft9001_reset.h](https://docs.zephyrproject.org/latest/doxygen/html/focaltech__ft9001__reset_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P011_以太网桥转发数据库（Ethernet bridge FDB）.md) · [返回大纲](大纲.md) · [下一章](P013_现场可编程门阵列（FPGA）.md)
