---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-63
title: bt_avrcp_search_rsp_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__search__rsp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第63章\_bt\_avrcp\_search\_rsp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__search__rsp.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

搜索（Search）响应。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

搜索（Search）响应。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 63.1\_数据成员（Data Fields）

<a id="r_abbaacf359228e5c56e8cf4147dafe258"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#abbaacf359228e5c56e8cf4147dafe258)。

状态类型 `bt_avrcp_status_t`。

<a id="r_ac1dadb58aa8852476a79799af8b8bd1e"></a>

```c
uint16_t uid_counter
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uid_counter](#ac1dadb58aa8852476a79799af8b8bd1e)。

搜索后的 UID 计数器。

<a id="r_ad58679ba2fee9137b3d8c7808b5dfcba"></a>

```c
uint32_t num_items
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[num_items](#ad58679ba2fee9137b3d8c7808b5dfcba)。

匹配的条目数量。

## 63.2\_详细说明（Detailed Documentation）

<a id="ad58679ba2fee9137b3d8c7808b5dfcba"></a>

### `num_items`

```c
uint32_t bt_avrcp_search_rsp::num_items
```

匹配的条目数量。

<a id="abbaacf359228e5c56e8cf4147dafe258"></a>

### `status`

```c
uint8_t bt_avrcp_search_rsp::status
```

状态类型 `bt_avrcp_status_t`。

<a id="ac1dadb58aa8852476a79799af8b8bd1e"></a>

### `uid_counter`

```c
uint16_t bt_avrcp_search_rsp::uid_counter
```

搜索后的 UID 计数器。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 63.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_avrcp_status_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga52368f4cc655bab75f96da80ddaaabe0)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P062_bt_avrcp_search_cmd_结构体.md) · [返回大纲](大纲.md) · [下一章](P064_bt_avrcp_set_absolute_volume_cmd_结构体.md)
