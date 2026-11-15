---
id: learning.zephyr-docs.kconfig-reference.page-229
title: "`modules/hal_nxp`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第229章\_`modules/hal_nxp`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/hal_nxp` 的 93 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BT_NXP_PCM_PINS_DIR_REVERSE"></a>

## 229.1 `CONFIG_BT_NXP_PCM_PINS_DIR_REVERSE`

**提示（Prompt）**：反转蓝牙模块 PCM 引脚方向（Reverse pins direction）

**说明（Help）**

启用后，反转蓝牙模块的脉冲编码调制（PCM）引脚方向。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_H4_NXP_CTLR
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:293`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L293)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_BT_H4_NXP_CTLR`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_H4_NXP_CTLR)。

<a id="CONFIG_HAS_MCUX_CACHE"></a>

## 229.2 `CONFIG_HAS_MCUX_CACHE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

SoC 中存在 L1 或 L2 缓存（cache）时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCUX
```

**被选择（Selected by）**

```text
CONFIG_SOC_MCXL255_CPU0
CONFIG_SOC_MCXL254_CPU0
CONFIG_SOC_MCXL253_CPU0
CONFIG_SOC_MCXN947_CPU0
CONFIG_SOC_MCXN547_CPU0
CONFIG_SOC_SERIES_IMXRT10XX
CONFIG_SOC_MIMXRT1189_CM7
CONFIG_SOC_MIMXRT1186_CM7
CONFIG_SOC_MIMXRT1185_CM7
CONFIG_SOC_MIMXRT118C_CM7
CONFIG_SOC_MIMXRT1187_CM7
CONFIG_SOC_SERIES_IMXRT11XX
CONFIG_SOC_MIMXRT595S_CM33
CONFIG_SOC_MIMXRT685S_CM33
CONFIG_SOC_MK66F18
CONFIG_SOC_SERIES_K8X
CONFIG_SOC_SERIES_KE1XF
CONFIG_SOC_MIMX8MM6_A53
CONFIG_SOC_MIMX8ML8_A53
CONFIG_SOC_MIMX8MN6_A53
CONFIG_SOC_MIMX9111
CONFIG_SOC_MIMX9131
CONFIG_SOC_MIMX9352_A55
CONFIG_SOC_MIMX9352_M33
CONFIG_SOC_MIMX94398_A55
CONFIG_SOC_MIMX94398_M7_0
CONFIG_SOC_MIMX94398_M7_1
CONFIG_SOC_MIMX9596_M7
CONFIG_SOC_MIMX9596_A55
CONFIG_SOC_MIMX9529_A55
CONFIG_SOC_MIMX9529_M7
CONFIG_SOC_SERIES_RW6XX
CONFIG_SOC_S32K142
CONFIG_SOC_S32K142W
CONFIG_SOC_S32K144
CONFIG_SOC_S32K144W
CONFIG_SOC_S32K146
CONFIG_SOC_S32K148
CONFIG_SOC_SERIES_S32K3
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:141`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L141)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)、[`CONFIG_SOC_MCXL255_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL255_CPU0)、[`CONFIG_SOC_MCXL254_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL254_CPU0)、[`CONFIG_SOC_MCXL253_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL253_CPU0)、[`CONFIG_SOC_MCXN947_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN947_CPU0)、[`CONFIG_SOC_MCXN547_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN547_CPU0)、[`CONFIG_SOC_SERIES_IMXRT10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT10XX)、[`CONFIG_SOC_MIMXRT1189_CM7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1189_CM7)、[`CONFIG_SOC_MIMXRT1186_CM7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1186_CM7)、[`CONFIG_SOC_MIMXRT1185_CM7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1185_CM7)、[`CONFIG_SOC_MIMXRT118C_CM7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT118C_CM7)、[`CONFIG_SOC_MIMXRT1187_CM7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1187_CM7)、[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_MIMXRT595S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT595S_CM33)、[`CONFIG_SOC_MIMXRT685S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_CM33)、[`CONFIG_SOC_MK66F18`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MK66F18)、[`CONFIG_SOC_SERIES_K8X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K8X)、[`CONFIG_SOC_SERIES_KE1XF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KE1XF)、[`CONFIG_SOC_MIMX8MM6_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8MM6_A53)、[`CONFIG_SOC_MIMX8ML8_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8ML8_A53)、[`CONFIG_SOC_MIMX8MN6_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8MN6_A53)、[`CONFIG_SOC_MIMX9111`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9111)、[`CONFIG_SOC_MIMX9131`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9131)、[`CONFIG_SOC_MIMX9352_A55`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9352_A55)、[`CONFIG_SOC_MIMX9352_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9352_M33)、[`CONFIG_SOC_MIMX94398_A55`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_A55)、[`CONFIG_SOC_MIMX94398_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M7_0)、[`CONFIG_SOC_MIMX94398_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M7_1)、[`CONFIG_SOC_MIMX9596_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9596_M7)、[`CONFIG_SOC_MIMX9596_A55`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9596_A55)、[`CONFIG_SOC_MIMX9529_A55`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9529_A55)、[`CONFIG_SOC_MIMX9529_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9529_M7)、[`CONFIG_SOC_SERIES_RW6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RW6XX)、[`CONFIG_SOC_S32K142`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K142)、[`CONFIG_SOC_S32K142W`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K142W)、[`CONFIG_SOC_S32K144`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K144)、[`CONFIG_SOC_S32K144W`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K144W)、[`CONFIG_SOC_S32K146`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K146)、[`CONFIG_SOC_S32K148`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K148)、[`CONFIG_SOC_SERIES_S32K3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`、`CONFIG_SOC_MCXL255_CPU0`、`CONFIG_SOC_MCXL254_CPU0`、`CONFIG_SOC_MCXL253_CPU0`、`CONFIG_SOC_MCXN947_CPU0`、`CONFIG_SOC_MCXN547_CPU0`、`CONFIG_SOC_SERIES_IMXRT10XX`、`CONFIG_SOC_MIMXRT1189_CM7`、`CONFIG_SOC_MIMXRT1186_CM7`、`CONFIG_SOC_MIMXRT1185_CM7`、`CONFIG_SOC_MIMXRT118C_CM7`、`CONFIG_SOC_MIMXRT1187_CM7`、`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_MIMXRT685S_CM33`、`CONFIG_SOC_MK66F18`、`CONFIG_SOC_SERIES_K8X`、`CONFIG_SOC_SERIES_KE1XF`、`CONFIG_SOC_SERIES_RW6XX`、`CONFIG_SOC_S32K142`、`CONFIG_SOC_S32K142W`、`CONFIG_SOC_S32K144`、`CONFIG_SOC_S32K144W`、`CONFIG_SOC_S32K146`、`CONFIG_SOC_S32K148`、`CONFIG_SOC_SERIES_S32K3`。

<a id="CONFIG_HAS_MCUX_ELS_PKC"></a>

## 229.3 `CONFIG_HAS_MCUX_ELS_PKC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

SoC 中存在 EdgeLock 安全子系统公钥密码加速器（EdgeLock Secure Subsystem - Public Key Cryptography，ELS PKC）时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCUX
```

**被选择（Selected by）**

```text
CONFIG_SOC_MCXN947_CPU0
CONFIG_SOC_MCXN547_CPU0
CONFIG_SOC_MCXN236
CONFIG_SOC_SERIES_RW6XX
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:178`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L178)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)、[`CONFIG_SOC_MCXN947_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN947_CPU0)、[`CONFIG_SOC_MCXN547_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN547_CPU0)、[`CONFIG_SOC_MCXN236`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN236)、[`CONFIG_SOC_SERIES_RW6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RW6XX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`、`CONFIG_SOC_MCXN947_CPU0`、`CONFIG_SOC_MCXN547_CPU0`、`CONFIG_SOC_MCXN236`、`CONFIG_SOC_SERIES_RW6XX`。

<a id="CONFIG_HAS_MCUX_LMEM_CACHE"></a>

## 229.4 `CONFIG_HAS_MCUX_LMEM_CACHE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

SoC 中存在 LMEM 缓存模块（Cache module）时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCUX
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_MCXE24X
CONFIG_SOC_MIMXRT1175_CM4
CONFIG_SOC_MIMXRT1176_CM4
CONFIG_SOC_MIMXRT1166_CM4
CONFIG_SOC_MK66F18
CONFIG_SOC_SERIES_K8X
CONFIG_SOC_SERIES_KE1XF
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:162`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L162)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)、[`CONFIG_SOC_SERIES_MCXE24X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE24X)、[`CONFIG_SOC_MIMXRT1175_CM4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1175_CM4)、[`CONFIG_SOC_MIMXRT1176_CM4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1176_CM4)、[`CONFIG_SOC_MIMXRT1166_CM4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1166_CM4)、[`CONFIG_SOC_MK66F18`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MK66F18)、[`CONFIG_SOC_SERIES_K8X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K8X)、[`CONFIG_SOC_SERIES_KE1XF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KE1XF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`、`CONFIG_SOC_SERIES_MCXE24X`、`CONFIG_SOC_MIMXRT1175_CM4`、`CONFIG_SOC_MIMXRT1176_CM4`、`CONFIG_SOC_MIMXRT1166_CM4`、`CONFIG_SOC_MK66F18`、`CONFIG_SOC_SERIES_K8X`、`CONFIG_SOC_SERIES_KE1XF`。

<a id="CONFIG_HAS_MCUX_MCM_LPCAC"></a>

## 229.5 `CONFIG_HAS_MCUX_MCM_LPCAC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

SoC 中存在由 MCM 控制的 LPCAC 代码缓存模块（code cache module）时设置此项。其启用、禁用和清除通过 MCM `CPCR2` 处理。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCUX
```

**被选择（Selected by）**

```text
CONFIG_SOC_MCXW716C
CONFIG_SOC_MCXW727C
CONFIG_SOC_MCXW70AC
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:200`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L200)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)、[`CONFIG_SOC_MCXW716C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXW716C)、[`CONFIG_SOC_MCXW727C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXW727C)、[`CONFIG_SOC_MCXW70AC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXW70AC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`、`CONFIG_SOC_MCXW716C`、`CONFIG_SOC_MCXW727C`、`CONFIG_SOC_MCXW70AC`。

<a id="CONFIG_HAS_MCUX_RDC"></a>

## 229.6 `CONFIG_HAS_MCUX_RDC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

SoC 中存在 RDC 模块（module）时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCUX
```

**被选择（Selected by）**

```text
CONFIG_SOC_MIMX8MM6_A53
CONFIG_SOC_MIMX8MM6_M4
CONFIG_SOC_MIMX8ML8_A53
CONFIG_SOC_MIMX8MN6_A53
CONFIG_SOC_MIMX8ML8_M7
CONFIG_SOC_MIMX8MQ6_M4
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:152`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L152)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)、[`CONFIG_SOC_MIMX8MM6_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8MM6_A53)、[`CONFIG_SOC_MIMX8MM6_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8MM6_M4)、[`CONFIG_SOC_MIMX8ML8_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8ML8_A53)、[`CONFIG_SOC_MIMX8MN6_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8MN6_A53)、[`CONFIG_SOC_MIMX8ML8_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8ML8_M7)、[`CONFIG_SOC_MIMX8MQ6_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8MQ6_M4)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`。

<a id="CONFIG_HAS_MCUX_SGI_PKC"></a>

## 229.7 `CONFIG_HAS_MCUX_SGI_PKC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

SoC 中存在安全网关接口公钥密码加速器（Secure Gateway Interface - Public Key Cryptography，SGI PKC）时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCUX
```

**被选择（Selected by）**

```text
CONFIG_SOC_MCXA266
CONFIG_SOC_MCXA366
CONFIG_SOC_MCXA577
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:172`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L172)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)、[`CONFIG_SOC_MCXA266`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXA266)、[`CONFIG_SOC_MCXA366`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXA366)、[`CONFIG_SOC_MCXA577`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXA577)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`、`CONFIG_SOC_MCXA266`、`CONFIG_SOC_MCXA366`、`CONFIG_SOC_MCXA577`。

<a id="CONFIG_HAS_MCUX_SRC"></a>

## 229.8 `CONFIG_HAS_MCUX_SRC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

SoC 中存在系统复位控制器（System Reset Controller，SRC）模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCUX
```

**被选择（Selected by）**

```text
CONFIG_SOC_MIMXRT1024
CONFIG_SOC_MIMXRT1051
CONFIG_SOC_MIMXRT1052
CONFIG_SOC_MIMXRT1062
CONFIG_SOC_MIMXRT1064
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:146`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L146)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)、[`CONFIG_SOC_MIMXRT1024`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1024)、[`CONFIG_SOC_MIMXRT1051`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1051)、[`CONFIG_SOC_MIMXRT1052`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1052)、[`CONFIG_SOC_MIMXRT1062`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1062)、[`CONFIG_SOC_MIMXRT1064`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1064)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`、`CONFIG_SOC_MIMXRT1024`、`CONFIG_SOC_MIMXRT1051`、`CONFIG_SOC_MIMXRT1052`、`CONFIG_SOC_MIMXRT1062`、`CONFIG_SOC_MIMXRT1064`。

<a id="CONFIG_HAS_MCUX_SYSCON_LPCAC"></a>

## 229.9 `CONFIG_HAS_MCUX_SYSCON_LPCAC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

SoC 中存在 SYSCON LPCAC 模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCUX
```

**被选择（Selected by）**

```text
CONFIG_SOC_LPC55S36
CONFIG_SOC_FAMILY_MCXA
CONFIG_SOC_MCXN947_CPU0
CONFIG_SOC_MCXN547_CPU0
CONFIG_SOC_MCXN236
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:167`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L167)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)、[`CONFIG_SOC_LPC55S36`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S36)、[`CONFIG_SOC_FAMILY_MCXA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXA)、[`CONFIG_SOC_MCXN947_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN947_CPU0)、[`CONFIG_SOC_MCXN547_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN547_CPU0)、[`CONFIG_SOC_MCXN236`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN236)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`、`CONFIG_SOC_LPC55S36`、`CONFIG_SOC_FAMILY_MCXA`、`CONFIG_SOC_MCXN947_CPU0`、`CONFIG_SOC_MCXN547_CPU0`、`CONFIG_SOC_MCXN236`。

<a id="CONFIG_HAS_MCUX_SYSINIT_DISABLE_WDOG"></a>

## 229.10 `CONFIG_HAS_MCUX_SYSINIT_DISABLE_WDOG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

