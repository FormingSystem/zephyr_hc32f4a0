---
id: learning.zephyr-docs.api-file-reference.page-306
title: zephyr__posix__poll.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/poll_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第306章\_zephyr\_\_posix\_\_poll.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/poll_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/net/socket.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 306.1\_宏定义（Macros）

<a id="r_af78a57e8ee17b7ecfe4510253d858afd"></a>

```c
#define pollfd zsock_pollfd
```

相关声明：[pollfd](#af78a57e8ee17b7ecfe4510253d858afd)、[zsock_pollfd](../posix_system_model_reference/P030_zsock_pollfd_结构体.md)。

<a id="r_a52ac479a805051f59643588b096024ff"></a>

```c
#define POLLIN ZSOCK_POLLIN
```

相关声明：[POLLIN](#a52ac479a805051f59643588b096024ff)、[ZSOCK_POLLIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga6ade0deb4952e1ea23b368d9eceee9ed)。

<a id="r_ab6f53b89c7a4cc5e8349f7c778d85168"></a>

```c
#define POLLPRI ZSOCK_POLLPRI
```

相关声明：[POLLPRI](#ab6f53b89c7a4cc5e8349f7c778d85168)、[ZSOCK_POLLPRI](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga1c96c16d5000db0fa4b69055ebb97839)。

<a id="r_a91b3c67129ac7675062f316b840a0d58"></a>

```c
#define POLLOUT ZSOCK_POLLOUT
```

相关声明：[POLLOUT](#a91b3c67129ac7675062f316b840a0d58)、[ZSOCK_POLLOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga9ca302c64dfb676798ce03100894ca3e)。

<a id="r_ab1c532446408c98559d4aaaeeeb99820"></a>

```c
#define POLLERR ZSOCK_POLLERR
```

相关声明：[POLLERR](#ab1c532446408c98559d4aaaeeeb99820)、[ZSOCK_POLLERR](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gad44368a112fbf91436a2439e7b767641)。

<a id="r_a262754fe6bdf27c2cd3da43284ec8536"></a>

```c
#define POLLHUP ZSOCK_POLLHUP
```

相关声明：[POLLHUP](#a262754fe6bdf27c2cd3da43284ec8536)、[ZSOCK_POLLHUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gadd341cd5c1f6d7deeaedc5c58dc56fe7)。

<a id="r_ae8bffe35c61e12fb7b408b89721896df"></a>

```c
#define POLLNVAL ZSOCK_POLLNVAL
```

相关声明：[POLLNVAL](#ae8bffe35c61e12fb7b408b89721896df)、[ZSOCK_POLLNVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga45c5b0efca6e09e4f7db78d1d007bf67)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 306.2\_类型定义（Typedefs）

<a id="r_aa49b6bf041fda66eda01c0170243c271"></a>

```c
typedef unsigned int nfds_t
```

相关声明：[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[nfds_t](#aa49b6bf041fda66eda01c0170243c271)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 306.3\_函数（Functions）

<a id="r_afa7e83ddea0ab5b08fcf614b89ac48ba"></a>

```c
int poll (struct zsock_pollfd *fds, int nfds, int timeout)
```

相关声明：[poll](#afa7e83ddea0ab5b08fcf614b89ac48ba)、[zsock_pollfd](../posix_system_model_reference/P030_zsock_pollfd_结构体.md)。

## 306.4\_详细说明（Detailed Documentation）

<a id="ab1c532446408c98559d4aaaeeeb99820"></a>

### `POLLERR`

```c
#define POLLERR ZSOCK_POLLERR
```

<a id="af78a57e8ee17b7ecfe4510253d858afd"></a>

### `pollfd`

```c
#define pollfd zsock_pollfd
```

<a id="a262754fe6bdf27c2cd3da43284ec8536"></a>

### `POLLHUP`

```c
#define POLLHUP ZSOCK_POLLHUP
```

<a id="a52ac479a805051f59643588b096024ff"></a>

### `POLLIN`

```c
#define POLLIN ZSOCK_POLLIN
```

<a id="ae8bffe35c61e12fb7b408b89721896df"></a>

### `POLLNVAL`

```c
#define POLLNVAL ZSOCK_POLLNVAL
```

<a id="a91b3c67129ac7675062f316b840a0d58"></a>

### `POLLOUT`

```c
#define POLLOUT ZSOCK_POLLOUT
```

<a id="ab6f53b89c7a4cc5e8349f7c778d85168"></a>

### `POLLPRI`

```c
#define POLLPRI ZSOCK_POLLPRI
```

<a id="aa49b6bf041fda66eda01c0170243c271"></a>

### `nfds_t`

```c
typedef unsigned int nfds_t
```

<a id="afa7e83ddea0ab5b08fcf614b89ac48ba"></a>

### `poll()`

```c
int poll ( struct zsock_pollfd * fds, int nfds, int timeout )
```


## 306.5\_原页交叉引用（Cross References）

- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P665_poll.h_源码浏览.md)
- [zsock_pollfd](../posix_system_model_reference/P030_zsock_pollfd_结构体.md)
- [ZSOCK_POLLIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga6ade0deb4952e1ea23b368d9eceee9ed)
- [ZSOCK_POLLPRI](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga1c96c16d5000db0fa4b69055ebb97839)
- [ZSOCK_POLLOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga9ca302c64dfb676798ce03100894ca3e)
- [ZSOCK_POLLERR](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gad44368a112fbf91436a2439e7b767641)
- [ZSOCK_POLLHUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gadd341cd5c1f6d7deeaedc5c58dc56fe7)
- [ZSOCK_POLLNVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga45c5b0efca6e09e4f7db78d1d007bf67)
- [unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P305_zephyr__drivers__pinctrl__pinctrl_soc_bflb_common.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P307_zephyr__posix__sys__socket.h_文件参考.md)
