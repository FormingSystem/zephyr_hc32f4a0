---
id: learning.zephyr-docs.api-source-reference.page-864
title: ti-dmtimer.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ti-dmtimer_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第864章\_ti-dmtimer.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ti-dmtimer_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ti-dmtimer_8h.html)。

## 864.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00018"></a>
<a id="l00020"></a>
<a id="l00022"></a>
<a id="l00024"></a>
<a id="l00026"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>

```c
/*
 * Copyright (c) 2026 Texas Instruments
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_TIMER_TI_DMTIMER_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_TIMER_TI_DMTIMER_H_


#define HFOSC0_CLKOUT           0x0
#define HFOSC0_CLKOUT_32K       0x1
#define MAIN_PLL0_HSDIV7_CLKOUT 0x2
#define CLK_12M_RC              0x3
#define MCU_EXT_REFCLK0         0x4
#define EXT_REFCLK1             0x5
#define CPTS_RFT_CLK            0x6
#define CPSW3G_CPTS_RFT_CLK     0x7
#define MAIN_PLL1_HSDIV3_CLKOUT 0x8
#define MAIN_PLL2_HSDIV6_CLKOUT 0x9
#define CPSW3G_CPTS_GENF0       0xA
#define CPSW3G_CPTS_GENF1       0xB
#define CPTS_GENF1              0xC
#define CPTS_GENF2              0xD
#define CPTS_GENF3              0xE
#define CPTS_GENF4              0xF


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_TIMER_TI_DMTIMER_H_ */
```

## 864.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Texas Instruments。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 54 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_TIMER_TI_DMTIMER_H_`。

## 864.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ti-dmtimer_8h.html)

---

[上一章](P863_ti-cc13xx-cc26xx-gpio.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P865_ti-vim.h_源码浏览.md)
