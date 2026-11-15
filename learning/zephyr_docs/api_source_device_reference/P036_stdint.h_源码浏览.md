---
id: learning.zephyr-docs.api-source-device-reference.page-36
title: stdint.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第36章\_stdint.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)。

## 36.1\_原始可见代码（Source Code）

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
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0bd5dec00e345e69027427f8621d6a6c"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a1a01d6a4e68e435471be2ae8db7e8fdc"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a2464ed69ccd3fd2b3b4c93cb78f6fa20"></a>
<a id="astdint_8h_html_a3a4bc1e426626e17f6a6e0f64decec56"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a4462f62ae74ff8172526401354d2fc9b"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>
<a id="astdint_8h_html_a530ba8ffc89f6393d2d0e2fb2db38b54"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_a61d44370ed65907c324edad5e8d34632"></a>
<a id="astdint_8h_html_a62c711f66c6d29c81429aeafdc4bc592"></a>
<a id="astdint_8h_html_a678494ae5435d8904e7972c94618e774"></a>
<a id="astdint_8h_html_a888269be199d49b7f40006aaafa5a350"></a>
<a id="astdint_8h_html_a8a5003442318117c64d16d6f32f64f37"></a>
<a id="astdint_8h_html_a98f573ff8187ff09c9594a3f2af7be0d"></a>
<a id="astdint_8h_html_a9d6c1dc12f73927ba41516de04a5fdb8"></a>
<a id="astdint_8h_html_aa44ff507c3d9a49e27fac64e9fadf062"></a>
<a id="astdint_8h_html_aaabed6e034edb01c259c003894d7f7c8"></a>
<a id="astdint_8h_html_aac7deaa1633720ec64bd432bbc31af40"></a>
<a id="astdint_8h_html_aba0cb5638c172422eb4a7555a143fbbc"></a>
<a id="astdint_8h_html_abcdb0a9f6e7d139ad4f521ab8f4efdc0"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astdint_8h_html_adb5f4bf8afa3bee9e4da1bb9daf4908d"></a>
<a id="astdint_8h_html_afe270aee8d96ad7f279a4020b9d58bdf"></a>

