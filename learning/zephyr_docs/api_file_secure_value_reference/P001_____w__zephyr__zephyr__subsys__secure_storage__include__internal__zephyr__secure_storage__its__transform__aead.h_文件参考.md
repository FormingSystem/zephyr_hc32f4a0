---
id: learning.zephyr-docs.api-file-secure-value-reference.page-1
title: ____w__zephyr__zephyr__subsys__secure_storage__include__internal__zephyr__secure_storage__its__transform__aead.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/aead_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_\_\_\_\_w\_\_zephyr\_\_zephyr\_\_subsys\_\_secure\_storage\_\_include\_\_internal\_\_zephyr\_\_secure\_storage\_\_its\_\_transform\_\_aead.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/aead_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

带关联数据的认证加密内部可信存储（AEAD ITS）变换模块API。

<a id="details"></a>

```c
#include <zephyr/secure_storage/its/common.h>
#include <psa/crypto_types.h>
```

查看此文件的源码。

内部可信存储（ITS）变换模块的带关联数据的认证加密（AEAD）API。此头文件声明的函数允许定制 ITS 变换模块的 AEAD 实现。除 AEAD ITS 变换模块本身外，不应直接调用这些函数。为其中一个或多个函数提供自定义实现时，即使用 `CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_.*_CUSTOM`，可以且必须包含此头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.1\_宏定义（Macros）

<a id="r_af3d68621e41397a71d396633870cac48"></a>

```c
#define SECURE_STORAGE_ITS_TRANSFORM_AEAD_TAG_SIZE
```

