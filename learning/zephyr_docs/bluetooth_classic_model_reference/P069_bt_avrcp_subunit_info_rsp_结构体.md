---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-69
title: bt_avrcp_subunit_info_rsp_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__subunit__info__rsp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第69章\_bt\_avrcp\_subunit\_info\_rsp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__subunit__info__rsp.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 69.1\_数据成员（Data Fields）

<a id="r_a144ad1d366436c8b2502a17833a36dc3"></a>

```c
bt_avrcp_subunit_type_t subunit_type
```

相关声明：[bt_avrcp_subunit_type_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga78ba828636b731b2c43e088a581bfee9)、[subunit_type](#a144ad1d366436c8b2502a17833a36dc3)。

<a id="r_a85cf595920ba2dbf9f0e4deca1d27483"></a>

```c
uint8_t max_subunit_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_subunit_id](#a85cf595920ba2dbf9f0e4deca1d27483)。

<a id="r_a47b69412c61682ed336737f34ac614dc"></a>

```c
const uint8_t * extended_subunit_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[extended_subunit_type](#a47b69412c61682ed336737f34ac614dc)。

包含 `max_subunit_id` 个条目。

<a id="r_a0be33096e6edf251c23a5322b3c30421"></a>

```c
const uint8_t * extended_subunit_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[extended_subunit_id](#a0be33096e6edf251c23a5322b3c30421)。

包含 `max_subunit_id` 个条目。

## 69.2\_详细说明（Detailed Documentation）

<a id="a0be33096e6edf251c23a5322b3c30421"></a>

### `extended_subunit_id`

```c
const uint8_t* bt_avrcp_subunit_info_rsp::extended_subunit_id
```

包含 `max_subunit_id` 个条目。

<a id="a47b69412c61682ed336737f34ac614dc"></a>

### `extended_subunit_type`

```c
const uint8_t* bt_avrcp_subunit_info_rsp::extended_subunit_type
```

包含 `max_subunit_id` 个条目。

<a id="a85cf595920ba2dbf9f0e4deca1d27483"></a>

### `max_subunit_id`

```c
uint8_t bt_avrcp_subunit_info_rsp::max_subunit_id
```

<a id="a144ad1d366436c8b2502a17833a36dc3"></a>

### `subunit_type`

```c
bt_avrcp_subunit_type_t bt_avrcp_subunit_info_rsp::subunit_type
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 69.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [bt_avrcp_subunit_type_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga78ba828636b731b2c43e088a581bfee9)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P068_bt_avrcp_set_player_app_setting_val_cmd_结构体.md) · [返回大纲](大纲.md) · [下一章](P070_bt_avrcp_tg_结构体.md)
