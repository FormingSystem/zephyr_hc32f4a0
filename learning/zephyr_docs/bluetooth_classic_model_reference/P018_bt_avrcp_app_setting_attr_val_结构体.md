---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-18
title: bt_avrcp_app_setting_attr_val_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__app__setting__attr__val.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_bt\_avrcp\_app\_setting\_attr\_val\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__app__setting__attr__val.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

AVRCP 属性值对（Attribute-Value Pair）。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

AVRCP 属性值对（Attribute-Value Pair）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 18.1\_数据成员（Data Fields）

<a id="r_ab6c7e9c0cf3097fff571cc93e3b2283b"></a>

```c
uint8_t attr_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[attr_id](#ab6c7e9c0cf3097fff571cc93e3b2283b)。

属性 ID。

<a id="r_a0ca2b498edfaa0199973ece7fcf304bc"></a>

```c
uint8_t value_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[value_id](#a0ca2b498edfaa0199973ece7fcf304bc)。

值 ID。

## 18.2\_详细说明（Detailed Documentation）

<a id="ab6c7e9c0cf3097fff571cc93e3b2283b"></a>

### `attr_id`

```c
uint8_t bt_avrcp_app_setting_attr_val::attr_id
```

属性 ID。

<a id="a0ca2b498edfaa0199973ece7fcf304bc"></a>

### `value_id`

```c
uint8_t bt_avrcp_app_setting_attr_val::value_id
```

值 ID。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 18.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P017_bt_avrcp_app_setting_attr_text_结构体.md) · [返回大纲](大纲.md) · [下一章](P019_bt_avrcp_app_setting_val_text_结构体.md)
