---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-93
title: bt_mesh_rpr_node_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__rpr__node.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第93章\_bt\_mesh\_rpr\_node\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__rpr__node.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

从整个Mesh网络角度看到的远程配网参与者（Remote Provisioning Actor）。

```c
#include <zephyr/bluetooth/mesh/rpr.h>
```

<a id="details"></a>

从整个Mesh网络角度看到的远程配网参与者（Remote Provisioning Actor）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 93.1\_数据成员（Data Fields）

<a id="r_a10ec7b9c480513e742566c6c3b9c4973"></a>

```c
uint16_t addr
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[addr](#a10ec7b9c480513e742566c6c3b9c4973)。

节点的单播地址（Unicast address）。

<a id="r_a2197a70aa97209a60136a09da1f513b2"></a>

```c
uint16_t net_idx
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[net_idx](#a2197a70aa97209a60136a09da1f513b2)。

与该节点通信所用的网络索引（Network index）。

<a id="r_a4a73478764d4d15642475b8a822130af"></a>

```c
uint8_t ttl
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ttl](#a4a73478764d4d15642475b8a822130af)。

与该节点通信所用的生存时间值（Time To Live，TTL）。

## 93.2\_详细说明（Detailed Documentation）

<a id="a10ec7b9c480513e742566c6c3b9c4973"></a>

### `addr`

```c
uint16_t bt_mesh_rpr_node::addr
```

节点的单播地址（Unicast address）。

<a id="a2197a70aa97209a60136a09da1f513b2"></a>

### `net_idx`

```c
uint16_t bt_mesh_rpr_node::net_idx
```

与该节点通信所用的网络索引（Network index）。

<a id="a4a73478764d4d15642475b8a822130af"></a>

### `ttl`

```c
uint8_t bt_mesh_rpr_node::ttl
```

与该节点通信所用的生存时间值（Time To Live，TTL）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/rpr.h`

## 93.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/rpr.h](https://docs.zephyrproject.org/latest/doxygen/html/rpr_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P092_bt_mesh_rpr_link_结构体.md) · [返回大纲](大纲.md) · [下一章](P094_bt_mesh_rpr_scan_status_结构体.md)
