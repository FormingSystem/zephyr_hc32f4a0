---
id: learning.zephyr-docs.api-source-reference.page-357
title: imx_scu_rsrc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/imx__scu__rsrc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第357章\_imx\_scu\_rsrc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/imx__scu__rsrc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/imx__scu__rsrc_8h.html)。

## 357.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
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
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
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

```c
/*
 * Copyright 2024 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_POWER_IMX_SCU_RSRC_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_POWER_IMX_SCU_RSRC_H_

#define IMX_SC_R_A53                  0U
#define IMX_SC_R_A53_0                1U
#define IMX_SC_R_A53_1                2U
#define IMX_SC_R_A53_2                3U
#define IMX_SC_R_A53_3                4U
#define IMX_SC_R_A72                  5U
#define IMX_SC_R_A72_0                6U
#define IMX_SC_R_A72_1                7U
#define IMX_SC_R_A72_2                8U
#define IMX_SC_R_A72_3                9U
#define IMX_SC_R_CCI                  10U
#define IMX_SC_R_DB                   11U
#define IMX_SC_R_DRC_0                12U
#define IMX_SC_R_DRC_1                13U
#define IMX_SC_R_GIC_SMMU             14U
#define IMX_SC_R_IRQSTR_M4_0          15U
#define IMX_SC_R_IRQSTR_M4_1          16U
#define IMX_SC_R_SMMU                 17U
#define IMX_SC_R_GIC                  18U
#define IMX_SC_R_DC_0_BLIT0           19U
#define IMX_SC_R_DC_0_BLIT1           20U
#define IMX_SC_R_DC_0_BLIT2           21U
#define IMX_SC_R_DC_0_BLIT_OUT        22U
#define IMX_SC_R_PERF                 23U
#define IMX_SC_R_USB_1_PHY            24U
#define IMX_SC_R_DC_0_WARP            25U
#define IMX_SC_R_V2X_MU_0             26U
#define IMX_SC_R_V2X_MU_1             27U
#define IMX_SC_R_DC_0_VIDEO0          28U
#define IMX_SC_R_DC_0_VIDEO1          29U
#define IMX_SC_R_DC_0_FRAC0           30U
#define IMX_SC_R_V2X_MU_2             31U
#define IMX_SC_R_DC_0                 32U
#define IMX_SC_R_GPU_2_PID0           33U
#define IMX_SC_R_DC_0_PLL_0           34U
#define IMX_SC_R_DC_0_PLL_1           35U
#define IMX_SC_R_DC_1_BLIT0           36U
#define IMX_SC_R_DC_1_BLIT1           37U
#define IMX_SC_R_DC_1_BLIT2           38U
#define IMX_SC_R_DC_1_BLIT_OUT        39U
#define IMX_SC_R_V2X_MU_3             40U
#define IMX_SC_R_V2X_MU_4             41U
#define IMX_SC_R_DC_1_WARP            42U
#define IMX_SC_R_UNUSED1              43U
#define IMX_SC_R_SECVIO               44U
#define IMX_SC_R_DC_1_VIDEO0          45U
#define IMX_SC_R_DC_1_VIDEO1          46U
#define IMX_SC_R_DC_1_FRAC0           47U
#define IMX_SC_R_UNUSED13             48U
#define IMX_SC_R_DC_1                 49U
#define IMX_SC_R_UNUSED14             50U
#define IMX_SC_R_DC_1_PLL_0           51U
#define IMX_SC_R_DC_1_PLL_1           52U
#define IMX_SC_R_SPI_0                53U
#define IMX_SC_R_SPI_1                54U
#define IMX_SC_R_SPI_2                55U
#define IMX_SC_R_SPI_3                56U
#define IMX_SC_R_UART_0               57U
#define IMX_SC_R_UART_1               58U
#define IMX_SC_R_UART_2               59U
#define IMX_SC_R_UART_3               60U
#define IMX_SC_R_UART_4               61U
#define IMX_SC_R_EMVSIM_0             62U
#define IMX_SC_R_EMVSIM_1             63U
#define IMX_SC_R_DMA_0_CH0            64U
#define IMX_SC_R_DMA_0_CH1            65U
#define IMX_SC_R_DMA_0_CH2            66U
#define IMX_SC_R_DMA_0_CH3            67U
#define IMX_SC_R_DMA_0_CH4            68U
#define IMX_SC_R_DMA_0_CH5            69U
#define IMX_SC_R_DMA_0_CH6            70U
#define IMX_SC_R_DMA_0_CH7            71U
#define IMX_SC_R_DMA_0_CH8            72U
#define IMX_SC_R_DMA_0_CH9            73U
#define IMX_SC_R_DMA_0_CH10           74U
#define IMX_SC_R_DMA_0_CH11           75U
#define IMX_SC_R_DMA_0_CH12           76U
#define IMX_SC_R_DMA_0_CH13           77U
#define IMX_SC_R_DMA_0_CH14           78U
#define IMX_SC_R_DMA_0_CH15           79U
#define IMX_SC_R_DMA_0_CH16           80U
#define IMX_SC_R_DMA_0_CH17           81U
#define IMX_SC_R_DMA_0_CH18           82U
#define IMX_SC_R_DMA_0_CH19           83U
#define IMX_SC_R_DMA_0_CH20           84U
#define IMX_SC_R_DMA_0_CH21           85U
#define IMX_SC_R_DMA_0_CH22           86U
#define IMX_SC_R_DMA_0_CH23           87U
#define IMX_SC_R_DMA_0_CH24           88U
#define IMX_SC_R_DMA_0_CH25           89U
#define IMX_SC_R_DMA_0_CH26           90U
#define IMX_SC_R_DMA_0_CH27           91U
#define IMX_SC_R_DMA_0_CH28           92U
#define IMX_SC_R_DMA_0_CH29           93U
#define IMX_SC_R_DMA_0_CH30           94U
#define IMX_SC_R_DMA_0_CH31           95U
#define IMX_SC_R_I2C_0                96U
#define IMX_SC_R_I2C_1                97U
#define IMX_SC_R_I2C_2                98U
#define IMX_SC_R_I2C_3                99U
#define IMX_SC_R_I2C_4                100U
#define IMX_SC_R_ADC_0                101U
#define IMX_SC_R_ADC_1                102U
#define IMX_SC_R_FTM_0                103U
#define IMX_SC_R_FTM_1                104U
#define IMX_SC_R_CAN_0                105U
#define IMX_SC_R_CAN_1                106U
#define IMX_SC_R_CAN_2                107U
#define IMX_SC_R_DMA_1_CH0            108U
#define IMX_SC_R_DMA_1_CH1            109U
#define IMX_SC_R_DMA_1_CH2            110U
#define IMX_SC_R_DMA_1_CH3            111U
#define IMX_SC_R_DMA_1_CH4            112U
#define IMX_SC_R_DMA_1_CH5            113U
#define IMX_SC_R_DMA_1_CH6            114U
#define IMX_SC_R_DMA_1_CH7            115U
#define IMX_SC_R_DMA_1_CH8            116U
#define IMX_SC_R_DMA_1_CH9            117U
#define IMX_SC_R_DMA_1_CH10           118U
#define IMX_SC_R_DMA_1_CH11           119U
#define IMX_SC_R_DMA_1_CH12           120U
#define IMX_SC_R_DMA_1_CH13           121U
#define IMX_SC_R_DMA_1_CH14           122U
#define IMX_SC_R_DMA_1_CH15           123U
#define IMX_SC_R_DMA_1_CH16           124U
#define IMX_SC_R_DMA_1_CH17           125U
#define IMX_SC_R_DMA_1_CH18           126U
#define IMX_SC_R_DMA_1_CH19           127U
#define IMX_SC_R_DMA_1_CH20           128U
#define IMX_SC_R_DMA_1_CH21           129U
#define IMX_SC_R_DMA_1_CH22           130U
#define IMX_SC_R_DMA_1_CH23           131U
#define IMX_SC_R_DMA_1_CH24           132U
#define IMX_SC_R_DMA_1_CH25           133U
#define IMX_SC_R_DMA_1_CH26           134U
#define IMX_SC_R_DMA_1_CH27           135U
#define IMX_SC_R_DMA_1_CH28           136U
#define IMX_SC_R_DMA_1_CH29           137U
#define IMX_SC_R_DMA_1_CH30           138U
#define IMX_SC_R_DMA_1_CH31           139U
#define IMX_SC_R_V2X_PID0             140U
#define IMX_SC_R_V2X_PID1             141U
#define IMX_SC_R_V2X_PID2             142U
#define IMX_SC_R_V2X_PID3             143U
#define IMX_SC_R_GPU_0_PID0           144U
#define IMX_SC_R_GPU_0_PID1           145U
#define IMX_SC_R_GPU_0_PID2           146U
#define IMX_SC_R_GPU_0_PID3           147U
#define IMX_SC_R_GPU_1_PID0           148U
#define IMX_SC_R_GPU_1_PID1           149U
#define IMX_SC_R_GPU_1_PID2           150U
#define IMX_SC_R_GPU_1_PID3           151U
#define IMX_SC_R_PCIE_A               152U
#define IMX_SC_R_SERDES_0             153U
#define IMX_SC_R_MATCH_0              154U
#define IMX_SC_R_MATCH_1              155U
#define IMX_SC_R_MATCH_2              156U
#define IMX_SC_R_MATCH_3              157U
#define IMX_SC_R_MATCH_4              158U
#define IMX_SC_R_MATCH_5              159U
#define IMX_SC_R_MATCH_6              160U
#define IMX_SC_R_MATCH_7              161U
#define IMX_SC_R_MATCH_8              162U
#define IMX_SC_R_MATCH_9              163U
#define IMX_SC_R_MATCH_10             164U
#define IMX_SC_R_MATCH_11             165U
#define IMX_SC_R_MATCH_12             166U
#define IMX_SC_R_MATCH_13             167U
#define IMX_SC_R_MATCH_14             168U
#define IMX_SC_R_PCIE_B               169U
#define IMX_SC_R_SATA_0               170U
#define IMX_SC_R_SERDES_1             171U
#define IMX_SC_R_HSIO_GPIO            172U
#define IMX_SC_R_MATCH_15             173U
#define IMX_SC_R_MATCH_16             174U
#define IMX_SC_R_MATCH_17             175U
#define IMX_SC_R_MATCH_18             176U
#define IMX_SC_R_MATCH_19             177U
#define IMX_SC_R_MATCH_20             178U
#define IMX_SC_R_MATCH_21             179U
#define IMX_SC_R_MATCH_22             180U
#define IMX_SC_R_MATCH_23             181U
#define IMX_SC_R_MATCH_24             182U
#define IMX_SC_R_MATCH_25             183U
#define IMX_SC_R_MATCH_26             184U
#define IMX_SC_R_MATCH_27             185U
#define IMX_SC_R_MATCH_28             186U
#define IMX_SC_R_LCD_0                187U
#define IMX_SC_R_LCD_0_PWM_0          188U
#define IMX_SC_R_LCD_0_I2C_0          189U
#define IMX_SC_R_LCD_0_I2C_1          190U
#define IMX_SC_R_PWM_0                191U
#define IMX_SC_R_PWM_1                192U
#define IMX_SC_R_PWM_2                193U
#define IMX_SC_R_PWM_3                194U
#define IMX_SC_R_PWM_4                195U
#define IMX_SC_R_PWM_5                196U
#define IMX_SC_R_PWM_6                197U
#define IMX_SC_R_PWM_7                198U
#define IMX_SC_R_GPIO_0               199U
#define IMX_SC_R_GPIO_1               200U
#define IMX_SC_R_GPIO_2               201U
#define IMX_SC_R_GPIO_3               202U
#define IMX_SC_R_GPIO_4               203U
#define IMX_SC_R_GPIO_5               204U
#define IMX_SC_R_GPIO_6               205U
#define IMX_SC_R_GPIO_7               206U
#define IMX_SC_R_GPT_0                207U
#define IMX_SC_R_GPT_1                208U
#define IMX_SC_R_GPT_2                209U
#define IMX_SC_R_GPT_3                210U
#define IMX_SC_R_GPT_4                211U
#define IMX_SC_R_KPP                  212U
#define IMX_SC_R_MU_0A                213U
#define IMX_SC_R_MU_1A                214U
#define IMX_SC_R_MU_2A                215U
#define IMX_SC_R_MU_3A                216U
#define IMX_SC_R_MU_4A                217U
#define IMX_SC_R_MU_5A                218U
#define IMX_SC_R_MU_6A                219U
#define IMX_SC_R_MU_7A                220U
#define IMX_SC_R_MU_8A                221U
#define IMX_SC_R_MU_9A                222U
#define IMX_SC_R_MU_10A               223U
#define IMX_SC_R_MU_11A               224U
#define IMX_SC_R_MU_12A               225U
#define IMX_SC_R_MU_13A               226U
#define IMX_SC_R_MU_5B                227U
#define IMX_SC_R_MU_6B                228U
#define IMX_SC_R_MU_7B                229U
#define IMX_SC_R_MU_8B                230U
#define IMX_SC_R_MU_9B                231U
#define IMX_SC_R_MU_10B               232U
#define IMX_SC_R_MU_11B               233U
#define IMX_SC_R_MU_12B               234U
#define IMX_SC_R_MU_13B               235U
#define IMX_SC_R_ROM_0                236U
#define IMX_SC_R_FSPI_0               237U
#define IMX_SC_R_FSPI_1               238U
#define IMX_SC_R_IEE                  239U
#define IMX_SC_R_IEE_R0               240U
#define IMX_SC_R_IEE_R1               241U
#define IMX_SC_R_IEE_R2               242U
#define IMX_SC_R_IEE_R3               243U
#define IMX_SC_R_IEE_R4               244U
#define IMX_SC_R_IEE_R5               245U
#define IMX_SC_R_IEE_R6               246U
#define IMX_SC_R_IEE_R7               247U
#define IMX_SC_R_SDHC_0               248U
#define IMX_SC_R_SDHC_1               249U
#define IMX_SC_R_SDHC_2               250U
#define IMX_SC_R_ENET_0               251U
#define IMX_SC_R_ENET_1               252U
#define IMX_SC_R_MLB_0                253U
#define IMX_SC_R_DMA_2_CH0            254U
#define IMX_SC_R_DMA_2_CH1            255U
#define IMX_SC_R_DMA_2_CH2            256U
#define IMX_SC_R_DMA_2_CH3            257U
#define IMX_SC_R_DMA_2_CH4            258U
#define IMX_SC_R_USB_0                259U
#define IMX_SC_R_USB_1                260U
#define IMX_SC_R_USB_0_PHY            261U
#define IMX_SC_R_USB_2                262U
#define IMX_SC_R_USB_2_PHY            263U
#define IMX_SC_R_DTCP                 264U
#define IMX_SC_R_NAND                 265U
#define IMX_SC_R_LVDS_0               266U
#define IMX_SC_R_LVDS_0_PWM_0         267U
#define IMX_SC_R_LVDS_0_I2C_0         268U
#define IMX_SC_R_LVDS_0_I2C_1         269U
#define IMX_SC_R_LVDS_1               270U
#define IMX_SC_R_LVDS_1_PWM_0         271U
#define IMX_SC_R_LVDS_1_I2C_0         272U
#define IMX_SC_R_LVDS_1_I2C_1         273U
#define IMX_SC_R_LVDS_2               274U
#define IMX_SC_R_LVDS_2_PWM_0         275U
#define IMX_SC_R_LVDS_2_I2C_0         276U
#define IMX_SC_R_LVDS_2_I2C_1         277U
#define IMX_SC_R_M4_0_PID0            278U
#define IMX_SC_R_M4_0_PID1            279U
#define IMX_SC_R_M4_0_PID2            280U
#define IMX_SC_R_M4_0_PID3            281U
#define IMX_SC_R_M4_0_PID4            282U
#define IMX_SC_R_M4_0_RGPIO           283U
#define IMX_SC_R_M4_0_SEMA42          284U
#define IMX_SC_R_M4_0_TPM             285U
#define IMX_SC_R_M4_0_PIT             286U
#define IMX_SC_R_M4_0_UART            287U
#define IMX_SC_R_M4_0_I2C             288U
#define IMX_SC_R_M4_0_INTMUX          289U
#define IMX_SC_R_ENET_0_A0            290U
#define IMX_SC_R_ENET_0_A1            291U
#define IMX_SC_R_M4_0_MU_0B           292U
#define IMX_SC_R_M4_0_MU_0A0          293U
#define IMX_SC_R_M4_0_MU_0A1          294U
#define IMX_SC_R_M4_0_MU_0A2          295U
#define IMX_SC_R_M4_0_MU_0A3          296U
#define IMX_SC_R_M4_0_MU_1A           297U
#define IMX_SC_R_M4_1_PID0            298U
#define IMX_SC_R_M4_1_PID1            299U
#define IMX_SC_R_M4_1_PID2            300U
#define IMX_SC_R_M4_1_PID3            301U
#define IMX_SC_R_M4_1_PID4            302U
#define IMX_SC_R_M4_1_RGPIO           303U
#define IMX_SC_R_M4_1_SEMA42          304U
#define IMX_SC_R_M4_1_TPM             305U
#define IMX_SC_R_M4_1_PIT             306U
#define IMX_SC_R_M4_1_UART            307U
#define IMX_SC_R_M4_1_I2C             308U
#define IMX_SC_R_M4_1_INTMUX          309U
#define IMX_SC_R_UNUSED17             310U
#define IMX_SC_R_UNUSED18             311U
#define IMX_SC_R_M4_1_MU_0B           312U
#define IMX_SC_R_M4_1_MU_0A0          313U
#define IMX_SC_R_M4_1_MU_0A1          314U
#define IMX_SC_R_M4_1_MU_0A2          315U
#define IMX_SC_R_M4_1_MU_0A3          316U
#define IMX_SC_R_M4_1_MU_1A           317U
#define IMX_SC_R_SAI_0                318U
#define IMX_SC_R_SAI_1                319U
#define IMX_SC_R_SAI_2                320U
#define IMX_SC_R_IRQSTR_SCU2          321U
#define IMX_SC_R_IRQSTR_DSP           322U
#define IMX_SC_R_ELCDIF_PLL           323U
#define IMX_SC_R_OCRAM                324U
#define IMX_SC_R_AUDIO_PLL_0          325U
#define IMX_SC_R_PI_0                 326U
#define IMX_SC_R_PI_0_PWM_0           327U
#define IMX_SC_R_PI_0_PWM_1           328U
#define IMX_SC_R_PI_0_I2C_0           329U
#define IMX_SC_R_PI_0_PLL             330U
#define IMX_SC_R_PI_1                 331U
#define IMX_SC_R_PI_1_PWM_0           332U
#define IMX_SC_R_PI_1_PWM_1           333U
#define IMX_SC_R_PI_1_I2C_0           334U
#define IMX_SC_R_PI_1_PLL             335U
#define IMX_SC_R_SC_PID0              336U
#define IMX_SC_R_SC_PID1              337U
#define IMX_SC_R_SC_PID2              338U
#define IMX_SC_R_SC_PID3              339U
#define IMX_SC_R_SC_PID4              340U
#define IMX_SC_R_SC_SEMA42            341U
#define IMX_SC_R_SC_TPM               342U
#define IMX_SC_R_SC_PIT               343U
#define IMX_SC_R_SC_UART              344U
#define IMX_SC_R_SC_I2C               345U
#define IMX_SC_R_SC_MU_0B             346U
#define IMX_SC_R_SC_MU_0A0            347U
#define IMX_SC_R_SC_MU_0A1            348U
#define IMX_SC_R_SC_MU_0A2            349U
#define IMX_SC_R_SC_MU_0A3            350U
#define IMX_SC_R_SC_MU_1A             351U
#define IMX_SC_R_SYSCNT_RD            352U
#define IMX_SC_R_SYSCNT_CMP           353U
#define IMX_SC_R_DEBUG                354U
#define IMX_SC_R_SYSTEM               355U
#define IMX_SC_R_SNVS                 356U
#define IMX_SC_R_OTP                  357U
#define IMX_SC_R_VPU_PID0             358U
#define IMX_SC_R_VPU_PID1             359U
#define IMX_SC_R_VPU_PID2             360U
#define IMX_SC_R_VPU_PID3             361U
#define IMX_SC_R_VPU_PID4             362U
#define IMX_SC_R_VPU_PID5             363U
#define IMX_SC_R_VPU_PID6             364U
#define IMX_SC_R_VPU_PID7             365U
#define IMX_SC_R_ENET_0_A2            366U
#define IMX_SC_R_ENET_1_A0            367U
#define IMX_SC_R_ENET_1_A1            368U
#define IMX_SC_R_ENET_1_A2            369U
#define IMX_SC_R_ENET_1_A3            370U
#define IMX_SC_R_ENET_1_A4            371U
#define IMX_SC_R_DMA_4_CH0            372U
#define IMX_SC_R_DMA_4_CH1            373U
#define IMX_SC_R_DMA_4_CH2            374U
#define IMX_SC_R_DMA_4_CH3            375U
#define IMX_SC_R_DMA_4_CH4            376U
#define IMX_SC_R_ISI_CH0              377U
#define IMX_SC_R_ISI_CH1              378U
#define IMX_SC_R_ISI_CH2              379U
#define IMX_SC_R_ISI_CH3              380U
#define IMX_SC_R_ISI_CH4              381U
#define IMX_SC_R_ISI_CH5              382U
#define IMX_SC_R_ISI_CH6              383U
#define IMX_SC_R_ISI_CH7              384U
#define IMX_SC_R_MJPEG_DEC_S0         385U
#define IMX_SC_R_MJPEG_DEC_S1         386U
#define IMX_SC_R_MJPEG_DEC_S2         387U
#define IMX_SC_R_MJPEG_DEC_S3         388U
#define IMX_SC_R_MJPEG_ENC_S0         389U
#define IMX_SC_R_MJPEG_ENC_S1         390U
#define IMX_SC_R_MJPEG_ENC_S2         391U
#define IMX_SC_R_MJPEG_ENC_S3         392U
#define IMX_SC_R_MIPI_0               393U
#define IMX_SC_R_MIPI_0_PWM_0         394U
#define IMX_SC_R_MIPI_0_I2C_0         395U
#define IMX_SC_R_MIPI_0_I2C_1         396U
#define IMX_SC_R_MIPI_1               397U
#define IMX_SC_R_MIPI_1_PWM_0         398U
#define IMX_SC_R_MIPI_1_I2C_0         399U
#define IMX_SC_R_MIPI_1_I2C_1         400U
#define IMX_SC_R_CSI_0                401U
#define IMX_SC_R_CSI_0_PWM_0          402U
#define IMX_SC_R_CSI_0_I2C_0          403U
#define IMX_SC_R_CSI_1                404U
#define IMX_SC_R_CSI_1_PWM_0          405U
#define IMX_SC_R_CSI_1_I2C_0          406U
#define IMX_SC_R_HDMI                 407U
#define IMX_SC_R_HDMI_I2S             408U
#define IMX_SC_R_HDMI_I2C_0           409U
#define IMX_SC_R_HDMI_PLL_0           410U
#define IMX_SC_R_HDMI_RX              411U
#define IMX_SC_R_HDMI_RX_BYPASS       412U
#define IMX_SC_R_HDMI_RX_I2C_0        413U
#define IMX_SC_R_ASRC_0               414U
#define IMX_SC_R_ESAI_0               415U
#define IMX_SC_R_SPDIF_0              416U
#define IMX_SC_R_SPDIF_1              417U
#define IMX_SC_R_SAI_3                418U
#define IMX_SC_R_SAI_4                419U
#define IMX_SC_R_SAI_5                420U
#define IMX_SC_R_GPT_5                421U
#define IMX_SC_R_GPT_6                422U
#define IMX_SC_R_GPT_7                423U
#define IMX_SC_R_GPT_8                424U
#define IMX_SC_R_GPT_9                425U
#define IMX_SC_R_GPT_10               426U
#define IMX_SC_R_DMA_2_CH5            427U
#define IMX_SC_R_DMA_2_CH6            428U
#define IMX_SC_R_DMA_2_CH7            429U
#define IMX_SC_R_DMA_2_CH8            430U
#define IMX_SC_R_DMA_2_CH9            431U
#define IMX_SC_R_DMA_2_CH10           432U
#define IMX_SC_R_DMA_2_CH11           433U
#define IMX_SC_R_DMA_2_CH12           434U
#define IMX_SC_R_DMA_2_CH13           435U
#define IMX_SC_R_DMA_2_CH14           436U
#define IMX_SC_R_DMA_2_CH15           437U
#define IMX_SC_R_DMA_2_CH16           438U
#define IMX_SC_R_DMA_2_CH17           439U
#define IMX_SC_R_DMA_2_CH18           440U
#define IMX_SC_R_DMA_2_CH19           441U
#define IMX_SC_R_DMA_2_CH20           442U
#define IMX_SC_R_DMA_2_CH21           443U
#define IMX_SC_R_DMA_2_CH22           444U
#define IMX_SC_R_DMA_2_CH23           445U
#define IMX_SC_R_DMA_2_CH24           446U
#define IMX_SC_R_DMA_2_CH25           447U
#define IMX_SC_R_DMA_2_CH26           448U
#define IMX_SC_R_DMA_2_CH27           449U
#define IMX_SC_R_DMA_2_CH28           450U
#define IMX_SC_R_DMA_2_CH29           451U
#define IMX_SC_R_DMA_2_CH30           452U
#define IMX_SC_R_DMA_2_CH31           453U
#define IMX_SC_R_ASRC_1               454U
#define IMX_SC_R_ESAI_1               455U
#define IMX_SC_R_SAI_6                456U
#define IMX_SC_R_SAI_7                457U
#define IMX_SC_R_AMIX                 458U
#define IMX_SC_R_MQS_0                459U
#define IMX_SC_R_DMA_3_CH0            460U
#define IMX_SC_R_DMA_3_CH1            461U
#define IMX_SC_R_DMA_3_CH2            462U
#define IMX_SC_R_DMA_3_CH3            463U
#define IMX_SC_R_DMA_3_CH4            464U
#define IMX_SC_R_DMA_3_CH5            465U
#define IMX_SC_R_DMA_3_CH6            466U
#define IMX_SC_R_DMA_3_CH7            467U
#define IMX_SC_R_DMA_3_CH8            468U
#define IMX_SC_R_DMA_3_CH9            469U
#define IMX_SC_R_DMA_3_CH10           470U
#define IMX_SC_R_DMA_3_CH11           471U
#define IMX_SC_R_DMA_3_CH12           472U
#define IMX_SC_R_DMA_3_CH13           473U
#define IMX_SC_R_DMA_3_CH14           474U
#define IMX_SC_R_DMA_3_CH15           475U
#define IMX_SC_R_DMA_3_CH16           476U
#define IMX_SC_R_DMA_3_CH17           477U
#define IMX_SC_R_DMA_3_CH18           478U
#define IMX_SC_R_DMA_3_CH19           479U
#define IMX_SC_R_DMA_3_CH20           480U
#define IMX_SC_R_DMA_3_CH21           481U
#define IMX_SC_R_DMA_3_CH22           482U
#define IMX_SC_R_DMA_3_CH23           483U
#define IMX_SC_R_DMA_3_CH24           484U
#define IMX_SC_R_DMA_3_CH25           485U
#define IMX_SC_R_DMA_3_CH26           486U
#define IMX_SC_R_DMA_3_CH27           487U
#define IMX_SC_R_DMA_3_CH28           488U
#define IMX_SC_R_DMA_3_CH29           489U
#define IMX_SC_R_DMA_3_CH30           490U
#define IMX_SC_R_DMA_3_CH31           491U
#define IMX_SC_R_AUDIO_PLL_1          492U
#define IMX_SC_R_AUDIO_CLK_0          493U
#define IMX_SC_R_AUDIO_CLK_1          494U
#define IMX_SC_R_MCLK_OUT_0           495U
#define IMX_SC_R_MCLK_OUT_1           496U
#define IMX_SC_R_PMIC_0               497U
#define IMX_SC_R_PMIC_1               498U
#define IMX_SC_R_SECO                 499U
#define IMX_SC_R_CAAM_JR1             500U
#define IMX_SC_R_CAAM_JR2             501U
#define IMX_SC_R_CAAM_JR3             502U
#define IMX_SC_R_SECO_MU_2            503U
#define IMX_SC_R_SECO_MU_3            504U
#define IMX_SC_R_SECO_MU_4            505U
#define IMX_SC_R_HDMI_RX_PWM_0        506U
#define IMX_SC_R_A35                  507U
#define IMX_SC_R_A35_0                508U
#define IMX_SC_R_A35_1                509U
#define IMX_SC_R_A35_2                510U
#define IMX_SC_R_A35_3                511U
#define IMX_SC_R_DSP                  512U
#define IMX_SC_R_DSP_RAM              513U
#define IMX_SC_R_CAAM_JR1_OUT         514U
#define IMX_SC_R_CAAM_JR2_OUT         515U
#define IMX_SC_R_CAAM_JR3_OUT         516U
#define IMX_SC_R_VPU_DEC_0            517U
#define IMX_SC_R_VPU_ENC_0            518U
#define IMX_SC_R_CAAM_JR0             519U
#define IMX_SC_R_CAAM_JR0_OUT         520U
#define IMX_SC_R_PMIC_2               521U
#define IMX_SC_R_DBLOGIC              522U
#define IMX_SC_R_HDMI_PLL_1           523U
#define IMX_SC_R_BOARD_R0             524U
#define IMX_SC_R_BOARD_R1             525U
#define IMX_SC_R_BOARD_R2             526U
#define IMX_SC_R_BOARD_R3             527U
#define IMX_SC_R_BOARD_R4             528U
#define IMX_SC_R_BOARD_R5             529U
#define IMX_SC_R_BOARD_R6             530U
#define IMX_SC_R_BOARD_R7             531U
#define IMX_SC_R_MJPEG_DEC_MP         532U
#define IMX_SC_R_MJPEG_ENC_MP         533U
#define IMX_SC_R_VPU_TS_0             534U
#define IMX_SC_R_VPU_MU_0             535U
#define IMX_SC_R_VPU_MU_1             536U
#define IMX_SC_R_VPU_MU_2             537U
#define IMX_SC_R_VPU_MU_3             538U
#define IMX_SC_R_VPU_ENC_1            539U
#define IMX_SC_R_VPU                  540U
#define IMX_SC_R_DMA_5_CH0            541U
#define IMX_SC_R_DMA_5_CH1            542U
#define IMX_SC_R_DMA_5_CH2            543U
#define IMX_SC_R_DMA_5_CH3            544U
#define IMX_SC_R_ATTESTATION          545U
#define IMX_SC_R_LAST                 546U

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_POWER_IMX_SCU_RSRC_H_ */
```

## 357.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2024 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 558 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_POWER_IMX_SCU_RSRC_H_`。

## 357.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/imx__scu__rsrc_8h.html)

---

[上一章](P356_imx_rdc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P358_in.h_源码浏览.md)