由 MCUX CMSIS `SystemInit()` 会遵从 `DISABLE_WDOG` 宏、据此控制启动时硬件看门狗（hardware watchdog）的 SoC 设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCUX
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_MCXE24X
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:184`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L184)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)、[`CONFIG_SOC_SERIES_MCXE24X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE24X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`、`CONFIG_SOC_SERIES_MCXE24X`。

<a id="CONFIG_HAS_MCUX_XCACHE"></a>

## 229.11 `CONFIG_HAS_MCUX_XCACHE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

SoC 中存在 XCACHE 模块时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCUX
```

**被选择（Selected by）**

```text
CONFIG_SOC_MIMXRT1189_CM33
CONFIG_SOC_MIMXRT1186_CM33
CONFIG_SOC_MIMXRT1185_CM33
CONFIG_SOC_MIMXRT118C_CM33
CONFIG_SOC_MIMXRT1187_CM33
CONFIG_SOC_MIMXRT1182
CONFIG_SOC_MIMXRT1181
CONFIG_SOC_MIMXRT798S_CM33_CPU0
CONFIG_SOC_MIMXRT758S_CM33_CPU0
CONFIG_SOC_MIMXRT735S_CM33_CPU0
CONFIG_SOC_MIMX94398_M33
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:157`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L157)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)、[`CONFIG_SOC_MIMXRT1189_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1189_CM33)、[`CONFIG_SOC_MIMXRT1186_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1186_CM33)、[`CONFIG_SOC_MIMXRT1185_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1185_CM33)、[`CONFIG_SOC_MIMXRT118C_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT118C_CM33)、[`CONFIG_SOC_MIMXRT1187_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1187_CM33)、[`CONFIG_SOC_MIMXRT1182`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1182)、[`CONFIG_SOC_MIMXRT1181`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1181)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT758S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT735S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_CM33_CPU0)、[`CONFIG_SOC_MIMX94398_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M33)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`、`CONFIG_SOC_MIMXRT1189_CM33`、`CONFIG_SOC_MIMXRT1186_CM33`、`CONFIG_SOC_MIMXRT1185_CM33`、`CONFIG_SOC_MIMXRT118C_CM33`、`CONFIG_SOC_MIMXRT1187_CM33`、`CONFIG_SOC_MIMXRT1182`、`CONFIG_SOC_MIMXRT1181`、`CONFIG_SOC_MIMXRT798S_CM33_CPU0`、`CONFIG_SOC_MIMXRT758S_CM33_CPU0`、`CONFIG_SOC_MIMXRT735S_CM33_CPU0`。

<a id="CONFIG_HAS_NXP_MONOLITHIC_NBU"></a>

## 229.12 `CONFIG_HAS_NXP_MONOLITHIC_NBU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

平台支持蓝牙／802.15.4 应用的单体构建（monolithic build）时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCUX
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_RW6XX
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:206`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L206)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)、[`CONFIG_SOC_SERIES_RW6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RW6XX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`、`CONFIG_SOC_SERIES_RW6XX`。

<a id="CONFIG_MCUX_CODE_QUICK_ACCESS_CUSTOM"></a>

## 229.13 `CONFIG_MCUX_CODE_QUICK_ACCESS_CUSTOM`

**提示（Prompt）**：使用自定义 CodeQuickAccess 放置方式（placement）

**说明（Help）**

不添加 MCUX SDK 默认的 `CodeQuickAccess` 链接器片段（linker snippet）。开发板或应用必须根据需要提供接收 `CodeQuickAccess` 输入段（input section）的链接器片段。如果此段放在非标准内存区域，开发板或应用必须确保执行之前将代码加载或复制到该区域。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUX_CODE_QUICK_ACCESS_PLACEMENT>
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → MCUX SDK CodeQuickAccess 放置方式（placement）

**配置项引用（Symbol References）**：[`CONFIG_MCUX_CODE_QUICK_ACCESS_PLACEMENT`](P229_modules_hal_nxp_配置项参考.md#CONFIG_MCUX_CODE_QUICK_ACCESS_PLACEMENT)。

<a id="CONFIG_MCUX_CODE_QUICK_ACCESS_ITCM"></a>

## 229.14 `CONFIG_MCUX_CODE_QUICK_ACCESS_ITCM`

**提示（Prompt）**：将 CodeQuickAccess 放置在 zephyr,itcm 中

**说明（Help）**

将 `CodeQuickAccess` 放置在设备树 chosen 节点 `zephyr,itcm` 选择的指令紧耦合存储器（ITCM）段中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → MCUX SDK CodeQuickAccess 放置方式（placement）

<a id="CONFIG_MCUX_CODE_QUICK_ACCESS_PLACEMENT"></a>

## 229.15 `CONFIG_MCUX_CODE_QUICK_ACCESS_PLACEMENT`

**提示（Prompt）**：MCUX SDK CodeQuickAccess 放置方式（placement）

**说明（Help）**

选择 MCUX SDK `CodeQuickAccess` 输入段（input section）的放置位置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_M && CONFIG_HAS_MCUX
```

**默认值（Defaults）**

```text
CONFIG_MCUX_CODE_QUICK_ACCESS_RAMFUNC if CONFIG_ARCH_HAS_RAMFUNC_SUPPORT
CONFIG_MCUX_CODE_QUICK_ACCESS_CUSTOM
```

**可选项（Choices）**

```text
CONFIG_MCUX_CODE_QUICK_ACCESS_RAMFUNC
CONFIG_MCUX_CODE_QUICK_ACCESS_ITCM
CONFIG_MCUX_CODE_QUICK_ACCESS_CUSTOM
CONFIG_MCUX_CODE_QUICK_ACCESS_RAMFUNC
CONFIG_MCUX_CODE_QUICK_ACCESS_ITCM
CONFIG_MCUX_CODE_QUICK_ACCESS_CUSTOM
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)、[`CONFIG_MCUX_CODE_QUICK_ACCESS_RAMFUNC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_MCUX_CODE_QUICK_ACCESS_RAMFUNC)、[`CONFIG_ARCH_HAS_RAMFUNC_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_RAMFUNC_SUPPORT)、[`CONFIG_MCUX_CODE_QUICK_ACCESS_CUSTOM`](P229_modules_hal_nxp_配置项参考.md#CONFIG_MCUX_CODE_QUICK_ACCESS_CUSTOM)、[`CONFIG_MCUX_CODE_QUICK_ACCESS_ITCM`](P229_modules_hal_nxp_配置项参考.md#CONFIG_MCUX_CODE_QUICK_ACCESS_ITCM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`、`CONFIG_ARCH_HAS_RAMFUNC_SUPPORT`。

<a id="CONFIG_MCUX_CODE_QUICK_ACCESS_RAMFUNC"></a>

## 229.16 `CONFIG_MCUX_CODE_QUICK_ACCESS_RAMFUNC`

**提示（Prompt）**：将 CodeQuickAccess 放置在 ramfunc 中

**说明（Help）**

将 `CodeQuickAccess` 放置在 Zephyr `ramfunc` 段中。启用 ramfunc 支持时，这会保留现有行为。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_HAS_RAMFUNC_SUPPORT && <choice CONFIG_MCUX_CODE_QUICK_ACCESS_PLACEMENT>
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → MCUX SDK CodeQuickAccess 放置方式（placement）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_HAS_RAMFUNC_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_RAMFUNC_SUPPORT)、[`CONFIG_MCUX_CODE_QUICK_ACCESS_PLACEMENT`](P229_modules_hal_nxp_配置项参考.md#CONFIG_MCUX_CODE_QUICK_ACCESS_PLACEMENT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_RAMFUNC_SUPPORT`。

<a id="CONFIG_MCUX_CORE_SUFFIX"></a>

## 229.17 `CONFIG_MCUX_CORE_SUFFIX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

描述在使用双核器件（dual core parts）时 MCUX SDK 所用核心标识符（core identifier）的字符串。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCUX
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:135`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L135)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`。

<a id="CONFIG_MCUX_DATA_QUICK_ACCESS_CUSTOM"></a>

## 229.18 `CONFIG_MCUX_DATA_QUICK_ACCESS_CUSTOM`

**提示（Prompt）**：使用自定义 DataQuickAccess 放置方式（placement）

**说明（Help）**

不添加 MCUX SDK 默认的 `DataQuickAccess` 链接器片段（linker snippet）。开发板或应用必须提供接收 `DataQuickAccess` 输入段（input section）的链接器片段。如果此段包含已初始化数据并放在非标准内存区域，开发板或应用必须确保使用之前将数据从 ROM 复制到该区域。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUX_DATA_QUICK_ACCESS_PLACEMENT>
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → MCUX SDK DataQuickAccess 放置方式（placement）

**配置项引用（Symbol References）**：[`CONFIG_MCUX_DATA_QUICK_ACCESS_PLACEMENT`](P229_modules_hal_nxp_配置项参考.md#CONFIG_MCUX_DATA_QUICK_ACCESS_PLACEMENT)。

<a id="CONFIG_MCUX_DATA_QUICK_ACCESS_DTCM"></a>

## 229.19 `CONFIG_MCUX_DATA_QUICK_ACCESS_DTCM`

**提示（Prompt）**：将 DataQuickAccess 放置在 zephyr,dtcm 中

**说明（Help）**

将 `DataQuickAccess` 放置在设备树 chosen 节点 `zephyr,dtcm` 选择的数据紧耦合存储器（DTCM）数据段中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → MCUX SDK DataQuickAccess 放置方式（placement）

<a id="CONFIG_MCUX_DATA_QUICK_ACCESS_PLACEMENT"></a>

## 229.20 `CONFIG_MCUX_DATA_QUICK_ACCESS_PLACEMENT`

**提示（Prompt）**：MCUX SDK DataQuickAccess 放置方式（placement）

**说明（Help）**

选择 MCUX SDK `DataQuickAccess` 输入段（input section）的放置位置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_M && CONFIG_HAS_MCUX
```

**默认值（Defaults）**

```text
CONFIG_MCUX_DATA_QUICK_ACCESS_SRAM
```

**可选项（Choices）**

```text
CONFIG_MCUX_DATA_QUICK_ACCESS_SRAM
CONFIG_MCUX_DATA_QUICK_ACCESS_DTCM
CONFIG_MCUX_DATA_QUICK_ACCESS_CUSTOM
CONFIG_MCUX_DATA_QUICK_ACCESS_SRAM
CONFIG_MCUX_DATA_QUICK_ACCESS_DTCM
CONFIG_MCUX_DATA_QUICK_ACCESS_CUSTOM
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)、[`CONFIG_MCUX_DATA_QUICK_ACCESS_SRAM`](P229_modules_hal_nxp_配置项参考.md#CONFIG_MCUX_DATA_QUICK_ACCESS_SRAM)、[`CONFIG_MCUX_DATA_QUICK_ACCESS_DTCM`](P229_modules_hal_nxp_配置项参考.md#CONFIG_MCUX_DATA_QUICK_ACCESS_DTCM)、[`CONFIG_MCUX_DATA_QUICK_ACCESS_CUSTOM`](P229_modules_hal_nxp_配置项参考.md#CONFIG_MCUX_DATA_QUICK_ACCESS_CUSTOM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`。

<a id="CONFIG_MCUX_DATA_QUICK_ACCESS_SRAM"></a>

## 229.21 `CONFIG_MCUX_DATA_QUICK_ACCESS_SRAM`

**提示（Prompt）**：将 DataQuickAccess 放置在 zephyr,sram 中

**说明（Help）**

将 `DataQuickAccess` 放置在 Zephyr 常规读写数据段（read-write data section）中。这会保留现有行为。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUX_DATA_QUICK_ACCESS_PLACEMENT>
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → MCUX SDK DataQuickAccess 放置方式（placement）

**配置项引用（Symbol References）**：[`CONFIG_MCUX_DATA_QUICK_ACCESS_PLACEMENT`](P229_modules_hal_nxp_配置项参考.md#CONFIG_MCUX_DATA_QUICK_ACCESS_PLACEMENT)。

<a id="CONFIG_MCUX_ELS_PKC"></a>

## 229.22 `CONFIG_MCUX_ELS_PKC`

**提示（Prompt）**：构建 els_pkc

**说明（Help）**

将 NXP MCU SDK 的 `els_pkc` 组件纳入构建。在集成 ELS PKC 加速器（accelerator）的 SoC 上启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCUX_ELS_PKC
```

**默认值（Defaults）**

```text
y if CONFIG_BUILD_WITH_TFM
y if CONFIG_MBEDTLS_PSA_CRYPTO_C
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.els_pkc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.els_pkc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX_ELS_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_HAS_MCUX_ELS_PKC)、[`CONFIG_BUILD_WITH_TFM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_WITH_TFM)、[`CONFIG_MBEDTLS_PSA_CRYPTO_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PSA_CRYPTO_C)。

<a id="CONFIG_MCUX_ELS_PKC_ENABLE_KEY_DERIVATION"></a>

## 229.23 `CONFIG_MCUX_ELS_PKC_ENABLE_KEY_DERIVATION`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

构建密钥派生（key derivation，HKDF／PBKDF2／NIST SP800-108／SP800-56C）和 RSA 密钥类型（key-type）源文件。它们提供 RT700／MIMXRT7xx 等平台所需的描述符符号（descriptor symbols）：`mcuxClKey_DerivationAlgorithmDescriptor_*`、`mcuxClKey_TypeDescriptor_derivationKey_variableLength` 和 `mcuxClKey_TypeDescriptor_Rsa_*`。不使用这组功能的平台，例如 MCXN、RW61x，保持禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y if CONFIG_SOC_SERIES_IMXRT7XX
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.els_pkc:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.els_pkc#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT7XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT7XX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT7XX`。

<a id="CONFIG_MCUX_ELS_PKC_TRNG_USE_ELS"></a>

## 229.24 `CONFIG_MCUX_ELS_PKC_TRNG_USE_ELS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

选择 `els_pkc` 使用的真随机数发生器（TRNG）来源。一些平台，例如 MCXN 和 RT700／MIMXRT7xx，没有独立 `SA_TRNG` 外设，而使用 ELS 内部 TRNG（`MCUXCL_FEATURE_TRNG_ELS`）；另一些平台，例如 RW61x，使用独立 `SA_TRNG`。启用时构建 `mcuxClTrng_ELS.c`，否则构建 `mcuxClTrng_SA_TRNG.c`。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y if CONFIG_SOC_FAMILY_MCXN || CONFIG_SOC_SERIES_IMXRT7XX
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.els_pkc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.els_pkc#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MCXN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXN)、[`CONFIG_SOC_SERIES_IMXRT7XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT7XX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MCXN`、`CONFIG_SOC_SERIES_IMXRT7XX`。

<a id="CONFIG_MCUX_NONCACHEABLE_CUSTOM"></a>

## 229.25 `CONFIG_MCUX_NONCACHEABLE_CUSTOM`

**提示（Prompt）**：使用自定义 NonCacheable 放置方式（placement）

**说明（Help）**

不添加 MCUX SDK 默认的 `NonCacheable` 和 `NonCacheable.init` 链接器片段（linker snippets）。开发板或应用必须根据需要提供接收这些输入段（input sections）的链接器片段。如果 `NonCacheable.init` 放在非标准内存区域，开发板或应用必须确保使用之前将已初始化数据从 ROM 复制到该区域。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUX_NONCACHEABLE_PLACEMENT>
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:123`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L123)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → MCUX SDK NonCacheable 放置方式（placement）

**配置项引用（Symbol References）**：[`CONFIG_MCUX_NONCACHEABLE_PLACEMENT`](P229_modules_hal_nxp_配置项参考.md#CONFIG_MCUX_NONCACHEABLE_PLACEMENT)。

<a id="CONFIG_MCUX_NONCACHEABLE_NOCACHE"></a>

## 229.26 `CONFIG_MCUX_NONCACHEABLE_NOCACHE`

**提示（Prompt）**：将 NonCacheable 段放在 Zephyr 不缓存内存（nocache memory）中

**说明（Help）**

将 `NonCacheable` 和 `NonCacheable.init` 输入段（input sections）放在 Zephyr `nocache` 段中。启用不缓存内存支持（nocache memory support）时，这会保留现有行为。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NOCACHE_MEMORY && <choice CONFIG_MCUX_NONCACHEABLE_PLACEMENT>
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → MCUX SDK NonCacheable 放置方式（placement）

**配置项引用（Symbol References）**：[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_MCUX_NONCACHEABLE_PLACEMENT`](P229_modules_hal_nxp_配置项参考.md#CONFIG_MCUX_NONCACHEABLE_PLACEMENT)。

<a id="CONFIG_MCUX_NONCACHEABLE_PLACEMENT"></a>

## 229.27 `CONFIG_MCUX_NONCACHEABLE_PLACEMENT`

**提示（Prompt）**：MCUX SDK NonCacheable 放置方式（placement）

**说明（Help）**

选择 MCUX SDK `NonCacheable` 和 `NonCacheable.init` 输入段（input sections）的放置位置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCUX
```

**默认值（Defaults）**

```text
CONFIG_MCUX_NONCACHEABLE_NOCACHE if CONFIG_NOCACHE_MEMORY
CONFIG_MCUX_NONCACHEABLE_CUSTOM
```

**可选项（Choices）**

```text
CONFIG_MCUX_NONCACHEABLE_NOCACHE
CONFIG_MCUX_NONCACHEABLE_CUSTOM
CONFIG_MCUX_NONCACHEABLE_NOCACHE
CONFIG_MCUX_NONCACHEABLE_CUSTOM
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)、[`CONFIG_MCUX_NONCACHEABLE_NOCACHE`](P229_modules_hal_nxp_配置项参考.md#CONFIG_MCUX_NONCACHEABLE_NOCACHE)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_MCUX_NONCACHEABLE_CUSTOM`](P229_modules_hal_nxp_配置项参考.md#CONFIG_MCUX_NONCACHEABLE_CUSTOM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`。

<a id="CONFIG_MCUX_OPTIMIZED_MEMCPY"></a>

## 229.28 `CONFIG_MCUX_OPTIMIZED_MEMCPY`

**提示（Prompt）**：使用 NXP 优化的 memcpy

**说明（Help）**

使用 NXP 优化的汇编版（assembly）`memcpy`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MINIMAL_LIBC && CONFIG_CPU_CORTEX_M && !CONFIG_ARMV6_M_ARMV8_M_BASELINE && CONFIG_HAS_MCUX
```

**默认值（Defaults）**

```text
y if "" = "gnu"
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_MINIMAL_LIBC`](P197_lib_配置项参考_1.md#CONFIG_MINIMAL_LIBC)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARMV6_M_ARMV8_M_BASELINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV6_M_ARMV8_M_BASELINE)、[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`。

<a id="CONFIG_MCUX_OPTIMIZED_MEMSET"></a>

## 229.29 `CONFIG_MCUX_OPTIMIZED_MEMSET`

**提示（Prompt）**：使用 NXP 优化的 memset

**说明（Help）**

使用 NXP 优化的汇编版（assembly）`memset`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MINIMAL_LIBC && CONFIG_CPU_CORTEX_M && !CONFIG_ARMV6_M_ARMV8_M_BASELINE && CONFIG_HAS_MCUX
```

**默认值（Defaults）**

```text
y if "" = "gnu"
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_MINIMAL_LIBC`](P197_lib_配置项参考_1.md#CONFIG_MINIMAL_LIBC)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARMV6_M_ARMV8_M_BASELINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV6_M_ARMV8_M_BASELINE)、[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`。

<a id="CONFIG_MCUX_PSA_CRYPTO_DRIVER_ELS_PKC"></a>

## 229.30 `CONFIG_MCUX_PSA_CRYPTO_DRIVER_ELS_PKC`

**提示（Prompt）**：为 els_pkc 构建 psa_crypto_driver

**说明（Help）**

将 NXP MCU SDK 的 `psa_crypto_driver` 组件纳入构建。该组件在 `els_pkc` 之上提供抽象层（abstraction），使 mbedtls 能够通过 `mbedtls psa_crypto_driver_wrapper` 使用 `els_pkc` 提供的硬件加速（hardware acceleration）。在集成 ELS PKC 加速器的 SoC 上默认启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_PSA_CRYPTO_C && CONFIG_MCUX_ELS_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.psa_crypto_driver:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.psa_crypto_driver#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_PSA_CRYPTO_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PSA_CRYPTO_C)、[`CONFIG_MCUX_ELS_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_MCUX_ELS_PKC)。

<a id="CONFIG_MCUX_PSA_CRYPTO_DRIVER_ELS_PKC_THREAD"></a>

## 229.31 `CONFIG_MCUX_PSA_CRYPTO_DRIVER_ELS_PKC_THREAD`

**提示（Prompt）**：psa-crypto-driver 的线程支持（Threading support）

**说明（Help）**

启用 `psa-crypto-driver` 组件的线程支持（threading support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUX_ELS_PKC && CONFIG_MCUX_PSA_CRYPTO_DRIVER_ELS_PKC
```

**默认值（Defaults）**

```text
n if CONFIG_BUILD_WITH_TFM
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.psa_crypto_driver:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.psa_crypto_driver#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → 为 els_pkc 构建 psa_crypto_driver

**配置项引用（Symbol References）**：[`CONFIG_MCUX_ELS_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_MCUX_ELS_PKC)、[`CONFIG_MCUX_PSA_CRYPTO_DRIVER_ELS_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_MCUX_PSA_CRYPTO_DRIVER_ELS_PKC)、[`CONFIG_BUILD_WITH_TFM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_MCUX_PSA_CRYPTO_DRIVER_USE_ELS_PKC_SHA1"></a>

## 229.32 `CONFIG_MCUX_PSA_CRYPTO_DRIVER_USE_ELS_PKC_SHA1`

**提示（Prompt）**：通过 psa-crypto-driver 使用 els-pkc 的 SHA1

**说明（Help）**

通过 `psa-crypto-driver` 组件启用 `els-pkc` 的 SHA1 功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUX_ELS_PKC && CONFIG_MCUX_PSA_CRYPTO_DRIVER_ELS_PKC
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.psa_crypto_driver:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.psa_crypto_driver#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → 为 els_pkc 构建 psa_crypto_driver

**配置项引用（Symbol References）**：[`CONFIG_MCUX_ELS_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_MCUX_ELS_PKC)、[`CONFIG_MCUX_PSA_CRYPTO_DRIVER_ELS_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_MCUX_PSA_CRYPTO_DRIVER_ELS_PKC)。

<a id="CONFIG_MCUX_SYSINIT_KEEP_WATCHDOG"></a>

## 229.33 `CONFIG_MCUX_SYSINIT_KEEP_WATCHDOG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

设置后，为 MCUX HAL 定义 `DISABLE_WDOG=0`，使 CMSIS `SystemInit()` 保持硬件看门狗（hardware watchdog）运行，由 Zephyr 看门狗驱动管理。否则，CMSIS 按默认行为在启动时禁用看门狗。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCUX_SYSINIT_DISABLE_WDOG && CONFIG_HAS_MCUX
```

**默认值（Defaults）**

```text
y if CONFIG_WATCHDOG && CONFIG_HAS_WDT_DISABLE_AT_BOOT && !CONFIG_WDT_DISABLE_AT_BOOT
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:190`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L190)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX_SYSINIT_DISABLE_WDOG`](P229_modules_hal_nxp_配置项参考.md#CONFIG_HAS_MCUX_SYSINIT_DISABLE_WDOG)、[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_DISABLE_AT_BOOT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_DISABLE_AT_BOOT)、[`CONFIG_WDT_DISABLE_AT_BOOT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_DISABLE_AT_BOOT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`。

<a id="CONFIG_NXP_COMPRESSED_WIFI_NB_FW"></a>

## 229.34 `CONFIG_NXP_COMPRESSED_WIFI_NB_FW`

**提示（Prompt）**：使用压缩的 Wi-Fi 或窄带固件（compressed Wi-Fi or NB firmware）

**说明（Help）**

启用后，使用压缩的 Wi-Fi 或窄带（Narrowband）固件镜像。压缩固件可降低闪存（flash memory）占用，但下载后必须在初始化阶段解压，从而增加启动时间和初始化延迟（initialization latency）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NXP_MONOLITHIC_WIFI || CONFIG_NXP_MONOLITHIC_NBU) && CONFIG_HAS_MCUX
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:217`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L217)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_NXP_MONOLITHIC_WIFI`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_MONOLITHIC_WIFI)、[`CONFIG_NXP_MONOLITHIC_NBU`](P229_modules_hal_nxp_配置项参考.md#CONFIG_NXP_MONOLITHIC_NBU)、[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`。

<a id="CONFIG_NXP_FW_LOADER"></a>

## 229.35 `CONFIG_NXP_FW_LOADER`

**提示（Prompt）**：包含固件加载器组件（firmware loader component）

**说明（Help）**

固件加载器（firmware loader）用于向嵌入式收发器（embedded transceivers）加载固件，是启用连接功能（connectivity features）所必需的。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCUX
```

**被选择（Selected by）**

```text
CONFIG_NXP_RW610
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:211`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L211)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)、[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`。

<a id="CONFIG_NXP_IEEE802154_MAC"></a>

## 229.36 `CONFIG_NXP_IEEE802154_MAC`

**提示（Prompt）**：使用 MAC 核间消息传递的窄带单元（Narrowband Unit，15.4）

**说明（Help）**

启用后，设备使用的窄带单元（NBU）固件将使用 802.15.4 MAC 接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_IEEE802154 && CONFIG_HAS_MCUX
```

**默认值（Defaults）**

```text
y if CONFIG_OPENTHREAD_RADIO_VENDOR_IMPLEMENTATION
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:240`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L240)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)、[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)、[`CONFIG_OPENTHREAD_RADIO_VENDOR_IMPLEMENTATION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_RADIO_VENDOR_IMPLEMENTATION)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`。

<a id="CONFIG_NXP_MCXW7X_BLE_CTRL"></a>

## 229.37 `CONFIG_NXP_MCXW7X_BLE_CTRL`

**提示（Prompt）**：包含 MCXW7X NXP 低功耗蓝牙控制器（BLE Controller）

**说明（Help）**

启用后，包含 MCXW7X NXP 低功耗蓝牙控制器（BLE Controller）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_NBU && CONFIG_HAS_MCUX
```

**被选择（Selected by）**

```text
CONFIG_SOC_MCXW716C
CONFIG_SOC_MCXW727C
CONFIG_SOC_MCXW70AC
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:254`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L254)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_NXP_NBU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_NBU)、[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)、[`CONFIG_SOC_MCXW716C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXW716C)、[`CONFIG_SOC_MCXW727C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXW727C)、[`CONFIG_SOC_MCXW70AC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXW70AC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`、`CONFIG_SOC_MCXW716C`、`CONFIG_SOC_MCXW727C`、`CONFIG_SOC_MCXW70AC`。

<a id="CONFIG_NXP_MONOLITHIC_NBU"></a>

## 229.38 `CONFIG_NXP_MONOLITHIC_NBU`

**提示（Prompt）**：窄带单元（BT／15.4）固件单体构建（monolithic build）

**说明（Help）**

启用后，设备使用的窄带单元（NBU）固件将直接与应用链接（link）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NXP_MONOLITHIC_NBU && CONFIG_HAS_MCUX
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:227`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L227)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NXP_MONOLITHIC_NBU`](P229_modules_hal_nxp_配置项参考.md#CONFIG_HAS_NXP_MONOLITHIC_NBU)、[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`。

<a id="CONFIG_NXP_MULTICORE"></a>

## 229.39 `CONFIG_NXP_MULTICORE`

**提示（Prompt）**：NXP 多核管理器（Multicore Manager）支持

**说明（Help）**

包含 NXP 多核管理器（Multicore Manager）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_MCXW716C
CONFIG_SOC_MCXW727C
CONFIG_SOC_MCXW70AC
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/mcux-sdk-ng/middleware/Kconfig.multicore:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/mcux-sdk-ng/middleware/Kconfig.multicore#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MCXW716C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXW716C)、[`CONFIG_SOC_MCXW727C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXW727C)、[`CONFIG_SOC_MCXW70AC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXW70AC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MCXW716C`、`CONFIG_SOC_MCXW727C`、`CONFIG_SOC_MCXW70AC`。

<a id="CONFIG_NXP_NEUTRON"></a>

## 229.40 `CONFIG_NXP_NEUTRON`

**提示（Prompt）**：NXP NEUTRON 神经网络处理单元驱动（NPU Driver）

**说明（Help）**

启用 NXP NEUTRON 神经网络处理单元（Neural Processing Unit）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_IMXRT7XX || CONFIG_SOC_FAMILY_MCXN) && CONFIG_HAS_MCUX
```

**被选择（Selected by）**

```text
CONFIG_TFLM_NXP_NEUTRON
CONFIG_TFLM_NXP_NEUTRON
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:260`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L260)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT7XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT7XX)、[`CONFIG_SOC_FAMILY_MCXN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXN)、[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)、[`CONFIG_TFLM_NXP_NEUTRON`](P229_modules_hal_nxp_配置项参考.md#CONFIG_TFLM_NXP_NEUTRON)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT7XX`、`CONFIG_SOC_FAMILY_MCXN`、`CONFIG_HAS_MCUX`。

<a id="CONFIG_NXP_RF_IMU"></a>

## 229.41 `CONFIG_NXP_RF_IMU`

**提示（Prompt）**：包含用于核间消息传递的 RF_IMU 适配器（adapter）

**说明（Help）**

核间消息传递（intercore messaging）需要 RF_IMU 适配器（adapter）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCUX
```

**主动选择（Selects）**

```text
CONFIG_EVENTS
```

**被选择（Selected by）**

```text
CONFIG_NXP_RW610
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:234`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L234)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)、[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`。

<a id="CONFIG_NXP_SNPS_BLE_CTRL"></a>

## 229.42 `CONFIG_NXP_SNPS_BLE_CTRL`

**提示（Prompt）**：包含 NXP SNPS 低功耗蓝牙控制器（BLE Controller）

**说明（Help）**

启用后，包含 NXP SNPS 低功耗蓝牙控制器（BLE Controller）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT && CONFIG_HAS_MCUX
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_MCXW2XX
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:248`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L248)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)、[`CONFIG_SOC_SERIES_MCXW2XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXW2XX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`、`CONFIG_SOC_SERIES_MCXW2XX`。

<a id="CONFIG_NXP_TRDC"></a>

## 229.43 `CONFIG_NXP_TRDC`

**提示（Prompt）**：使用 NXP TRDC 驱动

**说明（Help）**

启用 NXP 可信资源域控制器（Trusted Resource Domain Controller，TRDC）驱动，并引入 `driver.trdc` HAL 组件。供通过主 TRDC 实例路由外设访问的 SoC 使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCUX
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_MCXW727C || CONFIG_SOC_SERIES_IMXRT118X
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:275`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L275)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)、[`CONFIG_SOC_MCXW727C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXW727C)、[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`、`CONFIG_SOC_MCXW727C`、`CONFIG_SOC_SERIES_IMXRT118X`。

<a id="CONFIG_NXP_TRDC_1"></a>

## 229.44 `CONFIG_NXP_TRDC_1`

**提示（Prompt）**：使用 NXP TRDC_1 驱动

**说明（Help）**

启用 NXP `TRDC_1` 驱动，并引入 `driver.trdc_1` HAL 组件。适用于将次级 TRDC 实例暴露为 `TRDC_1` 变体的 SoC。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCUX
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_MIMX9352_M33
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:283`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L283)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)、[`CONFIG_SOC_MIMX9352_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9352_M33)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`。

<a id="CONFIG_PSA_CRYPTO_DRIVER_SGI_PKC"></a>

## 229.45 `CONFIG_PSA_CRYPTO_DRIVER_SGI_PKC`

**提示（Prompt）**：psa-crypto-driver 中的 SGI PKC 支持

**说明（Help）**

启用 `psa-crypto-driver` 组件中的 SGI PKC 支持。在集成 SGI PKC 加速器（accelerator）的 SoC 上默认启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_PSA_CRYPTO_C && CONFIG_HAS_MCUX_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SGI_PKC
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.psa_crypto_driver:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.psa_crypto_driver#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_PSA_CRYPTO_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PSA_CRYPTO_C)、[`CONFIG_HAS_MCUX_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_HAS_MCUX_SGI_PKC)、[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_PSA_CRYPTO_DRIVER_THREAD_EN"></a>

## 229.46 `CONFIG_PSA_CRYPTO_DRIVER_THREAD_EN`

**提示（Prompt）**：PSA Crypto 线程（Thread）

**说明（Help）**

启用 `PSA_CRYPTO_THREAD`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_PSA_CRYPTO_C
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.psa_crypto_driver:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.psa_crypto_driver#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_PSA_CRYPTO_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PSA_CRYPTO_C)。

<a id="CONFIG_SGI_PKC"></a>

## 229.47 `CONFIG_SGI_PKC`

**提示（Prompt）**：NXP SGI PKC 密码库（Cryptographic Library）

**说明（Help）**

启用 NXP 安全网关接口公钥密码（Secure Gateway Interface - Public Key Cryptography，SGI PKC）库支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCUX_SGI_PKC
```

**被选择（Selected by）**

```text
CONFIG_PSA_CRYPTO_DRIVER_SGI_PKC
CONFIG_PSA_CRYPTO_DRIVER_SGI_PKC
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_HAS_MCUX_SGI_PKC)、[`CONFIG_PSA_CRYPTO_DRIVER_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_PSA_CRYPTO_DRIVER_SGI_PKC)。

<a id="CONFIG_SGI_PKC_AEAD"></a>

## 229.48 `CONFIG_SGI_PKC_AEAD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

带关联数据的认证加密（Authenticated Encryption with Associated Data，AEAD）组件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:140`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L140)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_AEAD_MODES"></a>

## 229.49 `CONFIG_SGI_PKC_AEAD_MODES`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

认证加密模式（AEAD modes）组件，包括 CCM、GCM。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:146`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L146)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_AES"></a>

