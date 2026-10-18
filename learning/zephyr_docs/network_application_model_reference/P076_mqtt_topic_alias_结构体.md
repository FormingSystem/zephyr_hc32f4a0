---
id: learning.zephyr-docs.network-application-model-reference.page-76
title: mqtt_topic_alias_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__topic__alias.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第76章\_mqtt\_topic\_alias\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__topic__alias.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

别名主题（Aliased Topic）的抽象。

```c
#include <zephyr/net/mqtt.h>
```

<a id="details"></a>

别名主题（Aliased Topic）的抽象。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 76.1\_数据成员（Data Fields）

<a id="r_af056af89763a7d39f513759dd1f7e8a7"></a>

```c
uint8_t topic_buf [CONFIG_MQTT_TOPIC_ALIAS_STRING_MAX]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[topic_buf](#af056af89763a7d39f513759dd1f7e8a7)。

UTF-8编码的主题名称（Topic Name）。

<a id="r_aed7c3e3306dd3bf97073ca6b7f9c4902"></a>

```c
uint16_t topic_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[topic_size](#aed7c3e3306dd3bf97073ca6b7f9c4902)。

主题名称（Topic Name）的大小。

## 76.2\_详细说明（Detailed Documentation）

<a id="af056af89763a7d39f513759dd1f7e8a7"></a>

### `topic_buf`

```c
uint8_t mqtt_topic_alias::topic_buf[CONFIG_MQTT_TOPIC_ALIAS_STRING_MAX]
```

UTF-8编码的主题名称（Topic Name）。

<a id="aed7c3e3306dd3bf97073ca6b7f9c4902"></a>

### `topic_size`

```c
uint16_t mqtt_topic_alias::topic_size
```

主题名称（Topic Name）的大小。

本数据类型文档由以下文件生成：

- `zephyr/net/mqtt.h`

## 76.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P075_mqtt_topic_结构体.md) · [返回大纲](大纲.md) · [下一章](P077_mqtt_transport_结构体.md)
