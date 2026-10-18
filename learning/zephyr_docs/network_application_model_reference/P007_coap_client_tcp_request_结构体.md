---
id: learning.zephyr-docs.network-application-model-reference.page-7
title: coap_client_tcp_request_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcoap__client__tcp__request.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_coap\_client\_tcp\_request\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcoap__client__tcp__request.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CoAP TCP客户端请求（Client Request）的表示。

```c
#include <zephyr/net/coap_client_tcp.h>
```

<a id="details"></a>

CoAP TCP客户端请求（Client Request）的表示。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 7.1\_数据成员（Data Fields）

<a id="r_a62c381846bd997abb6cdb07344e84370"></a>

```c
enum coap_method method
```

相关声明：[coap_method](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga6a6547e3c755cf7a5033302c8294e0b7)、[method](#a62c381846bd997abb6cdb07344e84370)。

请求方法（Request Method）。

<a id="r_a691ab55e31c3a4b51cb427a24273dd54"></a>

```c
char path [MAX_TCP_PATH_SIZE]
```

相关声明：[path](#a691ab55e31c3a4b51cb427a24273dd54)。

请求资源的路径（Resource Path）。

<a id="r_ad2d2fe88ab399178f3a1d8dd72f6cf89"></a>

```c
enum coap_content_format fmt
```

相关声明：[coap_content_format](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga94a8f9956742d3928fc3c63b8d01ae73)、[fmt](#ad2d2fe88ab399178f3a1d8dd72f6cf89)。

要使用的内容格式（Content Format）。

<a id="r_aa32cf19f5e76d2c073f8fbb47b314a15"></a>

```c
const uint8_t * payload
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[payload](#aa32cf19f5e76d2c073f8fbb47b314a15)。

用户为发送请求分配的缓冲区（Buffer）。

<a id="r_a94815f05ca330d252a7800307e401782"></a>

```c
size_t len
```

相关声明：[len](#a94815f05ca330d252a7800307e401782)。

载荷长度（Payload Length）。

<a id="r_acf52d8cefdef4fef9540e7cd0ca67584"></a>

```c
coap_client_tcp_payload_cb_t payload_cb
```

相关声明：[coap_client_tcp_payload_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gad97f2afc8f4fec4b8b13eb73707ef953)、[payload_cb](#acf52d8cefdef4fef9540e7cd0ca67584)。

可选的载荷回调（Payload Callback）。

<a id="r_a8366b8978cb97f9fdcd1a4e7b419754f"></a>

```c
coap_client_tcp_response_cb_t cb
```

相关声明：[coap_client_tcp_response_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gaabd183897d2d59a23fca6848e463a400)、[cb](#a8366b8978cb97f9fdcd1a4e7b419754f)。

收到响应时调用的回调（Callback）。

<a id="r_a94af7ad3d156eb4a44525481073d5496"></a>

```c
struct coap_client_tcp_option options [MAX_TCP_EXTRA_OPTIONS]
```

相关声明：[coap_client_tcp_option](P006_coap_client_tcp_option_结构体.md)、[options](#a94af7ad3d156eb4a44525481073d5496)。

要添加到请求中的附加选项（Extra Options）。

<a id="r_a9eacf07abaf9ddd2b8a7bf50c12e0258"></a>

```c
uint8_t num_options
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_options](#a9eacf07abaf9ddd2b8a7bf50c12e0258)。

附加选项（Extra Options）的数量。

<a id="r_aae2ca57ccfeb43a6d29e47f714e97546"></a>

```c
void * user_data
```

相关声明：[user_data](#aae2ca57ccfeb43a6d29e47f714e97546)。

用户提供的上下文（Context）。

## 7.2\_详细说明（Detailed Documentation）

<a id="a8366b8978cb97f9fdcd1a4e7b419754f"></a>

### `cb`

```c
coap_client_tcp_response_cb_t coap_client_tcp_request::cb
```

收到响应时调用的回调（Callback）。

<a id="ad2d2fe88ab399178f3a1d8dd72f6cf89"></a>

### `fmt`

```c
enum coap_content_format coap_client_tcp_request::fmt
```

要使用的内容格式（Content Format）。

<a id="a94815f05ca330d252a7800307e401782"></a>

### `len`

```c
size_t coap_client_tcp_request::len
```

载荷长度（Payload Length）。

<a id="a62c381846bd997abb6cdb07344e84370"></a>

### `method`

```c
enum coap_method coap_client_tcp_request::method
```

请求方法（Request Method）。

<a id="a9eacf07abaf9ddd2b8a7bf50c12e0258"></a>

### `num_options`

```c
uint8_t coap_client_tcp_request::num_options
```

附加选项（Extra Options）的数量。

<a id="a94af7ad3d156eb4a44525481073d5496"></a>

### `options`

```c
struct coap_client_tcp_option coap_client_tcp_request::options[MAX_TCP_EXTRA_OPTIONS]
```

要添加到请求中的附加选项（Extra Options）。

<a id="a691ab55e31c3a4b51cb427a24273dd54"></a>

### `path`

```c
char coap_client_tcp_request::path[MAX_TCP_PATH_SIZE]
```

请求资源的路径（Resource Path）。

<a id="aa32cf19f5e76d2c073f8fbb47b314a15"></a>

### `payload`

```c
const uint8_t* coap_client_tcp_request::payload
```

用户为发送请求分配的缓冲区（Buffer）。

<a id="acf52d8cefdef4fef9540e7cd0ca67584"></a>

### `payload_cb`

```c
coap_client_tcp_payload_cb_t coap_client_tcp_request::payload_cb
```

可选的载荷回调（Payload Callback）。

<a id="aae2ca57ccfeb43a6d29e47f714e97546"></a>

### `user_data`

```c
void* coap_client_tcp_request::user_data
```

用户提供的上下文（Context）。

本数据类型文档由以下文件生成：

- `zephyr/net/coap_client_tcp.h`

## 7.3\_原页交叉引用（Cross References）

- [zephyr/net/coap_client_tcp.h](https://docs.zephyrproject.org/latest/doxygen/html/coap__client__tcp_8h_source.html)
- [coap_method](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga6a6547e3c755cf7a5033302c8294e0b7)
- [coap_content_format](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga94a8f9956742d3928fc3c63b8d01ae73)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [coap_client_tcp_payload_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gad97f2afc8f4fec4b8b13eb73707ef953)
- [coap_client_tcp_response_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gaabd183897d2d59a23fca6848e463a400)
- [coap_client_tcp_option](P006_coap_client_tcp_option_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P006_coap_client_tcp_option_结构体.md) · [返回大纲](大纲.md) · [下一章](P008_coap_core_metadata_结构体.md)
