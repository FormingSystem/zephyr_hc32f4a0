---
id: learning.zephyr-docs.api-source-register-time-reference.page-8
title: posix_time.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/posix__time_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_posix\_time.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/posix__time_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md)。

## 8.1\_原始可见代码（Source Code）

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
<a id="foldopen00074"></a>
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
<a id="a__timespec_8h_html_aa17c461cd5eca7fc12a66daa803c7fd7"></a>
<a id="aclock_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="aposix__signal_8h_html_a114f9c2461df851d2ad00aad8dcfa3f7"></a>
<a id="aposix__time_8h_html_a068e8016542eb374e3c6b301b4babad6"></a>
<a id="aposix__time_8h_html_a06dda57adfdeb4a9b346f69c95cba96a"></a>
<a id="aposix__time_8h_html_a19e896f49dbb87c8b21378bf8b316b39"></a>
<a id="aposix__time_8h_html_a21188eaca1b3e48ac3f7715398a1fc06"></a>
<a id="aposix__time_8h_html_a32207b51f2effa8441f4c728fd8519c0"></a>
<a id="aposix__time_8h_html_a3d8015c8bf5fadc92389635bd977e880"></a>
<a id="aposix__time_8h_html_a3e1d049d0ed1519b99570efc4d8a1ae3"></a>
<a id="aposix__time_8h_html_a3e348024a4a098ce0b8b51edba679a16"></a>
<a id="aposix__time_8h_html_a4f7ca787fc0b633679bc337c4fcd8688"></a>
<a id="aposix__time_8h_html_a5a2f2994bcb293fc783a3109f2c76362"></a>
<a id="aposix__time_8h_html_a5d4a389821dbcc362e93e8ecb895344e"></a>
<a id="aposix__time_8h_html_a6bb3206700910111f26e946bfbf0f2af"></a>
<a id="aposix__time_8h_html_a88051271ca3c003f7c7595fbbd214ea3"></a>
<a id="aposix__time_8h_html_a924d51d78cdcd9d7dee2613fb3a33cd1"></a>
<a id="aposix__time_8h_html_a9ce6a1ed91a601dee133c8b6cf8b721a"></a>
<a id="aposix__time_8h_html_aa1f5af873d05619cbcf7901e194b292c"></a>
<a id="aposix__time_8h_html_aa37fa84abebf94371f0c8426c2fc614d"></a>
<a id="aposix__time_8h_html_ab2cd29aa41b2b485b571f05ac22d9f7f"></a>
<a id="aposix__time_8h_html_abb5334ac0f38a87278861e6edab616db"></a>
<a id="aposix__time_8h_html_abd85b316719134b87f9b60e8abe5af76"></a>
<a id="aposix__time_8h_html_ad114bb350d7d5d12cff3fd19bf533303"></a>
<a id="aposix__time_8h_html_ad779f0bc22f64bd3bd977221b0ce1b8f"></a>
<a id="aposix__time_8h_html_adab8a7307d547eb2b882dd1cda3a7655"></a>
<a id="aposix__time_8h_html_adbf513dac252b14f87719a4a8b6913e7"></a>
<a id="astructitimerspec_html"></a>
<a id="astructitimerspec_html_a27cedae552e2b2fe0993c1b2c4ff1889"></a>
<a id="astructitimerspec_html_a754dda918053251c24558b07571d6e8f"></a>
<a id="astructsigevent_html"></a>
<a id="astructtimespec_html"></a>
<a id="astructtimespec_html_ae3c7510dafa8cbcaede866ed13c99683"></a>
<a id="astructtimespec_html_afc3302668d7cb5952f590da69fdd4955"></a>
<a id="astructtm_html"></a>
<a id="atoolchain_8h_html"></a>

