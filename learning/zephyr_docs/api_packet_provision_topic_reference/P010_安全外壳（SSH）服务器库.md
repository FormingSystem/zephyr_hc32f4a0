---
id: learning.zephyr-docs.api-packet-provision-topic-reference.page-10
title: 安全外壳（SSH）服务器库
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_安全外壳（SSH）服务器库

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

自 4.5 版提供（Since 4.5）；接口版本（Version）0.1.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 10.1\_数据结构（Data Structures）

<a id="r_ssh_5Fserver_5Fevent_5Fclient_5Fconnected"></a>

```c
struct ssh_server_event_client_connected
```

相关声明：[ssh_server_event_client_connected](../network_service_model_reference/P062_ssh_server_event_client_connected_结构体.md)。

客户端连接（Client Connection）的传输数据。

<a id="r_ssh_5Fserver_5Fevent_5Fclient_5Fdisconnected"></a>

```c
struct ssh_server_event_client_disconnected
```

相关声明：[ssh_server_event_client_disconnected](../network_service_model_reference/P063_ssh_server_event_client_disconnected_结构体.md)。

客户端断开连接（Client Disconnection）的传输数据。

<a id="r_ssh_5Fserver_5Fevent"></a>

```c
struct ssh_server_event
```

相关声明：[ssh_server_event](../network_service_model_reference/P061_ssh_server_event_结构体.md)。

SSH服务器事件（Server Event）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 10.2\_类型定义（Typedefs）

<a id="r_ga72953be174ebb5a948815f49d083105a"></a>

```c
typedef int(* ssh_server_event_callback_t) (struct ssh_server *sshd, const struct ssh_server_event *event, void *user_data)
```

