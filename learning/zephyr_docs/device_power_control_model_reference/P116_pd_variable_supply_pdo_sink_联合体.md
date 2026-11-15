---
id: learning.zephyr-docs.device-power-control-model-reference.page-116
title: pd_variable_supply_pdo_sink_联合体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unionpd__variable__supply__pdo__sink.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第116章\_pd\_variable\_supply\_pdo\_sink\_联合体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/unionpd__variable__supply__pdo__sink.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

创建可变供电PDO受电端（Sink）的值，见表6-15“可变供电（非电池）PDO—受电端”。

```c
#include <zephyr/drivers/usb_c/usbc_pd.h>
```

<a id="details"></a>

创建可变供电PDO受电端（Sink）的值，见表6-15“可变供电（非电池）PDO—受电端”。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 116.1\_数据成员（Data Fields）

```c
struct {
```

<a id="r_aaf3991dfefdffb3d6278663f1b46f2a8"></a>

```c
uint32_t operational_current: 10
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[operational_current](#ad648f2400a495b37d8b9f995556419d0)。

工作电流（Operational Current），以 10 mA 为单位。

<a id="r_a1c66d2f2775dea26c212959048ea194c"></a>

```c
uint32_t min_voltage: 10
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[min_voltage](#aaaa1cf3f08208966fb00093f910f70ab)。

最小电压，以 50 mV 为单位。

<a id="r_aef01ba3a131cc7ec5cacd485469362a3"></a>

```c
uint32_t max_voltage: 10
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[max_voltage](#ae360e7c2335a4f6cf5d267c8c82fdc45)。

最大电压，以 50 mV 为单位。

<a id="r_a9f7ae65bdb33eb059ad39d343042dade"></a>

```c
uint32_t type: 2
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[type](#ab7472487f253f5c2cb4d69eb805ede46)。

可变供电（Variable supply）。

<a id="r_af6496f290d7039095a7f3308cf87d8f9"></a>

```c
};
```

可变供电 PDO 的受电方字段。

<a id="r_a2ff80c049f98ab090b100b7f9877bffb"></a>

```c
uint32_t raw_value
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[raw_value](#a2ff80c049f98ab090b100b7f9877bffb)。

原始 PDO 值。

## 116.2\_详细说明（Detailed Documentation）

<a id="af6496f290d7039095a7f3308cf87d8f9"></a>

### `[struct]`

```c
struct { ... } pd_variable_supply_pdo_sink
```

可变供电 PDO 的受电方字段。

<a id="ae360e7c2335a4f6cf5d267c8c82fdc45"></a>

### `max_voltage`

```c
uint32_t pd_variable_supply_pdo_sink::max_voltage
```

最大电压，以 50 mV 为单位。

<a id="aaaa1cf3f08208966fb00093f910f70ab"></a>

### `min_voltage`

```c
uint32_t pd_variable_supply_pdo_sink::min_voltage
```

最小电压，以 50 mV 为单位。

<a id="ad648f2400a495b37d8b9f995556419d0"></a>

### `operational_current`

```c
uint32_t pd_variable_supply_pdo_sink::operational_current
```

工作电流（Operational Current），以 10 mA 为单位。

<a id="a2ff80c049f98ab090b100b7f9877bffb"></a>

### `raw_value`

```c
uint32_t pd_variable_supply_pdo_sink::raw_value
```

原始 PDO 值。

<a id="ab7472487f253f5c2cb4d69eb805ede46"></a>

### `type`

```c
uint32_t pd_variable_supply_pdo_sink::type
```

可变供电（Variable supply）。

设为 `PDO_VARIABLE`。

本数据类型文档由以下文件生成：

- `zephyr/drivers/usb_c/usbc_pd.h`

## 116.3\_原页交叉引用（Cross References）

- [zephyr/drivers/usb_c/usbc_pd.h](https://docs.zephyrproject.org/latest/doxygen/html/usbc__pd_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [pd_variable_supply_pdo_sink](P116_pd_variable_supply_pdo_sink_联合体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P115_pd_rdo_联合体.md) · [返回大纲](大纲.md) · [下一章](P117_pd_variable_supply_pdo_source_联合体.md)
