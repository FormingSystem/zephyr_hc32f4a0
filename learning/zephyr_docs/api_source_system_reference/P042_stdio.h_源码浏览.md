---
id: learning.zephyr-docs.api-source-system-reference.page-42
title: stdio.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stdio_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_stdio.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stdio_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P409_____w__zephyr__zephyr__lib__libc__minimal__include__stdio.h_文件参考.md)。

## 42.1\_原始可见代码（Source Code）

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
<a id="astdio_8h_html_a0cf1b75a23729bcc1669ce788d01aa63"></a>
<a id="astdio_8h_html_a1af16e2ea2a90f8b64983c9b3e644fad"></a>
<a id="astdio_8h_html_a32e4cef9beb0262cea4bdafb5b998276"></a>
<a id="astdio_8h_html_a610723ed7ffdf7b802f6093d45ffa09d"></a>
<a id="astdio_8h_html_a632165581e7417488441b703393668a4"></a>
<a id="astdio_8h_html_a6c67912b5a18e7d7ac03ca4e77425715"></a>
<a id="astdio_8h_html_a8524c494bbe2f2e686d35c3bd7ca4f2a"></a>
<a id="astdio_8h_html_aa6f061fe9cbedf135d97a91b0f7c0ca8"></a>
<a id="astdio_8h_html_ab39f9634fa53ffd52b87431f3afab11b"></a>
<a id="astdio_8h_html_ab6baefe2032389ec8daadad3492af3e0"></a>
<a id="astdio_8h_html_abc4556d2008bb7d9345dd8bef8ef65ee"></a>
<a id="astdio_8h_html_abe6299d5823dd023e610aaa619735a3f"></a>
<a id="astdio_8h_html_ac15bbd02a147d1595cdfb8b2979693d7"></a>
<a id="astdio_8h_html_ad41876f99f190c7488e64ef39c50a23f"></a>
<a id="astdio_8h_html_af097ff94eaf1896faa4664dd91858778"></a>
<a id="atoolchain_8h_html"></a>

```c
/* stdio.h */

/*
 * Copyright (c) 2014 Wind River Systems, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_STDIO_H_
#define ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_STDIO_H_

#include <zephyr/toolchain.h>
#include <stdarg.h>     /* Needed to get definition of va_list */
#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#if !defined(__FILE_defined)
#define __FILE_defined
typedef int  FILE;
#endif

#if !defined(EOF)
#define EOF  (-1)
#endif

#define stdin  ((FILE *) 1)
#define stdout ((FILE *) 2)
#define stderr ((FILE *) 3)

#define SEEK_SET        0       /* Seek from beginning of file.  */
#define SEEK_CUR        1       /* Seek from current position.  */
#define SEEK_END        2       /* Seek from end of file.  */

int __printf_like(1, 2) printf(const char *ZRESTRICT format, ...);
int __printf_like(3, 4) snprintf(char *ZRESTRICT str, size_t len,
                                 const char *ZRESTRICT format, ...);
int __printf_like(2, 3) sprintf(char *ZRESTRICT str,
                                const char *ZRESTRICT format, ...);
int __printf_like(2, 3) fprintf(FILE *ZRESTRICT stream,
                                const char *ZRESTRICT format, ...);


int __printf_like(1, 0) vprintf(const char *ZRESTRICT format, va_list list);
int __printf_like(3, 0) vsnprintf(char *ZRESTRICT str, size_t len,
                                  const char *ZRESTRICT format,
                                  va_list list);
int __printf_like(2, 0) vsprintf(char *ZRESTRICT str,
                                 const char *ZRESTRICT format, va_list list);
int __printf_like(2, 0) vfprintf(FILE *ZRESTRICT stream,
                                 const char *ZRESTRICT format,
                                 va_list ap);

void perror(const char *s);
int puts(const char *s);

int fputc(int c, FILE *stream);
int fputs(const char *ZRESTRICT s, FILE *ZRESTRICT stream);
size_t fwrite(const void *ZRESTRICT ptr, size_t size, size_t nitems,
              FILE *ZRESTRICT stream);
int remove(const char *path);
#define putc(c, stream) fputc(c, stream)
#define putchar(c) putc(c, stdout)

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_STDIO_H_ */
```

