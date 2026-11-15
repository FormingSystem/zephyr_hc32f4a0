---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-40
title: bt_avrcp_get_play_status_rsp_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__get__play__status__rsp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_bt\_avrcp\_get\_play\_status\_rsp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__get__play__status__rsp.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

获取播放状态（GetPlayStatus）响应。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

获取播放状态（GetPlayStatus）响应。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 40.1\_数据成员（Data Fields）

<a id="r_a51c7a55875e13bb8ff442d8deef0963c"></a>

```c
uint32_t song_length
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[song_length](#a51c7a55875e13bb8ff442d8deef0963c)。

歌曲总时长，单位为毫秒。

<a id="r_a22ca5e4357d8c92cb690995973964b88"></a>

```c
uint32_t song_position
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[song_position](#a22ca5e4357d8c92cb690995973964b88)。

歌曲中的当前位置，单位为毫秒。

<a id="r_a1a2d2ba12925e8424da262a5d2698beb"></a>

```c
uint8_t play_status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[play_status](#a1a2d2ba12925e8424da262a5d2698beb)。

播放状态（Play Status），类型为 `bt_avrcp_playback_status_t`。

## 40.2\_详细说明（Detailed Documentation）

<a id="a1a2d2ba12925e8424da262a5d2698beb"></a>

### `play_status`

```c
uint8_t bt_avrcp_get_play_status_rsp::play_status
```

播放状态（Play Status），类型为 `bt_avrcp_playback_status_t`。

<a id="a51c7a55875e13bb8ff442d8deef0963c"></a>

### `song_length`

```c
uint32_t bt_avrcp_get_play_status_rsp::song_length
```

歌曲总时长，单位为毫秒。

<a id="a22ca5e4357d8c92cb690995973964b88"></a>

### `song_position`

```c
uint32_t bt_avrcp_get_play_status_rsp::song_position
```

歌曲中的当前位置，单位为毫秒。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 40.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_avrcp_playback_status_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga433775fa2758df43ee1d26c78e9122d1)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P039_bt_avrcp_get_item_attrs_rsp_结构体.md) · [返回大纲](大纲.md) · [下一章](P041_bt_avrcp_get_player_app_setting_attr_text_cmd_结构体.md)
