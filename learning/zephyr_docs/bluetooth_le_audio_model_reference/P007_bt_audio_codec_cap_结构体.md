---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-7
title: bt_audio_codec_cap_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__audio__codec__cap.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_bt\_audio\_codec\_cap\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__audio__codec__cap.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

编解码器能力结构体（Codec Capability Structure）。

```c
#include <zephyr/bluetooth/audio/audio.h>
```

<a id="details"></a>

编解码器能力结构体（Codec Capability Structure）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 7.1\_数据成员（Data Fields）

<a id="r_a822a06f815091cc580ca2e5bbb3126f7"></a>

```c
uint8_t path_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[path_id](#a822a06f815091cc580ca2e5bbb3126f7)。

数据路径 ID（Data Path ID）。

<a id="r_a900a77db09e72de61d4ff652c6dbb10b"></a>

```c
bool ctlr_transcode
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[ctlr_transcode](#a900a77db09e72de61d4ff652c6dbb10b)。

本地控制器是否应进行转码（Transcoding）。

<a id="r_ae3892731e7ca05f3ec426c70f0d9e1a9"></a>

```c
uint8_t id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[id](#ae3892731e7ca05f3ec426c70f0d9e1a9)。

编解码器 ID（Codec ID）。

<a id="r_a763222d12a87958a5ba806303f98829a"></a>

```c
uint16_t cid
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[cid](#a763222d12a87958a5ba806303f98829a)。

编解码器公司 ID（Codec Company ID）。

<a id="r_a3b91269e16a3d63b3128a527caa5e3ff"></a>

```c
uint16_t vid
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[vid](#a3b91269e16a3d63b3128a527caa5e3ff)。

编解码器公司厂商 ID（Codec Company Vendor ID）。

<a id="r_acf3e22c6db1533fff7015acbc7eca196"></a>

```c
size_t data_len
```

相关声明：[data_len](#acf3e22c6db1533fff7015acbc7eca196)。

编解码器专用能力数据（Codec Specific Capabilities Data）的数量。

<a id="r_a455638aac9167d288a1e7a9fccabc49d"></a>

```c
uint8_t data [CONFIG_BT_AUDIO_CODEC_CAP_MAX_DATA_SIZE]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#a455638aac9167d288a1e7a9fccabc49d)。

编解码器专用能力数据。

<a id="r_afe806521d5aac36e9f6c6a0598500a8f"></a>

```c
size_t meta_len
```

相关声明：[meta_len](#afe806521d5aac36e9f6c6a0598500a8f)。

编解码器专用能力元数据（Codec Specific Capabilities Metadata）的数量。

<a id="r_acec4f5e31752d81d4dbf441223e7f44c"></a>

```c
uint8_t meta [CONFIG_BT_AUDIO_CODEC_CAP_MAX_METADATA_SIZE]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[meta](#acec4f5e31752d81d4dbf441223e7f44c)。

编解码器专用能力元数据。

## 7.2\_详细说明（Detailed Documentation）

<a id="a763222d12a87958a5ba806303f98829a"></a>

### `cid`

```c
uint16_t bt_audio_codec_cap::cid
```

编解码器公司 ID（Codec Company ID）。

<a id="a900a77db09e72de61d4ff652c6dbb10b"></a>

### `ctlr_transcode`

```c
bool bt_audio_codec_cap::ctlr_transcode
```

本地控制器是否应进行转码（Transcoding）。

此值为 `false` 时，等时（ISO）数据路径的编码格式实际设置为 `BT_HCI_CODING_FORMAT_TRANSPARENT`；否则使用 `bt_audio_codec_cfg::id`。

<a id="a455638aac9167d288a1e7a9fccabc49d"></a>

### `data`

```c
uint8_t bt_audio_codec_cap::data[CONFIG_BT_AUDIO_CODEC_CAP_MAX_DATA_SIZE]
```

编解码器专用能力数据。

<a id="acf3e22c6db1533fff7015acbc7eca196"></a>

### `data_len`

```c
size_t bt_audio_codec_cap::data_len
```

编解码器专用能力数据（Codec Specific Capabilities Data）的数量。

<a id="ae3892731e7ca05f3ec426c70f0d9e1a9"></a>

### `id`

```c
uint8_t bt_audio_codec_cap::id
```

编解码器 ID（Codec ID）。

<a id="acec4f5e31752d81d4dbf441223e7f44c"></a>

### `meta`

```c
uint8_t bt_audio_codec_cap::meta[CONFIG_BT_AUDIO_CODEC_CAP_MAX_METADATA_SIZE]
```

编解码器专用能力元数据。

<a id="afe806521d5aac36e9f6c6a0598500a8f"></a>

### `meta_len`

```c
size_t bt_audio_codec_cap::meta_len
```

编解码器专用能力元数据（Codec Specific Capabilities Metadata）的数量。

<a id="a822a06f815091cc580ca2e5bbb3126f7"></a>

### `path_id`

```c
uint8_t bt_audio_codec_cap::path_id
```

数据路径 ID（Data Path ID）。

HCI 路径使用 `BT_ISO_DATA_PATH_HCI`，其他值表示厂商专用 ID。

<a id="a3b91269e16a3d63b3128a527caa5e3ff"></a>

### `vid`

```c
uint16_t bt_audio_codec_cap::vid
```

编解码器公司厂商 ID（Codec Company Vendor ID）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/audio.h`

## 7.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/audio.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2audio_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [BT_HCI_CODING_FORMAT_TRANSPARENT](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#ad93af498e2265c180a01055eca2a4de0)
- [bt_audio_codec_cfg::id](P008_bt_audio_codec_cfg_结构体.md#aa2f99ec31ff3eb9b7b738bc8a1170f20)
- [BT_ISO_DATA_PATH_HCI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gadd421c69edccfd695d728ded5feb6862)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P006_bt_ascs_register_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P008_bt_audio_codec_cfg_结构体.md)
