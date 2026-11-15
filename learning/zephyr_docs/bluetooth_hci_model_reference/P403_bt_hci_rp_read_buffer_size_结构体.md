---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-403
title: bt_hci_rp_read_buffer_size_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__read__buffer__size.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第403章\_bt\_hci\_rp\_read\_buffer\_size\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__read__buffer__size.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 403.1\_数据成员（Data Fields）

<a id="r_a6adf126acfcec722dc078d097d2b2ba8"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a6adf126acfcec722dc078d097d2b2ba8)。

<a id="r_aba3f1597c929e3721c769beb98000218"></a>

```c
uint16_t acl_max_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[acl_max_len](#aba3f1597c929e3721c769beb98000218)。

<a id="r_a7d475559145f469006b2ef147704cd99"></a>

```c
uint8_t sco_max_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sco_max_len](#a7d475559145f469006b2ef147704cd99)。

<a id="r_a87ff361282be71aa60c7f88c50a7492f"></a>

```c
uint16_t acl_max_num
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[acl_max_num](#a87ff361282be71aa60c7f88c50a7492f)。

<a id="r_abc01fa1df6d787f0a2cb865daed5f4cc"></a>

```c
uint16_t sco_max_num
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sco_max_num](#abc01fa1df6d787f0a2cb865daed5f4cc)。

## 403.2\_详细说明（Detailed Documentation）

<a id="aba3f1597c929e3721c769beb98000218"></a>

### `acl_max_len`

```c
uint16_t bt_hci_rp_read_buffer_size::acl_max_len
```

<a id="a87ff361282be71aa60c7f88c50a7492f"></a>

### `acl_max_num`

```c
uint16_t bt_hci_rp_read_buffer_size::acl_max_num
```

<a id="a7d475559145f469006b2ef147704cd99"></a>

### `sco_max_len`

```c
uint8_t bt_hci_rp_read_buffer_size::sco_max_len
```

<a id="abc01fa1df6d787f0a2cb865daed5f4cc"></a>

### `sco_max_num`

```c
uint16_t bt_hci_rp_read_buffer_size::sco_max_num
```

<a id="a6adf126acfcec722dc078d097d2b2ba8"></a>

### `status`

```c
uint8_t bt_hci_rp_read_buffer_size::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 403.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P402_bt_hci_rp_read_bd_addr_结构体.md) · [返回大纲](大纲.md) · [下一章](P404_bt_hci_rp_read_class_of_device_结构体.md)
