---
id: learning.zephyr-docs.api-file-configuration-reference.page-8
title: zephyr__drivers__clock_control__arm_clock_control.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/arm__clock__control_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_zephyr\_\_drivers\_\_clock\_control\_\_arm\_clock\_control.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/arm__clock__control_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

基于ARM CMSDK的片上系统（SoCs）的时钟子系统定义。

<a id="details"></a>

```c
#include <zephyr/drivers/clock_control.h>
```

查看此文件的源码。

基于ARM CMSDK的片上系统（SoCs）的时钟子系统定义。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 8.1\_数据结构（Data Structures）

<a id="r_arm_5Fclock_5Fcontrol_5Ft"></a>

```c
struct arm_clock_control_t
```

相关声明：[arm_clock_control_t](../driver_model_reference/P014_Arm时钟控制.md)。

ARM CMSDK 片上系统（SoC）的时钟控制子系统描述符（Clock Control Subsystem Descriptor）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 8.2\_枚举（Enumerations）

<a id="r_gaf000c4220627db6eee0117062c6c50ef"></a>

```c
enum arm_bus_type_t { CMSDK_AHB = 0 , CMSDK_APB }
```

相关声明：[arm_bus_type_t](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__arm.html#gaf000c4220627db6eee0117062c6c50ef)、[CMSDK_AHB](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__arm.html#ggaf000c4220627db6eee0117062c6c50efa945c5ee4f308f798cc7d14c3471e0393)、[CMSDK_APB](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__arm.html#ggaf000c4220627db6eee0117062c6c50efa58c832e59253102458c445fc49e02d80)。

CMSDK 外设总线类型（Peripheral Bus Type）。

<a id="r_ga0a2c04415a74486aa29a4d1d0d7679e1"></a>

```c
enum arm_soc_state_t { SOC_ACTIVE = 0 , SOC_SLEEP , SOC_DEEPSLEEP }
```

相关声明：[arm_soc_state_t](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__arm.html#ga0a2c04415a74486aa29a4d1d0d7679e1)、[SOC_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__arm.html#gga0a2c04415a74486aa29a4d1d0d7679e1a440a3f8e72f1edcabd1c0acfb6fbebbf)、[SOC_SLEEP](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__arm.html#gga0a2c04415a74486aa29a4d1d0d7679e1a3ac4c2f680ed21227a058286db3ea094)、[SOC_DEEPSLEEP](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__arm.html#gga0a2c04415a74486aa29a4d1d0d7679e1afdb90f70cdbc1b44b88a934bafae2c98)。

可以为其配置时钟（Clock）的 CPU 电源状态（Power State）。


## 8.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control.h](../timer_reference/P096_时钟控制完整头文件.md)
- [查看此文件的源码。](../api_source_reference/P040_arm_clock_control.h_源码浏览.md)
- [arm_clock_control_t](../driver_model_reference/P014_Arm时钟控制.md)
- [arm_bus_type_t](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__arm.html#gaf000c4220627db6eee0117062c6c50ef)
- [CMSDK_AHB](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__arm.html#ggaf000c4220627db6eee0117062c6c50efa945c5ee4f308f798cc7d14c3471e0393)
- [CMSDK_APB](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__arm.html#ggaf000c4220627db6eee0117062c6c50efa58c832e59253102458c445fc49e02d80)
- [arm_soc_state_t](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__arm.html#ga0a2c04415a74486aa29a4d1d0d7679e1)
- [SOC_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__arm.html#gga0a2c04415a74486aa29a4d1d0d7679e1a440a3f8e72f1edcabd1c0acfb6fbebbf)
- [SOC_SLEEP](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__arm.html#gga0a2c04415a74486aa29a4d1d0d7679e1a3ac4c2f680ed21227a058286db3ea094)
- [SOC_DEEPSLEEP](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__arm.html#gga0a2c04415a74486aa29a4d1d0d7679e1afdb90f70cdbc1b44b88a934bafae2c98)

<a id="header-details"></a>

---

[上一章](P007_zephyr__drivers__sensor__apds9960.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P009_zephyr__dt-bindings__gpio__atmel-sam-gpio.h_文件参考.md)
