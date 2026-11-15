---
id: learning.zephyr-docs.kconfig-reference.page-205
title: "`modules/Kconfig.mcuboot`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第205章\_`modules/Kconfig.mcuboot`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/Kconfig.mcuboot` 的 39 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_APP_LINK_WITH_MCUBOOT_BOOTUTIL"></a>

## 205.1 `CONFIG_APP_LINK_WITH_MCUBOOT_BOOTUTIL`

**提示（Prompt）**：将应用目标 `app` 与 MCUboot bootutil 库链接（link）

**说明（Help）**

将 MCUboot bootutil 库的头文件加入 `app` 的包含路径（include path）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUBOOT_BOOTUTIL_LIB
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:452`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L452)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 实用工具库（utility library）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_BOOTUTIL_LIB`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTUTIL_LIB)。

<a id="CONFIG_BOOTLOADER_MCUBOOT"></a>

## 205.2 `CONFIG_BOOTLOADER_MCUBOOT`

**提示（Prompt）**：MCUboot 引导加载程序（bootloader）支持

**说明（Help）**

此选项表示目标使用 MCUboot 作为引导加载程序（bootloader），即此镜像将由 MCUboot 链式加载（chain-loaded）。它设置若干必需的构建系统和设备树（Device Tree）选项，使生成的镜像能够由 MCUboot 开源引导加载程序启动。目前包括：

- 将 `ROM_START_OFFSET` 设为默认值，为 MCUboot 镜像头（image header）预留空间。
- 对没有内建向量重定位机制（vector relocation mechanisms）的 Cortex-M0 或 Armv8-M baseline 目标，启用 `SW_VECTOR_RELAY_CLIENT`。

默认情况下，如果应用支持，此选项要求 Zephyr 在启动期间初始化核心架构硬件寄存器（core architecture HW registers），从而无需 MCUboot 自行复位核心寄存器状态。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MCUBOOT
```

**主动选择（Selects）**

```text
CONFIG_USE_DT_CODE_PARTITION if !CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD && !CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT
```

**弱选择（Implies）**

```text
CONFIG_INIT_ARCH_HW_AT_BOOT if CONFIG_ARCH_SUPPORTS_ARCH_HW_INIT
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT)、[`CONFIG_USE_DT_CODE_PARTITION`](P004_Kconfig.zephyr_配置项参考_2.md#CONFIG_USE_DT_CODE_PARTITION)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT)、[`CONFIG_INIT_ARCH_HW_AT_BOOT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_INIT_ARCH_HW_AT_BOOT)、[`CONFIG_ARCH_SUPPORTS_ARCH_HW_INIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_ARCH_HW_INIT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_SUPPORTS_ARCH_HW_INIT`。

<a id="CONFIG_BOOT_IMAGE_ACCESS_HOOKS"></a>

## 205.3 `CONFIG_BOOT_IMAGE_ACCESS_HOOKS`

**提示（Prompt）**：用于覆盖 MCUboot bootutil 原生例程的钩子（hooks）

**说明（Help）**

允许提供过程（procedures），以覆盖或扩展 MCUboot 原生的镜像数据访问例程（native routines）。应用项目负责将实现这些钩子（hooks）的源文件加入构建。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUBOOT_BOOTUTIL_LIB
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:412`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L412)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 实用工具库（utility library）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_BOOTUTIL_LIB`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTUTIL_LIB)。

<a id="CONFIG_MCUBOOT"></a>

## 205.4 `CONFIG_MCUBOOT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏选项（hidden option），用于表示当前镜像为 MCUBoot。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`modules/Kconfig.mcuboot:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

<a id="CONFIG_MCUBOOT_APPLICATION_FIRMWARE_UPDATER"></a>

## 205.5 `CONFIG_MCUBOOT_APPLICATION_FIRMWARE_UPDATER`

**提示（Prompt）**：应用是固件更新程序镜像（firmware updater image）

**说明（Help）**

当前镜像为固件更新程序镜像（firmware updater image）时选择此项。镜像签名时将使用槽位 1（slot 1）的信息。注意：此镜像的 Zephyr chosen 节点 `zephyr,code-partition` 应设置为 `slot1_partition`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUBOOT_BOOTLOADER_MODE_FIRMWARE_UPDATER && CONFIG_BOOTLOADER_MCUBOOT
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:378`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L378)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 引导加载程序（bootloader）支持 → 板载 MCUboot 运行模式（operation mode）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_BOOTLOADER_MODE_FIRMWARE_UPDATER`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_FIRMWARE_UPDATER)、[`CONFIG_BOOTLOADER_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_BOOTLOADER_MCUBOOT)。

<a id="CONFIG_MCUBOOT_BOOTLOADER_MODE"></a>

## 205.6 `CONFIG_MCUBOOT_BOOTLOADER_MODE`

**提示（Prompt）**：应用所假定的 MCUboot 运行模式（mode of operation）

**说明（Help）**

告知应用构建过程所假定的 MCUboot 运行模式（mode of operation）。`west sign` 会依据设备树（DT）配置验证应用，此信息对验证很重要。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BOOTLOADER_MCUBOOT
```

**默认值（Defaults）**

```text
CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_MOVE if CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_OFFSET
```

**可选项（Choices）**

```text
CONFIG_MCUBOOT_BOOTLOADER_MODE_SINGLE_APP
CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_OFFSET
CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_MOVE
CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_SCRATCH
CONFIG_MCUBOOT_BOOTLOADER_MODE_OVERWRITE_ONLY
CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD
CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT
CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP
CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT
CONFIG_MCUBOOT_BOOTLOADER_MODE_FIRMWARE_UPDATER
CONFIG_MCUBOOT_BOOTLOADER_MODE_SINGLE_APP_RAM_LOAD
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:190`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L190)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 引导加载程序（bootloader）支持 → 板载 MCUboot 运行模式（operation mode）

