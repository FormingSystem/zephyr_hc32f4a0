---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-88
title: bt_hci_cp_le_set_cl_cte_sampling_enable_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__cl__cte__sampling__enable.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第88章\_bt\_hci\_cp\_le\_set\_cl\_cte\_sampling\_enable\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__cl__cte__sampling__enable.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 88.1\_数据成员（Data Fields）

<a id="r_a91d3458e2049ab434e220403b7ba235d"></a>

```c
uint16_t sync_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sync_handle](#a91d3458e2049ab434e220403b7ba235d)。

<a id="r_aca9e1316c716525f00308f64b8c6cec4"></a>

```c
uint8_t sampling_enable
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sampling_enable](#aca9e1316c716525f00308f64b8c6cec4)。

<a id="r_aaaed0fc39158c653041fd760a00cecec"></a>

```c
uint8_t slot_durations
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[slot_durations](#aaaed0fc39158c653041fd760a00cecec)。

<a id="r_a38e770b3e5f9d7d63a564dfa7c80451f"></a>

```c
uint8_t max_sampled_cte
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_sampled_cte](#a38e770b3e5f9d7d63a564dfa7c80451f)。

<a id="r_a4f52142ef1d2365859189b7a2abe050b"></a>

```c
uint8_t switch_pattern_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[switch_pattern_len](#a4f52142ef1d2365859189b7a2abe050b)。

<a id="r_a67bb2dbfe1707f76a5e211e007459c22"></a>

```c
uint8_t ant_ids [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ant_ids](#a67bb2dbfe1707f76a5e211e007459c22)。

## 88.2\_详细说明（Detailed Documentation）

<a id="a67bb2dbfe1707f76a5e211e007459c22"></a>

### `ant_ids`

```c
uint8_t bt_hci_cp_le_set_cl_cte_sampling_enable::ant_ids[0]
```

<a id="a38e770b3e5f9d7d63a564dfa7c80451f"></a>

### `max_sampled_cte`

```c
uint8_t bt_hci_cp_le_set_cl_cte_sampling_enable::max_sampled_cte
```

<a id="aca9e1316c716525f00308f64b8c6cec4"></a>

### `sampling_enable`

```c
uint8_t bt_hci_cp_le_set_cl_cte_sampling_enable::sampling_enable
```

<a id="aaaed0fc39158c653041fd760a00cecec"></a>

### `slot_durations`

```c
uint8_t bt_hci_cp_le_set_cl_cte_sampling_enable::slot_durations
```

<a id="a4f52142ef1d2365859189b7a2abe050b"></a>

### `switch_pattern_len`

```c
uint8_t bt_hci_cp_le_set_cl_cte_sampling_enable::switch_pattern_len
```

<a id="a91d3458e2049ab434e220403b7ba235d"></a>

### `sync_handle`

```c
uint16_t bt_hci_cp_le_set_cl_cte_sampling_enable::sync_handle
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 88.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P087_bt_hci_cp_le_set_cig_params_test_结构体.md) · [返回大纲](大纲.md) · [下一章](P089_bt_hci_cp_le_set_cl_cte_tx_enable_结构体.md)
