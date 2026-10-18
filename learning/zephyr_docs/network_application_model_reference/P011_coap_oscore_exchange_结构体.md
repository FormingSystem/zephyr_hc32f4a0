---
id: learning.zephyr-docs.network-application-model-reference.page-11
title: coap_oscore_exchange_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcoap__oscore__exchange.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_coap\_oscore\_exchange\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcoap__oscore__exchange.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

受限RESTful环境对象安全（OSCORE）的交换条目。

```c
#include <zephyr/net/coap_oscore.h>
```

<a id="details"></a>

OSCORE交换条目（Exchange Entry）。通过匹配客户端地址和请求令牌，跟踪哪些服务器响应需要OSCORE保护，见RFC 8613第8.3节。用COAP_SERVICE_DEFINE_OSCORE定义的CoAP服务拥有这些条目的静态分配缓存。注意（Attention）：仅在启用Kconfig选项CONFIG_COAP_OSCORE时可用。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 11.1\_数据成员（Data Fields）

<a id="r_ab97aabcc192841eb9646e187ae3409c3"></a>

```c
struct net_sockaddr_storage addr
```

相关声明：[addr](#ab97aabcc192841eb9646e187ae3409c3)。

客户端地址（Client Address）。

<a id="r_a17cb77ffec08aeb0c808986a5d213ef2"></a>

```c
net_socklen_t addr_len
```

相关声明：[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)、[addr_len](#a17cb77ffec08aeb0c808986a5d213ef2)。

地址长度（Address Length）

<a id="r_a8a2114940e704221746fda5e4888df51"></a>

```c
uint8_t token [COAP_TOKEN_MAX_LEN]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[token](#a8a2114940e704221746fda5e4888df51)。

请求中的令牌（Token）。

<a id="r_a4742ebc7d9858fa1b31f09eed3a266e1"></a>

```c
uint8_t tkl
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tkl](#a4742ebc7d9858fa1b31f09eed3a266e1)。

令牌长度（Token Length）。

<a id="r_a8115ef4326b8739e6f73a8e5dd70e748"></a>

```c
int64_t timestamp
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[timestamp](#a8115ef4326b8739e6f73a8e5dd70e748)。

创建时间戳（Creation Timestamp）。

<a id="r_a4bc063a4f3e275fb22880fd93a052c2f"></a>

```c
struct coap_oscore_context * ctx
```

相关声明：[ctx](#a4bc063a4f3e275fb22880fd93a052c2f)。

本次交换所用的OSCORE上下文（Context）。

## 11.2\_详细说明（Detailed Documentation）

<a id="ab97aabcc192841eb9646e187ae3409c3"></a>

### `addr`

```c
struct net_sockaddr_storage coap_oscore_exchange::addr
```

客户端地址（Client Address）。

<a id="a17cb77ffec08aeb0c808986a5d213ef2"></a>

### `addr_len`

```c
net_socklen_t coap_oscore_exchange::addr_len
```

地址长度（Address Length）

<a id="a4bc063a4f3e275fb22880fd93a052c2f"></a>

### `ctx`

```c
struct coap_oscore_context* coap_oscore_exchange::ctx
```

本次交换所用的OSCORE上下文（Context）。

<a id="a8115ef4326b8739e6f73a8e5dd70e748"></a>

### `timestamp`

```c
int64_t coap_oscore_exchange::timestamp
```

创建时间戳（Creation Timestamp）。

<a id="a4742ebc7d9858fa1b31f09eed3a266e1"></a>

### `tkl`

```c
uint8_t coap_oscore_exchange::tkl
```

令牌长度（Token Length）。

<a id="a8a2114940e704221746fda5e4888df51"></a>

### `token`

```c
uint8_t coap_oscore_exchange::token[COAP_TOKEN_MAX_LEN]
```

请求中的令牌（Token）。

本数据类型文档由以下文件生成：

- `zephyr/net/coap_oscore.h`

## 11.3\_原页交叉引用（Cross References）

- [zephyr/net/coap_oscore.h](https://docs.zephyrproject.org/latest/doxygen/html/coap__oscore_8h_source.html)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [RFC 8613, section-8.3](https://datatracker.ietf.org/doc/html/rfc8613#section-8.3)
- [COAP_SERVICE_DEFINE_OSCORE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#ga306c2f205e9008a2bd3f1862f33460d8)
- [CONFIG_COAP_OSCORE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_OSCORE)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P010_coap_option_结构体.md) · [返回大纲](大纲.md) · [下一章](P012_coap_oscore_init_params_结构体.md)
