---
id: learning.zephyr-docs.api-source-device-reference.page-24
title: lpc84x-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lpc84x-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_lpc84x-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/lpc84x-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/lpc84x-pinctrl_8h.html)。

## 24.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00021"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
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
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
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

```c
/*
 * Copyright (c) 2026 Aerlync Labs Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_LPC84X_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_LPC84X_PINCTRL_H_



#define LPC84X_PINMUX_M(func, pin) (((func) << 16) | (pin))



#define LPC84X_PINMUX_F(func, pin) ((1U << 23) | ((func) << 16) | (pin))

#define LPC84X_SWM_USART0_TXD    0U
#define LPC84X_SWM_USART0_RXD    1U
#define LPC84X_SWM_USART0_RTS    2U
#define LPC84X_SWM_USART0_CTS    3U
#define LPC84X_SWM_USART0_SCLK   4U
#define LPC84X_SWM_USART1_TXD    5U
#define LPC84X_SWM_USART1_RXD    6U
#define LPC84X_SWM_USART1_RTS    7U
#define LPC84X_SWM_USART1_CTS    8U
#define LPC84X_SWM_USART1_SCLK   9U
#define LPC84X_SWM_USART2_TXD    10U
#define LPC84X_SWM_USART2_RXD    11U
#define LPC84X_SWM_USART2_RTS    12U
#define LPC84X_SWM_USART2_CTS    13U
#define LPC84X_SWM_USART2_SCLK   14U
#define LPC84X_SWM_SPI0_SCK      15U
#define LPC84X_SWM_SPI0_MOSI     16U
#define LPC84X_SWM_SPI0_MISO     17U
#define LPC84X_SWM_SPI0_SSEL0    18U
#define LPC84X_SWM_SPI0_SSEL1    19U
#define LPC84X_SWM_SPI0_SSEL2    20U
#define LPC84X_SWM_SPI0_SSEL3    21U
#define LPC84X_SWM_SPI1_SCK      22U
#define LPC84X_SWM_SPI1_MOSI     23U
#define LPC84X_SWM_SPI1_MISO     24U
#define LPC84X_SWM_SPI1_SSEL0    25U
#define LPC84X_SWM_SPI1_SSEL1    26U
#define LPC84X_SWM_SCT_PIN0      27U
#define LPC84X_SWM_SCT_PIN1      28U
#define LPC84X_SWM_SCT_PIN2      29U
#define LPC84X_SWM_SCT_PIN3      30U
#define LPC84X_SWM_SCT_OUT0      31U
#define LPC84X_SWM_SCT_OUT1      32U
#define LPC84X_SWM_SCT_OUT2      33U
#define LPC84X_SWM_SCT_OUT3      34U
#define LPC84X_SWM_SCT_OUT4      35U
#define LPC84X_SWM_SCT_OUT5      36U
#define LPC84X_SWM_SCT_OUT6      37U
#define LPC84X_SWM_I2C1_SDA      38U
#define LPC84X_SWM_I2C1_SCL      39U
#define LPC84X_SWM_I2C2_SDA      40U
#define LPC84X_SWM_I2C2_SCL      41U
#define LPC84X_SWM_I2C3_SDA      42U
#define LPC84X_SWM_I2C3_SCL      43U
#define LPC84X_SWM_ACMP_OUT      44U
#define LPC84X_SWM_CLKOUT        45U
#define LPC84X_SWM_GPIO_INT_BMAT 46U
#define LPC84X_SWM_USART3_TXD    47U
#define LPC84X_SWM_USART3_RXD    48U
#define LPC84X_SWM_USART3_SCLK   49U
#define LPC84X_SWM_USART4_TXD    50U
#define LPC84X_SWM_USART4_RXD    51U
#define LPC84X_SWM_USART4_SCLK   52U
#define LPC84X_SWM_T0_MAT_CHN0   53U
#define LPC84X_SWM_T0_MAT_CHN1   54U
#define LPC84X_SWM_T0_MAT_CHN2   55U
#define LPC84X_SWM_T0_MAT_CHN3   56U
#define LPC84X_SWM_T0_CAP_CHN0   57U
#define LPC84X_SWM_T0_CAP_CHN1   58U
#define LPC84X_SWM_T0_CAP_CHN2   59U

/* SWM fixed pin selection */
#define LPC84X_SWM_ACMP_INPUT1 0U
#define LPC84X_SWM_ACMP_INPUT2 1U
#define LPC84X_SWM_ACMP_INPUT3 2U
#define LPC84X_SWM_ACMP_INPUT4 3U
#define LPC84X_SWM_ACMP_INPUT5 4U
#define LPC84X_SWM_SWCLK       5U
#define LPC84X_SWM_SWDIO       6U
#define LPC84X_SWM_XTALIN      7U
#define LPC84X_SWM_XTALOUT     8U
#define LPC84X_SWM_RESETN      9U
#define LPC84X_SWM_CLKIN       10U
#define LPC84X_SWM_VDDCMP      11U
#define LPC84X_SWM_I2C0_SDA    12U
#define LPC84X_SWM_I2C0_SCL    13U
#define LPC84X_SWM_ADC_CHN0    14U
#define LPC84X_SWM_ADC_CHN1    15U
#define LPC84X_SWM_ADC_CHN2    16U
#define LPC84X_SWM_ADC_CHN3    17U
#define LPC84X_SWM_ADC_CHN4    18U
#define LPC84X_SWM_ADC_CHN5    19U
#define LPC84X_SWM_ADC_CHN6    20U
#define LPC84X_SWM_ADC_CHN7    21U
#define LPC84X_SWM_ADC_CHN8    22U
#define LPC84X_SWM_ADC_CHN9    23U
#define LPC84X_SWM_ADC_CHN10   24U
#define LPC84X_SWM_ADC_CHN11   25U
#define LPC84X_SWM_DAC_OUT0    26U
#define LPC84X_SWM_DAC_OUT1    27U
#define LPC84X_SWM_CAPT_X0     28U
#define LPC84X_SWM_CAPT_X1     29U
#define LPC84X_SWM_CAPT_X2     30U
#define LPC84X_SWM_CAPT_X3     31U
#define LPC84X_SWM_CAPT_X4     32U
#define LPC84X_SWM_CAPT_X5     33U
#define LPC84X_SWM_CAPT_X6     34U
#define LPC84X_SWM_CAPT_X7     35U
#define LPC84X_SWM_CAPT_X8     36U
#define LPC84X_SWM_CAPT_YL     37U
#define LPC84X_SWM_CAPT_YH     38U


/* Port 0 */
#define LPC84X_PIN_P0_0  0U
#define LPC84X_PIN_P0_1  1U
#define LPC84X_PIN_P0_2  2U
#define LPC84X_PIN_P0_3  3U
#define LPC84X_PIN_P0_4  4U
#define LPC84X_PIN_P0_5  5U
#define LPC84X_PIN_P0_6  6U
#define LPC84X_PIN_P0_7  7U
#define LPC84X_PIN_P0_8  8U
#define LPC84X_PIN_P0_9  9U
#define LPC84X_PIN_P0_10 10U
#define LPC84X_PIN_P0_11 11U
#define LPC84X_PIN_P0_12 12U
#define LPC84X_PIN_P0_13 13U
#define LPC84X_PIN_P0_14 14U
#define LPC84X_PIN_P0_15 15U
#define LPC84X_PIN_P0_16 16U
#define LPC84X_PIN_P0_17 17U
#define LPC84X_PIN_P0_18 18U
#define LPC84X_PIN_P0_19 19U
#define LPC84X_PIN_P0_20 20U
#define LPC84X_PIN_P0_21 21U
#define LPC84X_PIN_P0_22 22U
#define LPC84X_PIN_P0_23 23U
#define LPC84X_PIN_P0_24 24U
#define LPC84X_PIN_P0_25 25U
#define LPC84X_PIN_P0_26 26U
#define LPC84X_PIN_P0_27 27U
#define LPC84X_PIN_P0_28 28U
#define LPC84X_PIN_P0_29 29U
#define LPC84X_PIN_P0_30 30U
#define LPC84X_PIN_P0_31 31U

/* Port 1 */
#define LPC84X_PIN_P1_0  32U
#define LPC84X_PIN_P1_1  33U
#define LPC84X_PIN_P1_2  34U
#define LPC84X_PIN_P1_3  35U
#define LPC84X_PIN_P1_4  36U
#define LPC84X_PIN_P1_5  37U
#define LPC84X_PIN_P1_6  38U
#define LPC84X_PIN_P1_7  39U
#define LPC84X_PIN_P1_8  40U
#define LPC84X_PIN_P1_9  41U
#define LPC84X_PIN_P1_10 42U
#define LPC84X_PIN_P1_11 43U
#define LPC84X_PIN_P1_12 44U
#define LPC84X_PIN_P1_13 45U
#define LPC84X_PIN_P1_14 46U
#define LPC84X_PIN_P1_15 47U
#define LPC84X_PIN_P1_16 48U
#define LPC84X_PIN_P1_17 49U
#define LPC84X_PIN_P1_18 50U
#define LPC84X_PIN_P1_19 51U
#define LPC84X_PIN_P1_20 52U
#define LPC84X_PIN_P1_21 53U

#define IOCON_INDEX_PIO0_17 0U
#define IOCON_INDEX_PIO0_13 1U
#define IOCON_INDEX_PIO0_12 2U
#define IOCON_INDEX_PIO0_5  3U
#define IOCON_INDEX_PIO0_4  4U
#define IOCON_INDEX_PIO0_3  5U
#define IOCON_INDEX_PIO0_2  6U
#define IOCON_INDEX_PIO0_11 7U
#define IOCON_INDEX_PIO0_10 8U
#define IOCON_INDEX_PIO0_16 9U
#define IOCON_INDEX_PIO0_15 10U
#define IOCON_INDEX_PIO0_1  11U
#define IOCON_INDEX_PIO0_9  13U
#define IOCON_INDEX_PIO0_8  14U
#define IOCON_INDEX_PIO0_7  15U
#define IOCON_INDEX_PIO0_6  16U
#define IOCON_INDEX_PIO0_0  17U
#define IOCON_INDEX_PIO0_14 18U
#define IOCON_INDEX_PIO0_28 20U
#define IOCON_INDEX_PIO0_27 21U
#define IOCON_INDEX_PIO0_26 22U
#define IOCON_INDEX_PIO0_25 23U
#define IOCON_INDEX_PIO0_24 24U
#define IOCON_INDEX_PIO0_23 25U
#define IOCON_INDEX_PIO0_22 26U
#define IOCON_INDEX_PIO0_21 27U
#define IOCON_INDEX_PIO0_20 28U
#define IOCON_INDEX_PIO0_19 29U
#define IOCON_INDEX_PIO0_18 30U
#define IOCON_INDEX_PIO1_8  31U
#define IOCON_INDEX_PIO1_9  32U
#define IOCON_INDEX_PIO1_12 33U
#define IOCON_INDEX_PIO1_13 34U
#define IOCON_INDEX_PIO0_31 35U
#define IOCON_INDEX_PIO1_0  36U
#define IOCON_INDEX_PIO1_1  37U
#define IOCON_INDEX_PIO1_2  38U
#define IOCON_INDEX_PIO1_14 39U
#define IOCON_INDEX_PIO1_15 40U
#define IOCON_INDEX_PIO1_3  41U
#define IOCON_INDEX_PIO1_4  42U
#define IOCON_INDEX_PIO1_5  43U
#define IOCON_INDEX_PIO1_16 44U
#define IOCON_INDEX_PIO1_17 45U
#define IOCON_INDEX_PIO1_6  46U
#define IOCON_INDEX_PIO1_18 47U
#define IOCON_INDEX_PIO1_19 48U
#define IOCON_INDEX_PIO1_7  49U
#define IOCON_INDEX_PIO0_29 50U
#define IOCON_INDEX_PIO0_30 51U
#define IOCON_INDEX_PIO1_20 52U
#define IOCON_INDEX_PIO1_21 53U
#define IOCON_INDEX_PIO1_11 54U
#define IOCON_INDEX_PIO1_10 55U


/* < Pin define encoder */
#define LPC84X_PIN_DEFINE(swm, iocon) ((((swm) & 0xFF) << 8) | ((iocon) & 0xFF))


#define P0_0  LPC84X_PIN_DEFINE(LPC84X_PIN_P0_0, IOCON_INDEX_PIO0_0)
#define P0_1  LPC84X_PIN_DEFINE(LPC84X_PIN_P0_1, IOCON_INDEX_PIO0_1)
#define P0_2  LPC84X_PIN_DEFINE(LPC84X_PIN_P0_2, IOCON_INDEX_PIO0_2)
#define P0_3  LPC84X_PIN_DEFINE(LPC84X_PIN_P0_3, IOCON_INDEX_PIO0_3)
#define P0_4  LPC84X_PIN_DEFINE(LPC84X_PIN_P0_4, IOCON_INDEX_PIO0_4)
#define P0_5  LPC84X_PIN_DEFINE(LPC84X_PIN_P0_5, IOCON_INDEX_PIO0_5)
#define P0_6  LPC84X_PIN_DEFINE(LPC84X_PIN_P0_6, IOCON_INDEX_PIO0_6)
#define P0_7  LPC84X_PIN_DEFINE(LPC84X_PIN_P0_7, IOCON_INDEX_PIO0_7)
#define P0_8  LPC84X_PIN_DEFINE(LPC84X_PIN_P0_8, IOCON_INDEX_PIO0_8)
#define P0_9  LPC84X_PIN_DEFINE(LPC84X_PIN_P0_9, IOCON_INDEX_PIO0_9)
#define P0_10 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_10, IOCON_INDEX_PIO0_10)
#define P0_11 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_11, IOCON_INDEX_PIO0_11)
#define P0_12 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_12, IOCON_INDEX_PIO0_12)
#define P0_13 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_13, IOCON_INDEX_PIO0_13)
#define P0_14 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_14, IOCON_INDEX_PIO0_14)
#define P0_15 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_15, IOCON_INDEX_PIO0_15)
#define P0_16 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_16, IOCON_INDEX_PIO0_16)
#define P0_17 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_17, IOCON_INDEX_PIO0_17)
#define P0_18 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_18, IOCON_INDEX_PIO0_18)
#define P0_19 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_19, IOCON_INDEX_PIO0_19)
#define P0_20 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_20, IOCON_INDEX_PIO0_20)
#define P0_21 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_21, IOCON_INDEX_PIO0_21)
#define P0_22 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_22, IOCON_INDEX_PIO0_22)
#define P0_23 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_23, IOCON_INDEX_PIO0_23)
#define P0_24 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_24, IOCON_INDEX_PIO0_24)
#define P0_25 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_25, IOCON_INDEX_PIO0_25)
#define P0_26 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_26, IOCON_INDEX_PIO0_26)
#define P0_27 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_27, IOCON_INDEX_PIO0_27)
#define P0_28 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_28, IOCON_INDEX_PIO0_28)
#define P0_29 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_29, IOCON_INDEX_PIO0_29)
#define P0_30 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_30, IOCON_INDEX_PIO0_30)
#define P0_31 LPC84X_PIN_DEFINE(LPC84X_PIN_P0_31, IOCON_INDEX_PIO0_31)
#define P1_0  LPC84X_PIN_DEFINE(LPC84X_PIN_P1_0, IOCON_INDEX_PIO1_0)
#define P1_1  LPC84X_PIN_DEFINE(LPC84X_PIN_P1_1, IOCON_INDEX_PIO1_1)
#define P1_2  LPC84X_PIN_DEFINE(LPC84X_PIN_P1_2, IOCON_INDEX_PIO1_2)
#define P1_3  LPC84X_PIN_DEFINE(LPC84X_PIN_P1_3, IOCON_INDEX_PIO1_3)
#define P1_4  LPC84X_PIN_DEFINE(LPC84X_PIN_P1_4, IOCON_INDEX_PIO1_4)
#define P1_5  LPC84X_PIN_DEFINE(LPC84X_PIN_P1_5, IOCON_INDEX_PIO1_5)
#define P1_6  LPC84X_PIN_DEFINE(LPC84X_PIN_P1_6, IOCON_INDEX_PIO1_6)
#define P1_7  LPC84X_PIN_DEFINE(LPC84X_PIN_P1_7, IOCON_INDEX_PIO1_7)
#define P1_8  LPC84X_PIN_DEFINE(LPC84X_PIN_P1_8, IOCON_INDEX_PIO1_8)
#define P1_9  LPC84X_PIN_DEFINE(LPC84X_PIN_P1_9, IOCON_INDEX_PIO1_9)
#define P1_10 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_10, IOCON_INDEX_PIO1_10)
#define P1_11 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_11, IOCON_INDEX_PIO1_11)
#define P1_12 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_12, IOCON_INDEX_PIO1_12)
#define P1_13 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_13, IOCON_INDEX_PIO1_13)
#define P1_14 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_14, IOCON_INDEX_PIO1_14)
#define P1_15 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_15, IOCON_INDEX_PIO1_15)
#define P1_16 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_16, IOCON_INDEX_PIO1_16)
#define P1_17 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_17, IOCON_INDEX_PIO1_17)
#define P1_18 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_18, IOCON_INDEX_PIO1_18)
#define P1_19 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_19, IOCON_INDEX_PIO1_19)
#define P1_20 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_20, IOCON_INDEX_PIO1_20)
#define P1_21 LPC84X_PIN_DEFINE(LPC84X_PIN_P1_21, IOCON_INDEX_PIO1_21)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_LPC84X_PINCTRL_H_ */
```

## 24.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Aerlync Labs Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 99 行

开关矩阵固定引脚选择（SWM Fixed Pin Selection）。

### 注释 3：原第 146 行

端口 0（Port 0）。

### 注释 4：原第 180 行

端口 1（Port 1）。

### 注释 5：原第 270 行

引脚定义编码器（Pin Define Encoder）。

### 注释 6：原第 335 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_LPC84X_PINCTRL_H_`。

## 24.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/lpc84x-pinctrl_8h.html)

---

[上一章](P023_lp50xx.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P025_microchip-sam-gpio.h_源码浏览.md)
