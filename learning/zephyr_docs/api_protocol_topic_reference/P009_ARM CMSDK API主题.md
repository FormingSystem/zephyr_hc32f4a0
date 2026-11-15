---
id: learning.zephyr-docs.api-protocol-topic-reference.page-9
title: ARM CMSDK API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__arm.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_ARM CMSDK API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__arm.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 9.1\_文件（Files）

<a id="r_arm_5Fclock_5Fcontrol_2Eh"></a>

```c
file arm_clock_control.h
```

相关声明：[arm_clock_control.h](../api_file_configuration_reference/P008_zephyr__drivers__clock_control__arm_clock_control.h_文件参考.md)。

基于ARM CMSDK的片上系统（SoCs）的时钟子系统定义。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.2\_数据结构（Data Structures）

<a id="r_arm_5Fclock_5Fcontrol_5Ft"></a>

```c
struct arm_clock_control_t
```

相关声明：[arm_clock_control_t](../driver_model_reference/P014_Arm时钟控制.md)。

ARM CMSDK 片上系统（SoC）的时钟控制子系统描述符（Clock Control Subsystem Descriptor）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 9.3\_枚举（Enumerations）

<a id="r_gaf000c4220627db6eee0117062c6c50ef"></a>

```c
enum arm_bus_type_t { CMSDK_AHB = 0 , CMSDK_APB }
```

相关声明：[arm_bus_type_t](#gaf000c4220627db6eee0117062c6c50ef)、[CMSDK_AHB](#ggaf000c4220627db6eee0117062c6c50efa945c5ee4f308f798cc7d14c3471e0393)、[CMSDK_APB](#ggaf000c4220627db6eee0117062c6c50efa58c832e59253102458c445fc49e02d80)。

CMSDK 外设总线类型（Peripheral Bus Type）。

<a id="r_ga0a2c04415a74486aa29a4d1d0d7679e1"></a>

```c
enum arm_soc_state_t { SOC_ACTIVE = 0 , SOC_SLEEP , SOC_DEEPSLEEP }
```

相关声明：[arm_soc_state_t](#ga0a2c04415a74486aa29a4d1d0d7679e1)、[SOC_ACTIVE](#gga0a2c04415a74486aa29a4d1d0d7679e1a440a3f8e72f1edcabd1c0acfb6fbebbf)、[SOC_SLEEP](#gga0a2c04415a74486aa29a4d1d0d7679e1a3ac4c2f680ed21227a058286db3ea094)、[SOC_DEEPSLEEP](#gga0a2c04415a74486aa29a4d1d0d7679e1afdb90f70cdbc1b44b88a934bafae2c98)。

可以为其配置时钟（Clock）的 CPU 电源状态（Power State）。

## 9.4\_详细说明（Detailed Documentation）

<a id="gaf000c4220627db6eee0117062c6c50ef"></a>

### `arm_bus_type_t`

```c
enum arm_bus_type_t
```

```c
#include <zephyr/drivers/clock_control/arm_clock_control.h>
```

CMSDK 外设总线类型（Peripheral Bus Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CMSDK_AHB` | 高级高性能总线（AHB）外设总线。 |
| `CMSDK_APB` | 高级外设总线（APB）。 |

<a id="ga0a2c04415a74486aa29a4d1d0d7679e1"></a>

### `arm_soc_state_t`

```c
enum arm_soc_state_t
```

```c
#include <zephyr/drivers/clock_control/arm_clock_control.h>
```

可以为其配置时钟（Clock）的 CPU 电源状态（Power State）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SOC_ACTIVE` | 活动（运行）状态（Active/run state）。 |
| `SOC_SLEEP` | 睡眠状态（Sleep state）。 |
| `SOC_DEEPSLEEP` | 深度睡眠状态（Deep sleep state）。 |


## 9.5\_原页交叉引用（Cross References）

- [arm_clock_control.h](../api_file_configuration_reference/P008_zephyr__drivers__clock_control__arm_clock_control.h_文件参考.md)
- [arm_clock_control_t](../driver_model_reference/P014_Arm时钟控制.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggaf000c4220627db6eee0117062c6c50efa945c5ee4f308f798cc7d14c3471e0393"></a>
<a id="ggaf000c4220627db6eee0117062c6c50efa58c832e59253102458c445fc49e02d80"></a>
<a id="gga0a2c04415a74486aa29a4d1d0d7679e1a440a3f8e72f1edcabd1c0acfb6fbebbf"></a>
<a id="gga0a2c04415a74486aa29a4d1d0d7679e1a3ac4c2f680ed21227a058286db3ea094"></a>
<a id="gga0a2c04415a74486aa29a4d1d0d7679e1afdb90f70cdbc1b44b88a934bafae2c98"></a>

---

[上一章](P008_统计（Statistic）.md) · [返回大纲](大纲.md) · [下一章](P010_Atmel SAM 电源管理控制器（PMC）.md)
