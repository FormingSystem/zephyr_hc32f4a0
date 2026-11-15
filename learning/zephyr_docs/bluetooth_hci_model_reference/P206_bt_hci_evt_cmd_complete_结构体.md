---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-206
title: bt_hci_evt_cmd_complete_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__cmd__complete.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第206章\_bt\_hci\_evt\_cmd\_complete\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__cmd__complete.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 206.1\_数据成员（Data Fields）

<a id="r_a4da0539f81057722c8c322685bc12a40"></a>

```c
uint8_t ncmd
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ncmd](#a4da0539f81057722c8c322685bc12a40)。

<a id="r_a3e61d980b4fa3084d3c50ead735fb76d"></a>

```c
uint16_t opcode
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[opcode](#a3e61d980b4fa3084d3c50ead735fb76d)。

## 206.2\_详细说明（Detailed Documentation）

<a id="a4da0539f81057722c8c322685bc12a40"></a>

### `ncmd`

```c
uint8_t bt_hci_evt_cmd_complete::ncmd
```

<a id="a3e61d980b4fa3084d3c50ead735fb76d"></a>

### `opcode`

```c
uint16_t bt_hci_evt_cmd_complete::opcode
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 206.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P205_bt_hci_evt_cc_status_结构体.md) · [返回大纲](大纲.md) · [下一章](P207_bt_hci_evt_cmd_status_结构体.md)
