---
id: learning.zephyr-docs.api-source-device-reference.page-51
title: stm32wl_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32wl__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第51章\_stm32wl\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32wl__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P471_zephyr__dt-bindings__clock__stm32wl_clock.h_文件参考.md)。

## 51.1\_原始可见代码（Source Code）

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
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00053"></a>
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
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00072"></a>
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
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="astm32__common__clocks_8h_html"></a>

```c
/*
 * Copyright (c) 2022 Linaro Limited
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32WL_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32WL_CLOCK_H_

#include <zephyr/dt-bindings/clock/stm32_common_clocks.h>


#define STM32_CLOCK_BUS_AHB1    0x048
#define STM32_CLOCK_BUS_AHB2    0x04c
#define STM32_CLOCK_BUS_AHB3    0x050
#define STM32_CLOCK_BUS_APB0    0x054
#define STM32_CLOCK_BUS_APB1    0x058
#define STM32_CLOCK_BUS_APB1_2  0x05c
#define STM32_CLOCK_BUS_APB2    0x060
#define STM32_CLOCK_BUS_APB3    0x064

#define STM32_PERIPH_BUS_MIN    STM32_CLOCK_BUS_AHB1
#define STM32_PERIPH_BUS_MAX    STM32_CLOCK_BUS_APB3

/* RM0461, §6.4.29 Clock configuration register (RCC_CFGR3) */

/* defined in stm32_common_clocks.h */
/* Low speed clocks defined in stm32_common_clocks.h */
#define STM32_SRC_HSI           (STM32_SRC_LSI + 1)
#define STM32_SRC_MSI           (STM32_SRC_HSI + 1)
/* #define STM32_SRC_HSI48      TBD */
#define STM32_SRC_PCLK          (STM32_SRC_MSI + 1)
#define STM32_SRC_TIMPCLK1      (STM32_SRC_PCLK + 1)
#define STM32_SRC_TIMPCLK2      (STM32_SRC_TIMPCLK1 + 1)
#define STM32_SRC_PLL_P         (STM32_SRC_TIMPCLK2 + 1)
#define STM32_SRC_PLL_Q         (STM32_SRC_PLL_P + 1)
#define STM32_SRC_PLL_R         (STM32_SRC_PLL_Q + 1)

#define CCIPR_REG               0x88

#define BDCR_REG                0x90

#define CFGR1_REG        0x08

#define USART1_SEL(val)         STM32_DT_CLOCK_SELECT((val), 1, 0, CCIPR_REG)
#define USART2_SEL(val)         STM32_DT_CLOCK_SELECT((val), 3, 2, CCIPR_REG)
#define SPI2_SEL(val)           STM32_DT_CLOCK_SELECT((val), 9, 8, CCIPR_REG)
#define LPUART1_SEL(val)        STM32_DT_CLOCK_SELECT((val), 11, 10, CCIPR_REG)
#define I2C1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 13, 12, CCIPR_REG)
#define I2C2_SEL(val)           STM32_DT_CLOCK_SELECT((val), 15, 14, CCIPR_REG)
#define I2C3_SEL(val)           STM32_DT_CLOCK_SELECT((val), 17, 16, CCIPR_REG)
#define LPTIM1_SEL(val)         STM32_DT_CLOCK_SELECT((val), 19, 18, CCIPR_REG)
#define LPTIM2_SEL(val)         STM32_DT_CLOCK_SELECT((val), 21, 20, CCIPR_REG)
#define LPTIM3_SEL(val)         STM32_DT_CLOCK_SELECT((val), 23, 22, CCIPR_REG)
#define ADC_SEL(val)            STM32_DT_CLOCK_SELECT((val), 29, 28, CCIPR_REG)
#define RNG_SEL(val)            STM32_DT_CLOCK_SELECT((val), 31, 30, CCIPR_REG)
#define RTC_SEL(val)            STM32_DT_CLOCK_SELECT((val), 9, 8, BDCR_REG)
#define MCO1_SEL(val)       STM32_DT_CLOCK_SELECT(val, 27, 24, CFGR1_REG)
#define MCO1_PRE(val)       STM32_DT_CLOCK_SELECT(val, 30, 28, CFGR1_REG)

/* MCO prescaler : division factor */
#define MCO_PRE_DIV_1  0
#define MCO_PRE_DIV_2  1
#define MCO_PRE_DIV_4  2
#define MCO_PRE_DIV_8  3
#define MCO_PRE_DIV_16 4

/* MCO clock output */
#define MCO_SEL_NOCLK     0
#define MCO_SEL_SYSCLKPRE 1
#define MCO_SEL_MSI       2
#define MCO_SEL_HSI16     3
#define MCO_SEL_HSE32     4
#define MCO_SEL_PLL1RCLK  5
#define MCO_SEL_LSI       6
#define MCO_SEL_LSE       8
#define MCO_SEL_PLL1PCLK  13
#define MCO_SEL_PLL1QCLK  14


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32WL_CLOCK_H_ */
```

## 51.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Linaro Limited。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 27 行

参考手册 RM0461，第 6.4.29 节：时钟配置寄存器（Clock Configuration Register，`RCC_CFGR3`）。

### 注释 3：原第 30 行

在 `stm32_common_clocks.h` 中定义。

### 注释 4：原第 32 行

低速时钟定义在 `stm32_common_clocks.h` 中。

### 注释 5：原第 35 行

原注释中的待定宏（TBD）：`#define STM32_SRC_HSI48      TBD`。

### 注释 6：原第 74 行

微控制器时钟输出（MCO）预分频器：分频因子。

### 注释 7：原第 81 行

微控制器时钟输出（MCO clock output）。

### 注释 8：原第 95 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32WL_CLOCK_H_`。

## 51.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P471_zephyr__dt-bindings__clock__stm32wl_clock.h_文件参考.md)
- [zephyr/dt-bindings/clock/stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)
- [stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)

---

[上一章](P050_stm32wba_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P052_syslog.h_源码浏览.md)
