---
id: learning.zephyr-docs.device-power-control-model-reference.page-29
title: media_proxy_ctrl_cbs_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmedia__proxy__ctrl__cbs.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_media\_proxy\_ctrl\_cbs\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmedia__proxy__ctrl__cbs.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

媒体代理（Media Proxy）对控制器的回调。

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

<a id="details"></a>

由媒体代理（Media proxy）调用控制器的回调。控制器在注册时提供这些回调。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 29.1\_数据成员（Data Fields）

<a id="r_af2cd0f93aadd451f1b358e2d2d6a0049"></a>

```c
void(* local_player_instance )(struct media_player *player, int err)
```

相关声明：[local_player_instance](#af2cd0f93aadd451f1b358e2d2d6a0049)。

媒体播放器实例（Media Player Instance）回调。

<a id="r_a94b5ec6bc20299b722bd0e2cb28aed5e"></a>

```c
void(* player_name_recv )(struct media_player *player, int err, const char *name)
```

相关声明：[player_name_recv](#a94b5ec6bc20299b722bd0e2cb28aed5e)。

媒体播放器名称（Media Player Name）接收回调。

<a id="r_aaa7ba216e604be1c447a93231a0857d0"></a>

```c
void(* icon_id_recv )(struct media_player *player, int err, uint64_t id)
```

相关声明：[icon_id_recv](#aaa7ba216e604be1c447a93231a0857d0)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)。

媒体播放器图标对象 ID（Media Player Icon Object ID）接收回调。

<a id="r_a53c4809b7a10b9057f565411429d691b"></a>

```c
void(* icon_url_recv )(struct media_player *player, int err, const char *url)
```

相关声明：[icon_url_recv](#a53c4809b7a10b9057f565411429d691b)。

媒体播放器图标 URL（Media Player Icon URL）接收回调。

<a id="r_ade71f132ef66c7bfd13b1b1f3200681d"></a>

```c
void(* track_changed_recv )(struct media_player *player, int err)
```

相关声明：[track_changed_recv](#ade71f132ef66c7bfd13b1b1f3200681d)。

曲目变更（Track changed）接收回调。

<a id="r_ac1afc71ed04faa87e644d095ef14946f"></a>

```c
void(* track_title_recv )(struct media_player *player, int err, const char *title)
```

相关声明：[track_title_recv](#ac1afc71ed04faa87e644d095ef14946f)。

曲目标题（Track Title）接收回调。

<a id="r_a85c0bfc83bb26c74b11b5cb8182ff1e0"></a>

```c
void(* track_duration_recv )(struct media_player *player, int err, int32_t duration)
```

相关声明：[track_duration_recv](#a85c0bfc83bb26c74b11b5cb8182ff1e0)、[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)。

曲目时长（Track Duration）接收回调。

<a id="r_a6aa029523978e02dc1c8c7ff798e2433"></a>

```c
void(* track_position_recv )(struct media_player *player, int err, int32_t position)
```

相关声明：[track_position_recv](#a6aa029523978e02dc1c8c7ff798e2433)、[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)。

曲目位置（Track Position）接收回调。

<a id="r_a54f9f50e3b8f99b586a2c522a67da213"></a>

```c
void(* track_position_write )(struct media_player *player, int err, int32_t position)
```

相关声明：[track_position_write](#a54f9f50e3b8f99b586a2c522a67da213)、[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)。

曲目位置写入回调。

<a id="r_a5eb1466e8ba100c9d3cb12f097328b9e"></a>

```c
void(* playback_speed_recv )(struct media_player *player, int err, int8_t speed)
```

相关声明：[playback_speed_recv](#a5eb1466e8ba100c9d3cb12f097328b9e)、[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)。

播放速度（Playback Speed）接收回调。

<a id="r_ad84d5caca4be208bd5e5d93f5c801ddf"></a>

```c
void(* playback_speed_write )(struct media_player *player, int err, int8_t speed)
```

相关声明：[playback_speed_write](#ad84d5caca4be208bd5e5d93f5c801ddf)、[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)。

播放速度写入回调。

<a id="r_a2ba0e73f7e67c38f5abe555305753d0f"></a>

```c
void(* seeking_speed_recv )(struct media_player *player, int err, int8_t speed)
```

相关声明：[seeking_speed_recv](#a2ba0e73f7e67c38f5abe555305753d0f)、[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)。

搜索播放位置速度（Seeking Speed）接收回调。

<a id="r_aa7e7f7724689844491a4885544fc450c"></a>

```c
void(* track_segments_id_recv )(struct media_player *player, int err, uint64_t id)
```

相关声明：[track_segments_id_recv](#aa7e7f7724689844491a4885544fc450c)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)。

曲目片段对象 ID（Track Segments Object ID）接收回调。

<a id="r_aa3c2bd1734c6235eb2026915dbebc6c2"></a>

```c
void(* current_track_id_recv )(struct media_player *player, int err, uint64_t id)
```

相关声明：[current_track_id_recv](#aa3c2bd1734c6235eb2026915dbebc6c2)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)。

当前曲目对象 ID（Current Track Object ID）接收回调。

<a id="r_a66f35a59821f53f4ed9aa7dea0e4d654"></a>

```c
void(* current_track_id_write )(struct media_player *player, int err, uint64_t id)
```

相关声明：[current_track_id_write](#a66f35a59821f53f4ed9aa7dea0e4d654)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)。

当前曲目对象 ID 写入回调。

<a id="r_a5692c0d142977b8ec7a4ffb765fd0687"></a>

```c
void(* next_track_id_recv )(struct media_player *player, int err, uint64_t id)
```

相关声明：[next_track_id_recv](#a5692c0d142977b8ec7a4ffb765fd0687)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)。

下一曲目对象 ID（Next Track Object ID）接收回调。

<a id="r_a08b6fe1079b759de1f5a9f7751a22f21"></a>

```c
void(* next_track_id_write )(struct media_player *player, int err, uint64_t id)
```

相关声明：[next_track_id_write](#a08b6fe1079b759de1f5a9f7751a22f21)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)。

下一曲目对象 ID 写入回调。

<a id="r_a3c2b39bc46f8b2a7155c14dd430add8e"></a>

```c
void(* parent_group_id_recv )(struct media_player *player, int err, uint64_t id)
```

相关声明：[parent_group_id_recv](#a3c2b39bc46f8b2a7155c14dd430add8e)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)。

父分组对象 ID（Parent Group Object ID）接收回调。

<a id="r_a858a8854259c8e7a09164b916fae309a"></a>

```c
void(* current_group_id_recv )(struct media_player *player, int err, uint64_t id)
```

相关声明：[current_group_id_recv](#a858a8854259c8e7a09164b916fae309a)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)。

当前分组对象 ID（Current Group Object ID）接收回调。

<a id="r_ad1a65519a958aa27091a2ba41260db04"></a>

```c
void(* current_group_id_write )(struct media_player *player, int err, uint64_t id)
```

相关声明：[current_group_id_write](#ad1a65519a958aa27091a2ba41260db04)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)。

当前分组对象 ID 写入回调。

<a id="r_a92a3b0e3254d6b26e0d18476dce3b01e"></a>

```c
void(* playing_order_recv )(struct media_player *player, int err, uint8_t order)
```

相关声明：[playing_order_recv](#a92a3b0e3254d6b26e0d18476dce3b01e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

播放顺序（Playing Order）接收回调。

<a id="r_a67cf70c9b72a87b03009f1da0a8980f2"></a>

```c
void(* playing_order_write )(struct media_player *player, int err, uint8_t order)
```

相关声明：[playing_order_write](#a67cf70c9b72a87b03009f1da0a8980f2)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

播放顺序写入回调。

<a id="r_a85182342b606c78127f2690ac1beab7d"></a>

```c
void(* playing_orders_supported_recv )(struct media_player *player, int err, uint16_t orders)
```

相关声明：[playing_orders_supported_recv](#a85182342b606c78127f2690ac1beab7d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

支持的播放顺序（Playing Orders Supported）接收回调。

<a id="r_ad4199644afcf356a565b884129ca0cf3"></a>

```c
void(* media_state_recv )(struct media_player *player, int err, uint8_t state)
```

相关声明：[media_state_recv](#ad4199644afcf356a565b884129ca0cf3)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)。

媒体状态（Media State）接收回调。

<a id="r_a89bb28499c989a9a2ad13d40dda6c6db"></a>

```c
void(* command_send )(struct media_player *player, int err, const struct mpl_cmd *cmd)
```

相关声明：[command_send](#a89bb28499c989a9a2ad13d40dda6c6db)、[mpl_cmd](../audio_video_model_reference/P037_mpl_cmd_结构体.md)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)。

命令发送回调。

<a id="r_a90481b6563033a4520b85307e07e2e3a"></a>

```c
void(* command_recv )(struct media_player *player, int err, const struct mpl_cmd_ntf *result)
```

相关声明：[command_recv](#a90481b6563033a4520b85307e07e2e3a)、[mpl_cmd_ntf](../audio_video_model_reference/P038_mpl_cmd_ntf_结构体.md)。

命令结果接收回调。

<a id="r_a06fadb043fd0a795f872063b7950d414"></a>

```c
void(* commands_supported_recv )(struct media_player *player, int err, uint32_t opcodes)
```

相关声明：[commands_supported_recv](#a06fadb043fd0a795f872063b7950d414)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

支持的命令（Commands Supported）接收回调。

<a id="r_aee4a556023d56c3a0d4c2036b3bc0799"></a>

```c
void(* search_send )(struct media_player *player, int err, const struct mpl_search *search)
```

相关声明：[search_send](#aee4a556023d56c3a0d4c2036b3bc0799)、[mpl_search](../audio_video_model_reference/P040_mpl_search_结构体.md)。

搜索（Search）发送回调。

<a id="r_a0678ad4950c6f526c78d2143e9b7c385"></a>

```c
void(* search_recv )(struct media_player *player, int err, uint8_t result_code)
```

相关声明：[search_recv](#a0678ad4950c6f526c78d2143e9b7c385)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

搜索结果码接收回调。

<a id="r_af067e55ef7f676ad3c05f838160ed21e"></a>

```c
void(* search_results_id_recv )(struct media_player *player, int err, uint64_t id)
```

相关声明：[search_results_id_recv](#af067e55ef7f676ad3c05f838160ed21e)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)。

搜索结果对象 ID（Search Results Object ID）接收回调。另请参阅 `media_proxy_ctrl_get_search_results_id()`。

<a id="r_a08f3f55a5b56d1ede9141013fe456119"></a>

```c
void(* content_ctrl_id_recv )(struct media_player *player, int err, uint8_t ccid)
```

相关声明：[content_ctrl_id_recv](#a08f3f55a5b56d1ede9141013fe456119)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

内容控制 ID（Content Control ID）接收回调。

## 29.2\_详细说明（Detailed Documentation）

<a id="a90481b6563033a4520b85307e07e2e3a"></a>

### `command_recv`

```c
void(* media_proxy_ctrl_cbs::command_recv) (struct media_player *player, int err, const struct mpl_cmd_ntf *result)
```

命令结果接收回调。

收到命令结果时调用。另请参阅 `media_proxy_ctrl_send_command()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `result` | 收到的结果。 |

<a id="a89bb28499c989a9a2ad13d40dda6c6db"></a>

### `command_send`

```c
void(* media_proxy_ctrl_cbs::command_send) (struct media_player *player, int err, const struct mpl_cmd *cmd)
```

命令发送回调。

命令发送后调用。另请参阅 `media_proxy_ctrl_send_command()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `cmd` | 已发送的命令。 |

<a id="a06fadb043fd0a795f872063b7950d414"></a>

### `commands_supported_recv`

```c
void(* media_proxy_ctrl_cbs::commands_supported_recv) (struct media_player *player, int err, uint32_t opcodes)
```

支持的命令（Commands Supported）接收回调。

读取或更改“支持的命令”（Commands Supported）时调用。另请参阅 `media_proxy_ctrl_get_commands_supported()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `opcodes` | 支持的命令操作码（Opcodes），以位图表示。 |

<a id="a08f3f55a5b56d1ede9141013fe456119"></a>

### `content_ctrl_id_recv`

```c
void(* media_proxy_ctrl_cbs::content_ctrl_id_recv) (struct media_player *player, int err, uint8_t ccid)
```

内容控制 ID（Content Control ID）接收回调。

读取内容控制 ID 时调用。另请参阅 `media_proxy_ctrl_get_content_ctrl_id()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `ccid` | 内容控制 ID。 |

<a id="a858a8854259c8e7a09164b916fae309a"></a>

### `current_group_id_recv`

```c
void(* media_proxy_ctrl_cbs::current_group_id_recv) (struct media_player *player, int err, uint64_t id)
```

当前分组对象 ID（Current Group Object ID）接收回调。

读取或更改当前分组对象 ID 时调用。另请参阅 `media_proxy_ctrl_get_current_group_id()` 和 `media_proxy_ctrl_set_current_group_id()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `id` | 对象传输服务（Object Transfer Service）中当前分组对象的 ID，长度为 48 位。 |

<a id="ad1a65519a958aa27091a2ba41260db04"></a>

### `current_group_id_write`

```c
void(* media_proxy_ctrl_cbs::current_group_id_write) (struct media_player *player, int err, uint64_t id)
```

当前分组对象 ID 写入回调。

写入当前分组对象 ID 时调用。另请参阅 `media_proxy_ctrl_set_current_group_id()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `id` | 尝试写入的 48 位 ID。 |

<a id="aa3c2bd1734c6235eb2026915dbebc6c2"></a>

### `current_track_id_recv`

```c
void(* media_proxy_ctrl_cbs::current_track_id_recv) (struct media_player *player, int err, uint64_t id)
```

当前曲目对象 ID（Current Track Object ID）接收回调。

读取或更改当前曲目对象 ID 时调用。另请参阅 `media_proxy_ctrl_get_current_track_id()` 和 `media_proxy_ctrl_set_current_track_id()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `id` | 对象传输服务中当前曲目对象的 ID，长度为 48 位。 |

<a id="a66f35a59821f53f4ed9aa7dea0e4d654"></a>

### `current_track_id_write`

```c
void(* media_proxy_ctrl_cbs::current_track_id_write) (struct media_player *player, int err, uint64_t id)
```

当前曲目对象 ID 写入回调。

写入当前曲目对象 ID 时调用。另请参阅 `media_proxy_ctrl_set_current_track_id()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `id` | 尝试写入的 48 位 ID。 |

<a id="aaa7ba216e604be1c447a93231a0857d0"></a>

### `icon_id_recv`

```c
void(* media_proxy_ctrl_cbs::icon_id_recv) (struct media_player *player, int err, uint64_t id)
```

媒体播放器图标对象 ID（Media Player Icon Object ID）接收回调。

读取媒体播放器图标对象 ID 时调用。另请参阅 `media_proxy_ctrl_get_icon_id()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `id` | 对象传输服务中图标对象的 ID，长度为 48 位。 |

<a id="a53c4809b7a10b9057f565411429d691b"></a>

### `icon_url_recv`

```c
void(* media_proxy_ctrl_cbs::icon_url_recv) (struct media_player *player, int err, const char *url)
```

媒体播放器图标 URL（Media Player Icon URL）接收回调。

读取媒体播放器图标 URL 时调用。另请参阅 `media_proxy_ctrl_get_icon_url()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `url` | 图标的 URL。 |

<a id="af2cd0f93aadd451f1b358e2d2d6a0049"></a>

### `local_player_instance`

```c
void(* media_proxy_ctrl_cbs::local_player_instance) (struct media_player *player, int err)
```

媒体播放器实例（Media Player Instance）回调。

注册或读取本地媒体播放器实例时调用，读取部分尚待实现（TODO）。如果注册控制器时本地播放器实例已经注册，也会调用此回调。向控制器提供指向本地播放器实例的指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `err` | 错误值：成功时为 `0`，负值表示 `errno` 错误。 |

<a id="ad4199644afcf356a565b884129ca0cf3"></a>

### `media_state_recv`

```c
void(* media_proxy_ctrl_cbs::media_state_recv) (struct media_player *player, int err, uint8_t state)
```

媒体状态（Media State）接收回调。

读取或更改媒体状态时调用。另请参阅 `media_proxy_ctrl_get_media_state()` 和 `media_proxy_ctrl_send_command()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `state` | 媒体播放器状态。 |

<a id="a5692c0d142977b8ec7a4ffb765fd0687"></a>

### `next_track_id_recv`

```c
void(* media_proxy_ctrl_cbs::next_track_id_recv) (struct media_player *player, int err, uint64_t id)
```

下一曲目对象 ID（Next Track Object ID）接收回调。

读取或更改下一曲目对象 ID 时调用。另请参阅 `media_proxy_ctrl_get_next_track_id()` 和 `media_proxy_ctrl_set_next_track_id()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `id` | 对象传输服务中下一曲目对象的 ID，长度为 48 位。 |

<a id="a08b6fe1079b759de1f5a9f7751a22f21"></a>

### `next_track_id_write`

```c
void(* media_proxy_ctrl_cbs::next_track_id_write) (struct media_player *player, int err, uint64_t id)
```

下一曲目对象 ID 写入回调。

写入下一曲目对象 ID 时调用。另请参阅 `media_proxy_ctrl_set_next_track_id()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `id` | 尝试写入的 48 位 ID。 |

<a id="a3c2b39bc46f8b2a7155c14dd430add8e"></a>

### `parent_group_id_recv`

```c
void(* media_proxy_ctrl_cbs::parent_group_id_recv) (struct media_player *player, int err, uint64_t id)
```

父分组对象 ID（Parent Group Object ID）接收回调。

读取或更改父分组对象 ID 时调用。另请参阅 `media_proxy_ctrl_get_parent_group_id()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `id` | 对象传输服务中父分组对象的 ID，长度为 48 位。 |

<a id="a5eb1466e8ba100c9d3cb12f097328b9e"></a>

### `playback_speed_recv`

```c
void(* media_proxy_ctrl_cbs::playback_speed_recv) (struct media_player *player, int err, int8_t speed)
```

播放速度（Playback Speed）接收回调。

读取或更改播放速度时调用。另请参阅 `media_proxy_ctrl_get_playback_speed()` 和 `media_proxy_ctrl_set_playback_speed()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `speed` | 播放速度参数。 |

<a id="ad84d5caca4be208bd5e5d93f5c801ddf"></a>

### `playback_speed_write`

```c
void(* media_proxy_ctrl_cbs::playback_speed_write) (struct media_player *player, int err, int8_t speed)
```

播放速度写入回调。

写入播放速度时调用。另请参阅 `media_proxy_ctrl_set_playback_speed()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `speed` | 尝试写入的播放速度参数。 |

<a id="a94b5ec6bc20299b722bd0e2cb28aed5e"></a>

### `player_name_recv`

```c
void(* media_proxy_ctrl_cbs::player_name_recv) (struct media_player *player, int err, const char *name)
```

媒体播放器名称（Media Player Name）接收回调。

读取或更改媒体播放器名称时调用。另请参阅 `media_proxy_ctrl_name_get()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `name` | 媒体播放器名称。 |

<a id="a92a3b0e3254d6b26e0d18476dce3b01e"></a>

### `playing_order_recv`

```c
void(* media_proxy_ctrl_cbs::playing_order_recv) (struct media_player *player, int err, uint8_t order)
```

播放顺序（Playing Order）接收回调。

读取或更改播放顺序时调用。另请参阅 `media_proxy_ctrl_get_playing_order()` 和 `media_proxy_ctrl_set_playing_order()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `order` | 播放顺序。 |

<a id="a67cf70c9b72a87b03009f1da0a8980f2"></a>

### `playing_order_write`

```c
void(* media_proxy_ctrl_cbs::playing_order_write) (struct media_player *player, int err, uint8_t order)
```

播放顺序写入回调。

写入播放顺序时调用。另请参阅 `media_proxy_ctrl_set_playing_order()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `order` | 尝试写入的播放顺序。 |

<a id="a85182342b606c78127f2690ac1beab7d"></a>

### `playing_orders_supported_recv`

```c
void(* media_proxy_ctrl_cbs::playing_orders_supported_recv) (struct media_player *player, int err, uint16_t orders)
```

支持的播放顺序（Playing Orders Supported）接收回调。

读取“支持的播放顺序”时调用。另请参阅 `media_proxy_ctrl_get_playing_orders_supported()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `orders` | 支持的播放顺序。 |

<a id="a0678ad4950c6f526c78d2143e9b7c385"></a>

### `search_recv`

```c
void(* media_proxy_ctrl_cbs::search_recv) (struct media_player *player, int err, uint8_t result_code)
```

搜索结果码接收回调。

收到搜索结果码时调用。另请参阅 `media_proxy_ctrl_send_search()`。

搜索结果码指示搜索是否成功。搜索成功时，可以通过搜索结果对象 ID 访问实际搜索结果，即搜索找到的内容。搜索结果对象 ID 有独立的回调 `search_results_id_recv()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `result_code` | 搜索结果码。 |

<a id="af067e55ef7f676ad3c05f838160ed21e"></a>

### `search_results_id_recv`

```c
void(* media_proxy_ctrl_cbs::search_results_id_recv) (struct media_player *player, int err, uint64_t id)
```

搜索结果对象 ID（Search Results Object ID）接收回调。另请参阅 `media_proxy_ctrl_get_search_results_id()`。

读取或更改搜索结果对象 ID 时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `id` | 对象传输服务中搜索结果对象的 ID，长度为 48 位。 |

<a id="aee4a556023d56c3a0d4c2036b3bc0799"></a>

### `search_send`

```c
void(* media_proxy_ctrl_cbs::search_send) (struct media_player *player, int err, const struct mpl_search *search)
```

搜索（Search）发送回调。

搜索请求发送后调用。另请参阅 `media_proxy_ctrl_send_search()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `search` | 已发送的搜索请求。 |

<a id="a2ba0e73f7e67c38f5abe555305753d0f"></a>

### `seeking_speed_recv`

```c
void(* media_proxy_ctrl_cbs::seeking_speed_recv) (struct media_player *player, int err, int8_t speed)
```

搜索播放位置速度（Seeking Speed）接收回调。

读取或更改搜索播放位置速度（Seeking Speed）时调用。另请参阅 `media_proxy_ctrl_get_seeking_speed()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `speed` | 搜索播放位置的速度系数（Seeking speed factor）。 |

<a id="ade71f132ef66c7bfd13b1b1f3200681d"></a>

### `track_changed_recv`

```c
void(* media_proxy_ctrl_cbs::track_changed_recv) (struct media_player *player, int err)
```

曲目变更（Track changed）接收回调。

当前曲目发生变更时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |

<a id="a85c0bfc83bb26c74b11b5cb8182ff1e0"></a>

### `track_duration_recv`

```c
void(* media_proxy_ctrl_cbs::track_duration_recv) (struct media_player *player, int err, int32_t duration)
```

曲目时长（Track Duration）接收回调。

读取或更改曲目时长时调用。另请参阅 `media_proxy_ctrl_get_track_duration()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `duration` | 当前曲目的时长。 |

<a id="a6aa029523978e02dc1c8c7ff798e2433"></a>

### `track_position_recv`

```c
void(* media_proxy_ctrl_cbs::track_position_recv) (struct media_player *player, int err, int32_t position)
```

曲目位置（Track Position）接收回调。

读取或更改曲目位置时调用。另请参阅 `media_proxy_ctrl_get_track_position()` 和 `media_proxy_ctrl_set_track_position()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `position` | 播放器在曲目中的位置。 |

<a id="a54f9f50e3b8f99b586a2c522a67da213"></a>

### `track_position_write`

```c
void(* media_proxy_ctrl_cbs::track_position_write) (struct media_player *player, int err, int32_t position)
```

曲目位置写入回调。

写入曲目位置时调用。另请参阅 `media_proxy_ctrl_set_track_position()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `position` | 尝试写入的位置。 |

<a id="aa7e7f7724689844491a4885544fc450c"></a>

### `track_segments_id_recv`

```c
void(* media_proxy_ctrl_cbs::track_segments_id_recv) (struct media_player *player, int err, uint64_t id)
```

曲目片段对象 ID（Track Segments Object ID）接收回调。

读取曲目片段对象 ID 时调用。另请参阅 `media_proxy_ctrl_get_track_segments_id()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `id` | 对象传输服务中曲目片段对象的 ID，长度为 48 位。 |

<a id="ac1afc71ed04faa87e644d095ef14946f"></a>

### `track_title_recv`

```c
void(* media_proxy_ctrl_cbs::track_title_recv) (struct media_player *player, int err, const char *title)
```

曲目标题（Track Title）接收回调。

读取或更改曲目标题时调用。另请参阅 `media_proxy_ctrl_get_track_title()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `player` | 媒体播放器实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `title` | 当前曲目的标题。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/media_proxy.h`

## 29.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/media_proxy.h](https://docs.zephyrproject.org/latest/doxygen/html/media__proxy_8h_source.html)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [mpl_cmd](../audio_video_model_reference/P037_mpl_cmd_结构体.md)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [mpl_cmd_ntf](../audio_video_model_reference/P038_mpl_cmd_ntf_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [mpl_search](../audio_video_model_reference/P040_mpl_search_结构体.md)
- [media_proxy_ctrl_get_search_results_id()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga580a0c9fa47460be59f0571ee11a41b4)
- [media_proxy_ctrl_send_command()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga590762e7272b99fb8ac50a7841424670)
- [media_proxy_ctrl_get_commands_supported()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga15804287093b20d4a1616380729b33c8)
- [media_proxy_ctrl_get_content_ctrl_id()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga23488e77985a04216ec7c7fa785f09fc)
- [media_proxy_ctrl_get_current_group_id()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga2ae50a1988305b4247ff0af796b6d93e)
- [media_proxy_ctrl_set_current_group_id()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gae496885d0124f4e3fc2c0f203fcff118)
- [media_proxy_ctrl_get_current_track_id()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaebe7e3683041e28bef40df75cc991dea)
- [media_proxy_ctrl_set_current_track_id()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaea6adacedaded10f7c2c0f91b7159f74)
- [media_proxy_ctrl_get_icon_id()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga5efccb39cdb97eed476e0c0bff461ec1)
- [media_proxy_ctrl_get_icon_url()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gab6df6fe71c8273eca855eb3be27290dd)
- [media_proxy_ctrl_get_media_state()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga9433aaf24776c30557ea694795e75b3e)
- [media_proxy_ctrl_get_next_track_id()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gae32da32bd504061801730805729242e1)
- [media_proxy_ctrl_set_next_track_id()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga43b797717fb9b36b94a606dfabeb0fa7)
- [media_proxy_ctrl_get_parent_group_id()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga12dc878be39814660900ba875e13e537)
- [media_proxy_ctrl_get_playback_speed()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga2d64a23b3f881579a603a04baeb64088)
- [media_proxy_ctrl_set_playback_speed()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gabafbc857c3e6befe98e339acb58f17fb)
- [media_proxy_ctrl_get_playing_order()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga2f93bcde2460c6638880f8e6631eb68e)
- [media_proxy_ctrl_set_playing_order()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaa4040e97100f6e70527e6ad201309bbe)
- [media_proxy_ctrl_get_playing_orders_supported()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga030899757b79251f1d5a1055f65fe989)
- [media_proxy_ctrl_send_search()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga052c3fabac4a44ee2802ddd4a6c5c9ac)
- [media_proxy_ctrl_get_seeking_speed()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga817ca4ab611e214493fbc918036def0f)
- [media_proxy_ctrl_get_track_duration()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga488441418a8f2d358092019bbfe16788)
- [media_proxy_ctrl_get_track_position()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gae0bb75feb49a68b495150c6fba2f21a7)
- [media_proxy_ctrl_set_track_position()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga776bb5f16cf1f4f6cc3842aabd86b781)
- [media_proxy_ctrl_get_track_segments_id()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga1afcc097cb36c4f11141b82ce28e8126)
- [media_proxy_ctrl_get_track_title()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gabfbb49e79204130cb004f217af771b80)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P028_media_element_item_name_结构体.md) · [返回大纲](大纲.md) · [下一章](P030_media_proxy_pl_calls_结构体.md)
