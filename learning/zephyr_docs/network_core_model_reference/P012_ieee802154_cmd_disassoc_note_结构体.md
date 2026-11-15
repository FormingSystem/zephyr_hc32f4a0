---
id: learning.zephyr-docs.network-core-model-reference.page-12
title: ieee802154_cmd_disassoc_note_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__cmd__disassoc__note.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_ieee802154\_cmd\_disassoc\_note\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__cmd__disassoc__note.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

解除关联通知（Disassociation Notification）命令的载荷。

```c
#include <zephyr/net/ieee802154_frame.h>
```

<a id="details"></a>

解除关联通知（Disassociation Notification）命令的载荷。见第7.5.4节。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 12.1\_数据成员（Data Fields）

<a id="r_a2353dfa2ad8eb0efa8794cb09a65ea44"></a>

```c
uint8_t reason
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reason](#a2353dfa2ad8eb0efa8794cb09a65ea44)。

解除关联原因（Disassociation Reason），见ieee802154_disassociation_reason_field。

## 12.2\_详细说明（Detailed Documentation）

<a id="a2353dfa2ad8eb0efa8794cb09a65ea44"></a>

### `reason`

```c
uint8_t ieee802154_cmd_disassoc_note::reason
```

解除关联原因（Disassociation Reason），见ieee802154_disassociation_reason_field。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_frame.h`

## 12.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_frame.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [ieee802154_disassociation_reason_field](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a2ab06c343e03a4d6e28073780eb47648)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P011_ieee802154_cmd_coord_realign_结构体.md) · [返回大纲](大纲.md) · [下一章](P013_ieee802154_command_结构体.md)
