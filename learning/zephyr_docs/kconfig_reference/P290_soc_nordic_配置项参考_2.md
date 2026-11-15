---
id: learning.zephyr-docs.kconfig-reference.page-290
title: "`soc/nordic`配置项参考（2/3）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第290章\_`soc/nordic`配置项参考（2/3）

本章翻译官方 Kconfig 数据库中 `soc/nordic` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_NRF_APPROTECT_USE_UICR"></a>

## 290.1 `CONFIG_NRF_APPROTECT_USE_UICR`

**提示（Prompt）**：使用 UICR，默认（Use UICR, default）

**说明（Help）**

选择此项时，`SystemInit()` 将 `CTRL-AP.APPROTECT.DISABLE` 设为 `UICR.APPROTECT` 的值。如果 UICR 中禁用了访问端口保护（AP-Protect），则保持禁用；如果 UICR 中启用了 AP-Protect，则保持启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_NRF52 || CONFIG_SOC_SERIES_NRF53 || CONFIG_SOC_SERIES_NRF91) && <choice CONFIG_NRF_APPROTECT_HANDLING>
```

**定义位置（Location）**：[`soc/nordic/Kconfig:140`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/Kconfig#L140)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 访问端口保护处理（AP-Protect handling）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF52`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF52)、[`CONFIG_SOC_SERIES_NRF53`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_SERIES_NRF91`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF91)、[`CONFIG_NRF_APPROTECT_HANDLING`](P289_soc_nordic_配置项参考_1.md#CONFIG_NRF_APPROTECT_HANDLING)。

<a id="CONFIG_NRF_BPROT_FLASH_REGION_SIZE"></a>

## 290.2 `CONFIG_NRF_BPROT_FLASH_REGION_SIZE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF_BPROT 外设（nRF52）的 Flash 区域大小（FLASH region size）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_BPROT && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`soc/nordic/Kconfig:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/Kconfig#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_BPROT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_BPROT)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_BPROT`、`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF_CUSTOM_ON_ENTER_CPU_IDLE_HOOK"></a>

## 290.3 `CONFIG_NRF_CUSTOM_ON_ENTER_CPU_IDLE_HOOK`

**提示（Prompt）**：自定义 CPU 进入空闲状态钩子（on enter CPU idle hook）

**说明（Help）**

选择此项以使用自定义的 CPU 进入空闲状态钩子（on enter CPU idle hook）。启用后，钩子由用户实现。用户有责任在自定义钩子中实现默认版本所包含的 SoC 专用代码。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_ON_ENTER_CPU_IDLE_HOOK && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/Kconfig:234`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/Kconfig#L234)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_ARM_ON_ENTER_CPU_IDLE_HOOK`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_ON_ENTER_CPU_IDLE_HOOK)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF_ENABLE_CACHE"></a>

## 290.4 `CONFIG_NRF_ENABLE_CACHE`

**提示（Prompt）**：缓存（Cache）

**说明（Help）**

nRF5340 应用 MCU（CPUAPP）具有指令缓存和数据缓存（Instruction and Data cache），只能由安全代码（Secure code）访问。nRF5340 网络 MCU（CPUNET）仅具有指令缓存（I-Cache）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
((CONFIG_SOC_NRF5340_CPUAPP && (!CONFIG_TRUSTED_EXECUTION_NONSECURE || CONFIG_BUILD_WITH_TFM)) || CONFIG_SOC_NRF5340_CPUNET) && CONFIG_SOC_SERIES_NRF53 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_BUILD_WITH_TFM
```

**定义位置（Location）**：[`soc/nordic/nrf53/Kconfig:240`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf53/Kconfig#L240)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF5340_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF5340_CPUAPP)、[`CONFIG_TRUSTED_EXECUTION_NONSECURE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRUSTED_EXECUTION_NONSECURE)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_SOC_NRF5340_CPUNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF5340_CPUNET)、[`CONFIG_SOC_SERIES_NRF53`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_NRF5340_CPUAPP`、`CONFIG_SOC_NRF5340_CPUNET`、`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF_ENABLE_ICACHE"></a>

## 290.5 `CONFIG_NRF_ENABLE_ICACHE`

原库同名定义共 2 条；本项为数据库第 13892 条记录，各定义分别保留。

**提示（Prompt）**：指令缓存（The instruction cache，I-Cache）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_NRF52832 || CONFIG_SOC_NRF52833 || CONFIG_SOC_NRF52840) && CONFIG_SOC_SERIES_NRF52 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nordic/nrf52/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf52/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF52832`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF52832)、[`CONFIG_SOC_NRF52833`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF52833)、[`CONFIG_SOC_NRF52840`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF52840)、[`CONFIG_SOC_SERIES_NRF52`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF52)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_NRF52832`、`CONFIG_SOC_NRF52833`、`CONFIG_SOC_NRF52840`、`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF_ENABLE_ICACHE--record-13893"></a>

## 290.6 `CONFIG_NRF_ENABLE_ICACHE`

原库同名定义共 2 条；本项为数据库第 13893 条记录，各定义分别保留。

**提示（Prompt）**：指令缓存（Instruction cache，I-Cache）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NRF91 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nordic/nrf91/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf91/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF91`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF91)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF_FORCE_RAM_ON_REBOOT"></a>

## 290.7 `CONFIG_NRF_FORCE_RAM_ON_REBOOT`

**提示（Prompt）**：重启前强制为所有 RAM 块上电（power on all RAM blocks）

**说明（Help）**

RAM 电源配置会在软复位（soft reset）后保留，因此启动不同应用（例如引导加载程序）时，可能访问已断电的 RAM 块。触发软复位前，强制为所有 RAM 块上电，以避免这种情况。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NORDIC_RAM_CTRL && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NORDIC_RAM_CTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_RAM_CTRL)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NORDIC_RAM_CTRL`、`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF_MPU_FLASH_REGION_SIZE"></a>

## 290.8 `CONFIG_NRF_MPU_FLASH_REGION_SIZE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF_MPU 外设的 Flash 区域大小（FLASH region size）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_MPU && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
0x1000
```

**定义位置（Location）**：[`soc/nordic/Kconfig:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/Kconfig#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_MPU)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_MPU`、`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF_PLATFORM_DEPRECATED_SYMBOLS"></a>

## 290.9 `CONFIG_NRF_PLATFORM_DEPRECATED_SYMBOLS`

**提示（Prompt）**：生成已弃用的 HALTIUM／LUMOS 符号以兼容下游（downstream compatibility）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/Kconfig:246`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/Kconfig#L246)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF_PLATFORM_HALTIUM"></a>

## 290.10 `CONFIG_NRF_PLATFORM_HALTIUM`

**提示（Prompt）**：由 SOC_SERIES_NRF54H／SOC_SERIES_NRF92 替代（Replaced by）［已弃用，DEPRECATED］

**说明（Help）**

此选项已移除，请直接使用 `SOC_SERIES_NRF54H` 或 `SOC_SERIES_NRF92`。暂时保留此符号，使仍引用它的树外代码（out-of-tree code）可以继续构建，同时产生弃用警告（deprecation warning）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_PLATFORM_DEPRECATED_SYMBOLS && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_SERIES_NRF54H || CONFIG_SOC_SERIES_NRF92
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`soc/nordic/Kconfig:249`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/Kconfig#L249)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 生成已弃用的 HALTIUM／LUMOS 符号以兼容下游（downstream compatibility）

**配置项引用（Symbol References）**：[`CONFIG_NRF_PLATFORM_DEPRECATED_SYMBOLS`](P290_soc_nordic_配置项参考_2.md#CONFIG_NRF_PLATFORM_DEPRECATED_SYMBOLS)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_SOC_SERIES_NRF54H`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54H)、[`CONFIG_SOC_SERIES_NRF92`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF92)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF_PLATFORM_LUMOS"></a>

## 290.11 `CONFIG_NRF_PLATFORM_LUMOS`

**提示（Prompt）**：由 SOC_SERIES_NRF54L／SOC_SERIES_NRF71 替代（Replaced by）［已弃用，DEPRECATED］

**说明（Help）**

此选项已移除，请直接使用 `SOC_SERIES_NRF54L` 或 `SOC_SERIES_NRF71`。暂时保留此符号，使仍引用它的树外代码（out-of-tree code）可以继续构建，同时产生弃用警告（deprecation warning）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_PLATFORM_DEPRECATED_SYMBOLS && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_SERIES_NRF54L || CONFIG_SOC_SERIES_NRF71
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`soc/nordic/Kconfig:259`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/Kconfig#L259)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 生成已弃用的 HALTIUM／LUMOS 符号以兼容下游（downstream compatibility）

**配置项引用（Symbol References）**：[`CONFIG_NRF_PLATFORM_DEPRECATED_SYMBOLS`](P290_soc_nordic_配置项参考_2.md#CONFIG_NRF_PLATFORM_DEPRECATED_SYMBOLS)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_SOC_SERIES_NRF54L`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54L)、[`CONFIG_SOC_SERIES_NRF71`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF71)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF_SECURE_APPROTECT_DISABLE"></a>

## 290.12 `CONFIG_NRF_SECURE_APPROTECT_DISABLE`

**提示（Prompt）**：禁用（Disable）

**说明（Help）**

选择此项时，`SystemInit()` 禁用安全访问端口保护机制（Secure AP-Protect），允许调试安全处理环境（Secure Processing Environment，SPE）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_NRF54L_CPUAPP_COMMON && <choice CONFIG_NRF_SECURE_APPROTECT_HANDLING>
```

**定义位置（Location）**：[`soc/nordic/Kconfig:179`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/Kconfig#L179)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 安全访问端口保护处理（Secure AP-Protect handling）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF54L_CPUAPP_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54L_CPUAPP_COMMON)、[`CONFIG_NRF_SECURE_APPROTECT_HANDLING`](P290_soc_nordic_配置项参考_2.md#CONFIG_NRF_SECURE_APPROTECT_HANDLING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_NRF54L_CPUAPP_COMMON`。

<a id="CONFIG_NRF_SECURE_APPROTECT_HANDLING"></a>

## 290.13 `CONFIG_NRF_SECURE_APPROTECT_HANDLING`

**提示（Prompt）**：安全访问端口保护处理（Secure AP-Protect handling）

**说明（Help）**

指定 `SystemInit()` 函数如何处理安全访问端口保护机制（Secure AP-Protect）。支持 ARM TrustZone 及不同处理环境的 SoC 或系统级封装（SiP）提供此机制。此选择不适用于 nRF9160，其 AP-Protect 完全由硬件控制，即由 `UICR.APPROTECT` 寄存器控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_NRF5340_CPUAPP || CONFIG_SOC_NRF54L_CPUAPP_COMMON || CONFIG_SOC_SERIES_NRF91) && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
CONFIG_NRF_SECURE_APPROTECT_DISABLE if CONFIG_SOC_NRF54L_CPUAPP_COMMON
CONFIG_NRF_SECURE_APPROTECT_USE_UICR
```

**可选项（Choices）**

```text
CONFIG_NRF_SECURE_APPROTECT_DISABLE
CONFIG_NRF_SECURE_APPROTECT_USE_UICR
CONFIG_NRF_SECURE_APPROTECT_LOCK
CONFIG_NRF_SECURE_APPROTECT_USER_HANDLING
```

**定义位置（Location）**：[`soc/nordic/Kconfig:167`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/Kconfig#L167)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF5340_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF5340_CPUAPP)、[`CONFIG_SOC_NRF54L_CPUAPP_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54L_CPUAPP_COMMON)、[`CONFIG_SOC_SERIES_NRF91`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF91)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_NRF_SECURE_APPROTECT_DISABLE`](P290_soc_nordic_配置项参考_2.md#CONFIG_NRF_SECURE_APPROTECT_DISABLE)、[`CONFIG_NRF_SECURE_APPROTECT_USE_UICR`](P290_soc_nordic_配置项参考_2.md#CONFIG_NRF_SECURE_APPROTECT_USE_UICR)、[`CONFIG_NRF_SECURE_APPROTECT_LOCK`](P290_soc_nordic_配置项参考_2.md#CONFIG_NRF_SECURE_APPROTECT_LOCK)、[`CONFIG_NRF_SECURE_APPROTECT_USER_HANDLING`](P290_soc_nordic_配置项参考_2.md#CONFIG_NRF_SECURE_APPROTECT_USER_HANDLING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_NRF5340_CPUAPP`、`CONFIG_SOC_NRF54L_CPUAPP_COMMON`、`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF_SECURE_APPROTECT_LOCK"></a>

## 290.14 `CONFIG_NRF_SECURE_APPROTECT_LOCK`

**提示（Prompt）**：锁定（Lock）

**说明（Help）**

选择此项时，`SystemInit()` 锁定安全访问端口保护机制（Secure AP-Protect），使调试器持续无法访问安全处理环境（SPE）。只有通过控制访问端口（CTRL-AP）执行 ERASEALL 全部擦除操作，才能恢复对 SPE 的访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRF_SECURE_APPROTECT_HANDLING>
```

