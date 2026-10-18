---
id: learning.zephyr-docs.networking.api-153
title: QUIC全局统计数据
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__quic__global.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第153章\_QUIC全局统计数据

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__quic__global.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 153.1\_阅读说明与来源

译注：先读[QUIC传输接口指南](P143_QUIC传输接口.md)及[回显示例目录](P144_QUIC示例目录.md)，理解连接套接字、流套接字和 TLS 握手的关系，再按符号查询本组参考。

本组：[完整API参考](P147_QUIC完整API参考.md) · [头文件参考](P148_QUIC头文件参考.md) · [头文件源码](P149_QUIC头文件源码.md) · [会话状态](P150_QUIC会话状态.md) · [会话传输参数](P151_QUIC会话传输参数.md) · [统计数据](P152_QUIC统计数据.md) · [全局统计](P153_QUIC全局统计数据.md)。

QUIC 全局统计数据（QUIC Global Statistics）。

```c
#include <zephyr/net/quic.h>
```

QUIC 全局统计数据（QUIC Global Statistics）。

## 153.2\_数据成员（Data Fields）

<a id="r_aeee6bcc9a4e292bbda5279caeddcfad7"></a>

```c
uint32_t packets_rx
```

收到的所有包的数量，包括有效包和无效包。

<a id="r_ab42d5446da9d7316b6ebb3cbf82a2dea"></a>

```c
uint32_t connections_opened
```

打开的连接总数（Connections Opened）。

<a id="r_a828ecf5f479709cbcb3efcec3e3378b8"></a>

```c
uint32_t connections_closed
```

关闭的连接总数（Connections Closed）。

<a id="r_ac7072fb6d9d5a4fe500f2b2ce44cb38b"></a>

```c
uint32_t streams_opened
```

打开的流总数（Streams Opened）。

<a id="r_a4dc2127f494e0d30a77476d64c5a6618"></a>

```c
uint32_t streams_closed
```

关闭的流总数（Streams Closed）。

<a id="r_aa19241ebc473b9f1433455f53ee663bd"></a>

```c
uint32_t connection_open_failed
```

打开连接失败的总次数（Connection Open Failures）。

<a id="r_a93a56f2b3e09fde2b1e0a06e1d109c1c"></a>

```c
uint32_t stream_open_failed
```

打开流失败的总次数（Stream Open Failures）。

<a id="r_a5aff8a6fc934624e6f400c95f5e5a1d0"></a>

```c
uint32_t connection_close_failed
```

关闭连接失败的总次数（Connection Close Failures）。

<a id="r_a61f59a107c296f0bf12b39edc699c3a7"></a>

```c
uint32_t stream_close_failed
```

关闭流失败的总次数（Stream Close Failures）。

## 153.3\_详细说明（Detailed Documentation）

<a id="a5aff8a6fc934624e6f400c95f5e5a1d0"></a>

### `connection_close_failed`

```c
uint32_t net_stats_quic_global::connection_close_failed
```

关闭连接失败的总次数（Connection Close Failures）。

<a id="aa19241ebc473b9f1433455f53ee663bd"></a>

### `connection_open_failed`

```c
uint32_t net_stats_quic_global::connection_open_failed
```

打开连接失败的总次数（Connection Open Failures）。

<a id="a828ecf5f479709cbcb3efcec3e3378b8"></a>

### `connections_closed`

```c
uint32_t net_stats_quic_global::connections_closed
```

关闭的连接总数（Connections Closed）。

<a id="ab42d5446da9d7316b6ebb3cbf82a2dea"></a>

### `connections_opened`

```c
uint32_t net_stats_quic_global::connections_opened
```

打开的连接总数（Connections Opened）。

<a id="aeee6bcc9a4e292bbda5279caeddcfad7"></a>

### `packets_rx`

```c
uint32_t net_stats_quic_global::packets_rx
```

收到的所有包的数量，包括有效包和无效包。

<a id="a61f59a107c296f0bf12b39edc699c3a7"></a>

### `stream_close_failed`

```c
uint32_t net_stats_quic_global::stream_close_failed
```

关闭流失败的总次数（Stream Close Failures）。

<a id="a93a56f2b3e09fde2b1e0a06e1d109c1c"></a>

### `stream_open_failed`

```c
uint32_t net_stats_quic_global::stream_open_failed
```

打开流失败的总次数（Stream Open Failures）。

<a id="a4dc2127f494e0d30a77476d64c5a6618"></a>

### `streams_closed`

```c
uint32_t net_stats_quic_global::streams_closed
```

关闭的流总数（Streams Closed）。

<a id="ac7072fb6d9d5a4fe500f2b2ce44cb38b"></a>

### `streams_opened`

```c
uint32_t net_stats_quic_global::streams_opened
```

打开的流总数（Streams Opened）。

## 153.4\_相关源码与使用边界

声明来自 `<zephyr/net/quic.h>`。本仓库的[对应头文件](../../../include/zephyr/net/quic.h)可用于源码追踪，版本可能与官网 `latest` 不同；官方原始头文件及实现的读取摘要见[来源记录](../SOURCES.md)。

> 译注：本页定义计数字段，不提供采样周期、吞吐量单位或独立读取函数。打开／关闭的总数和错误次数不是当前活动连接数；不要把所有错误字段简单相加当作丢包总数。统计启用及网络 Shell 使用见[网络统计](P093_网络统计.md)与[网络Shell](P092_网络Shell.md)，具体字段更新位置以所用版本源码为准。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P152_QUIC统计数据.md) · [返回大纲](大纲.md) · [下一章](P154_网络跟踪.md)
