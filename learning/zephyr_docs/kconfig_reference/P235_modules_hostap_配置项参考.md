---
id: learning.zephyr-docs.kconfig-reference.page-235
title: "`modules/hostap`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第235章\_`modules/hostap`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/hostap` 的 90 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_EAP_AKA"></a>

## 235.1 `CONFIG_EAP_AKA`

**提示（Prompt）**：EAP-AKA 认证支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**定义位置（Location）**：[`modules/hostap/Kconfig:354`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L354)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → Wi-Fi 企业级密码功能支持（Enterprise Crypto support）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_EAP_ALL"></a>

## 235.2 `CONFIG_EAP_ALL`

**提示（Prompt）**：支持所有可扩展认证协议方法（EAP methods）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_EAP_TLS
CONFIG_EAP_PEAP
CONFIG_EAP_GTC
CONFIG_EAP_TTLS
CONFIG_EAP_MSCHAPV2
```

**定义位置（Location）**：[`modules/hostap/Kconfig:360`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L360)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → Wi-Fi 企业级密码功能支持（Enterprise Crypto support）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_EAP_TLS`](P235_modules_hostap_配置项参考.md#CONFIG_EAP_TLS)、[`CONFIG_EAP_PEAP`](P235_modules_hostap_配置项参考.md#CONFIG_EAP_PEAP)、[`CONFIG_EAP_GTC`](P235_modules_hostap_配置项参考.md#CONFIG_EAP_GTC)、[`CONFIG_EAP_TTLS`](P235_modules_hostap_配置项参考.md#CONFIG_EAP_TTLS)、[`CONFIG_EAP_MSCHAPV2`](P235_modules_hostap_配置项参考.md#CONFIG_EAP_MSCHAPV2)。

<a id="CONFIG_EAP_EKE"></a>

## 235.3 `CONFIG_EAP_EKE`

**提示（Prompt）**：EAP-EKE 认证支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**定义位置（Location）**：[`modules/hostap/Kconfig:345`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L345)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → Wi-Fi 企业级密码功能支持（Enterprise Crypto support）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_EAP_FAST"></a>

## 235.4 `CONFIG_EAP_FAST`

**提示（Prompt）**：EAP-FAST 认证支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**定义位置（Location）**：[`modules/hostap/Kconfig:357`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L357)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → Wi-Fi 企业级密码功能支持（Enterprise Crypto support）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_EAP_GPSK"></a>

## 235.5 `CONFIG_EAP_GPSK`

**提示（Prompt）**：EAP-GPSK 认证支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**定义位置（Location）**：[`modules/hostap/Kconfig:339`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L339)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → Wi-Fi 企业级密码功能支持（Enterprise Crypto support）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_EAP_GTC"></a>

## 235.6 `CONFIG_EAP_GTC`

**提示（Prompt）**：EAP-GTC 认证支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**被选择（Selected by）**

```text
CONFIG_EAP_ALL
CONFIG_EAP_ALL
CONFIG_EAP_ALL
```

**定义位置（Location）**：[`modules/hostap/Kconfig:324`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L324)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → Wi-Fi 企业级密码功能支持（Enterprise Crypto support）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_EAP_ALL`](P235_modules_hostap_配置项参考.md#CONFIG_EAP_ALL)。

<a id="CONFIG_EAP_IKEV2"></a>

## 235.7 `CONFIG_EAP_IKEV2`

**提示（Prompt）**：EAP-IKEv2 认证支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**定义位置（Location）**：[`modules/hostap/Kconfig:348`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L348)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → Wi-Fi 企业级密码功能支持（Enterprise Crypto support）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_EAP_MSCHAPV2"></a>

## 235.8 `CONFIG_EAP_MSCHAPV2`

**提示（Prompt）**：EAP-MSCHAPv2 认证支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**被选择（Selected by）**

```text
CONFIG_EAP_ALL
CONFIG_EAP_ALL
CONFIG_EAP_ALL
```

**定义位置（Location）**：[`modules/hostap/Kconfig:327`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L327)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → Wi-Fi 企业级密码功能支持（Enterprise Crypto support）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_EAP_ALL`](P235_modules_hostap_配置项参考.md#CONFIG_EAP_ALL)。

<a id="CONFIG_EAP_PAX"></a>

## 235.9 `CONFIG_EAP_PAX`

**提示（Prompt）**：EAP-PAX 认证支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**定义位置（Location）**：[`modules/hostap/Kconfig:333`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L333)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → Wi-Fi 企业级密码功能支持（Enterprise Crypto support）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_EAP_PEAP"></a>

## 235.10 `CONFIG_EAP_PEAP`

**提示（Prompt）**：EAP-PEAP 认证支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**被选择（Selected by）**

```text
CONFIG_EAP_ALL
CONFIG_EAP_ALL
CONFIG_EAP_ALL
```

**定义位置（Location）**：[`modules/hostap/Kconfig:321`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L321)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → Wi-Fi 企业级密码功能支持（Enterprise Crypto support）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_EAP_ALL`](P235_modules_hostap_配置项参考.md#CONFIG_EAP_ALL)。

<a id="CONFIG_EAP_PSK"></a>

## 235.11 `CONFIG_EAP_PSK`

**提示（Prompt）**：EAP-PSK 认证支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**定义位置（Location）**：[`modules/hostap/Kconfig:330`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L330)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → Wi-Fi 企业级密码功能支持（Enterprise Crypto support）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_EAP_PWD"></a>

## 235.12 `CONFIG_EAP_PWD`

**提示（Prompt）**：EAP-PWD 认证支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**定义位置（Location）**：[`modules/hostap/Kconfig:342`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L342)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → Wi-Fi 企业级密码功能支持（Enterprise Crypto support）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_EAP_SAKE"></a>

## 235.13 `CONFIG_EAP_SAKE`

**提示（Prompt）**：EAP-SAKE 认证支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**定义位置（Location）**：[`modules/hostap/Kconfig:336`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L336)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → Wi-Fi 企业级密码功能支持（Enterprise Crypto support）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_EAP_SERVER_ALL"></a>

## 235.14 `CONFIG_EAP_SERVER_ALL`

**提示（Prompt）**：支持所有可扩展认证协议方法（EAP methods）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_HOSTAPD_CRYPTO_ENTERPRISE && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_EAP_SERVER_TLS
CONFIG_EAP_SERVER_MSCHAPV2
CONFIG_EAP_SERVER_PEAP
CONFIG_EAP_SERVER_GTC
CONFIG_EAP_SERVER_TTLS
```

**定义位置（Location）**：[`modules/hostap/Kconfig:500`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L500)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → 基于 Hostapd 的完整接入点模式（FullAP mode）支持 → Hostapd 企业级密码功能支持（crypto enterprise support）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_HOSTAPD_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_HOSTAPD_CRYPTO_ENTERPRISE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_EAP_SERVER_TLS`](P235_modules_hostap_配置项参考.md#CONFIG_EAP_SERVER_TLS)、[`CONFIG_EAP_SERVER_MSCHAPV2`](P235_modules_hostap_配置项参考.md#CONFIG_EAP_SERVER_MSCHAPV2)、[`CONFIG_EAP_SERVER_PEAP`](P235_modules_hostap_配置项参考.md#CONFIG_EAP_SERVER_PEAP)、[`CONFIG_EAP_SERVER_GTC`](P235_modules_hostap_配置项参考.md#CONFIG_EAP_SERVER_GTC)、[`CONFIG_EAP_SERVER_TTLS`](P235_modules_hostap_配置项参考.md#CONFIG_EAP_SERVER_TTLS)。

<a id="CONFIG_EAP_SERVER_GTC"></a>

## 235.15 `CONFIG_EAP_SERVER_GTC`

**提示（Prompt）**：EAP-GTC 认证服务器支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_HOSTAPD_CRYPTO_ENTERPRISE && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**被选择（Selected by）**

```text
CONFIG_EAP_SERVER_ALL
CONFIG_EAP_SERVER_ALL
CONFIG_EAP_SERVER_ALL
```

**定义位置（Location）**：[`modules/hostap/Kconfig:494`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L494)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → 基于 Hostapd 的完整接入点模式（FullAP mode）支持 → Hostapd 企业级密码功能支持（crypto enterprise support）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_HOSTAPD_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_HOSTAPD_CRYPTO_ENTERPRISE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_EAP_SERVER_ALL`](P235_modules_hostap_配置项参考.md#CONFIG_EAP_SERVER_ALL)。

<a id="CONFIG_EAP_SERVER_IDENTITY"></a>

## 235.16 `CONFIG_EAP_SERVER_IDENTITY`

**提示（Prompt）**：EAP-IDENTITY 认证服务器支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_HOSTAPD_CRYPTO_ENTERPRISE && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**定义位置（Location）**：[`modules/hostap/Kconfig:485`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L485)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → 基于 Hostapd 的完整接入点模式（FullAP mode）支持 → Hostapd 企业级密码功能支持（crypto enterprise support）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_HOSTAPD_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_HOSTAPD_CRYPTO_ENTERPRISE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_EAP_SERVER_MSCHAPV2"></a>

## 235.17 `CONFIG_EAP_SERVER_MSCHAPV2`

**提示（Prompt）**：EAP-MSCHAPV2 认证服务器支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_HOSTAPD_CRYPTO_ENTERPRISE && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**被选择（Selected by）**

```text
CONFIG_EAP_SERVER_ALL
CONFIG_EAP_SERVER_ALL
CONFIG_EAP_SERVER_ALL
```

**定义位置（Location）**：[`modules/hostap/Kconfig:488`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L488)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → 基于 Hostapd 的完整接入点模式（FullAP mode）支持 → Hostapd 企业级密码功能支持（crypto enterprise support）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_HOSTAPD_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_HOSTAPD_CRYPTO_ENTERPRISE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_EAP_SERVER_ALL`](P235_modules_hostap_配置项参考.md#CONFIG_EAP_SERVER_ALL)。

<a id="CONFIG_EAP_SERVER_PEAP"></a>

## 235.18 `CONFIG_EAP_SERVER_PEAP`

**提示（Prompt）**：EAP-PEAP 认证服务器支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_HOSTAPD_CRYPTO_ENTERPRISE && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**被选择（Selected by）**

```text
CONFIG_EAP_SERVER_ALL
CONFIG_EAP_SERVER_ALL
CONFIG_EAP_SERVER_ALL
```

**定义位置（Location）**：[`modules/hostap/Kconfig:491`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L491)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → 基于 Hostapd 的完整接入点模式（FullAP mode）支持 → Hostapd 企业级密码功能支持（crypto enterprise support）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_HOSTAPD_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_HOSTAPD_CRYPTO_ENTERPRISE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_EAP_SERVER_ALL`](P235_modules_hostap_配置项参考.md#CONFIG_EAP_SERVER_ALL)。

<a id="CONFIG_EAP_SERVER_TLS"></a>

## 235.19 `CONFIG_EAP_SERVER_TLS`

**提示（Prompt）**：EAP-TLS 认证服务器支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_HOSTAPD_CRYPTO_ENTERPRISE && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**被选择（Selected by）**

```text
CONFIG_EAP_SERVER_ALL
CONFIG_EAP_SERVER_ALL
CONFIG_EAP_SERVER_ALL
```

**定义位置（Location）**：[`modules/hostap/Kconfig:482`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L482)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → 基于 Hostapd 的完整接入点模式（FullAP mode）支持 → Hostapd 企业级密码功能支持（crypto enterprise support）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_HOSTAPD_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_HOSTAPD_CRYPTO_ENTERPRISE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_EAP_SERVER_ALL`](P235_modules_hostap_配置项参考.md#CONFIG_EAP_SERVER_ALL)。

<a id="CONFIG_EAP_SERVER_TTLS"></a>

## 235.20 `CONFIG_EAP_SERVER_TTLS`

**提示（Prompt）**：EAP-TTLS 认证服务器支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_HOSTAPD_CRYPTO_ENTERPRISE && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**被选择（Selected by）**

```text
CONFIG_EAP_SERVER_ALL
CONFIG_EAP_SERVER_ALL
CONFIG_EAP_SERVER_ALL
```

**定义位置（Location）**：[`modules/hostap/Kconfig:497`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L497)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → 基于 Hostapd 的完整接入点模式（FullAP mode）支持 → Hostapd 企业级密码功能支持（crypto enterprise support）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_HOSTAPD_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_HOSTAPD_CRYPTO_ENTERPRISE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_EAP_SERVER_ALL`](P235_modules_hostap_配置项参考.md#CONFIG_EAP_SERVER_ALL)。

<a id="CONFIG_EAP_SIM"></a>

## 235.21 `CONFIG_EAP_SIM`

**提示（Prompt）**：EAP-SIM 认证支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**定义位置（Location）**：[`modules/hostap/Kconfig:351`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L351)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → Wi-Fi 企业级密码功能支持（Enterprise Crypto support）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_EAP_TLS"></a>

## 235.22 `CONFIG_EAP_TLS`

**提示（Prompt）**：EAP-TLS 认证支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**被选择（Selected by）**

```text
CONFIG_EAP_ALL
CONFIG_EAP_ALL
CONFIG_EAP_ALL
```

**定义位置（Location）**：[`modules/hostap/Kconfig:315`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L315)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → Wi-Fi 企业级密码功能支持（Enterprise Crypto support）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_EAP_ALL`](P235_modules_hostap_配置项参考.md#CONFIG_EAP_ALL)。

<a id="CONFIG_EAP_TLSV1_3"></a>

## 235.23 `CONFIG_EAP_TLSV1_3`

**提示（Prompt）**：可扩展认证协议（EAP）的 TLSv1.3 支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_X509_CRT_PARSE_C
CONFIG_MBEDTLS_X509_RSASSA_PSS_SUPPORT
CONFIG_MBEDTLS_SSL_PROTO_TLS1_3
CONFIG_MBEDTLS_SSL_SESSION_TICKETS
CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_PSK_ENABLED
CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED
CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_PSK_EPHEMERAL_ENABLED
CONFIG_PSA_WANT_ALG_GCM
CONFIG_PSA_WANT_ALG_RSA_OAEP
```

**定义位置（Location）**：[`modules/hostap/Kconfig:369`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L369)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → Wi-Fi 企业级密码功能支持（Enterprise Crypto support）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_MBEDTLS_X509_CRT_PARSE_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_X509_CRT_PARSE_C)、[`CONFIG_MBEDTLS_X509_RSASSA_PSS_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_X509_RSASSA_PSS_SUPPORT)、[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_SSL_PROTO_TLS1_3)、[`CONFIG_MBEDTLS_SSL_SESSION_TICKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_SSL_SESSION_TICKETS)、[`CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_PSK_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_PSK_ENABLED)、[`CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_EPHEMERAL_ENABLED)、[`CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_PSK_EPHEMERAL_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_PSK_EPHEMERAL_ENABLED)、[`CONFIG_PSA_WANT_ALG_GCM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_GCM)、[`CONFIG_PSA_WANT_ALG_RSA_OAEP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_RSA_OAEP)。

<a id="CONFIG_EAP_TTLS"></a>

## 235.24 `CONFIG_EAP_TTLS`

**提示（Prompt）**：EAP-TTLS 认证支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**被选择（Selected by）**

```text
CONFIG_EAP_ALL
CONFIG_EAP_ALL
CONFIG_EAP_ALL
```

**定义位置（Location）**：[`modules/hostap/Kconfig:318`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L318)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → Wi-Fi 企业级密码功能支持（Enterprise Crypto support）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_EAP_ALL`](P235_modules_hostap_配置项参考.md#CONFIG_EAP_ALL)。

<a id="CONFIG_SAE_PWE_EARLY_EXIT"></a>

## 235.25 `CONFIG_SAE_PWE_EARLY_EXIT`

**提示（Prompt）**：找到密码元素（PWE）后提前退出

**说明（Help）**

为缓解侧信道攻击（side-channel attacks），即使已找到密码元素（PWE），WPA 认证客户端（supplicant）仍执行全部迭代，但这可能给资源较少的系统带来较重负担，因此提供提前退出选项。注意：此方式非常不安全，不应在生产环境使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**定义位置（Location）**：[`modules/hostap/Kconfig:854`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L854)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_WIFI_NAN_MAX_SSI_LEN"></a>

## 235.26 `CONFIG_WIFI_NAN_MAX_SSI_LEN`

**提示（Prompt）**：邻近感知网络（NAN）服务专用信息的最大长度

**说明（Help）**

邻近感知网络（NAN）服务专用信息（Service Specific Info，SSI）载荷的最大长度，单位为字节。此值对应的数据内嵌在 NAN 事件和请求结构体中，因此增大它会使 `net_mgmt` 事件队列占用增加约 `CONFIG_NET_MGMT_EVENT_QUEUE_SIZE` 乘以该值的大小。需要更大 SSI 载荷的用户，例如采用 `MTU=350` 的 Matter PAF 配网（commissioning），应将此值设为所需大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_NAN && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
128
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`modules/hostap/Kconfig:545`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L545)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → 邻近感知网络（Neighbor Awareness Networking，NAN）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_NAN`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_NAN)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_WIFI_NM_HOSTAPD_AP"></a>

## 235.27 `CONFIG_WIFI_NM_HOSTAPD_AP`

**提示（Prompt）**：基于 Hostapd 的完整接入点模式（FullAP mode）支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**被选择（Selected by）**

```text
CONFIG_NXP_WIFI_SOFTAP_SUPPORT
```

**定义位置（Location）**：[`modules/hostap/Kconfig:473`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L473)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_NXP_WIFI_SOFTAP_SUPPORT`](P192_drivers_wifi_配置项参考_5.md#CONFIG_NXP_WIFI_SOFTAP_SUPPORT)。

<a id="CONFIG_WIFI_NM_HOSTAPD_CLEANUP_INTERVAL"></a>

## 235.28 `CONFIG_WIFI_NM_HOSTAPD_CLEANUP_INTERVAL`

**提示（Prompt）**：Hostapd 清理间隔（cleanup interval），单位为秒

**说明（Help）**

Hostapd 清理间隔（cleanup interval）。设备处于低功耗模式时，增大此间隔可避免频繁唤醒，从而节省功耗。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_HOSTAPD_AP && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`modules/hostap/Kconfig:636`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L636)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_HOSTAPD_AP`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_HOSTAPD_AP)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_WIFI_NM_HOSTAPD_CRYPTO_ENTERPRISE"></a>

## 235.29 `CONFIG_WIFI_NM_HOSTAPD_CRYPTO_ENTERPRISE`

**提示（Prompt）**：Hostapd 企业级密码功能支持（crypto enterprise support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_HOSTAPD_AP && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**主动选择（Selects）**

```text
CONFIG_WIFI_CERTIFICATE_LIB
```

**被弱选择（Implied by）**

```text
CONFIG_NXP_WIFI_SOFTAP_SUPPORT
```

**定义位置（Location）**：[`modules/hostap/Kconfig:476`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L476)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → 基于 Hostapd 的完整接入点模式（FullAP mode）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_HOSTAPD_AP`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_HOSTAPD_AP)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_WIFI_CERTIFICATE_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_CERTIFICATE_LIB)、[`CONFIG_NXP_WIFI_SOFTAP_SUPPORT`](P192_drivers_wifi_配置项参考_5.md#CONFIG_NXP_WIFI_SOFTAP_SUPPORT)。

<a id="CONFIG_WIFI_NM_HOSTAPD_REGULATORY_ENV"></a>

## 235.30 `CONFIG_WIFI_NM_HOSTAPD_REGULATORY_ENV`

**提示（Prompt）**：选择 Wi-Fi 监管环境（Regulatory Environment）

**说明（Help）**

国家／地区字符串（Country String，`dot11CountryString`）的第三个八位组（octet）。此参数用于设置该八位组。使用默认值 `0x20`，即十进制 `32`，可使用当前地区支持的所有环境（environments）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_HOSTAPD_AP && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`modules/hostap/Kconfig:884`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L884)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_HOSTAPD_AP`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_HOSTAPD_AP)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_WIFI_NM_HOSTAPD_REGULATORY_REGION"></a>

## 235.31 `CONFIG_WIFI_NM_HOSTAPD_REGULATORY_REGION`

**提示（Prompt）**：选择 Wi-Fi 监管域（Regulatory Domain）

**说明（Help）**

地区／国家代码（Region/Country code，ISO/IEC 3166-1），用于设置监管域（regulatory domain）。根据需要指定设备运行所在国家／地区，这可能限制可用信道和发送功率。此处的两个八位组（octets）用作国家／地区字符串（`dot11CountryString`）的前两个八位组。`00` 表示全球模式（World Wide mode）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_HOSTAPD_AP && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
"00"
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig)。

```text
"WW"
```

来源：[`boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig)。

