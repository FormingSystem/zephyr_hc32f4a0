---
id: learning.zephyr-docs.kconfig-reference.page-421
title: "`subsys/secure_storage`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第421章\_`subsys/secure_storage`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/secure_storage` 的 42 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SECURE_STORAGE"></a>

## 421.1 `CONFIG_SECURE_STORAGE`

**提示（Prompt）**：安全存储子系统（Secure storage subsystem）

**说明（Help）**

安全存储子系统（Secure storage subsystem）为尚无对应实现的开发板目标提供 PSA 安全存储 API（PSA Secure Storage API）函数，使应用能够以标准、可移植的方式使用该 API，以及 PSA Crypto API 中的持久密钥（Persistent key）。该子系统可配置，并可采用不同实现，以适应不同设备的能力。除提供 PSA 安全存储 API 的功能支持外，根据设备可用并实际使用的安全特性，它还可能保护静态存储数据（Data at rest）。但这种保护高度依赖设备和配置，并非子系统本身保证。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_BUILD_WITH_TFM
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_PSA_CRYPTO_STORAGE_C if CONFIG_MBEDTLS_PSA_CRYPTO_C
```

**被选择（Selected by）**

```text
CONFIG_FIDO2
```

**被弱选择（Implied by）**

```text
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_MBEDTLS_PSA_CRYPTO_STORAGE_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PSA_CRYPTO_STORAGE_C)、[`CONFIG_MBEDTLS_PSA_CRYPTO_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_PSA_CRYPTO_C)、[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)、[`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MBEDTLS_PSA_CRYPTO_STORAGE_C`、`CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG`。

<a id="CONFIG_SECURE_STORAGE_64_BIT_UID"></a>

## 421.2 `CONFIG_SECURE_STORAGE_64_BIT_UID`

**提示（Prompt）**：将 `psa_storage_uid_t` 设为 64 位

**说明（Help）**

Zephyr 默认使用 30 位的 `psa_storage_uid_t`，从而只需使用 32 位来标识表项，减少每个表项的内存占用。如果正在升级使用 Zephyr 4.3 之前版本、且已有存储数据的安装，应为向后兼容启用此项；因其他原因需要完整 64 位唯一标识符（UID）范围时，也可启用。注意：使用 `CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD` 时，此项同时影响生成的加密密钥和用于生成认证标签（Authentication tag）的附加数据，因此启用和禁用该项时存储的表项互不兼容。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SECURE_STORAGE
```

**被选择（Selected by）**

```text
CONFIG_TLS_CREDENTIALS_BACKEND_PROTECTED_STORAGE
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE)、[`CONFIG_TLS_CREDENTIALS_BACKEND_PROTECTED_STORAGE`](P408_subsys_net_配置项参考_18.md#CONFIG_TLS_CREDENTIALS_BACKEND_PROTECTED_STORAGE)。

<a id="CONFIG_SECURE_STORAGE_INIT_PRIORITY"></a>

## 421.3 `CONFIG_SECURE_STORAGE_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Initialization Priority）

**说明（Help）**

在 APPLICATION 级别随系统启动初始化的安全存储组件（Secure storage component）的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_SETTINGS || CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_ZMS || (CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD && !CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NO_INSECURE_KEY_WARNING)) && CONFIG_SECURE_STORAGE
```

**默认值（Defaults）**

```text
CONFIG_APPLICATION_INIT_PRIORITY
```

**取值范围（Ranges）**

```text
[0, 99]
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_SETTINGS`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_SETTINGS)、[`CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_ZMS`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_ZMS)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NO_INSECURE_KEY_WARNING`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NO_INSECURE_KEY_WARNING)、[`CONFIG_SECURE_STORAGE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE)、[`CONFIG_APPLICATION_INIT_PRIORITY`](P001_kernel_配置项参考_1.md#CONFIG_APPLICATION_INIT_PRIORITY)。

<a id="CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION"></a>

## 421.4 `CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION`

**提示（Prompt）**：内部可信存储（Internal Trusted Storage，ITS）API 实现

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SECURE_STORAGE
```

**可选项（Choices）**

```text
CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION_ZEPHYR
CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION_CUSTOM
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE)、[`CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION_ZEPHYR`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION_ZEPHYR)、[`CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION_CUSTOM`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION_CUSTOM)。

<a id="CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION_CUSTOM"></a>

## 421.5 `CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION_CUSTOM`

**提示（Prompt）**：自定义内部可信存储（ITS）实现

**说明（Help）**

使用自定义的内部可信存储（ITS）API 实现。需要实现 `<zephyr/secure_storage/its.h>` 中声明的函数；启用此 Kconfig 选项后，该头文件可用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION>
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 内部可信存储（Internal Trusted Storage，ITS）API 实现

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION)。

<a id="CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION_ZEPHYR"></a>

## 421.6 `CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION_ZEPHYR`

**提示（Prompt）**：Zephyr 的内部可信存储（ITS）实现

**说明（Help）**

使用 Zephyr 提供的内部可信存储（ITS）API 实现。它调用转换模块（Transform module）和存储模块（Store module）；这些模块均可配置，并支持自定义实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION>
```

**主动选择（Selects）**

```text
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE
CONFIG_SECURE_STORAGE_ITS_STORE_MODULE
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 内部可信存储（Internal Trusted Storage，ITS）API 实现

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE)、[`CONFIG_SECURE_STORAGE_ITS_STORE_MODULE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_STORE_MODULE)。

