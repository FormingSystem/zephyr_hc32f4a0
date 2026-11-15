---
id: learning.zephyr-docs.network-application-model-reference.page-35
title: http_request_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhttp__request.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_http\_request\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhttp__request.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

HTTP客户端请求（Client Request）。

```c
#include <zephyr/net/http/client.h>
```

<a id="details"></a>

HTTP客户端请求（Client Request），包含执行HTTP请求所需的全部数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 35.1\_数据成员（Data Fields）

<a id="r_abb86ccd0e0801c278ef37a78a4b7a958"></a>

```c
struct http_client_internal_data internal
```

相关声明：[http_client_internal_data](P027_http_client_internal_data_结构体.md)、[internal](#abb86ccd0e0801c278ef37a78a4b7a958)。

HTTP客户端请求（Client Request）的内部数据。

<a id="r_adbfcd3bcaf57205360bad957a13999e6"></a>

```c
enum http_method method
```

相关声明：[http_method](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#gaacd5f203e33ac338ca5cb8f02a3ff3b8)、[method](#adbfcd3bcaf57205360bad957a13999e6)。

HTTP方法（Method）：GET、HEAD、OPTIONS、POST等。

<a id="r_aba8bf528f3e279d55662eedc9168d25c"></a>

```c
http_response_cb_t response
```

相关声明：[http_response_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#ga6141c94f7da92b71713079063f3426be)、[response](#aba8bf528f3e279d55662eedc9168d25c)。

用户提供的回调函数（Callback Function），在收到响应时调用。

<a id="r_afbe0c199a4a58029bf2d83a0b463639c"></a>

```c
const struct http_parser_settings * http_cb
```

相关声明：[http_parser_settings](P033_http_parser_settings_结构体.md)、[http_cb](#afbe0c199a4a58029bf2d83a0b463639c)。

用户提供的HTTP回调函数列表；调用方应用可借此了解解析状态或HTTP字段。

<a id="r_abaabd58d149720720ffd61025d58e4a9"></a>

```c
uint8_t * recv_buf
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[recv_buf](#abaabd58d149720720ffd61025d58e4a9)。

用户提供的缓冲区（Buffer），用于存储接收的数据。

<a id="r_a9da5216bbd27ad54fd11368897ed660f"></a>

```c
size_t recv_buf_len
```

相关声明：[recv_buf_len](#a9da5216bbd27ad54fd11368897ed660f)。

用户提供的接收缓冲区（Receive Buffer）的长度。

<a id="r_a0da554e18c6b159f55fe12e6ba9fe4ca"></a>

```c
size_t data_len
```

相关声明：[data_len](#a0da554e18c6b159f55fe12e6ba9fe4ca)。

用户提供的接收缓冲区（Receive Buffer）中剩余未处理数据的长度。

<a id="r_a6a7573252e31fddb5cad5a6764c486c1"></a>

```c
const char * url
```

相关声明：[url](#a6a7573252e31fddb5cad5a6764c486c1)。

此次请求的URL，例如`/index.html`。

<a id="r_a38cad3f92ed5b712f749851bbeed9a2f"></a>

```c
const char * protocol
```

相关声明：[protocol](#a38cad3f92ed5b712f749851bbeed9a2f)。

HTTP协议（Protocol），例如“HTTP/1.1”。

<a id="r_a775ef341a6a85b135b10786e9b4a1cbf"></a>

```c
const char *const * header_fields
```

相关声明：[header_fields](#a775ef341a6a85b135b10786e9b4a1cbf)。

应用专用的HTTP头部字段（Header Fields）；Content-Type可在此处或下一个字段中指定。

<a id="r_a1e610f06e9a8ec05cb0de382163a8c79"></a>

```c
const char * content_type_value
```

相关声明：[content_type_value](#a1e610f06e9a8ec05cb0de382163a8c79)。

Content-Type头部字段的值，可为NULL。

<a id="r_a3ed1146d59f33e9042fae421619df27c"></a>

```c
const char * host
```

相关声明：[host](#a3ed1146d59f33e9042fae421619df27c)。

请求中使用的主机名（Hostname）。

<a id="r_abe9fdaab40cac6afb16acc2560dfe7e7"></a>

```c
const char * port
```

相关声明：[port](#abe9fdaab40cac6afb16acc2560dfe7e7)。

请求中使用的端口号（Port Number）。

<a id="r_a15551f2e8c772479fb7acac20765fa12"></a>

```c
http_payload_cb_t payload_cb
```

相关声明：[http_payload_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#gaf46ede77bdc83602c84b9342dd8d30ed)、[payload_cb](#a15551f2e8c772479fb7acac20765fa12)。

用户提供的回调函数（Callback Function），在需要发送载荷时调用。

<a id="r_af201ae38024233307ed2c87684ea70d3"></a>

```c
const char * payload
```

相关声明：[payload](#af201ae38024233307ed2c87684ea70d3)。

载荷（Payload），可为NULL。

<a id="r_a589615592c6c14bdecc03553c395c12f"></a>

```c
size_t payload_len
```

相关声明：[payload_len](#a589615592c6c14bdecc03553c395c12f)。

载荷长度（Payload Length）用于计算Content-Length。

<a id="r_ab6fe0ec09c24302279124043e82f17ff"></a>

```c
http_header_cb_t optional_headers_cb
```

相关声明：[http_header_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#ga34a431c54c52b86618ca0e27ce3862b4)、[optional_headers_cb](#ab6fe0ec09c24302279124043e82f17ff)。

用户提供的回调函数（Callback Function），在需要发送可选头部时调用。

<a id="r_aa29c2bcb70011c9776c959667e10bcf5"></a>

```c
const char ** optional_headers
```

相关声明：[optional_headers](#aa29c2bcb70011c9776c959667e10bcf5)。

以NULL终止的列表，包含应添加到HTTP请求的可选头部（Optional Headers）。

## 35.2\_详细说明（Detailed Documentation）

<a id="a1e610f06e9a8ec05cb0de382163a8c79"></a>

### `content_type_value`

```c
const char* http_request::content_type_value
```

Content-Type头部字段的值，可为NULL。

<a id="a0da554e18c6b159f55fe12e6ba9fe4ca"></a>

### `data_len`

```c
size_t http_request::data_len
```

用户提供的接收缓冲区（Receive Buffer）中剩余未处理数据的长度。

典型HTTP处理过程中，此值应为0；不过，在切换协议（Switching Protocols）时，可能留有属于新协议的数据。

<a id="a775ef341a6a85b135b10786e9b4a1cbf"></a>

### `header_fields`

```c
const char* const* http_request::header_fields
```

应用专用的HTTP头部字段（Header Fields）；Content-Type可在此处或下一个字段中指定。

Content-Type可能随应用而变化，但某些头部字段在应用的整个生命周期中都保持不变。这是以NULL终止的头部字段列表（Header Fields）。

<a id="a3ed1146d59f33e9042fae421619df27c"></a>

### `host`

```c
const char* http_request::host
```

请求中使用的主机名（Hostname）。

<a id="afbe0c199a4a58029bf2d83a0b463639c"></a>

### `http_cb`

```c
const struct http_parser_settings* http_request::http_cb
```

用户提供的HTTP回调函数列表；调用方应用可借此了解解析状态或HTTP字段。

此项可选，通常不需要。

<a id="abb86ccd0e0801c278ef37a78a4b7a958"></a>

### `internal`

```c
struct http_client_internal_data http_request::internal
```

HTTP客户端请求（Client Request）的内部数据。

<a id="adbfcd3bcaf57205360bad957a13999e6"></a>

### `method`

```c
enum http_method http_request::method
```

HTTP方法（Method）：GET、HEAD、OPTIONS、POST等。

<a id="aa29c2bcb70011c9776c959667e10bcf5"></a>

### `optional_headers`

```c
const char** http_request::optional_headers
```

以NULL终止的列表，包含应添加到HTTP请求的可选头部（Optional Headers）。

可为NULL。指定optional_headers_cb后会忽略此字段。注意，有两个类似字段包含头部：上面的header_fields和此处的optional_headers。这样设计是为了支持WebSocket用例：WebSocket使用header_fields，而应用专用的可选头部放在本字段中。

<a id="ab6fe0ec09c24302279124043e82f17ff"></a>

### `optional_headers_cb`

```c
http_header_cb_t http_request::optional_headers_cb
```

用户提供的回调函数（Callback Function），在需要发送可选头部时调用。

可为NULL，此时使用http_request中的optional_headers字段。optional_headers回调（Callback）使用户能够发送比实际可分配内存容量更多的HTTP头部数据。

<a id="af201ae38024233307ed2c87684ea70d3"></a>

### `payload`

```c
const char* http_request::payload
```

载荷（Payload），可为NULL。

<a id="a15551f2e8c772479fb7acac20765fa12"></a>

### `payload_cb`

```c
http_payload_cb_t http_request::payload_cb
```

用户提供的回调函数（Callback Function），在需要发送载荷时调用。

可为NULL，此时使用http_request中的payload字段。payload回调（Callback）使用户能够发送比实际可分配内存容量更多的数据。

<a id="a589615592c6c14bdecc03553c395c12f"></a>

### `payload_len`

```c
size_t http_request::payload_len
```

载荷长度（Payload Length）用于计算Content-Length。

分块传输（Chunked Transfers）时设为0。

<a id="abe9fdaab40cac6afb16acc2560dfe7e7"></a>

### `port`

```c
const char* http_request::port
```

请求中使用的端口号（Port Number）。

<a id="a38cad3f92ed5b712f749851bbeed9a2f"></a>

### `protocol`

```c
const char* http_request::protocol
```

HTTP协议（Protocol），例如“HTTP/1.1”。

<a id="abaabd58d149720720ffd61025d58e4a9"></a>

### `recv_buf`

```c
uint8_t* http_request::recv_buf
```

用户提供的缓冲区（Buffer），用于存储接收的数据。

<a id="a9da5216bbd27ad54fd11368897ed660f"></a>

### `recv_buf_len`

```c
size_t http_request::recv_buf_len
```

用户提供的接收缓冲区（Receive Buffer）的长度。

<a id="aba8bf528f3e279d55662eedc9168d25c"></a>

### `response`

```c
http_response_cb_t http_request::response
```

用户提供的回调函数（Callback Function），在收到响应时调用。

<a id="a6a7573252e31fddb5cad5a6764c486c1"></a>

### `url`

```c
const char* http_request::url
```

此次请求的URL，例如`/index.html`。

本数据类型文档由以下文件生成：

- `zephyr/net/http/client.h`

## 35.3\_原页交叉引用（Cross References）

- [zephyr/net/http/client.h](https://docs.zephyrproject.org/latest/doxygen/html/http_2client_8h_source.html)
- [http_client_internal_data](P027_http_client_internal_data_结构体.md)
- [http_method](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#gaacd5f203e33ac338ca5cb8f02a3ff3b8)
- [http_response_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#ga6141c94f7da92b71713079063f3426be)
- [http_parser_settings](P033_http_parser_settings_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [http_payload_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#gaf46ede77bdc83602c84b9342dd8d30ed)
- [http_header_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#ga34a431c54c52b86618ca0e27ce3862b4)
- [http_request](P035_http_request_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P034_http_parser_url_结构体.md) · [返回大纲](大纲.md) · [下一章](P036_http_request_ctx_结构体.md)
