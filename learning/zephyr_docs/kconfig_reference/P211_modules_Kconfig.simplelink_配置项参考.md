---
id: learning.zephyr-docs.kconfig-reference.page-211
title: "`modules/Kconfig.simplelink`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第211章\_`modules/Kconfig.simplelink`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/Kconfig.simplelink` 的 1 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SIMPLELINK_HOST_DRIVER"></a>

## 211.1 `CONFIG_SIMPLELINK_HOST_DRIVER`

**提示（Prompt）**：构建 SimpleLink Wi-Fi 主机驱动（Host Driver）

**说明（Help）**

构建 SimpleLink 主机驱动（host driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_CC3220SDK && CONFIG_MULTITHREADING
```

**主动选择（Selects）**

```text
CONFIG_ERRNO
CONFIG_POSIX_SYSTEM_INTERFACES
CONFIG_POSIX_SEMAPHORES
CONFIG_POSIX_THREADS
CONFIG_POSIX_TIMERS
```

**被选择（Selected by）**

```text
CONFIG_WIFI_SIMPLELINK
```

**定义位置（Location）**：[`modules/Kconfig.simplelink:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.simplelink#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_CC3220SDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_CC3220SDK)、[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_ERRNO`](P197_lib_配置项参考_1.md#CONFIG_ERRNO)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_SEMAPHORES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SEMAPHORES)、[`CONFIG_POSIX_THREADS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREADS)、[`CONFIG_POSIX_TIMERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_TIMERS)、[`CONFIG_WIFI_SIMPLELINK`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_SIMPLELINK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_CC3220SDK`。

<!-- kconfig-navigation -->

[上一章](P210_modules_Kconfig.renesas_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P212_modules_Kconfig.stm32_配置项参考_1.md)
