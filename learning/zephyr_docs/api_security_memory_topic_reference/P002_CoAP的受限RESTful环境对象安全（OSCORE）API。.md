---
id: learning.zephyr-docs.api-security-memory-topic-reference.page-2
title: CoAP的受限RESTful环境对象安全（OSCORE）API。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__coap__oscore.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_CoAP的受限RESTful环境对象安全（OSCORE）API。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__oscore.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CoAP的受限RESTful环境对象安全（OSCORE）API。

<a id="details"></a>

受限应用协议（CoAP）的对象安全（OSCORE）API。**引入版本（Since）：**4.5。**版本（Version）：**0.1.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_coap_5Foscore_5Finit_5Fparams"></a>

```c
struct coap_oscore_init_params
```

相关声明：[coap_oscore_init_params](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md)。

OSCORE安全上下文派生参数（Security Context Derivation Parameters），见RFC 8613第3.2节。

<a id="r_coap_5Foscore_5Fexchange"></a>

```c
struct coap_oscore_exchange
```

相关声明：[coap_oscore_exchange](../network_application_model_reference/P011_coap_oscore_exchange_结构体.md)。

受限RESTful环境对象安全（OSCORE）的交换条目。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 2.2\_枚举（Enumerations）

<a id="r_gad189c86f6afad030884f96778ed98091"></a>

```c
enum coap_oscore_aead_alg { COAP_OSCORE_AEAD_AES_CCM_16_64_128 = 0 }
```

