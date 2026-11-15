---
id: learning.zephyr-docs.kconfig-reference.page-410
title: "`subsys/nvmem`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第410章\_`subsys/nvmem`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/nvmem` 的 7 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_NVMEM"></a>

## 410.1 `CONFIG_NVMEM`

**提示（Prompt）**：非易失性存储器（Non Volatile Memory，NVMEM）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_HWINFO_NVMEM
CONFIG_IEEE802154_MCXW
```

**被弱选择（Implied by）**

```text
CONFIG_ETH_SAM_GMAC
```

**定义位置（Location）**：[`subsys/nvmem/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/nvmem/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_HWINFO_NVMEM`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_NVMEM)、[`CONFIG_IEEE802154_MCXW`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_MCXW)、[`CONFIG_ETH_SAM_GMAC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_SAM_GMAC)。

<a id="CONFIG_NVMEM_BBRAM"></a>

## 410.2 `CONFIG_NVMEM_BBRAM`

**提示（Prompt）**：电池后备 RAM（Battery-Backed RAM）的非易失性存储（NVMEM）支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BBRAM && CONFIG_NVMEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/nvmem/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/nvmem/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 非易失性存储器（Non Volatile Memory，NVMEM）

**配置项引用（Symbol References）**：[`CONFIG_BBRAM`](P052_drivers_bbram_配置项参考.md#CONFIG_BBRAM)、[`CONFIG_NVMEM`](P410_subsys_nvmem_配置项参考.md#CONFIG_NVMEM)。

<a id="CONFIG_NVMEM_EEPROM"></a>

## 410.3 `CONFIG_NVMEM_EEPROM`

**提示（Prompt）**：EEPROM 设备的非易失性存储（NVMEM）支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EEPROM && CONFIG_NVMEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/nvmem/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/nvmem/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 非易失性存储器（Non Volatile Memory，NVMEM）

**配置项引用（Symbol References）**：[`CONFIG_EEPROM`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM)、[`CONFIG_NVMEM`](P410_subsys_nvmem_配置项参考.md#CONFIG_NVMEM)。

<a id="CONFIG_NVMEM_FLASH"></a>

## 410.4 `CONFIG_NVMEM_FLASH`

**提示（Prompt）**：闪存设备（Flash device）的 NVMEM 读取支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH && CONFIG_NVMEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/nvmem/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/nvmem/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 非易失性存储器（Non Volatile Memory，NVMEM）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_NVMEM`](P410_subsys_nvmem_配置项参考.md#CONFIG_NVMEM)。

<a id="CONFIG_NVMEM_FLASH_WRITE"></a>

## 410.5 `CONFIG_NVMEM_FLASH_WRITE`

**提示（Prompt）**：闪存设备（Flash device）的 NVMEM 写入支持

**说明（Help）**

允许向闪存设备中的 NVMEM 单元（Cell）写入数据。由于闪存写入需要另外执行擦除或考虑写块大小（Write-block size）等，处理并不简单，因此专门提供此显式选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NVMEM_FLASH && CONFIG_NVMEM
```

**定义位置（Location）**：[`subsys/nvmem/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/nvmem/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 非易失性存储器（Non Volatile Memory，NVMEM） → 闪存设备（Flash device）的 NVMEM 读取支持

**配置项引用（Symbol References）**：[`CONFIG_NVMEM_FLASH`](P410_subsys_nvmem_配置项参考.md#CONFIG_NVMEM_FLASH)、[`CONFIG_NVMEM`](P410_subsys_nvmem_配置项参考.md#CONFIG_NVMEM)。

<a id="CONFIG_NVMEM_OTP"></a>

## 410.6 `CONFIG_NVMEM_OTP`

**提示（Prompt）**：一次性可编程存储器（OTP）处理设备的 NVMEM 读取支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OTP && CONFIG_NVMEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/nvmem/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/nvmem/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 非易失性存储器（Non Volatile Memory，NVMEM）

**配置项引用（Symbol References）**：[`CONFIG_OTP`](P133_drivers_otp_配置项参考.md#CONFIG_OTP)、[`CONFIG_NVMEM`](P410_subsys_nvmem_配置项参考.md#CONFIG_NVMEM)。

<a id="CONFIG_NVMEM_OTP_WRITE"></a>

## 410.7 `CONFIG_NVMEM_OTP_WRITE`

**提示（Prompt）**：一次性可编程存储器（OTP）处理设备的 NVMEM 写入支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NVMEM_OTP && CONFIG_OTP_PROGRAM && CONFIG_NVMEM
```

**定义位置（Location）**：[`subsys/nvmem/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/nvmem/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 非易失性存储器（Non Volatile Memory，NVMEM） → 一次性可编程存储器（OTP）处理设备的 NVMEM 读取支持

**配置项引用（Symbol References）**：[`CONFIG_NVMEM_OTP`](P410_subsys_nvmem_配置项参考.md#CONFIG_NVMEM_OTP)、[`CONFIG_OTP_PROGRAM`](P133_drivers_otp_配置项参考.md#CONFIG_OTP_PROGRAM)、[`CONFIG_NVMEM`](P410_subsys_nvmem_配置项参考.md#CONFIG_NVMEM)。

<!-- kconfig-navigation -->

[上一章](P409_subsys_net_配置项参考_19.md) · [返回大纲](大纲.md) · [下一章](P411_subsys_pm_配置项参考.md)
