---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-35
title: bt_avrcp_get_element_attrs_rsp_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__get__element__attrs__rsp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_bt\_avrcp\_get\_element\_attrs\_rsp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__get__element__attrs__rsp.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

获取元素属性（GetElementAttributes）响应结构体。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

获取元素属性（GetElementAttributes）响应结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 35.1\_数据成员（Data Fields）

<a id="r_ae93d33489d91b07a521055032e88b171"></a>

```c
uint8_t num_attrs
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_attrs](#ae93d33489d91b07a521055032e88b171)。

响应中的属性数量。

<a id="r_a952a0a601b1dcf69abccaab92ef51eea"></a>

```c
struct bt_avrcp_media_attr attrs []
```

相关声明：[bt_avrcp_media_attr](P053_bt_avrcp_media_attr_结构体.md)、[attrs](#a952a0a601b1dcf69abccaab92ef51eea)。

媒体属性（Media Attributes）数组。

## 35.2\_详细说明（Detailed Documentation）

<a id="a952a0a601b1dcf69abccaab92ef51eea"></a>

### `attrs`

```c
struct bt_avrcp_media_attr bt_avrcp_get_element_attrs_rsp::attrs[]
```

媒体属性（Media Attributes）数组。

<a id="ae93d33489d91b07a521055032e88b171"></a>

### `num_attrs`

```c
uint8_t bt_avrcp_get_element_attrs_rsp::num_attrs
```

响应中的属性数量。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 35.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_avrcp_media_attr](P053_bt_avrcp_media_attr_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P034_bt_avrcp_get_element_attrs_cmd_结构体.md) · [返回大纲](大纲.md) · [下一章](P036_bt_avrcp_get_folder_items_cmd_结构体.md)
