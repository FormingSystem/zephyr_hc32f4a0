---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-63
title: osdp_event_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structosdp__event.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第63章\_osdp\_event\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structosdp__event.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

开放监控设备协议（OSDP）的事件结构。

```c
#include <zephyr/mgmt/osdp.h>
```

<a id="details"></a>

开放监控设备协议（OSDP）的事件结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 63.1\_数据成员（Data Fields）

<a id="r_ae72763214c94751d359bf1887d8ea35a"></a>

```c
enum osdp_event_type type
```

相关声明：[osdp_event_type](https://docs.zephyrproject.org/latest/doxygen/html/osdp_8h.html#a81548fab575d89f66b45a5d4ac85984d)、[type](#ae72763214c94751d359bf1887d8ea35a)。

事件类型（Event Type）。

```c
union {
```

<a id="r_a52f0bdc9cb6a71f8023c8f463b2bd321"></a>

```c
struct osdp_event_keypress keypress
```

相关声明：[osdp_event_keypress](P065_osdp_event_keypress_结构体.md)、[keypress](#a35759c65fc80592e42d948059f8178d3)。

按键（Keypress）事件结构体。

<a id="r_a16b16d2c6db32921d813845a5ef1d14d"></a>

```c
struct osdp_event_cardread cardread
```

相关声明：[osdp_event_cardread](P064_osdp_event_cardread_结构体.md)、[cardread](#ae2488838c114c72ebf0286a6f5c67814)。

读卡（Card read）事件结构体。

<a id="r_a9aaea46780bc4ab60b805b46dc9f26ba"></a>

```c
};
```

事件（Event）。

## 63.2\_详细说明（Detailed Documentation）

<a id="a9aaea46780bc4ab60b805b46dc9f26ba"></a>

### `[union]`

```c
union { ... } osdp_event
```

事件（Event）。

<a id="ae2488838c114c72ebf0286a6f5c67814"></a>

### `cardread`

```c
struct osdp_event_cardread osdp_event::cardread
```

读卡（Card read）事件结构体。

<a id="a35759c65fc80592e42d948059f8178d3"></a>

### `keypress`

```c
struct osdp_event_keypress osdp_event::keypress
```

按键（Keypress）事件结构体。

<a id="ae72763214c94751d359bf1887d8ea35a"></a>

### `type`

```c
enum osdp_event_type osdp_event::type
```

事件类型（Event Type）。

用于选择联合体中的具体事件。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/osdp.h`

## 63.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/osdp.h](https://docs.zephyrproject.org/latest/doxygen/html/osdp_8h_source.html)
- [osdp_event_type](https://docs.zephyrproject.org/latest/doxygen/html/osdp_8h.html#a81548fab575d89f66b45a5d4ac85984d)
- [osdp_event_keypress](P065_osdp_event_keypress_结构体.md)
- [osdp_event_cardread](P064_osdp_event_cardread_结构体.md)
- [osdp_event](P063_osdp_event_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P062_osdp_cmd_text_结构体.md) · [返回大纲](大纲.md) · [下一章](P064_osdp_event_cardread_结构体.md)
