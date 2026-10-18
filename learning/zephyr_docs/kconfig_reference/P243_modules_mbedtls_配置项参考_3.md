---
id: learning.zephyr-docs.kconfig-reference.page-243
title: "`modules/mbedtls`配置项参考（3/3）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第243章\_`modules/mbedtls`配置项参考（3/3）

本章翻译官方 Kconfig 数据库中 `modules/mbedtls` 的 13 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_PSA_WANT_KEY_TYPE_RAW_DATA"></a>

## 243.1 `CONFIG_PSA_WANT_KEY_TYPE_RAW_DATA`

**提示（Prompt）**：原始数据类型（raw data type）：`PSA_WANT_KEY_TYPE_RAW_DATA`

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

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:299`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L299)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)。

<a id="CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_EXPORT"></a>

## 243.2 `CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_EXPORT`

**提示（Prompt）**：RSA 密钥对导出（RSA key pair export）：`PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_EXPORT`

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
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:327`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L327)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256)。

<a id="CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_GENERATE"></a>

## 243.3 `CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_GENERATE`

**提示（Prompt）**：RSA 密钥对生成（RSA key pair generation）：`PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_GENERATE`

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
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
```

**被弱选择（Implied by）**

```text
CONFIG_SSH_CRYPTO
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:331`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L331)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256)、[`CONFIG_SSH_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH_CRYPTO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SSH_CRYPTO`。

<a id="CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_IMPORT"></a>

## 243.4 `CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_IMPORT`

**提示（Prompt）**：RSA 密钥对导入（RSA key pair import）：`PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_IMPORT`

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
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
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

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:323`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L323)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256)、[`CONFIG_JWT_SIGN_RSA_PSA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_JWT_SIGN_RSA_PSA)、[`CONFIG_SSH_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH_CRYPTO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SSH_CRYPTO`。

<a id="CONFIG_PSA_WANT_KEY_TYPE_RSA_PUBLIC_KEY"></a>

## 243.5 `CONFIG_PSA_WANT_KEY_TYPE_RSA_PUBLIC_KEY`

**提示（Prompt）**：RSA 公钥类型（RSA public key type）：`PSA_WANT_KEY_TYPE_RSA_PUBLIC_KEY`

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
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA
CONFIG_JWT_SIGN_RSA_PSA
```

**被弱选择（Implied by）**

```text
CONFIG_SSH_CRYPTO
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.psa.auto:303`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.psa.auto#L303)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_CRYPTO_ENABLE_ALL`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_ENABLE_ALL)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA)、[`CONFIG_JWT_SIGN_RSA_PSA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_JWT_SIGN_RSA_PSA)、[`CONFIG_SSH_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH_CRYPTO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SSH_CRYPTO`。

<a id="CONFIG_TF_PSA_CRYPTO_BUILTIN"></a>

## 243.6 `CONFIG_TF_PSA_CRYPTO_BUILTIN`

**提示（Prompt）**：Zephyr 源码树内的 TF-PSA-Crypto 版本（in-tree version）

**说明（Help）**

链接 Zephyr 发行版附带的 TF-PSA-Crypto 源码。该版本与 Zephyr 集成良好，并受 Zephyr 支持，是推荐给多数用户的选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TF_PSA_CRYPTO_IMPLEMENTATION>
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → TF-PSA-Crypto 实现（implementation）

**配置项引用（Symbol References）**：[`CONFIG_TF_PSA_CRYPTO_IMPLEMENTATION`](P243_modules_mbedtls_配置项参考_3.md#CONFIG_TF_PSA_CRYPTO_IMPLEMENTATION)。

<a id="CONFIG_TF_PSA_CRYPTO_CONFIG_FILE"></a>

## 243.7 `CONFIG_TF_PSA_CRYPTO_CONFIG_FILE`

**提示（Prompt）**：TF-PSA-Crypto 配置文件（configuration file）

**说明（Help）**

指定构建 TF-PSA-Crypto 时使用的配置头文件（configuration header file）。默认文件可通过 Kconfig 调整。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**默认值（Defaults）**

```text
"config-tf-psa-crypto.h"
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_TF_PSA_CRYPTO_CUSTOM"></a>

## 243.8 `CONFIG_TF_PSA_CRYPTO_CUSTOM`

**提示（Prompt）**：自定义 TF-PSA-Crypto 库（Custom library）

**说明（Help）**

TF-PSA-Crypto 库必须在源码树外（out of tree）配置并添加。如果同时使用 `MBEDTLS_BUILTIN`，Mbed TLS 将不再自行添加和构建 TF-PSA-Crypto，但仍要求存在名为 `tfpsacrypto` 的 CMake 库。Zephyr 自身不会创建或使用该 CMake 库，用户需要为 Mbed TLS 的 CMake 配置提供它。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TF_PSA_CRYPTO_IMPLEMENTATION>
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → TF-PSA-Crypto 实现（implementation）

**配置项引用（Symbol References）**：[`CONFIG_TF_PSA_CRYPTO_IMPLEMENTATION`](P243_modules_mbedtls_配置项参考_3.md#CONFIG_TF_PSA_CRYPTO_IMPLEMENTATION)。

<a id="CONFIG_TF_PSA_CRYPTO_DRIVER_CONFIG_FILE"></a>

## 243.9 `CONFIG_TF_PSA_CRYPTO_DRIVER_CONFIG_FILE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

可选的驱动配置头文件（driver configuration header），在 `TF_PSA_CRYPTO_CONFIG_FILE` 的末尾包含。用于提供驱动分发接口（driver dispatch interface）所需的配置选项。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_TF_PSA_CRYPTO_CONFIG_FILE = "config-tf-psa-crypto.h" && CONFIG_MBEDTLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_TF_PSA_CRYPTO_CONFIG_FILE`](P243_modules_mbedtls_配置项参考_3.md#CONFIG_TF_PSA_CRYPTO_CONFIG_FILE)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_TF_PSA_CRYPTO_IMPLEMENTATION"></a>

## 243.10 `CONFIG_TF_PSA_CRYPTO_IMPLEMENTATION`

**提示（Prompt）**：TF-PSA-Crypto 实现（implementation）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**默认值（Defaults）**

```text
CONFIG_TF_PSA_CRYPTO_BUILTIN
```

**可选项（Choices）**

```text
CONFIG_TF_PSA_CRYPTO_BUILTIN
CONFIG_TF_PSA_CRYPTO_CUSTOM
CONFIG_TF_PSA_CRYPTO_BUILTIN
CONFIG_TF_PSA_CRYPTO_CUSTOM
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_TF_PSA_CRYPTO_BUILTIN`](P243_modules_mbedtls_配置项参考_3.md#CONFIG_TF_PSA_CRYPTO_BUILTIN)、[`CONFIG_TF_PSA_CRYPTO_CUSTOM`](P243_modules_mbedtls_配置项参考_3.md#CONFIG_TF_PSA_CRYPTO_CUSTOM)。

<a id="CONFIG_TF_PSA_CRYPTO_PQCP_MLDSA_87_ENABLED"></a>

## 243.11 `CONFIG_TF_PSA_CRYPTO_PQCP_MLDSA_87_ENABLED`

**提示（Prompt）**：后量子代码包（post-quantum code package，PQCP）的 mldsa-native 安全级别 87 驱动［实验性，EXPERIMENTAL］

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TF_PSA_CRYPTO_PQCP_MLDSA_ENABLED && CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:464`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L464)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → 后量子代码包（post-quantum code package，PQCP）的 mldsa-native 驱动［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_TF_PSA_CRYPTO_PQCP_MLDSA_ENABLED`](P243_modules_mbedtls_配置项参考_3.md#CONFIG_TF_PSA_CRYPTO_PQCP_MLDSA_ENABLED)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_TF_PSA_CRYPTO_PQCP_MLDSA_ENABLED"></a>

## 243.12 `CONFIG_TF_PSA_CRYPTO_PQCP_MLDSA_ENABLED`

**提示（Prompt）**：后量子代码包（post-quantum code package，PQCP）的 mldsa-native 驱动［实验性，EXPERIMENTAL］

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:458`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L458)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_TF_PSA_CRYPTO_USER_CONFIG_FILE"></a>

## 243.13 `CONFIG_TF_PSA_CRYPTO_USER_CONFIG_FILE`

**提示（Prompt）**：TF-PSA-Crypto 用户配置文件（User configuration file）

**说明（Help）**

若定义此项，其指定的头文件会在 `TF_PSA_CRYPTO_CONFIG_FILE` 之后包含。这样可以修改默认配置，包括取消已启用选项的定义（undefine）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS
```

**定义位置（Location）**：[`modules/mbedtls/Kconfig.tf-psa-crypto:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/mbedtls/Kconfig.tf-psa-crypto#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<!-- kconfig-navigation -->

[上一章](P242_modules_mbedtls_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P244_modules_nanopb_配置项参考.md)
