---
id: learning.zephyr-docs.api-source-supplement-reference.page-214
title: stm32wl3_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32wl3__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第214章\_stm32wl3\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32wl3__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/stm32wl3__clock_8h.html)。

## 214.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00016"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00021"></a>
<a id="l00022"></a>
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
<a id="l00042"></a>
<a id="astm32__common__clocks_8h_html"></a>

```c
/*
 * Copyright (c) 2024 STMicroelectronics
 * Copyright (c) 2026 Anders Frandsen <anfran@anfran.dk>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32WL3_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32WL3_CLOCK_H_

#include "stm32_common_clocks.h"

#define STM32_SRC_CLK_ROOT      STM32_SRC_SYSCLK

#define STM32_SRC_CLKSLOWMUX    (STM32_SRC_LSI + 1)
#define STM32_SRC_CLK_ROOT_DIV  (STM32_SRC_CLKSLOWMUX + 1)
#define STM32_SRC_CLKSYS        (STM32_SRC_CLK_ROOT_DIV + 1)

/* Bus clocks: offset of the RCC clock enable register for each bus */
#define STM32_CLOCK_BUS_AHB0    0x50
#define STM32_CLOCK_BUS_APB0    0x54
#define STM32_CLOCK_BUS_APB1    0x58
#define STM32_CLOCK_BUS_APB2    0x60

#define STM32_PERIPH_BUS_MIN    STM32_CLOCK_BUS_AHB0
#define STM32_PERIPH_BUS_MAX    STM32_CLOCK_BUS_APB2

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32WL3_CLOCK_H_ */
```

## 214.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 STMicroelectronics。

版权（Copyright）：© 2026 Anders Frandsen <anfran@anfran.dk>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 32 行

总线时钟：各总线的 RCC 时钟使能寄存器偏移量。

### 注释 3：原第 42 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32WL3_CLOCK_H_`。

## 214.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/stm32wl3__clock_8h.html)
- [stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)

---

[上一章](P213_stm32wba_reset.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P215_stm32wl3_reset.h_源码浏览.md)
