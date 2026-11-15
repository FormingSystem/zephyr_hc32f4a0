---
id: learning.zephyr-docs.api-source-supplement-reference.page-93
title: time.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2posix_2sys_2time_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第93章\_time.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2posix_2sys_2time_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2posix_2sys_2time_8h.html)。

## 93.1\_原始可见代码（Source Code）

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
<a id="a__timespec_8h_html_aa17c461cd5eca7fc12a66daa803c7fd7"></a>
<a id="a__timespec_8h_html_ad7acf95ceafb15a1d8d86af0c4982995"></a>
<a id="a__timeval_8h_html"></a>
<a id="ainclude_2zephyr_2posix_2sys_2time_8h_html_a2f316a4ad94a242df56b01953677015d"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="astructtimeval_html"></a>
<a id="astructtimeval_html_a810bf8fcd58e255a5c1896d19538b86a"></a>
<a id="astructtimeval_html_aef6ddab1064c430758f9f913b7e4a21e"></a>

```c
/*
 * Copyright (c) 2019 Linaro Limited
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_POSIX_SYS_TIME_H_
#define ZEPHYR_INCLUDE_POSIX_SYS_TIME_H_

#ifdef CONFIG_NEWLIB_LIBC
/* Kludge to support outdated newlib version as used in SDK 0.10 for Xtensa */
#include <newlib.h>

#ifdef __NEWLIB__
#include <sys/_timeval.h>
#else
#include <sys/types.h>
struct timeval {
        time_t tv_sec;
        suseconds_t tv_usec;
};
#endif

#else
#include <sys/types.h>
#include <sys/_timeval.h>
#endif /* CONFIG_NEWLIB_LIBC */

#ifdef __cplusplus
extern "C" {
#endif

int gettimeofday(struct timeval *tv, void *tz);

#ifdef __cplusplus
}
#endif

#endif  /* ZEPHYR_INCLUDE_POSIX_SYS_TIME_H_ */
```

## 93.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Linaro Limited。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 11 行

用于支持 Xtensa SDK 0.10 所采用的过时 newlib 版本的临时变通处理（Kludge）。

### 注释 3：原第 27 行

条件编译配置（Configuration）标记：`CONFIG_NEWLIB_LIBC`。

### 注释 4：原第 39 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_POSIX_SYS_TIME_H_`。

## 93.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2posix_2sys_2time_8h.html)
- [sys/_timeval.h](https://docs.zephyrproject.org/latest/doxygen/html/__timeval_8h.html)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [timeval](../posix_system_model_reference/P024_timeval_结构体.md)
- [time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)
- [tv_sec](../posix_system_model_reference/P024_timeval_结构体.md#aef6ddab1064c430758f9f913b7e4a21e)
- [suseconds_t](../time_headers_reference/P003_timespec类型头文件参考.md#ad7acf95ceafb15a1d8d86af0c4982995)
- [tv_usec](../posix_system_model_reference/P024_timeval_结构体.md#a810bf8fcd58e255a5c1896d19538b86a)
- [gettimeofday](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2posix_2sys_2time_8h.html#a2f316a4ad94a242df56b01953677015d)
- [_timeval.h](https://docs.zephyrproject.org/latest/doxygen/html/__timeval_8h.html)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [timeval::tv_usec](../posix_system_model_reference/P024_timeval_结构体.md#a810bf8fcd58e255a5c1896d19538b86a)
- [timeval::tv_sec](../posix_system_model_reference/P024_timeval_结构体.md#aef6ddab1064c430758f9f913b7e4a21e)

---

[上一章](P092_imx_spc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P094_types.h_源码浏览.md)
