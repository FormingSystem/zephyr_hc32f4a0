---
id: learning.zephyr-docs.network-application-model-reference.page-45
title: http_service_config_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhttp__service__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第45章\_http\_service\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhttp__service__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

HTTP服务配置（Service Configuration）。

```c
#include <zephyr/net/http/service.h>
```

<a id="details"></a>

HTTP服务配置（Service Configuration）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 45.1\_数据成员（Data Fields）

<a id="r_a7a3b7aa9e222cb816d7330c2c2be127f"></a>

```c
http_socket_create_fn socket_create
```

相关声明：[http_socket_create_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ga8b3eccd068dab84f64be2a267f7ed72c)、[socket_create](#a7a3b7aa9e222cb816d7330c2c2be127f)。

需要时为服务自定义套接字创建（Socket Creation）。

<a id="r_aa4c887036b350e7fc92799cefd0b0141"></a>

```c
enum http_version http_ver
```

相关声明：[http_version](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#gac26366c7dab24a62bd68e9e115d56db6)、[http_ver](#aa4c887036b350e7fc92799cefd0b0141)。

服务要使用的HTTP版本（Version）。

<a id="r_a4738a850d59dc1a6db82bd12174506ec"></a>

```c
struct http_service_h3_config h3
```

相关声明：[http_service_h3_config](P046_http_service_h3_config_结构体.md)、[h3](#a4738a850d59dc1a6db82bd12174506ec)。

HTTP/3专用配置（Specific Configuration）。

## 45.2\_详细说明（Detailed Documentation）

<a id="a4738a850d59dc1a6db82bd12174506ec"></a>

### `h3`

```c
struct http_service_h3_config http_service_config::h3
```

HTTP/3专用配置（Specific Configuration）。

<a id="aa4c887036b350e7fc92799cefd0b0141"></a>

### `http_ver`

```c
enum http_version http_service_config::http_ver
```

服务要使用的HTTP版本（Version）。

<a id="a7a3b7aa9e222cb816d7330c2c2be127f"></a>

### `socket_create`

```c
http_socket_create_fn http_service_config::socket_create
```

需要时为服务自定义套接字创建（Socket Creation）。

本数据类型文档由以下文件生成：

- `zephyr/net/http/service.h`

## 45.3\_原页交叉引用（Cross References）

- [zephyr/net/http/service.h](https://docs.zephyrproject.org/latest/doxygen/html/service_8h_source.html)
- [http_socket_create_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ga8b3eccd068dab84f64be2a267f7ed72c)
- [http_version](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#gac26366c7dab24a62bd68e9e115d56db6)
- [http_service_h3_config](P046_http_service_h3_config_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P044_http_response_ctx_结构体.md) · [返回大纲](大纲.md) · [下一章](P046_http_service_h3_config_结构体.md)
