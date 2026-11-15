---
id: learning.zephyr-docs.network-application-model-reference.page-18
title: dns_addrinfo_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdns__addrinfo.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_dns\_addrinfo\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdns__addrinfo.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

传给接收全部结果的回调的地址信息（Address Info）结构。

```c
#include <zephyr/net/dns_resolve.h>
```

<a id="details"></a>

传给接收全部结果的回调的地址信息（Address Info）结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 18.1\_数据成员（Data Fields）

<a id="r_af9a9458751ddb65219f3b5f6730df558"></a>

```c
uint8_t ai_family
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ai_family](#af9a9458751ddb65219f3b5f6730df558)。

地址信息的地址族（Address Family），同时充当类型判别值。

```c
union {
```

```c
struct {
```

<a id="r_aceedf675f62f44bb073832a6b38cfcb8"></a>

```c
net_socklen_t ai_addrlen
```

相关声明：[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)、[ai_addrlen](#aec286947b75b6f6689bd2df8bd7e761f)。

ai_addr字段或ai_canonname的长度。

```c
union {
```

<a id="r_ac50193d3b88a3309b61c5b327ee796b3"></a>

```c
struct net_sockaddr_storage ai_addr_storage
```

相关声明：[ai_addr_storage](#a6dd760be324864177dbbad21c21a6cfe)。

套接字地址信息存储（Socket Address Info Storage）。

<a id="r_ad6e017940f680978806956f9c895eec7"></a>

```c
}
```

NET_AF_INET或NET_AF_INET6地址信息。

<a id="r_a8d0183768f4b102ad0bc8425b99a8dc4"></a>

```c
char ai_canonname [20+1]
```

相关声明：[ai_canonname](#a21db6675aef2f8bafb83846343eae9ce)。

NET_AF_LOCAL地址的规范名称（Canonical Name）。

<a id="r_abc116c2f13ae7df4252bb51c817eae92"></a>

```c
}
```

A或AAAA记录（Records）。

```c
struct {
```

<a id="r_a9129c541debb773ecd89d198faa181f2"></a>

```c
enum dns_resolve_extension ai_extension
```

相关声明：[dns_resolve_extension](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga8a4330071b7161e1738dd91b1f6d6097)、[ai_extension](#ac130969f14020524d2c427888309656d)。

返回的扩展类型（Extension Kind）。

```c
union {
```

<a id="r_a7af9ffe113fd979019d8e4d618c22aee"></a>

```c
struct dns_resolve_txt ai_txt
```

相关声明：[dns_resolve_txt](P024_dns_resolve_txt_结构体.md)、[ai_txt](#a57ed2208756cbac08b811e98d4828dfd)。

文本记录（TXT）的信息。

<a id="r_a7b2f7e23037ba4ce71dee82c644f4a57"></a>

```c
struct dns_resolve_srv ai_srv
```

相关声明：[dns_resolve_srv](P023_dns_resolve_srv_结构体.md)、[ai_srv](#a266971c18f120e455ba9ea522644a7ae)。

服务位置记录（SRV）的信息。

<a id="r_afc04f2c539d7232509caf6a32650208e"></a>

```c
struct dns_resolve_private ai_private
```

相关声明：[dns_resolve_private](P022_dns_resolve_private_结构体.md)、[ai_private](#a9bdea16062e9f86b48fde8d5c3440a44)。

私有资源记录（RR）的信息。

<a id="r_aaf43ed79ab95e15dc0b07d9b894de4f0"></a>

```c
}
```

<a id="r_aa280e664304434c895dbd5f66ace919b"></a>

```c
}
```

服务位置（SRV）或文本（TXT）记录，属于NET_AF_UNSPEC扩展。

<a id="r_aa0a86d2d74233ea3d4a681123759bf54"></a>

```c
};
```

## 18.2\_详细说明（Detailed Documentation）

<a id="aa0a86d2d74233ea3d4a681123759bf54"></a>

### `[union]`

```c
union { ... } dns_addrinfo
```

<a id="a6dd760be324864177dbbad21c21a6cfe"></a>

### `ai_addr_storage`

```c
struct net_sockaddr_storage dns_addrinfo::ai_addr_storage
```

套接字地址信息存储（Socket Address Info Storage）。

<a id="aec286947b75b6f6689bd2df8bd7e761f"></a>

### `ai_addrlen`

```c
net_socklen_t dns_addrinfo::ai_addrlen
```

ai_addr字段或ai_canonname的长度。

<a id="a21db6675aef2f8bafb83846343eae9ce"></a>

### `ai_canonname`

```c
char dns_addrinfo::ai_canonname[20+1]
```

NET_AF_LOCAL地址的规范名称（Canonical Name）。

<a id="ac130969f14020524d2c427888309656d"></a>

### `ai_extension`

```c
enum dns_resolve_extension dns_addrinfo::ai_extension
```

返回的扩展类型（Extension Kind）。

<a id="af9a9458751ddb65219f3b5f6730df558"></a>

### `ai_family`

```c
uint8_t dns_addrinfo::ai_family
```

地址信息的地址族（Address Family），同时充当类型判别值。

<a id="a9bdea16062e9f86b48fde8d5c3440a44"></a>

### `ai_private`

```c
struct dns_resolve_private dns_addrinfo::ai_private
```

私有资源记录（RR）的信息。

<a id="a266971c18f120e455ba9ea522644a7ae"></a>

### `ai_srv`

```c
struct dns_resolve_srv dns_addrinfo::ai_srv
```

服务位置记录（SRV）的信息。

<a id="a57ed2208756cbac08b811e98d4828dfd"></a>

### `ai_txt`

```c
struct dns_resolve_txt dns_addrinfo::ai_txt
```

文本记录（TXT）的信息。

本数据类型文档由以下文件生成：

- `zephyr/net/dns_resolve.h`

## 18.3\_原页交叉引用（Cross References）

- [zephyr/net/dns_resolve.h](https://docs.zephyrproject.org/latest/doxygen/html/dns__resolve_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)
- [dns_resolve_extension](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga8a4330071b7161e1738dd91b1f6d6097)
- [dns_resolve_txt](P024_dns_resolve_txt_结构体.md)
- [dns_resolve_srv](P023_dns_resolve_srv_结构体.md)
- [dns_resolve_private](P022_dns_resolve_private_结构体.md)
- [dns_addrinfo](P018_dns_addrinfo_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P017_coap_transmission_parameters_结构体.md) · [返回大纲](大纲.md) · [下一章](P019_dns_resolve_context_结构体.md)
