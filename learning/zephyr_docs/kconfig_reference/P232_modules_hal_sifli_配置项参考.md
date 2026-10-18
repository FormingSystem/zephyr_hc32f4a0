---
id: learning.zephyr-docs.kconfig-reference.page-232
title: "`modules/hal_sifli`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第232章\_`modules/hal_sifli`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/hal_sifli` 的 44 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_USE_SIFLI_HAL"></a>

## 232.1 `CONFIG_USE_SIFLI_HAL`

**提示（Prompt）**：SiFli 硬件抽象层（HAL）

**说明（Help）**

启用 SiFli 硬件抽象层（HAL）模块。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SIFLI_HAL
```

**被选择（Selected by）**

```text
CONFIG_BT_SF32LB
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)、[`CONFIG_BT_SF32LB`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_SF32LB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_ADC"></a>

## 232.2 `CONFIG_USE_SIFLI_HAL_ADC`

**提示（Prompt）**：SiFli 模数转换器（ADC）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 模数转换器（ADC）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_AES"></a>

## 232.3 `CONFIG_USE_SIFLI_HAL_AES`

**提示（Prompt）**：SiFli 高级加密标准（AES）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 高级加密标准（AES）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_AON"></a>

## 232.4 `CONFIG_USE_SIFLI_HAL_AON`

**提示（Prompt）**：SiFli 始终供电域（AON）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 始终供电域（AON）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**被选择（Selected by）**

```text
CONFIG_USE_SIFLI_IPC_QUEUE
CONFIG_USE_SIFLI_IPC_QUEUE
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)、[`CONFIG_USE_SIFLI_IPC_QUEUE`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_IPC_QUEUE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_ATIM"></a>

## 232.5 `CONFIG_USE_SIFLI_HAL_ATIM`

**提示（Prompt）**：SiFli 高级定时器（ATIM）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 高级定时器（ATIM）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_SF32LB52X && CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_SF32LB52X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SF32LB52X)、[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_SF32LB52X`、`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_AUDCODEC"></a>

## 232.6 `CONFIG_USE_SIFLI_HAL_AUDCODEC`

**提示（Prompt）**：SiFli 音频编解码器（AUDCODEC）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 音频编解码器（AUDCODEC）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_SF32LB52X && CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_SF32LB52X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SF32LB52X)、[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_SF32LB52X`、`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_AUDPRC"></a>

## 232.7 `CONFIG_USE_SIFLI_HAL_AUDPRC`

**提示（Prompt）**：SiFli 音频处理器（AUDPRC）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 音频处理器（AUDPRC）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_SF32LB52X && CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_SF32LB52X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SF32LB52X)、[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_SF32LB52X`、`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_BUSMON"></a>

## 232.8 `CONFIG_USE_SIFLI_HAL_BUSMON`

**提示（Prompt）**：SiFli 总线监视器（BUSMON）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 总线监视器（BUSMON）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_CACHE"></a>

## 232.9 `CONFIG_USE_SIFLI_HAL_CACHE`

**提示（Prompt）**：SiFli 缓存（CACHE）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 缓存（CACHE）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_CRC"></a>

## 232.10 `CONFIG_USE_SIFLI_HAL_CRC`

**提示（Prompt）**：SiFli 循环冗余校验（CRC）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 循环冗余校验（CRC）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_DMA"></a>

## 232.11 `CONFIG_USE_SIFLI_HAL_DMA`

**提示（Prompt）**：SiFli 直接内存访问（DMA）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 直接内存访问（DMA）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_EPIC"></a>

## 232.12 `CONFIG_USE_SIFLI_HAL_EPIC`

**提示（Prompt）**：SiFli EPIC硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli EPIC硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_EXTDMA"></a>

## 232.13 `CONFIG_USE_SIFLI_HAL_EXTDMA`

**提示（Prompt）**：SiFli 扩展直接内存访问（EXTDMA）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 扩展直接内存访问（EXTDMA）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_EZIP"></a>

## 232.14 `CONFIG_USE_SIFLI_HAL_EZIP`

**提示（Prompt）**：SiFli EZIP硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli EZIP硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_GPIO"></a>

## 232.15 `CONFIG_USE_SIFLI_HAL_GPIO`

**提示（Prompt）**：SiFli 通用输入／输出（GPIO）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 通用输入／输出（GPIO）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_GPT"></a>

## 232.16 `CONFIG_USE_SIFLI_HAL_GPT`

**提示（Prompt）**：SiFli 通用定时器（GPT）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 通用定时器（GPT）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_HASH"></a>

## 232.17 `CONFIG_USE_SIFLI_HAL_HASH`

**提示（Prompt）**：SiFli 散列（HASH）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 散列（HASH）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_SF32LB52X && CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_SF32LB52X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SF32LB52X)、[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_SF32LB52X`、`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_HCD"></a>

## 232.18 `CONFIG_USE_SIFLI_HAL_HCD`

**提示（Prompt）**：SiFli 主机控制器（HCD）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 主机控制器（HCD）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_I2C"></a>

## 232.19 `CONFIG_USE_SIFLI_HAL_I2C`

**提示（Prompt）**：SiFli I2C硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli I2C硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:109`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L109)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_I2S"></a>

