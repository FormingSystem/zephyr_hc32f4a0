---
id: learning.zephyr-docs.api-file-storage-event-reference.page-19
title: zephyr__drivers__stepper__stepper.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stepper_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_zephyr\_\_drivers\_\_stepper\_\_stepper.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stepper_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

步进电机硬件驱动器（Stepper Hardware Driver）API的主头文件。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <errno.h>
#include <zephyr/syscalls/stepper.h>
```

查看此文件的源码。

步进电机硬件驱动器（Stepper Hardware Driver）API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 19.1\_数据结构（Data Structures）

<a id="r_stepper_5Fdriver_5Fapi"></a>

```c
struct stepper_driver_api
```

相关声明：[stepper_driver_api](../hardware/P236_步进硬件驱动函数表.md)。

驱动操作（Driver Operations）：步进电机硬件驱动器（Stepper Hardware Driver）的驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 19.2\_宏定义（Macros）

<a id="r_ga49df951f1b18bd399a609842514bdbc1"></a>

```c
#define MICRO_STEP_RES_INDEX(res)
```

相关声明：[MICRO_STEP_RES_INDEX](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ga49df951f1b18bd399a609842514bdbc1)。

计算微步分辨率索引（Microstep Resolution Index）的宏。

<a id="r_ga3196866d26d23c04313d802f2d8c61c1"></a>

```c
#define VALID_MICRO_STEP_RES(res)
```

相关声明：[VALID_MICRO_STEP_RES](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ga3196866d26d23c04313d802f2d8c61c1)。

检查微步分辨率（Microstep Resolution）是否有效。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 19.3\_类型定义（Typedefs）

<a id="r_ga7df452f0e21c8db860616a9e8854b11a"></a>

```c
typedef void(* stepper_event_cb_t) (const struct device *dev, const enum stepper_event event, void *user_data)
```

相关声明：[stepper_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ga7df452f0e21c8db860616a9e8854b11a)、[device](../device_reference/P002_设备对象结构.md)、[stepper_event](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#gab1534238fbf8d2270ea4f69d3a558b5f)。

步进驱动事件（Stepper Driver Events）的回调函数。

<a id="r_gab72c41a4685429cdb01365c66a247bb8"></a>

```c
typedef int(* stepper_enable_t) (const struct device *dev)
```

相关声明：[stepper_enable_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver__backend.html#gab72c41a4685429cdb01365c66a247bb8)、[device](../device_reference/P002_设备对象结构.md)。

启用步进硬件驱动器（Stepper Hardware Driver）的回调 API。

<a id="r_ga3bdb240620979bb7c1aec00bdc1e7391"></a>

```c
typedef int(* stepper_disable_t) (const struct device *dev)
```

相关声明：[stepper_disable_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver__backend.html#ga3bdb240620979bb7c1aec00bdc1e7391)、[device](../device_reference/P002_设备对象结构.md)。

禁用步进硬件驱动器（Stepper Hardware Driver）的回调 API。

<a id="r_ga01d81191585ac83ca1cdd2bcff16e7cb"></a>

```c
typedef int(* stepper_set_micro_step_res_t) (const struct device *dev, const enum stepper_micro_step_resolution resolution)
```

相关声明：[stepper_set_micro_step_res_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver__backend.html#ga01d81191585ac83ca1cdd2bcff16e7cb)、[device](../device_reference/P002_设备对象结构.md)、[stepper_micro_step_resolution](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#gad8d053f92eb3a194652b4600af531e30)。

设置步进微步分辨率（Stepper Micro-step Resolution）的回调 API。

<a id="r_gae2e5fe2ffa722cafe649bc6fbd945296"></a>

```c
typedef int(* stepper_get_micro_step_res_t) (const struct device *dev, enum stepper_micro_step_resolution *resolution)
```

相关声明：[stepper_get_micro_step_res_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver__backend.html#gae2e5fe2ffa722cafe649bc6fbd945296)、[device](../device_reference/P002_设备对象结构.md)、[stepper_micro_step_resolution](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#gad8d053f92eb3a194652b4600af531e30)。

获取步进微步分辨率（Stepper Micro-step Resolution）的回调 API。

<a id="r_gac903b636e01a33fa52882f0d70e745b3"></a>

```c
typedef int(* stepper_set_event_cb_t) (const struct device *dev, stepper_event_cb_t callback, void *user_data)
```

相关声明：[stepper_set_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver__backend.html#gac903b636e01a33fa52882f0d70e745b3)、[device](../device_reference/P002_设备对象结构.md)、[stepper_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ga7df452f0e21c8db860616a9e8854b11a)。

设置事件回调函数（Event Callback Function）的回调 API。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 19.4\_枚举（Enumerations）

<a id="r_gad8d053f92eb3a194652b4600af531e30"></a>

```c
enum stepper_micro_step_resolution { STEPPER_MICRO_STEP_1 = 1 , STEPPER_MICRO_STEP_2 = 2 , STEPPER_MICRO_STEP_4 = 4 , STEPPER_MICRO_STEP_8 = 8 , STEPPER_MICRO_STEP_16 = 16 , STEPPER_MICRO_STEP_32 = 32 , STEPPER_MICRO_STEP_64 = 64 , STEPPER_MICRO_STEP_128 = 128 , STEPPER_MICRO_STEP_256 = 256 }
```

相关声明：[stepper_micro_step_resolution](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#gad8d053f92eb3a194652b4600af531e30)、[STEPPER_MICRO_STEP_1](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggad8d053f92eb3a194652b4600af531e30a4c72780b13eb7f5ee5c433420a0eede9)、[STEPPER_MICRO_STEP_2](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggad8d053f92eb3a194652b4600af531e30a6f42ccb9a398946ce4eeac20c364f990)、[STEPPER_MICRO_STEP_4](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggad8d053f92eb3a194652b4600af531e30a4c5dd8c5054a1a66e65cceba719ca5e0)、[STEPPER_MICRO_STEP_8](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggad8d053f92eb3a194652b4600af531e30aae2b109417f88201514bedd0e2c71155)、[STEPPER_MICRO_STEP_16](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggad8d053f92eb3a194652b4600af531e30ac04236cc36c1201539f3fcc4aef1f1d8)、[STEPPER_MICRO_STEP_32](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggad8d053f92eb3a194652b4600af531e30af733d75d60220ae98bb08ee3a4c49d14)、[STEPPER_MICRO_STEP_64](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggad8d053f92eb3a194652b4600af531e30a25ea7a12d2ec3751e941f446b9637370)、[STEPPER_MICRO_STEP_128](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggad8d053f92eb3a194652b4600af531e30afc6d0ffc96256600c74b00057ec55e43)、[STEPPER_MICRO_STEP_256](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggad8d053f92eb3a194652b4600af531e30a7ff93a287c10971ac50644de2ae0161f)。

步进电机微步分辨率选项（Stepper Motor Micro-step Resolution Options）。

<a id="r_gab1534238fbf8d2270ea4f69d3a558b5f"></a>

```c
enum stepper_event { STEPPER_EVENT_STALL_DETECTED = 0 , STEPPER_EVENT_FAULT_DETECTED = 1 }
```

相关声明：[stepper_event](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#gab1534238fbf8d2270ea4f69d3a558b5f)、[STEPPER_EVENT_STALL_DETECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggab1534238fbf8d2270ea4f69d3a558b5fa99db863b18d3e004a06de3f7d1abe445)、[STEPPER_EVENT_FAULT_DETECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggab1534238fbf8d2270ea4f69d3a558b5faa1811857d120f56e0e7646457fc9e7d4)。

步进硬件驱动器事件（Stepper Hardware Driver Events）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 19.5\_函数（Functions）

<a id="r_ga3395b5f8b401d8175067edfb25c2e0e8"></a>

```c
int stepper_enable (const struct device *dev)
```

相关声明：[stepper_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ga3395b5f8b401d8175067edfb25c2e0e8)、[device](../device_reference/P002_设备对象结构.md)。

启用步进硬件驱动器（Stepper Hardware Driver）。

<a id="r_gab892a6b8d8fb34db0e682dd8f7de4218"></a>

```c
int stepper_disable (const struct device *dev)
```

相关声明：[stepper_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#gab892a6b8d8fb34db0e682dd8f7de4218)、[device](../device_reference/P002_设备对象结构.md)。

禁用步进硬件驱动器（Stepper Hardware Driver）。

<a id="r_ga609ddefa299ba40a997c626e4a36bdef"></a>

```c
int stepper_set_micro_step_res (const struct device *dev, enum stepper_micro_step_resolution res)
```

相关声明：[stepper_set_micro_step_res](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ga609ddefa299ba40a997c626e4a36bdef)、[device](../device_reference/P002_设备对象结构.md)、[stepper_micro_step_resolution](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#gad8d053f92eb3a194652b4600af531e30)。

设置步进硬件驱动器的微步分辨率（Micro-step Resolution）。

<a id="r_gaa5e17e04a470832a305cef048694ec0a"></a>

```c
int stepper_get_micro_step_res (const struct device *dev, enum stepper_micro_step_resolution *res)
```

相关声明：[stepper_get_micro_step_res](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#gaa5e17e04a470832a305cef048694ec0a)、[device](../device_reference/P002_设备对象结构.md)、[stepper_micro_step_resolution](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#gad8d053f92eb3a194652b4600af531e30)。

获取步进硬件驱动器的微步分辨率（Micro-step Resolution）。

<a id="r_gad9fff2d103daad42fe49c7bbd5233b1b"></a>

```c
int stepper_set_event_cb (const struct device *dev, stepper_event_cb_t callback, void *user_data)
```

相关声明：[stepper_set_event_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#gad9fff2d103daad42fe49c7bbd5233b1b)、[device](../device_reference/P002_设备对象结构.md)、[stepper_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ga7df452f0e21c8db860616a9e8854b11a)。

设置发生 `stepper_event` 时调用的回调函数（Callback Function）。


## 19.6\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P820_stepper.h_源码浏览.md)
- [stepper_driver_api](../hardware/P236_步进硬件驱动函数表.md)
- [MICRO_STEP_RES_INDEX](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ga49df951f1b18bd399a609842514bdbc1)
- [VALID_MICRO_STEP_RES](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ga3196866d26d23c04313d802f2d8c61c1)
- [stepper_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ga7df452f0e21c8db860616a9e8854b11a)
- [device](../device_reference/P002_设备对象结构.md)
- [stepper_event](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#gab1534238fbf8d2270ea4f69d3a558b5f)
- [stepper_enable_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver__backend.html#gab72c41a4685429cdb01365c66a247bb8)
- [stepper_disable_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver__backend.html#ga3bdb240620979bb7c1aec00bdc1e7391)
- [stepper_set_micro_step_res_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver__backend.html#ga01d81191585ac83ca1cdd2bcff16e7cb)
- [stepper_micro_step_resolution](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#gad8d053f92eb3a194652b4600af531e30)
- [stepper_get_micro_step_res_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver__backend.html#gae2e5fe2ffa722cafe649bc6fbd945296)
- [stepper_set_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver__backend.html#gac903b636e01a33fa52882f0d70e745b3)
- [STEPPER_MICRO_STEP_1](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggad8d053f92eb3a194652b4600af531e30a4c72780b13eb7f5ee5c433420a0eede9)
- [STEPPER_MICRO_STEP_2](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggad8d053f92eb3a194652b4600af531e30a6f42ccb9a398946ce4eeac20c364f990)
- [STEPPER_MICRO_STEP_4](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggad8d053f92eb3a194652b4600af531e30a4c5dd8c5054a1a66e65cceba719ca5e0)
- [STEPPER_MICRO_STEP_8](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggad8d053f92eb3a194652b4600af531e30aae2b109417f88201514bedd0e2c71155)
- [STEPPER_MICRO_STEP_16](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggad8d053f92eb3a194652b4600af531e30ac04236cc36c1201539f3fcc4aef1f1d8)
- [STEPPER_MICRO_STEP_32](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggad8d053f92eb3a194652b4600af531e30af733d75d60220ae98bb08ee3a4c49d14)
- [STEPPER_MICRO_STEP_64](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggad8d053f92eb3a194652b4600af531e30a25ea7a12d2ec3751e941f446b9637370)
- [STEPPER_MICRO_STEP_128](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggad8d053f92eb3a194652b4600af531e30afc6d0ffc96256600c74b00057ec55e43)
- [STEPPER_MICRO_STEP_256](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggad8d053f92eb3a194652b4600af531e30a7ff93a287c10971ac50644de2ae0161f)
- [STEPPER_EVENT_STALL_DETECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggab1534238fbf8d2270ea4f69d3a558b5fa99db863b18d3e004a06de3f7d1abe445)
- [STEPPER_EVENT_FAULT_DETECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ggab1534238fbf8d2270ea4f69d3a558b5faa1811857d120f56e0e7646457fc9e7d4)
- [stepper_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ga3395b5f8b401d8175067edfb25c2e0e8)
- [stepper_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#gab892a6b8d8fb34db0e682dd8f7de4218)
- [stepper_set_micro_step_res](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ga609ddefa299ba40a997c626e4a36bdef)
- [stepper_get_micro_step_res](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#gaa5e17e04a470832a305cef048694ec0a)
- [stepper_set_event_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#gad9fff2d103daad42fe49c7bbd5233b1b)

<a id="header-details"></a>

---

[上一章](P018_zephyr__dt-bindings__pinctrl__sf32lb-common-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P020_____w__zephyr__zephyr__subsys__secure_storage__include__internal__zephyr__secure_storage__its__store.h_文件参考.md)
