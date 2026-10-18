---
id: learning.zephyr-docs.network-service-model-reference.page-65
title: ssh_transport_event_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structssh__transport__event.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第65章\_ssh\_transport\_event\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structssh__transport__event.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SSH传输事件信息（Transport Event Information）。

```c
#include <zephyr/net/ssh/common.h>
```

<a id="details"></a>

SSH传输事件信息（Transport Event Information）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 65.1\_数据成员（Data Fields）

<a id="r_afa47dba4ec00ab1a2dfb6ae6c57fe498"></a>

```c
enum ssh_transport_event_type type
```

相关声明：[ssh_transport_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga578aed0a10600bc7a248dbb64ca13cc2)、[type](#afa47dba4ec00ab1a2dfb6ae6c57fe498)。

SSH 传输层发出的事件类型。

```c
union {
```

<a id="r_a497922c0bb2cf9478da91e996fcdd629"></a>

```c
struct ssh_transport_event_authenticate_result authenticate_result
```

相关声明：[ssh_transport_event_authenticate_result](P066_ssh_transport_event_authenticate_result_结构体.md)、[authenticate_result](#abb671e903a0e2d6492719f2cff1b29fd)。

`SSH_TRANSPORT_EVENT_AUTHENTICATE_RESULT` 的数据。

<a id="r_a34290a5fd5c27959c66082b2c7da558c"></a>

```c
struct ssh_transport_event_channel_open channel_open
```

相关声明：[ssh_transport_event_channel_open](P067_ssh_transport_event_channel_open_结构体.md)、[channel_open](#a2a244666ec5be86351c7099fabc2f7b5)。

`SSH_TRANSPORT_EVENT_CHANNEL_OPEN` 的数据。

<a id="r_a5699794e058f600d9d48e1197b797c21"></a>

```c
};
```

传输事件载荷数据。

## 65.2\_详细说明（Detailed Documentation）

<a id="a5699794e058f600d9d48e1197b797c21"></a>

### `[union]`

```c
union { ... } ssh_transport_event
```

传输事件载荷数据。

<a id="abb671e903a0e2d6492719f2cff1b29fd"></a>

### `authenticate_result`

```c
struct ssh_transport_event_authenticate_result ssh_transport_event::authenticate_result
```

`SSH_TRANSPORT_EVENT_AUTHENTICATE_RESULT` 的数据。

<a id="a2a244666ec5be86351c7099fabc2f7b5"></a>

### `channel_open`

```c
struct ssh_transport_event_channel_open ssh_transport_event::channel_open
```

`SSH_TRANSPORT_EVENT_CHANNEL_OPEN` 的数据。

<a id="afa47dba4ec00ab1a2dfb6ae6c57fe498"></a>

### `type`

```c
enum ssh_transport_event_type ssh_transport_event::type
```

SSH 传输层发出的事件类型。

本数据类型文档由以下文件生成：

- `zephyr/net/ssh/common.h`

## 65.3\_原页交叉引用（Cross References）

- [zephyr/net/ssh/common.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2net_2ssh_2common_8h_source.html)
- [ssh_transport_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga578aed0a10600bc7a248dbb64ca13cc2)
- [ssh_transport_event_authenticate_result](P066_ssh_transport_event_authenticate_result_结构体.md)
- [ssh_transport_event_channel_open](P067_ssh_transport_event_channel_open_结构体.md)
- [ssh_transport_event](P065_ssh_transport_event_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P064_ssh_transport_conf_结构体.md) · [返回大纲](大纲.md) · [下一章](P066_ssh_transport_event_authenticate_result_结构体.md)
