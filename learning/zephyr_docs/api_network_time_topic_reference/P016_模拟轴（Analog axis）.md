---
id: learning.zephyr-docs.api-network-time-topic-reference.page-16
title: 模拟轴（Analog axis）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__input__analog__axis.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_模拟轴（Analog axis）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__input__analog__axis.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 16.1\_文件（Files）

<a id="r_input_5Fanalog_5Faxis_2Eh"></a>

```c
file input_analog_axis.h
```

相关声明：[input_analog_axis.h](../api_file_interface_reference/P024_zephyr__input__input_analog_axis.h_文件参考.md)。

与模拟轴输入设备（Analog Axis Input Devices）交互的主头文件。

<a id="r_input_5Fanalog_5Faxis_5Fsettings_2Eh"></a>

```c
file input_analog_axis_settings.h
```

相关声明：[input_analog_axis_settings.h](../api_file_supplement_reference/P047_zephyr__input__input_analog_axis_settings.h_文件参考.md)。

可保存模拟轴校准数据（Analog Axis Calibration Data）的API公共头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 16.2\_数据结构（Data Structures）

<a id="r_analog_5Faxis_5Fcalibration"></a>

```c
struct analog_axis_calibration
```

相关声明：[analog_axis_calibration](../driver_model_reference/P008_模拟轴校准.md)。

模拟轴校准数据结构（Analog Axis Calibration Data Structure）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 16.3\_类型定义（Typedefs）

<a id="r_ga384e901afe29ae91e01c44b458034d64"></a>

```c
typedef void(* analog_axis_raw_data_t) (const struct device *dev, int channel, int16_t raw_val)
```

