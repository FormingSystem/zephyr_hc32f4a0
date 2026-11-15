---
id: learning.zephyr-docs.api-source-reference.page-23
title: alif-ensemble-e1c-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/alif-ensemble-e1c-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_alif-ensemble-e1c-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/alif-ensemble-e1c-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/alif-ensemble-e1c-pinctrl_8h.html)。

## 23.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00027"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="foldopen00056"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00140"></a>
<a id="l00147"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00412"></a>
<a id="l00414"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00446"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="l00468"></a>
<a id="l00470"></a>
<a id="l00471"></a>
<a id="l00472"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00505"></a>
<a id="l00506"></a>
<a id="l00507"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00532"></a>
<a id="l00533"></a>
<a id="l00534"></a>
<a id="l00535"></a>
<a id="l00536"></a>
<a id="l00537"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="l00541"></a>
<a id="l00542"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="l00545"></a>
<a id="l00546"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00552"></a>
<a id="l00553"></a>
<a id="l00554"></a>
<a id="l00555"></a>
<a id="l00556"></a>
<a id="l00557"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00561"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="l00566"></a>
<a id="l00568"></a>
<a id="l00569"></a>
<a id="l00570"></a>
<a id="l00571"></a>
<a id="l00572"></a>
<a id="l00573"></a>
<a id="l00574"></a>
<a id="l00575"></a>
<a id="l00577"></a>
<a id="l00578"></a>
<a id="l00579"></a>
<a id="l00580"></a>
<a id="l00581"></a>
<a id="l00582"></a>
<a id="l00583"></a>
<a id="l00584"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="l00588"></a>
<a id="l00589"></a>
<a id="l00590"></a>
<a id="l00591"></a>
<a id="l00592"></a>
<a id="l00593"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="l00597"></a>
<a id="l00598"></a>
<a id="l00599"></a>
<a id="l00600"></a>
<a id="l00601"></a>
<a id="l00602"></a>
<a id="l00604"></a>
<a id="l00605"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="l00608"></a>
<a id="l00609"></a>
<a id="l00610"></a>
<a id="l00611"></a>
<a id="l00613"></a>
<a id="l00614"></a>
<a id="l00615"></a>
<a id="l00616"></a>
<a id="l00617"></a>
<a id="l00618"></a>
<a id="l00619"></a>
<a id="l00620"></a>
<a id="l00622"></a>
<a id="l00623"></a>
<a id="l00624"></a>
<a id="l00625"></a>
<a id="l00626"></a>
<a id="l00627"></a>
<a id="l00628"></a>
<a id="l00629"></a>
<a id="l00631"></a>
<a id="l00632"></a>
<a id="l00633"></a>
<a id="l00634"></a>
<a id="l00635"></a>
<a id="l00636"></a>
<a id="l00637"></a>
<a id="l00638"></a>
<a id="l00640"></a>
<a id="l00641"></a>
<a id="l00642"></a>
<a id="l00643"></a>
<a id="l00644"></a>
<a id="l00645"></a>
<a id="l00646"></a>
<a id="l00647"></a>
<a id="l00649"></a>
<a id="l00650"></a>
<a id="l00651"></a>
<a id="l00652"></a>
<a id="l00653"></a>
<a id="l00654"></a>
<a id="l00655"></a>
<a id="l00656"></a>
<a id="l00658"></a>
<a id="l00659"></a>
<a id="l00660"></a>
<a id="l00661"></a>
<a id="l00662"></a>
<a id="l00663"></a>
<a id="l00664"></a>
<a id="l00665"></a>
<a id="l00667"></a>
<a id="l00668"></a>
<a id="l00669"></a>
<a id="l00670"></a>
<a id="l00671"></a>
<a id="l00672"></a>
<a id="l00673"></a>
<a id="l00674"></a>
<a id="l00676"></a>
<a id="l00677"></a>
<a id="l00678"></a>
<a id="l00679"></a>
<a id="l00680"></a>
<a id="l00681"></a>
<a id="l00682"></a>
<a id="l00683"></a>
<a id="l00684"></a>
<a id="l00686"></a>
<a id="l00687"></a>
<a id="l00688"></a>
<a id="l00689"></a>
<a id="l00690"></a>
<a id="l00691"></a>
<a id="l00692"></a>
<a id="l00693"></a>
<a id="l00694"></a>
<a id="l00696"></a>
<a id="l00697"></a>
<a id="l00698"></a>
<a id="l00699"></a>
<a id="l00700"></a>
<a id="l00701"></a>
<a id="l00702"></a>
<a id="l00703"></a>
<a id="l00704"></a>
<a id="l00706"></a>
<a id="l00707"></a>
<a id="l00708"></a>
<a id="l00709"></a>
<a id="l00710"></a>
<a id="l00711"></a>
<a id="l00712"></a>
<a id="l00713"></a>
<a id="l00714"></a>
<a id="l00716"></a>
<a id="l00717"></a>
<a id="l00718"></a>
<a id="l00719"></a>
<a id="l00720"></a>
<a id="l00721"></a>
<a id="l00722"></a>
<a id="l00723"></a>
<a id="l00724"></a>
<a id="l00726"></a>
<a id="l00727"></a>
<a id="l00728"></a>
<a id="l00729"></a>
<a id="l00730"></a>
<a id="l00731"></a>
<a id="l00732"></a>
<a id="l00733"></a>
<a id="l00734"></a>
<a id="l00736"></a>
<a id="l00744"></a>
<a id="l00746"></a>
<a id="l00747"></a>
<a id="l00749"></a>
<a id="l00750"></a>
<a id="l00752"></a>
<a id="l00753"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright Alif Semiconductor
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ALIF_ENSEMBLE_E1C_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ALIF_ENSEMBLE_E1C_PINCTRL_H_



#define ALIF_PINMUX_FUNC_POS    0U
#define ALIF_PINMUX_FUNC_MASK   0x7U
#define ALIF_PINMUX_PIN_POS     3U
#define ALIF_PINMUX_PIN_MASK    0x7U
#define ALIF_PINMUX_PORT_POS    6U
#define ALIF_PINMUX_PORT_MASK   0x1FU


#define ALIF_PINMUX(port, pin, func)                                    \
        ((((port) & ALIF_PINMUX_PORT_MASK) << ALIF_PINMUX_PORT_POS) |   \
        (((pin) & ALIF_PINMUX_PIN_MASK) << ALIF_PINMUX_PIN_POS) |       \
        (((func) & ALIF_PINMUX_FUNC_MASK) << ALIF_PINMUX_FUNC_POS))


#define PIN_P0_0__GPIO                  ALIF_PINMUX(0, 0, 0)
#define PIN_P0_0__SEUART_RX_A           ALIF_PINMUX(0, 0, 1)
#define PIN_P0_0__UART0_RX_A            ALIF_PINMUX(0, 0, 2)
#define PIN_P0_0__LPI2S_SDI_A           ALIF_PINMUX(0, 0, 3)
#define PIN_P0_0__SPI0_SS0_A            ALIF_PINMUX(0, 0, 4)
#define PIN_P0_0__LPI2C0_SCL_A          ALIF_PINMUX(0, 0, 5)
#define PIN_P0_0__ANA_S0                ALIF_PINMUX(0, 0, 6)

