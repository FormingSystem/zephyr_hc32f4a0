---
id: learning.zephyr-docs.api-source-supplement-reference.page-180
title: siwx91x-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/siwx91x-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第180章\_siwx91x-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/siwx91x-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/siwx91x-pinctrl_8h.html)。

## 180.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00021"></a>
<a id="l00050"></a>
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
<a id="l00560"></a>
<a id="l00561"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="l00566"></a>
<a id="l00567"></a>
<a id="l00568"></a>
<a id="l00569"></a>
<a id="l00570"></a>
<a id="l00571"></a>
<a id="l00572"></a>
<a id="l00573"></a>
<a id="l00574"></a>
<a id="l00575"></a>
<a id="l00576"></a>
<a id="l00577"></a>
<a id="l00578"></a>
<a id="l00579"></a>
<a id="l00580"></a>
<a id="l00581"></a>
<a id="l00582"></a>
<a id="l00583"></a>
<a id="l00584"></a>
<a id="l00585"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="l00588"></a>
<a id="l00589"></a>
<a id="l00590"></a>
<a id="l00591"></a>
<a id="l00592"></a>
<a id="l00593"></a>
<a id="l00594"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="l00597"></a>
<a id="l00598"></a>
<a id="l00599"></a>
<a id="l00600"></a>
<a id="l00601"></a>
<a id="l00602"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00605"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="l00608"></a>
<a id="l00609"></a>
<a id="l00610"></a>
<a id="l00611"></a>
<a id="l00612"></a>
<a id="l00613"></a>
<a id="l00614"></a>
<a id="l00615"></a>
<a id="l00616"></a>
<a id="l00617"></a>
<a id="l00618"></a>
<a id="l00619"></a>
<a id="l00620"></a>
<a id="l00621"></a>
<a id="l00622"></a>
<a id="l00623"></a>
<a id="l00624"></a>
<a id="l00625"></a>
<a id="l00626"></a>
<a id="l00627"></a>
<a id="l00628"></a>
<a id="l00629"></a>
<a id="l00630"></a>
<a id="l00631"></a>
<a id="l00632"></a>
<a id="l00633"></a>
<a id="l00634"></a>
<a id="l00635"></a>
<a id="l00636"></a>
<a id="l00637"></a>
<a id="l00638"></a>
<a id="l00639"></a>
<a id="l00640"></a>
<a id="l00641"></a>
<a id="l00642"></a>
<a id="l00643"></a>
<a id="l00644"></a>
<a id="l00645"></a>
<a id="l00646"></a>
<a id="l00647"></a>
<a id="l00648"></a>
<a id="l00649"></a>
<a id="l00650"></a>
<a id="l00651"></a>
<a id="l00652"></a>
<a id="l00653"></a>
<a id="l00654"></a>
<a id="l00655"></a>
<a id="l00656"></a>
<a id="l00657"></a>
<a id="l00658"></a>
<a id="l00659"></a>
<a id="l00660"></a>
<a id="l00662"></a>
<a id="l00664"></a>
<a id="l00665"></a>
<a id="l00666"></a>
<a id="l00667"></a>
<a id="l00668"></a>
<a id="l00669"></a>
<a id="l00670"></a>
<a id="l00671"></a>
<a id="l00672"></a>
<a id="l00673"></a>
<a id="asilabs-pinctrl-siwx91x_8h_html"></a>

