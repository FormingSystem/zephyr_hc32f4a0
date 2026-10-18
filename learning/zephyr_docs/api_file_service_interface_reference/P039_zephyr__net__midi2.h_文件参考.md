---
id: learning.zephyr-docs.api-file-service-interface-reference.page-39
title: zephyr__net__midi2.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/midi2_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_zephyr\_\_net\_\_midi2.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/midi2_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
#include <zephyr/audio/midi.h>
#include <zephyr/net/socket.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 39.1\_数据结构（Data Structures）

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

## 39.2\_宏定义（Macros）

<a id="r_ga918cdeae835fd4aa1c6cd810b579b085"></a>

```c
#define NETMIDI2_NONCE_SIZE 16
```

相关声明：[NETMIDI2_NONCE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#ga918cdeae835fd4aa1c6cd810b579b085)。

发送给客户端用于认证的随机数（Nonce）大小，单位为字节。

<a id="r_gad920903fa9295cd1f6f183bb365dcee3"></a>

```c
#define NETMIDI2_EP_DEFINE(_var_name, _ep_name, _piid, _port)
```

相关声明：[NETMIDI2_EP_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#gad920903fa9295cd1f6f183bb365dcee3)。

静态声明网络（UDP）MIDI 2.0 端点主机（Endpoint Host）。

<a id="r_ga18fc68f856a9799dc73217b9714a2fc2"></a>

```c
#define NETMIDI2_EP_DEFINE_WITH_AUTH(_var_name, _ep_name, _piid, _port, _secret)
```

相关声明：[NETMIDI2_EP_DEFINE_WITH_AUTH](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#ga18fc68f856a9799dc73217b9714a2fc2)。

静态声明网络（UDP）MIDI 2.0 端点主机（Endpoint Host），使用预定义共享密钥（Shared Secret Key）进行认证。

<a id="r_ga0228ef860898b072cbd3919cbcf2f49f"></a>

```c
#define NETMIDI2_EP_DEFINE_WITH_USERS(_var_name, _ep_name, _piid, _port, ...)
```

相关声明：[NETMIDI2_EP_DEFINE_WITH_USERS](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#ga0228ef860898b072cbd3919cbcf2f49f)。

静态声明网络（UDP）MIDI 2.0 端点主机（Endpoint Host），使用预定义用户名／密码列表进行认证。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 39.3\_枚举（Enumerations）

<a id="r_gae6ec636fa7aadbe9b7675404015d01e7"></a>

```c
enum netmidi2_auth_type { NETMIDI2_AUTH_NONE , NETMIDI2_AUTH_SHARED_SECRET , NETMIDI2_AUTH_USER_PASSWORD }
```

相关声明：[netmidi2_auth_type](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#gae6ec636fa7aadbe9b7675404015d01e7)、[NETMIDI2_AUTH_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#ggae6ec636fa7aadbe9b7675404015d01e7ab0d6258fa6ce35e6e9a260d585d1647e)、[NETMIDI2_AUTH_SHARED_SECRET](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#ggae6ec636fa7aadbe9b7675404015d01e7a42fa2f83dbd21f9747e32ac5f5180f90)、[NETMIDI2_AUTH_USER_PASSWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#ggae6ec636fa7aadbe9b7675404015d01e7a55b35a2303b341aa7309c0dc3898a414)。

网络 MIDI2 的认证类型（Authentication Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 39.4\_函数（Functions）

<a id="r_gabc608c8a74f503f729edfc0506a356cd"></a>

```c
int netmidi2_host_ep_start (struct netmidi2_ep *ep)
```

相关声明：[netmidi2_host_ep_start](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#gabc608c8a74f503f729edfc0506a356cd)、[netmidi2_ep](../network_service_model_reference/P031_netmidi2_ep_结构体.md)。

开始托管基于网络（UDP）的通用 MIDI 数据包（Universal MIDI Packet）端点。

<a id="r_ga694e4920c2091bfc532ad23e2e2bbd46"></a>

```c
void netmidi2_broadcast (struct netmidi2_ep *ep, const struct midi_ump ump)
```

相关声明：[netmidi2_broadcast](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#ga694e4920c2091bfc532ad23e2e2bbd46)、[netmidi2_ep](../network_service_model_reference/P031_netmidi2_ep_结构体.md)、[midi_ump](../usb/P099_通用MIDI数据包结构.md)。

向连接到端点的所有客户端发送通用 MIDI 数据包（Universal MIDI Packet）。

<a id="r_ga638d918c5e87be3d7f1013a2ad2810dd"></a>

```c
void netmidi2_send (struct netmidi2_session *sess, const struct midi_ump ump)
```

相关声明：[netmidi2_send](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#ga638d918c5e87be3d7f1013a2ad2810dd)、[netmidi2_session](../network_service_model_reference/P032_netmidi2_session_结构体.md)、[midi_ump](../usb/P099_通用MIDI数据包结构.md)。

向单个客户端发送通用 MIDI 数据包（Universal MIDI Packet）。


## 39.5\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/audio/midi.h](../api_source_reference/P529_midi.h_源码浏览.md)
- [zephyr/net/socket.h](../api_source_socket_ethernet_reference/P006_socket.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P528_midi2.h_源码浏览.md)
- [netmidi2_user](../network_service_model_reference/P033_netmidi2_user_结构体.md)
- [netmidi2_userlist](../network_service_model_reference/P034_netmidi2_userlist_结构体.md)
- [netmidi2_session](../network_service_model_reference/P032_netmidi2_session_结构体.md)
- [netmidi2_ep](../network_service_model_reference/P031_netmidi2_ep_结构体.md)
- [NETMIDI2_NONCE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#ga918cdeae835fd4aa1c6cd810b579b085)
- [NETMIDI2_EP_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#gad920903fa9295cd1f6f183bb365dcee3)
- [NETMIDI2_EP_DEFINE_WITH_AUTH](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#ga18fc68f856a9799dc73217b9714a2fc2)
- [NETMIDI2_EP_DEFINE_WITH_USERS](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#ga0228ef860898b072cbd3919cbcf2f49f)
- [netmidi2_auth_type](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#gae6ec636fa7aadbe9b7675404015d01e7)
- [NETMIDI2_AUTH_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#ggae6ec636fa7aadbe9b7675404015d01e7ab0d6258fa6ce35e6e9a260d585d1647e)
- [NETMIDI2_AUTH_SHARED_SECRET](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#ggae6ec636fa7aadbe9b7675404015d01e7a42fa2f83dbd21f9747e32ac5f5180f90)
- [NETMIDI2_AUTH_USER_PASSWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#ggae6ec636fa7aadbe9b7675404015d01e7a55b35a2303b341aa7309c0dc3898a414)
- [netmidi2_host_ep_start](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#gabc608c8a74f503f729edfc0506a356cd)
- [netmidi2_broadcast](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#ga694e4920c2091bfc532ad23e2e2bbd46)
- [midi_ump](../usb/P099_通用MIDI数据包结构.md)
- [netmidi2_send](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#ga638d918c5e87be3d7f1013a2ad2810dd)

---

[上一章](P038_zephyr__dt-bindings__sensor__lsm6dsv80x.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P040_zephyr__mpipe__mpipe_buffer.h_文件参考.md)
