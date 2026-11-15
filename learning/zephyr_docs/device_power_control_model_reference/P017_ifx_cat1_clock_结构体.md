---
id: learning.zephyr-docs.device-power-control-model-reference.page-17
title: ifx_cat1_clock_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structifx__cat1__clock.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_ifx\_cat1\_clock\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structifx__cat1__clock.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CAT1时钟描述符（Clock Descriptor）。

```c
#include <zephyr/drivers/clock_control/clock_control_ifx_cat1.h>
```

<a id="details"></a>

CAT1时钟描述符（Clock Descriptor）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 17.1\_数据成员（Data Fields）

<a id="r_ae8032f282998a9d9a31c5d967f384a4e"></a>

```c
enum ifx_cat1_clock_block block
```

相关声明：[ifx_cat1_clock_block](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gab62704a8cdfda5914cfb7dfe81afa8c0)、[block](#ae8032f282998a9d9a31c5d967f384a4e)。

时钟模块类型（Clock block type）。

<a id="r_ac02e464103810c9907c16194eba88979"></a>

```c
uint8_t channel
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channel](#ac02e464103810c9907c16194eba88979)。

时钟通道编号。

<a id="r_a4361f9f52e5621aedc0b4f2e0e011896"></a>

```c
uint8_t instance
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[instance](#a4361f9f52e5621aedc0b4f2e0e011896)。

外设时钟实例编号。

<a id="r_a0e1e36ab2abe21b227f8b76d195fc627"></a>

```c
uint8_t group
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[group](#a0e1e36ab2abe21b227f8b76d195fc627)。

外设时钟组编号。

<a id="r_af59f4aff030f57cffc4a44d761f18d66"></a>

```c
bool reserved
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[reserved](#af59f4aff030f57cffc4a44d761f18d66)。

保留供将来使用。

<a id="r_a95619b170032a2b9b111d2f59602fbe7"></a>

```c
const void * funcs
```

相关声明：[funcs](#a95619b170032a2b9b111d2f59602fbe7)。

时钟专用函数。

## 17.2\_详细说明（Detailed Documentation）

<a id="ae8032f282998a9d9a31c5d967f384a4e"></a>

### `block`

```c
enum ifx_cat1_clock_block ifx_cat1_clock::block
```

时钟模块类型（Clock block type）。

<a id="ac02e464103810c9907c16194eba88979"></a>

### `channel`

```c
uint8_t ifx_cat1_clock::channel
```

时钟通道编号。

<a id="a95619b170032a2b9b111d2f59602fbe7"></a>

### `funcs`

```c
const void* ifx_cat1_clock::funcs
```

时钟专用函数。

<a id="a0e1e36ab2abe21b227f8b76d195fc627"></a>

### `group`

```c
uint8_t ifx_cat1_clock::group
```

外设时钟组编号。

<a id="a4361f9f52e5621aedc0b4f2e0e011896"></a>

### `instance`

```c
uint8_t ifx_cat1_clock::instance
```

外设时钟实例编号。

<a id="af59f4aff030f57cffc4a44d761f18d66"></a>

### `reserved`

```c
bool ifx_cat1_clock::reserved
```

保留供将来使用。

本数据类型文档由以下文件生成：

- `zephyr/drivers/clock_control/clock_control_ifx_cat1.h`

## 17.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/clock_control_ifx_cat1.h](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__ifx__cat1_8h_source.html)
- [ifx_cat1_clock_block](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gab62704a8cdfda5914cfb7dfe81afa8c0)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P016_gpio_tle9104_channel_diagnostics_结构体.md) · [返回大纲](大纲.md) · [下一章](P018_ifx_cat1_resource_inst_结构体.md)
