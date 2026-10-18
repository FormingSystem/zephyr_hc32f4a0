---
id: learning.zephyr-docs.kconfig-reference.page-241
title: "`modules/mbedtls`配置项参考（1/3）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第241章\_`modules/mbedtls`配置项参考（1/3）

本章翻译官方 Kconfig 数据库中 `modules/mbedtls` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_APP_LINK_WITH_MBEDTLS"></a>

## 241.1 `CONFIG_APP_LINK_WITH_MBEDTLS`

**提示（Prompt）**：将应用目标 `app` 与 MBEDTLS 链接（link）

**说明（Help）**

将 MBEDTLS 头文件加入 `app` 的包含路径（include path）。如果这些路径对 `app` 造成别名冲突（aliasing issues），可以禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig:175`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig#L175)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS"></a>

## 241.2 `CONFIG_MBEDTLS`

**提示（Prompt）**：Mbed TLS 支持（Support）

**说明（Help）**

启用 Mbed TLS 密码库（cryptography library）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_PSA_CRYPTO_PROVIDER_MBEDTLS
CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_PSA_CRYPTO_PROVIDER_MBEDTLS
CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG
CONFIG_WIFI_ESP32
CONFIG_ESP32_WIFI_ENTERPRISE
CONFIG_BT_OBEX_AUTH
CONFIG_MCUMGR_TRANSPORT_UDP_DTLS
CONFIG_UPDATEHUB_DTLS
CONFIG_MCP_TRANSPORT_HTTP
CONFIG_LWM2M_DTLS_SUPPORT
CONFIG_QUIC_SOCKOPT_TLS
CONFIG_NET_SOCKETS_SOCKOPT_TLS
CONFIG_SSH_CRYPTO
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT)、[`CONFIG_PSA_CRYPTO_PROVIDER_MBEDTLS`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_PROVIDER_MBEDTLS)、[`CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG)、[`CONFIG_WIFI_ESP32`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32)、[`CONFIG_ESP32_WIFI_ENTERPRISE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_ENTERPRISE)、[`CONFIG_BT_OBEX_AUTH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBEX_AUTH)、[`CONFIG_MCUMGR_TRANSPORT_UDP_DTLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_UDP_DTLS)、[`CONFIG_UPDATEHUB_DTLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UPDATEHUB_DTLS)、[`CONFIG_MCP_TRANSPORT_HTTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCP_TRANSPORT_HTTP)、[`CONFIG_LWM2M_DTLS_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_DTLS_SUPPORT)、[`CONFIG_QUIC_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_SOCKOPT_TLS)、[`CONFIG_NET_SOCKETS_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_SOCKOPT_TLS)、[`CONFIG_SSH_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH_CRYPTO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SSH_CRYPTO`。

<a id="CONFIG_MBEDTLS_AES_FEWER_TABLES"></a>

## 241.3 `CONFIG_MBEDTLS_AES_FEWER_TABLES`

**提示（Prompt）**：将预计算 AES 表（precomputed AES tables）缩小约 6 kB

**说明（Help）**

缩小 AES 表（tables），代价是增加运行时算术运算。具体而言，将 4 次查表（table lookups）转换为 1 次查表、3 次加法和 6 次位移（bit shifts）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_AES_ROM_TABLES && CONFIG_PSA_WANT_KEY_TYPE_AES && CONFIG_MBEDTLS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → 使用存储在 ROM 中的预计算 AES 表（precomputed AES tables）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_AES_ROM_TABLES`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_AES_ROM_TABLES)、[`CONFIG_PSA_WANT_KEY_TYPE_AES`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_AES)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_AES_ROM_TABLES"></a>

## 241.4 `CONFIG_MBEDTLS_AES_ROM_TABLES`

**提示（Prompt）**：使用存储在 ROM 中的预计算 AES 表（precomputed AES tables）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_WANT_KEY_TYPE_AES && CONFIG_MBEDTLS
```

**被弱选择（Implied by）**

```text
CONFIG_BT_MESH_CRYPTO_LIB
CONFIG_BT_GATT_CACHING
CONFIG_BT_CRYPTO
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_PSA_WANT_KEY_TYPE_AES`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_AES)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_BT_MESH_CRYPTO_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_CRYPTO_LIB)、[`CONFIG_BT_GATT_CACHING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GATT_CACHING)、[`CONFIG_BT_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CRYPTO)。

<a id="CONFIG_MBEDTLS_ASN1_PARSE_C"></a>

## 241.5 `CONFIG_MBEDTLS_ASN1_PARSE_C`

**提示（Prompt）**：抽象语法记法一（ASN.1）解析函数支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**被选择（Selected by）**

```text
CONFIG_MBEDTLS_X509_USE_C
CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG
CONFIG_MBEDTLS_X509_USE_C
CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:186`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L186)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_X509_USE_C`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_X509_USE_C)、[`CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG)。

<a id="CONFIG_MBEDTLS_BASE64_C"></a>

## 241.6 `CONFIG_MBEDTLS_BASE64_C`

**提示（Prompt）**：Base64 模块

**说明（Help）**

此模块是隐私增强邮件格式（PEM）支持所必需的，X.509 又需要 PEM 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**被选择（Selected by）**

```text
CONFIG_MBEDTLS_PEM_PARSE_C
CONFIG_MBEDTLS_PEM_WRITE_C
CONFIG_MBEDTLS_PEM_PARSE_C
CONFIG_MBEDTLS_PEM_WRITE_C
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:217`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L217)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_PEM_PARSE_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_PEM_PARSE_C)、[`CONFIG_MBEDTLS_PEM_WRITE_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_PEM_WRITE_C)。

<a id="CONFIG_MBEDTLS_BUILTIN"></a>

## 241.7 `CONFIG_MBEDTLS_BUILTIN`

**提示（Prompt）**：Zephyr 源码树内的 Mbed TLS 版本（in-tree version）

**说明（Help）**

链接 Zephyr 发行版附带的 Mbed TLS 源码。该版本与 Zephyr 集成良好，并受 Zephyr 支持，是推荐给多数用户的选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MBEDTLS_IMPLEMENTATION>
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 实现（implementation）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_IMPLEMENTATION`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_IMPLEMENTATION)。

<a id="CONFIG_MBEDTLS_CFG_FILE"></a>

## 241.8 `CONFIG_MBEDTLS_CFG_FILE`

**提示（Prompt）**：Mbed TLS 配置文件（configuration file）［已弃用，DEPRECATED］

**说明（Help）**

此 Kconfig 选项已弃用，请改用 `MBEDTLS_CONFIG_FILE`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.deprecated:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.deprecated#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_CIPHER"></a>

## 241.9 `CONFIG_MBEDTLS_CIPHER`

**提示（Prompt）**：通用加解密层（Generic cipher layer）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_MBEDTLS_SSL_PROTO_TLS1_2
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_MBEDTLS_SSL_PROTO_TLS1_2
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:180`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L180)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT)、[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_2`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_2)。

<a id="CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8"></a>

## 241.10 `CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8`

**提示（Prompt）**：密码套件（Ciphersuite）`ECJPAKE_WITH_AES_128_CCM_8`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_SSL_PROTO_TLS1_2
CONFIG_MBEDTLS_KEY_EXCHANGE_ECJPAKE_ENABLED
CONFIG_PSA_WANT_ALG_JPAKE
CONFIG_PSA_WANT_ALG_CCM
CONFIG_PSA_WANT_KEY_TYPE_AES
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE
```

**弱选择（Implies）**

```text
CONFIG_PSA_WANT_ECC_SECP_R1_256
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.ciphersuites:149`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.ciphersuites#L149)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_2`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_2)、[`CONFIG_MBEDTLS_KEY_EXCHANGE_ECJPAKE_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_KEY_EXCHANGE_ECJPAKE_ENABLED)、[`CONFIG_PSA_WANT_ALG_JPAKE`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_JPAKE)、[`CONFIG_PSA_WANT_ALG_CCM`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_CCM)、[`CONFIG_PSA_WANT_KEY_TYPE_AES`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_AES)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE)、[`CONFIG_PSA_WANT_ECC_SECP_R1_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ECC_SECP_R1_256)。

<a id="CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256"></a>

## 241.11 `CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256`

**提示（Prompt）**：密码套件（Ciphersuite）`TLS1_3_AES_128_CCM_SHA256`

**说明（Help）**

默认情况下，此 Kconfig 选项弱选择（imply）使用 secp256r1 椭圆曲线的椭圆曲线数字签名算法（ECDSA）。可根据应用需要启用其他椭圆曲线或 RSA。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_SSL_PROTO_TLS1_3
CONFIG_PSA_WANT_ALG_SHA_256
CONFIG_PSA_WANT_KEY_TYPE_AES
CONFIG_PSA_WANT_ALG_CCM
```

**弱选择（Implies）**

```text
CONFIG_PSA_WANT_KEY_TYPE_ECC_PUBLIC_KEY
CONFIG_PSA_WANT_ALG_ECDSA
CONFIG_PSA_WANT_ECC_SECP_R1_256
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.ciphersuites:225`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.ciphersuites#L225)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_3`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_3)、[`CONFIG_PSA_WANT_ALG_SHA_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_256)、[`CONFIG_PSA_WANT_KEY_TYPE_AES`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_AES)、[`CONFIG_PSA_WANT_ALG_CCM`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_CCM)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_PUBLIC_KEY`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_PUBLIC_KEY)、[`CONFIG_PSA_WANT_ALG_ECDSA`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECDSA)、[`CONFIG_PSA_WANT_ECC_SECP_R1_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ECC_SECP_R1_256)。

<a id="CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256"></a>

## 241.12 `CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256`

**提示（Prompt）**：密码套件（Ciphersuite）`TLS1_3_AES_128_GCM_SHA256`

**说明（Help）**

默认情况下，此 Kconfig 选项弱选择（imply）使用 secp256r1 椭圆曲线的椭圆曲线数字签名算法（ECDSA）。可根据应用需要启用其他椭圆曲线或 RSA。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_SSL_PROTO_TLS1_3
CONFIG_PSA_WANT_ALG_SHA_256
CONFIG_PSA_WANT_KEY_TYPE_AES
CONFIG_PSA_WANT_ALG_GCM
```

**弱选择（Implies）**

```text
CONFIG_PSA_WANT_KEY_TYPE_ECC_PUBLIC_KEY
CONFIG_PSA_WANT_ALG_ECDSA
CONFIG_PSA_WANT_ECC_SECP_R1_256
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.ciphersuites:211`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.ciphersuites#L211)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_3`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_3)、[`CONFIG_PSA_WANT_ALG_SHA_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_256)、[`CONFIG_PSA_WANT_KEY_TYPE_AES`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_AES)、[`CONFIG_PSA_WANT_ALG_GCM`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_GCM)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_PUBLIC_KEY`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_PUBLIC_KEY)、[`CONFIG_PSA_WANT_ALG_ECDSA`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECDSA)、[`CONFIG_PSA_WANT_ECC_SECP_R1_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ECC_SECP_R1_256)。

<a id="CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384"></a>

## 241.13 `CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384`

**提示（Prompt）**：密码套件（Ciphersuite）`TLS1_3_AES_256_GCM_SHA384`

**说明（Help）**

默认情况下，此 Kconfig 选项弱选择（imply）使用 secp256r1 椭圆曲线的椭圆曲线数字签名算法（ECDSA）。可根据应用需要启用其他椭圆曲线或 RSA。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_SSL_PROTO_TLS1_3
CONFIG_PSA_WANT_ALG_SHA_384
CONFIG_PSA_WANT_KEY_TYPE_AES
CONFIG_PSA_WANT_ALG_GCM
```

**弱选择（Implies）**

```text
CONFIG_PSA_WANT_KEY_TYPE_ECC_PUBLIC_KEY
CONFIG_PSA_WANT_ALG_ECDSA
CONFIG_PSA_WANT_ECC_SECP_R1_256
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.ciphersuites:197`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.ciphersuites#L197)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_3`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_3)、[`CONFIG_PSA_WANT_ALG_SHA_384`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_384)、[`CONFIG_PSA_WANT_KEY_TYPE_AES`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_AES)、[`CONFIG_PSA_WANT_ALG_GCM`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_GCM)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_PUBLIC_KEY`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_PUBLIC_KEY)、[`CONFIG_PSA_WANT_ALG_ECDSA`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECDSA)、[`CONFIG_PSA_WANT_ECC_SECP_R1_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ECC_SECP_R1_256)。

