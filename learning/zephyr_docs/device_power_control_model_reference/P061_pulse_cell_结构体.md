---
id: learning.zephyr-docs.device-power-control-model-reference.page-61
title: pulse_cell_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpulse__cell.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第61章\_pulse\_cell\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpulse__cell.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

固定周期脉冲流（Fixed-Period Pulse Stream）的一个单元。

```c
#include <zephyr/drivers/pulse_io.h>
```

<a id="details"></a>

固定周期脉冲流中的一个单元（Cell）。单元周期在 `pulse_io_config` 中统一设置。`cell_duty_bits > 0` 的后端使用 `duty`，`cell_duty_bits == 0` 的后端仅使用 `level`。注意：与 `pulse_symbol` 相同，此位域布局是 RAM 中的 API 约定，不是 DMA 格式；后端按需转换。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 61.1\_数据成员（Data Fields）

<a id="r_a884c5d0305517a2b4914351cb371b231"></a>

```c
uint16_t duty
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[duty](#a884c5d0305517a2b4914351cb371b231)。

单元周期内的高电平持续时间，以时钟节拍（Tick）为单位。

<a id="r_adae24acc734855ddfdb7c0ed340f8ebb"></a>

```c
uint16_t level: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[level](#adae24acc734855ddfdb7c0ed340f8ebb)。

单元的线路电平，适用于仅支持电平的后端。

<a id="r_ac205607e071a653d65aed9d7beba2606"></a>

```c
uint16_t rsvd: 15
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[rsvd](#ac205607e071a653d65aed9d7beba2606)。

保留，必须为零。

## 61.2\_详细说明（Detailed Documentation）

<a id="a884c5d0305517a2b4914351cb371b231"></a>

### `duty`

```c
uint16_t pulse_cell::duty
```

单元周期内的高电平持续时间，以时钟节拍（Tick）为单位。

<a id="adae24acc734855ddfdb7c0ed340f8ebb"></a>

### `level`

```c
uint16_t pulse_cell::level
```

单元的线路电平，适用于仅支持电平的后端。

<a id="ac205607e071a653d65aed9d7beba2606"></a>

### `rsvd`

```c
uint16_t pulse_cell::rsvd
```

保留，必须为零。

本数据类型文档由以下文件生成：

- `zephyr/drivers/pulse_io.h`

## 61.3\_原页交叉引用（Cross References）

- [zephyr/drivers/pulse_io.h](https://docs.zephyrproject.org/latest/doxygen/html/pulse__io_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [pulse_io_config](P064_pulse_io_config_结构体.md)
- [pulse_symbol](P070_pulse_symbol_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P060_pinctrl_soc_pin_结构体.md) · [返回大纲](大纲.md) · [下一章](P062_pulse_io_bit_template_结构体.md)
