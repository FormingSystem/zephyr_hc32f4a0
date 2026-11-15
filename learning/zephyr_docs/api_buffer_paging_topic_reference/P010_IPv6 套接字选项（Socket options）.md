---
id: learning.zephyr-docs.api-buffer-paging-topic-reference.page-10
title: IPv6 套接字选项（Socket options）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ipv6__socket__options.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_IPv6 套接字选项（Socket options）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ipv6__socket__options.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-member-group"></a>
<a id="member-group"></a>

## 10.1\_IPv6 层级选项（IPv6 Level Options，NET_IPPROTO_IPV6）

<a id="r_ga6b3364d4ea2e4c34f1de975e6f66961b"></a>

```c
#define ZSOCK_IPV6_UNICAST_HOPS 16
```

相关声明：[ZSOCK_IPV6_UNICAST_HOPS](#ga6b3364d4ea2e4c34f1de975e6f66961b)。

设置套接字的单播跳数限制（Unicast Hop Limit）。

<a id="r_ga4f15d7b5032536896c0785f16830329d"></a>

```c
#define ZSOCK_IPV6_MULTICAST_IF 17
```

相关声明：[ZSOCK_IPV6_MULTICAST_IF](#ga4f15d7b5032536896c0785f16830329d)。

设置套接字的多播输出网络接口索引（Multicast Output Network Interface Index）。

<a id="r_ga78bda8f2e2c0e0fc3cf9788c42d8b6f8"></a>

```c
#define ZSOCK_IPV6_MULTICAST_HOPS 18
```

相关声明：[ZSOCK_IPV6_MULTICAST_HOPS](#ga78bda8f2e2c0e0fc3cf9788c42d8b6f8)。

设置套接字的多播跳数限制（Multicast Hop Limit）。

<a id="r_ga6fc007f21de54e12697a21712ca095c3"></a>

```c
#define ZSOCK_IPV6_MULTICAST_LOOP 19
```

相关声明：[ZSOCK_IPV6_MULTICAST_LOOP](#ga6fc007f21de54e12697a21712ca095c3)。

设置套接字的多播环回位（Multicast Loop Bit）。

<a id="r_gae438698778cfe58c28c7928f9b227f30"></a>

```c
#define ZSOCK_IPV6_ADD_MEMBERSHIP 20
```

相关声明：[ZSOCK_IPV6_ADD_MEMBERSHIP](#gae438698778cfe58c28c7928f9b227f30)。

加入 IPv6 多播组（Multicast Group）。

<a id="r_ga1d70e019e1341a3d54dfd7a819cb7071"></a>

```c
#define ZSOCK_IPV6_DROP_MEMBERSHIP 21
```

相关声明：[ZSOCK_IPV6_DROP_MEMBERSHIP](#ga1d70e019e1341a3d54dfd7a819cb7071)。

离开 IPv6 多播组（Multicast Group）。

<a id="r_gab524aa153b4a7005f988d7bb167bacab"></a>

```c
#define ZSOCK_IPV6_JOIN_GROUP ZSOCK_IPV6_ADD_MEMBERSHIP
```

相关声明：[ZSOCK_IPV6_JOIN_GROUP](#gab524aa153b4a7005f988d7bb167bacab)、[ZSOCK_IPV6_ADD_MEMBERSHIP](#gae438698778cfe58c28c7928f9b227f30)。

加入 IPv6 多播组（Multicast Group）。

<a id="r_ga1b2fc808d5b602e658d88d66f1f1d1d1"></a>

```c
#define ZSOCK_IPV6_LEAVE_GROUP ZSOCK_IPV6_DROP_MEMBERSHIP
```

相关声明：[ZSOCK_IPV6_LEAVE_GROUP](#ga1b2fc808d5b602e658d88d66f1f1d1d1)、[ZSOCK_IPV6_DROP_MEMBERSHIP](#ga1d70e019e1341a3d54dfd7a819cb7071)。

离开 IPv6 多播组（Multicast Group）。

<a id="r_gac37821fc6bd4b484ff36a00dea505245"></a>

```c
#define ZSOCK_IPV6_MTU 24
```

相关声明：[ZSOCK_IPV6_MTU](#gac37821fc6bd4b484ff36a00dea505245)。

对于 getsockopt()，获取指定套接字当前已知的 IPv6 路径最大传输单元（Path MTU）。

<a id="r_ga44b16e54bc2922153e9a07d628cf1cba"></a>

```c
#define ZSOCK_IPV6_DONTFRAG 62
```

相关声明：[ZSOCK_IPV6_DONTFRAG](#ga44b16e54bc2922153e9a07d628cf1cba)。

对此套接字禁用本地 IPv6 分片（Fragmentation）。

<a id="r_ga004e5f8352ae9c6d8096919e44fdd874"></a>

```c
#define ZSOCK_IPV6_V6ONLY 26
```

相关声明：[ZSOCK_IPV6_V6ONLY](#ga004e5f8352ae9c6d8096919e44fdd874)。

不支持 IPv4 访问。

<a id="r_gab399d0b2da77aa4331490bb312aa2fb0"></a>

```c
#define ZSOCK_IPV6_RECVPKTINFO 49
```

相关声明：[ZSOCK_IPV6_RECVPKTINFO](#gab399d0b2da77aa4331490bb312aa2fb0)。

传递 IPV6_RECVPKTINFO 辅助消息（Ancillary Message），其中包含 in6_pktinfo 结构体，提供入站数据包的一些信息。

<a id="r_ga24b054ba13a54ae2064aea31f52d7ed0"></a>

```c
#define ZSOCK_IPV6_PKTINFO 50
```

相关声明：[ZSOCK_IPV6_PKTINFO](#ga24b054ba13a54ae2064aea31f52d7ed0)。

在辅助数据（Ancillary Data）中返回 in6_pktinfo 结构体的选项。

<a id="r_gad0c689068bc6bff4369a1ea9b36d09a9"></a>

```c
#define ZSOCK_IPV6_RECVHOPLIMIT 51
```

相关声明：[ZSOCK_IPV6_RECVHOPLIMIT](#gad0c689068bc6bff4369a1ea9b36d09a9)。

传递 IPV6_RECVHOPLIMIT 辅助消息（Ancillary Message），其中包含入站数据包的跳数限制（Hop Limit）信息。

<a id="r_ga92c73652d38a41b8acea0a69362f3e0d"></a>

```c
#define ZSOCK_IPV6_HOPLIMIT 52
```

相关声明：[ZSOCK_IPV6_HOPLIMIT](#ga92c73652d38a41b8acea0a69362f3e0d)。

设置或获取出站数据包的跳数限制（Hoplimit）值。

<a id="r_ga6fd9aed65cb7a1a7eface8455501212b"></a>

```c
#define ZSOCK_IPV6_ADDR_PREFERENCES 72
```

相关声明：[ZSOCK_IPV6_ADDR_PREFERENCES](#ga6fd9aed65cb7a1a7eface8455501212b)。

RFC 5014：源地址选择（Source Address Selection）。

<a id="r_ga061badf1fcadf353667f10a64b77bcb5"></a>

```c
#define ZSOCK_IPV6_PREFER_SRC_TMP 0x0001
```

相关声明：[ZSOCK_IPV6_PREFER_SRC_TMP](#ga061badf1fcadf353667f10a64b77bcb5)。

优先使用临时地址（Temporary Address）作为源地址。

<a id="r_ga3acbfad85a26f4a71b51e570369122a4"></a>

```c
#define ZSOCK_IPV6_PREFER_SRC_PUBLIC 0x0002
```

相关声明：[ZSOCK_IPV6_PREFER_SRC_PUBLIC](#ga3acbfad85a26f4a71b51e570369122a4)。

优先使用公共地址（Public Address）作为源地址。

<a id="r_ga2ecb5f065f2f8806ff7ee680ce3b8bee"></a>

```c
#define ZSOCK_IPV6_PREFER_SRC_PUBTMP_DEFAULT 0x0100
```

相关声明：[ZSOCK_IPV6_PREFER_SRC_PUBTMP_DEFAULT](#ga2ecb5f065f2f8806ff7ee680ce3b8bee)。

根据输出接口配置，选择公共地址（Public Address）或临时地址（Temporary Address）作为默认源地址；这是默认值。

<a id="r_ga60f0a56613fdf6532dd2549273f6e6a2"></a>

```c
#define ZSOCK_IPV6_PREFER_SRC_COA 0x0004
```

相关声明：[ZSOCK_IPV6_PREFER_SRC_COA](#ga60f0a56613fdf6532dd2549273f6e6a2)。

优先使用转交地址（Care-of Address）作为源地址。

<a id="r_gac9afff595eac9ca47c0e14da20531d6b"></a>

```c
#define ZSOCK_IPV6_PREFER_SRC_HOME 0x0400
```

相关声明：[ZSOCK_IPV6_PREFER_SRC_HOME](#gac9afff595eac9ca47c0e14da20531d6b)。

优先使用家乡地址（Home Address）作为源地址。

<a id="r_gaa3b4dd46e7b1fdeaae6db4a692c7f57a"></a>

```c
#define ZSOCK_IPV6_PREFER_SRC_CGA 0x0008
```

相关声明：[ZSOCK_IPV6_PREFER_SRC_CGA](#gaa3b4dd46e7b1fdeaae6db4a692c7f57a)。

优先使用密码生成地址（Cryptographically Generated Address，CGA）作为源地址。

<a id="r_gaa10785a8136550462a895621b2866d0f"></a>

```c
#define ZSOCK_IPV6_PREFER_SRC_NONCGA 0x0800
```

相关声明：[ZSOCK_IPV6_PREFER_SRC_NONCGA](#gaa10785a8136550462a895621b2866d0f)。

优先使用非 CGA 地址作为源地址。

<a id="r_gabe60a1f3a16e4b0a4b2c997f91497c62"></a>

```c
#define ZSOCK_IPV6_TCLASS 67
```

相关声明：[ZSOCK_IPV6_TCLASS](#gabe60a1f3a16e4b0a4b2c997f91497c62)。

设置或获取出站数据包的流量类别（Traffic Class）值。

## 10.2\_详细说明（Detailed Documentation）

<a id="gae438698778cfe58c28c7928f9b227f30"></a>

### `ZSOCK_IPV6_ADD_MEMBERSHIP`

```c
#define ZSOCK_IPV6_ADD_MEMBERSHIP 20
```

```c
#include <zephyr/net/socket.h>
```

加入 IPv6 多播组（Multicast Group）。

<a id="ga6fd9aed65cb7a1a7eface8455501212b"></a>

### `ZSOCK_IPV6_ADDR_PREFERENCES`

```c
#define ZSOCK_IPV6_ADDR_PREFERENCES 72
```

```c
#include <zephyr/net/socket.h>
```

RFC 5014：源地址选择（Source Address Selection）。

<a id="ga44b16e54bc2922153e9a07d628cf1cba"></a>

### `ZSOCK_IPV6_DONTFRAG`

```c
#define ZSOCK_IPV6_DONTFRAG 62
```

```c
#include <zephyr/net/socket.h>
```

对此套接字禁用本地 IPv6 分片（Fragmentation）。

接受整数布尔值（0 表示允许分片，非零表示禁用分片）。启用后，大于接口 MTU 的数据报在本地被拒绝，并将 errno 设为 EMSGSIZE，而不再由协议栈分片。

适用于 NET_IPPROTO_IPV6 层级的 setsockopt() 和 getsockopt()。

此选项也可以作为 `sendmsg()` 的辅助数据（Ancillary Data）传入，为单个数据报覆盖分片处理方式（Fragmentation Handling）。

<a id="ga1d70e019e1341a3d54dfd7a819cb7071"></a>

### `ZSOCK_IPV6_DROP_MEMBERSHIP`

```c
#define ZSOCK_IPV6_DROP_MEMBERSHIP 21
```

```c
#include <zephyr/net/socket.h>
```

离开 IPv6 多播组（Multicast Group）。

<a id="ga92c73652d38a41b8acea0a69362f3e0d"></a>

### `ZSOCK_IPV6_HOPLIMIT`

```c
#define ZSOCK_IPV6_HOPLIMIT 52
```

```c
#include <zephyr/net/socket.h>
```

设置或获取出站数据包的跳数限制（Hoplimit）值。

<a id="gab524aa153b4a7005f988d7bb167bacab"></a>

### `ZSOCK_IPV6_JOIN_GROUP`

```c
#define ZSOCK_IPV6_JOIN_GROUP ZSOCK_IPV6_ADD_MEMBERSHIP
```

```c
#include <zephyr/net/socket.h>
```

加入 IPv6 多播组（Multicast Group）。

<a id="ga1b2fc808d5b602e658d88d66f1f1d1d1"></a>

### `ZSOCK_IPV6_LEAVE_GROUP`

```c
#define ZSOCK_IPV6_LEAVE_GROUP ZSOCK_IPV6_DROP_MEMBERSHIP
```

```c
#include <zephyr/net/socket.h>
```

离开 IPv6 多播组（Multicast Group）。

<a id="gac37821fc6bd4b484ff36a00dea505245"></a>

### `ZSOCK_IPV6_MTU`

```c
#define ZSOCK_IPV6_MTU 24
```

```c
#include <zephyr/net/socket.h>
```

对于 getsockopt()，获取指定套接字当前已知的 IPv6 路径最大传输单元（Path MTU）。

仅在套接字已连接时有效。对于 setsockopt()，设置该套接字使用的 MTU；MTU 受设备 MTU 限制，或在启用路径 MTU 发现（Path MTU Discovery）时受路径 MTU 限制。

<a id="ga78bda8f2e2c0e0fc3cf9788c42d8b6f8"></a>

### `ZSOCK_IPV6_MULTICAST_HOPS`

```c
#define ZSOCK_IPV6_MULTICAST_HOPS 18
```

```c
#include <zephyr/net/socket.h>
```

设置套接字的多播跳数限制（Multicast Hop Limit）。

<a id="ga4f15d7b5032536896c0785f16830329d"></a>

### `ZSOCK_IPV6_MULTICAST_IF`

```c
#define ZSOCK_IPV6_MULTICAST_IF 17
```

```c
#include <zephyr/net/socket.h>
```

设置套接字的多播输出网络接口索引（Multicast Output Network Interface Index）。

<a id="ga6fc007f21de54e12697a21712ca095c3"></a>

### `ZSOCK_IPV6_MULTICAST_LOOP`

```c
#define ZSOCK_IPV6_MULTICAST_LOOP 19
```

```c
#include <zephyr/net/socket.h>
```

设置套接字的多播环回位（Multicast Loop Bit）。

<a id="ga24b054ba13a54ae2064aea31f52d7ed0"></a>

### `ZSOCK_IPV6_PKTINFO`

```c
#define ZSOCK_IPV6_PKTINFO 50
```

```c
#include <zephyr/net/socket.h>
```

在辅助数据（Ancillary Data）中返回 in6_pktinfo 结构体的选项。

<a id="gaa3b4dd46e7b1fdeaae6db4a692c7f57a"></a>

### `ZSOCK_IPV6_PREFER_SRC_CGA`

```c
#define ZSOCK_IPV6_PREFER_SRC_CGA 0x0008
```

```c
#include <zephyr/net/socket.h>
```

优先使用密码生成地址（Cryptographically Generated Address，CGA）作为源地址。

Zephyr 忽略此项。

<a id="ga60f0a56613fdf6532dd2549273f6e6a2"></a>

### `ZSOCK_IPV6_PREFER_SRC_COA`

```c
#define ZSOCK_IPV6_PREFER_SRC_COA 0x0004
```

```c
#include <zephyr/net/socket.h>
```

优先使用转交地址（Care-of Address）作为源地址。

Zephyr 忽略此项。

<a id="gac9afff595eac9ca47c0e14da20531d6b"></a>

### `ZSOCK_IPV6_PREFER_SRC_HOME`

```c
#define ZSOCK_IPV6_PREFER_SRC_HOME 0x0400
```

```c
#include <zephyr/net/socket.h>
```

优先使用家乡地址（Home Address）作为源地址。

Zephyr 忽略此项。

<a id="gaa10785a8136550462a895621b2866d0f"></a>

### `ZSOCK_IPV6_PREFER_SRC_NONCGA`

```c
#define ZSOCK_IPV6_PREFER_SRC_NONCGA 0x0800
```

```c
#include <zephyr/net/socket.h>
```

优先使用非 CGA 地址作为源地址。

Zephyr 忽略此项。

<a id="ga3acbfad85a26f4a71b51e570369122a4"></a>

### `ZSOCK_IPV6_PREFER_SRC_PUBLIC`

```c
#define ZSOCK_IPV6_PREFER_SRC_PUBLIC 0x0002
```

```c
#include <zephyr/net/socket.h>
```

优先使用公共地址（Public Address）作为源地址。

<a id="ga2ecb5f065f2f8806ff7ee680ce3b8bee"></a>

### `ZSOCK_IPV6_PREFER_SRC_PUBTMP_DEFAULT`

```c
#define ZSOCK_IPV6_PREFER_SRC_PUBTMP_DEFAULT 0x0100
```

```c
#include <zephyr/net/socket.h>
```

根据输出接口配置，选择公共地址（Public Address）或临时地址（Temporary Address）作为默认源地址；这是默认值。

这是 Linux 专有选项，RFC 中未定义。

<a id="ga061badf1fcadf353667f10a64b77bcb5"></a>

### `ZSOCK_IPV6_PREFER_SRC_TMP`

```c
#define ZSOCK_IPV6_PREFER_SRC_TMP 0x0001
```

```c
#include <zephyr/net/socket.h>
```

优先使用临时地址（Temporary Address）作为源地址。

<a id="gad0c689068bc6bff4369a1ea9b36d09a9"></a>

### `ZSOCK_IPV6_RECVHOPLIMIT`

```c
#define ZSOCK_IPV6_RECVHOPLIMIT 51
```

```c
#include <zephyr/net/socket.h>
```

传递 IPV6_RECVHOPLIMIT 辅助消息（Ancillary Message），其中包含入站数据包的跳数限制（Hop Limit）信息。

参见 RFC 3542。

<a id="gab399d0b2da77aa4331490bb312aa2fb0"></a>

### `ZSOCK_IPV6_RECVPKTINFO`

```c
#define ZSOCK_IPV6_RECVPKTINFO 49
```

```c
#include <zephyr/net/socket.h>
```

传递 IPV6_RECVPKTINFO 辅助消息（Ancillary Message），其中包含 in6_pktinfo 结构体，提供入站数据包的一些信息。

参见 RFC 3542。

<a id="gabe60a1f3a16e4b0a4b2c997f91497c62"></a>

### `ZSOCK_IPV6_TCLASS`

```c
#define ZSOCK_IPV6_TCLASS 67
```

```c
#include <zephyr/net/socket.h>
```

设置或获取出站数据包的流量类别（Traffic Class）值。

<a id="ga6b3364d4ea2e4c34f1de975e6f66961b"></a>

### `ZSOCK_IPV6_UNICAST_HOPS`

```c
#define ZSOCK_IPV6_UNICAST_HOPS 16
```

```c
#include <zephyr/net/socket.h>
```

设置套接字的单播跳数限制（Unicast Hop Limit）。

<a id="ga004e5f8352ae9c6d8096919e44fdd874"></a>

### `ZSOCK_IPV6_V6ONLY`

```c
#define ZSOCK_IPV6_V6ONLY 26
```

```c
#include <zephyr/net/socket.h>
```

不支持 IPv4 访问。


## 10.3\_原页交叉引用（Cross References）

- [getsockopt()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a2d33f1c2b99a5d0df682f54c3ccb2ffa)
- [RFC 5014](https://datatracker.ietf.org/doc/html/rfc5014)
- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [EMSGSIZE](../error_reference/P003_系统错误号公共接口.md#gae37becfaa095a9df5c5c788bce5aa06f)
- [setsockopt()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a71c8788caef89a362e35ce5855e77077)
- [NET_IPPROTO_IPV6](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggaf06819bf427cc58be1229b27b373ca31acc28399f823adaa247347ab125eb37f4)
- [sendmsg()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a8a2ad4261d3978ba299926f45d56ed74)
- [RFC 3542](https://datatracker.ietf.org/doc/html/rfc3542)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P009_互联网控制消息协议（ICMP）.md) · [返回大纲](大纲.md) · [下一章](P011_后备存储 API（Backing Store APIs）.md)
