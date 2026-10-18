---
id: learning.zephyr-docs.api-file-interface-reference.page-24
title: zephyr__input__input_analog_axis.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/input__analog__axis_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_zephyr\_\_input\_\_input\_analog\_axis.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/input__analog__axis_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

与模拟轴输入设备（Analog Axis Input Devices）交互的主头文件。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/device.h>
```

查看此文件的源码。

与模拟轴输入设备（Analog Axis Input Devices）交互的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 24.1\_数据结构（Data Structures）

<a id="r_analog_5Faxis_5Fcalibration"></a>

```c
struct analog_axis_calibration
```

相关声明：[analog_axis_calibration](../driver_model_reference/P008_模拟轴校准.md)。

模拟轴校准数据结构（Analog Axis Calibration Data Structure）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 24.2\_类型定义（Typedefs）

<a id="r_ga384e901afe29ae91e01c44b458034d64"></a>

```c
typedef void(* analog_axis_raw_data_t) (const struct device *dev, int channel, int16_t raw_val)
```

相关声明：[analog_axis_raw_data_t](https://docs.zephyrproject.org/latest/doxygen/html/group__input__analog__axis.html#ga384e901afe29ae91e01c44b458034d64)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

模拟轴（analog axis）原始数据回调。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 24.3\_函数（Functions）

<a id="r_ga645237cdb40113e4253a24e902091f3e"></a>

```c
void analog_axis_set_raw_data_cb (const struct device *dev, analog_axis_raw_data_t cb)
```

相关声明：[analog_axis_set_raw_data_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__input__analog__axis.html#ga645237cdb40113e4253a24e902091f3e)、[device](../device_reference/P002_设备对象结构.md)、[analog_axis_raw_data_t](https://docs.zephyrproject.org/latest/doxygen/html/group__input__analog__axis.html#ga384e901afe29ae91e01c44b458034d64)。

设置原始数据回调（raw data callback）。

<a id="r_ga99dd3b96a43f115a8c90859e7eed24d4"></a>

```c
int analog_axis_num_axes (const struct device *dev)
```

相关声明：[analog_axis_num_axes](https://docs.zephyrproject.org/latest/doxygen/html/group__input__analog__axis.html#ga99dd3b96a43f115a8c90859e7eed24d4)、[device](../device_reference/P002_设备对象结构.md)。

获取已定义轴（axes）的数量。

<a id="r_gad359f00fa9c46219a55a218d26d0407a"></a>

```c
int analog_axis_calibration_get (const struct device *dev, int channel, struct analog_axis_calibration *cal)
```

相关声明：[analog_axis_calibration_get](https://docs.zephyrproject.org/latest/doxygen/html/group__input__analog__axis.html#gad359f00fa9c46219a55a218d26d0407a)、[device](../device_reference/P002_设备对象结构.md)、[analog_axis_calibration](../driver_model_reference/P008_模拟轴校准.md)。

获取轴的校准数据（calibration data）。

<a id="r_gaae496bde41a58d92521b0a24f762caeb"></a>

```c
int analog_axis_calibration_set (const struct device *dev, int channel, struct analog_axis_calibration *cal)
```

相关声明：[analog_axis_calibration_set](https://docs.zephyrproject.org/latest/doxygen/html/group__input__analog__axis.html#gaae496bde41a58d92521b0a24f762caeb)、[device](../device_reference/P002_设备对象结构.md)、[analog_axis_calibration](../driver_model_reference/P008_模拟轴校准.md)。

设置轴的校准数据。


## 24.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P377_input_analog_axis.h_源码浏览.md)
- [analog_axis_calibration](../driver_model_reference/P008_模拟轴校准.md)
- [analog_axis_raw_data_t](https://docs.zephyrproject.org/latest/doxygen/html/group__input__analog__axis.html#ga384e901afe29ae91e01c44b458034d64)
- [device](../device_reference/P002_设备对象结构.md)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [analog_axis_set_raw_data_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__input__analog__axis.html#ga645237cdb40113e4253a24e902091f3e)
- [analog_axis_num_axes](https://docs.zephyrproject.org/latest/doxygen/html/group__input__analog__axis.html#ga99dd3b96a43f115a8c90859e7eed24d4)
- [analog_axis_calibration_get](https://docs.zephyrproject.org/latest/doxygen/html/group__input__analog__axis.html#gad359f00fa9c46219a55a218d26d0407a)
- [analog_axis_calibration_set](https://docs.zephyrproject.org/latest/doxygen/html/group__input__analog__axis.html#gaae496bde41a58d92521b0a24f762caeb)

<a id="header-details"></a>

---

[上一章](P023_zephyr__dt-bindings__interrupt-controller__infineon-xmc4xxx-intc.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P025_zephyr__input__input_touch.h_文件参考.md)
