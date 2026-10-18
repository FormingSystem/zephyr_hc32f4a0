---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-147
title: bt_pacs_cap_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__pacs__cap.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第147章\_bt\_pacs\_cap\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__pacs__cap.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

已发布音频能力（Published Audio Capability）结构。

```c
#include <zephyr/bluetooth/audio/pacs.h>
```

<a id="details"></a>

已发布音频能力（Published Audio Capability）结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 147.1\_数据成员（Data Fields）

<a id="r_a2f311677a17aacec91f1ab7e1a7c787f"></a>

```c
const struct bt_audio_codec_cap * codec_cap
```

相关声明：[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[codec_cap](#a2f311677a17aacec91f1ab7e1a7c787f)。

编解码器能力（Codec capability）引用。

## 147.2\_详细说明（Detailed Documentation）

<a id="a2f311677a17aacec91f1ab7e1a7c787f"></a>

### `codec_cap`

```c
const struct bt_audio_codec_cap* bt_pacs_cap::codec_cap
```

编解码器能力（Codec capability）引用。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/pacs.h`

## 147.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/pacs.h](https://docs.zephyrproject.org/latest/doxygen/html/pacs_8h_source.html)
- [bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P146_bt_ots_obj_type_结构体.md) · [返回大纲](大纲.md) · [下一章](P148_bt_pacs_register_param_结构体.md)
