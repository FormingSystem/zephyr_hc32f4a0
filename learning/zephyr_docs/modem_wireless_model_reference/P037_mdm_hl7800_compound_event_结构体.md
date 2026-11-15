---
id: learning.zephyr-docs.modem-wireless-model-reference.page-37
title: mdm_hl7800_compound_event_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmdm__hl7800__compound__event.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_mdm\_hl7800\_compound\_event\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmdm__hl7800__compound__event.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

由代码和字符串组成的事件数据（Event Data）。

```c
#include <zephyr/drivers/modem/hl7800.h>
```

<a id="details"></a>

由代码和字符串组成的事件数据。调制解调器使用枚举值和字符串报告状态值；GPS 数值则使用数值类型和字符串报告。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 37.1\_数据成员（Data Fields）

<a id="r_abf3581062c802a15f71c250c56609aaf"></a>

```c
uint8_t code
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[code](#abf3581062c802a15f71c250c56609aaf)。

与事件类型匹配的枚举值。

<a id="r_a014d5de10c32177e4dd3fb011a0793d5"></a>

```c
char * string
```

相关声明：[string](#a014d5de10c32177e4dd3fb011a0793d5)。

随数值一同报告、以空字符（NUL）结尾的字符串。

## 37.2\_详细说明（Detailed Documentation）

<a id="abf3581062c802a15f71c250c56609aaf"></a>

### `code`

```c
uint8_t mdm_hl7800_compound_event::code
```

与事件类型匹配的枚举值。

<a id="a014d5de10c32177e4dd3fb011a0793d5"></a>

### `string`

```c
char* mdm_hl7800_compound_event::string
```

随数值一同报告、以空字符（NUL）结尾的字符串。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/hl7800.h`

## 37.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/hl7800.h](https://docs.zephyrproject.org/latest/doxygen/html/hl7800_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P036_mdm_hl7800_callback_agent_结构体.md) · [返回大纲](大纲.md) · [下一章](P038_mdm_hl7800_polte_location_data_结构体.md)
