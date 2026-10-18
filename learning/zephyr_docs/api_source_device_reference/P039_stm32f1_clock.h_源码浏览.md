---
id: learning.zephyr-docs.api-source-device-reference.page-39
title: stm32f1_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32f1__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_stm32f1\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32f1__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P423_zephyr__dt-bindings__clock__stm32f1_clock.h_文件参考.md)。

## 39.1\_原始可见代码（Source Code）

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
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
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
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="astm32__common__clocks_8h_html"></a>

```c
/*
 * Copyright (c) 2022 Linaro Limited
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F1_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F1_CLOCK_H_

#include <zephyr/dt-bindings/clock/stm32_common_clocks.h>



#define STM32_CLOCK_BUS_AHB1    0x014
#define STM32_CLOCK_BUS_APB2    0x018
#define STM32_CLOCK_BUS_APB1    0x01c

#define STM32_PERIPH_BUS_MIN    STM32_CLOCK_BUS_AHB1
#define STM32_PERIPH_BUS_MAX    STM32_CLOCK_BUS_APB1

/* defined in stm32_common_clocks.h */

/* Low speed clocks defined in stm32_common_clocks.h */
#define STM32_SRC_HSI           (STM32_SRC_LSI + 1)
#define STM32_SRC_HSE           (STM32_SRC_HSI + 1)
#define STM32_SRC_EXT_HSE       (STM32_SRC_HSE + 1)
#define STM32_SRC_PLLCLK        (STM32_SRC_EXT_HSE + 1)
#define STM32_SRC_TIMPCLK1      (STM32_SRC_PLLCLK + 1)
#define STM32_SRC_TIMPCLK2      (STM32_SRC_TIMPCLK1 + 1)

#define CFGR1_REG               0x04
#define CFGR2_REG               0x2C

#define BDCR_REG                0x20

#define ADC_PRE(val)            STM32_DT_CLOCK_SELECT((val), 15, 14, CFGR1_REG)
#define I2S2_SEL(val)           STM32_DT_CLOCK_SELECT((val), 17, 17, CFGR2_REG)
#define I2S3_SEL(val)           STM32_DT_CLOCK_SELECT((val), 18, 18, CFGR2_REG)
#define RTC_SEL(val)            STM32_DT_CLOCK_SELECT((val), 9, 8, BDCR_REG)

#define MCO1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 26, 24, CFGR1_REG)
/* No MCO prescaler support on STM32F1 series. */

/* ADC prescaler division factor */
#define ADC_PRE_DIV_2           0
#define ADC_PRE_DIV_4           1
#define ADC_PRE_DIV_6           2
#define ADC_PRE_DIV_8           3


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F1_CLOCK_H_ */
```

## 39.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Linaro Limited。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 24 行

在 `stm32_common_clocks.h` 中定义。

### 注释 3：原第 27 行

低速时钟定义在 `stm32_common_clocks.h` 中。

### 注释 4：原第 53 行

STM32F1 系列不支持微控制器时钟输出预分频器（MCO Prescaler）。

### 注释 5：原第 55 行

模数转换器预分频系数（ADC Prescaler Division Factor）。

### 注释 6：原第 63 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F1_CLOCK_H_`。

## 39.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P423_zephyr__dt-bindings__clock__stm32f1_clock.h_文件参考.md)
- [zephyr/dt-bindings/clock/stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)
- [stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)

---

[上一章](P038_stm32f0_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P040_stm32f3_clock.h_源码浏览.md)
