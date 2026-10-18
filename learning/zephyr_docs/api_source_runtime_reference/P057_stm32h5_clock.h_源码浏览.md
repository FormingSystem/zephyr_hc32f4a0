---
id: learning.zephyr-docs.api-source-runtime-reference.page-57
title: stm32h5_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32h5__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第57章\_stm32h5\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32h5__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/stm32h5__clock_8h.html)。

## 57.1\_原始可见代码（Source Code）

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
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00069"></a>
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
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
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
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00132"></a>
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
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="astm32__common__clocks_8h_html"></a>

```c
/*
 * Copyright (c) 2023 STMicroelectronics
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32H5_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32H5_CLOCK_H_

#include <zephyr/dt-bindings/clock/stm32_common_clocks.h>



/* RM0481/0492, Table 47 Kernel clock distribution summary */

/* defined in stm32_common_clocks.h */
/* Low speed clocks defined in stm32_common_clocks.h */
#define STM32_SRC_HSE           (STM32_SRC_LSI + 1)
#define STM32_SRC_CSI           (STM32_SRC_HSE + 1)
#define STM32_SRC_HSI           (STM32_SRC_CSI + 1)
#define STM32_SRC_HSI48         (STM32_SRC_HSI + 1)
#define STM32_SRC_HCLK          (STM32_SRC_HSI48 + 1)
#define STM32_SRC_PCLK1         (STM32_SRC_HCLK + 1)
#define STM32_SRC_PCLK2         (STM32_SRC_PCLK1 + 1)
#define STM32_SRC_PCLK3         (STM32_SRC_PCLK2 + 1)
#define STM32_SRC_TIMPCLK1      (STM32_SRC_PCLK3 + 1)
#define STM32_SRC_TIMPCLK2      (STM32_SRC_TIMPCLK1 + 1)
#define STM32_SRC_PLL1_P        (STM32_SRC_TIMPCLK2 + 1)
#define STM32_SRC_PLL1_Q        (STM32_SRC_PLL1_P + 1)
#define STM32_SRC_PLL1_R        (STM32_SRC_PLL1_Q + 1)
#define STM32_SRC_PLL2_P        (STM32_SRC_PLL1_R + 1)
#define STM32_SRC_PLL2_Q        (STM32_SRC_PLL2_P + 1)
#define STM32_SRC_PLL2_R        (STM32_SRC_PLL2_Q + 1)
#define STM32_SRC_PLL3_P        (STM32_SRC_PLL2_R + 1)
#define STM32_SRC_PLL3_Q        (STM32_SRC_PLL3_P + 1)
#define STM32_SRC_PLL3_R        (STM32_SRC_PLL3_Q + 1)
#define STM32_SRC_CKPER         (STM32_SRC_PLL3_R + 1)

#define STM32_CLOCK_BUS_AHB1    0x088
#define STM32_CLOCK_BUS_AHB2    0x08C
#define STM32_CLOCK_BUS_AHB4    0x094
#define STM32_CLOCK_BUS_APB1    0x09c
#define STM32_CLOCK_BUS_APB1_2  0x0A0
#define STM32_CLOCK_BUS_APB2    0x0A4
#define STM32_CLOCK_BUS_APB3    0x0A8

#define STM32_PERIPH_BUS_MIN    STM32_CLOCK_BUS_AHB1
#define STM32_PERIPH_BUS_MAX    STM32_CLOCK_BUS_APB3

#define CCIPR1_REG              0xD8
#define CCIPR2_REG              0xDC
#define CCIPR3_REG              0xE0
#define CCIPR4_REG              0xE4
#define CCIPR5_REG              0xE8

#define BDCR_REG                0xF0

#define CFGR1_REG               0x1C

#define USART1_SEL(val)         STM32_DT_CLOCK_SELECT((val), 2, 0, CCIPR1_REG)
#define USART2_SEL(val)         STM32_DT_CLOCK_SELECT((val), 5, 3, CCIPR1_REG)
#define USART3_SEL(val)         STM32_DT_CLOCK_SELECT((val), 8, 6, CCIPR1_REG)
#define USART4_SEL(val)         STM32_DT_CLOCK_SELECT((val), 11, 9, CCIPR1_REG)
#define USART5_SEL(val)         STM32_DT_CLOCK_SELECT((val), 14, 12, CCIPR1_REG)
#define USART6_SEL(val)         STM32_DT_CLOCK_SELECT((val), 17, 15, CCIPR1_REG)
#define USART7_SEL(val)         STM32_DT_CLOCK_SELECT((val), 20, 18, CCIPR1_REG)
#define USART8_SEL(val)         STM32_DT_CLOCK_SELECT((val), 23, 21, CCIPR1_REG)
#define USART9_SEL(val)         STM32_DT_CLOCK_SELECT((val), 26, 24, CCIPR1_REG)
#define USART10_SEL(val)        STM32_DT_CLOCK_SELECT((val), 29, 27, CCIPR1_REG)
#define TIMIC_SEL(val)          STM32_DT_CLOCK_SELECT((val), 31, 31, CCIPR1_REG)

#define USART11_SEL(val)        STM32_DT_CLOCK_SELECT((val), 2, 0, CCIPR2_REG)
#define USART12_SEL(val)        STM32_DT_CLOCK_SELECT((val), 6, 4, CCIPR2_REG)
#define LPTIM1_SEL(val)         STM32_DT_CLOCK_SELECT((val), 10, 8, CCIPR2_REG)
#define LPTIM2_SEL(val)         STM32_DT_CLOCK_SELECT((val), 14, 12, CCIPR2_REG)
#define LPTIM3_SEL(val)         STM32_DT_CLOCK_SELECT((val), 18, 16, CCIPR2_REG)
#define LPTIM4_SEL(val)         STM32_DT_CLOCK_SELECT((val), 22, 20, CCIPR2_REG)
#define LPTIM5_SEL(val)         STM32_DT_CLOCK_SELECT((val), 26, 24, CCIPR2_REG)
#define LPTIM6_SEL(val)         STM32_DT_CLOCK_SELECT((val), 30, 28, CCIPR2_REG)

#define SPI1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 2, 0, CCIPR3_REG)
#define SPI2_SEL(val)           STM32_DT_CLOCK_SELECT((val), 5, 3, CCIPR3_REG)
#define SPI3_SEL(val)           STM32_DT_CLOCK_SELECT((val), 8, 6, CCIPR3_REG)
#define SPI4_SEL(val)           STM32_DT_CLOCK_SELECT((val), 11, 9, CCIPR3_REG)
#define SPI5_SEL(val)           STM32_DT_CLOCK_SELECT((val), 14, 12, CCIPR3_REG)
#define SPI6_SEL(val)           STM32_DT_CLOCK_SELECT((val), 17, 15, CCIPR3_REG)
#define LPUART1_SEL(val)        STM32_DT_CLOCK_SELECT((val), 26, 24, CCIPR3_REG)

#define OCTOSPI1_SEL(val)       STM32_DT_CLOCK_SELECT((val), 1, 0, CCIPR4_REG)
#define SYSTICK_SEL(val)        STM32_DT_CLOCK_SELECT((val), 3, 2, CCIPR4_REG)
#define USB_SEL(val)            STM32_DT_CLOCK_SELECT((val), 5, 4, CCIPR4_REG)
#define OTGFS_SEL(val)          STM32_DT_CLOCK_SELECT((val), 5, 4, CCIPR4_REG)
#define SDMMC1_SEL(val)         STM32_DT_CLOCK_SELECT((val), 6, 6, CCIPR4_REG)
#define SDMMC2_SEL(val)         STM32_DT_CLOCK_SELECT((val), 7, 7, CCIPR4_REG)
#define OTGHS_SEL(val)          STM32_DT_CLOCK_SELECT((val), 11, 10, CCIPR4_REG)
#define OTGPHYREFCK_SEL(val)    STM32_DT_CLOCK_SELECT((val), 15, 12, CCIPR4_REG)
#define I2C1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 17, 16, CCIPR4_REG)
#define I2C2_SEL(val)           STM32_DT_CLOCK_SELECT((val), 19, 18, CCIPR4_REG)
#define I2C3_SEL(val)           STM32_DT_CLOCK_SELECT((val), 21, 20, CCIPR4_REG)
#define I2C4_SEL(val)           STM32_DT_CLOCK_SELECT((val), 23, 22, CCIPR4_REG)
#define I3C1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 25, 24, CCIPR4_REG)

#define ADCDAC_SEL(val)         STM32_DT_CLOCK_SELECT((val), 2, 0, CCIPR5_REG)
#define DAC_SEL(val)            STM32_DT_CLOCK_SELECT((val), 3, 3, CCIPR5_REG)
#define RNG_SEL(val)            STM32_DT_CLOCK_SELECT((val), 5, 4, CCIPR5_REG)
#define CEC_SEL(val)            STM32_DT_CLOCK_SELECT((val), 7, 6, CCIPR5_REG)
#define FDCAN_SEL(val)          STM32_DT_CLOCK_SELECT((val), 9, 8, CCIPR5_REG)
#define OCTOSPI2_SEL(val)       STM32_DT_CLOCK_SELECT((val), 13, 12, CCIPR5_REG)
#define SAI1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 18, 16, CCIPR5_REG)
#define SAI2_SEL(val)           STM32_DT_CLOCK_SELECT((val), 21, 19, CCIPR5_REG)
#define LTDC_SEL(val)           STM32_DT_CLOCK_SELECT((val), 22, 22, CCIPR5_REG)
#define CKPER_SEL(val)          STM32_DT_CLOCK_SELECT((val), 31, 30, CCIPR5_REG)

#define RTC_SEL(val)            STM32_DT_CLOCK_SELECT((val), 9, 8, BDCR_REG)

#define MCO1_PRE(val)           STM32_DT_CLOCK_SELECT((val), 21, 18, CFGR1_REG)
#define MCO1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 24, 22, CFGR1_REG)
#define MCO2_PRE(val)           STM32_DT_CLOCK_SELECT((val), 28, 25, CFGR1_REG)
#define MCO2_SEL(val)           STM32_DT_CLOCK_SELECT((val), 31, 29, CFGR1_REG)

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


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32H5_CLOCK_H_ */
```

## 57.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 STMicroelectronics。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 15 行

`RM0481/0492` 表 47：内核时钟分配汇总（Kernel clock distribution summary）。

### 注释 3：原第 18 行

在 `stm32_common_clocks.h` 中定义。

### 注释 4：原第 20 行

低速时钟定义在 `stm32_common_clocks.h` 中。

### 注释 5：原第 139 行

微控制器时钟输出（MCO）预分频器：分频因子。

### 注释 6：原第 158 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32H5_CLOCK_H_`。

## 57.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/stm32h5__clock_8h.html)
- [zephyr/dt-bindings/clock/stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)
- [stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)

---

[上一章](P056_stm32g0_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P058_stm32l1_clock.h_源码浏览.md)