<a id="CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256"></a>

## 241.14 `CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256`

**提示（Prompt）**：密码套件（Ciphersuite）`TLS1_3_CHACHA20_POLY1305_SHA256`

**说明（Help）**

默认情况下，此 Kconfig 选项弱选择（imply）使用 secp256r1 椭圆曲线的椭圆曲线数字签名算法（ECDSA）。可根据应用需要启用其他椭圆曲线或 RSA。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_SSL_PROTO_TLS1_3
CONFIG_PSA_WANT_ALG_SHA_256
CONFIG_PSA_WANT_KEY_TYPE_CHACHA20
CONFIG_PSA_WANT_ALG_CHACHA20_POLY1305
```

**弱选择（Implies）**

```text
CONFIG_PSA_WANT_KEY_TYPE_ECC_PUBLIC_KEY
CONFIG_PSA_WANT_ALG_ECDSA
CONFIG_PSA_WANT_ECC_SECP_R1_256
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.ciphersuites:239`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.ciphersuites#L239)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_3`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_3)、[`CONFIG_PSA_WANT_ALG_SHA_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_256)、[`CONFIG_PSA_WANT_KEY_TYPE_CHACHA20`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_CHACHA20)、[`CONFIG_PSA_WANT_ALG_CHACHA20_POLY1305`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_CHACHA20_POLY1305)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_PUBLIC_KEY`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_PUBLIC_KEY)、[`CONFIG_PSA_WANT_ALG_ECDSA`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECDSA)、[`CONFIG_PSA_WANT_ECC_SECP_R1_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ECC_SECP_R1_256)。

<a id="CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8"></a>

## 241.15 `CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8`

**提示（Prompt）**：密码套件（Ciphersuite）`TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_SSL_PROTO_TLS1_2
CONFIG_MBEDTLS_X509_CRT_PARSE_C
CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_ECDSA_ENABLED
CONFIG_PSA_WANT_ALG_TLS12_PRF
CONFIG_PSA_WANT_ALG_ECDH
CONFIG_PSA_WANT_ALG_ECDSA
CONFIG_PSA_WANT_ALG_SHA_256
CONFIG_PSA_WANT_ALG_CCM
CONFIG_PSA_WANT_KEY_TYPE_AES
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE
```

**弱选择（Implies）**

```text
CONFIG_PSA_WANT_ECC_SECP_R1_256
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.ciphersuites:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.ciphersuites#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_2`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_2)、[`CONFIG_MBEDTLS_X509_CRT_PARSE_C`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_X509_CRT_PARSE_C)、[`CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_ECDSA_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_ECDSA_ENABLED)、[`CONFIG_PSA_WANT_ALG_TLS12_PRF`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_TLS12_PRF)、[`CONFIG_PSA_WANT_ALG_ECDH`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECDH)、[`CONFIG_PSA_WANT_ALG_ECDSA`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECDSA)、[`CONFIG_PSA_WANT_ALG_SHA_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_256)、[`CONFIG_PSA_WANT_ALG_CCM`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_CCM)、[`CONFIG_PSA_WANT_KEY_TYPE_AES`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_AES)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE)、[`CONFIG_PSA_WANT_ECC_SECP_R1_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ECC_SECP_R1_256)。

<a id="CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256"></a>

## 241.16 `CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`

**提示（Prompt）**：密码套件（Ciphersuite）`TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_SSL_PROTO_TLS1_2
CONFIG_MBEDTLS_X509_CRT_PARSE_C
CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_ECDSA_ENABLED
CONFIG_PSA_WANT_ALG_TLS12_PRF
CONFIG_PSA_WANT_ALG_ECDH
CONFIG_PSA_WANT_ALG_ECDSA
CONFIG_PSA_WANT_ALG_SHA_256
CONFIG_PSA_WANT_ALG_GCM
CONFIG_PSA_WANT_KEY_TYPE_AES
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE
```

**被选择（Selected by）**

```text
CONFIG_ESP32_WIFI_ENTERPRISE
```

**弱选择（Implies）**

```text
CONFIG_PSA_WANT_ECC_SECP_R1_256
```

**被弱选择（Implied by）**

```text
CONFIG_QUIC_SOCKOPT_TLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.ciphersuites:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.ciphersuites#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_2`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_2)、[`CONFIG_MBEDTLS_X509_CRT_PARSE_C`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_X509_CRT_PARSE_C)、[`CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_ECDSA_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_ECDSA_ENABLED)、[`CONFIG_PSA_WANT_ALG_TLS12_PRF`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_TLS12_PRF)、[`CONFIG_PSA_WANT_ALG_ECDH`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECDH)、[`CONFIG_PSA_WANT_ALG_ECDSA`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECDSA)、[`CONFIG_PSA_WANT_ALG_SHA_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_256)、[`CONFIG_PSA_WANT_ALG_GCM`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_GCM)、[`CONFIG_PSA_WANT_KEY_TYPE_AES`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_AES)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE)、[`CONFIG_ESP32_WIFI_ENTERPRISE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_ENTERPRISE)、[`CONFIG_PSA_WANT_ECC_SECP_R1_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ECC_SECP_R1_256)、[`CONFIG_QUIC_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_SOCKOPT_TLS)。

<a id="CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384"></a>

## 241.17 `CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`

**提示（Prompt）**：密码套件（Ciphersuite）`TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_SSL_PROTO_TLS1_2
CONFIG_MBEDTLS_X509_CRT_PARSE_C
CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_ECDSA_ENABLED
CONFIG_PSA_WANT_ALG_TLS12_PRF
CONFIG_PSA_WANT_ALG_ECDH
CONFIG_PSA_WANT_ALG_ECDSA
CONFIG_PSA_WANT_ALG_SHA_384
CONFIG_PSA_WANT_ALG_GCM
CONFIG_PSA_WANT_KEY_TYPE_AES
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE
```

**被选择（Selected by）**

```text
CONFIG_ESP32_WIFI_SUITE_B_192
```

**弱选择（Implies）**

```text
CONFIG_PSA_WANT_ECC_SECP_R1_256
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.ciphersuites:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.ciphersuites#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_2`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_2)、[`CONFIG_MBEDTLS_X509_CRT_PARSE_C`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_X509_CRT_PARSE_C)、[`CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_ECDSA_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_ECDSA_ENABLED)、[`CONFIG_PSA_WANT_ALG_TLS12_PRF`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_TLS12_PRF)、[`CONFIG_PSA_WANT_ALG_ECDH`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECDH)、[`CONFIG_PSA_WANT_ALG_ECDSA`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECDSA)、[`CONFIG_PSA_WANT_ALG_SHA_384`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_384)、[`CONFIG_PSA_WANT_ALG_GCM`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_GCM)、[`CONFIG_PSA_WANT_KEY_TYPE_AES`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_AES)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE)、[`CONFIG_ESP32_WIFI_SUITE_B_192`](P189_drivers_wifi_配置项参考_2.md#CONFIG_ESP32_WIFI_SUITE_B_192)、[`CONFIG_PSA_WANT_ECC_SECP_R1_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ECC_SECP_R1_256)。

<a id="CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256"></a>

## 241.18 `CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`

**提示（Prompt）**：密码套件（Ciphersuite）`TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_SSL_PROTO_TLS1_2
CONFIG_MBEDTLS_X509_CRT_PARSE_C
CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_ECDSA_ENABLED
CONFIG_PSA_WANT_ALG_TLS12_PRF
CONFIG_PSA_WANT_ALG_ECDH
CONFIG_PSA_WANT_ALG_ECDSA
CONFIG_PSA_WANT_ALG_SHA_256
CONFIG_PSA_WANT_ALG_CHACHA20_POLY1305
CONFIG_PSA_WANT_KEY_TYPE_CHACHA20
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE
```

**弱选择（Implies）**

```text
CONFIG_PSA_WANT_ECC_SECP_R1_256
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.ciphersuites:161`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.ciphersuites#L161)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_2`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_2)、[`CONFIG_MBEDTLS_X509_CRT_PARSE_C`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_X509_CRT_PARSE_C)、[`CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_ECDSA_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_ECDSA_ENABLED)、[`CONFIG_PSA_WANT_ALG_TLS12_PRF`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_TLS12_PRF)、[`CONFIG_PSA_WANT_ALG_ECDH`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECDH)、[`CONFIG_PSA_WANT_ALG_ECDSA`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECDSA)、[`CONFIG_PSA_WANT_ALG_SHA_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_256)、[`CONFIG_PSA_WANT_ALG_CHACHA20_POLY1305`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_CHACHA20_POLY1305)、[`CONFIG_PSA_WANT_KEY_TYPE_CHACHA20`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_CHACHA20)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE)、[`CONFIG_PSA_WANT_ECC_SECP_R1_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ECC_SECP_R1_256)。

<a id="CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384"></a>

## 241.19 `CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384`

**提示（Prompt）**：密码套件（Ciphersuite）`TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_SSL_PROTO_TLS1_2
CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_PSK_ENABLED
CONFIG_PSA_WANT_ALG_TLS12_PRF
CONFIG_PSA_WANT_ALG_ECDH
CONFIG_PSA_WANT_ALG_ECDSA
CONFIG_PSA_WANT_ALG_SHA_384
CONFIG_PSA_WANT_ALG_CBC_NO_PADDING
CONFIG_PSA_WANT_KEY_TYPE_AES
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
```

**弱选择（Implies）**

```text
CONFIG_PSA_WANT_ECC_SECP_R1_256
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.ciphersuites:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.ciphersuites#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_2`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_2)、[`CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_PSK_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_PSK_ENABLED)、[`CONFIG_PSA_WANT_ALG_TLS12_PRF`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_TLS12_PRF)、[`CONFIG_PSA_WANT_ALG_ECDH`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECDH)、[`CONFIG_PSA_WANT_ALG_ECDSA`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECDSA)、[`CONFIG_PSA_WANT_ALG_SHA_384`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_384)、[`CONFIG_PSA_WANT_ALG_CBC_NO_PADDING`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_CBC_NO_PADDING)、[`CONFIG_PSA_WANT_KEY_TYPE_AES`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_AES)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT)、[`CONFIG_PSA_WANT_ECC_SECP_R1_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ECC_SECP_R1_256)。

<a id="CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256"></a>

## 241.20 `CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`

**提示（Prompt）**：密码套件（Ciphersuite）`TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_SSL_PROTO_TLS1_2
CONFIG_MBEDTLS_X509_CRT_PARSE_C
CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_RSA_ENABLED
CONFIG_PSA_WANT_ALG_TLS12_PRF
CONFIG_PSA_WANT_ALG_RSA_PSS
CONFIG_PSA_WANT_ALG_RSA_PKCS1V15_SIGN
CONFIG_PSA_WANT_ALG_ECDH
CONFIG_PSA_WANT_ALG_SHA_256
CONFIG_PSA_WANT_ALG_CBC_NO_PADDING
CONFIG_PSA_WANT_KEY_TYPE_AES
CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_IMPORT
CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_EXPORT
CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_GENERATE
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_ESP32_WIFI_ENTERPRISE
```

**弱选择（Implies）**

