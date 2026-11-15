---
id: learning.zephyr-docs.api-audio-path-topic-reference.page-1
title: 分配编号转字符串 API（Assigned numbers to string API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__to__str.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_分配编号转字符串 API（Assigned numbers to string API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__to__str.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

分配编号转字符串 API（Assigned numbers to string API）

<a id="details"></a>

分配编号转字符串（Assigned Numbers to String）API。提供函数，将蓝牙音频分配编号（Bluetooth Audio Assigned Numbers）的值转换为字符串表示。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.1\_函数（Functions）

<a id="r_ga26436fc678423ff1cf3543d381359d0f"></a>

```c
static char * bt_audio_context_bit_to_str (enum bt_audio_context context)
```

相关声明：[bt_audio_context_bit_to_str](#ga26436fc678423ff1cf3543d381359d0f)、[bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)。

返回 `bt_audio_context` 中某个特定位的字符串表示（String Representation）。

<a id="r_ga6926c4e8bda0874769177a903276c072"></a>

```c
static char * bt_audio_parental_rating_to_str (enum bt_audio_parental_rating parental_rating)
```

相关声明：[bt_audio_parental_rating_to_str](#ga6926c4e8bda0874769177a903276c072)、[bt_audio_parental_rating](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga6d4aff1f93dc0b902e4b5d1355f15760)。

返回 `bt_audio_parental_rating` 值的字符串表示（String Representation）。

<a id="r_ga1dd5865429e2438e0d4f88e891eda975"></a>

```c
static char * bt_audio_active_state_to_str (enum bt_audio_active_state state)
```

相关声明：[bt_audio_active_state_to_str](#ga1dd5865429e2438e0d4f88e891eda975)、[bt_audio_active_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga16d403ec4db7be997682331ad365ff5f)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

返回 `bt_audio_active_state` 值的字符串表示（String Representation）。

<a id="r_gadd3bac4f1f1b334cb60f5783fdc15c14"></a>

```c
static char * bt_audio_codec_cap_freq_bit_to_str (enum bt_audio_codec_cap_freq freq)
```

相关声明：[bt_audio_codec_cap_freq_bit_to_str](#gadd3bac4f1f1b334cb60f5783fdc15c14)、[bt_audio_codec_cap_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaafc1106d5d305874ee2f540c850ff5b4)。

返回 `bt_audio_codec_cap_freq` 中某个特定位的字符串表示（String Representation）。

<a id="r_ga6b9cc74dafcf03056862ae9823bce58d"></a>

```c
static char * bt_audio_codec_cap_frame_dur_bit_to_str (enum bt_audio_codec_cap_frame_dur frame_dur)
```

相关声明：[bt_audio_codec_cap_frame_dur_bit_to_str](#ga6b9cc74dafcf03056862ae9823bce58d)、[bt_audio_codec_cap_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaf37e8e19f956afb3c3a413cbaa1a21f5)。

返回 `bt_audio_codec_cap_frame_dur` 中某个特定位的字符串表示（String Representation）。

<a id="r_ga795742ed8d91e2b675fbcdaeee7a71ec"></a>

```c
static char * bt_audio_codec_cap_chan_count_bit_to_str (enum bt_audio_codec_cap_chan_count chan_count)
```

相关声明：[bt_audio_codec_cap_chan_count_bit_to_str](#ga795742ed8d91e2b675fbcdaeee7a71ec)、[bt_audio_codec_cap_chan_count](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gae695b5d17359967703f2509db1671fa5)。

返回 `bt_audio_codec_cap_chan_count` 中某个特定位的字符串表示（String Representation）。

<a id="r_gaa1b9f7166fd6e6797da65d9537357324"></a>

```c
static char * bt_audio_location_bit_to_str (enum bt_audio_location location)
```

相关声明：[bt_audio_location_bit_to_str](#gaa1b9f7166fd6e6797da65d9537357324)、[bt_audio_location](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga61230848c02098352320fe751332c4e8)。

返回 `bt_audio_location` 中某个特定位的字符串表示（String Representation）。

## 1.2\_详细说明（Detailed Documentation）

<a id="ga1dd5865429e2438e0d4f88e891eda975"></a>

### `bt_audio_active_state_to_str()`

```c
char * bt_audio_active_state_to_str ( enum bt_audio_active_state state)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/audio/audio.h>
```

返回 `bt_audio_active_state` 值的字符串表示（String Representation）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `state` | 活动状态值（Active State Value）。 |

**返回（Returns）**：返回值：所给活动状态值（Active State Value）的字符串表示。

<a id="ga795742ed8d91e2b675fbcdaeee7a71ec"></a>

### `bt_audio_codec_cap_chan_count_bit_to_str()`

```c
char * bt_audio_codec_cap_chan_count_bit_to_str ( enum bt_audio_codec_cap_chan_count chan_count)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/audio/audio.h>
```

返回 `bt_audio_codec_cap_chan_count` 中某个特定位的字符串表示（String Representation）。

若 `chan_count` 包含多个置位位，则返回 `"Unknown channel count"`，意为未知声道数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan_count` | 表示单帧声道数（Frame Channel Count）的一个位。 |

**返回（Returns）**：返回值：所给位的字符串表示（String Representation）。

<a id="ga6b9cc74dafcf03056862ae9823bce58d"></a>

### `bt_audio_codec_cap_frame_dur_bit_to_str()`

```c
char * bt_audio_codec_cap_frame_dur_bit_to_str ( enum bt_audio_codec_cap_frame_dur frame_dur)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/audio/audio.h>
```

返回 `bt_audio_codec_cap_frame_dur` 中某个特定位的字符串表示（String Representation）。

若 `frame_dur` 包含多个置位位，则返回 `"Unknown frame duration"`，意为未知帧时长。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `frame_dur` | 表示帧时长（Frame Duration）的一个位。 |

**返回（Returns）**：返回值：所给位的字符串表示（String Representation）。

<a id="gadd3bac4f1f1b334cb60f5783fdc15c14"></a>

### `bt_audio_codec_cap_freq_bit_to_str()`

```c
char * bt_audio_codec_cap_freq_bit_to_str ( enum bt_audio_codec_cap_freq freq)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/audio/audio.h>
```

返回 `bt_audio_codec_cap_freq` 中某个特定位的字符串表示（String Representation）。

若 `freq` 包含多个置位位，则返回 `"Unknown supported frequency"`，意为未知支持频率。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `freq` | 表示频率（Frequency）的一个位。 |

**返回（Returns）**：返回值：所给位的字符串表示（String Representation）。

<a id="ga26436fc678423ff1cf3543d381359d0f"></a>

### `bt_audio_context_bit_to_str()`

```c
char * bt_audio_context_bit_to_str ( enum bt_audio_context context)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/audio/audio.h>
```

返回 `bt_audio_context` 中某个特定位的字符串表示（String Representation）。

若 `context` 包含多个置位位，则返回 `"Unknown context"`，意为未知上下文。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 表示上下文（Context）的一个位。 |

**返回（Returns）**：返回值：所给位的字符串表示（String Representation）。

<a id="gaa1b9f7166fd6e6797da65d9537357324"></a>

### `bt_audio_location_bit_to_str()`

```c
char * bt_audio_location_bit_to_str ( enum bt_audio_location location)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/audio/audio.h>
```

返回 `bt_audio_location` 中某个特定位的字符串表示（String Representation）。

若 `location` 包含多个置位位，则返回 `"Unknown location"`，意为未知位置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `location` | 表示位置（Location）的一个位。 |

**返回（Returns）**：返回值：所给位的字符串表示（String Representation）。

<a id="ga6926c4e8bda0874769177a903276c072"></a>

### `bt_audio_parental_rating_to_str()`

```c
char * bt_audio_parental_rating_to_str ( enum bt_audio_parental_rating parental_rating)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/audio/audio.h>
```

返回 `bt_audio_parental_rating` 值的字符串表示（String Representation）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `parental_rating` | 家长分级值（Parental Rating Value）。 |

**返回（Returns）**：返回值：所给家长分级值（Parental Rating Value）的字符串表示。


## 1.3\_原页交叉引用（Cross References）

- [bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)
- [bt_audio_parental_rating](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga6d4aff1f93dc0b902e4b5d1355f15760)
- [bt_audio_active_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga16d403ec4db7be997682331ad365ff5f)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [bt_audio_codec_cap_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaafc1106d5d305874ee2f540c850ff5b4)
- [bt_audio_codec_cap_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaf37e8e19f956afb3c3a413cbaa1a21f5)
- [bt_audio_codec_cap_chan_count](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gae695b5d17359967703f2509db1671fa5)
- [bt_audio_location](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga61230848c02098352320fe751332c4e8)
- [zephyr/bluetooth/audio/audio.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2audio_8h.html)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_BAP 广播接收端 API（Broadcast Sink APIs）.md)