#define PIN_P0_1__GPIO                  ALIF_PINMUX(0, 1, 0)
#define PIN_P0_1__SEUART_TX_A           ALIF_PINMUX(0, 1, 1)
#define PIN_P0_1__UART0_TX_A            ALIF_PINMUX(0, 1, 2)
#define PIN_P0_1__LPI2S_SDO_A           ALIF_PINMUX(0, 1, 3)
#define PIN_P0_1__SPI0_SS1_A            ALIF_PINMUX(0, 1, 4)
#define PIN_P0_1__LPI2C0_SDA_A          ALIF_PINMUX(0, 1, 5)
#define PIN_P0_1__ANA_S1                ALIF_PINMUX(0, 1, 6)

#define PIN_P0_2__GPIO                  ALIF_PINMUX(0, 2, 0)
#define PIN_P0_2__JTAG1_TDI             ALIF_PINMUX(0, 2, 1)
#define PIN_P0_2__OSPI0_SS0_A           ALIF_PINMUX(0, 2, 2)
#define PIN_P0_2__UART0_CTS_A           ALIF_PINMUX(0, 2, 3)
#define PIN_P0_2__LPI2S_SCLK_A          ALIF_PINMUX(0, 2, 4)
#define PIN_P0_2__SPI0_SS2_A            ALIF_PINMUX(0, 2, 5)
#define PIN_P0_2__ANA_S2                ALIF_PINMUX(0, 2, 6)

#define PIN_P0_3__GPIO                  ALIF_PINMUX(0, 3, 0)
#define PIN_P0_3__JTAG1_TDO             ALIF_PINMUX(0, 3, 1)
#define PIN_P0_3__OSPI0_SS1_A           ALIF_PINMUX(0, 3, 2)
#define PIN_P0_3__UART0_RTS_A           ALIF_PINMUX(0, 3, 3)
#define PIN_P0_3__LPI2S_WS_A            ALIF_PINMUX(0, 3, 4)
#define PIN_P0_3__SPI1_SS0_A            ALIF_PINMUX(0, 3, 5)
#define PIN_P0_3__ANA_S3                ALIF_PINMUX(0, 3, 6)

#define PIN_P0_4__GPIO                  ALIF_PINMUX(0, 4, 0)
#define PIN_P0_4__JTAG1_TRST            ALIF_PINMUX(0, 4, 1)
#define PIN_P0_4__UART1_RX_A            ALIF_PINMUX(0, 4, 2)
#define PIN_P0_4__SPI1_SS1_A            ALIF_PINMUX(0, 4, 3)
#define PIN_P0_4__I2C0_SDA_A            ALIF_PINMUX(0, 4, 4)
#define PIN_P0_4__FAULT0_A              ALIF_PINMUX(0, 4, 5)
#define PIN_P0_4__ANA_S4                ALIF_PINMUX(0, 4, 6)

#define PIN_P0_5__GPIO                  ALIF_PINMUX(0, 5, 0)
#define PIN_P0_5__JTAG1_TCK             ALIF_PINMUX(0, 5, 1)
#define PIN_P0_5__UART1_TX_A            ALIF_PINMUX(0, 5, 2)
#define PIN_P0_5__SPI1_SS2_A            ALIF_PINMUX(0, 5, 3)
#define PIN_P0_5__I2C0_SCL_A            ALIF_PINMUX(0, 5, 4)
#define PIN_P0_5__I3C_SCL_A             ALIF_PINMUX(0, 5, 5)
#define PIN_P0_5__ANA_S5                ALIF_PINMUX(0, 5, 6)

#define PIN_P0_6__GPIO                  ALIF_PINMUX(0, 6, 0)
#define PIN_P0_6__JTAG1_TMS             ALIF_PINMUX(0, 6, 1)
#define PIN_P0_6__UART1_CTS_A           ALIF_PINMUX(0, 6, 2)
#define PIN_P0_6__I2C1_SDA_A            ALIF_PINMUX(0, 6, 3)
#define PIN_P0_6__FAULT2_A              ALIF_PINMUX(0, 6, 4)
#define PIN_P0_6__I3C_SDA_A             ALIF_PINMUX(0, 6, 5)
#define PIN_P0_6__ANA_S6                ALIF_PINMUX(0, 6, 6)

#define PIN_P0_7__GPIO                  ALIF_PINMUX(0, 7, 0)
#define PIN_P0_7__UART1_RTS_A           ALIF_PINMUX(0, 7, 1)
#define PIN_P0_7__I2C1_SCL_A            ALIF_PINMUX(0, 7, 2)
#define PIN_P0_7__FAULT3_A              ALIF_PINMUX(0, 7, 3)
#define PIN_P0_7__LPCAM_VSYNC_B         ALIF_PINMUX(0, 7, 4)
#define PIN_P0_7__ANA_S7                ALIF_PINMUX(0, 7, 6)



#define PIN_P1_0__GPIO                  ALIF_PINMUX(1, 0, 0)
#define PIN_P1_0__OSPI0_D0_A            ALIF_PINMUX(1, 0, 1)
#define PIN_P1_0__UART2_RX_A            ALIF_PINMUX(1, 0, 2)
#define PIN_P1_0__LPPDM_D0_A            ALIF_PINMUX(1, 0, 3)
#define PIN_P1_0__LPI2S_SDI_B           ALIF_PINMUX(1, 0, 4)
#define PIN_P1_0__SPI0_MISO_A           ALIF_PINMUX(1, 0, 5)
#define PIN_P1_0__LPCAM_D0_A            ALIF_PINMUX(1, 0, 6)
#define PIN_P1_0__SD_D0_A               ALIF_PINMUX(1, 0, 7)

#define PIN_P1_1__GPIO                  ALIF_PINMUX(1, 1, 0)
#define PIN_P1_1__OSPI0_D1_A            ALIF_PINMUX(1, 1, 1)
#define PIN_P1_1__UART2_TX_A            ALIF_PINMUX(1, 1, 2)
#define PIN_P1_1__LPPDM_C0_A            ALIF_PINMUX(1, 1, 3)
#define PIN_P1_1__LPI2S_SDO_B           ALIF_PINMUX(1, 1, 4)
#define PIN_P1_1__SPI0_MOSI_A           ALIF_PINMUX(1, 1, 5)
#define PIN_P1_1__LPCAM_D1_A            ALIF_PINMUX(1, 1, 6)
#define PIN_P1_1__SD_D1_A               ALIF_PINMUX(1, 1, 7)

#define PIN_P1_2__GPIO                  ALIF_PINMUX(1, 2, 0)
#define PIN_P1_2__OSPI0_D2_A            ALIF_PINMUX(1, 2, 1)
#define PIN_P1_2__LPPDM_D1_A            ALIF_PINMUX(1, 2, 2)
#define PIN_P1_2__LPI2S_SCLK_B          ALIF_PINMUX(1, 2, 3)
#define PIN_P1_2__SPI0_SCLK_A           ALIF_PINMUX(1, 2, 4)
#define PIN_P1_2__LPCAM_D2_A            ALIF_PINMUX(1, 2, 5)
#define PIN_P1_2__SD_D2_A               ALIF_PINMUX(1, 2, 6)
#define PIN_P1_2__CX_MWS_SF0            ALIF_PINMUX(1, 2, 7)