## 229.50 `CONFIG_SGI_PKC_AES`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

高级加密标准（AES）密码组件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:122`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L122)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_BUFFER"></a>

## 229.51 `CONFIG_SGI_PKC_BUFFER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

缓冲区管理组件（Buffer management component）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_CIPHER"></a>

## 229.52 `CONFIG_SGI_PKC_CIPHER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

加解密操作组件（Cipher operations component）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:128`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L128)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_CIPHER_MODES"></a>

## 229.53 `CONFIG_SGI_PKC_CIPHER_MODES`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

分组密码模式组件（Cipher modes component），包括 ECB、CBC、CTR。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:134`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L134)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_CORE"></a>

## 229.54 `CONFIG_SGI_PKC_CORE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

提供基础功能的核心组件（Core component）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_CRC"></a>

## 229.55 `CONFIG_SGI_PKC_CRC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

循环冗余校验（Cyclic Redundancy Check，CRC）组件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:282`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L282)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_CSSL_PRNG"></a>

## 229.56 `CONFIG_SGI_PKC_CSSL_PRNG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CSSL 伪随机数生成器（PRNG）组件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:246`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L246)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_DATA_INTEGRITY"></a>

## 229.57 `CONFIG_SGI_PKC_DATA_INTEGRITY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CSSL 数据完整性（Data Integrity）组件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_DMA"></a>