<a id="CONFIG_SECURE_STORAGE_ITS_MAX_DATA_SIZE"></a>

## 421.7 `CONFIG_SECURE_STORAGE_ITS_MAX_DATA_SIZE`

**提示（Prompt）**：内部可信存储（ITS）表项数据的最大大小（字节）

**说明（Help）**

内部可信存储（ITS）表项数据的最大大小，单位为字节。增大此值会增加处理 PSA ITS API 调用时的栈占用（Stack usage）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SECURE_STORAGE
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE)。

<a id="CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION"></a>

## 421.8 `CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION`

**提示（Prompt）**：内部可信存储（ITS）存储模块的实现

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SECURE_STORAGE_ITS_STORE_MODULE && CONFIG_SECURE_STORAGE
```

**可选项（Choices）**

```text
CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_ZMS
CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_SETTINGS
CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_NONE
CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_CUSTOM
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig.its_store:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig.its_store#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 内部可信存储（ITS）存储模块（Store module）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_ITS_STORE_MODULE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_STORE_MODULE)、[`CONFIG_SECURE_STORAGE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE)、[`CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_ZMS`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_ZMS)、[`CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_SETTINGS`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_SETTINGS)、[`CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_NONE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_NONE)、[`CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_CUSTOM`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_CUSTOM)。

<a id="CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_CUSTOM"></a>

## 421.9 `CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_CUSTOM`

**提示（Prompt）**：自定义 ITS 存储模块（Store module）实现

**说明（Help）**

实现 `<zephyr/secure_storage/its/store.h>` 中声明的函数；启用此 Kconfig 选项后，该头文件可用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION>
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig.its_store:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig.its_store#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 内部可信存储（ITS）存储模块（Store module） → 内部可信存储（ITS）存储模块的实现

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION)。

<a id="CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_NONE"></a>

## 421.10 `CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_NONE`

**提示（Prompt）**：不提供 ITS 存储模块（Store module）实现

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION>
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig.its_store:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig.its_store#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 内部可信存储（ITS）存储模块（Store module） → 内部可信存储（ITS）存储模块的实现

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION)。

<a id="CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_SETTINGS"></a>

## 421.11 `CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_SETTINGS`

**提示（Prompt）**：使用设置子系统（Settings subsystem）存储的 ITS 存储模块实现

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED && ((n && (n || n)) || (n && (n || n))) && CONFIG_SETTINGS && !CONFIG_SETTINGS_NONE && <choice CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION>
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig.its_store:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig.its_store#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 内部可信存储（ITS）存储模块（Store module） → 内部可信存储（ITS）存储模块的实现

