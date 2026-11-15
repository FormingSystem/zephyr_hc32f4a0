---
id: learning.zephyr-docs.api-source-architecture-reference.page-14
title: microchip-xec-gpio.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/microchip-xec-gpio_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_microchip-xec-gpio.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/microchip-xec-gpio_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_runtime_reference/P038_zephyr__dt-bindings__gpio__microchip-xec-gpio.h_文件参考.md)。

## 14.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
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
<a id="l00226"></a>
<a id="l00227"></a>

```c
/*
 * Copyright (c) 2022 Microchip Technology Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_MICROCHIP_XEC_GPIO_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_MICROCHIP_XEC_GPIO_H_


#define XEC_GPIO_HELPER(gpio_bank, gpio_bitpos) gpio_bank gpio_bitpos

/* bank A */
#define MCHP_GPIO_DECODE_000 XEC_GPIO_HELPER(&gpio_000_036, 0)
#define MCHP_GPIO_DECODE_001 XEC_GPIO_HELPER(&gpio_000_036, 1)
#define MCHP_GPIO_DECODE_002 XEC_GPIO_HELPER(&gpio_000_036, 2)
#define MCHP_GPIO_DECODE_003 XEC_GPIO_HELPER(&gpio_000_036, 3)
#define MCHP_GPIO_DECODE_004 XEC_GPIO_HELPER(&gpio_000_036, 4)
#define MCHP_GPIO_DECODE_005 XEC_GPIO_HELPER(&gpio_000_036, 5)
#define MCHP_GPIO_DECODE_006 XEC_GPIO_HELPER(&gpio_000_036, 6)
#define MCHP_GPIO_DECODE_007 XEC_GPIO_HELPER(&gpio_000_036, 7)
#define MCHP_GPIO_DECODE_010 XEC_GPIO_HELPER(&gpio_000_036, 8)
#define MCHP_GPIO_DECODE_011 XEC_GPIO_HELPER(&gpio_000_036, 9)
#define MCHP_GPIO_DECODE_012 XEC_GPIO_HELPER(&gpio_000_036, 10)
#define MCHP_GPIO_DECODE_013 XEC_GPIO_HELPER(&gpio_000_036, 11)
#define MCHP_GPIO_DECODE_014 XEC_GPIO_HELPER(&gpio_000_036, 12)
#define MCHP_GPIO_DECODE_015 XEC_GPIO_HELPER(&gpio_000_036, 13)
#define MCHP_GPIO_DECODE_016 XEC_GPIO_HELPER(&gpio_000_036, 14)
#define MCHP_GPIO_DECODE_017 XEC_GPIO_HELPER(&gpio_000_036, 15)
#define MCHP_GPIO_DECODE_020 XEC_GPIO_HELPER(&gpio_000_036, 16)
#define MCHP_GPIO_DECODE_021 XEC_GPIO_HELPER(&gpio_000_036, 17)
#define MCHP_GPIO_DECODE_022 XEC_GPIO_HELPER(&gpio_000_036, 18)
#define MCHP_GPIO_DECODE_023 XEC_GPIO_HELPER(&gpio_000_036, 19)
#define MCHP_GPIO_DECODE_024 XEC_GPIO_HELPER(&gpio_000_036, 20)
#define MCHP_GPIO_DECODE_025 XEC_GPIO_HELPER(&gpio_000_036, 21)
#define MCHP_GPIO_DECODE_026 XEC_GPIO_HELPER(&gpio_000_036, 22)
#define MCHP_GPIO_DECODE_027 XEC_GPIO_HELPER(&gpio_000_036, 23)
#define MCHP_GPIO_DECODE_030 XEC_GPIO_HELPER(&gpio_000_036, 24)
#define MCHP_GPIO_DECODE_031 XEC_GPIO_HELPER(&gpio_000_036, 25)
#define MCHP_GPIO_DECODE_032 XEC_GPIO_HELPER(&gpio_000_036, 26)
#define MCHP_GPIO_DECODE_033 XEC_GPIO_HELPER(&gpio_000_036, 27)
#define MCHP_GPIO_DECODE_034 XEC_GPIO_HELPER(&gpio_000_036, 28)
#define MCHP_GPIO_DECODE_035 XEC_GPIO_HELPER(&gpio_000_036, 29)
#define MCHP_GPIO_DECODE_036 XEC_GPIO_HELPER(&gpio_000_036, 30)

/* bank B */
#define MCHP_GPIO_DECODE_040 XEC_GPIO_HELPER(&gpio_040_076, 0)
#define MCHP_GPIO_DECODE_041 XEC_GPIO_HELPER(&gpio_040_076, 1)
#define MCHP_GPIO_DECODE_042 XEC_GPIO_HELPER(&gpio_040_076, 2)
#define MCHP_GPIO_DECODE_043 XEC_GPIO_HELPER(&gpio_040_076, 3)
#define MCHP_GPIO_DECODE_044 XEC_GPIO_HELPER(&gpio_040_076, 4)
#define MCHP_GPIO_DECODE_045 XEC_GPIO_HELPER(&gpio_040_076, 5)
#define MCHP_GPIO_DECODE_046 XEC_GPIO_HELPER(&gpio_040_076, 6)
#define MCHP_GPIO_DECODE_047 XEC_GPIO_HELPER(&gpio_040_076, 7)
#define MCHP_GPIO_DECODE_050 XEC_GPIO_HELPER(&gpio_040_076, 8)
#define MCHP_GPIO_DECODE_051 XEC_GPIO_HELPER(&gpio_040_076, 9)
#define MCHP_GPIO_DECODE_052 XEC_GPIO_HELPER(&gpio_040_076, 10)
#define MCHP_GPIO_DECODE_053 XEC_GPIO_HELPER(&gpio_040_076, 11)
#define MCHP_GPIO_DECODE_054 XEC_GPIO_HELPER(&gpio_040_076, 12)
#define MCHP_GPIO_DECODE_055 XEC_GPIO_HELPER(&gpio_040_076, 13)
#define MCHP_GPIO_DECODE_056 XEC_GPIO_HELPER(&gpio_040_076, 14)
#define MCHP_GPIO_DECODE_057 XEC_GPIO_HELPER(&gpio_040_076, 15)
#define MCHP_GPIO_DECODE_060 XEC_GPIO_HELPER(&gpio_040_076, 16)
#define MCHP_GPIO_DECODE_061 XEC_GPIO_HELPER(&gpio_040_076, 17)
#define MCHP_GPIO_DECODE_062 XEC_GPIO_HELPER(&gpio_040_076, 18)
#define MCHP_GPIO_DECODE_063 XEC_GPIO_HELPER(&gpio_040_076, 19)
#define MCHP_GPIO_DECODE_064 XEC_GPIO_HELPER(&gpio_040_076, 20)
#define MCHP_GPIO_DECODE_065 XEC_GPIO_HELPER(&gpio_040_076, 21)
#define MCHP_GPIO_DECODE_066 XEC_GPIO_HELPER(&gpio_040_076, 22)
#define MCHP_GPIO_DECODE_067 XEC_GPIO_HELPER(&gpio_040_076, 23)
#define MCHP_GPIO_DECODE_070 XEC_GPIO_HELPER(&gpio_040_076, 24)
#define MCHP_GPIO_DECODE_071 XEC_GPIO_HELPER(&gpio_040_076, 25)
#define MCHP_GPIO_DECODE_072 XEC_GPIO_HELPER(&gpio_040_076, 26)
#define MCHP_GPIO_DECODE_073 XEC_GPIO_HELPER(&gpio_040_076, 27)
#define MCHP_GPIO_DECODE_074 XEC_GPIO_HELPER(&gpio_040_076, 28)
#define MCHP_GPIO_DECODE_075 XEC_GPIO_HELPER(&gpio_040_076, 29)
#define MCHP_GPIO_DECODE_076 XEC_GPIO_HELPER(&gpio_040_076, 30)

/* bank C */
#define MCHP_GPIO_DECODE_100 XEC_GPIO_HELPER(&gpio_100_136, 0)
#define MCHP_GPIO_DECODE_101 XEC_GPIO_HELPER(&gpio_100_136, 1)
#define MCHP_GPIO_DECODE_102 XEC_GPIO_HELPER(&gpio_100_136, 2)
#define MCHP_GPIO_DECODE_103 XEC_GPIO_HELPER(&gpio_100_136, 3)
#define MCHP_GPIO_DECODE_104 XEC_GPIO_HELPER(&gpio_100_136, 4)
#define MCHP_GPIO_DECODE_105 XEC_GPIO_HELPER(&gpio_100_136, 5)
#define MCHP_GPIO_DECODE_106 XEC_GPIO_HELPER(&gpio_100_136, 6)
#define MCHP_GPIO_DECODE_107 XEC_GPIO_HELPER(&gpio_100_136, 7)
#define MCHP_GPIO_DECODE_110 XEC_GPIO_HELPER(&gpio_100_136, 8)
#define MCHP_GPIO_DECODE_111 XEC_GPIO_HELPER(&gpio_100_136, 9)
#define MCHP_GPIO_DECODE_112 XEC_GPIO_HELPER(&gpio_100_136, 10)
#define MCHP_GPIO_DECODE_113 XEC_GPIO_HELPER(&gpio_100_136, 11)
#define MCHP_GPIO_DECODE_114 XEC_GPIO_HELPER(&gpio_100_136, 12)
#define MCHP_GPIO_DECODE_115 XEC_GPIO_HELPER(&gpio_100_136, 13)
#define MCHP_GPIO_DECODE_116 XEC_GPIO_HELPER(&gpio_100_136, 14)
#define MCHP_GPIO_DECODE_117 XEC_GPIO_HELPER(&gpio_100_136, 15)
#define MCHP_GPIO_DECODE_120 XEC_GPIO_HELPER(&gpio_100_136, 16)
#define MCHP_GPIO_DECODE_121 XEC_GPIO_HELPER(&gpio_100_136, 17)
#define MCHP_GPIO_DECODE_122 XEC_GPIO_HELPER(&gpio_100_136, 18)
#define MCHP_GPIO_DECODE_123 XEC_GPIO_HELPER(&gpio_100_136, 19)
#define MCHP_GPIO_DECODE_124 XEC_GPIO_HELPER(&gpio_100_136, 20)
#define MCHP_GPIO_DECODE_125 XEC_GPIO_HELPER(&gpio_100_136, 21)
#define MCHP_GPIO_DECODE_126 XEC_GPIO_HELPER(&gpio_100_136, 22)
#define MCHP_GPIO_DECODE_127 XEC_GPIO_HELPER(&gpio_100_136, 23)
#define MCHP_GPIO_DECODE_130 XEC_GPIO_HELPER(&gpio_100_136, 24)
#define MCHP_GPIO_DECODE_131 XEC_GPIO_HELPER(&gpio_100_136, 25)
#define MCHP_GPIO_DECODE_132 XEC_GPIO_HELPER(&gpio_100_136, 26)
#define MCHP_GPIO_DECODE_133 XEC_GPIO_HELPER(&gpio_100_136, 27)
#define MCHP_GPIO_DECODE_134 XEC_GPIO_HELPER(&gpio_100_136, 28)
#define MCHP_GPIO_DECODE_135 XEC_GPIO_HELPER(&gpio_100_136, 29)
#define MCHP_GPIO_DECODE_136 XEC_GPIO_HELPER(&gpio_100_136, 30)

/* bank D */
#define MCHP_GPIO_DECODE_140 XEC_GPIO_HELPER(&gpio_140_176, 0)
#define MCHP_GPIO_DECODE_141 XEC_GPIO_HELPER(&gpio_140_176, 1)
#define MCHP_GPIO_DECODE_142 XEC_GPIO_HELPER(&gpio_140_176, 2)
#define MCHP_GPIO_DECODE_143 XEC_GPIO_HELPER(&gpio_140_176, 3)
#define MCHP_GPIO_DECODE_144 XEC_GPIO_HELPER(&gpio_140_176, 4)
#define MCHP_GPIO_DECODE_145 XEC_GPIO_HELPER(&gpio_140_176, 5)
#define MCHP_GPIO_DECODE_146 XEC_GPIO_HELPER(&gpio_140_176, 6)
#define MCHP_GPIO_DECODE_147 XEC_GPIO_HELPER(&gpio_140_176, 7)
#define MCHP_GPIO_DECODE_150 XEC_GPIO_HELPER(&gpio_140_176, 8)
#define MCHP_GPIO_DECODE_151 XEC_GPIO_HELPER(&gpio_140_176, 9)
#define MCHP_GPIO_DECODE_152 XEC_GPIO_HELPER(&gpio_140_176, 10)
#define MCHP_GPIO_DECODE_153 XEC_GPIO_HELPER(&gpio_140_176, 11)
#define MCHP_GPIO_DECODE_154 XEC_GPIO_HELPER(&gpio_140_176, 12)
#define MCHP_GPIO_DECODE_155 XEC_GPIO_HELPER(&gpio_140_176, 13)
#define MCHP_GPIO_DECODE_156 XEC_GPIO_HELPER(&gpio_140_176, 14)
#define MCHP_GPIO_DECODE_157 XEC_GPIO_HELPER(&gpio_140_176, 15)
#define MCHP_GPIO_DECODE_160 XEC_GPIO_HELPER(&gpio_140_176, 16)
#define MCHP_GPIO_DECODE_161 XEC_GPIO_HELPER(&gpio_140_176, 17)
#define MCHP_GPIO_DECODE_162 XEC_GPIO_HELPER(&gpio_140_176, 18)
#define MCHP_GPIO_DECODE_163 XEC_GPIO_HELPER(&gpio_140_176, 19)
#define MCHP_GPIO_DECODE_164 XEC_GPIO_HELPER(&gpio_140_176, 20)
#define MCHP_GPIO_DECODE_165 XEC_GPIO_HELPER(&gpio_140_176, 21)
#define MCHP_GPIO_DECODE_166 XEC_GPIO_HELPER(&gpio_140_176, 22)
#define MCHP_GPIO_DECODE_167 XEC_GPIO_HELPER(&gpio_140_176, 23)
#define MCHP_GPIO_DECODE_170 XEC_GPIO_HELPER(&gpio_140_176, 24)
#define MCHP_GPIO_DECODE_171 XEC_GPIO_HELPER(&gpio_140_176, 25)
#define MCHP_GPIO_DECODE_172 XEC_GPIO_HELPER(&gpio_140_176, 26)
#define MCHP_GPIO_DECODE_173 XEC_GPIO_HELPER(&gpio_140_176, 27)
#define MCHP_GPIO_DECODE_174 XEC_GPIO_HELPER(&gpio_140_176, 28)
#define MCHP_GPIO_DECODE_175 XEC_GPIO_HELPER(&gpio_140_176, 29)
#define MCHP_GPIO_DECODE_176 XEC_GPIO_HELPER(&gpio_140_176, 30)

/* bank E */
#define MCHP_GPIO_DECODE_200 XEC_GPIO_HELPER(&gpio_200_236, 0)
#define MCHP_GPIO_DECODE_201 XEC_GPIO_HELPER(&gpio_200_236, 1)
#define MCHP_GPIO_DECODE_202 XEC_GPIO_HELPER(&gpio_200_236, 2)
#define MCHP_GPIO_DECODE_203 XEC_GPIO_HELPER(&gpio_200_236, 3)
#define MCHP_GPIO_DECODE_204 XEC_GPIO_HELPER(&gpio_200_236, 4)
#define MCHP_GPIO_DECODE_205 XEC_GPIO_HELPER(&gpio_200_236, 5)
#define MCHP_GPIO_DECODE_206 XEC_GPIO_HELPER(&gpio_200_236, 6)
#define MCHP_GPIO_DECODE_207 XEC_GPIO_HELPER(&gpio_200_236, 7)
#define MCHP_GPIO_DECODE_210 XEC_GPIO_HELPER(&gpio_200_236, 8)
#define MCHP_GPIO_DECODE_211 XEC_GPIO_HELPER(&gpio_200_236, 9)
#define MCHP_GPIO_DECODE_212 XEC_GPIO_HELPER(&gpio_200_236, 10)
#define MCHP_GPIO_DECODE_213 XEC_GPIO_HELPER(&gpio_200_236, 11)
#define MCHP_GPIO_DECODE_214 XEC_GPIO_HELPER(&gpio_200_236, 12)
#define MCHP_GPIO_DECODE_215 XEC_GPIO_HELPER(&gpio_200_236, 13)
#define MCHP_GPIO_DECODE_216 XEC_GPIO_HELPER(&gpio_200_236, 14)
#define MCHP_GPIO_DECODE_217 XEC_GPIO_HELPER(&gpio_200_236, 15)
#define MCHP_GPIO_DECODE_220 XEC_GPIO_HELPER(&gpio_200_236, 16)
#define MCHP_GPIO_DECODE_221 XEC_GPIO_HELPER(&gpio_200_236, 17)
#define MCHP_GPIO_DECODE_222 XEC_GPIO_HELPER(&gpio_200_236, 18)
#define MCHP_GPIO_DECODE_223 XEC_GPIO_HELPER(&gpio_200_236, 19)
#define MCHP_GPIO_DECODE_224 XEC_GPIO_HELPER(&gpio_200_236, 20)
#define MCHP_GPIO_DECODE_225 XEC_GPIO_HELPER(&gpio_200_236, 21)
#define MCHP_GPIO_DECODE_226 XEC_GPIO_HELPER(&gpio_200_236, 22)
#define MCHP_GPIO_DECODE_227 XEC_GPIO_HELPER(&gpio_200_236, 23)
#define MCHP_GPIO_DECODE_230 XEC_GPIO_HELPER(&gpio_200_236, 24)
#define MCHP_GPIO_DECODE_231 XEC_GPIO_HELPER(&gpio_200_236, 25)
#define MCHP_GPIO_DECODE_232 XEC_GPIO_HELPER(&gpio_200_236, 26)
#define MCHP_GPIO_DECODE_233 XEC_GPIO_HELPER(&gpio_200_236, 27)
#define MCHP_GPIO_DECODE_234 XEC_GPIO_HELPER(&gpio_200_236, 28)
#define MCHP_GPIO_DECODE_235 XEC_GPIO_HELPER(&gpio_200_236, 29)
#define MCHP_GPIO_DECODE_236 XEC_GPIO_HELPER(&gpio_200_236, 30)

/* bank F */
#define MCHP_GPIO_DECODE_240 XEC_GPIO_HELPER(&gpio_240_276, 0)
#define MCHP_GPIO_DECODE_241 XEC_GPIO_HELPER(&gpio_240_276, 1)
#define MCHP_GPIO_DECODE_242 XEC_GPIO_HELPER(&gpio_240_276, 2)
#define MCHP_GPIO_DECODE_243 XEC_GPIO_HELPER(&gpio_240_276, 3)
#define MCHP_GPIO_DECODE_244 XEC_GPIO_HELPER(&gpio_240_276, 4)
#define MCHP_GPIO_DECODE_245 XEC_GPIO_HELPER(&gpio_240_276, 5)
#define MCHP_GPIO_DECODE_246 XEC_GPIO_HELPER(&gpio_240_276, 6)
#define MCHP_GPIO_DECODE_247 XEC_GPIO_HELPER(&gpio_240_276, 7)
#define MCHP_GPIO_DECODE_250 XEC_GPIO_HELPER(&gpio_240_276, 8)
#define MCHP_GPIO_DECODE_251 XEC_GPIO_HELPER(&gpio_240_276, 9)
#define MCHP_GPIO_DECODE_252 XEC_GPIO_HELPER(&gpio_240_276, 10)
#define MCHP_GPIO_DECODE_253 XEC_GPIO_HELPER(&gpio_240_276, 11)
#define MCHP_GPIO_DECODE_254 XEC_GPIO_HELPER(&gpio_240_276, 12)
#define MCHP_GPIO_DECODE_255 XEC_GPIO_HELPER(&gpio_240_276, 13)
#define MCHP_GPIO_DECODE_256 XEC_GPIO_HELPER(&gpio_240_276, 14)
#define MCHP_GPIO_DECODE_257 XEC_GPIO_HELPER(&gpio_240_276, 15)
#define MCHP_GPIO_DECODE_260 XEC_GPIO_HELPER(&gpio_240_276, 16)
#define MCHP_GPIO_DECODE_261 XEC_GPIO_HELPER(&gpio_240_276, 17)
#define MCHP_GPIO_DECODE_262 XEC_GPIO_HELPER(&gpio_240_276, 18)
#define MCHP_GPIO_DECODE_263 XEC_GPIO_HELPER(&gpio_240_276, 19)
#define MCHP_GPIO_DECODE_264 XEC_GPIO_HELPER(&gpio_240_276, 20)
#define MCHP_GPIO_DECODE_265 XEC_GPIO_HELPER(&gpio_240_276, 21)
#define MCHP_GPIO_DECODE_266 XEC_GPIO_HELPER(&gpio_240_276, 22)
#define MCHP_GPIO_DECODE_267 XEC_GPIO_HELPER(&gpio_240_276, 23)
#define MCHP_GPIO_DECODE_270 XEC_GPIO_HELPER(&gpio_240_276, 24)
#define MCHP_GPIO_DECODE_271 XEC_GPIO_HELPER(&gpio_240_276, 25)
#define MCHP_GPIO_DECODE_272 XEC_GPIO_HELPER(&gpio_240_276, 26)
#define MCHP_GPIO_DECODE_273 XEC_GPIO_HELPER(&gpio_240_276, 27)
#define MCHP_GPIO_DECODE_274 XEC_GPIO_HELPER(&gpio_240_276, 28)
#define MCHP_GPIO_DECODE_275 XEC_GPIO_HELPER(&gpio_240_276, 29)
#define MCHP_GPIO_DECODE_276 XEC_GPIO_HELPER(&gpio_240_276, 30)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_MICROCHIP_XEC_GPIO_H_ */
```

## 14.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Microchip Technology Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 27 行

组 A（Bank A）。

### 注释 3：原第 60 行

组 B（Bank B）。

### 注释 4：原第 93 行

组 C（Bank C）。

### 注释 5：原第 126 行

组 D（Bank D）。

### 注释 6：原第 159 行

组 E（Bank E）。

### 注释 7：原第 192 行

组 F（Bank F）。

### 注释 8：原第 227 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_MICROCHIP_XEC_GPIO_H_`。

## 14.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_runtime_reference/P038_zephyr__dt-bindings__gpio__microchip-xec-gpio.h_文件参考.md)

---

[上一章](P013_kinetis_pcc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P015_nxp-freqme.h_源码浏览.md)
