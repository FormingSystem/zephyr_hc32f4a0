---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-87
title: bt_mesh_priv_node_id_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__priv__node__id.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第87章\_bt\_mesh\_priv\_node\_id\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__priv__node__id.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

私有节点标识（Private Node Identity）。

```c
#include <zephyr/bluetooth/mesh/priv_beacon_cli.h>
```

<a id="details"></a>

私有节点标识（Private Node Identity）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 87.1\_数据成员（Data Fields）

<a id="r_ab772f79daa361a9199f8445b7bda7e44"></a>

```c
uint16_t net_idx
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[net_idx](#ab772f79daa361a9199f8445b7bda7e44)。

网络密钥索引（NetKey index）。

<a id="r_a5bd318e61b974a94765e0d28db15994f"></a>

```c
uint8_t state
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[state](#a5bd318e61b974a94765e0d28db15994f)。

私有节点身份状态（Private Node Identity state）。

<a id="r_a49c60fedb24de61a399f3da967f4ac7c"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a49c60fedb24de61a399f3da967f4ac7c)。

响应状态码（Response status code）。

## 87.2\_详细说明（Detailed Documentation）

<a id="ab772f79daa361a9199f8445b7bda7e44"></a>

### `net_idx`

```c
uint16_t bt_mesh_priv_node_id::net_idx
```

网络密钥索引（NetKey index）。

<a id="a5bd318e61b974a94765e0d28db15994f"></a>

### `state`

```c
uint8_t bt_mesh_priv_node_id::state
```

私有节点身份状态（Private Node Identity state）。

<a id="a49c60fedb24de61a399f3da967f4ac7c"></a>

### `status`

```c
uint8_t bt_mesh_priv_node_id::status
```

响应状态码（Response status code）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/priv_beacon_cli.h`

## 87.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/priv_beacon_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/priv__beacon__cli_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P086_bt_mesh_priv_beacon_cli_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P088_bt_mesh_prov_结构体.md)
