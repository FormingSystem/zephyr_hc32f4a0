---
id: learning.zephyr-docs.device-power-control-model-reference.page-108
title: pd_augmented_supply_pdo_source_联合体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unionpd__augmented__supply__pdo__source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第108章\_pd\_augmented\_supply\_pdo\_source\_联合体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/unionpd__augmented__supply__pdo__source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

创建增广供电PDO供电端（Source）的值，见表6-13“可编程电源APDO—供电端”。

```c
#include <zephyr/drivers/usb_c/usbc_pd.h>
```

<a id="details"></a>

创建增广供电PDO供电端（Source）的值，见表6-13“可编程电源APDO—供电端”。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 108.1\_数据成员（Data Fields）

```c
struct {
```

<a id="r_acae71c43921b7f7c74499dc0178c156a"></a>

```c
uint32_t max_current: 7
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[max_current](#a7ef0b26951ce2683c9c4ca0f19b73d6d)。

最大电流，以 50 mA 为增量单位。

<a id="r_a967c8434e630ce8886a1fc888022c178"></a>

```c
uint32_t reserved0: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reserved0](#ac046ddf128416ecbb8f3a26185d03e03)。

保留，必须设为零。

<a id="r_a5b753bab57046a800732b83107be6f4e"></a>

```c
uint32_t min_voltage: 8
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[min_voltage](#a56e1af2acda73fee7e40449b7c39745d)。

最小电压，以 100 mV 为增量单位。

<a id="r_af5900d2a79b5e66daf084fcc63ec3b0e"></a>

```c
uint32_t reserved1: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reserved1](#ae79eb7473040058c0b8572cfe4fa4dce)。

保留，必须设为零。

<a id="r_a32b822ba48db0c38a1f029630369c7a6"></a>

```c
uint32_t max_voltage: 8
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[max_voltage](#aba6df91a8c5da92517f885fa89af8747)。

最大电压，以 100 mV 为增量单位。

<a id="r_a46faa4ff862f0af98bbdd7b0907a8522"></a>

```c
uint32_t reserved2: 2
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reserved2](#ab5868f6ba91821d56ddb419e895a05fa)。

保留，必须设为零。

<a id="r_a194f66544d85b333c7cd2ea4fc0bb642"></a>

```c
uint32_t pps_power_limited: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[pps_power_limited](#abfac34ee5da0b1700b784c7bfe925c19)。

PPS 功率受限（Power Limited）。

<a id="r_a0d1e62971c26266b2bb60159672011ed"></a>

```c
uint32_t reserved3: 2
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reserved3](#aa59ad8a8eb4e2343c14bbe54937aa93d)。

`00b`：可编程电源（Programmable Power Supply，PPS）；`01b` 至 `11b`：保留，禁止使用。此处设置为保留字段，因为未设置时默认为 `0`。

<a id="r_a3d31544bdfbefb567c2a0ba938b787c7"></a>

```c
uint32_t type: 2
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[type](#ae064d7413ede09780ad7314ce31caaa1)。

增强电源数据对象（Augmented Power Data Object，APDO）。

<a id="r_a18a6704de9b5557824d63e52abef8b20"></a>

```c
};
```

增强供电 PDO 的供电方（Source）字段。

<a id="r_a093a674e538dcc2541ff86f50d0156df"></a>

```c
uint32_t raw_value
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[raw_value](#a093a674e538dcc2541ff86f50d0156df)。

原始 PDO 值。

## 108.2\_详细说明（Detailed Documentation）

<a id="a18a6704de9b5557824d63e52abef8b20"></a>

### `[struct]`

```c
struct { ... } pd_augmented_supply_pdo_source
```

增强供电 PDO 的供电方（Source）字段。

<a id="a7ef0b26951ce2683c9c4ca0f19b73d6d"></a>

### `max_current`

```c
uint32_t pd_augmented_supply_pdo_source::max_current
```

最大电流，以 50 mA 为增量单位。

<a id="aba6df91a8c5da92517f885fa89af8747"></a>

### `max_voltage`

```c
uint32_t pd_augmented_supply_pdo_source::max_voltage
```

最大电压，以 100 mV 为增量单位。

<a id="a56e1af2acda73fee7e40449b7c39745d"></a>

### `min_voltage`

```c
uint32_t pd_augmented_supply_pdo_source::min_voltage
```

最小电压，以 100 mV 为增量单位。

<a id="abfac34ee5da0b1700b784c7bfe925c19"></a>

### `pps_power_limited`

```c
uint32_t pd_augmented_supply_pdo_source::pps_power_limited
```

PPS 功率受限（Power Limited）。

<a id="a093a674e538dcc2541ff86f50d0156df"></a>

### `raw_value`

```c
uint32_t pd_augmented_supply_pdo_source::raw_value
```

原始 PDO 值。

<a id="ac046ddf128416ecbb8f3a26185d03e03"></a>

### `reserved0`

```c
uint32_t pd_augmented_supply_pdo_source::reserved0
```

保留，必须设为零。

<a id="ae79eb7473040058c0b8572cfe4fa4dce"></a>

### `reserved1`

```c
uint32_t pd_augmented_supply_pdo_source::reserved1
```

保留，必须设为零。

<a id="ab5868f6ba91821d56ddb419e895a05fa"></a>

### `reserved2`

```c
uint32_t pd_augmented_supply_pdo_source::reserved2
```

保留，必须设为零。

<a id="aa59ad8a8eb4e2343c14bbe54937aa93d"></a>

### `reserved3`

```c
uint32_t pd_augmented_supply_pdo_source::reserved3
```

`00b`：可编程电源（Programmable Power Supply，PPS）；`01b` 至 `11b`：保留，禁止使用。此处设置为保留字段，因为未设置时默认为 `0`。

<a id="ae064d7413ede09780ad7314ce31caaa1"></a>

### `type`

```c
uint32_t pd_augmented_supply_pdo_source::type
```

增强电源数据对象（Augmented Power Data Object，APDO）。

设为 `PDO_AUGMENTED`。

本数据类型文档由以下文件生成：

- `zephyr/drivers/usb_c/usbc_pd.h`

## 108.3\_原页交叉引用（Cross References）

- [zephyr/drivers/usb_c/usbc_pd.h](https://docs.zephyrproject.org/latest/doxygen/html/usbc__pd_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [pd_augmented_supply_pdo_source](P108_pd_augmented_supply_pdo_source_联合体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P107_pd_augmented_supply_pdo_sink_联合体.md) · [返回大纲](大纲.md) · [下一章](P109_pd_battery_supply_pdo_sink_联合体.md)
