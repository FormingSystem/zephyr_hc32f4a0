---
id: learning.zephyr-docs.api-source-architecture-reference.page-5
title: ch32v00x-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ch32v00x-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_ch32v00x-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ch32v00x-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P038_zephyr__dt-bindings__pinctrl__ch32v00x-pinctrl.h_文件参考.md)。

## 5.1\_原始可见代码（Source Code）

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
<a id="foldopen00039"></a>
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

```c
/*
 * Copyright (c) 2025 Michael Hope <michaelh@juju.nz>
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_CH32V00X_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_CH32V00X_PINCTRL_H_

#define CH32V00X_PINMUX_PORT_PA 0
#define CH32V00X_PINMUX_PORT_PB 1
#define CH32V00X_PINMUX_PORT_PC 2
#define CH32V00X_PINMUX_PORT_PD 3

/* Starting bit for the remap field in PCFR1 */
#define CH32V00X_PINMUX_SPI1_RM         0
#define CH32V00X_PINMUX_I2C1_RM         3
#define CH32V00X_PINMUX_USART1_RM       6
#define CH32V00X_PINMUX_TIM1_RM         10
#define CH32V00X_PINMUX_TIM2_RM         14
#define CH32V00X_PINMUX_PA1PA2_RM       17
#define CH32V00X_PINMUX_ADC_DTR_GINJ_RM 18
#define CH32V00X_PINMUX_ADC_DTR_GREG_RM 19
#define CH32V00X_PINMUX_USART2_RM       20

/* Port number with 0-3 */
#define CH32V00X_PINCTRL_PORT_SHIFT 0
#define CH32V00X_PINCTRL_PORT_MASK  GENMASK(1, 0)
/* Pin number 0-7 */
#define CH32V00X_PINCTRL_PIN_SHIFT  2
#define CH32V00X_PINCTRL_PIN_MASK   GENMASK(4, 2)
/* Base remap bit 0-31 */
#define CH32V00X_PINCTRL_BASE_SHIFT 5
#define CH32V00X_PINCTRL_BASE_MASK  GENMASK(9, 5)
/* Function remapping ID 0-7 */
#define CH32V00X_PINCTRL_RM_SHIFT   10
#define CH32V00X_PINCTRL_RM_MASK    GENMASK(12, 10)

#define CH32V00X_PINMUX_DEFINE(port, pin, rm, remapping)                                           \
        ((CH32V00X_PINMUX_PORT_##port << CH32V00X_PINCTRL_PORT_SHIFT) |                            \
         (pin << CH32V00X_PINCTRL_PIN_SHIFT) |                                                     \
         (CH32V00X_PINMUX_##rm##_RM << CH32V00X_PINCTRL_BASE_SHIFT) |                              \
         (remapping << CH32V00X_PINCTRL_RM_SHIFT))

#define TIM1_ETR_PC5_0  CH32V00X_PINMUX_DEFINE(PC, 5, TIM1, 0)
#define TIM1_ETR_PD4_1  CH32V00X_PINMUX_DEFINE(PD, 4, TIM1, 1)
#define TIM1_ETR_PC5_2  CH32V00X_PINMUX_DEFINE(PC, 5, TIM1, 2)
#define TIM1_ETR_PC2_3  CH32V00X_PINMUX_DEFINE(PC, 2, TIM1, 3)
#define TIM1_ETR_PD4_4  CH32V00X_PINMUX_DEFINE(PD, 4, TIM1, 4)
#define TIM1_ETR_PD4_5  CH32V00X_PINMUX_DEFINE(PD, 4, TIM1, 5)
#define TIM1_ETR_PD4_6  CH32V00X_PINMUX_DEFINE(PD, 4, TIM1, 6)
#define TIM1_ETR_PB4_7  CH32V00X_PINMUX_DEFINE(PB, 4, TIM1, 7)
#define TIM1_ETR_PB4_8  CH32V00X_PINMUX_DEFINE(PB, 4, TIM1, 8)
#define TIM1_ETR_PB4_9  CH32V00X_PINMUX_DEFINE(PB, 4, TIM1, 9)
#define TIM1_CH1_PD2_0  CH32V00X_PINMUX_DEFINE(PD, 2, TIM1, 0)
#define TIM1_CH1_PD2_1  CH32V00X_PINMUX_DEFINE(PD, 2, TIM1, 1)
#define TIM1_CH1_PC6_2  CH32V00X_PINMUX_DEFINE(PC, 6, TIM1, 2)
#define TIM1_CH1_PC4_3  CH32V00X_PINMUX_DEFINE(PC, 4, TIM1, 3)
#define TIM1_CH1_PA3_4  CH32V00X_PINMUX_DEFINE(PA, 3, TIM1, 4)
#define TIM1_CH1_PA3_5  CH32V00X_PINMUX_DEFINE(PA, 3, TIM1, 5)
#define TIM1_CH1_PA3_6  CH32V00X_PINMUX_DEFINE(PA, 3, TIM1, 6)
#define TIM1_CH1_PC4_7  CH32V00X_PINMUX_DEFINE(PC, 4, TIM1, 7)
#define TIM1_CH1_PC4_8  CH32V00X_PINMUX_DEFINE(PC, 4, TIM1, 8)
#define TIM1_CH1_PA0_9  CH32V00X_PINMUX_DEFINE(PA, 0, TIM1, 9)
#define TIM1_CH2_PA1_0  CH32V00X_PINMUX_DEFINE(PA, 1, TIM1, 0)
#define TIM1_CH2_PA1_1  CH32V00X_PINMUX_DEFINE(PA, 1, TIM1, 1)
#define TIM1_CH2_PC7_2  CH32V00X_PINMUX_DEFINE(PC, 7, TIM1, 2)
#define TIM1_CH2_PC7_3  CH32V00X_PINMUX_DEFINE(PC, 7, TIM1, 3)
#define TIM1_CH2_PB0_4  CH32V00X_PINMUX_DEFINE(PB, 0, TIM1, 4)
#define TIM1_CH2_PB0_5  CH32V00X_PINMUX_DEFINE(PB, 0, TIM1, 5)
#define TIM1_CH2_PB0_6  CH32V00X_PINMUX_DEFINE(PB, 0, TIM1, 6)
#define TIM1_CH2_PC5_7  CH32V00X_PINMUX_DEFINE(PC, 5, TIM1, 7)
#define TIM1_CH2_PC5_8  CH32V00X_PINMUX_DEFINE(PC, 5, TIM1, 8)
#define TIM1_CH2_PA1_9  CH32V00X_PINMUX_DEFINE(PA, 1, TIM1, 9)
#define TIM1_CH3_PC3_0  CH32V00X_PINMUX_DEFINE(PC, 3, TIM1, 0)
#define TIM1_CH3_PC3_1  CH32V00X_PINMUX_DEFINE(PC, 3, TIM1, 1)
#define TIM1_CH3_PC0_2  CH32V00X_PINMUX_DEFINE(PC, 0, TIM1, 2)
#define TIM1_CH3_PC5_3  CH32V00X_PINMUX_DEFINE(PC, 5, TIM1, 3)
#define TIM1_CH3_PB1_4  CH32V00X_PINMUX_DEFINE(PB, 1, TIM1, 4)
#define TIM1_CH3_PC3_5  CH32V00X_PINMUX_DEFINE(PC, 3, TIM1, 5)
#define TIM1_CH3_PB1_6  CH32V00X_PINMUX_DEFINE(PB, 1, TIM1, 6)
#define TIM1_CH3_PC6_7  CH32V00X_PINMUX_DEFINE(PC, 6, TIM1, 7)
#define TIM1_CH3_PC6_8  CH32V00X_PINMUX_DEFINE(PC, 6, TIM1, 8)
#define TIM1_CH3_PA2_9  CH32V00X_PINMUX_DEFINE(PA, 2, TIM1, 9)
#define TIM1_CH4_PC4_0  CH32V00X_PINMUX_DEFINE(PC, 4, TIM1, 0)
#define TIM1_CH4_PC4_1  CH32V00X_PINMUX_DEFINE(PC, 4, TIM1, 1)
#define TIM1_CH4_PD3_2  CH32V00X_PINMUX_DEFINE(PD, 3, TIM1, 2)
#define TIM1_CH4_PD4_3  CH32V00X_PINMUX_DEFINE(PD, 4, TIM1, 3)
#define TIM1_CH4_PD1_4  CH32V00X_PINMUX_DEFINE(PD, 1, TIM1, 4)
#define TIM1_CH4_PD1_5  CH32V00X_PINMUX_DEFINE(PD, 1, TIM1, 5)
#define TIM1_CH4_PB2_6  CH32V00X_PINMUX_DEFINE(PB, 2, TIM1, 6)
#define TIM1_CH4_PC7_7  CH32V00X_PINMUX_DEFINE(PC, 7, TIM1, 7)
#define TIM1_CH4_PC7_8  CH32V00X_PINMUX_DEFINE(PC, 7, TIM1, 8)
#define TIM1_CH4_PA3_9  CH32V00X_PINMUX_DEFINE(PA, 3, TIM1, 9)
#define TIM1_BKIN_PC2_0 CH32V00X_PINMUX_DEFINE(PC, 2, TIM1, 0)
#define TIM1_BKIN_PC2_1 CH32V00X_PINMUX_DEFINE(PC, 2, TIM1, 1)
#define TIM1_BKIN_PC1_2 CH32V00X_PINMUX_DEFINE(PC, 1, TIM1, 2)
#define TIM1_BKIN_PC1_3 CH32V00X_PINMUX_DEFINE(PC, 1, TIM1, 3)
#define TIM1_BKIN_PB3_4 CH32V00X_PINMUX_DEFINE(PB, 3, TIM1, 4)
#define TIM1_BKIN_PB3_5 CH32V00X_PINMUX_DEFINE(PB, 3, TIM1, 5)
#define TIM1_BKIN_PA7_6 CH32V00X_PINMUX_DEFINE(PA, 7, TIM1, 6)
#define TIM1_BKIN_PB2_7 CH32V00X_PINMUX_DEFINE(PB, 2, TIM1, 7)
#define TIM1_BKIN_PB2_8 CH32V00X_PINMUX_DEFINE(PB, 2, TIM1, 8)
#define TIM1_BKIN_PB2_9 CH32V00X_PINMUX_DEFINE(PB, 2, TIM1, 9)
#define TIM1_CH1N_PD0_0 CH32V00X_PINMUX_DEFINE(PD, 0, TIM1, 0)
#define TIM1_CH1N_PD0_1 CH32V00X_PINMUX_DEFINE(PD, 0, TIM1, 1)
#define TIM1_CH1N_PC3_2 CH32V00X_PINMUX_DEFINE(PC, 3, TIM1, 2)
#define TIM1_CH1N_PC3_3 CH32V00X_PINMUX_DEFINE(PC, 3, TIM1, 3)
#define TIM1_CH1N_PA0_4 CH32V00X_PINMUX_DEFINE(PA, 0, TIM1, 4)
#define TIM1_CH1N_PA0_5 CH32V00X_PINMUX_DEFINE(PA, 0, TIM1, 5)
#define TIM1_CH1N_PA0_6 CH32V00X_PINMUX_DEFINE(PA, 0, TIM1, 6)
#define TIM1_CH1N_PC0_7 CH32V00X_PINMUX_DEFINE(PC, 0, TIM1, 7)
#define TIM1_CH1N_PA3_8 CH32V00X_PINMUX_DEFINE(PA, 3, TIM1, 8)
#define TIM1_CH1N_PC0_9 CH32V00X_PINMUX_DEFINE(PC, 0, TIM1, 9)
#define TIM1_CH2N_PA2_0 CH32V00X_PINMUX_DEFINE(PA, 2, TIM1, 0)
#define TIM1_CH2N_PA2_1 CH32V00X_PINMUX_DEFINE(PA, 2, TIM1, 1)
#define TIM1_CH2N_PC4_2 CH32V00X_PINMUX_DEFINE(PC, 4, TIM1, 2)
#define TIM1_CH2N_PD2_3 CH32V00X_PINMUX_DEFINE(PD, 2, TIM1, 3)
#define TIM1_CH2N_PA2_4 CH32V00X_PINMUX_DEFINE(PA, 2, TIM1, 4)
#define TIM1_CH2N_PA2_5 CH32V00X_PINMUX_DEFINE(PA, 2, TIM1, 5)
#define TIM1_CH2N_PA2_6 CH32V00X_PINMUX_DEFINE(PA, 2, TIM1, 6)
#define TIM1_CH2N_PC1_7 CH32V00X_PINMUX_DEFINE(PC, 1, TIM1, 7)
#define TIM1_CH2N_PB0_8 CH32V00X_PINMUX_DEFINE(PB, 0, TIM1, 8)
#define TIM1_CH2N_PC1_9 CH32V00X_PINMUX_DEFINE(PC, 1, TIM1, 9)
#define TIM1_CH3N_PD1_0 CH32V00X_PINMUX_DEFINE(PD, 1, TIM1, 0)
#define TIM1_CH3N_PD1_1 CH32V00X_PINMUX_DEFINE(PD, 1, TIM1, 1)
#define TIM1_CH3N_PD1_2 CH32V00X_PINMUX_DEFINE(PD, 1, TIM1, 2)
#define TIM1_CH3N_PC6_3 CH32V00X_PINMUX_DEFINE(PC, 6, TIM1, 3)
#define TIM1_CH3N_PD0_4 CH32V00X_PINMUX_DEFINE(PD, 0, TIM1, 4)
#define TIM1_CH3N_PD0_5 CH32V00X_PINMUX_DEFINE(PD, 0, TIM1, 5)
#define TIM1_CH3N_PD0_6 CH32V00X_PINMUX_DEFINE(PD, 0, TIM1, 6)
#define TIM1_CH3N_PC2_7 CH32V00X_PINMUX_DEFINE(PC, 2, TIM1, 7)
#define TIM1_CH3N_PB1_8 CH32V00X_PINMUX_DEFINE(PB, 1, TIM1, 8)
#define TIM1_CH3N_PC2_9 CH32V00X_PINMUX_DEFINE(PC, 2, TIM1, 9)

#define TIM2_ETR_PD4_0 CH32V00X_PINMUX_DEFINE(PD, 4, TIM2, 0)
#define TIM2_ETR_PC1_1 CH32V00X_PINMUX_DEFINE(PC, 1, TIM2, 1)
#define TIM2_ETR_PC5_2 CH32V00X_PINMUX_DEFINE(PC, 5, TIM2, 2)
#define TIM2_ETR_PC1_3 CH32V00X_PINMUX_DEFINE(PC, 1, TIM2, 3)
#define TIM2_ETR_PC0_4 CH32V00X_PINMUX_DEFINE(PC, 0, TIM2, 4)
#define TIM2_ETR_PA0_5 CH32V00X_PINMUX_DEFINE(PA, 0, TIM2, 5)
#define TIM2_ETR_PB1_6 CH32V00X_PINMUX_DEFINE(PB, 1, TIM2, 6)
#define TIM2_ETR_PD3_7 CH32V00X_PINMUX_DEFINE(PD, 3, TIM2, 7)
#define TIM2_CH1_PD4_0 CH32V00X_PINMUX_DEFINE(PD, 4, TIM2, 0)
#define TIM2_CH1_PC1_1 CH32V00X_PINMUX_DEFINE(PC, 1, TIM2, 1)
#define TIM2_CH1_PC5_2 CH32V00X_PINMUX_DEFINE(PC, 5, TIM2, 2)
#define TIM2_CH1_PC1_3 CH32V00X_PINMUX_DEFINE(PC, 1, TIM2, 3)
#define TIM2_CH1_PC0_4 CH32V00X_PINMUX_DEFINE(PC, 0, TIM2, 4)
#define TIM2_CH1_PA0_5 CH32V00X_PINMUX_DEFINE(PA, 0, TIM2, 5)
#define TIM2_CH1_PB1_6 CH32V00X_PINMUX_DEFINE(PB, 1, TIM2, 6)
#define TIM2_CH1_PD3_7 CH32V00X_PINMUX_DEFINE(PD, 3, TIM2, 7)
#define TIM2_CH2_PD3_0 CH32V00X_PINMUX_DEFINE(PD, 3, TIM2, 0)
#define TIM2_CH2_PD3_1 CH32V00X_PINMUX_DEFINE(PD, 3, TIM2, 1)
#define TIM2_CH2_PC2_2 CH32V00X_PINMUX_DEFINE(PC, 2, TIM2, 2)
/* CH32V007 specific remap */
#define TIM2_CH2_PB3_2 CH32V00X_PINMUX_DEFINE(PB, 3, TIM2, 2)
#define TIM2_CH2_PC7_3 CH32V00X_PINMUX_DEFINE(PC, 7, TIM2, 3)
#define TIM2_CH2_PC1_4 CH32V00X_PINMUX_DEFINE(PC, 1, TIM2, 4)
#define TIM2_CH2_PA1_5 CH32V00X_PINMUX_DEFINE(PA, 1, TIM2, 5)
#define TIM2_CH2_PA1_6 CH32V00X_PINMUX_DEFINE(PA, 1, TIM2, 6)
#define TIM2_CH2_PD4_7 CH32V00X_PINMUX_DEFINE(PD, 4, TIM2, 7)
#define TIM2_CH3_PC0_0 CH32V00X_PINMUX_DEFINE(PC, 0, TIM2, 0)
#define TIM2_CH3_PC0_1 CH32V00X_PINMUX_DEFINE(PC, 0, TIM2, 1)
#define TIM2_CH3_PD2_2 CH32V00X_PINMUX_DEFINE(PD, 2, TIM2, 2)
#define TIM2_CH3_PD6_3 CH32V00X_PINMUX_DEFINE(PD, 6, TIM2, 3)
#define TIM2_CH3_PC3_4 CH32V00X_PINMUX_DEFINE(PC, 3, TIM2, 4)
#define TIM2_CH3_PA2_5 CH32V00X_PINMUX_DEFINE(PA, 2, TIM2, 5)
#define TIM2_CH3_PA2_6 CH32V00X_PINMUX_DEFINE(PA, 2, TIM2, 6)
#define TIM2_CH3_PA2_7 CH32V00X_PINMUX_DEFINE(PA, 2, TIM2, 7)
#define TIM2_CH4_PD7_0 CH32V00X_PINMUX_DEFINE(PD, 7, TIM2, 0)
#define TIM2_CH4_PD7_1 CH32V00X_PINMUX_DEFINE(PD, 7, TIM2, 1)
#define TIM2_CH4_PC1_2 CH32V00X_PINMUX_DEFINE(PC, 1, TIM2, 2)
#define TIM2_CH4_PD5_3 CH32V00X_PINMUX_DEFINE(PD, 5, TIM2, 3)
#define TIM2_CH4_PB6_4 CH32V00X_PINMUX_DEFINE(PB, 6, TIM2, 4)
#define TIM2_CH4_PA3_5 CH32V00X_PINMUX_DEFINE(PA, 3, TIM2, 5)
#define TIM2_CH4_PA3_6 CH32V00X_PINMUX_DEFINE(PA, 3, TIM2, 6)
#define TIM2_CH4_PA3_7 CH32V00X_PINMUX_DEFINE(PA, 3, TIM2, 7)

#define USART1_TX_PD5_0  CH32V00X_PINMUX_DEFINE(PD, 5, USART1, 0)
#define USART1_TX_PD6_1  CH32V00X_PINMUX_DEFINE(PD, 6, USART1, 1)
#define USART1_TX_PD0_2  CH32V00X_PINMUX_DEFINE(PD, 0, USART1, 2)
#define USART1_TX_PC0_3  CH32V00X_PINMUX_DEFINE(PC, 0, USART1, 3)
#define USART1_TX_PD1_4  CH32V00X_PINMUX_DEFINE(PD, 1, USART1, 4)
#define USART1_TX_PB3_5  CH32V00X_PINMUX_DEFINE(PB, 3, USART1, 5)
#define USART1_TX_PC5_6  CH32V00X_PINMUX_DEFINE(PC, 5, USART1, 6)
#define USART1_TX_PB5_7  CH32V00X_PINMUX_DEFINE(PB, 5, USART1, 7)
#define USART1_TX_PA0_8  CH32V00X_PINMUX_DEFINE(PA, 0, USART1, 8)
#define USART1_TX_PA0_9  CH32V00X_PINMUX_DEFINE(PA, 0, USART1, 9)
#define USART1_RX_PD6_0  CH32V00X_PINMUX_DEFINE(PD, 6, USART1, 0)
#define USART1_RX_PD5_1  CH32V00X_PINMUX_DEFINE(PD, 5, USART1, 1)
#define USART1_RX_PD1_2  CH32V00X_PINMUX_DEFINE(PD, 1, USART1, 2)
#define USART1_RX_PC1_3  CH32V00X_PINMUX_DEFINE(PC, 1, USART1, 3)
#define USART1_RX_PB3_4  CH32V00X_PINMUX_DEFINE(PB, 3, USART1, 4)
#define USART1_RX_PD1_5  CH32V00X_PINMUX_DEFINE(PD, 1, USART1, 5)
#define USART1_RX_PC6_6  CH32V00X_PINMUX_DEFINE(PC, 6, USART1, 6)
#define USART1_RX_PB6_7  CH32V00X_PINMUX_DEFINE(PB, 6, USART1, 7)
#define USART1_RX_PA1_8  CH32V00X_PINMUX_DEFINE(PA, 1, USART1, 8)
#define USART1_RX_PC4_9  CH32V00X_PINMUX_DEFINE(PC, 4, USART1, 9)
#define USART1_CTS_PD3_0 CH32V00X_PINMUX_DEFINE(PD, 3, USART1, 0)
#define USART1_CTS_PC6_1 CH32V00X_PINMUX_DEFINE(PC, 6, USART1, 1)
#define USART1_CTS_PC3_2 CH32V00X_PINMUX_DEFINE(PC, 3, USART1, 2)
#define USART1_CTS_PC6_3 CH32V00X_PINMUX_DEFINE(PC, 6, USART1, 3)
#define USART1_CTS_PD7_4 CH32V00X_PINMUX_DEFINE(PD, 7, USART1, 4)
#define USART1_CTS_PD7_5 CH32V00X_PINMUX_DEFINE(PD, 7, USART1, 5)
#define USART1_CTS_PC7_6 CH32V00X_PINMUX_DEFINE(PC, 7, USART1, 6)
#define USART1_CTS_PC7_7 CH32V00X_PINMUX_DEFINE(PC, 7, USART1, 7)
#define USART1_CTS_PD2_8 CH32V00X_PINMUX_DEFINE(PD, 2, USART1, 8)
#define USART1_CTS_PD5_9 CH32V00X_PINMUX_DEFINE(PD, 5, USART1, 9)
#define USART1_RTS_PC2_0 CH32V00X_PINMUX_DEFINE(PC, 2, USART1, 0)
#define USART1_RTS_PC7_1 CH32V00X_PINMUX_DEFINE(PC, 7, USART1, 1)
#define USART1_RTS_PC2_2 CH32V00X_PINMUX_DEFINE(PC, 2, USART1, 2)
#define USART1_RTS_PC7_3 CH32V00X_PINMUX_DEFINE(PC, 7, USART1, 3)
#define USART1_RTS_PA5_4 CH32V00X_PINMUX_DEFINE(PA, 5, USART1, 4)
#define USART1_RTS_PA5_5 CH32V00X_PINMUX_DEFINE(PA, 5, USART1, 5)
#define USART1_RTS_PB4_6 CH32V00X_PINMUX_DEFINE(PB, 4, USART1, 6)
#define USART1_RTS_PB4_7 CH32V00X_PINMUX_DEFINE(PB, 4, USART1, 7)
#define USART1_RTS_PD3_8 CH32V00X_PINMUX_DEFINE(PD, 3, USART1, 8)
#define USART1_RTS_PD4_9 CH32V00X_PINMUX_DEFINE(PD, 4, USART1, 9)

#define USART2_TX_PA7_0  CH32V00X_PINMUX_DEFINE(PA, 7, USART2, 0)
#define USART2_TX_PA4_1  CH32V00X_PINMUX_DEFINE(PA, 4, USART2, 1)
#define USART2_TX_PA2_2  CH32V00X_PINMUX_DEFINE(PA, 2, USART2, 2)
#define USART2_TX_PD2_3  CH32V00X_PINMUX_DEFINE(PD, 2, USART2, 3)
#define USART2_TX_PB0_4  CH32V00X_PINMUX_DEFINE(PB, 0, USART2, 4)
#define USART2_TX_PC4_5  CH32V00X_PINMUX_DEFINE(PC, 4, USART2, 5)
#define USART2_TX_PA6_6  CH32V00X_PINMUX_DEFINE(PA, 6, USART2, 6)
#define USART2_RX_PB3_0  CH32V00X_PINMUX_DEFINE(PB, 3, USART2, 0)
#define USART2_RX_PA5_1  CH32V00X_PINMUX_DEFINE(PA, 5, USART2, 1)
#define USART2_RX_PA3_2  CH32V00X_PINMUX_DEFINE(PA, 3, USART2, 2)
#define USART2_RX_PD3_3  CH32V00X_PINMUX_DEFINE(PD, 3, USART2, 3)
#define USART2_RX_PB1_4  CH32V00X_PINMUX_DEFINE(PB, 1, USART2, 4)
#define USART2_RX_PD1_5  CH32V00X_PINMUX_DEFINE(PD, 1, USART2, 5)
#define USART2_RX_PA5_6  CH32V00X_PINMUX_DEFINE(PA, 5, USART2, 6)
#define USART2_CTS_PA4_0 CH32V00X_PINMUX_DEFINE(PA, 4, USART2, 0)
#define USART2_CTS_PA7_1 CH32V00X_PINMUX_DEFINE(PA, 7, USART2, 1)
#define USART2_CTS_PA0_2 CH32V00X_PINMUX_DEFINE(PA, 0, USART2, 2)
#define USART2_CTS_PA0_3 CH32V00X_PINMUX_DEFINE(PA, 0, USART2, 3)
#define USART2_CTS_PB6_4 CH32V00X_PINMUX_DEFINE(PB, 6, USART2, 4)
#define USART2_CTS_PA4_5 CH32V00X_PINMUX_DEFINE(PA, 4, USART2, 5)
#define USART2_CTS_PA7_6 CH32V00X_PINMUX_DEFINE(PA, 7, USART2, 6)
#define USART2_RTS_PA5_0 CH32V00X_PINMUX_DEFINE(PA, 5, USART2, 0)
#define USART2_RTS_PB3_1 CH32V00X_PINMUX_DEFINE(PB, 3, USART2, 1)
#define USART2_RTS_PA1_2 CH32V00X_PINMUX_DEFINE(PA, 1, USART2, 2)
#define USART2_RTS_PA1_3 CH32V00X_PINMUX_DEFINE(PA, 1, USART2, 3)
#define USART2_RTS_PA1_4 CH32V00X_PINMUX_DEFINE(PA, 1, USART2, 4)
#define USART2_RTS_PA1_5 CH32V00X_PINMUX_DEFINE(PA, 1, USART2, 5)
#define USART2_RTS_PB3_6 CH32V00X_PINMUX_DEFINE(PB, 3, USART2, 6)

#define SPI1_NSS_PC1_0  CH32V00X_PINMUX_DEFINE(PC, 1, SPI1, 0)
#define SPI1_NSS_PC0_1  CH32V00X_PINMUX_DEFINE(PC, 0, SPI1, 1)
#define SPI1_NSS_PC4_2  CH32V00X_PINMUX_DEFINE(PC, 4, SPI1, 2)
#define SPI1_NSS_PB0_3  CH32V00X_PINMUX_DEFINE(PB, 0, SPI1, 3)
#define SPI1_NSS_PD3_4  CH32V00X_PINMUX_DEFINE(PD, 3, SPI1, 4)
#define SPI1_NSS_PC1_5  CH32V00X_PINMUX_DEFINE(PC, 1, SPI1, 5)
#define SPI1_NSS_PC4_6  CH32V00X_PINMUX_DEFINE(PC, 4, SPI1, 6)
#define SPI1_SCK_PC5_0  CH32V00X_PINMUX_DEFINE(PC, 5, SPI1, 0)
#define SPI1_SCK_PC5_1  CH32V00X_PINMUX_DEFINE(PC, 5, SPI1, 1)
#define SPI1_SCK_PD2_2  CH32V00X_PINMUX_DEFINE(PD, 2, SPI1, 2)
#define SPI1_SCK_PB1_3  CH32V00X_PINMUX_DEFINE(PB, 1, SPI1, 3)
#define SPI1_SCK_PD4_4  CH32V00X_PINMUX_DEFINE(PD, 4, SPI1, 4)
#define SPI1_SCK_PA1_5  CH32V00X_PINMUX_DEFINE(PA, 1, SPI1, 5)
#define SPI1_SCK_PB5_6  CH32V00X_PINMUX_DEFINE(PB, 5, SPI1, 6)
#define SPI1_MISO_PC7_0 CH32V00X_PINMUX_DEFINE(PC, 7, SPI1, 0)
#define SPI1_MISO_PC7_1 CH32V00X_PINMUX_DEFINE(PC, 7, SPI1, 1)
#define SPI1_MISO_PB3_2 CH32V00X_PINMUX_DEFINE(PB, 3, SPI1, 2)
#define SPI1_MISO_PB2_3 CH32V00X_PINMUX_DEFINE(PB, 2, SPI1, 3)
#define SPI1_MISO_PD5_4 CH32V00X_PINMUX_DEFINE(PD, 5, SPI1, 4)
#define SPI1_MISO_PB5_5 CH32V00X_PINMUX_DEFINE(PB, 5, SPI1, 5)
#define SPI1_MISO_PC7_6 CH32V00X_PINMUX_DEFINE(PC, 7, SPI1, 6)
#define SPI1_MOSI_PC6_0 CH32V00X_PINMUX_DEFINE(PC, 6, SPI1, 0)
#define SPI1_MOSI_PC6_1 CH32V00X_PINMUX_DEFINE(PC, 6, SPI1, 1)
#define SPI1_MOSI_PD3_2 CH32V00X_PINMUX_DEFINE(PD, 3, SPI1, 2)
#define SPI1_MOSI_PC0_3 CH32V00X_PINMUX_DEFINE(PC, 0, SPI1, 3)
#define SPI1_MOSI_PD6_4 CH32V00X_PINMUX_DEFINE(PD, 6, SPI1, 4)
#define SPI1_MOSI_PA2_5 CH32V00X_PINMUX_DEFINE(PA, 2, SPI1, 5)
#define SPI1_MOSI_PB4_6 CH32V00X_PINMUX_DEFINE(PB, 4, SPI1, 6)

#define I2C1_SCL_PC2_0 CH32V00X_PINMUX_DEFINE(PC, 2, I2C1, 0)
#define I2C1_SCL_PD1_1 CH32V00X_PINMUX_DEFINE(PD, 1, I2C1, 1)
#define I2C1_SCL_PC5_2 CH32V00X_PINMUX_DEFINE(PC, 5, I2C1, 2)
#define I2C1_SCL_PB5_3 CH32V00X_PINMUX_DEFINE(PB, 5, I2C1, 3)
#define I2C1_SCL_PB3_4 CH32V00X_PINMUX_DEFINE(PB, 3, I2C1, 4)
#define I2C1_SDA_PC1_0 CH32V00X_PINMUX_DEFINE(PC, 1, I2C1, 0)
#define I2C1_SDA_PD0_1 CH32V00X_PINMUX_DEFINE(PD, 0, I2C1, 1)
#define I2C1_SDA_PC6_2 CH32V00X_PINMUX_DEFINE(PC, 6, I2C1, 2)
/* CH32V007 specific remap */
#define I2C1_SDA_PC4_2 CH32V00X_PINMUX_DEFINE(PC, 4, I2C1, 2)
#define I2C1_SDA_PB6_3 CH32V00X_PINMUX_DEFINE(PB, 6, I2C1, 3)
#define I2C1_SDA_PD1_4 CH32V00X_PINMUX_DEFINE(PD, 1, I2C1, 4)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_CH32V00X_PINCTRL_H_ */
```

## 5.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Michael Hope <michaelh@juju.nz>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 15 行

PCFR1 中重映射字段（Remap Field）的起始位（Starting Bit）。

### 注释 3：原第 26 行

端口编号（Port Number）：0～3。

### 注释 4：原第 29 行

引脚编号（Pin Number）：0～7。

### 注释 5：原第 32 行

重映射基础位（Base Remap Bit）：0～31。

### 注释 6：原第 35 行

功能重映射标识（Function Remapping ID）：0～7。

### 注释 7：原第 155 行

CH32V007 专用重映射（Specific Remap）。

### 注释 8：原第 286 行

CH32V007 专用重映射（Specific Remap）。

### 注释 9：原第 291 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_CH32V00X_PINCTRL_H_`。

## 5.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P038_zephyr__dt-bindings__pinctrl__ch32v00x-pinctrl.h_文件参考.md)

---

[上一章](P004_ch32v003-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P006_mtch9010.h_源码浏览.md)
