---
id: learning.zephyr-docs.api-source-http-wifi-reference.page-5
title: inttypes.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/inttypes_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_inttypes.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/inttypes_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P171_____w__zephyr__zephyr__lib__libc__minimal__include__inttypes.h_文件参考.md)。

## 5.1\_原始可见代码（Source Code）

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
<a id="astdint_8h_html"></a>

```c
/*
 * Copyright (c) 2016 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_INTTYPES_H_
#define ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_INTTYPES_H_

#include <stdint.h>

#define PRId8                   "d"             /* int8_t */
#define PRId16                  "d"             /* int16_t */
#define PRId32                  "d"             /* int32_t */
#define PRId64                  "lld"           /* int64_t */
#define PRIdFAST8               "d"             /* int_fast8_t */
#define PRIdFAST16              "d"             /* int_fast16_t */
#define PRIdFAST32              "d"             /* int_fast32_t */
#define PRIdFAST64              "lld"           /* int_fast64_t */
#define PRIdLEAST8              "d"             /* int_least8_t */
#define PRIdLEAST16             "d"             /* int_least16_t */
#define PRIdLEAST32             "d"             /* int_least32_t */
#define PRIdLEAST64             "lld"           /* int_least64_t */
#define PRIdMAX                 "lld"           /* intmax_t */
#define PRIdPTR                 "ld"            /* intptr_t */

#define PRIi8                   "i"             /* int8_t */
#define PRIi16                  "i"             /* int16_t */
#define PRIi32                  "i"             /* int32_t */
#define PRIi64                  "lli"           /* int64_t */
#define PRIiFAST8               "i"             /* int_fast8_t */
#define PRIiFAST16              "i"             /* int_fast16_t */
#define PRIiFAST32              "i"             /* int_fast32_t */
#define PRIiFAST64              "lli"           /* int_fast64_t */
#define PRIiLEAST8              "i"             /* int_least8_t */
#define PRIiLEAST16             "i"             /* int_least16_t */
#define PRIiLEAST32             "i"             /* int_least32_t */
#define PRIiLEAST64             "lli"           /* int_least64_t */
#define PRIiMAX                 "lli"           /* intmax_t */
#define PRIiPTR                 "li"            /* intptr_t */

#define PRIo8                   "o"             /* int8_t */
#define PRIo16                  "o"             /* int16_t */
#define PRIo32                  "o"             /* int32_t */
#define PRIo64                  "llo"           /* int64_t */
#define PRIoFAST8               "o"             /* int_fast8_t */
#define PRIoFAST16              "o"             /* int_fast16_t */
#define PRIoFAST32              "o"             /* int_fast32_t */
#define PRIoFAST64              "llo"           /* int_fast64_t */
#define PRIoLEAST8              "o"             /* int_least8_t */
#define PRIoLEAST16             "o"             /* int_least16_t */
#define PRIoLEAST32             "o"             /* int_least32_t */
#define PRIoLEAST64             "llo"           /* int_least64_t */
#define PRIoMAX                 "llo"           /* intmax_t */
#define PRIoPTR                 "lo"            /* intptr_t */

#define PRIu8                   "u"             /* uint8_t */
#define PRIu16                  "u"             /* uint16_t */
#define PRIu32                  "u"             /* uint32_t */
#define PRIu64                  "llu"           /* uint64_t */
#define PRIuFAST8               "u"             /* uint_fast8_t */
#define PRIuFAST16              "u"             /* uint_fast16_t */
#define PRIuFAST32              "u"             /* uint_fast32_t */
#define PRIuFAST64              "llu"           /* uint_fast64_t */
#define PRIuLEAST8              "u"             /* uint_least8_t */
#define PRIuLEAST16             "u"             /* uint_least16_t */
#define PRIuLEAST32             "u"             /* uint_least32_t */
#define PRIuLEAST64             "llu"           /* uint_least64_t */
#define PRIuMAX                 "llu"           /* uintmax_t */
#define PRIuPTR                 "lu"            /* uintptr_t */

#define PRIx8                   "x"             /* uint8_t */
#define PRIx16                  "x"             /* uint16_t */
#define PRIx32                  "x"             /* uint32_t */
#define PRIx64                  "llx"           /* uint64_t */
#define PRIxFAST8               "x"             /* uint_fast8_t */
#define PRIxFAST16              "x"             /* uint_fast16_t */
#define PRIxFAST32              "x"             /* uint_fast32_t */
#define PRIxFAST64              "llx"           /* uint_fast64_t */
#define PRIxLEAST8              "x"             /* uint_least8_t */
#define PRIxLEAST16             "x"             /* uint_least16_t */
#define PRIxLEAST32             "x"             /* uint_least32_t */
#define PRIxLEAST64             "llx"           /* uint_least64_t */
#define PRIxMAX                 "llx"           /* uintmax_t */
#define PRIxPTR                 "lx"            /* uintptr_t */

#define PRIX8                   "X"             /* uint8_t */
#define PRIX16                  "X"             /* uint16_t */
#define PRIX32                  "X"             /* uint32_t */
#define PRIX64                  "llX"           /* uint64_t */
#define PRIXFAST8               "X"             /* uint_fast8_t */
#define PRIXFAST16              "X"             /* uint_fast16_t */
#define PRIXFAST32              "X"             /* uint_fast32_t */
#define PRIXFAST64              "llX"           /* uint_fast64_t */
#define PRIXLEAST8              "X"             /* uint_least8_t */
#define PRIXLEAST16             "X"             /* uint_least16_t */
#define PRIXLEAST32             "X"             /* uint_least32_t */
#define PRIXLEAST64             "llX"           /* uint_least64_t */
#define PRIXMAX                 "llX"           /* uintmax_t */
#define PRIXPTR                 "lX"            /* uintptr_t */

#endif
```