**配置项引用（Symbol References）**：[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_SETTINGS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS)、[`CONFIG_SETTINGS_NONE`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_NONE)、[`CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION)。

<a id="CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_ZMS"></a>

## 421.12 `CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_ZMS`

**提示（Prompt）**：使用 Zephyr 内存存储（ZMS）保存数据的 ITS 存储模块实现

**说明（Help）**

此 ITS 存储模块（Store module）直接使用 Zephyr 内存存储（ZMS）保存数据，需要设备树 chosen 属性 `zephyr,secure-storage-its-partition` 指向一个专供 ITS 使用的固定存储分区。与基于设置子系统（Settings）的实现相比，它在运行时间和存储空间上的开销更低；若同时禁用设置子系统，还可降低 ROM 占用。由于直接将 PSA 存储唯一标识符（UID）映射为 ZMS 表项 ID，它将 UID 值限制在低 30 位范围内。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED && n && (n || n) && CONFIG_ZMS && <choice CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION>
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig.its_store:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig.its_store#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 内部可信存储（ITS）存储模块（Store module） → 内部可信存储（ITS）存储模块的实现

**配置项引用（Symbol References）**：[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_ZMS`](P350_subsys_kvss_配置项参考.md#CONFIG_ZMS)、[`CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION)。

<a id="CONFIG_SECURE_STORAGE_ITS_STORE_MODULE"></a>

## 421.13 `CONFIG_SECURE_STORAGE_ITS_STORE_MODULE`

**提示（Prompt）**：内部可信存储（ITS）存储模块（Store module）

**说明（Help）**

负责在内部可信存储（ITS）数据与非易失性存储器（NVM）之间进行存储和获取的模块，由 Zephyr 的 ITS 实现调用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SECURE_STORAGE
```

**被选择（Selected by）**

```text
CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION_ZEPHYR
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE)、[`CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION_ZEPHYR`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION_ZEPHYR)。

<a id="CONFIG_SECURE_STORAGE_ITS_STORE_SETTINGS_NAME_CUSTOM"></a>

## 421.14 `CONFIG_SECURE_STORAGE_ITS_STORE_SETTINGS_NAME_CUSTOM`

**提示（Prompt）**：已存储设置项的自定义命名规则（Custom naming scheme）

**说明（Help）**

允许为此实现使用的设置项（Settings）指定自定义名称，替代默认命名规则。启用时，需要实现 `<zephyr/secure_storage/its/store/settings.h>` 中声明的 `secure_storage_its_store_settings_get_name()`，并适当设置 `CONFIG_SECURE_STORAGE_ITS_STORE_SETTINGS_NAME_MAX_LEN`。启用此 Kconfig 选项后，该头文件可用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_SETTINGS && CONFIG_SECURE_STORAGE_ITS_STORE_MODULE && CONFIG_SECURE_STORAGE
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig.its_store:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig.its_store#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 内部可信存储（ITS）存储模块（Store module）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_SETTINGS`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_SETTINGS)、[`CONFIG_SECURE_STORAGE_ITS_STORE_MODULE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_STORE_MODULE)、[`CONFIG_SECURE_STORAGE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE)。

<a id="CONFIG_SECURE_STORAGE_ITS_STORE_SETTINGS_NAME_MAX_LEN"></a>

## 421.15 `CONFIG_SECURE_STORAGE_ITS_STORE_SETTINGS_NAME_MAX_LEN`

**提示（Prompt）**：设置名称最大长度（Maximum setting name length）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_SETTINGS && CONFIG_SECURE_STORAGE_ITS_STORE_MODULE && CONFIG_SECURE_STORAGE
```

**默认值（Defaults）**

```text
0 if CONFIG_SECURE_STORAGE_ITS_STORE_SETTINGS_NAME_CUSTOM
22 if CONFIG_SECURE_STORAGE_64_BIT_UID
14
```

**取值范围（Ranges）**

```text
[2, 64]
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig.its_store:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig.its_store#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 内部可信存储（ITS）存储模块（Store module）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_SETTINGS`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_SETTINGS)、[`CONFIG_SECURE_STORAGE_ITS_STORE_MODULE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_STORE_MODULE)、[`CONFIG_SECURE_STORAGE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE)、[`CONFIG_SECURE_STORAGE_ITS_STORE_SETTINGS_NAME_CUSTOM`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_STORE_SETTINGS_NAME_CUSTOM)、[`CONFIG_SECURE_STORAGE_64_BIT_UID`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_64_BIT_UID)。

