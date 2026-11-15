---
id: learning.zephyr-docs.api-source-reference.page-459
title: lsm6dso16is.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lsm6dso16is_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第459章\_lsm6dso16is.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/lsm6dso16is_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/lsm6dso16is_8h.html)。

## 459.1\_原始可见代码（Source Code）

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
<a id="l00034"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00056"></a>
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
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00082"></a>

```c
/*
 * Copyright (c) 2023 STMicroelectronics
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_LSM6DSO16IS_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_LSM6DSO16IS_H_


#define LSM6DSO16IS_DT_FS_2G                    0
#define LSM6DSO16IS_DT_FS_16G                   1
#define LSM6DSO16IS_DT_FS_4G                    2
#define LSM6DSO16IS_DT_FS_8G                    3

#define LSM6DSO16IS_DT_FS_250DPS                0x0
#define LSM6DSO16IS_DT_FS_500DPS                0x1
#define LSM6DSO16IS_DT_FS_1000DPS               0x2
#define LSM6DSO16IS_DT_FS_2000DPS               0x3
#define LSM6DSO16IS_DT_FS_125DPS                0x10

#define LSM6DSO16IS_DT_ODR_OFF                  0x0
#define LSM6DSO16IS_DT_ODR_12Hz5_HP             0x1
#define LSM6DSO16IS_DT_ODR_26H_HP               0x2
#define LSM6DSO16IS_DT_ODR_52Hz_HP              0x3
#define LSM6DSO16IS_DT_ODR_104Hz_HP             0x4
#define LSM6DSO16IS_DT_ODR_208Hz_HP             0x5
#define LSM6DSO16IS_DT_ODR_416Hz_HP             0x6
#define LSM6DSO16IS_DT_ODR_833Hz_HP             0x7
#define LSM6DSO16IS_DT_ODR_1667Hz_HP            0x8
#define LSM6DSO16IS_DT_ODR_3333Hz_HP            0x9
#define LSM6DSO16IS_DT_ODR_6667Hz_HP            0xa
#define LSM6DSO16IS_DT_ODR_12Hz5_LP             0x11
#define LSM6DSO16IS_DT_ODR_26H_LP               0x12
#define LSM6DSO16IS_DT_ODR_52Hz_LP              0x13
#define LSM6DSO16IS_DT_ODR_104Hz_LP             0x14
#define LSM6DSO16IS_DT_ODR_208Hz_LP             0x15
#define LSM6DSO16IS_DT_ODR_416Hz_LP             0x16
#define LSM6DSO16IS_DT_ODR_833Hz_LP             0x17
#define LSM6DSO16IS_DT_ODR_1667Hz_LP            0x18
#define LSM6DSO16IS_DT_ODR_3333Hz_LP            0x19
#define LSM6DSO16IS_DT_ODR_6667Hz_LP            0x1a
#define LSM6DSO16IS_DT_ODR_1Hz6_LP              0x1b


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_LSM6DSO16IS_H_ */
```

## 459.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 STMicroelectronics。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 82 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_LSM6DSO16IS_H_`。

## 459.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/lsm6dso16is_8h.html)

---

[上一章](P458_lps2xdf.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P460_lsm6dso.h_源码浏览.md)
