---
id: learning.zephyr-docs.api-file-management-reference.page-22
title: zephyr__net__http__client.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/http_2client_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_zephyr\_\_net\_\_http\_\_client.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/http_2client_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

HTTP客户端（Client）API。

<a id="details"></a>

```c
#include <stdbool.h>
#include <zephyr/kernel.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/http/parser.h>
```

查看此文件的源码。

HTTP 客户端 API（HTTP client API），供应用程序发送 HTTP 请求使用。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 22.1\_数据结构（Data Structures）

<a id="r_http_5Fresponse"></a>

```c
struct http_response
```

相关声明：[http_response](../network_application_model_reference/P043_http_response_结构体.md)。

服务器返回的HTTP响应（Response）。

<a id="r_http_5Fclient_5Finternal_5Fdata"></a>

```c
struct http_client_internal_data
```

相关声明：[http_client_internal_data](../network_application_model_reference/P027_http_client_internal_data_结构体.md)。

应用不应访问的HTTP客户端内部数据（Internal Data）。

<a id="r_http_5Frequest"></a>

```c
struct http_request
```

相关声明：[http_request](../network_application_model_reference/P035_http_request_结构体.md)。

HTTP客户端请求（Client Request）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 22.2\_类型定义（Typedefs）

<a id="r_gaf46ede77bdc83602c84b9342dd8d30ed"></a>

```c
typedef int(* http_payload_cb_t) (int sock, struct http_request *req, void *user_data)
```

相关声明：[http_payload_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#gaf46ede77bdc83602c84b9342dd8d30ed)、[http_request](../network_application_model_reference/P035_http_request_结构体.md)。

需要向服务器发送数据时使用的回调。

<a id="r_ga34a431c54c52b86618ca0e27ce3862b4"></a>

```c
typedef int(* http_header_cb_t) (int sock, struct http_request *req, void *user_data)
```

相关声明：[http_header_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#ga34a431c54c52b86618ca0e27ce3862b4)、[http_request](../network_application_model_reference/P035_http_request_结构体.md)。

应用程序如希望在发送 HTTP 请求时构造额外的 HTTP 首部（headers），可使用此回调。

<a id="r_ga6141c94f7da92b71713079063f3426be"></a>

```c
typedef int(* http_response_cb_t) (struct http_response *rsp, enum http_final_call final_data, void *user_data)
```

相关声明：[http_response_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#ga6141c94f7da92b71713079063f3426be)、[http_response](../network_application_model_reference/P043_http_response_结构体.md)、[http_final_call](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#ga04fc31de51404e35b3dfab6261bb8e6d)。

从服务器收到数据时使用的回调。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 22.3\_枚举（Enumerations）

<a id="r_ga04fc31de51404e35b3dfab6261bb8e6d"></a>

```c
enum http_final_call { HTTP_DATA_MORE = 0 , HTTP_DATA_FINAL = 1 }
```

相关声明：[http_final_call](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#ga04fc31de51404e35b3dfab6261bb8e6d)、[HTTP_DATA_MORE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#gga04fc31de51404e35b3dfab6261bb8e6da3f75fb095e40bfb4efd2c16059093359)、[HTTP_DATA_FINAL](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#gga04fc31de51404e35b3dfab6261bb8e6da428633ff4a67c00c67fb5cbc23269d61)。

是否还有更多数据将要到达。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 22.4\_函数（Functions）

<a id="r_gaa38b6efb03f88d6959273a41b6acac81"></a>

```c
int http_client_req (int sock, struct http_request *req, int32_t timeout, void *user_data)
```

相关声明：[http_client_req](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#gaa38b6efb03f88d6959273a41b6acac81)、[http_request](../network_application_model_reference/P035_http_request_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

执行一次 HTTP 请求。


## 22.5\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)
- [zephyr/net/http/parser.h](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h_source.html)
- [查看此文件的源码。](../api_source_supplement_reference/P088_client.h_源码浏览.md)
- [http_response](../network_application_model_reference/P043_http_response_结构体.md)
- [http_client_internal_data](../network_application_model_reference/P027_http_client_internal_data_结构体.md)
- [http_request](../network_application_model_reference/P035_http_request_结构体.md)
- [http_payload_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#gaf46ede77bdc83602c84b9342dd8d30ed)
- [http_header_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#ga34a431c54c52b86618ca0e27ce3862b4)
- [http_response_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#ga6141c94f7da92b71713079063f3426be)
- [http_final_call](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#ga04fc31de51404e35b3dfab6261bb8e6d)
- [HTTP_DATA_MORE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#gga04fc31de51404e35b3dfab6261bb8e6da3f75fb095e40bfb4efd2c16059093359)
- [HTTP_DATA_FINAL](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#gga04fc31de51404e35b3dfab6261bb8e6da428633ff4a67c00c67fb5cbc23269d61)
- [http_client_req](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#gaa38b6efb03f88d6959273a41b6acac81)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)

<a id="header-details"></a>

---

[上一章](P021_zephyr__net__hostname.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P023_zephyr__drivers__i2c__i2c_nrfx_twim.h_文件参考.md)
