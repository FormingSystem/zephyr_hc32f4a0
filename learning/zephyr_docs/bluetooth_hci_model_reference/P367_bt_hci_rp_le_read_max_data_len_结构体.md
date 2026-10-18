---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-367
title: bt_hci_rp_le_read_max_data_len_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__max__data__len.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第367章\_bt\_hci\_rp\_le\_read\_max\_data\_len\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__max__data__len.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 367.1\_数据成员（Data Fields）

<a id="r_a654b34b1ee038bf442550a340a26070c"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a654b34b1ee038bf442550a340a26070c)。

<a id="r_a2c0b159c6248cb9df458d587f82a4152"></a>

```c
uint16_t max_tx_octets
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_tx_octets](#a2c0b159c6248cb9df458d587f82a4152)。

<a id="r_a6adc84bf3cc86f234e61982d871899b6"></a>

```c
uint16_t max_tx_time
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_tx_time](#a6adc84bf3cc86f234e61982d871899b6)。

<a id="r_a9273dac6614f1e120f0539b746bfd6cc"></a>

```c
uint16_t max_rx_octets
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_rx_octets](#a9273dac6614f1e120f0539b746bfd6cc)。

<a id="r_a963ef9c097906c8db46c35459eb4ecab"></a>

```c
uint16_t max_rx_time
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_rx_time](#a963ef9c097906c8db46c35459eb4ecab)。

## 367.2\_详细说明（Detailed Documentation）

<a id="a9273dac6614f1e120f0539b746bfd6cc"></a>

### `max_rx_octets`

```c
uint16_t bt_hci_rp_le_read_max_data_len::max_rx_octets
```

<a id="a963ef9c097906c8db46c35459eb4ecab"></a>

### `max_rx_time`

```c
uint16_t bt_hci_rp_le_read_max_data_len::max_rx_time
```

<a id="a2c0b159c6248cb9df458d587f82a4152"></a>

### `max_tx_octets`

```c
uint16_t bt_hci_rp_le_read_max_data_len::max_tx_octets
```

<a id="a6adc84bf3cc86f234e61982d871899b6"></a>

### `max_tx_time`

```c
uint16_t bt_hci_rp_le_read_max_data_len::max_tx_time
```

<a id="a654b34b1ee038bf442550a340a26070c"></a>

### `status`

```c
uint8_t bt_hci_rp_le_read_max_data_len::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 367.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P366_bt_hci_rp_le_read_max_adv_data_len_结构体.md) · [返回大纲](大纲.md) · [下一章](P368_bt_hci_rp_le_read_num_adv_sets_结构体.md)
