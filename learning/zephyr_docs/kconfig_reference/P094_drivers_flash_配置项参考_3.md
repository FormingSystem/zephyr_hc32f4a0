---
id: learning.zephyr-docs.kconfig-reference.page-94
title: "`drivers/flash`配置项参考（3/3）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第94章\_`drivers/flash`配置项参考（3/3）

本章翻译官方 Kconfig 数据库中 `drivers/flash` 的 66 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SOC_FLASH_ITE_IT51XXX_M1K"></a>

## 94.1 `CONFIG_SOC_FLASH_ITE_IT51XXX_M1K`

**提示（Prompt）**：ITE IT51XXX 手动闪存 1K 驱动（Manual Flash 1K Driver）

**说明（Help）**

闪存 M1K 驱动支持读取（最多 1K）、写入（1K）和擦除（4K）操作。可访问的闪存区域包括内部 e-Flash，以及通过 `FSCE#` 或 `FSCE1#` 连接的外部 SPI 闪存。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT51XXX_MANUAL_FLASH_1K_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_PINCTRL
CONFIG_FLASH_HAS_EX_OP
```

**定义位置（Location）**：[`drivers/flash/Kconfig.it51xxx_m1k:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.it51xxx_m1k#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_FLASH_HAS_EX_OP`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EX_OP)。

<a id="CONFIG_SOC_FLASH_ITE_IT8XXX2"></a>

## 94.2 `CONFIG_SOC_FLASH_ITE_IT8XXX2`

**提示（Prompt）**：ITE IT8XXX2 闪存驱动（Flash Driver）

**说明（Help）**

此闪存驱动支持读取、写入和擦除操作，也支持保护（Protection）。IT8XXX2 闪存大小为 1M 字节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT8XXX2_FLASH_CONTROLLER_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SOC_IT51XXX_USE_ILM if CONFIG_SOC_SERIES_IT51XXX
CONFIG_SOC_IT8XXX2_USE_ILM if CONFIG_SOC_SERIES_IT8XXX2
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_HAS_FLASH_LOAD_OFFSET
```

**定义位置（Location）**：[`drivers/flash/Kconfig.it8xxx2:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.it8xxx2#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_SOC_IT51XXX_USE_ILM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT51XXX_USE_ILM)、[`CONFIG_SOC_SERIES_IT51XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IT51XXX)、[`CONFIG_SOC_IT8XXX2_USE_ILM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT8XXX2_USE_ILM)、[`CONFIG_SOC_SERIES_IT8XXX2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IT8XXX2)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_HAS_FLASH_LOAD_OFFSET`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_HAS_FLASH_LOAD_OFFSET)。

<a id="CONFIG_SOC_FLASH_LPC"></a>

## 94.3 `CONFIG_SOC_FLASH_LPC`

**提示（Prompt）**：LPC 闪存适配层驱动（Flash Shim Driver）

**说明（Help）**

启用 LPC 在应用编程（IAP）闪存适配层驱动（Flash Shim Driver）。**警告**：此驱动在闪存擦除/写入操作期间禁用系统中断（System Interrupts）。这会影响整体系统性能，是否可接受取决于使用场景。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_NXP_IAP_FMC11_ENABLED || DT_HAS_NXP_IAP_FMC54_ENABLED) && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
```

**定义位置（Location）**：[`drivers/flash/Kconfig.lpc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.lpc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)。

<a id="CONFIG_SOC_FLASH_MAX32"></a>

## 94.4 `CONFIG_SOC_FLASH_MAX32`

**提示（Prompt）**：ADI MAX32 闪存驱动（Flash Driver）

**说明（Help）**

启用 MAX32 内部闪存驱动（Internal Flash Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX32_FLASH_CONTROLLER_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_FLASH_HAS_PAGE_LAYOUT
```

**定义位置（Location）**：[`drivers/flash/Kconfig.max32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.max32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)。

<a id="CONFIG_SOC_FLASH_MCUX"></a>

## 94.5 `CONFIG_SOC_FLASH_MCUX`

**提示（Prompt）**：MCUX 闪存适配层驱动（Flash Shim Driver）

**说明（Help）**

启用 MCUX 闪存适配层驱动（Flash Shim Driver）。**警告**：此驱动在闪存擦除/写入操作期间禁用系统中断（System Interrupts）。这会影响整体系统性能，是否可接受取决于使用场景。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_NXP_KINETIS_FTFA_ENABLED || DT_HAS_NXP_KINETIS_FTFE_ENABLED || DT_HAS_NXP_KINETIS_FTFL_ENABLED || DT_HAS_NXP_KINETIS_FTFC_ENABLED || DT_HAS_NXP_IAP_FMC55_ENABLED || DT_HAS_NXP_IAP_FMC553_ENABLED || DT_HAS_NXP_MSF1_ENABLED) && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_MPU_ALLOW_FLASH_WRITE if CONFIG_ARM_MPU
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mcux:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mcux#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_MPU_ALLOW_FLASH_WRITE`](P030_arch_arm_配置项参考_2.md#CONFIG_MPU_ALLOW_FLASH_WRITE)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)。

<a id="CONFIG_SOC_FLASH_MCUX_C40"></a>

## 94.6 `CONFIG_SOC_FLASH_MCUX_C40`

**提示（Prompt）**：MCUX C40 闪存驱动（Flash Driver）

**说明（Help）**

