---
id: learning.zephyr-docs.api-source-reference.page-830
title: stm32_common_clocks.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第830章\_stm32\_common\_clocks.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)。

## 830.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00010"></a>
<a id="l00012"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00021"></a>
<a id="l00023"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="foldopen00053"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>

```c
/*
 * Copyright (c) 2023 STMicroelectronics
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32_COMMON_CLOCKS_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32_COMMON_CLOCKS_H_

#define STM32_SRC_SYSCLK        0x001
#define STM32_SRC_LSE           0x002
#define STM32_SRC_LSI           0x003

#define NO_SEL                  0xFF

#define STM32_CLOCK_DIV_SHIFT   12

#define STM32_CLOCK_DIV(div)    (((div) - 1) << STM32_CLOCK_DIV_SHIFT)

#define STM32_DT_CLKSEL_REG_MASK        0xFFFFU
#define STM32_DT_CLKSEL_REG_SHIFT       0U
#define STM32_DT_CLKSEL_SHIFT_MASK      0x1FU
#define STM32_DT_CLKSEL_SHIFT_SHIFT     16U
#define STM32_DT_CLKSEL_WIDTH_MASK      0x3U
#define STM32_DT_CLKSEL_WIDTH_SHIFT     21U
#define STM32_DT_CLKSEL_VAL_MASK        0xFFU
#define STM32_DT_CLKSEL_VAL_SHIFT       24U

#define STM32_DT_CLOCK_SELECT(val, msb, lsb, reg)                                               \
        ((((reg) & STM32_DT_CLKSEL_REG_MASK) << STM32_DT_CLKSEL_REG_SHIFT) |                    \
         (((lsb) & STM32_DT_CLKSEL_SHIFT_MASK) << STM32_DT_CLKSEL_SHIFT_SHIFT) |                \
         ((((msb) - (lsb)) & STM32_DT_CLKSEL_WIDTH_MASK) << STM32_DT_CLKSEL_WIDTH_SHIFT) |      \
         (((val) & STM32_DT_CLKSEL_VAL_MASK) << STM32_DT_CLKSEL_VAL_SHIFT))

#define STM32_CLOCK(bus, bit) (STM32_CLOCK_BUS_##bus) (1 << bit)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32_COMMON_CLOCKS_H_ */
```

## 830.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 STMicroelectronics。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 68 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32_COMMON_CLOCKS_H_`。

## 830.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)

---

[上一章](P829_stm32_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P831_stm32_dcmi.h_源码浏览.md)
