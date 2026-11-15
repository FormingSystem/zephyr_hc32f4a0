---
id: learning.zephyr-docs.network-core-model-reference.page-118
title: net_sockaddr_can_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__sockaddr__can.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第118章\_net\_sockaddr\_can\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__sockaddr__can.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

struct net_sockaddr_can：CAN套接字（Socket）使用的net_sockaddr结构。

```c
#include <zephyr/net/net_ip.h>
```

<a id="details"></a>

struct net_sockaddr_can：CAN套接字（Socket）使用的net_sockaddr结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 118.1\_数据成员（Data Fields）

<a id="r_a7e25be69230e5887a8326e991ddba6e0"></a>

```c
net_sa_family_t can_family
```

相关声明：[net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)、[can_family](#a7e25be69230e5887a8326e991ddba6e0)。

地址族（Address family）。

<a id="r_a597d33def7c50f84f2b17c320b7ca6c5"></a>

```c
int can_ifindex
```

相关声明：[can_ifindex](#a597d33def7c50f84f2b17c320b7ca6c5)。

SocketCAN 网络接口索引（Network interface index）。

## 118.2\_详细说明（Detailed Documentation）

<a id="a7e25be69230e5887a8326e991ddba6e0"></a>

### `can_family`

```c
net_sa_family_t net_sockaddr_can::can_family
```

地址族（Address family）。

<a id="a597d33def7c50f84f2b17c320b7ca6c5"></a>

### `can_ifindex`

```c
int net_sockaddr_can::can_ifindex
```

SocketCAN 网络接口索引（Network interface index）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_ip.h`

## 118.3\_原页交叉引用（Cross References）

- [net_sockaddr_can](P118_net_sockaddr_can_结构体.md)
- [net_sockaddr](P117_net_sockaddr_结构体.md)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)
- [net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P117_net_sockaddr_结构体.md) · [返回大纲](大纲.md) · [下一章](P119_net_sockaddr_in_结构体.md)
