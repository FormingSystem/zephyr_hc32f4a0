---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-52
title: bt_avrcp_list_player_app_setting_vals_rsp_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__list__player__app__setting__vals__rsp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第52章\_bt\_avrcp\_list\_player\_app\_setting\_vals\_rsp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__list__player__app__setting__vals__rsp.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

列出播放器应用设置值（ListPlayerApplicationSettingValues）响应。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

列出播放器应用设置值（ListPlayerApplicationSettingValues）响应。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 52.1\_数据成员（Data Fields）

<a id="r_acf0b62de5a89ea69da09172ca6199535"></a>

```c
uint8_t num_values
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_values](#acf0b62de5a89ea69da09172ca6199535)。

此属性的取值数量。

<a id="r_a129bdffa4fbd075371ecf6114c614ea5"></a>

```c
uint8_t values []
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[values](#a129bdffa4fbd075371ecf6114c614ea5)。

可能取值的数组。

## 52.2\_详细说明（Detailed Documentation）

<a id="acf0b62de5a89ea69da09172ca6199535"></a>

### `num_values`

```c
uint8_t bt_avrcp_list_player_app_setting_vals_rsp::num_values
```

此属性的取值数量。

<a id="a129bdffa4fbd075371ecf6114c614ea5"></a>

### `values`

```c
uint8_t bt_avrcp_list_player_app_setting_vals_rsp::values[]
```

可能取值的数组。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 52.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P051_bt_avrcp_list_player_app_setting_vals_cmd_结构体.md) · [返回大纲](大纲.md) · [下一章](P053_bt_avrcp_media_attr_结构体.md)
