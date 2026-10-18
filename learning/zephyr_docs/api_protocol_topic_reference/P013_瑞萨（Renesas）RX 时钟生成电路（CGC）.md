---
id: learning.zephyr-docs.api-protocol-topic-reference.page-13
title: 瑞萨（Renesas）RX 时钟生成电路（CGC）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_瑞萨（Renesas）RX 时钟生成电路（CGC）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rx.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 13.1\_文件（Files）

<a id="r_renesas_5Frx_5Fcgc_2Eh"></a>

```c
file renesas_rx_cgc.h
```

相关声明：[renesas_rx_cgc.h](../api_file_interface_reference/P049_zephyr__drivers__clock_control__renesas_rx_cgc.h_文件参考.md)。

Renesas RX时钟发生电路（Clock Generator Circuit，CGC）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 13.2\_数据结构（Data Structures）

<a id="r_clock_5Fcontrol_5Frx_5Fpclk_5Fcfg"></a>

```c
struct clock_control_rx_pclk_cfg
```

相关声明：[clock_control_rx_pclk_cfg](../clock_cmsis_model_reference/P003_clock_control_rx_pclk_cfg_结构体.md)。

外设时钟（PCLK）配置。

<a id="r_clock_5Fcontrol_5Frx_5Fsubsys_5Fcfg"></a>

```c
struct clock_control_rx_subsys_cfg
```

相关声明：[clock_control_rx_subsys_cfg](../clock_cmsis_model_reference/P007_clock_control_rx_subsys_cfg_结构体.md)。

子系统时钟控制配置（Subsystem Clock Control Configuration）。

<a id="r_clock_5Fcontrol_5Frx_5Fpll_5Fcfg"></a>

```c
struct clock_control_rx_pll_cfg
```

相关声明：[clock_control_rx_pll_cfg](../clock_cmsis_model_reference/P004_clock_control_rx_pll_cfg_结构体.md)。

锁相环（Phase-Locked Loop，PLL）配置结构体。

<a id="r_clock_5Fcontrol_5Frx_5Fpll_5Fdata"></a>

```c
struct clock_control_rx_pll_data
```

相关声明：[clock_control_rx_pll_data](../clock_cmsis_model_reference/P005_clock_control_rx_pll_data_结构体.md)。

PLL 控制参数。

<a id="r_clock_5Fcontrol_5Frx_5Froot_5Fcfg"></a>

```c
struct clock_control_rx_root_cfg
```

相关声明：[clock_control_rx_root_cfg](../clock_cmsis_model_reference/P006_clock_control_rx_root_cfg_结构体.md)。

根时钟配置（Root Clock Configuration）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 13.3\_宏定义（Macros）

<a id="r_ga722b55a0a83757487eff84b93fe90964"></a>

```c
#define RX_CGC_PROP_HAS_STATUS_OKAY_OR(node_id, prop, default_value)
```

