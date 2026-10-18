---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-62
title: osdp_cmd_text_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structosdp__cmd__text.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第62章\_osdp\_cmd\_text\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structosdp__cmd__text.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于操控外设（PD）所支持任意显示单元（Display Units）的命令。

```c
#include <zephyr/mgmt/osdp.h>
```

<a id="details"></a>

用于操控外设（PD）所支持任意显示单元（Display Units）的命令。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 62.1\_数据成员（Data Fields）

<a id="r_a3fa3d0780aa98542a270f6bdb6f49737"></a>

```c
uint8_t reader
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reader](#a3fa3d0780aa98542a270f6bdb6f49737)。

读卡器编号（Reader number）。

<a id="r_a46fe3f66e01229e763a6f06bd8bdfab8"></a>

```c
uint8_t control_code
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[control_code](#a46fe3f66e01229e763a6f06bd8bdfab8)。

控制码（Control code）。

<a id="r_acde9abcb023eb77845af8ea0935e63fa"></a>

```c
uint8_t temp_time
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[temp_time](#acde9abcb023eb77845af8ea0935e63fa)。

临时文本的显示时长，单位为秒。

<a id="r_a16f11f35eacb2876b09d148349b7ed3c"></a>

```c
uint8_t offset_row
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[offset_row](#a16f11f35eacb2876b09d148349b7ed3c)。

显示首个字符的行号，从 1 开始计数。

<a id="r_a5e7b4c03b1649d8edbf53932ee90f7b3"></a>

```c
uint8_t offset_col
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[offset_col](#a5e7b4c03b1649d8edbf53932ee90f7b3)。

显示首个字符的列号，从 1 开始计数。

<a id="r_a4dcdd83d3b8d424533ca997111f5cd94"></a>

```c
uint8_t length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[length](#a4dcdd83d3b8d424533ca997111f5cd94)。

字符串中的字符数。

<a id="r_a3a94fa8b18d18845b60476148e2b7325"></a>

```c
uint8_t data [32]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#a3a94fa8b18d18845b60476148e2b7325)。

要显示的字符串。

## 62.2\_详细说明（Detailed Documentation）

<a id="a46fe3f66e01229e763a6f06bd8bdfab8"></a>

### `control_code`

```c
uint8_t osdp_cmd_text::control_code
```

控制码（Control code）。

- `1`：永久文本，不自动换行。
- `2`：永久文本，自动换行。
- `3`：临时文本，不自动换行。
- `4`：临时文本，自动换行。

<a id="a3a94fa8b18d18845b60476148e2b7325"></a>

### `data`

```c
uint8_t osdp_cmd_text::data[32]
```

要显示的字符串。

<a id="a4dcdd83d3b8d424533ca997111f5cd94"></a>

### `length`

```c
uint8_t osdp_cmd_text::length
```

字符串中的字符数。

<a id="a5e7b4c03b1649d8edbf53932ee90f7b3"></a>

### `offset_col`

```c
uint8_t osdp_cmd_text::offset_col
```

显示首个字符的列号，从 1 开始计数。

<a id="a16f11f35eacb2876b09d148349b7ed3c"></a>

### `offset_row`

```c
uint8_t osdp_cmd_text::offset_row
```

显示首个字符的行号，从 1 开始计数。

<a id="a3fa3d0780aa98542a270f6bdb6f49737"></a>

### `reader`

```c
uint8_t osdp_cmd_text::reader
```

读卡器编号（Reader number）。

`0` 表示第一个读卡器，`1` 表示第二个读卡器，依此类推。

<a id="acde9abcb023eb77845af8ea0935e63fa"></a>

### `temp_time`

```c
uint8_t osdp_cmd_text::temp_time
```

临时文本的显示时长，单位为秒。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/osdp.h`

## 62.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/osdp.h](https://docs.zephyrproject.org/latest/doxygen/html/osdp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P061_osdp_cmd_output_结构体.md) · [返回大纲](大纲.md) · [下一章](P063_osdp_event_结构体.md)
