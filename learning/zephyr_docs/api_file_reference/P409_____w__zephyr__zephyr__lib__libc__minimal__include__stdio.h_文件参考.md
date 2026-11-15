---
id: learning.zephyr-docs.api-file-reference.page-409
title: ____w__zephyr__zephyr__lib__libc__minimal__include__stdio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stdio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第409章\_\_\_\_\_w\_\_zephyr\_\_zephyr\_\_lib\_\_libc\_\_minimal\_\_include\_\_stdio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stdio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/toolchain.h>
#include <stdarg.h>
#include <stddef.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 409.1\_宏定义（Macros）

<a id="r_a59adc4c82490d23754cd39c2fb99b0da"></a>

```c
#define EOF (-1)
```

相关声明：[EOF](#a59adc4c82490d23754cd39c2fb99b0da)。

<a id="r_aaca70138f0cb63ddb026921afc635179"></a>

```c
#define stdin ((FILE *) 1)
```

相关声明：[stdin](#aaca70138f0cb63ddb026921afc635179)、[FILE](#ac15bbd02a147d1595cdfb8b2979693d7)。

<a id="r_a0c0ef221f95f64e8632451312fd18cc8"></a>

```c
#define stdout ((FILE *) 2)
```

相关声明：[stdout](#a0c0ef221f95f64e8632451312fd18cc8)、[FILE](#ac15bbd02a147d1595cdfb8b2979693d7)。

<a id="r_a5ce35bd5ba5021fd3b2e951e8f497656"></a>

```c
#define stderr ((FILE *) 3)
```

相关声明：[stderr](#a5ce35bd5ba5021fd3b2e951e8f497656)、[FILE](#ac15bbd02a147d1595cdfb8b2979693d7)。

<a id="r_a0d112bae8fd35be772185b6ec6bcbe64"></a>

```c
#define SEEK_SET 0 /* Seek from beginning of file. */
```

相关声明：[SEEK_SET](#a0d112bae8fd35be772185b6ec6bcbe64)。

<a id="r_a4c8d0b76b470ba65a43ca46a88320f39"></a>

```c
#define SEEK_CUR 1 /* Seek from current position. */
```

相关声明：[SEEK_CUR](#a4c8d0b76b470ba65a43ca46a88320f39)。

<a id="r_ad2a2e6c114780c3071efd24f16c7f7d8"></a>

```c
#define SEEK_END 2 /* Seek from end of file. */
```

相关声明：[SEEK_END](#ad2a2e6c114780c3071efd24f16c7f7d8)。

<a id="r_a0b8e699e4dfd158acee3d6526fe671c2"></a>

```c
#define putc(c, stream)
```

相关声明：[putc](#a0b8e699e4dfd158acee3d6526fe671c2)。

<a id="r_a568f021a83b2c22e1e700d12559d660a"></a>

```c
#define putchar(c)
```

相关声明：[putchar](#a568f021a83b2c22e1e700d12559d660a)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 409.2\_类型定义（Typedefs）

<a id="r_ac15bbd02a147d1595cdfb8b2979693d7"></a>

```c
typedef int FILE
```

相关声明：[FILE](#ac15bbd02a147d1595cdfb8b2979693d7)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 409.3\_函数（Functions）

<a id="r_a6c67912b5a18e7d7ac03ca4e77425715"></a>

```c
int printf (const char *ZRESTRICT format,...)
```

相关声明：[printf](#a6c67912b5a18e7d7ac03ca4e77425715)。

<a id="r_a8524c494bbe2f2e686d35c3bd7ca4f2a"></a>

```c
int snprintf (char *ZRESTRICT str, size_t len, const char *ZRESTRICT format,...)
```

相关声明：[snprintf](#a8524c494bbe2f2e686d35c3bd7ca4f2a)。

<a id="r_aa6f061fe9cbedf135d97a91b0f7c0ca8"></a>

```c
int sprintf (char *ZRESTRICT str, const char *ZRESTRICT format,...)
```

相关声明：[sprintf](#aa6f061fe9cbedf135d97a91b0f7c0ca8)。

<a id="r_af097ff94eaf1896faa4664dd91858778"></a>

```c
int fprintf (FILE *ZRESTRICT stream, const char *ZRESTRICT format,...)
```

相关声明：[fprintf](#af097ff94eaf1896faa4664dd91858778)、[FILE](#ac15bbd02a147d1595cdfb8b2979693d7)。

<a id="r_a1af16e2ea2a90f8b64983c9b3e644fad"></a>

```c
int vprintf (const char *ZRESTRICT format, va_list list)
```

相关声明：[vprintf](#a1af16e2ea2a90f8b64983c9b3e644fad)。

<a id="r_a632165581e7417488441b703393668a4"></a>

```c
int vsnprintf (char *ZRESTRICT str, size_t len, const char *ZRESTRICT format, va_list list)
```

相关声明：[vsnprintf](#a632165581e7417488441b703393668a4)。

<a id="r_a0cf1b75a23729bcc1669ce788d01aa63"></a>

```c
int vsprintf (char *ZRESTRICT str, const char *ZRESTRICT format, va_list list)
```

相关声明：[vsprintf](#a0cf1b75a23729bcc1669ce788d01aa63)。

<a id="r_abc4556d2008bb7d9345dd8bef8ef65ee"></a>

```c
int vfprintf (FILE *ZRESTRICT stream, const char *ZRESTRICT format, va_list ap)
```

相关声明：[vfprintf](#abc4556d2008bb7d9345dd8bef8ef65ee)、[FILE](#ac15bbd02a147d1595cdfb8b2979693d7)。

<a id="r_ab39f9634fa53ffd52b87431f3afab11b"></a>

```c
void perror (const char *s)
```

相关声明：[perror](#ab39f9634fa53ffd52b87431f3afab11b)。

<a id="r_ad41876f99f190c7488e64ef39c50a23f"></a>

```c
int puts (const char *s)
```

相关声明：[puts](#ad41876f99f190c7488e64ef39c50a23f)。

<a id="r_abe6299d5823dd023e610aaa619735a3f"></a>

```c
int fputc (int c, FILE *stream)
```

相关声明：[fputc](#abe6299d5823dd023e610aaa619735a3f)、[FILE](#ac15bbd02a147d1595cdfb8b2979693d7)。

<a id="r_ab6baefe2032389ec8daadad3492af3e0"></a>

```c
int fputs (const char *ZRESTRICT s, FILE *ZRESTRICT stream)
```

相关声明：[fputs](#ab6baefe2032389ec8daadad3492af3e0)、[FILE](#ac15bbd02a147d1595cdfb8b2979693d7)。

<a id="r_a610723ed7ffdf7b802f6093d45ffa09d"></a>

```c
size_t fwrite (const void *ZRESTRICT ptr, size_t size, size_t nitems, FILE *ZRESTRICT stream)
```

相关声明：[fwrite](#a610723ed7ffdf7b802f6093d45ffa09d)、[FILE](#ac15bbd02a147d1595cdfb8b2979693d7)。

<a id="r_a32e4cef9beb0262cea4bdafb5b998276"></a>

```c
int remove (const char *path)
```

相关声明：[remove](#a32e4cef9beb0262cea4bdafb5b998276)。

## 409.4\_详细说明（Detailed Documentation）

<a id="a59adc4c82490d23754cd39c2fb99b0da"></a>

### `EOF`

```c
#define EOF (-1)
```

<a id="a0b8e699e4dfd158acee3d6526fe671c2"></a>

### `putc`

```c
#define putc ( c, stream )
```

展开值（Value）：

```c
fputc(c, stream)
```

<a id="a568f021a83b2c22e1e700d12559d660a"></a>

### `putchar`

```c
#define putchar ( c)
```

展开值（Value）：

```c
putc(c, stdout)
```

<a id="a4c8d0b76b470ba65a43ca46a88320f39"></a>

### `SEEK_CUR`

```c
#define SEEK_CUR 1 /* Seek from current position. */
```

<a id="ad2a2e6c114780c3071efd24f16c7f7d8"></a>

### `SEEK_END`

```c
#define SEEK_END 2 /* Seek from end of file. */
```

<a id="a0d112bae8fd35be772185b6ec6bcbe64"></a>

### `SEEK_SET`

```c
#define SEEK_SET 0 /* Seek from beginning of file. */
```

<a id="a5ce35bd5ba5021fd3b2e951e8f497656"></a>

### `stderr`

```c
#define stderr ((FILE *) 3)
```

<a id="aaca70138f0cb63ddb026921afc635179"></a>

### `stdin`

```c
#define stdin ((FILE *) 1)
```

<a id="a0c0ef221f95f64e8632451312fd18cc8"></a>

### `stdout`

```c
#define stdout ((FILE *) 2)
```

<a id="ac15bbd02a147d1595cdfb8b2979693d7"></a>

### `FILE`

```c
typedef int FILE
```

<a id="af097ff94eaf1896faa4664dd91858778"></a>

### `fprintf()`

```c
int fprintf ( FILE *ZRESTRICT stream, const char *ZRESTRICT format, ... )
```

<a id="abe6299d5823dd023e610aaa619735a3f"></a>

### `fputc()`

```c
int fputc ( int c, FILE * stream )
```

<a id="ab6baefe2032389ec8daadad3492af3e0"></a>

### `fputs()`

```c
int fputs ( const char *ZRESTRICT s, FILE *ZRESTRICT stream )
```

<a id="a610723ed7ffdf7b802f6093d45ffa09d"></a>

### `fwrite()`

```c
size_t fwrite ( const void *ZRESTRICT ptr, size_t size, size_t nitems, FILE *ZRESTRICT stream )
```

<a id="ab39f9634fa53ffd52b87431f3afab11b"></a>

### `perror()`

```c
void perror ( const char * s)
```

<a id="a6c67912b5a18e7d7ac03ca4e77425715"></a>

### `printf()`

```c
int printf ( const char *ZRESTRICT format, ... )
```

<a id="ad41876f99f190c7488e64ef39c50a23f"></a>

### `puts()`

```c
int puts ( const char * s)
```

<a id="a32e4cef9beb0262cea4bdafb5b998276"></a>

### `remove()`

```c
int remove ( const char * path)
```

<a id="a8524c494bbe2f2e686d35c3bd7ca4f2a"></a>

### `snprintf()`

```c
int snprintf ( char *ZRESTRICT str, size_t len, const char *ZRESTRICT format, ... )
```

<a id="aa6f061fe9cbedf135d97a91b0f7c0ca8"></a>

### `sprintf()`

```c
int sprintf ( char *ZRESTRICT str, const char *ZRESTRICT format, ... )
```

<a id="abc4556d2008bb7d9345dd8bef8ef65ee"></a>

### `vfprintf()`

```c
int vfprintf ( FILE *ZRESTRICT stream, const char *ZRESTRICT format, va_list ap )
```

<a id="a1af16e2ea2a90f8b64983c9b3e644fad"></a>

### `vprintf()`

```c
int vprintf ( const char *ZRESTRICT format, va_list list )
```

<a id="a632165581e7417488441b703393668a4"></a>

### `vsnprintf()`

```c
int vsnprintf ( char *ZRESTRICT str, size_t len, const char *ZRESTRICT format, va_list list )
```

<a id="a0cf1b75a23729bcc1669ce788d01aa63"></a>

### `vsprintf()`

```c
int vsprintf ( char *ZRESTRICT str, const char *ZRESTRICT format, va_list list )
```


## 409.5\_原页交叉引用（Cross References）

- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h_source.html)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/stdio_8h_source.html)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astdio_8h_html_abe6299d5823dd023e610aaa619735a3f"></a>
<a id="astdio_8h_html_a0b8e699e4dfd158acee3d6526fe671c2"></a>
<a id="astdio_8h_html_a0c0ef221f95f64e8632451312fd18cc8"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P410_____w__zephyr__zephyr__lib__libc__minimal__include__stdlib.h_文件参考.md)
