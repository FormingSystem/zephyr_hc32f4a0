---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-100
title: bt_mesh_sol_pdu_rpl_cli_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__sol__pdu__rpl__cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第100章\_bt\_mesh\_sol\_pdu\_rpl\_cli\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__sol__pdu__rpl__cli.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

请求PDU重放保护列表客户端（Solicitation PDU RPL Client）的模型上下文。

```c
#include <zephyr/bluetooth/mesh/sol_pdu_rpl_cli.h>
```

<a id="details"></a>

请求PDU重放保护列表客户端（Solicitation PDU RPL Client）的模型上下文。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 100.1\_数据成员（Data Fields）

<a id="r_a272ff5ae0930f51c9175d99f5c9066e2"></a>

```c
const struct bt_mesh_model * model
```

相关声明：[bt_mesh_model](P075_bt_mesh_model_结构体.md)、[model](#a272ff5ae0930f51c9175d99f5c9066e2)。

请求协议数据单元重放保护列表模型条目指针（Solicitation PDU RPL model entry pointer）。

<a id="r_a291134f4b6acc60671307ef3b53c4ac8"></a>

```c
struct bt_mesh_msg_ack_ctx ack_ctx
```

相关声明：[bt_mesh_msg_ack_ctx](P081_bt_mesh_msg_ack_ctx_结构体.md)、[ack_ctx](#a291134f4b6acc60671307ef3b53c4ac8)。

<a id="r_a6c734589ee3361bfc071da55521a6dee"></a>

```c
void(* srpl_status )(struct bt_mesh_sol_pdu_rpl_cli *cli, uint16_t addr, uint16_t range_start, uint8_t range_length)
```

相关声明：[srpl_status](#a6c734589ee3361bfc071da55521a6dee)、[bt_mesh_sol_pdu_rpl_cli](P100_bt_mesh_sol_pdu_rpl_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

请求协议数据单元重放保护列表状态消息（Solicitation PDU RPL Status）的可选回调。

## 100.2\_详细说明（Detailed Documentation）

<a id="a291134f4b6acc60671307ef3b53c4ac8"></a>

### `ack_ctx`

```c
struct bt_mesh_msg_ack_ctx bt_mesh_sol_pdu_rpl_cli::ack_ctx
```

<a id="a272ff5ae0930f51c9175d99f5c9066e2"></a>

### `model`

```c
const struct bt_mesh_model* bt_mesh_sol_pdu_rpl_cli::model
```

请求协议数据单元重放保护列表模型条目指针（Solicitation PDU RPL model entry pointer）。

<a id="a6c734589ee3361bfc071da55521a6dee"></a>

### `srpl_status`

```c
void(* bt_mesh_sol_pdu_rpl_cli::srpl_status) (struct bt_mesh_sol_pdu_rpl_cli *cli, uint16_t addr, uint16_t range_start, uint8_t range_length)
```

请求协议数据单元重放保护列表状态消息（Solicitation PDU RPL Status）的可选回调。

处理从请求协议数据单元重放保护列表服务器（Solicitation PDU RPL server）收到的相应状态消息（Solicitation PDU RPL Status）。`start` 参数表示服务器已清除范围的起点；`length` 参数表示服务器已清除范围的长度。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 接收状态消息的请求协议数据单元重放保护列表客户端（Solicitation PDU RPL client）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `range_start` | 范围起始值（Range start value）。 |
| `range_length` | 范围长度值（Range length value）。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/sol_pdu_rpl_cli.h`

## 100.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/sol_pdu_rpl_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/sol__pdu__rpl__cli_8h_source.html)
- [bt_mesh_model](P075_bt_mesh_model_结构体.md)
- [bt_mesh_msg_ack_ctx](P081_bt_mesh_msg_ack_ctx_结构体.md)
- [bt_mesh_sol_pdu_rpl_cli](P100_bt_mesh_sol_pdu_rpl_cli_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P099_bt_mesh_send_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P101_bt_mesh_statistic_结构体.md)
