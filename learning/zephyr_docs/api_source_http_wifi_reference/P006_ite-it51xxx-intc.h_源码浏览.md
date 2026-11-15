---
id: learning.zephyr-docs.api-source-http-wifi-reference.page-6
title: ite-it51xxx-intc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ite-it51xxx-intc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_ite-it51xxx-intc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ite-it51xxx-intc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_interface_reference/P029_zephyr__dt-bindings__interrupt-controller__ite-it51xxx-intc.h_文件参考.md)。

## 6.1\_原始可见代码（Source Code）

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
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00048"></a>
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
<a id="l00097"></a>
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
<a id="l00236"></a>
<a id="l00238"></a>
<a id="l00239"></a>

```c
/*
 * Copyright (c) 2025 ITE Corporation. All Rights Reserved.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_ITE_IT51XXX_INTC_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_ITE_IT51XXX_INTC_H_


#define IRQ_TYPE_NONE         0
#define IRQ_TYPE_EDGE_RISING  1
#define IRQ_TYPE_EDGE_FALLING 2
#define IRQ_TYPE_EDGE_BOTH    (IRQ_TYPE_EDGE_FALLING | IRQ_TYPE_EDGE_RISING)
#define IRQ_TYPE_LEVEL_HIGH   4
#define IRQ_TYPE_LEVEL_LOW    8


/* IRQ numbers of WUC */
/* Group 0 of INTC */
#define IT51XXX_IRQ_WU20       1
#define IT51XXX_IRQ_KBC_OBE    2
#define IT51XXX_IRQ_SMB_D      4
#define IT51XXX_IRQ_WKINTD     5
#define IT51XXX_IRQ_WU23       6
/* Group 1 */
#define IT51XXX_IRQ_SMB_A      9
#define IT51XXX_IRQ_SMB_B      10
#define IT51XXX_IRQ_WU26       12
#define IT51XXX_IRQ_WKINTC     13
#define IT51XXX_IRQ_WU25       14
/* Group 2 */
#define IT51XXX_IRQ_SMB_C      16
#define IT51XXX_IRQ_WU24       17
#define IT51XXX_IRQ_PS2_0      20
#define IT51XXX_IRQ_WU22       21
/* Group 3 */
#define IT51XXX_IRQ_KBC_IBF    24
#define IT51XXX_IRQ_PMC1_IBF   25
#define IT51XXX_IRQ_PMC2_IBF   27
#define IT51XXX_IRQ_TIMER1     30
#define IT51XXX_IRQ_WU21       31
/* Group 4 */
#define IT51XXX_IRQ_SPI        37
/* Group 5 */
#define IT51XXX_IRQ_WU50       40
#define IT51XXX_IRQ_WU51       41
#define IT51XXX_IRQ_WU52       42
#define IT51XXX_IRQ_WU53       43
#define IT51XXX_IRQ_WU54       44
#define IT51XXX_IRQ_WU55       45
#define IT51XXX_IRQ_WU56       46
#define IT51XXX_IRQ_WU57       47
/* Group 6 */
#define IT51XXX_IRQ_WU60       48
#define IT51XXX_IRQ_WU61       49
#define IT51XXX_IRQ_WU62       50
#define IT51XXX_IRQ_WU63       51
#define IT51XXX_IRQ_WU64       52
#define IT51XXX_IRQ_WU65       53
#define IT51XXX_IRQ_WU66       54
#define IT51XXX_IRQ_WU67       55
/* Group 7 */
#define IT51XXX_IRQ_RTCT_ALARM1 56
#define IT51XXX_IRQ_RTCT_ALARM2 57

#define IT51XXX_IRQ_TIMER2     58
/* Group 8 */
#define IT51XXX_IRQ_PMC3_IBF   67
#define IT51XXX_IRQ_PMC4_IBF   69
/* Group 9 */
#define IT51XXX_IRQ_WU70       72
#define IT51XXX_IRQ_WU71       73
#define IT51XXX_IRQ_WU72       74
#define IT51XXX_IRQ_WU73       75
#define IT51XXX_IRQ_WU74       76
#define IT51XXX_IRQ_WU75       77
#define IT51XXX_IRQ_WU76       78
#define IT51XXX_IRQ_WU77       79
/* Group 10 */
#define IT51XXX_IRQ_WU88       85
#define IT51XXX_IRQ_WU89       86
#define IT51XXX_IRQ_WU90       87
/* Group 11 */
#define IT51XXX_IRQ_WU80       88
#define IT51XXX_IRQ_WU81       89
#define IT51XXX_IRQ_WU82       90
#define IT51XXX_IRQ_WU83       91
#define IT51XXX_IRQ_WU84       92
#define IT51XXX_IRQ_WU85       93
#define IT51XXX_IRQ_WU86       94
#define IT51XXX_IRQ_WU87       95
/* Group 12 */
#define IT51XXX_IRQ_WU91       96
#define IT51XXX_IRQ_WU92       97
#define IT51XXX_IRQ_WU93       98
#define IT51XXX_IRQ_WU95       100
#define IT51XXX_IRQ_WU96       101
#define IT51XXX_IRQ_WU97       102
#define IT51XXX_IRQ_WU98       103
/* Group 13 */
#define IT51XXX_IRQ_WU99       104
#define IT51XXX_IRQ_WU100      105
#define IT51XXX_IRQ_WU101      106
#define IT51XXX_IRQ_WU102      107
#define IT51XXX_IRQ_WU103      108
#define IT51XXX_IRQ_WU104      109
#define IT51XXX_IRQ_WU105      110
#define IT51XXX_IRQ_WU106      111
/* Group 14 */
#define IT51XXX_IRQ_WU107      112
#define IT51XXX_IRQ_WU108      113
#define IT51XXX_IRQ_WU109      114
#define IT51XXX_IRQ_WU110      115
#define IT51XXX_IRQ_WU111      116
#define IT51XXX_IRQ_WU112      117
#define IT51XXX_IRQ_WU113      118
#define IT51XXX_IRQ_WU114      119
/* Group 15 */
#define IT51XXX_IRQ_WU115      120
#define IT51XXX_IRQ_WU116      121
#define IT51XXX_IRQ_WU117      122
#define IT51XXX_IRQ_WU118      123
#define IT51XXX_IRQ_WU119      124
#define IT51XXX_IRQ_WU120      125
#define IT51XXX_IRQ_WU121      126
#define IT51XXX_IRQ_WU122      127
/* Group 16 */
#define IT51XXX_IRQ_WU128      128
#define IT51XXX_IRQ_WU129      129
#define IT51XXX_IRQ_WU131      131
#define IT51XXX_IRQ_WU132      132
#define IT51XXX_IRQ_WU133      133
#define IT51XXX_IRQ_WU134      134
#define IT51XXX_IRQ_WU135      135
/* Group 17 */
#define IT51XXX_IRQ_WU136      136
#define IT51XXX_IRQ_WU137      137
#define IT51XXX_IRQ_WU138      138
#define IT51XXX_IRQ_WU139      139
#define IT51XXX_IRQ_WU140      140
#define IT51XXX_IRQ_WU141      141
#define IT51XXX_IRQ_WU142      142
/* Group 18 */
#define IT51XXX_IRQ_WU127      148
#define IT51XXX_IRQ_PMC5_IBF   150
#define IT51XXX_IRQ_V_CMP      151
/* Group 19 */
#define IT51XXX_IRQ_PECI       152
#define IT51XXX_IRQ_ESPI       153
#define IT51XXX_IRQ_ESPI_VW    154
#define IT51XXX_IRQ_PCH_P80    155
#define IT51XXX_IRQ_TIMER3     157
#define IT51XXX_IRQ_PLL_CHANGE 159
/* Group 20 */
#define IT51XXX_IRQ_SMB_E      160
#define IT51XXX_IRQ_SMB_F      161
#define IT51XXX_IRQ_CRYPTO     162
#define IT51XXX_IRQ_WU40       163
#define IT51XXX_IRQ_WU45       166
/* Group 21 */
#define IT51XXX_IRQ_WU46       168
#define IT51XXX_IRQ_WU144      170
#define IT51XXX_IRQ_WU145      171
#define IT51XXX_IRQ_WU146      172
#define IT51XXX_IRQ_WU147      173
#define IT51XXX_IRQ_TIMER4     175
/* Group 22 */
#define IT51XXX_IRQ_WU148      176
#define IT51XXX_IRQ_WU149      177
#define IT51XXX_IRQ_WU150      178
#define IT51XXX_IRQ_WU151      179
#define IT51XXX_IRQ_I3C_M0     180
#define IT51XXX_IRQ_I3C_M1     181
#define IT51XXX_IRQ_I3C_S0     182
#define IT51XXX_IRQ_I3C_S1     183
#define IT51XXX_IRQ_USB        184
/* Group 25 */
#define IT51XXX_IRQ_SMB_SC     203
#define IT51XXX_IRQ_SMB_SB     204
#define IT51XXX_IRQ_SMB_SA     205
#define IT51XXX_IRQ_TIMER1_DW  207
/* Group 26 */
#define IT51XXX_IRQ_TIMER2_DW  208
#define IT51XXX_IRQ_TIMER3_DW  209
#define IT51XXX_IRQ_TIMER4_DW  210
#define IT51XXX_IRQ_TIMER5_DW  211
#define IT51XXX_IRQ_TIMER6_DW  212
#define IT51XXX_IRQ_TIMER7_DW  213
#define IT51XXX_IRQ_TIMER8_DW  214
/* Group 27 */
#define IT51XXX_IRQ_PWM_TACH0  219
#define IT51XXX_IRQ_PWM_TACH1  220
#define IT51XXX_IRQ_PWM_TACH2  221
#define IT51XXX_IRQ_SMB_G      222
#define IT51XXX_IRQ_SMB_H      223
/* Group 28 */
#define IT51XXX_IRQ_SMB_I      224



#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_ITE_IT51XXX_INTC_H_ */
```

