---
id: learning.zephyr-docs.api-source-runtime-reference.page-17
title: esp32-touch-sensor-input.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/esp32-touch-sensor-input_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_esp32-touch-sensor-input.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/esp32-touch-sensor-input_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/esp32-touch-sensor-input_8h.html)。

## 17.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="adt-util_8h_html"></a>

```c
/*
 * Copyright (c) 2023 Espressif Systems (Shanghai) Co., Ltd.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_INPUT_ESP32_TOUCH_SENSOR_INPUT_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_INPUT_ESP32_TOUCH_SENSOR_INPUT_H_

#include <zephyr/dt-bindings/dt-util.h>

/* Touch sensor IIR filter mode */
#define ESP32_TOUCH_FILTER_MODE_IIR_4           0
#define ESP32_TOUCH_FILTER_MODE_IIR_8           1
#define ESP32_TOUCH_FILTER_MODE_IIR_16          2
#define ESP32_TOUCH_FILTER_MODE_IIR_32          3
#define ESP32_TOUCH_FILTER_MODE_IIR_64          4
#define ESP32_TOUCH_FILTER_MODE_IIR_128         5
#define ESP32_TOUCH_FILTER_MODE_IIR_256         6
#define ESP32_TOUCH_FILTER_MODE_JITTER          7

/* Touch sensor level of filter noise threshold coefficient*/
#define ESP32_TOUCH_FILTER_NOISE_THR_4_8TH      0
#define ESP32_TOUCH_FILTER_NOISE_THR_3_8TH      1
#define ESP32_TOUCH_FILTER_NOISE_THR_2_8TH      2
#define ESP32_TOUCH_FILTER_NOISE_THR_8_8TH      3

/* Touch sensor level of filter applied on the original data */
#define ESP32_TOUCH_FILTER_SMOOTH_MODE_OFF      0
#define ESP32_TOUCH_FILTER_SMOOTH_MODE_IIR_2    1
#define ESP32_TOUCH_FILTER_SMOOTH_MODE_IIR_4    2
#define ESP32_TOUCH_FILTER_SMOOTH_MODE_IIR_8    3

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_INPUT_ESP32_TOUCH_SENSOR_INPUT_H_ */
```

## 17.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Espressif Systems (Shanghai) Co., Ltd.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 12 行

触摸传感器的 IIR 滤波器模式。

### 注释 3：原第 22 行

触摸传感器滤波噪声阈值系数的等级。

### 注释 4：原第 28 行

触摸传感器应用于原始数据的滤波等级。

### 注释 5：原第 34 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_INPUT_ESP32_TOUCH_SENSOR_INPUT_H_`。

## 17.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/esp32-touch-sensor-input_8h.html)
- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)
- [dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)

---

[上一章](P016_pcie.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P018_eth_nxp_enet_qos.h_源码浏览.md)
