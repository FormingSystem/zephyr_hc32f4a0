---
id: learning.zephyr-docs.api-source-device-reference.page-47
title: stm32mp13_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32mp13__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第47章\_stm32mp13\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32mp13__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P449_zephyr__dt-bindings__clock__stm32mp13_clock.h_文件参考.md)。

## 47.1\_原始可见代码（Source Code）

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
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
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
<a id="l00054"></a>
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
<a id="l00086"></a>
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
<a id="l00168"></a>
<a id="l00169"></a>
<a id="astm32__common__clocks_8h_html"></a>

```c
/*
 * Copyright (c) 2025 STMicroelectronics
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32MP13_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32MP13_CLOCK_H_

#include <zephyr/dt-bindings/clock/stm32_common_clocks.h>


/* defined in stm32_common_clocks.h */
#define STM32_SRC_HSE           (STM32_SRC_LSI + 1)
#define STM32_SRC_HSI           (STM32_SRC_HSE + 1)

#define STM32_SRC_PLL1_P        (STM32_SRC_HSI + 1)
#define STM32_SRC_PLL2_P        (STM32_SRC_PLL1_P + 1)
#define STM32_SRC_PLL2_Q        (STM32_SRC_PLL2_P + 1)
#define STM32_SRC_PLL2_R        (STM32_SRC_PLL2_Q + 1)
#define STM32_SRC_PLL3_P        (STM32_SRC_PLL2_R + 1)
#define STM32_SRC_PLL3_Q        (STM32_SRC_PLL3_P + 1)
#define STM32_SRC_PLL3_R        (STM32_SRC_PLL3_Q + 1)
#define STM32_SRC_PLL4_P        (STM32_SRC_PLL3_R + 1)
#define STM32_SRC_PLL4_Q        (STM32_SRC_PLL4_P + 1)
#define STM32_SRC_PLL4_R        (STM32_SRC_PLL4_Q + 1)

#define STM32_SRC_TIMPCLK1      (STM32_SRC_PLL4_R + 1)
#define STM32_SRC_TIMPCLK2      (STM32_SRC_TIMPCLK1 + 1)
#define STM32_SRC_TIMPCLK6      (STM32_SRC_TIMPCLK2 + 1)

#define STM32_CLOCK_BUS_APB1    0x700
#define STM32_CLOCK_BUS_APB2    0x708
#define STM32_CLOCK_BUS_APB3    0x710
#define STM32_CLOCK_BUS_APB3_S  0x718
#define STM32_CLOCK_BUS_APB4    0x728
#define STM32_CLOCK_BUS_APB4_NS 0x738
#define STM32_CLOCK_BUS_APB5    0x740
#define STM32_CLOCK_BUS_APB6    0x748
#define STM32_CLOCK_BUS_AHB2    0x750
#define STM32_CLOCK_BUS_AHB4    0x768
#define STM32_CLOCK_BUS_AHB5    0x778
#define STM32_CLOCK_BUS_AHB6    0x780

#define STM32_PERIPH_BUS_MIN    STM32_CLOCK_BUS_APB1
#define STM32_PERIPH_BUS_MAX    STM32_CLOCK_BUS_AHB6

#define BDCR_REG                0x400
#define MCO1CFGR_REG            0x460
#define MCO2CFGR_REG            0x464
#define I2C12CKSELR_REG         0x600
#define I2C345CKSELR_REG        0x604
#define SPI2S1CKSELR_REG        0x608
#define SPI2S23CKSELR_REG       0x60c
#define SPI45CKSELR_REG         0x610
#define UART12CKSELR_REG        0x614
#define UART35CKSELR_REG        0x618
#define UART4CKSELR_REG         0x61c
#define UART6CKSELR_REG         0x620
#define UART78CKSELR_REG        0x624
#define LPTIM1CKSELR_REG        0x628
#define LPTIM23CKSELR_REG       0x62c
#define LPTIM45CKSELR_REG       0x630
#define SAI1CKSELR_REG          0x634
#define SAI2CKSELR_REG          0x638
#define FDCANCKSELR_REG         0x63c
#define SPDIFCKSELR_REG         0x640
#define ADC12CKSELR_REG         0x644
#define SDMMC12CKSELR_REG       0x648
#define ETH12CKSELR_REG         0x64c
#define USBCKSELR_REG           0x650
#define QSPICKSELR_REG          0x654
#define FMCCKSELR_REG           0x658
#define RNG1CKSELR_REG          0x65c
#define STGENCKSELR_REG         0x660
#define DCMIPPCKSELR_REG        0x664
#define SAESCKSELR_REG          0x668

#define MCO1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 2, 0, MCO1CFGR_REG)
#define MCO1_PRE(val)           STM32_DT_CLOCK_SELECT((val), 7, 4, MCO1CFGR_REG)
#define MCO2_SEL(val)           STM32_DT_CLOCK_SELECT((val), 2, 0, MCO2CFGR_REG)
#define MCO2_PRE(val)           STM32_DT_CLOCK_SELECT((val), 7, 4, MCO2CFGR_REG)

#define MCOX_ON BIT(12)

/* MCO1 source */
#define MCO1_SEL_HSI    0
#define MCO1_SEL_HSE    1
#define MCO1_SEL_CSI    2
#define MCO1_SEL_LSI    3
#define MCO1_SEL_LSE    4

/* MCO2 source */
#define MCO2_SEL_MPU    0
#define MCO2_SEL_AXI    1
#define MCO2_SEL_MLAHB  2
#define MCO2_SEL_PLL4   3
#define MCO2_SEL_HSE    4
#define MCO2_SEL_HSI    5

/* MCO prescaler : division factor */
#define MCO_PRE_DIV_1   0
#define MCO_PRE_DIV_2   1
#define MCO_PRE_DIV_3   2
#define MCO_PRE_DIV_4   3
#define MCO_PRE_DIV_5   4
#define MCO_PRE_DIV_6   5
#define MCO_PRE_DIV_7   6
#define MCO_PRE_DIV_8   7
#define MCO_PRE_DIV_9   8
#define MCO_PRE_DIV_10  9
#define MCO_PRE_DIV_11  10
#define MCO_PRE_DIV_12  11
#define MCO_PRE_DIV_13  12
#define MCO_PRE_DIV_14  13
#define MCO_PRE_DIV_15  14
#define MCO_PRE_DIV_16  15

#define I2C12_SEL(val)          STM32_DT_CLOCK_SELECT((val), 2, 0, I2C12CKSELR_REG)
#define I2C3_SEL(val)           STM32_DT_CLOCK_SELECT((val), 2, 0, I2C345CKSELR_REG)
#define I2C4_SEL(val)           STM32_DT_CLOCK_SELECT((val), 5, 3, I2C345CKSELR_REG)
#define I2C5_SEL(val)           STM32_DT_CLOCK_SELECT((val), 8, 6, I2C345CKSELR_REG)
#define SPI1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 2, 0, SPI2S1CKSELR_REG)
#define SPI23_SEL(val)          STM32_DT_CLOCK_SELECT((val), 2, 0, SPI2S23CKSELR_REG)
#define SPI4_SEL(val)           STM32_DT_CLOCK_SELECT((val), 2, 0, SPI45CKSELR_REG)
#define SPI5_SEL(val)           STM32_DT_CLOCK_SELECT((val), 5, 3, SPI45CKSELR_REG)
#define UART1_SEL(val)          STM32_DT_CLOCK_SELECT((val), 2, 0, UART12CKSELR_REG)
#define UART2_SEL(val)          STM32_DT_CLOCK_SELECT((val), 5, 3, UART12CKSELR_REG)
#define UART35_SEL(val)         STM32_DT_CLOCK_SELECT((val), 2, 0, UART35CKSELR_REG)
#define UART4_SEL(val)          STM32_DT_CLOCK_SELECT((val), 2, 0, UART4CKSELR_REG)
#define UART6_SEL(val)          STM32_DT_CLOCK_SELECT((val), 2, 0, UART6CKSELR_REG)
#define UART78_SEL(val)         STM32_DT_CLOCK_SELECT((val), 2, 0, UART78CKSELR_REG)
#define LPTIME1_SEL(val)        STM32_DT_CLOCK_SELECT((val), 2, 0, LPTIM1CKSELR_REG)
#define LPTIME2_SEL(val)        STM32_DT_CLOCK_SELECT((val), 2, 0, LPTIM23CKSELR_REG)
#define LPTIME3_SEL(val)        STM32_DT_CLOCK_SELECT((val), 5, 3, LPTIM23CKSELR_REG)
#define LPTIME45_SEL(val)       STM32_DT_CLOCK_SELECT((val), 2, 0, LPTIM45CKSELR_REG)
#define SAI1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 2, 0, SAI1CKSELR_REG)
#define SAI2_SEL(val)           STM32_DT_CLOCK_SELECT((val), 2, 0, SAI2CKSELR_REG)
#define FDCAN_SEL(val)          STM32_DT_CLOCK_SELECT((val), 1, 0, FDCANCKSELR_REG)
#define SPDIF_SEL(val)          STM32_DT_CLOCK_SELECT((val), 1, 0, SPDIFCKSELR_REG)
#define ADC1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 1, 0, ADC12CKSELR_REG)
#define ADC2_SEL(val)           STM32_DT_CLOCK_SELECT((val), 3, 2, ADC12CKSELR_REG)
#define SDMMC1_SEL(val)         STM32_DT_CLOCK_SELECT((val), 2, 0, SDMMC12CKSELR_REG)
#define SDMMC2_SEL(val)         STM32_DT_CLOCK_SELECT((val), 5, 3, SDMMC12CKSELR_REG)
#define ETH1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 1, 0, ETH12CKSELR_REG)
#define ETH2_SEL(val)           STM32_DT_CLOCK_SELECT((val), 9, 8, ETH12CKSELR_REG)
/* The PTP clock is the ETHx kernel clock divided by (val + 1) */
#define ETH1_PTP_DIV(val)       STM32_DT_CLOCK_SELECT((val), 7, 4, ETH12CKSELR_REG)
#define ETH2_PTP_DIV(val)       STM32_DT_CLOCK_SELECT((val), 15, 12, ETH12CKSELR_REG)
#define USBPHY_SEL(val)         STM32_DT_CLOCK_SELECT((val), 1, 0, USBCKSELR_REG)
#define USBOTG_SEL(val)         STM32_DT_CLOCK_SELECT((val), 4, 4, USBCKSELR_REG)
#define QSPI_SEL(val)           STM32_DT_CLOCK_SELECT((val), 1, 0, QSPICKSELR_REG)
#define FMC_SEL(val)            STM32_DT_CLOCK_SELECT((val), 1, 0, FMCCKSELR_REG)
#define RNG1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 1, 0, RNG1CKSELR_REG)
#define STGEN_SEL(val)          STM32_DT_CLOCK_SELECT((val), 1, 0, STGENCKSELR_REG)
#define DCMIPP_SEL(val)         STM32_DT_CLOCK_SELECT((val), 1, 0, DCMIPPCKSELR_REG)
#define SAES_SEL(val)           STM32_DT_CLOCK_SELECT((val), 1, 0, SAESCKSELR_REG)
#define RTC_SEL(val)            STM32_DT_CLOCK_SELECT((val), 17, 16, BDCR_REG)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32MP13_CLOCK_H_ */
```

## 47.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 STMicroelectronics。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 14 行

在 `stm32_common_clocks.h` 中定义。

### 注释 3：原第 93 行

微控制器时钟输出 1 的时钟源（MCO1 Source）。

### 注释 4：原第 100 行

微控制器时钟输出 2 的时钟源（MCO2 Source）。

### 注释 5：原第 108 行

微控制器时钟输出（MCO）预分频器：分频因子。

### 注释 6：原第 154 行

精确时间协议时钟（PTP Clock）等于 ETHx 内核时钟（Kernel Clock）除以 `val + 1`。

### 注释 7：原第 169 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32MP13_CLOCK_H_`。

## 47.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P449_zephyr__dt-bindings__clock__stm32mp13_clock.h_文件参考.md)
- [zephyr/dt-bindings/clock/stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)
- [stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)

---

[上一章](P046_stm32l5_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P048_stm32u3_clock.h_源码浏览.md)
