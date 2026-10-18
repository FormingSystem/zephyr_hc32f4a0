---
id: learning.zephyr-docs.api-scoped-clock-topic-reference.page-18
title: 感知（Sensing）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_感知（Sensing）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

高层传感器框架（High-level sensor framework）。

<a id="details"></a>

高层传感器框架（High-level Sensor Framework）。感知子系统（Sensing Subsystem）向应用提供高层 API，用于发现传感器、打开传感器实例、配置报告行为（Reporting Behavior），以及通过回调接收采样数据。低层传感器访问请参见传感器接口（Sensor）。

<a id="header-groups"></a>
<a id="groups"></a>

## 18.1\_主题（Topics）

<a id="r_sensing_5Fdatatypes"></a>

相关声明：[数据类型（Data Types）](../api_topic_reference/P060_数据类型（Data Types）.md)。

感知子系统使用的传感器数据结构。

<a id="r_sensing_5Fsensor_5Ftypes"></a>

相关声明：[传感器类型——感知子系统（Sensor Types，Sensing）](../api_vector_pipeline_topic_reference/P026_传感器类型——感知子系统（Sensor Types，Sensing）.md)。

感知子系统使用的传感器类型标识符。

<a id="r_sensing_5Fsensor"></a>

相关声明：[传感器——感知子系统（Sensors，Sensing）](../api_input_runtime_topic_reference/P017_传感器——感知子系统（Sensors，Sensing）.md)。

用于操作感知子系统中传感器的接口。

<a id="header-files"></a>
<a id="files"></a>

## 18.2\_文件（Files）

<a id="r_sensing_2Eh"></a>

```c
file sensing.h
```

相关声明：[sensing.h](../api_file_storage_event_reference/P017_zephyr__sensing__sensing.h_文件参考.md)。

感知子系统（Sensing Subsystem）API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 18.3\_数据结构（Data Structures）

<a id="r_sensing_5Fsensor_5Fversion"></a>

```c
struct sensing_sensor_version
```

相关声明：[sensing_sensor_version](../sensor_navigation_model_reference/P032_sensing_sensor_version_结构体.md)。

传感器版本（Sensor Version）。

<a id="r_sensing_5Fsensor_5Finfo"></a>

```c
struct sensing_sensor_info
```

相关声明：[sensing_sensor_info](../sensor_navigation_model_reference/P026_sensing_sensor_info_结构体.md)。

传感器实例（Sensor Instance）的只读描述。

<a id="r_sensing_5Fcallback_5Flist"></a>

```c
struct sensing_callback_list
```

相关声明：[sensing_callback_list](../sensor_navigation_model_reference/P024_sensing_callback_list_结构体.md)。

传感器实例（Sensor Instance）的回调注册。

<a id="r_sensing_5Fsensor_5Fconfig"></a>

```c
struct sensing_sensor_config
```

相关声明：[sensing_sensor_config](../sensor_navigation_model_reference/P025_sensing_sensor_config_结构体.md)。

感知子系统（Sensing Subsystem）的传感器配置，包括间隔、灵敏度和延迟。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 18.4\_宏定义（Macros）

<a id="r_ga180bc8c822f125204964f3c667464273"></a>

```c
#define SENSING_SENSOR_VERSION(_major, _minor, _hotfix, _build)
```

