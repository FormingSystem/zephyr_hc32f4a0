---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-38
title: bt_avrcp_get_item_attrs_cmd_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__get__item__attrs__cmd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_bt\_avrcp\_get\_item\_attrs\_cmd\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__get__item__attrs__cmd.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

获取条目属性（GetItemAttributes）命令请求。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

获取条目属性（GetItemAttributes）命令请求。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 38.1\_数据成员（Data Fields）

<a id="r_a3d111f69d7cd25de618fc36fc2e054cb"></a>

```c
uint8_t scope
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[scope](#a3d111f69d7cd25de618fc36fc2e054cb)。

作用域类型 `bt_avrcp_scope_t`。

<a id="r_aebe4e58e9b48d6145b66eebf01b86632"></a>

```c
uint8_t uid [8]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uid](#aebe4e58e9b48d6145b66eebf01b86632)。

条目的 64 位 UID。

<a id="r_ab611ce1a434f4db21899980120c6fc6d"></a>

```c
uint16_t uid_counter
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uid_counter](#ab611ce1a434f4db21899980120c6fc6d)。

UID 计数器（UID Counter）。

<a id="r_ab08431ab53f8fec8854d85dd695eeb16"></a>

```c
uint8_t num_attrs
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_attrs](#ab08431ab53f8fec8854d85dd695eeb16)。

`0x00` 表示全部属性，其他值表示数量。

<a id="r_a350e99496274adbdc452d69c88aa0691"></a>

```c
uint32_t attr_ids []
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[attr_ids](#a350e99496274adbdc452d69c88aa0691)。

属性 ID，类型为 `bt_avrcp_media_attr_id_t`。

## 38.2\_详细说明（Detailed Documentation）

<a id="a350e99496274adbdc452d69c88aa0691"></a>

### `attr_ids`

```c
uint32_t bt_avrcp_get_item_attrs_cmd::attr_ids[]
```

属性 ID，类型为 `bt_avrcp_media_attr_id_t`。

<a id="ab08431ab53f8fec8854d85dd695eeb16"></a>

### `num_attrs`

```c
uint8_t bt_avrcp_get_item_attrs_cmd::num_attrs
```

`0x00` 表示全部属性，其他值表示数量。

<a id="a3d111f69d7cd25de618fc36fc2e054cb"></a>

### `scope`

```c
uint8_t bt_avrcp_get_item_attrs_cmd::scope
```

作用域类型 `bt_avrcp_scope_t`。

<a id="aebe4e58e9b48d6145b66eebf01b86632"></a>

### `uid`

```c
uint8_t bt_avrcp_get_item_attrs_cmd::uid[8]
```

条目的 64 位 UID。

<a id="ab611ce1a434f4db21899980120c6fc6d"></a>

### `uid_counter`

```c
uint16_t bt_avrcp_get_item_attrs_cmd::uid_counter
```

UID 计数器（UID Counter）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 38.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_avrcp_scope_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaabab9a4f37b3f9653ca95dd4b5944707)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_avrcp_media_attr_id_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga0ebc5d2657688b70119e11ac20d24592)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P037_bt_avrcp_get_folder_items_rsp_结构体.md) · [返回大纲](大纲.md) · [下一章](P039_bt_avrcp_get_item_attrs_rsp_结构体.md)
