---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-12
title: bt_bap_base_subgroup_bis_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__base__subgroup__bis.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_bt\_bap\_base\_subgroup\_bis\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__base__subgroup__bis.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

广播音频源端点（BASE）子组中每个广播等时流（Broadcast Isochronous Stream，BIS）的结构体。

```c
#include <zephyr/bluetooth/audio/bap.h>
```

<a id="details"></a>

广播音频源端点（BASE）子组中每个广播等时流（Broadcast Isochronous Stream，BIS）的结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 12.1\_数据成员（Data Fields）

<a id="r_ad0f5dff3150c36b1625f1f6f206d41d2"></a>

```c
uint8_t index
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[index](#ad0f5dff3150c36b1625f1f6f206d41d2)。

BIS 的唯一索引。

<a id="r_ac4132c798c04c0f93c944dc91891221e"></a>

```c
uint8_t data_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data_len](#ac4132c798c04c0f93c944dc91891221e)。

编解码器专用数据（Codec Specific Data）长度。

<a id="r_aa53f22b29e447822e8bb36d9245bfc77"></a>

```c
uint8_t * data
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#aa53f22b29e447822e8bb36d9245bfc77)。

编解码器专用数据。

## 12.2\_详细说明（Detailed Documentation）

<a id="aa53f22b29e447822e8bb36d9245bfc77"></a>

### `data`

```c
uint8_t* bt_bap_base_subgroup_bis::data
```

编解码器专用数据。

<a id="ac4132c798c04c0f93c944dc91891221e"></a>

### `data_len`

```c
uint8_t bt_bap_base_subgroup_bis::data_len
```

编解码器专用数据（Codec Specific Data）长度。

<a id="ad0f5dff3150c36b1625f1f6f206d41d2"></a>

### `index`

```c
uint8_t bt_bap_base_subgroup_bis::index
```

BIS 的唯一索引。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/bap.h`

## 12.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P011_bt_bap_base_codec_id_结构体.md) · [返回大纲](大纲.md) · [下一章](P013_bt_bap_bass_subgroup_结构体.md)
