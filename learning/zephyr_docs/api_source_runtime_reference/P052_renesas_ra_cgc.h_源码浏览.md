---
id: learning.zephyr-docs.api-source-runtime-reference.page-52
title: renesas_ra_cgc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas__ra__cgc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第52章\_renesas\_ra\_cgc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/renesas__ra__cgc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/renesas__ra__cgc_8h.html)。

## 52.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00024"></a>
<a id="foldopen00031"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="foldopen00041"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="foldopen00051"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00141"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00154"></a>
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00162"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00168"></a>
<a id="l00170"></a>
<a id="l00177"></a>
<a id="l00179"></a>
<a id="l00181"></a>
<a id="l00183"></a>
<a id="l00185"></a>
<a id="l00187"></a>
<a id="l00189"></a>
<a id="l00191"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00196"></a>
<a id="l00198"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00236"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00253"></a>
<a id="foldopen00257"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="foldopen00265"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="aclock__control_8h_html"></a>
<a id="ara__clock_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructclock__control__ra__pclk__cfg_html"></a>
<a id="astructclock__control__ra__pclk__cfg_html_a2ce24e482ea7557d197c87230eba0361"></a>
<a id="astructclock__control__ra__pclk__cfg_html_a7e4090da84776edb0db7f0eec18767a3"></a>
<a id="astructclock__control__ra__subsys__cfg_html"></a>
<a id="astructclock__control__ra__subsys__cfg_html_accdec304bb04737be3f75f0df3a29023"></a>
<a id="astructclock__control__ra__subsys__cfg_html_ad2dd15542bd355b716407bf9d9992f15"></a>

