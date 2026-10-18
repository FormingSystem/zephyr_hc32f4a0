---
id: learning.zephyr-docs.networking.api-152
title: QUIC统计数据
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__quic.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第152章\_QUIC统计数据

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__quic.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 152.1\_阅读说明与来源

译注：先读[QUIC传输接口指南](P143_QUIC传输接口.md)及[回显示例目录](P144_QUIC示例目录.md)，理解连接套接字、流套接字和 TLS 握手的关系，再按符号查询本组参考。

本组：[完整API参考](P147_QUIC完整API参考.md) · [头文件参考](P148_QUIC头文件参考.md) · [头文件源码](P149_QUIC头文件源码.md) · [会话状态](P150_QUIC会话状态.md) · [会话传输参数](P151_QUIC会话传输参数.md) · [统计数据](P152_QUIC统计数据.md) · [全局统计](P153_QUIC全局统计数据.md)。

QUIC 统计数据（QUIC Statistics）。

```c
#include <zephyr/net/quic.h>
```

QUIC 统计数据（QUIC Statistics）。

## 152.2\_数据成员（Data Fields）

<a id="r_a1cb94d0aad126499605ff0fd55a9c921"></a>

```c
uint32_t handshake_init_rx
```

收到的握手初始包（Handshake Init Packet）数量。

<a id="r_abc28dda5b520ed707fd757ba18e5446f"></a>

```c
uint32_t handshake_init_tx
```

发出的握手初始包数量。

<a id="r_a9e6c36c55d518d601d18c213ab957f7a"></a>

```c
uint32_t handshake_resp_rx
```

收到的握手响应包（Handshake Response Packet）数量。

<a id="r_ac821e5206622610f1ac6619901d4aa0d"></a>

```c
uint32_t handshake_resp_tx
```

发出的握手响应包数量。

<a id="r_ae8510e001e5188474836ce808eb3fe73"></a>

```c
uint32_t invalid_handshake
```

无效握手错误（Invalid Handshake Error）的数量。

<a id="r_ab654695fadc0e6c8f12b19d32ac3b557"></a>

```c
uint32_t peer_not_found
```

未找到对端错误（Peer Not Found Error）的数量。

<a id="r_a98554e8744477353c9d68377ea2717e8"></a>

```c
uint32_t invalid_packet
```

无效包（Invalid Packet）的数量。

<a id="r_ab940f3fa00526b78c9e25f664635b2cc"></a>

```c
uint32_t invalid_key
```

无效密钥错误（Invalid Key Error）的数量。

<a id="r_a379af69fa7b7709ceeb59ff5f69f9f0d"></a>

```c
uint32_t invalid_packet_len
```

无效包长度错误（Invalid Packet Length Error）的数量。

<a id="r_a1fc16ecebf7520992168960c1075c7ea"></a>

```c
uint32_t decrypt_failed
```

解密失败错误（Decryption Failure）的数量。

<a id="r_a37ed9533ed28547b796a96806e96d3f2"></a>

```c
uint32_t drop_rx
```

丢弃的接收包（RX Packet）的数量。

<a id="r_a3295a98cb2d8739d1162024f82e8fabd"></a>

```c
uint32_t drop_tx
```

丢弃的发送包（TX Packet）的数量。

<a id="r_a4f0635d82af4c8820b881f700733f4c6"></a>

```c
uint32_t alloc_failed
```

分配失败（Allocation Failure）的次数。

<a id="r_a71ab60160b7053da6f65b34f6940ac5c"></a>

```c
uint32_t valid_rx
```

收到的有效包（Valid Packet）的数量。

<a id="r_abd662d512982b4dcda59551a828fd768"></a>

```c
uint32_t valid_tx
```

发出的有效包的数量。

## 152.3\_详细说明（Detailed Documentation）

<a id="a4f0635d82af4c8820b881f700733f4c6"></a>

### `alloc_failed`

```c
uint32_t net_stats_quic::alloc_failed
```

