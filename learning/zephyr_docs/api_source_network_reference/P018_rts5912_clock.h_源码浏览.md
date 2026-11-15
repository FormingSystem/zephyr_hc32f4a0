---
id: learning.zephyr-docs.api-source-network-reference.page-18
title: rts5912_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rts5912__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_rts5912\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/rts5912__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/rts5912__clock_8h.html)。

## 18.1\_原始可见代码（Source Code）

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

```c
/*
 * SPDX-License-Identifier: Apache-2.0
 *
 * Copyright (c) 2024 Realtek Semiconductor Corporation, SIBG-SD7
 * Author: Lin Yu-Cheng <lin_yu_cheng@realtek.com>
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RTS5912_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RTS5912_CLOCK_H_

/* ====================================================================================== */
/* =====================================  I2CCLK  ======================================= */
#define I2CCLK_I2C0CLKPWR_Pos         (0)
#define I2CCLK_I2C0CLKPWR_Msk         (0x1)
#define I2CCLK_I2C0CLKSRC_Pos         (1)
#define I2CCLK_I2C0CLKSRC_Msk         (0x2)
#define I2CCLK_I2C0CLKDIV_Pos         (2)
#define I2CCLK_I2C0CLKDIV_Msk         (0xc)
#define I2CCLK_I2C1CLKPWR_Pos         (4)
#define I2CCLK_I2C1CLKPWR_Msk         (0x10)
#define I2CCLK_I2C1CLKSRC_Pos         (5)
#define I2CCLK_I2C1CLKSRC_Msk         (0x20)
#define I2CCLK_I2C1CLKDIV_Pos         (6)
#define I2CCLK_I2C1CLKDIV_Msk         (0xc0)
#define I2CCLK_I2C2CLKPWR_Pos         (8)
#define I2CCLK_I2C2CLKPWR_Msk         (0x100)
#define I2CCLK_I2C2CLKSRC_Pos         (9)
#define I2CCLK_I2C2CLKSRC_Msk         (0x200)
#define I2CCLK_I2C2CLKDIV_Pos         (10)
#define I2CCLK_I2C2CLKDIV_Msk         (0xc00)
#define I2CCLK_I2C3CLKPWR_Pos         (12)
#define I2CCLK_I2C3CLKPWR_Msk         (0x1000)
#define I2CCLK_I2C3CLKSRC_Pos         (13)
#define I2CCLK_I2C3CLKSRC_Msk         (0x2000)
#define I2CCLK_I2C3CLKDIV_Pos         (14)
#define I2CCLK_I2C3CLKDIV_Msk         (0xc000)
#define I2CCLK_I2C4CLKPWR_Pos         (16)
#define I2CCLK_I2C4CLKPWR_Msk         (0x10000)
#define I2CCLK_I2C4CLKSRC_Pos         (17)
#define I2CCLK_I2C4CLKSRC_Msk         (0x20000)
#define I2CCLK_I2C4CLKDIV_Pos         (18)
#define I2CCLK_I2C4CLKDIV_Msk         (0xc0000)
#define I2CCLK_I2C5CLKPWR_Pos         (20)
#define I2CCLK_I2C5CLKPWR_Msk         (0x100000)
#define I2CCLK_I2C5CLKSRC_Pos         (21)
#define I2CCLK_I2C5CLKSRC_Msk         (0x200000)
#define I2CCLK_I2C5CLKDIV_Pos         (22)
#define I2CCLK_I2C5CLKDIV_Msk         (0xc00000)
#define I2CCLK_I2C6CLKPWR_Pos         (24)
#define I2CCLK_I2C6CLKPWR_Msk         (0x1000000)
#define I2CCLK_I2C6CLKSRC_Pos         (25)
#define I2CCLK_I2C6CLKSRC_Msk         (0x2000000)
#define I2CCLK_I2C6CLKDIV_Pos         (26)
#define I2CCLK_I2C6CLKDIV_Msk         (0xc000000)
#define I2CCLK_I2C7CLKPWR_Pos         (28)
#define I2CCLK_I2C7CLKPWR_Msk         (0x10000000)
#define I2CCLK_I2C7CLKSRC_Pos         (29)
#define I2CCLK_I2C7CLKSRC_Msk         (0x20000000)
#define I2CCLK_I2C7CLKDIV_Pos         (30)
#define I2CCLK_I2C7CLKDIV_Msk         (0xc0000000)
/* ===================================  PERICLKPWR0  ==================================== */
#define PERICLKPWR0_GPIOCLKPWR_Pos    (0)
#define PERICLKPWR0_GPIOCLKPWR_Msk    (0x1)
#define PERICLKPWR0_TACHO0CLKPWR_Pos  (1)
#define PERICLKPWR0_TACHO0CLKPWR_Msk  (0x2)
#define PERICLKPWR0_TACHO1CLKPWR_Pos  (2)
#define PERICLKPWR0_TACHO1CLKPWR_Msk  (0x4)
#define PERICLKPWR0_TACHO2CLKPWR_Pos  (3)
#define PERICLKPWR0_TACHO2CLKPWR_Msk  (0x8)
#define PERICLKPWR0_TACHO3CLKPWR_Pos  (4)
#define PERICLKPWR0_TACHO3CLKPWR_Msk  (0x10)
#define PERICLKPWR0_PS2CLKPWR_Pos     (5)
#define PERICLKPWR0_PS2CLKPWR_Msk     (0x20)
#define PERICLKPWR0_KBMCLKPWR_Pos     (6)
#define PERICLKPWR0_KBMCLKPWR_Msk     (0x40)
#define PERICLKPWR0_PECICLKPWR_Pos    (7)
#define PERICLKPWR0_PECICLKPWR_Msk    (0x80)
#define PERICLKPWR0_PL0CLKPWR_Pos     (8)
#define PERICLKPWR0_PL0CLKPWR_Msk     (0x100)
#define PERICLKPWR0_PL1CLKPWR_Pos     (9)
#define PERICLKPWR0_PL1CLKPWR_Msk     (0x200)
#define PERICLKPWR0_PWM0CLKPWR_Pos    (10)
#define PERICLKPWR0_PWM0CLKPWR_Msk    (0x400)
#define PERICLKPWR0_PWM1CLKPWR_Pos    (11)
#define PERICLKPWR0_PWM1CLKPWR_Msk    (0x800)
#define PERICLKPWR0_PWM2CLKPWR_Pos    (12)
#define PERICLKPWR0_PWM2CLKPWR_Msk    (0x1000)
#define PERICLKPWR0_PWM3CLKPWR_Pos    (13)
#define PERICLKPWR0_PWM3CLKPWR_Msk    (0x2000)
#define PERICLKPWR0_PWM4CLKPWR_Pos    (14)
#define PERICLKPWR0_PWM4CLKPWR_Msk    (0x4000)
#define PERICLKPWR0_PWM5CLKPWR_Pos    (15)
#define PERICLKPWR0_PWM5CLKPWR_Msk    (0x8000)
#define PERICLKPWR0_PWM6CLKPWR_Pos    (16)
#define PERICLKPWR0_PWM6CLKPWR_Msk    (0x10000)
#define PERICLKPWR0_PWM7CLKPWR_Pos    (17)
#define PERICLKPWR0_PWM7CLKPWR_Msk    (0x20000)
#define PERICLKPWR0_PWM8CLKPWR_Pos    (18)
#define PERICLKPWR0_PWM8CLKPWR_Msk    (0x40000)
#define PERICLKPWR0_PWM9CLKPWR_Pos    (19)
#define PERICLKPWR0_PWM9CLKPWR_Msk    (0x80000)
#define PERICLKPWR0_PWM10CLKPWR_Pos   (20)
#define PERICLKPWR0_PWM10CLKPWR_Msk   (0x100000)
#define PERICLKPWR0_PWM11CLKPWR_Pos   (21)
#define PERICLKPWR0_PWM11CLKPWR_Msk   (0x200000)
#define PERICLKPWR0_ESPICLKPWR_Pos    (22)
#define PERICLKPWR0_ESPICLKPWR_Msk    (0x400000)
#define PERICLKPWR0_KBCCLKPWR_Pos     (23)
#define PERICLKPWR0_KBCCLKPWR_Msk     (0x800000)
#define PERICLKPWR0_ACPICLKPWR_Pos    (24)
#define PERICLKPWR0_ACPICLKPWR_Msk    (0x1000000)
#define PERICLKPWR0_PMPORT0CLKPWR_Pos (25)
#define PERICLKPWR0_PMPORT0CLKPWR_Msk (0x2000000)
#define PERICLKPWR0_PMPORT1CLKPWR_Pos (26)
#define PERICLKPWR0_PMPORT1CLKPWR_Msk (0x4000000)
#define PERICLKPWR0_PMPORT2CLKPWR_Pos (27)
#define PERICLKPWR0_PMPORT2CLKPWR_Msk (0x8000000)
#define PERICLKPWR0_PMPORT3CLKPWR_Pos (28)
#define PERICLKPWR0_PMPORT3CLKPWR_Msk (0x10000000)
#define PERICLKPWR0_P80CLKPWR_Pos     (29)
#define PERICLKPWR0_P80CLKPWR_Msk     (0x20000000)
#define PERICLKPWR0_EMI0CLKPWR_Pos    (30)
#define PERICLKPWR0_EMI0CLKPWR_Msk    (0x40000000)
#define PERICLKPWR0_EMI1CLKPWR_Pos    (31)
#define PERICLKPWR0_EMI1CLKPWR_Msk    (0x80000000)
/* =====================================  UARTCLK  ====================================== */
#define UARTCLK_PWR_Pos               (0)
#define UARTCLK_PWR_Msk               (0x1)
#define UARTCLK_SRC_Pos               (1)
#define UARTCLK_SRC_Msk               (0x2)
#define UARTCLK_DIV_Pos               (2)
#define UARTCLK_DIV_Msk               (0xc)
/* =====================================  ADCCLK  ======================================= */
#define ADCCLK_PWR_Pos                (0)
#define ADCCLK_PWR_Msk                (0x1)
#define ADCCLK_SRC_Pos                (1)
#define ADCCLK_SRC_Msk                (0x2)
#define ADCCLK_DIV_Pos                (2)
#define ADCCLK_DIV_Msk                (0x1c)
/* ===================================  PERICLKPWR1  ==================================== */
#define PERICLKPWR1_EMI2CLKPWR_Pos    (0)
#define PERICLKPWR1_EMI2CLKPWR_Msk    (0x1)
#define PERICLKPWR1_EMI3CLKPWR_Pos    (1)
#define PERICLKPWR1_EMI3CLKPWR_Msk    (0x2)
#define PERICLKPWR1_EMI4CLKPWR_Pos    (2)
#define PERICLKPWR1_EMI4CLKPWR_Msk    (0x4)
#define PERICLKPWR1_EMI5CLKPWR_Pos    (3)
#define PERICLKPWR1_EMI5CLKPWR_Msk    (0x8)
#define PERICLKPWR1_EMI6CLKPWR_Pos    (4)
#define PERICLKPWR1_EMI6CLKPWR_Msk    (0x10)
#define PERICLKPWR1_EMI7CLKPWR_Pos    (5)
#define PERICLKPWR1_EMI7CLKPWR_Msk    (0x20)
#define PERICLKPWR1_I3C0CLKPWR_Pos    (9)
#define PERICLKPWR1_I3C0CLKPWR_Msk    (0x200)
#define PERICLKPWR1_I3C1CLKPWR_Pos    (10)
#define PERICLKPWR1_I3C1CLKPWR_Msk    (0x400)
#define PERICLKPWR1_I2CAUTOCLKPWR_Pos (11)
#define PERICLKPWR1_I2CAUTOCLKPWR_Msk (0x800)
#define PERICLKPWR1_MCCLKPWR_Pos      (12)
#define PERICLKPWR1_MCCLKPWR_Msk      (0x1000)
#define PERICLKPWR1_TMR0CLKPWR_Pos    (13)
#define PERICLKPWR1_TMR0CLKPWR_Msk    (0x2000)
#define PERICLKPWR1_TMR1CLKPWR_Pos    (14)
#define PERICLKPWR1_TMR1CLKPWR_Msk    (0x4000)
#define PERICLKPWR1_TMR2CLKPWR_Pos    (15)
#define PERICLKPWR1_TMR2CLKPWR_Msk    (0x8000)
#define PERICLKPWR1_TMR3CLKPWR_Pos    (16)
#define PERICLKPWR1_TMR3CLKPWR_Msk    (0x10000)
#define PERICLKPWR1_TMR4CLKPWR_Pos    (17)
#define PERICLKPWR1_TMR4CLKPWR_Msk    (0x20000)
#define PERICLKPWR1_TMR5CLKPWR_Pos    (18)
#define PERICLKPWR1_TMR5CLKPWR_Msk    (0x40000)
#define PERICLKPWR1_RTMRCLKPWR_Pos    (19)
#define PERICLKPWR1_RTMRCLKPWR_Msk    (0x80000)
#define PERICLKPWR1_SLWTMR0CLKPWR_Pos (20)
#define PERICLKPWR1_SLWTMR0CLKPWR_Msk (0x100000)
#define PERICLKPWR1_SLWTMR1CLKPWR_Pos (21)
#define PERICLKPWR1_SLWTMR1CLKPWR_Msk (0x200000)
/* ===================================  PERICLKPWR2  ==================================== */
#define PERICLKPWR2_RTCCLKPWR_Pos     (0)
#define PERICLKPWR2_RTCCLKPWR_Msk     (0x1)
#define PERICLKPWR2_WDTCLKPWR_Pos     (1)
#define PERICLKPWR2_WDTCLKPWR_Msk     (0x2)
#define PERICLKPWR2_PWRBTNCLKPWR_Pos  (2)
#define PERICLKPWR2_PWRBTNCLKPWR_Msk  (0x4)
#define PERICLKPWR2_RC32KSRC_Pos      (30)
#define PERICLKPWR2_RC32KSRC_Msk      (0xc0000000)
/* ====================================================================================== */

#define RTS5912_SCCON_SYS         (0)
#define RTS5912_SCCON_I2C         (2)
#define RTS5912_SCCON_UART        (3)
#define RTS5912_SCCON_ADC         (4)
#define RTS5912_SCCON_PERIPH_GRP0 (5)
#define RTS5912_SCCON_PERIPH_GRP1 (6)
#define RTS5912_SCCON_PERIPH_GRP2 (7)

#define I2C0_CLKPWR (I2CCLK_I2C0CLKPWR_Pos)
#define I2C1_CLKPWR (I2CCLK_I2C1CLKPWR_Pos)
#define I2C2_CLKPWR (I2CCLK_I2C2CLKPWR_Pos)
#define I2C3_CLKPWR (I2CCLK_I2C3CLKPWR_Pos)
#define I2C4_CLKPWR (I2CCLK_I2C4CLKPWR_Pos)
#define I2C5_CLKPWR (I2CCLK_I2C5CLKPWR_Pos)
#define I2C6_CLKPWR (I2CCLK_I2C6CLKPWR_Pos)
#define I2C7_CLKPWR (I2CCLK_I2C7CLKPWR_Pos)

#define I2C0_PLL   (0x0 << I2CCLK_I2C0CLKSRC_Pos)
#define I2C0_RC25M (0x1 << I2CCLK_I2C0CLKSRC_Pos)
#define I2C1_PLL   (0x0 << I2CCLK_I2C1CLKSRC_Pos)
#define I2C1_RC25M (0x1 << I2CCLK_I2C1CLKSRC_Pos)
#define I2C2_PLL   (0x0 << I2CCLK_I2C2CLKSRC_Pos)
#define I2C2_RC25M (0x1 << I2CCLK_I2C2CLKSRC_Pos)
#define I2C3_PLL   (0x0 << I2CCLK_I2C3CLKSRC_Pos)
#define I2C3_RC25M (0x1 << I2CCLK_I2C3CLKSRC_Pos)
#define I2C4_PLL   (0x0 << I2CCLK_I2C4CLKSRC_Pos)
#define I2C4_RC25M (0x1 << I2CCLK_I2C4CLKSRC_Pos)
#define I2C5_PLL   (0x0 << I2CCLK_I2C5CLKSRC_Pos)
#define I2C5_RC25M (0x1 << I2CCLK_I2C5CLKSRC_Pos)
#define I2C6_PLL   (0x0 << I2CCLK_I2C6CLKSRC_Pos)
#define I2C6_RC25M (0x1 << I2CCLK_I2C6CLKSRC_Pos)
#define I2C7_PLL   (0x0 << I2CCLK_I2C7CLKSRC_Pos)
#define I2C7_RC25M (0x1 << I2CCLK_I2C7CLKSRC_Pos)

#define I2C0_CLKDIV1 (0 << I2CCLK_I2C0CLKDIV_Pos)
#define I2C0_CLKDIV2 (1 << I2CCLK_I2C0CLKDIV_Pos)
#define I2C0_CLKDIV4 (2 << I2CCLK_I2C0CLKDIV_Pos)
#define I2C0_CLKDIV8 (3 << I2CCLK_I2C0CLKDIV_Pos)

#define I2C1_CLKDIV1 (0 << I2CCLK_I2C1CLKDIV_Pos)
#define I2C1_CLKDIV2 (1 << I2CCLK_I2C1CLKDIV_Pos)
#define I2C1_CLKDIV4 (2 << I2CCLK_I2C1CLKDIV_Pos)
#define I2C1_CLKDIV8 (3 << I2CCLK_I2C1CLKDIV_Pos)

#define I2C2_CLKDIV1 (0 << I2CCLK_I2C2CLKDIV_Pos)
#define I2C2_CLKDIV2 (1 << I2CCLK_I2C2CLKDIV_Pos)
#define I2C2_CLKDIV4 (2 << I2CCLK_I2C2CLKDIV_Pos)
#define I2C2_CLKDIV8 (3 << I2CCLK_I2C2CLKDIV_Pos)

#define I2C3_CLKDIV1 (0 << I2CCLK_I2C3CLKDIV_Pos)
#define I2C3_CLKDIV2 (1 << I2CCLK_I2C3CLKDIV_Pos)
#define I2C3_CLKDIV4 (2 << I2CCLK_I2C3CLKDIV_Pos)
#define I2C3_CLKDIV8 (3 << I2CCLK_I2C3CLKDIV_Pos)

#define I2C4_CLKDIV1 (0 << I2CCLK_I2C4CLKDIV_Pos)
#define I2C4_CLKDIV2 (1 << I2CCLK_I2C4CLKDIV_Pos)
#define I2C4_CLKDIV4 (2 << I2CCLK_I2C4CLKDIV_Pos)
#define I2C4_CLKDIV8 (3 << I2CCLK_I2C4CLKDIV_Pos)

#define I2C5_CLKDIV1 (0 << I2CCLK_I2C5CLKDIV_Pos)
#define I2C5_CLKDIV2 (1 << I2CCLK_I2C5CLKDIV_Pos)
#define I2C5_CLKDIV4 (2 << I2CCLK_I2C5CLKDIV_Pos)
#define I2C5_CLKDIV8 (3 << I2CCLK_I2C5CLKDIV_Pos)

#define I2C6_CLKDIV1 (0 << I2CCLK_I2C6CLKDIV_Pos)
#define I2C6_CLKDIV2 (1 << I2CCLK_I2C6CLKDIV_Pos)
#define I2C6_CLKDIV4 (2 << I2CCLK_I2C6CLKDIV_Pos)
#define I2C6_CLKDIV8 (3 << I2CCLK_I2C6CLKDIV_Pos)

#define I2C7_CLKDIV1 (0 << I2CCLK_I2C7CLKDIV_Pos)
#define I2C7_CLKDIV2 (1 << I2CCLK_I2C7CLKDIV_Pos)
#define I2C7_CLKDIV4 (2 << I2CCLK_I2C7CLKDIV_Pos)
#define I2C7_CLKDIV8 (3 << I2CCLK_I2C7CLKDIV_Pos)

#define UART0_CLKPWR (UARTCLK_PWR_Pos)

#define UART0_RC25M (0x0 << UARTCLK_SRC_Pos)
#define UART0_PLL   (0x1 << UARTCLK_SRC_Pos)

#define UART0_CLKDIV1 (0 << UARTCLK_DIV_Pos)
#define UART0_CLKDIV2 (1 << UARTCLK_DIV_Pos)
#define UART0_CLKDIV4 (2 << UARTCLK_DIV_Pos)
#define UART0_CLKDIV8 (3 << UARTCLK_DIV_Pos)

#define ADC0_CLKPWR (ADCCLK_PWR_Pos)

#define ADC0_RC25M (0x0 << ADCCLK_SRC_Pos)
#define ADC0_PLL   (0x1 << ADCCLK_SRC_Pos)

#define ADC0_CLKDIV1 (0 << ADCCLK_DIV_Pos)
#define ADC0_CLKDIV2 (1 << ADCCLK_DIV_Pos)
#define ADC0_CLKDIV3 (2 << ADCCLK_DIV_Pos)
#define ADC0_CLKDIV4 (3 << ADCCLK_DIV_Pos)
#define ADC0_CLKDIV6 (4 << ADCCLK_DIV_Pos)
#define ADC0_CLKDIV8 (5 << ADCCLK_DIV_Pos)

#define PERIPH_GRP0_GPIO_CLKPWR    (PERICLKPWR0_GPIOCLKPWR_Pos)
#define PERIPH_GRP0_TACH0_CLKPWR   (PERICLKPWR0_TACHO0CLKPWR_Pos)
#define PERIPH_GRP0_TACH1_CLKPWR   (PERICLKPWR0_TACHO1CLKPWR_Pos)
#define PERIPH_GRP0_TACH2_CLKPWR   (PERICLKPWR0_TACHO2CLKPWR_Pos)
#define PERIPH_GRP0_TACH3_CLKPWR   (PERICLKPWR0_TACHO3CLKPWR_Pos)
#define PERIPH_GRP0_PS2_CLKPWR     (PERICLKPWR0_PS2CLKPWR_Pos)
#define PERIPH_GRP0_KBM_CLKPWR     (PERICLKPWR0_KBMCLKPWR_Pos)
#define PERIPH_GRP0_PECI_CLKPWR    (PERICLKPWR0_PECICLKPWR_Pos)
#define PERIPH_GRP0_LEDPWM0_CLKPWR (PERICLKPWR0_PL0CLKPWR_Pos)
#define PERIPH_GRP0_LEDPWM1_CLKPWR (PERICLKPWR0_PL1CLKPWR_Pos)
#define PERIPH_GRP0_PWM0_CLKPWR    (PERICLKPWR0_PWM0CLKPWR_Pos)
#define PERIPH_GRP0_PWM1_CLKPWR    (PERICLKPWR0_PWM1CLKPWR_Pos)
#define PERIPH_GRP0_PWM2_CLKPWR    (PERICLKPWR0_PWM2CLKPWR_Pos)
#define PERIPH_GRP0_PWM3_CLKPWR    (PERICLKPWR0_PWM3CLKPWR_Pos)
#define PERIPH_GRP0_PWM4_CLKPWR    (PERICLKPWR0_PWM4CLKPWR_Pos)
#define PERIPH_GRP0_PWM5_CLKPWR    (PERICLKPWR0_PWM5CLKPWR_Pos)
#define PERIPH_GRP0_PWM6_CLKPWR    (PERICLKPWR0_PWM6CLKPWR_Pos)
#define PERIPH_GRP0_PWM7_CLKPWR    (PERICLKPWR0_PWM7CLKPWR_Pos)
#define PERIPH_GRP0_PWM8_CLKPWR    (PERICLKPWR0_PWM8CLKPWR_Pos)
#define PERIPH_GRP0_PWM9_CLKPWR    (PERICLKPWR0_PWM9CLKPWR_Pos)
#define PERIPH_GRP0_PWM10_CLKPWR   (PERICLKPWR0_PWM10CLKPWR_Pos)
#define PERIPH_GRP0_PWM11_CLKPWR   (PERICLKPWR0_PWM11CLKPWR_Pos)
#define PERIPH_GRP0_ESPI_CLKPWR    (PERICLKPWR0_ESPICLKPWR_Pos)
#define PERIPH_GRP0_KBC_CLKPWR     (PERICLKPWR0_KBCCLKPWR_Pos)
#define PERIPH_GRP0_ACPI_CLKPWR    (PERICLKPWR0_ACPICLKPWR_Pos)
#define PERIPH_GRP0_PMPORT0_CLKPWR (PERICLKPWR0_PMPORT0CLKPWR_Pos)
#define PERIPH_GRP0_PMPORT1_CLKPWR (PERICLKPWR0_PMPORT1CLKPWR_Pos)
#define PERIPH_GRP0_PMPORT2_CLKPWR (PERICLKPWR0_PMPORT2CLKPWR_Pos)
#define PERIPH_GRP0_PMPORT3_CLKPWR (PERICLKPWR0_PMPORT3CLKPWR_Pos)
#define PERIPH_GRP0_P80_CLKPWR     (PERICLKPWR0_P80CLKPWR_Pos)
#define PERIPH_GRP0_EMI0_CLKPWR    (PERICLKPWR0_EMI0CLKPWR_Pos)
#define PERIPH_GRP0_EMI1_CLKPWR    (PERICLKPWR0_EMI1CLKPWR_Pos)

#define PERIPH_GRP1_EMI2_CLKPWR    (PERICLKPWR1_EMI2CLKPWR_Pos)
#define PERIPH_GRP1_EMI3_CLKPWR    (PERICLKPWR1_EMI3CLKPWR_Pos)
#define PERIPH_GRP1_EMI4_CLKPWR    (PERICLKPWR1_EMI4CLKPWR_Pos)
#define PERIPH_GRP1_EMI5_CLKPWR    (PERICLKPWR1_EMI5CLKPWR_Pos)
#define PERIPH_GRP1_EMI6_CLKPWR    (PERICLKPWR1_EMI6CLKPWR_Pos)
#define PERIPH_GRP1_EMI7_CLKPWR    (PERICLKPWR1_EMI7CLKPWR_Pos)
#define PERIPH_GRP1_I3C0_CLKPWR    (PERICLKPWR1_I3C0CLKPWR_Pos)
#define PERIPH_GRP1_I3C1_CLKPWR    (PERICLKPWR1_I3C1CLKPWR_Pos)
#define PERIPH_GRP1_I2CAUTO_CLKPWR (PERICLKPWR1_I2CAUTOCLKPWR_Pos)
#define PERIPH_GRP1_MC_CLKPWR      (PERICLKPWR1_MCCLKPWR_Pos)
#define PERIPH_GRP1_TMR0_CLKPWR    (PERICLKPWR1_TMR0CLKPWR_Pos)
#define PERIPH_GRP1_TMR1_CLKPWR    (PERICLKPWR1_TMR1CLKPWR_Pos)
#define PERIPH_GRP1_TMR2_CLKPWR    (PERICLKPWR1_TMR2CLKPWR_Pos)
#define PERIPH_GRP1_TMR3_CLKPWR    (PERICLKPWR1_TMR3CLKPWR_Pos)
#define PERIPH_GRP1_TMR4_CLKPWR    (PERICLKPWR1_TMR4CLKPWR_Pos)
#define PERIPH_GRP1_TMR5_CLKPWR    (PERICLKPWR1_TMR5CLKPWR_Pos)
#define PERIPH_GRP1_RTMR_CLKPWR    (PERICLKPWR1_RTMRCLKPWR_Pos)
#define PERIPH_GRP1_SLWTMR0_CLKPWR (PERICLKPWR1_SLWTMR0CLKPWR_Pos)
#define PERIPH_GRP1_SLWTMR1_CLKPWR (PERICLKPWR1_SLWTMR1CLKPWR_Pos)

#define PERIPH_GRP2_RTC_CLKPWR       (PERICLKPWR2_RTCCLKPWR_Pos)
#define PERIPH_GRP2_WDT_CLKPWR       (PERICLKPWR2_WDTCLKPWR_Pos)
#define PERIPH_GRP2_WDTPWRBTN_CLKPWR (PERICLKPWR2_PWRBTNCLKPWR_Pos)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RTS5912_CLOCK_H_ */
```

## 18.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

版权（Copyright）：© 2024 Realtek Semiconductor Corporation, SIBG-SD7。

作者（Author）：Lin Yu-Cheng <lin_yu_cheng@realtek.com>。

### 注释 2：原第 11 行

分隔线。

### 注释 3：原第 12 行

`I2CCLK` 寄存器分隔标题。

### 注释 4：原第 61 行

`PERICLKPWR0` 寄存器分隔标题。

### 注释 5：原第 126 行

`UARTCLK` 寄存器分隔标题。

### 注释 6：原第 133 行

`ADCCLK` 寄存器分隔标题。

### 注释 7：原第 140 行

`PERICLKPWR1` 寄存器分隔标题。

### 注释 8：原第 179 行

`PERICLKPWR2` 寄存器分隔标题。

### 注释 9：原第 188 行

分隔线。

### 注释 10：原第 343 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RTS5912_CLOCK_H_`。

## 18.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/rts5912__clock_8h.html)

---

[上一章](P017_rtl8752h-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P019_stm32-pinctrl-common.h_源码浏览.md)
