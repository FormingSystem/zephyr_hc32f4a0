---
id: learning.zephyr-docs.kconfig-reference.page-266
title: "`soc/bflb`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第266章\_`soc/bflb`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/bflb` 的 14 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BFLB_BL616CL_WL_RMEM_SIZE"></a>

## 266.1 `CONFIG_BFLB_BL616CL_WL_RMEM_SIZE`

**提示（Prompt）**：PHY／RF 保留内存大小，单位为字节（retention memory size）

**说明（Help）**

传给 `wl_cfg_get()`、用于保存物理层／射频校准数据（PHY/RF calibration data）的静态缓冲区大小，单位为字节。该缓冲区在应用的整个生命周期内持续存在。8192 与 Bouffalo SDK 的默认值一致。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_BFLB_BL616CL || CONFIG_WIFI_BFLB) && CONFIG_SOC_FAMILY_BFLB
```

**默认值（Defaults）**

```text
8192
```

**定义位置（Location）**：[`soc/bflb/bl616cl/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/bflb/bl616cl/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_BFLB_BL616CL`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB_BL616CL)、[`CONFIG_WIFI_BFLB`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB)、[`CONFIG_SOC_FAMILY_BFLB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_BFLB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_BFLB`。

<a id="CONFIG_BFLB_BL61X_WL_RMEM_SIZE"></a>

## 266.2 `CONFIG_BFLB_BL61X_WL_RMEM_SIZE`

**提示（Prompt）**：PHY／RF 保留内存大小，单位为字节（retention memory size）

**说明（Help）**

传给 `wl_cfg_get()`、用于保存物理层／射频校准数据（PHY/RF calibration data）的静态缓冲区大小，单位为字节。该缓冲区在应用的整个生命周期内持续存在。8192 与 Bouffalo SDK 的默认值一致。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_BFLB_BL61X || CONFIG_WIFI_BFLB || CONFIG_IEEE802154_BFLB) && CONFIG_SOC_FAMILY_BFLB
```

**默认值（Defaults）**

```text
8192
```

