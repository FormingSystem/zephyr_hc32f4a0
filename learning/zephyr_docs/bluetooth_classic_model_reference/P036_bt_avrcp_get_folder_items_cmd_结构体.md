---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-36
title: bt_avrcp_get_folder_items_cmd_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__get__folder__items__cmd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第36章\_bt\_avrcp\_get\_folder\_items\_cmd\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__get__folder__items__cmd.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

获取文件夹条目（GetFolderItems）命令请求。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

获取文件夹条目（GetFolderItems）命令请求。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 36.1\_数据成员（Data Fields）

<a id="r_af89fb8a745c45a3b768d16d93d5d4287"></a>

```c
uint8_t scope
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[scope](#af89fb8a745c45a3b768d16d93d5d4287)。

作用域类型 `bt_avrcp_scope_t`。

<a id="r_ae362914e3f3be32d6381035176431c88"></a>

```c
uint32_t start_item
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[start_item](#ae362914e3f3be32d6381035176431c88)。

起始条目索引。

<a id="r_abf2e154d28317043a88ea00475d777a2"></a>

```c
uint32_t end_item
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[end_item](#abf2e154d28317043a88ea00475d777a2)。

结束条目索引，包含该条目。

<a id="r_a7068f5115cf58c075f1deefbb10e4627"></a>

```c
uint8_t attr_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[attr_count](#a7068f5115cf58c075f1deefbb10e4627)。

`0x00` 表示全部，`0x01..0xFE` 表示数量，`0xFF` 表示无。

<a id="r_a790f3718f2e6e3d32d1824794a146e4e"></a>

```c
uint32_t attr_ids []
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[attr_ids](#a790f3718f2e6e3d32d1824794a146e4e)。

属性 ID，类型为 `bt_avrcp_media_attr_id_t`。

## 36.2\_详细说明（Detailed Documentation）

<a id="a7068f5115cf58c075f1deefbb10e4627"></a>

### `attr_count`

```c
uint8_t bt_avrcp_get_folder_items_cmd::attr_count
```

`0x00` 表示全部，`0x01..0xFE` 表示数量，`0xFF` 表示无。

<a id="a790f3718f2e6e3d32d1824794a146e4e"></a>

### `attr_ids`

```c
uint32_t bt_avrcp_get_folder_items_cmd::attr_ids[]
```

属性 ID，类型为 `bt_avrcp_media_attr_id_t`。

<a id="abf2e154d28317043a88ea00475d777a2"></a>

### `end_item`

```c
uint32_t bt_avrcp_get_folder_items_cmd::end_item
```

结束条目索引，包含该条目。

<a id="af89fb8a745c45a3b768d16d93d5d4287"></a>

### `scope`

```c
uint8_t bt_avrcp_get_folder_items_cmd::scope
```

作用域类型 `bt_avrcp_scope_t`。

<a id="ae362914e3f3be32d6381035176431c88"></a>

### `start_item`

```c
uint32_t bt_avrcp_get_folder_items_cmd::start_item
```

起始条目索引。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 36.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_avrcp_scope_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaabab9a4f37b3f9653ca95dd4b5944707)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_avrcp_media_attr_id_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga0ebc5d2657688b70119e11ac20d24592)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P035_bt_avrcp_get_element_attrs_rsp_结构体.md) · [返回大纲](大纲.md) · [下一章](P037_bt_avrcp_get_folder_items_rsp_结构体.md)
