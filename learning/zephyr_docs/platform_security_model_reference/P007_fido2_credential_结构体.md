---
id: learning.zephyr-docs.platform-security-model-reference.page-7
title: fido2_credential_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structfido2__credential.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_fido2\_credential\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structfido2__credential.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

已存储的FIDO2凭据（Credential）。

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

<a id="details"></a>

已存储的FIDO2凭据（Credential）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 7.1\_数据成员（Data Fields）

<a id="r_ae959db127d978174e796eb61566b3e1f"></a>

```c
uint8_t id [128]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[id](#ae959db127d978174e796eb61566b3e1f)。

凭据标识符（Credential identifier）。

<a id="r_aaf5c0b6a289e51c49e5c9e065fb28a7a"></a>

```c
uint16_t id_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[id_len](#aaf5c0b6a289e51c49e5c9e065fb28a7a)。

凭据标识符长度。

<a id="r_a6a0e84bb3432eaccdd85a7b9d72ed91d"></a>

```c
uint8_t rp_id_hash [32]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rp_id_hash](#a6a0e84bb3432eaccdd85a7b9d72ed91d)。

依赖方（relying party）ID 的 SHA-256 哈希。

<a id="r_af523edcf94f7a9f9cbbd7ea87bbe673a"></a>

```c
char rp_id [128]
```

相关声明：[rp_id](#af523edcf94f7a9f9cbbd7ea87bbe673a)。

依赖方标识符（relying party identifier）。

<a id="r_a194b53ed392542e1214e4289fe76d033"></a>

```c
char rp_name [64]
```

相关声明：[rp_name](#a194b53ed392542e1214e4289fe76d033)。

依赖方显示名称。

<a id="r_ae95bda862fcc760ffa5d723dfb3ff8aa"></a>

```c
char user_name [64]
```

相关声明：[user_name](#ae95bda862fcc760ffa5d723dfb3ff8aa)。

用户账户名称。

<a id="r_a2a097ffa153fc969e73850627654c97f"></a>

```c
char user_display_name [64]
```

相关声明：[user_display_name](#a2a097ffa153fc969e73850627654c97f)。

用户显示名称。

<a id="r_a0d3ac4d5515fae39f06c13c37aa385f7"></a>

```c
uint8_t user_id [64]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[user_id](#a0d3ac4d5515fae39f06c13c37aa385f7)。

用户句柄（User handle）。

<a id="r_af2e3794720dbad041de08aaba6dbd925"></a>

```c
uint16_t user_id_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[user_id_len](#af2e3794720dbad041de08aaba6dbd925)。

用户句柄长度。

<a id="r_aad709e654b5a0ebb6a2ee7d1a1e1c6a2"></a>

```c
uint32_t key_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[key_id](#aad709e654b5a0ebb6a2ee7d1a1e1c6a2)。

此凭据的 PSA Crypto 密钥标识符（key identifier）。

<a id="r_a1dde5d1541f18260df49175047c883df"></a>

```c
uint32_t sign_count
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[sign_count](#a1dde5d1541f18260df49175047c883df)。

签名计数器（Signature counter）。

<a id="r_a8951d380f675d378e7fcb584f87561cd"></a>

```c
uint32_t extensions
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[extensions](#a8951d380f675d378e7fcb584f87561cd)。

凭据扩展（credential extensions）位掩码，例如下列扩展。

<a id="r_a71a46e60f2e8204a83aaecd2dfb44e40"></a>

```c
int32_t algorithm
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[algorithm](#a71a46e60f2e8204a83aaecd2dfb44e40)。

COSE 算法标识符。

<a id="r_a7b7c2b9ba8ea5dea3428132e5e0462b7"></a>

```c
bool discoverable
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[discoverable](#a7b7c2b9ba8ea5dea3428132e5e0462b7)。

可发现凭据（discoverable credential），也称驻留凭据（resident credential）。

<a id="r_a5472886ee94fd507f4facf8681b62882"></a>

```c
uint8_t cred_protect
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cred_protect](#a5472886ee94fd507f4facf8681b62882)。

凭据保护级别（credential protection level）。

## 7.2\_详细说明（Detailed Documentation）

<a id="a71a46e60f2e8204a83aaecd2dfb44e40"></a>

### `algorithm`

```c
int32_t fido2_credential::algorithm
```

COSE 算法标识符。

<a id="a5472886ee94fd507f4facf8681b62882"></a>

### `cred_protect`

```c
uint8_t fido2_credential::cred_protect
```

凭据保护级别（credential protection level）。

<a id="a7b7c2b9ba8ea5dea3428132e5e0462b7"></a>

### `discoverable`

```c
bool fido2_credential::discoverable
```

可发现凭据（discoverable credential），也称驻留凭据（resident credential）。

<a id="a8951d380f675d378e7fcb584f87561cd"></a>

### `extensions`

```c
uint32_t fido2_credential::extensions
```

凭据扩展（credential extensions）位掩码，例如下列扩展。

`hmac-secret`、`largeBlob`。

<a id="ae959db127d978174e796eb61566b3e1f"></a>

### `id`

```c
uint8_t fido2_credential::id[128]
```

凭据标识符（Credential identifier）。

<a id="aaf5c0b6a289e51c49e5c9e065fb28a7a"></a>

### `id_len`

```c
uint16_t fido2_credential::id_len
```

凭据标识符长度。

<a id="aad709e654b5a0ebb6a2ee7d1a1e1c6a2"></a>

### `key_id`

```c
uint32_t fido2_credential::key_id
```

此凭据的 PSA Crypto 密钥标识符（key identifier）。

<a id="af523edcf94f7a9f9cbbd7ea87bbe673a"></a>

### `rp_id`

```c
char fido2_credential::rp_id[128]
```

依赖方标识符（relying party identifier）。

<a id="a6a0e84bb3432eaccdd85a7b9d72ed91d"></a>

### `rp_id_hash`

```c
uint8_t fido2_credential::rp_id_hash[32]
```

依赖方（relying party）ID 的 SHA-256 哈希。

<a id="a194b53ed392542e1214e4289fe76d033"></a>

### `rp_name`

```c
char fido2_credential::rp_name[64]
```

依赖方显示名称。

<a id="a1dde5d1541f18260df49175047c883df"></a>

### `sign_count`

```c
uint32_t fido2_credential::sign_count
```

签名计数器（Signature counter）。

<a id="a2a097ffa153fc969e73850627654c97f"></a>

### `user_display_name`

```c
char fido2_credential::user_display_name[64]
```

用户显示名称。

<a id="a0d3ac4d5515fae39f06c13c37aa385f7"></a>

### `user_id`

```c
uint8_t fido2_credential::user_id[64]
```

用户句柄（User handle）。

<a id="af2e3794720dbad041de08aaba6dbd925"></a>

### `user_id_len`

```c
uint16_t fido2_credential::user_id_len
```

用户句柄长度。

<a id="ae95bda862fcc760ffa5d723dfb3ff8aa"></a>

### `user_name`

```c
char fido2_credential::user_name[64]
```

用户账户名称。

本数据类型文档由以下文件生成：

- `zephyr/authentication/fido2/fido2_types.h`

## 7.3\_原页交叉引用（Cross References）

- [zephyr/authentication/fido2/fido2_types.h](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P006_fido2_attestation_result_结构体.md) · [返回大纲](大纲.md) · [下一章](P008_fido2_device_info_结构体.md)
