---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-91
title: bt_hci_cp_le_set_conn_cte_rx_params_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__conn__cte__rx__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第91章\_bt\_hci\_cp\_le\_set\_conn\_cte\_rx\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__conn__cte__rx__params.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 91.1\_数据成员（Data Fields）

<a id="r_a76968866cf5c6ef4bfb983cb6b68a827"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a76968866cf5c6ef4bfb983cb6b68a827)。

<a id="r_a615cae822878cf1344a990e30fa80044"></a>

```c
uint8_t sampling_enable
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sampling_enable](#a615cae822878cf1344a990e30fa80044)。

<a id="r_a6246d492b94c67af9604b89912dbdb61"></a>

```c
uint8_t slot_durations
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[slot_durations](#a6246d492b94c67af9604b89912dbdb61)。

<a id="r_a89194a5b9e6c7f0c176c915e451911df"></a>

```c
uint8_t switch_pattern_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[switch_pattern_len](#a89194a5b9e6c7f0c176c915e451911df)。

<a id="r_a519c37f5d797d8ddac5ba9be7c14b9f9"></a>

```c
uint8_t ant_ids [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ant_ids](#a519c37f5d797d8ddac5ba9be7c14b9f9)。

## 91.2\_详细说明（Detailed Documentation）

<a id="a519c37f5d797d8ddac5ba9be7c14b9f9"></a>

### `ant_ids`

```c
uint8_t bt_hci_cp_le_set_conn_cte_rx_params::ant_ids[0]
```

<a id="a76968866cf5c6ef4bfb983cb6b68a827"></a>

### `handle`

```c
uint16_t bt_hci_cp_le_set_conn_cte_rx_params::handle
```

<a id="a615cae822878cf1344a990e30fa80044"></a>

### `sampling_enable`

```c
uint8_t bt_hci_cp_le_set_conn_cte_rx_params::sampling_enable
```

<a id="a6246d492b94c67af9604b89912dbdb61"></a>

### `slot_durations`

```c
uint8_t bt_hci_cp_le_set_conn_cte_rx_params::slot_durations
```

<a id="a89194a5b9e6c7f0c176c915e451911df"></a>

### `switch_pattern_len`

```c
uint8_t bt_hci_cp_le_set_conn_cte_rx_params::switch_pattern_len
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 91.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P090_bt_hci_cp_le_set_cl_cte_tx_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P092_bt_hci_cp_le_set_conn_cte_tx_params_结构体.md)
