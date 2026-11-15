---
id: learning.zephyr-docs.api-file-reference.page-311
title: zephyr__posix__posix_time.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/posix__time_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第311章\_zephyr\_\_posix\_\_posix\_time.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/posix__time_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stddef.h>
#include <zephyr/sys/clock.h>
#include <zephyr/toolchain.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 311.1\_数据结构（Data Structures）

<a id="r_timespec"></a>

```c
struct timespec
```

相关声明：[timespec](../time_headers_reference/P005_timespec时间结构.md)。

<a id="r_itimerspec"></a>

```c
struct itimerspec
```

相关声明：[itimerspec](../time_headers_reference/P012_定时器时间规格结构.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 311.2\_宏定义（Macros）

<a id="r_a922ce1ae64374c9410c8a999e25e82af"></a>

```c
#define CLOCK_REALTIME ((clockid_t)SYS_CLOCK_REALTIME)
```

相关声明：[CLOCK_REALTIME](#a922ce1ae64374c9410c8a999e25e82af)、[clockid_t](#a6bb3206700910111f26e946bfbf0f2af)、[SYS_CLOCK_REALTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gac88ce6c820c962691fdc6e0b344bd887)。

<a id="r_a3d9fc3c745d0880902fe3ea3d5d5f71e"></a>

```c
#define CLOCKS_PER_SEC CONFIG_SYS_CLOCK_TICKS_PER_SEC
```

相关声明：[CLOCKS_PER_SEC](#a3d9fc3c745d0880902fe3ea3d5d5f71e)。

<a id="r_ae1c3939a1e7b7cd1e5a4a7fa601cc4e9"></a>

```c
#define CLOCK_PROCESS_CPUTIME_ID ((clockid_t)2)
```

相关声明：[CLOCK_PROCESS_CPUTIME_ID](#ae1c3939a1e7b7cd1e5a4a7fa601cc4e9)、[clockid_t](#a6bb3206700910111f26e946bfbf0f2af)。

<a id="r_a30114e19c18f57f83727bcaba2458f1e"></a>

```c
#define CLOCK_THREAD_CPUTIME_ID ((clockid_t)3)
```

相关声明：[CLOCK_THREAD_CPUTIME_ID](#a30114e19c18f57f83727bcaba2458f1e)、[clockid_t](#a6bb3206700910111f26e946bfbf0f2af)。

<a id="r_a6fb83f5e91e704391ff796553d5e0f46"></a>

```c
#define CLOCK_MONOTONIC ((clockid_t)SYS_CLOCK_MONOTONIC)
```

相关声明：[CLOCK_MONOTONIC](#a6fb83f5e91e704391ff796553d5e0f46)、[clockid_t](#a6bb3206700910111f26e946bfbf0f2af)、[SYS_CLOCK_MONOTONIC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gab8a1a7e619c67e9a86e773097ce3a8e5)。

<a id="r_adde83d9ea51f12d4149f016eededde54"></a>

```c
#define TIMER_ABSTIME SYS_TIMER_ABSTIME
```

相关声明：[TIMER_ABSTIME](#adde83d9ea51f12d4149f016eededde54)、[SYS_TIMER_ABSTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga647bea5f74dcf7f6f6fed2c1b78b540f)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 311.3\_类型定义（Typedefs）

<a id="r_a6bb3206700910111f26e946bfbf0f2af"></a>

```c
typedef unsigned long clockid_t
```

相关声明：[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[clockid_t](#a6bb3206700910111f26e946bfbf0f2af)。

<a id="r_aa37fa84abebf94371f0c8426c2fc614d"></a>

```c
typedef unsigned long timer_t
```

相关声明：[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[timer_t](#aa37fa84abebf94371f0c8426c2fc614d)。

<a id="r_aa1f5af873d05619cbcf7901e194b292c"></a>

```c
typedef void * locale_t
```

相关声明：[locale_t](#aa1f5af873d05619cbcf7901e194b292c)。

<a id="r_a288e13e815d43b06e75819f8939524df"></a>

```c
typedef int pid_t
```

相关声明：[pid_t](#a288e13e815d43b06e75819f8939524df)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 311.4\_函数（Functions）

<a id="r_a068e8016542eb374e3c6b301b4babad6"></a>

```c
char * asctime_r (const struct tm *ZRESTRICT tm, char *ZRESTRICT buf)
```

相关声明：[asctime_r](#a068e8016542eb374e3c6b301b4babad6)、[tm](../posix_system_model_reference/P025_tm_结构体.md)、[tm](../posix_system_model_reference/P025_tm_结构体.md)。

<a id="r_ab2cd29aa41b2b485b571f05ac22d9f7f"></a>

```c
int clock_getcpuclockid (pid_t pid, clockid_t *clock_id)
```

相关声明：[clock_getcpuclockid](#ab2cd29aa41b2b485b571f05ac22d9f7f)、[pid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a114f9c2461df851d2ad00aad8dcfa3f7)、[clockid_t](#a6bb3206700910111f26e946bfbf0f2af)。

<a id="r_a3e1d049d0ed1519b99570efc4d8a1ae3"></a>

```c
int clock_getres (clockid_t clock_id, struct timespec *ts)
```

相关声明：[clock_getres](#a3e1d049d0ed1519b99570efc4d8a1ae3)、[clockid_t](#a6bb3206700910111f26e946bfbf0f2af)、[timespec](../time_headers_reference/P005_timespec时间结构.md)。

<a id="r_a21188eaca1b3e48ac3f7715398a1fc06"></a>

```c
int clock_gettime (clockid_t clock_id, struct timespec *ts)
```

相关声明：[clock_gettime](#a21188eaca1b3e48ac3f7715398a1fc06)、[clockid_t](#a6bb3206700910111f26e946bfbf0f2af)、[timespec](../time_headers_reference/P005_timespec时间结构.md)。

<a id="r_a924d51d78cdcd9d7dee2613fb3a33cd1"></a>

```c
int clock_nanosleep (clockid_t clock_id, int flags, const struct timespec *rqtp, struct timespec *rmtp)
```

相关声明：[clock_nanosleep](#a924d51d78cdcd9d7dee2613fb3a33cd1)、[clockid_t](#a6bb3206700910111f26e946bfbf0f2af)、[flags](P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[timespec](../time_headers_reference/P005_timespec时间结构.md)、[timespec](../time_headers_reference/P005_timespec时间结构.md)。

<a id="r_adab8a7307d547eb2b882dd1cda3a7655"></a>

```c
int clock_settime (clockid_t clock_id, const struct timespec *ts)
```

相关声明：[clock_settime](#adab8a7307d547eb2b882dd1cda3a7655)、[clockid_t](#a6bb3206700910111f26e946bfbf0f2af)、[timespec](../time_headers_reference/P005_timespec时间结构.md)。

<a id="r_abb5334ac0f38a87278861e6edab616db"></a>

```c
char * ctime_r (const time_t *clock, char *buf)
```

相关声明：[ctime_r](#abb5334ac0f38a87278861e6edab616db)、[time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)。

<a id="r_abd85b316719134b87f9b60e8abe5af76"></a>

```c
struct tm * getdate (const char *string)
```

相关声明：[tm](../posix_system_model_reference/P025_tm_结构体.md)、[getdate](#abd85b316719134b87f9b60e8abe5af76)。

<a id="r_adbf513dac252b14f87719a4a8b6913e7"></a>

```c
struct tm * gmtime_r (const time_t *ZRESTRICT timer, struct tm *ZRESTRICT result)
```

相关声明：[tm](../posix_system_model_reference/P025_tm_结构体.md)、[gmtime_r](#adbf513dac252b14f87719a4a8b6913e7)、[time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)、[tm](../posix_system_model_reference/P025_tm_结构体.md)。

<a id="r_a3d8015c8bf5fadc92389635bd977e880"></a>

```c
struct tm * localtime_r (const time_t *ZRESTRICT timer, struct tm *ZRESTRICT result)
```

相关声明：[tm](../posix_system_model_reference/P025_tm_结构体.md)、[localtime_r](#a3d8015c8bf5fadc92389635bd977e880)、[time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)、[tm](../posix_system_model_reference/P025_tm_结构体.md)。

<a id="r_a9ce6a1ed91a601dee133c8b6cf8b721a"></a>

```c
int nanosleep (const struct timespec *rqtp, struct timespec *rmtp)
```

相关声明：[nanosleep](#a9ce6a1ed91a601dee133c8b6cf8b721a)、[timespec](../time_headers_reference/P005_timespec时间结构.md)、[timespec](../time_headers_reference/P005_timespec时间结构.md)。

<a id="r_a4f7ca787fc0b633679bc337c4fcd8688"></a>

```c
size_t strftime_l (char *ZRESTRICT s, size_t maxsize, const char *ZRESTRICT format, const struct tm *ZRESTRICT timeptr, locale_t locale)
```

相关声明：[strftime_l](#a4f7ca787fc0b633679bc337c4fcd8688)、[tm](../posix_system_model_reference/P025_tm_结构体.md)、[locale_t](#aa1f5af873d05619cbcf7901e194b292c)。

<a id="r_a5a2f2994bcb293fc783a3109f2c76362"></a>

```c
char * strptime (const char *ZRESTRICT s, const char *ZRESTRICT format, struct tm *ZRESTRICT tm)
```

相关声明：[strptime](#a5a2f2994bcb293fc783a3109f2c76362)、[tm](../posix_system_model_reference/P025_tm_结构体.md)、[tm](../posix_system_model_reference/P025_tm_结构体.md)。

<a id="r_a5d4a389821dbcc362e93e8ecb895344e"></a>

```c
int timer_create (clockid_t clockId, struct sigevent *ZRESTRICT evp, timer_t *ZRESTRICT timerid)
```

相关声明：[timer_create](#a5d4a389821dbcc362e93e8ecb895344e)、[clockid_t](#a6bb3206700910111f26e946bfbf0f2af)、[sigevent](../posix_system_model_reference/P018_sigevent_结构体.md)、[timer_t](#aa37fa84abebf94371f0c8426c2fc614d)。

<a id="r_ad114bb350d7d5d12cff3fd19bf533303"></a>

```c
int timer_delete (timer_t timerid)
```

相关声明：[timer_delete](#ad114bb350d7d5d12cff3fd19bf533303)、[timer_t](#aa37fa84abebf94371f0c8426c2fc614d)。

<a id="r_ad779f0bc22f64bd3bd977221b0ce1b8f"></a>

```c
int timer_getoverrun (timer_t timerid)
```

相关声明：[timer_getoverrun](#ad779f0bc22f64bd3bd977221b0ce1b8f)、[timer_t](#aa37fa84abebf94371f0c8426c2fc614d)。

<a id="r_a06dda57adfdeb4a9b346f69c95cba96a"></a>

```c
int timer_gettime (timer_t timerid, struct itimerspec *its)
```

相关声明：[timer_gettime](#a06dda57adfdeb4a9b346f69c95cba96a)、[timer_t](#aa37fa84abebf94371f0c8426c2fc614d)、[itimerspec](../time_headers_reference/P012_定时器时间规格结构.md)。

<a id="r_a32207b51f2effa8441f4c728fd8519c0"></a>

```c
int timer_settime (timer_t timerid, int flags, const struct itimerspec *value, struct itimerspec *ovalue)
```

相关声明：[timer_settime](#a32207b51f2effa8441f4c728fd8519c0)、[timer_t](#aa37fa84abebf94371f0c8426c2fc614d)、[flags](P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[itimerspec](../time_headers_reference/P012_定时器时间规格结构.md)、[itimerspec](../time_headers_reference/P012_定时器时间规格结构.md)。

<a id="header-var-members"></a>
<a id="var-members"></a>

## 311.5\_变量（Variables）

<a id="r_a88051271ca3c003f7c7595fbbd214ea3"></a>

```c
int daylight
```

相关声明：[daylight](#a88051271ca3c003f7c7595fbbd214ea3)。

<a id="r_a3e348024a4a098ce0b8b51edba679a16"></a>

```c
long timezone
```

相关声明：[timezone](#a3e348024a4a098ce0b8b51edba679a16)。

<a id="r_a19e896f49dbb87c8b21378bf8b316b39"></a>

```c
char * tzname []
```

相关声明：[tzname](#a19e896f49dbb87c8b21378bf8b316b39)。

## 311.6\_详细说明（Detailed Documentation）

<a id="a6fb83f5e91e704391ff796553d5e0f46"></a>

### `CLOCK_MONOTONIC`

```c
#define CLOCK_MONOTONIC ((clockid_t)SYS_CLOCK_MONOTONIC)
```

<a id="ae1c3939a1e7b7cd1e5a4a7fa601cc4e9"></a>

### `CLOCK_PROCESS_CPUTIME_ID`

```c
#define CLOCK_PROCESS_CPUTIME_ID ((clockid_t)2)
```

<a id="a922ce1ae64374c9410c8a999e25e82af"></a>

### `CLOCK_REALTIME`

```c
#define CLOCK_REALTIME ((clockid_t)SYS_CLOCK_REALTIME)
```

<a id="a30114e19c18f57f83727bcaba2458f1e"></a>

### `CLOCK_THREAD_CPUTIME_ID`

```c
#define CLOCK_THREAD_CPUTIME_ID ((clockid_t)3)
```

<a id="a3d9fc3c745d0880902fe3ea3d5d5f71e"></a>

### `CLOCKS_PER_SEC`

```c
#define CLOCKS_PER_SEC CONFIG_SYS_CLOCK_TICKS_PER_SEC
```

<a id="adde83d9ea51f12d4149f016eededde54"></a>

### `TIMER_ABSTIME`

```c
#define TIMER_ABSTIME SYS_TIMER_ABSTIME
```

<a id="a6bb3206700910111f26e946bfbf0f2af"></a>

### `clockid_t`

```c
typedef unsigned long clockid_t
```

<a id="aa1f5af873d05619cbcf7901e194b292c"></a>

### `locale_t`

```c
typedef void* locale_t
```

<a id="a288e13e815d43b06e75819f8939524df"></a>

### `pid_t`

```c
typedef int pid_t
```

<a id="aa37fa84abebf94371f0c8426c2fc614d"></a>

### `timer_t`

```c
typedef unsigned long timer_t
```

<a id="a068e8016542eb374e3c6b301b4babad6"></a>

### `asctime_r()`

```c
char * asctime_r ( const struct tm *ZRESTRICT tm, char *ZRESTRICT buf )
```

<a id="ab2cd29aa41b2b485b571f05ac22d9f7f"></a>

### `clock_getcpuclockid()`

```c
int clock_getcpuclockid ( pid_t pid, clockid_t * clock_id )
```

<a id="a3e1d049d0ed1519b99570efc4d8a1ae3"></a>

### `clock_getres()`

```c
int clock_getres ( clockid_t clock_id, struct timespec * ts )
```

<a id="a21188eaca1b3e48ac3f7715398a1fc06"></a>

### `clock_gettime()`

```c
int clock_gettime ( clockid_t clock_id, struct timespec * ts )
```

<a id="a924d51d78cdcd9d7dee2613fb3a33cd1"></a>

### `clock_nanosleep()`

```c
int clock_nanosleep ( clockid_t clock_id, int flags, const struct timespec * rqtp, struct timespec * rmtp )
```

<a id="adab8a7307d547eb2b882dd1cda3a7655"></a>

### `clock_settime()`

```c
int clock_settime ( clockid_t clock_id, const struct timespec * ts )
```

<a id="abb5334ac0f38a87278861e6edab616db"></a>

### `ctime_r()`

```c
char * ctime_r ( const time_t * clock, char * buf )
```

<a id="abd85b316719134b87f9b60e8abe5af76"></a>

### `getdate()`

```c
struct tm * getdate ( const char * string)
```

<a id="adbf513dac252b14f87719a4a8b6913e7"></a>

### `gmtime_r()`

```c
struct tm * gmtime_r ( const time_t *ZRESTRICT timer, struct tm *ZRESTRICT result )
```

<a id="a3d8015c8bf5fadc92389635bd977e880"></a>

### `localtime_r()`

```c
struct tm * localtime_r ( const time_t *ZRESTRICT timer, struct tm *ZRESTRICT result )
```

<a id="a9ce6a1ed91a601dee133c8b6cf8b721a"></a>

### `nanosleep()`

```c
int nanosleep ( const struct timespec * rqtp, struct timespec * rmtp )
```

<a id="a4f7ca787fc0b633679bc337c4fcd8688"></a>

### `strftime_l()`

```c
size_t strftime_l ( char *ZRESTRICT s, size_t maxsize, const char *ZRESTRICT format, const struct tm *ZRESTRICT timeptr, locale_t locale )
```

<a id="a5a2f2994bcb293fc783a3109f2c76362"></a>

### `strptime()`

```c
char * strptime ( const char *ZRESTRICT s, const char *ZRESTRICT format, struct tm *ZRESTRICT tm )
```

<a id="a5d4a389821dbcc362e93e8ecb895344e"></a>

### `timer_create()`

```c
int timer_create ( clockid_t clockId, struct sigevent *ZRESTRICT evp, timer_t *ZRESTRICT timerid )
```

<a id="ad114bb350d7d5d12cff3fd19bf533303"></a>

### `timer_delete()`

```c
int timer_delete ( timer_t timerid)
```

<a id="ad779f0bc22f64bd3bd977221b0ce1b8f"></a>

### `timer_getoverrun()`

```c
int timer_getoverrun ( timer_t timerid)
```

<a id="a06dda57adfdeb4a9b346f69c95cba96a"></a>

### `timer_gettime()`

```c
int timer_gettime ( timer_t timerid, struct itimerspec * its )
```

<a id="a32207b51f2effa8441f4c728fd8519c0"></a>

### `timer_settime()`

```c
int timer_settime ( timer_t timerid, int flags, const struct itimerspec * value, struct itimerspec * ovalue )
```

<a id="a88051271ca3c003f7c7595fbbd214ea3"></a>

### `daylight`

```c
int daylight
```

声明属性：`extern`。

<a id="a3e348024a4a098ce0b8b51edba679a16"></a>

### `timezone`

```c
long timezone
```

声明属性：`extern`。

<a id="a19e896f49dbb87c8b21378bf8b316b39"></a>

### `tzname`

```c
char* tzname[]
```

声明属性：`extern`。


## 311.7\_原页交叉引用（Cross References）

- [zephyr/sys/clock.h](../timer_reference/P091_系统时钟头文件源码.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h_source.html)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/posix__time_8h_source.html)
- [timespec](../time_headers_reference/P005_timespec时间结构.md)
- [itimerspec](../time_headers_reference/P012_定时器时间规格结构.md)
- [SYS_CLOCK_REALTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gac88ce6c820c962691fdc6e0b344bd887)
- [SYS_CLOCK_MONOTONIC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gab8a1a7e619c67e9a86e773097ce3a8e5)
- [SYS_TIMER_ABSTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga647bea5f74dcf7f6f6fed2c1b78b540f)
- [unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [tm](../posix_system_model_reference/P025_tm_结构体.md)
- [pid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a114f9c2461df851d2ad00aad8dcfa3f7)
- [flags](P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)
- [sigevent](../posix_system_model_reference/P018_sigevent_结构体.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>
<a id="doc-var-members"></a>
<a id="header-doc-var-members"></a>

---

[上一章](P310_zephyr__posix__posix_limits.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P312_zephyr__posix__posix_types.h_文件参考.md)
