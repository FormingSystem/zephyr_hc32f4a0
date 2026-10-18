---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-79
title: bt_iso_chan_ops_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__chan__ops.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第79章\_bt\_iso\_chan\_ops\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__chan__ops.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

等时信道（ISO Channel）的操作结构。

```c
#include <zephyr/bluetooth/iso.h>
```

<a id="details"></a>

等时通道操作结构（ISO Channel operations structure）。注意（Note）：回调在线程上下文（Thread context）中执行，绝不会从中断服务程序（ISR）调用。回调是在协议栈内部上下文中调用，还是在触发它的 API 调用中同步执行，以及具体使用哪个上下文，都不是 API 契约的一部分，可能随版本变化。有关在回调中阻塞的风险及缓解方法，参见回调执行上下文（Callback execution contexts）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 79.1\_数据成员（Data Fields）

<a id="r_a6b0e51770158da7b728e1084a8e44504"></a>

```c
void(* connected )(struct bt_iso_chan *chan)
```

相关声明：[connected](#a6b0e51770158da7b728e1084a8e44504)、[bt_iso_chan](P077_bt_iso_chan_结构体.md)。

通道连接回调（Channel connected callback）。

<a id="r_a2069849352019362e5dc7d68f835f359"></a>

```c
void(* disconnected )(struct bt_iso_chan *chan, uint8_t reason)
```

相关声明：[disconnected](#a2069849352019362e5dc7d68f835f359)、[bt_iso_chan](P077_bt_iso_chan_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通道断开回调（Channel disconnected callback）。

<a id="r_a7bf9fe04f42bacd59f623aa28a3b0665"></a>

```c
struct net_buf *(* alloc_buf )(struct bt_iso_chan *chan)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[alloc_buf](#a7bf9fe04f42bacd59f623aa28a3b0665)、[bt_iso_chan](P077_bt_iso_chan_结构体.md)。

通道分配缓冲区回调（Channel alloc_buf callback）。

<a id="r_a6d5d9423fff83f8f337f97b3fc018f39"></a>

```c
void(* recv )(struct bt_iso_chan *chan, const struct bt_iso_recv_info *info, struct net_buf *buf)
```

相关声明：[recv](#a6d5d9423fff83f8f337f97b3fc018f39)、[bt_iso_chan](P077_bt_iso_chan_结构体.md)、[bt_iso_recv_info](P086_bt_iso_recv_info_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

通道接收回调（Channel recv callback）。

<a id="r_a048954070628229b8aacd373de1fb236"></a>

```c
void(* sent )(struct bt_iso_chan *chan)
```

相关声明：[sent](#a048954070628229b8aacd373de1fb236)、[bt_iso_chan](P077_bt_iso_chan_结构体.md)。

通道发送完成回调（Channel sent callback）。

<a id="r_a750ac5c12155602a32b1f02bb2dc8fba"></a>

```c
void(* send_failed )(struct bt_iso_chan *chan, int err)
```

相关声明：[send_failed](#a750ac5c12155602a32b1f02bb2dc8fba)、[bt_iso_chan](P077_bt_iso_chan_结构体.md)。

通道发送失败回调（Channel send failed callback）。

## 79.2\_详细说明（Detailed Documentation）

<a id="a7bf9fe04f42bacd59f623aa28a3b0665"></a>

### `alloc_buf`

```c
struct net_buf *(* bt_iso_chan_ops::alloc_buf) (struct bt_iso_chan *chan)
```

通道分配缓冲区回调（Channel alloc_buf callback）。

提供此回调后，通道会通过它分配缓冲区（Buffers），以存储传入数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan` | 请求缓冲区（Buffer）的通道。 |

**返回（Returns）**：返回值（Returns）：已分配的缓冲区（Allocated buffer）。

<a id="a6b0e51770158da7b728e1084a8e44504"></a>

### `connected`

```c
void(* bt_iso_chan_ops::connected) (struct bt_iso_chan *chan)
```

通道连接回调（Channel connected callback）。

提供此回调后，每次连接完成（Connection completes）都会调用。

对于外设（Peripheral），调用此回调时已设置服务质量值（QoS values），参见 `bt_iso_chan_io_qos`。但外设没有关于重传次数（RTN）的信息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan` | 已连接的通道（Connected channel）。 |

<a id="a2069849352019362e5dc7d68f835f359"></a>

### `disconnected`

```c
void(* bt_iso_chan_ops::disconnected) (struct bt_iso_chan *chan, uint8_t reason)
```

通道断开回调（Channel disconnected callback）。

提供此回调后，每次通道断开（Disconnected）都会调用，包括连接被拒绝或设置安全性失败的情况。

如果通道曾成功建立，即已为其调用 `bt_iso_chan_ops::connected`，则通道对象（Channel object）仍有效，不得用 `memset` 将其内存清零，也不得以其他方式释放。为避免问题，建议使用 `k_work_submit` 或类似机制，避免在回调内覆盖任何数据。

由于上述原因，仍可对 `chan` 使用 `bt_iso_chan_get_info()`。

如果 `chan` 是单播连接等时流通道（Unicast CIS channel），且其关联的异步面向连接链路（ACL）也断开，则此回调始终先于 `bt_conn_cb::disconnected` 调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan` | 已断开的通道（Disconnected channel）。 |
| `reason` | 表示断开原因的 `BT_HCI_ERR_*` 值。 |

<a id="a6d5d9423fff83f8f337f97b3fc018f39"></a>

### `recv`

```c
void(* bt_iso_chan_ops::recv) (struct bt_iso_chan *chan, const struct bt_iso_recv_info *info, struct net_buf *buf)
```

通道接收回调（Channel recv callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan` | 正在接收数据的通道（Channel）。 |
| `buf` | 包含传入数据的缓冲区（Buffer）。 |
| `info` | 指向缓冲区元数据的指针，其生命周期与 `net_buf` 的生命周期关联。序列号和时间戳等元数据可以由蓝牙控制器提供。 |

<a id="a750ac5c12155602a32b1f02bb2dc8fba"></a>

### `send_failed`

```c
void(* bt_iso_chan_ops::send_failed) (struct bt_iso_chan *chan, int err)
```

通道发送失败回调（Channel send failed callback）。

如果调用 `bt_iso_chan_send()` 成功，但之后在请求发给蓝牙控制器（Bluetooth Controller）之前发送操作失败，则调用此回调。`chan` 已断开时可能发生这种情况。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan` | 发送操作失败的通道（Channel）。 |
| `err` | 发送失败原因（Send failure reason）。 |

<a id="a048954070628229b8aacd373de1fb236"></a>

### `sent`

```c
void(* bt_iso_chan_ops::sent) (struct bt_iso_chan *chan)
```

通道发送完成回调（Channel sent callback）。

控制器将服务数据单元（Service Data Unit，SDU）标记为完成后调用此回调。控制器何时进行标记取决于其实现，可能在 SDU 入发送队列之后，也可能在通过空口发出或被清除之后。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan` | 已发送数据的通道（Channel）。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/iso.h`

## 79.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/iso.h](https://docs.zephyrproject.org/latest/doxygen/html/iso_8h_source.html)
- [bt_iso_chan](P077_bt_iso_chan_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bt_iso_recv_info](P086_bt_iso_recv_info_结构体.md)
- [回调执行上下文（Callback execution contexts）](../bluetooth/P004_低功耗蓝牙主机.md#bluetooth-callback-contexts)
- [bt_iso_chan_io_qos](P078_bt_iso_chan_io_qos_结构体.md)
- [k_work_submit](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gace61b59575093d7442f39ccb7be686d7)
- [bt_iso_chan_get_info()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga75e58ed5bfa48f84000f1ce974d649c6)
- [bt_conn_cb::disconnected](P008_bt_conn_cb_结构体.md#a8b8983b5b5b05c9e2dae242485b6c914)
- [bt_iso_chan_send()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga0dbb89a133011a833be7d18161471c6a)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P078_bt_iso_chan_io_qos_结构体.md) · [返回大纲](大纲.md) · [下一章](P080_bt_iso_chan_path_结构体.md)