## 229.58 `CONFIG_SGI_PKC_DMA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

直接内存访问操作（DMA operations）组件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_ECC"></a>

## 229.59 `CONFIG_SGI_PKC_ECC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

椭圆曲线密码（Elliptic Curve Cryptography，ECC）组件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:189`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L189)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_FFDH"></a>

## 229.60 `CONFIG_SGI_PKC_FFDH`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

有限域 Diffie-Hellman（Finite Field Diffie-Hellman，FFDH）组件。仅在 MCXA2xx 平台上可用，没有 mcxa5xx 平台头文件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC_PLATFORM_MCXA && CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:201`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L201)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC_PLATFORM_MCXA`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC_PLATFORM_MCXA)、[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_FLOW_PROTECTION"></a>

## 229.61 `CONFIG_SGI_PKC_FLOW_PROTECTION`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CSSL 控制流保护（Flow Protection）组件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_GLIKEY"></a>

## 229.62 `CONFIG_SGI_PKC_GLIKEY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

用于密钥管理（key management）的 Glikey 组件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:288`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L288)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_HASH"></a>

## 229.63 `CONFIG_SGI_PKC_HASH`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

散列操作（Hash operations）组件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:152`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L152)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_HASHMODES"></a>

## 229.64 `CONFIG_SGI_PKC_HASHMODES`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

