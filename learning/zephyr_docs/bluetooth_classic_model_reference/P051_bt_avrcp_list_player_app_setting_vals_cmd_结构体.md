---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-51
title: bt_avrcp_list_player_app_setting_vals_cmd_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__list__player__app__setting__vals__cmd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第51章\_bt\_avrcp\_list\_player\_app\_setting\_vals\_cmd\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__list__player__app__setting__vals__cmd.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

列出播放器应用设置值（ListPlayerApplicationSettingValues）命令请求。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

列出播放器应用设置值（ListPlayerApplicationSettingValues）命令请求。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 51.1\_数据成员（Data Fields）

<a id="r_ae5dc4c95f535c3ce721c0f3d4d34fecf"></a>

```c
uint8_t attr_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[attr_id](#ae5dc4c95f535c3ce721c0f3d4d34fecf)。

要查询其取值的属性 ID。

## 51.2\_详细说明（Detailed Documentation）

<a id="ae5dc4c95f535c3ce721c0f3d4d34fecf"></a>

### `attr_id`

```c
uint8_t bt_avrcp_list_player_app_setting_vals_cmd::attr_id
```

要查询其取值的属性 ID。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 51.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P050_bt_avrcp_list_player_app_setting_attrs_rsp_结构体.md) · [返回大纲](大纲.md) · [下一章](P052_bt_avrcp_list_player_app_setting_vals_rsp_结构体.md)
