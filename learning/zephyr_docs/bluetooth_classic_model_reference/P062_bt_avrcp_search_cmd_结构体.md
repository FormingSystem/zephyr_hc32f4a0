---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-62
title: bt_avrcp_search_cmd_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__search__cmd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第62章\_bt\_avrcp\_search\_cmd\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__search__cmd.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

搜索（Search）命令请求。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

搜索（Search）命令请求。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 62.1\_数据成员（Data Fields）

<a id="r_aa3b1bda62dc37d4c003ea3b3af9567da"></a>

```c
uint16_t charset_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[charset_id](#aa3b1bda62dc37d4c003ea3b3af9567da)。

`str` 的字符集 ID，类型为 `bt_avrcp_charset_t`。

<a id="r_a390c55e028e54b1c655d2dc1de35e87c"></a>

```c
uint16_t search_str_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[search_str_len](#a390c55e028e54b1c655d2dc1de35e87c)。

搜索字符串的长度。

<a id="r_a953e7210d1d0f8ff2cb86e4742a4af7a"></a>

```c
uint8_t search_str []
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[search_str](#a953e7210d1d0f8ff2cb86e4742a4af7a)。

搜索字符串的字节数据。

## 62.2\_详细说明（Detailed Documentation）

<a id="aa3b1bda62dc37d4c003ea3b3af9567da"></a>

### `charset_id`

```c
uint16_t bt_avrcp_search_cmd::charset_id
```

`str` 的字符集 ID，类型为 `bt_avrcp_charset_t`。

<a id="a953e7210d1d0f8ff2cb86e4742a4af7a"></a>

### `search_str`

```c
uint8_t bt_avrcp_search_cmd::search_str[]
```

搜索字符串的字节数据。

<a id="a390c55e028e54b1c655d2dc1de35e87c"></a>

### `search_str_len`

```c
uint16_t bt_avrcp_search_cmd::search_str_len
```

搜索字符串的长度。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 62.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_avrcp_charset_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga81330413af9eba049da6557b14ae082c)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P061_bt_avrcp_register_notification_cmd_结构体.md) · [返回大纲](大纲.md) · [下一章](P063_bt_avrcp_search_rsp_结构体.md)
