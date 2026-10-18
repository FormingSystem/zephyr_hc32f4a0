---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-31
title: bt_avrcp_get_caps_rsp_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__get__caps__rsp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_bt\_avrcp\_get\_caps\_rsp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__get__caps__rsp.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 31.1\_数据成员（Data Fields）

<a id="r_a587d32dcd5abe2e1751a75bcc4bbe5b2"></a>

```c
uint8_t cap_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cap_id](#a587d32dcd5abe2e1751a75bcc4bbe5b2)。

能力类型 `bt_avrcp_cap_t`。

<a id="r_a1f588c2e4204c2f43c4872ee9d6ff6b1"></a>

```c
uint8_t cap_cnt
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cap_cnt](#a1f588c2e4204c2f43c4872ee9d6ff6b1)。

`*cap` 中包含的条目数量。

<a id="r_a8a4c9b7c09cf3db137431ff788006e87"></a>

```c
uint8_t cap []
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cap](#a8a4c9b7c09cf3db137431ff788006e87)。

每个条目占 1 或 3 个八位字节，取决于 `cap_id`。

## 31.2\_详细说明（Detailed Documentation）

<a id="a8a4c9b7c09cf3db137431ff788006e87"></a>

### `cap`

```c
uint8_t bt_avrcp_get_caps_rsp::cap[]
```

每个条目占 1 或 3 个八位字节，取决于 `cap_id`。

<a id="a1f588c2e4204c2f43c4872ee9d6ff6b1"></a>

### `cap_cnt`

```c
uint8_t bt_avrcp_get_caps_rsp::cap_cnt
```

`*cap` 中包含的条目数量。

<a id="a587d32dcd5abe2e1751a75bcc4bbe5b2"></a>

### `cap_id`

```c
uint8_t bt_avrcp_get_caps_rsp::cap_id
```

能力类型 `bt_avrcp_cap_t`。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 31.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_avrcp_cap_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gac311dc7b5f99162b954271529eeb84ea)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P030_bt_avrcp_folder_name_结构体.md) · [返回大纲](大纲.md) · [下一章](P032_bt_avrcp_get_curr_player_app_setting_val_cmd_结构体.md)
