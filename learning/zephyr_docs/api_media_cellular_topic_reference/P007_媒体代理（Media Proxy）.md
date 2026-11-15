---
id: learning.zephyr-docs.api-media-cellular-topic-reference.page-7
title: 媒体代理（Media Proxy）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_媒体代理（Media Proxy）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

媒体代理模块。

<a id="details"></a>

媒体代理模块（Media Proxy Module）。自 3.0 引入，版本 0.8.0。媒体代理模块连接媒体播放器（Media Players）与媒体控制器（Media Controllers）。播放器拥有或能够访问媒体内容，知道如何浏览和播放这些内容；控制器读取或获取播放器信息，通过设置播放器参数和发送命令控制播放器。媒体代理模块允许播放器实现向控制器公开自身，也允许控制器访问任何播放器并获取其更新。它支持对本地播放器实例执行本地与远端控制：控制器可以是本地应用，也可以是转发远端媒体控制客户端（Media Control Client）请求的媒体控制服务（Media Control Service）。可以仅有本地控制、仅有远端控制、两者兼有，甚至每类都有多个实例。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.1\_数据结构（Data Structures）

<a id="r_mpl_5Fcmd"></a>

```c
struct mpl_cmd
```

相关声明：[mpl_cmd](../audio_video_model_reference/P037_mpl_cmd_结构体.md)。

媒体播放器命令（Media Player Command）。

<a id="r_mpl_5Fcmd_5Fntf"></a>

```c
struct mpl_cmd_ntf
```

相关声明：[mpl_cmd_ntf](../audio_video_model_reference/P038_mpl_cmd_ntf_结构体.md)。

媒体命令通知（Media Command Notification）。

<a id="r_mpl_5Fsci"></a>

```c
struct mpl_sci
```

相关声明：[mpl_sci](../audio_video_model_reference/P039_mpl_sci_结构体.md)。

搜索控制项（Search Control Item）。

<a id="r_mpl_5Fsearch"></a>

```c
struct mpl_search
```

相关声明：[mpl_search](../audio_video_model_reference/P040_mpl_search_结构体.md)。

搜索（Search）。

<a id="r_media_5Fproxy_5Fctrl_5Fcbs"></a>

```c
struct media_proxy_ctrl_cbs
```

相关声明：[media_proxy_ctrl_cbs](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md)。

媒体代理（Media Proxy）对控制器的回调。

<a id="r_media_5Fproxy_5Fpl_5Fcalls"></a>

```c
struct media_proxy_pl_calls
```

相关声明：[media_proxy_pl_calls](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md)。

播放器中可由媒体代理（Media Proxy）调用的接口。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.2\_宏定义（Macros）

<a id="r_ga22c2599cd62a263a01c06c9bd9fff054"></a>

```c
#define MEDIA_PROXY_OPCODES_SUPPORTED_LEN 4U
```

