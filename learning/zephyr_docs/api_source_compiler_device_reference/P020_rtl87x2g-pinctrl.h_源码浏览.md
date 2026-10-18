---
id: learning.zephyr-docs.api-source-compiler-device-reference.page-20
title: rtl87x2g-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rtl87x2g-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_rtl87x2g-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/rtl87x2g-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/rtl87x2g-pinctrl_8h.html)。

## 20.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
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
<a id="l00224"></a>
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
<a id="l00317"></a>
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
<a id="l00425"></a>
<a id="l00426"></a>
<a id="abee-pinctrl_8h_html"></a>

```c
/*
 * Copyright (c) 2026, Realtek Semiconductor Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RTL87X2G_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RTL87X2G_PINCTRL_H_

#include "bee-pinctrl.h"

#define BEE_IDLE_MODE          0
#define BEE_UART0_TX           1
#define BEE_UART0_RX           2
#define BEE_UART0_CTS          3
#define BEE_UART0_RTS          4
#define BEE_UART1_TX           5
#define BEE_UART1_RX           6
#define BEE_UART1_CTS          7
#define BEE_UART1_RTS          8
#define BEE_UART2_TX           9
#define BEE_UART2_RX           10
#define BEE_UART2_CTS          11
#define BEE_UART2_RTS          12
#define BEE_UART3_TX           13
#define BEE_UART3_RX           14
#define BEE_UART3_CTS          15
#define BEE_UART3_RTS          16
#define BEE_UART4_TX           17
#define BEE_UART4_RX           18
#define BEE_UART4_CTS          19
#define BEE_UART4_RTS          20
#define BEE_UART5_TX           21
#define BEE_UART5_RX           22
#define BEE_UART5_CTS          23
#define BEE_UART5_RTS          24
#define BEE_I2C0_CLK           29
#define BEE_I2C0_DAT           30
#define BEE_I2C1_CLK           31
#define BEE_I2C1_DAT           32
#define BEE_I2C2_CLK           33
#define BEE_I2C2_DAT           34
#define BEE_I2C3_CLK           35
#define BEE_I2C3_DAT           36
#define BEE_SPI0_CLK_MASTER    37
#define BEE_SPI0_MO_MASTER     38
#define BEE_SPI0_MI_MASTER     39
#define BEE_SPI0_CSN_0_MASTER  40
#define BEE_SPI0_CSN_1_MASTER  41
#define BEE_SPI0_CSN_2_MASTER  42
#define BEE_SPI0_CSN_0_SLAVE   43
#define BEE_SPI0_CLK_SLAVE     44
#define BEE_SPI0_SO_SLAVE      45
#define BEE_SPI0_SI_SLAVE      46
#define BEE_SPI1_CLK_MASTER    47
#define BEE_SPI1_MO_MASTER     48
#define BEE_SPI1_MI_MASTER     49
#define BEE_SPI1_CSN_0_MASTER  50
#define BEE_SPI1_CSN_1_MASTER  51
#define BEE_SPI1_CSN_2_MASTER  52
#define BEE_SPI2W_DATA         53
#define BEE_SPI2W_CLK          54
#define BEE_SPI2W_CS           55
#define BEE_ENPWM0_P           65
#define BEE_ENPWM0_N           66
#define BEE_ENPWM1_P           67
#define BEE_ENPWM1_N           68
#define BEE_ENPWM2_P           69
#define BEE_ENPWM2_N           70
#define BEE_ENPWM3_P           71
#define BEE_ENPWM3_N           72
#define BEE_TIMER_PWM2         83
#define BEE_TIMER_PWM3         84
#define BEE_ISO7816_RST        85
#define BEE_ISO7816_CLK        86
#define BEE_ISO7816_IO         87
#define BEE_ISO7816_VCC_EN     88
#define BEE_DWGPIO             89
#define BEE_IRDA_TX            90
#define BEE_IRDA_RX            91
#define BEE_TIMER_PWM4         92
#define BEE_TIMER_PWM5         93
#define BEE_TIMER_PWM6         94
#define BEE_TIMER_PWM7         95
#define BEE_TIMER_PWM2_P       96
#define BEE_TIMER_PWM2_N       97
#define BEE_TIMER_PWM3_P       98
#define BEE_TIMER_PWM3_N       99
#define BEE_KEY_COL_0          100
#define BEE_KEY_COL_1          101
#define BEE_KEY_COL_2          102
#define BEE_KEY_COL_3          103
#define BEE_KEY_COL_4          104
#define BEE_KEY_COL_5          105
#define BEE_KEY_COL_6          106
#define BEE_KEY_COL_7          107
#define BEE_KEY_COL_8          108
#define BEE_KEY_COL_9          109
#define BEE_KEY_COL_10         110
#define BEE_KEY_COL_11         111
#define BEE_KEY_COL_12         112
#define BEE_KEY_COL_13         113
#define BEE_KEY_COL_14         114
#define BEE_KEY_COL_15         115
#define BEE_KEY_COL_16         116
#define BEE_KEY_COL_17         117
#define BEE_KEY_COL_18         118
#define BEE_KEY_COL_19         119
#define BEE_KEY_ROW_0          120
#define BEE_KEY_ROW_1          121
#define BEE_KEY_ROW_2          122
#define BEE_KEY_ROW_3          123
#define BEE_KEY_ROW_4          124
#define BEE_KEY_ROW_5          125
#define BEE_KEY_ROW_6          126
#define BEE_KEY_ROW_7          127
#define BEE_KEY_ROW_8          128
#define BEE_KEY_ROW_9          129
#define BEE_KEY_ROW_10         130
#define BEE_KEY_ROW_11         131
#define BEE_KM4_CLK_DIV_4      138
#define BEE_CARD_DETECT_N_0    147
#define BEE_BIU_VOLT_REG_0     148
#define BEE_BACK_END_POWER_0   149
#define BEE_CARD_INT_N_SDHC_0  150
#define BEE_A2C_TX             155
#define BEE_A2C_RX             156
#define BEE_LRC_SPORT1         157
#define BEE_BCLK_SPORT1        158
#define BEE_ADCDAT_SPORT1      159
#define BEE_DACDAT_SPORT1      160
#define BEE_DMIC1_CLK          162
#define BEE_DMIC1_DAT          163
#define BEE_LRC_I_CODEC_SLAVE  164
#define BEE_BCLK_I_CODEC_SLAVE 165
#define BEE_SDI_CODEC_SLAVE    166
#define BEE_SDO_CODEC_SLAVE    167
#define BEE_LRC_SPORT0         172
#define BEE_BCLK_SPORT0        173
#define BEE_ADCDAT_SPORT0      174
#define BEE_DACDAT_SPORT0      175
#define BEE_MCLK_OUT           176
#define BEE_MCLK_IN            189
#define BEE_LRC_RX_CODEC_SLAVE 190
#define BEE_LRC_RX_SPORT0      191
#define BEE_LRC_RX_SPORT1      192
#define BEE_PDM_DATA           196
#define BEE_PDM_CLK            197
#define BEE_I2S1_LRC_TX_SLAVE  198
#define BEE_I2S1_BCLK_SLAVE    199
#define BEE_I2S1_SDI_SLAVE     200
#define BEE_I2S1_SDO_SLAVE     201
#define BEE_I2S1_LRC_RX_SLAVE  202
#define BEE_BT_COEX_I_0        216
#define BEE_BT_COEX_I_1        217
#define BEE_BT_COEX_I_2        218
#define BEE_BT_COEX_I_3        219
#define BEE_BT_COEX_O_0        220
#define BEE_BT_COEX_O_1        221
#define BEE_BT_COEX_O_2        222
#define BEE_BT_COEX_O_3        223
#define BEE_PTA_I2C_CLK_SLAVE  224
#define BEE_PTA_I2C_DAT_SLAVE  225
#define BEE_PTA_I2C_INT_OUT    226
#define BEE_EN_EXPA            227
#define BEE_EN_EXLNA           228
#define BEE_SEL_TPM_SW         229
#define BEE_SEL_TPM_N_SW       230
#define BEE_ANT_SW0            231
#define BEE_ANT_SW1            232
#define BEE_ANT_SW2            233
#define BEE_ANT_SW3            234
#define BEE_ANT_SW4            235
#define BEE_ANT_SW5            236
#define BEE_PHY_GPIO_1         237
#define BEE_PHY_GPIO_2         238
#define BEE_SLOW_DEBUG_MUX_1   239
#define BEE_SLOW_DEBUG_MUX_2   240
#define BEE_TEST_MODE          246
#define BEE_SWD_CLK            253
#define BEE_SWD_DIO            254
#define BEE_DIG_DEBUG          255
#define BEE_PINMUX_MAX         (BEE_DIG_DEBUG + 1)
#define BEE_SW_MODE            (BEE_PINMUX_MAX + 1)
#define BEE_PWR_OFF            (BEE_PINMUX_MAX + 2)
#define BEE_SDHC0_CLK_P9_4     (BEE_PWR_OFF + 1)
#define BEE_SDHC0_CMD_P9_3     (BEE_PWR_OFF + 2)
#define BEE_SDHC0_D0_P10_0     (BEE_PWR_OFF + 3)
#define BEE_SDHC0_D1_P9_7      (BEE_PWR_OFF + 4)
#define BEE_SDHC0_D2_P9_6      (BEE_PWR_OFF + 5)
#define BEE_SDHC0_D3_P9_5      (BEE_PWR_OFF + 6)
#define BEE_SDHC0_D4_P4_4      (BEE_PWR_OFF + 7)
#define BEE_SDHC0_D5_P4_5      (BEE_PWR_OFF + 8)
#define BEE_SDHC0_D6_P4_6      (BEE_PWR_OFF + 9)
#define BEE_SDHC0_D7_P4_7      (BEE_PWR_OFF + 10)
#define BEE_SDHC1_CLK_P9_4     (BEE_PWR_OFF + 11)
#define BEE_SDHC1_CMD_P9_3     (BEE_PWR_OFF + 12)
#define BEE_SDHC1_D0_P10_0     (BEE_PWR_OFF + 13)
#define BEE_SDHC1_D1_P9_7      (BEE_PWR_OFF + 14)
#define BEE_SDHC1_D2_P9_6      (BEE_PWR_OFF + 15)
#define BEE_SDHC1_D3_P9_5      (BEE_PWR_OFF + 16)
#define BEE_SDHC1_D4_P4_4      (BEE_PWR_OFF + 17)
#define BEE_SDHC1_D5_P4_5      (BEE_PWR_OFF + 18)
#define BEE_SDHC1_D6_P4_6      (BEE_PWR_OFF + 19)
#define BEE_SDHC1_D7_P4_7      (BEE_PWR_OFF + 20)
#define BEE_QDPH0_IN_NONE      0x0F00
#define BEE_QDPH0_IN_P1_3_P1_4 0x0F01
#define BEE_QDPH0_IN_P5_6_P5_7 0x0F02
#define BEE_QDPH0_IN_P9_0_P9_1 0x0F03
#define BEE_PIN_DISCONNECTED   BEE_PIN_MSK

#define P0_0    0
#define P0_1    1
#define P0_2    2
/* Note: P0_3 defaults to outputting the Realtek internal log for rtl87x2g. */
#define P0_3    3
#define P0_4    4
#define P0_5    5
#define P0_6    6
#define P0_7    7
/* Note: P1_0/P1_1 default to SWD function for rtl87x2g. */
#define P1_0    8
#define P1_1    9
#define P1_2    10
#define P1_3    11
#define P1_4    12
#define P1_5    13
#define P1_6    14
#define P1_7    15
#define P2_0    16
#define P2_1    17
#define P2_2    18
#define P2_3    19
#define P2_4    20
#define P2_5    21
#define P2_6    22
#define P2_7    23
#define P3_0    24
#define P3_1    25
#define P3_2    26
#define P3_3    27
#define P3_4    28
#define P3_5    29
#define P3_6    30
#define P3_7    31
#define P4_0    32
#define P4_1    33
#define P4_2    34
#define P4_3    35
#define P4_4    36
#define P4_5    37
#define P4_6    38
#define P4_7    39
#define P5_0    40
#define P5_1    41
#define P5_2    42
#define P5_3    43
#define P5_4    44
#define P5_5    45
#define P5_6    46
#define P5_7    47
#define P6_0    48
#define P6_1    49
#define P6_2    50
#define P6_3    51
#define P6_4    52
#define P6_5    53
#define P6_6    54
#define P6_7    55
#define P7_0    56
#define P7_1    57
#define P7_2    58
#define P7_3    59
#define P7_4    60
#define MICBIAS 64
#define XI32K   65
#define XO32K   66
#define DACP    67
#define DACN    68
#define P9_0    72
#define P9_1    73
#define P9_2    74
#define P9_3    75
#define P9_4    76
#define P9_5    77
#define P9_6    78
#define P9_7    79
#define P10_0   80
#define P10_1   81
#define P10_2   82
#define ADC_0   P2_0
#define ADC_1   P2_1
#define ADC_2   P2_2
#define ADC_3   P2_3
#define ADC_4   P2_4
#define ADC_5   P2_5
#define ADC_6   P2_6
#define ADC_7   P2_7

/* Port 0 */
#define BEE_PSEL_GPIOA_0_P0_0 BEE_PSEL(DWGPIO, P0_0)
#define BEE_PSEL_GPIOA_1_P0_1 BEE_PSEL(DWGPIO, P0_1)
#define BEE_PSEL_GPIOA_2_P0_2 BEE_PSEL(DWGPIO, P0_2)
/* Note: P0_3 defaults to outputting the Realtek internal log for rtl87x2g. */
#define BEE_PSEL_GPIOA_3_P0_3 BEE_PSEL(DWGPIO, P0_3)
#define BEE_PSEL_GPIOA_4_P0_4 BEE_PSEL(DWGPIO, P0_4)
#define BEE_PSEL_GPIOA_5_P0_5 BEE_PSEL(DWGPIO, P0_5)
#define BEE_PSEL_GPIOA_6_P0_6 BEE_PSEL(DWGPIO, P0_6)
#define BEE_PSEL_GPIOA_7_P0_7 BEE_PSEL(DWGPIO, P0_7)

/* Port 1 */
/* Note: P1_0/P1_1 default to SWD function for rtl87x2g. */
#define BEE_PSEL_GPIOA_8_P1_0  BEE_PSEL(DWGPIO, P1_0)
#define BEE_PSEL_GPIOA_9_P1_1  BEE_PSEL(DWGPIO, P1_1)
#define BEE_PSEL_GPIOA_10_P1_2 BEE_PSEL(DWGPIO, P1_2)
#define BEE_PSEL_GPIOA_11_P1_3 BEE_PSEL(DWGPIO, P1_3)
#define BEE_PSEL_GPIOA_12_P1_4 BEE_PSEL(DWGPIO, P1_4)
#define BEE_PSEL_GPIOA_13_P1_5 BEE_PSEL(DWGPIO, P1_5)
#define BEE_PSEL_GPIOA_14_P1_6 BEE_PSEL(DWGPIO, P1_6)
#define BEE_PSEL_GPIOA_15_P1_7 BEE_PSEL(DWGPIO, P1_7)

/* Port 2 */
#define BEE_PSEL_GPIOA_21_P2_0 BEE_PSEL(DWGPIO, P2_0)
#define BEE_PSEL_GPIOA_22_P2_1 BEE_PSEL(DWGPIO, P2_1)
#define BEE_PSEL_GPIOA_23_P2_2 BEE_PSEL(DWGPIO, P2_2)
#define BEE_PSEL_GPIOA_24_P2_3 BEE_PSEL(DWGPIO, P2_3)
#define BEE_PSEL_GPIOA_25_P2_4 BEE_PSEL(DWGPIO, P2_4)
#define BEE_PSEL_GPIOA_26_P2_5 BEE_PSEL(DWGPIO, P2_5)
#define BEE_PSEL_GPIOA_27_P2_6 BEE_PSEL(DWGPIO, P2_6)
#define BEE_PSEL_GPIOA_28_P2_7 BEE_PSEL(DWGPIO, P2_7)

/* Port 3 */
#define BEE_PSEL_GPIOA_29_P3_0 BEE_PSEL(DWGPIO, P3_0)
#define BEE_PSEL_GPIOA_30_P3_1 BEE_PSEL(DWGPIO, P3_1)
#define BEE_PSEL_GPIOA_31_P3_2 BEE_PSEL(DWGPIO, P3_2)
#define BEE_PSEL_GPIOB_0_P3_3  BEE_PSEL(DWGPIO, P3_3)
#define BEE_PSEL_GPIOB_1_P3_4  BEE_PSEL(DWGPIO, P3_4)
#define BEE_PSEL_GPIOB_2_P3_5  BEE_PSEL(DWGPIO, P3_5)
#define BEE_PSEL_GPIOB_3_P3_6  BEE_PSEL(DWGPIO, P3_6)
#define BEE_PSEL_GPIOB_4_P3_7  BEE_PSEL(DWGPIO, P3_7)

/* Port 4 */
#define BEE_PSEL_GPIOB_5_P4_0  BEE_PSEL(DWGPIO, P4_0)
#define BEE_PSEL_GPIOB_6_P4_1  BEE_PSEL(DWGPIO, P4_1)
#define BEE_PSEL_GPIOB_7_P4_2  BEE_PSEL(DWGPIO, P4_2)
#define BEE_PSEL_GPIOB_8_P4_3  BEE_PSEL(DWGPIO, P4_3)
#define BEE_PSEL_GPIOB_9_P4_4  BEE_PSEL(DWGPIO, P4_4)
#define BEE_PSEL_GPIOB_10_P4_5 BEE_PSEL(DWGPIO, P4_5)
#define BEE_PSEL_GPIOB_11_P4_6 BEE_PSEL(DWGPIO, P4_6)
#define BEE_PSEL_GPIOB_12_P4_7 BEE_PSEL(DWGPIO, P4_7)

/* Port 5 */
#define BEE_PSEL_GPIOB_13_P5_0 BEE_PSEL(DWGPIO, P5_0)
#define BEE_PSEL_GPIOB_14_P5_1 BEE_PSEL(DWGPIO, P5_1)
#define BEE_PSEL_GPIOB_15_P5_2 BEE_PSEL(DWGPIO, P5_2)
#define BEE_PSEL_GPIOB_16_P5_3 BEE_PSEL(DWGPIO, P5_3)
#define BEE_PSEL_GPIOB_17_P5_4 BEE_PSEL(DWGPIO, P5_4)
#define BEE_PSEL_GPIOB_18_P5_5 BEE_PSEL(DWGPIO, P5_5)
#define BEE_PSEL_GPIOB_19_P5_6 BEE_PSEL(DWGPIO, P5_6)
#define BEE_PSEL_GPIOB_20_P5_7 BEE_PSEL(DWGPIO, P5_7)

/* Port 6 */
#define BEE_PSEL_GPIOB_19_P6_0 BEE_PSEL(DWGPIO, P6_0)
#define BEE_PSEL_GPIOB_20_P6_1 BEE_PSEL(DWGPIO, P6_1)
#define BEE_PSEL_GPIOB_21_P6_2 BEE_PSEL(DWGPIO, P6_2)
#define BEE_PSEL_GPIOB_22_P6_3 BEE_PSEL(DWGPIO, P6_3)
#define BEE_PSEL_GPIOB_23_P6_4 BEE_PSEL(DWGPIO, P6_4)
#define BEE_PSEL_GPIOB_24_P6_5 BEE_PSEL(DWGPIO, P6_5)
#define BEE_PSEL_GPIOB_25_P6_6 BEE_PSEL(DWGPIO, P6_6)
#define BEE_PSEL_GPIOB_26_P6_7 BEE_PSEL(DWGPIO, P6_7)

/* Port 7 */
#define BEE_PSEL_GPIOB_27_P7_0 BEE_PSEL(DWGPIO, P7_0)
#define BEE_PSEL_GPIOB_28_P7_1 BEE_PSEL(DWGPIO, P7_1)
#define BEE_PSEL_GPIOB_29_P7_2 BEE_PSEL(DWGPIO, P7_2)
#define BEE_PSEL_GPIOB_30_P7_3 BEE_PSEL(DWGPIO, P7_3)
#define BEE_PSEL_GPIOB_31_P7_4 BEE_PSEL(DWGPIO, P7_4)

/* Special Functions / Port 8 Equivalent */
/* Note: Using P8_x extracted from comments */
#define BEE_PSEL_GPIOA_16_P8_0 BEE_PSEL(DWGPIO, MICBIAS)
#define BEE_PSEL_GPIOA_17_P8_1 BEE_PSEL(DWGPIO, XI32K)
#define BEE_PSEL_GPIOA_18_P8_2 BEE_PSEL(DWGPIO, XO32K)
#define BEE_PSEL_GPIOA_19_P8_3 BEE_PSEL(DWGPIO, DACP)
#define BEE_PSEL_GPIOA_20_P8_4 BEE_PSEL(DWGPIO, DACN)

/* Port 9 */
#define BEE_PSEL_GPIOB_21_P9_0 BEE_PSEL(DWGPIO, P9_0)
#define BEE_PSEL_GPIOB_22_P9_1 BEE_PSEL(DWGPIO, P9_1)
#define BEE_PSEL_GPIOB_23_P9_2 BEE_PSEL(DWGPIO, P9_2)
#define BEE_PSEL_GPIOB_24_P9_3 BEE_PSEL(DWGPIO, P9_3)
#define BEE_PSEL_GPIOB_25_P9_4 BEE_PSEL(DWGPIO, P9_4)
#define BEE_PSEL_GPIOB_26_P9_5 BEE_PSEL(DWGPIO, P9_5)
#define BEE_PSEL_GPIOB_27_P9_6 BEE_PSEL(DWGPIO, P9_6)
#define BEE_PSEL_GPIOB_28_P9_7 BEE_PSEL(DWGPIO, P9_7)

/* Port 10 */
#define BEE_PSEL_GPIOB_29_P10_0 BEE_PSEL(DWGPIO, P10_0)
#define BEE_PSEL_GPIOB_30_P10_1 BEE_PSEL(DWGPIO, P10_1)
#define BEE_PSEL_GPIOB_31_P10_2 BEE_PSEL(DWGPIO, P10_2)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RTL87X2G_PINCTRL_H_ */
```

