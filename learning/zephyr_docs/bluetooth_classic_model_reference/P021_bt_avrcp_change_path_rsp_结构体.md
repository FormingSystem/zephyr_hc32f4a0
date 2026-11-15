---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-21
title: bt_avrcp_change_path_rsp_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__change__path__rsp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_bt\_avrcp\_change\_path\_rsp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__change__path__rsp.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

更改路径（ChangePath）响应。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

更改路径（ChangePath）响应。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 21.1\_数据成员（Data Fields）

<a id="r_ae56d599dc7aade35910b894ad464611a"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#ae56d599dc7aade35910b894ad464611a)。

状态类型 `bt_avrcp_status_t`。

<a id="r_a801ddd082bbdbb824943cfd8fd417dea"></a>

```c
uint32_t num_items
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[num_items](#a801ddd082bbdbb824943cfd8fd417dea)。

新文件夹中的条目数量。

## 21.2\_详细说明（Detailed Documentation）

<a id="a801ddd082bbdbb824943cfd8fd417dea"></a>

### `num_items`

```c
uint32_t bt_avrcp_change_path_rsp::num_items
```

新文件夹中的条目数量。

<a id="ae56d599dc7aade35910b894ad464611a"></a>

### `status`

```c
uint8_t bt_avrcp_change_path_rsp::status
```

状态类型 `bt_avrcp_status_t`。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 21.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_avrcp_status_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga52368f4cc655bab75f96da80ddaaabe0)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P020_bt_avrcp_change_path_cmd_结构体.md) · [返回大纲](大纲.md) · [下一章](P022_bt_avrcp_cover_art_ct_结构体.md)
