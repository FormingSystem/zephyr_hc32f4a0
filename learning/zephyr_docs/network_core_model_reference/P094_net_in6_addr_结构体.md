---
id: learning.zephyr-docs.network-core-model-reference.page-94
title: net_in6_addr_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__in6__addr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第94章\_net\_in6\_addr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__in6__addr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IPv6地址结构（Address Struct）。

```c
#include <zephyr/net/net_ip.h>
```

<a id="details"></a>

IPv6地址结构（Address Struct）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 94.1\_数据成员（Data Fields）

```c
union {
```

<a id="r_a1da5189e8def5e7688432ccec96b00ce"></a>

```c
uint8_t s6_addr [16]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[s6_addr](#adfee3135d20aa7b5252aab9b9803bcd7)。

IPv6 地址缓冲区（Address buffer）。

<a id="r_a6ace4f4f220f5ae07f675b7d9a9657bf"></a>

```c
uint16_t s6_addr16 [8]
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[s6_addr16](#a18fb132bfd7ac8945a981b8bb76e83ed)。

采用大端序（Big Endian）。

<a id="r_a680f4ac9ab35fb66bf4d0286446935a4"></a>

```c
uint32_t s6_addr32 [4]
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[s6_addr32](#ac2d541ca17ee6fa482765014f447f41a)。

采用大端序（Big Endian）。

<a id="r_a014068ff35daf7a80f933550bf732395"></a>

```c
};
```

## 94.2\_详细说明（Detailed Documentation）

<a id="a014068ff35daf7a80f933550bf732395"></a>

### `[union]`

```c
union { ... } net_in6_addr
```

<a id="adfee3135d20aa7b5252aab9b9803bcd7"></a>

### `s6_addr`

```c
uint8_t net_in6_addr::s6_addr[16]
```

IPv6 地址缓冲区（Address buffer）。

<a id="a18fb132bfd7ac8945a981b8bb76e83ed"></a>

### `s6_addr16`

```c
uint16_t net_in6_addr::s6_addr16[8]
```

采用大端序（Big Endian）。

<a id="ac2d541ca17ee6fa482765014f447f41a"></a>

### `s6_addr32`

```c
uint32_t net_in6_addr::s6_addr32[4]
```

采用大端序（Big Endian）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_ip.h`

## 94.3\_原页交叉引用（Cross References）

- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [net_in6_addr](P094_net_in6_addr_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P093_net_ifreq_结构体.md) · [返回大纲](大纲.md) · [下一章](P095_net_in6_pktinfo_结构体.md)
