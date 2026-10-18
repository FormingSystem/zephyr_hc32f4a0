---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-100
title: bt_hci_cp_le_set_ext_adv_param_v2_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__ext__adv__param__v2.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第100章\_bt\_hci\_cp\_le\_set\_ext\_adv\_param\_v2\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__ext__adv__param__v2.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 100.1\_数据成员（Data Fields）

<a id="r_ad9e43219b471e44884b33ea5ddd90513"></a>

```c
uint8_t handle
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[handle](#ad9e43219b471e44884b33ea5ddd90513)。

<a id="r_aff572d12a03ca9cbc2ee80f75e1f77c7"></a>

```c
uint16_t props
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[props](#aff572d12a03ca9cbc2ee80f75e1f77c7)。

<a id="r_a25fec4dc9203bb50bb030087b42f473e"></a>

```c
uint8_t prim_min_interval [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[prim_min_interval](#a25fec4dc9203bb50bb030087b42f473e)。

<a id="r_a6098216ae6ef0f9459aae16adecd193f"></a>

```c
uint8_t prim_max_interval [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[prim_max_interval](#a6098216ae6ef0f9459aae16adecd193f)。

<a id="r_a1a96a88729e311c6a60571997aae9fc3"></a>

```c
uint8_t prim_channel_map
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[prim_channel_map](#a1a96a88729e311c6a60571997aae9fc3)。

<a id="r_a554f89f00700bc3ea4996b0a971fedbf"></a>

```c
uint8_t own_addr_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[own_addr_type](#a554f89f00700bc3ea4996b0a971fedbf)。

<a id="r_ad8fccd11fbea598de62e057a69b72156"></a>

```c
bt_addr_le_t peer_addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[peer_addr](#ad8fccd11fbea598de62e057a69b72156)。

<a id="r_a047656dd56bf883f1e307dcabe96f1de"></a>

```c
uint8_t filter_policy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[filter_policy](#a047656dd56bf883f1e307dcabe96f1de)。

<a id="r_a5283a6a40d46e0fe787ed403acab9f90"></a>

```c
int8_t tx_power
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[tx_power](#a5283a6a40d46e0fe787ed403acab9f90)。

<a id="r_a92a215151c603c2f8dd1b7e730a8e979"></a>

```c
uint8_t prim_adv_phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[prim_adv_phy](#a92a215151c603c2f8dd1b7e730a8e979)。

<a id="r_ac31b52df1033d11585781fbecc10f578"></a>

```c
uint8_t sec_adv_max_skip
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sec_adv_max_skip](#ac31b52df1033d11585781fbecc10f578)。

<a id="r_a6c2a953fab938f304e815bd9d59d05ae"></a>

```c
uint8_t sec_adv_phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sec_adv_phy](#a6c2a953fab938f304e815bd9d59d05ae)。

<a id="r_aeb26f7f16e2c71542421aada577a993f"></a>

```c
uint8_t sid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sid](#aeb26f7f16e2c71542421aada577a993f)。

<a id="r_a9f2a6f38e8965dabe17ad743d3aeda70"></a>

```c
uint8_t scan_req_notify_enable
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[scan_req_notify_enable](#a9f2a6f38e8965dabe17ad743d3aeda70)。

<a id="r_a8767fb7f5492f0323edd9afb687318db"></a>

```c
uint8_t prim_adv_phy_opt
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[prim_adv_phy_opt](#a8767fb7f5492f0323edd9afb687318db)。

<a id="r_a0c7994ef034270a7fd814386e7b76cc8"></a>

```c
uint8_t sec_adv_phy_opt
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sec_adv_phy_opt](#a0c7994ef034270a7fd814386e7b76cc8)。

## 100.2\_详细说明（Detailed Documentation）

<a id="a047656dd56bf883f1e307dcabe96f1de"></a>

### `filter_policy`

```c
uint8_t bt_hci_cp_le_set_ext_adv_param_v2::filter_policy
```

<a id="ad9e43219b471e44884b33ea5ddd90513"></a>

### `handle`

```c
uint8_t bt_hci_cp_le_set_ext_adv_param_v2::handle
```

<a id="a554f89f00700bc3ea4996b0a971fedbf"></a>

### `own_addr_type`

```c
uint8_t bt_hci_cp_le_set_ext_adv_param_v2::own_addr_type
```

<a id="ad8fccd11fbea598de62e057a69b72156"></a>

### `peer_addr`

```c
bt_addr_le_t bt_hci_cp_le_set_ext_adv_param_v2::peer_addr
```

<a id="a92a215151c603c2f8dd1b7e730a8e979"></a>

### `prim_adv_phy`

```c
uint8_t bt_hci_cp_le_set_ext_adv_param_v2::prim_adv_phy
```

<a id="a8767fb7f5492f0323edd9afb687318db"></a>

### `prim_adv_phy_opt`

```c
uint8_t bt_hci_cp_le_set_ext_adv_param_v2::prim_adv_phy_opt
```

<a id="a1a96a88729e311c6a60571997aae9fc3"></a>

### `prim_channel_map`

```c
uint8_t bt_hci_cp_le_set_ext_adv_param_v2::prim_channel_map
```

<a id="a6098216ae6ef0f9459aae16adecd193f"></a>

### `prim_max_interval`

```c
uint8_t bt_hci_cp_le_set_ext_adv_param_v2::prim_max_interval[3]
```

<a id="a25fec4dc9203bb50bb030087b42f473e"></a>

### `prim_min_interval`

```c
uint8_t bt_hci_cp_le_set_ext_adv_param_v2::prim_min_interval[3]
```

<a id="aff572d12a03ca9cbc2ee80f75e1f77c7"></a>

### `props`

```c
uint16_t bt_hci_cp_le_set_ext_adv_param_v2::props
```

<a id="a9f2a6f38e8965dabe17ad743d3aeda70"></a>

### `scan_req_notify_enable`

```c
uint8_t bt_hci_cp_le_set_ext_adv_param_v2::scan_req_notify_enable
```

<a id="ac31b52df1033d11585781fbecc10f578"></a>

### `sec_adv_max_skip`

```c
uint8_t bt_hci_cp_le_set_ext_adv_param_v2::sec_adv_max_skip
```

<a id="a6c2a953fab938f304e815bd9d59d05ae"></a>

### `sec_adv_phy`

```c
uint8_t bt_hci_cp_le_set_ext_adv_param_v2::sec_adv_phy
```

<a id="a0c7994ef034270a7fd814386e7b76cc8"></a>

### `sec_adv_phy_opt`

```c
uint8_t bt_hci_cp_le_set_ext_adv_param_v2::sec_adv_phy_opt
```

<a id="aeb26f7f16e2c71542421aada577a993f"></a>

### `sid`

```c
uint8_t bt_hci_cp_le_set_ext_adv_param_v2::sid
```

<a id="a5283a6a40d46e0fe787ed403acab9f90"></a>

### `tx_power`

```c
int8_t bt_hci_cp_le_set_ext_adv_param_v2::tx_power
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 100.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P099_bt_hci_cp_le_set_ext_adv_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P101_bt_hci_cp_le_set_ext_scan_enable_结构体.md)
