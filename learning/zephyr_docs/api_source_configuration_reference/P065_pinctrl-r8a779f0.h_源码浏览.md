---
id: learning.zephyr-docs.api-source-configuration-reference.page-65
title: pinctrl-r8a779f0.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-r8a779f0_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第65章\_pinctrl-r8a779f0.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-r8a779f0_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-r8a779f0_8h.html)。

## 65.1\_原始可见代码（Source Code）

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
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
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
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
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
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="l00467"></a>
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
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00504"></a>
<a id="l00505"></a>
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
<a id="l00517"></a>
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00533"></a>
<a id="l00534"></a>
<a id="l00535"></a>
<a id="l00536"></a>
<a id="l00537"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00542"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="l00545"></a>
<a id="l00546"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00552"></a>
<a id="l00553"></a>
<a id="l00554"></a>
<a id="l00555"></a>
<a id="l00556"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00559"></a>
<a id="l00561"></a>
<a id="l00562"></a>
<a id="apinctrl-rcar-common_8h_html"></a>

```c
/*
 * Copyright (c) 2023 IoT.bzh
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_R8A779F0_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_R8A779F0_H_

#include "pinctrl-rcar-common.h"


/* Pins declaration */
#define PIN_NONE                   -1
#define PIN_SCIF_CLK               RCAR_GP_PIN(0, 0)
#define PIN_HSCK0                  RCAR_GP_PIN(0, 1)
#define PIN_HRX0                   RCAR_GP_PIN(0, 2)
#define PIN_HTX0                   RCAR_GP_PIN(0, 3)
#define PIN_HCTS0_N                RCAR_GP_PIN(0, 4)
#define PIN_HRTS0_N                RCAR_GP_PIN(0, 5)
#define PIN_RX0                    RCAR_GP_PIN(0, 6)
#define PIN_TX0                    RCAR_GP_PIN(0, 7)
#define PIN_SCK0                   RCAR_GP_PIN(0, 8)
#define PIN_RTS0_N                 RCAR_GP_PIN(0, 9)
#define PIN_CTS0_N                 RCAR_GP_PIN(0, 10)
#define PIN_MSIOF0_SYNC            RCAR_GP_PIN(0, 11)
#define PIN_MSIOF0_RXD             RCAR_GP_PIN(0, 12)
#define PIN_MSIOF0_TXD             RCAR_GP_PIN(0, 13)
#define PIN_MSIOF0_SCK             RCAR_GP_PIN(0, 14)
#define PIN_MSIOF0_SS1             RCAR_GP_PIN(0, 15)
#define PIN_MSIOF0_SS2             RCAR_GP_PIN(0, 16)
#define PIN_IRQ0                   RCAR_GP_PIN(0, 17)
#define PIN_IRQ1                   RCAR_GP_PIN(0, 18)
#define PIN_IRQ2                   RCAR_GP_PIN(0, 19)
#define PIN_IRQ3                   RCAR_GP_PIN(0, 20)
#define PIN_GP1_00                 RCAR_GP_PIN(1, 0)
#define PIN_GP1_01                 RCAR_GP_PIN(1, 1)
#define PIN_GP1_02                 RCAR_GP_PIN(1, 2)
#define PIN_GP1_03                 RCAR_GP_PIN(1, 3)
#define PIN_GP1_04                 RCAR_GP_PIN(1, 4)
#define PIN_GP1_05                 RCAR_GP_PIN(1, 5)
#define PIN_GP1_06                 RCAR_GP_PIN(1, 6)
#define PIN_GP1_07                 RCAR_GP_PIN(1, 7)
#define PIN_GP1_08                 RCAR_GP_PIN(1, 8)
#define PIN_GP1_09                 RCAR_GP_PIN(1, 9)
#define PIN_GP1_10                 RCAR_GP_PIN(1, 10)
#define PIN_GP1_11                 RCAR_GP_PIN(1, 11)
#define PIN_MMC_SD_CLK             RCAR_GP_PIN(1, 12)
#define PIN_MMC_SD_D0              RCAR_GP_PIN(1, 13)
#define PIN_MMC_SD_D1              RCAR_GP_PIN(1, 14)
#define PIN_MMC_SD_D2              RCAR_GP_PIN(1, 15)
#define PIN_MMC_SD_D3              RCAR_GP_PIN(1, 16)
#define PIN_MMC_D5                 RCAR_GP_PIN(1, 17)
#define PIN_MMC_D4                 RCAR_GP_PIN(1, 18)
#define PIN_MMC_D6                 RCAR_GP_PIN(1, 19)
#define PIN_MMC_DS                 RCAR_GP_PIN(1, 20)
#define PIN_MMC_D7                 RCAR_GP_PIN(1, 21)
#define PIN_MMC_SD_CMD             RCAR_GP_PIN(1, 22)
#define PIN_SD_CD                  RCAR_GP_PIN(1, 23)
#define PIN_SD_WP                  RCAR_GP_PIN(1, 24)
#define PIN_RPC_INT_N              RCAR_GP_PIN(2, 0)
#define PIN_RPC_WP_N               RCAR_GP_PIN(2, 1)
#define PIN_RPC_RESET_N            RCAR_GP_PIN(2, 2)
#define PIN_QSPI1_SSL              RCAR_GP_PIN(2, 3)
#define PIN_QSPI1_IO3              RCAR_GP_PIN(2, 4)
#define PIN_QSPI1_MISO_IO1         RCAR_GP_PIN(2, 5)
#define PIN_QSPI1_IO2              RCAR_GP_PIN(2, 6)
#define PIN_QSPI1_MOSI_IO0         RCAR_GP_PIN(2, 7)
#define PIN_QSPI1_SPCLK            RCAR_GP_PIN(2, 8)
#define PIN_QSPI0_MOSI_IO0         RCAR_GP_PIN(2, 9)
#define PIN_QSPI0_SPCLK            RCAR_GP_PIN(2, 10)
#define PIN_QSPI0_IO2              RCAR_GP_PIN(2, 11)
#define PIN_QSPI0_MISO_IO1         RCAR_GP_PIN(2, 12)
#define PIN_QSPI0_SSL              RCAR_GP_PIN(2, 13)
#define PIN_QSPI0_IO3              RCAR_GP_PIN(2, 14)
#define PIN_PCIE0_CLKREQ_N         RCAR_GP_PIN(2, 15)
#define PIN_PCIE1_CLKREQ_N         RCAR_GP_PIN(2, 16)
#define PIN_TSN1_MDIO              RCAR_GP_PIN(3, 0)
#define PIN_TSN2_MDIO              RCAR_GP_PIN(3, 1)
#define PIN_TSN0_MDIO              RCAR_GP_PIN(3, 2)
#define PIN_TSN2_MDC               RCAR_GP_PIN(3, 3)
#define PIN_TSN0_MDC               RCAR_GP_PIN(3, 4)
#define PIN_TSN1_MDC               RCAR_GP_PIN(3, 5)
#define PIN_TSN1_LINK              RCAR_GP_PIN(3, 6)
#define PIN_TSN2_LINK              RCAR_GP_PIN(3, 7)
#define PIN_TSN0_LINK              RCAR_GP_PIN(3, 8)
#define PIN_TSN2_PHY_INT           RCAR_GP_PIN(3, 9)
#define PIN_TSN0_PHY_INT           RCAR_GP_PIN(3, 10)
#define PIN_TSN1_PHY_INT           RCAR_GP_PIN(3, 11)
#define PIN_TSN0_MAGIC             RCAR_GP_PIN(3, 12)
#define PIN_TSN1_AVTP_PPS          RCAR_GP_PIN(3, 13)
#define PIN_TSN1_AVTP_MATCH        RCAR_GP_PIN(3, 14)
#define PIN_TSN1_AVTP_CAPTURE      RCAR_GP_PIN(3, 15)
#define PIN_TSN0_AVTP_PPS          RCAR_GP_PIN(3, 16)
#define PIN_TSN0_AVTP_MATCH        RCAR_GP_PIN(3, 17)
#define PIN_TSN0_AVTP_CAPTURE      RCAR_GP_PIN(3, 18)
#define PIN_GP4_00                 RCAR_GP_PIN(4, 0)
#define PIN_GP4_01                 RCAR_GP_PIN(4, 1)
#define PIN_GP4_02                 RCAR_GP_PIN(4, 2)
#define PIN_GP4_03                 RCAR_GP_PIN(4, 3)
#define PIN_GP4_04                 RCAR_GP_PIN(4, 4)
#define PIN_GP4_05                 RCAR_GP_PIN(4, 5)
#define PIN_GP4_06                 RCAR_GP_PIN(4, 6)
#define PIN_GP4_07                 RCAR_GP_PIN(4, 7)
#define PIN_GP4_08                 RCAR_GP_PIN(4, 8)
#define PIN_GP4_09                 RCAR_GP_PIN(4, 9)
#define PIN_GP4_10                 RCAR_GP_PIN(4, 10)
#define PIN_GP4_11                 RCAR_GP_PIN(4, 11)
#define PIN_GP4_12                 RCAR_GP_PIN(4, 12)
#define PIN_GP4_13                 RCAR_GP_PIN(4, 13)
#define PIN_GP4_14                 RCAR_GP_PIN(4, 14)
#define PIN_GP4_15                 RCAR_GP_PIN(4, 15)
#define PIN_GP4_16                 RCAR_GP_PIN(4, 16)
#define PIN_GP4_17                 RCAR_GP_PIN(4, 17)
#define PIN_GP4_18                 RCAR_GP_PIN(4, 18)
#define PIN_GP4_19                 RCAR_GP_PIN(4, 19)
#define PIN_MSPI0SC                RCAR_GP_PIN(4, 20)
#define PIN_MSPI0SI                RCAR_GP_PIN(4, 21)
#define PIN_MSPI0SO_MSPI0DCS       RCAR_GP_PIN(4, 22)
#define PIN_MSPI0CSS1              RCAR_GP_PIN(4, 23)
#define PIN_MSPI0CSS0              RCAR_GP_PIN(4, 24)
#define PIN_MSPI1SI                RCAR_GP_PIN(4, 25)
#define PIN_MSPI1SO_MSPI1DCS       RCAR_GP_PIN(4, 26)
#define PIN_MSPI1CSS0              RCAR_GP_PIN(4, 27)
#define PIN_MSPI1SC                RCAR_GP_PIN(4, 28)
#define PIN_MSPI1CSS2              RCAR_GP_PIN(4, 29)
#define PIN_MSPI1CSS1              RCAR_GP_PIN(4, 30)
#define PIN_RIIC0SCL               RCAR_GP_PIN(5, 0)
#define PIN_RIIC0SDA               RCAR_GP_PIN(5, 1)
#define PIN_ETNB0MD                RCAR_GP_PIN(5, 2)
#define PIN_ETNB0WOL               RCAR_GP_PIN(5, 3)
#define PIN_ETNB0LINKSTA           RCAR_GP_PIN(5, 4)
#define PIN_ETNB0MDC               RCAR_GP_PIN(5, 5)
#define PIN_ETNB0RXER              RCAR_GP_PIN(5, 6)
#define PIN_ETNB0RXD3              RCAR_GP_PIN(5, 7)
#define PIN_ETNB0RXD1              RCAR_GP_PIN(5, 8)
#define PIN_ETNB0RXD2              RCAR_GP_PIN(5, 9)
#define PIN_ETNB0RXDV              RCAR_GP_PIN(5, 10)
#define PIN_ETNB0RXD0              RCAR_GP_PIN(5, 11)
#define PIN_ETNB0RXCLK             RCAR_GP_PIN(5, 12)
#define PIN_ETNB0TXER              RCAR_GP_PIN(5, 13)
#define PIN_ETNB0TXD3              RCAR_GP_PIN(5, 14)
#define PIN_ETNB0TXCLK             RCAR_GP_PIN(5, 15)
#define PIN_ETNB0TXD1              RCAR_GP_PIN(5, 16)
#define PIN_ETNB0TXD2              RCAR_GP_PIN(5, 17)
#define PIN_ETNB0TXEN              RCAR_GP_PIN(5, 18)
#define PIN_ETNB0TXD0              RCAR_GP_PIN(5, 19)
#define PIN_RLIN37TX               RCAR_GP_PIN(6, 0)
#define PIN_RLIN37RX_INTP23        RCAR_GP_PIN(6, 1)
#define PIN_RLIN36TX               RCAR_GP_PIN(6, 2)
#define PIN_RLIN36RX_INTP22        RCAR_GP_PIN(6, 3)
#define PIN_RLIN35TX               RCAR_GP_PIN(6, 4)
#define PIN_RLIN35RX_INTP21        RCAR_GP_PIN(6, 5)
#define PIN_RLIN34TX               RCAR_GP_PIN(6, 6)
#define PIN_RLIN34RX_INTP20        RCAR_GP_PIN(6, 7)
#define PIN_RLIN33TX               RCAR_GP_PIN(6, 8)
#define PIN_RLIN33RX_INTP19        RCAR_GP_PIN(6, 9)
#define PIN_RLIN32TX               RCAR_GP_PIN(6, 10)
#define PIN_RLIN32RX_INTP18        RCAR_GP_PIN(6, 11)
#define PIN_RLIN31TX               RCAR_GP_PIN(6, 12)
#define PIN_RLIN31RX_INTP17        RCAR_GP_PIN(6, 13)
#define PIN_RLIN30TX               RCAR_GP_PIN(6, 14)
#define PIN_RLIN30RX_INTP16        RCAR_GP_PIN(6, 15)
#define PIN_INTP37                 RCAR_GP_PIN(6, 16)
#define PIN_INTP36                 RCAR_GP_PIN(6, 17)
#define PIN_INTP35                 RCAR_GP_PIN(6, 18)
#define PIN_INTP34                 RCAR_GP_PIN(6, 19)
#define PIN_INTP33                 RCAR_GP_PIN(6, 20)
#define PIN_INTP32                 RCAR_GP_PIN(6, 21)
#define PIN_NMI1                   RCAR_GP_PIN(6, 22)
#define PIN_PRESETOUT1_N           RCAR_GP_PIN(6, 31)
#define PIN_CAN0TX                 RCAR_GP_PIN(7, 0)
#define PIN_CAN0RX_INTP0           RCAR_GP_PIN(7, 1)
#define PIN_CAN1TX                 RCAR_GP_PIN(7, 2)
#define PIN_CAN1RX_INTP1           RCAR_GP_PIN(7, 3)
#define PIN_CAN2TX                 RCAR_GP_PIN(7, 4)
#define PIN_CAN2RX_INTP2           RCAR_GP_PIN(7, 5)
#define PIN_CAN3TX                 RCAR_GP_PIN(7, 6)
#define PIN_CAN3RX_INTP3           RCAR_GP_PIN(7, 7)
#define PIN_CAN4TX                 RCAR_GP_PIN(7, 8)
#define PIN_CAN4RX_INTP4           RCAR_GP_PIN(7, 9)
#define PIN_CAN5TX                 RCAR_GP_PIN(7, 10)
#define PIN_CAN5RX_INTP5           RCAR_GP_PIN(7, 11)
#define PIN_CAN6TX                 RCAR_GP_PIN(7, 12)
#define PIN_CAN6RX_INTP6           RCAR_GP_PIN(7, 13)
#define PIN_CAN7TX                 RCAR_GP_PIN(7, 14)
#define PIN_CAN7RX_INTP7           RCAR_GP_PIN(7, 15)
#define PIN_CAN8TX                 RCAR_GP_PIN(7, 16)
#define PIN_CAN8RX_INTP8           RCAR_GP_PIN(7, 17)
#define PIN_CAN9TX                 RCAR_GP_PIN(7, 18)
#define PIN_CAN9RX_INTP9           RCAR_GP_PIN(7, 19)
#define PIN_CAN10TX                RCAR_GP_PIN(7, 20)
#define PIN_CAN10RX_INTP10         RCAR_GP_PIN(7, 21)
#define PIN_CAN11TX                RCAR_GP_PIN(7, 22)
#define PIN_CAN11RX_INTP11         RCAR_GP_PIN(7, 23)
#define PIN_CAN12TX                RCAR_GP_PIN(7, 24)
#define PIN_CAN12RX_INTP12         RCAR_GP_PIN(7, 25)
#define PIN_CAN13TX                RCAR_GP_PIN(7, 26)
#define PIN_CAN13RX_INTP13         RCAR_GP_PIN(7, 27)
#define PIN_CAN14TX                RCAR_GP_PIN(7, 28)
#define PIN_CAN14RX_INTP14         RCAR_GP_PIN(7, 29)
#define PIN_CAN15TX                RCAR_GP_PIN(7, 30)
#define PIN_CAN15RX_INTP15         RCAR_GP_PIN(7, 31)

/* Pinmux function declarations */
#define FUNC_SCIF_CLK              IP0SR0(0, 0)
#define FUNC_HSCK0                 IP0SR0(4, 0)
#define FUNC_SCK3                  IP0SR0(4, 1)
#define FUNC_MSIOF3_SCK            IP0SR0(4, 2)
#define FUNC_TSN0_AVTP_CAPTURE_A   IP0SR0(4, 5)
#define FUNC_HRX0                  IP0SR0(8, 0)
#define FUNC_RX3                   IP0SR0(8, 1)
#define FUNC_MSIOF3_RXD            IP0SR0(8, 2)
#define FUNC_TSN0_AVTP_MATCH_A     IP0SR0(8, 5)
#define FUNC_HTX0                  IP0SR0(12, 0)
#define FUNC_TX3                   IP0SR0(12, 1)
#define FUNC_MSIOF3_TXD            IP0SR0(12, 2)
#define FUNC_HCTS0_N               IP0SR0(16, 0)
#define FUNC_CTS3_N                IP0SR0(16, 1)
#define FUNC_MSIOF3_SS1            IP0SR0(16, 2)
#define FUNC_TSN0_MDC_A            IP0SR0(16, 5)
#define FUNC_HRTS0_N               IP0SR0(20, 0)
#define FUNC_RTS3_N                IP0SR0(20, 1)
#define FUNC_MSIOF3_SS2            IP0SR0(20, 2)
#define FUNC_TSN0_MDIO_A           IP0SR0(20, 5)
#define FUNC_RX0                   IP0SR0(24, 0)
#define FUNC_HRX1                  IP0SR0(24, 1)
#define FUNC_MSIOF1_RXD            IP0SR0(24, 3)
#define FUNC_TSN1_AVTP_MATCH_A     IP0SR0(24, 5)
#define FUNC_TX0                   IP0SR0(28, 0)
#define FUNC_HTX1                  IP0SR0(28, 1)
#define FUNC_MSIOF1_TXD            IP0SR0(28, 3)
#define FUNC_TSN1_AVTP_CAPTURE_A   IP0SR0(28, 5)
#define FUNC_SCK0                  IP1SR0(0, 0)
#define FUNC_HSCK1                 IP1SR0(0, 1)
#define FUNC_MSIOF1_SCK            IP1SR0(0, 3)
#define FUNC_RTS0_N                IP1SR0(4, 0)
#define FUNC_HRTS1_N               IP1SR0(4, 1)
#define FUNC_MSIOF3_SYNC           IP1SR0(4, 2)
#define FUNC_TSN1_MDIO_A           IP1SR0(4, 5)
#define FUNC_CTS0_N                IP1SR0(8, 0)
#define FUNC_HCTS1_N               IP1SR0(8, 1)
#define FUNC_MSIOF1_SYNC           IP1SR0(8, 3)
#define FUNC_TSN1_MDC_A            IP1SR0(8, 5)
#define FUNC_MSIOF0_SYNC           IP1SR0(12, 0)
#define FUNC_HCTS3_N               IP1SR0(12, 1)
#define FUNC_CTS1_N                IP1SR0(12, 2)
#define FUNC_IRQ4                  IP1SR0(12, 3)
#define FUNC_TSN0_LINK_A           IP1SR0(12, 5)
#define FUNC_MSIOF0_RXD            IP1SR0(16, 0)
#define FUNC_HRX3                  IP1SR0(16, 1)
#define FUNC_RX1                   IP1SR0(16, 2)
#define FUNC_MSIOF0_TXD            IP1SR0(20, 0)
#define FUNC_HTX3                  IP1SR0(20, 1)
#define FUNC_TX1                   IP1SR0(20, 2)
#define FUNC_MSIOF0_SCK            IP1SR0(24, 0)
#define FUNC_HSCK3                 IP1SR0(24, 1)
#define FUNC_SCK1                  IP1SR0(24, 2)
#define FUNC_MSIOF0_SS1            IP1SR0(28, 0)
#define FUNC_HRTS3_N               IP1SR0(28, 1)
#define FUNC_RTS1_N                IP1SR0(28, 2)
#define FUNC_IRQ5                  IP1SR0(28, 3)
#define FUNC_TSN1_LINK_A           IP1SR0(28, 5)
#define FUNC_MSIOF0_SS2            IP2SR0(0, 0)
#define FUNC_TSN2_LINK_A           IP2SR0(0, 5)
#define FUNC_IRQ0                  IP2SR0(4, 0)
#define FUNC_MSIOF1_SS1            IP2SR0(4, 3)
#define FUNC_TSN0_MAGIC_A          IP2SR0(4, 5)
#define FUNC_IRQ1                  IP2SR0(8, 0)
#define FUNC_MSIOF1_SS2            IP2SR0(8, 3)
#define FUNC_TSN0_PHY_INT_A        IP2SR0(8, 5)
#define FUNC_IRQ2                  IP2SR0(12, 0)
#define FUNC_TSN1_PHY_INT_A        IP2SR0(12, 5)
#define FUNC_IRQ3                  IP2SR0(16, 0)
#define FUNC_TSN2_PHY_INT_A        IP2SR0(16, 5)
#define FUNC_GP1_00                IP0SR1(0, 0)
#define FUNC_TCLK1                 IP0SR1(0, 1)
#define FUNC_HSCK2                 IP0SR1(0, 2)
#define FUNC_GP1_01                IP0SR1(4, 0)

#define FUNC_MMC_SD_CLK            IPSR_DUMMY
#define FUNC_MMC_SD_D0             IPSR_DUMMY
#define FUNC_MMC_SD_D1             IPSR_DUMMY
#define FUNC_MMC_SD_D2             IPSR_DUMMY
#define FUNC_MMC_SD_D3             IPSR_DUMMY
#define FUNC_MMC_D4                IPSR_DUMMY
#define FUNC_MMC_D5                IPSR_DUMMY
#define FUNC_MMC_D6                IPSR_DUMMY
#define FUNC_MMC_D7                IPSR_DUMMY
#define FUNC_MMC_DS                IPSR_DUMMY
#define FUNC_MMC_SD_CMD            IPSR_DUMMY
#define FUNC_SD_CD                 IPSR_DUMMY
#define FUNC_SD_WP                 IPSR_DUMMY

#define FUNC_TCLK4                 IP0SR1(4, 1)
#define FUNC_HRX2                  IP0SR1(4, 2)
#define FUNC_GP1_02                IP0SR1(8, 0)
#define FUNC_HTX2                  IP0SR1(8, 2)
#define FUNC_MSIOF2_SS1            IP0SR1(8, 3)
#define FUNC_TSN2_MDC_A            IP0SR1(8, 5)
#define FUNC_GP1_03                IP0SR1(12, 0)
#define FUNC_TCLK2                 IP0SR1(12, 1)
#define FUNC_HCTS2_N               IP0SR1(12, 2)
#define FUNC_MSIOF2_SS2            IP0SR1(12, 3)
#define FUNC_CTS4_N                IP0SR1(12, 4)
#define FUNC_TSN2_MDIO_A           IP0SR1(12, 5)
#define FUNC_GP1_04                IP0SR1(16, 0)
#define FUNC_TCLK3                 IP0SR1(16, 1)
#define FUNC_HRTS2_N               IP0SR1(16, 2)
#define FUNC_MSIOF2_SYNC           IP0SR1(16, 3)
#define FUNC_RTS4_N                IP0SR1(16, 4)
#define FUNC_GP1_05                IP0SR1(20, 0)
#define FUNC_MSIOF2_SCK            IP0SR1(20, 1)
#define FUNC_SCK4                  IP0SR1(20, 2)
#define FUNC_GP1_06                IP0SR1(24, 0)
#define FUNC_MSIOF2_RXD            IP0SR1(24, 1)
#define FUNC_RX4                   IP0SR1(24, 2)
#define FUNC_GP1_07                IP0SR1(28, 0)
#define FUNC_MSIOF2_TXD            IP0SR1(28, 1)
#define FUNC_TX4                   IP0SR1(28, 2)
#define FUNC_GP4_00                IP0SR4(0, 0)
#define FUNC_MSPI4SC               IP0SR4(0, 1)
#define FUNC_TAUD0I2               IP0SR4(0, 3)
#define FUNC_TAUD0O2               IP0SR4(0, 4)
#define FUNC_GP4_01                IP0SR4(4, 0)
#define FUNC_MSPI4SI               IP0SR4(4, 1)
#define FUNC_TAUD0I4               IP0SR4(4, 3)
#define FUNC_TAUD0O4               IP0SR4(4, 4)
#define FUNC_GP4_02                IP0SR4(8, 0)
#define FUNC_MSPI4SO_MSPI4DCS      IP0SR4(8, 1)
#define FUNC_TAUD0I3               IP0SR4(8, 3)
#define FUNC_TAUD0O3               IP0SR4(8, 4)
#define FUNC_GP4_03                IP0SR4(12, 0)
#define FUNC_MSPI4CSS1             IP0SR4(12, 1)
#define FUNC_TAUD0I6               IP0SR4(12, 3)
#define FUNC_TAUD0O6               IP0SR4(12, 4)
#define FUNC_GP4_04                IP0SR4(16, 0)
#define FUNC_MSPI4CSS0             IP0SR4(16, 1)
#define FUNC_MSPI4SSI_N            IP0SR4(16, 2)
#define FUNC_TAUD0I5               IP0SR4(16, 3)
#define FUNC_TAUD0O5               IP0SR4(16, 4)
#define FUNC_GP4_05                IP0SR4(20, 0)
#define FUNC_MSPI4CSS3             IP0SR4(20, 1)
#define FUNC_TAUD0I8               IP0SR4(20, 3)
#define FUNC_TAUD0O8               IP0SR4(20, 4)
#define FUNC_GP4_06                IP0SR4(24, 0)
#define FUNC_MSPI4CSS2             IP0SR4(24, 1)
#define FUNC_TAUD0I7               IP0SR4(24, 3)
#define FUNC_TAUD0O7               IP0SR4(24, 4)
#define FUNC_GP4_07                IP0SR4(28, 0)
#define FUNC_MSPI4CSS5             IP0SR4(28, 1)
#define FUNC_TAUD0I10              IP0SR4(28, 3)
#define FUNC_TAUD0O10              IP0SR4(28, 4)
#define FUNC_GP4_08                IP1SR4(0, 0)
#define FUNC_MSPI4CSS4             IP1SR4(0, 1)
#define FUNC_TAUD0I9               IP1SR4(0, 3)
#define FUNC_TAUD0O9               IP1SR4(0, 4)
#define FUNC_GP4_09                IP1SR4(4, 0)
#define FUNC_MSPI4CSS7             IP1SR4(4, 1)
#define FUNC_TAUD0I12              IP1SR4(4, 3)
#define FUNC_TAUD0O12              IP1SR4(4, 4)
#define FUNC_GP4_10                IP1SR4(8, 0)
#define FUNC_MSPI4CSS6             IP1SR4(8, 1)
#define FUNC_TAUD0I11              IP1SR4(8, 3)
#define FUNC_TAUD0O11              IP1SR4(8, 4)
#define FUNC_GP4_11                IP1SR4(12, 0)
#define FUNC_ERRORIN0_N            IP1SR4(12, 1)
#define FUNC_TAUD0I14              IP1SR4(12, 3)
#define FUNC_TAUD0O14              IP1SR4(12, 4)
#define FUNC_GP4_12                IP1SR4(16, 0)
#define FUNC_ERROROUT_C_N          IP1SR4(16, 1)
#define FUNC_TAUD0I13              IP1SR4(16, 3)
#define FUNC_TAUD0O13              IP1SR4(16, 4)
#define FUNC_GP4_13                IP1SR4(20, 0)
#define FUNC_GP4_14                IP1SR4(24, 0)
#define FUNC_ERRORIN1_N            IP1SR4(24, 1)
#define FUNC_TAUD0I15              IP1SR4(24, 3)
#define FUNC_TAUD0O15              IP1SR4(24, 4)
#define FUNC_GP4_15                IP1SR4(28, 0)
#define FUNC_MSPI1CSS3             IP1SR4(28, 1)
#define FUNC_TAUD1I1               IP1SR4(28, 3)
#define FUNC_TAUD1O1               IP1SR4(28, 4)
#define FUNC_GP4_16                IP2SR4(0, 0)
#define FUNC_TAUD1I0               IP2SR4(0, 3)
#define FUNC_TAUD1O0               IP2SR4(0, 4)
#define FUNC_GP4_17                IP2SR4(4, 0)
#define FUNC_MSPI1CSS5             IP2SR4(4, 1)
#define FUNC_TAUD1I3               IP2SR4(4, 3)
#define FUNC_TAUD1O3               IP2SR4(4, 4)
#define FUNC_GP4_18                IP2SR4(8, 0)
#define FUNC_MSPI1CSS4             IP2SR4(8, 1)
#define FUNC_TAUD1I2               IP2SR4(8, 3)
#define FUNC_TAUD1O2               IP2SR4(8, 4)
#define FUNC_GP4_19                IP2SR4(12, 0)
#define FUNC_MSPI1CSS6             IP2SR4(12, 1)
#define FUNC_TAUD1I4               IP2SR4(12, 3)
#define FUNC_TAUD1O4               IP2SR4(12, 4)
#define FUNC_MSPI0SC               IP2SR4(16, 0)
#define FUNC_MSPI1CSS7             IP2SR4(16, 1)
#define FUNC_TAUD1I5               IP2SR4(16, 3)
#define FUNC_TAUD1O5               IP2SR4(16, 4)
#define FUNC_MSPI0SI               IP2SR4(20, 0)
#define FUNC_TAUD1I7               IP2SR4(20, 3)
#define FUNC_TAUD1O7               IP2SR4(20, 4)
#define FUNC_MSPI0SO_MSPI0DCS      IP2SR4(24, 0)
#define FUNC_TAUD1I6               IP2SR4(24, 3)
#define FUNC_TAUD1O6               IP2SR4(24, 4)
#define FUNC_MSPI0CSS1             IP2SR4(28, 0)
#define FUNC_TAUD1I9               IP2SR4(28, 3)
#define FUNC_TAUD1O9               IP2SR4(28, 4)
#define FUNC_MSPI0CSS0             IP3SR4(0, 0)
#define FUNC_MSPI0SSI_N            IP3SR4(0, 1)
#define FUNC_TAUD1I8               IP3SR4(0, 3)
#define FUNC_TAUD1O8               IP3SR4(0, 4)
#define FUNC_MSPI1SO_MSPI1DCS      IP3SR4(8, 0)
#define FUNC_MSPI0CSS3             IP3SR4(8, 2)
#define FUNC_TAUD1I11              IP3SR4(8, 3)
#define FUNC_TAUD1O11              IP3SR4(8, 4)
#define FUNC_MSPI1SC               IP3SR4(16, 0)
#define FUNC_MSPI0CSS2             IP3SR4(16, 2)
#define FUNC_TAUD1I10              IP3SR4(16, 3)
#define FUNC_TAUD1O10              IP3SR4(16, 4)
#define FUNC_RIIC0SCL              IP0SR5(0, 0)
#define FUNC_TAUD0I0               IP0SR5(0, 3)
#define FUNC_TAUD0O0               IP0SR5(0, 4)
#define FUNC_RIIC0SDA              IP0SR5(4, 0)
#define FUNC_TAUD0I1               IP0SR5(4, 3)
#define FUNC_TAUD0O1               IP0SR5(4, 4)
#define FUNC_ETNB0MD               IP0SR5(8, 0)
#define FUNC_ETNB0WOL              IP0SR5(12, 0)
#define FUNC_ETNB0LINKSTA          IP0SR5(16, 0)
#define FUNC_ETNB0MDC              IP0SR5(20, 0)
#define FUNC_ETNB0RXCLK            IP0SR5(24, 0)
#define FUNC_ETNB0CRS_DV           IP0SR5(24, 1)
#define FUNC_ETNB0TXCLK            IP0SR5(28, 0)
#define FUNC_ETNB0REFCLK           IP0SR5(28, 1)
#define FUNC_RLIN33TX              IP1SR6(0, 0)
#define FUNC_TAUJ3O3               IP1SR6(0, 3)
#define FUNC_TAUJ3I3               IP1SR6(0, 4)
#define FUNC_NMI1                  IP1SR6(0, 5)
#define FUNC_RLIN33RX_INTP19       IP1SR6(4, 0)
#define FUNC_TAUJ3O2               IP1SR6(4, 3)
#define FUNC_TAUJ3I2               IP1SR6(4, 4)
#define FUNC_RLIN32TX              IP1SR6(8, 0)
#define FUNC_TAUJ3O1               IP1SR6(8, 3)
#define FUNC_TAUJ3I1               IP1SR6(8, 4)
#define FUNC_RLIN32RX_INTP18       IP1SR6(12, 0)
#define FUNC_TAUJ3O0               IP1SR6(12, 3)
#define FUNC_TAUJ3I0               IP1SR6(12, 4)
#define FUNC_INTP35                IP1SR6(12, 5)
#define FUNC_RLIN31TX              IP1SR6(16, 0)
#define FUNC_TAUJ1I3               IP1SR6(16, 3)
#define FUNC_TAUJ1O3               IP1SR6(16, 4)
#define FUNC_INTP34                IP1SR6(16, 5)
#define FUNC_RLIN31RX_INTP17       IP1SR6(20, 0)
#define FUNC_TAUJ1I2               IP1SR6(20, 3)
#define FUNC_TAUJ1O2               IP1SR6(20, 4)
#define FUNC_INTP33                IP1SR6(20, 5)
#define FUNC_RLIN30TX              IP1SR6(24, 0)
#define FUNC_TAUJ1I1               IP1SR6(24, 3)
#define FUNC_TAUJ1O1               IP1SR6(24, 4)
#define FUNC_RLIN30RX_INTP16       IP1SR6(28, 0)
#define FUNC_TAUJ1I0               IP1SR6(28, 3)
#define FUNC_TAUJ1O0               IP1SR6(28, 4)
#define FUNC_FLXA0STPWT            IP2SR6(8, 2)
#define FUNC_CAN0TX                IP0SR7(0, 0)
#define FUNC_RSENT0SPCO            IP0SR7(0, 1)
#define FUNC_MSPI2SO_MSPI2DCS      IP0SR7(0, 3)
#define FUNC_CAN0RX_INTP0          IP0SR7(4, 0)
#define FUNC_RSENT0RX              IP0SR7(4, 1)
#define FUNC_RSENT0RX_RSENT0SPCO   IP0SR7(4, 2)
#define FUNC_MSPI2SC               IP0SR7(4, 3)
#define FUNC_CAN1TX                IP0SR7(8, 0)
#define FUNC_RSENT1SPCO            IP0SR7(8, 1)
#define FUNC_MSPI2SSI_N            IP0SR7(8, 3)
#define FUNC_MSPI2CSS0             IP0SR7(8, 4)
#define FUNC_CAN1RX_INTP1          IP0SR7(12, 0)
#define FUNC_RSENT1RX              IP0SR7(12, 1)
#define FUNC_RSENT1RX_RSENT1SPCO   IP0SR7(12, 2)
#define FUNC_MSPI2SI               IP0SR7(12, 3)
#define FUNC_CAN2TX                IP0SR7(16, 0)
#define FUNC_RSENT2SPCO            IP0SR7(16, 1)
#define FUNC_MSPI2CSS2             IP0SR7(16, 4)
#define FUNC_CAN2RX_INTP2          IP0SR7(20, 0)
#define FUNC_RSENT2RX              IP0SR7(20, 1)
#define FUNC_RSENT2RX_RSENT2SPCO   IP0SR7(20, 2)
#define FUNC_MSPI2CSS1             IP0SR7(20, 4)
#define FUNC_CAN3TX                IP0SR7(24, 0)
#define FUNC_RSENT3SPCO            IP0SR7(24, 1)
#define FUNC_MSPI2CSS4             IP0SR7(24, 4)
#define FUNC_CAN3RX_INTP3          IP0SR7(28, 0)
#define FUNC_RSENT3RX              IP0SR7(28, 1)
#define FUNC_RSENT3RX_RSENT3SPCO   IP0SR7(28, 2)
#define FUNC_MSPI2CSS3             IP0SR7(28, 4)
#define FUNC_CAN4TX                IP1SR7(0, 0)
#define FUNC_RSENT4SPCO            IP1SR7(0, 1)
#define FUNC_MSPI2CSS6             IP1SR7(0, 4)
#define FUNC_CAN4RX_INTP4          IP1SR7(4, 0)
#define FUNC_RSENT4RX              IP1SR7(4, 1)
#define FUNC_RSENT4RX_RSENT4SPCO   IP1SR7(4, 2)
#define FUNC_MSPI2CSS5             IP1SR7(4, 4)
#define FUNC_CAN5TX                IP1SR7(8, 0)
#define FUNC_RSENT5SPCO            IP1SR7(8, 1)
#define FUNC_CAN5RX_INTP5          IP1SR7(12, 0)
#define FUNC_RSENT5RX              IP1SR7(12, 1)
#define FUNC_RSENT5RX_RSENT5SPCO   IP1SR7(12, 2)
#define FUNC_MSPI2CSS7             IP1SR7(12, 4)
#define FUNC_CAN6TX                IP1SR7(16, 0)
#define FUNC_RSENT6SPCO            IP1SR7(16, 1)
#define FUNC_MSPI3SO_MSPI3DCS      IP1SR7(16, 3)
#define FUNC_CAN6RX_INTP6          IP1SR7(20, 0)
#define FUNC_RSENT6RX              IP1SR7(20, 1)
#define FUNC_RSENT6RX_RSENT6SPCO   IP1SR7(20, 2)
#define FUNC_MSPI3SC               IP1SR7(20, 3)
#define FUNC_CAN7TX                IP1SR7(24, 0)
#define FUNC_RSENT7SPCO            IP1SR7(24, 1)
#define FUNC_MSPI3SSI_N            IP1SR7(24, 3)
#define FUNC_CAN7RX_INTP7          IP1SR7(28, 0)
#define FUNC_RSENT7RX              IP1SR7(28, 1)
#define FUNC_RSENT7RX_RSENT7SPCO   IP1SR7(28, 2)
#define FUNC_MSPI3SI               IP1SR7(28, 3)
#define FUNC_CAN8TX                IP2SR7(0, 0)
#define FUNC_RLIN38TX              IP2SR7(0, 1)
#define FUNC_MSPI3CSS1             IP2SR7(0, 3)
#define FUNC_CAN8RX_INTP8          IP2SR7(4, 0)
#define FUNC_RLIN38RX_INTP24       IP2SR7(4, 1)
#define FUNC_MSPI3CSS0             IP2SR7(4, 3)
#define FUNC_CAN9TX                IP2SR7(8, 0)
#define FUNC_RLIN39TX              IP2SR7(8, 1)
#define FUNC_MSPI3CSS3             IP2SR7(8, 3)
#define FUNC_CAN9RX_INTP9          IP2SR7(12, 0)
#define FUNC_RLIN39RX_INTP25       IP2SR7(12, 1)
#define FUNC_MSPI3CSS2             IP2SR7(12, 3)
#define FUNC_CAN10TX               IP2SR7(16, 0)
#define FUNC_RLIN310TX             IP2SR7(16, 1)
#define FUNC_MSPI3CSS5             IP2SR7(16, 3)
#define FUNC_CAN10RX_INTP10        IP2SR7(20, 0)
#define FUNC_RLIN310RX_INTP26      IP2SR7(20, 1)
#define FUNC_MSPI3CSS4             IP2SR7(20, 3)
#define FUNC_CAN11TX               IP2SR7(24, 0)
#define FUNC_RLIN311TX             IP2SR7(24, 1)
#define FUNC_MSPI3CSS7             IP2SR7(24, 3)
#define FUNC_CAN11RX_INTP11        IP2SR7(28, 0)
#define FUNC_RLIN311RX_INTP27      IP2SR7(28, 1)
#define FUNC_MSPI3CSS6             IP2SR7(28, 3)
#define FUNC_FLXA0RXDB             IP3SR7(8, 2)
#define FUNC_FLXA0RXDA             IP3SR7(12, 2)
#define FUNC_FLXA0TXDB             IP3SR7(16, 2)
#define FUNC_FLXA0TXDA             IP3SR7(20, 2)
#define FUNC_FLXA0TXENB            IP3SR7(24, 2)
#define FUNC_FLXA0TXENA            IP3SR7(28, 2)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_R8A779F0_H_ */
```

## 65.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 IoT.bzh。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 20 行

引脚声明（Pins declaration）。

### 注释 3：原第 212 行

引脚复用功能声明（Pinmux function declarations）。

### 注释 4：原第 562 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_R8A779F0_H_`。

## 65.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-r8a779f0_8h.html)
- [pinctrl-rcar-common.h](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rcar-common_8h.html)

---

[上一章](P064_pinctrl-r8a77961.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P066_pinctrl-r8a779g0.h_源码浏览.md)
