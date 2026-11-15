---
id: learning.zephyr-docs.api-source-reference.page-760
title: sensing_sensor_types.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sensing__sensor__types_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第760章\_sensing\_sensor\_types.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sensing__sensor__types_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sensing__sensor__types_8h.html)。

## 760.1\_原始可见代码（Source Code）

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
<a id="l00028"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00080"></a>
<a id="l00081"></a>

```c
/*
 * Copyright (c) 2022-2023 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_SENSING_SENSING_SENSOR_TYPES_H_
#define ZEPHYR_INCLUDE_SENSING_SENSING_SENSOR_TYPES_H_



#define SENSING_SENSOR_TYPE_LIGHT_AMBIENTLIGHT                  0x41



#define SENSING_SENSOR_TYPE_MOTION_ACCELEROMETER_3D             0x73
#define SENSING_SENSOR_TYPE_MOTION_GYROMETER_3D                 0x76
#define SENSING_SENSOR_TYPE_MOTION_MOTION_DETECTOR              0x77
#define SENSING_SENSOR_TYPE_MOTION_UNCALIB_ACCELEROMETER_3D     0x240
#define SENSING_SENSOR_TYPE_MOTION_HINGE_ANGLE                  0x20B



#define SENSING_SENSOR_TYPE_OTHER_CUSTOM 0xE1


#define SENSING_SENSOR_TYPE_ALL                                 0xFFFF


#endif /* ZEPHYR_INCLUDE_SENSING_SENSING_SENSOR_TYPES_H_ */
```

## 760.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022-2023 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 81 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_SENSING_SENSING_SENSOR_TYPES_H_`。

## 760.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sensing__sensor__types_8h.html)

---

[上一章](P759_sensing_sensor.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P761_bd8lb600fs.h_源码浏览.md)