```c
/* stdint.h */

/*
 * Copyright (c) 2014 Wind River Systems, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_STDINT_H_
#define ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_STDINT_H_

#ifdef __cplusplus
extern "C" {
#endif

#define INT8_MAX    __INT8_MAX__
#define INT16_MAX   __INT16_MAX__
#define INT32_MAX   __INT32_MAX__
#define INT64_MAX   __INT64_MAX__
#define INTMAX_MAX  __INT64_MAX__

#define INT8_MIN    (-INT8_MAX - 1)
#define INT16_MIN   (-INT16_MAX - 1)
#define INT32_MIN   (-INT32_MAX - 1)
#define INT64_MIN   (-INT64_MAX - 1LL)

#define UINT8_MAX   __UINT8_MAX__
#define UINT16_MAX  __UINT16_MAX__
#define UINT32_MAX  __UINT32_MAX__
#define UINT64_MAX  __UINT64_MAX__
#define UINTMAX_MAX __UINT64_MAX__

#define INT_FAST8_MAX    __INT_FAST8_MAX__
#define INT_FAST16_MAX   __INT_FAST16_MAX__
#define INT_FAST32_MAX   __INT_FAST32_MAX__
#define INT_FAST64_MAX   __INT_FAST64_MAX__

#define INT_FAST8_MIN    (-INT_FAST8_MAX - 1)
#define INT_FAST16_MIN   (-INT_FAST16_MAX - 1)
#define INT_FAST32_MIN   (-INT_FAST32_MAX - 1)
#define INT_FAST64_MIN   (-INT_FAST64_MAX - 1LL)

#define UINT_FAST8_MAX    __UINT_FAST8_MAX__
#define UINT_FAST16_MAX   __UINT_FAST16_MAX__
#define UINT_FAST32_MAX   __UINT_FAST32_MAX__
#define UINT_FAST64_MAX   __UINT_FAST64_MAX__

#define INT_LEAST8_MAX    __INT_LEAST8_MAX__
#define INT_LEAST16_MAX   __INT_LEAST16_MAX__
#define INT_LEAST32_MAX   __INT_LEAST32_MAX__
#define INT_LEAST64_MAX   __INT_LEAST64_MAX__

#define INT_LEAST8_MIN    (-INT_LEAST8_MAX - 1)
#define INT_LEAST16_MIN   (-INT_LEAST16_MAX - 1)
#define INT_LEAST32_MIN   (-INT_LEAST32_MAX - 1)
#define INT_LEAST64_MIN   (-INT_LEAST64_MAX - 1LL)

#define UINT_LEAST8_MAX    __UINT_LEAST8_MAX__
#define UINT_LEAST16_MAX   __UINT_LEAST16_MAX__
#define UINT_LEAST32_MAX   __UINT_LEAST32_MAX__
#define UINT_LEAST64_MAX   __UINT_LEAST64_MAX__

#define INTPTR_MAX  __INTPTR_MAX__
#define INTPTR_MIN  (-INTPTR_MAX - 1)
#define UINTPTR_MAX __UINTPTR_MAX__

#define PTRDIFF_MAX __PTRDIFF_MAX__
#define PTRDIFF_MIN (-PTRDIFF_MAX - 1)

#define SIZE_MAX    __SIZE_MAX__

typedef __INT8_TYPE__           int8_t;
typedef __INT16_TYPE__          int16_t;
typedef __INT32_TYPE__          int32_t;
typedef __INT64_TYPE__          int64_t;
typedef __INT64_TYPE__          intmax_t;

typedef __INT_FAST8_TYPE__      int_fast8_t;
typedef __INT_FAST16_TYPE__     int_fast16_t;
typedef __INT_FAST32_TYPE__     int_fast32_t;
typedef __INT_FAST64_TYPE__     int_fast64_t;

typedef __INT_LEAST8_TYPE__     int_least8_t;
typedef __INT_LEAST16_TYPE__    int_least16_t;
typedef __INT_LEAST32_TYPE__    int_least32_t;
typedef __INT_LEAST64_TYPE__    int_least64_t;

typedef __UINT8_TYPE__          uint8_t;
typedef __UINT16_TYPE__         uint16_t;
typedef __UINT32_TYPE__         uint32_t;
typedef __UINT64_TYPE__         uint64_t;
typedef __UINT64_TYPE__         uintmax_t;

typedef __UINT_FAST8_TYPE__     uint_fast8_t;
typedef __UINT_FAST16_TYPE__    uint_fast16_t;
typedef __UINT_FAST32_TYPE__    uint_fast32_t;
typedef __UINT_FAST64_TYPE__    uint_fast64_t;

typedef __UINT_LEAST8_TYPE__    uint_least8_t;
typedef __UINT_LEAST16_TYPE__   uint_least16_t;
typedef __UINT_LEAST32_TYPE__   uint_least32_t;
typedef __UINT_LEAST64_TYPE__   uint_least64_t;

typedef __INTPTR_TYPE__         intptr_t;
typedef __UINTPTR_TYPE__        uintptr_t;

#if defined(__GNUC__) || defined(__clang__)
/* These macros must produce constant integer expressions, which can't
 * be done in the preprocessor (casts aren't allowed).  Defer to the
 * GCC internal functions where they're available.
 */
#define INT8_C(_v) __INT8_C(_v)
#define INT16_C(_v) __INT16_C(_v)
#define INT32_C(_v) __INT32_C(_v)
#define INT64_C(_v) __INT64_C(_v)
#define INTMAX_C(_v) __INTMAX_C(_v)

#define UINT8_C(_v) __UINT8_C(_v)
#define UINT16_C(_v) __UINT16_C(_v)
#define UINT32_C(_v) __UINT32_C(_v)
#define UINT64_C(_v) __UINT64_C(_v)
#define UINTMAX_C(_v) __UINTMAX_C(_v)
#endif /* defined(__GNUC__) || defined(__clang__) */

#ifdef __CCAC__
#ifndef __INT8_C
#define __INT8_C(x)     x
#endif

#ifndef INT8_C
#define INT8_C(x)       __INT8_C(x)
#endif

#ifndef __UINT8_C
#define __UINT8_C(x)    x ## U
#endif

#ifndef UINT8_C
#define UINT8_C(x)      __UINT8_C(x)
#endif

#ifndef __INT16_C
#define __INT16_C(x)    x
#endif

#ifndef INT16_C
#define INT16_C(x)      __INT16_C(x)
#endif

#ifndef __UINT16_C
#define __UINT16_C(x)   x ## U
#endif

#ifndef UINT16_C
#define UINT16_C(x)     __UINT16_C(x)
#endif

#ifndef __INT32_C
#define __INT32_C(x)    x
#endif

#ifndef INT32_C
#define INT32_C(x)      __INT32_C(x)
#endif

#ifndef __UINT32_C
#define __UINT32_C(x)   x ## U
#endif

#ifndef UINT32_C
#define UINT32_C(x)     __UINT32_C(x)
#endif

#ifndef __INT64_C
#define __INT64_C(x)    x
#endif

#ifndef INT64_C
#define INT64_C(x)      __INT64_C(x)
#endif

#ifndef __UINT64_C
#define __UINT64_C(x)   x ## ULL
#endif

#ifndef UINT64_C
#define UINT64_C(x)     __UINT64_C(x)
#endif

#ifndef __INTMAX_C
#define __INTMAX_C(x)   x
#endif

#ifndef INTMAX_C
#define INTMAX_C(x)     __INTMAX_C(x)
#endif

#ifndef __UINTMAX_C
#define __UINTMAX_C(x)  x ## ULL
#endif

#ifndef UINTMAX_C
#define UINTMAX_C(x)    __UINTMAX_C(x)
#endif
#endif /* __CCAC__ */

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_STDINT_H_ */
```

