---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-131
title: bt_hci_cp_le_tx_test_v3_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__tx__test__v3.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第131章\_bt\_hci\_cp\_le\_tx\_test\_v3\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__tx__test__v3.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 131.1\_数据成员（Data Fields）

<a id="r_a6486882bc375f229a88bbfa53be49670"></a>

```c
uint8_t tx_ch
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_ch](#a6486882bc375f229a88bbfa53be49670)。

<a id="r_a1c0828e51bb6c24e9dd1f12b5badcfea"></a>

```c
uint8_t test_data_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[test_data_len](#a1c0828e51bb6c24e9dd1f12b5badcfea)。

<a id="r_ad8f2d2ca3ad3be28c0aec9e8a0e1bc61"></a>

```c
uint8_t pkt_payload
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pkt_payload](#ad8f2d2ca3ad3be28c0aec9e8a0e1bc61)。

<a id="r_a712a30d9d6afc7d302041e1de6721de4"></a>

```c
uint8_t phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phy](#a712a30d9d6afc7d302041e1de6721de4)。

<a id="r_a52d2d6dcc188d5f02904e0e56f461841"></a>

```c
uint8_t cte_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cte_len](#a52d2d6dcc188d5f02904e0e56f461841)。

<a id="r_adf6b1653902fb13cc1ccc32cd91c990f"></a>

```c
uint8_t cte_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cte_type](#adf6b1653902fb13cc1ccc32cd91c990f)。

<a id="r_a459b850f35c61bf7f53d3730245cb4bb"></a>

```c
uint8_t switch_pattern_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[switch_pattern_len](#a459b850f35c61bf7f53d3730245cb4bb)。

<a id="r_afdb6dd44108e9a4a21ac31a74c1e083f"></a>

```c
uint8_t ant_ids [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ant_ids](#afdb6dd44108e9a4a21ac31a74c1e083f)。

## 131.2\_详细说明（Detailed Documentation）

<a id="afdb6dd44108e9a4a21ac31a74c1e083f"></a>

### `ant_ids`

```c
uint8_t bt_hci_cp_le_tx_test_v3::ant_ids[0]
```

<a id="a52d2d6dcc188d5f02904e0e56f461841"></a>

### `cte_len`

```c
uint8_t bt_hci_cp_le_tx_test_v3::cte_len
```

<a id="adf6b1653902fb13cc1ccc32cd91c990f"></a>

### `cte_type`

```c
uint8_t bt_hci_cp_le_tx_test_v3::cte_type
```

<a id="a712a30d9d6afc7d302041e1de6721de4"></a>

### `phy`

```c
uint8_t bt_hci_cp_le_tx_test_v3::phy
```

<a id="ad8f2d2ca3ad3be28c0aec9e8a0e1bc61"></a>

### `pkt_payload`

```c
uint8_t bt_hci_cp_le_tx_test_v3::pkt_payload
```

<a id="a459b850f35c61bf7f53d3730245cb4bb"></a>

### `switch_pattern_len`

```c
uint8_t bt_hci_cp_le_tx_test_v3::switch_pattern_len
```

<a id="a1c0828e51bb6c24e9dd1f12b5badcfea"></a>

### `test_data_len`

```c
uint8_t bt_hci_cp_le_tx_test_v3::test_data_len
```

<a id="a6486882bc375f229a88bbfa53be49670"></a>

### `tx_ch`

```c
uint8_t bt_hci_cp_le_tx_test_v3::tx_ch
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 131.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P130_bt_hci_cp_le_tx_test_结构体.md) · [返回大纲](大纲.md) · [下一章](P132_bt_hci_cp_le_tx_test_v4_结构体.md)
