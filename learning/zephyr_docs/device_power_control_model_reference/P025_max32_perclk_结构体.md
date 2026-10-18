---
id: learning.zephyr-docs.device-power-control-model-reference.page-25
title: max32_perclk_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmax32__perclk.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_max32\_perclk\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmax32__perclk.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MAX32设备的外设时钟描述符（Peripheral Clock Descriptor）。

```c
#include <zephyr/drivers/clock_control/adi_max32_clock_control.h>
```

<a id="details"></a>

MAX32设备的外设时钟描述符（Peripheral Clock Descriptor）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 25.1\_数据成员（Data Fields）

<a id="r_aef1b470aa172b72c180b1cb2a700c459"></a>

```c
uint32_t bus
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[bus](#aef1b470aa172b72c180b1cb2a700c459)。

外设时钟总线索引。

<a id="r_a10dd006d4c09983c0947a07eb9085348"></a>

```c
uint32_t bit
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[bit](#a10dd006d4c09983c0947a07eb9085348)。

总线寄存器内的外设使能位。

<a id="r_a02bb20153ff5e67ad9a7dbc5a45c646c"></a>

```c
uint32_t clk_src
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clk_src](#a02bb20153ff5e67ad9a7dbc5a45c646c)。

外设时钟源。

## 25.2\_详细说明（Detailed Documentation）

<a id="a10dd006d4c09983c0947a07eb9085348"></a>

### `bit`

```c
uint32_t max32_perclk::bit
```

总线寄存器内的外设使能位。

<a id="aef1b470aa172b72c180b1cb2a700c459"></a>

### `bus`

```c
uint32_t max32_perclk::bus
```

外设时钟总线索引。

<a id="a02bb20153ff5e67ad9a7dbc5a45c646c"></a>

### `clk_src`

```c
uint32_t max32_perclk::clk_src
```

外设时钟源。

为 `<zephyr/dt-bindings/clock/adi_max32_clock.h>` 中定义的 `ADI_MAX32_PRPH_CLK_SRC_*` 常量之一，例如 `ADI_MAX32_PRPH_CLK_SRC_PCLK`、`ADI_MAX32_PRPH_CLK_SRC_IBRO`、`ADI_MAX32_PRPH_CLK_SRC_IPLL`。

本数据类型文档由以下文件生成：

- `zephyr/drivers/clock_control/adi_max32_clock_control.h`

## 25.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/adi_max32_clock_control.h](https://docs.zephyrproject.org/latest/doxygen/html/adi__max32__clock__control_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [zephyr/dt-bindings/clock/adi_max32_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/adi__max32__clock_8h.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P024_max32664c_acc_data_t_结构体.md) · [返回大纲](大纲.md) · [下一章](P026_mb_image_结构体.md)