**定义位置（Location）**：[`soc/nordic/Kconfig:198`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/Kconfig#L198)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 安全访问端口保护处理（Secure AP-Protect handling）

**配置项引用（Symbol References）**：[`CONFIG_NRF_SECURE_APPROTECT_HANDLING`](P290_soc_nordic_配置项参考_2.md#CONFIG_NRF_SECURE_APPROTECT_HANDLING)。

<a id="CONFIG_NRF_SECURE_APPROTECT_USER_HANDLING"></a>

## 290.15 `CONFIG_NRF_SECURE_APPROTECT_USER_HANDLING`

**提示（Prompt）**：允许用户处理（Allow user handling）

**说明（Help）**

选择此项时，`SystemInit()` 不触碰安全访问端口保护机制（Secure AP-Protect）。用户代码可以在后续阶段处理它，例如实现对安全处理环境（SPE）的认证调试（authenticated debug）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_SOC_SERIES_NRF52 && <choice CONFIG_NRF_SECURE_APPROTECT_HANDLING>
```

**定义位置（Location）**：[`soc/nordic/Kconfig:206`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/Kconfig#L206)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 安全访问端口保护处理（Secure AP-Protect handling）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF52`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF52)、[`CONFIG_NRF_SECURE_APPROTECT_HANDLING`](P290_soc_nordic_配置项参考_2.md#CONFIG_NRF_SECURE_APPROTECT_HANDLING)。

<a id="CONFIG_NRF_SECURE_APPROTECT_USE_UICR"></a>

## 290.16 `CONFIG_NRF_SECURE_APPROTECT_USE_UICR`

**提示（Prompt）**：使用 UICR，默认（Use UICR, default）

**说明（Help）**

选择此项时，`SystemInit()` 将 `CTRL-AP.SECUREAPPROTECT.DISABLE` 设为 `UICR.SECUREAPPROTECT` 的值。如果 UICR 中禁用了安全访问端口保护（Secure AP-Protect），则保持禁用；如果 UICR 中启用了它，则保持启用，并阻止访问安全处理环境（SPE）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_NRF5340_CPUAPP || CONFIG_SOC_SERIES_NRF91) && <choice CONFIG_NRF_SECURE_APPROTECT_HANDLING>
```

**定义位置（Location）**：[`soc/nordic/Kconfig:187`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/Kconfig#L187)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 安全访问端口保护处理（Secure AP-Protect handling）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF5340_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF5340_CPUAPP)、[`CONFIG_SOC_SERIES_NRF91`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF91)、[`CONFIG_NRF_SECURE_APPROTECT_HANDLING`](P290_soc_nordic_配置项参考_2.md#CONFIG_NRF_SECURE_APPROTECT_HANDLING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_NRF5340_CPUAPP`。

<a id="CONFIG_NRF_SKIP_CLOCK_CONFIG"></a>

## 290.17 `CONFIG_NRF_SKIP_CLOCK_CONFIG`

**提示（Prompt）**：跳过时钟频率配置（Skip clock frequency configuration）

**说明（Help）**

使用此项时，系统初始化期间不设置 CPU 时钟频率。CPU 以硬件选择的默认频率运行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_NRF54L || CONFIG_SOC_SERIES_NRF71) && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y if CONFIG_TRUSTED_EXECUTION_NONSECURE
```

**定义位置（Location）**：[`soc/nordic/Kconfig:217`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/Kconfig#L217)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF54L`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54L)、[`CONFIG_SOC_SERIES_NRF71`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF71)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_TRUSTED_EXECUTION_NONSECURE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRUSTED_EXECUTION_NONSECURE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF_SOC_SECURE_SUPPORTED"></a>

## 290.18 `CONFIG_NRF_SOC_SECURE_SUPPORTED`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏功能，用于表示 `soc_secure` 函数可用。当构建不属于非安全构建时，这些函数始终可用；对于非安全构建（non-secure），这些函数必须重定向到安全固件公开的安全服务（secure services）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_SOC_SERIES_NRF54H && !CONFIG_SOC_SERIES_NRF92 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
!CONFIG_TRUSTED_EXECUTION_NONSECURE || (CONFIG_BUILD_WITH_TFM && CONFIG_TFM_PARTITION_PLATFORM)
```

**定义位置（Location）**：[`soc/nordic/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF54H`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54H)、[`CONFIG_SOC_SERIES_NRF92`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF92)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_TRUSTED_EXECUTION_NONSECURE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRUSTED_EXECUTION_NONSECURE)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_TFM_PARTITION_PLATFORM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_PLATFORM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF_SPU_FLASH_REGION_SIZE"></a>

## 290.19 `CONFIG_NRF_SPU_FLASH_REGION_SIZE`

原库同名定义共 2 条；本项为数据库第 13943 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF_SPU 外设的 Flash 区域大小（FLASH region size）

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_NRF5340_CPUAPP && CONFIG_SOC_SERIES_NRF53 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
0x4000
```

