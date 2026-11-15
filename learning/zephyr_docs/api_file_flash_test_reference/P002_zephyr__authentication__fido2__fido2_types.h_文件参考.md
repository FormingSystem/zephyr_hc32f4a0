---
id: learning.zephyr-docs.api-file-flash-test-reference.page-2
title: zephyr__authentication__fido2__fido2_types.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr\_\_authentication\_\_fido2\_\_fido2\_types.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

FIDO2共享类型定义（Shared Type Definitions）。

<a id="details"></a>

```c
#include <stddef.h>
#include <stdint.h>
#include <stdbool.h>
#include <zephyr/sys/util.h>
```

查看此文件的源码。

FIDO2共享类型定义（Shared Type Definitions）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_fido2_5Fcredential"></a>

```c
struct fido2_credential
```

相关声明：[fido2_credential](../platform_security_model_reference/P007_fido2_credential_结构体.md)。

已存储的FIDO2凭据（Credential）。

<a id="r_fido2_5Fdevice_5Finfo"></a>

```c
struct fido2_device_info
```

相关声明：[fido2_device_info](../platform_security_model_reference/P008_fido2_device_info_结构体.md)。

authenticatorGetInfo返回的设备信息。

<a id="r_ga7ff8f1d8d389b44e2a656b3ebe20f778"></a>

```c
#define FIDO2_CREDENTIAL_ID_MAX_SIZE 128
```

相关声明：[FIDO2_CREDENTIAL_ID_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga7ff8f1d8d389b44e2a656b3ebe20f778)。

FIDO2 共享类型（Shared Types）。

<a id="r_ga57628d326e2f62b318908af69485dbb8"></a>

```c
#define FIDO2_RP_ID_MAX_LEN 128
```

相关声明：[FIDO2_RP_ID_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga57628d326e2f62b318908af69485dbb8)。

依赖方标识符（Relying Party ID）的最大长度。

<a id="r_ga99da0bebb5865edd2e163a31da966618"></a>

```c
#define FIDO2_RP_NAME_MAX_LEN 64
```

相关声明：[FIDO2_RP_NAME_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga99da0bebb5865edd2e163a31da966618)。

依赖方名称（Relying Party Name）的最大长度。

<a id="r_ga6060501b6c00b076fc705276464050ab"></a>

```c
#define FIDO2_USER_NAME_MAX_LEN 64
```

相关声明：[FIDO2_USER_NAME_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6060501b6c00b076fc705276464050ab)。

用户名（User Name）的最大长度。

<a id="r_gaa4111c61a7446d3cb5efa41bf492d930"></a>

```c
#define FIDO2_USER_DISPLAY_NAME_MAX_LEN 64
```

相关声明：[FIDO2_USER_DISPLAY_NAME_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaa4111c61a7446d3cb5efa41bf492d930)。

用户显示名称（User Display Name）的最大长度。

<a id="r_gaf5eb8fcafd96dd1d3eec5424aff9748c"></a>

```c
#define FIDO2_USER_ID_MAX_SIZE 64
```

相关声明：[FIDO2_USER_ID_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaf5eb8fcafd96dd1d3eec5424aff9748c)。

用户标识符（User ID）的最大大小，单位为字节。

<a id="r_ga624b79a13eb53f43594b5c24332725fa"></a>

```c
#define FIDO2_AAGUID_SIZE 16
```

相关声明：[FIDO2_AAGUID_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga624b79a13eb53f43594b5c24332725fa)。

认证器证明全局唯一标识符（AAGUID）的大小，单位为字节。

<a id="r_gaead02ba380ab3899742dfbf41edc4a98"></a>

```c
#define FIDO2_SHA256_SIZE 32
```

相关声明：[FIDO2_SHA256_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaead02ba380ab3899742dfbf41edc4a98)。

SHA-256 哈希大小（Hash Size）。

<a id="r_gaa42cec8a02f80b77e8ddf3250d4b289b"></a>

```c
#define FIDO2_PIN_HASH_SIZE 16
```

相关声明：[FIDO2_PIN_HASH_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaa42cec8a02f80b77e8ddf3250d4b289b)。

PIN 哈希大小（PIN Hash Size）。

<a id="r_ga0f2e24c8976c81ecceba0f65bf4ebdd6"></a>

```c
#define FIDO2_PIN_HASH_ENC_MAX_SIZE 32
```

相关声明：[FIDO2_PIN_HASH_ENC_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga0f2e24c8976c81ecceba0f65bf4ebdd6)。

加密 PIN 哈希（Encrypted PIN Hash）的最大大小。

<a id="r_gaefdcb90bad8ec73fe1fec85dd4bf3765"></a>

```c
#define FIDO2_PIN_ENC_MAX_SIZE 80
```

相关声明：[FIDO2_PIN_ENC_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaefdcb90bad8ec73fe1fec85dd4bf3765)。

加密 PIN（Encrypted PIN）的最大大小。

<a id="r_gad0a93bad80a62f314df813f979bbef25"></a>

```c
#define FIDO2_PIN_AUTH_SIZE_P1 16
```

相关声明：[FIDO2_PIN_AUTH_SIZE_P1](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gad0a93bad80a62f314df813f979bbef25)。

PIN 协议 1 认证参数大小（Auth Param Size）。

