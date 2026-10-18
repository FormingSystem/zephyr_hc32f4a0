---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-127
title: bt_hci_cp_le_start_encryption_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__start__encryption.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第127章\_bt\_hci\_cp\_le\_start\_encryption\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__start__encryption.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 127.1\_数据成员（Data Fields）

<a id="r_a4ac6d63f336e36a347242153aced4c71"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a4ac6d63f336e36a347242153aced4c71)。

<a id="r_a896961309d9b3f136beecf70a7e6e8e4"></a>

```c
uint8_t rand [8]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rand](#a896961309d9b3f136beecf70a7e6e8e4)。

用于标识长期密钥（Long Term Key，LTK）的 64 位随机数。

<a id="r_ac1e1fd8b6b97bbd6f27b6e4322b03530"></a>

```c
uint8_t ediv [2]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ediv](#ac1e1fd8b6b97bbd6f27b6e4322b03530)。

用于标识 LTK 的 16 位加密分散值（Encrypted Diversifier，EDIV）。

<a id="r_a99d2dd719ce38976e9da8a73f26839a1"></a>

```c
uint8_t ltk [16]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ltk](#a99d2dd719ce38976e9da8a73f26839a1)。

## 127.2\_详细说明（Detailed Documentation）

<a id="ac1e1fd8b6b97bbd6f27b6e4322b03530"></a>

### `ediv`

```c
uint8_t bt_hci_cp_le_start_encryption::ediv[2]
```

用于标识 LTK 的 16 位加密分散值（Encrypted Diversifier，EDIV）。

<a id="a4ac6d63f336e36a347242153aced4c71"></a>

### `handle`

```c
uint16_t bt_hci_cp_le_start_encryption::handle
```

<a id="a99d2dd719ce38976e9da8a73f26839a1"></a>

### `ltk`

```c
uint8_t bt_hci_cp_le_start_encryption::ltk[16]
```

<a id="a896961309d9b3f136beecf70a7e6e8e4"></a>

### `rand`

```c
uint8_t bt_hci_cp_le_start_encryption::rand[8]
```

用于标识长期密钥（Long Term Key，LTK）的 64 位随机数。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 127.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P126_bt_hci_cp_le_setup_iso_path_结构体.md) · [返回大纲](大纲.md) · [下一章](P128_bt_hci_cp_le_subrate_request_结构体.md)