<a id="CONFIG_SECURE_STORAGE_ITS_STORE_SETTINGS_PREFIX"></a>

## 421.16 `CONFIG_SECURE_STORAGE_ITS_STORE_SETTINGS_PREFIX`

**提示（Prompt）**：保存设置项（Settings）的子树（Subtree），末尾带斜杠，可为空。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
!CONFIG_SECURE_STORAGE_ITS_STORE_SETTINGS_NAME_CUSTOM && CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_SETTINGS && CONFIG_SECURE_STORAGE_ITS_STORE_MODULE && CONFIG_SECURE_STORAGE
```

**默认值（Defaults）**

```text
"its/"
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig.its_store:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig.its_store#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 内部可信存储（ITS）存储模块（Store module）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_ITS_STORE_SETTINGS_NAME_CUSTOM`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_STORE_SETTINGS_NAME_CUSTOM)、[`CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_SETTINGS`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_SETTINGS)、[`CONFIG_SECURE_STORAGE_ITS_STORE_MODULE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_STORE_MODULE)、[`CONFIG_SECURE_STORAGE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE)。

<a id="CONFIG_SECURE_STORAGE_ITS_STORE_ZMS_SECTOR_SIZE"></a>

## 421.17 `CONFIG_SECURE_STORAGE_ITS_STORE_ZMS_SECTOR_SIZE`

**提示（Prompt）**：ZMS 分区的扇区大小（Sector size）

**说明（Help）**

扇区大小（Sector size）影响 ZMS 的运行时行为，并限制 ITS 表项的最大数据大小，即扇区大小减去 ZMS 和 ITS 的额外开销。修改此值会导致分区中已存储数据丢失。对于需要擦除的设备，该值必须为闪存页大小（Flash page size）的整数倍。更多信息参见 ZMS 文档。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_ZMS && CONFIG_SECURE_STORAGE_ITS_STORE_MODULE && CONFIG_SECURE_STORAGE
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig.its_store:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig.its_store#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 内部可信存储（ITS）存储模块（Store module）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_ZMS`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_ZMS)、[`CONFIG_SECURE_STORAGE_ITS_STORE_MODULE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_STORE_MODULE)、[`CONFIG_SECURE_STORAGE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE)。

<a id="CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_CRYPT_CUSTOM"></a>

## 421.18 `CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_CRYPT_CUSTOM`

**提示（Prompt）**：自定义带关联数据的认证加密（AEAD）加解密函数

**说明（Help）**

实现 `<zephyr/secure_storage/its/transform/aead.h>` 中声明的 `secure_storage_its_transform_aead_crypt()`；启用此 Kconfig 选项后，该头文件可用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD && CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE && CONFIG_SECURE_STORAGE
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig.its_transform:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig.its_transform#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 内部可信存储（ITS）转换模块（Transform module）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE)、[`CONFIG_SECURE_STORAGE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE)。

<a id="CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER"></a>

## 421.19 `CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER`

**提示（Prompt）**：AEAD ITS 转换模块的加密密钥提供程序（Encryption key provider）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_CRYPT_CUSTOM && CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD && CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE && CONFIG_SECURE_STORAGE
```

**默认值（Defaults）**

```text
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_DEVICE_ID_HASH if CONFIG_HWINFO_HAS_DRIVER
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_ENTRY_UID_HASH if !CONFIG_HWINFO_HAS_DRIVER
```

**可选项（Choices）**

```text
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_DEVICE_ID_HASH
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_ENTRY_UID_HASH
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_CUSTOM
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig.its_transform:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig.its_transform#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 内部可信存储（ITS）转换模块（Transform module）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_CRYPT_CUSTOM`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_CRYPT_CUSTOM)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE)、[`CONFIG_SECURE_STORAGE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_DEVICE_ID_HASH`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_DEVICE_ID_HASH)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_ENTRY_UID_HASH`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_ENTRY_UID_HASH)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_CUSTOM`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_CUSTOM)。

