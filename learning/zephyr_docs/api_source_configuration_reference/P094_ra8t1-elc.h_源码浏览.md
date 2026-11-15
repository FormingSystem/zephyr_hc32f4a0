---
id: learning.zephyr-docs.api-source-configuration-reference.page-94
title: ra8t1-elc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ra8t1-elc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第94章\_ra8t1-elc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ra8t1-elc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ra8t1-elc_8h.html)。

## 94.1\_原始可见代码（Source Code）

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
<a id="l00020"></a>
<a id="l00053"></a>
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
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00384"></a>
<a id="l00386"></a>
<a id="l00387"></a>

```c
/*
 * Copyright (c) 2025 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_MISC_RENESAS_RA_ELC_RA8T1_ELC_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_MISC_RENESAS_RA_ELC_RA8T1_ELC_H_




/* Event codes for Renesas RA8T1 Event Link Controller (ELC). */
#define RA_ELC_EVENT_NONE                    0x0
#define RA_ELC_EVENT_ICU_IRQ0                0x001
#define RA_ELC_EVENT_ICU_IRQ1                0x002
#define RA_ELC_EVENT_ICU_IRQ2                0x003
#define RA_ELC_EVENT_ICU_IRQ3                0x004
#define RA_ELC_EVENT_ICU_IRQ4                0x005
#define RA_ELC_EVENT_ICU_IRQ5                0x006
#define RA_ELC_EVENT_ICU_IRQ6                0x007
#define RA_ELC_EVENT_ICU_IRQ7                0x008
#define RA_ELC_EVENT_ICU_IRQ8                0x009
#define RA_ELC_EVENT_ICU_IRQ9                0x00A
#define RA_ELC_EVENT_ICU_IRQ10               0x00B
#define RA_ELC_EVENT_ICU_IRQ11               0x00C
#define RA_ELC_EVENT_ICU_IRQ12               0x00D
#define RA_ELC_EVENT_ICU_IRQ13               0x00E
#define RA_ELC_EVENT_ICU_IRQ14               0x00F
#define RA_ELC_EVENT_ICU_IRQ15               0x010
#define RA_ELC_EVENT_DMAC0_INT               0x011
#define RA_ELC_EVENT_DMAC1_INT               0x012
#define RA_ELC_EVENT_DMAC2_INT               0x013
#define RA_ELC_EVENT_DMAC3_INT               0x014
#define RA_ELC_EVENT_DMAC4_INT               0x015
#define RA_ELC_EVENT_DMAC5_INT               0x016
#define RA_ELC_EVENT_DMAC6_INT               0x017
#define RA_ELC_EVENT_DMAC7_INT               0x018
#define RA_ELC_EVENT_DTC_END                 0x021
#define RA_ELC_EVENT_DTC_COMPLETE            0x022
#define RA_ELC_EVENT_DMA_TRANSERR            0x027
#define RA_ELC_EVENT_DBG_CTIIRQ0             0x029
#define RA_ELC_EVENT_DBG_CTIIRQ1             0x02A
#define RA_ELC_EVENT_DBG_JBRXI               0x02B
#define RA_ELC_EVENT_FCU_FIFERR              0x030
#define RA_ELC_EVENT_FCU_FRDYI               0x031
#define RA_ELC_EVENT_LVD_LVD1                0x038
#define RA_ELC_EVENT_LVD_LVD2                0x039
#define RA_ELC_EVENT_CGC_MOSC_STOP           0x03E
#define RA_ELC_EVENT_ULPT0_INT               0x040
#define RA_ELC_EVENT_ULPT0_COMPARE_A         0x041
#define RA_ELC_EVENT_ULPT0_COMPARE_B         0x042
#define RA_ELC_EVENT_ULPT1_INT               0x043
#define RA_ELC_EVENT_ULPT1_COMPARE_A         0x044
#define RA_ELC_EVENT_ULPT1_COMPARE_B         0x045
#define RA_ELC_EVENT_AGT0_INT                0x046
#define RA_ELC_EVENT_AGT0_COMPARE_A          0x047
#define RA_ELC_EVENT_AGT0_COMPARE_B          0x048
#define RA_ELC_EVENT_AGT1_INT                0x049
#define RA_ELC_EVENT_AGT1_COMPARE_A          0x04A
#define RA_ELC_EVENT_AGT1_COMPARE_B          0x04B
#define RA_ELC_EVENT_IWDT_UNDERFLOW          0x052
#define RA_ELC_EVENT_WDT0_UNDERFLOW          0x053
#define RA_ELC_EVENT_USBFS_FIFO_0            0x058
#define RA_ELC_EVENT_USBFS_FIFO_1            0x059
#define RA_ELC_EVENT_USBFS_INT               0x05A
#define RA_ELC_EVENT_USBFS_RESUME            0x05B
#define RA_ELC_EVENT_IIC0_RXI                0x05C
#define RA_ELC_EVENT_IIC0_TXI                0x05D
#define RA_ELC_EVENT_IIC0_TEI                0x05E
#define RA_ELC_EVENT_IIC0_ERI                0x05F
#define RA_ELC_EVENT_IIC0_WUI                0x060
#define RA_ELC_EVENT_IIC1_RXI                0x061
#define RA_ELC_EVENT_IIC1_TXI                0x062
#define RA_ELC_EVENT_IIC1_TEI                0x063
#define RA_ELC_EVENT_IIC1_ERI                0x064
#define RA_ELC_EVENT_SDHIMMC0_ACCS           0x06B
#define RA_ELC_EVENT_SDHIMMC0_SDIO           0x06C
#define RA_ELC_EVENT_SDHIMMC0_CARD           0x06D
#define RA_ELC_EVENT_SDHIMMC0_DMA_REQ        0x06E
#define RA_ELC_EVENT_SDHIMMC1_ACCS           0x06F
#define RA_ELC_EVENT_SDHIMMC1_SDIO           0x070
#define RA_ELC_EVENT_SDHIMMC1_CARD           0x071
#define RA_ELC_EVENT_SDHIMMC1_DMA_REQ        0x072
#define RA_ELC_EVENT_ACMPHS0_INT             0x07B
#define RA_ELC_EVENT_ACMPHS1_INT             0x07C
#define RA_ELC_EVENT_ELC_SOFTWARE_EVENT_0    0x083
#define RA_ELC_EVENT_ELC_SOFTWARE_EVENT_1    0x084
#define RA_ELC_EVENT_IOPORT_EVENT_1          0x088
#define RA_ELC_EVENT_IOPORT_EVENT_2          0x089
#define RA_ELC_EVENT_IOPORT_EVENT_3          0x08A
#define RA_ELC_EVENT_IOPORT_EVENT_4          0x08B
#define RA_ELC_EVENT_CAC_FREQUENCY_ERROR     0x08C
#define RA_ELC_EVENT_CAC_MEASUREMENT_END     0x08D
#define RA_ELC_EVENT_CAC_OVERFLOW            0x08E
#define RA_ELC_EVENT_POEG0_EVENT             0x08F
#define RA_ELC_EVENT_POEG1_EVENT             0x090
#define RA_ELC_EVENT_POEG2_EVENT             0x091
#define RA_ELC_EVENT_POEG3_EVENT             0x092
#define RA_ELC_EVENT_OPS_UVW_EDGE            0x0A0
#define RA_ELC_EVENT_GPT0_CAPTURE_COMPARE_A  0x0A1
#define RA_ELC_EVENT_GPT0_CAPTURE_COMPARE_B  0x0A2
#define RA_ELC_EVENT_GPT0_COMPARE_C          0x0A3
#define RA_ELC_EVENT_GPT0_COMPARE_D          0x0A4
#define RA_ELC_EVENT_GPT0_COMPARE_E          0x0A5
#define RA_ELC_EVENT_GPT0_COMPARE_F          0x0A6
#define RA_ELC_EVENT_GPT0_COUNTER_OVERFLOW   0x0A7
#define RA_ELC_EVENT_GPT0_COUNTER_UNDERFLOW  0x0A8
#define RA_ELC_EVENT_GPT0_PC                 0x0A9
#define RA_ELC_EVENT_GPT1_CAPTURE_COMPARE_A  0x0AA
#define RA_ELC_EVENT_GPT1_CAPTURE_COMPARE_B  0x0AB
#define RA_ELC_EVENT_GPT1_COMPARE_C          0x0AC
#define RA_ELC_EVENT_GPT1_COMPARE_D          0x0AD
#define RA_ELC_EVENT_GPT1_COMPARE_E          0x0AE
#define RA_ELC_EVENT_GPT1_COMPARE_F          0x0AF
#define RA_ELC_EVENT_GPT1_COUNTER_OVERFLOW   0x0B0
#define RA_ELC_EVENT_GPT1_COUNTER_UNDERFLOW  0x0B1
#define RA_ELC_EVENT_GPT1_PC                 0x0B2
#define RA_ELC_EVENT_GPT2_CAPTURE_COMPARE_A  0x0B3
#define RA_ELC_EVENT_GPT2_CAPTURE_COMPARE_B  0x0B4
#define RA_ELC_EVENT_GPT2_COMPARE_C          0x0B5
#define RA_ELC_EVENT_GPT2_COMPARE_D          0x0B6
#define RA_ELC_EVENT_GPT2_COMPARE_E          0x0B7
#define RA_ELC_EVENT_GPT2_COMPARE_F          0x0B8
#define RA_ELC_EVENT_GPT2_COUNTER_OVERFLOW   0x0B9
#define RA_ELC_EVENT_GPT2_COUNTER_UNDERFLOW  0x0BA
#define RA_ELC_EVENT_GPT2_PC                 0x0BB
#define RA_ELC_EVENT_GPT3_CAPTURE_COMPARE_A  0x0BC
#define RA_ELC_EVENT_GPT3_CAPTURE_COMPARE_B  0x0BD
#define RA_ELC_EVENT_GPT3_COMPARE_C          0x0BE
#define RA_ELC_EVENT_GPT3_COMPARE_D          0x0BF
#define RA_ELC_EVENT_GPT3_COMPARE_E          0x0C0
#define RA_ELC_EVENT_GPT3_COMPARE_F          0x0C1
#define RA_ELC_EVENT_GPT3_COUNTER_OVERFLOW   0x0C2
#define RA_ELC_EVENT_GPT3_COUNTER_UNDERFLOW  0x0C3
#define RA_ELC_EVENT_GPT3_PC                 0x0C4
#define RA_ELC_EVENT_GPT4_CAPTURE_COMPARE_A  0x0C5
#define RA_ELC_EVENT_GPT4_CAPTURE_COMPARE_B  0x0C6
#define RA_ELC_EVENT_GPT4_COMPARE_C          0x0C7
#define RA_ELC_EVENT_GPT4_COMPARE_D          0x0C8
#define RA_ELC_EVENT_GPT4_COMPARE_E          0x0C9
#define RA_ELC_EVENT_GPT4_COMPARE_F          0x0CA
#define RA_ELC_EVENT_GPT4_COUNTER_OVERFLOW   0x0CB
#define RA_ELC_EVENT_GPT4_COUNTER_UNDERFLOW  0x0CC
#define RA_ELC_EVENT_GPT5_CAPTURE_COMPARE_A  0x0CE
#define RA_ELC_EVENT_GPT5_CAPTURE_COMPARE_B  0x0CF
#define RA_ELC_EVENT_GPT5_COMPARE_C          0x0D0
#define RA_ELC_EVENT_GPT5_COMPARE_D          0x0D1
#define RA_ELC_EVENT_GPT5_COMPARE_E          0x0D2
#define RA_ELC_EVENT_GPT5_COMPARE_F          0x0D3
#define RA_ELC_EVENT_GPT5_COUNTER_OVERFLOW   0x0D4
#define RA_ELC_EVENT_GPT5_COUNTER_UNDERFLOW  0x0D5
#define RA_ELC_EVENT_GPT6_CAPTURE_COMPARE_A  0x0D7
#define RA_ELC_EVENT_GPT6_CAPTURE_COMPARE_B  0x0D8
#define RA_ELC_EVENT_GPT6_COMPARE_C          0x0D9
#define RA_ELC_EVENT_GPT6_COMPARE_D          0x0DA
#define RA_ELC_EVENT_GPT6_COMPARE_E          0x0DB
#define RA_ELC_EVENT_GPT6_COMPARE_F          0x0DC
#define RA_ELC_EVENT_GPT6_COUNTER_OVERFLOW   0x0DD
#define RA_ELC_EVENT_GPT6_COUNTER_UNDERFLOW  0x0DE
#define RA_ELC_EVENT_GPT7_CAPTURE_COMPARE_A  0x0E0
#define RA_ELC_EVENT_GPT7_CAPTURE_COMPARE_B  0x0E1
#define RA_ELC_EVENT_GPT7_COMPARE_C          0x0E2
#define RA_ELC_EVENT_GPT7_COMPARE_D          0x0E3
#define RA_ELC_EVENT_GPT7_COMPARE_E          0x0E4
#define RA_ELC_EVENT_GPT7_COMPARE_F          0x0E5
#define RA_ELC_EVENT_GPT7_COUNTER_OVERFLOW   0x0E6
#define RA_ELC_EVENT_GPT7_COUNTER_UNDERFLOW  0x0E7
#define RA_ELC_EVENT_GPT8_CAPTURE_COMPARE_A  0x0E9
#define RA_ELC_EVENT_GPT8_CAPTURE_COMPARE_B  0x0EA
#define RA_ELC_EVENT_GPT8_COMPARE_C          0x0EB
#define RA_ELC_EVENT_GPT8_COMPARE_D          0x0EC
#define RA_ELC_EVENT_GPT8_COMPARE_E          0x0ED
#define RA_ELC_EVENT_GPT8_COMPARE_F          0x0EE
#define RA_ELC_EVENT_GPT8_COUNTER_OVERFLOW   0x0EF
#define RA_ELC_EVENT_GPT8_COUNTER_UNDERFLOW  0x0F0
#define RA_ELC_EVENT_GPT8_PC                 0x0F1
#define RA_ELC_EVENT_GPT9_CAPTURE_COMPARE_A  0x0F2
#define RA_ELC_EVENT_GPT9_CAPTURE_COMPARE_B  0x0F3
#define RA_ELC_EVENT_GPT9_COMPARE_C          0x0F4
#define RA_ELC_EVENT_GPT9_COMPARE_D          0x0F5
#define RA_ELC_EVENT_GPT9_COMPARE_E          0x0F6
#define RA_ELC_EVENT_GPT9_COMPARE_F          0x0F7
#define RA_ELC_EVENT_GPT9_COUNTER_OVERFLOW   0x0F8
#define RA_ELC_EVENT_GPT9_COUNTER_UNDERFLOW  0x0F9
#define RA_ELC_EVENT_GPT9_PC                 0x0FA
#define RA_ELC_EVENT_GPT10_CAPTURE_COMPARE_A 0x0FB
#define RA_ELC_EVENT_GPT10_CAPTURE_COMPARE_B 0x0FC
#define RA_ELC_EVENT_GPT10_COMPARE_C         0x0FD
#define RA_ELC_EVENT_GPT10_COMPARE_D         0x0FE
#define RA_ELC_EVENT_GPT10_COMPARE_E         0x0FF
#define RA_ELC_EVENT_GPT10_COMPARE_F         0x100
#define RA_ELC_EVENT_GPT10_COUNTER_OVERFLOW  0x101
#define RA_ELC_EVENT_GPT10_COUNTER_UNDERFLOW 0x102
#define RA_ELC_EVENT_GPT10_PC                0x103
#define RA_ELC_EVENT_GPT11_CAPTURE_COMPARE_A 0x104
#define RA_ELC_EVENT_GPT11_CAPTURE_COMPARE_B 0x105
#define RA_ELC_EVENT_GPT11_COMPARE_C         0x106
#define RA_ELC_EVENT_GPT11_COMPARE_D         0x107
#define RA_ELC_EVENT_GPT11_COMPARE_E         0x108
#define RA_ELC_EVENT_GPT11_COMPARE_F         0x109
#define RA_ELC_EVENT_GPT11_COUNTER_OVERFLOW  0x10A
#define RA_ELC_EVENT_GPT11_COUNTER_UNDERFLOW 0x10B
#define RA_ELC_EVENT_GPT12_CAPTURE_COMPARE_A 0x10D
#define RA_ELC_EVENT_GPT12_CAPTURE_COMPARE_B 0x10E
#define RA_ELC_EVENT_GPT12_COMPARE_C         0x10F
#define RA_ELC_EVENT_GPT12_COMPARE_D         0x110
#define RA_ELC_EVENT_GPT12_COMPARE_E         0x111
#define RA_ELC_EVENT_GPT12_COMPARE_F         0x112
#define RA_ELC_EVENT_GPT12_COUNTER_OVERFLOW  0x113
#define RA_ELC_EVENT_GPT12_COUNTER_UNDERFLOW 0x114
#define RA_ELC_EVENT_GPT13_CAPTURE_COMPARE_A 0x116
#define RA_ELC_EVENT_GPT13_CAPTURE_COMPARE_B 0x117
#define RA_ELC_EVENT_GPT13_COMPARE_C         0x118
#define RA_ELC_EVENT_GPT13_COMPARE_D         0x119
#define RA_ELC_EVENT_GPT13_COMPARE_E         0x11A
#define RA_ELC_EVENT_GPT13_COMPARE_F         0x11B
#define RA_ELC_EVENT_GPT13_COUNTER_OVERFLOW  0x11C
#define RA_ELC_EVENT_GPT13_COUNTER_UNDERFLOW 0x11D
#define RA_ELC_EVENT_EDMAC0_EINT             0x120
#define RA_ELC_EVENT_SCI0_RXI                0x124
#define RA_ELC_EVENT_SCI0_TXI                0x125
#define RA_ELC_EVENT_SCI0_TEI                0x126
#define RA_ELC_EVENT_SCI0_ERI                0x127
#define RA_ELC_EVENT_SCI0_AED                0x128
#define RA_ELC_EVENT_SCI0_BFD                0x129
#define RA_ELC_EVENT_SCI0_AM                 0x12A
#define RA_ELC_EVENT_SCI1_RXI                0x12B
#define RA_ELC_EVENT_SCI1_TXI                0x12C
#define RA_ELC_EVENT_SCI1_TEI                0x12D
#define RA_ELC_EVENT_SCI1_ERI                0x12E
#define RA_ELC_EVENT_SCI1_AED                0x12F
#define RA_ELC_EVENT_SCI1_BFD                0x130
#define RA_ELC_EVENT_SCI1_AM                 0x131
#define RA_ELC_EVENT_SCI2_RXI                0x132
#define RA_ELC_EVENT_SCI2_TXI                0x133
#define RA_ELC_EVENT_SCI2_TEI                0x134
#define RA_ELC_EVENT_SCI2_ERI                0x135
#define RA_ELC_EVENT_SCI2_AM                 0x138
#define RA_ELC_EVENT_SCI3_RXI                0x139
#define RA_ELC_EVENT_SCI3_TXI                0x13A
#define RA_ELC_EVENT_SCI3_TEI                0x13B
#define RA_ELC_EVENT_SCI3_ERI                0x13C
#define RA_ELC_EVENT_SCI3_AM                 0x13F
#define RA_ELC_EVENT_SCI4_RXI                0x140
#define RA_ELC_EVENT_SCI4_TXI                0x141
#define RA_ELC_EVENT_SCI4_TEI                0x142
#define RA_ELC_EVENT_SCI4_ERI                0x143
#define RA_ELC_EVENT_SCI4_AM                 0x146
#define RA_ELC_EVENT_SCI9_RXI                0x163
#define RA_ELC_EVENT_SCI9_TXI                0x164
#define RA_ELC_EVENT_SCI9_TEI                0x165
#define RA_ELC_EVENT_SCI9_ERI                0x166
#define RA_ELC_EVENT_SCI9_AM                 0x169
#define RA_ELC_EVENT_SPI0_RXI                0x178
#define RA_ELC_EVENT_SPI0_TXI                0x179
#define RA_ELC_EVENT_SPI0_IDLE               0x17A
#define RA_ELC_EVENT_SPI0_ERI                0x17B
#define RA_ELC_EVENT_SPI0_TEI                0x17C
#define RA_ELC_EVENT_SPI1_RXI                0x17D
#define RA_ELC_EVENT_SPI1_TXI                0x17E
#define RA_ELC_EVENT_SPI1_IDLE               0x17F
#define RA_ELC_EVENT_SPI1_ERI                0x180
#define RA_ELC_EVENT_SPI1_TEI                0x181
#define RA_ELC_EVENT_CAN_RXF                 0x185
#define RA_ELC_EVENT_CAN_GLERR               0x186
#define RA_ELC_EVENT_CAN0_DMAREQ0            0x187
#define RA_ELC_EVENT_CAN0_DMAREQ1            0x188
#define RA_ELC_EVENT_CAN1_DMAREQ0            0x18B
#define RA_ELC_EVENT_CAN1_DMAREQ1            0x18C
#define RA_ELC_EVENT_CAN0_TX                 0x18F
#define RA_ELC_EVENT_CAN0_CHERR              0x190
#define RA_ELC_EVENT_CAN0_COMFRX             0x191
#define RA_ELC_EVENT_CAN0_CF_DMAREQ          0x192
#define RA_ELC_EVENT_CAN0_RXMB               0x193
#define RA_ELC_EVENT_CAN1_TX                 0x194
#define RA_ELC_EVENT_CAN1_CHERR              0x195
#define RA_ELC_EVENT_CAN1_COMFRX             0x196
#define RA_ELC_EVENT_CAN1_CF_DMAREQ          0x197
#define RA_ELC_EVENT_CAN1_RXMB               0x198
#define RA_ELC_EVENT_CAN0_MRAM_ERI           0x19B
#define RA_ELC_EVENT_CAN1_MRAM_ERI           0x19C
#define RA_ELC_EVENT_I3C0_RESPONSE           0x19D
#define RA_ELC_EVENT_I3C0_COMMAND            0x19E
#define RA_ELC_EVENT_I3C0_IBI                0x19F
#define RA_ELC_EVENT_I3C0_RX                 0x1A0
#define RA_ELC_EVENT_IICB0_RXI               0x1A0
#define RA_ELC_EVENT_I3C0_TX                 0x1A1
#define RA_ELC_EVENT_IICB0_TXI               0x1A1
#define RA_ELC_EVENT_I3C0_RCV_STATUS         0x1A2
#define RA_ELC_EVENT_I3C0_HRESP              0x1A3
#define RA_ELC_EVENT_I3C0_HCMD               0x1A4
#define RA_ELC_EVENT_I3C0_HRX                0x1A5
#define RA_ELC_EVENT_I3C0_HTX                0x1A6
#define RA_ELC_EVENT_I3C0_TEND               0x1A7
#define RA_ELC_EVENT_IICB0_TEI               0x1A7
#define RA_ELC_EVENT_I3C0_EEI                0x1A8
#define RA_ELC_EVENT_IICB0_ERI               0x1A8
#define RA_ELC_EVENT_I3C0_STEV               0x1A9
#define RA_ELC_EVENT_I3C0_MREFOVF            0x1AA
#define RA_ELC_EVENT_I3C0_MREFCPT            0x1AB
#define RA_ELC_EVENT_I3C0_AMEV               0x1AC
#define RA_ELC_EVENT_I3C0_WU                 0x1AD
#define RA_ELC_EVENT_ADC0_SCAN_END           0x1AE
#define RA_ELC_EVENT_ADC0_SCAN_END_B         0x1AF
#define RA_ELC_EVENT_ADC0_WINDOW_A           0x1B0
#define RA_ELC_EVENT_ADC0_WINDOW_B           0x1B1
#define RA_ELC_EVENT_ADC0_COMPARE_MATCH      0x1B2
#define RA_ELC_EVENT_ADC0_COMPARE_MISMATCH   0x1B3
#define RA_ELC_EVENT_ADC1_SCAN_END           0x1B4
#define RA_ELC_EVENT_ADC1_SCAN_END_B         0x1B5
#define RA_ELC_EVENT_ADC1_WINDOW_A           0x1B6
#define RA_ELC_EVENT_ADC1_WINDOW_B           0x1B7
#define RA_ELC_EVENT_ADC1_COMPARE_MATCH      0x1B8
#define RA_ELC_EVENT_ADC1_COMPARE_MISMATCH   0x1B9
#define RA_ELC_EVENT_DOC_INT                 0x1BA
#define RA_ELC_EVENT_RSIP_TADI               0x1BC

/* Renesas RA ELC peripherals that can be linked to event signals. */
#define RA_ELC_PERIPHERAL_GPT_A   0
#define RA_ELC_PERIPHERAL_GPT_B   1
#define RA_ELC_PERIPHERAL_GPT_C   2
#define RA_ELC_PERIPHERAL_GPT_D   3
#define RA_ELC_PERIPHERAL_GPT_E   4
#define RA_ELC_PERIPHERAL_GPT_F   5
#define RA_ELC_PERIPHERAL_GPT_G   6
#define RA_ELC_PERIPHERAL_GPT_H   7
#define RA_ELC_PERIPHERAL_ADC0    8
#define RA_ELC_PERIPHERAL_ADC0_B  9
#define RA_ELC_PERIPHERAL_ADC1    10
#define RA_ELC_PERIPHERAL_ADC1_B  11
#define RA_ELC_PERIPHERAL_DAC0    12
#define RA_ELC_PERIPHERAL_DAC1    13
#define RA_ELC_PERIPHERAL_IOPORT1 14
#define RA_ELC_PERIPHERAL_IOPORT2 15
#define RA_ELC_PERIPHERAL_IOPORT3 16
#define RA_ELC_PERIPHERAL_IOPORT4 17
#define RA_ELC_PERIPHERAL_I3C     30



#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_MISC_RENESAS_RA_ELC_RA8T1_ELC_H_ */
```

## 94.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 56 行

Renesas RA8T1 事件链接控制器（Event Link Controller，ELC）的事件代码。

### 注释 3：原第 362 行

可链接到事件信号的 Renesas RA ELC 外设。

### 注释 4：原第 387 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_MISC_RENESAS_RA_ELC_RA8T1_ELC_H_`。

## 94.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ra8t1-elc_8h.html)

---

[上一章](P093_ra8m1-elc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P095_renesas_rcar_generic.h_源码浏览.md)
