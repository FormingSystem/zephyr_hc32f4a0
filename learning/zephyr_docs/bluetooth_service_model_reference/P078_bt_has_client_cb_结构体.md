---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-78
title: bt_has_client_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__has__client__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第78章\_bt\_has\_client\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__has__client__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

助听接入服务客户端（Hearing Access Service Client）的回调结构。

```c
#include <zephyr/bluetooth/audio/has.h>
```

<a id="details"></a>

助听接入服务客户端（Hearing Access Service Client）的回调结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 78.1\_数据成员（Data Fields）

<a id="r_acf35d62cce0c2181e2eefd8c43e3b568"></a>

```c
void(* discover )(struct bt_conn *conn, int err, struct bt_has *has, enum bt_has_hearing_aid_type type, enum bt_has_capabilities caps)
```

相关声明：[discover](#acf35d62cce0c2181e2eefd8c43e3b568)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_has](P077_bt_has_结构体.md)、[bt_has_hearing_aid_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gaa9572a32f912c8fe529b510aa23f4540)、[bt_has_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga50d470390967317cb84b17fd450546a4)。

`bt_has_discover` 的回调函数（Callback function）。

<a id="r_a4217754818ad047f287aceda8326bf99"></a>

```c
void(* preset_switch )(struct bt_has *has, int err, uint8_t index)
```

相关声明：[preset_switch](#a4217754818ad047f287aceda8326bf99)、[bt_has](P077_bt_has_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

听觉接入服务活动预设变化回调（Hearing Access Service active preset changes）。

<a id="r_a50759c76add5f4f76e23e742ae3ebe1b"></a>

```c
void(* preset_read_rsp )(struct bt_has *has, int err, const struct bt_has_preset_record *record, bool is_last)
```

相关声明：[preset_read_rsp](#a50759c76add5f4f76e23e742ae3ebe1b)、[bt_has](P077_bt_has_结构体.md)、[bt_has_preset_record](P081_bt_has_preset_record_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

预设读取操作回调（Presets read operation callback）。

<a id="r_aa54cf5f268e542947ffb30531b7702ba"></a>

```c
void(* preset_update )(struct bt_has *has, uint8_t index_prev, const struct bt_has_preset_record *record, bool is_last)
```

相关声明：[preset_update](#aa54cf5f268e542947ffb30531b7702ba)、[bt_has](P077_bt_has_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_has_preset_record](P081_bt_has_preset_record_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

预设更新通知回调（Preset update notification callback）。

<a id="r_a1c28e7b5542100ce93727ac097cc6dee"></a>

```c
void(* preset_deleted )(struct bt_has *has, uint8_t index, bool is_last)
```

相关声明：[preset_deleted](#a1c28e7b5542100ce93727ac097cc6dee)、[bt_has](P077_bt_has_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

预设删除通知回调（Preset deletion notification callback）。

<a id="r_a903397650915f3335dd2b8cd4f51d293"></a>

```c
void(* preset_availability )(struct bt_has *has, uint8_t index, bool available, bool is_last)
```

相关声明：[preset_availability](#a903397650915f3335dd2b8cd4f51d293)、[bt_has](P077_bt_has_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

预设可用性通知回调（Preset availability notification callback）。

## 78.2\_详细说明（Detailed Documentation）

<a id="acf35d62cce0c2181e2eefd8c43e3b568"></a>

### `discover`

```c
void(* bt_has_client_cb::discover) (struct bt_conn *conn, int err, struct bt_has *has, enum bt_has_hearing_aid_type type, enum bt_has_capabilities caps)
```

`bt_has_discover` 的回调函数（Callback function）。

发现过程（Discovery procedure）完成时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 蓝牙连接对象（Bluetooth connection object）。 |
| `err` | 成功时为 `0`，否则为属性协议错误（ATT error）或负的错误编号（errno）。 |
| `has` | 指向听觉接入服务对象（Hearing Access Service object）的指针；发生错误时为 `NULL`。 |
| `type` | 助听器类型（Hearing Aid type）。 |
| `caps` | 助听器能力（Hearing Aid capabilities）。 |

<a id="a903397650915f3335dd2b8cd4f51d293"></a>

### `preset_availability`

```c
void(* bt_has_client_cb::preset_availability) (struct bt_has *has, uint8_t index, bool available, bool is_last)
```

预设可用性通知回调（Preset availability notification callback）。

远端服务器通知预设可用性变化（Preset availability change）时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `has` | 指向听觉接入服务对象（Hearing Access Service object）的指针。 |
| `index` | 预设索引（Preset index）。 |
| `available` | 可用（Available）时为 `true`，否则为 `false`。 |
| `is_last` | 可以认为预设列表更新操作（Preset list update operation）已结束时为 `true`。 |

<a id="a1c28e7b5542100ce93727ac097cc6dee"></a>

### `preset_deleted`

```c
void(* bt_has_client_cb::preset_deleted) (struct bt_has *has, uint8_t index, bool is_last)
```

预设删除通知回调（Preset deletion notification callback）。

预设（Preset）被远端服务器删除时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `has` | 指向听觉接入服务对象（Hearing Access Service object）的指针。 |
| `index` | 预设索引（Preset index）。 |
| `is_last` | 可以认为预设列表更新操作（Preset list update operation）已结束时为 `true`。 |

<a id="a50759c76add5f4f76e23e742ae3ebe1b"></a>

### `preset_read_rsp`

```c
void(* bt_has_client_cb::preset_read_rsp) (struct bt_has *has, int err, const struct bt_has_preset_record *record, bool is_last)
```

预设读取操作回调（Presets read operation callback）。

远端服务器发送预设读取响应（Preset read response）时调用此回调。记录对象（Record object）及其成员都是临时的；要缓存信息，必须复制它们。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `has` | 指向听觉接入服务对象（Hearing Access Service object）的指针。 |
| `err` | 成功时为 `0`，否则为属性协议错误（ATT error）或负的错误编号（errno）。 |
| `record` | 预设记录（Preset record），发生错误时为 `NULL`。 |
| `is_last` | 可以认为读取预设操作（Read Presets）已结束时为 `true`。 |

<a id="a4217754818ad047f287aceda8326bf99"></a>

### `preset_switch`

```c
void(* bt_has_client_cb::preset_switch) (struct bt_has *has, int err, uint8_t index)
```

听觉接入服务活动预设变化回调（Hearing Access Service active preset changes）。

可选回调：远端服务器完成预设切换过程（Preset switch procedure）并改变活动预设（Active preset）时调用。要接收活动预设变化并支持切换预设，必须设置此回调。若未设置，`bt_has_client_discover` 将不发现活动索引特征（Active Index characteristic）和控制点特征（Control Point characteristic）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `has` | 指向听觉接入服务对象（Hearing Access Service object）的指针。 |
| `err` | 成功时为 `0`，否则为属性协议错误（ATT error）或负的错误编号（errno）。 |
| `index` | 活动预设索引（Active preset index）。 |

<a id="aa54cf5f268e542947ffb30531b7702ba"></a>

### `preset_update`

```c
void(* bt_has_client_cb::preset_update) (struct bt_has *has, uint8_t index_prev, const struct bt_has_preset_record *record, bool is_last)
```

预设更新通知回调（Preset update notification callback）。

远端服务器通知预设记录更新（Preset record update）时调用此回调。记录对象（Record object）及其对象都是临时的；要缓存信息，必须复制它们。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `has` | 指向听觉接入服务对象（Hearing Access Service object）的指针。 |
| `index_prev` | 列表中前一个预设的索引（Previous preset index）。 |
| `record` | 预设记录（Preset record）。 |
| `is_last` | 可以认为预设列表更新操作（Preset list update operation）已结束时为 `true`。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/has.h`

## 78.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/has.h](https://docs.zephyrproject.org/latest/doxygen/html/has_8h_source.html)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_has](P077_bt_has_结构体.md)
- [bt_has_hearing_aid_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gaa9572a32f912c8fe529b510aa23f4540)
- [bt_has_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga50d470390967317cb84b17fd450546a4)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_has_preset_record](P081_bt_has_preset_record_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_has_client_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gaf3765300072b0a6d1ee45699e710d4da)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P077_bt_has_结构体.md) · [返回大纲](大纲.md) · [下一章](P079_bt_has_features_param_结构体.md)
