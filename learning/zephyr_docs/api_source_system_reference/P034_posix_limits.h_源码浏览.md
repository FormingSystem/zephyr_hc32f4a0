---
id: learning.zephyr-docs.api-source-system-reference.page-34
title: posix_limits.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/posix__limits_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_posix\_limits.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/posix__limits_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P310_zephyr__posix__posix_limits.h_文件参考.md)。

## 34.1\_原始可见代码（Source Code）

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
<a id="foldopen00085"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="foldopen00087"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="foldopen00090"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="foldopen00098"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="foldopen00100"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="foldopen00102"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="foldopen00104"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="foldopen00106"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="foldopen00111"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
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
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>

```c
/*
 * Copyright The Zephyr Project Contributors
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_POSIX_POSIX_LIMITS_H_
#define ZEPHYR_INCLUDE_POSIX_POSIX_LIMITS_H_

#if defined(_POSIX_C_SOURCE) || defined(__DOXYGEN__)

/*
 * clang-format and checkpatch disagree on formatting here, so rely on checkpatch and disable
 * clang-format since checkpatch cannot be selectively disabled.
 */

/* clang-format off */

/* Maximum values */
#define _POSIX_CLOCKRES_MIN (20000000L)

/* Minimum values */
#define _POSIX_AIO_LISTIO_MAX               (2)
#define _POSIX_AIO_MAX                      (1)
#define _POSIX_ARG_MAX                      (4096)
#define _POSIX_CHILD_MAX                    (25)
#define _POSIX_DELAYTIMER_MAX               (32)
#define _POSIX_HOST_NAME_MAX                (255)
#define _POSIX_LINK_MAX                     (8)
#define _POSIX_LOGIN_NAME_MAX               (9)
#define _POSIX_MAX_CANON                    (255)
#define _POSIX_MAX_INPUT                    (255)
#define _POSIX_MQ_OPEN_MAX                  (8)
#define _POSIX_MQ_PRIO_MAX                  (32)
#define _POSIX_NAME_MAX                     (14)
#define _POSIX_NGROUPS_MAX                  (8)
#define _POSIX_OPEN_MAX                     (20)
#define _POSIX_PATH_MAX                     (256)
#define _POSIX_PIPE_BUF                     (512)
#define _POSIX_RE_DUP_MAX                   (255)
#define _POSIX_RTSIG_MAX                    (8)
#define _POSIX_SEM_NSEMS_MAX                (256)
#define _POSIX_SEM_VALUE_MAX                (32767)
#define _POSIX_SIGQUEUE_MAX                 (32)
#define _POSIX_SSIZE_MAX                    (32767)
#define _POSIX_SS_REPL_MAX                  (4)
#define _POSIX_STREAM_MAX                   (8)
#define _POSIX_SYMLINK_MAX                  (255)
#define _POSIX_SYMLOOP_MAX                  (8)
#define _POSIX_THREAD_DESTRUCTOR_ITERATIONS (4)
#define _POSIX_THREAD_KEYS_MAX              (128)
#define _POSIX_THREAD_THREADS_MAX           (64)
#define _POSIX_TIMER_MAX                    (32)
#define _POSIX_TRACE_EVENT_NAME_MAX         (30)
#define _POSIX_TRACE_NAME_MAX               (8)
#define _POSIX_TRACE_SYS_MAX                (8)
#define _POSIX_TRACE_USER_EVENT_MAX         (32)
#define _POSIX_TTY_NAME_MAX                 (9)
#define _POSIX_TZNAME_MAX                   (6)
#define _POSIX2_BC_BASE_MAX                 (99)
#define _POSIX2_BC_DIM_MAX                  (2048)
#define _POSIX2_BC_SCALE_MAX                (99)
#define _POSIX2_BC_STRING_MAX               (1000)
#define _POSIX2_CHARCLASS_NAME_MAX          (14)
#define _POSIX2_COLL_WEIGHTS_MAX            (2)
#define _POSIX2_EXPR_NEST_MAX               (32)
#define _POSIX2_LINE_MAX                    (2048)
#define _XOPEN_IOV_MAX                      (16)
#define _XOPEN_NAME_MAX                     (255)
#define _XOPEN_PATH_MAX                     (1024)

/* Other invariant values */
#define NL_LANGMAX (14)
#define NL_MSGMAX  (32767)
#define NL_SETMAX  (255)
#define NL_TEXTMAX (_POSIX2_LINE_MAX)
#define NZERO      (20)

/* Runtime invariant values */
#define AIO_LISTIO_MAX                _POSIX_AIO_LISTIO_MAX
#define AIO_MAX                       _POSIX_AIO_MAX
#define AIO_PRIO_DELTA_MAX            (0)
#define ARG_MAX                       _POSIX_ARG_MAX
#define ATEXIT_MAX                    (32)
#define DELAYTIMER_MAX \
        COND_CODE_1(CONFIG_POSIX_TIMERS, (CONFIG_POSIX_DELAYTIMER_MAX), (0))
#define HOST_NAME_MAX \
        COND_CODE_1(CONFIG_POSIX_NETWORKING, (CONFIG_POSIX_HOST_NAME_MAX), (0))
#define LOGIN_NAME_MAX                _POSIX_LOGIN_NAME_MAX
#define MQ_OPEN_MAX \
        COND_CODE_1(CONFIG_POSIX_MESSAGE_PASSING, (CONFIG_POSIX_MQ_OPEN_MAX), (0))
#define MQ_PRIO_MAX                   _POSIX_MQ_PRIO_MAX
#define OPEN_MAX                      CONFIG_POSIX_OPEN_MAX
#define PAGE_SIZE                     CONFIG_POSIX_PAGE_SIZE
#define PAGESIZE                      CONFIG_POSIX_PAGE_SIZE
#define PATH_MAX                      _POSIX_PATH_MAX
#define PTHREAD_DESTRUCTOR_ITERATIONS _POSIX_THREAD_DESTRUCTOR_ITERATIONS
#define PTHREAD_KEYS_MAX \
        COND_CODE_1(CONFIG_POSIX_THREADS, (CONFIG_POSIX_THREAD_KEYS_MAX), (0))
#define PTHREAD_THREADS_MAX \
        COND_CODE_1(CONFIG_POSIX_THREADS, (CONFIG_POSIX_THREAD_THREADS_MAX), (0))
#define RTSIG_MAX \
        COND_CODE_1(CONFIG_POSIX_REALTIME_SIGNALS, (CONFIG_POSIX_RTSIG_MAX), (0))
#define SEM_NSEMS_MAX \
        COND_CODE_1(CONFIG_POSIX_SEMAPHORES, (CONFIG_POSIX_SEM_NSEMS_MAX), (0))
#define SEM_VALUE_MAX \
        COND_CODE_1(CONFIG_POSIX_SEMAPHORES, (CONFIG_POSIX_SEM_VALUE_MAX), (0))
#define SIGQUEUE_MAX                  _POSIX_SIGQUEUE_MAX
#define STREAM_MAX                    _POSIX_STREAM_MAX
#define SYMLOOP_MAX                   _POSIX_SYMLOOP_MAX
#define TIMER_MAX \
        COND_CODE_1(CONFIG_POSIX_TIMERS, (CONFIG_POSIX_TIMER_MAX), (0))
#define TTY_NAME_MAX                  _POSIX_TTY_NAME_MAX
#define TZNAME_MAX                    _POSIX_TZNAME_MAX

/* Pathname variable values */
#define FILESIZEBITS             (32)
#define POSIX_ALLOC_SIZE_MIN     (256)
#define POSIX_REC_INCR_XFER_SIZE (1024)
#define POSIX_REC_MAX_XFER_SIZE  (32767)
#define POSIX_REC_MIN_XFER_SIZE  (1)
#define POSIX_REC_XFER_ALIGN     (4)
#define SYMLINK_MAX              _POSIX_SYMLINK_MAX

/* clang-format on */

#endif

#endif /* ZEPHYR_INCLUDE_POSIX_POSIX_LIMITS_H_ */
```

## 34.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：The Zephyr Project Contributors。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 12 行

clang-format 与 checkpatch 在此处的格式要求不一致，因此以 checkpatch 为准并禁用 clang-format，因为 checkpatch 无法有选择地禁用。

### 注释 3：原第 17 行

关闭 clang-format 自动排版（clang-format off）。

### 注释 4：原第 19 行

最大值（Maximum Values）。

### 注释 5：原第 22 行

最小值（Minimum Values）。

### 注释 6：原第 72 行

其他不变值（Other Invariant Values）。

### 注释 7：原第 79 行

运行时不变值（Runtime Invariant Values）。

### 注释 8：原第 116 行

路径名可变值（Pathname Variable Values）。

### 注释 9：原第 125 行

开启 clang-format 自动排版（clang-format on）。

### 注释 10：原第 129 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_POSIX_POSIX_LIMITS_H_`。

## 34.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P310_zephyr__posix__posix_limits.h_文件参考.md)

---

[上一章](P033_nxp_flexram.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P035_posix_types.h_源码浏览.md)
