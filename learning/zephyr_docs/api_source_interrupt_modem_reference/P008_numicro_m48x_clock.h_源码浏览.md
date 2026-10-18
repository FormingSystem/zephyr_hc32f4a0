---
id: learning.zephyr-docs.api-source-interrupt-modem-reference.page-8
title: numicro_m48x_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/numicro__m48x__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_numicro\_m48x\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/numicro__m48x__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P273_zephyr__dt-bindings__clock__numicro_m48x_clock.h_文件参考.md)。

## 8.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
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
<a id="l00103"></a>
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
<a id="l00150"></a>
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
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
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
<a id="l00367"></a>
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
<a id="l00415"></a>
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
<a id="l00661"></a>
<a id="l00662"></a>
<a id="l00663"></a>
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
<a id="l00674"></a>
<a id="l00675"></a>
<a id="l00676"></a>
<a id="l00678"></a>
<a id="l00679"></a>
<a id="l00680"></a>
<a id="l00683"></a>
<a id="l00684"></a>

```c


/*
 * Copyright (c) 2026 Fiona Behrens
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_NUMICRO_M48X_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_NUMICRO_M48X_CLOCK_H_



/* Beginning of M480 BSP clk_reg.h copy */


#define NUMICRO_CLK_AHBCLK_PDMACKEND_Pos  1
#define NUMICRO_CLK_AHBCLK_ISPCKEN_Pos    2
#define NUMICRO_CLK_AHBCLK_EBICKEN_Pos    3
#define NUMICRO_CLK_AHBCLK_EMACKEN_Pos    5
#define NUMICRO_CLK_AHBCLK_SDH0CKEN_Pos   6
#define NUMICRO_CLK_AHBCLK_CRCKEN_Pos     7
#define NUMICRO_CLK_AHBCLK_CCAPCKEN_Pos   8
#define NUMICRO_CLK_AHBCLK_SENCKEN_Pos    9
#define NUMICRO_CLK_AHBCLK_HSUSBDCKEN_Pos 10
#define NUMICRO_CLK_AHBCLK_CRPTCHKEN_Pos  12
#define NUMICRO_CLK_AHBCLK_SPIMCKEN_Pos   14
#define NUMICRO_CLK_AHBCLK_FMCIDLE_Pos    15
#define NUMICRO_CLK_AHBCLK_USBHCKEN_Pos   16
#define NUMICRO_CLK_AHBCLK_SDH1CKEN_Pos   17

#define NUMICRO_CLK_APBCLK0_WDTCKEN_Pos    0
#define NUMICRO_CLK_APBCLK0_RTCCKEN_Pos    1
#define NUMICRO_CLK_APBCLK0_TMR0CKEN_Pos   2
#define NUMICRO_CLK_APBCLK0_TMR1CKEN_Pos   3
#define NUMICRO_CLK_APBCLK0_TMR2CKEN_Pos   4
#define NUMICRO_CLK_APBCLK0_TMR3CKEN_Pos   5
#define NUMICRO_CLK_APBCLK0_CLKOCKEN_Pos   6
#define NUMICRO_CLK_APBCLK0_ACMP01CKEN_Pos 7
#define NUMICRO_CLK_APBCLK0_I2C0CKEN_Pos   8
#define NUMICRO_CLK_APBCLK0_I2C1CKEN_Pos   9
#define NUMICRO_CLK_APBCLK0_I2C2CKEN_Pos   10
#define NUMICRO_CLK_APBCLK0_QSPI0CKEN_Pos  12
#define NUMICRO_CLK_APBCLK0_SPI0CKEN_Pos   13
#define NUMICRO_CLK_APBCLK0_SPI1CKEN_Pos   14
#define NUMICRO_CLK_APBCLK0_SPI2CKEN_Pos   15
#define NUMICRO_CLK_APBCLK0_UART0CKEN_Pos  16
#define NUMICRO_CLK_APBCLK0_UART1CKEN_Pos  17
#define NUMICRO_CLK_APBCLK0_UART2CKEN_Pos  18
#define NUMICRO_CLK_APBCLK0_UART3CKEN_Pos  19
#define NUMICRO_CLK_APBCLK0_UART4CKEN_Pos  20
#define NUMICRO_CLK_APBCLK0_UART5CKEN_Pos  21
#define NUMICRO_CLK_APBCLK0_UART6CKEN_Pos  22
#define NUMICRO_CLK_APBCLK0_UART7CKEN_Pos  23
#define NUMICRO_CLK_APBCLK0_CAN0CKEN_Pos   24
#define NUMICRO_CLK_APBCLK0_CAN1CKEN_Pos   25
#define NUMICRO_CLK_APBCLK0_OTGCKEN_Pos    26
#define NUMICRO_CLK_APBCLK0_USBDCKEN_Pos   27
#define NUMICRO_CLK_APBCLK0_EADCCKEN_Pos   28
#define NUMICRO_CLK_APBCLK0_I2S0CKEN_Pos   29
#define NUMICRO_CLK_APBCLK0_HSOTGCKEN_Pos  30

#define NUMICRO_CLK_APBCLK1_SC0CKEN_Pos   0
#define NUMICRO_CLK_APBCLK1_SC1CKEN_Pos   1
#define NUMICRO_CLK_APBCLK1_SC2CKEN_Pos   2
#define NUMICRO_CLK_APBCLK1_QSPI1CKEN_Pos 4
#define NUMICRO_CLK_APBCLK1_SPI3CKEN_Pos  6
#define NUMICRO_CLK_APBCLK1_USCI0CKEN_Pos 8
#define NUMICRO_CLK_APBCLK1_USCI1CKEN_Pos 9
#define NUMICRO_CLK_APBCLK1_DACCKEN_Pos   12
#define NUMICRO_CLK_APBCLK1_EPWM0CKEN_Pos 16
#define NUMICRO_CLK_APBCLK1_EPWM1CKEN_Pos 17
#define NUMICRO_CLK_APBCLK1_BPWM0CKEN_Pos 18
#define NUMICRO_CLK_APBCLK1_BPWM1CKEN_Pos 19
#define NUMICRO_CLK_APBCLK1_QEI0CKEN_Pos  22
#define NUMICRO_CLK_APBCLK1_QEI1CKEN_Pos  23
#define NUMICRO_CLK_APBCLK1_TRNGCKEN_Pos  25
#define NUMICRO_CLK_APBCLK1_ECAP0CKEN_Pos 26
#define NUMICRO_CLK_APBCLK1_ECAP1CKEN_Pos 27
#define NUMICRO_CLK_APBCLK1_CAN2CKEN_Pos  28
#define NUMICRO_CLK_APBCLK1_OPACKEN_Pos   30
#define NUMICRO_CLK_APBCLK1_EADC1CKEN_Pos 31



#define NUMICRO_CLK_CLKSEL0_HCLKSEL_Pos  0
#define NUMICRO_CLK_CLKSEL0_STCLKSEL_Pos 3
#define NUMICRO_CLK_CLKSEL0_USBSEL_Pos   8
#define NUMICRO_CLK_CLKSEL0_CCAPSEL_Pos  16
#define NUMICRO_CLK_CLKSEL0_SDH0SEL_Pos  20
#define NUMICRO_CLK_CLKSEL0_SDH1SEL_Pos  22

#define NUMICRO_CLK_CLKSEL1_WDTSEL_Pos   0
#define NUMICRO_CLK_CLKSEL1_TMR0SEL_Pos  8
#define NUMICRO_CLK_CLKSEL1_TMR1SEL_Pos  12
#define NUMICRO_CLK_CLKSEL1_TMR2SEL_Pos  16
#define NUMICRO_CLK_CLKSEL1_TMR3SEL_Pos  20
#define NUMICRO_CLK_CLKSEL1_UART0SEL_Pos 24
#define NUMICRO_CLK_CLKSEL1_UART1SEL_Pos 26
#define NUMICRO_CLK_CLKSEL1_CLKOSEL_Pos  28
#define NUMICRO_CLK_CLKSEL1_WWDTSEL_Pos  30

#define NUMICRO_CLK_CLKSEL2_EPWM0SEL_Pos 0
#define NUMICRO_CLK_CLKSEL2_EPWM1SEL_Pos 1
#define NUMICRO_CLK_CLKSEL2_QSPI0SEL_Pos 2
#define NUMICRO_CLK_CLKSEL2_SPI0SEL_Pos  4
#define NUMICRO_CLK_CLKSEL2_SPI1SEL_Pos  6
#define NUMICRO_CLK_CLKSEL2_BPWM0SEL_Pos 8
#define NUMICRO_CLK_CLKSEL2_BPWM1SEL_Pos 9
#define NUMICRO_CLK_CLKSEL2_SPI2SEL_Pos  10
#define NUMICRO_CLK_CLKSEL2_SPI3SEL_Pos  12

#define NUMICRO_CLK_CLKSEL3_SC0SEL_Pos   0
#define NUMICRO_CLK_CLKSEL3_SC1SEL_Pos   2
#define NUMICRO_CLK_CLKSEL3_SC2SEL_Pos   4
#define NUMICRO_CLK_CLKSEL3_RTCSEL_Pos   8
#define NUMICRO_CLK_CLKSEL3_QSPI1SEL_Pos 12
#define NUMICRO_CLK_CLKSEL3_I2S0SEL_Pos  16
#define NUMICRO_CLK_CLKSEL3_UART6SEL_Pos 20
#define NUMICRO_CLK_CLKSEL3_UART7SEL_Pos 22
#define NUMICRO_CLK_CLKSEL3_UART2SEL_Pos 24
#define NUMICRO_CLK_CLKSEL3_UART3SEL_Pos 26
#define NUMICRO_CLK_CLKSEL3_UART4SEL_Pos 28
#define NUMICRO_CLK_CLKSEL3_UART5SEL_Pos 30



#define NUMICRO_CLK_CLKDIV0_HCLKDIV_Pos  0
#define NUMICRO_CLK_CLKDIV0_USBDIV_Pos   4
#define NUMICRO_CLK_CLKDIV0_UART0DIV_Pos 8
#define NUMICRO_CLK_CLKDIV0_UART1DIV_Pos 12
#define NUMICRO_CLK_CLKDIV0_EADCDIV_Pos  16
#define NUMICRO_CLK_CLKDIV0_SDH0DIV_Pos  24

#define NUMICRO_CLK_CLKDIV1_SC0DIV_Pos 0
#define NUMICRO_CLK_CLKDIV1_SC1DIV_Pos 8
#define NUMICRO_CLK_CLKDIV1_SC2DIV_Pos 16

#define NUMICRO_CLK_CLKDIV2_I2SDIV_Pos   0
#define NUMICRO_CLK_CLKDIV2_EADC1DIV_Pos 24

#define NUMICRO_CLK_CLKDIV3_CCAPDIV_Pos   0
#define NUMICRO_CLK_CLKDIV3_VSENSEDIV_Pos 8
#define NUMICRO_CLK_CLKDIV3_EMACDIV_Pos   16
#define NUMICRO_CLK_CLKDIV3_SDH1DIV_Pos   24

#define NUMICRO_CLK_CLKDIV4_UART2DIV_Pos 0
#define NUMICRO_CLK_CLKDIV4_UART3DIV_Pos 4
#define NUMICRO_CLK_CLKDIV4_UART4DIV_Pos 8
#define NUMICRO_CLK_CLKDIV4_UART5DIV_Pos 12
#define NUMICRO_CLK_CLKDIV4_UART6DIV_Pos 16
#define NUMICRO_CLK_CLKDIV4_UART7DIV_Pos 20


/* End of M480 BSP clk_reg.h copy */

/* Beginning of M480 BSP clk.h copy */


/*------------------------------------------------------------------------------------------------*/
/*  CLKSEL0 constant definitions.  (Write-protection) */
/*------------------------------------------------------------------------------------------------*/

#define NUMICRO_CLK_CLKSEL0_CCAPSEL_HXT  (0x0UL << NUMICRO_CLK_CLKSEL0_CCAPSEL_Pos)
#define NUMICRO_CLK_CLKSEL0_CCAPSEL_PLL  (0x1UL << NUMICRO_CLK_CLKSEL0_CCAPSEL_Pos)
#define NUMICRO_CLK_CLKSEL0_CCAPSEL_HCLK (0x2UL << NUMICRO_CLK_CLKSEL0_CCAPSEL_Pos)
#define NUMICRO_CLK_CLKSEL0_CCAPSEL_HIRC (0x3UL << NUMICRO_CLK_CLKSEL0_CCAPSEL_Pos)

#define NUMICRO_CLK_CLKSEL0_SDH0SEL_HXT  (0x0UL << NUMICRO_CLK_CLKSEL0_SDH0SEL_Pos)
#define NUMICRO_CLK_CLKSEL0_SDH0SEL_PLL  (0x1UL << NUMICRO_CLK_CLKSEL0_SDH0SEL_Pos)
#define NUMICRO_CLK_CLKSEL0_SDH0SEL_HIRC (0x3UL << NUMICRO_CLK_CLKSEL0_SDH0SEL_Pos)
#define NUMICRO_CLK_CLKSEL0_SDH0SEL_HCLK (0x2UL << NUMICRO_CLK_CLKSEL0_SDH0SEL_Pos)

#define NUMICRO_CLK_CLKSEL0_SDH1SEL_HXT  (0x0UL << NUMICRO_CLK_CLKSEL0_SDH1SEL_Pos)
#define NUMICRO_CLK_CLKSEL0_SDH1SEL_PLL  (0x1UL << NUMICRO_CLK_CLKSEL0_SDH1SEL_Pos)
#define NUMICRO_CLK_CLKSEL0_SDH1SEL_HIRC (0x3UL << NUMICRO_CLK_CLKSEL0_SDH1SEL_Pos)
#define NUMICRO_CLK_CLKSEL0_SDH1SEL_HCLK (0x2UL << NUMICRO_CLK_CLKSEL0_SDH1SEL_Pos)

/*------------------------------------------------------------------------------------------------*/
/*  CLKSEL1 constant definitions. */
/*------------------------------------------------------------------------------------------------*/
#define NUMICRO_CLK_CLKSEL1_WDTSEL_LXT          (0x1UL << NUMICRO_CLK_CLKSEL1_WDTSEL_Pos)
#define NUMICRO_CLK_CLKSEL1_WDTSEL_LIRC         (0x3UL << NUMICRO_CLK_CLKSEL1_WDTSEL_Pos)
#define NUMICRO_CLK_CLKSEL1_WDTSEL_HCLK_DIV2048 (0x2UL << NUMICRO_CLK_CLKSEL1_WDTSEL_Pos)

#define NUMICRO_CLK_CLKSEL1_TMR0SEL_HXT   (0x0UL << NUMICRO_CLK_CLKSEL1_TMR0SEL_Pos)
#define NUMICRO_CLK_CLKSEL1_TMR0SEL_LXT   (0x1UL << NUMICRO_CLK_CLKSEL1_TMR0SEL_Pos)
#define NUMICRO_CLK_CLKSEL1_TMR0SEL_LIRC  (0x5UL << NUMICRO_CLK_CLKSEL1_TMR0SEL_Pos)
#define NUMICRO_CLK_CLKSEL1_TMR0SEL_HIRC  (0x7UL << NUMICRO_CLK_CLKSEL1_TMR0SEL_Pos)
#define NUMICRO_CLK_CLKSEL1_TMR0SEL_PCLK0 (0x2UL << NUMICRO_CLK_CLKSEL1_TMR0SEL_Pos)
#define NUMICRO_CLK_CLKSEL1_TMR0SEL_EXT   (0x3UL << NUMICRO_CLK_CLKSEL1_TMR0SEL_Pos)

#define NUMICRO_CLK_CLKSEL1_TMR1SEL_HXT   (0x0UL << NUMICRO_CLK_CLKSEL1_TMR1SEL_Pos)
#define NUMICRO_CLK_CLKSEL1_TMR1SEL_LXT   (0x1UL << NUMICRO_CLK_CLKSEL1_TMR1SEL_Pos)
#define NUMICRO_CLK_CLKSEL1_TMR1SEL_LIRC  (0x5UL << NUMICRO_CLK_CLKSEL1_TMR1SEL_Pos)
#define NUMICRO_CLK_CLKSEL1_TMR1SEL_HIRC  (0x7UL << NUMICRO_CLK_CLKSEL1_TMR1SEL_Pos)
#define NUMICRO_CLK_CLKSEL1_TMR1SEL_PCLK0 (0x2UL << NUMICRO_CLK_CLKSEL1_TMR1SEL_Pos)
#define NUMICRO_CLK_CLKSEL1_TMR1SEL_EXT   (0x3UL << NUMICRO_CLK_CLKSEL1_TMR1SEL_Pos)

#define NUMICRO_CLK_CLKSEL1_TMR2SEL_HXT   (0x0UL << NUMICRO_CLK_CLKSEL1_TMR2SEL_Pos)
#define NUMICRO_CLK_CLKSEL1_TMR2SEL_LXT   (0x1UL << NUMICRO_CLK_CLKSEL1_TMR2SEL_Pos)
#define NUMICRO_CLK_CLKSEL1_TMR2SEL_LIRC  (0x5UL << NUMICRO_CLK_CLKSEL1_TMR2SEL_Pos)
#define NUMICRO_CLK_CLKSEL1_TMR2SEL_HIRC  (0x7UL << NUMICRO_CLK_CLKSEL1_TMR2SEL_Pos)
#define NUMICRO_CLK_CLKSEL1_TMR2SEL_PCLK1 (0x2UL << NUMICRO_CLK_CLKSEL1_TMR2SEL_Pos)
#define NUMICRO_CLK_CLKSEL1_TMR2SEL_EXT   (0x3UL << NUMICRO_CLK_CLKSEL1_TMR2SEL_Pos)

#define NUMICRO_CLK_CLKSEL1_TMR3SEL_HXT   (0x0UL << NUMICRO_CLK_CLKSEL1_TMR3SEL_Pos)
#define NUMICRO_CLK_CLKSEL1_TMR3SEL_LXT   (0x1UL << NUMICRO_CLK_CLKSEL1_TMR3SEL_Pos)
#define NUMICRO_CLK_CLKSEL1_TMR3SEL_LIRC  (0x5UL << NUMICRO_CLK_CLKSEL1_TMR3SEL_Pos)
#define NUMICRO_CLK_CLKSEL1_TMR3SEL_HIRC  (0x7UL << NUMICRO_CLK_CLKSEL1_TMR3SEL_Pos)
#define NUMICRO_CLK_CLKSEL1_TMR3SEL_PCLK1 (0x2UL << NUMICRO_CLK_CLKSEL1_TMR3SEL_Pos)
#define NUMICRO_CLK_CLKSEL1_TMR3SEL_EXT   (0x3UL << NUMICRO_CLK_CLKSEL1_TMR3SEL_Pos)

#define NUMICRO_CLK_CLKSEL1_UART0SEL_HXT  (0x0UL << NUMICRO_CLK_CLKSEL1_UART0SEL_Pos)
#define NUMICRO_CLK_CLKSEL1_UART0SEL_LXT  (0x2UL << NUMICRO_CLK_CLKSEL1_UART0SEL_Pos)
#define NUMICRO_CLK_CLKSEL1_UART0SEL_PLL  (0x1UL << NUMICRO_CLK_CLKSEL1_UART0SEL_Pos)
#define NUMICRO_CLK_CLKSEL1_UART0SEL_HIRC (0x3UL << NUMICRO_CLK_CLKSEL1_UART0SEL_Pos)

#define NUMICRO_CLK_CLKSEL1_UART1SEL_HXT  (0x0UL << NUMICRO_CLK_CLKSEL1_UART1SEL_Pos)
#define NUMICRO_CLK_CLKSEL1_UART1SEL_LXT  (0x2UL << NUMICRO_CLK_CLKSEL1_UART1SEL_Pos)
#define NUMICRO_CLK_CLKSEL1_UART1SEL_PLL  (0x1UL << NUMICRO_CLK_CLKSEL1_UART1SEL_Pos)
#define NUMICRO_CLK_CLKSEL1_UART1SEL_HIRC (0x3UL << NUMICRO_CLK_CLKSEL1_UART1SEL_Pos)

#define NUMICRO_CLK_CLKSEL1_CLKOSEL_HXT  (0x0UL << NUMICRO_CLK_CLKSEL1_CLKOSEL_Pos)
#define NUMICRO_CLK_CLKSEL1_CLKOSEL_LXT  (0x1UL << NUMICRO_CLK_CLKSEL1_CLKOSEL_Pos)
#define NUMICRO_CLK_CLKSEL1_CLKOSEL_HIRC (0x3UL << NUMICRO_CLK_CLKSEL1_CLKOSEL_Pos)
#define NUMICRO_CLK_CLKSEL1_CLKOSEL_HCLK (0x2UL << NUMICRO_CLK_CLKSEL1_CLKOSEL_Pos)

#define NUMICRO_CLK_CLKSEL1_WWDTSEL_LIRC         (0x3UL << NUMICRO_CLK_CLKSEL1_WWDTSEL_Pos)
#define NUMICRO_CLK_CLKSEL1_WWDTSEL_HCLK_DIV2048 (0x2UL << NUMICRO_CLK_CLKSEL1_WWDTSEL_Pos)

/*------------------------------------------------------------------------------------------------*/
/*  CLKSEL2 constant definitions. */
/*------------------------------------------------------------------------------------------------*/
#define NUMICRO_CLK_CLKSEL2_QSPI0SEL_HXT   (0x0UL << NUMICRO_CLK_CLKSEL2_QSPI0SEL_Pos)
#define NUMICRO_CLK_CLKSEL2_QSPI0SEL_PLL   (0x1UL << NUMICRO_CLK_CLKSEL2_QSPI0SEL_Pos)
#define NUMICRO_CLK_CLKSEL2_QSPI0SEL_HIRC  (0x3UL << NUMICRO_CLK_CLKSEL2_QSPI0SEL_Pos)
#define NUMICRO_CLK_CLKSEL2_QSPI0SEL_PCLK0 (0x2UL << NUMICRO_CLK_CLKSEL2_QSPI0SEL_Pos)

#define NUMICRO_CLK_CLKSEL2_SPI0SEL_HXT   (0x0UL << NUMICRO_CLK_CLKSEL2_SPI0SEL_Pos)
#define NUMICRO_CLK_CLKSEL2_SPI0SEL_PLL   (0x1UL << NUMICRO_CLK_CLKSEL2_SPI0SEL_Pos)
#define NUMICRO_CLK_CLKSEL2_SPI0SEL_HIRC  (0x3UL << NUMICRO_CLK_CLKSEL2_SPI0SEL_Pos)
#define NUMICRO_CLK_CLKSEL2_SPI0SEL_PCLK1 (0x2UL << NUMICRO_CLK_CLKSEL2_SPI0SEL_Pos)

#define NUMICRO_CLK_CLKSEL2_SPI1SEL_HXT   (0x0UL << NUMICRO_CLK_CLKSEL2_SPI1SEL_Pos)
#define NUMICRO_CLK_CLKSEL2_SPI1SEL_PLL   (0x1UL << NUMICRO_CLK_CLKSEL2_SPI1SEL_Pos)
#define NUMICRO_CLK_CLKSEL2_SPI1SEL_HIRC  (0x3UL << NUMICRO_CLK_CLKSEL2_SPI1SEL_Pos)
#define NUMICRO_CLK_CLKSEL2_SPI1SEL_PCLK0 (0x2UL << NUMICRO_CLK_CLKSEL2_SPI1SEL_Pos)

#define NUMICRO_CLK_CLKSEL2_EPWM0SEL_PLL   (0x0UL << NUMICRO_CLK_CLKSEL2_EPWM0SEL_Pos)
#define NUMICRO_CLK_CLKSEL2_EPWM0SEL_PCLK0 (0x1UL << NUMICRO_CLK_CLKSEL2_EPWM0SEL_Pos)

#define NUMICRO_CLK_CLKSEL2_EPWM1SEL_PLL   (0x0UL << NUMICRO_CLK_CLKSEL2_EPWM1SEL_Pos)
#define NUMICRO_CLK_CLKSEL2_EPWM1SEL_PCLK1 (0x1UL << NUMICRO_CLK_CLKSEL2_EPWM1SEL_Pos)

#define NUMICRO_CLK_CLKSEL2_BPWM0SEL_PLL   (0x0UL << NUMICRO_CLK_CLKSEL2_BPWM0SEL_Pos)
#define NUMICRO_CLK_CLKSEL2_BPWM0SEL_PCLK0 (0x1UL << NUMICRO_CLK_CLKSEL2_BPWM0SEL_Pos)

#define NUMICRO_CLK_CLKSEL2_BPWM1SEL_PLL   (0x0UL << NUMICRO_CLK_CLKSEL2_BPWM1SEL_Pos)
#define NUMICRO_CLK_CLKSEL2_BPWM1SEL_PCLK1 (0x1UL << NUMICRO_CLK_CLKSEL2_BPWM1SEL_Pos)

#define NUMICRO_CLK_CLKSEL2_SPI2SEL_HXT   (0x0UL << NUMICRO_CLK_CLKSEL2_SPI2SEL_Pos)
#define NUMICRO_CLK_CLKSEL2_SPI2SEL_PLL   (0x1UL << NUMICRO_CLK_CLKSEL2_SPI2SEL_Pos)
#define NUMICRO_CLK_CLKSEL2_SPI2SEL_HIRC  (0x3UL << NUMICRO_CLK_CLKSEL2_SPI2SEL_Pos)
#define NUMICRO_CLK_CLKSEL2_SPI2SEL_PCLK1 (0x2UL << NUMICRO_CLK_CLKSEL2_SPI2SEL_Pos)

#define NUMICRO_CLK_CLKSEL2_SPI3SEL_HXT   (0x0UL << NUMICRO_CLK_CLKSEL2_SPI3SEL_Pos)
#define NUMICRO_CLK_CLKSEL2_SPI3SEL_PLL   (0x1UL << NUMICRO_CLK_CLKSEL2_SPI3SEL_Pos)
#define NUMICRO_CLK_CLKSEL2_SPI3SEL_HIRC  (0x3UL << NUMICRO_CLK_CLKSEL2_SPI3SEL_Pos)
#define NUMICRO_CLK_CLKSEL2_SPI3SEL_PCLK0 (0x2UL << NUMICRO_CLK_CLKSEL2_SPI3SEL_Pos)

/*------------------------------------------------------------------------------------------------*/
/*  CLKSEL3 constant definitions. */
/*------------------------------------------------------------------------------------------------*/
#define NUMICRO_CLK_CLKSEL3_SC0SEL_HXT   (0x0UL << NUMICRO_CLK_CLKSEL3_SC0SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_SC0SEL_PLL   (0x1UL << NUMICRO_CLK_CLKSEL3_SC0SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_SC0SEL_HIRC  (0x3UL << NUMICRO_CLK_CLKSEL3_SC0SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_SC0SEL_PCLK0 (0x2UL << NUMICRO_CLK_CLKSEL3_SC0SEL_Pos)

#define NUMICRO_CLK_CLKSEL3_SC1SEL_HXT   (0x0UL << NUMICRO_CLK_CLKSEL3_SC1SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_SC1SEL_PLL   (0x1UL << NUMICRO_CLK_CLKSEL3_SC1SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_SC1SEL_HIRC  (0x3UL << NUMICRO_CLK_CLKSEL3_SC1SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_SC1SEL_PCLK1 (0x2UL << NUMICRO_CLK_CLKSEL3_SC1SEL_Pos)

#define NUMICRO_CLK_CLKSEL3_SC2SEL_HXT   (0x0UL << NUMICRO_CLK_CLKSEL3_SC2SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_SC2SEL_PLL   (0x1UL << NUMICRO_CLK_CLKSEL3_SC2SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_SC2SEL_HIRC  (0x3UL << NUMICRO_CLK_CLKSEL3_SC2SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_SC2SEL_PCLK0 (0x2UL << NUMICRO_CLK_CLKSEL3_SC2SEL_Pos)

#define NUMICRO_CLK_CLKSEL3_RTCSEL_LXT  (0x0UL << NUMICRO_CLK_CLKSEL3_RTCSEL_Pos)
#define NUMICRO_CLK_CLKSEL3_RTCSEL_LIRC (0x1UL << NUMICRO_CLK_CLKSEL3_RTCSEL_Pos)

#define NUMICRO_CLK_CLKSEL3_QSPI1SEL_HXT   (0x0UL << NUMICRO_CLK_CLKSEL3_QSPI1SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_QSPI1SEL_PLL   (0x1UL << NUMICRO_CLK_CLKSEL3_QSPI1SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_QSPI1SEL_HIRC  (0x3UL << NUMICRO_CLK_CLKSEL3_QSPI1SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_QSPI1SEL_PCLK1 (0x2UL << NUMICRO_CLK_CLKSEL3_QSPI1SEL_Pos)

#define NUMICRO_CLK_CLKSEL3_I2S0SEL_HXT   (0x0UL << NUMICRO_CLK_CLKSEL3_I2S0SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_I2S0SEL_PLL   (0x1UL << NUMICRO_CLK_CLKSEL3_I2S0SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_I2S0SEL_HIRC  (0x3UL << NUMICRO_CLK_CLKSEL3_I2S0SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_I2S0SEL_PCLK0 (0x2UL << NUMICRO_CLK_CLKSEL3_I2S0SEL_Pos)

#define NUMICRO_CLK_CLKSEL3_UART2SEL_HXT  (0x0UL << NUMICRO_CLK_CLKSEL3_UART2SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_UART2SEL_LXT  (0x2UL << NUMICRO_CLK_CLKSEL3_UART2SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_UART2SEL_PLL  (0x1UL << NUMICRO_CLK_CLKSEL3_UART2SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_UART2SEL_HIRC (0x3UL << NUMICRO_CLK_CLKSEL3_UART2SEL_Pos)

#define NUMICRO_CLK_CLKSEL3_UART3SEL_HXT  (0x0UL << NUMICRO_CLK_CLKSEL3_UART3SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_UART3SEL_LXT  (0x2UL << NUMICRO_CLK_CLKSEL3_UART3SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_UART3SEL_PLL  (0x1UL << NUMICRO_CLK_CLKSEL3_UART3SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_UART3SEL_HIRC (0x3UL << NUMICRO_CLK_CLKSEL3_UART3SEL_Pos)

#define NUMICRO_CLK_CLKSEL3_UART4SEL_HXT  (0x0UL << NUMICRO_CLK_CLKSEL3_UART4SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_UART4SEL_LXT  (0x2UL << NUMICRO_CLK_CLKSEL3_UART4SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_UART4SEL_PLL  (0x1UL << NUMICRO_CLK_CLKSEL3_UART4SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_UART4SEL_HIRC (0x3UL << NUMICRO_CLK_CLKSEL3_UART4SEL_Pos)

#define NUMICRO_CLK_CLKSEL3_UART5SEL_HXT  (0x0UL << NUMICRO_CLK_CLKSEL3_UART5SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_UART5SEL_LXT  (0x2UL << NUMICRO_CLK_CLKSEL3_UART5SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_UART5SEL_PLL  (0x1UL << NUMICRO_CLK_CLKSEL3_UART5SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_UART5SEL_HIRC (0x3UL << NUMICRO_CLK_CLKSEL3_UART5SEL_Pos)

#define NUMICRO_CLK_CLKSEL3_UART6SEL_HXT  (0x0UL << NUMICRO_CLK_CLKSEL3_UART6SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_UART6SEL_LXT  (0x2UL << NUMICRO_CLK_CLKSEL3_UART6SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_UART6SEL_PLL  (0x1UL << NUMICRO_CLK_CLKSEL3_UART6SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_UART6SEL_HIRC (0x3UL << NUMICRO_CLK_CLKSEL3_UART6SEL_Pos)

#define NUMICRO_CLK_CLKSEL3_UART7SEL_HXT  (0x0UL << NUMICRO_CLK_CLKSEL3_UART7SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_UART7SEL_LXT  (0x2UL << NUMICRO_CLK_CLKSEL3_UART7SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_UART7SEL_PLL  (0x1UL << NUMICRO_CLK_CLKSEL3_UART7SEL_Pos)
#define NUMICRO_CLK_CLKSEL3_UART7SEL_HIRC (0x3UL << NUMICRO_CLK_CLKSEL3_UART7SEL_Pos)



/*------------------------------------------------------------------------------------------------*/
/*  CLKDIV0 constant definitions. */
/*------------------------------------------------------------------------------------------------*/
#define NUMICRO_CLK_CLKDIV0_HCLK(x)  (((x) - 1UL) << NUMICRO_CLK_CLKDIV0_HCLKDIV_Pos)
#define NUMICRO_CLK_CLKDIV0_USB(x)   (((x) - 1UL) << NUMICRO_CLK_CLKDIV0_USBDIV_Pos)
#define NUMICRO_CLK_CLKDIV0_SDH0(x)  (((x) - 1UL) << NUMICRO_CLK_CLKDIV0_SDH0DIV_Pos)
#define NUMICRO_CLK_CLKDIV0_UART0(x) (((x) - 1UL) << NUMICRO_CLK_CLKDIV0_UART0DIV_Pos)
#define NUMICRO_CLK_CLKDIV0_UART1(x) (((x) - 1UL) << NUMICRO_CLK_CLKDIV0_UART1DIV_Pos)
#define NUMICRO_CLK_CLKDIV0_EADC(x)  (((x) - 1UL) << NUMICRO_CLK_CLKDIV0_EADCDIV_Pos)

/*------------------------------------------------------------------------------------------------*/
/*  CLKDIV1 constant definitions. */
/*------------------------------------------------------------------------------------------------*/
#define NUMICRO_CLK_CLKDIV1_SC0(x) (((x) - 1UL) << NUMICRO_CLK_CLKDIV1_SC0DIV_Pos)
#define NUMICRO_CLK_CLKDIV1_SC1(x) (((x) - 1UL) << NUMICRO_CLK_CLKDIV1_SC1DIV_Pos)
#define NUMICRO_CLK_CLKDIV1_SC2(x) (((x) - 1UL) << NUMICRO_CLK_CLKDIV1_SC2DIV_Pos)

/*------------------------------------------------------------------------------------------------*/
/*  CLKDIV2 constant definitions. */
/*------------------------------------------------------------------------------------------------*/
#define NUMICRO_CLK_CLKDIV2_I2S0(x)  (((x) - 1UL) << NUMICRO_CLK_CLKDIV2_I2SDIV_Pos)
#define NUMICRO_CLK_CLKDIV2_EADC1(x) (((x) - 1UL) << NUMICRO_CLK_CLKDIV2_EADC1DIV_Pos)

/*------------------------------------------------------------------------------------------------*/
/*  CLKDIV3 constant definitions. */
/*------------------------------------------------------------------------------------------------*/
#define NUMICRO_CLK_CLKDIV3_CCAP(x)   (((x) - 1UL) << NUMICRO_CLK_CLKDIV3_CCAPDIV_Pos)
#define NUMICRO_CLK_CLKDIV3_VSENSE(x) (((x) - 1UL) << NUMICRO_CLK_CLKDIV3_VSENSEDIV_Pos)
#define NUMICRO_CLK_CLKDIV3_EMAC(x)   (((x) - 1UL) << NUMICRO_CLK_CLKDIV3_EMACDIV_Pos)
#define NUMICRO_CLK_CLKDIV3_SDH1(x)   (((x) - 1UL) << NUMICRO_CLK_CLKDIV3_SDH1DIV_Pos)

/*------------------------------------------------------------------------------------------------*/
/*  CLKDIV4 constant definitions. */
/*------------------------------------------------------------------------------------------------*/
#define NUMICRO_CLK_CLKDIV4_UART2(x) (((x) - 1UL) << NUMICRO_CLK_CLKDIV4_UART2DIV_Pos)
#define NUMICRO_CLK_CLKDIV4_UART3(x) (((x) - 1UL) << NUMICRO_CLK_CLKDIV4_UART3DIV_Pos)
#define NUMICRO_CLK_CLKDIV4_UART4(x) (((x) - 1UL) << NUMICRO_CLK_CLKDIV4_UART4DIV_Pos)
#define NUMICRO_CLK_CLKDIV4_UART5(x) (((x) - 1UL) << NUMICRO_CLK_CLKDIV4_UART5DIV_Pos)
#define NUMICRO_CLK_CLKDIV4_UART6(x) (((x) - 1UL) << NUMICRO_CLK_CLKDIV4_UART6DIV_Pos)
#define NUMICRO_CLK_CLKDIV4_UART7(x) (((x) - 1UL) << NUMICRO_CLK_CLKDIV4_UART7DIV_Pos)



/*------------------------------------------------------------------------------------------------*/
/*  MODULE constant definitions. */
/*------------------------------------------------------------------------------------------------*/

/* APBCLK(31:30)|CLKSEL(29:28)|CLKSEL_Msk(27:25)
 * |CLKSEL_Pos(24:20)|CLKDIV(19:18)|CLKDIV_Msk(17:10)|CLKDIV_Pos(9:5)|IP_EN_Pos(4:0)
 */

#define NUMICRO_MODULE_APBCLK(x)     (((x) >> 30) & 0x3UL)
#define NUMICRO_MODULE_CLKSEL(x)     (((x) >> 28) & 0x3UL)
#define NUMICRO_MODULE_CLKSEL_Msk(x) (((x) >> 25) & 0x7UL)
#define NUMICRO_MODULE_CLKSEL_Pos(x) (((x) >> 20) & 0x1fUL)
#define NUMICRO_MODULE_CLKDIV(x)     (((x) >> 18) & 0x3UL)
#define NUMICRO_MODULE_CLKDIV_Msk(x) (((x) >> 10) & 0xffUL)
#define NUMICRO_MODULE_CLKDIV_Pos(x) (((x) >> 5) & 0x1fUL)
#define NUMICRO_MODULE_IP_EN_Pos(x)  (((x) >> 0) & 0x1fUL)
#define NUMICRO_MODULE_NoMsk         0x0UL
#define NUMICRO_NA                   NUMICRO_MODULE_NoMsk

#define NUMICRO_MODULE_APBCLK_ENC(x)     (((x) & 0x03UL) << 30)
#define NUMICRO_MODULE_CLKSEL_ENC(x)     (((x) & 0x03UL) << 28)
#define NUMICRO_MODULE_CLKSEL_Msk_ENC(x) (((x) & 0x07UL) << 25)
#define NUMICRO_MODULE_CLKSEL_Pos_ENC(x) (((x) & 0x1fUL) << 20)
#define NUMICRO_MODULE_CLKDIV_ENC(x)     (((x) & 0x03UL) << 18)
#define NUMICRO_MODULE_CLKDIV_Msk_ENC(x) (((x) & 0xffUL) << 10)
#define NUMICRO_MODULE_CLKDIV_Pos_ENC(x) (((x) & 0x1fUL) << 5)
#define NUMICRO_MODULE_IP_EN_Pos_ENC(x)  (((x) & 0x1fUL) << 0)

#define NUMICRO_MODULE_CLKSEL_VALUE_Msk 0x03
#define NUMICRO_MODULE_CLKDIV_VALUE_Msk 0x0F

#define NUMICRO_PDMA_MODULE                                                                        \
        ((0UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (NUMICRO_MODULE_NoMsk << 18) |                             \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (1UL << 0))
#define NUMICRO_ISP_MODULE                                                                         \
        ((0UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (NUMICRO_MODULE_NoMsk << 18) |                             \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (2UL << 0))
#define NUMICRO_EBI_MODULE                                                                         \
        ((0UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (NUMICRO_MODULE_NoMsk << 18) |                             \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (3UL << 0))
#define NUMICRO_USBH_MODULE                                                                        \
        ((0UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (NUMICRO_MODULE_NoMsk << 18) |                             \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (16UL << 0))
#define NUMICRO_EMAC_MODULE                                                                        \
        ((0UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (2UL << 18) | (0xFFUL << 10) | (16UL << 5) | (5UL << 0))
#define NUMICRO_SDH0_MODULE                                                                        \
        ((0UL << 30) | (0UL << 28) | (0x3UL << 25) | (20UL << 20) | (0UL << 18) | (0xFFUL << 10) | \
         (24UL << 5) | (6UL << 0))
#define NUMICRO_CRC_MODULE                                                                         \
        ((0UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (NUMICRO_MODULE_NoMsk << 18) |                             \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (7UL << 0))
#define NUMICRO_CCAP_MODULE                                                                        \
        ((0UL << 30) | (0UL << 28) | (0x3UL << 25) | (16UL << 20) | (2UL << 18) | (0xFFUL << 10) | \
         (0UL << 5) | (8UL << 0))
#define NUMICRO_SEN_MODULE                                                                         \
        ((0UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (NUMICRO_MODULE_NoMsk << 18) |                             \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (9UL << 0))
#define NUMICRO_HSUSBD_MODULE                                                                      \
        ((0UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (NUMICRO_MODULE_NoMsk << 18) |                             \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (10UL << 0))
#define NUMICRO_CRPT_MODULE                                                                        \
        ((0UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (NUMICRO_MODULE_NoMsk << 18) |                             \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (12UL << 0))
#define NUMICRO_SPIM_MODULE                                                                        \
        ((0UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (NUMICRO_MODULE_NoMsk << 18) |                             \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (14UL << 0))
#define NUMICRO_FMCIDLE_MODULE                                                                     \
        ((0UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (NUMICRO_MODULE_NoMsk << 18) |                             \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (15UL << 0))
#define NUMICRO_SDH1_MODULE                                                                        \
        ((0UL << 30) | (0UL << 28) | (0x3UL << 25) | (22UL << 20) | (2UL << 18) | (0xFFUL << 10) | \
         (24UL << 5) | (17UL << 0))
#define NUMICRO_WDT_MODULE                                                                         \
        ((1UL << 30) | (1UL << 28) | (0x3UL << 25) | (0UL << 20) | (NUMICRO_MODULE_NoMsk << 18) |  \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (0UL << 0))
#define NUMICRO_RTC_MODULE                                                                         \
        ((1UL << 30) | (3UL << 28) | (0x1UL << 25) | (8UL << 20) | (NUMICRO_MODULE_NoMsk << 18) |  \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (1UL << 0))
#define NUMICRO_TMR0_MODULE                                                                        \
        ((1UL << 30) | (1UL << 28) | (0x7UL << 25) | (8UL << 20) | (NUMICRO_MODULE_NoMsk << 18) |  \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (2UL << 0))
#define NUMICRO_TMR1_MODULE                                                                        \
        ((1UL << 30) | (1UL << 28) | (0x7UL << 25) | (12UL << 20) | (NUMICRO_MODULE_NoMsk << 18) | \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (3UL << 0))
#define NUMICRO_TMR2_MODULE                                                                        \
        ((1UL << 30) | (1UL << 28) | (0x7UL << 25) | (16UL << 20) | (NUMICRO_MODULE_NoMsk << 18) | \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (4UL << 0))
#define NUMICRO_TMR3_MODULE                                                                        \
        ((1UL << 30) | (1UL << 28) | (0x7UL << 25) | (20UL << 20) | (NUMICRO_MODULE_NoMsk << 18) | \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (5UL << 0))
#define NUMICRO_CLKO_MODULE                                                                        \
        ((1UL << 30) | (1UL << 28) | (0x3UL << 25) | (28UL << 20) | (NUMICRO_MODULE_NoMsk << 18) | \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (6UL << 0))
#define NUMICRO_WWDT_MODULE                                                                        \
        ((1UL << 30) | (1UL << 28) | (0x3UL << 25) | (30UL << 20) | (NUMICRO_MODULE_NoMsk << 18) | \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (0UL << 0))
#define NUMICRO_ACMP01_MODULE                                                                      \
        ((1UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (NUMICRO_MODULE_NoMsk << 18) |                             \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (7UL << 0))
#define NUMICRO_I2C0_MODULE                                                                        \
        ((1UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (NUMICRO_MODULE_NoMsk << 18) |                             \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (8UL << 0))
#define NUMICRO_I2C1_MODULE                                                                        \
        ((1UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (NUMICRO_MODULE_NoMsk << 18) |                             \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (9UL << 0))
#define NUMICRO_I2C2_MODULE                                                                        \
        ((1UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (NUMICRO_MODULE_NoMsk << 18) |                             \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (10UL << 0))
#define NUMICRO_QSPI0_MODULE                                                                       \
        ((1UL << 30) | (2UL << 28) | (0x3UL << 25) | (2UL << 20) | (NUMICRO_MODULE_NoMsk << 18) |  \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (12UL << 0))
#define NUMICRO_SPI0_MODULE                                                                        \
        ((1UL << 30) | (2UL << 28) | (0x3UL << 25) | (4UL << 20) | (NUMICRO_MODULE_NoMsk << 18) |  \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (13UL << 0))
#define NUMICRO_SPI1_MODULE                                                                        \
        ((1UL << 30) | (2UL << 28) | (0x3UL << 25) | (6UL << 20) | (NUMICRO_MODULE_NoMsk << 18) |  \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (14UL << 0))
#define NUMICRO_SPI2_MODULE                                                                        \
        ((1UL << 30) | (2UL << 28) | (0x3UL << 25) | (10UL << 20) | (NUMICRO_MODULE_NoMsk << 18) | \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (15UL << 0))
#define NUMICRO_UART0_MODULE                                                                       \
        ((1UL << 30) | (1UL << 28) | (0x3UL << 25) | (24UL << 20) | (0UL << 18) | (0xFUL << 10) |  \
         (8UL << 5) | (16UL << 0))
#define NUMICRO_UART1_MODULE                                                                       \
        ((1UL << 30) | (1UL << 28) | (0x3UL << 25) | (26UL << 20) | (0UL << 18) | (0xFUL << 10) |  \
         (12UL << 5) | (17UL << 0))
#define NUMICRO_UART2_MODULE                                                                       \
        ((1UL << 30) | (3UL << 28) | (0x3UL << 25) | (24UL << 20) | (3UL << 18) | (0xFUL << 10) |  \
         (0UL << 5) | (18UL << 0))
#define NUMICRO_UART3_MODULE                                                                       \
        ((1UL << 30) | (3UL << 28) | (0x3UL << 25) | (26UL << 20) | (3UL << 18) | (0xFUL << 10) |  \
         (4UL << 5) | (19UL << 0))
#define NUMICRO_UART4_MODULE                                                                       \
        ((1UL << 30) | (3UL << 28) | (0x3UL << 25) | (28UL << 20) | (3UL << 18) | (0xFUL << 10) |  \
         (8UL << 5) | (20UL << 0))
#define NUMICRO_UART5_MODULE                                                                       \
        ((1UL << 30) | (3UL << 28) | (0x3UL << 25) | (30UL << 20) | (3UL << 18) | (0xFUL << 10) |  \
         (12UL << 5) | (21UL << 0))
#define NUMICRO_UART6_MODULE                                                                       \
        ((1UL << 30) | (3UL << 28) | (0x3UL << 25) | (20UL << 20) | (3UL << 18) | (0xFUL << 10) |  \
         (16UL << 5) | (22UL << 0))
#define NUMICRO_UART7_MODULE                                                                       \
        ((1UL << 30) | (3UL << 28) | (0x3UL << 25) | (22UL << 20) | (3UL << 18) | (0xFUL << 10) |  \
         (20UL << 5) | (23UL << 0))
#define NUMICRO_CAN0_MODULE                                                                        \
        ((1UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (NUMICRO_MODULE_NoMsk << 18) |                             \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (24UL << 0))
#define NUMICRO_CAN1_MODULE                                                                        \
        ((1UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (NUMICRO_MODULE_NoMsk << 18) |                             \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (25UL << 0))
#define NUMICRO_OTG_MODULE                                                                         \
        ((1UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (NUMICRO_MODULE_NoMsk << 18) |                             \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (26UL << 0))
#define NUMICRO_USBD_MODULE                                                                        \
        ((1UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (NUMICRO_MODULE_NoMsk << 18) |                             \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (27UL << 0))
#define NUMICRO_EADC_MODULE                                                                        \
        ((1UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (0UL << 18) | (0xFFUL << 10) | (16UL << 5) | (28UL << 0))
#define NUMICRO_I2S0_MODULE                                                                        \
        ((1UL << 30) | (3UL << 28) | (0x3UL << 25) | (16UL << 20) | (2UL << 18) | (0xFUL << 10) |  \
         (0UL << 5) | (29UL << 0))
#define NUMICRO_HSOTG_MODULE                                                                       \
        ((1UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (NUMICRO_MODULE_NoMsk << 18) |                             \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (30UL << 0))
#define NUMICRO_SC0_MODULE                                                                         \
        ((2UL << 30) | (3UL << 28) | (0x3UL << 25) | (0UL << 20) | (1UL << 18) | (0xFFUL << 10) |  \
         (0UL << 5) | (0UL << 0))
#define NUMICRO_SC1_MODULE                                                                         \
        ((2UL << 30) | (3UL << 28) | (0x3UL << 25) | (2UL << 20) | (1UL << 18) | (0xFFUL << 10) |  \
         (8UL << 5) | (1UL << 0))
#define NUMICRO_SC2_MODULE                                                                         \
        ((2UL << 30) | (3UL << 28) | (0x3UL << 25) | (4UL << 20) | (1UL << 18) | (0xFFUL << 10) |  \
         (16UL << 5) | (2UL << 0))
#define NUMICRO_QSPI1_MODULE                                                                       \
        ((2UL << 30) | (3UL << 28) | (0x3UL << 25) | (12UL << 20) | (NUMICRO_MODULE_NoMsk << 18) | \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (4UL << 0))
#define NUMICRO_SPI3_MODULE                                                                        \
        ((2UL << 30) | (2UL << 28) | (0x3UL << 25) | (12UL << 20) | (NUMICRO_MODULE_NoMsk << 18) | \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (6UL << 0))
#define NUMICRO_USCI0_MODULE                                                                       \
        ((2UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (NUMICRO_MODULE_NoMsk << 18) |                             \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (8UL << 0))
#define NUMICRO_USCI1_MODULE                                                                       \
        ((2UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (NUMICRO_MODULE_NoMsk << 18) |                             \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (9UL << 0))
#define NUMICRO_DAC_MODULE                                                                         \
        ((2UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (NUMICRO_MODULE_NoMsk << 18) |                             \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (12UL << 0))
#define NUMICRO_CAN2_MODULE                                                                        \
        ((2UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (NUMICRO_MODULE_NoMsk << 18) |                             \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (28UL << 0))
#define NUMICRO_EPWM0_MODULE                                                                       \
        ((2UL << 30) | (2UL << 28) | (0x1UL << 25) | (0UL << 20) | (NUMICRO_MODULE_NoMsk << 18) |  \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (16UL << 0))
#define NUMICRO_EPWM1_MODULE                                                                       \
        ((2UL << 30) | (2UL << 28) | (0x1UL << 25) | (1UL << 20) | (NUMICRO_MODULE_NoMsk << 18) |  \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (17UL << 0))
#define NUMICRO_BPWM0_MODULE                                                                       \
        ((2UL << 30) | (2UL << 28) | (0x1UL << 25) | (8UL << 20) | (NUMICRO_MODULE_NoMsk << 18) |  \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (18UL << 0))
#define NUMICRO_BPWM1_MODULE                                                                       \
        ((2UL << 30) | (2UL << 28) | (0x1UL << 25) | (9UL << 20) | (NUMICRO_MODULE_NoMsk << 18) |  \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (19UL << 0))
#define NUMICRO_QEI0_MODULE                                                                        \
        ((2UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (NUMICRO_MODULE_NoMsk << 18) |                             \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (22UL << 0))
#define NUMICRO_QEI1_MODULE                                                                        \
        ((2UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (NUMICRO_MODULE_NoMsk << 18) |                             \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (23UL << 0))
#define NUMICRO_TRNG_MODULE                                                                        \
        ((2UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (NUMICRO_MODULE_NoMsk << 18) |                             \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (25UL << 0))
#define NUMICRO_ECAP0_MODULE                                                                       \
        ((2UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (NUMICRO_MODULE_NoMsk << 18) |                             \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (26UL << 0))
#define NUMICRO_ECAP1_MODULE                                                                       \
        ((2UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (NUMICRO_MODULE_NoMsk << 18) |                             \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (27UL << 0))
#define NUMICRO_OPA_MODULE                                                                         \
        ((2UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (NUMICRO_MODULE_NoMsk << 18) |                             \
         (NUMICRO_MODULE_NoMsk << 10) | (NUMICRO_MODULE_NoMsk << 5) | (30UL << 0))
#define NUMICRO_EADC1_MODULE                                                                       \
        ((2UL << 30) | (NUMICRO_MODULE_NoMsk << 28) | (NUMICRO_MODULE_NoMsk << 25) |               \
         (NUMICRO_MODULE_NoMsk << 20) | (2UL << 18) | (0xFFUL << 10) | (24UL << 5) | (31UL << 0))


/* End of M480 BSP clk.h copy */


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_NUMICRO_M48X_CLOCK_H_ */
```

