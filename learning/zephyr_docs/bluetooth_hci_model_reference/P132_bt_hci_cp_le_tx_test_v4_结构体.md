---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-132
title: bt_hci_cp_le_tx_test_v4_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__tx__test__v4.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第132章\_bt\_hci\_cp\_le\_tx\_test\_v4\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__tx__test__v4.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 132.1\_数据成员（Data Fields）

<a id="r_a3ccae40f09b2763b2b07dc16982f3973"></a>

```c
uint8_t tx_ch
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_ch](#a3ccae40f09b2763b2b07dc16982f3973)。

<a id="r_a7a8e2610fb8903ccfb6e4b08017f6112"></a>

```c
uint8_t test_data_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[test_data_len](#a7a8e2610fb8903ccfb6e4b08017f6112)。

<a id="r_abdd393eb264f04acf65e2dce4bd65ac0"></a>

```c
uint8_t pkt_payload
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pkt_payload](#abdd393eb264f04acf65e2dce4bd65ac0)。

<a id="r_a5db011159fe75f4522e03ea1efdc57bd"></a>

```c
uint8_t phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phy](#a5db011159fe75f4522e03ea1efdc57bd)。

<a id="r_a8dea923a63e787de3bfe07611eb7a1ed"></a>

```c
uint8_t cte_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cte_len](#a8dea923a63e787de3bfe07611eb7a1ed)。

<a id="r_ae950f71a3fcfca0cf738bc28693256cf"></a>

```c
uint8_t cte_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cte_type](#ae950f71a3fcfca0cf738bc28693256cf)。

<a id="r_a2039a87b5f32c4a45b8f858808df7cdc"></a>

```c
uint8_t switch_pattern_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[switch_pattern_len](#a2039a87b5f32c4a45b8f858808df7cdc)。

<a id="r_a3fe8ab7c0ee389dce8592cb7a38bc42c"></a>

```c
uint8_t ant_ids [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ant_ids](#a3fe8ab7c0ee389dce8592cb7a38bc42c)。

## 132.2\_详细说明（Detailed Documentation）

<a id="a3fe8ab7c0ee389dce8592cb7a38bc42c"></a>

### `ant_ids`

```c
uint8_t bt_hci_cp_le_tx_test_v4::ant_ids[0]
```

<a id="a8dea923a63e787de3bfe07611eb7a1ed"></a>

### `cte_len`

```c
uint8_t bt_hci_cp_le_tx_test_v4::cte_len
```

<a id="ae950f71a3fcfca0cf738bc28693256cf"></a>

### `cte_type`

```c
uint8_t bt_hci_cp_le_tx_test_v4::cte_type
```

<a id="a5db011159fe75f4522e03ea1efdc57bd"></a>

### `phy`

```c
uint8_t bt_hci_cp_le_tx_test_v4::phy
```

<a id="abdd393eb264f04acf65e2dce4bd65ac0"></a>

### `pkt_payload`

```c
uint8_t bt_hci_cp_le_tx_test_v4::pkt_payload
```

<a id="a2039a87b5f32c4a45b8f858808df7cdc"></a>

### `switch_pattern_len`

```c
uint8_t bt_hci_cp_le_tx_test_v4::switch_pattern_len
```

<a id="a7a8e2610fb8903ccfb6e4b08017f6112"></a>

### `test_data_len`

```c
uint8_t bt_hci_cp_le_tx_test_v4::test_data_len
```

<a id="a3ccae40f09b2763b2b07dc16982f3973"></a>

### `tx_ch`

```c
uint8_t bt_hci_cp_le_tx_test_v4::tx_ch
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 132.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P131_bt_hci_cp_le_tx_test_v3_结构体.md) · [返回大纲](大纲.md) · [下一章](P133_bt_hci_cp_le_tx_test_v4_tx_power_结构体.md)
