---
id: learning.zephyr-docs.network-application-model-reference.page-15
title: coap_reply_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcoap__reply.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_coap\_reply\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcoap__reply.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

表示请求应答的处理程序（Reply Handler）；观察资源时也会使用它。

```c
#include <zephyr/net/coap.h>
```

<a id="details"></a>

表示请求应答的处理程序（Reply Handler）；观察资源时也会使用它。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 15.1\_数据成员（Data Fields）

<a id="r_a6a888bbb5652761002ce26aba09352cc"></a>

```c
coap_reply_t reply
```

相关声明：[coap_reply_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga84eda10c4bf3e62241e686fdfa828868)、[reply](#a6a888bbb5652761002ce26aba09352cc)。

CoAP应答回调（Reply Callback）。

<a id="r_aa951d9ba4eb7f8041e8e82df9c1401dc"></a>

```c
void * user_data
```

相关声明：[user_data](#aa951d9ba4eb7f8041e8e82df9c1401dc)。

用户专用的不透明数据（Opaque Data）。

<a id="r_aea6b98e109e270c08df1554c5eee65fe"></a>

```c
int age
```

相关声明：[age](#aea6b98e109e270c08df1554c5eee65fe)。

应答年龄（Reply Age）。

<a id="r_a94d17732056de3d8ecb3412c686091f8"></a>

```c
uint16_t id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[id](#a94d17732056de3d8ecb3412c686091f8)。

应答标识（Reply ID）。

<a id="r_a18d40c327933c30681b924446c21ea9d"></a>

```c
uint8_t token [8]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[token](#a18d40c327933c30681b924446c21ea9d)。

应答令牌（Reply Token）。

<a id="r_a038ccb29c2abff6168db3247241a8cc3"></a>

```c
uint8_t tkl
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tkl](#a038ccb29c2abff6168db3247241a8cc3)。

扩展令牌长度（Extended Token Length）。

## 15.2\_详细说明（Detailed Documentation）

<a id="aea6b98e109e270c08df1554c5eee65fe"></a>

### `age`

```c
int coap_reply::age
```

应答年龄（Reply Age）。

<a id="a94d17732056de3d8ecb3412c686091f8"></a>

### `id`

```c
uint16_t coap_reply::id
```

应答标识（Reply ID）。

<a id="a6a888bbb5652761002ce26aba09352cc"></a>

### `reply`

```c
coap_reply_t coap_reply::reply
```

CoAP应答回调（Reply Callback）。

<a id="a038ccb29c2abff6168db3247241a8cc3"></a>

### `tkl`

```c
uint8_t coap_reply::tkl
```

扩展令牌长度（Extended Token Length）。

<a id="a18d40c327933c30681b924446c21ea9d"></a>

### `token`

```c
uint8_t coap_reply::token[8]
```

应答令牌（Reply Token）。

<a id="aa951d9ba4eb7f8041e8e82df9c1401dc"></a>

### `user_data`

```c
void* coap_reply::user_data
```

用户专用的不透明数据（Opaque Data）。

本数据类型文档由以下文件生成：

- `zephyr/net/coap.h`

## 15.3\_原页交叉引用（Cross References）

- [zephyr/net/coap.h](https://docs.zephyrproject.org/latest/doxygen/html/coap_8h_source.html)
- [coap_reply_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga84eda10c4bf3e62241e686fdfa828868)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P014_coap_pending_结构体.md) · [返回大纲](大纲.md) · [下一章](P016_coap_resource_结构体.md)
