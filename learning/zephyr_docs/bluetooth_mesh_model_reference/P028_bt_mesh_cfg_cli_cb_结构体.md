---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-28
title: bt_mesh_cfg_cli_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__cfg__cli__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_bt\_mesh\_cfg\_cli\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__cfg__cli__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Mesh配置客户端（Configuration Client）状态消息的回调。

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

<a id="details"></a>

Mesh配置客户端（Configuration Client）状态消息的回调。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 28.1\_数据成员（Data Fields）

<a id="r_aaae4e3f64e2033a466ad87d362ceb318"></a>

```c
void(* comp_data )(struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t page, struct net_buf_simple *buf)
```

相关声明：[comp_data](#aaae4e3f64e2033a466ad87d362ceb318)、[bt_mesh_cfg_cli](P027_bt_mesh_cfg_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

组成数据消息（Composition data）的可选回调。

<a id="r_ab4130e909826aa7746092f49f8b4c52e"></a>

```c
void(* mod_pub_status )(struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status, uint16_t elem_addr, uint16_t mod_id, uint16_t cid, struct bt_mesh_cfg_cli_mod_pub *pub)
```

相关声明：[mod_pub_status](#ab4130e909826aa7746092f49f8b4c52e)、[bt_mesh_cfg_cli](P027_bt_mesh_cfg_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_cfg_cli_mod_pub](P031_bt_mesh_cfg_cli_mod_pub_结构体.md)。

模型发布状态消息（Model Pub Status）的可选回调。

<a id="r_af4a43f4c65d111e95211b715048534cc"></a>

```c
void(* mod_sub_status )(struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status, uint16_t elem_addr, uint16_t sub_addr, uint32_t mod_id)
```

相关声明：[mod_sub_status](#af4a43f4c65d111e95211b715048534cc)、[bt_mesh_cfg_cli](P027_bt_mesh_cfg_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

模型订阅状态消息（Model Sub Status）的可选回调。

<a id="r_a0ad46d1d4793577679f66c62175e14cf"></a>

```c
void(* mod_sub_list )(struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status, uint16_t elem_addr, uint16_t mod_id, uint16_t cid, struct net_buf_simple *buf)
```

相关声明：[mod_sub_list](#a0ad46d1d4793577679f66c62175e14cf)、[bt_mesh_cfg_cli](P027_bt_mesh_cfg_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

模型订阅列表消息（Model Sub List）的可选回调。

<a id="r_acf88660364760442dfab5280ae735d2d"></a>

```c
void(* node_reset_status )(struct bt_mesh_cfg_cli *cli, uint16_t addr)
```

相关声明：[node_reset_status](#acf88660364760442dfab5280ae735d2d)、[bt_mesh_cfg_cli](P027_bt_mesh_cfg_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

节点重置状态消息（Node Reset Status）的可选回调。

<a id="r_a5cf2c17a88c53c514fcaa73a6fd81b67"></a>

```c
void(* beacon_status )(struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status)
```

相关声明：[beacon_status](#a5cf2c17a88c53c514fcaa73a6fd81b67)、[bt_mesh_cfg_cli](P027_bt_mesh_cfg_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

信标状态消息（Beacon Status）的可选回调。

<a id="r_ab937311c41af68b1cd52a8a1c86145b1"></a>

```c
void(* ttl_status )(struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status)
```

相关声明：[ttl_status](#ab937311c41af68b1cd52a8a1c86145b1)、[bt_mesh_cfg_cli](P027_bt_mesh_cfg_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

默认生存时间状态消息（Default TTL Status）的可选回调。

<a id="r_a9487a159a6c838a9218b3d76fa53248d"></a>

```c
void(* friend_status )(struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status)
```

相关声明：[friend_status](#a9487a159a6c838a9218b3d76fa53248d)、[bt_mesh_cfg_cli](P027_bt_mesh_cfg_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

友谊节点状态消息（Friend Status）的可选回调。

<a id="r_a6ef3730e9469bffd81cdd49c50cac7d5"></a>

```c
void(* gatt_proxy_status )(struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status)
```

相关声明：[gatt_proxy_status](#a6ef3730e9469bffd81cdd49c50cac7d5)、[bt_mesh_cfg_cli](P027_bt_mesh_cfg_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通用属性代理状态消息（GATT Proxy Status）的可选回调。

<a id="r_ad46ea40b75cc1d5d314fdefdca0076f8"></a>

```c
void(* network_transmit_status )(struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status)
```

相关声明：[network_transmit_status](#ad46ea40b75cc1d5d314fdefdca0076f8)、[bt_mesh_cfg_cli](P027_bt_mesh_cfg_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

网络传输状态消息（Network Transmit Status）的可选回调。

<a id="r_a89eab453e00662f6f3f8a5d78f20d120"></a>

```c
void(* relay_status )(struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status, uint8_t transmit)
```

相关声明：[relay_status](#a89eab453e00662f6f3f8a5d78f20d120)、[bt_mesh_cfg_cli](P027_bt_mesh_cfg_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

中继状态消息（Relay Status）的可选回调。

<a id="r_a49a7a8cab34bb70d2edd87b0017f1cf7"></a>

```c
void(* net_key_status )(struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status, uint16_t net_idx)
```

相关声明：[net_key_status](#a49a7a8cab34bb70d2edd87b0017f1cf7)、[bt_mesh_cfg_cli](P027_bt_mesh_cfg_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

网络密钥状态消息（NetKey Status）的可选回调。

<a id="r_acce08dfa5cb356a2203f0ef6c4e4bf5b"></a>

```c
void(* net_key_list )(struct bt_mesh_cfg_cli *cli, uint16_t addr, struct net_buf_simple *buf)
```

相关声明：[net_key_list](#acce08dfa5cb356a2203f0ef6c4e4bf5b)、[bt_mesh_cfg_cli](P027_bt_mesh_cfg_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

网络密钥列表消息（NetKey List）的可选回调。

<a id="r_a48ef4d0665d86d069b90533eb18e0fd0"></a>

```c
void(* app_key_status )(struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status, uint16_t net_idx, uint16_t app_idx)
```

相关声明：[app_key_status](#a48ef4d0665d86d069b90533eb18e0fd0)、[bt_mesh_cfg_cli](P027_bt_mesh_cfg_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

应用密钥状态消息（AppKey Status）的可选回调。

<a id="r_ac331fc103d0f331093929f39e5b9d6ba"></a>

```c
void(* app_key_list )(struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status, uint16_t net_idx, struct net_buf_simple *buf)
```

相关声明：[app_key_list](#ac331fc103d0f331093929f39e5b9d6ba)、[bt_mesh_cfg_cli](P027_bt_mesh_cfg_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

应用密钥列表消息（AppKey List）的可选回调。

<a id="r_a3ccff69f21e0f3c585b951eb60c1bf5c"></a>

```c
void(* mod_app_status )(struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status, uint16_t elem_addr, uint16_t app_idx, uint32_t mod_id)
```

相关声明：[mod_app_status](#a3ccff69f21e0f3c585b951eb60c1bf5c)、[bt_mesh_cfg_cli](P027_bt_mesh_cfg_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

模型应用密钥状态消息（Model App Status）的可选回调。

<a id="r_abf8501e73f44ab5ea7e54b8f2ff1f866"></a>

```c
void(* mod_app_list )(struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status, uint16_t elem_addr, uint16_t mod_id, uint16_t cid, struct net_buf_simple *buf)
```

相关声明：[mod_app_list](#abf8501e73f44ab5ea7e54b8f2ff1f866)、[bt_mesh_cfg_cli](P027_bt_mesh_cfg_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

模型应用密钥列表消息（Model App List）的可选回调。

<a id="r_aca2d779401fa4521813e6578bd3bbd91"></a>

```c
void(* node_identity_status )(struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status, uint16_t net_idx, uint8_t identity)
```

相关声明：[node_identity_status](#aca2d779401fa4521813e6578bd3bbd91)、[bt_mesh_cfg_cli](P027_bt_mesh_cfg_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

节点身份状态消息（Node Identity Status）的可选回调。

<a id="r_a66b5a8dd3bdd2468fe65496020b13495"></a>

```c
void(* lpn_timeout_status )(struct bt_mesh_cfg_cli *cli, uint16_t addr, uint16_t elem_addr, uint32_t timeout)
```

相关声明：[lpn_timeout_status](#a66b5a8dd3bdd2468fe65496020b13495)、[bt_mesh_cfg_cli](P027_bt_mesh_cfg_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

低功耗节点轮询超时状态消息（LPN PollTimeout Status）的可选回调。

<a id="r_a4d89033676eb4570cdd80f1715fd9bfb"></a>

```c
void(* krp_status )(struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status, uint16_t net_idx, uint8_t phase)
```

相关声明：[krp_status](#a4d89033676eb4570cdd80f1715fd9bfb)、[bt_mesh_cfg_cli](P027_bt_mesh_cfg_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

密钥刷新阶段状态消息（Key Refresh Phase Status）的可选回调。

<a id="r_a615852027a841b1779a50c9fd50bef6a"></a>

```c
void(* hb_pub_status )(struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status, struct bt_mesh_cfg_cli_hb_pub *pub)
```

相关声明：[hb_pub_status](#a615852027a841b1779a50c9fd50bef6a)、[bt_mesh_cfg_cli](P027_bt_mesh_cfg_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_cfg_cli_hb_pub](P029_bt_mesh_cfg_cli_hb_pub_结构体.md)。

心跳发布状态消息（Heartbeat Pub Status）的可选回调。

<a id="r_aa60dfd72a43273e1ffae2160bcc0845d"></a>

```c
void(* hb_sub_status )(struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status, struct bt_mesh_cfg_cli_hb_sub *sub)
```

相关声明：[hb_sub_status](#aa60dfd72a43273e1ffae2160bcc0845d)、[bt_mesh_cfg_cli](P027_bt_mesh_cfg_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_cfg_cli_hb_sub](P030_bt_mesh_cfg_cli_hb_sub_结构体.md)。

心跳订阅状态消息（Heartbeat Sub Status）的可选回调。

## 28.2\_详细说明（Detailed Documentation）

<a id="ac331fc103d0f331093929f39e5b9d6ba"></a>

### `app_key_list`

```c
void(* bt_mesh_cfg_cli_cb::app_key_list) (struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status, uint16_t net_idx, struct net_buf_simple *buf)
```

应用密钥列表消息（AppKey List）的可选回调。

处理从服务器收到的应用密钥列表消息（AppKey List）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 接收到状态消息（Status message）的客户端（Client）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `status` | 消息的状态码（Status code）。 |
| `net_idx` | 网络密钥索引（NetKey index）。 |
| `buf` | 包含密钥索引（Key indexes）的消息缓冲区。 |

**说明（Note）**：注意（Note）：应使用辅助函数 `bt_mesh_key_idx_unpack_list` 解码 `buf` 参数。

<a id="a48ef4d0665d86d069b90533eb18e0fd0"></a>

### `app_key_status`

```c
void(* bt_mesh_cfg_cli_cb::app_key_status) (struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status, uint16_t net_idx, uint16_t app_idx)
```

应用密钥状态消息（AppKey Status）的可选回调。

处理从服务器收到的应用密钥状态消息（AppKey Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 接收到状态消息（Status message）的客户端（Client）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `status` | 请求消息的状态码（Status Code）。 |
| `net_idx` | 网络密钥索引（NetKey index）。 |
| `app_idx` | 应用密钥索引（AppKey index）。 |

<a id="a5cf2c17a88c53c514fcaa73a6fd81b67"></a>

### `beacon_status`

```c
void(* bt_mesh_cfg_cli_cb::beacon_status) (struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status)
```

信标状态消息（Beacon Status）的可选回调。

处理从服务器收到的信标状态消息（Beacon Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 接收到状态消息（Status message）的客户端（Client）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `status` | 请求消息的状态码（Status Code）。 |

<a id="aaae4e3f64e2033a466ad87d362ceb318"></a>

### `comp_data`

```c
void(* bt_mesh_cfg_cli_cb::comp_data) (struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t page, struct net_buf_simple *buf)
```

组成数据消息（Composition data）的可选回调。

处理从服务器收到的组成数据消息（Composition data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 接收到状态消息（Status message）的客户端（Client）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `page` | 组成数据页（Composition data page）。 |
| `buf` | 组成数据缓冲区（Composition data buffer）。 |

**说明（Note）**：注意（Note）：有关 `buf` 的解码，参见 `bt_mesh_comp_p0_get` 和 `bt_mesh_comp_p1_elem_pull`。

<a id="a9487a159a6c838a9218b3d76fa53248d"></a>

### `friend_status`

```c
void(* bt_mesh_cfg_cli_cb::friend_status) (struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status)
```

友谊节点状态消息（Friend Status）的可选回调。

处理从服务器收到的友谊节点状态消息（Friend Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 接收到状态消息（Status message）的客户端（Client）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `status` | 请求消息的状态码（Status Code）。 |

<a id="a6ef3730e9469bffd81cdd49c50cac7d5"></a>

### `gatt_proxy_status`

```c
void(* bt_mesh_cfg_cli_cb::gatt_proxy_status) (struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status)
```

通用属性代理状态消息（GATT Proxy Status）的可选回调。

处理从服务器收到的通用属性代理状态消息（GATT Proxy Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 接收到状态消息（Status message）的客户端（Client）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `status` | 请求消息的状态码（Status Code）。 |

<a id="a615852027a841b1779a50c9fd50bef6a"></a>

### `hb_pub_status`

```c
void(* bt_mesh_cfg_cli_cb::hb_pub_status) (struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status, struct bt_mesh_cfg_cli_hb_pub *pub)
```

心跳发布状态消息（Heartbeat Pub Status）的可选回调。

处理从服务器收到的心跳发布状态消息（Heartbeat Pub Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 接收到状态消息（Status message）的客户端（Client）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `status` | 消息的状态码（Status code）。 |
| `pub` | 心跳发布配置参数（HB publication configuration parameters）。 |

<a id="aa60dfd72a43273e1ffae2160bcc0845d"></a>

### `hb_sub_status`

```c
void(* bt_mesh_cfg_cli_cb::hb_sub_status) (struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status, struct bt_mesh_cfg_cli_hb_sub *sub)
```

心跳订阅状态消息（Heartbeat Sub Status）的可选回调。

处理从服务器收到的心跳订阅状态消息（Heartbeat Sub Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 接收到状态消息（Status message）的客户端（Client）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `status` | 消息的状态码（Status code）。 |
| `sub` | 心跳订阅配置参数（HB subscription configuration parameters）。 |

<a id="a4d89033676eb4570cdd80f1715fd9bfb"></a>

### `krp_status`

```c
void(* bt_mesh_cfg_cli_cb::krp_status) (struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status, uint16_t net_idx, uint8_t phase)
```

密钥刷新阶段状态消息（Key Refresh Phase Status）的可选回调。

处理从服务器收到的密钥刷新阶段状态消息（Key Refresh Phase Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 接收到状态消息（Status message）的客户端（Client）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `status` | 消息的状态码（Status code）。 |
| `net_idx` | 网络密钥索引（NetKey index）。 |
| `phase` | 密钥刷新过程的阶段（KRP phase）。 |

<a id="a66b5a8dd3bdd2468fe65496020b13495"></a>

### `lpn_timeout_status`

```c
void(* bt_mesh_cfg_cli_cb::lpn_timeout_status) (struct bt_mesh_cfg_cli *cli, uint16_t addr, uint16_t elem_addr, uint32_t timeout)
```

低功耗节点轮询超时状态消息（LPN PollTimeout Status）的可选回调。

处理从服务器收到的低功耗节点轮询超时状态消息（LPN PollTimeout Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 接收到状态消息（Status message）的客户端（Client）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `elem_addr` | 低功耗节点（LPN）的单播地址（Unicast address）。 |
| `timeout` | 低功耗节点（LPN）的轮询超时定时器（PollTimeout timer）当前值。 |

<a id="abf8501e73f44ab5ea7e54b8f2ff1f866"></a>

### `mod_app_list`

```c
void(* bt_mesh_cfg_cli_cb::mod_app_list) (struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status, uint16_t elem_addr, uint16_t mod_id, uint16_t cid, struct net_buf_simple *buf)
```

模型应用密钥列表消息（Model App List）的可选回调。

处理从服务器收到的模型应用密钥列表消息（Model App List）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 接收到状态消息（Status message）的客户端（Client）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `status` | 消息的状态码（Status code）。 |
| `elem_addr` | 元素地址（Element address）。 |
| `mod_id` | 模型标识符（Model ID）。 |
| `cid` | 公司标识符（Company ID）。 |
| `buf` | 包含密钥索引（Key indexes）的消息缓冲区。 |

**说明（Note）**：注意（Note）：应使用辅助函数 `bt_mesh_key_idx_unpack_list` 解码 `buf` 参数。

<a id="a3ccff69f21e0f3c585b951eb60c1bf5c"></a>

### `mod_app_status`

```c
void(* bt_mesh_cfg_cli_cb::mod_app_status) (struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status, uint16_t elem_addr, uint16_t app_idx, uint32_t mod_id)
```

模型应用密钥状态消息（Model App Status）的可选回调。

处理从服务器收到的模型应用密钥状态消息（Model App Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 接收到状态消息（Status message）的客户端（Client）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `status` | 请求消息的状态码（Status Code）。 |
| `elem_addr` | 元素的单播地址（Unicast address）。 |
| `app_idx` | 应用密钥索引（Application key index）。 |
| `mod_id` | 元素内的模型标识符（Model ID）。 |

<a id="ab4130e909826aa7746092f49f8b4c52e"></a>

### `mod_pub_status`

```c
void(* bt_mesh_cfg_cli_cb::mod_pub_status) (struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status, uint16_t elem_addr, uint16_t mod_id, uint16_t cid, struct bt_mesh_cfg_cli_mod_pub *pub)
```

模型发布状态消息（Model Pub Status）的可选回调。

处理从服务器收到的模型发布状态消息（Model Pub Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 接收到状态消息（Status message）的客户端（Client）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `status` | 消息的状态码（Status code）。 |
| `elem_addr` | 元素地址（Element address）。 |
| `mod_id` | 模型标识符（Model ID）。 |
| `cid` | 公司标识符（Company ID）。 |
| `pub` | 发布配置参数（Publication configuration parameters）。 |

<a id="a0ad46d1d4793577679f66c62175e14cf"></a>

### `mod_sub_list`

```c
void(* bt_mesh_cfg_cli_cb::mod_sub_list) (struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status, uint16_t elem_addr, uint16_t mod_id, uint16_t cid, struct net_buf_simple *buf)
```

模型订阅列表消息（Model Sub List）的可选回调。

处理从服务器收到的模型订阅列表消息（Model Sub List）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 接收到状态消息（Status message）的客户端（Client）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `status` | 消息的状态码（Status code）。 |
| `elem_addr` | 元素地址（Element address）。 |
| `mod_id` | 模型标识符（Model ID）。 |
| `cid` | 公司标识符（Company ID）。 |
| `buf` | 包含订阅地址（Subscription addresses）的消息缓冲区。 |

**说明（Note）**：注意（Note）：只要 `buf->len` 大于或等于 `2`，就应反复调用 `net_buf_simple_pull_le16` 解码 `buf` 参数。

<a id="af4a43f4c65d111e95211b715048534cc"></a>

### `mod_sub_status`

```c
void(* bt_mesh_cfg_cli_cb::mod_sub_status) (struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status, uint16_t elem_addr, uint16_t sub_addr, uint32_t mod_id)
```

模型订阅状态消息（Model Sub Status）的可选回调。

处理从服务器收到的模型订阅状态消息（Model Sub Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 接收到状态消息（Status message）的客户端（Client）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `status` | 请求消息的状态码（Status Code）。 |
| `elem_addr` | 元素的单播地址（Unicast address）。 |
| `sub_addr` | 订阅地址（Sub address）。 |
| `mod_id` | 元素内的模型标识符（Model ID）。 |

<a id="acce08dfa5cb356a2203f0ef6c4e4bf5b"></a>

### `net_key_list`

```c
void(* bt_mesh_cfg_cli_cb::net_key_list) (struct bt_mesh_cfg_cli *cli, uint16_t addr, struct net_buf_simple *buf)
```

网络密钥列表消息（NetKey List）的可选回调。

处理从服务器收到的网络密钥列表消息（NetKey List）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 接收到状态消息（Status message）的客户端（Client）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `buf` | 包含密钥索引（Key indexes）的消息缓冲区。 |

**说明（Note）**：注意（Note）：应使用辅助函数 `bt_mesh_key_idx_unpack_list` 解码 `buf` 参数。

<a id="a49a7a8cab34bb70d2edd87b0017f1cf7"></a>

### `net_key_status`

```c
void(* bt_mesh_cfg_cli_cb::net_key_status) (struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status, uint16_t net_idx)
```

网络密钥状态消息（NetKey Status）的可选回调。

处理从服务器收到的网络密钥状态消息（NetKey Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 接收到状态消息（Status message）的客户端（Client）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `status` | 请求消息的状态码（Status Code）。 |
| `net_idx` | 网络密钥索引（NetKey index）。 |

<a id="ad46ea40b75cc1d5d314fdefdca0076f8"></a>

### `network_transmit_status`

```c
void(* bt_mesh_cfg_cli_cb::network_transmit_status) (struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status)
```

网络传输状态消息（Network Transmit Status）的可选回调。

处理从服务器收到的网络传输状态消息（Network Transmit Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 接收到状态消息（Status message）的客户端（Client）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `status` | 请求消息的状态码（Status Code）。 |

<a id="aca2d779401fa4521813e6578bd3bbd91"></a>

### `node_identity_status`

```c
void(* bt_mesh_cfg_cli_cb::node_identity_status) (struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status, uint16_t net_idx, uint8_t identity)
```

节点身份状态消息（Node Identity Status）的可选回调。

处理从服务器收到的节点身份状态消息（Node Identity Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 接收到状态消息（Status message）的客户端（Client）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `status` | 请求消息的状态码（Status Code）。 |
| `net_idx` | 网络密钥索引（NetKey index）。 |
| `identity` | 节点身份状态（Node identity state）。 |

<a id="acf88660364760442dfab5280ae735d2d"></a>

### `node_reset_status`

```c
void(* bt_mesh_cfg_cli_cb::node_reset_status) (struct bt_mesh_cfg_cli *cli, uint16_t addr)
```

节点重置状态消息（Node Reset Status）的可选回调。

处理从服务器收到的节点重置状态消息（Node Reset Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 接收到状态消息（Status message）的客户端（Client）。 |
| `addr` | 发送方地址（Address of sender）。 |

<a id="a89eab453e00662f6f3f8a5d78f20d120"></a>

### `relay_status`

```c
void(* bt_mesh_cfg_cli_cb::relay_status) (struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status, uint8_t transmit)
```

中继状态消息（Relay Status）的可选回调。

处理从服务器收到的中继状态消息（Relay Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 接收到状态消息（Status message）的客户端（Client）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `status` | 请求消息的状态码（Status Code）。 |
| `transmit` | 中继重传次数与间隔步数（Relay retransmit count and interval steps）。 |

<a id="ab937311c41af68b1cd52a8a1c86145b1"></a>

### `ttl_status`

```c
void(* bt_mesh_cfg_cli_cb::ttl_status) (struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status)
```

默认生存时间状态消息（Default TTL Status）的可选回调。

处理从服务器收到的默认生存时间状态消息（Default TTL Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 接收到状态消息（Status message）的客户端（Client）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `status` | 请求消息的状态码（Status Code）。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/cfg_cli.h`

## 28.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/cfg_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/cfg__cli_8h_source.html)
- [bt_mesh_cfg_cli](P027_bt_mesh_cfg_cli_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bt_mesh_cfg_cli_mod_pub](P031_bt_mesh_cfg_cli_mod_pub_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_mesh_cfg_cli_hb_pub](P029_bt_mesh_cfg_cli_hb_pub_结构体.md)
- [bt_mesh_cfg_cli_hb_sub](P030_bt_mesh_cfg_cli_hb_sub_结构体.md)
- [bt_mesh_key_idx_unpack_list](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaa411ab7db2e71a114a8108eaec9ca12c)
- [bt_mesh_comp_p0_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga1f79d98273a984f1c49b4d5dd5bf8d30)
- [bt_mesh_comp_p1_elem_pull](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gae9a19b089d898af914ea5c287aca8fba)
- [net_buf_simple_pull_le16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gad59d180ae81b55f6d618565a37d25dba)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P027_bt_mesh_cfg_cli_结构体.md) · [返回大纲](大纲.md) · [下一章](P029_bt_mesh_cfg_cli_hb_pub_结构体.md)
