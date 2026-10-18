---
id: learning.zephyr-docs.api-hid-pipeline-topic-reference.page-2
title: 蓝牙 HID 设备（Device）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_蓝牙 HID 设备（Device）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙 HID 设备（Device）

<a id="details"></a>

蓝牙 HID 设备（Device）

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_bt_5Fhid_5Fdevice_5Fcb"></a>

```c
struct bt_hid_device_cb
```

相关声明：[bt_hid_device_cb](../bluetooth_service_model_reference/P091_bt_hid_device_cb_结构体.md)。

由人机接口设备（HID）应用提供的回调。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.2\_函数（Functions）

<a id="r_ga296d1b9695091507438261035d067c02"></a>

```c
int bt_hid_device_register (const struct bt_hid_device_cb *cb)
```

相关声明：[bt_hid_device_register](#ga296d1b9695091507438261035d067c02)、[bt_hid_device_cb](../bluetooth_service_model_reference/P091_bt_hid_device_cb_结构体.md)。

注册人机接口设备（HID）回调。

<a id="r_ga35b0ec48658daa94010bef0c91503491"></a>

```c
int bt_hid_device_unregister (void)
```

相关声明：[bt_hid_device_unregister](#ga35b0ec48658daa94010bef0c91503491)。

注销 HID 设备回调并禁用 HID 服务。

<a id="r_gaf30d808e9903988d72d831c3c4aab617"></a>

```c
int bt_hid_device_connect (struct bt_conn *conn, struct bt_hid_device **hid)
```

相关声明：[bt_hid_device_connect](#gaf30d808e9903988d72d831c3c4aab617)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

在指定连接上发起向外建立的 HID 关联（Association）。

<a id="r_gae2000b4d39ed956cb37298bfcab351ed"></a>

```c
int bt_hid_device_disconnect (struct bt_hid_device *hid)
```

相关声明：[bt_hid_device_disconnect](#gae2000b4d39ed956cb37298bfcab351ed)。

断开此前已连接的 HID 关联（Association）。

<a id="r_gad6bc5203aa9a2c8e4e217005f8f58b2e"></a>

```c
struct net_buf * bt_hid_device_create_pdu (struct net_buf_pool *pool)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_hid_device_create_pdu](#gad6bc5203aa9a2c8e4e217005f8f58b2e)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

分配／创建适用于通过 L2CAP 传输 HID 的协议数据单元（PDU）缓冲区。

<a id="r_ga1034935eec4ff6a466990ee5f0c1ba2c"></a>

```c
int bt_hid_device_input_report (struct bt_hid_device *hid, struct net_buf *buf)
```

相关声明：[bt_hid_device_input_report](#ga1034935eec4ff6a466990ee5f0c1ba2c)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

向 HID 主机发送 HID 中断输入报告（Interrupt Input Report）。

<a id="r_gab5b6b5f1047961ed5164f4e1059201ad"></a>

```c
int bt_hid_device_virtual_cable_unplug (struct bt_hid_device *hid)
```

相关声明：[bt_hid_device_virtual_cable_unplug](#gab5b6b5f1047961ed5164f4e1059201ad)。

为指定 HID 关联触发虚拟电缆拔除（Virtual Cable Unplug）过程。

<a id="r_ga63608252095d8c0638c6c43809e42553"></a>

```c
struct bt_conn * bt_hid_device_get_conn (struct bt_hid_device *hid)
```

相关声明：[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_hid_device_get_conn](#ga63608252095d8c0638c6c43809e42553)。

获取与 HID 设备关联的异步无连接链路（ACL）连接。

## 2.3\_详细说明（Detailed Documentation）

<a id="gaf30d808e9903988d72d831c3c4aab617"></a>

### `bt_hid_device_connect()`

```c
int bt_hid_device_connect ( struct bt_conn * conn, struct bt_hid_device ** hid )
```

```c
#include <zephyr/bluetooth/classic/hid_device.h>
```

在指定连接上发起向外建立的 HID 关联（Association）。

成功时，`bt_hid_device` 实例保存在 `hid` 中。调用方不得释放此对象。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于关联（Association）的蓝牙连接（Bluetooth Connection）。 |
| `hid` | 成功时用于保存人机接口设备（HID Device）实例的指针。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="gad6bc5203aa9a2c8e4e217005f8f58b2e"></a>

### `bt_hid_device_create_pdu()`

```c
struct net_buf * bt_hid_device_create_pdu ( struct net_buf_pool * pool)
```

```c
#include <zephyr/bluetooth/classic/hid_device.h>
```

分配／创建适用于通过 L2CAP 传输 HID 的协议数据单元（PDU）缓冲区。

若 `pool` 为 `NULL`，实现可以使用默认缓冲池（Default Pool）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pool` | 用于分配的缓冲池（Buffer Pool）；为 `NULL` 时使用默认连接发送缓冲池（TX Pool）。 |

**说明（Note）**：注意：调用方应使用 `net_buf_add_*()` 向返回的缓冲区追加报告有效载荷（Report Payload）。

**返回（Returns）**：返回值：新的 `net_buf` 实例；失败返回 `NULL`。

<a id="gae2000b4d39ed956cb37298bfcab351ed"></a>

### `bt_hid_device_disconnect()`

```c
int bt_hid_device_disconnect ( struct bt_hid_device * hid)
```

```c
#include <zephyr/bluetooth/classic/hid_device.h>
```

断开此前已连接的 HID 关联（Association）。

断开连接是异步操作（Asynchronous）。在调用 `disconnected` 回调之前，调用方不应释放 `hid` 实例。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | 要断开连接的 HID 设备实例（Device Instance）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="ga63608252095d8c0638c6c43809e42553"></a>

### `bt_hid_device_get_conn()`

```c
struct bt_conn * bt_hid_device_get_conn ( struct bt_hid_device * hid)
```

```c
#include <zephyr/bluetooth/classic/hid_device.h>
```

获取与 HID 设备关联的异步无连接链路（ACL）连接。

适用于仅收到 HID 设备对象的回调，例如 `bt_hid_device_cb::vc_unplug`，但仍需要对端身份（Peer Identity）的情况，例如清除绑定信息（Bonding Information）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | HID 设备对象。 |

**返回（Returns）**：返回值：与 HID 设备关联的连接对象（Connection Object）；设备未连接时返回 `NULL`。调用方获得该连接对象的一个新引用，使用完毕后必须通过 `bt_conn_unref()` 释放。

<a id="ga1034935eec4ff6a466990ee5f0c1ba2c"></a>

### `bt_hid_device_input_report()`

```c
int bt_hid_device_input_report ( struct bt_hid_device * hid, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/hid_device.h>
```

向 HID 主机发送 HID 中断输入报告（Interrupt Input Report）。

缓冲区应包含完整的报告有效载荷（Report Payload）。若描述符声明了报告 ID（Report IDs），也必须包含报告 ID 字节，参见 HID 规范 v1.1.2 第 3.1.2.8 节。

HID 设备可以随时向主机发送中断通道消息（Interrupt Channel Messages）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | 用于发送数据的 HID 设备实例（Device Instance）。 |
| `buf` | 包含报告有效载荷（Report Payload）的缓冲区，成功时会被消耗。 |

**说明（Note）**：注意：必须使用 `bt_hid_device_create_pdu()` 分配缓冲区，以确保为 HID 和 L2CAP 头部预留足够的头部空间（Headroom）。

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="ga296d1b9695091507438261035d067c02"></a>

### `bt_hid_device_register()`

```c
int bt_hid_device_register ( const struct bt_hid_device_cb * cb)
```

```c
#include <zephyr/bluetooth/classic/hid_device.h>
```

注册人机接口设备（HID）回调。

回调指针必须在调用 `bt_hid_device_unregister()` 前一直有效。如果两次注册之间没有注销，第二次注册会被拒绝并返回 `-EALREADY`，原回调不会被替换。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 要注册的回调（Callbacks）。不得为 `NULL`，且必须提供必需的 `bt_hid_device_cb::get_report` 和 `bt_hid_device_cb::set_report` 回调。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | `cb` 为 `NULL`，或缺少必需回调（Mandatory Callback）时。 |
| `-EALREADY` | 已注册一组回调（Callback Set）时。 |

<a id="ga35b0ec48658daa94010bef0c91503491"></a>

### `bt_hid_device_unregister()`

```c
int bt_hid_device_unregister ( void )
```

```c
#include <zephyr/bluetooth/classic/hid_device.h>
```

注销 HID 设备回调并禁用 HID 服务。

清除回调并注销 L2CAP 服务器。调用方必须先断开所有活动 HID 会话（Active HID Sessions）再调用此函数，否则返回 `-EBUSY`，且不执行任何操作。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EBUSY` | 仍有活动 HID 会话（HID Session）时。 |

<a id="gab5b6b5f1047961ed5164f4e1059201ad"></a>

### `bt_hid_device_virtual_cable_unplug()`

```c
int bt_hid_device_virtual_cable_unplug ( struct bt_hid_device * hid)
```

```c
#include <zephyr/bluetooth/classic/hid_device.h>
```

为指定 HID 关联触发虚拟电缆拔除（Virtual Cable Unplug）过程。

请求远端主机将此设备视为已拔出（Unplugged）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | 要执行虚拟拔出的 HID 设备实例（Device Instance）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。


## 2.4\_原页交叉引用（Cross References）

- [bt_hid_device_cb](../bluetooth_service_model_reference/P091_bt_hid_device_cb_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [zephyr/bluetooth/classic/hid_device.h](../api_file_service_interface_reference/P025_zephyr__bluetooth__classic__hid_device.h_文件参考.md)
- [bt_hid_device_cb::vc_unplug](../bluetooth_service_model_reference/P091_bt_hid_device_cb_结构体.md#a71ee8022e59c83e2b28318432355663d)
- [bt_conn_unref()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga4b18c6b22a9f02be0d7d078b2ce51ff6)
- [bt_hid_device_cb::get_report](../bluetooth_service_model_reference/P091_bt_hid_device_cb_结构体.md#a42c35e661602bb1c8f5687ce04b055ef)
- [bt_hid_device_cb::set_report](../bluetooth_service_model_reference/P091_bt_hid_device_cb_结构体.md#a59768788c42e4369146767b95f9a22df)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_音频_视频远程控制封面图配置文件（Audio Video Remote Control Cover Art Profile）.md) · [返回大纲](大纲.md) · [下一章](P003_固件分发模型（Firmware Distribution models）.md)
