---
id: learning.zephyr-docs.clock-cmsis-model-reference.page-9
title: clock_mchp_subsys_dfll_config_结构体
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structclock__mchp__subsys__dfll__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_clock\_mchp\_subsys\_dfll\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structclock__mchp__subsys__dfll__config.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

DFLL 配置。

```c
#include <zephyr/drivers/clock_control/mchp_clock_sam_d5x_e5x.h>
```

<a id="details"></a>

DFLL 配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 9.1\_数据成员（Data Fields）

<a id="r_a82009cb6dd73ac71ed33b922536c62af"></a>

```c
bool on_demand_en
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[on_demand_en](#a82009cb6dd73ac71ed33b922536c62af)。

外设请求将振荡器用作时钟源时开启振荡器。

<a id="r_aba5aeb453d8cb5435ed26a154978bf75"></a>

```c
bool run_in_standby_en
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[run_in_standby_en](#aba5aeb453d8cb5435ed26a154978bf75)。

在待机睡眠模式（Standby Sleep Mode）中保持振荡器开启，除非设置了 `on_demand_en`。

<a id="r_af408de6428cffa98eacbefb37e85a2df"></a>

```c
bool closed_loop_en
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[closed_loop_en](#af408de6428cffa98eacbefb37e85a2df)。

启用闭环运行（Closed-loop Operation）。

<a id="r_aff185473ccf2ad46f4008e75c4f4b839"></a>

```c
enum clock_mchp_gclkgen src
```

相关声明：[clock_mchp_gclkgen](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gaab34442b0d6c171691ae299675542777)、[src](#aff185473ccf2ad46f4008e75c4f4b839)。

参考源时钟选择（Reference Source Clock Selection）。

<a id="r_ad38dd89aa8d1b1a7aa7889bdd5c6f058"></a>

```c
uint32_t multiply_factor
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[multiply_factor](#ad38dd89aa8d1b1a7aa7889bdd5c6f058)。

`CLK_DFLL` 输出频率与 `CLK_DFLL_REF` 输入频率的比值，范围为 0–65535。

## 9.2\_详细说明（Detailed Documentation）

<a id="af408de6428cffa98eacbefb37e85a2df"></a>

### `closed_loop_en`

```c
bool clock_mchp_subsys_dfll_config::closed_loop_en
```

启用闭环运行（Closed-loop Operation）。

<a id="ad38dd89aa8d1b1a7aa7889bdd5c6f058"></a>

### `multiply_factor`

```c
uint32_t clock_mchp_subsys_dfll_config::multiply_factor
```

`CLK_DFLL` 输出频率与 `CLK_DFLL_REF` 输入频率的比值，范围为 0–65535。

<a id="a82009cb6dd73ac71ed33b922536c62af"></a>

### `on_demand_en`

```c
bool clock_mchp_subsys_dfll_config::on_demand_en
```

外设请求将振荡器用作时钟源时开启振荡器。

<a id="aba5aeb453d8cb5435ed26a154978bf75"></a>

### `run_in_standby_en`

```c
bool clock_mchp_subsys_dfll_config::run_in_standby_en
```

在待机睡眠模式（Standby Sleep Mode）中保持振荡器开启，除非设置了 `on_demand_en`。

<a id="aff185473ccf2ad46f4008e75c4f4b839"></a>

### `src`

```c
enum clock_mchp_gclkgen clock_mchp_subsys_dfll_config::src
```

参考源时钟选择（Reference Source Clock Selection）。

本结构体文档由以下文件生成：

- `zephyr/drivers/clock_control/mchp_clock_sam_d5x_e5x.h`

## 9.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/mchp_clock_sam_d5x_e5x.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__sam__d5x__e5x_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [clock_mchp_gclkgen](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gaab34442b0d6c171691ae299675542777)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P008_clock_mchp_subsys_dfll48m_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P010_clock_mchp_subsys_dpll_config_结构体.md)
