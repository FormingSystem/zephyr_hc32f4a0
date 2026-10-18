---
id: learning.zephyr-docs.api-source-runtime-reference.page-35
title: it8xxx2_pwm.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/it8xxx2__pwm_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_it8xxx2\_pwm.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/it8xxx2__pwm_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/it8xxx2__pwm_8h.html)。

## 35.1\_原始可见代码（Source Code）

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
<a id="adt-util_8h_html"></a>

```c
/*
 * Copyright (c) 2021 ITE Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PWM_IT8XXX2_PWM_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PWM_IT8XXX2_PWM_H_

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

/*
 * Provides a type to hold PWM configuration flags.
 *
 * The upper 8 bits are reserved for SoC specific flags.
 *    Output onpe-drain flag    [ 8 ]
 */
#define PWM_IT8XXX2_OPEN_DRAIN  BIT(8)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PWM_IT8XXX2_PWM_H_ */
```

## 35.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 ITE Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 11 行

PWM 预分频器引用（Prescaler references）。

### 注释 3：原第 16 行

PWM 通道引用（Channel references）。

### 注释 4：原第 26 行

提供一种保存 PWM 配置标志的类型。

高 8 位保留给 SoC 专用标志。输出开漏标志（原文拼作 onpe-drain）位于第 8 位。

### 注释 5：原第 34 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PWM_IT8XXX2_PWM_H_`。

## 35.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/it8xxx2__pwm_8h.html)
- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)
- [dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)

---

[上一章](P034_intc_mchp_xec_ecia.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P036_kobject.h_源码浏览.md)
