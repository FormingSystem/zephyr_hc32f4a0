---
id: learning.zephyr-docs.api-lifecycle-capability-topic-reference.page-21
title: 安全外壳（SSH）客户端库
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__client.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_安全外壳（SSH）客户端库

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__client.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

自 4.5 版提供（Since 4.5）；接口版本（Version）0.1.0。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 21.1\_函数（Functions）

<a id="r_ga44a3e816f22b34290374158f4cd8702b"></a>

```c
int ssh_client_start (struct ssh_client *ssh, const char *user_name, const struct net_sockaddr *addr, int host_key_index, ssh_transport_event_callback_t callback, void *user_data)
```

相关声明：[ssh_client_start](#ga44a3e816f22b34290374158f4cd8702b)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[ssh_transport_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gaed450ebb53a676fafc58bb6cfe82a448)。

启动 SSH 客户端连接（SSH client connection）。

<a id="r_ga4e7daf40096a0494012065cdd8f635a5"></a>

```c
int ssh_client_stop (struct ssh_client *ssh)
```

相关声明：[ssh_client_stop](#ga4e7daf40096a0494012065cdd8f635a5)。

停止 SSH 客户端连接。

<a id="r_ga59ee3f15001a09bb7acb780dbbd2bfb4"></a>

```c
int ssh_client_register_transport_callback (struct ssh_transport_conf *conf)
```

相关声明：[ssh_client_register_transport_callback](#ga59ee3f15001a09bb7acb780dbbd2bfb4)、[ssh_transport_conf](../network_service_model_reference/P064_ssh_transport_conf_结构体.md)。

注册回调函数，以获取与服务器连接关联的传输对象（transport）。

<a id="r_gacea3dba8b5ae41b94b941607288de66e"></a>

```c
int ssh_client_unregister_transport_callback (struct ssh_transport_conf *conf)
```

相关声明：[ssh_client_unregister_transport_callback](#gacea3dba8b5ae41b94b941607288de66e)、[ssh_transport_conf](../network_service_model_reference/P064_ssh_transport_conf_结构体.md)。

注销用于获取与服务器连接关联传输对象的回调函数。

<a id="r_gad5147237b87360043d68f2d91eb12ee5"></a>

```c
struct ssh_client * ssh_transport_get_client (struct ssh_transport *transport)
```

相关声明：[ssh_transport_get_client](#gad5147237b87360043d68f2d91eb12ee5)。

获取拥有指定传输对象的 SSH 客户端实例。

## 21.2\_详细说明（Detailed Documentation）

<a id="ga59ee3f15001a09bb7acb780dbbd2bfb4"></a>

### `ssh_client_register_transport_callback()`

```c
int ssh_client_register_transport_callback ( struct ssh_transport_conf * conf)
```

```c
#include <zephyr/net/ssh/client.h>
```

注册回调函数，以获取与服务器连接关联的传输对象（transport）。

注册的回调用于接收客户端传输事件（Client-side Transport Events）。客户端角色只发出以下事件类型：

- 服务器接受所请求的 SSH 服务时，发出 `SSH_TRANSPORT_EVENT_SERVICE_ACCEPTED`。
- 认证尝试（Authentication Attempt）完成时，发出 `SSH_TRANSPORT_EVENT_AUTHENTICATE_RESULT`。
- 传输对象被拆除（Torn Down）时，发出 `SSH_TRANSPORT_EVENT_CLOSED`。

忽略回调返回值；回调作为观察者（Observer），无法影响传输流程（Transport Flow）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conf` | 传输回调配置数据（Transport Callback Configuration Data）。此结构体必须保持有效，直到被注销。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga44a3e816f22b34290374158f4cd8702b"></a>

### `ssh_client_start()`

```c
int ssh_client_start ( struct ssh_client * ssh, const char * user_name, const struct net_sockaddr * addr, int host_key_index, ssh_transport_event_callback_t callback, void * user_data )
```

```c
#include <zephyr/net/ssh/client.h>
```

启动 SSH 客户端连接（SSH client connection）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ssh` | SSH 客户端实例（Client Instance）。 |
| `user_name` | 用于认证（Authentication）的用户名。 |
| `addr` | 要连接的 SSH 服务器地址（Server Address）。 |
| `host_key_index` | 用于验证服务器身份（Server Identity）的主机密钥索引（Host Key Index）。 |
| `callback` | 发生 SSH 传输事件（Transport Events）时调用的回调。 |
| `user_data` | 要传递给回调（Callback）的用户数据（User Data）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga4e7daf40096a0494012065cdd8f635a5"></a>

### `ssh_client_stop()`

```c
int ssh_client_stop ( struct ssh_client * ssh)
```

```c
#include <zephyr/net/ssh/client.h>
```

停止 SSH 客户端连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ssh` | SSH 客户端实例（Client Instance）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gacea3dba8b5ae41b94b941607288de66e"></a>

### `ssh_client_unregister_transport_callback()`

```c
int ssh_client_unregister_transport_callback ( struct ssh_transport_conf * conf)
```

```c
#include <zephyr/net/ssh/client.h>
```

注销用于获取与服务器连接关联传输对象的回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conf` | 传输回调配置数据（Transport Callback Configuration Data）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="gad5147237b87360043d68f2d91eb12ee5"></a>

### `ssh_transport_get_client()`

```c
struct ssh_client * ssh_transport_get_client ( struct ssh_transport * transport)
```

```c
#include <zephyr/net/ssh/client.h>
```

获取拥有指定传输对象的 SSH 客户端实例。

已注册的传输回调（Transport Callback）会全局接收所有客户端实例的事件；在其中可使用此接口确定某个传输属于哪个客户端实例。本函数只能用于从客户端传输回调获得的传输对象。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `transport` | 要获取所属客户端（Owning Client）的传输对象（Transport）。 |

**返回（Returns）**：**返回值（Returns）：**指向所属 SSH 客户端实例（Client Instance）的指针；传输对象为 `NULL` 时返回 `NULL`。


## 21.3\_原页交叉引用（Cross References）

- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [ssh_transport_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gaed450ebb53a676fafc58bb6cfe82a448)
- [ssh_transport_conf](../network_service_model_reference/P064_ssh_transport_conf_结构体.md)
- [zephyr/net/ssh/client.h](../api_file_interface_reference/P054_zephyr__net__ssh__client.h_文件参考.md)
- [SSH_TRANSPORT_EVENT_SERVICE_ACCEPTED](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga578aed0a10600bc7a248dbb64ca13cc2a72f7351ace863e48a150a67daee364f3)
- [SSH_TRANSPORT_EVENT_AUTHENTICATE_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga578aed0a10600bc7a248dbb64ca13cc2a2264e7a3cafd2a7e90e61232e8b9604a)
- [SSH_TRANSPORT_EVENT_CLOSED](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga578aed0a10600bc7a248dbb64ca13cc2a75fcdde91f09ec0599575054300d90e8)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P020_传感器驱动后端 API.md) · [返回大纲](大纲.md) · [下一章](P022_安全Shell（SSH）密钥生成（Keygen）的API。.md)
