---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-279
title: bt_hci_evt_le_subrate_change_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__subrate__change.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第279章\_bt\_hci\_evt\_le\_subrate\_change\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__subrate__change.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 279.1\_数据成员（Data Fields）

<a id="r_aa49286a63d565feaf3d9329cd024ee9f"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#aa49286a63d565feaf3d9329cd024ee9f)。

<a id="r_adc08125e663a99c7232d0755c4bd760b"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#adc08125e663a99c7232d0755c4bd760b)。

<a id="r_a9387ffe45a856f7f443f5116a59a9ff2"></a>

```c
uint16_t subrate_factor
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[subrate_factor](#a9387ffe45a856f7f443f5116a59a9ff2)。

<a id="r_a95aaed5f8c93a1d6e8cab4c7ebfad8d7"></a>

```c
uint16_t peripheral_latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[peripheral_latency](#a95aaed5f8c93a1d6e8cab4c7ebfad8d7)。

<a id="r_a712b8b818115f1797787aab229040c8a"></a>

```c
uint16_t continuation_number
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[continuation_number](#a712b8b818115f1797787aab229040c8a)。

<a id="r_a2ad4a06feeb0d6d36461b4a4e53dfeb1"></a>

```c
uint16_t supervision_timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[supervision_timeout](#a2ad4a06feeb0d6d36461b4a4e53dfeb1)。

## 279.2\_详细说明（Detailed Documentation）

<a id="a712b8b818115f1797787aab229040c8a"></a>

### `continuation_number`

```c
uint16_t bt_hci_evt_le_subrate_change::continuation_number
```

<a id="adc08125e663a99c7232d0755c4bd760b"></a>

### `handle`

```c
uint16_t bt_hci_evt_le_subrate_change::handle
```

<a id="a95aaed5f8c93a1d6e8cab4c7ebfad8d7"></a>

### `peripheral_latency`

```c
uint16_t bt_hci_evt_le_subrate_change::peripheral_latency
```

<a id="aa49286a63d565feaf3d9329cd024ee9f"></a>

### `status`

```c
uint8_t bt_hci_evt_le_subrate_change::status
```

<a id="a9387ffe45a856f7f443f5116a59a9ff2"></a>

### `subrate_factor`

```c
uint16_t bt_hci_evt_le_subrate_change::subrate_factor
```

<a id="a2ad4a06feeb0d6d36461b4a4e53dfeb1"></a>

### `supervision_timeout`

```c
uint16_t bt_hci_evt_le_subrate_change::supervision_timeout
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 279.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P278_bt_hci_evt_le_scan_req_received_结构体.md) · [返回大纲](大纲.md) · [下一章](P280_bt_hci_evt_le_transmit_power_report_结构体.md)
