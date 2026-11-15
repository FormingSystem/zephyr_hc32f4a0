---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-6
title: bt_mesh_blob_cli_inputs_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__cli__inputs.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_bt\_mesh\_blob\_cli\_inputs\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__cli__inputs.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BLOB传输客户端（BLOB Transfer Client）的传输输入。

```c
#include <zephyr/bluetooth/mesh/blob_cli.h>
```

<a id="details"></a>

BLOB传输客户端（BLOB Transfer Client）的传输输入。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 6.1\_数据成员（Data Fields）

<a id="r_a835a539b307c659f57da6c20e9223ed1"></a>

```c
sys_slist_t targets
```

相关声明：[sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)、[targets](#a835a539b307c659f57da6c20e9223ed1)。

目标节点链表（Linked list of Target nodes）。

<a id="r_a7fb308f895c57b66b50e1ab060228cb3"></a>

```c
uint16_t app_idx
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[app_idx](#a7fb308f895c57b66b50e1ab060228cb3)。

发送时使用的应用密钥索引（AppKey index）。

<a id="r_ac204e179c2a6ea9cb672fc3c2f9ab017"></a>

```c
uint16_t group
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[group](#ac204e179c2a6ea9cb672fc3c2f9ab017)。

二进制大对象传输（BLOB transfer）的目的组地址（Group address）；若为 `BT_MESH_ADDR_UNASSIGNED`，则向每个目标节点分别发送每条消息。

<a id="r_adee5ecdba3adc4fe598483b1a160cafb"></a>

```c
uint8_t ttl
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ttl](#adee5ecdba3adc4fe598483b1a160cafb)。

二进制大对象传输消息的生存时间（Time to live，TTL）值。

<a id="r_a30fd3cd7a6df07f6aa90b85cdc6aea18"></a>

```c
uint16_t timeout_base
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[timeout_base](#a30fd3cd7a6df07f6aa90b85cdc6aea18)。

目标节点的额外响应时间（Additional response time），以 10 秒为增量。

## 6.2\_详细说明（Detailed Documentation）

<a id="a7fb308f895c57b66b50e1ab060228cb3"></a>

### `app_idx`

```c
uint16_t bt_mesh_blob_cli_inputs::app_idx
```

发送时使用的应用密钥索引（AppKey index）。

<a id="ac204e179c2a6ea9cb672fc3c2f9ab017"></a>

### `group`

```c
uint16_t bt_mesh_blob_cli_inputs::group
```

二进制大对象传输（BLOB transfer）的目的组地址（Group address）；若为 `BT_MESH_ADDR_UNASSIGNED`，则向每个目标节点分别发送每条消息。

<a id="a835a539b307c659f57da6c20e9223ed1"></a>

### `targets`

```c
sys_slist_t bt_mesh_blob_cli_inputs::targets
```

目标节点链表（Linked list of Target nodes）。

每个节点应指向 `bt_mesh_blob_target::n`。

<a id="a30fd3cd7a6df07f6aa90b85cdc6aea18"></a>

### `timeout_base`

```c
uint16_t bt_mesh_blob_cli_inputs::timeout_base
```

目标节点的额外响应时间（Additional response time），以 10 秒为增量。

额外时间可用于给目标节点（Target nodes）更多时间响应客户端（Client）的消息。实际超时值按以下公式计算：

原始示例（Example）：

```c
*  timeout = 20 seconds + (10 seconds * timeout_base) + (100 ms * TTL)
*
```

如果目标节点（Target node）未能在配置的传输超时内响应客户端（Client）的消息，则将其移出本次传输。

<a id="adee5ecdba3adc4fe598483b1a160cafb"></a>

### `ttl`

```c
uint8_t bt_mesh_blob_cli_inputs::ttl
```

二进制大对象传输消息的生存时间（Time to live，TTL）值。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/blob_cli.h`

## 6.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/blob_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/blob__cli_8h_source.html)
- [sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [BT_MESH_ADDR_UNASSIGNED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga6d11790af686e6d48f08c6f1cd65317c)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_mesh_blob_target::n](P012_bt_mesh_blob_target_结构体.md#aca0f3cabb5c457cfb11a4bc71c3bea85)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P005_bt_mesh_blob_cli_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P007_bt_mesh_blob_io_结构体.md)
