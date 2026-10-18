---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-16
title: bt_avrcp_add_to_now_playing_cmd_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__add__to__now__playing__cmd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_bt\_avrcp\_add\_to\_now\_playing\_cmd\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__add__to__now__playing__cmd.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

添加到当前播放列表（AddToNowPlaying）命令请求。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

添加到当前播放列表（AddToNowPlaying）命令请求。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 16.1\_数据成员（Data Fields）

<a id="r_af0676fbaab14bfd3e3330c3c1ea701c5"></a>

```c
uint8_t scope
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[scope](#af0676fbaab14bfd3e3330c3c1ea701c5)。

作用域（Scope），类型为 `bt_avrcp_scope_t`。

<a id="r_ad73c5b034f7017f05ee3c491bf8bdc10"></a>

```c
uint8_t uid [8]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uid](#ad73c5b034f7017f05ee3c491bf8bdc10)。

条目的唯一标识符（UID）。

<a id="r_a0dd07ff85b7cedcc8b20dfddf3ed5d91"></a>

```c
uint16_t uid_counter
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uid_counter](#a0dd07ff85b7cedcc8b20dfddf3ed5d91)。

UID 计数器（UID Counter）。

## 16.2\_详细说明（Detailed Documentation）

<a id="af0676fbaab14bfd3e3330c3c1ea701c5"></a>

### `scope`

```c
uint8_t bt_avrcp_add_to_now_playing_cmd::scope
```

作用域（Scope），类型为 `bt_avrcp_scope_t`。

<a id="ad73c5b034f7017f05ee3c491bf8bdc10"></a>

### `uid`

```c
uint8_t bt_avrcp_add_to_now_playing_cmd::uid[8]
```

条目的唯一标识符（UID）。

<a id="a0dd07ff85b7cedcc8b20dfddf3ed5d91"></a>

### `uid_counter`

```c
uint16_t bt_avrcp_add_to_now_playing_cmd::uid_counter
```

UID 计数器（UID Counter）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 16.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_avrcp_scope_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaabab9a4f37b3f9653ca95dd4b5944707)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P015_bt_avdtp_sep_ops_结构体.md) · [返回大纲](大纲.md) · [下一章](P017_bt_avrcp_app_setting_attr_text_结构体.md)
