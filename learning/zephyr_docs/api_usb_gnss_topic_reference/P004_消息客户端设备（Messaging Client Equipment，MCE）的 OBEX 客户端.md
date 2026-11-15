---
id: learning.zephyr-docs.api-usb-gnss-topic-reference.page-4
title: 消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mas.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mas.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端

<a id="details"></a>

消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.1\_数据结构（Data Structures）

<a id="r_bt_5Fmap_5Fmce_5Fmas_5Fcb"></a>

```c
struct bt_map_mce_mas_cb
```

相关声明：[bt_map_mce_mas_cb](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md)。

消息访问配置文件（MAP）客户端的MAS回调。

<a id="r_bt_5Fmap_5Fmce_5Fmas"></a>

```c
struct bt_map_mce_mas
```

相关声明：[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)。

消息访问配置文件（MAP）客户端的消息访问服务器（MAS）实例结构。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.2\_函数（Functions）

<a id="r_ga04bf8d4d99165e7cf49613fe82432ca7"></a>

```c
int bt_map_mce_mas_rfcomm_connect (struct bt_conn *conn, struct bt_map_mce_mas *mce_mas, const struct bt_map_mce_mas_cb *cb, uint8_t channel)
```

相关声明：[bt_map_mce_mas_rfcomm_connect](#ga04bf8d4d99165e7cf49613fe82432ca7)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[bt_map_mce_mas_cb](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通过 RFCOMM 连接 MAP 客户端的消息访问服务（MAS）。

<a id="r_ga3202aee97828ecd8ed6f39f9eb6c98f2"></a>

```c
int bt_map_mce_mas_rfcomm_disconnect (struct bt_map_mce_mas *mce_mas)
```

相关声明：[bt_map_mce_mas_rfcomm_disconnect](#ga3202aee97828ecd8ed6f39f9eb6c98f2)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)。

通过 RFCOMM 断开 MAP 客户端的消息访问服务（MAS）连接。

<a id="r_ga539c08b47cc73a23d24bd54dcb5d6dc4"></a>

```c
int bt_map_mce_mas_l2cap_connect (struct bt_conn *conn, struct bt_map_mce_mas *mce_mas, const struct bt_map_mce_mas_cb *cb, uint16_t psm)
```

相关声明：[bt_map_mce_mas_l2cap_connect](#ga539c08b47cc73a23d24bd54dcb5d6dc4)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[bt_map_mce_mas_cb](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

通过 L2CAP 连接 MAP 客户端的消息访问服务（MAS）。

<a id="r_ga1a00c2b646b9a10c3deb6f4953f04683"></a>

```c
int bt_map_mce_mas_l2cap_disconnect (struct bt_map_mce_mas *mce_mas)
```

相关声明：[bt_map_mce_mas_l2cap_disconnect](#ga1a00c2b646b9a10c3deb6f4953f04683)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)。

通过 L2CAP 断开 MAP 客户端的消息访问服务（MAS）连接。

<a id="r_ga666d58fd65852372fa22328b6cd9aa82"></a>

```c
struct net_buf * bt_map_mce_mas_create_pdu (struct bt_map_mce_mas *mce_mas, struct net_buf_pool *pool)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_map_mce_mas_create_pdu](#ga666d58fd65852372fa22328b6cd9aa82)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

为 MAP 客户端的消息访问服务（MAS）创建协议数据单元（PDU）。

<a id="r_ga01d1677204f204feb2474a61bfcc118a"></a>

```c
int bt_map_mce_mas_connect (struct bt_map_mce_mas *mce_mas, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_connect](#ga01d1677204f204feb2474a61bfcc118a)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送对象交换协议（OBEX）连接请求（Connect Request）。

<a id="r_ga0c58e5c7f70c15409ae9241d0b412400"></a>

```c
int bt_map_mce_mas_disconnect (struct bt_map_mce_mas *mce_mas, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_disconnect](#ga0c58e5c7f70c15409ae9241d0b412400)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 OBEX 断开请求（Disconnect Request）。

<a id="r_gaf9836663a18ecc62b5330a1682f4b42e"></a>

```c
int bt_map_mce_mas_abort (struct bt_map_mce_mas *mce_mas, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_abort](#gaf9836663a18ecc62b5330a1682f4b42e)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 OBEX 中止请求（Abort Request）。

<a id="r_ga9e6640177b225a5b7448cde8a17de4f0"></a>

```c
int bt_map_mce_mas_set_folder (struct bt_map_mce_mas *mce_mas, uint8_t flags, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_set_folder](#ga9e6640177b225a5b7448cde8a17de4f0)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送设置文件夹请求（Set Folder Request）。

<a id="r_gad528c35977847525d781a39c50a3e793"></a>

```c
int bt_map_mce_mas_set_ntf_reg (struct bt_map_mce_mas *mce_mas, bool final, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_set_ntf_reg](#gad528c35977847525d781a39c50a3e793)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送设置通知注册请求（Set Notification Registration Request）。

<a id="r_ga54fa7e185e5d949bec434935f51ae9fb"></a>

```c
int bt_map_mce_mas_get_folder_listing (struct bt_map_mce_mas *mce_mas, bool final, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_get_folder_listing](#ga54fa7e185e5d949bec434935f51ae9fb)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取文件夹列表请求（Get Folder Listing Request）。

<a id="r_gaf146e16f1b7950db4b5418bd27269ebb"></a>

```c
int bt_map_mce_mas_get_msg_listing (struct bt_map_mce_mas *mce_mas, bool final, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_get_msg_listing](#gaf146e16f1b7950db4b5418bd27269ebb)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取消息列表请求（Get Message Listing Request）。

<a id="r_ga39795b7002cf40984b130d38179a5472"></a>

```c
int bt_map_mce_mas_get_msg (struct bt_map_mce_mas *mce_mas, bool final, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_get_msg](#ga39795b7002cf40984b130d38179a5472)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取消息请求（Get Message Request）。

<a id="r_gaa03c3ea1d6ec10d02412b4525dd3ffe5"></a>

```c
int bt_map_mce_mas_set_msg_status (struct bt_map_mce_mas *mce_mas, bool final, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_set_msg_status](#gaa03c3ea1d6ec10d02412b4525dd3ffe5)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送设置消息状态请求（Set Message Status Request）。

<a id="r_ga54a2552080933e12b6b871bc9f898fce"></a>

```c
int bt_map_mce_mas_push_msg (struct bt_map_mce_mas *mce_mas, bool final, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_push_msg](#ga54a2552080933e12b6b871bc9f898fce)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送推送消息请求（Push Message Request）。

<a id="r_gae91fb531b7164b389994b9391fa8e51e"></a>

```c
int bt_map_mce_mas_update_inbox (struct bt_map_mce_mas *mce_mas, bool final, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_update_inbox](#gae91fb531b7164b389994b9391fa8e51e)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送更新收件箱请求（Update Inbox Request）。

<a id="r_gabbe39f067872a6c008269d483a97d234"></a>

```c
int bt_map_mce_mas_get_mas_inst_info (struct bt_map_mce_mas *mce_mas, bool final, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_get_mas_inst_info](#gabbe39f067872a6c008269d483a97d234)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取 MAS 实例信息请求（Get MAS Instance Info Request）。

<a id="r_ga3b1dc36240679618c98df515a351a5e7"></a>

```c
int bt_map_mce_mas_set_owner_status (struct bt_map_mce_mas *mce_mas, bool final, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_set_owner_status](#ga3b1dc36240679618c98df515a351a5e7)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送设置所有者状态请求（Set Owner Status Request）。

<a id="r_ga2206f238364c04e180153c5cff10de94"></a>

```c
int bt_map_mce_mas_get_owner_status (struct bt_map_mce_mas *mce_mas, bool final, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_get_owner_status](#ga2206f238364c04e180153c5cff10de94)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取所有者状态请求（Get Owner Status Request）。

<a id="r_gabdd72751375fa9a0aa1f99e75137cb9e"></a>

```c
int bt_map_mce_mas_get_convo_listing (struct bt_map_mce_mas *mce_mas, bool final, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_get_convo_listing](#gabdd72751375fa9a0aa1f99e75137cb9e)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取会话列表请求（Get Conversation Listing Request）。

<a id="r_ga28b33d6c38af9479e56e9c2c2c0f795a"></a>

```c
int bt_map_mce_mas_set_ntf_filter (struct bt_map_mce_mas *mce_mas, bool final, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_set_ntf_filter](#ga28b33d6c38af9479e56e9c2c2c0f795a)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送设置通知过滤器请求（Set Notification Filter Request）。

## 4.3\_详细说明（Detailed Documentation）

<a id="gaf9836663a18ecc62b5330a1682f4b42e"></a>

### `bt_map_mce_mas_abort()`

```c
int bt_map_mce_mas_abort ( struct bt_map_mce_mas * mce_mas, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送 OBEX 中止请求（Abort Request）。

中止当前正在进行的操作（Abort）。收到 OBEX 中止响应后，将调用中止回调 `bt_map_mce_mas_cb::abort`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `buf` | 包含中止头部（Abort Headers）的缓冲区，例如连接 ID 等。若为 `NULL`，发送默认中止请求。成功返回时，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga01d1677204f204feb2474a61bfcc118a"></a>

### `bt_map_mce_mas_connect()`

```c
int bt_map_mce_mas_connect ( struct bt_map_mce_mas * mce_mas, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送对象交换协议（OBEX）连接请求（Connect Request）。

发起与 MAS 的 OBEX 会话建立（Session Establishment）。必须在传输连接建立之后调用。收到 OBEX 连接响应后，将调用连接回调 `bt_map_mce_mas_cb::connect`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `buf` | 包含连接头部（Connect Headers）的缓冲区，例如目标 UUID、支持的功能等。为 `NULL` 时发送默认连接请求。若返回成功，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga666d58fd65852372fa22328b6cd9aa82"></a>

### `bt_map_mce_mas_create_pdu()`

```c
struct net_buf * bt_map_mce_mas_create_pdu ( struct bt_map_mce_mas * mce_mas, struct net_buf_pool * pool )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

为 MAP 客户端的消息访问服务（MAS）创建协议数据单元（PDU）。

分配用于构造消息访问配置文件（MAP）请求包的缓冲区。缓冲区大小根据协商后的最大传输单元（MTU）确定。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `pool` | 用于分配的缓冲池（Buffer Pool）；为 `NULL` 时使用默认缓冲池。 |

**返回（Returns）**：返回值：已分配的缓冲区（Allocated Buffer）；分配失败返回 `NULL`。

<a id="ga0c58e5c7f70c15409ae9241d0b412400"></a>

### `bt_map_mce_mas_disconnect()`

```c
int bt_map_mce_mas_disconnect ( struct bt_map_mce_mas * mce_mas, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送 OBEX 断开请求（Disconnect Request）。

发起 OBEX 会话终止（Session Termination）。收到 OBEX 断开响应后，将调用断开回调 `bt_map_mce_mas_cb::disconnect`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `buf` | 包含断开头部（Disconnect Headers）的缓冲区，例如连接 ID 等。若为 `NULL`，发送默认断开请求。成功返回时，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gabdd72751375fa9a0aa1f99e75137cb9e"></a>

### `bt_map_mce_mas_get_convo_listing()`

```c
int bt_map_mce_mas_get_convo_listing ( struct bt_map_mce_mas * mce_mas, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送获取会话列表请求（Get Conversation Listing Request）。

获取会话列表（Conversation Listing）。收到 `get_convo_listing` 响应后，将调用 `bt_map_mce_mas_cb::get_convo_listing` 回调，可能调用多次。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `final` | 如果这是最后一个数据包，则为 `true`；如果后面还有数据，则为 `false`。 |
| `buf` | 包含过滤参数（Filter Parameters）和头部的缓冲区。初始请求必须包含连接 ID（Connection ID）和类型头部（Type Header）。若返回成功，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga54fa7e185e5d949bec434935f51ae9fb"></a>

### `bt_map_mce_mas_get_folder_listing()`

```c
int bt_map_mce_mas_get_folder_listing ( struct bt_map_mce_mas * mce_mas, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送获取文件夹列表请求（Get Folder Listing Request）。

获取当前文件夹中的子文件夹列表（Subfolder Listing）。收到 `get_folder_listing` 响应后，将调用 `bt_map_mce_mas_cb::get_folder_listing` 回调，可能调用多次。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `final` | 如果这是最后一个数据包，则为 `true`；如果后面还有数据，则为 `false`。 |
| `buf` | 包含过滤参数（Filter Parameters）和头部的缓冲区。初始请求必须包含连接 ID（Connection ID）和类型头部（Type Header）。若返回成功，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gabbe39f067872a6c008269d483a97d234"></a>

### `bt_map_mce_mas_get_mas_inst_info()`

```c
int bt_map_mce_mas_get_mas_inst_info ( struct bt_map_mce_mas * mce_mas, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送获取 MAS 实例信息请求（Get MAS Instance Info Request）。

获取 MAS 实例信息（Instance Information）。收到 `get_mas_inst_info` 响应后，将调用 `bt_map_mce_mas_cb::get_mas_inst_info` 回调，可能调用多次。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `final` | 如果这是最后一个数据包，则为 `true`；如果后面还有数据，则为 `false`。 |
| `buf` | 包含实例 ID（Instance ID）和头部的缓冲区。初始请求必须包含连接 ID（Connection ID）、类型头部（Type Header）和应用参数（Application Parameters）。若返回成功，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga39795b7002cf40984b130d38179a5472"></a>

### `bt_map_mce_mas_get_msg()`

```c
int bt_map_mce_mas_get_msg ( struct bt_map_mce_mas * mce_mas, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送获取消息请求（Get Message Request）。

根据句柄（Handle）获取特定消息。收到 `get_msg` 响应后，将调用 `bt_map_mce_mas_cb::get_msg` 回调，可能调用多次。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `final` | 如果这是最后一个数据包，则为 `true`；如果后面还有数据，则为 `false`。 |
| `buf` | 包含消息句柄（Message Handle）、参数和头部的缓冲区。初始请求必须包含连接 ID（Connection ID）、类型头部（Type Header）和名称头部（Name Header）。若返回成功，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gaf146e16f1b7950db4b5418bd27269ebb"></a>

### `bt_map_mce_mas_get_msg_listing()`

```c
int bt_map_mce_mas_get_msg_listing ( struct bt_map_mce_mas * mce_mas, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送获取消息列表请求（Get Message Listing Request）。

获取当前文件夹中的消息列表（Message Listing）。收到 `get_msg_listing` 响应后，将调用 `bt_map_mce_mas_cb::get_msg_listing` 回调，可能调用多次。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `final` | 如果这是最后一个数据包，则为 `true`；如果后面还有数据，则为 `false`。 |
| `buf` | 包含文件夹名称（Folder Name）、过滤参数（Filter Parameters）和头部的缓冲区。初始请求必须包含连接 ID（Connection ID）、类型头部（Type Header）和名称头部（Name Header）。若返回成功，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga2206f238364c04e180153c5cff10de94"></a>

### `bt_map_mce_mas_get_owner_status()`

```c
int bt_map_mce_mas_get_owner_status ( struct bt_map_mce_mas * mce_mas, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送获取所有者状态请求（Get Owner Status Request）。

获取所有者在线状态（Presence）和聊天状态（Chat State）。收到 `get_owner_status` 响应后，将调用 `bt_map_mce_mas_cb::get_owner_status` 回调，可能调用多次。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `final` | 如果这是最后一个数据包，则为 `true`；如果后面还有数据，则为 `false`。 |
| `buf` | 包含头部（Headers）的缓冲区。初始请求必须包含连接 ID（Connection ID）和类型头部（Type Header）。若返回成功，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga539c08b47cc73a23d24bd54dcb5d6dc4"></a>

### `bt_map_mce_mas_l2cap_connect()`

```c
int bt_map_mce_mas_l2cap_connect ( struct bt_conn * conn, struct bt_map_mce_mas * mce_mas, const struct bt_map_mce_mas_cb * cb, uint16_t psm )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

通过 L2CAP 连接 MAP 客户端的消息访问服务（MAS）。

发起到远端 MAS 的 L2CAP 传输连接（Transport Connection）。成功后将调用 `bt_map_mce_mas_cb::l2cap_connected` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与远端设备的蓝牙连接（Bluetooth Connection）。 |
| `mce_mas` | MAS 客户端实例。 |
| `cb` | 指向回调结构体（Callback Structure）的指针，必须在连接的整个生命周期内保持有效。 |
| `psm` | 通过服务发现协议（SDP）发现的 L2CAP 协议／服务复用器（PSM）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga1a00c2b646b9a10c3deb6f4953f04683"></a>

### `bt_map_mce_mas_l2cap_disconnect()`

```c
int bt_map_mce_mas_l2cap_disconnect ( struct bt_map_mce_mas * mce_mas)
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

通过 L2CAP 断开 MAP 客户端的消息访问服务（MAS）连接。

关闭 L2CAP 传输连接（Transport Connection）。成功后将调用 `bt_map_mce_mas_cb::l2cap_disconnected` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga54a2552080933e12b6b871bc9f898fce"></a>

### `bt_map_mce_mas_push_msg()`

```c
int bt_map_mce_mas_push_msg ( struct bt_map_mce_mas * mce_mas, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送推送消息请求（Push Message Request）。

向服务器上传新消息（Upload Message）。收到 `push_msg` 响应后，将调用 `bt_map_mce_mas_cb::push_msg` 回调，可能调用多次。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `final` | 最后一个数据包时为 `true`，后面还有数据时为 `false`。 |
| `buf` | 包含消息数据（bMessage 格式）和头部的缓冲区。初始请求必须包含连接 ID（Connection ID）、类型头部（Type Header）、名称头部（Name Header）和应用参数（Application Parameters）。`final` 为 `true` 时必须包含正文结束头部（End-of-body Header）。若返回成功，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga04bf8d4d99165e7cf49613fe82432ca7"></a>

### `bt_map_mce_mas_rfcomm_connect()`

```c
int bt_map_mce_mas_rfcomm_connect ( struct bt_conn * conn, struct bt_map_mce_mas * mce_mas, const struct bt_map_mce_mas_cb * cb, uint8_t channel )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

通过 RFCOMM 连接 MAP 客户端的消息访问服务（MAS）。

发起到远端 MAS 的 RFCOMM 传输连接（Transport Connection）。成功后将调用 `bt_map_mce_mas_cb::rfcomm_connected` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与远端设备的蓝牙连接（Bluetooth Connection）。 |
| `mce_mas` | MAS 客户端实例。 |
| `cb` | 指向回调结构体（Callback Structure）的指针，必须在连接的整个生命周期内保持有效。 |
| `channel` | 通过服务发现协议（SDP）发现的 RFCOMM 服务器通道（Server Channel）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga3202aee97828ecd8ed6f39f9eb6c98f2"></a>

### `bt_map_mce_mas_rfcomm_disconnect()`

```c
int bt_map_mce_mas_rfcomm_disconnect ( struct bt_map_mce_mas * mce_mas)
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

通过 RFCOMM 断开 MAP 客户端的消息访问服务（MAS）连接。

关闭 RFCOMM 传输连接（Transport Connection）。成功后将调用 `bt_map_mce_mas_cb::rfcomm_disconnected` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga9e6640177b225a5b7448cde8a17de4f0"></a>

### `bt_map_mce_mas_set_folder()`

```c
int bt_map_mce_mas_set_folder ( struct bt_map_mce_mas * mce_mas, uint8_t flags, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送设置文件夹请求（Set Folder Request）。

在 MAS 的文件夹层次结构（Folder Hierarchy）中导航。收到 `set_folder` 响应后，将调用 `bt_map_mce_mas_cb::set_folder` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `flags` | 导航标志，参见 `bt_map_set_folder_flags`。 |
| `buf` | 包含文件夹名称（用于 `DOWN`）和头部的缓冲区。必须包含连接 ID（Connection ID）。若返回成功，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gaa03c3ea1d6ec10d02412b4525dd3ffe5"></a>

### `bt_map_mce_mas_set_msg_status()`

```c
int bt_map_mce_mas_set_msg_status ( struct bt_map_mce_mas * mce_mas, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送设置消息状态请求（Set Message Status Request）。

修改消息状态（Message Status），例如已读、已删除等。收到 `set_msg_status` 响应后，将调用 `bt_map_mce_mas_cb::set_msg_status` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `final` | 如果这是最后一个数据包，则为 `true`；如果后面还有数据，则为 `false`。 |
| `buf` | 包含消息句柄（Message Handle）、状态参数（Status Parameters）和头部的缓冲区。必须包含连接 ID（Connection ID）、类型头部（Type Header）、名称头部（Name Header）和应用参数（Application Parameters）。若返回成功，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga28b33d6c38af9479e56e9c2c2c0f795a"></a>

### `bt_map_mce_mas_set_ntf_filter()`

```c
int bt_map_mce_mas_set_ntf_filter ( struct bt_map_mce_mas * mce_mas, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送设置通知过滤器请求（Set Notification Filter Request）。

配置哪些事件类型（Event Types）应接收通知。收到 `set_ntf_filter` 响应后，将调用 `bt_map_mce_mas_cb::set_ntf_filter` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `final` | 如果这是最后一个数据包，则为 `true`；如果后面还有数据，则为 `false`。 |
| `buf` | 包含过滤掩码（Filter Mask）和头部的缓冲区。必须包含连接 ID（Connection ID）、类型头部（Type Header）和应用参数（Application Parameters）。若返回成功，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gad528c35977847525d781a39c50a3e793"></a>

### `bt_map_mce_mas_set_ntf_reg()`

```c
int bt_map_mce_mas_set_ntf_reg ( struct bt_map_mce_mas * mce_mas, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送设置通知注册请求（Set Notification Registration Request）。

启用或禁用来自 MAS 的事件通知（Event Notification）。收到 `set_ntf_reg` 响应后，将调用 `bt_map_mce_mas_cb::set_ntf_reg` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `final` | 如果这是最后一个数据包，则为 `true`；如果后面还有数据，则为 `false`。 |
| `buf` | 包含通知状态（Notification Status）和头部的缓冲区。必须包含连接 ID（Connection ID）、类型头部（Type Header）和应用参数（Application Parameters）。若返回成功，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga3b1dc36240679618c98df515a351a5e7"></a>

### `bt_map_mce_mas_set_owner_status()`

```c
int bt_map_mce_mas_set_owner_status ( struct bt_map_mce_mas * mce_mas, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送设置所有者状态请求（Set Owner Status Request）。

设置所有者在线状态（Presence）和聊天状态（Chat State）。收到 `set_owner_status` 响应后，将调用 `bt_map_mce_mas_cb::set_owner_status` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `final` | 如果这是最后一个数据包，则为 `true`；如果后面还有数据，则为 `false`。 |
| `buf` | 包含所有者状态数据（Owner Status Data）和头部的缓冲区。必须包含连接 ID（Connection ID）、类型头部（Type Header）和应用参数（Application Parameters）。若返回成功，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gae91fb531b7164b389994b9391fa8e51e"></a>

### `bt_map_mce_mas_update_inbox()`

```c
int bt_map_mce_mas_update_inbox ( struct bt_map_mce_mas * mce_mas, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送更新收件箱请求（Update Inbox Request）。

请求服务器检查新消息。收到 `update_inbox` 响应后，将调用 `bt_map_mce_mas_cb::update_inbox` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mas` | MAS 客户端实例。 |
| `final` | 如果这是最后一个数据包，则为 `true`；如果后面还有数据，则为 `false`。 |
| `buf` | 包含头部（Headers）的缓冲区。必须包含连接 ID（Connection ID）和类型头部（Type Header）。若返回成功，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。


## 4.4\_原页交叉引用（Cross References）

- [bt_map_mce_mas_cb](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md)
- [bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [zephyr/bluetooth/classic/map.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2classic_2map_8h.html)
- [bt_map_mce_mas_cb::abort](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#adea73e4018513fe3f5443e2a4c3450dd)
- [bt_map_mce_mas_cb::connect](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a41ff659151ea8d312ed178907005c9fa)
- [bt_map_mce_mas_cb::disconnect](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#adebef477e23b2534fb7f54665338b0e2)
- [bt_map_mce_mas_cb::get_convo_listing](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#adaebc7b993824d27757a9482e56a211e)
- [bt_map_mce_mas_cb::get_folder_listing](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#aca7392666d7b4ca34c38654ee8b37a63)
- [bt_map_mce_mas_cb::get_mas_inst_info](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a096e8d15124959cbbfa5c3961c44b55b)
- [bt_map_mce_mas_cb::get_msg](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a42a9441ceab421f0ebd9accd8577ff05)
- [bt_map_mce_mas_cb::get_msg_listing](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#acdc05fac490ad32b5f197c673b46565f)
- [bt_map_mce_mas_cb::get_owner_status](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#aa491f3f467f93536d8dcdb7897552d9b)
- [bt_map_mce_mas_cb::l2cap_connected](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a6a5a53dd82f8f7ddce0fadc4284d9ebe)
- [bt_map_mce_mas_cb::l2cap_disconnected](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#abb01bd4ee41818a5c11de09035255ad5)
- [bt_map_mce_mas_cb::push_msg](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#aabecb70ffb005db1048f8615712a358f)
- [bt_map_mce_mas_cb::rfcomm_connected](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a2c1255b9c721c844222a98e8ab5c5301)
- [bt_map_mce_mas_cb::rfcomm_disconnected](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a3f245b9e735bca51f16b579dea049b71)
- [bt_map_mce_mas_cb::set_folder](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a3554be8e90ec9605a0a2524cb37e2561)
- [bt_map_set_folder_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga5678131af7da533ff8b751555542933e)
- [bt_map_mce_mas_cb::set_msg_status](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a1e11b4382657e6656b41058ba575d73d)
- [bt_map_mce_mas_cb::set_ntf_filter](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a15c281a0eb09f8e249b629c30d8909d2)
- [bt_map_mce_mas_cb::set_ntf_reg](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a283872e83a71cc79e20c51fb1312b898)
- [bt_map_mce_mas_cb::set_owner_status](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#aa74d509e4c1e792c1187aef27bfd5e8b)
- [bt_map_mce_mas_cb::update_inbox](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a51523325824c0add586e97e4fc45b985)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P003_经过时间服务（Elapsed Time Service，ETS）。.md) · [返回大纲](大纲.md) · [下一章](P005_运行时配置（Runtime Configuration）.md)
