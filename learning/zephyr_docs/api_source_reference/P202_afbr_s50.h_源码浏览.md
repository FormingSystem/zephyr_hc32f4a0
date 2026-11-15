---
id: learning.zephyr-docs.api-source-reference.page-202
title: afbr_s50.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2afbr__s50_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第202章\_afbr\_s50.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2afbr__s50_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2afbr__s50_8h.html)。

## 202.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00023"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00070"></a>

```c
/*
 * Copyright (c) 2025 Croxel Inc.
 * Copyright (c) 2025 CogniPilot Foundation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_AFBR_S50_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_AFBR_S50_H_


#define AFBR_S50_DT_DFM_MODE_OFF                0
#define AFBR_S50_DT_DFM_MODE_4X                 1
#define AFBR_S50_DT_DFM_MODE_8X                 2

#define AFBR_S50_DT_MODE_SHORT_RANGE                                    1
#define AFBR_S50_DT_MODE_LONG_RANGE                                     2
#define AFBR_S50_DT_MODE_HIGH_SPEED_SHORT_RANGE                         5
#define AFBR_S50_DT_MODE_HIGH_SPEED_LONG_RANGE                          6
#define AFBR_S50_DT_MODE_HIGH_PRECISION_SHORT_RANGE                     9
#define AFBR_S50_DT_MODE_SHORT_RANGE_LASER_CLASS_2                      129
#define AFBR_S50_DT_MODE_LONG_RANGE_LASER_CLASS_2                       130
#define AFBR_S50_DT_MODE_HIGH_SPEED_SHORT_RANGE_LASER_CLASS_2           133
#define AFBR_S50_DT_MODE_HIGH_SPEED_LONG_RANGE_LASER_CLASS_2            134
#define AFBR_S50_DT_MODE_HIGH_PRECISION_SHORT_RANGE_LASER_CLASS_2       137


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_AFBR_S50_H_ */
```

## 202.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Croxel Inc.。

版权（Copyright）：© 2025 CogniPilot Foundation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 70 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_AFBR_S50_H_`。

## 202.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2afbr__s50_8h.html)

---

[上一章](P201_adxl355.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P203_icm4268x.h_源码浏览.md)
