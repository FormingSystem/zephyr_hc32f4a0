---
id: learning.zephyr-docs.api-source-reference.page-456
title: lpc84x-clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lpc84x-clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第456章\_lpc84x-clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/lpc84x-clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/lpc84x-clock_8h.html)。

## 456.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>

```c
/*
 * Copyright (c) 2026 Aerlync Labs Inc
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_LPC84X_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_LPC84X_CLOCK_H_

#define LPC84X_SYS_AHB_CLK_CTRL0 0U

#define LPC84X_SYS_AHB_CLK_CTRL1 4U

#define LPC84X_CLK_GATE_DEFINE(reg, bit) ((((reg) & 0xFFU) << 8U) | ((bit) & 0xFFU))

#define LPC84X_CLK_ROM LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 1U)

#define LPC84X_CLK_RAM0_1 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 2U)

#define LPC84X_CLK_FLASH LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 4U)

#define LPC84X_CLK_I2C0 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 5U)

#define LPC84X_CLK_GPIO0 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 6U)

#define LPC84X_CLK_SWM LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 7U)

#define LPC84X_CLK_SCT LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 8U)

#define LPC84X_CLK_WKT LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 9U)

#define LPC84X_CLK_MRT LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 10U)

#define LPC84X_CLK_SPI0 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 11U)

#define LPC84X_CLK_SPI1 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 12U)

#define LPC84X_CLK_CRC LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 13U)

#define LPC84X_CLK_UART0 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 14U)

#define LPC84X_CLK_UART1 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 15U)

#define LPC84X_CLK_UART2 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 16U)

#define LPC84X_CLK_WWDT LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 17U)

#define LPC84X_CLK_IOCON LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 18U)

#define LPC84X_CLK_ACMP LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 19U)

#define LPC84X_CLK_GPIO1 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 20U)

#define LPC84X_CLK_I2C1 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 21U)

#define LPC84X_CLK_I2C2 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 22U)

#define LPC84X_CLK_I2C3 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 23U)

#define LPC84X_CLK_ADC LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 24U)

#define LPC84X_CLK_CTIMER0 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 25U)

#define LPC84X_CLK_MTB LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 26U)

#define LPC84X_CLK_DAC0 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 27U)

#define LPC84X_CLK_GPIOINT LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 28U)

#define LPC84X_CLK_DMA LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 29U)

#define LPC84X_CLK_UART3 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 30U)

#define LPC84X_CLK_UART4 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 31U)

#define LPC84X_CLK_CAPT LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL1, 0U)

#define LPC84X_CLK_DAC1 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL1, 1U)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_LPC84X_CLOCK_H_ */
```

## 456.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Aerlync Labs Inc。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 129 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_LPC84X_CLOCK_H_`。

## 456.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/lpc84x-clock_8h.html)

---

[上一章](P455_lpc11u6x_clock_control.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P457_lps22hh.h_源码浏览.md)
