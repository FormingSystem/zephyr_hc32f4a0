---
id: learning.zephyr-docs.network-application-model-reference.page-14
title: coap_pending_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcoap__pending.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_coap\_pending\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcoap__pending.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

表示正在等待确认（ACK）的请求。

```c
#include <zephyr/net/coap.h>
```

<a id="details"></a>

表示正在等待确认（ACK）的请求。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 14.1\_数据成员（Data Fields）

```c
union {
```

<a id="r_a1cdb66a5f579658328470da8bba9856f"></a>

```c
struct net_sockaddr_storage addr_storage
```

相关声明：[addr_storage](#ab06a3561fd9ce0477862babe18e44a1e)。

远端地址存储（Remote Address Storage）。

<a id="r_adc559c0f5c39ec0eefcee8cab3dc7fc8"></a>

```c
};
```

CoAP远端地址存储（Remote Address Storage）。

<a id="r_a8b95f80a6eaac759ed0895201ff089d9"></a>

```c
int64_t t0
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[t0](#a8b95f80a6eaac759ed0895201ff089d9)。

请求发送的时间。

<a id="r_ab31339cc91df71ee6f90d5702f722fd6"></a>

```c
uint32_t timeout
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[timeout](#ab31339cc91df71ee6f90d5702f722fd6)。

超时（Timeout），单位为毫秒。

<a id="r_a8b1952271bd0c733c2fbcb158b60ca99"></a>

```c
uint16_t id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[id](#a8b1952271bd0c733c2fbcb158b60ca99)。

消息标识（Message ID）。

<a id="r_a0a506507e472b3813e672f2b455e4bcc"></a>

```c
uint8_t * data
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#a0a506507e472b3813e672f2b455e4bcc)。

用户分配的缓冲区（Buffer）。

<a id="r_a4eb95f8fadef7d42aecdf25cc5ee3b1d"></a>

```c
uint16_t len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[len](#a4eb95f8fadef7d42aecdf25cc5ee3b1d)。

CoAP数据包的长度。

<a id="r_a8aebb187845bcb6cb07dee68927f1aa6"></a>

```c
uint8_t retries
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[retries](#a8aebb187845bcb6cb07dee68927f1aa6)。

请求已发送的次数。

<a id="r_a05ca08379d13e10dfe86322f666c3d97"></a>

```c
struct coap_transmission_parameters params
```

相关声明：[coap_transmission_parameters](P017_coap_transmission_parameters_结构体.md)、[params](#a05ca08379d13e10dfe86322f666c3d97)。

传输参数（Transmission Parameters）。

## 14.2\_详细说明（Detailed Documentation）

<a id="adc559c0f5c39ec0eefcee8cab3dc7fc8"></a>

### `[union]`

```c
union { ... } coap_pending
```

CoAP远端地址存储（Remote Address Storage）。

<a id="ab06a3561fd9ce0477862babe18e44a1e"></a>

### `addr_storage`

```c
struct net_sockaddr_storage coap_pending::addr_storage
```

远端地址存储（Remote Address Storage）。

<a id="a0a506507e472b3813e672f2b455e4bcc"></a>

### `data`

```c
uint8_t* coap_pending::data
```

用户分配的缓冲区（Buffer）。

<a id="a8b1952271bd0c733c2fbcb158b60ca99"></a>

### `id`

```c
uint16_t coap_pending::id
```

消息标识（Message ID）。

<a id="a4eb95f8fadef7d42aecdf25cc5ee3b1d"></a>

### `len`

```c
uint16_t coap_pending::len
```

CoAP数据包的长度。

<a id="a05ca08379d13e10dfe86322f666c3d97"></a>

### `params`

```c
struct coap_transmission_parameters coap_pending::params
```

传输参数（Transmission Parameters）。

<a id="a8aebb187845bcb6cb07dee68927f1aa6"></a>

### `retries`

```c
uint8_t coap_pending::retries
```

请求已发送的次数。

<a id="a8b95f80a6eaac759ed0895201ff089d9"></a>

### `t0`

```c
int64_t coap_pending::t0
```

请求发送的时间。

<a id="ab31339cc91df71ee6f90d5702f722fd6"></a>

### `timeout`

```c
uint32_t coap_pending::timeout
```

超时（Timeout），单位为毫秒。

本数据类型文档由以下文件生成：

- `zephyr/net/coap.h`

## 14.3\_原页交叉引用（Cross References）

- [zephyr/net/coap.h](https://docs.zephyrproject.org/latest/doxygen/html/coap_8h_source.html)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [coap_transmission_parameters](P017_coap_transmission_parameters_结构体.md)
- [coap_pending](P014_coap_pending_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P013_coap_packet_结构体.md) · [返回大纲](大纲.md) · [下一章](P015_coap_reply_结构体.md)
