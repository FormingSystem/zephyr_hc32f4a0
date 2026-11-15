---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-71
title: bt_avrcp_tg_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__tg__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第71章\_bt\_avrcp\_tg\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__tg__cb.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 71.1\_数据成员（Data Fields）

<a id="r_a8f0994f1b59d16ef74a7430221f53db0"></a>

```c
void(* connected )(struct bt_conn *conn, struct bt_avrcp_tg *tg)
```

相关声明：[connected](#a8f0994f1b59d16ef74a7430221f53db0)、[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)、[bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)。

AVRCP 目标端（TG）连接已建立。

<a id="r_a9c64cc44157e6cedec9decc00f0022b3"></a>

```c
void(* disconnected )(struct bt_avrcp_tg *tg)
```

相关声明：[disconnected](#a9c64cc44157e6cedec9decc00f0022b3)、[bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)。

AVRCP 目标端（TG）连接已断开。

<a id="r_a933eb30910fef1e916e60ff21d4255ec"></a>

```c
void(* unit_info_req )(struct bt_avrcp_tg *tg, uint8_t tid)
```

相关声明：[unit_info_req](#a933eb30910fef1e916e60ff21d4255ec)、[bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

单元信息（Unit Info）请求回调。

<a id="r_a45954c3a1f3e8dffb1bc111845c875ce"></a>

```c
void(* register_notification )(struct bt_avrcp_tg *tg, uint8_t tid, uint8_t event_id, uint32_t interval)
```

相关声明：[register_notification](#a45954c3a1f3e8dffb1bc111845c875ce)、[bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

注册通知（Register Notification）请求回调。

<a id="r_ab9f1a086a71522986808f3ebc2cbd2de"></a>

```c
void(* subunit_info_req )(struct bt_avrcp_tg *tg, uint8_t tid)
```

相关声明：[subunit_info_req](#ab9f1a086a71522986808f3ebc2cbd2de)、[bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

子单元信息（Subunit Info）请求回调。

<a id="r_ab3fe452afec12ff31975763c5269c94f"></a>

```c
void(* get_caps )(struct bt_avrcp_tg *tg, uint8_t tid, uint8_t cap_id)
```

相关声明：[get_caps](#ab3fe452afec12ff31975763c5269c94f)、[bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取能力（Get Capabilities）请求回调。

<a id="r_a82c5ca1100844e5119224aa6bac19bd2"></a>

```c
void(* browsing_connected )(struct bt_conn *conn, struct bt_avrcp_tg *tg)
```

相关声明：[browsing_connected](#a82c5ca1100844e5119224aa6bac19bd2)、[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)、[bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)。

AVRCP 目标端（TG）浏览连接已建立。

<a id="r_ad66a2945e2cb464bf7324a0685106d47"></a>

```c
void(* browsing_disconnected )(struct bt_avrcp_tg *tg)
```

相关声明：[browsing_disconnected](#ad66a2945e2cb464bf7324a0685106d47)、[bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)。

AVRCP 目标端（TG）浏览连接已断开。

<a id="r_a4179686bbe4030c44f0a277532dcb96b"></a>

```c
void(* set_browsed_player )(struct bt_avrcp_tg *tg, uint8_t tid, uint16_t player_id)
```

相关声明：[set_browsed_player](#a4179686bbe4030c44f0a277532dcb96b)、[bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

设置浏览播放器（Set Browsed Player）请求回调。

<a id="r_a0f117772eb0f55e20214b0be8d93a6fa"></a>

```c
void(* get_folder_items )(struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

相关声明：[get_folder_items](#a0f117772eb0f55e20214b0be8d93a6fa)、[bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

获取文件夹条目（Get Folder Items）请求回调。

<a id="r_a37d8a221b66cf3bad74790532b559cff"></a>

```c
void(* change_path )(struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

相关声明：[change_path](#a37d8a221b66cf3bad74790532b559cff)、[bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

更改路径（Change Path）请求回调。

<a id="r_a878eaaf2358b0773e964dc68c910a377"></a>

```c
void(* get_item_attrs )(struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

相关声明：[get_item_attrs](#a878eaaf2358b0773e964dc68c910a377)、[bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

获取条目属性（Get Item Attributes）请求回调。

<a id="r_ae5a45a624cf6d9224aca975260e954c8"></a>

```c
void(* get_total_number_of_items )(struct bt_avrcp_tg *tg, uint8_t tid, uint8_t scope)
```

相关声明：[get_total_number_of_items](#ae5a45a624cf6d9224aca975260e954c8)、[bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取条目总数（Get Total Number Of Items）请求回调。

<a id="r_a8442f74b35a70c88defe84e948ced8d6"></a>

```c
void(* search )(struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

相关声明：[search](#a8442f74b35a70c88defe84e948ced8d6)、[bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

搜索（Search）请求回调。

<a id="r_a48b25910cffb470139e2a562b15802ce"></a>

```c
void(* passthrough_req )(struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

相关声明：[passthrough_req](#a48b25910cffb470139e2a562b15802ce)、[bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

透传（Pass Through）命令请求回调。

<a id="r_ae496f717332ea6a42507e3772793ba0e"></a>

```c
void(* list_player_app_setting_attrs )(struct bt_avrcp_tg *tg, uint8_t tid)
```

相关声明：[list_player_app_setting_attrs](#ae496f717332ea6a42507e3772793ba0e)、[bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

协议数据单元（PDU）ID 为 `BT_AVRCP_PDU_ID_LIST_PLAYER_APP_SETTING_ATTRS` 时的回调。

<a id="r_acd0d716aa960230b3e8f7c5c0bdb9b19"></a>

```c
void(* list_player_app_setting_vals )(struct bt_avrcp_tg *tg, uint8_t tid, uint8_t attr_id)
```

相关声明：[list_player_app_setting_vals](#acd0d716aa960230b3e8f7c5c0bdb9b19)、[bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

协议数据单元（PDU）ID 为 `BT_AVRCP_PDU_ID_LIST_PLAYER_APP_SETTING_VALS` 时的回调。

<a id="r_a51caea0e045788bbce8073f720eb7e19"></a>

```c
void(* get_curr_player_app_setting_val )(struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

相关声明：[get_curr_player_app_setting_val](#a51caea0e045788bbce8073f720eb7e19)、[bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

协议数据单元（PDU）ID 为 `BT_AVRCP_PDU_ID_GET_CURR_PLAYER_APP_SETTING_VAL` 时的回调。

<a id="r_a19308d4734cdd9bf397f7ba721920e97"></a>

```c
void(* set_player_app_setting_val )(struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

相关声明：[set_player_app_setting_val](#a19308d4734cdd9bf397f7ba721920e97)、[bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

协议数据单元（PDU）ID 为 `BT_AVRCP_PDU_ID_SET_PLAYER_APP_SETTING_VAL` 时的回调。

<a id="r_a20215fb3b4bb2d7c73f2d08ac3e801ec"></a>

```c
void(* get_player_app_setting_attr_text )(struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

相关声明：[get_player_app_setting_attr_text](#a20215fb3b4bb2d7c73f2d08ac3e801ec)、[bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

协议数据单元（PDU）ID 为 `BT_AVRCP_PDU_ID_GET_PLAYER_APP_SETTING_ATTR_TEXT` 时的回调。

<a id="r_a64bf13cf36066568ecbbe1006c717970"></a>

```c
void(* get_player_app_setting_val_text )(struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

相关声明：[get_player_app_setting_val_text](#a64bf13cf36066568ecbbe1006c717970)、[bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

协议数据单元（PDU）ID 为 `BT_AVRCP_PDU_ID_GET_PLAYER_APP_SETTING_VAL_TEXT` 时的回调。

<a id="r_ad8701332c6415915d32454788772dd09"></a>

```c
void(* inform_displayable_char_set )(struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

相关声明：[inform_displayable_char_set](#ad8701332c6415915d32454788772dd09)、[bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

协议数据单元（PDU）ID 为 `BT_AVRCP_PDU_ID_INFORM_DISPLAYABLE_CHAR_SET` 时的回调。

<a id="r_a883db478d1a35f0fe61f867d78366c91"></a>

```c
void(* inform_batt_status_of_ct )(struct bt_avrcp_tg *tg, uint8_t tid, uint8_t battery_status)
```

相关声明：[inform_batt_status_of_ct](#a883db478d1a35f0fe61f867d78366c91)、[bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

协议数据单元（PDU）ID 为 `BT_AVRCP_PDU_ID_INFORM_BATT_STATUS_OF_CT` 时的回调。

<a id="r_adf7e869f632ebc1ccbe7d8213a7c4f05"></a>

```c
void(* get_element_attrs )(struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

相关声明：[get_element_attrs](#adf7e869f632ebc1ccbe7d8213a7c4f05)、[bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

协议数据单元（PDU）ID 为 `BT_AVRCP_PDU_ID_GET_ELEMENT_ATTRS` 时的回调。

<a id="r_a2f022902183a0db38c65a41fdc0a8478"></a>

```c
void(* set_absolute_volume )(struct bt_avrcp_tg *tg, uint8_t tid, uint8_t absolute_volume)
```

相关声明：[set_absolute_volume](#a2f022902183a0db38c65a41fdc0a8478)、[bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置绝对音量（Set Absolute Volume）命令的目标端（TG）回调函数。

<a id="r_a889d781b5275ca24bf0603c370bb2a4e"></a>

```c
void(* get_play_status )(struct bt_avrcp_tg *tg, uint8_t tid)
```

相关声明：[get_play_status](#a889d781b5275ca24bf0603c370bb2a4e)、[bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

协议数据单元（PDU）ID 为 `BT_AVRCP_PDU_ID_GET_PLAY_STATUS` 时的回调。

<a id="r_a1ab779d9b5142590f9dcb42990d9d3cb"></a>

```c
void(* set_addressed_player )(struct bt_avrcp_tg *tg, uint8_t tid, uint16_t player_id)
```

相关声明：[set_addressed_player](#a1ab779d9b5142590f9dcb42990d9d3cb)、[bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

协议数据单元（PDU）ID 为 `BT_AVRCP_PDU_ID_SET_ADDRESSED_PLAYER` 时的回调。

<a id="r_af07da9dc841518013c6f6a1796f957f1"></a>

```c
void(* play_item )(struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

相关声明：[play_item](#af07da9dc841518013c6f6a1796f957f1)、[bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

协议数据单元（PDU）ID 为 `BT_AVRCP_PDU_ID_PLAY_ITEM` 时的回调。

<a id="r_a6946e152d68e5650f683ed6a449709d7"></a>

```c
void(* add_to_now_playing )(struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

相关声明：[add_to_now_playing](#a6946e152d68e5650f683ed6a449709d7)、[bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

协议数据单元（PDU）ID 为 `BT_AVRCP_PDU_ID_ADD_TO_NOW_PLAYING` 时的回调。

## 71.2\_详细说明（Detailed Documentation）

<a id="a6946e152d68e5650f683ed6a449709d7"></a>

### `add_to_now_playing`

```c
void(* bt_avrcp_tg_cb::add_to_now_playing) (struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

协议数据单元（PDU）ID 为 `BT_AVRCP_PDU_ID_ADD_TO_NOW_PLAYING` 时的回调。

目标端（TG）收到厂商相关命令（Vendor Dependent Command）`ADD_TO_NOW_PLAYING` 时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 命令的事务标签（Transaction Label）。 |
| `buf` | 包含 `ADD_TO_NOW_PLAYING` 命令载荷的缓冲区，格式为 `bt_avrcp_add_to_now_playing_cmd`。应用应按大端字节序（Big-endian）解析各字段。 |

<a id="a82c5ca1100844e5119224aa6bac19bd2"></a>

### `browsing_connected`

```c
void(* bt_avrcp_tg_cb::browsing_connected) (struct bt_conn *conn, struct bt_avrcp_tg *tg)
```

AVRCP 目标端（TG）浏览连接已建立。

此回调向应用通知 AVRCP 浏览连接，即音视频控制传输协议（AVCTP）的浏览 L2CAP 连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `tg` | AVRCP 目标端（TG）连接对象。 |

<a id="ad66a2945e2cb464bf7324a0685106d47"></a>

### `browsing_disconnected`

```c
void(* bt_avrcp_tg_cb::browsing_disconnected) (struct bt_avrcp_tg *tg)
```

AVRCP 目标端（TG）浏览连接已断开。

此回调向应用通知 AVRCP 浏览连接已经断开。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |

<a id="a37d8a221b66cf3bad74790532b559cff"></a>

### `change_path`

```c
void(* bt_avrcp_tg_cb::change_path) (struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

更改路径（Change Path）请求回调。

每当从控制端（CT）收到 AVRCP `CHANGE_PATH` 请求时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `buf` | 包含更改路径（Change Path）命令参数的请求缓冲区。应用可以按照 `bt_avrcp_change_path_cmd` 定义的格式解析载荷。注意，所有多八位字节字段均采用大端格式（Big-endian）编码。 |

<a id="a8f0994f1b59d16ef74a7430221f53db0"></a>

### `connected`

```c
void(* bt_avrcp_tg_cb::connected) (struct bt_conn *conn, struct bt_avrcp_tg *tg)
```

AVRCP 目标端（TG）连接已建立。

此回调向应用通知 AVRCP 连接，即 AVCTP 的 L2CAP 连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `tg` | AVRCP 目标端（TG）连接对象。 |

<a id="a9c64cc44157e6cedec9decc00f0022b3"></a>

### `disconnected`

```c
void(* bt_avrcp_tg_cb::disconnected) (struct bt_avrcp_tg *tg)
```

AVRCP 目标端（TG）连接已断开。

此回调向应用通知 AVRCP 连接已经断开。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |

<a id="ab3fe452afec12ff31975763c5269c94f"></a>

### `get_caps`

```c
void(* bt_avrcp_tg_cb::get_caps) (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t cap_id)
```

获取能力（Get Capabilities）请求回调。

每当收到 AVRCP 获取能力（Get Capabilities）命令时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `cap_id` | 请求的能力 ID。 |

<a id="a51caea0e045788bbce8073f720eb7e19"></a>

### `get_curr_player_app_setting_val`

```c
void(* bt_avrcp_tg_cb::get_curr_player_app_setting_val) (struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

协议数据单元（PDU）ID 为 `BT_AVRCP_PDU_ID_GET_CURR_PLAYER_APP_SETTING_VAL` 时的回调。

目标端（TG）收到厂商相关命令（Vendor Dependent Command）`GET_CURR_PLAYER_APP_SETTING_VAL` 时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 命令的事务标签（Transaction Label）。 |
| `buf` | 包含 `GET_CURR_PLAYER_APP_SETTING_VAL` 命令载荷的缓冲区，格式为 `bt_avrcp_get_curr_player_app_setting_val_cmd`。应用应按大端字节序（Big-endian）解析各字段。 |

<a id="adf7e869f632ebc1ccbe7d8213a7c4f05"></a>

### `get_element_attrs`

```c
void(* bt_avrcp_tg_cb::get_element_attrs) (struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

协议数据单元（PDU）ID 为 `BT_AVRCP_PDU_ID_GET_ELEMENT_ATTRS` 时的回调。

目标端（TG）收到厂商相关命令（Vendor Dependent Command）`GET_ELEMENT_ATTRS` 时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 命令的事务标签（Transaction Label）。 |
| `buf` | 包含 `GET_ELEMENT_ATTRS` 命令载荷的缓冲区，格式为 `bt_avrcp_get_element_attrs_cmd`。应用应按大端字节序（Big-endian）解析各字段。 |

<a id="a0f117772eb0f55e20214b0be8d93a6fa"></a>

### `get_folder_items`

```c
void(* bt_avrcp_tg_cb::get_folder_items) (struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

获取文件夹条目（Get Folder Items）请求回调。

每当从控制端（CT）收到 AVRCP `GET_FOLDER_ITEMS` 请求时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `buf` | 包含获取文件夹条目（Get Folder Items）命令参数的请求缓冲区。应用可以按照 `bt_avrcp_get_folder_items_cmd` 定义的格式解析载荷。注意，所有多八位字节字段均采用大端格式（Big-endian）编码。 |

<a id="a878eaaf2358b0773e964dc68c910a377"></a>

### `get_item_attrs`

```c
void(* bt_avrcp_tg_cb::get_item_attrs) (struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

获取条目属性（Get Item Attributes）请求回调。

每当从控制端（CT）收到 AVRCP `GET_ITEM_ATTRIBUTES` 请求时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `buf` | 包含获取条目属性（Get Item Attributes）命令参数的请求缓冲区。应用可以按照 `bt_avrcp_get_item_attrs_cmd` 定义的格式解析载荷。注意，所有多八位字节字段均采用大端格式（Big-endian）编码。 |

<a id="a889d781b5275ca24bf0603c370bb2a4e"></a>

### `get_play_status`

```c
void(* bt_avrcp_tg_cb::get_play_status) (struct bt_avrcp_tg *tg, uint8_t tid)
```

协议数据单元（PDU）ID 为 `BT_AVRCP_PDU_ID_GET_PLAY_STATUS` 时的回调。

目标端（TG）收到厂商相关命令（Vendor Dependent Command）`GET_PLAY_STATUS` 时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 命令的事务标签（Transaction Label）。 |

<a id="a20215fb3b4bb2d7c73f2d08ac3e801ec"></a>

### `get_player_app_setting_attr_text`

```c
void(* bt_avrcp_tg_cb::get_player_app_setting_attr_text) (struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

协议数据单元（PDU）ID 为 `BT_AVRCP_PDU_ID_GET_PLAYER_APP_SETTING_ATTR_TEXT` 时的回调。

目标端（TG）收到厂商相关命令（Vendor Dependent Command）`GET_PLAYER_APP_SETTING_ATTR_TEXT` 时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 命令的事务标签（Transaction Label）。 |
| `buf` | 包含 `GET_PLAYER_APP_SETTING_ATTR_TEXT` 命令载荷的缓冲区，格式为 `bt_avrcp_get_player_app_setting_attr_text_cmd`。应用应按大端字节序（Big-endian）解析各字段。 |

<a id="a64bf13cf36066568ecbbe1006c717970"></a>

### `get_player_app_setting_val_text`

```c
void(* bt_avrcp_tg_cb::get_player_app_setting_val_text) (struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

协议数据单元（PDU）ID 为 `BT_AVRCP_PDU_ID_GET_PLAYER_APP_SETTING_VAL_TEXT` 时的回调。

目标端（TG）收到厂商相关命令（Vendor Dependent Command）`GET_PLAYER_APP_SETTING_VAL_TEXT` 时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 命令的事务标签（Transaction Label）。 |
| `buf` | 包含 `GET_PLAYER_APP_SETTING_VAL_TEXT` 命令载荷的缓冲区，格式为 `bt_avrcp_get_player_app_setting_val_text_cmd`。应用应按大端字节序（Big-endian）解析各字段。 |

<a id="ae5a45a624cf6d9224aca975260e954c8"></a>

### `get_total_number_of_items`

```c
void(* bt_avrcp_tg_cb::get_total_number_of_items) (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t scope)
```

获取条目总数（Get Total Number Of Items）请求回调。

每当从控制端（CT）收到 AVRCP `GET_TOTAL_NUMBER_OF_ITEMS` 请求时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `scope` | 要获取条目总数的浏览作用域（Browsing Scope）；有效值参见 `bt_avrcp_scope_t`。 |

<a id="a883db478d1a35f0fe61f867d78366c91"></a>

### `inform_batt_status_of_ct`

```c
void(* bt_avrcp_tg_cb::inform_batt_status_of_ct) (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t battery_status)
```

协议数据单元（PDU）ID 为 `BT_AVRCP_PDU_ID_INFORM_BATT_STATUS_OF_CT` 时的回调。

目标端（TG）收到厂商相关命令（Vendor Dependent Command）`INFORM_BATT_STATUS_OF_CT` 时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 命令的事务标签（Transaction Label）。 |
| `battery_status` | 电池状态值，类型为 `bt_avrcp_battery_status_t`。 |

<a id="ad8701332c6415915d32454788772dd09"></a>

### `inform_displayable_char_set`

```c
void(* bt_avrcp_tg_cb::inform_displayable_char_set) (struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

协议数据单元（PDU）ID 为 `BT_AVRCP_PDU_ID_INFORM_DISPLAYABLE_CHAR_SET` 时的回调。

目标端（TG）收到厂商相关命令（Vendor Dependent Command）`INFORM_DISPLAYABLE_CHAR_SET` 时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 命令的事务标签（Transaction Label）。 |
| `buf` | 包含 `INFORM_DISPLAYABLE_CHAR_SET` 命令载荷的缓冲区，格式为 `bt_avrcp_inform_displayable_char_set_cmd`。应用应按大端字节序（Big-endian）解析各字段。 |

<a id="ae496f717332ea6a42507e3772793ba0e"></a>

### `list_player_app_setting_attrs`

```c
void(* bt_avrcp_tg_cb::list_player_app_setting_attrs) (struct bt_avrcp_tg *tg, uint8_t tid)
```

协议数据单元（PDU）ID 为 `BT_AVRCP_PDU_ID_LIST_PLAYER_APP_SETTING_ATTRS` 时的回调。

目标端（TG）收到厂商相关命令（Vendor Dependent Command）`LIST_PLAYER_APP_SETTING_ATTRS` 时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 命令的事务标签（Transaction Label）。 |

<a id="acd0d716aa960230b3e8f7c5c0bdb9b19"></a>

### `list_player_app_setting_vals`

```c
void(* bt_avrcp_tg_cb::list_player_app_setting_vals) (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t attr_id)
```

协议数据单元（PDU）ID 为 `BT_AVRCP_PDU_ID_LIST_PLAYER_APP_SETTING_VALS` 时的回调。

目标端（TG）收到厂商相关命令（Vendor Dependent Command）`LIST_PLAYER_APP_SETTING_VALS` 时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 命令的事务标签（Transaction Label）。 |
| `attr_id` | 要列出其可能取值的播放器应用设置属性 ID，例如均衡器（Equalizer）、重复模式（Repeat Mode）、随机播放（Shuffle）和扫描（Scan）。 |

<a id="a48b25910cffb470139e2a562b15802ce"></a>

### `passthrough_req`

```c
void(* bt_avrcp_tg_cb::passthrough_req) (struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

透传（Pass Through）命令请求回调。

每当请求 AVRCP 透传（Pass Through）命令时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `buf` | 包含透传（PASS THROUGH）命令载荷的缓冲区。应用可以按照 `bt_avrcp_passthrough_cmd` 定义的格式解析该载荷。注意，数据采用大端格式（Big-endian）编码。 |

<a id="af07da9dc841518013c6f6a1796f957f1"></a>

### `play_item`

```c
void(* bt_avrcp_tg_cb::play_item) (struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

协议数据单元（PDU）ID 为 `BT_AVRCP_PDU_ID_PLAY_ITEM` 时的回调。

目标端（TG）收到厂商相关命令（Vendor Dependent Command）`PLAY_ITEM` 时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 命令的事务标签（Transaction Label）。 |
| `buf` | 包含 `PLAY_ITEM` 命令载荷的缓冲区，格式为 `bt_avrcp_play_item_cmd`。应用应按大端字节序（Big-endian）解析各字段。 |

<a id="a45954c3a1f3e8dffb1bc111845c875ce"></a>

### `register_notification`

```c
void(* bt_avrcp_tg_cb::register_notification) (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t event_id, uint32_t interval)
```

注册通知（Register Notification）请求回调。

每当请求 AVRCP 注册通知（Register Notification）时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `event_id` | 控制端（CT）希望注册的事件 ID，类型为 `bt_avrcp_evt_t`。 |
| `interval` | 播放位置变化事件的播放间隔（Playback Interval）；其他事件将该值设为 0，表示忽略。 |

<a id="a8442f74b35a70c88defe84e948ced8d6"></a>

### `search`

```c
void(* bt_avrcp_tg_cb::search) (struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

搜索（Search）请求回调。

每当从控制端（CT）收到 AVRCP `SEARCH` 请求时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `buf` | 包含搜索（Search）命令参数的请求缓冲区。应用可以按照 `bt_avrcp_search_cmd` 定义的格式解析载荷。注意，所有多八位字节字段均采用大端格式（Big-endian）编码。 |

<a id="a2f022902183a0db38c65a41fdc0a8478"></a>

### `set_absolute_volume`

```c
void(* bt_avrcp_tg_cb::set_absolute_volume) (struct bt_avrcp_tg *tg, uint8_t tid, uint8_t absolute_volume)
```

设置绝对音量（Set Absolute Volume）命令的目标端（TG）回调函数。

从控制端（CT）收到设置绝对音量（Set Absolute Volume）命令时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 命令的事务标签（Transaction Label）。 |
| `absolute_volume` | 绝对音量值，范围为 `0x00–0x7F`。 |

<a id="a1ab779d9b5142590f9dcb42990d9d3cb"></a>

### `set_addressed_player`

```c
void(* bt_avrcp_tg_cb::set_addressed_player) (struct bt_avrcp_tg *tg, uint8_t tid, uint16_t player_id)
```

协议数据单元（PDU）ID 为 `BT_AVRCP_PDU_ID_SET_ADDRESSED_PLAYER` 时的回调。

目标端（TG）收到厂商相关命令（Vendor Dependent Command）`SET_ADDRESSED_PLAYER` 时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 命令的事务标签（Transaction Label）。 |
| `player_id` | 要设为受控播放器（Addressed Player）的播放器 ID。 |

<a id="a4179686bbe4030c44f0a277532dcb96b"></a>

### `set_browsed_player`

```c
void(* bt_avrcp_tg_cb::set_browsed_player) (struct bt_avrcp_tg *tg, uint8_t tid, uint16_t player_id)
```

设置浏览播放器（Set Browsed Player）请求回调。

每当收到 AVRCP 设置浏览播放器（Set Browsed Player）的请求时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `player_id` | 要设为浏览播放器（Browsed Player）的播放器 ID。 |

<a id="a19308d4734cdd9bf397f7ba721920e97"></a>

### `set_player_app_setting_val`

```c
void(* bt_avrcp_tg_cb::set_player_app_setting_val) (struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf)
```

协议数据单元（PDU）ID 为 `BT_AVRCP_PDU_ID_SET_PLAYER_APP_SETTING_VAL` 时的回调。

目标端（TG）收到厂商相关命令（Vendor Dependent Command）`SET_PLAYER_APP_SETTING_VAL` 时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 命令的事务标签（Transaction Label）。 |
| `buf` | 包含 `SET_PLAYER_APP_SETTING_VAL` 命令载荷的缓冲区，格式为 `bt_avrcp_set_player_app_setting_val_cmd`。应用应按大端字节序（Big-endian）解析各字段。 |

<a id="ab9f1a086a71522986808f3ebc2cbd2de"></a>

### `subunit_info_req`

```c
void(* bt_avrcp_tg_cb::subunit_info_req) (struct bt_avrcp_tg *tg, uint8_t tid)
```

子单元信息（Subunit Info）请求回调。

每当请求 AVRCP 子单元信息（Subunit Info）时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端（TG）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |

<a id="a933eb30910fef1e916e60ff21d4255ec"></a>

### `unit_info_req`

```c
void(* bt_avrcp_tg_cb::unit_info_req) (struct bt_avrcp_tg *tg, uint8_t tid)
```

单元信息（Unit Info）请求回调。

每当请求 AVRCP 单元信息（Unit Info）时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `tg` | AVRCP 目标端（TG）连接对象。 |

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 71.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)
- [bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)
- [bt_avrcp_add_to_now_playing_cmd](P016_bt_avrcp_add_to_now_playing_cmd_结构体.md)
- [bt_avrcp_change_path_cmd](P020_bt_avrcp_change_path_cmd_结构体.md)
- [bt_avrcp_get_curr_player_app_setting_val_cmd](P032_bt_avrcp_get_curr_player_app_setting_val_cmd_结构体.md)
- [bt_avrcp_get_element_attrs_cmd](P034_bt_avrcp_get_element_attrs_cmd_结构体.md)
- [bt_avrcp_get_folder_items_cmd](P036_bt_avrcp_get_folder_items_cmd_结构体.md)
- [bt_avrcp_get_item_attrs_cmd](P038_bt_avrcp_get_item_attrs_cmd_结构体.md)
- [bt_avrcp_get_player_app_setting_attr_text_cmd](P041_bt_avrcp_get_player_app_setting_attr_text_cmd_结构体.md)
- [bt_avrcp_get_player_app_setting_val_text_cmd](P043_bt_avrcp_get_player_app_setting_val_text_cmd_结构体.md)
- [bt_avrcp_scope_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaabab9a4f37b3f9653ca95dd4b5944707)
- [bt_avrcp_battery_status_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga33825b183b12a2b29d5148a7366c0e77)
- [bt_avrcp_inform_displayable_char_set_cmd](P048_bt_avrcp_inform_displayable_char_set_cmd_结构体.md)
- [bt_avrcp_passthrough_cmd](P056_bt_avrcp_passthrough_cmd_结构体.md)
- [bt_avrcp_play_item_cmd](P059_bt_avrcp_play_item_cmd_结构体.md)
- [bt_avrcp_evt_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaf55aae17f67a1361279ae208b17e4a75)
- [bt_avrcp_search_cmd](P062_bt_avrcp_search_cmd_结构体.md)
- [bt_avrcp_set_player_app_setting_val_cmd](P068_bt_avrcp_set_player_app_setting_val_cmd_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P070_bt_avrcp_tg_结构体.md) · [返回大纲](大纲.md) · [下一章](P072_bt_avrcp_unit_info_rsp_结构体.md)
