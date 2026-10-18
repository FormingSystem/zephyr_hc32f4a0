---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-236
title: bt_hci_evt_le_conn_rate_change_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__conn__rate__change.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第236章\_bt\_hci\_evt\_le\_conn\_rate\_change\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__conn__rate__change.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 236.1\_数据成员（Data Fields）

<a id="r_a8ad1a15c8b26be65d92944b4fc3c0ae1"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a8ad1a15c8b26be65d92944b4fc3c0ae1)。

<a id="r_a5b3947e67027b5425c21a0d509e19dc5"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a5b3947e67027b5425c21a0d509e19dc5)。

<a id="r_a31deb63251c897f7627b67c7cad2521f"></a>

```c
uint16_t conn_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_interval](#a31deb63251c897f7627b67c7cad2521f)。

<a id="r_a29d6bdbf04cb6bc68a84f3fafaf66a1f"></a>

```c
uint16_t subrate_factor
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[subrate_factor](#a29d6bdbf04cb6bc68a84f3fafaf66a1f)。

<a id="r_a67429e04fe601f367deeb5637d7d89c9"></a>

```c
uint16_t peripheral_latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[peripheral_latency](#a67429e04fe601f367deeb5637d7d89c9)。

<a id="r_a10671dd6e9b30b112e5841c482ee3067"></a>

```c
uint16_t continuation_number
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[continuation_number](#a10671dd6e9b30b112e5841c482ee3067)。

<a id="r_a3028aa8284c2f656f71d4b25da862cc9"></a>

```c
uint16_t supervision_timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[supervision_timeout](#a3028aa8284c2f656f71d4b25da862cc9)。

## 236.2\_详细说明（Detailed Documentation）

<a id="a31deb63251c897f7627b67c7cad2521f"></a>

### `conn_interval`

```c
uint16_t bt_hci_evt_le_conn_rate_change::conn_interval
```

<a id="a10671dd6e9b30b112e5841c482ee3067"></a>

### `continuation_number`

```c
uint16_t bt_hci_evt_le_conn_rate_change::continuation_number
```

<a id="a5b3947e67027b5425c21a0d509e19dc5"></a>

### `handle`

```c
uint16_t bt_hci_evt_le_conn_rate_change::handle
```

<a id="a67429e04fe601f367deeb5637d7d89c9"></a>

### `peripheral_latency`

```c
uint16_t bt_hci_evt_le_conn_rate_change::peripheral_latency
```

<a id="a8ad1a15c8b26be65d92944b4fc3c0ae1"></a>

### `status`

```c
uint8_t bt_hci_evt_le_conn_rate_change::status
```

<a id="a29d6bdbf04cb6bc68a84f3fafaf66a1f"></a>

### `subrate_factor`

```c
uint16_t bt_hci_evt_le_conn_rate_change::subrate_factor
```

<a id="a3028aa8284c2f656f71d4b25da862cc9"></a>

### `supervision_timeout`

```c
uint16_t bt_hci_evt_le_conn_rate_change::supervision_timeout
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 236.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P235_bt_hci_evt_le_conn_param_req_结构体.md) · [返回大纲](大纲.md) · [下一章](P237_bt_hci_evt_le_conn_update_complete_结构体.md)
