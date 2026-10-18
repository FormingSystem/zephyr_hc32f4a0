---
id: learning.zephyr-docs.api-file-network-pcie-reference.page-9
title: zephyr__net__net_pkt.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_zephyr\_\_net\_\_net\_pkt.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络数据包缓冲区描述符（Network Packet Buffer Descriptor）的API。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <stdbool.h>
#include <zephyr/net_buf.h>
#include <zephyr/net/net_core.h>
#include <zephyr/net/net_linkaddr.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/net_context.h>
#include <zephyr/net/net_time.h>
#include <zephyr/net/ethernet_vlan.h>
#include <zephyr/net/ptp_time.h>
#include <zephyr/logging/log_core.h>
```

查看此文件的源码。

网络数据包缓冲区描述符 API（Network Packet Buffer Descriptor API）。注意（Note）：此结构体不具备线程安全性（Thread Safety）。对于给定的 `net_pkt` 实例，同一时刻应只有一个线程访问，即采用独占所有权模型（Exclusive Ownership Model）。网络数据通过 `net_buf` 结构体在协议栈不同部分之间传递。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.1\_数据结构（Data Structures）

<a id="r_net_5Fpkt"></a>

```c
struct net_pkt
```

相关声明：[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

网络数据包（Network Packet）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.2\_宏定义（Macros）

<a id="r_gad63d4802ad4e10b89829aed35a9ae804"></a>

```c
#define NET_PKT_FRAG_FOR_EACH(_pkt, _var)
```

相关声明：[NET_PKT_FRAG_FOR_EACH](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gad63d4802ad4e10b89829aed35a9ae804)。

遍历网络数据包（Network Packet）的全部分片（Fragments）。

<a id="r_gafc7e98d5b64d816faabcbaa2ec22a2bb"></a>

```c
#define NET_PKT_SLAB_DEFINE(name, count)
```

相关声明：[NET_PKT_SLAB_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gafc7e98d5b64d816faabcbaa2ec22a2bb)。

创建 `net_pkt` 内存块池（Slab）。

<a id="r_ga94ab6300b59d739c4e3c5604d3fbe8a5"></a>

```c
#define NET_PKT_DATA_POOL_DEFINE(name, count)
```

相关声明：[NET_PKT_DATA_POOL_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga94ab6300b59d739c4e3c5604d3fbe8a5)。

创建数据分片 `net_buf` 缓冲池（Data Fragment Pool）。

<a id="r_ga2b2d0900ae76674d418918ec955bad48"></a>

```c
#define net_pkt_print_frags(pkt)
```

相关声明：[net_pkt_print_frags](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga2b2d0900ae76674d418918ec955bad48)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.3\_函数（Functions）

<a id="r_ga6f697a97dd09e24663cbddc332ec5f7c"></a>

```c
struct net_buf * net_pkt_get_reserve_data (struct net_buf_pool *pool, size_t min_len, k_timeout_t timeout)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_pkt_get_reserve_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga6f697a97dd09e24663cbddc332ec5f7c)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从给定缓冲池（Pool）获取数据缓冲区（Data Buffer）。

<a id="r_gaf48f4aac4d16a367d46ca76bf038a485"></a>

```c
struct net_buf * net_pkt_get_reserve_rx_data (size_t min_len, k_timeout_t timeout)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_pkt_get_reserve_rx_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gaf48f4aac4d16a367d46ca76bf038a485)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从缓冲池（Pool）获取接收数据缓冲区（RX DATA Buffer）。

<a id="r_gaba26ee929f154978afbd007f7f2b0bc9"></a>

```c
struct net_buf * net_pkt_get_reserve_tx_data (size_t min_len, k_timeout_t timeout)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_pkt_get_reserve_tx_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gaba26ee929f154978afbd007f7f2b0bc9)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从缓冲池（Pool）获取发送数据缓冲区（TX DATA Buffer）。

<a id="r_gafa7d666bddb182149d5f540880c46b4e"></a>

