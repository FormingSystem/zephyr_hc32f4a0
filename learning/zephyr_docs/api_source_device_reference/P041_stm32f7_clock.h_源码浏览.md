---
id: learning.zephyr-docs.api-source-device-reference.page-41
title: stm32f7_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32f7__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第41章\_stm32f7\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32f7__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P430_zephyr__dt-bindings__clock__stm32f7_clock.h_文件参考.md)。

## 41.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00018"></a>
<a id="l00020"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
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
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
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
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00067"></a>
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
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
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
<a id="l00124"></a>
<a id="l00125"></a>
<a id="astm32__common__clocks_8h_html"></a>

```c
/*
 * Copyright (c) 2022 STMicroelectronics
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F7_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F7_CLOCK_H_

#include <zephyr/dt-bindings/clock/stm32_common_clocks.h>



#define STM32_CLOCK_BUS_AHB1    0x030
#define STM32_CLOCK_BUS_AHB2    0x034
#define STM32_CLOCK_BUS_AHB3    0x038
#define STM32_CLOCK_BUS_APB1    0x040
#define STM32_CLOCK_BUS_APB2    0x044
#define STM32_CLOCK_BUS_APB3    0x0A8

#define STM32_PERIPH_BUS_MIN    STM32_CLOCK_BUS_AHB1
#define STM32_PERIPH_BUS_MAX    STM32_CLOCK_BUS_APB3

/* RM0386, 0390, 0402, 0430 § Dedicated Clock configuration register (RCC_DCKCFGRx) */

/* defined in stm32_common_clocks.h */

/* Low speed clocks defined in stm32_common_clocks.h */
#define STM32_SRC_HSI           (STM32_SRC_LSI + 1)
#define STM32_SRC_HSE           (STM32_SRC_HSI + 1)
#define STM32_SRC_PLL_P         (STM32_SRC_HSE + 1)
#define STM32_SRC_PLL_Q         (STM32_SRC_PLL_P + 1)
#define STM32_SRC_PLL_R         (STM32_SRC_PLL_Q + 1)
#define STM32_SRC_PLLI2S_P      (STM32_SRC_PLL_R + 1)
#define STM32_SRC_PLLI2S_Q      (STM32_SRC_PLLI2S_P + 1)
#define STM32_SRC_PLLI2S_POST_Q (STM32_SRC_PLLI2S_Q + 1)
#define STM32_SRC_PLLI2S_R      (STM32_SRC_PLLI2S_POST_Q + 1)
/* PLLSAI clock outputs */
#define STM32_SRC_PLLSAI_P      (STM32_SRC_PLLI2S_R + 1)
#define STM32_SRC_PLLSAI_Q      (STM32_SRC_PLLSAI_P + 1)
#define STM32_SRC_PLLSAI_POST_Q (STM32_SRC_PLLSAI_Q + 1)
#define STM32_SRC_PLLSAI_R      (STM32_SRC_PLLSAI_POST_Q + 1)
#define STM32_SRC_PLLSAI_POST_R (STM32_SRC_PLLSAI_R + 1)
#define STM32_SRC_PCLK          (STM32_SRC_PLLSAI_POST_R + 1)
#define STM32_SRC_TIMPCLK1      (STM32_SRC_PCLK + 1)
#define STM32_SRC_TIMPCLK2      (STM32_SRC_TIMPCLK1 + 1)

#define CFGR_REG                0x08

#define BDCR_REG                0x70

#define MCO1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 22, 21, CFGR_REG)
#define I2S_SEL(val)            STM32_DT_CLOCK_SELECT((val), 23, 23, CFGR_REG)
#define MCO1_PRE(val)           STM32_DT_CLOCK_SELECT((val), 26, 24, CFGR_REG)
#define MCO2_PRE(val)           STM32_DT_CLOCK_SELECT((val), 29, 27, CFGR_REG)
#define MCO2_SEL(val)           STM32_DT_CLOCK_SELECT((val), 31, 30, CFGR_REG)

/* MCO prescaler : division factor */
#define MCO_PRE_DIV_1 0
#define MCO_PRE_DIV_2 4
#define MCO_PRE_DIV_3 5
#define MCO_PRE_DIV_4 6
#define MCO_PRE_DIV_5 7

#define MCO1_SEL_HSI            0
#define MCO1_SEL_LSE            1
#define MCO1_SEL_HSE            2
#define MCO1_SEL_PLL            3

#define MCO2_SEL_SYSCLK         0
#define MCO2_SEL_PLL2S          1
#define MCO2_SEL_HSE            2
#define MCO2_SEL_PLL            3

#define RTC_SEL(val)            STM32_DT_CLOCK_SELECT((val), 9, 8, BDCR_REG)

#define DCKCFGR1_REG            0x8C
#define DCKCFGR2_REG            0x90

#define USART1_SEL(val)         STM32_DT_CLOCK_SELECT((val), 1, 0, DCKCFGR2_REG)
#define USART2_SEL(val)         STM32_DT_CLOCK_SELECT((val), 3, 2, DCKCFGR2_REG)
#define USART3_SEL(val)         STM32_DT_CLOCK_SELECT((val), 5, 4, DCKCFGR2_REG)
#define USART4_SEL(val)         STM32_DT_CLOCK_SELECT((val), 7, 6, DCKCFGR2_REG)
#define USART5_SEL(val)         STM32_DT_CLOCK_SELECT((val), 9, 8, DCKCFGR2_REG)
#define USART6_SEL(val)         STM32_DT_CLOCK_SELECT((val), 11, 10, DCKCFGR2_REG)
#define USART7_SEL(val)         STM32_DT_CLOCK_SELECT((val), 13, 12, DCKCFGR2_REG)
#define USART8_SEL(val)         STM32_DT_CLOCK_SELECT((val), 15, 14, DCKCFGR2_REG)
#define I2C1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 17, 16, DCKCFGR2_REG)
#define I2C2_SEL(val)           STM32_DT_CLOCK_SELECT((val), 19, 18, DCKCFGR2_REG)
#define I2C3_SEL(val)           STM32_DT_CLOCK_SELECT((val), 21, 20, DCKCFGR2_REG)
#define I2C4_SEL(val)           STM32_DT_CLOCK_SELECT((val), 23, 22, DCKCFGR2_REG)
#define LPTIM1_SEL(val)         STM32_DT_CLOCK_SELECT((val), 25, 24, DCKCFGR2_REG)
#define CEC_SEL(val)            STM32_DT_CLOCK_SELECT((val), 26, 26, DCKCFGR2_REG)
#define CK48M_SEL(val)          STM32_DT_CLOCK_SELECT((val), 27, 27, DCKCFGR2_REG)
#define SDMMC1_SEL(val)         STM32_DT_CLOCK_SELECT((val), 28, 28, DCKCFGR2_REG)
#define SDMMC2_SEL(val)         STM32_DT_CLOCK_SELECT((val), 29, 29, DCKCFGR2_REG)
#define DSI_SEL(val)            STM32_DT_CLOCK_SELECT((val), 30, 30, DCKCFGR2_REG)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F7_CLOCK_H_ */
```

## 41.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 STMicroelectronics。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 33 行

参考手册 RM0386、RM0390、RM0402、RM0430 中的专用时钟配置寄存器（Dedicated Clock Configuration Register，`RCC_DCKCFGRx`）章节。

### 注释 3：原第 36 行

在 `stm32_common_clocks.h` 中定义。

### 注释 4：原第 39 行

低速时钟定义在 `stm32_common_clocks.h` 中。

### 注释 5：原第 51 行

PLLSAI 时钟输出（Clock Outputs）。

### 注释 6：原第 76 行

微控制器时钟输出（MCO）预分频器：分频因子。

### 注释 7：原第 125 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F7_CLOCK_H_`。

## 41.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P430_zephyr__dt-bindings__clock__stm32f7_clock.h_文件参考.md)
- [zephyr/dt-bindings/clock/stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)
- [stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)

---

[上一章](P040_stm32f3_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P042_stm32g4_clock.h_源码浏览.md)