启用 NXP MCUX C40 内部闪存驱动，使用 MCUX C40 硬件抽象层（HAL）提供 Zephyr 闪存驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_C40_FLASH_CONTROLLER_ENABLED && DT_HAS_NXP_C40_FLASH_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_FLASH_HAS_PAGE_LAYOUT
```

**弱选择（Implies）**

```text
CONFIG_CODE_DATA_RELOCATION if CONFIG_XIP
CONFIG_CODE_DATA_RELOCATION_SRAM if CONFIG_XIP
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mcux:205`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mcux#L205)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_CODE_DATA_RELOCATION`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CODE_DATA_RELOCATION)、[`CONFIG_XIP`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XIP)、[`CONFIG_CODE_DATA_RELOCATION_SRAM`](P029_arch_arm_配置项参考_1.md#CONFIG_CODE_DATA_RELOCATION_SRAM)。

<a id="CONFIG_SOC_FLASH_MCUX_C40_APPLY_PROTECTION"></a>

## 94.7 `CONFIG_SOC_FLASH_MCUX_C40_APPLY_PROTECTION`

**提示（Prompt）**：初始化时应用默认保护窗口（Protection Windows，IVT/MCUboot）

**说明（Help）**

启用后，驱动在初始化期间，根据设备树（Devicetree）派生的已知区域（例如 `ivt_header`、`ivt_pad`、`mcuboot`）锁定或解除保护。对于原地执行（XIP）系统，可用它保持 IVT/引导加载程序（Bootloader）区域只读。如果引导加载程序或系统策略自行管理这些保护，则禁用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FLASH_MCUX_C40 && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y if CONFIG_XIP
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mcux:222`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mcux#L222)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → MCUX C40 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_MCUX_C40`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_MCUX_C40)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_XIP`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XIP)。

<a id="CONFIG_SOC_FLASH_NRF"></a>

## 94.8 `CONFIG_SOC_FLASH_NRF`

**提示（Prompt）**：Nordic Semiconductor nRF 闪存驱动（Flash Driver）

**说明（Help）**

启用 Nordic Semiconductor nRF 闪存驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_NORDIC_NRF51_FLASH_CONTROLLER_ENABLED || DT_HAS_NORDIC_NRF52_FLASH_CONTROLLER_ENABLED || DT_HAS_NORDIC_NRF53_FLASH_CONTROLLER_ENABLED || DT_HAS_NORDIC_NRF91_FLASH_CONTROLLER_ENABLED) && !CONFIG_FLASH_NRF_FORCE_ALT && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_NRFX_NVMC
CONFIG_MPU_ALLOW_FLASH_WRITE if CONFIG_ARM_MPU
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nrf:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nrf#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_NRF_FORCE_ALT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_NRF_FORCE_ALT)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_NRFX_NVMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_NVMC)、[`CONFIG_MPU_ALLOW_FLASH_WRITE`](P030_arch_arm_配置项参考_2.md#CONFIG_MPU_ALLOW_FLASH_WRITE)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)。

<a id="CONFIG_SOC_FLASH_NRF_CUSTOM_CONTEXT"></a>

## 94.9 `CONFIG_SOC_FLASH_NRF_CUSTOM_CONTEXT`

**提示（Prompt）**：Nordic nRFx 闪存驱动操作自定义上下文（Custom Context）

**说明（Help）**

启用指向自定义上下文（Custom Context）的指针，供需要存储现有结构体未涵盖的额外数据的驱动使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_COMPATIBLE_NRF && CONFIG_SOC_FLASH_NRF && CONFIG_FLASH
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nrf:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nrf#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Nordic Semiconductor nRF 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_COMPATIBLE_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF)、[`CONFIG_SOC_FLASH_NRF`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF`。

<a id="CONFIG_SOC_FLASH_NRF_EMULATE_ONE_BYTE_WRITE_ACCESS"></a>

## 94.10 `CONFIG_SOC_FLASH_NRF_EMULATE_ONE_BYTE_WRITE_ACCESS`

**提示（Prompt）**：8 位写块大小仿真（Write Block Size Emulation）

**说明（Help）**

启用此选项后，可以写入小于厂商规定的最小写块大小（Minimum Write Block Size）的数据块，但操作更复杂，需要用户具备非易失性存储器控制器（NVMC）的基本知识。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FLASH_NRF && CONFIG_FLASH
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nrf:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nrf#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Nordic Semiconductor nRF 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_NRF`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_SOC_FLASH_NRF_MRAM"></a>

## 94.11 `CONFIG_SOC_FLASH_NRF_MRAM`

**提示（Prompt）**：Nordic Semiconductor 用于 MRAM 的闪存驱动（Flash Driver）

**说明（Help）**

启用 Nordic Semiconductor 用于直接写入模式（Direct Write Mode）MRAM 的闪存驱动。MRAM 字（Word）在写入时自动擦除，但写入预先擦除的区域更快。因此，擦除 API 不是必需的，不过某些场景可通过它将擦除开销提前分摊，改善写入性能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_MRAM_ENABLED && CONFIG_HAS_NRFX && !CONFIG_RISCV_CORE_NORDIC_VPR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE
```

**弱选择（Implies）**

```text
CONFIG_NRFS
CONFIG_MRAM_LATENCY
CONFIG_MPU_ALLOW_FLASH_WRITE if CONFIG_ARM_MPU
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nrf_mram:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nrf_mram#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_RISCV_CORE_NORDIC_VPR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_CORE_NORDIC_VPR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE)、[`CONFIG_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS)、[`CONFIG_MRAM_LATENCY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MRAM_LATENCY)、[`CONFIG_MPU_ALLOW_FLASH_WRITE`](P030_arch_arm_配置项参考_2.md#CONFIG_MPU_ALLOW_FLASH_WRITE)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_SOC_FLASH_NRF_MRAMC"></a>

## 94.12 `CONFIG_SOC_FLASH_NRF_MRAMC`

**提示（Prompt）**：Nordic Semiconductor 使用 MRAM 控制器（MRAM Controller）的 MRAM 闪存驱动

**说明（Help）**

启用 Nordic Semiconductor 用于直接写入模式（Direct Write Mode）MRAMC 的闪存驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_MRAMC_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE
```

**弱选择（Implies）**

```text
CONFIG_NRFX_MRAMC if !CONFIG_BUILD_WITH_TFM
CONFIG_MPU_ALLOW_FLASH_WRITE if CONFIG_ARM_MPU
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nrf_mramc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nrf_mramc#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE)、[`CONFIG_NRFX_MRAMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_MRAMC)、[`CONFIG_BUILD_WITH_TFM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_WITH_TFM)、[`CONFIG_MPU_ALLOW_FLASH_WRITE`](P030_arch_arm_配置项参考_2.md#CONFIG_MPU_ALLOW_FLASH_WRITE)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)。

<a id="CONFIG_SOC_FLASH_NRF_PARTIAL_ERASE"></a>

## 94.13 `CONFIG_SOC_FLASH_NRF_PARTIAL_ERASE`

**提示（Prompt）**：Nordic nRFx 闪存驱动部分擦除（Partial Erase）

**说明（Help）**

启用部分擦除（Partial Erase）功能。部分擦除以时间片（Time Slice）执行，避免 MCU 在给定区域整个擦除操作期间一直阻塞，使 MCU 能在各次操作之间中断擦除去执行其他任务。启用 `SOC_FLASH_NRF_RADIO_SYNC_TICKER` 构建时，此功能也可改善闪存擦除操作与蓝牙（Bluetooth）之间的同步。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_NVMC_PE && CONFIG_SOC_FLASH_NRF && CONFIG_FLASH
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nrf:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nrf#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Nordic Semiconductor nRF 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_NVMC_PE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_NVMC_PE)、[`CONFIG_SOC_FLASH_NRF`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_NVMC_PE`。

<a id="CONFIG_SOC_FLASH_NRF_PARTIAL_ERASE_MS"></a>

## 94.14 `CONFIG_SOC_FLASH_NRF_PARTIAL_ERASE_MS`

**提示（Prompt）**：部分擦除超时时间（Partial Erase Timeout），以毫秒为单位

**说明（Help）**

