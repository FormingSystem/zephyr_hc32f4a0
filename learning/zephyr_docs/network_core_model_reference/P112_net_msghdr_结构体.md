---
id: learning.zephyr-docs.network-core-model-reference.page-112
title: net_msghdr_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__msghdr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第112章\_net\_msghdr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__msghdr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

消息结构（Message Struct）。

```c
#include <zephyr/net/net_ip.h>
```

<a id="details"></a>

消息结构（Message Struct）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 112.1\_数据成员（Data Fields）

<a id="r_a8f46d780cccad65cc755fb71eacf52ea"></a>

```c
void * msg_name
```

相关声明：[msg_name](#a8f46d780cccad65cc755fb71eacf52ea)。

可选的套接字地址（Socket address），采用大端字节序（Big endian）。

<a id="r_a38ea33c4a18d07022b89129107b6ffa5"></a>

```c
net_socklen_t msg_namelen
```

相关声明：[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)、[msg_namelen](#a38ea33c4a18d07022b89129107b6ffa5)。

套接字地址大小（Socket address size）。

<a id="r_a1263d9b8942042b7cf21727f8312ff7d"></a>

```c
struct net_iovec * msg_iov
```

相关声明：[net_iovec](P098_net_iovec_结构体.md)、[msg_iov](#a1263d9b8942042b7cf21727f8312ff7d)。

分散／聚集数组（Scatter/gather array）。

<a id="r_adbadc26695f3646aae690721e99d558a"></a>

```c
size_t msg_iovlen
```

相关声明：[msg_iovlen](#adbadc26695f3646aae690721e99d558a)。

`msg_iov` 中的元素个数（Number of elements）。

<a id="r_a6e12f22fc1750226e706e64529bb84bd"></a>

```c
void * msg_control
```

相关声明：[msg_control](#a6e12f22fc1750226e706e64529bb84bd)。

辅助数据（Ancillary data）。

<a id="r_a66dcca1e90e25dabe949842873b6edc4"></a>

```c
size_t msg_controllen
```

相关声明：[msg_controllen](#a66dcca1e90e25dabe949842873b6edc4)。

辅助数据缓冲区长度（Ancillary data buffer length）。

<a id="r_a0a07694671a1725d5ec8af16de3d6778"></a>

```c
int msg_flags
```

相关声明：[msg_flags](#a0a07694671a1725d5ec8af16de3d6778)。

所接收消息的标志（Flags）。

## 112.2\_详细说明（Detailed Documentation）

<a id="a6e12f22fc1750226e706e64529bb84bd"></a>

### `msg_control`

```c
void* net_msghdr::msg_control
```

辅助数据（Ancillary data）。

<a id="a66dcca1e90e25dabe949842873b6edc4"></a>

### `msg_controllen`

```c
size_t net_msghdr::msg_controllen
```

辅助数据缓冲区长度（Ancillary data buffer length）。

<a id="a0a07694671a1725d5ec8af16de3d6778"></a>

### `msg_flags`

```c
int net_msghdr::msg_flags
```

所接收消息的标志（Flags）。

<a id="a1263d9b8942042b7cf21727f8312ff7d"></a>

### `msg_iov`

```c
struct net_iovec* net_msghdr::msg_iov
```

分散／聚集数组（Scatter/gather array）。

<a id="adbadc26695f3646aae690721e99d558a"></a>

### `msg_iovlen`

```c
size_t net_msghdr::msg_iovlen
```

`msg_iov` 中的元素个数（Number of elements）。

<a id="a8f46d780cccad65cc755fb71eacf52ea"></a>

### `msg_name`

```c
void* net_msghdr::msg_name
```

可选的套接字地址（Socket address），采用大端字节序（Big endian）。

<a id="a38ea33c4a18d07022b89129107b6ffa5"></a>

### `msg_namelen`

```c
net_socklen_t net_msghdr::msg_namelen
```

套接字地址大小（Socket address size）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_ip.h`

## 112.3\_原页交叉引用（Cross References）

- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)
- [net_iovec](P098_net_iovec_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P111_net_mgmt_msghdr_结构体.md) · [返回大纲](大纲.md) · [下一章](P113_net_packet_mreq_结构体.md)
