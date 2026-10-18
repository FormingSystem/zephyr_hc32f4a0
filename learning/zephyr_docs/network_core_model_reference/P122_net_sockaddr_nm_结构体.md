---
id: learning.zephyr-docs.network-core-model-reference.page-122
title: net_sockaddr_nm_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__sockaddr__nm.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第122章\_net\_sockaddr\_nm\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__sockaddr__nm.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

struct net_sockaddr_nm：NET_MGMT套接字（Socket）使用的net_sockaddr结构。

```c
#include <zephyr/net/net_ip.h>
```

<a id="details"></a>

`struct net_sockaddr_nm`——用于 NET_MGMT 套接字的 `net_sockaddr` 结构。其概念与 Linux 的 `AF_NETLINK` 相似，但由于实现不同，为避免混淆 Zephyr 与 Linux，这里不使用 NETLINK 名称。套接字域（Socket domain），即地址族（Address family），为 `AF_NET_MGMT`；此服务面向数据报（Datagram-oriented），因此套接字类型为 `NET_SOCK_RAW` 或 `NET_SOCK_DGRAM`。协议（Protocol／Protocol type）选择此套接字所用于的功能。与 `bind()` 配合使用时，可在 `net_sockaddr_nm` 的 `nm_pid` 字段中填入调用线程自身的 ID。这里，`nm_pid` 充当此 `net_mgmt` 套接字的本地地址。应用负责选择一个唯一的整数值填入 `nm_pid`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 122.1\_数据成员（Data Fields）

<a id="r_aeaef27e6db3cca162dfd66337ccb629b"></a>

```c
net_sa_family_t nm_family
```

相关声明：[net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)、[nm_family](#aeaef27e6db3cca162dfd66337ccb629b)。

`AF_NET_MGMT` 地址族（Address family）。

<a id="r_a78e154af8b9530de3b12743115c91792"></a>

```c
int nm_ifindex
```

相关声明：[nm_ifindex](#a78e154af8b9530de3b12743115c91792)。

与此地址关联的网络接口（Network interface）。

<a id="r_ad2f9976b5c6e46f8969e83bbcefdbeb9"></a>

```c
uintptr_t nm_pid
```

相关声明：[uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)、[nm_pid](#ad2f9976b5c6e46f8969e83bbcefdbeb9)。

线程标识符（Thread ID）或类似值，用于区分不同的套接字（Sockets）。

<a id="r_a62ab3cea810b51107cc92cf43b2de6d9"></a>

```c
uint64_t nm_mask
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[nm_mask](#a62ab3cea810b51107cc92cf43b2de6d9)。

`net_mgmt` 掩码（Mask）。

## 122.2\_详细说明（Detailed Documentation）

<a id="aeaef27e6db3cca162dfd66337ccb629b"></a>

### `nm_family`

```c
net_sa_family_t net_sockaddr_nm::nm_family
```

`AF_NET_MGMT` 地址族（Address family）。

<a id="a78e154af8b9530de3b12743115c91792"></a>

### `nm_ifindex`

```c
int net_sockaddr_nm::nm_ifindex
```

与此地址关联的网络接口（Network interface）。

<a id="a62ab3cea810b51107cc92cf43b2de6d9"></a>

### `nm_mask`

```c
uint64_t net_sockaddr_nm::nm_mask
```

`net_mgmt` 掩码（Mask）。

<a id="ad2f9976b5c6e46f8969e83bbcefdbeb9"></a>

### `nm_pid`

```c
uintptr_t net_sockaddr_nm::nm_pid
```

线程标识符（Thread ID）或类似值，用于区分不同的套接字（Sockets）。

应用可以自行决定如何构造进程标识符（PID）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_ip.h`

## 122.3\_原页交叉引用（Cross References）

- [net_sockaddr_nm](P122_net_sockaddr_nm_结构体.md)
- [net_sockaddr](P117_net_sockaddr_结构体.md)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)
- [net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [bind()](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a05b4e957a092db3e68281988ceb32df8)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P121_net_sockaddr_ll_结构体.md) · [返回大纲](大纲.md) · [下一章](P123_net_socket_service_desc_结构体.md)
