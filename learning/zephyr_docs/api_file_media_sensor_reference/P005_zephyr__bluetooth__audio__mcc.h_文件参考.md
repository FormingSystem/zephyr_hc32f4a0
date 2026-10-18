---
id: learning.zephyr-docs.api-file-media-sensor-reference.page-5
title: zephyr__bluetooth__audio__mcc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mcc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_bluetooth\_\_audio\_\_mcc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mcc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙媒体控制客户端（Media Control Client，MCC）的API。

<a id="details"></a>

```c
#include <stdint.h>
#include <stdbool.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/net_buf.h>
#include <zephyr/bluetooth/audio/media_proxy.h>
```

查看此文件的源码。

蓝牙媒体控制客户端（Media Control Client，MCC）的API。

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

相关声明：[bt_mcc_discover_mcs_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gab268faeca207e115ee1be0843ab8c342)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

用于 `bt_mcc_discover_mcs()` 的回调函数（Callback Function）。

<a id="r_gaa943b61848ee43e91d473f6fdd0a604f"></a>

```c
typedef void(* bt_mcc_read_player_name_cb) (struct bt_conn *conn, int err, const char *name)
```

相关声明：[bt_mcc_read_player_name_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaa943b61848ee43e91d473f6fdd0a604f)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

用于 `bt_mcc_read_player_name()` 的回调函数（Callback Function）。

<a id="r_ga471d0491b70e5472e16c3035507761cc"></a>

```c
typedef void(* bt_mcc_read_icon_obj_id_cb) (struct bt_conn *conn, int err, uint64_t icon_id)
```

相关声明：[bt_mcc_read_icon_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga471d0491b70e5472e16c3035507761cc)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

用于 `bt_mcc_read_icon_obj_id()` 的回调函数（Callback Function）。

<a id="r_gaaddc4abe38f6ca811967ae6a10d8f8f0"></a>

```c
typedef void(* bt_mcc_read_icon_url_cb) (struct bt_conn *conn, int err, const char *icon_url)
```

相关声明：[bt_mcc_read_icon_url_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaaddc4abe38f6ca811967ae6a10d8f8f0)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

用于 `bt_mcc_read_icon_url()` 的回调函数（Callback Function）。

<a id="r_ga67611a3068284b0c7fbb3ef07dfe7688"></a>

```c
typedef void(* bt_mcc_track_changed_ntf_cb) (struct bt_conn *conn, int err)
```

相关声明：[bt_mcc_track_changed_ntf_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga67611a3068284b0c7fbb3ef07dfe7688)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

音轨变化通知（Track Changed Notification）的回调函数（Callback Function）。

<a id="r_ga6927860f1803aeade4994610da32d402"></a>

```c
typedef void(* bt_mcc_read_track_title_cb) (struct bt_conn *conn, int err, const char *title)
```

相关声明：[bt_mcc_read_track_title_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga6927860f1803aeade4994610da32d402)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

用于 `bt_mcc_read_track_title()` 的回调函数（Callback Function）。

<a id="r_ga7cdb524ff9c34f24c1740adb9eca072c"></a>

```c
typedef void(* bt_mcc_read_track_duration_cb) (struct bt_conn *conn, int err, int32_t dur)
```

