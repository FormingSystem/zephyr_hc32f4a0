---
id: learning.zephyr-docs.kconfig-reference.page-242
title: "`modules/mbedtls`配置项参考（2/3）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第242章\_`modules/mbedtls`配置项参考（2/3）

本章翻译官方 Kconfig 数据库中 `modules/mbedtls` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_MBEDTLS_SSL_PROTO_TLS1_3"></a>

## 242.1 `CONFIG_MBEDTLS_SSL_PROTO_TLS1_3`

**提示（Prompt）**：TLS 1.3 支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_PSA_WANT_ALG_HKDF_EXTRACT
CONFIG_PSA_WANT_ALG_HKDF_EXPAND
```

**被选择（Selected by）**

```text
CONFIG_EAP_TLSV1_3
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256
CONFIG_EAP_TLSV1_3
CONFIG_EAP_TLSV1_3
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration） → 传输层安全（TLS）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_PSA_WANT_ALG_HKDF_EXTRACT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_HKDF_EXTRACT)、[`CONFIG_PSA_WANT_ALG_HKDF_EXPAND`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_HKDF_EXPAND)、[`CONFIG_EAP_TLSV1_3`](P235_modules_hostap_配置项参考.md#CONFIG_EAP_TLSV1_3)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256)。

<a id="CONFIG_MBEDTLS_SSL_SERVER_NAME_INDICATION"></a>

## 242.2 `CONFIG_MBEDTLS_SSL_SERVER_NAME_INDICATION`

**提示（Prompt）**：SSL 中的 RFC 6066 服务器名称指示（SNI）支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_X509_CRT_PARSE_C && CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE
CONFIG_ESP32_WIFI_ENTERPRISE
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:229`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L229)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_X509_CRT_PARSE_C`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_X509_CRT_PARSE_C)、[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_ESP32_WIFI_ENTERPRISE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_ENTERPRISE)。

<a id="CONFIG_MBEDTLS_SSL_SESSION_TICKETS"></a>

## 242.3 `CONFIG_MBEDTLS_SSL_SESSION_TICKETS`

**提示（Prompt）**：在 TLS 1.3 中支持 RFC 5077 会话票据（session tickets）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_SSL_PROTO_TLS1_3 && CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**被选择（Selected by）**

```text
CONFIG_EAP_TLSV1_3
CONFIG_EAP_TLSV1_3
CONFIG_EAP_TLSV1_3
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration） → 传输层安全（TLS） → TLS 1.3 支持

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_3`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_3)、[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_EAP_TLSV1_3`](P235_modules_hostap_配置项参考.md#CONFIG_EAP_TLSV1_3)。

<a id="CONFIG_MBEDTLS_SSL_TLS1_3_COMPATIBILITY_MODE"></a>

## 242.4 `CONFIG_MBEDTLS_SSL_TLS1_3_COMPATIBILITY_MODE`

**提示（Prompt）**：TLS 1.3 中间设备兼容模式（middlebox compatibility mode）

**说明（Help）**

启用 RFC 8446 附录 D.4 定义的 TLS 1.3 中间设备兼容模式（middlebox compatibility mode）。与某些网络中间设备互操作时需要此功能。如果网络路径已知，可禁用以节省少量代码和带宽。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_SSL_PROTO_TLS1_3 && CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration） → 传输层安全（TLS） → TLS 1.3 支持

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_3`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_3)、[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED"></a>

## 242.5 `CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED`

**提示（Prompt）**：TLS 1.3 临时密钥交换模式（ephemeral key exchange mode）

**说明（Help）**

默认情况下，此 Kconfig 选项弱选择（imply）使用 secp256r1 椭圆曲线的椭圆曲线 Diffie-Hellman（ECDH）算法。也可使用其他椭圆曲线或有限域 Diffie-Hellman（FFDH）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_SSL_PROTO_TLS1_3 && CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_X509_CRT_PARSE_C
```

**被选择（Selected by）**

```text
CONFIG_EAP_TLSV1_3
CONFIG_EAP_TLSV1_3
CONFIG_EAP_TLSV1_3
```

**弱选择（Implies）**

```text
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE
CONFIG_PSA_WANT_ALG_ECDH
CONFIG_PSA_WANT_ECC_SECP_R1_256
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:204`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L204)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration） → 密码套件配置（Ciphersuite configuration）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_3`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_3)、[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_X509_CRT_PARSE_C`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_X509_CRT_PARSE_C)、[`CONFIG_EAP_TLSV1_3`](P235_modules_hostap_配置项参考.md#CONFIG_EAP_TLSV1_3)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE)、[`CONFIG_PSA_WANT_ALG_ECDH`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECDH)、[`CONFIG_PSA_WANT_ECC_SECP_R1_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ECC_SECP_R1_256)。

<a id="CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_PSK_ENABLED"></a>

## 242.6 `CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_PSK_ENABLED`

**提示（Prompt）**：TLS 1.3 预共享密钥交换模式（PSK key exchange mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_SSL_PROTO_TLS1_3 && CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**被选择（Selected by）**

```text
CONFIG_EAP_TLSV1_3
CONFIG_EAP_TLSV1_3
CONFIG_EAP_TLSV1_3
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:201`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L201)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration） → 密码套件配置（Ciphersuite configuration）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_3`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_3)、[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_EAP_TLSV1_3`](P235_modules_hostap_配置项参考.md#CONFIG_EAP_TLSV1_3)。

<a id="CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_PSK_EPHEMERAL_ENABLED"></a>

## 242.7 `CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_PSK_EPHEMERAL_ENABLED`

**提示（Prompt）**：TLS 1.3 预共享密钥临时密钥交换模式（PSK ephemeral key exchange mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_SSL_PROTO_TLS1_3 && CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**被选择（Selected by）**

```text
CONFIG_EAP_TLSV1_3
CONFIG_EAP_TLSV1_3
CONFIG_EAP_TLSV1_3
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:216`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L216)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration） → 密码套件配置（Ciphersuite configuration）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_3`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_3)、[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_EAP_TLSV1_3`](P235_modules_hostap_配置项参考.md#CONFIG_EAP_TLSV1_3)。

<a id="CONFIG_MBEDTLS_SSL_VARIABLE_BUFFER_LENGTH"></a>

## 242.8 `CONFIG_MBEDTLS_SSL_VARIABLE_BUFFER_LENGTH`

**提示（Prompt）**：握手后自动调整缓冲区大小（post-handshake buffer resize）

**说明（Help）**

启用后，根据各方向协商出的最大分片长度（maximum fragment length），自动调整 SSL 缓冲区大小。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_SSL_MAX_FRAGMENT_LENGTH && CONFIG_MBEDTLS_SSL_PROTO_TLS1_2 && CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration） → 传输层安全（TLS） → 最大分片长度扩展支持（Maximum Fragment Length，MFL；RFC 6066）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_SSL_MAX_FRAGMENT_LENGTH`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_MAX_FRAGMENT_LENGTH)、[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_2`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_2)、[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_USER_CONFIG_ENABLE"></a>

## 242.9 `CONFIG_MBEDTLS_USER_CONFIG_ENABLE`

**提示（Prompt）**：用户 Mbed TLS 配置文件（config file）［已弃用，DEPRECATED］

**说明（Help）**

此 Kconfig 选项已弃用，请改为直接定义 `MBEDTLS_USER_CONFIG_FILE`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.deprecated:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.deprecated#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_MBEDTLS_USER_CONFIG_FILE"></a>

## 242.10 `CONFIG_MBEDTLS_USER_CONFIG_FILE`

**提示（Prompt）**：Mbed TLS 用户配置文件（User configuration file）

**说明（Help）**

若定义此项，其指定的头文件会在 `MBEDTLS_CONFIG_FILE` 之后包含。这样可以修改默认配置，包括取消已启用选项的定义（undefine）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_VERSION_4_x"></a>

## 242.11 `CONFIG_MBEDTLS_VERSION_4_x`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

内部使用的隐藏 Kconfig 符号，用于标记支持 Mbed TLS 4.x。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

<a id="CONFIG_MBEDTLS_VERSION_C"></a>

## 242.12 `CONFIG_MBEDTLS_VERSION_C`

**提示（Prompt）**：版本信息支持（version information support）

**说明（Help）**

启用 `mbedtls_version_get_number()` 函数，以获取 Mbed TLS 版本信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:265`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L265)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_X509_CRL_PARSE_C"></a>

## 242.13 `CONFIG_MBEDTLS_X509_CRL_PARSE_C`

**提示（Prompt）**：X.509 证书吊销列表解析（CRL parsing）

**说明（Help）**

供 X.509 证书吊销列表解析（CRL parsing）使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_X509_USE_C
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
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:279`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L279)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_X509_USE_C`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_X509_USE_C)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_ESP32_WIFI_ENTERPRISE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_ENTERPRISE)、[`CONFIG_QUIC_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_SOCKOPT_TLS)。

<a id="CONFIG_MBEDTLS_X509_CRT_PARSE_C"></a>

## 242.14 `CONFIG_MBEDTLS_X509_CRT_PARSE_C`

