---
id: learning.zephyr-docs.api-source-supplement-reference.page-162
title: renesas_rza2m_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas__rza2m__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第162章\_renesas\_rza2m\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rza2m__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rza2m__clock_8h.html)。

## 162.1\_原始可见代码（Source Code）

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
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
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
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
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
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
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
<a id="foldopen00071"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>

```c
/*
 * Copyright (c) 2025 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RENESAS_RZA2M_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RENESAS_RZA2M_CLOCK_H_

#define RZA2M_MODULE_CORESIGHT 1UL
#define RZA2M_MODULE_OSTM0     2UL
#define RZA2M_MODULE_OSTM1     3UL
#define RZA2M_MODULE_OSTM2     4UL
#define RZA2M_MODULE_MTU3      5UL
#define RZA2M_MODULE_CANFD     6UL
#define RZA2M_MODULE_ADC       7UL
#define RZA2M_MODULE_GPT       8UL
#define RZA2M_MODULE_SCIFA0    9UL
#define RZA2M_MODULE_SCIFA1    10UL
#define RZA2M_MODULE_SCIFA2    11UL
#define RZA2M_MODULE_SCIFA3    12UL
#define RZA2M_MODULE_SCIFA4    13UL
#define RZA2M_MODULE_SCI0      14UL
#define RZA2M_MODULE_SCI1      15UL
#define RZA2M_MODULE_IrDA      16UL
#define RZA2M_MODULE_CEU       17UL
#define RZA2M_MODULE_RTC0      18UL
#define RZA2M_MODULE_RTC1      19UL
#define RZA2M_MODULE_JCU       20UL
#define RZA2M_MODULE_VIN       21UL
#define RZA2M_MODULE_ETHER     22UL
#define RZA2M_MODULE_USB0      23UL
#define RZA2M_MODULE_USB1      24UL
#define RZA2M_MODULE_IMR2      25UL
#define RZA2M_MODULE_DRW       26UL
#define RZA2M_MODULE_MIPI      27UL
#define RZA2M_MODULE_SSIF0     28UL
#define RZA2M_MODULE_SSIF1     29UL
#define RZA2M_MODULE_SSIF2     30UL
#define RZA2M_MODULE_SSIF3     31UL
#define RZA2M_MODULE_I2C0      32UL
#define RZA2M_MODULE_I2C1      33UL
#define RZA2M_MODULE_I2C2      34UL
#define RZA2M_MODULE_I2C3      35UL
#define RZA2M_MODULE_SPIBSC    36UL
#define RZA2M_MODULE_VDC6      37UL
#define RZA2M_MODULE_RSPI0     38UL
#define RZA2M_MODULE_RSPI1     39UL
#define RZA2M_MODULE_RSPI2     40UL
#define RZA2M_MODULE_HYPERBUS  41UL
#define RZA2M_MODULE_OCTAMEM   42UL
#define RZA2M_MODULE_RSPDIF    43UL
#define RZA2M_MODULE_DRP       44UL
#define RZA2M_MODULE_TSIP      45UL
#define RZA2M_MODULE_NAND      46UL
#define RZA2M_MODULE_SDMMC0    47UL
#define RZA2M_MODULE_SDMMC1    48UL

#define RZA2M_MODULE_SHIFT    8UL
#define RZA2M_CLOCK_SRC_SHIFT 0UL

#define RZA2M_CLK_EXTAL 0UL
#define RZA2M_CLK_I     1UL
#define RZA2M_CLK_G     2UL
#define RZA2M_CLK_B     3UL
#define RZA2M_CLK_P1    4UL
#define RZA2M_CLK_P1C   4UL
#define RZA2M_CLK_P0    5UL

#define RZA2M_CLOCK(module, clk)                                                                   \
        (((module) << RZA2M_MODULE_SHIFT) | ((clk) << RZA2M_CLOCK_SRC_SHIFT))

/*
 * Example: RZA2M_CLOCK(MODULE_SCIFA4, RZA2M_CLK_P1C) // SCIFA4
 */

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RENESAS_RZA2M_CLOCK_H_ */
```

## 162.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 74 行

示例（Example）：`RZA2M_CLOCK(MODULE_SCIFA4, RZA2M_CLK_P1C)`，对应 `SCIFA4`。

### 注释 3：原第 78 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RENESAS_RZA2M_CLOCK_H_`。

## 162.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rza2m__clock_8h.html)

---

[上一章](P161_renesas-rztn-gpio.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P163_rk3588-cru-reset.h_源码浏览.md)
