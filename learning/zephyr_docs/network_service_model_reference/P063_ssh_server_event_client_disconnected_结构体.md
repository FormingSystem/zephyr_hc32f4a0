---
id: learning.zephyr-docs.network-service-model-reference.page-63
title: ssh_server_event_client_disconnected_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structssh__server__event__client__disconnected.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第63章\_ssh\_server\_event\_client\_disconnected\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structssh__server__event__client__disconnected.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

客户端断开连接（Client Disconnection）的传输数据。

```c
#include <zephyr/net/ssh/server.h>
```

<a id="details"></a>

客户端断开连接（Client Disconnection）的传输数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 63.1\_数据成员（Data Fields）

<a id="r_af11ad585b8a21b1932612bc9c0f16d6d"></a>

```c
struct ssh_transport * transport
```

相关声明：[transport](#af11ad585b8a21b1932612bc9c0f16d6d)。

与已断开客户端关联的传输对象。

## 63.2\_详细说明（Detailed Documentation）

<a id="af11ad585b8a21b1932612bc9c0f16d6d"></a>

### `transport`

```c
struct ssh_transport* ssh_server_event_client_disconnected::transport
```

与已断开客户端关联的传输对象。

本数据类型文档由以下文件生成：

- `zephyr/net/ssh/server.h`

## 63.3\_原页交叉引用（Cross References）

- [zephyr/net/ssh/server.h](https://docs.zephyrproject.org/latest/doxygen/html/ssh_2server_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P062_ssh_server_event_client_connected_结构体.md) · [返回大纲](大纲.md) · [下一章](P064_ssh_transport_conf_结构体.md)
