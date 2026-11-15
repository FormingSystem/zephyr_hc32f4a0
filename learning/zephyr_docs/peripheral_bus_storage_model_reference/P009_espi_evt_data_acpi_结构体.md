---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-9
title: espi_evt_data_acpi_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structespi__evt__data__acpi.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_espi\_evt\_data\_acpi\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structespi__evt__data__acpi.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

高级配置与电源接口（ACPI）事件的数据格式。

```c
#include <zephyr/drivers/espi.h>
```

<a id="details"></a>

ACPI 事件的数据格式（Event data format）。ACPI 事件的数据存储于 `espi_event::evt_data`，此格式允许将原始事件数据作为位域操作。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 9.1\_数据成员（Data Fields）

<a id="r_aa5d1e0b548e9be6b65daf67316df8bfe"></a>

```c
uint32_t type: 8
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[type](#aa5d1e0b548e9be6b65daf67316df8bfe)。

事件类型标识符。

<a id="r_a8fb3633a97b1af7618b391539f576c6f"></a>

```c
uint32_t data: 8
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[data](#a8fb3633a97b1af7618b391539f576c6f)。

事件数据载荷（Payload）。

<a id="r_acb291c371bb201d0ceb739fca7e22d3b"></a>

```c
uint32_t reserved: 16
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reserved](#acb291c371bb201d0ceb739fca7e22d3b)。

保留字段，供将来使用。

## 9.2\_详细说明（Detailed Documentation）

<a id="a8fb3633a97b1af7618b391539f576c6f"></a>

### `data`

```c
uint32_t espi_evt_data_acpi::data
```

事件数据载荷（Payload）。

<a id="acb291c371bb201d0ceb739fca7e22d3b"></a>

### `reserved`

```c
uint32_t espi_evt_data_acpi::reserved
```

保留字段，供将来使用。

<a id="aa5d1e0b548e9be6b65daf67316df8bfe"></a>

### `type`

```c
uint32_t espi_evt_data_acpi::type
```

事件类型标识符。

本数据类型文档由以下文件生成：

- `zephyr/drivers/espi.h`

## 9.3\_原页交叉引用（Cross References）

- [zephyr/drivers/espi.h](https://docs.zephyrproject.org/latest/doxygen/html/espi_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [espi_event::evt_data](P008_espi_event_结构体.md#aa0491cbed5bec091721dfa14898b7277)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P008_espi_event_结构体.md) · [返回大纲](大纲.md) · [下一章](P010_espi_evt_data_kbc_结构体.md)