<a id="CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_CUSTOM"></a>

## 421.20 `CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_CUSTOM`

**提示（Prompt）**：自定义密钥提供程序（Custom key provider）

**说明（Help）**

实现 `<zephyr/secure_storage/its/transform/aead.h>` 中声明的 `secure_storage_its_transform_aead_get_key()`；启用此 Kconfig 选项后，该头文件可用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER>
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig.its_transform:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig.its_transform#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 内部可信存储（ITS）转换模块（Transform module） → AEAD ITS 转换模块的加密密钥提供程序（Encryption key provider）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER)。

<a id="CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_DEVICE_ID_HASH"></a>

## 421.21 `CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_DEVICE_ID_HASH`

**提示（Prompt）**：对硬件信息 API 返回的设备 ID 求哈希（Hash），不一定安全

**说明（Help）**

此密钥提供程序（Key provider）通过对以下数据求哈希（Hash）来生成密钥：

- 首选 `hwinfo_get_device_eui64()` 返回的设备 EUI-64。
- 次选 `hwinfo_get_device_uuid()` 返回的设备 ID。

除设备 ID 外，还将需要生成密钥的 ITS 表项唯一标识符（UID）作为盐值（Salt）加入哈希输入。这不一定安全：取决于设备，设备 ID 可能容易被攻击者读取、不具备唯一性，或能够被猜出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HWINFO_HAS_DRIVER && <choice CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER>
```

**主动选择（Selects）**

```text
CONFIG_PSA_WANT_ALG_SHA_256
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig.its_transform:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig.its_transform#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 内部可信存储（ITS）转换模块（Transform module） → AEAD ITS 转换模块的加密密钥提供程序（Encryption key provider）

**配置项引用（Symbol References）**：[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER)、[`CONFIG_PSA_WANT_ALG_SHA_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_256)。

<a id="CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_ENTRY_UID_HASH"></a>

## 421.22 `CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_ENTRY_UID_HASH`

**提示（Prompt）**：对 ITS 表项唯一标识符（UID）求哈希，不安全（Not secure）

**说明（Help）**

此密钥提供程序（Key provider）通过对 ITS 表项的唯一标识符（UID）求哈希（Hash）来生成该表项的密钥。这不安全，仅用于提供功能性支持，因为 UID 容易猜测，甚至由存储模块以明文保存。应尽可能使用安全的密钥提供程序。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER>
```

**主动选择（Selects）**

```text
CONFIG_NOT_SECURE
CONFIG_PSA_WANT_ALG_SHA_256
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig.its_transform:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig.its_transform#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 内部可信存储（ITS）转换模块（Transform module） → AEAD ITS 转换模块的加密密钥提供程序（Encryption key provider）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER)、[`CONFIG_NOT_SECURE`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_NOT_SECURE)、[`CONFIG_PSA_WANT_ALG_SHA_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_256)。

<a id="CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_SIZE"></a>

## 421.23 `CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_SIZE`

**提示（Prompt）**：AEAD ITS 转换模块的加密密钥大小（Encryption key size，字节）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_SIZE_IS_CONFIGURABLE && CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD && CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE && CONFIG_SECURE_STORAGE
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig.its_transform:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig.its_transform#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 内部可信存储（ITS）转换模块（Transform module）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_SIZE_IS_CONFIGURABLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_SIZE_IS_CONFIGURABLE)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE)、[`CONFIG_SECURE_STORAGE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_SIZE_IS_CONFIGURABLE`。

<a id="CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_PROVIDER"></a>

## 421.24 `CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_PROVIDER`

**提示（Prompt）**：AEAD ITS 转换模块的一次性数提供程序（Nonce provider）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD && CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE && CONFIG_SECURE_STORAGE
```

**可选项（Choices）**

```text
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_PROVIDER_DEFAULT
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_PROVIDER_CUSTOM
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig.its_transform:132`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig.its_transform#L132)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 内部可信存储（ITS）转换模块（Transform module）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE)、[`CONFIG_SECURE_STORAGE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_PROVIDER_DEFAULT`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_PROVIDER_DEFAULT)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_PROVIDER_CUSTOM`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_PROVIDER_CUSTOM)。