```text
"US"
```

来源：[`boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig)。

```text
"US"
```

**定义位置（Location）**：[`modules/hostap/Kconfig:873`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L873)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_HOSTAPD_AP`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_HOSTAPD_AP)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_WIFI_NM_HOSTAPD_WPS"></a>

## 235.32 `CONFIG_WIFI_NM_HOSTAPD_WPS`

**提示（Prompt）**：Hostapd 的 Wi-Fi 保护设置（WPS）支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_NONE && CONFIG_WIFI_NM_HOSTAPD_AP && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**被弱选择（Implied by）**

```text
CONFIG_NXP_WIFI_SOFTAP_SUPPORT
```

**定义位置（Location）**：[`modules/hostap/Kconfig:435`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L435)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_NONE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_NONE)、[`CONFIG_WIFI_NM_HOSTAPD_AP`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_HOSTAPD_AP)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_NXP_WIFI_SOFTAP_SUPPORT`](P192_drivers_wifi_配置项参考_5.md#CONFIG_NXP_WIFI_SOFTAP_SUPPORT)。

<a id="CONFIG_WIFI_NM_WPA_CTRL_RESP_TIMEOUT_S"></a>

## 235.33 `CONFIG_WIFI_NM_WPA_CTRL_RESP_TIMEOUT_S`

**提示（Prompt）**：WPA 认证客户端控制接口响应超时（control interface response timeout），单位为秒

**说明（Help）**

控制接口命令（control interface commands）等待认证客户端（supplicant）响应的超时。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
15
```

