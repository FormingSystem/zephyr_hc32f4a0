---
id: learning.zephyr-docs.api-source-device-reference.page-42
title: stm32g4_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32g4__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_stm32g4\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32g4__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P434_zephyr__dt-bindings__clock__stm32g4_clock.h_文件参考.md)。

## 42.1\_原始可见代码（Source Code）

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
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00031"></a>
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
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00055"></a>
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
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="astm32__common__clocks_8h_html"></a>

```c
/*
 * Copyright (c) 2022 Linaro Limited
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32G4_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32G4_CLOCK_H_

#include <zephyr/dt-bindings/clock/stm32_common_clocks.h>


#define STM32_CLOCK_BUS_AHB1    0x048
#define STM32_CLOCK_BUS_AHB2    0x04c
#define STM32_CLOCK_BUS_AHB3    0x050
#define STM32_CLOCK_BUS_APB1    0x058
#define STM32_CLOCK_BUS_APB1_2  0x05c
#define STM32_CLOCK_BUS_APB2    0x060

#define STM32_PERIPH_BUS_MIN    STM32_CLOCK_BUS_AHB1
#define STM32_PERIPH_BUS_MAX    STM32_CLOCK_BUS_APB2

/* RM0440, § Clock configuration register (RCC_CCIPRx) */

/* defined in stm32_common_clocks.h */

/* Low speed clocks defined in stm32_common_clocks.h */
#define STM32_SRC_HSI           (STM32_SRC_LSI + 1)
#define STM32_SRC_HSI48         (STM32_SRC_HSI + 1)
#define STM32_SRC_HSE           (STM32_SRC_HSI48 + 1)
#define STM32_SRC_MSI           (STM32_SRC_HSE + 1)
#define STM32_SRC_PCLK          (STM32_SRC_MSI + 1)
#define STM32_SRC_TIMPCLK1      (STM32_SRC_PCLK + 1)
#define STM32_SRC_TIMPCLK2      (STM32_SRC_TIMPCLK1 + 1)
#define STM32_SRC_PLL_P         (STM32_SRC_TIMPCLK2 + 1)
#define STM32_SRC_PLL_Q         (STM32_SRC_PLL_P + 1)
#define STM32_SRC_PLL_R         (STM32_SRC_PLL_Q + 1)
/* TODO: PLLSAI clocks */

#define CCIPR_REG               0x88
#define CCIPR2_REG              0x9C

#define BDCR_REG                0x90

#define USART1_SEL(val)         STM32_DT_CLOCK_SELECT((val), 1, 0, CCIPR_REG)
#define USART2_SEL(val)         STM32_DT_CLOCK_SELECT((val), 3, 2, CCIPR_REG)
#define USART3_SEL(val)         STM32_DT_CLOCK_SELECT((val), 5, 4, CCIPR_REG)
#define USART4_SEL(val)         STM32_DT_CLOCK_SELECT((val), 7, 6, CCIPR_REG)
#define USART5_SEL(val)         STM32_DT_CLOCK_SELECT((val), 9, 8, CCIPR_REG)
#define LPUART1_SEL(val)        STM32_DT_CLOCK_SELECT((val), 11, 10, CCIPR_REG)
#define I2C1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 13, 12, CCIPR_REG)
#define I2C2_SEL(val)           STM32_DT_CLOCK_SELECT((val), 15, 14, CCIPR_REG)
#define I2C3_SEL(val)           STM32_DT_CLOCK_SELECT((val), 17, 16, CCIPR_REG)
#define LPTIM1_SEL(val)         STM32_DT_CLOCK_SELECT((val), 19, 18, CCIPR_REG)
#define SAI1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 21, 20, CCIPR_REG)
#define I2S23_SEL(val)          STM32_DT_CLOCK_SELECT((val), 23, 22, CCIPR_REG)
#define FDCAN_SEL(val)          STM32_DT_CLOCK_SELECT((val), 25, 24, CCIPR_REG)
#define CLK48_SEL(val)          STM32_DT_CLOCK_SELECT((val), 27, 26, CCIPR_REG)
#define ADC12_SEL(val)          STM32_DT_CLOCK_SELECT((val), 29, 28, CCIPR_REG)
#define ADC34_SEL(val)          STM32_DT_CLOCK_SELECT((val), 31, 30, CCIPR_REG)
#define I2C4_SEL(val)           STM32_DT_CLOCK_SELECT((val), 1, 0, CCIPR2_REG)
#define QSPI_SEL(val)           STM32_DT_CLOCK_SELECT((val), 21, 20, CCIPR2_REG)
#define RTC_SEL(val)            STM32_DT_CLOCK_SELECT((val), 9, 8, BDCR_REG)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32G4_CLOCK_H_ */
```

## 42.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Linaro Limited。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 25 行

参考手册 RM0440 中的时钟配置寄存器（Clock Configuration Register，`RCC_CCIPRx`）章节。

### 注释 3：原第 28 行

在 `stm32_common_clocks.h` 中定义。

### 注释 4：原第 31 行

低速时钟定义在 `stm32_common_clocks.h` 中。

### 注释 5：原第 44 行

待办（TODO）：PLLSAI 时钟（Clocks）。

### 注释 6：原第 79 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32G4_CLOCK_H_`。

## 42.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P434_zephyr__dt-bindings__clock__stm32g4_clock.h_文件参考.md)
- [zephyr/dt-bindings/clock/stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)
- [stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)

---

[上一章](P041_stm32f7_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P043_stm32h7rs_clock.h_源码浏览.md)
