---
id: learning.zephyr-docs.network-application-model-reference.page-80
title: mqtt_utf8_pair_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__utf8__pair.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第80章\_mqtt\_utf8\_pair\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__utf8__pair.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

UTF-8编码的MQTT字符串对（String Pair）的抽象。

```c
#include <zephyr/net/mqtt.h>
```

<a id="details"></a>

UTF-8编码的MQTT字符串对（String Pair）的抽象。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 80.1\_数据成员（Data Fields）

<a id="r_aedea0e9eb2526c8e0da2319017427c2f"></a>

```c
struct mqtt_utf8 name
```

相关声明：[mqtt_utf8](P079_mqtt_utf8_结构体.md)、[name](#aedea0e9eb2526c8e0da2319017427c2f)。

<a id="r_a749e0afc65c06917ca2881b51c0c6763"></a>

```c
struct mqtt_utf8 value
```

相关声明：[mqtt_utf8](P079_mqtt_utf8_结构体.md)、[value](#a749e0afc65c06917ca2881b51c0c6763)。

## 80.2\_详细说明（Detailed Documentation）

<a id="aedea0e9eb2526c8e0da2319017427c2f"></a>

### `name`

```c
struct mqtt_utf8 mqtt_utf8_pair::name
```

<a id="a749e0afc65c06917ca2881b51c0c6763"></a>

### `value`

```c
struct mqtt_utf8 mqtt_utf8_pair::value
```

本数据类型文档由以下文件生成：

- `zephyr/net/mqtt.h`

## 80.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h_source.html)
- [mqtt_utf8](P079_mqtt_utf8_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P079_mqtt_utf8_结构体.md) · [返回大纲](大纲.md) · [下一章](P081_rtp_header_结构体.md)