**提示（Prompt）**：X.509 证书解析（certificate parsing）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_X509_USE_C
```

**被选择（Selected by）**

```text
CONFIG_EAP_TLSV1_3
CONFIG_MBEDTLS_KEY_EXCHANGE_ALL_ENABLED
CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG
CONFIG_EAP_TLSV1_3
CONFIG_EAP_TLSV1_3
CONFIG_MBEDTLS_KEY_EXCHANGE_ALL_ENABLED
CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG
CONFIG_ESP32_WIFI_ENTERPRISE
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:299`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L299)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_X509_USE_C`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_X509_USE_C)、[`CONFIG_EAP_TLSV1_3`](P235_modules_hostap_配置项参考.md#CONFIG_EAP_TLSV1_3)、[`CONFIG_MBEDTLS_KEY_EXCHANGE_ALL_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_KEY_EXCHANGE_ALL_ENABLED)、[`CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256)、[`CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG)、[`CONFIG_ESP32_WIFI_ENTERPRISE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_ENTERPRISE)。

<a id="CONFIG_MBEDTLS_X509_CRT_WRITE_C"></a>

## 242.15 `CONFIG_MBEDTLS_X509_CRT_WRITE_C`

**提示（Prompt）**：X.509 证书创建（certificate creation）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:296`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L296)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_MBEDTLS_X509_CSR_PARSE_C"></a>

## 242.16 `CONFIG_MBEDTLS_X509_CSR_PARSE_C`

**提示（Prompt）**：X.509 证书签名请求解析（Certificate Signing Request parsing）

**说明（Help）**

用于读取 X.509 证书请求（certificate request）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_X509_USE_C
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP
CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP
CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:290`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L290)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_X509_USE_C`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_X509_USE_C)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP)。

<a id="CONFIG_MBEDTLS_X509_CSR_WRITE_C"></a>

## 242.17 `CONFIG_MBEDTLS_X509_CSR_WRITE_C`

**提示（Prompt）**：X.509 证书签名请求写入（Certificate Signing Requests writing）

**说明（Help）**

用于写入 X.509 证书请求（certificate request）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP
CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP
CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:285`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L285)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP)。

<a id="CONFIG_MBEDTLS_X509_RSASSA_PSS_SUPPORT"></a>

## 242.18 `CONFIG_MBEDTLS_X509_RSASSA_PSS_SUPPORT`

**提示（Prompt）**：X.509 RSA-PSS 签名支持（signature support）

**说明（Help）**

启用对使用 RSASSA-PSS 算法签名的 X.509 证书的验证。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_BUILTIN && CONFIG_MBEDTLS
```

**被选择（Selected by）**

```text
CONFIG_EAP_TLSV1_3
CONFIG_EAP_TLSV1_3
CONFIG_EAP_TLSV1_3
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.mbedtls:303`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.mbedtls#L303)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → Mbed TLS 配置（configuration）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_BUILTIN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_BUILTIN)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_EAP_TLSV1_3`](P235_modules_hostap_配置项参考.md#CONFIG_EAP_TLSV1_3)。

<a id="CONFIG_MBEDTLS_X509_USE_C"></a>

## 242.19 `CONFIG_MBEDTLS_X509_USE_C`

**提示（Prompt）**：用于证书处理的 X.509 核心（core）

**说明（Help）**

启用处理证书所需的 X.509 核心（core）。X.509 解析模块（CRT、CRL 和 CSR）需要此功能，启用任一模块时都会自动选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_PK_PARSE_C
CONFIG_MBEDTLS_ASN1_PARSE_C
```

**被选择（Selected by）**

```text
CONFIG_MBEDTLS_X509_CRL_PARSE_C
CONFIG_MBEDTLS_X509_CSR_PARSE_C
CONFIG_MBEDTLS_X509_CRT_PARSE_C
CONFIG_MBEDTLS_X509_CRL_PARSE_C
CONFIG_MBEDTLS_X509_CSR_PARSE_C
CONFIG_MBEDTLS_X509_CRT_PARSE_C
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:285`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L285)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_PK_PARSE_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_PK_PARSE_C)、[`CONFIG_MBEDTLS_ASN1_PARSE_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_ASN1_PARSE_C)、[`CONFIG_MBEDTLS_X509_CRL_PARSE_C`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_X509_CRL_PARSE_C)、[`CONFIG_MBEDTLS_X509_CSR_PARSE_C`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_X509_CSR_PARSE_C)、[`CONFIG_MBEDTLS_X509_CRT_PARSE_C`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_X509_CRT_PARSE_C)。

<a id="CONFIG_MBEDTLS_ZEROIZE_ALT"></a>

## 242.20 `CONFIG_MBEDTLS_ZEROIZE_ALT`

**提示（Prompt）**：Mbed TLS 的 mbedtls_platform_zeroize 替代实现（alternate implementation）

**说明（Help）**

Mbed TLS 配置提供 `mbedtls_platform_zeroize` 的替代实现（alternate implementation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:211`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L211)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_PSA_CRYPTO"></a>

## 242.21 `CONFIG_PSA_CRYPTO`

**提示（Prompt）**：平台安全架构密码 API（PSA Crypto API）

**说明（Help）**

在构建中启用 PSA Crypto API 提供者（provider）。若启用 Trusted Firmware-M（TF-M），则由 TF-M 提供；否则由 Mbed TLS 提供。可选择 `PSA_CRYPTO_PROVIDER_CUSTOM` 使用源码树外实现（out-of-tree implementation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_OPENTHREAD_CRYPTO_PSA
CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_OPENTHREAD_CRYPTO_PSA
CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON
CONFIG_ESP32_BT_LE_CRYPTO_STACK_MBEDTLS
CONFIG_BT_SILABS_EFR32
CONFIG_CRYPTO_MBEDTLS_SHIM
CONFIG_IEEE802154_SILABS_EFR32
CONFIG_WIFI_ESP32
CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO
CONFIG_FIDO2
CONFIG_BT_MESH_CRYPTO_LIB
CONFIG_BT_HOST_CRYPTO
CONFIG_BT_ECC
CONFIG_BT_CRYPTO
CONFIG_JWT_SIGN_RSA_PSA
CONFIG_JWT_SIGN_ECDSA_PSA
CONFIG_LORAWAN_NATIVE
CONFIG_MCUMGR_GRP_FS_HASH_SHA256
CONFIG_UPDATEHUB
CONFIG_NET_IPV6_IID_STABLE
CONFIG_NET_IPV6_PE
CONFIG_MCP_TRANSPORT_HTTP
CONFIG_WEBSOCKET_CLIENT
CONFIG_NET_SOCKETS_SOCKOPT_TLS
CONFIG_TLS_CREDENTIALS_BACKEND_PROTECTED_STORAGE
CONFIG_WIREGUARD_CRYPTO
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD
CONFIG_SETTINGS_TFM_PSA
CONFIG_FLASH_AREA_CHECK_INTEGRITY
```

**被弱选择（Implied by）**

