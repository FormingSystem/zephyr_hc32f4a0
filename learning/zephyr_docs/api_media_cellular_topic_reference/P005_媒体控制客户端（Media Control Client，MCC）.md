---
id: learning.zephyr-docs.api-media-cellular-topic-reference.page-5
title: 媒体控制客户端（Media Control Client，MCC）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_媒体控制客户端（Media Control Client，MCC）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙媒体控制客户端（Media Control Client，MCC）接口。

<a id="details"></a>

蓝牙媒体控制客户端接口（Bluetooth Media Control Client Interface，MCC）。已更新至《媒体控制配置文件》（Media Control Profile）规范修订版 1.0。自 3.0 引入，版本 0.8.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

<a id="r_bt_5Fmcc_5Fcb"></a>

```c
struct bt_mcc_cb
```

相关声明：[bt_mcc_cb](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md)。

媒体控制客户端（Media Control Client）的回调。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 5.2\_类型定义（Typedefs）

<a id="r_gab268faeca207e115ee1be0843ab8c342"></a>

```c
typedef void(* bt_mcc_discover_mcs_cb) (struct bt_conn *conn, int err)
```

相关声明：[bt_mcc_discover_mcs_cb](#gab268faeca207e115ee1be0843ab8c342)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

用于 `bt_mcc_discover_mcs()` 的回调函数（Callback Function）。

<a id="r_gaa943b61848ee43e91d473f6fdd0a604f"></a>

```c
typedef void(* bt_mcc_read_player_name_cb) (struct bt_conn *conn, int err, const char *name)
```

相关声明：[bt_mcc_read_player_name_cb](#gaa943b61848ee43e91d473f6fdd0a604f)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

用于 `bt_mcc_read_player_name()` 的回调函数（Callback Function）。

<a id="r_ga471d0491b70e5472e16c3035507761cc"></a>

```c
typedef void(* bt_mcc_read_icon_obj_id_cb) (struct bt_conn *conn, int err, uint64_t icon_id)
```

相关声明：[bt_mcc_read_icon_obj_id_cb](#ga471d0491b70e5472e16c3035507761cc)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

用于 `bt_mcc_read_icon_obj_id()` 的回调函数（Callback Function）。

<a id="r_gaaddc4abe38f6ca811967ae6a10d8f8f0"></a>

```c
typedef void(* bt_mcc_read_icon_url_cb) (struct bt_conn *conn, int err, const char *icon_url)
```

相关声明：[bt_mcc_read_icon_url_cb](#gaaddc4abe38f6ca811967ae6a10d8f8f0)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

用于 `bt_mcc_read_icon_url()` 的回调函数（Callback Function）。

<a id="r_ga67611a3068284b0c7fbb3ef07dfe7688"></a>

```c
typedef void(* bt_mcc_track_changed_ntf_cb) (struct bt_conn *conn, int err)
```

相关声明：[bt_mcc_track_changed_ntf_cb](#ga67611a3068284b0c7fbb3ef07dfe7688)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

音轨变化通知（Track Changed Notification）的回调函数（Callback Function）。

<a id="r_ga6927860f1803aeade4994610da32d402"></a>

```c
typedef void(* bt_mcc_read_track_title_cb) (struct bt_conn *conn, int err, const char *title)
```

相关声明：[bt_mcc_read_track_title_cb](#ga6927860f1803aeade4994610da32d402)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

用于 `bt_mcc_read_track_title()` 的回调函数（Callback Function）。

<a id="r_ga7cdb524ff9c34f24c1740adb9eca072c"></a>

```c
typedef void(* bt_mcc_read_track_duration_cb) (struct bt_conn *conn, int err, int32_t dur)
```

相关声明：[bt_mcc_read_track_duration_cb](#ga7cdb524ff9c34f24c1740adb9eca072c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

用于 `bt_mcc_read_track_duration()` 的回调函数（Callback Function）。

<a id="r_ga128883c867b10e57d3f2f26a708b7263"></a>

```c
typedef void(* bt_mcc_read_track_position_cb) (struct bt_conn *conn, int err, int32_t pos)
```

相关声明：[bt_mcc_read_track_position_cb](#ga128883c867b10e57d3f2f26a708b7263)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

用于 `bt_mcc_read_track_position()` 的回调函数（Callback Function）。

<a id="r_ga1167f5e2ef4a7e78469aefc0cef18bff"></a>

```c
typedef void(* bt_mcc_set_track_position_cb) (struct bt_conn *conn, int err, int32_t pos)
```

相关声明：[bt_mcc_set_track_position_cb](#ga1167f5e2ef4a7e78469aefc0cef18bff)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

用于 `bt_mcc_set_track_position()` 的回调函数（Callback Function）。

<a id="r_ga6f5383be3f344c25361786d903640909"></a>

```c
typedef void(* bt_mcc_read_playback_speed_cb) (struct bt_conn *conn, int err, int8_t speed)
```

相关声明：[bt_mcc_read_playback_speed_cb](#ga6f5383be3f344c25361786d903640909)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

用于 `bt_mcc_read_playback_speed()` 的回调函数（Callback Function）。

<a id="r_ga1322f2ddbb587c70fd23a7ccfc1fc779"></a>

```c
typedef void(* bt_mcc_set_playback_speed_cb) (struct bt_conn *conn, int err, int8_t speed)
```

相关声明：[bt_mcc_set_playback_speed_cb](#ga1322f2ddbb587c70fd23a7ccfc1fc779)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

用于 `bt_mcc_set_playback_speed()` 的回调函数（Callback Function）。

<a id="r_ga3089e6165e8491325f7205279bb5bb83"></a>

```c
typedef void(* bt_mcc_read_seeking_speed_cb) (struct bt_conn *conn, int err, int8_t speed)
```

相关声明：[bt_mcc_read_seeking_speed_cb](#ga3089e6165e8491325f7205279bb5bb83)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

用于 `bt_mcc_read_seeking_speed()` 的回调函数（Callback Function）。

<a id="r_ga1fbf0b4fd624626127774d2662083875"></a>

```c
typedef void(* bt_mcc_read_segments_obj_id_cb) (struct bt_conn *conn, int err, uint64_t id)
```

相关声明：[bt_mcc_read_segments_obj_id_cb](#ga1fbf0b4fd624626127774d2662083875)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

用于 `bt_mcc_read_segments_obj_id()` 的回调函数（Callback Function）。

<a id="r_ga28ac116604248643b0b203b4a314b7b1"></a>

```c
typedef void(* bt_mcc_read_current_track_obj_id_cb) (struct bt_conn *conn, int err, uint64_t id)
```

相关声明：[bt_mcc_read_current_track_obj_id_cb](#ga28ac116604248643b0b203b4a314b7b1)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

用于 `bt_mcc_read_current_track_obj_id()` 的回调函数（Callback Function）。

<a id="r_gaf0d619b493a8fb4c00278a0a85bb2529"></a>

```c
typedef void(* bt_mcc_set_current_track_obj_id_cb) (struct bt_conn *conn, int err, uint64_t id)
```

相关声明：[bt_mcc_set_current_track_obj_id_cb](#gaf0d619b493a8fb4c00278a0a85bb2529)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

用于 `bt_mcc_set_current_track_obj_id()` 的回调函数（Callback Function）。

<a id="r_ga83d6614d4a0808782b1b4df115b872d2"></a>

```c
typedef void(* bt_mcc_read_next_track_obj_id_cb) (struct bt_conn *conn, int err, uint64_t id)
```

相关声明：[bt_mcc_read_next_track_obj_id_cb](#ga83d6614d4a0808782b1b4df115b872d2)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

用于 `bt_mcc_read_next_track_obj_id()` 的回调函数（Callback Function）。

<a id="r_ga2f3099d097b28ab9c4abf81e19474def"></a>

```c
typedef void(* bt_mcc_set_next_track_obj_id_cb) (struct bt_conn *conn, int err, uint64_t id)
```

相关声明：[bt_mcc_set_next_track_obj_id_cb](#ga2f3099d097b28ab9c4abf81e19474def)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

用于 `bt_mcc_set_next_track_obj_id()` 的回调函数（Callback Function）。

<a id="r_ga48dd365aa637336b9899db4b6986a5e4"></a>

```c
typedef void(* bt_mcc_read_parent_group_obj_id_cb) (struct bt_conn *conn, int err, uint64_t id)
```

相关声明：[bt_mcc_read_parent_group_obj_id_cb](#ga48dd365aa637336b9899db4b6986a5e4)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

用于 `bt_mcc_read_parent_group_obj_id()` 的回调函数（Callback Function）。

<a id="r_ga5f21a1eed4bfe4dfbca40949af895723"></a>

```c
typedef void(* bt_mcc_read_current_group_obj_id_cb) (struct bt_conn *conn, int err, uint64_t id)
```

相关声明：[bt_mcc_read_current_group_obj_id_cb](#ga5f21a1eed4bfe4dfbca40949af895723)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

用于 `bt_mcc_read_current_group_obj_id()` 的回调函数（Callback Function）。

<a id="r_ga8bbb0d28f7dcf23a30a8ca56d647ac2c"></a>

```c
typedef void(* bt_mcc_set_current_group_obj_id_cb) (struct bt_conn *conn, int err, uint64_t obj_id)
```

相关声明：[bt_mcc_set_current_group_obj_id_cb](#ga8bbb0d28f7dcf23a30a8ca56d647ac2c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

用于 `bt_mcc_set_current_group_obj_id()` 的回调函数（Callback Function）。

<a id="r_gafb0869e0ef5332d39070081efdacf17c"></a>

```c
typedef void(* bt_mcc_read_playing_order_cb) (struct bt_conn *conn, int err, uint8_t order)
```

相关声明：[bt_mcc_read_playing_order_cb](#gafb0869e0ef5332d39070081efdacf17c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

用于 `bt_mcc_read_playing_order()` 的回调函数（Callback Function）。

<a id="r_ga1a12fb89adf29c83bca02f701213c6d7"></a>

```c
typedef void(* bt_mcc_set_playing_order_cb) (struct bt_conn *conn, int err, uint8_t order)
```

相关声明：[bt_mcc_set_playing_order_cb](#ga1a12fb89adf29c83bca02f701213c6d7)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

用于 `bt_mcc_set_playing_order()` 的回调函数（Callback Function）。

<a id="r_gac45a2aff295535f70ac4a070e970b7a0"></a>

```c
typedef void(* bt_mcc_read_playing_orders_supported_cb) (struct bt_conn *conn, int err, uint16_t orders)
```

相关声明：[bt_mcc_read_playing_orders_supported_cb](#gac45a2aff295535f70ac4a070e970b7a0)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

用于 `bt_mcc_read_playing_orders_supported()` 的回调函数（Callback Function）。

<a id="r_ga200a827f4bf5d65570ddabd028269f77"></a>

```c
typedef void(* bt_mcc_read_media_state_cb) (struct bt_conn *conn, int err, uint8_t state)
```

相关声明：[bt_mcc_read_media_state_cb](#ga200a827f4bf5d65570ddabd028269f77)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

用于 `bt_mcc_read_media_state()` 的回调函数（Callback Function）。

<a id="r_gae4c2d1a5c41df1c3535418cc23d48f8e"></a>

```c
typedef void(* bt_mcc_send_cmd_cb) (struct bt_conn *conn, int err, const struct mpl_cmd *cmd)
```

相关声明：[bt_mcc_send_cmd_cb](#gae4c2d1a5c41df1c3535418cc23d48f8e)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[mpl_cmd](../audio_video_model_reference/P037_mpl_cmd_结构体.md)、[cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)。

用于 `bt_mcc_send_cmd()` 的回调函数（Callback Function）。

<a id="r_ga50da90a5c351c99494208b44096a61c8"></a>

```c
typedef void(* bt_mcc_cmd_ntf_cb) (struct bt_conn *conn, int err, const struct mpl_cmd_ntf *ntf)
```

相关声明：[bt_mcc_cmd_ntf_cb](#ga50da90a5c351c99494208b44096a61c8)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[mpl_cmd_ntf](../audio_video_model_reference/P038_mpl_cmd_ntf_结构体.md)。

命令通知（Command Notification）的回调函数（Callback Function）。

<a id="r_gab37df36e15132b9235d1093f5aa403cc"></a>

```c
typedef void(* bt_mcc_read_opcodes_supported_cb) (struct bt_conn *conn, int err, uint32_t opcodes)
```

相关声明：[bt_mcc_read_opcodes_supported_cb](#gab37df36e15132b9235d1093f5aa403cc)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

用于 `bt_mcc_read_opcodes_supported()` 的回调函数（Callback Function）。

<a id="r_ga9489c34b6006df8bd26e626030cab71f"></a>

```c
typedef void(* bt_mcc_send_search_cb) (struct bt_conn *conn, int err, const struct mpl_search *search)
```

相关声明：[bt_mcc_send_search_cb](#ga9489c34b6006df8bd26e626030cab71f)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[mpl_search](../audio_video_model_reference/P040_mpl_search_结构体.md)。

用于 `bt_mcc_send_search()` 的回调函数（Callback Function）。

<a id="r_gab168a4c86de444dd066802c4a5fe41c3"></a>

```c
typedef void(* bt_mcc_search_ntf_cb) (struct bt_conn *conn, int err, uint8_t result_code)
```

相关声明：[bt_mcc_search_ntf_cb](#gab168a4c86de444dd066802c4a5fe41c3)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

搜索通知（Search Notification）的回调函数（Callback Function）。

<a id="r_ga5a39822a21a6f2aa7a6548c57979a926"></a>

```c
typedef void(* bt_mcc_read_search_results_obj_id_cb) (struct bt_conn *conn, int err, uint64_t id)
```

相关声明：[bt_mcc_read_search_results_obj_id_cb](#ga5a39822a21a6f2aa7a6548c57979a926)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

用于 `bt_mcc_read_search_results_obj_id()` 的回调函数（Callback Function）。

<a id="r_gadb607997fdcb3e57bbfc90790de4b927"></a>

```c
typedef void(* bt_mcc_read_content_control_id_cb) (struct bt_conn *conn, int err, uint8_t ccid)
```

相关声明：[bt_mcc_read_content_control_id_cb](#gadb607997fdcb3e57bbfc90790de4b927)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

用于 `bt_mcc_read_content_control_id()` 的回调函数（Callback Function）。

<a id="r_gaf186e6adefa296de4146502665d738b3"></a>

```c
typedef void(* bt_mcc_otc_obj_selected_cb) (struct bt_conn *conn, int err)
```

相关声明：[bt_mcc_otc_obj_selected_cb](#gaf186e6adefa296de4146502665d738b3)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

对象被选中（Object Selected）时的回调函数（Callback Function）。

<a id="r_ga9805222315ca6e6df0720233055af10c"></a>

```c
typedef void(* bt_mcc_otc_obj_metadata_cb) (struct bt_conn *conn, int err)
```

相关声明：[bt_mcc_otc_obj_metadata_cb](#ga9805222315ca6e6df0720233055af10c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

用于 `bt_mcc_otc_read_object_metadata()` 的回调函数（Callback Function）。

<a id="r_ga13bedbb573bc5575ab75fc3ae65c1870"></a>

```c
typedef void(* bt_mcc_otc_read_icon_object_cb) (struct bt_conn *conn, int err, struct net_buf_simple *buf)
```

相关声明：[bt_mcc_otc_read_icon_object_cb](#ga13bedbb573bc5575ab75fc3ae65c1870)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

用于 `bt_mcc_otc_read_icon_object()` 的回调函数（Callback Function）。

<a id="r_ga1c4c842879cd8b209080a59d3ba125f8"></a>

```c
typedef void(* bt_mcc_otc_read_track_segments_object_cb) (struct bt_conn *conn, int err, struct net_buf_simple *buf)
```

相关声明：[bt_mcc_otc_read_track_segments_object_cb](#ga1c4c842879cd8b209080a59d3ba125f8)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

用于 `bt_mcc_otc_read_track_segments_object()` 的回调函数（Callback Function）。

<a id="r_gaff887eda3b84cad1052549f23c8dcfbe"></a>

```c
typedef void(* bt_mcc_otc_read_current_track_object_cb) (struct bt_conn *conn, int err, struct net_buf_simple *buf)
```

相关声明：[bt_mcc_otc_read_current_track_object_cb](#gaff887eda3b84cad1052549f23c8dcfbe)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

用于 `bt_mcc_otc_read_current_track_object()` 的回调函数（Callback Function）。

<a id="r_ga920f25e04e1be4ad5f7e220c2e9102b5"></a>

```c
typedef void(* bt_mcc_otc_read_next_track_object_cb) (struct bt_conn *conn, int err, struct net_buf_simple *buf)
```

相关声明：[bt_mcc_otc_read_next_track_object_cb](#ga920f25e04e1be4ad5f7e220c2e9102b5)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

用于 `bt_mcc_otc_read_next_track_object()` 的回调函数（Callback Function）。

<a id="r_gaca904bacb552792ffd85c6a640f0ba48"></a>

```c
typedef void(* bt_mcc_otc_read_parent_group_object_cb) (struct bt_conn *conn, int err, struct net_buf_simple *buf)
```

相关声明：[bt_mcc_otc_read_parent_group_object_cb](#gaca904bacb552792ffd85c6a640f0ba48)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

用于 `bt_mcc_otc_read_parent_group_object()` 的回调函数（Callback Function）。

<a id="r_ga0b309ae7ce23834f303c39017ffa4e50"></a>

```c
typedef void(* bt_mcc_otc_read_current_group_object_cb) (struct bt_conn *conn, int err, struct net_buf_simple *buf)
```

相关声明：[bt_mcc_otc_read_current_group_object_cb](#ga0b309ae7ce23834f303c39017ffa4e50)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

用于 `bt_mcc_otc_read_current_group_object()` 的回调函数（Callback Function）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.3\_函数（Functions）

<a id="r_ga94de08bb0a1e1324600e4957b648e92b"></a>

```c
int bt_mcc_init (struct bt_mcc_cb *cb)
```

相关声明：[bt_mcc_init](#ga94de08bb0a1e1324600e4957b648e92b)、[bt_mcc_cb](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md)。

初始化媒体控制客户端（Media Control Client）。

<a id="r_gaa1f9ead03b4cccaff1e3390b8052b0f3"></a>

```c
int bt_mcc_discover_mcs (struct bt_conn *conn, bool subscribe)
```

相关声明：[bt_mcc_discover_mcs](#gaa1f9ead03b4cccaff1e3390b8052b0f3)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

发现媒体控制服务（Media Control Service）。

<a id="r_ga724ce71fc88f1ca4bcf209c92c177f36"></a>

```c
int bt_mcc_read_player_name (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_player_name](#ga724ce71fc88f1ca4bcf209c92c177f36)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取媒体播放器名称（Media Player Name）。

<a id="r_ga0e69de33c37957a2b5473df7d3c3f389"></a>

```c
int bt_mcc_read_icon_obj_id (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_icon_obj_id](#ga0e69de33c37957a2b5473df7d3c3f389)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取图标对象 ID（Icon Object ID）。

<a id="r_ga38733456db6bc6558a511e104577c9c9"></a>

```c
int bt_mcc_read_icon_url (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_icon_url](#ga38733456db6bc6558a511e104577c9c9)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取图标对象 URL（Icon Object URL）。

<a id="r_ga7dfa14489a4cea4b00053c9aa75cf373"></a>

```c
int bt_mcc_read_track_title (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_track_title](#ga7dfa14489a4cea4b00053c9aa75cf373)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取曲目标题（Track Title）。

<a id="r_ga50a45f043bd2ae1741a120e02e9dc2f5"></a>

```c
int bt_mcc_read_track_duration (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_track_duration](#ga50a45f043bd2ae1741a120e02e9dc2f5)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取曲目时长（Track Duration）。

<a id="r_gaf143098f5dfcfba01df3d6f06472779e"></a>

```c
int bt_mcc_read_track_position (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_track_position](#gaf143098f5dfcfba01df3d6f06472779e)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取曲目位置（Track Position）。

<a id="r_gad324366d33bef6b1ed1c8fc881bf44cf"></a>

```c
int bt_mcc_set_track_position (struct bt_conn *conn, int32_t pos)
```

相关声明：[bt_mcc_set_track_position](#gad324366d33bef6b1ed1c8fc881bf44cf)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置音轨位置（Track Position）。

<a id="r_gaa566a4c42f0ab0ab6feddf4e25845609"></a>

```c
int bt_mcc_read_playback_speed (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_playback_speed](#gaa566a4c42f0ab0ab6feddf4e25845609)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取播放速度（Playback Speed）。

<a id="r_ga1382e5b6000896dc94f6489909301719"></a>

```c
int bt_mcc_set_playback_speed (struct bt_conn *conn, int8_t speed)
```

相关声明：[bt_mcc_set_playback_speed](#ga1382e5b6000896dc94f6489909301719)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

设置播放速度。

<a id="r_ga366fdfaa23cef9f1c3ba7ddd36a67658"></a>

```c
int bt_mcc_read_seeking_speed (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_seeking_speed](#ga366fdfaa23cef9f1c3ba7ddd36a67658)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取搜索速度（Seeking Speed）。

<a id="r_ga4cb0a95e91d3ec00ede64663a2b932f0"></a>

```c
int bt_mcc_read_segments_obj_id (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_segments_obj_id](#ga4cb0a95e91d3ec00ede64663a2b932f0)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取音轨分段对象标识符（Track Segments Object ID）。

<a id="r_ga5b3a8fb8e8251cf005b34e47619ae7b9"></a>

```c
int bt_mcc_read_current_track_obj_id (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_current_track_obj_id](#ga5b3a8fb8e8251cf005b34e47619ae7b9)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取当前曲目对象 ID（Current Track Object ID）。

<a id="r_ga8374ac230c5fe6b5a1bb7fa873fdeb49"></a>

```c
int bt_mcc_set_current_track_obj_id (struct bt_conn *conn, uint64_t id)
```

相关声明：[bt_mcc_set_current_track_obj_id](#ga8374ac230c5fe6b5a1bb7fa873fdeb49)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

设置当前曲目对象 ID。

<a id="r_ga11e4c02ba0b1fbc197aaf071b82a1eed"></a>

```c
int bt_mcc_read_next_track_obj_id (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_next_track_obj_id](#ga11e4c02ba0b1fbc197aaf071b82a1eed)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取下一曲目对象 ID（Next Track Object ID）。

<a id="r_gafeebcbb0c77d5d4acbe151fd9888d084"></a>

```c
int bt_mcc_set_next_track_obj_id (struct bt_conn *conn, uint64_t id)
```

相关声明：[bt_mcc_set_next_track_obj_id](#gafeebcbb0c77d5d4acbe151fd9888d084)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

设置下一曲目对象 ID。

<a id="r_ga8cb43a6947df48113b082d8cc8ccf25c"></a>

```c
int bt_mcc_read_current_group_obj_id (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_current_group_obj_id](#ga8cb43a6947df48113b082d8cc8ccf25c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取当前分组对象 ID（Current Group Object ID）。

<a id="r_gae3f385811f852d584595c6e531556aed"></a>

```c
int bt_mcc_set_current_group_obj_id (struct bt_conn *conn, uint64_t id)
```

相关声明：[bt_mcc_set_current_group_obj_id](#gae3f385811f852d584595c6e531556aed)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

设置当前分组对象 ID。

<a id="r_ga3ccd5961cc4c8d82fa988d300e12e1ae"></a>

```c
int bt_mcc_read_parent_group_obj_id (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_parent_group_obj_id](#ga3ccd5961cc4c8d82fa988d300e12e1ae)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取父分组对象 ID（Parent Group Object ID）。

<a id="r_ga077a134ff1404fb76aa756a5531fd1d7"></a>

```c
int bt_mcc_read_playing_order (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_playing_order](#ga077a134ff1404fb76aa756a5531fd1d7)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取播放顺序（Playing Order）。

<a id="r_ga05295649385c3a337401765627d09553"></a>

```c
int bt_mcc_set_playing_order (struct bt_conn *conn, uint8_t order)
```

相关声明：[bt_mcc_set_playing_order](#ga05295649385c3a337401765627d09553)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置播放顺序。

<a id="r_gaf61f6fcf3f96ccb6f5a72ffaad27dec4"></a>

```c
int bt_mcc_read_playing_orders_supported (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_playing_orders_supported](#gaf61f6fcf3f96ccb6f5a72ffaad27dec4)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取支持的播放顺序（Playing Orders Supported）。

<a id="r_gac1b440cfa54dd4b6e23bb47bf885f88d"></a>

```c
int bt_mcc_read_media_state (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_media_state](#gac1b440cfa54dd4b6e23bb47bf885f88d)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取媒体状态（Media State）。

<a id="r_ga3f4a538bcf436e4e80b73ed6e077dfa0"></a>

```c
int bt_mcc_send_cmd (struct bt_conn *conn, const struct mpl_cmd *cmd)
```

相关声明：[bt_mcc_send_cmd](#ga3f4a538bcf436e4e80b73ed6e077dfa0)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[mpl_cmd](../audio_video_model_reference/P037_mpl_cmd_结构体.md)、[cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)。

发送命令（Command）。

<a id="r_ga692160554947f92e8c81912c5e597086"></a>

```c
int bt_mcc_read_opcodes_supported (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_opcodes_supported](#ga692160554947f92e8c81912c5e597086)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取受支持的操作码（Opcodes Supported）。

<a id="r_ga324161056e03195820bbd7cc77ff287d"></a>

```c
int bt_mcc_send_search (struct bt_conn *conn, const struct mpl_search *search)
```

相关声明：[bt_mcc_send_search](#ga324161056e03195820bbd7cc77ff287d)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[mpl_search](../audio_video_model_reference/P040_mpl_search_结构体.md)。

发送搜索命令（Search Command）。

<a id="r_ga98814a516a027bdaa3250e93d55309fd"></a>

```c
int bt_mcc_read_search_results_obj_id (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_search_results_obj_id](#ga98814a516a027bdaa3250e93d55309fd)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

搜索结果组对象标识符（Search Results Group Object ID）。

<a id="r_ga77cbf810c35d1a17efce1fae6a941963"></a>

```c
int bt_mcc_read_content_control_id (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_content_control_id](#ga77cbf810c35d1a17efce1fae6a941963)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取内容控制 ID（Content Control ID）。

<a id="r_gadf687cb26a6d00bca73e273da583df88"></a>

```c
int bt_mcc_otc_read_object_metadata (struct bt_conn *conn)
```

相关声明：[bt_mcc_otc_read_object_metadata](#gadf687cb26a6d00bca73e273da583df88)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取当前对象元数据（Current Object Metadata）。

<a id="r_gaba527d8f0307ab11150a5434231c0e7e"></a>

```c
int bt_mcc_otc_read_icon_object (struct bt_conn *conn)
```

相关声明：[bt_mcc_otc_read_icon_object](#gaba527d8f0307ab11150a5434231c0e7e)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取图标对象（Icon Object）。

<a id="r_gac22e840b65895aa018ab1b4535a87672"></a>

```c
int bt_mcc_otc_read_track_segments_object (struct bt_conn *conn)
```

相关声明：[bt_mcc_otc_read_track_segments_object](#gac22e840b65895aa018ab1b4535a87672)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取音轨分段对象（Track Segments Object）。

<a id="r_gac4b09a77df52d2681e7652591ca32bf8"></a>

```c
int bt_mcc_otc_read_current_track_object (struct bt_conn *conn)
```

相关声明：[bt_mcc_otc_read_current_track_object](#gac4b09a77df52d2681e7652591ca32bf8)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取当前音轨对象（Current Track Object）。

<a id="r_ga611c9edebff5b4347ad1241ffd19f49e"></a>

```c
int bt_mcc_otc_read_next_track_object (struct bt_conn *conn)
```

相关声明：[bt_mcc_otc_read_next_track_object](#ga611c9edebff5b4347ad1241ffd19f49e)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取下一音轨对象（Next Track Object）。

<a id="r_ga4b1ebe682ad134795f8a1b494244f8b6"></a>

```c
int bt_mcc_otc_read_current_group_object (struct bt_conn *conn)
```

相关声明：[bt_mcc_otc_read_current_group_object](#ga4b1ebe682ad134795f8a1b494244f8b6)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取当前组对象（Current Group Object）。

<a id="r_gae001cb2d701457ce083aa8a0fd5ec518"></a>

```c
int bt_mcc_otc_read_parent_group_object (struct bt_conn *conn)
```

相关声明：[bt_mcc_otc_read_parent_group_object](#gae001cb2d701457ce083aa8a0fd5ec518)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取父组对象（Parent Group Object）。

<a id="r_gaa243806f65c4a37d41f25bcc4f1839fc"></a>

```c
struct bt_ots_client * bt_mcc_otc_inst (struct bt_conn *conn)
```

相关声明：[bt_ots_client](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md)、[bt_mcc_otc_inst](#gaa243806f65c4a37d41f25bcc4f1839fc)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

查找媒体控制客户端对象传输客户端实例（MCC OTC Instance）。

## 5.4\_详细说明（Detailed Documentation）

<a id="ga50da90a5c351c99494208b44096a61c8"></a>

### `bt_mcc_cmd_ntf_cb`

```c
typedef void(* bt_mcc_cmd_ntf_cb) (struct bt_conn *conn, int err, const struct mpl_cmd_ntf *ntf)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

命令通知（Command Notification）的回调函数（Callback Function）。

在媒体控制点（media control point）收到通知时调用。

命令通知（Command Notifications），即对媒体控制点写入操作的通知，使用的参数结构与发送命令、即写入媒体控制点时所用结构不同。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `ntf` | 命令通知（Command Notification）。 |

<a id="gab268faeca207e115ee1be0843ab8c342"></a>

### `bt_mcc_discover_mcs_cb`

```c
typedef void(* bt_mcc_discover_mcs_cb) (struct bt_conn *conn, int err)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_discover_mcs()` 的回调函数（Callback Function）。

发现媒体控制服务器（Media Control Server）时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |

<a id="ga9805222315ca6e6df0720233055af10c"></a>

### `bt_mcc_otc_obj_metadata_cb`

```c
typedef void(* bt_mcc_otc_obj_metadata_cb) (struct bt_conn *conn, int err)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_otc_read_object_metadata()` 的回调函数（Callback Function）。

读取对象元数据（Object Metadata）时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |

<a id="gaf186e6adefa296de4146502665d738b3"></a>

### `bt_mcc_otc_obj_selected_cb`

```c
typedef void(* bt_mcc_otc_obj_selected_cb) (struct bt_conn *conn, int err)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

对象被选中（Object Selected）时的回调函数（Callback Function）。

选中对象（Object）时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |

<a id="ga0b309ae7ce23834f303c39017ffa4e50"></a>

### `bt_mcc_otc_read_current_group_object_cb`

```c
typedef void(* bt_mcc_otc_read_current_group_object_cb) (struct bt_conn *conn, int err, struct net_buf_simple *buf)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_otc_read_current_group_object()` 的回调函数（Callback Function）。

在当前组对象（current group object）被读取时调用。

若 err 为 EMSGSIZE，则对象内容（Object Contents）已被截断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `buf` | 包含对象内容（Object Contents）的缓冲区。 |

<a id="gaff887eda3b84cad1052549f23c8dcfbe"></a>

### `bt_mcc_otc_read_current_track_object_cb`

```c
typedef void(* bt_mcc_otc_read_current_track_object_cb) (struct bt_conn *conn, int err, struct net_buf_simple *buf)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_otc_read_current_track_object()` 的回调函数（Callback Function）。

在当前音轨对象（current track object）被读取时调用。

若 err 为 EMSGSIZE，则对象内容（Object Contents）已被截断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `buf` | 包含对象内容（Object Contents）的缓冲区。 |

<a id="ga13bedbb573bc5575ab75fc3ae65c1870"></a>

### `bt_mcc_otc_read_icon_object_cb`

```c
typedef void(* bt_mcc_otc_read_icon_object_cb) (struct bt_conn *conn, int err, struct net_buf_simple *buf)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_otc_read_icon_object()` 的回调函数（Callback Function）。

在图标对象（icon object）被读取时调用。

若 err 为 EMSGSIZE，则对象内容（Object Contents）已被截断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `buf` | 包含对象内容（Object Contents）的缓冲区。 |

<a id="ga920f25e04e1be4ad5f7e220c2e9102b5"></a>

### `bt_mcc_otc_read_next_track_object_cb`

```c
typedef void(* bt_mcc_otc_read_next_track_object_cb) (struct bt_conn *conn, int err, struct net_buf_simple *buf)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_otc_read_next_track_object()` 的回调函数（Callback Function）。

在下一音轨对象（next track object）被读取时调用。

若 err 为 EMSGSIZE，则对象内容（Object Contents）已被截断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `buf` | 包含对象内容（Object Contents）的缓冲区。 |

<a id="gaca904bacb552792ffd85c6a640f0ba48"></a>

### `bt_mcc_otc_read_parent_group_object_cb`

```c
typedef void(* bt_mcc_otc_read_parent_group_object_cb) (struct bt_conn *conn, int err, struct net_buf_simple *buf)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_otc_read_parent_group_object()` 的回调函数（Callback Function）。

在父组对象（parent group object）被读取时调用。

若 err 为 EMSGSIZE，则对象内容（Object Contents）已被截断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `buf` | 包含对象内容（Object Contents）的缓冲区。 |

<a id="ga1c4c842879cd8b209080a59d3ba125f8"></a>

### `bt_mcc_otc_read_track_segments_object_cb`

```c
typedef void(* bt_mcc_otc_read_track_segments_object_cb) (struct bt_conn *conn, int err, struct net_buf_simple *buf)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_otc_read_track_segments_object()` 的回调函数（Callback Function）。

在音轨分段对象（track segments object）被读取时调用。

若 err 为 EMSGSIZE，则对象内容（Object Contents）已被截断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `buf` | 包含对象内容（Object Contents）的缓冲区。 |

<a id="gadb607997fdcb3e57bbfc90790de4b927"></a>

### `bt_mcc_read_content_control_id_cb`

```c
typedef void(* bt_mcc_read_content_control_id_cb) (struct bt_conn *conn, int err, uint8_t ccid)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_read_content_control_id()` 的回调函数（Callback Function）。

在内容控制ID（content control ID）被读取时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `ccid` | 内容控制 ID（Content Control ID）。 |

<a id="ga5f21a1eed4bfe4dfbca40949af895723"></a>

### `bt_mcc_read_current_group_obj_id_cb`

```c
typedef void(* bt_mcc_read_current_group_obj_id_cb) (struct bt_conn *conn, int err, uint64_t id)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_read_current_group_obj_id()` 的回调函数（Callback Function）。

在当前组对象ID（current group object ID）被读取或收到其通知时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `id` | 当前组对象 ID（Current Group Object ID），类型为 UINT48。 |

<a id="ga28ac116604248643b0b203b4a314b7b1"></a>

### `bt_mcc_read_current_track_obj_id_cb`

```c
typedef void(* bt_mcc_read_current_track_obj_id_cb) (struct bt_conn *conn, int err, uint64_t id)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_read_current_track_obj_id()` 的回调函数（Callback Function）。

在当前音轨对象ID（current track object ID）被读取或收到其通知时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `id` | 当前音轨对象 ID（Current Track Object ID），类型为 UINT48。 |

<a id="ga471d0491b70e5472e16c3035507761cc"></a>

### `bt_mcc_read_icon_obj_id_cb`

```c
typedef void(* bt_mcc_read_icon_obj_id_cb) (struct bt_conn *conn, int err, uint64_t icon_id)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_read_icon_obj_id()` 的回调函数（Callback Function）。

在图标对象ID（icon object ID）被读取时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `icon_id` | 图标对象 ID（Icon Object ID）。它是存放于 uint64_t 中的 UINT48。 |

<a id="gaaddc4abe38f6ca811967ae6a10d8f8f0"></a>

### `bt_mcc_read_icon_url_cb`

```c
typedef void(* bt_mcc_read_icon_url_cb) (struct bt_conn *conn, int err, const char *icon_url)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_read_icon_url()` 的回调函数（Callback Function）。

在图标URL（icon URL）被读取时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `icon_url` | 图标 URL（Icon URL）。 |

<a id="ga200a827f4bf5d65570ddabd028269f77"></a>

### `bt_mcc_read_media_state_cb`

```c
typedef void(* bt_mcc_read_media_state_cb) (struct bt_conn *conn, int err, uint8_t state)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_read_media_state()` 的回调函数（Callback Function）。

在媒体状态（media state）被读取或收到其通知时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `state` | 媒体状态（Media State）。 |

<a id="ga83d6614d4a0808782b1b4df115b872d2"></a>

### `bt_mcc_read_next_track_obj_id_cb`

```c
typedef void(* bt_mcc_read_next_track_obj_id_cb) (struct bt_conn *conn, int err, uint64_t id)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_read_next_track_obj_id()` 的回调函数（Callback Function）。

在下一音轨对象ID（next track object ID）被读取或收到其通知时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `id` | 下一音轨对象 ID（Next Track Object ID），类型为 UINT48。 |

<a id="gab37df36e15132b9235d1093f5aa403cc"></a>

### `bt_mcc_read_opcodes_supported_cb`

```c
typedef void(* bt_mcc_read_opcodes_supported_cb) (struct bt_conn *conn, int err, uint32_t opcodes)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_read_opcodes_supported()` 的回调函数（Callback Function）。

读取到或收到支持的操作码（命令）（Supported Opcodes / Commands）通知时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `opcodes` | 支持的操作码（Supported Opcodes）。 |

<a id="ga48dd365aa637336b9899db4b6986a5e4"></a>

### `bt_mcc_read_parent_group_obj_id_cb`

```c
typedef void(* bt_mcc_read_parent_group_obj_id_cb) (struct bt_conn *conn, int err, uint64_t id)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_read_parent_group_obj_id()` 的回调函数（Callback Function）。

在父组对象ID（parent group object ID）被读取或收到其通知时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `id` | 父组对象 ID（Parent Group Object ID），类型为 UINT48。 |

<a id="ga6f5383be3f344c25361786d903640909"></a>

### `bt_mcc_read_playback_speed_cb`

```c
typedef void(* bt_mcc_read_playback_speed_cb) (struct bt_conn *conn, int err, int8_t speed)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_read_playback_speed()` 的回调函数（Callback Function）。

在播放速度（playback speed）被读取或收到其通知时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `speed` | 播放速度（Playback Speed）。 |

<a id="gaa943b61848ee43e91d473f6fdd0a604f"></a>

### `bt_mcc_read_player_name_cb`

```c
typedef void(* bt_mcc_read_player_name_cb) (struct bt_conn *conn, int err, const char *name)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_read_player_name()` 的回调函数（Callback Function）。

在播放器名称（player name）被读取或收到其通知时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `name` | 播放器名称（Player Name）。 |

<a id="gafb0869e0ef5332d39070081efdacf17c"></a>

### `bt_mcc_read_playing_order_cb`

```c
typedef void(* bt_mcc_read_playing_order_cb) (struct bt_conn *conn, int err, uint8_t order)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_read_playing_order()` 的回调函数（Callback Function）。

在播放顺序（playing order）被读取或收到其通知时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `order` | 播放顺序（Playback Order）。 |

<a id="gac45a2aff295535f70ac4a070e970b7a0"></a>

### `bt_mcc_read_playing_orders_supported_cb`

```c
typedef void(* bt_mcc_read_playing_orders_supported_cb) (struct bt_conn *conn, int err, uint16_t orders)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_read_playing_orders_supported()` 的回调函数（Callback Function）。

读取到或收到支持的播放顺序（Supported Playing Orders）通知时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `orders` | 支持的播放顺序（Playing Orders Supported），以位图表示。 |

<a id="ga5a39822a21a6f2aa7a6548c57979a926"></a>

### `bt_mcc_read_search_results_obj_id_cb`

```c
typedef void(* bt_mcc_read_search_results_obj_id_cb) (struct bt_conn *conn, int err, uint64_t id)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_read_search_results_obj_id()` 的回调函数（Callback Function）。

在搜索结果对象ID（search results object ID）被读取或收到其通知时调用。

注意：如果服务器不存在该特征，搜索结果对象 ID（Search Results Object ID）的值可能为 0；尚未成功执行过搜索时就是这种情况。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `id` | 搜索结果对象 ID（Search Results Object ID），类型为 UINT48。 |

<a id="ga3089e6165e8491325f7205279bb5bb83"></a>

### `bt_mcc_read_seeking_speed_cb`

```c
typedef void(* bt_mcc_read_seeking_speed_cb) (struct bt_conn *conn, int err, int8_t speed)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_read_seeking_speed()` 的回调函数（Callback Function）。

在搜寻速度（seeking speed）被读取或收到其通知时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `speed` | 搜寻速度（Seeking Speed）。 |

<a id="ga1fbf0b4fd624626127774d2662083875"></a>

### `bt_mcc_read_segments_obj_id_cb`

```c
typedef void(* bt_mcc_read_segments_obj_id_cb) (struct bt_conn *conn, int err, uint64_t id)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_read_segments_obj_id()` 的回调函数（Callback Function）。

在音轨分段对象ID（track segments object ID）被读取时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `id` | 音轨分段对象 ID（Track Segments Object ID），类型为 UINT48。 |

<a id="ga7cdb524ff9c34f24c1740adb9eca072c"></a>

### `bt_mcc_read_track_duration_cb`

```c
typedef void(* bt_mcc_read_track_duration_cb) (struct bt_conn *conn, int err, int32_t dur)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_read_track_duration()` 的回调函数（Callback Function）。

在音轨时长（track duration）被读取或收到其通知时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `dur` | 音轨时长（Track Duration）。 |

<a id="ga128883c867b10e57d3f2f26a708b7263"></a>

### `bt_mcc_read_track_position_cb`

```c
typedef void(* bt_mcc_read_track_position_cb) (struct bt_conn *conn, int err, int32_t pos)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_read_track_position()` 的回调函数（Callback Function）。

在音轨位置（track position）被读取或收到其通知时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `pos` | 音轨位置（Track Position）。 |

<a id="ga6927860f1803aeade4994610da32d402"></a>

### `bt_mcc_read_track_title_cb`

```c
typedef void(* bt_mcc_read_track_title_cb) (struct bt_conn *conn, int err, const char *title)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_read_track_title()` 的回调函数（Callback Function）。

在音轨标题（track title）被读取或收到其通知时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `title` | 音轨标题（Track Title）。 |

<a id="gab168a4c86de444dd066802c4a5fe41c3"></a>

### `bt_mcc_search_ntf_cb`

```c
typedef void(* bt_mcc_search_ntf_cb) (struct bt_conn *conn, int err, uint8_t result_code)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

搜索通知（Search Notification）的回调函数（Callback Function）。

在搜索控制点（search control point）收到通知时调用。

搜索通知（Search Notifications），即对搜索控制点写入操作的通知，使用的参数结构与发送搜索、即写入搜索控制点时所用结构不同。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `result_code` | 搜索通知（Search Notification）。 |

<a id="gae4c2d1a5c41df1c3535418cc23d48f8e"></a>

### `bt_mcc_send_cmd_cb`

```c
typedef void(* bt_mcc_send_cmd_cb) (struct bt_conn *conn, int err, const struct mpl_cmd *cmd)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_send_cmd()` 的回调函数（Callback Function）。

发送命令时调用，即设置媒体控制点（Media Control Point）时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `cmd` | 已发送的命令。 |

<a id="ga9489c34b6006df8bd26e626030cab71f"></a>

### `bt_mcc_send_search_cb`

```c
typedef void(* bt_mcc_send_search_cb) (struct bt_conn *conn, int err, const struct mpl_search *search)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_send_search()` 的回调函数（Callback Function）。

发送搜索时调用，即设置搜索控制点（Search Control Point）时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `search` | 已设置或尝试设置的搜索（Search）。 |

<a id="ga8bbb0d28f7dcf23a30a8ca56d647ac2c"></a>

### `bt_mcc_set_current_group_obj_id_cb`

```c
typedef void(* bt_mcc_set_current_group_obj_id_cb) (struct bt_conn *conn, int err, uint64_t obj_id)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_set_current_group_obj_id()` 的回调函数（Callback Function）。

在当前组对象ID（current group object ID）被设置时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `obj_id` | 已设置或尝试设置的对象 ID（Object ID），类型为 UINT48。 |

<a id="gaf0d619b493a8fb4c00278a0a85bb2529"></a>

### `bt_mcc_set_current_track_obj_id_cb`

```c
typedef void(* bt_mcc_set_current_track_obj_id_cb) (struct bt_conn *conn, int err, uint64_t id)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_set_current_track_obj_id()` 的回调函数（Callback Function）。

在当前音轨对象ID（current track object ID）被设置时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `id` | 已设置或尝试设置的对象 ID（Object ID），类型为 UINT48。 |

<a id="ga2f3099d097b28ab9c4abf81e19474def"></a>

### `bt_mcc_set_next_track_obj_id_cb`

```c
typedef void(* bt_mcc_set_next_track_obj_id_cb) (struct bt_conn *conn, int err, uint64_t id)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_set_next_track_obj_id()` 的回调函数（Callback Function）。

在下一音轨对象ID（next track object ID）被设置时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `id` | 已设置或尝试设置的对象 ID（Object ID），类型为 UINT48。 |

<a id="ga1322f2ddbb587c70fd23a7ccfc1fc779"></a>

### `bt_mcc_set_playback_speed_cb`

```c
typedef void(* bt_mcc_set_playback_speed_cb) (struct bt_conn *conn, int err, int8_t speed)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_set_playback_speed()` 的回调函数（Callback Function）。

在播放速度（playback speed）被设置时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `speed` | 已设置或尝试设置的播放速度（Playback Speed）。 |

<a id="ga1a12fb89adf29c83bca02f701213c6d7"></a>

### `bt_mcc_set_playing_order_cb`

```c
typedef void(* bt_mcc_set_playing_order_cb) (struct bt_conn *conn, int err, uint8_t order)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_set_playing_order()` 的回调函数（Callback Function）。

在播放顺序（playing order）被设置时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `order` | 已设置或尝试设置的播放顺序（Playing Order）。 |

<a id="ga1167f5e2ef4a7e78469aefc0cef18bff"></a>

### `bt_mcc_set_track_position_cb`

```c
typedef void(* bt_mcc_set_track_position_cb) (struct bt_conn *conn, int err, int32_t pos)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

用于 `bt_mcc_set_track_position()` 的回调函数（Callback Function）。

在音轨位置（track position）被设置时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `pos` | 已设置或尝试设置的音轨位置（Track Position）。 |

<a id="ga67611a3068284b0c7fbb3ef07dfe7688"></a>

### `bt_mcc_track_changed_ntf_cb`

```c
typedef void(* bt_mcc_track_changed_ntf_cb) (struct bt_conn *conn, int err)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

音轨变化通知（Track Changed Notification）的回调函数（Callback Function）。

收到音轨变化通知（Track Change Notification）时调用。

音轨变化特征（Track Changed Characteristic）是一种特殊情况：不能读取或设置，只能发送通知。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于初始化媒体控制客户端（Media Control Client）的连接。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |

<a id="gaa1f9ead03b4cccaff1e3390b8052b0f3"></a>

### `bt_mcc_discover_mcs()`

```c
int bt_mcc_discover_mcs ( struct bt_conn * conn, bool subscribe )
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

发现媒体控制服务（Media Control Service）。

在连接指定的服务器上发现媒体控制服务（Media Control Service，MCS），可选择订阅通知（Notifications）。

必须在媒体控制客户端初始化后、使用其他客户端功能前调用一次。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |
| `subscribe` | 是否订阅通知（Notifications）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga94de08bb0a1e1324600e4957b648e92b"></a>

### `bt_mcc_init()`

```c
int bt_mcc_init ( struct bt_mcc_cb * cb)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

初始化媒体控制客户端（Media Control Client）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 要使用的回调（Callbacks）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gaa243806f65c4a37d41f25bcc4f1839fc"></a>

### `bt_mcc_otc_inst()`

```c
struct bt_ots_client * bt_mcc_otc_inst ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

查找媒体控制客户端对象传输客户端实例（MCC OTC Instance）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与 MCC 服务器的连接（Connection）。 |

**返回（Returns）**：返回：找到时返回指向 MCC 对象传输客户端（OTC）实例的指针，否则为 NULL。

<a id="ga4b1ebe682ad134795f8a1b494244f8b6"></a>

### `bt_mcc_otc_read_current_group_object()`

```c
int bt_mcc_otc_read_current_group_object ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

读取当前组对象（Current Group Object）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gac4b09a77df52d2681e7652591ca32bf8"></a>

### `bt_mcc_otc_read_current_track_object()`

```c
int bt_mcc_otc_read_current_track_object ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

读取当前音轨对象（Current Track Object）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gaba527d8f0307ab11150a5434231c0e7e"></a>

### `bt_mcc_otc_read_icon_object()`

```c
int bt_mcc_otc_read_icon_object ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

读取图标对象（Icon Object）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga611c9edebff5b4347ad1241ffd19f49e"></a>

### `bt_mcc_otc_read_next_track_object()`

```c
int bt_mcc_otc_read_next_track_object ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

读取下一音轨对象（Next Track Object）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gadf687cb26a6d00bca73e273da583df88"></a>

### `bt_mcc_otc_read_object_metadata()`

```c
int bt_mcc_otc_read_object_metadata ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

读取当前对象元数据（Current Object Metadata）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gae001cb2d701457ce083aa8a0fd5ec518"></a>

### `bt_mcc_otc_read_parent_group_object()`

```c
int bt_mcc_otc_read_parent_group_object ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

读取父组对象（Parent Group Object）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gac22e840b65895aa018ab1b4535a87672"></a>

### `bt_mcc_otc_read_track_segments_object()`

```c
int bt_mcc_otc_read_track_segments_object ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

读取音轨分段对象（Track Segments Object）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga77cbf810c35d1a17efce1fae6a941963"></a>

### `bt_mcc_read_content_control_id()`

```c
int bt_mcc_read_content_control_id ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

读取内容控制 ID（Content Control ID）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga8cb43a6947df48113b082d8cc8ccf25c"></a>

### `bt_mcc_read_current_group_obj_id()`

```c
int bt_mcc_read_current_group_obj_id ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

读取当前分组对象 ID（Current Group Object ID）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga5b3a8fb8e8251cf005b34e47619ae7b9"></a>

### `bt_mcc_read_current_track_obj_id()`

```c
int bt_mcc_read_current_track_obj_id ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

读取当前曲目对象 ID（Current Track Object ID）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga0e69de33c37957a2b5473df7d3c3f389"></a>

### `bt_mcc_read_icon_obj_id()`

```c
int bt_mcc_read_icon_obj_id ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

读取图标对象 ID（Icon Object ID）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga38733456db6bc6558a511e104577c9c9"></a>

### `bt_mcc_read_icon_url()`

```c
int bt_mcc_read_icon_url ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

读取图标对象 URL（Icon Object URL）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gac1b440cfa54dd4b6e23bb47bf885f88d"></a>

### `bt_mcc_read_media_state()`

```c
int bt_mcc_read_media_state ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

读取媒体状态（Media State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga11e4c02ba0b1fbc197aaf071b82a1eed"></a>

### `bt_mcc_read_next_track_obj_id()`

```c
int bt_mcc_read_next_track_obj_id ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

读取下一曲目对象 ID（Next Track Object ID）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga692160554947f92e8c81912c5e597086"></a>

### `bt_mcc_read_opcodes_supported()`

```c
int bt_mcc_read_opcodes_supported ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

读取受支持的操作码（Opcodes Supported）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga3ccd5961cc4c8d82fa988d300e12e1ae"></a>

### `bt_mcc_read_parent_group_obj_id()`

```c
int bt_mcc_read_parent_group_obj_id ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

读取父分组对象 ID（Parent Group Object ID）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gaa566a4c42f0ab0ab6feddf4e25845609"></a>

### `bt_mcc_read_playback_speed()`

```c
int bt_mcc_read_playback_speed ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

读取播放速度（Playback Speed）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga724ce71fc88f1ca4bcf209c92c177f36"></a>

### `bt_mcc_read_player_name()`

```c
int bt_mcc_read_player_name ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

读取媒体播放器名称（Media Player Name）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga077a134ff1404fb76aa756a5531fd1d7"></a>

### `bt_mcc_read_playing_order()`

```c
int bt_mcc_read_playing_order ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

读取播放顺序（Playing Order）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gaf61f6fcf3f96ccb6f5a72ffaad27dec4"></a>

### `bt_mcc_read_playing_orders_supported()`

```c
int bt_mcc_read_playing_orders_supported ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

读取支持的播放顺序（Playing Orders Supported）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga98814a516a027bdaa3250e93d55309fd"></a>

### `bt_mcc_read_search_results_obj_id()`

```c
int bt_mcc_read_search_results_obj_id ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

搜索结果组对象标识符（Search Results Group Object ID）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga366fdfaa23cef9f1c3ba7ddd36a67658"></a>

### `bt_mcc_read_seeking_speed()`

```c
int bt_mcc_read_seeking_speed ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

读取搜索速度（Seeking Speed）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga4cb0a95e91d3ec00ede64663a2b932f0"></a>

### `bt_mcc_read_segments_obj_id()`

```c
int bt_mcc_read_segments_obj_id ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

读取音轨分段对象标识符（Track Segments Object ID）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga50a45f043bd2ae1741a120e02e9dc2f5"></a>

### `bt_mcc_read_track_duration()`

```c
int bt_mcc_read_track_duration ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

读取曲目时长（Track Duration）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gaf143098f5dfcfba01df3d6f06472779e"></a>

### `bt_mcc_read_track_position()`

```c
int bt_mcc_read_track_position ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

读取曲目位置（Track Position）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga7dfa14489a4cea4b00053c9aa75cf373"></a>

### `bt_mcc_read_track_title()`

```c
int bt_mcc_read_track_title ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

读取曲目标题（Track Title）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga3f4a538bcf436e4e80b73ed6e077dfa0"></a>

### `bt_mcc_send_cmd()`

```c
int bt_mcc_send_cmd ( struct bt_conn * conn, const struct mpl_cmd * cmd )
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

发送命令（Command）。

向服务器的媒体控制点（Media Control Point）写入命令，例如播放（play）、暂停（pause）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |
| `cmd` | 要发送的命令。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga324161056e03195820bbd7cc77ff287d"></a>

### `bt_mcc_send_search()`

```c
int bt_mcc_send_search ( struct bt_conn * conn, const struct mpl_search * search )
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

发送搜索命令（Search Command）。

向服务器的搜索控制点（Search Control Point）写入搜索。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |
| `search` | 搜索（Search）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gae3f385811f852d584595c6e531556aed"></a>

### `bt_mcc_set_current_group_obj_id()`

```c
int bt_mcc_set_current_group_obj_id ( struct bt_conn * conn, uint64_t id )
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

设置当前分组对象 ID。

将当前组（Current Group）设为 id 参数指定的组。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |
| `id` | 要设为当前组的组的对象传输服务 ID（Object Transfer Service ID），类型为 UINT48。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga8374ac230c5fe6b5a1bb7fa873fdeb49"></a>

### `bt_mcc_set_current_track_obj_id()`

```c
int bt_mcc_set_current_track_obj_id ( struct bt_conn * conn, uint64_t id )
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

设置当前曲目对象 ID。

将当前音轨（Current Track）设为 id 参数指定的音轨。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |
| `id` | 要设为当前音轨的音轨的对象传输服务 ID（Object Transfer Service ID），类型为 UINT48。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gafeebcbb0c77d5d4acbe151fd9888d084"></a>

### `bt_mcc_set_next_track_obj_id()`

```c
int bt_mcc_set_next_track_obj_id ( struct bt_conn * conn, uint64_t id )
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

设置下一曲目对象 ID。

将下一音轨（Next Track）设为 id 参数指定的音轨。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |
| `id` | 要设为下一音轨的音轨的对象传输服务 ID（Object Transfer Service ID），类型为 UINT48。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga1382e5b6000896dc94f6489909301719"></a>

### `bt_mcc_set_playback_speed()`

```c
int bt_mcc_set_playback_speed ( struct bt_conn * conn, int8_t speed )
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

设置播放速度。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |
| `speed` | 播放速度（Playback Speed）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga05295649385c3a337401765627d09553"></a>

### `bt_mcc_set_playing_order()`

```c
int bt_mcc_set_playing_order ( struct bt_conn * conn, uint8_t order )
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

设置播放顺序。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |
| `order` | 播放顺序（Playing Order）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gad324366d33bef6b1ed1c8fc881bf44cf"></a>

### `bt_mcc_set_track_position()`

```c
int bt_mcc_set_track_position ( struct bt_conn * conn, int32_t pos )
```

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

设置音轨位置（Track Position）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接（Connection）。 |
| `pos` | 音轨位置（Track Position）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。


## 5.5\_原页交叉引用（Cross References）

- [bt_mcc_cb](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [mpl_cmd](../audio_video_model_reference/P037_mpl_cmd_结构体.md)
- [cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)
- [mpl_cmd_ntf](../audio_video_model_reference/P038_mpl_cmd_ntf_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [mpl_search](../audio_video_model_reference/P040_mpl_search_结构体.md)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_ots_client](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md)
- [zephyr/bluetooth/audio/mcc.h](../api_file_media_sensor_reference/P005_zephyr__bluetooth__audio__mcc.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P004_信道探测（Channel Sounding，CS）.md) · [返回大纲](大纲.md) · [下一章](P006_媒体控制服务（Media Control Service，MCS）.md)
