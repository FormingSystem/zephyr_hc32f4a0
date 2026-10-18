---
id: learning.zephyr-docs.api-source-reference.page-501
title: mchp_pic32ck_sg_gc_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32ck__sg__gc__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第501章\_mchp\_pic32ck\_sg\_gc\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32ck__sg__gc__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32ck__sg__gc__clock_8h.html)。

## 501.1\_原始可见代码（Source Code）

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
<a id="l00113"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00133"></a>
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
<a id="l00165"></a>
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
<a id="l00293"></a>
<a id="l00295"></a>
<a id="l00297"></a>
<a id="l00303"></a>
<a id="l00305"></a>
<a id="l00307"></a>
<a id="l00309"></a>
<a id="l00311"></a>
<a id="l00313"></a>
<a id="l00315"></a>
<a id="l00317"></a>
<a id="l00319"></a>
<a id="l00321"></a>
<a id="l00323"></a>
<a id="l00325"></a>
<a id="l00327"></a>
<a id="l00329"></a>
<a id="l00331"></a>
<a id="l00333"></a>
<a id="l00335"></a>
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
<a id="l00365"></a>
<a id="l00367"></a>
<a id="l00369"></a>
<a id="l00371"></a>
<a id="l00373"></a>
<a id="l00375"></a>
<a id="l00377"></a>
<a id="l00379"></a>
<a id="l00381"></a>
<a id="l00383"></a>
<a id="l00385"></a>
<a id="l00387"></a>
<a id="l00389"></a>
<a id="l00391"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00396"></a>
<a id="l00398"></a>
<a id="l00400"></a>
<a id="l00402"></a>
<a id="l00404"></a>
<a id="l00406"></a>
<a id="l00408"></a>
<a id="l00410"></a>
<a id="l00412"></a>
<a id="l00414"></a>
<a id="l00416"></a>
<a id="l00418"></a>
<a id="l00420"></a>
<a id="l00422"></a>
<a id="l00424"></a>
<a id="l00426"></a>
<a id="l00428"></a>
<a id="l00430"></a>
<a id="l00432"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00437"></a>
<a id="l00439"></a>
<a id="l00440"></a>

