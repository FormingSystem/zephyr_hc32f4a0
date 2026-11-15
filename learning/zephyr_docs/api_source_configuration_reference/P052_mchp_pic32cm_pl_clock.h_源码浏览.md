---
id: learning.zephyr-docs.api-source-configuration-reference.page-52
title: mchp_pic32cm_pl_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32cm__pl__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第52章\_mchp\_pic32cm\_pl\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32cm__pl__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32cm__pl__clock_8h.html)。

## 52.1\_原始可见代码（Source Code）

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
<a id="l00017"></a>
<a id="l00019"></a>
<a id="l00021"></a>
<a id="l00023"></a>
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="foldopen00094"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="foldopen00108"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="foldopen00111"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="foldopen00117"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="foldopen00120"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="foldopen00141"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="foldopen00144"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="foldopen00147"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="foldopen00150"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="foldopen00153"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="foldopen00156"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="foldopen00159"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="foldopen00162"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="foldopen00165"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="foldopen00168"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="foldopen00171"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="foldopen00174"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00183"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="foldopen00189"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="foldopen00192"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="foldopen00195"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="foldopen00198"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="foldopen00201"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="foldopen00204"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="foldopen00207"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="foldopen00210"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="foldopen00213"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="foldopen00216"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="foldopen00220"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="foldopen00223"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="foldopen00226"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="foldopen00229"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="foldopen00232"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="foldopen00235"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="foldopen00238"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="foldopen00241"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="foldopen00244"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="foldopen00247"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="foldopen00250"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="foldopen00254"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="foldopen00257"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="foldopen00260"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="foldopen00263"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="foldopen00266"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="foldopen00269"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="foldopen00273"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="foldopen00276"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="foldopen00279"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="foldopen00282"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="foldopen00285"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="foldopen00288"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="foldopen00291"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="foldopen00294"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="foldopen00297"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="foldopen00300"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="foldopen00303"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="foldopen00306"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>

