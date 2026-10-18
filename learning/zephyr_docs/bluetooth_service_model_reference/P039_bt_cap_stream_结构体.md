---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-39
title: bt_cap_stream_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__stream.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_bt\_cap\_stream\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__stream.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通用音频配置文件（Common Audio Profile，CAP）流结构体。

```c
#include <zephyr/bluetooth/audio/cap.h>
```

<a id="details"></a>

通用音频规范流结构（Common Audio Profile stream structure）。流表示一个基本音频规范（Basic Audio Profile，BAP）流及其操作回调。更多信息参见 `bt_bap_stream`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 39.1\_数据成员（Data Fields）

<a id="r_ad9d974d18ec42079b81107485b43bc18"></a>

```c
struct bt_bap_stream bap_stream
```

相关声明：[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)、[bap_stream](#ad9d974d18ec42079b81107485b43bc18)。

底层基本音频规范音频流（BAP audio stream）。

<a id="r_aa58c47ace3f844533ab545906ede52ba"></a>

```c
struct bt_bap_stream_ops * ops
```

相关声明：[bt_bap_stream_ops](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md)、[ops](#aa58c47ace3f844533ab545906ede52ba)。

音频流操作（Audio Stream Operations）。

## 39.2\_详细说明（Detailed Documentation）

<a id="ad9d974d18ec42079b81107485b43bc18"></a>

### `bap_stream`

```c
struct bt_bap_stream bt_cap_stream::bap_stream
```

底层基本音频规范音频流（BAP audio stream）。

<a id="aa58c47ace3f844533ab545906ede52ba"></a>

### `ops`

```c
struct bt_bap_stream_ops* bt_cap_stream::ops
```

音频流操作（Audio Stream Operations）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/cap.h`

## 39.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/cap.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html)
- [bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)
- [bt_bap_stream_ops](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P038_bt_cap_initiator_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P040_bt_cap_unicast_audio_start_param_结构体.md)