散列模式（Hash modes）组件，包括 SHA-224、SHA-256、SHA-384、SHA-512。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:158`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L158)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_HMAC"></a>

## 229.65 `CONFIG_SGI_PKC_HMAC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

基于散列的消息认证码（Hash-based Message Authentication Code，HMAC）组件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:176`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L176)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_KDF_MODES"></a>

## 229.66 `CONFIG_SGI_PKC_KDF_MODES`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

密钥派生函数模式（KDF modes）组件，包括 HKDF、SP800-108、SP800-56C、PBKDF2。仅在 MCXA5xx 平台上可用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC_PLATFORM_MCXA5 && CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:258`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L258)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC_PLATFORM_MCXA5`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC_PLATFORM_MCXA5)、[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_KEY"></a>

## 229.67 `CONFIG_SGI_PKC_KEY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

密钥管理组件（Key management component）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:215`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L215)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_MAC"></a>

## 229.68 `CONFIG_SGI_PKC_MAC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

消息认证码（Message Authentication Code，MAC）组件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:164`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L164)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_MAC_MODES"></a>

## 229.69 `CONFIG_SGI_PKC_MAC_MODES`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

消息认证码模式（MAC modes）组件，包括 CMAC、GMAC、CBC-MAC。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:170`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L170)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_MATH"></a>

