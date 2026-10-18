---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-38
title: bt_cap_initiator_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__initiator__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_bt\_cap\_initiator\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__initiator__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通用音频配置文件（Common Audio Profile，CAP）过程的回调结构体。

```c
#include <zephyr/bluetooth/audio/cap.h>
```

<a id="details"></a>

通用音频配置文件（Common Audio Profile，CAP）过程的回调结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 38.1\_数据成员（Data Fields）

<a id="r_a642a2f48e8f870bb1681ba58aa119de9"></a>

```c
void(* unicast_discovery_complete )(struct bt_conn *conn, int err, const struct bt_csip_set_coordinator_set_member *member, const struct bt_csip_set_coordinator_csis_inst *csis_inst)
```

相关声明：[unicast_discovery_complete](#a642a2f48e8f870bb1681ba58aa119de9)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_csip_set_coordinator_set_member](P058_bt_csip_set_coordinator_set_member_结构体.md)、[bt_csip_set_coordinator_csis_inst](P056_bt_csip_set_coordinator_csis_inst_结构体.md)。

`bt_cap_initiator_unicast_discover()` 的回调（Callback）。

<a id="r_aa70de1dda73ffdcbb8287f8f174984ea"></a>

```c
void(* unicast_start_complete )(int err, struct bt_conn *conn)
```

相关声明：[unicast_start_complete](#aa70de1dda73ffdcbb8287f8f174984ea)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

`bt_cap_initiator_unicast_audio_start()` 的回调（Callback）。

<a id="r_a64c9b0fb0bdfcc7434d8f2854a20a666"></a>

```c
void(* unicast_start_codec_configured )(void)
```

相关声明：[unicast_start_codec_configured](#a64c9b0fb0bdfcc7434d8f2854a20a666)。

所有流的编解码器配置（Codec configuration）已完成。

<a id="r_a5ef6349113a1c786a0441b6c494286d1"></a>

```c
void(* unicast_start_qos_configured )(void)
```

相关声明：[unicast_start_qos_configured](#a5ef6349113a1c786a0441b6c494286d1)。

所有流的服务质量配置（QoS configuration）已完成。

<a id="r_a06b2f73a6f6f8f3f88cd4c5bd87f4fbc"></a>

```c
void(* unicast_start_enabled )(void)
```

相关声明：[unicast_start_enabled](#a06b2f73a6f6f8f3f88cd4c5bd87f4fbc)。

所有流均已启用（Enabled）。

<a id="r_a8452b3c6775d1608272893719dd3887d"></a>

```c
void(* unicast_start_connected )(void)
```

相关声明：[unicast_start_connected](#a8452b3c6775d1608272893719dd3887d)。

所有流的连接等时流（CIS）均已连接。

<a id="r_a65d8dd89661f92b2e71e90b69a8b4320"></a>

```c
void(* unicast_start_started )(void)
```

相关声明：[unicast_start_started](#a65d8dd89661f92b2e71e90b69a8b4320)。

所有流均已启动（Started）。

<a id="r_a95266741841fca83cd2769c76652154e"></a>

```c
void(* unicast_update_complete )(int err, struct bt_conn *conn)
```

相关声明：[unicast_update_complete](#a95266741841fca83cd2769c76652154e)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

`bt_cap_initiator_unicast_audio_update()` 的回调（Callback）。

<a id="r_a2e910a82209d144878b6c69c1b2723ba"></a>

```c
void(* unicast_stop_complete )(int err, struct bt_conn *conn)
```

相关声明：[unicast_stop_complete](#a2e910a82209d144878b6c69c1b2723ba)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

`bt_cap_initiator_unicast_audio_stop()` 的回调（Callback）。

<a id="r_a8001c24d64df0881dbfd78382c2a2db7"></a>

```c
void(* unicast_stop_disabled )(void)
```

相关声明：[unicast_stop_disabled](#a8001c24d64df0881dbfd78382c2a2db7)。

所有流均已禁用（Disabled）。

<a id="r_a8c20d933b9ee1c1412d7ad719ff24683"></a>

```c
void(* unicast_stop_stopped )(void)
```

相关声明：[unicast_stop_stopped](#a8c20d933b9ee1c1412d7ad719ff24683)。

所有流均已停止（Stopped）。

<a id="r_a8f659ac17a242eab12c404f59e42d149"></a>

```c
void(* unicast_stop_released )(void)
```

相关声明：[unicast_stop_released](#a8f659ac17a242eab12c404f59e42d149)。

所有流均已释放（Released）。

<a id="r_afd9b20a78b9115409d4301c8d71c4405"></a>

```c
void(* broadcast_started )(struct bt_cap_broadcast_source *source)
```

相关声明：[broadcast_started](#afd9b20a78b9115409d4301c8d71c4405)、[bt_cap_broadcast_source](P017_bt_cap_broadcast_source_结构体.md)。

广播音频源已启动，其所有流均已准备好传输音频数据。

<a id="r_a85451f4cbf0c8e4d061a2b50b892529d"></a>

```c
void(* broadcast_stopped )(struct bt_cap_broadcast_source *source, uint8_t reason)
```

相关声明：[broadcast_stopped](#a85451f4cbf0c8e4d061a2b50b892529d)、[bt_cap_broadcast_source](P017_bt_cap_broadcast_source_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

广播音频源已停止，其所有流均未准备好传输音频数据。

## 38.2\_详细说明（Detailed Documentation）

<a id="afd9b20a78b9115409d4301c8d71c4405"></a>

### `broadcast_started`

```c
void(* bt_cap_initiator_cb::broadcast_started) (struct bt_cap_broadcast_source *source)
```

广播音频源已启动，其所有流均已准备好传输音频数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `source` | 已启动的广播音频源。 |

<a id="a85451f4cbf0c8e4d061a2b50b892529d"></a>

### `broadcast_stopped`

```c
void(* bt_cap_initiator_cb::broadcast_stopped) (struct bt_cap_broadcast_source *source, uint8_t reason)
```

广播音频源已停止，其所有流均未准备好传输音频数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `source` | 已停止的广播音频源。 |
| `reason` | 广播音频源停止的原因，参见 `BT_HCI_ERR_*` 值。 |

<a id="a642a2f48e8f870bb1681ba58aa119de9"></a>

### `unicast_discovery_complete`

```c
void(* bt_cap_initiator_cb::unicast_discovery_complete) (struct bt_conn *conn, int err, const struct bt_csip_set_coordinator_set_member *member, const struct bt_csip_set_coordinator_csis_inst *csis_inst)
```

`bt_cap_initiator_unicast_discover()` 的回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 传给 `bt_cap_initiator_unicast_discover()` 的连接指针（Connection pointer）。 |
| `err` | 找到通用音频服务（Common Audio Service）时为 `0`，否则为 `-ENODATA`。 |
| `member` | 指向集合成员（Set member）的指针。`err != 0` 时为 `NULL`。 |
| `csis_inst` | 若找到通用音频服务（Common Audio Service），且其中包含协调集合标识服务（Coordinated Set Identification Service），则为该服务。发生错误或远端设备不包含协调集合标识服务时为 `NULL`；`err != 0` 时为 `NULL`。 |

<a id="a64c9b0fb0bdfcc7434d8f2854a20a666"></a>

### `unicast_start_codec_configured`

```c
void(* bt_cap_initiator_cb::unicast_start_codec_configured) (void)
```

所有流的编解码器配置（Codec configuration）已完成。

传给 `bt_cap_initiator_unicast_audio_start()` 的所有流都已处于 `BT_BAP_EP_STATE_CODEC_CONFIGURED` 或更后面的状态，并采用请求的编解码器配置（Codec configuration）。

只有在至少向一个通用音频规范接受方（CAP acceptor）发送了配置编解码器操作（Config Codec）时才调用。若所有流已具备请求的编解码器配置，则不调用。

由于尚未开始服务质量配置子过程（QoS Configuration subprocedure），可以在此回调中通过 `bt_cap_unicast_group_reconfig()` 重新配置单播组（Unicast group）。但只有组内所有流之前均未连接过时才可这样做，因为一旦建立连接等时流（CIS），就不能重新配置单播组。当前过程仍在进行，因此不能在此回调中启动新的通用音频规范过程（CAP procedure）。

<a id="aa70de1dda73ffdcbb8287f8f174984ea"></a>

### `unicast_start_complete`

```c
void(* bt_cap_initiator_cb::unicast_start_complete) (int err, struct bt_conn *conn)
```

`bt_cap_initiator_unicast_audio_start()` 的回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `err` | 成功时为 `0`。无法执行子过程（Subprocedure）时为 `-ENOEXEC`；因内存不足而无法执行时为 `-ENOMEM`；对等设备拒绝请求时为 `-EACCES`；单播客户端已忙而无法执行时为 `-EBUSY`；参数无效时为 `-EINVAL`；发生非预期状态变化时为 `-EBADMSG`；因非预期状态而无法执行时为 `-EALREADY`；过程中连接断开时为 `-ECONNRESET`；因连接问题而无法执行时为 `-ENOTCONN`；通过 `bt_cap_initiator_unicast_audio_cancel()` 取消时为 `-ECANCELED`。 |
| `conn` | 指向发生错误的连接（Connection）的指针。`err` 为 `0`，或通过 `bt_cap_initiator_unicast_audio_cancel()` 取消时，为 `NULL`。 |

<a id="a8452b3c6775d1608272893719dd3887d"></a>

### `unicast_start_connected`

```c
void(* bt_cap_initiator_cb::unicast_start_connected) (void)
```

所有流的连接等时流（CIS）均已连接。

传给 `bt_cap_initiator_unicast_audio_start()` 的所有流均已建立连接等时流（CIS）。

只有在此过程中至少建立了一个连接等时流（CIS）时才调用。若所有 CIS 此前已建立，则不调用。

<a id="a06b2f73a6f6f8f3f88cd4c5bd87f4fbc"></a>

### `unicast_start_enabled`

```c
void(* bt_cap_initiator_cb::unicast_start_enabled) (void)
```

所有流均已启用（Enabled）。

传给 `bt_cap_initiator_unicast_audio_start()` 的所有流都已处于 `BT_BAP_EP_STATE_ENABLING` 或更后面的状态，并采用请求的元数据（Metadata）。

只有在至少向一个通用音频规范接受方（CAP acceptor）发送了启用操作（Enable）时才调用。若所有流此前已使用请求的元数据启用，则不调用。

<a id="a5ef6349113a1c786a0441b6c494286d1"></a>

### `unicast_start_qos_configured`

```c
void(* bt_cap_initiator_cb::unicast_start_qos_configured) (void)
```

所有流的服务质量配置（QoS configuration）已完成。

传给 `bt_cap_initiator_unicast_audio_start()` 的所有流都已处于 `BT_BAP_EP_STATE_QOS_CONFIGURED` 或更后面的状态，并采用单播组的服务质量配置（QoS configuration）。

只有在至少向一个通用音频规范接受方（CAP acceptor）发送了配置服务质量操作（Config QoS）时才调用。若所有流已具备请求的 QoS 配置，则不调用。

<a id="a65d8dd89661f92b2e71e90b69a8b4320"></a>

### `unicast_start_started`

```c
void(* bt_cap_initiator_cb::unicast_start_started) (void)
```

所有流均已启动（Started）。

传给 `bt_cap_initiator_unicast_audio_start()` 的所有流均已处于 `BT_BAP_EP_STATE_STREAMING` 状态。

只有在至少向一个通用音频规范接受方（CAP acceptor）发送了接收方启动就绪操作（Receiver Start Ready）时才调用。若所有流都由 CAP 接受方启动，则不调用。

<a id="a2e910a82209d144878b6c69c1b2723ba"></a>

### `unicast_stop_complete`

```c
void(* bt_cap_initiator_cb::unicast_stop_complete) (int err, struct bt_conn *conn)
```

`bt_cap_initiator_unicast_audio_stop()` 的回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `err` | 成功时为 `0`。无法执行子过程（Subprocedure）时为 `-ENOEXEC`；因内存不足而无法执行时为 `-ENOMEM`；对等设备拒绝请求时为 `-EACCES`；单播客户端已忙而无法执行时为 `-EBUSY`；参数无效时为 `-EINVAL`；发生非预期状态变化时为 `-EBADMSG`；因非预期状态而无法执行时为 `-EALREADY`；过程中连接断开时为 `-ECONNRESET`；因连接问题而无法执行时为 `-ENOTCONN`；通过 `bt_cap_initiator_unicast_audio_cancel()` 取消时为 `-ECANCELED`。 |
| `conn` | 指向发生错误的连接（Connection）的指针。`err` 为 `0`，或通过 `bt_cap_initiator_unicast_audio_cancel()` 取消时，为 `NULL`。 |

<a id="a8001c24d64df0881dbfd78382c2a2db7"></a>

### `unicast_stop_disabled`

```c
void(* bt_cap_initiator_cb::unicast_stop_disabled) (void)
```

所有流均已禁用（Disabled）。

传给 `bt_cap_initiator_unicast_audio_stop()` 的所有流均已处于 `BT_BAP_EP_STATE_DISABLING` 或 `BT_BAP_EP_STATE_QOS_CONFIGURED` 状态。

只有在至少向一个通用音频规范接受方（CAP acceptor）发送了禁用操作（Disable）时才调用。若没有任何流处于已启用或正在流传输状态，则不调用。

<a id="a8f659ac17a242eab12c404f59e42d149"></a>

### `unicast_stop_released`

```c
void(* bt_cap_initiator_cb::unicast_stop_released) (void)
```

所有流均已释放（Released）。

传给 `bt_cap_initiator_unicast_audio_stop()` 的所有流均已释放（Released）。

只有在至少向一个通用音频规范接受方（CAP acceptor）发送了释放操作（Release）时才调用。若未请求释放这些流，则不调用。

<a id="a8c20d933b9ee1c1412d7ad719ff24683"></a>

### `unicast_stop_stopped`

```c
void(* bt_cap_initiator_cb::unicast_stop_stopped) (void)
```

所有流均已停止（Stopped）。

传给 `bt_cap_initiator_unicast_audio_stop()` 的所有流均已处于 `BT_BAP_EP_STATE_QOS_CONFIGURED` 状态。

只有在至少向一个通用音频规范接受方（CAP acceptor）发送了接收方停止就绪操作（Receiver Stop Ready）时才调用。若没有任何流处于 `BT_BAP_EP_STATE_DISABLING` 状态，则不调用。

<a id="a95266741841fca83cd2769c76652154e"></a>

### `unicast_update_complete`

```c
void(* bt_cap_initiator_cb::unicast_update_complete) (int err, struct bt_conn *conn)
```

`bt_cap_initiator_unicast_audio_update()` 的回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `err` | 成功时为 `0`。无法执行子过程（Subprocedure）时为 `-ENOEXEC`；因内存不足而无法执行时为 `-ENOMEM`；对等设备拒绝请求时为 `-EACCES`；单播客户端已忙而无法执行时为 `-EBUSY`；参数无效时为 `-EINVAL`；发生非预期状态变化时为 `-EBADMSG`；过程中连接断开时为 `-ECONNRESET`；因连接问题而无法执行时为 `-ENOTCONN`；通过 `bt_cap_initiator_unicast_audio_cancel()` 取消时为 `-ECANCELED`。 |
| `conn` | 指向发生错误的连接（Connection）的指针。`err` 为 `0`，或通过 `bt_cap_initiator_unicast_audio_cancel()` 取消时，为 `NULL`。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/cap.h`

## 38.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/cap.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_csip_set_coordinator_set_member](P058_bt_csip_set_coordinator_set_member_结构体.md)
- [bt_csip_set_coordinator_csis_inst](P056_bt_csip_set_coordinator_csis_inst_结构体.md)
- [bt_cap_initiator_unicast_discover()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gab7b273d06abf9a3cb43afdd4e3c30c8d)
- [bt_cap_initiator_unicast_audio_start()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gae19686be7f8aef1cc92c70fea93e1184)
- [bt_cap_initiator_unicast_audio_update()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga92e4e2c12720ec25c4050cde307cd639)
- [bt_cap_initiator_unicast_audio_stop()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gafdf6f1656249ab3ae6296272dc36b66f)
- [bt_cap_broadcast_source](P017_bt_cap_broadcast_source_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [BT_BAP_EP_STATE_CODEC_CONFIGURED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa6585721b9bfbb744b0a27b5d7a6f5688)
- [bt_cap_unicast_group_reconfig()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga6c862b49aa1339225aeb05fad32c2f06)
- [bt_cap_initiator_unicast_audio_cancel()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga9fbddf102e29e8e969eade40fd60da4f)
- [BT_BAP_EP_STATE_ENABLING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa187f373140139caa320d593061e7c332)
- [BT_BAP_EP_STATE_QOS_CONFIGURED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa76cd25c523b1fc0500db9fb40f303523)
- [BT_BAP_EP_STATE_STREAMING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggaf210a91e1ff11d9bf7792ba47d1e1b4aae15bf7ad5a2e44401d15ff62aee85710)
- [BT_BAP_EP_STATE_DISABLING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa7b7a407f002502aced74e408c1278ae8)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P037_bt_cap_initiator_broadcast_subgroup_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P039_bt_cap_stream_结构体.md)
