---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-47
title: bt_hci_cp_le_iso_receive_test_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__iso__receive__test.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第47章\_bt\_hci\_cp\_le\_iso\_receive\_test\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__iso__receive__test.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 47.1\_数据成员（Data Fields）

<a id="r_ac1272441f5c7b79e1ef5f644f099d19e"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#ac1272441f5c7b79e1ef5f644f099d19e)。

<a id="r_a9ce7e13fc1c1a7c87c01e1ecb24c5324"></a>

```c
uint8_t payload_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[payload_type](#a9ce7e13fc1c1a7c87c01e1ecb24c5324)。

## 47.2\_详细说明（Detailed Documentation）

<a id="ac1272441f5c7b79e1ef5f644f099d19e"></a>

### `handle`

```c
uint16_t bt_hci_cp_le_iso_receive_test::handle
```

<a id="a9ce7e13fc1c1a7c87c01e1ecb24c5324"></a>

### `payload_type`

```c
uint8_t bt_hci_cp_le_iso_receive_test::payload_type
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 47.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P046_bt_hci_cp_le_generate_dhkey_v2_结构体.md) · [返回大纲](大纲.md) · [下一章](P048_bt_hci_cp_le_iso_test_end_结构体.md)
