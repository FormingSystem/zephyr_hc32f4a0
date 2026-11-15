---
id: learning.zephyr-docs.network-application-model-reference.page-25
title: dns_sd_rec_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdns__sd__rec.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_dns\_sd\_rec\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdns__sd__rec.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

DNS服务发现（Service Discovery）记录。

```c
#include <zephyr/net/dns_sd.h>
```

<a id="details"></a>

DNS服务发现（Service Discovery）记录。此结构用于实现RFC 6763，应用代码通常不应直接访问它。port指针必须非NULL。当port中的值非零时，服务会被通告为位于该端口；值为零时，不通告该服务。因此，多个服务如果把端口写死，就可以在同一端口上进行通告。另见（See Also）：RFC 6763。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 25.1\_数据成员（Data Fields）

<a id="r_a06a8d777d302f99a7ed8f4ddb7e3af7d"></a>

```c
const char * instance
```

相关声明：[instance](#a06a8d777d302f99a7ed8f4ddb7e3af7d)。

`<Instance>`（实例），例如：

<a id="r_ae944cbdafdaced49f7302292d23ea4f8"></a>

```c
const char * service
```

相关声明：[service](#ae944cbdafdaced49f7302292d23ea4f8)。

`<Service>`（服务）的前半部分，例如“_http”。

<a id="r_ad79c74e22f4546826b1de6c41402aa3e"></a>

```c
const char * proto
```

相关声明：[proto](#ad79c74e22f4546826b1de6c41402aa3e)。

`<Service>`（服务）的后半部分，为“_tcp”或“_udp”。

<a id="r_ad282799583cde5b60ae19d5f919c67fc"></a>

```c
const char * domain
```

相关声明：[domain](#ad282799583cde5b60ae19d5f919c67fc)。

`<Domain>`（域），例如“local”或“zephyrproject.org”。

<a id="r_ae0585e5a0643a483d6ad12b7ff853323"></a>

```c
const char * text
```

相关声明：[text](#ae0585e5a0643a483d6ad12b7ff853323)。

DNS文本记录（TXT Record）。

<a id="r_a852f246f90d3608acd3b660f57a59dfb"></a>

```c
size_t text_size
```

相关声明：[text_size](#a852f246f90d3608acd3b660f57a59dfb)。

DNS文本记录（TXT Record）的大小，单位为字节。

<a id="r_a714f196f0d5297d511d97f88c18aa993"></a>

```c
const uint16_t * port
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[port](#a714f196f0d5297d511d97f88c18aa993)。

指向服务所用端口号（Port Number）的指针。

## 25.2\_详细说明（Detailed Documentation）

<a id="ad282799583cde5b60ae19d5f919c67fc"></a>

### `domain`

```c
const char* dns_sd_rec::domain
```

`<Domain>`（域），例如“local”或“zephyrproject.org”。

<a id="a06a8d777d302f99a7ed8f4ddb7e3af7d"></a>

### `instance`

```c
const char* dns_sd_rec::instance
```

`<Instance>`（实例），例如：

“My HTTP Server”（我的HTTP服务器）。

<a id="a714f196f0d5297d511d97f88c18aa993"></a>

### `port`

```c
const uint16_t* dns_sd_rec::port
```

指向服务所用端口号（Port Number）的指针。

<a id="ad79c74e22f4546826b1de6c41402aa3e"></a>

### `proto`

```c
const char* dns_sd_rec::proto
```

`<Service>`（服务）的后半部分，为“_tcp”或“_udp”。

<a id="ae944cbdafdaced49f7302292d23ea4f8"></a>

### `service`

```c
const char* dns_sd_rec::service
```

`<Service>`（服务）的前半部分，例如“_http”。

<a id="ae0585e5a0643a483d6ad12b7ff853323"></a>

### `text`

```c
const char* dns_sd_rec::text
```

DNS文本记录（TXT Record）。

<a id="a852f246f90d3608acd3b660f57a59dfb"></a>

### `text_size`

```c
size_t dns_sd_rec::text_size
```

DNS文本记录（TXT Record）的大小，单位为字节。

本数据类型文档由以下文件生成：

- `zephyr/net/dns_sd.h`

## 25.3\_原页交叉引用（Cross References）

- [zephyr/net/dns_sd.h](https://docs.zephyrproject.org/latest/doxygen/html/dns__sd_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [RFC 6763](https://datatracker.ietf.org/doc/html/rfc6763)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P024_dns_resolve_txt_结构体.md) · [返回大纲](大纲.md) · [下一章](P026_http_client_ctx_结构体.md)