## 229.70 `CONFIG_SGI_PKC_MATH`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

用于公钥密码（PKC）的数学运算组件（Mathematical operations component）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:221`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L221)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_MEMORY"></a>

## 229.71 `CONFIG_SGI_PKC_MEMORY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

内存操作组件（Memory operations component），包括 CSSL Memory。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_PADDING"></a>

## 229.72 `CONFIG_SGI_PKC_PADDING`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

填充方案组件（Padding schemes component）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:182`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L182)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_PARAM_INTEGRITY"></a>

## 229.73 `CONFIG_SGI_PKC_PARAM_INTEGRITY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CSSL 参数完整性（Parameter Integrity）组件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_PKC"></a>

## 229.74 `CONFIG_SGI_PKC_PKC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

公钥密码（Public Key Cryptography，PKC）引擎组件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_PLATFORM_MCXA"></a>

## 229.75 `CONFIG_SGI_PKC_PLATFORM_MCXA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

对 MCXA2xx／MCXA3xx SoC 自动启用，选择 mcxa2xx 平台的包含目录（include directories）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_MCXA266 || CONFIG_SOC_MCXA366
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)、[`CONFIG_SOC_MCXA266`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXA266)、[`CONFIG_SOC_MCXA366`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXA366)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MCXA266`、`CONFIG_SOC_MCXA366`。

<a id="CONFIG_SGI_PKC_PLATFORM_MCXA5"></a>

## 229.76 `CONFIG_SGI_PKC_PLATFORM_MCXA5`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

对 MCXA5xx SoC 自动启用，选择 mcxa5xx 平台的包含目录（include directories）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_MCXA577
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)、[`CONFIG_SOC_MCXA577`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXA577)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MCXA577`。

