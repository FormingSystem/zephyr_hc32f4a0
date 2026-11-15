---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-119
title: bt_mcc_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mcc__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第119章\_bt\_mcc\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mcc__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

媒体控制客户端（Media Control Client）的回调。

```c
#include <zephyr/bluetooth/audio/mcc.h>
```

<a id="details"></a>

媒体控制客户端（Media Control Client）的回调。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 119.1\_数据成员（Data Fields）

<a id="r_a2f48a0e0b891131347b0ddc2cb5a8ba7"></a>

```c
bt_mcc_discover_mcs_cb discover_mcs
```

相关声明：[bt_mcc_discover_mcs_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gab268faeca207e115ee1be0843ab8c342)、[discover_mcs](#a2f48a0e0b891131347b0ddc2cb5a8ba7)。

发现完成回调（Discovery finished callback）。

<a id="r_aeea1ef17b3b1e24c965d71f210952079"></a>

```c
bt_mcc_read_player_name_cb read_player_name
```

相关声明：[bt_mcc_read_player_name_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaa943b61848ee43e91d473f6fdd0a604f)、[read_player_name](#aeea1ef17b3b1e24c965d71f210952079)。

读取播放器名称（player name）时的回调。

<a id="r_a00acb676c73ebbad2b0180b3e8373150"></a>

```c
bt_mcc_read_icon_obj_id_cb read_icon_obj_id
```

相关声明：[bt_mcc_read_icon_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga471d0491b70e5472e16c3035507761cc)、[read_icon_obj_id](#a00acb676c73ebbad2b0180b3e8373150)。

读取图标对象 ID（icon object ID）时的回调。

<a id="r_a8c7b5954e286d074a94a39bee266082c"></a>

```c
bt_mcc_read_icon_url_cb read_icon_url
```

相关声明：[bt_mcc_read_icon_url_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaaddc4abe38f6ca811967ae6a10d8f8f0)、[read_icon_url](#a8c7b5954e286d074a94a39bee266082c)。

读取图标 URL（icon URL）时的回调。

<a id="r_abb7769b73564a22645bfe6b11f239637"></a>

```c
bt_mcc_track_changed_ntf_cb track_changed_ntf
```

相关声明：[bt_mcc_track_changed_ntf_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga67611a3068284b0c7fbb3ef07dfe7688)、[track_changed_ntf](#abb7769b73564a22645bfe6b11f239637)。

收到曲目已变更（track changed）通知时的回调。

<a id="r_a3975e296b67eb244bf92254e9776ea3c"></a>

```c
bt_mcc_read_track_title_cb read_track_title
```

相关声明：[bt_mcc_read_track_title_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga6927860f1803aeade4994610da32d402)、[read_track_title](#a3975e296b67eb244bf92254e9776ea3c)。

读取曲目标题（track title）时的回调。

<a id="r_a85268d9ce708aef01aa528aaedf0f7e0"></a>

```c
bt_mcc_read_track_duration_cb read_track_duration
```

相关声明：[bt_mcc_read_track_duration_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga7cdb524ff9c34f24c1740adb9eca072c)、[read_track_duration](#a85268d9ce708aef01aa528aaedf0f7e0)。

读取曲目时长（track duration）时的回调。

<a id="r_ad1636e717ef5039586b7a1462041e888"></a>

```c
bt_mcc_read_track_position_cb read_track_position
```

相关声明：[bt_mcc_read_track_position_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga128883c867b10e57d3f2f26a708b7263)、[read_track_position](#ad1636e717ef5039586b7a1462041e888)。

读取曲目位置（track position）时的回调。

<a id="r_affa57da8f325dce8298d097af38d0d62"></a>

```c
bt_mcc_set_track_position_cb set_track_position
```

相关声明：[bt_mcc_set_track_position_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga1167f5e2ef4a7e78469aefc0cef18bff)、[set_track_position](#affa57da8f325dce8298d097af38d0d62)。

设置曲目位置（track position）时的回调。

<a id="r_a47f8d92b18b0e4ffb3aacde05e7cb410"></a>

```c
bt_mcc_read_playback_speed_cb read_playback_speed
```

相关声明：[bt_mcc_read_playback_speed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga6f5383be3f344c25361786d903640909)、[read_playback_speed](#a47f8d92b18b0e4ffb3aacde05e7cb410)。

读取播放速度（playback speed）时的回调。

<a id="r_a5f87b5d07241b4124911be0cd6c43b37"></a>

```c
bt_mcc_set_playback_speed_cb set_playback_speed
```

相关声明：[bt_mcc_set_playback_speed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga1322f2ddbb587c70fd23a7ccfc1fc779)、[set_playback_speed](#a5f87b5d07241b4124911be0cd6c43b37)。

设置播放速度（playback speed）时的回调。

<a id="r_a75c8e63baf45a119e9007f246362ab8d"></a>

```c
bt_mcc_read_seeking_speed_cb read_seeking_speed
```

相关声明：[bt_mcc_read_seeking_speed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga3089e6165e8491325f7205279bb5bb83)、[read_seeking_speed](#a75c8e63baf45a119e9007f246362ab8d)。

读取搜索播放速度（seeking speed）时的回调。

<a id="r_a810ceaee44fcbdec90a1ee227b6974df"></a>

```c
bt_mcc_read_segments_obj_id_cb read_segments_obj_id
```

相关声明：[bt_mcc_read_segments_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga1fbf0b4fd624626127774d2662083875)、[read_segments_obj_id](#a810ceaee44fcbdec90a1ee227b6974df)。

读取分段对象 ID（segments object ID）时的回调。

<a id="r_a46bd2c23d92d8362cdf9ad4862b78407"></a>

```c
bt_mcc_read_current_track_obj_id_cb read_current_track_obj_id
```

相关声明：[bt_mcc_read_current_track_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga28ac116604248643b0b203b4a314b7b1)、[read_current_track_obj_id](#a46bd2c23d92d8362cdf9ad4862b78407)。

读取当前曲目对象 ID（current track object ID）时的回调。

<a id="r_ac9e182bbdd9671c5caee5bcd42198d90"></a>

```c
bt_mcc_set_current_track_obj_id_cb set_current_track_obj_id
```

相关声明：[bt_mcc_set_current_track_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaf0d619b493a8fb4c00278a0a85bb2529)、[set_current_track_obj_id](#ac9e182bbdd9671c5caee5bcd42198d90)。

设置当前曲目对象 ID（current track object ID）时的回调。

<a id="r_a540797123f8968b49a6e98b30ea534c8"></a>

```c
bt_mcc_read_next_track_obj_id_cb read_next_track_obj_id
```

相关声明：[bt_mcc_read_next_track_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga83d6614d4a0808782b1b4df115b872d2)、[read_next_track_obj_id](#a540797123f8968b49a6e98b30ea534c8)。

读取下一曲目对象 ID（next track object ID）时的回调。

<a id="r_a4f2ea54d6c60beb28feab7b6453aec7c"></a>

```c
bt_mcc_set_next_track_obj_id_cb set_next_track_obj_id
```

相关声明：[bt_mcc_set_next_track_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga2f3099d097b28ab9c4abf81e19474def)、[set_next_track_obj_id](#a4f2ea54d6c60beb28feab7b6453aec7c)。

设置下一曲目对象 ID（next track object ID）时的回调。

<a id="r_a0e7757b6f911456feaca931cd33f117f"></a>

```c
bt_mcc_read_current_group_obj_id_cb read_current_group_obj_id
```

相关声明：[bt_mcc_read_current_group_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga5f21a1eed4bfe4dfbca40949af895723)、[read_current_group_obj_id](#a0e7757b6f911456feaca931cd33f117f)。

读取当前组对象 ID（current group object ID）时的回调。

<a id="r_ad8d3eff0cc183797280c9f668a840add"></a>

```c
bt_mcc_set_current_group_obj_id_cb set_current_group_obj_id
```

相关声明：[bt_mcc_set_current_group_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga8bbb0d28f7dcf23a30a8ca56d647ac2c)、[set_current_group_obj_id](#ad8d3eff0cc183797280c9f668a840add)。

设置当前组对象 ID（current group object ID）时的回调。

<a id="r_a87583247634728d3d9af7eb411d088a7"></a>

```c
bt_mcc_read_parent_group_obj_id_cb read_parent_group_obj_id
```

相关声明：[bt_mcc_read_parent_group_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga48dd365aa637336b9899db4b6986a5e4)、[read_parent_group_obj_id](#a87583247634728d3d9af7eb411d088a7)。

读取父组对象 ID（parent group object ID）时的回调。

<a id="r_a3538beef41edd96b8557b43c1266078b"></a>

```c
bt_mcc_read_playing_order_cb read_playing_order
```

相关声明：[bt_mcc_read_playing_order_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gafb0869e0ef5332d39070081efdacf17c)、[read_playing_order](#a3538beef41edd96b8557b43c1266078b)。

读取播放顺序（playing order）时的回调。

<a id="r_a00a0ba5ed665ef7fc2ca861d985ccd64"></a>

```c
bt_mcc_set_playing_order_cb set_playing_order
```

相关声明：[bt_mcc_set_playing_order_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga1a12fb89adf29c83bca02f701213c6d7)、[set_playing_order](#a00a0ba5ed665ef7fc2ca861d985ccd64)。

设置播放顺序（playing order）时的回调。

<a id="r_a929d7b8fc925961048d5ff5e70a5126e"></a>

```c
bt_mcc_read_playing_orders_supported_cb read_playing_orders_supported
```

相关声明：[bt_mcc_read_playing_orders_supported_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gac45a2aff295535f70ac4a070e970b7a0)、[read_playing_orders_supported](#a929d7b8fc925961048d5ff5e70a5126e)。

读取支持的播放顺序（supported playing orders）时的回调。

<a id="r_a38e4682608c7d7ff6c44431a6bdab3af"></a>

```c
bt_mcc_read_media_state_cb read_media_state
```

相关声明：[bt_mcc_read_media_state_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga200a827f4bf5d65570ddabd028269f77)、[read_media_state](#a38e4682608c7d7ff6c44431a6bdab3af)。

读取媒体状态（media state）时的回调。

<a id="r_a90e62e90752087da36122a65f6c9ed4e"></a>

```c
bt_mcc_send_cmd_cb send_cmd
```

相关声明：[bt_mcc_send_cmd_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gae4c2d1a5c41df1c3535418cc23d48f8e)、[send_cmd](#a90e62e90752087da36122a65f6c9ed4e)。

发送命令时的回调。

<a id="r_a835f60ad32edc4311a624e779972f0d5"></a>

```c
bt_mcc_cmd_ntf_cb cmd_ntf
```

相关声明：[bt_mcc_cmd_ntf_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga50da90a5c351c99494208b44096a61c8)、[cmd_ntf](#a835f60ad32edc4311a624e779972f0d5)。

命令通知（command notifications）回调。

<a id="r_ad7ddcae67bf71030ac2d8438ac2e863f"></a>

```c
bt_mcc_read_opcodes_supported_cb read_opcodes_supported
```

相关声明：[bt_mcc_read_opcodes_supported_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gab37df36e15132b9235d1093f5aa403cc)、[read_opcodes_supported](#ad7ddcae67bf71030ac2d8438ac2e863f)。

读取支持的操作码（supported opcodes）时的回调。

<a id="r_a1c7277f390f6b478090611be9e82a4f8"></a>

```c
bt_mcc_send_search_cb send_search
```

相关声明：[bt_mcc_send_search_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga9489c34b6006df8bd26e626030cab71f)、[send_search](#a1c7277f390f6b478090611be9e82a4f8)。

发送搜索查询（search query）时的回调。

<a id="r_a9f7f3424aa230a8752f40a40b82b0b66"></a>

```c
bt_mcc_search_ntf_cb search_ntf
```

相关声明：[bt_mcc_search_ntf_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gab168a4c86de444dd066802c4a5fe41c3)、[search_ntf](#a9f7f3424aa230a8752f40a40b82b0b66)。

收到搜索通知（search notification）时的回调。

<a id="r_aaa2bdfb99e5cd7c2a0d0c800533e8491"></a>

```c
bt_mcc_read_search_results_obj_id_cb read_search_results_obj_id
```

相关声明：[bt_mcc_read_search_results_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga5a39822a21a6f2aa7a6548c57979a926)、[read_search_results_obj_id](#aaa2bdfb99e5cd7c2a0d0c800533e8491)。

读取搜索结果对象 ID（search results object ID）时的回调。

<a id="r_ae4d0e2e4df695352e8d2ed76db1f420e"></a>

```c
bt_mcc_read_content_control_id_cb read_content_control_id
```

相关声明：[bt_mcc_read_content_control_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gadb607997fdcb3e57bbfc90790de4b927)、[read_content_control_id](#ae4d0e2e4df695352e8d2ed76db1f420e)。

读取内容控制 ID（content control ID）时的回调。

<a id="r_a17ebc9dbddd714d99b599b2a683ab771"></a>

```c
bt_mcc_otc_obj_selected_cb otc_obj_selected
```

相关声明：[bt_mcc_otc_obj_selected_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaf186e6adefa296de4146502665d738b3)、[otc_obj_selected](#a17ebc9dbddd714d99b599b2a683ab771)。

选择对象时的回调。

<a id="r_af1c9664a2459550af0a6ed611fd17263"></a>

```c
bt_mcc_otc_obj_metadata_cb otc_obj_metadata
```

相关声明：[bt_mcc_otc_obj_metadata_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga9805222315ca6e6df0720233055af10c)、[otc_obj_metadata](#af1c9664a2459550af0a6ed611fd17263)。

收到当前对象元数据（metadata）时的回调。

<a id="r_a054e0cfb27c01f43d499a2c44788cb73"></a>

```c
bt_mcc_otc_read_icon_object_cb otc_icon_object
```

相关声明：[bt_mcc_otc_read_icon_object_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga13bedbb573bc5575ab75fc3ae65c1870)、[otc_icon_object](#a054e0cfb27c01f43d499a2c44788cb73)。

读取当前图标对象时的回调。

<a id="r_a2c1b570ce8d83c3f20eb99807263a5cd"></a>

```c
bt_mcc_otc_read_track_segments_object_cb otc_track_segments_object
```

相关声明：[bt_mcc_otc_read_track_segments_object_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga1c4c842879cd8b209080a59d3ba125f8)、[otc_track_segments_object](#a2c1b570ce8d83c3f20eb99807263a5cd)。

读取曲目分段对象时的回调。

<a id="r_ad13669e60992a1a407534f387efd1da8"></a>

```c
bt_mcc_otc_read_current_track_object_cb otc_current_track_object
```

相关声明：[bt_mcc_otc_read_current_track_object_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaff887eda3b84cad1052549f23c8dcfbe)、[otc_current_track_object](#ad13669e60992a1a407534f387efd1da8)。

读取当前曲目对象时的回调。

<a id="r_a52724924ab19f59cc936344ebe13d437"></a>

```c
bt_mcc_otc_read_next_track_object_cb otc_next_track_object
```

相关声明：[bt_mcc_otc_read_next_track_object_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga920f25e04e1be4ad5f7e220c2e9102b5)、[otc_next_track_object](#a52724924ab19f59cc936344ebe13d437)。

读取下一曲目对象时的回调。

<a id="r_ac0e382f1117f983e7a2178fde274d460"></a>

```c
bt_mcc_otc_read_current_group_object_cb otc_current_group_object
```

相关声明：[bt_mcc_otc_read_current_group_object_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga0b309ae7ce23834f303c39017ffa4e50)、[otc_current_group_object](#ac0e382f1117f983e7a2178fde274d460)。

读取当前组对象时的回调。

<a id="r_a872d0322ba3889f1f7d32e8966b53624"></a>

```c
bt_mcc_otc_read_parent_group_object_cb otc_parent_group_object
```

相关声明：[bt_mcc_otc_read_parent_group_object_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaca904bacb552792ffd85c6a640f0ba48)、[otc_parent_group_object](#a872d0322ba3889f1f7d32e8966b53624)。

读取父组对象时的回调。

## 119.2\_详细说明（Detailed Documentation）

<a id="a835f60ad32edc4311a624e779972f0d5"></a>

### `cmd_ntf`

```c
bt_mcc_cmd_ntf_cb bt_mcc_cb::cmd_ntf
```

命令通知（command notifications）回调。

<a id="a2f48a0e0b891131347b0ddc2cb5a8ba7"></a>

### `discover_mcs`

```c
bt_mcc_discover_mcs_cb bt_mcc_cb::discover_mcs
```

发现完成回调（Discovery finished callback）。

<a id="ac0e382f1117f983e7a2178fde274d460"></a>

### `otc_current_group_object`

```c
bt_mcc_otc_read_current_group_object_cb bt_mcc_cb::otc_current_group_object
```

读取当前组对象时的回调。

<a id="ad13669e60992a1a407534f387efd1da8"></a>

### `otc_current_track_object`

```c
bt_mcc_otc_read_current_track_object_cb bt_mcc_cb::otc_current_track_object
```

读取当前曲目对象时的回调。

<a id="a054e0cfb27c01f43d499a2c44788cb73"></a>

### `otc_icon_object`

```c
bt_mcc_otc_read_icon_object_cb bt_mcc_cb::otc_icon_object
```

读取当前图标对象时的回调。

<a id="a52724924ab19f59cc936344ebe13d437"></a>

### `otc_next_track_object`

```c
bt_mcc_otc_read_next_track_object_cb bt_mcc_cb::otc_next_track_object
```

读取下一曲目对象时的回调。

<a id="af1c9664a2459550af0a6ed611fd17263"></a>

### `otc_obj_metadata`

```c
bt_mcc_otc_obj_metadata_cb bt_mcc_cb::otc_obj_metadata
```

收到当前对象元数据（metadata）时的回调。

<a id="a17ebc9dbddd714d99b599b2a683ab771"></a>

### `otc_obj_selected`

```c
bt_mcc_otc_obj_selected_cb bt_mcc_cb::otc_obj_selected
```

选择对象时的回调。

<a id="a872d0322ba3889f1f7d32e8966b53624"></a>

### `otc_parent_group_object`

```c
bt_mcc_otc_read_parent_group_object_cb bt_mcc_cb::otc_parent_group_object
```

读取父组对象时的回调。

<a id="a2c1b570ce8d83c3f20eb99807263a5cd"></a>

### `otc_track_segments_object`

```c
bt_mcc_otc_read_track_segments_object_cb bt_mcc_cb::otc_track_segments_object
```

读取曲目分段对象时的回调。

<a id="ae4d0e2e4df695352e8d2ed76db1f420e"></a>

### `read_content_control_id`

```c
bt_mcc_read_content_control_id_cb bt_mcc_cb::read_content_control_id
```

读取内容控制 ID（content control ID）时的回调。

<a id="a0e7757b6f911456feaca931cd33f117f"></a>

### `read_current_group_obj_id`

```c
bt_mcc_read_current_group_obj_id_cb bt_mcc_cb::read_current_group_obj_id
```

读取当前组对象 ID（current group object ID）时的回调。

<a id="a46bd2c23d92d8362cdf9ad4862b78407"></a>

### `read_current_track_obj_id`

```c
bt_mcc_read_current_track_obj_id_cb bt_mcc_cb::read_current_track_obj_id
```

读取当前曲目对象 ID（current track object ID）时的回调。

<a id="a00acb676c73ebbad2b0180b3e8373150"></a>

### `read_icon_obj_id`

```c
bt_mcc_read_icon_obj_id_cb bt_mcc_cb::read_icon_obj_id
```

读取图标对象 ID（icon object ID）时的回调。

<a id="a8c7b5954e286d074a94a39bee266082c"></a>

### `read_icon_url`

```c
bt_mcc_read_icon_url_cb bt_mcc_cb::read_icon_url
```

读取图标 URL（icon URL）时的回调。

<a id="a38e4682608c7d7ff6c44431a6bdab3af"></a>

### `read_media_state`

```c
bt_mcc_read_media_state_cb bt_mcc_cb::read_media_state
```

读取媒体状态（media state）时的回调。

<a id="a540797123f8968b49a6e98b30ea534c8"></a>

### `read_next_track_obj_id`

```c
bt_mcc_read_next_track_obj_id_cb bt_mcc_cb::read_next_track_obj_id
```

读取下一曲目对象 ID（next track object ID）时的回调。

<a id="ad7ddcae67bf71030ac2d8438ac2e863f"></a>

### `read_opcodes_supported`

```c
bt_mcc_read_opcodes_supported_cb bt_mcc_cb::read_opcodes_supported
```

读取支持的操作码（supported opcodes）时的回调。

<a id="a87583247634728d3d9af7eb411d088a7"></a>

### `read_parent_group_obj_id`

```c
bt_mcc_read_parent_group_obj_id_cb bt_mcc_cb::read_parent_group_obj_id
```

读取父组对象 ID（parent group object ID）时的回调。

<a id="a47f8d92b18b0e4ffb3aacde05e7cb410"></a>

### `read_playback_speed`

```c
bt_mcc_read_playback_speed_cb bt_mcc_cb::read_playback_speed
```

读取播放速度（playback speed）时的回调。

<a id="aeea1ef17b3b1e24c965d71f210952079"></a>

### `read_player_name`

```c
bt_mcc_read_player_name_cb bt_mcc_cb::read_player_name
```

读取播放器名称（player name）时的回调。

<a id="a3538beef41edd96b8557b43c1266078b"></a>

### `read_playing_order`

```c
bt_mcc_read_playing_order_cb bt_mcc_cb::read_playing_order
```

读取播放顺序（playing order）时的回调。

<a id="a929d7b8fc925961048d5ff5e70a5126e"></a>

### `read_playing_orders_supported`

```c
bt_mcc_read_playing_orders_supported_cb bt_mcc_cb::read_playing_orders_supported
```

读取支持的播放顺序（supported playing orders）时的回调。

<a id="aaa2bdfb99e5cd7c2a0d0c800533e8491"></a>

### `read_search_results_obj_id`

```c
bt_mcc_read_search_results_obj_id_cb bt_mcc_cb::read_search_results_obj_id
```

读取搜索结果对象 ID（search results object ID）时的回调。

<a id="a75c8e63baf45a119e9007f246362ab8d"></a>

### `read_seeking_speed`

```c
bt_mcc_read_seeking_speed_cb bt_mcc_cb::read_seeking_speed
```

读取搜索播放速度（seeking speed）时的回调。

<a id="a810ceaee44fcbdec90a1ee227b6974df"></a>

### `read_segments_obj_id`

```c
bt_mcc_read_segments_obj_id_cb bt_mcc_cb::read_segments_obj_id
```

读取分段对象 ID（segments object ID）时的回调。

<a id="a85268d9ce708aef01aa528aaedf0f7e0"></a>

### `read_track_duration`

```c
bt_mcc_read_track_duration_cb bt_mcc_cb::read_track_duration
```

读取曲目时长（track duration）时的回调。

<a id="ad1636e717ef5039586b7a1462041e888"></a>

### `read_track_position`

```c
bt_mcc_read_track_position_cb bt_mcc_cb::read_track_position
```

读取曲目位置（track position）时的回调。

<a id="a3975e296b67eb244bf92254e9776ea3c"></a>

### `read_track_title`

```c
bt_mcc_read_track_title_cb bt_mcc_cb::read_track_title
```

读取曲目标题（track title）时的回调。

<a id="a9f7f3424aa230a8752f40a40b82b0b66"></a>

### `search_ntf`

```c
bt_mcc_search_ntf_cb bt_mcc_cb::search_ntf
```

收到搜索通知（search notification）时的回调。

<a id="a90e62e90752087da36122a65f6c9ed4e"></a>

### `send_cmd`

```c
bt_mcc_send_cmd_cb bt_mcc_cb::send_cmd
```

发送命令时的回调。

<a id="a1c7277f390f6b478090611be9e82a4f8"></a>

### `send_search`

```c
bt_mcc_send_search_cb bt_mcc_cb::send_search
```

发送搜索查询（search query）时的回调。

<a id="ad8d3eff0cc183797280c9f668a840add"></a>

### `set_current_group_obj_id`

```c
bt_mcc_set_current_group_obj_id_cb bt_mcc_cb::set_current_group_obj_id
```

设置当前组对象 ID（current group object ID）时的回调。

<a id="ac9e182bbdd9671c5caee5bcd42198d90"></a>

### `set_current_track_obj_id`

```c
bt_mcc_set_current_track_obj_id_cb bt_mcc_cb::set_current_track_obj_id
```

设置当前曲目对象 ID（current track object ID）时的回调。

<a id="a4f2ea54d6c60beb28feab7b6453aec7c"></a>

### `set_next_track_obj_id`

```c
bt_mcc_set_next_track_obj_id_cb bt_mcc_cb::set_next_track_obj_id
```

设置下一曲目对象 ID（next track object ID）时的回调。

<a id="a5f87b5d07241b4124911be0cd6c43b37"></a>

### `set_playback_speed`

```c
bt_mcc_set_playback_speed_cb bt_mcc_cb::set_playback_speed
```

设置播放速度（playback speed）时的回调。

<a id="a00a0ba5ed665ef7fc2ca861d985ccd64"></a>

### `set_playing_order`

```c
bt_mcc_set_playing_order_cb bt_mcc_cb::set_playing_order
```

设置播放顺序（playing order）时的回调。

<a id="affa57da8f325dce8298d097af38d0d62"></a>

### `set_track_position`

```c
bt_mcc_set_track_position_cb bt_mcc_cb::set_track_position
```

设置曲目位置（track position）时的回调。

<a id="abb7769b73564a22645bfe6b11f239637"></a>

### `track_changed_ntf`

```c
bt_mcc_track_changed_ntf_cb bt_mcc_cb::track_changed_ntf
```

收到曲目已变更（track changed）通知时的回调。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/mcc.h`

## 119.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/mcc.h](https://docs.zephyrproject.org/latest/doxygen/html/mcc_8h_source.html)
- [bt_mcc_discover_mcs_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gab268faeca207e115ee1be0843ab8c342)
- [bt_mcc_read_player_name_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaa943b61848ee43e91d473f6fdd0a604f)
- [bt_mcc_read_icon_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga471d0491b70e5472e16c3035507761cc)
- [bt_mcc_read_icon_url_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaaddc4abe38f6ca811967ae6a10d8f8f0)
- [bt_mcc_track_changed_ntf_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga67611a3068284b0c7fbb3ef07dfe7688)
- [bt_mcc_read_track_title_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga6927860f1803aeade4994610da32d402)
- [bt_mcc_read_track_duration_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga7cdb524ff9c34f24c1740adb9eca072c)
- [bt_mcc_read_track_position_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga128883c867b10e57d3f2f26a708b7263)
- [bt_mcc_set_track_position_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga1167f5e2ef4a7e78469aefc0cef18bff)
- [bt_mcc_read_playback_speed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga6f5383be3f344c25361786d903640909)
- [bt_mcc_set_playback_speed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga1322f2ddbb587c70fd23a7ccfc1fc779)
- [bt_mcc_read_seeking_speed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga3089e6165e8491325f7205279bb5bb83)
- [bt_mcc_read_segments_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga1fbf0b4fd624626127774d2662083875)
- [bt_mcc_read_current_track_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga28ac116604248643b0b203b4a314b7b1)
- [bt_mcc_set_current_track_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaf0d619b493a8fb4c00278a0a85bb2529)
- [bt_mcc_read_next_track_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga83d6614d4a0808782b1b4df115b872d2)
- [bt_mcc_set_next_track_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga2f3099d097b28ab9c4abf81e19474def)
- [bt_mcc_read_current_group_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga5f21a1eed4bfe4dfbca40949af895723)
- [bt_mcc_set_current_group_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga8bbb0d28f7dcf23a30a8ca56d647ac2c)
- [bt_mcc_read_parent_group_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga48dd365aa637336b9899db4b6986a5e4)
- [bt_mcc_read_playing_order_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gafb0869e0ef5332d39070081efdacf17c)
- [bt_mcc_set_playing_order_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga1a12fb89adf29c83bca02f701213c6d7)
- [bt_mcc_read_playing_orders_supported_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gac45a2aff295535f70ac4a070e970b7a0)
- [bt_mcc_read_media_state_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga200a827f4bf5d65570ddabd028269f77)
- [bt_mcc_send_cmd_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gae4c2d1a5c41df1c3535418cc23d48f8e)
- [bt_mcc_cmd_ntf_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga50da90a5c351c99494208b44096a61c8)
- [bt_mcc_read_opcodes_supported_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gab37df36e15132b9235d1093f5aa403cc)
- [bt_mcc_send_search_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga9489c34b6006df8bd26e626030cab71f)
- [bt_mcc_search_ntf_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gab168a4c86de444dd066802c4a5fe41c3)
- [bt_mcc_read_search_results_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga5a39822a21a6f2aa7a6548c57979a926)
- [bt_mcc_read_content_control_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gadb607997fdcb3e57bbfc90790de4b927)
- [bt_mcc_otc_obj_selected_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaf186e6adefa296de4146502665d738b3)
- [bt_mcc_otc_obj_metadata_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga9805222315ca6e6df0720233055af10c)
- [bt_mcc_otc_read_icon_object_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga13bedbb573bc5575ab75fc3ae65c1870)
- [bt_mcc_otc_read_track_segments_object_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga1c4c842879cd8b209080a59d3ba125f8)
- [bt_mcc_otc_read_current_track_object_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaff887eda3b84cad1052549f23c8dcfbe)
- [bt_mcc_otc_read_next_track_object_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga920f25e04e1be4ad5f7e220c2e9102b5)
- [bt_mcc_otc_read_current_group_object_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga0b309ae7ce23834f303c39017ffa4e50)
- [bt_mcc_otc_read_parent_group_object_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaca904bacb552792ffd85c6a640f0ba48)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P118_bt_map_mse_mns_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P120_bt_micp_included_结构体.md)