```text
CONFIG_QUIC_SOCKOPT_TLS
CONFIG_SSH_CRYPTO
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.logic:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.logic#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA)、[`CONFIG_OPENTHREAD_CRYPTO_PSA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_CRYPTO_PSA)、[`CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON)、[`CONFIG_ESP32_BT_LE_CRYPTO_STACK_MBEDTLS`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_CRYPTO_STACK_MBEDTLS)、[`CONFIG_BT_SILABS_EFR32`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32)、[`CONFIG_CRYPTO_MBEDTLS_SHIM`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_MBEDTLS_SHIM)、[`CONFIG_IEEE802154_SILABS_EFR32`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_SILABS_EFR32)、[`CONFIG_WIFI_ESP32`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32)、[`CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO)、[`CONFIG_FIDO2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2)、[`CONFIG_BT_MESH_CRYPTO_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_CRYPTO_LIB)、[`CONFIG_BT_HOST_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HOST_CRYPTO)、[`CONFIG_BT_ECC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ECC)、[`CONFIG_BT_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CRYPTO)、[`CONFIG_JWT_SIGN_RSA_PSA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_JWT_SIGN_RSA_PSA)、[`CONFIG_JWT_SIGN_ECDSA_PSA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_JWT_SIGN_ECDSA_PSA)、[`CONFIG_LORAWAN_NATIVE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_NATIVE)、[`CONFIG_MCUMGR_GRP_FS_HASH_SHA256`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_GRP_FS_HASH_SHA256)、[`CONFIG_UPDATEHUB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UPDATEHUB)、[`CONFIG_NET_IPV6_IID_STABLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_IID_STABLE)、[`CONFIG_NET_IPV6_PE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_PE)、[`CONFIG_MCP_TRANSPORT_HTTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCP_TRANSPORT_HTTP)、[`CONFIG_WEBSOCKET_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WEBSOCKET_CLIENT)、[`CONFIG_NET_SOCKETS_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_SOCKOPT_TLS)、[`CONFIG_TLS_CREDENTIALS_BACKEND_PROTECTED_STORAGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TLS_CREDENTIALS_BACKEND_PROTECTED_STORAGE)、[`CONFIG_WIREGUARD_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIREGUARD_CRYPTO)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD)、[`CONFIG_SETTINGS_TFM_PSA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SETTINGS_TFM_PSA)、[`CONFIG_FLASH_AREA_CHECK_INTEGRITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_AREA_CHECK_INTEGRITY)、[`CONFIG_QUIC_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_SOCKOPT_TLS)、[`CONFIG_SSH_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH_CRYPTO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON`、`CONFIG_SSH_CRYPTO`。

<a id="CONFIG_PSA_CRYPTO_ENABLE_ALL"></a>

## 242.22 `CONFIG_PSA_CRYPTO_ENABLE_ALL`

**提示（Prompt）**：全部 PSA 密码功能（crypto features）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)。

<a id="CONFIG_PSA_CRYPTO_PROVIDER"></a>

## 242.23 `CONFIG_PSA_CRYPTO_PROVIDER`

**提示（Prompt）**：PSA Crypto API 提供者（provider）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**可选项（Choices）**

```text
CONFIG_PSA_CRYPTO_PROVIDER_TFM
CONFIG_PSA_CRYPTO_PROVIDER_MBEDTLS
CONFIG_PSA_CRYPTO_PROVIDER_CUSTOM
CONFIG_PSA_CRYPTO_PROVIDER_TFM
CONFIG_PSA_CRYPTO_PROVIDER_MBEDTLS
CONFIG_PSA_CRYPTO_PROVIDER_CUSTOM
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.logic:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.logic#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → 平台安全架构密码 API（PSA Crypto API）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_PROVIDER_TFM`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_PROVIDER_TFM)、[`CONFIG_PSA_CRYPTO_PROVIDER_MBEDTLS`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_PROVIDER_MBEDTLS)、[`CONFIG_PSA_CRYPTO_PROVIDER_CUSTOM`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_PROVIDER_CUSTOM)。

<a id="CONFIG_PSA_CRYPTO_PROVIDER_CUSTOM"></a>

## 242.24 `CONFIG_PSA_CRYPTO_PROVIDER_CUSTOM`

**提示（Prompt）**：使用源码树外库（out-of-tree library）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_BUILD_WITH_TFM && <choice CONFIG_PSA_CRYPTO_PROVIDER>
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.logic:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.logic#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → 平台安全架构密码 API（PSA Crypto API） → PSA Crypto API 提供者（provider）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_WITH_TFM)、[`CONFIG_PSA_CRYPTO_PROVIDER`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_PROVIDER)。

<a id="CONFIG_PSA_CRYPTO_PROVIDER_MBEDTLS"></a>

## 242.25 `CONFIG_PSA_CRYPTO_PROVIDER_MBEDTLS`

**提示（Prompt）**：使用 Mbed TLS

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_BUILD_WITH_TFM && <choice CONFIG_PSA_CRYPTO_PROVIDER>
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS
CONFIG_MBEDTLS_PSA_CRYPTO_C
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.logic:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.logic#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → 平台安全架构密码 API（PSA Crypto API） → PSA Crypto API 提供者（provider）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_WITH_TFM)、[`CONFIG_PSA_CRYPTO_PROVIDER`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_PROVIDER)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_PSA_CRYPTO_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_PSA_CRYPTO_C)。

<a id="CONFIG_PSA_CRYPTO_PROVIDER_TFM"></a>

## 242.26 `CONFIG_PSA_CRYPTO_PROVIDER_TFM`

**提示（Prompt）**：使用 Trusted Firmware-M（TF-M）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM && <choice CONFIG_PSA_CRYPTO_PROVIDER>
```

**主动选择（Selects）**

```text
CONFIG_TFM_PARTITION_CRYPTO
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.logic:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.logic#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → 平台安全架构密码 API（PSA Crypto API） → PSA Crypto API 提供者（provider）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_WITH_TFM)、[`CONFIG_PSA_CRYPTO_PROVIDER`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_PROVIDER)、[`CONFIG_TFM_PARTITION_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TFM_PARTITION_CRYPTO)。

<a id="CONFIG_PSA_WANT_ALG_CBC_NO_PADDING"></a>

## 242.27 `CONFIG_PSA_WANT_ALG_CBC_NO_PADDING`

**提示（Prompt）**：无填充的密码分组链接模式（CBC no padding）：`PSA_WANT_ALG_CBC_NO_PADDING`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_MBEDTLS_CIPHER_ALL_ENABLED
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHER_ALL_ENABLED
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384
CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO
CONFIG_FIDO2
```

**被弱选择（Implied by）**

```text
CONFIG_CRYPTO_MBEDTLS_SHIM
CONFIG_QUIC_SOCKOPT_TLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_MBEDTLS_CIPHER_ALL_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHER_ALL_ENABLED)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384)、[`CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO)、[`CONFIG_FIDO2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2)、[`CONFIG_CRYPTO_MBEDTLS_SHIM`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_MBEDTLS_SHIM)、[`CONFIG_QUIC_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_SOCKOPT_TLS)。

<a id="CONFIG_PSA_WANT_ALG_CBC_PKCS7"></a>

## 242.28 `CONFIG_PSA_WANT_ALG_CBC_PKCS7`

**提示（Prompt）**：采用 PKCS#7 填充的密码分组链接模式（CBC PKCS7）：`PSA_WANT_ALG_CBC_PKCS7`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_MBEDTLS_CIPHER_ALL_ENABLED
CONFIG_MBEDTLS_CIPHER_ALL_ENABLED
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_MBEDTLS_CIPHER_ALL_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHER_ALL_ENABLED)。

<a id="CONFIG_PSA_WANT_ALG_CCM"></a>

## 242.29 `CONFIG_PSA_WANT_ALG_CCM`

**提示（Prompt）**：带 CBC-MAC 的计数器模式（CCM）：`PSA_WANT_ALG_CCM`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_MBEDTLS_CIPHER_ALL_ENABLED
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_MBEDTLS_CIPHER_ALL_ENABLED
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON
CONFIG_WIFI_BFLB_WIFI4
CONFIG_BT_MESH_CRYPTO_LIB
```

**被弱选择（Implied by）**

```text
CONFIG_CRYPTO_MBEDTLS_SHIM
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA)、[`CONFIG_MBEDTLS_CIPHER_ALL_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHER_ALL_ENABLED)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8)、[`CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256)、[`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG)、[`CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON)、[`CONFIG_WIFI_BFLB_WIFI4`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB_WIFI4)、[`CONFIG_BT_MESH_CRYPTO_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_CRYPTO_LIB)、[`CONFIG_CRYPTO_MBEDTLS_SHIM`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_MBEDTLS_SHIM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`、`CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON`。

<a id="CONFIG_PSA_WANT_ALG_CCM_STAR_NO_TAG"></a>

## 242.30 `CONFIG_PSA_WANT_ALG_CCM_STAR_NO_TAG`

**提示（Prompt）**：不带认证标签的 CCM* 模式（CCM star no tag）：`PSA_WANT_ALG_CCM_STAR_NO_TAG`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)。

<a id="CONFIG_PSA_WANT_ALG_CFB"></a>

## 242.31 `CONFIG_PSA_WANT_ALG_CFB`

**提示（Prompt）**：密码反馈模式（Cipher Feedback，CFB）：`PSA_WANT_ALG_CFB`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)。

<a id="CONFIG_PSA_WANT_ALG_CHACHA20_POLY1305"></a>

## 242.32 `CONFIG_PSA_WANT_ALG_CHACHA20_POLY1305`

**提示（Prompt）**：ChaCha20-Poly1305 认证加密（authenticated encryption）：`PSA_WANT_ALG_CHACHA20_POLY1305`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_WANT_KEY_TYPE_CHACHA20 && CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_MBEDTLS_CIPHER_ALL_ENABLED
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHER_ALL_ENABLED
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_CHACHA20_POLY1305
```

**被弱选择（Implied by）**

```text
CONFIG_WIREGUARD_CRYPTO
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_WANT_KEY_TYPE_CHACHA20`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_CHACHA20)、[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_MBEDTLS_CIPHER_ALL_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHER_ALL_ENABLED)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_CHACHA20_POLY1305`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_CHACHA20_POLY1305)、[`CONFIG_WIREGUARD_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIREGUARD_CRYPTO)。

<a id="CONFIG_PSA_WANT_ALG_CMAC"></a>

## 242.33 `CONFIG_PSA_WANT_ALG_CMAC`

