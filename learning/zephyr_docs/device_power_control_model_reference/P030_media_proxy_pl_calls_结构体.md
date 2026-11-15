---
id: learning.zephyr-docs.device-power-control-model-reference.page-30
title: media_proxy_pl_calls_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmedia__proxy__pl__calls.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_media\_proxy\_pl\_calls\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmedia__proxy__pl__calls.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

播放器中可由媒体代理（Media Proxy）调用的接口。

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

<a id="details"></a>

播放器向媒体代理（Media proxy）提供的可调用操作，由播放器在注册时提供。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 30.1\_数据成员（Data Fields）

<a id="r_a2946f7572e12ffabc5f6ba2f562d52cf"></a>

```c
const char *(* get_player_name )(void)
```

相关声明：[get_player_name](#a2946f7572e12ffabc5f6ba2f562d52cf)。

读取媒体播放器名称（Media Player Name）。

<a id="r_acb3d3656aaed8c2801b7f4a5d40206f5"></a>

```c
void(* set_player_name )(const char *name)
```

相关声明：[set_player_name](#acb3d3656aaed8c2801b7f4a5d40206f5)。

设置媒体播放器名称。

<a id="r_ad1215725454c6b76dcdc197a275c03cf"></a>

```c
uint64_t(* get_icon_id )(void)
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[get_icon_id](#ad1215725454c6b76dcdc197a275c03cf)。

读取图标对象 ID（Icon Object ID）。

<a id="r_a319dd309f94c45292613ab9caa0e399b"></a>

```c
const char *(* get_icon_url )(void)
```

相关声明：[get_icon_url](#a319dd309f94c45292613ab9caa0e399b)。

读取图标 URL。

<a id="r_af9fc0af545c8c28f8f4dbf8c6afb4acf"></a>

```c
const char *(* get_track_title )(void)
```

相关声明：[get_track_title](#af9fc0af545c8c28f8f4dbf8c6afb4acf)。

读取曲目标题（Track Title）。

<a id="r_a1b852ccc45a6ee1174b9d58df3b599b6"></a>

```c
int32_t(* get_track_duration )(void)
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[get_track_duration](#a1b852ccc45a6ee1174b9d58df3b599b6)。

读取曲目时长（Track Duration）。

<a id="r_a11ea1cf984a7d11ac7e61405df84ee06"></a>

```c
int32_t(* get_track_position )(void)
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[get_track_position](#a11ea1cf984a7d11ac7e61405df84ee06)。

读取曲目位置（Track Position）。

<a id="r_a001ae07161b8a6c7dfc9c2e471f229e5"></a>

```c
void(* set_track_position )(int32_t position)
```

相关声明：[set_track_position](#a001ae07161b8a6c7dfc9c2e471f229e5)、[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)。

设置曲目位置。

<a id="r_ae1006d5c684e12e1e1c927f71aa93930"></a>

```c
int8_t(* get_playback_speed )(void)
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[get_playback_speed](#ae1006d5c684e12e1e1c927f71aa93930)。

获取播放速度（Playback Speed）。

<a id="r_a7535dad9be2f4b83c8a7c55fccc8a7af"></a>

```c
void(* set_playback_speed )(int8_t speed)
```

相关声明：[set_playback_speed](#a7535dad9be2f4b83c8a7c55fccc8a7af)、[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)。

设置播放速度。

<a id="r_aebf24b582cf33786f2dc17765d858a15"></a>

```c
int8_t(* get_seeking_speed )(void)
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[get_seeking_speed](#aebf24b582cf33786f2dc17765d858a15)。

获取搜索播放位置速度（Seeking Speed）。

<a id="r_a86a71b788b54a4e7c966f162fcab6433"></a>

```c
uint64_t(* get_track_segments_id )(void)
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[get_track_segments_id](#a86a71b788b54a4e7c966f162fcab6433)。

读取当前曲目片段对象 ID（Current Track Segments Object ID）。

<a id="r_a7f19bd75114835d151ff5b26733ed450"></a>

```c
uint64_t(* get_current_track_id )(void)
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[get_current_track_id](#a7f19bd75114835d151ff5b26733ed450)。

读取当前曲目对象 ID（Current Track Object ID）。

<a id="r_a422cec33063313a9aab86baf0bd65ef1"></a>

```c
void(* set_current_track_id )(uint64_t id)
```

相关声明：[set_current_track_id](#a422cec33063313a9aab86baf0bd65ef1)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)。

设置当前曲目对象 ID。

<a id="r_af939a96fbcfe474dfcdcfb353ae0aac5"></a>

```c
uint64_t(* get_next_track_id )(void)
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[get_next_track_id](#af939a96fbcfe474dfcdcfb353ae0aac5)。

读取下一曲目对象 ID（Next Track Object ID）。

<a id="r_acbf8dc9dcc8fbaba44d436310c92f3a9"></a>

```c
void(* set_next_track_id )(uint64_t id)
```

相关声明：[set_next_track_id](#acbf8dc9dcc8fbaba44d436310c92f3a9)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)。

设置下一曲目对象 ID。

<a id="r_a1409764199d47d0c27d07e13c8fa8f68"></a>

```c
uint64_t(* get_parent_group_id )(void)
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[get_parent_group_id](#a1409764199d47d0c27d07e13c8fa8f68)。

读取父分组对象 ID（Parent Group Object ID）。

<a id="r_a98b02d4689cd5e279f43094f3ca09339"></a>

```c
uint64_t(* get_current_group_id )(void)
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[get_current_group_id](#a98b02d4689cd5e279f43094f3ca09339)。

读取当前分组对象 ID（Current Group Object ID）。

<a id="r_a5049e21965e7fd08aaeafcbedf76809c"></a>

```c
void(* set_current_group_id )(uint64_t id)
```

相关声明：[set_current_group_id](#a5049e21965e7fd08aaeafcbedf76809c)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)。

设置当前分组对象 ID。

<a id="r_a98989105d01265de4b268b623a26df2e"></a>

```c
uint8_t(* get_playing_order )(void)
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[get_playing_order](#a98989105d01265de4b268b623a26df2e)。

读取播放顺序（Playing Order）。

<a id="r_ad6fad92957146aeaf1bec0e56606da72"></a>

```c
void(* set_playing_order )(uint8_t order)
```

相关声明：[set_playing_order](#ad6fad92957146aeaf1bec0e56606da72)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置播放顺序。

<a id="r_a9b733c3187cc032ef6644a16ffd3f7c9"></a>

```c
uint16_t(* get_playing_orders_supported )(void)
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[get_playing_orders_supported](#a9b733c3187cc032ef6644a16ffd3f7c9)。

读取支持的播放顺序（Playing Orders Supported）。

<a id="r_a6a339aa7ee564acacffd2637eeb8e7ea"></a>

```c
uint8_t(* get_media_state )(void)
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[get_media_state](#a6a339aa7ee564acacffd2637eeb8e7ea)。

读取媒体状态（Media State）。

<a id="r_abae1ff89136b93ce4dee5dbe12e6791d"></a>

```c
void(* send_command )(const struct mpl_cmd *command)
```

相关声明：[send_command](#abae1ff89136b93ce4dee5dbe12e6791d)、[mpl_cmd](../audio_video_model_reference/P037_mpl_cmd_结构体.md)。

发送命令。

<a id="r_ae0a4457fcc35d32541f2557698d5aa83"></a>

```c
uint32_t(* get_commands_supported )(void)
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[get_commands_supported](#ae0a4457fcc35d32541f2557698d5aa83)。

读取支持的命令（Commands Supported）。

<a id="r_a416ca20a05a66f4ce28635159173f064"></a>

```c
void(* send_search )(const struct mpl_search *search)
```

相关声明：[send_search](#a416ca20a05a66f4ce28635159173f064)、[mpl_search](../audio_video_model_reference/P040_mpl_search_结构体.md)。

设置搜索（Search）。

<a id="r_adf4003ba8ef1a5c38b75876f864564c5"></a>

```c
uint64_t(* get_search_results_id )(void)
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[get_search_results_id](#adf4003ba8ef1a5c38b75876f864564c5)。

读取搜索结果对象 ID（Search Results Object ID）。

<a id="r_a64bc23cc61e69b1b6c4050f76a9bc674"></a>

```c
uint8_t(* get_content_ctrl_id )(void)
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[get_content_ctrl_id](#a64bc23cc61e69b1b6c4050f76a9bc674)。

读取内容控制 ID（Content Control ID）。

## 30.2\_详细说明（Detailed Documentation）

<a id="ae0a4457fcc35d32541f2557698d5aa83"></a>

### `get_commands_supported`

```c
uint32_t(* media_proxy_pl_calls::get_commands_supported) (void)
```

读取支持的命令（Commands Supported）。

读取包含媒体播放器所支持命令操作码的位图。参见 `MEDIA_PROXY_OP_SUP_*` 定义。

**返回（Returns）**：返回值：媒体播放器支持的命令操作码。

<a id="a64bc23cc61e69b1b6c4050f76a9bc674"></a>

### `get_content_ctrl_id`

```c
uint8_t(* media_proxy_pl_calls::get_content_ctrl_id) (void)
```

读取内容控制 ID（Content Control ID）。

内容控制 ID 用于标识设备上的内容控制服务，并将其与相应的音频流关联。

**返回（Returns）**：返回值：媒体播放器的内容控制 ID。

<a id="a98b02d4689cd5e279f43094f3ca09339"></a>

### `get_current_group_id`

```c
uint64_t(* media_proxy_pl_calls::get_current_group_id) (void)
```

读取当前分组对象 ID（Current Group Object ID）。

获取一个 48 位 ID，通过该 ID 可从对象传输服务（Object Transfer Service）取得当前曲目对象（Current Track Object）。

当前分组对象的说明见《媒体控制服务》（Media Control Service）规范 v1.0 第 3.14 节和第 4.4 节。

**返回（Returns）**：返回值：当前分组对象 ID。

<a id="a7f19bd75114835d151ff5b26733ed450"></a>

### `get_current_track_id`

```c
uint64_t(* media_proxy_pl_calls::get_current_track_id) (void)
```

读取当前曲目对象 ID（Current Track Object ID）。

获取一个 48 位 ID，通过该 ID 可从对象传输服务（Object Transfer Service）取得当前曲目对象（Current Track Object）。

当前曲目对象的说明见《媒体控制服务》规范 v1.0 第 3.11 节和第 4.3 节。

**返回（Returns）**：返回值：当前曲目对象 ID。

<a id="ad1215725454c6b76dcdc197a275c03cf"></a>

### `get_icon_id`

```c
uint64_t(* media_proxy_pl_calls::get_icon_id) (void)
```

读取图标对象 ID（Icon Object ID）。

获取一个 48 位 ID，通过该 ID 可从对象传输服务取得图标对象（Icon Object）。

图标对象的说明见《媒体控制服务》规范 v1.0 第 3.2 节和第 4.1 节。

**返回（Returns）**：返回值：图标对象 ID。

<a id="a319dd309f94c45292613ab9caa0e399b"></a>

### `get_icon_url`

```c
const char *(* media_proxy_pl_calls::get_icon_url) (void)
```

读取图标 URL。

获取媒体播放器图标的 URL。

**返回（Returns）**：返回值：图标的 URL。

<a id="a6a339aa7ee564acacffd2637eeb8e7ea"></a>

### `get_media_state`

```c
uint8_t(* media_proxy_pl_calls::get_media_state) (void)
```

读取媒体状态（Media State）。

读取媒体播放器状态，参见 `MEDIA_PROXY_MEDIA_STATE_*` 定义。

**返回（Returns）**：返回值：媒体播放器状态。

<a id="af939a96fbcfe474dfcdcfb353ae0aac5"></a>

### `get_next_track_id`

```c
uint64_t(* media_proxy_pl_calls::get_next_track_id) (void)
```

读取下一曲目对象 ID（Next Track Object ID）。

获取一个 48 位 ID，通过该 ID 可从对象传输服务取得下一曲目对象（Next Track Object）。

**返回（Returns）**：返回值：下一曲目对象 ID。

<a id="a1409764199d47d0c27d07e13c8fa8f68"></a>

### `get_parent_group_id`

```c
uint64_t(* media_proxy_pl_calls::get_parent_group_id) (void)
```

读取父分组对象 ID（Parent Group Object ID）。

获取一个 48 位 ID，通过该 ID 可从对象传输服务取得父曲目对象（Parent Track Object）。

译注：原文使用 `Parent Track Object`；相关接口和相邻说明使用父分组对象（Parent Group Object）。此处保留原文称谓并指出差异。

父分组是当前分组的上级分组。

当前曲目对象的说明见《媒体控制服务》规范 v1.0 第 3.14 节和第 4.4 节。

译注：原文在此使用 `Current Track Object`；相邻父分组说明及上述章节编号指向分组对象，保留原文表述供对照。

**返回（Returns）**：返回值：当前分组对象 ID。

<a id="ae1006d5c684e12e1e1c927f71aa93930"></a>

### `get_playback_speed`

```c
int8_t(* media_proxy_pl_calls::get_playback_speed) (void)
```

获取播放速度（Playback Speed）。

播放速度参数与实际播放速度的关系如下：`实际播放速度 = 2^(speed_parameter/64)`。

速度参数为 `0` 时表示 1 倍速播放，即正常速度。参数为 `-128` 时表示正常速度的四分之一；参数为 `127` 时表示接近正常速度的四倍。

**返回（Returns）**：返回值：播放速度参数。

<a id="a2946f7572e12ffabc5f6ba2f562d52cf"></a>

### `get_player_name`

```c
const char *(* media_proxy_pl_calls::get_player_name) (void)
```

读取媒体播放器名称（Media Player Name）。

**返回（Returns）**：返回值：媒体播放器名称。

<a id="a98989105d01265de4b268b623a26df2e"></a>

### `get_playing_order`

```c
uint8_t(* media_proxy_pl_calls::get_playing_order) (void)
```

读取播放顺序（Playing Order）。

**返回（Returns）**：返回值：媒体播放器当前的播放顺序。

<a id="a9b733c3187cc032ef6644a16ffd3f7c9"></a>

### `get_playing_orders_supported`

```c
uint16_t(* media_proxy_pl_calls::get_playing_orders_supported) (void)
```

读取支持的播放顺序（Playing Orders Supported）。

读取包含媒体播放器所支持播放顺序的位图。参见 `MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_*` 定义。

**返回（Returns）**：返回值：媒体播放器支持的播放顺序。

<a id="adf4003ba8ef1a5c38b75876f864564c5"></a>

### `get_search_results_id`

```c
uint64_t(* media_proxy_pl_calls::get_search_results_id) (void)
```

读取搜索结果对象 ID（Search Results Object ID）。

获取一个 48 位 ID，通过该 ID 可从对象传输服务取得搜索结果对象（Search Results Object）。

搜索结果对象属于分组对象（Group object）。仅在执行过成功的搜索操作后，搜索结果对象才存在。

**返回（Returns）**：返回值：搜索结果对象 ID。

<a id="aebf24b582cf33786f2dc17765d858a15"></a>

### `get_seeking_speed`

```c
int8_t(* media_proxy_pl_calls::get_seeking_speed) (void)
```

获取搜索播放位置速度（Seeking Speed）。

搜索播放位置速度（Seeking speed）表示播放器移动播放位置的速度，是相对于实时播放速度的系数。例如，系数为 4 表示以实时播放速度的四倍搜索位置。正值表示向前搜索，负值表示向后搜索。

搜索播放位置速度不能直接设置；非零值是执行快退（Fast rewind）或快进（Fast forward）命令的结果。

**返回（Returns）**：返回值：搜索播放位置的速度系数。

<a id="a1b852ccc45a6ee1174b9d58df3b599b6"></a>

### `get_track_duration`

```c
int32_t(* media_proxy_pl_calls::get_track_duration) (void)
```

读取曲目时长（Track Duration）。

曲目时长以百分之一秒为单位。

**返回（Returns）**：返回值：当前曲目的时长。

<a id="a11ea1cf984a7d11ac7e61405df84ee06"></a>

### `get_track_position`

```c
int32_t(* media_proxy_pl_calls::get_track_position) (void)
```

读取曲目位置（Track Position）。

播放器的位置，即播放位置，以距曲目开头的百分之一秒数表示。

**返回（Returns）**：返回值：播放器在当前曲目中的位置。

<a id="a86a71b788b54a4e7c966f162fcab6433"></a>

### `get_track_segments_id`

```c
uint64_t(* media_proxy_pl_calls::get_track_segments_id) (void)
```

读取当前曲目片段对象 ID（Current Track Segments Object ID）。

获取一个 48 位 ID，通过该 ID 可从对象传输服务取得当前曲目片段对象（Current Track Segments Object）。

曲目片段对象的说明见《媒体控制服务》规范 v1.0 第 3.10 节和第 4.2 节。

**返回（Returns）**：返回值：当前曲目片段对象 ID。原文此处的 `Current The` 为重复措辞。

<a id="af9fc0af545c8c28f8f4dbf8c6afb4acf"></a>

### `get_track_title`

```c
const char *(* media_proxy_pl_calls::get_track_title) (void)
```

读取曲目标题（Track Title）。

**返回（Returns）**：返回值：当前曲目的标题。

<a id="abae1ff89136b93ce4dee5dbe12e6791d"></a>

### `send_command`

```c
void(* media_proxy_pl_calls::send_command) (const struct mpl_cmd *command)
```

发送命令。

向媒体播放器发送命令。播放、暂停等命令的操作码见 `MEDIA_PROXY_OP_*` 定义。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `command` | 要发送的命令。 |

<a id="a416ca20a05a66f4ce28635159173f064"></a>

### `send_search`

```c
void(* media_proxy_pl_calls::send_search) (const struct mpl_search *search)
```

设置搜索（Search）。

向媒体播放器写入搜索请求。搜索格式见《媒体控制服务》规范及 `mcs.h` 文件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `search` | 要写入的搜索请求。 |

<a id="a5049e21965e7fd08aaeafcbedf76809c"></a>

### `set_current_group_id`

```c
void(* media_proxy_pl_calls::set_current_group_id) (uint64_t id)
```

设置当前分组对象 ID。

将播放器的当前分组切换为给定 ID 对应的分组，并将当前曲目切换为该分组中的第一首曲目。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `id` | 分组对象的 ID。 |

<a id="a422cec33063313a9aab86baf0bd65ef1"></a>

### `set_current_track_id`

```c
void(* media_proxy_pl_calls::set_current_track_id) (uint64_t id)
```

设置当前曲目对象 ID。

将播放器的当前曲目切换为给定 ID 对应的曲目，行为类似于跳转曲目（Goto track）命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `id` | 曲目对象的 ID。 |

<a id="acbf8dc9dcc8fbaba44d436310c92f3a9"></a>

### `set_next_track_id`

```c
void(* media_proxy_pl_calls::set_next_track_id) (uint64_t id)
```

设置下一曲目对象 ID。

将播放器的下一曲目切换为给定 ID 对应的曲目。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `id` | 曲目对象的 ID。 |

<a id="a7535dad9be2f4b83c8a7c55fccc8a7af"></a>

### `set_playback_speed`

```c
void(* media_proxy_pl_calls::set_playback_speed) (int8_t speed)
```

设置播放速度。

播放速度参数的说明见 `get_playback_speed()` 函数。

注意：媒体播放器可能不支持播放速度参数的所有取值。如果给定值不受支持且高于当前值，播放器应将播放速度设为下一个更高的受支持值；相应地，若给定值低于当前值，应设为下一个更低的受支持值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `speed` | 要设置的播放速度参数。 |

<a id="acb3d3656aaed8c2801b7f4a5d40206f5"></a>

### `set_player_name`

```c
void(* media_proxy_pl_calls::set_player_name) (const char *name)
```

设置媒体播放器名称。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 新的媒体播放器名称。 |

<a id="ad6fad92957146aeaf1bec0e56606da72"></a>

### `set_playing_order`

```c
void(* media_proxy_pl_calls::set_playing_order) (uint8_t order)
```

设置播放顺序。

设置媒体播放器的播放顺序，参见 `MEDIA_PROXY_PLAYING_ORDER_*` 定义。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `order` | 要设置的播放顺序。 |

<a id="a001ae07161b8a6c7dfc9c2e471f229e5"></a>

### `set_track_position`

```c
void(* media_proxy_pl_calls::set_track_position) (int32_t position)
```

设置曲目位置。

设置媒体播放器在当前曲目中的播放位置。位置以百分之一秒为单位：正值从曲目开头计算，负值从曲目结尾向前计算。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `position` | 要设置的播放器位置。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/media_proxy.h`

## 30.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/media_proxy.h](https://docs.zephyrproject.org/latest/doxygen/html/media__proxy_8h_source.html)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [mpl_cmd](../audio_video_model_reference/P037_mpl_cmd_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [mpl_search](../audio_video_model_reference/P040_mpl_search_结构体.md)
- [mcs.h](https://docs.zephyrproject.org/latest/doxygen/html/mcs_8h.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P029_media_proxy_ctrl_cbs_结构体.md) · [返回大纲](大纲.md) · [下一章](P031_mfd_adp5585_config_结构体.md)
