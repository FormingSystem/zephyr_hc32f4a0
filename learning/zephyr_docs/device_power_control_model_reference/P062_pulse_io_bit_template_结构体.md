---
id: learning.zephyr-docs.device-power-control-model-reference.page-62
title: pulse_io_bit_template_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpulse__io__bit__template.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第62章\_pulse\_io\_bit\_template\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpulse__io__bit__template.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

pulse_io_encode_bytes使用的逐位模板（Per-Bit Template）。

```c
#include <zephyr/drivers/pulse_io.h>
```

<a id="details"></a>

`pulse_io_encode_bytes` 使用的逐位模板（Per-bit template）。每个输入位展开为一对 `pulse_symbol` 条目。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 62.1\_数据成员（Data Fields）

<a id="r_ab57882bf17ca354573f2e0bab95009fc"></a>

```c
struct pulse_symbol zero [2]
```

相关声明：[pulse_symbol](P070_pulse_symbol_结构体.md)、[zero](#ab57882bf17ca354573f2e0bab95009fc)。

遇到值为零的位时输出的符号对（Symbol pair）。

<a id="r_af5cf7de078f5a298afe49a64680ee0d0"></a>

```c
struct pulse_symbol one [2]
```

相关声明：[pulse_symbol](P070_pulse_symbol_结构体.md)、[one](#af5cf7de078f5a298afe49a64680ee0d0)。

遇到值为一的位时输出的符号对。

<a id="r_a32b1f8e31bc606180dac02beee6b3c74"></a>

```c
bool msb_first
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[msb_first](#a32b1f8e31bc606180dac02beee6b3c74)。

`true`：最高有效位优先（MSB first）；`false`：最低有效位优先（LSB first）。

## 62.2\_详细说明（Detailed Documentation）

<a id="a32b1f8e31bc606180dac02beee6b3c74"></a>

### `msb_first`

```c
bool pulse_io_bit_template::msb_first
```

`true`：最高有效位优先（MSB first）；`false`：最低有效位优先（LSB first）。

<a id="af5cf7de078f5a298afe49a64680ee0d0"></a>

### `one`

```c
struct pulse_symbol pulse_io_bit_template::one[2]
```

遇到值为一的位时输出的符号对。

<a id="ab57882bf17ca354573f2e0bab95009fc"></a>

### `zero`

```c
struct pulse_symbol pulse_io_bit_template::zero[2]
```

遇到值为零的位时输出的符号对（Symbol pair）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/pulse_io.h`

## 62.3\_原页交叉引用（Cross References）

- [pulse_io_encode_bytes](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#gaca42826a8404d4e5e1eacefc5f17debf)
- [zephyr/drivers/pulse_io.h](https://docs.zephyrproject.org/latest/doxygen/html/pulse__io_8h_source.html)
- [pulse_symbol](P070_pulse_symbol_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P061_pulse_cell_结构体.md) · [返回大纲](大纲.md) · [下一章](P063_pulse_io_caps_结构体.md)
