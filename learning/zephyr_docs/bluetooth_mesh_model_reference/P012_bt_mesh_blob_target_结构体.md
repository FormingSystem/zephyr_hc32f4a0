---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-12
title: bt_mesh_blob_target_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__target.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_bt\_mesh\_blob\_target\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__target.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BLOB传输客户端（BLOB Transfer Client）的目标节点。

```c
#include <zephyr/bluetooth/mesh/blob_cli.h>
```

<a id="details"></a>

BLOB传输客户端（BLOB Transfer Client）的目标节点。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 12.1\_数据成员（Data Fields）

<a id="r_aca0f3cabb5c457cfb11a4bc71c3bea85"></a>

```c
sys_snode_t n
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[n](#aca0f3cabb5c457cfb11a4bc71c3bea85)。

链表节点（Linked list node）。

<a id="r_ab4c032f92a4ec12e4bbd6fa84139c085"></a>

```c
uint16_t addr
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[addr](#ab4c032f92a4ec12e4bbd6fa84139c085)。

目标节点地址（Target node address）。

<a id="r_a0498f23d640af4b006398d5482fbaa53"></a>

```c
struct bt_mesh_blob_target_pull * pull
```

相关声明：[bt_mesh_blob_target_pull](P013_bt_mesh_blob_target_pull_结构体.md)、[pull](#a0498f23d640af4b006398d5482fbaa53)。

目标节点的拉取模式上下文（Pull mode context）。

<a id="r_a62b5a5be44d52ebf09421de57933459d"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a62b5a5be44d52ebf09421de57933459d)。

二进制大对象传输状态（BLOB transfer status），参见 `bt_mesh_blob_status`。

<a id="r_a711a031e841bb54c4985d02a81c6846a"></a>

```c
uint8_t procedure_complete:1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[procedure_complete](#a711a031e841bb54c4985d02a81c6846a)。

<a id="r_a4eef4809023e8d4a4ee8beece5e83160"></a>

```c
uint8_t acked:1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[acked](#a4eef4809023e8d4a4ee8beece5e83160)。

<a id="r_a3e14f4518ee054754dfa50d8070c1725"></a>

```c
uint8_t timedout:1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[timedout](#a3e14f4518ee054754dfa50d8070c1725)。

<a id="r_a7aa1066dbeee5ba4a5be5aa14d61d4d1"></a>

```c
uint8_t skip:1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[skip](#a7aa1066dbeee5ba4a5be5aa14d61d4d1)。

## 12.2\_详细说明（Detailed Documentation）

<a id="a4eef4809023e8d4a4ee8beece5e83160"></a>

### `acked`

```c
uint8_t bt_mesh_blob_target::acked
```

<a id="ab4c032f92a4ec12e4bbd6fa84139c085"></a>

### `addr`

```c
uint16_t bt_mesh_blob_target::addr
```

目标节点地址（Target node address）。

<a id="aca0f3cabb5c457cfb11a4bc71c3bea85"></a>

### `n`

```c
sys_snode_t bt_mesh_blob_target::n
```

链表节点（Linked list node）。

<a id="a711a031e841bb54c4985d02a81c6846a"></a>

### `procedure_complete`

```c
uint8_t bt_mesh_blob_target::procedure_complete
```

<a id="a0498f23d640af4b006398d5482fbaa53"></a>

### `pull`

```c
struct bt_mesh_blob_target_pull* bt_mesh_blob_target::pull
```

目标节点的拉取模式上下文（Pull mode context）。

以拉取模式（Pull mode）发送二进制大对象（BLOB）时，需要初始化。

<a id="a7aa1066dbeee5ba4a5be5aa14d61d4d1"></a>

### `skip`

```c
uint8_t bt_mesh_blob_target::skip
```

<a id="a62b5a5be44d52ebf09421de57933459d"></a>

### `status`

```c
uint8_t bt_mesh_blob_target::status
```

二进制大对象传输状态（BLOB transfer status），参见 `bt_mesh_blob_status`。

<a id="a3e14f4518ee054754dfa50d8070c1725"></a>

### `timedout`

```c
uint8_t bt_mesh_blob_target::timedout
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/blob_cli.h`

## 12.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/blob_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/blob__cli_8h_source.html)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_mesh_blob_target_pull](P013_bt_mesh_blob_target_pull_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_mesh_blob_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga7b5e2895a6577103a8a680a94ee7776d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P011_bt_mesh_blob_srv_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P013_bt_mesh_blob_target_pull_结构体.md)
