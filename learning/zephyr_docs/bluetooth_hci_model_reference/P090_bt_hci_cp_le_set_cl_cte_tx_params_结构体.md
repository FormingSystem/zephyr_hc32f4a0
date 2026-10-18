---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-90
title: bt_hci_cp_le_set_cl_cte_tx_params_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__cl__cte__tx__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第90章\_bt\_hci\_cp\_le\_set\_cl\_cte\_tx\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__cl__cte__tx__params.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 90.1\_数据成员（Data Fields）

<a id="r_a8f20e6e3bb408551d6cc494ad19391c4"></a>

```c
uint8_t handle
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[handle](#a8f20e6e3bb408551d6cc494ad19391c4)。

<a id="r_ab5c4742cf37cf7e802423beb4a9b4fa2"></a>

```c
uint8_t cte_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cte_len](#ab5c4742cf37cf7e802423beb4a9b4fa2)。

<a id="r_a869192cea35f4cd57984614e4c8bb5a5"></a>

```c
uint8_t cte_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cte_type](#a869192cea35f4cd57984614e4c8bb5a5)。

<a id="r_af5e82bf572b385904a0f24219bdc72ca"></a>

```c
uint8_t cte_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cte_count](#af5e82bf572b385904a0f24219bdc72ca)。

<a id="r_a8208571653e444221648d2a884eabfae"></a>

```c
uint8_t switch_pattern_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[switch_pattern_len](#a8208571653e444221648d2a884eabfae)。

<a id="r_a27a228653ea560a77369a6b1829a8a9d"></a>

```c
uint8_t ant_ids [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ant_ids](#a27a228653ea560a77369a6b1829a8a9d)。

## 90.2\_详细说明（Detailed Documentation）

<a id="a27a228653ea560a77369a6b1829a8a9d"></a>

### `ant_ids`

```c
uint8_t bt_hci_cp_le_set_cl_cte_tx_params::ant_ids[0]
```

<a id="af5e82bf572b385904a0f24219bdc72ca"></a>

### `cte_count`

```c
uint8_t bt_hci_cp_le_set_cl_cte_tx_params::cte_count
```

<a id="ab5c4742cf37cf7e802423beb4a9b4fa2"></a>

### `cte_len`

```c
uint8_t bt_hci_cp_le_set_cl_cte_tx_params::cte_len
```

<a id="a869192cea35f4cd57984614e4c8bb5a5"></a>

### `cte_type`

```c
uint8_t bt_hci_cp_le_set_cl_cte_tx_params::cte_type
```

<a id="a8f20e6e3bb408551d6cc494ad19391c4"></a>

### `handle`

```c
uint8_t bt_hci_cp_le_set_cl_cte_tx_params::handle
```

<a id="a8208571653e444221648d2a884eabfae"></a>

### `switch_pattern_len`

```c
uint8_t bt_hci_cp_le_set_cl_cte_tx_params::switch_pattern_len
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 90.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P089_bt_hci_cp_le_set_cl_cte_tx_enable_结构体.md) · [返回大纲](大纲.md) · [下一章](P091_bt_hci_cp_le_set_conn_cte_rx_params_结构体.md)
