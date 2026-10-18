---
id: learning.zephyr-docs.api-source-configuration-reference.page-110
title: stm32f37x_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32f37x__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第110章\_stm32f37x\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32f37x__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/stm32f37x__clock_8h.html)。

## 110.1\_原始可见代码（Source Code）

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
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="astm32f3__clock_8h_html"></a>

```c
/*
 * Copyright (c) 2025 STMicroelectronics
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F37X_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F37X_CLOCK_H_

#include <zephyr/dt-bindings/clock/stm32f3_clock.h>


/* On STM32F37x, the ADC prescaler is located in CFGR1 and the prescaler values are more limited */
#undef ADC12_PRE
#undef ADC34_PRE
#undef ADC_PRE_DISABLED
#undef ADC_PRE_DIV_1
#undef ADC_PRE_DIV_2
#undef ADC_PRE_DIV_4
#undef ADC_PRE_DIV_6
#undef ADC_PRE_DIV_8
#undef ADC_PRE_DIV_10
#undef ADC_PRE_DIV_12
#undef ADC_PRE_DIV_16
#undef ADC_PRE_DIV_32
#undef ADC_PRE_DIV_64
#undef ADC_PRE_DIV_128
#undef ADC_PRE_DIV_256

#define ADC_PRE(val)            STM32_DT_CLOCK_SELECT((val), 15, 14, CFGR_REG)

/* ADC prescaler division factor for STM32F37x */
#define ADC_PRE_DIV_2           0
#define ADC_PRE_DIV_4           1
#define ADC_PRE_DIV_6           2
#define ADC_PRE_DIV_8           3


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F37X_CLOCK_H_ */
```

## 110.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 STMicroelectronics。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 13 行

在 STM32F37x 上，ADC 预分频器位于 `CFGR1` 中，可用预分频值也更有限。

### 注释 3：原第 34 行

STM32F37x 的 ADC 预分频器分频因子。

### 注释 4：原第 42 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F37X_CLOCK_H_`。

## 110.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/stm32f37x__clock_8h.html)
- [zephyr/dt-bindings/clock/stm32f3_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32f3__clock_8h.html)
- [stm32f3_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32f3__clock_8h.html)

---

[上一章](P109_stm32f1-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P111_stm32g0_b1x_c1x_clock.h_源码浏览.md)