## 5.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2016 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 13 行

`int8_t`：8 位有符号整数类型（Integer Type）。

### 注释 3：原第 14 行

`int16_t`：16 位有符号整数类型（Integer Type）。

### 注释 4：原第 15 行

`int32_t`：32 位有符号整数类型（Integer Type）。

### 注释 5：原第 16 行

`int64_t`：64 位有符号整数类型（Integer Type）。

### 注释 6：原第 17 行

`int_fast8_t`：最快的至少 8 位有符号整数类型（Integer Type）。

### 注释 7：原第 18 行

`int_fast16_t`：最快的至少 16 位有符号整数类型（Integer Type）。

### 注释 8：原第 19 行

`int_fast32_t`：最快的至少 32 位有符号整数类型（Integer Type）。

### 注释 9：原第 20 行

`int_fast64_t`：最快的至少 64 位有符号整数类型（Integer Type）。

### 注释 10：原第 21 行

`int_least8_t`：至少 8 位有符号整数类型（Integer Type）。

### 注释 11：原第 22 行

`int_least16_t`：至少 16 位有符号整数类型（Integer Type）。

### 注释 12：原第 23 行

`int_least32_t`：至少 32 位有符号整数类型（Integer Type）。

### 注释 13：原第 24 行

`int_least64_t`：至少 64 位有符号整数类型（Integer Type）。

### 注释 14：原第 25 行

`intmax_t`：最大宽度的有符号整数类型（Integer Type）。

### 注释 15：原第 26 行

`intptr_t`：可表示指针值的有符号整数类型（Integer Type）。

### 注释 16：原第 28 行

`int8_t`：8 位有符号整数类型（Integer Type）。

### 注释 17：原第 29 行

`int16_t`：16 位有符号整数类型（Integer Type）。

### 注释 18：原第 30 行

`int32_t`：32 位有符号整数类型（Integer Type）。

### 注释 19：原第 31 行

`int64_t`：64 位有符号整数类型（Integer Type）。