**配置项引用（Symbol References）**：[`CONFIG_BOOTLOADER_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_BOOTLOADER_MCUBOOT)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_MOVE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_MOVE)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_OFFSET`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_OFFSET)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_SINGLE_APP`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_SINGLE_APP)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_SCRATCH`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_SCRATCH)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_OVERWRITE_ONLY`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_OVERWRITE_ONLY)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_FIRMWARE_UPDATER`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_FIRMWARE_UPDATER)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_SINGLE_APP_RAM_LOAD`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_SINGLE_APP_RAM_LOAD)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP"></a>

## 205.7 `CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP`

**提示（Prompt）**：MCUboot 已配置为直接原地执行模式（DirectXIP）

**说明（Help）**

MCUboot 要求设备树（DT）中存在 `slot0_partition` 和 `slot1_partition`。此模式下，可从任一分区启动，并选择应用镜像版本更高的分区。版本通常指 `major.minor.patch` 三元组；如果还选择了 `BOOT_VERSION_CMP_USE_BUILD_NUMBER`，则也会比较构建号（build number）。由于无法换回较旧版本的应用，此选项自动选择 `MCUBOOT_BOOTLOADER_NO_DOWNGRADE`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUBOOT_BOOTLOADER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE
CONFIG_MCUBOOT_BOOTLOADER_NO_DOWNGRADE
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:288`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L288)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 引导加载程序（bootloader）支持 → 板载 MCUboot 运行模式（operation mode） → 应用所假定的 MCUboot 运行模式（mode of operation）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_BOOTLOADER_MODE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE)、[`CONFIG_MCUBOOT_BOOTLOADER_NO_DOWNGRADE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_NO_DOWNGRADE)。

<a id="CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT"></a>

## 205.8 `CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT`

**提示（Prompt）**：MCUboot 已配置为带回退的 DirectXIP（DirectXIP with revert）

**说明（Help）**

MCUboot 要求设备树（DT）中存在 `slot0_partition` 和 `slot1_partition`。此模式下，只要应用被标记为下次启动时进行测试或永久启动，MCUboot 就会从任一槽位中选择版本更高的应用启动。标记为测试的应用必须在首次启动时自我确认（confirm），否则会被移除，MCUboot 将回退到先前获准的应用。此模式不允许自由切换应用版本：一旦较高版本获准，就不能再选择较低版本启动。由于无法对正在运行的应用降级，此模式选择 `MCUBOOT_BOOTLOADER_NO_DOWNGRADE`；但要注意，若较高版本应用未被确认，MCUboot 仍可能回退到较低版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUBOOT_BOOTLOADER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_MCUBOOT_BOOTUTIL_LIB
CONFIG_MCUBOOT_BOOTUTIL_LIB_FOR_REVERT
CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE
CONFIG_MCUBOOT_BOOTLOADER_NO_DOWNGRADE
```

**弱选择（Implies）**

```text
CONFIG_MCUBOOT_GENERATE_CONFIRMED_IMAGE
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:302`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L302)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 引导加载程序（bootloader）支持 → 板载 MCUboot 运行模式（operation mode） → 应用所假定的 MCUboot 运行模式（mode of operation）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_BOOTLOADER_MODE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE)、[`CONFIG_MCUBOOT_BOOTUTIL_LIB`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTUTIL_LIB)、[`CONFIG_MCUBOOT_BOOTUTIL_LIB_FOR_REVERT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTUTIL_LIB_FOR_REVERT)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE)、[`CONFIG_MCUBOOT_BOOTLOADER_NO_DOWNGRADE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_NO_DOWNGRADE)、[`CONFIG_MCUBOOT_GENERATE_CONFIRMED_IMAGE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_GENERATE_CONFIRMED_IMAGE)。

<a id="CONFIG_MCUBOOT_BOOTLOADER_MODE_FIRMWARE_UPDATER"></a>

## 205.9 `CONFIG_MCUBOOT_BOOTLOADER_MODE_FIRMWARE_UPDATER`

**提示（Prompt）**：MCUboot 已配置为固件更新程序模式（firmware updater mode）

**说明（Help）**

MCUboot 仅从 `slot0_partition` 启动主应用，但定义了进入 `slot1_partition` 的入口机制（entrance mechanism）。后者是专用的固件更新应用（firmware updater application），用于更新 `slot0_partition` 中的应用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUBOOT_BOOTLOADER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_MCUBOOT_IMGTOOL_OVERWRITE_ONLY
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:324`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L324)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 引导加载程序（bootloader）支持 → 板载 MCUboot 运行模式（operation mode） → 应用所假定的 MCUboot 运行模式（mode of operation）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_BOOTLOADER_MODE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE)、[`CONFIG_MCUBOOT_IMGTOOL_OVERWRITE_ONLY`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_IMGTOOL_OVERWRITE_ONLY)。

