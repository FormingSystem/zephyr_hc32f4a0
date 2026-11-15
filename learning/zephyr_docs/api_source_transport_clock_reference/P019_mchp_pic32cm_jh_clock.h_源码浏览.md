---
id: learning.zephyr-docs.api-source-transport-clock-reference.page-19
title: mchp_pic32cm_jh_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32cm__jh__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_mchp\_pic32cm\_jh\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32cm__jh__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32cm__jh__clock_8h.html)。

## 19.1\_原始可见代码（Source Code）

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
<a id="foldopen00056"></a>
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

```c
/*
 * Copyright (c) 2025 Microchip Technology Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MCHP_PIC32CM_JH_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MCHP_PIC32CM_JH_CLOCK_H_

#define MCHP_CLOCK_DERIVE_ID(type, mclkbus, mclkmaskbit, gclkperiph, inst)                         \
        (((type) << 26) | ((mclkbus) << 20) | ((mclkmaskbit) << 14) | ((gclkperiph) << 8) | inst)

/* XOSC_TYPE ids */
#define CLOCK_MCHP_XOSC_ID     MCHP_CLOCK_DERIVE_ID(0, 0x3f, 0x3f, 0x3f, 0)
#define CLOCK_MCHP_XOSC_ID_MAX (0)

/* OSC48M_TYPE ids */
#define CLOCK_MCHP_OSC48M_ID     MCHP_CLOCK_DERIVE_ID(1, 0x3f, 0x3f, 0x3f, 0)
#define CLOCK_MCHP_OSC48M_ID_MAX (0)

/* FDPLL_TYPE id */
#define CLOCK_MCHP_FDPLL_ID     MCHP_CLOCK_DERIVE_ID(2, 0x3f, 0x3f, 0, 0)
#define CLOCK_MCHP_FDPLL_ID_MAX (0)

/* RTC_TYPE ids */
#define CLOCK_MCHP_RTC_ID     MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 0)
#define CLOCK_MCHP_RTC_ID_MAX (0)

/* XOSC32K_TYPE ids */
#define CLOCK_MCHP_XOSC32K_ID_XOSC1K  MCHP_CLOCK_DERIVE_ID(4, 0x3f, 0x3f, 0x3f, 0)
#define CLOCK_MCHP_XOSC32K_ID_XOSC32K MCHP_CLOCK_DERIVE_ID(4, 0x3f, 0x3f, 0x3f, 1)
#define CLOCK_MCHP_XOSC32K_ID_MAX     (1)

/* OSC32K_TYPE ids */
#define CLOCK_MCHP_OSC32K_ID_OSC1K  MCHP_CLOCK_DERIVE_ID(5, 0x3f, 0x3f, 0x3f, 0)
#define CLOCK_MCHP_OSC32K_ID_OSC32K MCHP_CLOCK_DERIVE_ID(5, 0x3f, 0x3f, 0x3f, 1)
#define CLOCK_MCHP_OSC32K_ID_MAX    (1)

/* GCLKGEN_TYPE ids */
#define CLOCK_MCHP_GCLKGEN_ID_GEN0 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 0)
#define CLOCK_MCHP_GCLKGEN_ID_GEN1 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 1)
#define CLOCK_MCHP_GCLKGEN_ID_GEN2 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 2)
#define CLOCK_MCHP_GCLKGEN_ID_GEN3 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 3)
#define CLOCK_MCHP_GCLKGEN_ID_GEN4 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 4)
#define CLOCK_MCHP_GCLKGEN_ID_GEN5 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 5)
#define CLOCK_MCHP_GCLKGEN_ID_GEN6 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 6)
#define CLOCK_MCHP_GCLKGEN_ID_GEN7 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 7)
#define CLOCK_MCHP_GCLKGEN_ID_GEN8 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 8)
#define CLOCK_MCHP_GCLKGEN_ID_MAX  (8)

/* GCLKPERIPH_TYPE ids */
#define CLOCK_MCHP_GCLKPERIPH_ID_EIC              MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 2, 0)
#define CLOCK_MCHP_GCLKPERIPH_ID_FREQM_MSR        MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 3, 1)
#define CLOCK_MCHP_GCLKPERIPH_ID_FREQM_REF        MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 4, 2)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CHANNEL_0  MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 5, 3)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CHANNEL_1  MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 6, 4)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CHANNEL_2  MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 7, 5)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CHANNEL_3  MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 8, 6)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CHANNEL_4  MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 9, 7)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CHANNEL_5  MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 10, 8)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CHANNEL_6  MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 11, 9)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CHANNEL_7  MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 12, 10)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CHANNEL_8  MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 13, 11)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CHANNEL_9  MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 14, 12)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CHANNEL_10 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 15, 13)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CHANNEL_11 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 16, 14)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM_0_7_SLOW  MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 17, 15)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_CORE     MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 16)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_CORE     MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 19, 17)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_CORE     MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 20, 18)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_CORE     MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 21, 19)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM4_CORE     MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 22, 20)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM5_CORE     MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 23, 21)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM6_CORE     MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 24, 22)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM7_CORE     MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 25, 23)
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN0             MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 26, 24)
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN1             MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 27, 25)
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC0             MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 28, 26)
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC1             MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 28, 27)
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC2             MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 29, 28)
#define CLOCK_MCHP_GCLKPERIPH_ID_TC0              MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 30, 29)
#define CLOCK_MCHP_GCLKPERIPH_ID_TC1              MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 30, 30)
#define CLOCK_MCHP_GCLKPERIPH_ID_TC2              MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 31, 31)
#define CLOCK_MCHP_GCLKPERIPH_ID_TC3              MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 31, 32)
#define CLOCK_MCHP_GCLKPERIPH_ID_TC4              MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 32, 33)
#define CLOCK_MCHP_GCLKPERIPH_ID_TC5              MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 33, 34)
#define CLOCK_MCHP_GCLKPERIPH_ID_TC6              MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 34, 35)
#define CLOCK_MCHP_GCLKPERIPH_ID_TC7              MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 35, 36)
#define CLOCK_MCHP_GCLKPERIPH_ID_ADC0             MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 36, 37)
#define CLOCK_MCHP_GCLKPERIPH_ID_ADC1             MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 37, 38)
#define CLOCK_MCHP_GCLKPERIPH_ID_DAC              MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 38, 39)
#define CLOCK_MCHP_GCLKPERIPH_ID_PTC              MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 39, 40)
#define CLOCK_MCHP_GCLKPERIPH_ID_CCL              MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 40, 41)
#define CLOCK_MCHP_GCLKPERIPH_ID_PDEC             MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 41, 42)
#define CLOCK_MCHP_GCLKPERIPH_ID_AC               MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 42, 43)
#define CLOCK_MCHP_GCLKPERIPH_ID_MAX              (43)

/* MCLKCPU_TYPE ids */
#define CLOCK_MCHP_MCLKCPU_ID  MCHP_CLOCK_DERIVE_ID(8, 0x3f, 0x3f, 0x3f, 0)
#define CLOCK_MCHP_MCLKCPU_MAX (0)

/* MCLKPERIPH_TYPE ids */
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_APBA      MCHP_CLOCK_DERIVE_ID(9, 0, 0, 0x3f, 0)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_APBB      MCHP_CLOCK_DERIVE_ID(9, 0, 1, 0x3f, 1)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_APBC      MCHP_CLOCK_DERIVE_ID(9, 0, 2, 0x3f, 2)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_DSU       MCHP_CLOCK_DERIVE_ID(9, 0, 3, 0x3f, 3)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_HMATRIXHS MCHP_CLOCK_DERIVE_ID(9, 0, 4, 0x3f, 4)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_NVMCTRL   MCHP_CLOCK_DERIVE_ID(9, 0, 5, 0x3f, 5)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_MCRAMC    MCHP_CLOCK_DERIVE_ID(9, 0, 6, 0x3f, 6)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_DMAC      MCHP_CLOCK_DERIVE_ID(9, 0, 7, 0x3f, 7)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_CAN0      MCHP_CLOCK_DERIVE_ID(9, 0, 8, 0x3f, 8)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_CAN1      MCHP_CLOCK_DERIVE_ID(9, 0, 9, 0x3f, 9)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_PAC       MCHP_CLOCK_DERIVE_ID(9, 0, 10, 0x3f, 10)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_DIVAS     MCHP_CLOCK_DERIVE_ID(9, 0, 12, 0x3f, 11)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_APBD      MCHP_CLOCK_DERIVE_ID(9, 0, 13, 0x3f, 12)
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_ICM       MCHP_CLOCK_DERIVE_ID(9, 0, 14, 0x3f, 13)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_PAC        MCHP_CLOCK_DERIVE_ID(9, 1, 0, 0x3f, 14)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_PM         MCHP_CLOCK_DERIVE_ID(9, 1, 1, 0x3f, 15)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_MCLK       MCHP_CLOCK_DERIVE_ID(9, 1, 2, 0x3f, 16)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_RSTC       MCHP_CLOCK_DERIVE_ID(9, 1, 3, 0x3f, 17)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_OSCCTRL    MCHP_CLOCK_DERIVE_ID(9, 1, 4, 0x3f, 18)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_OSC32KCTRL MCHP_CLOCK_DERIVE_ID(9, 1, 5, 0x3f, 19)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_SUPC       MCHP_CLOCK_DERIVE_ID(9, 1, 6, 0x3f, 20)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_GCLK       MCHP_CLOCK_DERIVE_ID(9, 1, 7, 0x3f, 21)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_WDT        MCHP_CLOCK_DERIVE_ID(9, 1, 8, 0x3f, 22)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_RTC        MCHP_CLOCK_DERIVE_ID(9, 1, 9, 0x3f, 23)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_EIC        MCHP_CLOCK_DERIVE_ID(9, 1, 10, 0x3f, 24)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_FREQM      MCHP_CLOCK_DERIVE_ID(9, 1, 11, 0x3f, 25)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_MCRAMC     MCHP_CLOCK_DERIVE_ID(9, 1, 12, 0x3f, 26)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBB_PORT      MCHP_CLOCK_DERIVE_ID(9, 2, 0, 0x3f, 27)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBB_DSU       MCHP_CLOCK_DERIVE_ID(9, 2, 1, 0x3f, 28)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBB_NVMCTRL   MCHP_CLOCK_DERIVE_ID(9, 2, 2, 0x3f, 29)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBB_HMATRIXHS MCHP_CLOCK_DERIVE_ID(9, 2, 5, 0x3f, 30)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_EVSYS   MCHP_CLOCK_DERIVE_ID(9, 3, 0, 0x3f, 31)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_SERCOM0 MCHP_CLOCK_DERIVE_ID(9, 3, 1, 0x3f, 32)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_SERCOM1 MCHP_CLOCK_DERIVE_ID(9, 3, 2, 0x3f, 33)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_SERCOM2 MCHP_CLOCK_DERIVE_ID(9, 3, 3, 0x3f, 34)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_SERCOM3 MCHP_CLOCK_DERIVE_ID(9, 3, 4, 0x3f, 35)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_SERCOM4 MCHP_CLOCK_DERIVE_ID(9, 3, 5, 0x3f, 36)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_SERCOM5 MCHP_CLOCK_DERIVE_ID(9, 3, 6, 0x3f, 37)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_TCC0    MCHP_CLOCK_DERIVE_ID(9, 3, 9, 0x3f, 38)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_TCC1    MCHP_CLOCK_DERIVE_ID(9, 3, 10, 0x3f, 39)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_TCC2    MCHP_CLOCK_DERIVE_ID(9, 3, 11, 0x3f, 40)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_TC0     MCHP_CLOCK_DERIVE_ID(9, 3, 12, 0x3f, 41)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_TC1     MCHP_CLOCK_DERIVE_ID(9, 3, 13, 0x3f, 42)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_TC2     MCHP_CLOCK_DERIVE_ID(9, 3, 14, 0x3f, 43)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_TC3     MCHP_CLOCK_DERIVE_ID(9, 3, 15, 0x3f, 44)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_TC4     MCHP_CLOCK_DERIVE_ID(9, 3, 16, 0x3f, 45)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_ADC0    MCHP_CLOCK_DERIVE_ID(9, 3, 17, 0x3f, 46)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_ADC1    MCHP_CLOCK_DERIVE_ID(9, 3, 18, 0x3f, 47)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_AC      MCHP_CLOCK_DERIVE_ID(9, 3, 19, 0x3f, 48)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_DAC     MCHP_CLOCK_DERIVE_ID(9, 3, 20, 0x3f, 49)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_PTC     MCHP_CLOCK_DERIVE_ID(9, 3, 21, 0x3f, 50)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_CCL     MCHP_CLOCK_DERIVE_ID(9, 3, 22, 0x3f, 51)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_ICM     MCHP_CLOCK_DERIVE_ID(9, 3, 25, 0x3f, 52)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_PDEC    MCHP_CLOCK_DERIVE_ID(9, 3, 26, 0x3f, 53)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_SMBIST  MCHP_CLOCK_DERIVE_ID(9, 3, 27, 0x3f, 54)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBD_SERCOM6 MCHP_CLOCK_DERIVE_ID(9, 4, 0, 0x3f, 55)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBD_SERCOM7 MCHP_CLOCK_DERIVE_ID(9, 4, 1, 0x3f, 56)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBD_TC5     MCHP_CLOCK_DERIVE_ID(9, 4, 2, 0x3f, 57)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBD_TC6     MCHP_CLOCK_DERIVE_ID(9, 4, 3, 0x3f, 58)
#define CLOCK_MCHP_MCLKPERIPH_ID_APBD_TC7     MCHP_CLOCK_DERIVE_ID(9, 4, 4, 0x3f, 59)
#define CLOCK_MCHP_MCLKPERIPH_ID_MAX          (59)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MCHP_PIC32CM_JH_CLOCK_H_ */
```

## 19.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Microchip Technology Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 59 行

`XOSC_TYPE` 标识符（IDs）。

### 注释 3：原第 63 行

`OSC48M_TYPE` 标识符（IDs）。

### 注释 4：原第 67 行

`FDPLL_TYPE` 标识符（ID）。

### 注释 5：原第 71 行

`RTC_TYPE` 标识符（IDs）。

### 注释 6：原第 75 行

`XOSC32K_TYPE` 标识符（IDs）。

### 注释 7：原第 80 行

`OSC32K_TYPE` 标识符（IDs）。

### 注释 8：原第 85 行

`GCLKGEN_TYPE` 标识符（IDs）。

### 注释 9：原第 97 行

`GCLKPERIPH_TYPE` 标识符（IDs）。

### 注释 10：原第 144 行

`MCLKCPU_TYPE` 标识符（IDs）。

### 注释 11：原第 148 行

`MCLKPERIPH_TYPE` 标识符（IDs）。

### 注释 12：原第 215 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MCHP_PIC32CM_JH_CLOCK_H_`。

## 19.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32cm__jh__clock_8h.html)

---

[上一章](P018_kobject_internal.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P020_mchp_rstc_g1.h_源码浏览.md)