相关声明：[analog_axis_raw_data_t](#ga384e901afe29ae91e01c44b458034d64)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

模拟轴（analog axis）原始数据回调。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 16.4\_函数（Functions）

<a id="r_ga645237cdb40113e4253a24e902091f3e"></a>

```c
void analog_axis_set_raw_data_cb (const struct device *dev, analog_axis_raw_data_t cb)
```

相关声明：[analog_axis_set_raw_data_cb](#ga645237cdb40113e4253a24e902091f3e)、[device](../device_reference/P002_设备对象结构.md)、[analog_axis_raw_data_t](#ga384e901afe29ae91e01c44b458034d64)。

设置原始数据回调（raw data callback）。

<a id="r_ga99dd3b96a43f115a8c90859e7eed24d4"></a>

```c
int analog_axis_num_axes (const struct device *dev)
```

相关声明：[analog_axis_num_axes](#ga99dd3b96a43f115a8c90859e7eed24d4)、[device](../device_reference/P002_设备对象结构.md)。

获取已定义轴（axes）的数量。

<a id="r_gad359f00fa9c46219a55a218d26d0407a"></a>

```c
int analog_axis_calibration_get (const struct device *dev, int channel, struct analog_axis_calibration *cal)
```

相关声明：[analog_axis_calibration_get](#gad359f00fa9c46219a55a218d26d0407a)、[device](../device_reference/P002_设备对象结构.md)、[analog_axis_calibration](../driver_model_reference/P008_模拟轴校准.md)。

获取轴的校准数据（calibration data）。

<a id="r_gaae496bde41a58d92521b0a24f762caeb"></a>

```c
int analog_axis_calibration_set (const struct device *dev, int channel, struct analog_axis_calibration *cal)
```

相关声明：[analog_axis_calibration_set](#gaae496bde41a58d92521b0a24f762caeb)、[device](../device_reference/P002_设备对象结构.md)、[analog_axis_calibration](../driver_model_reference/P008_模拟轴校准.md)。

设置轴的校准数据。

<a id="r_ga56973ef7c7a465defdb7bd2934c86778"></a>

```c
int analog_axis_calibration_save (const struct device *dev)
```

相关声明：[analog_axis_calibration_save](#ga56973ef7c7a465defdb7bd2934c86778)、[device](../device_reference/P002_设备对象结构.md)。

保存校准数据（Calibration Data）。

## 16.5\_详细说明（Detailed Documentation）

<a id="ga384e901afe29ae91e01c44b458034d64"></a>

### `analog_axis_raw_data_t`

```c
typedef void(* analog_axis_raw_data_t) (const struct device *dev, int channel, int16_t raw_val)
```

```c
#include <zephyr/input/input_analog_axis.h>
```

模拟轴（analog axis）原始数据回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 模拟轴设备（analog axis device）。 |
| `channel` | 通道编号。 |
| `raw_val` | 通道的原始值（raw value）。 |

<a id="gad359f00fa9c46219a55a218d26d0407a"></a>

### `analog_axis_calibration_get()`

```c
int analog_axis_calibration_get ( const struct device * dev, int channel, struct analog_axis_calibration * cal )
```

```c
#include <zephyr/input/input_analog_axis.h>
```

获取轴的校准数据（calibration data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 模拟轴设备（analog axis device）。 |
| `channel` | 通道编号。 |
| `cal` | 指向 `analog_axis_calibration` 结构体的指针，该结构体将被填入当前校准数据（calibration data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EINVAL` | 指定通道无效时。 |

<a id="ga56973ef7c7a465defdb7bd2934c86778"></a>

### `analog_axis_calibration_save()`

```c
int analog_axis_calibration_save ( const struct device * dev)
```

```c
#include <zephyr/input/input_analog_axis_settings.h>
```

保存校准数据（Calibration Data）。

将校准数据永久保存到指定设备；要求已配置并初始化设置子系统（Settings subsystem）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 模拟轴设备（analog axis device）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-errno` | 发生任何其他错误时。 |

<a id="gaae496bde41a58d92521b0a24f762caeb"></a>

### `analog_axis_calibration_set()`

```c
int analog_axis_calibration_set ( const struct device * dev, int channel, struct analog_axis_calibration * cal )
```

```c
#include <zephyr/input/input_analog_axis.h>
```

设置轴的校准数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 模拟轴设备（analog axis device）。 |
| `channel` | 通道编号。 |
| `cal` | 指向包含新校准数据的 `analog_axis_calibration` 结构体的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EINVAL` | 指定通道无效时。 |

<a id="ga99dd3b96a43f115a8c90859e7eed24d4"></a>

### `analog_axis_num_axes()`

```c
int analog_axis_num_axes ( const struct device * dev)
```

```c
#include <zephyr/input/input_analog_axis.h>
```

获取已定义轴（axes）的数量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 模拟轴设备（analog axis device）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `n` | `dev` 已定义的轴数量。 |

<a id="ga645237cdb40113e4253a24e902091f3e"></a>

### `analog_axis_set_raw_data_cb()`

```c
void analog_axis_set_raw_data_cb ( const struct device * dev, analog_axis_raw_data_t cb )
```

```c
#include <zephyr/input/input_analog_axis.h>
```

设置原始数据回调（raw data callback）。

设置回调，以接收指定模拟轴设备的原始数据。应用程序可借此获取校准所需数据。将 `cb` 设为 `NULL` 可禁用回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 模拟轴设备（analog axis device）。 |
| `cb` | 要使用的 `analog_axis_raw_data_t` 回调，设为 `NULL` 则禁用。 |


## 16.6\_原页交叉引用（Cross References）

- [input_analog_axis.h](../api_file_interface_reference/P024_zephyr__input__input_analog_axis.h_文件参考.md)
- [input_analog_axis_settings.h](../api_file_supplement_reference/P047_zephyr__input__input_analog_axis_settings.h_文件参考.md)
- [analog_axis_calibration](../driver_model_reference/P008_模拟轴校准.md)
- [device](../device_reference/P002_设备对象结构.md)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [设置（Settings）。](../storage/P063_设置子系统接口.md)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P015_IIS2ICLX API主题.md) · [返回大纲](大纲.md) · [下一章](P017_指令内存接口（Instruction Memory APIs）.md)