<a id="CONFIG_SGI_PKC_PLATFORM_MCXL"></a>

## 229.77 `CONFIG_SGI_PKC_PLATFORM_MCXL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

对 MCXL2xx SoC 自动启用，选择 mcxl2xx 平台的包含目录（include directories）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_MCXL255
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)、[`CONFIG_SOC_MCXL255`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL255)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MCXL255`。

<a id="CONFIG_SGI_PKC_PLATFORM_MCXW"></a>

## 229.78 `CONFIG_SGI_PKC_PLATFORM_MCXW`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

对 MCXW7xx（W70／KW43）SoC 自动启用，选择 mcxw7x 平台的包含目录（include directories）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_MCXW70AC
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)、[`CONFIG_SOC_MCXW70AC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXW70AC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MCXW70AC`。

<a id="CONFIG_SGI_PKC_PRE_PROCESSOR"></a>

## 229.79 `CONFIG_SGI_PKC_PRE_PROCESSOR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CSSL C 预处理器（C Pre-Processor）组件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_PRNG"></a>

## 229.80 `CONFIG_SGI_PKC_PRNG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

伪随机数生成器（Pseudo Random Number Generator，PRNG）组件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:240`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L240)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_RANDOM"></a>

## 229.81 `CONFIG_SGI_PKC_RANDOM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

