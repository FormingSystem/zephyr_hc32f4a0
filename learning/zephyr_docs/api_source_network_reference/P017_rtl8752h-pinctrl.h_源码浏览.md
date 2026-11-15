---
id: learning.zephyr-docs.api-source-network-reference.page-17
title: rtl8752h-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rtl8752h-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_rtl8752h-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/rtl8752h-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/rtl8752h-pinctrl_8h.html)。

## 17.1\_原始可见代码（Source Code）

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
<a id="l00142"></a>
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
<a id="l00245"></a>
<a id="l00246"></a>
<a id="abee-pinctrl_8h_html"></a>

```c
/*
 * Copyright (c) 2026, Realtek Semiconductor Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RTL8752H_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RTL8752H_PINCTRL_H_

#include "bee-pinctrl.h"

#define BEE_IDLE_MODE          0
#define BEE_UART2_TX           1
#define BEE_UART2_RX           2
#define BEE_UART2_CTS          3
#define BEE_UART2_RTS          4
#define BEE_I2C0_CLK           5
#define BEE_I2C0_DAT           6
#define BEE_I2C1_CLK           7
#define BEE_I2C1_DAT           8
#define BEE_PWM2_P             9
#define BEE_PWM2_N             10
#define BEE_ENPWM0_P           11
#define BEE_ENPWM0_N           12
#define BEE_TIM_PWM0           13
#define BEE_TIM_PWM1           14
#define BEE_TIM_PWM2           15
#define BEE_TIM_PWM3           16
#define BEE_TIM_PWM4           17
#define BEE_TIM_PWM5           18
#define BEE_ENPWM0             19
#define BEE_ENPWM1             20
#define BEE_QDEC_PHASE_A_X     21
#define BEE_QDEC_PHASE_B_X     22
#define BEE_QDEC_PHASE_A_Y     23
#define BEE_QDEC_PHASE_B_Y     24
#define BEE_QDEC_PHASE_A_Z     25
#define BEE_QDEC_PHASE_B_Z     26
#define BEE_UART0_TX           29
#define BEE_UART0_RX           30
#define BEE_UART0_CTS          31
#define BEE_UART0_RTS          32
#define BEE_IRDA_TX            33
#define BEE_IRDA_RX            34
#define BEE_UART1_TX           35
#define BEE_UART1_RX           36
#define BEE_UART1_CTS          37
#define BEE_UART1_RTS          38
#define BEE_SPI1_SS_N_0_MASTER 39
#define BEE_SPI1_SS_N_1_MASTER 40
#define BEE_SPI1_SS_N_2_MASTER 41
#define BEE_SPI1_CLK_MASTER    42
#define BEE_SPI1_MO_MASTER     43
#define BEE_SPI1_MI_MASTER     44
#define BEE_SPI0_SS_N_0_SLAVE  45
#define BEE_SPI0_CLK_SLAVE     46
#define BEE_SPI0_SO_SLAVE      47
#define BEE_SPI0_SI_SLAVE      48
#define BEE_SPI0_SS_N_0_MASTER 49
#define BEE_SPI0_CLK_MASTER    50
#define BEE_SPI0_MO_MASTER     51
#define BEE_SPI0_MI_MASTER     52
#define BEE_SPI2W_DATA         53
#define BEE_SPI2W_CLK          54
#define BEE_SPI2W_CS           55
#define BEE_SWD_CLK            56
#define BEE_SWD_DIO            57
#define BEE_KEY_COL_0          58
#define BEE_KEY_COL_1          59
#define BEE_KEY_COL_2          60
#define BEE_KEY_COL_3          61
#define BEE_KEY_COL_4          62
#define BEE_KEY_COL_5          63
#define BEE_KEY_COL_6          64
#define BEE_KEY_COL_7          65
#define BEE_KEY_COL_8          66
#define BEE_KEY_COL_9          67
#define BEE_KEY_COL_10         68
#define BEE_KEY_COL_11         69
#define BEE_KEY_COL_12         70
#define BEE_KEY_COL_13         71
#define BEE_KEY_COL_14         72
#define BEE_KEY_COL_15         73
#define BEE_KEY_COL_16         74
#define BEE_KEY_COL_17         75
#define BEE_KEY_COL_18         76
#define BEE_KEY_COL_19         77
#define BEE_KEY_ROW_0          78
#define BEE_KEY_ROW_1          79
#define BEE_KEY_ROW_2          80
#define BEE_KEY_ROW_3          81
#define BEE_KEY_ROW_4          82
#define BEE_KEY_ROW_5          83
#define BEE_KEY_ROW_6          84
#define BEE_KEY_ROW_7          85
#define BEE_KEY_ROW_8          86
#define BEE_KEY_ROW_9          87
#define BEE_KEY_ROW_10         88
#define BEE_KEY_ROW_11         89
#define BEE_DWGPIO             90
#define BEE_DMIC1_CLK          96
#define BEE_DMIC1_DAT          97
#define BEE_LRC_I_CODEC_SLAVE  98
#define BEE_BCLK_I_CODEC_SLAVE 99
#define BEE_SDI_CODEC_SLAVE    100
#define BEE_SDO_CODEC_SLAVE    101
#define BEE_BT_COEX_I_0        106
#define BEE_BT_COEX_I_1        107
#define BEE_BT_COEX_I_2        108
#define BEE_BT_COEX_I_3        109
#define BEE_BT_COEX_O_0        110
#define BEE_BT_COEX_O_1        111
#define BEE_BT_COEX_O_2        112
#define BEE_BT_COEX_O_3        113
#define BEE_PTA_I2C_CLK_SLAVE  114
#define BEE_PTA_I2C_DAT_SLAVE  115
#define BEE_PTA_I2C_INT_OUT    116
#define BEE_EN_EXPA            117
#define BEE_EN_EXLNA           118
#define BEE_LRC_SPORT0         123
#define BEE_BCLK_SPORT0        124
#define BEE_ADCDAT_SPORT0      125
#define BEE_DACDAT_SPORT0      126
#define BEE_MCLK               127
#define BEE_PINMUX_MAX         (BEE_MCLK + 1)
#define BEE_SW_MODE            (BEE_PINMUX_MAX + 1)
#define BEE_PWR_OFF            (BEE_PINMUX_MAX + 2)
#define BEE_PIN_DISCONNECTED   BEE_PIN_MSK

#define P0_0 0
#define P0_1 1
#define P0_2 2
/* Note: P0_3 defaults to outputting the Realtek internal log for rtl8752h. */
#define P0_3 3
#define P0_4 4
#define P0_5 5
#define P0_6 6
#define P0_7 7
/* Note: P1_0/P1_1 default to SWD function for rtl8752h. */
#define P1_0 8
#define P1_1 9
#define P1_3 11
#define P1_4 12
#define P1_6 14
#define P1_7 15
#define P2_0 16
#define P2_1 17
#define P2_2 18
#define P2_3 19
#define P2_4 20
#define P2_5 21
#define P2_6 22
#define P2_7 23
#define P3_0 24
#define P3_1 25
#define P3_2 26
#define P3_3 27
#define P3_4 28
#define P3_5 29
#define P3_6 30
#define P4_0 32
#define P4_1 33
#define P4_2 34
#define P4_3 35
#define H_0  36
#define P5_1 37
#define P5_2 38


/* Port 0 */
#define BEE_PSEL_GPIOA_0_P0_0 BEE_PSEL(DWGPIO, P0_0)
#define BEE_PSEL_GPIOA_1_P0_1 BEE_PSEL(DWGPIO, P0_1)
#define BEE_PSEL_GPIOA_2_P0_2 BEE_PSEL(DWGPIO, P0_2)
/* Note: P0_3 defaults to outputting the Realtek internal log for rtl8752h. */
#define BEE_PSEL_GPIOA_3_P0_3 BEE_PSEL(DWGPIO, P0_3)
#define BEE_PSEL_GPIOA_4_P0_4 BEE_PSEL(DWGPIO, P0_4)
#define BEE_PSEL_GPIOA_5_P0_5 BEE_PSEL(DWGPIO, P0_5)
#define BEE_PSEL_GPIOA_6_P0_6 BEE_PSEL(DWGPIO, P0_6)
#define BEE_PSEL_GPIOA_7_P0_7 BEE_PSEL(DWGPIO, P0_7)

/* Port 1 */
/* Note: P1_0/P1_1 default to SWD function for rtl8752h. */
#define BEE_PSEL_GPIOA_8_P1_0  BEE_PSEL(DWGPIO, P1_0)
#define BEE_PSEL_GPIOA_9_P1_1  BEE_PSEL(DWGPIO, P1_1)
#define BEE_PSEL_GPIOA_11_P1_3 BEE_PSEL(DWGPIO, P1_3)
#define BEE_PSEL_GPIOA_12_P1_4 BEE_PSEL(DWGPIO, P1_4)
#define BEE_PSEL_GPIOA_14_P1_6 BEE_PSEL(DWGPIO, P1_6)
#define BEE_PSEL_GPIOA_15_P1_7 BEE_PSEL(DWGPIO, P1_7)

/* Port 2 */
#define BEE_PSEL_GPIOA_16_P2_0 BEE_PSEL(DWGPIO, P2_0)
#define BEE_PSEL_GPIOA_17_P2_1 BEE_PSEL(DWGPIO, P2_1)
#define BEE_PSEL_GPIOA_18_P2_2 BEE_PSEL(DWGPIO, P2_2)
#define BEE_PSEL_GPIOA_19_P2_3 BEE_PSEL(DWGPIO, P2_3)
#define BEE_PSEL_GPIOA_20_P2_4 BEE_PSEL(DWGPIO, P2_4)
#define BEE_PSEL_GPIOA_21_P2_5 BEE_PSEL(DWGPIO, P2_5)
#define BEE_PSEL_GPIOA_22_P2_6 BEE_PSEL(DWGPIO, P2_6)
#define BEE_PSEL_GPIOA_23_P2_7 BEE_PSEL(DWGPIO, P2_7)

/* Port 3 */
#define BEE_PSEL_GPIOA_24_P3_0 BEE_PSEL(DWGPIO, P3_0)
#define BEE_PSEL_GPIOA_25_P3_1 BEE_PSEL(DWGPIO, P3_1)
#define BEE_PSEL_GPIOA_26_P3_2 BEE_PSEL(DWGPIO, P3_2)
#define BEE_PSEL_GPIOA_27_P3_3 BEE_PSEL(DWGPIO, P3_3)
#define BEE_PSEL_GPIOA_28_P3_4 BEE_PSEL(DWGPIO, P3_4)
#define BEE_PSEL_GPIOA_29_P3_5 BEE_PSEL(DWGPIO, P3_5)
#define BEE_PSEL_GPIOA_30_P3_6 BEE_PSEL(DWGPIO, P3_6)

/* Port 4 */
#define BEE_PSEL_GPIOA_13_P4_0 BEE_PSEL(DWGPIO, P4_0)
#define BEE_PSEL_GPIOA_29_P4_1 BEE_PSEL(DWGPIO, P4_1)
#define BEE_PSEL_GPIOA_30_P4_2 BEE_PSEL(DWGPIO, P4_2)
#define BEE_PSEL_GPIOA_31_P4_3 BEE_PSEL(DWGPIO, P4_3)

/* Port 5 */
#define BEE_PSEL_GPIOA_11_P5_1 BEE_PSEL(DWGPIO, P5_1)
#define BEE_PSEL_GPIOA_12_P5_2 BEE_PSEL(DWGPIO, P5_2)

/* Other Ports (H) */
#define BEE_PSEL_GPIOA_10_H_0 BEE_PSEL(DWGPIO, H_0)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RTL8752H_PINCTRL_H_ */
```