## 8.2\_可见注释译文（Comments）

### 注释 1：原第 7 行

版权（Copyright）：© 2026 Fiona Behrens。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 28 行

M480 板级支持包（BSP）`clk_reg.h` 复制内容开始。

### 注释 3：原第 184 行

M480 板级支持包（BSP）`clk_reg.h` 复制内容结束。

### 注释 4：原第 186 行

M480 板级支持包（BSP）`clk.h` 复制内容开始。

### 注释 5：原第 193 行

分隔线。

### 注释 6：原第 194 行

`CLKSEL0` 常量定义，具有写保护（write-protection）。

### 注释 7：原第 195 行

分隔线。

### 注释 8：原第 212 行

分隔线。

### 注释 9：原第 213 行

`CLKSEL1` 常量定义。

### 注释 10：原第 214 行

分隔线。

### 注释 11：原第 265 行

分隔线。

### 注释 12：原第 266 行

`CLKSEL2` 常量定义。

### 注释 13：原第 267 行

分隔线。

### 注释 14：原第 305 行

分隔线。

### 注释 15：原第 306 行

`CLKSEL3` 常量定义。

### 注释 16：原第 307 行

分隔线。

### 注释 17：原第 373 行

分隔线。

### 注释 18：原第 374 行

`CLKDIV0` 常量定义。

