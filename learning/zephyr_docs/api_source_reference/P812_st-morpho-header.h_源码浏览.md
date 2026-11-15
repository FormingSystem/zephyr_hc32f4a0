---
id: learning.zephyr-docs.api-source-reference.page-812
title: st-morpho-header.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/st-morpho-header_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第812章\_st-morpho-header.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/st-morpho-header_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/st-morpho-header_8h.html)。

## 812.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00021"></a>
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
<a id="l00172"></a>
<a id="l00173"></a>

```c
/*
 * Copyright (c) 2023 Teslabs Engineering S.L.
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_ST_MORPHO_HEADER_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_ST_MORPHO_HEADER_H_


#define ST_MORPHO_PIN_MASK 0xFF

#define ST_MORPHO_L_1  0
#define ST_MORPHO_L_2  1
#define ST_MORPHO_L_3  2
#define ST_MORPHO_L_4  3
#define ST_MORPHO_L_5  4
#define ST_MORPHO_L_6  5
#define ST_MORPHO_L_7  6
#define ST_MORPHO_L_8  7
#define ST_MORPHO_L_9  8
#define ST_MORPHO_L_10 9
#define ST_MORPHO_L_11 10
#define ST_MORPHO_L_12 11
#define ST_MORPHO_L_13 12
#define ST_MORPHO_L_14 13
#define ST_MORPHO_L_15 14
#define ST_MORPHO_L_16 15
#define ST_MORPHO_L_17 16
#define ST_MORPHO_L_18 17
#define ST_MORPHO_L_19 18
#define ST_MORPHO_L_20 19
#define ST_MORPHO_L_21 20
#define ST_MORPHO_L_22 21
#define ST_MORPHO_L_23 22
#define ST_MORPHO_L_24 23
#define ST_MORPHO_L_25 24
#define ST_MORPHO_L_26 25
#define ST_MORPHO_L_27 26
#define ST_MORPHO_L_28 27
#define ST_MORPHO_L_29 28
#define ST_MORPHO_L_30 29
#define ST_MORPHO_L_31 30
#define ST_MORPHO_L_32 31
#define ST_MORPHO_L_33 32
#define ST_MORPHO_L_34 33
#define ST_MORPHO_L_35 34
#define ST_MORPHO_L_36 35
#define ST_MORPHO_L_37 36
#define ST_MORPHO_L_38 37
#define ST_MORPHO_L_39 38
#define ST_MORPHO_L_40 39
#define ST_MORPHO_L_41 40
#define ST_MORPHO_L_42 41
#define ST_MORPHO_L_43 42
#define ST_MORPHO_L_44 43
#define ST_MORPHO_L_45 44
#define ST_MORPHO_L_46 45
#define ST_MORPHO_L_47 46
#define ST_MORPHO_L_48 47
#define ST_MORPHO_L_49 48
#define ST_MORPHO_L_50 49
#define ST_MORPHO_L_51 50
#define ST_MORPHO_L_52 51
#define ST_MORPHO_L_53 52
#define ST_MORPHO_L_54 53
#define ST_MORPHO_L_55 54
#define ST_MORPHO_L_56 55
#define ST_MORPHO_L_57 56
#define ST_MORPHO_L_58 57
#define ST_MORPHO_L_59 58
#define ST_MORPHO_L_60 59
#define ST_MORPHO_L_61 60
#define ST_MORPHO_L_62 61
#define ST_MORPHO_L_63 62
#define ST_MORPHO_L_64 63
#define ST_MORPHO_L_65 64
#define ST_MORPHO_L_66 65
#define ST_MORPHO_L_67 66
#define ST_MORPHO_L_68 67
#define ST_MORPHO_L_69 68
#define ST_MORPHO_L_70 69
#define ST_MORPHO_L_71 70
#define ST_MORPHO_L_72 71

#define ST_MORPHO_R_1  72
#define ST_MORPHO_R_2  73
#define ST_MORPHO_R_3  74
#define ST_MORPHO_R_4  75
#define ST_MORPHO_R_5  76
#define ST_MORPHO_R_6  77
#define ST_MORPHO_R_7  78
#define ST_MORPHO_R_8  79
#define ST_MORPHO_R_9  80
#define ST_MORPHO_R_10 81
#define ST_MORPHO_R_11 82
#define ST_MORPHO_R_12 83
#define ST_MORPHO_R_13 84
#define ST_MORPHO_R_14 85
#define ST_MORPHO_R_15 86
#define ST_MORPHO_R_16 87
#define ST_MORPHO_R_17 88
#define ST_MORPHO_R_18 89
#define ST_MORPHO_R_19 90
#define ST_MORPHO_R_20 91
#define ST_MORPHO_R_21 92
#define ST_MORPHO_R_22 93
#define ST_MORPHO_R_23 94
#define ST_MORPHO_R_24 95
#define ST_MORPHO_R_25 96
#define ST_MORPHO_R_26 97
#define ST_MORPHO_R_27 98
#define ST_MORPHO_R_28 99
#define ST_MORPHO_R_29 100
#define ST_MORPHO_R_30 101
#define ST_MORPHO_R_31 102
#define ST_MORPHO_R_32 103
#define ST_MORPHO_R_33 104
#define ST_MORPHO_R_34 105
#define ST_MORPHO_R_35 106
#define ST_MORPHO_R_36 107
#define ST_MORPHO_R_37 108
#define ST_MORPHO_R_38 109
#define ST_MORPHO_R_39 110
#define ST_MORPHO_R_40 111
#define ST_MORPHO_R_41 112
#define ST_MORPHO_R_42 113
#define ST_MORPHO_R_43 114
#define ST_MORPHO_R_44 115
#define ST_MORPHO_R_45 116
#define ST_MORPHO_R_46 117
#define ST_MORPHO_R_47 118
#define ST_MORPHO_R_48 119
#define ST_MORPHO_R_49 120
#define ST_MORPHO_R_50 121
#define ST_MORPHO_R_51 122
#define ST_MORPHO_R_52 123
#define ST_MORPHO_R_53 124
#define ST_MORPHO_R_54 125
#define ST_MORPHO_R_55 126
#define ST_MORPHO_R_56 127
#define ST_MORPHO_R_57 128
#define ST_MORPHO_R_58 129
#define ST_MORPHO_R_59 130
#define ST_MORPHO_R_60 131
#define ST_MORPHO_R_61 132
#define ST_MORPHO_R_62 133
#define ST_MORPHO_R_63 134
#define ST_MORPHO_R_64 135
#define ST_MORPHO_R_65 136
#define ST_MORPHO_R_66 137
#define ST_MORPHO_R_67 138
#define ST_MORPHO_R_68 139
#define ST_MORPHO_R_69 140
#define ST_MORPHO_R_70 141
#define ST_MORPHO_R_71 142
#define ST_MORPHO_R_72 143


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_ST_MORPHO_HEADER_H_ */
```

## 812.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Teslabs Engineering S.L.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 173 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_ST_MORPHO_HEADER_H_`。

## 812.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/st-morpho-header_8h.html)

---

[上一章](P811_server.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P813_st87mxx_app_services.h_源码浏览.md)
