---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-64
title: osdp_event_cardread_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structosdp__event__cardread.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第64章\_osdp\_event\_cardread\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structosdp__event__cardread.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

开放监控设备协议（OSDP）的读卡事件（Cardread）。

```c
#include <zephyr/mgmt/osdp.h>
```

<a id="details"></a>

OSDP 读卡事件（Cardread event）。注意：`format` 设为 `OSDP_CARD_FMT_RAW_UNSPECIFIED` 或 `OSDP_CARD_FMT_RAW_WIEGAND` 时，长度以位（bit）为单位；设为 `OSDP_CARD_FMT_ASCII` 时，长度以字节（byte）为单位。因此，必须根据格式确定从 `data` 字段读取的字节数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 64.1\_数据成员（Data Fields）

<a id="r_ac6be298c814fcc933d6919a2c7fbb24c"></a>

```c
int reader_no
```

相关声明：[reader_no](#ac6be298c814fcc933d6919a2c7fbb24c)。

读卡器编号（Reader number）。

<a id="r_a7a94e50e9729468baac011dde4806f00"></a>

```c
enum osdp_event_cardread_format_e format
```

相关声明：[osdp_event_cardread_format_e](https://docs.zephyrproject.org/latest/doxygen/html/osdp_8h.html#a976512dfb1a4dc3ea9326d72a0abb5e7)、[format](#a7a94e50e9729468baac011dde4806f00)。

所读取卡片的数据格式。

<a id="r_a025b2965987644fe08581b93d1067cb1"></a>

```c
int direction
```

相关声明：[direction](#a025b2965987644fe08581b93d1067cb1)。

`data` 数组中的数据方向（Direction）。

<a id="r_a025f3a460042fda69212db1c20d40bc5"></a>

```c
int length
```

相关声明：[length](#a025f3a460042fda69212db1c20d40bc5)。

卡片数据长度，根据格式以字节或位为单位。

<a id="r_af431337d9312618312360ef723f15b98"></a>

```c
uint8_t data [64]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#af431337d9312618312360ef723f15b98)。

卡片数据，其长度根据格式按字节数或位数解释。

译注：原文的长度表述含重复的 `bits`，此处保留“单位由格式决定”的含义。

## 64.2\_详细说明（Detailed Documentation）

<a id="af431337d9312618312360ef723f15b98"></a>

### `data`

```c
uint8_t osdp_event_cardread::data[64]
```

卡片数据，其长度根据格式按字节数或位数解释。

译注：原文的长度表述含重复的 `bits`，此处保留“单位由格式决定”的含义。

<a id="a025b2965987644fe08581b93d1067cb1"></a>

### `direction`

```c
int osdp_event_cardread::direction
```

`data` 数组中的数据方向（Direction）。

- `0`：正向（Forward）。
- `1`：反向（Backward）。

<a id="a7a94e50e9729468baac011dde4806f00"></a>

### `format`

```c
enum osdp_event_cardread_format_e osdp_event_cardread::format
```

所读取卡片的数据格式。

<a id="a025f3a460042fda69212db1c20d40bc5"></a>

### `length`

```c
int osdp_event_cardread::length
```

卡片数据长度，根据格式以字节或位为单位。

<a id="ac6be298c814fcc933d6919a2c7fbb24c"></a>

### `reader_no`

```c
int osdp_event_cardread::reader_no
```

读卡器编号（Reader number）。

`0` 表示第一个读卡器，`1` 表示第二个读卡器，依此类推。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/osdp.h`

## 64.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/osdp.h](https://docs.zephyrproject.org/latest/doxygen/html/osdp_8h_source.html)
- [osdp_event_cardread_format_e](https://docs.zephyrproject.org/latest/doxygen/html/osdp_8h.html#a976512dfb1a4dc3ea9326d72a0abb5e7)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P063_osdp_event_结构体.md) · [返回大纲](大纲.md) · [下一章](P065_osdp_event_keypress_结构体.md)