NVMC 每次擦除部分闪存后停止、让 CPU 恢复执行之前允许使用的最长时间，以毫秒为单位。最小超时时间为 2 ms；最大值不应超过将 `FLASH_PAGE_ERASE_MAX_TIME_US` 换算成毫秒后的一半。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FLASH_NRF_PARTIAL_ERASE && CONFIG_SOC_FLASH_NRF && CONFIG_FLASH
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nrf:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nrf#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Nordic Semiconductor nRF 闪存驱动（Flash Driver） → Nordic nRFx 闪存驱动部分擦除（Partial Erase）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_NRF_PARTIAL_ERASE`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_PARTIAL_ERASE)、[`CONFIG_SOC_FLASH_NRF`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_SOC_FLASH_NRF_RADIO_SYNC_CHOICE"></a>

## 94.15 `CONFIG_SOC_FLASH_NRF_RADIO_SYNC_CHOICE`

原库同名定义共 2 条；本项为数据库第 17504 条记录，各定义分别保留。

**提示（Prompt）**：Nordic nRFx 闪存驱动同步（Synchronization）

**说明（Help）**

闪存驱动与无线电（Radio）之间的同步（Synchronization）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FLASH_NRF && CONFIG_FLASH
```

**默认值（Defaults）**

```text
CONFIG_SOC_FLASH_NRF_RADIO_SYNC_TICKER if CONFIG_BT_LL_SW_SPLIT
CONFIG_SOC_FLASH_NRF_RADIO_SYNC_NONE
```

**可选项（Choices）**

```text
CONFIG_SOC_FLASH_NRF_RADIO_SYNC_TICKER
CONFIG_SOC_FLASH_NRF_RADIO_SYNC_NONE
CONFIG_SOC_FLASH_NRF_RADIO_SYNC_TICKER
CONFIG_SOC_FLASH_NRF_RADIO_SYNC_NONE
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nrf:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nrf#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Nordic Semiconductor nRF 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_NRF`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_SOC_FLASH_NRF_RADIO_SYNC_TICKER`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_RADIO_SYNC_TICKER)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_SOC_FLASH_NRF_RADIO_SYNC_NONE`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_RADIO_SYNC_NONE)。

<a id="CONFIG_SOC_FLASH_NRF_RADIO_SYNC_CHOICE--record-17505"></a>

## 94.16 `CONFIG_SOC_FLASH_NRF_RADIO_SYNC_CHOICE`

原库同名定义共 2 条；本项为数据库第 17505 条记录，各定义分别保留。

**提示（Prompt）**：Nordic nRFx 闪存驱动同步（Synchronization）

**说明（Help）**

闪存驱动与无线电（Radio）之间的同步（Synchronization）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FLASH_NRF_RRAM && CONFIG_FLASH
```

**默认值（Defaults）**

```text
CONFIG_SOC_FLASH_NRF_RADIO_SYNC_TICKER if CONFIG_BT_LL_SW_SPLIT
CONFIG_SOC_FLASH_NRF_RADIO_SYNC_NONE
```

**可选项（Choices）**

```text
CONFIG_SOC_FLASH_NRF_RADIO_SYNC_TICKER
CONFIG_SOC_FLASH_NRF_RADIO_SYNC_NONE
CONFIG_SOC_FLASH_NRF_RADIO_SYNC_TICKER
CONFIG_SOC_FLASH_NRF_RADIO_SYNC_NONE
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nrf_rram:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nrf_rram#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Nordic Semiconductor 用于 nRF RRAM 的闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_NRF_RRAM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_RRAM)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_SOC_FLASH_NRF_RADIO_SYNC_TICKER`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_RADIO_SYNC_TICKER)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_SOC_FLASH_NRF_RADIO_SYNC_NONE`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_RADIO_SYNC_NONE)。

<a id="CONFIG_SOC_FLASH_NRF_RADIO_SYNC_NONE"></a>

## 94.17 `CONFIG_SOC_FLASH_NRF_RADIO_SYNC_NONE`

原库同名定义共 2 条；本项为数据库第 17506 条记录，各定义分别保留。

**提示（Prompt）**：无（None）

**说明（Help）**

禁用闪存驱动与无线电（Radio）之间的同步（Synchronization）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SOC_FLASH_NRF_RADIO_SYNC_CHOICE>
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nrf:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nrf#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Nordic Semiconductor nRF 闪存驱动（Flash Driver） → Nordic nRFx 闪存驱动同步（Synchronization）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_NRF_RADIO_SYNC_CHOICE`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_RADIO_SYNC_CHOICE)。

<a id="CONFIG_SOC_FLASH_NRF_RADIO_SYNC_NONE--record-17507"></a>

## 94.18 `CONFIG_SOC_FLASH_NRF_RADIO_SYNC_NONE`

原库同名定义共 2 条；本项为数据库第 17507 条记录，各定义分别保留。

**提示（Prompt）**：无（None）

**说明（Help）**

禁用闪存驱动与无线电（Radio）之间的同步（Synchronization）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SOC_FLASH_NRF_RADIO_SYNC_CHOICE>
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nrf_rram:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nrf_rram#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Nordic Semiconductor 用于 nRF RRAM 的闪存驱动（Flash Driver） → Nordic nRFx 闪存驱动同步（Synchronization）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_NRF_RADIO_SYNC_CHOICE`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_RADIO_SYNC_CHOICE)。

<a id="CONFIG_SOC_FLASH_NRF_RADIO_SYNC_TICKER"></a>

## 94.19 `CONFIG_SOC_FLASH_NRF_RADIO_SYNC_TICKER`

原库同名定义共 2 条；本项为数据库第 17508 条记录，各定义分别保留。

**提示（Prompt）**：Nordic nRFx 闪存驱动与无线电同步（Radio Synchronization）

**说明（Help）**

使用低功耗蓝牙链路层（Bluetooth LE LL）控制器的 ticker API，启用闪存驱动与无线电（Radio）之间的同步。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && <choice CONFIG_SOC_FLASH_NRF_RADIO_SYNC_CHOICE>
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nrf:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nrf#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Nordic Semiconductor nRF 闪存驱动（Flash Driver） → Nordic nRFx 闪存驱动同步（Synchronization）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_SOC_FLASH_NRF_RADIO_SYNC_CHOICE`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_RADIO_SYNC_CHOICE)。

<a id="CONFIG_SOC_FLASH_NRF_RADIO_SYNC_TICKER--record-17509"></a>

## 94.20 `CONFIG_SOC_FLASH_NRF_RADIO_SYNC_TICKER`

原库同名定义共 2 条；本项为数据库第 17509 条记录，各定义分别保留。

**提示（Prompt）**：Nordic nRFx 闪存驱动与无线电同步（Radio Synchronization）

**说明（Help）**

使用低功耗蓝牙链路层（Bluetooth LE LL）控制器的 ticker API，启用闪存驱动与无线电（Radio）之间的同步。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_LL_SW_SPLIT && <choice CONFIG_SOC_FLASH_NRF_RADIO_SYNC_CHOICE>
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nrf_rram:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nrf_rram#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Nordic Semiconductor 用于 nRF RRAM 的闪存驱动（Flash Driver） → Nordic nRFx 闪存驱动同步（Synchronization）

