---
id: learning.zephyr-docs.api-file-reference.page-187
title: ____w__zephyr__zephyr__lib__libc__minimal__include__time.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2time_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第187章\_\_\_\_\_w\_\_zephyr\_\_zephyr\_\_lib\_\_libc\_\_minimal\_\_include\_\_time.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2time_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
#include <zephyr/toolchain.h>
#include <sys/_types.h>
#include <sys/_timespec.h>
#include <zephyr/posix/posix_time.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 187.1\_数据结构（Data Structures）

<a id="r_tm"></a>

```c
struct tm
```

相关声明：[tm](../posix_system_model_reference/P025_tm_结构体.md)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 187.2\_函数（Functions）

<a id="r_a4bc4ff58d4ac838a36ba939747e5833e"></a>

```c
struct tm * gmtime (const time_t *timep)
```

相关声明：[tm](../posix_system_model_reference/P025_tm_结构体.md)、[gmtime](#a4bc4ff58d4ac838a36ba939747e5833e)、[time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)。

<a id="r_aee41f7a79e9f6ec34cdf7096fd597dbd"></a>

```c
struct tm * gmtime_r (const time_t *ZRESTRICT timep, struct tm *ZRESTRICT result)
```

相关声明：[tm](../posix_system_model_reference/P025_tm_结构体.md)、[gmtime_r](#aee41f7a79e9f6ec34cdf7096fd597dbd)、[time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)、[tm](../posix_system_model_reference/P025_tm_结构体.md)。

<a id="r_a068d11e0d50eab73920a3162d2ac9202"></a>

```c
char * asctime (const struct tm *timeptr)
```

相关声明：[asctime](#a068d11e0d50eab73920a3162d2ac9202)、[tm](../posix_system_model_reference/P025_tm_结构体.md)。

<a id="r_a47dad42d50a51f3ba4033320084c833b"></a>

```c
struct tm * localtime (const time_t *timer)
```

相关声明：[tm](../posix_system_model_reference/P025_tm_结构体.md)、[localtime](#a47dad42d50a51f3ba4033320084c833b)、[time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)。

<a id="r_a185521f2c273b9697eb1e536a37912fb"></a>

```c
char * ctime (const time_t *clock)
```

相关声明：[ctime](#a185521f2c273b9697eb1e536a37912fb)、[time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)。

<a id="r_a86ed062bf74f495209b11b650631e2f2"></a>

```c
char * asctime_r (const struct tm *ZRESTRICT tp, char *ZRESTRICT buf)
```

相关声明：[asctime_r](#a86ed062bf74f495209b11b650631e2f2)、[tm](../posix_system_model_reference/P025_tm_结构体.md)。

<a id="r_abb5334ac0f38a87278861e6edab616db"></a>

```c
char * ctime_r (const time_t *clock, char *buf)
```

相关声明：[ctime_r](#abb5334ac0f38a87278861e6edab616db)、[time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)。

<a id="r_a3d8015c8bf5fadc92389635bd977e880"></a>

```c
struct tm * localtime_r (const time_t *ZRESTRICT timer, struct tm *ZRESTRICT result)
```

相关声明：[tm](../posix_system_model_reference/P025_tm_结构体.md)、[localtime_r](#a3d8015c8bf5fadc92389635bd977e880)、[time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)、[tm](../posix_system_model_reference/P025_tm_结构体.md)。

<a id="r_a99ef1cb2c789827dd5db3886dccf9067"></a>

```c
time_t time (time_t *tloc)
```

相关声明：[time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)、[time](#a99ef1cb2c789827dd5db3886dccf9067)、[time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)。

## 187.3\_详细说明（Detailed Documentation）

<a id="a068d11e0d50eab73920a3162d2ac9202"></a>

### `asctime()`

```c
char * asctime ( const struct tm * timeptr)
```

<a id="a86ed062bf74f495209b11b650631e2f2"></a>

### `asctime_r()`

```c
char * asctime_r ( const struct tm *ZRESTRICT tp, char *ZRESTRICT buf )
```

<a id="a185521f2c273b9697eb1e536a37912fb"></a>

### `ctime()`

```c
char * ctime ( const time_t * clock)
```

<a id="abb5334ac0f38a87278861e6edab616db"></a>

### `ctime_r()`

```c
char * ctime_r ( const time_t * clock, char * buf )
```

<a id="a4bc4ff58d4ac838a36ba939747e5833e"></a>

### `gmtime()`

```c
struct tm * gmtime ( const time_t * timep)
```

<a id="aee41f7a79e9f6ec34cdf7096fd597dbd"></a>

### `gmtime_r()`

```c
struct tm * gmtime_r ( const time_t *ZRESTRICT timep, struct tm *ZRESTRICT result )
```

<a id="a47dad42d50a51f3ba4033320084c833b"></a>

### `localtime()`

```c
struct tm * localtime ( const time_t * timer)
```

<a id="a3d8015c8bf5fadc92389635bd977e880"></a>

### `localtime_r()`

```c
struct tm * localtime_r ( const time_t *ZRESTRICT timer, struct tm *ZRESTRICT result )
```

<a id="a99ef1cb2c789827dd5db3886dccf9067"></a>

### `time()`

```c
time_t time ( time_t * tloc)
```


## 187.4\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h_source.html)
- [sys/_types.h](../api_source_supplement_reference/P001__types.h_源码浏览.md)
- [sys/_timespec.h](../time_headers_reference/P004_timespec类型头文件源码.md)
- [zephyr/posix/posix_time.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__time_8h_source.html)
- [查看此文件的源码。](../api_source_configuration_reference/P048_time.h_源码浏览.md)
- [tm](../posix_system_model_reference/P025_tm_结构体.md)
- [time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P188_zephyr__sys__libc-hooks.h_文件参考.md)
