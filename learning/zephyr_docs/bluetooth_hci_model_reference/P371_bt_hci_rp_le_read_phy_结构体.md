---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-371
title: bt_hci_rp_le_read_phy_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__phy.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第371章\_bt\_hci\_rp\_le\_read\_phy\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__phy.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 371.1\_数据成员（Data Fields）

<a id="r_a65d412e37eb2cd839fae262f4f9d5b28"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a65d412e37eb2cd839fae262f4f9d5b28)。

<a id="r_ae708b4f8ad2632d73bedea640f138d9f"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#ae708b4f8ad2632d73bedea640f138d9f)。

<a id="r_a644c0065d97e5de006dc28f7bca62268"></a>

```c
uint8_t tx_phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_phy](#a644c0065d97e5de006dc28f7bca62268)。

<a id="r_a5a060e0c0d1e5f33222ab10a5d3977e8"></a>

```c
uint8_t rx_phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rx_phy](#a5a060e0c0d1e5f33222ab10a5d3977e8)。

## 371.2\_详细说明（Detailed Documentation）

<a id="ae708b4f8ad2632d73bedea640f138d9f"></a>

### `handle`

```c
uint16_t bt_hci_rp_le_read_phy::handle
```

<a id="a5a060e0c0d1e5f33222ab10a5d3977e8"></a>

### `rx_phy`

```c
uint8_t bt_hci_rp_le_read_phy::rx_phy
```

<a id="a65d412e37eb2cd839fae262f4f9d5b28"></a>

### `status`

```c
uint8_t bt_hci_rp_le_read_phy::status
```

<a id="a644c0065d97e5de006dc28f7bca62268"></a>

### `tx_phy`

```c
uint8_t bt_hci_rp_le_read_phy::tx_phy
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 371.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P370_bt_hci_rp_le_read_per_adv_list_size_结构体.md) · [返回大纲](大纲.md) · [下一章](P372_bt_hci_rp_le_read_rf_path_comp_结构体.md)
