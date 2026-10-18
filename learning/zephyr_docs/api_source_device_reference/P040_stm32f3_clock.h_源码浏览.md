---
id: learning.zephyr-docs.api-source-device-reference.page-40
title: stm32f3_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32f3__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_stm32f3\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32f3__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P426_zephyr__dt-bindings__clock__stm32f3_clock.h_文件参考.md)。

## 40.1\_原始可见代码（Source Code）

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
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="astm32__common__clocks_8h_html"></a>

```c
/*
 * Copyright (c) 2022 Linaro Limited
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F3_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F3_CLOCK_H_

#include <zephyr/dt-bindings/clock/stm32_common_clocks.h>


#define STM32_CLOCK_BUS_AHB1    0x014
#define STM32_CLOCK_BUS_APB2    0x018
#define STM32_CLOCK_BUS_APB1    0x01c

#define STM32_PERIPH_BUS_MIN    STM32_CLOCK_BUS_AHB1
#define STM32_PERIPH_BUS_MAX    STM32_CLOCK_BUS_APB1

/* RM0316, §9.4.13 Clock configuration register (RCC_CFGR3) */

/* Defined in stm32_common_clocks.h */

/* Low speed clocks defined in stm32_common_clocks.h */
#define STM32_SRC_HSI           (STM32_SRC_LSI + 1)
/* #define STM32_SRC_HSI48      TDB */
#define STM32_SRC_PCLK          (STM32_SRC_HSI + 1)
#define STM32_SRC_TIMPCLK1      (STM32_SRC_PCLK + 1)
#define STM32_SRC_TIMPCLK2      (STM32_SRC_TIMPCLK1 + 1)
#define STM32_SRC_TIMPLLCLK     (STM32_SRC_TIMPCLK2 + 1)
#define STM32_SRC_PLLCLK        (STM32_SRC_TIMPLLCLK + 1)

#define CFGR_REG                0x04
#define CFGR2_REG               0x2C
#define CFGR3_REG               0x30

#define BDCR_REG                0x20

#define I2S_SEL(val)            STM32_DT_CLOCK_SELECT((val), 23, 23, CFGR_REG)
#define MCO1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 26, 24, CFGR_REG)
#define MCO1_PRE(val)           STM32_DT_CLOCK_SELECT((val), 30, 28, CFGR_REG)
#define ADC12_PRE(val)          STM32_DT_CLOCK_SELECT((val), 8, 4, CFGR2_REG)
#define ADC34_PRE(val)          STM32_DT_CLOCK_SELECT((val), 13, 9, CFGR2_REG)
#define USART1_SEL(val)         STM32_DT_CLOCK_SELECT((val), 1, 0, CFGR3_REG)
#define I2C1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 4, 4, CFGR3_REG)
#define I2C2_SEL(val)           STM32_DT_CLOCK_SELECT((val), 5, 5, CFGR3_REG)
#define I2C3_SEL(val)           STM32_DT_CLOCK_SELECT((val), 6, 6, CFGR3_REG)
#define TIM1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 8, 8, CFGR3_REG)
#define TIM8_SEL(val)           STM32_DT_CLOCK_SELECT((val), 9, 9, CFGR3_REG)
#define TIM15_SEL(val)          STM32_DT_CLOCK_SELECT((val), 10, 10, CFGR3_REG)
#define TIM16_SEL(val)          STM32_DT_CLOCK_SELECT((val), 11, 11, CFGR3_REG)
#define TIM17_SEL(val)          STM32_DT_CLOCK_SELECT((val), 13, 13, CFGR3_REG)
#define TIM20_SEL(val)          STM32_DT_CLOCK_SELECT((val), 15, 15, CFGR3_REG)
#define USART2_SEL(val)         STM32_DT_CLOCK_SELECT((val), 17, 16, CFGR3_REG)
#define USART3_SEL(val)         STM32_DT_CLOCK_SELECT((val), 19, 18, CFGR3_REG)
#define USART4_SEL(val)         STM32_DT_CLOCK_SELECT((val), 21, 20, CFGR3_REG)
#define USART5_SEL(val)         STM32_DT_CLOCK_SELECT((val), 23, 22, CFGR3_REG)
#define TIM2_SEL(val)           STM32_DT_CLOCK_SELECT((val), 24, 24, CFGR3_REG)
#define TIM3_4_SEL(val)         STM32_DT_CLOCK_SELECT((val), 25, 25, CFGR3_REG)
#define RTC_SEL(val)            STM32_DT_CLOCK_SELECT((val), 9, 8, BDCR_REG)

/* ADC prescaler division factor for all F3 except F37x */
#define ADC_PRE_DISABLED        0x0
#define ADC_PRE_DIV_1           0x10
#define ADC_PRE_DIV_2           0x11
#define ADC_PRE_DIV_4           0x12
#define ADC_PRE_DIV_6           0x13
#define ADC_PRE_DIV_8           0x14
#define ADC_PRE_DIV_10          0x15
#define ADC_PRE_DIV_12          0x16
#define ADC_PRE_DIV_16          0x17
#define ADC_PRE_DIV_32          0x18
#define ADC_PRE_DIV_64          0x19
#define ADC_PRE_DIV_128         0x1A
#define ADC_PRE_DIV_256         0x1B


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F3_CLOCK_H_ */
```

## 40.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Linaro Limited。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 22 行

参考手册 RM0316，第 9.4.13 节：时钟配置寄存器（Clock Configuration Register，`RCC_CFGR3`）。

### 注释 3：原第 25 行

在 `stm32_common_clocks.h` 中定义。

### 注释 4：原第 28 行

低速时钟定义在 `stm32_common_clocks.h` 中。

### 注释 5：原第 30 行

原注释中的宏占位项：`#define STM32_SRC_HSI48      TDB`。其中 `TDB` 按原文保留。

### 注释 6：原第 75 行

除 F37x 之外的全部 F3 器件的模数转换器预分频系数（ADC Prescaler Division Factor）。

### 注释 7：原第 92 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F3_CLOCK_H_`。

## 40.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P426_zephyr__dt-bindings__clock__stm32f3_clock.h_文件参考.md)
- [zephyr/dt-bindings/clock/stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)
- [stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)

---

[上一章](P039_stm32f1_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P041_stm32f7_clock.h_源码浏览.md)
