---
id: learning.zephyr-docs.network-core-model-reference.page-96
title: net_in_addr_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__in__addr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第96章\_net\_in\_addr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__in__addr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IPv4地址结构（Address Struct）。

```c
#include <zephyr/net/net_ip.h>
```

<a id="details"></a>

IPv4地址结构（Address Struct）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 96.1\_数据成员（Data Fields）

```c
union {
```

<a id="r_ad56aadcadec742b97282fec89ad0ca67"></a>

```c
uint8_t s4_addr [4]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[s4_addr](#adca8424f8e83574c7f7d57a2138e7b8c)。

IPv4 地址缓冲区（Address buffer）。

<a id="r_a42e8d2e4f8b79e98db6b4172eb49fd24"></a>

```c
uint16_t s4_addr16 [2]
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[s4_addr16](#aac03b71ad3fbe365fa80a1f0a8b53cc5)。

采用大端序（Big Endian）。

<a id="r_a7d5e19dcb062f57f6b04643aa0e8c3aa"></a>

```c
uint32_t s4_addr32 [1]
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[s4_addr32](#ac8181820613973fc7d6b5db0e3e53abd)。

采用大端序（Big Endian）。

<a id="r_a89aad12896050c09293281b0d11872bb"></a>

```c
uint32_t s_addr
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[s_addr](#ad3ca9f01bd03dbe69617eae95743bfa4)。

采用大端字节序（Big endian），以兼容 POSIX。

<a id="r_a58a0f205e2bcba0b03446ca1efdd9d47"></a>

```c
};
```

## 96.2\_详细说明（Detailed Documentation）

<a id="a58a0f205e2bcba0b03446ca1efdd9d47"></a>

### `[union]`

```c
union { ... } net_in_addr
```

<a id="adca8424f8e83574c7f7d57a2138e7b8c"></a>

### `s4_addr`

```c
uint8_t net_in_addr::s4_addr[4]
```

IPv4 地址缓冲区（Address buffer）。

<a id="aac03b71ad3fbe365fa80a1f0a8b53cc5"></a>

### `s4_addr16`

```c
uint16_t net_in_addr::s4_addr16[2]
```

采用大端序（Big Endian）。

<a id="ac8181820613973fc7d6b5db0e3e53abd"></a>

### `s4_addr32`

```c
uint32_t net_in_addr::s4_addr32[1]
```

采用大端序（Big Endian）。

<a id="ad3ca9f01bd03dbe69617eae95743bfa4"></a>

### `s_addr`

```c
uint32_t net_in_addr::s_addr
```

采用大端字节序（Big endian），以兼容 POSIX。

本数据类型文档由以下文件生成：

- `zephyr/net/net_ip.h`

## 96.3\_原页交叉引用（Cross References）

- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [net_in_addr](P096_net_in_addr_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P095_net_in6_pktinfo_结构体.md) · [返回大纲](大纲.md) · [下一章](P097_net_in_pktinfo_结构体.md)
