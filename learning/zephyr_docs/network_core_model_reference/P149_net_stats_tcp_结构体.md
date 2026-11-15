---
id: learning.zephyr-docs.network-core-model-reference.page-149
title: net_stats_tcp_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__tcp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第149章\_net\_stats\_tcp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__tcp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

TCP统计信息（Statistics）。

```c
#include <zephyr/net/net_stats.h>
```

<a id="details"></a>

TCP统计信息（Statistics）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 149.1\_数据成员（Data Fields）

<a id="r_af80c18bcc253133ce5f0597ac190b349"></a>

```c
struct net_stats_bytes bytes
```

相关声明：[net_stats_bytes](P126_net_stats_bytes_结构体.md)、[bytes](#af80c18bcc253133ce5f0597ac190b349)。

接收与发送的传输控制协议应用数据量（TCP application data）。

<a id="r_abe567032cb4a267a984aec28c1e3cca4"></a>

```c
net_stats_t resent
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[resent](#abe567032cb4a267a984aec28c1e3cca4)。

重传数据量（Retransmitted data）。

<a id="r_aa549f7b6d5828009a09190fd64afa8e3"></a>

```c
net_stats_t drop
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[drop](#aa549f7b6d5828009a09190fd64afa8e3)。

TCP 层丢弃的数据包数量（Dropped packets）。

<a id="r_ad25edb2b39a6acc8152c35ad43a5042f"></a>

```c
net_stats_t recv
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[recv](#ad25edb2b39a6acc8152c35ad43a5042f)。

已接收的 TCP 报文段（Segments）数量。

<a id="r_aa987bebf96000b6b4e92bfafc218759a"></a>

```c
net_stats_t sent
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[sent](#aa987bebf96000b6b4e92bfafc218759a)。

已发送的 TCP 报文段（Segments）数量。

<a id="r_a5f045704859331918511e9c2281ac155"></a>

```c
net_stats_t seg_drop
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[seg_drop](#a5f045704859331918511e9c2281ac155)。

已丢弃的 TCP 报文段（Segments）数量。

<a id="r_a5099e174b0eafa322f0630f1f5c73a8b"></a>

```c
net_stats_t chkerr
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[chkerr](#a5099e174b0eafa322f0630f1f5c73a8b)。

校验和错误（Bad checksum）的 TCP 报文段数量。

<a id="r_a0d40abc85776f0a9b9510a909b7f6d18"></a>

```c
net_stats_t ackerr
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[ackerr](#a0d40abc85776f0a9b9510a909b7f6d18)。

接收到的确认号错误（Bad ACK number）的 TCP 报文段数量。

<a id="r_a471fcd5578f79ce77d20547b28503ac1"></a>

```c
net_stats_t rsterr
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[rsterr](#a471fcd5578f79ce77d20547b28503ac1)。

接收到的错误 TCP 复位报文段（Bad TCP RST segments）数量。

<a id="r_aa618cf86b962aca0f14eb9178c8ae61a"></a>

```c
net_stats_t rst
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[rst](#aa618cf86b962aca0f14eb9178c8ae61a)。

已接收的 TCP 复位报文段（TCP RST segments）数量。

<a id="r_a4a4ea6e5d87ef58b4271bd708cf39635"></a>

```c
net_stats_t rexmit
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[rexmit](#a4a4ea6e5d87ef58b4271bd708cf39635)。

已重传的 TCP 报文段（Retransmitted TCP segments）数量。

<a id="r_ac557ac0d8917bc2c2dfed74126f993c8"></a>

```c
net_stats_t conndrop
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[conndrop](#ac557ac0d8917bc2c2dfed74126f993c8)。

因可用连接数量不足而丢弃的连接尝试（Connection attempts）数量。

<a id="r_a67f55954a4c51f2b957c7d974e78c1c0"></a>

```c
net_stats_t connrst
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[connrst](#a67f55954a4c51f2b957c7d974e78c1c0)。

针对关闭端口发起、因而触发复位（RST）的连接尝试数量。

## 149.2\_详细说明（Detailed Documentation）

<a id="a0d40abc85776f0a9b9510a909b7f6d18"></a>

### `ackerr`

```c
net_stats_t net_stats_tcp::ackerr
```

接收到的确认号错误（Bad ACK number）的 TCP 报文段数量。

<a id="af80c18bcc253133ce5f0597ac190b349"></a>

### `bytes`

```c
struct net_stats_bytes net_stats_tcp::bytes
```

接收与发送的传输控制协议应用数据量（TCP application data）。

<a id="a5099e174b0eafa322f0630f1f5c73a8b"></a>

### `chkerr`

```c
net_stats_t net_stats_tcp::chkerr
```

校验和错误（Bad checksum）的 TCP 报文段数量。

<a id="ac557ac0d8917bc2c2dfed74126f993c8"></a>

### `conndrop`

```c
net_stats_t net_stats_tcp::conndrop
```

因可用连接数量不足而丢弃的连接尝试（Connection attempts）数量。

<a id="a67f55954a4c51f2b957c7d974e78c1c0"></a>

### `connrst`

```c
net_stats_t net_stats_tcp::connrst
```

针对关闭端口发起、因而触发复位（RST）的连接尝试数量。

<a id="aa549f7b6d5828009a09190fd64afa8e3"></a>

### `drop`

```c
net_stats_t net_stats_tcp::drop
```

TCP 层丢弃的数据包数量（Dropped packets）。

<a id="ad25edb2b39a6acc8152c35ad43a5042f"></a>

### `recv`

```c
net_stats_t net_stats_tcp::recv
```

已接收的 TCP 报文段（Segments）数量。

<a id="abe567032cb4a267a984aec28c1e3cca4"></a>

### `resent`

```c
net_stats_t net_stats_tcp::resent
```

重传数据量（Retransmitted data）。

<a id="a4a4ea6e5d87ef58b4271bd708cf39635"></a>

### `rexmit`

```c
net_stats_t net_stats_tcp::rexmit
```

已重传的 TCP 报文段（Retransmitted TCP segments）数量。

<a id="aa618cf86b962aca0f14eb9178c8ae61a"></a>

### `rst`

```c
net_stats_t net_stats_tcp::rst
```

已接收的 TCP 复位报文段（TCP RST segments）数量。

<a id="a471fcd5578f79ce77d20547b28503ac1"></a>

### `rsterr`

```c
net_stats_t net_stats_tcp::rsterr
```

接收到的错误 TCP 复位报文段（Bad TCP RST segments）数量。

<a id="a5f045704859331918511e9c2281ac155"></a>

### `seg_drop`

```c
net_stats_t net_stats_tcp::seg_drop
```

已丢弃的 TCP 报文段（Segments）数量。

<a id="aa987bebf96000b6b4e92bfafc218759a"></a>

### `sent`

```c
net_stats_t net_stats_tcp::sent
```

已发送的 TCP 报文段（Segments）数量。

本数据类型文档由以下文件生成：

- `zephyr/net/net_stats.h`

## 149.3\_原页交叉引用（Cross References）

- [zephyr/net/net_stats.h](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h_source.html)
- [net_stats_bytes](P126_net_stats_bytes_结构体.md)
- [net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P148_net_stats_tc_结构体.md) · [返回大纲](大纲.md) · [下一章](P150_net_stats_tx_time_结构体.md)
