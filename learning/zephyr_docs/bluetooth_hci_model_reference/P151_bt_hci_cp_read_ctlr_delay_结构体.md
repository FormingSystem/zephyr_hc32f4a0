---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-151
title: bt_hci_cp_read_ctlr_delay_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__read__ctlr__delay.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第151章\_bt\_hci\_cp\_read\_ctlr\_delay\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__read__ctlr__delay.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 151.1\_数据成员（Data Fields）

<a id="r_a2afb9ca8bc2e24cd479b29bc1a53c867"></a>

```c
struct bt_hci_cp_codec_id codec_id
```

相关声明：[bt_hci_cp_codec_id](P011_bt_hci_cp_codec_id_结构体.md)、[codec_id](#a2afb9ca8bc2e24cd479b29bc1a53c867)。

<a id="r_a60a6a5b87896d0c27d734b56ead58a9b"></a>

```c
uint8_t transport
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[transport](#a60a6a5b87896d0c27d734b56ead58a9b)。

<a id="r_a5e9f74d4f82809289038da29af0c663d"></a>

```c
uint8_t direction
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[direction](#a5e9f74d4f82809289038da29af0c663d)。

<a id="r_ac881526b479d5f1717efbe35cdcc7e87"></a>

```c
uint8_t codec_config_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[codec_config_len](#ac881526b479d5f1717efbe35cdcc7e87)。

<a id="r_a6c15d141c40bca8bd095f4a86f5a93bd"></a>

```c
uint8_t codec_config [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[codec_config](#a6c15d141c40bca8bd095f4a86f5a93bd)。

## 151.2\_详细说明（Detailed Documentation）

<a id="a6c15d141c40bca8bd095f4a86f5a93bd"></a>

### `codec_config`

```c
uint8_t bt_hci_cp_read_ctlr_delay::codec_config[0]
```

<a id="ac881526b479d5f1717efbe35cdcc7e87"></a>

### `codec_config_len`

```c
uint8_t bt_hci_cp_read_ctlr_delay::codec_config_len
```

<a id="a2afb9ca8bc2e24cd479b29bc1a53c867"></a>

### `codec_id`

```c
struct bt_hci_cp_codec_id bt_hci_cp_read_ctlr_delay::codec_id
```

<a id="a5e9f74d4f82809289038da29af0c663d"></a>

### `direction`

```c
uint8_t bt_hci_cp_read_ctlr_delay::direction
```

<a id="a60a6a5b87896d0c27d734b56ead58a9b"></a>

### `transport`

```c
uint8_t bt_hci_cp_read_ctlr_delay::transport
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 151.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [bt_hci_cp_codec_id](P011_bt_hci_cp_codec_id_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P150_bt_hci_cp_read_codec_capabilities_结构体.md) · [返回大纲](大纲.md) · [下一章](P152_bt_hci_cp_read_encryption_key_size_结构体.md)
