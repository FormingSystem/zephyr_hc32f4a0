---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-24
title: lin_filter_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structlin__filter.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_lin\_filter\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structlin__filter.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

LIN帧过滤器配置（Frame Filter Configuration），仅用于响应者模式。

```c
#include <zephyr/drivers/lin.h>
```

<a id="details"></a>

LIN 帧过滤器（Frame filter）配置，仅适用于响应方模式。此结构体用于定义接收消息的 LIN 帧过滤器。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 24.1\_数据成员（Data Fields）

<a id="r_a20028b04b390f8c8dc95dbc5355fdde1"></a>

```c
uint8_t primary_pid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[primary_pid](#a20028b04b390f8c8dc95dbc5355fdde1)。

要匹配的 LIN PID。

<a id="r_a36ac597c28bcc8f66c0369be41b6868e"></a>

```c
uint8_t secondary_pid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[secondary_pid](#a36ac597c28bcc8f66c0369be41b6868e)。

第二个 PID（如有）。

<a id="r_a4b7c5a4d4aea3b15fa248957071b34a8"></a>

```c
uint8_t mask
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mask](#a4b7c5a4d4aea3b15fa248957071b34a8)。

用于 ID 匹配的 LIN 掩码（Mask）。

## 24.2\_详细说明（Detailed Documentation）

<a id="a4b7c5a4d4aea3b15fa248957071b34a8"></a>

### `mask`

```c
uint8_t lin_filter::mask
```

用于 ID 匹配的 LIN 掩码（Mask）。

<a id="a20028b04b390f8c8dc95dbc5355fdde1"></a>

### `primary_pid`

```c
uint8_t lin_filter::primary_pid
```

要匹配的 LIN PID。

<a id="a36ac597c28bcc8f66c0369be41b6868e"></a>

### `secondary_pid`

```c
uint8_t lin_filter::secondary_pid
```

第二个 PID（如有）。

未使用时设为 `0x00`。

本数据类型文档由以下文件生成：

- `zephyr/drivers/lin.h`

## 24.3\_原页交叉引用（Cross References）

- [zephyr/drivers/lin.h](https://docs.zephyrproject.org/latest/doxygen/html/lin_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P023_lin_event_结构体.md) · [返回大纲](大纲.md) · [下一章](P025_lin_msg_结构体.md)
