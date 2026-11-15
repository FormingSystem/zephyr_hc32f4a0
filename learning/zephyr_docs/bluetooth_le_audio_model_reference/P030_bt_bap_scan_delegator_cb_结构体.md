---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-30
title: bt_bap_scan_delegator_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__scan__delegator__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_bt\_bap\_scan\_delegator\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__scan__delegator__cb.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

保存基本音频配置文件（BAP）扫描委托端（Scan Delegator）回调的结构体。

```c
#include <zephyr/bluetooth/audio/bap.h>
```

<a id="details"></a>

保存基本音频配置文件（BAP）扫描委托端（Scan Delegator）回调的结构体。可使用 `bt_bap_scan_delegator_register()` 注册这些回调。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 30.1\_数据成员（Data Fields）

<a id="r_a5d95631d95ae1085071c9b795eca1a8e"></a>

```c
void(* recv_state_updated )(struct bt_conn *conn, const struct bt_bap_scan_delegator_recv_state *recv_state)
```

相关声明：[recv_state_updated](#a5d95631d95ae1085071c9b795eca1a8e)、[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)、[bt_bap_scan_delegator_recv_state](P032_bt_bap_scan_delegator_recv_state_结构体.md)。

接收状态已更新。

<a id="r_a0ea55963f92361f35e68eadcf10306b1"></a>

```c
int(* pa_sync_req )(struct bt_conn *conn, const struct bt_bap_scan_delegator_recv_state *recv_state, bool past_avail, uint16_t pa_interval)
```

相关声明：[pa_sync_req](#a0ea55963f92361f35e68eadcf10306b1)、[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)、[bt_bap_scan_delegator_recv_state](P032_bt_bap_scan_delegator_recv_state_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

周期性广播同步请求（Periodic Advertising Sync Request）。

<a id="r_a5b918538cfe0edaa69155f891981eeae"></a>

```c
int(* pa_sync_term_req )(struct bt_conn *conn, const struct bt_bap_scan_delegator_recv_state *recv_state)
```

相关声明：[pa_sync_term_req](#a5b918538cfe0edaa69155f891981eeae)、[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)、[bt_bap_scan_delegator_recv_state](P032_bt_bap_scan_delegator_recv_state_结构体.md)。

周期性广播同步终止请求。

<a id="r_a78d011c817e60725a0ef14c68bd655cd"></a>

```c
void(* broadcast_code )(struct bt_conn *conn, const struct bt_bap_scan_delegator_recv_state *recv_state, const uint8_t broadcast_code[BT_ISO_BROADCAST_CODE_SIZE])
```

相关声明：[broadcast_code](#a78d011c817e60725a0ef14c68bd655cd)、[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)、[bt_bap_scan_delegator_recv_state](P032_bt_bap_scan_delegator_recv_state_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[BT_ISO_BROADCAST_CODE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga5551cab9896764eec39b8e6102e561e5)。

已收到广播码（Broadcast Code）。

<a id="r_a92351aea994520cd08f87d3d579d6e3b"></a>

```c
int(* bis_sync_req )(struct bt_conn *conn, const struct bt_bap_scan_delegator_recv_state *recv_state, const uint32_t bis_sync_req[0])
```

相关声明：[bis_sync_req](#a92351aea994520cd08f87d3d579d6e3b)、[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)、[bt_bap_scan_delegator_recv_state](P032_bt_bap_scan_delegator_recv_state_结构体.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

广播等时流（BIS）同步请求。

<a id="r_ae41d499d75123a1b70b778e8e95edcc3"></a>

```c
void(* scanning_state )(struct bt_conn *conn, bool is_scanning)
```

相关声明：[scanning_state](#ae41d499d75123a1b70b778e8e95edcc3)、[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

广播助手（Broadcast Assistant）扫描状态回调。

<a id="r_a1ca1642de4bcf3f6552d09761168b1fc"></a>

```c
int(* add_source )(struct bt_conn *conn, const struct bt_bap_scan_delegator_recv_state *recv_state)
```

相关声明：[add_source](#a1ca1642de4bcf3f6552d09761168b1fc)、[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)、[bt_bap_scan_delegator_recv_state](P032_bt_bap_scan_delegator_recv_state_结构体.md)。

添加音频源（Add Source）操作回调。

<a id="r_af862ad2d51d60e57cc50e20c256fde35"></a>

```c
int(* modify_source )(struct bt_conn *conn, const struct bt_bap_scan_delegator_recv_state *recv_state)
```

相关声明：[modify_source](#af862ad2d51d60e57cc50e20c256fde35)、[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)、[bt_bap_scan_delegator_recv_state](P032_bt_bap_scan_delegator_recv_state_结构体.md)。

修改音频源（Modify Source）操作回调。

<a id="r_a8da03993be622b5d25e8bd462dfd16c5"></a>

```c
int(* remove_source )(struct bt_conn *conn, uint8_t src_id)
```

相关声明：[remove_source](#a8da03993be622b5d25e8bd462dfd16c5)、[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

移除音频源（Remove Source）操作回调。

## 30.2\_详细说明（Detailed Documentation）

<a id="a1ca1642de4bcf3f6552d09761168b1fc"></a>

### `add_source`

```c
int(* bt_bap_scan_delegator_cb::add_source) (struct bt_conn *conn, const struct bt_bap_scan_delegator_recv_state *recv_state)
```

添加音频源（Add Source）操作回调。

收到添加音频源的请求时，这些回调会通知应用。应用可返回 0 接受请求，或返回其他值拒绝请求。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 指向发起请求的连接的指针；如果由本地触发，则为 `NULL`。 |
| `recv_state` | 指向请求添加的接收状态的指针。 |

返回（Returns）：接受时返回 0，返回其他值表示拒绝。

<a id="a92351aea994520cd08f87d3d579d6e3b"></a>

### `bis_sync_req`

```c
int(* bt_bap_scan_delegator_cb::bis_sync_req) (struct bt_conn *conn, const struct bt_bap_scan_delegator_recv_state *recv_state, const uint32_t bis_sync_req[0])
```

广播等时流（BIS）同步请求。

广播助手设备请求修改广播等时流（BIS）状态。应在合理时间内按照 `bis_sync_req` 满足该请求。广播助手也可能请求同步较少的索引，或不再同步任何索引。当任意 `bis_sync_req` 值为 `BT_BAP_BIS_SYNC_NO_PREF` 时，总会调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] conn` | 指向请求同步的广播助手连接的指针。 |
| `[in] recv_state` | 指向被请求进行同步的接收状态的指针。 |
| `[in] bis_sync_req` | 位域数组，表示广播助手请求每个子组同步的 BIS 索引。值为 0 表示请求终止 BIG 同步。 |

返回（Returns）：接受时返回 0，返回其他值表示拒绝。

<a id="a78d011c817e60725a0ef14c68bd655cd"></a>

### `broadcast_code`

```c
void(* bt_bap_scan_delegator_cb::broadcast_code) (struct bt_conn *conn, const struct bt_bap_scan_delegator_recv_state *recv_state, const uint8_t broadcast_code[BT_ISO_BROADCAST_CODE_SIZE])
```

已收到广播码（Broadcast Code）。

从广播助手收到的广播码。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 指向提供广播码的连接的指针。 |
| `recv_state` | 指向正在为其提供广播码的接收状态的指针。 |
| `broadcast_code` | 16 个八位字节的广播码。 |

<a id="af862ad2d51d60e57cc50e20c256fde35"></a>

### `modify_source`

```c
int(* bt_bap_scan_delegator_cb::modify_source) (struct bt_conn *conn, const struct bt_bap_scan_delegator_recv_state *recv_state)
```

修改音频源（Modify Source）操作回调。

收到修改音频源的请求时，这些回调会通知应用。应用可返回 0 接受请求，或返回其他值拒绝请求。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 指向发起请求的连接的指针；如果由本地触发，则为 `NULL`。 |
| `recv_state` | 指向请求修改的接收状态的指针。 |

返回（Returns）：接受时返回 0，返回其他值表示拒绝。

<a id="a0ea55963f92361f35e68eadcf10306b1"></a>

### `pa_sync_req`

```c
int(* bt_bap_scan_delegator_cb::pa_sync_req) (struct bt_conn *conn, const struct bt_bap_scan_delegator_recv_state *recv_state, bool past_avail, uint16_t pa_interval)
```

周期性广播同步请求（Periodic Advertising Sync Request）。

对端设备请求与 `recv_state` 指定的周期性广播者同步。关于将待完成同步通知广播助手：【译注：官方原文在“pending sync”处结束，未给出该句的后续操作说明。】

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 指向请求周期性广播同步的连接的指针。 |
| `recv_state` | 指向被请求进行周期性广播同步的接收状态的指针。 |
| `past_avail` | 周期性广播同步转移（Periodic Advertising Sync Transfer，PAST）可用时为 `true`。 |
| `pa_interval` | 周期性广播间隔。 |

返回（Returns）：接受时返回 0，返回其他值表示拒绝。

<a id="a5b918538cfe0edaa69155f891981eeae"></a>

### `pa_sync_term_req`

```c
int(* bt_bap_scan_delegator_cb::pa_sync_term_req) (struct bt_conn *conn, const struct bt_bap_scan_delegator_recv_state *recv_state)
```

周期性广播同步终止请求。

对端设备请求终止 `recv_state` 指定的周期性广播者同步。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 指向请求终止周期性广播同步的连接的指针。 |
| `recv_state` | 指向被请求进行周期性广播同步的接收状态的指针。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="a5d95631d95ae1085071c9b795eca1a8e"></a>

### `recv_state_updated`

```c
void(* bt_bap_scan_delegator_cb::recv_state_updated) (struct bt_conn *conn, const struct bt_bap_scan_delegator_recv_state *recv_state)
```

接收状态已更新。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 如果变化由远端设备引起，则为指向该远端设备连接的指针；否则为 `NULL`。 |
| `recv_state` | 指向已更新接收状态的指针。 |

<a id="a8da03993be622b5d25e8bd462dfd16c5"></a>

### `remove_source`

```c
int(* bt_bap_scan_delegator_cb::remove_source) (struct bt_conn *conn, uint8_t src_id)
```

移除音频源（Remove Source）操作回调。

收到移除音频源的请求时，这些回调会通知应用。应用可返回 0 接受请求，或返回其他值拒绝请求。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 指向发起请求的连接的指针；如果由本地触发，则为 `NULL`。 |
| `src_id` | 请求移除的音频源 ID。 |

返回（Returns）：接受时返回 0，返回其他值表示拒绝。

<a id="ae41d499d75123a1b70b778e8e95edcc3"></a>

### `scanning_state`

```c
void(* bt_bap_scan_delegator_cb::scanning_state) (struct bt_conn *conn, bool is_scanning)
```

广播助手（Broadcast Assistant）扫描状态回调。

广播助手将其扫描状态通知扫描委托端（Scan Delegator）时触发的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 指向发起扫描的连接的指针。 |
| `is_scanning` | 扫描已开始时为 `true`，扫描已停止时为 `false`。 |

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/bap.h`

## 30.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h_source.html)
- [bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)
- [bt_bap_scan_delegator_recv_state](P032_bt_bap_scan_delegator_recv_state_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [BT_ISO_BROADCAST_CODE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga5551cab9896764eec39b8e6102e561e5)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_bap_scan_delegator_register()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga7632ab444dbf99387871f7d0c90b11ba)
- [BT_BAP_BIS_SYNC_NO_PREF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga799f1417272e9b545c1e30ed4616b988)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P029_bt_bap_scan_delegator_add_src_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P031_bt_bap_scan_delegator_mod_src_param_结构体.md)
