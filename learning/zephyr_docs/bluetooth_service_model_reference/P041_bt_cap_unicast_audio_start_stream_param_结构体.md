---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-41
title: bt_cap_unicast_audio_start_stream_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__unicast__audio__start__stream__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第41章\_bt\_cap\_unicast\_audio\_start\_stream\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__unicast__audio__start__stream__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

`bt_cap_initiator_unicast_audio_start()` 函数的流专用参数（Stream Specific Parameters）。

```c
#include <zephyr/bluetooth/audio/cap.h>
```

<a id="details"></a>

`bt_cap_initiator_unicast_audio_start()` 函数的流专用参数（Stream Specific Parameters）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 41.1\_数据成员（Data Fields）

<a id="r_a9613a24e05a362a2f70d8e433ca6b42b"></a>

```c
union bt_cap_set_member member
```

相关声明：[bt_cap_set_member](P188_bt_cap_set_member_联合体.md)、[member](#a9613a24e05a362a2f70d8e433ca6b42b)。

协调集合或临时集合成员（Coordinated or ad-hoc set member）。

<a id="r_a109acdedd1249ea8342f06de28989d4e"></a>

```c
struct bt_cap_stream * stream
```

相关声明：[bt_cap_stream](P039_bt_cap_stream_结构体.md)、[stream](#a109acdedd1249ea8342f06de28989d4e)。

此成员的流（Stream）。

<a id="r_aa9a13263d287a2ddb241a8dc13baeffb"></a>

```c
struct bt_bap_ep * ep
```

相关声明：[bt_bap_ep](../bluetooth_le_audio_model_reference/P024_bt_bap_ep_结构体.md)、[ep](#aa9a13263d287a2ddb241a8dc13baeffb)。

流的端点引用（Endpoint reference）。

<a id="r_abbc53d6bfad43e1b211bb8003b7eea88"></a>

```c
const struct bt_audio_codec_cfg * codec_cfg
```

相关声明：[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[codec_cfg](#abbc53d6bfad43e1b211bb8003b7eea88)。

编解码器配置（Codec Configuration）。

## 41.2\_详细说明（Detailed Documentation）

<a id="abbc53d6bfad43e1b211bb8003b7eea88"></a>

### `codec_cfg`

```c
const struct bt_audio_codec_cfg* bt_cap_unicast_audio_start_stream_param::codec_cfg
```

编解码器配置（Codec Configuration）。

`codec_cfg.meta` 必须包含内容控制标识符列表（CCIDs，`BT_AUDIO_METADATA_TYPE_CCID_LIST`），以及非零的流上下文位域（Stream context，`BT_AUDIO_METADATA_TYPE_STREAM_CONTEXT`）。

此值分配给该流，并且在流处于非空闲状态（Non-idle）期间必须始终有效。

<a id="aa9a13263d287a2ddb241a8dc13baeffb"></a>

### `ep`

```c
struct bt_bap_ep* bt_cap_unicast_audio_start_stream_param::ep
```

流的端点引用（Endpoint reference）。

<a id="a9613a24e05a362a2f70d8e433ca6b42b"></a>

### `member`

```c
union bt_cap_set_member bt_cap_unicast_audio_start_stream_param::member
```

协调集合或临时集合成员（Coordinated or ad-hoc set member）。

<a id="a109acdedd1249ea8342f06de28989d4e"></a>

### `stream`

```c
struct bt_cap_stream* bt_cap_unicast_audio_start_stream_param::stream
```

此成员的流（Stream）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/cap.h`

## 41.3\_原页交叉引用（Cross References）

- [bt_cap_initiator_unicast_audio_start()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gae19686be7f8aef1cc92c70fea93e1184)
- [zephyr/bluetooth/audio/cap.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html)
- [bt_cap_set_member](P188_bt_cap_set_member_联合体.md)
- [bt_cap_stream](P039_bt_cap_stream_结构体.md)
- [bt_bap_ep](../bluetooth_le_audio_model_reference/P024_bt_bap_ep_结构体.md)
- [bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)
- [BT_AUDIO_METADATA_TYPE_CCID_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354a37b5552e04734392dc6c6eb9e19b377b)
- [BT_AUDIO_METADATA_TYPE_STREAM_CONTEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354a95f128b11584ee22100ae65ce751dbaa)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P040_bt_cap_unicast_audio_start_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P042_bt_cap_unicast_audio_stop_param_结构体.md)