<a id="CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE"></a>

## 205.10 `CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

所选模式支持防降级（downgrade prevention），不允许切换到版本低于当前运行应用的应用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BOOTLOADER_MCUBOOT
```

**被选择（Selected by）**

```text
CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_OFFSET
CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_MOVE
CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_SCRATCH
CONFIG_MCUBOOT_BOOTLOADER_MODE_OVERWRITE_ONLY
CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD
CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT
CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP
CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT
CONFIG_MCUBOOT_BOOTLOADER_MODE_SINGLE_APP_RAM_LOAD
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:350`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L350)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 引导加载程序（bootloader）支持 → 板载 MCUboot 运行模式（operation mode）

**配置项引用（Symbol References）**：[`CONFIG_BOOTLOADER_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_BOOTLOADER_MCUBOOT)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_OFFSET`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_OFFSET)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_MOVE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_MOVE)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_SCRATCH`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_SCRATCH)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_OVERWRITE_ONLY`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_OVERWRITE_ONLY)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_SINGLE_APP_RAM_LOAD`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_SINGLE_APP_RAM_LOAD)。

<a id="CONFIG_MCUBOOT_BOOTLOADER_MODE_OVERWRITE_ONLY"></a>

## 205.11 `CONFIG_MCUBOOT_BOOTLOADER_MODE_OVERWRITE_ONLY`

**提示（Prompt）**：MCUboot 已配置为仅覆盖主槽位（overwrite primary slot）

**说明（Help）**

MCUboot 使用镜像次槽位（secondary slot）的内容覆盖主槽位（primary slot）。此模式不保留次槽位中的上一版本，因此无法回退。它支持 `MCUBOOT_BOOTLOADER_NO_DOWNGRADE`；启用防降级后，只有次槽位版本高于主槽位版本时才会覆盖。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUBOOT_BOOTLOADER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE
CONFIG_MCUBOOT_IMGTOOL_OVERWRITE_ONLY
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:239`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L239)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 引导加载程序（bootloader）支持 → 板载 MCUboot 运行模式（operation mode） → 应用所假定的 MCUboot 运行模式（mode of operation）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_BOOTLOADER_MODE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE)、[`CONFIG_MCUBOOT_IMGTOOL_OVERWRITE_ONLY`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_IMGTOOL_OVERWRITE_ONLY)。

<a id="CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD"></a>

## 205.12 `CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD`

**提示（Prompt）**：MCUboot 已配置为 RAM 加载模式（RAM LOAD）

**说明（Help）**

MCUboot 要求设备树（DT）中存在 `slot0_partition` 和 `slot1_partition`。此模式下，它选择版本号更高的镜像，将其复制到 RAM 并从 RAM 开始执行。镜像必须链接为从 RAM 执行，复制目标地址在运行 `imgtool` 时通过 `load-addr` 参数指定。由于无法换回较旧版本的应用，此选项自动选择 `MCUBOOT_BOOTLOADER_NO_DOWNGRADE`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUBOOT_BOOTLOADER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE
CONFIG_MCUBOOT_BOOTLOADER_NO_DOWNGRADE
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:252`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L252)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 引导加载程序（bootloader）支持 → 板载 MCUboot 运行模式（operation mode） → 应用所假定的 MCUboot 运行模式（mode of operation）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_BOOTLOADER_MODE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE)、[`CONFIG_MCUBOOT_BOOTLOADER_NO_DOWNGRADE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_NO_DOWNGRADE)。

<a id="CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT"></a>

## 205.13 `CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT`

**提示（Prompt）**：MCUboot 已配置为带回退的 RAM 加载（RAM LOAD with revert）

**说明（Help）**

MCUboot 要求设备树（DT）中存在 `slot0_partition` 和 `slot1_partition`。此模式下，它选择版本号更高的镜像，将其复制到 RAM 并从 RAM 开始执行。镜像必须链接为从 RAM 执行，复制目标地址在运行 `imgtool` 时通过 `load-addr` 参数指定。由于 MCUboot 会自动选择最高版本的应用启动，此选项自动选择 `MCUBOOT_BOOTLOADER_NO_DOWNGRADE`。不过，若已启动版本未将自身标记为已确认（confirmed），MCUboot 会选择旧版本。

只要应用被标记为下次启动时进行测试或永久启动，MCUboot 就会从任一槽位中选择版本更高的应用启动。标记为测试的应用必须在首次启动时自我确认，否则会被移除，MCUboot 将回退到先前获准的应用。注意：此模式下，MCUboot 不会启动缺少镜像头（image header）的应用，因此手动烧写的应用应标记为已确认。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUBOOT_BOOTLOADER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_MCUBOOT_BOOTUTIL_LIB_FOR_REVERT if CONFIG_MCUBOOT_BOOTUTIL_LIB
CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE
CONFIG_MCUBOOT_BOOTLOADER_NO_DOWNGRADE
```

**弱选择（Implies）**

```text
CONFIG_MCUBOOT_GENERATE_CONFIRMED_IMAGE
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:264`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L264)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 引导加载程序（bootloader）支持 → 板载 MCUboot 运行模式（operation mode） → 应用所假定的 MCUboot 运行模式（mode of operation）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_BOOTLOADER_MODE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE)、[`CONFIG_MCUBOOT_BOOTUTIL_LIB_FOR_REVERT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTUTIL_LIB_FOR_REVERT)、[`CONFIG_MCUBOOT_BOOTUTIL_LIB`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTUTIL_LIB)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE)、[`CONFIG_MCUBOOT_BOOTLOADER_NO_DOWNGRADE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_NO_DOWNGRADE)、[`CONFIG_MCUBOOT_GENERATE_CONFIRMED_IMAGE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_GENERATE_CONFIRMED_IMAGE)。

<a id="CONFIG_MCUBOOT_BOOTLOADER_MODE_SINGLE_APP"></a>

## 205.14 `CONFIG_MCUBOOT_BOOTLOADER_MODE_SINGLE_APP`

**提示（Prompt）**：MCUboot 已配置为单槽位执行（single slot execution）

**说明（Help）**

MCUboot 仅启动位于 `slot0_partition` 的应用，不关心其他槽位。此模式下，应用无法通过设备固件升级（DFU）将自身更新写入次槽位，所有更新都必须通过 MCUboot 串行恢复（serial recovery）完成。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUBOOT_BOOTLOADER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_MCUBOOT_IMGTOOL_OVERWRITE_ONLY
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:200`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L200)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 引导加载程序（bootloader）支持 → 板载 MCUboot 运行模式（operation mode） → 应用所假定的 MCUboot 运行模式（mode of operation）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_BOOTLOADER_MODE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE)、[`CONFIG_MCUBOOT_IMGTOOL_OVERWRITE_ONLY`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_IMGTOOL_OVERWRITE_ONLY)。