#define PIN_P1_3__GPIO                  ALIF_PINMUX(1, 3, 0)
#define PIN_P1_3__LPUART_RTS_A          ALIF_PINMUX(1, 3, 1)
#define PIN_P1_3__LPPDM_C1_A            ALIF_PINMUX(1, 3, 2)
#define PIN_P1_3__I2S1_SCLK_SLV_A       ALIF_PINMUX(1, 3, 3)
#define PIN_P1_3__LPSPI_MISO_A          ALIF_PINMUX(1, 3, 4)
#define PIN_P1_3__CAN1_RXD_A            ALIF_PINMUX(1, 3, 5)
#define PIN_P1_3__CX_MWS_SF0            ALIF_PINMUX(1, 3, 6)

#define PIN_P1_4__GPIO                  ALIF_PINMUX(1, 4, 0)
#define PIN_P1_4__LPPDM_C2_A            ALIF_PINMUX(1, 4, 1)
#define PIN_P1_4__I2S0_SDI_A            ALIF_PINMUX(1, 4, 2)
#define PIN_P1_4__LPSPI_MOSI_A          ALIF_PINMUX(1, 4, 3)
#define PIN_P1_4__I2C1_SDA_A            ALIF_PINMUX(1, 4, 4)
#define PIN_P1_4__CDC_PCLK_A            ALIF_PINMUX(1, 4, 5)
#define PIN_P1_4__CAN1_TXD_A            ALIF_PINMUX(1, 4, 6)
#define PIN_P1_4__CX_MWS_SF1            ALIF_PINMUX(1, 4, 7)

#define PIN_P1_5__GPIO                  ALIF_PINMUX(1, 5, 0)
#define PIN_P1_5__LPPDM_D2_A            ALIF_PINMUX(1, 5, 1)
#define PIN_P1_5__I2S0_SDO_A            ALIF_PINMUX(1, 5, 2)
#define PIN_P1_5__LPSPI_SCLK_A          ALIF_PINMUX(1, 5, 3)
#define PIN_P1_5__I2C1_SCLA_A           ALIF_PINMUX(1, 5, 4)
#define PIN_P1_5__SD_RST_A              ALIF_PINMUX(1, 5, 5)
#define PIN_P1_5__CDC_DE_A              ALIF_PINMUX(1, 5, 6)
#define PIN_P1_5__CAN1_STBY_A           ALIF_PINMUX(1, 5, 7)

#define PIN_P1_6__GPIO                  ALIF_PINMUX(1, 6, 0)
#define PIN_P1_6__UART2_RX_A            ALIF_PINMUX(1, 6, 1)
#define PIN_P1_6__LPPDM_C3_A            ALIF_PINMUX(1, 6, 2)
#define PIN_P1_6__I2S0_SCLK_A           ALIF_PINMUX(1, 6, 3)
#define PIN_P1_6__LPCAM_D6_A            ALIF_PINMUX(1, 6, 4)
#define PIN_P1_6__CDC_HSYNC_A           ALIF_PINMUX(1, 6, 5)
#define PIN_P1_6__I3C_SDA_B             ALIF_PINMUX(1, 6, 6)
#define PIN_P1_6__CX_MWS_SF2            ALIF_PINMUX(1, 6, 7)

#define PIN_P1_7__GPIO                  ALIF_PINMUX(1, 7, 0)
#define PIN_P1_7__UART2_TX_A            ALIF_PINMUX(1, 7, 1)
#define PIN_P1_7__LPPDM_D3_A            ALIF_PINMUX(1, 7, 2)
#define PIN_P1_7__I2S0_WS_A             ALIF_PINMUX(1, 7, 3)
#define PIN_P1_7__LPCAM_D7_A            ALIF_PINMUX(1, 7, 4)
#define PIN_P1_7__CDC_VSYNC_A           ALIF_PINMUX(1, 7, 5)
#define PIN_P1_7__I3C_SCL_B             ALIF_PINMUX(1, 7, 6)
#define PIN_P1_7__CX_MWS_SF3            ALIF_PINMUX(1, 7, 7)

#define PIN_P2_0__GPIO                  ALIF_PINMUX(2, 0, 0)
#define PIN_P2_0__OSPI0_SS0_B           ALIF_PINMUX(2, 0, 1)
#define PIN_P2_0__LPUART_RX_A           ALIF_PINMUX(2, 0, 2)
#define PIN_P2_0__I2S1_SDI_A            ALIF_PINMUX(2, 0, 3)
#define PIN_P2_0__LPSPI_SS_A            ALIF_PINMUX(2, 0, 4)
#define PIN_P2_0__LPCAM_HSYNC_B         ALIF_PINMUX(2, 0, 5)
#define PIN_P2_0__ANA_S8                ALIF_PINMUX(2, 0, 6)
#define PIN_P2_0__CX_MWS_SF4            ALIF_PINMUX(2, 0, 7)

#define PIN_P2_1__GPIO                  ALIF_PINMUX(2, 1, 0)
#define PIN_P2_1__OSPI0_SS1_B           ALIF_PINMUX(2, 1, 1)
#define PIN_P2_1__LPUART_TX_A           ALIF_PINMUX(2, 1, 2)
#define PIN_P2_1__I2S1_SDO_A            ALIF_PINMUX(2, 1, 3)
#define PIN_P2_1__LPI2C0_SCL_B          ALIF_PINMUX(2, 1, 4)
#define PIN_P2_1__UT0_T1_A              ALIF_PINMUX(2, 1, 5)
#define PIN_P2_1__ANA_S9                ALIF_PINMUX(2, 1, 6)
#define PIN_P2_1__CX_MWS_PAT0           ALIF_PINMUX(2, 1, 7)

#define PIN_P2_2__GPIO                  ALIF_PINMUX(2, 2, 0)
#define PIN_P2_2__LPUART_RTS_A          ALIF_PINMUX(2, 2, 1)
#define PIN_P2_2__I2S1_SCLK_SLV_A       ALIF_PINMUX(2, 2, 2)
#define PIN_P2_2__LPI2C0_SDA_B          ALIF_PINMUX(2, 2, 3)
#define PIN_P2_2__UT1_T0_A              ALIF_PINMUX(2, 2, 4)
#define PIN_P2_2__ANA_S10               ALIF_PINMUX(2, 2, 5)
#define PIN_P2_2__CX_MWS_PAT1           ALIF_PINMUX(2, 2, 6)

#define PIN_P2_3__GPIO                  ALIF_PINMUX(2, 3, 0)
#define PIN_P2_3__LPUART_CTS_A          ALIF_PINMUX(2, 3, 1)
#define PIN_P2_3__I2S1_WS_SLV_A         ALIF_PINMUX(2, 3, 2)
#define PIN_P2_3__UT1_T1_A              ALIF_PINMUX(2, 3, 3)
#define PIN_P2_3__SD_RST_A              ALIF_PINMUX(2, 3, 4)
#define PIN_P2_3__CAN0_RXD_A            ALIF_PINMUX(2, 3, 5)
#define PIN_P2_3__ANA_S11               ALIF_PINMUX(2, 3, 6)
#define PIN_P2_3__CX_MWS_SYNC           ALIF_PINMUX(2, 3, 7)

#define PIN_P2_4__GPIO                  ALIF_PINMUX(2, 4, 0)
#define PIN_P2_4__UART3_RX_A            ALIF_PINMUX(2, 4, 1)
#define PIN_P2_4__I2S0_SDI_B            ALIF_PINMUX(2, 4, 2)
#define PIN_P2_4__I2C0_SCL_B            ALIF_PINMUX(2, 4, 3)
#define PIN_P2_4__UT2_T0_A              ALIF_PINMUX(2, 4, 4)
#define PIN_P2_4__CAN0_TXD_A            ALIF_PINMUX(2, 4, 5)
#define PIN_P2_4__ANA_S12               ALIF_PINMUX(2, 4, 6)
#define PIN_P2_4__CX_MWS_TX             ALIF_PINMUX(2, 4, 7)

