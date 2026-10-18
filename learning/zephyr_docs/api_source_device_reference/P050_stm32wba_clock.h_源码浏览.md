---
id: learning.zephyr-docs.api-source-device-reference.page-50
title: stm32wba_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32wba__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第50章\_stm32wba\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32wba__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P467_zephyr__dt-bindings__clock__stm32wba_clock.h_文件参考.md)。

## 50.1\_原始可见代码（Source Code）

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
<a id="l00019"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
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
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00059"></a>
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
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="astm32__common__clocks_8h_html"></a>

```c
/*
 * Copyright (c) 2023 STMicroelectronics
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32WBA_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32WBA_CLOCK_H_

#include <zephyr/dt-bindings/clock/stm32_common_clocks.h>



/* RM0493, Figure 34, clock tree */
/* RM0515, Figure 36, clock tree */

/* defined in stm32_common_clocks.h */
/* Low speed clocks defined in stm32_common_clocks.h */
#define STM32_SRC_HSE           (STM32_SRC_LSI + 1)
#define STM32_SRC_HSI16         (STM32_SRC_HSE + 1)
#define STM32_SRC_HCLK1         (STM32_SRC_HSI16 + 1)
#define STM32_SRC_HCLK5         (STM32_SRC_HCLK1 + 1)
#define STM32_SRC_PCLK1         (STM32_SRC_HCLK5 + 1)
#define STM32_SRC_PCLK2         (STM32_SRC_PCLK1 + 1)
#define STM32_SRC_PCLK7         (STM32_SRC_PCLK2 + 1)
#define STM32_SRC_TIMPCLK1      (STM32_SRC_PCLK7 + 1)
#define STM32_SRC_TIMPCLK2      (STM32_SRC_TIMPCLK1 + 1)
#define STM32_SRC_PLL1_P        (STM32_SRC_TIMPCLK2 + 1)
#define STM32_SRC_PLL1_Q        (STM32_SRC_PLL1_P + 1)
#define STM32_SRC_PLL1_R        (STM32_SRC_PLL1_Q + 1)

#define STM32_SRC_CLOCK_MIN     STM32_SRC_PLL1_P
#define STM32_SRC_CLOCK_MAX     STM32_SRC_SYSCLK

#define STM32_CLOCK_BUS_AHB1    0x088
#define STM32_CLOCK_BUS_AHB2    0x08C
#define STM32_CLOCK_BUS_AHB4    0x094
#define STM32_CLOCK_BUS_AHB5    0x098
#define STM32_CLOCK_BUS_APB1    0x09C
#define STM32_CLOCK_BUS_APB1_2  0x0A0
#define STM32_CLOCK_BUS_APB2    0x0A4
#define STM32_CLOCK_BUS_APB7    0x0A8

#define STM32_PERIPH_BUS_MIN    STM32_CLOCK_BUS_AHB1
#define STM32_PERIPH_BUS_MAX    STM32_CLOCK_BUS_APB7

#define CCIPR1_REG              0xE0
#define CCIPR2_REG              0xE4
#define CCIPR3_REG              0xE8
#define BCDR1_REG               0xF0

#define USART1_SEL(val)         STM32_DT_CLOCK_SELECT((val), 1, 0, CCIPR1_REG)
#define USART2_SEL(val)         STM32_DT_CLOCK_SELECT((val), 3, 2, CCIPR1_REG)
#define USART3_SEL(val)         STM32_DT_CLOCK_SELECT((val), 5, 4, CCIPR1_REG)
#define I2C1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 11, 10, CCIPR1_REG)
#define I2C2_SEL(val)           STM32_DT_CLOCK_SELECT((val), 13, 12, CCIPR1_REG)
#define I2C4_SEL(val)           STM32_DT_CLOCK_SELECT((val), 15, 14, CCIPR1_REG)
#define SPI2_SEL(val)           STM32_DT_CLOCK_SELECT((val), 17, 16, CCIPR1_REG)
#define LPTIM2_SEL(val)         STM32_DT_CLOCK_SELECT((val), 19, 18, CCIPR1_REG)
#define SPI1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 21, 20, CCIPR1_REG)
#define SYSTICK_SEL(val)        STM32_DT_CLOCK_SELECT((val), 23, 22, CCIPR1_REG)
#define TIMIC_SEL(val)          STM32_DT_CLOCK_SELECT((val), 31, 31, CCIPR1_REG)
#define SAI1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 7, 5, CCIPR2_REG)
#define RNG_SEL(val)            STM32_DT_CLOCK_SELECT((val), 13, 12, CCIPR2_REG)
#define OTGHS_SEL(val)          STM32_DT_CLOCK_SELECT((val), 29, 28, CCIPR2_REG)
#define LPUART1_SEL(val)        STM32_DT_CLOCK_SELECT((val), 1, 0, CCIPR3_REG)
#define SPI3_SEL(val)           STM32_DT_CLOCK_SELECT((val), 4, 3, CCIPR3_REG)
#define I2C3_SEL(val)           STM32_DT_CLOCK_SELECT((val), 7, 6, CCIPR3_REG)
#define LPTIM1_SEL(val)         STM32_DT_CLOCK_SELECT((val), 11, 10, CCIPR3_REG)
#define ADC_SEL(val)            STM32_DT_CLOCK_SELECT((val), 14, 12, CCIPR3_REG)
#define RTC_SEL(val)            STM32_DT_CLOCK_SELECT((val), 9, 8, BCDR1_REG)
#define CFGR1_REG               0x1C
#define MCO1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 27, 24, CFGR1_REG)
#define MCO1_PRE(val)           STM32_DT_CLOCK_SELECT((val), 30, 28, CFGR1_REG)

/* MCO prescaler : division factor */
#define MCO_PRE_DIV_1 0
#define MCO_PRE_DIV_2 1
#define MCO_PRE_DIV_4 2
#define MCO_PRE_DIV_8 3
#define MCO_PRE_DIV_16 4

/* MCO clock output */
#define MCO_SEL_SYSCLKPRE 1
#define MCO_SEL_HSI16 3
#define MCO_SEL_HSE32 4
#define MCO_SEL_PLL1RCLK 5
#define MCO_SEL_LSI 6
#define MCO_SEL_LSE 7
#define MCO_SEL_PLL1PCLK 8
#define MCO_SEL_PLL1QCLK 9
#define MCO_SEL_HCLK5 10


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32WBA_CLOCK_H_ */
```

## 50.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 STMicroelectronics。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 15 行

参考手册 RM0493，图 34：时钟树（Clock Tree）。

### 注释 3：原第 16 行

参考手册 RM0515，图 36：时钟树（Clock Tree）。

### 注释 4：原第 19 行

在 `stm32_common_clocks.h` 中定义。

### 注释 5：原第 21 行

低速时钟定义在 `stm32_common_clocks.h` 中。

### 注释 6：原第 91 行

微控制器时钟输出（MCO）预分频器：分频因子。

### 注释 7：原第 98 行

微控制器时钟输出（MCO clock output）。

### 注释 8：原第 111 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32WBA_CLOCK_H_`。

## 50.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P467_zephyr__dt-bindings__clock__stm32wba_clock.h_文件参考.md)
- [zephyr/dt-bindings/clock/stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)
- [stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)

---

[上一章](P049_stm32wb_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P051_stm32wl_clock.h_源码浏览.md)
