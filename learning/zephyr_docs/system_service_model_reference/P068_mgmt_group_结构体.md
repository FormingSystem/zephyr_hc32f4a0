---
id: learning.zephyr-docs.system-service-model-reference.page-68
title: mgmt_group_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmgmt__group.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第68章\_mgmt\_group\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmgmt__group.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

整个命令组（Command Group）的处理程序集合。

```c
#include <zephyr/mgmt/mcumgr/mgmt/mgmt.h>
```

<a id="details"></a>

整个命令组（Command Group）的处理程序集合。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 68.1\_数据成员（Data Fields）

<a id="r_ac150809b03f73c4c2f94742504af772c"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#ac150809b03f73c4c2f94742504af772c)。

条目列表节点（Entry list node）。

<a id="r_a7a6e90e500716095b9a22e3f56edac03"></a>

```c
const struct mgmt_handler * mg_handlers
```

相关声明：[mgmt_handler](P069_mgmt_handler_结构体.md)、[mg_handlers](#a7a6e90e500716095b9a22e3f56edac03)。

处理函数数组，每个命令 ID 对应一个条目。

<a id="r_a8b2de48e97c0de4c902d72aba4e920b4"></a>

```c
uint16_t mg_handlers_count
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[mg_handlers_count](#a8b2de48e97c0de4c902d72aba4e920b4)。

<a id="r_a9d55dbf947096eed7cacfb9087d304d4"></a>

```c
uint16_t mg_group_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[mg_group_id](#a9d55dbf947096eed7cacfb9087d304d4)。

此组的数值 ID。

## 68.2\_详细说明（Detailed Documentation）

<a id="a9d55dbf947096eed7cacfb9087d304d4"></a>

### `mg_group_id`

```c
uint16_t mgmt_group::mg_group_id
```

此组的数值 ID。

<a id="a7a6e90e500716095b9a22e3f56edac03"></a>

### `mg_handlers`

```c
const struct mgmt_handler* mgmt_group::mg_handlers
```

处理函数数组，每个命令 ID 对应一个条目。

<a id="a8b2de48e97c0de4c902d72aba4e920b4"></a>

### `mg_handlers_count`

```c
uint16_t mgmt_group::mg_handlers_count
```

<a id="ac150809b03f73c4c2f94742504af772c"></a>

### `node`

```c
sys_snode_t mgmt_group::node
```

条目列表节点（Entry list node）。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/mgmt/mgmt.h`

## 68.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/mcumgr/mgmt/mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_8h_source.html)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [mgmt_handler](P069_mgmt_handler_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P067_mgmt_evt_op_cmd_arg_结构体.md) · [返回大纲](大纲.md) · [下一章](P069_mgmt_handler_结构体.md)