相关声明：[coap_oscore_aead_alg](#gad189c86f6afad030884f96778ed98091)、[COAP_OSCORE_AEAD_AES_CCM_16_64_128](#ggad189c86f6afad030884f96778ed98091a7e2d8a3abb742efbe6afaeee0dd80123)。

用于保护 OSCORE 消息的带关联数据认证加密（AEAD）算法，参见 RFC 8613 第 3.1 节。

<a id="r_ga41bc77478b88bf7ca0f04f1ed0a2a0d1"></a>

```c
enum coap_oscore_hkdf { COAP_OSCORE_HKDF_SHA_256 = 0 }
```

相关声明：[coap_oscore_hkdf](#ga41bc77478b88bf7ca0f04f1ed0a2a0d1)、[COAP_OSCORE_HKDF_SHA_256](#gga41bc77478b88bf7ca0f04f1ed0a2a0d1abd3a2ccfa28e081e9d0672bd835949bd)。

用于派生 OSCORE 密钥的基于 HMAC 的密钥派生函数（HKDF）算法，参见 RFC 8613 第 3.1 节。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.3\_函数（Functions）

<a id="r_ga2e53e54122bc7c00c8bf67918617714a"></a>

```c
int coap_oscore_context_add (const struct coap_oscore_init_params *params, struct coap_oscore_context **ctx)
```

相关声明：[coap_oscore_context_add](#ga2e53e54122bc7c00c8bf67918617714a)、[coap_oscore_init_params](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md)。

添加 OSCORE 安全上下文。

<a id="r_ga7193e52c30307dcc319d9347fade7dbe"></a>

```c
int coap_oscore_context_remove (struct coap_oscore_context *ctx)
```

相关声明：[coap_oscore_context_remove](#ga7193e52c30307dcc319d9347fade7dbe)。

移除 OSCORE 安全上下文。

## 2.4\_详细说明（Detailed Documentation）

<a id="gad189c86f6afad030884f96778ed98091"></a>

### `coap_oscore_aead_alg`

```c
enum coap_oscore_aead_alg
```

```c
#include <zephyr/net/coap_oscore.h>
```

用于保护 OSCORE 消息的带关联数据认证加密（AEAD）算法，参见 RFC 8613 第 3.1 节。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `COAP_OSCORE_AEAD_AES_CCM_16_64_128` | AES-CCM 模式，使用 128 位密钥、64 位认证标签（Tag）和 13 字节随机数（Nonce）。 |

<a id="ga41bc77478b88bf7ca0f04f1ed0a2a0d1"></a>

### `coap_oscore_hkdf`

```c
enum coap_oscore_hkdf
```

```c
#include <zephyr/net/coap_oscore.h>
```

用于派生 OSCORE 密钥的基于 HMAC 的密钥派生函数（HKDF）算法，参见 RFC 8613 第 3.1 节。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `COAP_OSCORE_HKDF_SHA_256` | 基于 HMAC 的密钥派生函数（HKDF），使用 SHA-256，即 HKDF-SHA-256。 |

<a id="ga2e53e54122bc7c00c8bf67918617714a"></a>

### `coap_oscore_context_add()`

```c
int coap_oscore_context_add ( const struct coap_oscore_init_params * params, struct coap_oscore_context ** ctx )
```

```c
#include <zephyr/net/coap_oscore.h>
```

添加 OSCORE 安全上下文。

根据 `params` 派生公共上下文、发送方上下文和接收方上下文（Common, Sender and Recipient Contexts），参见 RFC 8613 第 3.2 节，并将其加入 CoAP 服务器可使用的上下文池。上下文从大小为 `CONFIG_COAP_OSCORE_MAX_CONTEXTS` 的固定池分配，并通过 `coap_oscore_context_remove()` 释放。每个上下文对应一个客户端身份，即接收方标识（Recipient ID）；要并发服务多个客户端，应为每个客户端添加一个上下文。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `params` | 派生参数（Derivation Parameters）。 |
| `ctx` | 成功时设为新创建的上下文句柄（Context Handle）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | `params` 为 `NULL`、缺少必要参数、参数大小无效，或无法派生上下文时。 |
| `-ENOTSUP` | `fresh_master_secret_salt` 为 `false`，同时禁用了 `CONFIG_COAP_OSCORE_CONTEXT_REUSE` 时。 |
| `-ENOMEM` | 没有空闲上下文槽（Context Slot）可用时。 |

**注意（Attention）**：注意（Attention）：仅在启用Kconfig选项CONFIG_COAP_OSCORE时可用。

<a id="ga7193e52c30307dcc319d9347fade7dbe"></a>

### `coap_oscore_context_remove()`

```c
int coap_oscore_context_remove ( struct coap_oscore_context * ctx)
```

```c
#include <zephyr/net/coap_oscore.h>
```

移除 OSCORE 安全上下文。

从 CoAP 服务器可使用的上下文池中移除上下文。上下文采用引用计数（Reference Counting）：若进行中的请求、活动交换或观察者（Observer）仍持有其引用，则保留上下文并返回 `-EAGAIN`。这些引用释放后应重试。传入 `NULL` 返回 `-EINVAL`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 要移除的上下文句柄（Context Handle）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EAGAIN` | 上下文正在使用，无法移除时。 |
| `-EINVAL` | `ctx` 为 `NULL` 或不是有效上下文句柄时。 |

**注意（Attention）**：注意（Attention）：仅在启用Kconfig选项CONFIG_COAP_OSCORE时可用。


## 2.5\_原页交叉引用（Cross References）

- [coap_oscore_init_params](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md)
- [RFC 8613, section-3.2](https://datatracker.ietf.org/doc/html/rfc8613#section-3.2)
- [coap_oscore_exchange](../network_application_model_reference/P011_coap_oscore_exchange_结构体.md)
- [RFC 8613, section-3.1](https://datatracker.ietf.org/doc/html/rfc8613#section-3.1)
- [zephyr/net/coap_oscore.h](../api_file_interface_reference/P009_zephyr__net__coap_oscore.h_文件参考.md)
- [CONFIG_COAP_OSCORE_MAX_CONTEXTS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_OSCORE_MAX_CONTEXTS)
- [CONFIG_COAP_OSCORE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_OSCORE)
- [CONFIG_COAP_OSCORE_CONTEXT_REUSE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_OSCORE_CONTEXT_REUSE)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggad189c86f6afad030884f96778ed98091a7e2d8a3abb742efbe6afaeee0dd80123"></a>
<a id="gga41bc77478b88bf7ca0f04f1ed0a2a0d1abd3a2ccfa28e081e9d0672bd835949bd"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_Ambiq API主题.md) · [返回大纲](大纲.md) · [下一章](P003_DHCPv4 服务器.md)
