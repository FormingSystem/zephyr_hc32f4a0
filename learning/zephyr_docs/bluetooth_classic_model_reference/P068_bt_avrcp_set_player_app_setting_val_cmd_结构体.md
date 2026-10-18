---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-68
title: bt_avrcp_set_player_app_setting_val_cmd_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__set__player__app__setting__val__cmd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第68章\_bt\_avrcp\_set\_player\_app\_setting\_val\_cmd\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__set__player__app__setting__val__cmd.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

设置播放器应用设置值（SetPlayerApplicationSettingValue）命令请求。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

设置播放器应用设置值（SetPlayerApplicationSettingValue）命令请求。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 68.1\_数据成员（Data Fields）

<a id="r_a8de91e220969f26121ea08d4e93b11ce"></a>

```c
uint8_t num_attrs
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_attrs](#a8de91e220969f26121ea08d4e93b11ce)。

要设置的属性数量。

<a id="r_a6eda2876b27b4e137ff80bf0283f96ae"></a>

```c
struct bt_avrcp_app_setting_attr_val attr_vals []
```

相关声明：[bt_avrcp_app_setting_attr_val](P018_bt_avrcp_app_setting_attr_val_结构体.md)、[attr_vals](#a6eda2876b27b4e137ff80bf0283f96ae)。

属性值对（Attribute-Value Pairs）数组。

## 68.2\_详细说明（Detailed Documentation）

<a id="a6eda2876b27b4e137ff80bf0283f96ae"></a>

### `attr_vals`

```c
struct bt_avrcp_app_setting_attr_val bt_avrcp_set_player_app_setting_val_cmd::attr_vals[]
```

属性值对（Attribute-Value Pairs）数组。

<a id="a8de91e220969f26121ea08d4e93b11ce"></a>

### `num_attrs`

```c
uint8_t bt_avrcp_set_player_app_setting_val_cmd::num_attrs
```

要设置的属性数量。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 68.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_avrcp_app_setting_attr_val](P018_bt_avrcp_app_setting_attr_val_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P067_bt_avrcp_set_browsed_player_rsp_结构体.md) · [返回大纲](大纲.md) · [下一章](P069_bt_avrcp_subunit_info_rsp_结构体.md)