<a id="CONFIG_MCUBOOT_BOOTLOADER_MODE_SINGLE_APP_RAM_LOAD"></a>

## 205.15 `CONFIG_MCUBOOT_BOOTLOADER_MODE_SINGLE_APP_RAM_LOAD`

**提示（Prompt）**：MCUboot 已配置为单应用 RAM 加载模式（single app RAM load mode）

**说明（Help）**

MCUboot 可从任意位置将镜像加载到 RAM。此模式下，它将镜像复制到 RAM 并从 RAM 开始执行。镜像必须链接为从 RAM 执行，复制目标地址在运行 `imgtool` 时通过 `load-addr` 参数指定。虽然不直接使用 `slot0_partition`，但仍必须在设备树（DT）中定义该分区，因为需要用它获取待加载镜像大小的信息。由于无法换回较旧版本的应用，此选项自动选择 `MCUBOOT_BOOTLOADER_NO_DOWNGRADE`。事实上，此模式不支持任何交换操作（swap operations）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUBOOT_BOOTLOADER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE
CONFIG_MCUBOOT_BOOTLOADER_NO_DOWNGRADE
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:333`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L333)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 引导加载程序（bootloader）支持 → 板载 MCUboot 运行模式（operation mode） → 应用所假定的 MCUboot 运行模式（mode of operation）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_BOOTLOADER_MODE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE)、[`CONFIG_MCUBOOT_BOOTLOADER_NO_DOWNGRADE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_NO_DOWNGRADE)。

<a id="CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_SCRATCH"></a>

## 205.16 `CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_SCRATCH`

**提示（Prompt）**：MCUboot 已配置为使用暂存分区交换（swap using scratch）

**说明（Help）**

MCUboot 要求设备树（DT）中存在 `slot0_partition`、`slot1_partition` 和 `scratch_partition`，应用从 `slot0_partition` 启动。将应用从次槽位交换到主槽位时，`scratch_partition` 用作临时存储（temporary storage）。如果 MCUboot 构建时启用了 `MCUBOOT_DOWNGRADE_PREVENTION`，则还应选择 `MCUBOOT_BOOTLOADER_NO_DOWNGRADE`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUBOOT_BOOTLOADER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:227`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L227)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 引导加载程序（bootloader）支持 → 板载 MCUboot 运行模式（operation mode） → 应用所假定的 MCUboot 运行模式（mode of operation）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_BOOTLOADER_MODE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE)。

<a id="CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_MOVE"></a>

## 205.17 `CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_MOVE`

**提示（Prompt）**：MCUboot 已配置为使用移动方式交换（swap using move）

**说明（Help）**

MCUboot 要求设备树（DT）中存在 `slot0_partition` 和 `slot1_partition`，应用从 `slot0_partition` 启动。如果 MCUboot 构建时启用了 `MCUBOOT_DOWNGRADE_PREVENTION`，则还应选择 `MCUBOOT_BOOTLOADER_NO_DOWNGRADE`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUBOOT_BOOTLOADER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:218`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L218)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 引导加载程序（bootloader）支持 → 板载 MCUboot 运行模式（operation mode） → 应用所假定的 MCUboot 运行模式（mode of operation）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_BOOTLOADER_MODE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE)。

<a id="CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_OFFSET"></a>

## 205.18 `CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_OFFSET`

**提示（Prompt）**：MCUboot 已配置为使用偏移方式交换（swap using offset）

**说明（Help）**

