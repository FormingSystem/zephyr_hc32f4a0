---
id: learning.zephyr-docs.kconfig-reference.page-82
title: "`drivers/edac`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第82章\_`drivers/edac`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/edac` 的 11 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_EDAC"></a>

## 82.1 `CONFIG_EDAC`

**提示（Prompt）**：错误检测与纠正（Error Detection and Correction，EDAC）驱动

**说明（Help）**

启用错误检测与纠正（Error Detection and Correction，EDAC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/edac/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/edac/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_EDAC_ERROR_INJECT"></a>

## 82.2 `CONFIG_EDAC_ERROR_INJECT`

**提示（Prompt）**：EDAC 错误注入机制（Error Injection Mechanism）

**说明（Help）**

启用错误注入（Error Injection）功能，以测试错误检查和报告。不应在生产系统（Production System）中启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EDAC
```

**定义位置（Location）**：[`drivers/edac/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/edac/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 错误检测与纠正（Error Detection and Correction，EDAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_EDAC`](P082_drivers_edac_配置项参考.md#CONFIG_EDAC)。

<a id="CONFIG_EDAC_IBECC"></a>

## 82.3 `CONFIG_EDAC_IBECC`

**提示（Prompt）**：带内纠错码（In-Band ECC，IBECC）

**说明（Help）**

此选项选择带内纠错码（In-Band ECC，IBECC）IP 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86 && CONFIG_PCIE && CONFIG_EDAC
```

