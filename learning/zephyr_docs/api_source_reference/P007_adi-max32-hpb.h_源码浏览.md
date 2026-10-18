---
id: learning.zephyr-docs.api-source-reference.page-7
title: adi-max32-hpb.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/adi-max32-hpb_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_adi-max32-hpb.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/adi-max32-hpb_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/adi-max32-hpb_8h.html)。

## 7.1\_原始可见代码（Source Code）

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

```c
/*
 * Copyright 2023 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_MEMORY_CONTROLLER_ADI_MAX32_HPB_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_MEMORY_CONTROLLER_ADI_MAX32_HPB_H_

#define ADI_MAX32_HPB_CS_HIGH_1_5  0
#define ADI_MAX32_HPB_CS_HIGH_2_5  1
#define ADI_MAX32_HPB_CS_HIGH_3_5  2
#define ADI_MAX32_HPB_CS_HIGH_4_5  3
#define ADI_MAX32_HPB_CS_HIGH_5_5  4
#define ADI_MAX32_HPB_CS_HIGH_6_5  5
#define ADI_MAX32_HPB_CS_HIGH_7_5  6
#define ADI_MAX32_HPB_CS_HIGH_8_5  7
#define ADI_MAX32_HPB_CS_HIGH_9_5  8
#define ADI_MAX32_HPB_CS_HIGH_10_5 9
#define ADI_MAX32_HPB_CS_HIGH_11_5 10
#define ADI_MAX32_HPB_CS_HIGH_12_5 11
#define ADI_MAX32_HPB_CS_HIGH_13_5 12
#define ADI_MAX32_HPB_CS_HIGH_14_5 13
#define ADI_MAX32_HPB_CS_HIGH_15_5 14
#define ADI_MAX32_HPB_CS_HIGH_16_5 15

#define ADI_MAX32_HPB_CS_SETUP_HOLD_1  0
#define ADI_MAX32_HPB_CS_SETUP_HOLD_2  1
#define ADI_MAX32_HPB_CS_SETUP_HOLD_3  2
#define ADI_MAX32_HPB_CS_SETUP_HOLD_4  3
#define ADI_MAX32_HPB_CS_SETUP_HOLD_5  4
#define ADI_MAX32_HPB_CS_SETUP_HOLD_6  5
#define ADI_MAX32_HPB_CS_SETUP_HOLD_7  6
#define ADI_MAX32_HPB_CS_SETUP_HOLD_8  7
#define ADI_MAX32_HPB_CS_SETUP_HOLD_9  8
#define ADI_MAX32_HPB_CS_SETUP_HOLD_10 9
#define ADI_MAX32_HPB_CS_SETUP_HOLD_11 10
#define ADI_MAX32_HPB_CS_SETUP_HOLD_12 11
#define ADI_MAX32_HPB_CS_SETUP_HOLD_13 12
#define ADI_MAX32_HPB_CS_SETUP_HOLD_14 13
#define ADI_MAX32_HPB_CS_SETUP_HOLD_15 14
#define ADI_MAX32_HPB_CS_SETUP_HOLD_16 15

#define ADI_MAX32_HPB_LAT_5 0x0
#define ADI_MAX32_HPB_LAT_6 0x1
#define ADI_MAX32_HPB_LAT_3 0xE
#define ADI_MAX32_HPB_LAT_4 0xF

#define ADI_MAX32_HPB_DEV_TYPE_HYPER_FLASH  0
#define ADI_MAX32_HPB_DEV_TYPE_XCCELA_PSRAM 1
#define ADI_MAX32_HPB_DEV_TYPE_HYPER_RAM    2

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_MEMORY_CONTROLLER_ADI_MAX32_HPB_H_ */
```

## 7.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2023 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 53 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_MEMORY_CONTROLLER_ADI_MAX32_HPB_H_`。

## 7.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/adi-max32-hpb_8h.html)

---

[上一章](P006_adi-max32-gpio.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P008_adi_max32_clock_control.h_源码浏览.md)
