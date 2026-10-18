---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-15
title: bt_bap_broadcast_assistant_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__broadcast__assistant__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_bt\_bap\_broadcast\_assistant\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__broadcast__assistant__cb.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

保存基本音频配置文件（Basic Audio Profile，BAP）广播助手（Broadcast Assistant）回调的结构体。

```c
#include <zephyr/bluetooth/audio/bap.h>
```

<a id="details"></a>

保存基本音频配置文件（BAP）广播助手（Broadcast Assistant）回调的结构体。可使用 `bt_bap_broadcast_assistant_register_cb()` 注册这些回调。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 15.1\_数据成员（Data Fields）

<a id="r_a01ad0a89db9041670f6a68d6f1680988"></a>

```c
void(* discover )(struct bt_conn *conn, int err, uint8_t recv_state_count)
```

相关声明：[discover](#a01ad0a89db9041670f6a68d6f1680988)、[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

`bt_bap_broadcast_assistant_discover` 的回调函数。

<a id="r_ab88d98b1e742ccd36aac69069ebf3f61"></a>

```c
void(* scan )(const struct bt_le_scan_recv_info *info, uint32_t broadcast_id)
```

相关声明：[scan](#ab88d98b1e742ccd36aac69069ebf3f61)、[bt_le_scan_recv_info](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__scan__recv__info.html)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

广播音频扫描服务（BASS）客户端扫描结果的回调函数。

<a id="r_a629ff4299b8ae5bcbddf28338caddfd0"></a>

```c
void(* recv_state )(struct bt_conn *conn, int err, const struct bt_bap_scan_delegator_recv_state *state)
```

相关声明：[recv_state](#a629ff4299b8ae5bcbddf28338caddfd0)、[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)、[bt_bap_scan_delegator_recv_state](P032_bt_bap_scan_delegator_recv_state_结构体.md)、[state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)。

读取或更新接收状态（Receive State）时的回调函数。

<a id="r_af3fb53d95cdc7ba202657e4c54e0b2b8"></a>

```c
void(* recv_state_removed )(struct bt_conn *conn, uint8_t src_id)
```

相关声明：[recv_state_removed](#af3fb53d95cdc7ba202657e4c54e0b2b8)、[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

移除接收状态时的回调函数。

<a id="r_ad2bdfcc0147a751910d82232a77e34f8"></a>

```c
void(* scan_start )(struct bt_conn *conn, int err)
```

相关声明：[scan_start](#ad2bdfcc0147a751910d82232a77e34f8)、[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)。

`bt_bap_broadcast_assistant_scan_start()` 的回调函数。

<a id="r_a80296a38e664aabff7ec27e007c59e95"></a>

```c
void(* scan_stop )(struct bt_conn *conn, int err)
```

相关声明：[scan_stop](#a80296a38e664aabff7ec27e007c59e95)、[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)。

`bt_bap_broadcast_assistant_scan_stop()` 的回调函数。

<a id="r_ad909b9e6e3c35be10a29ee5a4b7213fb"></a>

```c
void(* add_src )(struct bt_conn *conn, int err)
```

相关声明：[add_src](#ad909b9e6e3c35be10a29ee5a4b7213fb)、[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)。

`bt_bap_broadcast_assistant_add_src()` 的回调函数。

<a id="r_ab24e3ecb9764ca833524b787126b8c2c"></a>

```c
void(* mod_src )(struct bt_conn *conn, int err)
```

相关声明：[mod_src](#ab24e3ecb9764ca833524b787126b8c2c)、[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)。

`bt_bap_broadcast_assistant_mod_src()` 的回调函数。

<a id="r_a09de9cb86dad76b485ff52257a0c68dc"></a>

```c
void(* broadcast_code )(struct bt_conn *conn, int err)
```

相关声明：[broadcast_code](#a09de9cb86dad76b485ff52257a0c68dc)、[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)。

`bt_bap_broadcast_assistant_set_broadcast_code()` 的回调函数。

<a id="r_af0cf259088cd793152390b21813a9481"></a>

```c
void(* rem_src )(struct bt_conn *conn, int err)
```

相关声明：[rem_src](#af0cf259088cd793152390b21813a9481)、[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)。

`bt_bap_broadcast_assistant_rem_src()` 的回调函数。

## 15.2\_详细说明（Detailed Documentation）

<a id="ad909b9e6e3c35be10a29ee5a4b7213fb"></a>

### `add_src`

```c
void(* bt_bap_broadcast_assistant_cb::add_src) (struct bt_conn *conn, int err)
```

`bt_bap_broadcast_assistant_add_src()` 的回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接。 |
| `err` | 错误值。成功时为 0，失败时为 GATT 错误。 |

<a id="a09de9cb86dad76b485ff52257a0c68dc"></a>

### `broadcast_code`

```c
void(* bt_bap_broadcast_assistant_cb::broadcast_code) (struct bt_conn *conn, int err)
```

`bt_bap_broadcast_assistant_set_broadcast_code()` 的回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接。 |
| `err` | 错误值。成功时为 0，失败时为 GATT 错误。 |

<a id="a01ad0a89db9041670f6a68d6f1680988"></a>

### `discover`

```c
void(* bt_bap_broadcast_assistant_cb::discover) (struct bt_conn *conn, int err, uint8_t recv_state_count)
```

`bt_bap_broadcast_assistant_discover` 的回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于发现广播音频扫描服务（BASS）的连接。 |
| `err` | 错误值。成功时为 0，失败时为 GATT 错误或 `ERRNO`。 |
| `recv_state_count` | 服务器上的接收状态数量。 |

<a id="ab24e3ecb9764ca833524b787126b8c2c"></a>

### `mod_src`

```c
void(* bt_bap_broadcast_assistant_cb::mod_src) (struct bt_conn *conn, int err)
```

`bt_bap_broadcast_assistant_mod_src()` 的回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接。 |
| `err` | 错误值。成功时为 0，失败时为 GATT 错误。 |

<a id="a629ff4299b8ae5bcbddf28338caddfd0"></a>

### `recv_state`

```c
void(* bt_bap_broadcast_assistant_cb::recv_state) (struct bt_conn *conn, int err, const struct bt_bap_scan_delegator_recv_state *state)
```

读取或更新接收状态（Receive State）时的回调函数。

每当读取或更新接收状态时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与广播音频扫描服务（BASS）服务器的连接。 |
| `err` | 错误值。成功时为 0，失败时为 GATT 错误。 |
| `state` | 接收状态；若接收状态为空，则为 `NULL`。 |

<a id="af3fb53d95cdc7ba202657e4c54e0b2b8"></a>

### `recv_state_removed`

```c
void(* bt_bap_broadcast_assistant_cb::recv_state_removed) (struct bt_conn *conn, uint8_t src_id)
```

移除接收状态时的回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与广播音频扫描服务（BASS）服务器的连接。 |
| `src_id` | 接收状态（Receive State）。 |

<a id="af0cf259088cd793152390b21813a9481"></a>

### `rem_src`

```c
void(* bt_bap_broadcast_assistant_cb::rem_src) (struct bt_conn *conn, int err)
```

`bt_bap_broadcast_assistant_rem_src()` 的回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接。 |
| `err` | 错误值。成功时为 0，失败时为 GATT 错误。 |

<a id="ab88d98b1e742ccd36aac69069ebf3f61"></a>

### `scan`

```c
void(* bt_bap_broadcast_assistant_cb::scan) (const struct bt_le_scan_recv_info *info, uint32_t broadcast_id)
```

广播音频扫描服务（BASS）客户端扫描结果的回调函数。

扫描器发现广播 `BT_UUID_BROADCAST_AUDIO` UUID 的广播者时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `info` | 广播者信息（Advertiser Information）。 |
| `broadcast_id` | 24 位广播 ID。 |

<a id="ad2bdfcc0147a751910d82232a77e34f8"></a>

### `scan_start`

```c
void(* bt_bap_broadcast_assistant_cb::scan_start) (struct bt_conn *conn, int err)
```

`bt_bap_broadcast_assistant_scan_start()` 的回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接。 |
| `err` | 错误值。成功时为 0，失败时为 GATT 错误。 |

<a id="a80296a38e664aabff7ec27e007c59e95"></a>

### `scan_stop`

```c
void(* bt_bap_broadcast_assistant_cb::scan_stop) (struct bt_conn *conn, int err)
```

`bt_bap_broadcast_assistant_scan_stop()` 的回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接。 |
| `err` | 错误值。成功时为 0，失败时为 GATT 错误。 |

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/bap.h`

## 15.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h_source.html)
- [bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_le_scan_recv_info](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__scan__recv__info.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_bap_scan_delegator_recv_state](P032_bt_bap_scan_delegator_recv_state_结构体.md)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [bt_bap_broadcast_assistant_scan_start()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga98ac067e66d263aa41fc6f8df6bb9126)
- [bt_bap_broadcast_assistant_scan_stop()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga76cae35df980b78a10551811050b2760)
- [bt_bap_broadcast_assistant_add_src()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gac93cb4cab33d0b937e752bc0b71cad9e)
- [bt_bap_broadcast_assistant_mod_src()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaa9c292a7dcb470926d8d7d4be699a0c7)
- [bt_bap_broadcast_assistant_set_broadcast_code()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gabcec07689c13a996bcb9d2d417347dbb)
- [bt_bap_broadcast_assistant_rem_src()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga09785690db551677a043fcaa2fdb7f29)
- [bt_bap_broadcast_assistant_register_cb()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gabab24c44e9833029965475ad7b149e6e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P014_bt_bap_broadcast_assistant_add_src_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P016_bt_bap_broadcast_assistant_mod_src_param_结构体.md)
