---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-26
title: bt_bap_lc3_preset_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__lc3__preset.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_bt\_bap\_lc3\_preset\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__lc3__preset.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

保存 BAP 定义的低复杂度通信编解码器（Low Complexity Communication Codec，LC3）预设的结构体。

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

<a id="details"></a>

保存 BAP 定义的低复杂度通信编解码器（Low Complexity Communication Codec，LC3）预设的结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 26.1\_数据成员（Data Fields）

<a id="r_a2615416828c62842a076749796beb6da"></a>

```c
struct bt_audio_codec_cfg codec_cfg
```

相关声明：[bt_audio_codec_cfg](P008_bt_audio_codec_cfg_结构体.md)、[codec_cfg](#a2615416828c62842a076749796beb6da)。

LC3 编解码器。

<a id="r_a8f5954471875861bfd387446060e9565"></a>

```c
struct bt_bap_qos_cfg qos
```

相关声明：[bt_bap_qos_cfg](P027_bt_bap_qos_cfg_结构体.md)、[qos](#a8f5954471875861bfd387446060e9565)。

BAP 规范定义的 QoS 值。

## 26.2\_详细说明（Detailed Documentation）

<a id="a2615416828c62842a076749796beb6da"></a>

### `codec_cfg`

```c
struct bt_audio_codec_cfg bt_bap_lc3_preset::codec_cfg
```

LC3 编解码器。

<a id="a8f5954471875861bfd387446060e9565"></a>

### `qos`

```c
struct bt_bap_qos_cfg bt_bap_lc3_preset::qos
```

BAP 规范定义的 QoS 值。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/bap_lc3_preset.h`

## 26.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/bap_lc3_preset.h](https://docs.zephyrproject.org/latest/doxygen/html/bap__lc3__preset_8h_source.html)
- [bt_audio_codec_cfg](P008_bt_audio_codec_cfg_结构体.md)
- [bt_bap_qos_cfg](P027_bt_bap_qos_cfg_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P025_bt_bap_ep_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P027_bt_bap_qos_cfg_结构体.md)
