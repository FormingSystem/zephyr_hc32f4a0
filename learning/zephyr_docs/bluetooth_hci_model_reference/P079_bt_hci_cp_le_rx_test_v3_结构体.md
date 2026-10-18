---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-79
title: bt_hci_cp_le_rx_test_v3_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__rx__test__v3.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第79章\_bt\_hci\_cp\_le\_rx\_test\_v3\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__rx__test__v3.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 79.1\_数据成员（Data Fields）

<a id="r_abd33b70c948d4ee42d96d0d2e7f7cb1c"></a>

```c
uint8_t rx_ch
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rx_ch](#abd33b70c948d4ee42d96d0d2e7f7cb1c)。

<a id="r_ad1c211c59cf34d76429d4d4548966630"></a>

```c
uint8_t phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phy](#ad1c211c59cf34d76429d4d4548966630)。

<a id="r_a7ffde9dc565194c0108177cf11b02b5b"></a>

```c
uint8_t mod_index
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mod_index](#a7ffde9dc565194c0108177cf11b02b5b)。

<a id="r_ad1a1082d27b8a10e25eebd347404637c"></a>

```c
uint8_t expected_cte_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[expected_cte_len](#ad1a1082d27b8a10e25eebd347404637c)。

<a id="r_a55b5c4739e456167f17bf3899d096e61"></a>

```c
uint8_t expected_cte_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[expected_cte_type](#a55b5c4739e456167f17bf3899d096e61)。

<a id="r_a5cd5a44b0832b9f6e2198b9ad714b99b"></a>

```c
uint8_t slot_durations
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[slot_durations](#a5cd5a44b0832b9f6e2198b9ad714b99b)。

<a id="r_ab0832e72ef90b1269928378638fcb194"></a>

```c
uint8_t switch_pattern_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[switch_pattern_len](#ab0832e72ef90b1269928378638fcb194)。

<a id="r_aa6cd0835068f378949da182af13e2438"></a>

```c
uint8_t ant_ids [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ant_ids](#aa6cd0835068f378949da182af13e2438)。

## 79.2\_详细说明（Detailed Documentation）

<a id="aa6cd0835068f378949da182af13e2438"></a>

### `ant_ids`

```c
uint8_t bt_hci_cp_le_rx_test_v3::ant_ids[0]
```

<a id="ad1a1082d27b8a10e25eebd347404637c"></a>

### `expected_cte_len`

```c
uint8_t bt_hci_cp_le_rx_test_v3::expected_cte_len
```

<a id="a55b5c4739e456167f17bf3899d096e61"></a>

### `expected_cte_type`

```c
uint8_t bt_hci_cp_le_rx_test_v3::expected_cte_type
```

<a id="a7ffde9dc565194c0108177cf11b02b5b"></a>

### `mod_index`

```c
uint8_t bt_hci_cp_le_rx_test_v3::mod_index
```

<a id="ad1c211c59cf34d76429d4d4548966630"></a>

### `phy`

```c
uint8_t bt_hci_cp_le_rx_test_v3::phy
```

<a id="abd33b70c948d4ee42d96d0d2e7f7cb1c"></a>

### `rx_ch`

```c
uint8_t bt_hci_cp_le_rx_test_v3::rx_ch
```

<a id="a5cd5a44b0832b9f6e2198b9ad714b99b"></a>

### `slot_durations`

```c
uint8_t bt_hci_cp_le_rx_test_v3::slot_durations
```

<a id="ab0832e72ef90b1269928378638fcb194"></a>

### `switch_pattern_len`

```c
uint8_t bt_hci_cp_le_rx_test_v3::switch_pattern_len
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 79.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P078_bt_hci_cp_le_rx_test_结构体.md) · [返回大纲](大纲.md) · [下一章](P080_bt_hci_cp_le_security_enable_结构体.md)
