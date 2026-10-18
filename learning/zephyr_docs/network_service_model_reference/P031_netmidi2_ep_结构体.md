---
id: learning.zephyr-docs.network-service-model-reference.page-31
title: netmidi2_ep_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnetmidi2__ep.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_netmidi2\_ep\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnetmidi2__ep.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络MIDI 2.0端点（Endpoint）。

```c
#include <zephyr/net/midi2.h>
```

<a id="details"></a>

网络MIDI 2.0端点（Endpoint）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 31.1\_数据成员（Data Fields）

<a id="r_a439571c6a042c28e9002b090e617a391"></a>

```c
const char * name
```

相关声明：[name](#a439571c6a042c28e9002b090e617a391)。

端点名称（endpoint name）。

<a id="r_adf7a2f4826320c614bcb2cea9b5b214e"></a>

```c
const char * piid
```

相关声明：[piid](#adf7a2f4826320c614bcb2cea9b5b214e)。

端点产品实例 ID（product instance ID）。

```c
union {
```

<a id="r_a0c91e4a7fa4807d2cf7203e512d09f46"></a>

```c
struct net_sockaddr addr
```

相关声明：[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[addr](#a1da1c0bef306386df5d0923cadb04a10)。

<a id="r_aedc280e3df82952605b25c070bd6670e"></a>

```c
struct net_sockaddr_in addr4
```

相关声明：[net_sockaddr_in](../network_core_model_reference/P119_net_sockaddr_in_结构体.md)、[addr4](#a37befb690f98866d52abac009cc237c7)。

<a id="r_a3ecfed28eaaa3b74fd17fc3f46cb0a5a"></a>

```c
struct net_sockaddr_in6 addr6
```

相关声明：[net_sockaddr_in6](../network_core_model_reference/P120_net_sockaddr_in6_结构体.md)、[addr6](#a5d84716f1ff7f843391ec7faa633154d)。

<a id="r_a3f7c1fe02e53431752257103a0ec7f40"></a>

```c
};
```

本地端点地址。

<a id="r_aba537e498bc6210fd6b718879db711f3"></a>

```c
struct zsock_pollfd pollsock
```

相关声明：[zsock_pollfd](../posix_system_model_reference/P030_zsock_pollfd_结构体.md)、[pollsock](#aba537e498bc6210fd6b718879db711f3)。

封装在轮询描述符（poll descriptor）中的监听套接字。

<a id="r_ac6f1588dc3845a847dcebe81df64c776"></a>

```c
void(* rx_packet_cb )(struct netmidi2_session *session, const struct midi_ump ump)
```

相关声明：[rx_packet_cb](#ac6f1588dc3845a847dcebe81df64c776)、[netmidi2_session](P032_netmidi2_session_结构体.md)、[midi_ump](../usb/P099_通用MIDI数据包结构.md)。

从客户端收到数据时调用的函数。

<a id="r_ae73643aad93d83005fb5fa19b8a99ac7"></a>

```c
struct netmidi2_session peers [CONFIG_NETMIDI2_HOST_MAX_CLIENTS]
```

相关声明：[netmidi2_session](P032_netmidi2_session_结构体.md)、[peers](#ae73643aad93d83005fb5fa19b8a99ac7)。

此端点的对端列表。

<a id="r_afe9c4413a90f92834fdf06b59fc31363"></a>

```c
enum netmidi2_auth_type auth_type
```

相关声明：[netmidi2_auth_type](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#gae6ec636fa7aadbe9b7675404015d01e7)、[auth_type](#afe9c4413a90f92834fdf06b59fc31363)。

与此主机端点建立会话所需的身份验证类型。

```c
union {
```

<a id="r_ae878085ead14d69fb1e8f765e328aca1"></a>

```c
const char * shared_auth_secret
```

相关声明：[shared_auth_secret](#a7093bf87340a47a46180e3a720ee94c4)。

共享身份验证密钥（shared authentication key）。

<a id="r_a013f87811705a9a4326179edf1281106"></a>

```c
const struct netmidi2_userlist * userlist
```

相关声明：[netmidi2_userlist](P034_netmidi2_userlist_结构体.md)、[userlist](#a1389cb4e0a73ad7d44143d59c6cbac2e)。

用户及密码列表。

<a id="r_a272eb917cd1309acc878963ace5945f0"></a>

```c
};
```

## 31.2\_详细说明（Detailed Documentation）

<a id="a272eb917cd1309acc878963ace5945f0"></a>

### `[union]`

```c
union { ... } netmidi2_ep
```

<a id="a3f7c1fe02e53431752257103a0ec7f40"></a>

### `[union]`

```c
union { ... } netmidi2_ep
```

本地端点地址。

<a id="a1da1c0bef306386df5d0923cadb04a10"></a>

### `addr`

```c
struct net_sockaddr netmidi2_ep::addr
```

<a id="a37befb690f98866d52abac009cc237c7"></a>

### `addr4`

```c
struct net_sockaddr_in netmidi2_ep::addr4
```

<a id="a5d84716f1ff7f843391ec7faa633154d"></a>

### `addr6`

```c
struct net_sockaddr_in6 netmidi2_ep::addr6
```

<a id="afe9c4413a90f92834fdf06b59fc31363"></a>

### `auth_type`

```c
enum netmidi2_auth_type netmidi2_ep::auth_type
```

与此主机端点建立会话所需的身份验证类型。

<a id="a439571c6a042c28e9002b090e617a391"></a>

### `name`

```c
const char* netmidi2_ep::name
```

端点名称（endpoint name）。

<a id="ae73643aad93d83005fb5fa19b8a99ac7"></a>

### `peers`

```c
struct netmidi2_session netmidi2_ep::peers[CONFIG_NETMIDI2_HOST_MAX_CLIENTS]
```

此端点的对端列表。

<a id="adf7a2f4826320c614bcb2cea9b5b214e"></a>

### `piid`

```c
const char* netmidi2_ep::piid
```

端点产品实例 ID（product instance ID）。

<a id="aba537e498bc6210fd6b718879db711f3"></a>

### `pollsock`

```c
struct zsock_pollfd netmidi2_ep::pollsock
```

封装在轮询描述符（poll descriptor）中的监听套接字。

<a id="ac6f1588dc3845a847dcebe81df64c776"></a>

### `rx_packet_cb`

```c
void(* netmidi2_ep::rx_packet_cb) (struct netmidi2_session *session, const struct midi_ump ump)
```

从客户端收到数据时调用的函数。

<a id="a7093bf87340a47a46180e3a720ee94c4"></a>

### `shared_auth_secret`

```c
const char* netmidi2_ep::shared_auth_secret
```

共享身份验证密钥（shared authentication key）。

<a id="a1389cb4e0a73ad7d44143d59c6cbac2e"></a>

### `userlist`

```c
const struct netmidi2_userlist* netmidi2_ep::userlist
```

用户及密码列表。

本数据类型文档由以下文件生成：

- `zephyr/net/midi2.h`

## 31.3\_原页交叉引用（Cross References）

- [zephyr/net/midi2.h](https://docs.zephyrproject.org/latest/doxygen/html/midi2_8h_source.html)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [net_sockaddr_in](../network_core_model_reference/P119_net_sockaddr_in_结构体.md)
- [net_sockaddr_in6](../network_core_model_reference/P120_net_sockaddr_in6_结构体.md)
- [zsock_pollfd](../posix_system_model_reference/P030_zsock_pollfd_结构体.md)
- [netmidi2_session](P032_netmidi2_session_结构体.md)
- [midi_ump](../usb/P099_通用MIDI数据包结构.md)
- [netmidi2_auth_type](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#gae6ec636fa7aadbe9b7675404015d01e7)
- [netmidi2_userlist](P034_netmidi2_userlist_结构体.md)
- [netmidi2_ep](P031_netmidi2_ep_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P030_mdio_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P032_netmidi2_session_结构体.md)
