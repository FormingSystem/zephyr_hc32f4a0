---
id: learning.zephyr-docs.api-file-storage-event-reference.page-17
title: zephyr__sensing__sensing.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sensing_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_zephyr\_\_sensing\_\_sensing.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sensing_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

感知子系统（Sensing Subsystem）API的主头文件。

<a id="details"></a>

```c
#include <zephyr/sensing/sensing_datatypes.h>
#include <zephyr/sensing/sensing_sensor_types.h>
#include <zephyr/device.h>
```

查看此文件的源码。

感知子系统（Sensing Subsystem）API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 17.1\_数据结构（Data Structures）

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

## 17.2\_宏定义（Macros）

<a id="r_ga180bc8c822f125204964f3c667464273"></a>

```c
#define SENSING_SENSOR_VERSION(_major, _minor, _hotfix, _build)
```

相关声明：[SENSING_SENSOR_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga180bc8c822f125204964f3c667464273)。

构造打包的 `sensing_sensor_version` 值（Packed Value）。

<a id="r_ga16ac7bd397836280f7e8b4aa82f8eb4c"></a>

```c
#define SENSING_SENSITIVITY_INDEX_ALL -1
```

相关声明：[SENSING_SENSITIVITY_INDEX_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga16ac7bd397836280f7e8b4aa82f8eb4c)。

表示“应用到所有数据字段”（Apply to All Data Fields）的哨兵索引（Sentinel Index）。

<a id="define-members-0"></a>

### 传感器报告标志（Sensor Reporting Flags）

<a id="r_ga498dcf4dbd0eb42d8ca399df4acc2e5e"></a>

```c
#define SENSING_SENSOR_FLAG_REPORT_ON_EVENT BIT(0)
```

