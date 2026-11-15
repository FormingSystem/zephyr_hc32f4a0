---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-43
title: bt_avrcp_get_player_app_setting_val_text_cmd_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__get__player__app__setting__val__text__cmd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_bt\_avrcp\_get\_player\_app\_setting\_val\_text\_cmd\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__get__player__app__setting__val__text__cmd.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

获取播放器应用设置值文本（GetPlayerApplicationSettingValueText）命令请求。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

获取播放器应用设置值文本（GetPlayerApplicationSettingValueText）命令请求。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 43.1\_数据成员（Data Fields）

<a id="r_a6d71fc4760fe6a78ce030c256e1d3326"></a>

```c
uint8_t attr_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[attr_id](#a6d71fc4760fe6a78ce030c256e1d3326)。

属性 ID。

<a id="r_af4b5e65b4a22b36c42d8e545c43ebd7e"></a>

```c
uint8_t num_values
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_values](#af4b5e65b4a22b36c42d8e545c43ebd7e)。

要获取文本的值的数量。

<a id="r_acad6d1ebe3ae55fb12d29e38d6183640"></a>

```c
uint8_t value_ids []
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[value_ids](#acad6d1ebe3ae55fb12d29e38d6183640)。

值 ID 数组。

## 43.2\_详细说明（Detailed Documentation）

<a id="a6d71fc4760fe6a78ce030c256e1d3326"></a>

### `attr_id`

```c
uint8_t bt_avrcp_get_player_app_setting_val_text_cmd::attr_id
```

属性 ID。

<a id="af4b5e65b4a22b36c42d8e545c43ebd7e"></a>

### `num_values`

```c
uint8_t bt_avrcp_get_player_app_setting_val_text_cmd::num_values
```

要获取文本的值的数量。

<a id="acad6d1ebe3ae55fb12d29e38d6183640"></a>

### `value_ids`

```c
uint8_t bt_avrcp_get_player_app_setting_val_text_cmd::value_ids[]
```

值 ID 数组。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 43.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P042_bt_avrcp_get_player_app_setting_attr_text_rsp_结构体.md) · [返回大纲](大纲.md) · [下一章](P044_bt_avrcp_get_player_app_setting_val_text_rsp_结构体.md)