**提示（Prompt）**：基于分组密码的消息认证码（Cipher-based Message Authentication Code，CMAC）：`PSA_WANT_ALG_CMAC`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO
CONFIG_BT_MESH_CRYPTO_LIB
CONFIG_BT_GATT_CACHING
CONFIG_BT_CRYPTO
CONFIG_LORAWAN_NATIVE
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA)、[`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG)、[`CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO)、[`CONFIG_BT_MESH_CRYPTO_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_CRYPTO_LIB)、[`CONFIG_BT_GATT_CACHING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GATT_CACHING)、[`CONFIG_BT_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CRYPTO)、[`CONFIG_LORAWAN_NATIVE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_NATIVE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`。

<a id="CONFIG_PSA_WANT_ALG_CTR"></a>

## 242.34 `CONFIG_PSA_WANT_ALG_CTR`

**提示（Prompt）**：计数器模式（Counter mode，CTR）：`PSA_WANT_ALG_CTR`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_MBEDTLS_CIPHER_ALL_ENABLED
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_MBEDTLS_CIPHER_ALL_ENABLED
CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO
```

**被弱选择（Implied by）**

```text
CONFIG_SSH_CRYPTO
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA)、[`CONFIG_MBEDTLS_CIPHER_ALL_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHER_ALL_ENABLED)、[`CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO)、[`CONFIG_SSH_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH_CRYPTO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SSH_CRYPTO`。

<a id="CONFIG_PSA_WANT_ALG_DETERMINISTIC_ECDSA"></a>

## 242.35 `CONFIG_PSA_WANT_ALG_DETERMINISTIC_ECDSA`

**提示（Prompt）**：确定性椭圆曲线数字签名算法（deterministic ECDSA）：`PSA_WANT_ALG_DETERMINISTIC_ECDSA`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`。

<a id="CONFIG_PSA_WANT_ALG_ECB_NO_PADDING"></a>

## 242.36 `CONFIG_PSA_WANT_ALG_ECB_NO_PADDING`

**提示（Prompt）**：无填充的电子密码本模式（ECB no padding）：`PSA_WANT_ALG_ECB_NO_PADDING`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO
CONFIG_BT_MESH_CRYPTO_LIB
CONFIG_BT_HOST_CRYPTO
CONFIG_BT_GATT_CACHING
CONFIG_BT_CRYPTO
CONFIG_LORAWAN_NATIVE
```

**被弱选择（Implied by）**

```text
CONFIG_CRYPTO_MBEDTLS_SHIM
CONFIG_QUIC_SOCKOPT_TLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG)、[`CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO)、[`CONFIG_BT_MESH_CRYPTO_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_CRYPTO_LIB)、[`CONFIG_BT_HOST_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HOST_CRYPTO)、[`CONFIG_BT_GATT_CACHING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GATT_CACHING)、[`CONFIG_BT_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CRYPTO)、[`CONFIG_LORAWAN_NATIVE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_NATIVE)、[`CONFIG_CRYPTO_MBEDTLS_SHIM`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_MBEDTLS_SHIM)、[`CONFIG_QUIC_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_SOCKOPT_TLS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`。

<a id="CONFIG_PSA_WANT_ALG_ECDH"></a>

## 242.37 `CONFIG_PSA_WANT_ALG_ECDH`

**提示（Prompt）**：椭圆曲线迪菲–赫尔曼密钥协商（Elliptic Curve Diffie–Hellman，ECDH）：`PSA_WANT_ALG_ECDH`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON
CONFIG_ESP32_BT_LE_CRYPTO_STACK_MBEDTLS
CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO
CONFIG_FIDO2
CONFIG_BT_MESH_CRYPTO_LIB
CONFIG_BT_ECC
```

**被弱选择（Implied by）**

```text
CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED
CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED
CONFIG_QUIC_SOCKOPT_TLS
CONFIG_SSH_CRYPTO
CONFIG_WIREGUARD_CRYPTO
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256)、[`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG)、[`CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON)、[`CONFIG_ESP32_BT_LE_CRYPTO_STACK_MBEDTLS`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_CRYPTO_STACK_MBEDTLS)、[`CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO)、[`CONFIG_FIDO2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2)、[`CONFIG_BT_MESH_CRYPTO_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_CRYPTO_LIB)、[`CONFIG_BT_ECC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ECC)、[`CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED)、[`CONFIG_QUIC_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_SOCKOPT_TLS)、[`CONFIG_SSH_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH_CRYPTO)、[`CONFIG_WIREGUARD_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIREGUARD_CRYPTO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`、`CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON`、`CONFIG_SSH_CRYPTO`。

<a id="CONFIG_PSA_WANT_ALG_ECDSA"></a>

## 242.38 `CONFIG_PSA_WANT_ALG_ECDSA`

**提示（Prompt）**：椭圆曲线数字签名算法（Elliptic Curve Digital Signature Algorithm，ECDSA）：`PSA_WANT_ALG_ECDSA`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON
CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO
CONFIG_FIDO2
CONFIG_JWT_SIGN_ECDSA_PSA
```

**被弱选择（Implied by）**

```text
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256)、[`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG)、[`CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON)、[`CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO)、[`CONFIG_FIDO2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2)、[`CONFIG_JWT_SIGN_ECDSA_PSA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_JWT_SIGN_ECDSA_PSA)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`、`CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON`。

<a id="CONFIG_PSA_WANT_ALG_FFDH"></a>

## 242.39 `CONFIG_PSA_WANT_ALG_FFDH`

**提示（Prompt）**：有限域迪菲–赫尔曼密钥协商（Finite Field Diffie–Hellman，FFDH）：`PSA_WANT_ALG_FFDH`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)。

<a id="CONFIG_PSA_WANT_ALG_GCM"></a>

## 242.40 `CONFIG_PSA_WANT_ALG_GCM`

**提示（Prompt）**：伽罗瓦／计数器模式（Galois/Counter Mode，GCM）：`PSA_WANT_ALG_GCM`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_EAP_TLSV1_3
CONFIG_MBEDTLS_CIPHER_ALL_ENABLED
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256
CONFIG_EAP_TLSV1_3
CONFIG_EAP_TLSV1_3
CONFIG_MBEDTLS_CIPHER_ALL_ENABLED
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256
CONFIG_FIDO2
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_AES_GCM
```

**被弱选择（Implied by）**

```text
CONFIG_CRYPTO_MBEDTLS_SHIM
CONFIG_QUIC_SOCKOPT_TLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_EAP_TLSV1_3`](P235_modules_hostap_配置项参考.md#CONFIG_EAP_TLSV1_3)、[`CONFIG_MBEDTLS_CIPHER_ALL_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHER_ALL_ENABLED)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256)、[`CONFIG_FIDO2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_AES_GCM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_AES_GCM)、[`CONFIG_CRYPTO_MBEDTLS_SHIM`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_MBEDTLS_SHIM)、[`CONFIG_QUIC_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_SOCKOPT_TLS)。

<a id="CONFIG_PSA_WANT_ALG_HKDF"></a>

## 242.41 `CONFIG_PSA_WANT_ALG_HKDF`

**提示（Prompt）**：基于 HMAC 的密钥派生函数（HMAC-based Key Derivation Function，HKDF）：`PSA_WANT_ALG_HKDF`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**主动选择（Selects）**

```text
CONFIG_PSA_WANT_ALG_HMAC
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_PSA_WANT_ALG_HMAC`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_HMAC)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT)、[`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`。

<a id="CONFIG_PSA_WANT_ALG_HKDF_EXPAND"></a>

## 242.42 `CONFIG_PSA_WANT_ALG_HKDF_EXPAND`

**提示（Prompt）**：HKDF 扩展步骤（HKDF Expand）：`PSA_WANT_ALG_HKDF_EXPAND`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**主动选择（Selects）**

```text
CONFIG_PSA_WANT_ALG_HMAC
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_MBEDTLS_SSL_PROTO_TLS1_3
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_MBEDTLS_SSL_PROTO_TLS1_3
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
```

**被弱选择（Implied by）**

```text
CONFIG_QUIC_SOCKOPT_TLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_PSA_WANT_ALG_HMAC`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_HMAC)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT)、[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_3`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_3)、[`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG)、[`CONFIG_QUIC_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_SOCKOPT_TLS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`。

<a id="CONFIG_PSA_WANT_ALG_HKDF_EXTRACT"></a>

## 242.43 `CONFIG_PSA_WANT_ALG_HKDF_EXTRACT`

**提示（Prompt）**：HKDF 提取步骤（HKDF Extract）：`PSA_WANT_ALG_HKDF_EXTRACT`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**主动选择（Selects）**

```text
CONFIG_PSA_WANT_ALG_HMAC
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_MBEDTLS_SSL_PROTO_TLS1_3
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_MBEDTLS_SSL_PROTO_TLS1_3
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
```

**被弱选择（Implied by）**

```text
CONFIG_QUIC_SOCKOPT_TLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_PSA_WANT_ALG_HMAC`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_HMAC)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT)、[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_3`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_3)、[`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG)、[`CONFIG_QUIC_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_SOCKOPT_TLS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`。

<a id="CONFIG_PSA_WANT_ALG_HMAC"></a>

## 242.44 `CONFIG_PSA_WANT_ALG_HMAC`

**提示（Prompt）**：基于哈希的消息认证码（Hash-based Message Authentication Code，HMAC）：`PSA_WANT_ALG_HMAC`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_PSA_WANT_ALG_HKDF
CONFIG_PSA_WANT_ALG_HKDF_EXTRACT
CONFIG_PSA_WANT_ALG_HKDF_EXPAND
CONFIG_PSA_WANT_ALG_PBKDF2_HMAC
CONFIG_PSA_WANT_ALG_TLS12_PRF
CONFIG_PSA_WANT_ALG_TLS12_PSK_TO_MS
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_PSA_WANT_ALG_HKDF
CONFIG_PSA_WANT_ALG_HKDF_EXTRACT
CONFIG_PSA_WANT_ALG_HKDF_EXPAND
CONFIG_PSA_WANT_ALG_PBKDF2_HMAC
CONFIG_PSA_WANT_ALG_TLS12_PRF
CONFIG_PSA_WANT_ALG_TLS12_PSK_TO_MS
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON
CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO
CONFIG_FIDO2
CONFIG_FIDO2_EXT_HMAC_SECRET
CONFIG_BT_MESH_CRYPTO_LIB
CONFIG_NET_IPV6_IID_STABLE
CONFIG_NET_IPV6_PE
```

**被弱选择（Implied by）**

```text
CONFIG_SSH_CRYPTO
CONFIG_WIREGUARD_CRYPTO
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA)、[`CONFIG_PSA_WANT_ALG_HKDF`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_HKDF)、[`CONFIG_PSA_WANT_ALG_HKDF_EXTRACT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_HKDF_EXTRACT)、[`CONFIG_PSA_WANT_ALG_HKDF_EXPAND`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_HKDF_EXPAND)、[`CONFIG_PSA_WANT_ALG_PBKDF2_HMAC`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_PBKDF2_HMAC)、[`CONFIG_PSA_WANT_ALG_TLS12_PRF`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_TLS12_PRF)、[`CONFIG_PSA_WANT_ALG_TLS12_PSK_TO_MS`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_TLS12_PSK_TO_MS)、[`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG)、[`CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON)、[`CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO)、[`CONFIG_FIDO2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2)、[`CONFIG_FIDO2_EXT_HMAC_SECRET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2_EXT_HMAC_SECRET)、[`CONFIG_BT_MESH_CRYPTO_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_CRYPTO_LIB)、[`CONFIG_NET_IPV6_IID_STABLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_IID_STABLE)、[`CONFIG_NET_IPV6_PE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_PE)、[`CONFIG_SSH_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH_CRYPTO)、[`CONFIG_WIREGUARD_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIREGUARD_CRYPTO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`、`CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON`、`CONFIG_SSH_CRYPTO`。

<a id="CONFIG_PSA_WANT_ALG_JPAKE"></a>

## 242.45 `CONFIG_PSA_WANT_ALG_JPAKE`

**提示（Prompt）**：采用口令认证的 Juggling 密钥交换（Password Authenticated Key Exchange by Juggling，J-PAKE）：`PSA_WANT_ALG_JPAKE`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8)、[`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`。

<a id="CONFIG_PSA_WANT_ALG_MD5"></a>

## 242.46 `CONFIG_PSA_WANT_ALG_MD5`

**提示（Prompt）**：MD5 消息摘要算法（Message Digest 5）：`PSA_WANT_ALG_MD5`

**说明（Help）**

MD5 散列算法（hash algorithm）安全性较弱，已弃用，不应使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**主动选择（Selects）**

```text
CONFIG_NOT_SECURE
```

**被选择（Selected by）**

```text
CONFIG_MBEDTLS_HASH_ALL_ENABLED
CONFIG_MBEDTLS_HASH_ALL_ENABLED
CONFIG_BT_OBEX_AUTH
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_NOT_SECURE`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_NOT_SECURE)、[`CONFIG_MBEDTLS_HASH_ALL_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_HASH_ALL_ENABLED)、[`CONFIG_BT_OBEX_AUTH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBEX_AUTH)。

