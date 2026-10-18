---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-4
title: bt_bip_l2cap_server_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bip__l2cap__server.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_bt\_bip\_l2cap\_server\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bip__l2cap__server.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BIP 的 L2CAP 服务器结构体。

```c
#include <zephyr/bluetooth/classic/bip.h>
```

<a id="details"></a>

基本成像规范逻辑链路控制与适配协议服务器结构（BIP L2CAP server structure）。表示使用 L2CAP 传输的 BIP 服务器。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 4.1\_数据成员（Data Fields）

<a id="r_a830f0f266401a3e95c21e5fbb25bc057"></a>

```c
struct bt_goep_transport_l2cap_server server
```

相关声明：[bt_goep_transport_l2cap_server](P072_bt_goep_transport_l2cap_server_结构体.md)、[server](#a830f0f266401a3e95c21e5fbb25bc057)。

底层通用对象交换规范逻辑链路控制与适配协议服务器（GOEP L2CAP server）。

<a id="r_aeb027a550bef264ef287e25cc3d9ffa9"></a>

```c
int(* accept )(struct bt_conn *conn, struct bt_bip_l2cap_server *server, struct bt_bip **bip)
```

相关声明：[accept](#aeb027a550bef264ef287e25cc3d9ffa9)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_bip_l2cap_server](P004_bt_bip_l2cap_server_结构体.md)、[server](#a830f0f266401a3e95c21e5fbb25bc057)、[bt_bip](P001_bt_bip_结构体.md)。

接受连接回调（Accept connection callback）。

## 4.2\_详细说明（Detailed Documentation）

<a id="aeb027a550bef264ef287e25cc3d9ffa9"></a>

### `accept`

```c
int(* bt_bip_l2cap_server::accept) (struct bt_conn *conn, struct bt_bip_l2cap_server *server, struct bt_bip **bip)
```

接受连接回调（Accept connection callback）。

接受新的逻辑链路控制与适配协议连接（L2CAP connection）时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 蓝牙连接（Bluetooth Connection）。 |
| `server` | 逻辑链路控制与适配协议服务器实例（L2CAP server instance）。 |
| `bip` | 用于存放新建基本成像规范实例（BIP instance）的指针。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="a830f0f266401a3e95c21e5fbb25bc057"></a>

### `server`

```c
struct bt_goep_transport_l2cap_server bt_bip_l2cap_server::server
```

底层通用对象交换规范逻辑链路控制与适配协议服务器（GOEP L2CAP server）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/bip.h`

## 4.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/bip.h](https://docs.zephyrproject.org/latest/doxygen/html/bip_8h_source.html)
- [bt_goep_transport_l2cap_server](P072_bt_goep_transport_l2cap_server_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_bip_l2cap_server](P004_bt_bip_l2cap_server_结构体.md)
- [bt_bip](P001_bt_bip_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P003_bt_bip_client_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P005_bt_bip_rfcomm_server_结构体.md)
