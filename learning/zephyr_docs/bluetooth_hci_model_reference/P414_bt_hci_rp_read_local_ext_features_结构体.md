---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-414
title: bt_hci_rp_read_local_ext_features_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__read__local__ext__features.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第414章\_bt\_hci\_rp\_read\_local\_ext\_features\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__read__local__ext__features.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 414.1\_数据成员（Data Fields）

<a id="r_a9011f2c89f75939fa92fcf249d2203da"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a9011f2c89f75939fa92fcf249d2203da)。

<a id="r_a7e3669651dc2c2ed9541b7e4945a27f9"></a>

```c
uint8_t page
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[page](#a7e3669651dc2c2ed9541b7e4945a27f9)。

<a id="r_a3532e208b3fd347db80d8c55eade3c2d"></a>

```c
uint8_t max_page
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_page](#a3532e208b3fd347db80d8c55eade3c2d)。

<a id="r_a669e8c6faa4e45f472e4f8a3ebb03050"></a>

```c
uint8_t ext_features [8]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ext_features](#a669e8c6faa4e45f472e4f8a3ebb03050)。

## 414.2\_详细说明（Detailed Documentation）

<a id="a669e8c6faa4e45f472e4f8a3ebb03050"></a>

### `ext_features`

```c
uint8_t bt_hci_rp_read_local_ext_features::ext_features[8]
```

<a id="a3532e208b3fd347db80d8c55eade3c2d"></a>

### `max_page`

```c
uint8_t bt_hci_rp_read_local_ext_features::max_page
```

<a id="a7e3669651dc2c2ed9541b7e4945a27f9"></a>

### `page`

```c
uint8_t bt_hci_rp_read_local_ext_features::page
```

<a id="a9011f2c89f75939fa92fcf249d2203da"></a>

### `status`

```c
uint8_t bt_hci_rp_read_local_ext_features::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 414.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P413_bt_hci_rp_read_link_supervision_timeout_结构体.md) · [返回大纲](大纲.md) · [下一章](P415_bt_hci_rp_read_local_features_结构体.md)
