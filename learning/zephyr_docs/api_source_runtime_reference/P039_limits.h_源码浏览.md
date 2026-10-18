---
id: learning.zephyr-docs.api-source-runtime-reference.page-39
title: limits.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/limits_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_limits.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/limits_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/limits_8h.html)。

## 39.1\_原始可见代码（Source Code）

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
<a id="aposix__limits_8h_html"></a>

```c
/* limits.h */

/*
 * Copyright (c) 2014 Wind River Systems, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_LIMITS_H_
#define ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_LIMITS_H_

#ifdef __cplusplus
extern "C" {
#endif

#if __CHAR_BIT__ == 8
#define UCHAR_MAX       0xFFU
#else
#error "unexpected __CHAR_BIT__ value"
#endif

#define SCHAR_MAX       __SCHAR_MAX__
#define SCHAR_MIN       (-SCHAR_MAX - 1)

#ifdef __CHAR_UNSIGNED__
        /* 'char' is an unsigned type */
        #define CHAR_MAX  UCHAR_MAX
        #define CHAR_MIN  0
#else
        /* 'char' is a signed type */
        #define CHAR_MAX  SCHAR_MAX
        #define CHAR_MIN  SCHAR_MIN
#endif

#define CHAR_BIT        __CHAR_BIT__
#define LONG_BIT        (__SIZEOF_LONG__ * CHAR_BIT)
#define WORD_BIT        (__SIZEOF_POINTER__ * CHAR_BIT)

#define INT_MAX         __INT_MAX__
#define SHRT_MAX        __SHRT_MAX__
#define LONG_MAX        __LONG_MAX__
#define LLONG_MAX       __LONG_LONG_MAX__

#define INT_MIN         (-INT_MAX - 1)
#define SHRT_MIN        (-SHRT_MAX - 1)
#define LONG_MIN        (-LONG_MAX - 1L)
#define LLONG_MIN       (-LLONG_MAX - 1LL)

#if __SIZE_MAX__ == __UINT32_MAX__
#define SSIZE_MAX       __INT32_MAX__
#elif __SIZE_MAX__ == __UINT64_MAX__
#define SSIZE_MAX       __INT64_MAX__
#else
#error "unexpected __SIZE_MAX__ value"
#endif

#if __SIZEOF_SHORT__ == 2
#define USHRT_MAX       0xFFFFU
#else
#error "unexpected __SIZEOF_SHORT__ value"
#endif

#if __SIZEOF_INT__ == 4
#define UINT_MAX        0xFFFFFFFFU
#else
#error "unexpected __SIZEOF_INT__ value"
#endif

#if __SIZEOF_LONG__ == 4
#define ULONG_MAX       0xFFFFFFFFUL
#elif __SIZEOF_LONG__ == 8
#define ULONG_MAX       0xFFFFFFFFFFFFFFFFUL
#else
#error "unexpected __SIZEOF_LONG__ value"
#endif

#if __SIZEOF_LONG_LONG__ == 8
#define ULLONG_MAX      0xFFFFFFFFFFFFFFFFULL
#else
#error "unexpected __SIZEOF_LONG_LONG__ value"
#endif

#if defined(_POSIX_C_SOURCE) || defined(__DOXYGEN__)

#include <zephyr/posix/posix_limits.h>

#else

#define PATH_MAX    256

#endif

#ifdef __cplusplus
}
#endif

#endif  /* ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_LIMITS_H_ */
```

## 39.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

`limits.h` 头文件。

### 注释 2：原第 3 行

版权（Copyright）：© 2014 Wind River Systems, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 3：原第 26 行

`char` 是无符号类型（Unsigned type）。

### 注释 4：原第 30 行

`char` 是有符号类型（Signed type）。

### 注释 5：原第 97 行

头文件保护宏（Header guard）标记：`ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_LIMITS_H_`。

## 39.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/limits_8h.html)
- [zephyr/posix/posix_limits.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__limits_8h.html)
- [posix_limits.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__limits_8h.html)

---

[上一章](P038_types.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P040_lwm2m.h_源码浏览.md)
