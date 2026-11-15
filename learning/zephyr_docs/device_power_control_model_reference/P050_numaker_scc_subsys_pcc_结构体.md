---
id: learning.zephyr-docs.device-power-control-model-reference.page-50
title: numaker_scc_subsys_pcc_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnumaker__scc__subsys__pcc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第50章\_numaker\_scc\_subsys\_pcc\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnumaker__scc__subsys__pcc.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

外设时钟控制配置（Peripheral Clock Control Configuration）。

```c
#include <zephyr/drivers/clock_control/clock_control_numaker.h>
```

<a id="details"></a>

外设时钟控制配置（Peripheral Clock Control Configuration）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 50.1\_数据成员（Data Fields）

<a id="r_a4ebf5a91a803cd92f10d25fcdd0c0eeb"></a>

```c
uint32_t clk_modidx
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clk_modidx](#a4ebf5a91a803cd92f10d25fcdd0c0eeb)。

模块索引，对应板级支持包（BSP）`CLK_SetModuleClock()` 中的 `u32ModuleIdx`/`u64ModuleIdx`。

<a id="r_aed6a31a6ba27aa4eaf05cff984b9c360"></a>

```c
uint32_t clk_src
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clk_src](#aed6a31a6ba27aa4eaf05cff984b9c360)。

时钟源，对应 BSP `CLK_SetModuleClock()` 中的 `u32ClkSrc`。

<a id="r_af24dd5113645830ca2e4a3c9d0b92126"></a>

```c
uint32_t clk_div
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clk_div](#af24dd5113645830ca2e4a3c9d0b92126)。

时钟分频器，对应 BSP `CLK_SetModuleClock()` 中的 `u32ClkDiv`。

## 50.2\_详细说明（Detailed Documentation）

<a id="af24dd5113645830ca2e4a3c9d0b92126"></a>

### `clk_div`

```c
uint32_t numaker_scc_subsys_pcc::clk_div
```

时钟分频器，对应 BSP `CLK_SetModuleClock()` 中的 `u32ClkDiv`。

<a id="a4ebf5a91a803cd92f10d25fcdd0c0eeb"></a>

### `clk_modidx`

```c
uint32_t numaker_scc_subsys_pcc::clk_modidx
```

模块索引，对应板级支持包（BSP）`CLK_SetModuleClock()` 中的 `u32ModuleIdx`/`u64ModuleIdx`。

<a id="aed6a31a6ba27aa4eaf05cff984b9c360"></a>

### `clk_src`

```c
uint32_t numaker_scc_subsys_pcc::clk_src
```

时钟源，对应 BSP `CLK_SetModuleClock()` 中的 `u32ClkSrc`。

本数据类型文档由以下文件生成：

- `zephyr/drivers/clock_control/clock_control_numaker.h`

## 50.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/clock_control_numaker.h](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__numaker_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P049_numaker_scc_subsys_结构体.md) · [返回大纲](大纲.md) · [下一章](P051_numaker_scc_subsys_pcc_rate_结构体.md)