## 20.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026, Realtek Semiconductor Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 232 行

注意：对于 RTL87X2G，`P0_3` 默认用于输出 Realtek 内部日志（internal log）。

### 注释 3：原第 238 行

注意：对于 RTL87X2G，`P1_0/P1_1` 默认为串行线调试（SWD）功能。

### 注释 4：原第 322 行

端口 0（Port 0）。

### 注释 5：原第 326 行

注意：对于 RTL87X2G，`P0_3` 默认用于输出 Realtek 内部日志（internal log）。

### 注释 6：原第 333 行

端口 1（Port 1）。

### 注释 7：原第 334 行

注意：对于 RTL87X2G，`P1_0/P1_1` 默认为串行线调试（SWD）功能。

### 注释 8：原第 344 行

端口（Port）2。

### 注释 9：原第 354 行

端口（Port）3。

### 注释 10：原第 364 行

端口（Port）4。

### 注释 11：原第 374 行

端口（Port）5。

### 注释 12：原第 384 行

端口（Port）6。

### 注释 13：原第 394 行

端口（Port）7。

### 注释 14：原第 401 行

特殊功能（Special Functions）／端口 8 的等效功能。

### 注释 15：原第 402 行

注意：使用从注释中提取的 `P8_x`。

### 注释 16：原第 409 行

端口（Port）9。

### 注释 17：原第 419 行

端口（Port）10。

### 注释 18：原第 426 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RTL87X2G_PINCTRL_H_`。

## 20.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/rtl87x2g-pinctrl_8h.html)
- [bee-pinctrl.h](https://docs.zephyrproject.org/latest/doxygen/html/bee-pinctrl_8h.html)

---

[上一章](P019_pd.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P021_stm32-fmc-sdram.h_源码浏览.md)
