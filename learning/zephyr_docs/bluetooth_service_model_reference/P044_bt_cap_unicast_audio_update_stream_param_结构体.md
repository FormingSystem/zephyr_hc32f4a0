---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-44
title: bt_cap_unicast_audio_update_stream_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__unicast__audio__update__stream__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第44章\_bt\_cap\_unicast\_audio\_update\_stream\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__unicast__audio__update__stream__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

`bt_cap_initiator_unicast_audio_update()` 函数的流专用参数（Stream Specific Parameters）。

```c
#include <zephyr/bluetooth/audio/cap.h>
```

<a id="details"></a>

`bt_cap_initiator_unicast_audio_update()` 函数的流专用参数（Stream Specific Parameters）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 44.1\_数据成员（Data Fields）

<a id="r_a7a2042834b79ca37e3b3df9fc2f8a7a1"></a>

```c
struct bt_cap_stream * stream
```

相关声明：[bt_cap_stream](P039_bt_cap_stream_结构体.md)、[stream](#a7a2042834b79ca37e3b3df9fc2f8a7a1)。

要更新的流（Stream）。

<a id="r_a07c1ab3158377ce51d94084ad7dc3e9c"></a>

```c
size_t meta_len
```

相关声明：[meta_len](#a07c1ab3158377ce51d94084ad7dc3e9c)。

`meta` 的长度（Length）。

<a id="r_a87833f9e91b47513a27db0aa7692d8c0"></a>

```c
uint8_t * meta
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[meta](#a87833f9e91b47513a27db0aa7692d8c0)。

新的元数据（Metadata）。

## 44.2\_详细说明（Detailed Documentation）

<a id="a87833f9e91b47513a27db0aa7692d8c0"></a>

### `meta`

```c
uint8_t* bt_cap_unicast_audio_update_stream_param::meta
```

新的元数据（Metadata）。

元数据（Metadata）必须包含内容控制标识符列表（CCIDs）以及非零的上下文位域（Context bitfield）。

<a id="a07c1ab3158377ce51d94084ad7dc3e9c"></a>

### `meta_len`

```c
size_t bt_cap_unicast_audio_update_stream_param::meta_len
```

`meta` 的长度（Length）。

<a id="a7a2042834b79ca37e3b3df9fc2f8a7a1"></a>

### `stream`

```c
struct bt_cap_stream* bt_cap_unicast_audio_update_stream_param::stream
```

要更新的流（Stream）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/cap.h`

## 44.3\_原页交叉引用（Cross References）

- [bt_cap_initiator_unicast_audio_update()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga92e4e2c12720ec25c4050cde307cd639)
- [zephyr/bluetooth/audio/cap.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html)
- [bt_cap_stream](P039_bt_cap_stream_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P043_bt_cap_unicast_audio_update_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P045_bt_cap_unicast_group_结构体.md)