MCUboot 要求设备树（DT）中存在 `slot0_partition` 和 `slot1_partition`，应用从 `slot0_partition` 启动。如果 MCUboot 构建时启用了 `MCUBOOT_DOWNGRADE_PREVENTION`，则还应选择 `MCUBOOT_BOOTLOADER_NO_DOWNGRADE`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUBOOT_BOOTLOADER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:209`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L209)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 引导加载程序（bootloader）支持 → 板载 MCUboot 运行模式（operation mode） → 应用所假定的 MCUboot 运行模式（mode of operation）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_BOOTLOADER_MODE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE)。

<a id="CONFIG_MCUBOOT_BOOTLOADER_NO_DOWNGRADE"></a>

## 205.19 `CONFIG_MCUBOOT_BOOTLOADER_NO_DOWNGRADE`

**提示（Prompt）**：MCUboot 模式已启用防降级（downgrade prevention）

**说明（Help）**

所选 MCUboot 模式已启用防降级（downgrade prevention），不允许换回版本号更低的镜像。MCUboot 构建时启用了 `MCUBOOT_DOWNGRADE_PREVENTION` 选项时，应选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE && CONFIG_BOOTLOADER_MCUBOOT
```

**被选择（Selected by）**

```text
CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD
CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT
CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP
CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT
CONFIG_MCUBOOT_BOOTLOADER_MODE_SINGLE_APP_RAM_LOAD
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:357`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L357)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 引导加载程序（bootloader）支持 → 板载 MCUboot 运行模式（operation mode）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_HAS_NO_DOWNGRADE)、[`CONFIG_BOOTLOADER_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_BOOTLOADER_MCUBOOT)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_SINGLE_APP_RAM_LOAD`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_SINGLE_APP_RAM_LOAD)。

<a id="CONFIG_MCUBOOT_BOOTLOADER_SIGNATURE_TYPE_PURE"></a>

## 205.20 `CONFIG_MCUBOOT_BOOTLOADER_SIGNATURE_TYPE_PURE`

**提示（Prompt）**：针对镜像本身验证签名，而非针对镜像的 SHA

**说明（Help）**

MCUboot 已编译为使用纯签名验证（pure signature verification）来验证镜像，即针对镜像本身验证签名（signature），而不是针对镜像的 SHA 摘要验证。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BOOTLOADER_MCUBOOT
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:371`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L371)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 引导加载程序（bootloader）支持 → 板载 MCUboot 运行模式（operation mode）

**配置项引用（Symbol References）**：[`CONFIG_BOOTLOADER_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_BOOTLOADER_MCUBOOT)。

<a id="CONFIG_MCUBOOT_BOOTLOADER_USES_SHA512"></a>

## 205.21 `CONFIG_MCUBOOT_BOOTLOADER_USES_SHA512`

**提示（Prompt）**：MCUboot 使用 SHA512 计算镜像散列（image hash）

**说明（Help）**

MCUboot 已编译为使用 SHA512 验证镜像。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BOOTLOADER_MCUBOOT
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:366`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L366)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 引导加载程序（bootloader）支持 → 板载 MCUboot 运行模式（operation mode）

**配置项引用（Symbol References）**：[`CONFIG_BOOTLOADER_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_BOOTLOADER_MCUBOOT)。

<a id="CONFIG_MCUBOOT_BOOTUTIL_LIB"></a>

## 205.22 `CONFIG_MCUBOOT_BOOTUTIL_LIB`

**提示（Prompt）**：MCUboot 实用工具库（utility library）

**说明（Help）**

启用 MCUboot 实用工具库（utility library），实现链式加载应用（chain-loaded application）和 MCUboot 所需的函数。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT
CONFIG_MCUBOOT_IMG_MANAGER
CONFIG_MCUMGR_GRP_IMG_CLIENT
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:392`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L392)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT)、[`CONFIG_MCUBOOT_IMG_MANAGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUBOOT_IMG_MANAGER)、[`CONFIG_MCUMGR_GRP_IMG_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_GRP_IMG_CLIENT)。

<a id="CONFIG_MCUBOOT_BOOTUTIL_LIB_FOR_DIRECT_XIP"></a>

## 205.23 `CONFIG_MCUBOOT_BOOTUTIL_LIB_FOR_DIRECT_XIP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

增加在引导加载程序处于 DirectXIP 回退模式（DirectXIP-revert）时，将镜像设置为测试以及确认镜像（confirm images）的支持。此 Kconfig 已弃用，改用 `MCUBOOT_BOOTUTIL_LIB_FOR_REVERT`，因为后者也适用于带回退的 RAM 加载模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT && CONFIG_MCUBOOT_BOOTUTIL_LIB
```

**主动选择（Selects）**

```text
CONFIG_MCUBOOT_BOOTUTIL_LIB_FOR_REVERT
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:428`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L428)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 实用工具库（utility library）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT)、[`CONFIG_MCUBOOT_BOOTUTIL_LIB`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTUTIL_LIB)、[`CONFIG_MCUBOOT_BOOTUTIL_LIB_FOR_REVERT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTUTIL_LIB_FOR_REVERT)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_MCUBOOT_BOOTUTIL_LIB_FOR_REVERT"></a>

## 205.24 `CONFIG_MCUBOOT_BOOTUTIL_LIB_FOR_REVERT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

