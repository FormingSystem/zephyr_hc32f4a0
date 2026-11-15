---
id: learning.zephyr-docs.api-protocol-topic-reference.page-12
title: 瑞萨（Renesas）RA 时钟生成电路（CGC）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_瑞萨（Renesas）RA 时钟生成电路（CGC）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-groups"></a>
<a id="groups"></a>

## 12.1\_主题（Topics）

<a id="r_clock_5Fcontrol_5Frenesas_5Fra_5Fclkout"></a>

相关声明：[瑞萨 RA BSP 时钟输出分频常量（Clock Clkout Divider Constants）](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__clkout.html)。

PCLK 时钟源（Clock source）

<a id="r_clock_5Fcontrol_5Frenesas_5Fra_5Fsource"></a>

相关声明：[瑞萨 RA BSP 时钟源常量（Clock Source Constants）](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__source.html)。

瑞萨 RA BSP 时钟源常量（Clock source constants）

<a id="r_clock_5Fcontrol_5Frenesas_5Fra_5Fdiv"></a>

相关声明：[瑞萨 RA 时钟分频生成器（Clock Divider Generators）](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html)。

面向多个时钟域（Clock domains）的分频生成宏。

<a id="header-files"></a>
<a id="files"></a>

## 12.2\_文件（Files）

<a id="r_renesas_5Fra_5Fcgc_2Eh"></a>

```c
file renesas_ra_cgc.h
```

