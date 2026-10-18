---
id: learning.zephyr-docs.api-source-system-reference.page-46
title: stm32n6_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32n6__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第46章\_stm32n6\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32n6__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P455_zephyr__dt-bindings__clock__stm32n6_clock.h_文件参考.md)。

## 46.1\_原始可见代码（Source Code）

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
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
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
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
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
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
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
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="astm32__common__clocks_8h_html"></a>

```c
/*
 * Copyright (c) 2024 STMicroelectronics
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32N6_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32N6_CLOCK_H_

#include <zephyr/dt-bindings/clock/stm32_common_clocks.h>



/* RM0486, Figures 37 and 45 on clock distribution description */

/* defined in stm32_common_clocks.h */
#define STM32_SRC_HSE           (STM32_SRC_LSI + 1)
#define STM32_SRC_HSI           (STM32_SRC_HSE + 1)
#define STM32_SRC_MSI           (STM32_SRC_HSI + 1)
#define STM32_SRC_PLL1          (STM32_SRC_MSI + 1)
#define STM32_SRC_PLL2          (STM32_SRC_PLL1 + 1)
#define STM32_SRC_PLL3          (STM32_SRC_PLL2 + 1)
#define STM32_SRC_PLL4          (STM32_SRC_PLL3 + 1)
#define STM32_SRC_CKPER         (STM32_SRC_PLL4 + 1)
#define STM32_SRC_IC1           (STM32_SRC_CKPER + 1)
#define STM32_SRC_IC2           (STM32_SRC_IC1 + 1)
#define STM32_SRC_IC3           (STM32_SRC_IC2 + 1)
#define STM32_SRC_IC4           (STM32_SRC_IC3 + 1)
#define STM32_SRC_IC5           (STM32_SRC_IC4 + 1)
#define STM32_SRC_IC6           (STM32_SRC_IC5 + 1)
#define STM32_SRC_IC7           (STM32_SRC_IC6 + 1)
#define STM32_SRC_IC8           (STM32_SRC_IC7 + 1)
#define STM32_SRC_IC9           (STM32_SRC_IC8 + 1)
#define STM32_SRC_IC10          (STM32_SRC_IC9 + 1)
#define STM32_SRC_IC11          (STM32_SRC_IC10 + 1)
#define STM32_SRC_IC12          (STM32_SRC_IC11 + 1)
#define STM32_SRC_IC13          (STM32_SRC_IC12 + 1)
#define STM32_SRC_IC14          (STM32_SRC_IC13 + 1)
#define STM32_SRC_IC15          (STM32_SRC_IC14 + 1)
#define STM32_SRC_IC16          (STM32_SRC_IC15 + 1)
#define STM32_SRC_IC17          (STM32_SRC_IC16 + 1)
#define STM32_SRC_IC18          (STM32_SRC_IC17 + 1)
#define STM32_SRC_IC19          (STM32_SRC_IC18 + 1)
#define STM32_SRC_IC20          (STM32_SRC_IC19 + 1)
#define STM32_SRC_HSI_DIV       (STM32_SRC_IC20 + 1)
#define STM32_SRC_HSE_DIV2_OSC  (STM32_SRC_HSI_DIV + 1)
#define STM32_SRC_TIMG          (STM32_SRC_HSE_DIV2_OSC + 1)
#define STM32_SRC_HCLK1         (STM32_SRC_TIMG + 1)
#define STM32_SRC_HCLK2         (STM32_SRC_HCLK1 + 1)
#define STM32_SRC_HCLK3         (STM32_SRC_HCLK2 + 1)
#define STM32_SRC_HCLK4         (STM32_SRC_HCLK3 + 1)
#define STM32_SRC_HCLK5         (STM32_SRC_HCLK4 + 1)
#define STM32_SRC_PCLK1         (STM32_SRC_HCLK5 + 1)
#define STM32_SRC_PCLK2         (STM32_SRC_PCLK1 + 1)
#define STM32_SRC_PCLK4         (STM32_SRC_PCLK2 + 1)
#define STM32_SRC_PCLK5         (STM32_SRC_PCLK4 + 1)

/* #define STM32_SRC_I2SCKIN    TBD */

#define STM32_CLOCK_BUS_MISC    0x248
#define STM32_CLOCK_BUS_MEM     0x24C
#define STM32_CLOCK_BUS_AHB1    0x250
#define STM32_CLOCK_BUS_AHB2    0x254
#define STM32_CLOCK_BUS_AHB3    0x258
#define STM32_CLOCK_BUS_AHB4    0x25C
#define STM32_CLOCK_BUS_AHB5    0x260
#define STM32_CLOCK_BUS_APB1    0x264
#define STM32_CLOCK_BUS_APB1_2  0x268
#define STM32_CLOCK_BUS_APB2    0x26C
#define STM32_CLOCK_BUS_APB3    0x270
#define STM32_CLOCK_BUS_APB4    0x274
#define STM32_CLOCK_BUS_APB4_2  0x278
#define STM32_CLOCK_BUS_APB5    0x27C

#define STM32_CLOCK_LP_BUS_SHIFT        0x40

#define STM32_PERIPH_BUS_MIN    STM32_CLOCK_BUS_MISC
#define STM32_PERIPH_BUS_MAX    STM32_CLOCK_BUS_APB5

#define CCIPR1_REG              0x144
#define CCIPR2_REG              0x148
#define CCIPR3_REG              0x14C
#define CCIPR4_REG              0x150
#define CCIPR5_REG              0x154
#define CCIPR6_REG              0x158
#define CCIPR7_REG              0x15C
#define CCIPR8_REG              0x160
#define CCIPR9_REG              0x164
#define CCIPR12_REG             0x170
#define CCIPR13_REG             0x174
#define CCIPR14_REG             0x178

#define ADF1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 2, 0, CCIPR1_REG)
#define ADC12_SEL(val)          STM32_DT_CLOCK_SELECT((val), 6, 4, CCIPR1_REG)
#define ADC_PRE(val)            STM32_DT_CLOCK_SELECT((val), 15, 8, CCIPR1_REG)
#define DCMIPP_SEL(val)         STM32_DT_CLOCK_SELECT((val), 21, 20, CCIPR1_REG)
#define ETH1PTP_SEL(val)        STM32_DT_CLOCK_SELECT((val), 1, 0, CCIPR2_REG)
#define ETH1CLK_SEL(val)        STM32_DT_CLOCK_SELECT((val), 13, 12, CCIPR2_REG)
#define ETH1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 18, 16, CCIPR2_REG)
#define ETH1REFCLK_SEL(val)     STM32_DT_CLOCK_SELECT((val), 20, 20, CCIPR2_REG)
#define ETH1GTXCLK_SEL(val)     STM32_DT_CLOCK_SELECT((val), 24, 24, CCIPR2_REG)
#define FDCAN_SEL(val)          STM32_DT_CLOCK_SELECT((val), 1, 0, CCIPR3_REG)
#define FMC_SEL(val)            STM32_DT_CLOCK_SELECT((val), 5, 4, CCIPR3_REG)
#define I2C1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 2, 0, CCIPR4_REG)
#define I2C2_SEL(val)           STM32_DT_CLOCK_SELECT((val), 6, 4, CCIPR4_REG)
#define I2C3_SEL(val)           STM32_DT_CLOCK_SELECT((val), 10, 8, CCIPR4_REG)
#define I2C4_SEL(val)           STM32_DT_CLOCK_SELECT((val), 14, 12, CCIPR4_REG)
#define I3C1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 18, 16, CCIPR4_REG)
#define I3C2_SEL(val)           STM32_DT_CLOCK_SELECT((val), 22, 20, CCIPR4_REG)
#define LTDC_SEL(val)           STM32_DT_CLOCK_SELECT((val), 25, 24, CCIPR4_REG)
#define MCO1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 2, 0, CCIPR5_REG)
#define MCO1_PRE(val)           STM32_DT_CLOCK_SELECT((val), 7, 4, CCIPR5_REG)
#define MCO2_SEL(val)           STM32_DT_CLOCK_SELECT((val), 10, 8, CCIPR5_REG)
#define MCO2_PRE(val)           STM32_DT_CLOCK_SELECT((val), 15, 12, CCIPR5_REG)
#define MDF1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 18, 16, CCIPR5_REG)

/* MCO1 source */
#define MCO1_SEL_HSI  0
#define MCO1_SEL_LSE  1
#define MCO1_SEL_MSI  2
#define MCO1_SEL_LSI  3
#define MCO1_SEL_HSE  4
#define MCO1_SEL_IC5  5
#define MCO1_SEL_IC10 6
#define MCO1_SEL_SYSA 7

/* MCO2 source */
#define MCO2_SEL_HSI  0
#define MCO2_SEL_LSE  1
#define MCO2_SEL_MSI  2
#define MCO2_SEL_LSI  3
#define MCO2_SEL_HSE  4
#define MCO2_SEL_IC15 5
#define MCO2_SEL_IC20 6
#define MCO2_SEL_SYSB 7

/* MCO prescaler : division factor */
#define MCO_PRE_DIV_1  0
#define MCO_PRE_DIV_2  1
#define MCO_PRE_DIV_3  2
#define MCO_PRE_DIV_4  3
#define MCO_PRE_DIV_5  4
#define MCO_PRE_DIV_6  5
#define MCO_PRE_DIV_7  6
#define MCO_PRE_DIV_8  7
#define MCO_PRE_DIV_9  8
#define MCO_PRE_DIV_10 9
#define MCO_PRE_DIV_11 10
#define MCO_PRE_DIV_12 11
#define MCO_PRE_DIV_13 12
#define MCO_PRE_DIV_14 13
#define MCO_PRE_DIV_15 14
#define MCO_PRE_DIV_16 15

#define MDF1SEL(val)            STM32_DT_CLOCK_SELECT((val), 18, 16, CCIPR5_REG)
#define XSPI1_SEL(val)          STM32_DT_CLOCK_SELECT((val), 1, 0, CCIPR6_REG)
#define XSPI2_SEL(val)          STM32_DT_CLOCK_SELECT((val), 5, 4, CCIPR6_REG)
#define XSPI3_SEL(val)          STM32_DT_CLOCK_SELECT((val), 9, 8, CCIPR6_REG)
#define OTGPHY1_SEL(val)        STM32_DT_CLOCK_SELECT((val), 13, 12, CCIPR6_REG)
#define OTGPHY1CKREF_SEL(val)   STM32_DT_CLOCK_SELECT((val), 16, 16, CCIPR6_REG)
#define OTGPHY2_SEL(val)        STM32_DT_CLOCK_SELECT((val), 21, 20, CCIPR6_REG)
#define OTGPHY2CKREF_SEL(val)   STM32_DT_CLOCK_SELECT((val), 24, 24, CCIPR6_REG)
#define PER_SEL(val)            STM32_DT_CLOCK_SELECT((val), 2, 0, CCIPR7_REG)
#define PSSI_SEL(val)           STM32_DT_CLOCK_SELECT((val), 5, 4, CCIPR7_REG)
#define RTC_SEL(val)            STM32_DT_CLOCK_SELECT((val), 9, 8, CCIPR7_REG)
#define SAI1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 22, 20, CCIPR7_REG)
#define SAI2_SEL(val)           STM32_DT_CLOCK_SELECT((val), 26, 24, CCIPR7_REG)
#define SDMMC1_SEL(val)         STM32_DT_CLOCK_SELECT((val), 1, 0, CCIPR8_REG)
#define SDMMC2_SEL(val)         STM32_DT_CLOCK_SELECT((val), 5, 4, CCIPR8_REG)
#define SPDIFRX1_SEL(val)       STM32_DT_CLOCK_SELECT((val), 2, 0, CCIPR9_REG)
#define SPI1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 6, 4, CCIPR9_REG)
#define SPI2_SEL(val)           STM32_DT_CLOCK_SELECT((val), 10, 8, CCIPR9_REG)
#define SPI3_SEL(val)           STM32_DT_CLOCK_SELECT((val), 14, 12, CCIPR9_REG)
#define SPI4_SEL(val)           STM32_DT_CLOCK_SELECT((val), 18, 16, CCIPR9_REG)
#define SPI5_SEL(val)           STM32_DT_CLOCK_SELECT((val), 22, 20, CCIPR9_REG)
#define SPI6_SEL(val)           STM32_DT_CLOCK_SELECT((val), 26, 24, CCIPR9_REG)
#define LPTIM1_SEL(val)         STM32_DT_CLOCK_SELECT((val), 10, 8, CCIPR12_REG)
#define LPTIM2_SEL(val)         STM32_DT_CLOCK_SELECT((val), 14, 12, CCIPR12_REG)
#define LPTIM3_SEL(val)         STM32_DT_CLOCK_SELECT((val), 18, 16, CCIPR12_REG)
#define LPTIM4_SEL(val)         STM32_DT_CLOCK_SELECT((val), 22, 20, CCIPR12_REG)
#define LPTIM5_SEL(val)         STM32_DT_CLOCK_SELECT((val), 26, 24, CCIPR12_REG)
#define USART1_SEL(val)         STM32_DT_CLOCK_SELECT((val), 2, 0, CCIPR13_REG)
#define USART2_SEL(val)         STM32_DT_CLOCK_SELECT((val), 6, 4, CCIPR13_REG)
#define USART3_SEL(val)         STM32_DT_CLOCK_SELECT((val), 10, 8, CCIPR13_REG)
#define UART4_SEL(val)          STM32_DT_CLOCK_SELECT((val), 14, 12, CCIPR13_REG)
#define UART5_SEL(val)          STM32_DT_CLOCK_SELECT((val), 18, 16, CCIPR13_REG)
#define USART6_SEL(val)         STM32_DT_CLOCK_SELECT((val), 22, 20, CCIPR13_REG)
#define UART7_SEL(val)          STM32_DT_CLOCK_SELECT((val), 26, 24, CCIPR13_REG)
#define UART8_SEL(val)          STM32_DT_CLOCK_SELECT((val), 30, 28, CCIPR13_REG)
#define UART9_SEL(val)          STM32_DT_CLOCK_SELECT((val), 2, 0, CCIPR14_REG)
#define USART10_SEL(val)        STM32_DT_CLOCK_SELECT((val), 6, 4, CCIPR14_REG)
#define LPUART1_SEL(val)        STM32_DT_CLOCK_SELECT((val), 10, 8, CCIPR14_REG)

#define ICxCFGR_REG(ic)         (0xC4 + ((ic) - 1) * 4)

#define ICx_PLLy_SEL(ic, pll)   STM32_DT_CLOCK_SELECT((pll) - 1, 29, 28, ICxCFGR_REG(ic))

#define CFGR1_REG               0x20

#define CPU_SEL(val)            STM32_DT_CLOCK_SELECT((val), 17, 16, CFGR1_REG)

/* ADC prescaler division factor helper */
#define ADC_PRE_DIV(pres)       ((pres - 1) & 0xFFU)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32N6_CLOCK_H_ */
```

## 46.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 STMicroelectronics。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 15 行

参考手册 RM0486，图 37 和图 45 中的时钟分配说明（Clock Distribution Description）。

### 注释 3：原第 18 行

在 `stm32_common_clocks.h` 中定义。

### 注释 4：原第 64 行

原注释中的待定宏（TBD）：`#define STM32_SRC_I2SCKIN    TBD`。

### 注释 5：原第 131 行

微控制器时钟输出 1 的时钟源（MCO1 Source）。

### 注释 6：原第 141 行

微控制器时钟输出 2 的时钟源（MCO2 Source）。

### 注释 7：原第 151 行

微控制器时钟输出（MCO）预分频器：分频因子。

### 注释 8：原第 227 行

模数转换器预分频系数辅助宏（ADC Prescaler Division Factor Helper）。

### 注释 9：原第 232 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32N6_CLOCK_H_`。

## 46.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P455_zephyr__dt-bindings__clock__stm32n6_clock.h_文件参考.md)
- [zephyr/dt-bindings/clock/stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)
- [stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)

---

[上一章](P045_stm32mp2_reset.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P047_structs.h_源码浏览.md)
