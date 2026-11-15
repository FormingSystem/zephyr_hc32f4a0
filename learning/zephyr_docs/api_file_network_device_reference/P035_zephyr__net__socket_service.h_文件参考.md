---
id: learning.zephyr-docs.api-file-network-device-reference.page-35
title: zephyr__net__socket_service.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/socket__service_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_zephyr\_\_net\_\_socket\_service.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/socket__service_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BSD套接字服务（Socket Service）的API。

<a id="details"></a>

```c
#include <sys/types.h>
#include <zephyr/types.h>
#include <zephyr/net/socket.h>
#include <zephyr/logging/log_core.h>
#include <zephyr/syscalls/socket_service.h>
```

查看此文件的源码。

BSD 套接字服务 API（BSD Socket Service API），可用于安装一个 `k_work`，在套接字收到数据时调用。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 35.1\_数据结构（Data Structures）

<a id="r_net_5Fsocket_5Fservice_5Fevent"></a>

```c
struct net_socket_service_event
```

相关声明：[net_socket_service_event](../network_core_model_reference/P124_net_socket_service_event_结构体.md)。

该结构包含由哪个套接字（Socket）触发回调函数调用的信息。

<a id="r_net_5Fsocket_5Fservice_5Fdesc"></a>

```c
struct net_socket_service_desc
```

相关声明：[net_socket_service_desc](../network_core_model_reference/P123_net_socket_service_desc_结构体.md)。

保存套接字服务配置（Socket Service Configuration）信息的主结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 35.2\_宏定义（Macros）

<a id="r_ga424f319f9ccc675f8eeca23cb2c91bc4"></a>

```c
#define NET_SOCKET_SERVICE_SYNC_DEFINE(name, cb, count)
```

相关声明：[NET_SOCKET_SERVICE_SYNC_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__socket__service.html#ga424f319f9ccc675f8eeca23cb2c91bc4)。

静态定义网络套接字服务（Network Socket Service）。

<a id="r_gadee4c786ebf89706a6b0151244b55cc3"></a>

```c
#define NET_SOCKET_SERVICE_SYNC_DEFINE_STATIC(name, cb, count)
```

相关声明：[NET_SOCKET_SERVICE_SYNC_DEFINE_STATIC](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__socket__service.html#gadee4c786ebf89706a6b0151244b55cc3)。

在私有静态作用域（Private Static Scope）中静态定义网络套接字服务。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 35.3\_类型定义（Typedefs）

<a id="r_ga5d9495470c1ade51791df56c59cfb1f5"></a>

```c
typedef void(* net_socket_service_handler_t) (struct net_socket_service_event *pev)
```

相关声明：[net_socket_service_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__socket__service.html#ga5d9495470c1ade51791df56c59cfb1f5)、[net_socket_service_event](../network_core_model_reference/P124_net_socket_service_event_结构体.md)。

网络套接字服务处理函数（Service Handler）的签名。

<a id="r_ga15f0c6f47c7f5e28a26309fe875b92bd"></a>

```c
typedef void(* net_socket_service_cb_t) (const struct net_socket_service_desc *svc, void *user_data)
```

相关声明：[net_socket_service_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__socket__service.html#ga15f0c6f47c7f5e28a26309fe875b92bd)、[net_socket_service_desc](../network_core_model_reference/P123_net_socket_service_desc_结构体.md)。

遍历套接字服务（Socket Services）时使用的回调。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 35.4\_函数（Functions）

<a id="r_gaa72bb82aa413b711e61eda092504b091"></a>

```c
int net_socket_service_register (const struct net_socket_service_desc *service, struct zsock_pollfd *fds, int len, void *user_data)
```

相关声明：[net_socket_service_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__socket__service.html#gaa72bb82aa413b711e61eda092504b091)、[net_socket_service_desc](../network_core_model_reference/P123_net_socket_service_desc_结构体.md)、[zsock_pollfd](../posix_system_model_reference/P030_zsock_pollfd_结构体.md)。

注册可轮询套接字（Pollable Sockets）。

<a id="r_gae2d4eea01c9ea4e6a48315681e05afd6"></a>

```c
static int net_socket_service_unregister (const struct net_socket_service_desc *service)
```

相关声明：[net_socket_service_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__socket__service.html#gae2d4eea01c9ea4e6a48315681e05afd6)、[net_socket_service_desc](../network_core_model_reference/P123_net_socket_service_desc_结构体.md)。

注销可轮询套接字（Pollable Sockets）。

<a id="r_ga0b817d72b63fd3369c6a26723cbbc4fa"></a>

```c
static int net_socket_service_close (const struct net_socket_service_desc *service)
```

相关声明：[net_socket_service_close](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__socket__service.html#ga0b817d72b63fd3369c6a26723cbbc4fa)、[net_socket_service_desc](../network_core_model_reference/P123_net_socket_service_desc_结构体.md)。

注销可轮询套接字（Pollable Sockets），并自动关闭套接字。

<a id="r_gacc78dbe6c186fc86f23ab90943ee3097"></a>

```c
void net_socket_service_foreach (net_socket_service_cb_t cb, void *user_data)
```

相关声明：[net_socket_service_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__socket__service.html#gacc78dbe6c186fc86f23ab90943ee3097)、[net_socket_service_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__socket__service.html#ga15f0c6f47c7f5e28a26309fe875b92bd)。

遍历所有套接字服务（Socket Services），对每项服务调用回调。


## 35.5\_原页交叉引用（Cross References）

- [sys/types.h](../api_source_runtime_reference/P038_types.h_源码浏览.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/net/socket.h](../api_source_socket_ethernet_reference/P006_socket.h_源码浏览.md)
- [zephyr/logging/log_core.h](../log_internal_reference/P002_日志核心头文件源码.md)
- [查看此文件的源码。](../api_source_configuration_reference/P104_socket_service.h_源码浏览.md)
- [net_socket_service_event](../network_core_model_reference/P124_net_socket_service_event_结构体.md)
- [net_socket_service_desc](../network_core_model_reference/P123_net_socket_service_desc_结构体.md)
- [NET_SOCKET_SERVICE_SYNC_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__socket__service.html#ga424f319f9ccc675f8eeca23cb2c91bc4)
- [NET_SOCKET_SERVICE_SYNC_DEFINE_STATIC](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__socket__service.html#gadee4c786ebf89706a6b0151244b55cc3)
- [net_socket_service_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__socket__service.html#ga5d9495470c1ade51791df56c59cfb1f5)
- [net_socket_service_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__socket__service.html#ga15f0c6f47c7f5e28a26309fe875b92bd)
- [net_socket_service_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__socket__service.html#gaa72bb82aa413b711e61eda092504b091)
- [zsock_pollfd](../posix_system_model_reference/P030_zsock_pollfd_结构体.md)
- [net_socket_service_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__socket__service.html#gae2d4eea01c9ea4e6a48315681e05afd6)
- [net_socket_service_close](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__socket__service.html#ga0b817d72b63fd3369c6a26723cbbc4fa)
- [net_socket_service_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__socket__service.html#gacc78dbe6c186fc86f23ab90943ee3097)
- [k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)

<a id="header-details"></a>

---

[上一章](P034_zephyr__net__socket_offload.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P036_zephyr__net__socketcan.h_文件参考.md)
