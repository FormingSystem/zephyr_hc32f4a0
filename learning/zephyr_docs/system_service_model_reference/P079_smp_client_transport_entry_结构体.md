---
id: learning.zephyr-docs.system-service-model-reference.page-79
title: smp_client_transport_entry_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsmp__client__transport__entry.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第79章\_smp\_client\_transport\_entry\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsmp__client__transport__entry.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

简单管理协议（SMP）的客户端传输结构。

```c
#include <zephyr/mgmt/mcumgr/transport/smp.h>
```

<a id="details"></a>

简单管理协议（SMP）的客户端传输结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 79.1\_数据成员（Data Fields）

<a id="r_ad8ebd9f6bc7d322c51e6aecb2e926022"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#ad8ebd9f6bc7d322c51e6aecb2e926022)。

<a id="r_aebf774d7d0fe4eebe2e230a3680e0acf"></a>

```c
struct smp_transport * smpt
```

相关声明：[smp_transport](P081_smp_transport_结构体.md)、[smpt](#aebf774d7d0fe4eebe2e230a3680e0acf)。

传输结构体指针。

<a id="r_a6a8a368d3db1f03b4e6774d4a86123c2"></a>

```c
int smpt_type
```

相关声明：[smpt_type](#a6a8a368d3db1f03b4e6774d4a86123c2)。

传输类型（Transport type）。

<a id="r_a83e2e2851f48a8c13e296b3b1ce1d209"></a>

```c
char * name
```

相关声明：[name](#a83e2e2851f48a8c13e296b3b1ce1d209)。

传输名称，用于传输管理；设为 `NULL` 可省略。

## 79.2\_详细说明（Detailed Documentation）

<a id="a83e2e2851f48a8c13e296b3b1ce1d209"></a>

### `name`

```c
char* smp_client_transport_entry::name
```

传输名称，用于传输管理；设为 `NULL` 可省略。

<a id="ad8ebd9f6bc7d322c51e6aecb2e926022"></a>

### `node`

```c
sys_snode_t smp_client_transport_entry::node
```

<a id="aebf774d7d0fe4eebe2e230a3680e0acf"></a>

### `smpt`

```c
struct smp_transport* smp_client_transport_entry::smpt
```

传输结构体指针。

<a id="a6a8a368d3db1f03b4e6774d4a86123c2"></a>

### `smpt_type`

```c
int smp_client_transport_entry::smpt_type
```

传输类型（Transport type）。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/transport/smp.h`

## 79.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/mcumgr/transport/smp.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2transport_2smp_8h_source.html)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [smp_transport](P081_smp_transport_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P078_smp_client_object_结构体.md) · [返回大纲](大纲.md) · [下一章](P080_smp_streamer_结构体.md)
