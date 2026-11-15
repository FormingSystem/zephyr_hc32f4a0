---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-24
title: zephyr__psa__key_ids.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/key__ids_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_zephyr\_\_psa\_\_key\_ids.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/key__ids_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

此文件定义PSA密码（Crypto）API现有使用者的密钥ID范围。

<a id="details"></a>

```c
#include <stdint.h>
```

查看此文件的源码。

本文件定义 PSA 加密 API（PSA Crypto API）现有使用者的密钥 ID 范围（Key ID Ranges）。除应用之外，不同子系统也通过 PSA Crypto API 存储和使用持久密钥（Persistent Keys）。由于这些子系统彼此独立，使用不同 ID 范围来避免冲突。本文件作为 Zephyr 内所有已分配 PSA 密钥 ID 范围的登记表（Registry）。最终用户应用也有专用范围，即 `ZEPHYR_PSA_APPLICATION_KEY_ID_RANGE_BEGIN`。下列部分 ID 沿用此前已有且正在使用的值，另一些则在 PSA 用户密钥 ID 范围中选择适当位置，以尽量避免冲突，例如避开范围最前端。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 24.1\_宏定义（Macros）

<a id="r_a3e8bcbe8554a07e045a7330196c8a003"></a>

```c
#define ZEPHYR_PSA_OPENTHREAD_KEY_ID_RANGE_BEGIN (psa_key_id_t)0x20000
```