相关声明：[ssh_server_event_callback_t](#ga72953be174ebb5a948815f49d083105a)、[ssh_server_event](../network_service_model_reference/P061_ssh_server_event_结构体.md)。

安全外壳（SSH）服务器事件的回调函数类型。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 10.3\_枚举（Enumerations）

<a id="r_ga38729e64c5c13a3df058fba5481f56cd"></a>

```c
enum ssh_server_event_type { SSH_SERVER_EVENT_CLOSED , SSH_SERVER_EVENT_CLIENT_CONNECTED , SSH_SERVER_EVENT_CLIENT_DISCONNECTED }
```

相关声明：[ssh_server_event_type](#ga38729e64c5c13a3df058fba5481f56cd)、[SSH_SERVER_EVENT_CLOSED](#gga38729e64c5c13a3df058fba5481f56cda85d7f17dcdf41768d7fad6f356a9fc78)、[SSH_SERVER_EVENT_CLIENT_CONNECTED](#gga38729e64c5c13a3df058fba5481f56cda1eca79d603a6aa92a27eb0e636c34149)、[SSH_SERVER_EVENT_CLIENT_DISCONNECTED](#gga38729e64c5c13a3df058fba5481f56cda127d2b9f2843207f6f206147a21b2c29)。

服务器事件类型（Server Event Types）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 10.4\_函数（Functions）

<a id="r_ga017b274d7604ecca118aab5060bdfd7b"></a>

```c
int ssh_server_start (struct ssh_server *sshd, const struct net_sockaddr *bind_addr, int host_key_index, const char *username, const char *password, const int *authorized_keys, size_t authorized_keys_len, ssh_server_event_callback_t server_callback, ssh_transport_event_callback_t transport_callback, void *user_data)
```

相关声明：[ssh_server_start](#ga017b274d7604ecca118aab5060bdfd7b)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[ssh_server_event_callback_t](#ga72953be174ebb5a948815f49d083105a)、[ssh_transport_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gaed450ebb53a676fafc58bb6cfe82a448)。

启动安全外壳（SSH）服务器。

<a id="r_ga0ceb09a44c1d659d85f51dc5b842cef6"></a>

```c
int ssh_server_stop (struct ssh_server *sshd)
```

相关声明：[ssh_server_stop](#ga0ceb09a44c1d659d85f51dc5b842cef6)。

停止安全外壳（SSH）服务器。

<a id="r_gacd16569ffbf5b87530d27d9eba6229d4"></a>

```c
int ssh_server_transport_close (struct ssh_server *sshd, int idx)
```

相关声明：[ssh_server_transport_close](#gacd16569ffbf5b87530d27d9eba6229d4)。

关闭 SSH 服务器传输连接（Transport Connection）。

<a id="r_gad14ab0c8d54711b60e73ff7d0409b9d9"></a>

```c
int ssh_server_register_transport_callback (struct ssh_transport_conf *conf)
```

相关声明：[ssh_server_register_transport_callback](#gad14ab0c8d54711b60e73ff7d0409b9d9)、[ssh_transport_conf](../network_service_model_reference/P064_ssh_transport_conf_结构体.md)。

注册用于获取客户端连接所关联传输（Transport）的回调函数。

<a id="r_ga76a0afc5f12f7b3a7133c0e759a0bb25"></a>

```c
int ssh_server_unregister_transport_callback (struct ssh_transport_conf *conf)
```

相关声明：[ssh_server_unregister_transport_callback](#ga76a0afc5f12f7b3a7133c0e759a0bb25)、[ssh_transport_conf](../network_service_model_reference/P064_ssh_transport_conf_结构体.md)。

注销用于获取客户端连接所关联传输（Transport）的回调函数。

<a id="r_ga41202a4f05c23393071d71df948fc91d"></a>

```c
struct ssh_server * ssh_transport_get_server (struct ssh_transport *transport)
```

相关声明：[ssh_transport_get_server](#ga41202a4f05c23393071d71df948fc91d)。

获取拥有指定传输（Transport）的 SSH 服务器实例。

## 10.5\_详细说明（Detailed Documentation）

<a id="ga72953be174ebb5a948815f49d083105a"></a>

### `ssh_server_event_callback_t`

```c
typedef int(* ssh_server_event_callback_t) (struct ssh_server *sshd, const struct ssh_server_event *event, void *user_data)
```

```c
#include <zephyr/net/ssh/server.h>
```

安全外壳（SSH）服务器事件的回调函数类型。

SSH 服务器调用此回调，通知应用与客户端连接和断开相关的各种事件。回调接收 SSH 服务器实例指针、包含事件详细信息的结构体，以及服务器初始化时提供的用户数据（User Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sshd` | 指向正在调用此回调的 SSH 服务器实例（Server Instance）的指针。 |
| `event` | 指向包含所发生事件详细信息的结构体的指针。 |
| `user_data` | 指向服务器启动时提供的用户自定义数据（User-defined Data）的指针。 |

**返回（Returns）**：返回值：成功返回 0，非零值表示错误。

<a id="ga38729e64c5c13a3df058fba5481f56cd"></a>

### `ssh_server_event_type`

```c
enum ssh_server_event_type
```

```c
#include <zephyr/net/ssh/server.h>
```

服务器事件类型（Server Event Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SSH_SERVER_EVENT_CLOSED` | 服务器已关闭（Closed）。 |
| `SSH_SERVER_EVENT_CLIENT_CONNECTED` | 客户端已连接到服务器（Connected）。 |
| `SSH_SERVER_EVENT_CLIENT_DISCONNECTED` | 客户端已从服务器断开（Disconnected）。 |

<a id="gad14ab0c8d54711b60e73ff7d0409b9d9"></a>

### `ssh_server_register_transport_callback()`

```c
int ssh_server_register_transport_callback ( struct ssh_transport_conf * conf)
```

```c
#include <zephyr/net/ssh/server.h>
```

注册用于获取客户端连接所关联传输（Transport）的回调函数。

注册的回调用于服务器侧传输事件（Server-side Transport Events）。服务器角色只会发出以下事件类型：

- 客户端请求打开新通道时，产生 `SSH_TRANSPORT_EVENT_CHANNEL_OPEN` 事件。
- 传输对象被拆除（Torn Down）时，发出 `SSH_TRANSPORT_EVENT_CLOSED`。

忽略回调返回值；回调作为观察者（Observer），无法影响传输流程（Transport Flow）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conf` | 传输回调配置数据（Transport Callback Configuration Data）。此结构体必须保持有效，直到被注销。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga017b274d7604ecca118aab5060bdfd7b"></a>

### `ssh_server_start()`

```c
int ssh_server_start ( struct ssh_server * sshd, const struct net_sockaddr * bind_addr, int host_key_index, const char * username, const char * password, const int * authorized_keys, size_t authorized_keys_len, ssh_server_event_callback_t server_callback, ssh_transport_event_callback_t transport_callback, void * user_data )
```

```c
#include <zephyr/net/ssh/server.h>
```

启动安全外壳（SSH）服务器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sshd` | 指向要启动的 SSH 服务器实例（Server Instance）的指针。 |
| `bind_addr` | SSH 服务器要绑定的网络地址（Network Address）。 |
| `host_key_index` | SSH 服务器要使用的主机密钥索引（Host Key Index）。 |
| `username` | SSH 认证用户名（Authentication Username）。设为 `NULL` 或空字符串时，允许传入连接使用任意用户名。 |
| `password` | SSH 认证密码（Authentication Password）。设为 `NULL` 或空字符串时禁用密码认证。 |
| `authorized_keys` | 已授权公钥索引数组（Authorized Public Key Indices）。设为 `NULL` 时禁用公钥认证。 |
| `authorized_keys_len` | `authorized_keys` 数组长度。 |
| `server_callback` | 处理 SSH 服务器事件（Server Events）的回调函数。 |
| `transport_callback` | 处理 SSH 传输事件（Transport Events）的回调函数。 |
| `user_data` | 指向要传给回调函数的用户自定义数据（User-defined Data）的指针。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga0ceb09a44c1d659d85f51dc5b842cef6"></a>

### `ssh_server_stop()`

```c
int ssh_server_stop ( struct ssh_server * sshd)
```

```c
#include <zephyr/net/ssh/server.h>
```

停止安全外壳（SSH）服务器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sshd` | 指向要停止的 SSH 服务器实例（Server Instance）的指针。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="gacd16569ffbf5b87530d27d9eba6229d4"></a>

### `ssh_server_transport_close()`

```c
int ssh_server_transport_close ( struct ssh_server * sshd, int idx )
```

```c
#include <zephyr/net/ssh/server.h>
```

关闭 SSH 服务器传输连接（Transport Connection）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sshd` | 指向 SSH 服务器实例（Server Instance）的指针。 |
| `idx` | 要关闭的传输连接索引（Transport Connection Index）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga76a0afc5f12f7b3a7133c0e759a0bb25"></a>

### `ssh_server_unregister_transport_callback()`

```c
int ssh_server_unregister_transport_callback ( struct ssh_transport_conf * conf)
```

```c
#include <zephyr/net/ssh/server.h>
```

注销用于获取客户端连接所关联传输（Transport）的回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conf` | 传输回调配置数据（Transport Callback Configuration Data）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga41202a4f05c23393071d71df948fc91d"></a>

### `ssh_transport_get_server()`

```c
struct ssh_server * ssh_transport_get_server ( struct ssh_transport * transport)
```

```c
#include <zephyr/net/ssh/server.h>
```

获取拥有指定传输（Transport）的 SSH 服务器实例。

已注册的传输回调会全局接收所有服务器实例的事件，因此可在其中使用此函数，确定某个传输属于哪个服务器实例。只能对从服务器传输回调（Server Transport Callback）取得的传输调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `transport` | 要查询其所属服务器的传输（Transport）。 |

**返回（Returns）**：返回值：指向所属 SSH 服务器实例的指针；若传输为 `NULL`，则返回 `NULL`。


## 10.6\_原页交叉引用（Cross References）

- [ssh_server_event_client_connected](../network_service_model_reference/P062_ssh_server_event_client_connected_结构体.md)
- [ssh_server_event_client_disconnected](../network_service_model_reference/P063_ssh_server_event_client_disconnected_结构体.md)
- [ssh_server_event](../network_service_model_reference/P061_ssh_server_event_结构体.md)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [ssh_transport_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gaed450ebb53a676fafc58bb6cfe82a448)
- [ssh_transport_conf](../network_service_model_reference/P064_ssh_transport_conf_结构体.md)
- [zephyr/net/ssh/server.h](../api_file_service_interface_reference/P048_zephyr__net__ssh__server.h_文件参考.md)
- [SSH_TRANSPORT_EVENT_CHANNEL_OPEN](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga578aed0a10600bc7a248dbb64ca13cc2afb8adfb3fd445e92d74a93f3ec0663c9)
- [SSH_TRANSPORT_EVENT_CLOSED](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga578aed0a10600bc7a248dbb64ca13cc2a75fcdde91f09ec0599575054300d90e8)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga38729e64c5c13a3df058fba5481f56cda85d7f17dcdf41768d7fad6f356a9fc78"></a>
<a id="gga38729e64c5c13a3df058fba5481f56cda1eca79d603a6aa92a27eb0e636c34149"></a>
<a id="gga38729e64c5c13a3df058fba5481f56cda127d2b9f2843207f6f206147a21b2c29"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P009_引脚控制协议（Pin Control Protocol）.md) · [返回大纲](大纲.md)
