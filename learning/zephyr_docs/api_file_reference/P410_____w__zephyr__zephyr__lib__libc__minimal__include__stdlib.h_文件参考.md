---
id: learning.zephyr-docs.api-file-reference.page-410
title: ____w__zephyr__zephyr__lib__libc__minimal__include__stdlib.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第410章\_\_\_\_\_w\_\_zephyr\_\_zephyr\_\_lib\_\_libc\_\_minimal\_\_include\_\_stdlib.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stddef.h>
#include <limits.h>
#include <zephyr/toolchain.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 410.1\_宏定义（Macros）

<a id="r_a687984f47d8cce148d1b914d2b79612a"></a>

```c
#define EXIT_SUCCESS 0
```

相关声明：[EXIT_SUCCESS](#a687984f47d8cce148d1b914d2b79612a)。

<a id="r_a73efe787c131b385070f25d18b7c9aa4"></a>

```c
#define EXIT_FAILURE 1
```

相关声明：[EXIT_FAILURE](#a73efe787c131b385070f25d18b7c9aa4)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 410.2\_函数（Functions）

<a id="r_a6d257fc3f00865d0556ed7327c312b55"></a>

```c
unsigned long strtoul (const char *nptr, char **endptr, int base)
```

相关声明：[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[strtoul](#a6d257fc3f00865d0556ed7327c312b55)。

<a id="r_a311071298c2fe3e5d7057f396a6acfdc"></a>

```c
long strtol (const char *nptr, char **endptr, int base)
```

相关声明：[strtol](#a311071298c2fe3e5d7057f396a6acfdc)。

<a id="r_ae5835422eb2dfc17ea8deb3b15bcc541"></a>

```c
unsigned long long strtoull (const char *nptr, char **endptr, int base)
```

相关声明：[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[strtoull](#ae5835422eb2dfc17ea8deb3b15bcc541)。

<a id="r_afb901aa665b7e2e3e27025ca77fecd1b"></a>

```c
long long strtoll (const char *nptr, char **endptr, int base)
```

相关声明：[strtoll](#afb901aa665b7e2e3e27025ca77fecd1b)。

<a id="r_a30670a60464f77af17dfb353353d6df8"></a>

```c
int atoi (const char *s)
```

相关声明：[atoi](#a30670a60464f77af17dfb353353d6df8)。

<a id="r_a9c36d0fe3ec4675cbffdc9b52f5fb399"></a>

```c
void * malloc (size_t size)
```

相关声明：[malloc](#a9c36d0fe3ec4675cbffdc9b52f5fb399)。

<a id="r_a8006724372b77924155bd8618fe57516"></a>

```c
void * aligned_alloc (size_t alignment, size_t size)
```

相关声明：[aligned_alloc](#a8006724372b77924155bd8618fe57516)。

<a id="r_afbedc913aa4651b3c3b4b3aecd9b4711"></a>

```c
void free (void *ptr)
```

相关声明：[free](#afbedc913aa4651b3c3b4b3aecd9b4711)。

<a id="r_a2807e26a012717736641384f91ab2563"></a>

```c
void * calloc (size_t nmemb, size_t size)
```

相关声明：[calloc](#a2807e26a012717736641384f91ab2563)。

<a id="r_ad28fed1039f35d754710633141b4edf0"></a>

```c
void * realloc (void *ptr, size_t size)
```

相关声明：[realloc](#ad28fed1039f35d754710633141b4edf0)。

<a id="r_aa34babf7c7883ba6714ac6d010952465"></a>

```c
void * reallocarray (void *ptr, size_t nmemb, size_t size)
```

相关声明：[reallocarray](#aa34babf7c7883ba6714ac6d010952465)。

<a id="r_a5edc8d086d2525fdcd63486536cb4d9a"></a>

```c
void * bsearch (const void *key, const void *array, size_t count, size_t size, int(*cmp)(const void *key, const void *element))
```

相关声明：[bsearch](#a5edc8d086d2525fdcd63486536cb4d9a)。

<a id="r_ac47a43d4a9511216219413183ab689f2"></a>

```c
void qsort_r (void *base, size_t nmemb, size_t size, int(*compar)(const void *a, const void *b, void *arg), void *arg)
```

相关声明：[qsort_r](#ac47a43d4a9511216219413183ab689f2)。

<a id="r_ab92aa4266db30c870361edf7c7e050a2"></a>

```c
void qsort (void *base, size_t nmemb, size_t size, int(*compar)(const void *a, const void *b))
```

相关声明：[qsort](#ab92aa4266db30c870361edf7c7e050a2)。

<a id="r_ab924785decfca67fd65380b76a269206"></a>

```c
static FUNC_NORETURN void exit (int status)
```

相关声明：[exit](#ab924785decfca67fd65380b76a269206)。

<a id="r_a4bef6384a1777699c6eba3125e690419"></a>

```c
FUNC_NORETURN void abort (void)
```

相关声明：[abort](#a4bef6384a1777699c6eba3125e690419)。

<a id="r_ae0743c61576232ed6a443e6269af2b84"></a>

```c
static int abs (int __n)
```

相关声明：[abs](#ae0743c61576232ed6a443e6269af2b84)。

<a id="r_a8f842d6a8002a51ca6930a076ea86549"></a>

```c
static long labs (long __n)
```

相关声明：[labs](#a8f842d6a8002a51ca6930a076ea86549)。

<a id="r_a5613b9b7ce990f94ceaaf1f455cc98e6"></a>

```c
static long long llabs (long long __n)
```

相关声明：[llabs](#a5613b9b7ce990f94ceaaf1f455cc98e6)。

<a id="r_ab1ec8cf93b9478de49bb3e77465ab4af"></a>

```c
char * getenv (const char *name)
```

相关声明：[getenv](#ab1ec8cf93b9478de49bb3e77465ab4af)。

## 410.3\_详细说明（Detailed Documentation）

<a id="a73efe787c131b385070f25d18b7c9aa4"></a>

### `EXIT_FAILURE`

```c
#define EXIT_FAILURE 1
```

<a id="a687984f47d8cce148d1b914d2b79612a"></a>

### `EXIT_SUCCESS`

```c
#define EXIT_SUCCESS 0
```

<a id="a4bef6384a1777699c6eba3125e690419"></a>

### `abort()`

```c
FUNC_NORETURN void abort ( void )
```

<a id="ae0743c61576232ed6a443e6269af2b84"></a>

### `abs()`

```c
int abs ( int __n)
```

声明属性：`inline`、`static`。

<a id="a8006724372b77924155bd8618fe57516"></a>

### `aligned_alloc()`

```c
void * aligned_alloc ( size_t alignment, size_t size )
```

<a id="a30670a60464f77af17dfb353353d6df8"></a>

### `atoi()`

```c
int atoi ( const char * s)
```

<a id="a5edc8d086d2525fdcd63486536cb4d9a"></a>

### `bsearch()`

```c
void * bsearch ( const void * key, const void * array, size_t count, size_t size, int(* cmp )(const void *key, const void *element) )
```

<a id="a2807e26a012717736641384f91ab2563"></a>

### `calloc()`

```c
void * calloc ( size_t nmemb, size_t size )
```

<a id="ab924785decfca67fd65380b76a269206"></a>

### `exit()`

```c
FUNC_NORETURN void exit ( int status)
```

声明属性：`inline`、`static`。

<a id="afbedc913aa4651b3c3b4b3aecd9b4711"></a>

### `free()`

```c
void free ( void * ptr)
```

<a id="ab1ec8cf93b9478de49bb3e77465ab4af"></a>

### `getenv()`

```c
char * getenv ( const char * name)
```

<a id="a8f842d6a8002a51ca6930a076ea86549"></a>

### `labs()`

```c
long labs ( long __n)
```

声明属性：`inline`、`static`。

<a id="a5613b9b7ce990f94ceaaf1f455cc98e6"></a>

### `llabs()`

```c
long long llabs ( long long __n)
```

声明属性：`inline`、`static`。

<a id="a9c36d0fe3ec4675cbffdc9b52f5fb399"></a>

### `malloc()`

```c
void * malloc ( size_t size)
```

<a id="ab92aa4266db30c870361edf7c7e050a2"></a>

### `qsort()`

```c
void qsort ( void * base, size_t nmemb, size_t size, int(* compar )(const void *a, const void *b) )
```

<a id="ac47a43d4a9511216219413183ab689f2"></a>

### `qsort_r()`

```c
void qsort_r ( void * base, size_t nmemb, size_t size, int(* compar )(const void *a, const void *b, void *arg), void * arg )
```

<a id="ad28fed1039f35d754710633141b4edf0"></a>

### `realloc()`

```c
void * realloc ( void * ptr, size_t size )
```

<a id="aa34babf7c7883ba6714ac6d010952465"></a>

### `reallocarray()`

```c
void * reallocarray ( void * ptr, size_t nmemb, size_t size )
```

<a id="a311071298c2fe3e5d7057f396a6acfdc"></a>

### `strtol()`

```c
long strtol ( const char * nptr, char ** endptr, int base )
```

<a id="afb901aa665b7e2e3e27025ca77fecd1b"></a>

### `strtoll()`

```c
long long strtoll ( const char * nptr, char ** endptr, int base )
```

<a id="a6d257fc3f00865d0556ed7327c312b55"></a>

### `strtoul()`

```c
unsigned long strtoul ( const char * nptr, char ** endptr, int base )
```

<a id="ae5835422eb2dfc17ea8deb3b15bcc541"></a>

### `strtoull()`

```c
unsigned long long strtoull ( const char * nptr, char ** endptr, int base )
```


## 410.4\_原页交叉引用（Cross References）

- [limits.h](../api_source_runtime_reference/P039_limits.h_源码浏览.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h_source.html)
- [查看此文件的源码。](../api_source_configuration_reference/P107_stdlib.h_源码浏览.md)
- [unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P409_____w__zephyr__zephyr__lib__libc__minimal__include__stdio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P411_zephyr__dt-bindings__memory-controller__stm32-fmc-nor-psram.h_文件参考.md)