**配置项引用（Symbol References）**：[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_SOC_FLASH_NRF_RADIO_SYNC_CHOICE`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_RADIO_SYNC_CHOICE)。

<a id="CONFIG_SOC_FLASH_NRF_RRAM"></a>

## 94.21 `CONFIG_SOC_FLASH_NRF_RRAM`

**提示（Prompt）**：Nordic Semiconductor 用于 nRF RRAM 的闪存驱动（Flash Driver）

**说明（Help）**

启用 Nordic Semiconductor 用于 nRF RRAM 控制器的闪存驱动。整个连续的 RRAM 块在逻辑上被划分为页（Page），但始终支持部分擦除（Partial Erase）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_RRAM_CONTROLLER_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_RRAMC if !CONFIG_BUILD_WITH_TFM
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_DRIVER_FILL
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE
CONFIG_FLASH_NRF_FORCE_ALT
CONFIG_MPU_ALLOW_FLASH_WRITE if CONFIG_ARM_MPU
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nrf_rram:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nrf_rram#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_NRFX_RRAMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_RRAMC)、[`CONFIG_BUILD_WITH_TFM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_WITH_TFM)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_DRIVER_FILL`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_FILL)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE)、[`CONFIG_FLASH_NRF_FORCE_ALT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_NRF_FORCE_ALT)、[`CONFIG_MPU_ALLOW_FLASH_WRITE`](P030_arch_arm_配置项参考_2.md#CONFIG_MPU_ALLOW_FLASH_WRITE)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)。

<a id="CONFIG_SOC_FLASH_NRF_THROTTLING"></a>

## 94.22 `CONFIG_SOC_FLASH_NRF_THROTTLING`

**提示（Prompt）**：Nordic nRFx 闪存写操作节流（Write Throttling）

**说明（Help）**

为闪存写操作启用节流（Throttling），避免闪存控制器（Flash Memory Controller）过载。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FLASH_NRF_RRAM && CONFIG_FLASH
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nrf_rram:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nrf_rram#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Nordic Semiconductor 用于 nRF RRAM 的闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_NRF_RRAM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_RRAM)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_SOC_FLASH_NRF_TIMEOUT_MULTIPLIER"></a>

## 94.23 `CONFIG_SOC_FLASH_NRF_TIMEOUT_MULTIPLIER`

原库同名定义共 2 条；本项为数据库第 17512 条记录，各定义分别保留。

**提示（Prompt）**：闪存操作超时时间倍数（Timeout Multiplier）【×0.1】

**说明（Help）**

此倍数先除以 `10`，再应用于闪存擦除和写入操作的超时时间。相乘的基础超时时间足以在阻塞模式（Blocking Mode）下擦除全部 nRF 闪存页。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_SOC_FLASH_NRF_RADIO_SYNC_NONE && CONFIG_SOC_FLASH_NRF && CONFIG_FLASH
```

**默认值（Defaults）**

```text
15 if CONFIG_SOC_FLASH_NRF_PARTIAL_ERASE && CONFIG_SOC_FLASH_NRF_RADIO_SYNC_TICKER
10
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nrf:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nrf#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Nordic Semiconductor nRF 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_NRF_RADIO_SYNC_NONE`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_RADIO_SYNC_NONE)、[`CONFIG_SOC_FLASH_NRF`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_SOC_FLASH_NRF_PARTIAL_ERASE`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_PARTIAL_ERASE)、[`CONFIG_SOC_FLASH_NRF_RADIO_SYNC_TICKER`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_RADIO_SYNC_TICKER)。

<a id="CONFIG_SOC_FLASH_NRF_TIMEOUT_MULTIPLIER--record-17513"></a>

## 94.24 `CONFIG_SOC_FLASH_NRF_TIMEOUT_MULTIPLIER`

原库同名定义共 2 条；本项为数据库第 17513 条记录，各定义分别保留。

**提示（Prompt）**：闪存操作超时时间倍数（Timeout Multiplier）【×0.1】

**说明（Help）**

此倍数先除以 `10`，再应用于闪存擦除和写入操作的超时时间。相乘的基础超时时间足以在阻塞模式（Blocking Mode）下擦除全部 nRF 闪存页。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_SOC_FLASH_NRF_RADIO_SYNC_NONE && CONFIG_SOC_FLASH_NRF_RRAM && CONFIG_FLASH
```

**默认值（Defaults）**

```text
15
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nrf_rram:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nrf_rram#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Nordic Semiconductor 用于 nRF RRAM 的闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_NRF_RADIO_SYNC_NONE`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_RADIO_SYNC_NONE)、[`CONFIG_SOC_FLASH_NRF_RRAM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_RRAM)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_SOC_FLASH_NRF_UICR"></a>

## 94.25 `CONFIG_SOC_FLASH_NRF_UICR`

**提示（Prompt）**：访问用户信息配置寄存器（UICR）

**说明（Help）**

启用对用户信息配置寄存器（UICR）的操作。启用后，可像普通闪存一样读取和写入 UICR。擦除只能一次对整个 UICR 进行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_TRUSTED_EXECUTION_NONSECURE && CONFIG_SOC_FLASH_NRF && CONFIG_FLASH
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nrf:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nrf#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Nordic Semiconductor nRF 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_TRUSTED_EXECUTION_NONSECURE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRUSTED_EXECUTION_NONSECURE)、[`CONFIG_SOC_FLASH_NRF`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_SOC_FLASH_NUMAKER"></a>

## 94.26 `CONFIG_SOC_FLASH_NUMAKER`

**提示（Prompt）**：新唐（Nuvoton）NuMaker 微控制器（MCU）闪存驱动

**说明（Help）**

此选项启用新唐（Nuvoton）NuMaker 系列处理器的闪存控制器（FMC）驱动。如需启用 NuMaker FMC，请选择 `y`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NUMAKER_FMC_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_HAS_NUMAKER_FMC
```

**定义位置（Location）**：[`drivers/flash/Kconfig.numaker:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.numaker#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_HAS_NUMAKER_FMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NUMAKER_FMC)。

<a id="CONFIG_SOC_FLASH_NUMAKER_RMC"></a>

## 94.27 `CONFIG_SOC_FLASH_NUMAKER_RMC`

**提示（Prompt）**：新唐（Nuvoton）NuMaker 微控制器（MCU）嵌入式 RRAM 控制器

**说明（Help）**

此选项启用新唐（Nuvoton）NuMaker 系列处理器的 RRAM 控制器（RMC）驱动。如需启用 NuMaker RMC，请选择 `y`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NUMAKER_RMC_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE
CONFIG_HAS_NUMAKER_RMC
```

**定义位置（Location）**：[`drivers/flash/Kconfig.numaker_rmc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.numaker_rmc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE)、[`CONFIG_HAS_NUMAKER_RMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NUMAKER_RMC)。

<a id="CONFIG_SOC_FLASH_RENESAS_RA_HP"></a>

## 94.28 `CONFIG_SOC_FLASH_RENESAS_RA_HP`

**提示（Prompt）**：RA 高性能闪存（Flash HP）驱动

**说明（Help）**

为 RA 系列启用高性能闪存驱动（Flash High-Performance Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_FLASH_HP_CONTROLLER_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_PAGE_LAYOUT
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_USE_RA_FSP_FLASH_HP
```

**定义位置（Location）**：[`drivers/flash/Kconfig.renesas_ra:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.renesas_ra#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_PAGE_LAYOUT`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_USE_RA_FSP_FLASH_HP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_FLASH_HP)。

<a id="CONFIG_SOC_FLASH_RENESAS_RA_LP"></a>

## 94.29 `CONFIG_SOC_FLASH_RENESAS_RA_LP`

**提示（Prompt）**：RA 低功耗闪存（Flash LP）驱动

**说明（Help）**

为 RA 系列启用低功耗闪存驱动（Flash Low-Power Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_FLASH_LP_CONTROLLER_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_PAGE_LAYOUT
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_USE_RA_FSP_FLASH_LP
```

**定义位置（Location）**：[`drivers/flash/Kconfig.renesas_ra:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.renesas_ra#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_PAGE_LAYOUT`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_USE_RA_FSP_FLASH_LP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_FLASH_LP)。

<a id="CONFIG_SOC_FLASH_RENESAS_RA_MRAM"></a>

## 94.30 `CONFIG_SOC_FLASH_RENESAS_RA_MRAM`

**提示（Prompt）**：RA FLASH MRAM 驱动

**说明（Help）**

为 RA 系列启用 FLASH MRAM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_MRAM_CONTROLLER_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_PAGE_LAYOUT
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE
CONFIG_MPU_ALLOW_FLASH_WRITE if CONFIG_ARM_MPU
CONFIG_USE_RA_FSP_MRAM
```

**定义位置（Location）**：[`drivers/flash/Kconfig.renesas_ra:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.renesas_ra#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_PAGE_LAYOUT`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE)、[`CONFIG_MPU_ALLOW_FLASH_WRITE`](P030_arch_arm_配置项参考_2.md#CONFIG_MPU_ALLOW_FLASH_WRITE)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)、[`CONFIG_USE_RA_FSP_MRAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_MRAM)。

<a id="CONFIG_SOC_FLASH_RENESAS_RX"></a>

## 94.31 `CONFIG_SOC_FLASH_RENESAS_RX`

**提示（Prompt）**：RX 闪存驱动（Flash Driver）

**说明（Help）**

RX 系列闪存驱动（Flash Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RX_FLASH_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_USE_RX_RDP_FLASH
```

**定义位置（Location）**：[`drivers/flash/Kconfig.renesas_rx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.renesas_rx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_USE_RX_RDP_FLASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RX_RDP_FLASH)。