## 6.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 ITE Corporation. All Rights Reserved.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 51 行

唤醒控制器（WUC）的中断请求（IRQ）编号。

### 注释 3：原第 52 行

中断控制器（INTC）的组 0（Group 0）。

### 注释 4：原第 58 行

组 1（Group 1）。

### 注释 5：原第 64 行

组 2（Group 2）。

### 注释 6：原第 69 行

组 3（Group 3）。

### 注释 7：原第 75 行

组 4（Group 4）。

### 注释 8：原第 77 行

组 5（Group 5）。

### 注释 9：原第 86 行

组 6（Group 6）。

### 注释 10：原第 95 行

组 7（Group 7）。

### 注释 11：原第 102 行

组 8（Group 8）。

### 注释 12：原第 105 行

组 9（Group 9）。

### 注释 13：原第 114 行

组 10（Group 10）。

### 注释 14：原第 118 行

组 11（Group 11）。

### 注释 15：原第 127 行

组 12（Group 12）。

### 注释 16：原第 135 行

组 13（Group 13）。

### 注释 17：原第 144 行

组 14（Group 14）。

### 注释 18：原第 153 行

组 15（Group 15）。

### 注释 19：原第 162 行

组 16（Group 16）。

### 注释 20：原第 170 行

组 17（Group 17）。

### 注释 21：原第 178 行

组 18（Group 18）。

### 注释 22：原第 182 行

组 19（Group 19）。

### 注释 23：原第 189 行

组 20（Group 20）。

### 注释 24：原第 195 行

组 21（Group 21）。

### 注释 25：原第 202 行

组 22（Group 22）。

### 注释 26：原第 213 行

组 25（Group 25）。

### 注释 27：原第 218 行

组 26（Group 26）。

### 注释 28：原第 226 行

组 27（Group 27）。

### 注释 29：原第 232 行

组 28（Group 28）。

### 注释 30：原第 239 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_ITE_IT51XXX_INTC_H_`。

## 6.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_interface_reference/P029_zephyr__dt-bindings__interrupt-controller__ite-it51xxx-intc.h_文件参考.md)

---

[上一章](P005_inttypes.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P007_parser.h_源码浏览.md)