## 232.20 `CONFIG_USE_SIFLI_HAL_I2S`

**提示（Prompt）**：SiFli 芯片间音频接口（I2S）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 芯片间音频接口（I2S）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:114`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L114)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_LCD"></a>

## 232.21 `CONFIG_USE_SIFLI_HAL_LCD`

**提示（Prompt）**：SiFli 液晶显示（LCD）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 液晶显示（LCD）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_LCPU_CONFIGURE"></a>

## 232.22 `CONFIG_USE_SIFLI_HAL_LCPU_CONFIGURE`

**提示（Prompt）**：SiFli 低功耗核心配置（LCPU_CONFIGURE）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 低功耗核心配置（LCPU_CONFIGURE）硬件抽象层（HAL）模块。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**被选择（Selected by）**

```text
CONFIG_USE_SIFLI_IPC_QUEUE
CONFIG_USE_SIFLI_IPC_QUEUE
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)、[`CONFIG_USE_SIFLI_IPC_QUEUE`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_IPC_QUEUE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_LCPU_PATCH"></a>

## 232.23 `CONFIG_USE_SIFLI_HAL_LCPU_PATCH`

**提示（Prompt）**：SiFli 低功耗核心补丁（LCPU_PATCH）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 低功耗核心补丁（LCPU_PATCH）硬件抽象层（HAL）模块。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**被选择（Selected by）**

```text
CONFIG_USE_SIFLI_IPC_QUEUE
CONFIG_USE_SIFLI_IPC_QUEUE
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:129`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L129)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)、[`CONFIG_USE_SIFLI_IPC_QUEUE`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_IPC_QUEUE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_LPTIM"></a>

## 232.24 `CONFIG_USE_SIFLI_HAL_LPTIM`

**提示（Prompt）**：SiFli 低功耗定时器（LPTIM）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 低功耗定时器（LPTIM）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:139`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L139)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_LRC_CAL"></a>

## 232.25 `CONFIG_USE_SIFLI_HAL_LRC_CAL`

**提示（Prompt）**：SiFli 低频 RC 校准（LRC_CAL）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 低频 RC 校准（LRC_CAL）硬件抽象层（HAL）模块。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:134`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L134)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_MAILBOX"></a>

## 232.26 `CONFIG_USE_SIFLI_HAL_MAILBOX`

**提示（Prompt）**：SiFli 邮箱（MAILBOX）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 邮箱（MAILBOX）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**被选择（Selected by）**

```text
CONFIG_USE_SIFLI_IPC_QUEUE
CONFIG_USE_SIFLI_IPC_QUEUE
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:144`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L144)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)、[`CONFIG_USE_SIFLI_IPC_QUEUE`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_IPC_QUEUE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_MATH"></a>

## 232.27 `CONFIG_USE_SIFLI_HAL_MATH`

**提示（Prompt）**：SiFli 数学运算（MATH）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 数学运算（MATH）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:149`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L149)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_MMC"></a>

## 232.28 `CONFIG_USE_SIFLI_HAL_MMC`

**提示（Prompt）**：SiFli 多媒体卡（MMC）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 多媒体卡（MMC）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:154`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L154)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_MPI"></a>

## 232.29 `CONFIG_USE_SIFLI_HAL_MPI`

**提示（Prompt）**：SiFli MPI硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli MPI硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_SF32LB52X && CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:159`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L159)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_SF32LB52X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SF32LB52X)、[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_SF32LB52X`、`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_PCD"></a>

## 232.30 `CONFIG_USE_SIFLI_HAL_PCD`

**提示（Prompt）**：SiFli 外设控制器（PCD）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 外设控制器（PCD）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:165`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L165)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_PDM"></a>

## 232.31 `CONFIG_USE_SIFLI_HAL_PDM`

**提示（Prompt）**：SiFli 脉冲密度调制（PDM）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 脉冲密度调制（PDM）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:170`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L170)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_PINMUX"></a>

## 232.32 `CONFIG_USE_SIFLI_HAL_PINMUX`

**提示（Prompt）**：SiFli 引脚复用（PINMUX）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 引脚复用（PINMUX）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:175`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L175)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_PTC"></a>

## 232.33 `CONFIG_USE_SIFLI_HAL_PTC`

