---
id: learning.zephyr-docs.api-source-reference.page-25
title: ambiq-apollo3-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ambiq-apollo3-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_ambiq-apollo3-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ambiq-apollo3-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ambiq-apollo3-pinctrl_8h.html)。

## 25.1\_原始可见代码（Source Code）

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
<a id="l00538"></a>
<a id="l00540"></a>
<a id="l00541"></a>

```c
/*
 * Copyright (c) 2023 Ambiq Micro Inc. <www.ambiq.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_AMBIQ_APOLLO3_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_AMBIQ_APOLLO3_PINCTRL_H_




#define APOLLO3_ALT_FUNC_POS  0
#define APOLLO3_ALT_FUNC_MASK 0xf

#define APOLLO3_PIN_NUM_POS  4
#define APOLLO3_PIN_NUM_MASK 0x7f

#define APOLLO3_PINMUX(pin_num, alt_func)                                                          \
        (pin_num << APOLLO3_PIN_NUM_POS | alt_func << APOLLO3_ALT_FUNC_POS)

#define SLSCL_P0         APOLLO3_PINMUX(0, 0)
#define SLSCK_P0         APOLLO3_PINMUX(0, 1)
#define CLKOUT_P0        APOLLO3_PINMUX(0, 2)
#define GPIO_P0          APOLLO3_PINMUX(0, 3)
#define MSPI0_4_P0       APOLLO3_PINMUX(0, 5)
#define NCE0_P0          APOLLO3_PINMUX(0, 7)
#define SLSDAWIR3_P1     APOLLO3_PINMUX(1, 0)
#define SLMOSI_P1        APOLLO3_PINMUX(1, 1)
#define UART0TX_P1       APOLLO3_PINMUX(1, 2)
#define GPIO_P1          APOLLO3_PINMUX(1, 3)
#define MSPI0_5_P1       APOLLO3_PINMUX(1, 5)
#define NCE1_P1          APOLLO3_PINMUX(1, 7)
#define UART1RX_P2       APOLLO3_PINMUX(2, 0)
#define SLMISO_P2        APOLLO3_PINMUX(2, 1)
#define UART0RX_P2       APOLLO3_PINMUX(2, 2)
#define GPIO_P2          APOLLO3_PINMUX(2, 3)
#define MSPI0_6_P2       APOLLO3_PINMUX(2, 5)
#define NCE2_P2          APOLLO3_PINMUX(2, 7)
#define UA0RTS_P3        APOLLO3_PINMUX(3, 0)
#define SLNCE_P3         APOLLO3_PINMUX(3, 1)
#define NCE3_P3          APOLLO3_PINMUX(3, 2)
#define GPIO_P3          APOLLO3_PINMUX(3, 3)
#define MSPI0_7_P3       APOLLO3_PINMUX(3, 5)
#define TRIG1_P3         APOLLO3_PINMUX(3, 6)
#define I2SWCLK_P3       APOLLO3_PINMUX(3, 7)
#define UA0CTS_P4        APOLLO3_PINMUX(4, 0)
#define SLINT_P4         APOLLO3_PINMUX(4, 1)
#define NCE4_P4          APOLLO3_PINMUX(4, 2)
#define GPIO_P4          APOLLO3_PINMUX(4, 3)
#define UART1RX_P4       APOLLO3_PINMUX(4, 5)
#define CTIM17_P4        APOLLO3_PINMUX(4, 6)
#define MSPI0_2_P4       APOLLO3_PINMUX(4, 7)
#define M0SCL_P5         APOLLO3_PINMUX(5, 0)
#define M0SCK_P5         APOLLO3_PINMUX(5, 1)
#define UA0RTS_P5        APOLLO3_PINMUX(5, 2)
#define GPIO_P5          APOLLO3_PINMUX(5, 3)
#define CT8_P5           APOLLO3_PINMUX(5, 7)
#define M0SDAWIR3_P6     APOLLO3_PINMUX(6, 0)
#define M0MISO_P6        APOLLO3_PINMUX(6, 1)
#define UA0CTS_P6        APOLLO3_PINMUX(6, 2)
#define GPIO_P6          APOLLO3_PINMUX(6, 3)
#define CTIM10_P6        APOLLO3_PINMUX(6, 5)
#define I2SDAT_P6        APOLLO3_PINMUX(6, 7)
#define NCE7_P7          APOLLO3_PINMUX(7, 0)
#define M0MOSI_P7        APOLLO3_PINMUX(7, 1)
#define CLKOUT_P7        APOLLO3_PINMUX(7, 2)
#define GPIO_P7          APOLLO3_PINMUX(7, 3)
#define TRIG0_P7         APOLLO3_PINMUX(7, 4)
#define UART0TX_P7       APOLLO3_PINMUX(7, 5)
#define CTIM19_P7        APOLLO3_PINMUX(7, 7)
#define M1SCL_P8         APOLLO3_PINMUX(8, 0)
#define M1SCK_P8         APOLLO3_PINMUX(8, 1)
#define NCE8_P8          APOLLO3_PINMUX(8, 2)
#define GPIO_P8          APOLLO3_PINMUX(8, 3)
#define SCCCLK_P8        APOLLO3_PINMUX(8, 4)
#define UART1TX_P8       APOLLO3_PINMUX(8, 6)
#define M1SDAWIR3_P9     APOLLO3_PINMUX(9, 0)
#define M1MISO_P9        APOLLO3_PINMUX(9, 1)
#define NCE9_P9          APOLLO3_PINMUX(9, 2)
#define GPIO_P9          APOLLO3_PINMUX(9, 3)
#define SCCIO_P9         APOLLO3_PINMUX(9, 4)
#define UART1RX_P9       APOLLO3_PINMUX(9, 6)
#define UART1TX_P10      APOLLO3_PINMUX(10, 0)
#define M1MOSI_P10       APOLLO3_PINMUX(10, 1)
#define NCE10_P10        APOLLO3_PINMUX(10, 2)
#define GPIO_P10         APOLLO3_PINMUX(10, 3)
#define PDMCLK_P10       APOLLO3_PINMUX(10, 4)
#define UA1RTS_P10       APOLLO3_PINMUX(10, 6)
#define ADCSE2_P11       APOLLO3_PINMUX(11, 0)
#define NCE11_P11        APOLLO3_PINMUX(11, 1)
#define CTIM31_P11       APOLLO3_PINMUX(11, 2)
#define GPIO_P11         APOLLO3_PINMUX(11, 3)
#define SLINT_P11        APOLLO3_PINMUX(11, 4)
#define UA1CTS_P11       APOLLO3_PINMUX(11, 5)
#define UART0RX_P11      APOLLO3_PINMUX(11, 6)
#define PDMDATA_P11      APOLLO3_PINMUX(11, 7)
#define ADCD0NSE9_P12    APOLLO3_PINMUX(12, 0)
#define NCE12_P12        APOLLO3_PINMUX(12, 1)
#define CT0_P12          APOLLO3_PINMUX(12, 2)
#define GPIO_P12         APOLLO3_PINMUX(12, 3)
#define PDMCLK_P12       APOLLO3_PINMUX(12, 5)
#define UA0CTS_P12       APOLLO3_PINMUX(12, 6)
#define UART1TX_P12      APOLLO3_PINMUX(12, 7)
#define ADCD0PSE8_P13    APOLLO3_PINMUX(13, 0)
#define NCE13_P13        APOLLO3_PINMUX(13, 1)
#define CTIM2_P13        APOLLO3_PINMUX(13, 2)
#define GPIO_P13         APOLLO3_PINMUX(13, 3)
#define I2SBCLK_P13      APOLLO3_PINMUX(13, 4)
#define UA0RTS_P13       APOLLO3_PINMUX(13, 6)
#define UART1RX_P13      APOLLO3_PINMUX(13, 7)
#define ADCD1P_P14       APOLLO3_PINMUX(14, 0)
#define NCE14_P14        APOLLO3_PINMUX(14, 1)
#define UART1TX_P14      APOLLO3_PINMUX(14, 2)
#define GPIO_P14         APOLLO3_PINMUX(14, 3)
#define PDMCLK_P14       APOLLO3_PINMUX(14, 4)
#define SWDCK_P14        APOLLO3_PINMUX(14, 6)
#define XT32KHz_P14      APOLLO3_PINMUX(14, 7)
#define ADCD1N_P15       APOLLO3_PINMUX(15, 0)
#define NCE15_P15        APOLLO3_PINMUX(15, 1)
#define UART1RX_P15      APOLLO3_PINMUX(15, 2)
#define GPIO_P15         APOLLO3_PINMUX(15, 3)
#define PDMDATA_P15      APOLLO3_PINMUX(15, 4)
#define SWDIO_P15        APOLLO3_PINMUX(15, 6)
#define SWO_P15          APOLLO3_PINMUX(15, 7)
#define ADCSE0_P16       APOLLO3_PINMUX(16, 0)
#define NCE16_P16        APOLLO3_PINMUX(16, 1)
#define TRIG0_P16        APOLLO3_PINMUX(16, 2)
#define GPIO_P16         APOLLO3_PINMUX(16, 3)
#define SCCRST_P16       APOLLO3_PINMUX(16, 4)
#define CMPIN0_P16       APOLLO3_PINMUX(16, 5)
#define UART0TX_P16      APOLLO3_PINMUX(16, 6)
#define UA1RTS_P16       APOLLO3_PINMUX(16, 7)
#define CMPRF1_P17       APOLLO3_PINMUX(17, 0)
#define NCE17_P17        APOLLO3_PINMUX(17, 1)
#define TRIG1_P17        APOLLO3_PINMUX(17, 2)
#define GPIO_P17         APOLLO3_PINMUX(17, 3)
#define SCCCLK_P17       APOLLO3_PINMUX(17, 4)
#define UART0RX_P17      APOLLO3_PINMUX(17, 6)
#define UA1CTS_P17       APOLLO3_PINMUX(17, 7)
#define CMPIN1_P18       APOLLO3_PINMUX(18, 0)
#define NCE18_P18        APOLLO3_PINMUX(18, 1)
#define CTIM4_P18        APOLLO3_PINMUX(18, 2)
#define GPIO_P18         APOLLO3_PINMUX(18, 3)
#define UA0RTS_P18       APOLLO3_PINMUX(18, 4)
#define UART1TX_P18      APOLLO3_PINMUX(18, 6)
#define SCCIO_P18        APOLLO3_PINMUX(18, 7)
#define CMPRF0_P19       APOLLO3_PINMUX(19, 0)
#define NCE19_P19        APOLLO3_PINMUX(19, 1)
#define CTIM6_P19        APOLLO3_PINMUX(19, 2)
#define GPIO_P19         APOLLO3_PINMUX(19, 3)
#define SCCCLK_P19       APOLLO3_PINMUX(19, 4)
#define UART1RX_P19      APOLLO3_PINMUX(19, 6)
#define I2SBCLK_P19      APOLLO3_PINMUX(19, 7)
#define SWDCK_P20        APOLLO3_PINMUX(20, 0)
#define NCE20_P20        APOLLO3_PINMUX(20, 1)
#define GPIO_P20         APOLLO3_PINMUX(20, 3)
#define UART0TX_P20      APOLLO3_PINMUX(20, 4)
#define UART1TX_P20      APOLLO3_PINMUX(20, 5)
#define I2SBCLK_P20      APOLLO3_PINMUX(20, 6)
#define UA1RTS_P20       APOLLO3_PINMUX(20, 7)
#define SWDIO_P21        APOLLO3_PINMUX(21, 0)
#define NCE21_P21        APOLLO3_PINMUX(21, 1)
#define GPIO_P21         APOLLO3_PINMUX(21, 3)
#define UART0RX_P21      APOLLO3_PINMUX(21, 4)
#define UART1RX_P21      APOLLO3_PINMUX(21, 5)
#define SCCRST_P21       APOLLO3_PINMUX(21, 6)
#define UA1CTS_P21       APOLLO3_PINMUX(21, 7)
#define UART0TX_P22      APOLLO3_PINMUX(22, 0)
#define NCE22_P22        APOLLO3_PINMUX(22, 1)
#define CTIM12_P22       APOLLO3_PINMUX(22, 2)
#define GPIO_P22         APOLLO3_PINMUX(22, 3)
#define PDMCLK_P22       APOLLO3_PINMUX(22, 4)
#define MSPI0_0_P22      APOLLO3_PINMUX(22, 6)
#define SWO_P22          APOLLO3_PINMUX(22, 7)
#define UART0RX_P23      APOLLO3_PINMUX(23, 0)
#define NCE23_P23        APOLLO3_PINMUX(23, 1)
#define CTIM14_P23       APOLLO3_PINMUX(23, 2)
#define GPIO_P23         APOLLO3_PINMUX(23, 3)
#define I2SWCLK_P23      APOLLO3_PINMUX(23, 4)
#define CMPOUT_P23       APOLLO3_PINMUX(23, 5)
#define MSPI0_3_P23      APOLLO3_PINMUX(23, 6)
#define UART1TX_P24      APOLLO3_PINMUX(24, 0)
#define NCE24_P24        APOLLO3_PINMUX(24, 1)
#define MSPI0_8_P24      APOLLO3_PINMUX(24, 2)
#define GPIO_P24         APOLLO3_PINMUX(24, 3)
#define UA0CTS_P24       APOLLO3_PINMUX(24, 4)
#define CTIM21_P24       APOLLO3_PINMUX(24, 5)
#define XT32KHz_P24      APOLLO3_PINMUX(24, 6)
#define SWO_P24          APOLLO3_PINMUX(24, 7)
#define UART1RX_P25      APOLLO3_PINMUX(25, 0)
#define NCE25_P25        APOLLO3_PINMUX(25, 1)
#define CTIM1_P25        APOLLO3_PINMUX(25, 2)
#define GPIO_P25         APOLLO3_PINMUX(25, 3)
#define M2SDAWIR3_P25    APOLLO3_PINMUX(25, 4)
#define M2MISO_P25       APOLLO3_PINMUX(25, 5)
#define NCE26_P26        APOLLO3_PINMUX(26, 1)
#define CTIM3_P26        APOLLO3_PINMUX(26, 2)
#define GPIO_P26         APOLLO3_PINMUX(26, 3)
#define SCCRST_P26       APOLLO3_PINMUX(26, 4)
#define MSPI0_1_P26      APOLLO3_PINMUX(26, 5)
#define UART0TX_P26      APOLLO3_PINMUX(26, 6)
#define UA1CTS_P26       APOLLO3_PINMUX(26, 7)
#define UART0RX_P27      APOLLO3_PINMUX(27, 0)
#define NCE27_P27        APOLLO3_PINMUX(27, 1)
#define CTIM5_P27        APOLLO3_PINMUX(27, 2)
#define GPIO_P27         APOLLO3_PINMUX(27, 3)
#define M2SCL_P27        APOLLO3_PINMUX(27, 4)
#define M2SCK_P27        APOLLO3_PINMUX(27, 5)
#define I2SWCLK_P28      APOLLO3_PINMUX(28, 0)
#define NCE28_P28        APOLLO3_PINMUX(28, 1)
#define CTIM7_P28        APOLLO3_PINMUX(28, 2)
#define GPIO_P28         APOLLO3_PINMUX(28, 3)
#define M2MOSI_P28       APOLLO3_PINMUX(28, 5)
#define UART0TX_P28      APOLLO3_PINMUX(28, 6)
#define ADCSE1_P29       APOLLO3_PINMUX(29, 0)
#define NCE29_P29        APOLLO3_PINMUX(29, 1)
#define CTIM9_P29        APOLLO3_PINMUX(29, 2)
#define GPIO_P29         APOLLO3_PINMUX(29, 3)
#define UA0CTS_P29       APOLLO3_PINMUX(29, 4)
#define UA1CTS_P29       APOLLO3_PINMUX(29, 5)
#define UART0RX_P29      APOLLO3_PINMUX(29, 6)
#define PDMDATA_P29      APOLLO3_PINMUX(29, 7)
#define NCE30_P30        APOLLO3_PINMUX(30, 1)
#define CTIM11_P30       APOLLO3_PINMUX(30, 2)
#define GPIO_P30         APOLLO3_PINMUX(30, 3)
#define UART0TX_P30      APOLLO3_PINMUX(30, 4)
#define UA1RTS_P30       APOLLO3_PINMUX(30, 5)
#define BLEIF_SCK_P30    APOLLO3_PINMUX(30, 6)
#define I2SDAT_P30       APOLLO3_PINMUX(30, 7)
#define ADCSE3_P31       APOLLO3_PINMUX(31, 0)
#define NCE31_P31        APOLLO3_PINMUX(31, 1)
#define CTIM13_P31       APOLLO3_PINMUX(31, 2)
#define GPIO_P31         APOLLO3_PINMUX(31, 3)
#define UART0RX_P31      APOLLO3_PINMUX(31, 4)
#define SCCCLK_P31       APOLLO3_PINMUX(31, 5)
#define BLEIF_MISO_P31   APOLLO3_PINMUX(31, 6)
#define UA1RTS_P31       APOLLO3_PINMUX(31, 7)
#define ADCSE4_P32       APOLLO3_PINMUX(32, 0)
#define NCE32_P32        APOLLO3_PINMUX(32, 1)
#define CTIM15_P32       APOLLO3_PINMUX(32, 2)
#define GPIO_P32         APOLLO3_PINMUX(32, 3)
#define SCCIO_P32        APOLLO3_PINMUX(32, 4)
#define BLEIF_MOSI_P32   APOLLO3_PINMUX(32, 6)
#define UA1CTS_P32       APOLLO3_PINMUX(32, 7)
#define ADCSE5_P33       APOLLO3_PINMUX(33, 0)
#define NCE33_P33        APOLLO3_PINMUX(33, 1)
#define XT32KHz_P33      APOLLO3_PINMUX(33, 2)
#define GPIO_P33         APOLLO3_PINMUX(33, 3)
#define BLEIF_CSN_P33    APOLLO3_PINMUX(33, 4)
#define UA0CTS_P33       APOLLO3_PINMUX(33, 5)
#define CTIM23_P33       APOLLO3_PINMUX(33, 6)
#define SWO_P33          APOLLO3_PINMUX(33, 7)
#define ADCSE6_P34       APOLLO3_PINMUX(34, 0)
#define NCE34_P34        APOLLO3_PINMUX(34, 1)
#define UA1RTS_P34       APOLLO3_PINMUX(34, 2)
#define GPIO_P34         APOLLO3_PINMUX(34, 3)
#define CMPRF2_P34       APOLLO3_PINMUX(34, 4)
#define UA0RTS_P34       APOLLO3_PINMUX(34, 5)
#define UART0RX_P34      APOLLO3_PINMUX(34, 6)
#define PDMDATA_P34      APOLLO3_PINMUX(34, 7)
#define ADCSE7_P35       APOLLO3_PINMUX(35, 0)
#define NCE35_P35        APOLLO3_PINMUX(35, 1)
#define UART1TX_P35      APOLLO3_PINMUX(35, 2)
#define GPIO_P35         APOLLO3_PINMUX(35, 3)
#define I2SDAT_P35       APOLLO3_PINMUX(35, 4)
#define CTIM27_P35       APOLLO3_PINMUX(35, 5)
#define UA0RTS_P35       APOLLO3_PINMUX(35, 6)
#define BLEIF_STATUS_P35 APOLLO3_PINMUX(35, 7)
#define TRIG1_P36        APOLLO3_PINMUX(36, 0)
#define NCE36_P36        APOLLO3_PINMUX(36, 1)
#define UART1RX_P36      APOLLO3_PINMUX(36, 2)
#define GPIO_P36         APOLLO3_PINMUX(36, 3)
#define XT32KHz_P36      APOLLO3_PINMUX(36, 4)
#define UA1CTS_P36       APOLLO3_PINMUX(36, 5)
#define UA0CTS_P36       APOLLO3_PINMUX(36, 6)
#define PDMDATA_P36      APOLLO3_PINMUX(36, 7)
#define TRIG2_P37        APOLLO3_PINMUX(37, 0)
#define NCE37_P37        APOLLO3_PINMUX(37, 1)
#define UA0RTS_P37       APOLLO3_PINMUX(37, 2)
#define GPIO_P37         APOLLO3_PINMUX(37, 3)
#define SCCIO_P37        APOLLO3_PINMUX(37, 4)
#define UART1TX_P37      APOLLO3_PINMUX(37, 5)
#define PDMCLK_P37       APOLLO3_PINMUX(37, 6)
#define CTIM29_P37       APOLLO3_PINMUX(37, 7)
#define TRIG3_P38        APOLLO3_PINMUX(38, 0)
#define NCE38_P38        APOLLO3_PINMUX(38, 1)
#define UA0CTS_P38       APOLLO3_PINMUX(38, 2)
#define GPIO_P38         APOLLO3_PINMUX(38, 3)
#define M3MOSI_P38       APOLLO3_PINMUX(38, 5)
#define UART1RX_P38      APOLLO3_PINMUX(38, 6)
#define UART0TX_P39      APOLLO3_PINMUX(39, 0)
#define UART1TX_P39      APOLLO3_PINMUX(39, 1)
#define CTIM25_P39       APOLLO3_PINMUX(39, 2)
#define GPIO_P39         APOLLO3_PINMUX(39, 3)
#define M4SCL_P39        APOLLO3_PINMUX(39, 4)
#define M4SCK_P39        APOLLO3_PINMUX(39, 5)
#define UART0RX_P40      APOLLO3_PINMUX(40, 0)
#define UART1RX_P40      APOLLO3_PINMUX(40, 1)
#define TRIG0_P40        APOLLO3_PINMUX(40, 2)
#define GPIO_P40         APOLLO3_PINMUX(40, 3)
#define M4SDAWIR3_P40    APOLLO3_PINMUX(40, 4)
#define M4MISO_P40       APOLLO3_PINMUX(40, 5)
#define NCE41_P41        APOLLO3_PINMUX(41, 0)
#define BLEIF_IRQ_P41    APOLLO3_PINMUX(41, 1)
#define SWO_P41          APOLLO3_PINMUX(41, 2)
#define GPIO_P41         APOLLO3_PINMUX(41, 3)
#define I2SWCLK_P41      APOLLO3_PINMUX(41, 4)
#define UA1RTS_P41       APOLLO3_PINMUX(41, 5)
#define UART0TX_P41      APOLLO3_PINMUX(41, 6)
#define UA0RTS_P41       APOLLO3_PINMUX(41, 7)
#define UART1TX_P42      APOLLO3_PINMUX(42, 0)
#define NCE42_P42        APOLLO3_PINMUX(42, 1)
#define CTIM16_P42       APOLLO3_PINMUX(42, 2)
#define GPIO_P42         APOLLO3_PINMUX(42, 3)
#define M3SCL_P42        APOLLO3_PINMUX(42, 4)
#define M3SCK_P42        APOLLO3_PINMUX(42, 5)
#define UART1RX_P43      APOLLO3_PINMUX(43, 0)
#define NCE43_P43        APOLLO3_PINMUX(43, 1)
#define CTIM18_P43       APOLLO3_PINMUX(43, 2)
#define GPIO_P43         APOLLO3_PINMUX(43, 3)
#define M3SDAWIR3_P43    APOLLO3_PINMUX(43, 4)
#define M3MISO_P43       APOLLO3_PINMUX(43, 5)
#define UA1RTS_P44       APOLLO3_PINMUX(44, 0)
#define NCE44_P44        APOLLO3_PINMUX(44, 1)
#define CTIM20_P44       APOLLO3_PINMUX(44, 2)
#define GPIO_P44         APOLLO3_PINMUX(44, 3)
#define M4MOSI_P44       APOLLO3_PINMUX(44, 5)
#define UART0TX_P44      APOLLO3_PINMUX(44, 6)
#define UA1CTS_P45       APOLLO3_PINMUX(45, 0)
#define NCE45_P45        APOLLO3_PINMUX(45, 1)
#define CTIM22_P45       APOLLO3_PINMUX(45, 2)
#define GPIO_P45         APOLLO3_PINMUX(45, 3)
#define I2SDAT_P45       APOLLO3_PINMUX(45, 4)
#define PDMDATA_P45      APOLLO3_PINMUX(45, 5)
#define UART0RX_P45      APOLLO3_PINMUX(45, 6)
#define SWO_P45          APOLLO3_PINMUX(45, 7)
#define I2SBCLK_P46      APOLLO3_PINMUX(46, 0)
#define NCE46_P46        APOLLO3_PINMUX(46, 1)
#define CTIM24_P46       APOLLO3_PINMUX(46, 2)
#define GPIO_P46         APOLLO3_PINMUX(46, 3)
#define SCCRST_P46       APOLLO3_PINMUX(46, 4)
#define PDMCLK_P46       APOLLO3_PINMUX(46, 5)
#define UART1TX_P46      APOLLO3_PINMUX(46, 6)
#define SWO_P46          APOLLO3_PINMUX(46, 7)
#define XT32KHz_P47      APOLLO3_PINMUX(47, 0)
#define NCE47_P47        APOLLO3_PINMUX(47, 1)
#define CTIM26_P47       APOLLO3_PINMUX(47, 2)
#define GPIO_P47         APOLLO3_PINMUX(47, 3)
#define M5MOSI_P47       APOLLO3_PINMUX(47, 5)
#define UART1RX_P47      APOLLO3_PINMUX(47, 6)
#define UART0TX_P48      APOLLO3_PINMUX(48, 0)
#define NCE48_P48        APOLLO3_PINMUX(48, 1)
#define CTIM28_P48       APOLLO3_PINMUX(48, 2)
#define GPIO_P48         APOLLO3_PINMUX(48, 3)
#define M5SCL_P48        APOLLO3_PINMUX(48, 4)
#define M5SCK_P48        APOLLO3_PINMUX(48, 5)
#define UART0RX_P49      APOLLO3_PINMUX(49, 0)
#define NCE49_P49        APOLLO3_PINMUX(49, 1)
#define CTIM30_P49       APOLLO3_PINMUX(49, 2)
#define GPIO_P49         APOLLO3_PINMUX(49, 3)
#define M5SDAWIR3_P49    APOLLO3_PINMUX(49, 4)
#define M5MISO_P49       APOLLO3_PINMUX(49, 5)
#define SWO_P50          APOLLO3_PINMUX(50, 0)
#define NCE50_P50        APOLLO3_PINMUX(50, 1)
#define CT0_P50          APOLLO3_PINMUX(50, 2)
#define GPIO_P50         APOLLO3_PINMUX(50, 3)
#define UART0TX_P50      APOLLO3_PINMUX(50, 4)
#define UART0RX_P50      APOLLO3_PINMUX(50, 5)
#define UART1TX_P50      APOLLO3_PINMUX(50, 6)
#define UART1RX_P50      APOLLO3_PINMUX(50, 7)
#define MSPI1_0_P51      APOLLO3_PINMUX(51, 0)
#define NCE51_P51        APOLLO3_PINMUX(51, 1)
#define CTIM1_P51        APOLLO3_PINMUX(51, 2)
#define GPIO_P51         APOLLO3_PINMUX(51, 3)
#define MSPI1_1_P52      APOLLO3_PINMUX(52, 0)
#define NCE52_P52        APOLLO3_PINMUX(52, 1)
#define CTIM2_P52        APOLLO3_PINMUX(52, 2)
#define GPIO_P52         APOLLO3_PINMUX(52, 3)
#define MSPI1_2_P53      APOLLO3_PINMUX(53, 0)
#define NCE53_P53        APOLLO3_PINMUX(53, 1)
#define CTIM3_P53        APOLLO3_PINMUX(53, 2)
#define GPIO_P53         APOLLO3_PINMUX(53, 3)
#define MSPI1_3_P54      APOLLO3_PINMUX(54, 0)
#define NCE54_P54        APOLLO3_PINMUX(54, 1)
#define CTIM4_P54        APOLLO3_PINMUX(54, 2)
#define GPIO_P54         APOLLO3_PINMUX(54, 3)
#define MSPI1_4_P55      APOLLO3_PINMUX(55, 0)
#define NCE55_P55        APOLLO3_PINMUX(55, 1)
#define CTIM5_P55        APOLLO3_PINMUX(55, 2)
#define GPIO_P55         APOLLO3_PINMUX(55, 3)
#define MSPI1_5_P56      APOLLO3_PINMUX(56, 0)
#define NCE56_P56        APOLLO3_PINMUX(56, 1)
#define CTIM6_P56        APOLLO3_PINMUX(56, 2)
#define GPIO_P56         APOLLO3_PINMUX(56, 3)
#define MSPI1_6_P57      APOLLO3_PINMUX(57, 0)
#define NCE57_P57        APOLLO3_PINMUX(57, 1)
#define CTIM7_P57        APOLLO3_PINMUX(57, 2)
#define GPIO_P57         APOLLO3_PINMUX(57, 3)
#define MSPI1_7_P58      APOLLO3_PINMUX(58, 0)
#define NCE58_P58        APOLLO3_PINMUX(58, 1)
#define CTIM8_P58        APOLLO3_PINMUX(58, 2)
#define GPIO_P58         APOLLO3_PINMUX(58, 3)
#define MSPI1_8_P59      APOLLO3_PINMUX(59, 0)
#define NCE59_P59        APOLLO3_PINMUX(59, 1)
#define CTIM9_P59        APOLLO3_PINMUX(59, 2)
#define GPIO_P59         APOLLO3_PINMUX(59, 3)
#define MSPI1_9_P60      APOLLO3_PINMUX(60, 0)
#define NCE60_P60        APOLLO3_PINMUX(60, 1)
#define CTIM10_P60       APOLLO3_PINMUX(60, 2)
#define GPIO_P60         APOLLO3_PINMUX(60, 3)
#define SWO_P61          APOLLO3_PINMUX(61, 0)
#define NCE61_P61        APOLLO3_PINMUX(61, 1)
#define CTIM11_P61       APOLLO3_PINMUX(61, 2)
#define GPIO_P61         APOLLO3_PINMUX(61, 3)
#define UART0TX_P61      APOLLO3_PINMUX(61, 4)
#define UART0RX_P61      APOLLO3_PINMUX(61, 5)
#define UART1TX_P61      APOLLO3_PINMUX(61, 6)
#define UART1RX_P61      APOLLO3_PINMUX(61, 7)
#define SWO_P62          APOLLO3_PINMUX(62, 0)
#define NCE62_P62        APOLLO3_PINMUX(62, 1)
#define CTIM12_P62       APOLLO3_PINMUX(62, 2)
#define GPIO_P62         APOLLO3_PINMUX(62, 3)
#define UA0CTS_P62       APOLLO3_PINMUX(62, 4)
#define UA0RTS_P62       APOLLO3_PINMUX(62, 5)
#define UA1CTS_P62       APOLLO3_PINMUX(62, 6)
#define UA1RTS_P62       APOLLO3_PINMUX(62, 7)
#define SWO_P63          APOLLO3_PINMUX(63, 0)
#define NCE63_P63        APOLLO3_PINMUX(63, 1)
#define CTIM13_P63       APOLLO3_PINMUX(63, 2)
#define GPIO_P63         APOLLO3_PINMUX(63, 3)
#define UA0CTS_P63       APOLLO3_PINMUX(63, 4)
#define UA0RTS_P63       APOLLO3_PINMUX(63, 5)
#define UA1CTS_P63       APOLLO3_PINMUX(63, 6)
#define UA1RTS_P63       APOLLO3_PINMUX(63, 7)
#define MSPI2_0_P64      APOLLO3_PINMUX(64, 0)
#define NCE64_P64        APOLLO3_PINMUX(64, 1)
#define CTIM14_P64       APOLLO3_PINMUX(64, 2)
#define GPIO_P64         APOLLO3_PINMUX(64, 3)
#define MSPI2_1_P65      APOLLO3_PINMUX(65, 0)
#define NCE65_P65        APOLLO3_PINMUX(65, 1)
#define CTIM15_P65       APOLLO3_PINMUX(65, 2)
#define GPIO_P65         APOLLO3_PINMUX(65, 3)
#define MSPI2_2_P66      APOLLO3_PINMUX(66, 0)
#define NCE66_P66        APOLLO3_PINMUX(66, 1)
#define CTIM16_P66       APOLLO3_PINMUX(66, 2)
#define GPIO_P66         APOLLO3_PINMUX(66, 3)
#define MSPI2_3_P67      APOLLO3_PINMUX(67, 0)
#define NCE67_P67        APOLLO3_PINMUX(67, 1)
#define CTIM17_P67       APOLLO3_PINMUX(67, 2)
#define GPIO_P67         APOLLO3_PINMUX(67, 3)
#define MSPI2_4_P68      APOLLO3_PINMUX(68, 0)
#define NCE68_P68        APOLLO3_PINMUX(68, 1)
#define CTIM18_P68       APOLLO3_PINMUX(68, 2)
#define GPIO_P68         APOLLO3_PINMUX(68, 3)
#define SWO_P69          APOLLO3_PINMUX(69, 0)
#define NCE69_P69        APOLLO3_PINMUX(69, 1)
#define CTIM19_P69       APOLLO3_PINMUX(69, 2)
#define GPIO_P69         APOLLO3_PINMUX(69, 3)
#define UART0TX_P69      APOLLO3_PINMUX(69, 4)
#define UART0RX_P69      APOLLO3_PINMUX(69, 5)
#define UART1TX_P69      APOLLO3_PINMUX(69, 6)
#define UART1RX_P69      APOLLO3_PINMUX(69, 7)
#define SWO_P70          APOLLO3_PINMUX(70, 0)
#define NCE70_P70        APOLLO3_PINMUX(70, 1)
#define CTIM20_P70       APOLLO3_PINMUX(70, 2)
#define GPIO_P70         APOLLO3_PINMUX(70, 3)
#define UART0TX_P70      APOLLO3_PINMUX(70, 4)
#define UART0RX_P70      APOLLO3_PINMUX(70, 5)
#define UART1TX_P70      APOLLO3_PINMUX(70, 6)
#define UART1RX_P70      APOLLO3_PINMUX(70, 7)
#define SWO_P71          APOLLO3_PINMUX(71, 0)
#define NCE71_P71        APOLLO3_PINMUX(71, 1)
#define CTIM21_P71       APOLLO3_PINMUX(71, 2)
#define GPIO_P71         APOLLO3_PINMUX(71, 3)
#define UART0TX_P71      APOLLO3_PINMUX(71, 4)
#define UART0RX_P71      APOLLO3_PINMUX(71, 5)
#define UART1TX_P71      APOLLO3_PINMUX(71, 6)
#define UART1RX_P71      APOLLO3_PINMUX(71, 7)
#define SWO_P72          APOLLO3_PINMUX(72, 0)
#define NCE72_P72        APOLLO3_PINMUX(72, 1)
#define CTIM22_P72       APOLLO3_PINMUX(72, 2)
#define GPIO_P72         APOLLO3_PINMUX(72, 3)
#define UART0TX_P72      APOLLO3_PINMUX(72, 4)
#define UART0RX_P72      APOLLO3_PINMUX(72, 5)
#define UART1TX_P72      APOLLO3_PINMUX(72, 6)
#define UART1RX_P72      APOLLO3_PINMUX(72, 7)
#define SWO_P73          APOLLO3_PINMUX(73, 0)
#define NCE73_P73        APOLLO3_PINMUX(73, 1)
#define CTIM23_P73       APOLLO3_PINMUX(73, 2)
#define GPIO_P73         APOLLO3_PINMUX(73, 3)
#define UA0CTS_P73       APOLLO3_PINMUX(73, 4)
#define UA0RTS_P73       APOLLO3_PINMUX(73, 5)
#define UA1CTS_P73       APOLLO3_PINMUX(73, 6)
#define UA1RTS_P73       APOLLO3_PINMUX(73, 7)



#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_AMBIQ_APOLLO3_PINCTRL_H_ */
```

## 25.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Ambiq Micro Inc. <www.ambiq.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 541 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_AMBIQ_APOLLO3_PINCTRL_H_`。

## 25.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ambiq-apollo3-pinctrl_8h.html)

---

[上一章](P024_alif-ensemble-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P026_ambiq-apollo4-pinctrl.h_源码浏览.md)