<a id="CONFIG_SOC_FLASH_RTS5912"></a>

## 94.32 `CONFIG_SOC_FLASH_RTS5912`

**提示（Prompt）**：Realtek RTS5912 闪存驱动（Flash Driver）

**说明（Help）**

此闪存驱动支持读取、写入和擦除操作，也支持保护（Protection）。RTS5912 闪存大小为 960K 字节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_RTS5912_FLASH_CONTROLLER_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_FLASH_HAS_EX_OP
CONFIG_HAS_FLASH_LOAD_OFFSET
```

**定义位置（Location）**：[`drivers/flash/Kconfig.rts5912:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.rts5912#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_FLASH_HAS_EX_OP`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EX_OP)、[`CONFIG_HAS_FLASH_LOAD_OFFSET`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_HAS_FLASH_LOAD_OFFSET)。

<a id="CONFIG_SOC_FLASH_RV32M1"></a>

## 94.33 `CONFIG_SOC_FLASH_RV32M1`

**提示（Prompt）**：RV32M1 闪存适配层驱动（Flash Shim Driver）

**说明（Help）**

启用 RV32M1 闪存适配层驱动（Flash Shim Driver）。**警告**：此驱动在闪存擦除/写入操作期间禁用系统中断（System Interrupts）。这会影响整体系统性能，是否可接受取决于使用场景。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_OPENISA_RV32M1_FTFE_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
```

**定义位置（Location）**：[`drivers/flash/Kconfig.rv32m1:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.rv32m1#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)。

<a id="CONFIG_SOC_FLASH_SAM"></a>

## 94.34 `CONFIG_SOC_FLASH_SAM`

**提示（Prompt）**：Atmel SAM 闪存驱动（Flash Driver）

**说明（Help）**

启用 Atmel SAM 系列内部闪存驱动（Internal Flash Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM_FLASH_CONTROLLER_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_MPU_ALLOW_FLASH_WRITE if CONFIG_ARM_MPU
```

**定义位置（Location）**：[`drivers/flash/Kconfig.sam:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.sam#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_MPU_ALLOW_FLASH_WRITE`](P030_arch_arm_配置项参考_2.md#CONFIG_MPU_ALLOW_FLASH_WRITE)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)。

<a id="CONFIG_SOC_FLASH_SAM0"></a>

## 94.35 `CONFIG_SOC_FLASH_SAM0`

**提示（Prompt）**：Atmel SAM0 闪存驱动（Flash Driver）

**说明（Help）**

启用 Atmel SAM0 系列内部闪存驱动（Internal Flash Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM0_NVMCTRL_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_MPU_ALLOW_FLASH_WRITE if CONFIG_ARM_MPU
```

**定义位置（Location）**：[`drivers/flash/Kconfig.sam0:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.sam0#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_MPU_ALLOW_FLASH_WRITE`](P030_arch_arm_配置项参考_2.md#CONFIG_MPU_ALLOW_FLASH_WRITE)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)。

<a id="CONFIG_SOC_FLASH_SAM0_EMULATE_BYTE_PAGES"></a>

## 94.36 `CONFIG_SOC_FLASH_SAM0_EMULATE_BYTE_PAGES`

**提示（Prompt）**：仿真字节大小的页（Emulate Byte-Sized Pages）

**说明（Help）**

通过读/改/擦除/写（Read/Modify/Erase/Write）操作，仿真具有单字节大小页（Byte-Sized Page）的设备。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FLASH_SAM0 && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_SERIES_SAMC20 || CONFIG_SOC_SERIES_SAMC21
```

**定义位置（Location）**：[`drivers/flash/Kconfig.sam0:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.sam0#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Atmel SAM0 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_SAM0`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_SAM0)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_SOC_SERIES_SAMC20`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMC20)、[`CONFIG_SOC_SERIES_SAMC21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMC21)。