```c
/*
 * Copyright The Zephyr Project Contributors
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_POSIX_POSIX_TIME_H_
#define ZEPHYR_INCLUDE_POSIX_POSIX_TIME_H_

#if defined(_POSIX_C_SOURCE) || defined(__DOXYGEN__)

#include <stddef.h>

#include <zephyr/sys/clock.h>
#include <zephyr/toolchain.h>

#ifdef __cplusplus
extern "C" {
#endif

/* clock_t must be defined in the libc time.h */
/* size_t must be defined in the libc stddef.h */
/* time_t must be defined in the libc time.h */

#if !defined(_CLOCKID_T_DECLARED) && !defined(__clockid_t_defined)
typedef unsigned long clockid_t;
#define _CLOCKID_T_DECLARED
#define __clockid_t_defined
#endif

#if !defined(_TIMER_T_DECLARED) && !defined(__timer_t_defined)
typedef unsigned long timer_t;
#define _TIMER_T_DECLARED
#define __timer_t_defined
#endif

#if !defined(_LOCALE_T_DECLARED) && !defined(__locale_t_defined)
#ifdef CONFIG_NEWLIB_LIBC
struct __locale_t;
typedef struct __locale_t *locale_t;
#else
typedef void *locale_t;
#endif
#define _LOCALE_T_DECLARED
#define __locale_t_defined
#endif

#if !defined(_PID_T_DECLARED) && !defined(__pid_t_defined)
typedef int pid_t;
#define _PID_T_DECLARED
#define __pid_t_defined
#endif

#if defined(_POSIX_REALTIME_SIGNALS)
struct sigevent;
#endif

/* struct tm must be defined in the libc time.h */

#if __STDC_VERSION__ >= 201112L
/* struct timespec must be defined in the libc time.h */
#else
#if !defined(_TIMESPEC_DECLARED) && !defined(__timespec_defined)
struct timespec {
        time_t tv_sec;
        long tv_nsec;
};
#define _TIMESPEC_DECLARED
#define __timespec_defined
#endif
#endif

#if !defined(_ITIMERSPEC_DECLARED) && !defined(__itimerspec_defined)
struct itimerspec {
        struct timespec it_interval;
        struct timespec it_value;
};
#define _ITIMERSPEC_DECLARED
#define __itimerspec_defined
#endif

/* NULL must be defined in the libc stddef.h */

#ifndef CLOCK_REALTIME
#define CLOCK_REALTIME ((clockid_t)SYS_CLOCK_REALTIME)
#endif

#ifndef CLOCKS_PER_SEC
#if defined(_XOPEN_SOURCE)
#define CLOCKS_PER_SEC 1000000
#else
#define CLOCKS_PER_SEC CONFIG_SYS_CLOCK_TICKS_PER_SEC
#endif
#endif

#if defined(_POSIX_CPUTIME) || defined(__DOXYGEN__)
#ifndef CLOCK_PROCESS_CPUTIME_ID
#define CLOCK_PROCESS_CPUTIME_ID ((clockid_t)2)
#endif
#endif

#if defined(_POSIX_THREAD_CPUTIME) || defined(__DOXYGEN__)
#ifndef CLOCK_THREAD_CPUTIME_ID
#define CLOCK_THREAD_CPUTIME_ID ((clockid_t)3)
#endif
#endif

#if defined(_POSIX_MONOTONIC_CLOCK) || defined(__DOXYGEN__)
#ifndef CLOCK_MONOTONIC
#define CLOCK_MONOTONIC ((clockid_t)SYS_CLOCK_MONOTONIC)
#endif
#endif

#ifndef TIMER_ABSTIME
#define TIMER_ABSTIME SYS_TIMER_ABSTIME
#endif

/* asctime() must be declared in the libc time.h */
#if defined(_POSIX_THREAD_SAFE_FUNCTIONS) || defined(__DOXYGEN__)
char *asctime_r(const struct tm *ZRESTRICT tm, char *ZRESTRICT buf);
#endif
/* clock() must be declared in the libc time.h */
#if defined(_POSIX_CPUTIME) || defined(__DOXYGEN__)
int clock_getcpuclockid(pid_t pid, clockid_t *clock_id);
#endif
#if defined(_POSIX_TIMERS) || defined(__DOXYGEN__)
int clock_getres(clockid_t clock_id, struct timespec *ts);
int clock_gettime(clockid_t clock_id, struct timespec *ts);
#endif
#if defined(_POSIX_CLOCK_SELECTION) || defined(__DOXYGEN__)
int clock_nanosleep(clockid_t clock_id, int flags, const struct timespec *rqtp,
                    struct timespec *rmtp);
#endif
#if defined(_POSIX_TIMERS) || defined(__DOXYGEN__)
int clock_settime(clockid_t clock_id, const struct timespec *ts);
#endif
/* ctime() must be declared in the libc time.h */
#if defined(_POSIX_THREAD_SAFE_FUNCTIONS) || defined(__DOXYGEN__)
char *ctime_r(const time_t *clock, char *buf);
#endif
/* difftime() must be declared in the libc time.h */
#if defined(_XOPEN_SOURCE) || defined(__DOXYGEN__)
struct tm *getdate(const char *string);
#endif
/* gmtime() must be declared in the libc time.h */
#if __STDC_VERSION__ >= 202311L
/* gmtime_r() must be declared in the libc time.h */
#else
#if defined(_POSIX_THREAD_SAFE_FUNCTIONS) || defined(__DOXYGEN__)
struct tm *gmtime_r(const time_t *ZRESTRICT timer, struct tm *ZRESTRICT result);
#endif
#endif
/* localtime() must be declared in the libc time.h */
#if __STDC_VERSION__ >= 202311L
/* localtime_r() must be declared in the libc time.h */
#else
#if defined(_POSIX_THREAD_SAFE_FUNCTIONS) || defined(__DOXYGEN__)
struct tm *localtime_r(const time_t *ZRESTRICT timer, struct tm *ZRESTRICT result);
#endif
#endif
/* mktime() must be declared in the libc time.h */
#if defined(_POSIX_TIMERS) || defined(__DOXYGEN__)
int nanosleep(const struct timespec *rqtp, struct timespec *rmtp);
#endif
/* strftime() must be declared in the libc time.h */
size_t strftime_l(char *ZRESTRICT s, size_t maxsize, const char *ZRESTRICT format,
                  const struct tm *ZRESTRICT timeptr, locale_t locale);
#if defined(_XOPEN_SOURCE) || defined(__DOXYGEN__)
char *strptime(const char *ZRESTRICT s, const char *ZRESTRICT format, struct tm *ZRESTRICT tm);
#endif
/* time() must be declared in the libc time.h */
#if defined(_POSIX_TIMERS) || defined(__DOXYGEN__)
int timer_create(clockid_t clockId, struct sigevent *ZRESTRICT evp, timer_t *ZRESTRICT timerid);
int timer_delete(timer_t timerid);
int timer_getoverrun(timer_t timerid);
int timer_gettime(timer_t timerid, struct itimerspec *its);
int timer_settime(timer_t timerid, int flags, const struct itimerspec *value,
                  struct itimerspec *ovalue);
#endif

#if defined(_XOPEN_SOURCE) || defined(__DOXYGEN__)
extern int daylight;
extern long timezone;
#endif

extern char *tzname[];

#ifdef __cplusplus
}
#endif

#endif /* defined(_POSIX_C_SOURCE) || defined(__DOXYGEN__) */

#endif /* ZEPHYR_INCLUDE_POSIX_POSIX_TIME_H_ */
```

