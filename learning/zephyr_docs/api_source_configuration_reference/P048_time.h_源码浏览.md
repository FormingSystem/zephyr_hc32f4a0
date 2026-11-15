---
id: learning.zephyr-docs.api-source-configuration-reference.page-48
title: time.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2time_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第48章\_time.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2time_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2time_8h.html)。

## 48.1\_原始可见代码（Source Code）

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
<a id="foldopen00024"></a>
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
<a id="a__timespec_8h_html"></a>
<a id="a__timespec_8h_html_aa17c461cd5eca7fc12a66daa803c7fd7"></a>
<a id="a__timespec_8h_html_ad7acf95ceafb15a1d8d86af0c4982995"></a>
<a id="a__types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2time_8h_html_a068d11e0d50eab73920a3162d2ac9202"></a>
<a id="alib_2libc_2minimal_2include_2time_8h_html_a185521f2c273b9697eb1e536a37912fb"></a>
<a id="alib_2libc_2minimal_2include_2time_8h_html_a3d8015c8bf5fadc92389635bd977e880"></a>
<a id="alib_2libc_2minimal_2include_2time_8h_html_a47dad42d50a51f3ba4033320084c833b"></a>
<a id="alib_2libc_2minimal_2include_2time_8h_html_a4bc4ff58d4ac838a36ba939747e5833e"></a>
<a id="alib_2libc_2minimal_2include_2time_8h_html_a86ed062bf74f495209b11b650631e2f2"></a>
<a id="alib_2libc_2minimal_2include_2time_8h_html_a99ef1cb2c789827dd5db3886dccf9067"></a>
<a id="alib_2libc_2minimal_2include_2time_8h_html_abb5334ac0f38a87278861e6edab616db"></a>
<a id="alib_2libc_2minimal_2include_2time_8h_html_aee41f7a79e9f6ec34cdf7096fd597dbd"></a>
<a id="aposix__time_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astructtm_html"></a>
<a id="astructtm_html_a112ac36fa2f593777138a417cf031e17"></a>
<a id="astructtm_html_a33adf78fd6476b2120ce3b9c4a852053"></a>
<a id="astructtm_html_a3e7ca4e37f1abcaf56b8a916c38eb9fe"></a>
<a id="astructtm_html_a4d098a9a5c03a00b2ee61e10851de81e"></a>
<a id="astructtm_html_a5645ca0580c8ab2c24f6c2965d9c9f9c"></a>
<a id="astructtm_html_a93a0ba77cc23796df84405dcbcc57eb1"></a>
<a id="astructtm_html_ab8d8904bad43b0c8b96e61941c5b5310"></a>
<a id="astructtm_html_af414eb7c86cc3099595211eee4d4211b"></a>
<a id="astructtm_html_afe81a8c46f1c693c43f259b288859f4f"></a>
<a id="atoolchain_8h_html"></a>

```c
/*
 * Copyright (c) 2017 Intel Corporation
 * Copyright (c) 2019 Peter Bigot Consulting, LLC
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_TIME_H_
#define ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_TIME_H_

#include <stdint.h>
#include <zephyr/toolchain.h>
#include <sys/_types.h>
#include <sys/_timespec.h>

/* Minimal time.h to fulfill the requirements of certain libraries
 * like Mbed TLS and to support time APIs.
 */

#ifdef __cplusplus
extern "C" {
#endif

struct tm {
        int tm_sec;
        int tm_min;
        int tm_hour;
        int tm_mday;
        int tm_mon;
        int tm_year;
        int tm_wday;
        int tm_yday;
        int tm_isdst;
};

#if !defined(__time_t_defined)
#define __time_t_defined
typedef _TIME_T_ time_t;
#endif

#if !defined(__suseconds_t_defined)
#define __suseconds_t_defined
typedef _SUSECONDS_T_ suseconds_t;
#endif

/*
 * Conversion between civil time and UNIX time.  The companion
 * mktime() is not provided here since it
 * require access to time zone information.
 *
 * The localtime() & localtime_r() simply
 * wraps around the gmtime() & gmtime_r() functions, the
 * results are always expressed as UTC.
 */
struct tm *gmtime(const time_t *timep);
struct tm *gmtime_r(const time_t *ZRESTRICT timep,
                    struct tm *ZRESTRICT result);
char *asctime(const struct tm *timeptr);
struct tm *localtime(const time_t *timer);
char *ctime(const time_t *clock);
char *asctime_r(const struct tm *ZRESTRICT tp, char *ZRESTRICT buf);
char *ctime_r(const time_t *clock, char *buf);
struct tm *localtime_r(const time_t *ZRESTRICT timer, struct tm *ZRESTRICT result);

time_t time(time_t *tloc);

#ifdef __cplusplus
}
#endif

#include <zephyr/posix/posix_time.h>

#endif /* ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_STDIO_H_ */
```

## 48.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2017 Intel Corporation。