相关声明：[renesas_ra_cgc.h](https://docs.zephyrproject.org/latest/doxygen/html/renesas__ra__cgc_8h.html)。

Renesas RA时钟发生电路（Clock Generator Circuit，CGC）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 12.3\_数据结构（Data Structures）

<a id="r_clock_5Fcontrol_5Fra_5Fpclk_5Fcfg"></a>

```c
struct clock_control_ra_pclk_cfg
```

相关声明：[clock_control_ra_pclk_cfg](../clock_cmsis_model_reference/P001_clock_control_ra_pclk_cfg_结构体.md)。

外设时钟配置（Peripheral Clock Configuration）。

<a id="r_clock_5Fcontrol_5Fra_5Fsubsys_5Fcfg"></a>

```c
struct clock_control_ra_subsys_cfg
```

相关声明：[clock_control_ra_subsys_cfg](../clock_cmsis_model_reference/P002_clock_control_ra_subsys_cfg_结构体.md)。

子系统时钟控制配置（Subsystem Clock Control Configuration）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 12.4\_宏定义（Macros）

<a id="r_ga69f75bb6ad2e7c3d22936754ba3bf5b5"></a>

```c
#define RA_CGC_PROP_HAS_STATUS_OKAY_OR(node_id, prop, default_value)
```

相关声明：[RA_CGC_PROP_HAS_STATUS_OKAY_OR](#ga69f75bb6ad2e7c3d22936754ba3bf5b5)。

根据设备树状态（devicetree status）有条件地获取属性的辅助宏。

<a id="r_ga45ba53a59830676d22f80b29165ae399"></a>

```c
#define RA_CGC_CLK_SRC(node_id)
```

相关声明：[RA_CGC_CLK_SRC](#ga45ba53a59830676d22f80b29165ae399)。

从设备树获取时钟源（clock source）的辅助宏。

<a id="r_gaf54cadef83174db1f2180c65fb436c28"></a>

```c
#define RA_CGC_CLK_DIV(clk, prop, default_value)
```

相关声明：[RA_CGC_CLK_DIV](#gaf54cadef83174db1f2180c65fb436c28)。

用于计算时钟分频值（clock divider）的辅助宏。

## 12.5\_详细说明（Detailed Documentation）

<a id="gaf54cadef83174db1f2180c65fb436c28"></a>

### `RA_CGC_CLK_DIV`

```c
#define RA_CGC_CLK_DIV ( clk, prop, default_value )
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
UTIL_CAT(RA_CGC_DIV_, DT_NODE_FULL_NAME_UPPER_TOKEN(clk))                                  \
(RA_CGC_PROP_HAS_STATUS_OKAY_OR(clk, prop, default_value))
```

用于计算时钟分频值（clock divider）的辅助宏。

此宏展开为将 `RA_CGC_DIV_*` 前缀与设备树值组合后得到的标识符。

<a id="ga45ba53a59830676d22f80b29165ae399"></a>

### `RA_CGC_CLK_SRC`

```c
#define RA_CGC_CLK_SRC ( node_id)
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
COND_CODE_1(DT_NODE_HAS_STATUS(node_id, okay), \
        (UTIL_CAT(BSP_CLOCKS_SOURCE_, DT_NODE_FULL_NAME_UPPER_TOKEN(node_id))), \
        (BSP_CLOCKS_CLOCK_DISABLED))
```

从设备树获取时钟源（clock source）的辅助宏。

节点启用时展开为 `BSP_CLOCKS_SOURCE_*` 常量，否则展开为 `BSP_CLOCKS_CLOCK_DISABLED`。

<a id="ga69f75bb6ad2e7c3d22936754ba3bf5b5"></a>

### `RA_CGC_PROP_HAS_STATUS_OKAY_OR`

```c
#define RA_CGC_PROP_HAS_STATUS_OKAY_OR ( node_id, prop, default_value )
```

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

展开值（Value）：

```c
COND_CODE_1(DT_NODE_HAS_STATUS(node_id, okay), \
        (DT_PROP(node_id, prop)), (default_value))
```

根据设备树状态（devicetree status）有条件地获取属性的辅助宏。

节点标为 `okay` 时，返回设备树属性值；否则使用所提供的默认值。


## 12.6\_原页交叉引用（Cross References）

- [瑞萨 RA BSP 时钟输出分频常量（Clock Clkout Divider Constants）](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__clkout.html)
- [瑞萨 RA BSP 时钟源常量（Clock Source Constants）](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__source.html)
- [瑞萨 RA 时钟分频生成器（Clock Divider Generators）](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__ra__div.html)
- [renesas_ra_cgc.h](https://docs.zephyrproject.org/latest/doxygen/html/renesas__ra__cgc_8h.html)
- [clock_control_ra_pclk_cfg](../clock_cmsis_model_reference/P001_clock_control_ra_pclk_cfg_结构体.md)
- [clock_control_ra_subsys_cfg](../clock_cmsis_model_reference/P002_clock_control_ra_subsys_cfg_结构体.md)
- [UTIL_CAT](../util_reference/P006_内部宏工具头文件参考.md#a7e7766e792d1638bfbbc9d0f328d3d0d)
- [DT_NODE_FULL_NAME_UPPER_TOKEN](../dt_identity_reference/P001_设备树节点标识宏.md#gab966ae50efe46cc3a54f086f508edb3b)
- [COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)
- [DT_NODE_HAS_STATUS](../dt_identity_reference/P002_设备树存在性与状态宏.md#ga3b769d8105c7679e1d0575a1e7f1f653)
- [DT_PROP](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__clock__control__renesas__ra_html_ga69f75bb6ad2e7c3d22936754ba3bf5b5"></a>
<a id="agroup__devicetree-generic-id_html_gab966ae50efe46cc3a54f086f508edb3b"></a>
<a id="autil__internal_8h_html_a7e7766e792d1638bfbbc9d0f328d3d0d"></a>
<a id="agroup__devicetree-generic-exist_html_ga3b769d8105c7679e1d0575a1e7f1f653"></a>
<a id="agroup__sys-util_html_ga358bc3e7669c860a98839a51cd526b20"></a>
<a id="agroup__devicetree-generic-prop_html_ga8e1fd9ebacd85d2013df027d041d506b"></a>

---

[上一章](P011_乐鑫（Espressif）ESP32.md) · [返回大纲](大纲.md) · [下一章](P013_瑞萨（Renesas）RX 时钟生成电路（CGC）.md)