```c
/*
 * Copyright (c) 2024-2026 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_RENESAS_RA_CGC_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_RENESAS_RA_CGC_H_

#include <zephyr/drivers/clock_control.h>
#include <zephyr/dt-bindings/clock/ra_clock.h>


#define RA_CGC_PROP_HAS_STATUS_OKAY_OR(node_id, prop, default_value)                               \
        COND_CODE_1(DT_NODE_HAS_STATUS(node_id, okay), \
                (DT_PROP(node_id, prop)), (default_value))

#define RA_CGC_CLK_SRC(node_id)                                                                    \
        COND_CODE_1(DT_NODE_HAS_STATUS(node_id, okay), \
                (UTIL_CAT(BSP_CLOCKS_SOURCE_, DT_NODE_FULL_NAME_UPPER_TOKEN(node_id))), \
                (BSP_CLOCKS_CLOCK_DISABLED))

#define RA_CGC_CLK_DIV(clk, prop, default_value)                                                   \
        UTIL_CAT(RA_CGC_DIV_, DT_NODE_FULL_NAME_UPPER_TOKEN(clk))                                  \
        (RA_CGC_PROP_HAS_STATUS_OKAY_OR(clk, prop, default_value))


#define RA_CGC_DIV_BCLK(n)       UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
#define RA_CGC_DIV_CANFDCLK(n)   UTIL_CAT(BSP_CLOCKS_CANFD_CLOCK_DIV_, n)
#define RA_CGC_DIV_CECCLK(n)     UTIL_CAT(BSP_CLOCKS_CEC_CLOCK_DIV_, n)
#define RA_CGC_DIV_CLKOUT(n)     UTIL_CAT(BSP_CLOCKS_CLKOUT_DIV_, n)
#define RA_CGC_DIV_CPUCLK0(n)    UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
#define RA_CGC_DIV_CPUCLK1(n)    UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
#define RA_CGC_DIV_MRPCLK(n)     UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
#define RA_CGC_DIV_CPUCLK(n)     UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
#define RA_CGC_DIV_FCLK(n)       UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
#define RA_CGC_DIV_I3CCLK(n)     UTIL_CAT(BSP_CLOCKS_I3C_CLOCK_DIV_, n)
#define RA_CGC_DIV_ICLK(n)       UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
#define RA_CGC_DIV_LCDCLK(n)     UTIL_CAT(BSP_CLOCKS_LCD_CLOCK_DIV_, n)
#define RA_CGC_DIV_OCTASPICLK(n) UTIL_CAT(BSP_CLOCKS_OCTA_CLOCK_DIV_, n)
#define RA_CGC_DIV_PCLKA(n)      UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
#define RA_CGC_DIV_PCLKB(n)      UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
#define RA_CGC_DIV_PCLKC(n)      UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
#define RA_CGC_DIV_PCLKD(n)      UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
#define RA_CGC_DIV_PCLKE(n)      UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
#define RA_CGC_DIV_PLL(n)        UTIL_CAT(BSP_CLOCKS_PLL_DIV_, n)
#define RA_CGC_DIV_PLLP(n)       UTIL_CAT(BSP_CLOCKS_PLL_DIV_, n)
#define RA_CGC_DIV_PLLQ(n)       UTIL_CAT(BSP_CLOCKS_PLL_DIV_, n)
#define RA_CGC_DIV_PLLR(n)       UTIL_CAT(BSP_CLOCKS_PLL_DIV_, n)
#define RA_CGC_DIV_PLL2(n)       UTIL_CAT(BSP_CLOCKS_PLL_DIV_, n)
#define RA_CGC_DIV_PLL2P(n)      UTIL_CAT(BSP_CLOCKS_PLL_DIV_, n)
#define RA_CGC_DIV_PLL2Q(n)      UTIL_CAT(BSP_CLOCKS_PLL_DIV_, n)
#define RA_CGC_DIV_PLL2R(n)      UTIL_CAT(BSP_CLOCKS_PLL_DIV_, n)
#define RA_CGC_DIV_SCICLK(n)     UTIL_CAT(BSP_CLOCKS_SCI_CLOCK_DIV_, n)
#define RA_CGC_DIV_SPICLK(n)     UTIL_CAT(BSP_CLOCKS_SPI_CLOCK_DIV_, n)
#define RA_CGC_DIV_U60CLK(n)     UTIL_CAT(BSP_CLOCKS_USB60_CLOCK_DIV_, n)
#define RA_CGC_DIV_UCLK(n)       UTIL_CAT(BSP_CLOCKS_USB_CLOCK_DIV_, n)
#define RA_CGC_DIV_SCISPICLK(n)  UTIL_CAT(BSP_CLOCKS_SCISPI_CLOCK_DIV_, n)
#define RA_CGC_DIV_GPTCLK(n)     UTIL_CAT(BSP_CLOCKS_GPT_CLOCK_DIV_, n)
#define RA_CGC_DIV_IICCLK(n)     UTIL_CAT(BSP_CLOCKS_IIC_CLOCK_DIV_, n)
#define RA_CGC_DIV_ADCCLK(n)     UTIL_CAT(BSP_CLOCKS_ADC_CLOCK_DIV_, n)
#define RA_CGC_DIV_MRICLK(n)     UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
#define RA_CGC_DIV_NPUCLK(n)     UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
#define RA_CGC_DIV_BCLKA(n)      UTIL_CAT(BSP_CLOCKS_BCLKA_CLOCK_DIV_, n)
#define RA_CGC_DIV_ESWCLK(n)     UTIL_CAT(BSP_CLOCKS_ESW_CLOCK_DIV_, n)
#define RA_CGC_DIV_ESWPHYCLK(n)  UTIL_CAT(BSP_CLOCKS_ESWPHY_CLOCK_DIV_, n)
#define RA_CGC_DIV_ETHPHYCLK(n)  UTIL_CAT(BSP_CLOCKS_ETHPHY_CLOCK_DIV_, n)
#define RA_CGC_DIV_ESCCLK(n)     UTIL_CAT(BSP_CLOCKS_ESC_CLOCK_DIV_, n)
#define RA_CGC_DIV_DSMIFCLK(n)   UTIL_CAT(BSP_CLOCKS_DSMIF_CLOCK_DIV_, n)

#define RA_CGC_DIV_XTALDIV_CLK(n) UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
#define RA_CGC_DIV_HOCODIV_CLK(n) UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
#define RA_CGC_DIV_MOCODIV_CLK(n) UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
#define RA_CGC_DIV_SAU_CK00(n)    UTIL_CAT(BSP_CLOCKS_SAU_CLOCK_DIV_, n)
#define RA_CGC_DIV_SAU_CK01(n)    UTIL_CAT(BSP_CLOCKS_SAU_CLOCK_DIV_, n)
#define RA_CGC_DIV_SAU_CK10(n)    UTIL_CAT(BSP_CLOCKS_SAU_CLOCK_DIV_, n)
#define RA_CGC_DIV_SAU_CK11(n)    UTIL_CAT(BSP_CLOCKS_SAU_CLOCK_DIV_, n)
#define RA_CGC_DIV_TAU_CK01(n)    UTIL_CAT(TIMER_SOURCE_DIV_, n)
#define RA_CGC_DIV_TAU_CK02(n)    UTIL_CAT(TIMER_SOURCE_DIV_, n)
#define RA_CGC_DIV_TAU_CK03(n)    UTIL_CAT(TIMER_SOURCE_DIV_, n)
#define RA_CGC_DIV_TAU_CK04(n)    UTIL_CAT(TIMER_SOURCE_DIV_, n)


#define BSP_CLOCKS_SOURCE_PLL   BSP_CLOCKS_SOURCE_CLOCK_PLL
#define BSP_CLOCKS_SOURCE_PLLP  BSP_CLOCKS_SOURCE_CLOCK_PLL
#define BSP_CLOCKS_SOURCE_PLLQ  BSP_CLOCKS_SOURCE_CLOCK_PLL1Q
#define BSP_CLOCKS_SOURCE_PLLR  BSP_CLOCKS_SOURCE_CLOCK_PLL1R
#define BSP_CLOCKS_SOURCE_PLL2  BSP_CLOCKS_SOURCE_CLOCK_PLL2
#define BSP_CLOCKS_SOURCE_PLL2P BSP_CLOCKS_SOURCE_CLOCK_PLL2
#define BSP_CLOCKS_SOURCE_PLL2Q BSP_CLOCKS_SOURCE_CLOCK_PLL2Q
#define BSP_CLOCKS_SOURCE_PLL2R BSP_CLOCKS_SOURCE_CLOCK_PLL2R

#define BSP_CLOCKS_SOURCE_XTALDIV_CLK BSP_CLOCKS_SOURCE_CLOCK_MAIN_OSC
#define BSP_CLOCKS_SOURCE_HOCODIV_CLK BSP_CLOCKS_SOURCE_CLOCK_HOCO
#define BSP_CLOCKS_SOURCE_MOCODIV_CLK BSP_CLOCKS_SOURCE_CLOCK_MOCO

#if DT_NODE_HAS_STATUS_OKAY(DT_NODELABEL(pclk))
#if DT_SAME_NODE(DT_CLOCKS_CTLR(DT_NODELABEL(pclk)), DT_NODELABEL(hoco))
#define BSP_CLOCKS_SOURCE_PCLK BSP_CLOCKS_SOURCE_CLOCK_HOCO
#elif DT_SAME_NODE(DT_CLOCKS_CTLR(DT_NODELABEL(pclk)), DT_NODELABEL(moco))
#define BSP_CLOCKS_SOURCE_PCLK BSP_CLOCKS_SOURCE_CLOCK_MOCO
#elif DT_SAME_NODE(DT_CLOCKS_CTLR(DT_NODELABEL(pclk)), DT_NODELABEL(loco))
#define BSP_CLOCKS_SOURCE_PCLK BSP_CLOCKS_SOURCE_CLOCK_LOCO
#elif DT_SAME_NODE(DT_CLOCKS_CTLR(DT_NODELABEL(pclk)), DT_NODELABEL(xtal))
#define BSP_CLOCKS_SOURCE_PCLK BSP_CLOCKS_SOURCE_CLOCK_MAIN_OSC
#elif DT_SAME_NODE(DT_CLOCKS_CTLR(DT_NODELABEL(pclk)), DT_NODELABEL(subclk))
#define BSP_CLOCKS_SOURCE_PCLK BSP_CLOCKS_SOURCE_CLOCK_SUBCLOCK
#elif DT_SAME_NODE(DT_CLOCKS_CTLR(DT_NODELABEL(pclk)), DT_NODELABEL(hocodiv_clk))
#define BSP_CLOCKS_SOURCE_PCLK BSP_CLOCKS_SOURCE_HOCODIV_CLK
#elif DT_SAME_NODE(DT_CLOCKS_CTLR(DT_NODELABEL(pclk)), DT_NODELABEL(mocodiv_clk))
#define BSP_CLOCKS_SOURCE_PCLK BSP_CLOCKS_SOURCE_MOCODIV_CLK
#elif DT_SAME_NODE(DT_CLOCKS_CTLR(DT_NODELABEL(pclk)), DT_NODELABEL(xtaldiv_clk))
#define BSP_CLOCKS_SOURCE_PCLK BSP_CLOCKS_SOURCE_XTALDIV_CLK
#else
#error "Invalid pclk source clock"
#endif
#endif /* DT_NODE_HAS_STATUS_OKAY(DT_NODELABEL(pclk)) */

#if DT_NODE_HAS_STATUS_OKAY(DT_NODELABEL(fsxp))
#if DT_SAME_NODE(DT_CLOCKS_CTLR(DT_NODELABEL(fsxp)), DT_NODELABEL(loco))
#define BSP_CLOCKS_SOURCE_FSXP BSP_CLOCKS_SOURCE_CLOCK_LOCO
#elif DT_SAME_NODE(DT_CLOCKS_CTLR(DT_NODELABEL(fsxp)), DT_NODELABEL(subclk))
#define BSP_CLOCKS_SOURCE_FSXP BSP_CLOCKS_SOURCE_CLOCK_SUBCLOCK
#else
#error "Invalid fsxp source clock"
#endif /* DT_SAME_NODE(DT_CLOCKS_CTLR(DT_NODELABEL(fsxp)), DT_NODELABEL(loco)) */
#endif /* DT_NODE_HAS_STATUS_OKAY(DT_NODELABEL(fsxp)) */


#define BSP_CLOCKS_CLKOUT_DIV_1   (0)
#define BSP_CLOCKS_CLKOUT_DIV_2   (1)
#define BSP_CLOCKS_CLKOUT_DIV_4   (2)
#define BSP_CLOCKS_CLKOUT_DIV_8   (3)
#define BSP_CLOCKS_CLKOUT_DIV_16  (4)
#define BSP_CLOCKS_CLKOUT_DIV_32  (5)
#define BSP_CLOCKS_CLKOUT_DIV_64  (6)
#define BSP_CLOCKS_CLKOUT_DIV_128 (7)

struct clock_control_ra_pclk_cfg {
        uint32_t clk_src;
        uint32_t clk_div;
};

struct clock_control_ra_subsys_cfg {
        uint32_t mstp;
        uint32_t stop_bit;
};


#endif /* ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_RENESAS_RA_CGC_H_ */
```

