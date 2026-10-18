---
id: learning.zephyr-docs.api-source-reference.page-205
title: it8xxx2_vcmp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2it8xxx2__vcmp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第205章\_it8xxx2\_vcmp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2it8xxx2__vcmp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2it8xxx2__vcmp_8h.html)。

## 205.1\_原始可见代码（Source Code）

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
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00044"></a>
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
<a id="l00057"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00071"></a>

```c
/*
 * Copyright (c) 2022 ITE Technology Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_IT8XXX2_VCMP_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_IT8XXX2_VCMP_H_


#define VCMP_CHANNEL_0                          0
#define VCMP_CHANNEL_1                          1
#define VCMP_CHANNEL_2                          2
#define VCMP_CHANNEL_3                          3
#define VCMP_CHANNEL_4                          4
#define VCMP_CHANNEL_5                          5
#define VCMP_CHANNEL_CNT                        6

#define IT8XXX2_VCMP_SCAN_PERIOD_100US          0x10
#define IT8XXX2_VCMP_SCAN_PERIOD_200US          0x20
#define IT8XXX2_VCMP_SCAN_PERIOD_400US          0x30
#define IT8XXX2_VCMP_SCAN_PERIOD_600US          0x40
#define IT8XXX2_VCMP_SCAN_PERIOD_800US          0x50
#define IT8XXX2_VCMP_SCAN_PERIOD_1MS            0x60
#define IT8XXX2_VCMP_SCAN_PERIOD_1_5MS          0x70
#define IT8XXX2_VCMP_SCAN_PERIOD_2MS            0x80
#define IT8XXX2_VCMP_SCAN_PERIOD_2_5MS          0x90
#define IT8XXX2_VCMP_SCAN_PERIOD_3MS            0xa0
#define IT8XXX2_VCMP_SCAN_PERIOD_4MS            0xb0
#define IT8XXX2_VCMP_SCAN_PERIOD_5MS            0xc0

#define IT8XXX2_VCMP_LESS_OR_EQUAL              0
#define IT8XXX2_VCMP_GREATER                    1
#define IT8XXX2_VCMP_UNDEFINED                  0xffff


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_IT8XXX2_VCMP_H_ */
```

## 205.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 ITE Technology Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 71 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_IT8XXX2_VCMP_H_`。

## 205.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2it8xxx2__vcmp_8h.html)

---

[上一章](P204_icm566xx.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P206_lis2dh.h_源码浏览.md)
