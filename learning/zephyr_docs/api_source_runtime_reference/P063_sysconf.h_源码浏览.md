---
id: learning.zephyr-docs.api-source-runtime-reference.page-63
title: sysconf.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sysconf_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第63章\_sysconf.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sysconf_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sysconf_8h.html)。

## 63.1\_原始可见代码（Source Code）

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
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
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
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="alimits_8h_html"></a>
<a id="autil__macro_8h_html"></a>

```c
/*
 * Copyright (c) 2024, Meta
 * Copyright (c) 2024, Tenstorrent AI ULC
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_POSIX_SYS_SYSCONF_H_
#define ZEPHYR_INCLUDE_POSIX_SYS_SYSCONF_H_

#include <limits.h>

#include <zephyr/sys/util_macro.h>

#ifdef __cplusplus
extern "C" {
#endif

enum {
        _SC_ADVISORY_INFO,
        _SC_ASYNCHRONOUS_IO,
        _SC_BARRIERS,
        _SC_CLOCK_SELECTION,
        _SC_CPUTIME,
        _SC_FSYNC,
        _SC_IPV6,
        _SC_JOB_CONTROL,
        _SC_MAPPED_FILES,
        _SC_MEMLOCK,
        _SC_MEMLOCK_RANGE,
        _SC_MEMORY_PROTECTION,
        _SC_MESSAGE_PASSING,
        _SC_MONOTONIC_CLOCK,
        _SC_PRIORITIZED_IO,
        _SC_PRIORITY_SCHEDULING,
        _SC_RAW_SOCKETS,
        _SC_RE_DUP_MAX,
        _SC_READER_WRITER_LOCKS,
        _SC_REALTIME_SIGNALS,
        _SC_REGEXP,
        _SC_SAVED_IDS,
        _SC_SEMAPHORES,
        _SC_SHARED_MEMORY_OBJECTS,
        _SC_SHELL,
        _SC_SPAWN,
        _SC_SPIN_LOCKS,
        _SC_SPORADIC_SERVER,
        _SC_SS_REPL_MAX,
        _SC_SYNCHRONIZED_IO,
        _SC_THREAD_ATTR_STACKADDR,
        _SC_THREAD_ATTR_STACKSIZE,
        _SC_THREAD_CPUTIME,
        _SC_THREAD_PRIO_INHERIT,
        _SC_THREAD_PRIO_PROTECT,
        _SC_THREAD_PRIORITY_SCHEDULING,
        _SC_THREAD_PROCESS_SHARED,
        _SC_THREAD_ROBUST_PRIO_INHERIT,
        _SC_THREAD_ROBUST_PRIO_PROTECT,
        _SC_THREAD_SAFE_FUNCTIONS,
        _SC_THREAD_SPORADIC_SERVER,
        _SC_THREADS,
        _SC_TIMEOUTS,
        _SC_TIMERS,
        _SC_TRACE,
        _SC_TRACE_EVENT_FILTER,
        _SC_TRACE_EVENT_NAME_MAX,
        _SC_TRACE_INHERIT,
        _SC_TRACE_LOG,
        _SC_TRACE_NAME_MAX,
        _SC_TRACE_SYS_MAX,
        _SC_TRACE_USER_EVENT_MAX,
        _SC_TYPED_MEMORY_OBJECTS,
        _SC_VERSION,
        _SC_V7_ILP32_OFF32,
        _SC_V7_ILP32_OFFBIG,
        _SC_V7_LP64_OFF64,
        _SC_V7_LPBIG_OFFBIG,
        _SC_V6_ILP32_OFF32,
        _SC_V6_ILP32_OFFBIG,
        _SC_V6_LP64_OFF64,
        _SC_V6_LPBIG_OFFBIG,
        _SC_BC_BASE_MAX,
        _SC_BC_DIM_MAX,
        _SC_BC_SCALE_MAX,
        _SC_BC_STRING_MAX,
        _SC_2_C_BIND,
        _SC_2_C_DEV,
        _SC_2_CHAR_TERM,
        _SC_COLL_WEIGHTS_MAX,
        _SC_DELAYTIMER_MAX,
        _SC_EXPR_NEST_MAX,
        _SC_2_FORT_DEV,
        _SC_2_FORT_RUN,
        _SC_LINE_MAX,
        _SC_2_LOCALEDEF,
        _SC_2_PBS,
        _SC_2_PBS_ACCOUNTING,
        _SC_2_PBS_CHECKPOINT,
        _SC_2_PBS_LOCATE,
        _SC_2_PBS_MESSAGE,
        _SC_2_PBS_TRACK,
        _SC_2_SW_DEV,
        _SC_2_UPE,
        _SC_2_VERSION,
        _SC_XOPEN_CRYPT,
        _SC_XOPEN_ENH_I18N,
        _SC_XOPEN_REALTIME,
        _SC_XOPEN_REALTIME_THREADS,
        _SC_XOPEN_SHM,
        _SC_XOPEN_STREAMS,
        _SC_XOPEN_UNIX,
        _SC_XOPEN_UUCP,
        _SC_XOPEN_VERSION,
        _SC_CLK_TCK,
        _SC_GETGR_R_SIZE_MAX,
        _SC_GETPW_R_SIZE_MAX,
        _SC_AIO_LISTIO_MAX,
        _SC_AIO_MAX,
        _SC_AIO_PRIO_DELTA_MAX,
        _SC_ARG_MAX,
        _SC_ATEXIT_MAX,
        _SC_CHILD_MAX,
        _SC_HOST_NAME_MAX,
        _SC_IOV_MAX,
        _SC_LOGIN_NAME_MAX,
        _SC_NGROUPS_MAX,
        _SC_MQ_OPEN_MAX,
        _SC_MQ_PRIO_MAX,
        _SC_OPEN_MAX,
        _SC_PAGE_SIZE,
        _SC_PAGESIZE,
        _SC_THREAD_DESTRUCTOR_ITERATIONS,
        _SC_THREAD_KEYS_MAX,
        _SC_THREAD_STACK_MIN,
        _SC_THREAD_THREADS_MAX,
        _SC_RTSIG_MAX,
        _SC_SEM_NSEMS_MAX,
        _SC_SEM_VALUE_MAX,
        _SC_SIGQUEUE_MAX,
        _SC_STREAM_MAX,
        _SC_SYMLOOP_MAX,
        _SC_TIMER_MAX,
        _SC_TTY_NAME_MAX,
        _SC_TZNAME_MAX,
};

/*
 * clang-format and checkpatch disagree on formatting here, so rely on checkpatch and disable
 * clang-format since checkpatch cannot be selectively disabled.
 */

/* clang-format off */

#define __z_posix_sysconf_SC_ADVISORY_INFO (-1L)
#define __z_posix_sysconf_SC_ASYNCHRONOUS_IO                                                       \
        COND_CODE_1(CONFIG_POSIX_ASYNCHRONOUS_IO, (_POSIX_ASYNCHRONOUS_IO), (-1L))
#define __z_posix_sysconf_SC_BARRIERS COND_CODE_1(CONFIG_POSIX_BARRIERS, (_POSIX_BARRIERS), (-1L))
#define __z_posix_sysconf_SC_CLOCK_SELECTION                                                       \
        COND_CODE_1(CONFIG_POSIX_CLOCK_SELECTION, (_POSIX_CLOCK_SELECTION), (-1L))
#define __z_posix_sysconf_SC_CPUTIME \
        COND_CODE_1(CONFIG_POSIX_CPUTIME, (_POSIX_CPUTIME), (-1L))
#define __z_posix_sysconf_SC_FSYNC                                                                 \
        COND_CODE_1(CONFIG_POSIX_FSYNC, (_POSIX_FSYNC), (-1L))
#define __z_posix_sysconf_SC_IPV6              COND_CODE_1(CONFIG_NET_IPV6, (_POSIX_IPV6), (-1L))
#define __z_posix_sysconf_SC_JOB_CONTROL       (-1L)
#define __z_posix_sysconf_SC_MAPPED_FILES                                                          \
        COND_CODE_1(CONFIG_POSIX_MAPPED_FILES, (_POSIX_MAPPED_FILES), (-1L))
#define __z_posix_sysconf_SC_MEMLOCK                                                               \
        COND_CODE_1(CONFIG_POSIX_MEMLOCK, (_POSIX_MEMLOCK), (-1L))
#define __z_posix_sysconf_SC_MEMLOCK_RANGE                                                         \
        COND_CODE_1(CONFIG_POSIX_MEMLOCK_RANGE, (_POSIX_MEMLOCK_RANGE), (-1L))
#define __z_posix_sysconf_SC_MEMORY_PROTECTION                                                     \
        COND_CODE_1(CONFIG_POSIX_MEMORY_PROTECTION, (_POSIX_MEMORY_PROTECTION), (-1L))
#define __z_posix_sysconf_SC_MESSAGE_PASSING                                                       \
        COND_CODE_1(CONFIG_POSIX_MESSAGE_PASSING, (_POSIX_MESSAGE_PASSING), (-1L))
#define __z_posix_sysconf_SC_MONOTONIC_CLOCK                                                       \
        COND_CODE_1(CONFIG_POSIX_MONOTONIC_CLOCK, (_POSIX_MONOTONIC_CLOCK), (-1L))
#define __z_posix_sysconf_SC_PRIORITIZED_IO (-1L)
#define __z_posix_sysconf_SC_PRIORITY_SCHEDULING                                                   \
        COND_CODE_1(CONFIG_POSIX_PRIORITY_SCHEDULING, (_POSIX_PRIORITY_SCHEDULING), (-1L))
#define __z_posix_sysconf_SC_RAW_SOCKETS                                                           \
        COND_CODE_1(CONFIG_NET_SOCKETS_PACKET, (_POSIX_RAW_SOCKETS), (-1L))
#define __z_posix_sysconf_SC_RE_DUP_MAX _POSIX_RE_DUP_MAX
#define __z_posix_sysconf_SC_READER_WRITER_LOCKS                                                   \
        COND_CODE_1(CONFIG_POSIX_RW_LOCKS, (_POSIX_READER_WRITER_LOCKS), (-1L))
#define __z_posix_sysconf_SC_REALTIME_SIGNALS      (-1L)
#define __z_posix_sysconf_SC_REGEXP                (-1L)
#define __z_posix_sysconf_SC_SAVED_IDS             (-1L)
#define __z_posix_sysconf_SC_SEMAPHORES                                                            \
        COND_CODE_1(CONFIG_POSIX_SEMAPHORES, (_POSIX_SEMAPHORES), (-1L))
#define __z_posix_sysconf_SC_SHARED_MEMORY_OBJECTS                                                 \
        COND_CODE_1(CONFIG_POSIX_SHARED_MEMORY_OBJECTS, (_POSIX_SHARED_MEMORY_OBJECTS), (-1L))
#define __z_posix_sysconf_SC_SHELL                 (-1L)
#define __z_posix_sysconf_SC_SPAWN                 (-1L)
#define __z_posix_sysconf_SC_SPIN_LOCKS                                                            \
        COND_CODE_1(CONFIG_POSIX_SPIN_LOCKS, (_POSIX_SPIN_LOCKS), (-1L))
#define __z_posix_sysconf_SC_SPORADIC_SERVER (-1L)
#define __z_posix_sysconf_SC_SS_REPL_MAX     _POSIX_SS_REPL_MAX
#define __z_posix_sysconf_SC_SYNCHRONIZED_IO (-1L)
#define __z_posix_sysconf_SC_THREAD_ATTR_STACKADDR                                                 \
        COND_CODE_1(CONFIG_POSIX_THREAD_ATTR_STACKADDR, (_POSIX_THREAD_ATTR_STACKADDR), (-1))
#define __z_posix_sysconf_SC_THREAD_ATTR_STACKSIZE                                                 \
        COND_CODE_1(CONFIG_POSIX_THREAD_ATTR_STACKSIZE, (_POSIX_THREAD_ATTR_STACKSIZE), (-1L))
#define __z_posix_sysconf_SC_THREAD_CPUTIME (-1L)
#define __z_posix_sysconf_SC_THREAD_PRIO_INHERIT                                                   \
        COND_CODE_1(CONFIG_POSIX_THREAD_PRIO_INHERIT, (_POSIX_THREAD_PRIO_INHERIT), (-1L))
#define __z_posix_sysconf_SC_THREAD_PRIO_PROTECT        (-1L)
#define __z_posix_sysconf_SC_THREAD_PRIORITY_SCHEDULING                                            \
        COND_CODE_1(CONFIG_POSIX_THREAD_PRIORITY_SCHEDULING, (_POSIX_THREAD_PRIORITY_SCHEDULING),  \
                    (-1L))
#define __z_posix_sysconf_SC_THREAD_PROCESS_SHARED      (-1L)
#define __z_posix_sysconf_SC_THREAD_ROBUST_PRIO_INHERIT (-1L)
#define __z_posix_sysconf_SC_THREAD_ROBUST_PRIO_PROTECT (-1L)
#define __z_posix_sysconf_SC_THREAD_SAFE_FUNCTIONS                                                 \
        COND_CODE_1(CONFIG_POSIX_THREAD_SAFE_FUNCTIONS, (_POSIX_THREAD_SAFE_FUNCTIONS), (-1L))
#define __z_posix_sysconf_SC_THREAD_SPORADIC_SERVER       (-1L)
#define __z_posix_sysconf_SC_THREADS                                                               \
        COND_CODE_1(CONFIG_POSIX_THREADS, (_POSIX_THREADS), (-1L))
#define __z_posix_sysconf_SC_TIMEOUTS                                                              \
        COND_CODE_1(CONFIG_POSIX_TIMEOUTS, (_POSIX_TIMEOUTS), (-1L))
#define __z_posix_sysconf_SC_TIMERS                                                                \
        COND_CODE_1(CONFIG_POSIX_TIMEOUTS, (_POSIX_TIMERS), (-1))
#define __z_posix_sysconf_SC_TRACE                        (-1L)
#define __z_posix_sysconf_SC_TRACE_EVENT_FILTER           (-1L)
#define __z_posix_sysconf_SC_TRACE_EVENT_NAME_MAX         _POSIX_TRACE_NAME_MAX
#define __z_posix_sysconf_SC_TRACE_INHERIT                (-1L)
#define __z_posix_sysconf_SC_TRACE_LOG                    (-1L)
#define __z_posix_sysconf_SC_TRACE_NAME_MAX               _POSIX_TRACE_NAME_MAX
#define __z_posix_sysconf_SC_TRACE_SYS_MAX                _POSIX_TRACE_SYS_MAX
#define __z_posix_sysconf_SC_TRACE_USER_EVENT_MAX         _POSIX_TRACE_USER_EVENT_MAX
#define __z_posix_sysconf_SC_TYPED_MEMORY_OBJECTS         (-1L)
#define __z_posix_sysconf_SC_VERSION                      _POSIX_VERSION
#define __z_posix_sysconf_SC_V6_ILP32_OFF32               (-1L)
#define __z_posix_sysconf_SC_V6_ILP32_OFFBIG              (-1L)
#define __z_posix_sysconf_SC_V6_LP64_OFF64                (-1L)
#define __z_posix_sysconf_SC_V6_LPBIG_OFFBIG              (-1L)
#define __z_posix_sysconf_SC_V7_ILP32_OFF32               (-1L)
#define __z_posix_sysconf_SC_V7_ILP32_OFFBIG              (-1L)
#define __z_posix_sysconf_SC_V7_LP64_OFF64                (-1L)
#define __z_posix_sysconf_SC_V7_LPBIG_OFFBIG              (-1L)
#define __z_posix_sysconf_SC_BC_BASE_MAX                  _POSIX2_BC_BASE_MAX
#define __z_posix_sysconf_SC_BC_DIM_MAX                   _POSIX2_BC_DIM_MAX
#define __z_posix_sysconf_SC_BC_SCALE_MAX                 _POSIX2_BC_SCALE_MAX
#define __z_posix_sysconf_SC_BC_STRING_MAX                _POSIX2_BC_STRING_MAX
#define __z_posix_sysconf_SC_2_C_BIND                     _POSIX2_C_BIND
#define __z_posix_sysconf_SC_2_C_DEV                                                               \
        COND_CODE_1(_POSIX2_C_DEV > 0, (_POSIX2_C_DEV), (-1))
#define __z_posix_sysconf_SC_2_CHAR_TERM                  (-1L)
#define __z_posix_sysconf_SC_COLL_WEIGHTS_MAX             _POSIX2_COLL_WEIGHTS_MAX
#define __z_posix_sysconf_SC_DELAYTIMER_MAX                                                        \
        COND_CODE_1(CONFIG_POSIX_TIMERS, (CONFIG_POSIX_DELAYTIMER_MAX), (0))
#define __z_posix_sysconf_SC_EXPR_NEST_MAX                _POSIX2_EXPR_NEST_MAX
#define __z_posix_sysconf_SC_2_FORT_DEV                   (-1L)
#define __z_posix_sysconf_SC_2_FORT_RUN                   (-1L)
#define __z_posix_sysconf_SC_LINE_MAX                     (-1L)
#define __z_posix_sysconf_SC_2_LOCALEDEF                  (-1L)
#define __z_posix_sysconf_SC_2_PBS                        (-1L)
#define __z_posix_sysconf_SC_2_PBS_ACCOUNTING             (-1L)
#define __z_posix_sysconf_SC_2_PBS_CHECKPOINT             (-1L)
#define __z_posix_sysconf_SC_2_PBS_LOCATE                 (-1L)
#define __z_posix_sysconf_SC_2_PBS_MESSAGE                (-1L)
#define __z_posix_sysconf_SC_2_PBS_TRACK                  (-1L)
#define __z_posix_sysconf_SC_2_SW_DEV                     (-1L)
#define __z_posix_sysconf_SC_2_UPE                        (-1L)
#define __z_posix_sysconf_SC_2_VERSION                                                             \
        COND_CODE_1(_POSIX2_VERSION > 0, (_POSIX2_VERSION), (-1))
#define __z_posix_sysconf_SC_XOPEN_CRYPT                  (-1L)
#define __z_posix_sysconf_SC_XOPEN_ENH_I18N               (-1L)
#define __z_posix_sysconf_SC_XOPEN_REALTIME               (-1L)
#define __z_posix_sysconf_SC_XOPEN_REALTIME_THREADS       (-1L)
#define __z_posix_sysconf_SC_XOPEN_SHM                    (-1L)
#define __z_posix_sysconf_SC_XOPEN_STREAMS                                                         \
        COND_CODE_1(CONFIG_XOPEN_STREAMS, (_XOPEN_STREAMS), (-1))
#define __z_posix_sysconf_SC_XOPEN_UNIX                   (-1L)
#define __z_posix_sysconf_SC_XOPEN_UUCP                   (-1L)
#define __z_posix_sysconf_SC_XOPEN_VERSION                _XOPEN_VERSION
#define __z_posix_sysconf_SC_CLK_TCK                      (100L)
#define __z_posix_sysconf_SC_GETGR_R_SIZE_MAX             (0L)
#define __z_posix_sysconf_SC_GETPW_R_SIZE_MAX             (0L)
#define __z_posix_sysconf_SC_AIO_LISTIO_MAX               _POSIX_AIO_LISTIO_MAX
#define __z_posix_sysconf_SC_AIO_MAX                      _POSIX_AIO_MAX
#define __z_posix_sysconf_SC_AIO_PRIO_DELTA_MAX           0
#define __z_posix_sysconf_SC_ARG_MAX                      _POSIX_ARG_MAX
#define __z_posix_sysconf_SC_ATEXIT_MAX                   32
#define __z_posix_sysconf_SC_CHILD_MAX                    _POSIX_CHILD_MAX
#define __z_posix_sysconf_SC_HOST_NAME_MAX                                                         \
        COND_CODE_1(CONFIG_POSIX_NETWORKING, (CONFIG_POSIX_HOST_NAME_MAX), (0))
#define __z_posix_sysconf_SC_IOV_MAX                      16 /* _XOPEN_IOV_MAX */
#define __z_posix_sysconf_SC_LOGIN_NAME_MAX               _POSIX_LOGIN_NAME_MAX
#define __z_posix_sysconf_SC_NGROUPS_MAX                  _POSIX_NGROUPS_MAX
#define __z_posix_sysconf_SC_MQ_OPEN_MAX                                                           \
        COND_CODE_1(CONFIG_POSIX_MESSAGE_PASSING, (CONFIG_POSIX_MQ_OPEN_MAX), (0))
#define __z_posix_sysconf_SC_MQ_PRIO_MAX                  _POSIX_MQ_PRIO_MAX
#define __z_posix_sysconf_SC_OPEN_MAX                     CONFIG_POSIX_OPEN_MAX
#define __z_posix_sysconf_SC_PAGE_SIZE                    CONFIG_POSIX_PAGE_SIZE
#define __z_posix_sysconf_SC_PAGESIZE                     CONFIG_POSIX_PAGE_SIZE
#define __z_posix_sysconf_SC_THREAD_DESTRUCTOR_ITERATIONS _POSIX_THREAD_DESTRUCTOR_ITERATIONS
#define __z_posix_sysconf_SC_THREAD_KEYS_MAX                                                       \
        COND_CODE_1(CONFIG_POSIX_THREADS, (CONFIG_POSIX_THREAD_KEYS_MAX), (0))
#define __z_posix_sysconf_SC_THREAD_STACK_MIN             0
#define __z_posix_sysconf_SC_THREAD_THREADS_MAX                                                    \
        COND_CODE_1(CONFIG_POSIX_THREADS, (CONFIG_POSIX_THREAD_THREADS_MAX), (0))
#define __z_posix_sysconf_SC_RTSIG_MAX                                                             \
        COND_CODE_1(CONFIG_POSIX_REALTIME_SIGNALS, (CONFIG_POSIX_RTSIG_MAX), (0))
#define __z_posix_sysconf_SC_SEM_NSEMS_MAX                                                         \
        COND_CODE_1(CONFIG_POSIX_SEMAPHORES, (CONFIG_POSIX_SEM_NSEMS_MAX), (0))
#define __z_posix_sysconf_SC_SEM_VALUE_MAX                                                         \
        COND_CODE_1(CONFIG_POSIX_SEMAPHORES, (CONFIG_POSIX_SEM_VALUE_MAX), (0))
#define __z_posix_sysconf_SC_SIGQUEUE_MAX                 _POSIX_SIGQUEUE_MAX
#define __z_posix_sysconf_SC_STREAM_MAX                   _POSIX_STREAM_MAX
#define __z_posix_sysconf_SC_SYMLOOP_MAX                  _POSIX_SYMLOOP_MAX
#define __z_posix_sysconf_SC_TIMER_MAX                                                             \
        COND_CODE_1(CONFIG_POSIX_TIMERS, (CONFIG_POSIX_TIMER_MAX), (0))
#define __z_posix_sysconf_SC_TTY_NAME_MAX                 _POSIX_TTY_NAME_MAX
#define __z_posix_sysconf_SC_TZNAME_MAX                   _POSIX_TZNAME_MAX

#ifdef CONFIG_POSIX_SYSCONF_IMPL_MACRO
#define sysconf(x) (long)CONCAT(__z_posix_sysconf, x)
#endif

/* clang-format on */

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_POSIX_SYS_SYSCONF_H_ */
```

## 63.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024, Meta。

版权（Copyright）：© 2024, Tenstorrent AI ULC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 146 行

clang-format 与 checkpatch 在此处的格式要求不一致，因此以 checkpatch 为准并禁用 clang-format，因为 checkpatch 无法有选择地禁用。

### 注释 3：原第 151 行

关闭 clang-format 自动排版（clang-format off）。

### 注释 4：原第 287 行

限制值标记：`_XOPEN_IOV_MAX`。

### 注释 5：原第 320 行

开启 clang-format 自动排版（clang-format on）。

### 注释 6：原第 326 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_POSIX_SYS_SYSCONF_H_`。

## 63.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sysconf_8h.html)
- [limits.h](https://docs.zephyrproject.org/latest/doxygen/html/limits_8h.html)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P062_symtab.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P064_tsl2591.h_源码浏览.md)
