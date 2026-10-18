---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-33
title: bt_avrcp_get_curr_player_app_setting_val_rsp_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__get__curr__player__app__setting__val__rsp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_bt\_avrcp\_get\_curr\_player\_app\_setting\_val\_rsp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__get__curr__player__app__setting__val__rsp.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

获取当前播放器应用设置值（GetCurrentPlayerApplicationSettingValue）响应。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

获取当前播放器应用设置值（GetCurrentPlayerApplicationSettingValue）响应。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 33.1\_数据成员（Data Fields）

<a id="r_a1b289cd52db9fa5c34b69f6d68b3312d"></a>

```c
uint8_t num_attrs
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_attrs](#a1b289cd52db9fa5c34b69f6d68b3312d)。

返回的属性数量。

<a id="r_a6b978fe837d5e082729dd5df013d48a6"></a>

```c
struct bt_avrcp_app_setting_attr_val attr_vals []
```

相关声明：[bt_avrcp_app_setting_attr_val](P018_bt_avrcp_app_setting_attr_val_结构体.md)、[attr_vals](#a6b978fe837d5e082729dd5df013d48a6)。

属性值对（Attribute-Value Pairs）数组。

## 33.2\_详细说明（Detailed Documentation）

<a id="a6b978fe837d5e082729dd5df013d48a6"></a>

### `attr_vals`

```c
struct bt_avrcp_app_setting_attr_val bt_avrcp_get_curr_player_app_setting_val_rsp::attr_vals[]
```

属性值对（Attribute-Value Pairs）数组。

<a id="a1b289cd52db9fa5c34b69f6d68b3312d"></a>

### `num_attrs`

```c
uint8_t bt_avrcp_get_curr_player_app_setting_val_rsp::num_attrs
```

返回的属性数量。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 33.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_avrcp_app_setting_attr_val](P018_bt_avrcp_app_setting_attr_val_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P032_bt_avrcp_get_curr_player_app_setting_val_cmd_结构体.md) · [返回大纲](大纲.md) · [下一章](P034_bt_avrcp_get_element_attrs_cmd_结构体.md)
