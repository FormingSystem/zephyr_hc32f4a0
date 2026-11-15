---
id: learning.zephyr-docs.network-service-model-reference.page-59
title: ssh_channel_event_channel_request_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structssh__channel__event__channel__request.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第59章\_ssh\_channel\_event\_channel\_request\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structssh__channel__event__channel__request.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SSH_CHANNEL_EVENT_REQUEST事件的数据。

```c
#include <zephyr/net/ssh/common.h>
```

<a id="details"></a>

SSH_CHANNEL_EVENT_REQUEST事件的数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 59.1\_数据成员（Data Fields）

<a id="r_a36caf063cc61ad622c74d9a7d3c8053c"></a>

```c
enum ssh_channel_request_type type
```

相关声明：[ssh_channel_request_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga9341ecffa2ca568ed8312b7c7bd5b416)、[type](#a36caf063cc61ad622c74d9a7d3c8053c)。

所请求的通道操作。

<a id="r_a34c82071311d8c41cbecd387bece4620"></a>

```c
bool want_reply
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[want_reply](#a34c82071311d8c41cbecd387bece4620)。

对端期望回复时为 `true`。

## 59.2\_详细说明（Detailed Documentation）

<a id="a36caf063cc61ad622c74d9a7d3c8053c"></a>

### `type`

```c
enum ssh_channel_request_type ssh_channel_event_channel_request::type
```

所请求的通道操作。

<a id="a34c82071311d8c41cbecd387bece4620"></a>

### `want_reply`

```c
bool ssh_channel_event_channel_request::want_reply
```

对端期望回复时为 `true`。

本数据类型文档由以下文件生成：

- `zephyr/net/ssh/common.h`

## 59.3\_原页交叉引用（Cross References）

- [zephyr/net/ssh/common.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2net_2ssh_2common_8h_source.html)
- [ssh_channel_request_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga9341ecffa2ca568ed8312b7c7bd5b416)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P058_ssh_channel_event_结构体.md) · [返回大纲](大纲.md) · [下一章](P060_ssh_channel_event_channel_request_result_结构体.md)
