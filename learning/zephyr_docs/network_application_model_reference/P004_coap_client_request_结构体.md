---
id: learning.zephyr-docs.network-application-model-reference.page-4
title: coap_client_request_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcoap__client__request.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_coap\_client\_request\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcoap__client__request.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CoAP客户端请求（Client Request）的表示。

```c
#include <zephyr/net/coap_client.h>
```

<a id="details"></a>

CoAP客户端请求（Client Request）的表示。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 4.1\_数据成员（Data Fields）

<a id="r_a308709b298a7449d32492ee1170a6791"></a>

```c
enum coap_method method
```

相关声明：[coap_method](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga6a6547e3c755cf7a5033302c8294e0b7)、[method](#a308709b298a7449d32492ee1170a6791)。

请求方法（Request Method）。

<a id="r_a4db33f53cd9723d5c073d379578e5a18"></a>

```c
bool confirmable
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[confirmable](#a4db33f53cd9723d5c073d379578e5a18)。

CoAP可确认/不可确认消息（Confirmable / Non-confirmable Message）。

<a id="r_a5ed6e1221dff24cc5d86a00c68620a36"></a>

```c
char path [MAX_PATH_SIZE]
```

相关声明：[path](#a5ed6e1221dff24cc5d86a00c68620a36)。

请求资源的路径（Resource Path）。

<a id="r_ae0a506b0baef3133f8665a5c8799e8d3"></a>

```c
enum coap_content_format fmt
```

相关声明：[coap_content_format](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga94a8f9956742d3928fc3c63b8d01ae73)、[fmt](#ae0a506b0baef3133f8665a5c8799e8d3)。

要使用的内容格式（Content Format）。

<a id="r_aca43b59a62328be1d87901ab3e30f399"></a>

```c
const uint8_t * payload
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[payload](#aca43b59a62328be1d87901ab3e30f399)。

用户为发送请求分配的缓冲区（Buffer）。

<a id="r_a04e7fd6614e0a4b0a0e78f5420019582"></a>

```c
size_t len
```

相关声明：[len](#a04e7fd6614e0a4b0a0e78f5420019582)。

载荷长度（Payload Length）。

<a id="r_a14e1036a45b1bcfa60faaa5b158b535a"></a>

```c
coap_client_payload_cb_t payload_cb
```

相关声明：[coap_client_payload_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga3c35cc0227385124d0ebe25688e3bc1a)、[payload_cb](#a14e1036a45b1bcfa60faaa5b158b535a)。

可选的载荷回调（Payload Callback）。

<a id="r_aefc85ec14f031aabe5ed0830d819069a"></a>

```c
coap_client_response_cb_t cb
```

相关声明：[coap_client_response_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga37e6c0891c3e8eef3316e34d4b7a0318)、[cb](#aefc85ec14f031aabe5ed0830d819069a)。

收到响应时调用的回调（Callback）。

<a id="r_a333d2ed265a1a002c1ce116057d6e454"></a>

```c
struct coap_client_option options [MAX_EXTRA_OPTIONS]
```

相关声明：[coap_client_option](P003_coap_client_option_结构体.md)、[options](#a333d2ed265a1a002c1ce116057d6e454)。

要添加到请求中的附加选项（Extra Options）。

<a id="r_a03f9aec935feab0352254f2d425c59be"></a>

```c
uint8_t num_options
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_options](#a03f9aec935feab0352254f2d425c59be)。

附加选项（Extra Options）的数量。

<a id="r_ad725d95c1745d19e74d3ed39710b10b4"></a>

```c
void * user_data
```

相关声明：[user_data](#ad725d95c1745d19e74d3ed39710b10b4)。

用户提供的上下文（Context）。

<a id="r_aa50684b8d2c429eb2accc32a0c2908de"></a>

```c
uint32_t multicast_timeout_ms
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[multicast_timeout_ms](#aa50684b8d2c429eb2accc32a0c2908de)。

组播响应超时（Multicast Response Timeout），单位为毫秒。

## 4.2\_详细说明（Detailed Documentation）

<a id="aefc85ec14f031aabe5ed0830d819069a"></a>

### `cb`

```c
coap_client_response_cb_t coap_client_request::cb
```

收到响应时调用的回调（Callback）。

<a id="a4db33f53cd9723d5c073d379578e5a18"></a>

### `confirmable`

```c
bool coap_client_request::confirmable
```

CoAP可确认/不可确认消息（Confirmable / Non-confirmable Message）。

<a id="ae0a506b0baef3133f8665a5c8799e8d3"></a>

### `fmt`

```c
enum coap_content_format coap_client_request::fmt
```

要使用的内容格式（Content Format）。

<a id="a04e7fd6614e0a4b0a0e78f5420019582"></a>

### `len`

```c
size_t coap_client_request::len
```

载荷长度（Payload Length）。

<a id="a308709b298a7449d32492ee1170a6791"></a>

### `method`

```c
enum coap_method coap_client_request::method
```

请求方法（Request Method）。

<a id="aa50684b8d2c429eb2accc32a0c2908de"></a>

### `multicast_timeout_ms`

```c
uint32_t coap_client_request::multicast_timeout_ms
```

组播响应超时（Multicast Response Timeout），单位为毫秒。

大于0时表示组播请求（Multicast Request），可在超时时间内接收多个响应。超时后，最后一次回调以source=NULL表示完成，之后不再发出回调。按RFC 7252，组播请求始终为不可确认消息（Non-confirmable）。

**注意（Attention）**：注意（Attention）：仅在启用Kconfig选项CONFIG_COAP_CLIENT_MULTICAST时可用。

<a id="a03f9aec935feab0352254f2d425c59be"></a>

### `num_options`

```c
uint8_t coap_client_request::num_options
```

附加选项（Extra Options）的数量。

<a id="a333d2ed265a1a002c1ce116057d6e454"></a>

### `options`

```c
struct coap_client_option coap_client_request::options[MAX_EXTRA_OPTIONS]
```

要添加到请求中的附加选项（Extra Options）。

<a id="a5ed6e1221dff24cc5d86a00c68620a36"></a>

### `path`

```c
char coap_client_request::path[MAX_PATH_SIZE]
```

请求资源的路径（Resource Path）。

<a id="aca43b59a62328be1d87901ab3e30f399"></a>

### `payload`

```c
const uint8_t* coap_client_request::payload
```

用户为发送请求分配的缓冲区（Buffer）。

<a id="a14e1036a45b1bcfa60faaa5b158b535a"></a>

### `payload_cb`

```c
coap_client_payload_cb_t coap_client_request::payload_cb
```

可选的载荷回调（Payload Callback）。

<a id="ad725d95c1745d19e74d3ed39710b10b4"></a>

### `user_data`

```c
void* coap_client_request::user_data
```

用户提供的上下文（Context）。

本数据类型文档由以下文件生成：

- `zephyr/net/coap_client.h`

## 4.3\_原页交叉引用（Cross References）

- [zephyr/net/coap_client.h](https://docs.zephyrproject.org/latest/doxygen/html/coap__client_8h_source.html)
- [coap_method](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga6a6547e3c755cf7a5033302c8294e0b7)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [coap_content_format](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga94a8f9956742d3928fc3c63b8d01ae73)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [coap_client_payload_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga3c35cc0227385124d0ebe25688e3bc1a)
- [coap_client_response_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga37e6c0891c3e8eef3316e34d4b7a0318)
- [coap_client_option](P003_coap_client_option_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [RFC 7252](https://datatracker.ietf.org/doc/html/rfc7252)
- [CONFIG_COAP_CLIENT_MULTICAST](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_CLIENT_MULTICAST)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P003_coap_client_option_结构体.md) · [返回大纲](大纲.md) · [下一章](P005_coap_client_response_data_结构体.md)
