---
id: learning.zephyr-docs.network-service-model-reference.page-67
title: ssh_transport_event_channel_open_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structssh__transport__event__channel__open.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第67章\_ssh\_transport\_event\_channel\_open\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structssh__transport__event__channel__open.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SSH_TRANSPORT_EVENT_CHANNEL_OPEN事件的数据。

```c
#include <zephyr/net/ssh/common.h>
```

<a id="details"></a>

SSH_TRANSPORT_EVENT_CHANNEL_OPEN事件的数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 67.1\_数据成员（Data Fields）

<a id="r_aa996fe128fd859c73e4125311e7f436c"></a>

```c
struct ssh_channel * channel
```

相关声明：[channel](#aa996fe128fd859c73e4125311e7f436c)。

新打开的通道。

## 67.2\_详细说明（Detailed Documentation）

<a id="aa996fe128fd859c73e4125311e7f436c"></a>

### `channel`

```c
struct ssh_channel* ssh_transport_event_channel_open::channel
```

新打开的通道。

本数据类型文档由以下文件生成：

- `zephyr/net/ssh/common.h`

## 67.3\_原页交叉引用（Cross References）

- [zephyr/net/ssh/common.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2net_2ssh_2common_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P066_ssh_transport_event_authenticate_result_结构体.md) · [返回大纲](大纲.md) · [下一章](P068_virtual_interface_api_结构体.md)
