---
id: learning.zephyr-docs.api-source-reference.page-462
title: lsm6dsv320x.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lsm6dsv320x_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第462章\_lsm6dsv320x.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/lsm6dsv320x_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/lsm6dsv320x_8h.html)。

## 462.1\_原始可见代码（Source Code）

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
<a id="l00027"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="adt-bindings_2sensor_2lsm6dsvxxx_8h_html"></a>

```c
/*
 * Copyright (c) 2025 STMicroelectronics
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_LSM6DSV320X_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_LSM6DSV320X_H_

#include "lsm6dsvxxx.h"


#define LSM6DSV320X_HG_XL_ODR_OFF               0x0
#define LSM6DSV320X_HG_XL_ODR_AT_480Hz          0x3
#define LSM6DSV320X_HG_XL_ODR_AT_960Hz          0x4
#define LSM6DSV320X_HG_XL_ODR_AT_1920Hz         0x5
#define LSM6DSV320X_HG_XL_ODR_AT_3840Hz         0x6
#define LSM6DSV320X_HG_XL_ODR_AT_7680Hz         0x7

#define LSM6DSV320X_DT_FS_2G                    2
#define LSM6DSV320X_DT_FS_4G                    4
#define LSM6DSV320X_DT_FS_8G                    8
#define LSM6DSV320X_DT_FS_16G                   16
#define LSM6DSV320X_DT_FS_32G                   32
#define LSM6DSV320X_DT_FS_64G                   64
#define LSM6DSV320X_DT_FS_128G                  128
#define LSM6DSV320X_DT_FS_256G                  256
#define LSM6DSV320X_DT_FS_320G                  320

#define LSM6DSV320X_DT_FS_250DPS                0x1
#define LSM6DSV320X_DT_FS_500DPS                0x2
#define LSM6DSV320X_DT_FS_1000DPS               0x3
#define LSM6DSV320X_DT_FS_2000DPS               0x4
#define LSM6DSV320X_DT_FS_4000DPS               0x5


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_LSM6DSV320X_H_ */
```

## 462.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 STMicroelectronics。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 74 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_LSM6DSV320X_H_`。

## 462.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/lsm6dsv320x_8h.html)
- [lsm6dsvxxx.h](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2lsm6dsvxxx_8h.html)

---

[上一章](P461_lsm6dsv16x.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P463_lsm6dsv32x.h_源码浏览.md)
