---
id: learning.zephyr-docs.network-application-model-reference.page-79
title: mqtt_utf8_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__utf8.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第79章\_mqtt\_utf8\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__utf8.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

UTF-8编码字符串（Strings）的抽象。

```c
#include <zephyr/net/mqtt.h>
```

<a id="details"></a>

UTF-8编码字符串（Strings）的抽象。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 79.1\_数据成员（Data Fields）

<a id="r_a69a949e3c9cb1794f8d28091601eba16"></a>

```c
const uint8_t * utf8
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[utf8](#a69a949e3c9cb1794f8d28091601eba16)。

指向UTF-8字符串（String）的指针。

<a id="r_a2376f943335326dae74c798141326b70"></a>

```c
uint32_t size
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[size](#a2376f943335326dae74c798141326b70)。

UTF字符串（String）的大小，单位为字节。

## 79.2\_详细说明（Detailed Documentation）

<a id="a2376f943335326dae74c798141326b70"></a>

### `size`

```c
uint32_t mqtt_utf8::size
```

UTF字符串（String）的大小，单位为字节。

<a id="a69a949e3c9cb1794f8d28091601eba16"></a>

### `utf8`

```c
const uint8_t* mqtt_utf8::utf8
```

指向UTF-8字符串（String）的指针。

本数据类型文档由以下文件生成：

- `zephyr/net/mqtt.h`

## 79.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P078_mqtt_unsuback_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P080_mqtt_utf8_pair_结构体.md)
