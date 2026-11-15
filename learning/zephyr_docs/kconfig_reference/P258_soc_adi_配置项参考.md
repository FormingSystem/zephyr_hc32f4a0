---
id: learning.zephyr-docs.kconfig-reference.page-258
title: "`soc/adi`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第258章\_`soc/adi`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/adi` 的 17 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BUILD_WITH_TFM"></a>

## 258.1 `CONFIG_BUILD_WITH_TFM`

原库同名定义共 3 条；本项为数据库第 3449 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为开发板的非安全版本（Non-Secure version）自动设置 WITH_TFM

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_MAX32
```

**默认值（Defaults）**

```text
y if CONFIG_TRUSTED_EXECUTION_NONSECURE
```

**定义位置（Location）**：[`soc/adi/max32/Kconfig:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/adi/max32/Kconfig#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MAX32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32)、[`CONFIG_TRUSTED_EXECUTION_NONSECURE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRUSTED_EXECUTION_NONSECURE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MAX32`。

<a id="CONFIG_MAX32_ON_ENTER_CPU_IDLE_HOOK"></a>

## 258.2 `CONFIG_MAX32_ON_ENTER_CPU_IDLE_HOOK`

**提示（Prompt）**：启用 CPU 空闲钩子（CPU idle hook）

**说明（Help）**

启用钩子 `z_arm_on_enter_cpu_idle()`，在通过 `k_cpu_idle()` 或 `k_cpu_atomic_idle()` 使 CPU 空闲时调用。必要时，可通过该钩子跳过 `WFE/WFI` 指令，阻止 CPU 实际进入休眠（Sleep）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM && CONFIG_SOC_FAMILY_MAX32
```

**默认值（Defaults）**

```text
y if !CONFIG_PM
```

**弱选择（Implies）**

```text
CONFIG_ARM_ON_ENTER_CPU_IDLE_HOOK
```

**定义位置（Location）**：[`soc/adi/max32/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/adi/max32/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_SOC_FAMILY_MAX32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_ARM_ON_ENTER_CPU_IDLE_HOOK`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_ON_ENTER_CPU_IDLE_HOOK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MAX32`。

<a id="CONFIG_MAX32_SECONDARY_M4"></a>

## 258.3 `CONFIG_MAX32_SECONDARY_M4`

**提示（Prompt）**：启用辅助 M4 内核（Secondary M4 core）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX32_M4F_CPU1_ENABLED && CONFIG_SOC_FAMILY_MAX32
```

**定义位置（Location）**：[`soc/adi/max32/Kconfig:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/adi/max32/Kconfig#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MAX32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MAX32`。

<a id="CONFIG_MAX32_SECONDARY_M4_STARTUP_DELAY"></a>

## 258.4 `CONFIG_MAX32_SECONDARY_M4_STARTUP_DELAY`

**提示（Prompt）**：辅助 M4 内核启动延迟，单位为周期（startup delay in cycles）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MAX32_SECONDARY_M4 && CONFIG_SOC_FAMILY_MAX32
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`soc/adi/max32/Kconfig:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/adi/max32/Kconfig#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 启用辅助 M4 内核（Secondary M4 core）

**配置项引用（Symbol References）**：[`CONFIG_MAX32_SECONDARY_M4`](P258_soc_adi_配置项参考.md#CONFIG_MAX32_SECONDARY_M4)、[`CONFIG_SOC_FAMILY_MAX32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MAX32`。

<a id="CONFIG_MAX32_SECONDARY_RV32"></a>

## 258.5 `CONFIG_MAX32_SECONDARY_RV32`

**提示（Prompt）**：启用辅助 RISC-V 内核（Secondary RISC-V core）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX32_RV32_ENABLED && CONFIG_SOC_FAMILY_MAX32
```

