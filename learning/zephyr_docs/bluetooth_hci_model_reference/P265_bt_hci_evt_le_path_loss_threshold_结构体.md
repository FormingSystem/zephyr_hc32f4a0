---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-265
title: bt_hci_evt_le_path_loss_threshold_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__path__loss__threshold.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第265章\_bt\_hci\_evt\_le\_path\_loss\_threshold\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__path__loss__threshold.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 265.1\_数据成员（Data Fields）

<a id="r_a19b1e37c5e35e1e18424615b5c25d37f"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a19b1e37c5e35e1e18424615b5c25d37f)。

<a id="r_ac2b04c57137dcb6812fda06d4a22402a"></a>

```c
uint8_t current_path_loss
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[current_path_loss](#ac2b04c57137dcb6812fda06d4a22402a)。

<a id="r_add7984e06d523bb34e8380dae1710b7f"></a>

```c
uint8_t zone_entered
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[zone_entered](#add7984e06d523bb34e8380dae1710b7f)。

## 265.2\_详细说明（Detailed Documentation）

<a id="ac2b04c57137dcb6812fda06d4a22402a"></a>

### `current_path_loss`

```c
uint8_t bt_hci_evt_le_path_loss_threshold::current_path_loss
```

<a id="a19b1e37c5e35e1e18424615b5c25d37f"></a>

### `handle`

```c
uint16_t bt_hci_evt_le_path_loss_threshold::handle
```

<a id="add7984e06d523bb34e8380dae1710b7f"></a>

### `zone_entered`

```c
uint8_t bt_hci_evt_le_path_loss_threshold::zone_entered
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 265.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P264_bt_hci_evt_le_past_received_v2_结构体.md) · [返回大纲](大纲.md) · [下一章](P266_bt_hci_evt_le_per_adv_response_结构体.md)
