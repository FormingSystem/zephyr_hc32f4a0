---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-102
title: bt_l2cap_chan_ops_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__chan__ops.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第102章\_bt\_l2cap\_chan\_ops\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__chan__ops.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

逻辑链路控制与适配协议（L2CAP）的信道操作结构。

```c
#include <zephyr/bluetooth/l2cap.h>
```

<a id="details"></a>

L2CAP 通道操作结构体。此对象必须在通道的整个生命周期内保持有效且不变。注意：回调在线程上下文（thread context）中调用，绝不会在中断服务例程（ISR）中调用。回调究竟是在协议栈内部的上下文中执行，还是在触发它的 API 调用内同步执行，以及具体使用哪个上下文，均不属于 API 的保证范围，可能随版本变化。有关在回调中阻塞的风险及缓解方法，参见“回调执行上下文（Callback execution contexts）”。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 102.1\_数据成员（Data Fields）

<a id="r_a3a4dd75a11c9867adcade6d288dec2de"></a>

```c
void(* connected )(struct bt_l2cap_chan *chan)
```

相关声明：[connected](#a3a4dd75a11c9867adcade6d288dec2de)、[bt_l2cap_chan](P101_bt_l2cap_chan_结构体.md)。

通道连接回调（Channel connected callback）。

<a id="r_a2e5fcc77a5174de6e3933bb6a14e4ad3"></a>

```c
void(* disconnected )(struct bt_l2cap_chan *chan)
```

相关声明：[disconnected](#a2e5fcc77a5174de6e3933bb6a14e4ad3)、[bt_l2cap_chan](P101_bt_l2cap_chan_结构体.md)。

通道断开回调（Channel disconnected callback）。

<a id="r_a12f3290f9bd04fb5fe562c620dff6984"></a>

```c
void(* encrypt_change )(struct bt_l2cap_chan *chan, uint8_t hci_status)
```

相关声明：[encrypt_change](#a12f3290f9bd04fb5fe562c620dff6984)、[bt_l2cap_chan](P101_bt_l2cap_chan_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通道加密变化（`encrypt_change`）回调。

<a id="r_abb165dbe118dfbb3577d3e56a00a5735"></a>

```c
struct net_buf *(* alloc_seg )(struct bt_l2cap_chan *chan)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[alloc_seg](#abb165dbe118dfbb3577d3e56a00a5735)、[bt_l2cap_chan](P101_bt_l2cap_chan_结构体.md)。

通道分段缓冲区分配（`alloc_seg`）回调。

<a id="r_ab973539dd8b5e3ab115042a03362f141"></a>

```c
struct net_buf *(* alloc_buf )(struct bt_l2cap_chan *chan)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[alloc_buf](#ab973539dd8b5e3ab115042a03362f141)、[bt_l2cap_chan](P101_bt_l2cap_chan_结构体.md)。

通道分配缓冲区回调（Channel alloc_buf callback）。

<a id="r_a0ab419d3c52c08e0dfda236466d7cadd"></a>

```c
int(* recv )(struct bt_l2cap_chan *chan, struct net_buf *buf)
```

相关声明：[recv](#a0ab419d3c52c08e0dfda236466d7cadd)、[bt_l2cap_chan](P101_bt_l2cap_chan_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

通道接收回调（Channel recv callback）。

<a id="r_a770c09f3fb10c9d1e069333d22803d1a"></a>

```c
void(* sent )(struct bt_l2cap_chan *chan)
```

相关声明：[sent](#a770c09f3fb10c9d1e069333d22803d1a)、[bt_l2cap_chan](P101_bt_l2cap_chan_结构体.md)。

通道发送完成回调（Channel sent callback）。

<a id="r_a4be7fadf07368750cc33cf034d3073e7"></a>

```c
void(* status )(struct bt_l2cap_chan *chan, atomic_t *status)
```

相关声明：[status](#a4be7fadf07368750cc33cf034d3073e7)、[bt_l2cap_chan](P101_bt_l2cap_chan_结构体.md)、[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)。

通道状态（status）回调。

<a id="r_a6d974d0e472626cb1e5cd898a3dcbca6"></a>

```c
void(* released )(struct bt_l2cap_chan *chan)
```

相关声明：[released](#a6d974d0e472626cb1e5cd898a3dcbca6)、[bt_l2cap_chan](P101_bt_l2cap_chan_结构体.md)。

<a id="r_afba426353897bc3a57c936a98acab839"></a>

```c
void(* reconfigured )(struct bt_l2cap_chan *chan)
```

相关声明：[reconfigured](#afba426353897bc3a57c936a98acab839)、[bt_l2cap_chan](P101_bt_l2cap_chan_结构体.md)。

通道重新配置（reconfigured）回调。

<a id="r_a7759a713038d74748952d5f2eb712429"></a>

```c
void(* seg_recv )(struct bt_l2cap_chan *chan, size_t sdu_len, off_t seg_offset, struct net_buf_simple *seg)
```

相关声明：[seg_recv](#a7759a713038d74748952d5f2eb712429)、[bt_l2cap_chan](P101_bt_l2cap_chan_结构体.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

直接处理 L2CAP 分段（segments）。

## 102.2\_详细说明（Detailed Documentation）

<a id="ab973539dd8b5e3ab115042a03362f141"></a>

### `alloc_buf`

```c
struct net_buf *(* bt_l2cap_chan_ops::alloc_buf) (struct bt_l2cap_chan *chan)
```

通道分配缓冲区回调（Channel alloc_buf callback）。

如果提供了此回调，通道将使用它分配用于保存接收数据的缓冲区。需要分段的通道必须设置此回调。如果应用没有设置回调，L2CAP 服务数据单元（SDU）的 MTU 将被限制为 `BT_L2CAP_SDU_RX_MTU`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan` | 请求缓冲区（Buffer）的通道。 |

**说明（Note）**：注意：协议栈在缓冲区用户数据的前两个字节中保存已接收分段的数量。此回调返回的缓冲区，其用户数据大小必须至少为 `sizeof(uint16_t)`。

**返回（Returns）**：返回值（Returns）：已分配的缓冲区（Allocated buffer）。

<a id="abb165dbe118dfbb3577d3e56a00a5735"></a>

### `alloc_seg`

```c
struct net_buf *(* bt_l2cap_chan_ops::alloc_seg) (struct bt_l2cap_chan *chan)
```

通道分段缓冲区分配（`alloc_seg`）回调。

如果提供了此回调，通道将使用它分配用于保存分段的缓冲区。这样可避免使用大型 SDU 缓冲区存储可能小得多的 PDU 所造成的浪费。若提供此回调，它必须返回有效的缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan` | 请求缓冲区（Buffer）的通道。 |

**返回（Returns）**：返回值（Returns）：已分配的缓冲区（Allocated buffer）。

<a id="a3a4dd75a11c9867adcade6d288dec2de"></a>

### `connected`

```c
void(* bt_l2cap_chan_ops::connected) (struct bt_l2cap_chan *chan)
```

通道连接回调（Channel connected callback）。

提供此回调后，每次连接完成（Connection completes）都会调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan` | 已连接的通道（Connected channel）。 |

<a id="a2e5fcc77a5174de6e3933bb6a14e4ad3"></a>

### `disconnected`

```c
void(* bt_l2cap_chan_ops::disconnected) (struct bt_l2cap_chan *chan)
```

通道断开回调（Channel disconnected callback）。

如果提供了此回调，每当通道断开时都会调用它，包括连接被拒绝的情况。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan` | 已断开的通道（Disconnected channel）。 |

<a id="a12f3290f9bd04fb5fe562c620dff6984"></a>

### `encrypt_change`

```c
void(* bt_l2cap_chan_ops::encrypt_change) (struct bt_l2cap_chan *chan, uint8_t hci_status)
```

通道加密变化（`encrypt_change`）回调。

如果提供了此回调，每当安全级别发生变化（间接表示链路加密完成），或者身份验证过程失败时都会调用它。在这两种情况下，安全过程的发起方和响应方都会收到最终状态（HCI 状态）；此状态来自本地主机控制器发出的加密和身份验证相关事件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan` | 加密状态已发生变化的通道。 |
| `hci_status` | 因通道安全要求而执行的安全过程所产生的 HCI 状态。此值由 HCI 层填入：成功时设为 0；安全过程或身份验证失败时设为非零值，参见 HCI 错误码（HCI Error Codes）。 |

<a id="afba426353897bc3a57c936a98acab839"></a>

### `reconfigured`

```c
void(* bt_l2cap_chan_ops::reconfigured) (struct bt_l2cap_chan *chan)
```

通道重新配置（reconfigured）回调。

如果提供了此回调，每当对端或本地设备请求重新配置时都会调用它。应用可检查 `chan->le` 端点，获取更新后的 MTU 和最大 PDU 大小（MPS）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan` | 已重新配置的通道。 |

<a id="a0ab419d3c52c08e0dfda236466d7cadd"></a>

### `recv`

```c
int(* bt_l2cap_chan_ops::recv) (struct bt_l2cap_chan *chan, struct net_buf *buf)
```

通道接收回调（Channel recv callback）。

如果应用返回 `-EINPROGRESS`，则应用取得 `buf` 中引用的所有权。也就是说，可直接将此指针值传给 `bt_l2cap_chan_recv_complete`，无需调用 `net_buf_ref` 或 `net_buf_unref`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan` | 正在接收数据的通道（Channel）。 |
| `buf` | 包含传入数据的缓冲区（Buffer）。 |

**说明（Note）**：注意：此回调是必需的，除非已启用 `CONFIG_BT_L2CAP_SEG_RECV` 并提供了 `seg_recv`。

**返回（Returns）**：返回值：成功时返回 0，错误时返回负值。如果用户需要在数据处理完毕后调用 `bt_l2cap_chan_recv_complete` 进行确认，则返回 `-EINPROGRESS`；调用时必须传回收到的缓冲区，并保留其原始 `user_data`，其中包含此数据包使用的分段数或信用数。

<a id="a6d974d0e472626cb1e5cd898a3dcbca6"></a>

### `released`

```c
void(* bt_l2cap_chan_ops::released) (struct bt_l2cap_chan *chan)
```

<a id="a7759a713038d74748952d5f2eb712429"></a>

### `seg_recv`

```c
void(* bt_l2cap_chan_ops::seg_recv) (struct bt_l2cap_chan *chan, size_t sdu_len, off_t seg_offset, struct net_buf_simple *seg)
```

直接处理 L2CAP 分段（segments）。

这是 `bt_l2cap_chan_ops::recv` 的替代方式；二者不能同时使用。

每收到一个分段就立即调用。

与 `bt_l2cap_chan_ops::recv` 不同，此方式采用显式流控制。每调用一次此处理函数，对端就永久消耗一个信用（credit）。使用 `bt_l2cap_chan_give_credits` 授予信用。

`seg_offset == 0` 标志着一个 SDU 的开始；`seg_offset + seg->len == sdu_len` 标志着一个 SDU 的结束。

协议栈保证：

- 发送方拥有相应的信用（credit）。
- SDU 长度不超过 MTU。
- 分段长度不超过 MPS。

此外，L2CAP 协议还具有以下性质：

- 分段按顺序到达。
- SDU 之间不能交错传输，也不能中途终止。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan` | 接收通道。 |
| `sdu_len` | 此分段所属 SDU 的字节长度。 |
| `seg_offset` | 此分段在 SDU 中的字节偏移量。 |
| `seg` | 分段载荷（segment payload）。 |

**说明（Note）**：注意：使用此替代 API 时，应用负责设置接收（RX）MTU 和 MPS。MPS 不得超过 `BT_L2CAP_RX_MTU`。

<a id="a770c09f3fb10c9d1e069333d22803d1a"></a>

### `sent`

```c
void(* bt_l2cap_chan_ops::sent) (struct bt_l2cap_chan *chan)
```

通道发送完成回调（Channel sent callback）。

控制器将 SDU 标记为完成后，会调用此回调。控制器何时这样做取决于具体实现：可能是在 SDU 加入发送队列后，也可能是在其通过空中接口发送后。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan` | 已发送数据的通道（Channel）。 |

<a id="a4be7fadf07368750cc33cf034d3073e7"></a>

### `status`

```c
void(* bt_l2cap_chan_ops::status) (struct bt_l2cap_chan *chan, atomic_t *status)
```

通道状态（status）回调。

如果提供了此回调，每当通道状态变化时都会调用它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan` | 状态发生变化的通道。 |
| `status` | 通道状态。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/l2cap.h`

## 102.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/l2cap.h](https://docs.zephyrproject.org/latest/doxygen/html/l2cap_8h_source.html)
- [bt_l2cap_chan](P101_bt_l2cap_chan_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [回调执行上下文（Callback execution contexts）](../bluetooth/P004_低功耗蓝牙主机.md#bluetooth-callback-contexts)
- [BT_L2CAP_SDU_RX_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga13b93a8f09157fbcf739fa4949840efe)
- [CONFIG_BT_L2CAP_SEG_RECV](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_SEG_RECV)
- [bt_l2cap_chan_recv_complete](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gad53f5fc31314121ff84e740879eae3cf)
- [net_buf_ref](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga29387b2a672bf2bb8739046a46f3601f)
- [net_buf_unref](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gabedcb728bc2fc0c2b5319a8fd87e8273)
- [bt_l2cap_chan_give_credits](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga9bc950a929fc2bdb1463c268cea478b6)
- [BT_L2CAP_RX_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga6e458a1758e5012755f3b97f8348c966)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P101_bt_l2cap_chan_结构体.md) · [返回大纲](大纲.md) · [下一章](P103_bt_l2cap_fixed_chan_结构体.md)