**提示（Prompt）**：SiFli PTC硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli PTC硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:180`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L180)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_RNG"></a>

## 232.34 `CONFIG_USE_SIFLI_HAL_RNG`

**提示（Prompt）**：SiFli 随机数生成器（RNG）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 随机数生成器（RNG）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:185`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L185)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_RTC"></a>

## 232.35 `CONFIG_USE_SIFLI_HAL_RTC`

**提示（Prompt）**：SiFli 实时时钟（RTC）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 实时时钟（RTC）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:190`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L190)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_SD"></a>

## 232.36 `CONFIG_USE_SIFLI_HAL_SD`

**提示（Prompt）**：SiFli 安全数字卡（SD）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 安全数字卡（SD）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_SF32LB52X && CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:195`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L195)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_SF32LB52X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SF32LB52X)、[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_SF32LB52X`、`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_SDHCI"></a>

## 232.37 `CONFIG_USE_SIFLI_HAL_SDHCI`

**提示（Prompt）**：SiFli 安全数字主机控制器接口（SDHCI）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 安全数字主机控制器接口（SDHCI）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:201`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L201)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_SECU"></a>

## 232.38 `CONFIG_USE_SIFLI_HAL_SECU`

**提示（Prompt）**：SiFli 安全单元（SECU）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 安全单元（SECU）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_SF32LB52X && CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:206`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L206)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_SF32LB52X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SF32LB52X)、[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_SF32LB52X`、`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_SPI"></a>

## 232.39 `CONFIG_USE_SIFLI_HAL_SPI`

**提示（Prompt）**：SiFli 串行外设接口（SPI）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 串行外设接口（SPI）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:212`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L212)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_SYSTEM_CONFIG"></a>

## 232.40 `CONFIG_USE_SIFLI_HAL_SYSTEM_CONFIG`

**提示（Prompt）**：SiFli 系统配置（SYSTEM_CONFIG）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 系统配置（SYSTEM_CONFIG）硬件抽象层（HAL）模块。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:217`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L217)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_TSEN"></a>

## 232.41 `CONFIG_USE_SIFLI_HAL_TSEN`

**提示（Prompt）**：SiFli 温度传感器（TSEN）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 温度传感器（TSEN）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:222`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L222)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_UART"></a>

## 232.42 `CONFIG_USE_SIFLI_HAL_UART`

**提示（Prompt）**：SiFli 通用异步收发器（UART）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 通用异步收发器（UART）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:227`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L227)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_HAL_WDT"></a>

## 232.43 `CONFIG_USE_SIFLI_HAL_WDT`

**提示（Prompt）**：SiFli 看门狗定时器（WDT）硬件抽象层（HAL）模块

**说明（Help）**

启用 SiFli 看门狗定时器（WDT）硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:232`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L232)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<a id="CONFIG_USE_SIFLI_IPC_QUEUE"></a>

## 232.44 `CONFIG_USE_SIFLI_IPC_QUEUE`

**提示（Prompt）**：IPC_QUEUE：SiFli 进程间通信队列（IPC queue）

**说明（Help）**

启用用于 SiFli 核心间通信（core communication）的 IPC 队列模块。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SIFLI_HAL && CONFIG_HAS_SIFLI_HAL
```

**主动选择（Selects）**

```text
CONFIG_USE_SIFLI_HAL_MAILBOX
CONFIG_USE_SIFLI_HAL_LCPU_CONFIGURE
CONFIG_USE_SIFLI_HAL_LCPU_PATCH
CONFIG_USE_SIFLI_HAL_AON
```

**被选择（Selected by）**

```text
CONFIG_BT_SF32LB
```

**定义位置（Location）**：[`modules/hal_sifli/Kconfig:237`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_sifli/Kconfig#L237)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_sifli（模块路径 `modules/hal/sifli`，相对于 west 工作区顶层目录） → SiFli 硬件抽象层（HAL）

**配置项引用（Symbol References）**：[`CONFIG_USE_SIFLI_HAL`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL)、[`CONFIG_HAS_SIFLI_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SIFLI_HAL)、[`CONFIG_USE_SIFLI_HAL_MAILBOX`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL_MAILBOX)、[`CONFIG_USE_SIFLI_HAL_LCPU_CONFIGURE`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL_LCPU_CONFIGURE)、[`CONFIG_USE_SIFLI_HAL_LCPU_PATCH`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL_LCPU_PATCH)、[`CONFIG_USE_SIFLI_HAL_AON`](P232_modules_hal_sifli_配置项参考.md#CONFIG_USE_SIFLI_HAL_AON)、[`CONFIG_BT_SF32LB`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_SF32LB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SIFLI_HAL`。

<!-- kconfig-navigation -->

[上一章](P231_modules_hal_rpi_pico_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P233_modules_hal_silabs_配置项参考.md)