**定义位置（Location）**：[`modules/hostap/Kconfig:866`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L866)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT"></a>

## 235.34 `CONFIG_WIFI_NM_WPA_SUPPLICANT`

**提示（Prompt）**：来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**说明（Help）**

将 WPA 认证客户端（supplicant）作为 `WIFI_NM` 的网络管理后端（network management backend）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_POSIX_TIMERS
CONFIG_POSIX_SIGNALS
CONFIG_POSIX_API
CONFIG_XSI_SINGLE_PROCESS
CONFIG_NET_SOCKETS
CONFIG_NET_SOCKETS_PACKET
CONFIG_NET_L2_WIFI_MGMT
CONFIG_WIFI_NM
CONFIG_EXPERIMENTAL
CONFIG_COMMON_LIBC_MALLOC
CONFIG_ZVFS
CONFIG_ZVFS_EVENTFD
```

**被选择（Selected by）**

```text
CONFIG_WIFI_BFLB
CONFIG_NRF70_STA_MODE
CONFIG_NRF70_PROMISC_DATA_RX
```

**定义位置（Location）**：[`modules/hostap/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_TIMERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_TIMERS)、[`CONFIG_POSIX_SIGNALS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SIGNALS)、[`CONFIG_POSIX_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_API)、[`CONFIG_XSI_SINGLE_PROCESS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XSI_SINGLE_PROCESS)、[`CONFIG_NET_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS)、[`CONFIG_NET_SOCKETS_PACKET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_PACKET)、[`CONFIG_NET_L2_WIFI_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_WIFI_NM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_COMMON_LIBC_MALLOC`](P197_lib_配置项参考_1.md#CONFIG_COMMON_LIBC_MALLOC)、[`CONFIG_ZVFS`](P199_lib_配置项参考_3.md#CONFIG_ZVFS)、[`CONFIG_ZVFS_EVENTFD`](P199_lib_配置项参考_3.md#CONFIG_ZVFS_EVENTFD)、[`CONFIG_WIFI_BFLB`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB)、[`CONFIG_NRF70_STA_MODE`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_STA_MODE)、[`CONFIG_NRF70_PROMISC_DATA_RX`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_PROMISC_DATA_RX)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_11AC"></a>

## 235.35 `CONFIG_WIFI_NM_WPA_SUPPLICANT_11AC`

**提示（Prompt）**：IEEE 802.11ac 极高吞吐量（VHT）支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_WIFI_NM_WPA_SUPPLICANT_AP || CONFIG_WIFI_NM_HOSTAPD_AP) && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
y
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig)。

```text
n
```

**定义位置（Location）**：[`modules/hostap/Kconfig:558`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L558)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_AP`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_AP)、[`CONFIG_WIFI_NM_HOSTAPD_AP`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_HOSTAPD_AP)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_11AX"></a>