<a id="CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_PROVIDER_CUSTOM"></a>

## 421.25 `CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_PROVIDER_CUSTOM`

**提示（Prompt）**：自定义一次性数提供程序（Custom nonce provider）

**说明（Help）**

实现 `<zephyr/secure_storage/its/transform/aead.h>` 中声明的 `secure_storage_its_transform_aead_get_nonce()`；启用此 Kconfig 选项后，该头文件可用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_PROVIDER>
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig.its_transform:142`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig.its_transform#L142)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 内部可信存储（ITS）转换模块（Transform module） → AEAD ITS 转换模块的一次性数提供程序（Nonce provider）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_PROVIDER`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_PROVIDER)。

<a id="CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_PROVIDER_DEFAULT"></a>

## 421.26 `CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_PROVIDER_DEFAULT`

**提示（Prompt）**：默认一次性数提供程序（Default nonce provider）

**说明（Help）**

默认一次性数提供程序（Nonce provider）先使用 `psa_generate_random()` 为第一个 nonce 生成随机数，此后每次递增生成下一个 nonce。要保证此方式安全，随机数源必须确保设备重启之间不会重复取值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_PROVIDER>
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig.its_transform:135`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig.its_transform#L135)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 内部可信存储（ITS）转换模块（Transform module） → AEAD ITS 转换模块的一次性数提供程序（Nonce provider）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_PROVIDER`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_PROVIDER)。

<a id="CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_SIZE"></a>

## 421.27 `CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_SIZE`

**提示（Prompt）**：AEAD ITS 转换模块的一次性数大小（Nonce size，字节）

**说明（Help）**

修改本选项的值时，必须相应调整 `CONFIG_SECURE_STORAGE_ITS_TRANSFORM_OUTPUT_OVERHEAD`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD && CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE && CONFIG_SECURE_STORAGE
```

**默认值（Defaults）**

```text
12
```

**取值范围（Ranges）**

```text
[4, 24]
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig.its_transform:151`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig.its_transform#L151)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 内部可信存储（ITS）转换模块（Transform module）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE)、[`CONFIG_SECURE_STORAGE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE)。

<a id="CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NO_INSECURE_KEY_WARNING"></a>

## 421.28 `CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NO_INSECURE_KEY_WARNING`

**提示（Prompt）**：屏蔽不安全 ITS 加密密钥的警告（Insecure key warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_DEVICE_ID_HASH || CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_ENTRY_UID_HASH) && CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD && CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE && CONFIG_SECURE_STORAGE
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig.its_transform:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig.its_transform#L127)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 内部可信存储（ITS）转换模块（Transform module）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_DEVICE_ID_HASH`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_DEVICE_ID_HASH)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_ENTRY_UID_HASH`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_ENTRY_UID_HASH)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE)、[`CONFIG_SECURE_STORAGE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE)。

<a id="CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME"></a>

## 421.29 `CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME`

**提示（Prompt）**：AEAD ITS 转换模块的算法方案（Scheme）

**说明（Help）**

用于加密和认证数据的带关联数据的认证加密（AEAD）方案。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_IS_CONFIGURABLE && CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD && CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE && CONFIG_SECURE_STORAGE
```

**默认值（Defaults）**

```text
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_AES_GCM
```

**可选项（Choices）**

```text
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_AES_GCM
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_CHACHA20_POLY1305
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_CUSTOM
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig.its_transform:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig.its_transform#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 内部可信存储（ITS）转换模块（Transform module）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_IS_CONFIGURABLE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_IS_CONFIGURABLE)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE)、[`CONFIG_SECURE_STORAGE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_AES_GCM`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_AES_GCM)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_CHACHA20_POLY1305`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_CHACHA20_POLY1305)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_CUSTOM`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_CUSTOM)。

<a id="CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_AES_GCM"></a>

## 421.30 `CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_AES_GCM`