## 52.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024-2026 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 223 行

条件编译表达式：`DT_NODE_HAS_STATUS_OKAY(DT_NODELABEL(pclk))`。

### 注释 3：原第 233 行

条件编译表达式：`DT_SAME_NODE(DT_CLOCKS_CTLR(DT_NODELABEL(fsxp)), DT_NODELABEL(loco))`。

### 注释 4：原第 234 行

条件编译表达式：`DT_NODE_HAS_STATUS_OKAY(DT_NODELABEL(fsxp))`。

### 注释 5：原第 272 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_RENESAS_RA_CGC_H_`。

## 52.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/renesas__ra__cgc_8h.html)
- [zephyr/drivers/clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)
- [zephyr/dt-bindings/clock/ra_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/ra__clock_8h.html)
- [clock_control_ra_pclk_cfg](../clock_cmsis_model_reference/P001_clock_control_ra_pclk_cfg_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [clk_src](../clock_cmsis_model_reference/P001_clock_control_ra_pclk_cfg_结构体.md#a7e4090da84776edb0db7f0eec18767a3)
- [clk_div](../clock_cmsis_model_reference/P001_clock_control_ra_pclk_cfg_结构体.md#a2ce24e482ea7557d197c87230eba0361)
- [clock_control_ra_subsys_cfg](../clock_cmsis_model_reference/P002_clock_control_ra_subsys_cfg_结构体.md)
- [mstp](../clock_cmsis_model_reference/P002_clock_control_ra_subsys_cfg_结构体.md#accdec304bb04737be3f75f0df3a29023)
- [stop_bit](../clock_cmsis_model_reference/P002_clock_control_ra_subsys_cfg_结构体.md#ad2dd15542bd355b716407bf9d9992f15)
- [clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)
- [ra_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/ra__clock_8h.html)
- [clock_control_ra_pclk_cfg::clk_div](../clock_cmsis_model_reference/P001_clock_control_ra_pclk_cfg_结构体.md#a2ce24e482ea7557d197c87230eba0361)
- [clock_control_ra_pclk_cfg::clk_src](../clock_cmsis_model_reference/P001_clock_control_ra_pclk_cfg_结构体.md#a7e4090da84776edb0db7f0eec18767a3)
- [clock_control_ra_subsys_cfg::mstp](../clock_cmsis_model_reference/P002_clock_control_ra_subsys_cfg_结构体.md#accdec304bb04737be3f75f0df3a29023)
- [clock_control_ra_subsys_cfg::stop_bit](../clock_cmsis_model_reference/P002_clock_control_ra_subsys_cfg_结构体.md#ad2dd15542bd355b716407bf9d9992f15)

---

[上一章](P051_printk.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P053_rfcomm.h_源码浏览.md)
