---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-118
title: bt_map_mse_mns_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__map__mse__mns__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第118章\_bt\_map\_mse\_mns\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__map__mse__mns__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

消息访问配置文件（MAP）服务器的MNS回调。

```c
#include <zephyr/bluetooth/classic/map.h>
```

<a id="details"></a>

MAP 服务器 MNS 回调，用于处理 MAP 服务器 MNS 事件。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 118.1\_数据成员（Data Fields）

<a id="r_acbaddcaff6e7b5a4cedaccad97186dc4"></a>

```c
void(* rfcomm_connected )(struct bt_conn *conn, struct bt_map_mse_mns *mse_mns)
```

相关声明：[rfcomm_connected](#acbaddcaff6e7b5a4cedaccad97186dc4)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_map_mse_mns](P117_bt_map_mse_mns_结构体.md)。

RFCOMM 传输连接建立回调。

<a id="r_a8cc8665110f38287951012307ce8837b"></a>

```c
void(* rfcomm_disconnected )(struct bt_map_mse_mns *mse_mns)
```

相关声明：[rfcomm_disconnected](#a8cc8665110f38287951012307ce8837b)、[bt_map_mse_mns](P117_bt_map_mse_mns_结构体.md)。

RFCOMM 传输连接断开回调。

<a id="r_a62f7d9e4661fce6976650c3d90245dc8"></a>

```c
void(* l2cap_connected )(struct bt_conn *conn, struct bt_map_mse_mns *mse_mns)
```

相关声明：[l2cap_connected](#a62f7d9e4661fce6976650c3d90245dc8)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_map_mse_mns](P117_bt_map_mse_mns_结构体.md)。

L2CAP 传输连接建立回调。

<a id="r_abcf2bc6750a60d66cf9999d542d0c8c2"></a>

```c
void(* l2cap_disconnected )(struct bt_map_mse_mns *mse_mns)
```

相关声明：[l2cap_disconnected](#abcf2bc6750a60d66cf9999d542d0c8c2)、[bt_map_mse_mns](P117_bt_map_mse_mns_结构体.md)。

L2CAP 传输连接断开回调。

<a id="r_aac533d7aa478d0645a1853de8a5fd354"></a>

```c
void(* connect )(struct bt_map_mse_mns *mse_mns, uint8_t rsp_code, uint8_t version, uint16_t mopl, struct net_buf *buf)
```

相关声明：[connect](#aac533d7aa478d0645a1853de8a5fd354)、[bt_map_mse_mns](P117_bt_map_mse_mns_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

连接（Connect）回调。

<a id="r_a2afd0b35998943c07584a70fa6a6107a"></a>

```c
void(* disconnect )(struct bt_map_mse_mns *mse_mns, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[disconnect](#a2afd0b35998943c07584a70fa6a6107a)、[bt_map_mse_mns](P117_bt_map_mse_mns_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

断开连接（Disconnect）回调。

<a id="r_a168facdd5cdcc695814e4e9dd517f807"></a>

```c
void(* abort )(struct bt_map_mse_mns *mse_mns, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[abort](#a168facdd5cdcc695814e4e9dd517f807)、[bt_map_mse_mns](P117_bt_map_mse_mns_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

中止（Abort）回调。

<a id="r_ab38e352b61b54a9961f200c9cf30e5b8"></a>

```c
void(* send_event )(struct bt_map_mse_mns *mse_mns, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[send_event](#ab38e352b61b54a9961f200c9cf30e5b8)、[bt_map_mse_mns](P117_bt_map_mse_mns_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送事件（Send event）回调。

## 118.2\_详细说明（Detailed Documentation）

<a id="a168facdd5cdcc695814e4e9dd517f807"></a>

### `abort`

```c
void(* bt_map_mse_mns_cb::abort) (struct bt_map_mse_mns *mse_mns, uint8_t rsp_code, struct net_buf *buf)
```

中止（Abort）回调。

收到 OBEX `ABORT` 响应时调用。被中止的操作会被取消。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mns` | MNS 客户端实例。 |
| `rsp_code` | 响应码 `bt_obex_rsp_code`。 |
| `buf` | 包含响应头的缓冲区。 |

<a id="aac533d7aa478d0645a1853de8a5fd354"></a>

### `connect`

```c
void(* bt_map_mse_mns_cb::connect) (struct bt_map_mse_mns *mse_mns, uint8_t rsp_code, uint8_t version, uint16_t mopl, struct net_buf *buf)
```

连接（Connect）回调。

收到 OBEX `CONNECT` 响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mns` | MNS 客户端实例。 |
| `rsp_code` | 响应码 `bt_obex_rsp_code`；成功时为 `BT_OBEX_RSP_CODE_SUCCESS`。 |
| `version` | 服务器支持的 OBEX 协议版本。 |
| `mopl` | 服务器支持的最大 OBEX 数据包长度。 |
| `buf` | 包含附加响应头（连接 ID 等）的缓冲区。 |

<a id="a2afd0b35998943c07584a70fa6a6107a"></a>

### `disconnect`

```c
void(* bt_map_mse_mns_cb::disconnect) (struct bt_map_mse_mns *mse_mns, uint8_t rsp_code, struct net_buf *buf)
```

断开连接（Disconnect）回调。

收到 OBEX `DISCONNECT` 响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mns` | MNS 客户端实例。 |
| `rsp_code` | 响应码 `bt_obex_rsp_code`。 |
| `buf` | 包含响应头的缓冲区。 |

<a id="a62f7d9e4661fce6976650c3d90245dc8"></a>

### `l2cap_connected`

```c
void(* bt_map_mse_mns_cb::l2cap_connected) (struct bt_conn *conn, struct bt_map_mse_mns *mse_mns)
```

L2CAP 传输连接建立回调。

底层传输（L2CAP）连接建立时调用。此时尚未协商 OBEX 连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 蓝牙连接对象（Bluetooth connection object）。 |
| `mse_mns` | MNS 客户端实例。 |

<a id="abcf2bc6750a60d66cf9999d542d0c8c2"></a>

### `l2cap_disconnected`

```c
void(* bt_map_mse_mns_cb::l2cap_disconnected) (struct bt_map_mse_mns *mse_mns)
```

L2CAP 传输连接断开回调。

底层传输（L2CAP）连接关闭时调用。所有待处理操作均被取消。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mns` | MNS 客户端实例。 |

<a id="acbaddcaff6e7b5a4cedaccad97186dc4"></a>

### `rfcomm_connected`

```c
void(* bt_map_mse_mns_cb::rfcomm_connected) (struct bt_conn *conn, struct bt_map_mse_mns *mse_mns)
```

RFCOMM 传输连接建立回调。

底层传输（RFCOMM）连接建立时调用。此时尚未协商 OBEX 连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 蓝牙连接对象（Bluetooth connection object）。 |
| `mse_mns` | MNS 客户端实例。 |

<a id="a8cc8665110f38287951012307ce8837b"></a>

### `rfcomm_disconnected`

```c
void(* bt_map_mse_mns_cb::rfcomm_disconnected) (struct bt_map_mse_mns *mse_mns)
```

RFCOMM 传输连接断开回调。

底层传输（RFCOMM）连接关闭时调用。所有待处理操作均被取消。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mns` | MNS 客户端实例。 |

<a id="ab38e352b61b54a9961f200c9cf30e5b8"></a>

### `send_event`

```c
void(* bt_map_mse_mns_cb::send_event) (struct bt_map_mse_mns *mse_mns, uint8_t rsp_code, struct net_buf *buf)
```

发送事件（Send event）回调。

收到发送事件（`SendEvent`）响应时调用。如果请求分片，可能多次调用，响应码为 `BT_OBEX_RSP_CODE_CONTINUE`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mns` | MNS 客户端实例。 |
| `rsp_code` | 响应码 `bt_obex_rsp_code`；部分上传时为 `BT_OBEX_RSP_CODE_CONTINUE`。 |
| `buf` | 包含响应头的缓冲区。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/map.h`

## 118.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/map.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2classic_2map_8h_source.html)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_map_mse_mns](P117_bt_map_mse_mns_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bt_obex_rsp_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga81b84c24a976c6c13d33eb23b0b10ae9)
- [BT_OBEX_RSP_CODE_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9af449d3c85fbec550c76e29287a626789)
- [BT_OBEX_RSP_CODE_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a7e38ca653283f53b62fa4b21f48d998a)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P117_bt_map_mse_mns_结构体.md) · [返回大纲](大纲.md) · [下一章](P119_bt_mcc_cb_结构体.md)