### 注释 19：原第 375 行

分隔线。

### 注释 20：原第 383 行

分隔线。

### 注释 21：原第 384 行

`CLKDIV1` 常量定义。

### 注释 22：原第 385 行

分隔线。

### 注释 23：原第 390 行

分隔线。

### 注释 24：原第 391 行

`CLKDIV2` 常量定义。

### 注释 25：原第 392 行

分隔线。

### 注释 26：原第 396 行

分隔线。

### 注释 27：原第 397 行

`CLKDIV3` 常量定义。

### 注释 28：原第 398 行

分隔线。

### 注释 29：原第 404 行

分隔线。

### 注释 30：原第 405 行

`CLKDIV4` 常量定义。

### 注释 31：原第 406 行

分隔线。

### 注释 32：原第 421 行

分隔线。

### 注释 33：原第 422 行

`MODULE` 常量定义。

### 注释 34：原第 423 行

分隔线。

### 注释 35：原第 425 行

模块标识的位域布局（bit-field layout）：`APBCLK(31:30) | CLKSEL(29:28) | CLKSEL_Msk(27:25) | CLKSEL_Pos(24:20) | CLKDIV(19:18) | CLKDIV_Msk(17:10) | CLKDIV_Pos(9:5) | IP_EN_Pos(4:0)`。

### 注释 36：原第 679 行

M480 板级支持包（BSP）`clk.h` 复制内容结束。

### 注释 37：原第 684 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_NUMICRO_M48X_CLOCK_H_`。

## 8.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P273_zephyr__dt-bindings__clock__numicro_m48x_clock.h_文件参考.md)

---

[上一章](P007_net_stats.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P009_pthread.h_源码浏览.md)