版权（Copyright）：© 2019 Peter Bigot Consulting, LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 16 行

最小化的 `time.h`，用于满足 Mbed TLS 等特定库的要求，并支持时间 API。

### 注释 3：原第 46 行

民用时间（Civil time）与 UNIX 时间之间的转换。此处不提供配套的 `mktime()`，因为它需要访问时区信息。

`localtime()` 和 `localtime_r()` 只是对 `gmtime()` 和 `gmtime_r()` 的封装，结果始终以协调世界时（UTC）表示。

### 注释 4：原第 73 行

头文件保护宏（Header guard）标记：`ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_STDIO_H_`。

## 48.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2time_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [sys/_types.h](https://docs.zephyrproject.org/latest/doxygen/html/__types_8h.html)
- [sys/_timespec.h](../time_headers_reference/P003_timespec类型头文件参考.md)
- [tm](../posix_system_model_reference/P025_tm_结构体.md)
- [tm_sec](../posix_system_model_reference/P025_tm_结构体.md#a4d098a9a5c03a00b2ee61e10851de81e)
- [tm_min](../posix_system_model_reference/P025_tm_结构体.md#af414eb7c86cc3099595211eee4d4211b)
- [tm_hour](../posix_system_model_reference/P025_tm_结构体.md#a3e7ca4e37f1abcaf56b8a916c38eb9fe)
- [tm_mday](../posix_system_model_reference/P025_tm_结构体.md#ab8d8904bad43b0c8b96e61941c5b5310)
- [tm_mon](../posix_system_model_reference/P025_tm_结构体.md#a112ac36fa2f593777138a417cf031e17)
- [tm_year](../posix_system_model_reference/P025_tm_结构体.md#a33adf78fd6476b2120ce3b9c4a852053)
- [tm_wday](../posix_system_model_reference/P025_tm_结构体.md#afe81a8c46f1c693c43f259b288859f4f)
- [tm_yday](../posix_system_model_reference/P025_tm_结构体.md#a93a0ba77cc23796df84405dcbcc57eb1)
- [tm_isdst](../posix_system_model_reference/P025_tm_结构体.md#a5645ca0580c8ab2c24f6c2965d9c9f9c)
- [time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)
- [suseconds_t](../time_headers_reference/P003_timespec类型头文件参考.md#ad7acf95ceafb15a1d8d86af0c4982995)
- [gmtime](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2time_8h.html#a4bc4ff58d4ac838a36ba939747e5833e)
- [gmtime_r](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2time_8h.html#aee41f7a79e9f6ec34cdf7096fd597dbd)
- [asctime](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2time_8h.html#a068d11e0d50eab73920a3162d2ac9202)
- [localtime](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2time_8h.html#a47dad42d50a51f3ba4033320084c833b)
- [ctime](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2time_8h.html#a185521f2c273b9697eb1e536a37912fb)
- [asctime_r](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2time_8h.html#a86ed062bf74f495209b11b650631e2f2)
- [ctime_r](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2time_8h.html#abb5334ac0f38a87278861e6edab616db)
- [localtime_r](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2time_8h.html#a3d8015c8bf5fadc92389635bd977e880)
- [time](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2time_8h.html#a99ef1cb2c789827dd5db3886dccf9067)
- [zephyr/posix/posix_time.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__time_8h.html)
- [_timespec.h](../time_headers_reference/P003_timespec类型头文件参考.md)
- [_types.h](https://docs.zephyrproject.org/latest/doxygen/html/__types_8h.html)
- [posix_time.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__time_8h.html)
- [tm::tm_mon](../posix_system_model_reference/P025_tm_结构体.md#a112ac36fa2f593777138a417cf031e17)
- [tm::tm_year](../posix_system_model_reference/P025_tm_结构体.md#a33adf78fd6476b2120ce3b9c4a852053)
- [tm::tm_hour](../posix_system_model_reference/P025_tm_结构体.md#a3e7ca4e37f1abcaf56b8a916c38eb9fe)
- [tm::tm_sec](../posix_system_model_reference/P025_tm_结构体.md#a4d098a9a5c03a00b2ee61e10851de81e)
- [tm::tm_isdst](../posix_system_model_reference/P025_tm_结构体.md#a5645ca0580c8ab2c24f6c2965d9c9f9c)
- [tm::tm_yday](../posix_system_model_reference/P025_tm_结构体.md#a93a0ba77cc23796df84405dcbcc57eb1)
- [tm::tm_mday](../posix_system_model_reference/P025_tm_结构体.md#ab8d8904bad43b0c8b96e61941c5b5310)
- [tm::tm_min](../posix_system_model_reference/P025_tm_结构体.md#af414eb7c86cc3099595211eee4d4211b)
- [tm::tm_wday](../posix_system_model_reference/P025_tm_结构体.md#afe81a8c46f1c693c43f259b288859f4f)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P047_kinetis_sim.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P049_lwm2m_path.h_源码浏览.md)