相关声明：[ZEPHYR_PSA_OPENTHREAD_KEY_ID_RANGE_BEGIN](#a3e8bcbe8554a07e045a7330196c8a003)、[psa_key_id_t](#a11e986351c65bd3dc3c0fe2cd9926e4b)。

供 OpenThread 使用的 PSA 密钥 ID 范围（Key ID Range）。

<a id="r_a484d6a1af8ccc3a869b9a2b7753d1c2c"></a>

```c
#define ZEPHYR_PSA_OPENTHREAD_KEY_ID_RANGE_SIZE 0x10000
```

相关声明：[ZEPHYR_PSA_OPENTHREAD_KEY_ID_RANGE_SIZE](#a484d6a1af8ccc3a869b9a2b7753d1c2c)。

64 Ki（64 × 1024）。

<a id="r_ae4606ebca8aa09c0096897c927981cb6"></a>

```c
#define ZEPHYR_PSA_MATTER_KEY_ID_RANGE_BEGIN (psa_key_id_t)0x30000
```

相关声明：[ZEPHYR_PSA_MATTER_KEY_ID_RANGE_BEGIN](#ae4606ebca8aa09c0096897c927981cb6)、[psa_key_id_t](#a11e986351c65bd3dc3c0fe2cd9926e4b)。

供 Matter 使用的 PSA 密钥 ID 范围（Key ID Range）。

<a id="r_a6b459be7f0d6d39cd6bf8d482473b23f"></a>

```c
#define ZEPHYR_PSA_MATTER_KEY_ID_RANGE_SIZE 0x10000
```

相关声明：[ZEPHYR_PSA_MATTER_KEY_ID_RANGE_SIZE](#a6b459be7f0d6d39cd6bf8d482473b23f)。

64 Ki（64 × 1024）。

<a id="r_a032913d751fddc7a6a0ac3f98229947d"></a>

```c
#define ZEPHYR_PSA_BT_MESH_KEY_ID_RANGE_BEGIN (psa_key_id_t)0x20000000
```

相关声明：[ZEPHYR_PSA_BT_MESH_KEY_ID_RANGE_BEGIN](#a032913d751fddc7a6a0ac3f98229947d)、[psa_key_id_t](#a11e986351c65bd3dc3c0fe2cd9926e4b)。

供 Bluetooth Mesh 使用的 PSA 密钥 ID 范围（Key ID Range）。

<a id="r_a6b1b95861f2a8b9b9f45e0c8dee04007"></a>

```c
#define ZEPHYR_PSA_BT_MESH_KEY_ID_RANGE_SIZE 0xC000
```

相关声明：[ZEPHYR_PSA_BT_MESH_KEY_ID_RANGE_SIZE](#a6b1b95861f2a8b9b9f45e0c8dee04007)。

48 Ki（48 × 1024）。

<a id="r_ac02d47ca235e44f30e5fa32aa5cbfadc"></a>

```c
#define ZEPHYR_PSA_WIFI_CREDENTIALS_KEY_ID_RANGE_BEGIN (psa_key_id_t)0x20010000
```

相关声明：[ZEPHYR_PSA_WIFI_CREDENTIALS_KEY_ID_RANGE_BEGIN](#ac02d47ca235e44f30e5fa32aa5cbfadc)、[psa_key_id_t](#a11e986351c65bd3dc3c0fe2cd9926e4b)。

供 Wi-Fi 凭据管理（Credentials Management）使用的 PSA 密钥 ID 范围。

<a id="r_a86a47e671a632befdce9b201a66002d5"></a>

```c
#define ZEPHYR_PSA_WIFI_CREDENTIALS_KEY_ID_RANGE_SIZE 0x100
```

相关声明：[ZEPHYR_PSA_WIFI_CREDENTIALS_KEY_ID_RANGE_SIZE](#a86a47e671a632befdce9b201a66002d5)。

256。

<a id="r_a60948c97d6160f685985a3e4768403a7"></a>

```c
#define ZEPHYR_PSA_FIDO2_KEY_ID_RANGE_BEGIN (psa_key_id_t)0x20011000
```

相关声明：[ZEPHYR_PSA_FIDO2_KEY_ID_RANGE_BEGIN](#a60948c97d6160f685985a3e4768403a7)、[psa_key_id_t](#a11e986351c65bd3dc3c0fe2cd9926e4b)。

供 FIDO2 使用的 PSA 密钥 ID 范围（Key ID Range）。

<a id="r_aa39e59f3f1df32829af4e9189248d14b"></a>

```c
#define ZEPHYR_PSA_FIDO2_KEY_ID_RANGE_SIZE 0x1000
```

相关声明：[ZEPHYR_PSA_FIDO2_KEY_ID_RANGE_SIZE](#aa39e59f3f1df32829af4e9189248d14b)。

4 Ki（4 × 1024）。

<a id="r_af0f6e7d2b0798aaaccc3fb3bd12d1b8a"></a>

```c
#define ZEPHYR_PSA_APPLICATION_KEY_ID_RANGE_BEGIN (psa_key_id_t)0x30000000
```

相关声明：[ZEPHYR_PSA_APPLICATION_KEY_ID_RANGE_BEGIN](#af0f6e7d2b0798aaaccc3fb3bd12d1b8a)、[psa_key_id_t](#a11e986351c65bd3dc3c0fe2cd9926e4b)。

供最终用户应用（End-user Application）使用的 PSA 密钥 ID 范围。

<a id="r_ad222fd0bf1eb32eaa23d6bd52d300125"></a>

```c
#define ZEPHYR_PSA_APPLICATION_KEY_ID_RANGE_SIZE 0x100000
```

相关声明：[ZEPHYR_PSA_APPLICATION_KEY_ID_RANGE_SIZE](#ad222fd0bf1eb32eaa23d6bd52d300125)。

1 Mi（1024 × 1024）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 24.2\_类型定义（Typedefs）

<a id="r_a11e986351c65bd3dc3c0fe2cd9926e4b"></a>

```c
typedef uint32_t psa_key_id_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[psa_key_id_t](#a11e986351c65bd3dc3c0fe2cd9926e4b)。

## 24.3\_详细说明（Detailed Documentation）

<a id="af0f6e7d2b0798aaaccc3fb3bd12d1b8a"></a>

### `ZEPHYR_PSA_APPLICATION_KEY_ID_RANGE_BEGIN`

```c
#define ZEPHYR_PSA_APPLICATION_KEY_ID_RANGE_BEGIN (psa_key_id_t)0x30000000
```

供最终用户应用（End-user Application）使用的 PSA 密钥 ID 范围。

<a id="ad222fd0bf1eb32eaa23d6bd52d300125"></a>

### `ZEPHYR_PSA_APPLICATION_KEY_ID_RANGE_SIZE`

```c
#define ZEPHYR_PSA_APPLICATION_KEY_ID_RANGE_SIZE 0x100000
```

1 Mi（1024 × 1024）。

<a id="a032913d751fddc7a6a0ac3f98229947d"></a>

### `ZEPHYR_PSA_BT_MESH_KEY_ID_RANGE_BEGIN`

```c
#define ZEPHYR_PSA_BT_MESH_KEY_ID_RANGE_BEGIN (psa_key_id_t)0x20000000
```

供 Bluetooth Mesh 使用的 PSA 密钥 ID 范围（Key ID Range）。

<a id="a6b1b95861f2a8b9b9f45e0c8dee04007"></a>

### `ZEPHYR_PSA_BT_MESH_KEY_ID_RANGE_SIZE`

```c
#define ZEPHYR_PSA_BT_MESH_KEY_ID_RANGE_SIZE 0xC000
```

48 Ki（48 × 1024）。

<a id="a60948c97d6160f685985a3e4768403a7"></a>

### `ZEPHYR_PSA_FIDO2_KEY_ID_RANGE_BEGIN`

```c
#define ZEPHYR_PSA_FIDO2_KEY_ID_RANGE_BEGIN (psa_key_id_t)0x20011000
```

供 FIDO2 使用的 PSA 密钥 ID 范围（Key ID Range）。

<a id="aa39e59f3f1df32829af4e9189248d14b"></a>

### `ZEPHYR_PSA_FIDO2_KEY_ID_RANGE_SIZE`

```c
#define ZEPHYR_PSA_FIDO2_KEY_ID_RANGE_SIZE 0x1000
```

4 Ki（4 × 1024）。

<a id="ae4606ebca8aa09c0096897c927981cb6"></a>

### `ZEPHYR_PSA_MATTER_KEY_ID_RANGE_BEGIN`

```c
#define ZEPHYR_PSA_MATTER_KEY_ID_RANGE_BEGIN (psa_key_id_t)0x30000
```

供 Matter 使用的 PSA 密钥 ID 范围（Key ID Range）。

基础 ID（Base ID）与上游默认值相同，参见 [CHIPCryptoPALPSA.h](https://github.com/project-chip/connectedhomeip/blob/v1.4.0.0/src/crypto/CHIPCryptoPALPSA.h#L55)。

<a id="a6b459be7f0d6d39cd6bf8d482473b23f"></a>

### `ZEPHYR_PSA_MATTER_KEY_ID_RANGE_SIZE`

```c
#define ZEPHYR_PSA_MATTER_KEY_ID_RANGE_SIZE 0x10000
```

64 Ki（64 × 1024）。

<a id="a3e8bcbe8554a07e045a7330196c8a003"></a>

### `ZEPHYR_PSA_OPENTHREAD_KEY_ID_RANGE_BEGIN`

```c
#define ZEPHYR_PSA_OPENTHREAD_KEY_ID_RANGE_BEGIN (psa_key_id_t)0x20000
```

供 OpenThread 使用的 PSA 密钥 ID 范围（Key ID Range）。

基础 ID（Base ID）与上游默认值相同，参见 [OpenThread platform.h](https://github.com/openthread/openthread/blob/thread-reference-20230706/src/core/config/platform.h#L138)。

<a id="a484d6a1af8ccc3a869b9a2b7753d1c2c"></a>

### `ZEPHYR_PSA_OPENTHREAD_KEY_ID_RANGE_SIZE`

```c
#define ZEPHYR_PSA_OPENTHREAD_KEY_ID_RANGE_SIZE 0x10000
```

64 Ki（64 × 1024）。

<a id="ac02d47ca235e44f30e5fa32aa5cbfadc"></a>

### `ZEPHYR_PSA_WIFI_CREDENTIALS_KEY_ID_RANGE_BEGIN`

```c
#define ZEPHYR_PSA_WIFI_CREDENTIALS_KEY_ID_RANGE_BEGIN (psa_key_id_t)0x20010000
```

供 Wi-Fi 凭据管理（Credentials Management）使用的 PSA 密钥 ID 范围。

<a id="a86a47e671a632befdce9b201a66002d5"></a>

### `ZEPHYR_PSA_WIFI_CREDENTIALS_KEY_ID_RANGE_SIZE`

```c
#define ZEPHYR_PSA_WIFI_CREDENTIALS_KEY_ID_RANGE_SIZE 0x100
```

256。

<a id="a11e986351c65bd3dc3c0fe2cd9926e4b"></a>

### `psa_key_id_t`

```c
typedef uint32_t psa_key_id_t
```


## 24.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P429_key_ids.h_源码浏览.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [https://github.com/project-chip/connectedhomeip/blob/v1.4.0.0/src/crypto/CHIPCryptoPALPSA.h#L55](https://github.com/project-chip/connectedhomeip/blob/v1.4.0.0/src/crypto/CHIPCryptoPALPSA.h#L55)
- [https://github.com/openthread/openthread/blob/thread-reference-20230706/src/core/config/platform.h#L138](https://github.com/openthread/openthread/blob/thread-reference-20230706/src/core/config/platform.h#L138)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P023_zephyr__irq_nextlevel.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P025_zephyr__mpipe__mpipe_element.h_文件参考.md)