相关声明：[RX_CGC_PROP_HAS_STATUS_OKAY_OR](#ga722b55a0a83757487eff84b93fe90964)。

根据设备树状态（devicetree status）有条件地获取属性的辅助宏。

<a id="r_ga7a7b76c8c7318a073b4f43f72d1d412f"></a>

```c
#define RX_CGC_CLK_SRC(node_id)
```

相关声明：[RX_CGC_CLK_SRC](#ga7a7b76c8c7318a073b4f43f72d1d412f)。

从设备树获取时钟源（clock source）的辅助宏。

<a id="r_ga4baedac457dd6b7027af817fc1417710"></a>

```c
#define RX_IF_CLK_SRC(node_id)
```

相关声明：[RX_IF_CLK_SRC](#ga4baedac457dd6b7027af817fc1417710)。

从设备树获取 IF 时钟源的辅助宏。

<a id="r_gaa54af37a68c4a0855f750cdc39783954"></a>

```c
#define RX_LPT_CLK_SRC(node_id)
```

相关声明：[RX_LPT_CLK_SRC](#gaa54af37a68c4a0855f750cdc39783954)。

从设备树获取 LPT 时钟源的辅助宏。

<a id="r_gac82952f98470a18cee1f9f710a523fee"></a>

```c
#define RX_CGC_PLL_CLK_SRC(node_id)
```

相关声明：[RX_CGC_PLL_CLK_SRC](#gac82952f98470a18cee1f9f710a523fee)。

从设备树获取 PLL 时钟源的辅助宏。

## 13.4\_详细说明（Detailed Documentation）

<a id="ga7a7b76c8c7318a073b4f43f72d1d412f"></a>

### `RX_CGC_CLK_SRC`

```c
#define RX_CGC_CLK_SRC ( node_id)
```

```c
#include <zephyr/drivers/clock_control/renesas_rx_cgc.h>
```

展开值（Value）：

```c
COND_CODE_1(DT_NODE_HAS_STATUS(node_id, okay),                                             \
            (UTIL_CAT(RX_CLOCKS_SOURCE_, DT_NODE_FULL_NAME_UPPER_TOKEN(node_id))),        \
            (RX_CLOCKS_CLOCK_DISABLED))
```

从设备树获取时钟源（clock source）的辅助宏。

节点启用时展开为 `RX_CLOCKS_SOURCE_*` 常量，否则展开为 `RX_CLOCKS_CLOCK_DISABLED`。

<a id="gac82952f98470a18cee1f9f710a523fee"></a>

### `RX_CGC_PLL_CLK_SRC`

```c
#define RX_CGC_PLL_CLK_SRC ( node_id)
```

```c
#include <zephyr/drivers/clock_control/renesas_rx_cgc.h>
```

展开值（Value）：

```c
COND_CODE_1(DT_NODE_HAS_STATUS(node_id, okay),                                             \
        (UTIL_CAT(RX_PLL_CLOCKS_SOURCE_, DT_NODE_FULL_NAME_UPPER_TOKEN(node_id))),        \
            (RX_CLOCKS_CLOCK_DISABLED))
```

从设备树获取 PLL 时钟源的辅助宏。

节点启用时展开为 `RX_PLL_CLOCKS_SOURCE_*` 常量，否则展开为 `RX_CLOCKS_CLOCK_DISABLED`。

<a id="ga722b55a0a83757487eff84b93fe90964"></a>

### `RX_CGC_PROP_HAS_STATUS_OKAY_OR`

```c
#define RX_CGC_PROP_HAS_STATUS_OKAY_OR ( node_id, prop, default_value )
```

```c
#include <zephyr/drivers/clock_control/renesas_rx_cgc.h>
```

展开值（Value）：

```c
COND_CODE_1(DT_NODE_HAS_STATUS(node_id, okay), (DT_PROP(node_id, prop)),                   \
            (default_value))
```

根据设备树状态（devicetree status）有条件地获取属性的辅助宏。

节点标为 `okay` 时，返回设备树属性值；否则使用所提供的默认值。

<a id="ga4baedac457dd6b7027af817fc1417710"></a>

### `RX_IF_CLK_SRC`

```c
#define RX_IF_CLK_SRC ( node_id)
```

```c
#include <zephyr/drivers/clock_control/renesas_rx_cgc.h>
```

展开值（Value）：

```c
COND_CODE_1(DT_NODE_HAS_STATUS(node_id, okay),\
                (UTIL_CAT(RX_IF_CLOCKS_SOURCE_, DT_NODE_FULL_NAME_UPPER_TOKEN(node_id))),\
                (RX_CLOCKS_CLOCK_DISABLED))
```

从设备树获取 IF 时钟源的辅助宏。

节点启用时展开为 `RX_IF_CLOCKS_SOURCE_*` 常量，否则展开为 `RX_CLOCKS_CLOCK_DISABLED`。

<a id="gaa54af37a68c4a0855f750cdc39783954"></a>

### `RX_LPT_CLK_SRC`

```c
#define RX_LPT_CLK_SRC ( node_id)
```

```c
#include <zephyr/drivers/clock_control/renesas_rx_cgc.h>
```

展开值（Value）：

```c
COND_CODE_1(DT_NODE_HAS_STATUS(node_id, okay),\
                (UTIL_CAT(RX_LPT_CLOCKS_SOURCE_, DT_NODE_FULL_NAME_UPPER_TOKEN(node_id))),\
                (RX_LPT_CLOCKS_NON_USE))
```

从设备树获取 LPT 时钟源的辅助宏。

节点启用时展开为 `RX_LPT_CLOCKS_SOURCE_*` 常量，否则展开为 `RX_LPT_CLOCKS_NON_USE`。


## 13.5\_原页交叉引用（Cross References）

- [renesas_rx_cgc.h](../api_file_interface_reference/P049_zephyr__drivers__clock_control__renesas_rx_cgc.h_文件参考.md)
- [clock_control_rx_pclk_cfg](../clock_cmsis_model_reference/P003_clock_control_rx_pclk_cfg_结构体.md)
- [clock_control_rx_subsys_cfg](../clock_cmsis_model_reference/P007_clock_control_rx_subsys_cfg_结构体.md)
- [clock_control_rx_pll_cfg](../clock_cmsis_model_reference/P004_clock_control_rx_pll_cfg_结构体.md)
- [clock_control_rx_pll_data](../clock_cmsis_model_reference/P005_clock_control_rx_pll_data_结构体.md)
- [clock_control_rx_root_cfg](../clock_cmsis_model_reference/P006_clock_control_rx_root_cfg_结构体.md)
- [COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)
- [DT_NODE_HAS_STATUS](../dt_identity_reference/P002_设备树存在性与状态宏.md#ga3b769d8105c7679e1d0575a1e7f1f653)
- [UTIL_CAT](../util_reference/P006_内部宏工具头文件参考.md#a7e7766e792d1638bfbbc9d0f328d3d0d)
- [DT_NODE_FULL_NAME_UPPER_TOKEN](../dt_identity_reference/P001_设备树节点标识宏.md#gab966ae50efe46cc3a54f086f508edb3b)
- [DT_PROP](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b)
- [RX_LPT_CLOCKS_NON_USE](https://docs.zephyrproject.org/latest/doxygen/html/rx__clock_8h.html#a7fd495dac366a61bfe65314a616982d5)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__devicetree-generic-exist_html_ga3b769d8105c7679e1d0575a1e7f1f653"></a>
<a id="agroup__devicetree-generic-id_html_gab966ae50efe46cc3a54f086f508edb3b"></a>
<a id="agroup__sys-util_html_ga358bc3e7669c860a98839a51cd526b20"></a>
<a id="autil__internal_8h_html_a7e7766e792d1638bfbbc9d0f328d3d0d"></a>
<a id="agroup__devicetree-generic-prop_html_ga8e1fd9ebacd85d2013df027d041d506b"></a>
<a id="arx__clock_8h_html_a7fd495dac366a61bfe65314a616982d5"></a>

---

[上一章](P012_瑞萨（Renesas）RA 时钟生成电路（CGC）.md) · [返回大纲](大纲.md) · [下一章](P014_瑞萨（Renesas）RZ 时钟生成电路（CGC）.md)
