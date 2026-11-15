---
id: learning.zephyr-docs.network-application-model-reference.page-46
title: http_service_h3_config_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhttp__service__h3__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第46章\_http\_service\_h3\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhttp__service__h3__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

服务的HTTP/3配置。

```c
#include <zephyr/net/http/service.h>
```

<a id="details"></a>

服务的HTTP/3配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 46.1\_数据成员（Data Fields）

<a id="r_a0be4af47f80b4734f43fbc04fd86163c"></a>

```c
enum http_h3_alt_svc_policy alt_svc_policy
```

相关声明：[http_h3_alt_svc_policy](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ga6fa1d08ae3794379a09455530114e3bd)、[alt_svc_policy](#a0be4af47f80b4734f43fbc04fd86163c)。

服务的HTTP/3 Alt-Svc通告策略（Advertisement Policy）。

<a id="r_a0ffd5ab6f7804fb4dbd8cca2da6fda0a"></a>

```c
bool enable_session_tickets
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[enable_session_tickets](#a0ffd5ab6f7804fb4dbd8cca2da6fda0a)。

在此服务的HTTP/3监听器（Listener）上启用QUIC会话票据（Session Tickets）。

<a id="r_afec0c9db1dd92540d988317a6d491075"></a>

```c
uint32_t max_early_data_size
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[max_early_data_size](#afec0c9db1dd92540d988317a6d491075)。

HTTP/3监听器的早期数据（Early Data）上限，单位为字节。

## 46.2\_详细说明（Detailed Documentation）

<a id="a0be4af47f80b4734f43fbc04fd86163c"></a>

### `alt_svc_policy`

```c
enum http_h3_alt_svc_policy http_service_h3_config::alt_svc_policy
```

服务的HTTP/3 Alt-Svc通告策略（Advertisement Policy）。

<a id="a0ffd5ab6f7804fb4dbd8cca2da6fda0a"></a>

### `enable_session_tickets`

```c
bool http_service_h3_config::enable_session_tickets
```

在此服务的HTTP/3监听器（Listener）上启用QUIC会话票据（Session Tickets）。

<a id="afec0c9db1dd92540d988317a6d491075"></a>

### `max_early_data_size`

```c
uint32_t http_service_h3_config::max_early_data_size
```

HTTP/3监听器的早期数据（Early Data）上限，单位为字节。

0会使新签发票据保持禁用零往返（0-RTT）。非零值会通告相应的早期数据额度，并隐式启用HTTP/3监听器的会话票据签发。

本数据类型文档由以下文件生成：

- `zephyr/net/http/service.h`

## 46.3\_原页交叉引用（Cross References）

- [zephyr/net/http/service.h](https://docs.zephyrproject.org/latest/doxygen/html/service_8h_source.html)
- [http_h3_alt_svc_policy](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ga6fa1d08ae3794379a09455530114e3bd)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P045_http_service_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P047_lwm2m_ctx_结构体.md)
