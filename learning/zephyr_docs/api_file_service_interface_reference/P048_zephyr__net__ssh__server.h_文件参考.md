---
id: learning.zephyr-docs.api-file-service-interface-reference.page-48
title: zephyr__net__ssh__server.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ssh_2server_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第48章\_zephyr\_\_net\_\_ssh\_\_server.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ssh_2server_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

安全Shell（SSH）服务器的API。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/net/socket.h>
#include <zephyr/net/ssh/common.h>
```

查看此文件的源码。

安全Shell（SSH）服务器的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 48.1\_数据结构（Data Structures）

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

## 48.2\_类型定义（Typedefs）

<a id="r_ga72953be174ebb5a948815f49d083105a"></a>

```c
typedef int(* ssh_server_event_callback_t) (struct ssh_server *sshd, const struct ssh_server_event *event, void *user_data)
```

相关声明：[ssh_server_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#ga72953be174ebb5a948815f49d083105a)、[ssh_server_event](../network_service_model_reference/P061_ssh_server_event_结构体.md)。

安全外壳（SSH）服务器事件的回调函数类型。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 48.3\_枚举（Enumerations）

<a id="r_ga38729e64c5c13a3df058fba5481f56cd"></a>

```c
enum ssh_server_event_type { SSH_SERVER_EVENT_CLOSED , SSH_SERVER_EVENT_CLIENT_CONNECTED , SSH_SERVER_EVENT_CLIENT_DISCONNECTED }
```

相关声明：[ssh_server_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#ga38729e64c5c13a3df058fba5481f56cd)、[SSH_SERVER_EVENT_CLOSED](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#gga38729e64c5c13a3df058fba5481f56cda85d7f17dcdf41768d7fad6f356a9fc78)、[SSH_SERVER_EVENT_CLIENT_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#gga38729e64c5c13a3df058fba5481f56cda1eca79d603a6aa92a27eb0e636c34149)、[SSH_SERVER_EVENT_CLIENT_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#gga38729e64c5c13a3df058fba5481f56cda127d2b9f2843207f6f206147a21b2c29)。

服务器事件类型（Server Event Types）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 48.4\_函数（Functions）

<a id="r_ga017b274d7604ecca118aab5060bdfd7b"></a>

```c
int ssh_server_start (struct ssh_server *sshd, const struct net_sockaddr *bind_addr, int host_key_index, const char *username, const char *password, const int *authorized_keys, size_t authorized_keys_len, ssh_server_event_callback_t server_callback, ssh_transport_event_callback_t transport_callback, void *user_data)
```

相关声明：[ssh_server_start](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#ga017b274d7604ecca118aab5060bdfd7b)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[ssh_server_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#ga72953be174ebb5a948815f49d083105a)、[ssh_transport_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gaed450ebb53a676fafc58bb6cfe82a448)。

启动安全外壳（SSH）服务器。

<a id="r_ga0ceb09a44c1d659d85f51dc5b842cef6"></a>

```c
int ssh_server_stop (struct ssh_server *sshd)
```

相关声明：[ssh_server_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#ga0ceb09a44c1d659d85f51dc5b842cef6)。

停止安全外壳（SSH）服务器。

<a id="r_gacd16569ffbf5b87530d27d9eba6229d4"></a>

```c
int ssh_server_transport_close (struct ssh_server *sshd, int idx)
```

相关声明：[ssh_server_transport_close](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#gacd16569ffbf5b87530d27d9eba6229d4)。

关闭 SSH 服务器传输连接（Transport Connection）。

<a id="r_gad14ab0c8d54711b60e73ff7d0409b9d9"></a>

```c
int ssh_server_register_transport_callback (struct ssh_transport_conf *conf)
```

相关声明：[ssh_server_register_transport_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#gad14ab0c8d54711b60e73ff7d0409b9d9)、[ssh_transport_conf](../network_service_model_reference/P064_ssh_transport_conf_结构体.md)。

注册用于获取客户端连接所关联传输（Transport）的回调函数。

<a id="r_ga76a0afc5f12f7b3a7133c0e759a0bb25"></a>

```c
int ssh_server_unregister_transport_callback (struct ssh_transport_conf *conf)
```

相关声明：[ssh_server_unregister_transport_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#ga76a0afc5f12f7b3a7133c0e759a0bb25)、[ssh_transport_conf](../network_service_model_reference/P064_ssh_transport_conf_结构体.md)。

注销用于获取客户端连接所关联传输（Transport）的回调函数。

<a id="r_ga41202a4f05c23393071d71df948fc91d"></a>

```c
struct ssh_server * ssh_transport_get_server (struct ssh_transport *transport)
```

相关声明：[ssh_transport_get_server](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#ga41202a4f05c23393071d71df948fc91d)。

获取拥有指定传输（Transport）的 SSH 服务器实例。


## 48.5\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/net/socket.h](../api_source_socket_ethernet_reference/P006_socket.h_源码浏览.md)
- [zephyr/net/ssh/common.h](../api_source_architecture_reference/P010_common.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P811_server.h_源码浏览.md)
- [ssh_server_event_client_connected](../network_service_model_reference/P062_ssh_server_event_client_connected_结构体.md)
- [ssh_server_event_client_disconnected](../network_service_model_reference/P063_ssh_server_event_client_disconnected_结构体.md)
- [ssh_server_event](../network_service_model_reference/P061_ssh_server_event_结构体.md)
- [ssh_server_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#ga72953be174ebb5a948815f49d083105a)
- [ssh_server_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#ga38729e64c5c13a3df058fba5481f56cd)
- [SSH_SERVER_EVENT_CLOSED](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#gga38729e64c5c13a3df058fba5481f56cda85d7f17dcdf41768d7fad6f356a9fc78)
- [SSH_SERVER_EVENT_CLIENT_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#gga38729e64c5c13a3df058fba5481f56cda1eca79d603a6aa92a27eb0e636c34149)
- [SSH_SERVER_EVENT_CLIENT_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#gga38729e64c5c13a3df058fba5481f56cda127d2b9f2843207f6f206147a21b2c29)
- [ssh_server_start](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#ga017b274d7604ecca118aab5060bdfd7b)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [ssh_transport_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gaed450ebb53a676fafc58bb6cfe82a448)
- [ssh_server_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#ga0ceb09a44c1d659d85f51dc5b842cef6)
- [ssh_server_transport_close](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#gacd16569ffbf5b87530d27d9eba6229d4)
- [ssh_server_register_transport_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#gad14ab0c8d54711b60e73ff7d0409b9d9)
- [ssh_transport_conf](../network_service_model_reference/P064_ssh_transport_conf_结构体.md)
- [ssh_server_unregister_transport_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#ga76a0afc5f12f7b3a7133c0e759a0bb25)
- [ssh_transport_get_server](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#ga41202a4f05c23393071d71df948fc91d)

<a id="header-details"></a>

---

[上一章](P047_zephyr__mgmt__mcumgr__smp__smp_client.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P049_zephyr__sys__sys_getopt.h_文件参考.md)