**提示（Prompt）**：AES-GCM 认证加密（AEAD）方案

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME>
```

**主动选择（Selects）**

```text
CONFIG_PSA_WANT_KEY_TYPE_AES
CONFIG_PSA_WANT_ALG_GCM
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig.its_transform:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig.its_transform#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 内部可信存储（ITS）转换模块（Transform module） → AEAD ITS 转换模块的算法方案（Scheme）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME)、[`CONFIG_PSA_WANT_KEY_TYPE_AES`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_AES)、[`CONFIG_PSA_WANT_ALG_GCM`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_GCM)。

<a id="CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_CHACHA20_POLY1305"></a>

## 421.31 `CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_CHACHA20_POLY1305`

**提示（Prompt）**：ChaCha20-Poly1305 认证加密（AEAD）方案

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_SIZE = 12 && <choice CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME>
```

**主动选择（Selects）**

```text
CONFIG_PSA_WANT_KEY_TYPE_CHACHA20
CONFIG_PSA_WANT_ALG_CHACHA20_POLY1305
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig.its_transform:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig.its_transform#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 内部可信存储（ITS）转换模块（Transform module） → AEAD ITS 转换模块的算法方案（Scheme）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_SIZE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_SIZE)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME)、[`CONFIG_PSA_WANT_KEY_TYPE_CHACHA20`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_CHACHA20)、[`CONFIG_PSA_WANT_ALG_CHACHA20_POLY1305`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_CHACHA20_POLY1305)。

<a id="CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_CUSTOM"></a>

## 421.32 `CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_CUSTOM`

**提示（Prompt）**：自定义认证加密（AEAD）方案

**说明（Help）**

实现 `<zephyr/secure_storage/its/transform/aead.h>` 中声明的 `secure_storage_its_transform_aead_get_scheme()`，并适当设置 `CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_SIZE`。启用此 Kconfig 选项后，该头文件可用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME>
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig.its_transform:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig.its_transform#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 内部可信存储（ITS）转换模块（Transform module） → AEAD ITS 转换模块的算法方案（Scheme）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME)。

<a id="CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_IS_CONFIGURABLE"></a>

## 421.33 `CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_IS_CONFIGURABLE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表明 `secure_storage_its_transform_aead_crypt()` 实现是否从 `secure_storage_its_transform_aead_get_scheme()` 获取 AEAD 方案（Scheme）；该方案由 `CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME` 选择项配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD && CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE && CONFIG_SECURE_STORAGE
```

**默认值（Defaults）**

```text
y if !CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_CRYPT_CUSTOM
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig.its_transform:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig.its_transform#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 内部可信存储（ITS）转换模块（Transform module）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE)、[`CONFIG_SECURE_STORAGE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_CRYPT_CUSTOM`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_CRYPT_CUSTOM)。

<a id="CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION"></a>

## 421.34 `CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION`

**提示（Prompt）**：内部可信存储（ITS）转换模块（Transform module）的实现

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE && CONFIG_SECURE_STORAGE
```

**可选项（Choices）**

```text
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_CUSTOM
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig.its_transform:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig.its_transform#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 内部可信存储（ITS）转换模块（Transform module）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE)、[`CONFIG_SECURE_STORAGE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_CUSTOM`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_CUSTOM)。

<a id="CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD"></a>

## 421.35 `CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD`

**提示（Prompt）**：使用带关联数据的认证加密（AEAD）保护数据的 ITS 转换模块实现

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION>
```

**主动选择（Selects）**

```text
CONFIG_PSA_CRYPTO
```

**弱选择（Implies）**

```text
CONFIG_HWINFO
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig.its_transform:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig.its_transform#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 内部可信存储（ITS）转换模块（Transform module） → 内部可信存储（ITS）转换模块（Transform module）的实现

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION)、[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)。

<a id="CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_CUSTOM"></a>

## 421.36 `CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_CUSTOM`

**提示（Prompt）**：自定义 ITS 转换模块（Transform module）实现

**说明（Help）**

