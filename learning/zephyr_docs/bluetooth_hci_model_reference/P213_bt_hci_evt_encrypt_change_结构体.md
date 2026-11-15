---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-213
title: bt_hci_evt_encrypt_change_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__encrypt__change.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第213章\_bt\_hci\_evt\_encrypt\_change\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__encrypt__change.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 213.1\_数据成员（Data Fields）

<a id="r_af063bbd28d29edbcc81e907631167de7"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#af063bbd28d29edbcc81e907631167de7)。

<a id="r_a7737f659115ca602c1224c364a4c7404"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a7737f659115ca602c1224c364a4c7404)。

<a id="r_a61cc0e3c209acbb289d071515b44860a"></a>

```c
uint8_t encrypt
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[encrypt](#a61cc0e3c209acbb289d071515b44860a)。

## 213.2\_详细说明（Detailed Documentation）

<a id="a61cc0e3c209acbb289d071515b44860a"></a>

### `encrypt`

```c
uint8_t bt_hci_evt_encrypt_change::encrypt
```

<a id="a7737f659115ca602c1224c364a4c7404"></a>

### `handle`

```c
uint16_t bt_hci_evt_encrypt_change::handle
```

<a id="af063bbd28d29edbcc81e907631167de7"></a>

### `status`

```c
uint8_t bt_hci_evt_encrypt_change::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 213.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P212_bt_hci_evt_disconn_complete_结构体.md) · [返回大纲](大纲.md) · [下一章](P214_bt_hci_evt_encrypt_key_refresh_complete_结构体.md)
