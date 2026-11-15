---
id: learning.zephyr-docs.api-transport-control-topic-reference.page-9
title: IPv4 套接字选项（Socket options）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ipv4__socket__options.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_IPv4 套接字选项（Socket options）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ipv4__socket__options.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-member-group"></a>
<a id="member-group"></a>

## 9.1\_IPv4 层级选项（IPv4 Level Options，NET_IPPROTO_IP）

<a id="r_gad86db5ae0a9b9a971cb5ec75532595f9"></a>

```c
#define ZSOCK_IP_TOS 1
```

相关声明：[ZSOCK_IP_TOS](#gad86db5ae0a9b9a971cb5ec75532595f9)。

设置或获取传出数据包的服务类型（Type of Service，TOS）值。

<a id="r_ga87e8da2dafd3794240c5e1cdb2ef39fc"></a>

```c
#define ZSOCK_IP_TTL 2
```

相关声明：[ZSOCK_IP_TTL](#ga87e8da2dafd3794240c5e1cdb2ef39fc)。

设置或获取传出数据包的生存时间（Time to Live，TTL）值。

<a id="r_ga19b4e323fdbc59c7d8853658b4e15e16"></a>

```c
#define ZSOCK_IP_PKTINFO 8
```

相关声明：[ZSOCK_IP_PKTINFO](#ga19b4e323fdbc59c7d8853658b4e15e16)。

传递 `IP_PKTINFO` 辅助消息（Ancillary Message）；其中包含 `pktinfo` 结构体，提供传入数据包的相关信息。

<a id="r_ga32348af8cfe5540ffc85a70c642fb3e4"></a>

```c
#define ZSOCK_IP_RECVTTL 12
```

相关声明：[ZSOCK_IP_RECVTTL](#ga32348af8cfe5540ffc85a70c642fb3e4)。

传递 `IP_RECVTTL` 辅助消息（Ancillary Message），其中包含传入数据包的生存时间（Time to Live）信息。

<a id="r_gaea02e9ad4ca5347a7026388f0009e730"></a>

```c
#define ZSOCK_IP_MTU 14
```

相关声明：[ZSOCK_IP_MTU](#gaea02e9ad4ca5347a7026388f0009e730)。

获取当前套接字（Socket）目前已知的路径最大传输单元（Path MTU）。

<a id="r_ga3c8f7f8895a3daae11dcd439eb2499a3"></a>

```c
#define ZSOCK_IP_DONTFRAG 15
```

相关声明：[ZSOCK_IP_DONTFRAG](#ga3c8f7f8895a3daae11dcd439eb2499a3)。

禁用此套接字（Socket）的本地 IPv4 分片（Fragmentation）。

<a id="r_gaa14b3e744b44603a2aa520cacbeef95b"></a>

```c
#define ZSOCK_IP_MULTICAST_IF 32
```

相关声明：[ZSOCK_IP_MULTICAST_IF](#gaa14b3e744b44603a2aa520cacbeef95b)。

设置 IPv4 多播数据报（Multicast Datagram）使用的网络接口。

<a id="r_gab94fd2f344c2c3f1462ccec2f876b8f2"></a>

```c
#define ZSOCK_IP_MULTICAST_TTL 33
```

相关声明：[ZSOCK_IP_MULTICAST_TTL](#gab94fd2f344c2c3f1462ccec2f876b8f2)。

设置 IPv4 多播生存时间（Multicast TTL）值。

<a id="r_gaf5c2aec9a1fcaf0515ccd7d1d5b57cb2"></a>

```c
#define ZSOCK_IP_MULTICAST_LOOP 34
```

相关声明：[ZSOCK_IP_MULTICAST_LOOP](#gaf5c2aec9a1fcaf0515ccd7d1d5b57cb2)。

设置 IPv4 多播回环（Multicast Loop）值。

<a id="r_ga9bd617872815d3752e9464f98d32e1ce"></a>

```c
#define ZSOCK_IP_ADD_MEMBERSHIP 35
```

相关声明：[ZSOCK_IP_ADD_MEMBERSHIP](#ga9bd617872815d3752e9464f98d32e1ce)。

加入 IPv4 多播组（Multicast Group）。

<a id="r_ga5bf7c18d0400ee370db3bfeab812598a"></a>

```c
#define ZSOCK_IP_DROP_MEMBERSHIP 36
```

相关声明：[ZSOCK_IP_DROP_MEMBERSHIP](#ga5bf7c18d0400ee370db3bfeab812598a)。

离开 IPv4 多播组（Multicast Group）。

<a id="r_gaceaecf7f826715aab2740c57c6ec6407"></a>

```c
#define ZSOCK_IP_LOCAL_PORT_RANGE 51
```

相关声明：[ZSOCK_IP_LOCAL_PORT_RANGE](#gaceaecf7f826715aab2740c57c6ec6407)。

针对给定套接字（Socket）缩小全局端口范围（Global Port Range）。

## 9.2\_详细说明（Detailed Documentation）

<a id="ga9bd617872815d3752e9464f98d32e1ce"></a>

### `ZSOCK_IP_ADD_MEMBERSHIP`

```c
#define ZSOCK_IP_ADD_MEMBERSHIP 35
```

```c
#include <zephyr/net/socket.h>
```

加入 IPv4 多播组（Multicast Group）。

<a id="ga3c8f7f8895a3daae11dcd439eb2499a3"></a>

### `ZSOCK_IP_DONTFRAG`

```c
#define ZSOCK_IP_DONTFRAG 15
```

```c
#include <zephyr/net/socket.h>
```

禁用此套接字（Socket）的本地 IPv4 分片（Fragmentation）。

接受整数形式的布尔值：`0` 表示允许分片（Fragmentation），非零表示禁用分片。启用此选项后，超过接口 MTU 的数据报会被本地拒绝，并将 `errno` 设为 `EMSGSIZE`，而不会被分片。对于 IPv4，还会设置 IP 头中的禁止分片位（Don't Fragment，DF）。

适用于 `NET_IPPROTO_IP` 层级的 `setsockopt()` 和 `getsockopt()`。

此选项也可以作为 `sendmsg()` 的辅助数据（Ancillary Data）传入，为单个数据报覆盖分片处理方式（Fragmentation Handling）。

<a id="ga5bf7c18d0400ee370db3bfeab812598a"></a>

### `ZSOCK_IP_DROP_MEMBERSHIP`

```c
#define ZSOCK_IP_DROP_MEMBERSHIP 36
```

```c
#include <zephyr/net/socket.h>
```

离开 IPv4 多播组（Multicast Group）。

<a id="gaceaecf7f826715aab2740c57c6ec6407"></a>

### `ZSOCK_IP_LOCAL_PORT_RANGE`

```c
#define ZSOCK_IP_LOCAL_PORT_RANGE 51
```

```c
#include <zephyr/net/socket.h>
```

针对给定套接字（Socket）缩小全局端口范围（Global Port Range）。

<a id="gaea02e9ad4ca5347a7026388f0009e730"></a>

### `ZSOCK_IP_MTU`

```c
#define ZSOCK_IP_MTU 14
```

```c
#include <zephyr/net/socket.h>
```

获取当前套接字（Socket）目前已知的路径最大传输单元（Path MTU）。

返回整数。`ZSOCK_IP_MTU` 仅适用于 `getsockopt`，且只能用于已连接（Connected）的套接字。

<a id="gaa14b3e744b44603a2aa520cacbeef95b"></a>

### `ZSOCK_IP_MULTICAST_IF`

```c
#define ZSOCK_IP_MULTICAST_IF 32
```

```c
#include <zephyr/net/socket.h>
```

设置 IPv4 多播数据报（Multicast Datagram）使用的网络接口。

<a id="gaf5c2aec9a1fcaf0515ccd7d1d5b57cb2"></a>

### `ZSOCK_IP_MULTICAST_LOOP`

```c
#define ZSOCK_IP_MULTICAST_LOOP 34
```

```c
#include <zephyr/net/socket.h>
```

设置 IPv4 多播回环（Multicast Loop）值。

<a id="gab94fd2f344c2c3f1462ccec2f876b8f2"></a>

### `ZSOCK_IP_MULTICAST_TTL`

```c
#define ZSOCK_IP_MULTICAST_TTL 33
```

```c
#include <zephyr/net/socket.h>
```

设置 IPv4 多播生存时间（Multicast TTL）值。

<a id="ga19b4e323fdbc59c7d8853658b4e15e16"></a>

### `ZSOCK_IP_PKTINFO`

```c
#define ZSOCK_IP_PKTINFO 8
```

```c
#include <zephyr/net/socket.h>
```

传递 `IP_PKTINFO` 辅助消息（Ancillary Message）；其中包含 `pktinfo` 结构体，提供传入数据包的相关信息。

<a id="ga32348af8cfe5540ffc85a70c642fb3e4"></a>

### `ZSOCK_IP_RECVTTL`

```c
#define ZSOCK_IP_RECVTTL 12
```

```c
#include <zephyr/net/socket.h>
```

传递 `IP_RECVTTL` 辅助消息（Ancillary Message），其中包含传入数据包的生存时间（Time to Live）信息。

<a id="gad86db5ae0a9b9a971cb5ec75532595f9"></a>

### `ZSOCK_IP_TOS`

```c
#define ZSOCK_IP_TOS 1
```

```c
#include <zephyr/net/socket.h>
```

设置或获取传出数据包的服务类型（Type of Service，TOS）值。

<a id="ga87e8da2dafd3794240c5e1cdb2ef39fc"></a>

### `ZSOCK_IP_TTL`

```c
#define ZSOCK_IP_TTL 2
```

```c
#include <zephyr/net/socket.h>
```

设置或获取传出数据包的生存时间（Time to Live，TTL）值。


## 9.3\_原页交叉引用（Cross References）

- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [EMSGSIZE](../error_reference/P003_系统错误号公共接口.md#gae37becfaa095a9df5c5c788bce5aa06f)
- [setsockopt()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a71c8788caef89a362e35ce5855e77077)
- [getsockopt()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a2d33f1c2b99a5d0df682f54c3ccb2ffa)
- [NET_IPPROTO_IP](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggaf06819bf427cc58be1229b27b373ca31a41d4bfab7d2a68dd7b707eb70ed88b41)
- [sendmsg()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a8a2ad4261d3978ba299926f45d56ed74)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P008_ICM4268X API主题.md) · [返回大纲](大纲.md) · [下一章](P010_LIS2DS12 API主题.md)
