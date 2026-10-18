---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-82
title: bt_hci_cp_le_set_adv_data_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__adv__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第82章\_bt\_hci\_cp\_le\_set\_adv\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__adv__data.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 82.1\_数据成员（Data Fields）

<a id="r_a664313db17c12adb0de14371e46d26a8"></a>

```c
uint8_t len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[len](#a664313db17c12adb0de14371e46d26a8)。

<a id="r_a6fb8734ff5a9b77586b3e283b83985bb"></a>

```c
uint8_t data [31]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#a6fb8734ff5a9b77586b3e283b83985bb)。

## 82.2\_详细说明（Detailed Documentation）

<a id="a6fb8734ff5a9b77586b3e283b83985bb"></a>

### `data`

```c
uint8_t bt_hci_cp_le_set_adv_data::data[31]
```

<a id="a664313db17c12adb0de14371e46d26a8"></a>

### `len`

```c
uint8_t bt_hci_cp_le_set_adv_data::len
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 82.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P081_bt_hci_cp_le_set_addr_res_enable_结构体.md) · [返回大纲](大纲.md) · [下一章](P083_bt_hci_cp_le_set_adv_enable_结构体.md)
