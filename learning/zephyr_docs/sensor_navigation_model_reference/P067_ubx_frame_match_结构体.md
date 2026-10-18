---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-67
title: ubx_frame_match_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structubx__frame__match.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第67章\_ubx\_frame\_match\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structubx__frame__match.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/modem/ubx/protocol.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 67.1\_数据成员（Data Fields）

<a id="r_a40d79aebd93db1349820a7f6bef9c53e"></a>

```c
uint8_t class
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[class](#a40d79aebd93db1349820a7f6bef9c53e)。

<a id="r_ae65eaf921576c61ad758bfedc56d89c6"></a>

```c
uint8_t id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[id](#ae65eaf921576c61ad758bfedc56d89c6)。

```c
struct {
```

<a id="r_a63d9df4c009e0d8399049c09fd83c6da"></a>

```c
uint8_t * buf
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[buf](#af78f70c27f4334fd1dcaac72d9e4ece6)。

<a id="r_a5d118beb624874595130a5c03cdab2bb"></a>

```c
uint16_t len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[len](#a36c5fd74bd6d506111b1ef2ac39cb68a)。

<a id="r_abbc954596995ca2dfe65de3e310e02a0"></a>

```c
} payload
```

相关声明：[payload](#abbc954596995ca2dfe65de3e310e02a0)。

## 67.2\_详细说明（Detailed Documentation）

<a id="af78f70c27f4334fd1dcaac72d9e4ece6"></a>

### `buf`

```c
uint8_t* ubx_frame_match::buf
```

<a id="a40d79aebd93db1349820a7f6bef9c53e"></a>

### `class`

```c
uint8_t ubx_frame_match::class
```

<a id="ae65eaf921576c61ad758bfedc56d89c6"></a>

### `id`

```c
uint8_t ubx_frame_match::id
```

<a id="a36c5fd74bd6d506111b1ef2ac39cb68a"></a>

### `len`

```c
uint16_t ubx_frame_match::len
```

<a id="abbc954596995ca2dfe65de3e310e02a0"></a>

### `[struct]`

```c
struct { ... } ubx_frame_match::payload
```

本数据类型文档由以下文件生成：

- `zephyr/modem/ubx/protocol.h`

## 67.3\_原页交叉引用（Cross References）

- [zephyr/modem/ubx/protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2protocol_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P066_ubx_frame_结构体.md) · [返回大纲](大纲.md) · [下一章](P068_ubx_mon_gnss_结构体.md)
