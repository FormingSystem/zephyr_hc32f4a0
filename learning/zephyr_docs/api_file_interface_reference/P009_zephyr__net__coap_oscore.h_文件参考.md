---
id: learning.zephyr-docs.api-file-interface-reference.page-9
title: zephyr__net__coap_oscore.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/coap__oscore_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_zephyr\_\_net\_\_coap\_oscore.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/coap__oscore_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CoAP的受限RESTful环境对象安全（OSCORE）API。

<a id="details"></a>

```c
#include <stddef.h>
#include <stdint.h>
#include <stdbool.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/coap.h>
```

查看此文件的源码。

CoAP OSCORE API。此公共 API 用于创建受限 RESTful 环境对象安全（Object Security for Constrained RESTful Environments，OSCORE；RFC 8613）安全上下文（security context），并将其附加到 CoAP 客户端或服务。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.1\_数据结构（Data Structures）

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

## 9.2\_枚举（Enumerations）

<a id="r_gad189c86f6afad030884f96778ed98091"></a>

```c
enum coap_oscore_aead_alg { COAP_OSCORE_AEAD_AES_CCM_16_64_128 = 0 }
```

相关声明：[coap_oscore_aead_alg](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__oscore.html#gad189c86f6afad030884f96778ed98091)、[COAP_OSCORE_AEAD_AES_CCM_16_64_128](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__oscore.html#ggad189c86f6afad030884f96778ed98091a7e2d8a3abb742efbe6afaeee0dd80123)。

用于保护 OSCORE 消息的带关联数据认证加密（AEAD）算法，参见 RFC 8613 第 3.1 节。

<a id="r_ga41bc77478b88bf7ca0f04f1ed0a2a0d1"></a>

```c
enum coap_oscore_hkdf { COAP_OSCORE_HKDF_SHA_256 = 0 }
```

相关声明：[coap_oscore_hkdf](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__oscore.html#ga41bc77478b88bf7ca0f04f1ed0a2a0d1)、[COAP_OSCORE_HKDF_SHA_256](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__oscore.html#gga41bc77478b88bf7ca0f04f1ed0a2a0d1abd3a2ccfa28e081e9d0672bd835949bd)。

用于派生 OSCORE 密钥的基于 HMAC 的密钥派生函数（HKDF）算法，参见 RFC 8613 第 3.1 节。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.3\_函数（Functions）

<a id="r_ga2e53e54122bc7c00c8bf67918617714a"></a>

```c
int coap_oscore_context_add (const struct coap_oscore_init_params *params, struct coap_oscore_context **ctx)
```

相关声明：[coap_oscore_context_add](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__oscore.html#ga2e53e54122bc7c00c8bf67918617714a)、[coap_oscore_init_params](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md)。

添加 OSCORE 安全上下文。

<a id="r_ga7193e52c30307dcc319d9347fade7dbe"></a>

```c
int coap_oscore_context_remove (struct coap_oscore_context *ctx)
```

相关声明：[coap_oscore_context_remove](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__oscore.html#ga7193e52c30307dcc319d9347fade7dbe)。

移除 OSCORE 安全上下文。


## 9.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)
- [zephyr/net/coap.h](https://docs.zephyrproject.org/latest/doxygen/html/coap_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P108_coap_oscore.h_源码浏览.md)
- [coap_oscore_init_params](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md)
- [RFC 8613, section-3.2](https://datatracker.ietf.org/doc/html/rfc8613#section-3.2)
- [coap_oscore_exchange](../network_application_model_reference/P011_coap_oscore_exchange_结构体.md)
- [coap_oscore_aead_alg](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__oscore.html#gad189c86f6afad030884f96778ed98091)
- [COAP_OSCORE_AEAD_AES_CCM_16_64_128](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__oscore.html#ggad189c86f6afad030884f96778ed98091a7e2d8a3abb742efbe6afaeee0dd80123)
- [RFC 8613, section-3.1](https://datatracker.ietf.org/doc/html/rfc8613#section-3.1)
- [coap_oscore_hkdf](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__oscore.html#ga41bc77478b88bf7ca0f04f1ed0a2a0d1)
- [COAP_OSCORE_HKDF_SHA_256](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__oscore.html#gga41bc77478b88bf7ca0f04f1ed0a2a0d1abd3a2ccfa28e081e9d0672bd835949bd)
- [coap_oscore_context_add](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__oscore.html#ga2e53e54122bc7c00c8bf67918617714a)
- [coap_oscore_context_remove](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__oscore.html#ga7193e52c30307dcc319d9347fade7dbe)
- [RFC 8613](https://datatracker.ietf.org/doc/html/rfc8613)

<a id="header-details"></a>

---

[上一章](P008_zephyr__drivers__clock_control__clock_control_ifx.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_zephyr__bluetooth__mesh__dfu_metadata.h_文件参考.md)
