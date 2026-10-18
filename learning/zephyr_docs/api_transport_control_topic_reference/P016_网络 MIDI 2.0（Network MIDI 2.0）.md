---
id: learning.zephyr-docs.api-transport-control-topic-reference.page-16
title: 网络 MIDI 2.0（Network MIDI 2.0）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_网络 MIDI 2.0（Network MIDI 2.0）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

**引入版本（Since）：**4.3。**版本（Version）：**0.1.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 16.1\_主题（Topics）

<a id="r_netmidi10"></a>

相关声明：[用于通用 MIDI 数据包的用户数据报协议（User Datagram Protocol for Universal MIDI Packets）](../api_platform_topic_reference/P069_用于通用 MIDI 数据包的用户数据报协议（User Datagram Protocol for Universal MIDI Packets）.md)。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 16.2\_数据结构（Data Structures）

<a id="r_netmidi2_5Fuser"></a>

```c
struct netmidi2_user
```

相关声明：[netmidi2_user](../network_service_model_reference/P033_netmidi2_user_结构体.md)。

基于用户的认证（User-Based Authentication）所用的用户名/口令对。

<a id="r_netmidi2_5Fuserlist"></a>

```c
struct netmidi2_userlist
```

相关声明：[netmidi2_userlist](../network_service_model_reference/P034_netmidi2_userlist_结构体.md)。

基于用户的认证（User-Based Authentication）所用的用户列表。

<a id="r_netmidi2_5Fsession"></a>

```c
struct netmidi2_session
```

相关声明：[netmidi2_session](../network_service_model_reference/P032_netmidi2_session_结构体.md)。

网络MIDI 2会话（Session），表示与对端的连接。

<a id="r_netmidi2_5Fep"></a>

```c
struct netmidi2_ep
```

相关声明：[netmidi2_ep](../network_service_model_reference/P031_netmidi2_ep_结构体.md)。

网络MIDI 2.0端点（Endpoint）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 16.3\_宏定义（Macros）

<a id="r_ga918cdeae835fd4aa1c6cd810b579b085"></a>

```c
#define NETMIDI2_NONCE_SIZE 16
```

