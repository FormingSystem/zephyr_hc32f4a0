---
id: learning.zephyr-docs.device-power-control-model-reference.page-107
title: pd_augmented_supply_pdo_sink_联合体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unionpd__augmented__supply__pdo__sink.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第107章\_pd\_augmented\_supply\_pdo\_sink\_联合体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/unionpd__augmented__supply__pdo__sink.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

创建增广供电PDO受电端（Sink）的值，见表6-17“可编程电源APDO—受电端”。

```c
#include <zephyr/drivers/usb_c/usbc_pd.h>
```

<a id="details"></a>

创建增广供电PDO受电端（Sink）的值，见表6-17“可编程电源APDO—受电端”。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 107.1\_数据成员（Data Fields）

```c
struct {
```

<a id="r_a12ef7c45f9d329c0d8be125c78b0faeb"></a>

```c
uint32_t max_current: 7
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[max_current](#a0a5da0df48dff5fae42159026c91c7af)。

最大电流，以 50 mA 为增量单位。

<a id="r_a2d262b4fc646d9fe1a624954179fbf67"></a>

```c
uint32_t reserved0: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reserved0](#a3320455a4c7673d3db95f585b07cc319)。

保留，必须设为零。

<a id="r_a5d5f7c76ad94d2944a73b35900d791a0"></a>

```c
uint32_t min_voltage: 8
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[min_voltage](#ad83710136d9dcad3644ec36c1eee9cb0)。

最小电压，以 100 mV 为增量单位。

<a id="r_abf6a96abef9fa5373b06dec511444e0c"></a>

```c
uint32_t reserved1: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reserved1](#a2f1f6094af7449619ab626476fa51698)。

保留，必须设为零。

<a id="r_a9a3acaff77dcb8b4c2fa95eab5eb0d65"></a>

```c
uint32_t max_voltage: 8
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[max_voltage](#af5eca8ab38a3eaaaecd10cdc1092ce3c)。

最大电压，以 100 mV 为增量单位。

<a id="r_a9784092e4162339b9423ea99d80308e3"></a>

```c
uint32_t reserved2: 3
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reserved2](#adfa0b8ab656255cfecc9ca5e1ee05d49)。

保留，必须设为零。

<a id="r_a493364d2493dd2437c031fc69c6d8823"></a>

```c
uint32_t reserved3: 2
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reserved3](#a22e63fa7e83af25d9822dcf3d9b35f40)。

`00b`：可编程电源（Programmable Power Supply，PPS）；`01b` 至 `11b`：保留，禁止使用。此处设置为保留字段，因为未设置时默认为 `0`。

<a id="r_a58601df95afb606cb6578d0f653676d4"></a>

```c
uint32_t type: 2
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[type](#aa800bd5299c535e5de98d57aec1b2fff)。

增强电源数据对象（Augmented Power Data Object，APDO）。

<a id="r_ac395997261c3cf223c5440c3cdf630bf"></a>

```c
};
```

增强供电 PDO 的受电方（Sink）字段。

<a id="r_ae28a74642ffcdf1100f37e3542e1ca96"></a>

```c
uint32_t raw_value
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[raw_value](#ae28a74642ffcdf1100f37e3542e1ca96)。

原始 PDO 值。

## 107.2\_详细说明（Detailed Documentation）

<a id="ac395997261c3cf223c5440c3cdf630bf"></a>

### `[struct]`

```c
struct { ... } pd_augmented_supply_pdo_sink
```

增强供电 PDO 的受电方（Sink）字段。

<a id="a0a5da0df48dff5fae42159026c91c7af"></a>

### `max_current`

```c
uint32_t pd_augmented_supply_pdo_sink::max_current
```

最大电流，以 50 mA 为增量单位。

<a id="af5eca8ab38a3eaaaecd10cdc1092ce3c"></a>

### `max_voltage`

```c
uint32_t pd_augmented_supply_pdo_sink::max_voltage
```

最大电压，以 100 mV 为增量单位。

<a id="ad83710136d9dcad3644ec36c1eee9cb0"></a>

### `min_voltage`

```c
uint32_t pd_augmented_supply_pdo_sink::min_voltage
```

最小电压，以 100 mV 为增量单位。

<a id="ae28a74642ffcdf1100f37e3542e1ca96"></a>

### `raw_value`

```c
uint32_t pd_augmented_supply_pdo_sink::raw_value
```

原始 PDO 值。

<a id="a3320455a4c7673d3db95f585b07cc319"></a>

### `reserved0`

```c
uint32_t pd_augmented_supply_pdo_sink::reserved0
```

保留，必须设为零。

<a id="a2f1f6094af7449619ab626476fa51698"></a>

### `reserved1`

```c
uint32_t pd_augmented_supply_pdo_sink::reserved1
```

保留，必须设为零。

<a id="adfa0b8ab656255cfecc9ca5e1ee05d49"></a>

### `reserved2`

```c
uint32_t pd_augmented_supply_pdo_sink::reserved2
```

保留，必须设为零。

<a id="a22e63fa7e83af25d9822dcf3d9b35f40"></a>

### `reserved3`

```c
uint32_t pd_augmented_supply_pdo_sink::reserved3
```

`00b`：可编程电源（Programmable Power Supply，PPS）；`01b` 至 `11b`：保留，禁止使用。此处设置为保留字段，因为未设置时默认为 `0`。

<a id="aa800bd5299c535e5de98d57aec1b2fff"></a>

### `type`

```c
uint32_t pd_augmented_supply_pdo_sink::type
```

增强电源数据对象（Augmented Power Data Object，APDO）。

设为 `PDO_AUGMENTED`。

本数据类型文档由以下文件生成：

- `zephyr/drivers/usb_c/usbc_pd.h`

## 107.3\_原页交叉引用（Cross References）

- [zephyr/drivers/usb_c/usbc_pd.h](https://docs.zephyrproject.org/latest/doxygen/html/usbc__pd_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [pd_augmented_supply_pdo_sink](P107_pd_augmented_supply_pdo_sink_联合体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P106_fuel_gauge_prop_val_联合体.md) · [返回大纲](大纲.md) · [下一章](P108_pd_augmented_supply_pdo_source_联合体.md)