#define PIN_P2_5__GPIO                  ALIF_PINMUX(2, 5, 0)
#define PIN_P2_5__UART3_TX_A            ALIF_PINMUX(2, 5, 1)
#define PIN_P2_5__I2S0_SDO_B            ALIF_PINMUX(2, 5, 2)
#define PIN_P2_5__I2C0_SDA_B            ALIF_PINMUX(2, 5, 3)
#define PIN_P2_5__UT2_T1_A              ALIF_PINMUX(2, 5, 4)
#define PIN_P2_5__CAN0_STBY_A           ALIF_PINMUX(2, 5, 5)
#define PIN_P2_5__ANA_S13               ALIF_PINMUX(2, 5, 6)
#define PIN_P2_5__CX_MWS_RX             ALIF_PINMUX(2, 5, 7)

#define PIN_P2_6__GPIO                  ALIF_PINMUX(2, 6, 0)
#define PIN_P2_6__UART4_RX_A            ALIF_PINMUX(2, 6, 1)
#define PIN_P2_6__I2S0_SCLK_B           ALIF_PINMUX(2, 6, 2)
#define PIN_P2_6__I2C1_SDA_B            ALIF_PINMUX(2, 6, 3)
#define PIN_P2_6__UT3_T0_A              ALIF_PINMUX(2, 6, 4)
#define PIN_P2_6__ANA_S14               ALIF_PINMUX(2, 6, 6)

#define PIN_P2_7__GPIO                  ALIF_PINMUX(2, 7, 0)
#define PIN_P2_7__UART4_TX_A            ALIF_PINMUX(2, 7, 1)
#define PIN_P2_7__I2S0_WS_B             ALIF_PINMUX(2, 7, 2)
#define PIN_P2_7__I2C1_SCL_B            ALIF_PINMUX(2, 7, 3)
#define PIN_P2_7__UT3_T1_A              ALIF_PINMUX(2, 7, 4)
#define PIN_P2_7__ANA_S15               ALIF_PINMUX(2, 7, 6)

#define PIN_P3_0__GPIO                  ALIF_PINMUX(3, 0, 0)
#define PIN_P3_0__OSPI0_D0_A            ALIF_PINMUX(3, 0, 1)
#define PIN_P3_0__UART5_RX_A            ALIF_PINMUX(3, 0, 2)
#define PIN_P3_0__LPPDM_C0_B            ALIF_PINMUX(3, 0, 3)
#define PIN_P3_0__I2S1_SDI_B            ALIF_PINMUX(3, 0, 4)
#define PIN_P3_0__SPI2_MISO_A           ALIF_PINMUX(3, 0, 5)
#define PIN_P3_0__CDC_HSYNC_B           ALIF_PINMUX(3, 0, 6)

#define PIN_P3_1__GPIO                  ALIF_PINMUX(3, 1, 0)
#define PIN_P3_1__OSPI0_D1_A            ALIF_PINMUX(3, 1, 1)
#define PIN_P3_1__UART5_TX_A            ALIF_PINMUX(3, 1, 2)
#define PIN_P3_1__LPPDM_D0_B            ALIF_PINMUX(3, 1, 3)
#define PIN_P3_1__I2S1_SDO_B            ALIF_PINMUX(3, 1, 4)
#define PIN_P3_1__SPI2_MOSI_A           ALIF_PINMUX(3, 1, 5)
#define PIN_P3_1__CDC_VSYNC_B           ALIF_PINMUX(3, 1, 6)

#define PIN_P3_2__GPIO                  ALIF_PINMUX(3, 2, 0)
#define PIN_P3_2__OSPI0_D2_A            ALIF_PINMUX(3, 2, 1)
#define PIN_P3_2__UART3_RX_B            ALIF_PINMUX(3, 2, 2)
#define PIN_P3_2__LPPDM_C1_B            ALIF_PINMUX(3, 2, 3)
#define PIN_P3_2__I2S1_SCLK_SLV_B       ALIF_PINMUX(3, 2, 4)
#define PIN_P3_2__SPI2_SCLK_A           ALIF_PINMUX(3, 2, 5)
#define PIN_P3_2__CDC_PCLK_B            ALIF_PINMUX(3, 2, 6)

#define PIN_P3_3__GPIO                  ALIF_PINMUX(3, 3, 0)
#define PIN_P3_3__OSPI0_D3_A            ALIF_PINMUX(3, 3, 1)
#define PIN_P3_3__UART3_TX_B            ALIF_PINMUX(3, 3, 2)
#define PIN_P3_3__LPPDM_D1_B            ALIF_PINMUX(3, 3, 3)
#define PIN_P3_3__I2S1_WS_SLV_B         ALIF_PINMUX(3, 3, 4)
#define PIN_P3_3__SPI2_SS0_A            ALIF_PINMUX(3, 3, 5)
#define PIN_P3_3__CDC_DE_B              ALIF_PINMUX(3, 3, 6)

#define PIN_P3_4__GPIO                  ALIF_PINMUX(3, 4, 0)
#define PIN_P3_4__OSPI0_D4_A            ALIF_PINMUX(3, 4, 1)
#define PIN_P3_4__LPPDM_C2_B            ALIF_PINMUX(3, 4, 2)
#define PIN_P3_4__SPI1_MISO_A           ALIF_PINMUX(3, 4, 3)
#define PIN_P3_4__LPCAM_VSYNC_A         ALIF_PINMUX(3, 4, 4)
#define PIN_P3_4__SD_CMD_A              ALIF_PINMUX(3, 4, 5)
#define PIN_P3_4__CMP0_OUT_A            ALIF_PINMUX(3, 4, 6)

#define PIN_P3_5__GPIO                  ALIF_PINMUX(3, 5, 0)
#define PIN_P3_5__OSPI0_D5_A            ALIF_PINMUX(3, 5, 1)
#define PIN_P3_5__LPPDM_D2_B            ALIF_PINMUX(3, 5, 2)
#define PIN_P3_5__SPI1_MOSI_A           ALIF_PINMUX(3, 5, 3)
#define PIN_P3_5__LPCAM_HSYNC_A         ALIF_PINMUX(3, 5, 4)
#define PIN_P3_5__SD_CLK_A              ALIF_PINMUX(3, 5, 5)
#define PIN_P3_5__CMP1_OUT_A            ALIF_PINMUX(3, 5, 6)

#define PIN_P3_6__GPIO                  ALIF_PINMUX(3, 6, 0)
#define PIN_P3_6__OSPI0_D6_A            ALIF_PINMUX(3, 6, 1)
#define PIN_P3_6__UART4_RX_B            ALIF_PINMUX(3, 6, 2)
#define PIN_P3_6__LPPDM_C3_B            ALIF_PINMUX(3, 6, 3)
#define PIN_P3_6__SPI1_SCLK_A           ALIF_PINMUX(3, 6, 4)
#define PIN_P3_6__LPCAM_PCLK_A          ALIF_PINMUX(3, 6, 5)
#define PIN_P3_6__EXT_RTS_A             ALIF_PINMUX(3, 6, 6)
#define PIN_P3_6__CX_WLAN_TX            ALIF_PINMUX(3, 6, 7)

