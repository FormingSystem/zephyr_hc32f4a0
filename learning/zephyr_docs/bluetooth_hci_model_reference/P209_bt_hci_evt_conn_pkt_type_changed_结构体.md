---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-209
title: bt_hci_evt_conn_pkt_type_changed_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__conn__pkt__type__changed.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第209章\_bt\_hci\_evt\_conn\_pkt\_type\_changed\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__conn__pkt__type__changed.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

HCI 连接包类型已变化（Connection Packet Type Changed）事件参数。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="details"></a>

HCI 连接包类型已变化（Connection Packet Type Changed）事件参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 209.1\_数据成员（Data Fields）

<a id="r_aabad2dfce94a19a83a5f52e334da18f8"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#aabad2dfce94a19a83a5f52e334da18f8)。

HCI 状态（Status）。

<a id="r_abde9bbcf2afa3c9a49662aa8192de868"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#abde9bbcf2afa3c9a49662aa8192de868)。

连接句柄（Connection Handle）。

<a id="r_aa78e454d08e7c76b3e22242c4855ee62"></a>

```c
uint16_t packet_type
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[packet_type](#aa78e454d08e7c76b3e22242c4855ee62)。

包类型位掩码（Packet Type Bitmask）。

## 209.2\_详细说明（Detailed Documentation）

<a id="abde9bbcf2afa3c9a49662aa8192de868"></a>

### `handle`

```c
uint16_t bt_hci_evt_conn_pkt_type_changed::handle
```

连接句柄（Connection Handle）。

<a id="aa78e454d08e7c76b3e22242c4855ee62"></a>

### `packet_type`

```c
uint16_t bt_hci_evt_conn_pkt_type_changed::packet_type
```

包类型位掩码（Packet Type Bitmask）。

<a id="aabad2dfce94a19a83a5f52e334da18f8"></a>

### `status`

```c
uint8_t bt_hci_evt_conn_pkt_type_changed::status
```

HCI 状态（Status）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 209.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P208_bt_hci_evt_conn_complete_结构体.md) · [返回大纲](大纲.md) · [下一章](P210_bt_hci_evt_conn_request_结构体.md)