## 235.36 `CONFIG_WIFI_NM_WPA_SUPPLICANT_11AX`

**提示（Prompt）**：IEEE 802.11ax 高效率（HE）支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_WIFI_NM_WPA_SUPPLICANT_AP || CONFIG_WIFI_NM_HOSTAPD_AP) && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
y
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig)。

```text
n
```

**定义位置（Location）**：[`modules/hostap/Kconfig:563`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L563)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_AP`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_AP)、[`CONFIG_WIFI_NM_HOSTAPD_AP`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_HOSTAPD_AP)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_ADVANCED_FEATURES"></a>

## 235.37 `CONFIG_WIFI_NM_WPA_SUPPLICANT_ADVANCED_FEATURES`

**提示（Prompt）**：高级功能（Advanced features）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
y if !CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`modules/hostap/Kconfig:151`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L151)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_AP"></a>

## 235.38 `CONFIG_WIFI_NM_WPA_SUPPLICANT_AP`

**提示（Prompt）**：基于 WPA 认证客户端（supplicant）的软件接入点模式（SoftAP mode）支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
y if CONFIG_WIFI_USAGE_MODE_AP || CONFIG_WIFI_USAGE_MODE_STA_AP
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P
CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P
CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P
CONFIG_WIFI_BFLB_WIFI6
```

**定义位置（Location）**：[`modules/hostap/Kconfig:427`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L427)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_WIFI_USAGE_MODE_AP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_USAGE_MODE_AP)、[`CONFIG_WIFI_USAGE_MODE_STA_AP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_USAGE_MODE_STA_AP)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P)、[`CONFIG_WIFI_BFLB_WIFI6`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB_WIFI6)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_BGSCAN"></a>

## 235.39 `CONFIG_WIFI_NM_WPA_SUPPLICANT_BGSCAN`

**提示（Prompt）**：后台扫描（Background scanning），用于传统漫游；不支持 802.11r 时推荐使用

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_WNM && !CONFIG_WIFI_NM_WPA_SUPPLICANT_ROAMING && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**定义位置（Location）**：[`modules/hostap/Kconfig:608`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L608)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_WNM`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_WNM)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_ROAMING`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_ROAMING)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_BGSCAN_LEARN"></a>

## 235.40 `CONFIG_WIFI_NM_WPA_SUPPLICANT_BGSCAN_LEARN`

**提示（Prompt）**：学习（Learning）

**说明（Help）**

学习网络使用的信道，尝试避免在其他信道上进行后台扫描（background scans）；此功能为实验性（experimental）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_BGSCAN && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**定义位置（Location）**：[`modules/hostap/Kconfig:621`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L621)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → 后台扫描（Background scanning），用于传统漫游；不支持 802.11r 时推荐使用

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_BGSCAN`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_BGSCAN)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_BGSCAN_SIMPLE"></a>

## 235.41 `CONFIG_WIFI_NM_WPA_SUPPLICANT_BGSCAN_SIMPLE`

**提示（Prompt）**：简单后台扫描（Simple background scanning）

**说明（Help）**

根据信号强度（signal strength）定期进行后台扫描。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_BGSCAN && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hostap/Kconfig:615`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L615)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → 后台扫描（Background scanning），用于传统漫游；不支持 802.11r 时推荐使用

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_BGSCAN`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_BGSCAN)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_BSS_MAX_IDLE_TIME"></a>

## 235.42 `CONFIG_WIFI_NM_WPA_SUPPLICANT_BSS_MAX_IDLE_TIME`

**提示（Prompt）**：基本服务集（BSS）最大空闲超时，单位为秒

**说明（Help）**

基本服务集（BSS）最大空闲超时表示某客户端没有流量时，接入点（AP）仍可将其保持为关联状态（associated state）的时长。设为 `0` 时，不在关联请求（association request）中包含 BSS 最大空闲时间标签。非零时，站点（STA）可以通过在关联请求中包含 BSS 最大空闲周期（max idle period）提出期望超时；AP 可以采纳或忽略 STA 的偏好。参见 IEEE Std 802.11™-2020 第 11.21.13 节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
300
```

**取值范围（Ranges）**

```text
[0, 64000]
```

**定义位置（Location）**：[`modules/hostap/Kconfig:511`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L511)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_BTM_PRE_SCAN_CHECK"></a>

## 235.43 `CONFIG_WIFI_NM_WPA_SUPPLICANT_BTM_PRE_SCAN_CHECK`

**提示（Prompt）**：BSS 转换管理（BTM）的预扫描检查（Pre-scan check）

**说明（Help）**

启用 BSS 转换管理（BTM）的预扫描检查。找不到候选项（candidate）时，执行新扫描。如果芯片扫描耗时过长，导致 Wi-Fi Alliance QuickTrack（WFA QT）测试中发生解除关联（disassociations），请禁用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
y if !CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`modules/hostap/Kconfig:894`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L894)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_CLEANUP_INTERVAL"></a>

## 235.44 `CONFIG_WIFI_NM_WPA_SUPPLICANT_CLEANUP_INTERVAL`

**提示（Prompt）**：WPA 认证客户端清理间隔（cleanup interval），单位为秒

**说明（Help）**

WPA 认证客户端（supplicant）的清理间隔。设备处于低功耗模式时，增大间隔可避免频繁唤醒，从而节省功耗。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`modules/hostap/Kconfig:629`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L629)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_CLI"></a>

## 235.45 `CONFIG_WIFI_NM_WPA_SUPPLICANT_CLI`

**提示（Prompt）**：wpa_supplicant 命令行接口（CLI）支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**定义位置（Location）**：[`modules/hostap/Kconfig:470`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L470)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT"></a>

## 235.46 `CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT`

**提示（Prompt）**：Wi-Fi 的 Mbedtls 替代密码实现（crypto alt）支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_BACKEND>
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS
CONFIG_MBEDTLS_CIPHER
CONFIG_MBEDTLS_PKCS5_C
CONFIG_MBEDTLS_MD_C
CONFIG_MBEDTLS_PK_WRITE_C
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
CONFIG_MBEDTLS_NIST_KW_C
CONFIG_MBEDTLS_HAVE_ASM
CONFIG_MBEDTLS_CTR_DRBG_C
CONFIG_PSA_WANT_ALG_HKDF
CONFIG_PSA_WANT_ALG_HKDF_EXTRACT
CONFIG_PSA_WANT_ALG_HKDF_EXPAND
```

