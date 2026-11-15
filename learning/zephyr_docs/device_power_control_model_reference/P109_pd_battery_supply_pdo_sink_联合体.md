---
id: learning.zephyr-docs.device-power-control-model-reference.page-109
title: pd_battery_supply_pdo_sink_联合体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unionpd__battery__supply__pdo__sink.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第109章\_pd\_battery\_supply\_pdo\_sink\_联合体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/unionpd__battery__supply__pdo__sink.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

创建电池供电PDO受电端（Sink）的值，见表6-16“电池供电PDO—受电端”。

```c
#include <zephyr/drivers/usb_c/usbc_pd.h>
```

<a id="details"></a>

创建电池供电PDO受电端（Sink）的值，见表6-16“电池供电PDO—受电端”。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 109.1\_数据成员（Data Fields）

```c
struct {
```

<a id="r_a402f3b6f134554eb9bf7010a340982d9"></a>

```c
uint32_t operational_power: 10
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[operational_power](#a3f1072c4ca168aaedd13257f01f410aa)。

工作功率（Operational Power），以 250 mW 为单位。

<a id="r_aa9d1aa51f1f8ddce4c1a4cf6d1fdbfd7"></a>

```c
uint32_t min_voltage: 10
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[min_voltage](#a5a588a46ae8bef2dc10445c2f5422246)。

最小电压，以 50 mV 为单位。

<a id="r_aee1003513097ff02ee47de84cbc5bf30"></a>

```c
uint32_t max_voltage: 10
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[max_voltage](#a858efb23a0c143917b88e5596b899c79)。

最大电压，以 50 mV 为单位。

<a id="r_a3f28ad1af44bcfd5a85c1328650dc221"></a>

```c
uint32_t type: 2
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[type](#a515f6958ba647dc77a30414732afd82b)。

电池供电（Battery supply）。

<a id="r_a33d6a0746f05343c0d7fdab4a5f27917"></a>

```c
};
```

电池供电 PDO 的受电方字段。

<a id="r_aa973b26972c1e1a96c7e0c09dbed08f3"></a>

```c
uint32_t raw_value
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[raw_value](#aa973b26972c1e1a96c7e0c09dbed08f3)。

原始 PDO 值。

## 109.2\_详细说明（Detailed Documentation）

<a id="a33d6a0746f05343c0d7fdab4a5f27917"></a>

### `[struct]`

```c
struct { ... } pd_battery_supply_pdo_sink
```

电池供电 PDO 的受电方字段。

<a id="a858efb23a0c143917b88e5596b899c79"></a>

### `max_voltage`

```c
uint32_t pd_battery_supply_pdo_sink::max_voltage
```

最大电压，以 50 mV 为单位。

<a id="a5a588a46ae8bef2dc10445c2f5422246"></a>

### `min_voltage`

```c
uint32_t pd_battery_supply_pdo_sink::min_voltage
```

最小电压，以 50 mV 为单位。

<a id="a3f1072c4ca168aaedd13257f01f410aa"></a>

### `operational_power`

```c
uint32_t pd_battery_supply_pdo_sink::operational_power
```

工作功率（Operational Power），以 250 mW 为单位。

<a id="aa973b26972c1e1a96c7e0c09dbed08f3"></a>

### `raw_value`

```c
uint32_t pd_battery_supply_pdo_sink::raw_value
```

原始 PDO 值。

<a id="a515f6958ba647dc77a30414732afd82b"></a>

### `type`

```c
uint32_t pd_battery_supply_pdo_sink::type
```

电池供电（Battery supply）。

设为 `PDO_BATTERY`。

本数据类型文档由以下文件生成：

- `zephyr/drivers/usb_c/usbc_pd.h`

## 109.3\_原页交叉引用（Cross References）

- [zephyr/drivers/usb_c/usbc_pd.h](https://docs.zephyrproject.org/latest/doxygen/html/usbc__pd_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [pd_battery_supply_pdo_sink](P109_pd_battery_supply_pdo_sink_联合体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P108_pd_augmented_supply_pdo_source_联合体.md) · [返回大纲](大纲.md) · [下一章](P110_pd_battery_supply_pdo_source_联合体.md)