<a id="CONFIG_PSA_WANT_ALG_OFB"></a>

## 242.47 `CONFIG_PSA_WANT_ALG_OFB`

**提示（Prompt）**：输出反馈模式（Output Feedback，OFB）：`PSA_WANT_ALG_OFB`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)。

<a id="CONFIG_PSA_WANT_ALG_PBKDF2_AES_CMAC_PRF_128"></a>

## 242.48 `CONFIG_PSA_WANT_ALG_PBKDF2_AES_CMAC_PRF_128`

**提示（Prompt）**：采用 AES-CMAC-PRF-128 的基于口令的密钥派生函数 2（PBKDF2）：`PSA_WANT_ALG_PBKDF2_AES_CMAC_PRF_128`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_WANT_ALG_CMAC && CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:109`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L109)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_WANT_ALG_CMAC`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_CMAC)、[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA)。

<a id="CONFIG_PSA_WANT_ALG_PBKDF2_HMAC"></a>

## 242.49 `CONFIG_PSA_WANT_ALG_PBKDF2_HMAC`

**提示（Prompt）**：采用 HMAC 的基于口令的密钥派生函数 2（PBKDF2）：`PSA_WANT_ALG_PBKDF2_HMAC`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**主动选择（Selects）**

```text
CONFIG_PSA_WANT_ALG_HMAC
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_PSA_WANT_ALG_HMAC`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_HMAC)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA)、[`CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO)。

<a id="CONFIG_PSA_WANT_ALG_RIPEMD160"></a>

## 242.50 `CONFIG_PSA_WANT_ALG_RIPEMD160`

**提示（Prompt）**：RIPEMD-160 哈希算法（hash algorithm）：`PSA_WANT_ALG_RIPEMD160`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:114`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L114)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)。

<a id="CONFIG_PSA_WANT_ALG_RSA_OAEP"></a>

## 242.51 `CONFIG_PSA_WANT_ALG_RSA_OAEP`

**提示（Prompt）**：采用最优非对称加密填充的 RSA（RSA-OAEP）：`PSA_WANT_ALG_RSA_OAEP`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_EAP_TLSV1_3
CONFIG_EAP_TLSV1_3
CONFIG_EAP_TLSV1_3
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:118`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L118)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_EAP_TLSV1_3`](P235_modules_hostap_配置项参考.md#CONFIG_EAP_TLSV1_3)。

<a id="CONFIG_PSA_WANT_ALG_RSA_PKCS1V15_CRYPT"></a>

## 242.52 `CONFIG_PSA_WANT_ALG_RSA_PKCS1V15_CRYPT`

**提示（Prompt）**：RSA PKCS#1 v1.5 加密（encryption）：`PSA_WANT_ALG_RSA_PKCS1V15_CRYPT`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:122`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L122)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)。

<a id="CONFIG_PSA_WANT_ALG_RSA_PKCS1V15_SIGN"></a>

## 242.53 `CONFIG_PSA_WANT_ALG_RSA_PKCS1V15_SIGN`

**提示（Prompt）**：RSA PKCS#1 v1.5 签名（signature）：`PSA_WANT_ALG_RSA_PKCS1V15_SIGN`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_JWT_SIGN_RSA_PSA
```

**被弱选择（Implied by）**

```text
CONFIG_SSH_CRYPTO
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:126`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L126)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256)、[`CONFIG_JWT_SIGN_RSA_PSA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_JWT_SIGN_RSA_PSA)、[`CONFIG_SSH_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH_CRYPTO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SSH_CRYPTO`。

<a id="CONFIG_PSA_WANT_ALG_RSA_PSS"></a>

## 242.54 `CONFIG_PSA_WANT_ALG_RSA_PSS`

**提示（Prompt）**：RSA 概率签名方案（Probabilistic Signature Scheme，PSS）：`PSA_WANT_ALG_RSA_PSS`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:130`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L130)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256)。

<a id="CONFIG_PSA_WANT_ALG_SHA3_224"></a>

## 242.55 `CONFIG_PSA_WANT_ALG_SHA3_224`

**提示（Prompt）**：SHA3-224 安全哈希算法（Secure Hash Algorithm）：`PSA_WANT_ALG_SHA3_224`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被弱选择（Implied by）**

```text
CONFIG_CRYPTO_MBEDTLS_SHIM
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:159`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L159)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_CRYPTO_MBEDTLS_SHIM`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_MBEDTLS_SHIM)。

<a id="CONFIG_PSA_WANT_ALG_SHA3_256"></a>

## 242.56 `CONFIG_PSA_WANT_ALG_SHA3_256`

**提示（Prompt）**：SHA3-256 安全哈希算法（Secure Hash Algorithm）：`PSA_WANT_ALG_SHA3_256`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被弱选择（Implied by）**

```text
CONFIG_CRYPTO_MBEDTLS_SHIM
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:163`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L163)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_CRYPTO_MBEDTLS_SHIM`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_MBEDTLS_SHIM)。

<a id="CONFIG_PSA_WANT_ALG_SHA3_384"></a>

## 242.57 `CONFIG_PSA_WANT_ALG_SHA3_384`

**提示（Prompt）**：SHA3-384 安全哈希算法（Secure Hash Algorithm）：`PSA_WANT_ALG_SHA3_384`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被弱选择（Implied by）**

```text
CONFIG_CRYPTO_MBEDTLS_SHIM
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:167`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L167)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_CRYPTO_MBEDTLS_SHIM`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_MBEDTLS_SHIM)。

<a id="CONFIG_PSA_WANT_ALG_SHA3_512"></a>

## 242.58 `CONFIG_PSA_WANT_ALG_SHA3_512`

**提示（Prompt）**：SHA3-512 安全哈希算法（Secure Hash Algorithm）：`PSA_WANT_ALG_SHA3_512`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被弱选择（Implied by）**

```text
CONFIG_CRYPTO_MBEDTLS_SHIM
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:171`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L171)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_CRYPTO_MBEDTLS_SHIM`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_MBEDTLS_SHIM)。

<a id="CONFIG_PSA_WANT_ALG_SHAKE128"></a>

## 242.59 `CONFIG_PSA_WANT_ALG_SHAKE128`

**提示（Prompt）**：SHAKE128 可扩展输出函数（Extendable-Output Function，XOF）：`PSA_WANT_ALG_SHAKE128`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:195`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L195)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)。

<a id="CONFIG_PSA_WANT_ALG_SHAKE256"></a>

## 242.60 `CONFIG_PSA_WANT_ALG_SHAKE256`

