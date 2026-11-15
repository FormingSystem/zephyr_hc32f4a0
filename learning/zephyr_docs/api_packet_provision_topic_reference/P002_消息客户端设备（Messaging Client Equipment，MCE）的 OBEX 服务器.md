---
id: learning.zephyr-docs.api-packet-provision-topic-reference.page-2
title: 消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 服务器
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mns.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 服务器

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mns.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 服务器

<a id="details"></a>

消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 服务器

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_bt_5Fmap_5Fmce_5Fmns_5Frfcomm_5Fserver"></a>

```c
struct bt_map_mce_mns_rfcomm_server
```

相关声明：[bt_map_mce_mns_rfcomm_server](../bluetooth_service_model_reference/P112_bt_map_mce_mns_rfcomm_server_结构体.md)。

消息访问配置文件（MAP）客户端的MNS RFCOMM服务器。

<a id="r_bt_5Fmap_5Fmce_5Fmns_5Fl2cap_5Fserver"></a>

```c
struct bt_map_mce_mns_l2cap_server
```

相关声明：[bt_map_mce_mns_l2cap_server](../bluetooth_service_model_reference/P111_bt_map_mce_mns_l2cap_server_结构体.md)。

消息访问配置文件（MAP）客户端的MNS L2CAP服务器。

<a id="r_bt_5Fmap_5Fmce_5Fmns_5Fcb"></a>

```c
struct bt_map_mce_mns_cb
```

相关声明：[bt_map_mce_mns_cb](../bluetooth_service_model_reference/P110_bt_map_mce_mns_cb_结构体.md)。

消息访问配置文件（MAP）客户端的MNS回调。

<a id="r_bt_5Fmap_5Fmce_5Fmns"></a>

```c
struct bt_map_mce_mns
```

相关声明：[bt_map_mce_mns](../bluetooth_service_model_reference/P109_bt_map_mce_mns_结构体.md)。

消息访问配置文件（MAP）客户端的消息通知服务器（MNS）实例结构。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.2\_函数（Functions）

<a id="r_gabae24c99ada5dae44ca657ae96008a69"></a>

```c
int bt_map_mce_mns_register (struct bt_map_mce_mns *mce_mns, const struct bt_map_mce_mns_cb *cb)
```

