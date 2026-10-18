---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-92
title: bt_hid_host_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hid__host__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第92章\_bt\_hid\_host\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hid__host__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

由人机接口设备主机（HID Host）应用提供的回调。

```c
#include <zephyr/bluetooth/classic/hid_host.h>
```

<a id="details"></a>

由 HID 主机（Host）应用提供的回调。通过 `bt_hid_host_register()` 注册，以接收已连接 HID 设备的事件。任何时刻最多只能有一个尚未完成的控制通道事务，参见 HID 规范 v1.1.2 第 3.2.1 节；在响应到达之前，其他请求返回 `-EBUSY`。每个请求都有自己的结果回调，用于报告设备提供的 `HANDSHAKE` 结果码，因此只有设备作出应答时才会调用。按照 HID 规范 v1.1.2 第 5.2.6 节，始终没有应答的事务被视为连接丢失：协议栈拆除 HID 关联，改为调用 `disconnected` 回调。由于最多只有一个事务尚未完成，应用若在发出请求后收到 `disconnected`，就能确定该请求已丢失。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 92.1\_数据成员（Data Fields）

<a id="r_a973e729e0633f5fbecc2c6270ea15d6c"></a>

```c
void(* connected )(struct bt_hid_host *hid)
```

相关声明：[connected](#a973e729e0633f5fbecc2c6270ea15d6c)。

HID 连接已建立。

<a id="r_a8f5f6486fa37551922b18a62f8b75730"></a>

```c
void(* disconnected )(struct bt_hid_host *hid)
```

相关声明：[disconnected](#a8f5f6486fa37551922b18a62f8b75730)。

HID 连接已终止。

<a id="r_a78389dc6d2b89f4c16b95268a0c524e7"></a>

```c
void(* input_report )(struct bt_hid_host *hid, struct net_buf *buf)
```

相关声明：[input_report](#a78389dc6d2b89f4c16b95268a0c524e7)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

在中断通道上收到输入报告。

<a id="r_aabeb2d9589813690eec77297113090cd"></a>

```c
void(* get_report )(struct bt_hid_host *hid, uint8_t result_code, uint8_t type, struct net_buf *buf)
```

相关声明：[get_report](#aabeb2d9589813690eec77297113090cd)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

`GET_REPORT` 的结果。

<a id="r_a32df7ffd5ee0092297a146925d888dd8"></a>

```c
void(* set_report )(struct bt_hid_host *hid, uint8_t result_code)
```

相关声明：[set_report](#a32df7ffd5ee0092297a146925d888dd8)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

`SET_REPORT` 的结果。

<a id="r_a94cf9747616471c4ba2cec2057f714a9"></a>

```c
void(* get_protocol )(struct bt_hid_host *hid, uint8_t result_code, uint8_t protocol)
```

相关声明：[get_protocol](#a94cf9747616471c4ba2cec2057f714a9)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

`GET_PROTOCOL` 的结果。

<a id="r_a412114fad2e0624f96803827be7cd54a"></a>

```c
void(* set_protocol )(struct bt_hid_host *hid, uint8_t result_code)
```

相关声明：[set_protocol](#a412114fad2e0624f96803827be7cd54a)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

`SET_PROTOCOL` 的结果。

<a id="r_a26bd138b7be11a6402845fbfb7fdfbb3"></a>

```c
void(* vc_unplug )(struct bt_hid_host *hid)
```

相关声明：[vc_unplug](#a26bd138b7be11a6402845fbfb7fdfbb3)。

收到设备发送的虚拟线缆拔除（Virtual Cable Unplug）消息。

## 92.2\_详细说明（Detailed Documentation）

<a id="a973e729e0633f5fbecc2c6270ea15d6c"></a>

### `connected`

```c
void(* bt_hid_host_cb::connected) (struct bt_hid_host *hid)
```

HID 连接已建立。

当控制和中断 L2CAP 通道均已打开，且 HID 关联已准备好进行数据传输时调用。对于出站连接（由主机发起）和入站连接（由设备发起的重新连接），都会调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | HID 主机实例。 |

<a id="a8f5f6486fa37551922b18a62f8b75730"></a>

### `disconnected`

```c
void(* bt_hid_host_cb::disconnected) (struct bt_hid_host *hid)
```

HID 连接已终止。

HID 关联完全拆除后调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | HID 主机实例。 |

<a id="a94cf9747616471c4ba2cec2057f714a9"></a>

### `get_protocol`

```c
void(* bt_hid_host_cb::get_protocol) (struct bt_hid_host *hid, uint8_t result_code, uint8_t protocol)
```

`GET_PROTOCOL` 的结果。

每个 `GET_PROTOCOL` 事务都会调用此回调，无论设备使用携带协议模式八位字节的 `DATA` 消息应答，还是通过 `HANDSHAKE` 拒绝请求，参见 HID 规范 v1.1.2 第 3.2.1.5 节。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | HID 主机实例。 |
| `result_code` | `BT_HID_HS_RSP_SUCCESS`，或者设备回复的 `BT_HID_HS_RSP_ERR_*` 代码。 |
| `protocol` | 设备的协议模式：`BT_HID_PROTOCOL_BOOT_MODE` 或 `BT_HID_PROTOCOL_REPORT_MODE`。当 `result_code` 不是 `BT_HID_HS_RSP_SUCCESS` 时，此值未定义。 |

<a id="aabeb2d9589813690eec77297113090cd"></a>

### `get_report`

```c
void(* bt_hid_host_cb::get_report) (struct bt_hid_host *hid, uint8_t result_code, uint8_t type, struct net_buf *buf)
```

`GET_REPORT` 的结果。

每个 `GET_REPORT` 事务都会调用此回调，无论设备使用 `DATA` 消息应答，还是通过 `HANDSHAKE` 拒绝请求，参见 HID 规范 v1.1.2 第 3.2.1.1 节，因此可在同一处处理事务结果。

载荷按收到时的原样交付；如果使用报告 ID，则载荷以报告 ID 开头。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | HID 主机实例。 |
| `result_code` | `BT_HID_HS_RSP_SUCCESS`，或者设备回复的 `BT_HID_HS_RSP_ERR_*` 代码。 |
| `type` | 报告类型：`INPUT`、`OUTPUT` 或 `FEATURE`。当 `result_code` 不是 `BT_HID_HS_RSP_SUCCESS` 时，此值未定义。 |
| `buf` | 报告载荷，其所有权仍由协议栈持有；未收到 `DATA` 消息时为 `NULL`。 |

<a id="a78389dc6d2b89f4c16b95268a0c524e7"></a>

### `input_report`

```c
void(* bt_hid_host_cb::input_report) (struct bt_hid_host *hid, struct net_buf *buf)
```

在中断通道上收到输入报告。

由 HID 设备发送的异步输入报告数据。

载荷按收到时的原样交付。当报告描述符声明了报告 ID，或设备处于引导协议模式（Boot Protocol Mode）时，载荷以报告 ID 开头；只有应用能够判断这些情况。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | HID 主机实例。 |
| `buf` | 报告载荷；其所有权仍由协议栈持有。 |

<a id="a412114fad2e0624f96803827be7cd54a"></a>

### `set_protocol`

```c
void(* bt_hid_host_cb::set_protocol) (struct bt_hid_host *hid, uint8_t result_code)
```

`SET_PROTOCOL` 的结果。

设备以 `HANDSHAKE` 应答 `SET_PROTOCOL` 请求时调用；这是 SET 请求唯一可能收到的回复，参见 HID 规范 v1.1.2 第 3.2.1.6 节。只有 `result_code` 为 `BT_HID_HS_RSP_SUCCESS` 时，所请求的模式才已启用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | HID 主机实例。 |
| `result_code` | `BT_HID_HS_RSP_SUCCESS`，或者设备回复的 `BT_HID_HS_RSP_ERR_*` 代码。 |

<a id="a32df7ffd5ee0092297a146925d888dd8"></a>

### `set_report`

```c
void(* bt_hid_host_cb::set_report) (struct bt_hid_host *hid, uint8_t result_code)
```

`SET_REPORT` 的结果。

设备以 `HANDSHAKE` 应答 `SET_REPORT` 请求时调用；这是 SET 请求唯一可能收到的回复，参见 HID 规范 v1.1.2 第 3.2.1.2 节。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | HID 主机实例。 |
| `result_code` | `BT_HID_HS_RSP_SUCCESS`，或者设备回复的 `BT_HID_HS_RSP_ERR_*` 代码。 |

<a id="a26bd138b7be11a6402845fbfb7fdfbb3"></a>

### `vc_unplug`

```c
void(* bt_hid_host_cb::vc_unplug) (struct bt_hid_host *hid)
```

收到设备发送的虚拟线缆拔除（Virtual Cable Unplug）消息。

远端 HID 设备已发送 `VIRTUAL_CABLE_UNPLUG` 控制消息，协议栈会断开 HID 关联。HID 规范 v1.1.2 第 3.1.2.2.3 节还要求销毁绑定信息；这由应用负责，因为 `bt_br_unpair()` 会断开整个 ACL，连同运行于其上的其他规范连接一起断开。

拔除消息到达时仍未完成的控制事务会被丢弃，因此永远不会调用其结果回调：按照第 3.1.2.2.3 节，接收方会丢弃所有待处理的控制传输。正在等待此类回复的应用必须将此回调视为该事务的结果。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | HID 主机实例。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/hid_host.h`

## 92.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/hid_host.h](https://docs.zephyrproject.org/latest/doxygen/html/hid__host_8h_source.html)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_hid_host_register()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#ga86d49efef335609422f23b52717c9e1b)
- [bt_br_unpair()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaccab07100ab64fd805fe1d468bc889ac)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P091_bt_hid_device_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P093_bt_hrs_cb_结构体.md)