```text
CONFIG_PSA_WANT_ECC_SECP_R1_256
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.ciphersuites:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.ciphersuites#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_2`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_2)、[`CONFIG_MBEDTLS_X509_CRT_PARSE_C`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_X509_CRT_PARSE_C)、[`CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_RSA_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_RSA_ENABLED)、[`CONFIG_PSA_WANT_ALG_TLS12_PRF`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_TLS12_PRF)、[`CONFIG_PSA_WANT_ALG_RSA_PSS`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_RSA_PSS)、[`CONFIG_PSA_WANT_ALG_RSA_PKCS1V15_SIGN`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_RSA_PKCS1V15_SIGN)、[`CONFIG_PSA_WANT_ALG_ECDH`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECDH)、[`CONFIG_PSA_WANT_ALG_SHA_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_256)、[`CONFIG_PSA_WANT_ALG_CBC_NO_PADDING`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_CBC_NO_PADDING)、[`CONFIG_PSA_WANT_KEY_TYPE_AES`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_AES)、[`CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_IMPORT`](P243_modules_mbedtls_配置项参考_3.md#CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_IMPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_EXPORT`](P243_modules_mbedtls_配置项参考_3.md#CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_EXPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_GENERATE`](P243_modules_mbedtls_配置项参考_3.md#CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_GENERATE)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT)、[`CONFIG_ESP32_WIFI_ENTERPRISE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_ENTERPRISE)、[`CONFIG_PSA_WANT_ECC_SECP_R1_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ECC_SECP_R1_256)。

<a id="CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256"></a>

## 241.21 `CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`

**提示（Prompt）**：密码套件（Ciphersuite）`TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_SSL_PROTO_TLS1_2
CONFIG_MBEDTLS_X509_CRT_PARSE_C
CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_RSA_ENABLED
CONFIG_PSA_WANT_ALG_TLS12_PRF
CONFIG_PSA_WANT_ALG_RSA_PSS
CONFIG_PSA_WANT_ALG_RSA_PKCS1V15_SIGN
CONFIG_PSA_WANT_ALG_ECDH
CONFIG_PSA_WANT_ALG_SHA_256
CONFIG_PSA_WANT_ALG_GCM
CONFIG_PSA_WANT_KEY_TYPE_AES
CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_IMPORT
CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_EXPORT
CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_GENERATE
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE
```

**被选择（Selected by）**

```text
CONFIG_ESP32_WIFI_ENTERPRISE
```

**弱选择（Implies）**

```text
CONFIG_PSA_WANT_ECC_SECP_R1_256
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.ciphersuites:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.ciphersuites#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_2`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_2)、[`CONFIG_MBEDTLS_X509_CRT_PARSE_C`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_X509_CRT_PARSE_C)、[`CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_RSA_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_RSA_ENABLED)、[`CONFIG_PSA_WANT_ALG_TLS12_PRF`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_TLS12_PRF)、[`CONFIG_PSA_WANT_ALG_RSA_PSS`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_RSA_PSS)、[`CONFIG_PSA_WANT_ALG_RSA_PKCS1V15_SIGN`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_RSA_PKCS1V15_SIGN)、[`CONFIG_PSA_WANT_ALG_ECDH`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECDH)、[`CONFIG_PSA_WANT_ALG_SHA_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_256)、[`CONFIG_PSA_WANT_ALG_GCM`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_GCM)、[`CONFIG_PSA_WANT_KEY_TYPE_AES`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_AES)、[`CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_IMPORT`](P243_modules_mbedtls_配置项参考_3.md#CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_IMPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_EXPORT`](P243_modules_mbedtls_配置项参考_3.md#CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_EXPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_GENERATE`](P243_modules_mbedtls_配置项参考_3.md#CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_GENERATE)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE)、[`CONFIG_ESP32_WIFI_ENTERPRISE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_ENTERPRISE)、[`CONFIG_PSA_WANT_ECC_SECP_R1_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ECC_SECP_R1_256)。

<a id="CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384"></a>

## 241.22 `CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`

**提示（Prompt）**：密码套件（Ciphersuite）`TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_SSL_PROTO_TLS1_2
CONFIG_MBEDTLS_X509_CRT_PARSE_C
CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_RSA_ENABLED
CONFIG_PSA_WANT_ALG_TLS12_PRF
CONFIG_PSA_WANT_ALG_RSA_PSS
CONFIG_PSA_WANT_ALG_RSA_PKCS1V15_SIGN
CONFIG_PSA_WANT_ALG_ECDH
CONFIG_PSA_WANT_ALG_SHA_384
CONFIG_PSA_WANT_ALG_GCM
CONFIG_PSA_WANT_KEY_TYPE_AES
CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_IMPORT
CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_EXPORT
CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_GENERATE
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE
```

**被选择（Selected by）**

```text
CONFIG_ESP32_WIFI_SUITE_B_192
```

**弱选择（Implies）**

```text
CONFIG_PSA_WANT_ECC_SECP_R1_256
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.ciphersuites:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.ciphersuites#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_2`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_2)、[`CONFIG_MBEDTLS_X509_CRT_PARSE_C`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_X509_CRT_PARSE_C)、[`CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_RSA_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_RSA_ENABLED)、[`CONFIG_PSA_WANT_ALG_TLS12_PRF`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_TLS12_PRF)、[`CONFIG_PSA_WANT_ALG_RSA_PSS`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_RSA_PSS)、[`CONFIG_PSA_WANT_ALG_RSA_PKCS1V15_SIGN`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_RSA_PKCS1V15_SIGN)、[`CONFIG_PSA_WANT_ALG_ECDH`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECDH)、[`CONFIG_PSA_WANT_ALG_SHA_384`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_384)、[`CONFIG_PSA_WANT_ALG_GCM`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_GCM)、[`CONFIG_PSA_WANT_KEY_TYPE_AES`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_AES)、[`CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_IMPORT`](P243_modules_mbedtls_配置项参考_3.md#CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_IMPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_EXPORT`](P243_modules_mbedtls_配置项参考_3.md#CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_EXPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_GENERATE`](P243_modules_mbedtls_配置项参考_3.md#CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_GENERATE)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE)、[`CONFIG_ESP32_WIFI_SUITE_B_192`](P189_drivers_wifi_配置项参考_2.md#CONFIG_ESP32_WIFI_SUITE_B_192)、[`CONFIG_PSA_WANT_ECC_SECP_R1_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ECC_SECP_R1_256)。

<a id="CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256"></a>

## 241.23 `CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`

**提示（Prompt）**：密码套件（Ciphersuite）`TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_SSL_PROTO_TLS1_2
CONFIG_MBEDTLS_X509_CRT_PARSE_C
CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_RSA_ENABLED
CONFIG_PSA_WANT_ALG_TLS12_PRF
CONFIG_PSA_WANT_ALG_RSA_PSS
CONFIG_PSA_WANT_ALG_RSA_PKCS1V15_SIGN
CONFIG_PSA_WANT_ALG_ECDH
CONFIG_PSA_WANT_ALG_SHA_256
CONFIG_PSA_WANT_ALG_CHACHA20_POLY1305
CONFIG_PSA_WANT_KEY_TYPE_CHACHA20
CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_IMPORT
CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_EXPORT
CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_GENERATE
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE
```

**弱选择（Implies）**

```text
CONFIG_PSA_WANT_ECC_SECP_R1_256
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.ciphersuites:177`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.ciphersuites#L177)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_2`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_2)、[`CONFIG_MBEDTLS_X509_CRT_PARSE_C`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_X509_CRT_PARSE_C)、[`CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_RSA_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_RSA_ENABLED)、[`CONFIG_PSA_WANT_ALG_TLS12_PRF`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_TLS12_PRF)、[`CONFIG_PSA_WANT_ALG_RSA_PSS`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_RSA_PSS)、[`CONFIG_PSA_WANT_ALG_RSA_PKCS1V15_SIGN`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_RSA_PKCS1V15_SIGN)、[`CONFIG_PSA_WANT_ALG_ECDH`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECDH)、[`CONFIG_PSA_WANT_ALG_SHA_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_256)、[`CONFIG_PSA_WANT_ALG_CHACHA20_POLY1305`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_CHACHA20_POLY1305)、[`CONFIG_PSA_WANT_KEY_TYPE_CHACHA20`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_CHACHA20)、[`CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_IMPORT`](P243_modules_mbedtls_配置项参考_3.md#CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_IMPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_EXPORT`](P243_modules_mbedtls_配置项参考_3.md#CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_EXPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_GENERATE`](P243_modules_mbedtls_配置项参考_3.md#CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_GENERATE)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE)、[`CONFIG_PSA_WANT_ECC_SECP_R1_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ECC_SECP_R1_256)。

<a id="CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256"></a>

## 241.24 `CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256`

**提示（Prompt）**：密码套件（Ciphersuite）`TLS_PSK_WITH_AES_128_GCM_SHA256`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_SSL_PROTO_TLS1_2
CONFIG_MBEDTLS_KEY_EXCHANGE_PSK_ENABLED
CONFIG_PSA_WANT_ALG_TLS12_PSK_TO_MS
CONFIG_PSA_WANT_ALG_TLS12_PRF
CONFIG_PSA_WANT_ALG_GCM
CONFIG_PSA_WANT_ALG_SHA_256
CONFIG_PSA_WANT_KEY_TYPE_AES
CONFIG_PSA_WANT_KEY_TYPE_DERIVE
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.ciphersuites:138`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.ciphersuites#L138)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_2`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_2)、[`CONFIG_MBEDTLS_KEY_EXCHANGE_PSK_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_KEY_EXCHANGE_PSK_ENABLED)、[`CONFIG_PSA_WANT_ALG_TLS12_PSK_TO_MS`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_TLS12_PSK_TO_MS)、[`CONFIG_PSA_WANT_ALG_TLS12_PRF`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_TLS12_PRF)、[`CONFIG_PSA_WANT_ALG_GCM`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_GCM)、[`CONFIG_PSA_WANT_ALG_SHA_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_256)、[`CONFIG_PSA_WANT_KEY_TYPE_AES`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_AES)、[`CONFIG_PSA_WANT_KEY_TYPE_DERIVE`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_DERIVE)。

<a id="CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384"></a>

## 241.25 `CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384`

**提示（Prompt）**：密码套件（Ciphersuite）`TLS_PSK_WITH_AES_256_CBC_SHA384`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_SSL_PROTO_TLS1_2
CONFIG_MBEDTLS_KEY_EXCHANGE_PSK_ENABLED
CONFIG_PSA_WANT_ALG_TLS12_PSK_TO_MS
CONFIG_PSA_WANT_ALG_TLS12_PRF
CONFIG_PSA_WANT_ALG_CBC_NO_PADDING
CONFIG_PSA_WANT_ALG_SHA_384
CONFIG_PSA_WANT_KEY_TYPE_AES
CONFIG_PSA_WANT_KEY_TYPE_DERIVE
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.ciphersuites:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.ciphersuites#L127)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_2`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_2)、[`CONFIG_MBEDTLS_KEY_EXCHANGE_PSK_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_KEY_EXCHANGE_PSK_ENABLED)、[`CONFIG_PSA_WANT_ALG_TLS12_PSK_TO_MS`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_TLS12_PSK_TO_MS)、[`CONFIG_PSA_WANT_ALG_TLS12_PRF`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_TLS12_PRF)、[`CONFIG_PSA_WANT_ALG_CBC_NO_PADDING`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_CBC_NO_PADDING)、[`CONFIG_PSA_WANT_ALG_SHA_384`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_384)、[`CONFIG_PSA_WANT_KEY_TYPE_AES`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_AES)、[`CONFIG_PSA_WANT_KEY_TYPE_DERIVE`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_DERIVE)。

<a id="CONFIG_MBEDTLS_CIPHER_ALL_ENABLED"></a>

## 241.26 `CONFIG_MBEDTLS_CIPHER_ALL_ENABLED`

