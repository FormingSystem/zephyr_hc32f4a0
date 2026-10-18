---
id: learning.zephyr-docs.api-source-architecture-reference.page-16
title: nxp_mc_cgm.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nxp__mc__cgm_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_nxp\_mc\_cgm.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/nxp__mc__cgm_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/nxp__mc__cgm_8h.html)。

## 16.1\_原始可见代码（Source Code）

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
<a id="l00066"></a>
<a id="l00068"></a>
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
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>

```c
/*
 * Copyright 2025-2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_NXP_MC_CGM_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_NXP_MC_CGM_H_

/* Define a set of macros related to NXP mc_cgm IP configuration parameter */
#define NXP_PLL_MAXIDOCHANGE   DT_PROP(DT_NODELABEL(mc_cgm), max_ido_change)
#define NXP_PLL_STEPDURATION   DT_PROP(DT_NODELABEL(mc_cgm), step_duration)
#define NXP_PLL_CLKSRCFREQ     DT_PROP(DT_NODELABEL(mc_cgm), clk_src_freq)
#define NXP_PLL_MUX_0_DC_0_DIV DT_PROP(DT_NODELABEL(mc_cgm), mux_0_dc_0_div)
#define NXP_PLL_MUX_0_DC_1_DIV DT_PROP(DT_NODELABEL(mc_cgm), mux_0_dc_1_div)
#define NXP_PLL_MUX_0_DC_2_DIV DT_PROP(DT_NODELABEL(mc_cgm), mux_0_dc_2_div)
#define NXP_PLL_MUX_0_DC_3_DIV DT_PROP(DT_NODELABEL(mc_cgm), mux_0_dc_3_div)
#define NXP_PLL_MUX_0_DC_4_DIV DT_PROP(DT_NODELABEL(mc_cgm), mux_0_dc_4_div)
#define NXP_PLL_MUX_0_DC_5_DIV DT_PROP(DT_NODELABEL(mc_cgm), mux_0_dc_5_div)
#define NXP_PLL_MUX_0_DC_6_DIV DT_PROP(DT_NODELABEL(mc_cgm), mux_0_dc_6_div)
#define NXP_PLL_MUX_1_DC_0_DIV DT_PROP(DT_NODELABEL(mc_cgm), mux_1_dc_0_div)
#define NXP_PLL_MUX_2_DC_0_DIV DT_PROP(DT_NODELABEL(mc_cgm), mux_2_dc_0_div)
#define NXP_PLL_MUX_10_DC_0_DIV DT_PROP(DT_NODELABEL(mc_cgm), mux_10_dc_0_div)

/* Note- clock identifiers in this file must be unique,
 * as the driver uses them in a switch case
 */
#define MCUX_MC_CGM_PERIPHERAL_MASK        0xFF00UL
#define MCUX_MC_CGM_INSTANCE_MASK          0xFFUL
#define MCUX_MC_CGM_CLK_ID(high, low) ((high << 8) | (low))

/* These IDs are used within SOC macros, and thus cannot be defined
 * using the standard MCUX_MC_CGM_CLK_ID form
 */
/* --------------------- System layer clock --------------------- */
#define MCUX_CORESYS_CLK  MCUX_MC_CGM_CLK_ID(0x00, 0x00)
#define MCUX_AIPSPLAT_CLK MCUX_MC_CGM_CLK_ID(0x01, 0x00)
#define MCUX_AIPSSLOW_CLK MCUX_MC_CGM_CLK_ID(0x02, 0x00)
#define MCUX_HSE_CLK      MCUX_MC_CGM_CLK_ID(0x03, 0x00)
#define MCUX_DCM_CLK      MCUX_MC_CGM_CLK_ID(0x04, 0x00)
#define MCUX_LBIST_CLK    MCUX_MC_CGM_CLK_ID(0x05, 0x00)
#define MCUX_QSPI_CLK     MCUX_MC_CGM_CLK_ID(0x06, 0x00)

/* --------------------- MC_CGM clock --------------------- */
#define MCUX_FIRC_CLK    MCUX_MC_CGM_CLK_ID(0x10, 0x00)
#define MCUX_SIRC_CLK    MCUX_MC_CGM_CLK_ID(0x11, 0x00)
#define MCUX_FXOSC_CLK   MCUX_MC_CGM_CLK_ID(0x12, 0x00)
#define MCUX_SXOSC_CLK   MCUX_MC_CGM_CLK_ID(0x13, 0x00)
#define MCUX_PLLPHI0_CLK MCUX_MC_CGM_CLK_ID(0x14, 0x00)
#define MCUX_PLLPHI1_CLK MCUX_MC_CGM_CLK_ID(0x14, 0x01)

/* --------------------- Peripheral clock --------------------- */
#define MCUX_ADC0_CLK MCUX_MC_CGM_CLK_ID(0x20, 0x00)
#define MCUX_ADC1_CLK MCUX_MC_CGM_CLK_ID(0x20, 0x01)
#define MCUX_ADC2_CLK MCUX_MC_CGM_CLK_ID(0x20, 0x02)

#define MCUX_BCTU_CLK MCUX_MC_CGM_CLK_ID(0x21, 0x00)

#define MCUX_CMP0_CLK MCUX_MC_CGM_CLK_ID(0x22, 0x00)
#define MCUX_CMP1_CLK MCUX_MC_CGM_CLK_ID(0x22, 0x01)
#define MCUX_CMP2_CLK MCUX_MC_CGM_CLK_ID(0x22, 0x02)


#define MCUX_EMIOS0_CLK MCUX_MC_CGM_CLK_ID(0x23, 0x00)
#define MCUX_EMIOS1_CLK MCUX_MC_CGM_CLK_ID(0x23, 0x01)
#define MCUX_EMIOS2_CLK MCUX_MC_CGM_CLK_ID(0x23, 0x02)


#define MCUX_FLEXCAN0_CLK MCUX_MC_CGM_CLK_ID(0x24, 0x00)
#define MCUX_FLEXCAN1_CLK MCUX_MC_CGM_CLK_ID(0x24, 0x01)
#define MCUX_FLEXCAN2_CLK MCUX_MC_CGM_CLK_ID(0x24, 0x02)
#define MCUX_FLEXCAN3_CLK MCUX_MC_CGM_CLK_ID(0x24, 0x03)
#define MCUX_FLEXCAN4_CLK MCUX_MC_CGM_CLK_ID(0x24, 0x04)
#define MCUX_FLEXCAN5_CLK MCUX_MC_CGM_CLK_ID(0x24, 0x05)

#define MCUX_FLEXIO_CLK MCUX_MC_CGM_CLK_ID(0x25, 0x00)

#define MCUX_LPI2C0_CLK MCUX_MC_CGM_CLK_ID(0x26, 0x00)
#define MCUX_LPI2C1_CLK MCUX_MC_CGM_CLK_ID(0x26, 0x01)

#define MCUX_LPSPI0_CLK MCUX_MC_CGM_CLK_ID(0x27, 0x00)
#define MCUX_LPSPI1_CLK MCUX_MC_CGM_CLK_ID(0x27, 0x01)
#define MCUX_LPSPI2_CLK MCUX_MC_CGM_CLK_ID(0x27, 0x02)
#define MCUX_LPSPI3_CLK MCUX_MC_CGM_CLK_ID(0x27, 0x03)
#define MCUX_LPSPI4_CLK MCUX_MC_CGM_CLK_ID(0x27, 0x04)
#define MCUX_LPSPI5_CLK MCUX_MC_CGM_CLK_ID(0x27, 0x05)

#define MCUX_LPUART0_CLK  MCUX_MC_CGM_CLK_ID(0x28, 0x00)
#define MCUX_LPUART1_CLK  MCUX_MC_CGM_CLK_ID(0x28, 0x01)
#define MCUX_LPUART2_CLK  MCUX_MC_CGM_CLK_ID(0x28, 0x02)
#define MCUX_LPUART3_CLK  MCUX_MC_CGM_CLK_ID(0x28, 0x03)
#define MCUX_LPUART4_CLK  MCUX_MC_CGM_CLK_ID(0x28, 0x04)
#define MCUX_LPUART5_CLK  MCUX_MC_CGM_CLK_ID(0x28, 0x05)
#define MCUX_LPUART6_CLK  MCUX_MC_CGM_CLK_ID(0x28, 0x06)
#define MCUX_LPUART7_CLK  MCUX_MC_CGM_CLK_ID(0x28, 0x07)
#define MCUX_LPUART8_CLK  MCUX_MC_CGM_CLK_ID(0x28, 0x08)
#define MCUX_LPUART9_CLK  MCUX_MC_CGM_CLK_ID(0x28, 0x09)
#define MCUX_LPUART10_CLK MCUX_MC_CGM_CLK_ID(0x28, 0x0A)
#define MCUX_LPUART11_CLK MCUX_MC_CGM_CLK_ID(0x28, 0x0B)
#define MCUX_LPUART12_CLK MCUX_MC_CGM_CLK_ID(0x28, 0x0C)
#define MCUX_LPUART13_CLK MCUX_MC_CGM_CLK_ID(0x28, 0x0D)
#define MCUX_LPUART14_CLK MCUX_MC_CGM_CLK_ID(0x28, 0x0E)
#define MCUX_LPUART15_CLK MCUX_MC_CGM_CLK_ID(0x28, 0x0F)

#define MCUX_PIT0_CLK MCUX_MC_CGM_CLK_ID(0x29, 0x00)
#define MCUX_PIT1_CLK MCUX_MC_CGM_CLK_ID(0x29, 0x01)
#define MCUX_PIT2_CLK MCUX_MC_CGM_CLK_ID(0x29, 0x02)

#define MCUX_SAI0_CLK MCUX_MC_CGM_CLK_ID(0x2A, 0x00)
#define MCUX_SAI1_CLK MCUX_MC_CGM_CLK_ID(0x2A, 0x01)

#define MCUX_STM0_CLK MCUX_MC_CGM_CLK_ID(0x2B, 0x00)
#define MCUX_STM1_CLK MCUX_MC_CGM_CLK_ID(0x2B, 0x01)

/* --------------------- Partition 2 clock --------------------- */
#define MCUX_QSPISF_CLK MCUX_MC_CGM_CLK_ID(0x2C, 0x00)
#define MCUX_EMACRX_CLK MCUX_MC_CGM_CLK_ID(0x2C, 0x01)
#define MCUX_EMACTX_CLK MCUX_MC_CGM_CLK_ID(0x2C, 0x02)
#define MCUX_EMACTS_CLK MCUX_MC_CGM_CLK_ID(0x2C, 0x03)
#define MCUX_EMAC_CLK   MCUX_MC_CGM_CLK_ID(0x2C, 0x05)

#define MCUX_TEMPSENSE_CLK MCUX_MC_CGM_CLK_ID(0x2C, 0x04)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_NXP_MC_CGM_H_ */
```

## 16.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025-2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

定义与 NXP `mc_cgm` IP 配置参数（Configuration Parameters）有关的一组宏。

### 注释 3：原第 26 行

注意：本文件中的时钟标识符必须唯一，因为驱动会在 `switch case` 中使用它们。

### 注释 4：原第 33 行

这些标识（IDs）在 SoC 宏内部使用，因此不能采用标准 `MCUX_MC_CGM_CLK_ID` 形式定义。

### 注释 5：原第 36 行

系统层时钟（System Layer Clock）。

### 注释 6：原第 45 行

MC_CGM 时钟（Clock）。

### 注释 7：原第 53 行

外设时钟（Peripheral Clock）。

### 注释 8：原第 119 行

分区 2 时钟（Partition 2 Clock）。

### 注释 9：原第 129 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_NXP_MC_CGM_H_`。

## 16.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/nxp__mc__cgm_8h.html)

---

[上一章](P015_nxp-freqme.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P017_pinctrl_nxp_port_common.h_源码浏览.md)
