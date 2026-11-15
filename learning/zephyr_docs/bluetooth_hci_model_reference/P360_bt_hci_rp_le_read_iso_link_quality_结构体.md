---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-360
title: bt_hci_rp_le_read_iso_link_quality_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__iso__link__quality.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第360章\_bt\_hci\_rp\_le\_read\_iso\_link\_quality\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__iso__link__quality.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 360.1\_数据成员（Data Fields）

<a id="r_aef80c600f8916c098e08c43ca718d630"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#aef80c600f8916c098e08c43ca718d630)。

<a id="r_a9f2e8c26081ede43c7712b851d79f2cd"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a9f2e8c26081ede43c7712b851d79f2cd)。

<a id="r_aae42e05dff474062726b92c6d45eae4f"></a>

```c
uint32_t tx_unacked_packets
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[tx_unacked_packets](#aae42e05dff474062726b92c6d45eae4f)。

<a id="r_a12c0c3f9fe6c3c94742367f30bdcc630"></a>

```c
uint32_t tx_flushed_packets
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[tx_flushed_packets](#a12c0c3f9fe6c3c94742367f30bdcc630)。

<a id="r_a0d4468f6871716414ef4a601791bac58"></a>

```c
uint32_t tx_last_subevent_packets
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[tx_last_subevent_packets](#a0d4468f6871716414ef4a601791bac58)。

<a id="r_a7be135da9607045f60b616b84a68f5db"></a>

```c
uint32_t retransmitted_packets
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[retransmitted_packets](#a7be135da9607045f60b616b84a68f5db)。

<a id="r_a353070a64655a39f5410fe76e9168e97"></a>

```c
uint32_t crc_error_packets
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[crc_error_packets](#a353070a64655a39f5410fe76e9168e97)。

<a id="r_a6a16d0aa7ed220bac1ade12eb0f7703e"></a>

```c
uint32_t rx_unreceived_packets
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[rx_unreceived_packets](#a6a16d0aa7ed220bac1ade12eb0f7703e)。

<a id="r_a68c23277e65dc5694f5a27ee2cd364ff"></a>

```c
uint32_t duplicate_packets
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[duplicate_packets](#a68c23277e65dc5694f5a27ee2cd364ff)。

## 360.2\_详细说明（Detailed Documentation）

<a id="a353070a64655a39f5410fe76e9168e97"></a>

### `crc_error_packets`

```c
uint32_t bt_hci_rp_le_read_iso_link_quality::crc_error_packets
```

<a id="a68c23277e65dc5694f5a27ee2cd364ff"></a>

### `duplicate_packets`

```c
uint32_t bt_hci_rp_le_read_iso_link_quality::duplicate_packets
```

<a id="a9f2e8c26081ede43c7712b851d79f2cd"></a>

### `handle`

```c
uint16_t bt_hci_rp_le_read_iso_link_quality::handle
```

<a id="a7be135da9607045f60b616b84a68f5db"></a>

### `retransmitted_packets`

```c
uint32_t bt_hci_rp_le_read_iso_link_quality::retransmitted_packets
```

<a id="a6a16d0aa7ed220bac1ade12eb0f7703e"></a>

### `rx_unreceived_packets`

```c
uint32_t bt_hci_rp_le_read_iso_link_quality::rx_unreceived_packets
```

<a id="aef80c600f8916c098e08c43ca718d630"></a>

### `status`

```c
uint8_t bt_hci_rp_le_read_iso_link_quality::status
```

<a id="a12c0c3f9fe6c3c94742367f30bdcc630"></a>

### `tx_flushed_packets`

```c
uint32_t bt_hci_rp_le_read_iso_link_quality::tx_flushed_packets
```

<a id="a0d4468f6871716414ef4a601791bac58"></a>

### `tx_last_subevent_packets`

```c
uint32_t bt_hci_rp_le_read_iso_link_quality::tx_last_subevent_packets
```

<a id="aae42e05dff474062726b92c6d45eae4f"></a>

### `tx_unacked_packets`

```c
uint32_t bt_hci_rp_le_read_iso_link_quality::tx_unacked_packets
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 360.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P359_bt_hci_rp_le_read_fal_size_结构体.md) · [返回大纲](大纲.md) · [下一章](P361_bt_hci_rp_le_read_iso_tx_sync_结构体.md)
