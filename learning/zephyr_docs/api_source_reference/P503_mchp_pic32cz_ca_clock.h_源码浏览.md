---
id: learning.zephyr-docs.api-source-reference.page-503
title: mchp_pic32cz_ca_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32cz__ca__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第503章\_mchp\_pic32cz\_ca\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32cz__ca__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32cz__ca__clock_8h.html)。

## 503.1\_原始可见代码（Source Code）

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
<a id="foldopen00060"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00095"></a>
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
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00129"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00159"></a>
<a id="l00161"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00171"></a>
<a id="l00173"></a>
<a id="l00175"></a>
<a id="l00177"></a>
<a id="l00179"></a>
<a id="l00185"></a>
<a id="l00187"></a>
<a id="l00189"></a>
<a id="l00191"></a>
<a id="l00193"></a>
<a id="l00195"></a>
<a id="l00197"></a>
<a id="l00199"></a>
<a id="l00201"></a>
<a id="l00203"></a>
<a id="l00205"></a>
<a id="l00207"></a>
<a id="l00209"></a>
<a id="l00211"></a>
<a id="l00213"></a>
<a id="l00215"></a>
<a id="l00217"></a>
<a id="l00219"></a>
<a id="l00221"></a>
<a id="l00223"></a>
<a id="l00225"></a>
<a id="l00227"></a>
<a id="l00229"></a>
<a id="l00231"></a>
<a id="l00233"></a>
<a id="l00235"></a>
<a id="l00237"></a>
<a id="l00239"></a>
<a id="l00241"></a>
<a id="l00243"></a>
<a id="l00245"></a>
<a id="l00247"></a>
<a id="l00249"></a>
<a id="l00251"></a>
<a id="l00253"></a>
<a id="l00255"></a>
<a id="l00257"></a>
<a id="l00259"></a>
<a id="l00261"></a>
<a id="l00263"></a>
<a id="l00265"></a>
<a id="l00267"></a>
<a id="l00269"></a>
<a id="l00271"></a>
<a id="l00273"></a>
<a id="l00275"></a>
<a id="l00277"></a>
<a id="l00279"></a>
<a id="l00281"></a>
<a id="l00283"></a>
<a id="l00285"></a>
<a id="l00287"></a>
<a id="l00289"></a>
<a id="l00291"></a>
<a id="l00293"></a>
<a id="l00295"></a>
<a id="l00297"></a>
<a id="l00299"></a>
<a id="l00301"></a>
<a id="l00303"></a>
<a id="l00305"></a>
<a id="l00307"></a>
<a id="l00309"></a>
<a id="l00311"></a>
<a id="l00313"></a>
<a id="l00319"></a>
<a id="l00321"></a>
<a id="l00323"></a>
<a id="l00325"></a>
<a id="l00332"></a>
<a id="l00334"></a>
<a id="l00336"></a>
<a id="l00338"></a>
<a id="l00340"></a>
<a id="l00342"></a>
<a id="l00344"></a>
<a id="l00346"></a>
<a id="l00348"></a>
<a id="l00350"></a>
<a id="l00352"></a>
<a id="l00354"></a>
<a id="l00356"></a>
<a id="l00358"></a>
<a id="l00360"></a>
<a id="l00362"></a>
<a id="l00364"></a>
<a id="l00366"></a>
<a id="l00368"></a>
<a id="l00370"></a>
<a id="l00372"></a>
<a id="l00374"></a>
<a id="l00376"></a>
<a id="l00378"></a>
<a id="l00380"></a>
<a id="l00382"></a>
<a id="l00384"></a>
<a id="l00386"></a>
<a id="l00388"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00393"></a>
<a id="l00395"></a>
<a id="l00397"></a>
<a id="l00399"></a>
<a id="l00401"></a>
<a id="l00403"></a>
<a id="l00405"></a>
<a id="l00407"></a>
<a id="l00409"></a>
<a id="l00411"></a>
<a id="l00413"></a>
<a id="l00415"></a>
<a id="l00417"></a>
<a id="l00419"></a>
<a id="l00421"></a>
<a id="l00423"></a>
<a id="l00425"></a>
<a id="l00427"></a>
<a id="l00429"></a>
<a id="l00431"></a>
<a id="l00433"></a>
<a id="l00435"></a>
<a id="l00437"></a>
<a id="l00439"></a>
<a id="l00441"></a>
<a id="l00443"></a>
<a id="l00445"></a>
<a id="l00447"></a>
<a id="l00449"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00454"></a>
<a id="l00456"></a>
<a id="l00458"></a>
<a id="l00460"></a>
<a id="l00462"></a>
<a id="l00464"></a>
<a id="l00466"></a>
<a id="l00468"></a>
<a id="l00470"></a>
<a id="l00472"></a>
<a id="l00474"></a>
<a id="l00476"></a>
<a id="l00478"></a>
<a id="l00480"></a>
<a id="l00482"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00487"></a>
<a id="l00489"></a>
<a id="l00490"></a>