增加在引导加载程序处于带回退的直接原地执行（direct-xip with revert）或带回退的 RAM 加载（RAM load with revert）模式时，将镜像设置为测试以及确认镜像（confirm images）的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUBOOT_BOOTUTIL_LIB
```

**被选择（Selected by）**

```text
CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT
CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT
CONFIG_MCUBOOT_BOOTUTIL_LIB_FOR_DIRECT_XIP
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:420`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L420)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 实用工具库（utility library）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_BOOTUTIL_LIB`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTUTIL_LIB)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT)、[`CONFIG_MCUBOOT_BOOTUTIL_LIB_FOR_DIRECT_XIP`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTUTIL_LIB_FOR_DIRECT_XIP)。

<a id="CONFIG_MCUBOOT_BOOT_MAX_ALIGN"></a>

## 205.25 `CONFIG_MCUBOOT_BOOT_MAX_ALIGN`

**提示（Prompt）**：覆盖可编程闪存块对齐（programmable flash block alignment）

**说明（Help）**

允许覆盖可编程闪存块的对齐大小（alignment size）。默认取 chosen 节点 `zephyr,flash` 的写块大小（write block size）与 `8` 两者的最大值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUBOOT_BOOTUTIL_LIB
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:444`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L444)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 实用工具库（utility library）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_BOOTUTIL_LIB`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTUTIL_LIB)。

<a id="CONFIG_MCUBOOT_ENCRYPTION_ALG"></a>

## 205.26 `CONFIG_MCUBOOT_ENCRYPTION_ALG`

**提示（Prompt）**：用于镜像加密的算法（image encryption algorithm）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUBOOT_ENCRYPTION_KEY_FILE != "" && CONFIG_BOOTLOADER_MCUBOOT
```

**默认值（Defaults）**

```text
CONFIG_MCUBOOT_ENCRYPTION_ALG_AES_128
```

**可选项（Choices）**

```text
CONFIG_MCUBOOT_ENCRYPTION_ALG_AES_128
CONFIG_MCUBOOT_ENCRYPTION_ALG_AES_256
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 引导加载程序（bootloader）支持

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_ENCRYPTION_KEY_FILE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_ENCRYPTION_KEY_FILE)、[`CONFIG_BOOTLOADER_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_BOOTLOADER_MCUBOOT)、[`CONFIG_MCUBOOT_ENCRYPTION_ALG_AES_128`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_ENCRYPTION_ALG_AES_128)、[`CONFIG_MCUBOOT_ENCRYPTION_ALG_AES_256`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_ENCRYPTION_ALG_AES_256)。

<a id="CONFIG_MCUBOOT_ENCRYPTION_ALG_AES_128"></a>

## 205.27 `CONFIG_MCUBOOT_ENCRYPTION_ALG_AES_128`

**提示（Prompt）**：使用 AES-128 加密镜像

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUBOOT_ENCRYPTION_ALG>
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 引导加载程序（bootloader）支持 → 用于镜像加密的算法（image encryption algorithm）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_ENCRYPTION_ALG`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_ENCRYPTION_ALG)。

<a id="CONFIG_MCUBOOT_ENCRYPTION_ALG_AES_256"></a>

## 205.28 `CONFIG_MCUBOOT_ENCRYPTION_ALG_AES_256`

**提示（Prompt）**：使用 AES-256 加密镜像

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUBOOT_ENCRYPTION_ALG>
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 引导加载程序（bootloader）支持 → 用于镜像加密的算法（image encryption algorithm）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_ENCRYPTION_ALG`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_ENCRYPTION_ALG)。

<a id="CONFIG_MCUBOOT_ENCRYPTION_KEY_FILE"></a>

## 205.29 `CONFIG_MCUBOOT_ENCRYPTION_KEY_FILE`

**提示（Prompt）**：MCUboot 加密密钥文件路径（encryption key file path）

**说明（Help）**

此文件包含用于加密临时密钥（ephemeral key）的公钥（public key），临时密钥再用于加密镜像。对应私钥（private key）硬编码在 MCUboot 源码中，用于解密嵌入镜像的临时密钥。文件采用 PEM 格式。

设为非空值时，构建系统尝试使用 `west sign -t imgtool` 命令对最终二进制文件签名并加密。生成文件位于构建目录下的 `zephyr/zephyr.signed.encrypted.bin` 和 `zephyr/zephyr.signed.encrypted.hex`。可通过 `CONFIG_KERNEL_BIN_NAME` 自定义文件名。是否生成 bin 和 hex 文件分别取决于 `CONFIG_BUILD_OUTPUT_BIN` 和 `CONFIG_BUILD_OUTPUT_HEX`。

此选项允许绝对路径，也允许相对于 west 工作区顶层目录（workspace topdir）的路径。原文相对路径示例为 `./bootloader/mcuboot/enc-rsa2048-pub.pem`。留空时，必须手动加密 Zephyr 二进制文件。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUBOOT_SIGNATURE_KEY_FILE != "" && CONFIG_BOOTLOADER_MCUBOOT
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 引导加载程序（bootloader）支持

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_SIGNATURE_KEY_FILE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_SIGNATURE_KEY_FILE)、[`CONFIG_BOOTLOADER_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_BOOTLOADER_MCUBOOT)。

<a id="CONFIG_MCUBOOT_EXTRA_IMGTOOL_ARGS"></a>

## 205.30 `CONFIG_MCUBOOT_EXTRA_IMGTOOL_ARGS`

**提示（Prompt）**：签名时传给 imgtool 的额外参数（extra arguments）

**说明（Help）**

