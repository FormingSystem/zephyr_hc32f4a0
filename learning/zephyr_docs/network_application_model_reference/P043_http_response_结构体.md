---
id: learning.zephyr-docs.network-application-model-reference.page-43
title: http_response_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhttp__response.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_http\_response\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhttp__response.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

服务器返回的HTTP响应（Response）。

```c
#include <zephyr/net/http/client.h>
```

<a id="details"></a>

服务器返回的HTTP响应（Response）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 43.1\_数据成员（Data Fields）

<a id="r_af306ff4c8424b5abad76037abbfe2833"></a>

```c
const struct http_parser_settings * http_cb
```

相关声明：[http_parser_settings](P033_http_parser_settings_结构体.md)、[http_cb](#af306ff4c8424b5abad76037abbfe2833)。

供应用使用的HTTP解析器设置（Parser Settings）。

<a id="r_a1936119331645bb421d4a5dc0d3fffb5"></a>

```c
http_response_cb_t cb
```

相关声明：[http_response_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#ga6141c94f7da92b71713079063f3426be)、[cb](#a1936119331645bb421d4a5dc0d3fffb5)。

用户提供的HTTP响应回调（Response Callback），在已发送的HTTP请求收到响应时调用。

<a id="r_a45c8596746f5a359a1e18c95838b59d9"></a>

```c
uint8_t * body_frag_start
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[body_frag_start](#a45c8596746f5a359a1e18c95838b59d9)。

recv_buf中正文片段（Body Fragment）的起始地址。

<a id="r_a58405582a11aa86892b80133f8b4fa43"></a>

```c
size_t body_frag_len
```

相关声明：[body_frag_len](#a58405582a11aa86892b80133f8b4fa43)。

recv_buf中正文片段（Body Fragment）的长度。

<a id="r_aa16de8f3485062bf01b0536e64f58b46"></a>

```c
uint8_t * recv_buf
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[recv_buf](#aa16de8f3485062bf01b0536e64f58b46)。

存储响应（Response）的位置，由用户提供。

<a id="r_a7454c5963b7bb1c5311f77971d0d1d2f"></a>

```c
size_t recv_buf_len
```

相关声明：[recv_buf_len](#a7454c5963b7bb1c5311f77971d0d1d2f)。

响应缓冲区（Response Buffer）的最大长度。

<a id="r_a4208cf209674441a25231732aad91f89"></a>

```c
size_t data_len
```

相关声明：[data_len](#a4208cf209674441a25231732aad91f89)。

结果缓冲区（Result Buffer）中的数据长度。

<a id="r_aedcb476d4055a7ba04516cc7a8ef800f"></a>

```c
size_t content_length
```

相关声明：[content_length](#aedcb476d4055a7ba04516cc7a8ef800f)。

HTTP Content-Length字段的值。

<a id="r_a0eb2181115c753a3e1676a18d9a3ed59"></a>

```c
size_t processed
```

相关声明：[processed](#a0eb2181115c753a3e1676a18d9a3ed59)。

截至目前传递给响应回调（Response Callback）的数据量，包含本次传给回调的数据。

<a id="r_a6bf553c9399385afeb921f6abef9a875"></a>

```c
char http_status [HTTP_STATUS_STR_SIZE]
```

相关声明：[http_status](#a6bf553c9399385afeb921f6abef9a875)。

详细信息见RFC 7230第3.1.2节。

<a id="r_a94cd246204b04992712deefe51fc0c26"></a>

```c
uint16_t http_status_code
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[http_status_code](#a94cd246204b04992712deefe51fc0c26)。

与文字说明对应的HTTP数字状态码（Numeric Status Code）。

<a id="r_a1f88915f82406ae3592dec32b7430851"></a>

```c
struct http_content_range content_range
```

相关声明：[http_content_range](P028_http_content_range_结构体.md)、[content_range](#a1f88915f82406ae3592dec32b7430851)。

HTTP Content-Range响应字段的值。

<a id="r_a0d28b200a74c150e98b5fc18c61638cc"></a>

```c
uint8_t cl_present: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cl_present](#a0d28b200a74c150e98b5fc18c61638cc)。

是否存在Content-Length字段。

<a id="r_ac713af14995e36c1889291d12803ca18"></a>

```c
uint8_t body_found: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[body_found](#ac713af14995e36c1889291d12803ca18)。

是否找到消息正文（Message Body）。

<a id="r_a4f107746bfff244a841b950dd84b8162"></a>

```c
uint8_t message_complete: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[message_complete](#a4f107746bfff244a841b950dd84b8162)。

HTTP消息解析（Message Parsing）是否完成。

<a id="r_ade896effa407ccdc5c9a7ef3720e66e2"></a>

```c
uint8_t cr_present: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cr_present](#ade896effa407ccdc5c9a7ef3720e66e2)。

是否存在Content-Range字段。

## 43.2\_详细说明（Detailed Documentation）

<a id="ac713af14995e36c1889291d12803ca18"></a>

### `body_found`

```c
uint8_t http_response::body_found
```

是否找到消息正文（Message Body）。

<a id="a58405582a11aa86892b80133f8b4fa43"></a>

### `body_frag_len`

```c
size_t http_response::body_frag_len
```

recv_buf中正文片段（Body Fragment）的长度。

<a id="a45c8596746f5a359a1e18c95838b59d9"></a>

### `body_frag_start`

```c
uint8_t* http_response::body_frag_start
```

recv_buf中正文片段（Body Fragment）的起始地址。

原始示例（Example）：

```c
                  recv_buffer that contains header + body
                  _______________________________________

                              |←-------- body_frag_len ---------→|
           |←--------------------- data len --------------------→|
       ---------------------------------------------------------------
 ..header  |      header      |               body               |  body..
       ---------------------------------------------------------------
           ↑                  ↑
        recv_buf          body_frag_start


                     recv_buffer that contains body only
                     ___________________________________

            |←------------------ body_frag_len ------------------→|
            |←--------------------- data len --------------------→|
       ---------------------------------------------------------------
```

位置示意：`↑ recv_buf body_frag_start`。

位置约束：`body_frag_start >= recv_buf`。

关系式`body_frag_len = data_len - (body_frag_start - recv_buf)`仅对接收缓冲区报告的最后一个片段成立。分块正文（Chunked Body）可从同一个缓冲区报告多个片段，每个片段覆盖一个块的载荷。

<a id="a1936119331645bb421d4a5dc0d3fffb5"></a>

### `cb`

```c
http_response_cb_t http_response::cb
```

用户提供的HTTP响应回调（Response Callback），在已发送的HTTP请求收到响应时调用。

<a id="a0d28b200a74c150e98b5fc18c61638cc"></a>

### `cl_present`

```c
uint8_t http_response::cl_present
```

是否存在Content-Length字段。

<a id="aedcb476d4055a7ba04516cc7a8ef800f"></a>

### `content_length`

```c
size_t http_response::content_length
```

HTTP Content-Length字段的值。

响应为空（Null Response）时设为0。

<a id="a1f88915f82406ae3592dec32b7430851"></a>

### `content_range`

```c
struct http_content_range http_response::content_range
```

HTTP Content-Range响应字段的值。

由range_start、range_end和total_size组成。未提供总大小时，总大小设为0。

<a id="ade896effa407ccdc5c9a7ef3720e66e2"></a>

### `cr_present`

```c
uint8_t http_response::cr_present
```

是否存在Content-Range字段。

<a id="a4208cf209674441a25231732aad91f89"></a>

### `data_len`

```c
size_t http_response::data_len
```

结果缓冲区（Result Buffer）中的数据长度。

若该值大于recv_buf_len，表示数据已截断，无法完整复制到recv_buf。仅在用户未设置响应回调（Response Callback）时才可能发生这种情况。设置回调后，HTTP客户端API会多次调用响应回调，把全部数据交付用户。响应为空时为0。

<a id="af306ff4c8424b5abad76037abbfe2833"></a>

### `http_cb`

```c
const struct http_parser_settings* http_response::http_cb
```

供应用使用的HTTP解析器设置（Parser Settings）。

<a id="a6bf553c9399385afeb921f6abef9a875"></a>

### `http_status`

```c
char http_response::http_status[HTTP_STATUS_STR_SIZE]
```

详细信息见RFC 7230第3.1.2节。

状态码元素（Status-Code Element）是一个三位整数代码。

原因短语元素（Reason-Phrase Element）仅用于提供与数字状态码关联的文字说明。客户端应当（SHOULD）忽略原因短语内容。

给出空HTTP响应（Null Response）时为空白。

<a id="a94cd246204b04992712deefe51fc0c26"></a>

### `http_status_code`

```c
uint16_t http_response::http_status_code
```

与文字说明对应的HTTP数字状态码（Numeric Status Code）。

给出空响应（Null Response）时设为0；否则，对于有效HTTP响应，此值为三位整数代码。

<a id="a4f107746bfff244a841b950dd84b8162"></a>

### `message_complete`

```c
uint8_t http_response::message_complete
```

HTTP消息解析（Message Parsing）是否完成。

<a id="a0eb2181115c753a3e1676a18d9a3ed59"></a>

### `processed`

```c
size_t http_response::processed
```

截至目前传递给响应回调（Response Callback）的数据量，包含本次传给回调的数据。

整个正文（Body）接收完毕后，此值应等于content_length字段。给出空响应时为0。

<a id="aa16de8f3485062bf01b0536e64f58b46"></a>

### `recv_buf`

```c
uint8_t* http_response::recv_buf
```

存储响应（Response）的位置，由用户提供。

<a id="a7454c5963b7bb1c5311f77971d0d1d2f"></a>

### `recv_buf_len`

```c
size_t http_response::recv_buf_len
```

响应缓冲区（Response Buffer）的最大长度。

本数据类型文档由以下文件生成：

- `zephyr/net/http/client.h`

## 43.3\_原页交叉引用（Cross References）

- [zephyr/net/http/client.h](https://docs.zephyrproject.org/latest/doxygen/html/http_2client_8h_source.html)
- [http_parser_settings](P033_http_parser_settings_结构体.md)
- [http_response_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#ga6141c94f7da92b71713079063f3426be)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [RFC 7230, section-3.1.2](https://datatracker.ietf.org/doc/html/rfc7230#section-3.1.2)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [http_content_range](P028_http_content_range_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>
<a id="autotoc_md4"></a>

---

[上一章](P042_http_resource_detail_websocket_结构体.md) · [返回大纲](大纲.md) · [下一章](P044_http_response_ctx_结构体.md)
