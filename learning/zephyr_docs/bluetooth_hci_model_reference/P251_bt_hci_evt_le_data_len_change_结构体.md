---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-251
title: bt_hci_evt_le_data_len_change_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__data__len__change.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第251章\_bt\_hci\_evt\_le\_data\_len\_change\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__data__len__change.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 251.1\_数据成员（Data Fields）

<a id="r_a62ebc2f337f23f678c651bf3a276a2a7"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a62ebc2f337f23f678c651bf3a276a2a7)。

<a id="r_ae5ce481170336acafbe85687c672281b"></a>

```c
uint16_t max_tx_octets
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_tx_octets](#ae5ce481170336acafbe85687c672281b)。

<a id="r_a8264e7ec4aa37e9a699f81d0c56afa40"></a>

```c
uint16_t max_tx_time
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_tx_time](#a8264e7ec4aa37e9a699f81d0c56afa40)。

<a id="r_a60ecd89a8bbf06ae55b577e3d708d16f"></a>

```c
uint16_t max_rx_octets
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_rx_octets](#a60ecd89a8bbf06ae55b577e3d708d16f)。

<a id="r_a90771e400b998565e7a8bbf4288edd01"></a>

```c
uint16_t max_rx_time
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_rx_time](#a90771e400b998565e7a8bbf4288edd01)。

## 251.2\_详细说明（Detailed Documentation）

<a id="a62ebc2f337f23f678c651bf3a276a2a7"></a>

### `handle`

```c
uint16_t bt_hci_evt_le_data_len_change::handle
```

<a id="a60ecd89a8bbf06ae55b577e3d708d16f"></a>

### `max_rx_octets`

```c
uint16_t bt_hci_evt_le_data_len_change::max_rx_octets
```

<a id="a90771e400b998565e7a8bbf4288edd01"></a>

### `max_rx_time`

```c
uint16_t bt_hci_evt_le_data_len_change::max_rx_time
```

<a id="ae5ce481170336acafbe85687c672281b"></a>

### `max_tx_octets`

```c
uint16_t bt_hci_evt_le_data_len_change::max_tx_octets
```

<a id="a8264e7ec4aa37e9a699f81d0c56afa40"></a>

### `max_tx_time`

```c
uint16_t bt_hci_evt_le_data_len_change::max_tx_time
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 251.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P250_bt_hci_evt_le_cte_req_failed_结构体.md) · [返回大纲](大纲.md) · [下一章](P252_bt_hci_evt_le_direct_adv_info_结构体.md)
