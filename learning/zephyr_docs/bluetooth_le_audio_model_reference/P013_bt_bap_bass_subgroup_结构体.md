---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-13
title: bt_bap_bass_subgroup_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__bass__subgroup.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_bt\_bap\_bass\_subgroup\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__bass__subgroup.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

保存接收状态中子组专用信息（Subgroup Specific Information）的结构体。

```c
#include <zephyr/bluetooth/audio/bap.h>
```

<a id="details"></a>

保存接收状态中子组专用信息（Subgroup Specific Information）的结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 13.1\_数据成员（Data Fields）

<a id="r_ac8061995eb73ba30e335e37714396ff5"></a>

```c
uint32_t bis_sync
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[bis_sync](#ac8061995eb73ba30e335e37714396ff5)。

BIS 同步位域（BIS Synced Bitfield）。

<a id="r_ace1c1ff5d2f5cc79838653d468166664"></a>

```c
uint8_t metadata_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[metadata_len](#ace1c1ff5d2f5cc79838653d468166664)。

元数据长度。

<a id="r_a851fda16d0856714ebf4d3970c4d2e4b"></a>

```c
uint8_t metadata [CONFIG_BT_AUDIO_CODEC_CFG_MAX_METADATA_SIZE]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[metadata](#a851fda16d0856714ebf4d3970c4d2e4b)。

元数据（Metadata）。

## 13.2\_详细说明（Detailed Documentation）

<a id="ac8061995eb73ba30e335e37714396ff5"></a>

### `bis_sync`

```c
uint32_t bt_bap_bass_subgroup::bis_sync
```

BIS 同步位域（BIS Synced Bitfield）。

<a id="a851fda16d0856714ebf4d3970c4d2e4b"></a>

### `metadata`

```c
uint8_t bt_bap_bass_subgroup::metadata[CONFIG_BT_AUDIO_CODEC_CFG_MAX_METADATA_SIZE]
```

元数据（Metadata）。

<a id="ace1c1ff5d2f5cc79838653d468166664"></a>

### `metadata_len`

```c
uint8_t bt_bap_bass_subgroup::metadata_len
```

元数据长度。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/bap.h`

## 13.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P012_bt_bap_base_subgroup_bis_结构体.md) · [返回大纲](大纲.md) · [下一章](P014_bt_bap_broadcast_assistant_add_src_param_结构体.md)
