---
id: learning.zephyr-docs.api-source-reference.page-347
title: iis3dwb.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/iis3dwb_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第347章\_iis3dwb.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/iis3dwb_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/iis3dwb_8h.html)。

## 347.1\_原始可见代码（Source Code）

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
<a id="l00034"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="adt-util_8h_html"></a>

```c
/*
 * Copyright (c) 2025 STMicroelectronics
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_IIS3DWB_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_IIS3DWB_H_

#include <zephyr/dt-bindings/dt-util.h>


#define IIS3DWB_DT_ODR_OFF      0
#define IIS3DWB_DT_ODR_26k7Hz   5

#define IIS3DWB_DT_FS_2G  0
#define IIS3DWB_DT_FS_16G 1
#define IIS3DWB_DT_FS_4G  2
#define IIS3DWB_DT_FS_8G  3

#define IIS3DWB_DT_SLOPE_ODR_DIV_4  0x10
#define IIS3DWB_DT_HP_REF_MODE      0x37
#define IIS3DWB_DT_HP_ODR_DIV_10    0x11
#define IIS3DWB_DT_HP_ODR_DIV_20    0x12
#define IIS3DWB_DT_HP_ODR_DIV_45    0x13
#define IIS3DWB_DT_HP_ODR_DIV_100   0x14
#define IIS3DWB_DT_HP_ODR_DIV_200   0x15
#define IIS3DWB_DT_HP_ODR_DIV_400   0x16
#define IIS3DWB_DT_HP_ODR_DIV_800   0x17
#define IIS3DWB_DT_LP_6k3Hz         0x00
#define IIS3DWB_DT_LP_ODR_DIV_4     0x80
#define IIS3DWB_DT_LP_ODR_DIV_10    0x81
#define IIS3DWB_DT_LP_ODR_DIV_20    0x82
#define IIS3DWB_DT_LP_ODR_DIV_45    0x83
#define IIS3DWB_DT_LP_ODR_DIV_100   0x84
#define IIS3DWB_DT_LP_ODR_DIV_200   0x85
#define IIS3DWB_DT_LP_ODR_DIV_400   0x86
#define IIS3DWB_DT_LP_ODR_DIV_800   0x87

#define IIS3DWB_DT_XL_NOT_BATCHED        0x0
#define IIS3DWB_DT_XL_BATCHED_AT_26k7Hz  0xA

#define IIS3DWB_DT_TEMP_NOT_BATCHED      0
#define IIS3DWB_DT_TEMP_BATCHED_AT_104Hz 3

#define IIS3DWB_DT_TS_NOT_BATCHED 0x0
#define IIS3DWB_DT_DEC_TS_1       0x1
#define IIS3DWB_DT_DEC_TS_8       0x2
#define IIS3DWB_DT_DEC_TS_32      0x3


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_IIS3DWB_H_ */
```

## 347.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 STMicroelectronics。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 111 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_IIS3DWB_H_`。

## 347.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/iis3dwb_8h.html)
- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)
- [dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)

---

[上一章](P346_iis2iclx.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P348_img_mgmt_client.h_源码浏览.md)
