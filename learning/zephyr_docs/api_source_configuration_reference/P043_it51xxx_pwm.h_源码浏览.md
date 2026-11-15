---
id: learning.zephyr-docs.api-source-configuration-reference.page-43
title: it51xxx_pwm.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/it51xxx__pwm_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_it51xxx\_pwm.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/it51xxx__pwm_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/it51xxx__pwm_8h.html)。

## 43.1\_原始可见代码（Source Code）

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
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="adt-util_8h_html"></a>

```c
/*
 * Copyright (c) 2025 ITE Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PWM_IT51XXX_PWM_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PWM_IT51XXX_PWM_H_

#include <zephyr/dt-bindings/dt-util.h>

/* PWM prescaler references */
#define PWM_PRESCALER_C4        1
#define PWM_PRESCALER_C6        2
#define PWM_PRESCALER_C7        3

/* PWM channel references */
#define PWM_CHANNEL_0           0
#define PWM_CHANNEL_1           1
#define PWM_CHANNEL_2           2
#define PWM_CHANNEL_3           3
#define PWM_CHANNEL_4           4
#define PWM_CHANNEL_5           5
#define PWM_CHANNEL_6           6
#define PWM_CHANNEL_7           7

#define PWM_DIMMING_DC_40H 0
#define PWM_DIMMING_DC_80H 1
#define PWM_DIMMING_DC_C0H 2
#define PWM_DIMMING_DC_FFH 3

#define PWM_DIMMING_DC_STEP_1H 0
#define PWM_DIMMING_DC_STEP_2H 1
#define PWM_DIMMING_DC_STEP_4H 2
#define PWM_DIMMING_DC_STEP_8H 3

#define PWM_IT51XXX_OPEN_DRAIN   BIT(8)
#define PWM_IT51XXX_DIMMING_MODE BIT(9)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PWM_IT51XXX_PWM_H_ */
```

## 43.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 ITE Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 11 行

PWM 预分频器引用（Prescaler references）。

### 注释 3：原第 16 行

PWM 通道引用（Channel references）。

### 注释 4：原第 68 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PWM_IT51XXX_PWM_H_`。

## 43.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/it51xxx__pwm_8h.html)
- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)
- [dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)

---

[上一章](P042_ioapic.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P044_it8xxx2-i2c.h_源码浏览.md)
