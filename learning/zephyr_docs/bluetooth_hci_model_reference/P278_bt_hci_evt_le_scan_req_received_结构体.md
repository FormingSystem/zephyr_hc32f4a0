---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-278
title: bt_hci_evt_le_scan_req_received_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__scan__req__received.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第278章\_bt\_hci\_evt\_le\_scan\_req\_received\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__scan__req__received.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 278.1\_数据成员（Data Fields）

<a id="r_a62c6d5e5b7079665c0aea8eb676a0433"></a>

```c
uint8_t handle
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[handle](#a62c6d5e5b7079665c0aea8eb676a0433)。

<a id="r_a7dca5ad876dc97859a139d8bd4b207af"></a>

```c
bt_addr_le_t addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[addr](#a7dca5ad876dc97859a139d8bd4b207af)。

## 278.2\_详细说明（Detailed Documentation）

<a id="a7dca5ad876dc97859a139d8bd4b207af"></a>

### `addr`

```c
bt_addr_le_t bt_hci_evt_le_scan_req_received::addr
```

<a id="a62c6d5e5b7079665c0aea8eb676a0433"></a>

### `handle`

```c
uint8_t bt_hci_evt_le_scan_req_received::handle
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 278.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P277_bt_hci_evt_le_req_peer_sca_complete_结构体.md) · [返回大纲](大纲.md) · [下一章](P279_bt_hci_evt_le_subrate_change_结构体.md)