**定义位置（Location）**：[`drivers/edac/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/edac/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 错误检测与纠正（Error Detection and Correction，EDAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_PCIE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PCIE)、[`CONFIG_EDAC`](P082_drivers_edac_配置项参考.md#CONFIG_EDAC)。

<a id="CONFIG_EDAC_NXP_EIM"></a>

## 82.4 `CONFIG_EDAC_NXP_EIM`

**提示（Prompt）**：NXP EIM 驱动

**说明（Help）**

启用 NXP 错误注入模块（Error Injection Module，EIM）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_EIM_ENABLED && CONFIG_EDAC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/edac/Kconfig.mcux_erm:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/edac/Kconfig.mcux_erm#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 错误检测与纠正（Error Detection and Correction，EDAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_EDAC`](P082_drivers_edac_配置项参考.md#CONFIG_EDAC)。

<a id="CONFIG_EDAC_NXP_ERM"></a>

## 82.5 `CONFIG_EDAC_NXP_ERM`

**提示（Prompt）**：NXP ERM 驱动

**说明（Help）**

启用 NXP 错误报告模块（Error Reporting Module，ERM）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_ERM_ENABLED && CONFIG_EDAC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/edac/Kconfig.mcux_erm:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/edac/Kconfig.mcux_erm#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 错误检测与纠正（Error Detection and Correction，EDAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_EDAC`](P082_drivers_edac_配置项参考.md#CONFIG_EDAC)。

<a id="CONFIG_EDAC_NXP_ERM_DEFAULT_CHANNEL"></a>

## 82.6 `CONFIG_EDAC_NXP_ERM_DEFAULT_CHANNEL`

**提示（Prompt）**：NXP ERM 默认通道（Default Channel）

**说明（Help）**

设置 NXP 错误报告模块（Error Reporting Module）的默认通道（Default Channel）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_EDAC_NXP_ERM && CONFIG_EDAC
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/edac/Kconfig.mcux_erm:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/edac/Kconfig.mcux_erm#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 错误检测与纠正（Error Detection and Correction，EDAC）驱动 → NXP ERM 驱动

**配置项引用（Symbol References）**：[`CONFIG_EDAC_NXP_ERM`](P082_drivers_edac_配置项参考.md#CONFIG_EDAC_NXP_ERM)、[`CONFIG_EDAC`](P082_drivers_edac_配置项参考.md#CONFIG_EDAC)。

<a id="CONFIG_EDAC_NXP_ERM_VARY_WITH_EIM_CHANNEL"></a>

## 82.7 `CONFIG_EDAC_NXP_ERM_VARY_WITH_EIM_CHANNEL`

**提示（Prompt）**：根据 EIM 通道更新 EIM 通道（Update EIM Channel Based on EIM Channel）

**说明（Help）**

允许错误报告模块（ERM）通道根据所选的错误注入模块（EIM）通道动态调整。

> 译注：官方提示文本将被更新的通道写为 EIM，而帮助正文写为 ERM；此处分别保留两者的表述。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EDAC_NXP_EIM && CONFIG_EDAC_NXP_ERM && CONFIG_EDAC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/edac/Kconfig.mcux_erm:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/edac/Kconfig.mcux_erm#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 错误检测与纠正（Error Detection and Correction，EDAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_EDAC_NXP_EIM`](P082_drivers_edac_配置项参考.md#CONFIG_EDAC_NXP_EIM)、[`CONFIG_EDAC_NXP_ERM`](P082_drivers_edac_配置项参考.md#CONFIG_EDAC_NXP_ERM)、[`CONFIG_EDAC`](P082_drivers_edac_配置项参考.md#CONFIG_EDAC)。

<a id="CONFIG_EDAC_NXP_ERROR_INJECT"></a>

## 82.8 `CONFIG_EDAC_NXP_ERROR_INJECT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

这是一个辅助配置（Helper Configuration），当 `EDAC_ERROR_INJECT` 和 `EDAC_NXP_EIM` 均启用时启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EDAC
```

**默认值（Defaults）**

```text
y if CONFIG_EDAC_ERROR_INJECT && CONFIG_EDAC_NXP_EIM
```

**定义位置（Location）**：[`drivers/edac/Kconfig.mcux_erm:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/edac/Kconfig.mcux_erm#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 错误检测与纠正（Error Detection and Correction，EDAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_EDAC`](P082_drivers_edac_配置项参考.md#CONFIG_EDAC)、[`CONFIG_EDAC_ERROR_INJECT`](P082_drivers_edac_配置项参考.md#CONFIG_EDAC_ERROR_INJECT)、[`CONFIG_EDAC_NXP_EIM`](P082_drivers_edac_配置项参考.md#CONFIG_EDAC_NXP_EIM)。

<a id="CONFIG_EDAC_NXP_MECC"></a>

## 82.9 `CONFIG_EDAC_NXP_MECC`

**提示（Prompt）**：NXP MECC EDAC 驱动

**说明（Help）**

启用 NXP 内存 ECC 控制器（Memory ECC Controller，MECC）的 EDAC 驱动。此驱动通过标准 EDAC 接口，为片上 RAM（On-Chip RAM，OCRAM）访问提供单错纠正、双错检测（Single Error Correction and Double Error Detection，SEC-DED）ECC 功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_MECC_ENABLED && CONFIG_EDAC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/edac/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/edac/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 错误检测与纠正（Error Detection and Correction，EDAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_EDAC`](P082_drivers_edac_配置项参考.md#CONFIG_EDAC)。

<a id="CONFIG_EDAC_SHELL"></a>

## 82.10 `CONFIG_EDAC_SHELL`

**提示（Prompt）**：EDAC 命令行（Shell）

**说明（Help）**

启用 EDAC 命令行（Shell），用于调试 EDAC。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_EDAC
```

**定义位置（Location）**：[`drivers/edac/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/edac/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 错误检测与纠正（Error Detection and Correction，EDAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_EDAC`](P082_drivers_edac_配置项参考.md#CONFIG_EDAC)。

<a id="CONFIG_EDAC_SYNOPSYS"></a>

## 82.11 `CONFIG_EDAC_SYNOPSYS`

**提示（Prompt）**：Synopsys DDR 控制器 EDAC 驱动（原提示拼作 Synopsis）

**说明（Help）**

启用 Synopsys DDR 控制器（DDR Controller）的 EDAC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XLNX_ZYNQMP_DDRC_2_40A_ENABLED && CONFIG_EDAC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/edac/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/edac/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 错误检测与纠正（Error Detection and Correction，EDAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_EDAC`](P082_drivers_edac_配置项参考.md#CONFIG_EDAC)。

<!-- kconfig-navigation -->

[上一章](P081_drivers_dp_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P083_drivers_eeprom_配置项参考.md)
