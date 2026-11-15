---
id: learning.zephyr-docs.api-source-compiler-device-reference.page-23
title: toolchain.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_toolchain.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)。

## 23.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00023"></a>
<a id="l00027"></a>
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
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
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
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00159"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00306"></a>
<a id="l00310"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
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
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00442"></a>
<a id="l00443"></a>

```c
/*
 * Copyright (c) 2010-2014, Wind River Systems, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_TOOLCHAIN_H_
#define ZEPHYR_INCLUDE_TOOLCHAIN_H_



#ifdef __has_builtin
#define HAS_BUILTIN(x) __has_builtin(x)
#else
/*
 * The compiler doesn't provide the __has_builtin() macro, so instead we depend
 * on the toolchain-specific headers to define HAS_BUILTIN_x for the builtins
 * supported.
 */
#define HAS_BUILTIN(x) HAS_BUILTIN_##x
#endif

#if defined(__TOOLCHAIN_CUSTOM__)
/* This include line exists for off-tree definitions of compilers,
 * and therefore this header is not meant to exist in-tree
 */
#include <toolchain/other.h>
#elif defined(__XCC__)
#include <zephyr/toolchain/xcc.h>
#elif defined(__CCAC__)
#include <zephyr/toolchain/mwdt.h>
#elif defined(__ARMCOMPILER_VERSION)
#include <zephyr/toolchain/armclang.h>
#elif defined(__IAR_SYSTEMS_ICC__)
#include <zephyr/toolchain/iar.h>
#elif defined(__llvm__) ||                                                                         \
        (defined(_LINKER) && (defined(__LLD_LINKER_CMD__) || defined(__ELD_LINKER_CMD__)))
#include <zephyr/toolchain/llvm.h>
#elif defined(__GNUC__) || (defined(_LINKER) && defined(__GCC_LINKER_CMD__))
#include <zephyr/toolchain/gcc.h>
#else
#error "Invalid/unknown toolchain configuration"
#endif

#ifndef __noasan
#define __noasan /**/
#endif

#ifndef TOOLCHAIN_GCC_VERSION
#define TOOLCHAIN_GCC_VERSION 0
#endif

#ifndef TOOLCHAIN_CLANG_VERSION
#define TOOLCHAIN_CLANG_VERSION 0
#endif

#ifndef TOOLCHAIN_HAS_PRAGMA_DIAG
#define TOOLCHAIN_HAS_PRAGMA_DIAG 0
#endif

#if defined(__STDC_VERSION__) && __STDC_VERSION__ >= 201112L
/* _Generic is introduced in C11, so it is supported. */
# ifdef TOOLCHAIN_HAS_C_GENERIC
#  undef TOOLCHAIN_HAS_C_GENERIC
# endif
# define TOOLCHAIN_HAS_C_GENERIC 1
#else
# ifndef TOOLCHAIN_HAS_C_GENERIC
#  define TOOLCHAIN_HAS_C_GENERIC 0
# endif
#endif

#ifndef TOOLCHAIN_HAS_C_AUTO_TYPE
#define TOOLCHAIN_HAS_C_AUTO_TYPE 0
#endif

#ifndef TOOLCHAIN_HAS_ZLA
#define TOOLCHAIN_HAS_ZLA 0
#endif

#if TOOLCHAIN_HAS_PRAGMA_DIAG
#define TOOLCHAIN_PRAGMA(x) _Pragma(#x)
#else
#define TOOLCHAIN_PRAGMA(x)
#endif



#ifndef TOOLCHAIN_WARNING_ADDRESS_OF_PACKED_MEMBER
#define TOOLCHAIN_WARNING_ADDRESS_OF_PACKED_MEMBER
#endif

#ifndef TOOLCHAIN_WARNING_ARRAY_BOUNDS
#define TOOLCHAIN_WARNING_ARRAY_BOUNDS
#endif

#ifndef TOOLCHAIN_WARNING_ATTRIBUTES
#define TOOLCHAIN_WARNING_ATTRIBUTES
#endif

#ifndef TOOLCHAIN_WARNING_DELETE_NON_VIRTUAL_DTOR
#define TOOLCHAIN_WARNING_DELETE_NON_VIRTUAL_DTOR
#endif

#ifndef TOOLCHAIN_WARNING_EXTRA
#define TOOLCHAIN_WARNING_EXTRA
#endif

#ifndef TOOLCHAIN_WARNING_ARM_INTERRUPT_VFP_CLOBBER
#define TOOLCHAIN_WARNING_ARM_INTERRUPT_VFP_CLOBBER
#endif

#ifndef TOOLCHAIN_WARNING_NONNULL
#define TOOLCHAIN_WARNING_NONNULL
#endif

#ifndef TOOLCHAIN_WARNING_POINTER_ARITH
#define TOOLCHAIN_WARNING_POINTER_ARITH
#endif

#ifndef TOOLCHAIN_WARNING_SHADOW
#define TOOLCHAIN_WARNING_SHADOW
#endif

#ifndef TOOLCHAIN_WARNING_UNUSED_LABEL
#define TOOLCHAIN_WARNING_UNUSED_LABEL
#endif

#ifndef TOOLCHAIN_WARNING_UNUSED_VARIABLE
#define TOOLCHAIN_WARNING_UNUSED_VARIABLE
#endif

#ifndef TOOLCHAIN_WARNING_ALWAYS_INLINE
#define TOOLCHAIN_WARNING_ALWAYS_INLINE
#endif

#ifndef TOOLCHAIN_WARNING_CAST_QUAL
#define TOOLCHAIN_WARNING_CAST_QUAL
#endif



#ifndef TOOLCHAIN_DISABLE_WARNING
#define TOOLCHAIN_DISABLE_WARNING(warning)
#endif

#ifndef TOOLCHAIN_ENABLE_WARNING
#define TOOLCHAIN_ENABLE_WARNING(warning)
#endif

#ifndef TOOLCHAIN_DISABLE_CLANG_WARNING
#define TOOLCHAIN_DISABLE_CLANG_WARNING(warning)
#endif

#ifndef TOOLCHAIN_ENABLE_CLANG_WARNING
#define TOOLCHAIN_ENABLE_CLANG_WARNING(warning)
#endif

#ifndef TOOLCHAIN_DISABLE_GCC_WARNING
#define TOOLCHAIN_DISABLE_GCC_WARNING(warning)
#endif

#ifndef TOOLCHAIN_ENABLE_GCC_WARNING
#define TOOLCHAIN_ENABLE_GCC_WARNING(warning)
#endif

#ifndef TOOLCHAIN_DISABLE_IAR_WARNING
#define TOOLCHAIN_DISABLE_IAR_WARNING(warning)
#endif

#ifndef TOOLCHAIN_ENABLE_IAR_WARNING
#define TOOLCHAIN_ENABLE_IAR_WARNING(warning)
#endif


/*
 * Ensure that __BYTE_ORDER__ and related preprocessor definitions are defined,
 * and that they match the Kconfig option that is used in the code itself to
 * check for endianness.
 */
#ifndef _LINKER
#if !defined(__BYTE_ORDER__) || !defined(__ORDER_BIG_ENDIAN__) || \
    !defined(__ORDER_LITTLE_ENDIAN__)

/*
 * Displaying values unfortunately requires #pragma message which can't
 * be taken for granted + STRINGIFY() which is not available in this .h
 * file.
 */
#error "At least one byte _ORDER_ macro is not defined"

#else

#if (defined(CONFIG_BIG_ENDIAN) && (__BYTE_ORDER__ != __ORDER_BIG_ENDIAN__)) || \
    (defined(CONFIG_LITTLE_ENDIAN) && (__BYTE_ORDER__ != __ORDER_LITTLE_ENDIAN__))

#  error "Kconfig/toolchain endianness mismatch:"

#  if (__BYTE_ORDER__ != __ORDER_BIG_ENDIAN__) && (__BYTE_ORDER__ != __ORDER_LITTLE_ENDIAN__)
#    error "Unknown __BYTE_ORDER__ value"
#  else
#    ifdef CONFIG_BIG_ENDIAN
#      error "CONFIG_BIG_ENDIAN but __ORDER_LITTLE_ENDIAN__"
#    endif
#    ifdef CONFIG_LITTLE_ENDIAN
#      error "CONFIG_LITTLE_ENDIAN but __ORDER_BIG_ENDIAN__"
#   endif
# endif

#endif  /* Endianness mismatch */

#endif /* all _ORDER_ macros defined */

#endif /* !_LINKER */


#endif /* ZEPHYR_INCLUDE_TOOLCHAIN_H_ */
```

