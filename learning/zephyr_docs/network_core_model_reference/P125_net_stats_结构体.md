---
id: learning.zephyr-docs.network-core-model-reference.page-125
title: net_stats_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第125章\_net\_stats\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

在一个结构中保存全部网络统计信息（Network Statistics）。

```c
#include <zephyr/net/net_stats.h>
```

<a id="details"></a>

在一个结构中保存全部网络统计信息（Network Statistics）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 125.1\_数据成员（Data Fields）

<a id="r_a7a28233e6d23efdce0143469b9bb6c05"></a>

```c
struct net_stats_bytes bytes
```

相关声明：[net_stats_bytes](P126_net_stats_bytes_结构体.md)、[bytes](#a7a28233e6d23efdce0143469b9bb6c05)。

统计通过所有网络接口（Network interfaces）传输的数据量。

<a id="r_a3a4c90661d6b310b628262228a341fe2"></a>

```c
net_stats_t processing_error
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[processing_error](#a3a4c90661d6b310b628262228a341fe2)。

格式错误（Malformed）或没有对应处理程序的数据包数量。

<a id="r_ac42cb13954d164e92a1ef60919a2a34e"></a>

```c
struct net_stats_ip_errors ip_errors
```

相关声明：[net_stats_ip_errors](P135_net_stats_ip_errors_结构体.md)、[ip_errors](#ac42cb13954d164e92a1ef60919a2a34e)。

IP 层错误（IP layer errors）。

## 125.2\_详细说明（Detailed Documentation）

<a id="a7a28233e6d23efdce0143469b9bb6c05"></a>

### `bytes`

```c
struct net_stats_bytes net_stats::bytes
```

统计通过所有网络接口（Network interfaces）传输的数据量。

<a id="ac42cb13954d164e92a1ef60919a2a34e"></a>

### `ip_errors`

```c
struct net_stats_ip_errors net_stats::ip_errors
```

IP 层错误（IP layer errors）。

<a id="a3a4c90661d6b310b628262228a341fe2"></a>

### `processing_error`

```c
net_stats_t net_stats::processing_error
```

格式错误（Malformed）或没有对应处理程序的数据包数量。

本数据类型文档由以下文件生成：

- `zephyr/net/net_stats.h`

## 125.3\_原页交叉引用（Cross References）

- [zephyr/net/net_stats.h](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h_source.html)
- [net_stats_bytes](P126_net_stats_bytes_结构体.md)
- [net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)
- [net_stats_ip_errors](P135_net_stats_ip_errors_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P124_net_socket_service_event_结构体.md) · [返回大纲](大纲.md) · [下一章](P126_net_stats_bytes_结构体.md)