**提示（Prompt）**：SHAKE256 可扩展输出函数（Extendable-Output Function，XOF）：`PSA_WANT_ALG_SHAKE256`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:199`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L199)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)。

<a id="CONFIG_PSA_WANT_ALG_SHA_1"></a>

## 242.61 `CONFIG_PSA_WANT_ALG_SHA_1`

**提示（Prompt）**：SHA-1 安全哈希算法（Secure Hash Algorithm）：`PSA_WANT_ALG_SHA_1`

**说明（Help）**

SHA-1 散列算法（hash algorithm）安全性较弱，已弃用，不应直接用于散列数据。原文认为，它仍可用于 HMAC 等不受底层散列原始长度扩展攻击（raw length-extension attacks）影响的用途。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_MBEDTLS_HASH_ALL_ENABLED
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_MBEDTLS_HASH_ALL_ENABLED
CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO
CONFIG_MCP_TRANSPORT_HTTP
CONFIG_HTTP_SERVER_WEBSOCKET
CONFIG_WEBSOCKET_CLIENT
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:134`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L134)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA)、[`CONFIG_MBEDTLS_HASH_ALL_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_HASH_ALL_ENABLED)、[`CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO)、[`CONFIG_MCP_TRANSPORT_HTTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCP_TRANSPORT_HTTP)、[`CONFIG_HTTP_SERVER_WEBSOCKET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HTTP_SERVER_WEBSOCKET)、[`CONFIG_WEBSOCKET_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WEBSOCKET_CLIENT)。

<a id="CONFIG_PSA_WANT_ALG_SHA_224"></a>

## 242.62 `CONFIG_PSA_WANT_ALG_SHA_224`

**提示（Prompt）**：SHA-224 安全哈希算法（Secure Hash Algorithm）：`PSA_WANT_ALG_SHA_224`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_MBEDTLS_HASH_ALL_ENABLED
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_MBEDTLS_HASH_ALL_ENABLED
```

**被弱选择（Implied by）**

```text
CONFIG_CRYPTO_MBEDTLS_SHIM
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:143`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L143)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA)、[`CONFIG_MBEDTLS_HASH_ALL_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_HASH_ALL_ENABLED)、[`CONFIG_CRYPTO_MBEDTLS_SHIM`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_MBEDTLS_SHIM)。

<a id="CONFIG_PSA_WANT_ALG_SHA_256"></a>

## 242.63 `CONFIG_PSA_WANT_ALG_SHA_256`

**提示（Prompt）**：SHA-256 安全哈希算法（Secure Hash Algorithm）：`PSA_WANT_ALG_SHA_256`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_MBEDTLS_HASH_ALL_ENABLED
CONFIG_MBEDTLS_ENTROPY_C
CONFIG_MBEDTLS_LMS_C
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_MBEDTLS_HASH_ALL_ENABLED
CONFIG_MBEDTLS_ENTROPY_C
CONFIG_MBEDTLS_LMS_C
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON
CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO
CONFIG_FIDO2
CONFIG_BT_MESH_CRYPTO_LIB
CONFIG_JWT_SIGN_RSA_PSA
CONFIG_JWT_SIGN_ECDSA_PSA
CONFIG_MCUMGR_GRP_FS_HASH_SHA256
CONFIG_UPDATEHUB
CONFIG_NET_IPV6_IID_STABLE
CONFIG_NET_IPV6_PE
CONFIG_TLS_CREDENTIALS_BACKEND_PROTECTED_STORAGE
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_DEVICE_ID_HASH
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_ENTRY_UID_HASH
CONFIG_FLASH_AREA_CHECK_INTEGRITY
```

**被弱选择（Implied by）**

```text
CONFIG_MBEDTLS_PSA_P256M_DRIVER_ENABLED
CONFIG_MBEDTLS_PSA_P256M_DRIVER_ENABLED
CONFIG_CRYPTO_MBEDTLS_SHIM
CONFIG_QUIC_SOCKOPT_TLS
CONFIG_SSH_CRYPTO
CONFIG_WIREGUARD_CRYPTO
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:147`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L147)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA)、[`CONFIG_MBEDTLS_HASH_ALL_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_HASH_ALL_ENABLED)、[`CONFIG_MBEDTLS_ENTROPY_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_ENTROPY_C)、[`CONFIG_MBEDTLS_LMS_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_LMS_C)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256)、[`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG)、[`CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON)、[`CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO)、[`CONFIG_FIDO2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2)、[`CONFIG_BT_MESH_CRYPTO_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_CRYPTO_LIB)、[`CONFIG_JWT_SIGN_RSA_PSA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_JWT_SIGN_RSA_PSA)、[`CONFIG_JWT_SIGN_ECDSA_PSA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_JWT_SIGN_ECDSA_PSA)、[`CONFIG_MCUMGR_GRP_FS_HASH_SHA256`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_GRP_FS_HASH_SHA256)、[`CONFIG_UPDATEHUB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UPDATEHUB)、[`CONFIG_NET_IPV6_IID_STABLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_IID_STABLE)、[`CONFIG_NET_IPV6_PE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_PE)、[`CONFIG_TLS_CREDENTIALS_BACKEND_PROTECTED_STORAGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TLS_CREDENTIALS_BACKEND_PROTECTED_STORAGE)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_DEVICE_ID_HASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_DEVICE_ID_HASH)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_ENTRY_UID_HASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_ENTRY_UID_HASH)、[`CONFIG_FLASH_AREA_CHECK_INTEGRITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_AREA_CHECK_INTEGRITY)、[`CONFIG_MBEDTLS_PSA_P256M_DRIVER_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_PSA_P256M_DRIVER_ENABLED)、[`CONFIG_CRYPTO_MBEDTLS_SHIM`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_MBEDTLS_SHIM)、[`CONFIG_QUIC_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_SOCKOPT_TLS)、[`CONFIG_SSH_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH_CRYPTO)、[`CONFIG_WIREGUARD_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIREGUARD_CRYPTO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`、`CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON`、`CONFIG_SSH_CRYPTO`。

<a id="CONFIG_PSA_WANT_ALG_SHA_384"></a>

## 242.64 `CONFIG_PSA_WANT_ALG_SHA_384`

**提示（Prompt）**：SHA-384 安全哈希算法（Secure Hash Algorithm）：`PSA_WANT_ALG_SHA_384`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_MBEDTLS_HASH_ALL_ENABLED
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_MBEDTLS_HASH_ALL_ENABLED
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384
```

**被弱选择（Implied by）**

```text
CONFIG_CRYPTO_MBEDTLS_SHIM
CONFIG_QUIC_SOCKOPT_TLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:151`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L151)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA)、[`CONFIG_MBEDTLS_HASH_ALL_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_HASH_ALL_ENABLED)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384)、[`CONFIG_CRYPTO_MBEDTLS_SHIM`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_MBEDTLS_SHIM)、[`CONFIG_QUIC_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_SOCKOPT_TLS)。

<a id="CONFIG_PSA_WANT_ALG_SHA_512"></a>

## 242.65 `CONFIG_PSA_WANT_ALG_SHA_512`

**提示（Prompt）**：SHA-512 安全哈希算法（Secure Hash Algorithm）：`PSA_WANT_ALG_SHA_512`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_MBEDTLS_HASH_ALL_ENABLED
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_MBEDTLS_HASH_ALL_ENABLED
```

**被弱选择（Implied by）**

```text
CONFIG_CRYPTO_MBEDTLS_SHIM
CONFIG_SSH_HOST_KEY_ALG_RSA_SHA2_512
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:155`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L155)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA)、[`CONFIG_MBEDTLS_HASH_ALL_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_HASH_ALL_ENABLED)、[`CONFIG_CRYPTO_MBEDTLS_SHIM`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_MBEDTLS_SHIM)、[`CONFIG_SSH_HOST_KEY_ALG_RSA_SHA2_512`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH_HOST_KEY_ALG_RSA_SHA2_512)。

<a id="CONFIG_PSA_WANT_ALG_STREAM_CIPHER"></a>

## 242.66 `CONFIG_PSA_WANT_ALG_STREAM_CIPHER`

**提示（Prompt）**：流密码（stream cipher）：`PSA_WANT_ALG_STREAM_CIPHER`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_WANT_KEY_TYPE_CHACHA20 && CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:175`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L175)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_WANT_KEY_TYPE_CHACHA20`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_CHACHA20)、[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)。

<a id="CONFIG_PSA_WANT_ALG_TLS12_ECJPAKE_TO_PMS"></a>

## 242.67 `CONFIG_PSA_WANT_ALG_TLS12_ECJPAKE_TO_PMS`

**提示（Prompt）**：由 TLS 1.2 EC J-PAKE 派生预主密钥（pre-master secret，PMS）：`PSA_WANT_ALG_TLS12_ECJPAKE_TO_PMS`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_WANT_ALG_SHA_256 && CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:190`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L190)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_WANT_ALG_SHA_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_256)、[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`。

<a id="CONFIG_PSA_WANT_ALG_TLS12_PRF"></a>

## 242.68 `CONFIG_PSA_WANT_ALG_TLS12_PRF`

**提示（Prompt）**：TLS 1.2 伪随机函数（Pseudo-Random Function，PRF）：`PSA_WANT_ALG_TLS12_PRF`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**主动选择（Selects）**

```text
CONFIG_PSA_WANT_ALG_HMAC
```

**被选择（Selected by）**

```text
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:180`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L180)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_PSA_WANT_ALG_HMAC`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_HMAC)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256)、[`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`。

<a id="CONFIG_PSA_WANT_ALG_TLS12_PSK_TO_MS"></a>

## 242.69 `CONFIG_PSA_WANT_ALG_TLS12_PSK_TO_MS`

**提示（Prompt）**：由 TLS 1.2 预共享密钥（PSK）派生主密钥（master secret，MS）：`PSA_WANT_ALG_TLS12_PSK_TO_MS`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**主动选择（Selects）**

```text
CONFIG_PSA_WANT_ALG_HMAC
```

**被选择（Selected by）**

```text
CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:185`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L185)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_PSA_WANT_ALG_HMAC`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_HMAC)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256)。

<a id="CONFIG_PSA_WANT_DH_RFC7919_2048"></a>

## 242.70 `CONFIG_PSA_WANT_DH_RFC7919_2048`

**提示（Prompt）**：RFC 7919 的 2048 位迪菲–赫尔曼群（Diffie–Hellman group）：`PSA_WANT_DH_RFC7919_2048`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:239`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L239)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)。

<a id="CONFIG_PSA_WANT_DH_RFC7919_3072"></a>

## 242.71 `CONFIG_PSA_WANT_DH_RFC7919_3072`

**提示（Prompt）**：RFC 7919 的 3072 位迪菲–赫尔曼群（Diffie–Hellman group）：`PSA_WANT_DH_RFC7919_3072`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:243`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L243)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)。

<a id="CONFIG_PSA_WANT_DH_RFC7919_4096"></a>

## 242.72 `CONFIG_PSA_WANT_DH_RFC7919_4096`

**提示（Prompt）**：RFC 7919 的 4096 位迪菲–赫尔曼群（Diffie–Hellman group）：`PSA_WANT_DH_RFC7919_4096`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:247`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L247)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)。

<a id="CONFIG_PSA_WANT_DH_RFC7919_6144"></a>

## 242.73 `CONFIG_PSA_WANT_DH_RFC7919_6144`

