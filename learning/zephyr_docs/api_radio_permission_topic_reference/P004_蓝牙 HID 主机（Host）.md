---
id: learning.zephyr-docs.api-radio-permission-topic-reference.page-4
title: 蓝牙 HID 主机（Host）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_蓝牙 HID 主机（Host）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙 HID 主机（Host）

<a id="details"></a>

蓝牙 HID 主机（Host）

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.1\_数据结构（Data Structures）

<a id="r_bt_5Fhid_5Fhost_5Fcb"></a>

```c
struct bt_hid_host_cb
```

相关声明：[bt_hid_host_cb](../bluetooth_service_model_reference/P092_bt_hid_host_cb_结构体.md)。

由人机接口设备主机（HID Host）应用提供的回调。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.2\_函数（Functions）

<a id="r_ga86d49efef335609422f23b52717c9e1b"></a>

```c
int bt_hid_host_register (const struct bt_hid_host_cb *cb)
```

相关声明：[bt_hid_host_register](#ga86d49efef335609422f23b52717c9e1b)、[bt_hid_host_cb](../bluetooth_service_model_reference/P092_bt_hid_host_cb_结构体.md)。

注册 HID 主机回调（Host Callbacks）。

<a id="r_gaf1998a703fcf34e51e051a7a4c42937b"></a>

```c
int bt_hid_host_unregister (void)
```

相关声明：[bt_hid_host_unregister](#gaf1998a703fcf34e51e051a7a4c42937b)。

注销 HID 主机回调（Host Callbacks）。

<a id="r_ga8911b406dff5b2a0dd21f9abe3a571d5"></a>

```c
int bt_hid_host_connect (struct bt_conn *conn, struct bt_hid_host **hid)
```

相关声明：[bt_hid_host_connect](#ga8911b406dff5b2a0dd21f9abe3a571d5)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

向远程 HID 设备（Device）发起 HID 连接。

<a id="r_ga5061be29cffeb76c1be0c5f7912f4cc8"></a>

```c
struct bt_conn * bt_hid_host_get_conn (struct bt_hid_host *hid)
```

相关声明：[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_hid_host_get_conn](#ga5061be29cffeb76c1be0c5f7912f4cc8)。

获取 HID 关联（Association）的 ACL 连接。

<a id="r_gac0101a4f54d50d6615fc7cce41044107"></a>

```c
int bt_hid_host_disconnect (struct bt_hid_host *hid)
```

相关声明：[bt_hid_host_disconnect](#gac0101a4f54d50d6615fc7cce41044107)。

断开 HID 关联（Association）。

<a id="r_gae52c3d2ed7dd2a6868f9dff584ac2da4"></a>

```c
int bt_hid_host_get_report (struct bt_hid_host *hid, uint8_t type, uint8_t report_id, uint16_t buffer_size)
```

相关声明：[bt_hid_host_get_report](#gae52c3d2ed7dd2a6868f9dff584ac2da4)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向 HID 设备发送 `GET_REPORT` 请求。

<a id="r_ga2a7d73c8ad7faff0ece2217f35757576"></a>

```c
int bt_hid_host_set_report (struct bt_hid_host *hid, uint8_t type, struct net_buf *buf)
```

相关声明：[bt_hid_host_set_report](#ga2a7d73c8ad7faff0ece2217f35757576)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

向 HID 设备发送 `SET_REPORT` 请求。

<a id="r_ga45726162f45815aa9c2dc789e3b2beed"></a>

```c
int bt_hid_host_get_protocol (struct bt_hid_host *hid)
```

相关声明：[bt_hid_host_get_protocol](#ga45726162f45815aa9c2dc789e3b2beed)。

向 HID 设备发送 `GET_PROTOCOL` 请求。

<a id="r_gae13a5ae2473c239b4b109cd8e5b9a210"></a>

```c
int bt_hid_host_set_protocol (struct bt_hid_host *hid, uint8_t protocol)
```

相关声明：[bt_hid_host_set_protocol](#gae13a5ae2473c239b4b109cd8e5b9a210)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 HID 设备发送 `SET_PROTOCOL` 请求。

<a id="r_ga0415ec8597cb6ccc1016703438ac4f48"></a>

```c
int bt_hid_host_output_report (struct bt_hid_host *hid, struct net_buf *buf)
```

相关声明：[bt_hid_host_output_report](#ga0415ec8597cb6ccc1016703438ac4f48)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

在中断通道（Interrupt Channel）发送输出报告（Output Report）。

<a id="r_ga15db8aa5b2e56048a7e513730918ef50"></a>

```c
int bt_hid_host_suspend (struct bt_hid_host *hid)
```

相关声明：[bt_hid_host_suspend](#ga15db8aa5b2e56048a7e513730918ef50)。

向 HID 设备发送 `SUSPEND` 控制消息。

<a id="r_ga80472c16b68cfb7d1e8d9f73379e612a"></a>

```c
int bt_hid_host_exit_suspend (struct bt_hid_host *hid)
```

相关声明：[bt_hid_host_exit_suspend](#ga80472c16b68cfb7d1e8d9f73379e612a)。

向 HID 设备发送 `EXIT_SUSPEND` 控制消息。

<a id="r_ga6f7f967c1aa2cd15ba434fda1584b511"></a>

```c
int bt_hid_host_virtual_cable_unplug (struct bt_hid_host *hid)
```

相关声明：[bt_hid_host_virtual_cable_unplug](#ga6f7f967c1aa2cd15ba434fda1584b511)。

向 HID 设备发送虚拟线缆拔除（Virtual Cable Unplug）消息。

<a id="r_ga66ce643cbff7dbeb7dc4d4fe2b5476d7"></a>

```c
struct net_buf * bt_hid_host_create_pdu (struct net_buf_pool *pool)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_hid_host_create_pdu](#ga66ce643cbff7dbeb7dc4d4fe2b5476d7)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

为 HID 主机发送分配 PDU 缓冲区（PDU Buffer）。

## 4.3\_详细说明（Detailed Documentation）

<a id="ga8911b406dff5b2a0dd21f9abe3a571d5"></a>

### `bt_hid_host_connect()`

```c
int bt_hid_host_connect ( struct bt_conn * conn, struct bt_hid_host ** hid )
```

```c
#include <zephyr/bluetooth/classic/hid_host.h>
```

向远程 HID 设备（Device）发起 HID 连接。

打开 L2CAP 控制通道（Control Channel），建立后再打开中断通道（Interrupt Channel）。

此处不读取 HID 服务记录（Service Record）。需要报告描述符或设备属性的应用须自行通过 SDP 发现，也可自行决定是否在每次连接时执行发现。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与远端设备的 ACL 连接。 |
| `hid` | 成功时用于存放 HID 主机实例（HID Host Instance）的指针。 |

**返回（Returns）**：返回值（Returns）：成功返回 0；未调用 bt_hid_host_register() 时返回 -ENOTSUP；其他失败返回负 errno。

<a id="ga66ce643cbff7dbeb7dc4d4fe2b5476d7"></a>

### `bt_hid_host_create_pdu()`

```c
struct net_buf * bt_hid_host_create_pdu ( struct net_buf_pool * pool)
```

```c
#include <zephyr/bluetooth/classic/hid_host.h>
```

为 HID 主机发送分配 PDU 缓冲区（PDU Buffer）。

返回的缓冲区已为 HID 头部预留头部空间（Headroom），规范层可直接前置头部而无需复制。调用方仅通过 net_buf_add_*() 追加报告载荷（Report Payload），不得自行占用头部空间。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pool` | 要从中分配的缓冲池（Buffer Pool），传 NULL 使用默认池。 |

**返回（Returns）**：返回值（Returns）：成功返回 net_buf，失败返回 NULL。

<a id="gac0101a4f54d50d6615fc7cce41044107"></a>

### `bt_hid_host_disconnect()`

```c
int bt_hid_host_disconnect ( struct bt_hid_host * hid)
```

```c
#include <zephyr/bluetooth/classic/hid_host.h>
```

断开 HID 关联（Association）。

依据 HID 规范 v1.1.2 第 5.2.2 节，先拆除中断通道（Interrupt Channel），再拆除控制通道（Control Channel）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | HID 主机实例。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="ga80472c16b68cfb7d1e8d9f73379e612a"></a>

### `bt_hid_host_exit_suspend()`

```c
int bt_hid_host_exit_suspend ( struct bt_hid_host * hid)
```

```c
#include <zephyr/bluetooth/classic/hid_host.h>
```

向 HID 设备发送 `EXIT_SUSPEND` 控制消息。

通知设备主机正在退出低功耗状态（Low-power State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | HID 主机实例。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="ga5061be29cffeb76c1be0c5f7912f4cc8"></a>

### `bt_hid_host_get_conn()`

```c
struct bt_conn * bt_hid_host_get_conn ( struct bt_hid_host * hid)
```

```c
#include <zephyr/bluetooth/classic/hid_host.h>
```

获取 HID 关联（Association）的 ACL 连接。

供需要根据对端身份操作的应用使用，例如在虚拟线缆拔除（Virtual Cable Unplug，HID 规范 v1.1.2 第 3.1.2.2.3 节）后销毁绑定（Bonding）；协议栈将此工作留给应用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | HID 主机实例。 |

**返回（Returns）**：返回值（Returns）：ACL 连接的新引用，必须使用 bt_conn_unref() 释放；关联已解除时返回 NULL。

<a id="ga45726162f45815aa9c2dc789e3b2beed"></a>

### `bt_hid_host_get_protocol()`

```c
int bt_hid_host_get_protocol ( struct bt_hid_host * hid)
```

```c
#include <zephyr/bluetooth/classic/hid_host.h>
```

向 HID 设备发送 `GET_PROTOCOL` 请求。

响应通过 get_protocol 回调到达。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | HID 主机实例。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="gae52c3d2ed7dd2a6868f9dff584ac2da4"></a>

### `bt_hid_host_get_report()`

```c
int bt_hid_host_get_report ( struct bt_hid_host * hid, uint8_t type, uint8_t report_id, uint16_t buffer_size )
```

```c
#include <zephyr/bluetooth/classic/hid_host.h>
```

向 HID 设备发送 `GET_REPORT` 请求。

响应通过 get_report 回调异步到达；若设备始终不应答，则拆除关联（Association）。

报告描述符一旦声明报告 ID（Report IDs），就必须包含 ReportID 字段；在引导协议模式（Boot Protocol Mode）下始终需要此字段（HID 规范 v1.1.2 第 3.1.2.3 节及第 3.3.1 节）。只有应用知道描述符，因此由应用决定是否发送该字段。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | HID 主机实例。 |
| `type` | 报告类型（Report Type）：BT_HID_REPORT_TYPE_INPUT／OUTPUT／FEATURE。 |
| `report_id` | 要请求的报告 ID（Report ID）；0 表示省略此字段。USB HID 规范保留 ID 0，因此不能用它标识报告。 |
| `buffer_size` | 最大响应载荷大小（Payload Size），0 表示不限制；不得超过控制通道可接收的大小。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="ga0415ec8597cb6ccc1016703438ac4f48"></a>

### `bt_hid_host_output_report()`

```c
int bt_hid_host_output_report ( struct bt_hid_host * hid, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/hid_host.h>
```

在中断通道（Interrupt Channel）发送输出报告（Output Report）。

这是无确认的异步传输（Asynchronous Transfer）：HID 规范 v1.1.2 第 3.1.2.9 节规定中断通道传输不应答。报告描述符声明了报告 ID，或设备处于引导协议模式时，缓冲区必须以报告 ID 开头。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | HID 主机实例。 |
| `buf` | 包含输出报告（Output Report）的缓冲区，使用 bt_hid_host_create_pdu() 分配以容纳 HIDP 头部；成功时消费缓冲区。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="ga86d49efef335609422f23b52717c9e1b"></a>

### `bt_hid_host_register()`

```c
int bt_hid_host_register ( const struct bt_hid_host_cb * cb)
```

```c
#include <zephyr/bluetooth/classic/hid_host.h>
```

注册 HID 主机回调（Host Callbacks）。

注册应用回调，并设置 L2CAP 服务器，在 PSM 0x0011／0x0013 上接受由设备发起的入站重连（Device-initiated Reconnections）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（Callback Structure），必须在 HID 主机子系统的整个生命周期内保持有效。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="gae13a5ae2473c239b4b109cd8e5b9a210"></a>

### `bt_hid_host_set_protocol()`

```c
int bt_hid_host_set_protocol ( struct bt_hid_host * hid, uint8_t protocol )
```

```c
#include <zephyr/bluetooth/classic/hid_host.h>
```

向 HID 设备发送 `SET_PROTOCOL` 请求。

响应通过 set_protocol 回调到达。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | HID 主机实例。 |
| `protocol` | 目标协议（Target Protocol）：BT_HID_PROTOCOL_BOOT_MODE 或 BT_HID_PROTOCOL_REPORT_MODE。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="ga2a7d73c8ad7faff0ece2217f35757576"></a>

### `bt_hid_host_set_report()`

```c
int bt_hid_host_set_report ( struct bt_hid_host * hid, uint8_t type, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/hid_host.h>
```

向 HID 设备发送 `SET_REPORT` 请求。

响应通过 set_report 回调到达。报告描述符声明了报告 ID，或设备处于引导协议模式时，缓冲区必须以报告 ID 开头。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | HID 主机实例。 |
| `type` | 报告类型（Report Type）：BT_HID_REPORT_TYPE_INPUT／OUTPUT／FEATURE。 |
| `buf` | 包含报告载荷（Report Payload）的缓冲区，使用 bt_hid_host_create_pdu() 分配；失败时仍由调用方持有。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="ga15db8aa5b2e56048a7e513730918ef50"></a>

### `bt_hid_host_suspend()`

```c
int bt_hid_host_suspend ( struct bt_hid_host * hid)
```

```c
#include <zephyr/bluetooth/classic/hid_host.h>
```

向 HID 设备发送 `SUSPEND` 控制消息。

通知设备主机正在进入低功耗状态（Low-power State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | HID 主机实例。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="gaf1998a703fcf34e51e051a7a4c42937b"></a>

### `bt_hid_host_unregister()`

```c
int bt_hid_host_unregister ( void )
```

```c
#include <zephyr/bluetooth/classic/hid_host.h>
```

注销 HID 主机回调（Host Callbacks）。

注销 L2CAP 服务器，不再接受设备发起的入站重连。必须先断开所有 HID 关联（Associations）。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EBUSY` | 仍有活动 HID 关联（Association）时。 |
| `-EALREADY` | 未注册 HID 主机回调（Host Callbacks）时。 |

**返回（Returns）**：返回值（Returns）：成功返回 0，其他失败返回负 errno。

<a id="ga6f7f967c1aa2cd15ba434fda1584b511"></a>

### `bt_hid_host_virtual_cable_unplug()`

```c
int bt_hid_host_virtual_cable_unplug ( struct bt_hid_host * hid)
```

```c
#include <zephyr/bluetooth/classic/hid_host.h>
```

向 HID 设备发送虚拟线缆拔除（Virtual Cable Unplug）消息。

依据 HID 规范 v1.1.2 第 3.1.2.2.3 节，发送虚拟线缆拔除控制消息（VCU Control Message），等待 HID 设备通过断开关联来确认。若对端未断开，主机在事务超时后执行后备拆除（Fallback Teardown）。销毁绑定（Bonding）由应用负责，参见 vc_unplug 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | HID 主机实例。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。


## 4.4\_原页交叉引用（Cross References）

- [bt_hid_host_cb](../bluetooth_service_model_reference/P092_bt_hid_host_cb_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [zephyr/bluetooth/classic/hid_host.h](../api_file_storage_event_reference/P010_zephyr__bluetooth__classic__hid_host.h_文件参考.md)
- [bt_conn_unref()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga4b18c6b22a9f02be0d7d078b2ce51ff6)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P003_蓝牙HCI锁步命令（Lockstep Command）的辅助接口。.md) · [返回大纲](大纲.md) · [下一章](P005_应用配置（Application Configuration）.md)
