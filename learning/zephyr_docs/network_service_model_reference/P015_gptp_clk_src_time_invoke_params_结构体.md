---
id: learning.zephyr-docs.network-service-model-reference.page-15
title: gptp_clk_src_time_invoke_params_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structgptp__clk__src__time__invoke__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_gptp\_clk\_src\_time\_invoke\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structgptp__clk__src__time__invoke__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ClockSourceTime.invoke函数的参数。

```c
#include <zephyr/net/gptp.h>
```

<a id="details"></a>

`ClockSourceTime.invoke` 函数参数，即由 `ClockSourceTime.invoke` 函数传递的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 15.1\_数据成员（Data Fields）

<a id="r_aaf1ca90ce4e1b216c2edbb9fa72b044a"></a>

```c
double last_gm_freq_change
```

相关声明：[last_gm_freq_change](#aaf1ca90ce4e1b216c2edbb9fa72b044a)。

上一次时基指示器变化（Time Base Indicator Change）时的频率变化量。

<a id="r_a990360a4fdc5bdc8f6626e9dfdc05563"></a>

```c
struct net_ptp_extended_time src_time
```

相关声明：[net_ptp_extended_time](../network_core_model_reference/P115_net_ptp_extended_time_结构体.md)、[src_time](#a990360a4fdc5bdc8f6626e9dfdc05563)。

调用此函数的时间。

<a id="r_ab2328d1a7458ccc8e7fe771e50b463eb"></a>

```c
struct gptp_scaled_ns last_gm_phase_change
```

相关声明：[gptp_scaled_ns](P020_gptp_scaled_ns_结构体.md)、[last_gm_phase_change](#ab2328d1a7458ccc8e7fe771e50b463eb)。

上一次时基指示器变化时的相位变化量。

<a id="r_ada4c313104488059a520d4a2ffff33b4"></a>

```c
uint16_t time_base_indicator
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[time_base_indicator](#ada4c313104488059a520d4a2ffff33b4)。

时基（Time Base），只有相位或频率变化时才改变。

## 15.2\_详细说明（Detailed Documentation）

<a id="aaf1ca90ce4e1b216c2edbb9fa72b044a"></a>

### `last_gm_freq_change`

```c
double gptp_clk_src_time_invoke_params::last_gm_freq_change
```

上一次时基指示器变化（Time Base Indicator Change）时的频率变化量。

<a id="ab2328d1a7458ccc8e7fe771e50b463eb"></a>

### `last_gm_phase_change`

```c
struct gptp_scaled_ns gptp_clk_src_time_invoke_params::last_gm_phase_change
```

上一次时基指示器变化时的相位变化量。

<a id="a990360a4fdc5bdc8f6626e9dfdc05563"></a>

### `src_time`

```c
struct net_ptp_extended_time gptp_clk_src_time_invoke_params::src_time
```

调用此函数的时间。

<a id="ada4c313104488059a520d4a2ffff33b4"></a>

### `time_base_indicator`

```c
uint16_t gptp_clk_src_time_invoke_params::time_base_indicator
```

时基（Time Base），只有相位或频率变化时才改变。

本数据类型文档由以下文件生成：

- `zephyr/net/gptp.h`

## 15.3\_原页交叉引用（Cross References）

- [zephyr/net/gptp.h](https://docs.zephyrproject.org/latest/doxygen/html/gptp_8h_source.html)
- [net_ptp_extended_time](../network_core_model_reference/P115_net_ptp_extended_time_结构体.md)
- [gptp_scaled_ns](P020_gptp_scaled_ns_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P014_ethphy_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P016_gptp_flags_结构体.md)
