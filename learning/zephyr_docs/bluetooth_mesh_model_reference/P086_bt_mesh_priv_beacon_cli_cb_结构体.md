---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-86
title: bt_mesh_priv_beacon_cli_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__priv__beacon__cli__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第86章\_bt\_mesh\_priv\_beacon\_cli\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__priv__beacon__cli__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

私有信标客户端（Private Beacon Client）状态消息的回调。

```c
#include <zephyr/bluetooth/mesh/priv_beacon_cli.h>
```

<a id="details"></a>

私有信标客户端（Private Beacon Client）状态消息的回调。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 86.1\_数据成员（Data Fields）

<a id="r_ab4b58af5af27be22dc395df4b2fd35c4"></a>

```c
void(* priv_beacon_status )(struct bt_mesh_priv_beacon_cli *cli, uint16_t addr, struct bt_mesh_priv_beacon *priv_beacon)
```

相关声明：[priv_beacon_status](#ab4b58af5af27be22dc395df4b2fd35c4)、[bt_mesh_priv_beacon_cli](P085_bt_mesh_priv_beacon_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_priv_beacon](P084_bt_mesh_priv_beacon_结构体.md)。

私有信标状态消息（Private Beacon Status）的可选回调。

<a id="r_a825bb5dee44075a8b6d14efc5f68c372"></a>

```c
void(* priv_gatt_proxy_status )(struct bt_mesh_priv_beacon_cli *cli, uint16_t addr, uint8_t gatt_proxy)
```

相关声明：[priv_gatt_proxy_status](#a825bb5dee44075a8b6d14efc5f68c372)、[bt_mesh_priv_beacon_cli](P085_bt_mesh_priv_beacon_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

私有通用属性代理状态消息（Private GATT Proxy Status）的可选回调。

<a id="r_aa1206f9a75beb79449e5a1bad8e62f41"></a>

```c
void(* priv_node_id_status )(struct bt_mesh_priv_beacon_cli *cli, uint16_t addr, struct bt_mesh_priv_node_id *priv_node_id)
```

相关声明：[priv_node_id_status](#aa1206f9a75beb79449e5a1bad8e62f41)、[bt_mesh_priv_beacon_cli](P085_bt_mesh_priv_beacon_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_priv_node_id](P087_bt_mesh_priv_node_id_结构体.md)。

私有节点身份状态消息（Private Node Identity Status）的可选回调。

## 86.2\_详细说明（Detailed Documentation）

<a id="ab4b58af5af27be22dc395df4b2fd35c4"></a>

### `priv_beacon_status`

```c
void(* bt_mesh_priv_beacon_cli_cb::priv_beacon_status) (struct bt_mesh_priv_beacon_cli *cli, uint16_t addr, struct bt_mesh_priv_beacon *priv_beacon)
```

私有信标状态消息（Private Beacon Status）的可选回调。

处理从私有信标服务器（Private Beacon server）收到的私有信标状态消息（Private Beacon Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 私有信标客户端上下文（Private Beacon client context）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `priv_beacon` | 从服务器收到的 Mesh 私有信标状态（Mesh Private Beacon state）。 |

<a id="a825bb5dee44075a8b6d14efc5f68c372"></a>

### `priv_gatt_proxy_status`

```c
void(* bt_mesh_priv_beacon_cli_cb::priv_gatt_proxy_status) (struct bt_mesh_priv_beacon_cli *cli, uint16_t addr, uint8_t gatt_proxy)
```

私有通用属性代理状态消息（Private GATT Proxy Status）的可选回调。

处理从私有信标服务器（Private Beacon server）收到的私有通用属性代理状态消息（Private GATT Proxy Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 私有信标客户端上下文（Private Beacon client context）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `gatt_proxy` | 从服务器收到的私有通用属性代理状态（Private GATT Proxy state）。 |

<a id="aa1206f9a75beb79449e5a1bad8e62f41"></a>

### `priv_node_id_status`

```c
void(* bt_mesh_priv_beacon_cli_cb::priv_node_id_status) (struct bt_mesh_priv_beacon_cli *cli, uint16_t addr, struct bt_mesh_priv_node_id *priv_node_id)
```

私有节点身份状态消息（Private Node Identity Status）的可选回调。

处理从私有信标服务器（Private Beacon server）收到的私有节点身份状态消息（Private Node Identity Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 私有信标客户端上下文（Private Beacon client context）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `priv_node_id` | 从服务器收到的私有节点身份状态（Private Node Identity state）。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/priv_beacon_cli.h`

## 86.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/priv_beacon_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/priv__beacon__cli_8h_source.html)
- [bt_mesh_priv_beacon_cli](P085_bt_mesh_priv_beacon_cli_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_mesh_priv_beacon](P084_bt_mesh_priv_beacon_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_mesh_priv_node_id](P087_bt_mesh_priv_node_id_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P085_bt_mesh_priv_beacon_cli_结构体.md) · [返回大纲](大纲.md) · [下一章](P087_bt_mesh_priv_node_id_结构体.md)
