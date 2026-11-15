---
id: learning.zephyr-docs.network-application-model-reference.page-20
title: dns_resolve_context__dns_pending_query_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdns__resolve__context_1_1dns__pending__query.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_dns\_resolve\_context\_\_dns\_pending\_query\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdns__resolve__context_1_1dns__pending__query.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

结果回调（Result Callbacks）。

```c
#include <zephyr/net/dns_resolve.h>
```

<a id="details"></a>

结果回调（Result Callbacks）。这里设置多个回调，以便同时执行多个查询。仅在持有锁（Lock）时才可检查和修改此结构的内容。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 20.1\_数据成员（Data Fields）

<a id="r_a6f76b200b8c421399987be83b72b9230"></a>

```c
struct k_work_delayable timer
```

相关声明：[k_work_delayable](https://docs.zephyrproject.org/latest/doxygen/html/structk__work__delayable.html)、[timer](#a6f76b200b8c421399987be83b72b9230)。

超时定时器（Timeout Timer）。

<a id="r_a4260371a741b3c2e752848955eee5cae"></a>

```c
struct dns_resolve_context * ctx
```

相关声明：[dns_resolve_context](P019_dns_resolve_context_结构体.md)、[ctx](#a4260371a741b3c2e752848955eee5cae)。

指向ctx的回指针（Back Pointer），供超时处理程序使用。

<a id="r_aacf4003ce035658038ae44773091f2d0"></a>

```c
dns_resolve_cb_t cb
```

相关声明：[dns_resolve_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gafe22d0ef90c581982561ef0c33d1f722)、[cb](#aacf4003ce035658038ae44773091f2d0)。

结果回调（Result Callback）。

<a id="r_a6a1c93f3eab8f9aa55dbb26e704bb343"></a>

```c
void * user_data
```

相关声明：[user_data](#a6a1c93f3eab8f9aa55dbb26e704bb343)。

用户数据（User Data）。

<a id="r_a106464bda8d56283b06251c37964906b"></a>

```c
const char * query
```

相关声明：[query](#a106464bda8d56283b06251c37964906b)。

包含待解析对象的字符串，例如www.example.com。

<a id="r_af5796eb469e2fe3bcebea2ad55a8fd78"></a>

```c
enum dns_query_type query_type
```

相关声明：[dns_query_type](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga7169c5a920fb1b0d77910a6ab922e3f0)、[query_type](#af5796eb469e2fe3bcebea2ad55a8fd78)。

查询类型（Query Type）。

<a id="r_a773e2ad2bedb2d1030df3590e9a14173"></a>

```c
uint16_t id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[id](#a773e2ad2bedb2d1030df3590e9a14173)。

本次查询的DNS标识（DNS ID）。

<a id="r_a168fea99e8c6760cab49611ceb5a6fc1"></a>

```c
uint16_t query_hash
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[query_hash](#a168fea99e8c6760cab49611ceb5a6fc1)。

正在查询的DNS名称与查询类型组合的哈希（Hash）。

<a id="r_a1dccc8f927ba987da56c5d704ab67e1a"></a>

```c
uint16_t orig_query_hash
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[orig_query_hash](#a1dccc8f927ba987da56c5d704ab67e1a)。

调用方请求的原始DNS名称与查询类型组合的哈希（Hash）。

<a id="r_a334caa7c36c9b10d3fff51bfdee68e72"></a>

```c
uint8_t additional_queries
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[additional_queries](#a334caa7c36c9b10d3fff51bfdee68e72)。

<a id="r_ac3209c8e0fec2f52ee4da56b388ecda6"></a>

```c
bool cb_called
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[cb_called](#ac3209c8e0fec2f52ee4da56b388ecda6)。

表示回调至少已调用一次的标志（Flag）。

<a id="r_a28174f11134146a800588f5e32d4a147"></a>

```c
k_timepoint_t deadline
```

相关声明：[k_timepoint_t](../timer_reference/P088_内核时间点类型.md)、[deadline](#a28174f11134146a800588f5e32d4a147)。

查询截止时间（Query Deadline），用于保证服务器回退处理不超出最初的超时范围。

```c
struct {
```

<a id="r_aa9724f051381291b9e4bc21319749cf6"></a>

```c
atomic_t sent
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[sent](#a5402d71d11a3ef006703a1a8e6cc7651)。

记录已查询服务器的位集合（Bitset）。

<a id="r_a6c95197621a936fffa2625aa6f28f205"></a>

```c
atomic_t pending
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[pending](#aa2f4ee968b610ba74cdd7880076e1508)。

记录当前等待应答服务器的位集合（Bitset）。

<a id="r_a5170dd7d24867afe9172c62a344ea6de"></a>

```c
atomic_t failed
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[failed](#a8810792264f30d55b03d53a775bc68fa)。

记录本次查询已失败服务器的位集合（Bitset）。

<a id="r_ad3fb3c0f90eba5506a1152ae1bb7d6ab"></a>

```c
} servers
```

相关声明：[servers](#ad3fb3c0f90eba5506a1152ae1bb7d6ab)。

已配置DNS服务器的逐查询状态（Per-Query State）。

<a id="r_a8473953176dd2310fb4cfe28fb04948d"></a>

```c
enum dns_resolve_status last_status
```

相关声明：[dns_resolve_status](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga5baf1fea0482fb3a940b4f5350a3c58e)、[last_status](#a8473953176dd2310fb4cfe28fb04948d)。

已尝试服务器最近报告的终止状态（Terminal Status）。

## 20.2\_详细说明（Detailed Documentation）

<a id="a334caa7c36c9b10d3fff51bfdee68e72"></a>

### `additional_queries`

```c
uint8_t dns_resolve_context::dns_pending_query::additional_queries
```

<a id="aacf4003ce035658038ae44773091f2d0"></a>

### `cb`

```c
dns_resolve_cb_t dns_resolve_context::dns_pending_query::cb
```

结果回调（Result Callback）。

空值表示此槽位（Slot）未被使用。

<a id="ac3209c8e0fec2f52ee4da56b388ecda6"></a>

### `cb_called`

```c
bool dns_resolve_context::dns_pending_query::cb_called
```

表示回调至少已调用一次的标志（Flag）。

<a id="a4260371a741b3c2e752848955eee5cae"></a>

### `ctx`

```c
struct dns_resolve_context* dns_resolve_context::dns_pending_query::ctx
```

指向ctx的回指针（Back Pointer），供超时处理程序使用。

<a id="a28174f11134146a800588f5e32d4a147"></a>

### `deadline`

```c
k_timepoint_t dns_resolve_context::dns_pending_query::deadline
```

查询截止时间（Query Deadline），用于保证服务器回退处理不超出最初的超时范围。

<a id="a8810792264f30d55b03d53a775bc68fa"></a>

### `failed`

```c
atomic_t dns_resolve_context::dns_pending_query::failed
```

记录本次查询已失败服务器的位集合（Bitset）。

<a id="a773e2ad2bedb2d1030df3590e9a14173"></a>

### `id`

```c
uint16_t dns_resolve_context::dns_pending_query::id
```

本次查询的DNS标识（DNS ID）。

<a id="a8473953176dd2310fb4cfe28fb04948d"></a>

### `last_status`

```c
enum dns_resolve_status dns_resolve_context::dns_pending_query::last_status
```

已尝试服务器最近报告的终止状态（Terminal Status）。

<a id="a1dccc8f927ba987da56c5d704ab67e1a"></a>

### `orig_query_hash`

```c
uint16_t dns_resolve_context::dns_pending_query::orig_query_hash
```

调用方请求的原始DNS名称与查询类型组合的哈希（Hash）。

与query_hash不同，即使查询沿CNAME别名继续进行，该值也保持不变。

<a id="aa2f4ee968b610ba74cdd7880076e1508"></a>

### `pending`

```c
atomic_t dns_resolve_context::dns_pending_query::pending
```

记录当前等待应答服务器的位集合（Bitset）。

<a id="a106464bda8d56283b06251c37964906b"></a>

### `query`

```c
const char* dns_resolve_context::dns_pending_query::query
```

包含待解析对象的字符串，例如www.example.com。

查询开始时将此项设为非空值，之后不再使用。

如果查询完成时工作项（Work Item）仍在等待执行，则清除此指针以表示查询完成；但会延迟释放查询槽位，直到某次槽位请求确认工作项已被释放。

<a id="a168fea99e8c6760cab49611ceb5a6fc1"></a>

### `query_hash`

```c
uint16_t dns_resolve_context::dns_pending_query::query_hash
```

正在查询的DNS名称与查询类型组合的哈希（Hash）。

计算此哈希（Hash）是为了匹配正在接收的响应。这主要用于mDNS，因为mDNS将DNS标识设为0，无法仅凭标识找到正确的待处理查询。

<a id="af5796eb469e2fe3bcebea2ad55a8fd78"></a>

### `query_type`

```c
enum dns_query_type dns_resolve_context::dns_pending_query::query_type
```

查询类型（Query Type）。

<a id="a5402d71d11a3ef006703a1a8e6cc7651"></a>

### `sent`

```c
atomic_t dns_resolve_context::dns_pending_query::sent
```

记录已查询服务器的位集合（Bitset）。

<a id="ad3fb3c0f90eba5506a1152ae1bb7d6ab"></a>

### `[struct]`

```c
struct { ... } dns_resolve_context::dns_pending_query::servers
```

已配置DNS服务器的逐查询状态（Per-Query State）。

<a id="a6f76b200b8c421399987be83b72b9230"></a>

### `timer`

```c
struct k_work_delayable dns_resolve_context::dns_pending_query::timer
```

超时定时器（Timeout Timer）。

<a id="a6a1c93f3eab8f9aa55dbb26e704bb343"></a>

### `user_data`

```c
void* dns_resolve_context::dns_pending_query::user_data
```

用户数据（User Data）。

本数据类型文档由以下文件生成：

- `zephyr/net/dns_resolve.h`

## 20.3\_原页交叉引用（Cross References）

- [zephyr/net/dns_resolve.h](https://docs.zephyrproject.org/latest/doxygen/html/dns__resolve_8h_source.html)
- [k_work_delayable](https://docs.zephyrproject.org/latest/doxygen/html/structk__work__delayable.html)
- [dns_resolve_context](P019_dns_resolve_context_结构体.md)
- [dns_resolve_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gafe22d0ef90c581982561ef0c33d1f722)
- [dns_query_type](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga7169c5a920fb1b0d77910a6ab922e3f0)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [k_timepoint_t](../timer_reference/P088_内核时间点类型.md)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [dns_resolve_status](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga5baf1fea0482fb3a940b4f5350a3c58e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P019_dns_resolve_context_结构体.md) · [返回大纲](大纲.md) · [下一章](P021_dns_resolve_context__dns_server_info_结构体.md)
