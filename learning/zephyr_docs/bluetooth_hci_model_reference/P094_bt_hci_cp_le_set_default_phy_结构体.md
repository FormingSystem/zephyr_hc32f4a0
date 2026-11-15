---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-94
title: bt_hci_cp_le_set_default_phy_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__default__phy.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第94章\_bt\_hci\_cp\_le\_set\_default\_phy\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__default__phy.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 94.1\_数据成员（Data Fields）

<a id="r_abe1d83e372e874739588812040d0b540"></a>

```c
uint8_t all_phys
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[all_phys](#abe1d83e372e874739588812040d0b540)。

<a id="r_a0c4ab2d91021466fd136af3a0b6bde2a"></a>

```c
uint8_t tx_phys
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_phys](#a0c4ab2d91021466fd136af3a0b6bde2a)。

<a id="r_a4c3410f2ce9fb2817bc5d143908936d1"></a>

```c
uint8_t rx_phys
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rx_phys](#a4c3410f2ce9fb2817bc5d143908936d1)。

## 94.2\_详细说明（Detailed Documentation）

<a id="abe1d83e372e874739588812040d0b540"></a>

### `all_phys`

```c
uint8_t bt_hci_cp_le_set_default_phy::all_phys
```

<a id="a4c3410f2ce9fb2817bc5d143908936d1"></a>

### `rx_phys`

```c
uint8_t bt_hci_cp_le_set_default_phy::rx_phys
```

<a id="a0c4ab2d91021466fd136af3a0b6bde2a"></a>

### `tx_phys`

```c
uint8_t bt_hci_cp_le_set_default_phy::tx_phys
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 94.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P093_bt_hci_cp_le_set_data_len_结构体.md) · [返回大纲](大纲.md) · [下一章](P095_bt_hci_cp_le_set_default_subrate_结构体.md)
