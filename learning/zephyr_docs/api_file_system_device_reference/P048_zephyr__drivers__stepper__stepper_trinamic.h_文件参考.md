---
id: learning.zephyr-docs.api-file-system-device-reference.page-48
title: zephyr__drivers__stepper__stepper_trinamic.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stepper__trinamic_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第48章\_zephyr\_\_drivers\_\_stepper\_\_stepper\_trinamic.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stepper__trinamic_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Trinamic步进电机控制器专用功能（Stepper Controller Specific Functions）的公共API。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/drivers/stepper/stepper.h>
```

查看此文件的源码。

Trinamic步进电机控制器专用功能（Stepper Controller Specific Functions）的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 48.1\_数据结构（Data Structures）

<a id="r_tmc_5Fstallguard_5Fsettings"></a>

```c
struct tmc_stallguard_settings
```

相关声明：[tmc_stallguard_settings](../hardware/P242_Trinamic堵转检测设置.md)。

Trinamic步进电机StallGuard设置。

<a id="r_tmc_5Framp_5Fgenerator_5Fdata"></a>

```c
struct tmc_ramp_generator_data
```

相关声明：[tmc_ramp_generator_data](../hardware/P243_Trinamic斜坡发生器参数.md)。

Trinamic步进电机斜坡发生器（Stepper Ramp Generator）的数据。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 48.2\_宏定义（Macros）

<a id="r_ga05fe4dd5a148d23cd1240d3e3534726c"></a>

```c
#define TMC_RAMP_DT_SPEC_GET_COMMON(node)
```

相关声明：[TMC_RAMP_DT_SPEC_GET_COMMON](https://docs.zephyrproject.org/latest/doxygen/html/group__trinamic__stepper__ctrl.html#ga05fe4dd5a148d23cd1240d3e3534726c)。

从设备树（DT）获取 Trinamic 步进斜坡发生器（Stepper Ramp Generator）数据。

<a id="r_ga485a07aa34b72643ef77203d6e7c0de2"></a>

```c
#define TMC_RAMP_DT_SPEC_GET_TMC50XX(node)
```

相关声明：[TMC_RAMP_DT_SPEC_GET_TMC50XX](https://docs.zephyrproject.org/latest/doxygen/html/group__trinamic__stepper__ctrl.html#ga485a07aa34b72643ef77203d6e7c0de2)。

从设备树获取 TMC50XX 步进斜坡发生器数据。

<a id="r_ga92c5a6a95451f15cc5b5712ac2e50ad7"></a>

```c
#define TMC_RAMP_DT_SPEC_GET_TMC51XX(node)
```

相关声明：[TMC_RAMP_DT_SPEC_GET_TMC51XX](https://docs.zephyrproject.org/latest/doxygen/html/group__trinamic__stepper__ctrl.html#ga92c5a6a95451f15cc5b5712ac2e50ad7)。

从设备树获取 TMC51XX 步进斜坡发生器数据。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 48.3\_函数（Functions）

<a id="r_ga27c449d5c0bbacabae333c1356aedfd9"></a>

```c
int tmc50xx_stepper_ctrl_set_ramp (const struct device *dev, const struct tmc_ramp_generator_data *ramp_data)
```

相关声明：[tmc50xx_stepper_ctrl_set_ramp](https://docs.zephyrproject.org/latest/doxygen/html/group__trinamic__stepper__ctrl.html#ga27c449d5c0bbacabae333c1356aedfd9)、[device](../device_reference/P002_设备对象结构.md)、[tmc_ramp_generator_data](../hardware/P243_Trinamic斜坡发生器参数.md)。

配置 Trinamic 步进斜坡发生器。

<a id="r_ga3c59d8c7e49d3f5959712b23b2df47ac"></a>

```c
int tmc50xx_stepper_ctrl_set_max_velocity (const struct device *dev, uint32_t velocity)
```

相关声明：[tmc50xx_stepper_ctrl_set_max_velocity](https://docs.zephyrproject.org/latest/doxygen/html/group__trinamic__stepper__ctrl.html#ga3c59d8c7e49d3f5959712b23b2df47ac)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置步进电机（stepper motor）的最大速度。

<a id="r_ga7ef8f93f0301b2437b98eceac43407c7"></a>

```c
void tmc50xx_stepper_ctrl_configure_stallguard (const struct device *dev, const struct tmc_stallguard_settings *sg_settings)
```

相关声明：[tmc50xx_stepper_ctrl_configure_stallguard](https://docs.zephyrproject.org/latest/doxygen/html/group__trinamic__stepper__ctrl.html#ga7ef8f93f0301b2437b98eceac43407c7)、[device](../device_reference/P002_设备对象结构.md)、[tmc_stallguard_settings](../hardware/P242_Trinamic堵转检测设置.md)。

配置 TMC50XX 步进电机 StallGuard 设置。

<a id="r_ga08b0b69ad4db741165d128cb2b2c3188"></a>

```c
void tmc51xx_stepper_ctrl_configure_stallguard (const struct device *dev, const struct tmc_stallguard_settings *sg_settings)
```

相关声明：[tmc51xx_stepper_ctrl_configure_stallguard](https://docs.zephyrproject.org/latest/doxygen/html/group__trinamic__stepper__ctrl.html#ga08b0b69ad4db741165d128cb2b2c3188)、[device](../device_reference/P002_设备对象结构.md)、[tmc_stallguard_settings](../hardware/P242_Trinamic堵转检测设置.md)。

配置 TMC51XX 步进电机 StallGuard 设置。

<a id="r_gaa2534eba96364f813617706a08ea73f7"></a>

```c
int tmc51xx_stepper_ctrl_set_max_velocity (const struct device *dev, uint32_t velocity)
```

相关声明：[tmc51xx_stepper_ctrl_set_max_velocity](https://docs.zephyrproject.org/latest/doxygen/html/group__trinamic__stepper__ctrl.html#gaa2534eba96364f813617706a08ea73f7)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置步进电机（stepper motor）的最大速度。


## 48.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/drivers/stepper/stepper.h](../api_source_reference/P820_stepper.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P824_stepper_trinamic.h_源码浏览.md)
- [tmc_stallguard_settings](../hardware/P242_Trinamic堵转检测设置.md)
- [tmc_ramp_generator_data](../hardware/P243_Trinamic斜坡发生器参数.md)
- [TMC_RAMP_DT_SPEC_GET_COMMON](https://docs.zephyrproject.org/latest/doxygen/html/group__trinamic__stepper__ctrl.html#ga05fe4dd5a148d23cd1240d3e3534726c)
- [TMC_RAMP_DT_SPEC_GET_TMC50XX](https://docs.zephyrproject.org/latest/doxygen/html/group__trinamic__stepper__ctrl.html#ga485a07aa34b72643ef77203d6e7c0de2)
- [TMC_RAMP_DT_SPEC_GET_TMC51XX](https://docs.zephyrproject.org/latest/doxygen/html/group__trinamic__stepper__ctrl.html#ga92c5a6a95451f15cc5b5712ac2e50ad7)
- [tmc50xx_stepper_ctrl_set_ramp](https://docs.zephyrproject.org/latest/doxygen/html/group__trinamic__stepper__ctrl.html#ga27c449d5c0bbacabae333c1356aedfd9)
- [device](../device_reference/P002_设备对象结构.md)
- [tmc50xx_stepper_ctrl_set_max_velocity](https://docs.zephyrproject.org/latest/doxygen/html/group__trinamic__stepper__ctrl.html#ga3c59d8c7e49d3f5959712b23b2df47ac)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [tmc50xx_stepper_ctrl_configure_stallguard](https://docs.zephyrproject.org/latest/doxygen/html/group__trinamic__stepper__ctrl.html#ga7ef8f93f0301b2437b98eceac43407c7)
- [tmc51xx_stepper_ctrl_configure_stallguard](https://docs.zephyrproject.org/latest/doxygen/html/group__trinamic__stepper__ctrl.html#ga08b0b69ad4db741165d128cb2b2c3188)
- [tmc51xx_stepper_ctrl_set_max_velocity](https://docs.zephyrproject.org/latest/doxygen/html/group__trinamic__stepper__ctrl.html#gaa2534eba96364f813617706a08ea73f7)

<a id="header-details"></a>

---

[上一章](P047_zephyr__net__socket_select.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P049_zephyr__dt-bindings__sensor__stts22h.h_文件参考.md)