<a id="r_ga584ae6f184b200060162404c17f0391d"></a>

```c
#define FIDO2_PIN_AUTH_SIZE_P2 32
```

相关声明：[FIDO2_PIN_AUTH_SIZE_P2](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga584ae6f184b200060162404c17f0391d)。

PIN 协议 2 认证参数大小（Auth Param Size）。

<a id="r_ga6deaa8990424ff5a31787753e60355d2"></a>

```c
#define FIDO2_PIN_AUTH_MAX_SIZE 32
```

相关声明：[FIDO2_PIN_AUTH_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6deaa8990424ff5a31787753e60355d2)。

PIN 认证参数（Auth Param）的最大大小。

<a id="r_ga38ab5892a6d65b2ca4dab8cd59ea4567"></a>

```c
#define FIDO2_PIN_PADDED_SIZE 64
```

相关声明：[FIDO2_PIN_PADDED_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga38ab5892a6d65b2ca4dab8cd59ea4567)。

填充后的 PIN 大小（Padded PIN Size）。

<a id="r_gabeb1d03fa6426f2b7a8bf823a0cfd620"></a>

```c
#define FIDO2_PIN_TOKEN_ENC_MAX_SIZE 48
```

相关声明：[FIDO2_PIN_TOKEN_ENC_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gabeb1d03fa6426f2b7a8bf823a0cfd620)。

加密 PIN 令牌大小（Encrypted PIN Token Size）。

<a id="r_ga8e68d9a5a88e01a964538d4cf457af85"></a>

```c
#define FIDO2_DISCOVERABLE_CRED_ID_SIZE 32
```

相关声明：[FIDO2_DISCOVERABLE_CRED_ID_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga8e68d9a5a88e01a964538d4cf457af85)。

可发现凭据标识符（Discoverable Credential ID）的大小。

<a id="r_gad0a496f504dea20073ae15be879086f6"></a>

```c
#define FIDO2_NON_DISCOVERABLE_CRED_ID_SIZE 64
```

相关声明：[FIDO2_NON_DISCOVERABLE_CRED_ID_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gad0a496f504dea20073ae15be879086f6)。

不可发现凭据标识符（Non-discoverable Credential ID）的大小。

<a id="r_ga0288255da8902f9b30a345814419d06f"></a>

```c
#define FIDO2_AUTH_DATA_HEADER_SIZE 37
```

相关声明：[FIDO2_AUTH_DATA_HEADER_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga0288255da8902f9b30a345814419d06f)。

认证器数据头大小（Authenticator Data Header Size）。

<a id="r_gafb170c684357560e3c5999b3ae7aef80"></a>

```c
#define FIDO2_ATTESTED_CRED_DATA_MAX_SIZE (FIDO2_AAGUID_SIZE + 2 + FIDO2_CREDENTIAL_ID_MAX_SIZE + FIDO2_COSE_KEY_MAX_SIZE)
```

相关声明：[FIDO2_ATTESTED_CRED_DATA_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gafb170c684357560e3c5999b3ae7aef80)、[FIDO2_AAGUID_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga624b79a13eb53f43594b5c24332725fa)、[FIDO2_CREDENTIAL_ID_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga7ff8f1d8d389b44e2a656b3ebe20f778)。

证明凭据数据大小（Attested Credential Data Size）。

<a id="r_ga20de82a88a0f0d1c5e2f590450da98b3"></a>

```c
#define FIDO2_AUTH_DATA_MAX_SIZE (FIDO2_AUTH_DATA_HEADER_SIZE + FIDO2_ATTESTED_CRED_DATA_MAX_SIZE)
```

相关声明：[FIDO2_AUTH_DATA_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga20de82a88a0f0d1c5e2f590450da98b3)、[FIDO2_AUTH_DATA_HEADER_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga0288255da8902f9b30a345814419d06f)、[FIDO2_ATTESTED_CRED_DATA_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gafb170c684357560e3c5999b3ae7aef80)。

authenticatorData 最大大小（Maximum Size）8。

<a id="r_ga7fe764c73ecb327210eb080aa5b32a92"></a>

```c
#define FIDO2_MAX_EXTENSIONS 8
```

相关声明：[FIDO2_MAX_EXTENSIONS](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga7fe764c73ecb327210eb080aa5b32a92)。

支持的扩展（Extensions）的最大数量。

<a id="r_ga15f94b65bca9940f1a535e6ec1339fdf"></a>

```c
#define FIDO2_MAX_VERSIONS 4
```

相关声明：[FIDO2_MAX_VERSIONS](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga15f94b65bca9940f1a535e6ec1339fdf)。

支持的版本（Versions）的最大数量。

<a id="r_ga21282c628cd729631d3e02464693d454"></a>

```c
#define FIDO2_P256_UNCOMPRESSED_KEY_SIZE 65
```

相关声明：[FIDO2_P256_UNCOMPRESSED_KEY_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga21282c628cd729631d3e02464693d454)。

P-256 公钥导出大小（Public Key Export Size）。

<a id="r_ga03768c49b649e417454b17351825c89f"></a>

```c
#define FIDO2_P256_COORD_SIZE 32
```

相关声明：[FIDO2_P256_COORD_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga03768c49b649e417454b17351825c89f)。