#define PIN_P3_7__GPIO                  ALIF_PINMUX(3, 7, 0)
#define PIN_P3_7__OSPI0_D7_A            ALIF_PINMUX(3, 7, 1)
#define PIN_P3_7__UART4_TX_B            ALIF_PINMUX(3, 7, 2)
#define PIN_P3_7__LPPDM_D3_B            ALIF_PINMUX(3, 7, 3)
#define PIN_P3_7__LPCAM_XVCLK_A         ALIF_PINMUX(3, 7, 4)
#define PIN_P3_7__SD_RST_B              ALIF_PINMUX(3, 7, 5)
#define PIN_P3_7__EXT_CTS_A             ALIF_PINMUX(3, 7, 6)
#define PIN_P3_7__CX_WLAN_RX            ALIF_PINMUX(3, 7, 7)

#define PIN_P4_0__GPIO                  ALIF_PINMUX(4, 0, 0)
#define PIN_P4_0__OSPI0_SCLKN_A         ALIF_PINMUX(4, 0, 1)
#define PIN_P4_0__UART0_RX_B            ALIF_PINMUX(4, 0, 2)
#define PIN_P4_0__SPI2_SS1_A            ALIF_PINMUX(4, 0, 3)
#define PIN_P4_0__UT0_T0_A              ALIF_PINMUX(4, 0, 4)
#define PIN_P4_0__LPCAM_D0_A            ALIF_PINMUX(4, 0, 5)
#define PIN_P4_0__SD_D0_A               ALIF_PINMUX(4, 0, 6)
#define PIN_P4_0__EXT_RX_A              ALIF_PINMUX(4, 0, 7)

#define PIN_P4_1__GPIO                  ALIF_PINMUX(4, 1, 0)
#define PIN_P4_1__OSPI0_RXDS_A          ALIF_PINMUX(4, 1, 1)
#define PIN_P4_1__UART0_TX_B            ALIF_PINMUX(4, 1, 2)
#define PIN_P4_1__SPI2_SS2_A            ALIF_PINMUX(4, 1, 3)
#define PIN_P4_1__UT0_T1_A              ALIF_PINMUX(4, 1, 4)
#define PIN_P4_1__LPCAM_D1_A            ALIF_PINMUX(4, 1, 5)
#define PIN_P4_1__SD_D1_A               ALIF_PINMUX(4, 1, 6)
#define PIN_P4_1__EXT_TX_A              ALIF_PINMUX(4, 1, 7)

#define PIN_P4_2__GPIO                  ALIF_PINMUX(4, 2, 0)
#define PIN_P4_2__HFXO_OUT_A            ALIF_PINMUX(4, 2, 1)
#define PIN_P4_2__OSPI0_SCLK_A          ALIF_PINMUX(4, 2, 2)
#define PIN_P4_2__UART4_DE_A            ALIF_PINMUX(4, 2, 3)
#define PIN_P4_2__UT1_T0_A              ALIF_PINMUX(4, 2, 4)
#define PIN_P4_2__LPCAM_D2_A            ALIF_PINMUX(4, 2, 5)
#define PIN_P4_2__SD_D2_A               ALIF_PINMUX(4, 2, 6)
#define PIN_P4_2__EXT_TRACE_A           ALIF_PINMUX(4, 2, 7)

#define PIN_P4_3__GPIO                  ALIF_PINMUX(4, 3, 0)
#define PIN_P4_3__JTAG0_NSRST           ALIF_PINMUX(4, 3, 1)
#define PIN_P4_3__CS_MWS_ID0            ALIF_PINMUX(4, 3, 2)
#define PIN_P4_3__UT1_T1_A              ALIF_PINMUX(4, 3, 3)
#define PIN_P4_3__CMP0_OUT_B            ALIF_PINMUX(4, 3, 6)

#define PIN_P4_4__GPIO                  ALIF_PINMUX(4, 4, 0)
#define PIN_P4_4__JTAG0_TCK             ALIF_PINMUX(4, 4, 1)
#define PIN_P4_4__FAULT0_B              ALIF_PINMUX(4, 4, 2)
#define PIN_P4_4__CS_MWS_ID1            ALIF_PINMUX(4, 4, 3)
#define PIN_P4_4__UT2_T0_A              ALIF_PINMUX(4, 4, 4)

#define PIN_P4_5__GPIO                  ALIF_PINMUX(4, 5, 0)
#define PIN_P4_5__JTAG0_TMS             ALIF_PINMUX(4, 5, 1)
#define PIN_P4_5__FAULT1_B              ALIF_PINMUX(4, 5, 2)
#define PIN_P4_5__CS_MWS_ID2            ALIF_PINMUX(4, 5, 3)
#define PIN_P4_5__UT2_T1_A              ALIF_PINMUX(4, 5, 4)

#define PIN_P4_6__GPIO                  ALIF_PINMUX(4, 6, 0)
#define PIN_P4_6__JTAG0_TDI             ALIF_PINMUX(4, 6, 1)
#define PIN_P4_6__FAULT2_B              ALIF_PINMUX(4, 6, 2)
#define PIN_P4_6__LPI2S_WS_B            ALIF_PINMUX(4, 6, 3)
#define PIN_P4_6__UT3_T0_A              ALIF_PINMUX(4, 6, 4)

#define PIN_P4_7__GPIO                  ALIF_PINMUX(4, 7, 0)
#define PIN_P4_7__JTAG0_TDO             ALIF_PINMUX(4, 7, 1)
#define PIN_P4_7__FAULT3_B              ALIF_PINMUX(4, 7, 2)
#define PIN_P4_7__UT3_T1_A              ALIF_PINMUX(4, 7, 3)
#define PIN_P4_7__CS_MWS_ID4            ALIF_PINMUX(4, 7, 4)
#define PIN_P4_7__CMP1_OUT_B            ALIF_PINMUX(4, 7, 6)

#define PIN_P5_0__GPIO                  ALIF_PINMUX(5, 0, 0)
#define PIN_P5_0__OSPI0_D0_B            ALIF_PINMUX(5, 0, 1)
#define PIN_P5_0__UART1_RX_B            ALIF_PINMUX(5, 0, 2)
#define PIN_P5_0__SPI0_MISO_B           ALIF_PINMUX(5, 0, 3)
#define PIN_P5_0__CDC_D0_A              ALIF_PINMUX(5, 0, 4)
#define PIN_P5_0__CAN0_RXD_B            ALIF_PINMUX(5, 0, 5)
#define PIN_P5_0__DEBUG_PORT0           ALIF_PINMUX(5, 0, 6)

#define PIN_P5_1__GPIO                  ALIF_PINMUX(5, 1, 0)
#define PIN_P5_1__OSPI0_D1_B            ALIF_PINMUX(5, 1, 1)
#define PIN_P5_1__UART1_TX_B            ALIF_PINMUX(5, 1, 2)
#define PIN_P5_1__SPI0_MOSI_B           ALIF_PINMUX(5, 1, 3)
#define PIN_P5_1__CDC_D1_A              ALIF_PINMUX(5, 1, 4)
#define PIN_P5_1__CAN0_TXD_B            ALIF_PINMUX(5, 1, 5)
#define PIN_P5_1__DEBUG_PORT1           ALIF_PINMUX(5, 1, 6)

