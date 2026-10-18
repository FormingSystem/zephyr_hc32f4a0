---
id: learning.zephyr-docs.api-file-interface-reference.page-49
title: zephyr__drivers__clock_control__renesas_rx_cgc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__cgc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第49章\_zephyr\_\_drivers\_\_clock\_control\_\_renesas\_rx\_cgc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__cgc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Renesas RX时钟发生电路（Clock Generator Circuit，CGC）的头文件。

<a id="details"></a>

```c
#include <zephyr/drivers/clock_control.h>
#include <zephyr/dt-bindings/clock/rx_clock.h>
```

查看此文件的源码。

Renesas RX时钟发生电路（Clock Generator Circuit，CGC）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 49.1\_数据结构（Data Structures）

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

## 49.2\_宏定义（Macros）

<a id="r_ga722b55a0a83757487eff84b93fe90964"></a>

```c
#define RX_CGC_PROP_HAS_STATUS_OKAY_OR(node_id, prop, default_value)
```

相关声明：[RX_CGC_PROP_HAS_STATUS_OKAY_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rx.html#ga722b55a0a83757487eff84b93fe90964)。

根据设备树状态（devicetree status）有条件地获取属性的辅助宏。

<a id="r_ga7a7b76c8c7318a073b4f43f72d1d412f"></a>

```c
#define RX_CGC_CLK_SRC(node_id)
```

相关声明：[RX_CGC_CLK_SRC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rx.html#ga7a7b76c8c7318a073b4f43f72d1d412f)。

从设备树获取时钟源（clock source）的辅助宏。

<a id="r_ga4baedac457dd6b7027af817fc1417710"></a>

```c
#define RX_IF_CLK_SRC(node_id)
```

相关声明：[RX_IF_CLK_SRC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rx.html#ga4baedac457dd6b7027af817fc1417710)。

从设备树获取 IF 时钟源的辅助宏。

<a id="r_gaa54af37a68c4a0855f750cdc39783954"></a>

```c
#define RX_LPT_CLK_SRC(node_id)
```

相关声明：[RX_LPT_CLK_SRC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rx.html#gaa54af37a68c4a0855f750cdc39783954)。

从设备树获取 LPT 时钟源的辅助宏。

<a id="r_gac82952f98470a18cee1f9f710a523fee"></a>

```c
#define RX_CGC_PLL_CLK_SRC(node_id)
```

相关声明：[RX_CGC_PLL_CLK_SRC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rx.html#gac82952f98470a18cee1f9f710a523fee)。

从设备树获取 PLL 时钟源的辅助宏。


## 49.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control.h](../timer_reference/P096_时钟控制完整头文件.md)
- [zephyr/dt-bindings/clock/rx_clock.h](../api_source_reference/P743_rx_clock.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P710_renesas_rx_cgc.h_源码浏览.md)
- [clock_control_rx_pclk_cfg](../clock_cmsis_model_reference/P003_clock_control_rx_pclk_cfg_结构体.md)
- [clock_control_rx_subsys_cfg](../clock_cmsis_model_reference/P007_clock_control_rx_subsys_cfg_结构体.md)
- [clock_control_rx_pll_cfg](../clock_cmsis_model_reference/P004_clock_control_rx_pll_cfg_结构体.md)
- [clock_control_rx_pll_data](../clock_cmsis_model_reference/P005_clock_control_rx_pll_data_结构体.md)
- [clock_control_rx_root_cfg](../clock_cmsis_model_reference/P006_clock_control_rx_root_cfg_结构体.md)
- [RX_CGC_PROP_HAS_STATUS_OKAY_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rx.html#ga722b55a0a83757487eff84b93fe90964)
- [RX_CGC_CLK_SRC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rx.html#ga7a7b76c8c7318a073b4f43f72d1d412f)
- [RX_IF_CLK_SRC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rx.html#ga4baedac457dd6b7027af817fc1417710)
- [RX_LPT_CLK_SRC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rx.html#gaa54af37a68c4a0855f750cdc39783954)
- [RX_CGC_PLL_CLK_SRC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rx.html#gac82952f98470a18cee1f9f710a523fee)

<a id="header-details"></a>

---

[上一章](P048_zephyr__dt-bindings__gpio__renesas-rz-gpio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P050_zephyr__drivers__clock_control__renesas_rz_cgc.h_文件参考.md)
