---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-344
title: bt_hci_rp_le_iso_test_end_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__iso__test__end.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第344章\_bt\_hci\_rp\_le\_iso\_test\_end\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__iso__test__end.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 344.1\_数据成员（Data Fields）

<a id="r_a16feaeb739f6ed34d9ce3fc86248955c"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a16feaeb739f6ed34d9ce3fc86248955c)。

<a id="r_a4a4625d7b78abf3c039842df2a72ce8b"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a4a4625d7b78abf3c039842df2a72ce8b)。

<a id="r_a55490978e7416ecc308bf510f05afd4f"></a>

```c
uint32_t received_cnt
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[received_cnt](#a55490978e7416ecc308bf510f05afd4f)。

<a id="r_a10b3ee6110bc0bb9279b22f9963715c1"></a>

```c
uint32_t missed_cnt
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[missed_cnt](#a10b3ee6110bc0bb9279b22f9963715c1)。

<a id="r_ab4352fd5d9b822fb7fb75f8f5e2db6a9"></a>

```c
uint32_t failed_cnt
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[failed_cnt](#ab4352fd5d9b822fb7fb75f8f5e2db6a9)。

## 344.2\_详细说明（Detailed Documentation）

<a id="ab4352fd5d9b822fb7fb75f8f5e2db6a9"></a>

### `failed_cnt`

```c
uint32_t bt_hci_rp_le_iso_test_end::failed_cnt
```

<a id="a4a4625d7b78abf3c039842df2a72ce8b"></a>

### `handle`

```c
uint16_t bt_hci_rp_le_iso_test_end::handle
```

<a id="a10b3ee6110bc0bb9279b22f9963715c1"></a>

### `missed_cnt`

```c
uint32_t bt_hci_rp_le_iso_test_end::missed_cnt
```

<a id="a55490978e7416ecc308bf510f05afd4f"></a>

### `received_cnt`

```c
uint32_t bt_hci_rp_le_iso_test_end::received_cnt
```

<a id="a16feaeb739f6ed34d9ce3fc86248955c"></a>

### `status`

```c
uint8_t bt_hci_rp_le_iso_test_end::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 344.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P343_bt_hci_rp_le_iso_receive_test_结构体.md) · [返回大纲](大纲.md) · [下一章](P345_bt_hci_rp_le_iso_transmit_test_结构体.md)
