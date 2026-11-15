---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-4
title: bt_a2dp_codec_ie_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__a2dp__codec__ie.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_bt\_a2dp\_codec\_ie\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__a2dp__codec__ie.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

端点的编解码器信息元素（Codec Information Elements）。

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

<a id="details"></a>

端点的编解码器信息元素（Codec Information Elements）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 4.1\_数据成员（Data Fields）

<a id="r_a8ba1a0bfcbfd180cb19fb7c4a4ce8225"></a>

```c
uint8_t len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[len](#a8ba1a0bfcbfd180cb19fb7c4a4ce8225)。

`codec_cap` 的长度。

<a id="r_acd0b1b740e2adba463424e5c3fc726e9"></a>

```c
uint8_t codec_ie [CONFIG_BT_A2DP_CODEC_MAX_IE_LEN]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[codec_ie](#acd0b1b740e2adba463424e5c3fc726e9)。

编解码器信息元素（Codec Information Element）。

## 4.2\_详细说明（Detailed Documentation）

<a id="acd0b1b740e2adba463424e5c3fc726e9"></a>

### `codec_ie`

```c
uint8_t bt_a2dp_codec_ie::codec_ie[CONFIG_BT_A2DP_CODEC_MAX_IE_LEN]
```

编解码器信息元素（Codec Information Element）。

<a id="a8ba1a0bfcbfd180cb19fb7c4a4ce8225"></a>

### `len`

```c
uint8_t bt_a2dp_codec_ie::len
```

`codec_cap` 的长度。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/a2dp.h`

## 4.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/a2dp.h](https://docs.zephyrproject.org/latest/doxygen/html/a2dp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P003_bt_a2dp_codec_cfg_结构体.md) · [返回大纲](大纲.md) · [下一章](P005_bt_a2dp_codec_sbc_params_结构体.md)
