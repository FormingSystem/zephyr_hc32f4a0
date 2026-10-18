---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-11
title: bt_bap_base_codec_id_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__base__codec__id.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_bt\_bap\_base\_codec\_id\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__base__codec__id.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

广播音频源端点（Broadcast Audio Source Endpoint，BASE）的编解码器 ID 结构体。

```c
#include <zephyr/bluetooth/audio/bap.h>
```

<a id="details"></a>

广播音频源端点（Broadcast Audio Source Endpoint，BASE）的编解码器 ID 结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 11.1\_数据成员（Data Fields）

<a id="r_a9031aaf6a3f6e0acf68f1bfaed39b819"></a>

```c
uint8_t id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[id](#a9031aaf6a3f6e0acf68f1bfaed39b819)。

编解码器 ID（Codec ID）。

<a id="r_a0aadd7e53f72efd8c0e33dd9a8eca177"></a>

```c
uint16_t cid
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[cid](#a0aadd7e53f72efd8c0e33dd9a8eca177)。

编解码器公司 ID（Codec Company ID）。

<a id="r_a49802819cc3129a993320b95472f2262"></a>

```c
uint16_t vid
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[vid](#a49802819cc3129a993320b95472f2262)。

编解码器公司厂商 ID（Codec Company Vendor ID）。

## 11.2\_详细说明（Detailed Documentation）

<a id="a0aadd7e53f72efd8c0e33dd9a8eca177"></a>

### `cid`

```c
uint16_t bt_bap_base_codec_id::cid
```

编解码器公司 ID（Codec Company ID）。

<a id="a9031aaf6a3f6e0acf68f1bfaed39b819"></a>

### `id`

```c
uint8_t bt_bap_base_codec_id::id
```

编解码器 ID（Codec ID）。

<a id="a49802819cc3129a993320b95472f2262"></a>

### `vid`

```c
uint16_t bt_bap_base_codec_id::vid
```

编解码器公司厂商 ID（Codec Company Vendor ID）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/bap.h`

## 11.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P010_bt_bap_ascs_rsp_结构体.md) · [返回大纲](大纲.md) · [下一章](P012_bt_bap_base_subgroup_bis_结构体.md)
