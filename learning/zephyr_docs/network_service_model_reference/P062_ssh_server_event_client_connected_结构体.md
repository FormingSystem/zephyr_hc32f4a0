---
id: learning.zephyr-docs.network-service-model-reference.page-62
title: ssh_server_event_client_connected_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structssh__server__event__client__connected.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第62章\_ssh\_server\_event\_client\_connected\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structssh__server__event__client__connected.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

客户端连接（Client Connection）的传输数据。

```c
#include <zephyr/net/ssh/server.h>
```

<a id="details"></a>

客户端连接（Client Connection）的传输数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 62.1\_数据成员（Data Fields）

<a id="r_a1604bdb36cf125554c3355747c0ed2c1"></a>

```c
struct ssh_transport * transport
```

相关声明：[transport](#a1604bdb36cf125554c3355747c0ed2c1)。

与已连接客户端关联的传输对象（transport）。

## 62.2\_详细说明（Detailed Documentation）

<a id="a1604bdb36cf125554c3355747c0ed2c1"></a>

### `transport`

```c
struct ssh_transport* ssh_server_event_client_connected::transport
```

与已连接客户端关联的传输对象（transport）。

本数据类型文档由以下文件生成：

- `zephyr/net/ssh/server.h`

## 62.3\_原页交叉引用（Cross References）

- [zephyr/net/ssh/server.h](https://docs.zephyrproject.org/latest/doxygen/html/ssh_2server_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P061_ssh_server_event_结构体.md) · [返回大纲](大纲.md) · [下一章](P063_ssh_server_event_client_disconnected_结构体.md)
