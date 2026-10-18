---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-92
title: bt_hci_cp_le_set_conn_cte_tx_params_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__conn__cte__tx__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第92章\_bt\_hci\_cp\_le\_set\_conn\_cte\_tx\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__conn__cte__tx__params.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 92.1\_数据成员（Data Fields）

<a id="r_ae0a482982d804ffd7d16ea2b413e538d"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#ae0a482982d804ffd7d16ea2b413e538d)。

<a id="r_ab47f852b476ac2c35fc0631180e19fb4"></a>

```c
uint8_t cte_types
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cte_types](#ab47f852b476ac2c35fc0631180e19fb4)。

<a id="r_a8f0e5ee74662056f00eaa3a8c72f6fc4"></a>

```c
uint8_t switch_pattern_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[switch_pattern_len](#a8f0e5ee74662056f00eaa3a8c72f6fc4)。

<a id="r_abff85d652b3b2fd55ad78e53887cd7ce"></a>

```c
uint8_t ant_ids [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ant_ids](#abff85d652b3b2fd55ad78e53887cd7ce)。

## 92.2\_详细说明（Detailed Documentation）

<a id="abff85d652b3b2fd55ad78e53887cd7ce"></a>

### `ant_ids`

```c
uint8_t bt_hci_cp_le_set_conn_cte_tx_params::ant_ids[0]
```

<a id="ab47f852b476ac2c35fc0631180e19fb4"></a>

### `cte_types`

```c
uint8_t bt_hci_cp_le_set_conn_cte_tx_params::cte_types
```

<a id="ae0a482982d804ffd7d16ea2b413e538d"></a>

### `handle`

```c
uint16_t bt_hci_cp_le_set_conn_cte_tx_params::handle
```

<a id="a8f0e5ee74662056f00eaa3a8c72f6fc4"></a>

### `switch_pattern_len`

```c
uint8_t bt_hci_cp_le_set_conn_cte_tx_params::switch_pattern_len
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 92.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P091_bt_hci_cp_le_set_conn_cte_rx_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P093_bt_hci_cp_le_set_data_len_结构体.md)