相关声明：[bt_map_mce_mns_register](#gabae24c99ada5dae44ca657ae96008a69)、[bt_map_mce_mns](../bluetooth_service_model_reference/P109_bt_map_mce_mns_结构体.md)、[bt_map_mce_mns_cb](../bluetooth_service_model_reference/P110_bt_map_mce_mns_cb_结构体.md)。

注册 MAP 客户端的消息通知服务（MNS）服务器。

<a id="r_ga574790bc59c82d89010e61f535849a35"></a>

```c
int bt_map_mce_mns_rfcomm_register (struct bt_map_mce_mns_rfcomm_server *server)
```

相关声明：[bt_map_mce_mns_rfcomm_register](#ga574790bc59c82d89010e61f535849a35)、[bt_map_mce_mns_rfcomm_server](../bluetooth_service_model_reference/P112_bt_map_mce_mns_rfcomm_server_结构体.md)。

注册 MAP 客户端的 MNS RFCOMM 服务器。

<a id="r_gac6fa0bcfbea7b9a2a258678f5a2b8503"></a>

```c
int bt_map_mce_mns_rfcomm_disconnect (struct bt_map_mce_mns *mce_mns)
```

相关声明：[bt_map_mce_mns_rfcomm_disconnect](#gac6fa0bcfbea7b9a2a258678f5a2b8503)、[bt_map_mce_mns](../bluetooth_service_model_reference/P109_bt_map_mce_mns_结构体.md)。

通过 RFCOMM 断开 MAP 客户端 MNS 连接。

<a id="r_ga904970bac58822ec5336ce2bab226300"></a>

```c
int bt_map_mce_mns_l2cap_register (struct bt_map_mce_mns_l2cap_server *server)
```

相关声明：[bt_map_mce_mns_l2cap_register](#ga904970bac58822ec5336ce2bab226300)、[bt_map_mce_mns_l2cap_server](../bluetooth_service_model_reference/P111_bt_map_mce_mns_l2cap_server_结构体.md)。

注册 MAP 客户端的 MNS L2CAP 服务器。

<a id="r_gad4207d61fbe40c34e753132fc742aba3"></a>

```c
int bt_map_mce_mns_l2cap_disconnect (struct bt_map_mce_mns *mce_mns)
```

相关声明：[bt_map_mce_mns_l2cap_disconnect](#gad4207d61fbe40c34e753132fc742aba3)、[bt_map_mce_mns](../bluetooth_service_model_reference/P109_bt_map_mce_mns_结构体.md)。

通过 L2CAP 断开 MAP 客户端 MNS 连接。

<a id="r_ga029cb5034f7cbf059653c763e4c767c2"></a>

```c
struct net_buf * bt_map_mce_mns_create_pdu (struct bt_map_mce_mns *mce_mns, struct net_buf_pool *pool)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_map_mce_mns_create_pdu](#ga029cb5034f7cbf059653c763e4c767c2)、[bt_map_mce_mns](../bluetooth_service_model_reference/P109_bt_map_mce_mns_结构体.md)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

为 MAP 客户端 MNS 创建协议数据单元（PDU）。

<a id="r_gaab9161c0524c74cb4b03938c26642f4a"></a>

```c
int bt_map_mce_mns_connect (struct bt_map_mce_mns *mce_mns, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mce_mns_connect](#gaab9161c0524c74cb4b03938c26642f4a)、[bt_map_mce_mns](../bluetooth_service_model_reference/P109_bt_map_mce_mns_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 OBEX 连接响应（Connect Response）。

<a id="r_ga14411f8c0e8ce90824d366d28d4a2d2e"></a>

```c
int bt_map_mce_mns_disconnect (struct bt_map_mce_mns *mce_mns, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mce_mns_disconnect](#ga14411f8c0e8ce90824d366d28d4a2d2e)、[bt_map_mce_mns](../bluetooth_service_model_reference/P109_bt_map_mce_mns_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 OBEX 断开响应（Disconnect Response）。

<a id="r_ga7309e25833e6594dc0018afe8b0a403c"></a>

```c
int bt_map_mce_mns_abort (struct bt_map_mce_mns *mce_mns, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mce_mns_abort](#ga7309e25833e6594dc0018afe8b0a403c)、[bt_map_mce_mns](../bluetooth_service_model_reference/P109_bt_map_mce_mns_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 OBEX 中止响应（Abort Response）。

<a id="r_ga3e181d1bd37877dd8abf47a541c4b98e"></a>

```c
int bt_map_mce_mns_send_event (struct bt_map_mce_mns *mce_mns, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mce_mns_send_event](#ga3e181d1bd37877dd8abf47a541c4b98e)、[bt_map_mce_mns](../bluetooth_service_model_reference/P109_bt_map_mce_mns_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送事件响应（Event Response）。

## 2.3\_详细说明（Detailed Documentation）

<a id="ga7309e25833e6594dc0018afe8b0a403c"></a>

### `bt_map_mce_mns_abort()`

```c
int bt_map_mce_mns_abort ( struct bt_map_mce_mns * mce_mns, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送 OBEX 中止响应（Abort Response）。

响应来自远端消息服务器实体（MSE）的 OBEX ABORT 中止请求。从 `bt_map_mce_mns_cb::abort` 中止回调调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mns` | MNS 服务器实例。 |
| `rsp_code` | 响应码（Response Code）`bt_obex_rsp_code`；用 `BT_OBEX_RSP_CODE_SUCCESS` 表示接受。 |
| `buf` | 包含响应头部（Response Headers）的缓冲区。若为 `NULL`，发送默认响应。成功返回时，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gaab9161c0524c74cb4b03938c26642f4a"></a>

### `bt_map_mce_mns_connect()`

```c
int bt_map_mce_mns_connect ( struct bt_map_mce_mns * mce_mns, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送 OBEX 连接响应（Connect Response）。

响应来自远端消息服务器实体（MSE）的 OBEX CONNECT 连接请求。从 `bt_map_mce_mns_cb::connect` 连接回调调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mns` | MNS 服务器实例。 |
| `rsp_code` | 响应码（Response Code）`bt_obex_rsp_code`；用 `BT_OBEX_RSP_CODE_SUCCESS` 表示接受。 |
| `buf` | 包含响应头部（Response Headers）的缓冲区，例如 WHO、连接 ID 等。若为 `NULL`，发送默认响应。成功返回时，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga029cb5034f7cbf059653c763e4c767c2"></a>

### `bt_map_mce_mns_create_pdu()`

```c
struct net_buf * bt_map_mce_mns_create_pdu ( struct bt_map_mce_mns * mce_mns, struct net_buf_pool * pool )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

为 MAP 客户端 MNS 创建协议数据单元（PDU）。

分配用于构造 MAP 响应包的缓冲区。缓冲区大小根据协商后的最大传输单元（MTU）确定。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mns` | MNS 服务器实例。 |
| `pool` | 用于分配的缓冲池（Buffer Pool）；为 `NULL` 时使用默认缓冲池。 |

**返回（Returns）**：返回值：已分配的缓冲区（Allocated Buffer）；失败返回 `NULL`。

<a id="ga14411f8c0e8ce90824d366d28d4a2d2e"></a>

### `bt_map_mce_mns_disconnect()`

```c
int bt_map_mce_mns_disconnect ( struct bt_map_mce_mns * mce_mns, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送 OBEX 断开响应（Disconnect Response）。

响应来自远端消息服务器实体（MSE）的 OBEX DISCONNECT 断开请求。从 `bt_map_mce_mns_cb::disconnect` 断开回调调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mns` | MNS 服务器实例。 |
| `rsp_code` | 响应码（Response Code）`bt_obex_rsp_code`；用 `BT_OBEX_RSP_CODE_SUCCESS` 表示接受。 |
| `buf` | 包含响应头部（Response Headers）的缓冲区。若为 `NULL`，发送默认响应。成功返回时，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gad4207d61fbe40c34e753132fc742aba3"></a>

### `bt_map_mce_mns_l2cap_disconnect()`

```c
int bt_map_mce_mns_l2cap_disconnect ( struct bt_map_mce_mns * mce_mns)
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

通过 L2CAP 断开 MAP 客户端 MNS 连接。

关闭 L2CAP 传输连接（Transport Connection）。成功时调用 `bt_map_mce_mns_cb::l2cap_disconnected` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mns` | MNS 服务器实例。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga904970bac58822ec5336ce2bab226300"></a>

### `bt_map_mce_mns_l2cap_register()`

```c
int bt_map_mce_mns_l2cap_register ( struct bt_map_mce_mns_l2cap_server * server)
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

注册 MAP 客户端的 MNS L2CAP 服务器。

注册 L2CAP 服务器以接受传入的 MNS 连接。协议／服务复用器（PSM）可自动分配，也可显式指定。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | 已配置 `accept` 接受回调的 L2CAP 服务器结构体（Server Structure）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gabae24c99ada5dae44ca657ae96008a69"></a>

### `bt_map_mce_mns_register()`

```c
int bt_map_mce_mns_register ( struct bt_map_mce_mns * mce_mns, const struct bt_map_mce_mns_cb * cb )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

注册 MAP 客户端的消息通知服务（MNS）服务器。

将回调表（Callback Table）关联到服务器对象，并将其注册到底层 OBEX 服务器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mns` | MNS 服务器实例。 |
| `cb` | 指向回调结构体（Callback Structure）的指针，必须在服务器的整个生命周期内保持有效。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gac6fa0bcfbea7b9a2a258678f5a2b8503"></a>

### `bt_map_mce_mns_rfcomm_disconnect()`

```c
int bt_map_mce_mns_rfcomm_disconnect ( struct bt_map_mce_mns * mce_mns)
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

通过 RFCOMM 断开 MAP 客户端 MNS 连接。

关闭 RFCOMM 传输连接（Transport Connection）。成功时调用 `bt_map_mce_mns_cb::rfcomm_disconnected` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mns` | MNS 服务器实例。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga574790bc59c82d89010e61f535849a35"></a>

### `bt_map_mce_mns_rfcomm_register()`

```c
int bt_map_mce_mns_rfcomm_register ( struct bt_map_mce_mns_rfcomm_server * server)
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

注册 MAP 客户端的 MNS RFCOMM 服务器。

注册 RFCOMM 服务器以接受传入的 MNS 连接。服务器通道（Server Channel）可自动分配，也可显式指定。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | 已配置 `accept` 接受回调的 RFCOMM 服务器结构体（Server Structure）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga3e181d1bd37877dd8abf47a541c4b98e"></a>

### `bt_map_mce_mns_send_event()`

```c
int bt_map_mce_mns_send_event ( struct bt_map_mce_mns * mce_mns, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送事件响应（Event Response）。

响应来自远端消息服务器实体（MSE）的 SendEvent 请求。从 `bt_map_mce_mns_cb::send_event` 回调调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mce_mns` | MNS 服务器实例。 |
| `rsp_code` | 响应码（Response Code）`bt_obex_rsp_code`；部分完成使用 `BT_OBEX_RSP_CODE_CONTINUE`，全部完成使用 `BT_OBEX_RSP_CODE_SUCCESS`。 |
| `buf` | 包含响应头部（Response Headers）的缓冲区。若为 `NULL`，发送默认响应。成功返回时，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。


## 2.4\_原页交叉引用（Cross References）

- [bt_map_mce_mns_rfcomm_server](../bluetooth_service_model_reference/P112_bt_map_mce_mns_rfcomm_server_结构体.md)
- [bt_map_mce_mns_l2cap_server](../bluetooth_service_model_reference/P111_bt_map_mce_mns_l2cap_server_结构体.md)
- [bt_map_mce_mns_cb](../bluetooth_service_model_reference/P110_bt_map_mce_mns_cb_结构体.md)
- [bt_map_mce_mns](../bluetooth_service_model_reference/P109_bt_map_mce_mns_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [zephyr/bluetooth/classic/map.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2classic_2map_8h.html)
- [bt_map_mce_mns_cb::abort](../bluetooth_service_model_reference/P110_bt_map_mce_mns_cb_结构体.md#aa27a21b8c6a0d088ad487f9b51c7dfc1)
- [bt_obex_rsp_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga81b84c24a976c6c13d33eb23b0b10ae9)
- [BT_OBEX_RSP_CODE_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9af449d3c85fbec550c76e29287a626789)
- [bt_map_mce_mns_cb::connect](../bluetooth_service_model_reference/P110_bt_map_mce_mns_cb_结构体.md#ab3da25ab3b1d96914927e834e3ca45b6)
- [bt_map_mce_mns_cb::disconnect](../bluetooth_service_model_reference/P110_bt_map_mce_mns_cb_结构体.md#a8e3c2515dce12a6bee185ae4ac38a4e7)
- [bt_map_mce_mns_cb::l2cap_disconnected](../bluetooth_service_model_reference/P110_bt_map_mce_mns_cb_结构体.md#ad19cefcd45105bab829a427ab12f774b)
- [bt_map_mce_mns_cb::rfcomm_disconnected](../bluetooth_service_model_reference/P110_bt_map_mce_mns_cb_结构体.md#ad516d3cc29bc6f32e9f24415cfb5c56d)
- [bt_map_mce_mns_cb::send_event](../bluetooth_service_model_reference/P110_bt_map_mce_mns_cb_结构体.md#a7266e0e0d00994af225efd63615e595d)
- [BT_OBEX_RSP_CODE_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a7e38ca653283f53b62fa4b21f48d998a)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_电池备份 RAM（BBRAM）.md) · [返回大纲](大纲.md) · [下一章](P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 客户端.md)
