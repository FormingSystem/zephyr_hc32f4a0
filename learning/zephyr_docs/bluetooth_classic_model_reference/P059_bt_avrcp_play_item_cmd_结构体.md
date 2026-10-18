---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-59
title: bt_avrcp_play_item_cmd_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__play__item__cmd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第59章\_bt\_avrcp\_play\_item\_cmd\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__play__item__cmd.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

播放条目（PlayItem）命令请求。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

播放条目（PlayItem）命令请求。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 59.1\_数据成员（Data Fields）

<a id="r_a80ca2390bfa44bf2509161f4c6a5421a"></a>

```c
uint8_t scope
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[scope](#a80ca2390bfa44bf2509161f4c6a5421a)。

作用域（Scope），类型为 `bt_avrcp_scope_t`。

<a id="r_aebf33c2d1fa1a2574c485f777f114c0a"></a>

```c
uint8_t uid [8]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uid](#aebf33c2d1fa1a2574c485f777f114c0a)。

条目的唯一标识符（UID）。

<a id="r_ad2fa5d9e38a3ef5edc4430749ed13515"></a>

```c
uint16_t uid_counter
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uid_counter](#ad2fa5d9e38a3ef5edc4430749ed13515)。

UID 计数器（UID Counter）。

## 59.2\_详细说明（Detailed Documentation）

<a id="a80ca2390bfa44bf2509161f4c6a5421a"></a>

### `scope`

```c
uint8_t bt_avrcp_play_item_cmd::scope
```

作用域（Scope），类型为 `bt_avrcp_scope_t`。

<a id="aebf33c2d1fa1a2574c485f777f114c0a"></a>

### `uid`

```c
uint8_t bt_avrcp_play_item_cmd::uid[8]
```

条目的唯一标识符（UID）。

<a id="ad2fa5d9e38a3ef5edc4430749ed13515"></a>

### `uid_counter`

```c
uint16_t bt_avrcp_play_item_cmd::uid_counter
```

UID 计数器（UID Counter）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 59.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_avrcp_scope_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaabab9a4f37b3f9653ca95dd4b5944707)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P058_bt_avrcp_passthrough_rsp_结构体.md) · [返回大纲](大纲.md) · [下一章](P060_bt_avrcp_play_item_rsp_结构体.md)