## 8.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：The Zephyr Project Contributors。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 21 行

必须在 libc 的 `time.h` 中定义 `clock_t`。

### 注释 3：原第 22 行

必须在 libc 的 `stddef.h` 中定义 `size_t`。

### 注释 4：原第 23 行

必须在 libc 的 `time.h` 中定义 `time_t`。

### 注释 5：原第 58 行

必须在 libc 的 `time.h` 中定义 `struct tm`。

### 注释 6：原第 61 行

必须在 libc 的 `time.h` 中定义 `struct timespec`。

### 注释 7：原第 82 行

必须在 libc 的 `stddef.h` 中定义 `NULL`。

### 注释 8：原第 118 行

必须在 libc 的 `time.h` 中声明 `asctime()`。

### 注释 9：原第 122 行

必须在 libc 的 `time.h` 中声明 `clock()`。

### 注释 10：原第 137 行

必须在 libc 的 `time.h` 中声明 `ctime()`。

### 注释 11：原第 141 行

必须在 libc 的 `time.h` 中声明 `difftime()`。

### 注释 12：原第 145 行

必须在 libc 的 `time.h` 中声明 `gmtime()`。

### 注释 13：原第 147 行

必须在 libc 的 `time.h` 中声明 `gmtime_r()`。

### 注释 14：原第 153 行

必须在 libc 的 `time.h` 中声明 `localtime()`。

### 注释 15：原第 155 行

必须在 libc 的 `time.h` 中声明 `localtime_r()`。

### 注释 16：原第 161 行

必须在 libc 的 `time.h` 中声明 `mktime()`。

### 注释 17：原第 165 行

