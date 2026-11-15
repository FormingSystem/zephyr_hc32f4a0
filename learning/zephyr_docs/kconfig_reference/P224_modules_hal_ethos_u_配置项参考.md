---
id: learning.zephyr-docs.kconfig-reference.page-224
title: "`modules/hal_ethos_u`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第224章\_`modules/hal_ethos_u`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/hal_ethos_u` 的 21 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ETHOS_U"></a>

## 224.1 `CONFIG_ETHOS_U`

**提示（Prompt）**：Ethos-U 核心驱动（core driver）

**说明（Help）**

启用 Arm Ethos-U 核心驱动（core driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MULTITHREADING
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`modules/hal_ethos_u/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ethos_u/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ethos_u（模块路径 `modules/hal/ethos_u`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)。

<a id="CONFIG_ETHOS_U55_128"></a>

## 224.2 `CONFIG_ETHOS_U55_128`

**提示（Prompt）**：使用具有 128 个乘加单元（MACs）的 Ethos-U55

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ETHOS_U_NPU_CONFIG>
```

**定义位置（Location）**：[`modules/hal_ethos_u/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ethos_u/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ethos_u（模块路径 `modules/hal/ethos_u`，相对于 west 工作区顶层目录） → Ethos-U 核心驱动（core driver） → Ethos-U 神经网络处理单元（NPU）配置 → Ethos-U 神经网络处理单元（NPU）配置

**配置项引用（Symbol References）**：[`CONFIG_ETHOS_U_NPU_CONFIG`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U_NPU_CONFIG)。

<a id="CONFIG_ETHOS_U55_256"></a>

## 224.3 `CONFIG_ETHOS_U55_256`

**提示（Prompt）**：使用具有 256 个乘加单元（MACs）的 Ethos-U55

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ETHOS_U_NPU_CONFIG>
```

**定义位置（Location）**：[`modules/hal_ethos_u/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ethos_u/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ethos_u（模块路径 `modules/hal/ethos_u`，相对于 west 工作区顶层目录） → Ethos-U 核心驱动（core driver） → Ethos-U 神经网络处理单元（NPU）配置 → Ethos-U 神经网络处理单元（NPU）配置

**配置项引用（Symbol References）**：[`CONFIG_ETHOS_U_NPU_CONFIG`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U_NPU_CONFIG)。

<a id="CONFIG_ETHOS_U55_64"></a>

## 224.4 `CONFIG_ETHOS_U55_64`

**提示（Prompt）**：使用具有 64 个乘加单元（MACs）的 Ethos-U55

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ETHOS_U_NPU_CONFIG>
```

**定义位置（Location）**：[`modules/hal_ethos_u/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ethos_u/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ethos_u（模块路径 `modules/hal/ethos_u`，相对于 west 工作区顶层目录） → Ethos-U 核心驱动（core driver） → Ethos-U 神经网络处理单元（NPU）配置 → Ethos-U 神经网络处理单元（NPU）配置

**配置项引用（Symbol References）**：[`CONFIG_ETHOS_U_NPU_CONFIG`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U_NPU_CONFIG)。

<a id="CONFIG_ETHOS_U65_128"></a>

## 224.5 `CONFIG_ETHOS_U65_128`

**提示（Prompt）**：使用具有 128 个乘加单元（MACs）的 Ethos-U65

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ETHOS_U_NPU_CONFIG>
```

**定义位置（Location）**：[`modules/hal_ethos_u/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ethos_u/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ethos_u（模块路径 `modules/hal/ethos_u`，相对于 west 工作区顶层目录） → Ethos-U 核心驱动（core driver） → Ethos-U 神经网络处理单元（NPU）配置 → Ethos-U 神经网络处理单元（NPU）配置

**配置项引用（Symbol References）**：[`CONFIG_ETHOS_U_NPU_CONFIG`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U_NPU_CONFIG)。

<a id="CONFIG_ETHOS_U65_256"></a>

## 224.6 `CONFIG_ETHOS_U65_256`

**提示（Prompt）**：使用具有 256 个乘加单元（MACs）的 Ethos-U65

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ETHOS_U_NPU_CONFIG>
```

**定义位置（Location）**：[`modules/hal_ethos_u/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ethos_u/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ethos_u（模块路径 `modules/hal/ethos_u`，相对于 west 工作区顶层目录） → Ethos-U 核心驱动（core driver） → Ethos-U 神经网络处理单元（NPU）配置 → Ethos-U 神经网络处理单元（NPU）配置

**配置项引用（Symbol References）**：[`CONFIG_ETHOS_U_NPU_CONFIG`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U_NPU_CONFIG)。

<a id="CONFIG_ETHOS_U65_512"></a>

## 224.7 `CONFIG_ETHOS_U65_512`

**提示（Prompt）**：使用具有 512 个乘加单元（MACs）的 Ethos-U65

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ETHOS_U_NPU_CONFIG>
```

**定义位置（Location）**：[`modules/hal_ethos_u/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ethos_u/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ethos_u（模块路径 `modules/hal/ethos_u`，相对于 west 工作区顶层目录） → Ethos-U 核心驱动（core driver） → Ethos-U 神经网络处理单元（NPU）配置 → Ethos-U 神经网络处理单元（NPU）配置

**配置项引用（Symbol References）**：[`CONFIG_ETHOS_U_NPU_CONFIG`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U_NPU_CONFIG)。

<a id="CONFIG_ETHOS_U85_1024"></a>

## 224.8 `CONFIG_ETHOS_U85_1024`

**提示（Prompt）**：使用具有 1024 个乘加单元（MACs）的 Ethos-U85

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ETHOS_U_NPU_CONFIG>
```

**定义位置（Location）**：[`modules/hal_ethos_u/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ethos_u/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ethos_u（模块路径 `modules/hal/ethos_u`，相对于 west 工作区顶层目录） → Ethos-U 核心驱动（core driver） → Ethos-U 神经网络处理单元（NPU）配置 → Ethos-U 神经网络处理单元（NPU）配置

**配置项引用（Symbol References）**：[`CONFIG_ETHOS_U_NPU_CONFIG`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U_NPU_CONFIG)。

<a id="CONFIG_ETHOS_U85_128"></a>

## 224.9 `CONFIG_ETHOS_U85_128`

**提示（Prompt）**：使用具有 128 个乘加单元（MACs）的 Ethos-U85

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ETHOS_U_NPU_CONFIG>
```

**定义位置（Location）**：[`modules/hal_ethos_u/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ethos_u/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ethos_u（模块路径 `modules/hal/ethos_u`，相对于 west 工作区顶层目录） → Ethos-U 核心驱动（core driver） → Ethos-U 神经网络处理单元（NPU）配置 → Ethos-U 神经网络处理单元（NPU）配置

**配置项引用（Symbol References）**：[`CONFIG_ETHOS_U_NPU_CONFIG`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U_NPU_CONFIG)。

<a id="CONFIG_ETHOS_U85_2048"></a>

## 224.10 `CONFIG_ETHOS_U85_2048`

**提示（Prompt）**：使用具有 2048 个乘加单元（MACs）的 Ethos-U85

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ETHOS_U_NPU_CONFIG>
```

**定义位置（Location）**：[`modules/hal_ethos_u/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ethos_u/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ethos_u（模块路径 `modules/hal/ethos_u`，相对于 west 工作区顶层目录） → Ethos-U 核心驱动（core driver） → Ethos-U 神经网络处理单元（NPU）配置 → Ethos-U 神经网络处理单元（NPU）配置

**配置项引用（Symbol References）**：[`CONFIG_ETHOS_U_NPU_CONFIG`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U_NPU_CONFIG)。

<a id="CONFIG_ETHOS_U85_256"></a>

## 224.11 `CONFIG_ETHOS_U85_256`

**提示（Prompt）**：使用具有 256 个乘加单元（MACs）的 Ethos-U85

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ETHOS_U_NPU_CONFIG>
```

**定义位置（Location）**：[`modules/hal_ethos_u/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ethos_u/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ethos_u（模块路径 `modules/hal/ethos_u`，相对于 west 工作区顶层目录） → Ethos-U 核心驱动（core driver） → Ethos-U 神经网络处理单元（NPU）配置 → Ethos-U 神经网络处理单元（NPU）配置

**配置项引用（Symbol References）**：[`CONFIG_ETHOS_U_NPU_CONFIG`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U_NPU_CONFIG)。

<a id="CONFIG_ETHOS_U85_512"></a>

## 224.12 `CONFIG_ETHOS_U85_512`

**提示（Prompt）**：使用具有 512 个乘加单元（MACs）的 Ethos-U85

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ETHOS_U_NPU_CONFIG>
```

**定义位置（Location）**：[`modules/hal_ethos_u/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ethos_u/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ethos_u（模块路径 `modules/hal/ethos_u`，相对于 west 工作区顶层目录） → Ethos-U 核心驱动（core driver） → Ethos-U 神经网络处理单元（NPU）配置 → Ethos-U 神经网络处理单元（NPU）配置

**配置项引用（Symbol References）**：[`CONFIG_ETHOS_U_NPU_CONFIG`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U_NPU_CONFIG)。

<a id="CONFIG_ETHOS_U_LOG_LEVEL_CHOICE"></a>

## 224.13 `CONFIG_ETHOS_U_LOG_LEVEL_CHOICE`

**提示（Prompt）**：ETHOS_U 编译包含的最高日志级别（Max compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_ETHOS_U
```

**默认值（Defaults）**

```text
CONFIG_ETHOS_U_LOG_LEVEL_WRN
```

**可选项（Choices）**

```text
CONFIG_ETHOS_U_LOG_LEVEL_NONE
CONFIG_ETHOS_U_LOG_LEVEL_ERR
CONFIG_ETHOS_U_LOG_LEVEL_WRN
CONFIG_ETHOS_U_LOG_LEVEL_INF
CONFIG_ETHOS_U_LOG_LEVEL_DBG
CONFIG_ETHOS_U_LOG_LEVEL_DEFAULT
CONFIG_ETHOS_U_LOG_LEVEL_NONE
CONFIG_ETHOS_U_LOG_LEVEL_ERR
CONFIG_ETHOS_U_LOG_LEVEL_WRN
CONFIG_ETHOS_U_LOG_LEVEL_INF
CONFIG_ETHOS_U_LOG_LEVEL_DBG
CONFIG_ETHOS_U_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`modules/hal_ethos_u/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ethos_u/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ethos_u（模块路径 `modules/hal/ethos_u`，相对于 west 工作区顶层目录） → Ethos-U 核心驱动（core driver）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_ETHOS_U`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U)、[`CONFIG_ETHOS_U_LOG_LEVEL_WRN`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U_LOG_LEVEL_WRN)、[`CONFIG_ETHOS_U_LOG_LEVEL_NONE`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U_LOG_LEVEL_NONE)、[`CONFIG_ETHOS_U_LOG_LEVEL_ERR`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U_LOG_LEVEL_ERR)、[`CONFIG_ETHOS_U_LOG_LEVEL_INF`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U_LOG_LEVEL_INF)、[`CONFIG_ETHOS_U_LOG_LEVEL_DBG`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U_LOG_LEVEL_DBG)、[`CONFIG_ETHOS_U_LOG_LEVEL_DEFAULT`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U_LOG_LEVEL_DEFAULT)。

<a id="CONFIG_ETHOS_U_LOG_LEVEL_DBG"></a>

## 224.14 `CONFIG_ETHOS_U_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ETHOS_U_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`modules/hal_ethos_u/Kconfig:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ethos_u/Kconfig#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ethos_u（模块路径 `modules/hal/ethos_u`，相对于 west 工作区顶层目录） → Ethos-U 核心驱动（core driver） → ETHOS_U 编译包含的最高日志级别（Max compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ETHOS_U_LOG_LEVEL_CHOICE`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ETHOS_U_LOG_LEVEL_DEFAULT"></a>

## 224.15 `CONFIG_ETHOS_U_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ETHOS_U_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`modules/hal_ethos_u/Kconfig:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ethos_u/Kconfig#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ethos_u（模块路径 `modules/hal/ethos_u`，相对于 west 工作区顶层目录） → Ethos-U 核心驱动（core driver） → ETHOS_U 编译包含的最高日志级别（Max compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ETHOS_U_LOG_LEVEL_CHOICE`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ETHOS_U_LOG_LEVEL_ERR"></a>

## 224.16 `CONFIG_ETHOS_U_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ETHOS_U_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`modules/hal_ethos_u/Kconfig:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ethos_u/Kconfig#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ethos_u（模块路径 `modules/hal/ethos_u`，相对于 west 工作区顶层目录） → Ethos-U 核心驱动（core driver） → ETHOS_U 编译包含的最高日志级别（Max compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ETHOS_U_LOG_LEVEL_CHOICE`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ETHOS_U_LOG_LEVEL_INF"></a>

## 224.17 `CONFIG_ETHOS_U_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ETHOS_U_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`modules/hal_ethos_u/Kconfig:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ethos_u/Kconfig#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ethos_u（模块路径 `modules/hal/ethos_u`，相对于 west 工作区顶层目录） → Ethos-U 核心驱动（core driver） → ETHOS_U 编译包含的最高日志级别（Max compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ETHOS_U_LOG_LEVEL_CHOICE`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ETHOS_U_LOG_LEVEL_NONE"></a>

## 224.18 `CONFIG_ETHOS_U_LOG_LEVEL_NONE`

**提示（Prompt）**：无（None）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ETHOS_U_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`modules/hal_ethos_u/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ethos_u/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ethos_u（模块路径 `modules/hal/ethos_u`，相对于 west 工作区顶层目录） → Ethos-U 核心驱动（core driver） → ETHOS_U 编译包含的最高日志级别（Max compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ETHOS_U_LOG_LEVEL_CHOICE`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ETHOS_U_LOG_LEVEL_WRN"></a>

## 224.19 `CONFIG_ETHOS_U_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ETHOS_U_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`modules/hal_ethos_u/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ethos_u/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ethos_u（模块路径 `modules/hal/ethos_u`，相对于 west 工作区顶层目录） → Ethos-U 核心驱动（core driver） → ETHOS_U 编译包含的最高日志级别（Max compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ETHOS_U_LOG_LEVEL_CHOICE`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ETHOS_U_NPU_CONFIG"></a>

## 224.20 `CONFIG_ETHOS_U_NPU_CONFIG`

**提示（Prompt）**：Ethos-U 神经网络处理单元（NPU）配置

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETHOS_U
```

**默认值（Defaults）**

```text
CONFIG_ETHOS_U55_128 if CONFIG_SOC_SERIES_MPS3
CONFIG_ETHOS_U65_256 if CONFIG_SOC_CORSTONE315
CONFIG_ETHOS_U85_256 if CONFIG_SOC_CORSTONE320
CONFIG_ETHOS_U55_256 if CONFIG_SOC_SERIES_M55M1X
CONFIG_ETHOS_U55_128 if CONFIG_SOC_SERIES_PSE84
```

**可选项（Choices）**

```text
CONFIG_ETHOS_U55_64
CONFIG_ETHOS_U55_128
CONFIG_ETHOS_U55_256
CONFIG_ETHOS_U65_128
CONFIG_ETHOS_U65_256
CONFIG_ETHOS_U65_512
CONFIG_ETHOS_U85_128
CONFIG_ETHOS_U85_256
CONFIG_ETHOS_U85_512
CONFIG_ETHOS_U85_1024
CONFIG_ETHOS_U85_2048
CONFIG_ETHOS_U55_64
CONFIG_ETHOS_U55_128
CONFIG_ETHOS_U55_256
CONFIG_ETHOS_U65_128
CONFIG_ETHOS_U65_256
CONFIG_ETHOS_U65_512
CONFIG_ETHOS_U85_128
CONFIG_ETHOS_U85_256
CONFIG_ETHOS_U85_512
CONFIG_ETHOS_U85_1024
CONFIG_ETHOS_U85_2048
```

**定义位置（Location）**：[`modules/hal_ethos_u/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ethos_u/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ethos_u（模块路径 `modules/hal/ethos_u`，相对于 west 工作区顶层目录） → Ethos-U 核心驱动（core driver） → Ethos-U 神经网络处理单元（NPU）配置

**配置项引用（Symbol References）**：[`CONFIG_ETHOS_U`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U)、[`CONFIG_ETHOS_U55_128`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U55_128)、[`CONFIG_SOC_SERIES_MPS3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MPS3)、[`CONFIG_ETHOS_U65_256`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U65_256)、[`CONFIG_SOC_CORSTONE315`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE315)、[`CONFIG_ETHOS_U85_256`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U85_256)、[`CONFIG_SOC_CORSTONE320`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE320)、[`CONFIG_ETHOS_U55_256`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U55_256)、[`CONFIG_SOC_SERIES_M55M1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M55M1X)、[`CONFIG_SOC_SERIES_PSE84`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSE84)、[`CONFIG_ETHOS_U55_64`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U55_64)、[`CONFIG_ETHOS_U65_128`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U65_128)、[`CONFIG_ETHOS_U65_512`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U65_512)、[`CONFIG_ETHOS_U85_128`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U85_128)、[`CONFIG_ETHOS_U85_512`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U85_512)、[`CONFIG_ETHOS_U85_1024`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U85_1024)、[`CONFIG_ETHOS_U85_2048`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U85_2048)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_CORSTONE315`、`CONFIG_SOC_CORSTONE320`、`CONFIG_SOC_SERIES_PSE84`。

<a id="CONFIG_ETHOS_U_NPU_NAME"></a>

## 224.21 `CONFIG_ETHOS_U_NPU_NAME`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

所使用的 Ethos-U 神经网络处理单元（NPU）名称

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_ETHOS_U
```

**默认值（Defaults）**

```text
"ethos-u55-64" if CONFIG_ETHOS_U55_64
"ethos-u55-128" if CONFIG_ETHOS_U55_128
"ethos-u55-256" if CONFIG_ETHOS_U55_256
"ethos-u65-128" if CONFIG_ETHOS_U65_128
"ethos-u65-256" if CONFIG_ETHOS_U65_256
"ethos-u65-512" if CONFIG_ETHOS_U65_512
"ethos-u85-128" if CONFIG_ETHOS_U85_128
"ethos-u85-256" if CONFIG_ETHOS_U85_256
"ethos-u85-512" if CONFIG_ETHOS_U85_512
"ethos-u85-1024" if CONFIG_ETHOS_U85_1024
"ethos-u85-2048" if CONFIG_ETHOS_U85_2048
```

**定义位置（Location）**：[`modules/hal_ethos_u/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_ethos_u/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_ethos_u（模块路径 `modules/hal/ethos_u`，相对于 west 工作区顶层目录） → Ethos-U 核心驱动（core driver）

**配置项引用（Symbol References）**：[`CONFIG_ETHOS_U`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U)、[`CONFIG_ETHOS_U55_64`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U55_64)、[`CONFIG_ETHOS_U55_128`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U55_128)、[`CONFIG_ETHOS_U55_256`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U55_256)、[`CONFIG_ETHOS_U65_128`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U65_128)、[`CONFIG_ETHOS_U65_256`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U65_256)、[`CONFIG_ETHOS_U65_512`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U65_512)、[`CONFIG_ETHOS_U85_128`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U85_128)、[`CONFIG_ETHOS_U85_256`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U85_256)、[`CONFIG_ETHOS_U85_512`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U85_512)、[`CONFIG_ETHOS_U85_1024`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U85_1024)、[`CONFIG_ETHOS_U85_2048`](P224_modules_hal_ethos_u_配置项参考.md#CONFIG_ETHOS_U85_2048)。

<!-- kconfig-navigation -->

[上一章](P223_modules_hal_bouffalolab_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P225_modules_hal_gigadevice_配置项参考.md)
