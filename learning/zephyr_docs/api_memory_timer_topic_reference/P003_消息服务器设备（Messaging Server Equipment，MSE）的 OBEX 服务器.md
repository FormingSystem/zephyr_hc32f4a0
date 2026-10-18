---
id: learning.zephyr-docs.api-memory-timer-topic-reference.page-3
title: 消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器

<a id="details"></a>

消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

<a id="r_bt_5Fmap_5Fmse_5Fmas_5Frfcomm_5Fserver"></a>

```c
struct bt_map_mse_mas_rfcomm_server
```

相关声明：[bt_map_mse_mas_rfcomm_server](../bluetooth_service_model_reference/P116_bt_map_mse_mas_rfcomm_server_结构体.md)。

消息访问配置文件（MAP）服务器的MAS RFCOMM服务器。

<a id="r_bt_5Fmap_5Fmse_5Fmas_5Fl2cap_5Fserver"></a>

```c
struct bt_map_mse_mas_l2cap_server
```

相关声明：[bt_map_mse_mas_l2cap_server](../bluetooth_service_model_reference/P115_bt_map_mse_mas_l2cap_server_结构体.md)。

消息访问配置文件（MAP）服务器的MAS L2CAP服务器。

<a id="r_bt_5Fmap_5Fmse_5Fmas_5Fcb"></a>

```c
struct bt_map_mse_mas_cb
```

相关声明：[bt_map_mse_mas_cb](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md)。

消息访问配置文件（MAP）服务器的MAS回调。

<a id="r_bt_5Fmap_5Fmse_5Fmas"></a>

```c
struct bt_map_mse_mas
```

相关声明：[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)。

消息访问配置文件（MAP）服务器的消息访问服务器（MAS）实例结构。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.2\_函数（Functions）

<a id="r_ga14815828dbf7163ab8fb0b3a8c0165b4"></a>

```c
int bt_map_mse_mas_register (struct bt_map_mse_mas *mse_mas, const struct bt_map_mse_mas_cb *cb)
```

