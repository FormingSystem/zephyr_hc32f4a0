---
id: learning.zephyr-docs.api-source-workqueue-pin-control-reference.page-3
title: lpc11u6x-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lpc11u6x-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_lpc11u6x-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/lpc11u6x-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_management_reference/P027_zephyr__dt-bindings__pinctrl__lpc11u6x-pinctrl.h_文件参考.md)。

## 3.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00023"></a>
<a id="l00039"></a>
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
<a id="foldopen00106"></a>
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

```c
/*
 * Copyright (c) 2020 Seagate Technology LLC
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_LPC11U6X_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_LPC11U6X_PINCTRL_H_




#define IOCON_FUNC0 0
#define IOCON_FUNC1 1
#define IOCON_FUNC2 2
#define IOCON_FUNC3 3
#define IOCON_FUNC4 4
#define IOCON_FUNC5 5

#define IOCON_MODE_INACT        (0 << 3) /* No pull resistor. */
#define IOCON_MODE_PULLDOWN     (1 << 3) /* Enable pull-down resistor. */
#define IOCON_MODE_PULLUP       (2 << 3) /* Enable Pull-up resistor. */
#define IOCON_MODE_REPEATER     (3 << 3) /* Repeater mode. */

#define IOCON_HYS_EN            (1 << 5) /* Enable hysteresis. */

#define IOCON_INV_EN            (1 << 6) /* Invert input polarity. */

/* Only for analog pins. */
#define IOCON_ADMODE_EN         (0 << 7) /* Enable analog input mode. */
#define IOCON_DIGMODE_EN        (1 << 7) /* Enable digital I/O mode. */
#define IOCON_FILTR_DIS         (1 << 8) /* Disable noise filtering. */

/* Only for open-drain pins (I2C). */
#define IOCON_SFI2C_EN          (0 << 8) /* I2C standard mode / Fast-mode. */
#define IOCON_STDI2C_EN         (1 << 8) /* GPIO functionality. */
#define IOCON_FASTI2C_EN        (2 << 8) /* I2C Fast-mode Plus. */

#define IOCON_OPENDRAIN_EN      (1 << 10) /* Enable open-drain mode. */

/*
 * The digital filter mode allows to discard input pulses shorter than
 * 1, 2 or 3 clock cycles.
 */
#define IOCON_S_MODE_0CLK       (0 << 11) /* No input filter. */
#define IOCON_S_MODE_1CLK       (1 << 11)
#define IOCON_S_MODE_2CLK       (2 << 11)
#define IOCON_S_MODE_3CLK       (3 << 11)

/*
 * Clock divisor.
 */
#define IOCON_CLKDIV0           (0 << 13)
#define IOCON_CLKDIV1           (1 << 13)
#define IOCON_CLKDIV2           (2 << 13)
#define IOCON_CLKDIV3           (3 << 13)
#define IOCON_CLKDIV4           (4 << 13)
#define IOCON_CLKDIV5           (5 << 13)
#define IOCON_CLKDIV6           (6 << 13)


/*
 * Pin control definitions used by LPC pin control driver to make pinmux
 * selections.
 */

#define IOCON_MUX(offset, type, mux)            \
        (((offset & 0xFFF) << 20) |             \
        (((type) & 0x3) << 18) |                \
        (((mux) & 0xF) << 0))

#define IOCON_TYPE_D 0x0
#define IOCON_TYPE_I 0x1
#define IOCON_TYPE_A 0x2

#define RESET_PIO0_0 IOCON_MUX(0, IOCON_TYPE_D, 0) /* PIO0_0 */
#define PIO0_0_PIO0_0 IOCON_MUX(0, IOCON_TYPE_D, 1) /* PIO0_0 */
#define PIO0_1_PIO0_1 IOCON_MUX(1, IOCON_TYPE_D, 0) /* PIO0_1 */
#define CLKOUT_PIO0_1 IOCON_MUX(1, IOCON_TYPE_D, 1) /* PIO0_1 */
#define CT32B0_MAT2_PIO0_1 IOCON_MUX(1, IOCON_TYPE_D, 2) /* PIO0_1 */
#define USB_FTOGGLE_PIO0_1 IOCON_MUX(1, IOCON_TYPE_D, 3) /* PIO0_1 */
#define PIO0_2_PIO0_2 IOCON_MUX(2, IOCON_TYPE_D, 0) /* PIO0_2 */
#define SSP0_SSEL_PIO0_2 IOCON_MUX(2, IOCON_TYPE_D, 1) /* PIO0_2 */
#define CT16B0_CAP0_PIO0_2 IOCON_MUX(2, IOCON_TYPE_D, 2) /* PIO0_2 */
#define R_0_PIO0_2 IOCON_MUX(2, IOCON_TYPE_D, 3) /* PIO0_2 */
#define PIO0_3_PIO0_3 IOCON_MUX(3, IOCON_TYPE_D, 0) /* PIO0_3 */
#define USB_VBUS_PIO0_3 IOCON_MUX(3, IOCON_TYPE_D, 1) /* PIO0_3 */
#define R_1_PIO0_3 IOCON_MUX(3, IOCON_TYPE_D, 2) /* PIO0_3 */
#define PIO0_4_PIO0_4 IOCON_MUX(4, IOCON_TYPE_I, 0) /* PIO0_4 */
#define I2C0_SCL_PIO0_4 IOCON_MUX(4, IOCON_TYPE_I, 1) /* PIO0_4 */
#define R_2_PIO0_4 IOCON_MUX(4, IOCON_TYPE_I, 2) /* PIO0_4 */
#define PIO0_5_PIO0_5 IOCON_MUX(5, IOCON_TYPE_I, 0) /* PIO0_5 */
#define I2C0_SDA_PIO0_5 IOCON_MUX(5, IOCON_TYPE_I, 1) /* PIO0_5 */
#define R_3_PIO0_5 IOCON_MUX(5, IOCON_TYPE_I, 2) /* PIO0_5 */
#define PIO0_6_PIO0_6 IOCON_MUX(6, IOCON_TYPE_D, 0) /* PIO0_6 */
#define R_PIO0_6 IOCON_MUX(6, IOCON_TYPE_D, 1) /* PIO0_6 */
#define SSP0_SCK_PIO0_6 IOCON_MUX(6, IOCON_TYPE_D, 2) /* PIO0_6 */
#define R_4_PIO0_6 IOCON_MUX(6, IOCON_TYPE_D, 3) /* PIO0_6 */
#define PIO0_7_PIO0_7 IOCON_MUX(7, IOCON_TYPE_D, 0) /* PIO0_7 */
#define U0_CTS_PIO0_7 IOCON_MUX(7, IOCON_TYPE_D, 1) /* PIO0_7 */
#define R_5_PIO0_7 IOCON_MUX(7, IOCON_TYPE_D, 2) /* PIO0_7 */
#define I2C1_SCL_PIO0_7 IOCON_MUX(7, IOCON_TYPE_D, 3) /* PIO0_7 */
#define PIO0_8_PIO0_8 IOCON_MUX(8, IOCON_TYPE_D, 0) /* PIO0_8 */
#define SSP0_MISO_PIO0_8 IOCON_MUX(8, IOCON_TYPE_D, 1) /* PIO0_8 */
#define CT16B0_MAT0_PIO0_8 IOCON_MUX(8, IOCON_TYPE_D, 2) /* PIO0_8 */
#define R_6_PIO0_8 IOCON_MUX(8, IOCON_TYPE_D, 3) /* PIO0_8 */
#define PIO0_9_PIO0_9 IOCON_MUX(9, IOCON_TYPE_D, 0) /* PIO0_9 */
#define SSP0_MOSI_PIO0_9 IOCON_MUX(9, IOCON_TYPE_D, 1) /* PIO0_9 */
#define CT16B0_MAT1_PIO0_9 IOCON_MUX(9, IOCON_TYPE_D, 2) /* PIO0_9 */
#define R_7_PIO0_9 IOCON_MUX(9, IOCON_TYPE_D, 3) /* PIO0_9 */
#define SWCLK_PIO0_10 IOCON_MUX(10, IOCON_TYPE_D, 0) /* PIO0_10 */
#define PIO0_10_PIO0_10 IOCON_MUX(10, IOCON_TYPE_D, 1) /* PIO0_10 */
#define SSP0_SCK_PIO0_10 IOCON_MUX(10, IOCON_TYPE_D, 2) /* PIO0_10 */
#define CT16B0_MAT2_PIO0_10 IOCON_MUX(10, IOCON_TYPE_D, 3) /* PIO0_10 */
#define TDI_PIO0_11 IOCON_MUX(11, IOCON_TYPE_A, 0) /* PIO0_11 */
#define PIO0_11_PIO0_11 IOCON_MUX(11, IOCON_TYPE_A, 1) /* PIO0_11 */
#define ADC_9_PIO0_11 IOCON_MUX(11, IOCON_TYPE_A, 2) /* PIO0_11 */
#define CT32B0_MAT3_PIO0_11 IOCON_MUX(11, IOCON_TYPE_A, 3) /* PIO0_11 */
#define U1_RTS_PIO0_11 IOCON_MUX(11, IOCON_TYPE_A, 4) /* PIO0_11 */
#define U1_SCLK_PIO0_11 IOCON_MUX(11, IOCON_TYPE_A, 5) /* PIO0_11 */
#define TMS_PIO0_12 IOCON_MUX(12, IOCON_TYPE_A, 0) /* PIO0_12 */
#define PIO0_12_PIO0_12 IOCON_MUX(12, IOCON_TYPE_A, 1) /* PIO0_12 */
#define ADC_8_PIO0_12 IOCON_MUX(12, IOCON_TYPE_A, 2) /* PIO0_12 */
#define CT32B1_CAP0_PIO0_12 IOCON_MUX(12, IOCON_TYPE_A, 3) /* PIO0_12 */
#define U1_CTS_PIO0_12 IOCON_MUX(12, IOCON_TYPE_A, 4) /* PIO0_12 */
#define PIO0_12_PIO0_12 IOCON_MUX(12, IOCON_TYPE_A, 5) /* PIO0_12 */
#define TDO_PIO0_13 IOCON_MUX(13, IOCON_TYPE_A, 0) /* PIO0_13 */
#define PIO0_13_PIO0_13 IOCON_MUX(13, IOCON_TYPE_A, 1) /* PIO0_13 */
#define ADC_7_PIO0_13 IOCON_MUX(13, IOCON_TYPE_A, 2) /* PIO0_13 */
#define CT32B1_MAT0_PIO0_13 IOCON_MUX(13, IOCON_TYPE_A, 3) /* PIO0_13 */
#define U1_RXD_PIO0_13 IOCON_MUX(13, IOCON_TYPE_A, 4) /* PIO0_13 */
#define PIO0_13_PIO0_13 IOCON_MUX(13, IOCON_TYPE_A, 5) /* PIO0_13 */
#define TRST_PIO0_14 IOCON_MUX(14, IOCON_TYPE_A, 0) /* PIO0_14 */
#define PIO0_14_PIO0_14 IOCON_MUX(14, IOCON_TYPE_A, 1) /* PIO0_14 */
#define ADC_6_PIO0_14 IOCON_MUX(14, IOCON_TYPE_A, 2) /* PIO0_14 */
#define CT32B1_MAT1_PIO0_14 IOCON_MUX(14, IOCON_TYPE_A, 3) /* PIO0_14 */
#define U1_TXD_PIO0_14 IOCON_MUX(14, IOCON_TYPE_A, 4) /* PIO0_14 */
#define SWDIO_PIO0_15 IOCON_MUX(15, IOCON_TYPE_A, 0) /* PIO0_15 */
#define PIO0_15_PIO0_15 IOCON_MUX(15, IOCON_TYPE_A, 1) /* PIO0_15 */
#define ADC_3_PIO0_15 IOCON_MUX(15, IOCON_TYPE_A, 2) /* PIO0_15 */
#define CT32B1_MAT2_PIO0_15 IOCON_MUX(15, IOCON_TYPE_A, 3) /* PIO0_15 */
#define WAKEUP_PIO0_16 IOCON_MUX(16, IOCON_TYPE_A, 0) /* PIO0_16 */
#define PIO0_16_PIO0_16 IOCON_MUX(16, IOCON_TYPE_A, 1) /* PIO0_16 */
#define ADC_2_PIO0_16 IOCON_MUX(16, IOCON_TYPE_A, 2) /* PIO0_16 */
#define CT32B1_MAT3_PIO0_16 IOCON_MUX(16, IOCON_TYPE_A, 3) /* PIO0_16 */
#define R_8_PIO0_16 IOCON_MUX(16, IOCON_TYPE_A, 4) /* PIO0_16 */
#define PIO0_17_PIO0_17 IOCON_MUX(17, IOCON_TYPE_D, 0) /* PIO0_17 */
#define U0_RTS_PIO0_17 IOCON_MUX(17, IOCON_TYPE_D, 1) /* PIO0_17 */
#define CT32B0_CAP0_PIO0_17 IOCON_MUX(17, IOCON_TYPE_D, 2) /* PIO0_17 */
#define U0_SCLK_PIO0_17 IOCON_MUX(17, IOCON_TYPE_D, 3) /* PIO0_17 */
#define PIO0_18_PIO0_18 IOCON_MUX(18, IOCON_TYPE_D, 0) /* PIO0_18 */
#define U0_RXD_PIO0_18 IOCON_MUX(18, IOCON_TYPE_D, 1) /* PIO0_18 */
#define CT32B0_MAT0_PIO0_18 IOCON_MUX(18, IOCON_TYPE_D, 2) /* PIO0_18 */
#define PIO0_19_PIO0_19 IOCON_MUX(19, IOCON_TYPE_D, 0) /* PIO0_19 */
#define U0_TXD_PIO0_19 IOCON_MUX(19, IOCON_TYPE_D, 1) /* PIO0_19 */
#define CT32B0_MAT1_PIO0_19 IOCON_MUX(19, IOCON_TYPE_D, 2) /* PIO0_19 */
#define PIO0_20_PIO0_20 IOCON_MUX(20, IOCON_TYPE_D, 0) /* PIO0_20 */
#define CT16B1_CAP0_PIO0_20 IOCON_MUX(20, IOCON_TYPE_D, 1) /* PIO0_20 */
#define U2_RXD_PIO0_20 IOCON_MUX(20, IOCON_TYPE_D, 2) /* PIO0_20 */
#define PIO0_21_PIO0_21 IOCON_MUX(21, IOCON_TYPE_D, 0) /* PIO0_21 */
#define CT16B1_MAT0_PIO0_21 IOCON_MUX(21, IOCON_TYPE_D, 1) /* PIO0_21 */
#define SSP1_MOSI_PIO0_21 IOCON_MUX(21, IOCON_TYPE_D, 2) /* PIO0_21 */
#define PIO0_22_PIO0_22 IOCON_MUX(22, IOCON_TYPE_A, 0) /* PIO0_22 */
#define ADC_11_PIO0_22 IOCON_MUX(22, IOCON_TYPE_A, 1) /* PIO0_22 */
#define CT16B1_CAP1_PIO0_22 IOCON_MUX(22, IOCON_TYPE_A, 2) /* PIO0_22 */
#define SSP1_MISO_PIO0_22 IOCON_MUX(22, IOCON_TYPE_A, 3) /* PIO0_22 */
#define PIO0_23_PIO0_23 IOCON_MUX(23, IOCON_TYPE_A, 0) /* PIO0_23 */
#define ADC_1_PIO0_23 IOCON_MUX(23, IOCON_TYPE_A, 1) /* PIO0_23 */
#define R_9_PIO0_23 IOCON_MUX(23, IOCON_TYPE_A, 2) /* PIO0_23 */
#define U0_RI_PIO0_23 IOCON_MUX(23, IOCON_TYPE_A, 3) /* PIO0_23 */
#define SSP1_SSEL_PIO0_23 IOCON_MUX(23, IOCON_TYPE_A, 4) /* PIO0_23 */
#define PIO1_0_PIO1_0 IOCON_MUX(24, IOCON_TYPE_D, 0) /* PIO1_0 */
#define CT32B1_MAT0_PIO1_0 IOCON_MUX(24, IOCON_TYPE_D, 1) /* PIO1_0 */
#define R_10_PIO1_0 IOCON_MUX(24, IOCON_TYPE_D, 2) /* PIO1_0 */
#define U2_TXD_PIO1_0 IOCON_MUX(24, IOCON_TYPE_D, 3) /* PIO1_0 */
#define PIO1_1_PIO1_1 IOCON_MUX(25, IOCON_TYPE_D, 0) /* PIO1_1 */
#define CT32B1_MAT1_PIO1_1 IOCON_MUX(25, IOCON_TYPE_D, 1) /* PIO1_1 */
#define R_11_PIO1_1 IOCON_MUX(25, IOCON_TYPE_D, 2) /* PIO1_1 */
#define U0_DTR_PIO1_1 IOCON_MUX(25, IOCON_TYPE_D, 3) /* PIO1_1 */
#define PIO1_2_PIO1_2 IOCON_MUX(26, IOCON_TYPE_D, 0) /* PIO1_2 */
#define CT32B1_MAT2_PIO1_2 IOCON_MUX(26, IOCON_TYPE_D, 1) /* PIO1_2 */
#define R_12_PIO1_2 IOCON_MUX(26, IOCON_TYPE_D, 2) /* PIO1_2 */
#define U1_RXD_PIO1_2 IOCON_MUX(26, IOCON_TYPE_D, 3) /* PIO1_2 */
#define PIO1_3_PIO1_3 IOCON_MUX(27, IOCON_TYPE_A, 0) /* PIO1_3 */
#define CT32B1_MAT3_PIO1_3 IOCON_MUX(27, IOCON_TYPE_A, 1) /* PIO1_3 */
#define R_13_PIO1_3 IOCON_MUX(27, IOCON_TYPE_A, 2) /* PIO1_3 */
#define I2C1_SDA_PIO1_3 IOCON_MUX(27, IOCON_TYPE_A, 3) /* PIO1_3 */
#define ADC_5_PIO1_3 IOCON_MUX(27, IOCON_TYPE_A, 4) /* PIO1_3 */
#define PIO1_4_PIO1_4 IOCON_MUX(28, IOCON_TYPE_D, 0) /* PIO1_4 */
#define CT32B1_CAP0_PIO1_4 IOCON_MUX(28, IOCON_TYPE_D, 1) /* PIO1_4 */
#define R_14_PIO1_4 IOCON_MUX(28, IOCON_TYPE_D, 2) /* PIO1_4 */
#define U0_DSR_PIO1_4 IOCON_MUX(28, IOCON_TYPE_D, 3) /* PIO1_4 */
#define PIO1_5_PIO1_5 IOCON_MUX(29, IOCON_TYPE_D, 0) /* PIO1_5 */
#define CT32B1_CAP1_PIO1_5 IOCON_MUX(29, IOCON_TYPE_D, 1) /* PIO1_5 */
#define R_15_PIO1_5 IOCON_MUX(29, IOCON_TYPE_D, 2) /* PIO1_5 */
#define U0_DCD_PIO1_5 IOCON_MUX(29, IOCON_TYPE_D, 3) /* PIO1_5 */
#define PIO1_6_PIO1_6 IOCON_MUX(30, IOCON_TYPE_D, 0) /* PIO1_6 */
#define R_16_PIO1_6 IOCON_MUX(30, IOCON_TYPE_D, 1) /* PIO1_6 */
#define U2_RXD_PIO1_6 IOCON_MUX(30, IOCON_TYPE_D, 2) /* PIO1_6 */
#define CT32B0_CAP1_PIO1_6 IOCON_MUX(30, IOCON_TYPE_D, 3) /* PIO1_6 */
#define PIO1_7_PIO1_7 IOCON_MUX(31, IOCON_TYPE_D, 0) /* PIO1_7 */
#define R_17_PIO1_7 IOCON_MUX(31, IOCON_TYPE_D, 1) /* PIO1_7 */
#define U2_CTS_PIO1_7 IOCON_MUX(31, IOCON_TYPE_D, 2) /* PIO1_7 */
#define CT16B1_CAP0_PIO1_7 IOCON_MUX(31, IOCON_TYPE_D, 3) /* PIO1_7 */
#define PIO1_8_PIO1_8 IOCON_MUX(32, IOCON_TYPE_D, 0) /* PIO1_8 */
#define R_18_PIO1_8 IOCON_MUX(32, IOCON_TYPE_D, 1) /* PIO1_8 */
#define U1_TXD_PIO1_8 IOCON_MUX(32, IOCON_TYPE_D, 2) /* PIO1_8 */
#define CT16B0_CAP0_PIO1_8 IOCON_MUX(32, IOCON_TYPE_D, 3) /* PIO1_8 */
#define PIO1_9_PIO1_9 IOCON_MUX(33, IOCON_TYPE_A, 0) /* PIO1_9 */
#define U0_CTS_PIO1_9 IOCON_MUX(33, IOCON_TYPE_A, 1) /* PIO1_9 */
#define CT16B1_MAT1_PIO1_9 IOCON_MUX(33, IOCON_TYPE_A, 2) /* PIO1_9 */
#define ADC_0_PIO1_9 IOCON_MUX(33, IOCON_TYPE_A, 3) /* PIO1_9 */
#define PIO1_10_PIO1_10 IOCON_MUX(34, IOCON_TYPE_D, 0) /* PIO1_10 */
#define U2_RTS_PIO1_10 IOCON_MUX(34, IOCON_TYPE_D, 1) /* PIO1_10 */
#define U2_SCLK_PIO1_10 IOCON_MUX(34, IOCON_TYPE_D, 2) /* PIO1_10 */
#define CT16B1_MAT0_PIO1_10 IOCON_MUX(34, IOCON_TYPE_D, 3) /* PIO1_10 */
#define PIO1_11_PIO1_11 IOCON_MUX(35, IOCON_TYPE_D, 0) /* PIO1_11 */
#define I2C1_SCL_PIO1_11 IOCON_MUX(35, IOCON_TYPE_D, 1) /* PIO1_11 */
#define CT16B0_MAT2_PIO1_11 IOCON_MUX(35, IOCON_TYPE_D, 2) /* PIO1_11 */
#define U0_RI_PIO1_11 IOCON_MUX(35, IOCON_TYPE_D, 3) /* PIO1_11 */
#define PIO1_12_PIO1_12 IOCON_MUX(36, IOCON_TYPE_D, 0) /* PIO1_12 */
#define SSP0_MOSI_PIO1_12 IOCON_MUX(36, IOCON_TYPE_D, 1) /* PIO1_12 */
#define CT16B0_MAT1_PIO1_12 IOCON_MUX(36, IOCON_TYPE_D, 2) /* PIO1_12 */
#define R_21_PIO1_12 IOCON_MUX(36, IOCON_TYPE_D, 3) /* PIO1_12 */
#define PIO1_13_PIO1_13 IOCON_MUX(37, IOCON_TYPE_D, 0) /* PIO1_13 */
#define U1_CTS_PIO1_13 IOCON_MUX(37, IOCON_TYPE_D, 1) /* PIO1_13 */
#define SCT0_OUT3_PIO1_13 IOCON_MUX(37, IOCON_TYPE_D, 2) /* PIO1_13 */
#define R_22_PIO1_13 IOCON_MUX(37, IOCON_TYPE_D, 3) /* PIO1_13 */
#define PIO1_14_PIO1_14 IOCON_MUX(38, IOCON_TYPE_D, 0) /* PIO1_14 */
#define I2C1_SDA_PIO1_14 IOCON_MUX(38, IOCON_TYPE_D, 1) /* PIO1_14 */
#define CT32B1_MAT2_PIO1_14 IOCON_MUX(38, IOCON_TYPE_D, 2) /* PIO1_14 */
#define R_23_PIO1_14 IOCON_MUX(38, IOCON_TYPE_D, 3) /* PIO1_14 */
#define PIO1_15_PIO1_15 IOCON_MUX(39, IOCON_TYPE_D, 0) /* PIO1_15 */
#define SSP0_SSEL_PIO1_15 IOCON_MUX(39, IOCON_TYPE_D, 1) /* PIO1_15 */
#define CT32B1_MAT3_PIO1_15 IOCON_MUX(39, IOCON_TYPE_D, 2) /* PIO1_15 */
#define R_24_PIO1_15 IOCON_MUX(39, IOCON_TYPE_D, 3) /* PIO1_15 */
#define PIO1_16_PIO1_16 IOCON_MUX(40, IOCON_TYPE_D, 0) /* PIO1_16 */
#define SSP0_MISO_PIO1_16 IOCON_MUX(40, IOCON_TYPE_D, 1) /* PIO1_16 */
#define CT16B0_MAT0_PIO1_16 IOCON_MUX(40, IOCON_TYPE_D, 2) /* PIO1_16 */
#define R_25_PIO1_16 IOCON_MUX(40, IOCON_TYPE_D, 3) /* PIO1_16 */
#define PIO1_17_PIO1_17 IOCON_MUX(41, IOCON_TYPE_D, 0) /* PIO1_17 */
#define CT16B0_CAP2_PIO1_17 IOCON_MUX(41, IOCON_TYPE_D, 1) /* PIO1_17 */
#define U0_RXD_PIO1_17 IOCON_MUX(41, IOCON_TYPE_D, 2) /* PIO1_17 */
#define R_26_PIO1_17 IOCON_MUX(41, IOCON_TYPE_D, 3) /* PIO1_17 */
#define PIO1_18_PIO1_18 IOCON_MUX(42, IOCON_TYPE_D, 0) /* PIO1_18 */
#define CT16B1_CAP1_PIO1_18 IOCON_MUX(42, IOCON_TYPE_D, 1) /* PIO1_18 */
#define U0_TXD_PIO1_18 IOCON_MUX(42, IOCON_TYPE_D, 2) /* PIO1_18 */
#define R_27_PIO1_18 IOCON_MUX(42, IOCON_TYPE_D, 3) /* PIO1_18 */
#define PIO1_19_PIO1_19 IOCON_MUX(43, IOCON_TYPE_D, 0) /* PIO1_19 */
#define U2_CTS_PIO1_19 IOCON_MUX(43, IOCON_TYPE_D, 1) /* PIO1_19 */
#define SCT0_OUT0_PIO1_19 IOCON_MUX(43, IOCON_TYPE_D, 2) /* PIO1_19 */
#define R_28_PIO1_19 IOCON_MUX(43, IOCON_TYPE_D, 3) /* PIO1_19 */
#define PIO1_20_PIO1_20 IOCON_MUX(44, IOCON_TYPE_D, 0) /* PIO1_20 */
#define U0_DSR_PIO1_20 IOCON_MUX(44, IOCON_TYPE_D, 1) /* PIO1_20 */
#define SSP1_SCK_PIO1_20 IOCON_MUX(44, IOCON_TYPE_D, 2) /* PIO1_20 */
#define CT16B0_MAT0_PIO1_20 IOCON_MUX(44, IOCON_TYPE_D, 3) /* PIO1_20 */
#define PIO1_21_PIO1_21 IOCON_MUX(45, IOCON_TYPE_D, 0) /* PIO1_21 */
#define U0_DCD_PIO1_21 IOCON_MUX(45, IOCON_TYPE_D, 1) /* PIO1_21 */
#define SSP1_MISO_PIO1_21 IOCON_MUX(45, IOCON_TYPE_D, 2) /* PIO1_21 */
#define CT16B0_CAP1_PIO1_21 IOCON_MUX(45, IOCON_TYPE_D, 3) /* PIO1_21 */
#define PIO1_22_PIO1_22 IOCON_MUX(46, IOCON_TYPE_A, 0) /* PIO1_22 */
#define SSP1_MOSI_PIO1_22 IOCON_MUX(46, IOCON_TYPE_A, 1) /* PIO1_22 */
#define CT32B1_CAP1_PIO1_22 IOCON_MUX(46, IOCON_TYPE_A, 2) /* PIO1_22 */
#define ADC_4_PIO1_22 IOCON_MUX(46, IOCON_TYPE_A, 3) /* PIO1_22 */
#define R_29_PIO1_22 IOCON_MUX(46, IOCON_TYPE_A, 4) /* PIO1_22 */
#define PIO1_23_PIO1_23 IOCON_MUX(47, IOCON_TYPE_D, 0) /* PIO1_23 */
#define CT16B1_MAT1_PIO1_23 IOCON_MUX(47, IOCON_TYPE_D, 1) /* PIO1_23 */
#define SSP1_SSEL_PIO1_23 IOCON_MUX(47, IOCON_TYPE_D, 2) /* PIO1_23 */
#define U2_TXD_PIO1_23 IOCON_MUX(47, IOCON_TYPE_D, 3) /* PIO1_23 */
#define PIO1_24_PIO1_24 IOCON_MUX(48, IOCON_TYPE_D, 0) /* PIO1_24 */
#define CT32B0_MAT0_PIO1_24 IOCON_MUX(48, IOCON_TYPE_D, 1) /* PIO1_24 */
#define I2C1_SDA_PIO1_24 IOCON_MUX(48, IOCON_TYPE_D, 2) /* PIO1_24 */
#define PIO1_25_PIO1_25 IOCON_MUX(49, IOCON_TYPE_D, 0) /* PIO1_25 */
#define U2_RTS_PIO1_25 IOCON_MUX(49, IOCON_TYPE_D, 1) /* PIO1_25 */
#define U2_SCLK_PIO1_25 IOCON_MUX(49, IOCON_TYPE_D, 2) /* PIO1_25 */
#define SCT0_IN0_PIO1_25 IOCON_MUX(49, IOCON_TYPE_D, 3) /* PIO1_25 */
#define R_30_PIO1_25 IOCON_MUX(49, IOCON_TYPE_D, 4) /* PIO1_25 */
#define PIO1_26_PIO1_26 IOCON_MUX(50, IOCON_TYPE_D, 0) /* PIO1_26 */
#define CT32B0_MAT2_PIO1_26 IOCON_MUX(50, IOCON_TYPE_D, 1) /* PIO1_26 */
#define U0_RXD_PIO1_26 IOCON_MUX(50, IOCON_TYPE_D, 2) /* PIO1_26 */
#define R_19_PIO1_26 IOCON_MUX(50, IOCON_TYPE_D, 3) /* PIO1_26 */
#define PIO1_27_PIO1_27 IOCON_MUX(51, IOCON_TYPE_D, 0) /* PIO1_27 */
#define CT32B0_MAT3_PIO1_27 IOCON_MUX(51, IOCON_TYPE_D, 1) /* PIO1_27 */
#define U0_TXD_PIO1_27 IOCON_MUX(51, IOCON_TYPE_D, 2) /* PIO1_27 */
#define R_20_PIO1_27 IOCON_MUX(51, IOCON_TYPE_D, 3) /* PIO1_27 */
#define SSP1_SCK_PIO1_27 IOCON_MUX(51, IOCON_TYPE_D, 4) /* PIO1_27 */
#define PIO1_28_PIO1_28 IOCON_MUX(52, IOCON_TYPE_D, 0) /* PIO1_28 */
#define CT32B0_CAP0_PIO1_28 IOCON_MUX(52, IOCON_TYPE_D, 1) /* PIO1_28 */
#define U0_SCLK_PIO1_28 IOCON_MUX(52, IOCON_TYPE_D, 2) /* PIO1_28 */
#define U0_RTS_PIO1_28 IOCON_MUX(52, IOCON_TYPE_D, 3) /* PIO1_28 */
#define PIO1_29_PIO1_29 IOCON_MUX(53, IOCON_TYPE_A, 0) /* PIO1_29 */
#define SSP0_SCK_PIO1_29 IOCON_MUX(53, IOCON_TYPE_A, 1) /* PIO1_29 */
#define CT32B0_CAP1_PIO1_29 IOCON_MUX(53, IOCON_TYPE_A, 2) /* PIO1_29 */
#define U0_DTRn_PIO1_29 IOCON_MUX(53, IOCON_TYPE_A, 3) /* PIO1_29 */
#define ADC_10_PIO1_29 IOCON_MUX(53, IOCON_TYPE_A, 4) /* PIO1_29 */
#define PIO1_30_PIO1_30 IOCON_MUX(54, IOCON_TYPE_D, 0) /* PIO1_30 */
#define I2C1_SCL_PIO1_30 IOCON_MUX(54, IOCON_TYPE_D, 1) /* PIO1_30 */
#define SCT0_IN3_PIO1_30 IOCON_MUX(54, IOCON_TYPE_D, 2) /* PIO1_30 */
#define R_31_PIO1_30 IOCON_MUX(54, IOCON_TYPE_D, 3) /* PIO1_30 */
#define PIO1_31_PIO1_31 IOCON_MUX(55, IOCON_TYPE_D, 0) /* PIO1_31 */
#define PIO2_0_PIO2_0 IOCON_MUX(60, IOCON_TYPE_A, 0) /* PIO2_0 */
#define XTALIN_PIO2_0 IOCON_MUX(60, IOCON_TYPE_A, 1) /* PIO2_0 */
#define PIO2_1_PIO2_1 IOCON_MUX(61, IOCON_TYPE_A, 0) /* PIO2_1 */
#define XTALOUT_PIO2_1 IOCON_MUX(61, IOCON_TYPE_A, 1) /* PIO2_1 */
#define PIO2_2_PIO2_2 IOCON_MUX(63, IOCON_TYPE_D, 0) /* PIO2_2 */
#define U3_RTS_PIO2_2 IOCON_MUX(63, IOCON_TYPE_D, 1) /* PIO2_2 */
#define U3_SCLK_PIO2_2 IOCON_MUX(63, IOCON_TYPE_D, 2) /* PIO2_2 */
#define SCT0_OUT1_PIO2_2 IOCON_MUX(63, IOCON_TYPE_D, 3) /* PIO2_2 */
#define PIO2_3_PIO2_3 IOCON_MUX(64, IOCON_TYPE_D, 0) /* PIO2_3 */
#define U3_RXD_PIO2_3 IOCON_MUX(64, IOCON_TYPE_D, 1) /* PIO2_3 */
#define CT32B0_MAT1_PIO2_3 IOCON_MUX(64, IOCON_TYPE_D, 2) /* PIO2_3 */
#define PIO2_4_PIO2_4 IOCON_MUX(65, IOCON_TYPE_D, 0) /* PIO2_4 */
#define U3_TXD_PIO2_4 IOCON_MUX(65, IOCON_TYPE_D, 1) /* PIO2_4 */
#define CT32B0_MAT2_PIO2_4 IOCON_MUX(65, IOCON_TYPE_D, 2) /* PIO2_4 */
#define PIO2_5_PIO2_5 IOCON_MUX(66, IOCON_TYPE_D, 0) /* PIO2_5 */
#define U3_CTS_PIO2_5 IOCON_MUX(66, IOCON_TYPE_D, 1) /* PIO2_5 */
#define SCT0_IN1_PIO2_5 IOCON_MUX(66, IOCON_TYPE_D, 2) /* PIO2_5 */
#define PIO2_6_PIO2_6 IOCON_MUX(67, IOCON_TYPE_D, 0) /* PIO2_6 */
#define U1_RTS_PIO2_6 IOCON_MUX(67, IOCON_TYPE_D, 1) /* PIO2_6 */
#define U1_SCLK_PIO2_6 IOCON_MUX(67, IOCON_TYPE_D, 2) /* PIO2_6 */
#define SCT0_IN2_PIO2_6 IOCON_MUX(67, IOCON_TYPE_D, 3) /* PIO2_6 */
#define PIO2_7_PIO2_7 IOCON_MUX(68, IOCON_TYPE_D, 0) /* PIO2_7 */
#define SSP0_SCK_PIO2_7 IOCON_MUX(68, IOCON_TYPE_D, 1) /* PIO2_7 */
#define SCT0_OUT2_PIO2_7 IOCON_MUX(68, IOCON_TYPE_D, 2) /* PIO2_7 */
#define PIO2_8_PIO2_8 IOCON_MUX(69, IOCON_TYPE_D, 0) /* PIO2_8 */
#define SCT1_IN0_PIO2_8 IOCON_MUX(69, IOCON_TYPE_D, 1) /* PIO2_8 */
#define PIO2_9_PIO2_9 IOCON_MUX(70, IOCON_TYPE_D, 0) /* PIO2_9 */
#define SCT1_IN1_PIO2_9 IOCON_MUX(70, IOCON_TYPE_D, 1) /* PIO2_9 */
#define PIO2_10_PIO2_10 IOCON_MUX(71, IOCON_TYPE_D, 0) /* PIO2_10 */
#define U4_RTS_PIO2_10 IOCON_MUX(71, IOCON_TYPE_D, 1) /* PIO2_10 */
#define U4_SCLK_PIO2_10 IOCON_MUX(71, IOCON_TYPE_D, 2) /* PIO2_10 */
#define PIO2_11_PIO2_11 IOCON_MUX(72, IOCON_TYPE_D, 0) /* PIO2_11 */
#define U4_RXD_PIO2_11 IOCON_MUX(72, IOCON_TYPE_D, 1) /* PIO2_11 */
#define PIO2_12_PIO2_12 IOCON_MUX(73, IOCON_TYPE_D, 0) /* PIO2_12 */
#define U4_TXD_PIO2_12 IOCON_MUX(73, IOCON_TYPE_D, 1) /* PIO2_12 */
#define PIO2_13_PIO2_13 IOCON_MUX(74, IOCON_TYPE_D, 0) /* PIO2_13 */
#define U4_CTS_PIO2_13 IOCON_MUX(74, IOCON_TYPE_D, 1) /* PIO2_13 */
#define PIO2_14_PIO2_14 IOCON_MUX(75, IOCON_TYPE_D, 0) /* PIO2_14 */
#define SCT1_IN2_PIO2_14 IOCON_MUX(75, IOCON_TYPE_D, 1) /* PIO2_14 */
#define PIO2_15_PIO2_15 IOCON_MUX(76, IOCON_TYPE_D, 0) /* PIO2_15 */
#define SCT1_IN3_PIO2_15 IOCON_MUX(76, IOCON_TYPE_D, 1) /* PIO2_15 */
#define PIO2_16_PIO2_16 IOCON_MUX(77, IOCON_TYPE_D, 0) /* PIO2_16 */
#define SCT1_OUT0_PIO2_16 IOCON_MUX(77, IOCON_TYPE_D, 1) /* PIO2_16 */
#define PIO2_17_PIO2_17 IOCON_MUX(78, IOCON_TYPE_D, 0) /* PIO2_17 */
#define SCT1_OUT1_PIO2_17 IOCON_MUX(78, IOCON_TYPE_D, 1) /* PIO2_17 */
#define PIO2_18_PIO2_18 IOCON_MUX(79, IOCON_TYPE_D, 0) /* PIO2_18 */
#define SCT1_OUT2_PIO2_18 IOCON_MUX(79, IOCON_TYPE_D, 1) /* PIO2_18 */
#define PIO2_19_PIO2_19 IOCON_MUX(80, IOCON_TYPE_D, 0) /* PIO2_19 */
#define SCT1_OUT3_PIO2_19 IOCON_MUX(80, IOCON_TYPE_D, 1) /* PIO2_19 */
#define PIO2_20_PIO2_20 IOCON_MUX(81, IOCON_TYPE_D, 0) /* PIO2_20 */
#define PIO2_21_PIO2_21 IOCON_MUX(82, IOCON_TYPE_D, 0) /* PIO2_21 */
#define PIO2_22_PIO2_22 IOCON_MUX(83, IOCON_TYPE_D, 0) /* PIO2_22 */
#define PIO2_23_PIO2_23 IOCON_MUX(84, IOCON_TYPE_D, 0) /* PIO2_23 */

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_LPC11U6X_PINCTRL_H_ */
```