实现 `<zephyr/secure_storage/its/transform.h>` 中声明的函数，并适当设置 `CONFIG_SECURE_STORAGE_ITS_TRANSFORM_OUTPUT_OVERHEAD`。启用此 Kconfig 选项后，该头文件可用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION>
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig.its_transform:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig.its_transform#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 内部可信存储（ITS）转换模块（Transform module） → 内部可信存储（ITS）转换模块（Transform module）的实现

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION)。

<a id="CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE"></a>

## 421.37 `CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE`

**提示（Prompt）**：内部可信存储（ITS）转换模块（Transform module）

**说明（Help）**

负责在 ITS 数据写入非易失性存储器（NVM）前，以及从 NVM 读出后，进行转换（Transformation）和校验（Validation）的模块，由 Zephyr 的 ITS 实现调用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SECURE_STORAGE
```

**被选择（Selected by）**

```text
CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION_ZEPHYR
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE)、[`CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION_ZEPHYR`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION_ZEPHYR)。

<a id="CONFIG_SECURE_STORAGE_ITS_TRANSFORM_OUTPUT_OVERHEAD"></a>

## 421.38 `CONFIG_SECURE_STORAGE_ITS_TRANSFORM_OUTPUT_OVERHEAD`

**提示（Prompt）**：为存储而转换表项数据所需的额外开销（Overhead，字节）

**说明（Help）**

表示 ITS 表项数据经 `secure_storage_its_transform_to_store()` 处理后，大小会增加多少字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE && CONFIG_SECURE_STORAGE
```

**默认值（Defaults）**

```text
28 if CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD && CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_SIZE = 12
-1
```

**取值范围（Ranges）**

```text
[0, 1000]
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig.its_transform:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig.its_transform#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 内部可信存储（ITS）转换模块（Transform module）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE)、[`CONFIG_SECURE_STORAGE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_SIZE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_SIZE)。

<a id="CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION"></a>

## 421.39 `CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION`

**提示（Prompt）**：受保护存储（Protected Storage，PS）API 实现

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SECURE_STORAGE
```

**默认值（Defaults）**

```text
CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION_ITS
```

**可选项（Choices）**

```text
CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION_ITS
CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION_CUSTOM
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE)、[`CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION_ITS`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION_ITS)、[`CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION_CUSTOM`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION_CUSTOM)。

<a id="CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION_CUSTOM"></a>

## 421.40 `CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION_CUSTOM`

**提示（Prompt）**：自定义受保护存储（PS）实现

**说明（Help）**

使用自定义的受保护存储（PS）API 实现。需要实现 `<zephyr/secure_storage/ps.h>` 中声明的函数；启用此 Kconfig 选项后，该头文件可用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION>
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 受保护存储（Protected Storage，PS）API 实现

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION)。

<a id="CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION_ITS"></a>

## 421.41 `CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION_ITS`

**提示（Prompt）**：受保护存储（PS）直接调用内部可信存储（ITS）

**说明（Help）**

受保护存储（PS）API 没有独立实现，直接调用内部可信存储（ITS）API，因此 PS API 的实现与 ITS API 相同。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION>
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 受保护存储（Protected Storage，PS）API 实现

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION)。

<a id="CONFIG_SECURE_STORAGE_PS_SUPPORTS_SET_EXTENDED"></a>

## 421.42 `CONFIG_SECURE_STORAGE_PS_SUPPORTS_SET_EXTENDED`

**提示（Prompt）**：PS API 实现支持 `psa_ps_create()` 和 `psa_ps_set_extended()`

**说明（Help）**

指定是否实现 `psa_ps_create()` 和 `psa_ps_set_extended()` 函数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION_CUSTOM && CONFIG_SECURE_STORAGE
```

**定义位置（Location）**：[`subsys/secure_storage/Kconfig:120`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/Kconfig#L120)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION_CUSTOM`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION_CUSTOM)、[`CONFIG_SECURE_STORAGE`](P421_subsys_secure_storage_配置项参考.md#CONFIG_SECURE_STORAGE)。

<!-- kconfig-navigation -->

[上一章](P420_subsys_sd_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P422_subsys_sensing_配置项参考.md)
