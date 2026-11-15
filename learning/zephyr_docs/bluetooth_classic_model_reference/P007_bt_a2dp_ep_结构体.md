---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-7
title: bt_a2dp_ep_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__a2dp__ep.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_bt\_a2dp\_ep\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__a2dp__ep.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

流端点（Stream End Point）。

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

<a id="details"></a>

流端点（Stream End Point）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 7.1\_数据成员（Data Fields）

<a id="r_a912cf7cd18a58a1cc1a5e326e8bebb73"></a>

```c
uint8_t codec_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[codec_type](#a912cf7cd18a58a1cc1a5e326e8bebb73)。

编解码器类型（Codec Type），类型为 `bt_a2dp_codec_type`。

<a id="r_a990cba976814d4b18732ae68ce70421c"></a>

```c
bool delay_report
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[delay_report](#a990cba976814d4b18732ae68ce70421c)。

端点是否具有延迟报告服务（Delay Reporting Service）。

<a id="r_ae4dcc7f4bca5cc34cf05c2277379a1b3"></a>

```c
struct bt_a2dp_codec_ie * codec_cap
```

相关声明：[bt_a2dp_codec_ie](P004_bt_a2dp_codec_ie_结构体.md)、[codec_cap](#ae4dcc7f4bca5cc34cf05c2277379a1b3)。

能力（Capabilities）。

<a id="r_a2565b03e09e5abcf239c4c671b348c50"></a>

```c
struct bt_avdtp_sep sep
```

相关声明：[bt_avdtp_sep](P013_bt_avdtp_sep_结构体.md)、[sep](#a2565b03e09e5abcf239c4c671b348c50)。

AVDTP 流端点标识符（Stream End Point Identifier）。

<a id="r_a4902b9fde9be1aa9b7a35c22a21cd4a6"></a>

```c
struct bt_a2dp_stream * stream
```

相关声明：[bt_a2dp_stream](P009_bt_a2dp_stream_结构体.md)、[stream](#a4902b9fde9be1aa9b7a35c22a21cd4a6)。

## 7.2\_详细说明（Detailed Documentation）

<a id="ae4dcc7f4bca5cc34cf05c2277379a1b3"></a>

### `codec_cap`

```c
struct bt_a2dp_codec_ie* bt_a2dp_ep::codec_cap
```

能力（Capabilities）。

<a id="a912cf7cd18a58a1cc1a5e326e8bebb73"></a>

### `codec_type`

```c
uint8_t bt_a2dp_ep::codec_type
```

编解码器类型（Codec Type），类型为 `bt_a2dp_codec_type`。

<a id="a990cba976814d4b18732ae68ce70421c"></a>

### `delay_report`

```c
bool bt_a2dp_ep::delay_report
```

端点是否具有延迟报告服务（Delay Reporting Service）。

<a id="a2565b03e09e5abcf239c4c671b348c50"></a>

### `sep`

```c
struct bt_avdtp_sep bt_a2dp_ep::sep
```

AVDTP 流端点标识符（Stream End Point Identifier）。

<a id="a4902b9fde9be1aa9b7a35c22a21cd4a6"></a>

### `stream`

```c
struct bt_a2dp_stream* bt_a2dp_ep::stream
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/a2dp.h`

## 7.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/a2dp.h](https://docs.zephyrproject.org/latest/doxygen/html/a2dp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_a2dp_codec_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gafdb0a28b03d1e11f0595dd3f0b3cb4d6)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_a2dp_codec_ie](P004_bt_a2dp_codec_ie_结构体.md)
- [bt_avdtp_sep](P013_bt_avdtp_sep_结构体.md)
- [bt_a2dp_stream](P009_bt_a2dp_stream_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P006_bt_a2dp_discover_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P008_bt_a2dp_ep_info_结构体.md)