## 17.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026, Realtek Semiconductor Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 150 行

注意：对于 RTL8752H，`P0_3` 默认用于输出 Realtek 内部日志（internal log）。

### 注释 3：原第 156 行

注意：对于 RTL8752H，`P1_0/P1_1` 默认为串行线调试（Serial Wire Debug，SWD）功能。

### 注释 4：原第 192 行

端口 0（Port 0）。

### 注释 5：原第 196 行

注意：对于 RTL8752H，`P0_3` 默认用于输出 Realtek 内部日志（internal log）。

### 注释 6：原第 203 行

端口 1（Port 1）。

### 注释 7：原第 204 行

注意：对于 RTL8752H，`P1_0/P1_1` 默认为串行线调试（Serial Wire Debug，SWD）功能。

### 注释 8：原第 212 行

端口（Port）2。

### 注释 9：原第 222 行

端口（Port）3。

### 注释 10：原第 231 行

端口（Port）4。

### 注释 11：原第 237 行

端口（Port）5。

### 注释 12：原第 241 行

其他端口（Other Ports，H）。

### 注释 13：原第 246 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RTL8752H_PINCTRL_H_`。

## 17.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/rtl8752h-pinctrl_8h.html)
- [bee-pinctrl.h](https://docs.zephyrproject.org/latest/doxygen/html/bee-pinctrl_8h.html)

---

[上一章](P016_pinctrl-rza2m.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P018_rts5912_clock.h_源码浏览.md)
