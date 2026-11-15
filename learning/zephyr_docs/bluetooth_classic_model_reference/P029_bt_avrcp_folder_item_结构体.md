---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-29
title: bt_avrcp_folder_item_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__folder__item.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_bt\_avrcp\_folder\_item\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__folder__item.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

文件夹条目（Folder Item），`item_type=0x02`。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

文件夹条目（Folder Item），`item_type=0x02`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 29.1\_数据成员（Data Fields）

<a id="r_a8bfa3c0f6854961df4378f0cbe4918e4"></a>

```c
struct bt_avrcp_item_hdr hdr
```

相关声明：[bt_avrcp_item_hdr](P049_bt_avrcp_item_hdr_结构体.md)、[hdr](#a8bfa3c0f6854961df4378f0cbe4918e4)。

<a id="r_ab6cd2f27e38730e3137dd739f4483585"></a>

```c
uint8_t uid [8]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uid](#ab6cd2f27e38730e3137dd739f4483585)。

64 位文件夹 UID。

<a id="r_abeb5d94d8a9f91be8769403b6f360991"></a>

```c
uint8_t folder_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[folder_type](#abeb5d94d8a9f91be8769403b6f360991)。

文件夹类型 `bt_avrcp_folder_type_t`。

<a id="r_a168cb4f00af9685d8b9023b09f5dcbe2"></a>

```c
uint8_t playable
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[playable](#a168cb4f00af9685d8b9023b09f5dcbe2)。

0 表示不可播放（Non-playable），1 表示可播放（Playable）。

<a id="r_ab6fa897bd3c15801955592c972220391"></a>

```c
uint16_t charset_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[charset_id](#ab6fa897bd3c15801955592c972220391)。

名称使用的字符集 ID，参见 `bt_avrcp_charset_t`。

<a id="r_a99a9de89c0d2e7f1b95f80f245e4126c"></a>

```c
uint16_t name_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[name_len](#a99a9de89c0d2e7f1b95f80f245e4126c)。

名称长度，单位为字节。

<a id="r_a682d5d56c49f82e04a812249042353ca"></a>

```c
uint8_t name []
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[name](#a682d5d56c49f82e04a812249042353ca)。

文件夹名称字符串数据。

## 29.2\_详细说明（Detailed Documentation）

<a id="ab6fa897bd3c15801955592c972220391"></a>

### `charset_id`

```c
uint16_t bt_avrcp_folder_item::charset_id
```

名称使用的字符集 ID，参见 `bt_avrcp_charset_t`。

<a id="abeb5d94d8a9f91be8769403b6f360991"></a>

### `folder_type`

```c
uint8_t bt_avrcp_folder_item::folder_type
```

文件夹类型 `bt_avrcp_folder_type_t`。

<a id="a8bfa3c0f6854961df4378f0cbe4918e4"></a>

### `hdr`

```c
struct bt_avrcp_item_hdr bt_avrcp_folder_item::hdr
```

<a id="a682d5d56c49f82e04a812249042353ca"></a>

### `name`

```c
uint8_t bt_avrcp_folder_item::name[]
```

文件夹名称字符串数据。

<a id="a99a9de89c0d2e7f1b95f80f245e4126c"></a>

### `name_len`

```c
uint16_t bt_avrcp_folder_item::name_len
```

名称长度，单位为字节。

<a id="a168cb4f00af9685d8b9023b09f5dcbe2"></a>

### `playable`

```c
uint8_t bt_avrcp_folder_item::playable
```

0 表示不可播放（Non-playable），1 表示可播放（Playable）。

<a id="ab6cd2f27e38730e3137dd739f4483585"></a>

### `uid`

```c
uint8_t bt_avrcp_folder_item::uid[8]
```

64 位文件夹 UID。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 29.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [bt_avrcp_item_hdr](P049_bt_avrcp_item_hdr_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_avrcp_folder_type_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga09d191c490efcfb9f8139975090be0d5)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_avrcp_charset_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga81330413af9eba049da6557b14ae082c)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P028_bt_avrcp_event_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P030_bt_avrcp_folder_name_结构体.md)
