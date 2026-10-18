---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-150
title: bt_hci_cp_read_codec_capabilities_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__read__codec__capabilities.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第150章\_bt\_hci\_cp\_read\_codec\_capabilities\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__read__codec__capabilities.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 150.1\_数据成员（Data Fields）

<a id="r_ad48b7f228742d86a71dffa314331bbe1"></a>

```c
struct bt_hci_cp_codec_id codec_id
```

相关声明：[bt_hci_cp_codec_id](P011_bt_hci_cp_codec_id_结构体.md)、[codec_id](#ad48b7f228742d86a71dffa314331bbe1)。

<a id="r_a6479561573172356d7515ef92f75b8d4"></a>

```c
uint8_t transport
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[transport](#a6479561573172356d7515ef92f75b8d4)。

<a id="r_a237695f4d0a1359d5ce71d831708a69c"></a>

```c
uint8_t direction
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[direction](#a237695f4d0a1359d5ce71d831708a69c)。

## 150.2\_详细说明（Detailed Documentation）

<a id="ad48b7f228742d86a71dffa314331bbe1"></a>

### `codec_id`

```c
struct bt_hci_cp_codec_id bt_hci_cp_read_codec_capabilities::codec_id
```

<a id="a237695f4d0a1359d5ce71d831708a69c"></a>

### `direction`

```c
uint8_t bt_hci_cp_read_codec_capabilities::direction
```

<a id="a6479561573172356d7515ef92f75b8d4"></a>

### `transport`

```c
uint8_t bt_hci_cp_read_codec_capabilities::transport
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 150.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [bt_hci_cp_codec_id](P011_bt_hci_cp_codec_id_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P149_bt_hci_cp_read_auth_payload_timeout_结构体.md) · [返回大纲](大纲.md) · [下一章](P151_bt_hci_cp_read_ctlr_delay_结构体.md)
