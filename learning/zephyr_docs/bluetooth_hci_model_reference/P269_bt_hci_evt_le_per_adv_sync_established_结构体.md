---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-269
title: bt_hci_evt_le_per_adv_sync_established_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__per__adv__sync__established.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第269章\_bt\_hci\_evt\_le\_per\_adv\_sync\_established\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__per__adv__sync__established.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 269.1\_数据成员（Data Fields）

<a id="r_a9ebe918fee3121168dc5b45e64aaf263"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a9ebe918fee3121168dc5b45e64aaf263)。

<a id="r_a3af8529a858992f347ce9570c5696133"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a3af8529a858992f347ce9570c5696133)。

<a id="r_ab11929ef8d3c71c6f2cb7c549be21282"></a>

```c
uint8_t sid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sid](#ab11929ef8d3c71c6f2cb7c549be21282)。

<a id="r_adf65527ea968f4ece37d7e3c91c795d1"></a>

```c
bt_addr_le_t adv_addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[adv_addr](#adf65527ea968f4ece37d7e3c91c795d1)。

<a id="r_ab7ce6f56a69b54f02cde8fdae6860e42"></a>

```c
uint8_t phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phy](#ab7ce6f56a69b54f02cde8fdae6860e42)。

<a id="r_a4873b917a5bc140bb2f04ad2bee5dd69"></a>

```c
uint16_t interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval](#a4873b917a5bc140bb2f04ad2bee5dd69)。

<a id="r_aee68069899cc10bc38ad9fb95cf9b7b7"></a>

```c
uint8_t clock_accuracy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[clock_accuracy](#aee68069899cc10bc38ad9fb95cf9b7b7)。

## 269.2\_详细说明（Detailed Documentation）

<a id="adf65527ea968f4ece37d7e3c91c795d1"></a>

### `adv_addr`

```c
bt_addr_le_t bt_hci_evt_le_per_adv_sync_established::adv_addr
```

<a id="aee68069899cc10bc38ad9fb95cf9b7b7"></a>

### `clock_accuracy`

```c
uint8_t bt_hci_evt_le_per_adv_sync_established::clock_accuracy
```

<a id="a3af8529a858992f347ce9570c5696133"></a>

### `handle`

```c
uint16_t bt_hci_evt_le_per_adv_sync_established::handle
```

<a id="a4873b917a5bc140bb2f04ad2bee5dd69"></a>

### `interval`

```c
uint16_t bt_hci_evt_le_per_adv_sync_established::interval
```

<a id="ab7ce6f56a69b54f02cde8fdae6860e42"></a>

### `phy`

```c
uint8_t bt_hci_evt_le_per_adv_sync_established::phy
```

<a id="ab11929ef8d3c71c6f2cb7c549be21282"></a>

### `sid`

```c
uint8_t bt_hci_evt_le_per_adv_sync_established::sid
```

<a id="a9ebe918fee3121168dc5b45e64aaf263"></a>

### `status`

```c
uint8_t bt_hci_evt_le_per_adv_sync_established::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 269.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P268_bt_hci_evt_le_per_adv_subevent_data_request_结构体.md) · [返回大纲](大纲.md) · [下一章](P270_bt_hci_evt_le_per_adv_sync_established_v2_结构体.md)