**定义位置（Location）**：[`soc/bflb/bl61x/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/bflb/bl61x/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_BFLB_BL61X`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB_BL61X)、[`CONFIG_WIFI_BFLB`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB)、[`CONFIG_IEEE802154_BFLB`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_BFLB)、[`CONFIG_SOC_FAMILY_BFLB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_BFLB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_BFLB`。

<a id="CONFIG_SOC_SERIES_BL60X"></a>

## 266.3 `CONFIG_SOC_SERIES_BL60X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 BouffaloLab BL6xx 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_BFLB
```

**被选择（Selected by）**

```text
CONFIG_SOC_BL602C00Q2I
CONFIG_SOC_BL602C20Q2I
CONFIG_SOC_BL602C20Q2IS
CONFIG_SOC_BL602C40Q2IS
CONFIG_SOC_BL602L10Q2H
CONFIG_SOC_BL602L20Q2H
CONFIG_SOC_BL604E20Q2I
```

**定义位置（Location）**：[`soc/bflb/bl60x/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/bflb/bl60x/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_BFLB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_BFLB)、[`CONFIG_SOC_BL602C00Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL602C00Q2I)、[`CONFIG_SOC_BL602C20Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL602C20Q2I)、[`CONFIG_SOC_BL602C20Q2IS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL602C20Q2IS)、[`CONFIG_SOC_BL602C40Q2IS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL602C40Q2IS)、[`CONFIG_SOC_BL602L10Q2H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL602L10Q2H)、[`CONFIG_SOC_BL602L20Q2H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL602L20Q2H)、[`CONFIG_SOC_BL604E20Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL604E20Q2I)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_BFLB`、`CONFIG_SOC_BL602C00Q2I`、`CONFIG_SOC_BL602C20Q2I`、`CONFIG_SOC_BL602C20Q2IS`、`CONFIG_SOC_BL602C40Q2IS`、`CONFIG_SOC_BL602L10Q2H`、`CONFIG_SOC_BL602L20Q2H`、`CONFIG_SOC_BL604E20Q2I`。

<a id="CONFIG_SOC_SERIES_BL616CL"></a>

## 266.4 `CONFIG_SOC_SERIES_BL616CL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 BouffaloLab BL616CL 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_BFLB
```

**被选择（Selected by）**

```text
CONFIG_SOC_BL616CL3240
CONFIG_SOC_BL616CL3250
CONFIG_SOC_BL616CL3260
CONFIG_SOC_BL616CL4845
CONFIG_SOC_BL616CL4855
CONFIG_SOC_BL616CL4865
CONFIG_SOC_BL616CL4846
CONFIG_SOC_BL616CL4856
CONFIG_SOC_BL616CL4866
```

**定义位置（Location）**：[`soc/bflb/bl616cl/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/bflb/bl616cl/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_BFLB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_BFLB)、[`CONFIG_SOC_BL616CL3240`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL616CL3240)、[`CONFIG_SOC_BL616CL3250`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL616CL3250)、[`CONFIG_SOC_BL616CL3260`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL616CL3260)、[`CONFIG_SOC_BL616CL4845`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL616CL4845)、[`CONFIG_SOC_BL616CL4855`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL616CL4855)、[`CONFIG_SOC_BL616CL4865`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL616CL4865)、[`CONFIG_SOC_BL616CL4846`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL616CL4846)、[`CONFIG_SOC_BL616CL4856`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL616CL4856)、[`CONFIG_SOC_BL616CL4866`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL616CL4866)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_BFLB`、`CONFIG_SOC_BL616CL3240`、`CONFIG_SOC_BL616CL3250`、`CONFIG_SOC_BL616CL3260`、`CONFIG_SOC_BL616CL4845`、`CONFIG_SOC_BL616CL4855`、`CONFIG_SOC_BL616CL4865`、`CONFIG_SOC_BL616CL4846`、`CONFIG_SOC_BL616CL4856`、`CONFIG_SOC_BL616CL4866`。

<a id="CONFIG_SOC_SERIES_BL61X"></a>

## 266.5 `CONFIG_SOC_SERIES_BL61X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 BouffaloLab BL6xx 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_BFLB
```

**被选择（Selected by）**

```text
CONFIG_SOC_BL616C50Q2I
CONFIG_SOC_BL616S50Q2I
CONFIG_SOC_BL618M05Q2I
CONFIG_SOC_BL618M50Q2I
CONFIG_SOC_BL618M65Q2I
```

**定义位置（Location）**：[`soc/bflb/bl61x/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/bflb/bl61x/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_BFLB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_BFLB)、[`CONFIG_SOC_BL616C50Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL616C50Q2I)、[`CONFIG_SOC_BL616S50Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL616S50Q2I)、[`CONFIG_SOC_BL618M05Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL618M05Q2I)、[`CONFIG_SOC_BL618M50Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL618M50Q2I)、[`CONFIG_SOC_BL618M65Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL618M65Q2I)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_BFLB`、`CONFIG_SOC_BL616C50Q2I`、`CONFIG_SOC_BL616S50Q2I`、`CONFIG_SOC_BL618M05Q2I`、`CONFIG_SOC_BL618M50Q2I`、`CONFIG_SOC_BL618M65Q2I`。

<a id="CONFIG_SOC_SERIES_BL70X"></a>

## 266.6 `CONFIG_SOC_SERIES_BL70X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 BouffaloLab BL6xx 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_BFLB
```

**被选择（Selected by）**

```text
CONFIG_SOC_BL702SA0Q2I
CONFIG_SOC_BL702S10Q2I
CONFIG_SOC_BL702C10Q2H
CONFIG_SOC_BL706C00Q2I
CONFIG_SOC_BL706C10Q2I
CONFIG_SOC_BL706S10Q2I
CONFIG_SOC_BL706C22Q2I
```

**定义位置（Location）**：[`soc/bflb/bl70x/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/bflb/bl70x/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_BFLB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_BFLB)、[`CONFIG_SOC_BL702SA0Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL702SA0Q2I)、[`CONFIG_SOC_BL702S10Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL702S10Q2I)、[`CONFIG_SOC_BL702C10Q2H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL702C10Q2H)、[`CONFIG_SOC_BL706C00Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL706C00Q2I)、[`CONFIG_SOC_BL706C10Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL706C10Q2I)、[`CONFIG_SOC_BL706S10Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL706S10Q2I)、[`CONFIG_SOC_BL706C22Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL706C22Q2I)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_BFLB`、`CONFIG_SOC_BL702SA0Q2I`、`CONFIG_SOC_BL702S10Q2I`、`CONFIG_SOC_BL702C10Q2H`、`CONFIG_SOC_BL706C00Q2I`、`CONFIG_SOC_BL706C10Q2I`、`CONFIG_SOC_BL706S10Q2I`、`CONFIG_SOC_BL706C22Q2I`。

<a id="CONFIG_SOC_SERIES_BL70XL"></a>

## 266.7 `CONFIG_SOC_SERIES_BL70XL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 BouffaloLab BL70XL 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_BFLB
```

**被选择（Selected by）**

```text
CONFIG_SOC_BL702L10Q2I
CONFIG_SOC_BL704L22Q2H
CONFIG_SOC_BL704L10Q2IW
CONFIG_SOC_BL704L20Q2IW
CONFIG_SOC_BL702LA0Q2I
```

**定义位置（Location）**：[`soc/bflb/bl70xl/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/bflb/bl70xl/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_BFLB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_BFLB)、[`CONFIG_SOC_BL702L10Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL702L10Q2I)、[`CONFIG_SOC_BL704L22Q2H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL704L22Q2H)、[`CONFIG_SOC_BL704L10Q2IW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL704L10Q2IW)、[`CONFIG_SOC_BL704L20Q2IW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL704L20Q2IW)、[`CONFIG_SOC_BL702LA0Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL702LA0Q2I)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_BFLB`、`CONFIG_SOC_BL702L10Q2I`、`CONFIG_SOC_BL704L22Q2H`、`CONFIG_SOC_BL704L10Q2IW`、`CONFIG_SOC_BL704L20Q2IW`、`CONFIG_SOC_BL702LA0Q2I`。

<a id="CONFIG_SOC_SERIES_BL808"></a>

## 266.8 `CONFIG_SOC_SERIES_BL808`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 BouffaloLab BL808 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_BFLB
```

**被选择（Selected by）**

```text
CONFIG_SOC_BL808C09Q2I
CONFIG_SOC_BL808D09Q2I
```

**定义位置（Location）**：[`soc/bflb/bl808/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/bflb/bl808/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_BFLB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_BFLB)、[`CONFIG_SOC_BL808C09Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL808C09Q2I)、[`CONFIG_SOC_BL808D09Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BL808D09Q2I)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_BFLB`、`CONFIG_SOC_BL808C09Q2I`、`CONFIG_SOC_BL808D09Q2I`。

<a id="SB_CONFIG_SOC_SERIES_BL60X"></a>

## 266.9 `SB_CONFIG_SOC_SERIES_BL60X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 BouffaloLab BL6xx 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_BFLB
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_BL602C00Q2I
SB_CONFIG_SOC_BL602C20Q2I
SB_CONFIG_SOC_BL602C20Q2IS
SB_CONFIG_SOC_BL602C40Q2IS
SB_CONFIG_SOC_BL602L10Q2H
SB_CONFIG_SOC_BL602L20Q2H
SB_CONFIG_SOC_BL604E20Q2I
```

**定义位置（Location）**：[`soc/bflb/bl60x/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/bflb/bl60x/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_BFLB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_BFLB)、[`SB_CONFIG_SOC_BL602C00Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL602C00Q2I)、[`SB_CONFIG_SOC_BL602C20Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL602C20Q2I)、[`SB_CONFIG_SOC_BL602C20Q2IS`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL602C20Q2IS)、[`SB_CONFIG_SOC_BL602C40Q2IS`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL602C40Q2IS)、[`SB_CONFIG_SOC_BL602L10Q2H`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL602L10Q2H)、[`SB_CONFIG_SOC_BL602L20Q2H`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL602L20Q2H)、[`SB_CONFIG_SOC_BL604E20Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL604E20Q2I)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_BFLB`、`SB_CONFIG_SOC_BL602C00Q2I`、`SB_CONFIG_SOC_BL602C20Q2I`、`SB_CONFIG_SOC_BL602C20Q2IS`、`SB_CONFIG_SOC_BL602C40Q2IS`、`SB_CONFIG_SOC_BL602L10Q2H`、`SB_CONFIG_SOC_BL602L20Q2H`、`SB_CONFIG_SOC_BL604E20Q2I`。

<a id="SB_CONFIG_SOC_SERIES_BL616CL"></a>

## 266.10 `SB_CONFIG_SOC_SERIES_BL616CL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 BouffaloLab BL616CL 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_BFLB
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_BL616CL3240
SB_CONFIG_SOC_BL616CL3250
SB_CONFIG_SOC_BL616CL3260
SB_CONFIG_SOC_BL616CL4845
SB_CONFIG_SOC_BL616CL4855
SB_CONFIG_SOC_BL616CL4865
SB_CONFIG_SOC_BL616CL4846
SB_CONFIG_SOC_BL616CL4856
SB_CONFIG_SOC_BL616CL4866
```

**定义位置（Location）**：[`soc/bflb/bl616cl/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/bflb/bl616cl/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_BFLB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_BFLB)、[`SB_CONFIG_SOC_BL616CL3240`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL616CL3240)、[`SB_CONFIG_SOC_BL616CL3250`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL616CL3250)、[`SB_CONFIG_SOC_BL616CL3260`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL616CL3260)、[`SB_CONFIG_SOC_BL616CL4845`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL616CL4845)、[`SB_CONFIG_SOC_BL616CL4855`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL616CL4855)、[`SB_CONFIG_SOC_BL616CL4865`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL616CL4865)、[`SB_CONFIG_SOC_BL616CL4846`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL616CL4846)、[`SB_CONFIG_SOC_BL616CL4856`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL616CL4856)、[`SB_CONFIG_SOC_BL616CL4866`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL616CL4866)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_BFLB`、`SB_CONFIG_SOC_BL616CL3240`、`SB_CONFIG_SOC_BL616CL3250`、`SB_CONFIG_SOC_BL616CL3260`、`SB_CONFIG_SOC_BL616CL4845`、`SB_CONFIG_SOC_BL616CL4855`、`SB_CONFIG_SOC_BL616CL4865`、`SB_CONFIG_SOC_BL616CL4846`、`SB_CONFIG_SOC_BL616CL4856`、`SB_CONFIG_SOC_BL616CL4866`。

<a id="SB_CONFIG_SOC_SERIES_BL61X"></a>

## 266.11 `SB_CONFIG_SOC_SERIES_BL61X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 BouffaloLab BL6xx 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_BFLB
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_BL616C50Q2I
SB_CONFIG_SOC_BL616S50Q2I
SB_CONFIG_SOC_BL618M05Q2I
SB_CONFIG_SOC_BL618M50Q2I
SB_CONFIG_SOC_BL618M65Q2I
```

**定义位置（Location）**：[`soc/bflb/bl61x/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/bflb/bl61x/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_BFLB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_BFLB)、[`SB_CONFIG_SOC_BL616C50Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL616C50Q2I)、[`SB_CONFIG_SOC_BL616S50Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL616S50Q2I)、[`SB_CONFIG_SOC_BL618M05Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL618M05Q2I)、[`SB_CONFIG_SOC_BL618M50Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL618M50Q2I)、[`SB_CONFIG_SOC_BL618M65Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL618M65Q2I)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_BFLB`、`SB_CONFIG_SOC_BL616C50Q2I`、`SB_CONFIG_SOC_BL616S50Q2I`、`SB_CONFIG_SOC_BL618M05Q2I`、`SB_CONFIG_SOC_BL618M50Q2I`、`SB_CONFIG_SOC_BL618M65Q2I`。

<a id="SB_CONFIG_SOC_SERIES_BL70X"></a>

## 266.12 `SB_CONFIG_SOC_SERIES_BL70X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 BouffaloLab BL6xx 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_BFLB
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_BL702SA0Q2I
SB_CONFIG_SOC_BL702S10Q2I
SB_CONFIG_SOC_BL702C10Q2H
SB_CONFIG_SOC_BL706C00Q2I
SB_CONFIG_SOC_BL706C10Q2I
SB_CONFIG_SOC_BL706S10Q2I
SB_CONFIG_SOC_BL706C22Q2I
```

**定义位置（Location）**：[`soc/bflb/bl70x/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/bflb/bl70x/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_BFLB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_BFLB)、[`SB_CONFIG_SOC_BL702SA0Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL702SA0Q2I)、[`SB_CONFIG_SOC_BL702S10Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL702S10Q2I)、[`SB_CONFIG_SOC_BL702C10Q2H`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL702C10Q2H)、[`SB_CONFIG_SOC_BL706C00Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL706C00Q2I)、[`SB_CONFIG_SOC_BL706C10Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL706C10Q2I)、[`SB_CONFIG_SOC_BL706S10Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL706S10Q2I)、[`SB_CONFIG_SOC_BL706C22Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL706C22Q2I)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_BFLB`、`SB_CONFIG_SOC_BL702SA0Q2I`、`SB_CONFIG_SOC_BL702S10Q2I`、`SB_CONFIG_SOC_BL702C10Q2H`、`SB_CONFIG_SOC_BL706C00Q2I`、`SB_CONFIG_SOC_BL706C10Q2I`、`SB_CONFIG_SOC_BL706S10Q2I`、`SB_CONFIG_SOC_BL706C22Q2I`。

<a id="SB_CONFIG_SOC_SERIES_BL70XL"></a>

## 266.13 `SB_CONFIG_SOC_SERIES_BL70XL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 BouffaloLab BL70XL 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_BFLB
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_BL702L10Q2I
SB_CONFIG_SOC_BL704L22Q2H
SB_CONFIG_SOC_BL704L10Q2IW
SB_CONFIG_SOC_BL704L20Q2IW
SB_CONFIG_SOC_BL702LA0Q2I
```

**定义位置（Location）**：[`soc/bflb/bl70xl/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/bflb/bl70xl/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_BFLB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_BFLB)、[`SB_CONFIG_SOC_BL702L10Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL702L10Q2I)、[`SB_CONFIG_SOC_BL704L22Q2H`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL704L22Q2H)、[`SB_CONFIG_SOC_BL704L10Q2IW`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL704L10Q2IW)、[`SB_CONFIG_SOC_BL704L20Q2IW`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL704L20Q2IW)、[`SB_CONFIG_SOC_BL702LA0Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL702LA0Q2I)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_BFLB`、`SB_CONFIG_SOC_BL702L10Q2I`、`SB_CONFIG_SOC_BL704L22Q2H`、`SB_CONFIG_SOC_BL704L10Q2IW`、`SB_CONFIG_SOC_BL704L20Q2IW`、`SB_CONFIG_SOC_BL702LA0Q2I`。

<a id="SB_CONFIG_SOC_SERIES_BL808"></a>

## 266.14 `SB_CONFIG_SOC_SERIES_BL808`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 BouffaloLab BL808 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_BFLB
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_BL808C09Q2I
SB_CONFIG_SOC_BL808D09Q2I
```

**定义位置（Location）**：[`soc/bflb/bl808/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/bflb/bl808/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_BFLB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_BFLB)、[`SB_CONFIG_SOC_BL808C09Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL808C09Q2I)、[`SB_CONFIG_SOC_BL808D09Q2I`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BL808D09Q2I)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_BFLB`、`SB_CONFIG_SOC_BL808C09Q2I`、`SB_CONFIG_SOC_BL808D09Q2I`。

<!-- kconfig-navigation -->

[上一章](P265_soc_atmel_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P267_soc_brcm_配置项参考.md)
