---
id: learning.zephyr-docs.api-connection-topic-reference.page-7
title: 瑞萨 RA BSP 时钟输出分频常量（Clock Clkout Divider Constants）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__clkout.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_瑞萨 RA BSP 时钟输出分频常量（Clock Clkout Divider Constants）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__clkout.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

PCLK 时钟源（Clock source）

<a id="details"></a>

PCLK 时钟源；FSXP 时钟源；Renesas RA 板级支持包（BSP）的时钟输出分频常量（clkout divider constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.1\_宏定义（Macros）

<a id="r_gad56dead80f923b0b8840b3c84bdf65fa"></a>

```c
#define BSP_CLOCKS_CLKOUT_DIV_1 (0)
```

相关声明：[BSP_CLOCKS_CLKOUT_DIV_1](#gad56dead80f923b0b8840b3c84bdf65fa)。

时钟输出（Clkout）1 分频。

<a id="r_ga46ed6e2dc58841f0b112003ed9f4a5db"></a>

```c
#define BSP_CLOCKS_CLKOUT_DIV_2 (1)
```

相关声明：[BSP_CLOCKS_CLKOUT_DIV_2](#ga46ed6e2dc58841f0b112003ed9f4a5db)。

时钟输出 2 分频。

<a id="r_ga2ef0885ff687beeb8c5ec867bb97424b"></a>

```c
#define BSP_CLOCKS_CLKOUT_DIV_4 (2)
```

相关声明：[BSP_CLOCKS_CLKOUT_DIV_4](#ga2ef0885ff687beeb8c5ec867bb97424b)。

时钟输出 4 分频。

<a id="r_ga79d6afda43cf5f9f6246fdb28285fd8e"></a>

```c
#define BSP_CLOCKS_CLKOUT_DIV_8 (3)
```

相关声明：[BSP_CLOCKS_CLKOUT_DIV_8](#ga79d6afda43cf5f9f6246fdb28285fd8e)。

时钟输出 8 分频。

<a id="r_gac15fa2c5d5533746dd002636063bbf17"></a>

```c
#define BSP_CLOCKS_CLKOUT_DIV_16 (4)
```

相关声明：[BSP_CLOCKS_CLKOUT_DIV_16](#gac15fa2c5d5533746dd002636063bbf17)。

时钟输出 16 分频。

<a id="r_ga58684d2331eb5cd218bbfc58254b27e7"></a>

```c
#define BSP_CLOCKS_CLKOUT_DIV_32 (5)
```

相关声明：[BSP_CLOCKS_CLKOUT_DIV_32](#ga58684d2331eb5cd218bbfc58254b27e7)。

时钟输出 32 分频。

<a id="r_gaae419122d7da67d550e5d93e8108c237"></a>

```c
#define BSP_CLOCKS_CLKOUT_DIV_64 (6)
```

相关声明：[BSP_CLOCKS_CLKOUT_DIV_64](#gaae419122d7da67d550e5d93e8108c237)。

时钟输出 64 分频。

<a id="r_ga1541a9c2e367cea7a96da0d522d2c7eb"></a>

```c
#define BSP_CLOCKS_CLKOUT_DIV_128 (7)
```

相关声明：[BSP_CLOCKS_CLKOUT_DIV_128](#ga1541a9c2e367cea7a96da0d522d2c7eb)。

时钟输出 128 分频。

## 7.2\_详细说明（Detailed Documentation）

<a id="gad56dead80f923b0b8840b3c84bdf65fa"></a>

### `BSP_CLOCKS_CLKOUT_DIV_1`

```c
#define BSP_CLOCKS_CLKOUT_DIV_1 (0)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

时钟输出（Clkout）1 分频。

<a id="ga1541a9c2e367cea7a96da0d522d2c7eb"></a>

### `BSP_CLOCKS_CLKOUT_DIV_128`

```c
#define BSP_CLOCKS_CLKOUT_DIV_128 (7)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

时钟输出 128 分频。

<a id="gac15fa2c5d5533746dd002636063bbf17"></a>

### `BSP_CLOCKS_CLKOUT_DIV_16`

```c
#define BSP_CLOCKS_CLKOUT_DIV_16 (4)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

时钟输出 16 分频。

<a id="ga46ed6e2dc58841f0b112003ed9f4a5db"></a>

### `BSP_CLOCKS_CLKOUT_DIV_2`

```c
#define BSP_CLOCKS_CLKOUT_DIV_2 (1)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

时钟输出 2 分频。

<a id="ga58684d2331eb5cd218bbfc58254b27e7"></a>

### `BSP_CLOCKS_CLKOUT_DIV_32`

```c
#define BSP_CLOCKS_CLKOUT_DIV_32 (5)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

时钟输出 32 分频。

<a id="ga2ef0885ff687beeb8c5ec867bb97424b"></a>

### `BSP_CLOCKS_CLKOUT_DIV_4`

```c
#define BSP_CLOCKS_CLKOUT_DIV_4 (2)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

时钟输出 4 分频。

<a id="gaae419122d7da67d550e5d93e8108c237"></a>

### `BSP_CLOCKS_CLKOUT_DIV_64`

```c
#define BSP_CLOCKS_CLKOUT_DIV_64 (6)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

时钟输出 64 分频。

<a id="ga79d6afda43cf5f9f6246fdb28285fd8e"></a>

### `BSP_CLOCKS_CLKOUT_DIV_8`

```c
#define BSP_CLOCKS_CLKOUT_DIV_8 (3)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

时钟输出 8 分频。


## 7.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/renesas_ra_cgc.h](https://docs.zephyrproject.org/latest/doxygen/html/renesas__ra__cgc_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P006_博流智能（Bouffalo Lab）.md) · [返回大纲](大纲.md) · [下一章](P008_磁盘访问（Disk Access）.md)
