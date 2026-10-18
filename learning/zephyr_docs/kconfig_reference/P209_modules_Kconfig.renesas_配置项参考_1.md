---
id: learning.zephyr-docs.kconfig-reference.page-209
title: "`modules/Kconfig.renesas`配置项参考（1/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第209章\_`modules/Kconfig.renesas`配置项参考（1/2）

本章翻译官方 Kconfig 数据库中 `modules/Kconfig.renesas` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_HAS_RENESAS_RA_FSP"></a>

## 209.1 `CONFIG_HAS_RENESAS_RA_FSP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用瑞萨（Renesas）RA 灵活软件包（Flexible Software Package，FSP）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_RA0E1
CONFIG_SOC_SERIES_RA2A1
CONFIG_SOC_SERIES_RA2L1
CONFIG_SOC_SERIES_RA4C1
CONFIG_SOC_SERIES_RA4E1
CONFIG_SOC_SERIES_RA4E2
CONFIG_SOC_SERIES_RA4L1
CONFIG_SOC_SERIES_RA4M1
CONFIG_SOC_SERIES_RA4M2
CONFIG_SOC_SERIES_RA4M3
CONFIG_SOC_SERIES_RA4T1
CONFIG_SOC_SERIES_RA4W1
CONFIG_SOC_SERIES_RA6E1
CONFIG_SOC_SERIES_RA6E2
CONFIG_SOC_SERIES_RA6M1
CONFIG_SOC_SERIES_RA6M2
CONFIG_SOC_SERIES_RA6M3
CONFIG_SOC_SERIES_RA6M4
CONFIG_SOC_SERIES_RA6M5
CONFIG_SOC_SERIES_RA8D1
CONFIG_SOC_SERIES_RA8D2
CONFIG_SOC_SERIES_RA8E1
CONFIG_SOC_SERIES_RA8M1
CONFIG_SOC_SERIES_RA8M2
CONFIG_SOC_SERIES_RA8P1
CONFIG_SOC_SERIES_RA8T1
CONFIG_SOC_SERIES_RA8T2
```

**定义位置（Location）**：[`modules/Kconfig.renesas:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA0E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA0E1)、[`CONFIG_SOC_SERIES_RA2A1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA2A1)、[`CONFIG_SOC_SERIES_RA2L1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA2L1)、[`CONFIG_SOC_SERIES_RA4C1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4C1)、[`CONFIG_SOC_SERIES_RA4E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4E1)、[`CONFIG_SOC_SERIES_RA4E2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4E2)、[`CONFIG_SOC_SERIES_RA4L1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4L1)、[`CONFIG_SOC_SERIES_RA4M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M1)、[`CONFIG_SOC_SERIES_RA4M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M2)、[`CONFIG_SOC_SERIES_RA4M3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M3)、[`CONFIG_SOC_SERIES_RA4T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4T1)、[`CONFIG_SOC_SERIES_RA4W1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4W1)、[`CONFIG_SOC_SERIES_RA6E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6E1)、[`CONFIG_SOC_SERIES_RA6E2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6E2)、[`CONFIG_SOC_SERIES_RA6M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M1)、[`CONFIG_SOC_SERIES_RA6M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M2)、[`CONFIG_SOC_SERIES_RA6M3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M3)、[`CONFIG_SOC_SERIES_RA6M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M4)、[`CONFIG_SOC_SERIES_RA6M5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M5)、[`CONFIG_SOC_SERIES_RA8D1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8D1)、[`CONFIG_SOC_SERIES_RA8D2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8D2)、[`CONFIG_SOC_SERIES_RA8E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8E1)、[`CONFIG_SOC_SERIES_RA8M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8M1)、[`CONFIG_SOC_SERIES_RA8M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8M2)、[`CONFIG_SOC_SERIES_RA8P1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8P1)、[`CONFIG_SOC_SERIES_RA8T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8T1)、[`CONFIG_SOC_SERIES_RA8T2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8T2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_RA2L1`。

<a id="CONFIG_HAS_RENESAS_RA_RSIP_E11A"></a>

## 209.2 `CONFIG_HAS_RENESAS_RA_RSIP_E11A`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为 SCE 驱动包含 RSIP-E11A 实现（implementation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_RA_FSP_SCE && CONFIG_HAS_RENESAS_RA_FSP
```

**定义位置（Location）**：[`modules/Kconfig.renesas:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_USE_RA_FSP_SCE`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_USE_RA_FSP_SCE)、[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)。

<a id="CONFIG_HAS_RENESAS_RA_RSIP_E31A"></a>

## 209.3 `CONFIG_HAS_RENESAS_RA_RSIP_E31A`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为 SCE 驱动包含 RSIP-E31A 实现（implementation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_RA_FSP_SCE && CONFIG_HAS_RENESAS_RA_FSP
```

**定义位置（Location）**：[`modules/Kconfig.renesas:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_USE_RA_FSP_SCE`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_USE_RA_FSP_SCE)、[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)。

<a id="CONFIG_HAS_RENESAS_RA_RSIP_E50D"></a>

## 209.4 `CONFIG_HAS_RENESAS_RA_RSIP_E50D`

原库同名定义共 2 条；本项为数据库第 7315 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为 SCE 驱动包含 RSIP-E50D 实现（implementation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_RA_FSP_SCE && CONFIG_HAS_RENESAS_RA_FSP
```

**定义位置（Location）**：[`modules/Kconfig.renesas:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_USE_RA_FSP_SCE`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_USE_RA_FSP_SCE)、[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)。

<a id="CONFIG_HAS_RENESAS_RA_RSIP_E50D--record-7316"></a>

## 209.5 `CONFIG_HAS_RENESAS_RA_RSIP_E50D`

原库同名定义共 2 条；本项为数据库第 7316 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为 SCE 驱动包含 RSIP-E50D 实现（implementation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_RSIP_E50D_TRNG_ENABLED && CONFIG_USE_RA_FSP_SCE && CONFIG_HAS_RENESAS_RA_FSP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/Kconfig.renesas:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_USE_RA_FSP_SCE`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_USE_RA_FSP_SCE)、[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)。

<a id="CONFIG_HAS_RENESAS_RA_RSIP_E51A"></a>

## 209.6 `CONFIG_HAS_RENESAS_RA_RSIP_E51A`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为 SCE 驱动包含 RSIP-E51A 实现（implementation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_RSIP_E51A_TRNG_ENABLED && CONFIG_USE_RA_FSP_SCE && CONFIG_HAS_RENESAS_RA_FSP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/Kconfig.renesas:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_USE_RA_FSP_SCE`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_USE_RA_FSP_SCE)、[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)。

<a id="CONFIG_HAS_RENESAS_RA_SCE5"></a>

## 209.7 `CONFIG_HAS_RENESAS_RA_SCE5`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为 SCE 驱动包含 SCE5 实现（implementation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_SCE5_RNG_ENABLED && CONFIG_USE_RA_FSP_SCE && CONFIG_HAS_RENESAS_RA_FSP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/Kconfig.renesas:138`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L138)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_USE_RA_FSP_SCE`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_USE_RA_FSP_SCE)、[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)。

