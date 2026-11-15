---
id: learning.zephyr-docs.api-buffer-paging-topic-reference.page-3
title: 密码学（Cryptography）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__crypto.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_密码学（Cryptography）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__crypto.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

密码学（Cryptography）

<a id="details"></a>

密码学（Cryptography）。引入版本（Since）：1.8；API 版本（Version）：1.0.0。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.1\_函数（Functions）

<a id="r_ga2c85d3563547017ae97f22993272fb29"></a>

```c
int bt_rand (void *buf, size_t len)
```

相关声明：[bt_rand](#ga2c85d3563547017ae97f22993272fb29)。

生成随机数据（random data）。

<a id="r_ga54d34c154deaf5b6f1523de15ddec18f"></a>

```c
int bt_encrypt_le (const uint8_t key[16], const uint8_t plaintext[16], uint8_t enc_data[16])
```

相关声明：[bt_encrypt_le](#ga54d34c154deaf5b6f1523de15ddec18f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

对小端序（little-endian）数据进行 AES 加密。

<a id="r_gab93f5833e39b39e388bf40ba5c60d60f"></a>

```c
int bt_encrypt_be (const uint8_t key[16], const uint8_t plaintext[16], uint8_t enc_data[16])
```

相关声明：[bt_encrypt_be](#gab93f5833e39b39e388bf40ba5c60d60f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

对大端序（big-endian）数据进行 AES 加密。

<a id="r_ga413a29883453982f0da13590dd493166"></a>

```c
int bt_ccm_decrypt (const uint8_t key[16], uint8_t nonce[13], const uint8_t *enc_data, size_t len, const uint8_t *aad, size_t aad_len, uint8_t *plaintext, size_t mic_size)
```

相关声明：[bt_ccm_decrypt](#ga413a29883453982f0da13590dd493166)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

使用 AES-CCM 解密大端序数据。

<a id="r_ga7235be4697031ca6a0e535bdd707d3e1"></a>

```c
int bt_ccm_encrypt (const uint8_t key[16], uint8_t nonce[13], const uint8_t *plaintext, size_t len, const uint8_t *aad, size_t aad_len, uint8_t *enc_data, size_t mic_size)
```

相关声明：[bt_ccm_encrypt](#ga7235be4697031ca6a0e535bdd707d3e1)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

使用 AES-CCM 加密大端序数据。

## 3.2\_详细说明（Detailed Documentation）

<a id="ga413a29883453982f0da13590dd493166"></a>

### `bt_ccm_decrypt()`

```c
int bt_ccm_decrypt ( const uint8_t key[16], uint8_t nonce[13], const uint8_t * enc_data, size_t len, const uint8_t * aad, size_t aad_len, uint8_t * plaintext, size_t mic_size )
```

```c
#include <zephyr/bluetooth/crypto.h>
```

使用 AES-CCM 解密大端序数据。

使用 AES-CCM 对 enc_data 进行解密和认证，算法见 https://tools.ietf.org/html/rfc3610 。

假定消息完整性校验码（Message Integrity Check，MIC）紧跟在密文之后。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `key` | 128 位密钥（Key），最高有效字节优先（MS Byte First） |
| `nonce` | 13 字节一次性数值（Nonce），最高有效字节优先（MS Byte First） |
| `enc_data` | 加密数据（Encrypted Data） |
| `len` | 加密数据长度 |
| `aad` | 附加认证数据（Additional Authenticated Data） |
| `aad_len` | 附加认证数据长度 |
| `plaintext` | 用于存放结果的明文缓冲区（Plaintext Buffer） |
| `mic_size` | 尾部消息完整性校验码（MIC）的大小，单位为字节 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功解密数据。 |
| `-EINVAL` | 参数无效（Invalid Parameters）。 |
| `-EBADMSG` | 认证失败（Authentication Failed）。 |

<a id="ga7235be4697031ca6a0e535bdd707d3e1"></a>

### `bt_ccm_encrypt()`

```c
int bt_ccm_encrypt ( const uint8_t key[16], uint8_t nonce[13], const uint8_t * plaintext, size_t len, const uint8_t * aad, size_t aad_len, uint8_t * enc_data, size_t mic_size )
```

```c
#include <zephyr/bluetooth/crypto.h>
```

使用 AES-CCM 加密大端序数据。

使用 AES-CCM 对明文加密并生成消息完整性校验码（MIC），算法见 https://tools.ietf.org/html/rfc3610 。

将消息完整性校验码（MIC）紧接在密文之后。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `key` | 128 位密钥（Key），最高有效字节优先（MS Byte First） |
| `nonce` | 13 字节一次性数值（Nonce），最高有效字节优先（MS Byte First） |
| `plaintext` | 待加密的明文缓冲区（Plaintext Buffer） |
| `len` | 加密数据长度 |
| `aad` | 附加认证数据（Additional Authenticated Data） |
| `aad_len` | 附加认证数据长度 |
| `enc_data` | 用于存放加密数据的缓冲区 |
| `mic_size` | 尾部消息完整性校验码（MIC）的大小，单位为字节 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功加密数据。 |
| `-EINVAL` | 参数无效（Invalid Parameters）。 |

<a id="gab93f5833e39b39e388bf40ba5c60d60f"></a>

### `bt_encrypt_be()`

```c
int bt_encrypt_be ( const uint8_t key[16], const uint8_t plaintext[16], uint8_t enc_data[16] )
```

```c
#include <zephyr/bluetooth/crypto.h>
```

对大端序（big-endian）数据进行 AES 加密。

AES 加密辅助接口（Encrypt Helper）请求蓝牙控制器自身的硬件使用指定密钥加密明文，并返回加密数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `key` | 用于加密明文的 128 位密钥（Key），最高有效字节优先（MS Byte First） |
| `plaintext` | 待加密的 128 位明文数据块（Plaintext Data Block），最高有效字节优先（MS Byte First） |
| `enc_data` | 128 位加密数据块（Encrypted Data Block），最高有效字节优先（MS Byte First） |

**返回（Returns）**：返回值（Returns）：成功返回 0，否则返回错误码。

<a id="ga54d34c154deaf5b6f1523de15ddec18f"></a>

### `bt_encrypt_le()`

```c
int bt_encrypt_le ( const uint8_t key[16], const uint8_t plaintext[16], uint8_t enc_data[16] )
```

```c
#include <zephyr/bluetooth/crypto.h>
```

对小端序（little-endian）数据进行 AES 加密。

AES 加密辅助接口（Encrypt Helper）请求蓝牙控制器自身的硬件使用指定密钥加密明文，并返回加密数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `key` | 用于加密明文的 128 位密钥（Key），最低有效字节优先（LS Byte First） |
| `plaintext` | 待加密的 128 位明文数据块（Plaintext Data Block），最低有效字节优先（LS Byte First） |
| `enc_data` | 128 位加密数据块（Encrypted Data Block），最低有效字节优先（LS Byte First） |

**返回（Returns）**：返回值（Returns）：成功返回 0，否则返回错误码。

<a id="ga2c85d3563547017ae97f22993272fb29"></a>

### `bt_rand()`

```c
int bt_rand ( void * buf, size_t len )
```

```c
#include <zephyr/bluetooth/crypto.h>
```

生成随机数据（random data）。

利用蓝牙控制器自身随机数发生器（Random Number Generator，RNG）的随机数生成辅助接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 用于填入随机数据的缓冲区 |
| `len` | 要生成的随机数据长度 |

**返回（Returns）**：返回值（Returns）：成功返回 0，否则返回错误码；协议错误返回正值，协议栈内部错误返回负的 POSIX 错误码。


## 3.3\_原页交叉引用（Cross References）

- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [zephyr/bluetooth/crypto.h](../api_file_interface_reference/P005_zephyr__bluetooth__crypto.h_文件参考.md)
- [https://tools.ietf.org/html/rfc3610](https://tools.ietf.org/html/rfc3610)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P002_数据缓冲区（Data buffers）.md) · [返回大纲](大纲.md) · [下一章](P004_蓝牙HCI数据包辅助接口（Packet Helpers）。.md)
