---
id: learning.zephyr-docs.api-file-management-reference.page-16
title: zephyr__drivers__misc__ft8xx__ft8xx.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ft8xx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_zephyr\_\_drivers\_\_misc\_\_ft8xx\_\_ft8xx.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ft8xx_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

FT8XX公共API（Public API）。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/device.h>
```

查看此文件的源码。

FT8XX公共API（Public API）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 16.1\_数据结构（Data Structures）

<a id="r_ft8xx_5Ftouch_5Ftransform"></a>

```c
struct ft8xx_touch_transform
```

相关声明：[ft8xx_touch_transform](../sensor_navigation_model_reference/P008_ft8xx_touch_transform_结构体.md)。

保存触摸屏校准数据（Touchscreen Calibration Data）的结构。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 16.2\_类型定义（Typedefs）

<a id="r_ga846a90d72b56f388d5b4f60cf6d658b0"></a>

```c
typedef void(* ft8xx_int_callback) (const struct device *dev, void *user_data)
```

相关声明：[ft8xx_int_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__interface.html#ga846a90d72b56f388d5b4f60cf6d658b0)、[device](../device_reference/P002_设备对象结构.md)。

用于通知 API 用户 FT8xx 已触发中断的回调 API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 16.3\_函数（Functions）

<a id="r_ga586f6ff1eddd5b596d2e35fb5fdd8148"></a>

```c
void ft8xx_calibrate (const struct device *dev, struct ft8xx_touch_transform *data)
```

相关声明：[ft8xx_calibrate](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__interface.html#ga586f6ff1eddd5b596d2e35fb5fdd8148)、[device](../device_reference/P002_设备对象结构.md)、[ft8xx_touch_transform](../sensor_navigation_model_reference/P008_ft8xx_touch_transform_结构体.md)。

校准触摸屏（touchscreen calibration）。

<a id="r_ga1d74a13782c6ab9f8b07a28503058356"></a>

```c
void ft8xx_touch_transform_set (const struct device *dev, const struct ft8xx_touch_transform *data)
```

相关声明：[ft8xx_touch_transform_set](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__interface.html#ga1d74a13782c6ab9f8b07a28503058356)、[device](../device_reference/P002_设备对象结构.md)、[ft8xx_touch_transform](../sensor_navigation_model_reference/P008_ft8xx_touch_transform_结构体.md)。

设置触摸屏校准数据。

<a id="r_gaea3589b5a0aa34a09a81ea15c1595219"></a>

```c
int ft8xx_get_touch_tag (const struct device *dev)
```

相关声明：[ft8xx_get_touch_tag](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__interface.html#gaea3589b5a0aa34a09a81ea15c1595219)、[device](../device_reference/P002_设备对象结构.md)。

获取最近触摸元素的标签（tag）。

<a id="r_ga1c9ade4374b9619c68efa11dd1a56eae"></a>

```c
uint32_t ft8xx_get_tracker_value (const struct device *dev)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[ft8xx_get_tracker_value](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__interface.html#ga1c9ade4374b9619c68efa11dd1a56eae)、[device](../device_reference/P002_设备对象结构.md)。

获取被跟踪对象的标签及跟踪值（tracking value）。

<a id="r_gaf392199312ddb82451a4f31e2955079d"></a>

```c
void ft8xx_register_int (const struct device *dev, ft8xx_int_callback callback, void *user_data)
```

相关声明：[ft8xx_register_int](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__interface.html#gaf392199312ddb82451a4f31e2955079d)、[device](../device_reference/P002_设备对象结构.md)、[ft8xx_int_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__interface.html#ga846a90d72b56f388d5b4f60cf6d658b0)。

设置 FT8xx 触发中断时执行的回调。


## 16.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_architecture_reference/P008_ft8xx.h_源码浏览.md)
- [ft8xx_touch_transform](../sensor_navigation_model_reference/P008_ft8xx_touch_transform_结构体.md)
- [ft8xx_int_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__interface.html#ga846a90d72b56f388d5b4f60cf6d658b0)
- [device](../device_reference/P002_设备对象结构.md)
- [ft8xx_calibrate](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__interface.html#ga586f6ff1eddd5b596d2e35fb5fdd8148)
- [ft8xx_touch_transform_set](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__interface.html#ga1d74a13782c6ab9f8b07a28503058356)
- [ft8xx_get_touch_tag](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__interface.html#gaea3589b5a0aa34a09a81ea15c1595219)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [ft8xx_get_tracker_value](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__interface.html#ga1c9ade4374b9619c68efa11dd1a56eae)
- [ft8xx_register_int](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__interface.html#gaf392199312ddb82451a4f31e2955079d)

<a id="header-details"></a>

---

[上一章](P015_zephyr__mgmt__mcumgr__grp__fs_mgmt__fs_mgmt.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P017_zephyr__drivers__misc__ft8xx__ft8xx_common.h_文件参考.md)
