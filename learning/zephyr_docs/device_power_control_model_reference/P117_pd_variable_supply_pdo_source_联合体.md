---
id: learning.zephyr-docs.device-power-control-model-reference.page-117
title: pd_variable_supply_pdo_source_联合体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unionpd__variable__supply__pdo__source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第117章\_pd\_variable\_supply\_pdo\_source\_联合体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/unionpd__variable__supply__pdo__source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

创建可变供电PDO供电端（Source）的值，见表6-11“可变供电（非电池）PDO—供电端”。

```c
#include <zephyr/drivers/usb_c/usbc_pd.h>
```

<a id="details"></a>

创建可变供电PDO供电端（Source）的值，见表6-11“可变供电（非电池）PDO—供电端”。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 117.1\_数据成员（Data Fields）

```c
struct {
```

<a id="r_a4b529709161016a9bad4c0f4145b8b11"></a>

```c
uint32_t max_current: 10
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[max_current](#a8193ca96084db5901bb30195113ff01f)。

最大电流，以 10 mA 为单位。

<a id="r_a9e6e08c0ff5a040b5582bb7faaa5c9a0"></a>

```c
uint32_t min_voltage: 10
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[min_voltage](#a67d86c71997a7c0605b8a199cd51c920)。

最小电压，以 50 mV 为单位。

<a id="r_a0b857e69d391e774d040ed3af357b960"></a>

```c
uint32_t max_voltage: 10
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[max_voltage](#a008cf5201ea6d3e238d547b738570c45)。

最大电压，以 50 mV 为单位。

<a id="r_a35c1d7444ba578b7a3605e7801c140c0"></a>

```c
uint32_t type: 2
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[type](#aabd59b2c5f4bfbbbd5d70adfb009eaf7)。

可变供电（Variable supply）。

<a id="r_a800c4153acb2eee7915e559eb2cf0ac8"></a>

```c
};
```

可变供电 PDO 的供电方字段。

<a id="r_af00512126f128bf1cf31e802652af1bf"></a>

```c
uint32_t raw_value
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[raw_value](#af00512126f128bf1cf31e802652af1bf)。

原始 PDO 值。

## 117.2\_详细说明（Detailed Documentation）

<a id="a800c4153acb2eee7915e559eb2cf0ac8"></a>

### `[struct]`

```c
struct { ... } pd_variable_supply_pdo_source
```

可变供电 PDO 的供电方字段。

<a id="a8193ca96084db5901bb30195113ff01f"></a>

### `max_current`

```c
uint32_t pd_variable_supply_pdo_source::max_current
```

最大电流，以 10 mA 为单位。

<a id="a008cf5201ea6d3e238d547b738570c45"></a>

### `max_voltage`

```c
uint32_t pd_variable_supply_pdo_source::max_voltage
```

最大电压，以 50 mV 为单位。

<a id="a67d86c71997a7c0605b8a199cd51c920"></a>

### `min_voltage`

```c
uint32_t pd_variable_supply_pdo_source::min_voltage
```

最小电压，以 50 mV 为单位。

<a id="af00512126f128bf1cf31e802652af1bf"></a>

### `raw_value`

```c
uint32_t pd_variable_supply_pdo_source::raw_value
```

原始 PDO 值。

<a id="aabd59b2c5f4bfbbbd5d70adfb009eaf7"></a>

### `type`

```c
uint32_t pd_variable_supply_pdo_source::type
```

可变供电（Variable supply）。

设为 `PDO_VARIABLE`。

本数据类型文档由以下文件生成：

- `zephyr/drivers/usb_c/usbc_pd.h`

## 117.3\_原页交叉引用（Cross References）

- [zephyr/drivers/usb_c/usbc_pd.h](https://docs.zephyrproject.org/latest/doxygen/html/usbc__pd_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [pd_variable_supply_pdo_source](P117_pd_variable_supply_pdo_source_联合体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P116_pd_variable_supply_pdo_sink_联合体.md) · [返回大纲](大纲.md)
