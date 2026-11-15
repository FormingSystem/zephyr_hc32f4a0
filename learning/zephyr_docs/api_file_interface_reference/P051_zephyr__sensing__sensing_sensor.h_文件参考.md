---
id: learning.zephyr-docs.api-file-interface-reference.page-51
title: zephyr__sensing__sensing_sensor.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sensing__sensor_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第51章\_zephyr\_\_sensing\_\_sensing\_sensor.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sensing__sensor_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

感知子系统（Sensing Subsystem）传感器API的头文件。

<a id="details"></a>

```c
#include <stdbool.h>
#include <zephyr/device.h>
#include <zephyr/drivers/sensor.h>
#include <zephyr/sensing/sensing.h>
```

查看此文件的源码。

感知子系统（Sensing Subsystem）传感器API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 51.1\_数据结构（Data Structures）

<a id="r_sensing_5Fsensor_5Fregister_5Finfo"></a>

```c
struct sensing_sensor_register_info
```

相关声明：[sensing_sensor_register_info](../sensor_navigation_model_reference/P027_sensing_sensor_register_info_结构体.md)。

传感器注册信息（Sensor Registration Information）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 51.2\_宏定义（Macros）

<a id="r_gad5a9ccb04d96efc57078e880ca28b654"></a>

```c
#define SENSING_SENSORS_DT_DEFINE(node, reg_ptr, cb_list_ptr, init_fn, pm_device, data_ptr, cfg_ptr, level, prio, api_ptr, ...)
```

相关声明：[SENSING_SENSORS_DT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__sensor.html#gad5a9ccb04d96efc57078e880ca28b654)、[pm_device](../power/P039_通用设备运行时电源结构.md)。

与 `SENSOR_DEVICE_DT_DEFINE()` 类似，但加入感知子系统（sensing）的专用处理。

<a id="r_gae3c7a2acba53cc524a4b1043df49fe85"></a>

```c
#define SENSING_SENSORS_DT_INST_DEFINE(inst, ...)
```

相关声明：[SENSING_SENSORS_DT_INST_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__sensor.html#gae3c7a2acba53cc524a4b1043df49fe85)。

与 `SENSING_SENSORS_DT_DEFINE()` 类似，但用于兼容 `DT_DRV_COMPAT` 的实例。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 51.3\_函数（Functions）

<a id="r_gab4c41d02b3731e5829a41e1f5f5154a5"></a>

```c
int sensing_sensor_get_reporters (const struct device *dev, int type, sensing_sensor_handle_t *reporter_handles, int max_handles)
```

相关声明：[sensing_sensor_get_reporters](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__sensor.html#gab4c41d02b3731e5829a41e1f5f5154a5)、[device](../device_reference/P002_设备对象结构.md)、[sensing_sensor_handle_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gac959e076fcdc105dfaac1d7a984ba293)。

按传感器类型获取指定传感器实例的上报器句柄（reporter handles）。

<a id="r_ga2c5cfb298b2dfde967edfdd987115021"></a>

```c
int sensing_sensor_get_reporters_count (const struct device *dev, int type)
```

相关声明：[sensing_sensor_get_reporters_count](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__sensor.html#ga2c5cfb298b2dfde967edfdd987115021)、[device](../device_reference/P002_设备对象结构.md)。

按传感器类型获取指定传感器实例的上报器数量（reporters count）。

<a id="r_gab9446a3085b6b05da448dce59db50387"></a>

```c
int sensing_sensor_get_state (const struct device *dev, enum sensing_sensor_state *state)
```

相关声明：[sensing_sensor_get_state](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__sensor.html#gab9446a3085b6b05da448dce59db50387)、[device](../device_reference/P002_设备对象结构.md)、[sensing_sensor_state](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gabc9657708851e6a744a7cd73319efe06)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

获取此传感器的状态（state）。


## 51.4\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [zephyr/sensing/sensing.h](../api_source_reference/P757_sensing.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P759_sensing_sensor.h_源码浏览.md)
- [sensing_sensor_register_info](../sensor_navigation_model_reference/P027_sensing_sensor_register_info_结构体.md)
- [SENSING_SENSORS_DT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__sensor.html#gad5a9ccb04d96efc57078e880ca28b654)
- [pm_device](../power/P039_通用设备运行时电源结构.md)
- [SENSOR_DEVICE_DT_DEFINE()](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaa67ca630e3931a0c3821ba438c86690c)
- [SENSING_SENSORS_DT_INST_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__sensor.html#gae3c7a2acba53cc524a4b1043df49fe85)
- [sensing_sensor_get_reporters](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__sensor.html#gab4c41d02b3731e5829a41e1f5f5154a5)
- [device](../device_reference/P002_设备对象结构.md)
- [sensing_sensor_handle_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gac959e076fcdc105dfaac1d7a984ba293)
- [sensing_sensor_get_reporters_count](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__sensor.html#ga2c5cfb298b2dfde967edfdd987115021)
- [sensing_sensor_get_state](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__sensor.html#gab9446a3085b6b05da448dce59db50387)
- [sensing_sensor_state](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gabc9657708851e6a744a7cd73319efe06)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)

<a id="header-details"></a>

---

[上一章](P050_zephyr__drivers__clock_control__renesas_rz_cgc.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P052_zephyr__mgmt__mcumgr__grp__settings_mgmt__settings_mgmt.h_文件参考.md)