## 3.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Seagate Technology LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 59 行

没有上拉／下拉电阻（Pull Resistor）。

### 注释 3：原第 60 行

启用下拉电阻（Pull-down Resistor）。

### 注释 4：原第 61 行

启用上拉电阻（Pull-up Resistor）。

### 注释 5：原第 62 行

中继模式（Repeater Mode）。

### 注释 6：原第 64 行

启用迟滞（Hysteresis）。

### 注释 7：原第 66 行

反转输入极性（Invert Input Polarity）。

### 注释 8：原第 68 行

仅适用于模拟引脚（Analog Pins）。

### 注释 9：原第 69 行

启用模拟输入模式（Analog Input Mode）。

### 注释 10：原第 70 行

启用数字输入输出模式（Digital I/O Mode）。

### 注释 11：原第 71 行

禁用噪声滤波（Noise Filtering）。

### 注释 12：原第 73 行

仅适用于开漏引脚（Open-drain Pins），如 I2C。

### 注释 13：原第 74 行

I2C 标准模式／快速模式（Standard Mode/Fast-mode）。

### 注释 14：原第 75 行

通用输入输出（GPIO）功能。

### 注释 15：原第 76 行

I2C 增强快速模式（Fast-mode Plus）。

### 注释 16：原第 78 行

