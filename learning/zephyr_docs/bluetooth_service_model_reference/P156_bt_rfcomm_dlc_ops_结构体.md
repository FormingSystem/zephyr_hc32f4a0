---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-156
title: bt_rfcomm_dlc_ops_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__rfcomm__dlc__ops.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第156章\_bt\_rfcomm\_dlc\_ops\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__rfcomm__dlc__ops.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

RFCOMM数据链路连接（DLC）的操作结构。

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

<a id="details"></a>

RFCOMM 数据链路连接（DLC）操作结构体。此对象必须在 DLC 的整个生命周期内保持有效且不变。注意：回调在线程上下文（thread context）中调用，绝不会在中断服务例程（ISR）中调用。回调究竟是在协议栈内部的上下文中执行，还是在触发它的 API 调用内同步执行，以及具体使用哪个上下文，均不属于 API 的保证范围，可能随版本变化。有关在回调中阻塞的风险及缓解方法，参见“回调执行上下文（Callback execution contexts）”。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 156.1\_数据成员（Data Fields）

<a id="r_aba1719c36e7a1dc9705994bcdf134e28"></a>

```c
void(* connected )(struct bt_rfcomm_dlc *dlc)
```

相关声明：[connected](#aba1719c36e7a1dc9705994bcdf134e28)、[bt_rfcomm_dlc](P155_bt_rfcomm_dlc_结构体.md)。

DLC 连接建立（connected）回调。

<a id="r_a4eeaf7b5db6c93e846a72797e6612d30"></a>

```c
void(* disconnected )(struct bt_rfcomm_dlc *dlc)
```

相关声明：[disconnected](#a4eeaf7b5db6c93e846a72797e6612d30)、[bt_rfcomm_dlc](P155_bt_rfcomm_dlc_结构体.md)。

DLC 连接断开（disconnected）回调。

<a id="r_ab8ef2f8c1d27eee20d0b5e7fce6f7354"></a>

```c
int(* recv )(struct bt_rfcomm_dlc *dlc, struct net_buf *buf)
```

相关声明：[recv](#ab8ef2f8c1d27eee20d0b5e7fce6f7354)、[bt_rfcomm_dlc](P155_bt_rfcomm_dlc_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

DLC 接收（recv）回调。

<a id="r_a3ba98c41e03c88f330cba0e3539a1cec"></a>

```c
void(* sent )(struct bt_rfcomm_dlc *dlc, int err)
```

相关声明：[sent](#a3ba98c41e03c88f330cba0e3539a1cec)、[bt_rfcomm_dlc](P155_bt_rfcomm_dlc_结构体.md)。

DLC 已发送（sent）回调。

## 156.2\_详细说明（Detailed Documentation）

<a id="aba1719c36e7a1dc9705994bcdf134e28"></a>

### `connected`

```c
void(* bt_rfcomm_dlc_ops::connected) (struct bt_rfcomm_dlc *dlc)
```

DLC 连接建立（connected）回调。

提供此回调后，每次连接完成（Connection completes）都会调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dlc` | 已建立连接的 DLC。 |

<a id="a4eeaf7b5db6c93e846a72797e6612d30"></a>

### `disconnected`

```c
void(* bt_rfcomm_dlc_ops::disconnected) (struct bt_rfcomm_dlc *dlc)
```

DLC 连接断开（disconnected）回调。

如果提供了此回调，每当 DLC 断开时都会调用它，包括入站或出站连接被拒绝、被取消的情况。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dlc` | 已断开连接的 DLC。 |

<a id="ab8ef2f8c1d27eee20d0b5e7fce6f7354"></a>

### `recv`

```c
int(* bt_rfcomm_dlc_ops::recv) (struct bt_rfcomm_dlc *dlc, struct net_buf *buf)
```

DLC 接收（recv）回调。

每当 DLC 收到数据时调用。

如果处理 `buf` 所需的工作无法立即完成，例如需要将数据交给另一线程或工作队列，则返回 `-EINPROGRESS` 以推迟完成处理。在这种情况下，回调不得阻塞。随后，协议栈会暂缓返还接收流控制信用（CFC 模式），或置 `FC=1`（非 CFC 模式），直到针对每个尚未完成的缓冲区都调用了 `bt_rfcomm_dlc_recv_complete`。

返回 `-EINPROGRESS` 时，应用取得 `buf` 引用的所有权，并且最终必须恰好调用一次 `bt_rfcomm_dlc_recv_complete`，传回同一个 `buf` 指针。在此次所有权交接前后，无需调用 `net_buf_ref` 或 `net_buf_unref`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dlc` | 接收数据的 DLC。 |
| `buf` | 包含传入数据的缓冲区（Buffer）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 数据已同步处理完毕；协议栈保留 `buf` 的所有权。 |
| `-EINPROGRESS` | 数据处理被推迟；应用现在拥有 `buf`，处理完成后必须调用 `bt_rfcomm_dlc_recv_complete`。 |

**警告（Warning）**：警告：必须在此回调返回后，从线程上下文调用 `bt_rfcomm_dlc_recv_complete`。如果在 `recv` 回调内部、即其返回之前调用，会使进行中计数器下溢，并导致 `bt_rfcomm_dlc_recv_complete` 以 `-EINVAL` 失败。

**返回（Returns）**：返回值：其他负值错误码；协议栈将主动断开 DLC。

<a id="a3ba98c41e03c88f330cba0e3539a1cec"></a>

### `sent`

```c
void(* bt_rfcomm_dlc_ops::sent) (struct bt_rfcomm_dlc *dlc, int err)
```

DLC 已发送（sent）回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dlc` | 已发送数据的 DLC。 |
| `err` | 发送结果。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/rfcomm.h`

## 156.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/rfcomm.h](https://docs.zephyrproject.org/latest/doxygen/html/rfcomm_8h_source.html)
- [bt_rfcomm_dlc](P155_bt_rfcomm_dlc_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [回调执行上下文（Callback execution contexts）](../bluetooth/P004_低功耗蓝牙主机.md#bluetooth-callback-contexts)
- [bt_rfcomm_dlc_recv_complete](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga2ce765351798976136c3096a9a7f9465)
- [net_buf_ref](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga29387b2a672bf2bb8739046a46f3601f)
- [net_buf_unref](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gabedcb728bc2fc0c2b5319a8fd87e8273)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P155_bt_rfcomm_dlc_结构体.md) · [返回大纲](大纲.md) · [下一章](P157_bt_rfcomm_rpn_结构体.md)
