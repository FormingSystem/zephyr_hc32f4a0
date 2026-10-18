---
id: learning.zephyr-docs.posix-system-model-reference.page-29
title: zsock_addrinfo_结构体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structzsock__addrinfo.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_zsock\_addrinfo\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structzsock__addrinfo.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查询地址信息（Address Information）时使用的定义。

```c
#include <zephyr/net/socket.h>
```

<a id="details"></a>

查询地址信息时使用的定义。`getaddrinfo()` 返回由这些描述符组成的链表；调用 `getaddrinfo()` 时，也可将此结构体作为查询提示（hints）传入。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 29.1\_数据成员（Data Fields）

<a id="r_a7fdc7a266b2f96766f8c4e79649bfa65"></a>

```c
struct zsock_addrinfo * ai_next
```

相关声明：[zsock_addrinfo](P029_zsock_addrinfo_结构体.md)、[ai_next](#a7fdc7a266b2f96766f8c4e79649bfa65)。

指向下一个地址条目的指针。

<a id="r_a971514adde66f5c1a04efc7f42f244d1"></a>

```c
int ai_flags
```

相关声明：[ai_flags](#a971514adde66f5c1a04efc7f42f244d1)。

附加选项（Additional options）。

<a id="r_a83ef78e3347e69564e2663a769356d87"></a>

```c
int ai_family
```

相关声明：[ai_family](#a83ef78e3347e69564e2663a769356d87)。

所返回地址的地址族（address family）。

<a id="r_adcb8a732921a11a35f89241cfe413b78"></a>

```c
int ai_socktype
```

相关声明：[ai_socktype](#adcb8a732921a11a35f89241cfe413b78)。

套接字类型（Socket type），例如 `NET_SOCK_STREAM` 或 `NET_SOCK_DGRAM`。

<a id="r_aae090dcd0c1e73497560cbcc333a452d"></a>

```c
int ai_protocol
```

相关声明：[ai_protocol](#aae090dcd0c1e73497560cbcc333a452d)。

地址所用协议；0 表示任意协议。

<a id="r_ae6c344fdb8ae4b15fe4986ce1fc84453"></a>

```c
int ai_eflags
```

相关声明：[ai_eflags](#ae6c344fdb8ae4b15fe4986ce1fc84453)。

用于特殊用途的扩展标志。

<a id="r_a1bf757d3c4eb2ee6c76136edb6c622da"></a>

```c
net_socklen_t ai_addrlen
```

相关声明：[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)、[ai_addrlen](#a1bf757d3c4eb2ee6c76136edb6c622da)。

套接字地址的长度。

<a id="r_a59a931d41fc1f512b030fa9bb9c45d37"></a>

```c
struct net_sockaddr * ai_addr
```

相关声明：[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[ai_addr](#a59a931d41fc1f512b030fa9bb9c45d37)。

指向地址的指针。

<a id="r_aa9a96f1d5d49833beea05558879867cf"></a>

```c
char * ai_canonname
```

相关声明：[ai_canonname](#aa9a96f1d5d49833beea05558879867cf)。

可选的主机正式名称（official name）。

## 29.2\_详细说明（Detailed Documentation）

<a id="a59a931d41fc1f512b030fa9bb9c45d37"></a>

### `ai_addr`

```c
struct net_sockaddr* zsock_addrinfo::ai_addr
```

指向地址的指针。

<a id="a1bf757d3c4eb2ee6c76136edb6c622da"></a>

### `ai_addrlen`

```c
net_socklen_t zsock_addrinfo::ai_addrlen
```

套接字地址的长度。

<a id="aa9a96f1d5d49833beea05558879867cf"></a>

### `ai_canonname`

```c
char* zsock_addrinfo::ai_canonname
```

可选的主机正式名称（official name）。

<a id="ae6c344fdb8ae4b15fe4986ce1fc84453"></a>

### `ai_eflags`

```c
int zsock_addrinfo::ai_eflags
```

用于特殊用途的扩展标志。

<a id="a83ef78e3347e69564e2663a769356d87"></a>

### `ai_family`

```c
int zsock_addrinfo::ai_family
```

所返回地址的地址族（address family）。

<a id="a971514adde66f5c1a04efc7f42f244d1"></a>

### `ai_flags`

```c
int zsock_addrinfo::ai_flags
```

附加选项（Additional options）。

<a id="a7fdc7a266b2f96766f8c4e79649bfa65"></a>

### `ai_next`

```c
struct zsock_addrinfo* zsock_addrinfo::ai_next
```

指向下一个地址条目的指针。

<a id="aae090dcd0c1e73497560cbcc333a452d"></a>

### `ai_protocol`

```c
int zsock_addrinfo::ai_protocol
```

地址所用协议；0 表示任意协议。

<a id="adcb8a732921a11a35f89241cfe413b78"></a>

### `ai_socktype`

```c
int zsock_addrinfo::ai_socktype
```

套接字类型（Socket type），例如 `NET_SOCK_STREAM` 或 `NET_SOCK_DGRAM`。

本数据类型文档由以下文件生成：

- `zephyr/net/socket.h`

## 29.3\_原页交叉引用（Cross References）

- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h_source.html)
- [zsock_addrinfo](P029_zsock_addrinfo_结构体.md)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [getaddrinfo()](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h.html#adc9ea491d9008de7cd9e0a5b9147ca70)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P028_utsname_结构体.md) · [返回大纲](大纲.md) · [下一章](P030_zsock_pollfd_结构体.md)
