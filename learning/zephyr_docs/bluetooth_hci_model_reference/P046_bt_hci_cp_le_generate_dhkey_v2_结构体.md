---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-46
title: bt_hci_cp_le_generate_dhkey_v2_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__generate__dhkey__v2.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第46章\_bt\_hci\_cp\_le\_generate\_dhkey\_v2\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__generate__dhkey__v2.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 46.1\_数据成员（Data Fields）

<a id="r_acc3007adf301674b9e847297007c3cd1"></a>

```c
uint8_t key [64]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[key](#acc3007adf301674b9e847297007c3cd1)。

<a id="r_a3d47ad6d9df4d4023d2586c915ee8f2c"></a>

```c
uint8_t key_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[key_type](#a3d47ad6d9df4d4023d2586c915ee8f2c)。

## 46.2\_详细说明（Detailed Documentation）

<a id="acc3007adf301674b9e847297007c3cd1"></a>

### `key`

```c
uint8_t bt_hci_cp_le_generate_dhkey_v2::key[64]
```

<a id="a3d47ad6d9df4d4023d2586c915ee8f2c"></a>

### `key_type`

```c
uint8_t bt_hci_cp_le_generate_dhkey_v2::key_type
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 46.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P045_bt_hci_cp_le_generate_dhkey_结构体.md) · [返回大纲](大纲.md) · [下一章](P047_bt_hci_cp_le_iso_receive_test_结构体.md)
