---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-84
title: bt_hci_cp_le_set_adv_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__adv__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第84章\_bt\_hci\_cp\_le\_set\_adv\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__adv__param.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 84.1\_数据成员（Data Fields）

<a id="r_a2476c2a1858eab7e9b1449c1901363c4"></a>

```c
uint16_t min_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[min_interval](#a2476c2a1858eab7e9b1449c1901363c4)。

<a id="r_ab42c6b8f482e782d09386a3a1758903d"></a>

```c
uint16_t max_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_interval](#ab42c6b8f482e782d09386a3a1758903d)。

<a id="r_a9b09964156846fd480911dcc2d996a98"></a>

```c
uint8_t type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[type](#a9b09964156846fd480911dcc2d996a98)。

<a id="r_ad8c74cac74254354b314f07df7df1bf0"></a>

```c
uint8_t own_addr_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[own_addr_type](#ad8c74cac74254354b314f07df7df1bf0)。

<a id="r_ac774ef72175e43b083d04ecac263941b"></a>

```c
bt_addr_le_t direct_addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[direct_addr](#ac774ef72175e43b083d04ecac263941b)。

<a id="r_a2269ae424e47adddce5aa5f2f5b84c89"></a>

```c
uint8_t channel_map
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channel_map](#a2269ae424e47adddce5aa5f2f5b84c89)。

<a id="r_a662c5ae81f25a897a8e597f7227a1e39"></a>

```c
uint8_t filter_policy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[filter_policy](#a662c5ae81f25a897a8e597f7227a1e39)。

## 84.2\_详细说明（Detailed Documentation）

<a id="a2269ae424e47adddce5aa5f2f5b84c89"></a>

### `channel_map`

```c
uint8_t bt_hci_cp_le_set_adv_param::channel_map
```

<a id="ac774ef72175e43b083d04ecac263941b"></a>

### `direct_addr`

```c
bt_addr_le_t bt_hci_cp_le_set_adv_param::direct_addr
```

<a id="a662c5ae81f25a897a8e597f7227a1e39"></a>

### `filter_policy`

```c
uint8_t bt_hci_cp_le_set_adv_param::filter_policy
```

<a id="ab42c6b8f482e782d09386a3a1758903d"></a>

### `max_interval`

```c
uint16_t bt_hci_cp_le_set_adv_param::max_interval
```

<a id="a2476c2a1858eab7e9b1449c1901363c4"></a>

### `min_interval`

```c
uint16_t bt_hci_cp_le_set_adv_param::min_interval
```

<a id="ad8c74cac74254354b314f07df7df1bf0"></a>

### `own_addr_type`

```c
uint8_t bt_hci_cp_le_set_adv_param::own_addr_type
```

<a id="a9b09964156846fd480911dcc2d996a98"></a>

### `type`

```c
uint8_t bt_hci_cp_le_set_adv_param::type
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 84.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P083_bt_hci_cp_le_set_adv_enable_结构体.md) · [返回大纲](大纲.md) · [下一章](P085_bt_hci_cp_le_set_adv_set_random_addr_结构体.md)
