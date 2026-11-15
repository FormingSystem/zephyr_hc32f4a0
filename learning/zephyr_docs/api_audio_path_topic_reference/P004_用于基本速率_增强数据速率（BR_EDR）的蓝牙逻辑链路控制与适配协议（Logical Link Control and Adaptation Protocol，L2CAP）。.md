---
id: learning.zephyr-docs.api-audio-path-topic-reference.page-4
title: 用于基本速率_增强数据速率（BR_EDR）的蓝牙逻辑链路控制与适配协议（Logical Link Control and Adaptation Protocol，L2CAP）。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_用于基本速率\_增强数据速率（BR\_EDR）的蓝牙逻辑链路控制与适配协议（Logical Link Control and Adaptation Protocol，L2CAP）。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于基本速率/增强数据速率（BR/EDR）的蓝牙逻辑链路控制与适配协议（Logical Link Control and Adaptation Protocol，L2CAP）。

<a id="details"></a>

用于基本速率/增强数据速率（BR/EDR）的蓝牙逻辑链路控制与适配协议（Logical Link Control and Adaptation Protocol，L2CAP）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.1\_数据结构（Data Structures）

<a id="r_bt_5Fl2cap_5Fbr_5Fecho_5Fcb"></a>

```c
struct bt_l2cap_br_echo_cb
```

相关声明：[bt_l2cap_br_echo_cb](../bluetooth_service_model_reference/P098_bt_l2cap_br_echo_cb_结构体.md)。

回显（ECHO）请求/响应的回调结构。

<a id="r_bt_5Fl2cap_5Fbr_5Fconnless_5Fcb"></a>

```c
struct bt_l2cap_br_connless_cb
```

相关声明：[bt_l2cap_br_connless_cb](../bluetooth_service_model_reference/P097_bt_l2cap_br_connless_cb_结构体.md)。

无连接数据信道（Connectionless Data Channel）的回调结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.2\_宏定义（Macros）

<a id="r_ga12c146741591a55dc50d7d07f0755daa"></a>

```c
#define BT_L2CAP_BR_ECHO_REQ_RESERVE BT_L2CAP_BUF_SIZE(4)
```