#define PIN_P5_2__GPIO                  ALIF_PINMUX(5, 2, 0)
#define PIN_P5_2__HFXO_OUT_B            ALIF_PINMUX(5, 2, 1)
#define PIN_P5_2__OSPI0_D2_B            ALIF_PINMUX(5, 2, 2)
#define PIN_P5_2__UART2_RX_B            ALIF_PINMUX(5, 2, 3)
#define PIN_P5_2__SPI0_SCLK_B           ALIF_PINMUX(5, 2, 4)
#define PIN_P5_2__CDC_D2_A              ALIF_PINMUX(5, 2, 5)
#define PIN_P5_2__DEBUG_PORT2           ALIF_PINMUX(5, 2, 6)

#define PIN_P5_3__GPIO                  ALIF_PINMUX(5, 3, 0)
#define PIN_P5_3__OSPI0_D3_B            ALIF_PINMUX(5, 3, 1)
#define PIN_P5_3__UART2_TX_B            ALIF_PINMUX(5, 3, 2)
#define PIN_P5_3__SPI0_SS0_B            ALIF_PINMUX(5, 3, 3)
#define PIN_P5_3__CDC_D3_A              ALIF_PINMUX(5, 3, 4)
#define PIN_P5_3__DEBUG_PORT3           ALIF_PINMUX(5, 3, 5)

#define PIN_P5_4__GPIO                  ALIF_PINMUX(5, 4, 0)
#define PIN_P5_4__OSPI0_D4_B            ALIF_PINMUX(5, 4, 1)
#define PIN_P5_4__UART3_CTS_A           ALIF_PINMUX(5, 4, 2)
#define PIN_P5_4__LPPDM_C0_C            ALIF_PINMUX(5, 4, 3)
#define PIN_P5_4__SPI0_SS1_B            ALIF_PINMUX(5, 4, 4)
#define PIN_P5_4__CDC_D4_A              ALIF_PINMUX(5, 4, 5)
#define PIN_P5_4__DEBUG_PORT4           ALIF_PINMUX(5, 4, 6)

#define PIN_P5_5__GPIO                  ALIF_PINMUX(5, 5, 0)
#define PIN_P5_5__OSPI0_D5_B            ALIF_PINMUX(5, 5, 1)
#define PIN_P5_5__UART3_RTS_A           ALIF_PINMUX(5, 5, 2)
#define PIN_P5_5__LPPDM_C1_C            ALIF_PINMUX(5, 5, 3)
#define PIN_P5_5__SPI0_SS2_B            ALIF_PINMUX(5, 5, 4)
#define PIN_P5_5__CDC_D5_A              ALIF_PINMUX(5, 5, 5)
#define PIN_P5_5__DEBUG_PORT5           ALIF_PINMUX(5, 5, 6)

#define PIN_P5_6__GPIO                  ALIF_PINMUX(5, 6, 0)
#define PIN_P5_6__OSPI0_D6_B            ALIF_PINMUX(5, 6, 1)
#define PIN_P5_6__UART1_CTS_B           ALIF_PINMUX(5, 6, 2)
#define PIN_P5_6__LPPDM_D0_C            ALIF_PINMUX(5, 6, 3)
#define PIN_P5_6__LPSPI_MISO_B          ALIF_PINMUX(5, 6, 4)
#define PIN_P5_6__CDC_D6_A              ALIF_PINMUX(5, 6, 5)
#define PIN_P5_6__DEBUG_PORT6           ALIF_PINMUX(5, 6, 6)

#define PIN_P5_7__GPIO                  ALIF_PINMUX(5, 7, 0)
#define PIN_P5_7__OSPI0_D7_B            ALIF_PINMUX(5, 7, 1)
#define PIN_P5_7__UART1_RTS_B           ALIF_PINMUX(5, 7, 2)
#define PIN_P5_7__LPPDM_D1_C            ALIF_PINMUX(5, 7, 3)
#define PIN_P5_7__LPSPI_MOSI_B          ALIF_PINMUX(5, 7, 4)
#define PIN_P5_7__CDC_D7_A              ALIF_PINMUX(5, 7, 5)
#define PIN_P5_7__DEBUG_PORT7           ALIF_PINMUX(5, 7, 6)

#define PIN_P6_0__GPIO                  ALIF_PINMUX(6, 0, 0)
#define PIN_P6_0__OSPI0_D0_C            ALIF_PINMUX(6, 0, 1)
#define PIN_P6_0__UART4_DE_B            ALIF_PINMUX(6, 0, 2)
#define PIN_P6_0__LPSPI_SS_B            ALIF_PINMUX(6, 0, 3)
#define PIN_P6_0__UT0_T0_B              ALIF_PINMUX(6, 0, 4)
#define PIN_P6_0__SD_D0_B               ALIF_PINMUX(6, 0, 5)
#define PIN_P6_0__CDC_D8_A              ALIF_PINMUX(6, 0, 6)

#define PIN_P6_1__GPIO                  ALIF_PINMUX(6, 1, 0)
#define PIN_P6_1__OSPI0_D1_C            ALIF_PINMUX(6, 1, 1)
#define PIN_P6_1__UART5_DE_A            ALIF_PINMUX(6, 1, 2)
#define PIN_P6_1__SPI1_MISO_B           ALIF_PINMUX(6, 1, 3)
#define PIN_P6_1__UT0_T1_B              ALIF_PINMUX(6, 1, 4)
#define PIN_P6_1__SD_D1_B               ALIF_PINMUX(6, 1, 5)
#define PIN_P6_1__CDC_D9_A              ALIF_PINMUX(6, 1, 6)

#define PIN_P6_2__GPIO                  ALIF_PINMUX(6, 2, 0)
#define PIN_P6_2__OSPI0_D2_C            ALIF_PINMUX(6, 2, 1)
#define PIN_P6_2__UART2_CTS_A           ALIF_PINMUX(6, 2, 2)
#define PIN_P6_2__SPI1_MOSI_B           ALIF_PINMUX(6, 2, 3)
#define PIN_P6_2__UT1_T0_B              ALIF_PINMUX(6, 2, 4)
#define PIN_P6_2__SD_D2_B               ALIF_PINMUX(6, 2, 5)
#define PIN_P6_2__CDC_D10_A             ALIF_PINMUX(6, 2, 6)

#define PIN_P6_3__GPIO                  ALIF_PINMUX(6, 3, 0)
#define PIN_P6_3__OSPI0_D3_C            ALIF_PINMUX(6, 3, 1)
#define PIN_P6_3__UART2_RTS_A           ALIF_PINMUX(6, 3, 2)
#define PIN_P6_3__SPI1_SCLK_B           ALIF_PINMUX(6, 3, 3)
#define PIN_P6_3__UT1_T1_B              ALIF_PINMUX(6, 3, 4)
#define PIN_P6_3__SD_D3_B               ALIF_PINMUX(6, 3, 5)
#define PIN_P6_3__CDC_D11_A             ALIF_PINMUX(6, 3, 6)

#define PIN_P6_4__GPIO                  ALIF_PINMUX(6, 4, 0)
#define PIN_P6_4__OSPI0_D4_C            ALIF_PINMUX(6, 4, 1)
#define PIN_P6_4__UART2_CTS_B           ALIF_PINMUX(6, 4, 2)
#define PIN_P6_4__SPI1_SS0_B            ALIF_PINMUX(6, 4, 3)
#define PIN_P6_4__UT2_T0_B              ALIF_PINMUX(6, 4, 4)
#define PIN_P6_4__SD_D4_B               ALIF_PINMUX(6, 4, 5)
#define PIN_P6_4__CDC_D12_A             ALIF_PINMUX(6, 4, 6)

