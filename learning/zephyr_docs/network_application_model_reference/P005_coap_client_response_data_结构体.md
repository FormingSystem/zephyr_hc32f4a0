---
id: learning.zephyr-docs.network-application-model-reference.page-5
title: coap_client_response_data_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcoap__client__response__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_coap\_client\_response\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcoap__client__response__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CoAP客户端响应数据（Client Response Data）的表示。

```c
#include <zephyr/net/coap_client.h>
```

<a id="details"></a>

CoAP客户端响应数据（Client Response Data）的表示。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 5.1\_数据成员（Data Fields）

<a id="r_a5219445f266949bf3981a7dd337bb318"></a>

```c
int16_t result_code
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[result_code](#a5219445f266949bf3981a7dd337bb318)。

响应结果代码（Result Code）。

<a id="r_a8a0ac5afbab9feba492a31e2bf27c29f"></a>

```c
const struct coap_packet * packet
```

相关声明：[coap_packet](P013_coap_packet_结构体.md)、[packet](#a8a0ac5afbab9feba492a31e2bf27c29f)。

指向响应CoAP数据包（Packet）的指针。

<a id="r_ad8342db8f7aa17740fc3e2688c54312e"></a>

```c
size_t offset
```

相关声明：[offset](#ad8342db8f7aa17740fc3e2688c54312e)。

载荷相对于分块传输（Blockwise Transfer）起点的偏移量。

<a id="r_a4a600d4a686e2029b0a3c00c84d6ebe5"></a>

```c
const uint8_t * payload
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[payload](#a4a600d4a686e2029b0a3c00c84d6ebe5)。

包含响应载荷（Payload）的缓冲区。

<a id="r_ab11643c1c070644970889c3d53e0f26e"></a>

```c
size_t payload_len
```

相关声明：[payload_len](#ab11643c1c070644970889c3d53e0f26e)。

载荷大小（Payload Size）。

<a id="r_aac23eadaa55bab0bde1b9a9dd91e4650"></a>

```c
bool last_block
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[last_block](#aac23eadaa55bab0bde1b9a9dd91e4650)。

指示响应的最后一个块（Last Block）。

<a id="r_abdf9e0a188dbddb2a8c7390be53f4135"></a>

```c
const struct net_sockaddr * source
```

相关声明：[net_sockaddr](https://docs.zephyrproject.org/latest/doxygen/html/structnet__sockaddr.html)、[source](#abdf9e0a188dbddb2a8c7390be53f4135)。

响应的源地址（Source Address）。

<a id="r_aa4f0deb7f1c8462554f0d3c1904ab099"></a>

```c
net_socklen_t source_len
```

相关声明：[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)、[source_len](#aa4f0deb7f1c8462554f0d3c1904ab099)。

响应的源地址长度（Source Address Length）。

## 5.2\_详细说明（Detailed Documentation）

<a id="aac23eadaa55bab0bde1b9a9dd91e4650"></a>

### `last_block`

```c
bool coap_client_response_data::last_block
```

指示响应的最后一个块（Last Block）。

<a id="ad8342db8f7aa17740fc3e2688c54312e"></a>

### `offset`

```c
size_t coap_client_response_data::offset
```

载荷相对于分块传输（Blockwise Transfer）起点的偏移量。

<a id="a8a0ac5afbab9feba492a31e2bf27c29f"></a>

### `packet`

```c
const struct coap_packet* coap_client_response_data::packet
```

指向响应CoAP数据包（Packet）的指针。

结果为错误时取NULL。

<a id="a4a600d4a686e2029b0a3c00c84d6ebe5"></a>

### `payload`

```c
const uint8_t* coap_client_response_data::payload
```

包含响应载荷（Payload）的缓冲区。

载荷（Payload）为空时取NULL。

<a id="ab11643c1c070644970889c3d53e0f26e"></a>

### `payload_len`

```c
size_t coap_client_response_data::payload_len
```

载荷大小（Payload Size）。

<a id="a5219445f266949bf3981a7dd337bb318"></a>

### `result_code`

```c
int16_t coap_client_response_data::result_code
```

响应结果代码（Result Code）。

发送失败时为负值；为正值时表示coap_response_code。

<a id="abdf9e0a188dbddb2a8c7390be53f4135"></a>

### `source`

```c
const struct net_sockaddr* coap_client_response_data::source
```

响应的源地址（Source Address）。

**注意（Attention）**：注意（Attention）：仅在启用Kconfig选项CONFIG_COAP_CLIENT_MULTICAST时可用。

<a id="aa4f0deb7f1c8462554f0d3c1904ab099"></a>

### `source_len`

```c
net_socklen_t coap_client_response_data::source_len
```

响应的源地址长度（Source Address Length）。

**注意（Attention）**：注意（Attention）：仅在启用Kconfig选项CONFIG_COAP_CLIENT_MULTICAST时可用。

本数据类型文档由以下文件生成：

- `zephyr/net/coap_client.h`

## 5.3\_原页交叉引用（Cross References）

- [zephyr/net/coap_client.h](https://docs.zephyrproject.org/latest/doxygen/html/coap__client_8h_source.html)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [coap_packet](P013_coap_packet_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [net_sockaddr](https://docs.zephyrproject.org/latest/doxygen/html/structnet__sockaddr.html)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)
- [coap_response_code](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga1ea81a365834e96f43ab7be573069d26)
- [CONFIG_COAP_CLIENT_MULTICAST](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_CLIENT_MULTICAST)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P004_coap_client_request_结构体.md) · [返回大纲](大纲.md) · [下一章](P006_coap_client_tcp_option_结构体.md)