签名时，即 `CONFIG_MCUBOOT_SIGNATURE_KEY_FILE` 为非空字符串时，可使用此选项向 `imgtool` 传递额外选项。例如，可设为 `--version 1.2`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_BOOTLOADER_MCUBOOT
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:160`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L160)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 引导加载程序（bootloader）支持

**配置项引用（Symbol References）**：[`CONFIG_BOOTLOADER_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_BOOTLOADER_MCUBOOT)。

<a id="CONFIG_MCUBOOT_GENERATE_CONFIRMED_IMAGE"></a>

## 205.31 `CONFIG_MCUBOOT_GENERATE_CONFIRMED_IMAGE`

**提示（Prompt）**：同时生成已填充、已确认的镜像（padded, confirmed image）

**说明（Help）**

经过签名、填充（padded）并标记为已确认（confirmed）的二进制文件，位于构建目录下的 `zephyr/zephyr.signed.confirmed.bin` 和 `zephyr/zephyr.signed.confirmed.hex`。可通过 `CONFIG_KERNEL_BIN_NAME` 自定义文件名。是否生成 bin 和 hex 文件分别取决于 `CONFIG_BUILD_OUTPUT_BIN` 和 `CONFIG_BUILD_OUTPUT_HEX`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BOOTLOADER_MCUBOOT
```

**被弱选择（Implied by）**

```text
CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT
CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:177`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L177)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 引导加载程序（bootloader）支持

**配置项引用（Symbol References）**：[`CONFIG_BOOTLOADER_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_BOOTLOADER_MCUBOOT)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT)。

<a id="CONFIG_MCUBOOT_GENERATE_UNSIGNED_IMAGE"></a>

## 205.32 `CONFIG_MCUBOOT_GENERATE_UNSIGNED_IMAGE`

**提示（Prompt）**：生成可由 MCUboot 启动的未签名二进制镜像（unsigned binary image）

**说明（Help）**

启用后，未提供 MCUboot 签名密钥（signing key），即 `MCUBOOT_SIGNATURE_KEY_FILE` 留空时，也可自动生成未签名二进制镜像。此时生成镜像的散列值（hash），并将其放入未签名镜像中，替代签名。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BOOTLOADER_MCUBOOT
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:168`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L168)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 引导加载程序（bootloader）支持

**配置项引用（Symbol References）**：[`CONFIG_BOOTLOADER_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_BOOTLOADER_MCUBOOT)。

<a id="CONFIG_MCUBOOT_IMGTOOL_OVERWRITE_ONLY"></a>

## 205.33 `CONFIG_MCUBOOT_IMGTOOL_OVERWRITE_ONLY`

**提示（Prompt）**：使用仅覆盖升级（overwrite-only），而非交换升级（swap upgrades）

**说明（Help）**

启用后，将 `--overwrite-only` 选项传给 `imgtool`，避免在计算溢出（overflow）时计入交换状态区（swap status area）的大小。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BOOTLOADER_MCUBOOT
```

**被选择（Selected by）**

```text
CONFIG_MCUBOOT_BOOTLOADER_MODE_SINGLE_APP
CONFIG_MCUBOOT_BOOTLOADER_MODE_OVERWRITE_ONLY
CONFIG_MCUBOOT_BOOTLOADER_MODE_FIRMWARE_UPDATER
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:120`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L120)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 引导加载程序（bootloader）支持

**配置项引用（Symbol References）**：[`CONFIG_BOOTLOADER_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_BOOTLOADER_MCUBOOT)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_SINGLE_APP`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_SINGLE_APP)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_OVERWRITE_ONLY`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_OVERWRITE_ONLY)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_FIRMWARE_UPDATER`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_FIRMWARE_UPDATER)。

<a id="CONFIG_MCUBOOT_IMGTOOL_SIGN_VERSION"></a>

## 205.34 `CONFIG_MCUBOOT_IMGTOOL_SIGN_VERSION`

**提示（Prompt）**：签名时传给 imgtool 的版本号（version）

**说明（Help）**

使用 `imgtool` 签名时，将此设置作为版本参数传给工具。格式为 `major.minor.revision+build`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_BOOTLOADER_MCUBOOT
```

**默认值（Defaults）**

```text
"" if "" != ""
"0.0.0+0"
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 引导加载程序（bootloader）支持

**配置项引用（Symbol References）**：[`CONFIG_BOOTLOADER_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_BOOTLOADER_MCUBOOT)。

<a id="CONFIG_MCUBOOT_IMGTOOL_UUID_CID"></a>

## 205.35 `CONFIG_MCUBOOT_IMGTOOL_UUID_CID`

**提示（Prompt）**：附加镜像类别唯一标识符 TLV（image class unique identifier TLV）

**说明（Help）**

启用后，向 `imgtool` 传递 `--cid` 选项，其值由 `MCUBOOT_IMGTOOL_UUID_CID_NAME` 设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BOOTLOADER_MCUBOOT
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:142`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L142)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 引导加载程序（bootloader）支持

**配置项引用（Symbol References）**：[`CONFIG_BOOTLOADER_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_BOOTLOADER_MCUBOOT)。

<a id="CONFIG_MCUBOOT_IMGTOOL_UUID_CID_NAME"></a>

## 205.36 `CONFIG_MCUBOOT_IMGTOOL_UUID_CID_NAME`