```c
/*
 * Copyright (c) 2025-2026 Microchip Technology Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MCHP_PIC32CZ_CA_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MCHP_PIC32CZ_CA_CLOCK_H_

#define MCHP_CLOCK_DERIVE_ID(type, mclkmaskreg, mclkmaskbit, gclkperiph, inst)                     \
        (((type) << 26) | ((mclkmaskreg) << 20) | ((mclkmaskbit) << 14) | ((gclkperiph) << 8) |    \
         inst)

#define CLOCK_MCHP_XOSC_ID     MCHP_CLOCK_DERIVE_ID(0, 0x3f, 0x3f, 0x3f, 0)
#define CLOCK_MCHP_XOSC_ID_MAX (0)

#define CLOCK_MCHP_DFLL48M_ID     MCHP_CLOCK_DERIVE_ID(1, 0x3f, 0x3f, 0, 0)
#define CLOCK_MCHP_DFLL48M_ID_MAX (0)

#define CLOCK_MCHP_DPLL_ID_DPLL0 MCHP_CLOCK_DERIVE_ID(2, 0x3f, 0x3f, 1, 0)
#define CLOCK_MCHP_DPLL_ID_DPLL1 MCHP_CLOCK_DERIVE_ID(2, 0x3f, 0x3f, 2, 1)
#define CLOCK_MCHP_DPLL_ID_MAX   (1)

#define CLOCK_MCHP_DPLL0_ID_OUT0   MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 0)
#define CLOCK_MCHP_DPLL0_ID_OUT1   MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 1)
#define CLOCK_MCHP_DPLL0_ID_OUT2   MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 2)
#define CLOCK_MCHP_DPLL0_ID_OUT3   MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 3)
#define CLOCK_MCHP_DPLL1_ID_OUT0   MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 4)
#define CLOCK_MCHP_DPLL1_ID_OUT1   MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 5)
#define CLOCK_MCHP_DPLL1_ID_OUT2   MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 6)
#define CLOCK_MCHP_DPLL1_ID_OUT3   MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 7)
#define CLOCK_MCHP_DPLL_OUT_ID_MAX (7)

#define CLOCK_MCHP_RTC_ID     MCHP_CLOCK_DERIVE_ID(4, 0x3f, 0x3f, 0x3f, 0)
#define CLOCK_MCHP_RTC_ID_MAX (0)

#define CLOCK_MCHP_XOSC32K_ID     MCHP_CLOCK_DERIVE_ID(5, 0x3f, 0x3f, 0x3f, 0)
#define CLOCK_MCHP_XOSC32K_ID_MAX (0)

#define CLOCK_MCHP_GCLKGEN_ID_GEN0  MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 0)
#define CLOCK_MCHP_GCLKGEN_ID_GEN1  MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 1)
#define CLOCK_MCHP_GCLKGEN_ID_GEN2  MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 2)
#define CLOCK_MCHP_GCLKGEN_ID_GEN3  MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 3)
#define CLOCK_MCHP_GCLKGEN_ID_GEN4  MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 4)
#define CLOCK_MCHP_GCLKGEN_ID_GEN5  MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 5)
#define CLOCK_MCHP_GCLKGEN_ID_GEN6  MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 6)
#define CLOCK_MCHP_GCLKGEN_ID_GEN7  MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 7)
#define CLOCK_MCHP_GCLKGEN_ID_GEN8  MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 8)
#define CLOCK_MCHP_GCLKGEN_ID_GEN9  MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 9)
#define CLOCK_MCHP_GCLKGEN_ID_GEN10 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 10)
#define CLOCK_MCHP_GCLKGEN_ID_GEN11 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 11)
#define CLOCK_MCHP_GCLKGEN_ID_GEN12 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 12)
#define CLOCK_MCHP_GCLKGEN_ID_GEN13 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 13)
#define CLOCK_MCHP_GCLKGEN_ID_GEN14 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 14)
#define CLOCK_MCHP_GCLKGEN_ID_GEN15 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 15)
#define CLOCK_MCHP_GCLKGEN_ID_MAX   (15)

#define CLOCK_MCHP_GCLKPERIPH_ID_FREQM_MSR    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 3, 0)
#define CLOCK_MCHP_GCLKPERIPH_ID_FREQM_REF    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 4, 1)
#define CLOCK_MCHP_GCLKPERIPH_ID_EIC          MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 5, 2)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH0    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 6, 3)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH1    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 7, 4)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH2    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 8, 5)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH3    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 9, 6)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH4    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 10, 7)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH5    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 11, 8)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH6    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 12, 9)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH7    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 13, 10)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH8    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 14, 11)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH9    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 15, 12)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH10   MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 16, 13)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH11   MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 17, 14)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 15)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 16)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM4_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 17)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 19, 18)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 19, 19)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM5_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 19, 20)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM6_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 19, 21)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM7_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 20, 22)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM8_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 20, 23)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM9_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 20, 24)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 21, 25)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 22, 26)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 23, 27)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 24, 28)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM4_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 25, 29)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM5_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 26, 30)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM6_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 27, 31)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM7_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 28, 32)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM8_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 29, 33)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM9_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 30, 34)
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC0         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 31, 35)
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC1         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 32, 36)
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC2         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 33, 37)
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC6         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 37, 38)
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC7         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 38, 39)
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC8         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 39, 40)
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC9         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 40, 41)
#define CLOCK_MCHP_GCLKPERIPH_ID_ADC          MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 41, 42)
#define CLOCK_MCHP_GCLKPERIPH_ID_AC           MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 42, 43)
#define CLOCK_MCHP_GCLKPERIPH_ID_PTC          MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 43, 44)
#define CLOCK_MCHP_GCLKPERIPH_ID_I2S0         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 44, 45)
#define CLOCK_MCHP_GCLKPERIPH_ID_I2S1         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 45, 46)
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN0         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 46, 47)
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN1         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 47, 48)
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN2         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 48, 49)
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN3         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 49, 50)
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN4         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 50, 51)
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN5         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 51, 52)
#define CLOCK_MCHP_GCLKPERIPH_ID_GMAC_TX      MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 54, 53)
#define CLOCK_MCHP_GCLKPERIPH_ID_GMAC_TSU     MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 55, 54)
#define CLOCK_MCHP_GCLKPERIPH_ID_SQI0         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 56, 55)
#define CLOCK_MCHP_GCLKPERIPH_ID_SQI1         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 57, 56)
#define CLOCK_MCHP_GCLKPERIPH_ID_SDHC0_CORE   MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 58, 57)
#define CLOCK_MCHP_GCLKPERIPH_ID_SDHC0_SLOW   MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 59, 58)
#define CLOCK_MCHP_GCLKPERIPH_ID_SDHC1_CORE   MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 60, 59)
#define CLOCK_MCHP_GCLKPERIPH_ID_SDHC1_SLOW   MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 61, 60)
#define CLOCK_MCHP_GCLKPERIPH_ID_MLB          MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 62, 61)
#define CLOCK_MCHP_GCLKPERIPH_ID_CM7_TRACE    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 63, 62)
#define CLOCK_MCHP_GCLKPERIPH_ID_MAX          (62)

#define CLOCK_MCHP_MCLKDOMAIN_ID_CPU    MCHP_CLOCK_DERIVE_ID(8, 0x3f, 0x3f, 0x3f, 0)
#define CLOCK_MCHP_MCLKDOMAIN_ID_PERIPH MCHP_CLOCK_DERIVE_ID(8, 0x3f, 0x3f, 0x3f, 1)
#define CLOCK_MCHP_MCLKDOMAIN_MAX       (1)

#define CLOCK_MCHP_MCLKPERIPH_ID_DSU_AHB      MCHP_CLOCK_DERIVE_ID(9, 0, 0, 0x3f, 0)
#define CLOCK_MCHP_MCLKPERIPH_ID_DSU_APB      MCHP_CLOCK_DERIVE_ID(9, 0, 1, 0x3f, 1)
#define CLOCK_MCHP_MCLKPERIPH_ID_FCW_AHB      MCHP_CLOCK_DERIVE_ID(9, 0, 2, 0x3f, 2)
#define CLOCK_MCHP_MCLKPERIPH_ID_FCW_APB      MCHP_CLOCK_DERIVE_ID(9, 0, 3, 0x3f, 3)
#define CLOCK_MCHP_MCLKPERIPH_ID_FCR_AHB      MCHP_CLOCK_DERIVE_ID(9, 0, 4, 0x3f, 4)
#define CLOCK_MCHP_MCLKPERIPH_ID_FCR_APB      MCHP_CLOCK_DERIVE_ID(9, 0, 5, 0x3f, 5)
#define CLOCK_MCHP_MCLKPERIPH_ID_PM           MCHP_CLOCK_DERIVE_ID(9, 0, 6, 0x3f, 6)
#define CLOCK_MCHP_MCLKPERIPH_ID_SUPC         MCHP_CLOCK_DERIVE_ID(9, 0, 7, 0x3f, 7)
#define CLOCK_MCHP_MCLKPERIPH_ID_RSTC         MCHP_CLOCK_DERIVE_ID(9, 0, 8, 0x3f, 8)
#define CLOCK_MCHP_MCLKPERIPH_ID_OSCCTRL      MCHP_CLOCK_DERIVE_ID(9, 0, 9, 0x3f, 9)
#define CLOCK_MCHP_MCLKPERIPH_ID_OSC32KCTRL   MCHP_CLOCK_DERIVE_ID(9, 0, 10, 0x3f, 10)
#define CLOCK_MCHP_MCLKPERIPH_ID_FREQM        MCHP_CLOCK_DERIVE_ID(9, 0, 13, 0x3f, 11)
#define CLOCK_MCHP_MCLKPERIPH_ID_WDT          MCHP_CLOCK_DERIVE_ID(9, 0, 14, 0x3f, 12)
#define CLOCK_MCHP_MCLKPERIPH_ID_RTC          MCHP_CLOCK_DERIVE_ID(9, 0, 15, 0x3f, 13)
#define CLOCK_MCHP_MCLKPERIPH_ID_EIC          MCHP_CLOCK_DERIVE_ID(9, 0, 16, 0x3f, 14)
#define CLOCK_MCHP_MCLKPERIPH_ID_PAC_AHB      MCHP_CLOCK_DERIVE_ID(9, 0, 17, 0x3f, 15)
#define CLOCK_MCHP_MCLKPERIPH_ID_PAC_APB      MCHP_CLOCK_DERIVE_ID(9, 0, 18, 0x3f, 16)
#define CLOCK_MCHP_MCLKPERIPH_ID_DRMTCM       MCHP_CLOCK_DERIVE_ID(9, 0, 19, 0x3f, 17)
#define CLOCK_MCHP_MCLKPERIPH_ID_MCRAMC       MCHP_CLOCK_DERIVE_ID(9, 0, 20, 0x3f, 18)
#define CLOCK_MCHP_MCLKPERIPH_ID_TRAM         MCHP_CLOCK_DERIVE_ID(9, 0, 21, 0x3f, 19)
#define CLOCK_MCHP_MCLKPERIPH_ID_PORT_AHB     MCHP_CLOCK_DERIVE_ID(9, 0, 22, 0x3f, 20)
#define CLOCK_MCHP_MCLKPERIPH_ID_PORT_APB     MCHP_CLOCK_DERIVE_ID(9, 0, 23, 0x3f, 21)
#define CLOCK_MCHP_MCLKPERIPH_ID_DMAC_AHB     MCHP_CLOCK_DERIVE_ID(9, 0, 24, 0x3f, 22)
#define CLOCK_MCHP_MCLKPERIPH_ID_DMAC_APB     MCHP_CLOCK_DERIVE_ID(9, 0, 25, 0x3f, 23)
#define CLOCK_MCHP_MCLKPERIPH_ID_BUS_AHB      MCHP_CLOCK_DERIVE_ID(9, 0, 26, 0x3f, 24)
#define CLOCK_MCHP_MCLKPERIPH_ID_BUS_APB      MCHP_CLOCK_DERIVE_ID(9, 0, 27, 0x3f, 25)
#define CLOCK_MCHP_MCLKPERIPH_ID_BOOT_ROM_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 28, 0x3f, 26)
#define CLOCK_MCHP_MCLKPERIPH_ID_BOOT_ROM_APB MCHP_CLOCK_DERIVE_ID(9, 0, 29, 0x3f, 27)
#define CLOCK_MCHP_MCLKPERIPH_ID_EVSYS        MCHP_CLOCK_DERIVE_ID(9, 0, 30, 0x3f, 28)
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM0      MCHP_CLOCK_DERIVE_ID(9, 0, 31, 0x3f, 29)

#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM1 MCHP_CLOCK_DERIVE_ID(9, 1, 0, 0x3f, 30)
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM2 MCHP_CLOCK_DERIVE_ID(9, 1, 1, 0x3f, 31)
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM3 MCHP_CLOCK_DERIVE_ID(9, 1, 2, 0x3f, 32)
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM4 MCHP_CLOCK_DERIVE_ID(9, 1, 3, 0x3f, 33)
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM5 MCHP_CLOCK_DERIVE_ID(9, 1, 4, 0x3f, 34)
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM6 MCHP_CLOCK_DERIVE_ID(9, 1, 5, 0x3f, 35)
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM7 MCHP_CLOCK_DERIVE_ID(9, 1, 6, 0x3f, 36)
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM8 MCHP_CLOCK_DERIVE_ID(9, 1, 7, 0x3f, 37)
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM9 MCHP_CLOCK_DERIVE_ID(9, 1, 8, 0x3f, 38)
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC0    MCHP_CLOCK_DERIVE_ID(9, 1, 9, 0x3f, 39)
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC1    MCHP_CLOCK_DERIVE_ID(9, 1, 10, 0x3f, 40)
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC2    MCHP_CLOCK_DERIVE_ID(9, 1, 11, 0x3f, 41)
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC3    MCHP_CLOCK_DERIVE_ID(9, 1, 12, 0x3f, 42)
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC4    MCHP_CLOCK_DERIVE_ID(9, 1, 13, 0x3f, 43)
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC5    MCHP_CLOCK_DERIVE_ID(9, 1, 14, 0x3f, 44)
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC6    MCHP_CLOCK_DERIVE_ID(9, 1, 15, 0x3f, 45)
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC7    MCHP_CLOCK_DERIVE_ID(9, 1, 16, 0x3f, 46)
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC8    MCHP_CLOCK_DERIVE_ID(9, 1, 17, 0x3f, 47)
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC9    MCHP_CLOCK_DERIVE_ID(9, 1, 18, 0x3f, 48)
#define CLOCK_MCHP_MCLKPERIPH_ID_ADC     MCHP_CLOCK_DERIVE_ID(9, 1, 19, 0x3f, 49)
#define CLOCK_MCHP_MCLKPERIPH_ID_AC      MCHP_CLOCK_DERIVE_ID(9, 1, 20, 0x3f, 50)
#define CLOCK_MCHP_MCLKPERIPH_ID_PTC     MCHP_CLOCK_DERIVE_ID(9, 1, 21, 0x3f, 51)
#define CLOCK_MCHP_MCLKPERIPH_ID_I2S2    MCHP_CLOCK_DERIVE_ID(9, 1, 22, 0x3f, 52)
#define CLOCK_MCHP_MCLKPERIPH_ID_I2S1    MCHP_CLOCK_DERIVE_ID(9, 1, 23, 0x3f, 53)
#define CLOCK_MCHP_MCLKPERIPH_ID_CAN0    MCHP_CLOCK_DERIVE_ID(9, 1, 24, 0x3f, 54)
#define CLOCK_MCHP_MCLKPERIPH_ID_CAN1    MCHP_CLOCK_DERIVE_ID(9, 1, 25, 0x3f, 55)
#define CLOCK_MCHP_MCLKPERIPH_ID_CAN2    MCHP_CLOCK_DERIVE_ID(9, 1, 26, 0x3f, 56)
#define CLOCK_MCHP_MCLKPERIPH_ID_CAN3    MCHP_CLOCK_DERIVE_ID(9, 1, 27, 0x3f, 57)
#define CLOCK_MCHP_MCLKPERIPH_ID_CAN4    MCHP_CLOCK_DERIVE_ID(9, 1, 28, 0x3f, 58)
#define CLOCK_MCHP_MCLKPERIPH_ID_CAN5    MCHP_CLOCK_DERIVE_ID(9, 1, 29, 0x3f, 59)

#define CLOCK_MCHP_MCLKPERIPH_ID_GMAC_AHB  MCHP_CLOCK_DERIVE_ID(9, 2, 0, 0x3f, 60)
#define CLOCK_MCHP_MCLKPERIPH_ID_GMAC_APB  MCHP_CLOCK_DERIVE_ID(9, 2, 1, 0x3f, 61)
#define CLOCK_MCHP_MCLKPERIPH_ID_SQI0      MCHP_CLOCK_DERIVE_ID(9, 2, 2, 0x3f, 62)
#define CLOCK_MCHP_MCLKPERIPH_ID_SQI1      MCHP_CLOCK_DERIVE_ID(9, 2, 3, 0x3f, 63)
#define CLOCK_MCHP_MCLKPERIPH_ID_TRNG      MCHP_CLOCK_DERIVE_ID(9, 2, 4, 0x3f, 64)
#define CLOCK_MCHP_MCLKPERIPH_ID_SDHC0_AHB MCHP_CLOCK_DERIVE_ID(9, 2, 5, 0x3f, 65)
#define CLOCK_MCHP_MCLKPERIPH_ID_SDHC0_APB MCHP_CLOCK_DERIVE_ID(9, 2, 6, 0x3f, 66)
#define CLOCK_MCHP_MCLKPERIPH_ID_SDHC1_AHB MCHP_CLOCK_DERIVE_ID(9, 2, 7, 0x3f, 67)
#define CLOCK_MCHP_MCLKPERIPH_ID_SDHC1_APB MCHP_CLOCK_DERIVE_ID(9, 2, 8, 0x3f, 68)
#define CLOCK_MCHP_MCLKPERIPH_ID_HUSB0     MCHP_CLOCK_DERIVE_ID(9, 2, 9, 0x3f, 69)
#define CLOCK_MCHP_MCLKPERIPH_ID_HUSB1     MCHP_CLOCK_DERIVE_ID(9, 2, 10, 0x3f, 70)
#define CLOCK_MCHP_MCLKPERIPH_ID_EBI_AHB   MCHP_CLOCK_DERIVE_ID(9, 2, 11, 0x3f, 71)
#define CLOCK_MCHP_MCLKPERIPH_ID_EBI_APB   MCHP_CLOCK_DERIVE_ID(9, 2, 12, 0x3f, 72)
#define CLOCK_MCHP_MCLKPERIPH_ID_HSM       MCHP_CLOCK_DERIVE_ID(9, 2, 13, 0x3f, 73)
#define CLOCK_MCHP_MCLKPERIPH_ID_MLB_AHB   MCHP_CLOCK_DERIVE_ID(9, 2, 14, 0x3f, 74)
#define CLOCK_MCHP_MCLKPERIPH_ID_MLB_APB   MCHP_CLOCK_DERIVE_ID(9, 2, 15, 0x3f, 75)

#define CLOCK_MCHP_MCLKPERIPH_ID_MAX (75)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MCHP_PIC32CZ_CA_CLOCK_H_ */
```

## 503.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025-2026 Microchip Technology Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 490 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MCHP_PIC32CZ_CA_CLOCK_H_`。

## 503.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32cz__ca__clock_8h.html)

---

[上一章](P502_mchp_pic32cm_sg_gc_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P504_mchp_reset.h_源码浏览.md)
