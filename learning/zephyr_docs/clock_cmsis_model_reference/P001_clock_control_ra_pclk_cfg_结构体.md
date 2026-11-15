---
id: learning.zephyr-docs.clock-cmsis-model-reference.page-1
title: clock_control_ra_pclk_cfg_结构体
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structclock__control__ra__pclk__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_clock\_control\_ra\_pclk\_cfg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structclock__control__ra__pclk__cfg.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

外设时钟配置（Peripheral Clock Configuration）。

```c
#include <zephyr/drivers/clock_control/renesas_ra_cgc.h>
```

<a id="details"></a>

外设时钟配置（Peripheral Clock Configuration）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 1.1\_数据成员（Data Fields）

<a id="r_a7e4090da84776edb0db7f0eec18767a3"></a>

```c
uint32_t clk_src
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clk_src](#a7e4090da84776edb0db7f0eec18767a3)。

时钟源选择（Clock Source Selection）。

<a id="r_a2ce24e482ea7557d197c87230eba0361"></a>

```c
uint32_t clk_div
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clk_div](#a2ce24e482ea7557d197c87230eba0361)。

时钟分频值（Clock Divider Value）。

## 1.2\_详细说明（Detailed Documentation）

<a id="a2ce24e482ea7557d197c87230eba0361"></a>

### `clk_div`

```c
uint32_t clock_control_ra_pclk_cfg::clk_div
```

时钟分频值（Clock Divider Value）。

<a id="a7e4090da84776edb0db7f0eec18767a3"></a>

### `clk_src`

```c
uint32_t clock_control_ra_pclk_cfg::clk_src
```

时钟源选择（Clock Source Selection）。

本结构体文档由以下文件生成：

- `zephyr/drivers/clock_control/renesas_ra_cgc.h`

## 1.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/renesas_ra_cgc.h](https://docs.zephyrproject.org/latest/doxygen/html/renesas__ra__cgc_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_clock_control_ra_subsys_cfg_结构体.md)
