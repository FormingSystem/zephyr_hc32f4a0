---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-32
title: bt_avrcp_get_curr_player_app_setting_val_cmd_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__get__curr__player__app__setting__val__cmd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_bt\_avrcp\_get\_curr\_player\_app\_setting\_val\_cmd\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__get__curr__player__app__setting__val__cmd.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

获取当前播放器应用设置值（GetCurrentPlayerApplicationSettingValue）命令请求。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

获取当前播放器应用设置值（GetCurrentPlayerApplicationSettingValue）命令请求。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 32.1\_数据成员（Data Fields）

<a id="r_a76bbe05f5b05beaa4d9ae65efd8a4c5a"></a>

```c
uint8_t num_attrs
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_attrs](#a76bbe05f5b05beaa4d9ae65efd8a4c5a)。

要查询的属性数量。

<a id="r_a7676edfb915d4468660888f636eb6c4d"></a>

```c
uint8_t attr_ids []
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[attr_ids](#a7676edfb915d4468660888f636eb6c4d)。

属性 ID 数组。

## 32.2\_详细说明（Detailed Documentation）

<a id="a7676edfb915d4468660888f636eb6c4d"></a>

### `attr_ids`

```c
uint8_t bt_avrcp_get_curr_player_app_setting_val_cmd::attr_ids[]
```

属性 ID 数组。

<a id="a76bbe05f5b05beaa4d9ae65efd8a4c5a"></a>

### `num_attrs`

```c
uint8_t bt_avrcp_get_curr_player_app_setting_val_cmd::num_attrs
```

要查询的属性数量。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 32.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P031_bt_avrcp_get_caps_rsp_结构体.md) · [返回大纲](大纲.md) · [下一章](P033_bt_avrcp_get_curr_player_app_setting_val_rsp_结构体.md)
