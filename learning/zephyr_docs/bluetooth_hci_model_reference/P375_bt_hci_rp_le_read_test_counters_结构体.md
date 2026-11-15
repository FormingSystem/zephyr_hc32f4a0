---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-375
title: bt_hci_rp_le_read_test_counters_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__test__counters.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第375章\_bt\_hci\_rp\_le\_read\_test\_counters\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__test__counters.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 375.1\_数据成员（Data Fields）

<a id="r_ae1e78d68e9f55b31092a07575a66c1c0"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#ae1e78d68e9f55b31092a07575a66c1c0)。

<a id="r_a8121f879a3fb5550cc1aa468aacb81b7"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a8121f879a3fb5550cc1aa468aacb81b7)。

<a id="r_a8c4b2674fb129ca0de0bc45c608e13c7"></a>

```c
uint32_t received_cnt
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[received_cnt](#a8c4b2674fb129ca0de0bc45c608e13c7)。

<a id="r_ae96d05ffb2fbc681c804b04c8791aeab"></a>

```c
uint32_t missed_cnt
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[missed_cnt](#ae96d05ffb2fbc681c804b04c8791aeab)。

<a id="r_af6261d3547cd9b377fedc7a36891c2f7"></a>

```c
uint32_t failed_cnt
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[failed_cnt](#af6261d3547cd9b377fedc7a36891c2f7)。

## 375.2\_详细说明（Detailed Documentation）

<a id="af6261d3547cd9b377fedc7a36891c2f7"></a>

### `failed_cnt`

```c
uint32_t bt_hci_rp_le_read_test_counters::failed_cnt
```

<a id="a8121f879a3fb5550cc1aa468aacb81b7"></a>

### `handle`

```c
uint16_t bt_hci_rp_le_read_test_counters::handle
```

<a id="ae96d05ffb2fbc681c804b04c8791aeab"></a>

### `missed_cnt`

```c
uint32_t bt_hci_rp_le_read_test_counters::missed_cnt
```

<a id="a8c4b2674fb129ca0de0bc45c608e13c7"></a>

### `received_cnt`

```c
uint32_t bt_hci_rp_le_read_test_counters::received_cnt
```

<a id="ae1e78d68e9f55b31092a07575a66c1c0"></a>

### `status`

```c
uint8_t bt_hci_rp_le_read_test_counters::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 375.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P374_bt_hci_rp_le_read_supp_states_结构体.md) · [返回大纲](大纲.md) · [下一章](P376_bt_hci_rp_le_read_tx_power_结构体.md)
