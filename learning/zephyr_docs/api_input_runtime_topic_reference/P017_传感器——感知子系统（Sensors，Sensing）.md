---
id: learning.zephyr-docs.api-input-runtime-topic-reference.page-17
title: 传感器——感知子系统（Sensors，Sensing）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__sensor.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_传感器——感知子系统（Sensors，Sensing）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__sensor.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于操作感知子系统中传感器的接口。

<a id="details"></a>

用于操作感知子系统中传感器的接口。

<a id="header-files"></a>
<a id="files"></a>

## 17.1\_文件（Files）

<a id="r_sensing_5Fsensor_2Eh"></a>

```c
file sensing_sensor.h
```

相关声明：[sensing_sensor.h](../api_file_interface_reference/P051_zephyr__sensing__sensing_sensor.h_文件参考.md)。

感知子系统（Sensing Subsystem）传感器API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 17.2\_数据结构（Data Structures）

<a id="r_sensing_5Fsensor_5Fregister_5Finfo"></a>

```c
struct sensing_sensor_register_info
```

相关声明：[sensing_sensor_register_info](../sensor_navigation_model_reference/P027_sensing_sensor_register_info_结构体.md)。

传感器注册信息（Sensor Registration Information）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 17.3\_宏定义（Macros）

<a id="r_gad5a9ccb04d96efc57078e880ca28b654"></a>

```c
#define SENSING_SENSORS_DT_DEFINE(node, reg_ptr, cb_list_ptr, init_fn, pm_device, data_ptr, cfg_ptr, level, prio, api_ptr, ...)
```

