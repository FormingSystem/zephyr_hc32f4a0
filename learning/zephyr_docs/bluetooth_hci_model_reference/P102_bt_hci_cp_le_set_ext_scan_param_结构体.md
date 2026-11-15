---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-102
title: bt_hci_cp_le_set_ext_scan_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__ext__scan__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第102章\_bt\_hci\_cp\_le\_set\_ext\_scan\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__ext__scan__param.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 102.1\_数据成员（Data Fields）

<a id="r_a3418aa8dbdb8062ee452f5756eb9f30c"></a>

```c
uint8_t own_addr_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[own_addr_type](#a3418aa8dbdb8062ee452f5756eb9f30c)。

<a id="r_a47f6cf7f83451dcc2feac1a8d5837ad8"></a>

```c
uint8_t filter_policy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[filter_policy](#a47f6cf7f83451dcc2feac1a8d5837ad8)。

<a id="r_a6c38b7d074eb3c0cf5c301eb6c03b60c"></a>

```c
uint8_t phys
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phys](#a6c38b7d074eb3c0cf5c301eb6c03b60c)。

<a id="r_ab4eab9a52dca01bc19b35607d6ec5d36"></a>

```c
struct bt_hci_ext_scan_phy p [0]
```

相关声明：[bt_hci_ext_scan_phy](P309_bt_hci_ext_scan_phy_结构体.md)、[p](#ab4eab9a52dca01bc19b35607d6ec5d36)。

## 102.2\_详细说明（Detailed Documentation）

<a id="a47f6cf7f83451dcc2feac1a8d5837ad8"></a>

### `filter_policy`

```c
uint8_t bt_hci_cp_le_set_ext_scan_param::filter_policy
```

<a id="a3418aa8dbdb8062ee452f5756eb9f30c"></a>

### `own_addr_type`

```c
uint8_t bt_hci_cp_le_set_ext_scan_param::own_addr_type
```

<a id="ab4eab9a52dca01bc19b35607d6ec5d36"></a>

### `p`

```c
struct bt_hci_ext_scan_phy bt_hci_cp_le_set_ext_scan_param::p[0]
```

<a id="a6c38b7d074eb3c0cf5c301eb6c03b60c"></a>

### `phys`

```c
uint8_t bt_hci_cp_le_set_ext_scan_param::phys
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 102.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_hci_ext_scan_phy](P309_bt_hci_ext_scan_phy_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P101_bt_hci_cp_le_set_ext_scan_enable_结构体.md) · [返回大纲](大纲.md) · [下一章](P103_bt_hci_cp_le_set_ext_scan_rsp_data_结构体.md)
