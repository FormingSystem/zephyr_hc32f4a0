---
id: learning.zephyr-docs.api-source-reference.page-458
title: lps2xdf.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lps2xdf_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第458章\_lps2xdf.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/lps2xdf_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/lps2xdf_8h.html)。

## 458.1\_原始可见代码（Source Code）

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
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00082"></a>

```c
/*
 * Copyright (c) 2023 STMicroelectronics
 * Copyright (c) 2023 PHYTEC Messtechnik GmbH
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_LPS2XDF_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_LPS2XDF_H_


#define LPS2xDF_DT_ODR_POWER_DOWN               0
#define LPS2xDF_DT_ODR_1HZ                      1
#define LPS2xDF_DT_ODR_4HZ                      2
#define LPS2xDF_DT_ODR_10HZ                     3
#define LPS2xDF_DT_ODR_25HZ                     4
#define LPS2xDF_DT_ODR_50HZ                     5
#define LPS2xDF_DT_ODR_75HZ                     6
#define LPS2xDF_DT_ODR_100HZ                    7
#define LPS2xDF_DT_ODR_200HZ                    8

#define LPS2xDF_DT_LP_FILTER_OFF                0
#define LPS2xDF_DT_LP_FILTER_ODR_4              1
#define LPS2xDF_DT_LP_FILTER_ODR_9              3

#define LPS2xDF_DT_AVG_4_SAMPLES                0
#define LPS2xDF_DT_AVG_8_SAMPLES                1
#define LPS2xDF_DT_AVG_16_SAMPLES               2
#define LPS2xDF_DT_AVG_32_SAMPLES               3
#define LPS2xDF_DT_AVG_64_SAMPLES               4
#define LPS2xDF_DT_AVG_128_SAMPLES              5
#define LPS2xDF_DT_AVG_256_SAMPLES              6
#define LPS2xDF_DT_AVG_512_SAMPLES              7

#define LPS28DFW_DT_FS_MODE_1_1260              0
#define LPS28DFW_DT_FS_MODE_2_4060              1
#define ILPS22QS_DT_FS_MODE_1_1260              0
#define ILPS22QS_DT_FS_MODE_2_4060              1


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_LPS2XDF_H_ */
```

## 458.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 STMicroelectronics。

版权（Copyright）：© 2023 PHYTEC Messtechnik GmbH。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 82 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_LPS2XDF_H_`。

## 458.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/lps2xdf_8h.html)

---

[上一章](P457_lps22hh.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P459_lsm6dso16is.h_源码浏览.md)
