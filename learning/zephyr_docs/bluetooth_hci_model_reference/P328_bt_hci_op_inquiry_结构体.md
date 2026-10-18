---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-328
title: bt_hci_op_inquiry_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__op__inquiry.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第328章\_bt\_hci\_op\_inquiry\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__op__inquiry.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 328.1\_数据成员（Data Fields）

<a id="r_abdd03feccecbdbbb5d2c7c7f3213b62f"></a>

```c
uint8_t lap [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[lap](#abdd03feccecbdbbb5d2c7c7f3213b62f)。

<a id="r_ae77fa706c9875b5568a4af26a7724d08"></a>

```c
uint8_t length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[length](#ae77fa706c9875b5568a4af26a7724d08)。

<a id="r_ac8ed23243dbd9a7c46fedd8abe9666f5"></a>

```c
uint8_t num_rsp
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_rsp](#ac8ed23243dbd9a7c46fedd8abe9666f5)。

## 328.2\_详细说明（Detailed Documentation）

<a id="abdd03feccecbdbbb5d2c7c7f3213b62f"></a>

### `lap`

```c
uint8_t bt_hci_op_inquiry::lap[3]
```

<a id="ae77fa706c9875b5568a4af26a7724d08"></a>

### `length`

```c
uint8_t bt_hci_op_inquiry::length
```

<a id="ac8ed23243dbd9a7c46fedd8abe9666f5"></a>

### `num_rsp`

```c
uint8_t bt_hci_op_inquiry::num_rsp
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 328.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P327_bt_hci_mesh_pattern_结构体.md) · [返回大纲](大纲.md) · [下一章](P329_bt_hci_op_le_connection_rate_request_结构体.md)
