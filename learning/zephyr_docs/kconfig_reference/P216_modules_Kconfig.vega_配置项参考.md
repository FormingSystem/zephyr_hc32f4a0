---
id: learning.zephyr-docs.kconfig-reference.page-216
title: "`modules/Kconfig.vega`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第216章\_`modules/Kconfig.vega`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/Kconfig.vega` 的 6 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_HAS_RV32M1_FTFX"></a>

## 216.1 `CONFIG_HAS_RV32M1_FTFX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

SoC 中存在闪存模块（flash memory module，FTFA、FTFE 或 FTFL）时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_OPENISA_RV32M1
```

**定义位置（Location）**：[`modules/Kconfig.vega:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.vega#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_SOC_OPENISA_RV32M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_OPENISA_RV32M1)。

<a id="CONFIG_HAS_RV32M1_LPI2C"></a>

## 216.2 `CONFIG_HAS_RV32M1_LPI2C`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

SoC 中存在低功耗 I2C（LPI2C）模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_OPENISA_RV32M1
```

**定义位置（Location）**：[`modules/Kconfig.vega:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.vega#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_SOC_OPENISA_RV32M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_OPENISA_RV32M1)。

<a id="CONFIG_HAS_RV32M1_LPSPI"></a>

## 216.3 `CONFIG_HAS_RV32M1_LPSPI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

SoC 中存在低功耗 SPI（LPSPI）模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_OPENISA_RV32M1
```

**定义位置（Location）**：[`modules/Kconfig.vega:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.vega#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_SOC_OPENISA_RV32M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_OPENISA_RV32M1)。

<a id="CONFIG_HAS_RV32M1_LPUART"></a>

## 216.4 `CONFIG_HAS_RV32M1_LPUART`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

SoC 中存在低功耗 UART（LPUART）模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_OPENISA_RV32M1
```

**定义位置（Location）**：[`modules/Kconfig.vega:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.vega#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_SOC_OPENISA_RV32M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_OPENISA_RV32M1)。

<a id="CONFIG_HAS_RV32M1_TPM"></a>

## 216.5 `CONFIG_HAS_RV32M1_TPM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

SoC 中存在定时器／脉宽调制（Timer/PWM，TPM）模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_OPENISA_RV32M1
```

**定义位置（Location）**：[`modules/Kconfig.vega:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.vega#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_SOC_OPENISA_RV32M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_OPENISA_RV32M1)。

<a id="CONFIG_VEGA_SDK_HAL"></a>

## 216.6 `CONFIG_VEGA_SDK_HAL`

**提示（Prompt）**：RV32M1 VEGA 软件开发工具包（SDK）支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_OPENISA_RV32M1
```

**被选择（Selected by）**

```text
CONFIG_SOC_OPENISA_RV32M1
```

**定义位置（Location）**：[`modules/Kconfig.vega:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.vega#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_SOC_OPENISA_RV32M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_OPENISA_RV32M1)。

<!-- kconfig-navigation -->

[上一章](P215_modules_Kconfig.telink_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P217_modules_Kconfig.xtensa_配置项参考.md)
