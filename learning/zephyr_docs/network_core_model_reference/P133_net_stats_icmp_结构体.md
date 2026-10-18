---
id: learning.zephyr-docs.network-core-model-reference.page-133
title: net_stats_icmp_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__icmp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第133章\_net\_stats\_icmp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__icmp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

互联网控制消息协议（ICMP）统计信息。

```c
#include <zephyr/net/net_stats.h>
```

<a id="details"></a>

互联网控制消息协议（ICMP）统计信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 133.1\_数据成员（Data Fields）

<a id="r_ae6f226b55565c11fca0c9e099f08c267"></a>

```c
net_stats_t recv
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[recv](#ae6f226b55565c11fca0c9e099f08c267)。

已接收的互联网控制消息协议数据包（ICMP packets）数量。

<a id="r_a2d6eb7dfc8f4b439b399b039022f2889"></a>

```c
net_stats_t sent
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[sent](#a2d6eb7dfc8f4b439b399b039022f2889)。

已发送的互联网控制消息协议数据包（ICMP packets）数量。

<a id="r_a755f3388c05d4bd2988ddd16d1a4cf32"></a>

```c
net_stats_t drop
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[drop](#a755f3388c05d4bd2988ddd16d1a4cf32)。

已丢弃的互联网控制消息协议数据包（ICMP packets）数量。

<a id="r_ae1a29dd9b8e1ce9a737fa7f36c805cd4"></a>

```c
net_stats_t typeerr
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[typeerr](#ae1a29dd9b8e1ce9a737fa7f36c805cd4)。

类型错误的 ICMP 数据包（Wrong type）数量。

<a id="r_a6662bc547107a08c52e902a2446629bf"></a>

```c
net_stats_t chkerr
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[chkerr](#a6662bc547107a08c52e902a2446629bf)。

校验和错误的 ICMP 数据包（Bad checksum）数量。

## 133.2\_详细说明（Detailed Documentation）

<a id="a6662bc547107a08c52e902a2446629bf"></a>

### `chkerr`

```c
net_stats_t net_stats_icmp::chkerr
```

校验和错误的 ICMP 数据包（Bad checksum）数量。

<a id="a755f3388c05d4bd2988ddd16d1a4cf32"></a>

### `drop`

```c
net_stats_t net_stats_icmp::drop
```

已丢弃的互联网控制消息协议数据包（ICMP packets）数量。

<a id="ae6f226b55565c11fca0c9e099f08c267"></a>

### `recv`

```c
net_stats_t net_stats_icmp::recv
```

已接收的互联网控制消息协议数据包（ICMP packets）数量。

<a id="a2d6eb7dfc8f4b439b399b039022f2889"></a>

### `sent`

```c
net_stats_t net_stats_icmp::sent
```

已发送的互联网控制消息协议数据包（ICMP packets）数量。

<a id="ae1a29dd9b8e1ce9a737fa7f36c805cd4"></a>

### `typeerr`

```c
net_stats_t net_stats_icmp::typeerr
```

类型错误的 ICMP 数据包（Wrong type）数量。

本数据类型文档由以下文件生成：

- `zephyr/net/net_stats.h`

## 133.3\_原页交叉引用（Cross References）

- [zephyr/net/net_stats.h](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h_source.html)
- [net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P132_net_stats_eth_hw_timestamp_结构体.md) · [返回大纲](大纲.md) · [下一章](P134_net_stats_ip_结构体.md)
