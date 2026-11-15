---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-114
title: bt_map_mse_mas_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__map__mse__mas__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第114章\_bt\_map\_mse\_mas\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__map__mse__mas__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

消息访问配置文件（MAP）服务器的MAS回调。

```c
#include <zephyr/bluetooth/classic/map.h>
```

<a id="details"></a>

MAP 服务器 MAS 回调，用于处理 MAP 服务器 MAS 事件。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 114.1\_数据成员（Data Fields）

<a id="r_a92d897fa7c8f9d9e42a5b8e18b25a7e1"></a>

```c
void(* rfcomm_connected )(struct bt_conn *conn, struct bt_map_mse_mas *mse_mas)
```

相关声明：[rfcomm_connected](#a92d897fa7c8f9d9e42a5b8e18b25a7e1)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_map_mse_mas](P113_bt_map_mse_mas_结构体.md)。

RFCOMM 传输连接建立回调。

<a id="r_a462a2826086f8ebc40617752c463bf83"></a>

```c
void(* rfcomm_disconnected )(struct bt_map_mse_mas *mse_mas)
```

相关声明：[rfcomm_disconnected](#a462a2826086f8ebc40617752c463bf83)、[bt_map_mse_mas](P113_bt_map_mse_mas_结构体.md)。

RFCOMM 传输连接断开回调。

<a id="r_a5d5246c3d8e3a229fdd6d33f01d48e50"></a>

```c
void(* l2cap_connected )(struct bt_conn *conn, struct bt_map_mse_mas *mse_mas)
```

相关声明：[l2cap_connected](#a5d5246c3d8e3a229fdd6d33f01d48e50)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_map_mse_mas](P113_bt_map_mse_mas_结构体.md)。

L2CAP 传输连接建立回调。

<a id="r_a32dfc15ce0c67ef9b68d43c51a685668"></a>

```c
void(* l2cap_disconnected )(struct bt_map_mse_mas *mse_mas)
```

相关声明：[l2cap_disconnected](#a32dfc15ce0c67ef9b68d43c51a685668)、[bt_map_mse_mas](P113_bt_map_mse_mas_结构体.md)。

L2CAP 传输连接断开回调。

<a id="r_a1fd7e912c55a267e303e347bdd419ebe"></a>

```c
void(* connect )(struct bt_map_mse_mas *mse_mas, uint8_t version, uint16_t mopl, struct net_buf *buf)
```

相关声明：[connect](#a1fd7e912c55a267e303e347bdd419ebe)、[bt_map_mse_mas](P113_bt_map_mse_mas_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

连接（Connect）回调。

<a id="r_a0192c32ce2e08af30ba8288025ae0b55"></a>

```c
void(* disconnect )(struct bt_map_mse_mas *mse_mas, struct net_buf *buf)
```

相关声明：[disconnect](#a0192c32ce2e08af30ba8288025ae0b55)、[bt_map_mse_mas](P113_bt_map_mse_mas_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

断开连接（Disconnect）回调。

<a id="r_a58392850c26d91c10a6ed35c7d41d6eb"></a>

```c
void(* abort )(struct bt_map_mse_mas *mse_mas, struct net_buf *buf)
```

相关声明：[abort](#a58392850c26d91c10a6ed35c7d41d6eb)、[bt_map_mse_mas](P113_bt_map_mse_mas_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

中止（Abort）回调。

<a id="r_a6d0489d861546f5e9501ff6527df7d3f"></a>

```c
void(* set_ntf_reg )(struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf)
```

相关声明：[set_ntf_reg](#a6d0489d861546f5e9501ff6527df7d3f)、[bt_map_mse_mas](P113_bt_map_mse_mas_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

设置通知注册（Set notification registration）回调。

<a id="r_a06897a7617ee1f68f56c1b230f9f12e9"></a>

```c
void(* set_folder )(struct bt_map_mse_mas *mse_mas, uint8_t flags, struct net_buf *buf)
```

相关声明：[set_folder](#a06897a7617ee1f68f56c1b230f9f12e9)、[bt_map_mse_mas](P113_bt_map_mse_mas_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

设置文件夹（Set folder）回调。

<a id="r_a1b37e5006775590e91731e873c0c4dc9"></a>

```c
void(* get_folder_listing )(struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf)
```

相关声明：[get_folder_listing](#a1b37e5006775590e91731e873c0c4dc9)、[bt_map_mse_mas](P113_bt_map_mse_mas_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

获取文件夹列表（Get folder listing）回调。

<a id="r_ab3039d3b0e740e9eda1b3efd392916f8"></a>

```c
void(* get_msg_listing )(struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf)
```

相关声明：[get_msg_listing](#ab3039d3b0e740e9eda1b3efd392916f8)、[bt_map_mse_mas](P113_bt_map_mse_mas_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

获取消息列表（Get message listing）回调。

<a id="r_a47d93ccf18b704eaf8d0906e75b8ddff"></a>

```c
void(* get_msg )(struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf)
```

相关声明：[get_msg](#a47d93ccf18b704eaf8d0906e75b8ddff)、[bt_map_mse_mas](P113_bt_map_mse_mas_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

获取消息（Get message）回调。

<a id="r_a5fc25a4ad534e3490297faabcd86f51e"></a>

```c
void(* set_msg_status )(struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf)
```

相关声明：[set_msg_status](#a5fc25a4ad534e3490297faabcd86f51e)、[bt_map_mse_mas](P113_bt_map_mse_mas_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

设置消息状态（Set message status）回调。

<a id="r_a3113a29c5a6e7ba149bad09449cb5da4"></a>

```c
void(* push_msg )(struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf)
```

相关声明：[push_msg](#a3113a29c5a6e7ba149bad09449cb5da4)、[bt_map_mse_mas](P113_bt_map_mse_mas_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

推送消息（Push message）回调。

<a id="r_aed0b3894512dc0e3b363d3dd98b3dfbf"></a>

```c
void(* update_inbox )(struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf)
```

相关声明：[update_inbox](#aed0b3894512dc0e3b363d3dd98b3dfbf)、[bt_map_mse_mas](P113_bt_map_mse_mas_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

更新收件箱（Update inbox）回调。

<a id="r_a6aae3db4af23f0408f328cac2b9fbf14"></a>

```c
void(* get_mas_inst_info )(struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf)
```

相关声明：[get_mas_inst_info](#a6aae3db4af23f0408f328cac2b9fbf14)、[bt_map_mse_mas](P113_bt_map_mse_mas_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

获取 MAS 实例信息（Get MAS instance info）回调。

<a id="r_a5094efadea33ad701eaad813fe2bde50"></a>

```c
void(* set_owner_status )(struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf)
```

相关声明：[set_owner_status](#a5094efadea33ad701eaad813fe2bde50)、[bt_map_mse_mas](P113_bt_map_mse_mas_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

设置所有者状态（Set owner status）回调。

<a id="r_af016d7689a8546612c73bd41cdec6e5a"></a>

```c
void(* get_owner_status )(struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf)
```

相关声明：[get_owner_status](#af016d7689a8546612c73bd41cdec6e5a)、[bt_map_mse_mas](P113_bt_map_mse_mas_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

获取所有者状态（Get owner status）回调。

<a id="r_aff9b5da1a558e79eaa744677437e66cc"></a>

```c
void(* get_convo_listing )(struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf)
```

相关声明：[get_convo_listing](#aff9b5da1a558e79eaa744677437e66cc)、[bt_map_mse_mas](P113_bt_map_mse_mas_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

获取会话列表（Get conversation listing）回调。

<a id="r_a91407e120e3a312061c8431fd3bb48a7"></a>

```c
void(* set_ntf_filter )(struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf)
```

相关声明：[set_ntf_filter](#a91407e120e3a312061c8431fd3bb48a7)、[bt_map_mse_mas](P113_bt_map_mse_mas_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

设置通知过滤器（Set notification filter）回调。

## 114.2\_详细说明（Detailed Documentation）

<a id="a58392850c26d91c10a6ed35c7d41d6eb"></a>

### `abort`

```c
void(* bt_map_mse_mas_cb::abort) (struct bt_map_mse_mas *mse_mas, struct net_buf *buf)
```

中止（Abort）回调。

收到 OBEX `ABORT` 请求时调用。应用应使用 `bt_map_mse_mas_abort()` 作出响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `buf` | 包含请求头的缓冲区。 |

<a id="a1fd7e912c55a267e303e347bdd419ebe"></a>

### `connect`

```c
void(* bt_map_mse_mas_cb::connect) (struct bt_map_mse_mas *mse_mas, uint8_t version, uint16_t mopl, struct net_buf *buf)
```

连接（Connect）回调。

收到远端消息客户端设备（MCE）发送的 OBEX `CONNECT` 请求时调用。应用应使用 `bt_map_mse_mas_connect()` 作出响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `version` | 客户端请求的 OBEX 协议版本。 |
| `mopl` | 客户端请求的最大 OBEX 数据包长度。 |
| `buf` | 包含请求头（目标 UUID、支持的特性等）的缓冲区。 |

<a id="a0192c32ce2e08af30ba8288025ae0b55"></a>

### `disconnect`

```c
void(* bt_map_mse_mas_cb::disconnect) (struct bt_map_mse_mas *mse_mas, struct net_buf *buf)
```

断开连接（Disconnect）回调。

收到 OBEX `DISCONNECT` 请求时调用。应用应使用 `bt_map_mse_mas_disconnect()` 作出响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `buf` | 包含请求头的缓冲区。 |

<a id="aff9b5da1a558e79eaa744677437e66cc"></a>

### `get_convo_listing`

```c
void(* bt_map_mse_mas_cb::get_convo_listing) (struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf)
```

获取会话列表（Get conversation listing）回调。

收到获取会话列表（`GetConversationListing`）请求时调用。如果客户端请求继续传输，可能多次调用。应用应使用 `bt_map_mse_mas_get_convo_listing()` 作出响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `final` | 如果这是最后一个数据包，则为 `true`；如果后面还有数据，则为 `false`。 |
| `buf` | 包含过滤参数及头部的缓冲区。 |

<a id="a1b37e5006775590e91731e873c0c4dc9"></a>

### `get_folder_listing`

```c
void(* bt_map_mse_mas_cb::get_folder_listing) (struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf)
```

获取文件夹列表（Get folder listing）回调。

收到获取文件夹列表（`GetFolderListing`）请求时调用。如果客户端请求继续传输，可能多次调用。应用应使用 `bt_map_mse_mas_get_folder_listing()` 作出响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `final` | 如果这是最后一个数据包，则为 `true`；如果后面还有数据，则为 `false`。 |
| `buf` | 包含过滤参数及头部的缓冲区。 |

<a id="a6aae3db4af23f0408f328cac2b9fbf14"></a>

### `get_mas_inst_info`

```c
void(* bt_map_mse_mas_cb::get_mas_inst_info) (struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf)
```

获取 MAS 实例信息（Get MAS instance info）回调。

收到获取 MAS 实例信息（`GetMASInstanceInformation`）请求时调用。如果客户端请求继续传输，可能多次调用。应用应使用 `bt_map_mse_mas_get_mas_inst_info()` 作出响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `final` | 如果这是最后一个数据包，则为 `true`；如果后面还有数据，则为 `false`。 |
| `buf` | 包含实例 ID 及头部的缓冲区。 |

<a id="a47d93ccf18b704eaf8d0906e75b8ddff"></a>

### `get_msg`

```c
void(* bt_map_mse_mas_cb::get_msg) (struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf)
```

获取消息（Get message）回调。

收到获取消息（`GetMessage`）请求时调用。如果客户端请求继续传输，可能多次调用。应用应使用 `bt_map_mse_mas_get_msg()` 作出响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `final` | 如果这是最后一个数据包，则为 `true`；如果后面还有数据，则为 `false`。 |
| `buf` | 包含消息句柄、参数及头部的缓冲区。 |

<a id="ab3039d3b0e740e9eda1b3efd392916f8"></a>

### `get_msg_listing`

```c
void(* bt_map_mse_mas_cb::get_msg_listing) (struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf)
```

获取消息列表（Get message listing）回调。

收到获取消息列表（`GetMessageListing`）请求时调用。如果客户端请求继续传输，可能多次调用。应用应使用 `bt_map_mse_mas_get_msg_listing()` 作出响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `final` | 如果这是最后一个数据包，则为 `true`；如果后面还有数据，则为 `false`。 |
| `buf` | 包含文件夹名称、过滤参数及头部的缓冲区。 |

<a id="af016d7689a8546612c73bd41cdec6e5a"></a>

### `get_owner_status`

```c
void(* bt_map_mse_mas_cb::get_owner_status) (struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf)
```

获取所有者状态（Get owner status）回调。

收到获取所有者状态（`GetOwnerStatus`）请求时调用。如果客户端请求继续传输，可能多次调用。应用应使用 `bt_map_mse_mas_get_owner_status()` 作出响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `final` | 如果这是最后一个数据包，则为 `true`；如果后面还有数据，则为 `false`。 |
| `buf` | 包含头部的缓冲区。 |

<a id="a5d5246c3d8e3a229fdd6d33f01d48e50"></a>

### `l2cap_connected`

```c
void(* bt_map_mse_mas_cb::l2cap_connected) (struct bt_conn *conn, struct bt_map_mse_mas *mse_mas)
```

L2CAP 传输连接建立回调。

底层传输（L2CAP）连接建立时调用。此时尚未协商 OBEX 连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 蓝牙连接对象（Bluetooth connection object）。 |
| `mse_mas` | MAS 服务器实例。 |

<a id="a32dfc15ce0c67ef9b68d43c51a685668"></a>

### `l2cap_disconnected`

```c
void(* bt_map_mse_mas_cb::l2cap_disconnected) (struct bt_map_mse_mas *mse_mas)
```

L2CAP 传输连接断开回调。

底层传输（L2CAP）连接关闭时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |

<a id="a3113a29c5a6e7ba149bad09449cb5da4"></a>

### `push_msg`

```c
void(* bt_map_mse_mas_cb::push_msg) (struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf)
```

推送消息（Push message）回调。

收到推送消息（`PushMessage`）请求时调用。如果请求分片，可能多次调用。应用应使用 `bt_map_mse_mas_push_msg()` 作出响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `final` | 如果这是最后一个数据包，则为 `true`；如果后面还有数据，则为 `false`。 |
| `buf` | 包含消息数据（`bMessage` 格式）及头部的缓冲区。 |

<a id="a92d897fa7c8f9d9e42a5b8e18b25a7e1"></a>

### `rfcomm_connected`

```c
void(* bt_map_mse_mas_cb::rfcomm_connected) (struct bt_conn *conn, struct bt_map_mse_mas *mse_mas)
```

RFCOMM 传输连接建立回调。

底层传输（RFCOMM）连接建立时调用。此时尚未协商 OBEX 连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 蓝牙连接对象（Bluetooth connection object）。 |
| `mse_mas` | MAS 服务器实例。 |

<a id="a462a2826086f8ebc40617752c463bf83"></a>

### `rfcomm_disconnected`

```c
void(* bt_map_mse_mas_cb::rfcomm_disconnected) (struct bt_map_mse_mas *mse_mas)
```

RFCOMM 传输连接断开回调。

底层传输（RFCOMM）连接关闭时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |

<a id="a06897a7617ee1f68f56c1b230f9f12e9"></a>

### `set_folder`

```c
void(* bt_map_mse_mas_cb::set_folder) (struct bt_map_mse_mas *mse_mas, uint8_t flags, struct net_buf *buf)
```

设置文件夹（Set folder）回调。

收到设置文件夹（`SetFolder`）请求时调用。应用应使用 `bt_map_mse_mas_set_folder()` 作出响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `flags` | 导航标志，参见 `bt_map_set_folder_flags`。 |
| `buf` | 包含文件夹名称（用于 DOWN 操作）及头部的缓冲区。 |

<a id="a5fc25a4ad534e3490297faabcd86f51e"></a>

### `set_msg_status`

```c
void(* bt_map_mse_mas_cb::set_msg_status) (struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf)
```

设置消息状态（Set message status）回调。

收到设置消息状态（`SetMessageStatus`）请求时调用。如果请求分片，可能多次调用。应用应使用 `bt_map_mse_mas_set_msg_status()` 作出响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `final` | 如果这是最后一个数据包，则为 `true`；如果后面还有数据，则为 `false`。 |
| `buf` | 包含消息句柄、状态参数及头部的缓冲区。 |

<a id="a91407e120e3a312061c8431fd3bb48a7"></a>

### `set_ntf_filter`

```c
void(* bt_map_mse_mas_cb::set_ntf_filter) (struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf)
```

设置通知过滤器（Set notification filter）回调。

收到设置通知过滤器（`SetNotificationFilter`）请求时调用。如果请求分片，可能多次调用。应用应使用 `bt_map_mse_mas_set_ntf_filter()` 作出响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `final` | 如果这是最后一个数据包，则为 `true`；如果后面还有数据，则为 `false`。 |
| `buf` | 包含过滤掩码及头部的缓冲区。 |

<a id="a6d0489d861546f5e9501ff6527df7d3f"></a>

### `set_ntf_reg`

```c
void(* bt_map_mse_mas_cb::set_ntf_reg) (struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf)
```

设置通知注册（Set notification registration）回调。

收到设置通知注册（`SetNotificationRegistration`）请求时调用。如果请求分片，可能多次调用。应用应使用 `bt_map_mse_mas_set_ntf_reg()` 作出响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `final` | 如果这是最后一个数据包，则为 `true`；如果后面还有数据，则为 `false`。 |
| `buf` | 包含通知状态及头部的缓冲区。 |

<a id="a5094efadea33ad701eaad813fe2bde50"></a>

### `set_owner_status`

```c
void(* bt_map_mse_mas_cb::set_owner_status) (struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf)
```

设置所有者状态（Set owner status）回调。

收到设置所有者状态（`SetOwnerStatus`）请求时调用。如果请求分片，可能多次调用。应用应使用 `bt_map_mse_mas_set_owner_status()` 作出响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `final` | 如果这是最后一个数据包，则为 `true`；如果后面还有数据，则为 `false`。 |
| `buf` | 包含所有者状态数据及头部的缓冲区。 |

<a id="aed0b3894512dc0e3b363d3dd98b3dfbf"></a>

### `update_inbox`

```c
void(* bt_map_mse_mas_cb::update_inbox) (struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf)
```

更新收件箱（Update inbox）回调。

收到更新收件箱（`UpdateInbox`）请求时调用。如果请求分片，可能多次调用。应用应使用 `bt_map_mse_mas_update_inbox()` 作出响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `final` | 如果这是最后一个数据包，则为 `true`；如果后面还有数据，则为 `false`。 |
| `buf` | 包含头部的缓冲区。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/map.h`

## 114.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/map.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2classic_2map_8h_source.html)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_map_mse_mas](P113_bt_map_mse_mas_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [bt_map_mse_mas_abort()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#ga3eee467070483854e1a84a940ee031e2)
- [bt_map_mse_mas_connect()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#gadd1da4acdd8043aa542c0fe36259898f)
- [bt_map_mse_mas_disconnect()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#gabc3a8d9eb9dbc3fd028d39e4a262388b)
- [bt_map_mse_mas_get_convo_listing()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#gadeb8072cdca241b3ad15c2116733d155)
- [bt_map_mse_mas_get_folder_listing()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#ga8263ea5145edcfd277f73980a3fcea57)
- [bt_map_mse_mas_get_mas_inst_info()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#gab50e3d126e2d35e9b6724cf3112d0892)
- [bt_map_mse_mas_get_msg()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#ga852ae34e4f8b44fea3308a42baa15ec2)
- [bt_map_mse_mas_get_msg_listing()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#ga2833ef99d384109acf304532d1820a36)
- [bt_map_mse_mas_get_owner_status()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#ga37c155889cd0e2bb902da2bd25415509)
- [bt_map_mse_mas_push_msg()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#gabcd127dc45e03820079be0dc92066b89)
- [bt_map_mse_mas_set_folder()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#gac972589b96cd3931044f994d4c94cf20)
- [bt_map_set_folder_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga5678131af7da533ff8b751555542933e)
- [bt_map_mse_mas_set_msg_status()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#ga3cfbf0a8f1f1b6a730c401dac21e9f51)
- [bt_map_mse_mas_set_ntf_filter()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#ga3aacf3e78b40f06bbf17baada2c59e04)
- [bt_map_mse_mas_set_ntf_reg()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#ga55641e8681932d0e31021d3803625874)
- [bt_map_mse_mas_set_owner_status()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#ga275eff320f980230d8d80873ad0ef3ce)
- [bt_map_mse_mas_update_inbox()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#ga2c0ed0fdc8fee3f98e671c5ec187c8ed)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P113_bt_map_mse_mas_结构体.md) · [返回大纲](大纲.md) · [下一章](P115_bt_map_mse_mas_l2cap_server_结构体.md)