#define PIN_P6_5__GPIO                  ALIF_PINMUX(6, 5, 0)
#define PIN_P6_5__OSPI0_D5_C            ALIF_PINMUX(6, 5, 1)
#define PIN_P6_5__UART2_RTS_B           ALIF_PINMUX(6, 5, 2)
#define PIN_P6_5__SPI1_SS1_B            ALIF_PINMUX(6, 5, 3)
#define PIN_P6_5__UT2_T1_B              ALIF_PINMUX(6, 5, 4)
#define PIN_P6_5__SD_D5_B               ALIF_PINMUX(6, 5, 5)
#define PIN_P6_5__CDC_D13_A             ALIF_PINMUX(6, 5, 6)

#define PIN_P6_6__GPIO                  ALIF_PINMUX(6, 6, 0)
#define PIN_P6_6__OSPI0_D6_C            ALIF_PINMUX(6, 6, 1)
#define PIN_P6_6__UART0_CTS_B           ALIF_PINMUX(6, 6, 2)
#define PIN_P6_6__SPI1_SS2_B            ALIF_PINMUX(6, 6, 3)
#define PIN_P6_6__UT3_T0_B              ALIF_PINMUX(6, 6, 4)
#define PIN_P6_6__SD_D6_B               ALIF_PINMUX(6, 6, 5)
#define PIN_P6_6__CDC_D14_A             ALIF_PINMUX(6, 6, 6)

#define PIN_P6_7__GPIO                  ALIF_PINMUX(6, 7, 0)
#define PIN_P6_7__OSPI0_D7_C            ALIF_PINMUX(6, 7, 1)
#define PIN_P6_7__UART0_RTS_B           ALIF_PINMUX(6, 7, 2)
#define PIN_P6_7__SPI2_SS2_C            ALIF_PINMUX(6, 7, 3)
#define PIN_P6_7__UT3_T1_B              ALIF_PINMUX(6, 7, 4)
#define PIN_P6_7__SD_D7_B               ALIF_PINMUX(6, 7, 5)
#define PIN_P6_7__CDC_D15_A             ALIF_PINMUX(6, 7, 6)

#define PIN_P7_0__GPIO                  ALIF_PINMUX(7, 0, 0)
#define PIN_P7_0__OSPI0_SCLK_C          ALIF_PINMUX(7, 0, 1)
#define PIN_P7_0__LPUART_RX_B           ALIF_PINMUX(7, 0, 2)
#define PIN_P7_0__SPI2_MISO_B           ALIF_PINMUX(7, 0, 3)
#define PIN_P7_0__I2C0_SDA_C            ALIF_PINMUX(7, 0, 4)
#define PIN_P7_0__LPCAM_D0_B            ALIF_PINMUX(7, 0, 5)
#define PIN_P7_0__CDC_D16_A             ALIF_PINMUX(7, 0, 6)

#define PIN_P7_1__GPIO                  ALIF_PINMUX(7, 1, 0)
#define PIN_P7_1__OSPI0_SCLKN_C         ALIF_PINMUX(7, 1, 1)
#define PIN_P7_1__LPUART_TX_B           ALIF_PINMUX(7, 1, 2)
#define PIN_P7_1__SPI2_MOSI_B           ALIF_PINMUX(7, 1, 3)
#define PIN_P7_1__I2C0_SCL_C            ALIF_PINMUX(7, 1, 4)
#define PIN_P7_1__LPCAM_D1_B            ALIF_PINMUX(7, 1, 5)
#define PIN_P7_1__CDC_D17_A             ALIF_PINMUX(7, 1, 6)

#define PIN_P7_2__GPIO                  ALIF_PINMUX(7, 2, 0)
#define PIN_P7_2__OSPI0_SS0_C           ALIF_PINMUX(7, 2, 1)
#define PIN_P7_2__LPUART_CTS_B          ALIF_PINMUX(7, 2, 2)
#define PIN_P7_2__SPI2_SCLK_B           ALIF_PINMUX(7, 2, 3)
#define PIN_P7_2__I2C1_SDA_C            ALIF_PINMUX(7, 2, 4)
#define PIN_P7_2__LPCAM_D2_B            ALIF_PINMUX(7, 2, 5)
#define PIN_P7_2__CDC_D18_A             ALIF_PINMUX(7, 2, 6)

#define PIN_P7_3__GPIO                  ALIF_PINMUX(7, 3, 0)
#define PIN_P7_3__OSPI0_SS1_C           ALIF_PINMUX(7, 3, 1)
#define PIN_P7_3__LPUART_RTS_B          ALIF_PINMUX(7, 3, 2)
#define PIN_P7_3__SPI2_SS0_B            ALIF_PINMUX(7, 3, 3)
#define PIN_P7_3__I2C1_SCL_C            ALIF_PINMUX(7, 3, 4)
#define PIN_P7_3__LPCAM_D3_B            ALIF_PINMUX(7, 3, 5)
#define PIN_P7_3__CDC_D19_A             ALIF_PINMUX(7, 3, 6)

#define PIN_P7_4__GPIO                  ALIF_PINMUX(7, 4, 0)
#define PIN_P7_4__UART3_CTS_B           ALIF_PINMUX(7, 4, 1)
#define PIN_P7_4__LPPDM_C2_C            ALIF_PINMUX(7, 4, 2)
#define PIN_P7_4__SPI2_SS1_B            ALIF_PINMUX(7, 4, 3)
#define PIN_P7_4__LPI2C0_SCL_C          ALIF_PINMUX(7, 4, 4)
#define PIN_P7_4__LPCAM_D4_B            ALIF_PINMUX(7, 4, 5)
#define PIN_P7_4__CDC_D20_A             ALIF_PINMUX(7, 4, 6)

#define PIN_P7_5__GPIO                  ALIF_PINMUX(7, 5, 0)
#define PIN_P7_5__UART3_RTS_B           ALIF_PINMUX(7, 5, 1)
#define PIN_P7_5__LPPDM_D2_C            ALIF_PINMUX(7, 5, 2)
#define PIN_P7_5__SPI2_SS2_B            ALIF_PINMUX(7, 5, 3)
#define PIN_P7_5__LPI2C0_SDA_C          ALIF_PINMUX(7, 5, 4)
#define PIN_P7_5__LPCAM_D5_B            ALIF_PINMUX(7, 5, 5)
#define PIN_P7_5__CDC_D21_A             ALIF_PINMUX(7, 5, 6)

#define PIN_P7_6__GPIO                  ALIF_PINMUX(7, 6, 0)
#define PIN_P7_6__SEUART_RX_C           ALIF_PINMUX(7, 6, 1)
#define PIN_P7_6__UART5_RX_B            ALIF_PINMUX(7, 6, 2)
#define PIN_P7_6__LPPDM_C3_C            ALIF_PINMUX(7, 6, 3)
#define PIN_P7_6__SPI0_MISO_C           ALIF_PINMUX(7, 6, 4)
#define PIN_P7_6__LPCAM_D6_B            ALIF_PINMUX(7, 6, 5)
#define PIN_P7_6__CDC_D22_A             ALIF_PINMUX(7, 6, 6)

