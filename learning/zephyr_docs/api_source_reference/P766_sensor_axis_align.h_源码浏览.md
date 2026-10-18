---
id: learning.zephyr-docs.api-source-reference.page-766
title: sensor_axis_align.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sensor__axis__align_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第766章\_sensor\_axis\_align.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sensor__axis__align_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sensor__axis__align_8h.html)。

## 766.1\_原始可见代码（Source Code）

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
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>

```c
/*
 * Copyright 2025 CogniPilot Foundation
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_SENSOR_AXIS_ALIGN_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_SENSOR_AXIS_ALIGN_H_


#define SENSOR_AXIS_ALIGN_DT_X          0
#define SENSOR_AXIS_ALIGN_DT_Y          1
#define SENSOR_AXIS_ALIGN_DT_Z          2

#define SENSOR_AXIS_ALIGN_DT_NEG                0
#define SENSOR_AXIS_ALIGN_DT_POS                2


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_SENSOR_AXIS_ALIGN_H_ */
```

## 766.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025 CogniPilot Foundation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 46 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_SENSOR_AXIS_ALIGN_H_`。

## 766.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sensor__axis__align_8h.html)

---

[上一章](P765_sensor_attribute_types.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P767_sensor_clock.h_源码浏览.md)
