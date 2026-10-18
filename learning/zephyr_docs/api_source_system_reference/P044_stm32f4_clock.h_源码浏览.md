---
id: learning.zephyr-docs.api-source-system-reference.page-44
title: stm32f4_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32f4__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第44章\_stm32f4\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32f4__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P429_zephyr__dt-bindings__clock__stm32f4_clock.h_文件参考.md)。

## 44.1\_原始可见代码（Source Code）

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
<a id="l00014"></a>
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
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
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
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="astm32__common__clocks_8h_html"></a>

```c
/*
 * Copyright (c) 2022 Linaro Limited
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F4_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F4_CLOCK_H_

#include <zephyr/dt-bindings/clock/stm32_common_clocks.h>



#define STM32_CLOCK_BUS_AHB1 0x030
#define STM32_CLOCK_BUS_AHB2 0x034
#define STM32_CLOCK_BUS_AHB3 0x038
#define STM32_CLOCK_BUS_APB1 0x040
#define STM32_CLOCK_BUS_APB2 0x044
#define STM32_CLOCK_BUS_APB3 0x0A8

#define STM32_PERIPH_BUS_MIN STM32_CLOCK_BUS_AHB1
#define STM32_PERIPH_BUS_MAX STM32_CLOCK_BUS_APB3

/* RM0386, 0390, 0402, 0430 § Dedicated Clock configuration register (RCC_DCKCFGRx) */

/* defined in stm32_common_clocks.h */
/* Low speed clocks defined in stm32_common_clocks.h */
#define STM32_SRC_HSI           (STM32_SRC_LSI + 1)
#define STM32_SRC_HSE           (STM32_SRC_HSI + 1)
#define STM32_SRC_PLL_P         (STM32_SRC_HSE + 1)
#define STM32_SRC_PLL_Q         (STM32_SRC_PLL_P + 1)
#define STM32_SRC_PLL_R         (STM32_SRC_PLL_Q + 1)
#define STM32_SRC_PLL_POST_R    (STM32_SRC_PLL_R + 1)
#define STM32_SRC_PLLI2S_P      (STM32_SRC_PLL_POST_R + 1)
#define STM32_SRC_PLLI2S_Q      (STM32_SRC_PLLI2S_P + 1)
#define STM32_SRC_PLLI2S_POST_Q (STM32_SRC_PLLI2S_Q + 1)
#define STM32_SRC_PLLI2S_R      (STM32_SRC_PLLI2S_POST_Q + 1)
#define STM32_SRC_PLLI2S_POST_R (STM32_SRC_PLLI2S_R + 1)
/* PLLSAI clock outputs */
#define STM32_SRC_PLLSAI_P      (STM32_SRC_PLLI2S_POST_R + 1)
#define STM32_SRC_PLLSAI_Q      (STM32_SRC_PLLSAI_P + 1)
#define STM32_SRC_PLLSAI_POST_Q (STM32_SRC_PLLSAI_Q + 1)
#define STM32_SRC_PLLSAI_R      (STM32_SRC_PLLSAI_POST_Q + 1)
#define STM32_SRC_PLLSAI_POST_R (STM32_SRC_PLLSAI_R + 1)
/* CLK48MHz sources */
#define STM32_SRC_CK48          (STM32_SRC_PLLSAI_POST_R + 1)
#define STM32_SRC_TIMPCLK1      (STM32_SRC_CK48 + 1)
#define STM32_SRC_TIMPCLK2      (STM32_SRC_TIMPCLK1 + 1)


/* I2S_CKIN not supported yet */
/* #define STM32_SRC_I2S_CKIN   TBD */

#define CFGR_REG 0x08
#define BDCR_REG 0x70

#define MCO1_SEL(val) STM32_DT_CLOCK_SELECT((val), 22, 21, CFGR_REG)
#define I2S_SEL(val)  STM32_DT_CLOCK_SELECT((val), 23, 23, CFGR_REG)
#define MCO1_PRE(val) STM32_DT_CLOCK_SELECT((val), 26, 24, CFGR_REG)
#define MCO2_PRE(val) STM32_DT_CLOCK_SELECT((val), 29, 27, CFGR_REG)
#define MCO2_SEL(val) STM32_DT_CLOCK_SELECT((val), 31, 30, CFGR_REG)
#define RTC_SEL(val)  STM32_DT_CLOCK_SELECT((val), 9, 8, BDCR_REG)

/* MCO prescaler : division factor */
#define MCO_PRE_DIV_1 0
#define MCO_PRE_DIV_2 4
#define MCO_PRE_DIV_3 5
#define MCO_PRE_DIV_4 6
#define MCO_PRE_DIV_5 7


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F4_CLOCK_H_ */
```

## 44.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Linaro Limited。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 27 行

参考手册 RM0386、RM0390、RM0402、RM0430 中的专用时钟配置寄存器（Dedicated Clock Configuration Register，`RCC_DCKCFGRx`）章节。

### 注释 3：原第 30 行

在 `stm32_common_clocks.h` 中定义。

### 注释 4：原第 32 行

低速时钟定义在 `stm32_common_clocks.h` 中。

### 注释 5：原第 46 行

PLLSAI 时钟输出（Clock Outputs）。

### 注释 6：原第 52 行

48 MHz 时钟源（CLK48MHz Sources）。

### 注释 7：原第 59 行

尚不支持 `I2S_CKIN`。

### 注释 8：原第 60 行

原注释中的待定宏（TBD）：`#define STM32_SRC_I2S_CKIN   TBD`。

### 注释 9：原第 77 行

微控制器时钟输出（MCO）预分频器：分频因子。

### 注释 10：原第 86 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F4_CLOCK_H_`。

## 44.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P429_zephyr__dt-bindings__clock__stm32f4_clock.h_文件参考.md)
- [zephyr/dt-bindings/clock/stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)
- [stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)

---

[上一章](P043_stm32f10x_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P045_stm32mp2_reset.h_源码浏览.md)
