---
id: learning.zephyr-docs.api-source-compiler-device-reference.page-16
title: mchp_sam_d5x_e5x_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__sam__d5x__e5x__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_mchp\_sam\_d5x\_e5x\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mchp__sam__d5x__e5x__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mchp__sam__d5x__e5x__clock_8h.html)。

## 16.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="foldopen00055"></a>
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
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
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
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>

```c
/*
 * Copyright (c) 2025 Microchip Technology Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MCHP_SAM_D5X_E5X_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MCHP_SAM_D5X_E5X_CLOCK_H_

#define MCHP_CLOCK_DERIVE_ID(type, mclkbus, mclkmaskbit, gclkperiph, inst)                         \
        (((type) << 26) | ((mclkbus) << 20) | ((mclkmaskbit) << 14) | ((gclkperiph) << 8) | inst)

/* XOSC_TYPE ids */
#define CLOCK_MCHP_XOSC_ID_XOSC0 MCHP_CLOCK_DERIVE_ID(0, 0x3f, 0x3f, 0x3f, 0)
#define CLOCK_MCHP_XOSC_ID_XOSC1 MCHP_CLOCK_DERIVE_ID(0, 0x3f, 0x3f, 0x3f, 1)
#define CLOCK_MCHP_XOSC_ID_MAX   (1)

/* DFLL_TYPE ids */
#define CLOCK_MCHP_DFLL_ID  MCHP_CLOCK_DERIVE_ID(1, 0x3f, 0x3f, 0, 0)
#define CLOCK_MCHP_DFLL_MAX (0)

/* FDPLL_TYPE id */
#define CLOCK_MCHP_FDPLL_ID_FDPLL0 MCHP_CLOCK_DERIVE_ID(2, 0x3f, 0x3f, 1, 0)
#define CLOCK_MCHP_FDPLL_ID_FDPLL1 MCHP_CLOCK_DERIVE_ID(2, 0x3f, 0x3f, 2, 1)
#define CLOCK_MCHP_FDPLL_ID_MAX    (1)

/* RTC_TYPE ids */
#define CLOCK_MCHP_RTC_ID     MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 0)
#define CLOCK_MCHP_RTC_ID_MAX (0)

/* XOSC32K_TYPE ids */
#define CLOCK_MCHP_XOSC32K_ID_XOSC1K  MCHP_CLOCK_DERIVE_ID(4, 0x3f, 0x3f, 0x3f, 0)
#define CLOCK_MCHP_XOSC32K_ID_XOSC32K MCHP_CLOCK_DERIVE_ID(4, 0x3f, 0x3f, 0x3f, 1)
#define CLOCK_MCHP_XOSC32K_ID_MAX     (1)

/* GCLKGEN_TYPE ids */
#define CLOCK_MCHP_GCLKGEN_ID_GEN0  MCHP_CLOCK_DERIVE_ID(5, 0x3f, 0x3f, 0x3f, 0)
#define CLOCK_MCHP_GCLKGEN_ID_GEN1  MCHP_CLOCK_DERIVE_ID(5, 0x3f, 0x3f, 0x3f, 1)
#define CLOCK_MCHP_GCLKGEN_ID_GEN2  MCHP_CLOCK_DERIVE_ID(5, 0x3f, 0x3f, 0x3f, 2)
#define CLOCK_MCHP_GCLKGEN_ID_GEN3  MCHP_CLOCK_DERIVE_ID(5, 0x3f, 0x3f, 0x3f, 3)
#define CLOCK_MCHP_GCLKGEN_ID_GEN4  MCHP_CLOCK_DERIVE_ID(5, 0x3f, 0x3f, 0x3f, 4)
#define CLOCK_MCHP_GCLKGEN_ID_GEN5  MCHP_CLOCK_DERIVE_ID(5, 0x3f, 0x3f, 0x3f, 5)
#define CLOCK_MCHP_GCLKGEN_ID_GEN6  MCHP_CLOCK_DERIVE_ID(5, 0x3f, 0x3f, 0x3f, 6)
#define CLOCK_MCHP_GCLKGEN_ID_GEN7  MCHP_CLOCK_DERIVE_ID(5, 0x3f, 0x3f, 0x3f, 7)
#define CLOCK_MCHP_GCLKGEN_ID_GEN8  MCHP_CLOCK_DERIVE_ID(5, 0x3f, 0x3f, 0x3f, 8)
#define CLOCK_MCHP_GCLKGEN_ID_GEN9  MCHP_CLOCK_DERIVE_ID(5, 0x3f, 0x3f, 0x3f, 9)
#define CLOCK_MCHP_GCLKGEN_ID_GEN10 MCHP_CLOCK_DERIVE_ID(5, 0x3f, 0x3f, 0x3f, 10)
#define CLOCK_MCHP_GCLKGEN_ID_GEN11 MCHP_CLOCK_DERIVE_ID(5, 0x3f, 0x3f, 0x3f, 11)
#define CLOCK_MCHP_GCLKGEN_ID_MAX   (11)

/* GCLKPERIPH_TYPE ids */
#define CLOCK_MCHP_GCLKPERIPH_ID_SDHC0_SLOW   MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 3, 0)
#define CLOCK_MCHP_GCLKPERIPH_ID_SDHC1_SLOW   MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 3, 1)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_SLOW MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 3, 2)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_SLOW MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 3, 3)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_SLOW MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 3, 4)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_SLOW MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 3, 5)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM4_SLOW MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 3, 6)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM5_SLOW MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 3, 7)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM6_SLOW MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 3, 8)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM7_SLOW MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 3, 9)
#define CLOCK_MCHP_GCLKPERIPH_ID_EIC          MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 4, 10)
#define CLOCK_MCHP_GCLKPERIPH_ID_FREQM_MSR    MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 5, 11)
#define CLOCK_MCHP_GCLKPERIPH_ID_FREQM_REF    MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 6, 12)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_CORE MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 7, 13)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_CORE MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 8, 14)
#define CLOCK_MCHP_GCLKPERIPH_ID_TC0          MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 9, 15)
#define CLOCK_MCHP_GCLKPERIPH_ID_TC1          MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 9, 16)
#define CLOCK_MCHP_GCLKPERIPH_ID_USB          MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 10, 17)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS0       MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 11, 18)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS1       MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 12, 19)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS2       MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 13, 20)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS3       MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 14, 21)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS4       MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 15, 22)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS5       MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 16, 23)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS6       MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 17, 24)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS7       MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 18, 25)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS8       MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 19, 26)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS9       MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 20, 27)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS10      MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 21, 28)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS11      MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 22, 29)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_CORE MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 23, 30)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_CORE MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 24, 31)
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC0         MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 25, 32)
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC1         MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 25, 33)
#define CLOCK_MCHP_GCLKPERIPH_ID_TC2          MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 26, 34)
#define CLOCK_MCHP_GCLKPERIPH_ID_TC3          MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 26, 35)
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN0         MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 27, 36)
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN1         MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 28, 37)
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC2         MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 29, 38)
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC3         MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 29, 39)
#define CLOCK_MCHP_GCLKPERIPH_ID_TC4          MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 30, 40)
#define CLOCK_MCHP_GCLKPERIPH_ID_TC5          MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 30, 41)
#define CLOCK_MCHP_GCLKPERIPH_ID_PDEC         MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 31, 42)
#define CLOCK_MCHP_GCLKPERIPH_ID_AC           MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 32, 43)
#define CLOCK_MCHP_GCLKPERIPH_ID_CCL          MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 33, 44)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM4_CORE MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 34, 45)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM5_CORE MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 35, 46)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM6_CORE MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 36, 47)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM7_CORE MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 37, 48)
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC4         MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 38, 49)
#define CLOCK_MCHP_GCLKPERIPH_ID_TC6          MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 39, 50)
#define CLOCK_MCHP_GCLKPERIPH_ID_TC7          MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 39, 51)
#define CLOCK_MCHP_GCLKPERIPH_ID_ADC0         MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 40, 52)
#define CLOCK_MCHP_GCLKPERIPH_ID_ADC1         MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 41, 53)
#define CLOCK_MCHP_GCLKPERIPH_ID_DAC          MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 42, 54)
#define CLOCK_MCHP_GCLKPERIPH_ID_I2S0         MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 43, 55)
#define CLOCK_MCHP_GCLKPERIPH_ID_I2S1         MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 44, 56)
#define CLOCK_MCHP_GCLKPERIPH_ID_SDHC0        MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 45, 57)
#define CLOCK_MCHP_GCLKPERIPH_ID_SDHC1        MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 46, 58)
#define CLOCK_MCHP_GCLKPERIPH_ID_CM4_TRACE    MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 47, 59)
#define CLOCK_MCHP_GCLKPERIPH_ID_MAX          (59)

/* MCLKCPU_TYPE ids */
#define CLOCK_MCHP_MCLKCPU_ID  MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 0x3f, 0)
#define CLOCK_MCHP_MCLKCPU_MAX (0)

/* MCLKPERIPH_TYPE ids */
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_HPB0             MCHP_CLOCK_DERIVE_ID(8, 0, 0, 0x3f, 0)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_HPB1             MCHP_CLOCK_DERIVE_ID(8, 0, 1, 0x3f, 1)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_HPB2             MCHP_CLOCK_DERIVE_ID(8, 0, 2, 0x3f, 2)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_HPB3             MCHP_CLOCK_DERIVE_ID(8, 0, 3, 0x3f, 3)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_DSU              MCHP_CLOCK_DERIVE_ID(8, 0, 4, 0x3f, 4)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_NVMCTRL          MCHP_CLOCK_DERIVE_ID(8, 0, 6, 0x3f, 5)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_CMCC             MCHP_CLOCK_DERIVE_ID(8, 0, 8, 0x3f, 6)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_DMAC             MCHP_CLOCK_DERIVE_ID(8, 0, 9, 0x3f, 7)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_USB              MCHP_CLOCK_DERIVE_ID(8, 0, 10, 0x3f, 8)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_PAC              MCHP_CLOCK_DERIVE_ID(8, 0, 12, 0x3f, 9)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_QSPI             MCHP_CLOCK_DERIVE_ID(8, 0, 13, 0x3f, 10)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_GMAC             MCHP_CLOCK_DERIVE_ID(8, 0, 14, 0x3f, 11)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_SDHC0            MCHP_CLOCK_DERIVE_ID(8, 0, 15, 0x3f, 12)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_SDHC1            MCHP_CLOCK_DERIVE_ID(8, 0, 16, 0x3f, 13)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_CAN0             MCHP_CLOCK_DERIVE_ID(8, 0, 17, 0x3f, 14)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_CAN1             MCHP_CLOCK_DERIVE_ID(8, 0, 18, 0x3f, 15)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_ICM              MCHP_CLOCK_DERIVE_ID(8, 0, 19, 0x3f, 16)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_PUKCC            MCHP_CLOCK_DERIVE_ID(8, 0, 20, 0x3f, 17)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_QSPI_2X          MCHP_CLOCK_DERIVE_ID(8, 0, 21, 0x3f, 18)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_NVMCTRL_SMEEPROM MCHP_CLOCK_DERIVE_ID(8, 0, 22, 0x3f, 19)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_NVMCTRL_CACHE    MCHP_CLOCK_DERIVE_ID(8, 0, 23, 0x3f, 20)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_PAC        MCHP_CLOCK_DERIVE_ID(8, 1, 0, 0x3f, 21)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_PM         MCHP_CLOCK_DERIVE_ID(8, 1, 1, 0x3f, 22)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_MCLK       MCHP_CLOCK_DERIVE_ID(8, 1, 2, 0x3f, 23)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_RSTC       MCHP_CLOCK_DERIVE_ID(8, 1, 3, 0x3f, 24)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_OSCCTRL    MCHP_CLOCK_DERIVE_ID(8, 1, 4, 0x3f, 25)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_OSC32KCTRL MCHP_CLOCK_DERIVE_ID(8, 1, 5, 0x3f, 26)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_SUPC       MCHP_CLOCK_DERIVE_ID(8, 1, 6, 0x3f, 27)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_GCLK       MCHP_CLOCK_DERIVE_ID(8, 1, 7, 0x3f, 28)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_WDT        MCHP_CLOCK_DERIVE_ID(8, 1, 8, 0x3f, 29)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_RTC        MCHP_CLOCK_DERIVE_ID(8, 1, 9, 0x3f, 30)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_EIC        MCHP_CLOCK_DERIVE_ID(8, 1, 10, 0x3f, 31)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_FREQM      MCHP_CLOCK_DERIVE_ID(8, 1, 11, 0x3f, 32)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_SERCOM0    MCHP_CLOCK_DERIVE_ID(8, 1, 12, 0x3f, 33)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_SERCOM1    MCHP_CLOCK_DERIVE_ID(8, 1, 13, 0x3f, 34)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_TC0        MCHP_CLOCK_DERIVE_ID(8, 1, 14, 0x3f, 35)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_TC1        MCHP_CLOCK_DERIVE_ID(8, 1, 15, 0x3f, 36)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBB_USB     MCHP_CLOCK_DERIVE_ID(8, 2, 0, 0x3f, 37)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBB_DSU     MCHP_CLOCK_DERIVE_ID(8, 2, 1, 0x3f, 38)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBB_NVMCTRL MCHP_CLOCK_DERIVE_ID(8, 2, 2, 0x3f, 39)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBB_PORT    MCHP_CLOCK_DERIVE_ID(8, 2, 4, 0x3f, 40)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBB_EVSYS   MCHP_CLOCK_DERIVE_ID(8, 2, 7, 0x3f, 41)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBB_SERCOM2 MCHP_CLOCK_DERIVE_ID(8, 2, 9, 0x3f, 42)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBB_SERCOM3 MCHP_CLOCK_DERIVE_ID(8, 2, 10, 0x3f, 43)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBB_TCC0    MCHP_CLOCK_DERIVE_ID(8, 2, 11, 0x3f, 44)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBB_TCC1    MCHP_CLOCK_DERIVE_ID(8, 2, 12, 0x3f, 45)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBB_TC2     MCHP_CLOCK_DERIVE_ID(8, 2, 13, 0x3f, 46)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBB_TC3     MCHP_CLOCK_DERIVE_ID(8, 2, 14, 0x3f, 47)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBB_RAMECC  MCHP_CLOCK_DERIVE_ID(8, 2, 16, 0x3f, 48)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_GMAC MCHP_CLOCK_DERIVE_ID(8, 3, 2, 0x3f, 49)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_TCC2 MCHP_CLOCK_DERIVE_ID(8, 3, 3, 0x3f, 50)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_TCC3 MCHP_CLOCK_DERIVE_ID(8, 3, 4, 0x3f, 51)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_TC4  MCHP_CLOCK_DERIVE_ID(8, 3, 5, 0x3f, 52)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_TC5  MCHP_CLOCK_DERIVE_ID(8, 3, 6, 0x3f, 53)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_PDEC MCHP_CLOCK_DERIVE_ID(8, 3, 7, 0x3f, 54)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_AC   MCHP_CLOCK_DERIVE_ID(8, 3, 8, 0x3f, 55)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_AES  MCHP_CLOCK_DERIVE_ID(8, 3, 9, 0x3f, 56)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_TRNG MCHP_CLOCK_DERIVE_ID(8, 3, 10, 0x3f, 57)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_ICM  MCHP_CLOCK_DERIVE_ID(8, 3, 11, 0x3f, 58)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_QSPI MCHP_CLOCK_DERIVE_ID(8, 3, 13, 0x3f, 59)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_CCL  MCHP_CLOCK_DERIVE_ID(8, 3, 14, 0x3f, 60)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBD_SERCOM4 MCHP_CLOCK_DERIVE_ID(8, 4, 0, 0x3f, 61)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBD_SERCOM5 MCHP_CLOCK_DERIVE_ID(8, 4, 1, 0x3f, 62)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBD_SERCOM6 MCHP_CLOCK_DERIVE_ID(8, 4, 2, 0x3f, 63)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBD_SERCOM7 MCHP_CLOCK_DERIVE_ID(8, 4, 3, 0x3f, 64)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBD_TCC4    MCHP_CLOCK_DERIVE_ID(8, 4, 4, 0x3f, 65)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBD_TC6     MCHP_CLOCK_DERIVE_ID(8, 4, 5, 0x3f, 66)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBD_TC7     MCHP_CLOCK_DERIVE_ID(8, 4, 6, 0x3f, 67)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBD_ADC0    MCHP_CLOCK_DERIVE_ID(8, 4, 7, 0x3f, 68)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBD_ADC1    MCHP_CLOCK_DERIVE_ID(8, 4, 8, 0x3f, 69)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBD_DAC     MCHP_CLOCK_DERIVE_ID(8, 4, 9, 0x3f, 70)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBD_I2S     MCHP_CLOCK_DERIVE_ID(8, 4, 10, 0x3f, 71)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBD_PCC     MCHP_CLOCK_DERIVE_ID(8, 4, 11, 0x3f, 72)
#define CLOCK_MCHP_MCLKPERIPH_ID_MAX          (72)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MCHP_SAM_D5X_E5X_CLOCK_H_ */
```

## 16.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Microchip Technology Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 58 行

`XOSC_TYPE` 标识符（IDs）。

### 注释 3：原第 63 行

`DFLL_TYPE` 标识符（IDs）。

### 注释 4：原第 67 行

`FDPLL_TYPE` 标识符（ID）。

### 注释 5：原第 72 行

`RTC_TYPE` 标识符（IDs）。

### 注释 6：原第 76 行

`XOSC32K_TYPE` 标识符（IDs）。

### 注释 7：原第 81 行

`GCLKGEN_TYPE` 标识符（IDs）。

### 注释 8：原第 96 行

`GCLKPERIPH_TYPE` 标识符（IDs）。

### 注释 9：原第 159 行

`MCLKCPU_TYPE` 标识符（IDs）。

### 注释 10：原第 163 行

`MCLKPERIPH_TYPE` 标识符（IDs）。

### 注释 11：原第 243 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MCHP_SAM_D5X_E5X_CLOCK_H_`。

## 16.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mchp__sam__d5x__e5x__clock_8h.html)

---

[上一章](P015_intc_exti_stm32.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P017_tle9104.h_源码浏览.md)
