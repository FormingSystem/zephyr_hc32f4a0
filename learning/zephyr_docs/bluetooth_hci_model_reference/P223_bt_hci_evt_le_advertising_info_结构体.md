---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-223
title: bt_hci_evt_le_advertising_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__advertising__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第223章\_bt\_hci\_evt\_le\_advertising\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__advertising__info.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 223.1\_数据成员（Data Fields）

<a id="r_a5943685ccd3491a883ba9450f700bb86"></a>

```c
uint8_t evt_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[evt_type](#a5943685ccd3491a883ba9450f700bb86)。

<a id="r_a1d6863f1a601a2df9d772e3cc1fec118"></a>

```c
bt_addr_le_t addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[addr](#a1d6863f1a601a2df9d772e3cc1fec118)。

<a id="r_a11c223103bf89300bd90cb8725746121"></a>

```c
uint8_t length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[length](#a11c223103bf89300bd90cb8725746121)。

<a id="r_af7d9d720ca67714f2a809e2530a1ff98"></a>

```c
uint8_t data [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#af7d9d720ca67714f2a809e2530a1ff98)。

## 223.2\_详细说明（Detailed Documentation）

<a id="a1d6863f1a601a2df9d772e3cc1fec118"></a>

### `addr`

```c
bt_addr_le_t bt_hci_evt_le_advertising_info::addr
```

<a id="af7d9d720ca67714f2a809e2530a1ff98"></a>

### `data`

```c
uint8_t bt_hci_evt_le_advertising_info::data[0]
```

<a id="a5943685ccd3491a883ba9450f700bb86"></a>

### `evt_type`

```c
uint8_t bt_hci_evt_le_advertising_info::evt_type
```

<a id="a11c223103bf89300bd90cb8725746121"></a>

### `length`

```c
uint8_t bt_hci_evt_le_advertising_info::length
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 223.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P222_bt_hci_evt_le_adv_set_terminated_结构体.md) · [返回大纲](大纲.md) · [下一章](P224_bt_hci_evt_le_advertising_report_结构体.md)
