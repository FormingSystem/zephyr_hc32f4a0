---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-50
title: bt_avrcp_list_player_app_setting_attrs_rsp_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__list__player__app__setting__attrs__rsp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第50章\_bt\_avrcp\_list\_player\_app\_setting\_attrs\_rsp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__list__player__app__setting__attrs__rsp.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

列出播放器应用设置属性（ListPlayerApplicationSettingAttributes）响应。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

列出播放器应用设置属性（ListPlayerApplicationSettingAttributes）响应。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 50.1\_数据成员（Data Fields）

<a id="r_a43432a70ba4acc8e17db8d2effa3c964"></a>

```c
uint8_t num_attrs
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_attrs](#a43432a70ba4acc8e17db8d2effa3c964)。

应用设置属性数量。

<a id="r_a2e3313ae520d0d174f8b48589f54e355"></a>

```c
uint8_t attr_ids []
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[attr_ids](#a2e3313ae520d0d174f8b48589f54e355)。

属性 ID 数组，类型为 `bt_avrcp_player_attr_id_t`。

## 50.2\_详细说明（Detailed Documentation）

<a id="a2e3313ae520d0d174f8b48589f54e355"></a>

### `attr_ids`

```c
uint8_t bt_avrcp_list_player_app_setting_attrs_rsp::attr_ids[]
```

属性 ID 数组，类型为 `bt_avrcp_player_attr_id_t`。

<a id="a43432a70ba4acc8e17db8d2effa3c964"></a>

### `num_attrs`

```c
uint8_t bt_avrcp_list_player_app_setting_attrs_rsp::num_attrs
```

应用设置属性数量。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 50.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_avrcp_player_attr_id_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga8047dddc873566ee372e77c6eecd008f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P049_bt_avrcp_item_hdr_结构体.md) · [返回大纲](大纲.md) · [下一章](P051_bt_avrcp_list_player_app_setting_vals_cmd_结构体.md)