**定义位置（Location）**：[`soc/nordic/nrf53/Kconfig:134`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf53/Kconfig#L134)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF5340_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF5340_CPUAPP)、[`CONFIG_SOC_SERIES_NRF53`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_NRF5340_CPUAPP`、`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF_SPU_FLASH_REGION_SIZE--record-13944"></a>

## 290.20 `CONFIG_NRF_SPU_FLASH_REGION_SIZE`

原库同名定义共 2 条；本项为数据库第 13944 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF_SPU 外设的 Flash 区域大小（FLASH region size）

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NRF91 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
0x8000
```

**定义位置（Location）**：[`soc/nordic/nrf91/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf91/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF91`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF91)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF_SPU_RAM_REGION_SIZE"></a>

## 290.21 `CONFIG_NRF_SPU_RAM_REGION_SIZE`

原库同名定义共 2 条；本项为数据库第 13945 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF_SPU 外设的 RAM 区域大小（RAM region size）

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_NRF5340_CPUAPP && CONFIG_SOC_SERIES_NRF53 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
0x2000
```

**定义位置（Location）**：[`soc/nordic/nrf53/Kconfig:140`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf53/Kconfig#L140)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF5340_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF5340_CPUAPP)、[`CONFIG_SOC_SERIES_NRF53`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_NRF5340_CPUAPP`、`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF_SPU_RAM_REGION_SIZE--record-13946"></a>

## 290.22 `CONFIG_NRF_SPU_RAM_REGION_SIZE`

原库同名定义共 2 条；本项为数据库第 13946 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF_SPU 外设的 RAM 区域大小（RAM region size）

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NRF91 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
0x2000
```

**定义位置（Location）**：[`soc/nordic/nrf91/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf91/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF91`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF91)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF_SYS_EVENT"></a>

## 290.23 `CONFIG_NRF_SYS_EVENT`

**提示（Prompt）**：nRF 系统事件支持（system event support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_NORDIC_NRF
```

**主动选择（Selects）**

```text
CONFIG_NRFX_POWER if !CONFIG_SOC_SERIES_NRF54H && !CONFIG_SOC_SERIES_NRF92
```

**被选择（Selected by）**

```text
CONFIG_NRF_802154_CONSTLAT_CONTROL
CONFIG_NRF_802154_CONSTLAT_CONTROL
```

**定义位置（Location）**：[`soc/nordic/common/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_NRFX_POWER`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_POWER)、[`CONFIG_SOC_SERIES_NRF54H`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54H)、[`CONFIG_SOC_SERIES_NRF92`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF92)、[`CONFIG_NRF_802154_CONSTLAT_CONTROL`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_CONSTLAT_CONTROL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF_SYS_EVENT_GRTC_CHAN_CNT"></a>

## 290.24 `CONFIG_NRF_SYS_EVENT_GRTC_CHAN_CNT`

**提示（Prompt）**：用于唤醒电阻式 RAM 控制器的 GRTC 通道（RRAMC wake up）

**说明（Help）**

专用于唤醒电阻式 RAM 控制器（RRAMC）的全局实时时钟（GRTC）通道最大数量；通过 GRTC 比较通道与 RRAMC 唤醒任务之间的分布式可编程外设互连（DPPI）连接实现唤醒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_HAS_HW_NRF_MRAMC && CONFIG_NRF_SYS_EVENT_IRQ_LATENCY && CONFIG_NRF_SYS_EVENT && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[0, 16]
```

**定义位置（Location）**：[`soc/nordic/common/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → nRF 系统事件支持（system event support） → 注册事件以降低中断处理延迟（interrupt handling latency）

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_MRAMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_MRAMC)、[`CONFIG_NRF_SYS_EVENT_IRQ_LATENCY`](P290_soc_nordic_配置项参考_2.md#CONFIG_NRF_SYS_EVENT_IRQ_LATENCY)、[`CONFIG_NRF_SYS_EVENT`](P290_soc_nordic_配置项参考_2.md#CONFIG_NRF_SYS_EVENT)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_MRAMC`、`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF_SYS_EVENT_IRQ_LATENCY"></a>

## 290.25 `CONFIG_NRF_SYS_EVENT_IRQ_LATENCY`

**提示（Prompt）**：注册事件以降低中断处理延迟（interrupt handling latency）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_HAS_HW_NRF_RRAMC || CONFIG_HAS_HW_NRF_MRAMC) && !CONFIG_TRUSTED_EXECUTION_NONSECURE && CONFIG_NRF_SYS_EVENT && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nordic/common/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → nRF 系统事件支持（system event support）

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_RRAMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_RRAMC)、[`CONFIG_HAS_HW_NRF_MRAMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_MRAMC)、[`CONFIG_TRUSTED_EXECUTION_NONSECURE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRUSTED_EXECUTION_NONSECURE)、[`CONFIG_NRF_SYS_EVENT`](P290_soc_nordic_配置项参考_2.md#CONFIG_NRF_SYS_EVENT)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_RRAMC`、`CONFIG_HAS_HW_NRF_MRAMC`、`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF_SYS_EVENT_IRQ_LATENCY_MANUAL"></a>

## 290.26 `CONFIG_NRF_SYS_EVENT_IRQ_LATENCY_MANUAL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用后，表示可以手动控制非易失存储器（NVM）的电源模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_SYS_EVENT_IRQ_LATENCY && CONFIG_NRF_SYS_EVENT && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
!CONFIG_RISCV
```

**定义位置（Location）**：[`soc/nordic/common/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → nRF 系统事件支持（system event support） → 注册事件以降低中断处理延迟（interrupt handling latency）

**配置项引用（Symbol References）**：[`CONFIG_NRF_SYS_EVENT_IRQ_LATENCY`](P290_soc_nordic_配置项参考_2.md#CONFIG_NRF_SYS_EVENT_IRQ_LATENCY)、[`CONFIG_NRF_SYS_EVENT`](P290_soc_nordic_配置项参考_2.md#CONFIG_NRF_SYS_EVENT)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF_TRACE_PORT"></a>

## 290.27 `CONFIG_NRF_TRACE_PORT`

**提示（Prompt）**：nRF 跟踪端口接口单元（TPIU）

**说明（Help）**

启用此项以初始化跟踪端口接口单元（Trace Port Interface Unit，TPIU），使用硬件探针（hardware probe）进行跟踪。禁用时，跟踪引脚将用作 GPIO。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_SOC_SERIES_NRF51 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/Kconfig:226`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/Kconfig#L226)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF51`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF51)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF_TRUSTZONE_FLASH_REGION_SIZE"></a>

## 290.28 `CONFIG_NRF_TRUSTZONE_FLASH_REGION_SIZE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

从 TrustZone 的角度定义 Flash 区域大小（region size）。用于配置 TrustZone 和设置分区对齐要求（alignment requirements）。此抽象使得配置 TrustZone 时无需依赖特定外设的符号。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM && (CONFIG_SOC_SERIES_NRF54L || CONFIG_SOC_SERIES_NRF71 || CONFIG_SOC_SERIES_NRF53 || CONFIG_SOC_SERIES_NRF91) && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
CONFIG_NRF_SPU_FLASH_REGION_SIZE if CONFIG_SOC_SERIES_NRF53 || CONFIG_SOC_SERIES_NRF91
0
```

**定义位置（Location）**：[`soc/nordic/common/Kconfig.tfm:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/Kconfig.tfm#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_SOC_SERIES_NRF54L`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54L)、[`CONFIG_SOC_SERIES_NRF71`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF71)、[`CONFIG_SOC_SERIES_NRF53`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_SERIES_NRF91`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF91)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_NRF_SPU_FLASH_REGION_SIZE`](P290_soc_nordic_配置项参考_2.md#CONFIG_NRF_SPU_FLASH_REGION_SIZE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_NRF_TRUSTZONE_RAM_REGION_SIZE"></a>

## 290.29 `CONFIG_NRF_TRUSTZONE_RAM_REGION_SIZE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

从 TrustZone 的角度定义 RAM 区域大小（region size）。用于配置 TrustZone 和设置分区对齐要求（alignment requirements）。此抽象使得配置 TrustZone 时无需依赖特定外设的符号。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM && (CONFIG_SOC_SERIES_NRF54L || CONFIG_SOC_SERIES_NRF71 || CONFIG_SOC_SERIES_NRF53 || CONFIG_SOC_SERIES_NRF91) && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
CONFIG_NRF_SPU_RAM_REGION_SIZE if CONFIG_SOC_SERIES_NRF53 || CONFIG_SOC_SERIES_NRF91
0
```

**定义位置（Location）**：[`soc/nordic/common/Kconfig.tfm:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/Kconfig.tfm#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_SOC_SERIES_NRF54L`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54L)、[`CONFIG_SOC_SERIES_NRF71`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF71)、[`CONFIG_SOC_SERIES_NRF53`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_SERIES_NRF91`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF91)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_NRF_SPU_RAM_REGION_SIZE`](P290_soc_nordic_配置项参考_2.md#CONFIG_NRF_SPU_RAM_REGION_SIZE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_RISCV_CORE_NORDIC_VPR"></a>

## 290.30 `CONFIG_RISCV_CORE_NORDIC_VPR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RISC-V Nordic VPR 内核支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_NORDIC_NRF
```

**主动选择（Selects）**

```text
CONFIG_RISCV
CONFIG_RISCV_PRIVILEGED
CONFIG_RISCV_VECTORED_MODE
CONFIG_RISCV_SOC_HAS_ISR_STACKING
CONFIG_RISCV_SOC_HAS_GP_RELATIVE_ADDRESSING
CONFIG_RISCV_HAS_CLIC
CONFIG_RISCV_SOC_CONTEXT_SAVE
CONFIG_HAS_FLASH_LOAD_OFFSET
CONFIG_ARCH_HAS_CUSTOM_CPU_IDLE
CONFIG_ARCH_HAS_CUSTOM_CPU_ATOMIC_IDLE
CONFIG_INCLUDE_RESET_VECTOR
```

**被选择（Selected by）**

```text
CONFIG_SOC_NRF54H20_CPUPPR
CONFIG_SOC_NRF54H20_CPUFLPR
CONFIG_SOC_NRF54L05_CPUFLPR
CONFIG_SOC_NRF54L10_CPUFLPR
CONFIG_SOC_NRF54L15_CPUFLPR
CONFIG_SOC_NRF54LM20A_CPUFLPR
CONFIG_SOC_NRF54LM20B_CPUFLPR
CONFIG_SOC_NRF54LV10A_CPUFLPR
CONFIG_SOC_NRF7120_ENGA_CPUFLPR
CONFIG_SOC_NRF7120E_ENGA_CPUFLPR
CONFIG_SOC_NRF9230_ENGB_CPUPPR
```

**弱选择（Implies）**

```text
CONFIG_XIP
CONFIG_SHELL_REMOTE_CLI_SKIP_RO_STRINGS
```

**定义位置（Location）**：[`soc/nordic/common/vpr/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/vpr/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_RISCV_PRIVILEGED`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_PRIVILEGED)、[`CONFIG_RISCV_VECTORED_MODE`](P270_soc_common_配置项参考.md#CONFIG_RISCV_VECTORED_MODE)、[`CONFIG_RISCV_SOC_HAS_ISR_STACKING`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_SOC_HAS_ISR_STACKING)、[`CONFIG_RISCV_SOC_HAS_GP_RELATIVE_ADDRESSING`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_SOC_HAS_GP_RELATIVE_ADDRESSING)、[`CONFIG_RISCV_HAS_CLIC`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_HAS_CLIC)、[`CONFIG_RISCV_SOC_CONTEXT_SAVE`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_SOC_CONTEXT_SAVE)、[`CONFIG_HAS_FLASH_LOAD_OFFSET`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_HAS_FLASH_LOAD_OFFSET)、[`CONFIG_ARCH_HAS_CUSTOM_CPU_IDLE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_CUSTOM_CPU_IDLE)、[`CONFIG_ARCH_HAS_CUSTOM_CPU_ATOMIC_IDLE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_CUSTOM_CPU_ATOMIC_IDLE)、[`CONFIG_INCLUDE_RESET_VECTOR`](P034_arch_riscv_配置项参考_1.md#CONFIG_INCLUDE_RESET_VECTOR)、[`CONFIG_SOC_NRF54H20_CPUPPR`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54H20_CPUPPR)、[`CONFIG_SOC_NRF54H20_CPUFLPR`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54H20_CPUFLPR)、[`CONFIG_SOC_NRF54L05_CPUFLPR`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54L05_CPUFLPR)、[`CONFIG_SOC_NRF54L10_CPUFLPR`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54L10_CPUFLPR)、[`CONFIG_SOC_NRF54L15_CPUFLPR`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54L15_CPUFLPR)、[`CONFIG_SOC_NRF54LM20A_CPUFLPR`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54LM20A_CPUFLPR)、[`CONFIG_SOC_NRF54LM20B_CPUFLPR`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54LM20B_CPUFLPR)、[`CONFIG_SOC_NRF54LV10A_CPUFLPR`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54LV10A_CPUFLPR)、[`CONFIG_SOC_NRF7120_ENGA_CPUFLPR`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF7120_ENGA_CPUFLPR)、[`CONFIG_SOC_NRF7120E_ENGA_CPUFLPR`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF7120E_ENGA_CPUFLPR)、[`CONFIG_SOC_NRF9230_ENGB_CPUPPR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9230_ENGB_CPUPPR)、[`CONFIG_XIP`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XIP)、[`CONFIG_SHELL_REMOTE_CLI_SKIP_RO_STRINGS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_REMOTE_CLI_SKIP_RO_STRINGS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`、`CONFIG_SOC_NRF9230_ENGB_CPUPPR`。

<a id="CONFIG_SHELL_REMOTE_FLPR"></a>

## 290.31 `CONFIG_SHELL_REMOTE_FLPR`

**提示（Prompt）**：FLPR 的远程命令解释器（Remote Shell）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`soc/nordic/common/Kconfig:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/Kconfig#L127)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

<a id="CONFIG_SHELL_REMOTE_PPR"></a>

## 290.32 `CONFIG_SHELL_REMOTE_PPR`

**提示（Prompt）**：PPR 的远程命令解释器（Remote Shell）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`soc/nordic/common/Kconfig:123`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/Kconfig#L123)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

<a id="CONFIG_SHELL_REMOTE_RADIO"></a>

## 290.33 `CONFIG_SHELL_REMOTE_RADIO`

**提示（Prompt）**：无线电内核的远程命令解释器（Remote Shell for Radio core）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_NRF54H20_CPUAPP && CONFIG_SHELL_REMOTE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/Kconfig:131`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/Kconfig#L131)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF54H20_CPUAPP`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54H20_CPUAPP)、[`CONFIG_SHELL_REMOTE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_REMOTE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_HFXO_CAP_DEFAULT"></a>

## 290.34 `CONFIG_SOC_HFXO_CAP_DEFAULT`

**提示（Prompt）**：SoC 默认值（SoC default）

**说明（Help）**

此选项已弃用（deprecated），请改用设备树（DT）。要应用此配置，无需修改 SoC 设备树文件的默认值。使用此选项时，SoC 初始化例程不会改动 `XOSC32MCAPS` 寄存器值，因此采用 SoC 默认设置。注意，这未必是寄存器的复位值 0，因为 `SystemInit()` 函数在器件修调（device trimming）期间可能设置该寄存器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SOC_HFXO_LOAD_CAPACITANCE>
```

**定义位置（Location）**：[`soc/nordic/nrf53/Kconfig:180`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf53/Kconfig#L180)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 高频晶体振荡器负载电容（HFXO load capacitance）

**配置项引用（Symbol References）**：[`CONFIG_SOC_HFXO_LOAD_CAPACITANCE`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_HFXO_LOAD_CAPACITANCE)。

<a id="CONFIG_SOC_HFXO_CAP_EXTERNAL"></a>

## 290.35 `CONFIG_SOC_HFXO_CAP_EXTERNAL`

**提示（Prompt）**：使用外部负载电容（external load capacitors）

**说明（Help）**

此选项已弃用（deprecated），请改用设备树（DT）。示例配置：

```dts
&hfxo {
    load-capacitors = "external";
};
```

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SOC_HFXO_LOAD_CAPACITANCE>
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`soc/nordic/nrf53/Kconfig:192`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf53/Kconfig#L192)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 高频晶体振荡器负载电容（HFXO load capacitance）

**配置项引用（Symbol References）**：[`CONFIG_SOC_HFXO_LOAD_CAPACITANCE`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_HFXO_LOAD_CAPACITANCE)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_SOC_HFXO_CAP_INTERNAL"></a>

## 290.36 `CONFIG_SOC_HFXO_CAP_INTERNAL`

**提示（Prompt）**：使用内部负载电容（internal load capacitors）

**说明（Help）**

此选项已弃用（deprecated），请改用设备树（DT）。示例配置：

```dts
&hfxo {
    load-capacitors = "internal";
    ...
};
```

更多信息请参阅 `CONFIG_SOC_HFXO_CAP_INT_VALUE_X2`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_SOC_SECURE_SUPPORTED && <choice CONFIG_SOC_HFXO_LOAD_CAPACITANCE>
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`soc/nordic/nrf53/Kconfig:202`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf53/Kconfig#L202)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 高频晶体振荡器负载电容（HFXO load capacitance）

**配置项引用（Symbol References）**：[`CONFIG_NRF_SOC_SECURE_SUPPORTED`](P290_soc_nordic_配置项参考_2.md#CONFIG_NRF_SOC_SECURE_SUPPORTED)、[`CONFIG_SOC_HFXO_LOAD_CAPACITANCE`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_HFXO_LOAD_CAPACITANCE)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_SOC_HFXO_CAP_INT_VALUE_X2"></a>

## 290.37 `CONFIG_SOC_HFXO_CAP_INT_VALUE_X2`

**提示（Prompt）**：高频晶体振荡器内部负载电容的两倍值，单位为 pF（Doubled HFXO capacitance）

**说明（Help）**

此选项已弃用（deprecated），请改用设备树（DT）。示例配置：

```dts
&hfxo {
    load-capacitors = "internal";
    load-capacitance-femtofarad = <7000>;
};
```

可在 XC1 和 XC2 引脚上启用 7.0 pF～20.0 pF、步长为 0.5 pF 的内部电容。此选项指定两个电容各自电容值的两倍：设为 14，每个电容为 7.0 pF；设为 15，则为 7.5 pF，依此类推。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_HFXO_CAP_INTERNAL && (!CONFIG_TRUSTED_EXECUTION_NONSECURE || CONFIG_BUILD_WITH_TFM) && CONFIG_SOC_NRF5340_CPUAPP && CONFIG_SOC_SERIES_NRF53 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**取值范围（Ranges）**

```text
[14, 40]
```

**定义位置（Location）**：[`soc/nordic/nrf53/Kconfig:218`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf53/Kconfig#L218)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_HFXO_CAP_INTERNAL`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_HFXO_CAP_INTERNAL)、[`CONFIG_TRUSTED_EXECUTION_NONSECURE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRUSTED_EXECUTION_NONSECURE)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_SOC_NRF5340_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF5340_CPUAPP)、[`CONFIG_SOC_SERIES_NRF53`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_NRF5340_CPUAPP`、`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_HFXO_LOAD_CAPACITANCE"></a>

## 290.38 `CONFIG_SOC_HFXO_LOAD_CAPACITANCE`

**提示（Prompt）**：高频晶体振荡器负载电容（HFXO load capacitance）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(!CONFIG_TRUSTED_EXECUTION_NONSECURE || CONFIG_BUILD_WITH_TFM) && CONFIG_SOC_NRF5340_CPUAPP && CONFIG_SOC_SERIES_NRF53 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
CONFIG_SOC_HFXO_CAP_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_SOC_HFXO_CAP_DEFAULT
CONFIG_SOC_HFXO_CAP_EXTERNAL
CONFIG_SOC_HFXO_CAP_INTERNAL
```

**定义位置（Location）**：[`soc/nordic/nrf53/Kconfig:176`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf53/Kconfig#L176)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_TRUSTED_EXECUTION_NONSECURE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRUSTED_EXECUTION_NONSECURE)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_SOC_NRF5340_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF5340_CPUAPP)、[`CONFIG_SOC_SERIES_NRF53`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_SOC_HFXO_CAP_DEFAULT`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_HFXO_CAP_DEFAULT)、[`CONFIG_SOC_HFXO_CAP_EXTERNAL`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_HFXO_CAP_EXTERNAL)、[`CONFIG_SOC_HFXO_CAP_INTERNAL`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_HFXO_CAP_INTERNAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_NRF5340_CPUAPP`、`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_NRF53_ANOMALY_160_WORKAROUND_NEEDED"></a>

## 290.39 `CONFIG_SOC_NRF53_ANOMALY_160_WORKAROUND_NEEDED`

**提示（Prompt）**：nRF5340 异常 160 的规避措施（anomaly 160 workaround）

**说明（Help）**

表示应应用影响 nRF5340 SoC 的异常 160 规避措施（workaround）。对于应用 MCU，当 VREGMAIN 或 VREGRADIO 稳压器启用 DC/DC 模式时，此项默认启用；对于网络 MCU，始终默认启用。如果此项已启用，但因系统时钟被禁用而无法应用规避措施，会发出相关 CMake 警告。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NRF53 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y if "0" = 1
y if "0" = 1
```

**弱选择（Implies）**

```text
CONFIG_SOC_NRF53_ANOMALY_160_WORKAROUND
```

**被弱选择（Implied by）**

```text
CONFIG_SOC_NRF5340_CPUNET
```

**定义位置（Location）**：[`soc/nordic/nrf53/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf53/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF53`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_SOC_NRF53_ANOMALY_160_WORKAROUND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF53_ANOMALY_160_WORKAROUND)、[`CONFIG_SOC_NRF5340_CPUNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF5340_CPUNET)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`、`CONFIG_SOC_NRF53_ANOMALY_160_WORKAROUND`、`CONFIG_SOC_NRF5340_CPUNET`。

<a id="CONFIG_SOC_NRF53_ANOMALY_166_WORKAROUND"></a>

## 290.40 `CONFIG_SOC_NRF53_ANOMALY_166_WORKAROUND`

**提示（Prompt）**：nRF5340 异常 166 的规避措施（anomaly 166 workaround）

**说明（Help）**

表示应应用影响 nRF5340 SoC 的异常 166 规避措施（workaround）。此措施仅适用于应用内核，以及处于低压差稳压器模式（LDO mode）的 VREGMAIN。由于会明显增加功耗，默认禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
"0" = 0 && CONFIG_SOC_NRF5340_CPUAPP && CONFIG_SOC_SERIES_NRF53 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/nrf53/Kconfig:125`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf53/Kconfig#L125)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF5340_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF5340_CPUAPP)、[`CONFIG_SOC_SERIES_NRF53`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_NRF5340_CPUAPP`、`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_NRF53_ANOMALY_168_WORKAROUND"></a>

## 290.41 `CONFIG_SOC_NRF53_ANOMALY_168_WORKAROUND`

**提示（Prompt）**：nRF5340 异常 168 的规避措施（anomaly 168 workaround）

**说明（Help）**

表示应应用影响 nRF5340 SoC 的异常 168 规避措施（workaround）。此措施是在 CPU 退出空闲状态时（WFI／WFE 指令返回时）执行 8 条空操作指令（NOP），默认对应用内核和网络内核都启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NRF53 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**主动选择（Selects）**

```text
CONFIG_ARM_ON_EXIT_CPU_IDLE
```

**被弱选择（Implied by）**

```text
CONFIG_SOC_NRF5340_CPUAPP
CONFIG_SOC_NRF5340_CPUNET
```

**定义位置（Location）**：[`soc/nordic/nrf53/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf53/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF53`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_ARM_ON_EXIT_CPU_IDLE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_ON_EXIT_CPU_IDLE)、[`CONFIG_SOC_NRF5340_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF5340_CPUAPP)、[`CONFIG_SOC_NRF5340_CPUNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF5340_CPUNET)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`、`CONFIG_SOC_NRF5340_CPUAPP`、`CONFIG_SOC_NRF5340_CPUNET`。

<a id="CONFIG_SOC_NRF53_ANOMALY_168_WORKAROUND_FOR_EXECUTION_FROM_RAM"></a>

## 290.42 `CONFIG_SOC_NRF53_ANOMALY_168_WORKAROUND_FOR_EXECUTION_FROM_RAM`

**提示（Prompt）**：将规避措施扩展到从 RAM 以 128 MHz 执行的情况

**说明（Help）**

表示异常 168 的规避措施（workaround）还应覆盖一种特定情况：WFI／WFE 指令从 RAM 中以 128 MHz 执行。此时，WFI／WFE 之后需要执行 26 条空操作指令（NOP），而非 8 条。默认不启用此扩展。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_NRF53_ANOMALY_168_WORKAROUND && CONFIG_SOC_NRF5340_CPUAPP && CONFIG_SOC_SERIES_NRF53 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/nrf53/Kconfig:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf53/Kconfig#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → nRF5340 异常 168 的规避措施（anomaly 168 workaround）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF53_ANOMALY_168_WORKAROUND`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF53_ANOMALY_168_WORKAROUND)、[`CONFIG_SOC_NRF5340_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF5340_CPUAPP)、[`CONFIG_SOC_SERIES_NRF53`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_NRF5340_CPUAPP`、`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_NRF53_ANOMALY_47_WORKAROUND"></a>

## 290.43 `CONFIG_SOC_NRF53_ANOMALY_47_WORKAROUND`

**提示（Prompt）**：异常 47 规避措施（Anomaly 47 workaround）

**说明（Help）**

由于异常 47（Anomaly 47），在 400 kHz 下 SCL 时钟的低电平持续时间过短，无法满足 I2C 规范。此规避措施将 I2C 频率改为 390 kHz，而非 400 kHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_TWIM && CONFIG_SOC_SERIES_NRF53 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/nrf53/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf53/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_TWIM`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRFX_TWIM)、[`CONFIG_SOC_SERIES_NRF53`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_NRF53_CPUNET_ENABLE"></a>

## 290.44 `CONFIG_SOC_NRF53_CPUNET_ENABLE`

**提示（Prompt）**：启动时启用 NRF53 网络 MCU（Network MCU）

**说明（Help）**

此选项允许释放网络侧“强制关闭”（force off）信号，从而在系统启动期间为网络 MCU 上电。此外，此选项会分配网络 MCU 的带 EasyDMA UART（UARTE）所用的 GPIO 引脚。

注意：只有安全应用 MCU 固件（secure Application MCU firmware）能够配置 GPIO 引脚分配。因此，在开发板非安全版本中使用此选项时，应用必须考虑到：安全固件镜像必须已经为网络 MCU 配置好 GPIO 分配。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_NRF5340_CPUAPP && CONFIG_SOC_SERIES_NRF53 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y if CONFIG_NRF_802154_SER_HOST
```

**主动选择（Selects）**

```text
CONFIG_SOC_NRF53_CPUNET_MGMT
```

**定义位置（Location）**：[`soc/nordic/nrf53/Kconfig:159`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf53/Kconfig#L159)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF5340_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF5340_CPUAPP)、[`CONFIG_SOC_SERIES_NRF53`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_NRF_802154_SER_HOST`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SER_HOST)、[`CONFIG_SOC_NRF53_CPUNET_MGMT`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF53_CPUNET_MGMT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_NRF5340_CPUAPP`、`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_NRF53_CPUNET_MGMT"></a>

## 290.45 `CONFIG_SOC_NRF53_CPUNET_MGMT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

用于包含 nRF53 网络 CPU 管理（network CPU management）的隐藏选项

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_NRF5340_CPUAPP && CONFIG_SOC_SERIES_NRF53 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**主动选择（Selects）**

```text
CONFIG_ONOFF
```

**被选择（Selected by）**

```text
CONFIG_SOC_NRF5340_CPUAPP
CONFIG_SOC_NRF53_CPUNET_ENABLE
```

**定义位置（Location）**：[`soc/nordic/nrf53/Kconfig:153`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf53/Kconfig#L153)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF5340_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF5340_CPUAPP)、[`CONFIG_SOC_SERIES_NRF53`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_ONOFF`](P198_lib_配置项参考_2.md#CONFIG_ONOFF)、[`CONFIG_SOC_NRF53_CPUNET_ENABLE`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF53_CPUNET_ENABLE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_NRF5340_CPUAPP`、`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_NRF53_RTC_PRETICK"></a>

## 290.46 `CONFIG_SOC_NRF53_RTC_PRETICK`

**提示（Prompt）**：nRF5340 异常 165 的预节拍规避措施（Pre-tick workaround）

**说明（Help）**

表示应应用影响 nRF5340 SoC 的异常 165 预节拍规避措施（pre-tick workaround）。此措施适用于 RTC0、RTC1 的 `EVENTS_COMPARE` 和 `EVENTS_OVRFLW` 引起的唤醒，且相应中断已通过 `INTENSET` 寄存器启用。不处理仅由 `EVTEN` 生成这些事件、而未通过 `INTENSET` 启用中断的情况，也不处理 `EVENTS_TICK` 事件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
((CONFIG_SYS_CLOCK_EXISTS && CONFIG_SOC_NRF5340_CPUNET) || CONFIG_SOC_NRF5340_CPUAPP) && CONFIG_SOC_SERIES_NRF53 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**主动选择（Selects）**

```text
CONFIG_NRFX_GPPI
CONFIG_ARM_ON_ENTER_CPU_IDLE_HOOK if CONFIG_SOC_NRF5340_CPUNET
CONFIG_ARM_ON_ENTER_CPU_IDLE_PREPARE_HOOK if CONFIG_SOC_NRF5340_CPUNET
```

**被弱选择（Implied by）**

```text
CONFIG_SOC_NRF5340_CPUAPP
CONFIG_SOC_NRF5340_CPUNET
```

**定义位置（Location）**：[`soc/nordic/nrf53/Kconfig:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf53/Kconfig#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_SOC_NRF5340_CPUNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF5340_CPUNET)、[`CONFIG_SOC_NRF5340_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF5340_CPUAPP)、[`CONFIG_SOC_SERIES_NRF53`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_NRFX_GPPI`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_GPPI)、[`CONFIG_ARM_ON_ENTER_CPU_IDLE_HOOK`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_ON_ENTER_CPU_IDLE_HOOK)、[`CONFIG_ARM_ON_ENTER_CPU_IDLE_PREPARE_HOOK`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_ON_ENTER_CPU_IDLE_PREPARE_HOOK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_NRF5340_CPUNET`、`CONFIG_SOC_NRF5340_CPUAPP`、`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_NRF53_RTC_PRETICK_IPC_CH_FROM_NET"></a>

## 290.47 `CONFIG_SOC_NRF53_RTC_PRETICK_IPC_CH_FROM_NET`

**提示（Prompt）**：用于 RTC 预节拍的 IPC 0 通道（RTC pretick）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_NRF53_RTC_PRETICK && CONFIG_SOC_SERIES_NRF53 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[0, 15]
```

**定义位置（Location）**：[`soc/nordic/nrf53/Kconfig:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf53/Kconfig#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → nRF5340 异常 165 的预节拍规避措施（Pre-tick workaround）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF53_RTC_PRETICK`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF53_RTC_PRETICK)、[`CONFIG_SOC_SERIES_NRF53`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_NRF53_RTC_PRETICK_IPC_CH_TO_NET"></a>

## 290.48 `CONFIG_SOC_NRF53_RTC_PRETICK_IPC_CH_TO_NET`

**提示（Prompt）**：用于 RTC 预节拍的 IPC 1 通道（RTC pretick）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_NRF53_RTC_PRETICK && CONFIG_SOC_SERIES_NRF53 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
11
```

**取值范围（Ranges）**

```text
[0, 15]
```

**定义位置（Location）**：[`soc/nordic/nrf53/Kconfig:116`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf53/Kconfig#L116)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → nRF5340 异常 165 的预节拍规避措施（Pre-tick workaround）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF53_RTC_PRETICK`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF53_RTC_PRETICK)、[`CONFIG_SOC_SERIES_NRF53`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_NRF54H20"></a>

## 290.49 `CONFIG_SOC_NRF54H20`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

nRF54H20 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_NRF54H
```

**被选择（Selected by）**

```text
CONFIG_SOC_NRF54H20_CPUAPP
CONFIG_SOC_NRF54H20_CPURAD
CONFIG_SOC_NRF54H20_CPUPPR
CONFIG_SOC_NRF54H20_CPUFLPR
```

**定义位置（Location）**：[`soc/nordic/nrf54h/Kconfig.soc:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54h/Kconfig.soc#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF54H`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54H)、[`CONFIG_SOC_NRF54H20_CPUAPP`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54H20_CPUAPP)、[`CONFIG_SOC_NRF54H20_CPURAD`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54H20_CPURAD)、[`CONFIG_SOC_NRF54H20_CPUPPR`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54H20_CPUPPR)、[`CONFIG_SOC_NRF54H20_CPUFLPR`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54H20_CPUFLPR)。

<a id="CONFIG_SOC_NRF54H20_BICR_NAME"></a>

## 290.50 `CONFIG_SOC_NRF54H20_BICR_NAME`

**提示（Prompt）**：要使用的 nRF54H20 开发板信息配置寄存器文件名称（BICR file）

**说明（Help）**

首先在应用目录中查找此文件；未找到时，再在开发板目录中查找。应用可通过设置 `CONFIG_SOC_NRF54H20_BICR_NAME="some_bicr.json"` 选择一个 BICR 文件。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_NRF54H20_GENERATE_BICR && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
"bicr.json"
```

**定义位置（Location）**：[`soc/nordic/nrf54h/bicr/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54h/bicr/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 生成 nRF54H20 开发板信息配置寄存器文件（BICR file）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF54H20_GENERATE_BICR`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54H20_GENERATE_BICR)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_NRF54H20_CPUAPP"></a>

## 290.51 `CONFIG_SOC_NRF54H20_CPUAPP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

nRF54H20 应用 CPU（CPUAPP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_NRF54H20
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NRF54H20DK
```

**定义位置（Location）**：[`soc/nordic/nrf54h/Kconfig.soc:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54h/Kconfig.soc#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF54H20`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54H20)、[`CONFIG_BOARD_NRF54H20DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NRF54H20DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NRF54H20DK`。

<a id="CONFIG_SOC_NRF54H20_CPUFLPR"></a>

## 290.52 `CONFIG_SOC_NRF54H20_CPUFLPR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

nRF54H20 FLPR 内核（CPUFLPR）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_NRF54H20
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NRF54H20DK
```

**定义位置（Location）**：[`soc/nordic/nrf54h/Kconfig.soc:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54h/Kconfig.soc#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF54H20`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54H20)、[`CONFIG_BOARD_NRF54H20DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NRF54H20DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NRF54H20DK`。

<a id="CONFIG_SOC_NRF54H20_CPUPPR"></a>

## 290.53 `CONFIG_SOC_NRF54H20_CPUPPR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

nRF54H20 PPR 内核（CPUPPR）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_NRF54H20
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NRF54H20DK
```

**定义位置（Location）**：[`soc/nordic/nrf54h/Kconfig.soc:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54h/Kconfig.soc#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF54H20`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54H20)、[`CONFIG_BOARD_NRF54H20DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NRF54H20DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NRF54H20DK`。

<a id="CONFIG_SOC_NRF54H20_CPURAD"></a>

## 290.54 `CONFIG_SOC_NRF54H20_CPURAD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

nRF54H20 无线电 CPU（CPURAD）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_NRF54H20
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NRF54H20DK
```

**定义位置（Location）**：[`soc/nordic/nrf54h/Kconfig.soc:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54h/Kconfig.soc#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF54H20`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54H20)、[`CONFIG_BOARD_NRF54H20DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NRF54H20DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NRF54H20DK`。

<a id="CONFIG_SOC_NRF54H20_CPURAD_ENABLE"></a>

## 290.55 `CONFIG_SOC_NRF54H20_CPURAD_ENABLE`

**提示（Prompt）**：启动 nRF54H20 无线电内核（Radio core）

**说明（Help）**

在应用启动时启用无线电内核（Radiocore）的时钟，并为无线电内核子系统请求电源。随后无线电内核开始执行指令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_NRF54H20_CPUAPP && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y if CONFIG_NRF_802154_SER_HOST || CONFIG_BT_HCI_HOST
```

**主动选择（Selects）**

```text
CONFIG_IRONSIDE_SE_CALL
CONFIG_SOC_LATE_INIT_HOOK
```

**定义位置（Location）**：[`soc/nordic/nrf54h/Kconfig:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54h/Kconfig#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF54H20_CPUAPP`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54H20_CPUAPP)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_NRF_802154_SER_HOST`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SER_HOST)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_IRONSIDE_SE_CALL`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_IRONSIDE_SE_CALL)、[`CONFIG_SOC_LATE_INIT_HOOK`](P002_kernel_配置项参考_2.md#CONFIG_SOC_LATE_INIT_HOOK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_SOC_NRF54H20_CPURAD_ENABLE_CHECK_VTOR"></a>

## 290.56 `CONFIG_SOC_NRF54H20_CPURAD_ENABLE_CHECK_VTOR`

**提示（Prompt）**：启动无线电内核前检查向量表偏移寄存器（VTOR）

**说明（Help）**

启动无线电内核（Radiocore）前，验证向量表偏移寄存器（VTOR）不为 `0xFFFFFFFF`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_NRF54H20_CPURAD_ENABLE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nordic/nrf54h/Kconfig:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54h/Kconfig#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 启动 nRF54H20 无线电内核（Radio core）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF54H20_CPURAD_ENABLE`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54H20_CPURAD_ENABLE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_NRF54H20_CPURAD_ENABLE_DEBUG_WAIT"></a>

## 290.57 `CONFIG_SOC_NRF54H20_CPURAD_ENABLE_DEBUG_WAIT`

**提示（Prompt）**：以调试等待模式启动无线电内核（DEBUGWAIT mode）

**说明（Help）**

复位后立即暂停无线电内核（Radio core）。这样可确保调试器从第一条指令开始就能连接并取得控制权。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_NRF54H20_CPURAD_ENABLE && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/nrf54h/Kconfig:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54h/Kconfig#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 启动 nRF54H20 无线电内核（Radio core）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF54H20_CPURAD_ENABLE`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54H20_CPURAD_ENABLE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_NRF54H20_GENERATE_BICR"></a>

## 290.58 `CONFIG_SOC_NRF54H20_GENERATE_BICR`

**提示（Prompt）**：生成 nRF54H20 开发板信息配置寄存器文件（BICR file）

**说明（Help）**

此选项为所用开发板生成开发板信息配置寄存器文件（BICR file）。开发板目录必须包含 `bicr.json`，此选项才能工作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_NRF54H20_CPUAPP && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nordic/nrf54h/bicr/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54h/bicr/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF54H20_CPUAPP`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54H20_CPUAPP)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_NRF54H20_PM_S2RAM_OVERRIDE"></a>

## 290.59 `CONFIG_SOC_NRF54H20_PM_S2RAM_OVERRIDE`

**提示（Prompt）**：覆盖挂起到 RAM 实现（`pm_s2ram` implementation）

**说明（Help）**

覆盖 Nordic 挂起到 RAM 实现（s2ram implementation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/nrf54h/Kconfig:109`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54h/Kconfig#L109)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_NRF54L05"></a>

## 290.60 `CONFIG_SOC_NRF54L05`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54L05 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_NRF54L
```

**被选择（Selected by）**

```text
CONFIG_SOC_NRF54L05_CPUAPP
CONFIG_SOC_NRF54L05_CPUFLPR
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF54L`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54L)、[`CONFIG_SOC_NRF54L05_CPUAPP`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54L05_CPUAPP)、[`CONFIG_SOC_NRF54L05_CPUFLPR`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54L05_CPUFLPR)。

<a id="CONFIG_SOC_NRF54L05_CPUAPP"></a>

## 290.61 `CONFIG_SOC_NRF54L05_CPUAPP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54L05 应用 CPU（CPUAPP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_NRF54L05
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NRF54L15DK
CONFIG_BOARD_UBX_EVKNORAB2
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF54L05`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54L05)、[`CONFIG_BOARD_NRF54L15DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NRF54L15DK)、[`CONFIG_BOARD_UBX_EVKNORAB2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_UBX_EVKNORAB2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NRF54L15DK`、`CONFIG_BOARD_UBX_EVKNORAB2`。

<a id="CONFIG_SOC_NRF54L05_CPUFLPR"></a>

## 290.62 `CONFIG_SOC_NRF54L05_CPUFLPR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54L05 FLPR 内核（CPUFLPR）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_NRF54L05
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NRF54L15DK
CONFIG_BOARD_UBX_EVKNORAB2
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF54L05`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54L05)、[`CONFIG_BOARD_NRF54L15DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NRF54L15DK)、[`CONFIG_BOARD_UBX_EVKNORAB2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_UBX_EVKNORAB2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NRF54L15DK`、`CONFIG_BOARD_UBX_EVKNORAB2`。

<a id="CONFIG_SOC_NRF54L05_DEVELOP_IN_NRF54L15"></a>

## 290.63 `CONFIG_SOC_NRF54L05_DEVELOP_IN_NRF54L15`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

可使用 `nrf54l15dk` 开发板配置，在 nRF54L15 开发套件（DK）上开展面向 nRF54L05 SoC 的开发。`system_nrf54l.c` 及 SoC 勘误（errata）中的某些系统初始化功能需要考虑此符号。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NRF54L && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig:137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig#L137)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF54L`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54L)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_NRF54L10"></a>

## 290.64 `CONFIG_SOC_NRF54L10`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54L10 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_NRF54L
```

**被选择（Selected by）**

```text
CONFIG_SOC_NRF54L10_CPUAPP
CONFIG_SOC_NRF54L10_CPUFLPR
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF54L`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54L)、[`CONFIG_SOC_NRF54L10_CPUAPP`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54L10_CPUAPP)、[`CONFIG_SOC_NRF54L10_CPUFLPR`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54L10_CPUFLPR)。

<a id="CONFIG_SOC_NRF54L10_CPUAPP"></a>

## 290.65 `CONFIG_SOC_NRF54L10_CPUAPP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54L10 应用 CPU（CPUAPP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_NRF54L10
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NRF54L15DK
CONFIG_BOARD_UBX_EVKNORAB2
CONFIG_BOARD_BL54L15_DVK
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF54L10`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54L10)、[`CONFIG_BOARD_NRF54L15DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NRF54L15DK)、[`CONFIG_BOARD_UBX_EVKNORAB2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_UBX_EVKNORAB2)、[`CONFIG_BOARD_BL54L15_DVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_BL54L15_DVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NRF54L15DK`、`CONFIG_BOARD_UBX_EVKNORAB2`、`CONFIG_BOARD_BL54L15_DVK`。

<a id="CONFIG_SOC_NRF54L10_CPUFLPR"></a>

## 290.66 `CONFIG_SOC_NRF54L10_CPUFLPR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54L10 FLPR 内核（CPUFLPR）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_NRF54L10
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NRF54L15DK
CONFIG_BOARD_UBX_EVKNORAB2
CONFIG_BOARD_BL54L15_DVK
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF54L10`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54L10)、[`CONFIG_BOARD_NRF54L15DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NRF54L15DK)、[`CONFIG_BOARD_UBX_EVKNORAB2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_UBX_EVKNORAB2)、[`CONFIG_BOARD_BL54L15_DVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_BL54L15_DVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NRF54L15DK`、`CONFIG_BOARD_UBX_EVKNORAB2`、`CONFIG_BOARD_BL54L15_DVK`。

<a id="CONFIG_SOC_NRF54L10_DEVELOP_IN_NRF54L15"></a>

## 290.67 `CONFIG_SOC_NRF54L10_DEVELOP_IN_NRF54L15`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

可使用 `nrf54l15dk` 开发板配置，在 nRF54L15 开发套件（DK）上开展面向 nRF54L10 SoC 的开发。`system_nrf54l.c` 及 SoC 勘误（errata）中的某些系统初始化功能需要考虑此符号。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NRF54L && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig:130`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig#L130)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF54L`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54L)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_NRF54L15"></a>

## 290.68 `CONFIG_SOC_NRF54L15`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54L15 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_NRF54L
```

**被选择（Selected by）**

```text
CONFIG_SOC_NRF54L15_CPUAPP
CONFIG_SOC_NRF54L15_CPUFLPR
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF54L`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54L)、[`CONFIG_SOC_NRF54L15_CPUAPP`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54L15_CPUAPP)、[`CONFIG_SOC_NRF54L15_CPUFLPR`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54L15_CPUFLPR)。

<a id="CONFIG_SOC_NRF54L15_CPUAPP"></a>

## 290.69 `CONFIG_SOC_NRF54L15_CPUAPP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54L15 应用 CPU（CPUAPP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_NRF54L15
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NRF54L15TAG
CONFIG_BOARD_NRF54L15DK
CONFIG_BOARD_NRF93M1DK
CONFIG_BOARD_OPHELIA4EV
CONFIG_BOARD_XIAO_NRF54L15
CONFIG_BOARD_EC4L15BA1
CONFIG_BOARD_UBX_EVKNORAB2
CONFIG_BOARD_HOLYIOT_25008
CONFIG_BOARD_RAYTAC_AN54LV_DB_15
CONFIG_BOARD_RAYTAC_AN54LQ_DB_15
CONFIG_BOARD_BL54L15_DVK
CONFIG_BOARD_PANB611EVB
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF54L15`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54L15)、[`CONFIG_BOARD_NRF54L15TAG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NRF54L15TAG)、[`CONFIG_BOARD_NRF54L15DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NRF54L15DK)、[`CONFIG_BOARD_NRF93M1DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NRF93M1DK)、[`CONFIG_BOARD_OPHELIA4EV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_OPHELIA4EV)、[`CONFIG_BOARD_XIAO_NRF54L15`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_XIAO_NRF54L15)、[`CONFIG_BOARD_EC4L15BA1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EC4L15BA1)、[`CONFIG_BOARD_UBX_EVKNORAB2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_UBX_EVKNORAB2)、[`CONFIG_BOARD_HOLYIOT_25008`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_HOLYIOT_25008)、[`CONFIG_BOARD_RAYTAC_AN54LV_DB_15`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RAYTAC_AN54LV_DB_15)、[`CONFIG_BOARD_RAYTAC_AN54LQ_DB_15`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RAYTAC_AN54LQ_DB_15)、[`CONFIG_BOARD_BL54L15_DVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_BL54L15_DVK)、[`CONFIG_BOARD_PANB611EVB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_PANB611EVB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NRF54L15TAG`、`CONFIG_BOARD_NRF54L15DK`、`CONFIG_BOARD_NRF93M1DK`、`CONFIG_BOARD_OPHELIA4EV`、`CONFIG_BOARD_XIAO_NRF54L15`、`CONFIG_BOARD_EC4L15BA1`、`CONFIG_BOARD_UBX_EVKNORAB2`、`CONFIG_BOARD_HOLYIOT_25008`、`CONFIG_BOARD_RAYTAC_AN54LV_DB_15`、`CONFIG_BOARD_RAYTAC_AN54LQ_DB_15`、`CONFIG_BOARD_BL54L15_DVK`、`CONFIG_BOARD_PANB611EVB`。

<a id="CONFIG_SOC_NRF54L15_CPUFLPR"></a>

## 290.70 `CONFIG_SOC_NRF54L15_CPUFLPR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54L15 FLPR 内核（CPUFLPR）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_NRF54L15
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NRF54L15TAG
CONFIG_BOARD_NRF54L15DK
CONFIG_BOARD_NRF93M1DK
CONFIG_BOARD_OPHELIA4EV
CONFIG_BOARD_XIAO_NRF54L15
CONFIG_BOARD_EC4L15BA1
CONFIG_BOARD_UBX_EVKNORAB2
CONFIG_BOARD_RAYTAC_AN54LV_DB_15
CONFIG_BOARD_RAYTAC_AN54LQ_DB_15
CONFIG_BOARD_BL54L15_DVK
CONFIG_BOARD_PANB611EVB
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF54L15`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54L15)、[`CONFIG_BOARD_NRF54L15TAG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NRF54L15TAG)、[`CONFIG_BOARD_NRF54L15DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NRF54L15DK)、[`CONFIG_BOARD_NRF93M1DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NRF93M1DK)、[`CONFIG_BOARD_OPHELIA4EV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_OPHELIA4EV)、[`CONFIG_BOARD_XIAO_NRF54L15`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_XIAO_NRF54L15)、[`CONFIG_BOARD_EC4L15BA1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EC4L15BA1)、[`CONFIG_BOARD_UBX_EVKNORAB2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_UBX_EVKNORAB2)、[`CONFIG_BOARD_RAYTAC_AN54LV_DB_15`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RAYTAC_AN54LV_DB_15)、[`CONFIG_BOARD_RAYTAC_AN54LQ_DB_15`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RAYTAC_AN54LQ_DB_15)、[`CONFIG_BOARD_BL54L15_DVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_BL54L15_DVK)、[`CONFIG_BOARD_PANB611EVB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_PANB611EVB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NRF54L15TAG`、`CONFIG_BOARD_NRF54L15DK`、`CONFIG_BOARD_NRF93M1DK`、`CONFIG_BOARD_OPHELIA4EV`、`CONFIG_BOARD_XIAO_NRF54L15`、`CONFIG_BOARD_EC4L15BA1`、`CONFIG_BOARD_UBX_EVKNORAB2`、`CONFIG_BOARD_RAYTAC_AN54LV_DB_15`、`CONFIG_BOARD_RAYTAC_AN54LQ_DB_15`、`CONFIG_BOARD_BL54L15_DVK`、`CONFIG_BOARD_PANB611EVB`。

<a id="CONFIG_SOC_NRF54LM20A"></a>

## 290.71 `CONFIG_SOC_NRF54LM20A`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54LM20A 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_NRF54L
```

**被选择（Selected by）**

```text
CONFIG_SOC_NRF54LM20A_CPUAPP
CONFIG_SOC_NRF54LM20A_CPUFLPR
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF54L`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54L)、[`CONFIG_SOC_NRF54LM20A_CPUAPP`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54LM20A_CPUAPP)、[`CONFIG_SOC_NRF54LM20A_CPUFLPR`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54LM20A_CPUFLPR)。

<a id="CONFIG_SOC_NRF54LM20A_CPUAPP"></a>

## 290.72 `CONFIG_SOC_NRF54LM20A_CPUAPP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54LM20A 应用 CPU（CPUAPP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_NRF54LM20A
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NRF54LM20DK
CONFIG_BOARD_XIAO_NRF54LM20A
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF54LM20A`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54LM20A)、[`CONFIG_BOARD_NRF54LM20DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NRF54LM20DK)、[`CONFIG_BOARD_XIAO_NRF54LM20A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_XIAO_NRF54LM20A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NRF54LM20DK`、`CONFIG_BOARD_XIAO_NRF54LM20A`。

<a id="CONFIG_SOC_NRF54LM20A_CPUFLPR"></a>

## 290.73 `CONFIG_SOC_NRF54LM20A_CPUFLPR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54LM20A FLPR 内核（CPUFLPR）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_NRF54LM20A
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NRF54LM20DK
CONFIG_BOARD_XIAO_NRF54LM20A
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF54LM20A`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54LM20A)、[`CONFIG_BOARD_NRF54LM20DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NRF54LM20DK)、[`CONFIG_BOARD_XIAO_NRF54LM20A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_XIAO_NRF54LM20A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NRF54LM20DK`、`CONFIG_BOARD_XIAO_NRF54LM20A`。

<a id="CONFIG_SOC_NRF54LM20A_DEVELOP_IN_NRF54LM20B"></a>

## 290.74 `CONFIG_SOC_NRF54LM20A_DEVELOP_IN_NRF54LM20B`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

可使用 `nrf54lm20dk` 开发板配置，在 nRF54LM20B 开发套件（DK）上开展面向 nRF54LM20A 或 nRF54LM20B SoC 的开发。SoC 勘误（errata）中的某些系统初始化功能需要考虑此符号。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NRF54L && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig:123`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig#L123)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF54L`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54L)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_NRF54LM20B"></a>

## 290.75 `CONFIG_SOC_NRF54LM20B`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54LM20B 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_NRF54L
```

**被选择（Selected by）**

```text
CONFIG_SOC_NRF54LM20B_CPUAPP
CONFIG_SOC_NRF54LM20B_CPUFLPR
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF54L`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54L)、[`CONFIG_SOC_NRF54LM20B_CPUAPP`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54LM20B_CPUAPP)、[`CONFIG_SOC_NRF54LM20B_CPUFLPR`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54LM20B_CPUFLPR)。

<a id="CONFIG_SOC_NRF54LM20B_CPUAPP"></a>

## 290.76 `CONFIG_SOC_NRF54LM20B_CPUAPP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54LM20B 应用 CPU（CPUAPP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_NRF54LM20B
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NRF54LM20DK
CONFIG_BOARD_XIAO_NRF54LM20B
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF54LM20B`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54LM20B)、[`CONFIG_BOARD_NRF54LM20DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NRF54LM20DK)、[`CONFIG_BOARD_XIAO_NRF54LM20B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_XIAO_NRF54LM20B)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NRF54LM20DK`、`CONFIG_BOARD_XIAO_NRF54LM20B`。

<a id="CONFIG_SOC_NRF54LM20B_CPUFLPR"></a>

## 290.77 `CONFIG_SOC_NRF54LM20B_CPUFLPR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54LM20B FLPR 内核（CPUFLPR）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_NRF54LM20B
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NRF54LM20DK
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF54LM20B`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54LM20B)、[`CONFIG_BOARD_NRF54LM20DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NRF54LM20DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NRF54LM20DK`。

<a id="CONFIG_SOC_NRF54LV10A"></a>

## 290.78 `CONFIG_SOC_NRF54LV10A`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54LV10A 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_NRF54L
```

**被选择（Selected by）**

```text
CONFIG_SOC_NRF54LV10A_CPUAPP
CONFIG_SOC_NRF54LV10A_CPUFLPR
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF54L`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54L)、[`CONFIG_SOC_NRF54LV10A_CPUAPP`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54LV10A_CPUAPP)、[`CONFIG_SOC_NRF54LV10A_CPUFLPR`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54LV10A_CPUFLPR)。

<a id="CONFIG_SOC_NRF54LV10A_CPUAPP"></a>

## 290.79 `CONFIG_SOC_NRF54LV10A_CPUAPP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54LV10A 应用 CPU（CPUAPP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_NRF54LV10A
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NRF54LV10DK
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF54LV10A`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54LV10A)、[`CONFIG_BOARD_NRF54LV10DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NRF54LV10DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NRF54LV10DK`。

<a id="CONFIG_SOC_NRF54LV10A_CPUFLPR"></a>

## 290.80 `CONFIG_SOC_NRF54LV10A_CPUFLPR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54LV10A FLPR 内核（CPUFLPR）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_NRF54LV10A
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NRF54LV10DK
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:123`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L123)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF54LV10A`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54LV10A)、[`CONFIG_BOARD_NRF54LV10DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NRF54LV10DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NRF54LV10DK`。

<a id="CONFIG_SOC_NRF54LX_DISABLE_FICR_TRIMCNF"></a>

## 290.81 `CONFIG_SOC_NRF54LX_DISABLE_FICR_TRIMCNF`

**提示（Prompt）**：禁用器件修调（Disable trimming）

**说明（Help）**

禁用器件修调（trimming）。修调时，会将所有修调值从工厂信息配置寄存器（FICR）复制到目标地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NRF54L && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y if CONFIG_TRUSTED_EXECUTION_NONSECURE
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF54L`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54L)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_TRUSTED_EXECUTION_NONSECURE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRUSTED_EXECUTION_NONSECURE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_NRF54LX_SKIP_GLITCHDETECTOR_DISABLE"></a>

## 290.82 `CONFIG_SOC_NRF54LX_SKIP_GLITCHDETECTOR_DISABLE`

**提示（Prompt）**：跳过毛刺检测器禁用步骤（Skip disabling glitch detector）

**说明（Help）**

使用此项时，系统初始化期间不会禁用毛刺检测器（glitch detector）。CPU 在毛刺检测器的默认状态下运行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NRF54L && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y if CONFIG_TRUSTED_EXECUTION_NONSECURE || CONFIG_MCUBOOT
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF54L`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54L)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_TRUSTED_EXECUTION_NONSECURE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRUSTED_EXECUTION_NONSECURE)、[`CONFIG_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_NRF54LX_SKIP_TAMPC_SETUP"></a>

## 290.83 `CONFIG_SOC_NRF54LX_SKIP_TAMPC_SETUP`

**提示（Prompt）**：跳过防篡改控制器设置（Skip TAMPC setup）

**说明（Help）**

使用此项时，系统初始化期间省略防篡改控制器（Tamper controller）的设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NRF54L && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF54L`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54L)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_NRF54L_ANOMALY_56_WORKAROUND"></a>

## 290.84 `CONFIG_SOC_NRF54L_ANOMALY_56_WORKAROUND`

**提示（Prompt）**：为 nRF54L SoC 应用规避措施 56（workaround 56）

**说明（Help）**

此选项为 nRF54L 系列 SoC 启用配置规避措施 56（configuration workaround 56）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NRF54L && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF54L`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54L)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_NRF7120"></a>

## 290.85 `CONFIG_SOC_NRF7120`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF7120 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_NRF71
```

**被选择（Selected by）**

```text
CONFIG_SOC_NRF7120_ENGA
```

**定义位置（Location）**：[`soc/nordic/nrf71/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf71/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF71`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF71)、[`CONFIG_SOC_NRF7120_ENGA`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF7120_ENGA)。

<a id="CONFIG_SOC_NRF7120E"></a>

## 290.86 `CONFIG_SOC_NRF7120E`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF7120E 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_NRF71
```

**被选择（Selected by）**

```text
CONFIG_SOC_NRF7120E_ENGA
```

**定义位置（Location）**：[`soc/nordic/nrf71/Kconfig.soc:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf71/Kconfig.soc#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF71`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF71)、[`CONFIG_SOC_NRF7120E_ENGA`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF7120E_ENGA)。

<a id="CONFIG_SOC_NRF7120E_ENGA"></a>

## 290.87 `CONFIG_SOC_NRF7120E_ENGA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF7120E 工程 A 版（ENGA）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_NRF7120E
```

**被选择（Selected by）**

```text
CONFIG_SOC_NRF7120E_ENGA_CPUAPP
CONFIG_SOC_NRF7120E_ENGA_CPUFLPR
```

**定义位置（Location）**：[`soc/nordic/nrf71/Kconfig.soc:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf71/Kconfig.soc#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF7120E`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF7120E)、[`CONFIG_SOC_NRF7120E_ENGA_CPUAPP`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF7120E_ENGA_CPUAPP)、[`CONFIG_SOC_NRF7120E_ENGA_CPUFLPR`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF7120E_ENGA_CPUFLPR)。

<a id="CONFIG_SOC_NRF7120E_ENGA_CPUAPP"></a>

## 290.88 `CONFIG_SOC_NRF7120E_ENGA_CPUAPP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF7120E 工程 A 版应用 CPU（ENGA CPUAPP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_NRF7120E_ENGA
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NRF7120DK
```

**定义位置（Location）**：[`soc/nordic/nrf71/Kconfig.soc:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf71/Kconfig.soc#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF7120E_ENGA`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF7120E_ENGA)、[`CONFIG_BOARD_NRF7120DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NRF7120DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NRF7120DK`。

<a id="CONFIG_SOC_NRF7120E_ENGA_CPUFLPR"></a>

## 290.89 `CONFIG_SOC_NRF7120E_ENGA_CPUFLPR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF7120E 工程 A 版 FLPR 内核（ENGA CPUFLPR）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_NRF7120E_ENGA
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NRF7120DK
```

**定义位置（Location）**：[`soc/nordic/nrf71/Kconfig.soc:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf71/Kconfig.soc#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF7120E_ENGA`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF7120E_ENGA)、[`CONFIG_BOARD_NRF7120DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NRF7120DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NRF7120DK`。

<a id="CONFIG_SOC_NRF7120_APPROTECT_BOOT_WORKAROUND"></a>

## 290.90 `CONFIG_SOC_NRF7120_APPROTECT_BOOT_WORKAROUND`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 nRF7120 或 nRF7120E 应用内核时，启用访问端口保护启动规避措施（APPROTECT boot workaround）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NRF71 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_NRF7120_ENGA_CPUAPP || CONFIG_SOC_NRF7120E_ENGA_CPUAPP
```

**定义位置（Location）**：[`soc/nordic/nrf71/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf71/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF71`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF71)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_SOC_NRF7120_ENGA_CPUAPP`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF7120_ENGA_CPUAPP)、[`CONFIG_SOC_NRF7120E_ENGA_CPUAPP`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF7120E_ENGA_CPUAPP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_NRF7120_DEVELOP_IN_NRF7120E"></a>

## 290.91 `CONFIG_SOC_NRF7120_DEVELOP_IN_NRF7120E`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

可使用 `nrf7120dk` 开发板配置，在 nRF7120E 开发套件（DK）上开展面向 nRF7120 或 nRF7120E SoC 的开发。SoC 勘误（errata）中的某些系统初始化功能需要考虑此符号。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NRF71 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/nrf71/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf71/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF71`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF71)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_NRF7120_ENGA"></a>

## 290.92 `CONFIG_SOC_NRF7120_ENGA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF7120 工程 A 版（ENGA）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_NRF7120
```

**被选择（Selected by）**

```text
CONFIG_SOC_NRF7120_ENGA_CPUAPP
CONFIG_SOC_NRF7120_ENGA_CPUFLPR
```

**定义位置（Location）**：[`soc/nordic/nrf71/Kconfig.soc:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf71/Kconfig.soc#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF7120`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF7120)、[`CONFIG_SOC_NRF7120_ENGA_CPUAPP`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF7120_ENGA_CPUAPP)、[`CONFIG_SOC_NRF7120_ENGA_CPUFLPR`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF7120_ENGA_CPUFLPR)。

<a id="CONFIG_SOC_NRF7120_ENGA_CPUAPP"></a>

## 290.93 `CONFIG_SOC_NRF7120_ENGA_CPUAPP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF7120 工程 A 版应用 CPU（ENGA CPUAPP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_NRF7120_ENGA
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NRF7120DK
```

**定义位置（Location）**：[`soc/nordic/nrf71/Kconfig.soc:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf71/Kconfig.soc#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF7120_ENGA`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF7120_ENGA)、[`CONFIG_BOARD_NRF7120DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NRF7120DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NRF7120DK`。

<a id="CONFIG_SOC_NRF7120_ENGA_CPUFLPR"></a>

## 290.94 `CONFIG_SOC_NRF7120_ENGA_CPUFLPR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF7120 工程 A 版 FLPR 内核（ENGA CPUFLPR）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_NRF7120_ENGA
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NRF7120DK
```

**定义位置（Location）**：[`soc/nordic/nrf71/Kconfig.soc:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf71/Kconfig.soc#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF7120_ENGA`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF7120_ENGA)、[`CONFIG_BOARD_NRF7120DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NRF7120DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NRF7120DK`。

<a id="CONFIG_SOC_NRF7120_TFM_MRAMC_SERVICE"></a>

## 290.95 `CONFIG_SOC_NRF7120_TFM_MRAMC_SERVICE`

**提示（Prompt）**：TF-M 磁阻 RAM 控制器服务（MRAMC service）

**说明（Help）**

为 nRF7120 SoC 提供磁阻 RAM 控制器服务（MRAMC service）。此服务允许非安全应用通过安全服务调用（secure service call），请求系统配置 MRAMC。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_NRF7120 || CONFIG_SOC_NRF7120E) && CONFIG_SOC_FLASH_NRF_MRAMC && CONFIG_BUILD_WITH_TFM && CONFIG_SOC_SERIES_NRF71 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nordic/nrf71/Kconfig:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf71/Kconfig#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF7120`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF7120)、[`CONFIG_SOC_NRF7120E`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF7120E)、[`CONFIG_SOC_FLASH_NRF_MRAMC`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_MRAMC)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_SOC_SERIES_NRF71`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF71)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_NRF7120_WICR_SETUP"></a>