相关声明：[SENSING_SENSOR_VERSION](#ga180bc8c822f125204964f3c667464273)。

构造打包的 `sensing_sensor_version` 值（Packed Value）。

<a id="r_ga16ac7bd397836280f7e8b4aa82f8eb4c"></a>

```c
#define SENSING_SENSITIVITY_INDEX_ALL -1
```

相关声明：[SENSING_SENSITIVITY_INDEX_ALL](#ga16ac7bd397836280f7e8b4aa82f8eb4c)。

表示“应用到所有数据字段”（Apply to All Data Fields）的哨兵索引（Sentinel Index）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 18.5\_类型定义（Typedefs）

<a id="r_gac959e076fcdc105dfaac1d7a984ba293"></a>

```c
typedef void * sensing_sensor_handle_t
```

相关声明：[sensing_sensor_handle_t](#gac959e076fcdc105dfaac1d7a984ba293)。

已打开传感器实例（Sensor Instance）的不透明句柄（Opaque Handle）。

<a id="r_ga5440a8914b664209d62388183b3c89ea"></a>

```c
typedef void(* sensing_data_event_t) (sensing_sensor_handle_t handle, const void *buf, void *context)
```

相关声明：[sensing_data_event_t](#ga5440a8914b664209d62388183b3c89ea)、[sensing_sensor_handle_t](#gac959e076fcdc105dfaac1d7a984ba293)。

数据事件回调签名（Data Event Callback Signature）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 18.6\_枚举（Enumerations）

<a id="r_gabc9657708851e6a744a7cd73319efe06"></a>

```c
enum sensing_sensor_state { SENSING_SENSOR_STATE_READY = 0 , SENSING_SENSOR_STATE_OFFLINE = 1 }
```

相关声明：[sensing_sensor_state](#gabc9657708851e6a744a7cd73319efe06)、[SENSING_SENSOR_STATE_READY](#ggabc9657708851e6a744a7cd73319efe06a735fe339796ea7b4d2387d931382ce93)、[SENSING_SENSOR_STATE_OFFLINE](#ggabc9657708851e6a744a7cd73319efe06af23a28e861a8fa2d49b18a0fbe62600e)。

传感器状态（Sensor State）。

<a id="r_ga69d2ae9f45215742654bfc7e4676e6f2"></a>

```c
enum sensing_sensor_attribute { SENSING_SENSOR_ATTRIBUTE_INTERVAL = 0 , SENSING_SENSOR_ATTRIBUTE_SENSITIVITY = 1 , SENSING_SENSOR_ATTRIBUTE_LATENCY = 2 , SENSING_SENSOR_ATTRIBUTE_MAX }
```

相关声明：[sensing_sensor_attribute](#ga69d2ae9f45215742654bfc7e4676e6f2)、[SENSING_SENSOR_ATTRIBUTE_INTERVAL](#gga69d2ae9f45215742654bfc7e4676e6f2a8c9870b1303008b45e2caeb33f5c44a3)、[SENSING_SENSOR_ATTRIBUTE_SENSITIVITY](#gga69d2ae9f45215742654bfc7e4676e6f2abc39825a643b9d1452162f057f79774b)、[SENSING_SENSOR_ATTRIBUTE_LATENCY](#gga69d2ae9f45215742654bfc7e4676e6f2a2ccb8b476935ce27b2eedbb889e25476)、[SENSING_SENSOR_ATTRIBUTE_MAX](#gga69d2ae9f45215742654bfc7e4676e6f2a072ff2aa9640503bfd8cbc8f7d271980)。

传感器配置属性（Sensor Configuration Attribute）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 18.7\_函数（Functions）

<a id="r_gaf3b6c66c2db12115f3ebec0cdba32e86"></a>

```c
int sensing_get_sensors (int *num_sensors, const struct sensing_sensor_info **info)
```

相关声明：[sensing_get_sensors](#gaf3b6c66c2db12115f3ebec0cdba32e86)、[sensing_sensor_info](../sensor_navigation_model_reference/P026_sensing_sensor_info_结构体.md)。

获取所有支持的传感器实例（Sensor Instances）的信息。

<a id="r_ga8e427d28efc492f15d762af3308d78cd"></a>

```c
int sensing_open_sensor (const struct sensing_sensor_info *info, struct sensing_callback_list *cb_list, sensing_sensor_handle_t *handle)
```

相关声明：[sensing_open_sensor](#ga8e427d28efc492f15d762af3308d78cd)、[sensing_sensor_info](../sensor_navigation_model_reference/P026_sensing_sensor_info_结构体.md)、[sensing_callback_list](../sensor_navigation_model_reference/P024_sensing_callback_list_结构体.md)、[sensing_sensor_handle_t](#gac959e076fcdc105dfaac1d7a984ba293)。

根据传感子系统的传感器信息（Sensing Sensor Info）打开传感器实例。

<a id="r_ga4218453664fee0aa61697018e3193e7a"></a>

```c
int sensing_open_sensor_by_dt (const struct device *dev, struct sensing_callback_list *cb_list, sensing_sensor_handle_t *handle)
```

相关声明：[sensing_open_sensor_by_dt](#ga4218453664fee0aa61697018e3193e7a)、[device](../device_reference/P002_设备对象结构.md)、[sensing_callback_list](../sensor_navigation_model_reference/P024_sensing_callback_list_结构体.md)、[sensing_sensor_handle_t](#gac959e076fcdc105dfaac1d7a984ba293)。

根据设备（Device）打开传感器实例（Sensor Instance）。

<a id="r_ga98e49ea0e84e93867df20033d01ee66c"></a>

```c
int sensing_close_sensor (sensing_sensor_handle_t *handle)
```

相关声明：[sensing_close_sensor](#ga98e49ea0e84e93867df20033d01ee66c)、[sensing_sensor_handle_t](#gac959e076fcdc105dfaac1d7a984ba293)。

关闭传感器实例（Sensor Instance）。

<a id="r_ga46591a2d29f5b5e160a72bbe289884ab"></a>

```c
int sensing_set_config (sensing_sensor_handle_t handle, struct sensing_sensor_config *configs, int count)
```

相关声明：[sensing_set_config](#ga46591a2d29f5b5e160a72bbe289884ab)、[sensing_sensor_handle_t](#gac959e076fcdc105dfaac1d7a984ba293)、[sensing_sensor_config](../sensor_navigation_model_reference/P025_sensing_sensor_config_结构体.md)。

向传感子系统（Sensing Subsystem）设置当前配置项（Config Items）。

<a id="r_gaf4037066c9a7a9f3eb1c79a4d8ae0920"></a>

```c
int sensing_get_config (sensing_sensor_handle_t handle, struct sensing_sensor_config *configs, int count)
```

相关声明：[sensing_get_config](#gaf4037066c9a7a9f3eb1c79a4d8ae0920)、[sensing_sensor_handle_t](#gac959e076fcdc105dfaac1d7a984ba293)、[sensing_sensor_config](../sensor_navigation_model_reference/P025_sensing_sensor_config_结构体.md)。

从传感子系统（Sensing Subsystem）获取当前配置项（Config Items）。

<a id="r_ga4399f2e03d4d9444045b705b13cb6dfd"></a>

```c
const struct sensing_sensor_info * sensing_get_sensor_info (sensing_sensor_handle_t handle)
```

相关声明：[sensing_sensor_info](../sensor_navigation_model_reference/P026_sensing_sensor_info_结构体.md)、[sensing_get_sensor_info](#ga4399f2e03d4d9444045b705b13cb6dfd)、[sensing_sensor_handle_t](#gac959e076fcdc105dfaac1d7a984ba293)。

根据传感器实例句柄（Sensor Instance Handle）获取传感器信息。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 18.8\_传感器报告标志（Sensor Reporting Flags）

<a id="r_ga498dcf4dbd0eb42d8ca399df4acc2e5e"></a>

```c
#define SENSING_SENSOR_FLAG_REPORT_ON_EVENT BIT(0)
```

相关声明：[SENSING_SENSOR_FLAG_REPORT_ON_EVENT](#ga498dcf4dbd0eb42d8ca399df4acc2e5e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

指示传感器是否在事件发生时报告数据（Reporting Data on Event）的标志。

<a id="r_ga8b9766509e66fd8b8fa8e718a1544137"></a>

```c
#define SENSING_SENSOR_FLAG_REPORT_ON_CHANGE BIT(1)
```

相关声明：[SENSING_SENSOR_FLAG_REPORT_ON_CHANGE](#ga8b9766509e66fd8b8fa8e718a1544137)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

指示传感器是否在数据变化时报告数据（Reporting Data on Change）的标志。

## 18.9\_详细说明（Detailed Documentation）

<a id="ga16ac7bd397836280f7e8b4aa82f8eb4c"></a>

### `SENSING_SENSITIVITY_INDEX_ALL`

```c
#define SENSING_SENSITIVITY_INDEX_ALL -1
```

```c
#include <zephyr/sensing/sensing.h>
```

表示“应用到所有数据字段”（Apply to All Data Fields）的哨兵索引（Sentinel Index）。

传感器在一个样本中提供多个字段时，用于灵敏度配置（Sensitivity Configuration）。

<a id="ga8b9766509e66fd8b8fa8e718a1544137"></a>

### `SENSING_SENSOR_FLAG_REPORT_ON_CHANGE`

```c
#define SENSING_SENSOR_FLAG_REPORT_ON_CHANGE BIT(1)
```

```c
#include <zephyr/sensing/sensing.h>
```

指示传感器是否在数据变化时报告数据（Reporting Data on Change）的标志。

传感器数据发生变化时报告传感器数据（Report on Change）。

**说明（Note）**：注意（Note）：与 SENSING_SENSOR_FLAG_REPORT_ON_EVENT 互斥（Mutually Exclusive）。

<a id="ga498dcf4dbd0eb42d8ca399df4acc2e5e"></a>

### `SENSING_SENSOR_FLAG_REPORT_ON_EVENT`

```c
#define SENSING_SENSOR_FLAG_REPORT_ON_EVENT BIT(0)
```

```c
#include <zephyr/sensing/sensing.h>
```

指示传感器是否在事件发生时报告数据（Reporting Data on Event）的标志。

传感器事件（Sensor Event）发生时报告传感器数据，例如运动检测传感器报告检测到运动或静止的事件。

**说明（Note）**：注意（Note）：与 SENSING_SENSOR_FLAG_REPORT_ON_CHANGE 互斥（Mutually Exclusive）。

<a id="ga180bc8c822f125204964f3c667464273"></a>

### `SENSING_SENSOR_VERSION`

```c
#define SENSING_SENSOR_VERSION ( _major, _minor, _hotfix, _build )
```

```c
#include <zephyr/sensing/sensing.h>
```

展开值（Value）：

```c
(FIELD_PREP(GENMASK(31, 24), _major) |  \
 FIELD_PREP(GENMASK(23, 16), _minor) |  \
 FIELD_PREP(GENMASK(15, 8), _hotfix) |  \
 FIELD_PREP(GENMASK(7, 0), _build))
```

构造打包的 `sensing_sensor_version` 值（Packed Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_major` | 主版本（Major version）。 |
| `_minor` | 次版本（Minor version）。 |
| `_hotfix` | 热修复版本（Hotfix Version）。 |
| `_build` | 构建编号（Build Number）。 |

返回（Returns）：32 位打包版本值（Packed Version Value）。

<a id="ga5440a8914b664209d62388183b3c89ea"></a>

### `sensing_data_event_t`

```c
typedef void(* sensing_data_event_t) (sensing_sensor_handle_t handle, const void *buf, void *context)
```

```c
#include <zephyr/sensing/sensing.h>
```

数据事件回调签名（Data Event Callback Signature）。

感知子系统（Sensing Subsystem）调用此回调，为已打开的传感器传递缓冲的样本（Buffered Samples）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `handle` | 传给 sensing_open_sensor 的传感器实例句柄（Sensor Instance Handle）。 |
| `buf` | 指向传感器类型专用样本缓冲区（Sample Buffer）的指针；参见数据类型（Data Types）和传感器类型（Sensor Types，Sensing）。 |
| `context` | 通过 sensing_callback_list::context 提供的用户上下文指针（User Context Pointer）。 |

<a id="gac959e076fcdc105dfaac1d7a984ba293"></a>

### `sensing_sensor_handle_t`

```c
typedef void* sensing_sensor_handle_t
```

```c
#include <zephyr/sensing/sensing.h>
```

已打开传感器实例（Sensor Instance）的不透明句柄（Opaque Handle）。

有效句柄（Handle）通过 sensing_open_sensor 或 sensing_open_sensor_by_dt 获得；不再需要时，必须使用 sensing_close_sensor 关闭。

<a id="ga69d2ae9f45215742654bfc7e4676e6f2"></a>

### `sensing_sensor_attribute`

```c
enum sensing_sensor_attribute
```

```c
#include <zephyr/sensing/sensing.h>
```

传感器配置属性（Sensor Configuration Attribute）。

此枚举定义传感器配置可能具有的属性（Attributes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSING_SENSOR_ATTRIBUTE_INTERVAL` | 样本之间的报告间隔（Reporting Interval），单位为微秒（us）。参见 sensing_sensor_config::interval。 |
| `SENSING_SENSOR_ATTRIBUTE_SENSITIVITY` | 各字段的灵敏度阈值（Per-field Sensitivity Threshold）。参见 sensing_sensor_config::sensitivity。 |
| `SENSING_SENSOR_ATTRIBUTE_LATENCY` | 最大批处理延迟（Maximum Batching Latency），单位为微秒（us）。参见 sensing_sensor_config::latency。 |
| `SENSING_SENSOR_ATTRIBUTE_MAX` | 支持的属性数量（Number of Supported Attributes）。 |

<a id="gabc9657708851e6a744a7cd73319efe06"></a>

### `sensing_sensor_state`

```c
enum sensing_sensor_state
```

```c
#include <zephyr/sensing/sensing.h>
```

传感器状态（Sensor State）。

此枚举定义传感器可能处于的状态（States）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSING_SENSOR_STATE_READY` | 传感器已就绪（Ready）。 |
| `SENSING_SENSOR_STATE_OFFLINE` | 传感器离线（Offline）。 |

<a id="ga98e49ea0e84e93867df20033d01ee66c"></a>

### `sensing_close_sensor()`

```c
int sensing_close_sensor ( sensing_sensor_handle_t * handle)
```

```c
#include <zephyr/sensing/sensing.h>
```

关闭传感器实例（Sensor Instance）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `handle` | 需要关闭的传感器实例句柄（Sensor Instance Handle）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误值（Negative Error Value）。

<a id="gaf4037066c9a7a9f3eb1c79a4d8ae0920"></a>

### `sensing_get_config()`

```c
int sensing_get_config ( sensing_sensor_handle_t handle, struct sensing_sensor_config * configs, int count )
```

```c
#include <zephyr/sensing/sensing.h>
```

从传感子系统（Sensing Subsystem）获取当前配置项（Config Items）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `handle` | 传感器实例句柄（Sensor Instance Handle）。 |
| `configs` | 根据配置属性（Config Attribute）要获取的配置项。 |
| `count` | 配置项数量（Config Count）。 |

返回（Returns）：成功时为 0；失败、不受支持等情况下为负错误值。

<a id="ga4399f2e03d4d9444045b705b13cb6dfd"></a>

### `sensing_get_sensor_info()`

```c
const struct sensing_sensor_info * sensing_get_sensor_info ( sensing_sensor_handle_t handle)
```

```c
#include <zephyr/sensing/sensing.h>
```

根据传感器实例句柄（Sensor Instance Handle）获取传感器信息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `handle` | 传感器实例句柄（Sensor Instance Handle）。 |

返回（Returns）：成功时为指向 sensing_sensor_info 的常量指针（Const Pointer），失败时为 NULL。

<a id="gaf3b6c66c2db12115f3ebec0cdba32e86"></a>

### `sensing_get_sensors()`

```c
int sensing_get_sensors ( int * num_sensors, const struct sensing_sensor_info ** info )
```

```c
#include <zephyr/sensing/sensing.h>
```

获取所有支持的传感器实例（Sensor Instances）的信息。

此 API 仅返回传感器实例的只读信息（Read-only Information）；info 指针直接指向内部缓冲区，调用者无需分配缓冲区，也不会对传感器实例产生副作用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `num_sensors` | 获取传感器实例数量（Number of Sensor Instances）。 |
| `info` | 用于接收传感器实例信息数组指针（Information Array Pointer）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误值（Negative Error Value）。

<a id="ga8e427d28efc492f15d762af3308d78cd"></a>

### `sensing_open_sensor()`

```c
int sensing_open_sensor ( const struct sensing_sensor_info * info, struct sensing_callback_list * cb_list, sensing_sensor_handle_t * handle )
```

```c
#include <zephyr/sensing/sensing.h>
```

根据传感子系统的传感器信息（Sensing Sensor Info）打开传感器实例。

应用客户端使用它打开传感器实例（Sensor Instance）并获取句柄（Handle）。支持多个应用客户端打开同一实例，此时不同客户端获得不同的句柄；同时还会注册感知回调列表（Sensing Callback List）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `info` | 从 sensing_get_sensors 获取的传感器信息（Sensor Info）。 |
| `cb_list` | 要注册到感知子系统（Sensing）的回调列表，必须具有静态生命周期（Static Lifetime）。 |
| `handle` | 已打开实例的句柄（Instance Handle）；失败时设置为 NULL。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误值（Negative Error Value）。

<a id="ga4218453664fee0aa61697018e3193e7a"></a>

### `sensing_open_sensor_by_dt()`

```c
int sensing_open_sensor_by_dt ( const struct device * dev, struct sensing_callback_list * cb_list, sensing_sensor_handle_t * handle )
```

```c
#include <zephyr/sensing/sensing.h>
```

根据设备（Device）打开传感器实例（Sensor Instance）。

应用客户端使用它打开传感器实例（Sensor Instance）并获取句柄（Handle）。支持多个应用客户端打开同一实例，此时不同客户端获得不同的句柄；同时还会注册感知回调列表（Sensing Callback List）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 从设备树（Device Tree）获取的设备指针（Device Pointer）。 |
| `cb_list` | 要注册到感知子系统（Sensing）的回调列表，必须具有静态生命周期（Static Lifetime）。 |
| `handle` | 已打开实例的句柄（Instance Handle）；失败时设置为 NULL。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误值（Negative Error Value）。

<a id="ga46591a2d29f5b5e160a72bbe289884ab"></a>

### `sensing_set_config()`

```c
int sensing_set_config ( sensing_sensor_handle_t handle, struct sensing_sensor_config * configs, int count )
```

```c
#include <zephyr/sensing/sensing.h>
```

向传感子系统（Sensing Subsystem）设置当前配置项（Config Items）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `handle` | 传感器实例句柄（Sensor Instance Handle）。 |
| `configs` | 根据配置属性（Config Attribute）要设置的配置项。 |
| `count` | 配置项数量（Config Count）。 |

返回（Returns）：成功时为 0；失败、不受支持等情况下为负错误值。


## 18.10\_原页交叉引用（Cross References）

- [数据类型（Data Types）](../api_topic_reference/P060_数据类型（Data Types）.md)
- [传感器类型——感知子系统（Sensor Types，Sensing）](../api_vector_pipeline_topic_reference/P026_传感器类型——感知子系统（Sensor Types，Sensing）.md)
- [传感器——感知子系统（Sensors，Sensing）](../api_input_runtime_topic_reference/P017_传感器——感知子系统（Sensors，Sensing）.md)
- [sensing.h](../api_file_storage_event_reference/P017_zephyr__sensing__sensing.h_文件参考.md)
- [sensing_sensor_version](../sensor_navigation_model_reference/P032_sensing_sensor_version_结构体.md)
- [sensing_sensor_info](../sensor_navigation_model_reference/P026_sensing_sensor_info_结构体.md)
- [sensing_callback_list](../sensor_navigation_model_reference/P024_sensing_callback_list_结构体.md)
- [sensing_sensor_config](../sensor_navigation_model_reference/P025_sensing_sensor_config_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [传感器（Sensor）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)
- [FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)
- [GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)
- [sensing_callback_list::context](../sensor_navigation_model_reference/P024_sensing_callback_list_结构体.md#a43504dbe7d484f0d0e7d33b8bb6318d4)
- [sensing_sensor_config::interval](../sensor_navigation_model_reference/P025_sensing_sensor_config_结构体.md#a7512f7254f6960ed398150db23868965)
- [sensing_sensor_config::sensitivity](../sensor_navigation_model_reference/P025_sensing_sensor_config_结构体.md#acc1270dbe02ff6324e0f66acbde8ce33)
- [sensing_sensor_config::latency](../sensor_navigation_model_reference/P025_sensing_sensor_config_结构体.md#af9d2ee27b3a04fd65baa1d1d0cb2badc)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__sys-util_html_ga58530d20924859d16358c7400c37738d"></a>
<a id="asilabs-pinctrl-siwx91x_8h_html_aa03c8b31bf67a097dd9f8153a04ef86b"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga69d2ae9f45215742654bfc7e4676e6f2a8c9870b1303008b45e2caeb33f5c44a3"></a>
<a id="gga69d2ae9f45215742654bfc7e4676e6f2abc39825a643b9d1452162f057f79774b"></a>
<a id="gga69d2ae9f45215742654bfc7e4676e6f2a2ccb8b476935ce27b2eedbb889e25476"></a>
<a id="gga69d2ae9f45215742654bfc7e4676e6f2a072ff2aa9640503bfd8cbc8f7d271980"></a>
<a id="ggabc9657708851e6a744a7cd73319efe06a735fe339796ea7b4d2387d931382ce93"></a>
<a id="ggabc9657708851e6a744a7cd73319efe06af23a28e861a8fa2d49b18a0fbe62600e"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P017_系统控制与管理接口（SCMI）.md) · [返回大纲](大纲.md)
