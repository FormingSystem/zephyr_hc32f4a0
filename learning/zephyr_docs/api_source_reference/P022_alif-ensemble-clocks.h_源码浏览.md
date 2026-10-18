---
id: learning.zephyr-docs.api-source-reference.page-22
title: alif-ensemble-clocks.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/alif-ensemble-clocks_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_alif-ensemble-clocks.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/alif-ensemble-clocks_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/alif-ensemble-clocks_8h.html)。

## 22.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00024"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00046"></a>
<a id="foldopen00048"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="foldopen00051"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="foldopen00054"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="foldopen00057"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="foldopen00060"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="foldopen00063"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="foldopen00066"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="foldopen00069"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00078"></a>
<a id="foldopen00080"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="foldopen00083"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="foldopen00086"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="foldopen00089"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00102"></a>
<a id="foldopen00104"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="foldopen00107"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="foldopen00110"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="foldopen00113"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="foldopen00116"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="foldopen00119"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="foldopen00122"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="foldopen00125"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="aalif-clocks-common_8h_html"></a>

```c
/*
 * Copyright (c) 2025 Alif Semiconductor
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_ALIF_ENSEMBLE_CLOCKS_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_ALIF_ENSEMBLE_CLOCKS_H_


#include "alif-clocks-common.h"


#define ALIF_UART_CTRL_REG              0x08U

#define ALIF_I2C0_CTRL_REG              0x50U
#define ALIF_I2C1_CTRL_REG              0x54U
#define ALIF_I2C2_CTRL_REG              0x58U
#define ALIF_I2C3_CTRL_REG              0x5CU

#define ALIF_TIMER_CLKSEL_REG           0x04U



#define ALIF_UART0_SYST_PCLK        \
        ALIF_CLK_CFG(CLKCTL_PER_SLV, UART_CTRL, 0U, 1U, 1U, 1U, 8U, ALIF_PARENT_CLK_SYST_PCLK)

#define ALIF_UART1_SYST_PCLK        \
        ALIF_CLK_CFG(CLKCTL_PER_SLV, UART_CTRL, 1U, 1U, 1U, 1U, 9U, ALIF_PARENT_CLK_SYST_PCLK)

#define ALIF_UART2_SYST_PCLK        \
        ALIF_CLK_CFG(CLKCTL_PER_SLV, UART_CTRL, 2U, 1U, 1U, 1U, 10U, ALIF_PARENT_CLK_SYST_PCLK)

#define ALIF_UART3_SYST_PCLK        \
        ALIF_CLK_CFG(CLKCTL_PER_SLV, UART_CTRL, 3U, 1U, 1U, 1U, 11U, ALIF_PARENT_CLK_SYST_PCLK)

#define ALIF_UART4_SYST_PCLK        \
        ALIF_CLK_CFG(CLKCTL_PER_SLV, UART_CTRL, 4U, 1U, 1U, 1U, 12U, ALIF_PARENT_CLK_SYST_PCLK)

#define ALIF_UART5_SYST_PCLK        \
        ALIF_CLK_CFG(CLKCTL_PER_SLV, UART_CTRL, 5U, 1U, 1U, 1U, 13U, ALIF_PARENT_CLK_SYST_PCLK)

#define ALIF_UART6_SYST_PCLK        \
        ALIF_CLK_CFG(CLKCTL_PER_SLV, UART_CTRL, 6U, 1U, 1U, 1U, 14U, ALIF_PARENT_CLK_SYST_PCLK)

#define ALIF_UART7_SYST_PCLK        \
        ALIF_CLK_CFG(CLKCTL_PER_SLV, UART_CTRL, 7U, 1U, 1U, 1U, 15U, ALIF_PARENT_CLK_SYST_PCLK)



#define ALIF_I2C0_SYST_PCLK         \
        ALIF_CLK_CFG(CLKCTL_PER_SLV, I2C0_CTRL, 0U, 1U, 0U, 0U, 0U, ALIF_PARENT_CLK_SYST_PCLK)

#define ALIF_I2C1_SYST_PCLK         \
        ALIF_CLK_CFG(CLKCTL_PER_SLV, I2C1_CTRL, 0U, 1U, 0U, 0U, 0U, ALIF_PARENT_CLK_SYST_PCLK)

#define ALIF_I2C2_SYST_PCLK         \
        ALIF_CLK_CFG(CLKCTL_PER_SLV, I2C2_CTRL, 0U, 1U, 0U, 0U, 0U, ALIF_PARENT_CLK_SYST_PCLK)

#define ALIF_I2C3_SYST_PCLK         \
        ALIF_CLK_CFG(CLKCTL_PER_SLV, I2C3_CTRL, 0U, 1U, 0U, 0U, 0U, ALIF_PARENT_CLK_SYST_PCLK)



#define ALIF_LPTIMER0_S32K_CLK      \
        ALIF_CLK_CFG(VBAT, TIMER_CLKSEL, 0U, 0U, 0U, 2U, 0U, ALIF_PARENT_CLK_S32K)

#define ALIF_LPTIMER0_128K_CLK      \
        ALIF_CLK_CFG(VBAT, TIMER_CLKSEL, 0U, 0U, 1U, 2U, 0U, ALIF_PARENT_CLK_128K)

#define ALIF_LPTIMER1_S32K_CLK      \
        ALIF_CLK_CFG(VBAT, TIMER_CLKSEL, 0U, 0U, 0U, 2U, 4U, ALIF_PARENT_CLK_S32K)

#define ALIF_LPTIMER1_128K_CLK      \
        ALIF_CLK_CFG(VBAT, TIMER_CLKSEL, 0U, 0U, 1U, 2U, 4U, ALIF_PARENT_CLK_128K)

#define ALIF_LPTIMER2_S32K_CLK      \
        ALIF_CLK_CFG(VBAT, TIMER_CLKSEL, 0U, 0U, 0U, 2U, 8U, ALIF_PARENT_CLK_S32K)

#define ALIF_LPTIMER2_128K_CLK      \
        ALIF_CLK_CFG(VBAT, TIMER_CLKSEL, 0U, 0U, 1U, 2U, 8U, ALIF_PARENT_CLK_128K)

#define ALIF_LPTIMER3_S32K_CLK      \
        ALIF_CLK_CFG(VBAT, TIMER_CLKSEL, 0U, 0U, 0U, 2U, 12U, ALIF_PARENT_CLK_S32K)

#define ALIF_LPTIMER3_128K_CLK      \
        ALIF_CLK_CFG(VBAT, TIMER_CLKSEL, 0U, 0U, 1U, 2U, 12U, ALIF_PARENT_CLK_128K)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_ALIF_ENSEMBLE_CLOCKS_H_ */
```

## 22.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Alif Semiconductor。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 130 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_ALIF_ENSEMBLE_CLOCKS_H_`。

## 22.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/alif-ensemble-clocks_8h.html)
- [alif-clocks-common.h](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html)

---

[上一章](P021_alif-clocks-common.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P023_alif-ensemble-e1c-pinctrl.h_源码浏览.md)