相关声明：[MEDIA_PROXY_OPCODES_SUPPORTED_LEN](#ga22c2599cd62a263a01c06c9bd9fff054)。

媒体播放器（Media Player）支持的操作码字段长度。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.3\_函数（Functions）

<a id="r_ga352228fb77498b61205a22b0f3a75c8e"></a>

```c
int media_proxy_ctrl_register (struct media_proxy_ctrl_cbs *ctrl_cbs)
```

相关声明：[media_proxy_ctrl_register](#ga352228fb77498b61205a22b0f3a75c8e)、[media_proxy_ctrl_cbs](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md)。

向媒体代理（media_proxy）注册控制器（Controller）。

<a id="r_ga5aaa486e0c3663e21477984e54642ed1"></a>

```c
int media_proxy_ctrl_discover_player (struct bt_conn *conn)
```

相关声明：[media_proxy_ctrl_discover_player](#ga5aaa486e0c3663e21477984e54642ed1)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

发现远端媒体播放器（Remote Media Player）。

<a id="r_ga2261222d8581ed86e91a276b13359126"></a>

```c
int media_proxy_ctrl_get_player_name (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_player_name](#ga2261222d8581ed86e91a276b13359126)。

读取媒体播放器名称（Media Player Name）。

<a id="r_gae077bc84648137460a9aeb6cfd4acb4c"></a>

```c
int media_proxy_ctrl_set_player_name (struct media_player *player, const char *name)
```

相关声明：[media_proxy_ctrl_set_player_name](#gae077bc84648137460a9aeb6cfd4acb4c)。

设置媒体播放器名称。

<a id="r_ga5efccb39cdb97eed476e0c0bff461ec1"></a>

```c
int media_proxy_ctrl_get_icon_id (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_icon_id](#ga5efccb39cdb97eed476e0c0bff461ec1)。

读取图标对象 ID（Icon Object ID）。

<a id="r_gab6df6fe71c8273eca855eb3be27290dd"></a>

```c
int media_proxy_ctrl_get_icon_url (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_icon_url](#gab6df6fe71c8273eca855eb3be27290dd)。

读取图标 URL。

<a id="r_gabfbb49e79204130cb004f217af771b80"></a>

```c
int media_proxy_ctrl_get_track_title (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_track_title](#gabfbb49e79204130cb004f217af771b80)。

读取曲目标题（Track Title）。

<a id="r_ga488441418a8f2d358092019bbfe16788"></a>

```c
int media_proxy_ctrl_get_track_duration (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_track_duration](#ga488441418a8f2d358092019bbfe16788)。

读取曲目时长（Track Duration）。

<a id="r_gae0bb75feb49a68b495150c6fba2f21a7"></a>

```c
int media_proxy_ctrl_get_track_position (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_track_position](#gae0bb75feb49a68b495150c6fba2f21a7)。

读取曲目位置（Track Position）。

<a id="r_ga776bb5f16cf1f4f6cc3842aabd86b781"></a>

```c
int media_proxy_ctrl_set_track_position (struct media_player *player, int32_t position)
```

相关声明：[media_proxy_ctrl_set_track_position](#ga776bb5f16cf1f4f6cc3842aabd86b781)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置曲目位置。

<a id="r_ga2d64a23b3f881579a603a04baeb64088"></a>

```c
int media_proxy_ctrl_get_playback_speed (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_playback_speed](#ga2d64a23b3f881579a603a04baeb64088)。

获取播放速度（Playback Speed）。

<a id="r_gabafbc857c3e6befe98e339acb58f17fb"></a>

```c
int media_proxy_ctrl_set_playback_speed (struct media_player *player, int8_t speed)
```

相关声明：[media_proxy_ctrl_set_playback_speed](#gabafbc857c3e6befe98e339acb58f17fb)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

设置播放速度。

<a id="r_ga817ca4ab611e214493fbc918036def0f"></a>

```c
int media_proxy_ctrl_get_seeking_speed (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_seeking_speed](#ga817ca4ab611e214493fbc918036def0f)。

获取搜索播放位置速度（Seeking Speed）。

<a id="r_ga1afcc097cb36c4f11141b82ce28e8126"></a>

```c
int media_proxy_ctrl_get_track_segments_id (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_track_segments_id](#ga1afcc097cb36c4f11141b82ce28e8126)。

读取当前曲目片段对象 ID（Current Track Segments Object ID）。

<a id="r_gaebe7e3683041e28bef40df75cc991dea"></a>

```c
int media_proxy_ctrl_get_current_track_id (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_current_track_id](#gaebe7e3683041e28bef40df75cc991dea)。

读取当前曲目对象 ID（Current Track Object ID）。

<a id="r_gaea6adacedaded10f7c2c0f91b7159f74"></a>

```c
int media_proxy_ctrl_set_current_track_id (struct media_player *player, uint64_t id)
```

相关声明：[media_proxy_ctrl_set_current_track_id](#gaea6adacedaded10f7c2c0f91b7159f74)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

设置当前曲目对象 ID。

<a id="r_gae32da32bd504061801730805729242e1"></a>

```c
int media_proxy_ctrl_get_next_track_id (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_next_track_id](#gae32da32bd504061801730805729242e1)。

读取下一曲目对象 ID（Next Track Object ID）。

<a id="r_ga43b797717fb9b36b94a606dfabeb0fa7"></a>

```c
int media_proxy_ctrl_set_next_track_id (struct media_player *player, uint64_t id)
```

相关声明：[media_proxy_ctrl_set_next_track_id](#ga43b797717fb9b36b94a606dfabeb0fa7)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

设置下一曲目对象 ID。

<a id="r_ga12dc878be39814660900ba875e13e537"></a>

```c
int media_proxy_ctrl_get_parent_group_id (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_parent_group_id](#ga12dc878be39814660900ba875e13e537)。

读取父分组对象 ID（Parent Group Object ID）。

<a id="r_ga2ae50a1988305b4247ff0af796b6d93e"></a>

```c
int media_proxy_ctrl_get_current_group_id (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_current_group_id](#ga2ae50a1988305b4247ff0af796b6d93e)。

读取当前分组对象 ID（Current Group Object ID）。

<a id="r_gae496885d0124f4e3fc2c0f203fcff118"></a>

```c
int media_proxy_ctrl_set_current_group_id (struct media_player *player, uint64_t id)
```

相关声明：[media_proxy_ctrl_set_current_group_id](#gae496885d0124f4e3fc2c0f203fcff118)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

设置当前分组对象 ID。

<a id="r_ga2f93bcde2460c6638880f8e6631eb68e"></a>

```c
int media_proxy_ctrl_get_playing_order (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_playing_order](#ga2f93bcde2460c6638880f8e6631eb68e)。

读取播放顺序（Playing Order）。

<a id="r_gaa4040e97100f6e70527e6ad201309bbe"></a>

```c
int media_proxy_ctrl_set_playing_order (struct media_player *player, uint8_t order)
```

相关声明：[media_proxy_ctrl_set_playing_order](#gaa4040e97100f6e70527e6ad201309bbe)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置播放顺序。

<a id="r_ga030899757b79251f1d5a1055f65fe989"></a>

```c
int media_proxy_ctrl_get_playing_orders_supported (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_playing_orders_supported](#ga030899757b79251f1d5a1055f65fe989)。

读取支持的播放顺序（Playing Orders Supported）。

<a id="r_ga9433aaf24776c30557ea694795e75b3e"></a>

```c
int media_proxy_ctrl_get_media_state (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_media_state](#ga9433aaf24776c30557ea694795e75b3e)。

读取媒体状态（Media State）。

<a id="r_ga590762e7272b99fb8ac50a7841424670"></a>

```c
int media_proxy_ctrl_send_command (struct media_player *player, const struct mpl_cmd *command)
```

相关声明：[media_proxy_ctrl_send_command](#ga590762e7272b99fb8ac50a7841424670)、[mpl_cmd](../audio_video_model_reference/P037_mpl_cmd_结构体.md)。

发送命令。

<a id="r_ga15804287093b20d4a1616380729b33c8"></a>

```c
int media_proxy_ctrl_get_commands_supported (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_commands_supported](#ga15804287093b20d4a1616380729b33c8)。

读取支持的命令（Commands Supported）。

<a id="r_ga052c3fabac4a44ee2802ddd4a6c5c9ac"></a>

```c
int media_proxy_ctrl_send_search (struct media_player *player, const struct mpl_search *search)
```

相关声明：[media_proxy_ctrl_send_search](#ga052c3fabac4a44ee2802ddd4a6c5c9ac)、[mpl_search](../audio_video_model_reference/P040_mpl_search_结构体.md)。

设置搜索（Search）。

<a id="r_ga580a0c9fa47460be59f0571ee11a41b4"></a>

```c
int media_proxy_ctrl_get_search_results_id (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_search_results_id](#ga580a0c9fa47460be59f0571ee11a41b4)。

读取搜索结果对象 ID（Search Results Object ID）。

<a id="r_ga23488e77985a04216ec7c7fa785f09fc"></a>

```c
uint8_t media_proxy_ctrl_get_content_ctrl_id (struct media_player *player)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[media_proxy_ctrl_get_content_ctrl_id](#ga23488e77985a04216ec7c7fa785f09fc)。

读取内容控制 ID（Content Control ID）。

<a id="r_gac75e27a4a5e169481723cd6b39678274"></a>

```c
int media_proxy_pl_register (struct media_proxy_pl_calls *pl_calls)
```

相关声明：[media_proxy_pl_register](#gac75e27a4a5e169481723cd6b39678274)、[media_proxy_pl_calls](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md)。

向媒体代理（Media Proxy）注册播放器（Player）。

<a id="r_gab0b10b3de5674f2172e1a2f779cbe8d5"></a>

```c
int media_proxy_pl_init (void)
```

相关声明：[media_proxy_pl_init](#gab0b10b3de5674f2172e1a2f779cbe8d5)。

初始化播放器（Player）。

<a id="r_gaf535f1ab028407432ef890d278d936e0"></a>

```c
struct bt_ots * bt_mcs_get_ots (void)
```

相关声明：[bt_ots](../bluetooth_service_model_reference/P135_bt_ots_结构体.md)、[bt_mcs_get_ots](#gaf535f1ab028407432ef890d278d936e0)。

获取媒体控制服务（Media Control Service）使用的对象传输服务（Object Transfer Service）指针。

<a id="r_ga0a70dc60a4d6acbcc58e220b75dad92a"></a>

```c
void media_proxy_pl_name_cb (const char *name)
```

相关声明：[media_proxy_pl_name_cb](#ga0a70dc60a4d6acbcc58e220b75dad92a)。

播放器名称变化回调（Player Name Changed Callback）。

<a id="r_gadd348a8d5aff193f7a9113a759e85b1d"></a>

```c
void media_proxy_pl_icon_url_cb (const char *url)
```

相关声明：[media_proxy_pl_icon_url_cb](#gadd348a8d5aff193f7a9113a759e85b1d)。

播放器图标 URL 变化回调（Player Icon URL Changed Callback）。

<a id="r_ga4a93a18cb0b75cb16828243f0d37b4b4"></a>

```c
void media_proxy_pl_track_changed_cb (void)
```

相关声明：[media_proxy_pl_track_changed_cb](#ga4a93a18cb0b75cb16828243f0d37b4b4)。

音轨变化回调（Track Changed Callback）。

<a id="r_ga9489b517e4baa215f0b7b59243cee11c"></a>

```c
void media_proxy_pl_track_title_cb (char *title)
```

相关声明：[media_proxy_pl_track_title_cb](#ga9489b517e4baa215f0b7b59243cee11c)。

音轨标题回调（Track Title Callback）。

<a id="r_ga7b0f9633a5322557b91ea97eafac9f34"></a>

```c
void media_proxy_pl_track_duration_cb (int32_t duration)
```

相关声明：[media_proxy_pl_track_duration_cb](#ga7b0f9633a5322557b91ea97eafac9f34)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

音轨时长回调（Track Duration Callback）。

<a id="r_ga61d494d7e149cfa2c3f9546c1e3b99bd"></a>

```c
void media_proxy_pl_track_position_cb (int32_t position)
```

相关声明：[media_proxy_pl_track_position_cb](#ga61d494d7e149cfa2c3f9546c1e3b99bd)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

音轨位置回调（Track Position Callback）。

<a id="r_ga17c2ca149050e1382eb556f6dcccad21"></a>

```c
void media_proxy_pl_playback_speed_cb (int8_t speed)
```

相关声明：[media_proxy_pl_playback_speed_cb](#ga17c2ca149050e1382eb556f6dcccad21)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

播放速度回调（Playback Speed Callback）。

<a id="r_gaeaf89f4b760870896ed42687562971ca"></a>

```c
void media_proxy_pl_seeking_speed_cb (int8_t speed)
```

相关声明：[media_proxy_pl_seeking_speed_cb](#gaeaf89f4b760870896ed42687562971ca)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

搜寻速度回调（Seeking Speed Callback）。

<a id="r_gadcad4efdd714159d5d9611bbf74d5fae"></a>

```c
void media_proxy_pl_current_track_id_cb (uint64_t id)
```

相关声明：[media_proxy_pl_current_track_id_cb](#gadcad4efdd714159d5d9611bbf74d5fae)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

当前音轨对象 ID 回调（Current Track Object ID Callback）。

<a id="r_gaf0bd3447e64b6128710c07461766a0c9"></a>

```c
void media_proxy_pl_next_track_id_cb (uint64_t id)
```

相关声明：[media_proxy_pl_next_track_id_cb](#gaf0bd3447e64b6128710c07461766a0c9)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

下一音轨对象 ID 回调（Next Track Object ID Callback）。

<a id="r_ga64730f46b87cf9089aff65b6be12f42d"></a>

```c
void media_proxy_pl_parent_group_id_cb (uint64_t id)
```

相关声明：[media_proxy_pl_parent_group_id_cb](#ga64730f46b87cf9089aff65b6be12f42d)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

父组对象 ID 回调（Parent Group Object ID Callback）。

<a id="r_gad02f2924e1aa765c04cbbc6441e7d063"></a>

```c
void media_proxy_pl_current_group_id_cb (uint64_t id)
```

相关声明：[media_proxy_pl_current_group_id_cb](#gad02f2924e1aa765c04cbbc6441e7d063)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

当前组对象 ID 回调（Current Group Object ID Callback）。

<a id="r_ga96e8156b0267f3d55ee52ab307d81985"></a>

```c
void media_proxy_pl_playing_order_cb (uint8_t order)
```

相关声明：[media_proxy_pl_playing_order_cb](#ga96e8156b0267f3d55ee52ab307d81985)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

播放顺序回调（Playing Order Callback）。

<a id="r_ga842d7951a04702d6f819de44c47b9cac"></a>

```c
void media_proxy_pl_media_state_cb (uint8_t state)
```

相关声明：[media_proxy_pl_media_state_cb](#ga842d7951a04702d6f819de44c47b9cac)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

媒体状态回调（Media State Callback）。

<a id="r_ga694e83401835149833024cf094b98cd1"></a>

```c
void media_proxy_pl_command_cb (const struct mpl_cmd_ntf *cmd_ntf)
```

相关声明：[media_proxy_pl_command_cb](#ga694e83401835149833024cf094b98cd1)、[mpl_cmd_ntf](../audio_video_model_reference/P038_mpl_cmd_ntf_结构体.md)。

命令回调（Command Callback）。

<a id="r_ga70ea8a24a4e853a191e0947e1c2d1145"></a>

```c
void media_proxy_pl_commands_supported_cb (uint32_t opcodes)
```

相关声明：[media_proxy_pl_commands_supported_cb](#ga70ea8a24a4e853a191e0947e1c2d1145)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

支持的命令回调（Commands Supported Callback）。

<a id="r_ga8c0d75f61120047bacd0b933534e1b41"></a>

```c
void media_proxy_pl_search_cb (uint8_t result_code)
```

相关声明：[media_proxy_pl_search_cb](#ga8c0d75f61120047bacd0b933534e1b41)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

搜索回调（Search Callback）。

<a id="r_ga35896de266f2a2bd101279e4ce9900c7"></a>

```c
void media_proxy_pl_search_results_id_cb (uint64_t id)
```

相关声明：[media_proxy_pl_search_results_id_cb](#ga35896de266f2a2bd101279e4ce9900c7)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

搜索结果对象 ID 回调（Search Results Object ID Callback）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 7.4\_播放速度参数（Playback speed parameters）

允许 -128 到 127 的所有值，这里仅定义其中一部分。

<a id="r_ga61732644eecad1442d5cedbda8f8cc08"></a>

```c
#define MEDIA_PROXY_PLAYBACK_SPEED_MIN -128
```

相关声明：[MEDIA_PROXY_PLAYBACK_SPEED_MIN](#ga61732644eecad1442d5cedbda8f8cc08)。

最低播放速度（Minimum Playback Speed），对应 25% 速度。

<a id="r_ga5462f8d5ce98cc33a131b2e7b5548c41"></a>

```c
#define MEDIA_PROXY_PLAYBACK_SPEED_QUARTER -128
```

相关声明：[MEDIA_PROXY_PLAYBACK_SPEED_QUARTER](#ga5462f8d5ce98cc33a131b2e7b5548c41)。

四分之一播放速度（Quarter Playback Speed），对应 25% 速度。

<a id="r_ga4c765363c2a5b0d9800864859746ae33"></a>

```c
#define MEDIA_PROXY_PLAYBACK_SPEED_HALF -64
```

相关声明：[MEDIA_PROXY_PLAYBACK_SPEED_HALF](#ga4c765363c2a5b0d9800864859746ae33)。

半速播放（Half Playback Speed），对应 50% 速度。

<a id="r_ga6d8854bd54dcbb657f0ba545ec231368"></a>

```c
#define MEDIA_PROXY_PLAYBACK_SPEED_UNITY 0
```

相关声明：[MEDIA_PROXY_PLAYBACK_SPEED_UNITY](#ga6d8854bd54dcbb657f0ba545ec231368)。

一倍播放速度（Unity Playback Speed），对应 100% 速度。

<a id="r_gaa53d906340c0b2adb314945f5299464e"></a>

```c
#define MEDIA_PROXY_PLAYBACK_SPEED_DOUBLE 64
```

相关声明：[MEDIA_PROXY_PLAYBACK_SPEED_DOUBLE](#gaa53d906340c0b2adb314945f5299464e)。

双倍播放速度（Double Playback Speed），对应 200% 速度。

<a id="r_gaaccc9d75f96b5fe2de101b119a516d36"></a>

```c
#define MEDIA_PROXY_PLAYBACK_SPEED_MAX 127
```

相关声明：[MEDIA_PROXY_PLAYBACK_SPEED_MAX](#gaaccc9d75f96b5fe2de101b119a516d36)。

最高播放速度（Max Playback Speed），对应 395.7% 速度，接近 400%。

## 7.5\_搜寻速度因子（Seeking speed factors）

搜寻速度（Seeking Speed）的允许值为 -64 到 -4（含端点）、0，以及 4 到 64（含端点）。

<a id="r_gaa6aa7a6e98631152b4bd77b60c78d58a"></a>

```c
#define MEDIA_PROXY_SEEKING_SPEED_FACTOR_MAX 64
```

相关声明：[MEDIA_PROXY_SEEKING_SPEED_FACTOR_MAX](#gaa6aa7a6e98631152b4bd77b60c78d58a)。

最大搜寻速度（Maximum Seeking Speed），可取负值。

<a id="r_ga67c1069fa01425ad6cd8f36438b71826"></a>

```c
#define MEDIA_PROXY_SEEKING_SPEED_FACTOR_MIN 4
```

相关声明：[MEDIA_PROXY_SEEKING_SPEED_FACTOR_MIN](#ga67c1069fa01425ad6cd8f36438b71826)。

最小搜寻速度（Minimum Seeking Speed），可取负值。

<a id="r_ga58495e58bf84235efcee89289fc992c2"></a>

```c
#define MEDIA_PROXY_SEEKING_SPEED_FACTOR_ZERO 0
```

相关声明：[MEDIA_PROXY_SEEKING_SPEED_FACTOR_ZERO](#ga58495e58bf84235efcee89289fc992c2)。

不搜寻（No Seeking）。

## 7.6\_播放顺序（Playing orders）

<a id="r_ga8e721b49c361d2395bd8eb740d43e282"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDER_SINGLE_ONCE 0x01U
```

相关声明：[MEDIA_PROXY_PLAYING_ORDER_SINGLE_ONCE](#ga8e721b49c361d2395bd8eb740d43e282)。

单个音轨（Track）播放一次，没有下一音轨。

<a id="r_gadf5f0c15cb88cd92f49db1b57dbd2c18"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDER_SINGLE_REPEAT 0x02U
```

相关声明：[MEDIA_PROXY_PLAYING_ORDER_SINGLE_REPEAT](#gadf5f0c15cb88cd92f49db1b57dbd2c18)。

重复播放单个音轨（Track），下一音轨就是当前音轨。

<a id="r_ga63055a150b93f06e076b97abb6f6f682"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDER_INORDER_ONCE 0x03U
```

相关声明：[MEDIA_PROXY_PLAYING_ORDER_INORDER_ONCE](#ga63055a150b93f06e076b97abb6f6f682)。

按音轨顺序（Track Order）将组内音轨播放一次。

<a id="r_ga437068b9d90404cc68d41faaedfac9a8"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDER_INORDER_REPEAT 0x04U
```

相关声明：[MEDIA_PROXY_PLAYING_ORDER_INORDER_REPEAT](#ga437068b9d90404cc68d41faaedfac9a8)。

按音轨顺序（Track Order）重复播放组内音轨。

<a id="r_ga48a33dd8fbb8a8ab162c18bc0e9b7531"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDER_OLDEST_ONCE 0x05U
```

相关声明：[MEDIA_PROXY_PLAYING_ORDER_OLDEST_ONCE](#ga48a33dd8fbb8a8ab162c18bc0e9b7531)。

从最旧音轨开始，将组内音轨播放一次（Oldest First）。

<a id="r_ga63a33c4e3267ab39ab5892fb5b0bbe89"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDER_OLDEST_REPEAT 0x06U
```

相关声明：[MEDIA_PROXY_PLAYING_ORDER_OLDEST_REPEAT](#ga63a33c4e3267ab39ab5892fb5b0bbe89)。

从最旧音轨开始，重复播放组内音轨（Oldest First）。

<a id="r_gac344111e2b043cdfbcb9ac272622b16f"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDER_NEWEST_ONCE 0x07U
```

相关声明：[MEDIA_PROXY_PLAYING_ORDER_NEWEST_ONCE](#gac344111e2b043cdfbcb9ac272622b16f)。

从最新音轨开始，将组内音轨播放一次（Newest First）。

<a id="r_gaf10b815dc579dc67b1f092e0a85c51d9"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDER_NEWEST_REPEAT 0x08U
```

相关声明：[MEDIA_PROXY_PLAYING_ORDER_NEWEST_REPEAT](#gaf10b815dc579dc67b1f092e0a85c51d9)。

从最新音轨开始，重复播放组内音轨（Newest First）。

<a id="r_gae152374af5d567cf65d6d7b236b792a4"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDER_SHUFFLE_ONCE 0x09U
```

相关声明：[MEDIA_PROXY_PLAYING_ORDER_SHUFFLE_ONCE](#gae152374af5d567cf65d6d7b236b792a4)。

以随机顺序（Random Order）将组内音轨播放一次。

<a id="r_ga45161ec08b67e4d3bd59efa45027f3aa"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDER_SHUFFLE_REPEAT 0x0AU
```

相关声明：[MEDIA_PROXY_PLAYING_ORDER_SHUFFLE_REPEAT](#ga45161ec08b67e4d3bd59efa45027f3aa)。

以随机顺序（Random Order）重复播放组内音轨。

## 7.7\_支持的播放顺序（Playing orders supported）

位图（Bitmap），其顺序与上文的播放顺序相同。

注意，播放顺序（Playing Order）1 对应位 0，依此类推。

<a id="r_ga55b5a00ea9ec849e7c495463e5f1869d"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SINGLE_ONCE BIT(0U)
```

相关声明：[MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SINGLE_ONCE](#ga55b5a00ea9ec849e7c495463e5f1869d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

单个音轨（Track）播放一次，没有下一音轨。

<a id="r_ga465a82ace21a0e88356eccaf038f58e9"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SINGLE_REPEAT BIT(1U)
```

相关声明：[MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SINGLE_REPEAT](#ga465a82ace21a0e88356eccaf038f58e9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

重复播放单个音轨（Track），下一音轨就是当前音轨。

<a id="r_ga8fee464b8e17fffc4361972df15062af"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_INORDER_ONCE BIT(2U)
```

相关声明：[MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_INORDER_ONCE](#ga8fee464b8e17fffc4361972df15062af)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

按音轨顺序（Track Order）将组内音轨播放一次。

<a id="r_ga7faeff14de245ea670ca447b0adc4820"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_INORDER_REPEAT BIT(3U)
```

相关声明：[MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_INORDER_REPEAT](#ga7faeff14de245ea670ca447b0adc4820)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

按音轨顺序（Track Order）重复播放组内音轨。

<a id="r_gae3d848fc0b9117fe9bc51327627ac635"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_OLDEST_ONCE BIT(4U)
```

相关声明：[MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_OLDEST_ONCE](#gae3d848fc0b9117fe9bc51327627ac635)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

从最旧音轨开始，将组内音轨播放一次（Oldest First）。

<a id="r_ga7fa415d845dd1fefc8bdb74532878131"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_OLDEST_REPEAT BIT(5U)
```

相关声明：[MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_OLDEST_REPEAT](#ga7fa415d845dd1fefc8bdb74532878131)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

从最旧音轨开始，重复播放组内音轨（Oldest First）。

<a id="r_ga334f9e16ea7a52bfb6357ad619e3601b"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_NEWEST_ONCE BIT(6U)
```

相关声明：[MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_NEWEST_ONCE](#ga334f9e16ea7a52bfb6357ad619e3601b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

从最新音轨开始，将组内音轨播放一次（Newest First）。

<a id="r_gaaf5f08e2dd624e2bb1bd9b72ab4b2b33"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_NEWEST_REPEAT BIT(7U)
```

相关声明：[MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_NEWEST_REPEAT](#gaaf5f08e2dd624e2bb1bd9b72ab4b2b33)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

从最新音轨开始，重复播放组内音轨（Newest First）。

<a id="r_ga3e998cda3e91f1c9fbb8496a748bcf12"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SHUFFLE_ONCE BIT(8U)
```

相关声明：[MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SHUFFLE_ONCE](#ga3e998cda3e91f1c9fbb8496a748bcf12)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

以随机顺序（Random Order）将组内音轨播放一次。

<a id="r_ga4f0689fe1fc0ac2b3f9b9ef4ed1afb8b"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SHUFFLE_REPEAT BIT(9U)
```

相关声明：[MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SHUFFLE_REPEAT](#ga4f0689fe1fc0ac2b3f9b9ef4ed1afb8b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

以随机顺序（Random Order）重复播放组内音轨。

## 7.8\_媒体播放器状态（Media player states）

<a id="r_gab8c465e0e63898e53c39171b89d668c9"></a>

```c
#define MEDIA_PROXY_STATE_INACTIVE 0x00U
```

相关声明：[MEDIA_PROXY_STATE_INACTIVE](#gab8c465e0e63898e53c39171b89d668c9)。

当前音轨无效，且未选择任何音轨（Track）。

<a id="r_ga1967c76b290f1d20515740cf7139f49c"></a>

```c
#define MEDIA_PROXY_STATE_PLAYING 0x01U
```

相关声明：[MEDIA_PROXY_STATE_PLAYING](#ga1967c76b290f1d20515740cf7139f49c)。

媒体播放器（Media Player）正在播放当前音轨。

<a id="r_ga85325d7ff75ec05275a875d7d5540a6c"></a>

```c
#define MEDIA_PROXY_STATE_PAUSED 0x02U
```

相关声明：[MEDIA_PROXY_STATE_PAUSED](#ga85325d7ff75ec05275a875d7d5540a6c)。

当前音轨已暂停（Paused）。

<a id="r_gaa207ee7666ab18c40e5b1d2a6ed7f034"></a>

```c
#define MEDIA_PROXY_STATE_SEEKING 0x03U
```

相关声明：[MEDIA_PROXY_STATE_SEEKING](#gaa207ee7666ab18c40e5b1d2a6ed7f034)。

当前音轨正在快进或快退（Fast Forwarding / Fast Rewinding）。

<a id="r_gab0c8f3510109f18ef6445f035b27cbe9"></a>

```c
#define MEDIA_PROXY_STATE_LAST 0x04U
```

相关声明：[MEDIA_PROXY_STATE_LAST](#gab0c8f3510109f18ef6445f035b27cbe9)。

内部用作最后一个状态值（Last State Value）。

## 7.9\_媒体播放器命令操作码（Media player command opcodes）

<a id="r_gadd400bc6900abe1956d4de4efb212683"></a>

```c
#define MEDIA_PROXY_OP_PLAY 0x01U
```

相关声明：[MEDIA_PROXY_OP_PLAY](#gadd400bc6900abe1956d4de4efb212683)。

开始播放当前音轨（Track）。

<a id="r_ga69bcb42294e8cd1eb062bbe19399a3df"></a>

```c
#define MEDIA_PROXY_OP_PAUSE 0x02U
```

相关声明：[MEDIA_PROXY_OP_PAUSE](#ga69bcb42294e8cd1eb062bbe19399a3df)。

暂停播放当前音轨（Track）。

<a id="r_gabc2b497b95728325208e28db6d5cf4f8"></a>

```c
#define MEDIA_PROXY_OP_FAST_REWIND 0x03U
```

相关声明：[MEDIA_PROXY_OP_FAST_REWIND](#gabc2b497b95728325208e28db6d5cf4f8)。

快退（Fast Rewind）当前音轨。

<a id="r_gac0c0730bcf6592c5d2c61d21d09efb2b"></a>

```c
#define MEDIA_PROXY_OP_FAST_FORWARD 0x04U
```

相关声明：[MEDIA_PROXY_OP_FAST_FORWARD](#gac0c0730bcf6592c5d2c61d21d09efb2b)。

快进（Fast Forward）当前音轨。

<a id="r_gaf3707d44c7a3305ba896c0257b2109b3"></a>

```c
#define MEDIA_PROXY_OP_STOP 0x05U
```

相关声明：[MEDIA_PROXY_OP_STOP](#gaf3707d44c7a3305ba896c0257b2109b3)。

停止当前活动，回到暂停状态（Paused State），并将当前音轨位置设为当前音轨起点。

<a id="r_gaceb240f7f21074b6b7f9ed1e9d645cb0"></a>

```c
#define MEDIA_PROXY_OP_MOVE_RELATIVE 0x10U
```

相关声明：[MEDIA_PROXY_OP_MOVE_RELATIVE](#gaceb240f7f21074b6b7f9ed1e9d645cb0)。

相对于当前音轨位置（Current Track Position），设置新的当前位置。

<a id="r_ga7846fa5da200e0d921056b410e60677e"></a>

```c
#define MEDIA_PROXY_OP_PREV_SEGMENT 0x20U
```

相关声明：[MEDIA_PROXY_OP_PREV_SEGMENT](#ga7846fa5da200e0d921056b410e60677e)。

将当前音轨位置设为当前音轨上一段（Previous Segment）的起始位置。

<a id="r_gada5e3114b2b00f4ea27adf884f49429e"></a>

```c
#define MEDIA_PROXY_OP_NEXT_SEGMENT 0x21U
```

相关声明：[MEDIA_PROXY_OP_NEXT_SEGMENT](#gada5e3114b2b00f4ea27adf884f49429e)。

将当前音轨位置设为当前音轨下一段（Next Segment）的起始位置。

<a id="r_gac2e5c8e2cadd05092fa186f05ae74e57"></a>

```c
#define MEDIA_PROXY_OP_FIRST_SEGMENT 0x22U
```

相关声明：[MEDIA_PROXY_OP_FIRST_SEGMENT](#gac2e5c8e2cadd05092fa186f05ae74e57)。

将当前音轨位置设为当前音轨第一段（First Segment）的起始位置。

<a id="r_ga3f317208b9d8495c498325a4d37d41ad"></a>

```c
#define MEDIA_PROXY_OP_LAST_SEGMENT 0x23U
```

相关声明：[MEDIA_PROXY_OP_LAST_SEGMENT](#ga3f317208b9d8495c498325a4d37d41ad)。

将当前音轨位置设为当前音轨最后一段（Last Segment）的起始位置。

<a id="r_gab3bbf7eb7c562bc6a5148c75eb99ada5"></a>

```c
#define MEDIA_PROXY_OP_GOTO_SEGMENT 0x24U
```

相关声明：[MEDIA_PROXY_OP_GOTO_SEGMENT](#gab3bbf7eb7c562bc6a5148c75eb99ada5)。

将当前音轨位置设为当前音轨第 n 段（Nth Segment）的起始位置。

<a id="r_ga1b7db568fc3153c29ed4e951d95bee8e"></a>

```c
#define MEDIA_PROXY_OP_PREV_TRACK 0x30U
```

相关声明：[MEDIA_PROXY_OP_PREV_TRACK](#ga1b7db568fc3153c29ed4e951d95bee8e)。

按播放顺序（Playing Order）将当前音轨设为上一音轨。

<a id="r_gaae4cc32663f02bf96d1dcbbc8453e40b"></a>

```c
#define MEDIA_PROXY_OP_NEXT_TRACK 0x31U
```

相关声明：[MEDIA_PROXY_OP_NEXT_TRACK](#gaae4cc32663f02bf96d1dcbbc8453e40b)。

按播放顺序（Playing Order）将当前音轨设为下一音轨。

<a id="r_ga5c272e2e9b24ce92a7df7373d1b002cc"></a>

```c
#define MEDIA_PROXY_OP_FIRST_TRACK 0x32U
```

相关声明：[MEDIA_PROXY_OP_FIRST_TRACK](#ga5c272e2e9b24ce92a7df7373d1b002cc)。

按播放顺序（Playing Order）将当前音轨设为第一音轨。

<a id="r_ga72614d9a2fa4c938f1c7055bc219c8bc"></a>

```c
#define MEDIA_PROXY_OP_LAST_TRACK 0x33U
```

相关声明：[MEDIA_PROXY_OP_LAST_TRACK](#ga72614d9a2fa4c938f1c7055bc219c8bc)。

按播放顺序（Playing Order）将当前音轨设为最后一音轨。

<a id="r_gaf2f100d41413b14c5dbd8f2641a13bb0"></a>

```c
#define MEDIA_PROXY_OP_GOTO_TRACK 0x34U
```

相关声明：[MEDIA_PROXY_OP_GOTO_TRACK](#gaf2f100d41413b14c5dbd8f2641a13bb0)。

按播放顺序（Playing Order）将当前音轨设为第 n 个音轨。

<a id="r_gae15386adcfe1c5ca56eac7d0292dffd0"></a>

```c
#define MEDIA_PROXY_OP_PREV_GROUP 0x40U
```

相关声明：[MEDIA_PROXY_OP_PREV_GROUP](#gae15386adcfe1c5ca56eac7d0292dffd0)。

将当前组设为组序列（Sequence of Groups）中的上一组。

<a id="r_ga3cf10acf1ef8b7d3252eb37cb4e35f97"></a>

```c
#define MEDIA_PROXY_OP_NEXT_GROUP 0x41U
```

相关声明：[MEDIA_PROXY_OP_NEXT_GROUP](#ga3cf10acf1ef8b7d3252eb37cb4e35f97)。

将当前组设为组序列（Sequence of Groups）中的下一组。

<a id="r_ga5eb0a22c257e370cd76d73f7fa9e342c"></a>

```c
#define MEDIA_PROXY_OP_FIRST_GROUP 0x42U
```

相关声明：[MEDIA_PROXY_OP_FIRST_GROUP](#ga5eb0a22c257e370cd76d73f7fa9e342c)。

将当前组设为组序列（Sequence of Groups）中的第一组。

<a id="r_gaa6ac8f8bf674c0ffec22bd061e9be3dc"></a>

```c
#define MEDIA_PROXY_OP_LAST_GROUP 0x43U
```

相关声明：[MEDIA_PROXY_OP_LAST_GROUP](#gaa6ac8f8bf674c0ffec22bd061e9be3dc)。

将当前组设为组序列（Sequence of Groups）中的最后一组。

<a id="r_ga139d2ced243a6ff47d8335583974a0da"></a>

```c
#define MEDIA_PROXY_OP_GOTO_GROUP 0x44U
```

相关声明：[MEDIA_PROXY_OP_GOTO_GROUP](#ga139d2ced243a6ff47d8335583974a0da)。

将当前组设为组序列（Sequence of Groups）中的第 n 组。

<a id="r_gafe30bb1287b9a44655d76364d4832eac"></a>

```c
#define MEDIA_PROXY_OP_SUP_PLAY BIT(0U)
```

相关声明：[MEDIA_PROXY_OP_SUP_PLAY](#gafe30bb1287b9a44655d76364d4832eac)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

媒体播放器支持的命令操作码（Supported Command Opcodes）。

<a id="r_gaec37a692c28ca90c8053db9de2a6c44f"></a>

```c
#define MEDIA_PROXY_OP_SUP_PAUSE BIT(1U)
```

相关声明：[MEDIA_PROXY_OP_SUP_PAUSE](#gaec37a692c28ca90c8053db9de2a6c44f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持暂停操作码（Pause Opcode）。

<a id="r_ga99952473bafd76f6ceaf141307510f28"></a>

```c
#define MEDIA_PROXY_OP_SUP_FAST_REWIND BIT(2U)
```

相关声明：[MEDIA_PROXY_OP_SUP_FAST_REWIND](#ga99952473bafd76f6ceaf141307510f28)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持快退操作码（Fast Rewind Opcode）。

<a id="r_ga05453105bc3d1579110e908b794e3ac5"></a>

```c
#define MEDIA_PROXY_OP_SUP_FAST_FORWARD BIT(3U)
```

相关声明：[MEDIA_PROXY_OP_SUP_FAST_FORWARD](#ga05453105bc3d1579110e908b794e3ac5)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持快进操作码（Fast Forward Opcode）。

<a id="r_ga060ff676a0b2f249a26aaf61147b68e8"></a>

```c
#define MEDIA_PROXY_OP_SUP_STOP BIT(4U)
```

相关声明：[MEDIA_PROXY_OP_SUP_STOP](#ga060ff676a0b2f249a26aaf61147b68e8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持停止操作码（Stop Opcode）。

<a id="r_ga03c393a29c68529e4dd9038e3947468b"></a>

```c
#define MEDIA_PROXY_OP_SUP_MOVE_RELATIVE BIT(5U)
```

相关声明：[MEDIA_PROXY_OP_SUP_MOVE_RELATIVE](#ga03c393a29c68529e4dd9038e3947468b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持相对移动操作码（Move Relative Opcode）。

<a id="r_ga3d39700e21cbdf2906321c8899e0b626"></a>

```c
#define MEDIA_PROXY_OP_SUP_PREV_SEGMENT BIT(6U)
```

相关声明：[MEDIA_PROXY_OP_SUP_PREV_SEGMENT](#ga3d39700e21cbdf2906321c8899e0b626)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持上一段操作码（Previous Segment Opcode）。

<a id="r_ga26ae64ece06a1f6f8dd7eb2c9965a4b6"></a>

```c
#define MEDIA_PROXY_OP_SUP_NEXT_SEGMENT BIT(7U)
```

相关声明：[MEDIA_PROXY_OP_SUP_NEXT_SEGMENT](#ga26ae64ece06a1f6f8dd7eb2c9965a4b6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持下一段操作码（Next Segment Opcode）。

<a id="r_ga916ce95086dfeb127e124a8c5d530371"></a>

```c
#define MEDIA_PROXY_OP_SUP_FIRST_SEGMENT BIT(8U)
```

相关声明：[MEDIA_PROXY_OP_SUP_FIRST_SEGMENT](#ga916ce95086dfeb127e124a8c5d530371)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持第一段操作码（First Segment Opcode）。

<a id="r_gaf193ea0b4a34e3981f2f45d3b9c228a2"></a>

```c
#define MEDIA_PROXY_OP_SUP_LAST_SEGMENT BIT(9U)
```

相关声明：[MEDIA_PROXY_OP_SUP_LAST_SEGMENT](#gaf193ea0b4a34e3981f2f45d3b9c228a2)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持最后一段操作码（Last Segment Opcode）。

<a id="r_ga7af591de387958f5c187ba8d0e834247"></a>

```c
#define MEDIA_PROXY_OP_SUP_GOTO_SEGMENT BIT(10U)
```

相关声明：[MEDIA_PROXY_OP_SUP_GOTO_SEGMENT](#ga7af591de387958f5c187ba8d0e834247)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持转到指定段操作码（Goto Segment Opcode）。

<a id="r_gafe8bab8f90281e5894e5f79f32449e63"></a>

```c
#define MEDIA_PROXY_OP_SUP_PREV_TRACK BIT(11U)
```

相关声明：[MEDIA_PROXY_OP_SUP_PREV_TRACK](#gafe8bab8f90281e5894e5f79f32449e63)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持上一音轨操作码（Previous Track Opcode）。

<a id="r_gafc061bc953b0338aded4cef681f9e963"></a>

```c
#define MEDIA_PROXY_OP_SUP_NEXT_TRACK BIT(12U)
```

相关声明：[MEDIA_PROXY_OP_SUP_NEXT_TRACK](#gafc061bc953b0338aded4cef681f9e963)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持下一音轨操作码（Next Track Opcode）。

<a id="r_ga6e1d53fedf09bd95bcf112495dcfd64f"></a>

```c
#define MEDIA_PROXY_OP_SUP_FIRST_TRACK BIT(13U)
```

相关声明：[MEDIA_PROXY_OP_SUP_FIRST_TRACK](#ga6e1d53fedf09bd95bcf112495dcfd64f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持第一音轨操作码（First Track Opcode）。

<a id="r_gaf43188bb438b9a766d07cd2fa900e079"></a>

```c
#define MEDIA_PROXY_OP_SUP_LAST_TRACK BIT(14U)
```

相关声明：[MEDIA_PROXY_OP_SUP_LAST_TRACK](#gaf43188bb438b9a766d07cd2fa900e079)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持最后音轨操作码（Last Track Opcode）。

<a id="r_gad2364a0ef8c54bd9fa3372edddae32b0"></a>

```c
#define MEDIA_PROXY_OP_SUP_GOTO_TRACK BIT(15U)
```

相关声明：[MEDIA_PROXY_OP_SUP_GOTO_TRACK](#gad2364a0ef8c54bd9fa3372edddae32b0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持转到指定音轨操作码（Goto Track Opcode）。

<a id="r_ga496060d673b48e045a5a2a57aa82bddc"></a>

```c
#define MEDIA_PROXY_OP_SUP_PREV_GROUP BIT(16U)
```

相关声明：[MEDIA_PROXY_OP_SUP_PREV_GROUP](#ga496060d673b48e045a5a2a57aa82bddc)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持上一组操作码（Previous Group Opcode）。

<a id="r_ga324dae538f28e818eea79c83aaa0b22c"></a>

```c
#define MEDIA_PROXY_OP_SUP_NEXT_GROUP BIT(17U)
```

相关声明：[MEDIA_PROXY_OP_SUP_NEXT_GROUP](#ga324dae538f28e818eea79c83aaa0b22c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持下一组操作码（Next Group Opcode）。

<a id="r_ga716af4c6eb702729ec4f9ff9ccc49b32"></a>

```c
#define MEDIA_PROXY_OP_SUP_FIRST_GROUP BIT(18U)
```

相关声明：[MEDIA_PROXY_OP_SUP_FIRST_GROUP](#ga716af4c6eb702729ec4f9ff9ccc49b32)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持第一组操作码（First Group Opcode）。

<a id="r_gac944825600367a41e8213dfd9de569a3"></a>

```c
#define MEDIA_PROXY_OP_SUP_LAST_GROUP BIT(19U)
```

相关声明：[MEDIA_PROXY_OP_SUP_LAST_GROUP](#gac944825600367a41e8213dfd9de569a3)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持最后一组操作码（Last Group Opcode）。

<a id="r_gaec8b6d2d684c81b9da9fee870e0258c2"></a>

```c
#define MEDIA_PROXY_OP_SUP_GOTO_GROUP BIT(20U)
```

相关声明：[MEDIA_PROXY_OP_SUP_GOTO_GROUP](#gaec8b6d2d684c81b9da9fee870e0258c2)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持转到指定组操作码（Goto Group Opcode）。

## 7.10\_媒体播放器命令结果码（Media player command result codes）

<a id="r_gaa56458b11f4cb78f1265ea8538774108"></a>

```c
#define MEDIA_PROXY_CMD_SUCCESS 0x01U
```

相关声明：[MEDIA_PROXY_CMD_SUCCESS](#gaa56458b11f4cb78f1265ea8538774108)。

写入操作码（Opcode Write）所请求的动作已成功完成。

<a id="r_ga1637459cd6eaf9d4d63a04d1facc29b7"></a>

```c
#define MEDIA_PROXY_CMD_NOT_SUPPORTED 0x02U
```

相关声明：[MEDIA_PROXY_CMD_NOT_SUPPORTED](#ga1637459cd6eaf9d4d63a04d1facc29b7)。

写入媒体控制点（Media Control Point）时使用了无效或不支持的操作码。

<a id="r_ga7d0595796a80348b570add74c6dfa14e"></a>

```c
#define MEDIA_PROXY_CMD_PLAYER_INACTIVE 0x03U
```

相关声明：[MEDIA_PROXY_CMD_PLAYER_INACTIVE](#ga7d0595796a80348b570add74c6dfa14e)。

收到操作码时，媒体播放器状态（Media Player State）特征值为非活动（Inactive）；或执行该操作码所请求动作的结果，使该特征值变为 Inactive。

<a id="r_gaf2c68cb2ac32973b85594660d43688dd"></a>

```c
#define MEDIA_PROXY_CMD_CANNOT_BE_COMPLETED 0x04U
```

相关声明：[MEDIA_PROXY_CMD_CANNOT_BE_COMPLETED](#gaf2c68cb2ac32973b85594660d43688dd)。

由于播放器内部的某种条件，无法成功完成任何媒体控制点写入（Media Control Point Write）所请求的动作。

## 7.11\_搜索操作类型值（Search operation type values）

<a id="r_ga8be6fd8d9bb08836bea1c3f0d2e577ea"></a>

```c
#define MEDIA_PROXY_SEARCH_TYPE_TRACK_NAME 0x01U
```

相关声明：[MEDIA_PROXY_SEARCH_TYPE_TRACK_NAME](#ga8be6fd8d9bb08836bea1c3f0d2e577ea)。

按音轨名称（Track Name）搜索。

<a id="r_gaf0dbc19f843a444076d8886b1a05709b"></a>

```c
#define MEDIA_PROXY_SEARCH_TYPE_ARTIST_NAME 0x02U
```

相关声明：[MEDIA_PROXY_SEARCH_TYPE_ARTIST_NAME](#gaf0dbc19f843a444076d8886b1a05709b)。

按艺人名称（Artist Name）搜索。

<a id="r_ga1f0fb19dea467e90afd670ed9af0c092"></a>

```c
#define MEDIA_PROXY_SEARCH_TYPE_ALBUM_NAME 0x03U
```

相关声明：[MEDIA_PROXY_SEARCH_TYPE_ALBUM_NAME](#ga1f0fb19dea467e90afd670ed9af0c092)。

按专辑名称（Album Name）搜索。

<a id="r_gaca10de7253c1cdcf5e0c6544de33c116"></a>

```c
#define MEDIA_PROXY_SEARCH_TYPE_GROUP_NAME 0x04U
```

相关声明：[MEDIA_PROXY_SEARCH_TYPE_GROUP_NAME](#gaca10de7253c1cdcf5e0c6544de33c116)。

按组名称（Group Name）搜索。

<a id="r_ga28b1d7de2174e3714786cb369232f339"></a>

```c
#define MEDIA_PROXY_SEARCH_TYPE_EARLIEST_YEAR 0x05U
```

相关声明：[MEDIA_PROXY_SEARCH_TYPE_EARLIEST_YEAR](#ga28b1d7de2174e3714786cb369232f339)。

按最早年份（Earliest Year）搜索。

<a id="r_ga01fb087af00bf492d19cc19adcaa9dea"></a>

```c
#define MEDIA_PROXY_SEARCH_TYPE_LATEST_YEAR 0x06U
```

相关声明：[MEDIA_PROXY_SEARCH_TYPE_LATEST_YEAR](#ga01fb087af00bf492d19cc19adcaa9dea)。

按最晚年份（Latest Year）搜索。

<a id="r_ga55c3a003881a75ce964e23fc3b0cea8e"></a>

```c
#define MEDIA_PROXY_SEARCH_TYPE_GENRE 0x07U
```

相关声明：[MEDIA_PROXY_SEARCH_TYPE_GENRE](#ga55c3a003881a75ce964e23fc3b0cea8e)。

按流派（Genre）搜索。

<a id="r_gad758e14fbe978ffd95364a6fb27eab40"></a>

```c
#define MEDIA_PROXY_SEARCH_TYPE_ONLY_TRACKS 0x08U
```

相关声明：[MEDIA_PROXY_SEARCH_TYPE_ONLY_TRACKS](#gad758e14fbe978ffd95364a6fb27eab40)。

仅搜索音轨（Tracks）。

<a id="r_ga25270f6c90daaace6a80f3255aaaf7fd"></a>

```c
#define MEDIA_PROXY_SEARCH_TYPE_ONLY_GROUPS 0x09U
```

相关声明：[MEDIA_PROXY_SEARCH_TYPE_ONLY_GROUPS](#ga25270f6c90daaace6a80f3255aaaf7fd)。

仅搜索组（Groups）。

## 7.12\_搜索通知结果码（Search notification result codes）

<a id="r_ga2627f632efab868adddeebb59243497c"></a>

```c
#define MEDIA_PROXY_SEARCH_SUCCESS 0x01U
```

相关声明：[MEDIA_PROXY_SEARCH_SUCCESS](#ga2627f632efab868adddeebb59243497c)。

搜索请求（Search Request）已接受，搜索已开始。

<a id="r_gaf406225a87c697d784c5a429e89d2354"></a>

```c
#define MEDIA_PROXY_SEARCH_FAILURE 0x02U
```

相关声明：[MEDIA_PROXY_SEARCH_FAILURE](#gaf406225a87c697d784c5a429e89d2354)。

搜索请求（Search Request）无效，未开始搜索。

## 7.13\_组对象的对象类型（Group object object types）

<a id="r_ga7412b20ea355713443b7165f077b0a0d"></a>

```c
#define MEDIA_PROXY_GROUP_OBJECT_TRACK_TYPE 0x00U
```

相关声明：[MEDIA_PROXY_GROUP_OBJECT_TRACK_TYPE](#ga7412b20ea355713443b7165f077b0a0d)。

组对象类型（Group Object Type）为音轨（Track）。

<a id="r_ga63abba926894a45e187e3f4e4610cb35"></a>

```c
#define MEDIA_PROXY_GROUP_OBJECT_GROUP_TYPE 0x01U
```

相关声明：[MEDIA_PROXY_GROUP_OBJECT_GROUP_TYPE](#ga63abba926894a45e187e3f4e4610cb35)。

组对象类型（Group Object Type）为组（Group）。

## 7.14\_详细说明（Detailed Documentation）

<a id="gaf2c68cb2ac32973b85594660d43688dd"></a>

### `MEDIA_PROXY_CMD_CANNOT_BE_COMPLETED`

```c
#define MEDIA_PROXY_CMD_CANNOT_BE_COMPLETED 0x04U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

由于播放器内部的某种条件，无法成功完成任何媒体控制点写入（Media Control Point Write）所请求的动作。

<a id="ga1637459cd6eaf9d4d63a04d1facc29b7"></a>

### `MEDIA_PROXY_CMD_NOT_SUPPORTED`

```c
#define MEDIA_PROXY_CMD_NOT_SUPPORTED 0x02U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

写入媒体控制点（Media Control Point）时使用了无效或不支持的操作码。

<a id="ga7d0595796a80348b570add74c6dfa14e"></a>

### `MEDIA_PROXY_CMD_PLAYER_INACTIVE`

```c
#define MEDIA_PROXY_CMD_PLAYER_INACTIVE 0x03U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

收到操作码时，媒体播放器状态（Media Player State）特征值为非活动（Inactive）；或执行该操作码所请求动作的结果，使该特征值变为 Inactive。

<a id="gaa56458b11f4cb78f1265ea8538774108"></a>

### `MEDIA_PROXY_CMD_SUCCESS`

```c
#define MEDIA_PROXY_CMD_SUCCESS 0x01U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

写入操作码（Opcode Write）所请求的动作已成功完成。

<a id="ga63abba926894a45e187e3f4e4610cb35"></a>

### `MEDIA_PROXY_GROUP_OBJECT_GROUP_TYPE`

```c
#define MEDIA_PROXY_GROUP_OBJECT_GROUP_TYPE 0x01U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

组对象类型（Group Object Type）为组（Group）。

<a id="ga7412b20ea355713443b7165f077b0a0d"></a>

### `MEDIA_PROXY_GROUP_OBJECT_TRACK_TYPE`

```c
#define MEDIA_PROXY_GROUP_OBJECT_TRACK_TYPE 0x00U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

组对象类型（Group Object Type）为音轨（Track）。

<a id="gac0c0730bcf6592c5d2c61d21d09efb2b"></a>

### `MEDIA_PROXY_OP_FAST_FORWARD`

```c
#define MEDIA_PROXY_OP_FAST_FORWARD 0x04U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

快进（Fast Forward）当前音轨。

<a id="gabc2b497b95728325208e28db6d5cf4f8"></a>

### `MEDIA_PROXY_OP_FAST_REWIND`

```c
#define MEDIA_PROXY_OP_FAST_REWIND 0x03U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

快退（Fast Rewind）当前音轨。

<a id="ga5eb0a22c257e370cd76d73f7fa9e342c"></a>

### `MEDIA_PROXY_OP_FIRST_GROUP`

```c
#define MEDIA_PROXY_OP_FIRST_GROUP 0x42U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

将当前组设为组序列（Sequence of Groups）中的第一组。

<a id="gac2e5c8e2cadd05092fa186f05ae74e57"></a>

### `MEDIA_PROXY_OP_FIRST_SEGMENT`

```c
#define MEDIA_PROXY_OP_FIRST_SEGMENT 0x22U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

将当前音轨位置设为当前音轨第一段（First Segment）的起始位置。

<a id="ga5c272e2e9b24ce92a7df7373d1b002cc"></a>

### `MEDIA_PROXY_OP_FIRST_TRACK`

```c
#define MEDIA_PROXY_OP_FIRST_TRACK 0x32U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

按播放顺序（Playing Order）将当前音轨设为第一音轨。

<a id="ga139d2ced243a6ff47d8335583974a0da"></a>

### `MEDIA_PROXY_OP_GOTO_GROUP`

```c
#define MEDIA_PROXY_OP_GOTO_GROUP 0x44U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

将当前组设为组序列（Sequence of Groups）中的第 n 组。

<a id="gab3bbf7eb7c562bc6a5148c75eb99ada5"></a>

### `MEDIA_PROXY_OP_GOTO_SEGMENT`

```c
#define MEDIA_PROXY_OP_GOTO_SEGMENT 0x24U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

将当前音轨位置设为当前音轨第 n 段（Nth Segment）的起始位置。

<a id="gaf2f100d41413b14c5dbd8f2641a13bb0"></a>

### `MEDIA_PROXY_OP_GOTO_TRACK`

```c
#define MEDIA_PROXY_OP_GOTO_TRACK 0x34U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

按播放顺序（Playing Order）将当前音轨设为第 n 个音轨。

<a id="gaa6ac8f8bf674c0ffec22bd061e9be3dc"></a>

### `MEDIA_PROXY_OP_LAST_GROUP`

```c
#define MEDIA_PROXY_OP_LAST_GROUP 0x43U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

将当前组设为组序列（Sequence of Groups）中的最后一组。

<a id="ga3f317208b9d8495c498325a4d37d41ad"></a>

### `MEDIA_PROXY_OP_LAST_SEGMENT`

```c
#define MEDIA_PROXY_OP_LAST_SEGMENT 0x23U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

将当前音轨位置设为当前音轨最后一段（Last Segment）的起始位置。

<a id="ga72614d9a2fa4c938f1c7055bc219c8bc"></a>

### `MEDIA_PROXY_OP_LAST_TRACK`

```c
#define MEDIA_PROXY_OP_LAST_TRACK 0x33U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

按播放顺序（Playing Order）将当前音轨设为最后一音轨。

<a id="gaceb240f7f21074b6b7f9ed1e9d645cb0"></a>

### `MEDIA_PROXY_OP_MOVE_RELATIVE`

```c
#define MEDIA_PROXY_OP_MOVE_RELATIVE 0x10U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

相对于当前音轨位置（Current Track Position），设置新的当前位置。

<a id="ga3cf10acf1ef8b7d3252eb37cb4e35f97"></a>

### `MEDIA_PROXY_OP_NEXT_GROUP`

```c
#define MEDIA_PROXY_OP_NEXT_GROUP 0x41U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

将当前组设为组序列（Sequence of Groups）中的下一组。

<a id="gada5e3114b2b00f4ea27adf884f49429e"></a>

### `MEDIA_PROXY_OP_NEXT_SEGMENT`

```c
#define MEDIA_PROXY_OP_NEXT_SEGMENT 0x21U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

将当前音轨位置设为当前音轨下一段（Next Segment）的起始位置。

<a id="gaae4cc32663f02bf96d1dcbbc8453e40b"></a>

### `MEDIA_PROXY_OP_NEXT_TRACK`

```c
#define MEDIA_PROXY_OP_NEXT_TRACK 0x31U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

按播放顺序（Playing Order）将当前音轨设为下一音轨。

<a id="ga69bcb42294e8cd1eb062bbe19399a3df"></a>

### `MEDIA_PROXY_OP_PAUSE`

```c
#define MEDIA_PROXY_OP_PAUSE 0x02U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

暂停播放当前音轨（Track）。

<a id="gadd400bc6900abe1956d4de4efb212683"></a>

### `MEDIA_PROXY_OP_PLAY`

```c
#define MEDIA_PROXY_OP_PLAY 0x01U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

开始播放当前音轨（Track）。

<a id="gae15386adcfe1c5ca56eac7d0292dffd0"></a>

### `MEDIA_PROXY_OP_PREV_GROUP`

```c
#define MEDIA_PROXY_OP_PREV_GROUP 0x40U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

将当前组设为组序列（Sequence of Groups）中的上一组。

<a id="ga7846fa5da200e0d921056b410e60677e"></a>

### `MEDIA_PROXY_OP_PREV_SEGMENT`

```c
#define MEDIA_PROXY_OP_PREV_SEGMENT 0x20U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

将当前音轨位置设为当前音轨上一段（Previous Segment）的起始位置。

<a id="ga1b7db568fc3153c29ed4e951d95bee8e"></a>

### `MEDIA_PROXY_OP_PREV_TRACK`

```c
#define MEDIA_PROXY_OP_PREV_TRACK 0x30U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

按播放顺序（Playing Order）将当前音轨设为上一音轨。

<a id="gaf3707d44c7a3305ba896c0257b2109b3"></a>

### `MEDIA_PROXY_OP_STOP`

```c
#define MEDIA_PROXY_OP_STOP 0x05U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

停止当前活动，回到暂停状态（Paused State），并将当前音轨位置设为当前音轨起点。

<a id="ga05453105bc3d1579110e908b794e3ac5"></a>

### `MEDIA_PROXY_OP_SUP_FAST_FORWARD`

```c
#define MEDIA_PROXY_OP_SUP_FAST_FORWARD BIT(3U)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

支持快进操作码（Fast Forward Opcode）。

<a id="ga99952473bafd76f6ceaf141307510f28"></a>

### `MEDIA_PROXY_OP_SUP_FAST_REWIND`

```c
#define MEDIA_PROXY_OP_SUP_FAST_REWIND BIT(2U)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

支持快退操作码（Fast Rewind Opcode）。

<a id="ga716af4c6eb702729ec4f9ff9ccc49b32"></a>

### `MEDIA_PROXY_OP_SUP_FIRST_GROUP`

```c
#define MEDIA_PROXY_OP_SUP_FIRST_GROUP BIT(18U)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

支持第一组操作码（First Group Opcode）。

<a id="ga916ce95086dfeb127e124a8c5d530371"></a>

### `MEDIA_PROXY_OP_SUP_FIRST_SEGMENT`

```c
#define MEDIA_PROXY_OP_SUP_FIRST_SEGMENT BIT(8U)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

支持第一段操作码（First Segment Opcode）。

<a id="ga6e1d53fedf09bd95bcf112495dcfd64f"></a>

### `MEDIA_PROXY_OP_SUP_FIRST_TRACK`

```c
#define MEDIA_PROXY_OP_SUP_FIRST_TRACK BIT(13U)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

支持第一音轨操作码（First Track Opcode）。

<a id="gaec8b6d2d684c81b9da9fee870e0258c2"></a>

### `MEDIA_PROXY_OP_SUP_GOTO_GROUP`

```c
#define MEDIA_PROXY_OP_SUP_GOTO_GROUP BIT(20U)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

支持转到指定组操作码（Goto Group Opcode）。

<a id="ga7af591de387958f5c187ba8d0e834247"></a>

### `MEDIA_PROXY_OP_SUP_GOTO_SEGMENT`

```c
#define MEDIA_PROXY_OP_SUP_GOTO_SEGMENT BIT(10U)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

支持转到指定段操作码（Goto Segment Opcode）。

<a id="gad2364a0ef8c54bd9fa3372edddae32b0"></a>

### `MEDIA_PROXY_OP_SUP_GOTO_TRACK`

```c
#define MEDIA_PROXY_OP_SUP_GOTO_TRACK BIT(15U)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

支持转到指定音轨操作码（Goto Track Opcode）。

<a id="gac944825600367a41e8213dfd9de569a3"></a>

### `MEDIA_PROXY_OP_SUP_LAST_GROUP`

```c
#define MEDIA_PROXY_OP_SUP_LAST_GROUP BIT(19U)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

支持最后一组操作码（Last Group Opcode）。

<a id="gaf193ea0b4a34e3981f2f45d3b9c228a2"></a>

### `MEDIA_PROXY_OP_SUP_LAST_SEGMENT`

```c
#define MEDIA_PROXY_OP_SUP_LAST_SEGMENT BIT(9U)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

支持最后一段操作码（Last Segment Opcode）。

<a id="gaf43188bb438b9a766d07cd2fa900e079"></a>

### `MEDIA_PROXY_OP_SUP_LAST_TRACK`

```c
#define MEDIA_PROXY_OP_SUP_LAST_TRACK BIT(14U)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

支持最后音轨操作码（Last Track Opcode）。

<a id="ga03c393a29c68529e4dd9038e3947468b"></a>

### `MEDIA_PROXY_OP_SUP_MOVE_RELATIVE`

```c
#define MEDIA_PROXY_OP_SUP_MOVE_RELATIVE BIT(5U)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

支持相对移动操作码（Move Relative Opcode）。

<a id="ga324dae538f28e818eea79c83aaa0b22c"></a>

### `MEDIA_PROXY_OP_SUP_NEXT_GROUP`

```c
#define MEDIA_PROXY_OP_SUP_NEXT_GROUP BIT(17U)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

支持下一组操作码（Next Group Opcode）。

<a id="ga26ae64ece06a1f6f8dd7eb2c9965a4b6"></a>

### `MEDIA_PROXY_OP_SUP_NEXT_SEGMENT`

```c
#define MEDIA_PROXY_OP_SUP_NEXT_SEGMENT BIT(7U)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

支持下一段操作码（Next Segment Opcode）。

<a id="gafc061bc953b0338aded4cef681f9e963"></a>

### `MEDIA_PROXY_OP_SUP_NEXT_TRACK`

```c
#define MEDIA_PROXY_OP_SUP_NEXT_TRACK BIT(12U)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

支持下一音轨操作码（Next Track Opcode）。

<a id="gaec37a692c28ca90c8053db9de2a6c44f"></a>

### `MEDIA_PROXY_OP_SUP_PAUSE`

```c
#define MEDIA_PROXY_OP_SUP_PAUSE BIT(1U)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

支持暂停操作码（Pause Opcode）。

<a id="gafe30bb1287b9a44655d76364d4832eac"></a>

### `MEDIA_PROXY_OP_SUP_PLAY`

```c
#define MEDIA_PROXY_OP_SUP_PLAY BIT(0U)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

媒体播放器支持的命令操作码（Supported Command Opcodes）。

支持播放操作码（Play Opcode）。

<a id="ga496060d673b48e045a5a2a57aa82bddc"></a>

### `MEDIA_PROXY_OP_SUP_PREV_GROUP`

```c
#define MEDIA_PROXY_OP_SUP_PREV_GROUP BIT(16U)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

支持上一组操作码（Previous Group Opcode）。

<a id="ga3d39700e21cbdf2906321c8899e0b626"></a>

### `MEDIA_PROXY_OP_SUP_PREV_SEGMENT`

```c
#define MEDIA_PROXY_OP_SUP_PREV_SEGMENT BIT(6U)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

支持上一段操作码（Previous Segment Opcode）。

<a id="gafe8bab8f90281e5894e5f79f32449e63"></a>

### `MEDIA_PROXY_OP_SUP_PREV_TRACK`

```c
#define MEDIA_PROXY_OP_SUP_PREV_TRACK BIT(11U)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

支持上一音轨操作码（Previous Track Opcode）。

<a id="ga060ff676a0b2f249a26aaf61147b68e8"></a>

### `MEDIA_PROXY_OP_SUP_STOP`

```c
#define MEDIA_PROXY_OP_SUP_STOP BIT(4U)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

支持停止操作码（Stop Opcode）。

<a id="ga22c2599cd62a263a01c06c9bd9fff054"></a>

### `MEDIA_PROXY_OPCODES_SUPPORTED_LEN`

```c
#define MEDIA_PROXY_OPCODES_SUPPORTED_LEN 4U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

媒体播放器（Media Player）支持的操作码字段长度。

<a id="gaa53d906340c0b2adb314945f5299464e"></a>

### `MEDIA_PROXY_PLAYBACK_SPEED_DOUBLE`

```c
#define MEDIA_PROXY_PLAYBACK_SPEED_DOUBLE 64
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

双倍播放速度（Double Playback Speed），对应 200% 速度。

<a id="ga4c765363c2a5b0d9800864859746ae33"></a>

### `MEDIA_PROXY_PLAYBACK_SPEED_HALF`

```c
#define MEDIA_PROXY_PLAYBACK_SPEED_HALF -64
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

半速播放（Half Playback Speed），对应 50% 速度。

<a id="gaaccc9d75f96b5fe2de101b119a516d36"></a>

### `MEDIA_PROXY_PLAYBACK_SPEED_MAX`

```c
#define MEDIA_PROXY_PLAYBACK_SPEED_MAX 127
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

最高播放速度（Max Playback Speed），对应 395.7% 速度，接近 400%。

<a id="ga61732644eecad1442d5cedbda8f8cc08"></a>

### `MEDIA_PROXY_PLAYBACK_SPEED_MIN`

```c
#define MEDIA_PROXY_PLAYBACK_SPEED_MIN -128
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

最低播放速度（Minimum Playback Speed），对应 25% 速度。

<a id="ga5462f8d5ce98cc33a131b2e7b5548c41"></a>

### `MEDIA_PROXY_PLAYBACK_SPEED_QUARTER`

```c
#define MEDIA_PROXY_PLAYBACK_SPEED_QUARTER -128
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

四分之一播放速度（Quarter Playback Speed），对应 25% 速度。

<a id="ga6d8854bd54dcbb657f0ba545ec231368"></a>

### `MEDIA_PROXY_PLAYBACK_SPEED_UNITY`

```c
#define MEDIA_PROXY_PLAYBACK_SPEED_UNITY 0
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

一倍播放速度（Unity Playback Speed），对应 100% 速度。

<a id="ga63055a150b93f06e076b97abb6f6f682"></a>

### `MEDIA_PROXY_PLAYING_ORDER_INORDER_ONCE`

```c
#define MEDIA_PROXY_PLAYING_ORDER_INORDER_ONCE 0x03U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

按音轨顺序（Track Order）将组内音轨播放一次。

<a id="ga437068b9d90404cc68d41faaedfac9a8"></a>

### `MEDIA_PROXY_PLAYING_ORDER_INORDER_REPEAT`

```c
#define MEDIA_PROXY_PLAYING_ORDER_INORDER_REPEAT 0x04U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

按音轨顺序（Track Order）重复播放组内音轨。

<a id="gac344111e2b043cdfbcb9ac272622b16f"></a>

### `MEDIA_PROXY_PLAYING_ORDER_NEWEST_ONCE`

```c
#define MEDIA_PROXY_PLAYING_ORDER_NEWEST_ONCE 0x07U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

从最新音轨开始，将组内音轨播放一次（Newest First）。

<a id="gaf10b815dc579dc67b1f092e0a85c51d9"></a>

### `MEDIA_PROXY_PLAYING_ORDER_NEWEST_REPEAT`

```c
#define MEDIA_PROXY_PLAYING_ORDER_NEWEST_REPEAT 0x08U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

从最新音轨开始，重复播放组内音轨（Newest First）。

<a id="ga48a33dd8fbb8a8ab162c18bc0e9b7531"></a>

### `MEDIA_PROXY_PLAYING_ORDER_OLDEST_ONCE`

```c
#define MEDIA_PROXY_PLAYING_ORDER_OLDEST_ONCE 0x05U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

从最旧音轨开始，将组内音轨播放一次（Oldest First）。

<a id="ga63a33c4e3267ab39ab5892fb5b0bbe89"></a>

### `MEDIA_PROXY_PLAYING_ORDER_OLDEST_REPEAT`

```c
#define MEDIA_PROXY_PLAYING_ORDER_OLDEST_REPEAT 0x06U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

从最旧音轨开始，重复播放组内音轨（Oldest First）。

<a id="gae152374af5d567cf65d6d7b236b792a4"></a>

### `MEDIA_PROXY_PLAYING_ORDER_SHUFFLE_ONCE`

```c
#define MEDIA_PROXY_PLAYING_ORDER_SHUFFLE_ONCE 0x09U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

以随机顺序（Random Order）将组内音轨播放一次。

<a id="ga45161ec08b67e4d3bd59efa45027f3aa"></a>

### `MEDIA_PROXY_PLAYING_ORDER_SHUFFLE_REPEAT`

```c
#define MEDIA_PROXY_PLAYING_ORDER_SHUFFLE_REPEAT 0x0AU
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

以随机顺序（Random Order）重复播放组内音轨。

<a id="ga8e721b49c361d2395bd8eb740d43e282"></a>

### `MEDIA_PROXY_PLAYING_ORDER_SINGLE_ONCE`

```c
#define MEDIA_PROXY_PLAYING_ORDER_SINGLE_ONCE 0x01U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

单个音轨（Track）播放一次，没有下一音轨。

<a id="gadf5f0c15cb88cd92f49db1b57dbd2c18"></a>

### `MEDIA_PROXY_PLAYING_ORDER_SINGLE_REPEAT`

```c
#define MEDIA_PROXY_PLAYING_ORDER_SINGLE_REPEAT 0x02U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

重复播放单个音轨（Track），下一音轨就是当前音轨。

<a id="ga8fee464b8e17fffc4361972df15062af"></a>

### `MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_INORDER_ONCE`

```c
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_INORDER_ONCE BIT(2U)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

按音轨顺序（Track Order）将组内音轨播放一次。

<a id="ga7faeff14de245ea670ca447b0adc4820"></a>

### `MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_INORDER_REPEAT`

```c
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_INORDER_REPEAT BIT(3U)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

按音轨顺序（Track Order）重复播放组内音轨。

<a id="ga334f9e16ea7a52bfb6357ad619e3601b"></a>

### `MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_NEWEST_ONCE`

```c
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_NEWEST_ONCE BIT(6U)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

从最新音轨开始，将组内音轨播放一次（Newest First）。

<a id="gaaf5f08e2dd624e2bb1bd9b72ab4b2b33"></a>

### `MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_NEWEST_REPEAT`

```c
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_NEWEST_REPEAT BIT(7U)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

从最新音轨开始，重复播放组内音轨（Newest First）。

<a id="gae3d848fc0b9117fe9bc51327627ac635"></a>

### `MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_OLDEST_ONCE`

```c
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_OLDEST_ONCE BIT(4U)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

从最旧音轨开始，将组内音轨播放一次（Oldest First）。

<a id="ga7fa415d845dd1fefc8bdb74532878131"></a>

### `MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_OLDEST_REPEAT`

```c
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_OLDEST_REPEAT BIT(5U)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

从最旧音轨开始，重复播放组内音轨（Oldest First）。

<a id="ga3e998cda3e91f1c9fbb8496a748bcf12"></a>

### `MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SHUFFLE_ONCE`

```c
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SHUFFLE_ONCE BIT(8U)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

以随机顺序（Random Order）将组内音轨播放一次。

<a id="ga4f0689fe1fc0ac2b3f9b9ef4ed1afb8b"></a>

### `MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SHUFFLE_REPEAT`

```c
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SHUFFLE_REPEAT BIT(9U)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

以随机顺序（Random Order）重复播放组内音轨。

<a id="ga55b5a00ea9ec849e7c495463e5f1869d"></a>

### `MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SINGLE_ONCE`

```c
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SINGLE_ONCE BIT(0U)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

单个音轨（Track）播放一次，没有下一音轨。

<a id="ga465a82ace21a0e88356eccaf038f58e9"></a>

### `MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SINGLE_REPEAT`

```c
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SINGLE_REPEAT BIT(1U)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

重复播放单个音轨（Track），下一音轨就是当前音轨。

<a id="gaf406225a87c697d784c5a429e89d2354"></a>

### `MEDIA_PROXY_SEARCH_FAILURE`

```c
#define MEDIA_PROXY_SEARCH_FAILURE 0x02U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

搜索请求（Search Request）无效，未开始搜索。

<a id="ga2627f632efab868adddeebb59243497c"></a>

### `MEDIA_PROXY_SEARCH_SUCCESS`

```c
#define MEDIA_PROXY_SEARCH_SUCCESS 0x01U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

搜索请求（Search Request）已接受，搜索已开始。

<a id="ga1f0fb19dea467e90afd670ed9af0c092"></a>

### `MEDIA_PROXY_SEARCH_TYPE_ALBUM_NAME`

```c
#define MEDIA_PROXY_SEARCH_TYPE_ALBUM_NAME 0x03U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

按专辑名称（Album Name）搜索。

<a id="gaf0dbc19f843a444076d8886b1a05709b"></a>

### `MEDIA_PROXY_SEARCH_TYPE_ARTIST_NAME`

```c
#define MEDIA_PROXY_SEARCH_TYPE_ARTIST_NAME 0x02U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

按艺人名称（Artist Name）搜索。

<a id="ga28b1d7de2174e3714786cb369232f339"></a>

### `MEDIA_PROXY_SEARCH_TYPE_EARLIEST_YEAR`

```c
#define MEDIA_PROXY_SEARCH_TYPE_EARLIEST_YEAR 0x05U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

按最早年份（Earliest Year）搜索。

<a id="ga55c3a003881a75ce964e23fc3b0cea8e"></a>

### `MEDIA_PROXY_SEARCH_TYPE_GENRE`

```c
#define MEDIA_PROXY_SEARCH_TYPE_GENRE 0x07U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

按流派（Genre）搜索。

<a id="gaca10de7253c1cdcf5e0c6544de33c116"></a>

### `MEDIA_PROXY_SEARCH_TYPE_GROUP_NAME`

```c
#define MEDIA_PROXY_SEARCH_TYPE_GROUP_NAME 0x04U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

按组名称（Group Name）搜索。

<a id="ga01fb087af00bf492d19cc19adcaa9dea"></a>

### `MEDIA_PROXY_SEARCH_TYPE_LATEST_YEAR`

```c
#define MEDIA_PROXY_SEARCH_TYPE_LATEST_YEAR 0x06U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

按最晚年份（Latest Year）搜索。

<a id="ga25270f6c90daaace6a80f3255aaaf7fd"></a>

### `MEDIA_PROXY_SEARCH_TYPE_ONLY_GROUPS`

```c
#define MEDIA_PROXY_SEARCH_TYPE_ONLY_GROUPS 0x09U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

仅搜索组（Groups）。

<a id="gad758e14fbe978ffd95364a6fb27eab40"></a>

### `MEDIA_PROXY_SEARCH_TYPE_ONLY_TRACKS`

```c
#define MEDIA_PROXY_SEARCH_TYPE_ONLY_TRACKS 0x08U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

仅搜索音轨（Tracks）。

<a id="ga8be6fd8d9bb08836bea1c3f0d2e577ea"></a>

### `MEDIA_PROXY_SEARCH_TYPE_TRACK_NAME`

```c
#define MEDIA_PROXY_SEARCH_TYPE_TRACK_NAME 0x01U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

按音轨名称（Track Name）搜索。

<a id="gaa6aa7a6e98631152b4bd77b60c78d58a"></a>

### `MEDIA_PROXY_SEEKING_SPEED_FACTOR_MAX`

```c
#define MEDIA_PROXY_SEEKING_SPEED_FACTOR_MAX 64
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

最大搜寻速度（Maximum Seeking Speed），可取负值。

<a id="ga67c1069fa01425ad6cd8f36438b71826"></a>

### `MEDIA_PROXY_SEEKING_SPEED_FACTOR_MIN`

```c
#define MEDIA_PROXY_SEEKING_SPEED_FACTOR_MIN 4
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

最小搜寻速度（Minimum Seeking Speed），可取负值。

<a id="ga58495e58bf84235efcee89289fc992c2"></a>

### `MEDIA_PROXY_SEEKING_SPEED_FACTOR_ZERO`

```c
#define MEDIA_PROXY_SEEKING_SPEED_FACTOR_ZERO 0
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

不搜寻（No Seeking）。

<a id="gab8c465e0e63898e53c39171b89d668c9"></a>

### `MEDIA_PROXY_STATE_INACTIVE`

```c
#define MEDIA_PROXY_STATE_INACTIVE 0x00U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

当前音轨无效，且未选择任何音轨（Track）。

<a id="gab0c8f3510109f18ef6445f035b27cbe9"></a>

### `MEDIA_PROXY_STATE_LAST`

```c
#define MEDIA_PROXY_STATE_LAST 0x04U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

内部用作最后一个状态值（Last State Value）。

<a id="ga85325d7ff75ec05275a875d7d5540a6c"></a>

### `MEDIA_PROXY_STATE_PAUSED`

```c
#define MEDIA_PROXY_STATE_PAUSED 0x02U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

当前音轨已暂停（Paused）。

媒体播放器（Media Player）有当前音轨，但未在播放。

<a id="ga1967c76b290f1d20515740cf7139f49c"></a>

### `MEDIA_PROXY_STATE_PLAYING`

```c
#define MEDIA_PROXY_STATE_PLAYING 0x01U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

媒体播放器（Media Player）正在播放当前音轨。

<a id="gaa207ee7666ab18c40e5b1d2a6ed7f034"></a>

### `MEDIA_PROXY_STATE_SEEKING`

```c
#define MEDIA_PROXY_STATE_SEEKING 0x03U
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

当前音轨正在快进或快退（Fast Forwarding / Fast Rewinding）。

<a id="gaf535f1ab028407432ef890d278d936e0"></a>

### `bt_mcs_get_ots()`

```c
struct bt_ots * bt_mcs_get_ots ( void )
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

获取媒体控制服务（Media Control Service）使用的对象传输服务（Object Transfer Service）指针。

待办（TODO）：为此调用找到最合适的位置，并将它也移过去。

<a id="ga5aaa486e0c3663e21477984e54642ed1"></a>

### `media_proxy_ctrl_discover_player()`

```c
int media_proxy_ctrl_discover_player ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

发现远端媒体播放器（Remote Media Player）。

发现远端媒体播放器实例（Remote Media Player Instance）。通过蓝牙，借助媒体控制客户端和远端媒体控制服务发现并访问此实例。此调用启动对端媒体控制服务的 GATT 发现，设置句柄（Handles）与订阅（Subscriptions）。

在对远端播放器执行其他任何动作前，必须先调用一次。远端播放器实例通过 discover_player() 回调返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 要执行发现（Discovery）的连接。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga15804287093b20d4a1616380729b33c8"></a>

### `media_proxy_ctrl_get_commands_supported()`

```c
int media_proxy_ctrl_get_commands_supported ( struct media_player * player)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

读取支持的命令（Commands Supported）。

读取包含媒体播放器支持的命令操作码（Command Opcodes）的位图。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga23488e77985a04216ec7c7fa785f09fc"></a>

### `media_proxy_ctrl_get_content_ctrl_id()`

```c
uint8_t media_proxy_ctrl_get_content_ctrl_id ( struct media_player * player)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

读取内容控制 ID（Content Control ID）。

内容控制 ID 用于标识设备上的内容控制服务，并将其与相应的音频流关联。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga2ae50a1988305b4247ff0af796b6d93e"></a>

### `media_proxy_ctrl_get_current_group_id()`

```c
int media_proxy_ctrl_get_current_group_id ( struct media_player * player)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

读取当前分组对象 ID（Current Group Object ID）。

获取一个 48 位 ID，通过该 ID 可从对象传输服务（Object Transfer Service）取得当前曲目对象（Current Track Object）。

当前分组对象的说明见《媒体控制服务》（Media Control Service）规范 v1.0 第 3.14 节和第 4.4 节。

需要对象传输服务（Object Transfer Service）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gaebe7e3683041e28bef40df75cc991dea"></a>

### `media_proxy_ctrl_get_current_track_id()`

```c
int media_proxy_ctrl_get_current_track_id ( struct media_player * player)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

读取当前曲目对象 ID（Current Track Object ID）。

获取一个 48 位 ID，通过该 ID 可从对象传输服务（Object Transfer Service）取得当前曲目对象（Current Track Object）。

当前曲目对象的说明见《媒体控制服务》规范 v1.0 第 3.11 节和第 4.3 节。

需要对象传输服务（Object Transfer Service）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga5efccb39cdb97eed476e0c0bff461ec1"></a>

### `media_proxy_ctrl_get_icon_id()`

```c
int media_proxy_ctrl_get_icon_id ( struct media_player * player)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

读取图标对象 ID（Icon Object ID）。

获取一个 48 位 ID，通过该 ID 可从对象传输服务取得图标对象（Icon Object）。

图标对象的说明见《媒体控制服务》规范 v1.0 第 3.2 节和第 4.1 节。

需要对象传输服务（Object Transfer Service）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gab6df6fe71c8273eca855eb3be27290dd"></a>

### `media_proxy_ctrl_get_icon_url()`

```c
int media_proxy_ctrl_get_icon_url ( struct media_player * player)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

读取图标 URL。

获取媒体播放器图标的 URL。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga9433aaf24776c30557ea694795e75b3e"></a>

### `media_proxy_ctrl_get_media_state()`

```c
int media_proxy_ctrl_get_media_state ( struct media_player * player)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

读取媒体状态（Media State）。

读取媒体播放器状态（Media Player State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gae32da32bd504061801730805729242e1"></a>

### `media_proxy_ctrl_get_next_track_id()`

```c
int media_proxy_ctrl_get_next_track_id ( struct media_player * player)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

读取下一曲目对象 ID（Next Track Object ID）。

获取一个 48 位 ID，通过该 ID 可从对象传输服务取得下一曲目对象（Next Track Object）。

需要对象传输服务（Object Transfer Service）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga12dc878be39814660900ba875e13e537"></a>

### `media_proxy_ctrl_get_parent_group_id()`

```c
int media_proxy_ctrl_get_parent_group_id ( struct media_player * player)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

读取父分组对象 ID（Parent Group Object ID）。

获取一个 48 位 ID，通过该 ID 可从对象传输服务取得父曲目对象（Parent Track Object）。

译注：原文使用 `Parent Track Object`；相关接口和相邻说明使用父分组对象（Parent Group Object）。此处保留原文称谓并指出差异。

父分组是当前分组的上级分组。

当前曲目对象的说明见《媒体控制服务》规范 v1.0 第 3.14 节和第 4.4 节。

译注：原文在此使用 `Current Track Object`；相邻父分组说明及上述章节编号指向分组对象，保留原文表述供对照。

需要对象传输服务（Object Transfer Service）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga2d64a23b3f881579a603a04baeb64088"></a>

### `media_proxy_ctrl_get_playback_speed()`

```c
int media_proxy_ctrl_get_playback_speed ( struct media_player * player)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

获取播放速度（Playback Speed）。

播放速度参数与实际播放速度的关系如下：`实际播放速度 = 2^(speed_parameter/64)`。

速度参数为 `0` 时表示 1 倍速播放，即正常速度。参数为 `-128` 时表示正常速度的四分之一；参数为 `127` 时表示接近正常速度的四倍。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga2261222d8581ed86e91a276b13359126"></a>

### `media_proxy_ctrl_get_player_name()`

```c
int media_proxy_ctrl_get_player_name ( struct media_player * player)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

读取媒体播放器名称（Media Player Name）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga2f93bcde2460c6638880f8e6631eb68e"></a>

### `media_proxy_ctrl_get_playing_order()`

```c
int media_proxy_ctrl_get_playing_order ( struct media_player * player)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

读取播放顺序（Playing Order）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga030899757b79251f1d5a1055f65fe989"></a>

### `media_proxy_ctrl_get_playing_orders_supported()`

```c
int media_proxy_ctrl_get_playing_orders_supported ( struct media_player * player)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

读取支持的播放顺序（Playing Orders Supported）。

读取包含媒体播放器支持的播放顺序（Playing Orders）的位图。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga580a0c9fa47460be59f0571ee11a41b4"></a>

### `media_proxy_ctrl_get_search_results_id()`

```c
int media_proxy_ctrl_get_search_results_id ( struct media_player * player)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

读取搜索结果对象 ID（Search Results Object ID）。

获取一个 48 位 ID，通过该 ID 可从对象传输服务取得搜索结果对象（Search Results Object）。

搜索结果对象属于分组对象（Group object）。仅在执行过成功的搜索操作后，搜索结果对象才存在。

需要对象传输服务（Object Transfer Service）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga817ca4ab611e214493fbc918036def0f"></a>

### `media_proxy_ctrl_get_seeking_speed()`

```c
int media_proxy_ctrl_get_seeking_speed ( struct media_player * player)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

获取搜索播放位置速度（Seeking Speed）。

搜索播放位置速度（Seeking speed）表示播放器移动播放位置的速度，是相对于实时播放速度的系数。例如，系数为 4 表示以实时播放速度的四倍搜索位置。正值表示向前搜索，负值表示向后搜索。

搜索播放位置速度不能直接设置；非零值是执行快退（Fast rewind）或快进（Fast forward）命令的结果。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga488441418a8f2d358092019bbfe16788"></a>

### `media_proxy_ctrl_get_track_duration()`

```c
int media_proxy_ctrl_get_track_duration ( struct media_player * player)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

读取曲目时长（Track Duration）。

曲目时长以百分之一秒为单位。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gae0bb75feb49a68b495150c6fba2f21a7"></a>

### `media_proxy_ctrl_get_track_position()`

```c
int media_proxy_ctrl_get_track_position ( struct media_player * player)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

读取曲目位置（Track Position）。

播放器的位置，即播放位置，以距曲目开头的百分之一秒数表示。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga1afcc097cb36c4f11141b82ce28e8126"></a>

### `media_proxy_ctrl_get_track_segments_id()`

```c
int media_proxy_ctrl_get_track_segments_id ( struct media_player * player)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

读取当前曲目片段对象 ID（Current Track Segments Object ID）。

获取一个 48 位 ID，通过该 ID 可从对象传输服务取得当前曲目片段对象（Current Track Segments Object）。

曲目片段对象的说明见《媒体控制服务》规范 v1.0 第 3.10 节和第 4.2 节。

需要对象传输服务（Object Transfer Service）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gabfbb49e79204130cb004f217af771b80"></a>

### `media_proxy_ctrl_get_track_title()`

```c
int media_proxy_ctrl_get_track_title ( struct media_player * player)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

读取曲目标题（Track Title）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga352228fb77498b61205a22b0f3a75c8e"></a>

### `media_proxy_ctrl_register()`

```c
int media_proxy_ctrl_register ( struct media_proxy_ctrl_cbs * ctrl_cbs)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

向媒体代理（media_proxy）注册控制器（Controller）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctrl_cbs` | 提供给控制器的回调（Callbacks）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga590762e7272b99fb8ac50a7841424670"></a>

### `media_proxy_ctrl_send_command()`

```c
int media_proxy_ctrl_send_command ( struct media_player * player, const struct mpl_cmd * command )
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

发送命令。

向媒体播放器发送命令（Command）。命令可能使播放器改变状态，并可能产生两个回调：一个报告命令实际发送给播放器的情况，另一个报告播放器返回的命令结果。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `command` | 要发送的命令。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga052c3fabac4a44ee2802ddd4a6c5c9ac"></a>

### `media_proxy_ctrl_send_search()`

```c
int media_proxy_ctrl_send_search ( struct media_player * player, const struct mpl_search * search )
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

设置搜索（Search）。

向媒体播放器写入搜索（Search）。搜索成功时，可通过对象传输服务（OTS）中的组对象（Group Object）获得搜索结果。

最多可能产生三个回调（Callbacks）。

- 一个回调报告搜索实际发送给播放器的情况。
- 一个回调报告播放器返回的搜索结果码（Search Result Code）。
- 若搜索成功，另一个回调报告对象传输服务（OTS，原文写作 OTs）中的搜索结果对象 ID。

需要对象传输服务（Object Transfer Service）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `search` | 要写入的搜索请求。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gae496885d0124f4e3fc2c0f203fcff118"></a>

### `media_proxy_ctrl_set_current_group_id()`

```c
int media_proxy_ctrl_set_current_group_id ( struct media_player * player, uint64_t id )
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

设置当前分组对象 ID。

将播放器的当前分组切换为给定 ID 对应的分组，并将当前曲目切换为该分组中的第一首曲目。

需要对象传输服务（Object Transfer Service）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `id` | 分组对象的 ID。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gaea6adacedaded10f7c2c0f91b7159f74"></a>

### `media_proxy_ctrl_set_current_track_id()`

```c
int media_proxy_ctrl_set_current_track_id ( struct media_player * player, uint64_t id )
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

设置当前曲目对象 ID。

将播放器的当前曲目切换为给定 ID 对应的曲目，行为类似于跳转曲目（Goto track）命令。

需要对象传输服务（Object Transfer Service）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `id` | 曲目对象的 ID。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga43b797717fb9b36b94a606dfabeb0fa7"></a>

### `media_proxy_ctrl_set_next_track_id()`

```c
int media_proxy_ctrl_set_next_track_id ( struct media_player * player, uint64_t id )
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

设置下一曲目对象 ID。

将播放器的下一曲目切换为给定 ID 对应的曲目。

需要对象传输服务（Object Transfer Service）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `id` | 曲目对象的 ID。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gabafbc857c3e6befe98e339acb58f17fb"></a>

### `media_proxy_ctrl_set_playback_speed()`

```c
int media_proxy_ctrl_set_playback_speed ( struct media_player * player, int8_t speed )
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

设置播放速度。

播放速度参数的说明见 `get_playback_speed()` 函数。

注意：媒体播放器可能不支持播放速度参数的所有取值。如果给定值不受支持且高于当前值，播放器应将播放速度设为下一个更高的受支持值；相应地，若给定值低于当前值，应设为下一个更低的受支持值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `speed` | 要设置的播放速度参数。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gae077bc84648137460a9aeb6cfd4acb4c"></a>

### `media_proxy_ctrl_set_player_name()`

```c
int media_proxy_ctrl_set_player_name ( struct media_player * player, const char * name )
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

设置媒体播放器名称。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `name` | 新的媒体播放器名称。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gaa4040e97100f6e70527e6ad201309bbe"></a>

### `media_proxy_ctrl_set_playing_order()`

```c
int media_proxy_ctrl_set_playing_order ( struct media_player * player, uint8_t order )
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

设置播放顺序。

设置媒体播放器的播放顺序（Playing Order）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `order` | 要设置的播放顺序。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga776bb5f16cf1f4f6cc3842aabd86b781"></a>

### `media_proxy_ctrl_set_track_position()`

```c
int media_proxy_ctrl_set_track_position ( struct media_player * player, int32_t position )
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

设置曲目位置。

设置媒体播放器在当前曲目中的播放位置。位置以百分之一秒为单位：正值从曲目开头计算，负值从曲目结尾向前计算。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `position` | 要设置的音轨位置（Track Position）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga694e83401835149833024cf094b98cd1"></a>

### `media_proxy_pl_command_cb()`

```c
void media_proxy_pl_command_cb ( const struct mpl_cmd_ntf * cmd_ntf)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

命令回调（Command Callback）。

命令发送后调用，以通知命令是否成功执行。参见 MEDIA_PROXY_CMD_* 结果码定义。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cmd_ntf` | 命令结果（Command Result）。 |

<a id="ga70ea8a24a4e853a191e0947e1c2d1145"></a>

### `media_proxy_pl_commands_supported_cb()`

```c
void media_proxy_pl_commands_supported_cb ( uint32_t opcodes)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

支持的命令回调（Commands Supported Callback）。

支持的命令集合（Supported Commands）变化时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `opcodes` | 支持的命令操作码（Command Opcodes）。 |

<a id="gad02f2924e1aa765c04cbbc6441e7d063"></a>

### `media_proxy_pl_current_group_id_cb()`

```c
void media_proxy_pl_current_group_id_cb ( uint64_t id)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

当前组对象 ID 回调（Current Group Object ID Callback）。

当前组 ID（Current Group ID）变化时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `id` | 对象传输服务（OTS）中当前组对象的 ID。 |

<a id="gadcad4efdd714159d5d9611bbf74d5fae"></a>

### `media_proxy_pl_current_track_id_cb()`

```c
void media_proxy_pl_current_track_id_cb ( uint64_t id)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

当前音轨对象 ID 回调（Current Track Object ID Callback）。

当前音轨 ID（Current Track ID）变化时调用，例如音轨切换时。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `id` | 对象传输服务（OTS）中当前音轨对象的 ID。 |

<a id="gadd348a8d5aff193f7a9113a759e85b1d"></a>

### `media_proxy_pl_icon_url_cb()`

```c
void media_proxy_pl_icon_url_cb ( const char * url)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

播放器图标 URL 变化回调（Player Icon URL Changed Callback）。

播放器图标 URL（Player Icon URL）变化时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `url` | 播放器图标的 URL（Player Icon URL）。 |

<a id="gab0b10b3de5674f2172e1a2f779cbe8d5"></a>

### `media_proxy_pl_init()`

```c
int media_proxy_pl_init ( void )
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

初始化播放器（Player）。

待办（TODO）：移至播放器头文件（Player Header File）。

<a id="ga842d7951a04702d6f819de44c47b9cac"></a>

### `media_proxy_pl_media_state_cb()`

```c
void media_proxy_pl_media_state_cb ( uint8_t state)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

媒体状态回调（Media State Callback）。

媒体状态（Media State）变化时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `state` | 媒体播放器状态（Media Player State）。 |

<a id="ga0a70dc60a4d6acbcc58e220b75dad92a"></a>

### `media_proxy_pl_name_cb()`

```c
void media_proxy_pl_name_cb ( const char * name)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

播放器名称变化回调（Player Name Changed Callback）。

播放器名称（Player Name）变化时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 播放器名称（Player Name）。 |

<a id="gaf0bd3447e64b6128710c07461766a0c9"></a>

### `media_proxy_pl_next_track_id_cb()`

```c
void media_proxy_pl_next_track_id_cb ( uint64_t id)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

下一音轨对象 ID 回调（Next Track Object ID Callback）。

当前音轨 ID（Current Track ID）变化时调用。（原文此处写 current track，其相邻参数说明为下一音轨；保留这一疑点。）

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `id` | 对象传输服务（OTS）中下一音轨对象的 ID。 |

<a id="ga64730f46b87cf9089aff65b6be12f42d"></a>

### `media_proxy_pl_parent_group_id_cb()`

```c
void media_proxy_pl_parent_group_id_cb ( uint64_t id)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

父组对象 ID 回调（Parent Group Object ID Callback）。

父组 ID（Parent Group ID）变化时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `id` | 对象传输服务（OTS）中父组对象的 ID。 |

<a id="ga17c2ca149050e1382eb556f6dcccad21"></a>

### `media_proxy_pl_playback_speed_cb()`

```c
void media_proxy_pl_playback_speed_cb ( int8_t speed)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

播放速度回调（Playback Speed Callback）。

播放速度（Playback Speed）变化时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `speed` | 播放速度参数。 |

<a id="ga96e8156b0267f3d55ee52ab307d81985"></a>

### `media_proxy_pl_playing_order_cb()`

```c
void media_proxy_pl_playing_order_cb ( uint8_t order)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

播放顺序回调（Playing Order Callback）。

播放顺序（Playing Order）变化时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `order` | 播放顺序。 |

<a id="gac75e27a4a5e169481723cd6b39678274"></a>

### `media_proxy_pl_register()`

```c
int media_proxy_pl_register ( struct media_proxy_pl_calls * pl_calls)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

向媒体代理（Media Proxy）注册播放器（Player）。

向媒体代理模块（Media Proxy Module）注册播放器，供媒体控制器使用。

媒体代理可调用所提供 media_proxy_pl_calls 结构体中的任何非 NULL 函数指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pl_calls` | 指向媒体播放器调用接口（Media Player Calls）的函数指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga8c0d75f61120047bacd0b933534e1b41"></a>

### `media_proxy_pl_search_cb()`

```c
void media_proxy_pl_search_cb ( uint8_t result_code)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

搜索回调（Search Callback）。

设置搜索后调用，以通知搜索是否成功执行。参见 MEDIA_PROXY_SEARCH_* 结果码定义。

搜索成功时，实际搜索结果（Search Results）可从搜索结果对象中获取。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `result_code` | 搜索结果（Search Result），表示成功或失败。 |

<a id="ga35896de266f2a2bd101279e4ce9900c7"></a>

### `media_proxy_pl_search_results_id_cb()`

```c
void media_proxy_pl_search_results_id_cb ( uint64_t id)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

搜索结果对象 ID 回调（Search Results Object ID Callback）。

搜索结果 ID（Search Results ID）变化时调用，通常发生在新的搜索成功之后。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `id` | 对象传输服务（OTS）中搜索结果对象的 ID。 |

<a id="gaeaf89f4b760870896ed42687562971ca"></a>

### `media_proxy_pl_seeking_speed_cb()`

```c
void media_proxy_pl_seeking_speed_cb ( int8_t speed)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

搜寻速度回调（Seeking Speed Callback）。

搜寻速度（Seeking Speed）变化时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `speed` | 搜索播放位置的速度系数（Seeking speed factor）。 |

<a id="ga4a93a18cb0b75cb16828243f0d37b4b4"></a>

### `media_proxy_pl_track_changed_cb()`

```c
void media_proxy_pl_track_changed_cb ( void )
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

音轨变化回调（Track Changed Callback）。

播放器当前音轨（Current Track）变化时调用。

<a id="ga7b0f9633a5322557b91ea97eafac9f34"></a>

### `media_proxy_pl_track_duration_cb()`

```c
void media_proxy_pl_track_duration_cb ( int32_t duration)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

音轨时长回调（Track Duration Callback）。

当前音轨时长（Track Duration）变化时调用，例如音轨切换时。

音轨时长（Track Duration）以百分之一秒为单位。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `duration` | 音轨时长（Track Duration）。 |

<a id="ga61d494d7e149cfa2c3f9546c1e3b99bd"></a>

### `media_proxy_pl_track_position_cb()`

```c
void media_proxy_pl_track_position_cb ( int32_t position)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

音轨位置回调（Track Position Callback）。

媒体播放器在音轨中的位置变化，或播放器暂停等情况下调用。

例外：正常播放时位置变化不应调用此回调，即播放器正在以恒定速度播放的情况下。

音轨位置（Track Position）以从音轨起点开始的百分之一秒数表示。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `position` | 媒体播放器在音轨中的位置（Track Position）。 |

<a id="ga9489b517e4baa215f0b7b59243cee11c"></a>

### `media_proxy_pl_track_title_cb()`

```c
void media_proxy_pl_track_title_cb ( char * title)
```

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

音轨标题回调（Track Title Callback）。

播放器当前音轨（Current Track）变化时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `title` | 音轨标题（Track Title）。 |


## 7.15\_原页交叉引用（Cross References）

- [mpl_cmd](../audio_video_model_reference/P037_mpl_cmd_结构体.md)
- [mpl_cmd_ntf](../audio_video_model_reference/P038_mpl_cmd_ntf_结构体.md)
- [mpl_sci](../audio_video_model_reference/P039_mpl_sci_结构体.md)
- [mpl_search](../audio_video_model_reference/P040_mpl_search_结构体.md)
- [media_proxy_ctrl_cbs](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md)
- [media_proxy_pl_calls](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_ots](../bluetooth_service_model_reference/P135_bt_ots_结构体.md)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [zephyr/bluetooth/audio/media_proxy.h](../api_file_bluetooth_media_reference/P007_zephyr__bluetooth__audio__media_proxy.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P006_媒体控制服务（Media Control Service，MCS）.md) · [返回大纲](大纲.md) · [下一章](P008_电话承载服务（Telephone Bearer Service，TBS）.md)
