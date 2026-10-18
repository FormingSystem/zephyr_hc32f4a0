---
id: learning.zephyr-docs.api-socket-lora-topic-reference.page-11
title: 网络分组库（Network Packet Library）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_网络分组库（Network Packet Library）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络分组管理库。

<a id="details"></a>

网络数据包管理库（Network Packet Management Library）。起始版本（Since）：1.5。版本（Version）：0.8.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 11.1\_数据结构（Data Structures）

<a id="r_net_5Fpkt"></a>

```c
struct net_pkt
```

相关声明：[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

网络数据包（Network Packet）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.2\_宏定义（Macros）

<a id="r_gad63d4802ad4e10b89829aed35a9ae804"></a>

```c
#define NET_PKT_FRAG_FOR_EACH(_pkt, _var)
```

相关声明：[NET_PKT_FRAG_FOR_EACH](#gad63d4802ad4e10b89829aed35a9ae804)。

遍历网络数据包（Network Packet）的全部分片（Fragments）。

<a id="r_gafc7e98d5b64d816faabcbaa2ec22a2bb"></a>

```c
#define NET_PKT_SLAB_DEFINE(name, count)
```

相关声明：[NET_PKT_SLAB_DEFINE](#gafc7e98d5b64d816faabcbaa2ec22a2bb)。

创建 `net_pkt` 内存块池（Slab）。

<a id="r_ga94ab6300b59d739c4e3c5604d3fbe8a5"></a>

```c
#define NET_PKT_DATA_POOL_DEFINE(name, count)
```

相关声明：[NET_PKT_DATA_POOL_DEFINE](#ga94ab6300b59d739c4e3c5604d3fbe8a5)。

创建数据分片 `net_buf` 缓冲池（Data Fragment Pool）。

<a id="r_ga2b2d0900ae76674d418918ec955bad48"></a>

```c
#define net_pkt_print_frags(pkt)
```

相关声明：[net_pkt_print_frags](#ga2b2d0900ae76674d418918ec955bad48)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.3\_函数（Functions）

<a id="r_ga6f697a97dd09e24663cbddc332ec5f7c"></a>

```c
struct net_buf * net_pkt_get_reserve_data (struct net_buf_pool *pool, size_t min_len, k_timeout_t timeout)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_pkt_get_reserve_data](#ga6f697a97dd09e24663cbddc332ec5f7c)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从给定缓冲池（Pool）获取数据缓冲区（Data Buffer）。

<a id="r_gaf48f4aac4d16a367d46ca76bf038a485"></a>

```c
struct net_buf * net_pkt_get_reserve_rx_data (size_t min_len, k_timeout_t timeout)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_pkt_get_reserve_rx_data](#gaf48f4aac4d16a367d46ca76bf038a485)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从缓冲池（Pool）获取接收数据缓冲区（RX DATA Buffer）。

<a id="r_gaba26ee929f154978afbd007f7f2b0bc9"></a>

```c
struct net_buf * net_pkt_get_reserve_tx_data (size_t min_len, k_timeout_t timeout)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_pkt_get_reserve_tx_data](#gaba26ee929f154978afbd007f7f2b0bc9)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从缓冲池（Pool）获取发送数据缓冲区（TX DATA Buffer）。

<a id="r_gafa7d666bddb182149d5f540880c46b4e"></a>

```c
struct net_buf * net_pkt_get_frag (struct net_pkt *pkt, size_t min_len, k_timeout_t timeout)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_pkt_get_frag](#gafa7d666bddb182149d5f540880c46b4e)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

获取数据分片（Data Fragment），可来自用户专用缓冲池（User-specific Buffer Pool）或全局 DATA 池。

<a id="r_ga893d1660fd18ad5842224fda78466099"></a>

```c
void net_pkt_unref (struct net_pkt *pkt)
```

相关声明：[net_pkt_unref](#ga893d1660fd18ad5842224fda78466099)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

将数据包放回可用数据包内存块池（Packets Slab）。

<a id="r_ga4e83d4f60b46db8f57798c0e96d6cd7a"></a>

```c
struct net_pkt * net_pkt_ref (struct net_pkt *pkt)
```

相关声明：[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_pkt_ref](#ga4e83d4f60b46db8f57798c0e96d6cd7a)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

增加数据包引用计数（Packet Reference Count）。

<a id="r_gaea5e1045d188b3abbd85717ff09d563a"></a>

```c
struct net_buf * net_pkt_frag_ref (struct net_buf *frag)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_pkt_frag_ref](#gaea5e1045d188b3abbd85717ff09d563a)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

增加数据包分片引用计数（Packet Fragment Reference Count）。

<a id="r_ga5c75ef2149d2ba5ff07525988e0fb7cc"></a>

```c
void net_pkt_frag_unref (struct net_buf *frag)
```

相关声明：[net_pkt_frag_unref](#ga5c75ef2149d2ba5ff07525988e0fb7cc)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

减少数据包分片引用计数（Packet Fragment Reference Count）。

<a id="r_ga956c784f5417f0f79976c6e106ad0d76"></a>

```c
struct net_buf * net_pkt_frag_del (struct net_pkt *pkt, struct net_buf *parent, struct net_buf *frag)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_pkt_frag_del](#ga956c784f5417f0f79976c6e106ad0d76)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从数据包（Packet）中删除已有分片（Fragment）。

<a id="r_ga03a53365cfc2b6c3448763d81f56c2c0"></a>

```c
void net_pkt_frag_add (struct net_pkt *pkt, struct net_buf *frag)
```

相关声明：[net_pkt_frag_add](#ga03a53365cfc2b6c3448763d81f56c2c0)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

在数据包分片列表（Fragment List）末尾添加一个分片。

<a id="r_gabcd375d9dbdca21855abe27d7b5a0a7e"></a>

```c
void net_pkt_frag_insert (struct net_pkt *pkt, struct net_buf *frag)
```

相关声明：[net_pkt_frag_insert](#gabcd375d9dbdca21855abe27d7b5a0a7e)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

在数据包分片列表（Fragment List）开头插入一个分片。

<a id="r_gabf85446fb8000574b180d00c5db65a44"></a>

```c
void net_pkt_compact (struct net_pkt *pkt)
```

相关声明：[net_pkt_compact](#gabf85446fb8000574b180d00c5db65a44)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

压紧数据包分片列表（Compact the Fragment List）。

<a id="r_ga7b02b95838b928febfd4970de5e9c9f9"></a>

```c
void net_pkt_get_info (struct k_mem_slab **rx, struct k_mem_slab **tx, struct net_buf_pool **rx_data, struct net_buf_pool **tx_data)
```

相关声明：[net_pkt_get_info](#ga7b02b95838b928febfd4970de5e9c9f9)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

获取预定义的 RX、TX 和 DATA 缓冲池（Pools）的信息。

<a id="r_ga90d97ba913a875b3ee438e0ea8a970fd"></a>

```c
struct net_pkt * net_pkt_alloc (k_timeout_t timeout)
```

相关声明：[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_pkt_alloc](#ga90d97ba913a875b3ee438e0ea8a970fd)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

分配一个已初始化的 `net_pkt`。

<a id="r_gaf1edbaab59576262647089fa1751d9e3"></a>

```c
struct net_pkt * net_pkt_alloc_from_slab (struct k_mem_slab *slab, k_timeout_t timeout)
```

相关声明：[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_pkt_alloc_from_slab](#gaf1edbaab59576262647089fa1751d9e3)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从指定内存块池（Slab）分配一个已初始化的 `net_pkt`。

<a id="r_ga4cec027a0de4807879fd3bd3aed4f12a"></a>

```c
struct net_pkt * net_pkt_rx_alloc (k_timeout_t timeout)
```

相关声明：[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_pkt_rx_alloc](#ga4cec027a0de4807879fd3bd3aed4f12a)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

分配一个用于接收（RX）的已初始化 `net_pkt`。

<a id="r_ga770ffe22fc797691b1fc89954d60b2e6"></a>

```c
struct net_pkt * net_pkt_alloc_on_iface (struct net_if *iface, k_timeout_t timeout)
```

相关声明：[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_pkt_alloc_on_iface](#ga770ffe22fc797691b1fc89954d60b2e6)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

为指定网络接口（Network Interface）分配网络数据包（Network Packet）。

<a id="r_gae31b4afd510bce346f7d00a9ec5d190d"></a>

```c
int net_pkt_alloc_buffer (struct net_pkt *pkt, size_t size, enum net_ip_protocol proto, k_timeout_t timeout)
```

相关声明：[net_pkt_alloc_buffer](#gae31b4afd510bce346f7d00a9ec5d190d)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_ip_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaf06819bf427cc58be1229b27b373ca31)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

为 `net_pkt` 分配缓冲区（Buffer）。

<a id="r_ga0a292103ba0eacd62a15447e2765a485"></a>

```c
int net_pkt_alloc_buffer_with_reserve (struct net_pkt *pkt, size_t size, size_t reserve, enum net_ip_protocol proto, k_timeout_t timeout)
```

相关声明：[net_pkt_alloc_buffer_with_reserve](#ga0a292103ba0eacd62a15447e2765a485)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_ip_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaf06819bf427cc58be1229b27b373ca31)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

为 `net_pkt` 分配缓冲区，并在第一个 `net_buf` 中预留一些空间。

<a id="r_ga53819889ad86bc2c43407f12f113bb94"></a>

```c
int net_pkt_alloc_buffer_raw (struct net_pkt *pkt, size_t size, k_timeout_t timeout)
```

相关声明：[net_pkt_alloc_buffer_raw](#ga53819889ad86bc2c43407f12f113bb94)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

为 `net_pkt` 分配指定大小的缓冲区（Buffer），没有额外前置条件（Preconditions）。

<a id="r_ga4ea4f0897e5fe4dfaf7ceca5f18f1702"></a>

```c
struct net_pkt * net_pkt_alloc_with_buffer (struct net_if *iface, size_t size, net_sa_family_t family, enum net_ip_protocol proto, k_timeout_t timeout)
```

相关声明：[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_pkt_alloc_with_buffer](#ga4ea4f0897e5fe4dfaf7ceca5f18f1702)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)、[net_ip_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaf06819bf427cc58be1229b27b373ca31)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

一次性分配网络数据包（Network Packet）及其缓冲区（Buffer）。

<a id="r_ga2b11492ae3c16368aa6a0ab8f47b67e7"></a>

```c
void net_pkt_append_buffer (struct net_pkt *pkt, struct net_buf *buffer)
```

相关声明：[net_pkt_append_buffer](#ga2b11492ae3c16368aa6a0ab8f47b67e7)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

向数据包追加缓冲区（Append Buffer）。

<a id="r_gaeed119d192e3a14ea3eea6e623334519"></a>

```c
size_t net_pkt_available_buffer (struct net_pkt *pkt)
```

相关声明：[net_pkt_available_buffer](#gaeed119d192e3a14ea3eea6e623334519)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

获取数据包（Pkt）的可用缓冲区空间（Available Buffer Space）。

<a id="r_gaa9f63047b7945a4a155e5d88eac5203b"></a>

```c
size_t net_pkt_available_payload_buffer (struct net_pkt *pkt, enum net_ip_protocol proto)
```

相关声明：[net_pkt_available_payload_buffer](#gaa9f63047b7945a4a155e5d88eac5203b)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_ip_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaf06819bf427cc58be1229b27b373ca31)。

获取数据包（Pkt）可供有效载荷（Payload）使用的缓冲区空间。

<a id="r_ga71d1c49f68afab07324cebd835f08a29"></a>

```c
void net_pkt_trim_buffer (struct net_pkt *pkt)
```

相关声明：[net_pkt_trim_buffer](#ga71d1c49f68afab07324cebd835f08a29)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

裁剪 `net_pkt` 缓冲区（Trim Buffer）。

<a id="r_gab657c80669733a4afefaf1be6310107e"></a>

```c
int net_pkt_remove_tail (struct net_pkt *pkt, size_t length)
```

相关声明：[net_pkt_remove_tail](#gab657c80669733a4afefaf1be6310107e)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

从数据包尾部（Tail）移除 `length` 个字节。

<a id="r_ga1b7da39f62dfc8b8948d7689e2dd114a"></a>

```c
void net_pkt_cursor_init (struct net_pkt *pkt)
```

相关声明：[net_pkt_cursor_init](#ga1b7da39f62dfc8b8948d7689e2dd114a)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

初始化 `net_pkt` 游标（Cursor）。

<a id="r_gabd352b66cdeaff2fb45361a0fae62876"></a>

```c
static void net_pkt_cursor_backup (struct net_pkt *pkt, struct net_pkt_cursor *backup)
```

相关声明：[net_pkt_cursor_backup](#gabd352b66cdeaff2fb45361a0fae62876)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

备份 `net_pkt` 游标（Cursor）。

<a id="r_gad5ab788f01b4bb3640755e8c4a2c612e"></a>

```c
static void net_pkt_cursor_restore (struct net_pkt *pkt, struct net_pkt_cursor *backup)
```

相关声明：[net_pkt_cursor_restore](#gad5ab788f01b4bb3640755e8c4a2c612e)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

从备份恢复 `net_pkt` 游标（Cursor）。

<a id="r_gabc42ba1bcd0801a116651d965e65b9cd"></a>

```c
static void * net_pkt_cursor_get_pos (struct net_pkt *pkt)
```

相关声明：[net_pkt_cursor_get_pos](#gabc42ba1bcd0801a116651d965e65b9cd)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

返回游标当前位置（Current Cursor Position）。

<a id="r_ga223a79baa1e740a53c4ed0f083d62185"></a>

```c
int net_pkt_skip (struct net_pkt *pkt, size_t length)
```

相关声明：[net_pkt_skip](#ga223a79baa1e740a53c4ed0f083d62185)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

跳过 `net_pkt` 中的一部分数据。

<a id="r_gabd241a539bf1290f3d45610fd15b2c1f"></a>

```c
int net_pkt_memset (struct net_pkt *pkt, int byte, size_t length)
```

相关声明：[net_pkt_memset](#gabd241a539bf1290f3d45610fd15b2c1f)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

对 `net_pkt` 中的一部分数据执行内存填充（Memset）。

<a id="r_ga4648828ca353c8c0ecf00ae2648e963a"></a>

```c
int net_pkt_copy (struct net_pkt *pkt_dst, struct net_pkt *pkt_src, size_t length)
```

相关声明：[net_pkt_copy](#ga4648828ca353c8c0ecf00ae2648e963a)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

将一个数据包（Packet）的数据复制到另一个数据包中。

<a id="r_gaefefe50d0c68fb4997abc7b309740959"></a>

```c
struct net_pkt * net_pkt_clone (struct net_pkt *pkt, k_timeout_t timeout)
```

相关声明：[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_pkt_clone](#gaefefe50d0c68fb4997abc7b309740959)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

克隆数据包（Pkt）及其缓冲区（Buffer）。

<a id="r_ga66aec729118e4d927c921b872df82dda"></a>

```c
struct net_pkt * net_pkt_rx_clone (struct net_pkt *pkt, k_timeout_t timeout)
```

相关声明：[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_pkt_rx_clone](#ga66aec729118e4d927c921b872df82dda)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

克隆数据包（Pkt）及其缓冲区（Buffer）。

<a id="r_ga26ae9d1286cb98d255f1bfb65201f1e2"></a>

```c
struct net_pkt * net_pkt_shallow_clone (struct net_pkt *pkt, k_timeout_t timeout)
```

相关声明：[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_pkt_shallow_clone](#ga26ae9d1286cb98d255f1bfb65201f1e2)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

克隆数据包（Pkt），并增加其缓冲区引用计数（Buffer Refcount）。

<a id="r_ga914be010ddd225a4fc2d6ab521ee7b64"></a>

```c
int net_pkt_read (struct net_pkt *pkt, void *data, size_t length)
```

相关声明：[net_pkt_read](#ga914be010ddd225a4fc2d6ab521ee7b64)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

从 `net_pkt` 读取一部分数据。

<a id="r_gaf9b2753cb514804a77d9494c9f070089"></a>

```c
static int net_pkt_read_u8 (struct net_pkt *pkt, uint8_t *data)
```

相关声明：[net_pkt_read_u8](#gaf9b2753cb514804a77d9494c9f070089)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从 `net_pkt` 读取一个字节（`uint8_t`）。

<a id="r_ga500a318977cfecd4ec7c60cea01db2fc"></a>

```c
int net_pkt_read_be16 (struct net_pkt *pkt, uint16_t *data)
```

相关声明：[net_pkt_read_be16](#ga500a318977cfecd4ec7c60cea01db2fc)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

从 `net_pkt` 读取大端序（Big Endian）的 `uint16_t` 数据。

<a id="r_gab1735ef4f6a2e538a2692358295dd8d1"></a>

```c
int net_pkt_read_le16 (struct net_pkt *pkt, uint16_t *data)
```

相关声明：[net_pkt_read_le16](#gab1735ef4f6a2e538a2692358295dd8d1)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

从 `net_pkt` 读取小端序（Little Endian）的 `uint16_t` 数据。

<a id="r_gab38c99947d02982073df65c0d5893d2c"></a>

```c
int net_pkt_read_be32 (struct net_pkt *pkt, uint32_t *data)
```

相关声明：[net_pkt_read_be32](#gab38c99947d02982073df65c0d5893d2c)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 `net_pkt` 读取大端序（Big Endian）的 `uint32_t` 数据。

<a id="r_ga214e817ca3b5daa4126c0deecd4981d7"></a>

```c
int net_pkt_read_le32 (struct net_pkt *pkt, uint32_t *data)
```

相关声明：[net_pkt_read_le32](#ga214e817ca3b5daa4126c0deecd4981d7)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 `net_pkt` 读取小端序（Little Endian）的 `uint32_t` 数据。

<a id="r_gaf3a1eb735316e155e3e30c1ef4395d4d"></a>

```c
int net_pkt_read_be64 (struct net_pkt *pkt, uint64_t *data)
```

相关声明：[net_pkt_read_be64](#gaf3a1eb735316e155e3e30c1ef4395d4d)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

从 `net_pkt` 读取大端序（Big Endian）的 `uint64_t` 数据。

<a id="r_ga9a6e19dff44a64582edda084aa7ec96e"></a>

```c
int net_pkt_read_le64 (struct net_pkt *pkt, uint64_t *data)
```

相关声明：[net_pkt_read_le64](#ga9a6e19dff44a64582edda084aa7ec96e)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

从 `net_pkt` 读取小端序（Little Endian）的 `uint64_t` 数据。

<a id="r_gae99eadd977b7f66ecc91d2ccba34c6fa"></a>

```c
int net_pkt_write (struct net_pkt *pkt, const void *data, size_t length)
```

相关声明：[net_pkt_write](#gae99eadd977b7f66ecc91d2ccba34c6fa)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

向 `net_pkt` 写入数据。

<a id="r_gaa5129f661075c13d9b59627ae9110bd1"></a>

```c
static int net_pkt_write_u8 (struct net_pkt *pkt, uint8_t data)
```

相关声明：[net_pkt_write_u8](#gaa5129f661075c13d9b59627ae9110bd1)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 `net_pkt` 写入一个字节（`uint8_t`）的数据。

<a id="r_ga8e5083388ccb0333fdcf745bc60ad260"></a>

```c
static int net_pkt_write_be16 (struct net_pkt *pkt, uint16_t data)
```

相关声明：[net_pkt_write_be16](#ga8e5083388ccb0333fdcf745bc60ad260)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向 `net_pkt` 写入大端序（Big Endian）的 `uint16_t` 数据。

<a id="r_ga053aff4ff0a501f336132c35b7fb2022"></a>

```c
static int net_pkt_write_be32 (struct net_pkt *pkt, uint32_t data)
```

相关声明：[net_pkt_write_be32](#ga053aff4ff0a501f336132c35b7fb2022)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向 `net_pkt` 写入大端序（Big Endian）的 `uint32_t` 数据。

<a id="r_gaf2388032e4e0b76fe32e4618ef3ea548"></a>

```c
static int net_pkt_write_le32 (struct net_pkt *pkt, uint32_t data)
```

相关声明：[net_pkt_write_le32](#gaf2388032e4e0b76fe32e4618ef3ea548)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向 `net_pkt` 写入小端序（Little Endian）的 `uint32_t` 数据。

<a id="r_gac8a6ea1b0dc1bcd7b6a3f15869027dd1"></a>

```c
static int net_pkt_write_le16 (struct net_pkt *pkt, uint16_t data)
```

相关声明：[net_pkt_write_le16](#gac8a6ea1b0dc1bcd7b6a3f15869027dd1)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向 `net_pkt` 写入小端序（Little Endian）的 `uint16_t` 数据。

<a id="r_gadee5307216b6b3b725a2fd7584a224c9"></a>

```c
size_t net_pkt_remaining_data (struct net_pkt *pkt)
```

相关声明：[net_pkt_remaining_data](#gadee5307216b6b3b725a2fd7584a224c9)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

获取从当前游标位置（Current Cursor Position）起可读取的数据量。

<a id="r_ga9401d109ba978087139436c8a79c9bb0"></a>

```c
static size_t net_pkt_get_len (struct net_pkt *pkt)
```

相关声明：[net_pkt_get_len](#ga9401d109ba978087139436c8a79c9bb0)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

获取数据包存储的总字节数（Total Number of Bytes）。

<a id="r_ga2e7a0f9348a623c5160124da188445ee"></a>

```c
int net_pkt_update_length (struct net_pkt *pkt, size_t length)
```

相关声明：[net_pkt_update_length](#ga2e7a0f9348a623c5160124da188445ee)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

更新数据包总长度（Overall Packet Length）。

<a id="r_ga434c347a32600ee113c0e1cc13f70cd4"></a>

```c
int net_pkt_pull (struct net_pkt *pkt, size_t length)
```

相关声明：[net_pkt_pull](#ga434c347a32600ee113c0e1cc13f70cd4)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

从数据包当前游标位置（Current Cursor Position）移除数据。

<a id="r_gadb3b705a0431b3bb98fb2e8193c3b510"></a>

```c
uint16_t net_pkt_get_current_offset (struct net_pkt *pkt)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_pkt_get_current_offset](#gadb3b705a0431b3bb98fb2e8193c3b510)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

根据游标获取它在数据包中的实际偏移量（Actual Offset）。

<a id="r_gaf4ee5a8903b495e000a3a4c8a8493160"></a>

```c
bool net_pkt_is_contiguous (struct net_pkt *pkt, size_t size)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_pkt_is_contiguous](#gaf4ee5a8903b495e000a3a4c8a8493160)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

检查指定大小的数据是否能够连续存放（Fit Contiguously）。

<a id="r_gafbd6c0ab33139b134f67a8f8c0096445"></a>

```c
size_t net_pkt_get_contiguous_len (struct net_pkt *pkt)
```

相关声明：[net_pkt_get_contiguous_len](#gafbd6c0ab33139b134f67a8f8c0096445)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

获取连续缓冲区空间（Contiguous Buffer Space）。

<a id="r_gaa00da4276fd4a01faf80a92796f78e70"></a>

```c
void * net_pkt_get_data (struct net_pkt *pkt, struct net_pkt_data_access *access)
```

相关声明：[net_pkt_get_data](#gaa00da4276fd4a01faf80a92796f78e70)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

以连续方式（Contiguous Way）从网络数据包中获取数据。

<a id="r_ga98df84477b35e203b11029fc4ddec1cc"></a>

```c
int net_pkt_set_data (struct net_pkt *pkt, struct net_pkt_data_access *access)
```

相关声明：[net_pkt_set_data](#ga98df84477b35e203b11029fc4ddec1cc)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

向网络数据包设置连续数据（Contiguous Data）。

<a id="r_gac7226cbfa2da28408f9691d375bc8f9f"></a>

```c
static int net_pkt_acknowledge_data (struct net_pkt *pkt, struct net_pkt_data_access *access)
```

相关声明：[net_pkt_acknowledge_data](#gac7226cbfa2da28408f9691d375bc8f9f)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

确认先前从网络数据包取得的连续数据（Contiguous Data）。数据包需要设为覆盖模式（Overwrite Mode）。

## 11.4\_详细说明（Detailed Documentation）

<a id="ga94ab6300b59d739c4e3c5604d3fbe8a5"></a>

### `NET_PKT_DATA_POOL_DEFINE`

```c
#define NET_PKT_DATA_POOL_DEFINE ( name, count )
```

```c
#include <zephyr/net/net_pkt.h>
```

展开值（Value）：

```c
NET_BUF_POOL_DEFINE(name, count, CONFIG_NET_BUF_DATA_SIZE,      \
                    0, NULL)
```

创建数据分片 `net_buf` 缓冲池（Data Fragment Pool）。

`net_buf` 缓冲池（Pool）用于存储网络数据包的实际数据。它必须与一个 `net_pkt` 内存块池（Slab，`NET_PKT_SLAB_DEFINE`）配套使用，后者用于存储数据包元信息（Meta-information）。应用程序可使用此宏定义额外的、按上下文定制的发送数据包池（Per-context TX Packet Pools），参见 `net_context_setup_pools()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 缓冲池名称（Pool Name）。 |
| `count` | 此缓冲池（Pool）中的 `net_buf` 数量。 |

<a id="gad63d4802ad4e10b89829aed35a9ae804"></a>

### `NET_PKT_FRAG_FOR_EACH`

```c
#define NET_PKT_FRAG_FOR_EACH ( _pkt, _var )
```

```c
#include <zephyr/net/net_pkt.h>
```

展开值（Value）：

```c
for (struct net_buf *_var = (_pkt)->frags; _var != NULL; \
     _var = _var->frags)
```

遍历网络数据包（Network Packet）的全部分片（Fragments）。

遍历网络数据包库缓冲区（Network Packet Library Buffer）的分片链（Fragment Chain）。

使用示例：

原始示例（Example）：

```c
NET_PKT_FRAG_FOR_EACH(pkt, frag) {
    do_something(frag->data, frag->len);
}
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_pkt` | 指向网络数据包库（Network Packet Library）头缓冲区的指针，要遍历的是该缓冲区的分片链（Fragment Chain）。 |
| `_var` | 迭代器变量（Iterator Variable）的名称。宏在内部将此变量声明为 `struct net_buf *`，并在每次迭代时更新它。 |

**说明（Note）**：注意（Note）：从第一个分片缓冲区（Fragment Buffer）`(_pkt)->frags` 开始迭代。

<a id="ga2b2d0900ae76674d418918ec955bad48"></a>

### `net_pkt_print_frags`

```c
#define net_pkt_print_frags ( pkt)
```

```c
#include <zephyr/net/net_pkt.h>
```

<a id="gafc7e98d5b64d816faabcbaa2ec22a2bb"></a>

### `NET_PKT_SLAB_DEFINE`

```c
#define NET_PKT_SLAB_DEFINE ( name, count )
```

```c
#include <zephyr/net/net_pkt.h>
```

展开值（Value）：

```c
K_MEM_SLAB_DEFINE_TYPE(name, struct net_pkt, count);            \
NET_PKT_ALLOC_STATS_DEFINE(pkt_alloc_stats_##name, name)
```

创建 `net_pkt` 内存块池（Slab）。

`net_pkt` 内存块池（Slab）用于存储网络数据包的元信息（Meta-information）。它必须与一个数据分片池（Data Fragment Pool，`NET_PKT_DATA_POOL_DEFINE`）配套使用，后者用于存储实际数据包数据。应用程序可使用此宏定义额外的、按上下文定制的发送数据包内存块池（Per-context TX Packet Slabs），参见 `net_context_setup_pools()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 内存块池名称（Slab Name）。 |
| `count` | 此内存块池（Slab）中的 `net_pkt` 数量。 |

<a id="gac7226cbfa2da28408f9691d375bc8f9f"></a>

### `net_pkt_acknowledge_data()`

```c
int net_pkt_acknowledge_data ( struct net_pkt * pkt, struct net_pkt_data_access * access )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_pkt.h>
```

确认先前从网络数据包取得的连续数据（Contiguous Data）。数据包需要设为覆盖模式（Overwrite Mode）。

<a id="ga90d97ba913a875b3ee438e0ea8a970fd"></a>

### `net_pkt_alloc()`

```c
struct net_pkt * net_pkt_alloc ( k_timeout_t timeout)
```

```c
#include <zephyr/net/net_pkt.h>
```

分配一个已初始化的 `net_pkt`。

目前使用两个池（Pools）：一个用于发送（TX），一个用于接收（RX）。此分配器必须用于 TX。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `timeout` | 等待分配（Allocation）的最长时间。 |

**返回（Returns）**：返回值（Returns）：成功时返回指向新分配的 `net_pkt` 的指针，否则返回 `NULL`。

<a id="gae31b4afd510bce346f7d00a9ec5d190d"></a>

### `net_pkt_alloc_buffer()`

```c
int net_pkt_alloc_buffer ( struct net_pkt * pkt, size_t size, enum net_ip_protocol proto, k_timeout_t timeout )
```

```c
#include <zephyr/net/net_pkt.h>
```

为 `net_pkt` 分配缓冲区（Buffer）。

此分配器（Allocator）会考虑头部所需空间、最大传输单元（MTU）以及已有缓冲区（如果存在）。注意，由于这些因素，实际分配大小可能小于或大于请求大小。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 需要为其分配缓冲区（Buffer）的网络数据包（Network Packet）。 |
| `size` | 请求的缓冲区大小（Buffer Size）。 |
| `proto` | IP 协议类型（Protocol Type），`0` 可表示无协议。 |
| `timeout` | 等待分配（Allocation）的最长时间。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负错误码（errno）。

<a id="ga53819889ad86bc2c43407f12f113bb94"></a>

### `net_pkt_alloc_buffer_raw()`

```c
int net_pkt_alloc_buffer_raw ( struct net_pkt * pkt, size_t size, k_timeout_t timeout )
```

```c
#include <zephyr/net/net_pkt.h>
```

为 `net_pkt` 分配指定大小的缓冲区（Buffer），没有额外前置条件（Preconditions）。

如果使用固定大小缓冲区（Fixed Size Buffers），实际缓冲区大小可能大于请求大小。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 需要为其分配缓冲区（Buffer）的网络数据包（Network Packet）。 |
| `size` | 请求的缓冲区大小（Buffer Size）。 |
| `timeout` | 等待分配（Allocation）的最长时间。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负错误码（errno）。

<a id="ga0a292103ba0eacd62a15447e2765a485"></a>

### `net_pkt_alloc_buffer_with_reserve()`

```c
int net_pkt_alloc_buffer_with_reserve ( struct net_pkt * pkt, size_t size, size_t reserve, enum net_ip_protocol proto, k_timeout_t timeout )
```

```c
#include <zephyr/net/net_pkt.h>
```

为 `net_pkt` 分配缓冲区，并在第一个 `net_buf` 中预留一些空间。

此分配器（Allocator）会考虑头部所需空间、最大传输单元（MTU）以及已有缓冲区（如果存在）。注意，由于这些因素，实际分配大小可能小于或大于请求大小。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 需要为其分配缓冲区（Buffer）的网络数据包（Network Packet）。 |
| `size` | 请求的缓冲区大小（Buffer Size）。 |
| `reserve` | 要预留的链路层头部大小（L2 Header Size）。可以为 `0`，此时 L2 头部放在独立的 `net_buf` 中。 |
| `proto` | IP 协议类型（Protocol Type），`0` 可表示无协议。 |
| `timeout` | 等待分配（Allocation）的最长时间。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负错误码（errno）。

<a id="gaf1edbaab59576262647089fa1751d9e3"></a>

### `net_pkt_alloc_from_slab()`

```c
struct net_pkt * net_pkt_alloc_from_slab ( struct k_mem_slab * slab, k_timeout_t timeout )
```

```c
#include <zephyr/net/net_pkt.h>
```

从指定内存块池（Slab）分配一个已初始化的 `net_pkt`。

与使用核心内存块池（Core Slabs）的 `net_pkt_alloc()` 不同，此函数使用外部内存块池（External Slab），参见 `NET_PKT_SLAB_DEFINE()`。除非清楚其用途，否则不要使用。基本上，只有 `net_context` 应使用此函数，以便在其本地内存块池／缓冲池（如果存在）中先分配数据包，再分配缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `slab` | 用于分配数据包（Packet）的内存块池（Slab）。 |
| `timeout` | 等待分配（Allocation）的最长时间。 |

**返回（Returns）**：返回值（Returns）：成功时返回指向新分配的 `net_pkt` 的指针，否则返回 `NULL`。

<a id="ga770ffe22fc797691b1fc89954d60b2e6"></a>

### `net_pkt_alloc_on_iface()`

```c
struct net_pkt * net_pkt_alloc_on_iface ( struct net_if * iface, k_timeout_t timeout )
```

```c
#include <zephyr/net/net_pkt.h>
```

为指定网络接口（Network Interface）分配网络数据包（Network Packet）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 数据包（Packet）预计经过的网络接口（Network Interface）。 |
| `timeout` | 等待分配（Allocation）的最长时间。 |

**返回（Returns）**：返回值（Returns）：成功时返回指向新分配的 `net_pkt` 的指针，否则返回 `NULL`。

<a id="ga4ea4f0897e5fe4dfaf7ceca5f18f1702"></a>

### `net_pkt_alloc_with_buffer()`

```c
struct net_pkt * net_pkt_alloc_with_buffer ( struct net_if * iface, size_t size, net_sa_family_t family, enum net_ip_protocol proto, k_timeout_t timeout )
```

```c
#include <zephyr/net/net_pkt.h>
```

一次性分配网络数据包（Network Packet）及其缓冲区（Buffer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 数据包（Packet）预计经过的网络接口（Network Interface）。 |
| `size` | 缓冲区大小（Buffer Size）。 |
| `family` | 数据包所属的地址族（Family）。 |
| `proto` | IP 协议类型（Protocol Type），`0` 可表示无协议。 |
| `timeout` | 等待分配（Allocation）的最长时间。 |

**返回（Returns）**：返回值（Returns）：成功时返回指向新分配的 `net_pkt` 的指针，否则返回 `NULL`。

<a id="ga2b11492ae3c16368aa6a0ab8f47b67e7"></a>

### `net_pkt_append_buffer()`

```c
void net_pkt_append_buffer ( struct net_pkt * pkt, struct net_buf * buffer )
```

```c
#include <zephyr/net/net_pkt.h>
```

向数据包追加缓冲区（Append Buffer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 要向其追加缓冲区（Buffer）的网络数据包（Network Packet）。 |
| `buffer` | 要追加的缓冲区（Buffer）。 |

<a id="gaeed119d192e3a14ea3eea6e623334519"></a>

### `net_pkt_available_buffer()`

```c
size_t net_pkt_available_buffer ( struct net_pkt * pkt)
```

```c
#include <zephyr/net/net_pkt.h>
```

获取数据包（Pkt）的可用缓冲区空间（Available Buffer Space）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 要评估其可用缓冲空间（Buffer Availability）的 `net_pkt`。 |

**说明（Note）**：注意（Note）：任何分片（Fragment）中预留的字节，即头部预留空间（Headroom），均不计入可用空间。

**返回（Returns）**：返回值（Returns）：可用缓冲空间大小（Amount of Buffer Available）。

<a id="gaa9f63047b7945a4a155e5d88eac5203b"></a>

### `net_pkt_available_payload_buffer()`

```c
size_t net_pkt_available_payload_buffer ( struct net_pkt * pkt, enum net_ip_protocol proto )
```

```c
#include <zephyr/net/net_pkt.h>
```

获取数据包（Pkt）可供有效载荷（Payload）使用的缓冲区空间。

与 `net_pkt_available_buffer()` 不同，此函数会考虑头部空间（Headers Space）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 要评估其可用载荷缓冲空间（Payload Buffer Availability）的 `net_pkt`。 |
| `proto` | IP 协议类型（Protocol Type），`0` 可表示无协议。 |

**说明（Note）**：注意（Note）：任何分片（Fragment）中预留的字节，即头部预留空间（Headroom），均不计入可用空间。

**返回（Returns）**：返回值（Returns）：可供载荷使用的缓冲空间大小（Buffer Available for Payload）。

<a id="gaefefe50d0c68fb4997abc7b309740959"></a>

### `net_pkt_clone()`

```c
struct net_pkt * net_pkt_clone ( struct net_pkt * pkt, k_timeout_t timeout )
```

```c
#include <zephyr/net/net_pkt.h>
```

克隆数据包（Pkt）及其缓冲区（Buffer）。

克隆数据包（Cloned Packet）会从原数据包所在的同一个池（Pool）分配。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 要克隆的原始数据包（Original Packet）。 |
| `timeout` | 等待空闲缓冲区（Free Buffer）的超时（Timeout）。 |

**返回（Returns）**：返回值（Returns）：出错时为 `NULL`，否则为克隆的数据包（Cloned Packet）。

<a id="gabf85446fb8000574b180d00c5db65a44"></a>

### `net_pkt_compact()`

```c
void net_pkt_compact ( struct net_pkt * pkt)
```

```c
#include <zephyr/net/net_pkt.h>
```

压紧数据包分片列表（Compact the Fragment List）。

将后续分片（Fragment）的数据移到前面分片的可用尾部空间（Tailroom）中，并移除空分片。此操作不会回收头部预留空间（Headroom），也不保证数据包最终仅包含一个分片。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 网络数据包（Network Packet）。 |

<a id="ga4648828ca353c8c0ecf00ae2648e963a"></a>

### `net_pkt_copy()`

```c
int net_pkt_copy ( struct net_pkt * pkt_dst, struct net_pkt * pkt_src, size_t length )
```

```c
#include <zephyr/net/net_pkt.h>
```

将一个数据包（Packet）的数据复制到另一个数据包中。

两个 `net_pkt` 游标（Cursor）均应正确初始化，并在需要时通过 `net_pkt_skip` 定位。操作后会更新游标。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt_dst` | 目标网络数据包（Destination Network Packet）。 |
| `pkt_src` | 源网络数据包（Source Network Packet）。 |
| `length` | 待复制数据的长度（Length）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负错误码（errno）。

<a id="gabd352b66cdeaff2fb45361a0fae62876"></a>

### `net_pkt_cursor_backup()`

```c
void net_pkt_cursor_backup ( struct net_pkt * pkt, struct net_pkt_cursor * backup )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_pkt.h>
```

备份 `net_pkt` 游标（Cursor）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 要备份其游标（Cursor）的 `net_pkt`。 |
| `backup` | 用于备份 `net_pkt` 游标（Cursor）的游标对象。 |

<a id="gabc42ba1bcd0801a116651d965e65b9cd"></a>

### `net_pkt_cursor_get_pos()`

```c
void * net_pkt_cursor_get_pos ( struct net_pkt * pkt)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_pkt.h>
```

返回游标当前位置（Current Cursor Position）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 要返回其游标位置（Cursor Position）的 `net_pkt`。 |

**返回（Returns）**：返回值（Returns）：游标位置（Cursor Position）。

<a id="ga1b7da39f62dfc8b8948d7689e2dd114a"></a>

### `net_pkt_cursor_init()`

```c
void net_pkt_cursor_init ( struct net_pkt * pkt)
```

```c
#include <zephyr/net/net_pkt.h>
```

初始化 `net_pkt` 游标（Cursor）。

根据 `net_pkt` 的缓冲区（Buffer）初始化其游标（Cursor）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 要初始化其游标（Cursor）的 `net_pkt`。 |

<a id="gad5ab788f01b4bb3640755e8c4a2c612e"></a>

### `net_pkt_cursor_restore()`

```c
void net_pkt_cursor_restore ( struct net_pkt * pkt, struct net_pkt_cursor * backup )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_pkt.h>
```

从备份恢复 `net_pkt` 游标（Cursor）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 要恢复其游标（Cursor）的 `net_pkt`。 |
| `backup` | 用于恢复 `net_pkt` 游标（Cursor）的源游标对象。 |

<a id="ga03a53365cfc2b6c3448763d81f56c2c0"></a>

### `net_pkt_frag_add()`

```c
void net_pkt_frag_add ( struct net_pkt * pkt, struct net_buf * frag )
```

```c
#include <zephyr/net/net_pkt.h>
```

在数据包分片列表（Fragment List）末尾添加一个分片。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | `pkt`：要向其添加分片（Fragment）的网络数据包（Network Packet）。 |
| `frag` | 要添加的分片（Fragment）。 |

<a id="ga956c784f5417f0f79976c6e106ad0d76"></a>

### `net_pkt_frag_del()`

```c
struct net_buf * net_pkt_frag_del ( struct net_pkt * pkt, struct net_buf * parent, struct net_buf * frag )
```

```c
#include <zephyr/net/net_pkt.h>
```

从数据包（Packet）中删除已有分片（Fragment）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | `frag` 所属的网络数据包（Network Packet）。 |
| `parent` | `frag` 的父分片（Parent Fragment）；没有时为 `NULL`。 |
| `frag` | 要删除的分片（Fragment）。 |

**返回（Returns）**：返回值（Returns）：指向后续分片（Following Fragment）的指针；没有更多分片时为 `NULL`。

<a id="gabcd375d9dbdca21855abe27d7b5a0a7e"></a>

### `net_pkt_frag_insert()`

```c
void net_pkt_frag_insert ( struct net_pkt * pkt, struct net_buf * frag )
```

```c
#include <zephyr/net/net_pkt.h>
```

在数据包分片列表（Fragment List）开头插入一个分片。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | `pkt`：要向其插入分片（Fragment）的网络数据包（Network Packet）。 |
| `frag` | 要插入的分片（Fragment）。 |

<a id="gaea5e1045d188b3abbd85717ff09d563a"></a>

### `net_pkt_frag_ref()`

```c
struct net_buf * net_pkt_frag_ref ( struct net_buf * frag)
```

```c
#include <zephyr/net/net_pkt.h>
```

增加数据包分片引用计数（Packet Fragment Reference Count）。

标记该分片（Fragment）仍在使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `frag` | 要增加引用（Ref）的网络分片（Network Fragment）。 |

**返回（Returns）**：返回值（Returns）：指向已增加引用的网络分片（Referenced Network Fragment）的指针。

<a id="ga5c75ef2149d2ba5ff07525988e0fb7cc"></a>

### `net_pkt_frag_unref()`

```c
void net_pkt_frag_unref ( struct net_buf * frag)
```

```c
#include <zephyr/net/net_pkt.h>
```

减少数据包分片引用计数（Packet Fragment Reference Count）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `frag` | 要释放引用（Unref）的网络分片（Network Fragment）。 |

<a id="gafbd6c0ab33139b134f67a8f8c0096445"></a>

### `net_pkt_get_contiguous_len()`

```c
size_t net_pkt_get_contiguous_len ( struct net_pkt * pkt)
```

```c
#include <zephyr/net/net_pkt.h>
```

获取连续缓冲区空间（Contiguous Buffer Space）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 网络数据包（Network Packet）。 |

**返回（Returns）**：返回值（Returns）：从当前游标位置（Cursor Position）开始的可用连续缓冲空间（Contiguous Buffer Space），单位为字节。出错时为 `0`。

<a id="gadb3b705a0431b3bb98fb2e8193c3b510"></a>

### `net_pkt_get_current_offset()`

```c
uint16_t net_pkt_get_current_offset ( struct net_pkt * pkt)
```

```c
#include <zephyr/net/net_pkt.h>
```

根据游标获取它在数据包中的实际偏移量（Actual Offset）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 网络数据包（Network Packet）。 |

**返回（Returns）**：返回值（Returns）：成功时为有效偏移量（Offset）；否则，由于无法计算偏移量，返回 `0`。

<a id="gaa00da4276fd4a01faf80a92796f78e70"></a>

### `net_pkt_get_data()`

```c
void * net_pkt_get_data ( struct net_pkt * pkt, struct net_pkt_data_access * access )
```

```c
#include <zephyr/net/net_pkt.h>
```

以连续方式（Contiguous Way）从网络数据包中获取数据。

`net_pkt` 的游标（Cursor）应正确初始化，并在需要时通过 `net_pkt_skip` 定位。与其他函数不同，操作后不会更新游标位置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 要从中获取数据的网络数据包（Network Packet）。 |
| `access` | 指向有效 `net_pkt_data_access` 的指针，该对象描述要以连续形式（Contiguous）获取的数据。 |

**返回（Returns）**：返回值（Returns）：指向所请求连续数据（Contiguous Data）的指针，否则为 `NULL`。

<a id="gafa7d666bddb182149d5f540880c46b4e"></a>

### `net_pkt_get_frag()`

```c
struct net_buf * net_pkt_get_frag ( struct net_pkt * pkt, size_t min_len, k_timeout_t timeout )
```

```c
#include <zephyr/net/net_pkt.h>
```

获取数据分片（Data Fragment），可来自用户专用缓冲池（User-specific Buffer Pool）或全局 DATA 池。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 网络数据包（Network Packet）。 |
| `min_len` | 所请求分片（Fragment）的最小长度。 |
| `timeout` | 决定网络缓冲池（Net Buffer Pool）为空时采取的操作。`K_NO_WAIT` 表示立即返回；`K_FOREVER` 表示一直等待到可用为止；其他值表示最多等待指定时长。 |

**返回（Returns）**：返回值（Returns）：成功时为网络缓冲区（Network Buffer），否则为 `NULL`。

<a id="ga7b02b95838b928febfd4970de5e9c9f9"></a>

### `net_pkt_get_info()`

```c
void net_pkt_get_info ( struct k_mem_slab ** rx, struct k_mem_slab ** tx, struct net_buf_pool ** rx_data, struct net_buf_pool ** tx_data )
```

```c
#include <zephyr/net/net_pkt.h>
```

获取预定义的 RX、TX 和 DATA 缓冲池（Pools）的信息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rx` | 返回指向接收池（RX Pool）的指针。 |
| `tx` | 返回指向发送池（TX Pool）的指针。 |
| `rx_data` | 返回指向接收数据池（RX DATA Pool）的指针。 |
| `tx_data` | 返回指向发送数据池（TX DATA Pool）的指针。 |

<a id="ga9401d109ba978087139436c8a79c9bb0"></a>

### `net_pkt_get_len()`

```c
size_t net_pkt_get_len ( struct net_pkt * pkt)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_pkt.h>
```

获取数据包存储的总字节数（Total Number of Bytes）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 网络数据包（Network Packet）。 |

**返回（Returns）**：返回值（Returns）：数据包（Packet）中存储的总字节数。

<a id="ga6f697a97dd09e24663cbddc332ec5f7c"></a>

### `net_pkt_get_reserve_data()`

```c
struct net_buf * net_pkt_get_reserve_data ( struct net_buf_pool * pool, size_t min_len, k_timeout_t timeout )
```

```c
#include <zephyr/net/net_pkt.h>
```

从给定缓冲池（Pool）获取数据缓冲区（Data Buffer）。

此版本通常对应用程序没有用途，主要供网络分片代码（Network Fragmentation Code）使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pool` | 要使用的 `net_buf` 缓冲池（Pool）。 |
| `min_len` | 所请求分片（Fragment）的最小长度。 |
| `timeout` | 决定网络缓冲池（Net Buffer Pool）为空时采取的操作。`K_NO_WAIT` 表示立即返回；`K_FOREVER` 表示一直等待到可用为止；其他值表示最多等待指定时长。 |

**返回（Returns）**：返回值（Returns）：成功时为网络缓冲区（Network Buffer），否则为 `NULL`。

<a id="gaf48f4aac4d16a367d46ca76bf038a485"></a>

### `net_pkt_get_reserve_rx_data()`

```c
struct net_buf * net_pkt_get_reserve_rx_data ( size_t min_len, k_timeout_t timeout )
```

```c
#include <zephyr/net/net_pkt.h>
```

从缓冲池（Pool）获取接收数据缓冲区（RX DATA Buffer）。

通常应改用 `net_pkt_get_frag()`。

此版本通常对应用程序没有用途，主要供网络分片代码（Network Fragmentation Code）使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `min_len` | 所请求分片（Fragment）的最小长度。 |
| `timeout` | 决定网络缓冲池（Net Buffer Pool）为空时采取的操作。`K_NO_WAIT` 表示立即返回；`K_FOREVER` 表示一直等待到可用为止；其他值表示最多等待指定时长。 |

**返回（Returns）**：返回值（Returns）：成功时为网络缓冲区（Network Buffer），否则为 `NULL`。

<a id="gaba26ee929f154978afbd007f7f2b0bc9"></a>

### `net_pkt_get_reserve_tx_data()`

```c
struct net_buf * net_pkt_get_reserve_tx_data ( size_t min_len, k_timeout_t timeout )
```

```c
#include <zephyr/net/net_pkt.h>
```

从缓冲池（Pool）获取发送数据缓冲区（TX DATA Buffer）。

通常应改用 `net_pkt_get_frag()`。

此版本通常对应用程序没有用途，主要供网络分片代码（Network Fragmentation Code）使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `min_len` | 所请求分片（Fragment）的最小长度。 |
| `timeout` | 决定网络缓冲池（Net Buffer Pool）为空时采取的操作。`K_NO_WAIT` 表示立即返回；`K_FOREVER` 表示一直等待到可用为止；其他值表示最多等待指定时长。 |

**返回（Returns）**：返回值（Returns）：成功时为网络缓冲区（Network Buffer），否则为 `NULL`。

<a id="gaf4ee5a8903b495e000a3a4c8a8493160"></a>

### `net_pkt_is_contiguous()`

```c
bool net_pkt_is_contiguous ( struct net_pkt * pkt, size_t size )
```

```c
#include <zephyr/net/net_pkt.h>
```

检查指定大小的数据是否能够连续存放（Fit Contiguously）。

`net_pkt` 的游标（Cursor）应正确初始化，并在需要时通过 `net_pkt_skip` 定位。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 网络数据包（Network Packet）。 |
| `size` | 要检查连续性（Contiguity）的大小。 |

**返回（Returns）**：返回值（Returns）：满足该条件时为 `true`，否则为 `false`。

<a id="gabd241a539bf1290f3d45610fd15b2c1f"></a>

### `net_pkt_memset()`

```c
int net_pkt_memset ( struct net_pkt * pkt, int byte, size_t length )
```

```c
#include <zephyr/net/net_pkt.h>
```

对 `net_pkt` 中的一部分数据执行内存填充（Memset）。

`net_pkt` 的游标（Cursor）应正确初始化，并在需要时通过 `net_pkt_skip` 定位。操作后会更新游标位置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 要从当前游标位置（Cursor Position）开始填充其缓冲区的 `net_pkt`。 |
| `byte` | 要写入内存（Memory）的字节值。 |
| `length` | 使用给定字节执行 `memset` 的数据量（Amount of Data）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负错误码（errno）。

<a id="ga434c347a32600ee113c0e1cc13f70cd4"></a>

### `net_pkt_pull()`

```c
int net_pkt_pull ( struct net_pkt * pkt, size_t length )
```

```c
#include <zephyr/net/net_pkt.h>
```

从数据包当前游标位置（Current Cursor Position）移除数据。

数据包游标（Packet Cursor）应正确初始化和定位。此函数会重置游标。其工作方式类似于 `net_buf_pull()`，但可以处理多个 `net_buf` 分片（Fragment）。

不会保留底层分片布局（Fragment Layout）：剩余数据可能被移动，或者分片的数据指针（Data Pointer）可能前移。调用者不得假定分片数据指针、头部预留空间（Headroom）或尾部空间（Tailroom）保持不变。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 网络数据包（Network Packet）。 |
| `length` | 要移除的字节数（Number of Bytes）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负错误码（errno）。

<a id="ga914be010ddd225a4fc2d6ab521ee7b64"></a>

### `net_pkt_read()`

```c
int net_pkt_read ( struct net_pkt * pkt, void * data, size_t length )
```

```c
#include <zephyr/net/net_pkt.h>
```

从 `net_pkt` 读取一部分数据。

`net_pkt` 的游标（Cursor）应正确初始化，并在需要时通过 `net_pkt_skip` 定位。操作后会更新游标位置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 要从中读取部分数据的网络数据包（Network Packet）。 |
| `data` | 用于接收所复制数据的目标缓冲区（Destination Buffer）。 |
| `length` | 要复制的数据量（Amount of Data）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负错误码（errno）。

<a id="ga500a318977cfecd4ec7c60cea01db2fc"></a>

### `net_pkt_read_be16()`

```c
int net_pkt_read_be16 ( struct net_pkt * pkt, uint16_t * data )
```

```c
#include <zephyr/net/net_pkt.h>
```

从 `net_pkt` 读取大端序（Big Endian）的 `uint16_t` 数据。

`net_pkt` 的游标（Cursor）应正确初始化，并在需要时通过 `net_pkt_skip` 定位。操作后会更新游标位置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 要从中读取的网络数据包（Network Packet）。 |
| `data` | 用于接收所复制数据的目标（Destination）`uint16_t`。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负错误码（errno）。

<a id="gab38c99947d02982073df65c0d5893d2c"></a>

### `net_pkt_read_be32()`

```c
int net_pkt_read_be32 ( struct net_pkt * pkt, uint32_t * data )
```

```c
#include <zephyr/net/net_pkt.h>
```

从 `net_pkt` 读取大端序（Big Endian）的 `uint32_t` 数据。

`net_pkt` 的游标（Cursor）应正确初始化，并在需要时通过 `net_pkt_skip` 定位。操作后会更新游标位置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 要从中读取的网络数据包（Network Packet）。 |
| `data` | 用于接收所复制数据的目标（Destination）`uint32_t`。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负错误码（errno）。

<a id="gaf3a1eb735316e155e3e30c1ef4395d4d"></a>

### `net_pkt_read_be64()`

```c
int net_pkt_read_be64 ( struct net_pkt * pkt, uint64_t * data )
```

```c
#include <zephyr/net/net_pkt.h>
```

从 `net_pkt` 读取大端序（Big Endian）的 `uint64_t` 数据。

`net_pkt` 的游标（Cursor）应正确初始化，并在需要时通过 `net_pkt_skip` 定位。操作后会更新游标位置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 要从中读取的网络数据包（Network Packet）。 |
| `data` | 用于接收所复制数据的目标（Destination）`uint64_t`。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负错误码（errno）。

<a id="gab1735ef4f6a2e538a2692358295dd8d1"></a>

### `net_pkt_read_le16()`

```c
int net_pkt_read_le16 ( struct net_pkt * pkt, uint16_t * data )
```

```c
#include <zephyr/net/net_pkt.h>
```

从 `net_pkt` 读取小端序（Little Endian）的 `uint16_t` 数据。

`net_pkt` 的游标（Cursor）应正确初始化，并在需要时通过 `net_pkt_skip` 定位。操作后会更新游标位置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 要从中读取的网络数据包（Network Packet）。 |
| `data` | 用于接收所复制数据的目标（Destination）`uint16_t`。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负错误码（errno）。

<a id="ga214e817ca3b5daa4126c0deecd4981d7"></a>

### `net_pkt_read_le32()`

```c
int net_pkt_read_le32 ( struct net_pkt * pkt, uint32_t * data )
```

```c
#include <zephyr/net/net_pkt.h>
```

从 `net_pkt` 读取小端序（Little Endian）的 `uint32_t` 数据。

`net_pkt` 的游标（Cursor）应正确初始化，并在需要时通过 `net_pkt_skip` 定位。操作后会更新游标位置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 要从中读取的网络数据包（Network Packet）。 |
| `data` | 用于接收所复制数据的目标（Destination）`uint32_t`。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负错误码（errno）。

<a id="ga9a6e19dff44a64582edda084aa7ec96e"></a>

### `net_pkt_read_le64()`

```c
int net_pkt_read_le64 ( struct net_pkt * pkt, uint64_t * data )
```

```c
#include <zephyr/net/net_pkt.h>
```

从 `net_pkt` 读取小端序（Little Endian）的 `uint64_t` 数据。

`net_pkt` 的游标（Cursor）应正确初始化，并在需要时通过 `net_pkt_skip` 定位。操作后会更新游标位置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 要从中读取的网络数据包（Network Packet）。 |
| `data` | 用于接收所复制数据的目标（Destination）`uint64_t`。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负错误码（errno）。

<a id="gaf9b2753cb514804a77d9494c9f070089"></a>

### `net_pkt_read_u8()`

```c
int net_pkt_read_u8 ( struct net_pkt * pkt, uint8_t * data )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_pkt.h>
```

从 `net_pkt` 读取一个字节（`uint8_t`）。

`net_pkt` 的游标（Cursor）应正确初始化，并在需要时通过 `net_pkt_skip` 定位。操作后会更新游标位置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 要从中读取的网络数据包（Network Packet）。 |
| `data` | 用于接收所复制数据的目标（Destination）`uint8_t`。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负错误码（errno）。

<a id="ga4e83d4f60b46db8f57798c0e96d6cd7a"></a>

### `net_pkt_ref()`

```c
struct net_pkt * net_pkt_ref ( struct net_pkt * pkt)
```

```c
#include <zephyr/net/net_pkt.h>
```

增加数据包引用计数（Packet Reference Count）。

标记该数据包（Packet）仍在使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 要增加引用（Ref）的网络数据包（Network Packet）。 |

**返回（Returns）**：返回值（Returns）：成功时为网络数据包（Network Packet），否则为 `NULL`。

<a id="gadee5307216b6b3b725a2fd7584a224c9"></a>

### `net_pkt_remaining_data()`

```c
size_t net_pkt_remaining_data ( struct net_pkt * pkt)
```

```c
#include <zephyr/net/net_pkt.h>
```

获取从当前游标位置（Current Cursor Position）起可读取的数据量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 网络数据包（Network Packet）。 |

**返回（Returns）**：返回值（Returns）：从当前数据包游标（Packet Cursor）开始可读取的数据量。

<a id="gab657c80669733a4afefaf1be6310107e"></a>

### `net_pkt_remove_tail()`

```c
int net_pkt_remove_tail ( struct net_pkt * pkt, size_t length )
```

```c
#include <zephyr/net/net_pkt.h>
```

从数据包尾部（Tail）移除 `length` 个字节。

此函数不考虑数据包游标（Packet Cursor）。它用于从数据包尾部移除不需要的字节，例如附加的循环冗余校验（CRC）。如果移除的字节覆盖了一个或多个完整缓冲区，会负责释放这些缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 网络数据包（Network Packet）。 |
| `length` | 要移除的字节数（Number of Bytes）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | 数据包长度（Packet Length）小于 `length` 时。 |

<a id="ga4cec027a0de4807879fd3bd3aed4f12a"></a>

### `net_pkt_rx_alloc()`

```c
struct net_pkt * net_pkt_rx_alloc ( k_timeout_t timeout)
```

```c
#include <zephyr/net/net_pkt.h>
```

分配一个用于接收（RX）的已初始化 `net_pkt`。

目前使用两个池（Pools）：一个用于发送（TX），一个用于接收（RX）。此分配器必须用于 RX。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `timeout` | 等待分配（Allocation）的最长时间。 |

**返回（Returns）**：返回值（Returns）：成功时返回指向新分配的 `net_pkt` 的指针，否则返回 `NULL`。

<a id="ga66aec729118e4d927c921b872df82dda"></a>

### `net_pkt_rx_clone()`

```c
struct net_pkt * net_pkt_rx_clone ( struct net_pkt * pkt, k_timeout_t timeout )
```

```c
#include <zephyr/net/net_pkt.h>
```

克隆数据包（Pkt）及其缓冲区（Buffer）。

克隆数据包（Cloned Packet）将从接收数据包池（RX Packet Pool）分配。译注：原文 “poll” 按上下文作 “pool” 处理。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 要克隆的原始数据包（Original Packet）。 |
| `timeout` | 等待空闲缓冲区（Free Buffer）的超时（Timeout）。 |

**返回（Returns）**：返回值（Returns）：出错时为 `NULL`，否则为克隆的数据包（Cloned Packet）。

<a id="ga98df84477b35e203b11029fc4ddec1cc"></a>

### `net_pkt_set_data()`

```c
int net_pkt_set_data ( struct net_pkt * pkt, struct net_pkt_data_access * access )
```

```c
#include <zephyr/net/net_pkt.h>
```

向网络数据包设置连续数据（Contiguous Data）。

`net_pkt` 的游标（Cursor）应正确初始化，并在需要时通过 `net_pkt_skip` 定位。操作后会更新游标位置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 要向其设置数据的网络数据包（Network Packet）。 |
| `access` | 指向有效 `net_pkt_data_access` 的指针，该对象描述要设置的数据。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 0，否则返回负的 `errno` 值。

<a id="ga26ae9d1286cb98d255f1bfb65201f1e2"></a>

### `net_pkt_shallow_clone()`

```c
struct net_pkt * net_pkt_shallow_clone ( struct net_pkt * pkt, k_timeout_t timeout )
```

```c
#include <zephyr/net/net_pkt.h>
```

克隆数据包（Pkt），并增加其缓冲区引用计数（Buffer Refcount）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 要浅克隆（Shallow Clone）的原始数据包（Original Packet）。 |
| `timeout` | 等待空闲数据包（Free Packet）的超时（Timeout）。 |

**返回（Returns）**：返回值（Returns）：出错时为 `NULL`，否则为克隆的数据包（Cloned Packet）。

<a id="ga223a79baa1e740a53c4ed0f083d62185"></a>

### `net_pkt_skip()`

```c
int net_pkt_skip ( struct net_pkt * pkt, size_t length )
```

```c
#include <zephyr/net/net_pkt.h>
```

跳过 `net_pkt` 中的一部分数据。

`net_pkt` 的游标（Cursor）应正确初始化。此函数使游标前进请求的长度。`pkt->overwrite` 的值会影响函数行为：为 `false` 时，数据包长度增加 `length` 字节。此时其行为类似 `net_pkt_write` 或 `net_pkt_memset`，区别是它不会修改缓冲区内容本身，因此这些内容可能只是无效数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 要更新其游标（Cursor）、从缓冲区跳过给定数据量的 `net_pkt`。 |
| `length` | 要在缓冲区（Buffer）中跳过的数据量。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负错误码（errno）。

<a id="ga71d1c49f68afab07324cebd835f08a29"></a>

### `net_pkt_trim_buffer()`

```c
void net_pkt_trim_buffer ( struct net_pkt * pkt)
```

```c
#include <zephyr/net/net_pkt.h>
```

裁剪 `net_pkt` 缓冲区（Trim Buffer）。

此操作主要检查未使用的缓冲区（Unused Buffers），并按需释放它们。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 要裁剪其缓冲区（Buffer）的 `net_pkt`。 |

<a id="ga893d1660fd18ad5842224fda78466099"></a>

### `net_pkt_unref()`

```c
void net_pkt_unref ( struct net_pkt * pkt)
```

```c
#include <zephyr/net/net_pkt.h>
```

将数据包放回可用数据包内存块池（Packets Slab）。

释放数据包（Packet）以供其他用途。应用程序使用完数据包后必须调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 要释放的网络数据包（Network Packet）。 |

<a id="ga2e7a0f9348a623c5160124da188445ee"></a>

### `net_pkt_update_length()`

```c
int net_pkt_update_length ( struct net_pkt * pkt, size_t length )
```

```c
#include <zephyr/net/net_pkt.h>
```

更新数据包总长度（Overall Packet Length）。

与下文的 `net_pkt_pull()` 不同，此函数不考虑数据包游标（Packet Cursor）。它主要是为 IPv4 和 IPv6 输入函数提供的辅助函数，根据给定参数缩减总长度。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 网络数据包（Network Packet）。 |
| `length` | 数据包的新长度（New Packet Length）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负错误码（errno）。

<a id="gae99eadd977b7f66ecc91d2ccba34c6fa"></a>

### `net_pkt_write()`

```c
int net_pkt_write ( struct net_pkt * pkt, const void * data, size_t length )
```

```c
#include <zephyr/net/net_pkt.h>
```

向 `net_pkt` 写入数据。

`net_pkt` 的游标（Cursor）应正确初始化，并在需要时通过 `net_pkt_skip` 定位。操作后会更新游标位置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 要向其写入的网络数据包（Network Packet）。 |
| `data` | 要写入的数据（Data to be written）。 |
| `length` | 待写入数据的长度（Length）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负错误码（errno）。

<a id="ga8e5083388ccb0333fdcf745bc60ad260"></a>

### `net_pkt_write_be16()`

```c
int net_pkt_write_be16 ( struct net_pkt * pkt, uint16_t data )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_pkt.h>
```

向 `net_pkt` 写入大端序（Big Endian）的 `uint16_t` 数据。

`net_pkt` 的游标（Cursor）应正确初始化，并在需要时通过 `net_pkt_skip` 定位。操作后会更新游标位置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 要从中读取的网络数据包（Network Packet）。 |
| `data` | 要写入的、采用主机字节序（Host Byte Order）的 `uint16_t` 值。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负错误码（errno）。

<a id="ga053aff4ff0a501f336132c35b7fb2022"></a>

### `net_pkt_write_be32()`

```c
int net_pkt_write_be32 ( struct net_pkt * pkt, uint32_t data )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_pkt.h>
```

向 `net_pkt` 写入大端序（Big Endian）的 `uint32_t` 数据。

`net_pkt` 的游标（Cursor）应正确初始化，并在需要时通过 `net_pkt_skip` 定位。操作后会更新游标位置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 要从中读取的网络数据包（Network Packet）。 |
| `data` | 要写入的、采用主机字节序（Host Byte Order）的 `uint32_t` 值。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负错误码（errno）。

<a id="gac8a6ea1b0dc1bcd7b6a3f15869027dd1"></a>

### `net_pkt_write_le16()`

```c
int net_pkt_write_le16 ( struct net_pkt * pkt, uint16_t data )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_pkt.h>
```

向 `net_pkt` 写入小端序（Little Endian）的 `uint16_t` 数据。

`net_pkt` 的游标（Cursor）应正确初始化，并在需要时通过 `net_pkt_skip` 定位。操作后会更新游标位置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 要从中读取的网络数据包（Network Packet）。 |
| `data` | 要写入的、采用主机字节序（Host Byte Order）的 `uint16_t` 值。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负错误码（errno）。

<a id="gaf2388032e4e0b76fe32e4618ef3ea548"></a>

### `net_pkt_write_le32()`

```c
int net_pkt_write_le32 ( struct net_pkt * pkt, uint32_t data )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_pkt.h>
```

向 `net_pkt` 写入小端序（Little Endian）的 `uint32_t` 数据。

`net_pkt` 的游标（Cursor）应正确初始化，并在需要时通过 `net_pkt_skip` 定位。操作后会更新游标位置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 要从中读取的网络数据包（Network Packet）。 |
| `data` | 要写入的、采用主机字节序（Host Byte Order）的 `uint32_t` 值。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负错误码（errno）。

<a id="gaa5129f661075c13d9b59627ae9110bd1"></a>

### `net_pkt_write_u8()`

```c
int net_pkt_write_u8 ( struct net_pkt * pkt, uint8_t data )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_pkt.h>
```

向 `net_pkt` 写入一个字节（`uint8_t`）的数据。

`net_pkt` 的游标（Cursor）应正确初始化，并在需要时通过 `net_pkt_skip` 定位。操作后会更新游标位置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 要从中读取的网络数据包（Network Packet）。 |
| `data` | 要写入的 `uint8_t` 值。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负错误码（errno）。


## 11.5\_原页交叉引用（Cross References）

- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_ip_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaf06819bf427cc58be1229b27b373ca31)
- [net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [zephyr/net/net_pkt.h](../api_file_network_pcie_reference/P009_zephyr__net__net_pkt.h_文件参考.md)
- [NET_BUF_POOL_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga810aba8ba321fd012edc238ea9fe19dc)
- [net_context_setup_pools()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga41d258362d6a7a703bc0b65d08e2b4c4)
- [frags](../network_core_model_reference/P046_net_buf_结构体.md#a1fa032cc23854c35eae013020823fa88)
- [网络分组库（Network Packet Library）](P011_网络分组库（Network Packet Library）.md)
- [K_MEM_SLAB_DEFINE_TYPE](../heap_reference/P003_固定块内存池公共接口.md#ga8af8242518910449d31f7e97bed738cc)
- [net_context](../network_core_model_reference/P055_net_context_结构体.md)
- [net_buf_pull()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaef433d92734dd8691c292abdb823ba0e)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__net__buf_html_ga810aba8ba321fd012edc238ea9fe19dc"></a>
<a id="astructnet__buf_html"></a>
<a id="astructnet__buf_html_a1fa032cc23854c35eae013020823fa88"></a>
<a id="agroup__net__pkt_html_gad63d4802ad4e10b89829aed35a9ae804"></a>
<a id="agroup__mem__slab__apis_html_ga8af8242518910449d31f7e97bed738cc"></a>
<a id="astructnet__pkt_html"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P010_LoRaWAN API主题.md) · [返回大纲](大纲.md) · [下一章](P012_USB 电力传输（USB Power Delivery）.md)
