---
id: learning.zephyr-docs.api-source-reference.page-345
title: iis2dlpc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/iis2dlpc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第345章\_iis2dlpc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/iis2dlpc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/iis2dlpc_8h.html)。

## 345.1\_原始可见代码（Source Code）

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
<a id="l00022"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>

```c
/*
 * Copyright (c) 2023 STMicroelectronics
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_IIS2DLPC_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_IIS2DLPC_H_


#define IIS2DLPC_DT_LP_M1                       0
#define IIS2DLPC_DT_LP_M2                       1
#define IIS2DLPC_DT_LP_M3                       2
#define IIS2DLPC_DT_LP_M4                       3
#define IIS2DLPC_DT_HP_MODE                     4

#define IIS2DLPC_DT_FILTER_BW_ODR_DIV_2         0
#define IIS2DLPC_DT_FILTER_BW_ODR_DIV_4         1
#define IIS2DLPC_DT_FILTER_BW_ODR_DIV_10        2
#define IIS2DLPC_DT_FILTER_BW_ODR_DIV_20        3

#define IIS2DLPC_DT_SINGLE_TAP                  0
#define IIS2DLPC_DT_SINGLE_DOUBLE_TAP           1

#define IIS2DLPC_DT_FF_THRESHOLD_156_mg         0
#define IIS2DLPC_DT_FF_THRESHOLD_219_mg         1
#define IIS2DLPC_DT_FF_THRESHOLD_250_mg         2
#define IIS2DLPC_DT_FF_THRESHOLD_312_mg         3
#define IIS2DLPC_DT_FF_THRESHOLD_344_mg         4
#define IIS2DLPC_DT_FF_THRESHOLD_406_mg         5
#define IIS2DLPC_DT_FF_THRESHOLD_469_mg         6
#define IIS2DLPC_DT_FF_THRESHOLD_500_mg         7

#define IIS2DLPC_DT_WAKEUP_1_ODR                0
#define IIS2DLPC_DT_WAKEUP_2_ODR                1
#define IIS2DLPC_DT_WAKEUP_3_ODR                2
#define IIS2DLPC_DT_WAKEUP_4_ODR                3


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_IIS2DLPC_H_ */
```

## 345.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 STMicroelectronics。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 88 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_IIS2DLPC_H_`。

## 345.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/iis2dlpc_8h.html)

---

[上一章](P344_igmp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P346_iis2iclx.h_源码浏览.md)