#define PIN_P7_7__GPIO                  ALIF_PINMUX(7, 7, 0)
#define PIN_P7_7__SEUART_TX_C           ALIF_PINMUX(7, 7, 1)
#define PIN_P7_7__UART5_TX_B            ALIF_PINMUX(7, 7, 2)
#define PIN_P7_7__LPPDM_D3_C            ALIF_PINMUX(7, 7, 3)
#define PIN_P7_7__SPI0_MOSI_C           ALIF_PINMUX(7, 7, 4)
#define PIN_P7_7__LPCAM_D7_B            ALIF_PINMUX(7, 7, 5)
#define PIN_P7_7__CDC_D23_A             ALIF_PINMUX(7, 7, 6)

#define PIN_P8_0__GPIO                  ALIF_PINMUX(8, 0, 0)
#define PIN_P8_0__UART0_RX_C            ALIF_PINMUX(8, 0, 1)
#define PIN_P8_0__I2S0_SDI_C            ALIF_PINMUX(8, 0, 2)
#define PIN_P8_0__SPI0_SCLK_C           ALIF_PINMUX(8, 0, 3)
#define PIN_P8_0__UT0_T0_C              ALIF_PINMUX(8, 0, 4)
#define PIN_P8_0__SD_CMD_C              ALIF_PINMUX(8, 0, 5)
#define PIN_P8_0__I3C_SCL_C             ALIF_PINMUX(8, 0, 6)

#define PIN_P8_1__GPIO                  ALIF_PINMUX(8, 1, 0)
#define PIN_P8_1__UART0_TX_C            ALIF_PINMUX(8, 1, 1)
#define PIN_P8_1__I2S0_SDO_C            ALIF_PINMUX(8, 1, 2)
#define PIN_P8_1__SPI0_SS0_C            ALIF_PINMUX(8, 1, 3)
#define PIN_P8_1__UT0_T1_C              ALIF_PINMUX(8, 1, 4)
#define PIN_P8_1__SD_CLK_C              ALIF_PINMUX(8, 1, 5)
#define PIN_P8_1__I3C_SDA_C             ALIF_PINMUX(8, 1, 6)

#define PIN_P8_2__GPIO                  ALIF_PINMUX(8, 2, 0)
#define PIN_P8_2__SEUART_RX_B           ALIF_PINMUX(8, 2, 1)
#define PIN_P8_2__UART1_RX_C            ALIF_PINMUX(8, 2, 2)
#define PIN_P8_2__I2S0_SCLK_C           ALIF_PINMUX(8, 2, 3)
#define PIN_P8_2__SPI0_SS1_C            ALIF_PINMUX(8, 2, 4)
#define PIN_P8_2__UT1_T0_C              ALIF_PINMUX(8, 2, 5)
#define PIN_P8_2__SD_RST_C              ALIF_PINMUX(8, 2, 6)
#define PIN_P8_2__CAN0_RXD_C            ALIF_PINMUX(8, 2, 7)

#define PIN_P8_3__GPIO                  ALIF_PINMUX(8, 3, 0)
#define PIN_P8_3__SEUART_TX_B           ALIF_PINMUX(8, 3, 1)
#define PIN_P8_3__UART1_TX_C            ALIF_PINMUX(8, 3, 2)
#define PIN_P8_3__I2S0_WS_C             ALIF_PINMUX(8, 3, 3)
#define PIN_P8_3__SPI0_SS2_C            ALIF_PINMUX(8, 3, 4)
#define PIN_P8_3__UT1_T1_C              ALIF_PINMUX(8, 3, 5)
#define PIN_P8_3__CAN0_TXD_C            ALIF_PINMUX(8, 3, 6)
#define PIN_P8_3__EXT_RTS_B             ALIF_PINMUX(8, 3, 7)

#define PIN_P8_4__GPIO                  ALIF_PINMUX(8, 4, 0)
#define PIN_P8_4__UART2_RX_C            ALIF_PINMUX(8, 4, 1)
#define PIN_P8_4__I2S1_SDI_C            ALIF_PINMUX(8, 4, 2)
#define PIN_P8_4__SPI1_MISO_C           ALIF_PINMUX(8, 4, 3)
#define PIN_P8_4__UT2_T0_C              ALIF_PINMUX(8, 4, 4)
#define PIN_P8_4__LPCAM_VSYNC_C         ALIF_PINMUX(8, 4, 5)
#define PIN_P8_4__CAN0_STBY_C           ALIF_PINMUX(8, 4, 6)
#define PIN_P8_4__EXT_CTS_B             ALIF_PINMUX(8, 4, 7)

#define PIN_P8_5__GPIO                  ALIF_PINMUX(8, 5, 0)
#define PIN_P8_5__UART2_TX_C            ALIF_PINMUX(8, 5, 1)
#define PIN_P8_5__I2S1_SDO_C            ALIF_PINMUX(8, 5, 2)
#define PIN_P8_5__SPI1_MOSI_C           ALIF_PINMUX(8, 5, 3)
#define PIN_P8_5__UT2_T1_C              ALIF_PINMUX(8, 5, 4)
#define PIN_P8_5__LPCAM_HSYNC_C         ALIF_PINMUX(8, 5, 5)
#define PIN_P8_5__CAN1_RXD_B            ALIF_PINMUX(8, 5, 6)
#define PIN_P8_5__EXT_TRACE_B           ALIF_PINMUX(8, 5, 7)

#define PIN_P8_6__GPIO                  ALIF_PINMUX(8, 6, 0)
#define PIN_P8_6__UART3_RX_C            ALIF_PINMUX(8, 6, 1)
#define PIN_P8_6__I2S1_SCLK_SLV_C       ALIF_PINMUX(8, 6, 2)
#define PIN_P8_6__SPI1_SCLK_C           ALIF_PINMUX(8, 6, 3)
#define PIN_P8_6__UT3_T0_C              ALIF_PINMUX(8, 6, 4)
#define PIN_P8_6__LPCAM_PCLK_C          ALIF_PINMUX(8, 6, 5)
#define PIN_P8_6__CAN1_TXD_B            ALIF_PINMUX(8, 6, 6)
#define PIN_P8_6__EXT_RX_B              ALIF_PINMUX(8, 6, 7)

#define PIN_P8_7__GPIO                  ALIF_PINMUX(8, 7, 0)
#define PIN_P8_7__UART3_TX_C            ALIF_PINMUX(8, 7, 1)
#define PIN_P8_7__I2S1_WS_SLV_C         ALIF_PINMUX(8, 7, 2)
#define PIN_P8_7__SPI1_SS0_C            ALIF_PINMUX(8, 7, 3)
#define PIN_P8_7__UT3_T1_C              ALIF_PINMUX(8, 7, 4)
#define PIN_P8_7__LPCAM_XVCLK_C         ALIF_PINMUX(8, 7, 5)
#define PIN_P8_7__CAN1_STBY_B           ALIF_PINMUX(8, 7, 6)
#define PIN_P8_7__EXT_TX_B              ALIF_PINMUX(8, 7, 7)



#define PIN_P15_0__LPGPIO               ALIF_PINMUX(15, 0, 0)

#define PIN_P15_1__LPGPIO               ALIF_PINMUX(15, 1, 0)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ALIF_ENSEMBLE_E1C_PINCTRL_H_ */
```

## 23.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright Alif Semiconductor。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 753 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ALIF_ENSEMBLE_E1C_PINCTRL_H_`。

## 23.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/alif-ensemble-e1c-pinctrl_8h.html)

---

[上一章](P022_alif-ensemble-clocks.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P024_alif-ensemble-pinctrl.h_源码浏览.md)
