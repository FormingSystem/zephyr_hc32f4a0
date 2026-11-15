---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-108
title: bt_map_mce_mas_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__map__mce__mas__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第108章\_bt\_map\_mce\_mas\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__map__mce__mas__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

消息访问配置文件（MAP）客户端的MAS回调。

```c
#include <zephyr/bluetooth/classic/map.h>
```

<a id="details"></a>

MAP 客户端 MAS 回调，用于处理 MAP 客户端 MAS 事件。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 108.1\_数据成员（Data Fields）

<a id="r_a2c1255b9c721c844222a98e8ab5c5301"></a>

```c
void(* rfcomm_connected )(struct bt_conn *conn, struct bt_map_mce_mas *mce_mas)
```

相关声明：[rfcomm_connected](#a2c1255b9c721c844222a98e8ab5c5301)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_map_mce_mas](P107_bt_map_mce_mas_结构体.md)。

RFCOMM 传输连接建立回调。

<a id="r_a3f245b9e735bca51f16b579dea049b71"></a>

```c
void(* rfcomm_disconnected )(struct bt_map_mce_mas *mce_mas)
```

相关声明：[rfcomm_disconnected](#a3f245b9e735bca51f16b579dea049b71)、[bt_map_mce_mas](P107_bt_map_mce_mas_结构体.md)。

RFCOMM 传输连接断开回调。

<a id="r_a6a5a53dd82f8f7ddce0fadc4284d9ebe"></a>

```c
void(* l2cap_connected )(struct bt_conn *conn, struct bt_map_mce_mas *mce_mas)
```

相关声明：[l2cap_connected](#a6a5a53dd82f8f7ddce0fadc4284d9ebe)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_map_mce_mas](P107_bt_map_mce_mas_结构体.md)。

L2CAP 传输连接建立回调。

<a id="r_abb01bd4ee41818a5c11de09035255ad5"></a>

```c
void(* l2cap_disconnected )(struct bt_map_mce_mas *mce_mas)
```

相关声明：[l2cap_disconnected](#abb01bd4ee41818a5c11de09035255ad5)、[bt_map_mce_mas](P107_bt_map_mce_mas_结构体.md)。

L2CAP 传输连接断开回调。

<a id="r_a41ff659151ea8d312ed178907005c9fa"></a>

```c
void(* connect )(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, uint8_t version, uint16_t mopl, struct net_buf *buf)
```

相关声明：[connect](#a41ff659151ea8d312ed178907005c9fa)、[bt_map_mce_mas](P107_bt_map_mce_mas_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

连接（Connect）回调。

<a id="r_adebef477e23b2534fb7f54665338b0e2"></a>

```c
void(* disconnect )(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[disconnect](#adebef477e23b2534fb7f54665338b0e2)、[bt_map_mce_mas](P107_bt_map_mce_mas_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

断开连接（Disconnect）回调。

<a id="r_adea73e4018513fe3f5443e2a4c3450dd"></a>

```c
void(* abort )(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[abort](#adea73e4018513fe3f5443e2a4c3450dd)、[bt_map_mce_mas](P107_bt_map_mce_mas_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

中止（Abort）回调。

<a id="r_a283872e83a71cc79e20c51fb1312b898"></a>

```c
void(* set_ntf_reg )(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[set_ntf_reg](#a283872e83a71cc79e20c51fb1312b898)、[bt_map_mce_mas](P107_bt_map_mce_mas_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

设置通知注册（Set notification registration）回调。

<a id="r_a3554be8e90ec9605a0a2524cb37e2561"></a>

```c
void(* set_folder )(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[set_folder](#a3554be8e90ec9605a0a2524cb37e2561)、[bt_map_mce_mas](P107_bt_map_mce_mas_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

设置文件夹（Set folder）回调。

<a id="r_aca7392666d7b4ca34c38654ee8b37a63"></a>

```c
void(* get_folder_listing )(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[get_folder_listing](#aca7392666d7b4ca34c38654ee8b37a63)、[bt_map_mce_mas](P107_bt_map_mce_mas_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

获取文件夹列表（Get folder listing）回调。

<a id="r_acdc05fac490ad32b5f197c673b46565f"></a>

```c
void(* get_msg_listing )(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[get_msg_listing](#acdc05fac490ad32b5f197c673b46565f)、[bt_map_mce_mas](P107_bt_map_mce_mas_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

获取消息列表（Get message listing）回调。

<a id="r_a42a9441ceab421f0ebd9accd8577ff05"></a>

```c
void(* get_msg )(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[get_msg](#a42a9441ceab421f0ebd9accd8577ff05)、[bt_map_mce_mas](P107_bt_map_mce_mas_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

获取消息（Get message）回调。

<a id="r_a1e11b4382657e6656b41058ba575d73d"></a>

```c
void(* set_msg_status )(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[set_msg_status](#a1e11b4382657e6656b41058ba575d73d)、[bt_map_mce_mas](P107_bt_map_mce_mas_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

设置消息状态（Set message status）回调。

<a id="r_aabecb70ffb005db1048f8615712a358f"></a>

```c
void(* push_msg )(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[push_msg](#aabecb70ffb005db1048f8615712a358f)、[bt_map_mce_mas](P107_bt_map_mce_mas_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

推送消息（Push message）回调。

<a id="r_a51523325824c0add586e97e4fc45b985"></a>

```c
void(* update_inbox )(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[update_inbox](#a51523325824c0add586e97e4fc45b985)、[bt_map_mce_mas](P107_bt_map_mce_mas_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

更新收件箱（Update inbox）回调。

<a id="r_a096e8d15124959cbbfa5c3961c44b55b"></a>

```c
void(* get_mas_inst_info )(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[get_mas_inst_info](#a096e8d15124959cbbfa5c3961c44b55b)、[bt_map_mce_mas](P107_bt_map_mce_mas_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

获取 MAS 实例信息（Get MAS instance info）回调。

<a id="r_aa74d509e4c1e792c1187aef27bfd5e8b"></a>

```c
void(* set_owner_status )(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[set_owner_status](#aa74d509e4c1e792c1187aef27bfd5e8b)、[bt_map_mce_mas](P107_bt_map_mce_mas_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

设置所有者状态（Set owner status）回调。

<a id="r_aa491f3f467f93536d8dcdb7897552d9b"></a>

```c
void(* get_owner_status )(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[get_owner_status](#aa491f3f467f93536d8dcdb7897552d9b)、[bt_map_mce_mas](P107_bt_map_mce_mas_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

获取所有者状态（Get owner status）回调。

<a id="r_adaebc7b993824d27757a9482e56a211e"></a>

```c
void(* get_convo_listing )(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[get_convo_listing](#adaebc7b993824d27757a9482e56a211e)、[bt_map_mce_mas](P107_bt_map_mce_mas_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

获取会话列表（Get conversation listing）回调。

<a id="r_a15c281a0eb09f8e249b629c30d8909d2"></a>

```c
void(* set_ntf_filter )(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[set_ntf_filter](#a15c281a0eb09f8e249b629c30d8909d2)、[bt_map_mce_mas](P107_bt_map_mce_mas_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

设置通知过滤器（Set notification filter）回调。

## 108.2\_详细说明（Detailed Documentation）

<a id="adea73e4018513fe3f5443e2a4c3450dd"></a>

### `abort`

```c
void(* bt_map_mce_mas_cb::abort) (struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf)
```

中止（Abort）回调。

收到对象交换（OBEX）`ABORT` 响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `rsp_code` | 响应码 `bt_obex_rsp_code`。 |
| `buf` | 包含响应头的缓冲区。 |

<a id="a41ff659151ea8d312ed178907005c9fa"></a>

### `connect`

```c
void(* bt_map_mce_mas_cb::connect) (struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, uint8_t version, uint16_t mopl, struct net_buf *buf)
```

连接（Connect）回调。

收到 OBEX `CONNECT` 响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `rsp_code` | 响应码 `bt_obex_rsp_code`；成功时为 `BT_OBEX_RSP_CODE_SUCCESS`。 |
| `version` | 服务器支持的 OBEX 协议版本。 |
| `mopl` | 服务器支持的最大 OBEX 数据包长度。 |
| `buf` | 包含附加响应头（连接 ID 等）的缓冲区。 |

<a id="adebef477e23b2534fb7f54665338b0e2"></a>

### `disconnect`

```c
void(* bt_map_mce_mas_cb::disconnect) (struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf)
```

断开连接（Disconnect）回调。

收到 OBEX `DISCONNECT` 响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `rsp_code` | 响应码 `bt_obex_rsp_code`。 |
| `buf` | 包含响应头的缓冲区。 |

<a id="adaebc7b993824d27757a9482e56a211e"></a>

### `get_convo_listing`

```c
void(* bt_map_mce_mas_cb::get_convo_listing) (struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf)
```

获取会话列表（Get conversation listing）回调。

收到获取会话列表（`GetConversationListing`）响应时调用。如果响应分片，则单个请求可能多次触发此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `rsp_code` | 响应码 `bt_obex_rsp_code`；传输部分数据时为 `BT_OBEX_RSP_CODE_CONTINUE`。 |
| `buf` | 包含会话列表 XML 数据及头部的缓冲区。 |

<a id="aca7392666d7b4ca34c38654ee8b37a63"></a>

### `get_folder_listing`

```c
void(* bt_map_mce_mas_cb::get_folder_listing) (struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf)
```

获取文件夹列表（Get folder listing）回调。

收到获取文件夹列表（`GetFolderListing`）响应时调用。如果响应分片，则单个请求可能多次触发此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `rsp_code` | 响应码 `bt_obex_rsp_code`；传输部分数据时为 `BT_OBEX_RSP_CODE_CONTINUE`。 |
| `buf` | 包含文件夹列表 XML 数据及头部的缓冲区。 |

<a id="a096e8d15124959cbbfa5c3961c44b55b"></a>

### `get_mas_inst_info`

```c
void(* bt_map_mce_mas_cb::get_mas_inst_info) (struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf)
```

获取 MAS 实例信息（Get MAS instance info）回调。

收到获取 MAS 实例信息（`GetMASInstanceInformation`）响应时调用。如果响应分片，则单个请求可能多次触发此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `rsp_code` | 响应码 `bt_obex_rsp_code`；传输部分数据时为 `BT_OBEX_RSP_CODE_CONTINUE`。 |
| `buf` | 包含实例信息 XML 数据及头部的缓冲区。 |

<a id="a42a9441ceab421f0ebd9accd8577ff05"></a>

### `get_msg`

```c
void(* bt_map_mce_mas_cb::get_msg) (struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf)
```

获取消息（Get message）回调。

收到获取消息（`GetMessage`）响应时调用。如果响应分片，则单个请求可能多次触发此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `rsp_code` | 响应码 `bt_obex_rsp_code`；传输部分数据时为 `BT_OBEX_RSP_CODE_CONTINUE`。 |
| `buf` | 包含消息的 `bMessage` 数据及头部的缓冲区。 |

<a id="acdc05fac490ad32b5f197c673b46565f"></a>

### `get_msg_listing`

```c
void(* bt_map_mce_mas_cb::get_msg_listing) (struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf)
```

获取消息列表（Get message listing）回调。

收到获取消息列表（`GetMessageListing`）响应时调用。如果响应分片，则单个请求可能多次触发此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `rsp_code` | 响应码 `bt_obex_rsp_code`；传输部分数据时为 `BT_OBEX_RSP_CODE_CONTINUE`。 |
| `buf` | 包含消息列表 XML 数据及头部的缓冲区。 |

<a id="aa491f3f467f93536d8dcdb7897552d9b"></a>

### `get_owner_status`

```c
void(* bt_map_mce_mas_cb::get_owner_status) (struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf)
```

获取所有者状态（Get owner status）回调。

收到获取所有者状态（`GetOwnerStatus`）响应时调用。如果响应分片，则单个请求可能多次触发此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `rsp_code` | 响应码 `bt_obex_rsp_code`；传输部分数据时为 `BT_OBEX_RSP_CODE_CONTINUE`。 |
| `buf` | 包含所有者状态数据及头部的缓冲区。 |

<a id="a6a5a53dd82f8f7ddce0fadc4284d9ebe"></a>

### `l2cap_connected`

```c
void(* bt_map_mce_mas_cb::l2cap_connected) (struct bt_conn *conn, struct bt_map_mce_mas *mce_mas)
```

L2CAP 传输连接建立回调。

底层传输（L2CAP）连接建立时调用。此时尚未协商 OBEX 连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 蓝牙连接对象（Bluetooth connection object）。 |
| `mce_mas` | MAS 客户端实例。 |

<a id="abb01bd4ee41818a5c11de09035255ad5"></a>

### `l2cap_disconnected`

```c
void(* bt_map_mce_mas_cb::l2cap_disconnected) (struct bt_map_mce_mas *mce_mas)
```

L2CAP 传输连接断开回调。

底层传输（L2CAP）连接关闭时调用。所有待处理操作均被取消。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |

<a id="aabecb70ffb005db1048f8615712a358f"></a>

### `push_msg`

```c
void(* bt_map_mce_mas_cb::push_msg) (struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf)
```

推送消息（Push message）回调。

收到推送消息（`PushMessage`）响应时调用。如果请求分片，可能多次调用，响应码为 `BT_OBEX_RSP_CODE_CONTINUE`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `rsp_code` | 响应码 `bt_obex_rsp_code`；部分上传时为 `BT_OBEX_RSP_CODE_CONTINUE`。 |
| `buf` | 包含消息句柄（成功时）及头部的缓冲区。 |

<a id="a2c1255b9c721c844222a98e8ab5c5301"></a>

### `rfcomm_connected`

```c
void(* bt_map_mce_mas_cb::rfcomm_connected) (struct bt_conn *conn, struct bt_map_mce_mas *mce_mas)
```

RFCOMM 传输连接建立回调。

底层传输（RFCOMM）连接建立时调用。此时尚未协商 OBEX 连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 蓝牙连接对象（Bluetooth connection object）。 |
| `mce_mas` | MAS 客户端实例。 |

<a id="a3f245b9e735bca51f16b579dea049b71"></a>

### `rfcomm_disconnected`

```c
void(* bt_map_mce_mas_cb::rfcomm_disconnected) (struct bt_map_mce_mas *mce_mas)
```

RFCOMM 传输连接断开回调。

底层传输（RFCOMM）连接关闭时调用。所有待处理操作均被取消。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |

<a id="a3554be8e90ec9605a0a2524cb37e2561"></a>

### `set_folder`

```c
void(* bt_map_mce_mas_cb::set_folder) (struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf)
```

设置文件夹（Set folder）回调。

收到设置文件夹（`SetFolder`）响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `rsp_code` | 响应码 `bt_obex_rsp_code`。 |
| `buf` | 包含响应头的缓冲区。 |

<a id="a1e11b4382657e6656b41058ba575d73d"></a>

### `set_msg_status`

```c
void(* bt_map_mce_mas_cb::set_msg_status) (struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf)
```

设置消息状态（Set message status）回调。

收到设置消息状态（`SetMessageStatus`）响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `rsp_code` | 响应码 `bt_obex_rsp_code`。 |
| `buf` | 包含响应头的缓冲区。 |

<a id="a15c281a0eb09f8e249b629c30d8909d2"></a>

### `set_ntf_filter`

```c
void(* bt_map_mce_mas_cb::set_ntf_filter) (struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf)
```

设置通知过滤器（Set notification filter）回调。

收到设置通知过滤器（`SetNotificationFilter`）响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `rsp_code` | 响应码 `bt_obex_rsp_code`。 |
| `buf` | 包含响应头的缓冲区。 |

<a id="a283872e83a71cc79e20c51fb1312b898"></a>

### `set_ntf_reg`

```c
void(* bt_map_mce_mas_cb::set_ntf_reg) (struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf)
```

设置通知注册（Set notification registration）回调。

收到设置通知注册（`SetNotificationRegistration`）响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `rsp_code` | 响应码 `bt_obex_rsp_code`。 |
| `buf` | 包含响应头的缓冲区。 |

<a id="aa74d509e4c1e792c1187aef27bfd5e8b"></a>

### `set_owner_status`

```c
void(* bt_map_mce_mas_cb::set_owner_status) (struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf)
```

设置所有者状态（Set owner status）回调。

收到设置所有者状态（`SetOwnerStatus`）响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `rsp_code` | 响应码 `bt_obex_rsp_code`。 |
| `buf` | 包含响应头的缓冲区。 |

<a id="a51523325824c0add586e97e4fc45b985"></a>

### `update_inbox`

```c
void(* bt_map_mce_mas_cb::update_inbox) (struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf)
```

更新收件箱（Update inbox）回调。

收到更新收件箱（`UpdateInbox`）响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `rsp_code` | 响应码 `bt_obex_rsp_code`。 |
| `buf` | 包含响应头的缓冲区。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/map.h`

## 108.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/map.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2classic_2map_8h_source.html)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_map_mce_mas](P107_bt_map_mce_mas_结构体.md)
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

[上一章](P107_bt_map_mce_mas_结构体.md) · [返回大纲](大纲.md) · [下一章](P109_bt_map_mce_mns_结构体.md)
