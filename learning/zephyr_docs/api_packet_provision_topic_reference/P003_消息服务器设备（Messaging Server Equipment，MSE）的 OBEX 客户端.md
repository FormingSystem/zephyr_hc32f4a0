---
id: learning.zephyr-docs.api-packet-provision-topic-reference.page-3
title: 消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 客户端
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mns.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 客户端

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mns.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 客户端

<a id="details"></a>

消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 客户端

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

<a id="r_bt_5Fmap_5Fmse_5Fmns_5Fcb"></a>

```c
struct bt_map_mse_mns_cb
```

相关声明：[bt_map_mse_mns_cb](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md)。

消息访问配置文件（MAP）服务器的MNS回调。

<a id="r_bt_5Fmap_5Fmse_5Fmns"></a>

```c
struct bt_map_mse_mns
```

相关声明：[bt_map_mse_mns](../bluetooth_service_model_reference/P117_bt_map_mse_mns_结构体.md)。

消息访问配置文件（MAP）服务器的消息通知服务器（MNS）实例结构。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.2\_函数（Functions）

<a id="r_gadf2f434d2565703781a46851d4444a80"></a>

```c
int bt_map_mse_mns_rfcomm_connect (struct bt_conn *conn, struct bt_map_mse_mns *mse_mns, const struct bt_map_mse_mns_cb *cb, uint8_t channel)
```

