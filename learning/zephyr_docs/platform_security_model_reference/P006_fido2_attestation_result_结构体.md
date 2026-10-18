---
id: learning.zephyr-docs.platform-security-model-reference.page-6
title: fido2_attestation_result_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structfido2__attestation__result.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_fido2\_attestation\_result\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structfido2__attestation__result.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

证明回调（Attestation Callback）产生的证明结果。

```c
#include <zephyr/authentication/fido2/fido2_attestation.h>
```

<a id="details"></a>

证明回调（Attestation Callback）产生的证明结果。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 6.1\_数据成员（Data Fields）

<a id="r_a54faed1a597ea39e5938fa521388fd6f"></a>

```c
const char * fmt
```

相关声明：[fmt](#a54faed1a597ea39e5938fa521388fd6f)。

证明声明（attestation statement）的格式标识符，例如 `"packed"`、`"none"`。

<a id="r_a2283601407953326d34afbc7795202c4"></a>

```c
int32_t alg
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[alg](#a2283601407953326d34afbc7795202c4)。

CBOR 对象签名和加密（COSE）算法标识符，例如 -7 表示 ES256。

<a id="r_a64a5324c4cead032417560df0692004b"></a>

```c
const uint8_t * sig
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sig](#a64a5324c4cead032417560df0692004b)。

证明签名（Attestation signature）。

<a id="r_a4a387ed4358d5aa66c91adc3a15dd902"></a>

```c
size_t sig_len
```

相关声明：[sig_len](#a4a387ed4358d5aa66c91adc3a15dd902)。

`sig` 的长度，单位为字节。

<a id="r_a9c90db221f5dbc7371f526b8381fa091"></a>

```c
const uint8_t * x5c
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[x5c](#a9c90db221f5dbc7371f526b8381fa091)。

用于 `x5c` 数组、采用可辨别编码规则（DER）编码的证明证书（attestation certificate）。

<a id="r_a7be57d42d8c552659f59f8d49349f58f"></a>

```c
size_t x5c_len
```

相关声明：[x5c_len](#a7be57d42d8c552659f59f8d49349f58f)。

`x5c` 的长度，单位为字节。

## 6.2\_详细说明（Detailed Documentation）

<a id="a2283601407953326d34afbc7795202c4"></a>

### `alg`

```c
int32_t fido2_attestation_result::alg
```

CBOR 对象签名和加密（COSE）算法标识符，例如 -7 表示 ES256。

设为 0 可省略。

<a id="a54faed1a597ea39e5938fa521388fd6f"></a>

### `fmt`

```c
const char* fido2_attestation_result::fmt
```

证明声明（attestation statement）的格式标识符，例如 `"packed"`、`"none"`。

<a id="a64a5324c4cead032417560df0692004b"></a>

### `sig`

```c
const uint8_t* fido2_attestation_result::sig
```

证明签名（Attestation signature）。

设为 `NULL` 可省略。

<a id="a4a387ed4358d5aa66c91adc3a15dd902"></a>

### `sig_len`

```c
size_t fido2_attestation_result::sig_len
```

`sig` 的长度，单位为字节。

<a id="a9c90db221f5dbc7371f526b8381fa091"></a>

### `x5c`

```c
const uint8_t* fido2_attestation_result::x5c
```

用于 `x5c` 数组、采用可辨别编码规则（DER）编码的证明证书（attestation certificate）。

<a id="a7be57d42d8c552659f59f8d49349f58f"></a>

### `x5c_len`

```c
size_t fido2_attestation_result::x5c_len
```

`x5c` 的长度，单位为字节。

不存在时为 0。

本数据类型文档由以下文件生成：

- `zephyr/authentication/fido2/fido2_attestation.h`

## 6.3\_原页交叉引用（Cross References）

- [zephyr/authentication/fido2/fido2_attestation.h](https://docs.zephyrproject.org/latest/doxygen/html/fido2__attestation_8h_source.html)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P005_eic_config_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P007_fido2_credential_结构体.md)
