---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-37
title: bt_cap_initiator_broadcast_subgroup_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__initiator__broadcast__subgroup__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_bt\_cap\_initiator\_broadcast\_subgroup\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__initiator__broadcast__subgroup__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

`bt_cap_initiator_broadcast_create_param` 中供 `bt_cap_initiator_broadcast_audio_create()` 使用的参数部分。

```c
#include <zephyr/bluetooth/audio/cap.h>
```

<a id="details"></a>

`bt_cap_initiator_broadcast_create_param` 中供 `bt_cap_initiator_broadcast_audio_create()` 使用的参数部分。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 37.1\_数据成员（Data Fields）

<a id="r_a577a27836a02c7a6219182f1cb0bd769"></a>

```c
size_t stream_count
```

相关声明：[stream_count](#a577a27836a02c7a6219182f1cb0bd769)。

`stream_params` 中的参数数量。

<a id="r_a32e99898ee97a56105497c3ae480692a"></a>

```c
struct bt_cap_initiator_broadcast_stream_param * stream_params
```

相关声明：[bt_cap_initiator_broadcast_stream_param](P036_bt_cap_initiator_broadcast_stream_param_结构体.md)、[stream_params](#a32e99898ee97a56105497c3ae480692a)。

流参数数组（Stream Parameters Array）。

<a id="r_a252140d260f47404302a721a928f4765"></a>

```c
const struct bt_audio_codec_cfg * codec_cfg
```

相关声明：[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[codec_cfg](#a252140d260f47404302a721a928f4765)。

子组编解码器配置（Subgroup Codec Configuration）。

## 37.2\_详细说明（Detailed Documentation）

<a id="a252140d260f47404302a721a928f4765"></a>

### `codec_cfg`

```c
const struct bt_audio_codec_cfg* bt_cap_initiator_broadcast_subgroup_param::codec_cfg
```

子组编解码器配置（Subgroup Codec Configuration）。

<a id="a577a27836a02c7a6219182f1cb0bd769"></a>

### `stream_count`

```c
size_t bt_cap_initiator_broadcast_subgroup_param::stream_count
```

`stream_params` 中的参数数量。

<a id="a32e99898ee97a56105497c3ae480692a"></a>

### `stream_params`

```c
struct bt_cap_initiator_broadcast_stream_param* bt_cap_initiator_broadcast_subgroup_param::stream_params
```

流参数数组（Stream Parameters Array）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/cap.h`

## 37.3\_原页交叉引用（Cross References）

- [bt_cap_initiator_broadcast_create_param](P035_bt_cap_initiator_broadcast_create_param_结构体.md)
- [bt_cap_initiator_broadcast_audio_create()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga78697225c6b1291dfc016e20fd605fc4)
- [zephyr/bluetooth/audio/cap.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html)
- [bt_cap_initiator_broadcast_stream_param](P036_bt_cap_initiator_broadcast_stream_param_结构体.md)
- [bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P036_bt_cap_initiator_broadcast_stream_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P038_bt_cap_initiator_cb_结构体.md)