**提示（Prompt）**：全部可用密码算法与模式（ciphers and modes）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_PSA_WANT_KEY_TYPE_AES
CONFIG_PSA_WANT_KEY_TYPE_CAMELLIA
CONFIG_PSA_WANT_KEY_TYPE_CHACHA20
CONFIG_PSA_WANT_ALG_GCM
CONFIG_PSA_WANT_ALG_CCM
CONFIG_PSA_WANT_ALG_CBC_NO_PADDING
CONFIG_PSA_WANT_ALG_CBC_PKCS7
CONFIG_PSA_WANT_ALG_CTR
CONFIG_PSA_WANT_ALG_CHACHA20_POLY1305
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_PSA_WANT_KEY_TYPE_AES`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_AES)、[`CONFIG_PSA_WANT_KEY_TYPE_CAMELLIA`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_CAMELLIA)、[`CONFIG_PSA_WANT_KEY_TYPE_CHACHA20`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_CHACHA20)、[`CONFIG_PSA_WANT_ALG_GCM`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_GCM)、[`CONFIG_PSA_WANT_ALG_CCM`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_CCM)、[`CONFIG_PSA_WANT_ALG_CBC_NO_PADDING`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_CBC_NO_PADDING)、[`CONFIG_PSA_WANT_ALG_CBC_PKCS7`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_CBC_PKCS7)、[`CONFIG_PSA_WANT_ALG_CTR`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_CTR)、[`CONFIG_PSA_WANT_ALG_CHACHA20_POLY1305`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_CHACHA20_POLY1305)。

<a id="CONFIG_MBEDTLS_CONFIG_FILE"></a>

## 241.27 `CONFIG_MBEDTLS_CONFIG_FILE`

**提示（Prompt）**：Mbed TLS 配置文件（configuration file）

**说明（Help）**

使用指定的 Mbed TLS 配置文件（configuration file）。默认配置文件可通过 Kconfig 调整，适合与互联网上多数 HTTPS 服务器通信，但启用的功能相对较多。针对特定 TLS 用途优化资源时，可使用已有 Kconfig 选项，或选择其他配置。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**默认值（Defaults）**

```text
CONFIG_MBEDTLS_CFG_FILE if CONFIG_MBEDTLS_CFG_FILE != ""
"config-mbedtls.h"
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_CFG_FILE`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CFG_FILE)。

<a id="CONFIG_MBEDTLS_CTR_DRBG_C"></a>

## 241.28 `CONFIG_MBEDTLS_CTR_DRBG_C`

**提示（Prompt）**：基于 AES-256 的计数器模式确定性随机比特生成器（CTR_DRBG）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_ESP32_BT_LE_CRYPTO_STACK_MBEDTLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:116`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L116)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT)、[`CONFIG_ESP32_BT_LE_CRYPTO_STACK_MBEDTLS`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_CRYPTO_STACK_MBEDTLS)。

<a id="CONFIG_MBEDTLS_CUSTOM"></a>

## 241.29 `CONFIG_MBEDTLS_CUSTOM`

**提示（Prompt）**：自定义 Mbed TLS 库（Custom library）

**说明（Help）**

Mbed TLS 库必须在源码树外（out of tree）配置并添加。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MBEDTLS_IMPLEMENTATION>
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 实现（implementation）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_IMPLEMENTATION`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_IMPLEMENTATION)。

<a id="CONFIG_MBEDTLS_DEBUG"></a>

## 241.30 `CONFIG_MBEDTLS_DEBUG`

**提示（Prompt）**：启用 Mbed TLS 调试（debug activation）

**说明（Help）**

为 Mbed TLS 配置启用调试。如果使用 Mbed TLS／Zephyr 集成，例如原生 TLS 套接字（native TLS sockets），此项会激活调试日志。

如果直接使用 Mbed TLS，则需要自行进行额外配置，在应用中调用：

```c
mbedtls_ssl_conf_dbg(&mbedtls.conf, zephyr_mbedtls_debug, NULL);
```

如果 `zephyr_mbedtls_debug()` 不满足需求，也可以自行实现调试钩子函数（debug hook function）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**弱选择（Implies）**

```text
CONFIG_MBEDTLS_DEBUG_C
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_DEBUG_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_DEBUG_C)。

<a id="CONFIG_MBEDTLS_DEBUG_C"></a>

## 241.31 `CONFIG_MBEDTLS_DEBUG_C`

**提示（Prompt）**：调试函数（Debug functions），仅用于 TLS 和 X.509

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**被弱选择（Implied by）**

```text
CONFIG_MBEDTLS_DEBUG
CONFIG_MBEDTLS_DEBUG
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:226`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L226)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_DEBUG`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_DEBUG)。

<a id="CONFIG_MBEDTLS_DEBUG_EXTRACT_BASENAME"></a>

## 241.32 `CONFIG_MBEDTLS_DEBUG_EXTRACT_BASENAME`

**提示（Prompt）**：从文件名中提取基本名称（basename）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_DEBUG && CONFIG_MBEDTLS
```

**默认值（Defaults）**

```text
CONFIG_MBEDTLS_DEBUG_EXTRACT_BASENAME_AT_BUILDTIME if "zephyr" = "zephyr"
CONFIG_MBEDTLS_DEBUG_EXTRACT_BASENAME_AT_RUNTIME
```

**可选项（Choices）**

```text
CONFIG_MBEDTLS_DEBUG_EXTRACT_BASENAME_AT_BUILDTIME
CONFIG_MBEDTLS_DEBUG_EXTRACT_BASENAME_AT_RUNTIME
CONFIG_MBEDTLS_DEBUG_EXTRACT_BASENAME_DISABLED
CONFIG_MBEDTLS_DEBUG_EXTRACT_BASENAME_AT_BUILDTIME
CONFIG_MBEDTLS_DEBUG_EXTRACT_BASENAME_AT_RUNTIME
CONFIG_MBEDTLS_DEBUG_EXTRACT_BASENAME_DISABLED
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig:122`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig#L122)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → 启用 Mbed TLS 调试（debug activation）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_DEBUG`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_DEBUG)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_DEBUG_EXTRACT_BASENAME_AT_BUILDTIME`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_DEBUG_EXTRACT_BASENAME_AT_BUILDTIME)、[`CONFIG_MBEDTLS_DEBUG_EXTRACT_BASENAME_AT_RUNTIME`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_DEBUG_EXTRACT_BASENAME_AT_RUNTIME)、[`CONFIG_MBEDTLS_DEBUG_EXTRACT_BASENAME_DISABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_DEBUG_EXTRACT_BASENAME_DISABLED)。

<a id="CONFIG_MBEDTLS_DEBUG_EXTRACT_BASENAME_AT_BUILDTIME"></a>

## 241.33 `CONFIG_MBEDTLS_DEBUG_EXTRACT_BASENAME_AT_BUILDTIME`

**提示（Prompt）**：构建时（Buildtime）

**说明（Help）**

添加编译选项，将 `__FILE__` 宏中的完整源码路径转换为文件基本名称（basename）。启用调试消息时，可减少代码占用。这取决于编译器；如果不起作用，请改用 `MBEDTLS_DEBUG_EXTRACT_BASENAME_AT_RUNTIME`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MBEDTLS_DEBUG_EXTRACT_BASENAME>
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig#L127)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → 启用 Mbed TLS 调试（debug activation） → 从文件名中提取基本名称（basename）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_DEBUG_EXTRACT_BASENAME`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_DEBUG_EXTRACT_BASENAME)。

<a id="CONFIG_MBEDTLS_DEBUG_EXTRACT_BASENAME_AT_RUNTIME"></a>

## 241.34 `CONFIG_MBEDTLS_DEBUG_EXTRACT_BASENAME_AT_RUNTIME`

**提示（Prompt）**：运行时（Runtime）

**说明（Help）**

去除传给调试钩子（debug hook）的文件名参数中的目录部分，只保留并记录基本名称（basename）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MBEDTLS_DEBUG_EXTRACT_BASENAME>
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig:137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig#L137)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → 启用 Mbed TLS 调试（debug activation） → 从文件名中提取基本名称（basename）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_DEBUG_EXTRACT_BASENAME`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_DEBUG_EXTRACT_BASENAME)。

<a id="CONFIG_MBEDTLS_DEBUG_EXTRACT_BASENAME_DISABLED"></a>

## 241.35 `CONFIG_MBEDTLS_DEBUG_EXTRACT_BASENAME_DISABLED`

**提示（Prompt）**：禁用（Disabled）

**说明（Help）**

禁用从日志消息的文件名中提取基本名称（basename）。这样，Mbed TLS 库生成的日志消息中将出现完整路径，或相对于 west 根目录的路径。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MBEDTLS_DEBUG_EXTRACT_BASENAME>
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig:143`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig#L143)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → 启用 Mbed TLS 调试（debug activation） → 从文件名中提取基本名称（basename）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_DEBUG_EXTRACT_BASENAME`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_DEBUG_EXTRACT_BASENAME)。

<a id="CONFIG_MBEDTLS_DEBUG_LEVEL"></a>

## 241.36 `CONFIG_MBEDTLS_DEBUG_LEVEL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Zephyr 集成代码默认使用的 Mbed TLS 调试日志级别，原文引用路径为 `ext/lib/crypto/mbedtls/include/mbedtls/debug.h`：

- `0`：不调试（No debug）。
- `1`：错误（Error）。
- `2`：状态变化（State change）。
- `3`：信息（Information）。
- `4`：详细（Verbose）。

此项使 Zephyr 在 Mbed TLS 初始化期间调用 `mbedtls_debug_set_threshold()`，传入所配置的调试日志级别。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_DEBUG && CONFIG_MBEDTLS
```

**默认值（Defaults）**

```text
4 if CONFIG_MBEDTLS_LOG_LEVEL_DBG
3 if CONFIG_MBEDTLS_LOG_LEVEL_INF
2 if CONFIG_MBEDTLS_LOG_LEVEL_WRN
1 if CONFIG_MBEDTLS_LOG_LEVEL_ERR
0
```

**取值范围（Ranges）**

```text
[0, 4]
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig:102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig#L102)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → 启用 Mbed TLS 调试（debug activation）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_DEBUG`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_DEBUG)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_LOG_LEVEL_DBG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_LOG_LEVEL_DBG)、[`CONFIG_MBEDTLS_LOG_LEVEL_INF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_LOG_LEVEL_INF)、[`CONFIG_MBEDTLS_LOG_LEVEL_WRN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_LOG_LEVEL_WRN)、[`CONFIG_MBEDTLS_LOG_LEVEL_ERR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_LOG_LEVEL_ERR)。

<a id="CONFIG_MBEDTLS_DEBUG_STRIP_NEWLINE"></a>

## 241.37 `CONFIG_MBEDTLS_DEBUG_STRIP_NEWLINE`

**提示（Prompt）**：去除换行符（Strip newlines）

**说明（Help）**

如果日志字符串的最后一个字符是换行符（newline），则尝试将其去除。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_DEBUG && CONFIG_MBEDTLS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig:152`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig#L152)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → 启用 Mbed TLS 调试（debug activation）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_DEBUG`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_DEBUG)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_DECLARE_PRIVATE_IDENTIFIERS"></a>

## 241.38 `CONFIG_MBEDTLS_DECLARE_PRIVATE_IDENTIFIERS`

**提示（Prompt）**：旧式密码功能支持（Legacy crypto support，私有）

**说明（Help）**

旧式密码功能（legacy crypto）现在是 TF-PSA-Crypto 内部的私有实现，不应由新代码使用。仅在迁移仍需旧声明的调用者时启用此项：定义 `MBEDTLS_DECLARE_PRIVATE_IDENTIFIERS` 后，可通过 `mbedtls/private/*.h` 访问这些 API；相关文件位于 mbedtls 目标导出的 TF-PSA-Crypto 内建包含路径下。长期目标是在所有用户迁移到 PSA Crypto API 后移除此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_ESP32_BT_LE_CRYPTO_STACK_MBEDTLS
CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:447`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L447)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA)、[`CONFIG_ESP32_BT_LE_CRYPTO_STACK_MBEDTLS`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_CRYPTO_STACK_MBEDTLS)、[`CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO)。

<a id="CONFIG_MBEDTLS_ECP_NIST_OPTIM"></a>

## 241.39 `CONFIG_MBEDTLS_ECP_NIST_OPTIM`

**提示（Prompt）**：NIST 曲线优化（curves optimization）

**说明（Help）**

为每个 NIST 素数启用专用的模 p 运算例程（modulo p routines）。根据素数和架构不同，可使对应曲线上的运算加快 4～8 倍，代价是约减表（reduction tables）占用少量闪存。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_BASIC && CONFIG_MBEDTLS
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP
CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG
CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP
CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP
CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_BASIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_BASIC)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP)、[`CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_BASIC`。

<a id="CONFIG_MBEDTLS_ENABLE_HEAP"></a>

## 241.40 `CONFIG_MBEDTLS_ENABLE_HEAP`

**提示（Prompt）**：Mbed TLS 全局堆（Global heap）

**说明（Help）**

使 Mbed TLS 使用专用堆（dedicated heap）。此设置必须是全局的，因为 Mbed TLS 只能定义一个堆，Zephyr 中不同的应用和库不应分别自行设置。若同时启用本选项和 `MBEDTLS_INIT`，Zephyr 会在设备启动期间自动初始化该堆。禁用时，Mbed TLS 使用系统默认堆。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_MEMORY_BUFFER_ALLOC_C
```

**被选择（Selected by）**

```text
CONFIG_CRYPTO_MBEDTLS_SHIM
CONFIG_MCUMGR_TRANSPORT_UDP_DTLS
CONFIG_UPDATEHUB_DTLS
```

**被弱选择（Implied by）**

```text
CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG
CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:143`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L143)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_MEMORY_BUFFER_ALLOC_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_MEMORY_BUFFER_ALLOC_C)、[`CONFIG_CRYPTO_MBEDTLS_SHIM`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_MBEDTLS_SHIM)、[`CONFIG_MCUMGR_TRANSPORT_UDP_DTLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_UDP_DTLS)、[`CONFIG_UPDATEHUB_DTLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UPDATEHUB_DTLS)、[`CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG)。

