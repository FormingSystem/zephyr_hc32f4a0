---
id: learning.zephyr-docs.network-core-model-reference.page-110
title: net_mgmt_event_callback_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__mgmt__event__callback.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第110章\_net\_mgmt\_event\_callback\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__mgmt__event__callback.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络管理事件回调（Network Management Event Callback）结构；用于向网络管理事件部分注册回调，使该结构的所有者能够根据给定事件掩码接收网络事件通知。

```c
#include <zephyr/net/net_mgmt.h>
```

<a id="details"></a>

网络管理事件回调（Network Management Event Callback）结构；用于向网络管理事件部分注册回调，使该结构的所有者能够根据给定事件掩码接收网络事件通知。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 110.1\_数据成员（Data Fields）

<a id="r_a05a4f445731f9f72209a652f2653e1ea"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#a05a4f445731f9f72209a652f2653e1ea)。

供内部使用，用于将回调插入链表（List）。

```c
union {
```

<a id="r_a87f0cb8be96be6688c9c88e187ac2234"></a>

```c
net_mgmt_event_handler_t handler
```

相关声明：[net_mgmt_event_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga2e83a5a769ac52c846f255e23aea84d2)、[handler](#ada57aabc8acc3e9be93fb2726321f1b2)。

实际用于通知所有者（Owner）的回调函数（Callback function）。

<a id="r_a6a371db01e85d93b3a7b1eac6631f508"></a>

```c
struct k_sem * sync_call
```

相关声明：[k_sem](../synchronization_reference/P009_内核信号量结构.md)、[sync_call](#a7403d98fe528c492a4b1b449b43c10d3)。

供同步 `net_mgmt_event_wait()` 函数内部使用的信号量（Semaphore）。

<a id="r_a0306812b62c4176ef0fafbc4f89d5f07"></a>

```c
};
```

```c
union {
```

<a id="r_a6ab10af1cd8812a61757db68fd7f426f"></a>

```c
uint64_t event_mask
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[event_mask](#a99e3174c1052488877b3db6349de61e8)。

网络事件掩码（Network event mask）：掩码指定的事件发生时，应调用上述处理函数（Handler）。

<a id="r_ae3c6f3d34372e42ac8066409a44aa35f"></a>

```c
uint64_t raised_event
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[raised_event](#a555d868d6a0d6ecb04d09607fab06b79)。

当同步事件等待（Synchronous event wait）因某个事件成功解除阻塞时使用的内部占位字段（Internal place holder）。

<a id="r_a729c499ebef52b08828ab0cfe939135e"></a>

```c
};
```

网络事件掩码（Network event mask）：掩码指定的事件发生时，应调用上述处理函数（Handler）。

## 110.2\_详细说明（Detailed Documentation）

<a id="a729c499ebef52b08828ab0cfe939135e"></a>

### `[union]`

```c
union { ... } net_mgmt_event_callback
```

网络事件掩码（Network event mask）：掩码指定的事件发生时，应调用上述处理函数（Handler）。

所有者可在需要时修改此掩码（Mask），从而决定是否调用处理函数（Handler）。

<a id="a0306812b62c4176ef0fafbc4f89d5f07"></a>

### `[union]`

```c
union { ... } net_mgmt_event_callback
```

<a id="a99e3174c1052488877b3db6349de61e8"></a>

### `event_mask`

```c
uint64_t net_mgmt_event_callback::event_mask
```

网络事件掩码（Network event mask）：掩码指定的事件发生时，应调用上述处理函数（Handler）。

注意，只有命令部分（Command part）被视为掩码，可匹配一个或多个命令。层（Layer）和层代码（Layer code）采用精确匹配。因此，要接收来自多个层的事件，必须注册多个监听器（Listeners），每个待监听的层各注册一个。

<a id="ada57aabc8acc3e9be93fb2726321f1b2"></a>

### `handler`

```c
net_mgmt_event_handler_t net_mgmt_event_callback::handler
```

实际用于通知所有者（Owner）的回调函数（Callback function）。

<a id="a05a4f445731f9f72209a652f2653e1ea"></a>

### `node`

```c
sys_snode_t net_mgmt_event_callback::node
```

供内部使用，用于将回调插入链表（List）。

因此，任何外部代码都不应修改它。

<a id="a555d868d6a0d6ecb04d09607fab06b79"></a>

### `raised_event`

```c
uint64_t net_mgmt_event_callback::raised_event
```

当同步事件等待（Synchronous event wait）因某个事件成功解除阻塞时使用的内部占位字段（Internal place holder）。

<a id="a7403d98fe528c492a4b1b449b43c10d3"></a>

### `sync_call`

```c
struct k_sem* net_mgmt_event_callback::sync_call
```

供同步 `net_mgmt_event_wait()` 函数内部使用的信号量（Semaphore）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_mgmt.h`

## 110.3\_原页交叉引用（Cross References）

- [zephyr/net/net_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h_source.html)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [net_mgmt_event_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga2e83a5a769ac52c846f255e23aea84d2)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [net_mgmt_event_wait()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga7137c77c55ee2609941c88db79e22d1a)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [net_mgmt_event_callback](P110_net_mgmt_event_callback_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P109_net_lldpdu_结构体.md) · [返回大纲](大纲.md) · [下一章](P111_net_mgmt_msghdr_结构体.md)