<a id="CONFIG_SOC_FLASH_SI32"></a>

## 94.37 `CONFIG_SOC_FLASH_SI32`

**提示（Prompt）**：Si32 闪存驱动（Flash Driver）

**说明（Help）**

启用 Si32 闪存驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SI32_FLASH_CONTROLLER_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_FLASH_HAS_PAGE_LAYOUT
```

**定义位置（Location）**：[`drivers/flash/Kconfig.si32:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.si32#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)。

<a id="CONFIG_SOC_FLASH_SILABS_S2"></a>

## 94.38 `CONFIG_SOC_FLASH_SILABS_S2`

**提示（Prompt）**：Silicon Labs Series 2 闪存驱动（Flash Driver）

**说明（Help）**

启用 Silicon Labs Series 2 内部闪存驱动（Internal Flash Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SERIES2_FLASH_CONTROLLER_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_SILABS_SISDK_MSC
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_MPU_ALLOW_FLASH_WRITE if CONFIG_ARM_MPU
```

**定义位置（Location）**：[`drivers/flash/Kconfig.silabs:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.silabs#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_SILABS_SISDK_MSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_MSC)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_MPU_ALLOW_FLASH_WRITE`](P030_arch_arm_配置项参考_2.md#CONFIG_MPU_ALLOW_FLASH_WRITE)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)。

<a id="CONFIG_SOC_FLASH_SILABS_S2_DMA_READ"></a>

## 94.39 `CONFIG_SOC_FLASH_SILABS_S2_DMA_READ`

**提示（Prompt）**：对闪存读取操作（Flash Read Operation）使用 DMA

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/flash/Kconfig.silabs:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.silabs#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Silicon Labs Series 2 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_SOC_FLASH_SILABS_S2_DMA_WRITE"></a>

## 94.40 `CONFIG_SOC_FLASH_SILABS_S2_DMA_WRITE`

**提示（Prompt）**：对闪存写入操作（Flash Write Operation）使用 DMA

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/flash/Kconfig.silabs:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.silabs#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Silicon Labs Series 2 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_SOC_FLASH_SILABS_S3_EXTMEM"></a>

## 94.41 `CONFIG_SOC_FLASH_SILABS_S3_EXTMEM`

**提示（Prompt）**：Silicon Labs Series 3 EXTMEM 闪存驱动（Flash Driver）

**说明（Help）**

启用 Silicon Labs Series 3 EXTMEM 闪存驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SERIES3_EXTMEM_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_SILABS_SISDK_SE
```

**定义位置（Location）**：[`drivers/flash/Kconfig.silabs:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.silabs#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_SILABS_SISDK_SE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_SE)。

<a id="CONFIG_SOC_FLASH_SILABS_SIWX91X"></a>

## 94.42 `CONFIG_SOC_FLASH_SILABS_SIWX91X`

**提示（Prompt）**：Silabs SiWx91x 闪存驱动（Flash Driver）

**说明（Help）**

启用 Silicon Labs SiWx91x 芯片内嵌闪存的闪存控制器（Flash Controller）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SIWX91X_FLASH_CONTROLLER_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_SILABS_SIWX91X_NWP
```

**定义位置（Location）**：[`drivers/flash/Kconfig.siwx91x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.siwx91x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_SILABS_SIWX91X_NWP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SIWX91X_NWP)。

<a id="CONFIG_SOC_FLASH_SMARTBOND"></a>

## 94.43 `CONFIG_SOC_FLASH_SMARTBOND`

**提示（Prompt）**：瑞萨（Renesas）SmartBond™ 闪存驱动（Flash Driver）

**说明（Help）**

启用瑞萨（Renesas）SmartBond™ 微控制器（MCU）系列的闪存驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_SMARTBOND_FLASH_CONTROLLER_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_MPU_ALLOW_FLASH_WRITE if CONFIG_ARM_MPU
```

**定义位置（Location）**：[`drivers/flash/Kconfig.smartbond:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.smartbond#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_MPU_ALLOW_FLASH_WRITE`](P030_arch_arm_配置项参考_2.md#CONFIG_MPU_ALLOW_FLASH_WRITE)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)。

<a id="CONFIG_SOC_FLASH_STM32"></a>

## 94.44 `CONFIG_SOC_FLASH_STM32`

**提示（Prompt）**：STM32 闪存驱动（Flash Driver）

**说明（Help）**

为 STM32 系列启用闪存驱动（Flash Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_FLASH_CONTROLLER_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_MPU_ALLOW_FLASH_WRITE if CONFIG_ARM_MPU
CONFIG_USE_STM32_HAL_FLASH if CONFIG_BT_STM32WBA
CONFIG_USE_STM32_HAL_FLASH_EX if CONFIG_BT_STM32WBA
```

**定义位置（Location）**：[`drivers/flash/Kconfig.stm32:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.stm32#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_MPU_ALLOW_FLASH_WRITE`](P030_arch_arm_配置项参考_2.md#CONFIG_MPU_ALLOW_FLASH_WRITE)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)、[`CONFIG_USE_STM32_HAL_FLASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_FLASH)、[`CONFIG_BT_STM32WBA`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_STM32WBA)、[`CONFIG_USE_STM32_HAL_FLASH_EX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_FLASH_EX)。

<a id="CONFIG_SOC_FLASH_TELINK_B91"></a>

## 94.45 `CONFIG_SOC_FLASH_TELINK_B91`

**提示（Prompt）**：泰凌半导体（Telink Semiconductor）B91 闪存驱动（Flash Driver）

**说明（Help）**

启用泰凌（Telink）B91 闪存驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TELINK_B91_FLASH_CONTROLLER_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
```

**定义位置（Location）**：[`drivers/flash/Kconfig.b91:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.b91#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)。

<a id="CONFIG_SOC_FLASH_XMC4XXX"></a>

## 94.46 `CONFIG_SOC_FLASH_XMC4XXX`

**提示（Prompt）**：XMC4XXX 闪存驱动（Flash Driver）

**说明（Help）**

启用 XMC4XXX 闪存驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_XMC4XXX_FLASH_CONTROLLER_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
```

**定义位置（Location）**：[`drivers/flash/Kconfig.xmc4xxx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.xmc4xxx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)。

<a id="CONFIG_SPI_FLASH_AT25XV021A"></a>

## 94.47 `CONFIG_SPI_FLASH_AT25XV021A`

**提示（Prompt）**：Atmel AT25 SPI 闪存变体（Flash Variant）

**说明（Help）**

启用 AT25XV021A SPI 闪存变体（Flash Variant）的支持。生产过这些变体的厂商包括：

- 瑞萨电子（Renesas Electronics）。
- Adesto Technologies。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_AT25XV021A_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/flash/Kconfig.at25xv021a:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.at25xv021a#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_SPI_FLASH_AT45"></a>

