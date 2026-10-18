---
id: learning.zephyr-docs.api-vector-pipeline-topic-reference.page-6
title: 瑞萨 RA BSP 时钟源常量（Clock Source Constants）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_瑞萨 RA BSP 时钟源常量（Clock Source Constants）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

瑞萨 RA BSP 时钟源常量（Clock source constants）

<a id="details"></a>

瑞萨 RA BSP 时钟源常量（Clock source constants）

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.1\_宏定义（Macros）

<a id="r_gac6d940bf68229ce58e586d99e88021ad"></a>

```c
#define BSP_CLOCKS_SOURCE_PLL BSP_CLOCKS_SOURCE_CLOCK_PLL
```

相关声明：[BSP_CLOCKS_SOURCE_PLL](#gac6d940bf68229ce58e586d99e88021ad)。

PLL 锁相环时钟源（Clock Source）。

<a id="r_ga80b3c5e721364e07c795d759e56bef5f"></a>

```c
#define BSP_CLOCKS_SOURCE_PLLP BSP_CLOCKS_SOURCE_CLOCK_PLL
```

相关声明：[BSP_CLOCKS_SOURCE_PLLP](#ga80b3c5e721364e07c795d759e56bef5f)。

PLLP 时钟源（Clock Source）。

<a id="r_ga198180ae8a259e478c13cb667efdc036"></a>

```c
#define BSP_CLOCKS_SOURCE_PLLQ BSP_CLOCKS_SOURCE_CLOCK_PLL1Q
```

相关声明：[BSP_CLOCKS_SOURCE_PLLQ](#ga198180ae8a259e478c13cb667efdc036)。

PLLQ 时钟源（Clock Source）。

<a id="r_ga9cf8b84320ad1c418e554c44d0ae324c"></a>

```c
#define BSP_CLOCKS_SOURCE_PLLR BSP_CLOCKS_SOURCE_CLOCK_PLL1R
```

相关声明：[BSP_CLOCKS_SOURCE_PLLR](#ga9cf8b84320ad1c418e554c44d0ae324c)。

PLLR 时钟源（Clock Source）。

<a id="r_ga526d6007889c727bc820b23a8bd57eb1"></a>

```c
#define BSP_CLOCKS_SOURCE_PLL2 BSP_CLOCKS_SOURCE_CLOCK_PLL2
```

相关声明：[BSP_CLOCKS_SOURCE_PLL2](#ga526d6007889c727bc820b23a8bd57eb1)。

PLL2 时钟源（Clock Source）。

<a id="r_ga7d74f3dc378453283c5a2752d261a635"></a>

```c
#define BSP_CLOCKS_SOURCE_PLL2P BSP_CLOCKS_SOURCE_CLOCK_PLL2
```

相关声明：[BSP_CLOCKS_SOURCE_PLL2P](#ga7d74f3dc378453283c5a2752d261a635)。

PLL2P 时钟源（Clock Source）。

<a id="r_gae21c8ebb5bfd4160ced33343517cf755"></a>

```c
#define BSP_CLOCKS_SOURCE_PLL2Q BSP_CLOCKS_SOURCE_CLOCK_PLL2Q
```

相关声明：[BSP_CLOCKS_SOURCE_PLL2Q](#gae21c8ebb5bfd4160ced33343517cf755)。

PLL2Q 时钟源（Clock Source）。

<a id="r_ga2c9eb4860dc00767ec81567b7e1ef915"></a>

```c
#define BSP_CLOCKS_SOURCE_PLL2R BSP_CLOCKS_SOURCE_CLOCK_PLL2R
```

相关声明：[BSP_CLOCKS_SOURCE_PLL2R](#ga2c9eb4860dc00767ec81567b7e1ef915)。

PLL2R 时钟源（Clock Source）。

<a id="r_ga6e88996a2dba7df510f6f9c37d921abb"></a>

```c
#define BSP_CLOCKS_SOURCE_XTALDIV_CLK BSP_CLOCKS_SOURCE_CLOCK_MAIN_OSC
```

相关声明：[BSP_CLOCKS_SOURCE_XTALDIV_CLK](#ga6e88996a2dba7df510f6f9c37d921abb)。

XTALDIV_CLK 时钟源（Clock Source）。

<a id="r_ga54275c8fca9740aeb84a78a9df958977"></a>

```c
#define BSP_CLOCKS_SOURCE_HOCODIV_CLK BSP_CLOCKS_SOURCE_CLOCK_HOCO
```

相关声明：[BSP_CLOCKS_SOURCE_HOCODIV_CLK](#ga54275c8fca9740aeb84a78a9df958977)。

HOCODIV_CLK 时钟源（Clock Source）。

<a id="r_gafeb5b968b14bba1968899d01fc73ac60"></a>

```c
#define BSP_CLOCKS_SOURCE_MOCODIV_CLK BSP_CLOCKS_SOURCE_CLOCK_MOCO
```

相关声明：[BSP_CLOCKS_SOURCE_MOCODIV_CLK](#gafeb5b968b14bba1968899d01fc73ac60)。

MOCODIV_CLK 时钟源（Clock Source）。

## 6.2\_详细说明（Detailed Documentation）

<a id="ga54275c8fca9740aeb84a78a9df958977"></a>

### `BSP_CLOCKS_SOURCE_HOCODIV_CLK`

```c
#define BSP_CLOCKS_SOURCE_HOCODIV_CLK BSP_CLOCKS_SOURCE_CLOCK_HOCO
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

HOCODIV_CLK 时钟源（Clock Source）。

<a id="gafeb5b968b14bba1968899d01fc73ac60"></a>

### `BSP_CLOCKS_SOURCE_MOCODIV_CLK`

```c
#define BSP_CLOCKS_SOURCE_MOCODIV_CLK BSP_CLOCKS_SOURCE_CLOCK_MOCO
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

MOCODIV_CLK 时钟源（Clock Source）。

<a id="gac6d940bf68229ce58e586d99e88021ad"></a>

### `BSP_CLOCKS_SOURCE_PLL`

```c
#define BSP_CLOCKS_SOURCE_PLL BSP_CLOCKS_SOURCE_CLOCK_PLL
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

PLL 锁相环时钟源（Clock Source）。

<a id="ga526d6007889c727bc820b23a8bd57eb1"></a>

### `BSP_CLOCKS_SOURCE_PLL2`

```c
#define BSP_CLOCKS_SOURCE_PLL2 BSP_CLOCKS_SOURCE_CLOCK_PLL2
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

PLL2 时钟源（Clock Source）。

<a id="ga7d74f3dc378453283c5a2752d261a635"></a>

### `BSP_CLOCKS_SOURCE_PLL2P`

```c
#define BSP_CLOCKS_SOURCE_PLL2P BSP_CLOCKS_SOURCE_CLOCK_PLL2
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

PLL2P 时钟源（Clock Source）。

<a id="gae21c8ebb5bfd4160ced33343517cf755"></a>

### `BSP_CLOCKS_SOURCE_PLL2Q`

```c
#define BSP_CLOCKS_SOURCE_PLL2Q BSP_CLOCKS_SOURCE_CLOCK_PLL2Q
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

PLL2Q 时钟源（Clock Source）。

<a id="ga2c9eb4860dc00767ec81567b7e1ef915"></a>

### `BSP_CLOCKS_SOURCE_PLL2R`

```c
#define BSP_CLOCKS_SOURCE_PLL2R BSP_CLOCKS_SOURCE_CLOCK_PLL2R
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

PLL2R 时钟源（Clock Source）。

<a id="ga80b3c5e721364e07c795d759e56bef5f"></a>

### `BSP_CLOCKS_SOURCE_PLLP`

```c
#define BSP_CLOCKS_SOURCE_PLLP BSP_CLOCKS_SOURCE_CLOCK_PLL
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

PLLP 时钟源（Clock Source）。

<a id="ga198180ae8a259e478c13cb667efdc036"></a>

### `BSP_CLOCKS_SOURCE_PLLQ`

```c
#define BSP_CLOCKS_SOURCE_PLLQ BSP_CLOCKS_SOURCE_CLOCK_PLL1Q
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

PLLQ 时钟源（Clock Source）。

<a id="ga9cf8b84320ad1c418e554c44d0ae324c"></a>

### `BSP_CLOCKS_SOURCE_PLLR`

```c
#define BSP_CLOCKS_SOURCE_PLLR BSP_CLOCKS_SOURCE_CLOCK_PLL1R
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

PLLR 时钟源（Clock Source）。

<a id="ga6e88996a2dba7df510f6f9c37d921abb"></a>

### `BSP_CLOCKS_SOURCE_XTALDIV_CLK`

```c
#define BSP_CLOCKS_SOURCE_XTALDIV_CLK BSP_CLOCKS_SOURCE_CLOCK_MAIN_OSC
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

XTALDIV_CLK 时钟源（Clock Source）。


## 6.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/renesas_ra_cgc.h](https://docs.zephyrproject.org/latest/doxygen/html/renesas__ra__cgc_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P005_健康服务器模型（Health Server Model）.md) · [返回大纲](大纲.md) · [下一章](P007_Arm通用中断控制器（GIC Interrupt Controller）.md)