<a id="CONFIG_MBEDTLS_ENTROPY_C"></a>

## 241.41 `CONFIG_MBEDTLS_ENTROPY_C`

**提示（Prompt）**：Mbed TLS 熵累加器（entropy accumulator）

**说明（Help）**

此模块从已启用的熵源（entropy sources）收集熵数据，通常与 `CTR_DRBG` 或 `HMAC_DRBG` 配合，创建确定性随机数生成器（deterministic random number generator）。它要求启用 `PSA_WANT_ALG_SHA_256` 或 `PSA_WANT_ALG_SHA_512`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_PSA_WANT_ALG_SHA_256 if !CONFIG_PSA_WANT_ALG_SHA_512
```

**被选择（Selected by）**

```text
CONFIG_MBEDTLS_PSA_CRYPTO_LEGACY_RNG
CONFIG_MBEDTLS_PSA_CRYPTO_LEGACY_RNG
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:244`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L244)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_PSA_WANT_ALG_SHA_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_256)、[`CONFIG_PSA_WANT_ALG_SHA_512`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_512)、[`CONFIG_MBEDTLS_PSA_CRYPTO_LEGACY_RNG`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_PSA_CRYPTO_LEGACY_RNG)。

<a id="CONFIG_MBEDTLS_HASH_ALL_ENABLED"></a>

## 241.42 `CONFIG_MBEDTLS_HASH_ALL_ENABLED`

**提示（Prompt）**：全部可用消息认证码方法（MAC methods）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_PSA_WANT_ALG_MD5
CONFIG_PSA_WANT_ALG_SHA_1
CONFIG_PSA_WANT_ALG_SHA_224
CONFIG_PSA_WANT_ALG_SHA_256
CONFIG_PSA_WANT_ALG_SHA_384
CONFIG_PSA_WANT_ALG_SHA_512
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_PSA_WANT_ALG_MD5`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_MD5)、[`CONFIG_PSA_WANT_ALG_SHA_1`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_1)、[`CONFIG_PSA_WANT_ALG_SHA_224`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_224)、[`CONFIG_PSA_WANT_ALG_SHA_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_256)、[`CONFIG_PSA_WANT_ALG_SHA_384`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_384)、[`CONFIG_PSA_WANT_ALG_SHA_512`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_512)。

<a id="CONFIG_MBEDTLS_HAVE_ASM"></a>

## 241.43 `CONFIG_MBEDTLS_HAVE_ASM`

**提示（Prompt）**：使用汇编代码（assembly code）

**说明（Help）**

在 Mbed TLS 中启用汇编代码（assembly code）。可提高非对称密码（asymmetric cryptography）的性能，但可能影响代码体积。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**默认值（Defaults）**

```text
y if !CONFIG_ARM || CONFIG_ARMV7_M_ARMV8_M_MAINLINE
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:234`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L234)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ARMV7_M_ARMV8_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_M_ARMV8_M_MAINLINE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT)。

<a id="CONFIG_MBEDTLS_HAVE_TIME_DATE"></a>

## 241.44 `CONFIG_MBEDTLS_HAVE_TIME_DATE`

**提示（Prompt）**：Mbed TLS 日期／时间验证（Date/time validation）

**说明（Help）**

系统具有 `time.h`、`time()` 和 `gmtime_r()` 实现。系统还需要有效的时间源（time source），因为 Mbed TLS 在证书验证（certificate validation）时要求有效日期／时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:233`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L233)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_HEAP_CUSTOM_SECTION"></a>

## 241.45 `CONFIG_MBEDTLS_HEAP_CUSTOM_SECTION`

**提示（Prompt）**：为 Mbed TLS 堆使用自定义段（custom section）

**说明（Help）**

将 Mbed TLS 堆放在标记为 `.mbedtls_heap` 的自定义段中。自定义链接器脚本（linker scripts）可据此将堆重定位到特定位置，例如其他 SRAM 区域或外部内存。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_ENABLE_HEAP && CONFIG_MBEDTLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:171`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L171)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 全局堆（Global heap）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_ENABLE_HEAP`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_ENABLE_HEAP)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_HEAP_SIZE"></a>

## 241.46 `CONFIG_MBEDTLS_HEAP_SIZE`

**提示（Prompt）**：Mbed TLS 堆大小（Heap size）

**说明（Help）**

启用后，Mbed TLS 例程使用此堆，详情参见 `MBEDTLS_MEMORY_BUFFER_ALLOC_C`。堆大小依赖应用，因此不设置默认值。与互联网上任意 HTTPS 服务器进行流式通信（streaming communication）时，可能需要 32 KB 加额外开销，后者最多还需约 20 KB。某些专用且范围有限的 Mbed TLS API 用法可能只需 1000 字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_ENABLE_HEAP && CONFIG_MBEDTLS
```

**默认值（Defaults）**

```text
15360 if CONFIG_OPENTHREAD_COMMISSIONER || CONFIG_OPENTHREAD_JOINER
1024 if CONFIG_OPENTHREAD_CRYPTO_PSA
512
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:157`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L157)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 全局堆（Global heap）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_ENABLE_HEAP`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_ENABLE_HEAP)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_OPENTHREAD_COMMISSIONER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_COMMISSIONER)、[`CONFIG_OPENTHREAD_JOINER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_JOINER)、[`CONFIG_OPENTHREAD_CRYPTO_PSA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_CRYPTO_PSA)。

<a id="CONFIG_MBEDTLS_HMAC_DRBG_C"></a>

## 241.47 `CONFIG_MBEDTLS_HMAC_DRBG_C`

**提示（Prompt）**：基于 HMAC 的确定性随机比特生成器（HMAC_DRBG）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_MD_C
```

**被选择（Selected by）**

```text
CONFIG_MBEDTLS_PSA_CRYPTO_LEGACY_RNG
CONFIG_MBEDTLS_PSA_CRYPTO_LEGACY_RNG
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_MD_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_MD_C)、[`CONFIG_MBEDTLS_PSA_CRYPTO_LEGACY_RNG`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_PSA_CRYPTO_LEGACY_RNG)。

<a id="CONFIG_MBEDTLS_IMPLEMENTATION"></a>

## 241.48 `CONFIG_MBEDTLS_IMPLEMENTATION`

**提示（Prompt）**：Mbed TLS 实现（implementation）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**默认值（Defaults）**

```text
CONFIG_MBEDTLS_BUILTIN
```

**可选项（Choices）**

```text
CONFIG_MBEDTLS_BUILTIN
CONFIG_MBEDTLS_CUSTOM
CONFIG_MBEDTLS_BUILTIN
CONFIG_MBEDTLS_CUSTOM
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS_CUSTOM`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CUSTOM)。

<a id="CONFIG_MBEDTLS_INIT"></a>

## 241.49 `CONFIG_MBEDTLS_INIT`

**提示（Prompt）**：启动时初始化 Mbed TLS

**说明（Help）**

默认在 Zephyr 初始化阶段初始化 Mbed TLS。禁用此项会推迟初始化，直到显式调用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig:161`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig#L161)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_KEY_EXCHANGE_ALL_ENABLED"></a>

## 241.50 `CONFIG_MBEDTLS_KEY_EXCHANGE_ALL_ENABLED`

**提示（Prompt）**：全部可用密码套件模式（ciphersuite modes）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_MD_C
CONFIG_MBEDTLS_X509_CRT_PARSE_C
CONFIG_MBEDTLS_KEY_EXCHANGE_PSK_ENABLED
CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_PSK_ENABLED
CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_RSA_ENABLED
CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_ECDSA_ENABLED
CONFIG_MBEDTLS_KEY_EXCHANGE_ECJPAKE_ENABLED
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:153`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L153)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration） → 密码套件配置（Ciphersuite configuration）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_MD_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_MD_C)、[`CONFIG_MBEDTLS_X509_CRT_PARSE_C`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_X509_CRT_PARSE_C)、[`CONFIG_MBEDTLS_KEY_EXCHANGE_PSK_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_KEY_EXCHANGE_PSK_ENABLED)、[`CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_PSK_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_PSK_ENABLED)、[`CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_RSA_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_RSA_ENABLED)、[`CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_ECDSA_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_ECDSA_ENABLED)、[`CONFIG_MBEDTLS_KEY_EXCHANGE_ECJPAKE_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_KEY_EXCHANGE_ECJPAKE_ENABLED)。

<a id="CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_ECDSA_ENABLED"></a>

## 241.51 `CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_ECDSA_ENABLED`

**提示（Prompt）**：基于 ECDHE-ECDSA 的密码套件模式（ciphersuite modes）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_WANT_ALG_ECDH && CONFIG_PSA_WANT_ALG_ECDSA && CONFIG_MBEDTLS_X509_CRT_PARSE_C && CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE
CONFIG_MBEDTLS_KEY_EXCHANGE_ALL_ENABLED
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE
CONFIG_MBEDTLS_KEY_EXCHANGE_ALL_ENABLED
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG
```

**被弱选择（Implied by）**

```text
CONFIG_QUIC_SOCKOPT_TLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:190`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L190)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration） → 密码套件配置（Ciphersuite configuration）

**配置项引用（Symbol References）**：[`CONFIG_PSA_WANT_ALG_ECDH`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECDH)、[`CONFIG_PSA_WANT_ALG_ECDSA`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECDSA)、[`CONFIG_MBEDTLS_X509_CRT_PARSE_C`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_X509_CRT_PARSE_C)、[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_MBEDTLS_KEY_EXCHANGE_ALL_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_KEY_EXCHANGE_ALL_ENABLED)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256)、[`CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG)、[`CONFIG_QUIC_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_SOCKOPT_TLS)。

<a id="CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_PSK_ENABLED"></a>

## 241.52 `CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_PSK_ENABLED`

**提示（Prompt）**：基于 ECDHE-PSK 的密码套件模式（ciphersuite modes）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_BASIC && CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**被选择（Selected by）**

```text
CONFIG_MBEDTLS_KEY_EXCHANGE_ALL_ENABLED
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_KEY_EXCHANGE_ALL_ENABLED
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:166`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L166)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration） → 密码套件配置（Ciphersuite configuration）