启用开漏模式（Open-drain Mode）。

### 注释 17：原第 80 行

数字滤波模式（Digital Filter Mode）可丢弃短于 1、2 或 3 个时钟周期的输入脉冲。

### 注释 18：原第 84 行

不使用输入滤波（No Input Filter）。

### 注释 19：原第 89 行

时钟分频系数（Clock Divisor）。

### 注释 20：原第 101 行

LPC 引脚控制驱动（Pin Control Driver）用于选择引脚复用（Pinmux）的引脚控制定义。

### 注释 21：原第 115 行

引脚（Pin）：`PIO0_0`。

### 注释 22：原第 116 行

引脚（Pin）：`PIO0_0`。

### 注释 23：原第 117 行

引脚（Pin）：`PIO0_1`。

### 注释 24：原第 118 行

引脚（Pin）：`PIO0_1`。

### 注释 25：原第 119 行

引脚（Pin）：`PIO0_1`。

### 注释 26：原第 120 行

引脚（Pin）：`PIO0_1`。

### 注释 27：原第 121 行

引脚（Pin）：`PIO0_2`。

### 注释 28：原第 122 行

引脚（Pin）：`PIO0_2`。

### 注释 29：原第 123 行

引脚（Pin）：`PIO0_2`。

### 注释 30：原第 124 行