<a id="CONFIG_HAS_RENESAS_RA_SCE7"></a>

## 209.8 `CONFIG_HAS_RENESAS_RA_SCE7`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为 SCE 驱动包含 SCE7 实现（implementation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_SCE7_RNG_ENABLED && CONFIG_USE_RA_FSP_SCE && CONFIG_HAS_RENESAS_RA_FSP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/Kconfig.renesas:131`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L131)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_USE_RA_FSP_SCE`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_USE_RA_FSP_SCE)、[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)。

<a id="CONFIG_HAS_RENESAS_RA_SCE9"></a>

## 209.9 `CONFIG_HAS_RENESAS_RA_SCE9`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为 SCE 驱动包含 SCE9 实现（implementation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_SCE9_RNG_ENABLED && CONFIG_USE_RA_FSP_SCE && CONFIG_HAS_RENESAS_RA_FSP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/Kconfig.renesas:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_USE_RA_FSP_SCE`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_USE_RA_FSP_SCE)、[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)。

<a id="CONFIG_HAS_RENESAS_RA_TRNG"></a>

## 209.10 `CONFIG_HAS_RENESAS_RA_TRNG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为 SCE 驱动包含真随机数生成器（TRNG）实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_TRNG_ENABLED && CONFIG_USE_RA_FSP_SCE && CONFIG_HAS_RENESAS_RA_FSP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/Kconfig.renesas:145`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L145)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_USE_RA_FSP_SCE`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_USE_RA_FSP_SCE)、[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)。

<a id="CONFIG_HAS_RENESAS_RX_FSP"></a>

## 209.11 `CONFIG_HAS_RENESAS_RX_FSP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用瑞萨（Renesas）RX 灵活软件包（Flexible Software Package，FSP）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_RX74M
CONFIG_SOC_SERIES_RX74N
```

**定义位置（Location）**：[`modules/Kconfig.renesas:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RX74M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX74M)、[`CONFIG_SOC_SERIES_RX74N`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX74N)。

<a id="CONFIG_HAS_RENESAS_RX_RDP"></a>

## 209.12 `CONFIG_HAS_RENESAS_RX_RDP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用瑞萨（Renesas）RX 驱动包（RDP）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_RX130
CONFIG_SOC_SERIES_RX140
CONFIG_SOC_SERIES_RX14T
CONFIG_SOC_SERIES_RX261
CONFIG_SOC_SERIES_RX26T
```

**定义位置（Location）**：[`modules/Kconfig.renesas:494`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L494)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RX130`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX130)、[`CONFIG_SOC_SERIES_RX140`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX140)、[`CONFIG_SOC_SERIES_RX14T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX14T)、[`CONFIG_SOC_SERIES_RX261`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX261)、[`CONFIG_SOC_SERIES_RX26T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX26T)。

<a id="CONFIG_HAS_RENESAS_RZ_FSP"></a>

## 209.13 `CONFIG_HAS_RENESAS_RZ_FSP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用瑞萨（Renesas）RZ 灵活软件包（Flexible Software Package，FSP）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_RZA3M
CONFIG_SOC_SERIES_RZA3UL
CONFIG_SOC_SERIES_RZG2L
CONFIG_SOC_SERIES_RZG2UL
CONFIG_SOC_SERIES_RZG3E
CONFIG_SOC_SERIES_RZG3S
CONFIG_SOC_SERIES_RZN2H
CONFIG_SOC_SERIES_RZN2L
CONFIG_SOC_SERIES_RZT2H
CONFIG_SOC_SERIES_RZT2L
CONFIG_SOC_SERIES_RZT2M
CONFIG_SOC_R9A09G057H44GBG_CM33
CONFIG_SOC_R9A09G057H44GBG_CR8
CONFIG_SOC_SERIES_RZV2L
CONFIG_SOC_SERIES_RZV2N
```

**定义位置（Location）**：[`modules/Kconfig.renesas:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RZA3M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZA3M)、[`CONFIG_SOC_SERIES_RZA3UL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZA3UL)、[`CONFIG_SOC_SERIES_RZG2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZG2L)、[`CONFIG_SOC_SERIES_RZG2UL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZG2UL)、[`CONFIG_SOC_SERIES_RZG3E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZG3E)、[`CONFIG_SOC_SERIES_RZG3S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZG3S)、[`CONFIG_SOC_SERIES_RZN2H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZN2H)、[`CONFIG_SOC_SERIES_RZN2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZN2L)、[`CONFIG_SOC_SERIES_RZT2H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2H)、[`CONFIG_SOC_SERIES_RZT2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2L)、[`CONFIG_SOC_SERIES_RZT2M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2M)、[`CONFIG_SOC_R9A09G057H44GBG_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R9A09G057H44GBG_CM33)、[`CONFIG_SOC_R9A09G057H44GBG_CR8`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R9A09G057H44GBG_CR8)、[`CONFIG_SOC_SERIES_RZV2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZV2L)、[`CONFIG_SOC_SERIES_RZV2N`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZV2N)。

<a id="CONFIG_USE_RA_FSP_ACMPHS"></a>

## 209.14 `CONFIG_USE_RA_FSP_ACMPHS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP ACMPHS 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_COMPARATOR_RENESAS_RA
```

**定义位置（Location）**：[`modules/Kconfig.renesas:254`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L254)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_COMPARATOR_RENESAS_RA`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR_RENESAS_RA)。

<a id="CONFIG_USE_RA_FSP_ADC"></a>

## 209.15 `CONFIG_USE_RA_FSP_ADC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP 模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_ADC_RENESAS_RA
```

**定义位置（Location）**：[`modules/Kconfig.renesas:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_ADC_RENESAS_RA`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_RENESAS_RA)。

<a id="CONFIG_USE_RA_FSP_ADC_B"></a>

## 209.16 `CONFIG_USE_RA_FSP_ADC_B`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RX FSP ADC-B 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_ADC_RENESAS_RA_ADC_B
```

**定义位置（Location）**：[`modules/Kconfig.renesas:348`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L348)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_ADC_RENESAS_RA_ADC_B`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_RENESAS_RA_ADC_B)。

<a id="CONFIG_USE_RA_FSP_AGT"></a>

## 209.17 `CONFIG_USE_RA_FSP_AGT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP AGT 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_COUNTER_RA_AGT
```

**定义位置（Location）**：[`modules/Kconfig.renesas:184`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L184)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_COUNTER_RA_AGT`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_RA_AGT)。

<a id="CONFIG_USE_RA_FSP_CANFD"></a>

