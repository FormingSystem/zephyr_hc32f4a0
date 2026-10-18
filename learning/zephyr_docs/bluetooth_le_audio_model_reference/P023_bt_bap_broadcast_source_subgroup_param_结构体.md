---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-23
title: bt_bap_broadcast_source_subgroup_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__broadcast__source__subgroup__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_bt\_bap\_broadcast\_source\_subgroup\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__broadcast__source__subgroup__param.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

广播音频源的子组参数（Subgroup Parameters）。

```c
#include <zephyr/bluetooth/audio/bap.h>
```

<a id="details"></a>

广播音频源的子组参数（Subgroup Parameters）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 23.1\_数据成员（Data Fields）

<a id="r_a701d9480ffae2351149de6b962095d32"></a>

```c
size_t params_count
```

相关声明：[params_count](#a701d9480ffae2351149de6b962095d32)。

`stream_params` 中的参数数量。

<a id="r_a9719e89d8979f9502023e0032814c477"></a>

```c
struct bt_bap_broadcast_source_stream_param * params
```

相关声明：[bt_bap_broadcast_source_stream_param](P022_bt_bap_broadcast_source_stream_param_结构体.md)、[params](#a9719e89d8979f9502023e0032814c477)。

流参数数组（Stream Parameters Array）。

<a id="r_a4d5d610b562fc34c8840e4eed037ba86"></a>

```c
const struct bt_audio_codec_cfg * codec_cfg
```

相关声明：[bt_audio_codec_cfg](P008_bt_audio_codec_cfg_结构体.md)、[codec_cfg](#a4d5d610b562fc34c8840e4eed037ba86)。

子组编解码器配置（Subgroup Codec Configuration）。

## 23.2\_详细说明（Detailed Documentation）

<a id="a4d5d610b562fc34c8840e4eed037ba86"></a>

### `codec_cfg`

```c
const struct bt_audio_codec_cfg* bt_bap_broadcast_source_subgroup_param::codec_cfg
```

子组编解码器配置（Subgroup Codec Configuration）。

<a id="a9719e89d8979f9502023e0032814c477"></a>

### `params`

```c
struct bt_bap_broadcast_source_stream_param* bt_bap_broadcast_source_subgroup_param::params
```

流参数数组（Stream Parameters Array）。

<a id="a701d9480ffae2351149de6b962095d32"></a>

### `params_count`

```c
size_t bt_bap_broadcast_source_subgroup_param::params_count
```

`stream_params` 中的参数数量。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/bap.h`

## 23.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h_source.html)
- [bt_bap_broadcast_source_stream_param](P022_bt_bap_broadcast_source_stream_param_结构体.md)
- [bt_audio_codec_cfg](P008_bt_audio_codec_cfg_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P022_bt_bap_broadcast_source_stream_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P024_bt_bap_ep_结构体.md)
