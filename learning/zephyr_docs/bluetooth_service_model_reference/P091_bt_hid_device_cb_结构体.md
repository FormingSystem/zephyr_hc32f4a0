---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-91
title: bt_hid_device_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hid__device__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第91章\_bt\_hid\_device\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hid__device__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

由人机接口设备（HID）应用提供的回调。

```c
#include <zephyr/bluetooth/classic/hid_device.h>
```

<a id="details"></a>

由人机接口设备（HID）应用提供的回调。应用应通过 `bt_hid_device_register()` 注册此回调表的一个实例，以接收 HID 主机的事件和请求。只需提供应用需要的回调；未实现的回调应设为 `NULL`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 91.1\_数据成员（Data Fields）

<a id="r_a9c6dc500625337da8ce7a5f692d73fa9"></a>

```c
void(* connected )(struct bt_hid_device *hid)
```

相关声明：[connected](#a9c6dc500625337da8ce7a5f692d73fa9)。

向应用通知连接建立的 `connected` 回调。

<a id="r_aef0dda6b39282bc19f316ba364ae9420"></a>

```c
void(* disconnected )(struct bt_hid_device *hid)
```

相关声明：[disconnected](#aef0dda6b39282bc19f316ba364ae9420)。

向应用通知连接断开的 `disconnected` 回调。

<a id="r_a59768788c42e4369146767b95f9a22df"></a>

```c
int(* set_report )(struct bt_hid_device *hid, uint8_t type, struct net_buf *buf)
```

相关声明：[set_report](#a59768788c42e4369146767b95f9a22df)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

设置报告（Set_Report）请求回调。

<a id="r_a42c35e661602bb1c8f5687ce04b055ef"></a>

```c
int(* get_report )(struct bt_hid_device *hid, uint8_t type, bool size_present, struct net_buf *req, struct net_buf *rsp)
```

相关声明：[get_report](#a42c35e661602bb1c8f5687ce04b055ef)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

获取报告（Get_Report）请求回调。

<a id="r_a21ca7e5d28b575007fb12dbfe779d83a"></a>

```c
int(* set_protocol )(struct bt_hid_device *hid, uint8_t protocol)
```

相关声明：[set_protocol](#a21ca7e5d28b575007fb12dbfe779d83a)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置协议（Set_Protocol）请求回调。

<a id="r_af8fa358139cf4bec7483234c90bdf655"></a>

```c
void(* output_report )(struct bt_hid_device *hid, struct net_buf *buf)
```

相关声明：[output_report](#af8fa358139cf4bec7483234c90bdf655)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

输出报告（Output report）回调。

<a id="r_a71ee8022e59c83e2b28318432355663d"></a>

```c
void(* vc_unplug )(struct bt_hid_device *hid)
```

相关声明：[vc_unplug](#a71ee8022e59c83e2b28318432355663d)。

虚拟线缆拔除（Virtual Cable Unplug）通知回调。

<a id="r_a6221aa4f32aaa913536cb1ae70173a8e"></a>

```c
void(* suspend )(struct bt_hid_device *hid, bool suspended)
```

相关声明：[suspend](#a6221aa4f32aaa913536cb1ae70173a8e)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

挂起或退出挂起（Suspend/Exit-Suspend）通知回调。

## 91.2\_详细说明（Detailed Documentation）

<a id="a9c6dc500625337da8ce7a5f692d73fa9"></a>

### `connected`

```c
void(* bt_hid_device_cb::connected) (struct bt_hid_device *hid)
```

向应用通知连接建立的 `connected` 回调。

如果提供了此回调，每当 HID 关联（association）建立完成时都会调用它。此时控制通道与中断通道均已建立，设备已准备好进行 HID 数据传输。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | HID 设备对象。 |

<a id="aef0dda6b39282bc19f316ba364ae9420"></a>

### `disconnected`

```c
void(* bt_hid_device_cb::disconnected) (struct bt_hid_device *hid)
```

向应用通知连接断开的 `disconnected` 回调。

如果提供了此回调，每当 HID 关联断开时都会调用它，包括连接被拒绝、被取消以及建立期间发生错误的情况。HID 设备对象在此回调返回之前始终有效。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | HID 设备对象。 |

<a id="a42c35e661602bb1c8f5687ce04b055ef"></a>

### `get_report`

```c
int(* bt_hid_device_cb::get_report) (struct bt_hid_device *hid, uint8_t type, bool size_present, struct net_buf *req, struct net_buf *rsp)
```

获取报告（Get_Report）请求回调。

主机发送 `GET_REPORT` 请求时同步调用。此回调是必需的，因为 HID 规范 v1.1.2 要求支持 `GET_REPORT`，因此注册时必须提供。

应用在回调内将报告载荷追加到 `rsp`，然后返回 0，以此作出响应。如果报告描述符声明了报告 ID（Report ID），载荷必须包含报告 ID 字节。随后协议栈在前面添加 HIDP `DATA` 头并发送响应。

如果尚无可用数据，则返回 `-EAGAIN`；协议栈会回复 `NOT_READY` 握手消息，主机可以重试，参见 HID 规范 v1.1.2 第 3.2.1.1 节。其他负值 `errno` 会触发相应的握手错误响应。

`req` 包含 HIDP 头之后剩余的 `GET_REPORT` 参数：先是可选的报告 ID（是否存在由报告描述符决定）；当 `size_present` 为 `true` 时，其后还有一个按小端序存储的 2 字节 `BufferSize`，表示主机预期的最大响应长度。当 `size_present` 为 `false` 时，不存在 `BufferSize`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | HID 设备对象。 |
| `type` | 报告类型（Report type），参见 `BT_HID_REPORT_TYPE_*`。 |
| `size_present` | 如果请求中的 Size 位已置位，则为 `true`，表示 `req` 中可选的报告 ID 之后有一个 2 字节的 `BufferSize`。 |
| `req` | 剩余请求参数；其所有权仍由协议栈持有。 |
| `rsp` | 用于填入报告载荷的响应缓冲区；其所有权仍由协议栈持有，回调返回 0 时由协议栈发送。 |

**返回（Returns）**：返回值：若已将响应填入 `rsp`，则返回 0；返回 `-EAGAIN` 会回复 `NOT_READY`；其他负值 `errno` 表示握手错误。

<a id="af8fa358139cf4bec7483234c90bdf655"></a>

### `output_report`

```c
void(* bt_hid_device_cb::output_report) (struct bt_hid_device *hid, struct net_buf *buf)
```

输出报告（Output report）回调。

此回调提供通过中断通道从 HID 主机收到的输出报告数据。缓冲区包含原始报告载荷；如果描述符声明了报告 ID，则也包含该 ID。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | HID 设备对象。 |
| `buf` | 报告载荷缓冲区；其所有权仍由协议栈持有。 |

<a id="a21ca7e5d28b575007fb12dbfe779d83a"></a>

### `set_protocol`

```c
int(* bt_hid_device_cb::set_protocol) (struct bt_hid_device *hid, uint8_t protocol)
```

设置协议（Set_Protocol）请求回调。

主机发送 `SET_PROTOCOL` 请求时调用。如果支持所请求的协议模式，应用应返回 0；如果不支持，则返回负值 `errno`。驱动根据返回值更新内部协议模式标志，并发送适当的 `HANDSHAKE` 响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | HID 设备对象。 |
| `protocol` | 所请求的协议模式：`BT_HID_PROTOCOL_BOOT_MODE` 或 `BT_HID_PROTOCOL_REPORT_MODE`。 |

**返回（Returns）**：返回值：接受此协议模式时返回 0，否则返回负值 `errno`。

<a id="a59768788c42e4369146767b95f9a22df"></a>

### `set_report`

```c
int(* bt_hid_device_cb::set_report) (struct bt_hid_device *hid, uint8_t type, struct net_buf *buf)
```

设置报告（Set_Report）请求回调。

此回调提供 HID 主机发送的报告数据。此回调是必需的，因为 HID 规范 v1.1.2 要求支持 `SET_REPORT`，因此注册时必须提供。

缓冲区包含接收到的原始报告数据载荷（Report Data Payload）；如果描述符声明了报告 ID，则也包含报告 ID 字节。返回 0 表示接受报告；返回负值 `errno` 会触发相应的握手错误响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | HID 设备对象。 |
| `type` | 报告类型（Report type），参见 `BT_HID_REPORT_TYPE_*`。 |
| `buf` | 报告载荷缓冲区；其所有权仍由协议栈持有。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="a6221aa4f32aaa913536cb1ae70173a8e"></a>

### `suspend`

```c
void(* bt_hid_device_cb::suspend) (struct bt_hid_device *hid, bool suspended)
```

挂起或退出挂起（Suspend/Exit-Suspend）通知回调。

`SUSPEND` 与 `EXIT_SUSPEND` 是由 HID 主机发出的单向 `HID_CONTROL` 消息。此回调只是在收到每条此类消息时将其转交应用；设备本身不维护挂起状态机。根据 HID 规范，已挂起的设备在检测到本地用户活动后，通过重新连接来唤醒主机；随后主机可以选择发送 `EXIT_SUSPEND`。注意，`EXIT_SUSPEND` 并非必需，因此应用不得依赖它来退出挂起状态。

由于消息按原样转交，主机发送的每一条 `SUSPEND` 或 `EXIT_SUSPEND` 都可能触发此回调，包括重复消息。如果应用需要在重连前后保持幂等的挂起行为，或需要按对端分别处理挂起行为（例如 HID DRE/BV-09-C），则必须自行跟踪，并使用从异步无连接（ACL）连接取得的对端身份作为索引。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | HID 设备对象。 |
| `suspended` | 进入挂起时为 `true`，退出挂起时为 `false`。 |

<a id="a71ee8022e59c83e2b28318432355663d"></a>

### `vc_unplug`

```c
void(* bt_hid_device_cb::vc_unplug) (struct bt_hid_device *hid)
```

虚拟线缆拔除（Virtual Cable Unplug）通知回调。

HID 主机发送 `VIRTUAL_CABLE_UNPLUG` 类型的 `HID_CONTROL` 消息时调用。根据 HID 规范 v1.1.2 第 3.1.2.2.3 节，接收方必须销毁为该对端保存的所有绑定（bonding）及虚拟线缆（Virtual Cable）信息。

协议栈代应用拆除 `INTR` 和 `CTRL` 通道，但不会清除绑定信息：清除绑定需要丢弃链路密钥，并视条件断开 ACL，这可能影响共享同一 ACL 的其他规范（profile）。因此，应用负责在适当时机清除绑定信息，例如：

原始示例（Example）：

```c
struct bt_conn *conn = bt_hid_device_get_conn(hid);

if (conn != NULL) {
        bt_br_unpair(bt_conn_get_dst_br(conn));
        bt_conn_unref(conn);
}
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | HID 设备对象。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/hid_device.h`

## 91.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/hid_device.h](https://docs.zephyrproject.org/latest/doxygen/html/hid__device_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_hid_device_register()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html#ga296d1b9695091507438261035d067c02)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_hid_device_get_conn](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html#ga63608252095d8c0638c6c43809e42553)
- [bt_br_unpair](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaccab07100ab64fd805fe1d468bc889ac)
- [bt_conn_get_dst_br](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga1b02a1ce8e48ad483d73d1efd803618c)
- [bt_conn_unref](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga4b18c6b22a9f02be0d7d078b2ce51ff6)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>
<a id="agroup__bt__conn_html_ga1b02a1ce8e48ad483d73d1efd803618c"></a>
<a id="agroup__bt__conn_html_ga4b18c6b22a9f02be0d7d078b2ce51ff6"></a>
<a id="agroup__bt__gap_html_gaccab07100ab64fd805fe1d468bc889ac"></a>
<a id="agroup__bt__hid__device_html_ga63608252095d8c0638c6c43809e42553"></a>
<a id="astructbt__conn_html"></a>

---

[上一章](P090_bt_hfp_hf_current_call_结构体.md) · [返回大纲](大纲.md) · [下一章](P092_bt_hid_host_cb_结构体.md)