## 209.18 `CONFIG_USE_RA_FSP_CANFD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP 灵活数据速率 CAN（CANFD）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_CAN_RENESAS_RA_CANFD
```

**定义位置（Location）**：[`modules/Kconfig.renesas:189`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L189)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_CAN_RENESAS_RA_CANFD`](P060_drivers_can_配置项参考.md#CONFIG_CAN_RENESAS_RA_CANFD)。

<a id="CONFIG_USE_RA_FSP_CEU"></a>

## 209.19 `CONFIG_USE_RA_FSP_CEU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP CEU 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_VIDEO_RENESAS_RA_CEU
```

**定义位置（Location）**：[`modules/Kconfig.renesas:323`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L323)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_VIDEO_RENESAS_RA_CEU`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_RENESAS_RA_CEU)。

<a id="CONFIG_USE_RA_FSP_CRC"></a>

## 209.20 `CONFIG_USE_RA_FSP_CRC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP 循环冗余校验（CRC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_CRC_DRIVER_RENESAS_RA
```

**定义位置（Location）**：[`modules/Kconfig.renesas:244`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L244)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_CRC_DRIVER_RENESAS_RA`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_RENESAS_RA)。

<a id="CONFIG_USE_RA_FSP_CTSU"></a>

## 209.21 `CONFIG_USE_RA_FSP_CTSU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP CTSU 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_IOPORT
```

**被选择（Selected by）**

```text
CONFIG_INPUT_RENESAS_RA_CTSU
```

**定义位置（Location）**：[`modules/Kconfig.renesas:306`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L306)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_USE_RA_FSP_IOPORT`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_USE_RA_FSP_IOPORT)、[`CONFIG_INPUT_RENESAS_RA_CTSU`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RA_CTSU)。

<a id="CONFIG_USE_RA_FSP_DAC"></a>

## 209.22 `CONFIG_USE_RA_FSP_DAC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP 数模转换器（DAC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_DAC_RENESAS_RA
```

**定义位置（Location）**：[`modules/Kconfig.renesas:249`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L249)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_DAC_RENESAS_RA`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_RENESAS_RA)。

<a id="CONFIG_USE_RA_FSP_DISPLAY"></a>

## 209.23 `CONFIG_USE_RA_FSP_DISPLAY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP 显示（Display）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_RENESAS_RA_GLCDC
```

**定义位置（Location）**：[`modules/Kconfig.renesas:229`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L229)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_RENESAS_RA_GLCDC`](P077_drivers_display_配置项参考_1.md#CONFIG_RENESAS_RA_GLCDC)。

<a id="CONFIG_USE_RA_FSP_DMA"></a>

## 209.24 `CONFIG_USE_RA_FSP_DMA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP 直接内存访问（DMA）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_DMA_RENESAS_RA
CONFIG_I2C_RENESAS_RA_SCI_B_DMAC
CONFIG_UART_RA8_SCI_B_UART_DMAC
CONFIG_SPI_RENESAS_RA_SCI_B_DMAC
CONFIG_SPI_B_DMAC
```

**定义位置（Location）**：[`modules/Kconfig.renesas:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_DMA_RENESAS_RA`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_RENESAS_RA)、[`CONFIG_I2C_RENESAS_RA_SCI_B_DMAC`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_RENESAS_RA_SCI_B_DMAC)、[`CONFIG_UART_RA8_SCI_B_UART_DMAC`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_RA8_SCI_B_UART_DMAC)、[`CONFIG_SPI_RENESAS_RA_SCI_B_DMAC`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RA_SCI_B_DMAC)、[`CONFIG_SPI_B_DMAC`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_B_DMAC)。

<a id="CONFIG_USE_RA_FSP_DRW"></a>

## 209.25 `CONFIG_USE_RA_FSP_DRW`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP DRW 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_RENESAS_RA_DRW
```

**定义位置（Location）**：[`modules/Kconfig.renesas:338`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L338)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_RENESAS_RA_DRW`](P123_drivers_misc_配置项参考.md#CONFIG_RENESAS_RA_DRW)。

<a id="CONFIG_USE_RA_FSP_DTC"></a>

## 209.26 `CONFIG_USE_RA_FSP_DTC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP DTC 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_I2C_RENESAS_RA_SCI_DTC
CONFIG_I2C_RENESAS_RA_SCI_B_DTC
CONFIG_I2S_RENESAS_RA_SSIE_DTC
CONFIG_SDHC_RENESAS_RA
CONFIG_UART_SCI_RA
CONFIG_UART_RA8_SCI_B_UART_DTC
CONFIG_SPI_RA_DTC
CONFIG_SPI_RENESAS_RA_SCI_DTC
CONFIG_SPI_RENESAS_RA_SCI_B_DTC
CONFIG_SPI_B_RA_DTC
```

**定义位置（Location）**：[`modules/Kconfig.renesas:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_I2C_RENESAS_RA_SCI_DTC`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_RENESAS_RA_SCI_DTC)、[`CONFIG_I2C_RENESAS_RA_SCI_B_DTC`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_RENESAS_RA_SCI_B_DTC)、[`CONFIG_I2S_RENESAS_RA_SSIE_DTC`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_RENESAS_RA_SSIE_DTC)、[`CONFIG_SDHC_RENESAS_RA`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_RENESAS_RA)、[`CONFIG_UART_SCI_RA`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_SCI_RA)、[`CONFIG_UART_RA8_SCI_B_UART_DTC`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_RA8_SCI_B_UART_DTC)、[`CONFIG_SPI_RA_DTC`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RA_DTC)、[`CONFIG_SPI_RENESAS_RA_SCI_DTC`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RA_SCI_DTC)、[`CONFIG_SPI_RENESAS_RA_SCI_B_DTC`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RA_SCI_B_DTC)、[`CONFIG_SPI_B_RA_DTC`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_B_RA_DTC)。

<a id="CONFIG_USE_RA_FSP_ELC"></a>

## 209.27 `CONFIG_USE_RA_FSP_ELC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP ELC 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_RENESAS_RA_ELC
```

**定义位置（Location）**：[`modules/Kconfig.renesas:286`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L286)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_RENESAS_RA_ELC`](P123_drivers_misc_配置项参考.md#CONFIG_RENESAS_RA_ELC)。

<a id="CONFIG_USE_RA_FSP_ETHER"></a>

## 209.28 `CONFIG_USE_RA_FSP_ETHER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP 以太网（Ethernet）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_ETH_RENESAS_RA
```

**定义位置（Location）**：[`modules/Kconfig.renesas:199`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L199)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_ETH_RENESAS_RA`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_RENESAS_RA)。

<a id="CONFIG_USE_RA_FSP_ETHER_PHY"></a>

## 209.29 `CONFIG_USE_RA_FSP_ETHER_PHY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP 以太网物理层（Ethernet PHY）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_MDIO_RENESAS_RA
```

**定义位置（Location）**：[`modules/Kconfig.renesas:194`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L194)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_MDIO_RENESAS_RA`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO_RENESAS_RA)。

<a id="CONFIG_USE_RA_FSP_FLASH_HP"></a>

