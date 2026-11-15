---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-30
title: bt_avrcp_folder_name_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__folder__name.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_bt\_avrcp\_folder\_name\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__folder__name.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

获取文件夹名称的响应（Get Folder Name Response）。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

获取文件夹名称的响应（Get Folder Name Response）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 30.1\_数据成员（Data Fields）

<a id="r_a54673f0419fa51cee9250e5f5f1487fe"></a>

```c
uint16_t folder_name_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[folder_name_len](#a54673f0419fa51cee9250e5f5f1487fe)。

<a id="r_a0c339a18965911d0c3f52af9ae49f5dc"></a>

```c
uint8_t folder_name []
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[folder_name](#a0c339a18965911d0c3f52af9ae49f5dc)。

## 30.2\_详细说明（Detailed Documentation）

<a id="a0c339a18965911d0c3f52af9ae49f5dc"></a>

### `folder_name`

```c
uint8_t bt_avrcp_folder_name::folder_name[]
```

<a id="a54673f0419fa51cee9250e5f5f1487fe"></a>

### `folder_name_len`

```c
uint16_t bt_avrcp_folder_name::folder_name_len
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 30.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P029_bt_avrcp_folder_item_结构体.md) · [返回大纲](大纲.md) · [下一章](P031_bt_avrcp_get_caps_rsp_结构体.md)
