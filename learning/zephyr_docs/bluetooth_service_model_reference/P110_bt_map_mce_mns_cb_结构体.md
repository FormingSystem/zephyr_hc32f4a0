---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-110
title: bt_map_mce_mns_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__map__mce__mns__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第110章\_bt\_map\_mce\_mns\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__map__mce__mns__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

消息访问配置文件（MAP）客户端的MNS回调。

```c
#include <zephyr/bluetooth/classic/map.h>
```

<a id="details"></a>

MAP 客户端 MNS 回调，用于处理 MAP 客户端 MNS 事件。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 110.1\_数据成员（Data Fields）

<a id="r_a5b17ed8a8dcdf149924816fa07e4ff29"></a>

```c
void(* rfcomm_connected )(struct bt_conn *conn, struct bt_map_mce_mns *mce_mns)
```

相关声明：[rfcomm_connected](#a5b17ed8a8dcdf149924816fa07e4ff29)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_map_mce_mns](P109_bt_map_mce_mns_结构体.md)。

RFCOMM 传输连接建立回调。

<a id="r_ad516d3cc29bc6f32e9f24415cfb5c56d"></a>

```c
void(* rfcomm_disconnected )(struct bt_map_mce_mns *mce_mns)
```

相关声明：[rfcomm_disconnected](#ad516d3cc29bc6f32e9f24415cfb5c56d)、[bt_map_mce_mns](P109_bt_map_mce_mns_结构体.md)。

RFCOMM 传输连接断开回调。

<a id="r_a25e17d9e4d775963aedfe4f1a337a4ee"></a>

```c
void(* l2cap_connected )(struct bt_conn *conn, struct bt_map_mce_mns *mce_mns)
```

相关声明：[l2cap_connected](#a25e17d9e4d775963aedfe4f1a337a4ee)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_map_mce_mns](P109_bt_map_mce_mns_结构体.md)。

L2CAP 传输连接建立回调。

<a id="r_ad19cefcd45105bab829a427ab12f774b"></a>

```c
void(* l2cap_disconnected )(struct bt_map_mce_mns *mce_mns)
```

相关声明：[l2cap_disconnected](#ad19cefcd45105bab829a427ab12f774b)、[bt_map_mce_mns](P109_bt_map_mce_mns_结构体.md)。

L2CAP 传输连接断开回调。

<a id="r_ab3da25ab3b1d96914927e834e3ca45b6"></a>

```c
void(* connect )(struct bt_map_mce_mns *mce_mns, uint8_t version, uint16_t mopl, struct net_buf *buf)
```

相关声明：[connect](#ab3da25ab3b1d96914927e834e3ca45b6)、[bt_map_mce_mns](P109_bt_map_mce_mns_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

连接（Connect）回调。

<a id="r_a8e3c2515dce12a6bee185ae4ac38a4e7"></a>

```c
void(* disconnect )(struct bt_map_mce_mns *mce_mns, struct net_buf *buf)
```

相关声明：[disconnect](#a8e3c2515dce12a6bee185ae4ac38a4e7)、[bt_map_mce_mns](P109_bt_map_mce_mns_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

断开连接（Disconnect）回调。

<a id="r_aa27a21b8c6a0d088ad487f9b51c7dfc1"></a>

```c
void(* abort )(struct bt_map_mce_mns *mce_mns, struct net_buf *buf)
```

相关声明：[abort](#aa27a21b8c6a0d088ad487f9b51c7dfc1)、[bt_map_mce_mns](P109_bt_map_mce_mns_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

中止（Abort）回调。

<a id="r_a7266e0e0d00994af225efd63615e595d"></a>

```c
void(* send_event )(struct bt_map_mce_mns *mce_mns, bool final, struct net_buf *buf)
```

相关声明：[send_event](#a7266e0e0d00994af225efd63615e595d)、[bt_map_mce_mns](P109_bt_map_mce_mns_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送事件（Send event）回调。

## 110.2\_详细说明（Detailed Documentation）

<a id="aa27a21b8c6a0d088ad487f9b51c7dfc1"></a>

### `abort`

```c
void(* bt_map_mce_mns_cb::abort) (struct bt_map_mce_mns *mce_mns, struct net_buf *buf)
```

中止（Abort）回调。

收到 OBEX `ABORT` 请求时调用。应用应使用 `bt_map_mce_mns_abort()` 作出响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mns` | MNS 服务器实例。 |
| `buf` | 包含请求头的缓冲区。 |

<a id="ab3da25ab3b1d96914927e834e3ca45b6"></a>

### `connect`

```c
void(* bt_map_mce_mns_cb::connect) (struct bt_map_mce_mns *mce_mns, uint8_t version, uint16_t mopl, struct net_buf *buf)
```

连接（Connect）回调。

收到远端消息服务器设备（MSE）发送的 OBEX `CONNECT` 请求时调用。应用应使用 `bt_map_mce_mns_connect()` 作出响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mns` | MNS 服务器实例。 |
| `version` | 客户端请求的 OBEX 协议版本。 |
| `mopl` | 客户端请求的最大 OBEX 数据包长度。 |
| `buf` | 包含请求头（目标 UUID 等）的缓冲区。 |

<a id="a8e3c2515dce12a6bee185ae4ac38a4e7"></a>

### `disconnect`

```c
void(* bt_map_mce_mns_cb::disconnect) (struct bt_map_mce_mns *mce_mns, struct net_buf *buf)
```

断开连接（Disconnect）回调。

收到 OBEX `DISCONNECT` 请求时调用。应用应使用 `bt_map_mce_mns_disconnect()` 作出响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mns` | MNS 服务器实例。 |
| `buf` | 包含请求头的缓冲区。 |

<a id="a25e17d9e4d775963aedfe4f1a337a4ee"></a>

### `l2cap_connected`

```c
void(* bt_map_mce_mns_cb::l2cap_connected) (struct bt_conn *conn, struct bt_map_mce_mns *mce_mns)
```

L2CAP 传输连接建立回调。

底层传输（L2CAP）连接建立时调用。此时尚未协商 OBEX 连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 蓝牙连接对象（Bluetooth connection object）。 |
| `mce_mns` | MNS 服务器实例。 |

<a id="ad19cefcd45105bab829a427ab12f774b"></a>

### `l2cap_disconnected`

```c
void(* bt_map_mce_mns_cb::l2cap_disconnected) (struct bt_map_mce_mns *mce_mns)
```

L2CAP 传输连接断开回调。

底层传输（L2CAP）连接关闭时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mns` | MNS 服务器实例。 |

<a id="a5b17ed8a8dcdf149924816fa07e4ff29"></a>

### `rfcomm_connected`

```c
void(* bt_map_mce_mns_cb::rfcomm_connected) (struct bt_conn *conn, struct bt_map_mce_mns *mce_mns)
```

RFCOMM 传输连接建立回调。

底层传输（RFCOMM）连接建立时调用。此时尚未协商 OBEX 连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 蓝牙连接对象（Bluetooth connection object）。 |
| `mce_mns` | MNS 服务器实例。 |

<a id="ad516d3cc29bc6f32e9f24415cfb5c56d"></a>

### `rfcomm_disconnected`

```c
void(* bt_map_mce_mns_cb::rfcomm_disconnected) (struct bt_map_mce_mns *mce_mns)
```

RFCOMM 传输连接断开回调。

底层传输（RFCOMM）连接关闭时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mns` | MNS 服务器实例。 |

<a id="a7266e0e0d00994af225efd63615e595d"></a>

### `send_event`

```c
void(* bt_map_mce_mns_cb::send_event) (struct bt_map_mce_mns *mce_mns, bool final, struct net_buf *buf)
```

发送事件（Send event）回调。

收到远端 MSE 发送的发送事件（`SendEvent`）请求时调用。如果请求分片，可能多次调用。应用应使用 `bt_map_mce_mns_send_event()` 作出响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mns` | MNS 服务器实例。 |
| `final` | 如果这是最后一个数据包，则为 `true`；如果后面还有数据，则为 `false`。 |
| `buf` | 包含事件报告 XML 数据及头部的缓冲区。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/map.h`

## 110.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/map.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2classic_2map_8h_source.html)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_map_mce_mns](P109_bt_map_mce_mns_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_map_mce_mns_abort()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mns.html#ga7309e25833e6594dc0018afe8b0a403c)
- [bt_map_mce_mns_connect()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mns.html#gaab9161c0524c74cb4b03938c26642f4a)
- [bt_map_mce_mns_disconnect()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mns.html#ga14411f8c0e8ce90824d366d28d4a2d2e)
- [bt_map_mce_mns_send_event()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mns.html#ga3e181d1bd37877dd8abf47a541c4b98e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P109_bt_map_mce_mns_结构体.md) · [返回大纲](大纲.md) · [下一章](P111_bt_map_mce_mns_l2cap_server_结构体.md)