## 209.30 `CONFIG_USE_RA_FSP_FLASH_HP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP 高性能闪存（FLASH HP）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_SOC_FLASH_RENESAS_RA_HP
```

**定义位置（Location）**：[`modules/Kconfig.renesas:169`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L169)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_SOC_FLASH_RENESAS_RA_HP`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RENESAS_RA_HP)。

<a id="CONFIG_USE_RA_FSP_FLASH_LP"></a>

## 209.31 `CONFIG_USE_RA_FSP_FLASH_LP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP 低功耗闪存（FLASH LP）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_SOC_FLASH_RENESAS_RA_LP
```

**定义位置（Location）**：[`modules/Kconfig.renesas:174`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L174)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_SOC_FLASH_RENESAS_RA_LP`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RENESAS_RA_LP)。

<a id="CONFIG_USE_RA_FSP_GPT"></a>

## 209.32 `CONFIG_USE_RA_FSP_GPT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP GPT 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_PWM_RENESAS_RA
```

**定义位置（Location）**：[`modules/Kconfig.renesas:179`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L179)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_PWM_RENESAS_RA`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_RENESAS_RA)。

<a id="CONFIG_USE_RA_FSP_I2C_IIC_CONTROLLER"></a>

## 209.33 `CONFIG_USE_RA_FSP_I2C_IIC_CONTROLLER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用瑞萨（Renesas）RA I2C IIC 控制器（Controller）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_I2C_RENESAS_RA_IIC
```

**定义位置（Location）**：[`modules/Kconfig.renesas:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_I2C_RENESAS_RA_IIC`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_RENESAS_RA_IIC)。

<a id="CONFIG_USE_RA_FSP_I2C_IIC_TARGET"></a>

## 209.34 `CONFIG_USE_RA_FSP_I2C_IIC_TARGET`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用瑞萨（Renesas）RA I2C IIC 目标端（Target）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_I2C_RENESAS_RA_IIC
```

**定义位置（Location）**：[`modules/Kconfig.renesas:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_I2C_RENESAS_RA_IIC`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_RENESAS_RA_IIC)。

<a id="CONFIG_USE_RA_FSP_I3C"></a>

## 209.35 `CONFIG_USE_RA_FSP_I3C`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP I3C 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_I3C_RENESAS_RA
```

**定义位置（Location）**：[`modules/Kconfig.renesas:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_I3C_RENESAS_RA`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_RENESAS_RA)。

<a id="CONFIG_USE_RA_FSP_IOPORT"></a>

## 209.36 `CONFIG_USE_RA_FSP_IOPORT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP 输入／输出端口（IOPORT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_USE_RA_FSP_CTSU
```

**定义位置（Location）**：[`modules/Kconfig.renesas:301`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L301)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_USE_RA_FSP_CTSU`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_USE_RA_FSP_CTSU)。

<a id="CONFIG_USE_RA_FSP_IPC"></a>

## 209.37 `CONFIG_USE_RA_FSP_IPC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP 进程间通信（IPC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_MBOX_RENESAS_RA_IPC
```

**定义位置（Location）**：[`modules/Kconfig.renesas:328`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L328)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_MBOX_RENESAS_RA_IPC`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX_RENESAS_RA_IPC)。

<a id="CONFIG_USE_RA_FSP_LAYER3_SWITCH"></a>

## 209.38 `CONFIG_USE_RA_FSP_LAYER3_SWITCH`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP 以太网第三层交换机（Ethernet Layer3 Switch）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_ETH_RENESAS_RA_RMAC
```

**定义位置（Location）**：[`modules/Kconfig.renesas:209`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L209)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_ETH_RENESAS_RA_RMAC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_RENESAS_RA_RMAC)。

<a id="CONFIG_USE_RA_FSP_LPM"></a>

## 209.39 `CONFIG_USE_RA_FSP_LPM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP 低功耗模式（LPM）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PM && CONFIG_HAS_RENESAS_RA_FSP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/Kconfig.renesas:274`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L274)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)。

<a id="CONFIG_USE_RA_FSP_LVD"></a>

## 209.40 `CONFIG_USE_RA_FSP_LVD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP 低电压检测（LVD）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_COMPARATOR_RENESAS_RA_LVD
```

**定义位置（Location）**：[`modules/Kconfig.renesas:259`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L259)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_COMPARATOR_RENESAS_RA_LVD`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR_RENESAS_RA_LVD)。

<a id="CONFIG_USE_RA_FSP_MIPI_DSI"></a>

## 209.41 `CONFIG_USE_RA_FSP_MIPI_DSI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP MIPI 显示串行接口（MIPI DSI）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_MIPI_DSI_RENESAS_RA
```

**定义位置（Location）**：[`modules/Kconfig.renesas:234`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L234)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_MIPI_DSI_RENESAS_RA`](P122_drivers_mipi_dsi_配置项参考.md#CONFIG_MIPI_DSI_RENESAS_RA)。

<a id="CONFIG_USE_RA_FSP_MRAM"></a>

## 209.42 `CONFIG_USE_RA_FSP_MRAM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP 磁阻随机存取存储器（MRAM）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_SOC_FLASH_RENESAS_RA_MRAM
```

**定义位置（Location）**：[`modules/Kconfig.renesas:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_SOC_FLASH_RENESAS_RA_MRAM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RENESAS_RA_MRAM)。

<a id="CONFIG_USE_RA_FSP_OSPI_B_NOR_FLASH"></a>

## 209.43 `CONFIG_USE_RA_FSP_OSPI_B_NOR_FLASH`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP 八线 SPI（Octal-SPI）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_FLASH_RENESAS_RA_OSPI_B
```

**定义位置（Location）**：[`modules/Kconfig.renesas:281`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L281)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_FLASH_RENESAS_RA_OSPI_B`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_RENESAS_RA_OSPI_B)。

<a id="CONFIG_USE_RA_FSP_PDM"></a>

## 209.44 `CONFIG_USE_RA_FSP_PDM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP 脉冲密度调制（PDM）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_AUDIO_DMIC_RENESAS_RA_PDM
```

**定义位置（Location）**：[`modules/Kconfig.renesas:296`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L296)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_AUDIO_DMIC_RENESAS_RA_PDM`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_RENESAS_RA_PDM)。

<a id="CONFIG_USE_RA_FSP_QSPI_NOR_FLASH"></a>

## 209.45 `CONFIG_USE_RA_FSP_QSPI_NOR_FLASH`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP 四线 SPI（Quad-SPI）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_FLASH_RENESAS_RA_QSPI
```

**定义位置（Location）**：[`modules/Kconfig.renesas:318`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L318)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_FLASH_RENESAS_RA_QSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_RENESAS_RA_QSPI)。

<a id="CONFIG_USE_RA_FSP_RMAC"></a>

## 209.46 `CONFIG_USE_RA_FSP_RMAC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP 以太网 RMAC 驱动（Ethernet RMAC driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_ETH_RENESAS_RA_RMAC
```

**定义位置（Location）**：[`modules/Kconfig.renesas:204`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L204)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_ETH_RENESAS_RA_RMAC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_RENESAS_RA_RMAC)。

<a id="CONFIG_USE_RA_FSP_RTC"></a>

## 209.47 `CONFIG_USE_RA_FSP_RTC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP 实时时钟（RTC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_RTC_RENESAS_RA
```

**定义位置（Location）**：[`modules/Kconfig.renesas:333`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L333)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_RTC_RENESAS_RA`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_RENESAS_RA)。

