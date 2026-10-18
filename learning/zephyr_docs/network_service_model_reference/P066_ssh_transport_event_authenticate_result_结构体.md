---
id: learning.zephyr-docs.network-service-model-reference.page-66
title: ssh_transport_event_authenticate_result_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structssh__transport__event__authenticate__result.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第66章\_ssh\_transport\_event\_authenticate\_result\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structssh__transport__event__authenticate__result.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SSH_TRANSPORT_EVENT_AUTHENTICATE_RESULT事件的数据。

```c
#include <zephyr/net/ssh/common.h>
```

<a id="details"></a>

SSH_TRANSPORT_EVENT_AUTHENTICATE_RESULT事件的数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 66.1\_数据成员（Data Fields）

<a id="r_a2cd0258828b4c18155fde2c502fff46c"></a>

```c
bool success
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[success](#a2cd0258828b4c18155fde2c502fff46c)。

身份验证成功时为 `true`。

## 66.2\_详细说明（Detailed Documentation）

<a id="a2cd0258828b4c18155fde2c502fff46c"></a>

### `success`

```c
bool ssh_transport_event_authenticate_result::success
```

身份验证成功时为 `true`。

本数据类型文档由以下文件生成：

- `zephyr/net/ssh/common.h`

## 66.3\_原页交叉引用（Cross References）

- [zephyr/net/ssh/common.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2net_2ssh_2common_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P065_ssh_transport_event_结构体.md) · [返回大纲](大纲.md) · [下一章](P067_ssh_transport_event_channel_open_结构体.md)
