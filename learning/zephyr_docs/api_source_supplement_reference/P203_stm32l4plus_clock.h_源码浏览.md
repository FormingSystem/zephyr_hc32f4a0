---
id: learning.zephyr-docs.api-source-supplement-reference.page-203
title: stm32l4plus_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32l4plus__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第203章\_stm32l4plus\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32l4plus__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/stm32l4plus__clock_8h.html)。

## 203.1\_原始可见代码（Source Code）

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
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="astm32l4__clock_8h_html"></a>

```c
/*
 * Copyright (c) 2025 STMicroelectronics
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32L4PLUS_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32L4PLUS_CLOCK_H_

#include <zephyr/dt-bindings/clock/stm32l4_clock.h>


/*
 * On STM32L4+ series, the SAI1 / SAI2 input clock selection fields
 * are located within the CCIPR2 register instead of the CCIPR register
 */
#undef SAI1_SEL(val)
#undef SAI2_SEL(val)

#define SAI1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 7, 5, CCIPR2_REG)
#define SAI2_SEL(val)           STM32_DT_CLOCK_SELECT((val), 10, 8, CCIPR2_REG)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32L4PLUS_CLOCK_H_ */
```

## 203.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 STMicroelectronics。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 13 行

在 STM32L4+ 系列中，SAI1/SAI2 输入时钟选择字段位于 `CCIPR2` 寄存器，而非 `CCIPR` 寄存器。

### 注释 3：原第 26 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32L4PLUS_CLOCK_H_`。

## 203.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/stm32l4plus__clock_8h.html)
- [zephyr/dt-bindings/clock/stm32l4_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32l4__clock_8h.html)
- [stm32l4_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32l4__clock_8h.html)

---

[上一章](P202_stm32l1_reset.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P204_stm32mp13_reset.h_源码浏览.md)
