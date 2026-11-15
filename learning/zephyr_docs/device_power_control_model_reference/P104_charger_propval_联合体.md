---
id: learning.zephyr-docs.device-power-control-model-reference.page-104
title: charger_propval_联合体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unioncharger__propval.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第104章\_charger\_propval\_联合体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/unioncharger__propval.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

charger_property值的容器（Container）。

```c
#include <zephyr/drivers/charger.h>
```

<a id="details"></a>

charger_property值的容器（Container）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 104.1\_数据成员（Data Fields）

<a id="r_a8589124e6152b70b649788a8b94461ab"></a>

```c
enum charger_online online
```

相关声明：[charger_online](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gad95d2b1aaf18ac3a1c536f2d40317c19)、[online](#a8589124e6152b70b649788a8b94461ab)。

对应属性（Property）：`CHARGER_PROP_ONLINE`。

<a id="r_ab0eec508b90d205a1662fd6c69638764"></a>

```c
bool present
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[present](#ab0eec508b90d205a1662fd6c69638764)。

对应属性（Property）：`CHARGER_PROP_PRESENT`。

<a id="r_a7f4976d72d4a7d48385ceb9f18c510b5"></a>

```c
enum charger_status status
```

相关声明：[charger_status](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga4a3c46bc0916082d15e665f7665c89d7)、[status](#a7f4976d72d4a7d48385ceb9f18c510b5)。

对应属性（Property）：`CHARGER_PROP_STATUS`。

<a id="r_ac1a594de2b1c10d28b6a81dd66f1a6ba"></a>

```c
enum charger_charge_type charge_type
```

相关声明：[charger_charge_type](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gaee833a379a8674621d2fdf9b57d1f803)、[charge_type](#ac1a594de2b1c10d28b6a81dd66f1a6ba)。

对应属性（Property）：`CHARGER_PROP_CHARGE_TYPE`。

<a id="r_abd990f67423424da60856f4b6e8824a3"></a>

```c
enum charger_health health
```

相关声明：[charger_health](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gaab33241d3b85ab0770be9b1bd17e4412)、[health](#abd990f67423424da60856f4b6e8824a3)。

对应属性（Property）：`CHARGER_PROP_HEALTH`。

<a id="r_af4e383bb797432033050937740ce0ac3"></a>

```c
uint32_t const_charge_current_ua
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[const_charge_current_ua](#af4e383bb797432033050937740ce0ac3)。

对应属性（Property）：`CHARGER_PROP_CONSTANT_CHARGE_CURRENT_UA`。

<a id="r_a24a97e16505fa336bd3a68743d05936b"></a>

```c
uint32_t precharge_current_ua
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[precharge_current_ua](#a24a97e16505fa336bd3a68743d05936b)。

对应属性（Property）：`CHARGER_PROP_PRECHARGE_CURRENT_UA`。

<a id="r_a89d0c93d68650cefe29e891f4db928f4"></a>

```c
uint32_t charge_term_current_ua
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[charge_term_current_ua](#a89d0c93d68650cefe29e891f4db928f4)。

对应属性（Property）：`CHARGER_PROP_CHARGE_TERM_CURRENT_UA`。

<a id="r_a733bae9ce0bf7e902f8af307f94a356c"></a>

```c
uint32_t const_charge_voltage_uv
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[const_charge_voltage_uv](#a733bae9ce0bf7e902f8af307f94a356c)。

对应属性（Property）：`CHARGER_PROP_CONSTANT_CHARGE_VOLTAGE_UV`。

<a id="r_ae51670de8fa560f0c7610452db029bc2"></a>

```c
uint32_t input_current_regulation_current_ua
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[input_current_regulation_current_ua](#ae51670de8fa560f0c7610452db029bc2)。

对应属性（Property）：`CHARGER_PROP_INPUT_REGULATION_CURRENT_UA`。

<a id="r_afbe7b5fe1e421fb97b37d71ce14dc51a"></a>

```c
uint32_t input_voltage_regulation_voltage_uv
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[input_voltage_regulation_voltage_uv](#afbe7b5fe1e421fb97b37d71ce14dc51a)。

对应属性（Property）：`CHARGER_PROP_INPUT_REGULATION_VOLTAGE_UV`。

<a id="r_a0ad956ab4d0b306f94cce2aa81283a35"></a>

```c
struct charger_current_notifier input_current_notification
```

相关声明：[charger_current_notifier](P001_charger_current_notifier_结构体.md)、[input_current_notification](#a0ad956ab4d0b306f94cce2aa81283a35)。

对应属性（Property）：`CHARGER_PROP_INPUT_CURRENT_NOTIFICATION`。

<a id="r_af256e63ca94f7809da101ad1c33c8e7a"></a>

```c
struct charger_current_notifier discharge_current_notification
```

相关声明：[charger_current_notifier](P001_charger_current_notifier_结构体.md)、[discharge_current_notification](#af256e63ca94f7809da101ad1c33c8e7a)。

对应属性（Property）：`CHARGER_PROP_DISCHARGE_CURRENT_NOTIFICATION`。

<a id="r_a541d1bf0b3e32d7aaeb6a2f4f443c5dc"></a>

```c
uint32_t system_voltage_notification
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[system_voltage_notification](#a541d1bf0b3e32d7aaeb6a2f4f443c5dc)。

对应属性（Property）：`CHARGER_PROP_SYSTEM_VOLTAGE_NOTIFICATION_UV`。

<a id="r_ad77547e88ec465d2e37526751008f634"></a>

```c
charger_status_notifier_t status_notification
```

相关声明：[charger_status_notifier_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga7666697bde91b66829113efe151d1cb2)、[status_notification](#ad77547e88ec465d2e37526751008f634)。

对应属性（Property）：`CHARGER_PROP_STATUS_NOTIFICATION`。

<a id="r_ab9f40a6083ff2361ea4d161226cd77ad"></a>

```c
charger_online_notifier_t online_notification
```

相关声明：[charger_online_notifier_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gab29c2fafc53988555d72974199f25475)、[online_notification](#ab9f40a6083ff2361ea4d161226cd77ad)。

对应属性（Property）：`CHARGER_PROP_ONLINE_NOTIFICATION`。

<a id="r_a0e9c59df061dbe7d221244cd48530a10"></a>

```c
charger_custom_value_int_t custom_int
```

相关声明：[charger_custom_value_int_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga9325615cdd8985cbb3407257afb387a2)、[custom_int](#a0e9c59df061dbe7d221244cd48530a10)。

供下游自定义属性使用的通用整数值。

<a id="r_a7b7aa29e279028e502d8662c70fc1747"></a>

```c
charger_custom_value_uint_t custom_uint
```

相关声明：[charger_custom_value_uint_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gaa7a6c34b4871673151671eae1fac84da)、[custom_uint](#a7b7aa29e279028e502d8662c70fc1747)。

供下游自定义属性使用的通用无符号值。

<a id="r_a1619752e64e8f99d1a488d1fa887ee60"></a>

```c
charger_custom_value_bool_t custom_bool
```

相关声明：[charger_custom_value_bool_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga3b448c73ef8c4844ccbe7adb1f2458fe)、[custom_bool](#a1619752e64e8f99d1a488d1fa887ee60)。

供下游自定义属性使用的通用布尔值。

## 104.2\_详细说明（Detailed Documentation）

<a id="a89d0c93d68650cefe29e891f4db928f4"></a>

### `charge_term_current_ua`

```c
uint32_t charger_propval::charge_term_current_ua
```

对应属性（Property）：`CHARGER_PROP_CHARGE_TERM_CURRENT_UA`。

<a id="ac1a594de2b1c10d28b6a81dd66f1a6ba"></a>

### `charge_type`

```c
enum charger_charge_type charger_propval::charge_type
```

对应属性（Property）：`CHARGER_PROP_CHARGE_TYPE`。

<a id="af4e383bb797432033050937740ce0ac3"></a>

### `const_charge_current_ua`

```c
uint32_t charger_propval::const_charge_current_ua
```

对应属性（Property）：`CHARGER_PROP_CONSTANT_CHARGE_CURRENT_UA`。

<a id="a733bae9ce0bf7e902f8af307f94a356c"></a>

### `const_charge_voltage_uv`

```c
uint32_t charger_propval::const_charge_voltage_uv
```

对应属性（Property）：`CHARGER_PROP_CONSTANT_CHARGE_VOLTAGE_UV`。

<a id="a1619752e64e8f99d1a488d1fa887ee60"></a>

### `custom_bool`

```c
charger_custom_value_bool_t charger_propval::custom_bool
```

供下游自定义属性使用的通用布尔值。

<a id="a0e9c59df061dbe7d221244cd48530a10"></a>

### `custom_int`

```c
charger_custom_value_int_t charger_propval::custom_int
```

供下游自定义属性使用的通用整数值。

<a id="a7b7aa29e279028e502d8662c70fc1747"></a>

### `custom_uint`

```c
charger_custom_value_uint_t charger_propval::custom_uint
```

供下游自定义属性使用的通用无符号值。

<a id="af256e63ca94f7809da101ad1c33c8e7a"></a>

### `discharge_current_notification`

```c
struct charger_current_notifier charger_propval::discharge_current_notification
```

对应属性（Property）：`CHARGER_PROP_DISCHARGE_CURRENT_NOTIFICATION`。

<a id="abd990f67423424da60856f4b6e8824a3"></a>

### `health`

```c
enum charger_health charger_propval::health
```

对应属性（Property）：`CHARGER_PROP_HEALTH`。

<a id="a0ad956ab4d0b306f94cce2aa81283a35"></a>

### `input_current_notification`

```c
struct charger_current_notifier charger_propval::input_current_notification
```

对应属性（Property）：`CHARGER_PROP_INPUT_CURRENT_NOTIFICATION`。

<a id="ae51670de8fa560f0c7610452db029bc2"></a>

### `input_current_regulation_current_ua`

```c
uint32_t charger_propval::input_current_regulation_current_ua
```

对应属性（Property）：`CHARGER_PROP_INPUT_REGULATION_CURRENT_UA`。

<a id="afbe7b5fe1e421fb97b37d71ce14dc51a"></a>

### `input_voltage_regulation_voltage_uv`

```c
uint32_t charger_propval::input_voltage_regulation_voltage_uv
```

对应属性（Property）：`CHARGER_PROP_INPUT_REGULATION_VOLTAGE_UV`。

<a id="a8589124e6152b70b649788a8b94461ab"></a>

### `online`

```c
enum charger_online charger_propval::online
```

对应属性（Property）：`CHARGER_PROP_ONLINE`。

<a id="ab9f40a6083ff2361ea4d161226cd77ad"></a>

### `online_notification`

```c
charger_online_notifier_t charger_propval::online_notification
```

对应属性（Property）：`CHARGER_PROP_ONLINE_NOTIFICATION`。

<a id="a24a97e16505fa336bd3a68743d05936b"></a>

### `precharge_current_ua`

```c
uint32_t charger_propval::precharge_current_ua
```

对应属性（Property）：`CHARGER_PROP_PRECHARGE_CURRENT_UA`。

<a id="ab0eec508b90d205a1662fd6c69638764"></a>

### `present`

```c
bool charger_propval::present
```

对应属性（Property）：`CHARGER_PROP_PRESENT`。

<a id="a7f4976d72d4a7d48385ceb9f18c510b5"></a>

### `status`

```c
enum charger_status charger_propval::status
```

对应属性（Property）：`CHARGER_PROP_STATUS`。

<a id="ad77547e88ec465d2e37526751008f634"></a>

### `status_notification`

```c
charger_status_notifier_t charger_propval::status_notification
```

对应属性（Property）：`CHARGER_PROP_STATUS_NOTIFICATION`。

<a id="a541d1bf0b3e32d7aaeb6a2f4f443c5dc"></a>

### `system_voltage_notification`

```c
uint32_t charger_propval::system_voltage_notification
```

对应属性（Property）：`CHARGER_PROP_SYSTEM_VOLTAGE_NOTIFICATION_UV`。

本数据类型文档由以下文件生成：

- `zephyr/drivers/charger.h`

## 104.3\_原页交叉引用（Cross References）

- [charger_property](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga6eb3b4cc76e4f1e34732b7853eb860b7)
- [zephyr/drivers/charger.h](https://docs.zephyrproject.org/latest/doxygen/html/charger_8h_source.html)
- [charger_online](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gad95d2b1aaf18ac3a1c536f2d40317c19)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [charger_status](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga4a3c46bc0916082d15e665f7665c89d7)
- [charger_charge_type](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gaee833a379a8674621d2fdf9b57d1f803)
- [charger_health](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gaab33241d3b85ab0770be9b1bd17e4412)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [charger_current_notifier](P001_charger_current_notifier_结构体.md)
- [charger_status_notifier_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga7666697bde91b66829113efe151d1cb2)
- [charger_online_notifier_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gab29c2fafc53988555d72974199f25475)
- [charger_custom_value_int_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga9325615cdd8985cbb3407257afb387a2)
- [charger_custom_value_uint_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gaa7a6c34b4871673151671eae1fac84da)
- [charger_custom_value_bool_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga3b448c73ef8c4844ccbe7adb1f2458fe)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P103_wuc_dt_spec_结构体.md) · [返回大纲](大纲.md) · [下一章](P105_clock_mchp_xec_subsys_联合体.md)
