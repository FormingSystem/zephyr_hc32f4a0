---
id: learning.zephyr-docs.device-power-control-model-reference.page-11
title: fuel_gauge_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structfuel__gauge__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_fuel\_gauge\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structfuel__gauge__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：电量计（Fuel Gauge）驱动操作。

```c
#include <zephyr/drivers/fuel_gauge.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：电量计（Fuel Gauge）驱动操作。这是每个电量计驱动都需要定义的驱动 API 结构体。它包含驱动所实现操作的函数指针，以及其他驱动专用的常量数据。标记为 `REQ` 的成员必须由驱动设置，标记为 `OPT` 的成员为可选项。另请参阅 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 11.1\_数据成员（Data Fields）

<a id="r_ab729a85c69e561f1ca0aca9f8eb22d91"></a>

```c
fuel_gauge_get_property_t get_property
```

相关声明：[fuel_gauge_get_property_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface__backend.html#gaed940ae925236ad2f25cf05d78304568)、[get_property](#ab729a85c69e561f1ca0aca9f8eb22d91)。

`OPT`：获取电池电量计属性。

<a id="r_a74815d3bb721452bfd3e35cd1221b223"></a>

```c
fuel_gauge_set_property_t set_property
```

相关声明：[fuel_gauge_set_property_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface__backend.html#gae87a20a20f4f1fbb74d72afb2bcee4c9)、[set_property](#a74815d3bb721452bfd3e35cd1221b223)。

`OPT`：设置电池电量计属性。

<a id="r_ad12c13461173177d1c81846a85a3f570"></a>

```c
fuel_gauge_get_buffer_property_t get_buffer_property
```

相关声明：[fuel_gauge_get_buffer_property_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface__backend.html#gaf8843b8ba9ff3102ac4d6c0fa2cb3f69)、[get_buffer_property](#ad12c13461173177d1c81846a85a3f570)。

`OPT`：获取电池电量计的缓冲区属性（Buffer property）。

<a id="r_aa9963e6744222271ab45e2eabbf69f87"></a>

```c
fuel_gauge_set_buffer_property_t set_buffer_property
```

相关声明：[fuel_gauge_set_buffer_property_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface__backend.html#gae5908067ab2a8c70c517d3e12eb364c1)、[set_buffer_property](#aa9963e6744222271ab45e2eabbf69f87)。

`OPT`：设置电池电量计的缓冲区属性。

<a id="r_a406816c19022eea26f0fd61fb21d234c"></a>

```c
fuel_gauge_battery_cutoff_t battery_cutoff
```

相关声明：[fuel_gauge_battery_cutoff_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface__backend.html#ga698c8f84da7d1cbe7db1fc024e2388b7)、[battery_cutoff](#a406816c19022eea26f0fd61fb21d234c)。

`OPT`：让电量计切断（Cutoff）其关联电池。

## 11.2\_详细说明（Detailed Documentation）

<a id="a406816c19022eea26f0fd61fb21d234c"></a>

### `battery_cutoff`

```c
fuel_gauge_battery_cutoff_t fuel_gauge_driver_api::battery_cutoff
```

`OPT`：让电量计切断（Cutoff）其关联电池。

<a id="ad12c13461173177d1c81846a85a3f570"></a>

### `get_buffer_property`

```c
fuel_gauge_get_buffer_property_t fuel_gauge_driver_api::get_buffer_property
```

`OPT`：获取电池电量计的缓冲区属性（Buffer property）。

<a id="ab729a85c69e561f1ca0aca9f8eb22d91"></a>

### `get_property`

```c
fuel_gauge_get_property_t fuel_gauge_driver_api::get_property
```

`OPT`：获取电池电量计属性。

<a id="aa9963e6744222271ab45e2eabbf69f87"></a>

### `set_buffer_property`

```c
fuel_gauge_set_buffer_property_t fuel_gauge_driver_api::set_buffer_property
```

`OPT`：设置电池电量计的缓冲区属性。

<a id="a74815d3bb721452bfd3e35cd1221b223"></a>

### `set_property`

```c
fuel_gauge_set_property_t fuel_gauge_driver_api::set_property
```

`OPT`：设置电池电量计属性。

本数据类型文档由以下文件生成：

- `zephyr/drivers/fuel_gauge.h`

## 11.3\_原页交叉引用（Cross References）

- [zephyr/drivers/fuel_gauge.h](https://docs.zephyrproject.org/latest/doxygen/html/fuel__gauge_8h_source.html)
- [fuel_gauge_get_property_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface__backend.html#gaed940ae925236ad2f25cf05d78304568)
- [fuel_gauge_set_property_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface__backend.html#gae87a20a20f4f1fbb74d72afb2bcee4c9)
- [fuel_gauge_get_buffer_property_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface__backend.html#gaf8843b8ba9ff3102ac4d6c0fa2cb3f69)
- [fuel_gauge_set_buffer_property_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface__backend.html#gae5908067ab2a8c70c517d3e12eb364c1)
- [fuel_gauge_battery_cutoff_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface__backend.html#ga698c8f84da7d1cbe7db1fc024e2388b7)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P010_esp32_rtc_clock_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P012_gpio_acpi_res_结构体.md)