## 94.48 `CONFIG_SPI_FLASH_AT45`

**提示（Prompt）**：AT45 系列闪存驱动（Flash Driver）

**说明（Help）**

此驱动可处理多个 AT45 系列芯片实例。通过设备树（Devicetree）节点启用它们：将 `compatible` 属性设为 `atmel,at45`，并相应配置 JEDEC ID、芯片容量、块大小和页大小等其他必需属性。驱动仅支持这些芯片中为 2 的幂的二进制页大小（Binary Page Size），并在初始化时将芯片配置为该模式，除非此前已经完成配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_AT45_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/flash/Kconfig.at45:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.at45#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_SPI_FLASH_AT45_INIT_PRIORITY"></a>

## 94.49 `CONFIG_SPI_FLASH_AT45_INIT_PRIORITY`

**提示（Prompt）**：驱动初始化优先级（Driver Initialization Priority）

**说明（Help）**

设备驱动的初始化优先级（Initialization Priority）。SPI 驱动必须先于本驱动初始化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_FLASH_AT45 && CONFIG_FLASH
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/flash/Kconfig.at45:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.at45#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → AT45 系列闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SPI_FLASH_AT45`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_FLASH_AT45)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_SPI_FLASH_AT45_USE_READ_MODIFY_WRITE"></a>

## 94.50 `CONFIG_SPI_FLASH_AT45_USE_READ_MODIFY_WRITE`

**提示（Prompt）**：在 `flash_write()` 中使用读－改－写命令（Read-Modify-Write）

**说明（Help）**

使用读－改－写命令（Read-Modify-Write，操作码 `0x58`），代替默认的不含内置擦除的主存储器编程命令（Main Memory Program without Built-In Erase，操作码 `0x02`）。这样可以在未预先擦除相应页的情况下写入数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_FLASH_AT45 && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/flash/Kconfig.at45:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.at45#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → AT45 系列闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SPI_FLASH_AT45`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_FLASH_AT45)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_SPI_NAND"></a>

## 94.51 `CONFIG_SPI_NAND`

**提示（Prompt）**：SPI NAND 闪存（Flash）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_JEDEC_SPI_NAND_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EX_OP
CONFIG_SPI
CONFIG_CRC
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nand:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nand#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EX_OP`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EX_OP)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

<a id="CONFIG_SPI_NAND_BAD_BLOCK_CACHE"></a>

## 94.52 `CONFIG_SPI_NAND_BAD_BLOCK_CACHE`

**提示（Prompt）**：坏块缓存（Bad Block Cache）

**说明（Help）**

通过在内存中保留坏块表（Bad Block Table），启用坏块缓存（Bad Block Cache）。它能加快坏块检查，代价是略微增加内存用量。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_EX_OP_ENABLED && CONFIG_SPI_NAND && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nand:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nand#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → SPI NAND 闪存（Flash）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_EX_OP_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_EX_OP_ENABLED)、[`CONFIG_SPI_NAND`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_NAND)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_SPI_NAND_INIT_PRIORITY"></a>

## 94.53 `CONFIG_SPI_NAND_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动的初始化优先级（Initialization Priority）。设备连接在 SPI 总线上，必须在 SPI 驱动之后初始化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_NAND && CONFIG_FLASH
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nand:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nand#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → SPI NAND 闪存（Flash）

**配置项引用（Symbol References）**：[`CONFIG_SPI_NAND`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_NAND)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_SPI_NOR"></a>

## 94.54 `CONFIG_SPI_NOR`

**提示（Prompt）**：SPI NOR 闪存（Flash）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_JEDEC_SPI_NOR_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_JESD216
CONFIG_FLASH_HAS_EX_OP
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nor:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nor#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_JESD216`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_JESD216)、[`CONFIG_FLASH_HAS_EX_OP`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EX_OP)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_SPI_NOR_ACTIVE_DWELL_MS"></a>

## 94.55 `CONFIG_SPI_NOR_ACTIVE_DWELL_MS`

**提示（Prompt）**：最后一次使用后保持活动模式的停留时间（Dwell Period），以毫秒为单位

**说明（Help）**

