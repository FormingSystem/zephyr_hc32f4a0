---
id: learning.zephyr-docs.kconfig-reference.page-202
title: "`modules/Kconfig.infineon`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第202章\_`modules/Kconfig.infineon`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/Kconfig.infineon` 的 13 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_HAS_XMCLIB_CAN"></a>

## 202.1 `CONFIG_HAS_XMCLIB_CAN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 XMCLIB 控制器局域网（CAN）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_XMCLIB
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_XMC4XXX
```

**定义位置（Location）**：[`modules/Kconfig.infineon:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.infineon#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_XMCLIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_XMCLIB)、[`CONFIG_SOC_SERIES_XMC4XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XMC4XXX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_XMCLIB`。

<a id="CONFIG_HAS_XMCLIB_CCU"></a>

## 202.2 `CONFIG_HAS_XMCLIB_CCU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 XMCLIB 捕获／比较单元（CCU4／CCU8）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_XMCLIB
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_XMC4XXX
```

**定义位置（Location）**：[`modules/Kconfig.infineon:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.infineon#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_XMCLIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_XMCLIB)、[`CONFIG_SOC_SERIES_XMC4XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XMC4XXX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_XMCLIB`。

<a id="CONFIG_HAS_XMCLIB_DMA"></a>

## 202.3 `CONFIG_HAS_XMCLIB_DMA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 XMCLIB 直接内存访问（DMA）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_XMCLIB
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_XMC4XXX
```

**定义位置（Location）**：[`modules/Kconfig.infineon:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.infineon#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_XMCLIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_XMCLIB)、[`CONFIG_SOC_SERIES_XMC4XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XMC4XXX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_XMCLIB`。

<a id="CONFIG_HAS_XMCLIB_ECAT"></a>

## 202.4 `CONFIG_HAS_XMCLIB_ECAT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 XMCLIB EtherCAT 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_XMCLIB
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_XMC4XXX
```

**定义位置（Location）**：[`modules/Kconfig.infineon:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.infineon#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_XMCLIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_XMCLIB)、[`CONFIG_SOC_SERIES_XMC4XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XMC4XXX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_XMCLIB`。

<a id="CONFIG_HAS_XMCLIB_ERU"></a>

## 202.5 `CONFIG_HAS_XMCLIB_ERU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 XMCLIB 事件请求单元（Event Request Unit，ERU），以支持 GPIO 中断。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_XMCLIB
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_XMC4XXX
```

**定义位置（Location）**：[`modules/Kconfig.infineon:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.infineon#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_XMCLIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_XMCLIB)、[`CONFIG_SOC_SERIES_XMC4XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XMC4XXX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_XMCLIB`。

<a id="CONFIG_HAS_XMCLIB_ETH"></a>

## 202.6 `CONFIG_HAS_XMCLIB_ETH`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 XMCLIB 以太网媒体访问控制器（Ethernet MAC）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_XMCLIB
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_XMC4XXX
```

**定义位置（Location）**：[`modules/Kconfig.infineon:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.infineon#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_XMCLIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_XMCLIB)、[`CONFIG_SOC_SERIES_XMC4XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XMC4XXX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_XMCLIB`。

<a id="CONFIG_HAS_XMCLIB_FLASH"></a>

## 202.7 `CONFIG_HAS_XMCLIB_FLASH`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 XMCLIB 闪存（Flash）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_XMCLIB
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_XMC4XXX
```

**定义位置（Location）**：[`modules/Kconfig.infineon:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.infineon#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_XMCLIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_XMCLIB)、[`CONFIG_SOC_SERIES_XMC4XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XMC4XXX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_XMCLIB`。

<a id="CONFIG_HAS_XMCLIB_I2C"></a>

## 202.8 `CONFIG_HAS_XMCLIB_I2C`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 XMCLIB I2C 总线支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_XMCLIB
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_XMC4XXX
```

**定义位置（Location）**：[`modules/Kconfig.infineon:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.infineon#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_XMCLIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_XMCLIB)、[`CONFIG_SOC_SERIES_XMC4XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XMC4XXX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_XMCLIB`。

<a id="CONFIG_HAS_XMCLIB_RTC"></a>

## 202.9 `CONFIG_HAS_XMCLIB_RTC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 XMCLIB 实时时钟（RTC）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_XMCLIB
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_XMC4XXX
```

**定义位置（Location）**：[`modules/Kconfig.infineon:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.infineon#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_XMCLIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_XMCLIB)、[`CONFIG_SOC_SERIES_XMC4XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XMC4XXX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_XMCLIB`。

<a id="CONFIG_HAS_XMCLIB_SPI"></a>

## 202.10 `CONFIG_HAS_XMCLIB_SPI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 XMCLIB 串行外设接口（SPI）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_XMCLIB
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_XMC4XXX
```

**定义位置（Location）**：[`modules/Kconfig.infineon:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.infineon#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_XMCLIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_XMCLIB)、[`CONFIG_SOC_SERIES_XMC4XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XMC4XXX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_XMCLIB`。

<a id="CONFIG_HAS_XMCLIB_UART"></a>

## 202.11 `CONFIG_HAS_XMCLIB_UART`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 XMCLIB 通用异步收发器（Universal Asynchronous Receiver Transmitter，UART）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_XMCLIB
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_XMC4XXX
```

**定义位置（Location）**：[`modules/Kconfig.infineon:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.infineon#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_XMCLIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_XMCLIB)、[`CONFIG_SOC_SERIES_XMC4XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XMC4XXX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_XMCLIB`。

<a id="CONFIG_HAS_XMCLIB_VADC"></a>

## 202.12 `CONFIG_HAS_XMCLIB_VADC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 XMCLIB VADC 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_XMCLIB
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_XMC4XXX
```

**定义位置（Location）**：[`modules/Kconfig.infineon:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.infineon#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_XMCLIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_XMCLIB)、[`CONFIG_SOC_SERIES_XMC4XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XMC4XXX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_XMCLIB`。

<a id="CONFIG_HAS_XMCLIB_WDT"></a>

## 202.13 `CONFIG_HAS_XMCLIB_WDT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 XMCLIB 看门狗定时器（WDT）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_XMCLIB
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_XMC4XXX
```

**定义位置（Location）**：[`modules/Kconfig.infineon:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.infineon#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_XMCLIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_XMCLIB)、[`CONFIG_SOC_SERIES_XMC4XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XMC4XXX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_XMCLIB`。

<!-- kconfig-navigation -->

[上一章](P201_modules_Kconfig.esp32_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P203_modules_Kconfig.intel_配置项参考.md)
