---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-168
title: bt_hci_cp_setup_sync_conn_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__setup__sync__conn.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第168章\_bt\_hci\_cp\_setup\_sync\_conn\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__setup__sync__conn.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 168.1\_数据成员（Data Fields）

<a id="r_ad065185846694fc0070bb366e642f1c7"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#ad065185846694fc0070bb366e642f1c7)。

<a id="r_aa35718e13a7d778c779be535c2b1945e"></a>

```c
uint32_t tx_bandwidth
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[tx_bandwidth](#aa35718e13a7d778c779be535c2b1945e)。

<a id="r_a137601ab44970782e2f3d4fcd2c8fcc2"></a>

```c
uint32_t rx_bandwidth
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[rx_bandwidth](#a137601ab44970782e2f3d4fcd2c8fcc2)。

<a id="r_a5ffb5e552d4913974a10a16083f82864"></a>

```c
uint16_t max_latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_latency](#a5ffb5e552d4913974a10a16083f82864)。

<a id="r_a4d7df5b1aa714bc14d0b6c3cbccc5014"></a>

```c
uint16_t content_format
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[content_format](#a4d7df5b1aa714bc14d0b6c3cbccc5014)。

<a id="r_a61ebbc775d3ca0724ea173d72a96e0c0"></a>

```c
uint8_t retrans_effort
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[retrans_effort](#a61ebbc775d3ca0724ea173d72a96e0c0)。

<a id="r_a6d4c16a4d77d3ee4f8f65ab18a0f192d"></a>

```c
uint16_t pkt_type
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[pkt_type](#a6d4c16a4d77d3ee4f8f65ab18a0f192d)。

## 168.2\_详细说明（Detailed Documentation）

<a id="a4d7df5b1aa714bc14d0b6c3cbccc5014"></a>

### `content_format`

```c
uint16_t bt_hci_cp_setup_sync_conn::content_format
```

<a id="ad065185846694fc0070bb366e642f1c7"></a>

### `handle`

```c
uint16_t bt_hci_cp_setup_sync_conn::handle
```

<a id="a5ffb5e552d4913974a10a16083f82864"></a>

### `max_latency`

```c
uint16_t bt_hci_cp_setup_sync_conn::max_latency
```

<a id="a6d4c16a4d77d3ee4f8f65ab18a0f192d"></a>

### `pkt_type`

```c
uint16_t bt_hci_cp_setup_sync_conn::pkt_type
```

<a id="a61ebbc775d3ca0724ea173d72a96e0c0"></a>

### `retrans_effort`

```c
uint8_t bt_hci_cp_setup_sync_conn::retrans_effort
```

<a id="a137601ab44970782e2f3d4fcd2c8fcc2"></a>

### `rx_bandwidth`

```c
uint32_t bt_hci_cp_setup_sync_conn::rx_bandwidth
```

<a id="aa35718e13a7d778c779be535c2b1945e"></a>

### `tx_bandwidth`

```c
uint32_t bt_hci_cp_setup_sync_conn::tx_bandwidth
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 168.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P167_bt_hci_cp_set_event_mask_page_2_结构体.md) · [返回大纲](大纲.md) · [下一章](P169_bt_hci_cp_sniff_mode_结构体.md)