相关声明：[SENSING_SENSORS_DT_DEFINE](#gad5a9ccb04d96efc57078e880ca28b654)、[pm_device](../power/P039_通用设备运行时电源结构.md)。

与 `SENSOR_DEVICE_DT_DEFINE()` 类似，但加入感知子系统（sensing）的专用处理。

<a id="r_gae3c7a2acba53cc524a4b1043df49fe85"></a>

```c
#define SENSING_SENSORS_DT_INST_DEFINE(inst, ...)
```

相关声明：[SENSING_SENSORS_DT_INST_DEFINE](#gae3c7a2acba53cc524a4b1043df49fe85)。

与 `SENSING_SENSORS_DT_DEFINE()` 类似，但用于兼容 `DT_DRV_COMPAT` 的实例。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 17.4\_函数（Functions）

<a id="r_gab4c41d02b3731e5829a41e1f5f5154a5"></a>

```c
int sensing_sensor_get_reporters (const struct device *dev, int type, sensing_sensor_handle_t *reporter_handles, int max_handles)
```

相关声明：[sensing_sensor_get_reporters](#gab4c41d02b3731e5829a41e1f5f5154a5)、[device](../device_reference/P002_设备对象结构.md)、[sensing_sensor_handle_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gac959e076fcdc105dfaac1d7a984ba293)。

按传感器类型获取指定传感器实例的上报器句柄（reporter handles）。

<a id="r_ga2c5cfb298b2dfde967edfdd987115021"></a>

```c
int sensing_sensor_get_reporters_count (const struct device *dev, int type)
```

相关声明：[sensing_sensor_get_reporters_count](#ga2c5cfb298b2dfde967edfdd987115021)、[device](../device_reference/P002_设备对象结构.md)。

按传感器类型获取指定传感器实例的上报器数量（reporters count）。

<a id="r_gab9446a3085b6b05da448dce59db50387"></a>

```c
int sensing_sensor_get_state (const struct device *dev, enum sensing_sensor_state *state)
```

相关声明：[sensing_sensor_get_state](#gab9446a3085b6b05da448dce59db50387)、[device](../device_reference/P002_设备对象结构.md)、[sensing_sensor_state](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gabc9657708851e6a744a7cd73319efe06)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

获取此传感器的状态（state）。

## 17.5\_详细说明（Detailed Documentation）

<a id="gad5a9ccb04d96efc57078e880ca28b654"></a>

### `SENSING_SENSORS_DT_DEFINE`

```c
#define SENSING_SENSORS_DT_DEFINE ( node, reg_ptr, cb_list_ptr, init_fn, pm_device, data_ptr, cfg_ptr, level, prio, api_ptr, ... )
```

```c
#include <zephyr/sensing/sensing_sensor.h>
```

展开值（Value）：

```c
SENSOR_DEVICE_DT_DEFINE(node, init_fn, pm_device,               \
                        data_ptr, cfg_ptr, level, prio,         \
                        api_ptr, __VA_ARGS__);                  \
SENSING_CONNECTIONS_DEFINE(node,                                \
                           DT_PROP_LEN_OR(node, reporters, 0),  \
                           cb_list_ptr);                        \
SENSING_SENSORS_DEFINE(node, reg_ptr, cb_list_ptr);
```

与 `SENSOR_DEVICE_DT_DEFINE()` 类似，但加入感知子系统（sensing）的专用处理。

定义实现传感器 API 的传感器（Sensor）。可能在用于枚举全部传感子系统传感器的可迭代段（Sensing Sensor Iterable Section）中定义一个元素。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node` | 设备树节点标识符。 |
| `reg_ptr` | 指向设备 `sensing_sensor_register_info` 的指针。 |
| `cb_list_ptr` | 指向传感回调列表（Sensing Callback List）的指针。 |
| `init_fn` | 驱动初始化函数（Init Function）的名称。 |
| `pm_device` | 电源管理（PM）设备资源引用；设备不使用 PM 时为 `NULL`。 |
| `data_ptr` | 指向设备私有数据（Private Data）的指针。 |
| `cfg_ptr` | 包含此驱动实例配置信息（Configuration Information）的结构体地址。 |
| `level` | 初始化级别（Initialization Level），详情参见 `SYS_INIT()`。 |
| `prio` | 所选初始化级别内的优先级（Priority），详情参见 `SYS_INIT()`。 |
| `api_ptr` | 提供驱动使用的 API 函数结构体（API Function Struct）的初始指针，可以为 `NULL`。 |

<a id="gae3c7a2acba53cc524a4b1043df49fe85"></a>

### `SENSING_SENSORS_DT_INST_DEFINE`

```c
#define SENSING_SENSORS_DT_INST_DEFINE ( inst, ... )
```

```c
#include <zephyr/sensing/sensing_sensor.h>
```

展开值（Value）：

```c
SENSING_SENSORS_DT_DEFINE(DT_DRV_INST(inst), __VA_ARGS__)
```

与 `SENSING_SENSORS_DT_DEFINE()` 类似，但用于兼容 `DT_DRV_COMPAT` 的实例。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例编号（Instance Number）。调用 `SENSING_SENSORS_DT_DEFINE()` 时，由 `DT_DRV_INST(inst)` 替换。 |
| `...` | `SENSING_SENSORS_DT_DEFINE()` 所要求的其他参数。 |

<a id="gab4c41d02b3731e5829a41e1f5f5154a5"></a>

### `sensing_sensor_get_reporters()`

```c
int sensing_sensor_get_reporters ( const struct device * dev, int type, sensing_sensor_handle_t * reporter_handles, int max_handles )
```

```c
#include <zephyr/sensing/sensing_sensor.h>
```

按传感器类型获取指定传感器实例的上报器句柄（reporter handles）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 传感器实例的设备结构体（Device Structure）。 |
| `type` | 指定类型（Type）；`SENSING_SENSOR_TYPE_ALL` 表示获取全部类型的上报传感器（Reporters）。 |
| `max_handles` | 传入的 `reporter_handles` 数组最大容量（Max Count）。可通过 `sensing_sensor_get_reporters_count` 获取实际数量。 |
| `reporter_handles` | 用于接收所找到上报传感器实例（Reporter Sensor Instances）的输入句柄数组（Handles Array）。 |

**返回（Returns）**：**返回值（Returns）：**找到的上报传感器（Reporters）数量；未找到返回 `0`。

<a id="ga2c5cfb298b2dfde967edfdd987115021"></a>

### `sensing_sensor_get_reporters_count()`

```c
int sensing_sensor_get_reporters_count ( const struct device * dev, int type )
```

```c
#include <zephyr/sensing/sensing_sensor.h>
```

按传感器类型获取指定传感器实例的上报器数量（reporters count）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 传感器实例的设备结构体（Device Structure）。 |
| `type` | 要检查的传感器类型（Sensor Type），包括 `SENSING_SENSOR_TYPE_ALL`。 |

**返回（Returns）**：**返回值（Returns）：**指定类型的上报传感器（Reporters）数量；该类型不存在时返回 `0`。

<a id="gab9446a3085b6b05da448dce59db50387"></a>

### `sensing_sensor_get_state()`

```c
int sensing_sensor_get_state ( const struct device * dev, enum sensing_sensor_state * state )
```

```c
#include <zephyr/sensing/sensing_sensor.h>
```

获取此传感器的状态（state）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 传感器实例的设备结构体（Device Structure）。 |
| `state` | 返回的传感器状态值（Sensor State Value）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误值（Negative Error Value）。


## 17.6\_原页交叉引用（Cross References）

- [sensing_sensor.h](../api_file_interface_reference/P051_zephyr__sensing__sensing_sensor.h_文件参考.md)
- [sensing_sensor_register_info](../sensor_navigation_model_reference/P027_sensing_sensor_register_info_结构体.md)
- [pm_device](../power/P039_通用设备运行时电源结构.md)
- [SENSOR_DEVICE_DT_DEFINE()](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaa67ca630e3931a0c3821ba438c86690c)
- [device](../device_reference/P002_设备对象结构.md)
- [sensing_sensor_handle_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gac959e076fcdc105dfaac1d7a984ba293)
- [sensing_sensor_state](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gabc9657708851e6a744a7cd73319efe06)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [DT_PROP_LEN_OR](../dt_property_reference/P001_设备树属性读取宏.md#gabd2d8a9242818c7a9bf981114c912d75)
- [SYS_INIT()](../device_reference/P005_系统初始化接口.md#gaf507cc0613add8113c41896bd631254f)
- [DT_DRV_INST](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1)
- [SENSING_SENSOR_TYPE_ALL](../api_vector_pipeline_topic_reference/P026_传感器类型——感知子系统（Sensor Types，Sensing）.md#ga9f6bc03e84167bf0b1ae8ea4fe016223)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__devicetree-generic-prop_html_gabd2d8a9242818c7a9bf981114c912d75"></a>
<a id="agroup__sensor__interface_html_gaa67ca630e3931a0c3821ba438c86690c"></a>
<a id="astructpm__device_html"></a>
<a id="agroup__devicetree-inst_html_ga219f413efba2f4c0151468b9a25a8dc1"></a>
<a id="agroup__sensing__sensor_html_gad5a9ccb04d96efc57078e880ca28b654"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P016_系统电源协议（System Power Protocol）.md) · [返回大纲](大纲.md) · [下一章](P018_供电端回调（Source Callbacks）.md)