相关声明：[bt_map_mse_mns_rfcomm_connect](#gadf2f434d2565703781a46851d4444a80)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_map_mse_mns](../bluetooth_service_model_reference/P117_bt_map_mse_mns_结构体.md)、[bt_map_mse_mns_cb](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通过 RFCOMM 连接 MAP 服务器 MNS。

<a id="r_ga0513491439278cadc6897f9cb932cd67"></a>

```c
int bt_map_mse_mns_rfcomm_disconnect (struct bt_map_mse_mns *mse_mns)
```

相关声明：[bt_map_mse_mns_rfcomm_disconnect](#ga0513491439278cadc6897f9cb932cd67)、[bt_map_mse_mns](../bluetooth_service_model_reference/P117_bt_map_mse_mns_结构体.md)。

通过 RFCOMM 断开 MAP 服务器 MNS 连接。

<a id="r_ga46fc48dafd5c173199274be1a616a109"></a>

```c
int bt_map_mse_mns_l2cap_connect (struct bt_conn *conn, struct bt_map_mse_mns *mse_mns, const struct bt_map_mse_mns_cb *cb, uint16_t psm)
```

相关声明：[bt_map_mse_mns_l2cap_connect](#ga46fc48dafd5c173199274be1a616a109)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_map_mse_mns](../bluetooth_service_model_reference/P117_bt_map_mse_mns_结构体.md)、[bt_map_mse_mns_cb](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

通过 L2CAP 连接 MAP 服务器 MNS。

<a id="r_ga305dd055de4831ef68cff7b5346a4b5d"></a>

```c
int bt_map_mse_mns_l2cap_disconnect (struct bt_map_mse_mns *mse_mns)
```

相关声明：[bt_map_mse_mns_l2cap_disconnect](#ga305dd055de4831ef68cff7b5346a4b5d)、[bt_map_mse_mns](../bluetooth_service_model_reference/P117_bt_map_mse_mns_结构体.md)。

通过 L2CAP 断开 MAP 服务器 MNS 连接。

<a id="r_gaa0298eb521d012a910eba4a552d55fa7"></a>

```c
struct net_buf * bt_map_mse_mns_create_pdu (struct bt_map_mse_mns *mse_mns, struct net_buf_pool *pool)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_map_mse_mns_create_pdu](#gaa0298eb521d012a910eba4a552d55fa7)、[bt_map_mse_mns](../bluetooth_service_model_reference/P117_bt_map_mse_mns_结构体.md)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

为 MAP 服务器 MNS 创建协议数据单元（PDU）。

<a id="r_ga7bedc538a126b8c4d4c6fb393fc06218"></a>

```c
int bt_map_mse_mns_connect (struct bt_map_mse_mns *mse_mns, struct net_buf *buf)
```

相关声明：[bt_map_mse_mns_connect](#ga7bedc538a126b8c4d4c6fb393fc06218)、[bt_map_mse_mns](../bluetooth_service_model_reference/P117_bt_map_mse_mns_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送对象交换协议（OBEX）连接请求（Connect Request）。

<a id="r_ga08513e5aa2b54e4474ee647232c0af91"></a>

```c
int bt_map_mse_mns_disconnect (struct bt_map_mse_mns *mse_mns, struct net_buf *buf)
```

相关声明：[bt_map_mse_mns_disconnect](#ga08513e5aa2b54e4474ee647232c0af91)、[bt_map_mse_mns](../bluetooth_service_model_reference/P117_bt_map_mse_mns_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 OBEX 断开请求（Disconnect Request）。

<a id="r_gafc1be36425faa6242ed8eb4f21d76b5f"></a>

```c
int bt_map_mse_mns_abort (struct bt_map_mse_mns *mse_mns, struct net_buf *buf)
```

相关声明：[bt_map_mse_mns_abort](#gafc1be36425faa6242ed8eb4f21d76b5f)、[bt_map_mse_mns](../bluetooth_service_model_reference/P117_bt_map_mse_mns_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 OBEX 中止请求（Abort Request）。

<a id="r_gac8776edbbf4e2f891246cba86a1df589"></a>

```c
int bt_map_mse_mns_send_event (struct bt_map_mse_mns *mse_mns, bool final, struct net_buf *buf)
```

相关声明：[bt_map_mse_mns_send_event](#gac8776edbbf4e2f891246cba86a1df589)、[bt_map_mse_mns](../bluetooth_service_model_reference/P117_bt_map_mse_mns_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送事件通知请求（Event Notification Request）。

## 3.3\_详细说明（Detailed Documentation）

<a id="gafc1be36425faa6242ed8eb4f21d76b5f"></a>

### `bt_map_mse_mns_abort()`

```c
int bt_map_mse_mns_abort ( struct bt_map_mse_mns * mse_mns, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送 OBEX 中止请求（Abort Request）。

中止当前正在进行的操作。收到 OBEX 中止响应（Abort Response）后，将调用 `bt_map_mse_mns_cb::abort` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mns` | MNS 客户端实例。 |
| `buf` | 包含中止头部（Abort Headers）的缓冲区，例如连接 ID 等。若为 `NULL`，发送默认中止请求。成功返回时，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga7bedc538a126b8c4d4c6fb393fc06218"></a>

### `bt_map_mse_mns_connect()`

```c
int bt_map_mse_mns_connect ( struct bt_map_mse_mns * mse_mns, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送对象交换协议（OBEX）连接请求（Connect Request）。

发起与 MNS 的 OBEX 会话建立（Session Establishment）。必须在传输连接建立后调用。收到 OBEX 连接响应后，将调用 `bt_map_mse_mns_cb::connect` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mns` | MNS 客户端实例。 |
| `buf` | 包含连接头部（Connect Headers）的缓冲区，例如目标 UUID 等。若为 `NULL`，发送默认连接请求。成功返回时，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gaa0298eb521d012a910eba4a552d55fa7"></a>

### `bt_map_mse_mns_create_pdu()`

```c
struct net_buf * bt_map_mse_mns_create_pdu ( struct bt_map_mse_mns * mse_mns, struct net_buf_pool * pool )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

为 MAP 服务器 MNS 创建协议数据单元（PDU）。

分配用于构造消息访问配置文件（MAP）请求包的缓冲区。缓冲区大小根据协商后的最大传输单元（MTU）确定。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mns` | MNS 客户端实例。 |
| `pool` | 用于分配的缓冲池（Buffer Pool）；为 `NULL` 时使用默认缓冲池。 |

**返回（Returns）**：返回值：已分配的缓冲区（Allocated Buffer）；分配失败返回 `NULL`。

<a id="ga08513e5aa2b54e4474ee647232c0af91"></a>

### `bt_map_mse_mns_disconnect()`

```c
int bt_map_mse_mns_disconnect ( struct bt_map_mse_mns * mse_mns, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送 OBEX 断开请求（Disconnect Request）。

发起 OBEX 会话终止（Session Termination）。收到 OBEX 断开响应后，将调用 `bt_map_mse_mns_cb::disconnect` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mns` | MNS 客户端实例。 |
| `buf` | 包含断开头部（Disconnect Headers）的缓冲区，例如连接 ID 等。若为 `NULL`，发送默认断开请求。成功返回时，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga46fc48dafd5c173199274be1a616a109"></a>

### `bt_map_mse_mns_l2cap_connect()`

```c
int bt_map_mse_mns_l2cap_connect ( struct bt_conn * conn, struct bt_map_mse_mns * mse_mns, const struct bt_map_mse_mns_cb * cb, uint16_t psm )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

通过 L2CAP 连接 MAP 服务器 MNS。

发起到远端 MNS 的 L2CAP 传输连接（Transport Connection）。成功时调用 `bt_map_mse_mns_cb::l2cap_connected` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与远端设备的蓝牙连接（Bluetooth Connection）。 |
| `mse_mns` | MNS 客户端实例。 |
| `cb` | 指向回调结构体（Callback Structure）的指针，必须在连接的整个生命周期内保持有效。 |
| `psm` | 通过服务发现协议（SDP）发现的 L2CAP 协议／服务复用器（PSM）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga305dd055de4831ef68cff7b5346a4b5d"></a>

### `bt_map_mse_mns_l2cap_disconnect()`

```c
int bt_map_mse_mns_l2cap_disconnect ( struct bt_map_mse_mns * mse_mns)
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

通过 L2CAP 断开 MAP 服务器 MNS 连接。

关闭 L2CAP 传输连接（Transport Connection）。成功时调用 `bt_map_mse_mns_cb::l2cap_disconnected` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mns` | MNS 客户端实例。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gadf2f434d2565703781a46851d4444a80"></a>

### `bt_map_mse_mns_rfcomm_connect()`

```c
int bt_map_mse_mns_rfcomm_connect ( struct bt_conn * conn, struct bt_map_mse_mns * mse_mns, const struct bt_map_mse_mns_cb * cb, uint8_t channel )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

通过 RFCOMM 连接 MAP 服务器 MNS。

发起到远端 MNS 的 RFCOMM 传输连接（Transport Connection）。成功时调用 `bt_map_mse_mns_cb::rfcomm_connected` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与远端设备的蓝牙连接（Bluetooth Connection）。 |
| `mse_mns` | MNS 客户端实例。 |
| `cb` | 指向回调结构体（Callback Structure）的指针，必须在连接的整个生命周期内保持有效。 |
| `channel` | 通过服务发现协议（SDP）发现的 RFCOMM 服务器通道（Server Channel）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga0513491439278cadc6897f9cb932cd67"></a>

### `bt_map_mse_mns_rfcomm_disconnect()`

```c
int bt_map_mse_mns_rfcomm_disconnect ( struct bt_map_mse_mns * mse_mns)
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

通过 RFCOMM 断开 MAP 服务器 MNS 连接。

关闭 RFCOMM 传输连接（Transport Connection）。成功时调用 `bt_map_mse_mns_cb::rfcomm_disconnected` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mns` | MNS 客户端实例。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gac8776edbbf4e2f891246cba86a1df589"></a>

### `bt_map_mse_mns_send_event()`

```c
int bt_map_mse_mns_send_event ( struct bt_map_mse_mns * mse_mns, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/map.h>
```

发送事件通知请求（Event Notification Request）。

向远端消息客户端实体（MCE）发送事件通知（Event Notification）。可多次调用以发送分片事件数据。收到 `send_event` 响应后，将调用 `bt_map_mse_mns_cb::send_event` 回调，可能调用多次。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mse_mns` | MNS 客户端实例。 |
| `final` | 最后一个数据包时为 `true`，后面还有数据时为 `false`。 |
| `buf` | 包含事件报告 XML 数据及头部（Headers）的缓冲区。初始请求必须包含连接 ID、类型头部和应用参数。`final` 为 `true` 时必须包含正文结束头部（End-of-body Header）。成功返回时，函数已取得 `buf` 的所有权（Ownership）。 |

返回（Returns）：成功时为0，失败时为负错误码。


## 3.4\_原页交叉引用（Cross References）

- [bt_map_mse_mns_cb](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md)
- [bt_map_mse_mns](../bluetooth_service_model_reference/P117_bt_map_mse_mns_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [zephyr/bluetooth/classic/map.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2classic_2map_8h.html)
- [bt_map_mse_mns_cb::abort](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md#a168facdd5cdcc695814e4e9dd517f807)
- [bt_map_mse_mns_cb::connect](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md#aac533d7aa478d0645a1853de8a5fd354)
- [bt_map_mse_mns_cb::disconnect](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md#a2afd0b35998943c07584a70fa6a6107a)
- [bt_map_mse_mns_cb::l2cap_connected](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md#a62f7d9e4661fce6976650c3d90245dc8)
- [bt_map_mse_mns_cb::l2cap_disconnected](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md#abcf2bc6750a60d66cf9999d542d0c8c2)
- [bt_map_mse_mns_cb::rfcomm_connected](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md#acbaddcaff6e7b5a4cedaccad97186dc4)
- [bt_map_mse_mns_cb::rfcomm_disconnected](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md#a8cc8665110f38287951012307ce8837b)
- [bt_map_mse_mns_cb::send_event](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md#ab38e352b61b54a9961f200c9cf30e5b8)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P002_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 服务器.md) · [返回大纲](大纲.md) · [下一章](P004_远程配网客户端模型（Remote Provisioning Client model）.md)