```c
/*
 * Copyright (c) 2026 Microchip Technology Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MCHP_PIC32CM_PL_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MCHP_PIC32CM_PL_CLOCK_H_

/* Clock subsystem Types */
#define SUBSYS_TYPE_OSCHF      (0)
#define SUBSYS_TYPE_RTC        (1)
#define SUBSYS_TYPE_XOSC32K    (2)
#define SUBSYS_TYPE_OSC32K     (3)
#define SUBSYS_TYPE_GCLKGEN    (4)
#define SUBSYS_TYPE_GCLKPERIPH (5)
#define SUBSYS_TYPE_MCLKCPU    (6)
#define SUBSYS_TYPE_MCLKPERIPH (7)
#define SUBSYS_TYPE_MAX        (7)

#define MBUS_AHB  (0)
#define MBUS_APBA (1)
#define MBUS_APBB (2)
#define MBUS_APBC (3)
#define MBUS_MAX  (3)

#define INST_XOSC32K_XOSC1K  0
#define INST_XOSC32K_XOSC32K 1

#define INST_OSC32K_OSC1K  0
#define INST_OSC32K_OSC32K 1

#define MCHP_CLOCK_DERIVE_ID(type, mclkbus, mclkmaskbit, gclkperiph, inst)                         \
        (((type) << 26) | ((mclkbus) << 20) | ((mclkmaskbit) << 14) | ((gclkperiph) << 8) | inst)

#define CLOCK_MCHP_OSCHF_ID     MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_OSCHF, 0x3f, 0x3f, 0x3f, 0)
#define CLOCK_MCHP_OSCHF_ID_MAX (0)

#define CLOCK_MCHP_RTC_ID     MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_RTC, 0x3f, 0x3f, 0x3f, 0)
#define CLOCK_MCHP_RTC_ID_MAX (0)

#define CLOCK_MCHP_XOSC32K_ID_XOSC1K                                                               \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_XOSC32K, 0x3f, 0x3f, 0x3f, INST_XOSC32K_XOSC1K)

#define CLOCK_MCHP_XOSC32K_ID_XOSC32K                                                              \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_XOSC32K, 0x3f, 0x3f, 0x3f, INST_XOSC32K_XOSC32K)

#define CLOCK_MCHP_XOSC32K_ID_MAX (1)

#define CLOCK_MCHP_OSC32K_ID_OSC1K                                                                 \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_OSC32K, 0x3f, 0x3f, 0x3f, INST_OSC32K_OSC1K)

#define CLOCK_MCHP_OSC32K_ID_OSC32K                                                                \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_OSC32K, 0x3f, 0x3f, 0x3f, INST_OSC32K_OSC32K)

#define CLOCK_MCHP_OSC32K_ID_MAX (1)

#define CLOCK_MCHP_GCLKGEN_ID_GEN0 MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_GCLKGEN, 0x3f, 0x3f, 0x3f, 0)
#define CLOCK_MCHP_GCLKGEN_ID_GEN1 MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_GCLKGEN, 0x3f, 0x3f, 0x3f, 1)
#define CLOCK_MCHP_GCLKGEN_ID_GEN2 MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_GCLKGEN, 0x3f, 0x3f, 0x3f, 2)
#define CLOCK_MCHP_GCLKGEN_ID_GEN3 MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_GCLKGEN, 0x3f, 0x3f, 0x3f, 3)
#define CLOCK_MCHP_GCLKGEN_ID_MAX  (3)
#define GCLK_IO_MAX                CLOCK_MCHP_GCLKGEN_ID_MAX

#define CLOCK_MCHP_GCLKPERIPH_ID_EIC MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_GCLKPERIPH, 0x3f, 0x3f, 0, 0)
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CHANNEL_0                                                   \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_GCLKPERIPH, 0x3f, 0x3f, 1, 1)

#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CHANNEL_1                                                   \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_GCLKPERIPH, 0x3f, 0x3f, 2, 2)

#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CHANNEL_2                                                   \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_GCLKPERIPH, 0x3f, 0x3f, 3, 3)

#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CHANNEL_3                                                   \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_GCLKPERIPH, 0x3f, 0x3f, 4, 4)

#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_SLOW                                                      \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_GCLKPERIPH, 0x3f, 0x3f, 5, 5)

#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_CORE                                                      \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_GCLKPERIPH, 0x3f, 0x3f, 6, 6)

#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_SLOW                                                      \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_GCLKPERIPH, 0x3f, 0x3f, 7, 7)

#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_CORE                                                      \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_GCLKPERIPH, 0x3f, 0x3f, 8, 8)

#define CLOCK_MCHP_GCLKPERIPH_ID_TC0_TC1                                                           \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_GCLKPERIPH, 0x3f, 0x3f, 9, 9)

#define CLOCK_MCHP_GCLKPERIPH_ID_TC2                                                               \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_GCLKPERIPH, 0x3f, 0x3f, 10, 10)

#define CLOCK_MCHP_GCLKPERIPH_ID_TCC0                                                              \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_GCLKPERIPH, 0x3f, 0x3f, 11, 11)

#define CLOCK_MCHP_GCLKPERIPH_ID_CCL                                                               \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_GCLKPERIPH, 0x3f, 0x3f, 12, 12)

#define CLOCK_MCHP_GCLKPERIPH_ID_MAX (12)

#define GCLK_PH_MAX CLOCK_MCHP_GCLKPERIPH_ID_MAX

#define CLOCK_MCHP_MCLKCPU_ID  MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKCPU, 0x3f, 0x3f, 0x3f, 0)
#define CLOCK_MCHP_MCLKCPU_MAX (0)

/* MCLKPERIPH_TYPE ids */
#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_APBA                                                          \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_AHB, 0, 0x3f, 0)

#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_APBB                                                          \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_AHB, 1, 0x3f, 1)

#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_APBC                                                          \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_AHB, 2, 0x3f, 2)

#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_DSU                                                           \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_AHB, 3, 0x3f, 3)

#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_HMATRIXHS                                                     \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_AHB, 4, 0x3f, 4)

#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_NVMCTRL                                                       \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_AHB, 5, 0x3f, 5)

#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_HSRAM                                                         \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_AHB, 6, 0x3f, 6)

#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_DMAC                                                          \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_AHB, 7, 0x3f, 7)

#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_PAC                                                           \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_AHB, 8, 0x3f, 8)

#define CLOCK_MCHP_MCLKPERIPH_ID_AHB_BROM                                                          \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_AHB, 9, 0x3f, 9)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_PAC                                                          \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_APBA, 0, 0x3f, 10)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_PM                                                           \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_APBA, 1, 0x3f, 11)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_MCLK                                                         \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_APBA, 2, 0x3f, 12)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_RSTC                                                         \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_APBA, 3, 0x3f, 13)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_OSCCTRL                                                      \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_APBA, 4, 0x3f, 14)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_OSC32KCTRL                                                   \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_APBA, 5, 0x3f, 15)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_SUPC                                                         \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_APBA, 6, 0x3f, 16)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_GCLK                                                         \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_APBA, 7, 0x3f, 17)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_WDT                                                          \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_APBA, 8, 0x3f, 18)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_RTC                                                          \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_APBA, 9, 0x3f, 19)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBA_EIC                                                          \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_APBA, 10, 0x3f, 20)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBB_PORT                                                         \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_APBB, 0, 0x3f, 21)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBB_DSU                                                          \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_APBB, 1, 0x3f, 22)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBB_NVMCTRL                                                      \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_APBB, 2, 0x3f, 23)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBB_DMAC                                                         \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_APBB, 3, 0x3f, 24)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBB_MTB                                                          \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_APBB, 4, 0x3f, 25)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBB_HMATRIXHS                                                    \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_APBB, 5, 0x3f, 26)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_EVSYS                                                        \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_APBC, 0, 0x3f, 27)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_SERCOM0                                                      \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_APBC, 1, 0x3f, 28)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_SERCOM1                                                      \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_APBC, 2, 0x3f, 29)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_TC0                                                          \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_APBC, 3, 0x3f, 30)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_TC1                                                          \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_APBC, 4, 0x3f, 31)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_TC2                                                          \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_APBC, 5, 0x3f, 32)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_TCC0                                                         \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_APBC, 6, 0x3f, 33)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_ADC0                                                         \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_APBC, 7, 0x3f, 34)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_AC                                                           \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_APBC, 8, 0x3f, 35)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_CCL                                                          \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_APBC, 9, 0x3f, 36)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_PTC                                                          \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_APBC, 10, 0x3f, 37)

#define CLOCK_MCHP_MCLKPERIPH_ID_APBC_SYSCTRL                                                      \
        MCHP_CLOCK_DERIVE_ID(SUBSYS_TYPE_MCLKPERIPH, MBUS_APBC, 11, 0x3f, 38)

#define CLOCK_MCHP_MCLKPERIPH_ID_MAX (38)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MCHP_PIC32CM_PL_CLOCK_H_ */
```

## 52.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Microchip Technology Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 17 行

时钟子系统类型（Clock subsystem Types）。

### 注释 3：原第 187 行

`MCLKPERIPH_TYPE` 标识符（IDs）。

### 注释 4：原第 311 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MCHP_PIC32CM_PL_CLOCK_H_`。

## 52.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32cm__pl__clock_8h.html)

---

[上一章](P051_max32-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P053_mchp_xec_clock_control.h_源码浏览.md)