**定义位置（Location）**：[`modules/hostap/Kconfig:235`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L235)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → WPA 认证客户端密码实现（supplicant crypto implementation）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_BACKEND`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_BACKEND)、[`CONFIG_MBEDTLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_CIPHER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_CIPHER)、[`CONFIG_MBEDTLS_PKCS5_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PKCS5_C)、[`CONFIG_MBEDTLS_MD_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_MD_C)、[`CONFIG_MBEDTLS_PK_WRITE_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PK_WRITE_C)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256)、[`CONFIG_MBEDTLS_NIST_KW_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_NIST_KW_C)、[`CONFIG_MBEDTLS_HAVE_ASM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_HAVE_ASM)、[`CONFIG_MBEDTLS_CTR_DRBG_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_CTR_DRBG_C)、[`CONFIG_PSA_WANT_ALG_HKDF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_HKDF)、[`CONFIG_PSA_WANT_ALG_HKDF_EXTRACT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_HKDF_EXTRACT)、[`CONFIG_PSA_WANT_ALG_HKDF_EXPAND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_HKDF_EXPAND)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_BACKEND"></a>

## 235.47 `CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_BACKEND`

**提示（Prompt）**：WPA 认证客户端密码实现（supplicant crypto implementation）

**说明（Help）**

选择 WPA 认证客户端（supplicant）使用的密码实现（crypto implementation）。`WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT` 支持企业模式（enterprise mode）和设备配置协议（DPP）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
```

**可选项（Choices）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_NONE
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_EXT
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_NONE
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_EXT
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_NONE
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_EXT
```

**定义位置（Location）**：[`modules/hostap/Kconfig:227`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L227)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_NONE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_NONE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_EXT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_EXT)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE"></a>

## 235.48 `CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`

**提示（Prompt）**：Wi-Fi 企业级密码功能支持（Enterprise Crypto support）

**说明（Help）**

启用 Wi-Fi 企业级密码功能（Enterprise Crypto）支持。由于缺少证书验证（certificate validation），此功能被认为不安全（NOT SECURE）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_NONE && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_PEM_PARSE_C
CONFIG_MBEDTLS_PEM_WRITE_C
CONFIG_MBEDTLS_SSL_SERVER_NAME_INDICATION
CONFIG_MBEDTLS_X509_CRL_PARSE_C
CONFIG_MBEDTLS_SSL_PROTO_TLS1_2
CONFIG_MBEDTLS_SSL_KEYING_MATERIAL_EXPORT
CONFIG_NOT_SECURE
CONFIG_WIFI_CERTIFICATE_LIB
CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_ECDSA_ENABLED
CONFIG_MBEDTLS_SSL_EXTENDED_MASTER_SECRET
```

**定义位置（Location）**：[`modules/hostap/Kconfig:296`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L296)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_NONE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_NONE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_MBEDTLS_PEM_PARSE_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PEM_PARSE_C)、[`CONFIG_MBEDTLS_PEM_WRITE_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PEM_WRITE_C)、[`CONFIG_MBEDTLS_SSL_SERVER_NAME_INDICATION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_SSL_SERVER_NAME_INDICATION)、[`CONFIG_MBEDTLS_X509_CRL_PARSE_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_X509_CRL_PARSE_C)、[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_SSL_PROTO_TLS1_2)、[`CONFIG_MBEDTLS_SSL_KEYING_MATERIAL_EXPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_SSL_KEYING_MATERIAL_EXPORT)、[`CONFIG_NOT_SECURE`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_NOT_SECURE)、[`CONFIG_WIFI_CERTIFICATE_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_CERTIFICATE_LIB)、[`CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_ECDSA_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_ECDSA_ENABLED)、[`CONFIG_MBEDTLS_SSL_EXTENDED_MASTER_SECRET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_SSL_EXTENDED_MASTER_SECRET)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_EXT"></a>

## 235.49 `CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_EXT`

**提示（Prompt）**：hostap 外部密码实现支持（External Crypto support）

**说明（Help）**

为 hostap 使用外部密码实现（external crypto implementation），适用于由平台而非 Zephyr 提供密码实现的情况。外部实现应提供 hostap 所需的 API 和其他依赖。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_BACKEND>
```

**定义位置（Location）**：[`modules/hostap/Kconfig:254`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L254)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → WPA 认证客户端密码实现（supplicant crypto implementation）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_BACKEND`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_BACKEND)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA"></a>

## 235.50 `CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA`

**提示（Prompt）**：Wi-Fi 的平台安全架构密码支持（Crypto Platform Secure Architecture support）

**说明（Help）**

支持 Mbedtls 3.x 使用平台安全架构（PSA）API，而非旧式 API（legacy APIs）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PSA_CRYPTO
CONFIG_MBEDTLS_DECLARE_PRIVATE_IDENTIFIERS
CONFIG_PSA_WANT_ALG_ECDH
CONFIG_PSA_WANT_ALG_HMAC
CONFIG_PSA_WANT_ALG_CCM
CONFIG_PSA_WANT_ALG_CTR
CONFIG_PSA_WANT_ALG_SHA_1
CONFIG_PSA_WANT_ALG_SHA_256
CONFIG_PSA_WANT_ALG_SHA_224
CONFIG_PSA_WANT_ALG_SHA_384
CONFIG_PSA_WANT_ALG_SHA_512
CONFIG_PSA_WANT_ALG_PBKDF2_HMAC
CONFIG_PSA_WANT_ALG_CMAC
CONFIG_PSA_WANT_ALG_PBKDF2_AES_CMAC_PRF_128
CONFIG_PSA_WANT_KEY_TYPE_AES
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE
CONFIG_PSA_WANT_KEY_TYPE_ECC_PUBLIC_KEY
CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_IMPORT
CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_EXPORT
CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_GENERATE
CONFIG_PSA_WANT_KEY_TYPE_RSA_PUBLIC_KEY
CONFIG_PSA_WANT_KEY_TYPE_DERIVE
CONFIG_PSA_WANT_KEY_TYPE_HMAC
```

**定义位置（Location）**：[`modules/hostap/Kconfig:264`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L264)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_PSA_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_CRYPTO)、[`CONFIG_MBEDTLS_DECLARE_PRIVATE_IDENTIFIERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_DECLARE_PRIVATE_IDENTIFIERS)、[`CONFIG_PSA_WANT_ALG_ECDH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_ECDH)、[`CONFIG_PSA_WANT_ALG_HMAC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_HMAC)、[`CONFIG_PSA_WANT_ALG_CCM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_CCM)、[`CONFIG_PSA_WANT_ALG_CTR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_CTR)、[`CONFIG_PSA_WANT_ALG_SHA_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_SHA_1)、[`CONFIG_PSA_WANT_ALG_SHA_256`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_SHA_256)、[`CONFIG_PSA_WANT_ALG_SHA_224`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_SHA_224)、[`CONFIG_PSA_WANT_ALG_SHA_384`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_SHA_384)、[`CONFIG_PSA_WANT_ALG_SHA_512`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_SHA_512)、[`CONFIG_PSA_WANT_ALG_PBKDF2_HMAC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_PBKDF2_HMAC)、[`CONFIG_PSA_WANT_ALG_CMAC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_CMAC)、[`CONFIG_PSA_WANT_ALG_PBKDF2_AES_CMAC_PRF_128`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_PBKDF2_AES_CMAC_PRF_128)、[`CONFIG_PSA_WANT_KEY_TYPE_AES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_KEY_TYPE_AES)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_IMPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_EXPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_PUBLIC_KEY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_KEY_TYPE_ECC_PUBLIC_KEY)、[`CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_IMPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_IMPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_EXPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_EXPORT)、[`CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_GENERATE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_KEY_TYPE_RSA_KEY_PAIR_GENERATE)、[`CONFIG_PSA_WANT_KEY_TYPE_RSA_PUBLIC_KEY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_KEY_TYPE_RSA_PUBLIC_KEY)、[`CONFIG_PSA_WANT_KEY_TYPE_DERIVE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_KEY_TYPE_DERIVE)、[`CONFIG_PSA_WANT_KEY_TYPE_HMAC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_KEY_TYPE_HMAC)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_NONE"></a>

## 235.51 `CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_NONE`

