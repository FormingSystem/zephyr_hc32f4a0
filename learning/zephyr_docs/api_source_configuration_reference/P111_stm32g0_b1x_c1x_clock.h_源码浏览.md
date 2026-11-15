---
id: learning.zephyr-docs.api-source-configuration-reference.page-111
title: stm32g0_b1x_c1x_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32g0__b1x__c1x__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第111章\_stm32g0\_b1x\_c1x\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32g0__b1x__c1x__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/stm32g0__b1x__c1x__clock_8h.html)。

## 111.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
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
<a id="l00025"></a>
<a id="l00026"></a>

```c
/*
 * Copyright (c) 2025 Andreas Schuster <andreas.schuster@schuam.de>
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32G0_B1X_C1X_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32G0_B1X_C1X_CLOCK_H_


/* MCO prescaler : division factor */
#define MCO_PRE_DIV_256  8
#define MCO_PRE_DIV_512  9
#define MCO_PRE_DIV_1024 10

/* MCO clock output */
#define MCO_SEL_HSI48     2
#define MCO_SEL_PLLPCLK   8
#define MCO_SEL_PLLQCLK   9
#define MCO_SEL_RTCCLK    10
#define MCO_SEL_RTCWAKEUP 11


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32G0_B1X_C1X_CLOCK_H_ */
```

## 111.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Andreas Schuster <andreas.schuster@schuam.de>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 12 行

微控制器时钟输出（MCO）预分频器：分频因子。

### 注释 3：原第 17 行

微控制器时钟输出（MCO clock output）。

### 注释 4：原第 26 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32G0_B1X_C1X_CLOCK_H_`。

## 111.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/stm32g0__b1x__c1x__clock_8h.html)

---

[上一章](P110_stm32f37x_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P112_tcpci.h_源码浏览.md)
