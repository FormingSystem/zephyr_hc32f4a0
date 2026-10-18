---
id: learning.zephyr-docs.api-file-network-device-reference.page-15
title: zephyr__net__http__server.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/http_2server_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_zephyr\_\_net\_\_http\_\_server.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/http_2server_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

HTTP服务器（Server）API。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/kernel.h>
#include <zephyr/net/http/parser.h>
#include <zephyr/net/http/hpack.h>
#include <zephyr/net/http/status.h>
#include <zephyr/net/socket.h>
#include <zephyr/sys/iterable_sections.h>
```

查看此文件的源码。

HTTP服务器（Server）API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 15.1\_数据结构（Data Structures）

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

## 15.2\_宏定义（Macros）

<a id="r_ga709ddfe3f5ae5605b3399687f8be8c47"></a>

```c
#define HTTP_SERVER_CONTENT_TYPE(_extension, _content_type)
```

相关声明：[HTTP_SERVER_CONTENT_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ga709ddfe3f5ae5605b3399687f8be8c47)。

<a id="r_gad1ee2e803d6e38d54c344180a45a25c2"></a>

```c
#define HTTP_SERVER_CONTENT_TYPE_FOREACH(_it)
```

相关声明：[HTTP_SERVER_CONTENT_TYPE_FOREACH](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gad1ee2e803d6e38d54c344180a45a25c2)。

<a id="r_gae1710786f10729930cc6c220a19e2071"></a>

```c
#define HTTP_SERVER_REGISTER_HEADER_CAPTURE(_id, _header)
```

相关声明：[HTTP_SERVER_REGISTER_HEADER_CAPTURE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gae1710786f10729930cc6c220a19e2071)。

注册服务器应捕获的 HTTP 请求头（Request Header）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 15.3\_类型定义（Typedefs）

<a id="r_gae15ea0da7140b38609492bf23ec35b4c"></a>

```c
typedef int(* http_resource_dynamic_cb_t) (struct http_client_ctx *client, enum http_transaction_status status, const struct http_request_ctx *request_ctx, struct http_response_ctx *response_ctx, void *user_data)
```

相关声明：[http_resource_dynamic_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gae15ea0da7140b38609492bf23ec35b4c)、[http_client_ctx](../network_application_model_reference/P026_http_client_ctx_结构体.md)、[http_transaction_status](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ga53f208642bc31b937ce0b330054604f6)、[http_request_ctx](../network_application_model_reference/P036_http_request_ctx_结构体.md)、[http_response_ctx](../network_application_model_reference/P044_http_response_ctx_结构体.md)。

收到数据时使用的回调（Callback）。

<a id="r_gaa51ec52c8960a37566d2ac77d624be93"></a>

```c
typedef int(* http_resource_websocket_cb_t) (int ws_socket, struct http_request_ctx *request_ctx, void *user_data)
```

相关声明：[http_resource_websocket_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gaa51ec52c8960a37566d2ac77d624be93)、[http_request_ctx](../network_application_model_reference/P036_http_request_ctx_结构体.md)。

建立 WebSocket 连接时使用的回调（Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 15.4\_枚举（Enumerations）

<a id="r_ga23d0077fb99827b25491111bd74d00af"></a>

```c
enum http_resource_type { HTTP_RESOURCE_TYPE_STATIC , HTTP_RESOURCE_TYPE_STATIC_FS , HTTP_RESOURCE_TYPE_DYNAMIC , HTTP_RESOURCE_TYPE_WEBSOCKET }
```

相关声明：[http_resource_type](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ga23d0077fb99827b25491111bd74d00af)、[HTTP_RESOURCE_TYPE_STATIC](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga23d0077fb99827b25491111bd74d00afa1170c8c886888c5c0c5dcdc6c593a248)、[HTTP_RESOURCE_TYPE_STATIC_FS](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga23d0077fb99827b25491111bd74d00afa05a9e5c3c4c1cce4894e6250220fea6e)、[HTTP_RESOURCE_TYPE_DYNAMIC](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga23d0077fb99827b25491111bd74d00afae9cdb0e1f8861de769a570399484587e)、[HTTP_RESOURCE_TYPE_WEBSOCKET](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga23d0077fb99827b25491111bd74d00afa6691e6fe43d8ffbd1ef1fd5c59661866)。

HTTP 服务器资源类型（Resource Type）。

<a id="r_gaf124b6ddd491dd6075b9c68db6686607"></a>

```c
enum http_compression { HTTP_NONE = 0 , HTTP_GZIP = 1 , HTTP_COMPRESS = 2 , HTTP_DEFLATE = 3 , HTTP_BR = 4 , HTTP_ZSTD = 5 }
```

相关声明：[http_compression](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gaf124b6ddd491dd6075b9c68db6686607)、[HTTP_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ggaf124b6ddd491dd6075b9c68db6686607a1a4a25c52411b1a87abca823223c7202)、[HTTP_GZIP](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ggaf124b6ddd491dd6075b9c68db6686607a39d987341b53034e236ecc0a48f40ae8)、[HTTP_COMPRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ggaf124b6ddd491dd6075b9c68db6686607ad7f9cc84c671c70f15bff03a2cf92c50)、[HTTP_DEFLATE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ggaf124b6ddd491dd6075b9c68db6686607aa260077f859491f95c6ccb781a492e43)、[HTTP_BR](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ggaf124b6ddd491dd6075b9c68db6686607ae0de360c2162dab5adddd76f47f55569)、[HTTP_ZSTD](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ggaf124b6ddd491dd6075b9c68db6686607a710e784f734d4a574c302dc86f587aa0)。

HTTP 压缩方式（Compressions）。

<a id="r_ga53f208642bc31b937ce0b330054604f6"></a>

```c
enum http_transaction_status { HTTP_SERVER_TRANSACTION_ABORTED = -1 , HTTP_SERVER_REQUEST_DATA_MORE = 0 , HTTP_SERVER_REQUEST_DATA_FINAL = 1 , HTTP_SERVER_TRANSACTION_COMPLETE = 2 }
```

相关声明：[http_transaction_status](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ga53f208642bc31b937ce0b330054604f6)、[HTTP_SERVER_TRANSACTION_ABORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga53f208642bc31b937ce0b330054604f6ac2fa76992c5f220ced91fa80347b6521)、[HTTP_SERVER_REQUEST_DATA_MORE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga53f208642bc31b937ce0b330054604f6ab08486d8498944dd2b90a2ff57049474)、[HTTP_SERVER_REQUEST_DATA_FINAL](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga53f208642bc31b937ce0b330054604f6ae2f616c4343f1939758bdbe5dcb38ae2)、[HTTP_SERVER_TRANSACTION_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga53f208642bc31b937ce0b330054604f6acafd3ffbcec7a27be5fc71a8a20e51eb)。

指示当前正在处理的数据片段的状态（Status）。

<a id="r_ga6c15e872ece1b9a740b6dca3974101b3"></a>

```c
enum http_header_status { HTTP_HEADER_STATUS_OK , HTTP_HEADER_STATUS_DROPPED , HTTP_HEADER_STATUS_NONE }
```

相关声明：[http_header_status](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ga6c15e872ece1b9a740b6dca3974101b3)、[HTTP_HEADER_STATUS_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga6c15e872ece1b9a740b6dca3974101b3ad4ad497a135cc5855573cc0211e7b7ec)、[HTTP_HEADER_STATUS_DROPPED](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga6c15e872ece1b9a740b6dca3974101b3a3f41dca87eecce1ac499389e72285621)、[HTTP_HEADER_STATUS_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga6c15e872ece1b9a740b6dca3974101b3ac01b170099c3ea7fafa5d22f164930ed)。

已捕获请求头（Captured Request Headers）的状态。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 15.5\_函数（Functions）

<a id="r_ga8125ef45732f81ec1c629a8f41e4c14d"></a>

```c
int http_server_start (void)
```

相关声明：[http_server_start](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ga8125ef45732f81ec1c629a8f41e4c14d)。

启动 HTTP/2 服务器（Server）。

<a id="r_ga79f434b5bbc6d2a6ebc65a0c560730cf"></a>

```c
int http_server_stop (void)
```

相关声明：[http_server_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ga79f434b5bbc6d2a6ebc65a0c560730cf)。

停止 HTTP/2 服务器（Server）。


## 15.6\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/net/http/parser.h](../api_source_http_wifi_reference/P007_parser.h_源码浏览.md)
- [zephyr/net/http/hpack.h](../api_source_supplement_reference/P087_hpack.h_源码浏览.md)
- [zephyr/net/http/status.h](../api_source_reference/P818_status.h_源码浏览.md)
- [zephyr/net/socket.h](../api_source_socket_ethernet_reference/P006_socket.h_源码浏览.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [查看此文件的源码。](../api_source_configuration_reference/P030_server.h_源码浏览.md)
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
- [HTTP_SERVER_CONTENT_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ga709ddfe3f5ae5605b3399687f8be8c47)
- [HTTP_SERVER_CONTENT_TYPE_FOREACH](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gad1ee2e803d6e38d54c344180a45a25c2)
- [HTTP_SERVER_REGISTER_HEADER_CAPTURE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gae1710786f10729930cc6c220a19e2071)
- [http_resource_dynamic_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gae15ea0da7140b38609492bf23ec35b4c)
- [http_transaction_status](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ga53f208642bc31b937ce0b330054604f6)
- [http_resource_websocket_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gaa51ec52c8960a37566d2ac77d624be93)
- [http_resource_type](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ga23d0077fb99827b25491111bd74d00af)
- [HTTP_RESOURCE_TYPE_STATIC](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga23d0077fb99827b25491111bd74d00afa1170c8c886888c5c0c5dcdc6c593a248)
- [HTTP_RESOURCE_TYPE_STATIC_FS](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga23d0077fb99827b25491111bd74d00afa05a9e5c3c4c1cce4894e6250220fea6e)
- [HTTP_RESOURCE_TYPE_DYNAMIC](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga23d0077fb99827b25491111bd74d00afae9cdb0e1f8861de769a570399484587e)
- [HTTP_RESOURCE_TYPE_WEBSOCKET](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga23d0077fb99827b25491111bd74d00afa6691e6fe43d8ffbd1ef1fd5c59661866)
- [http_compression](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gaf124b6ddd491dd6075b9c68db6686607)
- [HTTP_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ggaf124b6ddd491dd6075b9c68db6686607a1a4a25c52411b1a87abca823223c7202)
- [HTTP_GZIP](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ggaf124b6ddd491dd6075b9c68db6686607a39d987341b53034e236ecc0a48f40ae8)
- [HTTP_COMPRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ggaf124b6ddd491dd6075b9c68db6686607ad7f9cc84c671c70f15bff03a2cf92c50)
- [HTTP_DEFLATE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ggaf124b6ddd491dd6075b9c68db6686607aa260077f859491f95c6ccb781a492e43)
- [HTTP_BR](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ggaf124b6ddd491dd6075b9c68db6686607ae0de360c2162dab5adddd76f47f55569)
- [HTTP_ZSTD](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ggaf124b6ddd491dd6075b9c68db6686607a710e784f734d4a574c302dc86f587aa0)
- [HTTP_SERVER_TRANSACTION_ABORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga53f208642bc31b937ce0b330054604f6ac2fa76992c5f220ced91fa80347b6521)
- [HTTP_SERVER_REQUEST_DATA_MORE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga53f208642bc31b937ce0b330054604f6ab08486d8498944dd2b90a2ff57049474)
- [HTTP_SERVER_REQUEST_DATA_FINAL](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga53f208642bc31b937ce0b330054604f6ae2f616c4343f1939758bdbe5dcb38ae2)
- [HTTP_SERVER_TRANSACTION_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga53f208642bc31b937ce0b330054604f6acafd3ffbcec7a27be5fc71a8a20e51eb)
- [http_header_status](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ga6c15e872ece1b9a740b6dca3974101b3)
- [HTTP_HEADER_STATUS_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga6c15e872ece1b9a740b6dca3974101b3ad4ad497a135cc5855573cc0211e7b7ec)
- [HTTP_HEADER_STATUS_DROPPED](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga6c15e872ece1b9a740b6dca3974101b3a3f41dca87eecce1ac499389e72285621)
- [HTTP_HEADER_STATUS_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga6c15e872ece1b9a740b6dca3974101b3ac01b170099c3ea7fafa5d22f164930ed)
- [http_server_start](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ga8125ef45732f81ec1c629a8f41e4c14d)
- [http_server_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ga79f434b5bbc6d2a6ebc65a0c560730cf)

<a id="header-details"></a>

---

[上一章](P014_zephyr__bluetooth__hci_pkt.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P016_zephyr__drivers__sensor__icm42x70.h_文件参考.md)