```c
struct net_buf * net_pkt_get_frag (struct net_pkt *pkt, size_t min_len, k_timeout_t timeout)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_pkt_get_frag](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gafa7d666bddb182149d5f540880c46b4e)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

获取数据分片（Data Fragment），可来自用户专用缓冲池（User-specific Buffer Pool）或全局 DATA 池。

<a id="r_ga893d1660fd18ad5842224fda78466099"></a>

```c
void net_pkt_unref (struct net_pkt *pkt)
```

相关声明：[net_pkt_unref](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga893d1660fd18ad5842224fda78466099)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

将数据包放回可用数据包内存块池（Packets Slab）。

<a id="r_ga4e83d4f60b46db8f57798c0e96d6cd7a"></a>

```c
struct net_pkt * net_pkt_ref (struct net_pkt *pkt)
```

相关声明：[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_pkt_ref](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga4e83d4f60b46db8f57798c0e96d6cd7a)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

增加数据包引用计数（Packet Reference Count）。

<a id="r_gaea5e1045d188b3abbd85717ff09d563a"></a>

```c
struct net_buf * net_pkt_frag_ref (struct net_buf *frag)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_pkt_frag_ref](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gaea5e1045d188b3abbd85717ff09d563a)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

增加数据包分片引用计数（Packet Fragment Reference Count）。

<a id="r_ga5c75ef2149d2ba5ff07525988e0fb7cc"></a>

```c
void net_pkt_frag_unref (struct net_buf *frag)
```

相关声明：[net_pkt_frag_unref](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga5c75ef2149d2ba5ff07525988e0fb7cc)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

减少数据包分片引用计数（Packet Fragment Reference Count）。

<a id="r_ga956c784f5417f0f79976c6e106ad0d76"></a>

