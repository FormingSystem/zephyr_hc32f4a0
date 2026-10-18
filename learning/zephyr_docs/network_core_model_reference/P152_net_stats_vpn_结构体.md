---
id: learning.zephyr-docs.network-core-model-reference.page-152
title: net_stats_vpn_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__vpn.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第152章\_net\_stats\_vpn\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__vpn.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

WireGuard虚拟专用网络（VPN）统计信息。

```c
#include <zephyr/net/wireguard.h>
```

<a id="details"></a>

WireGuard虚拟专用网络（VPN）统计信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 152.1\_数据成员（Data Fields）

<a id="r_abfc70aed88c4f037757f365e53acdcb9"></a>

```c
uint32_t keepalive_rx
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[keepalive_rx](#abfc70aed88c4f037757f365e53acdcb9)。

已接收的保活数据包（Keepalive packets）数量。

<a id="r_aa6c1df97501730a7efc279e97795d7d5"></a>

```c
uint32_t keepalive_tx
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[keepalive_tx](#aa6c1df97501730a7efc279e97795d7d5)。

已发送的保活数据包（Keepalive packets）数量。

<a id="r_a16018a6939274b078d555a25cede3f91"></a>

```c
uint32_t invalid_keepalive
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[invalid_keepalive](#a16018a6939274b078d555a25cede3f91)。

保活无效错误（Invalid keepalive errors）数量。

<a id="r_ac66dac12113dc1e71699587da25688c4"></a>

```c
uint32_t handshake_init_rx
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[handshake_init_rx](#ac66dac12113dc1e71699587da25688c4)。

已接收的握手初始化数据包（Handshake init packets）数量。

<a id="r_af3b87df2f50f042043830d946b3b0d8a"></a>

```c
uint32_t handshake_init_tx
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[handshake_init_tx](#af3b87df2f50f042043830d946b3b0d8a)。

已发送的握手初始化数据包（Handshake init packets）数量。

<a id="r_a65a6f590952602ec7c0981243443717a"></a>

```c
uint32_t handshake_resp_rx
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[handshake_resp_rx](#a65a6f590952602ec7c0981243443717a)。

已接收的握手响应数据包（Handshake response packets）数量。

<a id="r_a21f4d8739b17b6a4f4e7021036bf2e5d"></a>

```c
uint32_t handshake_resp_tx
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[handshake_resp_tx](#a21f4d8739b17b6a4f4e7021036bf2e5d)。

已发送的握手响应数据包（Handshake response packets）数量。

<a id="r_a526da409e515e96706053d1ba338b523"></a>

```c
uint32_t invalid_handshake
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[invalid_handshake](#a526da409e515e96706053d1ba338b523)。

握手无效错误（Invalid handshake errors）数量。

<a id="r_a6d4ec72b231a5896cc182dadc9668916"></a>

```c
uint32_t peer_not_found
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[peer_not_found](#a6d4ec72b231a5896cc182dadc9668916)。

未找到对等端错误（Peer not found errors）数量。

<a id="r_a27aed70a12946019541abe2dff8348f6"></a>

```c
uint32_t key_expired
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[key_expired](#a27aed70a12946019541abe2dff8348f6)。

密钥过期错误（Key expired errors）数量。

<a id="r_a3042940448514aa40f22bdbf16b56416"></a>

```c
uint32_t invalid_packet
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[invalid_packet](#a3042940448514aa40f22bdbf16b56416)。

无效数据包（Invalid packets）数量。

<a id="r_aba74653967d3235a132c2982a5a2f5ae"></a>

```c
uint32_t invalid_key
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[invalid_key](#aba74653967d3235a132c2982a5a2f5ae)。

密钥无效错误（Invalid key errors）数量。

<a id="r_a7c994e163e01ffc4efdda372f3c87399"></a>

```c
uint32_t invalid_mic
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[invalid_mic](#a7c994e163e01ffc4efdda372f3c87399)。

消息完整性码无效错误（Invalid MIC errors）数量。

<a id="r_adac60bd39ea0fb623184c438783d243e"></a>

```c
uint32_t invalid_packet_len
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[invalid_packet_len](#adac60bd39ea0fb623184c438783d243e)。

数据包长度无效错误（Invalid packet length errors）数量。

<a id="r_a11289adcdb8d08608425bedfde6bd143"></a>

```c
uint32_t invalid_cookie
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[invalid_cookie](#a11289adcdb8d08608425bedfde6bd143)。

Cookie 无效错误（Invalid cookie errors）数量。

<a id="r_a11d9999979ee421486b2af9288260187"></a>

```c
uint32_t invalid_mac1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[invalid_mac1](#a11d9999979ee421486b2af9288260187)。

MAC1 无效错误（Invalid MAC1 errors）数量。

<a id="r_a4b56c0355d183ef955203960ce158f38"></a>

```c
uint32_t invalid_mac2
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[invalid_mac2](#a4b56c0355d183ef955203960ce158f38)。

MAC2 无效错误（Invalid MAC2 errors）数量。

<a id="r_af40a96c70f8ab09f3f8a02317fafad6b"></a>

```c
uint32_t decrypt_failed
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[decrypt_failed](#af40a96c70f8ab09f3f8a02317fafad6b)。

解密失败错误（Decrypt failed errors）数量。

<a id="r_a625424c311d613f07f1451d82b30814d"></a>

```c
uint32_t drop_rx
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[drop_rx](#a625424c311d613f07f1451d82b30814d)。

已丢弃的接收数据包（RX packets）数量。

<a id="r_ada1951a74e4d7faf6ac2819e0cc6573f"></a>

```c
uint32_t drop_tx
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[drop_tx](#ada1951a74e4d7faf6ac2819e0cc6573f)。

已丢弃的发送数据包（TX packets）数量。

<a id="r_a056c976add7ee0ef33408a031e6f7197"></a>

```c
uint32_t alloc_failed
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[alloc_failed](#a056c976add7ee0ef33408a031e6f7197)。

分配失败（Allocation failures）次数。

<a id="r_af636ef839bd6e873cd3e88d2ca5dd535"></a>

```c
uint32_t invalid_ip_version
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[invalid_ip_version](#af636ef839bd6e873cd3e88d2ca5dd535)。

IP 版本无效（Invalid IP version）次数。

<a id="r_ab32df6f0be61194200cb0ca0b4719186"></a>

```c
uint32_t invalid_ip_family
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[invalid_ip_family](#ab32df6f0be61194200cb0ca0b4719186)。

IP 地址族无效（Invalid IP address family）次数。

<a id="r_a404ae2009f1c92c35a08efe2853afc01"></a>

```c
uint32_t denied_ip
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[denied_ip](#a404ae2009f1c92c35a08efe2853afc01)。

IP 地址被拒绝（Denied IP address）次数。

<a id="r_a9c481d278e8c345caea27cd74299e0d7"></a>

```c
uint32_t replay_error
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[replay_error](#a9c481d278e8c345caea27cd74299e0d7)。

重放错误（Replay errors）数量。

<a id="r_a6b95475546f9a8179d82348c7d3bd3ef"></a>

```c
uint32_t valid_rx
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[valid_rx](#a6b95475546f9a8179d82348c7d3bd3ef)。

已接收的有效数据包（Valid packets）数量。

<a id="r_ac199357ab8fbf13dceaefe40b3a12ce5"></a>

```c
uint32_t valid_tx
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[valid_tx](#ac199357ab8fbf13dceaefe40b3a12ce5)。

已发送的有效数据包（Valid packets）数量。

## 152.2\_详细说明（Detailed Documentation）

<a id="a056c976add7ee0ef33408a031e6f7197"></a>

### `alloc_failed`

```c
uint32_t net_stats_vpn::alloc_failed
```

分配失败（Allocation failures）次数。

<a id="af40a96c70f8ab09f3f8a02317fafad6b"></a>

### `decrypt_failed`

```c
uint32_t net_stats_vpn::decrypt_failed
```

解密失败错误（Decrypt failed errors）数量。

<a id="a404ae2009f1c92c35a08efe2853afc01"></a>

### `denied_ip`

```c
uint32_t net_stats_vpn::denied_ip
```

IP 地址被拒绝（Denied IP address）次数。

<a id="a625424c311d613f07f1451d82b30814d"></a>

### `drop_rx`

```c
uint32_t net_stats_vpn::drop_rx
```

已丢弃的接收数据包（RX packets）数量。

<a id="ada1951a74e4d7faf6ac2819e0cc6573f"></a>

### `drop_tx`

```c
uint32_t net_stats_vpn::drop_tx
```

已丢弃的发送数据包（TX packets）数量。

<a id="ac66dac12113dc1e71699587da25688c4"></a>

### `handshake_init_rx`

```c
uint32_t net_stats_vpn::handshake_init_rx
```

已接收的握手初始化数据包（Handshake init packets）数量。

<a id="af3b87df2f50f042043830d946b3b0d8a"></a>

### `handshake_init_tx`

```c
uint32_t net_stats_vpn::handshake_init_tx
```

已发送的握手初始化数据包（Handshake init packets）数量。

<a id="a65a6f590952602ec7c0981243443717a"></a>

### `handshake_resp_rx`

```c
uint32_t net_stats_vpn::handshake_resp_rx
```

已接收的握手响应数据包（Handshake response packets）数量。

<a id="a21f4d8739b17b6a4f4e7021036bf2e5d"></a>

### `handshake_resp_tx`

```c
uint32_t net_stats_vpn::handshake_resp_tx
```

已发送的握手响应数据包（Handshake response packets）数量。

<a id="a11289adcdb8d08608425bedfde6bd143"></a>

### `invalid_cookie`

```c
uint32_t net_stats_vpn::invalid_cookie
```

Cookie 无效错误（Invalid cookie errors）数量。

<a id="a526da409e515e96706053d1ba338b523"></a>

### `invalid_handshake`

```c
uint32_t net_stats_vpn::invalid_handshake
```

握手无效错误（Invalid handshake errors）数量。

<a id="ab32df6f0be61194200cb0ca0b4719186"></a>

### `invalid_ip_family`

```c
uint32_t net_stats_vpn::invalid_ip_family
```

IP 地址族无效（Invalid IP address family）次数。

<a id="af636ef839bd6e873cd3e88d2ca5dd535"></a>

### `invalid_ip_version`

```c
uint32_t net_stats_vpn::invalid_ip_version
```

IP 版本无效（Invalid IP version）次数。

<a id="a16018a6939274b078d555a25cede3f91"></a>

### `invalid_keepalive`

```c
uint32_t net_stats_vpn::invalid_keepalive
```

保活无效错误（Invalid keepalive errors）数量。

<a id="aba74653967d3235a132c2982a5a2f5ae"></a>

### `invalid_key`

```c
uint32_t net_stats_vpn::invalid_key
```

密钥无效错误（Invalid key errors）数量。

<a id="a11d9999979ee421486b2af9288260187"></a>

### `invalid_mac1`

```c
uint32_t net_stats_vpn::invalid_mac1
```

MAC1 无效错误（Invalid MAC1 errors）数量。

<a id="a4b56c0355d183ef955203960ce158f38"></a>

### `invalid_mac2`

```c
uint32_t net_stats_vpn::invalid_mac2
```

MAC2 无效错误（Invalid MAC2 errors）数量。

<a id="a7c994e163e01ffc4efdda372f3c87399"></a>

### `invalid_mic`

```c
uint32_t net_stats_vpn::invalid_mic
```

消息完整性码无效错误（Invalid MIC errors）数量。

<a id="a3042940448514aa40f22bdbf16b56416"></a>

### `invalid_packet`

```c
uint32_t net_stats_vpn::invalid_packet
```

无效数据包（Invalid packets）数量。

<a id="adac60bd39ea0fb623184c438783d243e"></a>

### `invalid_packet_len`

```c
uint32_t net_stats_vpn::invalid_packet_len
```

数据包长度无效错误（Invalid packet length errors）数量。

<a id="abfc70aed88c4f037757f365e53acdcb9"></a>

### `keepalive_rx`

```c
uint32_t net_stats_vpn::keepalive_rx
```

已接收的保活数据包（Keepalive packets）数量。

<a id="aa6c1df97501730a7efc279e97795d7d5"></a>

### `keepalive_tx`

```c
uint32_t net_stats_vpn::keepalive_tx
```

已发送的保活数据包（Keepalive packets）数量。

<a id="a27aed70a12946019541abe2dff8348f6"></a>

### `key_expired`

```c
uint32_t net_stats_vpn::key_expired
```

密钥过期错误（Key expired errors）数量。

<a id="a6d4ec72b231a5896cc182dadc9668916"></a>

### `peer_not_found`

```c
uint32_t net_stats_vpn::peer_not_found
```

未找到对等端错误（Peer not found errors）数量。

<a id="a9c481d278e8c345caea27cd74299e0d7"></a>

### `replay_error`

```c
uint32_t net_stats_vpn::replay_error
```

重放错误（Replay errors）数量。

<a id="a6b95475546f9a8179d82348c7d3bd3ef"></a>

### `valid_rx`

```c
uint32_t net_stats_vpn::valid_rx
```

已接收的有效数据包（Valid packets）数量。

<a id="ac199357ab8fbf13dceaefe40b3a12ce5"></a>

### `valid_tx`

```c
uint32_t net_stats_vpn::valid_tx
```

已发送的有效数据包（Valid packets）数量。

本数据类型文档由以下文件生成：

- `zephyr/net/wireguard.h`

## 152.3\_原页交叉引用（Cross References）

- [zephyr/net/wireguard.h](https://docs.zephyrproject.org/latest/doxygen/html/wireguard_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P151_net_stats_udp_结构体.md) · [返回大纲](大纲.md) · [下一章](P153_net_stats_wifi_结构体.md)
