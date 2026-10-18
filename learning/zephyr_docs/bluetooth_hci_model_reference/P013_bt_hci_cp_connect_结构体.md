---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-13
title: bt_hci_cp_connect_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__connect.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_bt\_hci\_cp\_connect\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__connect.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 13.1\_数据成员（Data Fields）

<a id="r_a6f0753aad19d4c9591fa74152d151aa9"></a>

```c
bt_addr_t bdaddr
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bdaddr](#a6f0753aad19d4c9591fa74152d151aa9)。

<a id="r_a652a4e01641893a8588110dc505ceea0"></a>

```c
uint16_t packet_type
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[packet_type](#a652a4e01641893a8588110dc505ceea0)。

<a id="r_a35b0e1f73f696aae2ca519e16d7bb668"></a>

```c
uint8_t pscan_rep_mode
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pscan_rep_mode](#a35b0e1f73f696aae2ca519e16d7bb668)。

<a id="r_aef01fcac1b9792353bd8095e6911d6c3"></a>

```c
uint8_t reserved
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reserved](#aef01fcac1b9792353bd8095e6911d6c3)。

<a id="r_ac379ec381ad4cf6760750203924e5dda"></a>

```c
uint16_t clock_offset
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[clock_offset](#ac379ec381ad4cf6760750203924e5dda)。

<a id="r_a7a3d772bfd4c83236f9f1ad657e33f17"></a>

```c
uint8_t allow_role_switch
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[allow_role_switch](#a7a3d772bfd4c83236f9f1ad657e33f17)。

## 13.2\_详细说明（Detailed Documentation）

<a id="a7a3d772bfd4c83236f9f1ad657e33f17"></a>

### `allow_role_switch`

```c
uint8_t bt_hci_cp_connect::allow_role_switch
```

<a id="a6f0753aad19d4c9591fa74152d151aa9"></a>

### `bdaddr`

```c
bt_addr_t bt_hci_cp_connect::bdaddr
```

<a id="ac379ec381ad4cf6760750203924e5dda"></a>

### `clock_offset`

```c
uint16_t bt_hci_cp_connect::clock_offset
```

<a id="a652a4e01641893a8588110dc505ceea0"></a>

### `packet_type`

```c
uint16_t bt_hci_cp_connect::packet_type
```

<a id="a35b0e1f73f696aae2ca519e16d7bb668"></a>

### `pscan_rep_mode`

```c
uint8_t bt_hci_cp_connect::pscan_rep_mode
```

<a id="aef01fcac1b9792353bd8095e6911d6c3"></a>

### `reserved`

```c
uint8_t bt_hci_cp_connect::reserved
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 13.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P012_bt_hci_cp_configure_data_path_结构体.md) · [返回大纲](大纲.md) · [下一章](P014_bt_hci_cp_connect_cancel_结构体.md)