<a id="CONFIG_USE_RA_FSP_SAU_UART"></a>

## 209.48 `CONFIG_USE_RA_FSP_SAU_UART`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP SAU UART 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_UART_RENESAS_RA_SAU
```

**定义位置（Location）**：[`modules/Kconfig.renesas:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_UART_RENESAS_RA_SAU`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_RENESAS_RA_SAU)。

<a id="CONFIG_USE_RA_FSP_SCE"></a>

## 209.49 `CONFIG_USE_RA_FSP_SCE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP SCE 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_ENTROPY_RENESAS_RA
```

**定义位置（Location）**：[`modules/Kconfig.renesas:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_ENTROPY_RENESAS_RA`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_RENESAS_RA)。

<a id="CONFIG_USE_RA_FSP_SCI_B_I2C"></a>

## 209.50 `CONFIG_USE_RA_FSP_SCI_B_I2C`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP SCI-B I2C 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_I2C_RENESAS_RA_SCI_B
```

**定义位置（Location）**：[`modules/Kconfig.renesas:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_I2C_RENESAS_RA_SCI_B`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_RENESAS_RA_SCI_B)。

<a id="CONFIG_USE_RA_FSP_SCI_B_LIN"></a>

## 209.51 `CONFIG_USE_RA_FSP_SCI_B_LIN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP SCI-B LIN 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_LIN_RENESAS_RA_SCI_B
```

**定义位置（Location）**：[`modules/Kconfig.renesas:343`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L343)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_LIN_RENESAS_RA_SCI_B`](P116_drivers_lin_配置项参考.md#CONFIG_LIN_RENESAS_RA_SCI_B)。

<a id="CONFIG_USE_RA_FSP_SCI_B_SPI"></a>

## 209.52 `CONFIG_USE_RA_FSP_SCI_B_SPI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP SCI-B SPI 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_SPI_RENESAS_RA_SCI_B
```

**定义位置（Location）**：[`modules/Kconfig.renesas:164`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L164)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_SPI_RENESAS_RA_SCI_B`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RA_SCI_B)。

<a id="CONFIG_USE_RA_FSP_SCI_B_UART"></a>

## 209.53 `CONFIG_USE_RA_FSP_SCI_B_UART`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP SCI-B UART 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_UART_RA8_SCI_B
```

**定义位置（Location）**：[`modules/Kconfig.renesas:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_UART_RA8_SCI_B`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_RA8_SCI_B)。

<a id="CONFIG_USE_RA_FSP_SCI_I2C"></a>

## 209.54 `CONFIG_USE_RA_FSP_SCI_I2C`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP SCI I2C 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_I2C_RENESAS_RA_SCI
```

**定义位置（Location）**：[`modules/Kconfig.renesas:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_I2C_RENESAS_RA_SCI`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_RENESAS_RA_SCI)。

<a id="CONFIG_USE_RA_FSP_SCI_SPI"></a>

## 209.55 `CONFIG_USE_RA_FSP_SCI_SPI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP SCI SPI 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_SPI_RENESAS_RA_SCI
```

**定义位置（Location）**：[`modules/Kconfig.renesas:159`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L159)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_SPI_RENESAS_RA_SCI`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RA_SCI)。

<a id="CONFIG_USE_RA_FSP_SCI_UART"></a>

## 209.56 `CONFIG_USE_RA_FSP_SCI_UART`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP SCI UART 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_UART_SCI_RA
```

**定义位置（Location）**：[`modules/Kconfig.renesas:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_UART_SCI_RA`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_SCI_RA)。

<a id="CONFIG_USE_RA_FSP_SDHI"></a>

## 209.57 `CONFIG_USE_RA_FSP_SDHI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP SDHI 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_SDHC_RENESAS_RA
```

**定义位置（Location）**：[`modules/Kconfig.renesas:239`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L239)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_SDHC_RENESAS_RA`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_RENESAS_RA)。

<a id="CONFIG_USE_RA_FSP_SDRAM"></a>

## 209.58 `CONFIG_USE_RA_FSP_SDRAM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP 同步动态随机存取存储器（SDRAM）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_MEMC_RENESAS_RA_SDRAM
```

**定义位置（Location）**：[`modules/Kconfig.renesas:224`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L224)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_MEMC_RENESAS_RA_SDRAM`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC_RENESAS_RA_SDRAM)。

<a id="CONFIG_USE_RA_FSP_SPI"></a>

## 209.59 `CONFIG_USE_RA_FSP_SPI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP 串行外设接口（SPI）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_SPI_RENESAS_RA
```

**定义位置（Location）**：[`modules/Kconfig.renesas:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_SPI_RENESAS_RA`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RA)。

<a id="CONFIG_USE_RA_FSP_SPI_B"></a>

## 209.60 `CONFIG_USE_RA_FSP_SPI_B`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP SPI-B 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_SPI_RENESAS_RA8
```

**定义位置（Location）**：[`modules/Kconfig.renesas:154`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L154)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_SPI_RENESAS_RA8`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RA8)。

<a id="CONFIG_USE_RA_FSP_SSI"></a>

## 209.61 `CONFIG_USE_RA_FSP_SSI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP I2S SSI 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_I2S_RENESAS_RA_SSIE
```

**定义位置（Location）**：[`modules/Kconfig.renesas:291`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L291)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_I2S_RENESAS_RA_SSIE`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_RENESAS_RA_SSIE)。

<a id="CONFIG_USE_RA_FSP_TOUCH"></a>

## 209.62 `CONFIG_USE_RA_FSP_TOUCH`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP 触摸库（TOUCH library）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_RA_FSP_CTSU && CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_INPUT_RENESAS_RA_CTSU
```

**定义位置（Location）**：[`modules/Kconfig.renesas:312`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L312)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_USE_RA_FSP_CTSU`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_USE_RA_FSP_CTSU)、[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_INPUT_RENESAS_RA_CTSU`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RA_CTSU)。

<a id="CONFIG_USE_RA_FSP_ULPT"></a>

## 209.63 `CONFIG_USE_RA_FSP_ULPT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP ULPT 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_COUNTER_RENESAS_RA_ULPT
```

**定义位置（Location）**：[`modules/Kconfig.renesas:269`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L269)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_COUNTER_RENESAS_RA_ULPT`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_RENESAS_RA_ULPT)。

<a id="CONFIG_USE_RA_FSP_USB_DEVICE"></a>

