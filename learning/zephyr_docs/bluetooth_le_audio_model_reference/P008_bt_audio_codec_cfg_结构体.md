---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-8
title: bt_audio_codec_cfg_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__audio__codec__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_bt\_audio\_codec\_cfg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__audio__codec__cfg.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

编解码器专用配置结构体（Codec Specific Configuration Structure）。

```c
#include <zephyr/bluetooth/audio/audio.h>
```

<a id="details"></a>

编解码器专用配置结构体（Codec Specific Configuration Structure）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 8.1\_数据成员（Data Fields）

<a id="r_a9386056bb02908407c9e3aad48abbd87"></a>

```c
uint8_t path_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[path_id](#a9386056bb02908407c9e3aad48abbd87)。

数据路径 ID（Data Path ID）。

<a id="r_a9e2c8081950a0830ffc270245ab308c1"></a>

```c
bool ctlr_transcode
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[ctlr_transcode](#a9e2c8081950a0830ffc270245ab308c1)。

本地控制器是否应进行转码（Transcoding）。

<a id="r_aa71d0e75b36f6dc664fdcd2e092f8d57"></a>

```c
enum bt_audio_codec_cfg_target_latency target_latency
```

相关声明：[bt_audio_codec_cfg_target_latency](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga62108a3dcc3e35f7b31a99f7a33679e6)、[target_latency](#aa71d0e75b36f6dc664fdcd2e092f8d57)。

目标延迟（Target Latency）。

<a id="r_a571a8b875dd0acac50e82620dc6d9aab"></a>

```c
enum bt_audio_codec_cfg_target_phy target_phy
```

相关声明：[bt_audio_codec_cfg_target_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga640af4e254e73f5c4646e9be4e99f3d1)、[target_phy](#a571a8b875dd0acac50e82620dc6d9aab)。

目标物理层（Target PHY）。

<a id="r_aa2f99ec31ff3eb9b7b738bc8a1170f20"></a>

```c
uint8_t id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[id](#aa2f99ec31ff3eb9b7b738bc8a1170f20)。

编解码器 ID（Codec ID）。

<a id="r_a664e21bcd6002b21d4b1b53d866db32d"></a>

```c
uint16_t cid
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[cid](#a664e21bcd6002b21d4b1b53d866db32d)。

编解码器公司 ID（Codec Company ID）。

<a id="r_a2996ab3f6ae1cab09ff5e3329b42468e"></a>

```c
uint16_t vid
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[vid](#a2996ab3f6ae1cab09ff5e3329b42468e)。

编解码器公司厂商 ID（Codec Company Vendor ID）。

<a id="r_a8a5a789e9993a48ce4c83a2156c1f43c"></a>

```c
size_t data_len
```

相关声明：[data_len](#a8a5a789e9993a48ce4c83a2156c1f43c)。

编解码器专用能力数据（Codec Specific Capabilities Data）的数量。

<a id="r_ad3709d5321f6faeb392452cb3b21023b"></a>

```c
uint8_t data [CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#ad3709d5321f6faeb392452cb3b21023b)。

编解码器专用能力数据。

<a id="r_a1e69a5c017e9571b50aba721f86876fb"></a>

```c
size_t meta_len
```

相关声明：[meta_len](#a1e69a5c017e9571b50aba721f86876fb)。

编解码器专用能力元数据（Codec Specific Capabilities Metadata）的数量。

<a id="r_a4f84974ea14b773ad8e2fd7c0ffa0c7f"></a>

```c
uint8_t meta [CONFIG_BT_AUDIO_CODEC_CFG_MAX_METADATA_SIZE]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[meta](#a4f84974ea14b773ad8e2fd7c0ffa0c7f)。

编解码器专用能力元数据。

## 8.2\_详细说明（Detailed Documentation）

<a id="a664e21bcd6002b21d4b1b53d866db32d"></a>

### `cid`

```c
uint16_t bt_audio_codec_cfg::cid
```

编解码器公司 ID（Codec Company ID）。

<a id="a9e2c8081950a0830ffc270245ab308c1"></a>

### `ctlr_transcode`

```c
bool bt_audio_codec_cfg::ctlr_transcode
```

本地控制器是否应进行转码（Transcoding）。

此值为 `false` 时，等时（ISO）数据路径的编码格式实际设置为 `BT_HCI_CODING_FORMAT_TRANSPARENT`；否则使用 `bt_audio_codec_cfg::id`。

<a id="ad3709d5321f6faeb392452cb3b21023b"></a>

### `data`

```c
uint8_t bt_audio_codec_cfg::data[CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE]
```

编解码器专用能力数据。

<a id="a8a5a789e9993a48ce4c83a2156c1f43c"></a>

### `data_len`

```c
size_t bt_audio_codec_cfg::data_len
```

编解码器专用能力数据（Codec Specific Capabilities Data）的数量。

<a id="aa2f99ec31ff3eb9b7b738bc8a1170f20"></a>

### `id`

```c
uint8_t bt_audio_codec_cfg::id
```

编解码器 ID（Codec ID）。

<a id="a4f84974ea14b773ad8e2fd7c0ffa0c7f"></a>

### `meta`

```c
uint8_t bt_audio_codec_cfg::meta[CONFIG_BT_AUDIO_CODEC_CFG_MAX_METADATA_SIZE]
```

编解码器专用能力元数据。

<a id="a1e69a5c017e9571b50aba721f86876fb"></a>

### `meta_len`

```c
size_t bt_audio_codec_cfg::meta_len
```

编解码器专用能力元数据（Codec Specific Capabilities Metadata）的数量。

<a id="a9386056bb02908407c9e3aad48abbd87"></a>

### `path_id`

```c
uint8_t bt_audio_codec_cfg::path_id
```

数据路径 ID（Data Path ID）。

HCI 路径使用 `BT_ISO_DATA_PATH_HCI`，其他值表示厂商专用 ID。

<a id="aa71d0e75b36f6dc664fdcd2e092f8d57"></a>

### `target_latency`

```c
enum bt_audio_codec_cfg_target_latency bt_audio_codec_cfg::target_latency
```

目标延迟（Target Latency）。

广播流不使用此项。

<a id="a571a8b875dd0acac50e82620dc6d9aab"></a>

### `target_phy`

```c
enum bt_audio_codec_cfg_target_phy bt_audio_codec_cfg::target_phy
```

目标物理层（Target PHY）。

广播流不使用此项。

<a id="a2996ab3f6ae1cab09ff5e3329b42468e"></a>

### `vid`

```c
uint16_t bt_audio_codec_cfg::vid
```

编解码器公司厂商 ID（Codec Company Vendor ID）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/audio.h`

## 8.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/audio.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2audio_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_audio_codec_cfg_target_latency](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga62108a3dcc3e35f7b31a99f7a33679e6)
- [bt_audio_codec_cfg_target_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga640af4e254e73f5c4646e9be4e99f3d1)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [BT_HCI_CODING_FORMAT_TRANSPARENT](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#ad93af498e2265c180a01055eca2a4de0)
- [BT_ISO_DATA_PATH_HCI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gadd421c69edccfd695d728ded5feb6862)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P007_bt_audio_codec_cap_结构体.md) · [返回大纲](大纲.md) · [下一章](P009_bt_audio_codec_octets_per_codec_frame_结构体.md)
