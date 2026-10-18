---
id: learning.zephyr-docs.api-file-reference.page-380
title: zephyr__posix__sys__select.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/select_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第380章\_zephyr\_\_posix\_\_sys\_\_select.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/select_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/posix/posix_types.h>
#include <zephyr/sys/fdtable.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 380.1\_宏定义（Macros）

<a id="r_a86c5dbf5a99358e288f573d6a1e0873f"></a>

```c
#define FD_SETSIZE ZVFS_FD_SETSIZE
```

相关声明：[FD_SETSIZE](#a86c5dbf5a99358e288f573d6a1e0873f)、[ZVFS_FD_SETSIZE](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#ae8d10dc8bd02e619f8c384c493f53709)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 380.2\_类型定义（Typedefs）

<a id="r_ae96e561afd32b1445d8a7370f23762a2"></a>

```c
typedef struct zvfs_fd_set fd_set
```

相关声明：[zvfs_fd_set](../posix_system_model_reference/P032_zvfs_fd_set_结构体.md)、[fd_set](#ae96e561afd32b1445d8a7370f23762a2)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 380.3\_函数（Functions）

<a id="r_a2aed0a9b18a0ac6a3b8bb3ea9c3a34ab"></a>

```c
int pselect (int nfds, fd_set *readfds, fd_set *writefds, fd_set *exceptfds, const struct timespec *timeout, const void *sigmask)
```

相关声明：[pselect](#a2aed0a9b18a0ac6a3b8bb3ea9c3a34ab)、[fd_set](#ae96e561afd32b1445d8a7370f23762a2)、[fd_set](#ae96e561afd32b1445d8a7370f23762a2)、[fd_set](#ae96e561afd32b1445d8a7370f23762a2)、[timespec](../time_headers_reference/P005_timespec时间结构.md)。

<a id="r_a7ffa34f8c9a12e7fd43f5ef65bf889fa"></a>

```c
int select (int nfds, fd_set *readfds, fd_set *writefds, fd_set *errorfds, struct timeval *timeout)
```

相关声明：[select](#a7ffa34f8c9a12e7fd43f5ef65bf889fa)、[fd_set](#ae96e561afd32b1445d8a7370f23762a2)、[fd_set](#ae96e561afd32b1445d8a7370f23762a2)、[fd_set](#ae96e561afd32b1445d8a7370f23762a2)、[timeval](../posix_system_model_reference/P024_timeval_结构体.md)。

<a id="r_a0835759308c63ca23a1760980eea21d7"></a>

```c
void FD_CLR (int fd, fd_set *fdset)
```

相关声明：[FD_CLR](#a0835759308c63ca23a1760980eea21d7)、[fd_set](#ae96e561afd32b1445d8a7370f23762a2)。

<a id="r_ac38fe1ff5db5e46e778f13ad5accdf98"></a>

```c
int FD_ISSET (int fd, fd_set *fdset)
```

相关声明：[FD_ISSET](#ac38fe1ff5db5e46e778f13ad5accdf98)、[fd_set](#ae96e561afd32b1445d8a7370f23762a2)。

<a id="r_a8c14b5b455292781fbcc2e34a47923d6"></a>

```c
void FD_SET (int fd, fd_set *fdset)
```

相关声明：[FD_SET](#a8c14b5b455292781fbcc2e34a47923d6)、[fd_set](#ae96e561afd32b1445d8a7370f23762a2)。

<a id="r_a3f88268fa19b2068723de10d848e8a42"></a>

```c
void FD_ZERO (fd_set *fdset)
```

相关声明：[FD_ZERO](#a3f88268fa19b2068723de10d848e8a42)、[fd_set](#ae96e561afd32b1445d8a7370f23762a2)。

## 380.4\_详细说明（Detailed Documentation）

<a id="a86c5dbf5a99358e288f573d6a1e0873f"></a>

### `FD_SETSIZE`

```c
#define FD_SETSIZE ZVFS_FD_SETSIZE
```

<a id="ae96e561afd32b1445d8a7370f23762a2"></a>

### `fd_set`

```c
typedef struct zvfs_fd_set fd_set
```

<a id="a0835759308c63ca23a1760980eea21d7"></a>

### `FD_CLR()`

```c
void FD_CLR ( int fd, fd_set * fdset )
```

<a id="ac38fe1ff5db5e46e778f13ad5accdf98"></a>

### `FD_ISSET()`

```c
int FD_ISSET ( int fd, fd_set * fdset )
```

<a id="a8c14b5b455292781fbcc2e34a47923d6"></a>

### `FD_SET()`

```c
void FD_SET ( int fd, fd_set * fdset )
```

<a id="a3f88268fa19b2068723de10d848e8a42"></a>

### `FD_ZERO()`

```c
void FD_ZERO ( fd_set * fdset)
```

<a id="a2aed0a9b18a0ac6a3b8bb3ea9c3a34ab"></a>

### `pselect()`

```c
int pselect ( int nfds, fd_set * readfds, fd_set * writefds, fd_set * exceptfds, const struct timespec * timeout, const void * sigmask )
```

<a id="a7ffa34f8c9a12e7fd43f5ef65bf889fa"></a>

### `select()`

```c
int select ( int nfds, fd_set * readfds, fd_set * writefds, fd_set * errorfds, struct timeval * timeout )
```


## 380.5\_原页交叉引用（Cross References）

- [zephyr/posix/posix_types.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h_source.html)
- [zephyr/sys/fdtable.h](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P753_select.h_源码浏览.md)
- [ZVFS_FD_SETSIZE](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#ae8d10dc8bd02e619f8c384c493f53709)
- [zvfs_fd_set](../posix_system_model_reference/P032_zvfs_fd_set_结构体.md)
- [timespec](../time_headers_reference/P005_timespec时间结构.md)
- [timeval](../posix_system_model_reference/P024_timeval_结构体.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P379_zephyr__linker__section_tags.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P381_zephyr__posix__semaphore.h_文件参考.md)
