---
id: learning.zephyr-docs.network-core-model-reference.page-151
title: net_stats_udp_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__udp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第151章\_net\_stats\_udp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__udp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

UDP统计信息（Statistics）。

```c
#include <zephyr/net/net_stats.h>
```

<a id="details"></a>

UDP统计信息（Statistics）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 151.1\_数据成员（Data Fields）

<a id="r_a2d884bf9106e60d430ffec7c7964a609"></a>

```c
net_stats_t drop
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[drop](#a2d884bf9106e60d430ffec7c7964a609)。

已丢弃的用户数据报协议报文段（UDP segments）数量。

<a id="r_a0ea91d85fe322661fb909f5e94e55a34"></a>

```c
net_stats_t recv
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[recv](#a0ea91d85fe322661fb909f5e94e55a34)。

已接收的用户数据报协议报文段（UDP segments）数量。

<a id="r_ab4e8228c221901d3ded55f3f823bfa1c"></a>

```c
net_stats_t sent
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[sent](#ab4e8228c221901d3ded55f3f823bfa1c)。

已发送的用户数据报协议报文段（UDP segments）数量。

<a id="r_a4c57d5f68ebda7981400729b9c7fe0f7"></a>

```c
net_stats_t chkerr
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[chkerr](#a4c57d5f68ebda7981400729b9c7fe0f7)。

校验和错误（Bad checksum）的 UDP 报文段数量。

## 151.2\_详细说明（Detailed Documentation）

<a id="a4c57d5f68ebda7981400729b9c7fe0f7"></a>

### `chkerr`

```c
net_stats_t net_stats_udp::chkerr
```

校验和错误（Bad checksum）的 UDP 报文段数量。

<a id="a2d884bf9106e60d430ffec7c7964a609"></a>

### `drop`

```c
net_stats_t net_stats_udp::drop
```

已丢弃的用户数据报协议报文段（UDP segments）数量。

<a id="a0ea91d85fe322661fb909f5e94e55a34"></a>

### `recv`

```c
net_stats_t net_stats_udp::recv
```

已接收的用户数据报协议报文段（UDP segments）数量。

<a id="ab4e8228c221901d3ded55f3f823bfa1c"></a>

### `sent`

```c
net_stats_t net_stats_udp::sent
```

已发送的用户数据报协议报文段（UDP segments）数量。

本数据类型文档由以下文件生成：

- `zephyr/net/net_stats.h`

## 151.3\_原页交叉引用（Cross References）

- [zephyr/net/net_stats.h](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h_source.html)
- [net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P150_net_stats_tx_time_结构体.md) · [返回大纲](大纲.md) · [下一章](P152_net_stats_vpn_结构体.md)