## 23.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2010-2014, Wind River Systems, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 41 行

编译器没有提供 `__has_builtin()` 宏，因此改为依赖工具链专用头文件，为支持的内建函数（builtins）定义 `HAS_BUILTIN_x`。

### 注释 3：原第 50 行

此包含语句用于源码树之外（off-tree）的编译器定义，因此本头文件不应存在于源码树之内（in-tree）。

### 注释 4：原第 83 行

空注释，无需翻译。

### 注释 5：原第 115 行

`_Generic` 在 C11 中引入，因此受支持。

### 注释 6：原第 401 行

确保定义 `__BYTE_ORDER__` 及相关预处理器定义，且它们与代码本身用于检查字节序（endianness）的 Kconfig 选项一致。

### 注释 7：原第 410 行

可惜，显示数值需要使用不能保证始终可用的 `#pragma message`，以及本 `.h` 文件中不可用的 `STRINGIFY()`。

### 注释 8：原第 435 行

字节序不匹配（endianness mismatch）。

### 注释 9：原第 437 行

所有 `_ORDER_` 宏均已定义。

### 注释 10：原第 439 行

条件表达式：`!_LINKER`。

### 注释 11：原第 443 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_TOOLCHAIN_H_`。

## 23.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P022_stm32mp2_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P024_wch_exti.h_源码浏览.md)
