---
id: learning.zephyr-docs.kconfig-reference.page-208
title: "`modules/Kconfig.open-amp`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第208章\_`modules/Kconfig.open-amp`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/Kconfig.open-amp` 的 5 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_OPENAMP"></a>

## 208.1 `CONFIG_OPENAMP`

**提示（Prompt）**：OpenAMP 支持（Support）

**说明（Help）**

启用 OpenAMP 进程间通信库（IPC library）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZEPHYR_OPEN_AMP_MODULE
```

**主动选择（Selects）**

```text
CONFIG_LIBMETAL
```

**被选择（Selected by）**

```text
CONFIG_ETH_IVSHMEM
CONFIG_RPMSG_SERVICE
CONFIG_IPC_SERVICE_BACKEND_RPMSG
```

**被弱选择（Implied by）**

```text
CONFIG_OPENAMP_RSC_TABLE
```

**定义位置（Location）**：[`modules/Kconfig.open-amp:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.open-amp#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_OPEN_AMP_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_OPEN_AMP_MODULE)、[`CONFIG_LIBMETAL`](P204_modules_Kconfig.libmetal_配置项参考.md#CONFIG_LIBMETAL)、[`CONFIG_ETH_IVSHMEM`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_IVSHMEM)、[`CONFIG_RPMSG_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RPMSG_SERVICE)、[`CONFIG_IPC_SERVICE_BACKEND_RPMSG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IPC_SERVICE_BACKEND_RPMSG)、[`CONFIG_OPENAMP_RSC_TABLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENAMP_RSC_TABLE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_OPEN_AMP_MODULE`。

<a id="CONFIG_OPENAMP_MASTER"></a>

## 208.2 `CONFIG_OPENAMP_MASTER`

**提示（Prompt）**：OpenAMP 主端（Master）支持

**说明（Help）**

启用 OpenAMP VirtIO 主端（Master）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENAMP
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_RPMSG_SERVICE_MODE_MASTER
```

**定义位置（Location）**：[`modules/Kconfig.open-amp:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.open-amp#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → OpenAMP 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_OPENAMP`](P208_modules_Kconfig.open-amp_配置项参考.md#CONFIG_OPENAMP)、[`CONFIG_RPMSG_SERVICE_MODE_MASTER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RPMSG_SERVICE_MODE_MASTER)。

<a id="CONFIG_OPENAMP_SLAVE"></a>

## 208.3 `CONFIG_OPENAMP_SLAVE`

**提示（Prompt）**：OpenAMP 从端（Slave）支持

**说明（Help）**

启用 OpenAMP VirtIO 从端（Slave）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENAMP
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_RPMSG_SERVICE_MODE_REMOTE
```

**定义位置（Location）**：[`modules/Kconfig.open-amp:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.open-amp#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → OpenAMP 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_OPENAMP`](P208_modules_Kconfig.open-amp_配置项参考.md#CONFIG_OPENAMP)、[`CONFIG_RPMSG_SERVICE_MODE_REMOTE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RPMSG_SERVICE_MODE_REMOTE)。

<a id="CONFIG_OPENAMP_SRC_PATH"></a>

## 208.4 `CONFIG_OPENAMP_SRC_PATH`

**提示（Prompt）**：OpenAMP 库源码路径（source path）

**说明（Help）**

指定 open-amp 库的源码路径（source path）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENAMP && CONFIG_OPENAMP
```

**默认值（Defaults）**

```text
"open-amp"
```

**定义位置（Location）**：[`modules/Kconfig.open-amp:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.open-amp#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → OpenAMP 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_OPENAMP`](P208_modules_Kconfig.open-amp_配置项参考.md#CONFIG_OPENAMP)。

<a id="CONFIG_OPENAMP_WITH_DCACHE"></a>

## 208.5 `CONFIG_OPENAMP_WITH_DCACHE`

**提示（Prompt）**：构建启用虚拟环缓存操作（vrings cache operations）的 OpenAMP

**说明（Help）**

构建 OpenAMP 时，启用虚拟环缓存操作（vrings cache operations）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CACHE_MANAGEMENT && CONFIG_OPENAMP
```

**定义位置（Location）**：[`modules/Kconfig.open-amp:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.open-amp#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → OpenAMP 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_OPENAMP`](P208_modules_Kconfig.open-amp_配置项参考.md#CONFIG_OPENAMP)。

<!-- kconfig-navigation -->

[上一章](P207_modules_Kconfig.nuvoton_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P209_modules_Kconfig.renesas_配置项参考_1.md)
