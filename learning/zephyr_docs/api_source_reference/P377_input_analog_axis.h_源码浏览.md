---
id: learning.zephyr-docs.api-source-reference.page-377
title: input_analog_axis.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/input__analog__axis_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第377章\_input\_analog\_axis.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/input__analog__axis_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/input__analog__axis_8h.html)。

## 377.1\_原始可见代码（Source Code）

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
<a id="l00018"></a>
<a id="l00024"></a>
<a id="foldopen00032"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__input__analog__axis_html_ga384e901afe29ae91e01c44b458034d64"></a>
<a id="agroup__input__analog__axis_html_ga645237cdb40113e4253a24e902091f3e"></a>
<a id="agroup__input__analog__axis_html_ga99dd3b96a43f115a8c90859e7eed24d4"></a>
<a id="agroup__input__analog__axis_html_gaae496bde41a58d92521b0a24f762caeb"></a>
<a id="agroup__input__analog__axis_html_gad359f00fa9c46219a55a218d26d0407a"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_afe270aee8d96ad7f279a4020b9d58bdf"></a>
<a id="astructanalog__axis__calibration_html"></a>
<a id="astructanalog__axis__calibration_html_a2a0b2c3ec62b66c05b187411a8b3e4db"></a>
<a id="astructanalog__axis__calibration_html_a67a595a038b2a244d16e759aecf5856a"></a>
<a id="astructanalog__axis__calibration_html_a8c583137a2605d7ba48da2291de46590"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright 2023 Google LLC
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_INPUT_INPUT_ANALOG_AXIS_H_
#define ZEPHYR_INCLUDE_INPUT_INPUT_ANALOG_AXIS_H_

#include <stdint.h>
#include <zephyr/device.h>


struct analog_axis_calibration {
        int16_t in_min;
        int16_t in_max;
        uint16_t in_deadzone;
};

typedef void (*analog_axis_raw_data_t)(const struct device *dev,
                                       int channel, int16_t raw_val);

void analog_axis_set_raw_data_cb(const struct device *dev, analog_axis_raw_data_t cb);

int analog_axis_num_axes(const struct device *dev);

int analog_axis_calibration_get(const struct device *dev,
                                int channel,
                                struct analog_axis_calibration *cal);

int analog_axis_calibration_set(const struct device *dev,
                                int channel,
                                struct analog_axis_calibration *cal);


#endif /* ZEPHYR_INCLUDE_INPUT_INPUT_ANALOG_AXIS_H_ */
```

## 377.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2023 Google LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 103 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_INPUT_INPUT_ANALOG_AXIS_H_`。

## 377.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/input__analog__axis_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [analog_axis_calibration](../driver_model_reference/P008_模拟轴校准.md)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [in_min](../driver_model_reference/P008_模拟轴校准.md#a2a0b2c3ec62b66c05b187411a8b3e4db)
- [in_max](../driver_model_reference/P008_模拟轴校准.md#a67a595a038b2a244d16e759aecf5856a)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [in_deadzone](../driver_model_reference/P008_模拟轴校准.md#a8c583137a2605d7ba48da2291de46590)
- [analog_axis_raw_data_t](https://docs.zephyrproject.org/latest/doxygen/html/group__input__analog__axis.html#ga384e901afe29ae91e01c44b458034d64)
- [device](../device_reference/P002_设备对象结构.md)
- [analog_axis_set_raw_data_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__input__analog__axis.html#ga645237cdb40113e4253a24e902091f3e)
- [analog_axis_num_axes](https://docs.zephyrproject.org/latest/doxygen/html/group__input__analog__axis.html#ga99dd3b96a43f115a8c90859e7eed24d4)
- [analog_axis_calibration_get](https://docs.zephyrproject.org/latest/doxygen/html/group__input__analog__axis.html#gad359f00fa9c46219a55a218d26d0407a)
- [analog_axis_calibration_set](https://docs.zephyrproject.org/latest/doxygen/html/group__input__analog__axis.html#gaae496bde41a58d92521b0a24f762caeb)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [analog_axis_calibration::in_min](../driver_model_reference/P008_模拟轴校准.md#a2a0b2c3ec62b66c05b187411a8b3e4db)
- [analog_axis_calibration::in_max](../driver_model_reference/P008_模拟轴校准.md#a67a595a038b2a244d16e759aecf5856a)
- [analog_axis_calibration::in_deadzone](../driver_model_reference/P008_模拟轴校准.md#a8c583137a2605d7ba48da2291de46590)

---

[上一章](P376_input.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P378_input_analog_axis_settings.h_源码浏览.md)