## 290.96 `CONFIG_SOC_NRF7120_WICR_SETUP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启动时编程 Wi-Fi 信息配置寄存器（Wi-Fi Information Configuration Registers，WICR）。WICR 是用于配置 Wi-Fi 相关设置和值的非易失存储器区域（NVM region）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NRF71 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y if DT_HAS_NORDIC_NRF_WICR_ENABLED
```

**主动选择（Selects）**

```text
CONFIG_NRFX_MRAMC if !CONFIG_BUILD_WITH_TFM
```

**定义位置（Location）**：[`soc/nordic/nrf71/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf71/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF71`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF71)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_NRFX_MRAMC`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_MRAMC)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_NRF71_WIFI_BOOT"></a>

## 290.97 `CONFIG_SOC_NRF71_WIFI_BOOT`

**提示（Prompt）**：nRF71 在系统初始化时启动 Wi-Fi（start Wi-Fi on system initialization）

**说明（Help）**

控制是否在系统初始化时启动 Wi-Fi 内核。禁用时，应用必须先启动 Wi-Fi 内核才能使用。已启动的 Wi-Fi 内核只有配合 Wi-Fi 驱动才有用，因此默认禁用；必须由负责该内核的驱动或应用显式启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NRF71 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/nrf71/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf71/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF71`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF71)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_NRF71_WIFI_DAP"></a>

## 290.98 `CONFIG_SOC_NRF71_WIFI_DAP`

**提示（Prompt）**：nRF71 Wi-Fi 调试访问端口（Debug access port）

**说明（Help）**

控制用于调试 nRF71 Wi-Fi 内核的 Wi-Fi AHB 调试访问端口（Debug AP，DAP）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NRF71 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/nrf71/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf71/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF71`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF71)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_NRF9280"></a>

