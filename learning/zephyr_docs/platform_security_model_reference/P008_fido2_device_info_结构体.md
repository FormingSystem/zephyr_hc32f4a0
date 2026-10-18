---
id: learning.zephyr-docs.platform-security-model-reference.page-8
title: fido2_device_info_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structfido2__device__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_fido2\_device\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structfido2__device__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

authenticatorGetInfo返回的设备信息。

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

<a id="details"></a>

authenticatorGetInfo返回的设备信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 8.1\_数据成员（Data Fields）

<a id="r_a67b8b3a2c27cafaf66c3d0ae6f339668"></a>

```c
const char * versions [4]
```

相关声明：[versions](#a67b8b3a2c27cafaf66c3d0ae6f339668)。

支持的协议版本。

<a id="r_ae3e5fadc6f5a03ce1d6782c650399c39"></a>

```c
uint8_t num_versions
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_versions](#ae3e5fadc6f5a03ce1d6782c650399c39)。

支持的版本数量。

<a id="r_a74739097a2ef4a6beeb6edfce5836884"></a>

```c
const char * extensions [8]
```

相关声明：[extensions](#a74739097a2ef4a6beeb6edfce5836884)。

支持的扩展（extensions）。

<a id="r_a12d5e2334b2608bac80175cefa117481"></a>

```c
uint8_t num_extensions
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_extensions](#a12d5e2334b2608bac80175cefa117481)。

支持的扩展数量。

<a id="r_abfab9809f2f6cb195fa232895e526d29"></a>

```c
uint8_t aaguid [16]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[aaguid](#abfab9809f2f6cb195fa232895e526d29)。

认证器证明全局唯一标识符（Authenticator Attestation GUID，AAGUID）。

<a id="r_aa69757cebdc3631d1b3c15b62d273f70"></a>

```c
uint16_t max_credential_count
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_credential_count](#aa69757cebdc3631d1b3c15b62d273f70)。

最大凭据数量。

<a id="r_a8ddee975f649f1a8c1c91022c57259ec"></a>

```c
uint16_t max_credential_id_length
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_credential_id_length](#a8ddee975f649f1a8c1c91022c57259ec)。

最大凭据 ID 长度。

<a id="r_ae0efb9db99d6d5c1575ffa0a336deab5"></a>

```c
uint16_t max_msg_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_msg_size](#ae0efb9db99d6d5c1575ffa0a336deab5)。

最大简洁二进制对象表示（CBOR）消息大小，单位为字节。

<a id="r_a45da1b425879bc623bdd7651a81b9470"></a>

```c
uint8_t transports
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[transports](#a45da1b425879bc623bdd7651a81b9470)。

支持的传输方式位掩码。

```c
struct {
```

<a id="r_ad7147f86bb55f16226c3f0159efc1a0d"></a>

```c
bool plat
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[plat](#a7f59a4d2e3fd26bd6bfc9193276816c0)。

平台设备（Platform device）。

<a id="r_a1fd3ded88aca5d9fa7ff8f8866284961"></a>

```c
bool rk
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[rk](#acc1c4bff7028f3a78d233861386bd88e)。

驻留密钥（resident key）支持。

<a id="r_a4e756ab42eb6a461a71f865936027b17"></a>

```c
bool client_pin
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[client_pin](#a1f73e8e29f134a69529fd5f4061d28db)。

支持客户端 PIN（个人识别码）。

<a id="r_ab3d3c6c9f5771bc01fd5d21b98edb5c3"></a>

```c
bool up
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[up](#a278775ff0bdc201889e104fe0b61f41d)。

用户在场（user presence）支持。

<a id="r_a5c2fce5544245870299d2775bf96589c"></a>

```c
bool uv
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[uv](#a23b57e04315b12e64a5fcfae8b3f3738)。

内置用户验证（user verification）支持。

<a id="r_ae3b5e820f15a6844c0634dcdfdc173ef"></a>

```c
bool cred_mgmt
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[cred_mgmt](#ad2c8042b987fed875fc7198f4e7c4c94)。

凭据管理（credential management）支持。

<a id="r_a9e5d6e3599cf32808c229ef506133960"></a>

```c
bool pin_uv_auth_token
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[pin_uv_auth_token](#abb11da815f9a176c8ae12c1474d1bcc7)。

支持 `pinUvAuthToken`。

<a id="r_a645339018aaf26962448fafc4d2ced87"></a>

```c
bool make_cred_uv_not_rqd
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[make_cred_uv_not_rqd](#ac0bc83f02cbf76bb5fcb2fcca33a9a3e)。

支持 `makeCredUvNotRqd`。

<a id="r_a9bac9ad8d44eecadb61c9b71ffdde695"></a>

```c
bool always_uv
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[always_uv](#ab3b443cf0183568dc4c6cb34784a5588)。

认证器始终要求用户验证（UV）。

<a id="r_a2a34abcebd2a226370e448b47340850e"></a>

```c
bool no_mc_ga_permissions_with_client_pin
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[no_mc_ga_permissions_with_client_pin](#ac2c2d357d5a472b7164378aa097c86f9)。

仅在存在 `clientPin` 时有效。

<a id="r_af127645cf37845b41479e3a84941cf67"></a>

```c
} options
```

相关声明：[options](#af127645cf37845b41479e3a84941cf67)。

客户端到认证器协议（CTAP）2.1 选项映射（Options Map）。

<a id="r_abd1b7b2b922ddae9d89ccf10cc679ad8"></a>

```c
uint32_t firmware_version
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[firmware_version](#abd1b7b2b922ddae9d89ccf10cc679ad8)。

固件版本（Firmware Version）。

<a id="r_a9a8944dc4fb8b56aa8bf94077c8663fa"></a>

```c
uint8_t pin_uv_auth_protocols [2]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pin_uv_auth_protocols](#a9a8944dc4fb8b56aa8bf94077c8663fa)。

支持的 PIN/用户验证（UV）身份验证协议版本。

<a id="r_aa788eed12e5e1629ece697ea372ee5a6"></a>

```c
uint8_t num_pin_uv_auth_protocols
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_pin_uv_auth_protocols](#aa788eed12e5e1629ece697ea372ee5a6)。

支持的 PIN/UV 身份验证协议数量。

<a id="r_aa72be5c8dc8d34043467c91526bdb93a"></a>

```c
uint8_t pin_retries
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pin_retries](#aa72be5c8dc8d34043467c91526bdb93a)。

剩余 PIN 重试次数。

<a id="r_a1f9daa2e0dfb4b2a9caf79b5a478f7c8"></a>

```c
uint8_t min_pin_length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[min_pin_length](#a1f9daa2e0dfb4b2a9caf79b5a478f7c8)。

当前最小 PIN 长度。

## 8.2\_详细说明（Detailed Documentation）

<a id="abfab9809f2f6cb195fa232895e526d29"></a>

### `aaguid`

```c
uint8_t fido2_device_info::aaguid[16]
```

认证器证明全局唯一标识符（Authenticator Attestation GUID，AAGUID）。

<a id="ab3b443cf0183568dc4c6cb34784a5588"></a>

### `always_uv`

```c
bool fido2_device_info::always_uv
```

认证器始终要求用户验证（UV）。

<a id="a1f73e8e29f134a69529fd5f4061d28db"></a>

### `client_pin`

```c
bool fido2_device_info::client_pin
```

支持客户端 PIN（个人识别码）。

<a id="ad2c8042b987fed875fc7198f4e7c4c94"></a>

### `cred_mgmt`

```c
bool fido2_device_info::cred_mgmt
```

凭据管理（credential management）支持。

<a id="a74739097a2ef4a6beeb6edfce5836884"></a>

### `extensions`

```c
const char* fido2_device_info::extensions[8]
```

支持的扩展（extensions）。

<a id="abd1b7b2b922ddae9d89ccf10cc679ad8"></a>

### `firmware_version`

```c
uint32_t fido2_device_info::firmware_version
```

固件版本（Firmware Version）。

<a id="ac0bc83f02cbf76bb5fcb2fcca33a9a3e"></a>

### `make_cred_uv_not_rqd`

```c
bool fido2_device_info::make_cred_uv_not_rqd
```

支持 `makeCredUvNotRqd`。

<a id="aa69757cebdc3631d1b3c15b62d273f70"></a>

### `max_credential_count`

```c
uint16_t fido2_device_info::max_credential_count
```

最大凭据数量。

<a id="a8ddee975f649f1a8c1c91022c57259ec"></a>

### `max_credential_id_length`

```c
uint16_t fido2_device_info::max_credential_id_length
```

最大凭据 ID 长度。

<a id="ae0efb9db99d6d5c1575ffa0a336deab5"></a>

### `max_msg_size`

```c
uint16_t fido2_device_info::max_msg_size
```

最大简洁二进制对象表示（CBOR）消息大小，单位为字节。

<a id="a1f9daa2e0dfb4b2a9caf79b5a478f7c8"></a>

### `min_pin_length`

```c
uint8_t fido2_device_info::min_pin_length
```

当前最小 PIN 长度。

<a id="ac2c2d357d5a472b7164378aa097c86f9"></a>

### `no_mc_ga_permissions_with_client_pin`

```c
bool fido2_device_info::no_mc_ga_permissions_with_client_pin
```

仅在存在 `clientPin` 时有效。

<a id="a12d5e2334b2608bac80175cefa117481"></a>

### `num_extensions`

```c
uint8_t fido2_device_info::num_extensions
```

支持的扩展数量。

<a id="aa788eed12e5e1629ece697ea372ee5a6"></a>

### `num_pin_uv_auth_protocols`

```c
uint8_t fido2_device_info::num_pin_uv_auth_protocols
```

支持的 PIN/UV 身份验证协议数量。

<a id="ae3e5fadc6f5a03ce1d6782c650399c39"></a>

### `num_versions`

```c
uint8_t fido2_device_info::num_versions
```

支持的版本数量。

<a id="af127645cf37845b41479e3a84941cf67"></a>

### `[struct]`

```c
struct { ... } fido2_device_info::options
```

客户端到认证器协议（CTAP）2.1 选项映射（Options Map）。

<a id="aa72be5c8dc8d34043467c91526bdb93a"></a>

### `pin_retries`

```c
uint8_t fido2_device_info::pin_retries
```

剩余 PIN 重试次数。

<a id="a9a8944dc4fb8b56aa8bf94077c8663fa"></a>

### `pin_uv_auth_protocols`

```c
uint8_t fido2_device_info::pin_uv_auth_protocols[2]
```

支持的 PIN/用户验证（UV）身份验证协议版本。

<a id="abb11da815f9a176c8ae12c1474d1bcc7"></a>

### `pin_uv_auth_token`

```c
bool fido2_device_info::pin_uv_auth_token
```

支持 `pinUvAuthToken`。

<a id="a7f59a4d2e3fd26bd6bfc9193276816c0"></a>

### `plat`

```c
bool fido2_device_info::plat
```

平台设备（Platform device）。

<a id="acc1c4bff7028f3a78d233861386bd88e"></a>

### `rk`

```c
bool fido2_device_info::rk
```

驻留密钥（resident key）支持。

<a id="a45da1b425879bc623bdd7651a81b9470"></a>

### `transports`

```c
uint8_t fido2_device_info::transports
```

支持的传输方式位掩码。

<a id="a278775ff0bdc201889e104fe0b61f41d"></a>

### `up`

```c
bool fido2_device_info::up
```

用户在场（user presence）支持。

<a id="a23b57e04315b12e64a5fcfae8b3f3738"></a>

### `uv`

```c
bool fido2_device_info::uv
```

内置用户验证（user verification）支持。

<a id="a67b8b3a2c27cafaf66c3d0ae6f339668"></a>

### `versions`

```c
const char* fido2_device_info::versions[4]
```

支持的协议版本。

本数据类型文档由以下文件生成：

- `zephyr/authentication/fido2/fido2_types.h`

## 8.3\_原页交叉引用（Cross References）

- [zephyr/authentication/fido2/fido2_types.h](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P007_fido2_credential_结构体.md) · [返回大纲](大纲.md) · [下一章](P009_fido2_storage_api_结构体.md)