**提示（Prompt）**：RFC 7919 的 6144 位迪菲–赫尔曼群（Diffie–Hellman group）：`PSA_WANT_DH_RFC7919_6144`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:251`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L251)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)。

<a id="CONFIG_PSA_WANT_DH_RFC7919_8192"></a>

## 242.74 `CONFIG_PSA_WANT_DH_RFC7919_8192`

**提示（Prompt）**：RFC 7919 的 8192 位迪菲–赫尔曼群（Diffie–Hellman group）：`PSA_WANT_DH_RFC7919_8192`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:255`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L255)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)。

<a id="CONFIG_PSA_WANT_ECC_BRAINPOOL_P_R1_256"></a>

## 242.75 `CONFIG_PSA_WANT_ECC_BRAINPOOL_P_R1_256`

**提示（Prompt）**：Brainpool 256 位 P-r1 椭圆曲线（elliptic curve）：`PSA_WANT_ECC_BRAINPOOL_P_R1_256`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:203`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L203)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)。

<a id="CONFIG_PSA_WANT_ECC_BRAINPOOL_P_R1_384"></a>

## 242.76 `CONFIG_PSA_WANT_ECC_BRAINPOOL_P_R1_384`

**提示（Prompt）**：Brainpool 384 位 P-r1 椭圆曲线（elliptic curve）：`PSA_WANT_ECC_BRAINPOOL_P_R1_384`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:207`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L207)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)。

<a id="CONFIG_PSA_WANT_ECC_BRAINPOOL_P_R1_512"></a>

## 242.77 `CONFIG_PSA_WANT_ECC_BRAINPOOL_P_R1_512`

**提示（Prompt）**：Brainpool 512 位 P-r1 椭圆曲线（elliptic curve）：`PSA_WANT_ECC_BRAINPOOL_P_R1_512`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:211`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L211)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)。

<a id="CONFIG_PSA_WANT_ECC_MONTGOMERY_255"></a>

## 242.78 `CONFIG_PSA_WANT_ECC_MONTGOMERY_255`

**提示（Prompt）**：255 位 Montgomery 椭圆曲线（elliptic curve）：`PSA_WANT_ECC_MONTGOMERY_255`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被弱选择（Implied by）**

```text
CONFIG_QUIC_SOCKOPT_TLS
CONFIG_SSH_CRYPTO
CONFIG_WIREGUARD_CRYPTO
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:215`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L215)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_QUIC_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_SOCKOPT_TLS)、[`CONFIG_SSH_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH_CRYPTO)、[`CONFIG_WIREGUARD_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIREGUARD_CRYPTO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SSH_CRYPTO`。

<a id="CONFIG_PSA_WANT_ECC_MONTGOMERY_448"></a>

## 242.79 `CONFIG_PSA_WANT_ECC_MONTGOMERY_448`

**提示（Prompt）**：448 位 Montgomery 椭圆曲线（elliptic curve）：`PSA_WANT_ECC_MONTGOMERY_448`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:219`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L219)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)。

<a id="CONFIG_PSA_WANT_ECC_SECP_K1_256"></a>

## 242.80 `CONFIG_PSA_WANT_ECC_SECP_K1_256`

**提示（Prompt）**：256 位 secp-k1 椭圆曲线（elliptic curve）：`PSA_WANT_ECC_SECP_K1_256`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:223`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L223)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)。

<a id="CONFIG_PSA_WANT_ECC_SECP_R1_256"></a>

## 242.81 `CONFIG_PSA_WANT_ECC_SECP_R1_256`

**提示（Prompt）**：256 位 secp-r1 椭圆曲线（elliptic curve）：`PSA_WANT_ECC_SECP_R1_256`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON
CONFIG_ESP32_BT_LE_CRYPTO_STACK_MBEDTLS
CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO
CONFIG_FIDO2
CONFIG_BT_MESH_CRYPTO_LIB
CONFIG_BT_ECC
CONFIG_JWT_SIGN_ECDSA_PSA
```

**被弱选择（Implied by）**

```text
CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256
CONFIG_QUIC_SOCKOPT_TLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:227`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L227)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG)、[`CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON)、[`CONFIG_ESP32_BT_LE_CRYPTO_STACK_MBEDTLS`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_CRYPTO_STACK_MBEDTLS)、[`CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO)、[`CONFIG_FIDO2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2)、[`CONFIG_BT_MESH_CRYPTO_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_CRYPTO_LIB)、[`CONFIG_BT_ECC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ECC)、[`CONFIG_JWT_SIGN_ECDSA_PSA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_JWT_SIGN_ECDSA_PSA)、[`CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256)、[`CONFIG_QUIC_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_SOCKOPT_TLS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`、`CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON`。

<a id="CONFIG_PSA_WANT_ECC_SECP_R1_384"></a>

## 242.82 `CONFIG_PSA_WANT_ECC_SECP_R1_384`

**提示（Prompt）**：384 位 secp-r1 椭圆曲线（elliptic curve）：`PSA_WANT_ECC_SECP_R1_384`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP
CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP
CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP
CONFIG_ESP32_WIFI_SUITE_B_192
```

**被弱选择（Implied by）**

```text
CONFIG_QUIC_SOCKOPT_TLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:231`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L231)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP)、[`CONFIG_ESP32_WIFI_SUITE_B_192`](P189_drivers_wifi_配置项参考_2.md#CONFIG_ESP32_WIFI_SUITE_B_192)、[`CONFIG_QUIC_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_SOCKOPT_TLS)。

<a id="CONFIG_PSA_WANT_ECC_SECP_R1_521"></a>

## 242.83 `CONFIG_PSA_WANT_ECC_SECP_R1_521`

**提示（Prompt）**：521 位 secp-r1 椭圆曲线（elliptic curve）：`PSA_WANT_ECC_SECP_R1_521`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:235`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L235)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)。

<a id="CONFIG_PSA_WANT_KEY_TYPE_AES"></a>

## 242.84 `CONFIG_PSA_WANT_KEY_TYPE_AES`

**提示（Prompt）**：AES 密钥类型（key type）：`PSA_WANT_KEY_TYPE_AES`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_MBEDTLS_CIPHER_ALL_ENABLED
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
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_MBEDTLS_CIPHER_ALL_ENABLED
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
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON
CONFIG_WIFI_BFLB_WIFI4
CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO
CONFIG_BT_MESH_CRYPTO_LIB
CONFIG_BT_HOST_CRYPTO
CONFIG_BT_GATT_CACHING
CONFIG_BT_CRYPTO
CONFIG_LORAWAN_NATIVE
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_AES_GCM
```

**被弱选择（Implied by）**

```text
CONFIG_CRYPTO_MBEDTLS_SHIM
CONFIG_QUIC_SOCKOPT_TLS
CONFIG_SSH_CRYPTO
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:275`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L275)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA)、[`CONFIG_MBEDTLS_CIPHER_ALL_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHER_ALL_ENABLED)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256)、[`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG)、[`CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON)、[`CONFIG_WIFI_BFLB_WIFI4`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB_WIFI4)、[`CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO)、[`CONFIG_BT_MESH_CRYPTO_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_CRYPTO_LIB)、[`CONFIG_BT_HOST_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HOST_CRYPTO)、[`CONFIG_BT_GATT_CACHING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GATT_CACHING)、[`CONFIG_BT_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CRYPTO)、[`CONFIG_LORAWAN_NATIVE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_NATIVE)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_AES_GCM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_AES_GCM)、[`CONFIG_CRYPTO_MBEDTLS_SHIM`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_MBEDTLS_SHIM)、[`CONFIG_QUIC_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_SOCKOPT_TLS)、[`CONFIG_SSH_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH_CRYPTO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`、`CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON`、`CONFIG_SSH_CRYPTO`。

<a id="CONFIG_PSA_WANT_KEY_TYPE_ARIA"></a>

## 242.85 `CONFIG_PSA_WANT_KEY_TYPE_ARIA`

**提示（Prompt）**：ARIA 密钥类型（key type）：`PSA_WANT_KEY_TYPE_ARIA`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:279`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L279)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)。

<a id="CONFIG_PSA_WANT_KEY_TYPE_CAMELLIA"></a>

## 242.86 `CONFIG_PSA_WANT_KEY_TYPE_CAMELLIA`

**提示（Prompt）**：Camellia 密钥类型（key type）：`PSA_WANT_KEY_TYPE_CAMELLIA`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_MBEDTLS_CIPHER_ALL_ENABLED
CONFIG_MBEDTLS_CIPHER_ALL_ENABLED
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:283`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L283)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_MBEDTLS_CIPHER_ALL_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHER_ALL_ENABLED)。

<a id="CONFIG_PSA_WANT_KEY_TYPE_CHACHA20"></a>

## 242.87 `CONFIG_PSA_WANT_KEY_TYPE_CHACHA20`

**提示（Prompt）**：ChaCha20 密钥类型（key type）：`PSA_WANT_KEY_TYPE_CHACHA20`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_MBEDTLS_CIPHER_ALL_ENABLED
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHER_ALL_ENABLED
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_CHACHA20_POLY1305
```

**被弱选择（Implied by）**

```text
CONFIG_WIREGUARD_CRYPTO
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:287`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L287)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_MBEDTLS_CIPHER_ALL_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHER_ALL_ENABLED)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_CHACHA20_POLY1305`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_CHACHA20_POLY1305)、[`CONFIG_WIREGUARD_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIREGUARD_CRYPTO)。

<a id="CONFIG_PSA_WANT_KEY_TYPE_DERIVE"></a>

## 242.88 `CONFIG_PSA_WANT_KEY_TYPE_DERIVE`

**提示（Prompt）**：密钥派生输入类型（derive key type）：`PSA_WANT_KEY_TYPE_DERIVE`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256
```

**被弱选择（Implied by）**

```text
CONFIG_QUIC_SOCKOPT_TLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:259`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L259)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256)、[`CONFIG_QUIC_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_SOCKOPT_TLS)。

<a id="CONFIG_PSA_WANT_KEY_TYPE_DH_KEY_PAIR_EXPORT"></a>

## 242.89 `CONFIG_PSA_WANT_KEY_TYPE_DH_KEY_PAIR_EXPORT`

**提示（Prompt）**：迪菲–赫尔曼密钥对导出（DH key pair export）：`PSA_WANT_KEY_TYPE_DH_KEY_PAIR_EXPORT`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:339`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L339)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)。