**定义位置（Location）**：[`soc/adi/max32/Kconfig:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/adi/max32/Kconfig#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MAX32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MAX32`。

<a id="CONFIG_MAX32_SECONDARY_RV32_STARTUP_DELAY"></a>

## 258.6 `CONFIG_MAX32_SECONDARY_RV32_STARTUP_DELAY`

**提示（Prompt）**：辅助 RISC-V 内核启动延迟，单位为周期（startup delay in cycles）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MAX32_SECONDARY_RV32 && CONFIG_SOC_FAMILY_MAX32
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`soc/adi/max32/Kconfig:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/adi/max32/Kconfig#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_MAX32_SECONDARY_RV32`](P258_soc_adi_配置项参考.md#CONFIG_MAX32_SECONDARY_RV32)、[`CONFIG_SOC_FAMILY_MAX32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MAX32`。

<a id="CONFIG_MAX32_STANDBY_DELAY"></a>

## 258.7 `CONFIG_MAX32_STANDBY_DELAY`

**提示（Prompt）**：启动后在指定毫秒数内禁止待机（Prevent standby on boot）

**说明（Help）**

在指定毫秒数内阻止系统进入待机模式（standby mode）。目的是防止使用电源管理（power management）时无法再接入调试（debug lockout）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PM && CONFIG_SOC_FAMILY_MAX32
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`soc/adi/max32/Kconfig:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/adi/max32/Kconfig#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_SOC_FAMILY_MAX32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MAX32`。

<a id="CONFIG_SOC_FAMILY_MAX32_ERRATA_30282"></a>

## 258.8 `CONFIG_SOC_FAMILY_MAX32_ERRATA_30282`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果 SoC 受勘误 30282（errata 30282）影响，请选择此项；该勘误可能导致在指令缓存（instruction cache）启用时进入待机模式（standby mode）会引发系统硬故障（HardFault）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_MAX32
```

**被选择（Selected by）**

```text
CONFIG_SOC_MAX32657
```

**定义位置（Location）**：[`soc/adi/max32/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/adi/max32/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MAX32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32)、[`CONFIG_SOC_MAX32657`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MAX32657)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MAX32`、`CONFIG_SOC_MAX32657`。

<a id="CONFIG_SOC_FAMILY_MAX32_HALT_AFTER_BOOTLOADER_SUPPORT"></a>

## 258.9 `CONFIG_SOC_FAMILY_MAX32_HALT_AFTER_BOOTLOADER_SUPPORT`

**提示（Prompt）**：用于 JLink 的引导加载程序集成后停机（Halt after bootloader integration）

**说明（Help）**

使用 JLink 烧录 MAX32 SoC 时，为支持在复位后正确停机（halt），在早期复位代码中插入一个简短的虚拟读取（dummy read），以触发已设置的硬件断点（hardware breakpoint）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_FAMILY_MAX32_M4 || CONFIG_SOC_FAMILY_MAX32_M33) && CONFIG_SOC_FAMILY_MAX32
```

**默认值（Defaults）**

```text
y if !CONFIG_TRUSTED_EXECUTION_NONSECURE
```

**主动选择（Selects）**

```text
CONFIG_SOC_EARLY_RESET_HOOK
```

