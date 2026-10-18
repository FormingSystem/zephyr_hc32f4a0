---
id: learning.zephyr-docs.kconfig-reference.page-314
title: "`soc/ti`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第314章\_`soc/ti`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/ti` 的 87 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_CC13X2_CC26X2_BASIC_BT"></a>

## 314.1 `CONFIG_CC13X2_CC26X2_BASIC_BT`

**提示（Prompt）**：裸机蓝牙支持（Baremetal Bluetooth support）

**说明（Help）**

为 CC13X2 和 CC26X2 系列微控制器启用蓝牙支持，使用 TI driverlib，而不使用 Zephyr 或 TI 蓝牙协议栈（Bluetooth stack）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_CC1352P && CONFIG_SOC_FAMILY_TI_SIMPLELINK
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2_cc26x2/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2_cc26x2/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_CC1352P`](P314_soc_ti_配置项参考.md#CONFIG_SOC_CC1352P)、[`CONFIG_SOC_FAMILY_TI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TI_SIMPLELINK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TI_SIMPLELINK`。

<a id="CONFIG_CC13X2_CC26X2_BOOST_MODE"></a>

## 314.2 `CONFIG_CC13X2_CC26X2_BOOST_MODE`

原库同名定义共 2 条；本项为数据库第 3622 条记录，各定义分别保留。

**提示（Prompt）**：无线电增强模式（Radio boost mode，VDDR_HH）

**说明（Help）**

启用 +14dBm 无线电增强模式（radio boost mode），将 `CCFG_FORCE_VDDR_HH` 设为 1。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_CC13X2_CC26X2 && CONFIG_SOC_FAMILY_TI_SIMPLELINK
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2_cc26x2/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2_cc26x2/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 客户配置（Customer Configuration，CCFG）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_CC13X2_CC26X2`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC13X2_CC26X2)、[`CONFIG_SOC_FAMILY_TI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TI_SIMPLELINK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TI_SIMPLELINK`。

<a id="CONFIG_CC13X2_CC26X2_BOOST_MODE--record-3623"></a>

## 314.3 `CONFIG_CC13X2_CC26X2_BOOST_MODE`

原库同名定义共 2 条；本项为数据库第 3623 条记录，各定义分别保留。

**提示（Prompt）**：无线电增强模式（Radio boost mode，VDDR_HH）

**说明（Help）**

启用 +14dBm 无线电增强模式（radio boost mode），将 `CCFG_FORCE_VDDR_HH` 设为 1。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7 && CONFIG_SOC_FAMILY_TI_SIMPLELINK
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 客户配置（Customer Configuration，CCFG）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7)、[`CONFIG_SOC_FAMILY_TI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TI_SIMPLELINK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TI_SIMPLELINK`。

<a id="CONFIG_CC13X2_CC26X2_BOOTLOADER_BACKDOOR_ENABLE"></a>

## 314.4 `CONFIG_CC13X2_CC26X2_BOOTLOADER_BACKDOOR_ENABLE`

原库同名定义共 2 条；本项为数据库第 3624 条记录，各定义分别保留。

**提示（Prompt）**：ROM 引导加载程序后门入口（ROM bootloader backdoor）

**说明（Help）**

启用 ROM 引导加载程序后门入口（bootloader backdoor）：复位时，若关联引脚处于正确逻辑电平，就启动引导加载程序。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CC13X2_CC26X2_BOOTLOADER_ENABLE && CONFIG_SOC_SERIES_CC13X2_CC26X2 && CONFIG_SOC_FAMILY_TI_SIMPLELINK
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2_cc26x2/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2_cc26x2/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 客户配置（Customer Configuration，CCFG） → ROM 引导加载程序（ROM bootloader）

**配置项引用（Symbol References）**：[`CONFIG_CC13X2_CC26X2_BOOTLOADER_ENABLE`](P314_soc_ti_配置项参考.md#CONFIG_CC13X2_CC26X2_BOOTLOADER_ENABLE)、[`CONFIG_SOC_SERIES_CC13X2_CC26X2`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC13X2_CC26X2)、[`CONFIG_SOC_FAMILY_TI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TI_SIMPLELINK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TI_SIMPLELINK`。

<a id="CONFIG_CC13X2_CC26X2_BOOTLOADER_BACKDOOR_ENABLE--record-3625"></a>

## 314.5 `CONFIG_CC13X2_CC26X2_BOOTLOADER_BACKDOOR_ENABLE`

原库同名定义共 2 条；本项为数据库第 3625 条记录，各定义分别保留。

**提示（Prompt）**：ROM 引导加载程序后门入口（ROM bootloader backdoor）

**说明（Help）**

启用 ROM 引导加载程序后门入口（bootloader backdoor）：复位时，若关联引脚处于正确逻辑电平，就启动引导加载程序。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CC13X2_CC26X2_BOOTLOADER_ENABLE && CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7 && CONFIG_SOC_FAMILY_TI_SIMPLELINK
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 客户配置（Customer Configuration，CCFG） → ROM 引导加载程序（ROM bootloader）

**配置项引用（Symbol References）**：[`CONFIG_CC13X2_CC26X2_BOOTLOADER_ENABLE`](P314_soc_ti_配置项参考.md#CONFIG_CC13X2_CC26X2_BOOTLOADER_ENABLE)、[`CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7)、[`CONFIG_SOC_FAMILY_TI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TI_SIMPLELINK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TI_SIMPLELINK`。

<a id="CONFIG_CC13X2_CC26X2_BOOTLOADER_BACKDOOR_LEVEL"></a>

## 314.6 `CONFIG_CC13X2_CC26X2_BOOTLOADER_BACKDOOR_LEVEL`

原库同名定义共 2 条；本项为数据库第 3626 条记录，各定义分别保留。

**提示（Prompt）**：ROM 引导加载程序后门入口电平（backdoor level）

**说明（Help）**

设置引导加载程序后门入口所选引脚的有效电平（active level）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CC13X2_CC26X2_BOOTLOADER_BACKDOOR_ENABLE && CONFIG_SOC_SERIES_CC13X2_CC26X2 && CONFIG_SOC_FAMILY_TI_SIMPLELINK
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 1]
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2_cc26x2/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2_cc26x2/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 客户配置（Customer Configuration，CCFG） → ROM 引导加载程序（ROM bootloader） → ROM 引导加载程序后门入口（ROM bootloader backdoor）

**配置项引用（Symbol References）**：[`CONFIG_CC13X2_CC26X2_BOOTLOADER_BACKDOOR_ENABLE`](P314_soc_ti_配置项参考.md#CONFIG_CC13X2_CC26X2_BOOTLOADER_BACKDOOR_ENABLE)、[`CONFIG_SOC_SERIES_CC13X2_CC26X2`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC13X2_CC26X2)、[`CONFIG_SOC_FAMILY_TI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TI_SIMPLELINK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TI_SIMPLELINK`。

<a id="CONFIG_CC13X2_CC26X2_BOOTLOADER_BACKDOOR_LEVEL--record-3627"></a>

## 314.7 `CONFIG_CC13X2_CC26X2_BOOTLOADER_BACKDOOR_LEVEL`

原库同名定义共 2 条；本项为数据库第 3627 条记录，各定义分别保留。

**提示（Prompt）**：ROM 引导加载程序后门入口电平（backdoor level）

**说明（Help）**

设置引导加载程序后门入口所选引脚的有效电平（active level）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CC13X2_CC26X2_BOOTLOADER_BACKDOOR_ENABLE && CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7 && CONFIG_SOC_FAMILY_TI_SIMPLELINK
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 1]
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 客户配置（Customer Configuration，CCFG） → ROM 引导加载程序（ROM bootloader） → ROM 引导加载程序后门入口（ROM bootloader backdoor）

**配置项引用（Symbol References）**：[`CONFIG_CC13X2_CC26X2_BOOTLOADER_BACKDOOR_ENABLE`](P314_soc_ti_配置项参考.md#CONFIG_CC13X2_CC26X2_BOOTLOADER_BACKDOOR_ENABLE)、[`CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7)、[`CONFIG_SOC_FAMILY_TI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TI_SIMPLELINK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TI_SIMPLELINK`。

<a id="CONFIG_CC13X2_CC26X2_BOOTLOADER_BACKDOOR_PIN"></a>

## 314.8 `CONFIG_CC13X2_CC26X2_BOOTLOADER_BACKDOOR_PIN`

原库同名定义共 2 条；本项为数据库第 3628 条记录，各定义分别保留。

**提示（Prompt）**：ROM 引导加载程序后门入口引脚（backdoor pin）

**说明（Help）**

设置启用引导加载程序后门入口时，要检查电平的引脚。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CC13X2_CC26X2_BOOTLOADER_BACKDOOR_ENABLE && CONFIG_SOC_SERIES_CC13X2_CC26X2 && CONFIG_SOC_FAMILY_TI_SIMPLELINK
```

**默认值（Defaults）**

```text
255
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2_cc26x2/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2_cc26x2/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 客户配置（Customer Configuration，CCFG） → ROM 引导加载程序（ROM bootloader） → ROM 引导加载程序后门入口（ROM bootloader backdoor）

**配置项引用（Symbol References）**：[`CONFIG_CC13X2_CC26X2_BOOTLOADER_BACKDOOR_ENABLE`](P314_soc_ti_配置项参考.md#CONFIG_CC13X2_CC26X2_BOOTLOADER_BACKDOOR_ENABLE)、[`CONFIG_SOC_SERIES_CC13X2_CC26X2`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC13X2_CC26X2)、[`CONFIG_SOC_FAMILY_TI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TI_SIMPLELINK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TI_SIMPLELINK`。

<a id="CONFIG_CC13X2_CC26X2_BOOTLOADER_BACKDOOR_PIN--record-3629"></a>

## 314.9 `CONFIG_CC13X2_CC26X2_BOOTLOADER_BACKDOOR_PIN`

原库同名定义共 2 条；本项为数据库第 3629 条记录，各定义分别保留。

**提示（Prompt）**：ROM 引导加载程序后门入口引脚（backdoor pin）

**说明（Help）**

设置启用引导加载程序后门入口时，要检查电平的引脚。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CC13X2_CC26X2_BOOTLOADER_BACKDOOR_ENABLE && CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7 && CONFIG_SOC_FAMILY_TI_SIMPLELINK
```

**默认值（Defaults）**

```text
255
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 客户配置（Customer Configuration，CCFG） → ROM 引导加载程序（ROM bootloader） → ROM 引导加载程序后门入口（ROM bootloader backdoor）

**配置项引用（Symbol References）**：[`CONFIG_CC13X2_CC26X2_BOOTLOADER_BACKDOOR_ENABLE`](P314_soc_ti_配置项参考.md#CONFIG_CC13X2_CC26X2_BOOTLOADER_BACKDOOR_ENABLE)、[`CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7)、[`CONFIG_SOC_FAMILY_TI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TI_SIMPLELINK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TI_SIMPLELINK`。

<a id="CONFIG_CC13X2_CC26X2_BOOTLOADER_ENABLE"></a>

## 314.10 `CONFIG_CC13X2_CC26X2_BOOTLOADER_ENABLE`

原库同名定义共 2 条；本项为数据库第 3630 条记录，各定义分别保留。

**提示（Prompt）**：ROM 引导加载程序（ROM bootloader）

**说明（Help）**

启用 CC13xx／CC26xx 器件 ROM 中的串行引导加载程序（serial bootloader）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_CC13X2_CC26X2 && CONFIG_SOC_FAMILY_TI_SIMPLELINK
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2_cc26x2/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2_cc26x2/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 客户配置（Customer Configuration，CCFG）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_CC13X2_CC26X2`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC13X2_CC26X2)、[`CONFIG_SOC_FAMILY_TI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TI_SIMPLELINK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TI_SIMPLELINK`。

<a id="CONFIG_CC13X2_CC26X2_BOOTLOADER_ENABLE--record-3631"></a>

## 314.11 `CONFIG_CC13X2_CC26X2_BOOTLOADER_ENABLE`

原库同名定义共 2 条；本项为数据库第 3631 条记录，各定义分别保留。

**提示（Prompt）**：ROM 引导加载程序（ROM bootloader）

**说明（Help）**

启用 CC13xx／CC26xx 器件 ROM 中的串行引导加载程序（serial bootloader）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7 && CONFIG_SOC_FAMILY_TI_SIMPLELINK
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 客户配置（Customer Configuration，CCFG）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7)、[`CONFIG_SOC_FAMILY_TI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TI_SIMPLELINK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TI_SIMPLELINK`。

<a id="CONFIG_CC13X2_CC26X2_HAS_CUSTOM_RF_HWATTRS"></a>

## 314.12 `CONFIG_CC13X2_CC26X2_HAS_CUSTOM_RF_HWATTRS`

原库同名定义共 2 条；本项为数据库第 3632 条记录，各定义分别保留。

**提示（Prompt）**：开发板定义自有 RFCC26XX 硬件属性结构体（hwAttrs structure）

**说明（Help）**

开发板定义自己的 `RFCC26XX_hwAttrs` 结构体，例如用于自定义天线切换回调（antenna switching callback）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_CC13X2_CC26X2 && CONFIG_SOC_FAMILY_TI_SIMPLELINK
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2_cc26x2/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2_cc26x2/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 客户配置（Customer Configuration，CCFG）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_CC13X2_CC26X2`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC13X2_CC26X2)、[`CONFIG_SOC_FAMILY_TI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TI_SIMPLELINK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TI_SIMPLELINK`。

<a id="CONFIG_CC13X2_CC26X2_HAS_CUSTOM_RF_HWATTRS--record-3633"></a>

## 314.13 `CONFIG_CC13X2_CC26X2_HAS_CUSTOM_RF_HWATTRS`

原库同名定义共 2 条；本项为数据库第 3633 条记录，各定义分别保留。

**提示（Prompt）**：开发板定义自有 RFCC26XX 硬件属性结构体（hwAttrs structure）

**说明（Help）**

开发板定义自己的 `RFCC26XX_hwAttrs` 结构体，例如用于自定义天线切换回调（antenna switching callback）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7 && CONFIG_SOC_FAMILY_TI_SIMPLELINK
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 客户配置（Customer Configuration，CCFG）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7)、[`CONFIG_SOC_FAMILY_TI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TI_SIMPLELINK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TI_SIMPLELINK`。

<a id="CONFIG_CC13X2_CC26X2_XOSC_CAPARRAY_DELTA"></a>

## 314.14 `CONFIG_CC13X2_CC26X2_XOSC_CAPARRAY_DELTA`

**提示（Prompt）**：电容阵列调谐增量（Cap array tuning delta）

**说明（Help）**

启用特定的电容阵列调谐增量（cap array tuning delta）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7 && CONFIG_SOC_FAMILY_TI_SIMPLELINK
```

**默认值（Defaults）**

```text
0xD5
```

**取值范围（Ranges）**

```text
[0, 0xFF]
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 客户配置（Customer Configuration，CCFG）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7)、[`CONFIG_SOC_FAMILY_TI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TI_SIMPLELINK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TI_SIMPLELINK`。

<a id="CONFIG_CC23X0_BLDR_ENABLED"></a>

## 314.15 `CONFIG_CC23X0_BLDR_ENABLED`

**提示（Prompt）**：引导加载程序命令（Bootloader commands）

**说明（Help）**

设为 `n` 时，引导加载程序（bootloader）忽略所有命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_CC23X0 && CONFIG_SOC_FAMILY_TI_SIMPLELINK
```

**定义位置（Location）**：[`soc/ti/simplelink/cc23x0/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc23x0/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 引导加载程序配置（Bootloader Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_CC23X0`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC23X0)、[`CONFIG_SOC_FAMILY_TI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TI_SIMPLELINK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TI_SIMPLELINK`。

<a id="CONFIG_CC23X0_BLDR_VTOR_TYPE"></a>

## 314.16 `CONFIG_CC23X0_BLDR_VTOR_TYPE`

**提示（Prompt）**：用户引导加载程序向量表指针（bootloader vector table pointer）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_CC23X0 && CONFIG_SOC_FAMILY_TI_SIMPLELINK
```

**默认值（Defaults）**

```text
CONFIG_CC23X0_BLDR_VTOR_TYPE_UNDEF
```

**可选项（Choices）**

```text
CONFIG_CC23X0_BLDR_VTOR_TYPE_UNDEF
CONFIG_CC23X0_BLDR_VTOR_TYPE_FORBID
CONFIG_CC23X0_BLDR_VTOR_TYPE_USE_FCFG
CONFIG_CC23X0_BLDR_VTOR_TYPE_FLASH
```

**定义位置（Location）**：[`soc/ti/simplelink/cc23x0/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc23x0/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 引导加载程序配置（Bootloader Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_CC23X0`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC23X0)、[`CONFIG_SOC_FAMILY_TI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TI_SIMPLELINK)、[`CONFIG_CC23X0_BLDR_VTOR_TYPE_UNDEF`](P314_soc_ti_配置项参考.md#CONFIG_CC23X0_BLDR_VTOR_TYPE_UNDEF)、[`CONFIG_CC23X0_BLDR_VTOR_TYPE_FORBID`](P314_soc_ti_配置项参考.md#CONFIG_CC23X0_BLDR_VTOR_TYPE_FORBID)、[`CONFIG_CC23X0_BLDR_VTOR_TYPE_USE_FCFG`](P314_soc_ti_配置项参考.md#CONFIG_CC23X0_BLDR_VTOR_TYPE_USE_FCFG)、[`CONFIG_CC23X0_BLDR_VTOR_TYPE_FLASH`](P314_soc_ti_配置项参考.md#CONFIG_CC23X0_BLDR_VTOR_TYPE_FLASH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TI_SIMPLELINK`。

<a id="CONFIG_CC23X0_BLDR_VTOR_TYPE_FLASH"></a>

## 314.17 `CONFIG_CC23X0_BLDR_VTOR_TYPE_FLASH`

**提示（Prompt）**：使用有效的主 Flash 地址（valid main flash address）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CC23X0_BLDR_VTOR_TYPE>
```

**定义位置（Location）**：[`soc/ti/simplelink/cc23x0/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc23x0/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 引导加载程序配置（Bootloader Configuration） → 用户引导加载程序向量表指针（bootloader vector table pointer）

**配置项引用（Symbol References）**：[`CONFIG_CC23X0_BLDR_VTOR_TYPE`](P314_soc_ti_配置项参考.md#CONFIG_CC23X0_BLDR_VTOR_TYPE)。

<a id="CONFIG_CC23X0_BLDR_VTOR_TYPE_FORBID"></a>

## 314.18 `CONFIG_CC23X0_BLDR_VTOR_TYPE_FORBID`

**提示（Prompt）**：不调用引导加载程序（No bootloader invoked）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CC23X0_BLDR_VTOR_TYPE>
```

**定义位置（Location）**：[`soc/ti/simplelink/cc23x0/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc23x0/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 引导加载程序配置（Bootloader Configuration） → 用户引导加载程序向量表指针（bootloader vector table pointer）

**配置项引用（Symbol References）**：[`CONFIG_CC23X0_BLDR_VTOR_TYPE`](P314_soc_ti_配置项参考.md#CONFIG_CC23X0_BLDR_VTOR_TYPE)。

<a id="CONFIG_CC23X0_BLDR_VTOR_TYPE_UNDEF"></a>

## 314.19 `CONFIG_CC23X0_BLDR_VTOR_TYPE_UNDEF`

**提示（Prompt）**：ROM 串行引导加载程序（ROM serial bootloader）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CC23X0_BLDR_VTOR_TYPE>
```

**定义位置（Location）**：[`soc/ti/simplelink/cc23x0/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc23x0/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 引导加载程序配置（Bootloader Configuration） → 用户引导加载程序向量表指针（bootloader vector table pointer）

**配置项引用（Symbol References）**：[`CONFIG_CC23X0_BLDR_VTOR_TYPE`](P314_soc_ti_配置项参考.md#CONFIG_CC23X0_BLDR_VTOR_TYPE)。

<a id="CONFIG_CC23X0_BLDR_VTOR_TYPE_USE_FCFG"></a>

## 314.20 `CONFIG_CC23X0_BLDR_VTOR_TYPE_USE_FCFG`

**提示（Prompt）**：使用工厂配置（Use factory configuration）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CC23X0_BLDR_VTOR_TYPE>
```

**定义位置（Location）**：[`soc/ti/simplelink/cc23x0/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc23x0/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 引导加载程序配置（Bootloader Configuration） → 用户引导加载程序向量表指针（bootloader vector table pointer）

**配置项引用（Symbol References）**：[`CONFIG_CC23X0_BLDR_VTOR_TYPE`](P314_soc_ti_配置项参考.md#CONFIG_CC23X0_BLDR_VTOR_TYPE)。

<a id="CONFIG_CC3220SF_DEBUG"></a>

## 314.21 `CONFIG_CC3220SF_DEBUG`

**提示（Prompt）**：前置调试头部，并禁用 Flash 验证（Prepend debug header）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_CC3220SF && CONFIG_SOC_FAMILY_TI_SIMPLELINK
```

**默认值（Defaults）**

```text
CONFIG_XIP
```

**定义位置（Location）**：[`soc/ti/simplelink/cc32xx/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc32xx/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_CC3220SF`](P314_soc_ti_配置项参考.md#CONFIG_SOC_CC3220SF)、[`CONFIG_SOC_FAMILY_TI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TI_SIMPLELINK)、[`CONFIG_XIP`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XIP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TI_SIMPLELINK`。

<a id="CONFIG_CC3235SF_DEBUG"></a>

## 314.22 `CONFIG_CC3235SF_DEBUG`

**提示（Prompt）**：前置调试头部，并禁用 Flash 验证（Prepend debug header）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_CC3235SF && CONFIG_SOC_FAMILY_TI_SIMPLELINK
```

**默认值（Defaults）**

```text
CONFIG_XIP
```

**定义位置（Location）**：[`soc/ti/simplelink/cc32xx/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc32xx/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_CC3235SF`](P314_soc_ti_配置项参考.md#CONFIG_SOC_CC3235SF)、[`CONFIG_SOC_FAMILY_TI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TI_SIMPLELINK)、[`CONFIG_XIP`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XIP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TI_SIMPLELINK`。

<a id="CONFIG_HAS_TI_CCFG"></a>

## 314.23 `CONFIG_HAS_TI_CCFG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

客户配置寄存器（Customer Configuration，CCFG）位于 Flash 末尾时选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_TI_SIMPLELINK
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_CC13X2_CC26X2
CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7
CONFIG_SOC_SERIES_CC23X0
```

**定义位置（Location）**：[`soc/ti/simplelink/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_TI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TI_SIMPLELINK)、[`CONFIG_SOC_SERIES_CC13X2_CC26X2`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC13X2_CC26X2)、[`CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7)、[`CONFIG_SOC_SERIES_CC23X0`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC23X0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TI_SIMPLELINK`。

<a id="CONFIG_SOC_CC1312R"></a>

## 314.24 `CONFIG_SOC_CC1312R`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CC1312R 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_CC13X2_CC26X2
```

**被选择（Selected by）**

```text
CONFIG_BOARD_CC1312R1_LAUNCHXL
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2_cc26x2/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2_cc26x2/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_CC13X2_CC26X2`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC13X2_CC26X2)、[`CONFIG_BOARD_CC1312R1_LAUNCHXL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_CC1312R1_LAUNCHXL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_CC1312R1_LAUNCHXL`。

<a id="CONFIG_SOC_CC1352P"></a>

## 314.25 `CONFIG_SOC_CC1352P`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CC1352P 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_CC13X2_CC26X2
```

**被选择（Selected by）**

```text
CONFIG_BOARD_CC1352P1_LAUNCHXL
CONFIG_BOARD_BEAGLECONNECT_FREEDOM
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2_cc26x2/Kconfig.soc:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2_cc26x2/Kconfig.soc#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_CC13X2_CC26X2`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC13X2_CC26X2)、[`CONFIG_BOARD_CC1352P1_LAUNCHXL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_CC1352P1_LAUNCHXL)、[`CONFIG_BOARD_BEAGLECONNECT_FREEDOM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_BEAGLECONNECT_FREEDOM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_CC1352P1_LAUNCHXL`、`CONFIG_BOARD_BEAGLECONNECT_FREEDOM`。

<a id="CONFIG_SOC_CC1352P7"></a>

## 314.26 `CONFIG_SOC_CC1352P7`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CC1352P7 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7
```

**被选择（Selected by）**

```text
CONFIG_BOARD_CC1352P7_LP
CONFIG_BOARD_BEAGLEPLAY
CONFIG_BOARD_BEAGLECONNECT_FREEDOM
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7)、[`CONFIG_BOARD_CC1352P7_LP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_CC1352P7_LP)、[`CONFIG_BOARD_BEAGLEPLAY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_BEAGLEPLAY)、[`CONFIG_BOARD_BEAGLECONNECT_FREEDOM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_BEAGLECONNECT_FREEDOM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_CC1352P7_LP`、`CONFIG_BOARD_BEAGLEPLAY`、`CONFIG_BOARD_BEAGLECONNECT_FREEDOM`。

<a id="CONFIG_SOC_CC1352R"></a>

## 314.27 `CONFIG_SOC_CC1352R`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CC1352R 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_CC13X2_CC26X2
```

**被选择（Selected by）**

```text
CONFIG_BOARD_CC1352R1_LAUNCHXL
CONFIG_BOARD_CC1352R_SENSORTAG
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2_cc26x2/Kconfig.soc:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2_cc26x2/Kconfig.soc#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_CC13X2_CC26X2`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC13X2_CC26X2)、[`CONFIG_BOARD_CC1352R1_LAUNCHXL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_CC1352R1_LAUNCHXL)、[`CONFIG_BOARD_CC1352R_SENSORTAG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_CC1352R_SENSORTAG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_CC1352R1_LAUNCHXL`、`CONFIG_BOARD_CC1352R_SENSORTAG`。

<a id="CONFIG_SOC_CC1352R7"></a>

## 314.28 `CONFIG_SOC_CC1352R7`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CC1352R7 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig.soc:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig.soc#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7)。

<a id="CONFIG_SOC_CC2340R5"></a>

## 314.29 `CONFIG_SOC_CC2340R5`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CC2340R5 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_CC23X0
```

**被选择（Selected by）**

```text
CONFIG_BOARD_LP_EM_CC2340R5
```

**定义位置（Location）**：[`soc/ti/simplelink/cc23x0/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc23x0/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_CC23X0`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC23X0)、[`CONFIG_BOARD_LP_EM_CC2340R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_LP_EM_CC2340R5)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_LP_EM_CC2340R5`。

<a id="CONFIG_SOC_CC2652P"></a>

## 314.30 `CONFIG_SOC_CC2652P`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CC2652P 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_CC13X2_CC26X2
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2_cc26x2/Kconfig.soc:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2_cc26x2/Kconfig.soc#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_CC13X2_CC26X2`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC13X2_CC26X2)。

<a id="CONFIG_SOC_CC2652P7"></a>

## 314.31 `CONFIG_SOC_CC2652P7`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CC2652P7 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig.soc:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig.soc#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7)。

<a id="CONFIG_SOC_CC2652R"></a>

## 314.32 `CONFIG_SOC_CC2652R`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CC2652R 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_CC13X2_CC26X2
```

**被选择（Selected by）**

```text
CONFIG_BOARD_CC26X2R1_LAUNCHXL
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2_cc26x2/Kconfig.soc:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2_cc26x2/Kconfig.soc#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_CC13X2_CC26X2`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC13X2_CC26X2)、[`CONFIG_BOARD_CC26X2R1_LAUNCHXL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_CC26X2R1_LAUNCHXL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_CC26X2R1_LAUNCHXL`。

<a id="CONFIG_SOC_CC2652R7"></a>

## 314.33 `CONFIG_SOC_CC2652R7`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CC2652R7 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig.soc:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig.soc#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7)。

<a id="CONFIG_SOC_CC3220SF"></a>

## 314.34 `CONFIG_SOC_CC3220SF`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CC3220SF 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_CC32XX
```

**被选择（Selected by）**

```text
CONFIG_BOARD_CC3220SF_LAUNCHXL
```

**定义位置（Location）**：[`soc/ti/simplelink/cc32xx/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc32xx/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_CC32XX`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC32XX)、[`CONFIG_BOARD_CC3220SF_LAUNCHXL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_CC3220SF_LAUNCHXL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_CC3220SF_LAUNCHXL`。

<a id="CONFIG_SOC_CC3235SF"></a>

## 314.35 `CONFIG_SOC_CC3235SF`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CC3235SF 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_CC32XX
```

**被选择（Selected by）**

```text
CONFIG_BOARD_CC3235SF_LAUNCHXL
```

**定义位置（Location）**：[`soc/ti/simplelink/cc32xx/Kconfig.soc:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc32xx/Kconfig.soc#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_CC32XX`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC32XX)、[`CONFIG_BOARD_CC3235SF_LAUNCHXL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_CC3235SF_LAUNCHXL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_CC3235SF_LAUNCHXL`。

<a id="CONFIG_SOC_FAMILY_TI_K3_BOOT_SPRINGBOARD"></a>

## 314.36 `CONFIG_SOC_FAMILY_TI_K3_BOOT_SPRINGBOARD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果 Zephyr 代码区域位于 DRAM 中，而该区域默认受内存保护单元（MPU）保护、不可执行，则此选项在 A 类紧耦合内存（ATCM）中启用启动跳板（boot springboard），先设置执行权限，再跳转到 DRAM 代码区域。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_AM64X_R5 || CONFIG_SOC_SERIES_J721E_R5 || CONFIG_SOC_SERIES_J722S_R5) && CONFIG_SOC_FAMILY_TI_K3
```

**默认值（Defaults）**

```text
0x0 >= 0x80000000
```

**定义位置（Location）**：[`soc/ti/k3/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/k3/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_AM64X_R5`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_AM64X_R5)、[`CONFIG_SOC_SERIES_J721E_R5`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_J721E_R5)、[`CONFIG_SOC_SERIES_J722S_R5`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_J722S_R5)、[`CONFIG_SOC_FAMILY_TI_K3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TI_K3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TI_K3`。

<a id="CONFIG_SOC_MSP432P401R"></a>

## 314.37 `CONFIG_SOC_MSP432P401R`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

MSP432P401R 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_MSP432P4XX
```

**被选择（Selected by）**

```text
CONFIG_BOARD_MSP_EXP432P401R_LAUNCHXL
```

**定义位置（Location）**：[`soc/ti/simplelink/msp432p4xx/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/msp432p4xx/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_MSP432P4XX`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_MSP432P4XX)、[`CONFIG_BOARD_MSP_EXP432P401R_LAUNCHXL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MSP_EXP432P401R_LAUNCHXL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_MSP_EXP432P401R_LAUNCHXL`。

<a id="CONFIG_SOC_SERIES_AM13E"></a>

## 314.38 `CONFIG_SOC_SERIES_AM13E`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 TI AM13E 系列片上系统（SoCs）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_TI_AM13
```

**被选择（Selected by）**

```text
CONFIG_SOC_AM13E23019
```

**定义位置（Location）**：[`soc/ti/am13/am13e/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/am13/am13e/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_TI_AM13`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TI_AM13)、[`CONFIG_SOC_AM13E23019`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AM13E23019)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TI_AM13`、`CONFIG_SOC_AM13E23019`。

<a id="CONFIG_SOC_SERIES_AM62LX_A53"></a>

## 314.39 `CONFIG_SOC_SERIES_AM62LX_A53`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 AM62LX A53 系列支持（Series support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_AM62LX
```

**被选择（Selected by）**

```text
CONFIG_SOC_AM62L3_A53
```

**定义位置（Location）**：[`soc/ti/k3/am62lx/Kconfig.soc:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/k3/am62lx/Kconfig.soc#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_AM62LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM62LX)、[`CONFIG_SOC_AM62L3_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AM62L3_A53)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_AM62LX`、`CONFIG_SOC_AM62L3_A53`。

<a id="CONFIG_SOC_SERIES_AM62X_A53"></a>

## 314.40 `CONFIG_SOC_SERIES_AM62X_A53`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 AM62X A53 系列支持（Series support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_AM62X
```

**被选择（Selected by）**

```text
CONFIG_SOC_AM6234_A53
CONFIG_SOC_AM6254_A53
CONFIG_SOC_AM6232_A53
```

**定义位置（Location）**：[`soc/ti/k3/am62x/Kconfig.soc:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/k3/am62x/Kconfig.soc#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_AM62X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM62X)、[`CONFIG_SOC_AM6234_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AM6234_A53)、[`CONFIG_SOC_AM6254_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AM6254_A53)、[`CONFIG_SOC_AM6232_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AM6232_A53)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_AM62X`、`CONFIG_SOC_AM6234_A53`、`CONFIG_SOC_AM6254_A53`、`CONFIG_SOC_AM6232_A53`。

<a id="CONFIG_SOC_SERIES_AM62X_M4"></a>

## 314.41 `CONFIG_SOC_SERIES_AM62X_M4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 AM62X M4 系列支持（Series support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_AM62X
```

**被选择（Selected by）**

```text
CONFIG_SOC_AM6234_M4
CONFIG_SOC_AM6254_M4
CONFIG_SOC_AM6232_M4
```

**定义位置（Location）**：[`soc/ti/k3/am62x/Kconfig.soc:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/k3/am62x/Kconfig.soc#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_AM62X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM62X)、[`CONFIG_SOC_AM6234_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AM6234_M4)、[`CONFIG_SOC_AM6254_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AM6254_M4)、[`CONFIG_SOC_AM6232_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AM6232_M4)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_AM62X`、`CONFIG_SOC_AM6234_M4`、`CONFIG_SOC_AM6254_M4`、`CONFIG_SOC_AM6232_M4`。

<a id="CONFIG_SOC_SERIES_AM64X_M4"></a>

## 314.42 `CONFIG_SOC_SERIES_AM64X_M4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 AM64X M4 系列支持（Series support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_AM64X
```

**被选择（Selected by）**

```text
CONFIG_SOC_AM6442_M4
CONFIG_SOC_AM2434_M4
```

**定义位置（Location）**：[`soc/ti/k3/am64x/Kconfig.soc:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/k3/am64x/Kconfig.soc#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_AM64X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM64X)、[`CONFIG_SOC_AM6442_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AM6442_M4)、[`CONFIG_SOC_AM2434_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AM2434_M4)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_AM64X`、`CONFIG_SOC_AM6442_M4`、`CONFIG_SOC_AM2434_M4`。

<a id="CONFIG_SOC_SERIES_AM64X_R5"></a>

## 314.43 `CONFIG_SOC_SERIES_AM64X_R5`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 AM64X R5 系列支持（Series support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_AM64X
```

**被选择（Selected by）**

```text
CONFIG_SOC_AM2434_R5F0_0
CONFIG_SOC_AM6442_R5F0_0
CONFIG_SOC_AM6442_R5F0_1
CONFIG_SOC_AM6442_R5F1_0
CONFIG_SOC_AM6442_R5F1_1
```

**定义位置（Location）**：[`soc/ti/k3/am64x/Kconfig.soc:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/k3/am64x/Kconfig.soc#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_AM64X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM64X)、[`CONFIG_SOC_AM2434_R5F0_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AM2434_R5F0_0)、[`CONFIG_SOC_AM6442_R5F0_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AM6442_R5F0_0)、[`CONFIG_SOC_AM6442_R5F0_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AM6442_R5F0_1)、[`CONFIG_SOC_AM6442_R5F1_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AM6442_R5F1_0)、[`CONFIG_SOC_AM6442_R5F1_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AM6442_R5F1_1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_AM64X`、`CONFIG_SOC_AM2434_R5F0_0`、`CONFIG_SOC_AM6442_R5F0_0`、`CONFIG_SOC_AM6442_R5F0_1`、`CONFIG_SOC_AM6442_R5F1_0`、`CONFIG_SOC_AM6442_R5F1_1`。

<a id="CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7"></a>

## 314.44 `CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 TI SimpleLink CC13x2x7／CC26x2x7 片上系统（SoCs）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_TI_SIMPLELINK
```

**被选择（Selected by）**

```text
CONFIG_SOC_CC1352P7
CONFIG_SOC_CC1352R7
CONFIG_SOC_CC2652P7
CONFIG_SOC_CC2652R7
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_TI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TI_SIMPLELINK)、[`CONFIG_SOC_CC1352P7`](P314_soc_ti_配置项参考.md#CONFIG_SOC_CC1352P7)、[`CONFIG_SOC_CC1352R7`](P314_soc_ti_配置项参考.md#CONFIG_SOC_CC1352R7)、[`CONFIG_SOC_CC2652P7`](P314_soc_ti_配置项参考.md#CONFIG_SOC_CC2652P7)、[`CONFIG_SOC_CC2652R7`](P314_soc_ti_配置项参考.md#CONFIG_SOC_CC2652R7)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TI_SIMPLELINK`。

<a id="CONFIG_SOC_SERIES_CC13X2_CC26X2"></a>

## 314.45 `CONFIG_SOC_SERIES_CC13X2_CC26X2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 TI SimpleLink CC13x2／CC26x2 片上系统（SoCs）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_TI_SIMPLELINK
```

**被选择（Selected by）**

```text
CONFIG_SOC_CC1312R
CONFIG_SOC_CC1352P
CONFIG_SOC_CC1352R
CONFIG_SOC_CC2652P
CONFIG_SOC_CC2652R
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2_cc26x2/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2_cc26x2/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_TI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TI_SIMPLELINK)、[`CONFIG_SOC_CC1312R`](P314_soc_ti_配置项参考.md#CONFIG_SOC_CC1312R)、[`CONFIG_SOC_CC1352P`](P314_soc_ti_配置项参考.md#CONFIG_SOC_CC1352P)、[`CONFIG_SOC_CC1352R`](P314_soc_ti_配置项参考.md#CONFIG_SOC_CC1352R)、[`CONFIG_SOC_CC2652P`](P314_soc_ti_配置项参考.md#CONFIG_SOC_CC2652P)、[`CONFIG_SOC_CC2652R`](P314_soc_ti_配置项参考.md#CONFIG_SOC_CC2652R)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TI_SIMPLELINK`。

<a id="CONFIG_SOC_SERIES_CC23X0"></a>

## 314.46 `CONFIG_SOC_SERIES_CC23X0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 TI SimpleLink CC23X0 系列片上系统（SoCs）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_TI_SIMPLELINK
```

**被选择（Selected by）**

```text
CONFIG_SOC_CC2340R5
```

**定义位置（Location）**：[`soc/ti/simplelink/cc23x0/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc23x0/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_TI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TI_SIMPLELINK)、[`CONFIG_SOC_CC2340R5`](P314_soc_ti_配置项参考.md#CONFIG_SOC_CC2340R5)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TI_SIMPLELINK`。

<a id="CONFIG_SOC_SERIES_CC32XX"></a>

## 314.47 `CONFIG_SOC_SERIES_CC32XX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 TI SimpleLink CC32xx 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_TI_SIMPLELINK
```

**被选择（Selected by）**

```text
CONFIG_SOC_CC3220SF
CONFIG_SOC_CC3235SF
```

**定义位置（Location）**：[`soc/ti/simplelink/cc32xx/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc32xx/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_TI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TI_SIMPLELINK)、[`CONFIG_SOC_CC3220SF`](P314_soc_ti_配置项参考.md#CONFIG_SOC_CC3220SF)、[`CONFIG_SOC_CC3235SF`](P314_soc_ti_配置项参考.md#CONFIG_SOC_CC3235SF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TI_SIMPLELINK`。

<a id="CONFIG_SOC_SERIES_J721E_R5"></a>

## 314.48 `CONFIG_SOC_SERIES_J721E_R5`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 J721E R5 系列支持（Series support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_J721E
```

**被选择（Selected by）**

```text
CONFIG_SOC_J721E_MAIN_R5F0_0
CONFIG_SOC_J721E_MAIN_R5F0_1
CONFIG_SOC_J721E_MAIN_R5F1_0
CONFIG_SOC_J721E_MAIN_R5F1_1
CONFIG_SOC_J721E_MCU_R5F0_0
CONFIG_SOC_J721E_MCU_R5F0_1
```

**定义位置（Location）**：[`soc/ti/k3/j721e/Kconfig.soc:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/k3/j721e/Kconfig.soc#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_J721E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_J721E)、[`CONFIG_SOC_J721E_MAIN_R5F0_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_J721E_MAIN_R5F0_0)、[`CONFIG_SOC_J721E_MAIN_R5F0_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_J721E_MAIN_R5F0_1)、[`CONFIG_SOC_J721E_MAIN_R5F1_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_J721E_MAIN_R5F1_0)、[`CONFIG_SOC_J721E_MAIN_R5F1_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_J721E_MAIN_R5F1_1)、[`CONFIG_SOC_J721E_MCU_R5F0_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_J721E_MCU_R5F0_0)、[`CONFIG_SOC_J721E_MCU_R5F0_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_J721E_MCU_R5F0_1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_J721E`、`CONFIG_SOC_J721E_MAIN_R5F0_0`、`CONFIG_SOC_J721E_MAIN_R5F0_1`、`CONFIG_SOC_J721E_MAIN_R5F1_0`、`CONFIG_SOC_J721E_MAIN_R5F1_1`、`CONFIG_SOC_J721E_MCU_R5F0_0`、`CONFIG_SOC_J721E_MCU_R5F0_1`。

<a id="CONFIG_SOC_SERIES_J722S_R5"></a>

## 314.49 `CONFIG_SOC_SERIES_J722S_R5`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 J722S R5 系列支持（Series support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_J722S
```

**被选择（Selected by）**

```text
CONFIG_SOC_J722S_MAIN_R5F0_0
CONFIG_SOC_J722S_MCU_R5F0_0
```

**定义位置（Location）**：[`soc/ti/k3/j722s/Kconfig.soc:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/k3/j722s/Kconfig.soc#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_J722S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_J722S)、[`CONFIG_SOC_J722S_MAIN_R5F0_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_J722S_MAIN_R5F0_0)、[`CONFIG_SOC_J722S_MCU_R5F0_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_J722S_MCU_R5F0_0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_J722S`、`CONFIG_SOC_J722S_MAIN_R5F0_0`、`CONFIG_SOC_J722S_MCU_R5F0_0`。

<a id="CONFIG_SOC_SERIES_MSP432P4XX"></a>

## 314.50 `CONFIG_SOC_SERIES_MSP432P4XX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 TI SimpleLink MSP432P4XX 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_TI_SIMPLELINK
```

**被选择（Selected by）**

```text
CONFIG_SOC_MSP432P401R
```

**定义位置（Location）**：[`soc/ti/simplelink/msp432p4xx/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/msp432p4xx/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_TI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TI_SIMPLELINK)、[`CONFIG_SOC_MSP432P401R`](P314_soc_ti_配置项参考.md#CONFIG_SOC_MSP432P401R)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TI_SIMPLELINK`。

<a id="CONFIG_SOC_SERIES_MSPM0G"></a>

## 314.51 `CONFIG_SOC_SERIES_MSPM0G`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 TI MSPM0G 系列片上系统（SoCs）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_TI_MSPM
```

**被选择（Selected by）**

```text
CONFIG_SOC_MSPM0G1105
CONFIG_SOC_MSPM0G1106
CONFIG_SOC_MSPM0G1107
CONFIG_SOC_MSPM0G1505
CONFIG_SOC_MSPM0G1506
CONFIG_SOC_MSPM0G1507
CONFIG_SOC_MSPM0G1518
CONFIG_SOC_MSPM0G1519
CONFIG_SOC_MSPM0G3105
CONFIG_SOC_MSPM0G3106
CONFIG_SOC_MSPM0G3107
CONFIG_SOC_MSPM0G3505
CONFIG_SOC_MSPM0G3506
CONFIG_SOC_MSPM0G3507
CONFIG_SOC_MSPM0G3518
CONFIG_SOC_MSPM0G3519
```

**定义位置（Location）**：[`soc/ti/mspm/mspm0g/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/mspm/mspm0g/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_TI_MSPM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TI_MSPM)、[`CONFIG_SOC_MSPM0G1105`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0G1105)、[`CONFIG_SOC_MSPM0G1106`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0G1106)、[`CONFIG_SOC_MSPM0G1107`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0G1107)、[`CONFIG_SOC_MSPM0G1505`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0G1505)、[`CONFIG_SOC_MSPM0G1506`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0G1506)、[`CONFIG_SOC_MSPM0G1507`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0G1507)、[`CONFIG_SOC_MSPM0G1518`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0G1518)、[`CONFIG_SOC_MSPM0G1519`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0G1519)、[`CONFIG_SOC_MSPM0G3105`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0G3105)、[`CONFIG_SOC_MSPM0G3106`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0G3106)、[`CONFIG_SOC_MSPM0G3107`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0G3107)、[`CONFIG_SOC_MSPM0G3505`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0G3505)、[`CONFIG_SOC_MSPM0G3506`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0G3506)、[`CONFIG_SOC_MSPM0G3507`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0G3507)、[`CONFIG_SOC_MSPM0G3518`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0G3518)、[`CONFIG_SOC_MSPM0G3519`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0G3519)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TI_MSPM`、`CONFIG_SOC_MSPM0G1105`、`CONFIG_SOC_MSPM0G1106`、`CONFIG_SOC_MSPM0G1107`、`CONFIG_SOC_MSPM0G1505`、`CONFIG_SOC_MSPM0G1506`、`CONFIG_SOC_MSPM0G1507`、`CONFIG_SOC_MSPM0G1518`、`CONFIG_SOC_MSPM0G1519`、`CONFIG_SOC_MSPM0G3105`、`CONFIG_SOC_MSPM0G3106`、`CONFIG_SOC_MSPM0G3107`、`CONFIG_SOC_MSPM0G3505`、`CONFIG_SOC_MSPM0G3506`、`CONFIG_SOC_MSPM0G3507`、`CONFIG_SOC_MSPM0G3518`、`CONFIG_SOC_MSPM0G3519`。

<a id="CONFIG_SOC_SERIES_MSPM0L"></a>

## 314.52 `CONFIG_SOC_SERIES_MSPM0L`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 TI MSPM0L 系列片上系统（SoCs）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_TI_MSPM
```

**被选择（Selected by）**

```text
CONFIG_SOC_MSPM0L1105
CONFIG_SOC_MSPM0L1106
CONFIG_SOC_MSPM0L1117
CONFIG_SOC_MSPM0L1227
CONFIG_SOC_MSPM0L1228
CONFIG_SOC_MSPM0L1303
CONFIG_SOC_MSPM0L1304
CONFIG_SOC_MSPM0L1305
CONFIG_SOC_MSPM0L1306
CONFIG_SOC_MSPM0L1343
CONFIG_SOC_MSPM0L1344
CONFIG_SOC_MSPM0L1345
CONFIG_SOC_MSPM0L1346
CONFIG_SOC_MSPM0L2227
CONFIG_SOC_MSPM0L2228
```

**定义位置（Location）**：[`soc/ti/mspm/mspm0l/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/mspm/mspm0l/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_TI_MSPM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TI_MSPM)、[`CONFIG_SOC_MSPM0L1105`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0L1105)、[`CONFIG_SOC_MSPM0L1106`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0L1106)、[`CONFIG_SOC_MSPM0L1117`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0L1117)、[`CONFIG_SOC_MSPM0L1227`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0L1227)、[`CONFIG_SOC_MSPM0L1228`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0L1228)、[`CONFIG_SOC_MSPM0L1303`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0L1303)、[`CONFIG_SOC_MSPM0L1304`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0L1304)、[`CONFIG_SOC_MSPM0L1305`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0L1305)、[`CONFIG_SOC_MSPM0L1306`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0L1306)、[`CONFIG_SOC_MSPM0L1343`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0L1343)、[`CONFIG_SOC_MSPM0L1344`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0L1344)、[`CONFIG_SOC_MSPM0L1345`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0L1345)、[`CONFIG_SOC_MSPM0L1346`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0L1346)、[`CONFIG_SOC_MSPM0L2227`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0L2227)、[`CONFIG_SOC_MSPM0L2228`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0L2228)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TI_MSPM`、`CONFIG_SOC_MSPM0L1105`、`CONFIG_SOC_MSPM0L1106`、`CONFIG_SOC_MSPM0L1117`、`CONFIG_SOC_MSPM0L1227`、`CONFIG_SOC_MSPM0L1228`、`CONFIG_SOC_MSPM0L1303`、`CONFIG_SOC_MSPM0L1304`、`CONFIG_SOC_MSPM0L1305`、`CONFIG_SOC_MSPM0L1306`、`CONFIG_SOC_MSPM0L1343`、`CONFIG_SOC_MSPM0L1344`、`CONFIG_SOC_MSPM0L1345`、`CONFIG_SOC_MSPM0L1346`、`CONFIG_SOC_MSPM0L2227`、`CONFIG_SOC_MSPM0L2228`。

<a id="CONFIG_SOC_SERIES_MSPM33C"></a>

## 314.53 `CONFIG_SOC_SERIES_MSPM33C`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 TI MSPM33C 系列片上系统（SoCs）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_TI_MSPM
```

**被选择（Selected by）**

```text
CONFIG_SOC_MSPM33C321A
```

**定义位置（Location）**：[`soc/ti/mspm/mspm33c/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/mspm/mspm33c/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_TI_MSPM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TI_MSPM)、[`CONFIG_SOC_MSPM33C321A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM33C321A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TI_MSPM`、`CONFIG_SOC_MSPM33C321A`。

<a id="CONFIG_SOC_TI_LM3S6965"></a>

## 314.54 `CONFIG_SOC_TI_LM3S6965`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

TI LM3S6965 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_BOARD_QEMU_CORTEX_M3
```

**定义位置（Location）**：[`soc/ti/lm3s6965/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/lm3s6965/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BOARD_QEMU_CORTEX_M3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_QEMU_CORTEX_M3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_QEMU_CORTEX_M3`。

<a id="CONFIG_SOC_TI_TM4C123GH6PM"></a>

## 314.55 `CONFIG_SOC_TI_TM4C123GH6PM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

TI Tiva C 系列 TM4C123GH6PM：ARM Cortex-M4F、80 MHz、256 KB Flash、32 KB SRAM。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_TM4C123X
```

**被选择（Selected by）**

```text
CONFIG_BOARD_TM4C123GXL
```

**定义位置（Location）**：[`soc/ti/tiva_c/tm4c123x/Kconfig.soc:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/tiva_c/tm4c123x/Kconfig.soc#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_TM4C123X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_TM4C123X)、[`CONFIG_BOARD_TM4C123GXL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_TM4C123GXL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_TM4C123X`、`CONFIG_BOARD_TM4C123GXL`。

<a id="CONFIG_TI_SIMPLELINK_DYNAMIC_DPL_OBJECTS"></a>

## 314.56 `CONFIG_TI_SIMPLELINK_DYNAMIC_DPL_OBJECTS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为驱动移植层对象（DPL objects）开启动态内存分配，并为此预留额外内存。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_TI_SIMPLELINK
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_CC23X0
```

**定义位置（Location）**：[`soc/ti/simplelink/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_TI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TI_SIMPLELINK)、[`CONFIG_SOC_SERIES_CC23X0`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC23X0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TI_SIMPLELINK`。

<a id="SB_CONFIG_SOC_CC1312R"></a>

## 314.57 `SB_CONFIG_SOC_CC1312R`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CC1312R 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_CC13X2_CC26X2
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_CC1312R1_LAUNCHXL
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2_cc26x2/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2_cc26x2/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_CC13X2_CC26X2`](P314_soc_ti_配置项参考.md#SB_CONFIG_SOC_SERIES_CC13X2_CC26X2)、[`SB_CONFIG_BOARD_CC1312R1_LAUNCHXL`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_CC1312R1_LAUNCHXL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_CC1312R1_LAUNCHXL`。

<a id="SB_CONFIG_SOC_CC1352P"></a>

## 314.58 `SB_CONFIG_SOC_CC1352P`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CC1352P 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_CC13X2_CC26X2
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_CC1352P1_LAUNCHXL
SB_CONFIG_BOARD_BEAGLECONNECT_FREEDOM
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2_cc26x2/Kconfig.soc:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2_cc26x2/Kconfig.soc#L18)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_CC13X2_CC26X2`](P314_soc_ti_配置项参考.md#SB_CONFIG_SOC_SERIES_CC13X2_CC26X2)、[`SB_CONFIG_BOARD_CC1352P1_LAUNCHXL`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_CC1352P1_LAUNCHXL)、[`SB_CONFIG_BOARD_BEAGLECONNECT_FREEDOM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_BEAGLECONNECT_FREEDOM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_CC1352P1_LAUNCHXL`、`SB_CONFIG_BOARD_BEAGLECONNECT_FREEDOM`。

<a id="SB_CONFIG_SOC_CC1352P7"></a>

## 314.59 `SB_CONFIG_SOC_CC1352P7`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CC1352P7 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_CC1352P7_LP
SB_CONFIG_BOARD_BEAGLEPLAY
SB_CONFIG_BOARD_BEAGLECONNECT_FREEDOM
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7`](P314_soc_ti_配置项参考.md#SB_CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7)、[`SB_CONFIG_BOARD_CC1352P7_LP`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_CC1352P7_LP)、[`SB_CONFIG_BOARD_BEAGLEPLAY`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_BEAGLEPLAY)、[`SB_CONFIG_BOARD_BEAGLECONNECT_FREEDOM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_BEAGLECONNECT_FREEDOM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_CC1352P7_LP`、`SB_CONFIG_BOARD_BEAGLEPLAY`、`SB_CONFIG_BOARD_BEAGLECONNECT_FREEDOM`。

<a id="SB_CONFIG_SOC_CC1352R"></a>

## 314.60 `SB_CONFIG_SOC_CC1352R`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CC1352R 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_CC13X2_CC26X2
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_CC1352R1_LAUNCHXL
SB_CONFIG_BOARD_CC1352R_SENSORTAG
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2_cc26x2/Kconfig.soc:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2_cc26x2/Kconfig.soc#L24)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_CC13X2_CC26X2`](P314_soc_ti_配置项参考.md#SB_CONFIG_SOC_SERIES_CC13X2_CC26X2)、[`SB_CONFIG_BOARD_CC1352R1_LAUNCHXL`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_CC1352R1_LAUNCHXL)、[`SB_CONFIG_BOARD_CC1352R_SENSORTAG`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_CC1352R_SENSORTAG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_CC1352R1_LAUNCHXL`、`SB_CONFIG_BOARD_CC1352R_SENSORTAG`。

<a id="SB_CONFIG_SOC_CC1352R7"></a>

## 314.61 `SB_CONFIG_SOC_CC1352R7`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CC1352R7 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig.soc:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig.soc#L17)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7`](P314_soc_ti_配置项参考.md#SB_CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7)。

<a id="SB_CONFIG_SOC_CC2340R5"></a>

## 314.62 `SB_CONFIG_SOC_CC2340R5`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CC2340R5 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_CC23X0
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_LP_EM_CC2340R5
```

**定义位置（Location）**：[`soc/ti/simplelink/cc23x0/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc23x0/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_CC23X0`](P314_soc_ti_配置项参考.md#SB_CONFIG_SOC_SERIES_CC23X0)、[`SB_CONFIG_BOARD_LP_EM_CC2340R5`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_LP_EM_CC2340R5)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_LP_EM_CC2340R5`。

<a id="SB_CONFIG_SOC_CC2652P"></a>

## 314.63 `SB_CONFIG_SOC_CC2652P`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CC2652P 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_CC13X2_CC26X2
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2_cc26x2/Kconfig.soc:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2_cc26x2/Kconfig.soc#L30)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_CC13X2_CC26X2`](P314_soc_ti_配置项参考.md#SB_CONFIG_SOC_SERIES_CC13X2_CC26X2)。

<a id="SB_CONFIG_SOC_CC2652P7"></a>

## 314.64 `SB_CONFIG_SOC_CC2652P7`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CC2652P7 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig.soc:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig.soc#L23)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7`](P314_soc_ti_配置项参考.md#SB_CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7)。

<a id="SB_CONFIG_SOC_CC2652R"></a>

## 314.65 `SB_CONFIG_SOC_CC2652R`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CC2652R 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_CC13X2_CC26X2
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_CC26X2R1_LAUNCHXL
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2_cc26x2/Kconfig.soc:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2_cc26x2/Kconfig.soc#L36)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_CC13X2_CC26X2`](P314_soc_ti_配置项参考.md#SB_CONFIG_SOC_SERIES_CC13X2_CC26X2)、[`SB_CONFIG_BOARD_CC26X2R1_LAUNCHXL`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_CC26X2R1_LAUNCHXL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_CC26X2R1_LAUNCHXL`。

<a id="SB_CONFIG_SOC_CC2652R7"></a>

## 314.66 `SB_CONFIG_SOC_CC2652R7`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CC2652R7 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig.soc:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig.soc#L29)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7`](P314_soc_ti_配置项参考.md#SB_CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7)。

<a id="SB_CONFIG_SOC_CC3220SF"></a>

## 314.67 `SB_CONFIG_SOC_CC3220SF`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CC3220SF 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_CC32XX
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_CC3220SF_LAUNCHXL
```

**定义位置（Location）**：[`soc/ti/simplelink/cc32xx/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc32xx/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_CC32XX`](P314_soc_ti_配置项参考.md#SB_CONFIG_SOC_SERIES_CC32XX)、[`SB_CONFIG_BOARD_CC3220SF_LAUNCHXL`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_CC3220SF_LAUNCHXL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_CC3220SF_LAUNCHXL`。

<a id="SB_CONFIG_SOC_CC3235SF"></a>

## 314.68 `SB_CONFIG_SOC_CC3235SF`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CC3235SF 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_CC32XX
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_CC3235SF_LAUNCHXL
```

**定义位置（Location）**：[`soc/ti/simplelink/cc32xx/Kconfig.soc:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc32xx/Kconfig.soc#L17)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_CC32XX`](P314_soc_ti_配置项参考.md#SB_CONFIG_SOC_SERIES_CC32XX)、[`SB_CONFIG_BOARD_CC3235SF_LAUNCHXL`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_CC3235SF_LAUNCHXL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_CC3235SF_LAUNCHXL`。

<a id="SB_CONFIG_SOC_MSP432P401R"></a>

## 314.69 `SB_CONFIG_SOC_MSP432P401R`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

MSP432P401R 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_MSP432P4XX
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_MSP_EXP432P401R_LAUNCHXL
```

**定义位置（Location）**：[`soc/ti/simplelink/msp432p4xx/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/msp432p4xx/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_MSP432P4XX`](P314_soc_ti_配置项参考.md#SB_CONFIG_SOC_SERIES_MSP432P4XX)、[`SB_CONFIG_BOARD_MSP_EXP432P401R_LAUNCHXL`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MSP_EXP432P401R_LAUNCHXL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_MSP_EXP432P401R_LAUNCHXL`。

<a id="SB_CONFIG_SOC_SERIES_AM13E"></a>

## 314.70 `SB_CONFIG_SOC_SERIES_AM13E`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 TI AM13E 系列片上系统（SoCs）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_TI_AM13
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_AM13E23019
```

**定义位置（Location）**：[`soc/ti/am13/am13e/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/am13/am13e/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_TI_AM13`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_TI_AM13)、[`SB_CONFIG_SOC_AM13E23019`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_AM13E23019)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_TI_AM13`、`SB_CONFIG_SOC_AM13E23019`。

<a id="SB_CONFIG_SOC_SERIES_AM62LX_A53"></a>

## 314.71 `SB_CONFIG_SOC_SERIES_AM62LX_A53`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 AM62LX A53 系列支持（Series support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_AM62LX
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_AM62L3_A53
```

**定义位置（Location）**：[`soc/ti/k3/am62lx/Kconfig.soc:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/k3/am62lx/Kconfig.soc#L9)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_AM62LX`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SERIES_AM62LX)、[`SB_CONFIG_SOC_AM62L3_A53`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_AM62L3_A53)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SERIES_AM62LX`、`SB_CONFIG_SOC_AM62L3_A53`。

<a id="SB_CONFIG_SOC_SERIES_AM62X_A53"></a>

## 314.72 `SB_CONFIG_SOC_SERIES_AM62X_A53`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 AM62X A53 系列支持（Series support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_AM62X
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_AM6234_A53
SB_CONFIG_SOC_AM6254_A53
SB_CONFIG_SOC_AM6232_A53
```

**定义位置（Location）**：[`soc/ti/k3/am62x/Kconfig.soc:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/k3/am62x/Kconfig.soc#L9)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_AM62X`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SERIES_AM62X)、[`SB_CONFIG_SOC_AM6234_A53`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_AM6234_A53)、[`SB_CONFIG_SOC_AM6254_A53`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_AM6254_A53)、[`SB_CONFIG_SOC_AM6232_A53`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_AM6232_A53)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SERIES_AM62X`、`SB_CONFIG_SOC_AM6234_A53`、`SB_CONFIG_SOC_AM6254_A53`、`SB_CONFIG_SOC_AM6232_A53`。

<a id="SB_CONFIG_SOC_SERIES_AM62X_M4"></a>

## 314.73 `SB_CONFIG_SOC_SERIES_AM62X_M4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 AM62X M4 系列支持（Series support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_AM62X
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_AM6234_M4
SB_CONFIG_SOC_AM6254_M4
SB_CONFIG_SOC_AM6232_M4
```

**定义位置（Location）**：[`soc/ti/k3/am62x/Kconfig.soc:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/k3/am62x/Kconfig.soc#L15)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_AM62X`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SERIES_AM62X)、[`SB_CONFIG_SOC_AM6234_M4`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_AM6234_M4)、[`SB_CONFIG_SOC_AM6254_M4`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_AM6254_M4)、[`SB_CONFIG_SOC_AM6232_M4`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_AM6232_M4)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SERIES_AM62X`、`SB_CONFIG_SOC_AM6234_M4`、`SB_CONFIG_SOC_AM6254_M4`、`SB_CONFIG_SOC_AM6232_M4`。

<a id="SB_CONFIG_SOC_SERIES_AM64X_M4"></a>

## 314.74 `SB_CONFIG_SOC_SERIES_AM64X_M4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 AM64X M4 系列支持（Series support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_AM64X
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_AM6442_M4
SB_CONFIG_SOC_AM2434_M4
```

**定义位置（Location）**：[`soc/ti/k3/am64x/Kconfig.soc:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/k3/am64x/Kconfig.soc#L9)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_AM64X`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SERIES_AM64X)、[`SB_CONFIG_SOC_AM6442_M4`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_AM6442_M4)、[`SB_CONFIG_SOC_AM2434_M4`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_AM2434_M4)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SERIES_AM64X`、`SB_CONFIG_SOC_AM6442_M4`、`SB_CONFIG_SOC_AM2434_M4`。

<a id="SB_CONFIG_SOC_SERIES_AM64X_R5"></a>

## 314.75 `SB_CONFIG_SOC_SERIES_AM64X_R5`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 AM64X R5 系列支持（Series support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_AM64X
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_AM2434_R5F0_0
SB_CONFIG_SOC_AM6442_R5F0_0
SB_CONFIG_SOC_AM6442_R5F0_1
SB_CONFIG_SOC_AM6442_R5F1_0
SB_CONFIG_SOC_AM6442_R5F1_1
```

**定义位置（Location）**：[`soc/ti/k3/am64x/Kconfig.soc:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/k3/am64x/Kconfig.soc#L15)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_AM64X`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SERIES_AM64X)、[`SB_CONFIG_SOC_AM2434_R5F0_0`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_AM2434_R5F0_0)、[`SB_CONFIG_SOC_AM6442_R5F0_0`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_AM6442_R5F0_0)、[`SB_CONFIG_SOC_AM6442_R5F0_1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_AM6442_R5F0_1)、[`SB_CONFIG_SOC_AM6442_R5F1_0`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_AM6442_R5F1_0)、[`SB_CONFIG_SOC_AM6442_R5F1_1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_AM6442_R5F1_1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SERIES_AM64X`、`SB_CONFIG_SOC_AM2434_R5F0_0`、`SB_CONFIG_SOC_AM6442_R5F0_0`、`SB_CONFIG_SOC_AM6442_R5F0_1`、`SB_CONFIG_SOC_AM6442_R5F1_0`、`SB_CONFIG_SOC_AM6442_R5F1_1`。

<a id="SB_CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7"></a>

## 314.76 `SB_CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 TI SimpleLink CC13x2x7／CC26x2x7 片上系统（SoCs）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_TI_SIMPLELINK
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_CC1352P7
SB_CONFIG_SOC_CC1352R7
SB_CONFIG_SOC_CC2652P7
SB_CONFIG_SOC_CC2652R7
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2x7_cc26x2x7/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_TI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_TI_SIMPLELINK)、[`SB_CONFIG_SOC_CC1352P7`](P314_soc_ti_配置项参考.md#SB_CONFIG_SOC_CC1352P7)、[`SB_CONFIG_SOC_CC1352R7`](P314_soc_ti_配置项参考.md#SB_CONFIG_SOC_CC1352R7)、[`SB_CONFIG_SOC_CC2652P7`](P314_soc_ti_配置项参考.md#SB_CONFIG_SOC_CC2652P7)、[`SB_CONFIG_SOC_CC2652R7`](P314_soc_ti_配置项参考.md#SB_CONFIG_SOC_CC2652R7)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_TI_SIMPLELINK`。

<a id="SB_CONFIG_SOC_SERIES_CC13X2_CC26X2"></a>

## 314.77 `SB_CONFIG_SOC_SERIES_CC13X2_CC26X2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 TI SimpleLink CC13x2／CC26x2 片上系统（SoCs）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_TI_SIMPLELINK
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_CC1312R
SB_CONFIG_SOC_CC1352P
SB_CONFIG_SOC_CC1352R
SB_CONFIG_SOC_CC2652P
SB_CONFIG_SOC_CC2652R
```

**定义位置（Location）**：[`soc/ti/simplelink/cc13x2_cc26x2/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc13x2_cc26x2/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_TI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_TI_SIMPLELINK)、[`SB_CONFIG_SOC_CC1312R`](P314_soc_ti_配置项参考.md#SB_CONFIG_SOC_CC1312R)、[`SB_CONFIG_SOC_CC1352P`](P314_soc_ti_配置项参考.md#SB_CONFIG_SOC_CC1352P)、[`SB_CONFIG_SOC_CC1352R`](P314_soc_ti_配置项参考.md#SB_CONFIG_SOC_CC1352R)、[`SB_CONFIG_SOC_CC2652P`](P314_soc_ti_配置项参考.md#SB_CONFIG_SOC_CC2652P)、[`SB_CONFIG_SOC_CC2652R`](P314_soc_ti_配置项参考.md#SB_CONFIG_SOC_CC2652R)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_TI_SIMPLELINK`。

<a id="SB_CONFIG_SOC_SERIES_CC23X0"></a>

## 314.78 `SB_CONFIG_SOC_SERIES_CC23X0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 TI SimpleLink CC23X0 系列片上系统（SoCs）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_TI_SIMPLELINK
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_CC2340R5
```

**定义位置（Location）**：[`soc/ti/simplelink/cc23x0/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc23x0/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_TI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_TI_SIMPLELINK)、[`SB_CONFIG_SOC_CC2340R5`](P314_soc_ti_配置项参考.md#SB_CONFIG_SOC_CC2340R5)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_TI_SIMPLELINK`。

<a id="SB_CONFIG_SOC_SERIES_CC32XX"></a>

## 314.79 `SB_CONFIG_SOC_SERIES_CC32XX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 TI SimpleLink CC32xx 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_TI_SIMPLELINK
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_CC3220SF
SB_CONFIG_SOC_CC3235SF
```

**定义位置（Location）**：[`soc/ti/simplelink/cc32xx/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/cc32xx/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_TI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_TI_SIMPLELINK)、[`SB_CONFIG_SOC_CC3220SF`](P314_soc_ti_配置项参考.md#SB_CONFIG_SOC_CC3220SF)、[`SB_CONFIG_SOC_CC3235SF`](P314_soc_ti_配置项参考.md#SB_CONFIG_SOC_CC3235SF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_TI_SIMPLELINK`。

<a id="SB_CONFIG_SOC_SERIES_J721E_R5"></a>

## 314.80 `SB_CONFIG_SOC_SERIES_J721E_R5`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 J721E R5 系列支持（Series support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_J721E
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_J721E_MAIN_R5F0_0
SB_CONFIG_SOC_J721E_MAIN_R5F0_1
SB_CONFIG_SOC_J721E_MAIN_R5F1_0
SB_CONFIG_SOC_J721E_MAIN_R5F1_1
SB_CONFIG_SOC_J721E_MCU_R5F0_0
SB_CONFIG_SOC_J721E_MCU_R5F0_1
```

**定义位置（Location）**：[`soc/ti/k3/j721e/Kconfig.soc:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/k3/j721e/Kconfig.soc#L9)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_J721E`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SERIES_J721E)、[`SB_CONFIG_SOC_J721E_MAIN_R5F0_0`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_J721E_MAIN_R5F0_0)、[`SB_CONFIG_SOC_J721E_MAIN_R5F0_1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_J721E_MAIN_R5F0_1)、[`SB_CONFIG_SOC_J721E_MAIN_R5F1_0`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_J721E_MAIN_R5F1_0)、[`SB_CONFIG_SOC_J721E_MAIN_R5F1_1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_J721E_MAIN_R5F1_1)、[`SB_CONFIG_SOC_J721E_MCU_R5F0_0`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_J721E_MCU_R5F0_0)、[`SB_CONFIG_SOC_J721E_MCU_R5F0_1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_J721E_MCU_R5F0_1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SERIES_J721E`、`SB_CONFIG_SOC_J721E_MAIN_R5F0_0`、`SB_CONFIG_SOC_J721E_MAIN_R5F0_1`、`SB_CONFIG_SOC_J721E_MAIN_R5F1_0`、`SB_CONFIG_SOC_J721E_MAIN_R5F1_1`、`SB_CONFIG_SOC_J721E_MCU_R5F0_0`、`SB_CONFIG_SOC_J721E_MCU_R5F0_1`。

<a id="SB_CONFIG_SOC_SERIES_J722S_R5"></a>

## 314.81 `SB_CONFIG_SOC_SERIES_J722S_R5`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 J722S R5 系列支持（Series support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_J722S
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_J722S_MAIN_R5F0_0
SB_CONFIG_SOC_J722S_MCU_R5F0_0
```

**定义位置（Location）**：[`soc/ti/k3/j722s/Kconfig.soc:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/k3/j722s/Kconfig.soc#L9)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_J722S`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SERIES_J722S)、[`SB_CONFIG_SOC_J722S_MAIN_R5F0_0`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_J722S_MAIN_R5F0_0)、[`SB_CONFIG_SOC_J722S_MCU_R5F0_0`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_J722S_MCU_R5F0_0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SERIES_J722S`、`SB_CONFIG_SOC_J722S_MAIN_R5F0_0`、`SB_CONFIG_SOC_J722S_MCU_R5F0_0`。

<a id="SB_CONFIG_SOC_SERIES_MSP432P4XX"></a>

## 314.82 `SB_CONFIG_SOC_SERIES_MSP432P4XX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 TI SimpleLink MSP432P4XX 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_TI_SIMPLELINK
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_MSP432P401R
```

**定义位置（Location）**：[`soc/ti/simplelink/msp432p4xx/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/simplelink/msp432p4xx/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_TI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_TI_SIMPLELINK)、[`SB_CONFIG_SOC_MSP432P401R`](P314_soc_ti_配置项参考.md#SB_CONFIG_SOC_MSP432P401R)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_TI_SIMPLELINK`。

<a id="SB_CONFIG_SOC_SERIES_MSPM0G"></a>

## 314.83 `SB_CONFIG_SOC_SERIES_MSPM0G`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 TI MSPM0G 系列片上系统（SoCs）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_TI_MSPM
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_MSPM0G1105
SB_CONFIG_SOC_MSPM0G1106
SB_CONFIG_SOC_MSPM0G1107
SB_CONFIG_SOC_MSPM0G1505
SB_CONFIG_SOC_MSPM0G1506
SB_CONFIG_SOC_MSPM0G1507
SB_CONFIG_SOC_MSPM0G1518
SB_CONFIG_SOC_MSPM0G1519
SB_CONFIG_SOC_MSPM0G3105
SB_CONFIG_SOC_MSPM0G3106
SB_CONFIG_SOC_MSPM0G3107
SB_CONFIG_SOC_MSPM0G3505
SB_CONFIG_SOC_MSPM0G3506
SB_CONFIG_SOC_MSPM0G3507
SB_CONFIG_SOC_MSPM0G3518
SB_CONFIG_SOC_MSPM0G3519
```

**定义位置（Location）**：[`soc/ti/mspm/mspm0g/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/mspm/mspm0g/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_TI_MSPM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_TI_MSPM)、[`SB_CONFIG_SOC_MSPM0G1105`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM0G1105)、[`SB_CONFIG_SOC_MSPM0G1106`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM0G1106)、[`SB_CONFIG_SOC_MSPM0G1107`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM0G1107)、[`SB_CONFIG_SOC_MSPM0G1505`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM0G1505)、[`SB_CONFIG_SOC_MSPM0G1506`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM0G1506)、[`SB_CONFIG_SOC_MSPM0G1507`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM0G1507)、[`SB_CONFIG_SOC_MSPM0G1518`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM0G1518)、[`SB_CONFIG_SOC_MSPM0G1519`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM0G1519)、[`SB_CONFIG_SOC_MSPM0G3105`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM0G3105)、[`SB_CONFIG_SOC_MSPM0G3106`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM0G3106)、[`SB_CONFIG_SOC_MSPM0G3107`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM0G3107)、[`SB_CONFIG_SOC_MSPM0G3505`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM0G3505)、[`SB_CONFIG_SOC_MSPM0G3506`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM0G3506)、[`SB_CONFIG_SOC_MSPM0G3507`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM0G3507)、[`SB_CONFIG_SOC_MSPM0G3518`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM0G3518)、[`SB_CONFIG_SOC_MSPM0G3519`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM0G3519)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_TI_MSPM`、`SB_CONFIG_SOC_MSPM0G1105`、`SB_CONFIG_SOC_MSPM0G1106`、`SB_CONFIG_SOC_MSPM0G1107`、`SB_CONFIG_SOC_MSPM0G1505`、`SB_CONFIG_SOC_MSPM0G1506`、`SB_CONFIG_SOC_MSPM0G1507`、`SB_CONFIG_SOC_MSPM0G1518`、`SB_CONFIG_SOC_MSPM0G1519`、`SB_CONFIG_SOC_MSPM0G3105`、`SB_CONFIG_SOC_MSPM0G3106`、`SB_CONFIG_SOC_MSPM0G3107`、`SB_CONFIG_SOC_MSPM0G3505`、`SB_CONFIG_SOC_MSPM0G3506`、`SB_CONFIG_SOC_MSPM0G3507`、`SB_CONFIG_SOC_MSPM0G3518`、`SB_CONFIG_SOC_MSPM0G3519`。

<a id="SB_CONFIG_SOC_SERIES_MSPM0L"></a>

## 314.84 `SB_CONFIG_SOC_SERIES_MSPM0L`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 TI MSPM0L 系列片上系统（SoCs）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_TI_MSPM
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_MSPM0L1105
SB_CONFIG_SOC_MSPM0L1106
SB_CONFIG_SOC_MSPM0L1117
SB_CONFIG_SOC_MSPM0L1227
SB_CONFIG_SOC_MSPM0L1228
SB_CONFIG_SOC_MSPM0L1303
SB_CONFIG_SOC_MSPM0L1304
SB_CONFIG_SOC_MSPM0L1305
SB_CONFIG_SOC_MSPM0L1306
SB_CONFIG_SOC_MSPM0L1343
SB_CONFIG_SOC_MSPM0L1344
SB_CONFIG_SOC_MSPM0L1345
SB_CONFIG_SOC_MSPM0L1346
SB_CONFIG_SOC_MSPM0L2227
SB_CONFIG_SOC_MSPM0L2228
```

**定义位置（Location）**：[`soc/ti/mspm/mspm0l/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/mspm/mspm0l/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_TI_MSPM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_TI_MSPM)、[`SB_CONFIG_SOC_MSPM0L1105`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM0L1105)、[`SB_CONFIG_SOC_MSPM0L1106`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM0L1106)、[`SB_CONFIG_SOC_MSPM0L1117`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM0L1117)、[`SB_CONFIG_SOC_MSPM0L1227`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM0L1227)、[`SB_CONFIG_SOC_MSPM0L1228`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM0L1228)、[`SB_CONFIG_SOC_MSPM0L1303`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM0L1303)、[`SB_CONFIG_SOC_MSPM0L1304`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM0L1304)、[`SB_CONFIG_SOC_MSPM0L1305`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM0L1305)、[`SB_CONFIG_SOC_MSPM0L1306`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM0L1306)、[`SB_CONFIG_SOC_MSPM0L1343`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM0L1343)、[`SB_CONFIG_SOC_MSPM0L1344`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM0L1344)、[`SB_CONFIG_SOC_MSPM0L1345`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM0L1345)、[`SB_CONFIG_SOC_MSPM0L1346`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM0L1346)、[`SB_CONFIG_SOC_MSPM0L2227`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM0L2227)、[`SB_CONFIG_SOC_MSPM0L2228`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM0L2228)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_TI_MSPM`、`SB_CONFIG_SOC_MSPM0L1105`、`SB_CONFIG_SOC_MSPM0L1106`、`SB_CONFIG_SOC_MSPM0L1117`、`SB_CONFIG_SOC_MSPM0L1227`、`SB_CONFIG_SOC_MSPM0L1228`、`SB_CONFIG_SOC_MSPM0L1303`、`SB_CONFIG_SOC_MSPM0L1304`、`SB_CONFIG_SOC_MSPM0L1305`、`SB_CONFIG_SOC_MSPM0L1306`、`SB_CONFIG_SOC_MSPM0L1343`、`SB_CONFIG_SOC_MSPM0L1344`、`SB_CONFIG_SOC_MSPM0L1345`、`SB_CONFIG_SOC_MSPM0L1346`、`SB_CONFIG_SOC_MSPM0L2227`、`SB_CONFIG_SOC_MSPM0L2228`。

<a id="SB_CONFIG_SOC_SERIES_MSPM33C"></a>

## 314.85 `SB_CONFIG_SOC_SERIES_MSPM33C`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 TI MSPM33C 系列片上系统（SoCs）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_TI_MSPM
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_MSPM33C321A
```

**定义位置（Location）**：[`soc/ti/mspm/mspm33c/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/mspm/mspm33c/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_TI_MSPM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_TI_MSPM)、[`SB_CONFIG_SOC_MSPM33C321A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MSPM33C321A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_TI_MSPM`、`SB_CONFIG_SOC_MSPM33C321A`。

<a id="SB_CONFIG_SOC_TI_LM3S6965"></a>

## 314.86 `SB_CONFIG_SOC_TI_LM3S6965`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

TI LM3S6965 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_QEMU_CORTEX_M3
```

**定义位置（Location）**：[`soc/ti/lm3s6965/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/lm3s6965/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_BOARD_QEMU_CORTEX_M3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_QEMU_CORTEX_M3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_QEMU_CORTEX_M3`。

<a id="SB_CONFIG_SOC_TI_TM4C123GH6PM"></a>

## 314.87 `SB_CONFIG_SOC_TI_TM4C123GH6PM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

TI Tiva C 系列 TM4C123GH6PM：ARM Cortex-M4F、80 MHz、256 KB Flash、32 KB SRAM。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_TM4C123X
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_TM4C123GXL
```

**定义位置（Location）**：[`soc/ti/tiva_c/tm4c123x/Kconfig.soc:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ti/tiva_c/tm4c123x/Kconfig.soc#L15)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_TM4C123X`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SERIES_TM4C123X)、[`SB_CONFIG_BOARD_TM4C123GXL`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_TM4C123GXL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SERIES_TM4C123X`、`SB_CONFIG_BOARD_TM4C123GXL`。

<!-- kconfig-navigation -->

[上一章](P313_soc_telink_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P315_soc_wch_配置项参考.md)
