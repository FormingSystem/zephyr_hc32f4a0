---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-5
title: bt_hci_cmd_hdr_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cmd__hdr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_bt\_hci\_cmd\_hdr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cmd__hdr.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 5.1\_数据成员（Data Fields）

<a id="r_a09c63aab094ca0f39bab44708fdb83e4"></a>

```c
uint16_t opcode
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[opcode](#a09c63aab094ca0f39bab44708fdb83e4)。

<a id="r_afe2a97da8b473cafd3cc4e5e52dadf93"></a>

```c
uint8_t param_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[param_len](#afe2a97da8b473cafd3cc4e5e52dadf93)。

## 5.2\_详细说明（Detailed Documentation）

<a id="a09c63aab094ca0f39bab44708fdb83e4"></a>

### `opcode`

```c
uint16_t bt_hci_cmd_hdr::opcode
```

<a id="afe2a97da8b473cafd3cc4e5e52dadf93"></a>

### `param_len`

```c
uint8_t bt_hci_cmd_hdr::param_len
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 5.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P004_bt_hci_cis_params_test_结构体.md) · [返回大纲](大纲.md) · [下一章](P006_bt_hci_codec_capability_info_结构体.md)