## 209.64 `CONFIG_USE_RA_FSP_USB_DEVICE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP USB 设备控制器（Device Controller）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_UDC_RENESAS_RA
```

**定义位置（Location）**：[`modules/Kconfig.renesas:214`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L214)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_UDC_RENESAS_RA`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_RENESAS_RA)。

<a id="CONFIG_USE_RA_FSP_USB_HOST"></a>

## 209.65 `CONFIG_USE_RA_FSP_USB_HOST`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP USB 主机控制器（Host Controller）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_UHC_RENESAS_RA
```

**定义位置（Location）**：[`modules/Kconfig.renesas:219`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L219)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_UHC_RENESAS_RA`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_RENESAS_RA)。

<a id="CONFIG_USE_RA_FSP_WDT"></a>

## 209.66 `CONFIG_USE_RA_FSP_WDT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RA FSP 看门狗定时器（WDT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RA_FSP
```

**被选择（Selected by）**

```text
CONFIG_WDT_RENESAS_RA
```

**定义位置（Location）**：[`modules/Kconfig.renesas:264`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L264)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_WDT_RENESAS_RA`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_RENESAS_RA)。

<a id="CONFIG_USE_RX_FSP_SCI_B_UART"></a>

## 209.67 `CONFIG_USE_RX_FSP_SCI_B_UART`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RX FSP SCI-B UART 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RX_FSP
```

**被选择（Selected by）**

```text
CONFIG_UART_RENESAS_RX_SCI_B
```

**定义位置（Location）**：[`modules/Kconfig.renesas:562`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L562)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RX_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RX_FSP)、[`CONFIG_UART_RENESAS_RX_SCI_B`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_RENESAS_RX_SCI_B)。

<a id="CONFIG_USE_RX_RDP_ADC"></a>

## 209.68 `CONFIG_USE_RX_RDP_ADC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RX RDP 模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RX_RDP
```

**被选择（Selected by）**

```text
CONFIG_ADC_RENESAS_RX
```

**定义位置（Location）**：[`modules/Kconfig.renesas:531`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L531)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RX_RDP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RX_RDP)、[`CONFIG_ADC_RENESAS_RX`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_RENESAS_RX)。

<a id="CONFIG_USE_RX_RDP_CTSU"></a>

## 209.69 `CONFIG_USE_RX_RDP_CTSU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RX RDP CTSU 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RX_RDP
```

**被选择（Selected by）**

```text
CONFIG_INPUT_RENESAS_RX_CTSU
```

**定义位置（Location）**：[`modules/Kconfig.renesas:541`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L541)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RX_RDP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RX_RDP)、[`CONFIG_INPUT_RENESAS_RX_CTSU`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RX_CTSU)。

<a id="CONFIG_USE_RX_RDP_FLASH"></a>

## 209.70 `CONFIG_USE_RX_RDP_FLASH`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RX RDP 闪存（Flash）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RX_RDP
```

**被选择（Selected by）**

```text
CONFIG_SOC_FLASH_RENESAS_RX
```

**定义位置（Location）**：[`modules/Kconfig.renesas:526`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L526)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RX_RDP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RX_RDP)、[`CONFIG_SOC_FLASH_RENESAS_RX`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RENESAS_RX)。

<a id="CONFIG_USE_RX_RDP_GPIO"></a>

## 209.71 `CONFIG_USE_RX_RDP_GPIO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RX RDP MPC 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RX_RDP
```

**被选择（Selected by）**

```text
CONFIG_PINCTRL_RENESAS_RX
```

**定义位置（Location）**：[`modules/Kconfig.renesas:506`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L506)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RX_RDP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RX_RDP)、[`CONFIG_PINCTRL_RENESAS_RX`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL_RENESAS_RX)。

<a id="CONFIG_USE_RX_RDP_I2C"></a>

## 209.72 `CONFIG_USE_RX_RDP_I2C`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RX RDP I2C 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RX_RDP
```

**被选择（Selected by）**

```text
CONFIG_I2C_RENESAS_RX_RIIC
```

**定义位置（Location）**：[`modules/Kconfig.renesas:521`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L521)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RX_RDP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RX_RDP)、[`CONFIG_I2C_RENESAS_RX_RIIC`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RENESAS_RX_RIIC)。

<a id="CONFIG_USE_RX_RDP_IWDT"></a>

## 209.73 `CONFIG_USE_RX_RDP_IWDT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RX RDP 独立看门狗定时器（IWDT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RX_RDP
```

**被选择（Selected by）**

```text
CONFIG_WDT_RENESAS_RX_IWDT
```

**定义位置（Location）**：[`modules/Kconfig.renesas:536`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L536)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RX_RDP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RX_RDP)、[`CONFIG_WDT_RENESAS_RX_IWDT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_RENESAS_RX_IWDT)。

<a id="CONFIG_USE_RX_RDP_LPC"></a>

## 209.74 `CONFIG_USE_RX_RDP_LPC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RX RDP LPC 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PM && CONFIG_HAS_RENESAS_RX_RDP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/Kconfig.renesas:551`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L551)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_HAS_RENESAS_RX_RDP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RX_RDP)。

<a id="CONFIG_USE_RX_RDP_LVD"></a>

## 209.75 `CONFIG_USE_RX_RDP_LVD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RX RDP 低电压检测（LVD）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RX_RDP
```

**被选择（Selected by）**

```text
CONFIG_COMPARATOR_RENESAS_RX_LVD
```

**定义位置（Location）**：[`modules/Kconfig.renesas:546`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L546)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RX_RDP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RX_RDP)、[`CONFIG_COMPARATOR_RENESAS_RX_LVD`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR_RENESAS_RX_LVD)。

<a id="CONFIG_USE_RX_RDP_MPC"></a>

## 209.76 `CONFIG_USE_RX_RDP_MPC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RX RDP MPC 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RX_RDP
```

**被选择（Selected by）**

```text
CONFIG_PINCTRL_RENESAS_RX
```

**定义位置（Location）**：[`modules/Kconfig.renesas:501`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L501)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RX_RDP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RX_RDP)、[`CONFIG_PINCTRL_RENESAS_RX`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL_RENESAS_RX)。

<a id="CONFIG_USE_RX_RDP_RSPI"></a>

## 209.77 `CONFIG_USE_RX_RDP_RSPI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RX RDP RSPI 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RX_RDP
```

**被选择（Selected by）**

```text
CONFIG_SPI_RENESAS_RX
```

**定义位置（Location）**：[`modules/Kconfig.renesas:516`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L516)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RX_RDP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RX_RDP)、[`CONFIG_SPI_RENESAS_RX`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RX)。

<a id="CONFIG_USE_RX_RDP_SCI_UART"></a>

## 209.78 `CONFIG_USE_RX_RDP_SCI_UART`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RX RDP SCI UART 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RX_RDP
```

**被选择（Selected by）**

```text
CONFIG_UART_RENESAS_RX
```