```c
struct net_buf * net_pkt_frag_del (struct net_pkt *pkt, struct net_buf *parent, struct net_buf *frag)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_pkt_frag_del](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga956c784f5417f0f79976c6e106ad0d76)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从数据包（Packet）中删除已有分片（Fragment）。

<a id="r_ga03a53365cfc2b6c3448763d81f56c2c0"></a>

```c
void net_pkt_frag_add (struct net_pkt *pkt, struct net_buf *frag)
```

相关声明：[net_pkt_frag_add](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga03a53365cfc2b6c3448763d81f56c2c0)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

在数据包分片列表（Fragment List）末尾添加一个分片。

<a id="r_gabcd375d9dbdca21855abe27d7b5a0a7e"></a>

```c
void net_pkt_frag_insert (struct net_pkt *pkt, struct net_buf *frag)
```

相关声明：[net_pkt_frag_insert](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gabcd375d9dbdca21855abe27d7b5a0a7e)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

在数据包分片列表（Fragment List）开头插入一个分片。

<a id="r_gabf85446fb8000574b180d00c5db65a44"></a>

```c
void net_pkt_compact (struct net_pkt *pkt)
```

相关声明：[net_pkt_compact](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gabf85446fb8000574b180d00c5db65a44)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

压紧数据包分片列表（Compact the Fragment List）。

<a id="r_ga7b02b95838b928febfd4970de5e9c9f9"></a>

```c
void net_pkt_get_info (struct k_mem_slab **rx, struct k_mem_slab **tx, struct net_buf_pool **rx_data, struct net_buf_pool **tx_data)
```

相关声明：[net_pkt_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga7b02b95838b928febfd4970de5e9c9f9)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

获取预定义的 RX、TX 和 DATA 缓冲池（Pools）的信息。

<a id="r_ga90d97ba913a875b3ee438e0ea8a970fd"></a>

```c
struct net_pkt * net_pkt_alloc (k_timeout_t timeout)
```

相关声明：[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_pkt_alloc](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga90d97ba913a875b3ee438e0ea8a970fd)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

分配一个已初始化的 `net_pkt`。

<a id="r_gaf1edbaab59576262647089fa1751d9e3"></a>

```c
struct net_pkt * net_pkt_alloc_from_slab (struct k_mem_slab *slab, k_timeout_t timeout)
```

相关声明：[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_pkt_alloc_from_slab](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gaf1edbaab59576262647089fa1751d9e3)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从指定内存块池（Slab）分配一个已初始化的 `net_pkt`。

<a id="r_ga4cec027a0de4807879fd3bd3aed4f12a"></a>

```c
struct net_pkt * net_pkt_rx_alloc (k_timeout_t timeout)
```

相关声明：[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_pkt_rx_alloc](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga4cec027a0de4807879fd3bd3aed4f12a)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

分配一个用于接收（RX）的已初始化 `net_pkt`。

<a id="r_ga770ffe22fc797691b1fc89954d60b2e6"></a>

```c
struct net_pkt * net_pkt_alloc_on_iface (struct net_if *iface, k_timeout_t timeout)
```

相关声明：[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_pkt_alloc_on_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga770ffe22fc797691b1fc89954d60b2e6)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

为指定网络接口（Network Interface）分配网络数据包（Network Packet）。

<a id="r_gae31b4afd510bce346f7d00a9ec5d190d"></a>

```c
int net_pkt_alloc_buffer (struct net_pkt *pkt, size_t size, enum net_ip_protocol proto, k_timeout_t timeout)
```

相关声明：[net_pkt_alloc_buffer](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gae31b4afd510bce346f7d00a9ec5d190d)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_ip_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaf06819bf427cc58be1229b27b373ca31)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

为 `net_pkt` 分配缓冲区（Buffer）。

<a id="r_ga0a292103ba0eacd62a15447e2765a485"></a>

```c
int net_pkt_alloc_buffer_with_reserve (struct net_pkt *pkt, size_t size, size_t reserve, enum net_ip_protocol proto, k_timeout_t timeout)
```

相关声明：[net_pkt_alloc_buffer_with_reserve](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga0a292103ba0eacd62a15447e2765a485)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_ip_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaf06819bf427cc58be1229b27b373ca31)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

为 `net_pkt` 分配缓冲区，并在第一个 `net_buf` 中预留一些空间。

<a id="r_ga53819889ad86bc2c43407f12f113bb94"></a>

```c
int net_pkt_alloc_buffer_raw (struct net_pkt *pkt, size_t size, k_timeout_t timeout)
```

相关声明：[net_pkt_alloc_buffer_raw](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga53819889ad86bc2c43407f12f113bb94)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

为 `net_pkt` 分配指定大小的缓冲区（Buffer），没有额外前置条件（Preconditions）。

<a id="r_ga4ea4f0897e5fe4dfaf7ceca5f18f1702"></a>

```c
struct net_pkt * net_pkt_alloc_with_buffer (struct net_if *iface, size_t size, net_sa_family_t family, enum net_ip_protocol proto, k_timeout_t timeout)
```

相关声明：[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_pkt_alloc_with_buffer](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga4ea4f0897e5fe4dfaf7ceca5f18f1702)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)、[net_ip_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaf06819bf427cc58be1229b27b373ca31)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

一次性分配网络数据包（Network Packet）及其缓冲区（Buffer）。

<a id="r_ga2b11492ae3c16368aa6a0ab8f47b67e7"></a>

```c
void net_pkt_append_buffer (struct net_pkt *pkt, struct net_buf *buffer)
```

相关声明：[net_pkt_append_buffer](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga2b11492ae3c16368aa6a0ab8f47b67e7)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

向数据包追加缓冲区（Append Buffer）。

<a id="r_gaeed119d192e3a14ea3eea6e623334519"></a>

```c
size_t net_pkt_available_buffer (struct net_pkt *pkt)
```

相关声明：[net_pkt_available_buffer](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gaeed119d192e3a14ea3eea6e623334519)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

获取数据包（Pkt）的可用缓冲区空间（Available Buffer Space）。

<a id="r_gaa9f63047b7945a4a155e5d88eac5203b"></a>

```c
size_t net_pkt_available_payload_buffer (struct net_pkt *pkt, enum net_ip_protocol proto)
```

相关声明：[net_pkt_available_payload_buffer](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gaa9f63047b7945a4a155e5d88eac5203b)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_ip_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaf06819bf427cc58be1229b27b373ca31)。

获取数据包（Pkt）可供有效载荷（Payload）使用的缓冲区空间。

<a id="r_ga71d1c49f68afab07324cebd835f08a29"></a>

```c
void net_pkt_trim_buffer (struct net_pkt *pkt)
```

相关声明：[net_pkt_trim_buffer](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga71d1c49f68afab07324cebd835f08a29)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

裁剪 `net_pkt` 缓冲区（Trim Buffer）。

<a id="r_gab657c80669733a4afefaf1be6310107e"></a>

```c
int net_pkt_remove_tail (struct net_pkt *pkt, size_t length)
```

相关声明：[net_pkt_remove_tail](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gab657c80669733a4afefaf1be6310107e)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

从数据包尾部（Tail）移除 `length` 个字节。

<a id="r_ga1b7da39f62dfc8b8948d7689e2dd114a"></a>

```c
void net_pkt_cursor_init (struct net_pkt *pkt)
```

相关声明：[net_pkt_cursor_init](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga1b7da39f62dfc8b8948d7689e2dd114a)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

初始化 `net_pkt` 游标（Cursor）。

<a id="r_gabd352b66cdeaff2fb45361a0fae62876"></a>

```c
static void net_pkt_cursor_backup (struct net_pkt *pkt, struct net_pkt_cursor *backup)
```

相关声明：[net_pkt_cursor_backup](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gabd352b66cdeaff2fb45361a0fae62876)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

备份 `net_pkt` 游标（Cursor）。

<a id="r_gad5ab788f01b4bb3640755e8c4a2c612e"></a>

```c
static void net_pkt_cursor_restore (struct net_pkt *pkt, struct net_pkt_cursor *backup)
```

相关声明：[net_pkt_cursor_restore](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gad5ab788f01b4bb3640755e8c4a2c612e)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

从备份恢复 `net_pkt` 游标（Cursor）。

<a id="r_gabc42ba1bcd0801a116651d965e65b9cd"></a>

```c
static void * net_pkt_cursor_get_pos (struct net_pkt *pkt)
```

相关声明：[net_pkt_cursor_get_pos](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gabc42ba1bcd0801a116651d965e65b9cd)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

返回游标当前位置（Current Cursor Position）。

<a id="r_ga223a79baa1e740a53c4ed0f083d62185"></a>

```c
int net_pkt_skip (struct net_pkt *pkt, size_t length)
```

相关声明：[net_pkt_skip](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga223a79baa1e740a53c4ed0f083d62185)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

跳过 `net_pkt` 中的一部分数据。

<a id="r_gabd241a539bf1290f3d45610fd15b2c1f"></a>

```c
int net_pkt_memset (struct net_pkt *pkt, int byte, size_t length)
```

相关声明：[net_pkt_memset](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gabd241a539bf1290f3d45610fd15b2c1f)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

对 `net_pkt` 中的一部分数据执行内存填充（Memset）。

<a id="r_ga4648828ca353c8c0ecf00ae2648e963a"></a>

```c
int net_pkt_copy (struct net_pkt *pkt_dst, struct net_pkt *pkt_src, size_t length)
```

相关声明：[net_pkt_copy](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga4648828ca353c8c0ecf00ae2648e963a)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

将一个数据包（Packet）的数据复制到另一个数据包中。

<a id="r_gaefefe50d0c68fb4997abc7b309740959"></a>

```c
struct net_pkt * net_pkt_clone (struct net_pkt *pkt, k_timeout_t timeout)
```

相关声明：[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_pkt_clone](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gaefefe50d0c68fb4997abc7b309740959)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

克隆数据包（Pkt）及其缓冲区（Buffer）。

<a id="r_ga66aec729118e4d927c921b872df82dda"></a>

```c
struct net_pkt * net_pkt_rx_clone (struct net_pkt *pkt, k_timeout_t timeout)
```

相关声明：[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_pkt_rx_clone](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga66aec729118e4d927c921b872df82dda)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

克隆数据包（Pkt）及其缓冲区（Buffer）。

<a id="r_ga26ae9d1286cb98d255f1bfb65201f1e2"></a>

```c
struct net_pkt * net_pkt_shallow_clone (struct net_pkt *pkt, k_timeout_t timeout)
```

相关声明：[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_pkt_shallow_clone](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga26ae9d1286cb98d255f1bfb65201f1e2)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

克隆数据包（Pkt），并增加其缓冲区引用计数（Buffer Refcount）。

<a id="r_ga914be010ddd225a4fc2d6ab521ee7b64"></a>

```c
int net_pkt_read (struct net_pkt *pkt, void *data, size_t length)
```

相关声明：[net_pkt_read](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga914be010ddd225a4fc2d6ab521ee7b64)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

从 `net_pkt` 读取一部分数据。

<a id="r_gaf9b2753cb514804a77d9494c9f070089"></a>

```c
static int net_pkt_read_u8 (struct net_pkt *pkt, uint8_t *data)
```

相关声明：[net_pkt_read_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gaf9b2753cb514804a77d9494c9f070089)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从 `net_pkt` 读取一个字节（`uint8_t`）。

<a id="r_ga500a318977cfecd4ec7c60cea01db2fc"></a>

```c
int net_pkt_read_be16 (struct net_pkt *pkt, uint16_t *data)
```

相关声明：[net_pkt_read_be16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga500a318977cfecd4ec7c60cea01db2fc)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

从 `net_pkt` 读取大端序（Big Endian）的 `uint16_t` 数据。

<a id="r_gab1735ef4f6a2e538a2692358295dd8d1"></a>

```c
int net_pkt_read_le16 (struct net_pkt *pkt, uint16_t *data)
```

相关声明：[net_pkt_read_le16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gab1735ef4f6a2e538a2692358295dd8d1)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

从 `net_pkt` 读取小端序（Little Endian）的 `uint16_t` 数据。

<a id="r_gab38c99947d02982073df65c0d5893d2c"></a>

```c
int net_pkt_read_be32 (struct net_pkt *pkt, uint32_t *data)
```

相关声明：[net_pkt_read_be32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gab38c99947d02982073df65c0d5893d2c)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 `net_pkt` 读取大端序（Big Endian）的 `uint32_t` 数据。

<a id="r_ga214e817ca3b5daa4126c0deecd4981d7"></a>

```c
int net_pkt_read_le32 (struct net_pkt *pkt, uint32_t *data)
```

相关声明：[net_pkt_read_le32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga214e817ca3b5daa4126c0deecd4981d7)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 `net_pkt` 读取小端序（Little Endian）的 `uint32_t` 数据。

<a id="r_gaf3a1eb735316e155e3e30c1ef4395d4d"></a>

```c
int net_pkt_read_be64 (struct net_pkt *pkt, uint64_t *data)
```

相关声明：[net_pkt_read_be64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gaf3a1eb735316e155e3e30c1ef4395d4d)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

从 `net_pkt` 读取大端序（Big Endian）的 `uint64_t` 数据。

<a id="r_ga9a6e19dff44a64582edda084aa7ec96e"></a>

```c
int net_pkt_read_le64 (struct net_pkt *pkt, uint64_t *data)
```

相关声明：[net_pkt_read_le64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga9a6e19dff44a64582edda084aa7ec96e)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

从 `net_pkt` 读取小端序（Little Endian）的 `uint64_t` 数据。

<a id="r_gae99eadd977b7f66ecc91d2ccba34c6fa"></a>

```c
int net_pkt_write (struct net_pkt *pkt, const void *data, size_t length)
```

相关声明：[net_pkt_write](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gae99eadd977b7f66ecc91d2ccba34c6fa)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

向 `net_pkt` 写入数据。

<a id="r_gaa5129f661075c13d9b59627ae9110bd1"></a>

```c
static int net_pkt_write_u8 (struct net_pkt *pkt, uint8_t data)
```

相关声明：[net_pkt_write_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gaa5129f661075c13d9b59627ae9110bd1)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 `net_pkt` 写入一个字节（`uint8_t`）的数据。

<a id="r_ga8e5083388ccb0333fdcf745bc60ad260"></a>

```c
static int net_pkt_write_be16 (struct net_pkt *pkt, uint16_t data)
```

相关声明：[net_pkt_write_be16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga8e5083388ccb0333fdcf745bc60ad260)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向 `net_pkt` 写入大端序（Big Endian）的 `uint16_t` 数据。

<a id="r_ga053aff4ff0a501f336132c35b7fb2022"></a>

```c
static int net_pkt_write_be32 (struct net_pkt *pkt, uint32_t data)
```

相关声明：[net_pkt_write_be32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga053aff4ff0a501f336132c35b7fb2022)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向 `net_pkt` 写入大端序（Big Endian）的 `uint32_t` 数据。

<a id="r_gaf2388032e4e0b76fe32e4618ef3ea548"></a>

```c
static int net_pkt_write_le32 (struct net_pkt *pkt, uint32_t data)
```

相关声明：[net_pkt_write_le32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gaf2388032e4e0b76fe32e4618ef3ea548)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向 `net_pkt` 写入小端序（Little Endian）的 `uint32_t` 数据。

<a id="r_gac8a6ea1b0dc1bcd7b6a3f15869027dd1"></a>

```c
static int net_pkt_write_le16 (struct net_pkt *pkt, uint16_t data)
```

相关声明：[net_pkt_write_le16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gac8a6ea1b0dc1bcd7b6a3f15869027dd1)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向 `net_pkt` 写入小端序（Little Endian）的 `uint16_t` 数据。

<a id="r_gadee5307216b6b3b725a2fd7584a224c9"></a>

```c
size_t net_pkt_remaining_data (struct net_pkt *pkt)
```

相关声明：[net_pkt_remaining_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gadee5307216b6b3b725a2fd7584a224c9)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

获取从当前游标位置（Current Cursor Position）起可读取的数据量。

<a id="r_ga9401d109ba978087139436c8a79c9bb0"></a>

```c
static size_t net_pkt_get_len (struct net_pkt *pkt)
```

相关声明：[net_pkt_get_len](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga9401d109ba978087139436c8a79c9bb0)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

获取数据包存储的总字节数（Total Number of Bytes）。

<a id="r_ga2e7a0f9348a623c5160124da188445ee"></a>

```c
int net_pkt_update_length (struct net_pkt *pkt, size_t length)
```

相关声明：[net_pkt_update_length](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga2e7a0f9348a623c5160124da188445ee)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

更新数据包总长度（Overall Packet Length）。

<a id="r_ga434c347a32600ee113c0e1cc13f70cd4"></a>

```c
int net_pkt_pull (struct net_pkt *pkt, size_t length)
```

相关声明：[net_pkt_pull](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga434c347a32600ee113c0e1cc13f70cd4)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

从数据包当前游标位置（Current Cursor Position）移除数据。

<a id="r_gadb3b705a0431b3bb98fb2e8193c3b510"></a>

```c
uint16_t net_pkt_get_current_offset (struct net_pkt *pkt)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_pkt_get_current_offset](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gadb3b705a0431b3bb98fb2e8193c3b510)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

