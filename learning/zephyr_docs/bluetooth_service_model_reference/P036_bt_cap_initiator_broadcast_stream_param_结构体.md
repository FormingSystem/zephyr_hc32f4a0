---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-36
title: bt_cap_initiator_broadcast_stream_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__initiator__broadcast__stream__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第36章\_bt\_cap\_initiator\_broadcast\_stream\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__initiator__broadcast__stream__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

`bt_cap_initiator_broadcast_subgroup_param` 中供 `bt_cap_initiator_broadcast_audio_create()` 使用的参数部分。

```c
#include <zephyr/bluetooth/audio/cap.h>
```

<a id="details"></a>

`bt_cap_initiator_broadcast_subgroup_param` 中供 `bt_cap_initiator_broadcast_audio_create()` 使用的参数部分。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 36.1\_数据成员（Data Fields）

<a id="r_a7e5ddb85024b58d6ecbb6d7f70ef5c6a"></a>

```c
struct bt_cap_stream * stream
```

相关声明：[bt_cap_stream](P039_bt_cap_stream_结构体.md)、[stream](#a7e5ddb85024b58d6ecbb6d7f70ef5c6a)。

音频流（Audio Stream）。

<a id="r_aa4677e278d6d4823551ccfd9c27c68a4"></a>

```c
size_t data_len
```

相关声明：[data_len](#aa4677e278d6d4823551ccfd9c27c68a4)。

`p` 数据数组的长度（Data array length）。

<a id="r_a72720e8423dbeb0341041cc24a9e0869"></a>

```c
uint8_t * data
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#a72720e8423dbeb0341041cc24a9e0869)。

BIS 编解码器专用配置（Codec Specific Configuration）。

## 36.2\_详细说明（Detailed Documentation）

<a id="a72720e8423dbeb0341041cc24a9e0869"></a>

### `data`

```c
uint8_t* bt_cap_initiator_broadcast_stream_param::data
```

BIS 编解码器专用配置（Codec Specific Configuration）。

<a id="aa4677e278d6d4823551ccfd9c27c68a4"></a>

### `data_len`

```c
size_t bt_cap_initiator_broadcast_stream_param::data_len
```

`p` 数据数组的长度（Data array length）。

可省略 BIS 专用数据，并将此值设为 0。

<a id="a7e5ddb85024b58d6ecbb6d7f70ef5c6a"></a>

### `stream`

```c
struct bt_cap_stream* bt_cap_initiator_broadcast_stream_param::stream
```

音频流（Audio Stream）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/cap.h`

## 36.3\_原页交叉引用（Cross References）

- [bt_cap_initiator_broadcast_subgroup_param](P037_bt_cap_initiator_broadcast_subgroup_param_结构体.md)
- [bt_cap_initiator_broadcast_audio_create()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga78697225c6b1291dfc016e20fd605fc4)
- [zephyr/bluetooth/audio/cap.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html)
- [bt_cap_stream](P039_bt_cap_stream_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P035_bt_cap_initiator_broadcast_create_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P037_bt_cap_initiator_broadcast_subgroup_param_结构体.md)