相关声明：[SECURE_STORAGE_ITS_TRANSFORM_AEAD_TAG_SIZE](#af3d68621e41397a71d396633870cac48)。

ITS 变换的 AEAD 认证标签大小（Tag Size）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.2\_函数（Functions）

<a id="r_a59a656fec3b4347c2bd6ac4843877856"></a>

```c
psa_status_t secure_storage_its_transform_aead_crypt (psa_key_usage_t operation, secure_storage_its_uid_t uid, const uint8_t nonce[static CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_SIZE], size_t add_data_len, const uint8_t *add_data, size_t input_len, const uint8_t *input, size_t output_size, uint8_t *output, size_t *output_len)
```

相关声明：[psa_status_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9)、[secure_storage_its_transform_aead_crypt](#a59a656fec3b4347c2bd6ac4843877856)、[secure_storage_its_uid_t](../platform_security_model_reference/P053_secure_storage_its_uid_t_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

加密或解密 ITS 条目（Entry）。

<a id="r_abf498c228e9c8d6f32432d859b5d225e"></a>

```c
void secure_storage_its_transform_aead_get_scheme (psa_key_type_t *key_type, psa_algorithm_t *alg)
```

相关声明：[secure_storage_its_transform_aead_get_scheme](#abf498c228e9c8d6f32432d859b5d225e)。

返回 AEAD 操作使用的密钥类型（Key Type）和算法（Algorithm）。

<a id="r_a2a8cf814d206a63fd4c850da478b0077"></a>

```c
psa_status_t secure_storage_its_transform_aead_get_key (secure_storage_its_uid_t uid, uint8_t key[static CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_SIZE])
```

相关声明：[psa_status_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9)、[secure_storage_its_transform_aead_get_key](#a2a8cf814d206a63fd4c850da478b0077)、[secure_storage_its_uid_t](../platform_security_model_reference/P053_secure_storage_its_uid_t_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

返回 ITS 条目的 AEAD 操作使用的加密密钥（Encryption Key）。

<a id="r_a2d29f8a15b7314e1b2211bbb93d5a1b2"></a>

```c
psa_status_t secure_storage_its_transform_aead_get_nonce (uint8_t nonce[static CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_SIZE])
```

相关声明：[psa_status_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9)、[secure_storage_its_transform_aead_get_nonce](#a2d29f8a15b7314e1b2211bbb93d5a1b2)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

为 AEAD 操作生成一次性数值（Nonce）。

## 1.3\_详细说明（Detailed Documentation）

<a id="af3d68621e41397a71d396633870cac48"></a>

### `SECURE_STORAGE_ITS_TRANSFORM_AEAD_TAG_SIZE`

```c
#define SECURE_STORAGE_ITS_TRANSFORM_AEAD_TAG_SIZE
```

展开值（Value）：

```c
(CONFIG_SECURE_STORAGE_ITS_TRANSFORM_OUTPUT_OVERHEAD   \
 - CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_SIZE)
```

ITS 变换的 AEAD 认证标签大小（Tag Size）。

<a id="a59a656fec3b4347c2bd6ac4843877856"></a>

### `secure_storage_its_transform_aead_crypt()`

```c
psa_status_t secure_storage_its_transform_aead_crypt ( psa_key_usage_t operation, secure_storage_its_uid_t uid, const uint8_t nonce[static CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_SIZE], size_t add_data_len, const uint8_t * add_data, size_t input_len, const uint8_t * input, size_t output_size, uint8_t * output, size_t * output_len )
```

加密或解密 ITS 条目（Entry）。

加密时，`output_len` 必须恰好等于 `input_len` 加上认证标签大小（Tag Size）；标签大小为 `CONFIG_SECURE_STORAGE_ITS_TRANSFORM_OUTPUT_OVERHEAD` 减去 `CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_SIZE`。解密时必须去除同样大小的扩展部分。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] operation` | 要执行的操作（Operation），为 `PSA_KEY_USAGE_{ENCRYPT,DECRYPT}`。 |
| `[in] uid` | 要处理的 ITS 条目的唯一标识符（UID）。 |
| `[in] nonce` | AEAD 操作使用的一次性数值（Nonce）。 |
| `[in] add_data_len` | `add_data` 的大小，单位为字节。 |
| `[in] add_data` | 要认证的附加数据（Additional Data）。 |
| `[in] input_len` | `input` 的大小，单位为字节。 |
| `[in] input` | 加密时的明文（Plaintext），或解密时的密文（Ciphertext）。 |
| `[in] output_size` | 输出缓冲区大小（Output Buffer Size），单位为字节。 |
| `[out] output` | 加密时的密文（Ciphertext），或解密时的明文（Plaintext）。 |
| `[out] output_len` | 成功时，`output` 的大小，单位为字节。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `PSA_SUCCESS`，其他值均表示失败。

<a id="a2a8cf814d206a63fd4c850da478b0077"></a>

### `secure_storage_its_transform_aead_get_key()`

```c
psa_status_t secure_storage_its_transform_aead_get_key ( secure_storage_its_uid_t uid, uint8_t key[static CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_SIZE] )
```

返回 ITS 条目的 AEAD 操作使用的加密密钥（Encryption Key）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uid` | 使用此密钥的 ITS 条目的唯一标识符（UID）。 |
| `[out] key` | 加密密钥（Encryption Key）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `PSA_SUCCESS`，其他值均表示失败。

<a id="a2d29f8a15b7314e1b2211bbb93d5a1b2"></a>

### `secure_storage_its_transform_aead_get_nonce()`

```c
psa_status_t secure_storage_its_transform_aead_get_nonce ( uint8_t nonce[static CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_SIZE])
```

为 AEAD 操作生成一次性数值（Nonce）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[out] nonce` | 生成的一次性数值（Nonce）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `PSA_SUCCESS`，其他值均表示失败。

<a id="abf498c228e9c8d6f32432d859b5d225e"></a>

### `secure_storage_its_transform_aead_get_scheme()`

```c
void secure_storage_its_transform_aead_get_scheme ( psa_key_type_t * key_type, psa_algorithm_t * alg )
```

返回 AEAD 操作使用的密钥类型（Key Type）和算法（Algorithm）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[out] key_type` | 要使用的密钥类型（Key Type）。 |
| `[out] alg` | 要使用的算法（Algorithm）。 |


## 1.4\_原页交叉引用（Cross References）

- [zephyr/secure_storage/its/common.h](../api_source_reference/P843_common.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P004_aead.h_源码浏览.md)
- [psa_status_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9)
- [secure_storage_its_uid_t](../platform_security_model_reference/P053_secure_storage_its_uid_t_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_.*_CUSTOM](https://docs.zephyrproject.org/latest/kconfig.html#!CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_.%2A_CUSTOM)
- [PSA_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a4cc859e2c66ca381c7418db3527a65e1)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__dt-bindings__gpio__arduino-header-r3.h_文件参考.md)
