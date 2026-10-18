---
id: learning.zephyr-docs.api-source-device-reference.page-48
title: stm32u3_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32u3__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第48章\_stm32u3\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32u3__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P459_zephyr__dt-bindings__clock__stm32u3_clock.h_文件参考.md)。

## 48.1\_原始可见代码（Source Code）

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
<a id="l00018"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00058"></a>
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
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00093"></a>
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
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="astm32__common__clocks_8h_html"></a>

```c
/*
 * Copyright (c) 2025 STMicroelectronics
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32U3_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32U3_CLOCK_H_

#include <zephyr/dt-bindings/clock/stm32_common_clocks.h>



/* RM0487, Figure 36 Clock tree for STM32U3 Series */

/* defined in stm32_common_clocks.h */
#define STM32_SRC_HSE           (STM32_SRC_LSI + 1)
#define STM32_SRC_HSI16         (STM32_SRC_HSE + 1)
#define STM32_SRC_HSI48         (STM32_SRC_HSI16 + 1)
#define STM32_SRC_MSIS          (STM32_SRC_HSI48 + 1)
#define STM32_SRC_MSIK          (STM32_SRC_MSIS + 1)
#define STM32_SRC_HCLK          (STM32_SRC_MSIK + 1)
#define STM32_SRC_PCLK1         (STM32_SRC_HCLK + 1)
#define STM32_SRC_PCLK2         (STM32_SRC_PCLK1 + 1)
#define STM32_SRC_PCLK3         (STM32_SRC_PCLK2 + 1)
#define STM32_SRC_TIMPCLK1      (STM32_SRC_PCLK3 + 1)
#define STM32_SRC_TIMPCLK2      (STM32_SRC_TIMPCLK1 + 1)
/* #define STM32_SRC_ICLK       TBD */

#define STM32_CLOCK_BUS_AHB1    0x088
#define STM32_CLOCK_BUS_AHB1_2  0x094
#define STM32_CLOCK_BUS_AHB2    0x08C
#define STM32_CLOCK_BUS_AHB2_2  0x090
#define STM32_CLOCK_BUS_APB1    0x09C
#define STM32_CLOCK_BUS_APB1_2  0x0A0
#define STM32_CLOCK_BUS_APB2    0x0A4
#define STM32_CLOCK_BUS_APB3    0x0A8

#define STM32_PERIPH_BUS_MIN    STM32_CLOCK_BUS_AHB1
#define STM32_PERIPH_BUS_MAX    STM32_CLOCK_BUS_APB3

#define CCIPR1_REG              0x100
#define CCIPR2_REG              0x104
#define CCIPR3_REG              0x108

#define BDCR_REG                0x110

#define CFGR1_REG               0x0C

#define USART1_SEL(val)         STM32_DT_CLOCK_SELECT((val), 0, 0, CCIPR1_REG)
#define USART3_SEL(val)         STM32_DT_CLOCK_SELECT((val), 2, 2, CCIPR1_REG)
#define UART4_SEL(val)          STM32_DT_CLOCK_SELECT((val), 4, 4, CCIPR1_REG)
#define UART5_SEL(val)          STM32_DT_CLOCK_SELECT((val), 6, 6, CCIPR1_REG)
#define I3C1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 8, 8, CCIPR1_REG)
#define I2C1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 10, 10, CCIPR1_REG)
#define I2C2_SEL(val)           STM32_DT_CLOCK_SELECT((val), 12, 12, CCIPR1_REG)
#define I3C2_SEL(val)           STM32_DT_CLOCK_SELECT((val), 14, 14, CCIPR1_REG)
#define SPI2_SEL(val)           STM32_DT_CLOCK_SELECT((val), 16, 16, CCIPR1_REG)
#define LPTIM2_SEL(val)         STM32_DT_CLOCK_SELECT((val), 19, 18, CCIPR1_REG)
#define SPI1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 20, 20, CCIPR1_REG)
#define SYSTICK_SEL(val)        STM32_DT_CLOCK_SELECT((val), 23, 22, CCIPR1_REG)
#define FDCAN1_SEL(val)         STM32_DT_CLOCK_SELECT((val), 24, 24, CCIPR1_REG)
#define ICLK_SEL(val)           STM32_DT_CLOCK_SELECT((val), 27, 26, CCIPR1_REG)
#define USB1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 28, 28, CCIPR1_REG)
#define TIMIC_SEL(val)          STM32_DT_CLOCK_SELECT((val), 31, 29, CCIPR1_REG)
#define ADF1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 1, 0, CCIPR2_REG)
#define SPI3_SEL(val)           STM32_DT_CLOCK_SELECT((val), 3, 3, CCIPR2_REG)
#define SAI1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 6, 5, CCIPR2_REG)
#define RNG_SEL(val)            STM32_DT_CLOCK_SELECT((val), 11, 11, CCIPR2_REG)
#define ADCDAC_PRE(val)         STM32_DT_CLOCK_SELECT((val), 15, 12, CCIPR2_REG)
#define ADCDAC_SEL(val)         STM32_DT_CLOCK_SELECT((val), 17, 16, CCIPR2_REG)
#define DAC1SH_SEL(val)         STM32_DT_CLOCK_SELECT((val), 19, 19, CCIPR2_REG)
#define OCTOSPI_SEL(val)        STM32_DT_CLOCK_SELECT((val), 20, 20, CCIPR2_REG)
#define LPUART1_SEL(val)        STM32_DT_CLOCK_SELECT((val), 1, 0, CCIPR3_REG)
#define I2C3_SEL(val)           STM32_DT_CLOCK_SELECT((val), 6, 6, CCIPR3_REG)
#define LPTIM34_SEL(val)        STM32_DT_CLOCK_SELECT((val), 9, 8, CCIPR3_REG)
#define LPTIM1_SEL(val)         STM32_DT_CLOCK_SELECT((val), 11, 10, CCIPR3_REG)
#define RTC_SEL(val)            STM32_DT_CLOCK_SELECT((val), 9, 8, BDCR_REG)

#define MCO1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 27, 24, CFGR1_REG)
#define MCO1_PRE(val)           STM32_DT_CLOCK_SELECT((val), 30, 28, CFGR1_REG)

/* MCO prescaler : division factor */
#define MCO_PRE_DIV_1   0
#define MCO_PRE_DIV_2   1
#define MCO_PRE_DIV_4   2
#define MCO_PRE_DIV_8   3
#define MCO_PRE_DIV_16  4
#define MCO_PRE_DIV_32  5
#define MCO_PRE_DIV_64  6
#define MCO_PRE_DIV_128 7

/* ADC/DAC prescaler division factor */
#define ADCDAC_PRE_DIV_1        0x0
#define ADCDAC_PRE_DIV_2        0x1
#define ADCDAC_PRE_DIV_4        0x8
#define ADCDAC_PRE_DIV_8        0x9
#define ADCDAC_PRE_DIV_16       0xA
#define ADCDAC_PRE_DIV_32       0xB
#define ADCDAC_PRE_DIV_64       0xC
#define ADCDAC_PRE_DIV_128      0xD
#define ADCDAC_PRE_DIV_256      0xE
#define ADCDAC_PRE_DIV_512      0xF


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32U3_CLOCK_H_ */
```

## 48.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 STMicroelectronics。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 15 行

参考手册 RM0487，图 36：STM32U3 系列时钟树（Clock Tree）。

### 注释 3：原第 18 行

在 `stm32_common_clocks.h` 中定义。

### 注释 4：原第 33 行

待定的宏定义：`#define STM32_SRC_ICLK TBD`。

### 注释 5：原第 98 行

微控制器时钟输出（MCO）预分频器：分频因子。

### 注释 6：原第 108 行

模数／数模转换器预分频系数（ADC / DAC Prescaler Division Factor）。

### 注释 7：原第 122 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32U3_CLOCK_H_`。

## 48.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P459_zephyr__dt-bindings__clock__stm32u3_clock.h_文件参考.md)
- [zephyr/dt-bindings/clock/stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)
- [stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)

---

[上一章](P047_stm32mp13_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P049_stm32wb_clock.h_源码浏览.md)
