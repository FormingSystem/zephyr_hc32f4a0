---
id: learning.zephyr-docs.api-source-reference.page-37
title: arduino-mega-header.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/arduino-mega-header_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_arduino-mega-header.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/arduino-mega-header_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/arduino-mega-header_8h.html)。

## 37.1\_原始可见代码（Source Code）

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
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
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
<a id="l00072"></a>
<a id="l00073"></a>
<a id="aarduino-header-r3_8h_html"></a>

```c
/*
 * Copyright (c) 2026 Analog Devices, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_ARDUINO_MEGA_HEADER_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_ARDUINO_MEGA_HEADER_H_

#include "arduino-header-r3.h"


#define ARDUINO_MEGA_HEADER_A0 ARDUINO_HEADER_R3_A0
#define ARDUINO_MEGA_HEADER_A1 ARDUINO_HEADER_R3_A1
#define ARDUINO_MEGA_HEADER_A2 ARDUINO_HEADER_R3_A2
#define ARDUINO_MEGA_HEADER_A3 ARDUINO_HEADER_R3_A3
#define ARDUINO_MEGA_HEADER_A4 ARDUINO_HEADER_R3_A4
#define ARDUINO_MEGA_HEADER_A5 ARDUINO_HEADER_R3_A5

#define ARDUINO_MEGA_HEADER_D0 ARDUINO_HEADER_R3_D0
#define ARDUINO_MEGA_HEADER_D1 ARDUINO_HEADER_R3_D1
#define ARDUINO_MEGA_HEADER_D2 ARDUINO_HEADER_R3_D2
#define ARDUINO_MEGA_HEADER_D3 ARDUINO_HEADER_R3_D3
#define ARDUINO_MEGA_HEADER_D4 ARDUINO_HEADER_R3_D4
#define ARDUINO_MEGA_HEADER_D5 ARDUINO_HEADER_R3_D5
#define ARDUINO_MEGA_HEADER_D6 ARDUINO_HEADER_R3_D6
#define ARDUINO_MEGA_HEADER_D7 ARDUINO_HEADER_R3_D7

#define ARDUINO_MEGA_HEADER_D8  ARDUINO_HEADER_R3_D8
#define ARDUINO_MEGA_HEADER_D9  ARDUINO_HEADER_R3_D9
#define ARDUINO_MEGA_HEADER_D10 ARDUINO_HEADER_R3_D10
#define ARDUINO_MEGA_HEADER_D11 ARDUINO_HEADER_R3_D11
#define ARDUINO_MEGA_HEADER_D12 ARDUINO_HEADER_R3_D12
#define ARDUINO_MEGA_HEADER_D13 ARDUINO_HEADER_R3_D13
#define ARDUINO_MEGA_HEADER_SDA1 ARDUINO_HEADER_R3_D14
#define ARDUINO_MEGA_HEADER_SCL1 ARDUINO_HEADER_R3_D15

#define ARDUINO_MEGA_HEADER_D14 22
#define ARDUINO_MEGA_HEADER_D15 23
#define ARDUINO_MEGA_HEADER_D16 24
#define ARDUINO_MEGA_HEADER_D17 25
#define ARDUINO_MEGA_HEADER_D18 26
#define ARDUINO_MEGA_HEADER_D19 27
#define ARDUINO_MEGA_HEADER_D20 28
#define ARDUINO_MEGA_HEADER_D21 29

#define ARDUINO_MEGA_HEADER_A6 30
#define ARDUINO_MEGA_HEADER_A7 31

#define ARDUINO_MEGA_HEADER_A8  32
#define ARDUINO_MEGA_HEADER_A9  33
#define ARDUINO_MEGA_HEADER_A10 34
#define ARDUINO_MEGA_HEADER_A11 35
#define ARDUINO_MEGA_HEADER_A12 36
#define ARDUINO_MEGA_HEADER_A13 37
#define ARDUINO_MEGA_HEADER_A14 38
#define ARDUINO_MEGA_HEADER_A15 39


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_ARDUINO_MEGA_HEADER_H_ */
```

## 37.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Analog Devices, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 73 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_ARDUINO_MEGA_HEADER_H_`。

## 37.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/arduino-mega-header_8h.html)
- [arduino-header-r3.h](https://docs.zephyrproject.org/latest/doxygen/html/arduino-header-r3_8h.html)

---

[上一章](P036_arduino-header-r3.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P038_arduino-mkr-header.h_源码浏览.md)
