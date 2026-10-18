---
id: learning.zephyr-docs.api-file-runtime-reference.page-65
title: zephyr__drivers__stepper__stepper_tmcm3216.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stepper__tmcm3216_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第65章\_zephyr\_\_drivers\_\_stepper\_\_stepper\_tmcm3216.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stepper__tmcm3216_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ADI TMCM-3216步进电机控制器（Stepper Motor Controller）的公共API。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/drivers/stepper/stepper.h>
```

查看此文件的源码。

ADI TMCM-3216步进电机控制器（Stepper Motor Controller）的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 65.1\_数据结构（Data Structures）

<a id="r_tmcm3216_5Fstatus"></a>

```c
struct tmcm3216_status
```

相关声明：[tmcm3216_status](../hardware/P241_TMCM3216电机状态.md)。

TMCM-3216的电机状态（Motor Status）结构。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 65.2\_函数（Functions）

<a id="r_gae0777cd5cbac3899d7f1315e9d1c53fb"></a>

```c
int tmcm3216_get_max_velocity (const struct device *dev, uint32_t *velocity)
```

相关声明：[tmcm3216_get_max_velocity](https://docs.zephyrproject.org/latest/doxygen/html/group__tmcm3216__stepper__ctrl.html#gae0777cd5cbac3899d7f1315e9d1c53fb)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取 TMCM-3216 电机的最大速度（Maximum Velocity）。

<a id="r_gac41f95b33de1a90356c127b64e586dba"></a>

```c
int tmcm3216_get_actual_velocity (const struct device *dev, int32_t *velocity)
```

相关声明：[tmcm3216_get_actual_velocity](https://docs.zephyrproject.org/latest/doxygen/html/group__tmcm3216__stepper__ctrl.html#gac41f95b33de1a90356c127b64e586dba)、[device](../device_reference/P002_设备对象结构.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

获取 TMCM-3216 电机的实际速度（Actual Velocity）。

<a id="r_ga1c6fe3f3d758e02e1c4f427bfc1754bf"></a>

```c
int tmcm3216_get_status (const struct device *dev, struct tmcm3216_status *status)
```

相关声明：[tmcm3216_get_status](https://docs.zephyrproject.org/latest/doxygen/html/group__tmcm3216__stepper__ctrl.html#ga1c6fe3f3d758e02e1c4f427bfc1754bf)、[device](../device_reference/P002_设备对象结构.md)、[tmcm3216_status](../hardware/P241_TMCM3216电机状态.md)。

获取 TMCM-3216 电机的状态（Motor Status）。


## 65.3\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/stepper/stepper.h](../api_source_reference/P820_stepper.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P823_stepper_tmcm3216.h_源码浏览.md)
- [tmcm3216_status](../hardware/P241_TMCM3216电机状态.md)
- [tmcm3216_get_max_velocity](https://docs.zephyrproject.org/latest/doxygen/html/group__tmcm3216__stepper__ctrl.html#gae0777cd5cbac3899d7f1315e9d1c53fb)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [tmcm3216_get_actual_velocity](https://docs.zephyrproject.org/latest/doxygen/html/group__tmcm3216__stepper__ctrl.html#gac41f95b33de1a90356c127b64e586dba)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [tmcm3216_get_status](https://docs.zephyrproject.org/latest/doxygen/html/group__tmcm3216__stepper__ctrl.html#ga1c6fe3f3d758e02e1c4f427bfc1754bf)

<a id="header-details"></a>

---

[上一章](P064_zephyr__dt-bindings__sensor__stcc4.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P066_zephyr__dt-bindings__power__stm32_pwr.h_文件参考.md)
