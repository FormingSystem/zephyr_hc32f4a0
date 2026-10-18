---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-123
title: bt_hci_cp_le_set_scan_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__scan__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第123章\_bt\_hci\_cp\_le\_set\_scan\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__scan__param.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 123.1\_数据成员（Data Fields）

<a id="r_ad19a479cc3c27ab24286b537b646261e"></a>

```c
uint8_t scan_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[scan_type](#ad19a479cc3c27ab24286b537b646261e)。

<a id="r_adcd8be074a8b19e0e7d02c4ea8209c93"></a>

```c
uint16_t interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval](#adcd8be074a8b19e0e7d02c4ea8209c93)。

<a id="r_a3b5b4767092fc69a63d2219d60722407"></a>

```c
uint16_t window
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[window](#a3b5b4767092fc69a63d2219d60722407)。

<a id="r_a694c74a6fc95f767d2e89e6596d51e98"></a>

```c
uint8_t addr_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[addr_type](#a694c74a6fc95f767d2e89e6596d51e98)。

<a id="r_ab7a268e17a5d564d475ff9dee5e6e14b"></a>

```c
uint8_t filter_policy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[filter_policy](#ab7a268e17a5d564d475ff9dee5e6e14b)。

## 123.2\_详细说明（Detailed Documentation）

<a id="a694c74a6fc95f767d2e89e6596d51e98"></a>

### `addr_type`

```c
uint8_t bt_hci_cp_le_set_scan_param::addr_type
```

<a id="ab7a268e17a5d564d475ff9dee5e6e14b"></a>

### `filter_policy`

```c
uint8_t bt_hci_cp_le_set_scan_param::filter_policy
```

<a id="adcd8be074a8b19e0e7d02c4ea8209c93"></a>

### `interval`

```c
uint16_t bt_hci_cp_le_set_scan_param::interval
```

<a id="ad19a479cc3c27ab24286b537b646261e"></a>

### `scan_type`

```c
uint8_t bt_hci_cp_le_set_scan_param::scan_type
```

<a id="a3b5b4767092fc69a63d2219d60722407"></a>

### `window`

```c
uint16_t bt_hci_cp_le_set_scan_param::window
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 123.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P122_bt_hci_cp_le_set_scan_enable_结构体.md) · [返回大纲](大纲.md) · [下一章](P124_bt_hci_cp_le_set_scan_rsp_data_结构体.md)