## 42.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

标准输入输出头文件（Standard I/O Header）：`stdio.h`。

### 注释 2：原第 3 行

版权（Copyright）：© 2014 Wind River Systems, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 3：原第 13 行

用于获取 `va_list` 的定义。

### 注释 4：原第 33 行

从文件开头（Beginning of File）进行定位（Seek）。

### 注释 5：原第 34 行

从当前位置（Current Position）进行定位（Seek）。

### 注释 6：原第 35 行

从文件末尾（End of File）进行定位（Seek）。

### 注释 7：原第 71 行

头文件保护宏（Header guard）标记：`ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_STDIO_H_`。

## 42.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P409_____w__zephyr__zephyr__lib__libc__minimal__include__stdio.h_文件参考.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [FILE](../api_file_reference/P409_____w__zephyr__zephyr__lib__libc__minimal__include__stdio.h_文件参考.md#ac15bbd02a147d1595cdfb8b2979693d7)
- [printf](../api_file_reference/P409_____w__zephyr__zephyr__lib__libc__minimal__include__stdio.h_文件参考.md#a6c67912b5a18e7d7ac03ca4e77425715)
- [snprintf](../api_file_reference/P409_____w__zephyr__zephyr__lib__libc__minimal__include__stdio.h_文件参考.md#a8524c494bbe2f2e686d35c3bd7ca4f2a)
- [sprintf](../api_file_reference/P409_____w__zephyr__zephyr__lib__libc__minimal__include__stdio.h_文件参考.md#aa6f061fe9cbedf135d97a91b0f7c0ca8)
- [fprintf](../api_file_reference/P409_____w__zephyr__zephyr__lib__libc__minimal__include__stdio.h_文件参考.md#af097ff94eaf1896faa4664dd91858778)
- [vprintf](../api_file_reference/P409_____w__zephyr__zephyr__lib__libc__minimal__include__stdio.h_文件参考.md#a1af16e2ea2a90f8b64983c9b3e644fad)
- [vsnprintf](../api_file_reference/P409_____w__zephyr__zephyr__lib__libc__minimal__include__stdio.h_文件参考.md#a632165581e7417488441b703393668a4)
- [vsprintf](../api_file_reference/P409_____w__zephyr__zephyr__lib__libc__minimal__include__stdio.h_文件参考.md#a0cf1b75a23729bcc1669ce788d01aa63)
- [vfprintf](../api_file_reference/P409_____w__zephyr__zephyr__lib__libc__minimal__include__stdio.h_文件参考.md#abc4556d2008bb7d9345dd8bef8ef65ee)
- [perror](../api_file_reference/P409_____w__zephyr__zephyr__lib__libc__minimal__include__stdio.h_文件参考.md#ab39f9634fa53ffd52b87431f3afab11b)
- [puts](../api_file_reference/P409_____w__zephyr__zephyr__lib__libc__minimal__include__stdio.h_文件参考.md#ad41876f99f190c7488e64ef39c50a23f)
- [fputc](../api_file_reference/P409_____w__zephyr__zephyr__lib__libc__minimal__include__stdio.h_文件参考.md#abe6299d5823dd023e610aaa619735a3f)
- [fputs](../api_file_reference/P409_____w__zephyr__zephyr__lib__libc__minimal__include__stdio.h_文件参考.md#ab6baefe2032389ec8daadad3492af3e0)
- [fwrite](../api_file_reference/P409_____w__zephyr__zephyr__lib__libc__minimal__include__stdio.h_文件参考.md#a610723ed7ffdf7b802f6093d45ffa09d)
- [remove](../api_file_reference/P409_____w__zephyr__zephyr__lib__libc__minimal__include__stdio.h_文件参考.md#a32e4cef9beb0262cea4bdafb5b998276)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P041_socketcan.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P043_stm32f10x_clock.h_源码浏览.md)