```c
/*
 * Copyright (c) 2026 Microchip Technology Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef INCLUDE_ZEPHYR_DT_BINDINGS_CLOCK_MCHP_PIC32CK_SG_GC_CLOCK_H_
#define INCLUDE_ZEPHYR_DT_BINDINGS_CLOCK_MCHP_PIC32CK_SG_GC_CLOCK_H_

#define MCHP_CLOCK_DERIVE_ID(type, mclkmaskreg, mclkmaskbit, gclkperiph, inst)                     \
        (((type) << 26) | ((mclkmaskreg) << 20) | ((mclkmaskbit) << 14) | ((gclkperiph) << 8) |    \
         inst)

#define CLOCK_MCHP_XOSC_ID     MCHP_CLOCK_DERIVE_ID(0, 0x3f, 0x3f, 0x3f, 0)
#define CLOCK_MCHP_XOSC_ID_MAX (0)

#define CLOCK_MCHP_DFLL48M_ID     MCHP_CLOCK_DERIVE_ID(1, 0x3f, 0x3f, 0, 0)
#define CLOCK_MCHP_DFLL48M_ID_MAX (0)

#define CLOCK_MCHP_PLL_ID_PLL0 MCHP_CLOCK_DERIVE_ID(2, 0x3f, 0x3f, 0, 0)
#define CLOCK_MCHP_PLL_ID_MAX  (0)

#define CLOCK_MCHP_PLL0_ID_OUT0    MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 0)
#define CLOCK_MCHP_PLL0_ID_OUT1    MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 1)
#define CLOCK_MCHP_PLL0_ID_OUT2    MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 2)
#define CLOCK_MCHP_PLL0_ID_OUT3    MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 3)
#define CLOCK_MCHP_PLL0_ID_OUT4    MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 4)
#define CLOCK_MCHP_PLL0_ID_OUT5    MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 5)
#define CLOCK_MCHP_PLL0_OUT_ID_MAX (5)

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
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH0    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 6, 4)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH1    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 7, 5)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH2    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 8, 6)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH3    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 9, 7)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH4    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 10, 8)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH5    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 11, 9)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH6    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 12, 10)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH7    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 13, 11)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH8    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 14, 12)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH9    MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 15, 13)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH10   MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 16, 14)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH11   MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 17, 15)
#define CLOCK_MCHP_GCLKPERIPH_ID_SDMMC0_SLOW  MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 16)
#define CLOCK_MCHP_GCLKPERIPH_ID_SDMMC1_SLOW  MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 17)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 18)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 19)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM4_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 20)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 21)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 22)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM5_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 23)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM6_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 24)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM7_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 25)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 19, 26)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 20, 27)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 21, 28)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 22, 29)
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC0         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 23, 30)
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC1         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 23, 31)
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC2         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 24, 32)
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC3         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 24, 33)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM4_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 25, 34)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM5_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 26, 35)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM6_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 27, 36)
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM7_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 28, 37)
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC4         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 29, 38)
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC5         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 30, 39)
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC6         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 31, 40)
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC7         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 32, 41)
#define CLOCK_MCHP_GCLKPERIPH_ID_ADC          MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 33, 42)
#define CLOCK_MCHP_GCLKPERIPH_ID_AC           MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 34, 43)
#define CLOCK_MCHP_GCLKPERIPH_ID_PTC          MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 35, 44)
#define CLOCK_MCHP_GCLKPERIPH_ID_SPI_IXS      MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 36, 45)
#define CLOCK_MCHP_GCLKPERIPH_ID_CCL          MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 37, 46)
#define CLOCK_MCHP_GCLKPERIPH_ID_PDEC         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 38, 47)
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN0         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 39, 48)
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN1         MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 40, 49)
#define CLOCK_MCHP_GCLKPERIPH_ID_ETH_TX       MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 41, 50)
#define CLOCK_MCHP_GCLKPERIPH_ID_ETH_TSU      MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 42, 51)
#define CLOCK_MCHP_GCLKPERIPH_ID_SQI          MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 43, 52)
#define CLOCK_MCHP_GCLKPERIPH_ID_SDMMC0       MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 44, 53)
#define CLOCK_MCHP_GCLKPERIPH_ID_SDMMC1       MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 45, 54)
#define CLOCK_MCHP_GCLKPERIPH_ID_USB          MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 46, 55)
#define CLOCK_MCHP_GCLKPERIPH_ID_CPU0_TRACE   MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 47, 56)
#define CLOCK_MCHP_GCLKPERIPH_ID_MAX          (56)

#define CLOCK_MCHP_MCLKCPU_ID  MCHP_CLOCK_DERIVE_ID(8, 0x3f, 0x3f, 0x3f, 0)
#define CLOCK_MCHP_MCLKCPU_MAX (0)

#define CLOCK_MCHP_MCLKPERIPH_ID_DSU_AHB    MCHP_CLOCK_DERIVE_ID(9, 0, 3, 0x3f, 0)
#define CLOCK_MCHP_MCLKPERIPH_ID_FCR_AHB    MCHP_CLOCK_DERIVE_ID(9, 0, 4, 0x3f, 1)
#define CLOCK_MCHP_MCLKPERIPH_ID_FCW_AHB    MCHP_CLOCK_DERIVE_ID(9, 0, 5, 0x3f, 2)
#define CLOCK_MCHP_MCLKPERIPH_ID_PAC_AHB    MCHP_CLOCK_DERIVE_ID(9, 0, 6, 0x3f, 3)
#define CLOCK_MCHP_MCLKPERIPH_ID_DMA0_AHB   MCHP_CLOCK_DERIVE_ID(9, 0, 8, 0x3f, 4)
#define CLOCK_MCHP_MCLKPERIPH_ID_DMA1_AHB   MCHP_CLOCK_DERIVE_ID(9, 0, 9, 0x3f, 5)
#define CLOCK_MCHP_MCLKPERIPH_ID_PRM_AHB    MCHP_CLOCK_DERIVE_ID(9, 0, 12, 0x3f, 6)
#define CLOCK_MCHP_MCLKPERIPH_ID_CAN0_AHB   MCHP_CLOCK_DERIVE_ID(9, 0, 13, 0x3f, 7)
#define CLOCK_MCHP_MCLKPERIPH_ID_CAN1_AHB   MCHP_CLOCK_DERIVE_ID(9, 0, 14, 0x3f, 8)
#define CLOCK_MCHP_MCLKPERIPH_ID_ETH_AHB    MCHP_CLOCK_DERIVE_ID(9, 0, 15, 0x3f, 9)
#define CLOCK_MCHP_MCLKPERIPH_ID_SQI_AHB    MCHP_CLOCK_DERIVE_ID(9, 0, 16, 0x3f, 10)
#define CLOCK_MCHP_MCLKPERIPH_ID_SDMMC0_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 17, 0x3f, 11)
#define CLOCK_MCHP_MCLKPERIPH_ID_SDMMC1_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 18, 0x3f, 12)
#define CLOCK_MCHP_MCLKPERIPH_ID_USBFS_AHB  MCHP_CLOCK_DERIVE_ID(9, 0, 19, 0x3f, 13)
#define CLOCK_MCHP_MCLKPERIPH_ID_USBHS_AHB  MCHP_CLOCK_DERIVE_ID(9, 0, 20, 0x3f, 14)
#define CLOCK_MCHP_MCLKPERIPH_ID_EBI_AHB    MCHP_CLOCK_DERIVE_ID(9, 0, 21, 0x3f, 15)
#define CLOCK_MCHP_MCLKPERIPH_ID_HSM_AHB    MCHP_CLOCK_DERIVE_ID(9, 0, 22, 0x3f, 16)

#define CLOCK_MCHP_MCLKPERIPH_ID_DSU_APB        MCHP_CLOCK_DERIVE_ID(9, 1, 0, 0x3f, 17)
#define CLOCK_MCHP_MCLKPERIPH_ID_FCR_APB        MCHP_CLOCK_DERIVE_ID(9, 1, 1, 0x3f, 18)
#define CLOCK_MCHP_MCLKPERIPH_ID_FCW_APB        MCHP_CLOCK_DERIVE_ID(9, 1, 2, 0x3f, 19)
#define CLOCK_MCHP_MCLKPERIPH_ID_RSTC_APB       MCHP_CLOCK_DERIVE_ID(9, 1, 5, 0x3f, 20)
#define CLOCK_MCHP_MCLKPERIPH_ID_OSCCTRL_APB    MCHP_CLOCK_DERIVE_ID(9, 1, 6, 0x3f, 21)
#define CLOCK_MCHP_MCLKPERIPH_ID_OSC32KCTRL_APB MCHP_CLOCK_DERIVE_ID(9, 1, 7, 0x3f, 22)
#define CLOCK_MCHP_MCLKPERIPH_ID_FREQM_APB      MCHP_CLOCK_DERIVE_ID(9, 1, 10, 0x3f, 23)
#define CLOCK_MCHP_MCLKPERIPH_ID_WDT_APB        MCHP_CLOCK_DERIVE_ID(9, 1, 11, 0x3f, 24)
#define CLOCK_MCHP_MCLKPERIPH_ID_RTC_APB        MCHP_CLOCK_DERIVE_ID(9, 1, 12, 0x3f, 25)
#define CLOCK_MCHP_MCLKPERIPH_ID_EIC_APB        MCHP_CLOCK_DERIVE_ID(9, 1, 13, 0x3f, 26)
#define CLOCK_MCHP_MCLKPERIPH_ID_PAC_APB        MCHP_CLOCK_DERIVE_ID(9, 1, 14, 0x3f, 27)
#define CLOCK_MCHP_MCLKPERIPH_ID_TRAM_APB       MCHP_CLOCK_DERIVE_ID(9, 1, 15, 0x3f, 28)
#define CLOCK_MCHP_MCLKPERIPH_ID_MBISTINTF_APB  MCHP_CLOCK_DERIVE_ID(9, 1, 18, 0x3f, 29)
#define CLOCK_MCHP_MCLKPERIPH_ID_TDM_APB        MCHP_CLOCK_DERIVE_ID(9, 1, 19, 0x3f, 30)

#define CLOCK_MCHP_MCLKPERIPH_ID_PORT_APB    MCHP_CLOCK_DERIVE_ID(9, 2, 0, 0x3f, 31)
#define CLOCK_MCHP_MCLKPERIPH_ID_DMA0_APB    MCHP_CLOCK_DERIVE_ID(9, 2, 1, 0x3f, 32)
#define CLOCK_MCHP_MCLKPERIPH_ID_DMA1_APB    MCHP_CLOCK_DERIVE_ID(9, 2, 2, 0x3f, 33)
#define CLOCK_MCHP_MCLKPERIPH_ID_PRM_APB     MCHP_CLOCK_DERIVE_ID(9, 2, 4, 0x3f, 34)
#define CLOCK_MCHP_MCLKPERIPH_ID_IDAU_APB    MCHP_CLOCK_DERIVE_ID(9, 2, 5, 0x3f, 35)
#define CLOCK_MCHP_MCLKPERIPH_ID_EVSYS_APB   MCHP_CLOCK_DERIVE_ID(9, 2, 6, 0x3f, 36)
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM0_APB MCHP_CLOCK_DERIVE_ID(9, 2, 7, 0x3f, 37)
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM1_APB MCHP_CLOCK_DERIVE_ID(9, 2, 8, 0x3f, 38)
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM2_APB MCHP_CLOCK_DERIVE_ID(9, 2, 9, 0x3f, 39)
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM3_APB MCHP_CLOCK_DERIVE_ID(9, 2, 10, 0x3f, 40)
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC0_APB    MCHP_CLOCK_DERIVE_ID(9, 2, 11, 0x3f, 41)
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC1_APB    MCHP_CLOCK_DERIVE_ID(9, 2, 12, 0x3f, 42)
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC2_APB    MCHP_CLOCK_DERIVE_ID(9, 2, 13, 0x3f, 43)
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC3_APB    MCHP_CLOCK_DERIVE_ID(9, 2, 14, 0x3f, 44)

#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM4_APB MCHP_CLOCK_DERIVE_ID(9, 3, 0, 0x3f, 45)
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM5_APB MCHP_CLOCK_DERIVE_ID(9, 3, 1, 0x3f, 46)
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM6_APB MCHP_CLOCK_DERIVE_ID(9, 3, 2, 0x3f, 47)
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM7_APB MCHP_CLOCK_DERIVE_ID(9, 3, 3, 0x3f, 48)
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC4_APB    MCHP_CLOCK_DERIVE_ID(9, 3, 4, 0x3f, 49)
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC5_APB    MCHP_CLOCK_DERIVE_ID(9, 3, 5, 0x3f, 50)
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC6_APB    MCHP_CLOCK_DERIVE_ID(9, 3, 6, 0x3f, 51)
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC7_APB    MCHP_CLOCK_DERIVE_ID(9, 3, 7, 0x3f, 52)
#define CLOCK_MCHP_MCLKPERIPH_ID_ADC_APB     MCHP_CLOCK_DERIVE_ID(9, 3, 8, 0x3f, 53)
#define CLOCK_MCHP_MCLKPERIPH_ID_AC_APB      MCHP_CLOCK_DERIVE_ID(9, 3, 9, 0x3f, 54)
#define CLOCK_MCHP_MCLKPERIPH_ID_PTC_APB     MCHP_CLOCK_DERIVE_ID(9, 3, 10, 0x3f, 55)
#define CLOCK_MCHP_MCLKPERIPH_ID_I2S_APB     MCHP_CLOCK_DERIVE_ID(9, 3, 11, 0x3f, 56)
#define CLOCK_MCHP_MCLKPERIPH_ID_PCC_APB     MCHP_CLOCK_DERIVE_ID(9, 3, 12, 0x3f, 57)
#define CLOCK_MCHP_MCLKPERIPH_ID_CCL_APB     MCHP_CLOCK_DERIVE_ID(9, 3, 13, 0x3f, 58)
#define CLOCK_MCHP_MCLKPERIPH_ID_PDEC_APB    MCHP_CLOCK_DERIVE_ID(9, 3, 14, 0x3f, 59)
#define CLOCK_MCHP_MCLKPERIPH_ID_ETH_APB     MCHP_CLOCK_DERIVE_ID(9, 3, 15, 0x3f, 60)
#define CLOCK_MCHP_MCLKPERIPH_ID_TRNG_APB    MCHP_CLOCK_DERIVE_ID(9, 3, 16, 0x3f, 61)
#define CLOCK_MCHP_MCLKPERIPH_ID_USB_APB     MCHP_CLOCK_DERIVE_ID(9, 3, 17, 0x3f, 62)
#define CLOCK_MCHP_MCLKPERIPH_ID_EBI_APB     MCHP_CLOCK_DERIVE_ID(9, 3, 18, 0x3f, 63)
#define CLOCK_MCHP_MCLKPERIPH_ID_BSDAP_AHB   MCHP_CLOCK_DERIVE_ID(9, 3, 19, 0x3f, 64)

#define CLOCK_MCHP_MCLKPERIPH_ID_MAX (64)

#endif /* INCLUDE_ZEPHYR_DT_BINDINGS_CLOCK_MCHP_PIC32CK_SG_GC_CLOCK_H_ */
```

## 501.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Microchip Technology Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 440 行

头文件保护宏（Header guard）标记：`INCLUDE_ZEPHYR_DT_BINDINGS_CLOCK_MCHP_PIC32CK_SG_GC_CLOCK_H_`。

## 501.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32ck__sg__gc__clock_8h.html)

---

[上一章](P500_mchp_nvmctrl_g3.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P502_mchp_pic32cm_sg_gc_clock.h_源码浏览.md)
