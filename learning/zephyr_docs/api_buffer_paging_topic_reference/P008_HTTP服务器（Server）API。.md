---
id: learning.zephyr-docs.api-buffer-paging-topic-reference.page-8
title: HTTP服务器（Server）API。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_HTTP服务器（Server）API。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

自 Zephyr 3.7 起提供；API 版本为 0.1.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 8.1\_数据结构（Data Structures）

<a id="r_http_5Fresource_5Fdetail"></a>

```c
struct http_resource_detail
```

相关声明：[http_resource_detail](../network_application_model_reference/P038_http_resource_detail_结构体.md)。

所有资源类型通用的服务器资源（Server Resource）表示。

<a id="r_http_5Fresource_5Fdetail_5Fstatic"></a>

```c
struct http_resource_detail_static
```

相关声明：[http_resource_detail_static](../network_application_model_reference/P040_http_resource_detail_static_结构体.md)。

静态服务器资源（Static Server Resource）的表示。

<a id="r_http_5Fresource_5Fdetail_5Fstatic_5Ffs"></a>

```c
struct http_resource_detail_static_fs
```

相关声明：[http_resource_detail_static_fs](../network_application_model_reference/P041_http_resource_detail_static_fs_结构体.md)。

静态文件系统服务器资源（Static Filesystem Server Resource）的表示。

<a id="r_http_5Fcontent_5Ftype"></a>

```c
struct http_content_type
```

相关声明：[http_content_type](../network_application_model_reference/P029_http_content_type_结构体.md)。

<a id="r_http_5Fheader"></a>

```c
struct http_header
```

相关声明：[http_header](../network_application_model_reference/P030_http_header_结构体.md)。

HTTP头部（Header）的表示。

<a id="r_http_5Frequest_5Fctx"></a>

```c
struct http_request_ctx
```

相关声明：[http_request_ctx](../network_application_model_reference/P036_http_request_ctx_结构体.md)。

HTTP请求上下文（Request Context）。

<a id="r_http_5Fresponse_5Fctx"></a>

```c
struct http_response_ctx
```

相关声明：[http_response_ctx](../network_application_model_reference/P044_http_response_ctx_结构体.md)。

HTTP响应上下文（Response Context）。

<a id="r_http_5Fresource_5Fdetail_5Fdynamic"></a>

```c
struct http_resource_detail_dynamic
```

相关声明：[http_resource_detail_dynamic](../network_application_model_reference/P039_http_resource_detail_dynamic_结构体.md)。

动态服务器资源（Dynamic Server Resource）的表示。

<a id="r_http_5Fresource_5Fdetail_5Fwebsocket"></a>

```c
struct http_resource_detail_websocket
```

相关声明：[http_resource_detail_websocket](../network_application_model_reference/P042_http_resource_detail_websocket_结构体.md)。

WebSocket服务器资源（Server Resource）的表示。

<a id="r_http_5Fclient_5Fctx"></a>

```c
struct http_client_ctx
```

相关声明：[http_client_ctx](../network_application_model_reference/P026_http_client_ctx_结构体.md)。

连接到服务器的HTTP客户端（Client）的表示。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 8.2\_宏定义（Macros）

<a id="r_ga709ddfe3f5ae5605b3399687f8be8c47"></a>

```c
#define HTTP_SERVER_CONTENT_TYPE(_extension, _content_type)
```

