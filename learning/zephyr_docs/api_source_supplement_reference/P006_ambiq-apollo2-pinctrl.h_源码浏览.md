---
id: learning.zephyr-docs.api-source-supplement-reference.page-6
title: ambiq-apollo2-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ambiq-apollo2-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_ambiq-apollo2-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ambiq-apollo2-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ambiq-apollo2-pinctrl_8h.html)。

## 6.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00021"></a>
<a id="l00051"></a>
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
<a id="l00490"></a>
<a id="l00492"></a>
<a id="l00493"></a>

```c
/*
 * SPDX-License-Identifier: Apache-2.0
 *
 * Copyright (c) 2025 Linumiz GmbH
 * Author: Sri Surya  <srisurya@linumiz.com>
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_AMBIQ_APOLLO2_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_AMBIQ_APOLLO2_PINCTRL_H_




#define APOLLO2_ALT_FUNC_POS  0
#define APOLLO2_ALT_FUNC_MASK 0x7

#define APOLLO2_PIN_NUM_POS  3
#define APOLLO2_PIN_NUM_MASK 0x3f

#define APOLLO2_PINMUX(pin_num, alt_func)                                       \
        (((pin_num) << APOLLO2_PIN_NUM_POS) | ((alt_func) << APOLLO2_ALT_FUNC_POS))

#define SLSCL_P0        APOLLO2_PINMUX(0, 0)
#define SLSCK_P0        APOLLO2_PINMUX(0, 1)
#define CLKOUT_P0       APOLLO2_PINMUX(0, 2)
#define GPIO0_P0        APOLLO2_PINMUX(0, 3)
#define MXSCKLB_P0      APOLLO2_PINMUX(0, 4)
#define M2SCK_P0        APOLLO2_PINMUX(0, 5)
#define MXSCLLB_P0      APOLLO2_PINMUX(0, 6)
#define M2SCL_P0        APOLLO2_PINMUX(0, 7)

#define SLSDA_P1        APOLLO2_PINMUX(1, 0)
#define SLMISO_P1       APOLLO2_PINMUX(1, 1)
#define UART0TX_P1      APOLLO2_PINMUX(1, 2)
#define GPIO1_P1        APOLLO2_PINMUX(1, 3)
#define MXMISOLB_P1     APOLLO2_PINMUX(1, 4)
#define M2MISO_P1       APOLLO2_PINMUX(1, 5)
#define MXSDALB_P1      APOLLO2_PINMUX(1, 6)
#define M2SDA_P1        APOLLO2_PINMUX(1, 7)

#define SLWIR3_P2       APOLLO2_PINMUX(2, 0)
#define SLMOSI_P2       APOLLO2_PINMUX(2, 1)
#define UART0RX_P2      APOLLO2_PINMUX(2, 2)
#define GPIO2_P2        APOLLO2_PINMUX(2, 3)
#define MXMOSILB_P2     APOLLO2_PINMUX(2, 4)
#define M2MOSI_P2       APOLLO2_PINMUX(2, 5)
#define MXWIR3LB_P2     APOLLO2_PINMUX(2, 6)
#define M2WIR3_P2       APOLLO2_PINMUX(2, 7)

#define UART0RTS_P3     APOLLO2_PINMUX(3, 0)
#define SLNCE_P3        APOLLO2_PINMUX(3, 1)
#define M1NCE4_P3       APOLLO2_PINMUX(3, 2)
#define GPIO3_P3        APOLLO2_PINMUX(3, 3)
#define MXNCELB_P3      APOLLO2_PINMUX(3, 4)
#define M2NCE0_P3       APOLLO2_PINMUX(3, 5)
#define TRIG1_P3        APOLLO2_PINMUX(3, 6)
#define I2S_WCLK_P3     APOLLO2_PINMUX(3, 7)

#define UART0CTS_P4     APOLLO2_PINMUX(4, 0)
#define SLINT_P4        APOLLO2_PINMUX(4, 1)
#define M0NCE5_P4       APOLLO2_PINMUX(4, 2)
#define GPIO4_P4        APOLLO2_PINMUX(4, 3)
#define SLINTGP_P4      APOLLO2_PINMUX(4, 4)
#define M2NCE5_P4       APOLLO2_PINMUX(4, 5)
#define CLKOUT_P4       APOLLO2_PINMUX(4, 6)
#define _32KHZ_XT_P4    APOLLO2_PINMUX(4, 7)

#define M0SCL_P5        APOLLO2_PINMUX(5, 0)
#define M0SCK_P5        APOLLO2_PINMUX(5, 1)
#define UART0RTS_P5     APOLLO2_PINMUX(5, 2)
#define GPIO5_P5        APOLLO2_PINMUX(5, 3)
#define M0SCKLB_P5      APOLLO2_PINMUX(5, 4)
#define M0SCLLB_P5      APOLLO2_PINMUX(5, 6)
#define M1NCE2_P5       APOLLO2_PINMUX(5, 7)

#define M0SDA_P6        APOLLO2_PINMUX(6, 0)
#define M0MISO_P6       APOLLO2_PINMUX(6, 1)
#define UART0CTS_P6     APOLLO2_PINMUX(6, 2)
#define GPIO6_P6        APOLLO2_PINMUX(6, 3)
#define SLMISOLB_P6     APOLLO2_PINMUX(6, 4)
#define M1NCE0_P6       APOLLO2_PINMUX(6, 5)
#define SLSDALB_P6      APOLLO2_PINMUX(6, 6)
#define I2S_DAT_P6      APOLLO2_PINMUX(6, 7)

#define M0WIR3_P7       APOLLO2_PINMUX(7, 0)
#define M0MOSI_P7       APOLLO2_PINMUX(7, 1)
#define CLKOUT_P7       APOLLO2_PINMUX(7, 2)
#define GPIO7_P7        APOLLO2_PINMUX(7, 3)
#define TRIG0_P7        APOLLO2_PINMUX(7, 4)
#define UART0TX_P7      APOLLO2_PINMUX(7, 5)
#define SLWIR3LB_P7     APOLLO2_PINMUX(7, 6)
#define M1NCE1_P7       APOLLO2_PINMUX(7, 7)

#define M1SCL_P8        APOLLO2_PINMUX(8, 0)
#define M1SCK_P8        APOLLO2_PINMUX(8, 1)
#define M0NCE4_P8       APOLLO2_PINMUX(8, 2)
#define GPIO8_P8        APOLLO2_PINMUX(8, 3)
#define M2NCE4_P8       APOLLO2_PINMUX(8, 4)
#define M1SCKLB_P8      APOLLO2_PINMUX(8, 5)
#define UART1TX_P8      APOLLO2_PINMUX(8, 6)
#define M1SCLLB_P8      APOLLO2_PINMUX(8, 7)

#define M1SDA_P9        APOLLO2_PINMUX(9, 0)
#define M1MISO_P9       APOLLO2_PINMUX(9, 1)
#define M0NCE5_P9       APOLLO2_PINMUX(9, 2)
#define GPIO9_P9        APOLLO2_PINMUX(9, 3)
#define M4NCE5_P9       APOLLO2_PINMUX(9, 4)
#define SLMISOLB_P9     APOLLO2_PINMUX(9, 5)
#define UART1RX_P9      APOLLO2_PINMUX(9, 6)
#define SLSDALB_P9      APOLLO2_PINMUX(9, 7)

#define M1WIR3_P10      APOLLO2_PINMUX(10, 0)
#define M1MOSI_P10      APOLLO2_PINMUX(10, 1)
#define M0NCE6_P10      APOLLO2_PINMUX(10, 2)
#define GPIO10_P10      APOLLO2_PINMUX(10, 3)
#define M2NCE6_P10      APOLLO2_PINMUX(10, 4)
#define UART1RTS_P10    APOLLO2_PINMUX(10, 5)
#define M4NCE4_P10      APOLLO2_PINMUX(10, 6)
#define SLWIR3LB_P10    APOLLO2_PINMUX(10, 7)

#define ADCSE2_P11      APOLLO2_PINMUX(11, 0)
#define M0NCE0_P11      APOLLO2_PINMUX(11, 1)
#define CLKOUT_P11      APOLLO2_PINMUX(11, 2)
#define GPIO11_P11      APOLLO2_PINMUX(11, 3)
#define M2NCE7_P11      APOLLO2_PINMUX(11, 4)
#define UART1CTS_P11    APOLLO2_PINMUX(11, 5)
#define UART0RX_P11     APOLLO2_PINMUX(11, 6)
#define PDM_DATA_P11    APOLLO2_PINMUX(11, 7)

#define ADCD0NSE9_P12   APOLLO2_PINMUX(12, 0)
#define M1NCE0_P12      APOLLO2_PINMUX(12, 1)
#define TCTA0_P12       APOLLO2_PINMUX(12, 2)
#define GPIO12_P12      APOLLO2_PINMUX(12, 3)
#define CLKOUT_P12      APOLLO2_PINMUX(12, 4)
#define PDM_CLK_P12     APOLLO2_PINMUX(12, 5)
#define UART0CTS_P12    APOLLO2_PINMUX(12, 6)
#define UART1TX_P12     APOLLO2_PINMUX(12, 7)

#define ADCD0PSE8_P13   APOLLO2_PINMUX(13, 0)
#define M1NCE1_P13      APOLLO2_PINMUX(13, 1)
#define TCTB0_P13       APOLLO2_PINMUX(13, 2)
#define GPIO13_P13      APOLLO2_PINMUX(13, 3)
#define M2NCE3_P13      APOLLO2_PINMUX(13, 4)
#define UART0RTS_P13    APOLLO2_PINMUX(13, 6)
#define UART1RX_P13     APOLLO2_PINMUX(13, 7)

#define ADCD1P_P14      APOLLO2_PINMUX(14, 0)
#define M1NCE2_P14      APOLLO2_PINMUX(14, 1)
#define UART1TX_P14     APOLLO2_PINMUX(14, 2)
#define GPIO14_P14      APOLLO2_PINMUX(14, 3)
#define M2NCE1_P14      APOLLO2_PINMUX(14, 4)
#define SWDCK_P14       APOLLO2_PINMUX(14, 6)
#define _32KHZ_XT_P14   APOLLO2_PINMUX(14, 7)

#define ADCD1N_P15      APOLLO2_PINMUX(15, 0)
#define M1NCE3_P15      APOLLO2_PINMUX(15, 1)
#define UART1RX_P15     APOLLO2_PINMUX(15, 2)
#define GPIO15_P15      APOLLO2_PINMUX(15, 3)
#define M2NCE2_P15      APOLLO2_PINMUX(15, 4)
#define SWDIO_P15       APOLLO2_PINMUX(15, 6)
#define SWO_P15         APOLLO2_PINMUX(15, 7)

#define ADCSE0_P16      APOLLO2_PINMUX(16, 0)
#define M0NCE4_P16      APOLLO2_PINMUX(16, 1)
#define TRIG0_P16       APOLLO2_PINMUX(16, 2)
#define GPIO16_P16      APOLLO2_PINMUX(16, 3)
#define M2NCE3_P16      APOLLO2_PINMUX(16, 4)
#define CMPIN0_P16      APOLLO2_PINMUX(16, 5)
#define UART0TX_P16     APOLLO2_PINMUX(16, 6)
#define UART1RTS_P16    APOLLO2_PINMUX(16, 7)

#define CMPRF1_P17      APOLLO2_PINMUX(17, 0)
#define M0NCE1_P17      APOLLO2_PINMUX(17, 1)
#define TRIG1_P17       APOLLO2_PINMUX(17, 2)
#define GPIO17_P17      APOLLO2_PINMUX(17, 3)
#define M4NCE3_P17      APOLLO2_PINMUX(17, 4)
#define UART0RX_P17     APOLLO2_PINMUX(17, 6)
#define UART1CTS_P17    APOLLO2_PINMUX(17, 7)

#define CMPIN1_P18      APOLLO2_PINMUX(18, 0)
#define M0NCE2_P18      APOLLO2_PINMUX(18, 1)
#define TCTA1_P18       APOLLO2_PINMUX(18, 2)
#define GPIO18_P18      APOLLO2_PINMUX(18, 3)
#define M4NCE1_P18      APOLLO2_PINMUX(18, 4)
#define UART1TX_P18     APOLLO2_PINMUX(18, 6)
#define _32KHZ_XT_P18   APOLLO2_PINMUX(18, 7)

#define CMPRF0_P19      APOLLO2_PINMUX(19, 0)
#define M0NCE3_P19      APOLLO2_PINMUX(19, 1)
#define TCTB1_P19       APOLLO2_PINMUX(19, 2)
#define GPIO19_P19      APOLLO2_PINMUX(19, 3)
#define TCTA1_P19       APOLLO2_PINMUX(19, 4)
#define UART1RX_P19     APOLLO2_PINMUX(19, 6)
#define I2S_BCLK_P19    APOLLO2_PINMUX(19, 7)

#define SWDCK_P20       APOLLO2_PINMUX(20, 0)
#define M1NCE5_P20      APOLLO2_PINMUX(20, 1)
#define TCTA2_P20       APOLLO2_PINMUX(20, 2)
#define GPIO20_P20      APOLLO2_PINMUX(20, 3)
#define UART0TX_P20     APOLLO2_PINMUX(20, 4)
#define UART1TX_P20     APOLLO2_PINMUX(20, 5)

#define SWDIO_P21       APOLLO2_PINMUX(21, 0)
#define M1NCE6_P21      APOLLO2_PINMUX(21, 1)
#define TCTB2_P21       APOLLO2_PINMUX(21, 2)
#define GPIO21_P21      APOLLO2_PINMUX(21, 3)
#define UART0RX_P21     APOLLO2_PINMUX(21, 4)
#define UART1RX_P21     APOLLO2_PINMUX(21, 5)

#define UART0TX_P22     APOLLO2_PINMUX(22, 0)
#define M1NCE7_P22      APOLLO2_PINMUX(22, 1)
#define TCTA3_P22       APOLLO2_PINMUX(22, 2)
#define GPIO22_P22      APOLLO2_PINMUX(22, 3)
#define PDM_CLK_P22     APOLLO2_PINMUX(22, 4)
#define TCTB1_P22       APOLLO2_PINMUX(22, 6)
#define SWO_P22         APOLLO2_PINMUX(22, 7)

#define UART0RX_P23     APOLLO2_PINMUX(23, 0)
#define M0NCE0_P23      APOLLO2_PINMUX(23, 1)
#define TCTB3_P23       APOLLO2_PINMUX(23, 2)
#define GPIO23_P23      APOLLO2_PINMUX(23, 3)
#define PDM_DATA_P23    APOLLO2_PINMUX(23, 4)
#define CMPOUT_P23      APOLLO2_PINMUX(23, 5)
#define TCTB1_P23       APOLLO2_PINMUX(23, 6)

#define M2NCE1_P24      APOLLO2_PINMUX(24, 0)
#define M0NCE1_P24      APOLLO2_PINMUX(24, 1)
#define CLKOUT_P24      APOLLO2_PINMUX(24, 2)
#define GPIO24_P24      APOLLO2_PINMUX(24, 3)
#define M5NCE0_P24      APOLLO2_PINMUX(24, 4)
#define TCTA1_P24       APOLLO2_PINMUX(24, 5)
#define I2S_BCLK_P24    APOLLO2_PINMUX(24, 6)
#define SWO_P24         APOLLO2_PINMUX(24, 7)

#define M0NCE2_P25      APOLLO2_PINMUX(25, 1)
#define TCTA0_P25       APOLLO2_PINMUX(25, 2)
#define GPIO25_P25      APOLLO2_PINMUX(25, 3)
#define M2SDA_P25       APOLLO2_PINMUX(25, 4)
#define M2MISO_P25      APOLLO2_PINMUX(25, 5)
#define SLMISOLB_P25    APOLLO2_PINMUX(25, 6)
#define SLSDALB_P25     APOLLO2_PINMUX(25, 7)

#define M0NCE3_P26      APOLLO2_PINMUX(26, 1)
#define TCTB0_P26       APOLLO2_PINMUX(26, 2)
#define GPIO26_P26      APOLLO2_PINMUX(26, 3)
#define M2NCE0_P26      APOLLO2_PINMUX(26, 4)
#define TCTA1_P26       APOLLO2_PINMUX(26, 5)
#define M5NCE1_P26      APOLLO2_PINMUX(26, 6)
#define M3NCE0_P26      APOLLO2_PINMUX(26, 7)

#define M1NCE4_P27      APOLLO2_PINMUX(27, 1)
#define TCTA1_P27       APOLLO2_PINMUX(27, 2)
#define GPIO27_P27      APOLLO2_PINMUX(27, 3)
#define M2SCL_P27       APOLLO2_PINMUX(27, 4)
#define M2SCK_P27       APOLLO2_PINMUX(27, 5)
#define M2SCKLB_P27     APOLLO2_PINMUX(27, 6)
#define M2SCLLB_P27     APOLLO2_PINMUX(27, 7)

#define I2S_WCLK_P28    APOLLO2_PINMUX(28, 0)
#define M1NCE5_P28      APOLLO2_PINMUX(28, 1)
#define TCTB1_P28       APOLLO2_PINMUX(28, 2)
#define GPIO28_P28      APOLLO2_PINMUX(28, 3)
#define M2WIR3_P28      APOLLO2_PINMUX(28, 4)
#define M2MOSI_P28      APOLLO2_PINMUX(28, 5)
#define M5NCE3_P28      APOLLO2_PINMUX(28, 6)
#define SLWIR3LB_P28    APOLLO2_PINMUX(28, 7)

#define ADCSE1_P29      APOLLO2_PINMUX(29, 0)
#define M1NCE6_P29      APOLLO2_PINMUX(29, 1)
#define TCTA2_P29       APOLLO2_PINMUX(29, 2)
#define GPIO29_P29      APOLLO2_PINMUX(29, 3)
#define UART0CTS_P29    APOLLO2_PINMUX(29, 4)
#define UART1CTS_P29    APOLLO2_PINMUX(29, 5)
#define M4NCE0_P29      APOLLO2_PINMUX(29, 6)
#define PDM_DATA_P29    APOLLO2_PINMUX(29, 7)

#define M1NCE7_P30      APOLLO2_PINMUX(30, 1)
#define TCTB2_P30       APOLLO2_PINMUX(30, 2)
#define GPIO30_P30      APOLLO2_PINMUX(30, 3)
#define UART0TX_P30     APOLLO2_PINMUX(30, 4)
#define UART1RTS_P30    APOLLO2_PINMUX(30, 5)
#define I2S_DAT_P30     APOLLO2_PINMUX(30, 7)

#define ADCSE3_P31      APOLLO2_PINMUX(31, 0)
#define M0NCE4_P31      APOLLO2_PINMUX(31, 1)
#define TCTA3_P31       APOLLO2_PINMUX(31, 2)
#define GPIO31_P31      APOLLO2_PINMUX(31, 3)
#define UART0RX_P31     APOLLO2_PINMUX(31, 4)
#define TCTB1_P31       APOLLO2_PINMUX(31, 5)

#define ADCSE4_P32      APOLLO2_PINMUX(32, 0)
#define M0NCE5_P32      APOLLO2_PINMUX(32, 1)
#define TCTB3_P32       APOLLO2_PINMUX(32, 2)
#define GPIO32_P32      APOLLO2_PINMUX(32, 3)
#define TCTB1_P32       APOLLO2_PINMUX(32, 5)

#define ADCSE5_P33      APOLLO2_PINMUX(33, 0)
#define M0NCE6_P33      APOLLO2_PINMUX(33, 1)
#define _32KHZ_XT_P33   APOLLO2_PINMUX(33, 2)
#define GPIO33_P33      APOLLO2_PINMUX(33, 3)
#define M3NCE7_P33      APOLLO2_PINMUX(33, 5)
#define TCTB1_P33       APOLLO2_PINMUX(33, 6)
#define SWO_P33         APOLLO2_PINMUX(33, 7)

#define ADCSE6_P34      APOLLO2_PINMUX(34, 0)
#define M0NCE7_P34      APOLLO2_PINMUX(34, 1)
#define M2NCE3_P34      APOLLO2_PINMUX(34, 2)
#define GPIO34_P34      APOLLO2_PINMUX(34, 3)
#define CMPRF2_P34      APOLLO2_PINMUX(34, 4)
#define M3NCE1_P34      APOLLO2_PINMUX(34, 5)
#define M4NCE0_P34      APOLLO2_PINMUX(34, 6)
#define M5NCE2_P34      APOLLO2_PINMUX(34, 7)

#define ADCSE7_P35      APOLLO2_PINMUX(35, 0)
#define M1NCE0_P35      APOLLO2_PINMUX(35, 1)
#define UART1TX_P35     APOLLO2_PINMUX(35, 2)
#define GPIO35_P35      APOLLO2_PINMUX(35, 3)
#define M4NCE6_P35      APOLLO2_PINMUX(35, 4)
#define TCTA1_P35       APOLLO2_PINMUX(35, 5)
#define UART0RTS_P35    APOLLO2_PINMUX(35, 6)
#define M3NCE2_P35      APOLLO2_PINMUX(35, 7)

#define TRIG1_P36       APOLLO2_PINMUX(36, 0)
#define M1NCE1_P36      APOLLO2_PINMUX(36, 1)
#define UART1RX_P36     APOLLO2_PINMUX(36, 2)
#define GPIO36_P36      APOLLO2_PINMUX(36, 3)
#define _32KHZ_XT_P36   APOLLO2_PINMUX(36, 4)
#define M2NCE0_P36      APOLLO2_PINMUX(36, 5)
#define UART0CTS_P36    APOLLO2_PINMUX(36, 6)
#define M3NCE3_P36      APOLLO2_PINMUX(36, 7)

#define TRIG2_P37       APOLLO2_PINMUX(37, 0)
#define M1NCE2_P37      APOLLO2_PINMUX(37, 1)
#define UART0RTS_P37    APOLLO2_PINMUX(37, 2)
#define GPIO37_P37      APOLLO2_PINMUX(37, 3)
#define M3NCE4_P37      APOLLO2_PINMUX(37, 4)
#define M4NCE1_P37      APOLLO2_PINMUX(37, 5)
#define PDM_CLK_P37     APOLLO2_PINMUX(37, 6)
#define TCTA1_P37       APOLLO2_PINMUX(37, 7)

#define TRIG3_P38       APOLLO2_PINMUX(38, 0)
#define M1NCE3_P38      APOLLO2_PINMUX(38, 1)
#define UART0CTS_P38    APOLLO2_PINMUX(38, 2)
#define GPIO38_P38      APOLLO2_PINMUX(38, 3)
#define M3WIR3_P38      APOLLO2_PINMUX(38, 4)
#define M3MOSI_P38      APOLLO2_PINMUX(38, 5)
#define M4NCE7_P38      APOLLO2_PINMUX(38, 6)
#define SLWIR3LB_P38    APOLLO2_PINMUX(38, 7)

#define UART0TX_P39     APOLLO2_PINMUX(39, 0)
#define UART1TX_P39     APOLLO2_PINMUX(39, 1)
#define CLKOUT_P39      APOLLO2_PINMUX(39, 2)
#define GPIO39_P39      APOLLO2_PINMUX(39, 3)
#define M4SCL_P39       APOLLO2_PINMUX(39, 4)
#define M4SCK_P39       APOLLO2_PINMUX(39, 5)
#define M4SCKLB_P39     APOLLO2_PINMUX(39, 6)
#define M4SCLLB_P39     APOLLO2_PINMUX(39, 7)

#define UART0RX_P40     APOLLO2_PINMUX(40, 0)
#define UART1RX_P40     APOLLO2_PINMUX(40, 1)
#define TRIG0_P40       APOLLO2_PINMUX(40, 2)
#define GPIO40_P40      APOLLO2_PINMUX(40, 3)
#define M4SDA_P40       APOLLO2_PINMUX(40, 4)
#define M4MISO_P40      APOLLO2_PINMUX(40, 5)
#define SLMISOLB_P40    APOLLO2_PINMUX(40, 6)
#define SLSDALB_P40     APOLLO2_PINMUX(40, 7)

#define M2NCE1_P41      APOLLO2_PINMUX(41, 0)
#define CLKOUT_P41      APOLLO2_PINMUX(41, 1)
#define SWO_P41         APOLLO2_PINMUX(41, 2)
#define GPIO41_P41      APOLLO2_PINMUX(41, 3)
#define M3NCE5_P41      APOLLO2_PINMUX(41, 4)
#define M5NCE7_P41      APOLLO2_PINMUX(41, 5)
#define M4NCE2_P41      APOLLO2_PINMUX(41, 6)
#define UART0RTS_P41    APOLLO2_PINMUX(41, 7)

#define M2NCE2_P42      APOLLO2_PINMUX(42, 0)
#define M0NCE0_P42      APOLLO2_PINMUX(42, 1)
#define TCTA0_P42       APOLLO2_PINMUX(42, 2)
#define GPIO42_P42      APOLLO2_PINMUX(42, 3)
#define M3SCL_P42       APOLLO2_PINMUX(42, 4)
#define M3SCK_P42       APOLLO2_PINMUX(42, 5)
#define M3SCKLB_P42     APOLLO2_PINMUX(42, 6)
#define M3SCLLB_P42     APOLLO2_PINMUX(42, 7)

#define M2NCE4_P43      APOLLO2_PINMUX(43, 0)
#define M0NCE1_P43      APOLLO2_PINMUX(43, 1)
#define TCTB0_P43       APOLLO2_PINMUX(43, 2)
#define GPIO43_P43      APOLLO2_PINMUX(43, 3)
#define M3SDA_P43       APOLLO2_PINMUX(43, 4)
#define M3MISO_P43      APOLLO2_PINMUX(43, 5)
#define SLMISOLB_P43    APOLLO2_PINMUX(43, 6)
#define SLSDALB_P43     APOLLO2_PINMUX(43, 7)

#define UART1RTS_P44    APOLLO2_PINMUX(44, 0)
#define M0NCE2_P44      APOLLO2_PINMUX(44, 1)
#define TCTA1_P44       APOLLO2_PINMUX(44, 2)
#define GPIO44_P44      APOLLO2_PINMUX(44, 3)
#define M4WIR3_P44      APOLLO2_PINMUX(44, 4)
#define M4MOSI_P44      APOLLO2_PINMUX(44, 5)
#define M5NCE6_P44      APOLLO2_PINMUX(44, 6)
#define SLWIR3LB_P44    APOLLO2_PINMUX(44, 7)

#define UART1CTS_P45    APOLLO2_PINMUX(45, 0)
#define M0NCE3_P45      APOLLO2_PINMUX(45, 1)
#define TCTB1_P45       APOLLO2_PINMUX(45, 2)
#define GPIO45_P45      APOLLO2_PINMUX(45, 3)
#define M4NCE3_P45      APOLLO2_PINMUX(45, 4)
#define M3NCE6_P45      APOLLO2_PINMUX(45, 5)
#define M5NCE5_P45      APOLLO2_PINMUX(45, 6)
#define SWO_P45         APOLLO2_PINMUX(45, 7)

#define _32KHZ_XT_P46   APOLLO2_PINMUX(46, 0)
#define M0NCE4_P46      APOLLO2_PINMUX(46, 1)
#define TCTA2_P46       APOLLO2_PINMUX(46, 2)
#define GPIO46_P46      APOLLO2_PINMUX(46, 3)
#define TCTA1_P46       APOLLO2_PINMUX(46, 4)
#define M5NCE4_P46      APOLLO2_PINMUX(46, 5)
#define M4NCE4_P46      APOLLO2_PINMUX(46, 6)
#define SWO_P46         APOLLO2_PINMUX(46, 7)

#define M2NCE5_P47      APOLLO2_PINMUX(47, 0)
#define M0NCE5_P47      APOLLO2_PINMUX(47, 1)
#define TCTB2_P47       APOLLO2_PINMUX(47, 2)
#define GPIO47_P47      APOLLO2_PINMUX(47, 3)
#define M5WIR3_P47      APOLLO2_PINMUX(47, 4)
#define M5MOSI_P47      APOLLO2_PINMUX(47, 5)
#define M4NCE5_P47      APOLLO2_PINMUX(47, 6)
#define SLWIR3LB_P47    APOLLO2_PINMUX(47, 7)

#define M2NCE6_P48      APOLLO2_PINMUX(48, 0)
#define M0NCE6_P48      APOLLO2_PINMUX(48, 1)
#define TCTA3_P48       APOLLO2_PINMUX(48, 2)
#define GPIO48_P48      APOLLO2_PINMUX(48, 3)
#define M5SCL_P48       APOLLO2_PINMUX(48, 4)
#define M5SCK_P48       APOLLO2_PINMUX(48, 5)
#define M5SCKLB_P48     APOLLO2_PINMUX(48, 6)
#define M5SCLLB_P48     APOLLO2_PINMUX(48, 7)

#define M2NCE7_P49      APOLLO2_PINMUX(49, 0)
#define M0NCE7_P49      APOLLO2_PINMUX(49, 1)
#define TCTB3_P49       APOLLO2_PINMUX(49, 2)
#define GPIO49_P49      APOLLO2_PINMUX(49, 3)
#define M5SDA_P49       APOLLO2_PINMUX(49, 4)
#define M5MISO_P49      APOLLO2_PINMUX(49, 5)
#define SLMISOLB_P49    APOLLO2_PINMUX(49, 6)
#define SLSDALB_P49     APOLLO2_PINMUX(49, 7)



#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_AMBIQ_APOLLO2_PINCTRL_H_ */
```

## 6.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

版权（Copyright）：© 2025 Linumiz GmbH。

作者（Author）：Sri Surya <srisurya@linumiz.com>。

### 注释 2：原第 493 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_AMBIQ_APOLLO2_PINCTRL_H_`。

## 6.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ambiq-apollo2-pinctrl_8h.html)

---

[上一章](P005_aio.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P007_ameba_clock_control.h_源码浏览.md)
