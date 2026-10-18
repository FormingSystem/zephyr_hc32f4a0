---
id: learning.zephyr-docs.device-power-control-model-reference.page-105
title: clock_mchp_xec_subsys_联合体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unionclock__mchp__xec__subsys.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第105章\_clock\_mchp\_xec\_subsys\_联合体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/unionclock__mchp__xec__subsys.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于与时钟控制（Clock Control）API交互的结构。

```c
#include <zephyr/drivers/clock_control/mchp_xec_clock_control.h>
```

<a id="details"></a>

用于与时钟控制（Clock Control）API交互的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 105.1\_数据成员（Data Fields）

<a id="r_a653526788db4739ec3ee878018d1c91b"></a>

```c
uint32_t val
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[val](#a653526788db4739ec3ee878018d1c91b)。

原始 32 位值。

```c
struct {
```

<a id="r_afd777d827820ab2c860ecd2380310800"></a>

```c
uint32_t pcr_data: 24
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[pcr_data](#af4d56bf6d2f6a7344a9ef1af7ac659b5)。

编码后的 PCR 数据。

<a id="r_ad3fa4a9ee55c1eb598bcdb6ff3ca0f32"></a>

```c
uint32_t bus: 8
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[bus](#ab70cb665df85146d2cac2b34fb802419)。

时钟 ID。

<a id="r_a0aea2694dc278f2c71f33599f73bff9e"></a>

```c
} bits
```

相关声明：[bits](#a0aea2694dc278f2c71f33599f73bff9e)。

位域视图（Bitfield view）。

## 105.2\_详细说明（Detailed Documentation）

<a id="a0aea2694dc278f2c71f33599f73bff9e"></a>

### `[struct]`

```c
struct { ... } clock_mchp_xec_subsys::bits
```

位域视图（Bitfield view）。

<a id="ab70cb665df85146d2cac2b34fb802419"></a>

### `bus`

```c
uint32_t clock_mchp_xec_subsys::bus
```

时钟 ID。

<a id="af4d56bf6d2f6a7344a9ef1af7ac659b5"></a>

### `pcr_data`

```c
uint32_t clock_mchp_xec_subsys::pcr_data
```

编码后的 PCR 数据。

<a id="a653526788db4739ec3ee878018d1c91b"></a>

### `val`

```c
uint32_t clock_mchp_xec_subsys::val
```

原始 32 位值。

本数据类型文档由以下文件生成：

- `zephyr/drivers/clock_control/mchp_xec_clock_control.h`

## 105.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/mchp_xec_clock_control.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__xec__clock__control_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P104_charger_propval_联合体.md) · [返回大纲](大纲.md) · [下一章](P106_fuel_gauge_prop_val_联合体.md)
