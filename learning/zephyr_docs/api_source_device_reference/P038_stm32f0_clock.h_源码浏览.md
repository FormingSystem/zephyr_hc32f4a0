---
id: learning.zephyr-docs.api-source-device-reference.page-38
title: stm32f0_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32f0__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_stm32f0\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32f0__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P421_zephyr__dt-bindings__clock__stm32f0_clock.h_文件参考.md)。

## 38.1\_原始可见代码（Source Code）

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
<a id="l00023"></a>
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>
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
<a id="l00085"></a>
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
<a id="l00117"></a>
<a id="l00118"></a>
<a id="astm32__common__clocks_8h_html"></a>

```c
/*
 * Copyright (c) 2022 Linaro Limited
 * Copyright (c) 2026 Witekio
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F0_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F0_CLOCK_H_

#include <zephyr/dt-bindings/clock/stm32_common_clocks.h>


#define STM32_CLOCK_BUS_AHB1    0x014
#define STM32_CLOCK_BUS_APB2    0x018
#define STM32_CLOCK_BUS_APB1    0x01c

#define STM32_PERIPH_BUS_MIN    STM32_CLOCK_BUS_AHB1
#define STM32_PERIPH_BUS_MAX    STM32_CLOCK_BUS_APB1


/* defined in stm32_common_clocks.h */
/* Low speed clocks defined in stm32_common_clocks.h */
#define STM32_SRC_HSI           (STM32_SRC_LSI + 1)
#define STM32_SRC_HSI14         (STM32_SRC_HSI + 1)
#define STM32_SRC_HSI48         (STM32_SRC_HSI14 + 1)
#define STM32_SRC_PCLK          (STM32_SRC_HSI48 + 1)
#define STM32_SRC_TIMPCLK1      (STM32_SRC_PCLK + 1)
#define STM32_SRC_PLLCLK        (STM32_SRC_TIMPCLK1 + 1)

#define CFGR1_REG               0x04
#define CFGR3_REG               0x30

#define BDCR_REG                0x20

#define USART1_SEL(val)         STM32_DT_CLOCK_SELECT((val), 1, 0, CFGR3_REG)
#define I2C1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 4, 4, CFGR3_REG)
#define CEC_SEL(val)            STM32_DT_CLOCK_SELECT((val), 6, 6, CFGR3_REG)
#define USB_SEL(val)            STM32_DT_CLOCK_SELECT((val), 7, 7, CFGR3_REG)
#define USART2_SEL(val)         STM32_DT_CLOCK_SELECT((val), 17, 16, CFGR3_REG)
#define USART3_SEL(val)         STM32_DT_CLOCK_SELECT((val), 19, 18, CFGR3_REG)
#define RTC_SEL(val)            STM32_DT_CLOCK_SELECT((val), 9, 8, BDCR_REG)

#define MCO1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 27, 24, CFGR1_REG)
#define MCO1_PRE(val)           STM32_DT_CLOCK_SELECT((val), 30, 28, CFGR1_REG)
#define MCO1_PRE_PLLDIV(pre_val, div_val) \
        STM32_DT_CLOCK_SELECT((div_val << 3) | (pre_val), 31, 28, CFGR1_REG)

/* MCO source clock selector */
#define MCO_SEL_HSI14  (1)
#define MCO_SEL_LSI    (2)
#define MCO_SEL_LSE    (3)
#define MCO_SEL_SYSCLK (4)
#define MCO_SEL_HSI    (5)
#define MCO_SEL_HSE    (6)
#define MCO_SEL_PLL    (7)              /* PLL/2 or PLL, see below */
#define MCO_SEL_HSI48  (8)

/* MCO prescaler : division factor */
#define MCO_PRE_DIV_1   (0)
#define MCO_PRE_DIV_2   (1)
#define MCO_PRE_DIV_4   (2)
#define MCO_PRE_DIV_8   (3)
#define MCO_PRE_DIV_16  (4)
#define MCO_PRE_DIV_32  (5)
#define MCO_PRE_DIV_64  (6)
#define MCO_PRE_DIV_128 (7)

/*
 * MCO PLL source divider
 *
 * By default, the MCO_SEL_PLL source goes through a divide-by-2
 * prescaler and outputs "PLL / 2". It is possible to output the
 * undivided PLL clock by disabling the prescaler on some SoCs
 * by using MCO_PLL_DIV_1.
 *
 * Refer to RM00091 Rev 10 §6.2.12 (or RM0360 Rev 5 §7.2.11) to
 * determine if disabling the prescaler is possible on your SoC.
 *
 * Here is an example of how to declare the PLL as source with no division using
 * the MCO1_PRE_PLLDIV macro:
 *              &clk_hsi {
 *                      status = "okay";
 *              };
 *
 *              &pll {
 *                      clocks = <&clk_hsi>;
 *                      prediv = <1>;
 *                      mul = <2>;
 *                      status = "okay";
 *              };
 *
 *              &mco1 {
 *                      clocks = <&rcc STM32_SRC_PLLCLK (MCO1_SEL(MCO_SEL_PLL))>;
 *                      prescaler = <MCO1_PRE_PLLDIV(MCO_PRE_DIV_128, MCO_PLL_DIV_1)>;
 *                      pinctrl-0 = <&rcc_mco_pa8>;
 *                      pinctrl-names = "default";
 *                      status = "okay";
 *              };
 */
#define MCO_PLL_DIV_2   (0)             /* default value */
#define MCO_PLL_DIV_1   (1)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F0_CLOCK_H_ */
```

