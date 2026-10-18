---
id: learning.zephyr-docs.api-file-system-device-reference.page-5
title: zephyr__drivers__clock_control__clock_control_bflb_common.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/clock__control__bflb__common_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_drivers\_\_clock\_control\_\_clock\_control\_bflb\_common.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__bflb__common_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

全部Bouffalo Lab平台通用的时序与时钟辅助接口（Timing and Clock Helpers）。

查看此文件的源码。

<a id="details"></a>

全部Bouffalo Lab平台通用的时序与时钟辅助接口（Timing and Clock Helpers）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 主时钟多路选择器选项（Main clock mux selections，参见 clock_bflb_set_root_clock()）

<a id="r_ga62631545e2b11958a758dd19b0b585a9"></a>

```c
#define BFLB_MAIN_CLOCK_RC32M 0
```

相关声明：[BFLB_MAIN_CLOCK_RC32M](../api_connection_topic_reference/P006_博流智能（Bouffalo Lab）.md#ga62631545e2b11958a758dd19b0b585a9)。

XCLK 为 RC32M，主时钟为 XCLK。

<a id="r_ga2a346b6b40fbe61a7eccc805da79f2c2"></a>

```c
#define BFLB_MAIN_CLOCK_XTAL 1
```

相关声明：[BFLB_MAIN_CLOCK_XTAL](../api_connection_topic_reference/P006_博流智能（Bouffalo Lab）.md#ga2a346b6b40fbe61a7eccc805da79f2c2)。

XCLK 为晶体时钟（crystal），主时钟为 XCLK。

<a id="r_ga13d8cc22719f66c29680bedbe0897c45"></a>

```c
#define BFLB_MAIN_CLOCK_PLL_RC32M 2
```

相关声明：[BFLB_MAIN_CLOCK_PLL_RC32M](../api_connection_topic_reference/P006_博流智能（Bouffalo Lab）.md#ga13d8cc22719f66c29680bedbe0897c45)。

XCLK 为 RC32M，主时钟为锁相环（PLL）时钟。

<a id="r_ga8d56227817defb1b5d442b499ad5a0aa"></a>

```c
#define BFLB_MAIN_CLOCK_PLL_XTAL 3
```

相关声明：[BFLB_MAIN_CLOCK_PLL_XTAL](../api_connection_topic_reference/P006_博流智能（Bouffalo Lab）.md#ga8d56227817defb1b5d442b499ad5a0aa)。

XCLK 为晶体时钟，主时钟为 PLL 时钟。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.2\_函数（Functions）

<a id="r_ga56da89547422c68d755cae71ebc8213e"></a>

```c
static void clock_bflb_settle (void)
```

相关声明：[clock_bflb_settle](../api_connection_topic_reference/P006_博流智能（Bouffalo Lab）.md#ga56da89547422c68d755cae71ebc8213e)。

忙等待（busy-wait）几个 CPU 周期，让时钟变化稳定下来。

<a id="r_gad8f2fcc97e98aad258410a97880abcfb"></a>

```c
static void clock_bflb_set_root_clock (uint32_t clock)
```

相关声明：[clock_bflb_set_root_clock](../api_connection_topic_reference/P006_博流智能（Bouffalo Lab）.md#gad8f2fcc97e98aad258410a97880abcfb)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

选择根时钟，即主时钟（root/main clock）的时钟源。

<a id="r_ga3f2549b3d7feb0693b140760fc5e7975"></a>

```c
static uint32_t clock_bflb_get_root_clock (void)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[clock_bflb_get_root_clock](../api_connection_topic_reference/P006_博流智能（Bouffalo Lab）.md#ga3f2549b3d7feb0693b140760fc5e7975)。

获取当前选择的根时钟（主时钟）源。


## 5.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_device_reference/P003_clock_control_bflb_common.h_源码浏览.md)
- [BFLB_MAIN_CLOCK_RC32M](../api_connection_topic_reference/P006_博流智能（Bouffalo Lab）.md#ga62631545e2b11958a758dd19b0b585a9)
- [BFLB_MAIN_CLOCK_XTAL](../api_connection_topic_reference/P006_博流智能（Bouffalo Lab）.md#ga2a346b6b40fbe61a7eccc805da79f2c2)
- [BFLB_MAIN_CLOCK_PLL_RC32M](../api_connection_topic_reference/P006_博流智能（Bouffalo Lab）.md#ga13d8cc22719f66c29680bedbe0897c45)
- [BFLB_MAIN_CLOCK_PLL_XTAL](../api_connection_topic_reference/P006_博流智能（Bouffalo Lab）.md#ga8d56227817defb1b5d442b499ad5a0aa)
- [clock_bflb_settle](../api_connection_topic_reference/P006_博流智能（Bouffalo Lab）.md#ga56da89547422c68d755cae71ebc8213e)
- [clock_bflb_set_root_clock](../api_connection_topic_reference/P006_博流智能（Bouffalo Lab）.md#gad8f2fcc97e98aad258410a97880abcfb)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [clock_bflb_get_root_clock](../api_connection_topic_reference/P006_博流智能（Bouffalo Lab）.md#ga3f2549b3d7feb0693b140760fc5e7975)

<a id="header-details"></a>

---

[上一章](P004_zephyr__dt-bindings__sensor__bq274xx.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__dt-bindings__input__cst8xx-gesture-codes.h_文件参考.md)
