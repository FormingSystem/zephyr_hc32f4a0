---
id: learning.zephyr-docs.api-source-reference.page-502
title: mchp_pic32cm_sg_gc_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32cm__sg__gc__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第502章\_mchp\_pic32cm\_sg\_gc\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32cm__sg__gc__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32cm__sg__gc__clock_8h.html)。

## 502.1\_原始可见代码（Source Code）

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
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00127"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00141"></a>
<a id="l00143"></a>
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
<a id="l00169"></a>
<a id="l00171"></a>
<a id="l00173"></a>
<a id="l00175"></a>
<a id="l00177"></a>
<a id="l00179"></a>
<a id="l00181"></a>
<a id="l00183"></a>
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
<a id="l00259"></a>
<a id="l00261"></a>
<a id="l00263"></a>
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
<a id="l00315"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00320"></a>
<a id="l00322"></a>
<a id="l00324"></a>
<a id="l00326"></a>
<a id="l00328"></a>
<a id="l00330"></a>
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
<a id="l00381"></a>
<a id="l00383"></a>
<a id="l00385"></a>
<a id="l00386"></a>

```c
/*
 * Copyright (c) 2026 Microchip Technology Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MCHP_PIC32CM_SG_GC_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MCHP_PIC32CM_SG_GC_CLOCK_H_

#define MCHP_CLOCK_DERIVE_ID(type, mclkmaskreg, mclkmaskbit, gclkperiph, inst)                     \
        (((type) << 26) | ((mclkmaskreg) << 20) | ((mclkmaskbit) << 14) | ((gclkperiph) << 8) |    \
         inst)

#define CLOCK_MCHP_XOSC_ID     MCHP_CLOCK_DERIVE_ID(0, 0x3f, 0x3f, 0x3f, 0)
#define CLOCK_MCHP_XOSC_ID_MAX (0)

#define CLOCK_MCHP_DFLL48M_ID     MCHP_CLOCK_DERIVE_ID(1, 0x3f, 0x3f, 0, 0)
#define CLOCK_MCHP_DFLL48M_ID_MAX (0)

#define CLOCK_MCHP_DPLL_ID_DPLL0 MCHP_CLOCK_DERIVE_ID(2, 0x3f, 0x3f, 1, 0)
#define CLOCK_MCHP_DPLL_ID_MAX   (0)

#define CLOCK_MCHP_DPLL0_ID_OUT0   MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 0)
#define CLOCK_MCHP_DPLL0_ID_OUT1   MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 1)
#define CLOCK_MCHP_DPLL0_ID_OUT2   MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 2)
#define CLOCK_MCHP_DPLL0_ID_OUT3   MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 3)
#define CLOCK_MCHP_DPLL0_ID_OUT4   MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 4)
#define CLOCK_MCHP_DPLL_OUT_ID_MAX (4)

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
#define CLOCK_MCHP_GCLKGEN_ID_MAX   (11)

#define CLOCK_MCHP_GCLKPERIPH_ID_FREQM_MSR0   MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 2, 0)
#define CLOCK_MCHP_GCLKPERIPH_ID_FREQM_MSR1   MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 3, 1)
#define CLOCK_MCHP_GCLKPERIPH_ID_FREQM_REF    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 4, 2)
#define CLOCK_MCHP_GCLKPERIPH_ID_EIC          MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 5, 3)
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN0         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 6, 4)
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN1         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 7, 5)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH0    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 8, 6)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH1    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 9, 7)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH2    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 10, 8)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH3    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 11, 9)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH4    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 12, 10)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH5    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 13, 11)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH6    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 14, 12)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH7    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 15, 13)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH8    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 16, 14)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH9    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 17, 15)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH10   MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 16)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH11   MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 19, 17)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 20, 18)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 20, 19)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 20, 20)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 20, 21)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 21, 22)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 22, 23)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 23, 24)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 24, 25)
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC0         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 25, 26)
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC1         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 25, 27)
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC2         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 26, 28)
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC3         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 27, 29)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM4_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 28, 30)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM5_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 29, 31)
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC4         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 30, 32)
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC5         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 31, 33)
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC6         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 32, 34)
#define CLOCK_MCHP_GCLKPERIPH_ID_ADC          MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 33, 35)
#define CLOCK_MCHP_GCLKPERIPH_ID_AC           MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 34, 36)
#define CLOCK_MCHP_GCLKPERIPH_ID_PTC          MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 35, 37)
#define CLOCK_MCHP_GCLKPERIPH_ID_CCL0         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 36, 38)
#define CLOCK_MCHP_GCLKPERIPH_ID_CCL1         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 37, 39)
#define CLOCK_MCHP_GCLKPERIPH_ID_USB          MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 38, 40)
#define CLOCK_MCHP_GCLKPERIPH_ID_MAX          (40)

#define CLOCK_MCHP_MCLKDOMAIN_ID_CPU MCHP_CLOCK_DERIVE_ID(8, 0x3f, 0x3f, 0x3f, 0)
#define CLOCK_MCHP_MCLKDOMAIN_MAX    (0)

#define CLOCK_MCHP_MCLKPERIPH_ID_DSU_AHB      MCHP_CLOCK_DERIVE_ID(9, 0, 0, 0x3f, 0)
#define CLOCK_MCHP_MCLKPERIPH_ID_FCR_AHB      MCHP_CLOCK_DERIVE_ID(9, 0, 1, 0x3f, 1)
#define CLOCK_MCHP_MCLKPERIPH_ID_FCW_AHB      MCHP_CLOCK_DERIVE_ID(9, 0, 2, 0x3f, 2)
#define CLOCK_MCHP_MCLKPERIPH_ID_PM           MCHP_CLOCK_DERIVE_ID(9, 0, 3, 0x3f, 3)
#define CLOCK_MCHP_MCLKPERIPH_ID_SUPC         MCHP_CLOCK_DERIVE_ID(9, 0, 4, 0x3f, 4)
#define CLOCK_MCHP_MCLKPERIPH_ID_RSTC         MCHP_CLOCK_DERIVE_ID(9, 0, 5, 0x3f, 5)
#define CLOCK_MCHP_MCLKPERIPH_ID_OSCCTRL      MCHP_CLOCK_DERIVE_ID(9, 0, 6, 0x3f, 6)
#define CLOCK_MCHP_MCLKPERIPH_ID_OSC32KCTRL   MCHP_CLOCK_DERIVE_ID(9, 0, 7, 0x3f, 7)
#define CLOCK_MCHP_MCLKPERIPH_ID_FREQM        MCHP_CLOCK_DERIVE_ID(9, 0, 10, 0x3f, 8)
#define CLOCK_MCHP_MCLKPERIPH_ID_WDT          MCHP_CLOCK_DERIVE_ID(9, 0, 11, 0x3f, 9)
#define CLOCK_MCHP_MCLKPERIPH_ID_RTC          MCHP_CLOCK_DERIVE_ID(9, 0, 12, 0x3f, 10)
#define CLOCK_MCHP_MCLKPERIPH_ID_EIC          MCHP_CLOCK_DERIVE_ID(9, 0, 13, 0x3f, 11)
#define CLOCK_MCHP_MCLKPERIPH_ID_PAC_APB      MCHP_CLOCK_DERIVE_ID(9, 0, 14, 0x3f, 12)
#define CLOCK_MCHP_MCLKPERIPH_ID_TRAM         MCHP_CLOCK_DERIVE_ID(9, 0, 15, 0x3f, 13)
#define CLOCK_MCHP_MCLKPERIPH_ID_MCRAMC_APB   MCHP_CLOCK_DERIVE_ID(9, 0, 21, 0x3f, 14)
#define CLOCK_MCHP_MCLKPERIPH_ID_MCRAMC_AHB   MCHP_CLOCK_DERIVE_ID(9, 0, 22, 0x3f, 15)
#define CLOCK_MCHP_MCLKPERIPH_ID_CAN0         MCHP_CLOCK_DERIVE_ID(9, 0, 23, 0x3f, 16)
#define CLOCK_MCHP_MCLKPERIPH_ID_CAN1         MCHP_CLOCK_DERIVE_ID(9, 0, 24, 0x3f, 17)
#define CLOCK_MCHP_MCLKPERIPH_ID_H2PB0_AHB    MCHP_CLOCK_DERIVE_ID(9, 0, 25, 0x3f, 18)
#define CLOCK_MCHP_MCLKPERIPH_ID_H2PB0_APB    MCHP_CLOCK_DERIVE_ID(9, 0, 26, 0x3f, 19)
#define CLOCK_MCHP_MCLKPERIPH_ID_PORT_APB     MCHP_CLOCK_DERIVE_ID(9, 0, 27, 0x3f, 20)
#define CLOCK_MCHP_MCLKPERIPH_ID_DMAC_AHB     MCHP_CLOCK_DERIVE_ID(9, 0, 28, 0x3f, 21)
#define CLOCK_MCHP_MCLKPERIPH_ID_DMAC_APB     MCHP_CLOCK_DERIVE_ID(9, 0, 29, 0x3f, 22)
#define CLOCK_MCHP_MCLKPERIPH_ID_HMATRIX2_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 30, 0x3f, 23)
#define CLOCK_MCHP_MCLKPERIPH_ID_HMATRIX2_APB MCHP_CLOCK_DERIVE_ID(9, 0, 31, 0x3f, 24)

#define CLOCK_MCHP_MCLKPERIPH_ID_BROMC_AHB MCHP_CLOCK_DERIVE_ID(9, 1, 0, 0x3f, 25)
#define CLOCK_MCHP_MCLKPERIPH_ID_BROMC_APB MCHP_CLOCK_DERIVE_ID(9, 1, 1, 0x3f, 26)
#define CLOCK_MCHP_MCLKPERIPH_ID_IDAU      MCHP_CLOCK_DERIVE_ID(9, 1, 2, 0x3f, 27)
#define CLOCK_MCHP_MCLKPERIPH_ID_EVSYS     MCHP_CLOCK_DERIVE_ID(9, 1, 3, 0x3f, 28)
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM0   MCHP_CLOCK_DERIVE_ID(9, 1, 4, 0x3f, 29)
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM1   MCHP_CLOCK_DERIVE_ID(9, 1, 5, 0x3f, 30)
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM2   MCHP_CLOCK_DERIVE_ID(9, 1, 6, 0x3f, 31)
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM3   MCHP_CLOCK_DERIVE_ID(9, 1, 7, 0x3f, 32)
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC0      MCHP_CLOCK_DERIVE_ID(9, 1, 8, 0x3f, 33)
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC1      MCHP_CLOCK_DERIVE_ID(9, 1, 9, 0x3f, 34)
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC2      MCHP_CLOCK_DERIVE_ID(9, 1, 10, 0x3f, 35)
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC3      MCHP_CLOCK_DERIVE_ID(9, 1, 11, 0x3f, 36)
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM4   MCHP_CLOCK_DERIVE_ID(9, 1, 12, 0x3f, 37)
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM5   MCHP_CLOCK_DERIVE_ID(9, 1, 13, 0x3f, 38)
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC4      MCHP_CLOCK_DERIVE_ID(9, 1, 14, 0x3f, 39)
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC5      MCHP_CLOCK_DERIVE_ID(9, 1, 15, 0x3f, 40)
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC6      MCHP_CLOCK_DERIVE_ID(9, 1, 16, 0x3f, 41)
#define CLOCK_MCHP_MCLKPERIPH_ID_ADC       MCHP_CLOCK_DERIVE_ID(9, 1, 17, 0x3f, 42)
#define CLOCK_MCHP_MCLKPERIPH_ID_AC        MCHP_CLOCK_DERIVE_ID(9, 1, 18, 0x3f, 43)
#define CLOCK_MCHP_MCLKPERIPH_ID_PTC       MCHP_CLOCK_DERIVE_ID(9, 1, 19, 0x3f, 44)
#define CLOCK_MCHP_MCLKPERIPH_ID_CCL0      MCHP_CLOCK_DERIVE_ID(9, 1, 20, 0x3f, 45)
#define CLOCK_MCHP_MCLKPERIPH_ID_CCL1      MCHP_CLOCK_DERIVE_ID(9, 1, 21, 0x3f, 46)
#define CLOCK_MCHP_MCLKPERIPH_ID_USB_AHB   MCHP_CLOCK_DERIVE_ID(9, 1, 22, 0x3f, 47)
#define CLOCK_MCHP_MCLKPERIPH_ID_USB_APB   MCHP_CLOCK_DERIVE_ID(9, 1, 23, 0x3f, 48)
#define CLOCK_MCHP_MCLKPERIPH_ID_AT        MCHP_CLOCK_DERIVE_ID(9, 1, 24, 0x3f, 49)
#define CLOCK_MCHP_MCLKPERIPH_ID_H2PB1_AHB MCHP_CLOCK_DERIVE_ID(9, 1, 25, 0x3f, 50)
#define CLOCK_MCHP_MCLKPERIPH_ID_H2PB1_APB MCHP_CLOCK_DERIVE_ID(9, 1, 26, 0x3f, 51)
#define CLOCK_MCHP_MCLKPERIPH_ID_H2PB2_AHB MCHP_CLOCK_DERIVE_ID(9, 1, 27, 0x3f, 52)
#define CLOCK_MCHP_MCLKPERIPH_ID_H2PB2_APB MCHP_CLOCK_DERIVE_ID(9, 1, 28, 0x3f, 53)
#define CLOCK_MCHP_MCLKPERIPH_ID_HSM       MCHP_CLOCK_DERIVE_ID(9, 1, 30, 0x3f, 54)
#define CLOCK_MCHP_MCLKPERIPH_ID_PUF       MCHP_CLOCK_DERIVE_ID(9, 1, 31, 0x3f, 55)

#define CLOCK_MCHP_MCLKPERIPH_ID_MAX (55)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MCHP_PIC32CM_SG_GC_CLOCK_H_ */
```

## 502.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Microchip Technology Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 386 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MCHP_PIC32CM_SG_GC_CLOCK_H_`。

## 502.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32cm__sg__gc__clock_8h.html)

---

[上一章](P501_mchp_pic32ck_sg_gc_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P503_mchp_pic32cz_ca_clock.h_源码浏览.md)
