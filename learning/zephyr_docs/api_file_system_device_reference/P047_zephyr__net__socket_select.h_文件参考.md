---
id: learning.zephyr-docs.api-file-system-device-reference.page-47
title: zephyr__net__socket_select.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/socket__select_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第47章\_zephyr\_\_net\_\_socket\_select.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/socket__select_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BSD select支持函数（Support Functions）。

<a id="details"></a>

```c
#include <time.h>
#include <zephyr/toolchain.h>
#include <zephyr/net/socket_types.h>
#include <zephyr/sys/fdtable.h>
```

查看此文件的源码。

BSD select支持函数（Support Functions）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 47.1\_宏定义（Macros）

<a id="r_ga5c88da69b8d9401d3ae02495056f7e23"></a>

```c
#define ZSOCK_FD_SETSIZE ZVFS_FD_SETSIZE
```

相关声明：[ZSOCK_FD_SETSIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga5c88da69b8d9401d3ae02495056f7e23)、[ZVFS_FD_SETSIZE](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#ae8d10dc8bd02e619f8c384c493f53709)。

可添加到 `zsock_fd_set` 中的文件描述符数量。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 47.2\_类型定义（Typedefs）

<a id="r_ga1cdeeddce9000b9fd29b638c422f48f8"></a>

```c
typedef struct zvfs_fd_set zsock_fd_set
```

相关声明：[zvfs_fd_set](../posix_system_model_reference/P032_zvfs_fd_set_结构体.md)、[zsock_fd_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga1cdeeddce9000b9fd29b638c422f48f8)。

套接字文件描述符集合（socket file descriptor set）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 47.3\_函数（Functions）

<a id="r_ga1a065da89061bcb10b10663a9ffbdd10"></a>

```c
static int zsock_select (int nfds, zsock_fd_set *readfds, zsock_fd_set *writefds, zsock_fd_set *exceptfds, struct zsock_timeval *timeout)
```

相关声明：[zsock_select](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga1a065da89061bcb10b10663a9ffbdd10)、[zsock_fd_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga1cdeeddce9000b9fd29b638c422f48f8)、[zsock_fd_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga1cdeeddce9000b9fd29b638c422f48f8)、[zsock_fd_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga1cdeeddce9000b9fd29b638c422f48f8)。

轮询多个套接字事件的传统函数（legacy function）。

<a id="r_gaa4855f07c1329a150f371044e4384490"></a>

```c
static void ZSOCK_FD_ZERO (zsock_fd_set *set)
```

相关声明：[ZSOCK_FD_ZERO](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaa4855f07c1329a150f371044e4384490)、[zsock_fd_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga1cdeeddce9000b9fd29b638c422f48f8)。

初始化并清空 `fd_set`。

<a id="r_gab92b08adccc22a85e7a1c06bf11a88bc"></a>

```c
static int ZSOCK_FD_ISSET (int fd, zsock_fd_set *set)
```

相关声明：[ZSOCK_FD_ISSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gab92b08adccc22a85e7a1c06bf11a88bc)、[zsock_fd_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga1cdeeddce9000b9fd29b638c422f48f8)。

检查套接字是否属于 `fd_set`。

<a id="r_ga7023ec00d24af41a7cbf5f376fb44487"></a>

```c
static void ZSOCK_FD_CLR (int fd, zsock_fd_set *set)
```

相关声明：[ZSOCK_FD_CLR](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga7023ec00d24af41a7cbf5f376fb44487)、[zsock_fd_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga1cdeeddce9000b9fd29b638c422f48f8)。

从 `fd_set` 移除套接字。

<a id="r_ga5d07f52910f6d881295ec659716767f1"></a>

```c
static void ZSOCK_FD_SET (int fd, zsock_fd_set *set)
```

相关声明：[ZSOCK_FD_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga5d07f52910f6d881295ec659716767f1)、[zsock_fd_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga1cdeeddce9000b9fd29b638c422f48f8)。

将套接字添加到 `fd_set`。


## 47.4\_原页交叉引用（Cross References）

- [zephyr/toolchain.h](../api_source_compiler_device_reference/P023_toolchain.h_源码浏览.md)
- [zephyr/net/socket_types.h](../api_source_configuration_reference/P105_socket_types.h_源码浏览.md)
- [zephyr/sys/fdtable.h](../api_source_architecture_reference/P007_fdtable.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P802_socket_select.h_源码浏览.md)
- [ZSOCK_FD_SETSIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga5c88da69b8d9401d3ae02495056f7e23)
- [ZVFS_FD_SETSIZE](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#ae8d10dc8bd02e619f8c384c493f53709)
- [zsock_fd_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga1cdeeddce9000b9fd29b638c422f48f8)
- [zvfs_fd_set](../posix_system_model_reference/P032_zvfs_fd_set_结构体.md)
- [zsock_select](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga1a065da89061bcb10b10663a9ffbdd10)
- [ZSOCK_FD_ZERO](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaa4855f07c1329a150f371044e4384490)
- [fd_set](../api_file_reference/P380_zephyr__posix__sys__select.h_文件参考.md#ae96e561afd32b1445d8a7370f23762a2)
- [ZSOCK_FD_ISSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gab92b08adccc22a85e7a1c06bf11a88bc)
- [ZSOCK_FD_CLR](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga7023ec00d24af41a7cbf5f376fb44487)
- [ZSOCK_FD_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga5d07f52910f6d881295ec659716767f1)

<a id="header-details"></a>

---

[上一章](P046_zephyr__mgmt__mcumgr__transport__smp_bt.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P048_zephyr__drivers__stepper__stepper_trinamic.h_文件参考.md)
