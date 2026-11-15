---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-444
title: bt_hci_vs_codec_info_v2_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__vs__codec__info__v2.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第444章\_bt\_hci\_vs\_codec\_info\_v2\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__vs__codec__info__v2.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 444.1\_数据成员（Data Fields）

<a id="r_aa6ce27b4acd3dff516e4d7ed2e6434bc"></a>

```c
uint16_t company_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[company_id](#aa6ce27b4acd3dff516e4d7ed2e6434bc)。

<a id="r_ae7b7d5d65629a1e3039b3c7cf167a9c1"></a>

```c
uint16_t codec_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[codec_id](#ae7b7d5d65629a1e3039b3c7cf167a9c1)。

<a id="r_ac2a91a045e4b53315850b6d4f1d38b2c"></a>

```c
uint8_t transports
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[transports](#ac2a91a045e4b53315850b6d4f1d38b2c)。

## 444.2\_详细说明（Detailed Documentation）

<a id="ae7b7d5d65629a1e3039b3c7cf167a9c1"></a>

### `codec_id`

```c
uint16_t bt_hci_vs_codec_info_v2::codec_id
```

<a id="aa6ce27b4acd3dff516e4d7ed2e6434bc"></a>

### `company_id`

```c
uint16_t bt_hci_vs_codec_info_v2::company_id
```

<a id="ac2a91a045e4b53315850b6d4f1d38b2c"></a>

### `transports`

```c
uint8_t bt_hci_vs_codec_info_v2::transports
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 444.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P443_bt_hci_vs_codec_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P445_bt_hci_vs_codecs_结构体.md)
