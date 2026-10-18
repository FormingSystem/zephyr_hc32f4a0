---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-99
title: bt_hci_cp_le_set_ext_adv_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__ext__adv__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第99章\_bt\_hci\_cp\_le\_set\_ext\_adv\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__ext__adv__param.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 99.1\_数据成员（Data Fields）

<a id="r_a65fe609dde9515212659087a024e7c65"></a>

```c
uint8_t handle
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[handle](#a65fe609dde9515212659087a024e7c65)。

<a id="r_a4af102ae90ca6917b3134491c5ff079f"></a>

```c
uint16_t props
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[props](#a4af102ae90ca6917b3134491c5ff079f)。

<a id="r_ab5a80941b3d832c2906daed8cf069a02"></a>

```c
uint8_t prim_min_interval [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[prim_min_interval](#ab5a80941b3d832c2906daed8cf069a02)。

<a id="r_a08aa741a56e825a11424bf024ac65e14"></a>

```c
uint8_t prim_max_interval [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[prim_max_interval](#a08aa741a56e825a11424bf024ac65e14)。

<a id="r_ad7a0b9028bcdb57a9011d4677412aed5"></a>

```c
uint8_t prim_channel_map
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[prim_channel_map](#ad7a0b9028bcdb57a9011d4677412aed5)。

<a id="r_a3594f7337ccd739f59ac7845757de0e8"></a>

```c
uint8_t own_addr_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[own_addr_type](#a3594f7337ccd739f59ac7845757de0e8)。

<a id="r_a819e599df4025036fab2dabd7c61ea37"></a>

```c
bt_addr_le_t peer_addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[peer_addr](#a819e599df4025036fab2dabd7c61ea37)。

<a id="r_a29a62f8989f89b014cadbad9b94e996a"></a>

```c
uint8_t filter_policy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[filter_policy](#a29a62f8989f89b014cadbad9b94e996a)。

<a id="r_a5f7f3e477b5b0b8122b85f3e53dd7878"></a>

```c
int8_t tx_power
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[tx_power](#a5f7f3e477b5b0b8122b85f3e53dd7878)。

<a id="r_a048874197ccbdbc626f0563be5c41ec7"></a>

```c
uint8_t prim_adv_phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[prim_adv_phy](#a048874197ccbdbc626f0563be5c41ec7)。

<a id="r_a5793c6afe545290a1e792bcc73585b72"></a>

```c
uint8_t sec_adv_max_skip
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sec_adv_max_skip](#a5793c6afe545290a1e792bcc73585b72)。

<a id="r_abc82ba984647eb00bc490c01ce746a15"></a>

```c
uint8_t sec_adv_phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sec_adv_phy](#abc82ba984647eb00bc490c01ce746a15)。

<a id="r_af8bc3509fdd5e89c27db466727fe1cd9"></a>

```c
uint8_t sid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sid](#af8bc3509fdd5e89c27db466727fe1cd9)。

<a id="r_ae694df46b1db4b029d1e177768b3821f"></a>

```c
uint8_t scan_req_notify_enable
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[scan_req_notify_enable](#ae694df46b1db4b029d1e177768b3821f)。

## 99.2\_详细说明（Detailed Documentation）

<a id="a29a62f8989f89b014cadbad9b94e996a"></a>

### `filter_policy`

```c
uint8_t bt_hci_cp_le_set_ext_adv_param::filter_policy
```

<a id="a65fe609dde9515212659087a024e7c65"></a>

### `handle`

```c
uint8_t bt_hci_cp_le_set_ext_adv_param::handle
```

<a id="a3594f7337ccd739f59ac7845757de0e8"></a>

### `own_addr_type`

```c
uint8_t bt_hci_cp_le_set_ext_adv_param::own_addr_type
```

<a id="a819e599df4025036fab2dabd7c61ea37"></a>

### `peer_addr`

```c
bt_addr_le_t bt_hci_cp_le_set_ext_adv_param::peer_addr
```

<a id="a048874197ccbdbc626f0563be5c41ec7"></a>

### `prim_adv_phy`

```c
uint8_t bt_hci_cp_le_set_ext_adv_param::prim_adv_phy
```

<a id="ad7a0b9028bcdb57a9011d4677412aed5"></a>

### `prim_channel_map`

```c
uint8_t bt_hci_cp_le_set_ext_adv_param::prim_channel_map
```

<a id="a08aa741a56e825a11424bf024ac65e14"></a>

### `prim_max_interval`

```c
uint8_t bt_hci_cp_le_set_ext_adv_param::prim_max_interval[3]
```

<a id="ab5a80941b3d832c2906daed8cf069a02"></a>

### `prim_min_interval`

```c
uint8_t bt_hci_cp_le_set_ext_adv_param::prim_min_interval[3]
```

<a id="a4af102ae90ca6917b3134491c5ff079f"></a>

### `props`

```c
uint16_t bt_hci_cp_le_set_ext_adv_param::props
```

<a id="ae694df46b1db4b029d1e177768b3821f"></a>

### `scan_req_notify_enable`

```c
uint8_t bt_hci_cp_le_set_ext_adv_param::scan_req_notify_enable
```

<a id="a5793c6afe545290a1e792bcc73585b72"></a>

### `sec_adv_max_skip`

```c
uint8_t bt_hci_cp_le_set_ext_adv_param::sec_adv_max_skip
```

<a id="abc82ba984647eb00bc490c01ce746a15"></a>

### `sec_adv_phy`

```c
uint8_t bt_hci_cp_le_set_ext_adv_param::sec_adv_phy
```

<a id="af8bc3509fdd5e89c27db466727fe1cd9"></a>

### `sid`

```c
uint8_t bt_hci_cp_le_set_ext_adv_param::sid
```

<a id="a5f7f3e477b5b0b8122b85f3e53dd7878"></a>

### `tx_power`

```c
int8_t bt_hci_cp_le_set_ext_adv_param::tx_power
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 99.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P098_bt_hci_cp_le_set_ext_adv_enable_结构体.md) · [返回大纲](大纲.md) · [下一章](P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md)