## 36.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

标准整数类型头文件（Standard Integer Types Header）：`stdint.h`。

### 注释 2：原第 3 行

版权（Copyright）：© 2014 Wind River Systems, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 3：原第 108 行

这些宏必须生成常量整数表达式（Constant Integer Expressions）；预处理器（Preprocessor）不允许类型转换（Casts），因此无法完成此任务。若 GCC 内部函数（Internal Functions）可用，则交由它们处理。

### 注释 4：原第 123 行

条件编译（Conditional Compilation）：`defined(__GNUC__) || defined(__clang__)`。

### 注释 5：原第 205 行

编译器标识（Compiler Identifier）：`__CCAC__`。

### 注释 6：原第 211 行

头文件保护宏（Header guard）标记：`ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_STDINT_H_`。

## 36.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)
- [intmax_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a9d6c1dc12f73927ba41516de04a5fdb8)
- [int_fast8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a98f573ff8187ff09c9594a3f2af7be0d)
- [int_fast16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a888269be199d49b7f40006aaafa5a350)
- [int_fast32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a530ba8ffc89f6393d2d0e2fb2db38b54)
- [int_fast64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#abcdb0a9f6e7d139ad4f521ab8f4efdc0)
- [int_least8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#adb5f4bf8afa3bee9e4da1bb9daf4908d)
- [int_least16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3a4bc1e426626e17f6a6e0f64decec56)
- [int_least32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4462f62ae74ff8172526401354d2fc9b)
- [int_least64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a8a5003442318117c64d16d6f32f64f37)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [uintmax_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#aac7deaa1633720ec64bd432bbc31af40)
- [uint_fast8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2464ed69ccd3fd2b3b4c93cb78f6fa20)
- [uint_fast16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#aaabed6e034edb01c259c003894d7f7c8)
- [uint_fast32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#aa44ff507c3d9a49e27fac64e9fadf062)
- [uint_fast64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a62c711f66c6d29c81429aeafdc4bc592)
- [uint_least8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a61d44370ed65907c324edad5e8d34632)
- [uint_least16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a1a01d6a4e68e435471be2ae8db7e8fdc)
- [uint_least32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a678494ae5435d8904e7972c94618e774)
- [uint_least64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#aba0cb5638c172422eb4a7555a143fbbc)
- [intptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0bd5dec00e345e69027427f8621d6a6c)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)

---

[上一章](P035_st-zio-header.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P037_stm32c5_clock.h_源码浏览.md)
