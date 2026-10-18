---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-11
title: espi_evt_data_pvt_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structespi__evt__data__pvt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_espi\_evt\_data\_pvt\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structespi__evt__data__pvt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

私有通道（Private Channel，PVT）事件的数据格式。

```c
#include <zephyr/drivers/espi.h>
```

<a id="details"></a>

私有通道（Private Channel，PVT）事件的数据格式。PVT 事件的数据存储于 `espi_event::evt_data`，此格式允许将原始事件数据作为位域操作。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 11.1\_数据成员（Data Fields）

<a id="r_adf7edc5acdfb9affde2d1ff1d18cf23d"></a>

```c
uint32_t type: 8
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[type](#adf7edc5acdfb9affde2d1ff1d18cf23d)。

事件类型标识符。

<a id="r_a67a1ac452110cfdb0c9c5e0f453c5c57"></a>

```c
uint32_t data: 8
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[data](#a67a1ac452110cfdb0c9c5e0f453c5c57)。

事件数据载荷（Payload）。

<a id="r_aff82e44d2a95e985d1a672169f55e4df"></a>

```c
uint32_t reserved: 16
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reserved](#aff82e44d2a95e985d1a672169f55e4df)。

保留字段，供将来使用。

## 11.2\_详细说明（Detailed Documentation）

<a id="a67a1ac452110cfdb0c9c5e0f453c5c57"></a>

### `data`

```c
uint32_t espi_evt_data_pvt::data
```

事件数据载荷（Payload）。

<a id="aff82e44d2a95e985d1a672169f55e4df"></a>

### `reserved`

```c
uint32_t espi_evt_data_pvt::reserved
```

保留字段，供将来使用。

<a id="adf7edc5acdfb9affde2d1ff1d18cf23d"></a>

### `type`

```c
uint32_t espi_evt_data_pvt::type
```

事件类型标识符。

本数据类型文档由以下文件生成：

- `zephyr/drivers/espi.h`

## 11.3\_原页交叉引用（Cross References）

- [zephyr/drivers/espi.h](https://docs.zephyrproject.org/latest/doxygen/html/espi_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [espi_event::evt_data](P008_espi_event_结构体.md#aa0491cbed5bec091721dfa14898b7277)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P010_espi_evt_data_kbc_结构体.md) · [返回大纲](大纲.md) · [下一章](P012_espi_flash_packet_结构体.md)
