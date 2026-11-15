---
id: learning.zephyr-docs.clock-cmsis-model-reference.page-13
title: clock_mchp_subsys_gclkgen_config_结构体
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structclock__mchp__subsys__gclkgen__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_clock\_mchp\_subsys\_gclkgen\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structclock__mchp__subsys__gclkgen__config.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

通用时钟发生器（GCLK Generator）配置结构体。

```c
#include <zephyr/drivers/clock_control/mchp_clock_pic32ck_sg_gc.h>
```

<a id="details"></a>

通用时钟发生器（GCLK Generator）配置结构体，用于 GCLK 发生器配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 13.1\_数据成员（Data Fields）

<a id="r_af803dcb746c1438f6e08ac30042d3651"></a>

```c
uint16_t div_factor
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[div_factor](#af803dcb746c1438f6e08ac30042d3651)。

表示相应发生器的分频值。

<a id="r_a59f3f908c254d4299164b5fea5885514"></a>

```c
bool run_in_standby_en
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[run_in_standby_en](#a59f3f908c254d4299164b5fea5885514)。

配置振荡器在待机睡眠模式中开启，除非设置了 `on_demand_en`。

<a id="r_aeb553aa051490aefb8d38cc9ce7e8166"></a>

```c
enum clock_mchp_gclk_src_clock src
```

相关声明：[clock_mchp_gclk_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ga073dab68c78edce3985eb201a039a989)、[src](#aeb553aa051490aefb8d38cc9ce7e8166)。

发生器源时钟选择（Generator Source Clock Selection）。

## 13.2\_详细说明（Detailed Documentation）

<a id="af803dcb746c1438f6e08ac30042d3651"></a>

### `div_factor`

```c
uint16_t clock_mchp_subsys_gclkgen_config::div_factor
```

表示相应发生器的分频值。

发生器的分频值。

实际分频因子取决于 `div_select` 的状态，`gclk1` 范围为 0–65535，其他发生器为 0–255。

实际分频因子取决于 `div_select` 的状态，`gclk1` 范围为 0–65535，其他发生器为 0–255。

<a id="a59f3f908c254d4299164b5fea5885514"></a>

### `run_in_standby_en`

```c
bool clock_mchp_subsys_gclkgen_config::run_in_standby_en
```

配置振荡器在待机睡眠模式中开启，除非设置了 `on_demand_en`。

在待机睡眠模式中保持发生器运行，除非设置了 `on_demand_en`。

<a id="aeb553aa051490aefb8d38cc9ce7e8166"></a>

### `src`

```c
enum clock_mchp_gclk_src_clock clock_mchp_subsys_gclkgen_config::src
```

发生器源时钟选择（Generator Source Clock Selection）。

本结构体文档由以下文件生成：

- `zephyr/drivers/clock_control/mchp_clock_pic32ck_sg_gc.h`
- `zephyr/drivers/clock_control/mchp_clock_pic32cm_jh.h`
- `zephyr/drivers/clock_control/mchp_clock_pic32cm_sg_gc.h`
- `zephyr/drivers/clock_control/mchp_clock_pic32cz_ca.h`
- `zephyr/drivers/clock_control/mchp_clock_sam_d5x_e5x.h`

## 13.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/mchp_clock_pic32ck_sg_gc.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [clock_mchp_gclk_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ga073dab68c78edce3985eb201a039a989)
- [mchp_clock_pic32cm_jh.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__jh_8h_source.html)
- [mchp_clock_pic32cm_sg_gc.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__sg__gc_8h_source.html)
- [mchp_clock_pic32cz_ca.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cz__ca_8h_source.html)
- [mchp_clock_sam_d5x_e5x.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__sam__d5x__e5x_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P012_clock_mchp_subsys_fdpll_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P014_clock_mchp_subsys_gclkperiph_config_结构体.md)