引脚（Pin）：`PIO0_2`。

### 注释 31：原第 125 行

引脚（Pin）：`PIO0_3`。

### 注释 32：原第 126 行

引脚（Pin）：`PIO0_3`。

### 注释 33：原第 127 行

引脚（Pin）：`PIO0_3`。

### 注释 34：原第 128 行

引脚（Pin）：`PIO0_4`。

### 注释 35：原第 129 行

引脚（Pin）：`PIO0_4`。

### 注释 36：原第 130 行

引脚（Pin）：`PIO0_4`。

### 注释 37：原第 131 行

引脚（Pin）：`PIO0_5`。

### 注释 38：原第 132 行

引脚（Pin）：`PIO0_5`。

### 注释 39：原第 133 行

引脚（Pin）：`PIO0_5`。

### 注释 40：原第 134 行

引脚（Pin）：`PIO0_6`。

### 注释 41：原第 135 行

引脚（Pin）：`PIO0_6`。

### 注释 42：原第 136 行

引脚（Pin）：`PIO0_6`。

### 注释 43：原第 137 行

引脚（Pin）：`PIO0_6`。

### 注释 44：原第 138 行

引脚（Pin）：`PIO0_7`。

### 注释 45：原第 139 行

引脚（Pin）：`PIO0_7`。

