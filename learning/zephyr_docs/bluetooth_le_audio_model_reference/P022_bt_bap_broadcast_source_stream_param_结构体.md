---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-22
title: bt_bap_broadcast_source_stream_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__broadcast__source__stream__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_bt\_bap\_broadcast\_source\_stream\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__broadcast__source__stream__param.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

广播音频源的流参数。

```c
#include <zephyr/bluetooth/audio/bap.h>
```

<a id="details"></a>

广播音频源的流参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 22.1\_数据成员（Data Fields）

<a id="r_a9c92fb50b62d963e01b1506b790fb5e1"></a>

```c
struct bt_bap_stream * stream
```

相关声明：[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[stream](#a9c92fb50b62d963e01b1506b790fb5e1)。

音频流（Audio Stream）。

<a id="r_ac79a76ad748673ca4bd52c597cd073df"></a>

```c
size_t data_len
```

相关声明：[data_len](#ac79a76ad748673ca4bd52c597cd073df)。

`data` 数组中的元素数量。

<a id="r_aa1925bb8a770c05b34928d7220177ffa"></a>

```c
const uint8_t * data
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#aa1925bb8a770c05b34928d7220177ffa)。

BIS 编解码器专用配置（Codec Specific Configuration）。

## 22.2\_详细说明（Detailed Documentation）

<a id="aa1925bb8a770c05b34928d7220177ffa"></a>

### `data`

```c
const uint8_t* bt_bap_broadcast_source_stream_param::data
```

BIS 编解码器专用配置（Codec Specific Configuration）。

<a id="ac79a76ad748673ca4bd52c597cd073df"></a>

### `data_len`

```c
size_t bt_bap_broadcast_source_stream_param::data_len
```

`data` 数组中的元素数量。

可省略 BIS 专用数据，并将此值设为 0。

<a id="a9c92fb50b62d963e01b1506b790fb5e1"></a>

### `stream`

```c
struct bt_bap_stream* bt_bap_broadcast_source_stream_param::stream
```

音频流（Audio Stream）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/bap.h`

## 22.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h_source.html)
- [bt_bap_stream](P033_bt_bap_stream_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P021_bt_bap_broadcast_source_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P023_bt_bap_broadcast_source_subgroup_param_结构体.md)
