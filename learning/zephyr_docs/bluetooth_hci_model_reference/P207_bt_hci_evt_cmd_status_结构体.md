---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-207
title: bt_hci_evt_cmd_status_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__cmd__status.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第207章\_bt\_hci\_evt\_cmd\_status\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__cmd__status.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 207.1\_数据成员（Data Fields）

<a id="r_aedd1560409005dbce409b892af1e3edf"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#aedd1560409005dbce409b892af1e3edf)。

<a id="r_aed690e1cea2411df167e66cfaa742639"></a>

```c
uint8_t ncmd
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ncmd](#aed690e1cea2411df167e66cfaa742639)。

<a id="r_a34002b693dc201083be4be77cfddcdb5"></a>

```c
uint16_t opcode
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[opcode](#a34002b693dc201083be4be77cfddcdb5)。

## 207.2\_详细说明（Detailed Documentation）

<a id="aed690e1cea2411df167e66cfaa742639"></a>

### `ncmd`

```c
uint8_t bt_hci_evt_cmd_status::ncmd
```

<a id="a34002b693dc201083be4be77cfddcdb5"></a>

### `opcode`

```c
uint16_t bt_hci_evt_cmd_status::opcode
```

<a id="aedd1560409005dbce409b892af1e3edf"></a>

### `status`

```c
uint8_t bt_hci_evt_cmd_status::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 207.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P206_bt_hci_evt_cmd_complete_结构体.md) · [返回大纲](大纲.md) · [下一章](P208_bt_hci_evt_conn_complete_结构体.md)
