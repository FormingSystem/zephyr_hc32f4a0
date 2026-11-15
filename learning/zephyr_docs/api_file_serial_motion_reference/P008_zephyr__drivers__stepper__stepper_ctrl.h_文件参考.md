---
id: learning.zephyr-docs.api-file-serial-motion-reference.page-8
title: zephyr__drivers__stepper__stepper_ctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stepper__ctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_zephyr\_\_drivers\_\_stepper\_\_stepper\_ctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stepper__ctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

步进电机运动控制器（Stepper Motion Controller）驱动API的主头文件。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <errno.h>
#include <zephyr/syscalls/stepper_ctrl.h>
```

查看此文件的源码。

步进电机运动控制器（Stepper Motion Controller）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 8.1\_数据结构（Data Structures）

<a id="r_stepper_5Fctrl_5Framp"></a>

```c
struct stepper_ctrl_ramp
```

相关声明：[stepper_ctrl_ramp](../hardware/P231_步进速度斜坡结构.md)。

步进电机运动控制器（Stepper Motion Controller）的斜坡参数。

<a id="r_stepper_5Fctrl_5Fdriver_5Fapi"></a>

```c
struct stepper_ctrl_driver_api
```

相关声明：[stepper_ctrl_driver_api](../hardware/P234_步进运动控制函数表.md)。

驱动操作（Driver Operations）：步进电机运动控制器（Stepper Motion Controller）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 8.2\_类型定义（Typedefs）

<a id="r_ga69198946de2a596894b1fc26a13a4c58"></a>

```c
typedef void(* stepper_ctrl_event_callback_t) (const struct device *dev, const enum stepper_ctrl_event event, void *user_data)
```

相关声明：[stepper_ctrl_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#ga69198946de2a596894b1fc26a13a4c58)、[device](../device_reference/P002_设备对象结构.md)、[stepper_ctrl_event](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#ga61dfffaeb3d7f76c34c9a9e3ab7627d0)。

步进电机运动控制器（Stepper Motion Controller）事件的回调函数。

<a id="r_ga142d6eecbaead22de75e3e3d69e23550"></a>

```c
typedef int(* stepper_ctrl_set_reference_position_t) (const struct device *dev, const int32_t value)
```

相关声明：[stepper_ctrl_set_reference_position_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl__backend.html#ga142d6eecbaead22de75e3e3d69e23550)、[device](../device_reference/P002_设备对象结构.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置步进电机运动控制器的参考位置（Reference Position）。

<a id="r_ga0d807a6415c0040fcf493d5c9c3fa5b1"></a>

```c
typedef int(* stepper_ctrl_get_actual_position_t) (const struct device *dev, int32_t *value)
```

相关声明：[stepper_ctrl_get_actual_position_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl__backend.html#ga0d807a6415c0040fcf493d5c9c3fa5b1)、[device](../device_reference/P002_设备对象结构.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

获取步进电机运动控制器的实际位置，即参考位置（Actual/Reference Position）。

<a id="r_ga1570a86e75fbcecfc63213cd144b4a5b"></a>

```c
typedef int(* stepper_ctrl_set_event_cb_t) (const struct device *dev, stepper_ctrl_event_callback_t callback, void *user_data)
```

相关声明：[stepper_ctrl_set_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl__backend.html#ga1570a86e75fbcecfc63213cd144b4a5b)、[device](../device_reference/P002_设备对象结构.md)、[stepper_ctrl_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#ga69198946de2a596894b1fc26a13a4c58)。

设置在步进电机运动控制器（Stepper Motion Controller）事件发生时调用的回调函数。

<a id="r_gac78bf81389bd3013fea18caca0e77e54"></a>

```c
typedef int(* stepper_ctrl_set_microstep_interval_t) (const struct device *dev, const uint64_t microstep_interval_ns)
```

相关声明：[stepper_ctrl_set_microstep_interval_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl__backend.html#gac78bf81389bd3013fea18caca0e77e54)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

设置步间时间间隔（Time Interval between Steps），单位为纳秒。

<a id="r_ga719f13485d6c74a365e69661b3f02abe"></a>

```c
typedef int(* stepper_ctrl_configure_ramp_t) (const struct device *dev, const struct stepper_ctrl_ramp *ramp)
```

相关声明：[stepper_ctrl_configure_ramp_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl__backend.html#ga719f13485d6c74a365e69661b3f02abe)、[device](../device_reference/P002_设备对象结构.md)、[stepper_ctrl_ramp](../hardware/P231_步进速度斜坡结构.md)。

配置步进电机运动控制器的斜坡参数（Ramp Parameters）。

<a id="r_gab3a7b8c29e066fc8e4a0333fb7098992"></a>

```c
typedef int(* stepper_ctrl_move_by_t) (const struct device *dev, const int32_t micro_steps)
```

相关声明：[stepper_ctrl_move_by_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl__backend.html#gab3a7b8c29e066fc8e4a0333fb7098992)、[device](../device_reference/P002_设备对象结构.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

使步进电机按给定的微步数（Micro-steps）进行相对移动。

<a id="r_ga8bba3a3304eece57b9047e5f5d2e2fc4"></a>

```c
typedef int(* stepper_ctrl_move_to_t) (const struct device *dev, const int32_t micro_steps)
```

相关声明：[stepper_ctrl_move_to_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl__backend.html#ga8bba3a3304eece57b9047e5f5d2e2fc4)、[device](../device_reference/P002_设备对象结构.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

使步进电机移动到以微步（Micro-steps）表示的绝对位置。

<a id="r_ga2dbdb4e8b581e3766866f7e9435c3429"></a>

```c
typedef int(* stepper_ctrl_run_t) (const struct device *dev, const enum stepper_ctrl_direction direction)
```

相关声明：[stepper_ctrl_run_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl__backend.html#ga2dbdb4e8b581e3766866f7e9435c3429)、[device](../device_reference/P002_设备对象结构.md)、[stepper_ctrl_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#ga188b64bc308fb78a77cfdcf4bfe1b5f7)。

按给定步间隔（Step Interval）和方向运行步进电机。

<a id="r_gaef2903403ded0b2b60e56bd8412a4938"></a>

```c
typedef int(* stepper_ctrl_stop_t) (const struct device *dev)
```

相关声明：[stepper_ctrl_stop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl__backend.html#gaef2903403ded0b2b60e56bd8412a4938)、[device](../device_reference/P002_设备对象结构.md)。

停止步进电机（Stepper）。

<a id="r_gadc066df6951f3bffed3de0d922588842"></a>

```c
typedef int(* stepper_ctrl_is_moving_t) (const struct device *dev, bool *is_moving)
```

相关声明：[stepper_ctrl_is_moving_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl__backend.html#gadc066df6951f3bffed3de0d922588842)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

检查步进电机是否到达目标位置（Target Position）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 8.3\_枚举（Enumerations）

<a id="r_ga188b64bc308fb78a77cfdcf4bfe1b5f7"></a>

```c
enum stepper_ctrl_direction { STEPPER_CTRL_DIRECTION_NEGATIVE = 0 , STEPPER_CTRL_DIRECTION_POSITIVE = 1 }
```

相关声明：[stepper_ctrl_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#ga188b64bc308fb78a77cfdcf4bfe1b5f7)、[STEPPER_CTRL_DIRECTION_NEGATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gga188b64bc308fb78a77cfdcf4bfe1b5f7a3a7272f5a1643140271b009d848d63d8)、[STEPPER_CTRL_DIRECTION_POSITIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gga188b64bc308fb78a77cfdcf4bfe1b5f7a339a2080488f0395a791586b0e6b0330)。

步进电机运动控制器方向选项（Stepper Motion Controller Direction Options）。

<a id="r_ga81a1a98c7381cf5845d9e6a908bdd4a5"></a>

```c
enum stepper_ctrl_run_mode { STEPPER_CTRL_RUN_MODE_HOLD = 0 , STEPPER_CTRL_RUN_MODE_POSITION = 1 , STEPPER_CTRL_RUN_MODE_VELOCITY = 2 }
```

相关声明：[stepper_ctrl_run_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#ga81a1a98c7381cf5845d9e6a908bdd4a5)、[STEPPER_CTRL_RUN_MODE_HOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gga81a1a98c7381cf5845d9e6a908bdd4a5a5dadeff6f35458f9310744e9b6e305b7)、[STEPPER_CTRL_RUN_MODE_POSITION](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gga81a1a98c7381cf5845d9e6a908bdd4a5aa7bd6559d26845de9cba1e1a15a1d841)、[STEPPER_CTRL_RUN_MODE_VELOCITY](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gga81a1a98c7381cf5845d9e6a908bdd4a5ab5ab3be4513a981e070c65dffac633ad)。

步进电机运动控制器运行模式选项（Run Mode Options）。

<a id="r_ga61dfffaeb3d7f76c34c9a9e3ab7627d0"></a>

```c
enum stepper_ctrl_event { STEPPER_CTRL_EVENT_STEPS_COMPLETED = 0 , STEPPER_CTRL_EVENT_LEFT_END_STOP_DETECTED = 1 , STEPPER_CTRL_EVENT_RIGHT_END_STOP_DETECTED = 2 , STEPPER_CTRL_EVENT_STOPPED = 3 }
```

相关声明：[stepper_ctrl_event](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#ga61dfffaeb3d7f76c34c9a9e3ab7627d0)、[STEPPER_CTRL_EVENT_STEPS_COMPLETED](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gga61dfffaeb3d7f76c34c9a9e3ab7627d0abcdf3ebb12e2452b8dd97a78f7799fa3)、[STEPPER_CTRL_EVENT_LEFT_END_STOP_DETECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gga61dfffaeb3d7f76c34c9a9e3ab7627d0a391d21e562f172dfd5e554b7540e24a0)、[STEPPER_CTRL_EVENT_RIGHT_END_STOP_DETECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gga61dfffaeb3d7f76c34c9a9e3ab7627d0a3339b85fb6aafe8d96b47a1fcc2be21c)、[STEPPER_CTRL_EVENT_STOPPED](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gga61dfffaeb3d7f76c34c9a9e3ab7627d0ae8d633746759b9399dc149a1b31429a3)。

步进电机运动控制器事件（Events）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.4\_函数（Functions）

<a id="r_gae723aee1b73b3b65d8ead0546b976cd0"></a>

```c
int stepper_ctrl_set_reference_position (const struct device *dev, const int32_t value)
```

相关声明：[stepper_ctrl_set_reference_position](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gae723aee1b73b3b65d8ead0546b976cd0)、[device](../device_reference/P002_设备对象结构.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置参考位置（Reference Position）。

<a id="r_gaf2c33e8fcf6cd03dfb9361c0246281fb"></a>

```c
int stepper_ctrl_get_actual_position (const struct device *dev, int32_t *value)
```

相关声明：[stepper_ctrl_get_actual_position](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gaf2c33e8fcf6cd03dfb9361c0246281fb)、[device](../device_reference/P002_设备对象结构.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

获取实际步数（Actual Step Count）。

<a id="r_gacd154f195a34a0de50ab26c81ce469d8"></a>

```c
int stepper_ctrl_set_event_cb (const struct device *dev, stepper_ctrl_event_callback_t callback, void *user_data)
```

相关声明：[stepper_ctrl_set_event_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gacd154f195a34a0de50ab26c81ce469d8)、[device](../device_reference/P002_设备对象结构.md)、[stepper_ctrl_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#ga69198946de2a596894b1fc26a13a4c58)。

设置在步进电机运动控制器（Stepper Motion Controller）事件发生时调用的回调函数。

<a id="r_ga1cb888e11712c54bd879a5b0015ea298"></a>

```c
int stepper_ctrl_set_microstep_interval (const struct device *dev, const uint64_t microstep_interval_ns)
```

相关声明：[stepper_ctrl_set_microstep_interval](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#ga1cb888e11712c54bd879a5b0015ea298)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

设置以纳秒为单位的步间时间间隔（Time Interval between Steps），并立即生效。

<a id="r_gae0ebe9949b9fe2bda51c4dc9d537cac5"></a>

```c
int stepper_ctrl_configure_ramp (const struct device *dev, const struct stepper_ctrl_ramp *ramp)
```

相关声明：[stepper_ctrl_configure_ramp](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gae0ebe9949b9fe2bda51c4dc9d537cac5)、[device](../device_reference/P002_设备对象结构.md)、[stepper_ctrl_ramp](../hardware/P231_步进速度斜坡结构.md)。

配置步进电机运动控制器的斜坡（Ramp）。

<a id="r_gaa968ec0a373206d239ac96abc20ee9ea"></a>

```c
int stepper_ctrl_move_by (const struct device *dev, const int32_t micro_steps)
```

相关声明：[stepper_ctrl_move_by](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gaa968ec0a373206d239ac96abc20ee9ea)、[device](../device_reference/P002_设备对象结构.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置从当前位置起要移动的微步数（Micro-steps），即：

<a id="r_gac264384ffdd5c4eca154ddf941abf8a5"></a>

```c
int stepper_ctrl_move_to (const struct device *dev, const int32_t micro_steps)
```

相关声明：[stepper_ctrl_move_to](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gac264384ffdd5c4eca154ddf941abf8a5)、[device](../device_reference/P002_设备对象结构.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置步进电机的绝对目标位置（Absolute Target Position）。

<a id="r_ga544a15b5df405c08127fa8529cfbcf0b"></a>

```c
int stepper_ctrl_run (const struct device *dev, const enum stepper_ctrl_direction direction)
```

相关声明：[stepper_ctrl_run](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#ga544a15b5df405c08127fa8529cfbcf0b)、[device](../device_reference/P002_设备对象结构.md)、[stepper_ctrl_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#ga188b64bc308fb78a77cfdcf4bfe1b5f7)。

按给定步间隔（Step Interval）和方向运行步进电机。

<a id="r_ga780784ec0b192e68849627ff97116c78"></a>

```c
int stepper_ctrl_stop (const struct device *dev)
```

相关声明：[stepper_ctrl_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#ga780784ec0b192e68849627ff97116c78)、[device](../device_reference/P002_设备对象结构.md)。

停止步进电机（Stepper）。

<a id="r_gae78e47cb34035887cf4e8c6a7c6de9de"></a>

```c
int stepper_ctrl_is_moving (const struct device *dev, bool *is_moving)
```

相关声明：[stepper_ctrl_is_moving](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gae78e47cb34035887cf4e8c6a7c6de9de)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

检查步进电机当前是否正在移动（Moving）。


## 8.5\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P821_stepper_ctrl.h_源码浏览.md)
- [stepper_ctrl_ramp](../hardware/P231_步进速度斜坡结构.md)
- [stepper_ctrl_driver_api](../hardware/P234_步进运动控制函数表.md)
- [stepper_ctrl_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#ga69198946de2a596894b1fc26a13a4c58)
- [device](../device_reference/P002_设备对象结构.md)
- [stepper_ctrl_event](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#ga61dfffaeb3d7f76c34c9a9e3ab7627d0)
- [stepper_ctrl_set_reference_position_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl__backend.html#ga142d6eecbaead22de75e3e3d69e23550)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [stepper_ctrl_get_actual_position_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl__backend.html#ga0d807a6415c0040fcf493d5c9c3fa5b1)
- [stepper_ctrl_set_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl__backend.html#ga1570a86e75fbcecfc63213cd144b4a5b)
- [stepper_ctrl_set_microstep_interval_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl__backend.html#gac78bf81389bd3013fea18caca0e77e54)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [stepper_ctrl_configure_ramp_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl__backend.html#ga719f13485d6c74a365e69661b3f02abe)
- [stepper_ctrl_move_by_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl__backend.html#gab3a7b8c29e066fc8e4a0333fb7098992)
- [stepper_ctrl_move_to_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl__backend.html#ga8bba3a3304eece57b9047e5f5d2e2fc4)
- [stepper_ctrl_run_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl__backend.html#ga2dbdb4e8b581e3766866f7e9435c3429)
- [stepper_ctrl_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#ga188b64bc308fb78a77cfdcf4bfe1b5f7)
- [stepper_ctrl_stop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl__backend.html#gaef2903403ded0b2b60e56bd8412a4938)
- [stepper_ctrl_is_moving_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl__backend.html#gadc066df6951f3bffed3de0d922588842)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [STEPPER_CTRL_DIRECTION_NEGATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gga188b64bc308fb78a77cfdcf4bfe1b5f7a3a7272f5a1643140271b009d848d63d8)
- [STEPPER_CTRL_DIRECTION_POSITIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gga188b64bc308fb78a77cfdcf4bfe1b5f7a339a2080488f0395a791586b0e6b0330)
- [stepper_ctrl_run_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#ga81a1a98c7381cf5845d9e6a908bdd4a5)
- [STEPPER_CTRL_RUN_MODE_HOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gga81a1a98c7381cf5845d9e6a908bdd4a5a5dadeff6f35458f9310744e9b6e305b7)
- [STEPPER_CTRL_RUN_MODE_POSITION](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gga81a1a98c7381cf5845d9e6a908bdd4a5aa7bd6559d26845de9cba1e1a15a1d841)
- [STEPPER_CTRL_RUN_MODE_VELOCITY](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gga81a1a98c7381cf5845d9e6a908bdd4a5ab5ab3be4513a981e070c65dffac633ad)
- [STEPPER_CTRL_EVENT_STEPS_COMPLETED](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gga61dfffaeb3d7f76c34c9a9e3ab7627d0abcdf3ebb12e2452b8dd97a78f7799fa3)
- [STEPPER_CTRL_EVENT_LEFT_END_STOP_DETECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gga61dfffaeb3d7f76c34c9a9e3ab7627d0a391d21e562f172dfd5e554b7540e24a0)
- [STEPPER_CTRL_EVENT_RIGHT_END_STOP_DETECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gga61dfffaeb3d7f76c34c9a9e3ab7627d0a3339b85fb6aafe8d96b47a1fcc2be21c)
- [STEPPER_CTRL_EVENT_STOPPED](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gga61dfffaeb3d7f76c34c9a9e3ab7627d0ae8d633746759b9399dc149a1b31429a3)
- [stepper_ctrl_set_reference_position](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gae723aee1b73b3b65d8ead0546b976cd0)
- [stepper_ctrl_get_actual_position](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gaf2c33e8fcf6cd03dfb9361c0246281fb)
- [stepper_ctrl_set_event_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gacd154f195a34a0de50ab26c81ce469d8)
- [stepper_ctrl_set_microstep_interval](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#ga1cb888e11712c54bd879a5b0015ea298)
- [stepper_ctrl_configure_ramp](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gae0ebe9949b9fe2bda51c4dc9d537cac5)
- [stepper_ctrl_move_by](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gaa968ec0a373206d239ac96abc20ee9ea)
- [stepper_ctrl_move_to](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gac264384ffdd5c4eca154ddf941abf8a5)
- [stepper_ctrl_run](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#ga544a15b5df405c08127fa8529cfbcf0b)
- [stepper_ctrl_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#ga780784ec0b192e68849627ff97116c78)
- [stepper_ctrl_is_moving](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gae78e47cb34035887cf4e8c6a7c6de9de)

<a id="header-details"></a>

---

[上一章](P007_zephyr__drivers__pwm__max31790.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P009_zephyr__drivers__mm__system_mm.h_文件参考.md)
