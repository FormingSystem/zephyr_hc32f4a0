---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-281
title: bt_hci_evt_link_key_notify_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__link__key__notify.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第281章\_bt\_hci\_evt\_link\_key\_notify\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__link__key__notify.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 281.1\_数据成员（Data Fields）

<a id="r_a02647d66142c037b8bca2e748bc15319"></a>

```c
bt_addr_t bdaddr
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bdaddr](#a02647d66142c037b8bca2e748bc15319)。

<a id="r_a4a1b50d8874d01a6a5dc5c52524c9bed"></a>

```c
uint8_t link_key [16]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[link_key](#a4a1b50d8874d01a6a5dc5c52524c9bed)。

<a id="r_a664580660a690af0d9ae3a62d79ad94b"></a>

```c
uint8_t key_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[key_type](#a664580660a690af0d9ae3a62d79ad94b)。

## 281.2\_详细说明（Detailed Documentation）

<a id="a02647d66142c037b8bca2e748bc15319"></a>

### `bdaddr`

```c
bt_addr_t bt_hci_evt_link_key_notify::bdaddr
```

<a id="a664580660a690af0d9ae3a62d79ad94b"></a>

### `key_type`

```c
uint8_t bt_hci_evt_link_key_notify::key_type
```

<a id="a4a1b50d8874d01a6a5dc5c52524c9bed"></a>

### `link_key`

```c
uint8_t bt_hci_evt_link_key_notify::link_key[16]
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 281.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P280_bt_hci_evt_le_transmit_power_report_结构体.md) · [返回大纲](大纲.md) · [下一章](P282_bt_hci_evt_link_key_req_结构体.md)
