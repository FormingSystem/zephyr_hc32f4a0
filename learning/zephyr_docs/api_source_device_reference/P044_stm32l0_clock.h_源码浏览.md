---
id: learning.zephyr-docs.api-source-device-reference.page-44
title: stm32l0_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32l0__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第44章\_stm32l0\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32l0__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P442_zephyr__dt-bindings__clock__stm32l0_clock.h_文件参考.md)。

## 44.1\_原始可见代码（Source Code）

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
<a id="l00011"></a>
<a id="l00013"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00059"></a>
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
<a id="l00082"></a>
<a id="l00083"></a>
<a id="astm32__common__clocks_8h_html"></a>

```c
/*
 * Copyright (c) 2022 Linaro Limited
 * Copyright (c) 2026 Witekio
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32L0_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32L0_CLOCK_H_

#include <zephyr/dt-bindings/clock/stm32_common_clocks.h>


#define STM32_CLOCK_BUS_IOP     0x02c
#define STM32_CLOCK_BUS_AHB1    0x030
#define STM32_CLOCK_BUS_APB2    0x034
#define STM32_CLOCK_BUS_APB1    0x038

#define STM32_PERIPH_BUS_MIN    STM32_CLOCK_BUS_IOP
#define STM32_PERIPH_BUS_MAX    STM32_CLOCK_BUS_APB1

/* RM0367, §7.3.20 Clock configuration register (RCC_CCIPR) */

/* defined in stm32_common_clocks.h */

/* Low speed clocks defined in stm32_common_clocks.h */
#define STM32_SRC_HSE           (STM32_SRC_LSI + 1)
#define STM32_SRC_HSI           (STM32_SRC_HSE + 1)
#define STM32_SRC_HSI48         (STM32_SRC_HSI + 1)
#define STM32_SRC_PCLK          (STM32_SRC_HSI48 + 1)
#define STM32_SRC_TIMPCLK1      (STM32_SRC_PCLK + 1)
#define STM32_SRC_TIMPCLK2      (STM32_SRC_TIMPCLK1 + 1)

#define CFGR_REG               0x0C

#define CCIPR_REG               0x4C

#define CSR_REG         0x50

#define USART1_SEL(val)         STM32_DT_CLOCK_SELECT((val), 1, 0, CCIPR_REG)
#define USART2_SEL(val)         STM32_DT_CLOCK_SELECT((val), 3, 2, CCIPR_REG)
#define LPUART1_SEL(val)        STM32_DT_CLOCK_SELECT((val), 11, 10, CCIPR_REG)
#define I2C1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 13, 12, CCIPR_REG)
#define I2C3_SEL(val)           STM32_DT_CLOCK_SELECT((val), 17, 16, CCIPR_REG)
#define LPTIM1_SEL(val)         STM32_DT_CLOCK_SELECT((val), 19, 18, CCIPR_REG)
#define HSI48_SEL(val)          STM32_DT_CLOCK_SELECT((val), 26, 26, CCIPR_REG)
#define RTC_SEL(val)            STM32_DT_CLOCK_SELECT((val), 17, 16, CSR_REG)

#define MCO1_SEL(val)       STM32_DT_CLOCK_SELECT((val), 27, 24, CFGR_REG)
#define MCO1_PRE(val)       STM32_DT_CLOCK_SELECT((val), 30, 28, CFGR_REG)

/* MCO source clock selector */
#define MCO_SEL_SYSCLK   (1)
#define MCO_SEL_HSI16    (2)
#define MCO_SEL_MSI      (3)
#define MCO_SEL_HSE      (4)
#define MCO_SEL_PLL      (5)
#define MCO_SEL_LSI      (6)
#define MCO_SEL_LSE      (7)
#define MCO_SEL_HSI48    (8)

/* MCO prescaler : division factor */
#define MCO_PRE_DIV_1  (0)
#define MCO_PRE_DIV_2  (1)
#define MCO_PRE_DIV_4  (2)
#define MCO_PRE_DIV_8  (3)
#define MCO_PRE_DIV_16 (4)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32L0_CLOCK_H_ */
```

## 44.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Linaro Limited。

版权（Copyright）：© 2026 Witekio。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 24 行

参考手册 RM0367，第 7.3.20 节：时钟配置寄存器（Clock Configuration Register，`RCC_CCIPR`）。

### 注释 3：原第 27 行

在 `stm32_common_clocks.h` 中定义。

### 注释 4：原第 30 行

低速时钟定义在 `stm32_common_clocks.h` 中。

### 注释 5：原第 64 行

微控制器时钟输出源时钟选择器（MCO Source Clock Selector）。

### 注释 6：原第 74 行

微控制器时钟输出（MCO）预分频器：分频因子。

### 注释 7：原第 83 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32L0_CLOCK_H_`。

## 44.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P442_zephyr__dt-bindings__clock__stm32l0_clock.h_文件参考.md)
- [zephyr/dt-bindings/clock/stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)
- [stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)

---

[上一章](P043_stm32h7rs_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P045_stm32l4_clock.h_源码浏览.md)
