---
id: learning.zephyr-docs.api-source-configuration-reference.page-73
title: pwm_mchp_pwm_g1.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pwm__mchp__pwm__g1_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第73章\_pwm\_mchp\_pwm\_g1.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pwm__mchp__pwm__g1_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pwm__mchp__pwm__g1_8h.html)。

## 73.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00023"></a>
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
<a id="l00048"></a>
<a id="l00049"></a>

```c
/*
 * Copyright (c) 2026 Microchip Technology Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef __PWM_MCHP_PWM_G1_H__
#define __PWM_MCHP_PWM_G1_H__


#define PWM_PRESCALER_POS       8

/* the clock for the PWM channel is divided by peripheral clock */
#define PWM_PRESCALER_DIV_1     (1 << PWM_PRESCALER_POS)
#define PWM_PRESCALER_DIV_2     (2 << PWM_PRESCALER_POS)
#define PWM_PRESCALER_DIV_4     (3 << PWM_PRESCALER_POS)
#define PWM_PRESCALER_DIV_8     (4 << PWM_PRESCALER_POS)
#define PWM_PRESCALER_DIV_16    (5 << PWM_PRESCALER_POS)
#define PWM_PRESCALER_DIV_32    (6 << PWM_PRESCALER_POS)
#define PWM_PRESCALER_DIV_64    (7 << PWM_PRESCALER_POS)
#define PWM_PRESCALER_DIV_128   (8 << PWM_PRESCALER_POS)
#define PWM_PRESCALER_DIV_256   (9 << PWM_PRESCALER_POS)
#define PWM_PRESCALER_DIV_1024  (10 << PWM_PRESCALER_POS)

/* the clock for the PWM channel is from CLKA */
#define PWM_PRESCALER_CLKA      (11 << PWM_PRESCALER_POS)

/* the clock for the PWM channel is from CLKA */
#define PWM_PRESCALER_CLKB      (12 << PWM_PRESCALER_POS)

#define PWM_PRESCALER_MASK      (0xF << PWM_PRESCALER_POS)

#endif /* __PWM_MCHP_PWM_G1_H__ */
```

## 73.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Microchip Technology Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 27 行

PWM 通道的时钟由外设时钟分频而来。

### 注释 3：原第 39 行

PWM 通道的时钟来自 CLKA。

### 注释 4：原第 42 行

PWM 通道的时钟来自 CLKA。

### 注释 5：原第 49 行

头文件保护宏（Header guard）标记：`__PWM_MCHP_PWM_G1_H__`。

## 73.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pwm__mchp__pwm__g1_8h.html)

---

[上一章](P072_pulse_io.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P074_ra2a1-elc.h_源码浏览.md)