相关声明：[bt_map_mse_mas_register](#ga14815828dbf7163ab8fb0b3a8c0165b4)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[bt_map_mse_mas_cb](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md)。

注册消息访问配置文件服务器（MAP Server）的消息访问服务器（MAS）。

<a id="r_ga670bebf0edd1e8d5f7a2de5403e042d0"></a>

```c
int bt_map_mse_mas_rfcomm_register (struct bt_map_mse_mas_rfcomm_server *server)
```

相关声明：[bt_map_mse_mas_rfcomm_register](#ga670bebf0edd1e8d5f7a2de5403e042d0)、[bt_map_mse_mas_rfcomm_server](../bluetooth_service_model_reference/P116_bt_map_mse_mas_rfcomm_server_结构体.md)。

注册 MAP 服务器的 MAS RFCOMM 服务器（Server）。

<a id="r_ga7db0773e3e0425f77e965fece30c3697"></a>

```c
int bt_map_mse_mas_rfcomm_disconnect (struct bt_map_mse_mas *mse_mas)
```

相关声明：[bt_map_mse_mas_rfcomm_disconnect](#ga7db0773e3e0425f77e965fece30c3697)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)。

通过 RFCOMM 断开 MAP 服务器 MAS 的连接。

<a id="r_ga031515fbb0ca110532f5a1e971a01739"></a>

```c
int bt_map_mse_mas_l2cap_register (struct bt_map_mse_mas_l2cap_server *server)
```

相关声明：[bt_map_mse_mas_l2cap_register](#ga031515fbb0ca110532f5a1e971a01739)、[bt_map_mse_mas_l2cap_server](../bluetooth_service_model_reference/P115_bt_map_mse_mas_l2cap_server_结构体.md)。

注册 MAP 服务器的 MAS L2CAP 服务器（Server）。

<a id="r_ga6df473fe69d8b3d183ee8385613f786f"></a>

```c
int bt_map_mse_mas_l2cap_disconnect (struct bt_map_mse_mas *mse_mas)
```

相关声明：[bt_map_mse_mas_l2cap_disconnect](#ga6df473fe69d8b3d183ee8385613f786f)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)。

通过 L2CAP 断开 MAP 服务器 MAS 的连接。

<a id="r_gab1c7678b39dad5309efde0b5950a997f"></a>

```c
struct net_buf * bt_map_mse_mas_create_pdu (struct bt_map_mse_mas *mse_mas, struct net_buf_pool *pool)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_map_mse_mas_create_pdu](#gab1c7678b39dad5309efde0b5950a997f)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

为 MAP 服务器 MAS 创建协议数据单元（PDU）。

<a id="r_gadd1da4acdd8043aa542c0fe36259898f"></a>

```c
int bt_map_mse_mas_connect (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_connect](#gadd1da4acdd8043aa542c0fe36259898f)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 OBEX 连接响应（Connect Response）。

<a id="r_gabc3a8d9eb9dbc3fd028d39e4a262388b"></a>

```c
int bt_map_mse_mas_disconnect (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_disconnect](#gabc3a8d9eb9dbc3fd028d39e4a262388b)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 OBEX 断开响应（Disconnect Response）。

<a id="r_ga3eee467070483854e1a84a940ee031e2"></a>

```c
int bt_map_mse_mas_abort (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_abort](#ga3eee467070483854e1a84a940ee031e2)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 OBEX 中止响应（Abort Response）。

<a id="r_gac972589b96cd3931044f994d4c94cf20"></a>

```c
int bt_map_mse_mas_set_folder (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_set_folder](#gac972589b96cd3931044f994d4c94cf20)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送设置文件夹响应（Set Folder Response）。

<a id="r_ga55641e8681932d0e31021d3803625874"></a>

```c
int bt_map_mse_mas_set_ntf_reg (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_set_ntf_reg](#ga55641e8681932d0e31021d3803625874)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送设置通知注册响应（Set Notification Registration Response）。

<a id="r_ga8263ea5145edcfd277f73980a3fcea57"></a>

```c
int bt_map_mse_mas_get_folder_listing (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_get_folder_listing](#ga8263ea5145edcfd277f73980a3fcea57)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取文件夹列表响应（Get Folder Listing Response）。

<a id="r_ga2833ef99d384109acf304532d1820a36"></a>

```c
int bt_map_mse_mas_get_msg_listing (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_get_msg_listing](#ga2833ef99d384109acf304532d1820a36)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取消息列表响应（Get Message Listing Response）。

<a id="r_ga852ae34e4f8b44fea3308a42baa15ec2"></a>

```c
int bt_map_mse_mas_get_msg (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_get_msg](#ga852ae34e4f8b44fea3308a42baa15ec2)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取消息响应（Get Message Response）。

<a id="r_ga3cfbf0a8f1f1b6a730c401dac21e9f51"></a>

```c
int bt_map_mse_mas_set_msg_status (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_set_msg_status](#ga3cfbf0a8f1f1b6a730c401dac21e9f51)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送设置消息状态响应（Set Message Status Response）。

<a id="r_gabcd127dc45e03820079be0dc92066b89"></a>

```c
int bt_map_mse_mas_push_msg (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_push_msg](#gabcd127dc45e03820079be0dc92066b89)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送推送消息响应（Push Message Response）。

<a id="r_ga2c0ed0fdc8fee3f98e671c5ec187c8ed"></a>

```c
int bt_map_mse_mas_update_inbox (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_update_inbox](#ga2c0ed0fdc8fee3f98e671c5ec187c8ed)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送更新收件箱响应（Update Inbox Response）。

<a id="r_gab50e3d126e2d35e9b6724cf3112d0892"></a>

```c
int bt_map_mse_mas_get_mas_inst_info (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_get_mas_inst_info](#gab50e3d126e2d35e9b6724cf3112d0892)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取 MAS 实例信息响应（Get MAS Instance Info Response）。

<a id="r_ga275eff320f980230d8d80873ad0ef3ce"></a>

```c
int bt_map_mse_mas_set_owner_status (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_set_owner_status](#ga275eff320f980230d8d80873ad0ef3ce)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送设置所有者状态响应（Set Owner Status Response）。

<a id="r_ga37c155889cd0e2bb902da2bd25415509"></a>

```c
int bt_map_mse_mas_get_owner_status (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_get_owner_status](#ga37c155889cd0e2bb902da2bd25415509)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取所有者状态响应（Get Owner Status Response）。

<a id="r_gadeb8072cdca241b3ad15c2116733d155"></a>

```c
int bt_map_mse_mas_get_convo_listing (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_get_convo_listing](#gadeb8072cdca241b3ad15c2116733d155)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取会话列表响应（Get Conversation Listing Response）。

<a id="r_ga3aacf3e78b40f06bbf17baada2c59e04"></a>

```c
int bt_map_mse_mas_set_ntf_filter (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_set_ntf_filter](#ga3aacf3e78b40f06bbf17baada2c59e04)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送设置通知过滤器响应（Set Notification Filter Response）。

## 3.3\_详细说明（Detailed Documentation）

<a id="ga3eee467070483854e1a84a940ee031e2"></a>

### `bt_map_mse_mas_abort()`

```c
int bt_map_mse_mas_abort ( struct bt_map_mse_mas * mse_mas, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送 OBEX 中止响应（Abort Response）。

响应远端消息客户端设备（MCE）发来的 OBEX ABORT 请求。从中止回调 bt_map_mse_mas_cb::abort 调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `rsp_code` | 响应码（Response Code）`bt_obex_rsp_code`；用 `BT_OBEX_RSP_CODE_SUCCESS` 表示接受。 |
| `buf` | 包含响应头部（Response Headers）的缓冲区。若为 `NULL`，发送默认响应。成功返回时，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gadd1da4acdd8043aa542c0fe36259898f"></a>

### `bt_map_mse_mas_connect()`

```c
int bt_map_mse_mas_connect ( struct bt_map_mse_mas * mse_mas, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送 OBEX 连接响应（Connect Response）。

响应远端消息客户端设备（MCE）发来的 OBEX CONNECT 请求。从连接回调 bt_map_mse_mas_cb::connect 调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `rsp_code` | 响应码（Response Code）`bt_obex_rsp_code`；用 `BT_OBEX_RSP_CODE_SUCCESS` 表示接受。 |
| `buf` | 包含响应头部（Response Headers）的缓冲区，例如 WHO、连接 ID 等。若为 `NULL`，发送默认响应。成功返回时，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gab1c7678b39dad5309efde0b5950a997f"></a>

### `bt_map_mse_mas_create_pdu()`

```c
struct net_buf * bt_map_mse_mas_create_pdu ( struct bt_map_mse_mas * mse_mas, struct net_buf_pool * pool )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

为 MAP 服务器 MAS 创建协议数据单元（PDU）。

分配用于构造 MAP 响应包的缓冲区。缓冲区大小根据协商后的最大传输单元（MTU）确定。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `pool` | 用于分配的缓冲池（Buffer Pool）；为 `NULL` 时使用默认缓冲池。 |

**返回（Returns）**：返回值：已分配的缓冲区（Allocated Buffer）；分配失败返回 `NULL`。

<a id="gabc3a8d9eb9dbc3fd028d39e4a262388b"></a>

### `bt_map_mse_mas_disconnect()`

```c
int bt_map_mse_mas_disconnect ( struct bt_map_mse_mas * mse_mas, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送 OBEX 断开响应（Disconnect Response）。

响应远端消息客户端设备（MCE）发来的 OBEX DISCONNECT 请求。从断开连接回调 bt_map_mse_mas_cb::disconnect 调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `rsp_code` | 响应码（Response Code）`bt_obex_rsp_code`；用 `BT_OBEX_RSP_CODE_SUCCESS` 表示接受。 |
| `buf` | 包含响应头（Response Headers）的缓冲区。返回成功时，函数已接管 buf 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gadeb8072cdca241b3ad15c2116733d155"></a>

### `bt_map_mse_mas_get_convo_listing()`

```c
int bt_map_mse_mas_get_convo_listing ( struct bt_map_mse_mas * mse_mas, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送获取会话列表响应（Get Conversation Listing Response）。

响应远端消息客户端设备（MCE）发来的 GetConversationListing 请求。可以多次调用，以发送分片响应（Fragmented Response）。从获取会话列表回调 bt_map_mse_mas_cb::get_convo_listing 调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `rsp_code` | 响应码（Response Code）`bt_obex_rsp_code`；部分完成使用 `BT_OBEX_RSP_CODE_CONTINUE`，全部完成使用 `BT_OBEX_RSP_CODE_SUCCESS`。 |
| `buf` | 包含会话列表 XML 数据（Conversation Listing XML Data）及头部的缓冲区。返回成功时，函数已接管 buf 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga8263ea5145edcfd277f73980a3fcea57"></a>

### `bt_map_mse_mas_get_folder_listing()`

```c
int bt_map_mse_mas_get_folder_listing ( struct bt_map_mse_mas * mse_mas, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送获取文件夹列表响应（Get Folder Listing Response）。

响应远端消息客户端设备（MCE）发来的 GetFolderListing 请求。可以多次调用，以发送分片响应（Fragmented Response）。从获取文件夹列表回调 bt_map_mse_mas_cb::get_folder_listing 调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `rsp_code` | 响应码（Response Code）`bt_obex_rsp_code`；部分完成使用 `BT_OBEX_RSP_CODE_CONTINUE`，全部完成使用 `BT_OBEX_RSP_CODE_SUCCESS`。 |
| `buf` | 包含文件夹列表 XML 数据（Folder Listing XML Data）及头部的缓冲区。返回成功时，函数已接管 buf 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gab50e3d126e2d35e9b6724cf3112d0892"></a>

### `bt_map_mse_mas_get_mas_inst_info()`

```c
int bt_map_mse_mas_get_mas_inst_info ( struct bt_map_mse_mas * mse_mas, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送获取 MAS 实例信息响应（Get MAS Instance Info Response）。

响应远端消息客户端设备（MCE）发来的 GetMASInstanceInformation 请求。可以多次调用，以发送分片响应（Fragmented Response）。从获取 MAS 实例信息回调 bt_map_mse_mas_cb::get_mas_inst_info 调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `rsp_code` | 响应码（Response Code）`bt_obex_rsp_code`；部分完成使用 `BT_OBEX_RSP_CODE_CONTINUE`，全部完成使用 `BT_OBEX_RSP_CODE_SUCCESS`。 |
| `buf` | 包含实例信息 XML 数据（Instance Information XML Data）及头部的缓冲区。返回成功时，函数已接管 buf 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga852ae34e4f8b44fea3308a42baa15ec2"></a>

### `bt_map_mse_mas_get_msg()`

```c
int bt_map_mse_mas_get_msg ( struct bt_map_mse_mas * mse_mas, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送获取消息响应（Get Message Response）。

响应远端消息客户端设备（MCE）发来的 GetMessage 请求。可以多次调用，以发送分片响应（Fragmented Response）。从获取消息回调 bt_map_mse_mas_cb::get_msg 调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `rsp_code` | 响应码（Response Code）`bt_obex_rsp_code`；部分完成使用 `BT_OBEX_RSP_CODE_CONTINUE`，全部完成使用 `BT_OBEX_RSP_CODE_SUCCESS`。 |
| `buf` | 包含消息 bMessage 数据及头部的缓冲区。返回成功时，函数已接管 buf 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga2833ef99d384109acf304532d1820a36"></a>

### `bt_map_mse_mas_get_msg_listing()`

```c
int bt_map_mse_mas_get_msg_listing ( struct bt_map_mse_mas * mse_mas, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送获取消息列表响应（Get Message Listing Response）。

响应远端消息客户端设备（MCE）发来的 GetMessageListing 请求。可以多次调用，以发送分片响应（Fragmented Response）。从获取消息列表回调 bt_map_mse_mas_cb::get_msg_listing 调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `rsp_code` | 响应码（Response Code）`bt_obex_rsp_code`；部分完成使用 `BT_OBEX_RSP_CODE_CONTINUE`，全部完成使用 `BT_OBEX_RSP_CODE_SUCCESS`。 |
| `buf` | 包含消息列表 XML 数据（Message Listing XML Data）及头部的缓冲区。返回成功时，函数已接管 buf 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga37c155889cd0e2bb902da2bd25415509"></a>

### `bt_map_mse_mas_get_owner_status()`

```c
int bt_map_mse_mas_get_owner_status ( struct bt_map_mse_mas * mse_mas, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送获取所有者状态响应（Get Owner Status Response）。

响应远端消息客户端设备（MCE）发来的 GetOwnerStatus 请求。可以多次调用，以发送分片响应（Fragmented Response）。从获取所有者状态回调 bt_map_mse_mas_cb::get_owner_status 调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `rsp_code` | 响应码（Response Code）`bt_obex_rsp_code`；部分完成使用 `BT_OBEX_RSP_CODE_CONTINUE`，全部完成使用 `BT_OBEX_RSP_CODE_SUCCESS`。 |
| `buf` | 包含所有者状态数据（Owner Status Data）及头部的缓冲区。返回成功时，函数已接管 buf 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga6df473fe69d8b3d183ee8385613f786f"></a>

### `bt_map_mse_mas_l2cap_disconnect()`

```c
int bt_map_mse_mas_l2cap_disconnect ( struct bt_map_mse_mas * mse_mas)
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

通过 L2CAP 断开 MAP 服务器 MAS 的连接。

关闭 L2CAP 传输连接（Transport Connection）。成功时，调用断开回调 bt_map_mse_mas_cb::l2cap_disconnected。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga031515fbb0ca110532f5a1e971a01739"></a>

### `bt_map_mse_mas_l2cap_register()`

```c
int bt_map_mse_mas_l2cap_register ( struct bt_map_mse_mas_l2cap_server * server)
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

注册 MAP 服务器的 MAS L2CAP 服务器（Server）。

注册 L2CAP 服务器，以接受传入的 MAS 连接。协议／服务复用器值（PSM）可以自动分配，也可以指定。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | 已配置 `accept` 接受回调的 L2CAP 服务器结构体（Server Structure）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gabcd127dc45e03820079be0dc92066b89"></a>

### `bt_map_mse_mas_push_msg()`

```c
int bt_map_mse_mas_push_msg ( struct bt_map_mse_mas * mse_mas, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送推送消息响应（Push Message Response）。

响应远端消息客户端设备（MCE）发来的 PushMessage 请求。请求被分片时，可以多次调用。从推送消息回调 bt_map_mse_mas_cb::push_msg 调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `rsp_code` | 响应码（Response Code）`bt_obex_rsp_code`；部分完成使用 `BT_OBEX_RSP_CODE_CONTINUE`，全部完成使用 `BT_OBEX_RSP_CODE_SUCCESS`。 |
| `buf` | 包含消息句柄（Message Handle，仅成功时）及头部的缓冲区。返回成功时，函数已接管 buf 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga14815828dbf7163ab8fb0b3a8c0165b4"></a>

### `bt_map_mse_mas_register()`

```c
int bt_map_mse_mas_register ( struct bt_map_mse_mas * mse_mas, const struct bt_map_mse_mas_cb * cb )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

注册消息访问配置文件服务器（MAP Server）的消息访问服务器（MAS）。

将回调表（Callback Table）关联到服务器对象，并将其注册到底层 OBEX 服务器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `cb` | 指向回调结构体（Callback Structure）的指针，必须在服务器的整个生命周期内保持有效。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga7db0773e3e0425f77e965fece30c3697"></a>

### `bt_map_mse_mas_rfcomm_disconnect()`

```c
int bt_map_mse_mas_rfcomm_disconnect ( struct bt_map_mse_mas * mse_mas)
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

通过 RFCOMM 断开 MAP 服务器 MAS 的连接。

关闭 RFCOMM 传输连接（Transport Connection）。成功时，调用断开回调 bt_map_mse_mas_cb::rfcomm_disconnected。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga670bebf0edd1e8d5f7a2de5403e042d0"></a>

### `bt_map_mse_mas_rfcomm_register()`

```c
int bt_map_mse_mas_rfcomm_register ( struct bt_map_mse_mas_rfcomm_server * server)
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

注册 MAP 服务器的 MAS RFCOMM 服务器（Server）。

注册 RFCOMM 服务器，以接受传入的 MAS 连接。服务器通道（Server Channel）可以自动分配，也可以指定。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | 已配置 `accept` 接受回调的 RFCOMM 服务器结构体（Server Structure）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gac972589b96cd3931044f994d4c94cf20"></a>

### `bt_map_mse_mas_set_folder()`

```c
int bt_map_mse_mas_set_folder ( struct bt_map_mse_mas * mse_mas, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送设置文件夹响应（Set Folder Response）。

响应远端消息客户端设备（MCE）发来的 SetPath 请求。从设置文件夹回调 bt_map_mse_mas_cb::set_folder 调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `rsp_code` | 响应码 `bt_obex_rsp_code`；成功时为 `BT_OBEX_RSP_CODE_SUCCESS`。 |
| `buf` | 包含响应头部（Response Headers）的缓冲区。若为 `NULL`，发送默认响应。成功返回时，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga3cfbf0a8f1f1b6a730c401dac21e9f51"></a>

### `bt_map_mse_mas_set_msg_status()`

```c
int bt_map_mse_mas_set_msg_status ( struct bt_map_mse_mas * mse_mas, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送设置消息状态响应（Set Message Status Response）。

响应远端消息客户端设备（MCE）发来的 SetMessageStatus 请求。从设置消息状态回调 bt_map_mse_mas_cb::set_msg_status 调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `rsp_code` | 响应码 `bt_obex_rsp_code`；成功时为 `BT_OBEX_RSP_CODE_SUCCESS`。 |
| `buf` | 包含响应头部（Response Headers）的缓冲区。若为 `NULL`，发送默认响应。成功返回时，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga3aacf3e78b40f06bbf17baada2c59e04"></a>

### `bt_map_mse_mas_set_ntf_filter()`

```c
int bt_map_mse_mas_set_ntf_filter ( struct bt_map_mse_mas * mse_mas, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送设置通知过滤器响应（Set Notification Filter Response）。

响应远端消息客户端设备（MCE）发来的 SetNotificationFilter 请求。从设置通知过滤器回调 bt_map_mse_mas_cb::set_ntf_filter 调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `rsp_code` | 响应码 `bt_obex_rsp_code`；成功时为 `BT_OBEX_RSP_CODE_SUCCESS`。 |
| `buf` | 包含响应头部（Response Headers）的缓冲区。若为 `NULL`，发送默认响应。成功返回时，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga55641e8681932d0e31021d3803625874"></a>

### `bt_map_mse_mas_set_ntf_reg()`

```c
int bt_map_mse_mas_set_ntf_reg ( struct bt_map_mse_mas * mse_mas, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送设置通知注册响应（Set Notification Registration Response）。

响应远端消息客户端设备（MCE）发来的 SetNotificationRegistration 请求。从设置通知注册回调 bt_map_mse_mas_cb::set_ntf_reg 调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `rsp_code` | 响应码 `bt_obex_rsp_code`；成功时为 `BT_OBEX_RSP_CODE_SUCCESS`。 |
| `buf` | 包含响应头部（Response Headers）的缓冲区。若为 `NULL`，发送默认响应。成功返回时，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga275eff320f980230d8d80873ad0ef3ce"></a>

### `bt_map_mse_mas_set_owner_status()`

```c
int bt_map_mse_mas_set_owner_status ( struct bt_map_mse_mas * mse_mas, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送设置所有者状态响应（Set Owner Status Response）。

响应远端消息客户端设备（MCE）发来的 SetOwnerStatus 请求。从设置所有者状态回调 bt_map_mse_mas_cb::set_owner_status 调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `rsp_code` | 响应码 `bt_obex_rsp_code`；成功时为 `BT_OBEX_RSP_CODE_SUCCESS`。 |
| `buf` | 包含响应头部（Response Headers）的缓冲区。若为 `NULL`，发送默认响应。成功返回时，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga2c0ed0fdc8fee3f98e671c5ec187c8ed"></a>

### `bt_map_mse_mas_update_inbox()`

```c
int bt_map_mse_mas_update_inbox ( struct bt_map_mse_mas * mse_mas, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送更新收件箱响应（Update Inbox Response）。

响应远端消息客户端设备（MCE）发来的 UpdateInbox 请求。从更新收件箱回调 bt_map_mse_mas_cb::update_inbox 调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mas` | MAS 服务器实例。 |
| `rsp_code` | 响应码 `bt_obex_rsp_code`；成功时为 `BT_OBEX_RSP_CODE_SUCCESS`。 |
| `buf` | 包含响应头部（Response Headers）的缓冲区。若为 `NULL`，发送默认响应。成功返回时，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。


## 3.4\_原页交叉引用（Cross References）

- [bt_map_mse_mas_rfcomm_server](../bluetooth_service_model_reference/P116_bt_map_mse_mas_rfcomm_server_结构体.md)
- [bt_map_mse_mas_l2cap_server](../bluetooth_service_model_reference/P115_bt_map_mse_mas_l2cap_server_结构体.md)
- [bt_map_mse_mas_cb](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md)
- [bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [zephyr/bluetooth/classic/map.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2classic_2map_8h.html)
- [bt_map_mse_mas_cb::abort](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a58392850c26d91c10a6ed35c7d41d6eb)
- [bt_obex_rsp_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga81b84c24a976c6c13d33eb23b0b10ae9)
- [BT_OBEX_RSP_CODE_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9af449d3c85fbec550c76e29287a626789)
- [bt_map_mse_mas_cb::connect](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a1fd7e912c55a267e303e347bdd419ebe)
- [bt_map_mse_mas_cb::disconnect](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a0192c32ce2e08af30ba8288025ae0b55)
- [bt_map_mse_mas_cb::get_convo_listing](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#aff9b5da1a558e79eaa744677437e66cc)
- [BT_OBEX_RSP_CODE_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a7e38ca653283f53b62fa4b21f48d998a)
- [bt_map_mse_mas_cb::get_folder_listing](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a1b37e5006775590e91731e873c0c4dc9)
- [bt_map_mse_mas_cb::get_mas_inst_info](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a6aae3db4af23f0408f328cac2b9fbf14)
- [bt_map_mse_mas_cb::get_msg](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a47d93ccf18b704eaf8d0906e75b8ddff)
- [bt_map_mse_mas_cb::get_msg_listing](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#ab3039d3b0e740e9eda1b3efd392916f8)
- [bt_map_mse_mas_cb::get_owner_status](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#af016d7689a8546612c73bd41cdec6e5a)
- [bt_map_mse_mas_cb::l2cap_disconnected](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a32dfc15ce0c67ef9b68d43c51a685668)
- [bt_map_mse_mas_cb::push_msg](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a3113a29c5a6e7ba149bad09449cb5da4)
- [bt_map_mse_mas_cb::rfcomm_disconnected](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a462a2826086f8ebc40617752c463bf83)
- [bt_map_mse_mas_cb::set_folder](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a06897a7617ee1f68f56c1b230f9f12e9)
- [bt_map_mse_mas_cb::set_msg_status](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a5fc25a4ad534e3490297faabcd86f51e)
- [bt_map_mse_mas_cb::set_ntf_filter](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a91407e120e3a312061c8431fd3bb48a7)
- [bt_map_mse_mas_cb::set_ntf_reg](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a6d0489d861546f5e9501ff6527df7d3f)
- [bt_map_mse_mas_cb::set_owner_status](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a5094efadea33ad701eaad813fe2bde50)
- [bt_map_mse_mas_cb::update_inbox](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#aed0b3894512dc0e3b363d3dd98b3dfbf)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P002_BAP 单播客户端 API（Unicast Client APIs）.md) · [返回大纲](大纲.md) · [下一章](P004_EM32 时钟门控标识符（Clock Gating IDs）.md)