### 注释 20：原第 32 行

`int_fast8_t`：最快的至少 8 位有符号整数类型（Integer Type）。

### 注释 21：原第 33 行

`int_fast16_t`：最快的至少 16 位有符号整数类型（Integer Type）。

### 注释 22：原第 34 行

`int_fast32_t`：最快的至少 32 位有符号整数类型（Integer Type）。

### 注释 23：原第 35 行

`int_fast64_t`：最快的至少 64 位有符号整数类型（Integer Type）。

### 注释 24：原第 36 行

`int_least8_t`：至少 8 位有符号整数类型（Integer Type）。

### 注释 25：原第 37 行

`int_least16_t`：至少 16 位有符号整数类型（Integer Type）。

### 注释 26：原第 38 行

`int_least32_t`：至少 32 位有符号整数类型（Integer Type）。

### 注释 27：原第 39 行

`int_least64_t`：至少 64 位有符号整数类型（Integer Type）。

### 注释 28：原第 40 行

`intmax_t`：最大宽度的有符号整数类型（Integer Type）。

### 注释 29：原第 41 行

`intptr_t`：可表示指针值的有符号整数类型（Integer Type）。

### 注释 30：原第 43 行

`int8_t`：8 位有符号整数类型（Integer Type）。

### 注释 31：原第 44 行

`int16_t`：16 位有符号整数类型（Integer Type）。

### 注释 32：原第 45 行

`int32_t`：32 位有符号整数类型（Integer Type）。

### 注释 33：原第 46 行

`int64_t`：64 位有符号整数类型（Integer Type）。

### 注释 34：原第 47 行

`int_fast8_t`：最快的至少 8 位有符号整数类型（Integer Type）。

### 注释 35：原第 48 行

`int_fast16_t`：最快的至少 16 位有符号整数类型（Integer Type）。

### 注释 36：原第 49 行

`int_fast32_t`：最快的至少 32 位有符号整数类型（Integer Type）。

### 注释 37：原第 50 行

`int_fast64_t`：最快的至少 64 位有符号整数类型（Integer Type）。

### 注释 38：原第 51 行

`int_least8_t`：至少 8 位有符号整数类型（Integer Type）。

### 注释 39：原第 52 行

`int_least16_t`：至少 16 位有符号整数类型（Integer Type）。

### 注释 40：原第 53 行

`int_least32_t`：至少 32 位有符号整数类型（Integer Type）。

### 注释 41：原第 54 行

`int_least64_t`：至少 64 位有符号整数类型（Integer Type）。

### 注释 42：原第 55 行

`intmax_t`：最大宽度的有符号整数类型（Integer Type）。

### 注释 43：原第 56 行

`intptr_t`：可表示指针值的有符号整数类型（Integer Type）。

### 注释 44：原第 58 行

`uint8_t`：8 位无符号整数类型（Integer Type）。

### 注释 45：原第 59 行

`uint16_t`：16 位无符号整数类型（Integer Type）。

### 注释 46：原第 60 行

`uint32_t`：32 位无符号整数类型（Integer Type）。

### 注释 47：原第 61 行

`uint64_t`：64 位无符号整数类型（Integer Type）。

### 注释 48：原第 62 行

`uint_fast8_t`：最快的至少 8 位无符号整数类型（Integer Type）。

### 注释 49：原第 63 行

`uint_fast16_t`：最快的至少 16 位无符号整数类型（Integer Type）。

### 注释 50：原第 64 行

`uint_fast32_t`：最快的至少 32 位无符号整数类型（Integer Type）。

### 注释 51：原第 65 行

`uint_fast64_t`：最快的至少 64 位无符号整数类型（Integer Type）。

### 注释 52：原第 66 行

`uint_least8_t`：至少 8 位无符号整数类型（Integer Type）。

### 注释 53：原第 67 行

`uint_least16_t`：至少 16 位无符号整数类型（Integer Type）。

