---
id: learning.zephyr-docs.api-file-reference.page-381
title: zephyr__posix__semaphore.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/semaphore_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第381章\_zephyr\_\_posix\_\_semaphore.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/semaphore_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <time.h>
#include <zephyr/posix/posix_types.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 381.1\_宏定义（Macros）

<a id="r_a2ef55dcb46a51cb0f879f4c1724bdded"></a>

```c
#define SEM_FAILED ((sem_t *) 0)
```

相关声明：[SEM_FAILED](#a2ef55dcb46a51cb0f879f4c1724bdded)、[sem_t](P312_zephyr__posix__posix_types.h_文件参考.md#afb4edc6a51d66a7a352424942b631a1e)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 381.2\_函数（Functions）

<a id="r_a42cc945f89772ca24e87a569a5f2dbd7"></a>

```c
int sem_destroy (sem_t *semaphore)
```

相关声明：[sem_destroy](#a42cc945f89772ca24e87a569a5f2dbd7)、[sem_t](P312_zephyr__posix__posix_types.h_文件参考.md#afb4edc6a51d66a7a352424942b631a1e)。

<a id="r_af4d15a2fd215951eb7ea2424ffdd335e"></a>

```c
int sem_getvalue (sem_t *ZRESTRICT semaphore, int *ZRESTRICT value)
```

相关声明：[sem_getvalue](#af4d15a2fd215951eb7ea2424ffdd335e)、[sem_t](P312_zephyr__posix__posix_types.h_文件参考.md#afb4edc6a51d66a7a352424942b631a1e)。

<a id="r_a1fee59859601fb325fafb32ee41b5691"></a>

```c
int sem_init (sem_t *semaphore, int pshared, unsigned int value)
```

相关声明：[sem_init](#a1fee59859601fb325fafb32ee41b5691)、[sem_t](P312_zephyr__posix__posix_types.h_文件参考.md#afb4edc6a51d66a7a352424942b631a1e)、[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

<a id="r_a2bee748f81a960f80dfccf675f38e3d8"></a>

```c
int sem_post (sem_t *semaphore)
```

相关声明：[sem_post](#a2bee748f81a960f80dfccf675f38e3d8)、[sem_t](P312_zephyr__posix__posix_types.h_文件参考.md#afb4edc6a51d66a7a352424942b631a1e)。

<a id="r_a91a6510735a16f94defc52ecbb7971ac"></a>

```c
int sem_timedwait (sem_t *ZRESTRICT semaphore, struct timespec *ZRESTRICT abstime)
```

相关声明：[sem_timedwait](#a91a6510735a16f94defc52ecbb7971ac)、[sem_t](P312_zephyr__posix__posix_types.h_文件参考.md#afb4edc6a51d66a7a352424942b631a1e)、[timespec](../time_headers_reference/P005_timespec时间结构.md)。

<a id="r_a0f2fd32f79e2815f52f2afd2f5069960"></a>

```c
int sem_trywait (sem_t *semaphore)
```

相关声明：[sem_trywait](#a0f2fd32f79e2815f52f2afd2f5069960)、[sem_t](P312_zephyr__posix__posix_types.h_文件参考.md#afb4edc6a51d66a7a352424942b631a1e)。

<a id="r_a355d892eec64a2dc95143635469c6524"></a>

```c
int sem_wait (sem_t *semaphore)
```

相关声明：[sem_wait](#a355d892eec64a2dc95143635469c6524)、[sem_t](P312_zephyr__posix__posix_types.h_文件参考.md#afb4edc6a51d66a7a352424942b631a1e)。

<a id="r_a0ed06fc3db017281dc6f1eefff97053a"></a>

```c
sem_t * sem_open (const char *name, int oflags,...)
```

相关声明：[sem_t](P312_zephyr__posix__posix_types.h_文件参考.md#afb4edc6a51d66a7a352424942b631a1e)、[sem_open](#a0ed06fc3db017281dc6f1eefff97053a)。

<a id="r_a776256d1a473906f8b7490689bfcb75c"></a>

```c
int sem_unlink (const char *name)
```

相关声明：[sem_unlink](#a776256d1a473906f8b7490689bfcb75c)。

<a id="r_a4e398fea1080fd7919e5c72ee94e2fc5"></a>

```c
int sem_close (sem_t *sem)
```

相关声明：[sem_close](#a4e398fea1080fd7919e5c72ee94e2fc5)、[sem_t](P312_zephyr__posix__posix_types.h_文件参考.md#afb4edc6a51d66a7a352424942b631a1e)。

## 381.3\_详细说明（Detailed Documentation）

<a id="a2ef55dcb46a51cb0f879f4c1724bdded"></a>

### `SEM_FAILED`

```c
#define SEM_FAILED ((sem_t *) 0)
```

<a id="a4e398fea1080fd7919e5c72ee94e2fc5"></a>

### `sem_close()`

```c
int sem_close ( sem_t * sem)
```

<a id="a42cc945f89772ca24e87a569a5f2dbd7"></a>

### `sem_destroy()`

```c
int sem_destroy ( sem_t * semaphore)
```

<a id="af4d15a2fd215951eb7ea2424ffdd335e"></a>

### `sem_getvalue()`

```c
int sem_getvalue ( sem_t *ZRESTRICT semaphore, int *ZRESTRICT value )
```

<a id="a1fee59859601fb325fafb32ee41b5691"></a>

### `sem_init()`

```c
int sem_init ( sem_t * semaphore, int pshared, unsigned int value )
```

<a id="a0ed06fc3db017281dc6f1eefff97053a"></a>

### `sem_open()`

```c
sem_t * sem_open ( const char * name, int oflags, ... )
```

<a id="a2bee748f81a960f80dfccf675f38e3d8"></a>

### `sem_post()`

```c
int sem_post ( sem_t * semaphore)
```

<a id="a91a6510735a16f94defc52ecbb7971ac"></a>

### `sem_timedwait()`

```c
int sem_timedwait ( sem_t *ZRESTRICT semaphore, struct timespec *ZRESTRICT abstime )
```

<a id="a0f2fd32f79e2815f52f2afd2f5069960"></a>

### `sem_trywait()`

```c
int sem_trywait ( sem_t * semaphore)
```

<a id="a776256d1a473906f8b7490689bfcb75c"></a>

### `sem_unlink()`

```c
int sem_unlink ( const char * name)
```

<a id="a355d892eec64a2dc95143635469c6524"></a>

### `sem_wait()`

```c
int sem_wait ( sem_t * semaphore)
```


## 381.4\_原页交叉引用（Cross References）

- [zephyr/posix/posix_types.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P754_semaphore.h_源码浏览.md)
- [sem_t](P312_zephyr__posix__posix_types.h_文件参考.md#afb4edc6a51d66a7a352424942b631a1e)
- [unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [timespec](../time_headers_reference/P005_timespec时间结构.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P380_zephyr__posix__sys__select.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P382_zephyr__sensing__sensing_datatypes.h_文件参考.md)
