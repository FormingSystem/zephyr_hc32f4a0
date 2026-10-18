---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-355
title: bt_hci_rp_le_read_buffer_size_v2_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__buffer__size__v2.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第355章\_bt\_hci\_rp\_le\_read\_buffer\_size\_v2\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__buffer__size__v2.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 355.1\_数据成员（Data Fields）

<a id="r_a3b9cc0577d0f5f3c2b934a28915f2177"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a3b9cc0577d0f5f3c2b934a28915f2177)。

<a id="r_ac391149d3d7442e074aad4b98659bd02"></a>

```c
uint16_t acl_max_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[acl_max_len](#ac391149d3d7442e074aad4b98659bd02)。

<a id="r_a1c7938defb076d973b8339c17cc930df"></a>

```c
uint8_t acl_max_num
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[acl_max_num](#a1c7938defb076d973b8339c17cc930df)。

<a id="r_a9758d477c502575a1c176eb6a63e1a1a"></a>

```c
uint16_t iso_max_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[iso_max_len](#a9758d477c502575a1c176eb6a63e1a1a)。

<a id="r_ac3379adf42f9bbee8ae72fb4a7606fd1"></a>

```c
uint8_t iso_max_num
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[iso_max_num](#ac3379adf42f9bbee8ae72fb4a7606fd1)。

## 355.2\_详细说明（Detailed Documentation）

<a id="ac391149d3d7442e074aad4b98659bd02"></a>

### `acl_max_len`

```c
uint16_t bt_hci_rp_le_read_buffer_size_v2::acl_max_len
```

<a id="a1c7938defb076d973b8339c17cc930df"></a>

### `acl_max_num`

```c
uint8_t bt_hci_rp_le_read_buffer_size_v2::acl_max_num
```

<a id="a9758d477c502575a1c176eb6a63e1a1a"></a>

### `iso_max_len`

```c
uint16_t bt_hci_rp_le_read_buffer_size_v2::iso_max_len
```

<a id="ac3379adf42f9bbee8ae72fb4a7606fd1"></a>

### `iso_max_num`

```c
uint8_t bt_hci_rp_le_read_buffer_size_v2::iso_max_num
```

<a id="a3b9cc0577d0f5f3c2b934a28915f2177"></a>

### `status`

```c
uint8_t bt_hci_rp_le_read_buffer_size_v2::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 355.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P354_bt_hci_rp_le_read_buffer_size_结构体.md) · [返回大纲](大纲.md) · [下一章](P356_bt_hci_rp_le_read_chan_map_结构体.md)
