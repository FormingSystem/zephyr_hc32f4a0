---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-44
title: bt_avrcp_get_player_app_setting_val_text_rsp_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__get__player__app__setting__val__text__rsp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第44章\_bt\_avrcp\_get\_player\_app\_setting\_val\_text\_rsp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__get__player__app__setting__val__text__rsp.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

获取播放器应用设置值文本（GetPlayerApplicationSettingValueText）响应。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

获取播放器应用设置值文本（GetPlayerApplicationSettingValueText）响应。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 44.1\_数据成员（Data Fields）

<a id="r_a45368c39caa9b87ff8101de5801807c3"></a>

```c
uint8_t num_values
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_values](#a45368c39caa9b87ff8101de5801807c3)。

返回的值的数量。

<a id="r_a49b1ebb7ebce5ccc9f7d5e77f79f107c"></a>

```c
struct bt_avrcp_app_setting_val_text value_text []
```

相关声明：[bt_avrcp_app_setting_val_text](P019_bt_avrcp_app_setting_val_text_结构体.md)、[value_text](#a49b1ebb7ebce5ccc9f7d5e77f79f107c)。

## 44.2\_详细说明（Detailed Documentation）

<a id="a45368c39caa9b87ff8101de5801807c3"></a>

### `num_values`

```c
uint8_t bt_avrcp_get_player_app_setting_val_text_rsp::num_values
```

返回的值的数量。

<a id="a49b1ebb7ebce5ccc9f7d5e77f79f107c"></a>

### `value_text`

```c
struct bt_avrcp_app_setting_val_text bt_avrcp_get_player_app_setting_val_text_rsp::value_text[]
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 44.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_avrcp_app_setting_val_text](P019_bt_avrcp_app_setting_val_text_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P043_bt_avrcp_get_player_app_setting_val_text_cmd_结构体.md) · [返回大纲](大纲.md) · [下一章](P045_bt_avrcp_get_total_number_of_items_cmd_结构体.md)
