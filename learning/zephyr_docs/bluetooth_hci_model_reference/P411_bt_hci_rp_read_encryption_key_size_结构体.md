---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-411
title: bt_hci_rp_read_encryption_key_size_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__read__encryption__key__size.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第411章\_bt\_hci\_rp\_read\_encryption\_key\_size\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__read__encryption__key__size.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 411.1\_数据成员（Data Fields）

<a id="r_a17213ccb9179739aa79c3749a2296f65"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a17213ccb9179739aa79c3749a2296f65)。

<a id="r_af0b89b2035f956891244b10409be0f51"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#af0b89b2035f956891244b10409be0f51)。

<a id="r_af1cd71c6216b26d460c04a68405f05d5"></a>

```c
uint8_t key_size
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[key_size](#af1cd71c6216b26d460c04a68405f05d5)。

## 411.2\_详细说明（Detailed Documentation）

<a id="af0b89b2035f956891244b10409be0f51"></a>

### `handle`

```c
uint16_t bt_hci_rp_read_encryption_key_size::handle
```

<a id="af1cd71c6216b26d460c04a68405f05d5"></a>

### `key_size`

```c
uint8_t bt_hci_rp_read_encryption_key_size::key_size
```

<a id="a17213ccb9179739aa79c3749a2296f65"></a>

### `status`

```c
uint8_t bt_hci_rp_read_encryption_key_size::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 411.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P410_bt_hci_rp_read_default_link_policy_settings_结构体.md) · [返回大纲](大纲.md) · [下一章](P412_bt_hci_rp_read_link_policy_settings_结构体.md)
