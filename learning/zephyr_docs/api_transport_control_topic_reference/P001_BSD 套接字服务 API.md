---
id: learning.zephyr-docs.api-transport-control-topic-reference.page-1
title: BSD 套接字服务 API
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__socket__service.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_BSD 套接字服务 API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__socket__service.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BSD 套接字服务 API

<a id="details"></a>

BSD 套接字服务（Socket Service）API。**引入版本（Since）：**3.6。**版本（Version）：**0.2.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

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

## 1.2\_宏定义（Macros）

<a id="r_ga424f319f9ccc675f8eeca23cb2c91bc4"></a>

```c
#define NET_SOCKET_SERVICE_SYNC_DEFINE(name, cb, count)
```

相关声明：[NET_SOCKET_SERVICE_SYNC_DEFINE](#ga424f319f9ccc675f8eeca23cb2c91bc4)。

静态定义网络套接字服务（Network Socket Service）。

<a id="r_gadee4c786ebf89706a6b0151244b55cc3"></a>

```c
#define NET_SOCKET_SERVICE_SYNC_DEFINE_STATIC(name, cb, count)
```

相关声明：[NET_SOCKET_SERVICE_SYNC_DEFINE_STATIC](#gadee4c786ebf89706a6b0151244b55cc3)。

在私有静态作用域（Private Static Scope）中静态定义网络套接字服务。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.3\_类型定义（Typedefs）

<a id="r_ga5d9495470c1ade51791df56c59cfb1f5"></a>

```c
typedef void(* net_socket_service_handler_t) (struct net_socket_service_event *pev)
```

相关声明：[net_socket_service_handler_t](#ga5d9495470c1ade51791df56c59cfb1f5)、[net_socket_service_event](../network_core_model_reference/P124_net_socket_service_event_结构体.md)。

网络套接字服务处理函数（Service Handler）的签名。

<a id="r_ga15f0c6f47c7f5e28a26309fe875b92bd"></a>

```c
typedef void(* net_socket_service_cb_t) (const struct net_socket_service_desc *svc, void *user_data)
```

相关声明：[net_socket_service_cb_t](#ga15f0c6f47c7f5e28a26309fe875b92bd)、[net_socket_service_desc](../network_core_model_reference/P123_net_socket_service_desc_结构体.md)。

遍历套接字服务（Socket Services）时使用的回调。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.4\_函数（Functions）

<a id="r_gaa72bb82aa413b711e61eda092504b091"></a>

```c
int net_socket_service_register (const struct net_socket_service_desc *service, struct zsock_pollfd *fds, int len, void *user_data)
```

相关声明：[net_socket_service_register](#gaa72bb82aa413b711e61eda092504b091)、[net_socket_service_desc](../network_core_model_reference/P123_net_socket_service_desc_结构体.md)、[zsock_pollfd](../posix_system_model_reference/P030_zsock_pollfd_结构体.md)。

注册可轮询套接字（Pollable Sockets）。

<a id="r_gae2d4eea01c9ea4e6a48315681e05afd6"></a>

```c
static int net_socket_service_unregister (const struct net_socket_service_desc *service)
```

相关声明：[net_socket_service_unregister](#gae2d4eea01c9ea4e6a48315681e05afd6)、[net_socket_service_desc](../network_core_model_reference/P123_net_socket_service_desc_结构体.md)。

注销可轮询套接字（Pollable Sockets）。

<a id="r_ga0b817d72b63fd3369c6a26723cbbc4fa"></a>

```c
static int net_socket_service_close (const struct net_socket_service_desc *service)
```

相关声明：[net_socket_service_close](#ga0b817d72b63fd3369c6a26723cbbc4fa)、[net_socket_service_desc](../network_core_model_reference/P123_net_socket_service_desc_结构体.md)。

注销可轮询套接字（Pollable Sockets），并自动关闭套接字。

<a id="r_gacc78dbe6c186fc86f23ab90943ee3097"></a>

```c
void net_socket_service_foreach (net_socket_service_cb_t cb, void *user_data)
```

相关声明：[net_socket_service_foreach](#gacc78dbe6c186fc86f23ab90943ee3097)、[net_socket_service_cb_t](#ga15f0c6f47c7f5e28a26309fe875b92bd)。

遍历所有套接字服务（Socket Services），对每项服务调用回调。

## 1.5\_详细说明（Detailed Documentation）

<a id="ga424f319f9ccc675f8eeca23cb2c91bc4"></a>

### `NET_SOCKET_SERVICE_SYNC_DEFINE`

```c
#define NET_SOCKET_SERVICE_SYNC_DEFINE ( name, cb, count )
```

```c
#include <zephyr/net/socket_service.h>
```

展开值（Value）：

```c
__z_net_socket_service_define(name, cb, count)
```

静态定义网络套接字服务（Network Socket Service）。

此服务同步调用用户回调（User Callback）：服务 API 会等待用户回调返回，然后才继续处理下一个套接字服务（Socket Service）。

可使用以下方式，从定义此套接字服务（Socket Service）的模块之外访问它：

原始示例（Example）：

```c
extern struct net_socket_service_desc <name>;
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 服务名称（Service Name）。 |
| `cb` | 出现套接字活动（Socket Activity）时调用的回调函数。 |
| `count` | 此服务所需的可轮询套接字（Pollable Sockets）数量。 |

**说明（Note）**：**注意（Note）：**此宏不能与 `static` 关键字一起使用。如需这种用法，请改用 `NET_SOCKET_SERVICE_SYNC_DEFINE_STATIC`。

<a id="gadee4c786ebf89706a6b0151244b55cc3"></a>

### `NET_SOCKET_SERVICE_SYNC_DEFINE_STATIC`

```c
#define NET_SOCKET_SERVICE_SYNC_DEFINE_STATIC ( name, cb, count )
```

```c
#include <zephyr/net/socket_service.h>
```

展开值（Value）：

```c
__z_net_socket_service_define(name, cb, count, static)
```

在私有静态作用域（Private Static Scope）中静态定义网络套接字服务。

此服务同步调用用户回调（User Callback）：服务 API 会等待用户回调返回，然后才继续处理下一个套接字服务（Socket Service）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 服务名称（Service Name）。 |
| `cb` | 出现套接字活动（Socket Activity）时调用的回调函数。 |
| `count` | 此服务所需的可轮询套接字（Pollable Sockets）数量。 |

<a id="ga15f0c6f47c7f5e28a26309fe875b92bd"></a>

### `net_socket_service_cb_t`

```c
typedef void(* net_socket_service_cb_t) (const struct net_socket_service_desc *svc, void *user_data)
```

```c
#include <zephyr/net/socket_service.h>
```

遍历套接字服务（Socket Services）时使用的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `svc` | 指向当前套接字服务（Socket Service）的指针。 |
| `user_data` | 指向用户数据的有效指针，或为 `NULL`。 |

<a id="ga5d9495470c1ade51791df56c59cfb1f5"></a>

### `net_socket_service_handler_t`

```c
typedef void(* net_socket_service_handler_t) (struct net_socket_service_event *pev)
```

```c
#include <zephyr/net/socket_service.h>
```

网络套接字服务处理函数（Service Handler）的签名。

套接字服务（Socket Service）将调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pev` | 提供处理程序（Handler）的套接字服务事件（Socket Service Event）。 |

<a id="ga0b817d72b63fd3369c6a26723cbbc4fa"></a>

### `net_socket_service_close()`

```c
int net_socket_service_close ( const struct net_socket_service_desc * service)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/socket_service.h>
```

注销可轮询套接字（Pollable Sockets），并自动关闭套接字。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `service` | 指向服务描述（Service Description）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 无错误（No Error）。 |
| `-ENOENT` | 未找到服务（Service）。 |
| `-EINVAL` | 参数无效（Invalid Parameter）。 |

<a id="gacc78dbe6c186fc86f23ab90943ee3097"></a>

### `net_socket_service_foreach()`

```c
void net_socket_service_foreach ( net_socket_service_cb_t cb, void * user_data )
```

```c
#include <zephyr/net/socket_service.h>
```

遍历所有套接字服务（Socket Services），对每项服务调用回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 要调用的用户提供回调函数。 |
| `user_data` | 用户指定的数据。 |

<a id="gaa72bb82aa413b711e61eda092504b091"></a>

### `net_socket_service_register()`

```c
int net_socket_service_register ( const struct net_socket_service_desc * service, struct zsock_pollfd * fds, int len, void * user_data )
```

```c
#include <zephyr/net/socket_service.h>
```

注册可轮询套接字（Pollable Sockets）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `service` | 指向服务描述（Service Description）的指针。 |
| `fds` | 要轮询（Poll）的套接字数组（Socket Array）。 |
| `len` | 套接字数组（Socket Array）的长度。 |
| `user_data` | 用户专用数据（User Specific Data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 无错误（No Error）。 |
| `-ENOENT` | 未找到服务（Service）。 |
| `-EINVAL` | 参数无效（Invalid Parameter）。 |

<a id="gae2d4eea01c9ea4e6a48315681e05afd6"></a>

### `net_socket_service_unregister()`

```c
int net_socket_service_unregister ( const struct net_socket_service_desc * service)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/socket_service.h>
```

注销可轮询套接字（Pollable Sockets）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `service` | 指向服务描述（Service Description）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 无错误（No Error）。 |
| `-ENOENT` | 未找到服务（Service）。 |
| `-EINVAL` | 参数无效（Invalid Parameter）。 |


## 1.6\_原页交叉引用（Cross References）

- [net_socket_service_event](../network_core_model_reference/P124_net_socket_service_event_结构体.md)
- [net_socket_service_desc](../network_core_model_reference/P123_net_socket_service_desc_结构体.md)
- [zsock_pollfd](../posix_system_model_reference/P030_zsock_pollfd_结构体.md)
- [zephyr/net/socket_service.h](../api_file_network_device_reference/P035_zephyr__net__socket_service.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astructnet__socket__service__desc_html"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_通用对象交换规范（Generic Object Exchange Profile，GOEP）.md)