**提示（Prompt）**：Wi-Fi 不使用密码功能（No Crypto support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_BACKEND>
```

**定义位置（Location）**：[`modules/hostap/Kconfig:251`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L251)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → WPA 认证客户端密码实现（supplicant crypto implementation）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_BACKEND`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_BACKEND)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_TEST"></a>

## 235.52 `CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_TEST`

**提示（Prompt）**：在 HostAP 中测试密码功能（crypto）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**定义位置（Location）**：[`modules/hostap/Kconfig:862`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L862)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_DEBUG_LEVEL"></a>

## 235.53 `CONFIG_WIFI_NM_WPA_SUPPLICANT_DEBUG_LEVEL`

**提示（Prompt）**：WPA 认证客户端编译包含的最低调试消息级别（Min compiled-in debug message level）

**说明（Help）**

固件编译时包含的 WPA 认证客户端（supplicant）调试消息的最低优先级。可用级别和输出消息的函数见认证客户端的 `wpa_debug.h` 文件。注意：除编译时过滤（compile-time filtering）外，还可配置运行时过滤（runtime filtering）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
0 if CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_DBG
3 if CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_INF
4 if CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_WRN
5 if CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_ERR
5
```

**定义位置（Location）**：[`modules/hostap/Kconfig:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_DBG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_DBG)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_INF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_INF)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_WRN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_WRN)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_ERR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_ERR)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_DEBUG_SHOW_KEYS"></a>

## 235.54 `CONFIG_WIFI_NM_WPA_SUPPLICANT_DEBUG_SHOW_KEYS`

**提示（Prompt）**：在调试输出中包含密钥材料（key material）

**说明（Help）**

启用后，调试输出包含密钥材料（key material），例如密码、加密密钥等，相当于 `wpa_supplicant` 的 `-K` 命令行标志。

警告：这存在安全风险，仅应在开发或调试期间启用。生产系统不得记录密钥材料，否则可能破坏网络安全。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**定义位置（Location）**：[`modules/hostap/Kconfig:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP"></a>

## 235.55 `CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP`

**提示（Prompt）**：Wi-Fi Alliance Easy Connect 设备配置协议（WFA Easy Connect DPP）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**主动选择（Selects）**

```text
CONFIG_DPP
CONFIG_DPP2
CONFIG_DPP3
CONFIG_GAS
CONFIG_GAS_SERVER
CONFIG_OFFCHANNEL
CONFIG_MBEDTLS_X509_CSR_WRITE_C
CONFIG_MBEDTLS_X509_CSR_PARSE_C
CONFIG_MBEDTLS_ECP_NIST_OPTIM
CONFIG_PSA_WANT_ECC_SECP_R1_384
```

**定义位置（Location）**：[`modules/hostap/Kconfig:528`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L528)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_DPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DPP)、[`CONFIG_DPP2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DPP2)、[`CONFIG_DPP3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DPP3)、[`CONFIG_GAS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GAS)、[`CONFIG_GAS_SERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GAS_SERVER)、[`CONFIG_OFFCHANNEL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OFFCHANNEL)、[`CONFIG_MBEDTLS_X509_CSR_WRITE_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_X509_CSR_WRITE_C)、[`CONFIG_MBEDTLS_X509_CSR_PARSE_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_X509_CSR_PARSE_C)、[`CONFIG_MBEDTLS_ECP_NIST_OPTIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_ECP_NIST_OPTIM)、[`CONFIG_PSA_WANT_ECC_SECP_R1_384`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ECC_SECP_R1_384)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_DPP`、`CONFIG_DPP2`、`CONFIG_DPP3`、`CONFIG_GAS`、`CONFIG_GAS_SERVER`、`CONFIG_OFFCHANNEL`。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_EAPOL"></a>

## 235.56 `CONFIG_WIFI_NM_WPA_SUPPLICANT_EAPOL`

**提示（Prompt）**：局域网上的可扩展认证协议客户端（EAPoL supplicant）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
y if CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P
CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P
CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P
```

**定义位置（Location）**：[`modules/hostap/Kconfig:466`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L466)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_GLOBAL_HEAP"></a>

## 235.57 `CONFIG_WIFI_NM_WPA_SUPPLICANT_GLOBAL_HEAP`

**提示（Prompt）**：Wi-Fi 驱动使用 Zephyr 内核堆（Kernel Heap）

**说明（Help）**

启用后，认证客户端（supplicant）使用 `K_HEAP` 分配内存。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hostap/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_HEAP"></a>

## 235.58 `CONFIG_WIFI_NM_WPA_SUPPLICANT_HEAP`

**提示（Prompt）**：wpa_supplicant 专用内存池（Dedicated memory pool）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_WIFI_NM_WPA_SUPPLICANT_GLOBAL_HEAP && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
66560 if CONFIG_WIFI_NM_HOSTAPD_AP
60000 if CONFIG_WIFI_USAGE_MODE_STA_AP
55000 if CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE
41808 if CONFIG_WIFI_NM_WPA_SUPPLICANT_AP
40000 if CONFIG_WIFI_NM_MAX_MANAGED_INTERFACES = 2
30000
```

**定义位置（Location）**：[`modules/hostap/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_GLOBAL_HEAP`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_GLOBAL_HEAP)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_WIFI_NM_HOSTAPD_AP`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_HOSTAPD_AP)、[`CONFIG_WIFI_USAGE_MODE_STA_AP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_USAGE_MODE_STA_AP)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_AP`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_AP)、[`CONFIG_WIFI_NM_MAX_MANAGED_INTERFACES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_MAX_MANAGED_INTERFACES)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_LEGACY_CRYPTO"></a>

## 235.59 `CONFIG_WIFI_NM_WPA_SUPPLICANT_LEGACY_CRYPTO`

**提示（Prompt）**：用于向后兼容的旧式密码算法（Legacy non-FIPS crypto）

**说明（Help）**

从认证客户端（supplicant）构建中移除 `CONFIG_FIPS`，重新启用旧式且安全性已被攻破的密码调用路径（legacy and broken crypto call sites）。本条原文说明，`CONFIG_FIPS` 不代表真正的 FIPS 验证，MbedTLS 未通过 FIPS 验证；它只是从默认构建中剔除这些算法的开关。此选项还会链接 hostap 的 `rc4.c`，用于组密钥解封装（group-key unwrap）。关闭 `PSA_WANT_ALG_MD5` 时，CMake 会链接 `md5-internal.c` 和 `md5.c`，使 EAPOL-Key v1 的 HMAC-MD5 不依赖 PSA。

此选项不包含有线等效保密（WEP）。WEP 已弃用，必须通过 `CONFIG_WIFI_NM_WPA_SUPPLICANT_WEP` 单独启用，且只有与本选项同时启用时才生效。此项默认启用，使 WPA／TKIP 和其他旧式接入点（AP）的互操作开箱可用。它并非仅控制 TKIP：它整体禁用 `CONFIG_FIPS`，恢复整套旧式密码功能，包括：

- WPA1／TKIP 的 EAPOL-Key 描述符版本 1，包括四次握手的 HMAC-MD5 消息完整性码（MIC）和 RC4 组密钥解封装。
- 基于 MD5／RC4／DES 的路径，例如 EAP-FAST 密钥导出、IKEv2 MD5 伪随机函数（PRF）、EAP-PWD MD5。

启用的主要原因，是兼容现场仍存在的旧式 WPA-PSK／TKIP 接入点，以及传统互操作／QuickTrack 测试用例。原文指出，TKIP 已弃用，不允许用于当前 Wi-Fi Alliance 认证项目。如果需要完全剔除旧算法的构建，请关闭此项。

此快照暂时默认启用；后续 Zephyr 版本将改为默认禁用。届时，除非显式设置 `LEGACY_CRYPTO`，WEP 和 TKIP 互操作也会随之禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_NONE && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NOT_SECURE
```

**定义位置（Location）**：[`modules/hostap/Kconfig:179`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L179)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_NONE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_NONE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_NOT_SECURE`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_NOT_SECURE)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_NAN"></a>

## 235.60 `CONFIG_WIFI_NM_WPA_SUPPLICANT_NAN`

