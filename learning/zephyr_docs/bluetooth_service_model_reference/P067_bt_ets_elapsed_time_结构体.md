---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-67
title: bt_ets_elapsed_time_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__ets__elapsed__time.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第67章\_bt\_ets\_elapsed\_time\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__ets__elapsed__time.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

GATT 规范补充文档（GATT Specification Supplement）第 3.82 节定义的经过时间（Elapsed Time）数据结构。

```c
#include <zephyr/bluetooth/services/ets.h>
```

<a id="details"></a>

GATT 规范补充文档（GATT Specification Supplement）第 3.82 节定义的经过时间（Elapsed Time）数据结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 67.1\_数据成员（Data Fields）

<a id="r_a026b22dc6d130c32ab80357bcb51f83f"></a>

```c
uint8_t flags
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flags](#a026b22dc6d130c32ab80357bcb51f83f)。

标志字段（Flags field）。

<a id="r_a60181194e382ea490ddcc1118bc463f7"></a>

```c
uint8_t time_value [6]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[time_value](#a60181194e382ea490ddcc1118bc463f7)。

实际时间值（Time value），分辨率由标志（Flags）定义。

<a id="r_af2ec700659c1db49ae66f8ed31f20c90"></a>

```c
uint8_t time_sync_src
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[time_sync_src](#af2ec700659c1db49ae66f8ed31f20c90)。

时间同步源类型（Time synchronization source type）。

<a id="r_a0e5ba7c5d8aafff23a01f7b0d5f4c075"></a>

```c
int8_t tz_dst_offset
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[tz_dst_offset](#a0e5ba7c5d8aafff23a01f7b0d5f4c075)。

相对于协调世界时（UTC）的时区与夏令时合并偏移量（Combined Time Zone Daylight Saving Time offset），以 15 分钟为单位，带符号。

## 67.2\_详细说明（Detailed Documentation）

<a id="a026b22dc6d130c32ab80357bcb51f83f"></a>

### `flags`

```c
uint8_t bt_ets_elapsed_time::flags
```

标志字段（Flags field）。

**参阅（See Also）**：另见（See also）：`BT_ETS_FLAGS`。

<a id="af2ec700659c1db49ae66f8ed31f20c90"></a>

### `time_sync_src`

```c
uint8_t bt_ets_elapsed_time::time_sync_src
```

时间同步源类型（Time synchronization source type）。

**参阅（See Also）**：另见（See also）：`BT_ETS_TIME_SOURCE`。

<a id="a60181194e382ea490ddcc1118bc463f7"></a>

### `time_value`

```c
uint8_t bt_ets_elapsed_time::time_value[6]
```

实际时间值（Time value），分辨率由标志（Flags）定义。

时间值字段（Time Value）保存一个计数器，统计的时间单位由时钟时间分辨率（Time resolution）决定。报告一天中的时间（Time of day）时，时间轴起点为 `2000-01-01 00:00:00`；用于节拍计数器（Tick counter）时，起点由具体实现决定。

<a id="a0e5ba7c5d8aafff23a01f7b0d5f4c075"></a>

### `tz_dst_offset`

```c
int8_t bt_ets_elapsed_time::tz_dst_offset
```

相对于协调世界时（UTC）的时区与夏令时合并偏移量（Combined Time Zone Daylight Saving Time offset），以 15 分钟为单位，带符号。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/services/ets.h`

## 67.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/services/ets.h](https://docs.zephyrproject.org/latest/doxygen/html/ets_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [BT_ETS_FLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#BT_ETS_FLAGS)
- [BT_ETS_TIME_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#BT_ETS_TIME_SOURCE)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P066_bt_ets_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P068_bt_gmap_cb_结构体.md)
