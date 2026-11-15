---
id: learning.zephyr-docs.api-source-reference.page-823
title: stepper_tmcm3216.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stepper__tmcm3216_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第823章\_stepper\_tmcm3216.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stepper__tmcm3216_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/stepper__tmcm3216_8h.html)。

## 823.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="foldopen00032"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__tmcm3216__stepper__ctrl_html_ga1c6fe3f3d758e02e1c4f427bfc1754bf"></a>
<a id="agroup__tmcm3216__stepper__ctrl_html_gac41f95b33de1a90356c127b64e586dba"></a>
<a id="agroup__tmcm3216__stepper__ctrl_html_gae0777cd5cbac3899d7f1315e9d1c53fb"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astepper_8h_html"></a>
<a id="astructdevice_html"></a>
<a id="astructtmcm3216__status_html"></a>
<a id="astructtmcm3216__status_html_a01545007f7daa58767e79c2219b2f540"></a>
<a id="astructtmcm3216__status_html_a655198502089019b589dfedcff0edfe9"></a>
<a id="astructtmcm3216__status_html_a8f2d53c1e485f54e047140104009f2b4"></a>
<a id="astructtmcm3216__status_html_a9aa81031f63badd5fa0d9f8de815e62d"></a>
<a id="astructtmcm3216__status_html_aaf7c198c0542f25b72fc997863cf0b8a"></a>
<a id="astructtmcm3216__status_html_adee8489201ca68aa3a1cf2ff2f545ed6"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright (c) 2025 Alexis Czezar C Torreno
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_STEPPER_TMCM3216_H_
#define ZEPHYR_INCLUDE_DRIVERS_STEPPER_TMCM3216_H_


#include <zephyr/device.h>
#include <zephyr/drivers/stepper/stepper.h>

#ifdef __cplusplus
extern "C" {
#endif

struct tmcm3216_status {
        bool position_reached;
        bool right_endstop;
        bool left_endstop;
        bool is_moving;
        int32_t actual_position;
        int32_t actual_velocity;
};

int tmcm3216_get_max_velocity(const struct device *dev, uint32_t *velocity);

int tmcm3216_get_actual_velocity(const struct device *dev, int32_t *velocity);

int tmcm3216_get_status(const struct device *dev, struct tmcm3216_status *status);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_STEPPER_TMCM3216_H_ */
```

## 823.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2025 Alexis Czezar C Torreno。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 82 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_STEPPER_TMCM3216_H_`。

## 823.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/stepper__tmcm3216_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/stepper/stepper.h](https://docs.zephyrproject.org/latest/doxygen/html/stepper_8h.html)
- [tmcm3216_status](../hardware/P241_TMCM3216电机状态.md)
- [position_reached](https://docs.zephyrproject.org/latest/doxygen/html/structtmcm3216__status.html#aaf7c198c0542f25b72fc997863cf0b8a)
- [right_endstop](https://docs.zephyrproject.org/latest/doxygen/html/structtmcm3216__status.html#a8f2d53c1e485f54e047140104009f2b4)
- [left_endstop](https://docs.zephyrproject.org/latest/doxygen/html/structtmcm3216__status.html#adee8489201ca68aa3a1cf2ff2f545ed6)
- [is_moving](https://docs.zephyrproject.org/latest/doxygen/html/structtmcm3216__status.html#a01545007f7daa58767e79c2219b2f540)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [actual_position](https://docs.zephyrproject.org/latest/doxygen/html/structtmcm3216__status.html#a9aa81031f63badd5fa0d9f8de815e62d)
- [actual_velocity](https://docs.zephyrproject.org/latest/doxygen/html/structtmcm3216__status.html#a655198502089019b589dfedcff0edfe9)
- [tmcm3216_get_max_velocity](https://docs.zephyrproject.org/latest/doxygen/html/group__tmcm3216__stepper__ctrl.html#gae0777cd5cbac3899d7f1315e9d1c53fb)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [tmcm3216_get_actual_velocity](https://docs.zephyrproject.org/latest/doxygen/html/group__tmcm3216__stepper__ctrl.html#gac41f95b33de1a90356c127b64e586dba)
- [tmcm3216_get_status](https://docs.zephyrproject.org/latest/doxygen/html/group__tmcm3216__stepper__ctrl.html#ga1c6fe3f3d758e02e1c4f427bfc1754bf)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [stepper.h](https://docs.zephyrproject.org/latest/doxygen/html/stepper_8h.html)
- [tmcm3216_status::is_moving](https://docs.zephyrproject.org/latest/doxygen/html/structtmcm3216__status.html#a01545007f7daa58767e79c2219b2f540)
- [tmcm3216_status::actual_velocity](https://docs.zephyrproject.org/latest/doxygen/html/structtmcm3216__status.html#a655198502089019b589dfedcff0edfe9)
- [tmcm3216_status::right_endstop](https://docs.zephyrproject.org/latest/doxygen/html/structtmcm3216__status.html#a8f2d53c1e485f54e047140104009f2b4)
- [tmcm3216_status::actual_position](https://docs.zephyrproject.org/latest/doxygen/html/structtmcm3216__status.html#a9aa81031f63badd5fa0d9f8de815e62d)
- [tmcm3216_status::position_reached](https://docs.zephyrproject.org/latest/doxygen/html/structtmcm3216__status.html#aaf7c198c0542f25b72fc997863cf0b8a)
- [tmcm3216_status::left_endstop](https://docs.zephyrproject.org/latest/doxygen/html/structtmcm3216__status.html#adee8489201ca68aa3a1cf2ff2f545ed6)

---

[上一章](P822_stepper_drv84xx.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P824_stepper_trinamic.h_源码浏览.md)