**提示（Prompt）**：邻近感知网络（Neighbor Awareness Networking，NAN）支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_NONE && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**定义位置（Location）**：[`modules/hostap/Kconfig:541`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L541)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_NONE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_NONE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_NO_DEBUG"></a>

## 235.61 `CONFIG_WIFI_NM_WPA_SUPPLICANT_NO_DEBUG`

**提示（Prompt）**：禁用调试消息打印，可显著减小代码体积（code size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**定义位置（Location）**：[`modules/hostap/Kconfig:524`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L524)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_NW_SEL"></a>

## 235.62 `CONFIG_WIFI_NM_WPA_SUPPLICANT_NW_SEL`

**提示（Prompt）**：WPA 认证客户端网络选择准则（Network selection criterion）

**说明（Help）**

选择认证客户端（supplicant）的网络选择方法（network selection method）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_NW_SEL_RELIABILITY
```

**可选项（Choices）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_NW_SEL_THROUGHPUT
CONFIG_WIFI_NM_WPA_SUPPLICANT_NW_SEL_RELIABILITY
CONFIG_WIFI_NM_WPA_SUPPLICANT_NW_SEL_THROUGHPUT
CONFIG_WIFI_NM_WPA_SUPPLICANT_NW_SEL_RELIABILITY
CONFIG_WIFI_NM_WPA_SUPPLICANT_NW_SEL_THROUGHPUT
CONFIG_WIFI_NM_WPA_SUPPLICANT_NW_SEL_RELIABILITY
```

**定义位置（Location）**：[`modules/hostap/Kconfig:836`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L836)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_NW_SEL_RELIABILITY`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_NW_SEL_RELIABILITY)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_NW_SEL_THROUGHPUT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_NW_SEL_THROUGHPUT)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_NW_SEL_RELIABILITY"></a>

## 235.63 `CONFIG_WIFI_NM_WPA_SUPPLICANT_NW_SEL_RELIABILITY`

**提示（Prompt）**：基于可靠性的网络选择（Reliability-based network selection）

**说明（Help）**

根据可靠性（reliability）选择网络。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NM_WPA_SUPPLICANT_NW_SEL>
```

**定义位置（Location）**：[`modules/hostap/Kconfig:847`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L847)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → WPA 认证客户端网络选择准则（Network selection criterion）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_NW_SEL`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_NW_SEL)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_NW_SEL_THROUGHPUT"></a>

## 235.64 `CONFIG_WIFI_NM_WPA_SUPPLICANT_NW_SEL_THROUGHPUT`

**提示（Prompt）**：基于吞吐量的网络选择（Throughput-based network selection）

**说明（Help）**

根据吞吐量（throughput）选择网络。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NM_WPA_SUPPLICANT_NW_SEL>
```

**定义位置（Location）**：[`modules/hostap/Kconfig:842`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L842)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → WPA 认证客户端网络选择准则（Network selection criterion）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_NW_SEL`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_NW_SEL)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_OWE"></a>

## 235.65 `CONFIG_WIFI_NM_WPA_SUPPLICANT_OWE`

**提示（Prompt）**：wpa_supplicant 包装层的机会式无线加密（OWE）支持

**说明（Help）**

通过 `wpa_supplicant` 网络管理器（network manager）提供机会式无线加密（OWE）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3 && CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_COMMON && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**定义位置（Location）**：[`modules/hostap/Kconfig:420`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L420)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_COMMON`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_COMMON)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P"></a>

## 235.66 `CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P`

**提示（Prompt）**：点对点模式（P2P mode）支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**主动选择（Selects）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_AP
CONFIG_WIFI_NM_WPA_SUPPLICANT_WPS
CONFIG_WIFI_NM_WPA_SUPPLICANT_EAPOL
```

**定义位置（Location）**：[`modules/hostap/Kconfig:440`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L440)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_AP`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_AP)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_WPS`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_WPS)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_EAPOL`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_EAPOL)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P_DEVICE_NAME"></a>

## 235.67 `CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P_DEVICE_NAME`

**提示（Prompt）**：默认 Wi-Fi 点对点设备名称（P2P device name）

**说明（Help）**

在点对点设备信息属性（P2P Device Info attribute）和 Wi-Fi 保护设置属性（WPS attributes）中通告的设备名称。认证客户端（supplicant）初始化时应用此名称，运行时可修改。最长为 32 个字符（`WPS_DEV_NAME_MAX_LEN`）。留空时，初始化会保留 `wpa_supplicant` 默认设备名称。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
"ZephyrP2PDevice"
```

**定义位置（Location）**：[`modules/hostap/Kconfig:455`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L455)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → 点对点模式（P2P mode）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P_PROV_DISC_REQ_RETRIES"></a>

## 235.68 `CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P_PROV_DISC_REQ_RETRIES`

**提示（Prompt）**：点对点配置发现请求重试次数（P2P provision discovery request retries）

**说明（Help）**

对端未监听时，点对点配置发现请求（P2P provision discovery requests）的最大重试次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
120
```

**定义位置（Location）**：[`modules/hostap/Kconfig:448`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L448)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → 点对点模式（P2P mode）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_PRINT_PMK"></a>

## 235.69 `CONFIG_WIFI_NM_WPA_SUPPLICANT_PRINT_PMK`

**提示（Prompt）**：每次成功握手打印一次成对主密钥（PMK）［实验性，EXPERIMENTAL］

**说明（Help）**

每次四次握手（4-way handshake）完成后，将成对主密钥（PMK）作为十六进制字符串打印一次，不受 `WIFI_NM_WPA_SUPPLICANT_DEBUG_LEVEL` 和 `WIFI_NM_WPA_SUPPLICANT_DEBUG_SHOW_KEYS` 控制。目的是获取解密空中 Wi-Fi 抓包（over-the-air Wi-Fi capture）所需的 PMK，同时避免启用完整认证客户端调试输出时的大量日志。

警告：这存在安全风险，仅应在开发或调试期间启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`modules/hostap/Kconfig:128`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L128)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_PRIO"></a>

## 235.70 `CONFIG_WIFI_NM_WPA_SUPPLICANT_PRIO`

**提示（Prompt）**：wpa_supplicant 线程优先级（Thread priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`modules/hostap/Kconfig:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_ROAMING"></a>

## 235.71 `CONFIG_WIFI_NM_WPA_SUPPLICANT_ROAMING`

**提示（Prompt）**：漫游支持（Roaming support）

**说明（Help）**

启用 `wpa_supplicant` 漫游（roaming）支持。当前基本服务集（BSS）的接收信号强度指示（RSSI）下降时，站点（STA）尝试寻找 RSSI 更好的接入点（AP）。找到后，STA 自动重新关联到新 AP，而不丢失连接。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**被选择（Selected by）**

```text
CONFIG_NXP_WIFI_ROAMING
```

**弱选择（Implies）**

```text
CONFIG_IEEE80211R
```

**定义位置（Location）**：[`modules/hostap/Kconfig:581`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L581)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_NXP_WIFI_ROAMING`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_ROAMING)、[`CONFIG_IEEE80211R`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IEEE80211R)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_IEEE80211R`。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_ROAMING_RETRY"></a>

## 235.72 `CONFIG_WIFI_NM_WPA_SUPPLICANT_ROAMING_RETRY`

**提示（Prompt）**：每种漫游方法的重试次数（Retry count）

**说明（Help）**

分别尝试 11K 和 11V 漫游（roaming）的次数。达到次数后，回退到下一种漫游方法；两者都达到次数后，回退到执行全信道扫描的传统漫游（legacy roaming）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_ROAMING && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`modules/hostap/Kconfig:589`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L589)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → 漫游支持（Roaming support）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_ROAMING`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_ROAMING)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_ROBUST_AV"></a>

## 235.73 `CONFIG_WIFI_NM_WPA_SUPPLICANT_ROBUST_AV`

**提示（Prompt）**：稳健音视频流传输支持（Robust Audio Video streaming support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_ADVANCED_FEATURES && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hostap/Kconfig:157`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L157)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_ADVANCED_FEATURES`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_ADVANCED_FEATURES)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_RRM"></a>