**定义位置（Location）**：[`modules/Kconfig.renesas:511`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L511)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RX_RDP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RX_RDP)、[`CONFIG_UART_RENESAS_RX`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_RENESAS_RX)。

<a id="CONFIG_USE_RZ_FSP_ADC"></a>

## 209.79 `CONFIG_USE_RZ_FSP_ADC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RZ FSP 模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RZ_FSP
```

**被选择（Selected by）**

```text
CONFIG_ADC_RENESAS_RZ
```

**定义位置（Location）**：[`modules/Kconfig.renesas:357`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L357)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RZ_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RZ_FSP)、[`CONFIG_ADC_RENESAS_RZ`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_RENESAS_RZ)。

<a id="CONFIG_USE_RZ_FSP_ADC_C"></a>

## 209.80 `CONFIG_USE_RZ_FSP_ADC_C`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RZ FSP ADC-C 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RZ_FSP
```

**被选择（Selected by）**

```text
CONFIG_ADC_RENESAS_RZ_ADC_C
```

**定义位置（Location）**：[`modules/Kconfig.renesas:362`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L362)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RZ_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RZ_FSP)、[`CONFIG_ADC_RENESAS_RZ_ADC_C`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_RENESAS_RZ_ADC_C)。

<a id="CONFIG_USE_RZ_FSP_ADC_E"></a>

## 209.81 `CONFIG_USE_RZ_FSP_ADC_E`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RZ FSP ADC-E 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RZ_FSP
```

**被选择（Selected by）**

```text
CONFIG_ADC_RENESAS_RZ_ADC_E
```

**定义位置（Location）**：[`modules/Kconfig.renesas:367`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L367)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RZ_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RZ_FSP)、[`CONFIG_ADC_RENESAS_RZ_ADC_E`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_RENESAS_RZ_ADC_E)。

<a id="CONFIG_USE_RZ_FSP_CANFD"></a>

## 209.82 `CONFIG_USE_RZ_FSP_CANFD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RZ FSP 灵活数据速率 CAN（CANFD）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RZ_FSP
```

**被选择（Selected by）**

```text
CONFIG_CAN_RENESAS_RZ_CANFD
```

**定义位置（Location）**：[`modules/Kconfig.renesas:422`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L422)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RZ_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RZ_FSP)、[`CONFIG_CAN_RENESAS_RZ_CANFD`](P060_drivers_can_配置项参考.md#CONFIG_CAN_RENESAS_RZ_CANFD)。

<a id="CONFIG_USE_RZ_FSP_CGC"></a>

## 209.83 `CONFIG_USE_RZ_FSP_CGC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RZ FSP CGC 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RZ_FSP
```

**被选择（Selected by）**

```text
CONFIG_CLOCK_CONTROL_RENESAS_RZ_CGC
```

**定义位置（Location）**：[`modules/Kconfig.renesas:432`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L432)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RZ_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RZ_FSP)、[`CONFIG_CLOCK_CONTROL_RENESAS_RZ_CGC`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_RENESAS_RZ_CGC)。

<a id="CONFIG_USE_RZ_FSP_CMTW"></a>

## 209.84 `CONFIG_USE_RZ_FSP_CMTW`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RZ FSP CMTW 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RZ_FSP
```

**被选择（Selected by）**

```text
CONFIG_COUNTER_RENESAS_RZ_CMTW
```

**定义位置（Location）**：[`modules/Kconfig.renesas:452`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L452)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RZ_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RZ_FSP)、[`CONFIG_COUNTER_RENESAS_RZ_CMTW`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_RENESAS_RZ_CMTW)。

<a id="CONFIG_USE_RZ_FSP_CPG"></a>

## 209.85 `CONFIG_USE_RZ_FSP_CPG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RZ FSP 时钟控制（CLOCK CONTROL）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RZ_FSP
```

**被选择（Selected by）**

```text
CONFIG_CLOCK_CONTROL_RENESAS_RZ_CPG
```

**定义位置（Location）**：[`modules/Kconfig.renesas:427`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L427)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RZ_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RZ_FSP)、[`CONFIG_CLOCK_CONTROL_RENESAS_RZ_CPG`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_RENESAS_RZ_CPG)。

<a id="CONFIG_USE_RZ_FSP_DISPLAY"></a>

## 209.86 `CONFIG_USE_RZ_FSP_DISPLAY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RZ FSP 显示（Display）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RZ_FSP
```

**被选择（Selected by）**

```text
CONFIG_RENESAS_RZ_LCDC
```

**定义位置（Location）**：[`modules/Kconfig.renesas:482`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L482)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RZ_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RZ_FSP)、[`CONFIG_RENESAS_RZ_LCDC`](P077_drivers_display_配置项参考_1.md#CONFIG_RENESAS_RZ_LCDC)。

<a id="CONFIG_USE_RZ_FSP_DMAC"></a>

## 209.87 `CONFIG_USE_RZ_FSP_DMAC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RZ FSP 直接内存访问控制器（DMAC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RZ_FSP
```

**被选择（Selected by）**

```text
CONFIG_DMA_RENESAS_RZ_DMAC
CONFIG_SPI_RENESAS_RZ_RSPI_DMAC
CONFIG_SPI_RENESAS_RZ_DMA
```

**定义位置（Location）**：[`modules/Kconfig.renesas:407`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L407)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RZ_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RZ_FSP)、[`CONFIG_DMA_RENESAS_RZ_DMAC`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_RENESAS_RZ_DMAC)、[`CONFIG_SPI_RENESAS_RZ_RSPI_DMAC`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RZ_RSPI_DMAC)、[`CONFIG_SPI_RENESAS_RZ_DMA`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RZ_DMA)。

<a id="CONFIG_USE_RZ_FSP_DMAC_B"></a>

## 209.88 `CONFIG_USE_RZ_FSP_DMAC_B`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RZ FSP DMAC_B 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RZ_FSP
```

**被选择（Selected by）**

```text
CONFIG_DMA_RENESAS_RZ_DMAC_B
CONFIG_SPI_RENESAS_RZ_RSPI_DMAC
CONFIG_SPI_RENESAS_RZ_DMA
```

**定义位置（Location）**：[`modules/Kconfig.renesas:412`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L412)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RZ_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RZ_FSP)、[`CONFIG_DMA_RENESAS_RZ_DMAC_B`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_RENESAS_RZ_DMAC_B)、[`CONFIG_SPI_RENESAS_RZ_RSPI_DMAC`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RZ_RSPI_DMAC)、[`CONFIG_SPI_RENESAS_RZ_DMA`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RZ_DMA)。

<a id="CONFIG_USE_RZ_FSP_EXT_IRQ"></a>

