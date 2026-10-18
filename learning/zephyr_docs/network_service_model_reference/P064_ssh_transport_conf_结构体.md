---
id: learning.zephyr-docs.network-service-model-reference.page-64
title: ssh_transport_conf_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structssh__transport__conf.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第64章\_ssh\_transport\_conf\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structssh__transport__conf.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SSH传输回调（Transport Callback）的配置。

```c
#include <zephyr/net/ssh/common.h>
```

<a id="details"></a>

SSH传输回调（Transport Callback）的配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 64.1\_数据成员（Data Fields）

<a id="r_a84db4c215eed55af55cf9a8d95a08599"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#a84db4c215eed55af55cf9a8d95a08599)。

列表节点（List Node）。

<a id="r_a769d50cabe9a88cc14df0cb47203fd32"></a>

```c
ssh_transport_event_callback_t cb
```

相关声明：[ssh_transport_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gaed450ebb53a676fafc58bb6cfe82a448)、[cb](#a769d50cabe9a88cc14df0cb47203fd32)。

由服务器调用的回调函数，用于取得客户端连接的传输对象。

<a id="r_a00639f5bd1d033d60279f32026293b33"></a>

```c
void * user_data
```

相关声明：[user_data](#a00639f5bd1d033d60279f32026293b33)。

传给回调函数的用户数据。

## 64.2\_详细说明（Detailed Documentation）

<a id="a769d50cabe9a88cc14df0cb47203fd32"></a>

### `cb`

```c
ssh_transport_event_callback_t ssh_transport_conf::cb
```

由服务器调用的回调函数，用于取得客户端连接的传输对象。

<a id="a84db4c215eed55af55cf9a8d95a08599"></a>

### `node`

```c
sys_snode_t ssh_transport_conf::node
```

列表节点（List Node）。

<a id="a00639f5bd1d033d60279f32026293b33"></a>

### `user_data`

```c
void* ssh_transport_conf::user_data
```

传给回调函数的用户数据。

本数据类型文档由以下文件生成：

- `zephyr/net/ssh/common.h`

## 64.3\_原页交叉引用（Cross References）

- [zephyr/net/ssh/common.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2net_2ssh_2common_8h_source.html)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [ssh_transport_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gaed450ebb53a676fafc58bb6cfe82a448)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P063_ssh_server_event_client_disconnected_结构体.md) · [返回大纲](大纲.md) · [下一章](P065_ssh_transport_event_结构体.md)
