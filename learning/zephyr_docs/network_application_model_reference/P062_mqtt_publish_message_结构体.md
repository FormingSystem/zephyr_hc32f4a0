---
id: learning.zephyr-docs.network-application-model-reference.page-62
title: mqtt_publish_message_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__publish__message.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第62章\_mqtt\_publish\_message\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__publish__message.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

发布消息（Publish Message）的参数。

```c
#include <zephyr/net/mqtt.h>
```

<a id="details"></a>

发布消息（Publish Message）的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 62.1\_数据成员（Data Fields）

<a id="r_acf5dba605db61efe68ec29337eea95e9"></a>

```c
struct mqtt_topic topic
```

相关声明：[mqtt_topic](P075_mqtt_topic_结构体.md)、[topic](#acf5dba605db61efe68ec29337eea95e9)。

数据发布到的主题（Topic）。

<a id="r_a6cfed92c8f8fb319d3cbf40b956cb94d"></a>

```c
struct mqtt_binstr payload
```

相关声明：[mqtt_binstr](P053_mqtt_binstr_结构体.md)、[payload](#a6cfed92c8f8fb319d3cbf40b956cb94d)。

在发布主题上的载荷（Payload）。

## 62.2\_详细说明（Detailed Documentation）

<a id="a6cfed92c8f8fb319d3cbf40b956cb94d"></a>

### `payload`

```c
struct mqtt_binstr mqtt_publish_message::payload
```

在发布主题上的载荷（Payload）。

<a id="acf5dba605db61efe68ec29337eea95e9"></a>

### `topic`

```c
struct mqtt_topic mqtt_publish_message::topic
```

数据发布到的主题（Topic）。

本数据类型文档由以下文件生成：

- `zephyr/net/mqtt.h`

## 62.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h_source.html)
- [mqtt_topic](P075_mqtt_topic_结构体.md)
- [mqtt_binstr](P053_mqtt_binstr_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P061_mqtt_pubcomp_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P063_mqtt_publish_param_结构体.md)
