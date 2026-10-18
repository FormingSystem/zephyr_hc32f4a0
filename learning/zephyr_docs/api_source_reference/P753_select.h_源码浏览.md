---
id: learning.zephyr-docs.api-source-reference.page-753
title: select.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/select_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第753章\_select.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/select_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/select_8h.html)。

## 753.1\_原始可见代码（Source Code）

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
<a id="afdtable_8h_html"></a>
<a id="aposix__types_8h_html"></a>
<a id="aselect_8h_html_a0835759308c63ca23a1760980eea21d7"></a>
<a id="aselect_8h_html_a2aed0a9b18a0ac6a3b8bb3ea9c3a34ab"></a>
<a id="aselect_8h_html_a3f88268fa19b2068723de10d848e8a42"></a>
<a id="aselect_8h_html_a7ffa34f8c9a12e7fd43f5ef65bf889fa"></a>
<a id="aselect_8h_html_a8c14b5b455292781fbcc2e34a47923d6"></a>
<a id="aselect_8h_html_ac38fe1ff5db5e46e778f13ad5accdf98"></a>
<a id="aselect_8h_html_ae96e561afd32b1445d8a7370f23762a2"></a>
<a id="astructtimespec_html"></a>
<a id="astructtimeval_html"></a>
<a id="astructzvfs__fd__set_html"></a>

```c
/*
 * Copyright (c) 2019 Linaro Limited
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_POSIX_SYS_SELECT_H_
#define ZEPHYR_INCLUDE_POSIX_SYS_SELECT_H_

#include <zephyr/posix/posix_types.h>
#include <zephyr/sys/fdtable.h>

#ifdef __cplusplus
extern "C" {
#endif

#define FD_SETSIZE ZVFS_FD_SETSIZE

typedef struct zvfs_fd_set fd_set;

struct timeval;

int pselect(int nfds, fd_set *readfds, fd_set *writefds, fd_set *exceptfds,
            const struct timespec *timeout, const void *sigmask);
int select(int nfds, fd_set *readfds, fd_set *writefds, fd_set *errorfds, struct timeval *timeout);
void FD_CLR(int fd, fd_set *fdset);
int FD_ISSET(int fd, fd_set *fdset);
void FD_SET(int fd, fd_set *fdset);
void FD_ZERO(fd_set *fdset);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_POSIX_SYS_SELECT_H_ */
```

## 753.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Linaro Limited。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 34 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_POSIX_SYS_SELECT_H_`。

## 753.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/select_8h.html)
- [zephyr/posix/posix_types.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html)
- [zephyr/sys/fdtable.h](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html)
- [zvfs_fd_set](../posix_system_model_reference/P032_zvfs_fd_set_结构体.md)
- [fd_set](https://docs.zephyrproject.org/latest/doxygen/html/select_8h.html#ae96e561afd32b1445d8a7370f23762a2)
- [timeval](../posix_system_model_reference/P024_timeval_结构体.md)
- [pselect](https://docs.zephyrproject.org/latest/doxygen/html/select_8h.html#a2aed0a9b18a0ac6a3b8bb3ea9c3a34ab)
- [timespec](../time_headers_reference/P005_timespec时间结构.md)
- [select](https://docs.zephyrproject.org/latest/doxygen/html/select_8h.html#a7ffa34f8c9a12e7fd43f5ef65bf889fa)
- [FD_CLR](https://docs.zephyrproject.org/latest/doxygen/html/select_8h.html#a0835759308c63ca23a1760980eea21d7)
- [FD_ISSET](https://docs.zephyrproject.org/latest/doxygen/html/select_8h.html#ac38fe1ff5db5e46e778f13ad5accdf98)
- [FD_SET](https://docs.zephyrproject.org/latest/doxygen/html/select_8h.html#a8c14b5b455292781fbcc2e34a47923d6)
- [FD_ZERO](https://docs.zephyrproject.org/latest/doxygen/html/select_8h.html#a3f88268fa19b2068723de10d848e8a42)
- [fdtable.h](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html)
- [posix_types.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html)

---

[上一章](P752_sdmmc_stm32.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P754_semaphore.h_源码浏览.md)
