---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-115
title: bt_hci_cp_le_set_per_adv_param_v2_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__per__adv__param__v2.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第115章\_bt\_hci\_cp\_le\_set\_per\_adv\_param\_v2\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__per__adv__param__v2.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 115.1\_数据成员（Data Fields）

<a id="r_aee1088b46914c8e26d9e97ce573291c6"></a>

```c
uint8_t handle
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[handle](#aee1088b46914c8e26d9e97ce573291c6)。

<a id="r_ae36e28210a515f73648e6f8b3984fb55"></a>

```c
uint16_t min_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[min_interval](#ae36e28210a515f73648e6f8b3984fb55)。

<a id="r_acc9718286ab0847a3444d3fc2d3c93bc"></a>

```c
uint16_t max_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_interval](#acc9718286ab0847a3444d3fc2d3c93bc)。

<a id="r_ad2d658bb0be35aee6b5c133fece89068"></a>

```c
uint16_t props
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[props](#ad2d658bb0be35aee6b5c133fece89068)。

<a id="r_a7bea764aa5d21e03946804566b1f9869"></a>

```c
uint8_t num_subevents
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_subevents](#a7bea764aa5d21e03946804566b1f9869)。

<a id="r_a79dfc3b13068d9c51f0a756f025aaeba"></a>

```c
uint8_t subevent_interval
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subevent_interval](#a79dfc3b13068d9c51f0a756f025aaeba)。

<a id="r_acdeb503c0a13291158ad389c9f6ac206"></a>

```c
uint8_t response_slot_delay
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[response_slot_delay](#acdeb503c0a13291158ad389c9f6ac206)。

<a id="r_a35fcc697e60d3c398f03be7503f611bd"></a>

```c
uint8_t response_slot_spacing
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[response_slot_spacing](#a35fcc697e60d3c398f03be7503f611bd)。

<a id="r_a2483eb4457f9dc22ff8473175662e260"></a>

```c
uint8_t num_response_slots
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_response_slots](#a2483eb4457f9dc22ff8473175662e260)。

## 115.2\_详细说明（Detailed Documentation）

<a id="aee1088b46914c8e26d9e97ce573291c6"></a>

### `handle`

```c
uint8_t bt_hci_cp_le_set_per_adv_param_v2::handle
```

<a id="acc9718286ab0847a3444d3fc2d3c93bc"></a>

### `max_interval`

```c
uint16_t bt_hci_cp_le_set_per_adv_param_v2::max_interval
```

<a id="ae36e28210a515f73648e6f8b3984fb55"></a>

### `min_interval`

```c
uint16_t bt_hci_cp_le_set_per_adv_param_v2::min_interval
```

<a id="a2483eb4457f9dc22ff8473175662e260"></a>

### `num_response_slots`

```c
uint8_t bt_hci_cp_le_set_per_adv_param_v2::num_response_slots
```

<a id="a7bea764aa5d21e03946804566b1f9869"></a>

### `num_subevents`

```c
uint8_t bt_hci_cp_le_set_per_adv_param_v2::num_subevents
```

<a id="ad2d658bb0be35aee6b5c133fece89068"></a>

### `props`

```c
uint16_t bt_hci_cp_le_set_per_adv_param_v2::props
```

<a id="acdeb503c0a13291158ad389c9f6ac206"></a>

### `response_slot_delay`

```c
uint8_t bt_hci_cp_le_set_per_adv_param_v2::response_slot_delay
```

<a id="a35fcc697e60d3c398f03be7503f611bd"></a>

### `response_slot_spacing`

```c
uint8_t bt_hci_cp_le_set_per_adv_param_v2::response_slot_spacing
```

<a id="a79dfc3b13068d9c51f0a756f025aaeba"></a>

### `subevent_interval`

```c
uint8_t bt_hci_cp_le_set_per_adv_param_v2::subevent_interval
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 115.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P114_bt_hci_cp_le_set_per_adv_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P116_bt_hci_cp_le_set_per_adv_recv_enable_结构体.md)
