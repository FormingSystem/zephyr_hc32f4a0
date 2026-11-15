---
id: learning.zephyr-docs.device-power-control-model-reference.page-54
title: numicro_scc_subsys_pcc_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnumicro__scc__subsys__pcc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第54章\_numicro\_scc\_subsys\_pcc\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnumicro__scc__subsys__pcc.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

外设时钟控制（Peripheral Clock Control）的配置结构。

```c
#include <zephyr/drivers/clock_control/clock_control_numicro.h>
```

<a id="details"></a>

外设时钟控制（Peripheral Clock Control）的配置结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 54.1\_数据成员（Data Fields）

<a id="r_ab762fc4005619ccefc6cfe7da5c8c158"></a>

```c
uint32_t clk_mod
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clk_mod](#ab762fc4005619ccefc6cfe7da5c8c158)。

时钟模块。

<a id="r_a18db15a6377bba17e05a57444828c4cd"></a>

```c
uint32_t clk_src
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clk_src](#a18db15a6377bba17e05a57444828c4cd)。

时钟源（Clock Source）。

<a id="r_a55df199b041ef093c560f29265782b93"></a>

```c
uint32_t clk_div
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clk_div](#a55df199b041ef093c560f29265782b93)。

时钟分频器（Clock divider）。

## 54.2\_详细说明（Detailed Documentation）

<a id="a55df199b041ef093c560f29265782b93"></a>

### `clk_div`

```c
uint32_t numicro_scc_subsys_pcc::clk_div
```

时钟分频器（Clock divider）。

<a id="ab762fc4005619ccefc6cfe7da5c8c158"></a>

### `clk_mod`

```c
uint32_t numicro_scc_subsys_pcc::clk_mod
```

时钟模块。

<a id="a18db15a6377bba17e05a57444828c4cd"></a>

### `clk_src`

```c
uint32_t numicro_scc_subsys_pcc::clk_src
```

时钟源（Clock Source）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/clock_control/clock_control_numicro.h`

## 54.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/clock_control_numicro.h](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__numicro_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P053_numicro_scc_subsys_结构体.md) · [返回大纲](大纲.md) · [下一章](P055_pd_msg_结构体.md)