### 注释 54：原第 68 行

`uint_least32_t`：至少 32 位无符号整数类型（Integer Type）。

### 注释 55：原第 69 行

`uint_least64_t`：至少 64 位无符号整数类型（Integer Type）。

### 注释 56：原第 70 行

`uintmax_t`：最大宽度的无符号整数类型（Integer Type）。

### 注释 57：原第 71 行

`uintptr_t`：可表示指针值的无符号整数类型（Integer Type）。

### 注释 58：原第 73 行

`uint8_t`：8 位无符号整数类型（Integer Type）。

### 注释 59：原第 74 行

`uint16_t`：16 位无符号整数类型（Integer Type）。

### 注释 60：原第 75 行

`uint32_t`：32 位无符号整数类型（Integer Type）。

### 注释 61：原第 76 行

`uint64_t`：64 位无符号整数类型（Integer Type）。

### 注释 62：原第 77 行

`uint_fast8_t`：最快的至少 8 位无符号整数类型（Integer Type）。

### 注释 63：原第 78 行

`uint_fast16_t`：最快的至少 16 位无符号整数类型（Integer Type）。

### 注释 64：原第 79 行

`uint_fast32_t`：最快的至少 32 位无符号整数类型（Integer Type）。

### 注释 65：原第 80 行

`uint_fast64_t`：最快的至少 64 位无符号整数类型（Integer Type）。

### 注释 66：原第 81 行

`uint_least8_t`：至少 8 位无符号整数类型（Integer Type）。

### 注释 67：原第 82 行

`uint_least16_t`：至少 16 位无符号整数类型（Integer Type）。

### 注释 68：原第 83 行

`uint_least32_t`：至少 32 位无符号整数类型（Integer Type）。

### 注释 69：原第 84 行

`uint_least64_t`：至少 64 位无符号整数类型（Integer Type）。

### 注释 70：原第 85 行

`uintmax_t`：最大宽度的无符号整数类型（Integer Type）。

### 注释 71：原第 86 行

`uintptr_t`：可表示指针值的无符号整数类型（Integer Type）。

### 注释 72：原第 88 行

`uint8_t`：8 位无符号整数类型（Integer Type）。

### 注释 73：原第 89 行

`uint16_t`：16 位无符号整数类型（Integer Type）。

### 注释 74：原第 90 行

`uint32_t`：32 位无符号整数类型（Integer Type）。

### 注释 75：原第 91 行

`uint64_t`：64 位无符号整数类型（Integer Type）。

### 注释 76：原第 92 行

`uint_fast8_t`：最快的至少 8 位无符号整数类型（Integer Type）。

### 注释 77：原第 93 行

`uint_fast16_t`：最快的至少 16 位无符号整数类型（Integer Type）。

### 注释 78：原第 94 行

`uint_fast32_t`：最快的至少 32 位无符号整数类型（Integer Type）。

### 注释 79：原第 95 行

`uint_fast64_t`：最快的至少 64 位无符号整数类型（Integer Type）。

### 注释 80：原第 96 行

`uint_least8_t`：至少 8 位无符号整数类型（Integer Type）。

### 注释 81：原第 97 行

`uint_least16_t`：至少 16 位无符号整数类型（Integer Type）。

### 注释 82：原第 98 行

`uint_least32_t`：至少 32 位无符号整数类型（Integer Type）。

### 注释 83：原第 99 行

`uint_least64_t`：至少 64 位无符号整数类型（Integer Type）。

### 注释 84：原第 100 行

`uintmax_t`：最大宽度的无符号整数类型（Integer Type）。

### 注释 85：原第 101 行

`uintptr_t`：可表示指针值的无符号整数类型（Integer Type）。

## 5.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P171_____w__zephyr__zephyr__lib__libc__minimal__include__inttypes.h_文件参考.md)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)

---

[上一章](P004_intc_esp32.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P006_ite-it51xxx-intc.h_源码浏览.md)
