---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-45
title: bt_avrcp_get_total_number_of_items_cmd_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__get__total__number__of__items__cmd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第45章\_bt\_avrcp\_get\_total\_number\_of\_items\_cmd\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__get__total__number__of__items__cmd.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

获取条目总数（GetTotalNumberOfItems）命令请求。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

获取条目总数（GetTotalNumberOfItems）命令请求。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 45.1\_数据成员（Data Fields）

<a id="r_a1d6f1eaa83bdaf37a77bffd10f370ca7"></a>

```c
uint8_t scope
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[scope](#a1d6f1eaa83bdaf37a77bffd10f370ca7)。

作用域类型 `bt_avrcp_scope_t`。

## 45.2\_详细说明（Detailed Documentation）

<a id="a1d6f1eaa83bdaf37a77bffd10f370ca7"></a>

### `scope`

```c
uint8_t bt_avrcp_get_total_number_of_items_cmd::scope
```

作用域类型 `bt_avrcp_scope_t`。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 45.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_avrcp_scope_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaabab9a4f37b3f9653ca95dd4b5944707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P044_bt_avrcp_get_player_app_setting_val_text_rsp_结构体.md) · [返回大纲](大纲.md) · [下一章](P046_bt_avrcp_get_total_number_of_items_rsp_结构体.md)