根据游标获取它在数据包中的实际偏移量（Actual Offset）。

<a id="r_gaf4ee5a8903b495e000a3a4c8a8493160"></a>

```c
bool net_pkt_is_contiguous (struct net_pkt *pkt, size_t size)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_pkt_is_contiguous](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gaf4ee5a8903b495e000a3a4c8a8493160)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

检查指定大小的数据是否能够连续存放（Fit Contiguously）。

<a id="r_gafbd6c0ab33139b134f67a8f8c0096445"></a>

```c
size_t net_pkt_get_contiguous_len (struct net_pkt *pkt)
```

相关声明：[net_pkt_get_contiguous_len](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gafbd6c0ab33139b134f67a8f8c0096445)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

获取连续缓冲区空间（Contiguous Buffer Space）。

<a id="r_gaa00da4276fd4a01faf80a92796f78e70"></a>

```c
void * net_pkt_get_data (struct net_pkt *pkt, struct net_pkt_data_access *access)
```

相关声明：[net_pkt_get_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gaa00da4276fd4a01faf80a92796f78e70)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

以连续方式（Contiguous Way）从网络数据包中获取数据。

<a id="r_ga98df84477b35e203b11029fc4ddec1cc"></a>

```c
int net_pkt_set_data (struct net_pkt *pkt, struct net_pkt_data_access *access)
```

相关声明：[net_pkt_set_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga98df84477b35e203b11029fc4ddec1cc)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

向网络数据包设置连续数据（Contiguous Data）。

<a id="r_gac7226cbfa2da28408f9691d375bc8f9f"></a>

```c
static int net_pkt_acknowledge_data (struct net_pkt *pkt, struct net_pkt_data_access *access)
```

相关声明：[net_pkt_acknowledge_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gac7226cbfa2da28408f9691d375bc8f9f)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

确认先前从网络数据包取得的连续数据（Contiguous Data）。数据包需要设为覆盖模式（Overwrite Mode）。


## 9.4\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/net_buf.h](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [zephyr/net/net_core.h](../api_source_system_reference/P023_net_core.h_源码浏览.md)
- [zephyr/net/net_linkaddr.h](../api_source_reference/P576_net_linkaddr.h_源码浏览.md)
- [zephyr/net/net_ip.h](../api_source_packet_gnss_reference/P005_net_ip.h_源码浏览.md)
- [zephyr/net/net_if.h](../api_source_network_reference/P013_net_if.h_源码浏览.md)
- [zephyr/net/net_context.h](../api_source_system_reference/P022_net_context.h_源码浏览.md)
- [zephyr/net/net_time.h](../api_source_supplement_reference/P125_net_time.h_源码浏览.md)
- [zephyr/net/ethernet_vlan.h](../api_source_reference/P247_ethernet_vlan.h_源码浏览.md)
- [zephyr/net/ptp_time.h](../api_source_reference/P681_ptp_time.h_源码浏览.md)
- [zephyr/logging/log_core.h](../log_internal_reference/P002_日志核心头文件源码.md)
- [查看此文件的源码。](../api_source_packet_gnss_reference/P006_net_pkt.h_源码浏览.md)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [NET_PKT_FRAG_FOR_EACH](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gad63d4802ad4e10b89829aed35a9ae804)
- [NET_PKT_SLAB_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gafc7e98d5b64d816faabcbaa2ec22a2bb)
- [NET_PKT_DATA_POOL_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga94ab6300b59d739c4e3c5604d3fbe8a5)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [net_pkt_print_frags](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga2b2d0900ae76674d418918ec955bad48)
- [net_pkt_get_reserve_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga6f697a97dd09e24663cbddc332ec5f7c)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [net_pkt_get_reserve_rx_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gaf48f4aac4d16a367d46ca76bf038a485)
- [net_pkt_get_reserve_tx_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gaba26ee929f154978afbd007f7f2b0bc9)
- [net_pkt_get_frag](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gafa7d666bddb182149d5f540880c46b4e)
- [net_pkt_unref](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga893d1660fd18ad5842224fda78466099)
- [net_pkt_ref](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga4e83d4f60b46db8f57798c0e96d6cd7a)
- [net_pkt_frag_ref](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gaea5e1045d188b3abbd85717ff09d563a)
- [net_pkt_frag_unref](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga5c75ef2149d2ba5ff07525988e0fb7cc)
- [net_pkt_frag_del](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga956c784f5417f0f79976c6e106ad0d76)
- [net_pkt_frag_add](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga03a53365cfc2b6c3448763d81f56c2c0)
- [net_pkt_frag_insert](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gabcd375d9dbdca21855abe27d7b5a0a7e)
- [net_pkt_compact](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gabf85446fb8000574b180d00c5db65a44)
- [net_pkt_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga7b02b95838b928febfd4970de5e9c9f9)
- [net_pkt_alloc](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga90d97ba913a875b3ee438e0ea8a970fd)
- [net_pkt_alloc_from_slab](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gaf1edbaab59576262647089fa1751d9e3)
- [net_pkt_rx_alloc](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga4cec027a0de4807879fd3bd3aed4f12a)
- [net_pkt_alloc_on_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga770ffe22fc797691b1fc89954d60b2e6)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_pkt_alloc_buffer](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gae31b4afd510bce346f7d00a9ec5d190d)
- [net_ip_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaf06819bf427cc58be1229b27b373ca31)
- [net_pkt_alloc_buffer_with_reserve](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga0a292103ba0eacd62a15447e2765a485)
- [net_pkt_alloc_buffer_raw](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga53819889ad86bc2c43407f12f113bb94)
- [net_pkt_alloc_with_buffer](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga4ea4f0897e5fe4dfaf7ceca5f18f1702)
- [net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)
- [net_pkt_append_buffer](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga2b11492ae3c16368aa6a0ab8f47b67e7)
- [net_pkt_available_buffer](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gaeed119d192e3a14ea3eea6e623334519)
- [net_pkt_available_payload_buffer](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gaa9f63047b7945a4a155e5d88eac5203b)
- [net_pkt_trim_buffer](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga71d1c49f68afab07324cebd835f08a29)
- [net_pkt_remove_tail](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gab657c80669733a4afefaf1be6310107e)
- [net_pkt_cursor_init](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga1b7da39f62dfc8b8948d7689e2dd114a)
- [net_pkt_cursor_backup](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gabd352b66cdeaff2fb45361a0fae62876)
- [net_pkt_cursor_restore](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gad5ab788f01b4bb3640755e8c4a2c612e)
- [net_pkt_cursor_get_pos](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gabc42ba1bcd0801a116651d965e65b9cd)
- [net_pkt_skip](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga223a79baa1e740a53c4ed0f083d62185)
- [net_pkt_memset](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gabd241a539bf1290f3d45610fd15b2c1f)
- [net_pkt_copy](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga4648828ca353c8c0ecf00ae2648e963a)
- [net_pkt_clone](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gaefefe50d0c68fb4997abc7b309740959)
- [net_pkt_rx_clone](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga66aec729118e4d927c921b872df82dda)
- [net_pkt_shallow_clone](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga26ae9d1286cb98d255f1bfb65201f1e2)
- [net_pkt_read](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga914be010ddd225a4fc2d6ab521ee7b64)
- [net_pkt_read_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gaf9b2753cb514804a77d9494c9f070089)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_pkt_read_be16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga500a318977cfecd4ec7c60cea01db2fc)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_pkt_read_le16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gab1735ef4f6a2e538a2692358295dd8d1)
- [net_pkt_read_be32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gab38c99947d02982073df65c0d5893d2c)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [net_pkt_read_le32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga214e817ca3b5daa4126c0deecd4981d7)
- [net_pkt_read_be64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gaf3a1eb735316e155e3e30c1ef4395d4d)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [net_pkt_read_le64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga9a6e19dff44a64582edda084aa7ec96e)
- [net_pkt_write](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gae99eadd977b7f66ecc91d2ccba34c6fa)
- [net_pkt_write_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gaa5129f661075c13d9b59627ae9110bd1)
- [net_pkt_write_be16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga8e5083388ccb0333fdcf745bc60ad260)
- [net_pkt_write_be32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga053aff4ff0a501f336132c35b7fb2022)
- [net_pkt_write_le32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gaf2388032e4e0b76fe32e4618ef3ea548)
- [net_pkt_write_le16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gac8a6ea1b0dc1bcd7b6a3f15869027dd1)
- [net_pkt_remaining_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gadee5307216b6b3b725a2fd7584a224c9)
- [net_pkt_get_len](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga9401d109ba978087139436c8a79c9bb0)
- [net_pkt_update_length](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga2e7a0f9348a623c5160124da188445ee)
- [net_pkt_pull](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga434c347a32600ee113c0e1cc13f70cd4)
- [net_pkt_get_current_offset](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gadb3b705a0431b3bb98fb2e8193c3b510)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [net_pkt_is_contiguous](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gaf4ee5a8903b495e000a3a4c8a8493160)
- [net_pkt_get_contiguous_len](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gafbd6c0ab33139b134f67a8f8c0096445)
- [net_pkt_get_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gaa00da4276fd4a01faf80a92796f78e70)
- [net_pkt_set_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#ga98df84477b35e203b11029fc4ddec1cc)
- [net_pkt_acknowledge_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gac7226cbfa2da28408f9691d375bc8f9f)

<a id="header-details"></a>

---

[上一章](P008_zephyr__net__net_context.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_zephyr__drivers__pcie__endpoint__pcie_ep.h_文件参考.md)
