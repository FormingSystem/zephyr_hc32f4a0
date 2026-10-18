---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-342
title: bt_hci_rp_le_encrypt_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__encrypt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第342章\_bt\_hci\_rp\_le\_encrypt\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__encrypt.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 342.1\_数据成员（Data Fields）

<a id="r_aee480917cc6af7dea77717a9cb5840bb"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#aee480917cc6af7dea77717a9cb5840bb)。

<a id="r_ac20cd9f4ceffea6999114f65437aefdc"></a>

```c
uint8_t enc_data [16]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[enc_data](#ac20cd9f4ceffea6999114f65437aefdc)。

## 342.2\_详细说明（Detailed Documentation）

<a id="ac20cd9f4ceffea6999114f65437aefdc"></a>

### `enc_data`

```c
uint8_t bt_hci_rp_le_encrypt::enc_data[16]
```

<a id="aee480917cc6af7dea77717a9cb5840bb"></a>

### `status`

```c
uint8_t bt_hci_rp_le_encrypt::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 342.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P341_bt_hci_rp_le_default_past_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P343_bt_hci_rp_le_iso_receive_test_结构体.md)
