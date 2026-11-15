---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-83
title: bt_mesh_od_priv_proxy_cli_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__od__priv__proxy__cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第83章\_bt\_mesh\_od\_priv\_proxy\_cli\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__od__priv__proxy__cli.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

按需私有代理客户端（On-Demand Private Proxy Client）的模型上下文。

```c
#include <zephyr/bluetooth/mesh/od_priv_proxy_cli.h>
```

<a id="details"></a>

按需私有代理客户端（On-Demand Private Proxy Client）的模型上下文。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 83.1\_数据成员（Data Fields）

<a id="r_aeab540da0e42de4aa3e1550cd933f805"></a>

```c
const struct bt_mesh_model * model
```

相关声明：[bt_mesh_model](P075_bt_mesh_model_结构体.md)、[model](#aeab540da0e42de4aa3e1550cd933f805)。

请求协议数据单元重放保护列表模型条目指针（Solicitation PDU RPL model entry pointer）。

<a id="r_a8f172612abc904718018a6c2d9002e5e"></a>

```c
struct bt_mesh_msg_ack_ctx ack_ctx
```

相关声明：[bt_mesh_msg_ack_ctx](P081_bt_mesh_msg_ack_ctx_结构体.md)、[ack_ctx](#a8f172612abc904718018a6c2d9002e5e)。

<a id="r_aebd18bb98ded2e5dc3fca3fe121f3bc6"></a>

```c
void(* od_status )(struct bt_mesh_od_priv_proxy_cli *cli, uint16_t addr, uint8_t state)
```

相关声明：[od_status](#aebd18bb98ded2e5dc3fca3fe121f3bc6)、[bt_mesh_od_priv_proxy_cli](P083_bt_mesh_od_priv_proxy_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)。

按需私有代理状态消息（On-Demand Private Proxy Status）的可选回调。

## 83.2\_详细说明（Detailed Documentation）

<a id="a8f172612abc904718018a6c2d9002e5e"></a>

### `ack_ctx`

```c
struct bt_mesh_msg_ack_ctx bt_mesh_od_priv_proxy_cli::ack_ctx
```

<a id="aeab540da0e42de4aa3e1550cd933f805"></a>

### `model`

```c
const struct bt_mesh_model* bt_mesh_od_priv_proxy_cli::model
```

请求协议数据单元重放保护列表模型条目指针（Solicitation PDU RPL model entry pointer）。

<a id="aebd18bb98ded2e5dc3fca3fe121f3bc6"></a>

### `od_status`

```c
void(* bt_mesh_od_priv_proxy_cli::od_status) (struct bt_mesh_od_priv_proxy_cli *cli, uint16_t addr, uint8_t state)
```

按需私有代理状态消息（On-Demand Private Proxy Status）的可选回调。

处理从按需私有代理服务器（On-Demand Private Proxy server）收到的按需私有代理状态消息（On-Demand Private Proxy Status）。`state` 参数表示该服务器的状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 接收状态消息的按需私有代理客户端（On-Demand Private Proxy client）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `state` | 状态值（State value）。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/od_priv_proxy_cli.h`

## 83.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/od_priv_proxy_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/od__priv__proxy__cli_8h_source.html)
- [bt_mesh_model](P075_bt_mesh_model_结构体.md)
- [bt_mesh_msg_ack_ctx](P081_bt_mesh_msg_ack_ctx_结构体.md)
- [bt_mesh_od_priv_proxy_cli](P083_bt_mesh_od_priv_proxy_cli_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P082_bt_mesh_msg_ctx_结构体.md) · [返回大纲](大纲.md) · [下一章](P084_bt_mesh_priv_beacon_结构体.md)
