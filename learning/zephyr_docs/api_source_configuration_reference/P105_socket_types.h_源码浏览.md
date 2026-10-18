---
id: learning.zephyr-docs.api-source-configuration-reference.page-105
title: socket_types.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/socket__types_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第105章\_socket\_types.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/socket__types_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/socket__types_8h.html)。

## 105.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
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
<a id="l00062"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="a__timespec_8h_html_aa17c461cd5eca7fc12a66daa803c7fd7"></a>
<a id="a__timespec_8h_html_ad7acf95ceafb15a1d8d86af0c4982995"></a>
<a id="a__timeval_8h_html"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="astructtimeval_html"></a>
<a id="astructtimeval_html_a810bf8fcd58e255a5c1896d19538b86a"></a>
<a id="astructtimeval_html_aef6ddab1064c430758f9f913b7e4a21e"></a>

```c
/*
 * Copyright (c) 2021 Nordic Semiconductor
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_SOCKET_TYPES_H_
#define ZEPHYR_INCLUDE_NET_SOCKET_TYPES_H_


#include <zephyr/types.h>


#ifdef CONFIG_NEWLIB_LIBC

#include <newlib.h>

#ifdef __NEWLIB__
#include <sys/_timeval.h>
#else /* __NEWLIB__ */
#include <sys/types.h>
/* workaround for older Newlib 2.x, as it lacks sys/_timeval.h */
struct timeval {
        time_t tv_sec;
        suseconds_t tv_usec;
};
#endif /* __NEWLIB__ */

#else /* CONFIG_NEWLIB_LIBC */

#if defined(CONFIG_NATIVE_LIBC)
#include <bits/types/struct_timeval.h>
#else
#include <sys/_timeval.h>
#endif

#endif /* CONFIG_NEWLIB_LIBC */

#ifdef __cplusplus
extern "C" {
#endif

#define zsock_timeval timeval

#ifdef __cplusplus
}
#endif



#endif /* ZEPHYR_INCLUDE_NET_SOCKET_TYPES_H_ */
```

## 105.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 Nordic Semiconductor。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 32 行

条件编译标记：`__NEWLIB__`。

### 注释 3：原第 34 行

针对较旧 Newlib 2.x 的变通处理，因为该版本缺少 `sys/_timeval.h`。

### 注释 4：原第 39 行

条件编译标记：`__NEWLIB__`。

### 注释 5：原第 41 行

条件编译配置（Configuration）标记：`CONFIG_NEWLIB_LIBC`。

### 注释 6：原第 49 行

条件编译配置（Configuration）标记：`CONFIG_NEWLIB_LIBC`。

### 注释 7：原第 67 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_SOCKET_TYPES_H_`。

## 105.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/socket__types_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [sys/_timeval.h](https://docs.zephyrproject.org/latest/doxygen/html/__timeval_8h.html)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [timeval](../posix_system_model_reference/P024_timeval_结构体.md)
- [time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)
- [tv_sec](../posix_system_model_reference/P024_timeval_结构体.md#aef6ddab1064c430758f9f913b7e4a21e)
- [suseconds_t](../time_headers_reference/P003_timespec类型头文件参考.md#ad7acf95ceafb15a1d8d86af0c4982995)
- [tv_usec](../posix_system_model_reference/P024_timeval_结构体.md#a810bf8fcd58e255a5c1896d19538b86a)
- [_timeval.h](https://docs.zephyrproject.org/latest/doxygen/html/__timeval_8h.html)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [timeval::tv_usec](../posix_system_model_reference/P024_timeval_结构体.md#a810bf8fcd58e255a5c1896d19538b86a)
- [timeval::tv_sec](../posix_system_model_reference/P024_timeval_结构体.md#aef6ddab1064c430758f9f913b7e4a21e)

---

[上一章](P104_socket_service.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P106_stats.h_源码浏览.md)