相关声明：[SENSING_SENSOR_FLAG_REPORT_ON_EVENT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga498dcf4dbd0eb42d8ca399df4acc2e5e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

指示传感器是否在事件发生时报告数据（Reporting Data on Event）的标志。

<a id="r_ga8b9766509e66fd8b8fa8e718a1544137"></a>

```c
#define SENSING_SENSOR_FLAG_REPORT_ON_CHANGE BIT(1)
```

相关声明：[SENSING_SENSOR_FLAG_REPORT_ON_CHANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga8b9766509e66fd8b8fa8e718a1544137)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

指示传感器是否在数据变化时报告数据（Reporting Data on Change）的标志。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 17.3\_类型定义（Typedefs）

<a id="r_gac959e076fcdc105dfaac1d7a984ba293"></a>

```c
typedef void * sensing_sensor_handle_t
```

相关声明：[sensing_sensor_handle_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gac959e076fcdc105dfaac1d7a984ba293)。

已打开传感器实例（Sensor Instance）的不透明句柄（Opaque Handle）。

<a id="r_ga5440a8914b664209d62388183b3c89ea"></a>

```c
typedef void(* sensing_data_event_t) (sensing_sensor_handle_t handle, const void *buf, void *context)
```

相关声明：[sensing_data_event_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga5440a8914b664209d62388183b3c89ea)、[sensing_sensor_handle_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gac959e076fcdc105dfaac1d7a984ba293)。

数据事件回调签名（Data Event Callback Signature）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 17.4\_枚举（Enumerations）

<a id="r_gabc9657708851e6a744a7cd73319efe06"></a>

```c
enum sensing_sensor_state { SENSING_SENSOR_STATE_READY = 0 , SENSING_SENSOR_STATE_OFFLINE = 1 }
```

相关声明：[sensing_sensor_state](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gabc9657708851e6a744a7cd73319efe06)、[SENSING_SENSOR_STATE_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ggabc9657708851e6a744a7cd73319efe06a735fe339796ea7b4d2387d931382ce93)、[SENSING_SENSOR_STATE_OFFLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ggabc9657708851e6a744a7cd73319efe06af23a28e861a8fa2d49b18a0fbe62600e)。

传感器状态（Sensor State）。

<a id="r_ga69d2ae9f45215742654bfc7e4676e6f2"></a>

```c
enum sensing_sensor_attribute { SENSING_SENSOR_ATTRIBUTE_INTERVAL = 0 , SENSING_SENSOR_ATTRIBUTE_SENSITIVITY = 1 , SENSING_SENSOR_ATTRIBUTE_LATENCY = 2 , SENSING_SENSOR_ATTRIBUTE_MAX }
```

相关声明：[sensing_sensor_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga69d2ae9f45215742654bfc7e4676e6f2)、[SENSING_SENSOR_ATTRIBUTE_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gga69d2ae9f45215742654bfc7e4676e6f2a8c9870b1303008b45e2caeb33f5c44a3)、[SENSING_SENSOR_ATTRIBUTE_SENSITIVITY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gga69d2ae9f45215742654bfc7e4676e6f2abc39825a643b9d1452162f057f79774b)、[SENSING_SENSOR_ATTRIBUTE_LATENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gga69d2ae9f45215742654bfc7e4676e6f2a2ccb8b476935ce27b2eedbb889e25476)、[SENSING_SENSOR_ATTRIBUTE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gga69d2ae9f45215742654bfc7e4676e6f2a072ff2aa9640503bfd8cbc8f7d271980)。

传感器配置属性（Sensor Configuration Attribute）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 17.5\_函数（Functions）

<a id="r_gaf3b6c66c2db12115f3ebec0cdba32e86"></a>

```c
int sensing_get_sensors (int *num_sensors, const struct sensing_sensor_info **info)
```

相关声明：[sensing_get_sensors](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gaf3b6c66c2db12115f3ebec0cdba32e86)、[sensing_sensor_info](../sensor_navigation_model_reference/P026_sensing_sensor_info_结构体.md)。

获取所有支持的传感器实例（Sensor Instances）的信息。

<a id="r_ga8e427d28efc492f15d762af3308d78cd"></a>

```c
int sensing_open_sensor (const struct sensing_sensor_info *info, struct sensing_callback_list *cb_list, sensing_sensor_handle_t *handle)
```

相关声明：[sensing_open_sensor](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga8e427d28efc492f15d762af3308d78cd)、[sensing_sensor_info](../sensor_navigation_model_reference/P026_sensing_sensor_info_结构体.md)、[sensing_callback_list](../sensor_navigation_model_reference/P024_sensing_callback_list_结构体.md)、[sensing_sensor_handle_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gac959e076fcdc105dfaac1d7a984ba293)。

根据传感子系统的传感器信息（Sensing Sensor Info）打开传感器实例。

<a id="r_ga4218453664fee0aa61697018e3193e7a"></a>

```c
int sensing_open_sensor_by_dt (const struct device *dev, struct sensing_callback_list *cb_list, sensing_sensor_handle_t *handle)
```

相关声明：[sensing_open_sensor_by_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga4218453664fee0aa61697018e3193e7a)、[device](../device_reference/P002_设备对象结构.md)、[sensing_callback_list](../sensor_navigation_model_reference/P024_sensing_callback_list_结构体.md)、[sensing_sensor_handle_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gac959e076fcdc105dfaac1d7a984ba293)。

根据设备（Device）打开传感器实例（Sensor Instance）。

<a id="r_ga98e49ea0e84e93867df20033d01ee66c"></a>

```c
int sensing_close_sensor (sensing_sensor_handle_t *handle)
```

相关声明：[sensing_close_sensor](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga98e49ea0e84e93867df20033d01ee66c)、[sensing_sensor_handle_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gac959e076fcdc105dfaac1d7a984ba293)。

关闭传感器实例（Sensor Instance）。

<a id="r_ga46591a2d29f5b5e160a72bbe289884ab"></a>

```c
int sensing_set_config (sensing_sensor_handle_t handle, struct sensing_sensor_config *configs, int count)
```

相关声明：[sensing_set_config](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga46591a2d29f5b5e160a72bbe289884ab)、[sensing_sensor_handle_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gac959e076fcdc105dfaac1d7a984ba293)、[sensing_sensor_config](../sensor_navigation_model_reference/P025_sensing_sensor_config_结构体.md)。

向传感子系统（Sensing Subsystem）设置当前配置项（Config Items）。

<a id="r_gaf4037066c9a7a9f3eb1c79a4d8ae0920"></a>

```c
int sensing_get_config (sensing_sensor_handle_t handle, struct sensing_sensor_config *configs, int count)
```

相关声明：[sensing_get_config](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gaf4037066c9a7a9f3eb1c79a4d8ae0920)、[sensing_sensor_handle_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gac959e076fcdc105dfaac1d7a984ba293)、[sensing_sensor_config](../sensor_navigation_model_reference/P025_sensing_sensor_config_结构体.md)。

从传感子系统（Sensing Subsystem）获取当前配置项（Config Items）。

<a id="r_ga4399f2e03d4d9444045b705b13cb6dfd"></a>

```c
const struct sensing_sensor_info * sensing_get_sensor_info (sensing_sensor_handle_t handle)
```

相关声明：[sensing_sensor_info](../sensor_navigation_model_reference/P026_sensing_sensor_info_结构体.md)、[sensing_get_sensor_info](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga4399f2e03d4d9444045b705b13cb6dfd)、[sensing_sensor_handle_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gac959e076fcdc105dfaac1d7a984ba293)。

根据传感器实例句柄（Sensor Instance Handle）获取传感器信息。


## 17.6\_原页交叉引用（Cross References）

- [zephyr/sensing/sensing_datatypes.h](../api_source_reference/P758_sensing_datatypes.h_源码浏览.md)
- [zephyr/sensing/sensing_sensor_types.h](../api_source_reference/P760_sensing_sensor_types.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P757_sensing.h_源码浏览.md)
- [sensing_sensor_version](../sensor_navigation_model_reference/P032_sensing_sensor_version_结构体.md)
- [sensing_sensor_info](../sensor_navigation_model_reference/P026_sensing_sensor_info_结构体.md)
- [sensing_callback_list](../sensor_navigation_model_reference/P024_sensing_callback_list_结构体.md)
- [sensing_sensor_config](../sensor_navigation_model_reference/P025_sensing_sensor_config_结构体.md)
- [SENSING_SENSOR_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga180bc8c822f125204964f3c667464273)
- [SENSING_SENSITIVITY_INDEX_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga16ac7bd397836280f7e8b4aa82f8eb4c)
- [SENSING_SENSOR_FLAG_REPORT_ON_EVENT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga498dcf4dbd0eb42d8ca399df4acc2e5e)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [SENSING_SENSOR_FLAG_REPORT_ON_CHANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga8b9766509e66fd8b8fa8e718a1544137)
- [sensing_sensor_handle_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gac959e076fcdc105dfaac1d7a984ba293)
- [sensing_data_event_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga5440a8914b664209d62388183b3c89ea)
- [sensing_sensor_state](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gabc9657708851e6a744a7cd73319efe06)
- [SENSING_SENSOR_STATE_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ggabc9657708851e6a744a7cd73319efe06a735fe339796ea7b4d2387d931382ce93)
- [SENSING_SENSOR_STATE_OFFLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ggabc9657708851e6a744a7cd73319efe06af23a28e861a8fa2d49b18a0fbe62600e)
- [sensing_sensor_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga69d2ae9f45215742654bfc7e4676e6f2)
- [SENSING_SENSOR_ATTRIBUTE_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gga69d2ae9f45215742654bfc7e4676e6f2a8c9870b1303008b45e2caeb33f5c44a3)
- [SENSING_SENSOR_ATTRIBUTE_SENSITIVITY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gga69d2ae9f45215742654bfc7e4676e6f2abc39825a643b9d1452162f057f79774b)
- [SENSING_SENSOR_ATTRIBUTE_LATENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gga69d2ae9f45215742654bfc7e4676e6f2a2ccb8b476935ce27b2eedbb889e25476)
- [SENSING_SENSOR_ATTRIBUTE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gga69d2ae9f45215742654bfc7e4676e6f2a072ff2aa9640503bfd8cbc8f7d271980)
- [sensing_get_sensors](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gaf3b6c66c2db12115f3ebec0cdba32e86)
- [sensing_open_sensor](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga8e427d28efc492f15d762af3308d78cd)
- [sensing_open_sensor_by_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga4218453664fee0aa61697018e3193e7a)
- [device](../device_reference/P002_设备对象结构.md)
- [sensing_close_sensor](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga98e49ea0e84e93867df20033d01ee66c)
- [sensing_set_config](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga46591a2d29f5b5e160a72bbe289884ab)
- [sensing_get_config](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gaf4037066c9a7a9f3eb1c79a4d8ae0920)
- [sensing_get_sensor_info](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga4399f2e03d4d9444045b705b13cb6dfd)

<a id="header-details"></a>

---

[上一章](P016_zephyr__drivers__misc__flexram__nxp_flexram.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P018_zephyr__dt-bindings__pinctrl__sf32lb-common-pinctrl.h_文件参考.md)
