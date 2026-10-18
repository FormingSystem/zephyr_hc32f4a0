---
id: learning.zephyr-docs.platform-security-model-reference.page-36
title: scmi_clock_rate_config_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structscmi__clock__rate__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第36章\_scmi\_clock\_rate\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structscmi__clock__rate__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

描述CLOCK_RATE_SET命令的参数。

```c
#include <zephyr/drivers/firmware/scmi/clk.h>
```

<a id="details"></a>

描述CLOCK_RATE_SET命令的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 36.1\_数据成员（Data Fields）

<a id="r_a784dfe157fad46cfa038be4cac21560c"></a>

```c
uint32_t flags
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[flags](#a784dfe157fad46cfa038be4cac21560c)。

频率设置标志，参见 `SCMI_CLK_RATE_SET_FLAGS_*`。

<a id="r_ab9a77f5d0213008afc023ae3406cbb81"></a>

```c
uint32_t clk_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clk_id](#ab9a77f5d0213008afc023ae3406cbb81)。

待设置频率的时钟 ID。

<a id="r_a240149068386c9da08236589186ba4d8"></a>

```c
uint32_t rate [2]
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[rate](#a240149068386c9da08236589186ba4d8)。

以 Hz 为单位的 64 位频率，拆分为 `{ 低 32 位, 高 32 位 }`。

## 36.2\_详细说明（Detailed Documentation）

<a id="ab9a77f5d0213008afc023ae3406cbb81"></a>

### `clk_id`

```c
uint32_t scmi_clock_rate_config::clk_id
```

待设置频率的时钟 ID。

<a id="a784dfe157fad46cfa038be4cac21560c"></a>

### `flags`

```c
uint32_t scmi_clock_rate_config::flags
```

频率设置标志，参见 `SCMI_CLK_RATE_SET_FLAGS_*`。

<a id="a240149068386c9da08236589186ba4d8"></a>

### `rate`

```c
uint32_t scmi_clock_rate_config::rate[2]
```

以 Hz 为单位的 64 位频率，拆分为 `{ 低 32 位, 高 32 位 }`。

本数据类型文档由以下文件生成：

- `zephyr/drivers/firmware/scmi/clk.h`

## 36.3\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/scmi/clk.h](https://docs.zephyrproject.org/latest/doxygen/html/clk_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P035_scmi_clock_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P037_scmi_message_结构体.md)