### 注释 46：原第 140 行

引脚（Pin）：`PIO0_7`。

### 注释 47：原第 141 行

引脚（Pin）：`PIO0_7`。

### 注释 48：原第 142 行

引脚（Pin）：`PIO0_8`。

### 注释 49：原第 143 行

引脚（Pin）：`PIO0_8`。

### 注释 50：原第 144 行

引脚（Pin）：`PIO0_8`。

### 注释 51：原第 145 行

引脚（Pin）：`PIO0_8`。

### 注释 52：原第 146 行

引脚（Pin）：`PIO0_9`。

### 注释 53：原第 147 行

引脚（Pin）：`PIO0_9`。

### 注释 54：原第 148 行

引脚（Pin）：`PIO0_9`。

### 注释 55：原第 149 行

引脚（Pin）：`PIO0_9`。

### 注释 56：原第 150 行

引脚（Pin）：`PIO0_10`。

### 注释 57：原第 151 行

引脚（Pin）：`PIO0_10`。

### 注释 58：原第 152 行

引脚（Pin）：`PIO0_10`。

### 注释 59：原第 153 行

引脚（Pin）：`PIO0_10`。

### 注释 60：原第 154 行

引脚（Pin）：`PIO0_11`。

### 注释 61：原第 155 行

引脚（Pin）：`PIO0_11`。

