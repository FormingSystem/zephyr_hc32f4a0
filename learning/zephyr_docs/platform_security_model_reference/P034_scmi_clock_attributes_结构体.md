---
id: learning.zephyr-docs.platform-security-model-reference.page-34
title: scmi_clock_attributes_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structscmi__clock__attributes.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_scmi\_clock\_attributes\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structscmi__clock__attributes.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

描述CLOCK_ATTRIBUTES命令的应答内容。

```c
#include <zephyr/drivers/firmware/scmi/clk.h>
```

<a id="details"></a>

描述CLOCK_ATTRIBUTES命令的应答内容。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 34.1\_数据成员（Data Fields）

<a id="r_a799a83ff8c0de3c62da2d206c471a630"></a>

```c
uint32_t attributes
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[attributes](#a799a83ff8c0de3c62da2d206c471a630)。

时钟属性（Clock attributes）。

<a id="r_ae85727aa3446b3f3b2ccc173367a9396"></a>

```c
uint8_t clock_name [16]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[clock_name](#ae85727aa3446b3f3b2ccc173367a9396)。

时钟名称。

<a id="r_ab8379494c52bc400a545ff6808dbbf97"></a>

```c
uint32_t clock_enable_delay
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clock_enable_delay](#ab8379494c52bc400a545ff6808dbbf97)。

平台引入的时钟使能延迟。

## 34.2\_详细说明（Detailed Documentation）

<a id="a799a83ff8c0de3c62da2d206c471a630"></a>

### `attributes`

```c
uint32_t scmi_clock_attributes::attributes
```

时钟属性（Clock attributes）。

<a id="ab8379494c52bc400a545ff6808dbbf97"></a>

### `clock_enable_delay`

```c
uint32_t scmi_clock_attributes::clock_enable_delay
```

平台引入的时钟使能延迟。

<a id="ae85727aa3446b3f3b2ccc173367a9396"></a>

### `clock_name`

```c
uint8_t scmi_clock_attributes::clock_name[16]
```

时钟名称。

本数据类型文档由以下文件生成：

- `zephyr/drivers/firmware/scmi/clk.h`

## 34.3\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/scmi/clk.h](https://docs.zephyrproject.org/latest/doxygen/html/clk_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P033_scmi_channel_结构体.md) · [返回大纲](大纲.md) · [下一章](P035_scmi_clock_config_结构体.md)