<a id="CONFIG_PSA_WANT_KEY_TYPE_DH_KEY_PAIR_GENERATE"></a>

## 242.90 `CONFIG_PSA_WANT_KEY_TYPE_DH_KEY_PAIR_GENERATE`

**提示（Prompt）**：迪菲–赫尔曼密钥对生成（DH key pair generation）：`PSA_WANT_KEY_TYPE_DH_KEY_PAIR_GENERATE`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:343`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L343)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)。

<a id="CONFIG_PSA_WANT_KEY_TYPE_DH_KEY_PAIR_IMPORT"></a>

## 242.91 `CONFIG_PSA_WANT_KEY_TYPE_DH_KEY_PAIR_IMPORT`

**提示（Prompt）**：迪菲–赫尔曼密钥对导入（DH key pair import）：`PSA_WANT_KEY_TYPE_DH_KEY_PAIR_IMPORT`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:335`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L335)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)。

<a id="CONFIG_PSA_WANT_KEY_TYPE_DH_PUBLIC_KEY"></a>

## 242.92 `CONFIG_PSA_WANT_KEY_TYPE_DH_PUBLIC_KEY`

**提示（Prompt）**：迪菲–赫尔曼公钥类型（DH public key type）：`PSA_WANT_KEY_TYPE_DH_PUBLIC_KEY`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:295`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L295)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)。

<a id="CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_DERIVE"></a>

## 242.93 `CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_DERIVE`

**提示（Prompt）**：椭圆曲线密钥对派生（ECC key pair derivation）：`PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_DERIVE`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_BT_MESH_CRYPTO_LIB
```

**被弱选择（Implied by）**

```text
CONFIG_QUIC_SOCKOPT_TLS
CONFIG_WIREGUARD_CRYPTO
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:319`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L319)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG)、[`CONFIG_BT_MESH_CRYPTO_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_CRYPTO_LIB)、[`CONFIG_QUIC_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_SOCKOPT_TLS)、[`CONFIG_WIREGUARD_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIREGUARD_CRYPTO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`。

<a id="CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT"></a>

## 242.94 `CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT`

**提示（Prompt）**：椭圆曲线密钥对导出（ECC key pair export）：`PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON
CONFIG_ESP32_BT_LE_CRYPTO_STACK_MBEDTLS
CONFIG_ESP32_WIFI_ENABLE_WPA3_SAE
CONFIG_BT_MESH_CRYPTO_LIB
CONFIG_BT_ECC
```

**被弱选择（Implied by）**

```text
CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED
CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED
CONFIG_WIREGUARD_CRYPTO
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:311`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L311)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256)、[`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG)、[`CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON)、[`CONFIG_ESP32_BT_LE_CRYPTO_STACK_MBEDTLS`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_CRYPTO_STACK_MBEDTLS)、[`CONFIG_ESP32_WIFI_ENABLE_WPA3_SAE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_ENABLE_WPA3_SAE)、[`CONFIG_BT_MESH_CRYPTO_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_CRYPTO_LIB)、[`CONFIG_BT_ECC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ECC)、[`CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED)、[`CONFIG_WIREGUARD_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIREGUARD_CRYPTO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`、`CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON`。

<a id="CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE"></a>

## 242.95 `CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE`

**提示（Prompt）**：椭圆曲线密钥对生成（ECC key pair generation）：`PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON
CONFIG_ESP32_BT_LE_CRYPTO_STACK_MBEDTLS
CONFIG_ESP32_WIFI_ENABLE_WPA3_SAE
CONFIG_FIDO2
CONFIG_BT_MESH_CRYPTO_LIB
CONFIG_BT_ECC
```

**被弱选择（Implied by）**

```text
CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED
CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED
CONFIG_QUIC_SOCKOPT_TLS
CONFIG_SSH_CRYPTO
CONFIG_WIREGUARD_CRYPTO
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:315`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L315)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256)、[`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG)、[`CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON)、[`CONFIG_ESP32_BT_LE_CRYPTO_STACK_MBEDTLS`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_CRYPTO_STACK_MBEDTLS)、[`CONFIG_ESP32_WIFI_ENABLE_WPA3_SAE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_ENABLE_WPA3_SAE)、[`CONFIG_FIDO2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2)、[`CONFIG_BT_MESH_CRYPTO_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_CRYPTO_LIB)、[`CONFIG_BT_ECC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ECC)、[`CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED)、[`CONFIG_QUIC_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_SOCKOPT_TLS)、[`CONFIG_SSH_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH_CRYPTO)、[`CONFIG_WIREGUARD_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIREGUARD_CRYPTO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`、`CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON`、`CONFIG_SSH_CRYPTO`。

<a id="CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT"></a>

## 242.96 `CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT`

**提示（Prompt）**：椭圆曲线密钥对导入（ECC key pair import）：`PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON
CONFIG_ESP32_BT_LE_CRYPTO_STACK_MBEDTLS
CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO
CONFIG_BT_MESH_CRYPTO_LIB
CONFIG_BT_ECC
CONFIG_JWT_SIGN_ECDSA_PSA
```

**被弱选择（Implied by）**

```text
CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED
CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED
CONFIG_WIREGUARD_CRYPTO
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:307`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L307)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256)、[`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG)、[`CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON)、[`CONFIG_ESP32_BT_LE_CRYPTO_STACK_MBEDTLS`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_CRYPTO_STACK_MBEDTLS)、[`CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO)、[`CONFIG_BT_MESH_CRYPTO_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_CRYPTO_LIB)、[`CONFIG_BT_ECC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ECC)、[`CONFIG_JWT_SIGN_ECDSA_PSA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_JWT_SIGN_ECDSA_PSA)、[`CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED)、[`CONFIG_WIREGUARD_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIREGUARD_CRYPTO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`、`CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON`。

<a id="CONFIG_PSA_WANT_KEY_TYPE_ECC_PUBLIC_KEY"></a>

## 242.97 `CONFIG_PSA_WANT_KEY_TYPE_ECC_PUBLIC_KEY`

**提示（Prompt）**：椭圆曲线公钥类型（ECC public key type）：`PSA_WANT_KEY_TYPE_ECC_PUBLIC_KEY`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON
CONFIG_ESP32_BT_LE_CRYPTO_STACK_MBEDTLS
CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO
CONFIG_FIDO2
```

**被弱选择（Implied by）**

```text
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256
CONFIG_QUIC_SOCKOPT_TLS
CONFIG_SSH_CRYPTO
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:291`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L291)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA)、[`CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON)、[`CONFIG_ESP32_BT_LE_CRYPTO_STACK_MBEDTLS`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_CRYPTO_STACK_MBEDTLS)、[`CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_MBEDTLS_CRYPTO)、[`CONFIG_FIDO2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256)、[`CONFIG_QUIC_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_SOCKOPT_TLS)、[`CONFIG_SSH_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH_CRYPTO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON`、`CONFIG_SSH_CRYPTO`。

<a id="CONFIG_PSA_WANT_KEY_TYPE_HMAC"></a>

## 242.98 `CONFIG_PSA_WANT_KEY_TYPE_HMAC`

**提示（Prompt）**：HMAC 密钥类型（key type）：`PSA_WANT_KEY_TYPE_HMAC`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON
CONFIG_BT_MESH_CRYPTO_LIB
CONFIG_NET_IPV6_IID_STABLE
CONFIG_NET_IPV6_PE
```

**被弱选择（Implied by）**

```text
CONFIG_SSH_CRYPTO
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:271`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L271)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA)、[`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG)、[`CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON)、[`CONFIG_BT_MESH_CRYPTO_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_CRYPTO_LIB)、[`CONFIG_NET_IPV6_IID_STABLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_IID_STABLE)、[`CONFIG_NET_IPV6_PE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_PE)、[`CONFIG_SSH_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH_CRYPTO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`、`CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON`、`CONFIG_SSH_CRYPTO`。

<a id="CONFIG_PSA_WANT_KEY_TYPE_PASSWORD"></a>

## 242.99 `CONFIG_PSA_WANT_KEY_TYPE_PASSWORD`

**提示（Prompt）**：口令类型（password type）：`PSA_WANT_KEY_TYPE_PASSWORD`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:263`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L263)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)。

<a id="CONFIG_PSA_WANT_KEY_TYPE_PASSWORD_HASH"></a>

## 242.100 `CONFIG_PSA_WANT_KEY_TYPE_PASSWORD_HASH`

**提示（Prompt）**：口令哈希类型（password hash type）：`PSA_WANT_KEY_TYPE_PASSWORD_HASH`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO
```

**默认值（Defaults）**

```text
y if CONFIG_PSA_CRYPTO_ENABLE_ALL
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:267`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L267)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)。

<!-- kconfig-navigation -->

[上一章](P241_modules_mbedtls_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P243_modules_mbedtls_配置项参考_3.md)
