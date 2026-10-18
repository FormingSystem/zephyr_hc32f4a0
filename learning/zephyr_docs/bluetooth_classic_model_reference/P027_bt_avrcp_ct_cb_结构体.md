---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-27
title: bt_avrcp_ct_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__ct__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_bt\_avrcp\_ct\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__ct__cb.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 27.1\_数据成员（Data Fields）

<a id="r_a134720ca0e05d4e6c893f391ca842344"></a>

```c
void(* connected )(struct bt_conn *conn, struct bt_avrcp_ct *ct)
```

相关声明：[connected](#a134720ca0e05d4e6c893f391ca842344)、[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)、[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)。

AVRCP 控制端（CT）连接已建立。

<a id="r_aae8977ac1f58e40bbf52c1c52e571395"></a>

```c
void(* disconnected )(struct bt_avrcp_ct *ct)
```

相关声明：[disconnected](#aae8977ac1f58e40bbf52c1c52e571395)、[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)。

AVRCP 控制端（CT）连接已断开。

<a id="r_a3035cc2cace9a3e8d463d54c72dd1fed"></a>

```c
void(* browsing_connected )(struct bt_conn *conn, struct bt_avrcp_ct *ct)
```

相关声明：[browsing_connected](#a3035cc2cace9a3e8d463d54c72dd1fed)、[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)、[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)。

AVRCP 控制端（CT）浏览连接（Browsing Connection）已建立。

<a id="r_ae92ce375dd6cff3b2b719b39b02e99af"></a>

```c
void(* browsing_disconnected )(struct bt_avrcp_ct *ct)
```

相关声明：[browsing_disconnected](#ae92ce375dd6cff3b2b719b39b02e99af)、[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)。

AVRCP 控制端（CT）浏览连接已断开。

<a id="r_a15e7780c8c5c4037434c2ab20f47a8f6"></a>

```c
void(* get_caps )(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status, struct net_buf *buf)
```

相关声明：[get_caps](#a15e7780c8c5c4037434c2ab20f47a8f6)、[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

`bt_avrcp_get_caps()` 的回调函数。

<a id="r_ac842ad673b8a943e9f1b188346b8d92d"></a>

```c
void(* unit_info_rsp )(struct bt_avrcp_ct *ct, uint8_t tid, struct bt_avrcp_unit_info_rsp *rsp)
```

相关声明：[unit_info_rsp](#ac842ad673b8a943e9f1b188346b8d92d)、[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_avrcp_unit_info_rsp](P072_bt_avrcp_unit_info_rsp_结构体.md)。

`bt_avrcp_get_unit_info()` 的回调函数。

<a id="r_a4e33bc54f28204959ccd4fa2c766980d"></a>

```c
void(* subunit_info_rsp )(struct bt_avrcp_ct *ct, uint8_t tid, struct bt_avrcp_subunit_info_rsp *rsp)
```

相关声明：[subunit_info_rsp](#a4e33bc54f28204959ccd4fa2c766980d)、[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_avrcp_subunit_info_rsp](P069_bt_avrcp_subunit_info_rsp_结构体.md)。

`bt_avrcp_get_subunit_info()` 的回调函数。

<a id="r_a69ab87eb920eae066034054e7bf89c7b"></a>

```c
void(* passthrough_rsp )(struct bt_avrcp_ct *ct, uint8_t tid, bt_avrcp_rsp_t result, const struct bt_avrcp_passthrough_rsp *rsp)
```

相关声明：[passthrough_rsp](#a69ab87eb920eae066034054e7bf89c7b)、[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_avrcp_rsp_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaba2d8faec2c3baf7403199ea8a509326)、[bt_avrcp_passthrough_rsp](P058_bt_avrcp_passthrough_rsp_结构体.md)。

`bt_avrcp_passthrough()` 的回调函数。

<a id="r_a768c099504dd24ee67556f69b493ddb0"></a>

```c
void(* set_browsed_player )(struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

相关声明：[set_browsed_player](#a768c099504dd24ee67556f69b493ddb0)、[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

`bt_avrcp_ct_set_browsed_player()` 的回调函数。

<a id="r_a2350f1a00f68008b73ca1400f8954b4b"></a>

```c
void(* get_folder_items )(struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

相关声明：[get_folder_items](#a2350f1a00f68008b73ca1400f8954b4b)、[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

`bt_avrcp_ct_get_folder_items()` 的回调函数。

<a id="r_afc0ef62c71331961f3196bc2668f4dbb"></a>

```c
void(* change_path )(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status, uint32_t num_items)
```

相关声明：[change_path](#afc0ef62c71331961f3196bc2668f4dbb)、[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

`bt_avrcp_ct_change_path()` 的回调函数。

<a id="r_ad7b512d997a5326cee867651ad7cbfaf"></a>

```c
void(* get_item_attrs )(struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

相关声明：[get_item_attrs](#ad7b512d997a5326cee867651ad7cbfaf)、[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

`bt_avrcp_ct_get_item_attrs()` 的回调函数。

<a id="r_a4b74108af0ab8cb0119af8c477ff9b33"></a>

```c
void(* get_total_number_of_items )(struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

相关声明：[get_total_number_of_items](#a4b74108af0ab8cb0119af8c477ff9b33)、[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

`bt_avrcp_ct_get_total_number_of_items()` 的回调函数。

<a id="r_a0e361f81921ae80e89947e1ede29b66c"></a>

```c
void(* search )(struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

相关声明：[search](#a0e361f81921ae80e89947e1ede29b66c)、[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

`bt_avrcp_ct_search()` 的回调函数。

<a id="r_a81e9799d9efe9133dedd91386e49960c"></a>

```c
void(* browsing_general_reject )(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status)
```

相关声明：[browsing_general_reject](#a81e9799d9efe9133dedd91386e49960c)、[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

浏览通道通用拒绝响应（General Reject Response）的回调函数。

<a id="r_a0c8b90004b116751f94b2c5c1af02af8"></a>

```c
void(* notification )(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status, uint8_t event_id, struct bt_avrcp_event_data *data)
```

相关声明：[notification](#a0c8b90004b116751f94b2c5c1af02af8)、[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_avrcp_event_data](P028_bt_avrcp_event_data_结构体.md)。

事件通知响应（Event Notification Response）的控制端（CT）回调函数。

<a id="r_a3c37bfd2f03a8c76a725b38210794e21"></a>

```c
void(* list_player_app_setting_attrs )(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status, struct net_buf *buf)
```

相关声明：[list_player_app_setting_attrs](#a3c37bfd2f03a8c76a725b38210794e21)、[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

协议数据单元（PDU）ID 为 `LIST_PLAYER_APP_SETTING_ATTRS` 时的回调。

<a id="r_a8b16ac730eb5c9dc95e7c3e660f802cc"></a>

```c
void(* list_player_app_setting_vals )(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status, struct net_buf *buf)
```

相关声明：[list_player_app_setting_vals](#a8b16ac730eb5c9dc95e7c3e660f802cc)、[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

协议数据单元（PDU）ID 为 `LIST_PLAYER_APP_SETTING_VALS` 时的回调。

<a id="r_ac5fd1a8d9927edbd56cb24f8760c8401"></a>

```c
void(* get_curr_player_app_setting_val )(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status, struct net_buf *buf)
```

相关声明：[get_curr_player_app_setting_val](#ac5fd1a8d9927edbd56cb24f8760c8401)、[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

协议数据单元（PDU）ID 为 `GET_CURR_PLAYER_APP_SETTING_VAL` 时的回调。

<a id="r_a5990204dc0d6b0437308e69eef8f7f47"></a>

```c
void(* set_player_app_setting_val )(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status)
```

相关声明：[set_player_app_setting_val](#a5990204dc0d6b0437308e69eef8f7f47)、[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

协议数据单元（PDU）ID 为 `SET_PLAYER_APP_SETTING_VAL` 时的回调。

<a id="r_a02a9fa26f9827f327b6030758c539210"></a>

```c
void(* get_player_app_setting_attr_text )(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status, struct net_buf *buf)
```

相关声明：[get_player_app_setting_attr_text](#a02a9fa26f9827f327b6030758c539210)、[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

协议数据单元（PDU）ID 为 `GET_PLAYER_APP_SETTING_ATTR_TEXT` 时的回调。

<a id="r_ac41f9cfa20c1b1a092515b345b468a10"></a>

```c
void(* get_player_app_setting_val_text )(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status, struct net_buf *buf)
```

相关声明：[get_player_app_setting_val_text](#ac41f9cfa20c1b1a092515b345b468a10)、[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

协议数据单元（PDU）ID 为 `GET_PLAYER_APP_SETTING_VAL_TEXT` 时的回调。

<a id="r_a80f78ad02b0b7e9db9de19a0dceeea50"></a>

```c
void(* inform_displayable_char_set )(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status)
```

相关声明：[inform_displayable_char_set](#a80f78ad02b0b7e9db9de19a0dceeea50)、[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

协议数据单元（PDU）ID 为 `INFORM_DISPLAYABLE_CHAR_SET` 时的回调。

<a id="r_a1b88debebdf19263d760f9f8e3d447d6"></a>

```c
void(* inform_batt_status_of_ct )(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status)
```

相关声明：[inform_batt_status_of_ct](#a1b88debebdf19263d760f9f8e3d447d6)、[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

协议数据单元（PDU）ID 为 `INFORM_BATT_STATUS_OF_CT` 时的回调。

<a id="r_ad102ac42003f1013b14809c4dd1057a4"></a>

```c
void(* set_absolute_volume )(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status, uint8_t absolute_volume)
```

相关声明：[set_absolute_volume](#ad102ac42003f1013b14809c4dd1057a4)、[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置绝对音量（Set Absolute Volume）响应的控制端（CT）回调函数。

<a id="r_accb0eaa7ae05c888b963278fe320c17c"></a>

```c
void(* get_element_attrs )(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status, struct net_buf *buf)
```

相关声明：[get_element_attrs](#accb0eaa7ae05c888b963278fe320c17c)、[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

协议数据单元（PDU）ID 为 `GET_ELEMENT_ATTRS` 时的回调。

<a id="r_ac25d85d11c28d64225b42a6e5f3fa3ce"></a>

```c
void(* get_play_status )(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status, struct net_buf *buf)
```

相关声明：[get_play_status](#ac25d85d11c28d64225b42a6e5f3fa3ce)、[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

协议数据单元（PDU）ID 为 `GET_PLAY_STATUS` 时的回调。

<a id="r_a6748f42e5ba39a1a6b2d7a50729c0316"></a>

```c
void(* set_addressed_player )(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status)
```

相关声明：[set_addressed_player](#a6748f42e5ba39a1a6b2d7a50729c0316)、[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

协议数据单元（PDU）ID 为 `SET_ADDRESSED_PLAYER` 时的回调。

<a id="r_a7ae520df749b156f9875cf3e6ee62a96"></a>

```c
void(* play_item )(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status)
```

相关声明：[play_item](#a7ae520df749b156f9875cf3e6ee62a96)、[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

协议数据单元（PDU）ID 为 `PLAY_ITEM` 时的回调。

<a id="r_ae5f09e516a212e97c36e0c32074c9477"></a>

```c
void(* add_to_now_playing )(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status)
```

相关声明：[add_to_now_playing](#ae5f09e516a212e97c36e0c32074c9477)、[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

协议数据单元（PDU）ID 为 `ADD_TO_NOW_PLAYING` 时的回调。

## 27.2\_详细说明（Detailed Documentation）

<a id="ae5f09e516a212e97c36e0c32074c9477"></a>

### `add_to_now_playing`

```c
void(* bt_avrcp_ct_cb::add_to_now_playing) (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status)
```

协议数据单元（PDU）ID 为 `ADD_TO_NOW_PLAYING` 时的回调。

收到 `ADD_TO_NOW_PLAYING` 响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `status` | 目标端（TG）返回的状态码，表示操作结果，类型为 `bt_avrcp_status_t`。通常对应 `BT_AVRCP_STATUS_*` 值，例如 `BT_AVRCP_STATUS_SUCCESS` 或 `BT_AVRCP_STATUS_INVALID_PARAMETER`。 |

<a id="a3035cc2cace9a3e8d463d54c72dd1fed"></a>

### `browsing_connected`

```c
void(* bt_avrcp_ct_cb::browsing_connected) (struct bt_conn *conn, struct bt_avrcp_ct *ct)
```

AVRCP 控制端（CT）浏览连接（Browsing Connection）已建立。

此回调向应用通知 AVRCP 浏览连接，即音视频控制传输协议（AVCTP）的浏览 L2CAP 连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `ct` | AVRCP 控制端（CT）连接对象。 |

<a id="ae92ce375dd6cff3b2b719b39b02e99af"></a>

### `browsing_disconnected`

```c
void(* bt_avrcp_ct_cb::browsing_disconnected) (struct bt_avrcp_ct *ct)
```

AVRCP 控制端（CT）浏览连接已断开。

此回调向应用通知 AVRCP 浏览连接已经断开。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |

<a id="a81e9799d9efe9133dedd91386e49960c"></a>

### `browsing_general_reject`

```c
void(* bt_avrcp_ct_cb::browsing_general_reject) (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status)
```

浏览通道通用拒绝响应（General Reject Response）的回调函数。

在浏览通道上收到通用拒绝响应（General Reject Response）时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 响应的事务标签（Transaction Label）。 |
| `status` | 表示拒绝原因的状态码，参见 `bt_avrcp_status_t`。 |

<a id="afc0ef62c71331961f3196bc2668f4dbb"></a>

### `change_path`

```c
void(* bt_avrcp_ct_cb::change_path) (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status, uint32_t num_items)
```

`bt_avrcp_ct_change_path()` 的回调函数。

更改路径（Change Path）过程完成时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 响应的事务标签（Transaction Label）。 |
| `status` | 操作状态，参见 `bt_avrcp_status_t`。 |
| `num_items` | 新文件夹中的条目数量，仅在 `status` 为 `BT_AVRCP_STATUS_OPERATION_COMPLETED` 时有效。 |

<a id="a134720ca0e05d4e6c893f391ca842344"></a>

### `connected`

```c
void(* bt_avrcp_ct_cb::connected) (struct bt_conn *conn, struct bt_avrcp_ct *ct)
```

AVRCP 控制端（CT）连接已建立。

此回调向应用通知 AVRCP 连接，即 AVCTP 的 L2CAP 连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `ct` | AVRCP 控制端（CT）连接对象。 |

<a id="aae8977ac1f58e40bbf52c1c52e571395"></a>

### `disconnected`

```c
void(* bt_avrcp_ct_cb::disconnected) (struct bt_avrcp_ct *ct)
```

AVRCP 控制端（CT）连接已断开。

此回调向应用通知 AVRCP 连接已经断开。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |

<a id="a15e7780c8c5c4037434c2ab20f47a8f6"></a>

### `get_caps`

```c
void(* bt_avrcp_ct_cb::get_caps) (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status, struct net_buf *buf)
```

`bt_avrcp_get_caps()` 的回调函数。

获取能力（Get Capabilities）过程完成时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 响应的事务标签（Transaction Label）。 |
| `status` | 目标端（TG）返回的状态码，表示操作结果，类型为 `bt_avrcp_status_t`。通常对应 `BT_AVRCP_STATUS_*` 值，例如 `BT_AVRCP_STATUS_SUCCESS` 或 `BT_AVRCP_STATUS_INVALID_PARAMETER`。 |
| `buf` | 包含目标端（TG）返回的 `BT_AVRCP_PDU_ID_GET_CAPS` 载荷的响应缓冲区，应用可以按照 `bt_avrcp_get_caps_rsp` 定义的格式解析。如果 `status` 在 `BT_AVRCP_STATUS_INVALID_COMMAND` 到 `BT_AVRCP_STATUS_ADDRESSED_PLAYER_CHANGED` 范围内，且不等于 `BT_AVRCP_STATUS_OPERATION_COMPLETED`，则表示 AVRCP 响应码为 AV/C 拒绝响应（REJECTED），此时 `buf` 为 `NULL`。注意，所有多八位字节字段均采用大端格式（Big-endian）编码。 |

<a id="ac5fd1a8d9927edbd56cb24f8760c8401"></a>

### `get_curr_player_app_setting_val`

```c
void(* bt_avrcp_ct_cb::get_curr_player_app_setting_val) (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status, struct net_buf *buf)
```

协议数据单元（PDU）ID 为 `GET_CURR_PLAYER_APP_SETTING_VAL` 时的回调。

收到 `GET_CURR_PLAYER_APP_SETTING_VAL` 响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `status` | 目标端（TG）返回的状态码，表示操作结果，类型为 `bt_avrcp_status_t`。通常对应 `BT_AVRCP_STATUS_*` 值，例如 `BT_AVRCP_STATUS_SUCCESS` 或 `BT_AVRCP_STATUS_INVALID_PARAMETER`。 |
| `buf` | 包含目标端（TG）返回的 `GET_CURR_PLAYER_APP_SETTING_VAL` 载荷的响应缓冲区，应用可以按照 `bt_avrcp_get_curr_player_app_setting_val_rsp` 定义的格式解析。如果 `status` 在 `BT_AVRCP_STATUS_INVALID_COMMAND` 到 `BT_AVRCP_STATUS_ADDRESSED_PLAYER_CHANGED` 范围内，且不等于 `BT_AVRCP_STATUS_OPERATION_COMPLETED`，则表示 AVRCP 响应码为 AV/C 拒绝响应（REJECTED），此时 `buf` 为 `NULL`。注意，所有多八位字节字段均采用大端格式（Big-endian）编码。 |

<a id="accb0eaa7ae05c888b963278fe320c17c"></a>

### `get_element_attrs`

```c
void(* bt_avrcp_ct_cb::get_element_attrs) (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status, struct net_buf *buf)
```

协议数据单元（PDU）ID 为 `GET_ELEMENT_ATTRS` 时的回调。

收到 `GET_ELEMENT_ATTRS` 响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `status` | 目标端（TG）返回的状态码，表示操作结果，类型为 `bt_avrcp_status_t`。通常对应 `BT_AVRCP_STATUS_*` 值，例如 `BT_AVRCP_STATUS_SUCCESS` 或 `BT_AVRCP_STATUS_INVALID_PARAMETER`。 |
| `buf` | 包含目标端（TG）返回的 `GET_ELEMENT_ATTRS` 载荷的响应缓冲区，应用可以按照 `bt_avrcp_get_element_attrs_rsp` 定义的格式解析。如果 `status` 在 `BT_AVRCP_STATUS_INVALID_COMMAND` 到 `BT_AVRCP_STATUS_ADDRESSED_PLAYER_CHANGED` 范围内，且不等于 `BT_AVRCP_STATUS_OPERATION_COMPLETED`，则表示 AVRCP 响应码为 AV/C 拒绝响应（REJECTED），此时 `buf` 为 `NULL`。注意，所有多八位字节字段均采用大端格式（Big-endian）编码。 |

<a id="a2350f1a00f68008b73ca1400f8954b4b"></a>

### `get_folder_items`

```c
void(* bt_avrcp_ct_cb::get_folder_items) (struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

`bt_avrcp_ct_get_folder_items()` 的回调函数。

获取文件夹条目（Get Folder Items）过程完成时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 响应的事务标签（Transaction Label）。 |
| `buf` | 包含获取文件夹条目（Get Folder Items）响应数据的缓冲区。操作成功时，应用可以按照 `bt_avrcp_get_folder_items_rsp` 定义的格式解析载荷。如果 `status` 表示拒绝错误或操作未完成，则 `buf` 仅包含一个状态字节。注意，数据采用大端格式（Big-endian）编码。 |

<a id="ad7b512d997a5326cee867651ad7cbfaf"></a>

### `get_item_attrs`

```c
void(* bt_avrcp_ct_cb::get_item_attrs) (struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

`bt_avrcp_ct_get_item_attrs()` 的回调函数。

获取条目属性（Get Item Attributes）过程完成时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 响应的事务标签（Transaction Label）。 |
| `buf` | 包含获取条目属性（Get Item Attributes）响应数据的缓冲区。操作成功时，应用可以按照 `bt_avrcp_get_item_attrs_rsp` 定义的格式解析载荷。如果 `status` 表示拒绝错误或操作未完成，则 `buf` 仅包含一个状态字节。注意，数据采用大端格式（Big-endian）编码。 |

<a id="ac25d85d11c28d64225b42a6e5f3fa3ce"></a>

### `get_play_status`

```c
void(* bt_avrcp_ct_cb::get_play_status) (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status, struct net_buf *buf)
```

协议数据单元（PDU）ID 为 `GET_PLAY_STATUS` 时的回调。

收到 `GET_PLAY_STATUS` 响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `status` | 目标端（TG）返回的状态码，表示操作结果，类型为 `bt_avrcp_status_t`。通常对应 `BT_AVRCP_STATUS_*` 值，例如 `BT_AVRCP_STATUS_SUCCESS` 或 `BT_AVRCP_STATUS_INVALID_PARAMETER`。 |
| `buf` | 包含目标端（TG）返回的 `GET_PLAY_STATUS` 载荷的响应缓冲区，应用可以按照 `bt_avrcp_get_play_status_rsp` 定义的格式解析。如果 `status` 在 `BT_AVRCP_STATUS_INVALID_COMMAND` 到 `BT_AVRCP_STATUS_ADDRESSED_PLAYER_CHANGED` 范围内，且不等于 `BT_AVRCP_STATUS_OPERATION_COMPLETED`，则表示 AVRCP 响应码为 AV/C 拒绝响应（REJECTED），此时 `buf` 为 `NULL`。注意，所有多八位字节字段均采用大端格式（Big-endian）编码。 |

<a id="a02a9fa26f9827f327b6030758c539210"></a>

### `get_player_app_setting_attr_text`

```c
void(* bt_avrcp_ct_cb::get_player_app_setting_attr_text) (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status, struct net_buf *buf)
```

协议数据单元（PDU）ID 为 `GET_PLAYER_APP_SETTING_ATTR_TEXT` 时的回调。

收到 `GET_PLAYER_APP_SETTING_ATTR_TEXT` 响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `status` | 目标端（TG）返回的状态码，表示操作结果，类型为 `bt_avrcp_status_t`。通常对应 `BT_AVRCP_STATUS_*` 值，例如 `BT_AVRCP_STATUS_SUCCESS` 或 `BT_AVRCP_STATUS_INVALID_PARAMETER`。 |
| `buf` | 包含目标端（TG）返回的 `GET_PLAYER_APP_SETTING_ATTR_TEXT` 载荷的响应缓冲区，应用可以按照 `bt_avrcp_get_player_app_setting_attr_text_rsp` 定义的格式解析。如果 `status` 在 `BT_AVRCP_STATUS_INVALID_COMMAND` 到 `BT_AVRCP_STATUS_ADDRESSED_PLAYER_CHANGED` 范围内，且不等于 `BT_AVRCP_STATUS_OPERATION_COMPLETED`，则表示 AVRCP 响应码为 AV/C 拒绝响应（REJECTED），此时 `buf` 为 `NULL`。注意，所有多八位字节字段均采用大端格式（Big-endian）编码。 |

<a id="ac41f9cfa20c1b1a092515b345b468a10"></a>

### `get_player_app_setting_val_text`

```c
void(* bt_avrcp_ct_cb::get_player_app_setting_val_text) (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status, struct net_buf *buf)
```

协议数据单元（PDU）ID 为 `GET_PLAYER_APP_SETTING_VAL_TEXT` 时的回调。

收到 `GET_PLAYER_APP_SETTING_VAL_TEXT` 响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `status` | 目标端（TG）返回的状态码，表示操作结果，类型为 `bt_avrcp_status_t`。通常对应 `BT_AVRCP_STATUS_*` 值，例如 `BT_AVRCP_STATUS_SUCCESS` 或 `BT_AVRCP_STATUS_INVALID_PARAMETER`。 |
| `buf` | 包含目标端（TG）返回的 `GET_PLAYER_APP_SETTING_VAL_TEXT` 载荷的响应缓冲区，应用可以按照 `bt_avrcp_get_player_app_setting_val_text_rsp` 定义的格式解析。如果 `status` 在 `BT_AVRCP_STATUS_INVALID_COMMAND` 到 `BT_AVRCP_STATUS_ADDRESSED_PLAYER_CHANGED` 范围内，且不等于 `BT_AVRCP_STATUS_OPERATION_COMPLETED`，则表示 AVRCP 响应码为 AV/C 拒绝响应（REJECTED），此时 `buf` 为 `NULL`。注意，所有多八位字节字段均采用大端格式（Big-endian）编码。 |

<a id="a4b74108af0ab8cb0119af8c477ff9b33"></a>

### `get_total_number_of_items`

```c
void(* bt_avrcp_ct_cb::get_total_number_of_items) (struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

`bt_avrcp_ct_get_total_number_of_items()` 的回调函数。

获取条目总数（Get Total Number Of Items）过程完成时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 响应的事务标签（Transaction Label）。 |
| `buf` | 包含获取条目总数（Get Total Number Of Items）响应数据的缓冲区。操作成功时，应用可以按照 `bt_avrcp_get_total_number_of_items_rsp` 定义的格式解析载荷。如果 `status` 表示拒绝错误或操作未完成，则 `buf` 仅包含一个状态字节。注意，数据采用大端格式（Big-endian）编码。 |

<a id="a1b88debebdf19263d760f9f8e3d447d6"></a>

### `inform_batt_status_of_ct`

```c
void(* bt_avrcp_ct_cb::inform_batt_status_of_ct) (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status)
```

协议数据单元（PDU）ID 为 `INFORM_BATT_STATUS_OF_CT` 时的回调。

收到 `INFORM_BATT_STATUS_OF_CT` 响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `status` | 目标端（TG）返回的状态码，表示操作结果，类型为 `bt_avrcp_status_t`。通常对应 `BT_AVRCP_STATUS_*` 值，例如 `BT_AVRCP_STATUS_SUCCESS` 或 `BT_AVRCP_STATUS_INVALID_PARAMETER`。 |

<a id="a80f78ad02b0b7e9db9de19a0dceeea50"></a>

### `inform_displayable_char_set`

```c
void(* bt_avrcp_ct_cb::inform_displayable_char_set) (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status)
```

协议数据单元（PDU）ID 为 `INFORM_DISPLAYABLE_CHAR_SET` 时的回调。

收到 `INFORM_DISPLAYABLE_CHAR_SET` 响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `status` | 目标端（TG）返回的状态码，表示操作结果，类型为 `bt_avrcp_status_t`。通常对应 `BT_AVRCP_STATUS_*` 值，例如 `BT_AVRCP_STATUS_SUCCESS` 或 `BT_AVRCP_STATUS_INVALID_PARAMETER`。 |

<a id="a3c37bfd2f03a8c76a725b38210794e21"></a>

### `list_player_app_setting_attrs`

```c
void(* bt_avrcp_ct_cb::list_player_app_setting_attrs) (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status, struct net_buf *buf)
```

协议数据单元（PDU）ID 为 `LIST_PLAYER_APP_SETTING_ATTRS` 时的回调。

收到 `LIST_PLAYER_APP_SETTING_ATTRS` 响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `status` | 目标端（TG）返回的状态码，表示操作结果，类型为 `bt_avrcp_status_t`。通常对应 `BT_AVRCP_STATUS_*` 值，例如 `BT_AVRCP_STATUS_SUCCESS` 或 `BT_AVRCP_STATUS_INVALID_PARAMETER`。 |
| `buf` | 包含目标端（TG）返回的 `LIST_PLAYER_APP_SETTING_ATTRS` 载荷的响应缓冲区，应用可以按照 `bt_avrcp_list_player_app_setting_attrs_rsp` 定义的格式解析。如果 `status` 在 `BT_AVRCP_STATUS_INVALID_COMMAND` 到 `BT_AVRCP_STATUS_ADDRESSED_PLAYER_CHANGED` 范围内，且不等于 `BT_AVRCP_STATUS_OPERATION_COMPLETED`，则表示 AVRCP 响应码为 AV/C 拒绝响应（REJECTED），此时 `buf` 为 `NULL`。注意，所有多八位字节字段均采用大端格式（Big-endian）编码。 |

<a id="a8b16ac730eb5c9dc95e7c3e660f802cc"></a>

### `list_player_app_setting_vals`

```c
void(* bt_avrcp_ct_cb::list_player_app_setting_vals) (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status, struct net_buf *buf)
```

协议数据单元（PDU）ID 为 `LIST_PLAYER_APP_SETTING_VALS` 时的回调。

收到 `LIST_PLAYER_APP_SETTING_VALS` 响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `status` | 目标端（TG）返回的状态码，表示操作结果，类型为 `bt_avrcp_status_t`。通常对应 `BT_AVRCP_STATUS_*` 值，例如 `BT_AVRCP_STATUS_SUCCESS` 或 `BT_AVRCP_STATUS_INVALID_PARAMETER`。 |
| `buf` | 包含目标端（TG）返回的 `LIST_PLAYER_APP_SETTING_VALS` 载荷的响应缓冲区，应用可以按照 `bt_avrcp_list_player_app_setting_vals_rsp` 定义的格式解析。如果 `status` 在 `BT_AVRCP_STATUS_INVALID_COMMAND` 到 `BT_AVRCP_STATUS_ADDRESSED_PLAYER_CHANGED` 范围内，且不等于 `BT_AVRCP_STATUS_OPERATION_COMPLETED`，则表示 AVRCP 响应码为 AV/C 拒绝响应（REJECTED），此时 `buf` 为 `NULL`。注意，所有多八位字节字段均采用大端格式（Big-endian）编码。 |

<a id="a0c8b90004b116751f94b2c5c1af02af8"></a>

### `notification`

```c
void(* bt_avrcp_ct_cb::notification) (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status, uint8_t event_id, struct bt_avrcp_event_data *data)
```

事件通知响应（Event Notification Response）的控制端（CT）回调函数。

当 AVRCP 目标端（Target，TG）对先前注册的事件发送响应，即对注册通知（Register Notification）作出响应时调用。此回调报告事件类型、响应阶段（例如临时响应 Interim）以及事件专用的载荷。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（Controller，CT）连接上下文（Connection Context）。 |
| `tid` | 事务标签，用于将本次通知与原始注册通知（Register Notification）请求关联。 |
| `status` | 目标端状态／阶段码（`BT_AVRCP_STATUS_*`）。临时通知通常使用 `BT_AVRCP_STATUS_SUCCESS`；参数无效或事件不受支持时可能返回错误码。 |
| `event_id` | AVRCP 事件标识符。参见 `bt_avrcp_event_data`。它对应某个 AVRCP 事件类型，例如 `EVENT_PLAYBACK_STATUS_CHANGED`、`EVENT_TRACK_CHANGED` 等。 |
| `data` | 指向包含事件专用数据的 `bt_avrcp_event_data` 结构体的指针。联合体（Union）的内容取决于 `event_id`。 |

说明（Note）：此回调仅针对目标端（TG）的临时通知（Interim Notifications）和错误状态调用。对于状态变化（CHANGED）事件通知，必须先使用 `bt_avrcp_notify_changed_cb_t` 注册事件。

<a id="a69ab87eb920eae066034054e7bf89c7b"></a>

### `passthrough_rsp`

```c
void(* bt_avrcp_ct_cb::passthrough_rsp) (struct bt_avrcp_ct *ct, uint8_t tid, bt_avrcp_rsp_t result, const struct bt_avrcp_passthrough_rsp *rsp)
```

`bt_avrcp_passthrough()` 的回调函数。

收到透传（Pass Through）响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 响应的事务标签（Transaction Label）。 |
| `result` | 操作结果。 |
| `rsp` | 透传（PASS THROUGH）命令的响应。 |

<a id="a7ae520df749b156f9875cf3e6ee62a96"></a>

### `play_item`

```c
void(* bt_avrcp_ct_cb::play_item) (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status)
```

协议数据单元（PDU）ID 为 `PLAY_ITEM` 时的回调。

收到 `PLAY_ITEM` 响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `status` | 目标端（TG）返回的状态码，表示操作结果，类型为 `bt_avrcp_status_t`。通常对应 `BT_AVRCP_STATUS_*` 值，例如 `BT_AVRCP_STATUS_SUCCESS` 或 `BT_AVRCP_STATUS_INVALID_PARAMETER`。 |

<a id="a0e361f81921ae80e89947e1ede29b66c"></a>

### `search`

```c
void(* bt_avrcp_ct_cb::search) (struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

`bt_avrcp_ct_search()` 的回调函数。

搜索（Search）过程完成时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 响应的事务标签（Transaction Label）。 |
| `buf` | 包含搜索（Search）响应数据的缓冲区。操作成功时，应用可以按照 `bt_avrcp_search_rsp` 定义的格式解析载荷。如果 `status` 表示拒绝错误或操作未完成，则 `buf` 仅包含一个状态字节。注意，数据采用大端格式（Big-endian）编码。 |

<a id="ad102ac42003f1013b14809c4dd1057a4"></a>

### `set_absolute_volume`

```c
void(* bt_avrcp_ct_cb::set_absolute_volume) (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status, uint8_t absolute_volume)
```

设置绝对音量（Set Absolute Volume）响应的控制端（CT）回调函数。

从目标端（TG）收到设置绝对音量（Set Absolute Volume）响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 响应的事务标签（Transaction Label）。 |
| `status` | 目标端（TG）返回的状态码，表示操作结果，类型为 `bt_avrcp_status_t`。通常对应 `BT_AVRCP_STATUS_*` 值，例如 `BT_AVRCP_STATUS_SUCCESS` 或 `BT_AVRCP_STATUS_INVALID_PARAMETER`。 |
| `absolute_volume` | 绝对音量值，范围为 `0x00–0x7F`。 |

<a id="a6748f42e5ba39a1a6b2d7a50729c0316"></a>

### `set_addressed_player`

```c
void(* bt_avrcp_ct_cb::set_addressed_player) (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status)
```

协议数据单元（PDU）ID 为 `SET_ADDRESSED_PLAYER` 时的回调。

收到 `SET_ADDRESSED_PLAYER` 响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `status` | 目标端（TG）返回的状态码，表示操作结果，类型为 `bt_avrcp_status_t`。通常对应 `BT_AVRCP_STATUS_*` 值，例如 `BT_AVRCP_STATUS_SUCCESS` 或 `BT_AVRCP_STATUS_INVALID_PARAMETER`。 |

<a id="a768c099504dd24ee67556f69b493ddb0"></a>

### `set_browsed_player`

```c
void(* bt_avrcp_ct_cb::set_browsed_player) (struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf)
```

`bt_avrcp_ct_set_browsed_player()` 的回调函数。

设置浏览播放器（Set Browsed Player）过程完成时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 响应的事务标签（Transaction Label）。 |
| `buf` | 包含设置浏览播放器（set browsed player）响应数据的缓冲区。操作成功时，应用可以按照 `bt_avrcp_set_browsed_player_rsp` 定义的格式解析载荷。如果 `status` 表示拒绝错误或操作未完成，则 `buf` 仅包含一个状态字节。注意，数据采用大端格式（Big-endian）编码。 |

<a id="a5990204dc0d6b0437308e69eef8f7f47"></a>

### `set_player_app_setting_val`

```c
void(* bt_avrcp_ct_cb::set_player_app_setting_val) (struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status)
```

协议数据单元（PDU）ID 为 `SET_PLAYER_APP_SETTING_VAL` 时的回调。

收到 `SET_PLAYER_APP_SETTING_VAL` 响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 请求的事务标签（Transaction Label）。 |
| `status` | 目标端（TG）返回的状态码，表示操作结果，类型为 `bt_avrcp_status_t`。通常对应 `BT_AVRCP_STATUS_*` 值，例如 `BT_AVRCP_STATUS_SUCCESS` 或 `BT_AVRCP_STATUS_INVALID_PARAMETER`。 |

<a id="a4e33bc54f28204959ccd4fa2c766980d"></a>

### `subunit_info_rsp`

```c
void(* bt_avrcp_ct_cb::subunit_info_rsp) (struct bt_avrcp_ct *ct, uint8_t tid, struct bt_avrcp_subunit_info_rsp *rsp)
```

`bt_avrcp_get_subunit_info()` 的回调函数。

获取子单元信息（Get Subunit Info）过程完成时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 响应的事务标签（Transaction Label）。 |
| `rsp` | 子单元信息（SUBUNIT INFO）命令的响应。 |

<a id="ac842ad673b8a943e9f1b188346b8d92d"></a>

### `unit_info_rsp`

```c
void(* bt_avrcp_ct_cb::unit_info_rsp) (struct bt_avrcp_ct *ct, uint8_t tid, struct bt_avrcp_unit_info_rsp *rsp)
```

`bt_avrcp_get_unit_info()` 的回调函数。

获取单元信息（Get Unit Info）过程完成时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端（CT）连接对象。 |
| `tid` | 响应的事务标签（Transaction Label）。 |
| `rsp` | 单元信息（UNIT INFO）命令的响应。 |

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 27.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)
- [bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)
- [bt_avrcp_unit_info_rsp](P072_bt_avrcp_unit_info_rsp_结构体.md)
- [bt_avrcp_subunit_info_rsp](P069_bt_avrcp_subunit_info_rsp_结构体.md)
- [bt_avrcp_rsp_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaba2d8faec2c3baf7403199ea8a509326)
- [bt_avrcp_passthrough_rsp](P058_bt_avrcp_passthrough_rsp_结构体.md)
- [bt_avrcp_ct_set_browsed_player()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab0886ea325dddc67167bed86ec6c31e9)
- [bt_avrcp_ct_get_folder_items()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gad77454a6d56942ffe57d5b716f7aa39d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_avrcp_ct_change_path()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab8730a40ab9bc208a53a035243b8cb1b)
- [bt_avrcp_ct_get_item_attrs()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga4ae38864d35a66a306ced13544e442d4)
- [bt_avrcp_ct_get_total_number_of_items()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gadef2624ec50c0bb138d7eae8525784c5)
- [bt_avrcp_ct_search()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab8b765fab76ba2585730f328c0abc167)
- [bt_avrcp_event_data](P028_bt_avrcp_event_data_结构体.md)
- [bt_avrcp_status_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga52368f4cc655bab75f96da80ddaaabe0)
- [bt_avrcp_get_caps_rsp](P031_bt_avrcp_get_caps_rsp_结构体.md)
- [bt_avrcp_get_curr_player_app_setting_val_rsp](P033_bt_avrcp_get_curr_player_app_setting_val_rsp_结构体.md)
- [bt_avrcp_get_element_attrs_rsp](P035_bt_avrcp_get_element_attrs_rsp_结构体.md)
- [bt_avrcp_get_folder_items_rsp](P037_bt_avrcp_get_folder_items_rsp_结构体.md)
- [bt_avrcp_get_item_attrs_rsp](P039_bt_avrcp_get_item_attrs_rsp_结构体.md)
- [bt_avrcp_get_play_status_rsp](P040_bt_avrcp_get_play_status_rsp_结构体.md)
- [bt_avrcp_get_player_app_setting_attr_text_rsp](P042_bt_avrcp_get_player_app_setting_attr_text_rsp_结构体.md)
- [bt_avrcp_get_player_app_setting_val_text_rsp](P044_bt_avrcp_get_player_app_setting_val_text_rsp_结构体.md)
- [bt_avrcp_get_total_number_of_items_rsp](P046_bt_avrcp_get_total_number_of_items_rsp_结构体.md)
- [bt_avrcp_list_player_app_setting_attrs_rsp](P050_bt_avrcp_list_player_app_setting_attrs_rsp_结构体.md)
- [bt_avrcp_list_player_app_setting_vals_rsp](P052_bt_avrcp_list_player_app_setting_vals_rsp_结构体.md)
- [bt_avrcp_notify_changed_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab9bd888ef5443bd0a3d34a34b972f409)
- [bt_avrcp_search_rsp](P063_bt_avrcp_search_rsp_结构体.md)
- [bt_avrcp_set_browsed_player_rsp](P067_bt_avrcp_set_browsed_player_rsp_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P026_bt_avrcp_ct_结构体.md) · [返回大纲](大纲.md) · [下一章](P028_bt_avrcp_event_data_结构体.md)
