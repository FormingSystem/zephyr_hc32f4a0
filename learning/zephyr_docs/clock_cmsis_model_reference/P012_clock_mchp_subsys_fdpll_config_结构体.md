---
id: learning.zephyr-docs.clock-cmsis-model-reference.page-12
title: clock_mchp_subsys_fdpll_config_结构体
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structclock__mchp__subsys__fdpll__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_clock\_mchp\_subsys\_fdpll\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structclock__mchp__subsys__fdpll__config.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

分数数字锁相环（Fractional DPLL，FDPLL）配置。

```c
#include <zephyr/drivers/clock_control/mchp_clock_pic32cm_jh.h>
```

<a id="details"></a>

分数数字锁相环（Fractional DPLL，FDPLL）配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 12.1\_数据成员（Data Fields）

<a id="r_a1ae355aede60d06e8ae395517ba5f7cd"></a>

```c
bool on_demand_en
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[on_demand_en](#a1ae355aede60d06e8ae395517ba5f7cd)。

外设请求将振荡器用作时钟源时开启振荡器。

<a id="r_aa3e53c57298528f9033e08cc238f6891"></a>

```c
bool run_in_standby_en
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[run_in_standby_en](#aa3e53c57298528f9033e08cc238f6891)。

在待机睡眠模式（Standby Sleep Mode）中保持振荡器开启，除非设置了 `on_demand_en`。

<a id="r_aa081dea6b720e1bf79c4eb1ba139c664"></a>

```c
uint32_t divider_ratio_frac
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[divider_ratio_frac](#aa081dea6b720e1bf79c4eb1ba139c664)。

倍频因子的小数部分，范围为 0–31。

<a id="r_a763e54cbab07657be8eff1b8ca45f65e"></a>

```c
uint32_t divider_ratio_int
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[divider_ratio_int](#a763e54cbab07657be8eff1b8ca45f65e)。

倍频因子的整数部分，范围为 0–4095。

<a id="r_a24bc48331e32436c8f6c2cf3c76e7ed5"></a>

```c
uint32_t xosc_clock_divider
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[xosc_clock_divider](#a24bc48331e32436c8f6c2cf3c76e7ed5)。

外部振荡器（XOSC）的时钟分频因子，范围为 0–2047。

<a id="r_a8057b8d7233e11008eb81f798083ad6a"></a>

```c
enum clock_mchp_fdpll_src_clock src
```

相关声明：[clock_mchp_fdpll_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gaca271f1fae614cbd8c12fed31bcb64ea)、[src](#a8057b8d7233e11008eb81f798083ad6a)。

参考源时钟选择（Reference Source Clock Selection）。

## 12.2\_详细说明（Detailed Documentation）

<a id="aa081dea6b720e1bf79c4eb1ba139c664"></a>

### `divider_ratio_frac`

```c
uint32_t clock_mchp_subsys_fdpll_config::divider_ratio_frac
```

倍频因子的小数部分，范围为 0–31。

<a id="a763e54cbab07657be8eff1b8ca45f65e"></a>

### `divider_ratio_int`

```c
uint32_t clock_mchp_subsys_fdpll_config::divider_ratio_int
```

倍频因子的整数部分，范围为 0–4095。

<a id="a1ae355aede60d06e8ae395517ba5f7cd"></a>

### `on_demand_en`

```c
bool clock_mchp_subsys_fdpll_config::on_demand_en
```

外设请求将振荡器用作时钟源时开启振荡器。

<a id="aa3e53c57298528f9033e08cc238f6891"></a>

### `run_in_standby_en`

```c
bool clock_mchp_subsys_fdpll_config::run_in_standby_en
```

在待机睡眠模式（Standby Sleep Mode）中保持振荡器开启，除非设置了 `on_demand_en`。

<a id="a8057b8d7233e11008eb81f798083ad6a"></a>

### `src`

```c
enum clock_mchp_fdpll_src_clock clock_mchp_subsys_fdpll_config::src
```

参考源时钟选择（Reference Source Clock Selection）。

<a id="a24bc48331e32436c8f6c2cf3c76e7ed5"></a>

### `xosc_clock_divider`

```c
uint32_t clock_mchp_subsys_fdpll_config::xosc_clock_divider
```

外部振荡器（XOSC）的时钟分频因子，范围为 0–2047。

本结构体文档由以下文件生成：

- `zephyr/drivers/clock_control/mchp_clock_pic32cm_jh.h`
- `zephyr/drivers/clock_control/mchp_clock_sam_d5x_e5x.h`

## 12.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/mchp_clock_pic32cm_jh.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__jh_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [clock_mchp_fdpll_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gaca271f1fae614cbd8c12fed31bcb64ea)
- [mchp_clock_sam_d5x_e5x.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__sam__d5x__e5x_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P011_clock_mchp_subsys_dpll_out_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P013_clock_mchp_subsys_gclkgen_config_结构体.md)