## 209.89 `CONFIG_USE_RZ_FSP_EXT_IRQ`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RZ FSP 外部中断请求（External IRQ）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RZ_FSP
```

**被选择（Selected by）**

```text
CONFIG_RENESAS_RZ_EXT_IRQ
```

**定义位置（Location）**：[`modules/Kconfig.renesas:402`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L402)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RZ_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RZ_FSP)、[`CONFIG_RENESAS_RZ_EXT_IRQ`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_RENESAS_RZ_EXT_IRQ)。

<a id="CONFIG_USE_RZ_FSP_GPT"></a>

## 209.90 `CONFIG_USE_RZ_FSP_GPT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RZ FSP GPT 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RZ_FSP
```

**被选择（Selected by）**

```text
CONFIG_PWM_RENESAS_RZ_GPT
```

**定义位置（Location）**：[`modules/Kconfig.renesas:397`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L397)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RZ_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RZ_FSP)、[`CONFIG_PWM_RENESAS_RZ_GPT`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_RENESAS_RZ_GPT)。

<a id="CONFIG_USE_RZ_FSP_GTM"></a>

## 209.91 `CONFIG_USE_RZ_FSP_GTM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RZ FSP GTM 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RZ_FSP
```

**被选择（Selected by）**

```text
CONFIG_COUNTER_RENESAS_RZ_GTM
CONFIG_RZ_OS_TIMER
```

**定义位置（Location）**：[`modules/Kconfig.renesas:392`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L392)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RZ_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RZ_FSP)、[`CONFIG_COUNTER_RENESAS_RZ_GTM`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_RENESAS_RZ_GTM)、[`CONFIG_RZ_OS_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_RZ_OS_TIMER)。

<a id="CONFIG_USE_RZ_FSP_IIC_MASTER"></a>

## 209.92 `CONFIG_USE_RZ_FSP_IIC_MASTER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RZ FSP IIC 主控制器（MASTER）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RZ_FSP
```

**被选择（Selected by）**

```text
CONFIG_I2C_RENESAS_RZ_IIC
```

**定义位置（Location）**：[`modules/Kconfig.renesas:382`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L382)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RZ_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RZ_FSP)、[`CONFIG_I2C_RENESAS_RZ_IIC`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RENESAS_RZ_IIC)。

<a id="CONFIG_USE_RZ_FSP_IOPORT"></a>

## 209.93 `CONFIG_USE_RZ_FSP_IOPORT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RZ FSP 输入／输出端口（IOPORT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RZ_FSP
```

**被选择（Selected by）**

```text
CONFIG_GPIO_RENESAS_RZ
CONFIG_PINCTRL_RENESAS_RZ
```

**定义位置（Location）**：[`modules/Kconfig.renesas:372`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L372)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RZ_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RZ_FSP)、[`CONFIG_GPIO_RENESAS_RZ`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_RENESAS_RZ)、[`CONFIG_PINCTRL_RENESAS_RZ`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL_RENESAS_RZ)。

<a id="CONFIG_USE_RZ_FSP_MHU"></a>

## 209.94 `CONFIG_USE_RZ_FSP_MHU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RZ FSP MHU 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RZ_FSP
```

**被选择（Selected by）**

```text
CONFIG_MBOX_RENESAS_RZ_MHU
```

**定义位置（Location）**：[`modules/Kconfig.renesas:417`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L417)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RZ_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RZ_FSP)、[`CONFIG_MBOX_RENESAS_RZ_MHU`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX_RENESAS_RZ_MHU)。

<a id="CONFIG_USE_RZ_FSP_MIPI_DSI"></a>

## 209.95 `CONFIG_USE_RZ_FSP_MIPI_DSI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RZ FSP MIPI 显示串行接口（MIPI-DSI）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RZ_FSP
```

**被选择（Selected by）**

```text
CONFIG_MIPI_DSI_RENESAS_RZ
```

**定义位置（Location）**：[`modules/Kconfig.renesas:487`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L487)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RZ_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RZ_FSP)、[`CONFIG_MIPI_DSI_RENESAS_RZ`](P122_drivers_mipi_dsi_配置项参考.md#CONFIG_MIPI_DSI_RENESAS_RZ)。

<a id="CONFIG_USE_RZ_FSP_MTU"></a>

## 209.96 `CONFIG_USE_RZ_FSP_MTU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RZ FSP MTU 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RZ_FSP
```

**被选择（Selected by）**

```text
CONFIG_PWM_RENESAS_RZ_MTU
```

**定义位置（Location）**：[`modules/Kconfig.renesas:447`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L447)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RZ_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RZ_FSP)、[`CONFIG_PWM_RENESAS_RZ_MTU`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_RENESAS_RZ_MTU)。

<a id="CONFIG_USE_RZ_FSP_QSPI_SPIBSC"></a>

## 209.97 `CONFIG_USE_RZ_FSP_QSPI_SPIBSC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RZ FSP QSPI SPIBSC 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RZ_FSP
```

**被选择（Selected by）**

```text
CONFIG_FLASH_RENESAS_RZ_QSPI_SPIBSC
```

**定义位置（Location）**：[`modules/Kconfig.renesas:477`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L477)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RZ_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RZ_FSP)、[`CONFIG_FLASH_RENESAS_RZ_QSPI_SPIBSC`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_RENESAS_RZ_QSPI_SPIBSC)。

<a id="CONFIG_USE_RZ_FSP_QSPI_XSPI"></a>

## 209.98 `CONFIG_USE_RZ_FSP_QSPI_XSPI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RZ FSP QSPI XSPI 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RZ_FSP
```

**被选择（Selected by）**

```text
CONFIG_FLASH_RENESAS_RZ_QSPI_XSPI
```

**定义位置（Location）**：[`modules/Kconfig.renesas:472`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L472)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RZ_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RZ_FSP)、[`CONFIG_FLASH_RENESAS_RZ_QSPI_XSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_RENESAS_RZ_QSPI_XSPI)。

<a id="CONFIG_USE_RZ_FSP_RIIC_MASTER"></a>

## 209.99 `CONFIG_USE_RZ_FSP_RIIC_MASTER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RZ FSP RIIC 主控制器（MASTER）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RZ_FSP
```

**被选择（Selected by）**

```text
CONFIG_I2C_RENESAS_RZ_RIIC
```

**定义位置（Location）**：[`modules/Kconfig.renesas:387`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L387)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RZ_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RZ_FSP)、[`CONFIG_I2C_RENESAS_RZ_RIIC`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RENESAS_RZ_RIIC)。

<a id="CONFIG_USE_RZ_FSP_RSPI_SPI"></a>

## 209.100 `CONFIG_USE_RZ_FSP_RSPI_SPI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RZ FSP RSPI 驱动（driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_RENESAS_RZ_FSP
```

**被选择（Selected by）**

```text
CONFIG_SPI_RENESAS_RZ_RSPI
```

**定义位置（Location）**：[`modules/Kconfig.renesas:437`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.renesas#L437)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_HAS_RENESAS_RZ_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RZ_FSP)、[`CONFIG_SPI_RENESAS_RZ_RSPI`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RZ_RSPI)。

<!-- kconfig-navigation -->

[上一章](P208_modules_Kconfig.open-amp_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P210_modules_Kconfig.renesas_配置项参考_2.md)