分配失败（Allocation Failure）的次数。

<a id="a1fc16ecebf7520992168960c1075c7ea"></a>

### `decrypt_failed`

```c
uint32_t net_stats_quic::decrypt_failed
```

解密失败错误（Decryption Failure）的数量。

<a id="a37ed9533ed28547b796a96806e96d3f2"></a>

### `drop_rx`

```c
uint32_t net_stats_quic::drop_rx
```

丢弃的接收包（RX Packet）的数量。

<a id="a3295a98cb2d8739d1162024f82e8fabd"></a>

### `drop_tx`

```c
uint32_t net_stats_quic::drop_tx
```

丢弃的发送包（TX Packet）的数量。

<a id="a1cb94d0aad126499605ff0fd55a9c921"></a>

### `handshake_init_rx`

```c
uint32_t net_stats_quic::handshake_init_rx
```

收到的握手初始包（Handshake Init Packet）数量。

<a id="abc28dda5b520ed707fd757ba18e5446f"></a>

### `handshake_init_tx`

```c
uint32_t net_stats_quic::handshake_init_tx
```

发出的握手初始包数量。

<a id="a9e6c36c55d518d601d18c213ab957f7a"></a>

### `handshake_resp_rx`

```c
uint32_t net_stats_quic::handshake_resp_rx
```

收到的握手响应包（Handshake Response Packet）数量。

<a id="ac821e5206622610f1ac6619901d4aa0d"></a>

### `handshake_resp_tx`

```c
uint32_t net_stats_quic::handshake_resp_tx
```

发出的握手响应包数量。

<a id="ae8510e001e5188474836ce808eb3fe73"></a>

### `invalid_handshake`

```c
uint32_t net_stats_quic::invalid_handshake
```

无效握手错误（Invalid Handshake Error）的数量。

<a id="ab940f3fa00526b78c9e25f664635b2cc"></a>

### `invalid_key`

```c
uint32_t net_stats_quic::invalid_key
```

无效密钥错误（Invalid Key Error）的数量。

<a id="a98554e8744477353c9d68377ea2717e8"></a>

### `invalid_packet`

```c
uint32_t net_stats_quic::invalid_packet
```

无效包（Invalid Packet）的数量。

<a id="a379af69fa7b7709ceeb59ff5f69f9f0d"></a>

### `invalid_packet_len`

```c
uint32_t net_stats_quic::invalid_packet_len
```

无效包长度错误（Invalid Packet Length Error）的数量。

<a id="ab654695fadc0e6c8f12b19d32ac3b557"></a>

### `peer_not_found`

```c
uint32_t net_stats_quic::peer_not_found
```

未找到对端错误（Peer Not Found Error）的数量。

<a id="a71ab60160b7053da6f65b34f6940ac5c"></a>

### `valid_rx`

```c
uint32_t net_stats_quic::valid_rx
```

收到的有效包（Valid Packet）的数量。

<a id="abd662d512982b4dcda59551a828fd768"></a>

### `valid_tx`

```c
uint32_t net_stats_quic::valid_tx
```

发出的有效包的数量。

## 152.4\_相关源码与使用边界

声明来自 `<zephyr/net/quic.h>`。本仓库的[对应头文件](../../../include/zephyr/net/quic.h)可用于源码追踪，版本可能与官网 `latest` 不同；官方原始头文件及实现的读取摘要见[来源记录](../SOURCES.md)。

> 译注：本页定义计数字段，不提供采样周期、吞吐量单位或独立读取函数。打开／关闭的总数和错误次数不是当前活动连接数；不要把所有错误字段简单相加当作丢包总数。统计启用及网络 Shell 使用见[网络统计](P093_网络统计.md)与[网络Shell](P092_网络Shell.md)，具体字段更新位置以所用版本源码为准。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P151_QUIC会话传输参数.md) · [返回大纲](大纲.md) · [下一章](P153_QUIC全局统计数据.md)
