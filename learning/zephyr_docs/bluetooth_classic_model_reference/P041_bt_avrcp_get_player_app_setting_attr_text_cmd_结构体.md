---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-41
title: bt_avrcp_get_player_app_setting_attr_text_cmd_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__get__player__app__setting__attr__text__cmd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第41章\_bt\_avrcp\_get\_player\_app\_setting\_attr\_text\_cmd\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__get__player__app__setting__attr__text__cmd.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

获取播放器应用设置属性文本（GetPlayerApplicationSettingAttributeText）命令请求。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

获取播放器应用设置属性文本（GetPlayerApplicationSettingAttributeText）命令请求。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 41.1\_数据成员（Data Fields）

<a id="r_a7cec43cbd74ad7f916e76bb63e989eec"></a>

```c
uint8_t num_attrs
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_attrs](#a7cec43cbd74ad7f916e76bb63e989eec)。

要获取文本的属性数量。

<a id="r_a8606b94d15d9642f5319ded86ec2eb8c"></a>

```c
uint8_t attr_ids []
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[attr_ids](#a8606b94d15d9642f5319ded86ec2eb8c)。

属性 ID 数组。

## 41.2\_详细说明（Detailed Documentation）

<a id="a8606b94d15d9642f5319ded86ec2eb8c"></a>

### `attr_ids`

```c
uint8_t bt_avrcp_get_player_app_setting_attr_text_cmd::attr_ids[]
```

属性 ID 数组。

<a id="a7cec43cbd74ad7f916e76bb63e989eec"></a>

### `num_attrs`

```c
uint8_t bt_avrcp_get_player_app_setting_attr_text_cmd::num_attrs
```

要获取文本的属性数量。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 41.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P040_bt_avrcp_get_play_status_rsp_结构体.md) · [返回大纲](大纲.md) · [下一章](P042_bt_avrcp_get_player_app_setting_attr_text_rsp_结构体.md)
