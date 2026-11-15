---
id: learning.zephyr-docs.api-vector-pipeline-topic-reference.page-9
title: 电量计驱动后端 API（Fuel Gauge Driver Backend API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_电量计驱动后端 API（Fuel Gauge Driver Backend API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

本组包含实现电量计（Fuel Gauge）驱动所需的 API 类型定义、回调签名及其他辅助项。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.1\_数据结构（Data Structures）

<a id="r_fuel_5Fgauge_5Fdriver_5Fapi"></a>

```c
struct fuel_gauge_driver_api
```

相关声明：[fuel_gauge_driver_api](../device_power_control_model_reference/P011_fuel_gauge_driver_api_结构体.md)。

驱动操作（Driver Operations）：电量计（Fuel Gauge）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 9.2\_类型定义（Typedefs）

<a id="r_gaed940ae925236ad2f25cf05d78304568"></a>

```c
typedef int(* fuel_gauge_get_property_t) (const struct device *dev, fuel_gauge_prop_t prop, union fuel_gauge_prop_val *val)
```

相关声明：[fuel_gauge_get_property_t](#gaed940ae925236ad2f25cf05d78304568)、[device](../device_reference/P002_设备对象结构.md)、[fuel_gauge_prop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga633eb1cb8dd64123252634b833b2f806)、[fuel_gauge_prop_val](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md)。

获取电量计（Fuel Gauge）属性的回调 API。

<a id="r_gae87a20a20f4f1fbb74d72afb2bcee4c9"></a>

```c
typedef int(* fuel_gauge_set_property_t) (const struct device *dev, fuel_gauge_prop_t prop, union fuel_gauge_prop_val val)
```

相关声明：[fuel_gauge_set_property_t](#gae87a20a20f4f1fbb74d72afb2bcee4c9)、[device](../device_reference/P002_设备对象结构.md)、[fuel_gauge_prop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga633eb1cb8dd64123252634b833b2f806)、[fuel_gauge_prop_val](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md)。

设置电量计（Fuel Gauge）属性的回调 API。

<a id="r_gaf8843b8ba9ff3102ac4d6c0fa2cb3f69"></a>

```c
typedef int(* fuel_gauge_get_buffer_property_t) (const struct device *dev, fuel_gauge_prop_t prop_type, void *dst, size_t dst_len)
```

相关声明：[fuel_gauge_get_buffer_property_t](#gaf8843b8ba9ff3102ac4d6c0fa2cb3f69)、[device](../device_reference/P002_设备对象结构.md)、[fuel_gauge_prop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga633eb1cb8dd64123252634b833b2f806)。

获取电量计缓冲区属性（Buffer Property）的回调 API。

<a id="r_gae5908067ab2a8c70c517d3e12eb364c1"></a>

```c
typedef int(* fuel_gauge_set_buffer_property_t) (const struct device *dev, fuel_gauge_prop_t prop_type, const void *src, size_t src_len)
```

相关声明：[fuel_gauge_set_buffer_property_t](#gae5908067ab2a8c70c517d3e12eb364c1)、[device](../device_reference/P002_设备对象结构.md)、[fuel_gauge_prop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga633eb1cb8dd64123252634b833b2f806)。

设置电量计缓冲区属性（Buffer Property）的回调 API。

<a id="r_ga698c8f84da7d1cbe7db1fc024e2388b7"></a>

```c
typedef int(* fuel_gauge_battery_cutoff_t) (const struct device *dev)
```

相关声明：[fuel_gauge_battery_cutoff_t](#ga698c8f84da7d1cbe7db1fc024e2388b7)、[device](../device_reference/P002_设备对象结构.md)。

执行电池切断（Battery Cutoff）的回调 API。

## 9.3\_详细说明（Detailed Documentation）

<a id="ga698c8f84da7d1cbe7db1fc024e2388b7"></a>

### `fuel_gauge_battery_cutoff_t`

```c
typedef int(* fuel_gauge_battery_cutoff_t) (const struct device *dev)
```

```c
#include <zephyr/drivers/fuel_gauge.h>
```

执行电池切断（Battery Cutoff）的回调 API。

参数说明参见 `fuel_gauge_battery_cutoff()`。

<a id="gaf8843b8ba9ff3102ac4d6c0fa2cb3f69"></a>

### `fuel_gauge_get_buffer_property_t`

```c
typedef int(* fuel_gauge_get_buffer_property_t) (const struct device *dev, fuel_gauge_prop_t prop_type, void *dst, size_t dst_len)
```

```c
#include <zephyr/drivers/fuel_gauge.h>
```

获取电量计缓冲区属性（Buffer Property）的回调 API。

参数说明参见 `fuel_gauge_get_buffer_property()`。

<a id="gaed940ae925236ad2f25cf05d78304568"></a>

### `fuel_gauge_get_property_t`

```c
typedef int(* fuel_gauge_get_property_t) (const struct device *dev, fuel_gauge_prop_t prop, union fuel_gauge_prop_val *val)
```

```c
#include <zephyr/drivers/fuel_gauge.h>
```

获取电量计（Fuel Gauge）属性的回调 API。

参数说明参见 `fuel_gauge_get_property()`。

<a id="gae5908067ab2a8c70c517d3e12eb364c1"></a>

### `fuel_gauge_set_buffer_property_t`

```c
typedef int(* fuel_gauge_set_buffer_property_t) (const struct device *dev, fuel_gauge_prop_t prop_type, const void *src, size_t src_len)
```

```c
#include <zephyr/drivers/fuel_gauge.h>
```

设置电量计缓冲区属性（Buffer Property）的回调 API。

参数说明参见 `fuel_gauge_set_buffer_prop()`。

<a id="gae87a20a20f4f1fbb74d72afb2bcee4c9"></a>

### `fuel_gauge_set_property_t`

```c
typedef int(* fuel_gauge_set_property_t) (const struct device *dev, fuel_gauge_prop_t prop, union fuel_gauge_prop_val val)
```

```c
#include <zephyr/drivers/fuel_gauge.h>
```

设置电量计（Fuel Gauge）属性的回调 API。

参数说明参见 `fuel_gauge_set_property()`。


## 9.4\_原页交叉引用（Cross References）

- [fuel_gauge_driver_api](../device_power_control_model_reference/P011_fuel_gauge_driver_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [fuel_gauge_prop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga633eb1cb8dd64123252634b833b2f806)
- [fuel_gauge_prop_val](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md)
- [zephyr/drivers/fuel_gauge.h](https://docs.zephyrproject.org/latest/doxygen/html/fuel__gauge_8h.html)
- [fuel_gauge_battery_cutoff()](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga763a40688dc8fc6a0ba85fdc79178ebc)
- [fuel_gauge_set_buffer_prop()](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#gac63f43b6023b9f2183001d6876fe328a)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P008_ARITHRSTCR 复位控制（Reset Control）.md) · [返回大纲](大纲.md) · [下一章](P010_ISM330DHCX API主题.md)