相关声明：[bt_mcc_read_track_duration_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga7cdb524ff9c34f24c1740adb9eca072c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

用于 `bt_mcc_read_track_duration()` 的回调函数（Callback Function）。

<a id="r_ga128883c867b10e57d3f2f26a708b7263"></a>

```c
typedef void(* bt_mcc_read_track_position_cb) (struct bt_conn *conn, int err, int32_t pos)
```

相关声明：[bt_mcc_read_track_position_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga128883c867b10e57d3f2f26a708b7263)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

用于 `bt_mcc_read_track_position()` 的回调函数（Callback Function）。

<a id="r_ga1167f5e2ef4a7e78469aefc0cef18bff"></a>

```c
typedef void(* bt_mcc_set_track_position_cb) (struct bt_conn *conn, int err, int32_t pos)
```

相关声明：[bt_mcc_set_track_position_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga1167f5e2ef4a7e78469aefc0cef18bff)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

用于 `bt_mcc_set_track_position()` 的回调函数（Callback Function）。

<a id="r_ga6f5383be3f344c25361786d903640909"></a>

```c
typedef void(* bt_mcc_read_playback_speed_cb) (struct bt_conn *conn, int err, int8_t speed)
```

相关声明：[bt_mcc_read_playback_speed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga6f5383be3f344c25361786d903640909)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

用于 `bt_mcc_read_playback_speed()` 的回调函数（Callback Function）。

<a id="r_ga1322f2ddbb587c70fd23a7ccfc1fc779"></a>

```c
typedef void(* bt_mcc_set_playback_speed_cb) (struct bt_conn *conn, int err, int8_t speed)
```

相关声明：[bt_mcc_set_playback_speed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga1322f2ddbb587c70fd23a7ccfc1fc779)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

用于 `bt_mcc_set_playback_speed()` 的回调函数（Callback Function）。

<a id="r_ga3089e6165e8491325f7205279bb5bb83"></a>

```c
typedef void(* bt_mcc_read_seeking_speed_cb) (struct bt_conn *conn, int err, int8_t speed)
```

相关声明：[bt_mcc_read_seeking_speed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga3089e6165e8491325f7205279bb5bb83)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

用于 `bt_mcc_read_seeking_speed()` 的回调函数（Callback Function）。

<a id="r_ga1fbf0b4fd624626127774d2662083875"></a>

```c
typedef void(* bt_mcc_read_segments_obj_id_cb) (struct bt_conn *conn, int err, uint64_t id)
```

相关声明：[bt_mcc_read_segments_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga1fbf0b4fd624626127774d2662083875)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

用于 `bt_mcc_read_segments_obj_id()` 的回调函数（Callback Function）。

<a id="r_ga28ac116604248643b0b203b4a314b7b1"></a>

```c
typedef void(* bt_mcc_read_current_track_obj_id_cb) (struct bt_conn *conn, int err, uint64_t id)
```

相关声明：[bt_mcc_read_current_track_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga28ac116604248643b0b203b4a314b7b1)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

用于 `bt_mcc_read_current_track_obj_id()` 的回调函数（Callback Function）。

<a id="r_gaf0d619b493a8fb4c00278a0a85bb2529"></a>

```c
typedef void(* bt_mcc_set_current_track_obj_id_cb) (struct bt_conn *conn, int err, uint64_t id)
```

相关声明：[bt_mcc_set_current_track_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaf0d619b493a8fb4c00278a0a85bb2529)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

用于 `bt_mcc_set_current_track_obj_id()` 的回调函数（Callback Function）。

<a id="r_ga83d6614d4a0808782b1b4df115b872d2"></a>

```c
typedef void(* bt_mcc_read_next_track_obj_id_cb) (struct bt_conn *conn, int err, uint64_t id)
```

相关声明：[bt_mcc_read_next_track_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga83d6614d4a0808782b1b4df115b872d2)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

用于 `bt_mcc_read_next_track_obj_id()` 的回调函数（Callback Function）。

<a id="r_ga2f3099d097b28ab9c4abf81e19474def"></a>

```c
typedef void(* bt_mcc_set_next_track_obj_id_cb) (struct bt_conn *conn, int err, uint64_t id)
```

相关声明：[bt_mcc_set_next_track_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga2f3099d097b28ab9c4abf81e19474def)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

用于 `bt_mcc_set_next_track_obj_id()` 的回调函数（Callback Function）。

<a id="r_ga48dd365aa637336b9899db4b6986a5e4"></a>

```c
typedef void(* bt_mcc_read_parent_group_obj_id_cb) (struct bt_conn *conn, int err, uint64_t id)
```

相关声明：[bt_mcc_read_parent_group_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga48dd365aa637336b9899db4b6986a5e4)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

用于 `bt_mcc_read_parent_group_obj_id()` 的回调函数（Callback Function）。

<a id="r_ga5f21a1eed4bfe4dfbca40949af895723"></a>

```c
typedef void(* bt_mcc_read_current_group_obj_id_cb) (struct bt_conn *conn, int err, uint64_t id)
```

相关声明：[bt_mcc_read_current_group_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga5f21a1eed4bfe4dfbca40949af895723)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

用于 `bt_mcc_read_current_group_obj_id()` 的回调函数（Callback Function）。

<a id="r_ga8bbb0d28f7dcf23a30a8ca56d647ac2c"></a>

```c
typedef void(* bt_mcc_set_current_group_obj_id_cb) (struct bt_conn *conn, int err, uint64_t obj_id)
```

相关声明：[bt_mcc_set_current_group_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga8bbb0d28f7dcf23a30a8ca56d647ac2c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

用于 `bt_mcc_set_current_group_obj_id()` 的回调函数（Callback Function）。

<a id="r_gafb0869e0ef5332d39070081efdacf17c"></a>

```c
typedef void(* bt_mcc_read_playing_order_cb) (struct bt_conn *conn, int err, uint8_t order)
```

相关声明：[bt_mcc_read_playing_order_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gafb0869e0ef5332d39070081efdacf17c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

用于 `bt_mcc_read_playing_order()` 的回调函数（Callback Function）。

<a id="r_ga1a12fb89adf29c83bca02f701213c6d7"></a>

```c
typedef void(* bt_mcc_set_playing_order_cb) (struct bt_conn *conn, int err, uint8_t order)
```

相关声明：[bt_mcc_set_playing_order_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga1a12fb89adf29c83bca02f701213c6d7)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

用于 `bt_mcc_set_playing_order()` 的回调函数（Callback Function）。

<a id="r_gac45a2aff295535f70ac4a070e970b7a0"></a>

```c
typedef void(* bt_mcc_read_playing_orders_supported_cb) (struct bt_conn *conn, int err, uint16_t orders)
```

相关声明：[bt_mcc_read_playing_orders_supported_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gac45a2aff295535f70ac4a070e970b7a0)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

用于 `bt_mcc_read_playing_orders_supported()` 的回调函数（Callback Function）。

<a id="r_ga200a827f4bf5d65570ddabd028269f77"></a>

```c
typedef void(* bt_mcc_read_media_state_cb) (struct bt_conn *conn, int err, uint8_t state)
```

相关声明：[bt_mcc_read_media_state_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga200a827f4bf5d65570ddabd028269f77)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

用于 `bt_mcc_read_media_state()` 的回调函数（Callback Function）。

<a id="r_gae4c2d1a5c41df1c3535418cc23d48f8e"></a>

```c
typedef void(* bt_mcc_send_cmd_cb) (struct bt_conn *conn, int err, const struct mpl_cmd *cmd)
```

相关声明：[bt_mcc_send_cmd_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gae4c2d1a5c41df1c3535418cc23d48f8e)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[mpl_cmd](../audio_video_model_reference/P037_mpl_cmd_结构体.md)、[cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)。

用于 `bt_mcc_send_cmd()` 的回调函数（Callback Function）。

<a id="r_ga50da90a5c351c99494208b44096a61c8"></a>

```c
typedef void(* bt_mcc_cmd_ntf_cb) (struct bt_conn *conn, int err, const struct mpl_cmd_ntf *ntf)
```

相关声明：[bt_mcc_cmd_ntf_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga50da90a5c351c99494208b44096a61c8)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[mpl_cmd_ntf](../audio_video_model_reference/P038_mpl_cmd_ntf_结构体.md)。

命令通知（Command Notification）的回调函数（Callback Function）。

<a id="r_gab37df36e15132b9235d1093f5aa403cc"></a>

```c
typedef void(* bt_mcc_read_opcodes_supported_cb) (struct bt_conn *conn, int err, uint32_t opcodes)
```

相关声明：[bt_mcc_read_opcodes_supported_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gab37df36e15132b9235d1093f5aa403cc)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

用于 `bt_mcc_read_opcodes_supported()` 的回调函数（Callback Function）。

<a id="r_ga9489c34b6006df8bd26e626030cab71f"></a>

```c
typedef void(* bt_mcc_send_search_cb) (struct bt_conn *conn, int err, const struct mpl_search *search)
```

相关声明：[bt_mcc_send_search_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga9489c34b6006df8bd26e626030cab71f)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[mpl_search](../audio_video_model_reference/P040_mpl_search_结构体.md)。

用于 `bt_mcc_send_search()` 的回调函数（Callback Function）。

<a id="r_gab168a4c86de444dd066802c4a5fe41c3"></a>

```c
typedef void(* bt_mcc_search_ntf_cb) (struct bt_conn *conn, int err, uint8_t result_code)
```

相关声明：[bt_mcc_search_ntf_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gab168a4c86de444dd066802c4a5fe41c3)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

搜索通知（Search Notification）的回调函数（Callback Function）。

<a id="r_ga5a39822a21a6f2aa7a6548c57979a926"></a>

```c
typedef void(* bt_mcc_read_search_results_obj_id_cb) (struct bt_conn *conn, int err, uint64_t id)
```

相关声明：[bt_mcc_read_search_results_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga5a39822a21a6f2aa7a6548c57979a926)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

用于 `bt_mcc_read_search_results_obj_id()` 的回调函数（Callback Function）。

<a id="r_gadb607997fdcb3e57bbfc90790de4b927"></a>

```c
typedef void(* bt_mcc_read_content_control_id_cb) (struct bt_conn *conn, int err, uint8_t ccid)
```

相关声明：[bt_mcc_read_content_control_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gadb607997fdcb3e57bbfc90790de4b927)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

用于 `bt_mcc_read_content_control_id()` 的回调函数（Callback Function）。

<a id="r_gaf186e6adefa296de4146502665d738b3"></a>

```c
typedef void(* bt_mcc_otc_obj_selected_cb) (struct bt_conn *conn, int err)
```

相关声明：[bt_mcc_otc_obj_selected_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaf186e6adefa296de4146502665d738b3)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

对象被选中（Object Selected）时的回调函数（Callback Function）。

<a id="r_ga9805222315ca6e6df0720233055af10c"></a>

```c
typedef void(* bt_mcc_otc_obj_metadata_cb) (struct bt_conn *conn, int err)
```

相关声明：[bt_mcc_otc_obj_metadata_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga9805222315ca6e6df0720233055af10c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

用于 `bt_mcc_otc_read_object_metadata()` 的回调函数（Callback Function）。

<a id="r_ga13bedbb573bc5575ab75fc3ae65c1870"></a>

```c
typedef void(* bt_mcc_otc_read_icon_object_cb) (struct bt_conn *conn, int err, struct net_buf_simple *buf)
```

相关声明：[bt_mcc_otc_read_icon_object_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga13bedbb573bc5575ab75fc3ae65c1870)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

用于 `bt_mcc_otc_read_icon_object()` 的回调函数（Callback Function）。

<a id="r_ga1c4c842879cd8b209080a59d3ba125f8"></a>

```c
typedef void(* bt_mcc_otc_read_track_segments_object_cb) (struct bt_conn *conn, int err, struct net_buf_simple *buf)
```

相关声明：[bt_mcc_otc_read_track_segments_object_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga1c4c842879cd8b209080a59d3ba125f8)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

用于 `bt_mcc_otc_read_track_segments_object()` 的回调函数（Callback Function）。

<a id="r_gaff887eda3b84cad1052549f23c8dcfbe"></a>

```c
typedef void(* bt_mcc_otc_read_current_track_object_cb) (struct bt_conn *conn, int err, struct net_buf_simple *buf)
```

相关声明：[bt_mcc_otc_read_current_track_object_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaff887eda3b84cad1052549f23c8dcfbe)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

用于 `bt_mcc_otc_read_current_track_object()` 的回调函数（Callback Function）。

<a id="r_ga920f25e04e1be4ad5f7e220c2e9102b5"></a>

```c
typedef void(* bt_mcc_otc_read_next_track_object_cb) (struct bt_conn *conn, int err, struct net_buf_simple *buf)
```

相关声明：[bt_mcc_otc_read_next_track_object_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga920f25e04e1be4ad5f7e220c2e9102b5)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

用于 `bt_mcc_otc_read_next_track_object()` 的回调函数（Callback Function）。

<a id="r_gaca904bacb552792ffd85c6a640f0ba48"></a>

```c
typedef void(* bt_mcc_otc_read_parent_group_object_cb) (struct bt_conn *conn, int err, struct net_buf_simple *buf)
```

相关声明：[bt_mcc_otc_read_parent_group_object_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaca904bacb552792ffd85c6a640f0ba48)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

用于 `bt_mcc_otc_read_parent_group_object()` 的回调函数（Callback Function）。

<a id="r_ga0b309ae7ce23834f303c39017ffa4e50"></a>

```c
typedef void(* bt_mcc_otc_read_current_group_object_cb) (struct bt_conn *conn, int err, struct net_buf_simple *buf)
```

相关声明：[bt_mcc_otc_read_current_group_object_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga0b309ae7ce23834f303c39017ffa4e50)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

用于 `bt_mcc_otc_read_current_group_object()` 的回调函数（Callback Function）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.3\_函数（Functions）

<a id="r_ga94de08bb0a1e1324600e4957b648e92b"></a>

```c
int bt_mcc_init (struct bt_mcc_cb *cb)
```

相关声明：[bt_mcc_init](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga94de08bb0a1e1324600e4957b648e92b)、[bt_mcc_cb](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md)。

初始化媒体控制客户端（Media Control Client）。

<a id="r_gaa1f9ead03b4cccaff1e3390b8052b0f3"></a>

```c
int bt_mcc_discover_mcs (struct bt_conn *conn, bool subscribe)
```

相关声明：[bt_mcc_discover_mcs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaa1f9ead03b4cccaff1e3390b8052b0f3)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

发现媒体控制服务（Media Control Service）。

<a id="r_ga724ce71fc88f1ca4bcf209c92c177f36"></a>

```c
int bt_mcc_read_player_name (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_player_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga724ce71fc88f1ca4bcf209c92c177f36)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取媒体播放器名称（Media Player Name）。

<a id="r_ga0e69de33c37957a2b5473df7d3c3f389"></a>

```c
int bt_mcc_read_icon_obj_id (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_icon_obj_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga0e69de33c37957a2b5473df7d3c3f389)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取图标对象 ID（Icon Object ID）。

<a id="r_ga38733456db6bc6558a511e104577c9c9"></a>

```c
int bt_mcc_read_icon_url (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_icon_url](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga38733456db6bc6558a511e104577c9c9)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取图标对象 URL（Icon Object URL）。

<a id="r_ga7dfa14489a4cea4b00053c9aa75cf373"></a>

```c
int bt_mcc_read_track_title (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_track_title](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga7dfa14489a4cea4b00053c9aa75cf373)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取曲目标题（Track Title）。

<a id="r_ga50a45f043bd2ae1741a120e02e9dc2f5"></a>

```c
int bt_mcc_read_track_duration (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_track_duration](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga50a45f043bd2ae1741a120e02e9dc2f5)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取曲目时长（Track Duration）。

<a id="r_gaf143098f5dfcfba01df3d6f06472779e"></a>

```c
int bt_mcc_read_track_position (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_track_position](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaf143098f5dfcfba01df3d6f06472779e)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取曲目位置（Track Position）。

<a id="r_gad324366d33bef6b1ed1c8fc881bf44cf"></a>

```c
int bt_mcc_set_track_position (struct bt_conn *conn, int32_t pos)
```

相关声明：[bt_mcc_set_track_position](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gad324366d33bef6b1ed1c8fc881bf44cf)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置音轨位置（Track Position）。

<a id="r_gaa566a4c42f0ab0ab6feddf4e25845609"></a>

```c
int bt_mcc_read_playback_speed (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_playback_speed](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaa566a4c42f0ab0ab6feddf4e25845609)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取播放速度（Playback Speed）。

<a id="r_ga1382e5b6000896dc94f6489909301719"></a>

```c
int bt_mcc_set_playback_speed (struct bt_conn *conn, int8_t speed)
```

相关声明：[bt_mcc_set_playback_speed](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga1382e5b6000896dc94f6489909301719)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

设置播放速度。

<a id="r_ga366fdfaa23cef9f1c3ba7ddd36a67658"></a>

```c
int bt_mcc_read_seeking_speed (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_seeking_speed](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga366fdfaa23cef9f1c3ba7ddd36a67658)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取搜索速度（Seeking Speed）。

<a id="r_ga4cb0a95e91d3ec00ede64663a2b932f0"></a>

```c
int bt_mcc_read_segments_obj_id (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_segments_obj_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga4cb0a95e91d3ec00ede64663a2b932f0)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取音轨分段对象标识符（Track Segments Object ID）。

<a id="r_ga5b3a8fb8e8251cf005b34e47619ae7b9"></a>

```c
int bt_mcc_read_current_track_obj_id (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_current_track_obj_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga5b3a8fb8e8251cf005b34e47619ae7b9)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取当前曲目对象 ID（Current Track Object ID）。

<a id="r_ga8374ac230c5fe6b5a1bb7fa873fdeb49"></a>

```c
int bt_mcc_set_current_track_obj_id (struct bt_conn *conn, uint64_t id)
```

相关声明：[bt_mcc_set_current_track_obj_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga8374ac230c5fe6b5a1bb7fa873fdeb49)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

设置当前曲目对象 ID。

<a id="r_ga11e4c02ba0b1fbc197aaf071b82a1eed"></a>

```c
int bt_mcc_read_next_track_obj_id (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_next_track_obj_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga11e4c02ba0b1fbc197aaf071b82a1eed)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取下一曲目对象 ID（Next Track Object ID）。

<a id="r_gafeebcbb0c77d5d4acbe151fd9888d084"></a>

```c
int bt_mcc_set_next_track_obj_id (struct bt_conn *conn, uint64_t id)
```

相关声明：[bt_mcc_set_next_track_obj_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gafeebcbb0c77d5d4acbe151fd9888d084)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

设置下一曲目对象 ID。

<a id="r_ga8cb43a6947df48113b082d8cc8ccf25c"></a>

```c
int bt_mcc_read_current_group_obj_id (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_current_group_obj_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga8cb43a6947df48113b082d8cc8ccf25c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取当前分组对象 ID（Current Group Object ID）。

<a id="r_gae3f385811f852d584595c6e531556aed"></a>

```c
int bt_mcc_set_current_group_obj_id (struct bt_conn *conn, uint64_t id)
```

相关声明：[bt_mcc_set_current_group_obj_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gae3f385811f852d584595c6e531556aed)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

设置当前分组对象 ID。

<a id="r_ga3ccd5961cc4c8d82fa988d300e12e1ae"></a>

```c
int bt_mcc_read_parent_group_obj_id (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_parent_group_obj_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga3ccd5961cc4c8d82fa988d300e12e1ae)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取父分组对象 ID（Parent Group Object ID）。

<a id="r_ga077a134ff1404fb76aa756a5531fd1d7"></a>

```c
int bt_mcc_read_playing_order (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_playing_order](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga077a134ff1404fb76aa756a5531fd1d7)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取播放顺序（Playing Order）。

<a id="r_ga05295649385c3a337401765627d09553"></a>

```c
int bt_mcc_set_playing_order (struct bt_conn *conn, uint8_t order)
```

相关声明：[bt_mcc_set_playing_order](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga05295649385c3a337401765627d09553)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置播放顺序。

<a id="r_gaf61f6fcf3f96ccb6f5a72ffaad27dec4"></a>

```c
int bt_mcc_read_playing_orders_supported (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_playing_orders_supported](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaf61f6fcf3f96ccb6f5a72ffaad27dec4)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取支持的播放顺序（Playing Orders Supported）。

<a id="r_gac1b440cfa54dd4b6e23bb47bf885f88d"></a>

```c
int bt_mcc_read_media_state (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_media_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gac1b440cfa54dd4b6e23bb47bf885f88d)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取媒体状态（Media State）。

<a id="r_ga3f4a538bcf436e4e80b73ed6e077dfa0"></a>

```c
int bt_mcc_send_cmd (struct bt_conn *conn, const struct mpl_cmd *cmd)
```

相关声明：[bt_mcc_send_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga3f4a538bcf436e4e80b73ed6e077dfa0)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[mpl_cmd](../audio_video_model_reference/P037_mpl_cmd_结构体.md)、[cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)。

发送命令（Command）。

<a id="r_ga692160554947f92e8c81912c5e597086"></a>

```c
int bt_mcc_read_opcodes_supported (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_opcodes_supported](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga692160554947f92e8c81912c5e597086)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取受支持的操作码（Opcodes Supported）。

<a id="r_ga324161056e03195820bbd7cc77ff287d"></a>

```c
int bt_mcc_send_search (struct bt_conn *conn, const struct mpl_search *search)
```

相关声明：[bt_mcc_send_search](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga324161056e03195820bbd7cc77ff287d)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[mpl_search](../audio_video_model_reference/P040_mpl_search_结构体.md)。

发送搜索命令（Search Command）。

<a id="r_ga98814a516a027bdaa3250e93d55309fd"></a>

```c
int bt_mcc_read_search_results_obj_id (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_search_results_obj_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga98814a516a027bdaa3250e93d55309fd)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

搜索结果组对象标识符（Search Results Group Object ID）。

<a id="r_ga77cbf810c35d1a17efce1fae6a941963"></a>

```c
int bt_mcc_read_content_control_id (struct bt_conn *conn)
```

相关声明：[bt_mcc_read_content_control_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga77cbf810c35d1a17efce1fae6a941963)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取内容控制 ID（Content Control ID）。

<a id="r_gadf687cb26a6d00bca73e273da583df88"></a>

```c
int bt_mcc_otc_read_object_metadata (struct bt_conn *conn)
```

相关声明：[bt_mcc_otc_read_object_metadata](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gadf687cb26a6d00bca73e273da583df88)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取当前对象元数据（Current Object Metadata）。

<a id="r_gaba527d8f0307ab11150a5434231c0e7e"></a>

```c
int bt_mcc_otc_read_icon_object (struct bt_conn *conn)
```

相关声明：[bt_mcc_otc_read_icon_object](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaba527d8f0307ab11150a5434231c0e7e)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取图标对象（Icon Object）。

<a id="r_gac22e840b65895aa018ab1b4535a87672"></a>

```c
int bt_mcc_otc_read_track_segments_object (struct bt_conn *conn)
```

相关声明：[bt_mcc_otc_read_track_segments_object](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gac22e840b65895aa018ab1b4535a87672)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取音轨分段对象（Track Segments Object）。

<a id="r_gac4b09a77df52d2681e7652591ca32bf8"></a>

```c
int bt_mcc_otc_read_current_track_object (struct bt_conn *conn)
```

相关声明：[bt_mcc_otc_read_current_track_object](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gac4b09a77df52d2681e7652591ca32bf8)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取当前音轨对象（Current Track Object）。

<a id="r_ga611c9edebff5b4347ad1241ffd19f49e"></a>

```c
int bt_mcc_otc_read_next_track_object (struct bt_conn *conn)
```

相关声明：[bt_mcc_otc_read_next_track_object](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga611c9edebff5b4347ad1241ffd19f49e)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取下一音轨对象（Next Track Object）。

<a id="r_ga4b1ebe682ad134795f8a1b494244f8b6"></a>

```c
int bt_mcc_otc_read_current_group_object (struct bt_conn *conn)
```

相关声明：[bt_mcc_otc_read_current_group_object](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga4b1ebe682ad134795f8a1b494244f8b6)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取当前组对象（Current Group Object）。

<a id="r_gae001cb2d701457ce083aa8a0fd5ec518"></a>

```c
int bt_mcc_otc_read_parent_group_object (struct bt_conn *conn)
```

相关声明：[bt_mcc_otc_read_parent_group_object](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gae001cb2d701457ce083aa8a0fd5ec518)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取父组对象（Parent Group Object）。

<a id="r_gaa243806f65c4a37d41f25bcc4f1839fc"></a>

```c
struct bt_ots_client * bt_mcc_otc_inst (struct bt_conn *conn)
```

相关声明：[bt_ots_client](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md)、[bt_mcc_otc_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaa243806f65c4a37d41f25bcc4f1839fc)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

查找媒体控制客户端对象传输客户端实例（MCC OTC Instance）。


## 5.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/bluetooth/conn.h](../api_source_register_time_reference/P002_conn.h_源码浏览.md)
- [zephyr/net_buf.h](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [zephyr/bluetooth/audio/media_proxy.h](../api_source_runtime_reference/P042_media_proxy.h_源码浏览.md)
- [查看此文件的源码。](../api_source_register_time_reference/P004_mcc.h_源码浏览.md)
- [bt_mcc_cb](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md)
- [bt_mcc_discover_mcs_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gab268faeca207e115ee1be0843ab8c342)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_mcc_discover_mcs()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaa1f9ead03b4cccaff1e3390b8052b0f3)
- [bt_mcc_read_player_name_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaa943b61848ee43e91d473f6fdd0a604f)
- [bt_mcc_read_player_name()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga724ce71fc88f1ca4bcf209c92c177f36)
- [bt_mcc_read_icon_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga471d0491b70e5472e16c3035507761cc)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [bt_mcc_read_icon_obj_id()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga0e69de33c37957a2b5473df7d3c3f389)
- [bt_mcc_read_icon_url_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaaddc4abe38f6ca811967ae6a10d8f8f0)
- [bt_mcc_read_icon_url()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga38733456db6bc6558a511e104577c9c9)
- [bt_mcc_track_changed_ntf_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga67611a3068284b0c7fbb3ef07dfe7688)
- [bt_mcc_read_track_title_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga6927860f1803aeade4994610da32d402)
- [bt_mcc_read_track_title()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga7dfa14489a4cea4b00053c9aa75cf373)
- [bt_mcc_read_track_duration_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga7cdb524ff9c34f24c1740adb9eca072c)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [bt_mcc_read_track_duration()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga50a45f043bd2ae1741a120e02e9dc2f5)
- [bt_mcc_read_track_position_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga128883c867b10e57d3f2f26a708b7263)
- [bt_mcc_read_track_position()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaf143098f5dfcfba01df3d6f06472779e)
- [bt_mcc_set_track_position_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga1167f5e2ef4a7e78469aefc0cef18bff)
- [bt_mcc_set_track_position()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gad324366d33bef6b1ed1c8fc881bf44cf)
- [bt_mcc_read_playback_speed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga6f5383be3f344c25361786d903640909)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [bt_mcc_read_playback_speed()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaa566a4c42f0ab0ab6feddf4e25845609)
- [bt_mcc_set_playback_speed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga1322f2ddbb587c70fd23a7ccfc1fc779)
- [bt_mcc_set_playback_speed()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga1382e5b6000896dc94f6489909301719)
- [bt_mcc_read_seeking_speed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga3089e6165e8491325f7205279bb5bb83)
- [bt_mcc_read_seeking_speed()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga366fdfaa23cef9f1c3ba7ddd36a67658)
- [bt_mcc_read_segments_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga1fbf0b4fd624626127774d2662083875)
- [bt_mcc_read_segments_obj_id()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga4cb0a95e91d3ec00ede64663a2b932f0)
- [bt_mcc_read_current_track_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga28ac116604248643b0b203b4a314b7b1)
- [bt_mcc_read_current_track_obj_id()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga5b3a8fb8e8251cf005b34e47619ae7b9)
- [bt_mcc_set_current_track_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaf0d619b493a8fb4c00278a0a85bb2529)
- [bt_mcc_set_current_track_obj_id()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga8374ac230c5fe6b5a1bb7fa873fdeb49)
- [bt_mcc_read_next_track_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga83d6614d4a0808782b1b4df115b872d2)
- [bt_mcc_read_next_track_obj_id()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga11e4c02ba0b1fbc197aaf071b82a1eed)
- [bt_mcc_set_next_track_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga2f3099d097b28ab9c4abf81e19474def)
- [bt_mcc_set_next_track_obj_id()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gafeebcbb0c77d5d4acbe151fd9888d084)
- [bt_mcc_read_parent_group_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga48dd365aa637336b9899db4b6986a5e4)
- [bt_mcc_read_parent_group_obj_id()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga3ccd5961cc4c8d82fa988d300e12e1ae)
- [bt_mcc_read_current_group_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga5f21a1eed4bfe4dfbca40949af895723)
- [bt_mcc_read_current_group_obj_id()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga8cb43a6947df48113b082d8cc8ccf25c)
- [bt_mcc_set_current_group_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga8bbb0d28f7dcf23a30a8ca56d647ac2c)
- [bt_mcc_set_current_group_obj_id()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gae3f385811f852d584595c6e531556aed)
- [bt_mcc_read_playing_order_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gafb0869e0ef5332d39070081efdacf17c)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_mcc_read_playing_order()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga077a134ff1404fb76aa756a5531fd1d7)
- [bt_mcc_set_playing_order_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga1a12fb89adf29c83bca02f701213c6d7)
- [bt_mcc_set_playing_order()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga05295649385c3a337401765627d09553)
- [bt_mcc_read_playing_orders_supported_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gac45a2aff295535f70ac4a070e970b7a0)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_mcc_read_playing_orders_supported()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaf61f6fcf3f96ccb6f5a72ffaad27dec4)
- [bt_mcc_read_media_state_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga200a827f4bf5d65570ddabd028269f77)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [bt_mcc_read_media_state()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gac1b440cfa54dd4b6e23bb47bf885f88d)
- [bt_mcc_send_cmd_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gae4c2d1a5c41df1c3535418cc23d48f8e)
- [mpl_cmd](../audio_video_model_reference/P037_mpl_cmd_结构体.md)
- [cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)
- [bt_mcc_send_cmd()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga3f4a538bcf436e4e80b73ed6e077dfa0)
- [bt_mcc_cmd_ntf_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga50da90a5c351c99494208b44096a61c8)
- [mpl_cmd_ntf](../audio_video_model_reference/P038_mpl_cmd_ntf_结构体.md)
- [bt_mcc_read_opcodes_supported_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gab37df36e15132b9235d1093f5aa403cc)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bt_mcc_read_opcodes_supported()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga692160554947f92e8c81912c5e597086)
- [bt_mcc_send_search_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga9489c34b6006df8bd26e626030cab71f)
- [mpl_search](../audio_video_model_reference/P040_mpl_search_结构体.md)
- [bt_mcc_send_search()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga324161056e03195820bbd7cc77ff287d)
- [bt_mcc_search_ntf_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gab168a4c86de444dd066802c4a5fe41c3)
- [bt_mcc_read_search_results_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga5a39822a21a6f2aa7a6548c57979a926)
- [bt_mcc_read_search_results_obj_id()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga98814a516a027bdaa3250e93d55309fd)
- [bt_mcc_read_content_control_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gadb607997fdcb3e57bbfc90790de4b927)
- [bt_mcc_read_content_control_id()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga77cbf810c35d1a17efce1fae6a941963)
- [bt_mcc_otc_obj_selected_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaf186e6adefa296de4146502665d738b3)
- [bt_mcc_otc_obj_metadata_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga9805222315ca6e6df0720233055af10c)
- [bt_mcc_otc_read_object_metadata()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gadf687cb26a6d00bca73e273da583df88)
- [bt_mcc_otc_read_icon_object_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga13bedbb573bc5575ab75fc3ae65c1870)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bt_mcc_otc_read_icon_object()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaba527d8f0307ab11150a5434231c0e7e)
- [bt_mcc_otc_read_track_segments_object_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga1c4c842879cd8b209080a59d3ba125f8)
- [bt_mcc_otc_read_track_segments_object()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gac22e840b65895aa018ab1b4535a87672)
- [bt_mcc_otc_read_current_track_object_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaff887eda3b84cad1052549f23c8dcfbe)
- [bt_mcc_otc_read_current_track_object()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gac4b09a77df52d2681e7652591ca32bf8)
- [bt_mcc_otc_read_next_track_object_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga920f25e04e1be4ad5f7e220c2e9102b5)
- [bt_mcc_otc_read_next_track_object()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga611c9edebff5b4347ad1241ffd19f49e)
- [bt_mcc_otc_read_parent_group_object_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaca904bacb552792ffd85c6a640f0ba48)
- [bt_mcc_otc_read_parent_group_object()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gae001cb2d701457ce083aa8a0fd5ec518)
- [bt_mcc_otc_read_current_group_object_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga0b309ae7ce23834f303c39017ffa4e50)
- [bt_mcc_otc_read_current_group_object()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga4b1ebe682ad134795f8a1b494244f8b6)
- [bt_mcc_init](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga94de08bb0a1e1324600e4957b648e92b)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_ots_client](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md)
- [bt_mcc_otc_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaa243806f65c4a37d41f25bcc4f1839fc)

<a id="header-details"></a>

---

[上一章](P004_zephyr__video__formats.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__dt-bindings__clock__rx_clock.h_文件参考.md)
