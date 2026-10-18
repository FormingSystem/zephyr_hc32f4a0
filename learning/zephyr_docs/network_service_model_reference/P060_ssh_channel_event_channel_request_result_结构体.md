---
id: learning.zephyr-docs.network-service-model-reference.page-60
title: ssh_channel_event_channel_request_result_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structssh__channel__event__channel__request__result.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第60章\_ssh\_channel\_event\_channel\_request\_result\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structssh__channel__event__channel__request__result.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SSH_CHANNEL_EVENT_REQUEST_RESULT事件的数据。

```c
#include <zephyr/net/ssh/common.h>
```

<a id="details"></a>

SSH_CHANNEL_EVENT_REQUEST_RESULT事件的数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 60.1\_数据成员（Data Fields）

<a id="r_aa613a72ee7051b656fbfee2cb7bba465"></a>

```c
bool success
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[success](#aa613a72ee7051b656fbfee2cb7bba465)。

请求成功时为 `true`。

## 60.2\_详细说明（Detailed Documentation）

<a id="aa613a72ee7051b656fbfee2cb7bba465"></a>

### `success`

```c
bool ssh_channel_event_channel_request_result::success
```

请求成功时为 `true`。

本数据类型文档由以下文件生成：

- `zephyr/net/ssh/common.h`

## 60.3\_原页交叉引用（Cross References）

- [zephyr/net/ssh/common.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2net_2ssh_2common_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P059_ssh_channel_event_channel_request_结构体.md) · [返回大纲](大纲.md) · [下一章](P061_ssh_server_event_结构体.md)
