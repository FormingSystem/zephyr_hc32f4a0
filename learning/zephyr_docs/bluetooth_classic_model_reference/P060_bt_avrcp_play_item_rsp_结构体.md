---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-60
title: bt_avrcp_play_item_rsp_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__play__item__rsp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第60章\_bt\_avrcp\_play\_item\_rsp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__play__item__rsp.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

播放条目（PlayItem）响应。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

播放条目（PlayItem）响应。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 60.1\_数据成员（Data Fields）

<a id="r_a36f361a78dbceaac63508fe75ce907b4"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a36f361a78dbceaac63508fe75ce907b4)。

状态类型 `bt_avrcp_status_t`。

## 60.2\_详细说明（Detailed Documentation）

<a id="a36f361a78dbceaac63508fe75ce907b4"></a>

### `status`

```c
uint8_t bt_avrcp_play_item_rsp::status
```

状态类型 `bt_avrcp_status_t`。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 60.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_avrcp_status_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga52368f4cc655bab75f96da80ddaaabe0)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P059_bt_avrcp_play_item_cmd_结构体.md) · [返回大纲](大纲.md) · [下一章](P061_bt_avrcp_register_notification_cmd_结构体.md)
