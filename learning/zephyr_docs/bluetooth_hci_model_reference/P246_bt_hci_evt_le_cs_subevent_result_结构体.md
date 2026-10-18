---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-246
title: bt_hci_evt_le_cs_subevent_result_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__cs__subevent__result.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第246章\_bt\_hci\_evt\_le\_cs\_subevent\_result\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__cs__subevent__result.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 246.1\_数据成员（Data Fields）

<a id="r_a3b9c8392fa3aadc2e0673923e0346278"></a>

```c
uint16_t conn_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_handle](#a3b9c8392fa3aadc2e0673923e0346278)。

<a id="r_a2e8bdef7f85a4cefeaf625d0c3a4db03"></a>

```c
uint8_t config_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[config_id](#a2e8bdef7f85a4cefeaf625d0c3a4db03)。

<a id="r_a0d6b2ca9f148173abb6207cf7c473c7f"></a>

```c
uint16_t start_acl_conn_event_counter
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[start_acl_conn_event_counter](#a0d6b2ca9f148173abb6207cf7c473c7f)。

<a id="r_ad08558fd68eb6c43d95a3f0f62bafff0"></a>

```c
uint16_t procedure_counter
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[procedure_counter](#ad08558fd68eb6c43d95a3f0f62bafff0)。

<a id="r_aba480f7ad78069fd8b83493fac42244e"></a>

```c
uint16_t frequency_compensation
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[frequency_compensation](#aba480f7ad78069fd8b83493fac42244e)。

<a id="r_a9a7260f63122a94cf7eb6ddc3344f742"></a>

```c
uint8_t reference_power_level
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reference_power_level](#a9a7260f63122a94cf7eb6ddc3344f742)。

<a id="r_a27a2848009838977f26df75bfc9bc3c3"></a>

```c
uint8_t procedure_done_status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[procedure_done_status](#a27a2848009838977f26df75bfc9bc3c3)。

<a id="r_aeda28dfb30c51ce2955e1c313069c111"></a>

```c
uint8_t subevent_done_status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subevent_done_status](#aeda28dfb30c51ce2955e1c313069c111)。

<a id="r_acf6f9c4e6fa5897be872d9953993517b"></a>

```c
uint8_t subevent_abort_reason: 4
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subevent_abort_reason](#acf6f9c4e6fa5897be872d9953993517b)。

<a id="r_ab81c9c55697b2f2c92e3ea2073932ad1"></a>

```c
uint8_t procedure_abort_reason: 4
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[procedure_abort_reason](#ab81c9c55697b2f2c92e3ea2073932ad1)。

<a id="r_a9931d5818b801a9c36853f88b259c25e"></a>

```c
uint8_t num_antenna_paths
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_antenna_paths](#a9931d5818b801a9c36853f88b259c25e)。

<a id="r_af8c827d508614f553b9f503d0394411b"></a>

```c
uint8_t num_steps_reported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_steps_reported](#af8c827d508614f553b9f503d0394411b)。

<a id="r_a43b46a37648b9fde72634dd7dd6a68e6"></a>

```c
uint8_t steps []
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[steps](#a43b46a37648b9fde72634dd7dd6a68e6)。

## 246.2\_详细说明（Detailed Documentation）

<a id="a2e8bdef7f85a4cefeaf625d0c3a4db03"></a>

### `config_id`

```c
uint8_t bt_hci_evt_le_cs_subevent_result::config_id
```

<a id="a3b9c8392fa3aadc2e0673923e0346278"></a>

### `conn_handle`

```c
uint16_t bt_hci_evt_le_cs_subevent_result::conn_handle
```

<a id="aba480f7ad78069fd8b83493fac42244e"></a>

### `frequency_compensation`

```c
uint16_t bt_hci_evt_le_cs_subevent_result::frequency_compensation
```

<a id="a9931d5818b801a9c36853f88b259c25e"></a>

### `num_antenna_paths`

```c
uint8_t bt_hci_evt_le_cs_subevent_result::num_antenna_paths
```

<a id="af8c827d508614f553b9f503d0394411b"></a>

### `num_steps_reported`

```c
uint8_t bt_hci_evt_le_cs_subevent_result::num_steps_reported
```

<a id="ab81c9c55697b2f2c92e3ea2073932ad1"></a>

### `procedure_abort_reason`

```c
uint8_t bt_hci_evt_le_cs_subevent_result::procedure_abort_reason
```

<a id="ad08558fd68eb6c43d95a3f0f62bafff0"></a>

### `procedure_counter`

```c
uint16_t bt_hci_evt_le_cs_subevent_result::procedure_counter
```

<a id="a27a2848009838977f26df75bfc9bc3c3"></a>

### `procedure_done_status`

```c
uint8_t bt_hci_evt_le_cs_subevent_result::procedure_done_status
```

<a id="a9a7260f63122a94cf7eb6ddc3344f742"></a>

### `reference_power_level`

```c
uint8_t bt_hci_evt_le_cs_subevent_result::reference_power_level
```

<a id="a0d6b2ca9f148173abb6207cf7c473c7f"></a>

### `start_acl_conn_event_counter`

```c
uint16_t bt_hci_evt_le_cs_subevent_result::start_acl_conn_event_counter
```

<a id="a43b46a37648b9fde72634dd7dd6a68e6"></a>

### `steps`

```c
uint8_t bt_hci_evt_le_cs_subevent_result::steps[]
```

<a id="acf6f9c4e6fa5897be872d9953993517b"></a>

### `subevent_abort_reason`

```c
uint8_t bt_hci_evt_le_cs_subevent_result::subevent_abort_reason
```

<a id="aeda28dfb30c51ce2955e1c313069c111"></a>

### `subevent_done_status`

```c
uint8_t bt_hci_evt_le_cs_subevent_result::subevent_done_status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 246.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P245_bt_hci_evt_le_cs_security_enable_complete_结构体.md) · [返回大纲](大纲.md) · [下一章](P247_bt_hci_evt_le_cs_subevent_result_continue_结构体.md)
