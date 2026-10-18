---
id: learning.zephyr-docs.network-application-model-reference.page-32
title: http_parser_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhttp__parser.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_http\_parser\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhttp__parser.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/net/http/parser.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 32.1\_数据成员（Data Fields）

<a id="r_ac6c327558547d55eb64a8aea1310cc2e"></a>

```c
unsigned int type: 2
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[type](#ac6c327558547d55eb64a8aea1310cc2e)。

私有（PRIVATE）。

<a id="r_a5e54708e0cb3f9ced19bd829dcdeaf53"></a>

```c
unsigned int flags: 8
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[flags](#a5e54708e0cb3f9ced19bd829dcdeaf53)。

<a id="r_a6f5952e0b47c83aeacf64fc287fd8003"></a>

```c
unsigned int state: 7
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[state](#a6f5952e0b47c83aeacf64fc287fd8003)。

<a id="r_ac5b254b99c6472ca19ae1f426758ce75"></a>

```c
unsigned int header_state: 7
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[header_state](#ac5b254b99c6472ca19ae1f426758ce75)。

<a id="r_a6f7ba706f975f447b3bf72be97facdf8"></a>

```c
unsigned int index: 7
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[index](#a6f7ba706f975f447b3bf72be97facdf8)。

<a id="r_acd80a931fcc87d41999397af1662fc3c"></a>

```c
unsigned int lenient_http_headers: 1
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[lenient_http_headers](#acd80a931fcc87d41999397af1662fc3c)。

<a id="r_a78085ca896bb3b9aa1ecb0f6fddc039d"></a>

```c
uint32_t nread
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[nread](#a78085ca896bb3b9aa1ecb0f6fddc039d)。

<a id="r_a7fd5a194802b1206bb773e096d291f29"></a>

```c
uint64_t content_length
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[content_length](#a7fd5a194802b1206bb773e096d291f29)。

<a id="r_a4cad8367f35e6739a9ffc45b851f49aa"></a>

```c
bool content_range_present
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[content_range_present](#a4cad8367f35e6739a9ffc45b851f49aa)。

<a id="r_ade28251e8473212ad8b9b28dcd343c93"></a>

```c
struct http_content_range content_range
```

相关声明：[http_content_range](P028_http_content_range_结构体.md)、[content_range](#ade28251e8473212ad8b9b28dcd343c93)。

<a id="r_ac994a4a8268652f5ce82de5bde5c3f9d"></a>

```c
unsigned short http_major
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[http_major](#ac994a4a8268652f5ce82de5bde5c3f9d)。

只读（READ-ONLY）。

<a id="r_ae8af6433c824f5348773842db62ad4ab"></a>

```c
unsigned short http_minor
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[http_minor](#ae8af6433c824f5348773842db62ad4ab)。

<a id="r_a82f5aed92ca3566489def7bc384bab26"></a>

```c
unsigned int status_code: 16
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[status_code](#a82f5aed92ca3566489def7bc384bab26)。

<a id="r_a7955de339fafd81ad54380845913457d"></a>

```c
unsigned int method: 8
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[method](#a7955de339fafd81ad54380845913457d)。

<a id="r_ab8638d65fa174bc1925d77e2533117fa"></a>

```c
unsigned int http_errno: 7
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[http_errno](#ab8638d65fa174bc1925d77e2533117fa)。

<a id="r_a748f476eacc5ac56b84dd07dbafb42a4"></a>

```c
unsigned int upgrade: 1
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[upgrade](#a748f476eacc5ac56b84dd07dbafb42a4)。

<a id="r_a7e87ce57b97f60f1fdb7039a8ecb0bca"></a>

```c
void * data
```

相关声明：[data](#a7e87ce57b97f60f1fdb7039a8ecb0bca)。

公共（PUBLIC）。

<a id="r_af2c5cbcfbecce1cce001fe2531a6bd8c"></a>

```c
const struct net_sockaddr * addr
```

相关声明：[net_sockaddr](https://docs.zephyrproject.org/latest/doxygen/html/structnet__sockaddr.html)、[addr](#af2c5cbcfbecce1cce001fe2531a6bd8c)。

## 32.2\_详细说明（Detailed Documentation）

<a id="af2c5cbcfbecce1cce001fe2531a6bd8c"></a>

### `addr`

```c
const struct net_sockaddr* http_parser::addr
```

<a id="a7fd5a194802b1206bb773e096d291f29"></a>

### `content_length`

```c
uint64_t http_parser::content_length
```

<a id="ade28251e8473212ad8b9b28dcd343c93"></a>

### `content_range`

```c
struct http_content_range http_parser::content_range
```

<a id="a4cad8367f35e6739a9ffc45b851f49aa"></a>

### `content_range_present`

```c
bool http_parser::content_range_present
```

<a id="a7e87ce57b97f60f1fdb7039a8ecb0bca"></a>

### `data`

```c
void* http_parser::data
```

公共（PUBLIC）。

<a id="a5e54708e0cb3f9ced19bd829dcdeaf53"></a>

### `flags`

```c
unsigned int http_parser::flags
```

<a id="ac5b254b99c6472ca19ae1f426758ce75"></a>

### `header_state`

```c
unsigned int http_parser::header_state
```

<a id="ab8638d65fa174bc1925d77e2533117fa"></a>

### `http_errno`

```c
unsigned int http_parser::http_errno
```

<a id="ac994a4a8268652f5ce82de5bde5c3f9d"></a>

### `http_major`

```c
unsigned short http_parser::http_major
```

只读（READ-ONLY）。

<a id="ae8af6433c824f5348773842db62ad4ab"></a>

### `http_minor`

```c
unsigned short http_parser::http_minor
```

<a id="a6f7ba706f975f447b3bf72be97facdf8"></a>

### `index`

```c
unsigned int http_parser::index
```

<a id="acd80a931fcc87d41999397af1662fc3c"></a>

### `lenient_http_headers`

```c
unsigned int http_parser::lenient_http_headers
```

<a id="a7955de339fafd81ad54380845913457d"></a>

### `method`

```c
unsigned int http_parser::method
```

<a id="a78085ca896bb3b9aa1ecb0f6fddc039d"></a>

### `nread`

```c
uint32_t http_parser::nread
```

<a id="a6f5952e0b47c83aeacf64fc287fd8003"></a>

### `state`

```c
unsigned int http_parser::state
```

<a id="a82f5aed92ca3566489def7bc384bab26"></a>

### `status_code`

```c
unsigned int http_parser::status_code
```

<a id="ac6c327558547d55eb64a8aea1310cc2e"></a>

### `type`

```c
unsigned int http_parser::type
```

私有（PRIVATE）。

<a id="a748f476eacc5ac56b84dd07dbafb42a4"></a>

### `upgrade`

```c
unsigned int http_parser::upgrade
```

本数据类型文档由以下文件生成：

- `zephyr/net/http/parser.h`

## 32.3\_原页交叉引用（Cross References）

- [zephyr/net/http/parser.h](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h_source.html)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [http_content_range](P028_http_content_range_结构体.md)
- [net_sockaddr](https://docs.zephyrproject.org/latest/doxygen/html/structnet__sockaddr.html)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P031_http_hpack_header_buf_结构体.md) · [返回大纲](大纲.md) · [下一章](P033_http_parser_settings_结构体.md)
