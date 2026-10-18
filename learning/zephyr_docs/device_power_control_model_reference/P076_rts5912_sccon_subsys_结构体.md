---
id: learning.zephyr-docs.device-power-control-model-reference.page-76
title: rts5912_sccon_subsys_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structrts5912__sccon__subsys.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第76章\_rts5912\_sccon\_subsys\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structrts5912__sccon__subsys.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

RTS5912系统时钟控制器（SCCON）的子系统选择器。

```c
#include <zephyr/drivers/clock_control/clock_control_rts5912.h>
```

<a id="details"></a>

RTS5912系统时钟控制器（SCCON）的子系统选择器。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 76.1\_数据成员（Data Fields）

<a id="r_aeadd64cc7eb73d39d5f7119c2b86365e"></a>

```c
uint32_t clk_grp
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clk_grp](#aeadd64cc7eb73d39d5f7119c2b86365e)。

时钟组。

<a id="r_a28a8e0a3078f7a724948ecec91760382"></a>

```c
uint32_t clk_idx
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clk_idx](#a28a8e0a3078f7a724948ecec91760382)。

组内的时钟索引。

<a id="r_a4743dd2a82bce16d93eb3caf60615909"></a>

```c
uint32_t clk_src
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clk_src](#a4743dd2a82bce16d93eb3caf60615909)。

时钟源（Clock Source）。

<a id="r_a1657eff3e6d6846e87e6d844f0bd102b"></a>

```c
uint32_t clk_div
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clk_div](#a1657eff3e6d6846e87e6d844f0bd102b)。

时钟分频器（Clock divider）。

## 76.2\_详细说明（Detailed Documentation）

<a id="a1657eff3e6d6846e87e6d844f0bd102b"></a>

### `clk_div`

```c
uint32_t rts5912_sccon_subsys::clk_div
```

时钟分频器（Clock divider）。

<a id="aeadd64cc7eb73d39d5f7119c2b86365e"></a>

### `clk_grp`

```c
uint32_t rts5912_sccon_subsys::clk_grp
```

时钟组。

<a id="a28a8e0a3078f7a724948ecec91760382"></a>

### `clk_idx`

```c
uint32_t rts5912_sccon_subsys::clk_idx
```

组内的时钟索引。

<a id="a4743dd2a82bce16d93eb3caf60615909"></a>

### `clk_src`

```c
uint32_t rts5912_sccon_subsys::clk_src
```

时钟源（Clock Source）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/clock_control/clock_control_rts5912.h`

## 76.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/clock_control_rts5912.h](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__rts5912_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P075_renesas_rx_ctsu_touch_cfg_结构体.md) · [返回大纲](大纲.md) · [下一章](P077_rx_irq_dig_filt_s_结构体.md)