### 注释 62：原第 156 行

引脚（Pin）：`PIO0_11`。

### 注释 63：原第 157 行

引脚（Pin）：`PIO0_11`。

### 注释 64：原第 158 行

引脚（Pin）：`PIO0_11`。

### 注释 65：原第 159 行

引脚（Pin）：`PIO0_11`。

### 注释 66：原第 160 行

引脚（Pin）：`PIO0_12`。

### 注释 67：原第 161 行

引脚（Pin）：`PIO0_12`。

### 注释 68：原第 162 行

引脚（Pin）：`PIO0_12`。

### 注释 69：原第 163 行

引脚（Pin）：`PIO0_12`。

### 注释 70：原第 164 行

引脚（Pin）：`PIO0_12`。

### 注释 71：原第 165 行

引脚（Pin）：`PIO0_12`。

### 注释 72：原第 166 行

引脚（Pin）：`PIO0_13`。

### 注释 73：原第 167 行

引脚（Pin）：`PIO0_13`。

### 注释 74：原第 168 行

引脚（Pin）：`PIO0_13`。

### 注释 75：原第 169 行

引脚（Pin）：`PIO0_13`。

### 注释 76：原第 170 行

引脚（Pin）：`PIO0_13`。

### 注释 77：原第 171 行

引脚（Pin）：`PIO0_13`。

### 注释 78：原第 172 行

引脚（Pin）：`PIO0_14`。

### 注释 79：原第 173 行

引脚（Pin）：`PIO0_14`。

### 注释 80：原第 174 行

引脚（Pin）：`PIO0_14`。

### 注释 81：原第 175 行

引脚（Pin）：`PIO0_14`。

### 注释 82：原第 176 行

引脚（Pin）：`PIO0_14`。

### 注释 83：原第 177 行

引脚（Pin）：`PIO0_15`。

### 注释 84：原第 178 行

引脚（Pin）：`PIO0_15`。

### 注释 85：原第 179 行

引脚（Pin）：`PIO0_15`。

### 注释 86：原第 180 行

引脚（Pin）：`PIO0_15`。

### 注释 87：原第 181 行

引脚（Pin）：`PIO0_16`。

### 注释 88：原第 182 行

引脚（Pin）：`PIO0_16`。

### 注释 89：原第 183 行

引脚（Pin）：`PIO0_16`。

### 注释 90：原第 184 行

引脚（Pin）：`PIO0_16`。

### 注释 91：原第 185 行

引脚（Pin）：`PIO0_16`。

### 注释 92：原第 186 行

引脚（Pin）：`PIO0_17`。

### 注释 93：原第 187 行

引脚（Pin）：`PIO0_17`。

### 注释 94：原第 188 行

引脚（Pin）：`PIO0_17`。

### 注释 95：原第 189 行

引脚（Pin）：`PIO0_17`。

### 注释 96：原第 190 行

引脚（Pin）：`PIO0_18`。

### 注释 97：原第 191 行

引脚（Pin）：`PIO0_18`。

### 注释 98：原第 192 行

引脚（Pin）：`PIO0_18`。

### 注释 99：原第 193 行

引脚（Pin）：`PIO0_19`。

### 注释 100：原第 194 行

引脚（Pin）：`PIO0_19`。

### 注释 101：原第 195 行

引脚（Pin）：`PIO0_19`。

### 注释 102：原第 196 行

引脚（Pin）：`PIO0_20`。

### 注释 103：原第 197 行

