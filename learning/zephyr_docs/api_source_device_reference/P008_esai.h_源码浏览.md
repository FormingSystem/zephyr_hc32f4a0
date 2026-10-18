---
id: learning.zephyr-docs.api-source-device-reference.page-8
title: esai.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/esai_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_esai.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/esai_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P078_zephyr__dt-bindings__dai__esai.h_文件参考.md)。

## 8.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
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

```c
/*
 * Copyright 2024 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_DAI_ESAI_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_DAI_ESAI_H_

/* ESAI pin IDs
 * the values of these macros are meant to match
 * the bit position from PCRC/PRRC's PC/PDC associated
 * with each of these pins.
 */
#define ESAI_PIN_SCKR 0
#define ESAI_PIN_FSR 1
#define ESAI_PIN_HCKR 2
#define ESAI_PIN_SCKT 3
#define ESAI_PIN_FST 4
#define ESAI_PIN_HCKT 5
#define ESAI_PIN_SDO5_SDI0 6
#define ESAI_PIN_SDO4_SDI1 7
#define ESAI_PIN_SDO3_SDI2 8
#define ESAI_PIN_SDO2_SDI3 9
#define ESAI_PIN_SDO1 10
#define ESAI_PIN_SDO0 11

/* ESAI pin modes
 * the values of these macros are set according to
 * the following table:
 *
 * PDC = 0, PC = 0 => DISCONNECTED (0)
 * PDC = 0, PC = 1 => GPIO INPUT (1)
 * PDC = 1, PC = 0 => GPIO OUTPUT (2)
 * PDC = 1, PC = 1 => ESAI (3)
 */
#define ESAI_PIN_DISCONNECTED 0
#define ESAI_PIN_GPIO_INPUT 1
#define ESAI_PIN_GPIO_OUTPUT 2
#define ESAI_PIN_ESAI 3

/* ESAI clock IDs */
#define ESAI_CLOCK_HCKT 0
#define ESAI_CLOCK_HCKR 1
#define ESAI_CLOCK_SCKR 2
#define ESAI_CLOCK_SCKT 3
#define ESAI_CLOCK_FSR 4
#define ESAI_CLOCK_FST 5

/* ESAI clock directions */
#define ESAI_CLOCK_INPUT 0
#define ESAI_CLOCK_OUTPUT 1

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_DAI_ESAI_H_ */
```

## 8.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2024 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

增强型串行音频接口引脚标识（ESAI Pin IDs）。这些宏的值应与 PCRC／PRRC 的 PC／PDC 中每个对应引脚的位位置（Bit Position）匹配。

### 注释 3：原第 28 行

增强型串行音频接口引脚模式（ESAI Pin Modes）。宏值按下表设置：

| PDC | PC | 模式（Mode） | 值 |
| --- | --- | --- | --- |
| 0 | 0 | 断开（DISCONNECTED） | 0 |
| 0 | 1 | GPIO 输入（GPIO INPUT） | 1 |
| 1 | 0 | GPIO 输出（GPIO OUTPUT） | 2 |
| 1 | 1 | ESAI | 3 |

### 注释 4：原第 42 行

增强型串行音频接口时钟标识（ESAI Clock IDs）。

### 注释 5：原第 50 行

增强型串行音频接口时钟方向（ESAI Clock Directions）。

### 注释 6：原第 54 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_DAI_ESAI_H_`。

## 8.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P078_zephyr__dt-bindings__dai__esai.h_文件参考.md)

---

[上一章](P007_bluetooth.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P009_fuel_gauge.h_源码浏览.md)