闪存访问通常成批发生。如果每次访问之间都进入并退出深度掉电模式（Deep Power-Down，DPD），总操作时间会显著增加。此选项控制每次 API 调用后保持活动模式（Active Mode）的时长；如果下一次事务在停留时间（Dwell Period）结束前发生，就可省去“活动→空闲→活动”的状态转换过程。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PM_DEVICE_RUNTIME && CONFIG_SPI_NOR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nor:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nor#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → SPI NOR 闪存（Flash）

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE_RUNTIME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE_RUNTIME)、[`CONFIG_SPI_NOR`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_NOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_SPI_NOR_FLASH_LAYOUT_PAGE_SIZE"></a>

## 94.56 `CONFIG_SPI_NOR_FLASH_LAYOUT_PAGE_SIZE`

**提示（Prompt）**：`FLASH_LAYOUT` 功能使用的页大小（Page Size）

**说明（Help）**

使用 `CONFIG_FLASH_PAGE_LAYOUT` 时，此驱动支持对应 API。默认页大小（Page Size）等于块大小（Block Size）`65536`。其他选项包括 32 KB 擦除大小 `32768`、扇区大小（Sector Size）`4096`，或扇区大小的任意非零整数倍。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_NOR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
65536
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nor:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nor#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → SPI NOR 闪存（Flash）

**配置项引用（Symbol References）**：[`CONFIG_SPI_NOR`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_NOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_SPI_NOR_INIT_PRIORITY"></a>

## 94.57 `CONFIG_SPI_NOR_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动的初始化优先级（Initialization Priority）。设备连接在 SPI 总线上，必须在 SPI 驱动之后初始化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_NOR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nor:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nor#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → SPI NOR 闪存（Flash）

**配置项引用（Symbol References）**：[`CONFIG_SPI_NOR`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_NOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_SPI_NOR_SFDP"></a>

## 94.58 `CONFIG_SPI_NOR_SFDP`

**提示（Prompt）**：串行闪存可发现参数（Serial Flash Discoverable Parameters，SFDP）的来源

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_NOR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
CONFIG_SPI_NOR_SFDP_MINIMAL
```

**可选项（Choices）**

```text
CONFIG_SPI_NOR_SFDP_MINIMAL
CONFIG_SPI_NOR_SFDP_DEVICETREE
CONFIG_SPI_NOR_SFDP_RUNTIME
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nor:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nor#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → SPI NOR 闪存（Flash）

**配置项引用（Symbol References）**：[`CONFIG_SPI_NOR`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_NOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_SPI_NOR_SFDP_MINIMAL`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_NOR_SFDP_MINIMAL)、[`CONFIG_SPI_NOR_SFDP_DEVICETREE`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_NOR_SFDP_DEVICETREE)、[`CONFIG_SPI_NOR_SFDP_RUNTIME`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_NOR_SFDP_RUNTIME)。

<a id="CONFIG_SPI_NOR_SFDP_DEVICETREE"></a>

## 94.59 `CONFIG_SPI_NOR_SFDP_DEVICETREE`

**提示（Prompt）**：来自设备树节点的基本闪存参数（Basic Flash Parameters）

**说明（Help）**

必须通过设备树（Devicetree）的 `sfdp-bfp` 属性提供 JESD216 基本闪存参数表（Basic Flash Parameters Table）。还必须提供 `size` 和 `jedec-id` 属性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nor:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nor#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → SPI NOR 闪存（Flash） → 串行闪存可发现参数（Serial Flash Discoverable Parameters，SFDP）的来源

<a id="CONFIG_SPI_NOR_SFDP_MINIMAL"></a>

## 94.60 `CONFIG_SPI_NOR_SFDP_MINIMAL`

**提示（Prompt）**：固定闪存配置（Fixed Flash Configuration）

**说明（Help）**

合成一个最小配置（Minimal Configuration），假定页大小为 256 字节，或采用设备树（Devicetree）属性 `page-size` 指定的大小，并使用标准的 4 KiB 和 64 KiB 擦除指令。设备树的 `jedec,spi-nor` 节点中必须提供 `size` 和 `jedec-id` 属性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nor:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nor#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → SPI NOR 闪存（Flash） → 串行闪存可发现参数（Serial Flash Discoverable Parameters，SFDP）的来源

<a id="CONFIG_SPI_NOR_SFDP_RUNTIME"></a>

## 94.61 `CONFIG_SPI_NOR_SFDP_RUNTIME`

**提示（Prompt）**：运行时读取闪存参数（Read Flash Parameters at Runtime）

**说明（Help）**

运行时从设备读取全部闪存设备特征（Flash Device Characteristics）。此选项最灵活，因为它应能为所有受支持的 JESD216 兼容器件提供功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SPI_NOR_SFDP>
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nor:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nor#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → SPI NOR 闪存（Flash） → 串行闪存可发现参数（Serial Flash Discoverable Parameters，SFDP）的来源

**配置项引用（Symbol References）**：[`CONFIG_SPI_NOR_SFDP`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_NOR_SFDP)。

<a id="CONFIG_SPI_NOR_SLEEP_ERASE_MS"></a>

## 94.62 `CONFIG_SPI_NOR_SLEEP_ERASE_MS`

**提示（Prompt）**：等待擦除操作时的轮询间隔（Polling Delay），以毫秒为单位

**说明（Help）**

等待闪存完成擦除操作（Erase Operation）期间，两次轮询（Polling）之间的延迟。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_NOR_SLEEP_WHILE_WAITING_UNTIL_READY && CONFIG_SPI_NOR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nor:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nor#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → SPI NOR 闪存（Flash） → 等待闪存操作完成时休眠（Sleep while Waiting）

**配置项引用（Symbol References）**：[`CONFIG_SPI_NOR_SLEEP_WHILE_WAITING_UNTIL_READY`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_NOR_SLEEP_WHILE_WAITING_UNTIL_READY)、[`CONFIG_SPI_NOR`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_NOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_SPI_NOR_SLEEP_WHILE_WAITING_UNTIL_READY"></a>

## 94.63 `CONFIG_SPI_NOR_SLEEP_WHILE_WAITING_UNTIL_READY`

**提示（Prompt）**：等待闪存操作完成时休眠（Sleep while Waiting）

**说明（Help）**

闪存操作可能需要 1 ms 至 240 秒才能完成。启用此选项后，对慢速操作的状态寄存器（Status Register）进行轮询时，在两次轮询之间加入延迟。如果本驱动是唯一使用 `k_sleep` 的组件，禁用此项可以显著节省闪存空间；构建引导加载程序（Bootloader）时可能出现这种情况。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_NOR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nor:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nor#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → SPI NOR 闪存（Flash）

**配置项引用（Symbol References）**：[`CONFIG_SPI_NOR`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_NOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_STM32WBA_FLASH_MNGR_THREAD_PRIO"></a>

## 94.64 `CONFIG_STM32WBA_FLASH_MNGR_THREAD_PRIO`

**提示（Prompt）**：闪存管理器线程优先级（Flash Manager Thread Priority）

**说明（Help）**

此选项设置闪存管理器（Flash Manager）线程的协作式优先级（Cooperative Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_STM32WBAX && CONFIG_SOC_FLASH_STM32 && CONFIG_FLASH
```

**默认值（Defaults）**

```text
14
```

**定义位置（Location）**：[`drivers/flash/Kconfig.stm32:131`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.stm32#L131)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → STM32 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_STM32WBAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBAX)、[`CONFIG_SOC_FLASH_STM32`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_STM32)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32WBAX`。

<a id="CONFIG_STM32WBA_FLASH_MNGR_THREAD_STACK_SIZE"></a>

## 94.65 `CONFIG_STM32WBA_FLASH_MNGR_THREAD_STACK_SIZE`

**提示（Prompt）**：STM32WBAx 闪存管理器线程栈大小（Flash Manager Thread Stack Size）

**说明（Help）**

闪存管理器（Flash Manager）线程的栈大小，以字节为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_STM32WBAX && CONFIG_SOC_FLASH_STM32 && CONFIG_FLASH
```

**默认值（Defaults）**

```text
768
```

**定义位置（Location）**：[`drivers/flash/Kconfig.stm32:125`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.stm32#L125)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → STM32 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_STM32WBAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBAX)、[`CONFIG_SOC_FLASH_STM32`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_STM32)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32WBAX`。

<a id="CONFIG_USE_MICROCHIP_QSPI_FLASH_WITH_STM32"></a>

## 94.66 `CONFIG_USE_MICROCHIP_QSPI_FLASH_WITH_STM32`

**提示（Prompt）**：包含 STM32 配合 Microchip QSPI 闪存运行时的补丁（Patch）

**说明（Help）**

当使用的 Microchip QSPI 闪存在执行 `PP_1_4_4` 操作时采用 `PP_1_1_4` 操作码 `32H`，而不是通常的 `38H` 时，设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_FLASH_STM32_QSPI || CONFIG_FLASH_STM32_OSPI || CONFIG_FLASH_STM32_XSPI) && CONFIG_SOC_FLASH_STM32 && CONFIG_FLASH
```

**定义位置（Location）**：[`drivers/flash/Kconfig.stm32:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.stm32#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → STM32 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_STM32_QSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_QSPI)、[`CONFIG_FLASH_STM32_OSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_OSPI)、[`CONFIG_FLASH_STM32_XSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_XSPI)、[`CONFIG_SOC_FLASH_STM32`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_STM32)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<!-- kconfig-navigation -->

[上一章](P093_drivers_flash_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P095_drivers_fpga_配置项参考.md)
