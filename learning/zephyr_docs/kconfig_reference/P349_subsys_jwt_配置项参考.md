---
id: learning.zephyr-docs.kconfig-reference.page-349
title: "`subsys/jwt`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第349章\_`subsys/jwt`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/jwt` 的 3 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_JWT"></a>

## 349.1 `CONFIG_JWT`

**提示（Prompt）**：JSON Web 令牌生成（JSON Web Token generation）

**说明（Help）**

启用 JSON Web 令牌（JWT）创建功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_JSON_LIBRARY
```

**定义位置（Location）**：[`subsys/jwt/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/jwt/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_JSON_LIBRARY`](P197_lib_配置项参考_1.md#CONFIG_JSON_LIBRARY)。

<a id="CONFIG_JWT_SIGN_ECDSA_PSA"></a>

## 349.2 `CONFIG_JWT_SIGN_ECDSA_PSA`

**提示（Prompt）**：使用椭圆曲线数字签名算法（ECDSA）签名 ES-256，并使用 PSA Crypto API。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**主动选择（Selects）**

```text
CONFIG_PSA_CRYPTO
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT
CONFIG_PSA_WANT_ALG_ECDSA
CONFIG_PSA_WANT_ECC_SECP_R1_256
CONFIG_PSA_WANT_ALG_SHA_256
```

**定义位置（Location）**：[`subsys/jwt/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/jwt/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → JSON Web 令牌生成（JSON Web Token generation） → JWT 签名算法（signature algorithm）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT)、[`CONFIG_PSA_WANT_ALG_ECDSA`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECDSA)、[`CONFIG_PSA_WANT_ECC_SECP_R1_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ECC_SECP_R1_256)、[`CONFIG_PSA_WANT_ALG_SHA_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_256)。

<a id="CONFIG_JWT_SIGN_RSA_PSA"></a>

## 349.3 `CONFIG_JWT_SIGN_RSA_PSA`

**提示（Prompt）**：使用 RSA 签名 RS-256，并使用 PSA Crypto API。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**主动选择（Selects）**

```text
CONFIG_PSA_CRYPTO
CONFIG_PSA_WANT_KEY_TYPE_RSA_PUBLIC_KEY
CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_IMPORT
CONFIG_PSA_WANT_ALG_RSA_PKCS1V15_SIGN
CONFIG_PSA_WANT_ALG_SHA_256
```

**定义位置（Location）**：[`subsys/jwt/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/jwt/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → JSON Web 令牌生成（JSON Web Token generation） → JWT 签名算法（signature algorithm）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_WANT_KEY_TYPE_RSA_PUBLIC_KEY`](P243_modules_mbedtls_配置项参考_3.md#CONFIG_PSA_WANT_KEY_TYPE_RSA_PUBLIC_KEY)、[`CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_IMPORT`](P243_modules_mbedtls_配置项参考_3.md#CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_IMPORT)、[`CONFIG_PSA_WANT_ALG_RSA_PKCS1V15_SIGN`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_RSA_PKCS1V15_SIGN)、[`CONFIG_PSA_WANT_ALG_SHA_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_256)。

<!-- kconfig-navigation -->

[上一章](P348_subsys_ipc_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P350_subsys_kvss_配置项参考.md)
