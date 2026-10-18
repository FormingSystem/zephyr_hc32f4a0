---
id: learning.zephyr-docs.api-source-configuration-reference.page-68
title: pinctrl-rx.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rx_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第68章\_pinctrl-rx.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rx_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rx_8h.html)。

## 68.1\_原始可见代码（Source Code）

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
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00085"></a>
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
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00109"></a>
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
<a id="l00156"></a>
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
<a id="l00205"></a>
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
<a id="l00246"></a>
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
<a id="l00264"></a>
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
<a id="l00315"></a>
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
<a id="l00374"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00437"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00446"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00463"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="l00470"></a>
<a id="l00471"></a>
<a id="l00472"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00486"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00501"></a>
<a id="l00506"></a>
<a id="l00507"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00518"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="l00531"></a>
<a id="l00533"></a>
<a id="foldopen00547"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="l00549"></a>
<a id="l00551"></a>
<a id="l00552"></a>

```c
/*
 * Copyright (c) 2024 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RX_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RX_H_




/* Multi-Function Pin Controller (MPC) bit field positions and masks. */
#define RX_PORT_NUM_POS  0
#define RX_PORT_NUM_MASK 0x1f

#define RX_PIN_NUM_POS  5
#define RX_PIN_NUM_MASK 0xf

#define RX_PSEL_MASK 0x1f
#define RX_PSEL_POS  9

/* Peripheral-function selector (PSEL) values. */
#define RX_PSEL_RSCI      0xA
#define RX_PSEL_RSCI_TXDB 0xC
#define RX_PSEL_SCI_1     0xA
#define RX_PSEL_SCI_5     0xA
#define RX_PSEL_SCI_6     0xB
#define RX_PSEL_SCI_12    0xC
#define RX_PSEL_TMR       0x5
#define RX_PSEL_POE       0x7
#define RX_PSEL_ADC       0x0
#define RX_PSEL_LVD       0x0

#define RX_PSEL_P0nPFS_HIZ    0x0
#define RX_PSEL_P0nPFS_ADTRG0 0x1


#define RX_PSEL_P1nPFS_MTIOC0B 0x01
#define RX_PSEL_P1nPFS_MTIOC3A 0x01
#define RX_PSEL_P1nPFS_MTIOC3C 0x01

#define RX_PSEL_P1nPFS_MTCLKA  0x02
#define RX_PSEL_P1nPFS_MTCLKB  0x02
#define RX_PSEL_P1nPFS_MTIOC3B 0x02
#define RX_PSEL_P1nPFS_MTIOC3D 0x02

#define RX_PSEL_P1nPFS_TMCI1 0x5
#define RX_PSEL_P1nPFS_TMO1  0x5
#define RX_PSEL_P1nPFS_TMCI2 0x5
#define RX_PSEL_P1nPFS_TMO2  0x5
#define RX_PSEL_P1nPFS_TMRI2 0x5
#define RX_PSEL_P1nPFS_TMO3  0x5

#define RX_PSEL_P1nPFS_RTCOUT 0x7
#define RX_PSEL_P1nPFS_POE8   0x7

#define RX_PSEL_P1nPFS_ADTRG0 0x9

#define RX_PSEL_P1nPFS_RXD1   0xA
#define RX_PSEL_P1nPFS_SMISO1 0xA
#define RX_PSEL_P1nPFS_SSCL1  0xA
#define RX_PSEL_P1nPFS_TXD1   0xA
#define RX_PSEL_P1nPFS_SMOSI1 0xA
#define RX_PSEL_P1nPFS_SSDA1  0xA

#define RX_PSEL_P1nPFS_CTS1 0xB
#define RX_PSEL_P1nPFS_RTS1 0xB
#define RX_PSEL_P1nPFS_SS1  0xB

#define RX_PSEL_P1nPFS_MOSIA 0xD
#define RX_PSEL_P1nPFS_MISOA 0xD

#define RX_PSEL_P1nPFS_SCL 0xF
#define RX_PSEL_P1nPFS_SDA 0xF

#define RX_PSEL_P1nPFS_TS5 0x19
#define RX_PSEL_P1nPFS_TS6 0x19



#define RX_PSEL_P2nPFS_MTIOC1A 0x01
#define RX_PSEL_P2nPFS_MTIOC1B 0x01
#define RX_PSEL_P2nPFS_MTIOC2A 0x01
#define RX_PSEL_P2nPFS_MTIOC2B 0x01
#define RX_PSEL_P2nPFS_MTIOC3B 0x01
#define RX_PSEL_P2nPFS_MTIOC3D 0x01
#define RX_PSEL_P2nPFS_MTIOC4A 0x01
#define RX_PSEL_P2nPFS_MTIOC4C 0x01

#define RX_PSEL_P2nPFS_MTCLKA 0x02
#define RX_PSEL_P2nPFS_MTCLKB 0x02
#define RX_PSEL_P2nPFS_MTCLKC 0x02
#define RX_PSEL_P2nPFS_MTCLKD 0x02

#define RX_PSEL_P2nPFS_TMCI0 0x5
#define RX_PSEL_P2nPFS_TMO0  0x5
#define RX_PSEL_P2nPFS_TMRI0 0x5
#define RX_PSEL_P2nPFS_TMO1  0x5
#define RX_PSEL_P2nPFS_TMRI1 0x5
#define RX_PSEL_P2nPFS_TMCI3 0x5

#define RX_PSEL_P2nPFS_ADTRG0 0x9

#define RX_PSEL_P2nPFS_RXD0   0xA
#define RX_PSEL_P2nPFS_SMISO0 0xA
#define RX_PSEL_P2nPFS_SSCL0  0xA
#define RX_PSEL_P2nPFS_TXD0   0xA
#define RX_PSEL_P2nPFS_SMOSI0 0xA
#define RX_PSEL_P2nPFS_SSDA0  0xA
#define RX_PSEL_P2nPFS_SCK0   0xA
#define RX_PSEL_P2nPFS_TXD1   0xA
#define RX_PSEL_P2nPFS_SMOSI1 0xA
#define RX_PSEL_P2nPFS_SSDA1  0xA
#define RX_PSEL_P2nPFS_SCK1   0xA

#define RX_PSEL_P2nPFS_CTS0 0xB
#define RX_PSEL_P2nPFS_RTS0 0xB
#define RX_PSEL_P2nPFS_SS0  0xB

#define RX_PSEL_P2nPFS_TS3 0x19
#define RX_PSEL_P2nPFS_TS4 0x19


#define RX_PSEL_P3nPFS_MTIOC0A 0x01
#define RX_PSEL_P3nPFS_MTIOC0C 0x01
#define RX_PSEL_P3nPFS_MTIOC0D 0x01
#define RX_PSEL_P3nPFS_MTIOC4B 0x01
#define RX_PSEL_P3nPFS_MTIOC4D 0x01

#define RX_PSEL_P3nPFS_TMCI2 0x5
#define RX_PSEL_P3nPFS_TMO3  0x5
#define RX_PSEL_P3nPFS_TMRI3 0x5
#define RX_PSEL_P3nPFS_TMCI3 0x5

#define RX_PSEL_P3nPFS_RTCOUT 0x7
#define RX_PSEL_P3nPFS_POE2   0x7
#define RX_PSEL_P3nPFS_POE3   0x7
#define RX_PSEL_P3nPFS_POE8   0x7

#define RX_PSEL_P3nPFS_RXD1   0xA
#define RX_PSEL_P3nPFS_SMISO1 0xA
#define RX_PSEL_P3nPFS_SSCL1  0xA

#define RX_PSEL_P3nPFS_CTS1   0xB
#define RX_PSEL_P3nPFS_RTS1   0xB
#define RX_PSEL_P3nPFS_SS1    0xB
#define RX_PSEL_P3nPFS_RXD6   0xB
#define RX_PSEL_P3nPFS_SMISO6 0xB
#define RX_PSEL_P3nPFS_SSCL6  0xB
#define RX_PSEL_P3nPFS_TXD6   0xB
#define RX_PSEL_P3nPFS_SMOSI6 0xB
#define RX_PSEL_P3nPFS_SSDA6  0xB
#define RX_PSEL_P3nPFS_SCK6   0xB

#define RX_PSEL_P3nPFS_TS0 0x19
#define RX_PSEL_P3nPFS_TS1 0x19
#define RX_PSEL_P3nPFS_TS2 0x19


#define RX_PSEL_P5nPFS_MTIOC4B 0x01
#define RX_PSEL_P5nPFS_MTIOC4D 0x01

#define RX_PSEL_P5nPFS_TMCI1 0x5
#define RX_PSEL_P5nPFS_TMO3  0x5

#define RX_PSEL_P5nPFS_TS11 0x19
#define RX_PSEL_P5nPFS_TS12 0x19

#define RX_PSEL_P5nPFS_PMC0 0x19
#define RX_PSEL_P5nPFS_PMC1 0x19


#define RX_PSEL_PAnPFS_MTIOC4A 0x01
#define RX_PSEL_PAnPFS_MTIOC0B 0x01
#define RX_PSEL_PAnPFS_MTIOC0D 0x01
#define RX_PSEL_PAnPFS_MTIOC5U 0x01
#define RX_PSEL_PAnPFS_MTIOC5V 0x01

#define RX_PSEL_PAnPFS_MTCLKA 0x02
#define RX_PSEL_PAnPFS_MTCLKB 0x02
#define RX_PSEL_PAnPFS_MTCLKC 0x02
#define RX_PSEL_PAnPFS_MTCLKD 0x02

#define RX_PSEL_PAnPFS_TMRI0 0x5
#define RX_PSEL_PAnPFS_TMCI3 0x5

#define RX_PSEL_PAnPFS_POE2   0x7
#define RX_PSEL_PAnPFS_CACREF 0x7

#define RX_PSEL_PAnPFS_RXD5   0xA
#define RX_PSEL_PAnPFS_SMISO5 0xA
#define RX_PSEL_PAnPFS_SSCL5  0xA
#define RX_PSEL_PAnPFS_TXD5   0xA
#define RX_PSEL_PAnPFS_SMOSI5 0xA
#define RX_PSEL_PAnPFS_SSDA5  0xA
#define RX_PSEL_PAnPFS_SCK5   0xA

#define RX_PSEL_PAnPFS_CTS5 0xB
#define RX_PSEL_PAnPFS_RTS5 0xB
#define RX_PSEL_PAnPFS_SS5  0xB

#define RX_PSEL_PAnPFS_SSLA0  0xD
#define RX_PSEL_PAnPFS_SSLA1  0xD
#define RX_PSEL_PAnPFS_SSLA2  0xD
#define RX_PSEL_PAnPFS_SSLA3  0xD
#define RX_PSEL_PAnPFS_RSPCKA 0xD
#define RX_PSEL_PAnPFS_MOSIA  0xD
#define RX_PSEL_PAnPFS_MISOA  0xD

#define RX_PSEL_PAnPFS_TS26 0x19
#define RX_PSEL_PAnPFS_TS27 0x19
#define RX_PSEL_PAnPFS_TS28 0x19
#define RX_PSEL_PAnPFS_TS29 0x19
#define RX_PSEL_PAnPFS_TS30 0x19
#define RX_PSEL_PAnPFS_TS31 0x19
#define RX_PSEL_PAnPFS_TS32 0x19


#define RX_PSEL_PBnPFS_MTIOC0A 0x01
#define RX_PSEL_PBnPFS_MTIOC0C 0x01
#define RX_PSEL_PBnPFS_MTIOC2A 0x01
#define RX_PSEL_PBnPFS_MTIOC3B 0x01
#define RX_PSEL_PBnPFS_MTIOC3D 0x01
#define RX_PSEL_PBnPFS_MTIOC5W 0x01

#define RX_PSEL_PBnPFS_MTIOC1B 0x02
#define RX_PSEL_PBnPFS_MTIOC4A 0x02
#define RX_PSEL_PBnPFS_MTIOC4C 0x02

#define RX_PSEL_PBnPFS_TMO0  0x5
#define RX_PSEL_PBnPFS_TMRI1 0x5
#define RX_PSEL_PBnPFS_TMCI0 0x5

#define RX_PSEL_PBnPFS_POE1 0x7
#define RX_PSEL_PBnPFS_POE3 0x7

#define RX_PSEL_PBnPFS_RXD9   0xA
#define RX_PSEL_PBnPFS_SMISO9 0xA
#define RX_PSEL_PBnPFS_SSCL9  0xA
#define RX_PSEL_PBnPFS_TXD9   0xA
#define RX_PSEL_PBnPFS_SMOSI9 0xA
#define RX_PSEL_PBnPFS_SSDA9  0xA
#define RX_PSEL_PBnPFS_SCK9   0xA

#define RX_PSEL_PBnPFS_CTS6   0xB
#define RX_PSEL_PBnPFS_RTS6   0xB
#define RX_PSEL_PBnPFS_SS6    0xB
#define RX_PSEL_PBnPFS_CTS9   0xB
#define RX_PSEL_PBnPFS_RTS9   0xB
#define RX_PSEL_PBnPFS_SS9    0xB
#define RX_PSEL_PBnPFS_RXD6   0xB
#define RX_PSEL_PBnPFS_SMISO6 0xB
#define RX_PSEL_PBnPFS_SSCL6  0xB
#define RX_PSEL_PBnPFS_TXD6   0xB
#define RX_PSEL_PBnPFS_SMOSI6 0xB
#define RX_PSEL_PBnPFS_SSDA6  0xB
#define RX_PSEL_PBnPFS_SCK6   0xB

#define RX_PSEL_PBnPFS_RSPCKA 0xD

#define RX_PSEL_PBnPFS_CMPOB1 0x10

#define RX_PSEL_PBnPFS_TS18 0x19
#define RX_PSEL_PBnPFS_TS19 0x19
#define RX_PSEL_PBnPFS_TS20 0x19
#define RX_PSEL_PBnPFS_TS21 0x19
#define RX_PSEL_PBnPFS_TS22 0x19
#define RX_PSEL_PBnPFS_TS23 0x19
#define RX_PSEL_PBnPFS_TS24 0x19
#define RX_PSEL_PBnPFS_TS25 0x19


#define RX_PSEL_PCnPFS_MTIOC3A 0x01
#define RX_PSEL_PCnPFS_MTIOC3B 0x01
#define RX_PSEL_PCnPFS_MTIOC3C 0x01
#define RX_PSEL_PCnPFS_MTIOC3D 0x01
#define RX_PSEL_PCnPFS_MTIOC4B 0x01
#define RX_PSEL_PCnPFS_MTIOC4D 0x01

#define RX_PSEL_PCnPFS_MTCLKA 0x02
#define RX_PSEL_PCnPFS_MTCLKB 0x02
#define RX_PSEL_PCnPFS_MTCLKC 0x02
#define RX_PSEL_PCnPFS_MTCLKD 0x02

#define RX_PSEL_PCnPFS_TMCI1 0x5
#define RX_PSEL_PCnPFS_TMO2  0x5
#define RX_PSEL_PCnPFS_TMRI2 0x5
#define RX_PSEL_PCnPFS_TMCI2 0x5

#define RX_PSEL_PCnPFS_POE0   0x7
#define RX_PSEL_PCnPFS_CACREF 0x7

#define RX_PSEL_PCnPFS_RXD5   0xA
#define RX_PSEL_PCnPFS_SMISO5 0xA
#define RX_PSEL_PCnPFS_SSCL5  0xA
#define RX_PSEL_PCnPFS_TXD5   0xA
#define RX_PSEL_PCnPFS_SMOSI5 0xA
#define RX_PSEL_PCnPFS_SSDA5  0xA
#define RX_PSEL_PCnPFS_SCK5   0xA
#define RX_PSEL_PCnPFS_RXD8   0xA
#define RX_PSEL_PCnPFS_SMISO8 0xA
#define RX_PSEL_PCnPFS_SSCL8  0xA
#define RX_PSEL_PCnPFS_TXD8   0xA
#define RX_PSEL_PCnPFS_SMOSI8 0xA
#define RX_PSEL_PCnPFS_SSDA8  0xA
#define RX_PSEL_PCnPFS_SCK8   0xA

#define RX_PSEL_PCnPFS_CTS5 0xB
#define RX_PSEL_PCnPFS_RTS5 0xB
#define RX_PSEL_PCnPFS_SS5  0xB
#define RX_PSEL_PCnPFS_CTS8 0xB
#define RX_PSEL_PCnPFS_RTS8 0xB
#define RX_PSEL_PCnPFS_SS8  0xB

#define RX_PSEL_PCnPFS_SSLA0  0xD
#define RX_PSEL_PCnPFS_SSLA1  0xD
#define RX_PSEL_PCnPFS_SSLA2  0xD
#define RX_PSEL_PCnPFS_SSLA3  0xD
#define RX_PSEL_PCnPFS_RSPCKA 0xD
#define RX_PSEL_PCnPFS_MOSIA  0xD
#define RX_PSEL_PCnPFS_MISOA  0xD

#define RX_PSEL_PCnPFS_TS13  0x19
#define RX_PSEL_PCnPFS_TS14  0x19
#define RX_PSEL_PCnPFS_TS15  0x19
#define RX_PSEL_PCnPFS_TS16  0x19
#define RX_PSEL_PCnPFS_TS17  0x19
#define RX_PSEL_PCnPFS_TSCAP 0x19


#define RX_PSEL_PDnPFS_MTIOC4B 0x01
#define RX_PSEL_PDnPFS_MTIOC4D 0x01
#define RX_PSEL_PDnPFS_MTIOC5W 0x01
#define RX_PSEL_PDnPFS_MTIOC5V 0x01
#define RX_PSEL_PDnPFS_MTIOC5U 0x01

#define RX_PSEL_PDnPFS_POE0 0x7
#define RX_PSEL_PDnPFS_POE1 0x7
#define RX_PSEL_PDnPFS_POE2 0x7
#define RX_PSEL_PDnPFS_POE3 0x7
#define RX_PSEL_PDnPFS_POE8 0x7

#define RX_PSEL_PDnPFS_RXD6   0xB
#define RX_PSEL_PDnPFS_SMISO6 0xB
#define RX_PSEL_PDnPFS_SSCL6  0xB
#define RX_PSEL_PDnPFS_TXD6   0xB
#define RX_PSEL_PDnPFS_SMOSI6 0xB
#define RX_PSEL_PDnPFS_SSDA6  0xB
#define RX_PSEL_PDnPFS_SCK6   0xB


#define RX_PSEL_PEnPFS_MTIOC4A 0x01
#define RX_PSEL_PEnPFS_MTIOC4B 0x01
#define RX_PSEL_PEnPFS_MTIOC4C 0x01
#define RX_PSEL_PEnPFS_MTIOC4D 0x01

#define RX_PSEL_PEnPFS_MTIOC1A 0x02
#define RX_PSEL_PEnPFS_MTIOC2B 0x02

#define RX_PSEL_PEnPFS_POE8 0x7

#define RX_PSEL_PEnPFS_CLKOUT 0x9

#define RX_PSEL_PEnPFS_RXD12   0xC
#define RX_PSEL_PEnPFS_SMISO12 0xC
#define RX_PSEL_PEnPFS_SSCL12  0xC
#define RX_PSEL_PEnPFS_TXD12   0xC
#define RX_PSEL_PEnPFS_SMOSI12 0xC
#define RX_PSEL_PEnPFS_SSDA12  0xC
#define RX_PSEL_PEnPFS_SCK12   0xC
#define RX_PSEL_PEnPFS_TXDX12  0xC
#define RX_PSEL_PEnPFS_RXDX12  0xC
#define RX_PSEL_PEnPFS_SIOX12  0xC
#define RX_PSEL_PEnPFS_CTS12   0xC
#define RX_PSEL_PEnPFS_RTS12   0xC
#define RX_PSEL_PEnPFS_SS12    0xC

#define RX_PSEL_PEnPFS_CMPOB0 0X10

#define RX_PSEL_PEnPFS_TS33 0X19
#define RX_PSEL_PEnPFS_TS34 0x19
#define RX_PSEL_PEnPFS_TS35 0x19


#define RX_PSEL_PHnPFS_TMO0  0x05
#define RX_PSEL_PHnPFS_TMRI0 0x05
#define RX_PSEL_PHnPFS_TMCI0 0x05

#define RX_PSEL_PHnPFS_CACREF 0x7

#define RX_PSEL_PHnPFS_TS7  0x19
#define RX_PSEL_PHnPFS_TS8  0x19
#define RX_PSEL_PHnPFS_TS9  0x19
#define RX_PSEL_PHnPFS_TS10 0x19


#define RX_PSEL_PJnPFS_MTIOC3A 0x01
#define RX_PSEL_PJnPFS_MTIOC3C 0x01

#define RX_PSEL_PJnPFS_CTS6 0xB
#define RX_PSEL_PJnPFS_TTS6 0xB
#define RX_PSEL_PJnPFS_SS6  0xB



#define RX_PSEL(psel, port_num, pin_num)                                                           \
        (psel << RX_PSEL_POS | pin_num << RX_PIN_NUM_POS | port_num << RX_PORT_NUM_POS)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RX_H_ */
```

## 68.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 73 行

多功能引脚控制器（Multi-Function Pin Controller，MPC）位域的位置和掩码。

### 注释 3：原第 89 行

外设功能选择器（PSEL）取值。

### 注释 4：原第 552 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RX_H_`。

## 68.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rx_8h.html)

---

[上一章](P067_pinctrl-ra0.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P069_pinctrl-zynqmp.h_源码浏览.md)
