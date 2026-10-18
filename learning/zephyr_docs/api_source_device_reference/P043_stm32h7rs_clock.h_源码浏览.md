---
id: learning.zephyr-docs.api-source-device-reference.page-43
title: stm32h7rs_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32h7rs__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_stm32h7rs\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32h7rs__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P440_zephyr__dt-bindings__clock__stm32h7rs_clock.h_文件参考.md)。

## 43.1\_原始可见代码（Source Code）

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
<a id="l00019"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00027"></a>
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
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="astm32__common__clocks_8h_html"></a>

```c
/*
 * Copyright (c) 2024 STMicroelectronics
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32H7RS_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32H7RS_CLOCK_H_

#include <zephyr/dt-bindings/clock/stm32_common_clocks.h>



/* RM0477  */

/* defined in stm32_common_clocks.h */

/* Low speed clocks defined in stm32_common_clocks.h */
#define STM32_SRC_HSE           (STM32_SRC_LSI + 1)
#define STM32_SRC_HSI48         (STM32_SRC_HSE + 1)
#define STM32_SRC_HSI_KER       (STM32_SRC_HSI48 + 1) /* HSI + HSIKERON */
#define STM32_SRC_CSI_KER       (STM32_SRC_HSI_KER + 1) /* CSI + CSIKERON */
#define STM32_SRC_PLL1_P        (STM32_SRC_CSI_KER + 1)
#define STM32_SRC_PLL1_Q        (STM32_SRC_PLL1_P + 1)
#define STM32_SRC_PLL1_R        (STM32_SRC_PLL1_Q + 1)
#define STM32_SRC_PLL1_S        (STM32_SRC_PLL1_R + 1)
#define STM32_SRC_PLL2_P        (STM32_SRC_PLL1_S + 1)
#define STM32_SRC_PLL2_Q        (STM32_SRC_PLL2_P + 1)
#define STM32_SRC_PLL2_R        (STM32_SRC_PLL2_Q + 1)
#define STM32_SRC_PLL2_S        (STM32_SRC_PLL2_R + 1)
#define STM32_SRC_PLL2_T        (STM32_SRC_PLL2_S + 1)
#define STM32_SRC_PLL3_P        (STM32_SRC_PLL2_T + 1)
#define STM32_SRC_PLL3_Q        (STM32_SRC_PLL3_P + 1)
#define STM32_SRC_PLL3_R        (STM32_SRC_PLL3_Q + 1)
#define STM32_SRC_PLL3_S        (STM32_SRC_PLL3_R + 1)

#define STM32_SRC_CKPER         (STM32_SRC_PLL3_S + 1)
#define STM32_SRC_HCLK1         (STM32_SRC_CKPER + 1)
#define STM32_SRC_HCLK2         (STM32_SRC_HCLK1 + 1)
#define STM32_SRC_HCLK3         (STM32_SRC_HCLK2 + 1)
#define STM32_SRC_HCLK4         (STM32_SRC_HCLK3 + 1)
#define STM32_SRC_HCLK5         (STM32_SRC_HCLK4 + 1)
#define STM32_SRC_TIMPCLK1      (STM32_SRC_HCLK5 + 1)
#define STM32_SRC_TIMPCLK2      (STM32_SRC_TIMPCLK1 + 1)
#define STM32_SRC_PCLK1         (STM32_SRC_TIMPCLK2 + 1)
#define STM32_SRC_PCLK2         (STM32_SRC_PCLK1 + 1)
#define STM32_SRC_PCLK4         (STM32_SRC_PCLK2 + 1)
#define STM32_SRC_PCLK5         (STM32_SRC_PCLK4 + 1)

#define STM32_CLOCK_BUS_AHB1    0x138
#define STM32_CLOCK_BUS_AHB2    0x13C
#define STM32_CLOCK_BUS_AHB3    0x158
#define STM32_CLOCK_BUS_AHB4    0x140
#define STM32_CLOCK_BUS_AHB5    0x134
#define STM32_CLOCK_BUS_APB1    0x148
#define STM32_CLOCK_BUS_APB1_2  0x14C
#define STM32_CLOCK_BUS_APB2    0x150
#define STM32_CLOCK_BUS_APB4    0x154
#define STM32_CLOCK_BUS_APB5    0x144
#define STM32_PERIPH_BUS_MIN    STM32_CLOCK_BUS_AHB5
#define STM32_PERIPH_BUS_MAX    STM32_CLOCK_BUS_AHB3

#define D1CCIPR_REG             0x4C
#define D2CCIPR_REG             0x50
#define D3CCIPR_REG             0x54
#define D4CCIPR_REG             0x58

#define BDCR_REG                0x70

#define CFGR_REG                0x10


/* TODO to be completed */

#define FMC_SEL(val)            STM32_DT_CLOCK_SELECT((val), 1, 0, D1CCIPR_REG)
#define SDMMC_SEL(val)          STM32_DT_CLOCK_SELECT((val), 2, 2, D1CCIPR_REG)
#define XSPI1_SEL(val)          STM32_DT_CLOCK_SELECT((val), 5, 4, D1CCIPR_REG)
#define XSPI2_SEL(val)          STM32_DT_CLOCK_SELECT((val), 7, 6, D1CCIPR_REG)
#define USBREFCK_SEL(val)       STM32_DT_CLOCK_SELECT((val), 11, 8, D1CCIPR_REG)
#define USBPHYC_SEL(val)        STM32_DT_CLOCK_SELECT((val), 13, 12, D1CCIPR_REG)
#define OTGFS_SEL(val)          STM32_DT_CLOCK_SELECT((val), 15, 14, D1CCIPR_REG)
#define ADC_SEL(val)            STM32_DT_CLOCK_SELECT((val), 25, 24, D1CCIPR_REG)
#define CKPER_SEL(val)          STM32_DT_CLOCK_SELECT((val), 29, 28, D1CCIPR_REG)

#define USART234578_SEL(val)    STM32_DT_CLOCK_SELECT((val), 2, 0, D2CCIPR_REG)
#define SPI23_SEL(val)          STM32_DT_CLOCK_SELECT((val), 6, 4, D2CCIPR_REG)
#define I2C23_SEL(val)          STM32_DT_CLOCK_SELECT((val), 9, 8, D2CCIPR_REG)
#define I2C1_I3C1_SEL(val)      STM32_DT_CLOCK_SELECT((val), 13, 12, D2CCIPR_REG)
#define LPTIM1_SEL(val)         STM32_DT_CLOCK_SELECT((val), 18, 16, D2CCIPR_REG)
#define FDCAN_SEL(val)          STM32_DT_CLOCK_SELECT((val), 23, 22, D2CCIPR_REG)

#define USART1_SEL(val)         STM32_DT_CLOCK_SELECT((val), 2, 0, D3CCIPR_REG)
#define SPI45_SEL(val)          STM32_DT_CLOCK_SELECT((val), 6, 4, D3CCIPR_REG)
#define SPI1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 10, 8, D3CCIPR_REG)
#define SAI1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 18, 16, D3CCIPR_REG)
#define SAI2_SEL(val)           STM32_DT_CLOCK_SELECT((val), 22, 20, D3CCIPR_REG)

#define LPUART1_SEL(val)        STM32_DT_CLOCK_SELECT((val), 2, 0, D4CCIPR_REG)
#define SPI6_SEL(val)           STM32_DT_CLOCK_SELECT((val), 6, 4, D4CCIPR_REG)
#define LPTIM23_SEL(val)        STM32_DT_CLOCK_SELECT((val), 10, 8, D4CCIPR_REG)
#define LPTIM45_SEL(val)        STM32_DT_CLOCK_SELECT((val), 14, 12, D4CCIPR_REG)

#define RTC_SEL(val)            STM32_DT_CLOCK_SELECT((val), 9, 8, BDCR_REG)

#define MCO1_PRE(val)           STM32_DT_CLOCK_SELECT((val), 21, 18, CFGR_REG)
#define MCO1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 24, 22, CFGR_REG)
#define MCO2_PRE(val)           STM32_DT_CLOCK_SELECT((val), 28, 25, CFGR_REG)
#define MCO2_SEL(val)           STM32_DT_CLOCK_SELECT((val), 31, 29, CFGR_REG)

/* MCO prescaler : division factor */
#define MCO_PRE_DIV_1 1
#define MCO_PRE_DIV_2 2
#define MCO_PRE_DIV_3 3
#define MCO_PRE_DIV_4 4
#define MCO_PRE_DIV_5 5
#define MCO_PRE_DIV_6 6
#define MCO_PRE_DIV_7 7
#define MCO_PRE_DIV_8 8
#define MCO_PRE_DIV_9 9
#define MCO_PRE_DIV_10 10
#define MCO_PRE_DIV_11 11
#define MCO_PRE_DIV_12 12
#define MCO_PRE_DIV_13 13
#define MCO_PRE_DIV_14 14
#define MCO_PRE_DIV_15 15


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32H7RS_CLOCK_H_ */
```

## 43.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 STMicroelectronics。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 15 行

参考手册（Reference Manual）：RM0477。

### 注释 3：原第 18 行

在 `stm32_common_clocks.h` 中定义。

### 注释 4：原第 21 行

低速时钟定义在 `stm32_common_clocks.h` 中。

### 注释 5：原第 24 行

内部高速时钟（HSI）加内核时钟保持控制（`HSIKERON`）：`HSI + HSIKERON`。

### 注释 6：原第 25 行

内部 CSI 时钟加内核时钟保持控制（`CSIKERON`）：`CSI + CSIKERON`。

### 注释 7：原第 84 行

待办（TODO）：尚待补充。

### 注释 8：原第 127 行

微控制器时钟输出（MCO）预分频器：分频因子。

### 注释 9：原第 146 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32H7RS_CLOCK_H_`。

## 43.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P440_zephyr__dt-bindings__clock__stm32h7rs_clock.h_文件参考.md)
- [zephyr/dt-bindings/clock/stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)
- [stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)

---

[上一章](P042_stm32g4_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P044_stm32l0_clock.h_源码浏览.md)