随机数生成组件（Random number generation component）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:228`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L228)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_RANDOM_MODES"></a>

## 229.82 `CONFIG_SGI_PKC_RANDOM_MODES`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

随机数模式（Random modes）组件，采用 CTR-DRBG。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:234`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L234)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_RESOURCE"></a>

## 229.83 `CONFIG_SGI_PKC_RESOURCE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

资源管理组件（Resource management component）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_RSA"></a>

## 229.84 `CONFIG_SGI_PKC_RSA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

RSA 密码组件（cryptographic component）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:195`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L195)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_SECURE_COUNTER"></a>

## 229.85 `CONFIG_SGI_PKC_SECURE_COUNTER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CSSL 安全计数器（Secure Counter）组件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_SESSION"></a>

## 229.86 `CONFIG_SGI_PKC_SESSION`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

会话管理组件（Session management component）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_SGI"></a>

## 229.87 `CONFIG_SGI_PKC_SGI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

安全网关接口（Secure Gateway Interface，SGI）驱动组件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:109`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L109)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_SIGNATURE"></a>

## 229.88 `CONFIG_SGI_PKC_SIGNATURE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

数字签名组件（Digital signature component）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:209`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L209)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_TOOLCHAIN"></a>

## 229.89 `CONFIG_SGI_PKC_TOOLCHAIN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

工具链专用定义与宏（Toolchain-specific definitions and macros）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_TRNG"></a>

## 229.90 `CONFIG_SGI_PKC_TRNG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

真随机数生成器（True Random Number Generator，TRNG）组件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:252`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L252)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_XOF"></a>

## 229.91 `CONFIG_SGI_PKC_XOF`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

可扩展输出函数（Extendable Output Function，XOF）组件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC_PLATFORM_MCXA5 && CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:266`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L266)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC_PLATFORM_MCXA5`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC_PLATFORM_MCXA5)、[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_SGI_PKC_XOF_MODES"></a>

## 229.92 `CONFIG_SGI_PKC_XOF_MODES`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

可扩展输出函数模式（XOF modes）组件，包括 SHAKE-128、SHAKE-256。仅在 MCXA5xx 平台上可用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SGI_PKC_PLATFORM_MCXA5 && CONFIG_SGI_PKC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc:273`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/nxp_crypto_hal/Kconfig.sgi_pkc#L273)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → NXP SGI PKC 密码库（Cryptographic Library）

**配置项引用（Symbol References）**：[`CONFIG_SGI_PKC_PLATFORM_MCXA5`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC_PLATFORM_MCXA5)、[`CONFIG_SGI_PKC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_SGI_PKC)。

<a id="CONFIG_TFLM_NXP_NEUTRON"></a>

## 229.93 `CONFIG_TFLM_NXP_NEUTRON`

**提示（Prompt）**：TensorFlow Lite Micro 与 NEUTRON 集成（integration）

**说明（Help）**

启用 TensorFlow Lite Micro 与 NEUTRON 神经网络处理单元（NPU）的集成，使 TFLM 模型可以使用 NEUTRON 加速器进行推理操作（inference operations）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TENSORFLOW_LITE_MICRO && CONFIG_HAS_MCUX
```

**主动选择（Selects）**

```text
CONFIG_NXP_NEUTRON
```

**定义位置（Location）**：[`modules/hal_nxp/mcux/Kconfig.mcux:266`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nxp/mcux/Kconfig.mcux#L266)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_TENSORFLOW_LITE_MICRO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TENSORFLOW_LITE_MICRO)、[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)、[`CONFIG_NXP_NEUTRON`](P229_modules_hal_nxp_配置项参考.md#CONFIG_NXP_NEUTRON)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`。

<!-- kconfig-navigation -->

[上一章](P228_modules_hal_nordic_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P230_modules_hal_realtek_配置项参考.md)
