---
id: learning.zephyr-docs.clock-cmsis-model-reference.page-3
title: clock_control_rx_pclk_cfg_结构体
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structclock__control__rx__pclk__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_clock\_control\_rx\_pclk\_cfg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structclock__control__rx__pclk__cfg.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

外设时钟（PCLK）配置。

```c
#include <zephyr/drivers/clock_control/renesas_rx_cgc.h>
```

<a id="details"></a>

外设时钟（PCLK）配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 3.1\_数据成员（Data Fields）

<a id="r_a46ba3c9011b9bfeb792db0017da55d5c"></a>

```c
const struct device * clock_src_dev
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[clock_src_dev](#a46ba3c9011b9bfeb792db0017da55d5c)。

时钟源（Clock Source）。

<a id="r_ad6b95060d8b16fc514451c9403facbe3"></a>

```c
uint32_t clk_div
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clk_div](#ad6b95060d8b16fc514451c9403facbe3)。

分频器配置（Divider Configuration）。

## 3.2\_详细说明（Detailed Documentation）

<a id="ad6b95060d8b16fc514451c9403facbe3"></a>

### `clk_div`

```c
uint32_t clock_control_rx_pclk_cfg::clk_div
```

分频器配置（Divider Configuration）。

<a id="a46ba3c9011b9bfeb792db0017da55d5c"></a>

### `clock_src_dev`

```c
const struct device* clock_control_rx_pclk_cfg::clock_src_dev
```

时钟源（Clock Source）。

本结构体文档由以下文件生成：

- `zephyr/drivers/clock_control/renesas_rx_cgc.h`

## 3.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/renesas_rx_cgc.h](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__cgc_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P002_clock_control_ra_subsys_cfg_结构体.md) · [返回大纲](大纲.md) · [下一章](P004_clock_control_rx_pll_cfg_结构体.md)
