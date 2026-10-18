---
id: learning.zephyr-docs.api-source-device-reference.page-35
title: st-zio-header.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/st-zio-header_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_st-zio-header.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/st-zio-header_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/st-zio-header_8h.html)。

## 35.1\_原始可见代码（Source Code）

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
<a id="l00134"></a>
<a id="l00135"></a>

```c
/*
 * Copyright (c) 2026 Michele Vaccari
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_ST_ZIO_HEADER_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_ST_ZIO_HEADER_H_


#define ST_ZIO_PIN_MASK 0xFF

/* CN7 connector (upper right) */
#define ST_ZIO_CN7_1  0
#define ST_ZIO_CN7_2  1
#define ST_ZIO_CN7_3  2
#define ST_ZIO_CN7_4  3
#define ST_ZIO_CN7_5  4
#define ST_ZIO_CN7_6  5
#define ST_ZIO_CN7_7  6
#define ST_ZIO_CN7_8  7
#define ST_ZIO_CN7_9  8
#define ST_ZIO_CN7_10 9
#define ST_ZIO_CN7_11 10
#define ST_ZIO_CN7_12 11
#define ST_ZIO_CN7_13 12
#define ST_ZIO_CN7_14 13
#define ST_ZIO_CN7_15 14
#define ST_ZIO_CN7_16 15
#define ST_ZIO_CN7_17 16
#define ST_ZIO_CN7_18 17
#define ST_ZIO_CN7_19 18
#define ST_ZIO_CN7_20 19

/* CN8 connector (upper left) */
#define ST_ZIO_CN8_1  20
#define ST_ZIO_CN8_2  21
#define ST_ZIO_CN8_3  22
#define ST_ZIO_CN8_4  23
#define ST_ZIO_CN8_5  24
#define ST_ZIO_CN8_6  25
#define ST_ZIO_CN8_7  26
#define ST_ZIO_CN8_8  27
#define ST_ZIO_CN8_9  28
#define ST_ZIO_CN8_10 29
#define ST_ZIO_CN8_11 30
#define ST_ZIO_CN8_12 31
#define ST_ZIO_CN8_13 32
#define ST_ZIO_CN8_14 33
#define ST_ZIO_CN8_15 34
#define ST_ZIO_CN8_16 35

/* CN9 connector (lower left) */
#define ST_ZIO_CN9_1  36
#define ST_ZIO_CN9_2  37
#define ST_ZIO_CN9_3  38
#define ST_ZIO_CN9_4  39
#define ST_ZIO_CN9_5  40
#define ST_ZIO_CN9_6  41
#define ST_ZIO_CN9_7  42
#define ST_ZIO_CN9_8  43
#define ST_ZIO_CN9_9  44
#define ST_ZIO_CN9_10 45
#define ST_ZIO_CN9_11 46
#define ST_ZIO_CN9_12 47
#define ST_ZIO_CN9_13 48
#define ST_ZIO_CN9_14 49
#define ST_ZIO_CN9_15 50
#define ST_ZIO_CN9_16 51
#define ST_ZIO_CN9_17 52
#define ST_ZIO_CN9_18 53
#define ST_ZIO_CN9_19 54
#define ST_ZIO_CN9_20 55
#define ST_ZIO_CN9_21 56
#define ST_ZIO_CN9_22 57
#define ST_ZIO_CN9_23 58
#define ST_ZIO_CN9_24 59
#define ST_ZIO_CN9_25 60
#define ST_ZIO_CN9_26 61
#define ST_ZIO_CN9_27 62
#define ST_ZIO_CN9_28 63
#define ST_ZIO_CN9_29 64
#define ST_ZIO_CN9_30 65

/* CN10 connector (lower right) */
#define ST_ZIO_CN10_1  66
#define ST_ZIO_CN10_2  67
#define ST_ZIO_CN10_3  68
#define ST_ZIO_CN10_4  69
#define ST_ZIO_CN10_5  70
#define ST_ZIO_CN10_6  71
#define ST_ZIO_CN10_7  72
#define ST_ZIO_CN10_8  73
#define ST_ZIO_CN10_9  74
#define ST_ZIO_CN10_10 75
#define ST_ZIO_CN10_11 76
#define ST_ZIO_CN10_12 77
#define ST_ZIO_CN10_13 78
#define ST_ZIO_CN10_14 79
#define ST_ZIO_CN10_15 80
#define ST_ZIO_CN10_16 81
#define ST_ZIO_CN10_17 82
#define ST_ZIO_CN10_18 83
#define ST_ZIO_CN10_19 84
#define ST_ZIO_CN10_20 85
#define ST_ZIO_CN10_21 86
#define ST_ZIO_CN10_22 87
#define ST_ZIO_CN10_23 88
#define ST_ZIO_CN10_24 89
#define ST_ZIO_CN10_25 90
#define ST_ZIO_CN10_26 91
#define ST_ZIO_CN10_27 92
#define ST_ZIO_CN10_28 93
#define ST_ZIO_CN10_29 94
#define ST_ZIO_CN10_30 95
#define ST_ZIO_CN10_31 96
#define ST_ZIO_CN10_32 97
#define ST_ZIO_CN10_33 98
#define ST_ZIO_CN10_34 99


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_ST_ZIO_HEADER_H_ */
```

## 35.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Michele Vaccari。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 25 行

CN7 连接器（Connector），位于右上方（Upper Right）。

### 注释 3：原第 47 行

CN8 连接器（Connector），位于左上方（Upper Left）。

### 注释 4：原第 65 行

CN9 连接器（Connector），位于左下方（Lower Left）。

### 注释 5：原第 97 行

CN10 连接器（Connector），位于右下方（Lower Right）。

### 注释 6：原第 135 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_ST_ZIO_HEADER_H_`。

## 35.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/st-zio-header_8h.html)

---

[上一章](P034_section_tags.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P036_stdint.h_源码浏览.md)