相关声明：[HTTP_SERVER_CONTENT_TYPE](#ga709ddfe3f5ae5605b3399687f8be8c47)。

<a id="r_gad1ee2e803d6e38d54c344180a45a25c2"></a>

```c
#define HTTP_SERVER_CONTENT_TYPE_FOREACH(_it)
```

相关声明：[HTTP_SERVER_CONTENT_TYPE_FOREACH](#gad1ee2e803d6e38d54c344180a45a25c2)。

<a id="r_gae1710786f10729930cc6c220a19e2071"></a>

```c
#define HTTP_SERVER_REGISTER_HEADER_CAPTURE(_id, _header)
```

相关声明：[HTTP_SERVER_REGISTER_HEADER_CAPTURE](#gae1710786f10729930cc6c220a19e2071)。

注册服务器应捕获的 HTTP 请求头（Request Header）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 8.3\_类型定义（Typedefs）

<a id="r_gae15ea0da7140b38609492bf23ec35b4c"></a>

```c
typedef int(* http_resource_dynamic_cb_t) (struct http_client_ctx *client, enum http_transaction_status status, const struct http_request_ctx *request_ctx, struct http_response_ctx *response_ctx, void *user_data)
```

相关声明：[http_resource_dynamic_cb_t](#gae15ea0da7140b38609492bf23ec35b4c)、[http_client_ctx](../network_application_model_reference/P026_http_client_ctx_结构体.md)、[http_transaction_status](#ga53f208642bc31b937ce0b330054604f6)、[http_request_ctx](../network_application_model_reference/P036_http_request_ctx_结构体.md)、[http_response_ctx](../network_application_model_reference/P044_http_response_ctx_结构体.md)。

收到数据时使用的回调（Callback）。

<a id="r_gaa51ec52c8960a37566d2ac77d624be93"></a>

```c
typedef int(* http_resource_websocket_cb_t) (int ws_socket, struct http_request_ctx *request_ctx, void *user_data)
```

相关声明：[http_resource_websocket_cb_t](#gaa51ec52c8960a37566d2ac77d624be93)、[http_request_ctx](../network_application_model_reference/P036_http_request_ctx_结构体.md)。

建立 WebSocket 连接时使用的回调（Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 8.4\_枚举（Enumerations）

<a id="r_ga23d0077fb99827b25491111bd74d00af"></a>

```c
enum http_resource_type { HTTP_RESOURCE_TYPE_STATIC , HTTP_RESOURCE_TYPE_STATIC_FS , HTTP_RESOURCE_TYPE_DYNAMIC , HTTP_RESOURCE_TYPE_WEBSOCKET }
```

相关声明：[http_resource_type](#ga23d0077fb99827b25491111bd74d00af)、[HTTP_RESOURCE_TYPE_STATIC](#gga23d0077fb99827b25491111bd74d00afa1170c8c886888c5c0c5dcdc6c593a248)、[HTTP_RESOURCE_TYPE_STATIC_FS](#gga23d0077fb99827b25491111bd74d00afa05a9e5c3c4c1cce4894e6250220fea6e)、[HTTP_RESOURCE_TYPE_DYNAMIC](#gga23d0077fb99827b25491111bd74d00afae9cdb0e1f8861de769a570399484587e)、[HTTP_RESOURCE_TYPE_WEBSOCKET](#gga23d0077fb99827b25491111bd74d00afa6691e6fe43d8ffbd1ef1fd5c59661866)。

HTTP 服务器资源类型（Resource Type）。

<a id="r_gaf124b6ddd491dd6075b9c68db6686607"></a>

```c
enum http_compression { HTTP_NONE = 0 , HTTP_GZIP = 1 , HTTP_COMPRESS = 2 , HTTP_DEFLATE = 3 , HTTP_BR = 4 , HTTP_ZSTD = 5 }
```

相关声明：[http_compression](#gaf124b6ddd491dd6075b9c68db6686607)、[HTTP_NONE](#ggaf124b6ddd491dd6075b9c68db6686607a1a4a25c52411b1a87abca823223c7202)、[HTTP_GZIP](#ggaf124b6ddd491dd6075b9c68db6686607a39d987341b53034e236ecc0a48f40ae8)、[HTTP_COMPRESS](#ggaf124b6ddd491dd6075b9c68db6686607ad7f9cc84c671c70f15bff03a2cf92c50)、[HTTP_DEFLATE](#ggaf124b6ddd491dd6075b9c68db6686607aa260077f859491f95c6ccb781a492e43)、[HTTP_BR](#ggaf124b6ddd491dd6075b9c68db6686607ae0de360c2162dab5adddd76f47f55569)、[HTTP_ZSTD](#ggaf124b6ddd491dd6075b9c68db6686607a710e784f734d4a574c302dc86f587aa0)。

HTTP 压缩方式（Compressions）。

<a id="r_ga53f208642bc31b937ce0b330054604f6"></a>

```c
enum http_transaction_status { HTTP_SERVER_TRANSACTION_ABORTED = -1 , HTTP_SERVER_REQUEST_DATA_MORE = 0 , HTTP_SERVER_REQUEST_DATA_FINAL = 1 , HTTP_SERVER_TRANSACTION_COMPLETE = 2 }
```

相关声明：[http_transaction_status](#ga53f208642bc31b937ce0b330054604f6)、[HTTP_SERVER_TRANSACTION_ABORTED](#gga53f208642bc31b937ce0b330054604f6ac2fa76992c5f220ced91fa80347b6521)、[HTTP_SERVER_REQUEST_DATA_MORE](#gga53f208642bc31b937ce0b330054604f6ab08486d8498944dd2b90a2ff57049474)、[HTTP_SERVER_REQUEST_DATA_FINAL](#gga53f208642bc31b937ce0b330054604f6ae2f616c4343f1939758bdbe5dcb38ae2)、[HTTP_SERVER_TRANSACTION_COMPLETE](#gga53f208642bc31b937ce0b330054604f6acafd3ffbcec7a27be5fc71a8a20e51eb)。

指示当前正在处理的数据片段的状态（Status）。

<a id="r_ga6c15e872ece1b9a740b6dca3974101b3"></a>

```c
enum http_header_status { HTTP_HEADER_STATUS_OK , HTTP_HEADER_STATUS_DROPPED , HTTP_HEADER_STATUS_NONE }
```

相关声明：[http_header_status](#ga6c15e872ece1b9a740b6dca3974101b3)、[HTTP_HEADER_STATUS_OK](#gga6c15e872ece1b9a740b6dca3974101b3ad4ad497a135cc5855573cc0211e7b7ec)、[HTTP_HEADER_STATUS_DROPPED](#gga6c15e872ece1b9a740b6dca3974101b3a3f41dca87eecce1ac499389e72285621)、[HTTP_HEADER_STATUS_NONE](#gga6c15e872ece1b9a740b6dca3974101b3ac01b170099c3ea7fafa5d22f164930ed)。

已捕获请求头（Captured Request Headers）的状态。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.5\_函数（Functions）

<a id="r_ga8125ef45732f81ec1c629a8f41e4c14d"></a>

```c
int http_server_start (void)
```

相关声明：[http_server_start](#ga8125ef45732f81ec1c629a8f41e4c14d)。

启动 HTTP/2 服务器（Server）。

<a id="r_ga79f434b5bbc6d2a6ebc65a0c560730cf"></a>

```c
int http_server_stop (void)
```

相关声明：[http_server_stop](#ga79f434b5bbc6d2a6ebc65a0c560730cf)。

停止 HTTP/2 服务器（Server）。

## 8.6\_详细说明（Detailed Documentation）

<a id="ga709ddfe3f5ae5605b3399687f8be8c47"></a>

### `HTTP_SERVER_CONTENT_TYPE`

```c
#define HTTP_SERVER_CONTENT_TYPE ( _extension, _content_type )
```

```c
#include <zephyr/net/http/server.h>
```

展开值（Value）：

```c
const STRUCT_SECTION_ITERABLE(http_content_type, _extension) = {                           \
        .extension = STRINGIFY(_extension),                                                \
        .extension_len = sizeof(STRINGIFY(_extension)) - 1,                                \
        .content_type = _content_type,                                                     \
};
```

<a id="gad1ee2e803d6e38d54c344180a45a25c2"></a>

### `HTTP_SERVER_CONTENT_TYPE_FOREACH`

```c
#define HTTP_SERVER_CONTENT_TYPE_FOREACH ( _it)
```

```c
#include <zephyr/net/http/server.h>
```

展开值（Value）：

```c
STRUCT_SECTION_FOREACH(http_content_type, _it)
```

<a id="gae1710786f10729930cc6c220a19e2071"></a>

### `HTTP_SERVER_REGISTER_HEADER_CAPTURE`

```c
#define HTTP_SERVER_REGISTER_HEADER_CAPTURE ( _id, _header )
```

```c
#include <zephyr/net/http/server.h>
```

展开值（Value）：

```c
BUILD_ASSERT(sizeof(_header) <= CONFIG_HTTP_SERVER_MAX_HEADER_LEN,                         \
             "Header is too long to be captured, try increasing "                          \
             "CONFIG_HTTP_SERVER_MAX_HEADER_LEN");                                         \
static const char *const _id##_str = _header;                                              \
static const STRUCT_SECTION_ITERABLE(http_header_name, _id) = {                            \
        .name = _id##_str,                                                                 \
}
```

注册服务器应捕获的 HTTP 请求头（Request Header）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_id` | 头部捕获实例（Header Capture Instance）的变量名 |
| `_header` | 要捕获的头字段，以字符串字面量指定 |

<a id="gae15ea0da7140b38609492bf23ec35b4c"></a>

### `http_resource_dynamic_cb_t`

```c
typedef int(* http_resource_dynamic_cb_t) (struct http_client_ctx *client, enum http_transaction_status status, const struct http_request_ctx *request_ctx, struct http_response_ctx *response_ctx, void *user_data)
```

```c
#include <zephyr/net/http/server.h>
```

收到数据时使用的回调（Callback）。

可以指定要发送给客户端的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 此客户端连接的 HTTP 上下文（Context）信息。 |
| `status` | HTTP 事务状态（Transaction Status）。HTTP_SERVER_REQUEST_DATA_MORE 和 HTTP_SERVER_REQUEST_DATA_FINAL 描述请求体交付进度；HTTP_SERVER_TRANSACTION_ABORTED 和 HTTP_SERVER_TRANSACTION_COMPLETE 是终结通知。 |
| `request_ctx` | 包含已接收 HTTP 请求数据的请求上下文结构体（Request Context）。捕获的请求头字段（启用 CONFIG_HTTP_SERVER_CAPTURE_HEADERS 时）仅在一次请求的首次回调中可用；参见 http_request_ctx。 |
| `response_ctx` | 供应用填写响应数据的响应上下文结构体（Response Context）。 |
| `user_data` | 用户指定的数据。 |

**返回（Returns）**：返回值（Returns）：0 表示成功，服务器可发送 response_ctx 中提供的任何响应数据；小于 0 表示错误，关闭连接。

<a id="gaa51ec52c8960a37566d2ac77d624be93"></a>

### `http_resource_websocket_cb_t`

```c
typedef int(* http_resource_websocket_cb_t) (int ws_socket, struct http_request_ctx *request_ctx, void *user_data)
```

```c
#include <zephyr/net/http/server.h>
```

建立 WebSocket 连接时使用的回调（Callback）。

应用须处理与连接有关的全部功能，包括读写 WebSocket 数据和关闭连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ws_socket` | 用于 WebSocket 数据的套接字（Socket）。 |
| `request_ctx` | 与 HTTP 升级请求（Upgrade Request）关联的请求上下文结构体 |
| `user_data` | 用户指定的数据。 |

**返回（Returns）**：返回值（Returns）：0 表示接受连接，HTTP 服务器库此后不再处理该套接字的数据收发，由应用负责通过所提供的套接字收发数据；小于 0 表示错误，关闭连接。

<a id="gaf124b6ddd491dd6075b9c68db6686607"></a>

### `http_compression`

```c
enum http_compression
```

```c
#include <zephyr/net/http/server.h>
```

HTTP 压缩方式（Compressions）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HTTP_NONE` | NONE（不压缩）。 |
| `HTTP_GZIP` | GZIP（GZIP 压缩）。 |
| `HTTP_COMPRESS` | COMPRESS（COMPRESS 压缩）。 |
| `HTTP_DEFLATE` | DEFLATE（DEFLATE 压缩）。 |
| `HTTP_BR` | BR（Brotli 压缩）。 |
| `HTTP_ZSTD` | ZSTD（Zstandard 压缩）。 |

<a id="ga6c15e872ece1b9a740b6dca3974101b3"></a>

### `http_header_status`

```c
enum http_header_status
```

```c
#include <zephyr/net/http/server.h>
```

已捕获请求头（Captured Request Headers）的状态。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HTTP_HEADER_STATUS_OK` | 已成功捕获所有可用头字段（Headers）。 |
| `HTTP_HEADER_STATUS_DROPPED` | 空间不足，已丢弃一个或多个头字段（Headers）。 |
| `HTTP_HEADER_STATUS_NONE` | 没有可用的头字段状态（Header Status）。 |

<a id="ga23d0077fb99827b25491111bd74d00af"></a>

### `http_resource_type`

```c
enum http_resource_type
```

```c
#include <zephyr/net/http/server.h>
```

HTTP 服务器资源类型（Resource Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HTTP_RESOURCE_TYPE_STATIC` | 静态资源（Static Resource），运行时不可修改。 |
| `HTTP_RESOURCE_TYPE_STATIC_FS` | 从文件系统提供经过 gzip 压缩的静态文件。 |
| `HTTP_RESOURCE_TYPE_DYNAMIC` | 动态资源（Dynamic Resource）；服务器通过注册的 http_resource_dynamic_cb_t 与应用交互。 |
| `HTTP_RESOURCE_TYPE_WEBSOCKET` | WebSocket 资源；升级后由应用接管 WebSocket 连接。 |

<a id="ga53f208642bc31b937ce0b330054604f6"></a>

### `http_transaction_status`

```c
enum http_transaction_status
```

```c
#include <zephyr/net/http/server.h>
```

指示当前正在处理的数据片段的状态（Status）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HTTP_SERVER_TRANSACTION_ABORTED` | 事务中止（Transaction Aborted），数据不完整。 |
| `HTTP_SERVER_REQUEST_DATA_MORE` | 事务尚未完成（Transaction Incomplete），预期还有后续数据。 |
| `HTTP_SERVER_REQUEST_DATA_FINAL` | 当前事务中的最后一个数据片段（Final Data Fragment）。 |
| `HTTP_SERVER_TRANSACTION_COMPLETE` | 事务完成（Transaction Completed），响应已全部发送。 |

<a id="ga8125ef45732f81ec1c629a8f41e4c14d"></a>

### `http_server_start()`

```c
int http_server_start ( void )
```

```c
#include <zephyr/net/http/server.h>
```

启动 HTTP/2 服务器（Server）。

服务器在后台线程（Background Thread）中运行。启动后，服务器为系统中注册的所有 HTTP 服务创建服务器套接字并接受客户端连接（参见 HTTP_SERVICE_DEFINE）。

<a id="ga79f434b5bbc6d2a6ebc65a0c560730cf"></a>

### `http_server_stop()`

```c
int http_server_stop ( void )
```

```c
#include <zephyr/net/http/server.h>
```

停止 HTTP/2 服务器（Server）。

关闭所有服务器套接字，并挂起服务器线程。


## 8.7\_原页交叉引用（Cross References）

- [http_resource_detail](../network_application_model_reference/P038_http_resource_detail_结构体.md)
- [http_resource_detail_static](../network_application_model_reference/P040_http_resource_detail_static_结构体.md)
- [http_resource_detail_static_fs](../network_application_model_reference/P041_http_resource_detail_static_fs_结构体.md)
- [http_content_type](../network_application_model_reference/P029_http_content_type_结构体.md)
- [http_header](../network_application_model_reference/P030_http_header_结构体.md)
- [http_request_ctx](../network_application_model_reference/P036_http_request_ctx_结构体.md)
- [http_response_ctx](../network_application_model_reference/P044_http_response_ctx_结构体.md)
- [http_resource_detail_dynamic](../network_application_model_reference/P039_http_resource_detail_dynamic_结构体.md)
- [http_resource_detail_websocket](../network_application_model_reference/P042_http_resource_detail_websocket_结构体.md)
- [http_client_ctx](../network_application_model_reference/P026_http_client_ctx_结构体.md)
- [zephyr/net/http/server.h](../api_file_network_device_reference/P015_zephyr__net__http__server.h_文件参考.md)
- [STRUCT_SECTION_ITERABLE](../iterable_reference/P001_可遍历段公共接口.md#ga9104f42cbe4a67a931bed7f7cc8f600f)
- [STRUCT_SECTION_FOREACH](../iterable_reference/P001_可遍历段公共接口.md#gad723296f2650c25dd278e8586bfaf0ab)
- [CONFIG_HTTP_SERVER_CAPTURE_HEADERS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HTTP_SERVER_CAPTURE_HEADERS)
- [HTTP_SERVICE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ga24ace8d5ad9ffb68e9a746c7b483b720)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="astructhttp__content__type_html"></a>
<a id="agroup__iterable__section__apis_html_gad723296f2650c25dd278e8586bfaf0ab"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggaf124b6ddd491dd6075b9c68db6686607a1a4a25c52411b1a87abca823223c7202"></a>
<a id="ggaf124b6ddd491dd6075b9c68db6686607a39d987341b53034e236ecc0a48f40ae8"></a>
<a id="ggaf124b6ddd491dd6075b9c68db6686607ad7f9cc84c671c70f15bff03a2cf92c50"></a>
<a id="ggaf124b6ddd491dd6075b9c68db6686607aa260077f859491f95c6ccb781a492e43"></a>
<a id="ggaf124b6ddd491dd6075b9c68db6686607ae0de360c2162dab5adddd76f47f55569"></a>
<a id="ggaf124b6ddd491dd6075b9c68db6686607a710e784f734d4a574c302dc86f587aa0"></a>
<a id="gga6c15e872ece1b9a740b6dca3974101b3ad4ad497a135cc5855573cc0211e7b7ec"></a>
<a id="gga6c15e872ece1b9a740b6dca3974101b3a3f41dca87eecce1ac499389e72285621"></a>
<a id="gga6c15e872ece1b9a740b6dca3974101b3ac01b170099c3ea7fafa5d22f164930ed"></a>
<a id="gga23d0077fb99827b25491111bd74d00afa1170c8c886888c5c0c5dcdc6c593a248"></a>
<a id="gga23d0077fb99827b25491111bd74d00afa05a9e5c3c4c1cce4894e6250220fea6e"></a>
<a id="gga23d0077fb99827b25491111bd74d00afae9cdb0e1f8861de769a570399484587e"></a>
<a id="gga23d0077fb99827b25491111bd74d00afa6691e6fe43d8ffbd1ef1fd5c59661866"></a>
<a id="gga53f208642bc31b937ce0b330054604f6ac2fa76992c5f220ced91fa80347b6521"></a>
<a id="gga53f208642bc31b937ce0b330054604f6ab08486d8498944dd2b90a2ff57049474"></a>
<a id="gga53f208642bc31b937ce0b330054604f6ae2f616c4343f1939758bdbe5dcb38ae2"></a>
<a id="gga53f208642bc31b937ce0b330054604f6acafd3ffbcec7a27be5fc71a8a20e51eb"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P007_IPSRSTCR 复位控制（Reset Control）.md) · [返回大纲](大纲.md) · [下一章](P009_互联网控制消息协议（ICMP）.md)
