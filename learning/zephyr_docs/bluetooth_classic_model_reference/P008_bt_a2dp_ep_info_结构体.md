---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-8
title: bt_a2dp_ep_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__a2dp__ep__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_bt\_a2dp\_ep\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__a2dp__ep__info.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 8.1\_数据成员（Data Fields）

<a id="r_aca4f893b087a8429dd104b67114e36d7"></a>

```c
uint8_t codec_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[codec_type](#aca4f893b087a8429dd104b67114e36d7)。

编解码器类型（Codec Type），类型为 `bt_a2dp_codec_type`。

<a id="r_a4da1ac388f49a05cbb0134223132593d"></a>

```c
bool delay_report
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[delay_report](#a4da1ac388f49a05cbb0134223132593d)。

端点是否具有延迟报告服务（Delay Reporting Service）。

<a id="r_a7647012b4ea73a0124e2a3239a3bad7b"></a>

```c
struct bt_a2dp_codec_ie codec_cap
```

相关声明：[bt_a2dp_codec_ie](P004_bt_a2dp_codec_ie_结构体.md)、[codec_cap](#a7647012b4ea73a0124e2a3239a3bad7b)。

编解码器能力；如果使用 SBC，则通过 `a2dp_codec_sbc.h` 中的函数解析。

<a id="r_a675fc76ec6d27cf53f4c8e6e926e50b5"></a>

```c
struct bt_avdtp_sep_info * sep_info
```

相关声明：[bt_avdtp_sep_info](P014_bt_avdtp_sep_info_结构体.md)、[sep_info](#a675fc76ec6d27cf53f4c8e6e926e50b5)。

流端点信息（Stream End Point Information）。

## 8.2\_详细说明（Detailed Documentation）

<a id="a7647012b4ea73a0124e2a3239a3bad7b"></a>

### `codec_cap`

```c
struct bt_a2dp_codec_ie bt_a2dp_ep_info::codec_cap
```

编解码器能力；如果使用 SBC，则通过 `a2dp_codec_sbc.h` 中的函数解析。

<a id="aca4f893b087a8429dd104b67114e36d7"></a>

### `codec_type`

```c
uint8_t bt_a2dp_ep_info::codec_type
```

编解码器类型（Codec Type），类型为 `bt_a2dp_codec_type`。

<a id="a4da1ac388f49a05cbb0134223132593d"></a>

### `delay_report`

```c
bool bt_a2dp_ep_info::delay_report
```

端点是否具有延迟报告服务（Delay Reporting Service）。

<a id="a675fc76ec6d27cf53f4c8e6e926e50b5"></a>

### `sep_info`

```c
struct bt_avdtp_sep_info* bt_a2dp_ep_info::sep_info
```

流端点信息（Stream End Point Information）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/a2dp.h`

## 8.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/a2dp.h](https://docs.zephyrproject.org/latest/doxygen/html/a2dp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_a2dp_codec_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gafdb0a28b03d1e11f0595dd3f0b3cb4d6)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_a2dp_codec_ie](P004_bt_a2dp_codec_ie_结构体.md)
- [a2dp_codec_sbc.h](https://docs.zephyrproject.org/latest/doxygen/html/a2dp__codec__sbc_8h.html)
- [bt_avdtp_sep_info](P014_bt_avdtp_sep_info_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P007_bt_a2dp_ep_结构体.md) · [返回大纲](大纲.md) · [下一章](P009_bt_a2dp_stream_结构体.md)
