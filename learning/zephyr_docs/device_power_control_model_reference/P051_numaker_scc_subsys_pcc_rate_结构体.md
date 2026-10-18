---
id: learning.zephyr-docs.device-power-control-model-reference.page-51
title: numaker_scc_subsys_pcc_rate_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnumaker__scc__subsys__pcc__rate.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第51章\_numaker\_scc\_subsys\_pcc\_rate\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnumaker__scc__subsys__pcc__rate.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

外设时钟控制频率信息（Peripheral Clock Control Rate Information）。

```c
#include <zephyr/drivers/clock_control/clock_control_numaker.h>
```

<a id="details"></a>

外设时钟控制频率信息（Peripheral Clock Control Rate Information）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 51.1\_数据成员（Data Fields）

<a id="r_a792d0898930c44509f9be2daaf00ba97"></a>

```c
uint32_t clk_modidx_real
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clk_modidx_real](#a792d0898930c44509f9be2daaf00ba97)。

解析后的模块索引。

<a id="r_a8e32abe756e48ba9836d2498651e4b48"></a>

```c
uint32_t clk_src_idx
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clk_src_idx](#a8e32abe756e48ba9836d2498651e4b48)。

从 `clk_src` 解码得到的时钟源索引。

<a id="r_a14bfb22faf2ac674a3769242de557bd6"></a>

```c
uint32_t clk_src_rate
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clk_src_rate](#a14bfb22faf2ac674a3769242de557bd6)。

时钟源频率，单位为 Hz。

<a id="r_a20d5cc4ed27b98c995ddaf89a6b7938f"></a>

```c
uint32_t clk_div_value
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clk_div_value](#a20d5cc4ed27b98c995ddaf89a6b7938f)。

解码后的时钟分频值。

<a id="r_ac1368bffb5781c37662535ea7a11b3fb"></a>

```c
uint32_t clk_div_value_max
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clk_div_value_max](#ac1368bffb5781c37662535ea7a11b3fb)。

支持的最大分频值。

<a id="r_af826904ecf107d6e2a027832922afbb1"></a>

```c
uint32_t clk_mod_rate
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clk_mod_rate](#af826904ecf107d6e2a027832922afbb1)。

最终的模块时钟频率，单位为 Hz。

## 51.2\_详细说明（Detailed Documentation）

<a id="a20d5cc4ed27b98c995ddaf89a6b7938f"></a>

### `clk_div_value`

```c
uint32_t numaker_scc_subsys_pcc_rate::clk_div_value
```

解码后的时钟分频值。

<a id="ac1368bffb5781c37662535ea7a11b3fb"></a>

### `clk_div_value_max`

```c
uint32_t numaker_scc_subsys_pcc_rate::clk_div_value_max
```

支持的最大分频值。

<a id="af826904ecf107d6e2a027832922afbb1"></a>

### `clk_mod_rate`

```c
uint32_t numaker_scc_subsys_pcc_rate::clk_mod_rate
```

最终的模块时钟频率，单位为 Hz。

<a id="a792d0898930c44509f9be2daaf00ba97"></a>

### `clk_modidx_real`

```c
uint32_t numaker_scc_subsys_pcc_rate::clk_modidx_real
```

解析后的模块索引。

<a id="a8e32abe756e48ba9836d2498651e4b48"></a>

### `clk_src_idx`

```c
uint32_t numaker_scc_subsys_pcc_rate::clk_src_idx
```

从 `clk_src` 解码得到的时钟源索引。

<a id="a14bfb22faf2ac674a3769242de557bd6"></a>

### `clk_src_rate`

```c
uint32_t numaker_scc_subsys_pcc_rate::clk_src_rate
```

时钟源频率，单位为 Hz。

本数据类型文档由以下文件生成：

- `zephyr/drivers/clock_control/clock_control_numaker.h`

## 51.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/clock_control_numaker.h](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__numaker_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P050_numaker_scc_subsys_pcc_结构体.md) · [返回大纲](大纲.md) · [下一章](P052_numaker_scc_subsys_rate_结构体.md)