引脚（Pin）：`PIO0_20`。

### 注释 104：原第 198 行

引脚（Pin）：`PIO0_20`。

### 注释 105：原第 199 行

引脚（Pin）：`PIO0_21`。

### 注释 106：原第 200 行

引脚（Pin）：`PIO0_21`。

### 注释 107：原第 201 行

引脚（Pin）：`PIO0_21`。

### 注释 108：原第 202 行

引脚（Pin）：`PIO0_22`。

### 注释 109：原第 203 行

引脚（Pin）：`PIO0_22`。

### 注释 110：原第 204 行

引脚（Pin）：`PIO0_22`。

### 注释 111：原第 205 行

引脚（Pin）：`PIO0_22`。

### 注释 112：原第 206 行

引脚（Pin）：`PIO0_23`。

### 注释 113：原第 207 行

引脚（Pin）：`PIO0_23`。

### 注释 114：原第 208 行

引脚（Pin）：`PIO0_23`。

### 注释 115：原第 209 行

引脚（Pin）：`PIO0_23`。

### 注释 116：原第 210 行

引脚（Pin）：`PIO0_23`。

### 注释 117：原第 211 行

引脚（Pin）：`PIO1_0`。

### 注释 118：原第 212 行

引脚（Pin）：`PIO1_0`。

### 注释 119：原第 213 行

引脚（Pin）：`PIO1_0`。

### 注释 120：原第 214 行

引脚（Pin）：`PIO1_0`。

### 注释 121：原第 215 行

引脚（Pin）：`PIO1_1`。

### 注释 122：原第 216 行

引脚（Pin）：`PIO1_1`。

### 注释 123：原第 217 行

引脚（Pin）：`PIO1_1`。

### 注释 124：原第 218 行

引脚（Pin）：`PIO1_1`。

### 注释 125：原第 219 行

引脚（Pin）：`PIO1_2`。

### 注释 126：原第 220 行

引脚（Pin）：`PIO1_2`。

### 注释 127：原第 221 行

引脚（Pin）：`PIO1_2`。

### 注释 128：原第 222 行

引脚（Pin）：`PIO1_2`。

### 注释 129：原第 223 行

引脚（Pin）：`PIO1_3`。

### 注释 130：原第 224 行

引脚（Pin）：`PIO1_3`。

### 注释 131：原第 225 行

引脚（Pin）：`PIO1_3`。

### 注释 132：原第 226 行

引脚（Pin）：`PIO1_3`。

### 注释 133：原第 227 行

引脚（Pin）：`PIO1_3`。

### 注释 134：原第 228 行

引脚（Pin）：`PIO1_4`。

### 注释 135：原第 229 行

引脚（Pin）：`PIO1_4`。

### 注释 136：原第 230 行

引脚（Pin）：`PIO1_4`。

### 注释 137：原第 231 行

引脚（Pin）：`PIO1_4`。

### 注释 138：原第 232 行

引脚（Pin）：`PIO1_5`。

### 注释 139：原第 233 行

引脚（Pin）：`PIO1_5`。

### 注释 140：原第 234 行

引脚（Pin）：`PIO1_5`。

### 注释 141：原第 235 行

引脚（Pin）：`PIO1_5`。

### 注释 142：原第 236 行

引脚（Pin）：`PIO1_6`。

### 注释 143：原第 237 行

引脚（Pin）：`PIO1_6`。

### 注释 144：原第 238 行

引脚（Pin）：`PIO1_6`。

### 注释 145：原第 239 行

引脚（Pin）：`PIO1_6`。

### 注释 146：原第 240 行

引脚（Pin）：`PIO1_7`。

### 注释 147：原第 241 行

引脚（Pin）：`PIO1_7`。

### 注释 148：原第 242 行

引脚（Pin）：`PIO1_7`。

### 注释 149：原第 243 行

引脚（Pin）：`PIO1_7`。

### 注释 150：原第 244 行

引脚（Pin）：`PIO1_8`。

### 注释 151：原第 245 行

引脚（Pin）：`PIO1_8`。

### 注释 152：原第 246 行

引脚（Pin）：`PIO1_8`。

### 注释 153：原第 247 行

引脚（Pin）：`PIO1_8`。

### 注释 154：原第 248 行

引脚（Pin）：`PIO1_9`。

### 注释 155：原第 249 行

引脚（Pin）：`PIO1_9`。

### 注释 156：原第 250 行

引脚（Pin）：`PIO1_9`。

### 注释 157：原第 251 行

引脚（Pin）：`PIO1_9`。

### 注释 158：原第 252 行

引脚（Pin）：`PIO1_10`。

### 注释 159：原第 253 行

引脚（Pin）：`PIO1_10`。

### 注释 160：原第 254 行

引脚（Pin）：`PIO1_10`。

### 注释 161：原第 255 行

引脚（Pin）：`PIO1_10`。

### 注释 162：原第 256 行

引脚（Pin）：`PIO1_11`。

### 注释 163：原第 257 行

引脚（Pin）：`PIO1_11`。

### 注释 164：原第 258 行

引脚（Pin）：`PIO1_11`。

### 注释 165：原第 259 行

引脚（Pin）：`PIO1_11`。

### 注释 166：原第 260 行

引脚（Pin）：`PIO1_12`。

### 注释 167：原第 261 行

引脚（Pin）：`PIO1_12`。

### 注释 168：原第 262 行

引脚（Pin）：`PIO1_12`。

### 注释 169：原第 263 行

引脚（Pin）：`PIO1_12`。

### 注释 170：原第 264 行

引脚（Pin）：`PIO1_13`。

### 注释 171：原第 265 行

引脚（Pin）：`PIO1_13`。

### 注释 172：原第 266 行

引脚（Pin）：`PIO1_13`。

### 注释 173：原第 267 行

引脚（Pin）：`PIO1_13`。

### 注释 174：原第 268 行

引脚（Pin）：`PIO1_14`。

### 注释 175：原第 269 行

引脚（Pin）：`PIO1_14`。

### 注释 176：原第 270 行

引脚（Pin）：`PIO1_14`。

### 注释 177：原第 271 行

引脚（Pin）：`PIO1_14`。

### 注释 178：原第 272 行

引脚（Pin）：`PIO1_15`。

### 注释 179：原第 273 行

引脚（Pin）：`PIO1_15`。

### 注释 180：原第 274 行

引脚（Pin）：`PIO1_15`。

### 注释 181：原第 275 行

引脚（Pin）：`PIO1_15`。

### 注释 182：原第 276 行

引脚（Pin）：`PIO1_16`。

### 注释 183：原第 277 行

引脚（Pin）：`PIO1_16`。

### 注释 184：原第 278 行

引脚（Pin）：`PIO1_16`。

### 注释 185：原第 279 行

引脚（Pin）：`PIO1_16`。

### 注释 186：原第 280 行

引脚（Pin）：`PIO1_17`。

### 注释 187：原第 281 行

引脚（Pin）：`PIO1_17`。

### 注释 188：原第 282 行

引脚（Pin）：`PIO1_17`。

### 注释 189：原第 283 行

引脚（Pin）：`PIO1_17`。

### 注释 190：原第 284 行

引脚（Pin）：`PIO1_18`。

### 注释 191：原第 285 行

引脚（Pin）：`PIO1_18`。

### 注释 192：原第 286 行

引脚（Pin）：`PIO1_18`。

### 注释 193：原第 287 行

引脚（Pin）：`PIO1_18`。

### 注释 194：原第 288 行

引脚（Pin）：`PIO1_19`。

### 注释 195：原第 289 行

引脚（Pin）：`PIO1_19`。

### 注释 196：原第 290 行

引脚（Pin）：`PIO1_19`。

### 注释 197：原第 291 行

引脚（Pin）：`PIO1_19`。

### 注释 198：原第 292 行

引脚（Pin）：`PIO1_20`。

### 注释 199：原第 293 行

引脚（Pin）：`PIO1_20`。

### 注释 200：原第 294 行

引脚（Pin）：`PIO1_20`。

### 注释 201：原第 295 行

引脚（Pin）：`PIO1_20`。

### 注释 202：原第 296 行

引脚（Pin）：`PIO1_21`。

### 注释 203：原第 297 行

