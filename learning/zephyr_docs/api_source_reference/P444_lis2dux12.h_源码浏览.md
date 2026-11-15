---
id: learning.zephyr-docs.api-source-reference.page-444
title: lis2dux12.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lis2dux12_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第444章\_lis2dux12.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/lis2dux12_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/lis2dux12_8h.html)。

## 444.1\_原始可见代码（Source Code）

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
<a id="l00024"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="adt-util_8h_html"></a>

```c
/*
 * Copyright (c) 2023 STMicroelectronics
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_LIS2DUX12_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_LIS2DUX12_H_

#include <zephyr/dt-bindings/dt-util.h>


#define LIS2DUX12_OPER_MODE_POWER_DOWN        0
#define LIS2DUX12_OPER_MODE_LOW_POWER         1
#define LIS2DUX12_OPER_MODE_HIGH_PERFORMANCE  2
#define LIS2DUX12_OPER_MODE_SINGLE_SHOT       3

#define LIS2DUX12_DT_ODR_OFF      0
#define LIS2DUX12_DT_ODR_1Hz_ULP  1
#define LIS2DUX12_DT_ODR_3Hz_ULP  2
#define LIS2DUX12_DT_ODR_25Hz_ULP 3
#define LIS2DUX12_DT_ODR_6Hz      4
#define LIS2DUX12_DT_ODR_12Hz5    5
#define LIS2DUX12_DT_ODR_25Hz     6
#define LIS2DUX12_DT_ODR_50Hz     7
#define LIS2DUX12_DT_ODR_100Hz    8
#define LIS2DUX12_DT_ODR_200Hz    9
#define LIS2DUX12_DT_ODR_400Hz    10
#define LIS2DUX12_DT_ODR_800Hz    11
#define LIS2DUX12_DT_ODR_END      12

#define LIS2DUX12_DT_FS_2G  0
#define LIS2DUX12_DT_FS_4G  1
#define LIS2DUX12_DT_FS_8G  2
#define LIS2DUX12_DT_FS_16G 3

#define LIS2DUX12_DT_BDR_XL_ODR        0x0
#define LIS2DUX12_DT_BDR_XL_ODR_DIV_2  0x1
#define LIS2DUX12_DT_BDR_XL_ODR_DIV_4  0x2
#define LIS2DUX12_DT_BDR_XL_ODR_DIV_8  0x3
#define LIS2DUX12_DT_BDR_XL_ODR_DIV_16 0x4
#define LIS2DUX12_DT_BDR_XL_ODR_DIV_32 0x5
#define LIS2DUX12_DT_BDR_XL_ODR_DIV_64 0x6
#define LIS2DUX12_DT_BDR_XL_ODR_OFF    0x7

#define LIS2DUX12_DT_DEC_TS_OFF  0x0
#define LIS2DUX12_DT_DEC_TS_1    0x1
#define LIS2DUX12_DT_DEC_TS_8    0x2
#define LIS2DUX12_DT_DEC_TS_32   0x3

#define LIS2DUXXX_FIFO_EMPTY         0x0
#define LIS2DUXXX_XL_TEMP_TAG        0x2
#define LIS2DUXXX_XL_ONLY_2X_TAG     0x3
#define LIS2DUXXX_TIMESTAMP_TAG      0x4
#define LIS2DUXXX_STEP_COUNTER_TAG   0x12
#define LIS2DUXXX_MLC_RESULT_TAG     0x1A
#define LIS2DUXXX_MLC_FILTER_TAG     0x1B
#define LIS2DUXXX_MLC_FEATURE        0x1C
#define LIS2DUXXX_FSM_RESULT_TAG     0x1D

#define LIS2DUXXX_DT_BYPASS_MODE            0x0
#define LIS2DUXXX_DT_FIFO_MODE              0x1
#define LIS2DUXXX_DT_STREAM_TO_FIFO_MODE    0x3
#define LIS2DUXXX_DT_BYPASS_TO_STREAM_MODE  0x4
#define LIS2DUXXX_DT_STREAM_MODE            0x6
#define LIS2DUXXX_DT_BYPASS_TO_FIFO_MODE    0x7
#define LIS2DUXXX_DT_FIFO_OFF               0x8

#define LIS2DUXXX_DT_FIFO_CTRL           0x15U
#define LIS2DUXXX_DT_STATUS              0x25U
#define LIS2DUXXX_DT_FIFO_STATUS1        0x26U
#define LIS2DUXXX_DT_OUTX_L              0x28U
#define LIS2DUXXX_DT_FIFO_DATA_OUT_TAG   0x40U


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_LIS2DUX12_H_ */
```

## 444.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 STMicroelectronics。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 147 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_LIS2DUX12_H_`。

## 444.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/lis2dux12_8h.html)
- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)
- [dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)

---

[上一章](P443_lis2du12.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P445_lis2dw12.h_源码浏览.md)
