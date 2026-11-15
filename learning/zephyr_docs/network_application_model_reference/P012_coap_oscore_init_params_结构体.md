---
id: learning.zephyr-docs.network-application-model-reference.page-12
title: coap_oscore_init_params_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcoap__oscore__init__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_coap\_oscore\_init\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcoap__oscore__init__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

OSCORE安全上下文派生参数（Security Context Derivation Parameters），见RFC 8613第3.2节。

```c
#include <zephyr/net/coap_oscore.h>
```

<a id="details"></a>

OSCORE安全上下文派生参数（Security Context Derivation Parameters），见RFC 8613第3.2节。说明（Note）：coap_oscore_context_add()会把所有引用的缓冲区复制到上下文池，因此调用一返回，调用方即可释放或复用这些缓冲区；它们无需比派生出的上下文存活得更久。注意（Attention）：仅在启用Kconfig选项CONFIG_COAP_OSCORE时可用。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 12.1\_数据成员（Data Fields）

<a id="r_a6b4842301e3de5b5b6a27b3f5b7f2b16"></a>

```c
const uint8_t * master_secret
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[master_secret](#a6b4842301e3de5b5b6a27b3f5b7f2b16)。

主密钥（Master Secret），必填；AES-CCM-16-64-128通常使用16字节。

<a id="r_a836d7cd5a6181fff740aa4958b3217ca"></a>

```c
size_t master_secret_len
```

相关声明：[master_secret_len](#a836d7cd5a6181fff740aa4958b3217ca)。

master_secret的长度，单位为字节。

<a id="r_a9c5b4efd2f490c65c79b72317e7d703f"></a>

```c
const uint8_t * sender_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sender_id](#a9c5b4efd2f490c65c79b72317e7d703f)。

发送方ID（Sender ID），必填。

<a id="r_a1eb4865020de525243b7a6e8cae2cf9f"></a>

```c
size_t sender_id_len
```

相关声明：[sender_id_len](#a1eb4865020de525243b7a6e8cae2cf9f)。

sender_id的长度，单位为字节。

<a id="r_a5180b28768cc1396c27bb8f712919a7d"></a>

```c
const uint8_t * recipient_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[recipient_id](#a5180b28768cc1396c27bb8f712919a7d)。

接收方ID（Recipient ID），必填。

<a id="r_a1108ec5f1f6d01995149bbef0430278c"></a>

```c
size_t recipient_id_len
```

相关声明：[recipient_id_len](#a1108ec5f1f6d01995149bbef0430278c)。

recipient_id的长度，单位为字节。

<a id="r_a149618d292ea959fed2eb1aa4b61e03f"></a>

```c
const uint8_t * master_salt
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[master_salt](#a149618d292ea959fed2eb1aa4b61e03f)。

主盐值（Master Salt），可选；不使用时设为NULL。

<a id="r_a5b6b967e34473ddc2a3d9f9f19656340"></a>

```c
size_t master_salt_len
```

相关声明：[master_salt_len](#a5b6b967e34473ddc2a3d9f9f19656340)。

master_salt的长度，单位为字节；不使用时为0。

<a id="r_a0ad550ea2dc25001f78054a843ae2118"></a>

```c
const uint8_t * id_context
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[id_context](#a0ad550ea2dc25001f78054a843ae2118)。

标识符上下文（ID Context），可选；不使用时设为NULL。

<a id="r_a1e9ed9e0b5d27133519cc639629f5d66"></a>

```c
size_t id_context_len
```

相关声明：[id_context_len](#a1e9ed9e0b5d27133519cc639629f5d66)。

id_context的长度，单位为字节；不使用时为0。

<a id="r_a923f137c01c062e6fa596589d14b1321"></a>

```c
enum coap_oscore_aead_alg aead_alg
```

相关声明：[coap_oscore_aead_alg](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__oscore.html#gad189c86f6afad030884f96778ed98091)、[aead_alg](#a923f137c01c062e6fa596589d14b1321)。

带关联数据的认证加密（AEAD）算法；默认算法使用COAP_OSCORE_AEAD_AES_CCM_16_64_128。

<a id="r_a2c1c9a3175976ee35194ec54404eae4a"></a>

```c
enum coap_oscore_hkdf hkdf
```

相关声明：[coap_oscore_hkdf](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__oscore.html#ga41bc77478b88bf7ca0f04f1ed0a2a0d1)、[hkdf](#a2c1c9a3175976ee35194ec54404eae4a)。

密钥派生函数（KDF）算法；默认算法使用COAP_OSCORE_HKDF_SHA_256。

<a id="r_a3cab68148e70cf453545058fdb0e94e3"></a>

```c
bool fresh_master_secret_salt
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[fresh_master_secret_salt](#a3cab68148e70cf453545058fdb0e94e3)。

每次启动时主密钥（Master Secret）与主盐值（Master Salt）的组合都唯一，则为true（例如：

## 12.2\_详细说明（Detailed Documentation）

<a id="a923f137c01c062e6fa596589d14b1321"></a>

### `aead_alg`

```c
enum coap_oscore_aead_alg coap_oscore_init_params::aead_alg
```

带关联数据的认证加密（AEAD）算法；默认算法使用COAP_OSCORE_AEAD_AES_CCM_16_64_128。

<a id="a3cab68148e70cf453545058fdb0e94e3"></a>

### `fresh_master_secret_salt`

```c
bool coap_oscore_init_params::fresh_master_secret_salt
```

每次启动时主密钥（Master Secret）与主盐值（Master Salt）的组合都唯一，则为true（例如：

通过EDHOC派生）。目前不支持复用主密钥和主盐值。将此项设置为false会导致错误。

<a id="a2c1c9a3175976ee35194ec54404eae4a"></a>

### `hkdf`

```c
enum coap_oscore_hkdf coap_oscore_init_params::hkdf
```

密钥派生函数（KDF）算法；默认算法使用COAP_OSCORE_HKDF_SHA_256。

<a id="a0ad550ea2dc25001f78054a843ae2118"></a>

### `id_context`

```c
const uint8_t* coap_oscore_init_params::id_context
```

标识符上下文（ID Context），可选；不使用时设为NULL。

<a id="a1e9ed9e0b5d27133519cc639629f5d66"></a>

### `id_context_len`

```c
size_t coap_oscore_init_params::id_context_len
```

id_context的长度，单位为字节；不使用时为0。

<a id="a149618d292ea959fed2eb1aa4b61e03f"></a>

### `master_salt`

```c
const uint8_t* coap_oscore_init_params::master_salt
```

主盐值（Master Salt），可选；不使用时设为NULL。

<a id="a5b6b967e34473ddc2a3d9f9f19656340"></a>

### `master_salt_len`

```c
size_t coap_oscore_init_params::master_salt_len
```

master_salt的长度，单位为字节；不使用时为0。

<a id="a6b4842301e3de5b5b6a27b3f5b7f2b16"></a>

### `master_secret`

```c
const uint8_t* coap_oscore_init_params::master_secret
```

主密钥（Master Secret），必填；AES-CCM-16-64-128通常使用16字节。

<a id="a836d7cd5a6181fff740aa4958b3217ca"></a>

### `master_secret_len`

```c
size_t coap_oscore_init_params::master_secret_len
```

master_secret的长度，单位为字节。

<a id="a5180b28768cc1396c27bb8f712919a7d"></a>

### `recipient_id`

```c
const uint8_t* coap_oscore_init_params::recipient_id
```

接收方ID（Recipient ID），必填。

<a id="a1108ec5f1f6d01995149bbef0430278c"></a>

### `recipient_id_len`

```c
size_t coap_oscore_init_params::recipient_id_len
```

recipient_id的长度，单位为字节。

<a id="a9c5b4efd2f490c65c79b72317e7d703f"></a>

### `sender_id`

```c
const uint8_t* coap_oscore_init_params::sender_id
```

发送方ID（Sender ID），必填。

<a id="a1eb4865020de525243b7a6e8cae2cf9f"></a>

### `sender_id_len`

```c
size_t coap_oscore_init_params::sender_id_len
```

sender_id的长度，单位为字节。

本数据类型文档由以下文件生成：

- `zephyr/net/coap_oscore.h`

## 12.3\_原页交叉引用（Cross References）

- [RFC 8613, section-3.2](https://datatracker.ietf.org/doc/html/rfc8613#section-3.2)
- [zephyr/net/coap_oscore.h](https://docs.zephyrproject.org/latest/doxygen/html/coap__oscore_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [coap_oscore_aead_alg](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__oscore.html#gad189c86f6afad030884f96778ed98091)
- [COAP_OSCORE_AEAD_AES_CCM_16_64_128](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__oscore.html#ggad189c86f6afad030884f96778ed98091a7e2d8a3abb742efbe6afaeee0dd80123)
- [coap_oscore_hkdf](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__oscore.html#ga41bc77478b88bf7ca0f04f1ed0a2a0d1)
- [COAP_OSCORE_HKDF_SHA_256](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__oscore.html#gga41bc77478b88bf7ca0f04f1ed0a2a0d1abd3a2ccfa28e081e9d0672bd835949bd)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [coap_oscore_context_add()](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__oscore.html#ga2e53e54122bc7c00c8bf67918617714a)
- [CONFIG_COAP_OSCORE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_OSCORE)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P011_coap_oscore_exchange_结构体.md) · [返回大纲](大纲.md) · [下一章](P013_coap_packet_结构体.md)