**配置项引用（Symbol References）**：[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_BASIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_BASIC)、[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_KEY_EXCHANGE_ALL_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_KEY_EXCHANGE_ALL_ENABLED)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_BASIC`。

<a id="CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_RSA_ENABLED"></a>

## 241.53 `CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_RSA_ENABLED`

**提示（Prompt）**：基于 ECDHE-RSA 的密码套件模式（ciphersuite modes）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_BASIC && CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_BASIC && CONFIG_MBEDTLS_X509_CRT_PARSE_C && CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**被选择（Selected by）**

```text
CONFIG_MBEDTLS_KEY_EXCHANGE_ALL_ENABLED
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_KEY_EXCHANGE_ALL_ENABLED
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:184`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L184)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration） → 密码套件配置（Ciphersuite configuration）

**配置项引用（Symbol References）**：[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_BASIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_BASIC)、[`CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_BASIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_BASIC)、[`CONFIG_MBEDTLS_X509_CRT_PARSE_C`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_X509_CRT_PARSE_C)、[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_KEY_EXCHANGE_ALL_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_KEY_EXCHANGE_ALL_ENABLED)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_BASIC`、`CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_BASIC`。

<a id="CONFIG_MBEDTLS_KEY_EXCHANGE_ECJPAKE_ENABLED"></a>

## 241.54 `CONFIG_MBEDTLS_KEY_EXCHANGE_ECJPAKE_ENABLED`

**提示（Prompt）**：基于 ECJPAKE 的密码套件模式（ciphersuite modes）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_WANT_ALG_JPAKE && CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**被选择（Selected by）**

```text
CONFIG_MBEDTLS_KEY_EXCHANGE_ALL_ENABLED
CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8
CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG
CONFIG_MBEDTLS_KEY_EXCHANGE_ALL_ENABLED
CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8
CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:195`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L195)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration） → 密码套件配置（Ciphersuite configuration）

**配置项引用（Symbol References）**：[`CONFIG_PSA_WANT_ALG_JPAKE`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_JPAKE)、[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_KEY_EXCHANGE_ALL_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_KEY_EXCHANGE_ALL_ENABLED)、[`CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8)、[`CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG)。

<a id="CONFIG_MBEDTLS_KEY_EXCHANGE_PSK_ENABLED"></a>

## 241.55 `CONFIG_MBEDTLS_KEY_EXCHANGE_PSK_ENABLED`

**提示（Prompt）**：基于预共享密钥（PSK）的密码套件模式（ciphersuite modes）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**被选择（Selected by）**

```text
CONFIG_MBEDTLS_KEY_EXCHANGE_ALL_ENABLED
CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_KEY_EXCHANGE_ALL_ENABLED
CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:163`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L163)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration） → 密码套件配置（Ciphersuite configuration）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_KEY_EXCHANGE_ALL_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_KEY_EXCHANGE_ALL_ENABLED)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256)。

<a id="CONFIG_MBEDTLS_LMS_C"></a>

## 241.56 `CONFIG_MBEDTLS_LMS_C`

**提示（Prompt）**：支持 LMS 签名方案（signature schemes）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_PSA_CRYPTO_CLIENT && CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_PSA_WANT_ALG_SHA_256
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:364`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L364)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_PSA_CRYPTO_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PSA_CRYPTO_CLIENT)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_PSA_WANT_ALG_SHA_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_256)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MBEDTLS_PSA_CRYPTO_CLIENT`。

<a id="CONFIG_MBEDTLS_MD_C"></a>

## 241.57 `CONFIG_MBEDTLS_MD_C`

**提示（Prompt）**：通用消息摘要层（Generic message digest layer）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_MBEDTLS_SSL_PROTO_TLS1_2
CONFIG_MBEDTLS_KEY_EXCHANGE_ALL_ENABLED
CONFIG_MBEDTLS_HMAC_DRBG_C
CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_MBEDTLS_SSL_PROTO_TLS1_2
CONFIG_MBEDTLS_KEY_EXCHANGE_ALL_ENABLED
CONFIG_MBEDTLS_HMAC_DRBG_C
CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG
CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:183`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L183)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT)、[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_2`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_2)、[`CONFIG_MBEDTLS_KEY_EXCHANGE_ALL_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_KEY_EXCHANGE_ALL_ENABLED)、[`CONFIG_MBEDTLS_HMAC_DRBG_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_HMAC_DRBG_C)、[`CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG)、[`CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO)。

<a id="CONFIG_MBEDTLS_MEMORY_BUFFER_ALLOC_C"></a>

## 241.58 `CONFIG_MBEDTLS_MEMORY_BUFFER_ALLOC_C`

**提示（Prompt）**：缓冲区内存分配器（Buffer memory allocator）

**说明（Help）**

启用基于缓冲区（原文称“stack based buffer”，栈式缓冲区）的分配器实现，用于“分配”动态内存，替换 `calloc()` 和 `free()` 调用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_MBEDTLS_ENABLE_HEAP
CONFIG_MBEDTLS_ENABLE_HEAP
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:125`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L125)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_ENABLE_HEAP`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_ENABLE_HEAP)。

<a id="CONFIG_MBEDTLS_MEMORY_DEBUG"></a>

## 241.59 `CONFIG_MBEDTLS_MEMORY_DEBUG`

**提示（Prompt）**：启用 Mbed TLS 内存调试（memory debug activation）

**说明（Help）**

启用缓冲区分配器内存问题的调试。自动向标准错误（stderr）打印全部内存分配问题的致命消息，并启用用于输出已分配内存调试信息的函数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_MEMORY_BUFFER_ALLOC_C && CONFIG_MBEDTLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:134`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L134)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → 缓冲区内存分配器（Buffer memory allocator）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_MEMORY_BUFFER_ALLOC_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_MEMORY_BUFFER_ALLOC_C)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_NIST_KW_C"></a>

## 241.60 `CONFIG_MBEDTLS_NIST_KW_C`

**提示（Prompt）**：NIST 密钥封装（key wrap）

**说明（Help）**

NIST SP 800-38F 定义的 128 位分组密码（block ciphers）密钥封装模式（Key Wrapping mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_WANT_KEY_TYPE_AES && CONFIG_MBEDTLS
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:440`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L440)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_PSA_WANT_KEY_TYPE_AES`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_AES)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT)。

<a id="CONFIG_MBEDTLS_OPENTHREAD_OPTIMIZATIONS_ENABLED"></a>

## 241.61 `CONFIG_MBEDTLS_OPENTHREAD_OPTIMIZATIONS_ENABLED`

**提示（Prompt）**：面向 OpenThread 的 MbedTLS 优化（optimizations）

**说明（Help）**

启用 OpenThread 专用的 Mbed TLS 优化，在使用 OpenThread 时节省部分 RAM／ROM。注意：如果应用还需要在 OpenThread 之上使用其他 Mbed TLS 服务，例如安全套接字（secure sockets），建议禁用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD && CONFIG_MBEDTLS
```

**默认值（Defaults）**

```text
y if !CONFIG_NET_SOCKETS_SOCKOPT_TLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:265`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L265)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_NET_SOCKETS_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_SOCKOPT_TLS)。

<a id="CONFIG_MBEDTLS_PEM_PARSE_C"></a>

## 241.62 `CONFIG_MBEDTLS_PEM_PARSE_C`

**提示（Prompt）**：PEM 解码／解析（decoding / parsing）

**说明（Help）**

增加 PEM 文件解码／解析（decoding / parsing）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_BASE64_C
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE
CONFIG_ESP32_WIFI_ENTERPRISE
```

**被弱选择（Implied by）**

```text
CONFIG_QUIC_SOCKOPT_TLS
CONFIG_SSH_CRYPTO
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:222`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L222)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_BASE64_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BASE64_C)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_ESP32_WIFI_ENTERPRISE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_ENTERPRISE)、[`CONFIG_QUIC_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_SOCKOPT_TLS)、[`CONFIG_SSH_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH_CRYPTO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SSH_CRYPTO`。

<a id="CONFIG_MBEDTLS_PEM_WRITE_C"></a>

## 241.63 `CONFIG_MBEDTLS_PEM_WRITE_C`

**提示（Prompt）**：PEM 编码／写入（encoding / writing）

**说明（Help）**

增加 PEM 文件编码／写入（encoding / writing）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_BASE64_C
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE
```

**被弱选择（Implied by）**

```text
CONFIG_SSH_CRYPTO
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:228`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L228)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_BASE64_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BASE64_C)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_SSH_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH_CRYPTO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SSH_CRYPTO`。

<a id="CONFIG_MBEDTLS_PKCS5_C"></a>

## 241.64 `CONFIG_MBEDTLS_PKCS5_C`

**提示（Prompt）**：基于密码的加密函数（Password-based encryption functions）

**说明（Help）**

启用公钥密码标准 5（PKCS5）函数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_MD_C && CONFIG_MBEDTLS
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:294`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L294)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_MD_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_MD_C)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT)、[`CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO)。

<a id="CONFIG_MBEDTLS_PK_PARSE_C"></a>

## 241.65 `CONFIG_MBEDTLS_PK_PARSE_C`

**提示（Prompt）**：通用公钥／非对称密钥解析器（public/asymmetric key parser）

**说明（Help）**

启用通用公钥解析函数（public key parse functions）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**被选择（Selected by）**

```text
CONFIG_MBEDTLS_X509_USE_C
CONFIG_MBEDTLS_X509_USE_C
CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO
```

**被弱选择（Implied by）**

```text
CONFIG_SSH_CRYPTO
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:275`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L275)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_X509_USE_C`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_X509_USE_C)、[`CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO)、[`CONFIG_SSH_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH_CRYPTO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SSH_CRYPTO`。

<a id="CONFIG_MBEDTLS_PK_WRITE_C"></a>

## 241.66 `CONFIG_MBEDTLS_PK_WRITE_C`

**提示（Prompt）**：通用公钥／非对称密钥写入器（public/asymmetric key writer）

**说明（Help）**

启用通用公钥写入函数（public key write functions）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG
CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO
```

**被弱选择（Implied by）**

```text
CONFIG_SSH_CRYPTO
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:280`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L280)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT)、[`CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG)、[`CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO)、[`CONFIG_SSH_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH_CRYPTO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SSH_CRYPTO`。

<a id="CONFIG_MBEDTLS_PLATFORM_NO_STD_FUNCTIONS"></a>

## 241.67 `CONFIG_MBEDTLS_PLATFORM_NO_STD_FUNCTIONS`

**提示（Prompt）**：移除对标准 libc 函数的使用

**说明（Help）**

防止 Mbed TLS 链接 libc 中的以下标准函数：`snprintf`、`vsnprintf`、`printf`、`fprintf`、`calloc`、`free`、`setbuf`、`exit` 和 `time`。默认情况下，Mbed TLS 为这些函数使用桩函数（stub functions）。桩函数仅返回成功，不实现所需功能。用户可以调用 `mbedtls_platform_set_xxx()`，在运行时设置自己的 `xxx()` 实现，分别覆盖各个桩函数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:189`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L189)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_PLATFORM_SNPRINTF_ALT"></a>

## 241.68 `CONFIG_MBEDTLS_PLATFORM_SNPRINTF_ALT`

**提示（Prompt）**：允许运行时设置自定义 snprintf

**说明（Help）**

允许通过 `mbedtls_platform_set_snprintf()` 设置自定义 `snprintf()` 函数。包含 `mbedtls/platform.h` 可获得该函数原型（prototype）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_PLATFORM_NO_STD_FUNCTIONS && CONFIG_MBEDTLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:203`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L203)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → 移除对标准 libc 函数的使用

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_PLATFORM_NO_STD_FUNCTIONS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_PLATFORM_NO_STD_FUNCTIONS)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_PROMPTLESS"></a>

## 241.69 `CONFIG_MBEDTLS_PROMPTLESS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

用于禁用 MBEDTLS 选择提示（prompt）的符号。Kconfig 树内部可使用此符号隐藏 Mbed TLS 菜单提示，改由依赖子配置处理 MBEDTLS 的选择，从而避免配置符号卡住（stuck symbol）的行为。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`modules/mbedtls/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

<a id="CONFIG_MBEDTLS_PSA_ASSUME_EXCLUSIVE_BUFFERS"></a>

## 241.70 `CONFIG_MBEDTLS_PSA_ASSUME_EXCLUSIVE_BUFFERS`

**提示（Prompt）**：假定 PSA Crypto 操作独占缓冲区（exclusive buffers）

**说明（Help）**

假定传给 PSA 函数的所有缓冲区都由该函数独占，且不位于共享内存（shared memory）中。启用后可避免内部缓冲区复制，改善性能。但应用必须确保缓冲区不重叠（overlap）。某些算法和模式还可能有额外约束，例如输入大小必须是分组大小（block size）的整数倍。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_PSA_CRYPTO_C && CONFIG_MBEDTLS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:371`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L371)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_PSA_CRYPTO_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_PSA_CRYPTO_C)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_PSA_CRYPTO_BUILTIN_KEYS"></a>

## 241.71 `CONFIG_MBEDTLS_PSA_CRYPTO_BUILTIN_KEYS`

**提示（Prompt）**：PSA Crypto 核心内建密钥支持（Built-in key support）

**说明（Help）**

在 PSA Crypto 中启用平台内建密钥（built-in keys）支持。这些密钥通常从硬件唯一密钥（hardware unique key）派生，或保存在安全元件（secure element）中。Mbed TLS 使用从 `MBEDTLS_PSA_KEY_ID_BUILTIN_MIN` 到 `MBEDTLS_PSA_KEY_ID_BUILTIN_MAX` 的密钥 ID 表示内建密钥。平台必须实现 `mbedtls_psa_platform_get_builtin_key()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_PSA_CRYPTO_C && CONFIG_MBEDTLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:429`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L429)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_PSA_CRYPTO_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_PSA_CRYPTO_C)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_PSA_CRYPTO_C"></a>

