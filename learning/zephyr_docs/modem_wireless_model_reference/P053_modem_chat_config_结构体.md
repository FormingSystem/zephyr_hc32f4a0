---
id: learning.zephyr-docs.modem-wireless-model-reference.page-53
title: modem_chat_config_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmodem__chat__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第53章\_modem\_chat\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmodem__chat__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

交互配置（Chat Configuration）。

```c
#include <zephyr/modem/chat.h>
```

<a id="details"></a>

交互配置（Chat Configuration）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 53.1\_数据成员（Data Fields）

<a id="r_ac002d9f43309db8c3c35826127d94194"></a>

```c
void * user_data
```

相关声明：[user_data](#ac002d9f43309db8c3c35826127d94194)。

应用可自由使用的用户数据，随调制解调器匹配回调传入。

<a id="r_a295de98c2e8866059e7194c57d0502b7"></a>

```c
uint8_t * receive_buf
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[receive_buf](#a295de98c2e8866059e7194c57d0502b7)。

用于保存已解析参数的接收缓冲区。

<a id="r_a76f85951f5750f0d07b1253af118ec6f"></a>

```c
uint16_t receive_buf_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[receive_buf_size](#a76f85951f5750f0d07b1253af118ec6f)。

接收缓冲区大小应为最长行长度加上最长匹配项长度。

<a id="r_a38e1eb6fb1e5a452f999bf8b3090141c"></a>

```c
const uint8_t * delimiter
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[delimiter](#a38e1eb6fb1e5a452f999bf8b3090141c)。

分隔符（Delimiter）。

<a id="r_aa30ccfd372c47c64e2a7b7c840405499"></a>

```c
uint8_t delimiter_size
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[delimiter_size](#aa30ccfd372c47c64e2a7b7c840405499)。

分隔符大小。

<a id="r_a00f0dc42251980cd51a8f2fd70b82e4f"></a>

```c
const uint8_t * filter
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[filter](#a00f0dc42251980cd51a8f2fd70b82e4f)。

解析器会丢弃的字节。

<a id="r_af762b783d33e192ef45647e0b2e2d70b"></a>

```c
uint8_t filter_size
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[filter_size](#af762b783d33e192ef45647e0b2e2d70b)。

过滤器（filter）的大小。

<a id="r_ae2afa6465bfad9c83dd57498165888b4"></a>

```c
uint8_t ** argv
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[argv](#ae2afa6465bfad9c83dd57498165888b4)。

用于指向已解析参数的指针数组。

<a id="r_a2cf551a0946459b2825595026ebc7490"></a>

```c
uint16_t argv_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[argv_size](#a2cf551a0946459b2825595026ebc7490)。

指针数组中的元素数量。

<a id="r_a661d96b8a7031b17e6f660c6e0e4be11"></a>

```c
const struct modem_chat_match * unsol_matches
```

相关声明：[modem_chat_match](P054_modem_chat_match_结构体.md)、[unsol_matches](#a661d96b8a7031b17e6f660c6e0e4be11)。

非请求消息匹配项（unsolicited matches）数组。

<a id="r_addfa7cacc676190d9e29c451d47ea3bd"></a>

```c
uint16_t unsol_matches_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[unsol_matches_size](#addfa7cacc676190d9e29c451d47ea3bd)。

非请求消息匹配项数组中的元素数量。

## 53.2\_详细说明（Detailed Documentation）

<a id="ae2afa6465bfad9c83dd57498165888b4"></a>

### `argv`

```c
uint8_t** modem_chat_config::argv
```

用于指向已解析参数的指针数组。

<a id="a2cf551a0946459b2825595026ebc7490"></a>

### `argv_size`

```c
uint16_t modem_chat_config::argv_size
```

指针数组中的元素数量。

<a id="a38e1eb6fb1e5a452f999bf8b3090141c"></a>

### `delimiter`

```c
const uint8_t* modem_chat_config::delimiter
```

分隔符（Delimiter）。

<a id="aa30ccfd372c47c64e2a7b7c840405499"></a>

### `delimiter_size`

```c
uint8_t modem_chat_config::delimiter_size
```

分隔符大小。

<a id="a00f0dc42251980cd51a8f2fd70b82e4f"></a>

### `filter`

```c
const uint8_t* modem_chat_config::filter
```

解析器会丢弃的字节。

<a id="af762b783d33e192ef45647e0b2e2d70b"></a>

### `filter_size`

```c
uint8_t modem_chat_config::filter_size
```

过滤器（filter）的大小。

<a id="a295de98c2e8866059e7194c57d0502b7"></a>

### `receive_buf`

```c
uint8_t* modem_chat_config::receive_buf
```

用于保存已解析参数的接收缓冲区。

<a id="a76f85951f5750f0d07b1253af118ec6f"></a>

### `receive_buf_size`

```c
uint16_t modem_chat_config::receive_buf_size
```

接收缓冲区大小应为最长行长度加上最长匹配项长度。

<a id="a661d96b8a7031b17e6f660c6e0e4be11"></a>

### `unsol_matches`

```c
const struct modem_chat_match* modem_chat_config::unsol_matches
```

非请求消息匹配项（unsolicited matches）数组。

<a id="addfa7cacc676190d9e29c451d47ea3bd"></a>

### `unsol_matches_size`

```c
uint16_t modem_chat_config::unsol_matches_size
```

非请求消息匹配项数组中的元素数量。

<a id="ac002d9f43309db8c3c35826127d94194"></a>

### `user_data`

```c
void* modem_chat_config::user_data
```

应用可自由使用的用户数据，随调制解调器匹配回调传入。

本数据类型文档由以下文件生成：

- `zephyr/modem/chat.h`

## 53.3\_原页交叉引用（Cross References）

- [zephyr/modem/chat.h](https://docs.zephyrproject.org/latest/doxygen/html/chat_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [modem_chat_match](P054_modem_chat_match_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P052_modem_chat_结构体.md) · [返回大纲](大纲.md) · [下一章](P054_modem_chat_match_结构体.md)
