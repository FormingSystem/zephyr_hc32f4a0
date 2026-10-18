---
id: learning.zephyr-docs.api-file-reference.page-310
title: zephyr__posix__posix_limits.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/posix__limits_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第310章\_zephyr\_\_posix\_\_posix\_limits.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/posix__limits_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 310.1\_宏定义（Macros）

<a id="r_a82c429c39d68f08d56e4bfdb050fe54a"></a>

```c
#define NL_LANGMAX (14)
```

相关声明：[NL_LANGMAX](#a82c429c39d68f08d56e4bfdb050fe54a)。

<a id="r_a7e7a512ab4395a4bb0be4ff872764e45"></a>

```c
#define NL_MSGMAX (32767)
```

相关声明：[NL_MSGMAX](#a7e7a512ab4395a4bb0be4ff872764e45)。

<a id="r_a5dd5a06bde8cda4edb4dfda129375a1a"></a>

```c
#define NL_SETMAX (255)
```

相关声明：[NL_SETMAX](#a5dd5a06bde8cda4edb4dfda129375a1a)。

<a id="r_a934658c7b37ed12672f76ec304a5b460"></a>

```c
#define NL_TEXTMAX (_POSIX2_LINE_MAX)
```

相关声明：[NL_TEXTMAX](#a934658c7b37ed12672f76ec304a5b460)。

<a id="r_a3b04cc1d4ce6930b578eede1f1c6ebfc"></a>

```c
#define NZERO (20)
```

相关声明：[NZERO](#a3b04cc1d4ce6930b578eede1f1c6ebfc)。

<a id="r_a0b4029afb1dcaf401c08b7b147d00cec"></a>

```c
#define AIO_LISTIO_MAX _POSIX_AIO_LISTIO_MAX
```

相关声明：[AIO_LISTIO_MAX](#a0b4029afb1dcaf401c08b7b147d00cec)。

<a id="r_a0889d4ed1489519e1e8a83ca6f212c5a"></a>

```c
#define AIO_MAX _POSIX_AIO_MAX
```

相关声明：[AIO_MAX](#a0889d4ed1489519e1e8a83ca6f212c5a)。

<a id="r_aa9d8b79923c4fc549c074fc387ef65c9"></a>

```c
#define AIO_PRIO_DELTA_MAX (0)
```

相关声明：[AIO_PRIO_DELTA_MAX](#aa9d8b79923c4fc549c074fc387ef65c9)。

<a id="r_a7dd33d4d7fdd2221a03ce948d7419424"></a>

```c
#define ARG_MAX _POSIX_ARG_MAX
```

相关声明：[ARG_MAX](#a7dd33d4d7fdd2221a03ce948d7419424)。

<a id="r_abf407c2e796fa3e943acf18be72aa01d"></a>

```c
#define ATEXIT_MAX (32)
```

相关声明：[ATEXIT_MAX](#abf407c2e796fa3e943acf18be72aa01d)。

<a id="r_a86025bd0a07f29a6ae97f310ff9c701c"></a>

```c
#define DELAYTIMER_MAX COND_CODE_1(CONFIG_POSIX_TIMERS, (CONFIG_POSIX_DELAYTIMER_MAX), (0))
```

相关声明：[DELAYTIMER_MAX](#a86025bd0a07f29a6ae97f310ff9c701c)、[COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)。

<a id="r_ac956117a90023ec0971b8f9fce9dec75"></a>

```c
#define HOST_NAME_MAX COND_CODE_1(CONFIG_POSIX_NETWORKING, (CONFIG_POSIX_HOST_NAME_MAX), (0))
```

相关声明：[HOST_NAME_MAX](#ac956117a90023ec0971b8f9fce9dec75)、[COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)。

<a id="r_af3b7f7833ae69cac7adf84f5973715fe"></a>

```c
#define LOGIN_NAME_MAX _POSIX_LOGIN_NAME_MAX
```

相关声明：[LOGIN_NAME_MAX](#af3b7f7833ae69cac7adf84f5973715fe)。

<a id="r_abea867e23b4ca9316a0a7511f1b783d3"></a>

```c
#define MQ_OPEN_MAX COND_CODE_1(CONFIG_POSIX_MESSAGE_PASSING, (CONFIG_POSIX_MQ_OPEN_MAX), (0))
```

相关声明：[MQ_OPEN_MAX](#abea867e23b4ca9316a0a7511f1b783d3)、[COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)。

<a id="r_ad1516b4f64b6dc890b1fa3bf576bfef9"></a>

```c
#define MQ_PRIO_MAX _POSIX_MQ_PRIO_MAX
```

相关声明：[MQ_PRIO_MAX](#ad1516b4f64b6dc890b1fa3bf576bfef9)。

<a id="r_a35969138e24f6cf13b0763f713c6d53b"></a>

```c
#define OPEN_MAX CONFIG_POSIX_OPEN_MAX
```

相关声明：[OPEN_MAX](#a35969138e24f6cf13b0763f713c6d53b)。

<a id="r_a7d467c1d283fdfa1f2081ba1e0d01b6e"></a>

```c
#define PAGE_SIZE CONFIG_POSIX_PAGE_SIZE
```

相关声明：[PAGE_SIZE](#a7d467c1d283fdfa1f2081ba1e0d01b6e)。

<a id="r_a519adc2af3ba06a8f0548b6690050a89"></a>

```c
#define PAGESIZE CONFIG_POSIX_PAGE_SIZE
```

相关声明：[PAGESIZE](#a519adc2af3ba06a8f0548b6690050a89)。

<a id="r_ae688d728e1acdfe5988c7db45d6f0166"></a>

```c
#define PATH_MAX _POSIX_PATH_MAX
```

相关声明：[PATH_MAX](#ae688d728e1acdfe5988c7db45d6f0166)。

<a id="r_a1d96b13a4ba5975d724c5fe13788a957"></a>

```c
#define PTHREAD_DESTRUCTOR_ITERATIONS _POSIX_THREAD_DESTRUCTOR_ITERATIONS
```

相关声明：[PTHREAD_DESTRUCTOR_ITERATIONS](#a1d96b13a4ba5975d724c5fe13788a957)。

<a id="r_a0a23e66e087bcf5c253b9b2746f19a64"></a>

```c
#define PTHREAD_KEYS_MAX COND_CODE_1(CONFIG_POSIX_THREADS, (CONFIG_POSIX_THREAD_KEYS_MAX), (0))
```

相关声明：[PTHREAD_KEYS_MAX](#a0a23e66e087bcf5c253b9b2746f19a64)、[COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)。

<a id="r_ab8f25dec585d6255fcf40b67db66c1c5"></a>

```c
#define PTHREAD_THREADS_MAX COND_CODE_1(CONFIG_POSIX_THREADS, (CONFIG_POSIX_THREAD_THREADS_MAX), (0))
```

相关声明：[PTHREAD_THREADS_MAX](#ab8f25dec585d6255fcf40b67db66c1c5)、[COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)。

<a id="r_ad7f754398cdc81462f3d626e74a41b69"></a>

```c
#define RTSIG_MAX COND_CODE_1(CONFIG_POSIX_REALTIME_SIGNALS, (CONFIG_POSIX_RTSIG_MAX), (0))
```

相关声明：[RTSIG_MAX](#ad7f754398cdc81462f3d626e74a41b69)、[COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)。

<a id="r_a829c888ff8820c37384a5531577cea33"></a>

```c
#define SEM_NSEMS_MAX COND_CODE_1(CONFIG_POSIX_SEMAPHORES, (CONFIG_POSIX_SEM_NSEMS_MAX), (0))
```

相关声明：[SEM_NSEMS_MAX](#a829c888ff8820c37384a5531577cea33)、[COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)。

<a id="r_a2961bb23950351c6b10976674c27ddaf"></a>

```c
#define SEM_VALUE_MAX COND_CODE_1(CONFIG_POSIX_SEMAPHORES, (CONFIG_POSIX_SEM_VALUE_MAX), (0))
```

相关声明：[SEM_VALUE_MAX](#a2961bb23950351c6b10976674c27ddaf)、[COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)。

<a id="r_a649781c35d0360b7d68ef6d55f2aa668"></a>

```c
#define SIGQUEUE_MAX _POSIX_SIGQUEUE_MAX
```

相关声明：[SIGQUEUE_MAX](#a649781c35d0360b7d68ef6d55f2aa668)。

<a id="r_a238bb3d2a0e88f9ff3e46a6affd7f61d"></a>

```c
#define STREAM_MAX _POSIX_STREAM_MAX
```

相关声明：[STREAM_MAX](#a238bb3d2a0e88f9ff3e46a6affd7f61d)。

<a id="r_a41170bbc4e205b3bc9c2b06033aecc17"></a>

```c
#define SYMLOOP_MAX _POSIX_SYMLOOP_MAX
```

相关声明：[SYMLOOP_MAX](#a41170bbc4e205b3bc9c2b06033aecc17)。

<a id="r_a9cb39fc9fca65abcf086c5b293db3772"></a>

```c
#define TIMER_MAX COND_CODE_1(CONFIG_POSIX_TIMERS, (CONFIG_POSIX_TIMER_MAX), (0))
```

相关声明：[TIMER_MAX](#a9cb39fc9fca65abcf086c5b293db3772)、[COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)。

<a id="r_a8e87ff1f5de326c7161ef933ff2fb0f1"></a>

```c
#define TTY_NAME_MAX _POSIX_TTY_NAME_MAX
```

相关声明：[TTY_NAME_MAX](#a8e87ff1f5de326c7161ef933ff2fb0f1)。

<a id="r_afb3fe48998f8d32cfb7047b917a8039e"></a>

```c
#define TZNAME_MAX _POSIX_TZNAME_MAX
```

相关声明：[TZNAME_MAX](#afb3fe48998f8d32cfb7047b917a8039e)。

<a id="r_a34ef6afc1709d5686f1353804aa03e88"></a>

```c
#define FILESIZEBITS (32)
```

相关声明：[FILESIZEBITS](#a34ef6afc1709d5686f1353804aa03e88)。

<a id="r_aa9c42ba60b7eac67360d9804a99e8bba"></a>

```c
#define POSIX_ALLOC_SIZE_MIN (256)
```

相关声明：[POSIX_ALLOC_SIZE_MIN](#aa9c42ba60b7eac67360d9804a99e8bba)。

<a id="r_a9d04829540462d79aa8751d230987d8b"></a>

```c
#define POSIX_REC_INCR_XFER_SIZE (1024)
```

相关声明：[POSIX_REC_INCR_XFER_SIZE](#a9d04829540462d79aa8751d230987d8b)。

<a id="r_a17269b771b87209b99c9698c782f0d9b"></a>

```c
#define POSIX_REC_MAX_XFER_SIZE (32767)
```

相关声明：[POSIX_REC_MAX_XFER_SIZE](#a17269b771b87209b99c9698c782f0d9b)。

<a id="r_a3dae40a21514758cfd61dfb8f159c6f4"></a>

```c
#define POSIX_REC_MIN_XFER_SIZE (1)
```

相关声明：[POSIX_REC_MIN_XFER_SIZE](#a3dae40a21514758cfd61dfb8f159c6f4)。

<a id="r_a40069c33a92e401df7b3b09d1e65ce55"></a>

```c
#define POSIX_REC_XFER_ALIGN (4)
```

相关声明：[POSIX_REC_XFER_ALIGN](#a40069c33a92e401df7b3b09d1e65ce55)。

<a id="r_af552b1b86caac064b8d74f73ac9d3f0c"></a>

```c
#define SYMLINK_MAX _POSIX_SYMLINK_MAX
```

相关声明：[SYMLINK_MAX](#af552b1b86caac064b8d74f73ac9d3f0c)。

## 310.2\_详细说明（Detailed Documentation）

<a id="a0b4029afb1dcaf401c08b7b147d00cec"></a>

### `AIO_LISTIO_MAX`

```c
#define AIO_LISTIO_MAX _POSIX_AIO_LISTIO_MAX
```

<a id="a0889d4ed1489519e1e8a83ca6f212c5a"></a>

### `AIO_MAX`

```c
#define AIO_MAX _POSIX_AIO_MAX
```

<a id="aa9d8b79923c4fc549c074fc387ef65c9"></a>

### `AIO_PRIO_DELTA_MAX`

```c
#define AIO_PRIO_DELTA_MAX (0)
```

<a id="a7dd33d4d7fdd2221a03ce948d7419424"></a>

### `ARG_MAX`

```c
#define ARG_MAX _POSIX_ARG_MAX
```

<a id="abf407c2e796fa3e943acf18be72aa01d"></a>

### `ATEXIT_MAX`

```c
#define ATEXIT_MAX (32)
```

<a id="a86025bd0a07f29a6ae97f310ff9c701c"></a>

### `DELAYTIMER_MAX`

```c
#define DELAYTIMER_MAX COND_CODE_1(CONFIG_POSIX_TIMERS, (CONFIG_POSIX_DELAYTIMER_MAX), (0))
```

<a id="a34ef6afc1709d5686f1353804aa03e88"></a>

### `FILESIZEBITS`

```c
#define FILESIZEBITS (32)
```

<a id="ac956117a90023ec0971b8f9fce9dec75"></a>

### `HOST_NAME_MAX`

```c
#define HOST_NAME_MAX COND_CODE_1(CONFIG_POSIX_NETWORKING, (CONFIG_POSIX_HOST_NAME_MAX), (0))
```

<a id="af3b7f7833ae69cac7adf84f5973715fe"></a>

### `LOGIN_NAME_MAX`

```c
#define LOGIN_NAME_MAX _POSIX_LOGIN_NAME_MAX
```

<a id="abea867e23b4ca9316a0a7511f1b783d3"></a>

### `MQ_OPEN_MAX`

```c
#define MQ_OPEN_MAX COND_CODE_1(CONFIG_POSIX_MESSAGE_PASSING, (CONFIG_POSIX_MQ_OPEN_MAX), (0))
```

<a id="ad1516b4f64b6dc890b1fa3bf576bfef9"></a>

### `MQ_PRIO_MAX`

```c
#define MQ_PRIO_MAX _POSIX_MQ_PRIO_MAX
```

<a id="a82c429c39d68f08d56e4bfdb050fe54a"></a>

### `NL_LANGMAX`

```c
#define NL_LANGMAX (14)
```

<a id="a7e7a512ab4395a4bb0be4ff872764e45"></a>

### `NL_MSGMAX`

```c
#define NL_MSGMAX (32767)
```

<a id="a5dd5a06bde8cda4edb4dfda129375a1a"></a>

### `NL_SETMAX`

```c
#define NL_SETMAX (255)
```

<a id="a934658c7b37ed12672f76ec304a5b460"></a>

### `NL_TEXTMAX`

```c
#define NL_TEXTMAX (_POSIX2_LINE_MAX)
```

<a id="a3b04cc1d4ce6930b578eede1f1c6ebfc"></a>

### `NZERO`

```c
#define NZERO (20)
```

<a id="a35969138e24f6cf13b0763f713c6d53b"></a>

### `OPEN_MAX`

```c
#define OPEN_MAX CONFIG_POSIX_OPEN_MAX
```

<a id="a7d467c1d283fdfa1f2081ba1e0d01b6e"></a>

### `PAGE_SIZE`

```c
#define PAGE_SIZE CONFIG_POSIX_PAGE_SIZE
```

<a id="a519adc2af3ba06a8f0548b6690050a89"></a>

### `PAGESIZE`

```c
#define PAGESIZE CONFIG_POSIX_PAGE_SIZE
```

<a id="ae688d728e1acdfe5988c7db45d6f0166"></a>

### `PATH_MAX`

```c
#define PATH_MAX _POSIX_PATH_MAX
```

<a id="aa9c42ba60b7eac67360d9804a99e8bba"></a>

### `POSIX_ALLOC_SIZE_MIN`

```c
#define POSIX_ALLOC_SIZE_MIN (256)
```

<a id="a9d04829540462d79aa8751d230987d8b"></a>

### `POSIX_REC_INCR_XFER_SIZE`

```c
#define POSIX_REC_INCR_XFER_SIZE (1024)
```

<a id="a17269b771b87209b99c9698c782f0d9b"></a>

### `POSIX_REC_MAX_XFER_SIZE`

```c
#define POSIX_REC_MAX_XFER_SIZE (32767)
```

<a id="a3dae40a21514758cfd61dfb8f159c6f4"></a>

### `POSIX_REC_MIN_XFER_SIZE`

```c
#define POSIX_REC_MIN_XFER_SIZE (1)
```

<a id="a40069c33a92e401df7b3b09d1e65ce55"></a>

### `POSIX_REC_XFER_ALIGN`

```c
#define POSIX_REC_XFER_ALIGN (4)
```

<a id="a1d96b13a4ba5975d724c5fe13788a957"></a>

### `PTHREAD_DESTRUCTOR_ITERATIONS`

```c
#define PTHREAD_DESTRUCTOR_ITERATIONS _POSIX_THREAD_DESTRUCTOR_ITERATIONS
```

<a id="a0a23e66e087bcf5c253b9b2746f19a64"></a>

### `PTHREAD_KEYS_MAX`

```c
#define PTHREAD_KEYS_MAX COND_CODE_1(CONFIG_POSIX_THREADS, (CONFIG_POSIX_THREAD_KEYS_MAX), (0))
```

<a id="ab8f25dec585d6255fcf40b67db66c1c5"></a>

### `PTHREAD_THREADS_MAX`

```c
#define PTHREAD_THREADS_MAX COND_CODE_1(CONFIG_POSIX_THREADS, (CONFIG_POSIX_THREAD_THREADS_MAX), (0))
```

<a id="ad7f754398cdc81462f3d626e74a41b69"></a>

### `RTSIG_MAX`

```c
#define RTSIG_MAX COND_CODE_1(CONFIG_POSIX_REALTIME_SIGNALS, (CONFIG_POSIX_RTSIG_MAX), (0))
```

<a id="a829c888ff8820c37384a5531577cea33"></a>

### `SEM_NSEMS_MAX`

```c
#define SEM_NSEMS_MAX COND_CODE_1(CONFIG_POSIX_SEMAPHORES, (CONFIG_POSIX_SEM_NSEMS_MAX), (0))
```

<a id="a2961bb23950351c6b10976674c27ddaf"></a>

### `SEM_VALUE_MAX`

```c
#define SEM_VALUE_MAX COND_CODE_1(CONFIG_POSIX_SEMAPHORES, (CONFIG_POSIX_SEM_VALUE_MAX), (0))
```

<a id="a649781c35d0360b7d68ef6d55f2aa668"></a>

### `SIGQUEUE_MAX`

```c
#define SIGQUEUE_MAX _POSIX_SIGQUEUE_MAX
```

<a id="a238bb3d2a0e88f9ff3e46a6affd7f61d"></a>

### `STREAM_MAX`

```c
#define STREAM_MAX _POSIX_STREAM_MAX
```

<a id="af552b1b86caac064b8d74f73ac9d3f0c"></a>

### `SYMLINK_MAX`

```c
#define SYMLINK_MAX _POSIX_SYMLINK_MAX
```

<a id="a41170bbc4e205b3bc9c2b06033aecc17"></a>

### `SYMLOOP_MAX`

```c
#define SYMLOOP_MAX _POSIX_SYMLOOP_MAX
```

<a id="a9cb39fc9fca65abcf086c5b293db3772"></a>

### `TIMER_MAX`

```c
#define TIMER_MAX COND_CODE_1(CONFIG_POSIX_TIMERS, (CONFIG_POSIX_TIMER_MAX), (0))
```

<a id="a8e87ff1f5de326c7161ef933ff2fb0f1"></a>

### `TTY_NAME_MAX`

```c
#define TTY_NAME_MAX _POSIX_TTY_NAME_MAX
```

<a id="afb3fe48998f8d32cfb7047b917a8039e"></a>

### `TZNAME_MAX`

```c
#define TZNAME_MAX _POSIX_TZNAME_MAX
```


## 310.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/posix__limits_8h_source.html)
- [COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P309_zephyr__posix__posix_features.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P311_zephyr__posix__posix_time.h_文件参考.md)