## 290.99 `CONFIG_SOC_NRF9280`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

nRF9280 系统级封装（SiP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_NRF9230_ENGB_CPUAPP if CONFIG_SOC_NRF9280_CPUAPP
CONFIG_SOC_NRF9230_ENGB_CPURAD if CONFIG_SOC_NRF9280_CPURAD
CONFIG_SOC_NRF9230_ENGB_CPUPPR if CONFIG_SOC_NRF9280_CPUPPR
```

**被选择（Selected by）**

```text
CONFIG_SOC_NRF9280_CPUAPP
CONFIG_SOC_NRF9280_CPURAD
CONFIG_SOC_NRF9280_CPUPPR
```

**定义位置（Location）**：[`soc/nordic/nrf92/Kconfig.soc:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf92/Kconfig.soc#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF9230_ENGB_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9230_ENGB_CPUAPP)、[`CONFIG_SOC_NRF9280_CPUAPP`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF9280_CPUAPP)、[`CONFIG_SOC_NRF9230_ENGB_CPURAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9230_ENGB_CPURAD)、[`CONFIG_SOC_NRF9280_CPURAD`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_NRF9280_CPURAD)、[`CONFIG_SOC_NRF9230_ENGB_CPUPPR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9230_ENGB_CPUPPR)、[`CONFIG_SOC_NRF9280_CPUPPR`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_NRF9280_CPUPPR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_NRF9230_ENGB_CPUAPP`、`CONFIG_SOC_NRF9230_ENGB_CPURAD`、`CONFIG_SOC_NRF9230_ENGB_CPUPPR`。

<a id="CONFIG_SOC_NRF9280_CPUAPP"></a>

## 290.100 `CONFIG_SOC_NRF9280_CPUAPP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

nRF9280 应用 CPU（CPUAPP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_NRF9280
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NRF9280PDK
```

**定义位置（Location）**：[`soc/nordic/nrf92/Kconfig.soc:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf92/Kconfig.soc#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF9280`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF9280)、[`CONFIG_BOARD_NRF9280PDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NRF9280PDK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NRF9280PDK`。

<!-- kconfig-navigation -->

[上一章](P289_soc_nordic_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P291_soc_nordic_配置项参考_3.md)
