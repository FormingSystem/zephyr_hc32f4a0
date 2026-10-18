---
id: learning.zephyr-docs.network-core-model-reference.page-127
title: net_stats_dns_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__dns.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第127章\_net\_stats\_dns\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__dns.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

DNS统计信息（Statistics）。

```c
#include <zephyr/net/net_stats.h>
```

<a id="details"></a>

DNS统计信息（Statistics）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 127.1\_数据成员（Data Fields）

<a id="r_abc9be2039a3ff9e62b956ae27fd0ab84"></a>

```c
net_stats_t recv
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[recv](#abc9be2039a3ff9e62b956ae27fd0ab84)。

已接收的域名系统查询（DNS queries）数量。

<a id="r_ac07b9f4d084b978cc11e7799fb71a435"></a>

```c
net_stats_t sent
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[sent](#ac07b9f4d084b978cc11e7799fb71a435)。

已发送的域名系统响应（DNS responses）数量。

<a id="r_a04756603a183f35dbf6f55000556b546"></a>

```c
net_stats_t drop
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[drop](#a04756603a183f35dbf6f55000556b546)。

已丢弃的域名系统数据包（DNS packets）数量。

## 127.2\_详细说明（Detailed Documentation）

<a id="a04756603a183f35dbf6f55000556b546"></a>

### `drop`

```c
net_stats_t net_stats_dns::drop
```

已丢弃的域名系统数据包（DNS packets）数量。

<a id="abc9be2039a3ff9e62b956ae27fd0ab84"></a>

### `recv`

```c
net_stats_t net_stats_dns::recv
```

已接收的域名系统查询（DNS queries）数量。

<a id="ac07b9f4d084b978cc11e7799fb71a435"></a>

### `sent`

```c
net_stats_t net_stats_dns::sent
```

已发送的域名系统响应（DNS responses）数量。

本数据类型文档由以下文件生成：

- `zephyr/net/net_stats.h`

## 127.3\_原页交叉引用（Cross References）

- [zephyr/net/net_stats.h](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h_source.html)
- [net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P126_net_stats_bytes_结构体.md) · [返回大纲](大纲.md) · [下一章](P128_net_stats_eth_结构体.md)
