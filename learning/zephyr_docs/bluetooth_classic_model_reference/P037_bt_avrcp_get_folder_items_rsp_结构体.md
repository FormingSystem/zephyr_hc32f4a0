---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-37
title: bt_avrcp_get_folder_items_rsp_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__get__folder__items__rsp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_bt\_avrcp\_get\_folder\_items\_rsp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__get__folder__items__rsp.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

获取文件夹条目（GetFolderItems）响应。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

获取文件夹条目（GetFolderItems）响应。`items[]` 数组包含一串条目，每个条目均以 `bt_avrcp_item_hdr` 结构体开头。应用应根据头部的 `item_type` 字段选择相应结构体解析：`item_type = BT_AVRCP_ITEM_TYPE_MEDIA_PLAYER (0x01)` 时按 `bt_avrcp_media_player_item` 解析；`item_type = BT_AVRCP_ITEM_TYPE_FOLDER (0x02)` 时按 `bt_avrcp_folder_item` 解析；`item_type = BT_AVRCP_ITEM_TYPE_MEDIA_ELEMENT (0x03)` 时按 `bt_avrcp_media_element_item` 解析。说明（Note）：所有多八位字节字段都采用大端格式（Big-endian），需要使用 `sys_be16_to_cpu()`、`sys_be32_to_cpu()` 等函数转换。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 37.1\_数据成员（Data Fields）

<a id="r_a7ef2c44e62e2e35b86db3398a84fa88c"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a7ef2c44e62e2e35b86db3398a84fa88c)。

状态类型 `bt_avrcp_status_t`。

<a id="r_a387d5ed3a962e27632821505fd6f0b03"></a>

```c
uint16_t uid_counter
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uid_counter](#a387d5ed3a962e27632821505fd6f0b03)。

UID 计数器（UID Counter）。

<a id="r_a0b95f4d78a16bea65f18690f0081e099"></a>

```c
uint16_t num_items
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[num_items](#a0b95f4d78a16bea65f18690f0081e099)。

本响应中的条目数量。

<a id="r_a073136a279ed9b5f2aaf9db8c6f17607"></a>

```c
uint8_t items []
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[items](#a073136a279ed9b5f2aaf9db8c6f17607)。

条目序列；每个条目均以 `bt_avrcp_item_hdr` 开头。

## 37.2\_详细说明（Detailed Documentation）

<a id="a073136a279ed9b5f2aaf9db8c6f17607"></a>

### `items`

```c
uint8_t bt_avrcp_get_folder_items_rsp::items[]
```

条目序列；每个条目均以 `bt_avrcp_item_hdr` 开头。

<a id="a0b95f4d78a16bea65f18690f0081e099"></a>

### `num_items`

```c
uint16_t bt_avrcp_get_folder_items_rsp::num_items
```

本响应中的条目数量。

<a id="a7ef2c44e62e2e35b86db3398a84fa88c"></a>

### `status`

```c
uint8_t bt_avrcp_get_folder_items_rsp::status
```

状态类型 `bt_avrcp_status_t`。

<a id="a387d5ed3a962e27632821505fd6f0b03"></a>

### `uid_counter`

```c
uint16_t bt_avrcp_get_folder_items_rsp::uid_counter
```

UID 计数器（UID Counter）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 37.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_avrcp_status_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga52368f4cc655bab75f96da80ddaaabe0)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_avrcp_item_hdr](P049_bt_avrcp_item_hdr_结构体.md)
- [bt_avrcp_media_player_item](P055_bt_avrcp_media_player_item_结构体.md)
- [bt_avrcp_folder_item](P029_bt_avrcp_folder_item_结构体.md)
- [bt_avrcp_media_element_item](P054_bt_avrcp_media_element_item_结构体.md)
- [sys_be16_to_cpu()](../byteorder_reference/P001_系统字节序头文件参考.md#a840037a5fd3d36817dc92a44469df704)
- [sys_be32_to_cpu()](../byteorder_reference/P001_系统字节序头文件参考.md#aee4cefae7f089197e77c487faafda269)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P036_bt_avrcp_get_folder_items_cmd_结构体.md) · [返回大纲](大纲.md) · [下一章](P038_bt_avrcp_get_item_attrs_cmd_结构体.md)