必须在 libc 的 `time.h` 中声明 `strftime()`。

### 注释 18：原第 171 行

必须在 libc 的 `time.h` 中声明 `time()`。

### 注释 19：原第 192 行

条件表达式：`defined(_POSIX_C_SOURCE) || defined(__DOXYGEN__)`。

### 注释 20：原第 194 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_POSIX_POSIX_TIME_H_`。

## 8.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md)
- [zephyr/sys/clock.h](../timer_reference/P090_系统时钟头文件参考.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [clockid_t](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md#a6bb3206700910111f26e946bfbf0f2af)
- [timer_t](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md#aa37fa84abebf94371f0c8426c2fc614d)
- [locale_t](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md#aa1f5af873d05619cbcf7901e194b292c)
- [pid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a114f9c2461df851d2ad00aad8dcfa3f7)
- [sigevent](../posix_system_model_reference/P018_sigevent_结构体.md)
- [timespec](../time_headers_reference/P005_timespec时间结构.md)
- [time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)
- [tv_sec](../time_headers_reference/P005_timespec时间结构.md#afc3302668d7cb5952f590da69fdd4955)
- [tv_nsec](../time_headers_reference/P005_timespec时间结构.md#ae3c7510dafa8cbcaede866ed13c99683)
- [itimerspec](../time_headers_reference/P012_定时器时间规格结构.md)
- [it_interval](../time_headers_reference/P012_定时器时间规格结构.md#a27cedae552e2b2fe0993c1b2c4ff1889)
- [it_value](../time_headers_reference/P012_定时器时间规格结构.md#a754dda918053251c24558b07571d6e8f)
- [asctime_r](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md#a068e8016542eb374e3c6b301b4babad6)
- [tm](../posix_system_model_reference/P025_tm_结构体.md)
- [clock_getcpuclockid](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md#ab2cd29aa41b2b485b571f05ac22d9f7f)
- [clock_getres](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md#a3e1d049d0ed1519b99570efc4d8a1ae3)
- [clock_gettime](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md#a21188eaca1b3e48ac3f7715398a1fc06)
- [clock_nanosleep](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md#a924d51d78cdcd9d7dee2613fb3a33cd1)
- [flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [clock_settime](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md#adab8a7307d547eb2b882dd1cda3a7655)
- [ctime_r](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md#abb5334ac0f38a87278861e6edab616db)
- [getdate](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md#abd85b316719134b87f9b60e8abe5af76)
- [gmtime_r](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md#adbf513dac252b14f87719a4a8b6913e7)
- [localtime_r](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md#a3d8015c8bf5fadc92389635bd977e880)
- [nanosleep](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md#a9ce6a1ed91a601dee133c8b6cf8b721a)
- [strftime_l](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md#a4f7ca787fc0b633679bc337c4fcd8688)
- [strptime](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md#a5a2f2994bcb293fc783a3109f2c76362)
- [timer_create](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md#a5d4a389821dbcc362e93e8ecb895344e)
- [timer_delete](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md#ad114bb350d7d5d12cff3fd19bf533303)
- [timer_getoverrun](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md#ad779f0bc22f64bd3bd977221b0ce1b8f)
- [timer_gettime](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md#a06dda57adfdeb4a9b346f69c95cba96a)
- [timer_settime](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md#a32207b51f2effa8441f4c728fd8519c0)
- [daylight](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md#a88051271ca3c003f7c7595fbbd214ea3)
- [timezone](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md#a3e348024a4a098ce0b8b51edba679a16)
- [tzname](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md#a19e896f49dbb87c8b21378bf8b316b39)
- [clock.h](../timer_reference/P090_系统时钟头文件参考.md)
- [itimerspec::it_interval](../time_headers_reference/P012_定时器时间规格结构.md#a27cedae552e2b2fe0993c1b2c4ff1889)
- [itimerspec::it_value](../time_headers_reference/P012_定时器时间规格结构.md#a754dda918053251c24558b07571d6e8f)
- [timespec::tv_nsec](../time_headers_reference/P005_timespec时间结构.md#ae3c7510dafa8cbcaede866ed13c99683)
- [timespec::tv_sec](../time_headers_reference/P005_timespec时间结构.md#afc3302668d7cb5952f590da69fdd4955)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P007_numaker_m46x_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P009_stm32-fmc-nor-psram.h_源码浏览.md)
