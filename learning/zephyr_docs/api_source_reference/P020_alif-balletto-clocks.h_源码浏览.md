---
id: learning.zephyr-docs.api-source-reference.page-20
title: alif-balletto-clocks.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/alif-balletto-clocks_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_alif-balletto-clocks.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/alif-balletto-clocks_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/alif-balletto-clocks_8h.html)。

## 20.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00023"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00042"></a>
<a id="foldopen00044"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="foldopen00047"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="foldopen00050"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="foldopen00053"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="foldopen00056"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="foldopen00059"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00068"></a>
<a id="foldopen00070"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="foldopen00073"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00086"></a>
<a id="foldopen00088"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="foldopen00091"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="foldopen00094"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="foldopen00097"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="aalif-clocks-common_8h_html"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright Alif Semiconductor
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_ALIF_BALLETTO_CLOCKS_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_ALIF_BALLETTO_CLOCKS_H_


#include "alif-clocks-common.h"


#define ALIF_UART_CTRL_REG              0x08U

#define ALIF_I2C0_CTRL_REG              0x50U

#define ALIF_I2C1_CTRL_REG              0x54U

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



#define ALIF_I2C0_SYST_PCLK         \
        ALIF_CLK_CFG(CLKCTL_PER_SLV, I2C0_CTRL, 0U, 1U, 0U, 0U, 0U, ALIF_PARENT_CLK_SYST_PCLK)

#define ALIF_I2C1_SYST_PCLK         \
        ALIF_CLK_CFG(CLKCTL_PER_SLV, I2C1_CTRL, 0U, 1U, 0U, 0U, 0U, ALIF_PARENT_CLK_SYST_PCLK)



#define ALIF_LPTIMER0_S32K_CLK      \
        ALIF_CLK_CFG(VBAT, TIMER_CLKSEL, 0U, 0U, 0U, 2U, 0U, ALIF_PARENT_CLK_S32K)

#define ALIF_LPTIMER0_128K_CLK      \
        ALIF_CLK_CFG(VBAT, TIMER_CLKSEL, 0U, 0U, 1U, 2U, 0U, ALIF_PARENT_CLK_128K)

#define ALIF_LPTIMER1_S32K_CLK      \
        ALIF_CLK_CFG(VBAT, TIMER_CLKSEL, 0U, 0U, 0U, 2U, 4U, ALIF_PARENT_CLK_S32K)

#define ALIF_LPTIMER1_128K_CLK      \
        ALIF_CLK_CFG(VBAT, TIMER_CLKSEL, 0U, 0U, 1U, 2U, 4U, ALIF_PARENT_CLK_128K)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_ALIF_BALLETTO_CLOCKS_H_ */
```

## 20.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright Alif Semiconductor。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 102 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_ALIF_BALLETTO_CLOCKS_H_`。

## 20.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/alif-balletto-clocks_8h.html)
- [alif-clocks-common.h](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html)

---

[上一章](P019_alif-balletto-b1-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P021_alif-clocks-common.h_源码浏览.md)
