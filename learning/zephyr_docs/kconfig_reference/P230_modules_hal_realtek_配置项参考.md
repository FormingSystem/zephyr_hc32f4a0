---
id: learning.zephyr-docs.kconfig-reference.page-230
title: "`modules/hal_realtek`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第230章\_`modules/hal_realtek`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/hal_realtek` 的 7 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_REALTEK_AMEBA_OS_WRAPPER"></a>

## 230.1 `CONFIG_REALTEK_AMEBA_OS_WRAPPER`

**提示（Prompt）**：Realtek Ameba 操作系统包装层（OS Wrapper Layer）

**说明（Help）**

启用 Realtek Ameba 操作系统包装抽象层（OS wrapper abstraction layer），为 Ameba HAL 驱动提供实时操作系统抽象（RTOS abstraction）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_REALTEK_AMEBA && CONFIG_HAS_REALTEK_AMEBA
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_SDHC_AMEBA
```

**定义位置（Location）**：[`modules/hal_realtek/ameba/Kconfig.ameba:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_realtek/ameba/Kconfig.ameba#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_AMEBA)、[`CONFIG_HAS_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_AMEBA)、[`CONFIG_SDHC_AMEBA`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_AMEBA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_REALTEK_AMEBA`、`CONFIG_HAS_REALTEK_AMEBA`。

<a id="CONFIG_REALTEK_BEE_OSIF_MSGQ_MAX_COUNT"></a>

## 230.2 `CONFIG_REALTEK_BEE_OSIF_MSGQ_MAX_COUNT`

**提示（Prompt）**：最大消息队列数量（message queues）

**说明（Help）**

设置操作系统接口（OSIF）支持的消息队列对象（message queue objects）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_REALTEK_BEE_OS_INTERFACE && CONFIG_HAS_REALTEK_BEE
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`modules/hal_realtek/bee/Kconfig.bee:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_realtek/bee/Kconfig.bee#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 操作系统接口层（OS Interface，OSIF）

**配置项引用（Symbol References）**：[`CONFIG_USE_REALTEK_BEE_OS_INTERFACE`](P230_modules_hal_realtek_配置项参考.md#CONFIG_USE_REALTEK_BEE_OS_INTERFACE)、[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`。

<a id="CONFIG_REALTEK_BEE_OSIF_MUTEX_MAX_COUNT"></a>

## 230.3 `CONFIG_REALTEK_BEE_OSIF_MUTEX_MAX_COUNT`

**提示（Prompt）**：最大互斥锁数量（mutexes）

**说明（Help）**

设置操作系统接口（OSIF）支持的互斥锁对象（mutex objects）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_REALTEK_BEE_OS_INTERFACE && CONFIG_HAS_REALTEK_BEE
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`modules/hal_realtek/bee/Kconfig.bee:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_realtek/bee/Kconfig.bee#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 操作系统接口层（OS Interface，OSIF）

**配置项引用（Symbol References）**：[`CONFIG_USE_REALTEK_BEE_OS_INTERFACE`](P230_modules_hal_realtek_配置项参考.md#CONFIG_USE_REALTEK_BEE_OS_INTERFACE)、[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`。

<a id="CONFIG_REALTEK_BEE_OSIF_SEM_MAX_COUNT"></a>

## 230.4 `CONFIG_REALTEK_BEE_OSIF_SEM_MAX_COUNT`

**提示（Prompt）**：最大信号量数量（semaphores）

**说明（Help）**

设置操作系统接口（OSIF）支持的信号量对象（semaphore objects）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_REALTEK_BEE_OS_INTERFACE && CONFIG_HAS_REALTEK_BEE
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`modules/hal_realtek/bee/Kconfig.bee:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_realtek/bee/Kconfig.bee#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 操作系统接口层（OS Interface，OSIF）

**配置项引用（Symbol References）**：[`CONFIG_USE_REALTEK_BEE_OS_INTERFACE`](P230_modules_hal_realtek_配置项参考.md#CONFIG_USE_REALTEK_BEE_OS_INTERFACE)、[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`。

<a id="CONFIG_REALTEK_BEE_OSIF_TASK_MAX_COUNT"></a>

## 230.5 `CONFIG_REALTEK_BEE_OSIF_TASK_MAX_COUNT`

**提示（Prompt）**：最大任务数量（tasks）

**说明（Help）**

设置操作系统接口（OSIF）支持的任务／线程对象（task/thread objects）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_REALTEK_BEE_OS_INTERFACE && CONFIG_HAS_REALTEK_BEE
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`modules/hal_realtek/bee/Kconfig.bee:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_realtek/bee/Kconfig.bee#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 操作系统接口层（OS Interface，OSIF）

**配置项引用（Symbol References）**：[`CONFIG_USE_REALTEK_BEE_OS_INTERFACE`](P230_modules_hal_realtek_配置项参考.md#CONFIG_USE_REALTEK_BEE_OS_INTERFACE)、[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`。

<a id="CONFIG_REALTEK_BEE_OSIF_TIMER_MAX_COUNT"></a>

## 230.6 `CONFIG_REALTEK_BEE_OSIF_TIMER_MAX_COUNT`

**提示（Prompt）**：最大定时器数量（timers）

**说明（Help）**

设置可在操作系统接口（OSIF）层同时分配的定时器对象（timer objects）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_REALTEK_BEE_OS_INTERFACE && CONFIG_HAS_REALTEK_BEE
```

**默认值（Defaults）**

```text
64
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`modules/hal_realtek/bee/Kconfig.bee:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_realtek/bee/Kconfig.bee#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`） → Realtek Bee 操作系统接口层（OS Interface，OSIF）

**配置项引用（Symbol References）**：[`CONFIG_USE_REALTEK_BEE_OS_INTERFACE`](P230_modules_hal_realtek_配置项参考.md#CONFIG_USE_REALTEK_BEE_OS_INTERFACE)、[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`。

<a id="CONFIG_USE_REALTEK_BEE_OS_INTERFACE"></a>

## 230.7 `CONFIG_USE_REALTEK_BEE_OS_INTERFACE`

**提示（Prompt）**：Realtek Bee 操作系统接口层（OS Interface，OSIF）

**说明（Help）**

启用 Realtek Bee 操作系统接口（OS Interface，OSIF）抽象层。此层提供统一的 API 包装（wrapper），确保 Realtek Bee 系列 SoC 能在不同底层操作系统之间移植。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_REALTEK_BEE
```

**主动选择（Selects）**

```text
CONFIG_POLL
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_RTL8752H
CONFIG_SOC_SERIES_RTL87X2G
```

**定义位置（Location）**：[`modules/hal_realtek/bee/Kconfig.bee:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_realtek/bee/Kconfig.bee#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_realtek`（Realtek 硬件抽象层模块；工作区相对路径 `modules/hal/realtek`）

**配置项引用（Symbol References）**：[`CONFIG_HAS_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_REALTEK_BEE)、[`CONFIG_POLL`](P002_kernel_配置项参考_2.md#CONFIG_POLL)、[`CONFIG_SOC_SERIES_RTL8752H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTL8752H)、[`CONFIG_SOC_SERIES_RTL87X2G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTL87X2G)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_REALTEK_BEE`。

<!-- kconfig-navigation -->

[上一章](P229_modules_hal_nxp_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P231_modules_hal_rpi_pico_配置项参考.md)
