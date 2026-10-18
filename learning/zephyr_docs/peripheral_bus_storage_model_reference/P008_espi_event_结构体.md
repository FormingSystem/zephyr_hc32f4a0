---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-8
title: espi_event_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structespi__event.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_espi\_event\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structespi__event.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

增强型串行外设接口（eSPI）事件。

```c
#include <zephyr/drivers/espi.h>
```

<a id="details"></a>

eSPI 事件（Event）。表示传给应用程序回调的 eSPI 总线事件，提供所发生事件的详细信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 8.1\_数据成员（Data Fields）

<a id="r_acac75eb1d2b384aa337a5240825b635f"></a>

```c
enum espi_bus_event evt_type
```

相关声明：[espi_bus_event](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga36ac3fbf9813f78bad90f047e1eb1128)、[evt_type](#acac75eb1d2b384aa337a5240825b635f)。

发生的事件类型。

<a id="r_aea36925bd3f599c1481c9cc867795c33"></a>

```c
uint32_t evt_details
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[evt_details](#aea36925bd3f599c1481c9cc867795c33)。

事件的附加详细信息。

<a id="r_aa0491cbed5bec091721dfa14898b7277"></a>

```c
uint32_t evt_data
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[evt_data](#aa0491cbed5bec091721dfa14898b7277)。

与事件关联的数据。

## 8.2\_详细说明（Detailed Documentation）

<a id="aa0491cbed5bec091721dfa14898b7277"></a>

### `evt_data`

```c
uint32_t espi_event::evt_data
```

与事件关联的数据。

含义取决于 `evt_type`。可使用 `espi_evt_data_*` 结构体将原始事件数据作为位域（Bit field）操作。

<a id="aea36925bd3f599c1481c9cc867795c33"></a>

### `evt_details`

```c
uint32_t espi_event::evt_details
```

事件的附加详细信息。

含义取决于 `evt_type`。

<a id="acac75eb1d2b384aa337a5240825b635f"></a>

### `evt_type`

```c
enum espi_bus_event espi_event::evt_type
```

发生的事件类型。

本数据类型文档由以下文件生成：

- `zephyr/drivers/espi.h`

## 8.3\_原页交叉引用（Cross References）

- [zephyr/drivers/espi.h](https://docs.zephyrproject.org/latest/doxygen/html/espi_8h_source.html)
- [espi_bus_event](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga36ac3fbf9813f78bad90f047e1eb1128)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P007_espi_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P009_espi_evt_data_acpi_结构体.md)
