---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-358
title: bt_hci_rp_le_read_default_data_len_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__default__data__len.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第358章\_bt\_hci\_rp\_le\_read\_default\_data\_len\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__default__data__len.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 358.1\_数据成员（Data Fields）

<a id="r_a62d735826ad3ca5d4bea7d0fb87dea7e"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a62d735826ad3ca5d4bea7d0fb87dea7e)。

<a id="r_a1ec4ba1c0286132e87fcffeb988a37f9"></a>

```c
uint16_t max_tx_octets
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_tx_octets](#a1ec4ba1c0286132e87fcffeb988a37f9)。

<a id="r_ae193eab40c2afa55b78a1906e6a26f26"></a>

```c
uint16_t max_tx_time
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_tx_time](#ae193eab40c2afa55b78a1906e6a26f26)。

## 358.2\_详细说明（Detailed Documentation）

<a id="a1ec4ba1c0286132e87fcffeb988a37f9"></a>

### `max_tx_octets`

```c
uint16_t bt_hci_rp_le_read_default_data_len::max_tx_octets
```

<a id="ae193eab40c2afa55b78a1906e6a26f26"></a>

### `max_tx_time`

```c
uint16_t bt_hci_rp_le_read_default_data_len::max_tx_time
```

<a id="a62d735826ad3ca5d4bea7d0fb87dea7e"></a>

### `status`

```c
uint8_t bt_hci_rp_le_read_default_data_len::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 358.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P357_bt_hci_rp_le_read_chan_tx_power_结构体.md) · [返回大纲](大纲.md) · [下一章](P359_bt_hci_rp_le_read_fal_size_结构体.md)