## 241.72 `CONFIG_MBEDTLS_PSA_CRYPTO_C`

**提示（Prompt）**：平台安全架构密码 API（Platform Security Architecture cryptography API）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_BUILD_WITH_TFM && CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_CSPRNG_NEEDED if CONFIG_PSA_CRYPTO_PROVIDER_MBEDTLS
```

**被选择（Selected by）**

```text
CONFIG_PSA_CRYPTO_PROVIDER_MBEDTLS
CONFIG_PSA_CRYPTO_PROVIDER_MBEDTLS
CONFIG_WIFI_BFLB_WIFI4
CONFIG_MCP_TRANSPORT_HTTP
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:355`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L355)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_WITH_TFM)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_CSPRNG_NEEDED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CSPRNG_NEEDED)、[`CONFIG_PSA_CRYPTO_PROVIDER_MBEDTLS`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_PROVIDER_MBEDTLS)、[`CONFIG_WIFI_BFLB_WIFI4`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB_WIFI4)、[`CONFIG_MCP_TRANSPORT_HTTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCP_TRANSPORT_HTTP)。

<a id="CONFIG_MBEDTLS_PSA_CRYPTO_EXTERNAL_RNG"></a>

## 241.73 `CONFIG_MBEDTLS_PSA_CRYPTO_EXTERNAL_RNG`

**提示（Prompt）**：密码学安全驱动（Cryptographically secure driver）

**说明（Help）**

使用密码学安全随机数生成器（cryptographically secure random generator）提供随机数据，替代旧版 Mbed TLS 模块。相比 `MBEDTLS_PSA_CRYPTO_LEGACY_RNG`，此方式占用更小，但要求系统存在密码学安全伪随机数生成器（CSPRNG）。若不存在 CSPRNG：

- 不会回退到使用弱熵的随机数生成器。
- PSA Crypto 初始化将失败，其所有 API 都不可用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MBEDTLS_PSA_CRYPTO_RNG_SOURCE>
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:307`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L307)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → PSA Crypto 随机源（random source）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_PSA_CRYPTO_RNG_SOURCE`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_PSA_CRYPTO_RNG_SOURCE)。

<a id="CONFIG_MBEDTLS_PSA_CRYPTO_EXTERNAL_RNG_ALLOW_NON_CSPRNG"></a>

## 241.74 `CONFIG_MBEDTLS_PSA_CRYPTO_EXTERNAL_RNG_ALLOW_NON_CSPRNG`

**提示（Prompt）**：允许非密码学安全随机源（non-cryptographically secure random sources），仅用于测试

**说明（Help）**

`MBEDTLS_PSA_CRYPTO_EXTERNAL_RNG` 默认仅允许依赖密码学安全随机数生成器。但仅出于测试目的，有时需要启用外部随机数生成（external random number generation），同时使用弱随机源（非密码学安全）。

警告：此选项仅应在测试中启用，不用于生产环境，因为生成的值不具备密码学安全性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_PSA_CRYPTO_EXTERNAL_RNG && CONFIG_MBEDTLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:343`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L343)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_PSA_CRYPTO_EXTERNAL_RNG`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_PSA_CRYPTO_EXTERNAL_RNG)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_PSA_CRYPTO_LEGACY_RNG"></a>

## 241.75 `CONFIG_MBEDTLS_PSA_CRYPTO_LEGACY_RNG`

**提示（Prompt）**：Mbed TLS 旧式模块（legacy modules）：`ENTROPY + [CTR|HMAC]_DRBG`

**说明（Help）**

使用旧式 Mbed TLS 模块（legacy modules）生成随机数据。此配置使用熵模块（entropy module）收集数据，再在其上使用 `ctr_drbg` 或 `hmac_drbg` 改善随机性。

安全级别取决于系统启用的熵源（entropy sources）类型：原文指出，使用弱熵源时，生成的数据仅为伪随机数据，并强烈建议在条件允许时使用强熵源，以获得其所称的“真正随机数据”（real random data）。

此实现与 `MBEDTLS_PSA_CRYPTO_EXTERNAL_RNG` 的另一项区别是内存占用：它引入了“外部”版本不需要的旧式模块，因此占用更大。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MBEDTLS_PSA_CRYPTO_RNG_SOURCE>
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_ENTROPY_C
CONFIG_MBEDTLS_HMAC_DRBG_C if !CONFIG_MBEDTLS_CTR_DRBG_C
CONFIG_TEST_RANDOM_GENERATOR if !CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:319`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L319)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → PSA Crypto 随机源（random source）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_PSA_CRYPTO_RNG_SOURCE`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_PSA_CRYPTO_RNG_SOURCE)、[`CONFIG_MBEDTLS_ENTROPY_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_ENTROPY_C)、[`CONFIG_MBEDTLS_HMAC_DRBG_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_HMAC_DRBG_C)、[`CONFIG_MBEDTLS_CTR_DRBG_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CTR_DRBG_C)、[`CONFIG_TEST_RANDOM_GENERATOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TEST_RANDOM_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_MBEDTLS_PSA_CRYPTO_RNG_SOURCE"></a>

## 241.76 `CONFIG_MBEDTLS_PSA_CRYPTO_RNG_SOURCE`

**提示（Prompt）**：PSA Crypto 随机源（random source）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_PSA_CRYPTO_C && CONFIG_MBEDTLS
```

**默认值（Defaults）**

```text
CONFIG_MBEDTLS_PSA_CRYPTO_EXTERNAL_RNG if (CONFIG_CSPRNG_ENABLED && !CONFIG_ENTROPY_NEEDS_PRNG) || !CONFIG_PSA_CRYPTO_PROVIDER_MBEDTLS
CONFIG_MBEDTLS_PSA_CRYPTO_LEGACY_RNG
```

**可选项（Choices）**

```text
CONFIG_MBEDTLS_PSA_CRYPTO_EXTERNAL_RNG
CONFIG_MBEDTLS_PSA_CRYPTO_LEGACY_RNG
CONFIG_MBEDTLS_PSA_CRYPTO_EXTERNAL_RNG
CONFIG_MBEDTLS_PSA_CRYPTO_LEGACY_RNG
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:300`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L300)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_PSA_CRYPTO_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_PSA_CRYPTO_C)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_PSA_CRYPTO_EXTERNAL_RNG`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_PSA_CRYPTO_EXTERNAL_RNG)、[`CONFIG_CSPRNG_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CSPRNG_ENABLED)、[`CONFIG_ENTROPY_NEEDS_PRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_NEEDS_PRNG)、[`CONFIG_PSA_CRYPTO_PROVIDER_MBEDTLS`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_PROVIDER_MBEDTLS)、[`CONFIG_MBEDTLS_PSA_CRYPTO_LEGACY_RNG`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_PSA_CRYPTO_LEGACY_RNG)。

<a id="CONFIG_MBEDTLS_PSA_DRIVER_GET_ENTROPY"></a>

## 241.77 `CONFIG_MBEDTLS_PSA_DRIVER_GET_ENTROPY`

**提示（Prompt）**：通过熵驱动或随机数生成器向 Mbed TLS 提供熵数据（entropy data）

**说明（Help）**

通过系统中的熵驱动（entropy driver，若可用），或通用随机数生成器（random number generator），向 Mbed TLS 熵模块提供熵数据。

警告：后者可能不安全，因为最终可能使用较弱或仅供测试的源，例如基于系统定时器的随机数生成器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_ENTROPY_C && CONFIG_MBEDTLS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:253`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L253)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 熵累加器（entropy accumulator）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_ENTROPY_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_ENTROPY_C)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_PSA_KEY_SLOT_COUNT"></a>

## 241.78 `CONFIG_MBEDTLS_PSA_KEY_SLOT_COUNT`

**提示（Prompt）**：PSA Crypto 核心密钥槽数量（key slots）

**说明（Help）**

设置 PSA Crypto 核心可用的密钥槽（key slots）数量。注意：每个槽即使未使用，也会增加约 40 字节 RAM 占用，此外还包括：

- 设置 `MBEDTLS_PSA_STATIC_KEY_SLOTS` 时，增加构建中通过 `PSA_WANT` 符号启用的最大非对称／对称密钥类型的长度；这些空间均在构建时静态定义。
- 未设置 `MBEDTLS_PSA_STATIC_KEY_SLOTS` 且槽已使用时，增加从堆中分配、用于保存该槽密钥材料（key material）的内存。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_PSA_CRYPTO_C && CONFIG_MBEDTLS
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:416`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L416)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_PSA_CRYPTO_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_PSA_CRYPTO_C)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_PSA_P256M_DRIVER_ENABLED"></a>

## 241.79 `CONFIG_MBEDTLS_PSA_P256M_DRIVER_ENABLED`

**提示（Prompt）**：P256-M 驱动（driver）

**说明（Help）**

通过标准 PSA API 启用 secp256r1 曲线的优化软件实现（optimized software implementation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_PSA_CRYPTO_C && CONFIG_MBEDTLS
```

**弱选择（Implies）**

```text
CONFIG_PSA_WANT_ALG_SHA_256
```

**被弱选择（Implied by）**

```text
CONFIG_BT_ECC
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:384`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L384)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_PSA_CRYPTO_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_PSA_CRYPTO_C)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_PSA_WANT_ALG_SHA_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_256)、[`CONFIG_BT_ECC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ECC)。

<a id="CONFIG_MBEDTLS_PSA_P256M_DRIVER_RAW"></a>

## 241.80 `CONFIG_MBEDTLS_PSA_P256M_DRIVER_RAW`

**提示（Prompt）**：直接访问 p256-m 驱动，不经过 PSA 接口

**说明（Help）**

允许直接访问 p256-m 驱动接口。

警告：Zephyr 代码库禁止使用此 Kconfig 选项。用户可在内存极其受限的设备上启用，但 p256-m 接口完全不保证随时间保持稳定。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_PSA_P256M_DRIVER_ENABLED && CONFIG_MBEDTLS_PSA_CRYPTO_C && CONFIG_MBEDTLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:391`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L391)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → P256-M 驱动（driver）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_PSA_P256M_DRIVER_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_PSA_P256M_DRIVER_ENABLED)、[`CONFIG_MBEDTLS_PSA_CRYPTO_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_PSA_CRYPTO_C)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_PSA_STATIC_KEY_SLOTS"></a>

## 241.81 `CONFIG_MBEDTLS_PSA_STATIC_KEY_SLOTS`

**提示（Prompt）**：使用静态分配的密钥缓冲区保存密钥材料（key material）

**说明（Help）**

默认情况下，Mbed TLS 的 PSA Crypto 核心使用堆内存保存每个密钥槽（key slot）的密钥材料。这可能引入不希望承担的堆内存及其管理代码需求，同时影响 RAM 和 ROM 占用。启用此符号后，Mbed TLS 在构建时预分配所有保存密钥材料的槽缓冲区，从而不再需要堆内存。每个缓冲区的大小可容纳构建中通过 `PSA_WANT` 符号启用的最大非对称／对称密钥类型。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_PSA_CRYPTO_C && CONFIG_MBEDTLS
```

**默认值（Defaults）**

```text
y if !CONFIG_MBEDTLS_ENABLE_HEAP
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:402`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L402)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_PSA_CRYPTO_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_PSA_CRYPTO_C)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_ENABLE_HEAP`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_ENABLE_HEAP)。

<a id="CONFIG_MBEDTLS_PSK_MAX_LEN"></a>

## 241.82 `CONFIG_MBEDTLS_PSK_MAX_LEN`

**提示（Prompt）**：TLS 预共享密钥（pre-shared keys）的最大大小

**说明（Help）**

TLS 预共享密钥（PSK）的最大大小，单位为字节。不使用 PSK 密钥交换（key exchange）时无效。TLS 1.3 会话票据（session tickets）派生的恢复 PSK 长度与协商密码套件的散列长度相同。恢复握手（resumption handshake）加载 PSK 时，Mbed TLS 会执行此限制。因此，启用会话票据和基于 SHA-384 的密码套件时，默认值需要提高到 `48`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**默认值（Defaults）**

