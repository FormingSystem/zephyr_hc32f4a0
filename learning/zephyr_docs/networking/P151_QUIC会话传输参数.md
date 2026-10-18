---
id: learning.zephyr-docs.networking.api-151
title: QUIC会话传输参数
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structquic__session__transport__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第151章\_QUIC会话传输参数

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structquic__session__transport__params.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 151.1\_阅读说明与来源

译注：先读[QUIC传输接口指南](P143_QUIC传输接口.md)及[回显示例目录](P144_QUIC示例目录.md)，理解连接套接字、流套接字和 TLS 握手的关系，再按符号查询本组参考。

本组：[完整API参考](P147_QUIC完整API参考.md) · [头文件参考](P148_QUIC头文件参考.md) · [头文件源码](P149_QUIC头文件源码.md) · [会话状态](P150_QUIC会话状态.md) · [会话传输参数](P151_QUIC会话传输参数.md) · [统计数据](P152_QUIC统计数据.md) · [全局统计](P153_QUIC全局统计数据.md)。

为会话恢复保存的对端传输参数（Remembered Peer Transport Parameters）。

```c
#include <zephyr/net/quic.h>
```

为会话恢复保存的对端传输参数（Remembered Peer Transport Parameters）。它们是与所存票据关联的服务端限制，用于初始化早期流量控制状态，并校验后续支持 0-RTT 的恢复尝试。

## 151.2\_数据成员（Data Fields）

<a id="r_a841404605dc741a8f3d52e31e9d2f102"></a>

```c
bool valid
```

存在已保存的传输参数快照（Snapshot）时为 `true`。

<a id="r_af782abfbd2085b9454f2a3341c3346e2"></a>

```c
uint64_t initial_max_data
```

保存的 `initial_max_data`。

<a id="r_ad8219a81f06c0977fd25721061c2bf9c"></a>

```c
uint64_t initial_max_stream_data_bidi_local
```

保存的 `initial_max_stream_data_bidi_local`。

<a id="r_a5ea1c1f18506ac03b9c40effd843e1a2"></a>

```c
uint64_t initial_max_stream_data_bidi_remote
```

保存的 `initial_max_stream_data_bidi_remote`。

<a id="r_a025a059a8b630be61e128cd108bea4ad"></a>

```c
uint64_t initial_max_stream_data_uni
```

保存的 `initial_max_stream_data_uni`。

<a id="r_a8955b20664d98dc46956e54fae75ac3c"></a>

```c
uint64_t initial_max_streams_bidi
```

保存的 `initial_max_streams_bidi`。

<a id="r_a7ddc746aa834fbc97192f99ca5042128"></a>

```c
uint64_t initial_max_streams_uni
```

保存的 `initial_max_streams_uni`。

<a id="r_aa8ddb2d0324be686e4de72ce46d6de1b"></a>

```c
uint64_t max_idle_timeout
```

保存的 `max_idle_timeout`，单位毫秒。

<a id="r_af5b1546f88f1713ffd4d7fa2c54dbeb0"></a>

```c
uint16_t max_udp_payload_size
```

保存的 `max_udp_payload_size`。

## 151.3\_详细说明（Detailed Documentation）

<a id="af782abfbd2085b9454f2a3341c3346e2"></a>

### `initial_max_data`

```c
uint64_t quic_session_transport_params::initial_max_data
```

保存的 `initial_max_data`。

<a id="ad8219a81f06c0977fd25721061c2bf9c"></a>

### `initial_max_stream_data_bidi_local`

```c
uint64_t quic_session_transport_params::initial_max_stream_data_bidi_local
```

保存的 `initial_max_stream_data_bidi_local`。

<a id="a5ea1c1f18506ac03b9c40effd843e1a2"></a>

### `initial_max_stream_data_bidi_remote`

```c
uint64_t quic_session_transport_params::initial_max_stream_data_bidi_remote
```

保存的 `initial_max_stream_data_bidi_remote`。

<a id="a025a059a8b630be61e128cd108bea4ad"></a>

### `initial_max_stream_data_uni`

```c
uint64_t quic_session_transport_params::initial_max_stream_data_uni
```

保存的 `initial_max_stream_data_uni`。

<a id="a8955b20664d98dc46956e54fae75ac3c"></a>

### `initial_max_streams_bidi`

```c
uint64_t quic_session_transport_params::initial_max_streams_bidi
```

保存的 `initial_max_streams_bidi`。

<a id="a7ddc746aa834fbc97192f99ca5042128"></a>

### `initial_max_streams_uni`

```c
uint64_t quic_session_transport_params::initial_max_streams_uni
```

保存的 `initial_max_streams_uni`。

<a id="aa8ddb2d0324be686e4de72ce46d6de1b"></a>

### `max_idle_timeout`

```c
uint64_t quic_session_transport_params::max_idle_timeout
```

保存的 `max_idle_timeout`，单位毫秒。

<a id="af5b1546f88f1713ffd4d7fa2c54dbeb0"></a>

### `max_udp_payload_size`

```c
uint16_t quic_session_transport_params::max_udp_payload_size
```

保存的 `max_udp_payload_size`。

<a id="a841404605dc741a8f3d52e31e9d2f102"></a>

### `valid`

```c
bool quic_session_transport_params::valid
```

存在已保存的传输参数快照（Snapshot）时为 `true`。

## 151.4\_相关源码与使用边界

声明来自 `<zephyr/net/quic.h>`。本仓库的[对应头文件](../../../include/zephyr/net/quic.h)可用于源码追踪，版本可能与官网 `latest` 不同；官方原始头文件及实现的读取摘要见[来源记录](../SOURCES.md)。

> 译注：这里保存的是对端（服务端）通告参数，因此 `bidi_local`／`bidi_remote` 的命名视角不能随意换成当前客户端视角。`valid` 只表示快照存在，不保证未来恢复一定获准，也不代替对实际新连接参数的校验；配置项含义可与[指南中的传输参数表](P143_QUIC传输接口.md)对照。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P150_QUIC会话状态.md) · [返回大纲](大纲.md) · [下一章](P152_QUIC统计数据.md)
