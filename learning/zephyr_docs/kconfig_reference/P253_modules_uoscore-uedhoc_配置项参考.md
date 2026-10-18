---
id: learning.zephyr-docs.kconfig-reference.page-253
title: "`modules/uoscore-uedhoc`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第253章\_`modules/uoscore-uedhoc`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/uoscore-uedhoc` 的 5 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_UEDHOC"></a>

## 253.1 `CONFIG_UEDHOC`

**提示（Prompt）**：UEDHOC 库（UEDHOC library）

**说明（Help）**

此选项启用 UEDHOC 库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZCBOR && CONFIG_ZCBOR_CANONICAL
```

**主动选择（Selects）**

```text
CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON
```

**定义位置（Location）**：[`modules/uoscore-uedhoc/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/uoscore-uedhoc/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → uoscore-uedhoc（模块路径 `modules/lib/uoscore-uedhoc`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_ZCBOR`](P254_modules_zcbor_配置项参考.md#CONFIG_ZCBOR)、[`CONFIG_ZCBOR_CANONICAL`](P254_modules_zcbor_配置项参考.md#CONFIG_ZCBOR_CANONICAL)、[`CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON`。

<a id="CONFIG_UEDHOC_DEBUG"></a>

## 253.2 `CONFIG_UEDHOC_DEBUG`

**提示（Prompt）**：uedhoc 库中的调试日志（Debug logs）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UEDHOC
```

**定义位置（Location）**：[`modules/uoscore-uedhoc/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/uoscore-uedhoc/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → uoscore-uedhoc（模块路径 `modules/lib/uoscore-uedhoc`，相对于 west 工作区顶层目录） → UEDHOC 库（UEDHOC library）

**配置项引用（Symbol References）**：[`CONFIG_UEDHOC`](P253_modules_uoscore-uedhoc_配置项参考.md#CONFIG_UEDHOC)。

<a id="CONFIG_UOSCORE"></a>

## 253.3 `CONFIG_UOSCORE`

**提示（Prompt）**：UOSCORE 库（UOSCORE library）

**说明（Help）**

此选项启用 UOSCORE 库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZCBOR && CONFIG_ZCBOR_CANONICAL
```

**主动选择（Selects）**

```text
CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON
```

**定义位置（Location）**：[`modules/uoscore-uedhoc/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/uoscore-uedhoc/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → uoscore-uedhoc（模块路径 `modules/lib/uoscore-uedhoc`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_ZCBOR`](P254_modules_zcbor_配置项参考.md#CONFIG_ZCBOR)、[`CONFIG_ZCBOR_CANONICAL`](P254_modules_zcbor_配置项参考.md#CONFIG_ZCBOR_CANONICAL)、[`CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_UOSCORE_UEDHOC_CRYPTO_COMMON`。

<a id="CONFIG_UOSCORE_DEBUG"></a>

## 253.4 `CONFIG_UOSCORE_DEBUG`

**提示（Prompt）**：uoscore 库中的调试日志（Debug logs）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UOSCORE
```

**定义位置（Location）**：[`modules/uoscore-uedhoc/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/uoscore-uedhoc/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → uoscore-uedhoc（模块路径 `modules/lib/uoscore-uedhoc`，相对于 west 工作区顶层目录） → UOSCORE 库（UOSCORE library）

**配置项引用（Symbol References）**：[`CONFIG_UOSCORE`](P253_modules_uoscore-uedhoc_配置项参考.md#CONFIG_UOSCORE)。

<a id="CONFIG_UOSCORE_NVM_SUPPORT"></a>

## 253.5 `CONFIG_UOSCORE_NVM_SUPPORT`

**提示（Prompt）**：用于持久保存 OSCORE 发送方序列号的非易失存储支持（non-volatile storage for OSCORE SSN persistence）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS && CONFIG_UOSCORE
```

**被选择（Selected by）**

```text
CONFIG_COAP_OSCORE_CONTEXT_REUSE
```

**定义位置（Location）**：[`modules/uoscore-uedhoc/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/uoscore-uedhoc/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → uoscore-uedhoc（模块路径 `modules/lib/uoscore-uedhoc`，相对于 west 工作区顶层目录） → UOSCORE 库（UOSCORE library）

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SETTINGS)、[`CONFIG_UOSCORE`](P253_modules_uoscore-uedhoc_配置项参考.md#CONFIG_UOSCORE)、[`CONFIG_COAP_OSCORE_CONTEXT_REUSE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_OSCORE_CONTEXT_REUSE)。

<!-- kconfig-navigation -->

[上一章](P252_modules_trusted-firmware-m_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P254_modules_zcbor_配置项参考.md)
