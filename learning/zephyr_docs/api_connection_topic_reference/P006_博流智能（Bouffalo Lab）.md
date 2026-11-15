---
id: learning.zephyr-docs.api-connection-topic-reference.page-6
title: 博流智能（Bouffalo Lab）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__bflb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_博流智能（Bouffalo Lab）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__bflb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 6.1\_文件（Files）

<a id="r_clock_5Fcontrol_5Fbflb_5Fcommon_2Eh"></a>

```c
file clock_control_bflb_common.h
```

相关声明：[clock_control_bflb_common.h](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__bflb__common_8h.html)。

全部Bouffalo Lab平台通用的时序与时钟辅助接口（Timing and Clock Helpers）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.2\_函数（Functions）

<a id="r_ga56da89547422c68d755cae71ebc8213e"></a>

```c
static void clock_bflb_settle (void)
```

相关声明：[clock_bflb_settle](#ga56da89547422c68d755cae71ebc8213e)。

忙等待（busy-wait）几个 CPU 周期，让时钟变化稳定下来。

<a id="r_gad8f2fcc97e98aad258410a97880abcfb"></a>

```c
static void clock_bflb_set_root_clock (uint32_t clock)
```

相关声明：[clock_bflb_set_root_clock](#gad8f2fcc97e98aad258410a97880abcfb)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

选择根时钟，即主时钟（root/main clock）的时钟源。

<a id="r_ga3f2549b3d7feb0693b140760fc5e7975"></a>

```c
static uint32_t clock_bflb_get_root_clock (void)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[clock_bflb_get_root_clock](#ga3f2549b3d7feb0693b140760fc5e7975)。

获取当前选择的根时钟（主时钟）源。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 6.3\_主时钟多路选择器选项（Main clock mux selections，参见 clock_bflb_set_root_clock()）

<a id="r_ga62631545e2b11958a758dd19b0b585a9"></a>

```c
#define BFLB_MAIN_CLOCK_RC32M 0
```

相关声明：[BFLB_MAIN_CLOCK_RC32M](#ga62631545e2b11958a758dd19b0b585a9)。

XCLK 为 RC32M，主时钟为 XCLK。

<a id="r_ga2a346b6b40fbe61a7eccc805da79f2c2"></a>

```c
#define BFLB_MAIN_CLOCK_XTAL 1
```

相关声明：[BFLB_MAIN_CLOCK_XTAL](#ga2a346b6b40fbe61a7eccc805da79f2c2)。

XCLK 为晶体时钟（crystal），主时钟为 XCLK。

<a id="r_ga13d8cc22719f66c29680bedbe0897c45"></a>

```c
#define BFLB_MAIN_CLOCK_PLL_RC32M 2
```

相关声明：[BFLB_MAIN_CLOCK_PLL_RC32M](#ga13d8cc22719f66c29680bedbe0897c45)。

XCLK 为 RC32M，主时钟为锁相环（PLL）时钟。

<a id="r_ga8d56227817defb1b5d442b499ad5a0aa"></a>

```c
#define BFLB_MAIN_CLOCK_PLL_XTAL 3
```

相关声明：[BFLB_MAIN_CLOCK_PLL_XTAL](#ga8d56227817defb1b5d442b499ad5a0aa)。

XCLK 为晶体时钟，主时钟为 PLL 时钟。

## 6.4\_详细说明（Detailed Documentation）

<a id="ga13d8cc22719f66c29680bedbe0897c45"></a>

### `BFLB_MAIN_CLOCK_PLL_RC32M`

```c
#define BFLB_MAIN_CLOCK_PLL_RC32M 2
```

```c
#include <zephyr/drivers/clock_control/clock_control_bflb_common.h>
```

XCLK 为 RC32M，主时钟为锁相环（PLL）时钟。

<a id="ga8d56227817defb1b5d442b499ad5a0aa"></a>

### `BFLB_MAIN_CLOCK_PLL_XTAL`

```c
#define BFLB_MAIN_CLOCK_PLL_XTAL 3
```

```c
#include <zephyr/drivers/clock_control/clock_control_bflb_common.h>
```

XCLK 为晶体时钟，主时钟为 PLL 时钟。

<a id="ga62631545e2b11958a758dd19b0b585a9"></a>

### `BFLB_MAIN_CLOCK_RC32M`

```c
#define BFLB_MAIN_CLOCK_RC32M 0
```

```c
#include <zephyr/drivers/clock_control/clock_control_bflb_common.h>
```

XCLK 为 RC32M，主时钟为 XCLK。

<a id="ga2a346b6b40fbe61a7eccc805da79f2c2"></a>

### `BFLB_MAIN_CLOCK_XTAL`

```c
#define BFLB_MAIN_CLOCK_XTAL 1
```

```c
#include <zephyr/drivers/clock_control/clock_control_bflb_common.h>
```

XCLK 为晶体时钟（crystal），主时钟为 XCLK。

<a id="ga3f2549b3d7feb0693b140760fc5e7975"></a>

### `clock_bflb_get_root_clock()`

```c
uint32_t clock_bflb_get_root_clock ( void )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/clock_control/clock_control_bflb_common.h>
```

获取当前选择的根时钟（主时钟）源。

**返回（Returns）**：返回值：某个 `BFLB_MAIN_CLOCK_*` 选择项。

<a id="gad8f2fcc97e98aad258410a97880abcfb"></a>

### `clock_bflb_set_root_clock()`

```c
void clock_bflb_set_root_clock ( uint32_t clock)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/clock_control/clock_control_bflb_common.h>
```

选择根时钟，即主时钟（root/main clock）的时钟源。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `clock` | 某个 `BFLB_MAIN_CLOCK_*` 选择项。超出范围的值回退到 `BFLB_MAIN_CLOCK_RC32M`。 |

<a id="ga56da89547422c68d755cae71ebc8213e"></a>

### `clock_bflb_settle()`

```c
void clock_bflb_settle ( void )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/clock_control/clock_control_bflb_common.h>
```

忙等待（busy-wait）几个 CPU 周期，让时钟变化稳定下来。


## 6.5\_原页交叉引用（Cross References）

- [clock_control_bflb_common.h](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__bflb__common_8h.html)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P005_蓝牙 Mesh 二进制大对象（BLOB）传输服务器模型 API.md) · [返回大纲](大纲.md) · [下一章](P007_瑞萨 RA BSP 时钟输出分频常量（Clock Clkout Divider Constants）.md)
