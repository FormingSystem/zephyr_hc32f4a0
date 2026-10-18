---
id: learning.zephyr-docs.api-source-reference.page-40
title: arm_clock_control.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/arm__clock__control_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_arm\_clock\_control.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/arm__clock__control_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/arm__clock__control_8h.html)。

## 40.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00023"></a>
<a id="foldopen00025"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="foldopen00031"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="foldopen00038"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="aclock__control_8h_html"></a>
<a id="agroup__clock__control__arm_html_ga0a2c04415a74486aa29a4d1d0d7679e1"></a>
<a id="agroup__clock__control__arm_html_gaf000c4220627db6eee0117062c6c50ef"></a>
<a id="agroup__clock__control__arm_html_gga0a2c04415a74486aa29a4d1d0d7679e1a3ac4c2f680ed21227a058286db3ea094"></a>
<a id="agroup__clock__control__arm_html_gga0a2c04415a74486aa29a4d1d0d7679e1a440a3f8e72f1edcabd1c0acfb6fbebbf"></a>
<a id="agroup__clock__control__arm_html_gga0a2c04415a74486aa29a4d1d0d7679e1afdb90f70cdbc1b44b88a934bafae2c98"></a>
<a id="agroup__clock__control__arm_html_ggaf000c4220627db6eee0117062c6c50efa58c832e59253102458c445fc49e02d80"></a>
<a id="agroup__clock__control__arm_html_ggaf000c4220627db6eee0117062c6c50efa945c5ee4f308f798cc7d14c3471e0393"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructarm__clock__control__t_html"></a>
<a id="astructarm__clock__control__t_html_a46cd4433f02663f09022a71ae7fe6550"></a>
<a id="astructarm__clock__control__t_html_ab2946697523620aa1f52ae69c636721e"></a>
<a id="astructarm__clock__control__t_html_ab596009f00c33d84af817c860bdb9e40"></a>

```c
/*
 * Copyright (c) 2016 Linaro Limited.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_ARM_CLOCK_CONTROL_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_ARM_CLOCK_CONTROL_H_

#include <zephyr/drivers/clock_control.h>


enum arm_bus_type_t {
        CMSDK_AHB = 0,
        CMSDK_APB,
};

enum arm_soc_state_t {
        SOC_ACTIVE = 0,
        SOC_SLEEP,
        SOC_DEEPSLEEP,
};

struct arm_clock_control_t {
        enum arm_bus_type_t bus;
        enum arm_soc_state_t state;
        uint32_t device;
};


#endif /* ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_ARM_CLOCK_CONTROL_H_ */
```

## 40.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2016 Linaro Limited.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 46 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_ARM_CLOCK_CONTROL_H_`。

## 40.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/arm__clock__control_8h.html)
- [zephyr/drivers/clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)
- [arm_bus_type_t](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__arm.html#gaf000c4220627db6eee0117062c6c50ef)
- [CMSDK_AHB](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__arm.html#ggaf000c4220627db6eee0117062c6c50efa945c5ee4f308f798cc7d14c3471e0393)
- [CMSDK_APB](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__arm.html#ggaf000c4220627db6eee0117062c6c50efa58c832e59253102458c445fc49e02d80)
- [arm_soc_state_t](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__arm.html#ga0a2c04415a74486aa29a4d1d0d7679e1)
- [SOC_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__arm.html#gga0a2c04415a74486aa29a4d1d0d7679e1a440a3f8e72f1edcabd1c0acfb6fbebbf)
- [SOC_SLEEP](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__arm.html#gga0a2c04415a74486aa29a4d1d0d7679e1a3ac4c2f680ed21227a058286db3ea094)
- [SOC_DEEPSLEEP](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__arm.html#gga0a2c04415a74486aa29a4d1d0d7679e1afdb90f70cdbc1b44b88a934bafae2c98)
- [arm_clock_control_t](../driver_model_reference/P014_Arm时钟控制.md)
- [bus](../driver_model_reference/P014_Arm时钟控制.md#ab596009f00c33d84af817c860bdb9e40)
- [state](../driver_model_reference/P014_Arm时钟控制.md#a46cd4433f02663f09022a71ae7fe6550)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [device](../driver_model_reference/P014_Arm时钟控制.md#ab2946697523620aa1f52ae69c636721e)
- [clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)
- [arm_clock_control_t::state](../driver_model_reference/P014_Arm时钟控制.md#a46cd4433f02663f09022a71ae7fe6550)
- [arm_clock_control_t::device](../driver_model_reference/P014_Arm时钟控制.md#ab2946697523620aa1f52ae69c636721e)
- [arm_clock_control_t::bus](../driver_model_reference/P014_Arm时钟控制.md#ab596009f00c33d84af817c860bdb9e40)

---

[上一章](P039_arduino-nano-header.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P041_ast10x0_clock.h_源码浏览.md)