**提示（Prompt）**：镜像类别 UUID（Image class UUID）

**说明（Help）**

镜像类别唯一标识符（image class unique identifier），支持以下格式：

- 镜像类别名称（image class name），例如 `nRF5340_door_lock_btperipheral`。此格式要求定义 `MCUBOOT_IMGTOOL_UUID_VID_NAME`，因为厂商标识符（VID）的 UUID 用作镜像类别 UUID 的命名空间（namespace）。
- 原始 UUID，例如 `12345678-1234-5678-1234-567812345678`。
- 原始十六进制 UUID（HEX UUID），原文示例为 `12345678123456781234567812345678`。

译注：最后一个十六进制示例按原文保留，其字符数与去掉连字符后的标准 UUID 示例不同；不将其视为已验证的有效 UUID。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUBOOT_IMGTOOL_UUID_CID && CONFIG_BOOTLOADER_MCUBOOT
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:148`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L148)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 引导加载程序（bootloader）支持 → 附加镜像类别唯一标识符 TLV（image class unique identifier TLV）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_IMGTOOL_UUID_CID`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_IMGTOOL_UUID_CID)、[`CONFIG_BOOTLOADER_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_BOOTLOADER_MCUBOOT)。

<a id="CONFIG_MCUBOOT_IMGTOOL_UUID_VID"></a>

## 205.37 `CONFIG_MCUBOOT_IMGTOOL_UUID_VID`

**提示（Prompt）**：附加厂商唯一标识符 TLV（vendor unique identifier TLV）

**说明（Help）**

启用后，向 `imgtool` 传递 `--vid` 选项，其值由 `MCUBOOT_IMGTOOL_UUID_VID_NAME` 设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BOOTLOADER_MCUBOOT
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:126`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L126)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 引导加载程序（bootloader）支持

**配置项引用（Symbol References）**：[`CONFIG_BOOTLOADER_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_BOOTLOADER_MCUBOOT)。

<a id="CONFIG_MCUBOOT_IMGTOOL_UUID_VID_NAME"></a>

## 205.38 `CONFIG_MCUBOOT_IMGTOOL_UUID_VID_NAME`

**提示（Prompt）**：厂商 UUID（Vendor UUID）

**说明（Help）**

厂商唯一标识符（vendor unique identifier），支持以下格式：

- 域名（domain name），原文示例为 `amce.corp`。
- 原始 UUID，例如 `12345678-1234-5678-1234-567812345678`。
- 原始十六进制 UUID（HEX UUID），原文示例为 `12345678123456781234567812345678`。

译注：最后一个十六进制示例按原文保留，其字符数与去掉连字符后的标准 UUID 示例不同；不将其视为已验证的有效 UUID。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUBOOT_IMGTOOL_UUID_VID && CONFIG_BOOTLOADER_MCUBOOT
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:132`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L132)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 引导加载程序（bootloader）支持 → 附加厂商唯一标识符 TLV（vendor unique identifier TLV）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_IMGTOOL_UUID_VID`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_IMGTOOL_UUID_VID)、[`CONFIG_BOOTLOADER_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_BOOTLOADER_MCUBOOT)。

<a id="CONFIG_MCUBOOT_SIGNATURE_KEY_FILE"></a>

## 205.39 `CONFIG_MCUBOOT_SIGNATURE_KEY_FILE`

**提示（Prompt）**：MCUboot 签名密钥文件路径（signing key file path）

**说明（Help）**

此 PEM 格式文件包含一个密钥对（key pair），目标的 MCUboot 镜像使用其公钥部分进行验证。设为非空值时，构建系统尝试使用 `west sign -t imgtool` 命令为最终二进制文件签名。签名文件位于构建目录下的 `zephyr/zephyr.signed.bin` 和 `zephyr/zephyr.signed.hex`。可通过 `CONFIG_KERNEL_BIN_NAME` 自定义文件名。是否生成 bin 和 hex 文件分别取决于 `CONFIG_BUILD_OUTPUT_BIN` 和 `CONFIG_BUILD_OUTPUT_HEX`。

此选项应指向 MCUboot `.config` 中第一个 `BOOT_SIGNATURE_KEY_FILE` 选项所指向的同一文件。路径可以是绝对路径，也可以相对于 west 工作区顶层目录（workspace topdir）。MCUboot 配置项用于 MCUboot 引导加载程序镜像；此选项用于将由 MCUboot 加载的应用。MCUboot 配置项可使用相对于 MCUboot 仓库根目录的路径。

如果留空且未设置 `MCUBOOT_GENERATE_UNSIGNED_IMAGE`，则必须手动签名并准备 Zephyr 二进制文件，使 MCUboot 能够启动它们。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
!CONFIG_MCUBOOT_GENERATE_UNSIGNED_IMAGE && CONFIG_BOOTLOADER_MCUBOOT
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`modules/Kconfig.mcuboot:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.mcuboot#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 引导加载程序（bootloader）支持

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_GENERATE_UNSIGNED_IMAGE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_GENERATE_UNSIGNED_IMAGE)、[`CONFIG_BOOTLOADER_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_BOOTLOADER_MCUBOOT)。

<!-- kconfig-navigation -->

[上一章](P204_modules_Kconfig.libmetal_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P206_modules_Kconfig.microchip_配置项参考.md)
