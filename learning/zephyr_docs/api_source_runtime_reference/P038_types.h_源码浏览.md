---
id: learning.zephyr-docs.api-source-runtime-reference.page-38
title: types.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_types.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)。

## 38.1\_原始可见代码（Source Code）

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
<a id="a__timespec_8h_html_aa17c461cd5eca7fc12a66daa803c7fd7"></a>
<a id="a__timespec_8h_html_ad7acf95ceafb15a1d8d86af0c4982995"></a>
<a id="a__types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a5c5d83d87790efd59ea916c2b99f9118"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a98a5cc5f4a350bf5652565021a2f239f"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_adb8322e115035a284aab704909e63d00"></a>
<a id="astdint_8h_html"></a>

```c
/*
 * Copyright (c) 2016 Intel Corporation
 * Copyright (c) 2017 ARM Ltd
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_SYS_TYPES_H_
#define ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_SYS_TYPES_H_

#include <stdint.h>
#include <sys/_types.h>

typedef unsigned int mode_t;

#if !defined(__ssize_t_defined)
#define __ssize_t_defined

/* Static code analysis tool can raise a violation
 * in the line below where name of macro 'unsigned' is the same
 * as keyword. It is made on purpose, deliberated deviation.
 *
 * We trick compiler to make sure the type of ssize_t won't be unsigned long.
 * As otherwise the type of ssize_t will be unsigned long
 * which is not correct. More details view in commit b889120
 */
#define unsigned signed /* parasoft-suppress MISRAC2012-RULE_20_4-a MISRAC2012-RULE_20_4-b */
typedef __SIZE_TYPE__ ssize_t;
#undef unsigned

#endif

#if !defined(__off_t_defined)
#define __off_t_defined
/* off_t is defined such that it matches the size of a pointer */
typedef __INTPTR_TYPE__ off_t;
#endif

#if !defined(__time_t_defined)
#define __time_t_defined
typedef _TIME_T_ time_t;
#endif

#if !defined(__suseconds_t_defined)
#define __suseconds_t_defined
typedef _SUSECONDS_T_ suseconds_t;
#endif

#endif /* ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_SYS_TYPES_H_ */
```

## 38.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2016 Intel Corporation。

版权（Copyright）：© 2017 ARM Ltd。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 19 行

静态代码分析工具可能对下一行报告违规，因为宏名 `unsigned` 与关键字相同。这是有意为之的偏离（Deliberated deviation）。

这里通过一种编译器技巧确保 `ssize_t` 的类型不会成为 `unsigned long`；否则 `ssize_t` 会成为该无符号类型，这是不正确的。更多细节见提交 `b889120`。

### 注释 3：原第 27 行

Parasoft 静态分析抑制指令：`parasoft-suppress MISRAC2012-RULE_20_4-a MISRAC2012-RULE_20_4-b`。

### 注释 4：原第 35 行

`off_t` 的定义使其大小与指针大小一致。

### 注释 5：原第 49 行

头文件保护宏（Header guard）标记：`ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_SYS_TYPES_H_`。

## 38.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [sys/_types.h](https://docs.zephyrproject.org/latest/doxygen/html/__types_8h.html)
- [mode_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#adb8322e115035a284aab704909e63d00)
- [ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)
- [suseconds_t](../time_headers_reference/P003_timespec类型头文件参考.md#ad7acf95ceafb15a1d8d86af0c4982995)
- [_types.h](https://docs.zephyrproject.org/latest/doxygen/html/__types_8h.html)

---

[上一章](P037_led_strip.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P039_limits.h_源码浏览.md)
