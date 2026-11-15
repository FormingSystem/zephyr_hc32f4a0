---
id: learning.zephyr-docs.api-source-configuration-reference.page-107
title: stdlib.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第107章\_stdlib.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html)。

## 107.1\_原始可见代码（Source Code）

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
<a id="foldopen00047"></a>
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
<a id="foldopen00060"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="foldopen00065"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="foldopen00070"></a>
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
<a id="alimits_8h_html"></a>
<a id="astdlib_8h_html_a2807e26a012717736641384f91ab2563"></a>
<a id="astdlib_8h_html_a30670a60464f77af17dfb353353d6df8"></a>
<a id="astdlib_8h_html_a311071298c2fe3e5d7057f396a6acfdc"></a>
<a id="astdlib_8h_html_a4bef6384a1777699c6eba3125e690419"></a>
<a id="astdlib_8h_html_a5613b9b7ce990f94ceaaf1f455cc98e6"></a>
<a id="astdlib_8h_html_a5edc8d086d2525fdcd63486536cb4d9a"></a>
<a id="astdlib_8h_html_a6d257fc3f00865d0556ed7327c312b55"></a>
<a id="astdlib_8h_html_a8006724372b77924155bd8618fe57516"></a>
<a id="astdlib_8h_html_a8f842d6a8002a51ca6930a076ea86549"></a>
<a id="astdlib_8h_html_a9c36d0fe3ec4675cbffdc9b52f5fb399"></a>
<a id="astdlib_8h_html_aa34babf7c7883ba6714ac6d010952465"></a>
<a id="astdlib_8h_html_ab1ec8cf93b9478de49bb3e77465ab4af"></a>
<a id="astdlib_8h_html_ab924785decfca67fd65380b76a269206"></a>
<a id="astdlib_8h_html_ab92aa4266db30c870361edf7c7e050a2"></a>
<a id="astdlib_8h_html_ac47a43d4a9511216219413183ab689f2"></a>
<a id="astdlib_8h_html_ad28fed1039f35d754710633141b4edf0"></a>
<a id="astdlib_8h_html_ae0743c61576232ed6a443e6269af2b84"></a>
<a id="astdlib_8h_html_ae5835422eb2dfc17ea8deb3b15bcc541"></a>
<a id="astdlib_8h_html_afb901aa665b7e2e3e27025ca77fecd1b"></a>
<a id="astdlib_8h_html_afbedc913aa4651b3c3b4b3aecd9b4711"></a>
<a id="atoolchain_8h_html"></a>

```c
/* stdlib.h */

/*
 * Copyright (c) 2011-2014 Wind River Systems, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_STDLIB_H_
#define ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_STDLIB_H_

#include <stddef.h>
#include <limits.h>

#include <zephyr/toolchain.h>

#ifdef __cplusplus
extern "C" {
#endif

unsigned long strtoul(const char *nptr, char **endptr, int base);
long strtol(const char *nptr, char **endptr, int base);
unsigned long long strtoull(const char *nptr, char **endptr, int base);
long long strtoll(const char *nptr, char **endptr, int base);
int atoi(const char *s);

void *malloc(size_t size);
void *aligned_alloc(size_t alignment, size_t size); /* From C11 */

void free(void *ptr);
void *calloc(size_t nmemb, size_t size);
void *realloc(void *ptr, size_t size);
void *reallocarray(void *ptr, size_t nmemb, size_t size);

void *bsearch(const void *key, const void *array,
              size_t count, size_t size,
              int (*cmp)(const void *key, const void *element));

void qsort_r(void *base, size_t nmemb, size_t size,
             int (*compar)(const void *a, const void *b, void *arg), void *arg);
void qsort(void *base, size_t nmemb, size_t size,
           int (*compar)(const void *a, const void *b));

#define EXIT_SUCCESS 0
#define EXIT_FAILURE 1
FUNC_NORETURN void _exit(int status);
FUNC_NORETURN static inline void exit(int status)
{
        _exit(status);
}
FUNC_NORETURN void abort(void);

#ifdef CONFIG_MINIMAL_LIBC_RAND
#define RAND_MAX INT_MAX
int rand_r(unsigned int *seed);
int rand(void);
void srand(unsigned int seed);
#endif /* CONFIG_MINIMAL_LIBC_RAND */

static inline int abs(int __n)
{
        return (__n < 0) ? -__n : __n;
}

static inline long labs(long __n)
{
        return (__n < 0L) ? -__n : __n;
}

static inline long long llabs(long long __n)
{
        return (__n < 0LL) ? -__n : __n;
}

char *getenv(const char *name);
#if _POSIX_C_SOURCE >= 200112L
int setenv(const char *name, const char *val, int overwrite);
int unsetenv(const char *name);
#endif

#ifdef _BSD_SOURCE
int getenv_r(const char *name, char *buf, size_t len);
#endif

#ifdef __cplusplus
}
#endif

#endif  /* ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_STDLIB_H_ */
```

## 107.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

`stdlib.h` 头文件。

### 注释 2：原第 3 行

版权（Copyright）：© 2011-2014 Wind River Systems, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 3：原第 28 行

来自 C11。

### 注释 4：原第 58 行

条件编译配置（Configuration）标记：`CONFIG_MINIMAL_LIBC_RAND`。

### 注释 5：原第 89 行

头文件保护宏（Header guard）标记：`ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_STDLIB_H_`。

## 107.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html)
- [limits.h](https://docs.zephyrproject.org/latest/doxygen/html/limits_8h.html)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [strtoul](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html#a6d257fc3f00865d0556ed7327c312b55)
- [strtol](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html#a311071298c2fe3e5d7057f396a6acfdc)
- [strtoull](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html#ae5835422eb2dfc17ea8deb3b15bcc541)
- [strtoll](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html#afb901aa665b7e2e3e27025ca77fecd1b)
- [atoi](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html#a30670a60464f77af17dfb353353d6df8)
- [malloc](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html#a9c36d0fe3ec4675cbffdc9b52f5fb399)
- [aligned_alloc](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html#a8006724372b77924155bd8618fe57516)
- [free](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html#afbedc913aa4651b3c3b4b3aecd9b4711)
- [calloc](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html#a2807e26a012717736641384f91ab2563)
- [realloc](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html#ad28fed1039f35d754710633141b4edf0)
- [reallocarray](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html#aa34babf7c7883ba6714ac6d010952465)
- [bsearch](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html#a5edc8d086d2525fdcd63486536cb4d9a)
- [qsort_r](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html#ac47a43d4a9511216219413183ab689f2)
- [qsort](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html#ab92aa4266db30c870361edf7c7e050a2)
- [exit](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html#ab924785decfca67fd65380b76a269206)
- [abort](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html#a4bef6384a1777699c6eba3125e690419)
- [abs](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html#ae0743c61576232ed6a443e6269af2b84)
- [labs](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html#a8f842d6a8002a51ca6930a076ea86549)
- [llabs](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html#a5613b9b7ce990f94ceaaf1f455cc98e6)
- [getenv](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html#ab1ec8cf93b9478de49bb3e77465ab4af)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P106_stats.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P108_stm32f1-afio.h_源码浏览.md)