**定义位置（Location）**：[`soc/adi/max32/Kconfig:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/adi/max32/Kconfig#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MAX32_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_M4)、[`CONFIG_SOC_FAMILY_MAX32_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_M33)、[`CONFIG_SOC_FAMILY_MAX32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32)、[`CONFIG_TRUSTED_EXECUTION_NONSECURE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRUSTED_EXECUTION_NONSECURE)、[`CONFIG_SOC_EARLY_RESET_HOOK`](P002_kernel_配置项参考_2.md#CONFIG_SOC_EARLY_RESET_HOOK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MAX32_M4`、`CONFIG_SOC_FAMILY_MAX32_M33`、`CONFIG_SOC_FAMILY_MAX32`。

<a id="CONFIG_SOC_FAMILY_MAX32_SECURE_BOOT_SUPPORTED"></a>

## 258.10 `CONFIG_SOC_FAMILY_MAX32_SECURE_BOOT_SUPPORTED`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示 SoC 支持安全启动签名（secure boot signing）。具有安全启动能力且需要镜像签名的 SoC 会选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_MAX32651
CONFIG_SOC_MAX32672
```

**定义位置（Location）**：[`soc/adi/max32/Kconfig.soc:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/adi/max32/Kconfig.soc#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MAX32651`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MAX32651)、[`CONFIG_SOC_MAX32672`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MAX32672)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MAX32651`、`CONFIG_SOC_MAX32672`。

<a id="CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_KEY_PATH"></a>

## 258.11 `CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_KEY_PATH`

**提示（Prompt）**：安全 SoC 的密钥路径（key path）

**说明（Help）**

用于签署镜像的私钥路径（private key path）。签名工具（signing tool）使用此私钥为镜像签名。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING && CONFIG_SOC_FAMILY_MAX32
```

**定义位置（Location）**：[`soc/adi/max32/sbt/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/adi/max32/sbt/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 安全 SoC 镜像签名（image signing）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING`](P258_soc_adi_配置项参考.md#CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING)、[`CONFIG_SOC_FAMILY_MAX32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MAX32`。

<a id="CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNATURE_SECTION_SIZE"></a>

## 258.12 `CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNATURE_SECTION_SIZE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

链接时预留的签名节（signature section）大小，由所选签名算法（signing algorithm）决定。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING && CONFIG_SOC_FAMILY_MAX32
```

**默认值（Defaults）**

```text
256 if CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING_ALGO_RSA2048
64 if CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING_ALGO_ECDSA256
```

**定义位置（Location）**：[`soc/adi/max32/sbt/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/adi/max32/sbt/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 安全 SoC 镜像签名（image signing）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING`](P258_soc_adi_配置项参考.md#CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING)、[`CONFIG_SOC_FAMILY_MAX32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32)、[`CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING_ALGO_RSA2048`](P258_soc_adi_配置项参考.md#CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING_ALGO_RSA2048)、[`CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING_ALGO_ECDSA256`](P258_soc_adi_配置项参考.md#CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING_ALGO_ECDSA256)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MAX32`。

<a id="CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING"></a>

## 258.13 `CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING`

**提示（Prompt）**：安全 SoC 镜像签名（image signing）

**说明（Help）**

选择此项可为安全 SoC 启用镜像签名（image signing）。此项用于设置链接器配置并启用镜像签名，是必需的。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_MAX32_SECURE_BOOT_SUPPORTED && CONFIG_SOC_FAMILY_MAX32
```

**主动选择（Selects）**

```text
CONFIG_HAVE_CUSTOM_LINKER_SCRIPT
CONFIG_BUILD_OUTPUT_HEX_GAP_FILL if CONFIG_BUILD_OUTPUT_HEX
```

**定义位置（Location）**：[`soc/adi/max32/sbt/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/adi/max32/sbt/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MAX32_SECURE_BOOT_SUPPORTED`](P258_soc_adi_配置项参考.md#CONFIG_SOC_FAMILY_MAX32_SECURE_BOOT_SUPPORTED)、[`CONFIG_SOC_FAMILY_MAX32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32)、[`CONFIG_HAVE_CUSTOM_LINKER_SCRIPT`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_HAVE_CUSTOM_LINKER_SCRIPT)、[`CONFIG_BUILD_OUTPUT_HEX_GAP_FILL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_BUILD_OUTPUT_HEX_GAP_FILL)、[`CONFIG_BUILD_OUTPUT_HEX`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_BUILD_OUTPUT_HEX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MAX32`。

<a id="CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING_ALGO"></a>

## 258.14 `CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING_ALGO`

**提示（Prompt）**：安全 SoC 签名算法（signing algorithm）

**说明（Help）**

用于安全启动镜像签名（secure boot image signing）的签名算法。在各 SoC 的 `Kconfig.defconfig` 文件中设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING && CONFIG_SOC_FAMILY_MAX32
```

**默认值（Defaults）**

```text
CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING_ALGO_RSA2048
```

**可选项（Choices）**

```text
CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING_ALGO_RSA2048
CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING_ALGO_ECDSA256
```

**定义位置（Location）**：[`soc/adi/max32/sbt/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/adi/max32/sbt/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 安全 SoC 镜像签名（image signing）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING`](P258_soc_adi_配置项参考.md#CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING)、[`CONFIG_SOC_FAMILY_MAX32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32)、[`CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING_ALGO_RSA2048`](P258_soc_adi_配置项参考.md#CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING_ALGO_RSA2048)、[`CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING_ALGO_ECDSA256`](P258_soc_adi_配置项参考.md#CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING_ALGO_ECDSA256)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MAX32`。

<a id="CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING_ALGO_ECDSA256"></a>

## 258.15 `CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING_ALGO_ECDSA256`

**提示（Prompt）**：安全 SoC 签名算法 ECDSA256（signing algorithm）

**说明（Help）**

此 SoC 的签名算法（signing algorithm）为 ECDSA256。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING_ALGO>
```

**定义位置（Location）**：[`soc/adi/max32/sbt/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/adi/max32/sbt/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 安全 SoC 镜像签名（image signing） → 安全 SoC 签名算法（signing algorithm）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING_ALGO`](P258_soc_adi_配置项参考.md#CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING_ALGO)。

<a id="CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING_ALGO_RSA2048"></a>

## 258.16 `CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING_ALGO_RSA2048`

**提示（Prompt）**：安全 SoC 签名算法 RSA2048（signing algorithm）

**说明（Help）**

此 SoC 的签名算法（signing algorithm）为 RSA2048。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING_ALGO>
```

**定义位置（Location）**：[`soc/adi/max32/sbt/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/adi/max32/sbt/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 安全 SoC 镜像签名（image signing） → 安全 SoC 签名算法（signing algorithm）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING_ALGO`](P258_soc_adi_配置项参考.md#CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING_ALGO)。

<a id="SB_CONFIG_SOC_FAMILY_MAX32_SECURE_BOOT_SUPPORTED"></a>

## 258.17 `SB_CONFIG_SOC_FAMILY_MAX32_SECURE_BOOT_SUPPORTED`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示 SoC 支持安全启动签名（secure boot signing）。具有安全启动能力且需要镜像签名的 SoC 会选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
SB_CONFIG_SOC_MAX32651
SB_CONFIG_SOC_MAX32672
```

**定义位置（Location）**：[`soc/adi/max32/Kconfig.soc:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/adi/max32/Kconfig.soc#L24)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MAX32651`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MAX32651)、[`SB_CONFIG_SOC_MAX32672`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MAX32672)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MAX32651`、`SB_CONFIG_SOC_MAX32672`。

<!-- kconfig-navigation -->

[上一章](P257_soc_Kconfig.v2_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P259_soc_alif_配置项参考.md)