相关声明：[BT_L2CAP_BR_ECHO_REQ_RESERVE](#ga12c146741591a55dc50d7d07f0755daa)、[BT_L2CAP_BUF_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gab95b119de4757588074e367a90a7136a)。

传出的 L2CAP ECHO 请求协议数据单元（ECHO REQ PDU）所需的头部预留空间（Headroom）。

<a id="r_ga2961971c1f80aa6168f6cd47b991bf4d"></a>

```c
#define BT_L2CAP_BR_ECHO_RSP_RESERVE BT_L2CAP_BUF_SIZE(4)
```

相关声明：[BT_L2CAP_BR_ECHO_RSP_RESERVE](#ga2961971c1f80aa6168f6cd47b991bf4d)、[BT_L2CAP_BUF_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gab95b119de4757588074e367a90a7136a)。

传出的 L2CAP ECHO 响应协议数据单元（ECHO RSP PDU）所需的头部预留空间（Headroom）。

<a id="r_gaf90200c4933ca513eaa8a324f3f09614"></a>

```c
#define BT_L2CAP_CONNLESS_SDU_HDR_SIZE 2
```

相关声明：[BT_L2CAP_CONNLESS_SDU_HDR_SIZE](#gaf90200c4933ca513eaa8a324f3f09614)。

L2CAP 无连接服务数据单元（Connectionless SDU）的头部大小。

<a id="r_gac0c4332fa7020bdc52a4431c6a506524"></a>

```c
#define BT_L2CAP_CONNLESS_RESERVE BT_L2CAP_BUF_SIZE(BT_L2CAP_CONNLESS_SDU_HDR_SIZE)
```

相关声明：[BT_L2CAP_CONNLESS_RESERVE](#gac0c4332fa7020bdc52a4431c6a506524)、[BT_L2CAP_BUF_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gab95b119de4757588074e367a90a7136a)、[BT_L2CAP_CONNLESS_SDU_HDR_SIZE](#gaf90200c4933ca513eaa8a324f3f09614)。

无连接数据通道（Connectionless Data Channel）内传出的 L2CAP PDU 格式所需的头部预留空间（Headroom）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.3\_函数（Functions）

<a id="r_ga62c0115185f5026c1a842848dc5336ce"></a>

```c
int bt_l2cap_br_echo_cb_register (struct bt_l2cap_br_echo_cb *cb)
```

相关声明：[bt_l2cap_br_echo_cb_register](#ga62c0115185f5026c1a842848dc5336ce)、[bt_l2cap_br_echo_cb](../bluetooth_service_model_reference/P098_bt_l2cap_br_echo_cb_结构体.md)。

注册回显（ECHO）回调。

<a id="r_ga00ef7d0a42d8e544b195172af44b88b2"></a>

```c
int bt_l2cap_br_echo_cb_unregister (struct bt_l2cap_br_echo_cb *cb)
```

相关声明：[bt_l2cap_br_echo_cb_unregister](#ga00ef7d0a42d8e544b195172af44b88b2)、[bt_l2cap_br_echo_cb](../bluetooth_service_model_reference/P098_bt_l2cap_br_echo_cb_结构体.md)。

注销回显（ECHO）回调。

<a id="r_ga3c6ad17ba18f5c00e39a379ed735de21"></a>

```c
int bt_l2cap_br_echo_req (struct bt_conn *conn, struct net_buf *buf)
```

相关声明：[bt_l2cap_br_echo_req](#ga3c6ad17ba18f5c00e39a379ed735de21)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

通过回显请求（ECHO Request）发送回显数据。

<a id="r_ga8ebf537cc7e4c0a68a320f9c65c94b05"></a>

```c
int bt_l2cap_br_echo_rsp (struct bt_conn *conn, uint8_t identifier, struct net_buf *buf)
```

相关声明：[bt_l2cap_br_echo_rsp](#ga8ebf537cc7e4c0a68a320f9c65c94b05)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

通过回显响应（ECHO Response）发送回显数据。

<a id="r_gad1b4d59a8849124518bb973233b3f362"></a>

```c
int bt_l2cap_br_connless_register (struct bt_l2cap_br_connless_cb *cb)
```

相关声明：[bt_l2cap_br_connless_register](#gad1b4d59a8849124518bb973233b3f362)、[bt_l2cap_br_connless_cb](../bluetooth_service_model_reference/P097_bt_l2cap_br_connless_cb_结构体.md)。

注册无连接数据通道（Connectionless Data Channel）回调。

<a id="r_gaa83e03f5ea5d62de096e1ebabb530697"></a>

```c
int bt_l2cap_br_connless_unregister (struct bt_l2cap_br_connless_cb *cb)
```

相关声明：[bt_l2cap_br_connless_unregister](#gaa83e03f5ea5d62de096e1ebabb530697)、[bt_l2cap_br_connless_cb](../bluetooth_service_model_reference/P097_bt_l2cap_br_connless_cb_结构体.md)。

注销无连接数据通道（Connectionless Data Channel）回调。

<a id="r_ga3478f19778e657a2d047f68f26b89966"></a>

```c
int bt_l2cap_br_connless_send (struct bt_conn *conn, uint16_t psm, struct net_buf *buf)
```

相关声明：[bt_l2cap_br_connless_send](#ga3478f19778e657a2d047f68f26b89966)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

通过无连接数据通道（Connectionless Data Channel）发送数据。

## 4.4\_详细说明（Detailed Documentation）

<a id="ga12c146741591a55dc50d7d07f0755daa"></a>

### `BT_L2CAP_BR_ECHO_REQ_RESERVE`

```c
#define BT_L2CAP_BR_ECHO_REQ_RESERVE BT_L2CAP_BUF_SIZE(4)
```

```c
#include <zephyr/bluetooth/classic/l2cap_br.h>
```

传出的 L2CAP ECHO 请求协议数据单元（ECHO REQ PDU）所需的头部预留空间（Headroom）。

<a id="ga2961971c1f80aa6168f6cd47b991bf4d"></a>

### `BT_L2CAP_BR_ECHO_RSP_RESERVE`

```c
#define BT_L2CAP_BR_ECHO_RSP_RESERVE BT_L2CAP_BUF_SIZE(4)
```

```c
#include <zephyr/bluetooth/classic/l2cap_br.h>
```

传出的 L2CAP ECHO 响应协议数据单元（ECHO RSP PDU）所需的头部预留空间（Headroom）。

<a id="gac0c4332fa7020bdc52a4431c6a506524"></a>

### `BT_L2CAP_CONNLESS_RESERVE`

```c
#define BT_L2CAP_CONNLESS_RESERVE BT_L2CAP_BUF_SIZE(BT_L2CAP_CONNLESS_SDU_HDR_SIZE)
```

```c
#include <zephyr/bluetooth/classic/l2cap_br.h>
```

无连接数据通道（Connectionless Data Channel）内传出的 L2CAP PDU 格式所需的头部预留空间（Headroom）。

<a id="gaf90200c4933ca513eaa8a324f3f09614"></a>

### `BT_L2CAP_CONNLESS_SDU_HDR_SIZE`

```c
#define BT_L2CAP_CONNLESS_SDU_HDR_SIZE 2
```

```c
#include <zephyr/bluetooth/classic/l2cap_br.h>
```

L2CAP 无连接服务数据单元（Connectionless SDU）的头部大小。

<a id="gad1b4d59a8849124518bb973233b3f362"></a>

### `bt_l2cap_br_connless_register()`

```c
int bt_l2cap_br_connless_register ( struct bt_l2cap_br_connless_cb * cb)
```

```c
#include <zephyr/bluetooth/classic/l2cap_br.h>
```

注册无连接数据通道（Connectionless Data Channel）回调。

注册用于监测和接收无连接数据通道帧（Connectionless Data Channel Frames）的回调。这样应用就能在不建立连接的情况下接收发送到指定协议／服务复用器（PSM）的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（Callback Struct），必须指向持续有效的内存。PSM 字段必须设置为所需的协议／服务复用器（Protocol/Service Multiplexer）值；设为 0 则接收所有无连接数据帧。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | `cb` 为 `NULL`，或 PSM 值、`recv` 回调、安全级别（Security Level）无效时。 |
| `-EEXIST` | 具有相同 PSM 的回调已注册时。 |

<a id="ga3478f19778e657a2d047f68f26b89966"></a>

### `bt_l2cap_br_connless_send()`

```c
int bt_l2cap_br_connless_send ( struct bt_conn * conn, uint16_t psm, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/l2cap_br.h>
```

通过无连接数据通道（Connectionless Data Channel）发送数据。

通过无连接数据通道（Connectionless Data Channel）发送数据。此函数允许在不建立 L2CAP 通道连接的情况下，向指定 PSM 发送数据。

应用必须在发送前于缓冲区中预留 `BT_L2CAP_CONNLESS_RESERVE` 字节。出错时，应用仍持有 `buf` 的所有权（Ownership），且返回的缓冲区保持不变。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `psm` | 标识目标服务的协议／服务复用器（Protocol/Service Multiplexer）。 |
| `buf` | 包含待发送数据的缓冲区（Buffer）。应用必须在缓冲区头部预留足够空间（Headroom），以容纳 L2CAP 头部。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | `conn` 或 `buf` 为 `NULL`、`psm` 无效、`buf` 的引用计数不等于 1、`buf` 头部预留空间（Headroom）小于 `BT_L2CAP_CONNLESS_RESERVE`，或 `buf->user_data_size` 小于 `struct closure` 的大小时。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ESHUTDOWN` | 底层的无连接 L2CAP 通道（Connectionless Channel）为 `NULL` 时。 |

**返回（Returns）**：返回值：远端不支持无连接接收功能时返回 `-ENOTSUP`；找不到无连接 L2CAP 通道时返回 `-ENOTCONN`；数据大小超过对端无连接通道的最大传输单元（MTU）时返回 `-EMSGSIZE`。

<a id="gaa83e03f5ea5d62de096e1ebabb530697"></a>

### `bt_l2cap_br_connless_unregister()`

```c
int bt_l2cap_br_connless_unregister ( struct bt_l2cap_br_connless_cb * cb)
```

```c
#include <zephyr/bluetooth/classic/l2cap_br.h>
```

注销无连接数据通道（Connectionless Data Channel）回调。

注销用于监测和接收无连接数据通道帧（Connectionless Data Channel Frames）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 已注册的 `cb` 回调。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | `cb` 为 `NULL` 时。 |
| `-ENOENT` | `cb` 未注册（Registered）时。 |

<a id="ga62c0115185f5026c1a842848dc5336ce"></a>

### `bt_l2cap_br_echo_cb_register()`

```c
int bt_l2cap_br_echo_cb_register ( struct bt_l2cap_br_echo_cb * cb)
```

```c
#include <zephyr/bluetooth/classic/l2cap_br.h>
```

注册回显（ECHO）回调。

注册回调，以监测 L2CAP 基本速率（BR）回显请求／响应（Echo Request/Response）数据包。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（Callback Struct），必须指向持续有效的内存。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EEXIST` | `cb` 已注册（Registered）时。 |

<a id="ga00ef7d0a42d8e544b195172af44b88b2"></a>

### `bt_l2cap_br_echo_cb_unregister()`

```c
int bt_l2cap_br_echo_cb_unregister ( struct bt_l2cap_br_echo_cb * cb)
```

```c
#include <zephyr/bluetooth/classic/l2cap_br.h>
```

注销回显（ECHO）回调。

注销用于监测 L2CAP BR 回显请求／响应（Echo Request/Response）数据包的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（Callback Struct）指向持续有效的内存。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | `cb` 为 `NULL` 时。 |
| `-ENOENT` | `cb` 未注册（Registered）时。 |

<a id="ga3c6ad17ba18f5c00e39a379ed735de21"></a>

### `bt_l2cap_br_echo_req()`

```c
int bt_l2cap_br_echo_req ( struct bt_conn * conn, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/l2cap_br.h>
```

通过回显请求（ECHO Request）发送回显数据。

通过回显请求（ECHO Request）发送回显数据。应用必须在发送前于缓冲区中预留 `BT_L2CAP_BR_ECHO_REQ_RESERVE` 字节。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 异步无连接（ACL）连接对象。 |
| `buf` | 要发送的回显数据（ECHO Data）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga8ebf537cc7e4c0a68a320f9c65c94b05"></a>

### `bt_l2cap_br_echo_rsp()`

```c
int bt_l2cap_br_echo_rsp ( struct bt_conn * conn, uint8_t identifier, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/l2cap_br.h>
```

通过回显响应（ECHO Response）发送回显数据。

通过回显响应（ECHO Response）发送回显数据。应用必须在发送前于缓冲区中预留 `BT_L2CAP_BR_ECHO_RSP_RESERVE` 字节。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 异步无连接（ACL）连接对象。 |
| `identifier` | ECHO 请求的标识符。 |
| `buf` | 要发送的回显数据（ECHO Data）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。


## 4.5\_原页交叉引用（Cross References）

- [bt_l2cap_br_echo_cb](../bluetooth_service_model_reference/P098_bt_l2cap_br_echo_cb_结构体.md)
- [bt_l2cap_br_connless_cb](../bluetooth_service_model_reference/P097_bt_l2cap_br_connless_cb_结构体.md)
- [BT_L2CAP_BUF_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gab95b119de4757588074e367a90a7136a)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [zephyr/bluetooth/classic/l2cap_br.h](../api_file_system_power_reference/P022_zephyr__bluetooth__classic__l2cap_br.h_文件参考.md)
- [recv](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#adee01662b0cf762a014efd87ab811276)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P003_加密广播数据（Encrypted Advertising Data，EAD）.md) · [返回大纲](大纲.md) · [下一章](P005_蓝牙 Mesh BLOB 模型 API.md)
