---
id: learning.zephyr-docs.api-device-topic-reference.page-7
title: 充电器驱动后端 API（Charger Driver Backend API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_充电器驱动后端 API（Charger Driver Backend API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

本组包含实现充电器（Charger）驱动所需的 API 类型定义、回调签名及其他辅助定义。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.1\_数据结构（Data Structures）

<a id="r_charger_5Fdriver_5Fapi"></a>

```c
struct charger_driver_api
```

相关声明：[charger_driver_api](../device_power_control_model_reference/P002_charger_driver_api_结构体.md)。

驱动操作（Driver Operations）：充电器（Charger）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 7.2\_类型定义（Typedefs）

<a id="r_gafb7488129e0a6c086d3ff0ffadb6c82b"></a>

```c
typedef int(* charger_get_property_t) (const struct device *dev, const charger_prop_t prop, union charger_propval *val)
```

相关声明：[charger_get_property_t](#gafb7488129e0a6c086d3ff0ffadb6c82b)、[device](../device_reference/P002_设备对象结构.md)、[charger_prop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga4ce808890de2d01cdb75feddbf275635)、[charger_propval](../device_power_control_model_reference/P104_charger_propval_联合体.md)。

用于获取充电器属性（charger property）的回调 API。

<a id="r_ga6556781abf0e81eee431c88cb894a8e6"></a>

```c
typedef int(* charger_set_property_t) (const struct device *dev, const charger_prop_t prop, const union charger_propval *val)
```

相关声明：[charger_set_property_t](#ga6556781abf0e81eee431c88cb894a8e6)、[device](../device_reference/P002_设备对象结构.md)、[charger_prop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga4ce808890de2d01cdb75feddbf275635)、[charger_propval](../device_power_control_model_reference/P104_charger_propval_联合体.md)。

用于设置充电器属性的回调 API。

<a id="r_gaf035c2972693a8763fd08b7db8c9c0bd"></a>

```c
typedef int(* charger_charge_enable_t) (const struct device *dev, const bool enable)
```

相关声明：[charger_charge_enable_t](#gaf035c2972693a8763fd08b7db8c9c0bd)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

用于启用或禁用充电周期（charge cycle）的回调 API。

## 7.3\_详细说明（Detailed Documentation）

<a id="gaf035c2972693a8763fd08b7db8c9c0bd"></a>

### `charger_charge_enable_t`

```c
typedef int(* charger_charge_enable_t) (const struct device *dev, const bool enable)
```

```c
#include <zephyr/drivers/charger.h>
```

用于启用或禁用充电周期（charge cycle）的回调 API。

参数说明参见 `charger_charge_enable()`。

<a id="gafb7488129e0a6c086d3ff0ffadb6c82b"></a>

### `charger_get_property_t`

```c
typedef int(* charger_get_property_t) (const struct device *dev, const charger_prop_t prop, union charger_propval *val)
```

```c
#include <zephyr/drivers/charger.h>
```

用于获取充电器属性（charger property）的回调 API。

参数说明参见 `charger_get_prop()`。

<a id="ga6556781abf0e81eee431c88cb894a8e6"></a>

### `charger_set_property_t`

```c
typedef int(* charger_set_property_t) (const struct device *dev, const charger_prop_t prop, const union charger_propval *val)
```

```c
#include <zephyr/drivers/charger.h>
```

用于设置充电器属性的回调 API。

参数说明参见 `charger_set_prop()`。


## 7.4\_原页交叉引用（Cross References）

- [charger_driver_api](../device_power_control_model_reference/P002_charger_driver_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [charger_prop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga4ce808890de2d01cdb75feddbf275635)
- [charger_propval](../device_power_control_model_reference/P104_charger_propval_联合体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [zephyr/drivers/charger.h](https://docs.zephyrproject.org/latest/doxygen/html/charger_8h.html)
- [charger_charge_enable()](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gace1ea9841574d75d314db078df5a0b3a)
- [charger_get_prop()](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga00e5b61d517c93d7d3c863b14b07b738)
- [charger_set_prop()](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga0036e3f5924585457a99a2e444ef5aab)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P006_蓝牙 Mesh 请求 PDU 重放保护列表客户端（Solicitation PDU RPL Client）.md) · [返回大纲](大纲.md) · [下一章](P008_ENS160 API主题.md)
