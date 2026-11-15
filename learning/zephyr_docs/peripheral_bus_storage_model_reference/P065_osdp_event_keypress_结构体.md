---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-65
title: osdp_event_keypress_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structosdp__event__keypress.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第65章\_osdp\_event\_keypress\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structosdp__event__keypress.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

开放监控设备协议（OSDP）的键盘事件（Keypad）。

```c
#include <zephyr/mgmt/osdp.h>
```

<a id="details"></a>

开放监控设备协议（OSDP）的键盘事件（Keypad）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 65.1\_数据成员（Data Fields）

<a id="r_ae6964a42e982021ef44372dca6af1166"></a>

```c
int reader_no
```

相关声明：[reader_no](#ae6964a42e982021ef44372dca6af1166)。

读卡器编号（Reader number）。

<a id="r_a41460942a34a488c78712bfba164f865"></a>

```c
int length
```

相关声明：[length](#a41460942a34a488c78712bfba164f865)。

按键数据长度，单位为字节。

<a id="r_a88ac427349340142426e69fb99242cb4"></a>

```c
uint8_t data [64]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#a88ac427349340142426e69fb99242cb4)。

包含 `length` 个字节的按键数据。

## 65.2\_详细说明（Detailed Documentation）

<a id="a88ac427349340142426e69fb99242cb4"></a>

### `data`

```c
uint8_t osdp_event_keypress::data[64]
```

包含 `length` 个字节的按键数据。

<a id="a41460942a34a488c78712bfba164f865"></a>

### `length`

```c
int osdp_event_keypress::length
```

按键数据长度，单位为字节。

<a id="ae6964a42e982021ef44372dca6af1166"></a>

### `reader_no`

```c
int osdp_event_keypress::reader_no
```

读卡器编号（Reader number）。

在连接到当前 PD 的读卡器范围内，此编号表示对应的读卡器。LibOSDP 不支持此项。

译注：原文为重复措辞“this number indicated this number”，此处结合其读卡器上下文译出。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/osdp.h`

## 65.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/osdp.h](https://docs.zephyrproject.org/latest/doxygen/html/osdp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P064_osdp_event_cardread_结构体.md) · [返回大纲](大纲.md) · [下一章](P066_peci_buf_结构体.md)
