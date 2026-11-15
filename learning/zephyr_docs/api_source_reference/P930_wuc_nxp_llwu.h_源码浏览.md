---
id: learning.zephyr-docs.api-source-reference.page-930
title: wuc_nxp_llwu.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/wuc__nxp__llwu_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第930章\_wuc\_nxp\_llwu.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/wuc__nxp__llwu_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/wuc__nxp__llwu_8h.html)。

## 930.1\_原始可见代码（Source Code）

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
<a id="l00028"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="foldopen00053"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="foldopen00061"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00174"></a>
<a id="l00176"></a>
<a id="l00178"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00186"></a>
<a id="l00188"></a>
<a id="l00190"></a>
<a id="l00192"></a>
<a id="l00194"></a>
<a id="l00196"></a>
<a id="l00198"></a>
<a id="l00202"></a>
<a id="l00204"></a>
<a id="l00206"></a>
<a id="l00208"></a>
<a id="l00210"></a>
<a id="l00212"></a>
<a id="l00213"></a>

```c
/*
 * Copyright 2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_WUC_WUC_NXP_LLWU_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_WUC_WUC_NXP_LLWU_H_


#define NXP_LLWU_WAKEUP_SOURCE_TYPE_PIN    (0U << 31)
#define NXP_LLWU_WAKEUP_SOURCE_TYPE_MODULE (1U << 31)

#define NXP_LLWU_PIN_EDGE_RISING  1
#define NXP_LLWU_PIN_EDGE_FALLING 2
#define NXP_LLWU_PIN_EDGE_ANY     3

#define NXP_LLWU_PIN_WAKEUP(pin_index, edge_type)                                                  \
        (NXP_LLWU_WAKEUP_SOURCE_TYPE_PIN | (((edge_type) & 0x3) << 8) | ((pin_index) & 0xFF))

#define NXP_LLWU_MODULE_WAKEUP(module_index)                                                       \
        (NXP_LLWU_WAKEUP_SOURCE_TYPE_MODULE | ((module_index) & 0xFF))

#define NXP_LLWU_PIN_0_RISING  NXP_LLWU_PIN_WAKEUP(1, NXP_LLWU_PIN_EDGE_RISING)
#define NXP_LLWU_PIN_0_FALLING NXP_LLWU_PIN_WAKEUP(1, NXP_LLWU_PIN_EDGE_FALLING)
#define NXP_LLWU_PIN_0_ANY     NXP_LLWU_PIN_WAKEUP(1, NXP_LLWU_PIN_EDGE_ANY)

#define NXP_LLWU_PIN_1_RISING  NXP_LLWU_PIN_WAKEUP(2, NXP_LLWU_PIN_EDGE_RISING)
#define NXP_LLWU_PIN_1_FALLING NXP_LLWU_PIN_WAKEUP(2, NXP_LLWU_PIN_EDGE_FALLING)
#define NXP_LLWU_PIN_1_ANY     NXP_LLWU_PIN_WAKEUP(2, NXP_LLWU_PIN_EDGE_ANY)

#define NXP_LLWU_PIN_2_RISING  NXP_LLWU_PIN_WAKEUP(3, NXP_LLWU_PIN_EDGE_RISING)
#define NXP_LLWU_PIN_2_FALLING NXP_LLWU_PIN_WAKEUP(3, NXP_LLWU_PIN_EDGE_FALLING)
#define NXP_LLWU_PIN_2_ANY     NXP_LLWU_PIN_WAKEUP(3, NXP_LLWU_PIN_EDGE_ANY)

#define NXP_LLWU_PIN_3_RISING  NXP_LLWU_PIN_WAKEUP(4, NXP_LLWU_PIN_EDGE_RISING)
#define NXP_LLWU_PIN_3_FALLING NXP_LLWU_PIN_WAKEUP(4, NXP_LLWU_PIN_EDGE_FALLING)
#define NXP_LLWU_PIN_3_ANY     NXP_LLWU_PIN_WAKEUP(4, NXP_LLWU_PIN_EDGE_ANY)

#define NXP_LLWU_PIN_4_RISING  NXP_LLWU_PIN_WAKEUP(5, NXP_LLWU_PIN_EDGE_RISING)
#define NXP_LLWU_PIN_4_FALLING NXP_LLWU_PIN_WAKEUP(5, NXP_LLWU_PIN_EDGE_FALLING)
#define NXP_LLWU_PIN_4_ANY     NXP_LLWU_PIN_WAKEUP(5, NXP_LLWU_PIN_EDGE_ANY)

#define NXP_LLWU_PIN_5_RISING  NXP_LLWU_PIN_WAKEUP(6, NXP_LLWU_PIN_EDGE_RISING)
#define NXP_LLWU_PIN_5_FALLING NXP_LLWU_PIN_WAKEUP(6, NXP_LLWU_PIN_EDGE_FALLING)
#define NXP_LLWU_PIN_5_ANY     NXP_LLWU_PIN_WAKEUP(6, NXP_LLWU_PIN_EDGE_ANY)

#define NXP_LLWU_PIN_6_RISING  NXP_LLWU_PIN_WAKEUP(7, NXP_LLWU_PIN_EDGE_RISING)
#define NXP_LLWU_PIN_6_FALLING NXP_LLWU_PIN_WAKEUP(7, NXP_LLWU_PIN_EDGE_FALLING)
#define NXP_LLWU_PIN_6_ANY     NXP_LLWU_PIN_WAKEUP(7, NXP_LLWU_PIN_EDGE_ANY)

#define NXP_LLWU_PIN_7_RISING  NXP_LLWU_PIN_WAKEUP(8, NXP_LLWU_PIN_EDGE_RISING)
#define NXP_LLWU_PIN_7_FALLING NXP_LLWU_PIN_WAKEUP(8, NXP_LLWU_PIN_EDGE_FALLING)
#define NXP_LLWU_PIN_7_ANY     NXP_LLWU_PIN_WAKEUP(8, NXP_LLWU_PIN_EDGE_ANY)

#define NXP_LLWU_PIN_8_RISING  NXP_LLWU_PIN_WAKEUP(9, NXP_LLWU_PIN_EDGE_RISING)
#define NXP_LLWU_PIN_8_FALLING NXP_LLWU_PIN_WAKEUP(9, NXP_LLWU_PIN_EDGE_FALLING)
#define NXP_LLWU_PIN_8_ANY     NXP_LLWU_PIN_WAKEUP(9, NXP_LLWU_PIN_EDGE_ANY)

#define NXP_LLWU_PIN_9_RISING  NXP_LLWU_PIN_WAKEUP(10, NXP_LLWU_PIN_EDGE_RISING)
#define NXP_LLWU_PIN_9_FALLING NXP_LLWU_PIN_WAKEUP(10, NXP_LLWU_PIN_EDGE_FALLING)
#define NXP_LLWU_PIN_9_ANY     NXP_LLWU_PIN_WAKEUP(10, NXP_LLWU_PIN_EDGE_ANY)

#define NXP_LLWU_PIN_10_RISING  NXP_LLWU_PIN_WAKEUP(11, NXP_LLWU_PIN_EDGE_RISING)
#define NXP_LLWU_PIN_10_FALLING NXP_LLWU_PIN_WAKEUP(11, NXP_LLWU_PIN_EDGE_FALLING)
#define NXP_LLWU_PIN_10_ANY     NXP_LLWU_PIN_WAKEUP(11, NXP_LLWU_PIN_EDGE_ANY)

#define NXP_LLWU_PIN_11_RISING  NXP_LLWU_PIN_WAKEUP(12, NXP_LLWU_PIN_EDGE_RISING)
#define NXP_LLWU_PIN_11_FALLING NXP_LLWU_PIN_WAKEUP(12, NXP_LLWU_PIN_EDGE_FALLING)
#define NXP_LLWU_PIN_11_ANY     NXP_LLWU_PIN_WAKEUP(12, NXP_LLWU_PIN_EDGE_ANY)

#define NXP_LLWU_PIN_12_RISING  NXP_LLWU_PIN_WAKEUP(13, NXP_LLWU_PIN_EDGE_RISING)
#define NXP_LLWU_PIN_12_FALLING NXP_LLWU_PIN_WAKEUP(13, NXP_LLWU_PIN_EDGE_FALLING)
#define NXP_LLWU_PIN_12_ANY     NXP_LLWU_PIN_WAKEUP(13, NXP_LLWU_PIN_EDGE_ANY)

#define NXP_LLWU_PIN_13_RISING  NXP_LLWU_PIN_WAKEUP(14, NXP_LLWU_PIN_EDGE_RISING)
#define NXP_LLWU_PIN_13_FALLING NXP_LLWU_PIN_WAKEUP(14, NXP_LLWU_PIN_EDGE_FALLING)
#define NXP_LLWU_PIN_13_ANY     NXP_LLWU_PIN_WAKEUP(14, NXP_LLWU_PIN_EDGE_ANY)

#define NXP_LLWU_PIN_14_RISING  NXP_LLWU_PIN_WAKEUP(15, NXP_LLWU_PIN_EDGE_RISING)
#define NXP_LLWU_PIN_14_FALLING NXP_LLWU_PIN_WAKEUP(15, NXP_LLWU_PIN_EDGE_FALLING)
#define NXP_LLWU_PIN_14_ANY     NXP_LLWU_PIN_WAKEUP(15, NXP_LLWU_PIN_EDGE_ANY)

#define NXP_LLWU_PIN_15_RISING  NXP_LLWU_PIN_WAKEUP(16, NXP_LLWU_PIN_EDGE_RISING)
#define NXP_LLWU_PIN_15_FALLING NXP_LLWU_PIN_WAKEUP(16, NXP_LLWU_PIN_EDGE_FALLING)
#define NXP_LLWU_PIN_15_ANY     NXP_LLWU_PIN_WAKEUP(16, NXP_LLWU_PIN_EDGE_ANY)

#define NXP_LLWU_MODULE_0 NXP_LLWU_MODULE_WAKEUP(1)
#define NXP_LLWU_MODULE_1 NXP_LLWU_MODULE_WAKEUP(2)
#define NXP_LLWU_MODULE_2 NXP_LLWU_MODULE_WAKEUP(3)
#define NXP_LLWU_MODULE_3 NXP_LLWU_MODULE_WAKEUP(4)
#define NXP_LLWU_MODULE_4 NXP_LLWU_MODULE_WAKEUP(5)
#define NXP_LLWU_MODULE_5 NXP_LLWU_MODULE_WAKEUP(6)
#define NXP_LLWU_MODULE_6 NXP_LLWU_MODULE_WAKEUP(7)
#define NXP_LLWU_MODULE_7 NXP_LLWU_MODULE_WAKEUP(8)

#define NXP_LLWU_IS_PIN_SOURCE(source)    (((source) & (1U << 31)) == 0)
#define NXP_LLWU_IS_MODULE_SOURCE(source) (((source) & (1U << 31)) != 0)
#define NXP_LLWU_GET_PIN_INDEX(source)    ((source) & 0xFF)
#define NXP_LLWU_GET_PIN_EDGE(source)     (((source) >> 8) & 0x3)
#define NXP_LLWU_GET_MODULE_INDEX(source) ((source) & 0xFF)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_WUC_WUC_NXP_LLWU_H_ */
```

## 930.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 213 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_WUC_WUC_NXP_LLWU_H_`。

## 930.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/wuc__nxp__llwu_8h.html)

---

[上一章](P929_wuc_ite_it8xxx2.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P931_xbr818.h_源码浏览.md)
