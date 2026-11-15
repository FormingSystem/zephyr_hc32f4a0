---
id: learning.zephyr-docs.api-source-reference.page-206
title: lis2dh.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2lis2dh_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第206章\_lis2dh.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2lis2dh_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2lis2dh_8h.html)。

## 206.1\_原始可见代码（Source Code）

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
<a id="l00020"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00048"></a>

```c
/*
 * Copyright (c) 2023 STMicroelectronics
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_LIS2DH_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_LIS2DH_H_


#define LIS2DH_DT_GPIO_INT_EDGE_BOTH            0
#define LIS2DH_DT_GPIO_INT_EDGE_RISING          1
#define LIS2DH_DT_GPIO_INT_EDGE_FALLING         2
#define LIS2DH_DT_GPIO_INT_LEVEL_HIGH           3
#define LIS2DH_DT_GPIO_INT_LEVEL_LOW            4

#define LIS2DH_DT_ANYM_OR_COMBINATION           0
#define LIS2DH_DT_ANYM_6D_MOVEMENT              1
#define LIS2DH_DT_ANYM_AND_COMBINATION          2
#define LIS2DH_DT_ANYM_6D_POSITION              3


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_LIS2DH_H_ */
```

## 206.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 STMicroelectronics。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 48 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_LIS2DH_H_`。

## 206.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2lis2dh_8h.html)

---

[上一章](P205_it8xxx2_vcmp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P207_lsm6dsvxxx.h_源码浏览.md)
