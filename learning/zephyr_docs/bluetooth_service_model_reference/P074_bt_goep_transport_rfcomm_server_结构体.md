---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-74
title: bt_goep_transport_rfcomm_server_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__goep__transport__rfcomm__server.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第74章\_bt\_goep\_transport\_rfcomm\_server\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__goep__transport__rfcomm__server.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

GOEP v1.1 的服务器结构体。

```c
#include <zephyr/bluetooth/classic/goep.h>
```

<a id="details"></a>

GOEP v1.1 的服务器结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 74.1\_数据成员（Data Fields）

<a id="r_adaa1fb6c58cdb28560e3b4be272ae94d"></a>

```c
struct bt_rfcomm_server rfcomm
```

相关声明：[bt_rfcomm_server](P158_bt_rfcomm_server_结构体.md)、[rfcomm](#adaa1fb6c58cdb28560e3b4be272ae94d)。

GOEP v1.1 使用的串口仿真协议服务器（RFCOMM server）。

<a id="r_a66c433a47c20018f9f0a018b4fbc8048"></a>

```c
int(* accept )(struct bt_conn *conn, struct bt_goep_transport_rfcomm_server *server, struct bt_goep **goep)
```

相关声明：[accept](#a66c433a47c20018f9f0a018b4fbc8048)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_goep_transport_rfcomm_server](P074_bt_goep_transport_rfcomm_server_结构体.md)、[bt_goep](P070_bt_goep_结构体.md)。

服务器接受回调（Server accept callback）。

<a id="r_a4d1df6a46e76d2f9e37a2d791d79bb84"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#a4d1df6a46e76d2f9e37a2d791d79bb84)。

## 74.2\_详细说明（Detailed Documentation）

<a id="a66c433a47c20018f9f0a018b4fbc8048"></a>

### `accept`

```c
int(* bt_goep_transport_rfcomm_server::accept) (struct bt_conn *conn, struct bt_goep_transport_rfcomm_server *server, struct bt_goep **goep)
```

服务器接受回调（Server accept callback）。

新的传入通用对象交换规范连接（GOEP connection）需要授权（Authorization）时，调用此回调。

回调返回前，应将 `bt_goep::transport_ops` 初始化为指向有效 `bt_goep_transport_ops` 对象的地址。`bt_obex::rx` 的 `mtu` 字段值将被忽略，改为赋予根据 `CONFIG_BT_GOEP_RFCOMM_MTU` 计算的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 请求授权（Authorization）的连接。 |
| `server` | 指向与此回调对应的服务器结构（Server structure）的指针。 |
| `goep` | 用于接收已分配通用对象交换规范对象（GOEP object）的指针。 |

**警告（Warning）**：警告（Warning）：调用者负责将通用对象交换规范对象（GOEP object）的父对象清零。

**说明（Note）**：注意（Note）：接受回调（Accept callback）必须按以下方式初始化返回的 GOEP 实例：将 `bt_goep::transport_ops` 设置为有效的操作表；通过 `bt_goep::v1` 提供所指向的 `bt_goep_transport_v1` 实例，该实例在传输连接整个生命周期内必须有效且地址稳定，同时将 `bt_goep::v2` 设为 `NULL`；将版本专用对象的反向指针 `bt_goep_transport_v1::goep` 初始化为指向父通用对象交换规范对象（GOEP）。版本专用对象必须在整个传输生命周期内保持有效。

**返回（Returns）**：返回值（Returns）：成功时为 `0`，错误时为负值。没有空间容纳新对象时为 `-ENOMEM`；应用未授权此连接时为 `-EACCES`；加密密钥太短时为 `-EPERM`。

<a id="a4d1df6a46e76d2f9e37a2d791d79bb84"></a>

### `node`

```c
sys_snode_t bt_goep_transport_rfcomm_server::node
```

<a id="adaa1fb6c58cdb28560e3b4be272ae94d"></a>

### `rfcomm`

```c
struct bt_rfcomm_server bt_goep_transport_rfcomm_server::rfcomm
```

GOEP v1.1 使用的串口仿真协议服务器（RFCOMM server）。

`bt_goep_transport_rfcomm_server::rfcomm` 用于注册串口仿真协议服务器（RFCOMM server）。

`bt_rfcomm_server::channel` 可以传入预先设置的通道（Channel），但不推荐；也可传入 `0`，让 `bt_goep_transport_rfcomm_server_register` 调用时自动分配通道。GOEP 应用不应使用 `bt_rfcomm_server::accept`，而应使用 `bt_goep_transport_rfcomm_server::accept`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/goep.h`

## 74.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/goep.h](https://docs.zephyrproject.org/latest/doxygen/html/goep_8h_source.html)
- [bt_rfcomm_server](P158_bt_rfcomm_server_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_goep_transport_rfcomm_server](P074_bt_goep_transport_rfcomm_server_结构体.md)
- [bt_goep](P070_bt_goep_结构体.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [bt_goep::transport_ops](P070_bt_goep_结构体.md#abca52709a4b2535eccecb632a1a6f29d)
- [bt_goep_transport_ops](P073_bt_goep_transport_ops_结构体.md)
- [bt_obex::rx](P127_bt_obex_结构体.md#ac2bc4ebc3b440c1be71c033b7c051c98)
- [CONFIG_BT_GOEP_RFCOMM_MTU](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GOEP_RFCOMM_MTU)
- [bt_goep::v1](P070_bt_goep_结构体.md#a9820cd834fb77847110b0c0f490b637e)
- [bt_goep_transport_v1](P075_bt_goep_transport_v1_结构体.md)
- [bt_goep::v2](P070_bt_goep_结构体.md#a6d341f018f6e7dc9187eab11cea9bc53)
- [bt_goep_transport_v1::goep](P075_bt_goep_transport_v1_结构体.md#a82ed6f11432432f051c705bddfd7a53b)
- [通用对象交换规范（Generic Object Exchange Profile，GOEP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html)
- [bt_rfcomm_server::channel](P158_bt_rfcomm_server_结构体.md#a30b22ea64c0fdd7130e8aaa79519e776)
- [bt_goep_transport_rfcomm_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep__transport__rfcomm.html#ga781dc33ffa086753319c84f59b8e977f)
- [bt_rfcomm_server::accept](P158_bt_rfcomm_server_结构体.md#ac08708bb8161f787737962f62d3c003f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P073_bt_goep_transport_ops_结构体.md) · [返回大纲](大纲.md) · [下一章](P075_bt_goep_transport_v1_结构体.md)
