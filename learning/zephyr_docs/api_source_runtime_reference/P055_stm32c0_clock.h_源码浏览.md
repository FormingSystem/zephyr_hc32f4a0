---
id: learning.zephyr-docs.api-source-runtime-reference.page-55
title: stm32c0_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32c0__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第55章\_stm32c0\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32c0__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/stm32c0__clock_8h.html)。

## 55.1\_原始可见代码（Source Code）

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
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00026"></a>
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
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00060"></a>
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
<a id="astm32__common__clocks_8h_html"></a>

```c
/*
 * Copyright (c) 2023 Benjamin Björnsson <benjamin.bjornsson@gmail.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32C0_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32C0_CLOCK_H_

#include <zephyr/dt-bindings/clock/stm32_common_clocks.h>


#define STM32_CLOCK_BUS_IOP     0x034
#define STM32_CLOCK_BUS_AHB1    0x038
#define STM32_CLOCK_BUS_APB1    0x03c
#define STM32_CLOCK_BUS_APB1_2  0x040

#define STM32_PERIPH_BUS_MIN    STM32_CLOCK_BUS_IOP
#define STM32_PERIPH_BUS_MAX    STM32_CLOCK_BUS_APB1_2

/* RM0490, §5.4.21/22 Clock configuration register (RCC_CCIPRx) */

/* defined in stm32_common_clocks.h */
/* Low speed clocks defined in stm32_common_clocks.h
 * STM32_SRC_HSI relates to HSI48 clock mentioned in RM0490 Reference Manual
 * STM32_SRC_HSI48 relates to HSIUSB48 mentioned in RM0490 Reference Manual
 */
#define STM32_SRC_HSI           (STM32_SRC_LSI + 1)
#define STM32_SRC_HSI48         (STM32_SRC_HSI + 1)
#define STM32_SRC_HSE           (STM32_SRC_HSI48 + 1)
#define STM32_SRC_PCLK          (STM32_SRC_HSE + 1)
#define STM32_SRC_TIMPCLK1      (STM32_SRC_PCLK + 1)

#define CCIPR_REG               0x54
#define CCIPR2_REG              0x58

#define CSR1_REG                0x5C

#define CFGR1_REG               0x08

#define USART1_SEL(val)         STM32_DT_CLOCK_SELECT((val), 1, 0, CCIPR_REG)
#define FDCAN_SEL(val)          STM32_DT_CLOCK_SELECT((val), 9, 8, CCIPR_REG)
#define I2C1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 13, 12, CCIPR_REG)
#define I2C2_I2S1_SEL(val)      STM32_DT_CLOCK_SELECT((val), 15, 14, CCIPR_REG)
#define ADC_SEL(val)            STM32_DT_CLOCK_SELECT((val), 31, 30, CCIPR_REG)
#define USB_SEL(val)            STM32_DT_CLOCK_SELECT((val), 12, 12, CCIPR2_REG)
#define RTC_SEL(val)            STM32_DT_CLOCK_SELECT((val), 9, 8, CSR1_REG)

#define MCO2_SEL(val)           STM32_DT_CLOCK_SELECT((val), 19, 16, CFGR1_REG)
#define MCO2_PRE(val)           STM32_DT_CLOCK_SELECT((val), 23, 20, CFGR1_REG)
#define MCO1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 27, 24, CFGR1_REG)
#define MCO1_PRE(val)           STM32_DT_CLOCK_SELECT((val), 31, 28, CFGR1_REG)

/* MCO prescaler : division factor */
#define MCO_PRE_DIV_1   0
#define MCO_PRE_DIV_2   1
#define MCO_PRE_DIV_4   2
#define MCO_PRE_DIV_8   3
#define MCO_PRE_DIV_16  4
#define MCO_PRE_DIV_32  5
#define MCO_PRE_DIV_64  6
#define MCO_PRE_DIV_128 7


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32C0_CLOCK_H_ */
```

## 55.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Benjamin Björnsson <benjamin.bjornsson@gmail.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 23 行

`RM0490` 第 5.4.21/22 节：时钟配置寄存器（Clock configuration register，`RCC_CCIPRx`）。

### 注释 3：原第 26 行

在 `stm32_common_clocks.h` 中定义。

### 注释 4：原第 28 行

低速时钟定义在 `stm32_common_clocks.h` 中。`STM32_SRC_HSI` 对应 `RM0490` 参考手册中的 HSI48 时钟；`STM32_SRC_HSI48` 对应该手册中的 HSIUSB48。

### 注释 5：原第 67 行

微控制器时钟输出（MCO）预分频器：分频因子。

### 注释 6：原第 79 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32C0_CLOCK_H_`。

## 55.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/stm32c0__clock_8h.html)
- [zephyr/dt-bindings/clock/stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)
- [stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)

---

[上一章](P054_socket_net_mgmt.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P056_stm32g0_clock.h_源码浏览.md)
