---
id: learning.zephyr-docs.api-source-reference.page-625
title: nxp_s32k148_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nxp__s32k148__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第625章\_nxp\_s32k148\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/nxp__s32k148__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/nxp__s32k148__clock_8h.html)。

## 625.1\_原始可见代码（Source Code）

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

```c
/*
 * Copyright 2023 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_NXP_S32K148_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_NXP_S32K148_CLOCK_H_

#define NXP_S32_LPO_128K_CLK                       1U
#define NXP_S32_SIRC_CLK                           2U
#define NXP_S32_SIRC_VLP_CLK                       3U
#define NXP_S32_SIRC_STOP_CLK                      4U
#define NXP_S32_FIRC_CLK                           5U
#define NXP_S32_FIRC_VLP_CLK                       6U
#define NXP_S32_FIRC_STOP_CLK                      7U
#define NXP_S32_SOSC_CLK                           8U
#define NXP_S32_SPLL_CLK                           9U
#define NXP_S32_SIRCDIV1_CLK                       10U
#define NXP_S32_SIRCDIV2_CLK                       11U
#define NXP_S32_FIRCDIV1_CLK                       12U
#define NXP_S32_FIRCDIV2_CLK                       13U
#define NXP_S32_SOSCDIV1_CLK                       14U
#define NXP_S32_SOSCDIV2_CLK                       15U
#define NXP_S32_SPLLDIV1_CLK                       16U
#define NXP_S32_SPLLDIV2_CLK                       17U
#define NXP_S32_LPO_32K_CLK                        18U
#define NXP_S32_LPO_1K_CLK                         19U
#define NXP_S32_TCLK0_REF_CLK                      20U
#define NXP_S32_TCLK1_REF_CLK                      21U
#define NXP_S32_TCLK2_REF_CLK                      22U
#define NXP_S32_SCS_CLK                            24U
#define NXP_S32_SCS_RUN_CLK                        25U
#define NXP_S32_SCS_VLPR_CLK                       26U
#define NXP_S32_SCS_HSRUN_CLK                      27U
#define NXP_S32_CORE_CLK                           28U
#define NXP_S32_CORE_RUN_CLK                       29U
#define NXP_S32_CORE_VLPR_CLK                      30U
#define NXP_S32_CORE_HSRUN_CLK                     31U
#define NXP_S32_BUS_CLK                            32U
#define NXP_S32_BUS_RUN_CLK                        33U
#define NXP_S32_BUS_VLPR_CLK                       34U
#define NXP_S32_BUS_HSRUN_CLK                      35U
#define NXP_S32_SLOW_CLK                           36U
#define NXP_S32_SLOW_RUN_CLK                       37U
#define NXP_S32_SLOW_VLPR_CLK                      38U
#define NXP_S32_SLOW_HSRUN_CLK                     39U
#define NXP_S32_RTC_CLK                            40U
#define NXP_S32_LPO_CLK                            41U
#define NXP_S32_SCG_CLKOUT_CLK                     42U
#define NXP_S32_FTM0_EXT_CLK                       43U
#define NXP_S32_FTM1_EXT_CLK                       44U
#define NXP_S32_FTM2_EXT_CLK                       45U
#define NXP_S32_FTM3_EXT_CLK                       46U
#define NXP_S32_FTM4_EXT_CLK                       47U
#define NXP_S32_FTM5_EXT_CLK                       48U
#define NXP_S32_ADC0_CLK                           50U
#define NXP_S32_ADC1_CLK                           51U
#define NXP_S32_CLKOUT0_CLK                        52U
#define NXP_S32_CMP0_CLK                           53U
#define NXP_S32_CRC0_CLK                           54U
#define NXP_S32_DMA0_CLK                           55U
#define NXP_S32_DMAMUX0_CLK                        56U
#define NXP_S32_EIM0_CLK                           57U
#define NXP_S32_ENET_CLK                           58U
#define NXP_S32_ERM0_CLK                           59U
#define NXP_S32_EWM0_CLK                           60U
#define NXP_S32_FLEXCAN0_CLK                       61U
#define NXP_S32_FLEXCAN1_CLK                       62U
#define NXP_S32_FLEXCAN2_CLK                       63U
#define NXP_S32_FLEXIO_CLK                         64U
#define NXP_S32_FTFC_CLK                           65U
#define NXP_S32_FTM0_CLK                           66U
#define NXP_S32_FTM1_CLK                           67U
#define NXP_S32_FTM2_CLK                           68U
#define NXP_S32_FTM3_CLK                           69U
#define NXP_S32_FTM4_CLK                           70U
#define NXP_S32_FTM5_CLK                           71U
#define NXP_S32_LPI2C0_CLK                         72U
#define NXP_S32_LPIT0_CLK                          73U
#define NXP_S32_LPSPI0_CLK                         74U
#define NXP_S32_LPSPI1_CLK                         75U
#define NXP_S32_LPSPI2_CLK                         76U
#define NXP_S32_LPTMR0_CLK                         77U
#define NXP_S32_LPUART0_CLK                        78U
#define NXP_S32_LPUART1_CLK                        79U
#define NXP_S32_LPUART2_CLK                        80U
#define NXP_S32_MPU0_CLK                           81U
#define NXP_S32_MSCM0_CLK                          82U
#define NXP_S32_PDB0_CLK                           83U
#define NXP_S32_PDB1_CLK                           84U
#define NXP_S32_PORTA_CLK                          85U
#define NXP_S32_PORTB_CLK                          86U
#define NXP_S32_PORTC_CLK                          87U
#define NXP_S32_PORTD_CLK                          88U
#define NXP_S32_PORTE_CLK                          89U
#define NXP_S32_RTC0_CLK                           90U
#define NXP_S32_TRACE_CLK                          91U

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_NXP_S32K148_CLOCK_H_ */
```

## 625.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2023 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 100 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_NXP_S32K148_CLOCK_H_`。

## 625.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/nxp__s32k148__clock_8h.html)

---

[上一章](P624_nxp_s32k146_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P626_nxp_s32k344_clock.h_源码浏览.md)
