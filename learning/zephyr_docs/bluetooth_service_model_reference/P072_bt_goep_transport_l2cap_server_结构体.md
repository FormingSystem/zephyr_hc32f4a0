---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-72
title: bt_goep_transport_l2cap_server_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__goep__transport__l2cap__server.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第72章\_bt\_goep\_transport\_l2cap\_server\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__goep__transport__l2cap__server.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

GOEP v2.0 及更高版本的服务器结构体。

```c
#include <zephyr/bluetooth/classic/goep.h>
```

<a id="details"></a>

GOEP v2.0 及更高版本的服务器结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 72.1\_数据成员（Data Fields）

<a id="r_a514125628a8d90cb8c50982c2f2c133d"></a>

```c
struct bt_l2cap_server l2cap
```

相关声明：[bt_l2cap_server](P106_bt_l2cap_server_结构体.md)、[l2cap](#a514125628a8d90cb8c50982c2f2c133d)。

GOEP v2.0 及后续版本使用的 L2CAP 协议／服务复用器（PSM）。

<a id="r_a7441985cb5ce8e2f961dcd5c5175f9c8"></a>

```c
int(* accept )(struct bt_conn *conn, struct bt_goep_transport_l2cap_server *server, struct bt_goep **goep)
```

相关声明：[accept](#a7441985cb5ce8e2f961dcd5c5175f9c8)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_goep_transport_l2cap_server](P072_bt_goep_transport_l2cap_server_结构体.md)、[bt_goep](P070_bt_goep_结构体.md)。

服务器接受回调（Server accept callback）。

<a id="r_a8003824bb36da572b290fcb3a55b6c59"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#a8003824bb36da572b290fcb3a55b6c59)。

## 72.2\_详细说明（Detailed Documentation）

<a id="a7441985cb5ce8e2f961dcd5c5175f9c8"></a>

### `accept`

```c
int(* bt_goep_transport_l2cap_server::accept) (struct bt_conn *conn, struct bt_goep_transport_l2cap_server *server, struct bt_goep **goep)
```

服务器接受回调（Server accept callback）。

新的传入通用对象交换规范连接（GOEP connection）需要授权（Authorization）时，调用此回调。

回调返回前，应将 `bt_goep::transport_ops` 初始化为指向有效 `bt_goep_transport_ops` 对象的地址。`bt_obex::rx` 的 `mtu` 字段值将被忽略，改为赋予根据 `CONFIG_BT_GOEP_L2CAP_MTU` 计算的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 请求授权（Authorization）的连接。 |
| `server` | 指向与此回调对应的服务器结构（Server structure）的指针。 |
| `goep` | 用于接收已分配通用对象交换规范对象（GOEP object）的指针。 |

**警告（Warning）**：警告（Warning）：调用者负责将通用对象交换规范对象（GOEP object）的父对象清零。

**说明（Note）**：注意（Note）：接受回调（Accept callback）必须按以下方式初始化返回的 GOEP 实例：将 `bt_goep::transport_ops` 设置为有效的操作表；通过 `bt_goep::v2` 提供所指向的 `bt_goep_transport_v2` 实例，该实例在传输连接整个生命周期内必须有效且地址稳定，同时将 `bt_goep::v1` 设为 `NULL`；将版本专用对象的反向指针 `bt_goep_transport_v2::goep` 初始化为指向父通用对象交换规范对象（GOEP）。版本专用对象必须在整个传输生命周期内保持有效。

**返回（Returns）**：返回值（Returns）：成功时为 `0`，错误时为负值。没有空间容纳新对象时为 `-ENOMEM`；应用未授权此连接时为 `-EACCES`；加密密钥太短时为 `-EPERM`。

<a id="a514125628a8d90cb8c50982c2f2c133d"></a>

### `l2cap`

```c
struct bt_l2cap_server bt_goep_transport_l2cap_server::l2cap
```

GOEP v2.0 及后续版本使用的 L2CAP 协议／服务复用器（PSM）。

`bt_goep_transport_l2cap_server::l2cap` 用于注册逻辑链路控制与适配协议服务器（L2CAP server）。

`bt_l2cap_server::psm` 可以传入预先设置的协议／服务复用器（PSM），但不推荐；也可传入 `0`，让 `bt_goep_transport_l2cap_server_register` 调用时自动分配 PSM。`bt_l2cap_server::sec_level` 用于要求 L2CAP 服务器的最低安全等级。GOEP 应用不应使用 `bt_l2cap_server::accept`，而应使用 `bt_goep_transport_l2cap_server::accept`。

<a id="a8003824bb36da572b290fcb3a55b6c59"></a>

### `node`

```c
sys_snode_t bt_goep_transport_l2cap_server::node
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/goep.h`

## 72.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/goep.h](https://docs.zephyrproject.org/latest/doxygen/html/goep_8h_source.html)
- [bt_l2cap_server](P106_bt_l2cap_server_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_goep_transport_l2cap_server](P072_bt_goep_transport_l2cap_server_结构体.md)
- [bt_goep](P070_bt_goep_结构体.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [bt_goep::transport_ops](P070_bt_goep_结构体.md#abca52709a4b2535eccecb632a1a6f29d)
- [bt_goep_transport_ops](P073_bt_goep_transport_ops_结构体.md)
- [bt_obex::rx](P127_bt_obex_结构体.md#ac2bc4ebc3b440c1be71c033b7c051c98)
- [CONFIG_BT_GOEP_L2CAP_MTU](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GOEP_L2CAP_MTU)
- [bt_goep::v2](P070_bt_goep_结构体.md#a6d341f018f6e7dc9187eab11cea9bc53)
- [bt_goep_transport_v2](P076_bt_goep_transport_v2_结构体.md)
- [bt_goep::v1](P070_bt_goep_结构体.md#a9820cd834fb77847110b0c0f490b637e)
- [bt_goep_transport_v2::goep](P076_bt_goep_transport_v2_结构体.md#a5d3086e35bd244810e87d4bd0023e7bc)
- [通用对象交换规范（Generic Object Exchange Profile，GOEP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html)
- [bt_l2cap_server::psm](P106_bt_l2cap_server_结构体.md#a07925dda8566ee7518b1809725e1b110)
- [bt_goep_transport_l2cap_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep__transport__l2cap.html#ga5f7a699eb8c857c6b6b99c506953f176)
- [bt_l2cap_server::sec_level](P106_bt_l2cap_server_结构体.md#a9f082abf679a397264a7b51fa4400852)
- [bt_l2cap_server::accept](P106_bt_l2cap_server_结构体.md#ad31a1908f7dc733f9497164ccabba2af)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P071_bt_goep_transport_结构体.md) · [返回大纲](大纲.md) · [下一章](P073_bt_goep_transport_ops_结构体.md)
