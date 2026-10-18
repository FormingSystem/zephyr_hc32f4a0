---
id: learning.zephyr-docs.network-core-model-reference.page-78
title: net_icmp_ping_params_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__icmp__ping__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第78章\_net\_icmp\_ping\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__icmp__ping__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

表示发送回显请求（Echo-Request，ping）消息时所需参数的结构。

```c
#include <zephyr/net/icmp.h>
```

<a id="details"></a>

表示发送回显请求（Echo-Request，ping）消息时所需参数的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 78.1\_数据成员（Data Fields）

<a id="r_a138d6de6072ebbf3ae454eb3ee28b138"></a>

```c
uint16_t identifier
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[identifier](#a138d6de6072ebbf3ae454eb3ee28b138)。

帮助将回显应答（Echo Replies）匹配到本回显请求（Echo Request）的标识符。

<a id="r_a3756461b95ce1b7fde9d59819de10d85"></a>

```c
uint16_t sequence
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sequence](#a3756461b95ce1b7fde9d59819de10d85)。

帮助将回显应答（Echo Replies）匹配到本回显请求（Echo Request）的序列号。

<a id="r_aaf5a9493b5d98f72bb27758fd24c64ec"></a>

```c
uint8_t tc_tos
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tc_tos](#aaf5a9493b5d98f72bb27758fd24c64ec)。

可以是IPv4服务类型（Type of Service）字段值，也可以是IPv6流量类别（Traffic Class）字段值。

<a id="r_a3a9abdb27bfb94ca6515e280bf6bee3c"></a>

```c
int priority
```

相关声明：[priority](#a3a9abdb27bfb94ca6515e280bf6bee3c)。

网络数据包优先级（Network Packet Priority）。

<a id="r_ac2247bc63eea000200429f0f441031bf"></a>

```c
const void * data
```

相关声明：[data](#ac2247bc63eea000200429f0f441031bf)。

任意载荷数据（Payload Data），会原样包含在回显应答（Echo Reply）中。

<a id="r_a342b75123a32e35f91bda3e11601598b"></a>

```c
size_t data_size
```

相关声明：[data_size](#a342b75123a32e35f91bda3e11601598b)。

载荷数据（Payload Data）的大小，单位为字节。

## 78.2\_详细说明（Detailed Documentation）

<a id="ac2247bc63eea000200429f0f441031bf"></a>

### `data`

```c
const void* net_icmp_ping_params::data
```

任意载荷数据（Payload Data），会原样包含在回显应答（Echo Reply）中。

可为NULL。

<a id="a342b75123a32e35f91bda3e11601598b"></a>

### `data_size`

```c
size_t net_icmp_ping_params::data_size
```

载荷数据（Payload Data）的大小，单位为字节。

可为0。data指针为NULL时，函数将生成指定大小的载荷（Payload）。

<a id="a138d6de6072ebbf3ae454eb3ee28b138"></a>

### `identifier`

```c
uint16_t net_icmp_ping_params::identifier
```

帮助将回显应答（Echo Replies）匹配到本回显请求（Echo Request）的标识符。

可为0。

<a id="a3a9abdb27bfb94ca6515e280bf6bee3c"></a>

### `priority`

```c
int net_icmp_ping_params::priority
```

网络数据包优先级（Network Packet Priority）。

<a id="a3756461b95ce1b7fde9d59819de10d85"></a>

### `sequence`

```c
uint16_t net_icmp_ping_params::sequence
```

帮助将回显应答（Echo Replies）匹配到本回显请求（Echo Request）的序列号。

可为0。

<a id="aaf5a9493b5d98f72bb27758fd24c64ec"></a>

### `tc_tos`

```c
uint8_t net_icmp_ping_params::tc_tos
```

可以是IPv4服务类型（Type of Service）字段值，也可以是IPv6流量类别（Traffic Class）字段值。

表示差分服务代码点（DSCP）与显式拥塞通知（ECN）的组合值。

本数据类型文档由以下文件生成：

- `zephyr/net/icmp.h`

## 78.3\_原页交叉引用（Cross References）

- [zephyr/net/icmp.h](https://docs.zephyrproject.org/latest/doxygen/html/icmp_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P077_net_icmp_offload_结构体.md) · [返回大纲](大纲.md) · [下一章](P079_net_if_结构体.md)