## 235.74 `CONFIG_WIFI_NM_WPA_SUPPLICANT_RRM`

**提示（Prompt）**：无线电资源管理支持（Radio Resource Management support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_ADVANCED_FEATURES && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hostap/Kconfig:174`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L174)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_ADVANCED_FEATURES`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_ADVANCED_FEATURES)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_SKIP_DHCP_ON_ROAMING"></a>

## 235.75 `CONFIG_WIFI_NM_WPA_SUPPLICANT_SKIP_DHCP_ON_ROAMING`

**提示（Prompt）**：漫游到新接入点后跳过 DHCP（Skip DHCP）

**说明（Help）**

对于第二层漫游（L2 roaming），原接入点和新接入点位于同一子网（subnet），客户端可继续使用相同 IP 地址并跳过 DHCP；启用此项即可跳过。对于第三层漫游（L3 roaming），原接入点和新接入点位于不同子网，客户端需要在漫游后获取新 IP 地址；禁用此项可在漫游后保留 DHCP 流程。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**被选择（Selected by）**

```text
CONFIG_NXP_WIFI_ROAMING
```

**定义位置（Location）**：[`modules/hostap/Kconfig:599`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L599)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_NXP_WIFI_ROAMING`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_ROAMING)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_THREAD_STACK_SIZE"></a>

## 235.76 `CONFIG_WIFI_NM_WPA_SUPPLICANT_THREAD_STACK_SIZE`

**提示（Prompt）**：wpa_supplicant 线程栈大小（Stack size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
8600 if CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE || CONFIG_WIFI_USAGE_MODE_STA_AP
8000 if CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P
6300
```

**定义位置（Location）**：[`modules/hostap/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_WIFI_USAGE_MODE_STA_AP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_USAGE_MODE_STA_AP)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_WEP"></a>

## 235.77 `CONFIG_WIFI_NM_WPA_SUPPLICANT_WEP`

**提示（Prompt）**：有线等效保密（WEP）支持［已弃用，DEPRECATED］

**说明（Help）**

已弃用：有线等效保密（WEP）是旧式且已被攻破的密码机制，将被移除。在其尚未移除期间，可与 `WIFI_NM_WPA_SUPPLICANT_LEGACY_CRYPTO` 一起启用以保留 WEP 支持。未启用 `LEGACY_CRYPTO` 时，此项无效。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_NONE && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
CONFIG_NOT_SECURE
```

**定义位置（Location）**：[`modules/hostap/Kconfig:216`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L216)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_NONE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_NONE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)、[`CONFIG_NOT_SECURE`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_NOT_SECURE)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_WNM"></a>

## 235.78 `CONFIG_WIFI_NM_WPA_SUPPLICANT_WNM`

**提示（Prompt）**：无线网络管理支持（Wireless Network Management support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_ADVANCED_FEATURES && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hostap/Kconfig:170`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L170)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → 高级功能（Advanced features）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_ADVANCED_FEATURES`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_ADVANCED_FEATURES)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3"></a>

## 235.79 `CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

内部 WPA3／对等实体同时认证（SAE）实现，基于大整数（bignum）。由 `WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_INT` 选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_INT
CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_INT
CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_INT
```

**定义位置（Location）**：[`modules/hostap/Kconfig:406`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L406)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_INT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_INT)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_COMMON"></a>

## 235.80 `CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_COMMON`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示 WPA3／对等实体同时认证（SAE）可用，无论采用内部还是外部实现。可在代码中使用此项控制 WPA3 功能，而无需区分后端（backend）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
y if CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_INT || CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_EXT
```

**定义位置（Location）**：[`modules/hostap/Kconfig:412`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L412)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_INT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_INT)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_EXT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_EXT)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION"></a>

## 235.81 `CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION`

**提示（Prompt）**：WPA3 实现（implementation）

**说明（Help）**

选择 WPA3／对等实体同时认证（SAE）的提供方式。内部方式（Internal）使用认证客户端基于大整数（bignum）的实现；外部方式（External）使用树外实现（out-of-tree implementation），例如 PSA crypto；无（None）则禁用 WPA3。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_NONE && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_INT
```

**可选项（Choices）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_NONE
CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_INT
CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_EXT
CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_NONE
CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_INT
CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_EXT
CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_NONE
CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_INT
CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_EXT
```

**定义位置（Location）**：[`modules/hostap/Kconfig:383`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L383)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_NONE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_NONE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_INT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_INT)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_NONE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_NONE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_EXT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_EXT)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_EXT"></a>

## 235.82 `CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_EXT`

**提示（Prompt）**：外部（External）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION>
```

**定义位置（Location）**：[`modules/hostap/Kconfig:401`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L401)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → WPA3 实现（implementation）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_INT"></a>

## 235.83 `CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_INT`

**提示（Prompt）**：内部使用（Internal）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION>
```

**主动选择（Selects）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3
```

**定义位置（Location）**：[`modules/hostap/Kconfig:397`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L397)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → WPA3 实现（implementation）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_NONE"></a>

## 235.84 `CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_NONE`

**提示（Prompt）**：无（None）

**说明（Help）**

WPA3 已禁用，仅可使用 WPA2 及更早版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION>
```

**定义位置（Location）**：[`modules/hostap/Kconfig:392`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L392)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → WPA3 实现（implementation）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_WPS"></a>

## 235.85 `CONFIG_WIFI_NM_WPA_SUPPLICANT_WPS`

**提示（Prompt）**：Wi-Fi 保护设置（WPS）支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_NONE && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P
CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P
CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P
```

**定义位置（Location）**：[`modules/hostap/Kconfig:431`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L431)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_NONE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_NONE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_WQ_PRIO"></a>

## 235.86 `CONFIG_WIFI_NM_WPA_SUPPLICANT_WQ_PRIO`

**提示（Prompt）**：wpa_supplicant 接口工作队列（iface workqueue）线程优先级

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
7
```

**定义位置（Location）**：[`modules/hostap/Kconfig:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_WQ_STACK_SIZE"></a>

## 235.87 `CONFIG_WIFI_NM_WPA_SUPPLICANT_WQ_STACK_SIZE`

**提示（Prompt）**：wpa_supplicant 接口工作队列（iface workqueue）栈大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
4400
```

**定义位置（Location）**：[`modules/hostap/Kconfig:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_WPA_CLI"></a>

## 235.88 `CONFIG_WPA_CLI`

**提示（Prompt）**：WPA 命令行接口（CLI）支持

**说明（Help）**

为 `wpa_supplicant` 启用 WPA 命令行接口（CLI）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
y if CONFIG_WIFI_NM_WPA_SUPPLICANT_CLI
```

**定义位置（Location）**：[`modules/hostap/Kconfig:568`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L568)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CLI`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CLI)。

<a id="CONFIG_ZVFS_EVENTFD_ADD_SIZE_WIFI_NM_WPA_SUPPLICANT"></a>

## 235.89 `CONFIG_ZVFS_EVENTFD_ADD_SIZE_WIFI_NM_WPA_SUPPLICANT`

**提示（Prompt）**：hostap 所需的事件文件描述符数量（eventfds）

**说明（Help）**

WPA 认证客户端（supplicant）和 `hostapd` 会分配多个 ZVFS 事件文件描述符（eventfds），例如用于认证客户端事件套接字（event socket），以及本地／全局控制接口套接字对（socket pairs）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`modules/hostap/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_ZVFS_OPEN_ADD_SIZE_WIFI_NM_WPA_SUPPLICANT"></a>

## 235.90 `CONFIG_ZVFS_OPEN_ADD_SIZE_WIFI_NM_WPA_SUPPLICANT`

**提示（Prompt）**：hostap 所需的套接字描述符数量（socket descriptors）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
12
```

**定义位置（Location）**：[`modules/hostap/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<!-- kconfig-navigation -->

[上一章](P234_modules_hal_tdk_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P236_modules_liblc3_配置项参考.md)
