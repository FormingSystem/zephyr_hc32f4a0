---
id: learning.zephyr-docs.api-lifecycle-capability-topic-reference.page-3
title: HTTP客户端（Client）API。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_HTTP客户端（Client）API。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

HTTP客户端（Client）API。

<a id="details"></a>

HTTP 客户端（Client）API。**引入版本（Since）：**2.1。**版本（Version）：**0.2.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

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

## 3.2\_类型定义（Typedefs）

<a id="r_gaf46ede77bdc83602c84b9342dd8d30ed"></a>

```c
typedef int(* http_payload_cb_t) (int sock, struct http_request *req, void *user_data)
```

相关声明：[http_payload_cb_t](#gaf46ede77bdc83602c84b9342dd8d30ed)、[http_request](../network_application_model_reference/P035_http_request_结构体.md)。

需要向服务器发送数据时使用的回调。

<a id="r_ga34a431c54c52b86618ca0e27ce3862b4"></a>

```c
typedef int(* http_header_cb_t) (int sock, struct http_request *req, void *user_data)
```

相关声明：[http_header_cb_t](#ga34a431c54c52b86618ca0e27ce3862b4)、[http_request](../network_application_model_reference/P035_http_request_结构体.md)。

应用程序如希望在发送 HTTP 请求时构造额外的 HTTP 首部（headers），可使用此回调。

<a id="r_ga6141c94f7da92b71713079063f3426be"></a>

```c
typedef int(* http_response_cb_t) (struct http_response *rsp, enum http_final_call final_data, void *user_data)
```

相关声明：[http_response_cb_t](#ga6141c94f7da92b71713079063f3426be)、[http_response](../network_application_model_reference/P043_http_response_结构体.md)、[http_final_call](#ga04fc31de51404e35b3dfab6261bb8e6d)。

从服务器收到数据时使用的回调。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 3.3\_枚举（Enumerations）

<a id="r_ga04fc31de51404e35b3dfab6261bb8e6d"></a>

```c
enum http_final_call { HTTP_DATA_MORE = 0 , HTTP_DATA_FINAL = 1 }
```

相关声明：[http_final_call](#ga04fc31de51404e35b3dfab6261bb8e6d)、[HTTP_DATA_MORE](#gga04fc31de51404e35b3dfab6261bb8e6da3f75fb095e40bfb4efd2c16059093359)、[HTTP_DATA_FINAL](#gga04fc31de51404e35b3dfab6261bb8e6da428633ff4a67c00c67fb5cbc23269d61)。

是否还有更多数据将要到达。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.4\_函数（Functions）

<a id="r_gaa38b6efb03f88d6959273a41b6acac81"></a>

```c
int http_client_req (int sock, struct http_request *req, int32_t timeout, void *user_data)
```

相关声明：[http_client_req](#gaa38b6efb03f88d6959273a41b6acac81)、[http_request](../network_application_model_reference/P035_http_request_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

执行一次 HTTP 请求。

## 3.5\_详细说明（Detailed Documentation）

<a id="ga34a431c54c52b86618ca0e27ce3862b4"></a>

### `http_header_cb_t`

```c
typedef int(* http_header_cb_t) (int sock, struct http_request *req, void *user_data)
```

```c
#include <zephyr/net/http/client.h>
```

应用程序如希望在发送 HTTP 请求时构造额外的 HTTP 首部（headers），可使用此回调。

此项为可选（Optional）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sock` | 连接的套接字 ID（Socket ID）。 |
| `req` | HTTP 请求信息（Request Information）。 |
| `user_data` | 在 `http_client_req()` 中指定的用户数据（User Data）。 |

**返回（Returns）**：**返回值（Returns）：**非负值表示已发送的数据量，此时 `http_client_req()` 应继续发送数据；负值表示 `http_client_req()` 应向调用者返回该错误码。

<a id="gaf46ede77bdc83602c84b9342dd8d30ed"></a>

### `http_payload_cb_t`

```c
typedef int(* http_payload_cb_t) (int sock, struct http_request *req, void *user_data)
```

```c
#include <zephyr/net/http/client.h>
```

需要向服务器发送数据时使用的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sock` | 连接的套接字 ID（Socket ID）。 |
| `req` | HTTP 请求信息（Request Information）。 |
| `user_data` | 在 `http_client_req()` 中指定的用户数据（User Data）。 |

**返回（Returns）**：**返回值（Returns）：**非负值表示已发送的数据量，此时 `http_client_req()` 应继续发送数据；负值表示 `http_client_req()` 应向调用者返回该错误码。

<a id="ga6141c94f7da92b71713079063f3426be"></a>

### `http_response_cb_t`

```c
typedef int(* http_response_cb_t) (struct http_response *rsp, enum http_final_call final_data, void *user_data)
```

```c
#include <zephyr/net/http/client.h>
```

从服务器收到数据时使用的回调。

对于一个已接收缓冲区（Received Buffer），回调可能运行多次，例如分块正文（Chunked Body）的每个块调用一次。每次调用通过 `body_frag_start` 和 `body_frag_len` 提供一个连续片段（Contiguous Fragment）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rsp` | HTTP 响应信息（Response Information）。 |
| `final_data` | 此数据缓冲区（Data Buffer）是否包含全部数据，还是仍有后续数据。 |
| `user_data` | 在 `http_client_req()` 中指定的用户数据（User Data）。 |

**返回（Returns）**：**返回值（Returns）：**`0` 表示 `http_client_req()` 应继续下载，负值表示应中止下载。

<a id="ga04fc31de51404e35b3dfab6261bb8e6d"></a>

### `http_final_call`

```c
enum http_final_call
```

```c
#include <zephyr/net/http/client.h>
```

是否还有更多数据将要到达。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HTTP_DATA_MORE` | 后续还有数据（More Data）。 |
| `HTTP_DATA_FINAL` | 数据结束（End of Data）。 |

<a id="gaa38b6efb03f88d6959273a41b6acac81"></a>

### `http_client_req()`

```c
int http_client_req ( int sock, struct http_request * req, int32_t timeout, void * user_data )
```

```c
#include <zephyr/net/http/client.h>
```

执行一次 HTTP 请求。

从 HTTP 服务器收到数据时调用回调。调用本函数之前，调用者必须已建立到服务器的连接，即必须已经成功为套接字执行 `connect()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sock` | 连接的套接字 ID（Socket ID）。 |
| `req` | HTTP 请求信息（Request Information）。 |
| `timeout` | 等待数据的最大超时时间（Timeout），单位为毫秒。超时值不能为 `0`，否则没有时间接收数据。 |
| `user_data` | 传递给回调（Callback）的用户指定数据（User-specified Data）。 |

**返回（Returns）**：**返回值（Returns）：**负值表示错误，非负值表示已发送到服务器的数据量。


## 3.6\_原页交叉引用（Cross References）

- [http_response](../network_application_model_reference/P043_http_response_结构体.md)
- [http_client_internal_data](../network_application_model_reference/P027_http_client_internal_data_结构体.md)
- [http_request](../network_application_model_reference/P035_http_request_结构体.md)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [zephyr/net/http/client.h](../api_file_management_reference/P022_zephyr__net__http__client.h_文件参考.md)
- [connect()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a90f0aa598d0f4ab4ea99ecf289a6a7fb)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga04fc31de51404e35b3dfab6261bb8e6da3f75fb095e40bfb4efd2c16059093359"></a>
<a id="gga04fc31de51404e35b3dfab6261bb8e6da428633ff4a67c00c67fb5cbc23269d61"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P002_公共广播配置文件（Public Broadcast Profile，PBP）.md) · [返回大纲](大纲.md) · [下一章](P004_ICM42686 API主题.md)
