---
id: learning.zephyr-docs.network-application-model-reference.page-23
title: dns_resolve_srv_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdns__resolve__srv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_dns\_resolve\_srv\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdns__resolve__srv.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

服务位置记录（SRV）的信息。

```c
#include <zephyr/net/dns_resolve.h>
```

<a id="details"></a>

服务位置记录（SRV）的信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 23.1\_数据成员（Data Fields）

<a id="r_a338bc4db1b0fb51c074467e04bb0f955"></a>

```c
uint16_t priority
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[priority](#a338bc4db1b0fb51c074467e04bb0f955)。

服务器选择顺序的优先级（Priority）；数值越小，优先级越高。

<a id="r_aaf1b0b289ffbeacd1df9cbcbad7f2563"></a>

```c
uint16_t weight
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[weight](#aaf1b0b289ffbeacd1df9cbcbad7f2563)。

用于负载均衡（Load Balancing）的服务器权重。

<a id="r_ab205aab04f4c271db1c5ff5c52e427ff"></a>

```c
uint16_t port
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[port](#ab205aab04f4c271db1c5ff5c52e427ff)。

服务的端口号（Port Number）。

<a id="r_aacda738fbb4bb3826fc229868432d29b"></a>

```c
size_t targetlen
```

相关声明：[targetlen](#aacda738fbb4bb3826fc229868432d29b)。

target字段的长度。

<a id="r_a55e8628a7bf305794fe10d114b32d25f"></a>

```c
char target [20+1]
```

相关声明：[target](#a55e8628a7bf305794fe10d114b32d25f)。

target字段，以NULL结尾。

## 23.2\_详细说明（Detailed Documentation）

<a id="ab205aab04f4c271db1c5ff5c52e427ff"></a>

### `port`

```c
uint16_t dns_resolve_srv::port
```

服务的端口号（Port Number）。

<a id="a338bc4db1b0fb51c074467e04bb0f955"></a>

### `priority`

```c
uint16_t dns_resolve_srv::priority
```

服务器选择顺序的优先级（Priority）；数值越小，优先级越高。

<a id="a55e8628a7bf305794fe10d114b32d25f"></a>

### `target`

```c
char dns_resolve_srv::target[20+1]
```

target字段，以NULL结尾。

<a id="aacda738fbb4bb3826fc229868432d29b"></a>

### `targetlen`

```c
size_t dns_resolve_srv::targetlen
```

target字段的长度。

<a id="aaf1b0b289ffbeacd1df9cbcbad7f2563"></a>

### `weight`

```c
uint16_t dns_resolve_srv::weight
```

用于负载均衡（Load Balancing）的服务器权重。

本数据类型文档由以下文件生成：

- `zephyr/net/dns_resolve.h`

## 23.3\_原页交叉引用（Cross References）

- [zephyr/net/dns_resolve.h](https://docs.zephyrproject.org/latest/doxygen/html/dns__resolve_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P022_dns_resolve_private_结构体.md) · [返回大纲](大纲.md) · [下一章](P024_dns_resolve_txt_结构体.md)
