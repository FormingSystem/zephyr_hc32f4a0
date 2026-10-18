---
id: learning.zephyr-docs.api-memory-timer-topic-reference.page-11
title: 传输层安全（TLS）的凭据管理。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_传输层安全（TLS）的凭据管理。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

传输层安全（TLS）的凭据管理。

<a id="details"></a>

TLS 凭据管理（TLS Credentials Management）。起始版本（Since）：1.13。接口版本（Version）：0.8.0。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.1\_宏定义（Macros）

<a id="r_ga79f3eea68c2706edd3320822968bd696"></a>

```c
#define SEC_TAG_TLS_INVALID (-1)
```

相关声明：[SEC_TAG_TLS_INVALID](#ga79f3eea68c2706edd3320822968bd696)。

无效的安全标签（Secure Tag）值。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 11.2\_类型定义（Typedefs）

<a id="r_gaadfe9694309e473f7be74ed98dfb36d3"></a>

```c
typedef int sec_tag_t
```

相关声明：[sec_tag_t](#gaadfe9694309e473f7be74ed98dfb36d3)。

安全标签（Secure Tag），用于引用 TLS 凭据（Credential）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 11.3\_枚举（Enumerations）

<a id="r_ga3a754894d0162634b59d60e319f37cd5"></a>

```c
enum tls_credential_type { TLS_CREDENTIAL_NONE , TLS_CREDENTIAL_CA_CERTIFICATE , TLS_CREDENTIAL_PUBLIC_CERTIFICATE , TLS_CREDENTIAL_PRIVATE_KEY , TLS_CREDENTIAL_PSK , TLS_CREDENTIAL_PSK_ID , TLS_CREDENTIAL_PRIVATE_KEY_PSA }
```

相关声明：[tls_credential_type](#ga3a754894d0162634b59d60e319f37cd5)、[TLS_CREDENTIAL_NONE](#gga3a754894d0162634b59d60e319f37cd5a7009a9f266011529e64ec4e4c6692315)、[TLS_CREDENTIAL_CA_CERTIFICATE](#gga3a754894d0162634b59d60e319f37cd5adcf949c1422f4d3b38795ae40d2321d5)、[TLS_CREDENTIAL_PUBLIC_CERTIFICATE](#gga3a754894d0162634b59d60e319f37cd5acd8b96102765f7f2a83582eab80df3d8)、[TLS_CREDENTIAL_PRIVATE_KEY](#gga3a754894d0162634b59d60e319f37cd5a406e8bb1f992af5a72921f47b140840e)、[TLS_CREDENTIAL_PSK](#gga3a754894d0162634b59d60e319f37cd5accc6ad916ee6c6badafcc4c23e2a47df)、[TLS_CREDENTIAL_PSK_ID](#gga3a754894d0162634b59d60e319f37cd5a1edcd43ba510558e4b1315e1bb86560d)、[TLS_CREDENTIAL_PRIVATE_KEY_PSA](#gga3a754894d0162634b59d60e319f37cd5ae7f4b9f4ed9865678d7cbdb741ca19e1)。

TLS 凭据类型（Credential Types）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.4\_函数（Functions）

<a id="r_ga640ff6dd3eb4d5017feaab6fab2bb2f7"></a>

```c
int tls_credential_add (sec_tag_t tag, enum tls_credential_type type, const void *cred, size_t credlen)
```

相关声明：[tls_credential_add](#ga640ff6dd3eb4d5017feaab6fab2bb2f7)、[sec_tag_t](#gaadfe9694309e473f7be74ed98dfb36d3)、[tls_credential_type](#ga3a754894d0162634b59d60e319f37cd5)。

添加 TLS 凭据（Credential）。

<a id="r_gac3ac4ca887faf6c1f2ae60c6a08f8795"></a>

```c
int tls_credential_get (sec_tag_t tag, enum tls_credential_type type, void *cred, size_t *credlen)
```

相关声明：[tls_credential_get](#gac3ac4ca887faf6c1f2ae60c6a08f8795)、[sec_tag_t](#gaadfe9694309e473f7be74ed98dfb36d3)、[tls_credential_type](#ga3a754894d0162634b59d60e319f37cd5)。

获取 TLS 凭据（Credential）。

<a id="r_ga9d8b47a7a2675fb3b3c6ee346e925aca"></a>

```c
int tls_credential_delete (sec_tag_t tag, enum tls_credential_type type)
```

相关声明：[tls_credential_delete](#ga9d8b47a7a2675fb3b3c6ee346e925aca)、[sec_tag_t](#gaadfe9694309e473f7be74ed98dfb36d3)、[tls_credential_type](#ga3a754894d0162634b59d60e319f37cd5)。

删除 TLS 凭据（Credential）。

<a id="r_ga7508492d623044d33406de5abdf29216"></a>

```c
int tls_credential_expiry (sec_tag_t tag, enum tls_credential_type type, time_t *expiry)
```

相关声明：[tls_credential_expiry](#ga7508492d623044d33406de5abdf29216)、[sec_tag_t](#gaadfe9694309e473f7be74ed98dfb36d3)、[tls_credential_type](#ga3a754894d0162634b59d60e319f37cd5)、[time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)。

获取 TLS 凭据的到期时间（Expiry Time）。

## 11.5\_详细说明（Detailed Documentation）

<a id="ga79f3eea68c2706edd3320822968bd696"></a>

### `SEC_TAG_TLS_INVALID`

```c
#define SEC_TAG_TLS_INVALID (-1)
```

```c
#include <zephyr/net/tls_credentials.h>
```

无效的安全标签（Secure Tag）值。

<a id="gaadfe9694309e473f7be74ed98dfb36d3"></a>

### `sec_tag_t`

```c
typedef int sec_tag_t
```

```c
#include <zephyr/net/tls_credentials.h>
```

安全标签（Secure Tag），用于引用 TLS 凭据（Credential）。

凭据在系统中注册后，可使用安全标签（Secure Tag）引用该凭据。

**说明（Note）**：注意（Note）：某些 TLS 凭据（Credential）成对出现：`TLS_CREDENTIAL_PUBLIC_CERTIFICATE` 与 `TLS_CREDENTIAL_PRIVATE_KEY` 配对，`TLS_CREDENTIAL_PSK` 与 `TLS_CREDENTIAL_PSK_ID` 配对。在支持根据一个标签获取多个凭据的子系统中使用时，例如 TLS 套接字（TLS Socket），通常应为同一对凭据分配相同的安全标签（Secure Tag）。但请注意，某些子系统或实现可能要求每个安全标签仅对应一个凭据。负值保留供内部使用。

<a id="ga3a754894d0162634b59d60e319f37cd5"></a>

### `tls_credential_type`

```c
enum tls_credential_type
```

```c
#include <zephyr/net/tls_credentials.h>
```

TLS 凭据类型（Credential Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `TLS_CREDENTIAL_NONE` | 未指定的凭据（Unspecified Credential）。 |
| `TLS_CREDENTIAL_CA_CERTIFICATE` | 受信任的证书颁发机构证书（CA Certificate）。用于验证远程服务器的身份，配合基于证书的密码套件（Certificate-based Ciphersuite）使用。 |
| `TLS_CREDENTIAL_PUBLIC_CERTIFICATE` | 客户端或服务器的公开证书（Public Certificate）。用于注册自己的证书，应与对应的私钥（Private Key）一起注册。配合基于证书的密码套件（Certificate-based Ciphersuite）使用。 |
| `TLS_CREDENTIAL_PRIVATE_KEY` | 私钥（Private Key）。应与对应的公开证书（Public Certificate）一起注册。配合基于证书的密码套件（Certificate-based Ciphersuite）使用。 |
| `TLS_CREDENTIAL_PSK` | 预共享密钥（Pre-shared Key）。应与对应的预共享密钥标识（PSK Identity）一起注册。配合基于 PSK 的密码套件（PSK-based Ciphersuite）使用。 |
| `TLS_CREDENTIAL_PSK_ID` | 预共享密钥标识（Pre-shared Key Identity）。应与对应的预共享密钥（PSK）一起注册。配合基于 PSK 的密码套件（PSK-based Ciphersuite）使用。 |
| `TLS_CREDENTIAL_PRIVATE_KEY_PSA` | 驻留在 PSA 中的私钥（Private Key Resident in PSA）。凭据缓冲区（Credential Buffer）保存的是 `psa_key_id_t`，用于引用 PSA 中已存在的密钥，例如在设备上通过 `psa_generate_key()` 生成的密钥；其中不保存密钥材料（Key Material）本身。密钥始终留在 PSA 内：握手签名（Handshake Signature）通过 `psa_sign_hash()` 完成。应与对应的公开证书（Public Certificate）一起注册，并用本类型替代 `TLS_CREDENTIAL_PRIVATE_KEY`。 |

<a id="ga640ff6dd3eb4d5017feaab6fab2bb2f7"></a>

### `tls_credential_add()`

```c
int tls_credential_add ( sec_tag_t tag, enum tls_credential_type type, const void * cred, size_t credlen )
```

```c
#include <zephyr/net/tls_credentials.h>
```

添加 TLS 凭据（Credential）。

本函数添加一个 TLS 凭据（TLS Credential），供 TLS/DTLS 进行身份验证（Authentication）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tag` | 用于引用该凭据的安全标签（Security Tag）。 |
| `type` | TLS/DTLS 凭据类型（Credential Type）。 |
| `cred` | TLS/DTLS 凭据（Credential）。 |
| `credlen` | TLS/DTLS 凭据长度（Credential Length）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 已成功添加 TLS 凭据（TLS Credential）。 |
| `-EACCES` | 访问 TLS 凭据子系统（TLS Credential Subsystem）被拒绝。 |
| `-ENOMEM` | 内存不足，无法添加新的 TLS 凭据（TLS Credential）。 |
| `-EEXIST` | 指定标签（Tag）和类型（Type）的 TLS 凭据已存在。 |

<a id="ga9d8b47a7a2675fb3b3c6ee346e925aca"></a>

### `tls_credential_delete()`

```c
int tls_credential_delete ( sec_tag_t tag, enum tls_credential_type type )
```

```c
#include <zephyr/net/tls_credentials.h>
```

删除 TLS 凭据（Credential）。

本函数删除由安全标签（Secure Tag）`tag` 和凭据类型 `type` 标识的 TLS 凭据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tag` | 与待删除凭据对应的安全标签（Security Tag）。 |
| `type` | 待删除 TLS/DTLS 凭据的类型（Credential Type）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 已成功删除 TLS 凭据（TLS Credential）。 |
| `-EACCES` | 访问 TLS 凭据子系统（TLS Credential Subsystem）被拒绝。 |
| `-ENOENT` | 未找到请求的 TLS 凭据（TLS Credential）。 |

<a id="ga7508492d623044d33406de5abdf29216"></a>

### `tls_credential_expiry()`

```c
int tls_credential_expiry ( sec_tag_t tag, enum tls_credential_type type, time_t * expiry )
```

```c
#include <zephyr/net/tls_credentials.h>
```

获取 TLS 凭据的到期时间（Expiry Time）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tag` | TLS 凭据的安全标签（Security Tag）。 |
| `type` | TLS 凭据的类型（Credential Type）。 |
| `expiry` | 用于存储到期时间（Expiry Time）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 已成功获取 TLS 凭据的到期时间（Expiry Time）。 |
| `-EACCES` | 访问 TLS 凭据子系统（TLS Credential Subsystem）被拒绝。 |
| `-ENOENT` | 未找到请求的 TLS 凭据（TLS Credential）。 |
| `-ENOTSUP` | TLS 凭据存储（TLS Credential Storage）不支持获取到期时间（Expiry Time）。 |

<a id="gac3ac4ca887faf6c1f2ae60c6a08f8795"></a>

### `tls_credential_get()`

```c
int tls_credential_get ( sec_tag_t tag, enum tls_credential_type type, void * cred, size_t * credlen )
```

```c
#include <zephyr/net/tls_credentials.h>
```

获取 TLS 凭据（Credential）。

本函数获取已注册的 TLS 凭据，该凭据由安全标签（Secure Tag）`tag` 和凭据类型 `type` 标识。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tag` | 请求的凭据所对应的安全标签（Security Tag）。 |
| `type` | 请求的 TLS/DTLS 凭据的类型（Credential Type）。 |
| `cred` | 用于保存 TLS/DTLS 凭据的缓冲区（Buffer）。 |
| `credlen` | 输入时表示缓冲区大小（Buffer Size）；输出时表示 TLS/DTLS 凭据长度（Credential Length）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 已成功获取 TLS 凭据（TLS Credential）。 |
| `-EACCES` | 访问 TLS 凭据子系统（TLS Credential Subsystem）被拒绝。 |
| `-ENOENT` | 未找到请求的 TLS 凭据（TLS Credential）。 |
| `-EFBIG` | 提供的缓冲区无法容纳请求的 TLS 凭据。请检查 `*credlen`，获取所需大小。 |


## 11.6\_原页交叉引用（Cross References）

- [time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)
- [zephyr/net/tls_credentials.h](../api_file_service_interface_reference/P051_zephyr__net__tls_credentials.h_文件参考.md)
- [psa_key_id_t](../api_file_protocol_service_reference/P024_zephyr__psa__key_ids.h_文件参考.md#a11e986351c65bd3dc3c0fe2cd9926e4b)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga3a754894d0162634b59d60e319f37cd5a7009a9f266011529e64ec4e4c6692315"></a>
<a id="gga3a754894d0162634b59d60e319f37cd5adcf949c1422f4d3b38795ae40d2321d5"></a>
<a id="gga3a754894d0162634b59d60e319f37cd5acd8b96102765f7f2a83582eab80df3d8"></a>
<a id="gga3a754894d0162634b59d60e319f37cd5a406e8bb1f992af5a72921f47b140840e"></a>
<a id="gga3a754894d0162634b59d60e319f37cd5accc6ad916ee6c6badafcc4c23e2a47df"></a>
<a id="gga3a754894d0162634b59d60e319f37cd5a1edcd43ba510558e4b1315e1bb86560d"></a>
<a id="gga3a754894d0162634b59d60e319f37cd5ae7f4b9f4ed9865678d7cbdb741ca19e1"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P010_定时器 API（Timer APIs）.md) · [返回大纲](大纲.md)
