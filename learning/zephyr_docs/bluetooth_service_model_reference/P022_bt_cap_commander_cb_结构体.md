---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-22
title: bt_cap_commander_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__commander__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_bt\_cap\_commander\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__commander__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通用音频配置文件（Common Audio Profile，CAP）过程的回调结构体。

```c
#include <zephyr/bluetooth/audio/cap.h>
```

<a id="details"></a>

通用音频配置文件（Common Audio Profile，CAP）过程的回调结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 22.1\_数据成员（Data Fields）

<a id="r_af989b3ebe7e5cc83a1ca4b2ef080e14d"></a>

```c
void(* discovery_complete )(struct bt_conn *conn, int err, const struct bt_csip_set_coordinator_set_member *member, const struct bt_csip_set_coordinator_csis_inst *csis_inst)
```

相关声明：[discovery_complete](#af989b3ebe7e5cc83a1ca4b2ef080e14d)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_csip_set_coordinator_set_member](P058_bt_csip_set_coordinator_set_member_结构体.md)、[bt_csip_set_coordinator_csis_inst](P056_bt_csip_set_coordinator_csis_inst_结构体.md)。

`bt_cap_commander_discover()` 的回调（Callback）。

<a id="r_a3a7777603c23c14bc9d01cf29bc70ef7"></a>

```c
void(* volume_changed )(struct bt_conn *conn, int err)
```

相关声明：[volume_changed](#a3a7777603c23c14bc9d01cf29bc70ef7)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

`bt_cap_commander_change_volume()` 的回调（Callback）。

<a id="r_acc9fcedf7f7abe86e055d48e6df124c7"></a>

```c
void(* volume_mute_changed )(struct bt_conn *conn, int err)
```

相关声明：[volume_mute_changed](#acc9fcedf7f7abe86e055d48e6df124c7)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

`bt_cap_commander_change_volume_mute_state()` 的回调（Callback）。

<a id="r_a3bacfffef8d122db4574463777dfd507"></a>

```c
void(* volume_offset_changed )(struct bt_conn *conn, int err)
```

相关声明：[volume_offset_changed](#a3bacfffef8d122db4574463777dfd507)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

`bt_cap_commander_change_volume_offset()` 的回调（Callback）。

<a id="r_aa49e7eaf5c45d70c800f28b81f9967e5"></a>

```c
void(* microphone_mute_changed )(struct bt_conn *conn, int err)
```

相关声明：[microphone_mute_changed](#aa49e7eaf5c45d70c800f28b81f9967e5)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

`bt_cap_commander_change_microphone_mute_state()` 的回调（Callback）。

<a id="r_a1e83872924e1aa1293c499184ade9173"></a>

```c
void(* microphone_gain_changed )(struct bt_conn *conn, int err)
```

相关声明：[microphone_gain_changed](#a1e83872924e1aa1293c499184ade9173)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

`bt_cap_commander_change_microphone_gain_setting()` 的回调（Callback）。

<a id="r_a14f6a51db5a76aac015a5de617712af3"></a>

```c
void(* broadcast_reception_start )(struct bt_conn *conn, int err)
```

相关声明：[broadcast_reception_start](#a14f6a51db5a76aac015a5de617712af3)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

`bt_cap_commander_broadcast_reception_start()` 的回调（Callback）。

<a id="r_a2188c52e3daf0a695d7c42e6cac561cf"></a>

```c
void(* broadcast_reception_stop )(struct bt_conn *conn, int err)
```

相关声明：[broadcast_reception_stop](#a2188c52e3daf0a695d7c42e6cac561cf)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

`bt_cap_commander_broadcast_reception_stop()` 的回调（Callback）。

<a id="r_a7dfa1903f5cd71e67b6da0f5ff2fb299"></a>

```c
void(* distribute_broadcast_code )(struct bt_conn *conn, int err)
```

相关声明：[distribute_broadcast_code](#a7dfa1903f5cd71e67b6da0f5ff2fb299)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

`bt_cap_commander_distribute_broadcast_code()` 的回调（Callback）。

## 22.2\_详细说明（Detailed Documentation）

<a id="a14f6a51db5a76aac015a5de617712af3"></a>

### `broadcast_reception_start`

```c
void(* bt_cap_commander_cb::broadcast_reception_start) (struct bt_conn *conn, int err)
```

`bt_cap_commander_broadcast_reception_start()` 的回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 指向发生错误的连接（Connection）的指针。`err` 为 `0`，或已通过 `bt_cap_commander_cancel()` 取消时，为 `NULL`。 |
| `err` | 成功时为 `0`；属性协议错误（ATT error）时为带有具体 `BT_ATT_ERR_*` 错误码的 `BT_GATT_ERR()`；通过 `bt_cap_commander_cancel()` 取消时为 `-ECANCELED`。 |

<a id="a2188c52e3daf0a695d7c42e6cac561cf"></a>

### `broadcast_reception_stop`

```c
void(* bt_cap_commander_cb::broadcast_reception_stop) (struct bt_conn *conn, int err)
```

`bt_cap_commander_broadcast_reception_stop()` 的回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 指向发生错误的连接（Connection）的指针。`err` 为 `0`，或已通过 `bt_cap_commander_cancel()` 取消时，为 `NULL`。 |
| `err` | 成功时为 `0`；属性协议错误（ATT error）时为带有具体 `BT_ATT_ERR_*` 错误码的 `BT_GATT_ERR()`；通过 `bt_cap_commander_cancel()` 取消时为 `-ECANCELED`。 |

<a id="af989b3ebe7e5cc83a1ca4b2ef080e14d"></a>

### `discovery_complete`

```c
void(* bt_cap_commander_cb::discovery_complete) (struct bt_conn *conn, int err, const struct bt_csip_set_coordinator_set_member *member, const struct bt_csip_set_coordinator_csis_inst *csis_inst)
```

`bt_cap_commander_discover()` 的回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 传给 `bt_cap_commander_discover()` 的连接指针（Connection pointer）。 |
| `err` | 找到通用音频服务（Common Audio Service）时为 `0`，否则为 `-ENODATA`。 |
| `member` | 指向集合成员（Set member）的指针。`err != 0` 时为 `NULL`。 |
| `csis_inst` | 若找到通用音频服务（Common Audio Service），且其中包含协调集合标识服务（Coordinated Set Identification Service），则为该服务。发生错误或远端设备不包含协调集合标识服务时为 `NULL`；`err != 0` 时为 `NULL`。 |

<a id="a7dfa1903f5cd71e67b6da0f5ff2fb299"></a>

### `distribute_broadcast_code`

```c
void(* bt_cap_commander_cb::distribute_broadcast_code) (struct bt_conn *conn, int err)
```

`bt_cap_commander_distribute_broadcast_code()` 的回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 指向发生错误的连接（Connection）的指针。`err` 为 `0`，或已通过 `bt_cap_commander_cancel()` 取消时，为 `NULL`。 |
| `err` | 成功时为 `0`；属性协议错误（ATT error）时为带有具体 `BT_ATT_ERR_*` 错误码的 `BT_GATT_ERR()`；通过 `bt_cap_commander_cancel()` 取消时为 `-ECANCELED`。 |

<a id="a1e83872924e1aa1293c499184ade9173"></a>

### `microphone_gain_changed`

```c
void(* bt_cap_commander_cb::microphone_gain_changed) (struct bt_conn *conn, int err)
```

`bt_cap_commander_change_microphone_gain_setting()` 的回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 指向发生错误的连接（Connection）的指针。`err` 为 `0`，或已通过 `bt_cap_commander_cancel()` 取消时，为 `NULL`。 |
| `err` | 成功时为 `0`；属性协议错误（ATT error）时为带有具体 `BT_ATT_ERR_*` 错误码的 `BT_GATT_ERR()`；通过 `bt_cap_commander_cancel()` 取消时为 `-ECANCELED`。 |

<a id="aa49e7eaf5c45d70c800f28b81f9967e5"></a>

### `microphone_mute_changed`

```c
void(* bt_cap_commander_cb::microphone_mute_changed) (struct bt_conn *conn, int err)
```

`bt_cap_commander_change_microphone_mute_state()` 的回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 指向发生错误的连接（Connection）的指针。`err` 为 `0`，或已通过 `bt_cap_commander_cancel()` 取消时，为 `NULL`。 |
| `err` | 成功时为 `0`；属性协议错误（ATT error）时为带有具体 `BT_ATT_ERR_*` 错误码的 `BT_GATT_ERR()`；通过 `bt_cap_commander_cancel()` 取消时为 `-ECANCELED`。 |

<a id="a3a7777603c23c14bc9d01cf29bc70ef7"></a>

### `volume_changed`

```c
void(* bt_cap_commander_cb::volume_changed) (struct bt_conn *conn, int err)
```

`bt_cap_commander_change_volume()` 的回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 指向发生错误的连接（Connection）的指针。`err` 为 `0`，或已通过 `bt_cap_commander_cancel()` 取消时，为 `NULL`。 |
| `err` | 成功时为 `0`；属性协议错误（ATT error）时为带有具体 `BT_ATT_ERR_*` 错误码的 `BT_GATT_ERR()`；通过 `bt_cap_commander_cancel()` 取消时为 `-ECANCELED`。 |

<a id="acc9fcedf7f7abe86e055d48e6df124c7"></a>

### `volume_mute_changed`

```c
void(* bt_cap_commander_cb::volume_mute_changed) (struct bt_conn *conn, int err)
```

`bt_cap_commander_change_volume_mute_state()` 的回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 指向发生错误的连接（Connection）的指针。`err` 为 `0`，或已通过 `bt_cap_commander_cancel()` 取消时，为 `NULL`。 |
| `err` | 成功时为 `0`；属性协议错误（ATT error）时为带有具体 `BT_ATT_ERR_*` 错误码的 `BT_GATT_ERR()`；通过 `bt_cap_commander_cancel()` 取消时为 `-ECANCELED`。 |

<a id="a3bacfffef8d122db4574463777dfd507"></a>

### `volume_offset_changed`

```c
void(* bt_cap_commander_cb::volume_offset_changed) (struct bt_conn *conn, int err)
```

`bt_cap_commander_change_volume_offset()` 的回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 指向发生错误的连接（Connection）的指针。`err` 为 `0`，或已通过 `bt_cap_commander_cancel()` 取消时，为 `NULL`。 |
| `err` | 成功时为 `0`；属性协议错误（ATT error）时为带有具体 `BT_ATT_ERR_*` 错误码的 `BT_GATT_ERR()`；通过 `bt_cap_commander_cancel()` 取消时为 `-ECANCELED`。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/cap.h`

## 22.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/cap.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_csip_set_coordinator_set_member](P058_bt_csip_set_coordinator_set_member_结构体.md)
- [bt_csip_set_coordinator_csis_inst](P056_bt_csip_set_coordinator_csis_inst_结构体.md)
- [bt_cap_commander_discover()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga165c67bddcbe220050293a4c73fb6ede)
- [bt_cap_commander_change_volume()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gaff96953334eab1a38b30720b41c0d1a6)
- [bt_cap_commander_change_volume_mute_state()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac5f94baa82fa6deade6f83346a56b5e4)
- [bt_cap_commander_change_volume_offset()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gae2cd451b387659b0a2021a9023d74dfa)
- [bt_cap_commander_change_microphone_mute_state()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga19cc7ed5992a528a7795b76e7add6d54)
- [bt_cap_commander_change_microphone_gain_setting()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga958cd5925699624d23479ad2ace6b55b)
- [bt_cap_commander_broadcast_reception_start()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga25be83bb53c8e2ab76f311eaf4f615b9)
- [bt_cap_commander_broadcast_reception_stop()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac5b2b6d617a092fb98b23c41b2f52d15)
- [bt_cap_commander_distribute_broadcast_code()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gaf86582ad529b6ee801d1154db7e33827)
- [bt_cap_commander_cancel()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga7abf029533fed391930257605f3c752c)
- [BT_GATT_ERR()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gaff31756c1bf8ee755e65b1e0fb689bb7)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P021_bt_cap_commander_broadcast_reception_stop_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P023_bt_cap_commander_change_microphone_gain_setting_member_param_结构体.md)