P-256 坐标大小（Coordinate Size）。

<a id="r_gaa54dab9d9f69e30167e8e26b57750d03"></a>

```c
#define FIDO2_EC_POINT_UNCOMPRESSED 0x04
```

相关声明：[FIDO2_EC_POINT_UNCOMPRESSED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaa54dab9d9f69e30167e8e26b57750d03)。

椭圆曲线点前缀（EC Point Prefix）。

<a id="r_gadd8a4b5d7acd36c8eef7e593ece7f9ba"></a>

```c
#define FIDO2_ECDSA_SIG_MAX_SIZE 72
```

相关声明：[FIDO2_ECDSA_SIG_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gadd8a4b5d7acd36c8eef7e593ece7f9ba)。

ASN.1 编码的 ECDSA 签名长度（Signature Length）。

<a id="r_gae9b40fa6a6e68946588075afc6fe770a"></a>

```c
#define FIDO2_EXT_HMAC_SECRET BIT(0)
```

相关声明：[FIDO2_EXT_HMAC_SECRET](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gae9b40fa6a6e68946588075afc6fe770a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

凭据扩展（Credential Extension）：HMAC secret。

<a id="r_ga8ec5a639800de3f326a963188f1d9426"></a>

```c
#define FIDO2_EXT_LARGE_BLOB_KEY BIT(1)
```

相关声明：[FIDO2_EXT_LARGE_BLOB_KEY](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga8ec5a639800de3f326a963188f1d9426)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

凭据扩展（Credential Extension）：largeBlobKey。

<a id="r_ga6ce7d790ac95281ddf48fdfcc26e62b1"></a>

```c
#define FIDO2_EXT_CRED_BLOB BIT(2)
```

相关声明：[FIDO2_EXT_CRED_BLOB](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6ce7d790ac95281ddf48fdfcc26e62b1)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

凭据扩展（Credential Extension）：credBlob。

<a id="r_ga014d98ca20bdba2ec3e03de0ce074221"></a>

```c
#define FIDO2_EXT_THIRD_PARTY_PAY BIT(3)
```

相关声明：[FIDO2_EXT_THIRD_PARTY_PAY](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga014d98ca20bdba2ec3e03de0ce074221)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

凭据扩展（Credential Extension）：thirdPartyPayment。

<a id="r_ga3e2b16dffcd2c4a5b8958c5473a49bce"></a>

```c
#define FIDO2_TRANSPORT_USB BIT(0)
```

相关声明：[FIDO2_TRANSPORT_USB](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga3e2b16dffcd2c4a5b8958c5473a49bce)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

USB 传输（Transport）。

<a id="r_ga70811c17432b511a72481030abe09b2e"></a>

```c
#define FIDO2_TRANSPORT_BLE BIT(1)
```

相关声明：[FIDO2_TRANSPORT_BLE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga70811c17432b511a72481030abe09b2e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

低功耗蓝牙（BLE）传输（Transport）。

<a id="r_ga6b1cc385bcce20455922f617c8221f98"></a>

```c
#define FIDO2_TRANSPORT_NFC BIT(2)
```

相关声明：[FIDO2_TRANSPORT_NFC](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b1cc385bcce20455922f617c8221f98)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

近场通信（NFC）传输（Transport）。

<a id="r_ga82f1ff43692a451fcd11ec623165db6e"></a>

```c
#define AUTH_DATA_FLAG_UP BIT(0)
```

相关声明：[AUTH_DATA_FLAG_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga82f1ff43692a451fcd11ec623165db6e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

用户在场（User Present，UP）结果。

<a id="r_gac08abdf137cc2062f0e4b4a81ee2802b"></a>

```c
#define AUTH_DATA_FLAG_UV BIT(2)
```

相关声明：[AUTH_DATA_FLAG_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gac08abdf137cc2062f0e4b4a81ee2802b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

用户已验证（User Verified，UV）结果。

<a id="r_ga66a31ee72d63974ac4838f35149cd1d9"></a>

```c
#define AUTH_DATA_FLAG_AT BIT(6)
```

相关声明：[AUTH_DATA_FLAG_AT](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga66a31ee72d63974ac4838f35149cd1d9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

包含证明凭据数据（Attested Credential Data，AT）。

<a id="r_ga01d9f3d9e550f3cf16083d8048b6c6b4"></a>

```c
#define AUTH_DATA_FLAG_ED BIT(7)
```

相关声明：[AUTH_DATA_FLAG_ED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga01d9f3d9e550f3cf16083d8048b6c6b4)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

包含扩展数据（Extension Data，ED）。

<a id="r_ga6b3b79c7ef54b3ebbe686d4f67aaf7fc"></a>

```c
enum fido2_status { FIDO2_OK = 0x00 , FIDO2_ERR_INVALID_COMMAND = 0x01 , FIDO2_ERR_INVALID_PARAMETER = 0x02 , FIDO2_ERR_INVALID_LENGTH = 0x03 , FIDO2_ERR_INVALID_SEQ = 0x04 , FIDO2_ERR_TIMEOUT = 0x05 , FIDO2_ERR_CHANNEL_BUSY = 0x06 , FIDO2_ERR_LOCK_REQUIRED = 0x0A , FIDO2_ERR_INVALID_CHANNEL = 0x0B , FIDO2_ERR_CBOR_UNEXPECTED_TYPE = 0x11 , FIDO2_ERR_INVALID_CBOR = 0x12 , FIDO2_ERR_MISSING_PARAMETER = 0x14 , FIDO2_ERR_LIMIT_EXCEEDED = 0x15 , FIDO2_ERR_UNSUPPORTED_EXTENSION = 0x16 , FIDO2_ERR_FP_DATABASE_FULL = 0x17 , FIDO2_ERR_LARGE_BLOB_STORAGE_FULL = 0x18 , FIDO2_ERR_CREDENTIAL_EXCLUDED = 0x19 , FIDO2_ERR_PROCESSING = 0x21 , FIDO2_ERR_INVALID_CREDENTIAL = 0x22 , FIDO2_ERR_USER_ACTION_PENDING = 0x23 , FIDO2_ERR_OPERATION_PENDING = 0x24 , FIDO2_ERR_NO_OPERATIONS = 0x25 , FIDO2_ERR_UNSUPPORTED_ALGORITHM = 0x26 , FIDO2_ERR_OPERATION_DENIED = 0x27 , FIDO2_ERR_KEY_STORE_FULL = 0x28 , FIDO2_ERR_UNSUPPORTED_OPTION = 0x2B , FIDO2_ERR_INVALID_OPTION = 0x2C , FIDO2_ERR_KEEPALIVE_CANCEL = 0x2D , FIDO2_ERR_NO_CREDENTIALS = 0x2E , FIDO2_ERR_USER_ACTION_TIMEOUT = 0x2F , FIDO2_ERR_NOT_ALLOWED = 0x30 , FIDO2_ERR_PIN_INVALID = 0x31 , FIDO2_ERR_PIN_BLOCKED = 0x32 , FIDO2_ERR_PIN_AUTH_INVALID = 0x33 , FIDO2_ERR_PIN_AUTH_BLOCKED = 0x34 , FIDO2_ERR_PIN_NOT_SET = 0x35 , FIDO2_ERR_PUAT_REQUIRED = 0x36 , FIDO2_ERR_PIN_POLICY_VIOLATION = 0x37 , FIDO2_ERR_RESERVED = 0x38 , FIDO2_ERR_REQUEST_TOO_LARGE = 0x39 , FIDO2_ERR_ACTION_TIMEOUT = 0x3A , FIDO2_ERR_UP_REQUIRED = 0x3B , FIDO2_ERR_UV_BLOCKED = 0x3C , FIDO2_ERR_INTEGRITY_FAILURE = 0x3D , FIDO2_ERR_INVALID_SUBCOMMAND = 0x3E , FIDO2_ERR_UV_INVALID = 0x3F , FIDO2_ERR_UNAUTHORIZED_PERMISSION = 0x40 , FIDO2_ERR_OTHER = 0x7F }
```

相关声明：[fido2_status](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fc)、[FIDO2_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaa08efc6dee799b3e1fb8490bc64bd1cf)、[FIDO2_ERR_INVALID_COMMAND](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcab263ae4a933b875d54a86d4a6da8dc4e)、[FIDO2_ERR_INVALID_PARAMETER](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcab4382a900e27d13b5043241f2f6dc2fe)、[FIDO2_ERR_INVALID_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcacbaf6656b7eac960f4bc0e561de47011)、[FIDO2_ERR_INVALID_SEQ](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca809431ef12cd0ba7094a80c39d6bdc2d)、[FIDO2_ERR_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaf713403e6582ce02cace5d29f45405af)、[FIDO2_ERR_CHANNEL_BUSY](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcac36b384a558597d72980f2425008c7b6)、[FIDO2_ERR_LOCK_REQUIRED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcacf7163e857eb9b8b6ddef1e7ff2b7351)、[FIDO2_ERR_INVALID_CHANNEL](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca1ece48887496a5962823530201eaf48c)、[FIDO2_ERR_CBOR_UNEXPECTED_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca17c4a70a8f87425c4d849585d28280d4)、[FIDO2_ERR_INVALID_CBOR](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcac804a5a070c6552d89d403ffc953c00d)、[FIDO2_ERR_MISSING_PARAMETER](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcad19e5127b17b8e0abee8bfe7d1ae595f)、[FIDO2_ERR_LIMIT_EXCEEDED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaee29e086a2af8e697b6467c9667cb327)、[FIDO2_ERR_UNSUPPORTED_EXTENSION](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcabe9d8c984a0c0a62616a4a94af655a78)、[FIDO2_ERR_FP_DATABASE_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcacc4208f8ab39ba6b67c9358df6b88797)、[FIDO2_ERR_LARGE_BLOB_STORAGE_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaffdba1168067976851629c2111f46f6a)、[FIDO2_ERR_CREDENTIAL_EXCLUDED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca5dfe38f41a7863bc04928d7c566568b7)、[FIDO2_ERR_PROCESSING](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca128911647928193e076041834e398e75)、[FIDO2_ERR_INVALID_CREDENTIAL](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca4c53af9f0ad3e857bf86efea60b9370f)、[FIDO2_ERR_USER_ACTION_PENDING](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca8d108ee70faea78aa0669a90081dd05c)、[FIDO2_ERR_OPERATION_PENDING](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca020a5895146a35c2dedace5e0ff96112)、[FIDO2_ERR_NO_OPERATIONS](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca376b899ff97c4d39f201f20e03a36ed7)、[FIDO2_ERR_UNSUPPORTED_ALGORITHM](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca3521d75934cddcd0d009279541381c41)、[FIDO2_ERR_OPERATION_DENIED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca507f5ded749fdba95d6b16d859052d43)、[FIDO2_ERR_KEY_STORE_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcacb6d4da143bbd72b7d361a7a4e38b1da)、[FIDO2_ERR_UNSUPPORTED_OPTION](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaad5b849ccb37209d531444bb346e3158)、[FIDO2_ERR_INVALID_OPTION](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca05bb5e1370a3e46ef1a2f2545cf5675c)、[FIDO2_ERR_KEEPALIVE_CANCEL](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca336c3e439e0a1b3eb24cf3edc38455e1)、[FIDO2_ERR_NO_CREDENTIALS](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcafcbd15f2df2744ed0afd3613540ad6a3)、[FIDO2_ERR_USER_ACTION_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca39355da927952f311dd8cdf9fe5cced8)、[FIDO2_ERR_NOT_ALLOWED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca739a74cd005fc1b3b8853f7aa2db7e3e)、[FIDO2_ERR_PIN_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca6eb4c3a5f51db1d0232ef8ca21d194e6)、[FIDO2_ERR_PIN_BLOCKED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca05c0bff840ed8b7e85c147876792760f)、[FIDO2_ERR_PIN_AUTH_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca63548371fe576d03e00a2d428bf2501b)、[FIDO2_ERR_PIN_AUTH_BLOCKED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca57a9754a770796bdb303ec5503222060)、[FIDO2_ERR_PIN_NOT_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcab59eee02a04da8ca4bf54ceba81794d0)、[FIDO2_ERR_PUAT_REQUIRED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca5c952ab01843550e24d3aa672f05fec9)、[FIDO2_ERR_PIN_POLICY_VIOLATION](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca8406e112b928b9f556cced2f0c391cfe)、[FIDO2_ERR_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca935a727495553c4bf584a92c39d780b7)、[FIDO2_ERR_REQUEST_TOO_LARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca0ca1a5d18e501d446c58ddcc4f8fbc05)、[FIDO2_ERR_ACTION_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca356a92621e9d79fd5d599f1c13a7da93)、[FIDO2_ERR_UP_REQUIRED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaa28ed4a202b7c8eca14a727b708b0d50)、[FIDO2_ERR_UV_BLOCKED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaeb3d5db8b9e7ad3123df8d2a76ed4bfe)、[FIDO2_ERR_INTEGRITY_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca43b6e71c8f000bb2eccfc8a45c4591d3)、[FIDO2_ERR_INVALID_SUBCOMMAND](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca53aa4e296d54d24d7aab0bfc7747d893)、[FIDO2_ERR_UV_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca620c7a76e1481401e9dce1a5a75c8ee8)、[FIDO2_ERR_UNAUTHORIZED_PERMISSION](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca69c9ebc7f40bcc26641eaa910a84f7e4)、[FIDO2_ERR_OTHER](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcab52bc5933983ff9464292f4a470e0217)。

CTAP2 状态码（Status Codes）。

<a id="r_gaec9e2106f2d776266909f5e2baf924d9"></a>

```c
enum fido2_cmd { FIDO2_CMD_MAKE_CREDENTIAL = 0x01 , FIDO2_CMD_GET_ASSERTION = 0x02 , FIDO2_CMD_GET_INFO = 0x04 , FIDO2_CMD_CLIENT_PIN = 0x06 , FIDO2_CMD_RESET = 0x07 , FIDO2_CMD_GET_NEXT_ASSERTION = 0x08 , FIDO2_CMD_CREDENTIAL_MGMT = 0x0A , FIDO2_CMD_SELECTION = 0x0B }
```

相关声明：[fido2_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaec9e2106f2d776266909f5e2baf924d9)、[FIDO2_CMD_MAKE_CREDENTIAL](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaec9e2106f2d776266909f5e2baf924d9aca44c6fcf4ff9f7d43693607a4ea178a)、[FIDO2_CMD_GET_ASSERTION](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaec9e2106f2d776266909f5e2baf924d9a64758dfc5b08bccc58369e97ecd8eae0)、[FIDO2_CMD_GET_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaec9e2106f2d776266909f5e2baf924d9a2419f886d7fcfe8e4e77a4b5f21d5bfc)、[FIDO2_CMD_CLIENT_PIN](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaec9e2106f2d776266909f5e2baf924d9a6b7d85b947ad93ab5159ffe7f2934948)、[FIDO2_CMD_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaec9e2106f2d776266909f5e2baf924d9aacffe603fa91c1102164c1d022bcd678)、[FIDO2_CMD_GET_NEXT_ASSERTION](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaec9e2106f2d776266909f5e2baf924d9adc26ad4d923d58ca0f33d63c9dae1c27)、[FIDO2_CMD_CREDENTIAL_MGMT](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaec9e2106f2d776266909f5e2baf924d9a4984d83c6210b1855106ff39b413e614)、[FIDO2_CMD_SELECTION](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaec9e2106f2d776266909f5e2baf924d9a327a6fbfb22651dfed6d1d1ded574ab7)。

CTAP2 命令码（Command Codes）。

<a id="r_gae9411b5f6c2596cf49f7ebcf04fd7955"></a>

```c
enum fido2_cred_protect { FIDO2_CRED_PROTECT_UV_OPTIONAL = 0x01 , FIDO2_CRED_PROTECT_UV_OPTIONAL_WITH_LIST = 0x02 , FIDO2_CRED_PROTECT_UV_REQUIRED = 0x03 }
```

相关声明：[fido2_cred_protect](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gae9411b5f6c2596cf49f7ebcf04fd7955)、[FIDO2_CRED_PROTECT_UV_OPTIONAL](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gae9411b5f6c2596cf49f7ebcf04fd7955a07603aa0b0598319d504ca9e23e76078)、[FIDO2_CRED_PROTECT_UV_OPTIONAL_WITH_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gae9411b5f6c2596cf49f7ebcf04fd7955a2299549abdae08cd0e71c7db3d918ca6)、[FIDO2_CRED_PROTECT_UV_REQUIRED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gae9411b5f6c2596cf49f7ebcf04fd7955aef0d3d870129fc9e72138d309c641be6)。

凭据保护级别（Credential Protection Levels）。

<a id="r_ga86aa0e78a95ea9e399c3831348fe8684"></a>

```c
enum fido2_cose_alg { FIDO2_COSE_ES256 = -7 , FIDO2_COSE_EDDSA = -8 , FIDO2_COSE_ECDHES_HKDF256 = -25 , FIDO2_COSE_RS256 = -257 }
```

相关声明：[fido2_cose_alg](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga86aa0e78a95ea9e399c3831348fe8684)、[FIDO2_COSE_ES256](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga86aa0e78a95ea9e399c3831348fe8684a94ae94ce511d5898c12059766adf95c3)、[FIDO2_COSE_EDDSA](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga86aa0e78a95ea9e399c3831348fe8684a21d965a84070571fb2e0d475cf27043d)、[FIDO2_COSE_ECDHES_HKDF256](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga86aa0e78a95ea9e399c3831348fe8684a386cd8a5baf42b49b2271d655645b103)、[FIDO2_COSE_RS256](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga86aa0e78a95ea9e399c3831348fe8684ad2a327ca6649f0abd4153dee72952167)。

COSE 算法标识符（Algorithm Identifiers）。


## 2.2\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P262_fido2_types.h_源码浏览.md)
- [fido2_credential](../platform_security_model_reference/P007_fido2_credential_结构体.md)
- [fido2_device_info](../platform_security_model_reference/P008_fido2_device_info_结构体.md)
- [FIDO2_CREDENTIAL_ID_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga7ff8f1d8d389b44e2a656b3ebe20f778)
- [FIDO2_RP_ID_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga57628d326e2f62b318908af69485dbb8)
- [FIDO2_RP_NAME_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga99da0bebb5865edd2e163a31da966618)
- [FIDO2_USER_NAME_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6060501b6c00b076fc705276464050ab)
- [FIDO2_USER_DISPLAY_NAME_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaa4111c61a7446d3cb5efa41bf492d930)
- [FIDO2_USER_ID_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaf5eb8fcafd96dd1d3eec5424aff9748c)
- [FIDO2_AAGUID_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga624b79a13eb53f43594b5c24332725fa)
- [FIDO2_SHA256_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaead02ba380ab3899742dfbf41edc4a98)
- [FIDO2_PIN_HASH_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaa42cec8a02f80b77e8ddf3250d4b289b)
- [FIDO2_PIN_HASH_ENC_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga0f2e24c8976c81ecceba0f65bf4ebdd6)
- [FIDO2_PIN_ENC_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaefdcb90bad8ec73fe1fec85dd4bf3765)
- [FIDO2_PIN_AUTH_SIZE_P1](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gad0a93bad80a62f314df813f979bbef25)
- [FIDO2_PIN_AUTH_SIZE_P2](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga584ae6f184b200060162404c17f0391d)
- [FIDO2_PIN_AUTH_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6deaa8990424ff5a31787753e60355d2)
- [FIDO2_PIN_PADDED_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga38ab5892a6d65b2ca4dab8cd59ea4567)
- [FIDO2_PIN_TOKEN_ENC_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gabeb1d03fa6426f2b7a8bf823a0cfd620)
- [FIDO2_DISCOVERABLE_CRED_ID_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga8e68d9a5a88e01a964538d4cf457af85)
- [FIDO2_NON_DISCOVERABLE_CRED_ID_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gad0a496f504dea20073ae15be879086f6)
- [FIDO2_AUTH_DATA_HEADER_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga0288255da8902f9b30a345814419d06f)
- [FIDO2_ATTESTED_CRED_DATA_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gafb170c684357560e3c5999b3ae7aef80)
- [FIDO2_AUTH_DATA_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga20de82a88a0f0d1c5e2f590450da98b3)
- [FIDO2_MAX_EXTENSIONS](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga7fe764c73ecb327210eb080aa5b32a92)
- [FIDO2_MAX_VERSIONS](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga15f94b65bca9940f1a535e6ec1339fdf)
- [FIDO2_P256_UNCOMPRESSED_KEY_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga21282c628cd729631d3e02464693d454)
- [FIDO2_P256_COORD_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga03768c49b649e417454b17351825c89f)
- [FIDO2_EC_POINT_UNCOMPRESSED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaa54dab9d9f69e30167e8e26b57750d03)
- [FIDO2_ECDSA_SIG_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gadd8a4b5d7acd36c8eef7e593ece7f9ba)
- [FIDO2_EXT_HMAC_SECRET](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gae9b40fa6a6e68946588075afc6fe770a)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [FIDO2_EXT_LARGE_BLOB_KEY](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga8ec5a639800de3f326a963188f1d9426)
- [FIDO2_EXT_CRED_BLOB](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6ce7d790ac95281ddf48fdfcc26e62b1)
- [FIDO2_EXT_THIRD_PARTY_PAY](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga014d98ca20bdba2ec3e03de0ce074221)
- [FIDO2_TRANSPORT_USB](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga3e2b16dffcd2c4a5b8958c5473a49bce)
- [FIDO2_TRANSPORT_BLE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga70811c17432b511a72481030abe09b2e)
- [FIDO2_TRANSPORT_NFC](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b1cc385bcce20455922f617c8221f98)
- [AUTH_DATA_FLAG_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga82f1ff43692a451fcd11ec623165db6e)
- [AUTH_DATA_FLAG_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gac08abdf137cc2062f0e4b4a81ee2802b)
- [AUTH_DATA_FLAG_AT](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga66a31ee72d63974ac4838f35149cd1d9)
- [AUTH_DATA_FLAG_ED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga01d9f3d9e550f3cf16083d8048b6c6b4)
- [fido2_status](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fc)
- [FIDO2_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaa08efc6dee799b3e1fb8490bc64bd1cf)
- [FIDO2_ERR_INVALID_COMMAND](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcab263ae4a933b875d54a86d4a6da8dc4e)
- [FIDO2_ERR_INVALID_PARAMETER](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcab4382a900e27d13b5043241f2f6dc2fe)
- [FIDO2_ERR_INVALID_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcacbaf6656b7eac960f4bc0e561de47011)
- [FIDO2_ERR_INVALID_SEQ](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca809431ef12cd0ba7094a80c39d6bdc2d)
- [FIDO2_ERR_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaf713403e6582ce02cace5d29f45405af)
- [FIDO2_ERR_CHANNEL_BUSY](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcac36b384a558597d72980f2425008c7b6)
- [FIDO2_ERR_LOCK_REQUIRED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcacf7163e857eb9b8b6ddef1e7ff2b7351)
- [FIDO2_ERR_INVALID_CHANNEL](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca1ece48887496a5962823530201eaf48c)
- [FIDO2_ERR_CBOR_UNEXPECTED_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca17c4a70a8f87425c4d849585d28280d4)
- [FIDO2_ERR_INVALID_CBOR](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcac804a5a070c6552d89d403ffc953c00d)
- [FIDO2_ERR_MISSING_PARAMETER](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcad19e5127b17b8e0abee8bfe7d1ae595f)
- [FIDO2_ERR_LIMIT_EXCEEDED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaee29e086a2af8e697b6467c9667cb327)
- [FIDO2_ERR_UNSUPPORTED_EXTENSION](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcabe9d8c984a0c0a62616a4a94af655a78)
- [FIDO2_ERR_FP_DATABASE_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcacc4208f8ab39ba6b67c9358df6b88797)
- [FIDO2_ERR_LARGE_BLOB_STORAGE_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaffdba1168067976851629c2111f46f6a)
- [FIDO2_ERR_CREDENTIAL_EXCLUDED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca5dfe38f41a7863bc04928d7c566568b7)
- [FIDO2_ERR_PROCESSING](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca128911647928193e076041834e398e75)
- [FIDO2_ERR_INVALID_CREDENTIAL](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca4c53af9f0ad3e857bf86efea60b9370f)
- [FIDO2_ERR_USER_ACTION_PENDING](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca8d108ee70faea78aa0669a90081dd05c)
- [FIDO2_ERR_OPERATION_PENDING](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca020a5895146a35c2dedace5e0ff96112)
- [FIDO2_ERR_NO_OPERATIONS](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca376b899ff97c4d39f201f20e03a36ed7)
- [FIDO2_ERR_UNSUPPORTED_ALGORITHM](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca3521d75934cddcd0d009279541381c41)
- [FIDO2_ERR_OPERATION_DENIED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca507f5ded749fdba95d6b16d859052d43)
- [FIDO2_ERR_KEY_STORE_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcacb6d4da143bbd72b7d361a7a4e38b1da)
- [FIDO2_ERR_UNSUPPORTED_OPTION](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaad5b849ccb37209d531444bb346e3158)
- [FIDO2_ERR_INVALID_OPTION](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca05bb5e1370a3e46ef1a2f2545cf5675c)
- [FIDO2_ERR_KEEPALIVE_CANCEL](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca336c3e439e0a1b3eb24cf3edc38455e1)
- [FIDO2_ERR_NO_CREDENTIALS](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcafcbd15f2df2744ed0afd3613540ad6a3)
- [FIDO2_ERR_USER_ACTION_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca39355da927952f311dd8cdf9fe5cced8)
- [FIDO2_ERR_NOT_ALLOWED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca739a74cd005fc1b3b8853f7aa2db7e3e)
- [FIDO2_ERR_PIN_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca6eb4c3a5f51db1d0232ef8ca21d194e6)
- [FIDO2_ERR_PIN_BLOCKED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca05c0bff840ed8b7e85c147876792760f)
- [FIDO2_ERR_PIN_AUTH_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca63548371fe576d03e00a2d428bf2501b)
- [FIDO2_ERR_PIN_AUTH_BLOCKED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca57a9754a770796bdb303ec5503222060)
- [FIDO2_ERR_PIN_NOT_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcab59eee02a04da8ca4bf54ceba81794d0)
- [FIDO2_ERR_PUAT_REQUIRED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca5c952ab01843550e24d3aa672f05fec9)
- [FIDO2_ERR_PIN_POLICY_VIOLATION](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca8406e112b928b9f556cced2f0c391cfe)
- [FIDO2_ERR_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca935a727495553c4bf584a92c39d780b7)
- [FIDO2_ERR_REQUEST_TOO_LARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca0ca1a5d18e501d446c58ddcc4f8fbc05)
- [FIDO2_ERR_ACTION_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca356a92621e9d79fd5d599f1c13a7da93)
- [FIDO2_ERR_UP_REQUIRED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaa28ed4a202b7c8eca14a727b708b0d50)
- [FIDO2_ERR_UV_BLOCKED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaeb3d5db8b9e7ad3123df8d2a76ed4bfe)
- [FIDO2_ERR_INTEGRITY_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca43b6e71c8f000bb2eccfc8a45c4591d3)
- [FIDO2_ERR_INVALID_SUBCOMMAND](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca53aa4e296d54d24d7aab0bfc7747d893)
- [FIDO2_ERR_UV_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca620c7a76e1481401e9dce1a5a75c8ee8)
- [FIDO2_ERR_UNAUTHORIZED_PERMISSION](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca69c9ebc7f40bcc26641eaa910a84f7e4)
- [FIDO2_ERR_OTHER](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcab52bc5933983ff9464292f4a470e0217)
- [fido2_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaec9e2106f2d776266909f5e2baf924d9)
- [FIDO2_CMD_MAKE_CREDENTIAL](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaec9e2106f2d776266909f5e2baf924d9aca44c6fcf4ff9f7d43693607a4ea178a)
- [FIDO2_CMD_GET_ASSERTION](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaec9e2106f2d776266909f5e2baf924d9a64758dfc5b08bccc58369e97ecd8eae0)
- [FIDO2_CMD_GET_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaec9e2106f2d776266909f5e2baf924d9a2419f886d7fcfe8e4e77a4b5f21d5bfc)
- [FIDO2_CMD_CLIENT_PIN](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaec9e2106f2d776266909f5e2baf924d9a6b7d85b947ad93ab5159ffe7f2934948)
- [FIDO2_CMD_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaec9e2106f2d776266909f5e2baf924d9aacffe603fa91c1102164c1d022bcd678)
- [FIDO2_CMD_GET_NEXT_ASSERTION](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaec9e2106f2d776266909f5e2baf924d9adc26ad4d923d58ca0f33d63c9dae1c27)
- [FIDO2_CMD_CREDENTIAL_MGMT](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaec9e2106f2d776266909f5e2baf924d9a4984d83c6210b1855106ff39b413e614)
- [FIDO2_CMD_SELECTION](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaec9e2106f2d776266909f5e2baf924d9a327a6fbfb22651dfed6d1d1ded574ab7)
- [fido2_cred_protect](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gae9411b5f6c2596cf49f7ebcf04fd7955)
- [FIDO2_CRED_PROTECT_UV_OPTIONAL](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gae9411b5f6c2596cf49f7ebcf04fd7955a07603aa0b0598319d504ca9e23e76078)
- [FIDO2_CRED_PROTECT_UV_OPTIONAL_WITH_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gae9411b5f6c2596cf49f7ebcf04fd7955a2299549abdae08cd0e71c7db3d918ca6)
- [FIDO2_CRED_PROTECT_UV_REQUIRED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gae9411b5f6c2596cf49f7ebcf04fd7955aef0d3d870129fc9e72138d309c641be6)
- [fido2_cose_alg](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga86aa0e78a95ea9e399c3831348fe8684)
- [FIDO2_COSE_ES256](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga86aa0e78a95ea9e399c3831348fe8684a94ae94ce511d5898c12059766adf95c3)
- [FIDO2_COSE_EDDSA](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga86aa0e78a95ea9e399c3831348fe8684a21d965a84070571fb2e0d475cf27043d)
- [FIDO2_COSE_ECDHES_HKDF256](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga86aa0e78a95ea9e399c3831348fe8684a386cd8a5baf42b49b2271d655645b103)
- [FIDO2_COSE_RS256](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga86aa0e78a95ea9e399c3831348fe8684ad2a327ca6649f0abd4153dee72952167)

<a id="header-details"></a>

---

[上一章](P001_zephyr__drivers__auxdisplay.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__storage__flash_map.h_文件参考.md)