引脚（Pin）：`PIO1_21`。

### 注释 204：原第 298 行

引脚（Pin）：`PIO1_21`。

### 注释 205：原第 299 行

引脚（Pin）：`PIO1_21`。

### 注释 206：原第 300 行

引脚（Pin）：`PIO1_22`。

### 注释 207：原第 301 行

引脚（Pin）：`PIO1_22`。

### 注释 208：原第 302 行

引脚（Pin）：`PIO1_22`。

### 注释 209：原第 303 行

引脚（Pin）：`PIO1_22`。

### 注释 210：原第 304 行

引脚（Pin）：`PIO1_22`。

### 注释 211：原第 305 行

引脚（Pin）：`PIO1_23`。

### 注释 212：原第 306 行

引脚（Pin）：`PIO1_23`。

### 注释 213：原第 307 行

引脚（Pin）：`PIO1_23`。

### 注释 214：原第 308 行

引脚（Pin）：`PIO1_23`。

### 注释 215：原第 309 行

引脚（Pin）：`PIO1_24`。

### 注释 216：原第 310 行

引脚（Pin）：`PIO1_24`。

### 注释 217：原第 311 行

引脚（Pin）：`PIO1_24`。

### 注释 218：原第 312 行

引脚（Pin）：`PIO1_25`。

### 注释 219：原第 313 行

引脚（Pin）：`PIO1_25`。

### 注释 220：原第 314 行

引脚（Pin）：`PIO1_25`。

### 注释 221：原第 315 行

引脚（Pin）：`PIO1_25`。

### 注释 222：原第 316 行

引脚（Pin）：`PIO1_25`。

### 注释 223：原第 317 行

引脚（Pin）：`PIO1_26`。

### 注释 224：原第 318 行

引脚（Pin）：`PIO1_26`。

### 注释 225：原第 319 行

引脚（Pin）：`PIO1_26`。

### 注释 226：原第 320 行

引脚（Pin）：`PIO1_26`。

### 注释 227：原第 321 行

引脚（Pin）：`PIO1_27`。

### 注释 228：原第 322 行

引脚（Pin）：`PIO1_27`。

### 注释 229：原第 323 行

引脚（Pin）：`PIO1_27`。

### 注释 230：原第 324 行

引脚（Pin）：`PIO1_27`。

### 注释 231：原第 325 行

引脚（Pin）：`PIO1_27`。

### 注释 232：原第 326 行

引脚（Pin）：`PIO1_28`。

### 注释 233：原第 327 行

引脚（Pin）：`PIO1_28`。

### 注释 234：原第 328 行

引脚（Pin）：`PIO1_28`。

### 注释 235：原第 329 行

引脚（Pin）：`PIO1_28`。

### 注释 236：原第 330 行

引脚（Pin）：`PIO1_29`。

### 注释 237：原第 331 行

引脚（Pin）：`PIO1_29`。

### 注释 238：原第 332 行

引脚（Pin）：`PIO1_29`。

### 注释 239：原第 333 行

引脚（Pin）：`PIO1_29`。

### 注释 240：原第 334 行

引脚（Pin）：`PIO1_29`。

### 注释 241：原第 335 行

引脚（Pin）：`PIO1_30`。

### 注释 242：原第 336 行

引脚（Pin）：`PIO1_30`。

### 注释 243：原第 337 行

引脚（Pin）：`PIO1_30`。

### 注释 244：原第 338 行

引脚（Pin）：`PIO1_30`。

### 注释 245：原第 339 行

引脚（Pin）：`PIO1_31`。

### 注释 246：原第 340 行

引脚（Pin）：`PIO2_0`。

### 注释 247：原第 341 行

引脚（Pin）：`PIO2_0`。

### 注释 248：原第 342 行

引脚（Pin）：`PIO2_1`。

### 注释 249：原第 343 行

引脚（Pin）：`PIO2_1`。

### 注释 250：原第 344 行

引脚（Pin）：`PIO2_2`。

### 注释 251：原第 345 行

引脚（Pin）：`PIO2_2`。

### 注释 252：原第 346 行

引脚（Pin）：`PIO2_2`。

### 注释 253：原第 347 行

引脚（Pin）：`PIO2_2`。

### 注释 254：原第 348 行

引脚（Pin）：`PIO2_3`。

### 注释 255：原第 349 行

引脚（Pin）：`PIO2_3`。

### 注释 256：原第 350 行

引脚（Pin）：`PIO2_3`。

### 注释 257：原第 351 行

引脚（Pin）：`PIO2_4`。

### 注释 258：原第 352 行

引脚（Pin）：`PIO2_4`。

### 注释 259：原第 353 行

引脚（Pin）：`PIO2_4`。

### 注释 260：原第 354 行

引脚（Pin）：`PIO2_5`。

### 注释 261：原第 355 行

引脚（Pin）：`PIO2_5`。

### 注释 262：原第 356 行

引脚（Pin）：`PIO2_5`。

### 注释 263：原第 357 行

引脚（Pin）：`PIO2_6`。

### 注释 264：原第 358 行

引脚（Pin）：`PIO2_6`。

### 注释 265：原第 359 行

引脚（Pin）：`PIO2_6`。

### 注释 266：原第 360 行

引脚（Pin）：`PIO2_6`。

### 注释 267：原第 361 行

引脚（Pin）：`PIO2_7`。

### 注释 268：原第 362 行

引脚（Pin）：`PIO2_7`。

### 注释 269：原第 363 行

引脚（Pin）：`PIO2_7`。

### 注释 270：原第 364 行

引脚（Pin）：`PIO2_8`。

### 注释 271：原第 365 行

引脚（Pin）：`PIO2_8`。

### 注释 272：原第 366 行

引脚（Pin）：`PIO2_9`。

### 注释 273：原第 367 行

引脚（Pin）：`PIO2_9`。

### 注释 274：原第 368 行

引脚（Pin）：`PIO2_10`。

### 注释 275：原第 369 行

引脚（Pin）：`PIO2_10`。

### 注释 276：原第 370 行

引脚（Pin）：`PIO2_10`。

### 注释 277：原第 371 行

引脚（Pin）：`PIO2_11`。

### 注释 278：原第 372 行

引脚（Pin）：`PIO2_11`。

### 注释 279：原第 373 行

引脚（Pin）：`PIO2_12`。

### 注释 280：原第 374 行

引脚（Pin）：`PIO2_12`。

### 注释 281：原第 375 行

引脚（Pin）：`PIO2_13`。

### 注释 282：原第 376 行

引脚（Pin）：`PIO2_13`。

### 注释 283：原第 377 行

引脚（Pin）：`PIO2_14`。

### 注释 284：原第 378 行

引脚（Pin）：`PIO2_14`。

### 注释 285：原第 379 行

引脚（Pin）：`PIO2_15`。

### 注释 286：原第 380 行

引脚（Pin）：`PIO2_15`。

### 注释 287：原第 381 行

引脚（Pin）：`PIO2_16`。

### 注释 288：原第 382 行

引脚（Pin）：`PIO2_16`。

### 注释 289：原第 383 行

引脚（Pin）：`PIO2_17`。

### 注释 290：原第 384 行

引脚（Pin）：`PIO2_17`。

### 注释 291：原第 385 行

引脚（Pin）：`PIO2_18`。

### 注释 292：原第 386 行

引脚（Pin）：`PIO2_18`。

### 注释 293：原第 387 行

引脚（Pin）：`PIO2_19`。

### 注释 294：原第 388 行

引脚（Pin）：`PIO2_19`。

### 注释 295：原第 389 行

引脚（Pin）：`PIO2_20`。

### 注释 296：原第 390 行

引脚（Pin）：`PIO2_21`。

### 注释 297：原第 391 行

引脚（Pin）：`PIO2_22`。

### 注释 298：原第 392 行

引脚（Pin）：`PIO2_23`。

### 注释 299：原第 394 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_LPC11U6X_PINCTRL_H_`。

## 3.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_management_reference/P027_zephyr__dt-bindings__pinctrl__lpc11u6x-pinctrl.h_文件参考.md)

---

[上一章](P002_kernel.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P004_pinctrl-rzg2-common.h_源码浏览.md)