相关声明：[NETMIDI2_NONCE_SIZE](#ga918cdeae835fd4aa1c6cd810b579b085)。

发送给客户端用于认证的随机数（Nonce）大小，单位为字节。

<a id="r_gad920903fa9295cd1f6f183bb365dcee3"></a>

```c
#define NETMIDI2_EP_DEFINE(_var_name, _ep_name, _piid, _port)
```

相关声明：[NETMIDI2_EP_DEFINE](#gad920903fa9295cd1f6f183bb365dcee3)。

静态声明网络（UDP）MIDI 2.0 端点主机（Endpoint Host）。

<a id="r_ga18fc68f856a9799dc73217b9714a2fc2"></a>

```c
#define NETMIDI2_EP_DEFINE_WITH_AUTH(_var_name, _ep_name, _piid, _port, _secret)
```

相关声明：[NETMIDI2_EP_DEFINE_WITH_AUTH](#ga18fc68f856a9799dc73217b9714a2fc2)。

静态声明网络（UDP）MIDI 2.0 端点主机（Endpoint Host），使用预定义共享密钥（Shared Secret Key）进行认证。

<a id="r_ga0228ef860898b072cbd3919cbcf2f49f"></a>

```c
#define NETMIDI2_EP_DEFINE_WITH_USERS(_var_name, _ep_name, _piid, _port, ...)
```

相关声明：[NETMIDI2_EP_DEFINE_WITH_USERS](#ga0228ef860898b072cbd3919cbcf2f49f)。

静态声明网络（UDP）MIDI 2.0 端点主机（Endpoint Host），使用预定义用户名／密码列表进行认证。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 16.4\_枚举（Enumerations）

<a id="r_gae6ec636fa7aadbe9b7675404015d01e7"></a>

```c
enum netmidi2_auth_type { NETMIDI2_AUTH_NONE , NETMIDI2_AUTH_SHARED_SECRET , NETMIDI2_AUTH_USER_PASSWORD }
```

相关声明：[netmidi2_auth_type](#gae6ec636fa7aadbe9b7675404015d01e7)、[NETMIDI2_AUTH_NONE](#ggae6ec636fa7aadbe9b7675404015d01e7ab0d6258fa6ce35e6e9a260d585d1647e)、[NETMIDI2_AUTH_SHARED_SECRET](#ggae6ec636fa7aadbe9b7675404015d01e7a42fa2f83dbd21f9747e32ac5f5180f90)、[NETMIDI2_AUTH_USER_PASSWORD](#ggae6ec636fa7aadbe9b7675404015d01e7a55b35a2303b341aa7309c0dc3898a414)。

网络 MIDI2 的认证类型（Authentication Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 16.5\_函数（Functions）

<a id="r_gabc608c8a74f503f729edfc0506a356cd"></a>

```c
int netmidi2_host_ep_start (struct netmidi2_ep *ep)
```

相关声明：[netmidi2_host_ep_start](#gabc608c8a74f503f729edfc0506a356cd)、[netmidi2_ep](../network_service_model_reference/P031_netmidi2_ep_结构体.md)。

开始托管基于网络（UDP）的通用 MIDI 数据包（Universal MIDI Packet）端点。

<a id="r_ga694e4920c2091bfc532ad23e2e2bbd46"></a>

```c
void netmidi2_broadcast (struct netmidi2_ep *ep, const struct midi_ump ump)
```

相关声明：[netmidi2_broadcast](#ga694e4920c2091bfc532ad23e2e2bbd46)、[netmidi2_ep](../network_service_model_reference/P031_netmidi2_ep_结构体.md)、[midi_ump](../usb/P099_通用MIDI数据包结构.md)。

向连接到端点的所有客户端发送通用 MIDI 数据包（Universal MIDI Packet）。

<a id="r_ga638d918c5e87be3d7f1013a2ad2810dd"></a>

```c
void netmidi2_send (struct netmidi2_session *sess, const struct midi_ump ump)
```

相关声明：[netmidi2_send](#ga638d918c5e87be3d7f1013a2ad2810dd)、[netmidi2_session](../network_service_model_reference/P032_netmidi2_session_结构体.md)、[midi_ump](../usb/P099_通用MIDI数据包结构.md)。

向单个客户端发送通用 MIDI 数据包（Universal MIDI Packet）。

## 16.6\_详细说明（Detailed Documentation）

<a id="gad920903fa9295cd1f6f183bb365dcee3"></a>

### `NETMIDI2_EP_DEFINE`

```c
#define NETMIDI2_EP_DEFINE ( _var_name, _ep_name, _piid, _port )
```

```c
#include <zephyr/net/midi2.h>
```

展开值（Value）：

```c
static struct netmidi2_ep _var_name = { \
        .name = (_ep_name), \
        .piid = (_piid), \
        .addr4.sin_port = (_port), \
        .auth_type = NETMIDI2_AUTH_NONE, \
}
```

静态声明网络（UDP）MIDI 2.0 端点主机（Endpoint Host）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_var_name` | 保存服务器数据（Server Data）的变量名称。 |
| `_ep_name` | 通用 MIDI 数据包（UMP）端点名称（Endpoint Name）。 |
| `_piid` | UMP 产品实例 ID（Product Instance ID）。若为 `NULL`，将在运行时使用 HWINFO 设备 ID。 |
| `_port` | 要监听的 UDP 端口；`0` 表示自动分配（Automatic Assignment）。 |

<a id="ga18fc68f856a9799dc73217b9714a2fc2"></a>

### `NETMIDI2_EP_DEFINE_WITH_AUTH`

```c
#define NETMIDI2_EP_DEFINE_WITH_AUTH ( _var_name, _ep_name, _piid, _port, _secret )
```

```c
#include <zephyr/net/midi2.h>
```

展开值（Value）：

```c
static struct netmidi2_ep _var_name = { \
        .name = (_ep_name), \
        .piid = (_piid), \
        .addr4.sin_port = (_port), \
        .auth_type = NETMIDI2_AUTH_SHARED_SECRET, \
        .shared_auth_secret = (_secret), \
}
```

静态声明网络（UDP）MIDI 2.0 端点主机（Endpoint Host），使用预定义共享密钥（Shared Secret Key）进行认证。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_var_name` | 保存服务器数据（Server Data）的变量名称。 |
| `_ep_name` | 通用 MIDI 数据包（UMP）端点名称（Endpoint Name）。 |
| `_piid` | UMP 产品实例 ID（Product Instance ID）。若为 `NULL`，将在运行时使用 HWINFO 设备 ID。 |
| `_port` | 要监听的 UDP 端口；`0` 表示自动分配（Automatic Assignment）。 |
| `_secret` | 客户端必须提供才能连接的共享密钥（Shared Secret Key）。 |

<a id="ga0228ef860898b072cbd3919cbcf2f49f"></a>

### `NETMIDI2_EP_DEFINE_WITH_USERS`

```c
#define NETMIDI2_EP_DEFINE_WITH_USERS ( _var_name, _ep_name, _piid, _port, ... )
```

```c
#include <zephyr/net/midi2.h>
```

展开值（Value）：

```c
static const struct netmidi2_userlist users_of_##_var_name = { \
        .n_users = ARRAY_SIZE(((struct netmidi2_user []) { __VA_ARGS__ })), \
        .users = { __VA_ARGS__ }, \
}; \
static struct netmidi2_ep _var_name = { \
        .name = (_ep_name), \
        .piid = (_piid), \
        .addr4.sin_port = (_port), \
        .auth_type = NETMIDI2_AUTH_USER_PASSWORD, \
        .userlist = &users_of_##_var_name, \
}
```

静态声明网络（UDP）MIDI 2.0 端点主机（Endpoint Host），使用预定义用户名／密码列表进行认证。

使用示例：

原始示例（Example）：

```c
NETMIDI2_EP_DEFINE_WITH_USERS(my_server, "endpoint", NULL, 0,
                               {.name="user1", .password="passwd1"},
                               {.name="user2", .password="passwd2"})
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_var_name` | 保存服务器数据（Server Data）的变量名称。 |
| `_ep_name` | 通用 MIDI 数据包（UMP）端点名称（Endpoint Name）。 |
| `_piid` | UMP 产品实例 ID（Product Instance ID）。若为 `NULL`，将在运行时使用 HWINFO 设备 ID。 |
| `_port` | 要监听的 UDP 端口；`0` 表示自动分配（Automatic Assignment）。 |
| `...` | 用户名／密码对（Username/Password Pairs），即 `struct netmidi2_user`。 |

<a id="ga918cdeae835fd4aa1c6cd810b579b085"></a>

### `NETMIDI2_NONCE_SIZE`

```c
#define NETMIDI2_NONCE_SIZE 16
```

```c
#include <zephyr/net/midi2.h>
```

发送给客户端用于认证的随机数（Nonce）大小，单位为字节。

**参阅（See Also）**：**另见（See Also）：**《通用 MIDI 数据包的用户数据报协议》（User Datagram Protocol for Universal MIDI Packets），6.7 节“邀请回复：需要认证”（Invitation Reply: Authentication Required）。

<a id="gae6ec636fa7aadbe9b7675404015d01e7"></a>

### `netmidi2_auth_type`

```c
enum netmidi2_auth_type
```

```c
#include <zephyr/net/midi2.h>
```

网络 MIDI2 的认证类型（Authentication Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NETMIDI2_AUTH_NONE` | 无需认证（No Authentication Required）。 |
| `NETMIDI2_AUTH_SHARED_SECRET` | 使用共享密钥（Shared Secret Key）认证。 |
| `NETMIDI2_AUTH_USER_PASSWORD` | 使用用户名和密码（Username and Password）认证。 |

<a id="ga694e4920c2091bfc532ad23e2e2bbd46"></a>

### `netmidi2_broadcast()`

```c
void netmidi2_broadcast ( struct netmidi2_ep * ep, const struct midi_ump ump )
```

```c
#include <zephyr/net/midi2.h>
```

向连接到端点的所有客户端发送通用 MIDI 数据包（Universal MIDI Packet）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` ep` | 端点（Endpoint）。 |
| `[in] ump` | 要发送的数据包（Packet）。 |

<a id="gabc608c8a74f503f729edfc0506a356cd"></a>

### `netmidi2_host_ep_start()`

```c
int netmidi2_host_ep_start ( struct netmidi2_ep * ep)
```

```c
#include <zephyr/net/midi2.h>
```

开始托管基于网络（UDP）的通用 MIDI 数据包（Universal MIDI Packet）端点。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ep` | 要启动的网络端点（Network Endpoint）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，出错返回 `-errno`。

<a id="ga638d918c5e87be3d7f1013a2ad2810dd"></a>

### `netmidi2_send()`

```c
void netmidi2_send ( struct netmidi2_session * sess, const struct midi_ump ump )
```

```c
#include <zephyr/net/midi2.h>
```

向单个客户端发送通用 MIDI 数据包（Universal MIDI Packet）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` sess` | 标识单个客户端的会话（Session）。 |
| `[in] ump` | 要发送的数据包（Packet）。 |


## 16.7\_原页交叉引用（Cross References）

- [用于通用 MIDI 数据包的用户数据报协议（User Datagram Protocol for Universal MIDI Packets）](../api_platform_topic_reference/P069_用于通用 MIDI 数据包的用户数据报协议（User Datagram Protocol for Universal MIDI Packets）.md)
- [netmidi2_user](../network_service_model_reference/P033_netmidi2_user_结构体.md)
- [netmidi2_userlist](../network_service_model_reference/P034_netmidi2_userlist_结构体.md)
- [netmidi2_session](../network_service_model_reference/P032_netmidi2_session_结构体.md)
- [netmidi2_ep](../network_service_model_reference/P031_netmidi2_ep_结构体.md)
- [midi_ump](../usb/P099_通用MIDI数据包结构.md)
- [zephyr/net/midi2.h](../api_file_service_interface_reference/P039_zephyr__net__midi2.h_文件参考.md)
- [ARRAY_SIZE](../util_reference/P001_通用工具公共接口.md#ga70c57aae3eb654e205459b4362c8089a)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__net__midi2_html_ggae6ec636fa7aadbe9b7675404015d01e7ab0d6258fa6ce35e6e9a260d585d1647e"></a>
<a id="astructnetmidi2__ep_html"></a>
<a id="agroup__net__midi2_html_ggae6ec636fa7aadbe9b7675404015d01e7a42fa2f83dbd21f9747e32ac5f5180f90"></a>
<a id="agroup__net__midi2_html_ggae6ec636fa7aadbe9b7675404015d01e7a55b35a2303b341aa7309c0dc3898a414"></a>
<a id="agroup__sys-util_html_ga70c57aae3eb654e205459b4362c8089a"></a>
<a id="astructnetmidi2__user_html"></a>
<a id="astructnetmidi2__userlist_html"></a>
<a id="agroup__net__midi2_html_ga0228ef860898b072cbd3919cbcf2f49f"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggae6ec636fa7aadbe9b7675404015d01e7ab0d6258fa6ce35e6e9a260d585d1647e"></a>
<a id="ggae6ec636fa7aadbe9b7675404015d01e7a42fa2f83dbd21f9747e32ac5f5180f90"></a>
<a id="ggae6ec636fa7aadbe9b7675404015d01e7a55b35a2303b341aa7309c0dc3898a414"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P015_调制解调器 UBX 协议（Modem Ubx）.md) · [返回大纲](大纲.md) · [下一章](P017_Renesas RZ_A 引脚控制辅助工具（Pin control helpers）.md)
