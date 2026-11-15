---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-45
title: mspi_event_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmspi__event.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第45章\_mspi\_event\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__event.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MSPI事件（Event）。

```c
#include <zephyr/drivers/mspi.h>
```

<a id="details"></a>

MSPI事件（Event）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 45.1\_数据成员（Data Fields）

<a id="r_a65079ed0fcdb2ca607dab070f2ed010b"></a>

```c
enum mspi_bus_event evt_type
```

相关声明：[mspi_bus_event](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga4cd05950729893e08ef0d4a12e2242d5)、[evt_type](#a65079ed0fcdb2ca607dab070f2ed010b)。

事件类型（Event Type）。

<a id="r_aeeb42b82bd219169e6f185ecdcc2129d"></a>

```c
struct mspi_event_data evt_data
```

相关声明：[mspi_event_data](P046_mspi_event_data_结构体.md)、[evt_data](#aeeb42b82bd219169e6f185ecdcc2129d)。

与事件关联的数据。

## 45.2\_详细说明（Detailed Documentation）

<a id="aeeb42b82bd219169e6f185ecdcc2129d"></a>

### `evt_data`

```c
struct mspi_event_data mspi_event::evt_data
```

与事件关联的数据。

<a id="a65079ed0fcdb2ca607dab070f2ed010b"></a>

### `evt_type`

```c
enum mspi_bus_event mspi_event::evt_type
```

事件类型（Event Type）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/mspi.h`

## 45.3\_原页交叉引用（Cross References）

- [zephyr/drivers/mspi.h](https://docs.zephyrproject.org/latest/doxygen/html/mspi_8h_source.html)
- [mspi_bus_event](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga4cd05950729893e08ef0d4a12e2242d5)
- [mspi_event_data](P046_mspi_event_data_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P044_mspi_dw_timing_cfg_结构体.md) · [返回大纲](大纲.md) · [下一章](P046_mspi_event_data_结构体.md)
