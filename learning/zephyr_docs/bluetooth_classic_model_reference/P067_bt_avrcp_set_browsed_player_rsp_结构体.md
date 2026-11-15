---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-67
title: bt_avrcp_set_browsed_player_rsp_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__set__browsed__player__rsp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第67章\_bt\_avrcp\_set\_browsed\_player\_rsp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__set__browsed__player__rsp.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

设置浏览播放器（Set Browsed Player）响应结构体。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

设置浏览播放器（Set Browsed Player）响应结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 67.1\_数据成员（Data Fields）

<a id="r_a7d07c8595a14800385db33662b3096c5"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a7d07c8595a14800385db33662b3096c5)。

状态，类型为 `bt_avrcp_status_t`。

<a id="r_a5c0a40b5fbcd85dca0b904a106cfede9"></a>

```c
uint16_t uid_counter
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uid_counter](#a5c0a40b5fbcd85dca0b904a106cfede9)。

UID 计数器（UID Counter）。

<a id="r_a995907daaada393c045265583d0bad92"></a>

```c
uint32_t num_items
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[num_items](#a995907daaada393c045265583d0bad92)。

文件夹中的条目数量。

<a id="r_a61e93ead82b56cb3f61d1337423af05d"></a>

```c
uint16_t charset_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[charset_id](#a61e93ead82b56cb3f61d1337423af05d)。

字符集 ID，类型为 `bt_avrcp_charset_t`。

<a id="r_a9c7989c84c89790673a0f25922a72f59"></a>

```c
uint8_t folder_depth
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[folder_depth](#a9c7989c84c89790673a0f25922a72f59)。

文件夹深度（Folder Depth）。

<a id="r_a889cfb87961402d8a41b17292ec89b11"></a>

```c
struct bt_avrcp_folder_name folder_names [0]
```

相关声明：[bt_avrcp_folder_name](P030_bt_avrcp_folder_name_结构体.md)、[folder_names](#a889cfb87961402d8a41b17292ec89b11)。

文件夹名称数据。

## 67.2\_详细说明（Detailed Documentation）

<a id="a61e93ead82b56cb3f61d1337423af05d"></a>

### `charset_id`

```c
uint16_t bt_avrcp_set_browsed_player_rsp::charset_id
```

字符集 ID，类型为 `bt_avrcp_charset_t`。

<a id="a9c7989c84c89790673a0f25922a72f59"></a>

### `folder_depth`

```c
uint8_t bt_avrcp_set_browsed_player_rsp::folder_depth
```

文件夹深度（Folder Depth）。

<a id="a889cfb87961402d8a41b17292ec89b11"></a>

### `folder_names`

```c
struct bt_avrcp_folder_name bt_avrcp_set_browsed_player_rsp::folder_names[0]
```

文件夹名称数据。

<a id="a995907daaada393c045265583d0bad92"></a>

### `num_items`

```c
uint32_t bt_avrcp_set_browsed_player_rsp::num_items
```

文件夹中的条目数量。

<a id="a7d07c8595a14800385db33662b3096c5"></a>

### `status`

```c
uint8_t bt_avrcp_set_browsed_player_rsp::status
```

状态，类型为 `bt_avrcp_status_t`。

<a id="a5c0a40b5fbcd85dca0b904a106cfede9"></a>

### `uid_counter`

```c
uint16_t bt_avrcp_set_browsed_player_rsp::uid_counter
```

UID 计数器（UID Counter）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 67.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_avrcp_status_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga52368f4cc655bab75f96da80ddaaabe0)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_avrcp_charset_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga81330413af9eba049da6557b14ae082c)
- [bt_avrcp_folder_name](P030_bt_avrcp_folder_name_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P066_bt_avrcp_set_addressed_player_cmd_结构体.md) · [返回大纲](大纲.md) · [下一章](P068_bt_avrcp_set_player_app_setting_val_cmd_结构体.md)