```text
48 if CONFIG_MBEDTLS_SSL_SESSION_TICKETS && CONFIG_PSA_WANT_ALG_SHA_384
32
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:170`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L170)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration） → 密码套件配置（Ciphersuite configuration）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_SSL_SESSION_TICKETS`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_SSL_SESSION_TICKETS)、[`CONFIG_PSA_WANT_ALG_SHA_384`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_384)。

<a id="CONFIG_MBEDTLS_SHA256_SMALLER"></a>

## 241.83 `CONFIG_MBEDTLS_SHA256_SMALLER`

**提示（Prompt）**：更小的 SHA-256 实现（Smaller implementation）

**说明（Help）**

启用 ROM 占用更小但性能也更低的 SHA-256 实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_WANT_ALG_SHA_256 && CONFIG_MBEDTLS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_PSA_WANT_ALG_SHA_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_256)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_SHELL"></a>

## 241.84 `CONFIG_MBEDTLS_SHELL`

**提示（Prompt）**：Mbed TLS 命令行（shell）

**说明（Help）**

启用 Mbed TLS 命令行模块（shell module），可显示该库的调试信息，例如堆使用情况（heap usage）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_MBEDTLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig:168`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig#L168)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_SSL_ALPN"></a>

## 241.85 `CONFIG_MBEDTLS_SSL_ALPN`

**提示（Prompt）**：支持设置所支持的应用层协议（Application Layer Protocols）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_MBEDTLS_SSL_PROTO_TLS1_2 || CONFIG_MBEDTLS_SSL_PROTO_TLS1_3) && CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:122`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L122)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration） → 传输层安全（TLS）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_2`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_2)、[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_3`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_3)、[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_SSL_CACHE_C"></a>

## 241.86 `CONFIG_MBEDTLS_SSL_CACHE_C`

**提示（Prompt）**：SSL 会话缓存支持（session cache support）

**说明（Help）**

启用简单的服务器侧 SSL 缓存实现（cache implementation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:240`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L240)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_SSL_CACHE_DEFAULT_MAX_ENTRIES"></a>

## 241.87 `CONFIG_MBEDTLS_SSL_CACHE_DEFAULT_MAX_ENTRIES`

**提示（Prompt）**：SSL 缓存条目（cache entries）的最大数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_SSL_CACHE_C && CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:251`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L251)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration） → SSL 会话缓存支持（session cache support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_SSL_CACHE_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_CACHE_C)、[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_SSL_CACHE_DEFAULT_TIMEOUT"></a>

## 241.88 `CONFIG_MBEDTLS_SSL_CACHE_DEFAULT_TIMEOUT`

**提示（Prompt）**：SSL 缓存条目的默认超时（default timeout）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_SSL_CACHE_C && CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**默认值（Defaults）**

```text
86400
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:247`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L247)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration） → SSL 会话缓存支持（session cache support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_SSL_CACHE_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_CACHE_C)、[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_SSL_DTLS_CONNECTION_ID"></a>

## 241.89 `CONFIG_MBEDTLS_SSL_DTLS_CONNECTION_ID`

原库同名定义共 2 条；本项为数据库第 10821 条记录，各定义分别保留。

**提示（Prompt）**：DTLS 连接标识符扩展（Connection ID extension）

**说明（Help）**

启用 DTLS 连接标识符扩展（Connection ID extension）支持，使底层传输发生变化后仍能识别同一 DTLS 连接。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_SSL_PROTO_DTLS && CONFIG_MBEDTLS_SSL_PROTO_TLS1_2 && CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration） → 传输层安全（TLS） → TLS 1.2／DTLS 1.2 支持 → 数据报传输层安全（DTLS）支持

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_SSL_PROTO_DTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_PROTO_DTLS)、[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_2`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_2)、[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_SSL_DTLS_CONNECTION_ID--record-10822"></a>

## 241.90 `CONFIG_MBEDTLS_SSL_DTLS_CONNECTION_ID`

原库同名定义共 2 条；本项为数据库第 10822 条记录，各定义分别保留。

**提示（Prompt）**：DTLS 连接标识符扩展（Connection ID extension）

**说明（Help）**

启用 DTLS 连接标识符扩展（Connection ID extension）支持，使底层传输发生变化后仍能识别同一 DTLS 连接。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_SSL_PROTO_DTLS && CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:271`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L271)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_SSL_PROTO_DTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_PROTO_DTLS)、[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_SSL_EARLY_DATA"></a>

## 241.91 `CONFIG_MBEDTLS_SSL_EARLY_DATA`

**提示（Prompt）**：TLS 1.3 早期数据（early data，0-RTT）支持

**说明（Help）**

启用 TLS 1.3 早期数据（early data，0-RTT）支持，在握手完成前发送应用数据以降低延迟。此功能需要会话票据（session tickets），且早期数据仅用于预共享密钥（PSK）交换模式。如果需要关注 0-RTT 重放防护（replay protection），应禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_SSL_SESSION_TICKETS && CONFIG_MBEDTLS_SSL_PROTO_TLS1_3 && CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration） → 传输层安全（TLS） → TLS 1.3 支持 → 在 TLS 1.3 中支持 RFC 5077 会话票据（session tickets）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_SSL_SESSION_TICKETS`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_SSL_SESSION_TICKETS)、[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_3`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_3)、[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_SSL_ENCRYPT_THEN_MAC"></a>

## 241.92 `CONFIG_MBEDTLS_SSL_ENCRYPT_THEN_MAC`

**提示（Prompt）**：先加密后认证扩展（Encrypt-then-MAC，RFC 7366）

**说明（Help）**

为 TLS 1.2 启用先加密后认证扩展（Encrypt-then-MAC，RFC 7366）。此扩展将 CBC 密码套件默认的先认证后加密（MAC-then-encrypt）改为先加密后认证，从而更好地抵御填充预言机攻击（padding oracle attacks）。仅在必须与不符合规范的对端互操作时禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_SSL_PROTO_TLS1_2 && CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration） → 传输层安全（TLS）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_2`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_2)、[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_SSL_EXTENDED_MASTER_SECRET"></a>

## 241.93 `CONFIG_MBEDTLS_SSL_EXTENDED_MASTER_SECRET`

**提示（Prompt）**：（D）TLS 扩展主密钥扩展（Extended Master Secret extension）

**说明（Help）**

启用（D）TLS 扩展主密钥（Extended Master Secret）扩展，确保每个连接和每个会话的主密钥（master secrets）均不同。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_SSL_PROTO_TLS1_2 && CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE
CONFIG_ESP32_WIFI_ENTERPRISE
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:257`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L257)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_2`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_2)、[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_ESP32_WIFI_ENTERPRISE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_ENTERPRISE)。

<a id="CONFIG_MBEDTLS_SSL_IN_CONTENT_LEN"></a>

## 241.94 `CONFIG_MBEDTLS_SSL_IN_CONTENT_LEN`

**提示（Prompt）**：传入 TLS 消息的最大载荷大小（incoming payload size）

**说明（Help）**

传入 TLS 载荷（payload）的最大大小。独立设置此值可使用不对称缓冲区大小。例如，设备主要发送小请求但接收大响应，如 OTA 固件或服务器证书，可以保留较大的输入缓冲区和较小的输出缓冲区以节省堆内存。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**默认值（Defaults）**

```text
CONFIG_MBEDTLS_SSL_MAX_CONTENT_LEN if CONFIG_MBEDTLS_SSL_MAX_CONTENT_LEN > 0
1500
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L127)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration） → 传输层安全（TLS）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_SSL_MAX_CONTENT_LEN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_MAX_CONTENT_LEN)。

<a id="CONFIG_MBEDTLS_SSL_KEYING_MATERIAL_EXPORT"></a>

## 241.95 `CONFIG_MBEDTLS_SSL_KEYING_MATERIAL_EXPORT`

**提示（Prompt）**：TLS 密钥材料导出支持（keying material export support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE
CONFIG_ESP32_WIFI_ENTERPRISE
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:221`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L221)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration） → 密码套件配置（Ciphersuite configuration）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_ESP32_WIFI_ENTERPRISE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_ENTERPRISE)。

<a id="CONFIG_MBEDTLS_SSL_MAX_CONTENT_LEN"></a>

## 241.96 `CONFIG_MBEDTLS_SSL_MAX_CONTENT_LEN`

**提示（Prompt）**：TLS 协议消息的最大载荷大小（payload size）［已弃用，DEPRECATED］

**说明（Help）**

已弃用。请使用 `MBEDTLS_SSL_IN_CONTENT_LEN` 和 `MBEDTLS_SSL_OUT_CONTENT_LEN`，分别控制传入和传出 TLS 缓冲区大小。TLS 标准规定最大载荷（payload）为 16384 字节；为获得最大的互操作性并适用于通用场景，必须使用该值。特定用途可大幅降低。例如，DTLS 载荷受 UDP 数据报大小限制；即使是 HTTPS REST API，载荷也可限定为 REST 请求、REST 响应和服务器证书中最大项的大小。Mbed TLS 对输入和输出缓冲区分别使用此值，因此会分配两倍大小的空间，位于 Mbed TLS 自有堆中，`MBEDTLS_HEAP_SIZE` 必须能容纳这些空间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.deprecated:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.deprecated#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_SSL_MAX_FRAGMENT_LENGTH"></a>

## 241.97 `CONFIG_MBEDTLS_SSL_MAX_FRAGMENT_LENGTH`

**提示（Prompt）**：最大分片长度扩展支持（Maximum Fragment Length，MFL；RFC 6066）

**说明（Help）**

启用最大分片长度（MFL）协商支持，符合 RFC 6066，可请求小于已配置缓冲区大小的分片。Mbed TLS 在 TLS 1.3 模式下不支持此扩展。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MBEDTLS_SSL_PROTO_TLS1_3 && CONFIG_MBEDTLS_SSL_PROTO_TLS1_2 && CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration） → 传输层安全（TLS）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_3`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_3)、[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_2`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_2)、[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_SSL_OUT_CONTENT_LEN"></a>

## 241.98 `CONFIG_MBEDTLS_SSL_OUT_CONTENT_LEN`

**提示（Prompt）**：传出 TLS 消息的最大载荷大小（outgoing payload size）

**说明（Help）**

传出 TLS 载荷（payload）的最大大小。独立设置此值可使用不对称缓冲区大小。对于发送小请求的受限设备，此值可以远小于输入缓冲区大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**默认值（Defaults）**

```text
CONFIG_MBEDTLS_SSL_MAX_CONTENT_LEN if CONFIG_MBEDTLS_SSL_MAX_CONTENT_LEN > 0
1500
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:138`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L138)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration） → 传输层安全（TLS）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_SSL_MAX_CONTENT_LEN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_MAX_CONTENT_LEN)。

<a id="CONFIG_MBEDTLS_SSL_PROTO_DTLS"></a>

## 241.99 `CONFIG_MBEDTLS_SSL_PROTO_DTLS`

**提示（Prompt）**：数据报传输层安全（DTLS）支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_SSL_PROTO_TLS1_2 && CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**被选择（Selected by）**

```text
CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG
CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG
CONFIG_NET_SOCKETS_ENABLE_DTLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration） → 传输层安全（TLS） → TLS 1.2／DTLS 1.2 支持

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_2`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_2)、[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG)、[`CONFIG_NET_SOCKETS_ENABLE_DTLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_ENABLE_DTLS)。

<a id="CONFIG_MBEDTLS_SSL_PROTO_TLS1_2"></a>

## 241.100 `CONFIG_MBEDTLS_SSL_PROTO_TLS1_2`

**提示（Prompt）**：TLS 1.2／DTLS 1.2 支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_CIPHER
CONFIG_MBEDTLS_MD_C
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG
CONFIG_NET_SOCKETS_ENABLE_DTLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration） → 传输层安全（TLS）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_CIPHER`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHER)、[`CONFIG_MBEDTLS_MD_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_MD_C)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256)、[`CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG)、[`CONFIG_NET_SOCKETS_ENABLE_DTLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_ENABLE_DTLS)。

<!-- kconfig-navigation -->

[上一章](P240_modules_lvgl_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P242_modules_mbedtls_配置项参考_2.md)