## 38.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Linaro Limited。

版权（Copyright）：© 2026 Witekio。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 25 行

在 `stm32_common_clocks.h` 中定义。

### 注释 3：原第 27 行

低速时钟定义在 `stm32_common_clocks.h` 中。

### 注释 4：原第 61 行

微控制器时钟输出源时钟选择器（MCO Source Clock Selector）。

### 注释 5：原第 68 行

锁相环时钟（PLL）二分频，即 `PLL/2`，或不分频的 PLL；见下文。

### 注释 6：原第 71 行

微控制器时钟输出（MCO）预分频器：分频因子。

### 注释 7：原第 81 行

微控制器时钟输出的锁相环源分频器（MCO PLL Source Divider）。

默认情况下，`MCO_SEL_PLL` 时钟源经过二分频预分频器（Divide-by-2 Prescaler），输出 `PLL / 2`。某些片上系统（SoCs）可以使用 `MCO_PLL_DIV_1` 禁用该预分频器，输出不分频的 PLL 时钟。

参见 RM00091 修订版 10 第 6.2.12 节，或 RM0360 修订版 5 第 7.2.11 节，确认所用 SoC 是否允许禁用预分频器。

以下示例使用 `MCO1_PRE_PLLDIV` 宏，将 PLL 声明为不分频的时钟源：

```c
&clk_hsi {
status = "okay";
};

&pll {
clocks = <&clk_hsi>;
prediv = <1>;
mul = <2>;
status = "okay";
};

&mco1 {
clocks = <&rcc STM32_SRC_PLLCLK (MCO1_SEL(MCO_SEL_PLL))>;
prescaler = <MCO1_PRE_PLLDIV(MCO_PRE_DIV_128, MCO_PLL_DIV_1)>;
pinctrl-0 = <&rcc_mco_pa8>;
pinctrl-names = "default";
status = "okay";
};
```

### 注释 8：原第 113 行

默认值（Default Value）。

### 注释 9：原第 118 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F0_CLOCK_H_`。

## 38.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P421_zephyr__dt-bindings__clock__stm32f0_clock.h_文件参考.md)
- [zephyr/dt-bindings/clock/stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)
- [stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)

---

[上一章](P037_stm32c5_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P039_stm32f1_clock.h_源码浏览.md)