```c
/*
 * Copyright (c) 2024 Silicon Laboratories Inc.
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SILABS_SIWX91X_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SILABS_SIWX91X_PINCTRL_H_


#include <zephyr/dt-bindings/pinctrl/silabs-pinctrl-siwx91x.h>




#define AGPIO_ULP0           SIWX91X_GPIO(0xFF, 7, 0xFF, 4, 0,  0)
#define AGPIO_ULP1           SIWX91X_GPIO(0xFF, 7, 0xFF, 4, 0,  1)
#define AGPIO_ULP2           SIWX91X_GPIO(0xFF, 7, 0xFF, 4, 0,  2)
#define AGPIO_ULP4           SIWX91X_GPIO(0xFF, 7, 0xFF, 4, 0,  4)
#define AGPIO_ULP5           SIWX91X_GPIO(0xFF, 7, 0xFF, 4, 0,  5)
#define AGPIO_ULP6           SIWX91X_GPIO(0xFF, 7, 0xFF, 4, 0,  6)
#define AGPIO_ULP7           SIWX91X_GPIO(0xFF, 7, 0xFF, 4, 0,  7)
#define AGPIO_ULP8           SIWX91X_GPIO(0xFF, 7, 0xFF, 4, 0,  8)
#define AGPIO_ULP9           SIWX91X_GPIO(0xFF, 7, 0xFF, 4, 0,  9)
#define AGPIO_ULP10          SIWX91X_GPIO(0xFF, 7, 0xFF, 4, 0, 10)
#define AGPIO_ULP11          SIWX91X_GPIO(0xFF, 7, 0xFF, 4, 0, 11)

#define ADC_TOPGPIO_HP25     SIWX91X_GPIO(14, 0xFF, 0, 1, 9, 0)
#define ADC_TOPGPIO_HP26     SIWX91X_GPIO(14, 0xFF, 0, 1, 10, 0)
#define ADC_TOPGPIO_HP27     SIWX91X_GPIO(14, 0xFF, 0, 1, 11, 0)
#define ADC_TOPGPIO_HP28     SIWX91X_GPIO(14, 0xFF, 0, 1, 12, 0)
#define ADC_TOPGPIO_HP29     SIWX91X_GPIO(14, 0xFF, 0, 1, 13, 0)
#define ADC_TOPGPIO_HP30     SIWX91X_GPIO(14, 0xFF, 0, 1, 14, 0)

#define AUXULP_TRIG0_HP11    SIWX91X_GPIO(9,     5,    6, 0, 11,  5)
#define AUXULP_TRIG0_HP30    SIWX91X_GPIO(11,    5,    0, 1, 14, 11)
#define AUXULP_TRIG0_HP49    SIWX91X_GPIO(9,     5,   13, 3,  1, 11)
#define AUXULP_TRIG0_ULP5    SIWX91X_GPIO(0xFF,  5, 0xFF, 4,  0,  5)
#define AUXULP_TRIG0_ULP6    SIWX91X_GPIO(0xFF, 10, 0xFF, 4,  0,  6)
#define AUXULP_TRIG0_ULP11   SIWX91X_GPIO(0xFF,  5, 0xFF, 4,  0, 11)
#define AUXULP_TRIG1_ULP4    SIWX91X_GPIO(0xFF,  5, 0xFF, 4,  0,  4)
#define AUXULP_TRIG1_ULP7    SIWX91X_GPIO(0xFF, 10, 0xFF, 4,  0,  7)

#define CLK_I2SPLL_HP27      SIWX91X_GPIO(12, 0xFF,  0, 1, 11, 0)
#define CLK_I2SPLL_HP48      SIWX91X_GPIO(10, 0xFF, 12, 3,  0, 0)
#define CLK_I2SPLL_HP54      SIWX91X_GPIO(10, 0xFF, 18, 3,  6, 0)
#define CLK_INTFPLL_HP26     SIWX91X_GPIO(12, 0xFF,  0, 1, 10, 0)
#define CLK_INTFPLL_HP47     SIWX91X_GPIO(10, 0xFF, 11, 2, 15, 0)
#define CLK_INTFPLL_HP53     SIWX91X_GPIO(10, 0xFF, 17, 3,  5, 0)
#define CLK_MCUOUT_HP11      SIWX91X_GPIO(12, 0xFF,  6, 0, 11, 0)
#define CLK_MEMSREF_HP50     SIWX91X_GPIO(10, 0xFF, 14, 3,  2, 0)
#define CLK_MEMSREF_HP56     SIWX91X_GPIO(10, 0xFF, 20, 3,  8, 0)
#define CLK_OUT_HP12         SIWX91X_GPIO(8,  0xFF,  7, 0, 12, 0)
#define CLK_OUT_HP15         SIWX91X_GPIO(8,  0xFF,  8, 0, 15, 0)
#define CLK_PLLTESTMODE_HP51 SIWX91X_GPIO(10, 0xFF, 15, 3,  3, 0)
#define CLK_SOCPLL_HP25      SIWX91X_GPIO(12, 0xFF,  0, 1,  9, 0)
#define CLK_SOCPLL_HP46      SIWX91X_GPIO(10, 0xFF, 10, 2, 14, 0)
#define CLK_SOCPLL_HP52      SIWX91X_GPIO(10, 0xFF, 16, 3,  4, 0)
#define CLK_XTALONIN_HP28    SIWX91X_GPIO(12, 0xFF,  0, 1, 12, 0)
#define CLK_XTALONIN_HP57    SIWX91X_GPIO(10, 0xFF, 21, 3,  9, 0)

#define COMP1_OUT_HP8        SIWX91X_GPIO(9,    5,    3, 0,  8, 2)
#define COMP1_OUT_HP28       SIWX91X_GPIO(11,   5,    0, 1, 12, 9)
#define COMP1_OUT_HP47       SIWX91X_GPIO(9,    5,   11, 2, 15, 9)
#define COMP1_OUT_ULP2       SIWX91X_GPIO(0xFF, 5, 0xFF, 4,  0, 2)
#define COMP1_OUT_ULP6       SIWX91X_GPIO(0xFF, 9, 0xFF, 4,  0, 6)
#define COMP2_OUT_ULP7       SIWX91X_GPIO(0xFF, 9, 0xFF, 4,  0, 7)

#define GSPI_CLK_HP8         SIWX91X_GPIO(4,  0xFF,  3, 0,  8, 0)
#define GSPI_CLK_HP25        SIWX91X_GPIO(4,  0xFF,  0, 1,  9, 0)
#define GSPI_CLK_HP46        SIWX91X_GPIO(4,  0xFF, 10, 2, 14, 0)
#define GSPI_CLK_HP52        SIWX91X_GPIO(4,  0xFF, 16, 3,  4, 0)
#define GSPI_CS0_HP9         SIWX91X_GPIO(4,  0xFF,  4, 0,  9, 0)
#define GSPI_CS0_HP28        SIWX91X_GPIO(4,  0xFF,  0, 1, 12, 0)
#define GSPI_CS0_HP49        SIWX91X_GPIO(4,  0xFF, 13, 3,  1, 0)
#define GSPI_CS0_HP53        SIWX91X_GPIO(4,  0xFF, 17, 3,  5, 0)
#define GSPI_CS1_HP10        SIWX91X_GPIO(4,  0xFF,  5, 0, 10, 0)
#define GSPI_CS1_HP29        SIWX91X_GPIO(4,  0xFF,  0, 1, 13, 0)
#define GSPI_CS1_HP50        SIWX91X_GPIO(4,  0xFF, 14, 3,  2, 0)
#define GSPI_CS1_HP54        SIWX91X_GPIO(4,  0xFF, 18, 3,  6, 0)
#define GSPI_CS2_HP15        SIWX91X_GPIO(4,  0xFF,  8, 0, 15, 0)
#define GSPI_CS2_HP30        SIWX91X_GPIO(4,  0xFF,  0, 1, 14, 0)
#define GSPI_CS2_HP51        SIWX91X_GPIO(4,  0xFF, 15, 3,  3, 0)
#define GSPI_CS2_HP55        SIWX91X_GPIO(4,  0xFF, 19, 3,  7, 0)
#define GSPI_MISO_HP11       SIWX91X_GPIO(4,  0xFF,  6, 0, 11, 0)
#define GSPI_MISO_HP26       SIWX91X_GPIO(4,  0xFF,  0, 1, 10, 0)
#define GSPI_MISO_HP47       SIWX91X_GPIO(4,  0xFF, 11, 2, 15, 0)
#define GSPI_MISO_HP56       SIWX91X_GPIO(4,  0xFF, 20, 3,  8, 0)
#define GSPI_MOSI_HP6        SIWX91X_GPIO(12, 0xFF,  1, 0,  6, 0)
#define GSPI_MOSI_HP12       SIWX91X_GPIO(4,  0xFF,  7, 0, 12, 0)
#define GSPI_MOSI_HP27       SIWX91X_GPIO(4,  0xFF,  0, 1, 11, 0)
#define GSPI_MOSI_HP48       SIWX91X_GPIO(4,  0xFF, 12, 3,  0, 0)
#define GSPI_MOSI_HP57       SIWX91X_GPIO(4,  0xFF, 21, 3,  9, 0)

#define I2C0_SCL_HP7         SIWX91X_GPIO(4,  0xFF,  2, 0,  7,  0)
#define I2C0_SCL_HP32        SIWX91X_GPIO(11, 0xFF,  9, 2,  0,  0)
#define I2C0_SCL_ULP1        SIWX91X_GPIO(4,     6, 23, 4,  1,  1)
#define I2C0_SCL_ULP2        SIWX91X_GPIO(4,     6, 24, 4,  2,  2)
#define I2C0_SCL_ULP11       SIWX91X_GPIO(4,     6, 33, 4, 11, 11)
#define I2C0_SDA_HP6         SIWX91X_GPIO(4,  0xFF,  1, 0,  6,  0)
#define I2C0_SDA_HP31        SIWX91X_GPIO(11, 0xFF,  9, 1, 15,  0)
#define I2C0_SDA_ULP0        SIWX91X_GPIO(4,     6, 22, 4,  0,  0)
#define I2C0_SDA_ULP3        SIWX91X_GPIO(4,     6, 25, 4,  3,  3)
#define I2C0_SDA_ULP10       SIWX91X_GPIO(4,     6, 32, 4, 10, 10)

#define I2C1_SCL_HP6         SIWX91X_GPIO(5,  0xFF,  1, 0,  6, 0)
#define I2C1_SCL_HP29        SIWX91X_GPIO(5,  0xFF,  0, 1, 13, 0)
#define I2C1_SCL_HP33        SIWX91X_GPIO(11, 0xFF,  9, 2,  1, 0)
#define I2C1_SCL_HP50        SIWX91X_GPIO(5,  0xFF, 14, 3,  2, 0)
#define I2C1_SCL_HP54        SIWX91X_GPIO(5,  0xFF, 18, 3,  6, 0)
#define I2C1_SCL_ULP0        SIWX91X_GPIO(5,     6, 22, 4,  0, 0)
#define I2C1_SCL_ULP2        SIWX91X_GPIO(5,     6, 24, 4,  2, 2)
#define I2C1_SCL_ULP6        SIWX91X_GPIO(5,     6, 28, 4,  6, 6)
#define I2C1_SDA_HP7         SIWX91X_GPIO(5,  0xFF,  2, 0,  7, 0)
#define I2C1_SDA_HP30        SIWX91X_GPIO(5,  0xFF,  0, 1, 14, 0)
#define I2C1_SDA_HP34        SIWX91X_GPIO(11, 0xFF,  9, 2,  2, 0)
#define I2C1_SDA_HP51        SIWX91X_GPIO(5,  0xFF, 15, 3,  3, 0)
#define I2C1_SDA_HP55        SIWX91X_GPIO(5,  0xFF, 19, 3,  7, 0)
#define I2C1_SDA_ULP1        SIWX91X_GPIO(5,     6, 23, 4,  1, 1)
#define I2C1_SDA_ULP3        SIWX91X_GPIO(5,     6, 25, 4,  3, 3)
#define I2C1_SDA_ULP7        SIWX91X_GPIO(5,     6, 29, 4,  7, 7)

#define I2S0_CLK_HP8         SIWX91X_GPIO(7, 0xFF,  3, 0,  8, 0)
#define I2S0_CLK_HP25        SIWX91X_GPIO(7, 0xFF,  0, 1,  9, 0)
#define I2S0_CLK_HP46        SIWX91X_GPIO(7, 0xFF, 10, 2, 14, 0)
#define I2S0_CLK_HP52        SIWX91X_GPIO(7, 0xFF, 16, 3,  4, 0)
#define I2S0_DIN0_HP10       SIWX91X_GPIO(7, 0xFF,  5, 0, 10, 0)
#define I2S0_DIN0_HP27       SIWX91X_GPIO(7, 0xFF,  0, 1, 11, 0)
#define I2S0_DIN0_HP48       SIWX91X_GPIO(7, 0xFF, 12, 3,  0, 0)
#define I2S0_DIN0_HP56       SIWX91X_GPIO(7, 0xFF, 20, 3,  8, 0)
#define I2S0_DIN1_HP6        SIWX91X_GPIO(7, 0xFF,  1, 0,  6, 0)
#define I2S0_DIN1_HP29       SIWX91X_GPIO(7, 0xFF,  0, 1, 13, 0)
#define I2S0_DIN1_HP50       SIWX91X_GPIO(7, 0xFF, 14, 3,  2, 0)
#define I2S0_DIN1_HP54       SIWX91X_GPIO(7, 0xFF, 18, 3,  6, 0)
#define I2S0_DOUT0_HP11      SIWX91X_GPIO(7, 0xFF,  6, 0, 11, 0)
#define I2S0_DOUT0_HP28      SIWX91X_GPIO(7, 0xFF,  0, 1, 12, 0)
#define I2S0_DOUT0_HP49      SIWX91X_GPIO(7, 0xFF, 13, 3,  1, 0)
#define I2S0_DOUT0_HP57      SIWX91X_GPIO(7, 0xFF, 21, 3,  9, 0)
#define I2S0_DOUT1_HP7       SIWX91X_GPIO(7, 0xFF,  2, 0,  7, 0)
#define I2S0_DOUT1_HP29      SIWX91X_GPIO(7, 0xFF,  0, 1, 14, 0)
#define I2S0_DOUT1_HP51      SIWX91X_GPIO(7, 0xFF, 15, 3,  3, 0)
#define I2S0_DOUT1_HP55      SIWX91X_GPIO(7, 0xFF, 19, 3,  7, 0)
#define I2S0_WS_HP9          SIWX91X_GPIO(7, 0xFF,  4, 0,  9, 0)
#define I2S0_WS_HP26         SIWX91X_GPIO(7, 0xFF,  0, 1, 10, 0)
#define I2S0_WS_HP47         SIWX91X_GPIO(7, 0xFF, 11, 2, 15, 0)
#define I2S0_WS_HP53         SIWX91X_GPIO(7, 0xFF, 17, 3,  5, 0)

#define IR_INPUT_HP15        SIWX91X_GPIO(9,     1,    8, 0, 15,  7)
#define IR_INPUT_HP26        SIWX91X_GPIO(11,    1,    0, 1, 10,  7)
#define IR_INPUT_HP29        SIWX91X_GPIO(11,    4,    0, 1, 13, 10)
#define IR_INPUT_HP48        SIWX91X_GPIO(9,     4,   12, 3,  0, 10)
#define IR_INPUT_ULP4        SIWX91X_GPIO(0xFF, 10, 0xFF, 4,  0,  4)
#define IR_INPUT_ULP7        SIWX91X_GPIO(0xFF,  1, 0xFF, 4,  0,  7)
#define IR_INPUT_ULP10       SIWX91X_GPIO(0xFF,  4, 0xFF, 4,  0, 10)
#define IR_OUTPUT_HP11       SIWX91X_GPIO(9,     1,    6, 0, 11,  5)
#define IR_OUTPUT_ULP5       SIWX91X_GPIO(0xFF,  1, 0xFF, 4,  0,  5)

#define PMU_TEST1_HP6        SIWX91X_GPIO(8,  0xFF,  1, 0,  6,  0)
#define PMU_TEST1_HP29       SIWX91X_GPIO(8,  0xFF,  0, 1, 13,  0)
#define PMU_TEST1_HP30       SIWX91X_GPIO(12, 0xFF,  0, 1, 14,  0)
#define PMU_TEST1_ULP0       SIWX91X_GPIO(13,    6, 22, 4,  0,  0)
#define PMU_TEST1_ULP2       SIWX91X_GPIO(10,    6, 24, 4,  2,  2)
#define PMU_TEST1_ULP6       SIWX91X_GPIO(12,    6, 28, 4,  6,  6)
#define PMU_TEST1_ULP10      SIWX91X_GPIO(10,    6, 32, 4, 10, 10)
#define PMU_TEST2_HP7        SIWX91X_GPIO(8,  0xFF,  2, 0,  7,  0)
#define PMU_TEST2_HP30       SIWX91X_GPIO(8,  0xFF,  0, 1, 14,  0)
#define PMU_TEST2_ULP1       SIWX91X_GPIO(13,    6, 23, 4,  1,  1)
#define PMU_TEST2_ULP3       SIWX91X_GPIO(10,    6, 25, 4,  3,  3)
#define PMU_TEST2_ULP7       SIWX91X_GPIO(12,    6, 29, 4,  7,  7)
#define PMU_TEST2_ULP11      SIWX91X_GPIO(10,    6, 33, 4, 11, 11)

#define PSRAM_CLK_HP46       SIWX91X_GPIO(11, 0xFF, 10, 2, 14, 0)
#define PSRAM_CLK_HP52       SIWX91X_GPIO(12, 0xFF, 16, 3,  4, 0)
#define PSRAM_CSN0_HP49      SIWX91X_GPIO(11, 0xFF, 13, 3,  1, 0)
#define PSRAM_CSN0_HP55      SIWX91X_GPIO(12, 0xFF, 19, 3,  7, 0)
#define PSRAM_CSN1_HP53      SIWX91X_GPIO(11, 0xFF, 17, 3,  5, 0)
#define PSRAM_D0_HP47        SIWX91X_GPIO(11, 0xFF, 11, 2, 15, 0)
#define PSRAM_D0_HP53        SIWX91X_GPIO(12, 0xFF, 17, 3,  5, 0)
#define PSRAM_D1_HP48        SIWX91X_GPIO(11, 0xFF, 12, 3,  0, 0)
#define PSRAM_D1_HP54        SIWX91X_GPIO(12, 0xFF, 18, 3,  6, 0)
#define PSRAM_D2_HP50        SIWX91X_GPIO(11, 0xFF, 14, 3,  2, 0)
#define PSRAM_D2_HP56        SIWX91X_GPIO(12, 0xFF, 20, 3,  8, 0)
#define PSRAM_D3_HP51        SIWX91X_GPIO(11, 0xFF, 15, 3,  3, 0)
#define PSRAM_D3_HP57        SIWX91X_GPIO(12, 0xFF, 21, 3,  9, 0)
#define PSRAM_D4_HP54        SIWX91X_GPIO(11, 0xFF, 18, 3,  6, 0)
#define PSRAM_D5_HP55        SIWX91X_GPIO(11, 0xFF, 19, 3,  7, 0)
#define PSRAM_D6_HP56        SIWX91X_GPIO(11, 0xFF, 20, 3,  8, 0)
#define PSRAM_D7_HP57        SIWX91X_GPIO(11, 0xFF, 21, 3,  9, 0)

#define PWM_0H_HP7           SIWX91X_GPIO(10, 0xFF,  2, 0,  7,  0)
#define PWM_0H_ULP1          SIWX91X_GPIO(12,    6, 23, 4,  1,  1)
#define PWM_0L_HP6           SIWX91X_GPIO(10, 0xFF,  1, 0,  6,  0)
#define PWM_0L_ULP0          SIWX91X_GPIO(12,    6, 22, 4,  0,  0)
#define PWM_1H_HP9           SIWX91X_GPIO(10, 0xFF,  4, 0,  9,  0)
#define PWM_1H_ULP3          SIWX91X_GPIO(8,     6, 25, 4,  3,  3)
#define PWM_1H_ULP5          SIWX91X_GPIO(12,    6, 27, 4,  5,  5)
#define PWM_1L_HP8           SIWX91X_GPIO(10, 0xFF,  3, 0,  8,  0)
#define PWM_1L_ULP2          SIWX91X_GPIO(8,     6, 24, 4,  2,  2)
#define PWM_1L_ULP4          SIWX91X_GPIO(12,    6, 26, 4,  4,  4)
#define PWM_2H_HP11          SIWX91X_GPIO(10, 0xFF,  6, 0, 11,  0)
#define PWM_2H_ULP5          SIWX91X_GPIO(8,     6, 27, 4,  5,  5)
#define PWM_2L_HP10          SIWX91X_GPIO(10, 0xFF,  5, 0, 10,  0)
#define PWM_2L_ULP4          SIWX91X_GPIO(8,     6, 26, 4,  4,  4)
#define PWM_3H_HP15          SIWX91X_GPIO(10, 0xFF,  8, 0, 15,  0)
#define PWM_3H_ULP7          SIWX91X_GPIO(8,     6, 29, 4,  7,  7)
#define PWM_3L_HP12          SIWX91X_GPIO(10, 0xFF,  7, 0, 12,  0)
#define PWM_3L_ULP6          SIWX91X_GPIO(8,     6, 28, 4,  6,  6)
#define PWM_EXTTRIG0_HP27    SIWX91X_GPIO(10, 0xFF,  0, 1, 11,  0)
#define PWM_EXTTRIG0_HP51    SIWX91X_GPIO(8,  0xFF, 15, 3,  3,  0)
#define PWM_EXTTRIG0_ULP6    SIWX91X_GPIO(10,    6, 28, 4,  6,  6)
#define PWM_EXTTRIG0_ULP11   SIWX91X_GPIO(8,     6, 33, 4, 11, 11)
#define PWM_EXTTRIG1_HP28    SIWX91X_GPIO(10, 0xFF,  0, 1, 12,  0)
#define PWM_EXTTRIG1_HP54    SIWX91X_GPIO(8,  0xFF, 18, 3,  6,  0)
#define PWM_EXTTRIG1_ULP7    SIWX91X_GPIO(10,    6, 29, 4,  7,  7)
#define PWM_EXTTRIG2_HP29    SIWX91X_GPIO(10, 0xFF,  0, 1, 13,  0)
#define PWM_EXTTRIG2_HP55    SIWX91X_GPIO(8,  0xFF, 19, 3,  7,  0)
#define PWM_EXTTRIG2_ULP8    SIWX91X_GPIO(10,    6, 30, 4,  8,  8)
#define PWM_EXTTRIG3_HP30    SIWX91X_GPIO(10, 0xFF,  0, 1, 14,  0)
#define PWM_EXTTRIG3_HP50    SIWX91X_GPIO(8,  0xFF, 14, 3,  2,  0)
#define PWM_EXTTRIG3_ULP9    SIWX91X_GPIO(10,    6, 31, 4,  9,  9)
#define PWM_FAULTA_HP25      SIWX91X_GPIO(10, 0xFF,  0, 1,  9,  0)
#define PWM_FAULTA_ULP4      SIWX91X_GPIO(10,    6, 26, 4,  4,  4)
#define PWM_FAULTA_ULP9      SIWX91X_GPIO(8,     6, 31, 4,  9,  9)
#define PWM_FAULTB_HP26      SIWX91X_GPIO(10, 0xFF,  0, 1, 10,  0)
#define PWM_FAULTB_ULP5      SIWX91X_GPIO(10,    6, 27, 4,  5,  5)
#define PWM_FAULTB_ULP10     SIWX91X_GPIO(8,     6, 32, 4, 10, 10)
#define PWM_SLEEPEVENT_ULP8  SIWX91X_GPIO(8,     6, 30, 4,  8,  8)

#define QEI_DIR_HP11         SIWX91X_GPIO(5,  0xFF,  6, 0, 11,  0)
#define QEI_DIR_HP28         SIWX91X_GPIO(5,  0xFF,  0, 1, 12,  0)
#define QEI_DIR_HP34         SIWX91X_GPIO(13, 0xFF,  9, 2,  2,  0)
#define QEI_DIR_HP49         SIWX91X_GPIO(3,  0xFF, 13, 3,  1,  0)
#define QEI_DIR_HP57         SIWX91X_GPIO(5,  0xFF, 21, 3,  9,  0)
#define QEI_DIR_ULP3         SIWX91X_GPIO(3,     6, 25, 4,  3,  3)
#define QEI_DIR_ULP7         SIWX91X_GPIO(3,     6, 29, 4,  7,  7)
#define QEI_DIR_ULP11        SIWX91X_GPIO(3,     6, 33, 4, 11, 11)
#define QEI_IDX_HP8          SIWX91X_GPIO(5,  0xFF,  3, 0,  8,  0)
#define QEI_IDX_HP31         SIWX91X_GPIO(13, 0xFF,  9, 1, 15,  0)
#define QEI_IDX_HP25         SIWX91X_GPIO(5,  0xFF,  0, 1,  9,  0)
#define QEI_IDX_HP46         SIWX91X_GPIO(3,  0xFF, 10, 2, 14,  0)
#define QEI_IDX_HP52         SIWX91X_GPIO(5,  0xFF, 16, 3,  4,  0)
#define QEI_IDX_ULP0         SIWX91X_GPIO(3,     6, 22, 4,  0,  0)
#define QEI_IDX_ULP4         SIWX91X_GPIO(3,     6, 26, 4,  4,  4)
#define QEI_IDX_ULP8         SIWX91X_GPIO(3,     6, 30, 4,  8,  8)
#define QEI_PHA_HP9          SIWX91X_GPIO(5,  0xFF,  4, 0,  9,  0)
#define QEI_PHA_HP26         SIWX91X_GPIO(5,  0xFF,  0, 1, 10,  0)
#define QEI_PHA_HP32         SIWX91X_GPIO(13, 0xFF,  9, 2,  0,  0)
#define QEI_PHA_HP47         SIWX91X_GPIO(3,  0xFF, 11, 2, 15,  0)
#define QEI_PHA_HP53         SIWX91X_GPIO(5,  0xFF, 17, 3,  5,  0)
#define QEI_PHA_ULP1         SIWX91X_GPIO(3,     6, 23, 4,  1,  1)
#define QEI_PHA_ULP5         SIWX91X_GPIO(3,     6, 27, 4,  5,  5)
#define QEI_PHA_ULP9         SIWX91X_GPIO(3,     6, 31, 4,  9,  9)
#define QEI_PHB_HP10         SIWX91X_GPIO(5,  0xFF,  5, 0, 10,  0)
#define QEI_PHB_HP27         SIWX91X_GPIO(5,  0xFF,  0, 1, 11,  0)
#define QEI_PHB_HP33         SIWX91X_GPIO(13, 0xFF,  9, 2,  1,  0)
#define QEI_PHB_HP48         SIWX91X_GPIO(3,  0xFF, 12, 3,  0,  0)
#define QEI_PHB_HP56         SIWX91X_GPIO(5,  0xFF, 20, 3,  8,  0)
#define QEI_PHB_ULP2         SIWX91X_GPIO(3,     6, 24, 4,  2,  2)
#define QEI_PHB_ULP6         SIWX91X_GPIO(3,     6, 28, 4,  6,  6)
#define QEI_PHB_ULP10        SIWX91X_GPIO(3,     6, 32, 4, 10, 10)

#define QSPI_CLK_HP8         SIWX91X_GPIO(11, 0xFF,  3, 0,  8, 0)
#define QSPI_CLK_HP46        SIWX91X_GPIO(1,  0xFF, 10, 2, 14, 0)
#define QSPI_CLK_HP52        SIWX91X_GPIO(9,  0xFF, 16, 3,  4, 0)
#define QSPI_CSN0_HP7        SIWX91X_GPIO(11, 0xFF,  2, 0,  7, 0)
#define QSPI_CSN0_HP49       SIWX91X_GPIO(1,  0xFF, 13, 3,  1, 0)
#define QSPI_CSN0_HP55       SIWX91X_GPIO(9,  0xFF, 19, 3,  7, 0)
#define QSPI_CSN1_HP7        SIWX91X_GPIO(12, 0xFF,  2, 0,  7, 0)
#define QSPI_CSN1_HP53       SIWX91X_GPIO(1,  0xFF, 17, 3,  5, 0)
#define QSPI_CSN9_HP49       SIWX91X_GPIO(10, 0xFF, 13, 3,  1, 0)
#define QSPI_D0_HP6          SIWX91X_GPIO(11, 0xFF,  1, 0,  6, 0)
#define QSPI_D0_HP47         SIWX91X_GPIO(1,  0xFF, 11, 2, 15, 0)
#define QSPI_D0_HP53         SIWX91X_GPIO(9,  0xFF, 17, 3,  5, 0)
#define QSPI_D1_HP9          SIWX91X_GPIO(11, 0xFF,  4, 0,  9, 0)
#define QSPI_D1_HP48         SIWX91X_GPIO(1,  0xFF, 12, 3,  0, 0)
#define QSPI_D1_HP54         SIWX91X_GPIO(9,  0xFF, 18, 3,  6, 0)
#define QSPI_D2_HP10         SIWX91X_GPIO(11, 0xFF,  5, 0, 10, 0)
#define QSPI_D2_HP50         SIWX91X_GPIO(1,  0xFF, 14, 3,  2, 0)
#define QSPI_D2_HP56         SIWX91X_GPIO(9,  0xFF, 20, 3,  8, 0)
#define QSPI_D3_HP11         SIWX91X_GPIO(11, 0xFF,  6, 0, 11, 0)
#define QSPI_D3_HP51         SIWX91X_GPIO(1,  0xFF, 15, 3,  3, 0)
#define QSPI_D3_HP57         SIWX91X_GPIO(9,  0xFF, 21, 3,  9, 0)
#define QSPI_D4_HP54         SIWX91X_GPIO(1,  0xFF, 18, 3,  6, 0)
#define QSPI_D5_HP55         SIWX91X_GPIO(1,  0xFF, 19, 3,  7, 0)
#define QSPI_D6_HP56         SIWX91X_GPIO(1,  0xFF, 20, 3,  8, 0)
#define QSPI_D7_HP57         SIWX91X_GPIO(1,  0xFF, 21, 3,  9, 0)

#define SCT_IN0_HP25         SIWX91X_GPIO(9,  0xFF,  0, 1,  9,  0)
#define SCT_IN0_ULP0         SIWX91X_GPIO(7,     6, 22, 4,  0,  0)
#define SCT_IN0_ULP4         SIWX91X_GPIO(9,     6, 26, 4,  4,  4)
#define SCT_IN1_HP26         SIWX91X_GPIO(9,  0xFF,  0, 1, 10,  0)
#define SCT_IN1_ULP1         SIWX91X_GPIO(7,     6, 23, 4,  1,  1)
#define SCT_IN1_ULP5         SIWX91X_GPIO(9,     6, 27, 4,  5,  5)
#define SCT_IN2_HP27         SIWX91X_GPIO(9,  0xFF,  0, 1, 11,  0)
#define SCT_IN2_ULP2         SIWX91X_GPIO(7,     6, 24, 4,  2,  2)
#define SCT_IN2_ULP6         SIWX91X_GPIO(9,     6, 28, 4,  6,  6)
#define SCT_IN3_HP28         SIWX91X_GPIO(9,  0xFF,  0, 1, 12,  0)
#define SCT_IN3_ULP3         SIWX91X_GPIO(7,     6, 25, 4,  3,  3)
#define SCT_IN3_ULP7         SIWX91X_GPIO(9,     6, 29, 4,  7,  7)
#define SCT_OUT0_HP29        SIWX91X_GPIO(9,  0xFF,  0, 1, 13,  0)
#define SCT_OUT0_ULP4        SIWX91X_GPIO(7,     6, 26, 4,  4,  4)
#define SCT_OUT1_HP30        SIWX91X_GPIO(9,  0xFF,  0, 1, 14,  0)
#define SCT_OUT1_ULP5        SIWX91X_GPIO(7,     6, 27, 4,  5,  5)
#define SCT_OUT2_HP8         SIWX91X_GPIO(12, 0xFF,  3, 0,  8,  0)
#define SCT_OUT2_ULP6        SIWX91X_GPIO(7,     6, 28, 4,  6,  6)
#define SCT_OUT3_HP9         SIWX91X_GPIO(12, 0xFF,  4, 0,  9,  0)
#define SCT_OUT3_ULP7        SIWX91X_GPIO(7,     6, 29, 4,  7,  7)
#define SCT_OUT4_ULP4        SIWX91X_GPIO(13,    6, 26, 4,  4,  4)
#define SCT_OUT4_ULP8        SIWX91X_GPIO(7,     6, 30, 4,  8,  8)
#define SCT_OUT5_ULP5        SIWX91X_GPIO(13,    6, 27, 4,  5,  5)
#define SCT_OUT5_ULP9        SIWX91X_GPIO(7,     6, 31, 4,  9,  9)
#define SCT_OUT6_ULP6        SIWX91X_GPIO(13,    6, 28, 4,  6,  6)
#define SCT_OUT6_ULP10       SIWX91X_GPIO(7,     6, 32, 4, 10, 10)
#define SCT_OUT7_ULP7        SIWX91X_GPIO(13,    6, 29, 4,  7,  7)
#define SCT_OUT7_ULP11       SIWX91X_GPIO(7,     6, 33, 4, 11, 11)

#define SIO_0_HP6            SIWX91X_GPIO(1, 0xFF,  1, 0,  6,  0)
#define SIO_0_HP25           SIWX91X_GPIO(1, 0xFF,  0, 1,  9,  0)
#define SIO_0_ULP0           SIWX91X_GPIO(1,    6, 22, 4,  0,  0)
#define SIO_0_ULP8           SIWX91X_GPIO(1,    6, 30, 4,  8,  8)
#define SIO_1_HP7            SIWX91X_GPIO(1, 0xFF,  2, 0,  7,  0)
#define SIO_1_HP26           SIWX91X_GPIO(1, 0xFF,  0, 1, 10,  0)
#define SIO_1_ULP1           SIWX91X_GPIO(1,    6, 23, 4,  1,  1)
#define SIO_1_ULP9           SIWX91X_GPIO(1,    6, 31, 4,  9,  9)
#define SIO_2_HP8            SIWX91X_GPIO(1, 0xFF,  3, 0,  8,  0)
#define SIO_2_HP27           SIWX91X_GPIO(1, 0xFF,  0, 1, 11,  0)
#define SIO_2_ULP2           SIWX91X_GPIO(1,    6, 24, 4,  2,  2)
#define SIO_2_ULP10          SIWX91X_GPIO(1,    6, 32, 4, 10, 10)
#define SIO_3_HP9            SIWX91X_GPIO(1, 0xFF,  4, 0,  9,  0)
#define SIO_3_HP28           SIWX91X_GPIO(1, 0xFF,  0, 1, 12,  0)
#define SIO_3_ULP3           SIWX91X_GPIO(1,    6, 25, 4,  3,  3)
#define SIO_3_ULP11          SIWX91X_GPIO(1,    6, 33, 4, 11, 11)
#define SIO_4_HP10           SIWX91X_GPIO(1, 0xFF,  5, 0, 10,  0)
#define SIO_4_HP29           SIWX91X_GPIO(1, 0xFF,  0, 1, 13,  0)
#define SIO_4_ULP4           SIWX91X_GPIO(1,    6, 26, 4,  4,  4)
#define SIO_5_HP11           SIWX91X_GPIO(1, 0xFF,  6, 0, 11,  0)
#define SIO_5_HP30           SIWX91X_GPIO(1, 0xFF,  0, 1, 14,  0)
#define SIO_5_ULP5           SIWX91X_GPIO(1,    6, 27, 4,  5,  5)
#define SIO_6_ULP6           SIWX91X_GPIO(1,    6, 28, 4,  6,  6)
#define SIO_7_HP15           SIWX91X_GPIO(1, 0xFF,  8, 0, 15,  0)
#define SIO_7_ULP7           SIWX91X_GPIO(1,    6, 29, 4,  7,  7)

#define SSI_CLK_HP8          SIWX91X_GPIO(3,  0xFF,  3, 0,  8, 0)
#define SSI_CLK_HP25         SIWX91X_GPIO(3,  0xFF,  0, 1,  9, 0)
#define SSI_CLK_HP52         SIWX91X_GPIO(3,  0xFF, 16, 3,  4, 0)
#define SSI_CS0_HP9          SIWX91X_GPIO(3,  0xFF,  4, 0,  9, 0)
#define SSI_CS0_HP28         SIWX91X_GPIO(3,  0xFF,  0, 1, 12, 0)
#define SSI_CS0_HP53         SIWX91X_GPIO(3,  0xFF, 17, 3,  5, 0)
#define SSI_CS1_HP10         SIWX91X_GPIO(3,  0xFF,  5, 0, 10, 0)
#define SSI_CS2_HP15         SIWX91X_GPIO(3,  0xFF,  8, 0, 15, 0)
#define SSI_CS2_HP50         SIWX91X_GPIO(3,  0xFF, 14, 3,  2, 0)
#define SSI_CS3_HP51         SIWX91X_GPIO(3,  0xFF, 15, 3,  3, 0)
#define SSI_DATA0_HP11       SIWX91X_GPIO(3,  0xFF,  6, 0, 11, 0)
#define SSI_DATA0_HP26       SIWX91X_GPIO(3,  0xFF,  0, 1, 10, 0)
#define SSI_DATA0_HP56       SIWX91X_GPIO(3,  0xFF, 20, 3,  8, 0)
#define SSI_DATA1_HP10       SIWX91X_GPIO(12, 0xFF,  5, 0, 10, 0)
#define SSI_DATA1_HP12       SIWX91X_GPIO(3,  0xFF,  7, 0, 12, 0)
#define SSI_DATA1_HP27       SIWX91X_GPIO(3,  0xFF,  0, 1, 11, 0)
#define SSI_DATA1_HP57       SIWX91X_GPIO(3,  0xFF, 21, 3,  9, 0)
#define SSI_DATA2_HP6        SIWX91X_GPIO(3,  0xFF,  1, 0,  6, 0)
#define SSI_DATA2_HP29       SIWX91X_GPIO(3,  0xFF,  0, 1, 13, 0)
#define SSI_DATA2_HP54       SIWX91X_GPIO(3,  0xFF, 18, 3,  6, 0)
#define SSI_DATA3_HP7        SIWX91X_GPIO(3,  0xFF,  2, 0,  7, 0)
#define SSI_DATA3_HP30       SIWX91X_GPIO(3,  0xFF,  0, 1, 14, 0)
#define SSI_DATA3_HP55       SIWX91X_GPIO(3,  0xFF, 19, 3,  7, 0)

#define SSIS_CLK_HP8         SIWX91X_GPIO(8, 0xFF,  3, 0,  8, 0)
#define SSIS_CLK_HP26        SIWX91X_GPIO(8, 0xFF,  0, 1, 10, 0)
#define SSIS_CLK_HP47        SIWX91X_GPIO(8, 0xFF, 11, 2, 15, 0)
#define SSIS_CLK_HP52        SIWX91X_GPIO(8, 0xFF, 16, 3,  4, 0)
#define SSIS_CS_HP9          SIWX91X_GPIO(8, 0xFF,  4, 0,  9, 0)
#define SSIS_CS_HP25         SIWX91X_GPIO(8, 0xFF,  0, 1,  9, 0)
#define SSIS_CS_HP46         SIWX91X_GPIO(8, 0xFF, 10, 2, 14, 0)
#define SSIS_CS_HP53         SIWX91X_GPIO(8, 0xFF, 17, 3,  5, 0)
#define SSIS_MISO_HP11       SIWX91X_GPIO(8, 0xFF,  6, 0, 11, 0)
#define SSIS_MISO_HP28       SIWX91X_GPIO(8, 0xFF,  0, 1, 12, 0)
#define SSIS_MISO_HP49       SIWX91X_GPIO(8, 0xFF, 13, 3,  1, 0)
#define SSIS_MISO_HP57       SIWX91X_GPIO(8, 0xFF, 21, 3,  9, 0)
#define SSIS_MOSI_HP10       SIWX91X_GPIO(8, 0xFF,  5, 0, 10, 0)
#define SSIS_MOSI_HP27       SIWX91X_GPIO(8, 0xFF,  0, 1, 11, 0)
#define SSIS_MOSI_HP48       SIWX91X_GPIO(8, 0xFF, 12, 3,  0, 0)
#define SSIS_MOSI_HP56       SIWX91X_GPIO(8, 0xFF, 20, 3,  8, 0)

#define TIMER0_HP7           SIWX91X_GPIO(9,    5,    2, 0,  7, 1)
#define TIMER0_HP27          SIWX91X_GPIO(11,   5,    0, 1, 11, 8)
#define TIMER0_HP46          SIWX91X_GPIO(9,    5,   10, 2, 14, 8)
#define TIMER0_ULP4          SIWX91X_GPIO(0xFF, 9, 0xFF, 4,  0, 4)
#define TIMER0_ULP8          SIWX91X_GPIO(0xFF, 5, 0xFF, 4,  0, 8)

#define TIMER1_HP15          SIWX91X_GPIO(9,    5,    8, 0, 15, 7)
#define TIMER1_HP26          SIWX91X_GPIO(11,   5,    0, 1, 10, 7)
#define TIMER1_ULP5          SIWX91X_GPIO(0xFF, 9, 0xFF, 4,  0, 5)
#define TIMER1_ULP7          SIWX91X_GPIO(0xFF, 5, 0xFF, 4,  0, 7)

#define TIMER2_ULP1          SIWX91X_GPIO(0xFF, 5, 0xFF, 4, 0, 1)

#define TRACE_CLK_HP7        SIWX91X_GPIO(13, 0xFF,  2, 0,  7, 0)
#define TRACE_CLK_HP47       SIWX91X_GPIO(6,  0xFF, 11, 2, 15, 0)
#define TRACE_CLK_HP53       SIWX91X_GPIO(6,  0xFF, 17, 3,  5, 0)
#define TRACE_CLKIN_HP6      SIWX91X_GPIO(13, 0xFF,  1, 0,  6, 0)
#define TRACE_CLKIN_HP15     SIWX91X_GPIO(6,  0xFF,  8, 0, 15, 0)
#define TRACE_CLKIN_HP46     SIWX91X_GPIO(6,  0xFF, 10, 2, 14, 0)
#define TRACE_CLKIN_HP52     SIWX91X_GPIO(6,  0xFF, 16, 3,  4, 0)
#define TRACE_D0_HP8         SIWX91X_GPIO(13, 0xFF,  3, 0,  8, 0)
#define TRACE_D0_HP48        SIWX91X_GPIO(6,  0xFF, 12, 3,  0, 0)
#define TRACE_D0_HP54        SIWX91X_GPIO(6,  0xFF, 18, 3,  6, 0)
#define TRACE_D1_HP9         SIWX91X_GPIO(13, 0xFF,  4, 0,  9, 0)
#define TRACE_D1_HP49        SIWX91X_GPIO(6,  0xFF, 13, 3,  1, 0)
#define TRACE_D1_HP55        SIWX91X_GPIO(6,  0xFF, 19, 3,  7, 0)
#define TRACE_D2_HP10        SIWX91X_GPIO(13, 0xFF,  5, 0, 10, 0)
#define TRACE_D2_HP50        SIWX91X_GPIO(6,  0xFF, 14, 3,  2, 0)
#define TRACE_D2_HP56        SIWX91X_GPIO(6,  0xFF, 20, 3,  8, 0)
#define TRACE_D3_HP11        SIWX91X_GPIO(13, 0xFF,  6, 0, 11, 0)
#define TRACE_D3_HP51        SIWX91X_GPIO(6,  0xFF, 15, 3,  3, 0)
#define TRACE_D3_HP57        SIWX91X_GPIO(6,  0xFF, 21, 3,  9, 0)

#define UART0_CLK_HP8        SIWX91X_GPIO(2,  0xFF,  3, 0,  8,  0)
#define UART0_CLK_HP25       SIWX91X_GPIO(2,  0xFF,  0, 1,  9,  0)
#define UART0_CLK_HP52       SIWX91X_GPIO(2,  0xFF, 16, 3,  4,  0)
#define UART0_CLK_ULP0       SIWX91X_GPIO(2,     6, 22, 4,  0,  0)
#define UART0_CTS_HP6        SIWX91X_GPIO(2,  0xFF,  1, 0,  6,  0)
#define UART0_CTS_HP26       SIWX91X_GPIO(2,  0xFF,  0, 1, 10,  0)
#define UART0_CTS_HP56       SIWX91X_GPIO(2,  0xFF, 20, 3,  8,  0)
#define UART0_CTS_ULP6       SIWX91X_GPIO(2,     6, 28, 4,  6,  6)
#define UART0_DCD_HP12       SIWX91X_GPIO(2,  0xFF,  7, 0, 12,  0)
#define UART0_DCD_HP29       SIWX91X_GPIO(12, 0xFF,  0, 1, 13,  0)
#define UART0_DSR_HP11       SIWX91X_GPIO(2,  0xFF,  6, 0, 11,  0)
#define UART0_DSR_HP57       SIWX91X_GPIO(2,  0xFF, 21, 3,  9,  0)
#define UART0_DTR_HP7        SIWX91X_GPIO(2,  0xFF,  2, 0,  7,  0)
#define UART0_IRRX_HP25      SIWX91X_GPIO(13, 0xFF,  0, 1,  9,  0)
#define UART0_IRRX_HP47      SIWX91X_GPIO(2,  0xFF, 11, 2, 15,  0)
#define UART0_IRRX_ULP0      SIWX91X_GPIO(11,    6, 22, 4,  0,  0)
#define UART0_IRRX_ULP7      SIWX91X_GPIO(2,     6, 29, 4,  7,  7)
#define UART0_IRTX_HP26      SIWX91X_GPIO(13, 0xFF,  0, 1, 10,  0)
#define UART0_IRTX_HP48      SIWX91X_GPIO(2,  0xFF, 12, 3,  0,  0)
#define UART0_IRTX_ULP1      SIWX91X_GPIO(11,    6, 23, 4,  1,  1)
#define UART0_IRTX_ULP8      SIWX91X_GPIO(2,     6, 30, 4,  8,  8)
#define UART0_RI_HP27        SIWX91X_GPIO(2,  0xFF,  0, 1, 11,  0)
#define UART0_RI_HP46        SIWX91X_GPIO(2,  0xFF, 10, 2, 14,  0)
#define UART0_RI_ULP4        SIWX91X_GPIO(11,    6, 26, 4,  4,  4)
#define UART0_RS485DE_HP29   SIWX91X_GPIO(13, 0xFF,  0, 1, 13,  0)
#define UART0_RS485DE_HP51   SIWX91X_GPIO(2,  0xFF, 15, 3,  3,  0)
#define UART0_RS485DE_ULP7   SIWX91X_GPIO(11,    6, 29, 4,  7,  7)
#define UART0_RS485DE_ULP11  SIWX91X_GPIO(2,     6, 33, 4, 11, 11)
#define UART0_RS485EN_HP27   SIWX91X_GPIO(13, 0xFF,  0, 1, 11,  0)
#define UART0_RS485EN_HP49   SIWX91X_GPIO(2,  0xFF, 13, 3,  1,  0)
#define UART0_RS485EN_ULP5   SIWX91X_GPIO(11,    6, 27, 4,  5,  5)
#define UART0_RS485EN_ULP9   SIWX91X_GPIO(2,     6, 31, 4,  9,  9)
#define UART0_RS485RE_HP28   SIWX91X_GPIO(13, 0xFF,  0, 1, 12,  0)
#define UART0_RS485RE_HP50   SIWX91X_GPIO(2,  0xFF, 14, 3,  2,  0)
#define UART0_RS485RE_ULP6   SIWX91X_GPIO(11,    6, 28, 4,  6,  6)
#define UART0_RS485RE_ULP10  SIWX91X_GPIO(2,     6, 32, 4, 10, 10)
#define UART0_RTS_HP9        SIWX91X_GPIO(2,  0xFF,  4, 0,  9,  0)
#define UART0_RTS_HP28       SIWX91X_GPIO(2,  0xFF,  0, 1, 12,  0)
#define UART0_RTS_HP53       SIWX91X_GPIO(2,  0xFF, 17, 3,  5,  0)
#define UART0_RTS_ULP5       SIWX91X_GPIO(2,     6, 27, 4,  5,  5)
#define UART0_RX_HP10        SIWX91X_GPIO(2,  0xFF,  5, 0, 10,  0)
#define UART0_RX_HP29        SIWX91X_GPIO(2,  0xFF,  0, 1, 13,  0)
#define UART0_RX_HP55        SIWX91X_GPIO(2,  0xFF, 19, 3,  7,  0)
#define UART0_RX_ULP1        SIWX91X_GPIO(2,     6, 23, 4,  1,  1)
#define UART0_RX_ULP6        SIWX91X_GPIO(4,     6, 28, 4,  6,  6)
#define UART0_TX_HP30        SIWX91X_GPIO(2,  0xFF,  0, 1, 14,  0)
#define UART0_TX_HP54        SIWX91X_GPIO(2,  0xFF, 18, 3,  6,  0)
#define UART0_TX_ULP4        SIWX91X_GPIO(2,     6, 26, 4,  4,  4)
#define UART0_TX_ULP7        SIWX91X_GPIO(4,     6, 29, 4,  7,  7)

#define UART1_CTS_HP11       SIWX91X_GPIO(6,  0xFF,  6, 0, 11,  0)
#define UART1_CTS_HP32       SIWX91X_GPIO(12, 0xFF,  9, 2,  0,  0)
#define UART1_CTS_HP51       SIWX91X_GPIO(9,  0xFF, 15, 3,  3,  0)
#define UART1_CTS_ULP1       SIWX91X_GPIO(9,     6, 23, 4,  1,  1)
#define UART1_CTS_ULP7       SIWX91X_GPIO(6,     6, 29, 4,  7,  7)
#define UART1_CTS_ULP9       SIWX91X_GPIO(9,     6, 31, 4,  9,  9)
#define UART1_RS485DE_HP9    SIWX91X_GPIO(6,  0xFF,  4, 0,  9,  0)
#define UART1_RS485DE_ULP2   SIWX91X_GPIO(6,     6, 24, 4,  2,  2)
#define UART1_RS485DE_ULP11  SIWX91X_GPIO(6,     6, 33, 4, 11, 11)
#define UART1_RS485EN_HP12   SIWX91X_GPIO(6,  0xFF,  7, 0, 12,  0)
#define UART1_RS485EN_HP26   SIWX91X_GPIO(6,  0xFF,  0, 1, 10,  0)
#define UART1_RS485EN_ULP0   SIWX91X_GPIO(6,     6, 22, 4,  0,  0)
#define UART1_RS485RE_HP8    SIWX91X_GPIO(6,  0xFF,  3, 0,  8,  0)
#define UART1_RS485RE_ULP1   SIWX91X_GPIO(6,     6, 23, 4,  1,  1)
#define UART1_RS485RE_ULP10  SIWX91X_GPIO(6,     6, 32, 4, 10, 10)
#define UART1_RTS_HP10       SIWX91X_GPIO(6,  0xFF,  5, 0, 10,  0)
#define UART1_RTS_HP27       SIWX91X_GPIO(6,  0xFF,  0, 1, 11,  0)
#define UART1_RTS_HP28       SIWX91X_GPIO(6,  0xFF,  0, 1, 12,  0)
#define UART1_RTS_HP31       SIWX91X_GPIO(12, 0xFF,  9, 1, 15,  0)
#define UART1_RTS_HP50       SIWX91X_GPIO(9,  0xFF, 14, 3,  2,  0)
#define UART1_RTS_ULP0       SIWX91X_GPIO(9,     6, 22, 4,  0,  0)
#define UART1_RTS_ULP6       SIWX91X_GPIO(6,     6, 28, 4,  6,  6)
#define UART1_RTS_ULP8       SIWX91X_GPIO(9,     6, 30, 4,  8,  8)
#define UART1_RX_HP6         SIWX91X_GPIO(6,  0xFF,  1, 0,  6,  0)
#define UART1_RX_HP29        SIWX91X_GPIO(6,  0xFF,  0, 1, 13,  0)
#define UART1_RX_HP33        SIWX91X_GPIO(12, 0xFF,  9, 2,  1,  0)
#define UART1_RX_ULP2        SIWX91X_GPIO(9,     6, 24, 4,  1,  1)
#define UART1_RX_ULP4        SIWX91X_GPIO(6,     6, 26, 4,  4,  4)
#define UART1_RX_ULP8        SIWX91X_GPIO(6,     6, 30, 4,  8,  8)
#define UART1_RX_ULP10       SIWX91X_GPIO(9,     6, 32, 4, 10, 10)
#define UART1_TX_HP15        SIWX91X_GPIO(2,  0xFF,  8, 0, 15,  0)
#define UART1_TX_HP7         SIWX91X_GPIO(6,  0xFF,  2, 0,  7,  0)
#define UART1_TX_HP30        SIWX91X_GPIO(6,  0xFF,  0, 1, 14,  0)
#define UART1_TX_HP34        SIWX91X_GPIO(12, 0xFF,  9, 2,  2,  0)
#define UART1_TX_ULP3        SIWX91X_GPIO(9,     6, 25, 4,  1,  1)
#define UART1_TX_ULP5        SIWX91X_GPIO(6,     6, 27, 4,  5,  5)
#define UART1_TX_ULP9        SIWX91X_GPIO(6,     6, 31, 4,  9,  9)
#define UART1_TX_ULP11       SIWX91X_GPIO(9,     6, 33, 4, 11, 11)

#define ULPI2C_SCL_HP11      SIWX91X_GPIO(9,    4,    6, 0, 11,  5)
#define ULPI2C_SCL_HP15      SIWX91X_GPIO(9,    4,    8, 0, 15,  7)
#define ULPI2C_SCL_HP7       SIWX91X_GPIO(9,    4,    2, 0,  7,  1)
#define ULPI2C_SCL_HP26      SIWX91X_GPIO(11,   4,    0, 1, 10,  7)
#define ULPI2C_SCL_HP27      SIWX91X_GPIO(11,   4,    0, 1, 11,  8)
#define ULPI2C_SCL_HP46      SIWX91X_GPIO(9,    4,   10, 2, 14,  8)
#define ULPI2C_SCL_ULP1      SIWX91X_GPIO(0xFF, 4, 0xFF, 4,  0,  1)
#define ULPI2C_SCL_ULP5      SIWX91X_GPIO(0xFF, 4, 0xFF, 4,  0,  5)
#define ULPI2C_SCL_ULP7      SIWX91X_GPIO(0xFF, 4, 0xFF, 4,  0,  7)
#define ULPI2C_SCL_ULP8      SIWX91X_GPIO(0xFF, 4, 0xFF, 4,  0,  8)
#define ULPI2C_SDA_HP6       SIWX91X_GPIO(9,    4,    1, 0,  6,  0)
#define ULPI2C_SDA_HP10      SIWX91X_GPIO(9,    4,    5, 0, 10,  4)
#define ULPI2C_SDA_HP12      SIWX91X_GPIO(9,    4,    7, 0, 12,  6)
#define ULPI2C_SDA_HP25      SIWX91X_GPIO(11,   4,    0, 1,  9,  6)
#define ULPI2C_SDA_HP28      SIWX91X_GPIO(11,   4,    0, 1, 12,  9)
#define ULPI2C_SDA_HP30      SIWX91X_GPIO(11,   4,    0, 1, 14, 11)
#define ULPI2C_SDA_HP47      SIWX91X_GPIO(9,    4,   11, 2, 15,  9)
#define ULPI2C_SDA_HP49      SIWX91X_GPIO(9,    4,   13, 3,  1, 11)
#define ULPI2C_SDA_ULP0      SIWX91X_GPIO(0xFF, 4, 0xFF, 4,  0,  0)
#define ULPI2C_SDA_ULP4      SIWX91X_GPIO(0xFF, 4, 0xFF, 4,  0,  4)
#define ULPI2C_SDA_ULP6      SIWX91X_GPIO(0xFF, 4, 0xFF, 4,  0,  6)
#define ULPI2C_SDA_ULP9      SIWX91X_GPIO(0xFF, 4, 0xFF, 4,  0,  9)
#define ULPI2C_SDA_ULP11     SIWX91X_GPIO(0xFF, 4, 0xFF, 4,  0, 11)

#define ULPI2S_CLK_HP15      SIWX91X_GPIO(9,    2,    8, 0, 15,  7)
#define ULPI2S_CLK_HP26      SIWX91X_GPIO(11,   2,    0, 1, 10,  7)
#define ULPI2S_CLK_HP27      SIWX91X_GPIO(11,   2,    0, 1, 11,  8)
#define ULPI2S_CLK_HP46      SIWX91X_GPIO(9,    2,   10, 2, 14,  8)
#define ULPI2S_CLK_ULP7      SIWX91X_GPIO(0xFF, 2, 0xFF, 4,  0,  7)
#define ULPI2S_CLK_ULP8      SIWX91X_GPIO(0xFF, 2, 0xFF, 4,  0,  8)
#define ULPI2S_DIN_HP12      SIWX91X_GPIO(9,    2,    7, 0, 12,  6)
#define ULPI2S_DIN_HP6       SIWX91X_GPIO(9,    2,    1, 0,  6,  0)
#define ULPI2S_DIN_HP25      SIWX91X_GPIO(11,   2,    0, 1,  9,  6)
#define ULPI2S_DIN_HP28      SIWX91X_GPIO(11,   2,    0, 1, 12,  9)
#define ULPI2S_DIN_HP47      SIWX91X_GPIO(9,    2,   11, 2, 15,  9)
#define ULPI2S_DIN_ULP0      SIWX91X_GPIO(0xFF, 2, 0xFF, 4,  0,  0)
#define ULPI2S_DIN_ULP6      SIWX91X_GPIO(0xFF, 2, 0xFF, 4,  0,  6)
#define ULPI2S_DIN_ULP9      SIWX91X_GPIO(0xFF, 2, 0xFF, 4,  0,  9)
#define ULPI2S_DOUT_HP7      SIWX91X_GPIO(9,    2,    2, 0,  7,  1)
#define ULPI2S_DOUT_HP11     SIWX91X_GPIO(9,    2,    6, 0, 11,  5)
#define ULPI2S_DOUT_HP30     SIWX91X_GPIO(11,   2,    0, 1, 14, 11)
#define ULPI2S_DOUT_HP49     SIWX91X_GPIO(9,    2,   13, 3,  1, 11)
#define ULPI2S_DOUT_ULP1     SIWX91X_GPIO(0xFF, 2, 0xFF, 4,  0,  1)
#define ULPI2S_DOUT_ULP5     SIWX91X_GPIO(0xFF, 2, 0xFF, 4,  0,  5)
#define ULPI2S_DOUT_ULP11    SIWX91X_GPIO(0xFF, 2, 0xFF, 4,  0, 11)
#define ULPI2S_WS_HP8        SIWX91X_GPIO(9,    2,    3, 0,  8,  2)
#define ULPI2S_WS_HP10       SIWX91X_GPIO(9,    2,    5, 0, 10,  4)
#define ULPI2S_WS_HP29       SIWX91X_GPIO(11,   2,    0, 1, 13, 10)
#define ULPI2S_WS_HP48       SIWX91X_GPIO(9,    2,   12, 3,  0, 10)
#define ULPI2S_WS_ULP2       SIWX91X_GPIO(0xFF, 2, 0xFF, 4,  0,  2)
#define ULPI2S_WS_ULP4       SIWX91X_GPIO(0xFF, 2, 0xFF, 4,  0,  4)
#define ULPI2S_WS_ULP10      SIWX91X_GPIO(0xFF, 2, 0xFF, 4,  0, 10)

#define ULPSSI_CLK_HP6       SIWX91X_GPIO(9,    1,    1, 0,  6,  0)
#define ULPSSI_CLK_HP27      SIWX91X_GPIO(11,   1,    0, 1, 11,  8)
#define ULPSSI_CLK_HP46      SIWX91X_GPIO(9,    1,   10, 2, 14,  8)
#define ULPSSI_CLK_ULP0      SIWX91X_GPIO(0xFF, 1, 0xFF, 4,  0,  0)
#define ULPSSI_CLK_ULP4      SIWX91X_GPIO(0xFF, 8, 0xFF, 4,  0,  4)
#define ULPSSI_CLK_ULP8      SIWX91X_GPIO(0xFF, 1, 0xFF, 4,  0,  8)
#define ULPSSI_CS0_HP29      SIWX91X_GPIO(11,   1,    0, 1, 13, 10)
#define ULPSSI_CS0_HP48      SIWX91X_GPIO(9,    1,   12, 3,  0, 10)
#define ULPSSI_CS0_ULP7      SIWX91X_GPIO(0xFF, 8, 0xFF, 4,  0,  7)
#define ULPSSI_CS0_ULP10     SIWX91X_GPIO(0xFF, 1, 0xFF, 4,  0, 10)
#define ULPSSI_CS1_HP10      SIWX91X_GPIO(9,    1,    5, 0, 10,  4)
#define ULPSSI_CS1_ULP4      SIWX91X_GPIO(0xFF, 1, 0xFF, 4,  0,  4)
#define ULPSSI_CS2_HP12      SIWX91X_GPIO(9,    1,    7, 0, 12,  6)
#define ULPSSI_CS2_HP25      SIWX91X_GPIO(11,   1,    0, 1,  9,  6)
#define ULPSSI_CS2_ULP6      SIWX91X_GPIO(0xFF, 1, 0xFF, 4,  0,  6)
#define ULPSSI_DIN_HP8       SIWX91X_GPIO(9,    1,    3, 0,  8,  2)
#define ULPSSI_DIN_HP28      SIWX91X_GPIO(11,   1,    0, 1, 12,  9)
#define ULPSSI_DIN_HP47      SIWX91X_GPIO(9,    1,   11, 2, 15,  9)
#define ULPSSI_DIN_ULP2      SIWX91X_GPIO(0xFF, 1, 0xFF, 4,  0,  2)
#define ULPSSI_DIN_ULP6      SIWX91X_GPIO(0xFF, 8, 0xFF, 4,  0,  6)
#define ULPSSI_DIN_ULP9      SIWX91X_GPIO(0xFF, 1, 0xFF, 4,  0,  9)
#define ULPSSI_DOUT_HP7      SIWX91X_GPIO(9,    1,    2, 0,  7,  1)
#define ULPSSI_DOUT_HP30     SIWX91X_GPIO(11,   1,    0, 1, 14, 11)
#define ULPSSI_DOUT_HP49     SIWX91X_GPIO(9,    1,   13, 3,  1, 11)
#define ULPSSI_DOUT_ULP1     SIWX91X_GPIO(0xFF, 1, 0xFF, 4,  0,  1)
#define ULPSSI_DOUT_ULP5     SIWX91X_GPIO(0xFF, 8, 0xFF, 4,  0,  5)
#define ULPSSI_DOUT_ULP11    SIWX91X_GPIO(0xFF, 1, 0xFF, 4,  0, 11)

#define ULPUART_CTS_HP7      SIWX91X_GPIO(9,    3,    2, 0,  7,  1)
#define ULPUART_CTS_HP11     SIWX91X_GPIO(9,    3,    6, 0, 11,  5)
#define ULPUART_CTS_HP27     SIWX91X_GPIO(11,   3,    0, 1, 11,  8)
#define ULPUART_CTS_HP46     SIWX91X_GPIO(9,    3,   10, 2, 14,  8)
#define ULPUART_CTS_ULP1     SIWX91X_GPIO(0xFF, 3, 0xFF, 4,  0,  1)
#define ULPUART_CTS_ULP5     SIWX91X_GPIO(0xFF, 3, 0xFF, 4,  0,  5)
#define ULPUART_CTS_ULP8     SIWX91X_GPIO(0xFF, 3, 0xFF, 4,  0,  8)
#define ULPUART_RTS_HP6      SIWX91X_GPIO(9,    3,    1, 0,  6,  0)
#define ULPUART_RTS_HP10     SIWX91X_GPIO(9,    3,    5, 0, 10,  4)
#define ULPUART_RTS_HP29     SIWX91X_GPIO(11,   3,    0, 1, 13, 10)
#define ULPUART_RTS_HP48     SIWX91X_GPIO(9,    3,   12, 3,  0, 10)
#define ULPUART_RTS_ULP0     SIWX91X_GPIO(0xFF, 3, 0xFF, 4,  0,  0)
#define ULPUART_RTS_ULP4     SIWX91X_GPIO(0xFF, 3, 0xFF, 4,  0,  4)
#define ULPUART_RTS_ULP10    SIWX91X_GPIO(0xFF, 3, 0xFF, 4,  0, 10)
#define ULPUART_RX_HP8       SIWX91X_GPIO(9,    3,    3, 0,  8,  2)
#define ULPUART_RX_HP12      SIWX91X_GPIO(9,    3,    7, 0, 12,  6)
#define ULPUART_RX_HP25      SIWX91X_GPIO(11,   3,    0, 1,  9,  6)
#define ULPUART_RX_HP28      SIWX91X_GPIO(11,   3,    0, 1, 12,  9)
#define ULPUART_RX_HP47      SIWX91X_GPIO(9,    3,   11, 2, 15,  9)
#define ULPUART_RX_ULP2      SIWX91X_GPIO(0xFF, 3, 0xFF, 4,  0,  2)
#define ULPUART_RX_ULP6      SIWX91X_GPIO(0xFF, 3, 0xFF, 4,  0,  6)
#define ULPUART_RX_ULP9      SIWX91X_GPIO(0xFF, 3, 0xFF, 4,  0,  9)
#define ULPUART_TX_HP15      SIWX91X_GPIO(9,    3,    8, 0, 15,  7)
#define ULPUART_TX_HP26      SIWX91X_GPIO(11,   3,    0, 1, 10,  7)
#define ULPUART_TX_HP30      SIWX91X_GPIO(11,   3,    0, 1, 14, 11)
#define ULPUART_TX_HP49      SIWX91X_GPIO(9,    3,   13, 3,  1, 11)
#define ULPUART_TX_ULP7      SIWX91X_GPIO(0xFF, 3, 0xFF, 4,  0,  7)
#define ULPUART_TX_ULP11     SIWX91X_GPIO(0xFF, 3, 0xFF, 4,  0, 11)

#define UULP_GPIO4_ULP2      SIWX91X_GPIO(0xFF,  4, 0xFF, 4, 0, 2)
#define UULP_TESTMODE0_ULP7  SIWX91X_GPIO(0xFF, 11, 0xFF, 4, 0, 7)
#define UULP_TESTMODE0_ULP9  SIWX91X_GPIO(0xFF,  5, 0xFF, 4, 0, 9)

#define WIFI_ANT0_ULP0       SIWX91X_GPIO(0xFF, 6, 0xFF, 4, 0,  0)
#define WIFI_ANT1_ULP4       SIWX91X_GPIO(0xFF, 6, 0xFF, 4, 0,  4)
#define WIFI_ANT2_ULP5       SIWX91X_GPIO(0xFF, 6, 0xFF, 4, 0,  5)



/* The following definitions are duplicates of signals that are also
 * available on the same pins using other GPIO modes.
 * #define IR_OUTPUT_ULP5       SIWX91X_GPIO(0xFF, 10, 0xFF, 4, 0, 5)
 * #define PMU_TEST2_HP30       SIWX91X_GPIO(13, 0xFF, 0, 1, 14, 0)
 * #define PWM_1H_ULP1          SIWX91X_GPIO(8, 6, 23, 4, 1, 1)
 * #define PWM_1L_ULP0          SIWX91X_GPIO(8, 6, 22, 4, 0, 0)
 */

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SILABS_SIWX91X_PINCTRL_H_ */
```

## 180.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Silicon Laboratories Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 665 行

以下定义与通过其他 GPIO 模式可在相同引脚上使用的信号重复：

```c
#define IR_OUTPUT_ULP5       SIWX91X_GPIO(0xFF, 10, 0xFF, 4, 0, 5)
#define PMU_TEST2_HP30       SIWX91X_GPIO(13, 0xFF, 0, 1, 14, 0)
#define PWM_1H_ULP1          SIWX91X_GPIO(8, 6, 23, 4, 1, 1)
#define PWM_1L_ULP0          SIWX91X_GPIO(8, 6, 22, 4, 0, 0)
```

### 注释 3：原第 673 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SILABS_SIWX91X_PINCTRL_H_`。

## 180.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/siwx91x-pinctrl_8h.html)
- [zephyr/dt-bindings/pinctrl/silabs-pinctrl-siwx91x.h](https://docs.zephyrproject.org/latest/doxygen/html/silabs-pinctrl-siwx91x_8h.html)
- [silabs-pinctrl-siwx91x.h](https://docs.zephyrproject.org/latest/doxygen/html/silabs-pinctrl-siwx91x_8h.html)

---

[上一章](P179_simulator.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P181_six301-dma.h_源码浏览.md)
