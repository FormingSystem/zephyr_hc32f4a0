---
id: learning.zephyr-docs.device-power-control-model-reference.page-110
title: pd_battery_supply_pdo_source_联合体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unionpd__battery__supply__pdo__source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第110章\_pd\_battery\_supply\_pdo\_source\_联合体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/unionpd__battery__supply__pdo__source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

创建电池供电PDO供电端（Source）的值，见表6-12“电池供电PDO—供电端”。

```c
#include <zephyr/drivers/usb_c/usbc_pd.h>
```

<a id="details"></a>

创建电池供电PDO供电端（Source）的值，见表6-12“电池供电PDO—供电端”。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 110.1\_数据成员（Data Fields）

```c
struct {
```

<a id="r_abd025ff8575268c9a75354672520a8e6"></a>

```c
uint32_t max_power: 10
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[max_power](#a00ea9931d839cf83b56513f77aa7d5b9)。

最大允许功率（Maximum Allowable Power），以 250 mW 为单位。

<a id="r_af358f8985ff6433a24b61fab6cfe2116"></a>

```c
uint32_t min_voltage: 10
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[min_voltage](#afa2335788e7fde01b90afd95bccf6d5f)。

最小电压，以 50 mV 为单位。

<a id="r_a614ad8010d49ad0763d681c92946ae09"></a>

```c
uint32_t max_voltage: 10
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[max_voltage](#a673ea076da8810bc694b2dc82bbede67)。

最大电压，以 50 mV 为单位。

<a id="r_acd053ca82ff097c25940aa882404b3c0"></a>

```c
uint32_t type: 2
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[type](#ac7157c3fbae86d34e2c7d82bf9af3a3f)。

电池供电（Battery supply）。

<a id="r_a0d1db555b693d55a5f8b7e007be2d422"></a>

```c
};
```

电池供电 PDO 的供电方字段。

<a id="r_a1e775dc0082b531216c154724be360b0"></a>

```c
uint32_t raw_value
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[raw_value](#a1e775dc0082b531216c154724be360b0)。

原始 PDO 值。

## 110.2\_详细说明（Detailed Documentation）

<a id="a0d1db555b693d55a5f8b7e007be2d422"></a>

### `[struct]`

```c
struct { ... } pd_battery_supply_pdo_source
```

电池供电 PDO 的供电方字段。

<a id="a00ea9931d839cf83b56513f77aa7d5b9"></a>

### `max_power`

```c
uint32_t pd_battery_supply_pdo_source::max_power
```

最大允许功率（Maximum Allowable Power），以 250 mW 为单位。

<a id="a673ea076da8810bc694b2dc82bbede67"></a>

### `max_voltage`

```c
uint32_t pd_battery_supply_pdo_source::max_voltage
```

最大电压，以 50 mV 为单位。

<a id="afa2335788e7fde01b90afd95bccf6d5f"></a>

### `min_voltage`

```c
uint32_t pd_battery_supply_pdo_source::min_voltage
```

最小电压，以 50 mV 为单位。

<a id="a1e775dc0082b531216c154724be360b0"></a>

### `raw_value`

```c
uint32_t pd_battery_supply_pdo_source::raw_value
```

原始 PDO 值。

<a id="ac7157c3fbae86d34e2c7d82bf9af3a3f"></a>

### `type`

```c
uint32_t pd_battery_supply_pdo_source::type
```

电池供电（Battery supply）。

设为 `PDO_BATTERY`。

本数据类型文档由以下文件生成：

- `zephyr/drivers/usb_c/usbc_pd.h`

## 110.3\_原页交叉引用（Cross References）

- [zephyr/drivers/usb_c/usbc_pd.h](https://docs.zephyrproject.org/latest/doxygen/html/usbc__pd_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [pd_battery_supply_pdo_source](P110_pd_battery_supply_pdo_source_联合体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P109_pd_battery_supply_pdo_sink_联合体.md) · [返回大纲](大纲.md) · [下一章](P111_pd_ext_header_联合体.md)
