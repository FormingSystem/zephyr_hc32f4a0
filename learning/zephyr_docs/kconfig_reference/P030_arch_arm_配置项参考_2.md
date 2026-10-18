---
id: learning.zephyr-docs.kconfig-reference.page-30
title: "`arch/arm`配置项参考（2/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第30章\_`arch/arm`配置项参考（2/2）

本章翻译官方 Kconfig 数据库中 `arch/arm` 的 74 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_CPU_CORTEX_M_HAS_BASEPRI"></a>

## 30.1 `CONFIG_CPU_CORTEX_M_HAS_BASEPRI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示 CPU 具有 `BASEPRI` 寄存器，用于定义异常处理的最低优先级（Minimum Priority）。`BASEPRI` 设为非零值时，会阻止与该值同级或更低优先级的所有异常激活。实现 ARMv7-M 或 ARM8-M 主线（Mainline）架构的 CPU 始终具有此寄存器。

译注：`ARM8-M` 按原文保留。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARMV7_M_ARMV8_M_MAINLINE && CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_ARMV7_M_ARMV8_M_MAINLINE
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:131`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L131)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARMV7_M_ARMV8_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_M_ARMV8_M_MAINLINE)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_CPU_CORTEX_M_HAS_CMSE"></a>

## 30.2 `CONFIG_CPU_CORTEX_M_HAS_CMSE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示 Cortex-M CPU 具有 CMSE 内建函数（Intrinsics）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_ARMV8_M_BASELINE || CONFIG_ARMV8_M_MAINLINE) && CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_PSC3
CONFIG_ARMV8_M_BASELINE
CONFIG_ARMV8_M_MAINLINE
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:187`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L187)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARMV8_M_BASELINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_M_BASELINE)、[`CONFIG_ARMV8_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_M_MAINLINE)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_SOC_SERIES_PSC3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSC3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_PSC3`。

<a id="CONFIG_CPU_CORTEX_M_HAS_DWT"></a>

## 30.3 `CONFIG_CPU_CORTEX_M_HAS_DWT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示 CPU 实现 ARMv7-M 及以上架构定义的数据观察点与跟踪（DWT）单元。虽然 ARMv6-M 也定义了一个称为 DWT 的单元，但其功能集和寄存器映射都与 ARMv7-M 及以上的 DWT 有显著差异。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_CPU_CORTEX_M0 && !CONFIG_CPU_CORTEX_M0PLUS && !CONFIG_CPU_CORTEX_M1 && CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC
CONFIG_SOC_LPC54114_M4
CONFIG_SOC_LPC54628
CONFIG_SOC_SERIES_LPC55XXX
CONFIG_SOC_SR100
CONFIG_SOC_SERIES_MEC15XX
CONFIG_SOC_SERIES_MEC165XB
CONFIG_SOC_SERIES_MEC172X
CONFIG_SOC_SERIES_MEC174X
CONFIG_SOC_SERIES_MEC175X
CONFIG_SOC_SERIES_SAMD51
CONFIG_SOC_SERIES_SAME51
CONFIG_SOC_SERIES_SAME53
CONFIG_SOC_SERIES_SAME54
CONFIG_SOC_KB1200
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
CONFIG_SOC_SERIES_RA8D2
CONFIG_SOC_SERIES_RA8E1
CONFIG_SOC_SERIES_RA8M2
CONFIG_SOC_SERIES_RA8P1
CONFIG_SOC_SERIES_RA8T2
CONFIG_SOC_FAMILY_MCXA
CONFIG_SOC_SERIES_MCXE24X
CONFIG_SOC_SERIES_MCXE31X
CONFIG_SOC_MCXL255_CPU0
CONFIG_SOC_MCXL254_CPU0
CONFIG_SOC_MCXL253_CPU0
CONFIG_SOC_FAMILY_MCXN
CONFIG_SOC_FAMILY_MCXW
CONFIG_SOC_SERIES_AM62X_M4
CONFIG_SOC_SERIES_AM64X_M4
CONFIG_SOC_SERIES_EFM32TG
CONFIG_SOC_SERIES_EFM32WG
CONFIG_SOC_SERIES_EFM32PG12B
CONFIG_SOC_SERIES_EFM32PG1B
CONFIG_SOC_SERIES_EFR32BG13P
CONFIG_SOC_SERIES_EFR32FG13P
CONFIG_SOC_SERIES_EFR32FG1P
CONFIG_SOC_SERIES_EFR32MG12P
CONFIG_SOC_SERIES_EFR32MG13P
CONFIG_SOC_FAMILY_SILABS_S2_XG21
CONFIG_SOC_FAMILY_SILABS_S2_XG22
CONFIG_SOC_FAMILY_SILABS_S2_XG23
CONFIG_SOC_FAMILY_SILABS_S2_XG24
CONFIG_SOC_FAMILY_SILABS_S2_XG26
CONFIG_SOC_FAMILY_SILABS_S2_XG27
CONFIG_SOC_FAMILY_SILABS_S2_XG28
CONFIG_SOC_FAMILY_SILABS_S2_XG29
CONFIG_SOC_FAMILY_SILABS_S3_SIX301
CONFIG_SOC_FAMILY_SILABS_SIWX91X
CONFIG_SOC_SERIES_IMXRT10XX
CONFIG_SOC_SERIES_IMXRT118X
CONFIG_SOC_SERIES_IMXRT11XX
CONFIG_SOC_SERIES_IMXRT266X_CM85
CONFIG_SOC_MIMXRT595S_CM33
CONFIG_SOC_MIMXRT685S_CM33
CONFIG_SOC_MIMXRT798S_CM33_CPU0
CONFIG_SOC_MIMXRT798S_CM33_CPU1
CONFIG_SOC_MIMXRT758S_CM33_CPU0
CONFIG_SOC_MIMXRT758S_CM33_CPU1
CONFIG_SOC_MIMXRT735S_CM33_CPU0
CONFIG_SOC_MIMXRT735S_CM33_CPU1
CONFIG_SOC_SERIES_M333X
CONFIG_SOC_SERIES_M335X
CONFIG_SOC_SERIES_M46X
CONFIG_SOC_SERIES_M55M1X
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA
CONFIG_SOC_SERIES_K2X
CONFIG_SOC_SERIES_K6X
CONFIG_SOC_SERIES_K8X
CONFIG_SOC_SERIES_KE1XF
CONFIG_SOC_SERIES_KV5X
CONFIG_SOC_MKW22D5
CONFIG_SOC_MKW24D5
CONFIG_SOC_NRF52832
CONFIG_SOC_NRF52833
CONFIG_SOC_NRF52840
CONFIG_SOC_SERIES_NRF53
CONFIG_SOC_NRF54H20_CPUAPP_COMMON
CONFIG_SOC_NRF54H20_CPURAD_COMMON
CONFIG_SOC_NRF54L_CPUAPP_COMMON
CONFIG_SOC_SERIES_NRF91
CONFIG_SOC_SERIES_TM4C123X
CONFIG_SOC_FAMILY_PSOC6
CONFIG_SOC_FAMILY_PSOC6_LEGACY_M4
CONFIG_SOC_TI_LM3S6965
CONFIG_SOC_SERIES_IMX6SX
CONFIG_SOC_SERIES_IMX7D
CONFIG_SOC_MIMX9352_M33
CONFIG_SOC_MIMX9596_M7
CONFIG_SOC_MIMX9529_M7
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG
CONFIG_SOC_SERIES_CC13X2_CC26X2
CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7
CONFIG_SOC_SERIES_CC32XX
CONFIG_SOC_SERIES_MSP432P4XX
CONFIG_SOC_SERIES_NPCM4
CONFIG_SOC_SERIES_APOLLO2X
CONFIG_SOC_SERIES_APOLLO3X
CONFIG_SOC_SERIES_APOLLO4X
CONFIG_SOC_SERIES_APOLLO5X
CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X
CONFIG_SOC_FAMILY_ENSEMBLE_RTSS
CONFIG_SOC_SERIES_DA1469X
CONFIG_SOC_SERIES_RZG2L
CONFIG_SOC_SERIES_RZG2UL
CONFIG_SOC_SERIES_RZG3E
CONFIG_SOC_SERIES_RZG3S
CONFIG_SOC_R9A09G057H44GBG_CM33
CONFIG_SOC_SERIES_RZV2L
CONFIG_SOC_SERIES_RZV2N
CONFIG_SOC_SERIES_B1
CONFIG_SOC_SERIES_SAM3X
CONFIG_SOC_SERIES_SAM4E
CONFIG_SOC_SERIES_SAM4L
CONFIG_SOC_SERIES_SAM4S
CONFIG_SOC_SERIES_SAMX7X
CONFIG_SOC_SERIES_SMARTFUSION2
CONFIG_SOC_SERIES_XMC4XXX
CONFIG_SOC_SERIES_M48X
CONFIG_SOC_SERIES_STM32C5X
CONFIG_SOC_SERIES_STM32F1X
CONFIG_SOC_SERIES_STM32F2X
CONFIG_SOC_SERIES_STM32F3X
CONFIG_SOC_SERIES_STM32F4X
CONFIG_SOC_SERIES_STM32F7X
CONFIG_SOC_SERIES_STM32G4X
CONFIG_SOC_SERIES_STM32H5X
CONFIG_SOC_SERIES_STM32H7RSX
CONFIG_SOC_SERIES_STM32H7X
CONFIG_SOC_SERIES_STM32L1X
CONFIG_SOC_SERIES_STM32L4X
CONFIG_SOC_SERIES_STM32L5X
CONFIG_SOC_SERIES_STM32MP1X
CONFIG_SOC_STM32MP2X_M33
CONFIG_SOC_SERIES_STM32N6X
CONFIG_SOC_SERIES_STM32U3X
CONFIG_SOC_SERIES_STM32U5X
CONFIG_SOC_SERIES_STM32WBAX
CONFIG_SOC_SERIES_STM32WBX
CONFIG_SOC_SERIES_STM32WLX
CONFIG_SOC_SERIES_BEETLE
CONFIG_SOC_MUSCA_B1
CONFIG_SOC_MUSCA_S1
CONFIG_SOC_SERIES_NPCK3
CONFIG_SOC_SERIES_NPCX4
CONFIG_SOC_SERIES_NPCX7
CONFIG_SOC_SERIES_NPCX9
CONFIG_SOC_SERIES_RW6XX
CONFIG_SOC_S32K142
CONFIG_SOC_S32K142W
CONFIG_SOC_S32K144
CONFIG_SOC_S32K144W
CONFIG_SOC_S32K146
CONFIG_SOC_S32K148
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:120`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L120)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M0`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M0)、[`CONFIG_CPU_CORTEX_M0PLUS`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M0PLUS)、[`CONFIG_CPU_CORTEX_M1`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M1)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC)、[`CONFIG_SOC_LPC54114_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC54114_M4)、[`CONFIG_SOC_LPC54628`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC54628)、[`CONFIG_SOC_SERIES_LPC55XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC55XXX)、[`CONFIG_SOC_SR100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SR100)、[`CONFIG_SOC_SERIES_MEC15XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC15XX)、[`CONFIG_SOC_SERIES_MEC165XB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC165XB)、[`CONFIG_SOC_SERIES_MEC172X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC172X)、[`CONFIG_SOC_SERIES_MEC174X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC174X)、[`CONFIG_SOC_SERIES_MEC175X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC175X)、[`CONFIG_SOC_SERIES_SAMD51`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMD51)、[`CONFIG_SOC_SERIES_SAME51`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAME51)、[`CONFIG_SOC_SERIES_SAME53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAME53)、[`CONFIG_SOC_SERIES_SAME54`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAME54)、[`CONFIG_SOC_KB1200`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_KB1200)、[`CONFIG_SOC_SERIES_RA4C1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4C1)、[`CONFIG_SOC_SERIES_RA4E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4E1)、[`CONFIG_SOC_SERIES_RA4E2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4E2)、[`CONFIG_SOC_SERIES_RA4L1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4L1)、[`CONFIG_SOC_SERIES_RA4M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M1)、[`CONFIG_SOC_SERIES_RA4M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M2)、[`CONFIG_SOC_SERIES_RA4M3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M3)、[`CONFIG_SOC_SERIES_RA4T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4T1)、[`CONFIG_SOC_SERIES_RA4W1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4W1)、[`CONFIG_SOC_SERIES_RA6E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6E1)、[`CONFIG_SOC_SERIES_RA6E2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6E2)、[`CONFIG_SOC_SERIES_RA6M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M1)、[`CONFIG_SOC_SERIES_RA6M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M2)、[`CONFIG_SOC_SERIES_RA6M3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M3)、[`CONFIG_SOC_SERIES_RA6M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M4)、[`CONFIG_SOC_SERIES_RA6M5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M5)、[`CONFIG_SOC_SERIES_RA8D2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8D2)、[`CONFIG_SOC_SERIES_RA8E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8E1)、[`CONFIG_SOC_SERIES_RA8M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8M2)、[`CONFIG_SOC_SERIES_RA8P1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8P1)、[`CONFIG_SOC_SERIES_RA8T2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8T2)、[`CONFIG_SOC_FAMILY_MCXA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXA)、[`CONFIG_SOC_SERIES_MCXE24X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE24X)、[`CONFIG_SOC_SERIES_MCXE31X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE31X)、[`CONFIG_SOC_MCXL255_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL255_CPU0)、[`CONFIG_SOC_MCXL254_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL254_CPU0)、[`CONFIG_SOC_MCXL253_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL253_CPU0)、[`CONFIG_SOC_FAMILY_MCXN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXN)、[`CONFIG_SOC_FAMILY_MCXW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXW)、[`CONFIG_SOC_SERIES_AM62X_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM62X_M4)、[`CONFIG_SOC_SERIES_AM64X_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM64X_M4)、[`CONFIG_SOC_SERIES_EFM32TG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32TG)、[`CONFIG_SOC_SERIES_EFM32WG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32WG)、[`CONFIG_SOC_SERIES_EFM32PG12B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32PG12B)、[`CONFIG_SOC_SERIES_EFM32PG1B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32PG1B)、[`CONFIG_SOC_SERIES_EFR32BG13P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32BG13P)、[`CONFIG_SOC_SERIES_EFR32FG13P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32FG13P)、[`CONFIG_SOC_SERIES_EFR32FG1P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32FG1P)、[`CONFIG_SOC_SERIES_EFR32MG12P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32MG12P)、[`CONFIG_SOC_SERIES_EFR32MG13P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32MG13P)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG21)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG22`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG22)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG23`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG23)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG24`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG24)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG26`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG26)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG27`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG27)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG28`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG28)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG29`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG29)、[`CONFIG_SOC_FAMILY_SILABS_S3_SIX301`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S3_SIX301)、[`CONFIG_SOC_FAMILY_SILABS_SIWX91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_SIWX91X)、[`CONFIG_SOC_SERIES_IMXRT10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT10XX)、[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_SERIES_IMXRT266X_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT266X_CM85)、[`CONFIG_SOC_MIMXRT595S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT595S_CM33)、[`CONFIG_SOC_MIMXRT685S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_CM33)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU1)、[`CONFIG_SOC_MIMXRT758S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT758S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_CM33_CPU1)、[`CONFIG_SOC_MIMXRT735S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT735S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_CM33_CPU1)、[`CONFIG_SOC_SERIES_M333X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M333X)、[`CONFIG_SOC_SERIES_M335X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M335X)、[`CONFIG_SOC_SERIES_M46X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M46X)、[`CONFIG_SOC_SERIES_M55M1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M55M1X)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA)、[`CONFIG_SOC_SERIES_K2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K2X)、[`CONFIG_SOC_SERIES_K6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K6X)、[`CONFIG_SOC_SERIES_K8X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K8X)、[`CONFIG_SOC_SERIES_KE1XF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KE1XF)、[`CONFIG_SOC_SERIES_KV5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KV5X)、[`CONFIG_SOC_MKW22D5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MKW22D5)、[`CONFIG_SOC_MKW24D5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MKW24D5)、[`CONFIG_SOC_NRF52832`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF52832)、[`CONFIG_SOC_NRF52833`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF52833)、[`CONFIG_SOC_NRF52840`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF52840)、[`CONFIG_SOC_SERIES_NRF53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_NRF54H20_CPUAPP_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPUAPP_COMMON)、[`CONFIG_SOC_NRF54H20_CPURAD_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPURAD_COMMON)、[`CONFIG_SOC_NRF54L_CPUAPP_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54L_CPUAPP_COMMON)、[`CONFIG_SOC_SERIES_NRF91`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF91)、[`CONFIG_SOC_SERIES_TM4C123X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_TM4C123X)、[`CONFIG_SOC_FAMILY_PSOC6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY_M4)、[`CONFIG_SOC_TI_LM3S6965`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_TI_LM3S6965)、[`CONFIG_SOC_SERIES_IMX6SX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMX6SX)、[`CONFIG_SOC_SERIES_IMX7D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMX7D)、[`CONFIG_SOC_MIMX9352_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9352_M33)、[`CONFIG_SOC_MIMX9596_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9596_M7)、[`CONFIG_SOC_MIMX9529_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9529_M7)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG)、[`CONFIG_SOC_SERIES_CC13X2_CC26X2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC13X2_CC26X2)、[`CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7)、[`CONFIG_SOC_SERIES_CC32XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC32XX)、[`CONFIG_SOC_SERIES_MSP432P4XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSP432P4XX)、[`CONFIG_SOC_SERIES_NPCM4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCM4)、[`CONFIG_SOC_SERIES_APOLLO2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO2X)、[`CONFIG_SOC_SERIES_APOLLO3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO3X)、[`CONFIG_SOC_SERIES_APOLLO4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO4X)、[`CONFIG_SOC_SERIES_APOLLO5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO5X)、[`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X)、[`CONFIG_SOC_FAMILY_ENSEMBLE_RTSS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ENSEMBLE_RTSS)、[`CONFIG_SOC_SERIES_DA1469X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_DA1469X)、[`CONFIG_SOC_SERIES_RZG2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZG2L)、[`CONFIG_SOC_SERIES_RZG2UL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZG2UL)、[`CONFIG_SOC_SERIES_RZG3E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZG3E)、[`CONFIG_SOC_SERIES_RZG3S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZG3S)、[`CONFIG_SOC_R9A09G057H44GBG_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R9A09G057H44GBG_CM33)、[`CONFIG_SOC_SERIES_RZV2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZV2L)、[`CONFIG_SOC_SERIES_RZV2N`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZV2N)、[`CONFIG_SOC_SERIES_B1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_B1)、[`CONFIG_SOC_SERIES_SAM3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAM3X)、[`CONFIG_SOC_SERIES_SAM4E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAM4E)、[`CONFIG_SOC_SERIES_SAM4L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAM4L)、[`CONFIG_SOC_SERIES_SAM4S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAM4S)、[`CONFIG_SOC_SERIES_SAMX7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMX7X)、[`CONFIG_SOC_SERIES_SMARTFUSION2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SMARTFUSION2)、[`CONFIG_SOC_SERIES_XMC4XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XMC4XXX)、[`CONFIG_SOC_SERIES_M48X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M48X)、[`CONFIG_SOC_SERIES_STM32C5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32C5X)、[`CONFIG_SOC_SERIES_STM32F1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F1X)、[`CONFIG_SOC_SERIES_STM32F2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F2X)、[`CONFIG_SOC_SERIES_STM32F3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F3X)、[`CONFIG_SOC_SERIES_STM32F4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F4X)、[`CONFIG_SOC_SERIES_STM32F7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F7X)、[`CONFIG_SOC_SERIES_STM32G4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32G4X)、[`CONFIG_SOC_SERIES_STM32H5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H5X)、[`CONFIG_SOC_SERIES_STM32H7RSX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7RSX)、[`CONFIG_SOC_SERIES_STM32H7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7X)、[`CONFIG_SOC_SERIES_STM32L1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L1X)、[`CONFIG_SOC_SERIES_STM32L4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L4X)、[`CONFIG_SOC_SERIES_STM32L5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L5X)、[`CONFIG_SOC_SERIES_STM32MP1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32MP1X)、[`CONFIG_SOC_STM32MP2X_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32MP2X_M33)、[`CONFIG_SOC_SERIES_STM32N6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32N6X)、[`CONFIG_SOC_SERIES_STM32U3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U3X)、[`CONFIG_SOC_SERIES_STM32U5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U5X)、[`CONFIG_SOC_SERIES_STM32WBAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBAX)、[`CONFIG_SOC_SERIES_STM32WBX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBX)、[`CONFIG_SOC_SERIES_STM32WLX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WLX)、[`CONFIG_SOC_SERIES_BEETLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BEETLE)、[`CONFIG_SOC_MUSCA_B1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MUSCA_B1)、[`CONFIG_SOC_MUSCA_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MUSCA_S1)、[`CONFIG_SOC_SERIES_NPCK3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCK3)、[`CONFIG_SOC_SERIES_NPCX4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCX4)、[`CONFIG_SOC_SERIES_NPCX7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCX7)、[`CONFIG_SOC_SERIES_NPCX9`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCX9)、[`CONFIG_SOC_SERIES_RW6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RW6XX)、[`CONFIG_SOC_S32K142`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K142)、[`CONFIG_SOC_S32K142W`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K142W)、[`CONFIG_SOC_S32K144`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K144)、[`CONFIG_SOC_S32K144W`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K144W)、[`CONFIG_SOC_S32K146`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K146)、[`CONFIG_SOC_S32K148`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K148)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`、`CONFIG_SOC_LPC54114_M4`、`CONFIG_SOC_LPC54628`、`CONFIG_SOC_SERIES_LPC55XXX`、`CONFIG_SOC_SR100`、`CONFIG_SOC_FAMILY_MCXA`、`CONFIG_SOC_SERIES_MCXE24X`、`CONFIG_SOC_SERIES_MCXE31X`、`CONFIG_SOC_MCXL255_CPU0`、`CONFIG_SOC_MCXL254_CPU0`、`CONFIG_SOC_MCXL253_CPU0`、`CONFIG_SOC_FAMILY_MCXN`、`CONFIG_SOC_FAMILY_MCXW`、`CONFIG_SOC_FAMILY_SILABS_SIWX91X`、`CONFIG_SOC_SERIES_IMXRT10XX`、`CONFIG_SOC_SERIES_IMXRT118X`、`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_SERIES_IMXRT266X_CM85`、`CONFIG_SOC_MIMXRT685S_CM33`、`CONFIG_SOC_MIMXRT798S_CM33_CPU0`、`CONFIG_SOC_MIMXRT798S_CM33_CPU1`、`CONFIG_SOC_MIMXRT758S_CM33_CPU0`、`CONFIG_SOC_MIMXRT758S_CM33_CPU1`、`CONFIG_SOC_MIMXRT735S_CM33_CPU0`、`CONFIG_SOC_MIMXRT735S_CM33_CPU1`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`、`CONFIG_SOC_SERIES_K2X`、`CONFIG_SOC_SERIES_K6X`、`CONFIG_SOC_SERIES_K8X`、`CONFIG_SOC_SERIES_KE1XF`、`CONFIG_SOC_SERIES_KV5X`、`CONFIG_SOC_MKW22D5`、`CONFIG_SOC_MKW24D5`、`CONFIG_SOC_NRF52832`、`CONFIG_SOC_NRF52833`、`CONFIG_SOC_NRF52840`、`CONFIG_SOC_NRF54H20_CPUAPP_COMMON`、`CONFIG_SOC_NRF54H20_CPURAD_COMMON`、`CONFIG_SOC_NRF54L_CPUAPP_COMMON`、`CONFIG_SOC_SERIES_TM4C123X`、`CONFIG_SOC_FAMILY_PSOC6`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY_M4`、`CONFIG_SOC_SERIES_IMX6SX`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG`、`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`、`CONFIG_SOC_FAMILY_ENSEMBLE_RTSS`、`CONFIG_SOC_SERIES_B1`、`CONFIG_SOC_SERIES_STM32C5X`、`CONFIG_SOC_SERIES_STM32F1X`、`CONFIG_SOC_SERIES_STM32F2X`、`CONFIG_SOC_SERIES_STM32F3X`、`CONFIG_SOC_SERIES_STM32F4X`、`CONFIG_SOC_SERIES_STM32F7X`、`CONFIG_SOC_SERIES_STM32G4X`、`CONFIG_SOC_SERIES_STM32H5X`、`CONFIG_SOC_SERIES_STM32H7RSX`、`CONFIG_SOC_SERIES_STM32H7X`、`CONFIG_SOC_SERIES_STM32L1X`、`CONFIG_SOC_SERIES_STM32L4X`、`CONFIG_SOC_SERIES_STM32L5X`、`CONFIG_SOC_SERIES_STM32MP1X`、`CONFIG_SOC_STM32MP2X_M33`、`CONFIG_SOC_SERIES_STM32N6X`、`CONFIG_SOC_SERIES_STM32U3X`、`CONFIG_SOC_SERIES_STM32U5X`、`CONFIG_SOC_SERIES_STM32WBAX`、`CONFIG_SOC_SERIES_STM32WBX`、`CONFIG_SOC_SERIES_STM32WLX`、`CONFIG_SOC_SERIES_RW6XX`、`CONFIG_SOC_S32K142`、`CONFIG_SOC_S32K142W`、`CONFIG_SOC_S32K144`、`CONFIG_SOC_S32K144W`、`CONFIG_SOC_S32K146`、`CONFIG_SOC_S32K148`。

<a id="CONFIG_CPU_CORTEX_M_HAS_PROGRAMMABLE_FAULT_PRIOS"></a>

## 30.4 `CONFIG_CPU_CORTEX_M_HAS_PROGRAMMABLE_FAULT_PRIOS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示 CPU 可以触发 HardFault 之外、具有可配置优先级的系统故障（System Fault），因此需要为它们保留一个优先级。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARMV7_M_ARMV8_M_MAINLINE && CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_ARMV7_M_ARMV8_M_MAINLINE
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:172`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L172)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARMV7_M_ARMV8_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_M_ARMV8_M_MAINLINE)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_CPU_CORTEX_M_HAS_SPLIM"></a>

## 30.5 `CONFIG_CPU_CORTEX_M_HAS_SPLIM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示 CPU 具有 `MSPLIM`、`PSPLIM` 寄存器。这两个栈指针限制寄存器（Stack Pointer Limit Registers）分别限制主栈指针（Main Stack Pointer）和进程栈指针（Process Stack Pointer）可向下移动的范围。实现 ARMv8-M 主扩展（Main Extension，即 Mainline）的 MCU 始终具有它们。具有安全扩展（Security Extension）的 ARMv8-M 主线实现还具有额外的安全寄存器实例；具有安全扩展的 ARMv8-M 基线实现则仅具有安全实例。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_ARMV8_M_MAINLINE || (CONFIG_ARMV8_M_SE && !CONFIG_ARM_NONSECURE_FIRMWARE)) && CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_ARMV8_M_MAINLINE
CONFIG_ARMV8_M_SE
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:156`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L156)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARMV8_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_M_MAINLINE)、[`CONFIG_ARMV8_M_SE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_M_SE)、[`CONFIG_ARM_NONSECURE_FIRMWARE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_NONSECURE_FIRMWARE)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_CPU_CORTEX_M_HAS_SYSTICK"></a>

## 30.6 `CONFIG_CPU_CORTEX_M_HAS_SYSTICK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CPU 实现 SysTick 定时器（Timer）时，启用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC
CONFIG_SOC_SERIES_PSOC4000T
CONFIG_SOC_SERIES_PSOC4100SMAX
CONFIG_SOC_SERIES_PSOC4100TP
CONFIG_SOC_AM13E23019
CONFIG_SOC_FT9001
CONFIG_SOC_SERIES_LPC11U6X
CONFIG_SOC_SERIES_LPC51U68
CONFIG_SOC_SERIES_LPC54XXX
CONFIG_SOC_SERIES_LPC55XXX
CONFIG_SOC_SERIES_LPC84X
CONFIG_SOC_SR100
CONFIG_SOC_EOS_S3
CONFIG_SOC_SERIES_SAMC20
CONFIG_SOC_SERIES_SAMC21
CONFIG_SOC_SERIES_SAMD20
CONFIG_SOC_SERIES_SAMD21
CONFIG_SOC_SERIES_SAML21
CONFIG_SOC_SERIES_SAMR21
CONFIG_SOC_SERIES_SAMR34
CONFIG_SOC_SERIES_SAMR35
CONFIG_SOC_SERIES_VALKYRIE
CONFIG_SOC_BCM58402_M7
CONFIG_SOC_SERIES_RP2040
CONFIG_SOC_RP2350A_M33_0
CONFIG_SOC_RP2350B_M33_0
CONFIG_SOC_SERIES_RA0E1
CONFIG_SOC_SERIES_RA2A1
CONFIG_SOC_SERIES_RA2L1
CONFIG_SOC_SERIES_RA8P1
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC
CONFIG_SOC_FAMILY_MCXA
CONFIG_SOC_FAMILY_MCXC
CONFIG_SOC_FAMILY_MCXL
CONFIG_SOC_FAMILY_MCXN
CONFIG_SOC_FAMILY_MCXW
CONFIG_SOC_SERIES_AM62X_M4
CONFIG_SOC_SERIES_AM64X_M4
CONFIG_SOC_SERIES_EFM32HG
CONFIG_SOC_SERIES_SIM3U
CONFIG_SOC_MIMXRT595S_CM33
CONFIG_SOC_MIMXRT685S_CM33
CONFIG_SOC_MIMXRT798S_CM33_CPU0
CONFIG_SOC_MIMXRT798S_CM33_CPU1
CONFIG_SOC_MIMXRT758S_CM33_CPU0
CONFIG_SOC_MIMXRT758S_CM33_CPU1
CONFIG_SOC_MIMXRT735S_CM33_CPU0
CONFIG_SOC_MIMXRT735S_CM33_CPU1
CONFIG_SOC_SERIES_M031X
CONFIG_SOC_SERIES_M2L31X
CONFIG_SOC_SERIES_M333X
CONFIG_SOC_SERIES_M335X
CONFIG_SOC_SERIES_M55M1X
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA
CONFIG_SOC_SERIES_K32LX
CONFIG_SOC_SERIES_KE1XZ
CONFIG_SOC_SERIES_KL2X
CONFIG_SOC_SERIES_KWX
CONFIG_SOC_FAMILY_PSOC6_LEGACY
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL
CONFIG_SOC_CYT4DNJBZS_M0P
CONFIG_SOC_CYT4DNJBZS_M7_0
CONFIG_SOC_CYT4DNJBZS_M7_1
CONFIG_SOC_SERIES_XMC7200
CONFIG_SOC_SERIES_GD32C2X1
CONFIG_SOC_SERIES_GD32E10X
CONFIG_SOC_SERIES_GD32F403
CONFIG_SOC_SERIES_GD32L23X
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH
CONFIG_SOC_FAMILY_ENSEMBLE_RTSS
CONFIG_SOC_SERIES_DA1469X
CONFIG_SOC_SERIES_B1
CONFIG_SOC_SERIES_RTL8752H
CONFIG_SOC_FAMILY_MAX32_M33
CONFIG_SOC_FAMILY_MAX32_M4
CONFIG_SOC_SERIES_MSPM0G
CONFIG_SOC_SERIES_MSPM0L
CONFIG_SOC_SERIES_STM32C0X
CONFIG_SOC_SERIES_STM32F0X
CONFIG_SOC_SERIES_STM32G0X
CONFIG_SOC_SERIES_STM32L0X
CONFIG_SOC_SERIES_STM32U0X
CONFIG_SOC_SERIES_STM32WB0X
CONFIG_SOC_SERIES_STM32WL3X
CONFIG_SOC_AN383
CONFIG_SOC_SERIES_RW6XX
CONFIG_ARMV7_M_ARMV8_M_MAINLINE
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:109`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L109)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC)、[`CONFIG_SOC_SERIES_PSOC4000T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSOC4000T)、[`CONFIG_SOC_SERIES_PSOC4100SMAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSOC4100SMAX)、[`CONFIG_SOC_SERIES_PSOC4100TP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSOC4100TP)、[`CONFIG_SOC_AM13E23019`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AM13E23019)、[`CONFIG_SOC_FT9001`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FT9001)、[`CONFIG_SOC_SERIES_LPC11U6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC11U6X)、[`CONFIG_SOC_SERIES_LPC51U68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC51U68)、[`CONFIG_SOC_SERIES_LPC54XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC54XXX)、[`CONFIG_SOC_SERIES_LPC55XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC55XXX)、[`CONFIG_SOC_SERIES_LPC84X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC84X)、[`CONFIG_SOC_SR100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SR100)、[`CONFIG_SOC_EOS_S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EOS_S3)、[`CONFIG_SOC_SERIES_SAMC20`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMC20)、[`CONFIG_SOC_SERIES_SAMC21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMC21)、[`CONFIG_SOC_SERIES_SAMD20`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMD20)、[`CONFIG_SOC_SERIES_SAMD21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMD21)、[`CONFIG_SOC_SERIES_SAML21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAML21)、[`CONFIG_SOC_SERIES_SAMR21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMR21)、[`CONFIG_SOC_SERIES_SAMR34`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMR34)、[`CONFIG_SOC_SERIES_SAMR35`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMR35)、[`CONFIG_SOC_SERIES_VALKYRIE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_VALKYRIE)、[`CONFIG_SOC_BCM58402_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BCM58402_M7)、[`CONFIG_SOC_SERIES_RP2040`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RP2040)、[`CONFIG_SOC_RP2350A_M33_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350A_M33_0)、[`CONFIG_SOC_RP2350B_M33_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350B_M33_0)、[`CONFIG_SOC_SERIES_RA0E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA0E1)、[`CONFIG_SOC_SERIES_RA2A1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA2A1)、[`CONFIG_SOC_SERIES_RA2L1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA2L1)、[`CONFIG_SOC_SERIES_RA8P1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8P1)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC)、[`CONFIG_SOC_FAMILY_MCXA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXA)、[`CONFIG_SOC_FAMILY_MCXC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXC)、[`CONFIG_SOC_FAMILY_MCXL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXL)、[`CONFIG_SOC_FAMILY_MCXN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXN)、[`CONFIG_SOC_FAMILY_MCXW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXW)、[`CONFIG_SOC_SERIES_AM62X_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM62X_M4)、[`CONFIG_SOC_SERIES_AM64X_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM64X_M4)、[`CONFIG_SOC_SERIES_EFM32HG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32HG)、[`CONFIG_SOC_SERIES_SIM3U`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SIM3U)、[`CONFIG_SOC_MIMXRT595S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT595S_CM33)、[`CONFIG_SOC_MIMXRT685S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_CM33)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU1)、[`CONFIG_SOC_MIMXRT758S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT758S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_CM33_CPU1)、[`CONFIG_SOC_MIMXRT735S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT735S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_CM33_CPU1)、[`CONFIG_SOC_SERIES_M031X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M031X)、[`CONFIG_SOC_SERIES_M2L31X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M2L31X)、[`CONFIG_SOC_SERIES_M333X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M333X)、[`CONFIG_SOC_SERIES_M335X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M335X)、[`CONFIG_SOC_SERIES_M55M1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M55M1X)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA)、[`CONFIG_SOC_SERIES_K32LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K32LX)、[`CONFIG_SOC_SERIES_KE1XZ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KE1XZ)、[`CONFIG_SOC_SERIES_KL2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KL2X)、[`CONFIG_SOC_SERIES_KWX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KWX)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL)、[`CONFIG_SOC_CYT4DNJBZS_M0P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4DNJBZS_M0P)、[`CONFIG_SOC_CYT4DNJBZS_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4DNJBZS_M7_0)、[`CONFIG_SOC_CYT4DNJBZS_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4DNJBZS_M7_1)、[`CONFIG_SOC_SERIES_XMC7200`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XMC7200)、[`CONFIG_SOC_SERIES_GD32C2X1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32C2X1)、[`CONFIG_SOC_SERIES_GD32E10X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32E10X)、[`CONFIG_SOC_SERIES_GD32F403`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32F403)、[`CONFIG_SOC_SERIES_GD32L23X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32L23X)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH)、[`CONFIG_SOC_FAMILY_ENSEMBLE_RTSS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ENSEMBLE_RTSS)、[`CONFIG_SOC_SERIES_DA1469X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_DA1469X)、[`CONFIG_SOC_SERIES_B1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_B1)、[`CONFIG_SOC_SERIES_RTL8752H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTL8752H)、[`CONFIG_SOC_FAMILY_MAX32_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_M33)、[`CONFIG_SOC_FAMILY_MAX32_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_M4)、[`CONFIG_SOC_SERIES_MSPM0G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSPM0G)、[`CONFIG_SOC_SERIES_MSPM0L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSPM0L)、[`CONFIG_SOC_SERIES_STM32C0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32C0X)、[`CONFIG_SOC_SERIES_STM32F0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F0X)、[`CONFIG_SOC_SERIES_STM32G0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32G0X)、[`CONFIG_SOC_SERIES_STM32L0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L0X)、[`CONFIG_SOC_SERIES_STM32U0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U0X)、[`CONFIG_SOC_SERIES_STM32WB0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WB0X)、[`CONFIG_SOC_SERIES_STM32WL3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WL3X)、[`CONFIG_SOC_AN383`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AN383)、[`CONFIG_SOC_SERIES_RW6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RW6XX)、[`CONFIG_ARMV7_M_ARMV8_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_M_ARMV8_M_MAINLINE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`、`CONFIG_SOC_AM13E23019`、`CONFIG_SOC_SERIES_LPC11U6X`、`CONFIG_SOC_SERIES_LPC51U68`、`CONFIG_SOC_SERIES_LPC54XXX`、`CONFIG_SOC_SERIES_LPC55XXX`、`CONFIG_SOC_SERIES_LPC84X`、`CONFIG_SOC_SR100`、`CONFIG_SOC_SERIES_RA2L1`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC`、`CONFIG_SOC_FAMILY_MCXA`、`CONFIG_SOC_FAMILY_MCXC`、`CONFIG_SOC_FAMILY_MCXL`、`CONFIG_SOC_FAMILY_MCXN`、`CONFIG_SOC_FAMILY_MCXW`、`CONFIG_SOC_MIMXRT685S_CM33`、`CONFIG_SOC_MIMXRT798S_CM33_CPU0`、`CONFIG_SOC_MIMXRT798S_CM33_CPU1`、`CONFIG_SOC_MIMXRT758S_CM33_CPU0`、`CONFIG_SOC_MIMXRT758S_CM33_CPU1`、`CONFIG_SOC_MIMXRT735S_CM33_CPU0`、`CONFIG_SOC_MIMXRT735S_CM33_CPU1`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`、`CONFIG_SOC_SERIES_K32LX`、`CONFIG_SOC_SERIES_KE1XZ`、`CONFIG_SOC_SERIES_KL2X`、`CONFIG_SOC_SERIES_KWX`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL`、`CONFIG_SOC_CYT4DNJBZS_M0P`、`CONFIG_SOC_CYT4DNJBZS_M7_0`、`CONFIG_SOC_CYT4DNJBZS_M7_1`、`CONFIG_SOC_SERIES_XMC7200`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`、`CONFIG_SOC_FAMILY_ENSEMBLE_RTSS`、`CONFIG_SOC_SERIES_B1`、`CONFIG_SOC_FAMILY_MAX32_M33`、`CONFIG_SOC_FAMILY_MAX32_M4`、`CONFIG_SOC_SERIES_STM32C0X`、`CONFIG_SOC_SERIES_STM32F0X`、`CONFIG_SOC_SERIES_STM32G0X`、`CONFIG_SOC_SERIES_STM32L0X`、`CONFIG_SOC_SERIES_STM32U0X`、`CONFIG_SOC_SERIES_STM32WB0X`、`CONFIG_SOC_SERIES_STM32WL3X`、`CONFIG_SOC_SERIES_RW6XX`。

<a id="CONFIG_CPU_CORTEX_M_HAS_VTOR"></a>

## 30.7 `CONFIG_CPU_CORTEX_M_HAS_VTOR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示 CPU 具有向量表偏移寄存器（VTOR），它指示向量表基地址相对于内存地址 `0x00000000` 的偏移量。原文称其始终存在于实现 ARMv7-M 或 ARMv8-M 架构的 CPU；在 ARMv6-M、ARMv8-M 基线（Baseline）实现中为可选，但 Cortex-M0/M1 从不实现。

译注：原文对 ARMv8-M 的概述与随后列出的 Baseline 可选条件同时保留，应按具体内核的实现确认。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_CPU_CORTEX_M0 && !CONFIG_CPU_CORTEX_M1 && CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC
CONFIG_SOC_SERIES_PSOC4000T
CONFIG_SOC_SERIES_PSOC4100SMAX
CONFIG_SOC_SERIES_PSOC4100TP
CONFIG_SOC_AM13E23019
CONFIG_SOC_FT9001
CONFIG_SOC_SERIES_LPC51U68
CONFIG_SOC_LPC54114_M0
CONFIG_SOC_SERIES_LPC84X
CONFIG_SOC_SERIES_SAMC20
CONFIG_SOC_SERIES_SAMC21
CONFIG_SOC_SERIES_SAMD20
CONFIG_SOC_SERIES_SAMD21
CONFIG_SOC_SERIES_SAML21
CONFIG_SOC_SERIES_SAMR21
CONFIG_SOC_SERIES_SAMR34
CONFIG_SOC_SERIES_SAMR35
CONFIG_SOC_SERIES_RP2040
CONFIG_SOC_RP2350A_M33_0
CONFIG_SOC_RP2350B_M33_0
CONFIG_SOC_SERIES_RA0E1
CONFIG_SOC_SERIES_RA2A1
CONFIG_SOC_SERIES_RA2L1
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC
CONFIG_SOC_FAMILY_MCXC
CONFIG_SOC_FAMILY_MCXL
CONFIG_SOC_SERIES_EFM32HG
CONFIG_SOC_SERIES_M2L31X
CONFIG_SOC_SERIES_M333X
CONFIG_SOC_SERIES_M335X
CONFIG_SOC_SERIES_M55M1X
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA
CONFIG_SOC_SERIES_K32LX
CONFIG_SOC_SERIES_KE1XZ
CONFIG_SOC_SERIES_KL2X
CONFIG_SOC_SERIES_KWX
CONFIG_SOC_FAMILY_PSOC6_LEGACY_M0
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL
CONFIG_SOC_CYT4DNJBZS_M0P
CONFIG_SOC_CYT4DNJBZS_M7_0
CONFIG_SOC_CYT4DNJBZS_M7_1
CONFIG_SOC_SERIES_XMC7200
CONFIG_SOC_SERIES_GD32C2X1
CONFIG_SOC_SERIES_GD32E10X
CONFIG_SOC_SERIES_GD32F403
CONFIG_SOC_SERIES_GD32L23X
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH
CONFIG_SOC_SERIES_CC23X0
CONFIG_SOC_SERIES_APOLLO5X
CONFIG_SOC_FAMILY_ENSEMBLE_RTSS
CONFIG_SOC_SERIES_B1
CONFIG_SOC_SERIES_RTL8752H
CONFIG_SOC_SERIES_MSPM0G
CONFIG_SOC_SERIES_MSPM0L
CONFIG_SOC_SERIES_STM32C0X
CONFIG_SOC_SERIES_STM32G0X
CONFIG_SOC_SERIES_STM32L0X
CONFIG_SOC_SERIES_STM32U0X
CONFIG_SOC_SERIES_STM32WB0X
CONFIG_SOC_SERIES_STM32WL3X
CONFIG_SOC_AN383
CONFIG_ARMV7_M_ARMV8_M_MAINLINE
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:144`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L144)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M0`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M0)、[`CONFIG_CPU_CORTEX_M1`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M1)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC)、[`CONFIG_SOC_SERIES_PSOC4000T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSOC4000T)、[`CONFIG_SOC_SERIES_PSOC4100SMAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSOC4100SMAX)、[`CONFIG_SOC_SERIES_PSOC4100TP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSOC4100TP)、[`CONFIG_SOC_AM13E23019`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AM13E23019)、[`CONFIG_SOC_FT9001`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FT9001)、[`CONFIG_SOC_SERIES_LPC51U68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC51U68)、[`CONFIG_SOC_LPC54114_M0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC54114_M0)、[`CONFIG_SOC_SERIES_LPC84X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC84X)、[`CONFIG_SOC_SERIES_SAMC20`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMC20)、[`CONFIG_SOC_SERIES_SAMC21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMC21)、[`CONFIG_SOC_SERIES_SAMD20`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMD20)、[`CONFIG_SOC_SERIES_SAMD21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMD21)、[`CONFIG_SOC_SERIES_SAML21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAML21)、[`CONFIG_SOC_SERIES_SAMR21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMR21)、[`CONFIG_SOC_SERIES_SAMR34`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMR34)、[`CONFIG_SOC_SERIES_SAMR35`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMR35)、[`CONFIG_SOC_SERIES_RP2040`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RP2040)、[`CONFIG_SOC_RP2350A_M33_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350A_M33_0)、[`CONFIG_SOC_RP2350B_M33_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350B_M33_0)、[`CONFIG_SOC_SERIES_RA0E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA0E1)、[`CONFIG_SOC_SERIES_RA2A1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA2A1)、[`CONFIG_SOC_SERIES_RA2L1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA2L1)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC)、[`CONFIG_SOC_FAMILY_MCXC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXC)、[`CONFIG_SOC_FAMILY_MCXL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXL)、[`CONFIG_SOC_SERIES_EFM32HG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32HG)、[`CONFIG_SOC_SERIES_M2L31X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M2L31X)、[`CONFIG_SOC_SERIES_M333X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M333X)、[`CONFIG_SOC_SERIES_M335X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M335X)、[`CONFIG_SOC_SERIES_M55M1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M55M1X)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA)、[`CONFIG_SOC_SERIES_K32LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K32LX)、[`CONFIG_SOC_SERIES_KE1XZ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KE1XZ)、[`CONFIG_SOC_SERIES_KL2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KL2X)、[`CONFIG_SOC_SERIES_KWX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KWX)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY_M0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY_M0)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL)、[`CONFIG_SOC_CYT4DNJBZS_M0P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4DNJBZS_M0P)、[`CONFIG_SOC_CYT4DNJBZS_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4DNJBZS_M7_0)、[`CONFIG_SOC_CYT4DNJBZS_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4DNJBZS_M7_1)、[`CONFIG_SOC_SERIES_XMC7200`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XMC7200)、[`CONFIG_SOC_SERIES_GD32C2X1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32C2X1)、[`CONFIG_SOC_SERIES_GD32E10X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32E10X)、[`CONFIG_SOC_SERIES_GD32F403`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32F403)、[`CONFIG_SOC_SERIES_GD32L23X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32L23X)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH)、[`CONFIG_SOC_SERIES_CC23X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC23X0)、[`CONFIG_SOC_SERIES_APOLLO5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO5X)、[`CONFIG_SOC_FAMILY_ENSEMBLE_RTSS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ENSEMBLE_RTSS)、[`CONFIG_SOC_SERIES_B1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_B1)、[`CONFIG_SOC_SERIES_RTL8752H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTL8752H)、[`CONFIG_SOC_SERIES_MSPM0G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSPM0G)、[`CONFIG_SOC_SERIES_MSPM0L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSPM0L)、[`CONFIG_SOC_SERIES_STM32C0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32C0X)、[`CONFIG_SOC_SERIES_STM32G0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32G0X)、[`CONFIG_SOC_SERIES_STM32L0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L0X)、[`CONFIG_SOC_SERIES_STM32U0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U0X)、[`CONFIG_SOC_SERIES_STM32WB0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WB0X)、[`CONFIG_SOC_SERIES_STM32WL3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WL3X)、[`CONFIG_SOC_AN383`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AN383)、[`CONFIG_ARMV7_M_ARMV8_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_M_ARMV8_M_MAINLINE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`、`CONFIG_SOC_AM13E23019`、`CONFIG_SOC_SERIES_LPC51U68`、`CONFIG_SOC_LPC54114_M0`、`CONFIG_SOC_SERIES_LPC84X`、`CONFIG_SOC_SERIES_RA2L1`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC`、`CONFIG_SOC_FAMILY_MCXC`、`CONFIG_SOC_FAMILY_MCXL`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`、`CONFIG_SOC_SERIES_K32LX`、`CONFIG_SOC_SERIES_KE1XZ`、`CONFIG_SOC_SERIES_KL2X`、`CONFIG_SOC_SERIES_KWX`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY_M0`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL`、`CONFIG_SOC_CYT4DNJBZS_M0P`、`CONFIG_SOC_CYT4DNJBZS_M7_0`、`CONFIG_SOC_CYT4DNJBZS_M7_1`、`CONFIG_SOC_SERIES_XMC7200`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`、`CONFIG_SOC_FAMILY_ENSEMBLE_RTSS`、`CONFIG_SOC_SERIES_B1`、`CONFIG_SOC_SERIES_STM32C0X`、`CONFIG_SOC_SERIES_STM32G0X`、`CONFIG_SOC_SERIES_STM32L0X`、`CONFIG_SOC_SERIES_STM32U0X`、`CONFIG_SOC_SERIES_STM32WB0X`、`CONFIG_SOC_SERIES_STM32WL3X`。

<a id="CONFIG_CPU_CORTEX_R4"></a>

## 30.8 `CONFIG_CPU_CORTEX_R4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-R4 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_AARCH32_CORTEX_R
CONFIG_ARMV7_R
CONFIG_ARMV7_R_FP if CONFIG_CPU_HAS_FPU
```

**定义位置（Location）**：[`arch/arm/core/cortex_a_r/Kconfig:158`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_a_r/Kconfig#L158)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_AARCH32_CORTEX_R`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_R)、[`CONFIG_ARMV7_R`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_R)、[`CONFIG_ARMV7_R_FP`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_R_FP)、[`CONFIG_CPU_HAS_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU)。

<a id="CONFIG_CPU_CORTEX_R5"></a>

## 30.9 `CONFIG_CPU_CORTEX_R5`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-R5 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_AARCH32_CORTEX_R
CONFIG_ARMV7_R
CONFIG_ARMV7_R_FP if CONFIG_CPU_HAS_FPU
CONFIG_CPU_HAS_ICACHE
CONFIG_CPU_HAS_DCACHE
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_AM64X_R5
CONFIG_SOC_SERIES_J721E_R5
CONFIG_SOC_SERIES_J722S_R5
CONFIG_SOC_XILINX_ZYNQMP_RPU
CONFIG_SOC_VERSAL_RPU
```

**定义位置（Location）**：[`arch/arm/core/cortex_a_r/Kconfig:166`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_a_r/Kconfig#L166)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_AARCH32_CORTEX_R`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_R)、[`CONFIG_ARMV7_R`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_R)、[`CONFIG_ARMV7_R_FP`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_R_FP)、[`CONFIG_CPU_HAS_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU)、[`CONFIG_CPU_HAS_ICACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_ICACHE)、[`CONFIG_CPU_HAS_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCACHE)、[`CONFIG_SOC_SERIES_AM64X_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM64X_R5)、[`CONFIG_SOC_SERIES_J721E_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_J721E_R5)、[`CONFIG_SOC_SERIES_J722S_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_J722S_R5)、[`CONFIG_SOC_XILINX_ZYNQMP_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XILINX_ZYNQMP_RPU)、[`CONFIG_SOC_VERSAL_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_VERSAL_RPU)。

<a id="CONFIG_CPU_CORTEX_R52"></a>

## 30.10 `CONFIG_CPU_CORTEX_R52`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-R52 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_AARCH32_CORTEX_R
CONFIG_AARCH32_ARMV8_R
CONFIG_CPU_HAS_ICACHE
CONFIG_CPU_HAS_DCACHE
CONFIG_VFP_SP_D16 if !CONFIG_USE_SWITCH
```

**被选择（Selected by）**

```text
CONFIG_SOC_R8A779F0_R52
CONFIG_SOC_R8A779G0_R52
CONFIG_SOC_R8A78000_R52
CONFIG_SOC_SERIES_RZN2H
CONFIG_SOC_SERIES_RZN2L
CONFIG_SOC_SERIES_RZT2H
CONFIG_SOC_SERIES_RZT2L
CONFIG_SOC_SERIES_RZT2M
CONFIG_SOC_AMD_VERSALNET_RPU
CONFIG_SOC_AMD_VERSAL2_RPU
CONFIG_SOC_FVP_AEMV8R_AARCH32
CONFIG_SOC_AN536
CONFIG_SOC_S32K566_R52
CONFIG_SOC_SERIES_S32ZE
```

**定义位置（Location）**：[`arch/arm/core/cortex_a_r/Kconfig:192`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_a_r/Kconfig#L192)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_AARCH32_CORTEX_R`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_R)、[`CONFIG_AARCH32_ARMV8_R`](P029_arch_arm_配置项参考_1.md#CONFIG_AARCH32_ARMV8_R)、[`CONFIG_CPU_HAS_ICACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_ICACHE)、[`CONFIG_CPU_HAS_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCACHE)、[`CONFIG_VFP_SP_D16`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_SP_D16)、[`CONFIG_USE_SWITCH`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH)、[`CONFIG_SOC_R8A779F0_R52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A779F0_R52)、[`CONFIG_SOC_R8A779G0_R52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A779G0_R52)、[`CONFIG_SOC_R8A78000_R52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A78000_R52)、[`CONFIG_SOC_SERIES_RZN2H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZN2H)、[`CONFIG_SOC_SERIES_RZN2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZN2L)、[`CONFIG_SOC_SERIES_RZT2H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2H)、[`CONFIG_SOC_SERIES_RZT2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2L)、[`CONFIG_SOC_SERIES_RZT2M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2M)、[`CONFIG_SOC_AMD_VERSALNET_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSALNET_RPU)、[`CONFIG_SOC_AMD_VERSAL2_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSAL2_RPU)、[`CONFIG_SOC_FVP_AEMV8R_AARCH32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FVP_AEMV8R_AARCH32)、[`CONFIG_SOC_AN536`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AN536)、[`CONFIG_SOC_S32K566_R52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K566_R52)、[`CONFIG_SOC_SERIES_S32ZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32ZE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_R8A779G0_R52`、`CONFIG_SOC_FVP_AEMV8R_AARCH32`、`CONFIG_SOC_AN536`、`CONFIG_SOC_S32K566_R52`、`CONFIG_SOC_SERIES_S32ZE`。

<a id="CONFIG_CPU_CORTEX_R52_CACHE_SEGREGATION"></a>

## 30.11 `CONFIG_CPU_CORTEX_R52_CACHE_SEGREGATION`

**提示（Prompt）**：控制 Flash 与 AXIM 之间的 L1 指令／数据缓存路划分（Cache Way Segregation）

**说明（Help）**

控制 Flash 与 AXIM 之间的 L1 指令／数据缓存路划分（Cache Way Segregation）。仅允许在系统复位后、缓存尚未被启用过之前更新划分控制；否则更新会被忽略。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_R52 && CONFIG_ARM
```

**定义位置（Location）**：[`arch/arm/core/cortex_a_r/Kconfig:202`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_a_r/Kconfig#L202)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_R52`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_R52)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_CPU_CORTEX_R52_DCACHE_FLASH_WAY"></a>

## 30.12 `CONFIG_CPU_CORTEX_R52_DCACHE_FLASH_WAY`

**提示（Prompt）**：L1 数据缓存的 Flash 路（D-cache Flash Ways）

**说明（Help）**

为 Flash 接口配置 L1 数据缓存路（D-cache Ways）。默认采用复位值，即所有数据缓存路都分配给 AXIM 接口。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_R52_CACHE_SEGREGATION && CONFIG_ARM
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 4]
```

**定义位置（Location）**：[`arch/arm/core/cortex_a_r/Kconfig:219`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_a_r/Kconfig#L219)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options） → 控制 Flash 与 AXIM 之间的 L1 指令／数据缓存路划分（Cache Way Segregation）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_R52_CACHE_SEGREGATION`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_R52_CACHE_SEGREGATION)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_CPU_CORTEX_R52_ICACHE_FLASH_WAY"></a>

## 30.13 `CONFIG_CPU_CORTEX_R52_ICACHE_FLASH_WAY`

**提示（Prompt）**：L1 指令缓存的 Flash 路（I-cache Flash Ways）

**说明（Help）**

为 Flash 接口配置 L1 指令缓存路（I-cache Ways）。默认采用复位值，即所有指令缓存路都分配给 AXIM 接口。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_R52_CACHE_SEGREGATION && CONFIG_ARM
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 4]
```

**定义位置（Location）**：[`arch/arm/core/cortex_a_r/Kconfig:210`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_a_r/Kconfig#L210)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options） → 控制 Flash 与 AXIM 之间的 L1 指令／数据缓存路划分（Cache Way Segregation）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_R52_CACHE_SEGREGATION`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_R52_CACHE_SEGREGATION)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_CPU_CORTEX_R7"></a>

## 30.14 `CONFIG_CPU_CORTEX_R7`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-R7 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_AARCH32_CORTEX_R
CONFIG_ARMV7_R
CONFIG_ARMV7_R_FP if CONFIG_CPU_HAS_FPU
```

**被选择（Selected by）**

```text
CONFIG_SOC_R8A77951_R7
```

**定义位置（Location）**：[`arch/arm/core/cortex_a_r/Kconfig:176`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_a_r/Kconfig#L176)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_AARCH32_CORTEX_R`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_R)、[`CONFIG_ARMV7_R`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_R)、[`CONFIG_ARMV7_R_FP`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_R_FP)、[`CONFIG_CPU_HAS_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU)、[`CONFIG_SOC_R8A77951_R7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A77951_R7)。

<a id="CONFIG_CPU_CORTEX_R8"></a>

## 30.15 `CONFIG_CPU_CORTEX_R8`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-R8 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_AARCH32_CORTEX_R
CONFIG_ARMV7_R
CONFIG_ARMV7_R_FP if CONFIG_CPU_HAS_FPU
```

**被选择（Selected by）**

```text
CONFIG_SOC_CORTEX_R8_VIRTUAL
CONFIG_SOC_R9A09G057H44GBG_CR8
```

**定义位置（Location）**：[`arch/arm/core/cortex_a_r/Kconfig:184`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_a_r/Kconfig#L184)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_AARCH32_CORTEX_R`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_R)、[`CONFIG_ARMV7_R`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_R)、[`CONFIG_ARMV7_R_FP`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_R_FP)、[`CONFIG_CPU_HAS_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU)、[`CONFIG_SOC_CORTEX_R8_VIRTUAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORTEX_R8_VIRTUAL)、[`CONFIG_SOC_R9A09G057H44GBG_CR8`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R9A09G057H44GBG_CR8)。

<a id="CONFIG_CPU_HAS_ARM_MPU"></a>

## 30.16 `CONFIG_CPU_HAS_ARM_MPU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CPU 具有 ARM 类型的内存保护单元（Memory Protection Unit，MPU）时，启用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_HAS_MPU
```

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC
CONFIG_SOC_SERIES_PSOC4100SMAX
CONFIG_SOC_R8A78000_R52
CONFIG_SOC_AM13E23019
CONFIG_SOC_FT9001
CONFIG_SOC_LPC54114_M4
CONFIG_SOC_LPC54628
CONFIG_SOC_LPC55S06
CONFIG_SOC_LPC55S16
CONFIG_SOC_LPC55S26
CONFIG_SOC_LPC55S28
CONFIG_SOC_LPC55S36
CONFIG_SOC_LPC55S69_CPU0
CONFIG_SOC_SR100
CONFIG_SOC_SERIES_MEC15XX
CONFIG_SOC_SERIES_MEC165XB
CONFIG_SOC_SERIES_MEC172X
CONFIG_SOC_SERIES_MEC174X
CONFIG_SOC_SERIES_MEC175X
CONFIG_SOC_CORTEX_R8_VIRTUAL
CONFIG_SOC_EOS_S3
CONFIG_SOC_SERIES_SAMC21
CONFIG_SOC_SERIES_SAMD51
CONFIG_SOC_SERIES_SAME51
CONFIG_SOC_SERIES_SAME53
CONFIG_SOC_SERIES_SAME54
CONFIG_SOC_SERIES_VALKYRIE
CONFIG_SOC_BCM58402_M7
CONFIG_SOC_SERIES_RP2040
CONFIG_SOC_RP2350A_M33_0
CONFIG_SOC_RP2350B_M33_0
CONFIG_SOC_KB1200
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
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC
CONFIG_SOC_SERIES_MCXAXX6
CONFIG_SOC_SERIES_MCXAXX4
CONFIG_SOC_SERIES_MCXAXX7
CONFIG_SOC_SERIES_MCXE31X
CONFIG_SOC_MCXL255_CPU0
CONFIG_SOC_MCXL254_CPU0
CONFIG_SOC_MCXL253_CPU0
CONFIG_SOC_MCXN947_CPU0
CONFIG_SOC_MCXN547_CPU0
CONFIG_SOC_MCXN236
CONFIG_SOC_FAMILY_MCXW
CONFIG_SOC_SERIES_MCXW2XX
CONFIG_SOC_SERIES_AM64X_R5
CONFIG_SOC_SERIES_J721E_R5
CONFIG_SOC_SERIES_J722S_R5
CONFIG_SOC_SERIES_EFM32WG
CONFIG_SOC_SERIES_EFM32GG11B
CONFIG_SOC_SERIES_EFM32GG12B
CONFIG_SOC_SERIES_EFM32JG12B
CONFIG_SOC_SERIES_EFM32PG12B
CONFIG_SOC_SERIES_EFM32PG1B
CONFIG_SOC_SERIES_EFR32BG13P
CONFIG_SOC_SERIES_EFR32FG13P
CONFIG_SOC_SERIES_EFR32FG1P
CONFIG_SOC_SERIES_EFR32MG12P
CONFIG_SOC_SERIES_EFR32MG13P
CONFIG_SOC_FAMILY_SILABS_S2_XG21
CONFIG_SOC_FAMILY_SILABS_S2_XG22
CONFIG_SOC_FAMILY_SILABS_S2_XG23
CONFIG_SOC_FAMILY_SILABS_S2_XG24
CONFIG_SOC_FAMILY_SILABS_S2_XG26
CONFIG_SOC_FAMILY_SILABS_S2_XG27
CONFIG_SOC_FAMILY_SILABS_S2_XG28
CONFIG_SOC_FAMILY_SILABS_S2_XG29
CONFIG_SOC_FAMILY_SILABS_S3_SIX301
CONFIG_SOC_FAMILY_SILABS_SIWX91X
CONFIG_SOC_MIMXRT1011
CONFIG_SOC_MIMXRT1015
CONFIG_SOC_MIMXRT1021
CONFIG_SOC_MIMXRT1024
CONFIG_SOC_MIMXRT1041
CONFIG_SOC_MIMXRT1042
CONFIG_SOC_MIMXRT1051
CONFIG_SOC_MIMXRT1052
CONFIG_SOC_MIMXRT1062
CONFIG_SOC_MIMXRT1064
CONFIG_SOC_SERIES_IMXRT118X
CONFIG_SOC_SERIES_IMXRT11XX
CONFIG_SOC_SERIES_IMXRT266X_CM85
CONFIG_SOC_MIMXRT595S_CM33
CONFIG_SOC_MIMXRT685S_CM33
CONFIG_SOC_MIMXRT798S_CM33_CPU0
CONFIG_SOC_MIMXRT798S_CM33_CPU1
CONFIG_SOC_MIMXRT758S_CM33_CPU0
CONFIG_SOC_MIMXRT758S_CM33_CPU1
CONFIG_SOC_MIMXRT735S_CM33_CPU0
CONFIG_SOC_MIMXRT735S_CM33_CPU1
CONFIG_SOC_SERIES_M2L31X
CONFIG_SOC_SERIES_M333X
CONFIG_SOC_SERIES_M335X
CONFIG_SOC_SERIES_M46X
CONFIG_SOC_SERIES_M55M1X
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA
CONFIG_SOC_SERIES_KV5X
CONFIG_SOC_SERIES_SF32LB52X
CONFIG_SOC_SERIES_AST10X0
CONFIG_SOC_SERIES_NRF52
CONFIG_SOC_SERIES_NRF53
CONFIG_SOC_NRF54H20_CPUAPP_COMMON
CONFIG_SOC_NRF54H20_CPURAD_COMMON
CONFIG_SOC_NRF54L05_CPUAPP
CONFIG_SOC_NRF54L10_CPUAPP
CONFIG_SOC_NRF54L15_CPUAPP
CONFIG_SOC_NRF54LM20A_CPUAPP
CONFIG_SOC_NRF54LM20B_CPUAPP
CONFIG_SOC_NRF54LV10A_CPUAPP
CONFIG_SOC_NRF7120_ENGA_CPUAPP
CONFIG_SOC_NRF7120E_ENGA_CPUAPP
CONFIG_SOC_SERIES_NRF91
CONFIG_SOC_NRF9230_ENGB_CPUAPP
CONFIG_SOC_NRF9230_ENGB_CPURAD
CONFIG_SOC_SERIES_TM4C123X
CONFIG_SOC_SERIES_AMEBAD
CONFIG_SOC_SERIES_AMEBADPLUS
CONFIG_SOC_SERIES_AMEBAG2
CONFIG_SOC_FAMILY_PSOC6
CONFIG_SOC_FAMILY_PSOC6_LEGACY
CONFIG_SOC_SERIES_IMX6SX
CONFIG_SOC_SERIES_IMX7D
CONFIG_SOC_MIMX8MM6_M4
CONFIG_SOC_MIMX8ML8_M7
CONFIG_SOC_MIMX8MQ6_M4
CONFIG_SOC_MIMX9352_M33
CONFIG_SOC_MIMX94398_M33
CONFIG_SOC_MIMX94398_M7_0
CONFIG_SOC_MIMX94398_M7_1
CONFIG_SOC_MIMX9596_M7
CONFIG_SOC_MIMX9529_M7
CONFIG_SOC_SERIES_PSE84
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG
CONFIG_SOC_CYT4DNJBZS_M0P
CONFIG_SOC_CYT4DNJBZS_M7_0
CONFIG_SOC_CYT4DNJBZS_M7_1
CONFIG_SOC_SERIES_XMC7200
CONFIG_SOC_SERIES_CYW20829
CONFIG_SOC_SERIES_PSC3
CONFIG_SOC_SERIES_GD32A50X
CONFIG_SOC_SERIES_GD32E50X
CONFIG_SOC_SERIES_GD32F403
CONFIG_SOC_SERIES_GD32F4XX
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH
CONFIG_SOC_SERIES_CC13X2_CC26X2
CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7
CONFIG_SOC_SERIES_MSP432P4XX
CONFIG_SOC_XILINX_ZYNQMP_RPU
CONFIG_SOC_SERIES_NPCM4
CONFIG_SOC_SERIES_APOLLO2X
CONFIG_SOC_SERIES_APOLLO3X
CONFIG_SOC_SERIES_APOLLO4X
CONFIG_SOC_SERIES_APOLLO5X
CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X
CONFIG_SOC_VERSAL_RPU
CONFIG_SOC_FAMILY_ENSEMBLE_RTSS
CONFIG_SOC_SERIES_DA1469X
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
CONFIG_SOC_SERIES_B1
CONFIG_SOC_EM32F967
CONFIG_SOC_SERIES_SAM3X
CONFIG_SOC_SERIES_SAM4E
CONFIG_SOC_SERIES_SAM4L
CONFIG_SOC_SERIES_SAM4S
CONFIG_SOC_SERIES_SAMX7X
CONFIG_SOC_SERIES_SMARTFUSION2
CONFIG_SOC_SERIES_XMC4XXX
CONFIG_SOC_AMD_VERSALNET_RPU
CONFIG_SOC_SERIES_RTL8752H
CONFIG_SOC_SERIES_RTL87X2G
CONFIG_SOC_FAMILY_MAX32_M33
CONFIG_SOC_FAMILY_MAX32_M4
CONFIG_SOC_RTS5817
CONFIG_SOC_SERIES_MSPM0G
CONFIG_SOC_MSPM0L1117
CONFIG_SOC_MSPM0L2227
CONFIG_SOC_MSPM0L2228
CONFIG_SOC_SERIES_MSPM33C
CONFIG_SOC_AMD_VERSAL2_RPU
CONFIG_SOC_SERIES_M48X
CONFIG_SOC_SERIES_STM32C0X
CONFIG_SOC_SERIES_STM32C5X
CONFIG_SOC_SERIES_STM32F2X
CONFIG_SOC_SERIES_STM32F4X
CONFIG_SOC_SERIES_STM32F7X
CONFIG_SOC_SERIES_STM32G0X
CONFIG_SOC_SERIES_STM32G4X
CONFIG_SOC_SERIES_STM32H5X
CONFIG_SOC_SERIES_STM32H7RSX
CONFIG_SOC_SERIES_STM32H7X
CONFIG_SOC_STM32L051XX
CONFIG_SOC_STM32L053XX
CONFIG_SOC_STM32L071XX
CONFIG_SOC_STM32L072XX
CONFIG_SOC_STM32L073XX
CONFIG_SOC_STM32L081XX
CONFIG_SOC_STM32L083XX
CONFIG_SOC_SERIES_STM32L1X
CONFIG_SOC_SERIES_STM32L4X
CONFIG_SOC_SERIES_STM32L5X
CONFIG_SOC_SERIES_STM32MP1X
CONFIG_SOC_STM32MP2X_M33
CONFIG_SOC_SERIES_STM32N6X
CONFIG_SOC_SERIES_STM32U0X
CONFIG_SOC_SERIES_STM32U3X
CONFIG_SOC_SERIES_STM32U5X
CONFIG_SOC_SERIES_STM32WB0X
CONFIG_SOC_SERIES_STM32WBAX
CONFIG_SOC_SERIES_STM32WBX
CONFIG_SOC_SERIES_STM32WL3X
CONFIG_SOC_SERIES_STM32WLX
CONFIG_SOC_SERIES_BEETLE
CONFIG_SOC_FVP_AEMV8R_AARCH32
CONFIG_SOC_AN521
CONFIG_SOC_AN383
CONFIG_SOC_AN385
CONFIG_SOC_AN386
CONFIG_SOC_AN500
CONFIG_SOC_CORSTONE300
CONFIG_SOC_CORSTONE310
CONFIG_SOC_AN536
CONFIG_SOC_CORSTONE315
CONFIG_SOC_CORSTONE320
CONFIG_SOC_MUSCA_B1
CONFIG_SOC_MUSCA_S1
CONFIG_SOC_SERIES_NPCK3
CONFIG_SOC_SERIES_NPCX4
CONFIG_SOC_SERIES_NPCX7
CONFIG_SOC_SERIES_NPCX9
CONFIG_SOC_SERIES_RW6XX
CONFIG_SOC_SERIES_S32K3
CONFIG_SOC_SERIES_S32K5
CONFIG_SOC_SERIES_S32ZE
```

**定义位置（Location）**：[`arch/arm/Kconfig:156`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/Kconfig#L156)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_HAS_MPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MPU)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC)、[`CONFIG_SOC_SERIES_PSOC4100SMAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSOC4100SMAX)、[`CONFIG_SOC_R8A78000_R52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A78000_R52)、[`CONFIG_SOC_AM13E23019`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AM13E23019)、[`CONFIG_SOC_FT9001`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FT9001)、[`CONFIG_SOC_LPC54114_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC54114_M4)、[`CONFIG_SOC_LPC54628`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC54628)、[`CONFIG_SOC_LPC55S06`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S06)、[`CONFIG_SOC_LPC55S16`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S16)、[`CONFIG_SOC_LPC55S26`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S26)、[`CONFIG_SOC_LPC55S28`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S28)、[`CONFIG_SOC_LPC55S36`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S36)、[`CONFIG_SOC_LPC55S69_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S69_CPU0)、[`CONFIG_SOC_SR100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SR100)、[`CONFIG_SOC_SERIES_MEC15XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC15XX)、[`CONFIG_SOC_SERIES_MEC165XB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC165XB)、[`CONFIG_SOC_SERIES_MEC172X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC172X)、[`CONFIG_SOC_SERIES_MEC174X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC174X)、[`CONFIG_SOC_SERIES_MEC175X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC175X)、[`CONFIG_SOC_CORTEX_R8_VIRTUAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORTEX_R8_VIRTUAL)、[`CONFIG_SOC_EOS_S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EOS_S3)、[`CONFIG_SOC_SERIES_SAMC21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMC21)、[`CONFIG_SOC_SERIES_SAMD51`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMD51)、[`CONFIG_SOC_SERIES_SAME51`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAME51)、[`CONFIG_SOC_SERIES_SAME53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAME53)、[`CONFIG_SOC_SERIES_SAME54`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAME54)、[`CONFIG_SOC_SERIES_VALKYRIE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_VALKYRIE)、[`CONFIG_SOC_BCM58402_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BCM58402_M7)、[`CONFIG_SOC_SERIES_RP2040`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RP2040)、[`CONFIG_SOC_RP2350A_M33_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350A_M33_0)、[`CONFIG_SOC_RP2350B_M33_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350B_M33_0)、[`CONFIG_SOC_KB1200`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_KB1200)、[`CONFIG_SOC_SERIES_RA2A1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA2A1)、[`CONFIG_SOC_SERIES_RA2L1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA2L1)、[`CONFIG_SOC_SERIES_RA4C1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4C1)、[`CONFIG_SOC_SERIES_RA4E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4E1)、[`CONFIG_SOC_SERIES_RA4E2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4E2)、[`CONFIG_SOC_SERIES_RA4L1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4L1)、[`CONFIG_SOC_SERIES_RA4M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M1)、[`CONFIG_SOC_SERIES_RA4M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M2)、[`CONFIG_SOC_SERIES_RA4M3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M3)、[`CONFIG_SOC_SERIES_RA4T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4T1)、[`CONFIG_SOC_SERIES_RA4W1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4W1)、[`CONFIG_SOC_SERIES_RA6E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6E1)、[`CONFIG_SOC_SERIES_RA6E2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6E2)、[`CONFIG_SOC_SERIES_RA6M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M1)、[`CONFIG_SOC_SERIES_RA6M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M2)、[`CONFIG_SOC_SERIES_RA6M3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M3)、[`CONFIG_SOC_SERIES_RA6M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M4)、[`CONFIG_SOC_SERIES_RA6M5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M5)、[`CONFIG_SOC_SERIES_RA8D1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8D1)、[`CONFIG_SOC_SERIES_RA8D2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8D2)、[`CONFIG_SOC_SERIES_RA8E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8E1)、[`CONFIG_SOC_SERIES_RA8M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8M1)、[`CONFIG_SOC_SERIES_RA8M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8M2)、[`CONFIG_SOC_SERIES_RA8P1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8P1)、[`CONFIG_SOC_SERIES_RA8T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8T1)、[`CONFIG_SOC_SERIES_RA8T2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8T2)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC)、[`CONFIG_SOC_SERIES_MCXAXX6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXAXX6)、[`CONFIG_SOC_SERIES_MCXAXX4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXAXX4)、[`CONFIG_SOC_SERIES_MCXAXX7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXAXX7)、[`CONFIG_SOC_SERIES_MCXE31X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE31X)、[`CONFIG_SOC_MCXL255_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL255_CPU0)、[`CONFIG_SOC_MCXL254_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL254_CPU0)、[`CONFIG_SOC_MCXL253_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL253_CPU0)、[`CONFIG_SOC_MCXN947_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN947_CPU0)、[`CONFIG_SOC_MCXN547_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN547_CPU0)、[`CONFIG_SOC_MCXN236`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN236)、[`CONFIG_SOC_FAMILY_MCXW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXW)、[`CONFIG_SOC_SERIES_MCXW2XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXW2XX)、[`CONFIG_SOC_SERIES_AM64X_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM64X_R5)、[`CONFIG_SOC_SERIES_J721E_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_J721E_R5)、[`CONFIG_SOC_SERIES_J722S_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_J722S_R5)、[`CONFIG_SOC_SERIES_EFM32WG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32WG)、[`CONFIG_SOC_SERIES_EFM32GG11B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32GG11B)、[`CONFIG_SOC_SERIES_EFM32GG12B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32GG12B)、[`CONFIG_SOC_SERIES_EFM32JG12B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32JG12B)、[`CONFIG_SOC_SERIES_EFM32PG12B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32PG12B)、[`CONFIG_SOC_SERIES_EFM32PG1B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32PG1B)、[`CONFIG_SOC_SERIES_EFR32BG13P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32BG13P)、[`CONFIG_SOC_SERIES_EFR32FG13P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32FG13P)、[`CONFIG_SOC_SERIES_EFR32FG1P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32FG1P)、[`CONFIG_SOC_SERIES_EFR32MG12P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32MG12P)、[`CONFIG_SOC_SERIES_EFR32MG13P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32MG13P)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG21)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG22`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG22)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG23`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG23)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG24`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG24)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG26`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG26)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG27`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG27)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG28`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG28)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG29`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG29)、[`CONFIG_SOC_FAMILY_SILABS_S3_SIX301`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S3_SIX301)、[`CONFIG_SOC_FAMILY_SILABS_SIWX91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_SIWX91X)、[`CONFIG_SOC_MIMXRT1011`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1011)、[`CONFIG_SOC_MIMXRT1015`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1015)、[`CONFIG_SOC_MIMXRT1021`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1021)、[`CONFIG_SOC_MIMXRT1024`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1024)、[`CONFIG_SOC_MIMXRT1041`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1041)、[`CONFIG_SOC_MIMXRT1042`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1042)、[`CONFIG_SOC_MIMXRT1051`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1051)、[`CONFIG_SOC_MIMXRT1052`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1052)、[`CONFIG_SOC_MIMXRT1062`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1062)、[`CONFIG_SOC_MIMXRT1064`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1064)、[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_SERIES_IMXRT266X_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT266X_CM85)、[`CONFIG_SOC_MIMXRT595S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT595S_CM33)、[`CONFIG_SOC_MIMXRT685S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_CM33)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU1)、[`CONFIG_SOC_MIMXRT758S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT758S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_CM33_CPU1)、[`CONFIG_SOC_MIMXRT735S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT735S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_CM33_CPU1)、[`CONFIG_SOC_SERIES_M2L31X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M2L31X)、[`CONFIG_SOC_SERIES_M333X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M333X)、[`CONFIG_SOC_SERIES_M335X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M335X)、[`CONFIG_SOC_SERIES_M46X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M46X)、[`CONFIG_SOC_SERIES_M55M1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M55M1X)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA)、[`CONFIG_SOC_SERIES_KV5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KV5X)、[`CONFIG_SOC_SERIES_SF32LB52X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SF32LB52X)、[`CONFIG_SOC_SERIES_AST10X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AST10X0)、[`CONFIG_SOC_SERIES_NRF52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF52)、[`CONFIG_SOC_SERIES_NRF53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_NRF54H20_CPUAPP_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPUAPP_COMMON)、[`CONFIG_SOC_NRF54H20_CPURAD_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPURAD_COMMON)、[`CONFIG_SOC_NRF54L05_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54L05_CPUAPP)、[`CONFIG_SOC_NRF54L10_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54L10_CPUAPP)、[`CONFIG_SOC_NRF54L15_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54L15_CPUAPP)、[`CONFIG_SOC_NRF54LM20A_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54LM20A_CPUAPP)、[`CONFIG_SOC_NRF54LM20B_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54LM20B_CPUAPP)、[`CONFIG_SOC_NRF54LV10A_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54LV10A_CPUAPP)、[`CONFIG_SOC_NRF7120_ENGA_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF7120_ENGA_CPUAPP)、[`CONFIG_SOC_NRF7120E_ENGA_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF7120E_ENGA_CPUAPP)、[`CONFIG_SOC_SERIES_NRF91`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF91)、[`CONFIG_SOC_NRF9230_ENGB_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9230_ENGB_CPUAPP)、[`CONFIG_SOC_NRF9230_ENGB_CPURAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9230_ENGB_CPURAD)、[`CONFIG_SOC_SERIES_TM4C123X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_TM4C123X)、[`CONFIG_SOC_SERIES_AMEBAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAD)、[`CONFIG_SOC_SERIES_AMEBADPLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBADPLUS)、[`CONFIG_SOC_SERIES_AMEBAG2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAG2)、[`CONFIG_SOC_FAMILY_PSOC6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_SERIES_IMX6SX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMX6SX)、[`CONFIG_SOC_SERIES_IMX7D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMX7D)、[`CONFIG_SOC_MIMX8MM6_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8MM6_M4)、[`CONFIG_SOC_MIMX8ML8_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8ML8_M7)、[`CONFIG_SOC_MIMX8MQ6_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8MQ6_M4)、[`CONFIG_SOC_MIMX9352_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9352_M33)、[`CONFIG_SOC_MIMX94398_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M33)、[`CONFIG_SOC_MIMX94398_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M7_0)、[`CONFIG_SOC_MIMX94398_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M7_1)、[`CONFIG_SOC_MIMX9596_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9596_M7)、[`CONFIG_SOC_MIMX9529_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9529_M7)、[`CONFIG_SOC_SERIES_PSE84`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSE84)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG)、[`CONFIG_SOC_CYT4DNJBZS_M0P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4DNJBZS_M0P)、[`CONFIG_SOC_CYT4DNJBZS_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4DNJBZS_M7_0)、[`CONFIG_SOC_CYT4DNJBZS_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4DNJBZS_M7_1)、[`CONFIG_SOC_SERIES_XMC7200`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XMC7200)、[`CONFIG_SOC_SERIES_CYW20829`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CYW20829)、[`CONFIG_SOC_SERIES_PSC3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSC3)、[`CONFIG_SOC_SERIES_GD32A50X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32A50X)、[`CONFIG_SOC_SERIES_GD32E50X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32E50X)、[`CONFIG_SOC_SERIES_GD32F403`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32F403)、[`CONFIG_SOC_SERIES_GD32F4XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32F4XX)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH)、[`CONFIG_SOC_SERIES_CC13X2_CC26X2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC13X2_CC26X2)、[`CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7)、[`CONFIG_SOC_SERIES_MSP432P4XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSP432P4XX)、[`CONFIG_SOC_XILINX_ZYNQMP_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XILINX_ZYNQMP_RPU)、[`CONFIG_SOC_SERIES_NPCM4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCM4)、[`CONFIG_SOC_SERIES_APOLLO2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO2X)、[`CONFIG_SOC_SERIES_APOLLO3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO3X)、[`CONFIG_SOC_SERIES_APOLLO4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO4X)、[`CONFIG_SOC_SERIES_APOLLO5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO5X)、[`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X)、[`CONFIG_SOC_VERSAL_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_VERSAL_RPU)、[`CONFIG_SOC_FAMILY_ENSEMBLE_RTSS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ENSEMBLE_RTSS)、[`CONFIG_SOC_SERIES_DA1469X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_DA1469X)、[`CONFIG_SOC_SERIES_RZG2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZG2L)、[`CONFIG_SOC_SERIES_RZG2UL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZG2UL)、[`CONFIG_SOC_SERIES_RZG3E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZG3E)、[`CONFIG_SOC_SERIES_RZG3S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZG3S)、[`CONFIG_SOC_SERIES_RZN2H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZN2H)、[`CONFIG_SOC_SERIES_RZN2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZN2L)、[`CONFIG_SOC_SERIES_RZT2H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2H)、[`CONFIG_SOC_SERIES_RZT2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2L)、[`CONFIG_SOC_SERIES_RZT2M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2M)、[`CONFIG_SOC_R9A09G057H44GBG_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R9A09G057H44GBG_CM33)、[`CONFIG_SOC_R9A09G057H44GBG_CR8`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R9A09G057H44GBG_CR8)、[`CONFIG_SOC_SERIES_RZV2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZV2L)、[`CONFIG_SOC_SERIES_RZV2N`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZV2N)、[`CONFIG_SOC_SERIES_B1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_B1)、[`CONFIG_SOC_EM32F967`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EM32F967)、[`CONFIG_SOC_SERIES_SAM3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAM3X)、[`CONFIG_SOC_SERIES_SAM4E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAM4E)、[`CONFIG_SOC_SERIES_SAM4L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAM4L)、[`CONFIG_SOC_SERIES_SAM4S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAM4S)、[`CONFIG_SOC_SERIES_SAMX7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMX7X)、[`CONFIG_SOC_SERIES_SMARTFUSION2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SMARTFUSION2)、[`CONFIG_SOC_SERIES_XMC4XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XMC4XXX)、[`CONFIG_SOC_AMD_VERSALNET_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSALNET_RPU)、[`CONFIG_SOC_SERIES_RTL8752H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTL8752H)、[`CONFIG_SOC_SERIES_RTL87X2G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTL87X2G)、[`CONFIG_SOC_FAMILY_MAX32_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_M33)、[`CONFIG_SOC_FAMILY_MAX32_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_M4)、[`CONFIG_SOC_RTS5817`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RTS5817)、[`CONFIG_SOC_SERIES_MSPM0G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSPM0G)、[`CONFIG_SOC_MSPM0L1117`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0L1117)、[`CONFIG_SOC_MSPM0L2227`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0L2227)、[`CONFIG_SOC_MSPM0L2228`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MSPM0L2228)、[`CONFIG_SOC_SERIES_MSPM33C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSPM33C)、[`CONFIG_SOC_AMD_VERSAL2_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSAL2_RPU)、[`CONFIG_SOC_SERIES_M48X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M48X)、[`CONFIG_SOC_SERIES_STM32C0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32C0X)、[`CONFIG_SOC_SERIES_STM32C5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32C5X)、[`CONFIG_SOC_SERIES_STM32F2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F2X)、[`CONFIG_SOC_SERIES_STM32F4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F4X)、[`CONFIG_SOC_SERIES_STM32F7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F7X)、[`CONFIG_SOC_SERIES_STM32G0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32G0X)、[`CONFIG_SOC_SERIES_STM32G4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32G4X)、[`CONFIG_SOC_SERIES_STM32H5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H5X)、[`CONFIG_SOC_SERIES_STM32H7RSX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7RSX)、[`CONFIG_SOC_SERIES_STM32H7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7X)、[`CONFIG_SOC_STM32L051XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32L051XX)、[`CONFIG_SOC_STM32L053XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32L053XX)、[`CONFIG_SOC_STM32L071XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32L071XX)、[`CONFIG_SOC_STM32L072XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32L072XX)、[`CONFIG_SOC_STM32L073XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32L073XX)、[`CONFIG_SOC_STM32L081XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32L081XX)、[`CONFIG_SOC_STM32L083XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32L083XX)、[`CONFIG_SOC_SERIES_STM32L1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L1X)、[`CONFIG_SOC_SERIES_STM32L4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L4X)、[`CONFIG_SOC_SERIES_STM32L5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L5X)、[`CONFIG_SOC_SERIES_STM32MP1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32MP1X)、[`CONFIG_SOC_STM32MP2X_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32MP2X_M33)、[`CONFIG_SOC_SERIES_STM32N6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32N6X)、[`CONFIG_SOC_SERIES_STM32U0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U0X)、[`CONFIG_SOC_SERIES_STM32U3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U3X)、[`CONFIG_SOC_SERIES_STM32U5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U5X)、[`CONFIG_SOC_SERIES_STM32WB0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WB0X)、[`CONFIG_SOC_SERIES_STM32WBAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBAX)、[`CONFIG_SOC_SERIES_STM32WBX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBX)、[`CONFIG_SOC_SERIES_STM32WL3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WL3X)、[`CONFIG_SOC_SERIES_STM32WLX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WLX)、[`CONFIG_SOC_SERIES_BEETLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BEETLE)、[`CONFIG_SOC_FVP_AEMV8R_AARCH32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FVP_AEMV8R_AARCH32)、[`CONFIG_SOC_AN521`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AN521)、[`CONFIG_SOC_AN383`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AN383)、[`CONFIG_SOC_AN385`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AN385)、[`CONFIG_SOC_AN386`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AN386)、[`CONFIG_SOC_AN500`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AN500)、[`CONFIG_SOC_CORSTONE300`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE300)、[`CONFIG_SOC_CORSTONE310`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE310)、[`CONFIG_SOC_AN536`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AN536)、[`CONFIG_SOC_CORSTONE315`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE315)、[`CONFIG_SOC_CORSTONE320`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE320)、[`CONFIG_SOC_MUSCA_B1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MUSCA_B1)、[`CONFIG_SOC_MUSCA_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MUSCA_S1)、[`CONFIG_SOC_SERIES_NPCK3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCK3)、[`CONFIG_SOC_SERIES_NPCX4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCX4)、[`CONFIG_SOC_SERIES_NPCX7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCX7)、[`CONFIG_SOC_SERIES_NPCX9`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCX9)、[`CONFIG_SOC_SERIES_RW6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RW6XX)、[`CONFIG_SOC_SERIES_S32K3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K3)、[`CONFIG_SOC_SERIES_S32K5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K5)、[`CONFIG_SOC_SERIES_S32ZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32ZE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`、`CONFIG_SOC_AM13E23019`、`CONFIG_SOC_LPC54114_M4`、`CONFIG_SOC_LPC54628`、`CONFIG_SOC_LPC55S06`、`CONFIG_SOC_LPC55S16`、`CONFIG_SOC_LPC55S26`、`CONFIG_SOC_LPC55S28`、`CONFIG_SOC_LPC55S36`、`CONFIG_SOC_LPC55S69_CPU0`、`CONFIG_SOC_SR100`、`CONFIG_SOC_SERIES_RA2L1`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC`、`CONFIG_SOC_SERIES_MCXAXX6`、`CONFIG_SOC_SERIES_MCXAXX4`、`CONFIG_SOC_SERIES_MCXAXX7`、`CONFIG_SOC_SERIES_MCXE31X`、`CONFIG_SOC_MCXL255_CPU0`、`CONFIG_SOC_MCXL254_CPU0`、`CONFIG_SOC_MCXL253_CPU0`、`CONFIG_SOC_MCXN947_CPU0`、`CONFIG_SOC_MCXN547_CPU0`、`CONFIG_SOC_MCXN236`、`CONFIG_SOC_FAMILY_MCXW`、`CONFIG_SOC_SERIES_MCXW2XX`、`CONFIG_SOC_FAMILY_SILABS_SIWX91X`、`CONFIG_SOC_MIMXRT1011`、`CONFIG_SOC_MIMXRT1015`、`CONFIG_SOC_MIMXRT1021`、`CONFIG_SOC_MIMXRT1024`、`CONFIG_SOC_MIMXRT1041`、`CONFIG_SOC_MIMXRT1042`、`CONFIG_SOC_MIMXRT1051`、`CONFIG_SOC_MIMXRT1052`、`CONFIG_SOC_MIMXRT1062`、`CONFIG_SOC_MIMXRT1064`、`CONFIG_SOC_SERIES_IMXRT118X`、`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_SERIES_IMXRT266X_CM85`、`CONFIG_SOC_MIMXRT685S_CM33`、`CONFIG_SOC_MIMXRT798S_CM33_CPU0`、`CONFIG_SOC_MIMXRT798S_CM33_CPU1`、`CONFIG_SOC_MIMXRT758S_CM33_CPU0`、`CONFIG_SOC_MIMXRT758S_CM33_CPU1`、`CONFIG_SOC_MIMXRT735S_CM33_CPU0`、`CONFIG_SOC_MIMXRT735S_CM33_CPU1`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`、`CONFIG_SOC_SERIES_KV5X`、`CONFIG_SOC_SERIES_SF32LB52X`、`CONFIG_SOC_NRF54H20_CPUAPP_COMMON`、`CONFIG_SOC_NRF54H20_CPURAD_COMMON`、`CONFIG_SOC_NRF9230_ENGB_CPUAPP`、`CONFIG_SOC_NRF9230_ENGB_CPURAD`、`CONFIG_SOC_SERIES_TM4C123X`、`CONFIG_SOC_SERIES_AMEBAD`、`CONFIG_SOC_SERIES_AMEBADPLUS`、`CONFIG_SOC_SERIES_AMEBAG2`、`CONFIG_SOC_FAMILY_PSOC6`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_SERIES_IMX6SX`、`CONFIG_SOC_SERIES_PSE84`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG`、`CONFIG_SOC_CYT4DNJBZS_M0P`、`CONFIG_SOC_CYT4DNJBZS_M7_0`、`CONFIG_SOC_CYT4DNJBZS_M7_1`、`CONFIG_SOC_SERIES_XMC7200`、`CONFIG_SOC_SERIES_CYW20829`、`CONFIG_SOC_SERIES_PSC3`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`、`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`、`CONFIG_SOC_FAMILY_ENSEMBLE_RTSS`、`CONFIG_SOC_SERIES_B1`、`CONFIG_SOC_FAMILY_MAX32_M33`、`CONFIG_SOC_FAMILY_MAX32_M4`、`CONFIG_SOC_RTS5817`、`CONFIG_SOC_MSPM0L1117`、`CONFIG_SOC_MSPM0L2227`、`CONFIG_SOC_MSPM0L2228`、`CONFIG_SOC_SERIES_STM32C0X`、`CONFIG_SOC_SERIES_STM32C5X`、`CONFIG_SOC_SERIES_STM32F2X`、`CONFIG_SOC_SERIES_STM32F4X`、`CONFIG_SOC_SERIES_STM32F7X`、`CONFIG_SOC_SERIES_STM32G0X`、`CONFIG_SOC_SERIES_STM32G4X`、`CONFIG_SOC_SERIES_STM32H5X`、`CONFIG_SOC_SERIES_STM32H7RSX`、`CONFIG_SOC_SERIES_STM32H7X`、`CONFIG_SOC_STM32L051XX`、`CONFIG_SOC_STM32L053XX`、`CONFIG_SOC_STM32L071XX`、`CONFIG_SOC_STM32L072XX`、`CONFIG_SOC_STM32L073XX`、`CONFIG_SOC_STM32L081XX`、`CONFIG_SOC_STM32L083XX`、`CONFIG_SOC_SERIES_STM32L1X`、`CONFIG_SOC_SERIES_STM32L4X`、`CONFIG_SOC_SERIES_STM32L5X`、`CONFIG_SOC_SERIES_STM32MP1X`、`CONFIG_SOC_STM32MP2X_M33`、`CONFIG_SOC_SERIES_STM32N6X`、`CONFIG_SOC_SERIES_STM32U0X`、`CONFIG_SOC_SERIES_STM32U3X`、`CONFIG_SOC_SERIES_STM32U5X`、`CONFIG_SOC_SERIES_STM32WB0X`、`CONFIG_SOC_SERIES_STM32WBAX`、`CONFIG_SOC_SERIES_STM32WBX`、`CONFIG_SOC_SERIES_STM32WL3X`、`CONFIG_SOC_SERIES_STM32WLX`、`CONFIG_SOC_FVP_AEMV8R_AARCH32`、`CONFIG_SOC_AN521`、`CONFIG_SOC_CORSTONE300`、`CONFIG_SOC_CORSTONE310`、`CONFIG_SOC_AN536`、`CONFIG_SOC_CORSTONE315`、`CONFIG_SOC_CORSTONE320`、`CONFIG_SOC_SERIES_RW6XX`、`CONFIG_SOC_SERIES_S32K3`、`CONFIG_SOC_SERIES_S32K5`、`CONFIG_SOC_SERIES_S32ZE`。

<a id="CONFIG_CPU_HAS_ARM_SAU"></a>

## 30.17 `CONFIG_CPU_HAS_ARM_SAU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

MCU 实现 ARM 安全属性单元（Security Attribution Unit，SAU）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_HAS_TEE
```

**被选择（Selected by）**

```text
CONFIG_SOC_LPC55S06
CONFIG_SOC_LPC55S16
CONFIG_SOC_LPC55S26
CONFIG_SOC_LPC55S28
CONFIG_SOC_LPC55S36
CONFIG_SOC_LPC55S69_CPU0
CONFIG_SOC_SR100
CONFIG_SOC_RP2350A_M33_0
CONFIG_SOC_RP2350B_M33_0
CONFIG_SOC_SERIES_RA8D1
CONFIG_SOC_SERIES_RA8D2
CONFIG_SOC_SERIES_RA8E1
CONFIG_SOC_SERIES_RA8M1
CONFIG_SOC_SERIES_RA8M2
CONFIG_SOC_SERIES_RA8P1
CONFIG_SOC_SERIES_RA8T1
CONFIG_SOC_SERIES_RA8T2
CONFIG_SOC_SERIES_MCXAXX7
CONFIG_SOC_MCXL255_CPU0
CONFIG_SOC_MCXL254_CPU0
CONFIG_SOC_MCXL253_CPU0
CONFIG_SOC_MCXN947_CPU0
CONFIG_SOC_MCXN547_CPU0
CONFIG_SOC_MCXN236
CONFIG_SOC_FAMILY_MCXW
CONFIG_SOC_SERIES_MCXW2XX
CONFIG_SOC_FAMILY_SILABS_S2_XG21
CONFIG_SOC_FAMILY_SILABS_S2_XG22
CONFIG_SOC_FAMILY_SILABS_S2_XG23
CONFIG_SOC_FAMILY_SILABS_S2_XG24
CONFIG_SOC_FAMILY_SILABS_S2_XG26
CONFIG_SOC_FAMILY_SILABS_S2_XG27
CONFIG_SOC_FAMILY_SILABS_S2_XG28
CONFIG_SOC_FAMILY_SILABS_S2_XG29
CONFIG_SOC_FAMILY_SILABS_S3_SIX301
CONFIG_SOC_SERIES_IMXRT118X
CONFIG_SOC_SERIES_IMXRT266X_CM85
CONFIG_SOC_MIMXRT595S_CM33
CONFIG_SOC_MIMXRT685S_CM33
CONFIG_SOC_MIMXRT798S_CM33_CPU0
CONFIG_SOC_MIMXRT798S_CM33_CPU1
CONFIG_SOC_MIMXRT758S_CM33_CPU0
CONFIG_SOC_MIMXRT758S_CM33_CPU1
CONFIG_SOC_MIMXRT735S_CM33_CPU0
CONFIG_SOC_MIMXRT735S_CM33_CPU1
CONFIG_SOC_NRF54H20_CPUAPP_COMMON
CONFIG_SOC_NRF54H20_CPURAD_COMMON
CONFIG_SOC_NRF54L05_CPUAPP
CONFIG_SOC_NRF54L10_CPUAPP
CONFIG_SOC_NRF54L15_CPUAPP
CONFIG_SOC_NRF54LM20A_CPUAPP
CONFIG_SOC_NRF54LM20B_CPUAPP
CONFIG_SOC_NRF54LV10A_CPUAPP
CONFIG_SOC_NRF7120_ENGA_CPUAPP
CONFIG_SOC_NRF7120E_ENGA_CPUAPP
CONFIG_SOC_NRF9230_ENGB_CPUAPP
CONFIG_SOC_NRF9230_ENGB_CPURAD
CONFIG_SOC_SERIES_AMEBAD
CONFIG_SOC_SERIES_AMEBADPLUS
CONFIG_SOC_SERIES_AMEBAG2
CONFIG_SOC_MIMX9352_M33
CONFIG_SOC_MIMX94398_M33
CONFIG_SOC_SERIES_PSE84_M33
CONFIG_SOC_SERIES_PSC3
CONFIG_SOC_SERIES_APOLLO5X
CONFIG_SOC_SERIES_RTL87X2G
CONFIG_SOC_FAMILY_MAX32_M33
CONFIG_SOC_SERIES_STM32H5X
CONFIG_SOC_SERIES_STM32L5X
CONFIG_SOC_STM32MP2X_M33
CONFIG_SOC_SERIES_STM32N6X
CONFIG_SOC_SERIES_STM32U3X
CONFIG_SOC_SERIES_STM32U5X
CONFIG_SOC_SERIES_STM32WBAX
CONFIG_SOC_AN521_CPU0
CONFIG_SOC_CORSTONE300
CONFIG_SOC_CORSTONE310
CONFIG_SOC_CORSTONE315
CONFIG_SOC_CORSTONE320
CONFIG_SOC_MUSCA_B1
CONFIG_SOC_MUSCA_S1
CONFIG_SOC_SERIES_RW6XX
```

**定义位置（Location）**：[`arch/arm/Kconfig:179`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/Kconfig#L179)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_HAS_TEE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_TEE)、[`CONFIG_SOC_LPC55S06`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S06)、[`CONFIG_SOC_LPC55S16`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S16)、[`CONFIG_SOC_LPC55S26`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S26)、[`CONFIG_SOC_LPC55S28`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S28)、[`CONFIG_SOC_LPC55S36`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S36)、[`CONFIG_SOC_LPC55S69_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S69_CPU0)、[`CONFIG_SOC_SR100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SR100)、[`CONFIG_SOC_RP2350A_M33_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350A_M33_0)、[`CONFIG_SOC_RP2350B_M33_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350B_M33_0)、[`CONFIG_SOC_SERIES_RA8D1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8D1)、[`CONFIG_SOC_SERIES_RA8D2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8D2)、[`CONFIG_SOC_SERIES_RA8E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8E1)、[`CONFIG_SOC_SERIES_RA8M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8M1)、[`CONFIG_SOC_SERIES_RA8M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8M2)、[`CONFIG_SOC_SERIES_RA8P1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8P1)、[`CONFIG_SOC_SERIES_RA8T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8T1)、[`CONFIG_SOC_SERIES_RA8T2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8T2)、[`CONFIG_SOC_SERIES_MCXAXX7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXAXX7)、[`CONFIG_SOC_MCXL255_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL255_CPU0)、[`CONFIG_SOC_MCXL254_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL254_CPU0)、[`CONFIG_SOC_MCXL253_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL253_CPU0)、[`CONFIG_SOC_MCXN947_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN947_CPU0)、[`CONFIG_SOC_MCXN547_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN547_CPU0)、[`CONFIG_SOC_MCXN236`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN236)、[`CONFIG_SOC_FAMILY_MCXW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXW)、[`CONFIG_SOC_SERIES_MCXW2XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXW2XX)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG21)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG22`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG22)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG23`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG23)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG24`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG24)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG26`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG26)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG27`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG27)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG28`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG28)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG29`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG29)、[`CONFIG_SOC_FAMILY_SILABS_S3_SIX301`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S3_SIX301)、[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_SOC_SERIES_IMXRT266X_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT266X_CM85)、[`CONFIG_SOC_MIMXRT595S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT595S_CM33)、[`CONFIG_SOC_MIMXRT685S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_CM33)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU1)、[`CONFIG_SOC_MIMXRT758S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT758S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_CM33_CPU1)、[`CONFIG_SOC_MIMXRT735S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT735S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_CM33_CPU1)、[`CONFIG_SOC_NRF54H20_CPUAPP_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPUAPP_COMMON)、[`CONFIG_SOC_NRF54H20_CPURAD_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPURAD_COMMON)、[`CONFIG_SOC_NRF54L05_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54L05_CPUAPP)、[`CONFIG_SOC_NRF54L10_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54L10_CPUAPP)、[`CONFIG_SOC_NRF54L15_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54L15_CPUAPP)、[`CONFIG_SOC_NRF54LM20A_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54LM20A_CPUAPP)、[`CONFIG_SOC_NRF54LM20B_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54LM20B_CPUAPP)、[`CONFIG_SOC_NRF54LV10A_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54LV10A_CPUAPP)、[`CONFIG_SOC_NRF7120_ENGA_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF7120_ENGA_CPUAPP)、[`CONFIG_SOC_NRF7120E_ENGA_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF7120E_ENGA_CPUAPP)、[`CONFIG_SOC_NRF9230_ENGB_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9230_ENGB_CPUAPP)、[`CONFIG_SOC_NRF9230_ENGB_CPURAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9230_ENGB_CPURAD)、[`CONFIG_SOC_SERIES_AMEBAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAD)、[`CONFIG_SOC_SERIES_AMEBADPLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBADPLUS)、[`CONFIG_SOC_SERIES_AMEBAG2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAG2)、[`CONFIG_SOC_MIMX9352_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9352_M33)、[`CONFIG_SOC_MIMX94398_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M33)、[`CONFIG_SOC_SERIES_PSE84_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSE84_M33)、[`CONFIG_SOC_SERIES_PSC3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSC3)、[`CONFIG_SOC_SERIES_APOLLO5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO5X)、[`CONFIG_SOC_SERIES_RTL87X2G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTL87X2G)、[`CONFIG_SOC_FAMILY_MAX32_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_M33)、[`CONFIG_SOC_SERIES_STM32H5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H5X)、[`CONFIG_SOC_SERIES_STM32L5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L5X)、[`CONFIG_SOC_STM32MP2X_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32MP2X_M33)、[`CONFIG_SOC_SERIES_STM32N6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32N6X)、[`CONFIG_SOC_SERIES_STM32U3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U3X)、[`CONFIG_SOC_SERIES_STM32U5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U5X)、[`CONFIG_SOC_SERIES_STM32WBAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBAX)、[`CONFIG_SOC_AN521_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AN521_CPU0)、[`CONFIG_SOC_CORSTONE300`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE300)、[`CONFIG_SOC_CORSTONE310`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE310)、[`CONFIG_SOC_CORSTONE315`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE315)、[`CONFIG_SOC_CORSTONE320`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE320)、[`CONFIG_SOC_MUSCA_B1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MUSCA_B1)、[`CONFIG_SOC_MUSCA_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MUSCA_S1)、[`CONFIG_SOC_SERIES_RW6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RW6XX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_LPC55S06`、`CONFIG_SOC_LPC55S16`、`CONFIG_SOC_LPC55S26`、`CONFIG_SOC_LPC55S28`、`CONFIG_SOC_LPC55S36`、`CONFIG_SOC_LPC55S69_CPU0`、`CONFIG_SOC_SR100`、`CONFIG_SOC_SERIES_MCXAXX7`、`CONFIG_SOC_MCXL255_CPU0`、`CONFIG_SOC_MCXL254_CPU0`、`CONFIG_SOC_MCXL253_CPU0`、`CONFIG_SOC_MCXN947_CPU0`、`CONFIG_SOC_MCXN547_CPU0`、`CONFIG_SOC_MCXN236`、`CONFIG_SOC_FAMILY_MCXW`、`CONFIG_SOC_SERIES_MCXW2XX`、`CONFIG_SOC_SERIES_IMXRT118X`、`CONFIG_SOC_SERIES_IMXRT266X_CM85`、`CONFIG_SOC_MIMXRT685S_CM33`、`CONFIG_SOC_MIMXRT798S_CM33_CPU0`、`CONFIG_SOC_MIMXRT798S_CM33_CPU1`、`CONFIG_SOC_MIMXRT758S_CM33_CPU0`、`CONFIG_SOC_MIMXRT758S_CM33_CPU1`、`CONFIG_SOC_MIMXRT735S_CM33_CPU0`、`CONFIG_SOC_MIMXRT735S_CM33_CPU1`、`CONFIG_SOC_NRF54H20_CPUAPP_COMMON`、`CONFIG_SOC_NRF54H20_CPURAD_COMMON`、`CONFIG_SOC_NRF9230_ENGB_CPUAPP`、`CONFIG_SOC_NRF9230_ENGB_CPURAD`、`CONFIG_SOC_SERIES_AMEBAD`、`CONFIG_SOC_SERIES_AMEBADPLUS`、`CONFIG_SOC_SERIES_AMEBAG2`、`CONFIG_SOC_SERIES_PSE84_M33`、`CONFIG_SOC_SERIES_PSC3`、`CONFIG_SOC_FAMILY_MAX32_M33`、`CONFIG_SOC_SERIES_STM32H5X`、`CONFIG_SOC_SERIES_STM32L5X`、`CONFIG_SOC_STM32MP2X_M33`、`CONFIG_SOC_SERIES_STM32N6X`、`CONFIG_SOC_SERIES_STM32U3X`、`CONFIG_SOC_SERIES_STM32U5X`、`CONFIG_SOC_SERIES_STM32WBAX`、`CONFIG_SOC_CORSTONE300`、`CONFIG_SOC_CORSTONE310`、`CONFIG_SOC_CORSTONE315`、`CONFIG_SOC_CORSTONE320`、`CONFIG_SOC_SERIES_RW6XX`。

<a id="CONFIG_CPU_HAS_CUSTOM_FIXED_SOC_MPU_REGIONS"></a>

## 30.18 `CONFIG_CPU_HAS_CUSTOM_FIXED_SOC_MPU_REGIONS`

**提示（Prompt）**：自定义 SoC 固定 MPU 区域定义（Fixed MPU Region Definition）

**说明（Help）**

启用后，表示 SoC 会在其定义中自行定义并配置固定 MPU 区域（Fixed MPU Regions）。这些区域目前用于设置 Flash 和 SRAM 的默认访问策略，在启动时编程。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_IMXRT10XX
CONFIG_SOC_SERIES_IMXRT118X
CONFIG_SOC_SERIES_IMXRT11XX
CONFIG_SOC_SERIES_M55M1X
CONFIG_SOC_NRF54H20_CPUAPP_COMMON
CONFIG_SOC_NRF54H20_CPURAD_COMMON
CONFIG_SOC_NRF9230_ENGB_CPUAPP
CONFIG_SOC_NRF9230_ENGB_CPURAD
CONFIG_SOC_MIMX8ML8_M7
CONFIG_SOC_SERIES_PSE84
CONFIG_SOC_SERIES_CYW20829
CONFIG_SOC_FAMILY_MAX32_M33
CONFIG_SOC_SERIES_STM32H7RSX
CONFIG_SOC_SERIES_STM32H7X
CONFIG_SOC_SERIES_STM32N6X
CONFIG_SOC_SERIES_NPCX4
CONFIG_SOC_SERIES_NPCX7
CONFIG_SOC_SERIES_S32K1
CONFIG_SOC_SERIES_S32K3
CONFIG_SOC_S32K566_M7
```

**定义位置（Location）**：[`arch/arm/Kconfig:170`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/Kconfig#L170)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_SOC_SERIES_IMXRT10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT10XX)、[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_SERIES_M55M1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M55M1X)、[`CONFIG_SOC_NRF54H20_CPUAPP_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPUAPP_COMMON)、[`CONFIG_SOC_NRF54H20_CPURAD_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPURAD_COMMON)、[`CONFIG_SOC_NRF9230_ENGB_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9230_ENGB_CPUAPP)、[`CONFIG_SOC_NRF9230_ENGB_CPURAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9230_ENGB_CPURAD)、[`CONFIG_SOC_MIMX8ML8_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8ML8_M7)、[`CONFIG_SOC_SERIES_PSE84`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSE84)、[`CONFIG_SOC_SERIES_CYW20829`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CYW20829)、[`CONFIG_SOC_FAMILY_MAX32_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_M33)、[`CONFIG_SOC_SERIES_STM32H7RSX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7RSX)、[`CONFIG_SOC_SERIES_STM32H7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7X)、[`CONFIG_SOC_SERIES_STM32N6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32N6X)、[`CONFIG_SOC_SERIES_NPCX4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCX4)、[`CONFIG_SOC_SERIES_NPCX7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCX7)、[`CONFIG_SOC_SERIES_S32K1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K1)、[`CONFIG_SOC_SERIES_S32K3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K3)、[`CONFIG_SOC_S32K566_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K566_M7)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT10XX`、`CONFIG_SOC_SERIES_IMXRT118X`、`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_NRF54H20_CPUAPP_COMMON`、`CONFIG_SOC_NRF54H20_CPURAD_COMMON`、`CONFIG_SOC_NRF9230_ENGB_CPUAPP`、`CONFIG_SOC_NRF9230_ENGB_CPURAD`、`CONFIG_SOC_SERIES_PSE84`、`CONFIG_SOC_SERIES_CYW20829`、`CONFIG_SOC_FAMILY_MAX32_M33`、`CONFIG_SOC_SERIES_STM32H7RSX`、`CONFIG_SOC_SERIES_STM32H7X`、`CONFIG_SOC_SERIES_STM32N6X`、`CONFIG_SOC_SERIES_S32K1`、`CONFIG_SOC_SERIES_S32K3`、`CONFIG_SOC_S32K566_M7`。

<a id="CONFIG_CPU_HAS_NEON"></a>

## 30.19 `CONFIG_CPU_HAS_NEON`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示支持 NEON 高级单指令多数据（Advanced SIMD）协处理器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_HAS_FPU
```

**被选择（Selected by）**

```text
CONFIG_NEON
```

**定义位置（Location）**：[`arch/arm/core/Kconfig.vfp:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig.vfp#L19)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_HAS_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU)、[`CONFIG_NEON`](P030_arch_arm_配置项参考_2.md#CONFIG_NEON)。

<a id="CONFIG_CPU_HAS_NRF_IDAU"></a>

## 30.20 `CONFIG_CPU_HAS_NRF_IDAU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

MCU 实现 nRF 厂商专用的安全属性单元（Security Attribution Unit）。按 ARM 术语，该单元称为实现定义属性单元（Implementation-Defined Attribution Unit，IDAU）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_HAS_TEE
```

**被选择（Selected by）**

```text
CONFIG_SOC_NRF5340_CPUAPP
CONFIG_SOC_SERIES_NRF91
```

**定义位置（Location）**：[`arch/arm/Kconfig:185`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/Kconfig#L185)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_HAS_TEE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_TEE)、[`CONFIG_SOC_NRF5340_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF5340_CPUAPP)、[`CONFIG_SOC_SERIES_NRF91`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF91)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_NRF5340_CPUAPP`。

<a id="CONFIG_CPU_HAS_NXP_SYSMPU"></a>

## 30.21 `CONFIG_CPU_HAS_NXP_SYSMPU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CPU 具有 NXP 系统内存保护单元（System Memory Protection Unit，SYSMPU）时，启用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_HAS_MPU
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_MCXE24X
CONFIG_SOC_MK22F12
CONFIG_SOC_SERIES_K6X
CONFIG_SOC_SERIES_K8X
CONFIG_SOC_SERIES_KE1XF
CONFIG_SOC_SERIES_S32K1
```

**定义位置（Location）**：[`arch/arm/Kconfig:163`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/Kconfig#L163)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_HAS_MPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MPU)、[`CONFIG_SOC_SERIES_MCXE24X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE24X)、[`CONFIG_SOC_MK22F12`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MK22F12)、[`CONFIG_SOC_SERIES_K6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K6X)、[`CONFIG_SOC_SERIES_K8X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K8X)、[`CONFIG_SOC_SERIES_KE1XF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KE1XF)、[`CONFIG_SOC_SERIES_S32K1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_MCXE24X`、`CONFIG_SOC_MK22F12`、`CONFIG_SOC_SERIES_K6X`、`CONFIG_SOC_SERIES_K8X`、`CONFIG_SOC_SERIES_KE1XF`、`CONFIG_SOC_SERIES_S32K1`。

<a id="CONFIG_CPU_HAS_VFP"></a>

## 30.22 `CONFIG_CPU_HAS_VFP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示支持向量浮点（Vectored Floating-Point，VFP）协处理器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_HAS_FPU
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_AMEBAD
CONFIG_SOC_SERIES_AMEBADPLUS
CONFIG_SOC_AN386
CONFIG_VFP_SP_D16
CONFIG_VFP_SP_D16_FP16
CONFIG_VFP_SP_D16_FP16_FMAC
CONFIG_VFP_DP_D16
CONFIG_VFP_DP_D16_FP16
CONFIG_VFP_DP_D16_FP16_FMAC
CONFIG_VFP_U_DP_D16_FP16_FMAC
CONFIG_VFP_DP_D32
CONFIG_VFP_DP_D32_FP16_FMAC
CONFIG_VFP_U_DP_D32_FP16_FMAC
```

**弱选择（Implies）**

```text
CONFIG_FPU
CONFIG_FPU_SHARING
```

**定义位置（Location）**：[`arch/arm/core/Kconfig.vfp:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig.vfp#L10)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_HAS_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU)、[`CONFIG_SOC_SERIES_AMEBAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAD)、[`CONFIG_SOC_SERIES_AMEBADPLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBADPLUS)、[`CONFIG_SOC_AN386`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AN386)、[`CONFIG_VFP_SP_D16`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_SP_D16)、[`CONFIG_VFP_SP_D16_FP16`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_SP_D16_FP16)、[`CONFIG_VFP_SP_D16_FP16_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_SP_D16_FP16_FMAC)、[`CONFIG_VFP_DP_D16`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_DP_D16)、[`CONFIG_VFP_DP_D16_FP16`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_DP_D16_FP16)、[`CONFIG_VFP_DP_D16_FP16_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_DP_D16_FP16_FMAC)、[`CONFIG_VFP_U_DP_D16_FP16_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_U_DP_D16_FP16_FMAC)、[`CONFIG_VFP_DP_D32`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_DP_D32)、[`CONFIG_VFP_DP_D32_FP16_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_DP_D32_FP16_FMAC)、[`CONFIG_VFP_U_DP_D32_FP16_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_U_DP_D32_FP16_FMAC)、[`CONFIG_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU)、[`CONFIG_FPU_SHARING`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU_SHARING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_AMEBAD`、`CONFIG_SOC_SERIES_AMEBADPLUS`。

<a id="CONFIG_CUSTOM_SECTION_ALIGN"></a>

## 30.23 `CONFIG_CUSTOM_SECTION_ALIGN`

**提示（Prompt）**：自定义段对齐（Custom Section Align）

**说明（Help）**

`MPU_REQUIRES_POWER_OF_TWO_ALIGNMENT` 在 ARMv7-M 上有时会使链接脚本定义的内存段浪费空间。使用此符号保证用户自定义段的对齐大小，避免为满足对齐要求使用更多内存。但必须仔细配置 MPU 区域和 ARMv7-M 子区域（Sub-region），才能覆盖此功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_MPU && CONFIG_CPU_HAS_MPU && CONFIG_ARM
```

**定义位置（Location）**：[`arch/arm/core/mpu/Kconfig:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/mpu/Kconfig#L77)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MPU)、[`CONFIG_CPU_HAS_MPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MPU)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_CUSTOM_SECTION_MIN_ALIGN_SIZE"></a>

## 30.24 `CONFIG_CUSTOM_SECTION_MIN_ALIGN_SIZE`

**提示（Prompt）**：自定义段对齐大小（Custom Section Align Size）

**说明（Help）**

链接脚本中内存段（Memory Section）的自定义对齐大小，通常应减少对齐所消耗的内存。即使由用户配置，若硬件要求对齐为 2 的幂，仍必须遵守。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_MPU && CONFIG_CPU_HAS_MPU && CONFIG_ARM
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`arch/arm/core/mpu/Kconfig:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/mpu/Kconfig#L86)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MPU)、[`CONFIG_CPU_HAS_MPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MPU)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_DISABLE_TCM_ECC"></a>

## 30.25 `CONFIG_DISABLE_TCM_ECC`

**提示（Prompt）**：禁用 TCM 错误校正码（ECC）

**说明（Help）**

此选项禁用紧耦合存储器（Tightly Coupled Memory，TCM）的错误校正码（ECC）检查。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_AARCH32_CORTEX_R && CONFIG_ARM
```

**定义位置（Location）**：[`arch/arm/core/cortex_a_r/Kconfig:301`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_a_r/Kconfig#L301)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_AARCH32_CORTEX_R`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_R)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_DYNAMIC_DIRECT_INTERRUPTS"></a>

## 30.26 `CONFIG_DYNAMIC_DIRECT_INTERRUPTS`

**提示（Prompt）**：动态直接中断（Dynamic Direct Interrupts）支持

**说明（Help）**

直接中断（Direct Interrupt）为性能关键的中断处理而设计，不经过全部公共中断处理代码。此选项允许在运行时为直接中断安装中断服务例程（ISR）。注意：要求内核启用动态中断（Dynamic Interrupt）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DYNAMIC_INTERRUPTS && (CONFIG_ARMV6_M_ARMV8_M_BASELINE || CONFIG_ARMV7_M_ARMV8_M_MAINLINE) && CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:356`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L356)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options） → ARM Cortex-M0/M0+/M1/M3/M4/M7/M23/M33/M55 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_DYNAMIC_INTERRUPTS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DYNAMIC_INTERRUPTS)、[`CONFIG_ARMV6_M_ARMV8_M_BASELINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV6_M_ARMV8_M_BASELINE)、[`CONFIG_ARMV7_M_ARMV8_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_M_ARMV8_M_MAINLINE)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_FAULT_DUMP"></a>

## 30.27 `CONFIG_FAULT_DUMP`

**提示（Prompt）**：故障转储级别（Fault Dump Level）

**说明（Help）**

故障发生时显示信息的详细程度：

- `2`：默认级别，显示具体且详细的信息，使用长字符串，内存占用最多。
- `1`：显示一般、简短的信息，使用短字符串，内存占用较少。
- `0`：关闭。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[0, 2]
```

**定义位置（Location）**：[`arch/arm/core/Kconfig:219`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig#L219)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_FP16"></a>

## 30.28 `CONFIG_FP16`

**提示（Prompt）**：半精度浮点存储支持（Half-precision Floating Point Storage）

**说明（Help）**

此选项通过 `__fp16` 和 `_Float16` 类型启用半精度（16 位）浮点支持。`__fp16` 支持 IEEE 格式和 ARM 替代格式（Alternative Format），`_Float16` 由 ISO/IEC TS 18661-3:2015 定义。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`arch/arm/core/Kconfig:350`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig#L350)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_FP16_ALT"></a>

## 30.29 `CONFIG_FP16_ALT`

**提示（Prompt）**：FP16 ARM 替代格式（Alternative Format）

**说明（Help）**

此选项为 FP16 选择 ARM 替代格式（Alternative Format）。其表示方式类似 IEEE 754-2008，但不支持无穷大（Infinity）或非数（NaN），而是扩大指数范围，因此可以表示 `2^(-14)` 到 `131008` 的规格化值（Normalized Value）。注意，Clang 不支持 ARM 替代格式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`arch/arm/core/Kconfig:370`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig#L370)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options） → 半精度浮点存储支持（Half-precision Floating Point Storage） → FP16 格式（Format）

<a id="CONFIG_FP16_ARITHMETIC"></a>

## 30.30 `CONFIG_FP16_ARITHMETIC`

**提示（Prompt）**：半精度浮点算术支持（Half-precision Floating Point Arithmetic）

**说明（Help）**

此选项表示目标支持半精度（16 位）浮点算术（Floating-point Arithmetic）。要求硬件具有原生 f16 运算能力，例如支持 MVE 浮点的 Cortex-M 处理器，或具有 NEON 的 Cortex-A 处理器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FP16 && (CONFIG_ARMV8_1_M_MVEF || CONFIG_CPU_CORTEX_A) && CONFIG_ARM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`arch/arm/core/Kconfig:383`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig#L383)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options） → 半精度浮点存储支持（Half-precision Floating Point Storage）

**配置项引用（Symbol References）**：[`CONFIG_FP16`](P030_arch_arm_配置项参考_2.md#CONFIG_FP16)、[`CONFIG_ARMV8_1_M_MVEF`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_1_M_MVEF)、[`CONFIG_CPU_CORTEX_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_A)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_FP16_IEEE"></a>

## 30.31 `CONFIG_FP16_IEEE`

**提示（Prompt）**：FP16 IEEE 格式（Format）

**说明（Help）**

此选项为 FP16 选择 IEEE 754-2008 格式，可表示 `2^(-14)` 到 `65504` 的规格化值（Normalized Value）。有效数精度（Significand Precision）为 11 位，约相当于 3 位十进制数字。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`arch/arm/core/Kconfig:363`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig#L363)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options） → 半精度浮点存储支持（Half-precision Floating Point Storage） → FP16 格式（Format）

<a id="CONFIG_FP_HARDABI"></a>

## 30.32 `CONFIG_FP_HARDABI`

**提示（Prompt）**：硬浮点应用二进制接口（Floating Point Hard ABI）

**说明（Help）**

此选项选择生成硬件浮点指令，并采用 FPU 专用调用约定（Calling Conventions）的浮点应用二进制接口（ABI）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**主动选择（Selects）**

```text
CONFIG_FPU_SHARING
```

**定义位置（Location）**：[`arch/arm/core/Kconfig:333`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig#L333)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options） → 浮点应用二进制接口（Floating Point ABI）

**配置项引用（Symbol References）**：[`CONFIG_FPU_SHARING`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU_SHARING)。

<a id="CONFIG_FP_SOFTABI"></a>

## 30.33 `CONFIG_FP_SOFTABI`

**提示（Prompt）**：软浮点应用二进制接口（Floating Point Soft ABI）

**说明（Help）**

此选项选择生成硬件浮点指令，但采用软浮点调用约定（Soft-float Calling Conventions）的浮点应用二进制接口（ABI）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**主动选择（Selects）**

```text
CONFIG_FPU_SHARING
```

**定义位置（Location）**：[`arch/arm/core/Kconfig:341`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig#L341)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options） → 浮点应用二进制接口（Floating Point ABI）

**配置项引用（Symbol References）**：[`CONFIG_FPU_SHARING`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU_SHARING)。

<a id="CONFIG_HAS_SWO"></a>

## 30.34 `CONFIG_HAS_SWO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用后，表示 SoC 具有串行线输出（SWO）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_LPC55XXX
CONFIG_SOC_SERIES_MEC165XB
CONFIG_SOC_SERIES_MEC172X
CONFIG_SOC_SERIES_MEC174X
CONFIG_SOC_SERIES_MEC175X
CONFIG_SOC_SERIES_RA2A1
CONFIG_SOC_SERIES_RA2L1
CONFIG_SOC_SERIES_RA4C1
CONFIG_SOC_SERIES_RA4E1
CONFIG_SOC_SERIES_RA4E2
CONFIG_SOC_SERIES_RA4L1
CONFIG_SOC_SERIES_RA4M1
CONFIG_SOC_SERIES_RA4M2
CONFIG_SOC_SERIES_RA4M3
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
CONFIG_SOC_SERIES_EFM32GG11B
CONFIG_SOC_SERIES_EFM32GG12B
CONFIG_SOC_SERIES_EFM32JG12B
CONFIG_SOC_SERIES_EFM32PG12B
CONFIG_SOC_SERIES_EFM32PG1B
CONFIG_SOC_SERIES_EFR32BG13P
CONFIG_SOC_SERIES_EFR32FG13P
CONFIG_SOC_SERIES_EFR32FG1P
CONFIG_SOC_SERIES_EFR32MG12P
CONFIG_SOC_SERIES_EFR32MG13P
CONFIG_SOC_FAMILY_SILABS_S2_XG21
CONFIG_SOC_FAMILY_SILABS_S2_XG22
CONFIG_SOC_FAMILY_SILABS_S2_XG23
CONFIG_SOC_FAMILY_SILABS_S2_XG24
CONFIG_SOC_FAMILY_SILABS_S2_XG26
CONFIG_SOC_FAMILY_SILABS_S2_XG27
CONFIG_SOC_FAMILY_SILABS_S2_XG28
CONFIG_SOC_FAMILY_SILABS_S2_XG29
CONFIG_SOC_FAMILY_SILABS_S3_SIX301
CONFIG_SOC_FAMILY_SILABS_SIWX91X
CONFIG_SOC_SERIES_IMXRT10XX
CONFIG_SOC_MIMXRT1064
CONFIG_SOC_SERIES_IMXRT118X
CONFIG_SOC_SERIES_IMXRT11XX
CONFIG_SOC_SERIES_IMXRT266X_CM85
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA
CONFIG_SOC_SERIES_NRF52
CONFIG_SOC_SERIES_NRF53
CONFIG_SOC_NRF54L05_CPUAPP
CONFIG_SOC_NRF54L10_CPUAPP
CONFIG_SOC_NRF54L15_CPUAPP
CONFIG_SOC_NRF54LM20A_CPUAPP
CONFIG_SOC_NRF54LM20B_CPUAPP
CONFIG_SOC_NRF54LV10A_CPUAPP
CONFIG_SOC_NRF7120_ENGA_CPUAPP
CONFIG_SOC_NRF7120E_ENGA_CPUAPP
CONFIG_SOC_SERIES_APOLLO2X
CONFIG_SOC_SERIES_APOLLO3X
CONFIG_SOC_SERIES_APOLLO4X
CONFIG_SOC_SERIES_APOLLO5X
CONFIG_SOC_SERIES_SAMX7X
CONFIG_SOC_SERIES_STM32C5X
CONFIG_SOC_SERIES_STM32F1X
CONFIG_SOC_SERIES_STM32F2X
CONFIG_SOC_SERIES_STM32F3X
CONFIG_SOC_SERIES_STM32F4X
CONFIG_SOC_SERIES_STM32F7X
CONFIG_SOC_SERIES_STM32G4X
CONFIG_SOC_SERIES_STM32H5X
CONFIG_SOC_SERIES_STM32H7RSX
CONFIG_SOC_SERIES_STM32H7X
CONFIG_SOC_SERIES_STM32L1X
CONFIG_SOC_SERIES_STM32L4X
CONFIG_SOC_SERIES_STM32L5X
CONFIG_SOC_SERIES_STM32U5X
CONFIG_SOC_SERIES_STM32WBX
CONFIG_SOC_SERIES_NPCK3
```

**定义位置（Location）**：[`arch/arm/Kconfig:193`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/Kconfig#L193)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_SOC_SERIES_LPC55XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC55XXX)、[`CONFIG_SOC_SERIES_MEC165XB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC165XB)、[`CONFIG_SOC_SERIES_MEC172X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC172X)、[`CONFIG_SOC_SERIES_MEC174X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC174X)、[`CONFIG_SOC_SERIES_MEC175X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC175X)、[`CONFIG_SOC_SERIES_RA2A1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA2A1)、[`CONFIG_SOC_SERIES_RA2L1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA2L1)、[`CONFIG_SOC_SERIES_RA4C1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4C1)、[`CONFIG_SOC_SERIES_RA4E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4E1)、[`CONFIG_SOC_SERIES_RA4E2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4E2)、[`CONFIG_SOC_SERIES_RA4L1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4L1)、[`CONFIG_SOC_SERIES_RA4M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M1)、[`CONFIG_SOC_SERIES_RA4M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M2)、[`CONFIG_SOC_SERIES_RA4M3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M3)、[`CONFIG_SOC_SERIES_RA4W1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4W1)、[`CONFIG_SOC_SERIES_RA6E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6E1)、[`CONFIG_SOC_SERIES_RA6E2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6E2)、[`CONFIG_SOC_SERIES_RA6M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M1)、[`CONFIG_SOC_SERIES_RA6M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M2)、[`CONFIG_SOC_SERIES_RA6M3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M3)、[`CONFIG_SOC_SERIES_RA6M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M4)、[`CONFIG_SOC_SERIES_RA6M5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M5)、[`CONFIG_SOC_SERIES_RA8D1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8D1)、[`CONFIG_SOC_SERIES_RA8D2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8D2)、[`CONFIG_SOC_SERIES_RA8E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8E1)、[`CONFIG_SOC_SERIES_RA8M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8M1)、[`CONFIG_SOC_SERIES_RA8M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8M2)、[`CONFIG_SOC_SERIES_RA8P1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8P1)、[`CONFIG_SOC_SERIES_RA8T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8T1)、[`CONFIG_SOC_SERIES_RA8T2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8T2)、[`CONFIG_SOC_SERIES_EFM32GG11B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32GG11B)、[`CONFIG_SOC_SERIES_EFM32GG12B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32GG12B)、[`CONFIG_SOC_SERIES_EFM32JG12B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32JG12B)、[`CONFIG_SOC_SERIES_EFM32PG12B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32PG12B)、[`CONFIG_SOC_SERIES_EFM32PG1B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32PG1B)、[`CONFIG_SOC_SERIES_EFR32BG13P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32BG13P)、[`CONFIG_SOC_SERIES_EFR32FG13P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32FG13P)、[`CONFIG_SOC_SERIES_EFR32FG1P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32FG1P)、[`CONFIG_SOC_SERIES_EFR32MG12P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32MG12P)、[`CONFIG_SOC_SERIES_EFR32MG13P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32MG13P)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG21)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG22`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG22)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG23`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG23)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG24`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG24)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG26`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG26)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG27`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG27)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG28`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG28)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG29`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG29)、[`CONFIG_SOC_FAMILY_SILABS_S3_SIX301`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S3_SIX301)、[`CONFIG_SOC_FAMILY_SILABS_SIWX91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_SIWX91X)、[`CONFIG_SOC_SERIES_IMXRT10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT10XX)、[`CONFIG_SOC_MIMXRT1064`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1064)、[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_SERIES_IMXRT266X_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT266X_CM85)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA)、[`CONFIG_SOC_SERIES_NRF52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF52)、[`CONFIG_SOC_SERIES_NRF53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_NRF54L05_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54L05_CPUAPP)、[`CONFIG_SOC_NRF54L10_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54L10_CPUAPP)、[`CONFIG_SOC_NRF54L15_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54L15_CPUAPP)、[`CONFIG_SOC_NRF54LM20A_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54LM20A_CPUAPP)、[`CONFIG_SOC_NRF54LM20B_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54LM20B_CPUAPP)、[`CONFIG_SOC_NRF54LV10A_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54LV10A_CPUAPP)、[`CONFIG_SOC_NRF7120_ENGA_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF7120_ENGA_CPUAPP)、[`CONFIG_SOC_NRF7120E_ENGA_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF7120E_ENGA_CPUAPP)、[`CONFIG_SOC_SERIES_APOLLO2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO2X)、[`CONFIG_SOC_SERIES_APOLLO3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO3X)、[`CONFIG_SOC_SERIES_APOLLO4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO4X)、[`CONFIG_SOC_SERIES_APOLLO5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO5X)、[`CONFIG_SOC_SERIES_SAMX7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMX7X)、[`CONFIG_SOC_SERIES_STM32C5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32C5X)、[`CONFIG_SOC_SERIES_STM32F1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F1X)、[`CONFIG_SOC_SERIES_STM32F2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F2X)、[`CONFIG_SOC_SERIES_STM32F3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F3X)、[`CONFIG_SOC_SERIES_STM32F4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F4X)、[`CONFIG_SOC_SERIES_STM32F7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F7X)、[`CONFIG_SOC_SERIES_STM32G4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32G4X)、[`CONFIG_SOC_SERIES_STM32H5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H5X)、[`CONFIG_SOC_SERIES_STM32H7RSX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7RSX)、[`CONFIG_SOC_SERIES_STM32H7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7X)、[`CONFIG_SOC_SERIES_STM32L1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L1X)、[`CONFIG_SOC_SERIES_STM32L4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L4X)、[`CONFIG_SOC_SERIES_STM32L5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L5X)、[`CONFIG_SOC_SERIES_STM32U5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U5X)、[`CONFIG_SOC_SERIES_STM32WBX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBX)、[`CONFIG_SOC_SERIES_NPCK3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCK3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_LPC55XXX`、`CONFIG_SOC_SERIES_RA2L1`、`CONFIG_SOC_FAMILY_SILABS_SIWX91X`、`CONFIG_SOC_SERIES_IMXRT10XX`、`CONFIG_SOC_MIMXRT1064`、`CONFIG_SOC_SERIES_IMXRT118X`、`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_SERIES_IMXRT266X_CM85`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`、`CONFIG_SOC_SERIES_STM32C5X`、`CONFIG_SOC_SERIES_STM32F1X`、`CONFIG_SOC_SERIES_STM32F2X`、`CONFIG_SOC_SERIES_STM32F3X`、`CONFIG_SOC_SERIES_STM32F4X`、`CONFIG_SOC_SERIES_STM32F7X`、`CONFIG_SOC_SERIES_STM32G4X`、`CONFIG_SOC_SERIES_STM32H5X`、`CONFIG_SOC_SERIES_STM32H7RSX`、`CONFIG_SOC_SERIES_STM32H7X`、`CONFIG_SOC_SERIES_STM32L1X`、`CONFIG_SOC_SERIES_STM32L4X`、`CONFIG_SOC_SERIES_STM32L5X`、`CONFIG_SOC_SERIES_STM32U5X`、`CONFIG_SOC_SERIES_STM32WBX`。

<a id="CONFIG_ISA_ARM"></a>

## 30.35 `CONFIG_ISA_ARM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

来源：[Arm A32 与 T32 指令集说明](https://developer.arm.com/products/architecture/instruction-sets/a32-and-t32-instruction-sets)。A32 指令在 Armv8 之前的架构中称为 Arm 指令，宽度为 32 位，按 4 字节边界对齐。A-profile 和 R-profile 架构均支持 A32。传统上，A32 用于要求最高性能的应用，或用于处理中断、处理器启动等硬件异常。引入 Thumb-2 技术后，其大部分功能已纳入 T32。

译注：此 ARM 外部引用未取得可核验的正文，访问结果为受限响应、空的应用外壳或其他支持入口。保留官方 Kconfig 原始地址，不将外部正文记为已验证；本条译文依据已保存的 Zephyr 官方配置数据库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_ARMV7_A
CONFIG_AARCH32_ARMV8_A
CONFIG_ARMV7_R
```

**定义位置（Location）**：[`arch/arm/core/Kconfig:135`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig#L135)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ARMV7_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARMV7_A)、[`CONFIG_AARCH32_ARMV8_A`](P029_arch_arm_配置项参考_1.md#CONFIG_AARCH32_ARMV8_A)、[`CONFIG_ARMV7_R`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_R)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARMV7_A`。

<a id="CONFIG_ISA_THUMB2"></a>

## 30.36 `CONFIG_ISA_THUMB2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

来源：[Arm 指令集架构说明](http://www.arm.com/products/processors/technologies/instruction-set-architectures.php)。Thumb-2 技术是 ARM Cortex 架构所基于的指令集，为各种嵌入式应用提升性能、能效（Energy Efficiency）和代码密度（Code Density）。它建立在 Thumb 这种面向 ARM 微处理器内核的创新高代码密度指令集之上，为开发低成本、高性能系统的开发者提供更强能力。

此技术向后兼容已有 ARM 和 Thumb 方案，同时显著扩展 Thumb 指令集的功能，使更多应用代码能够受益于 Thumb 的高代码密度。原文称，对于经过性能优化的代码，Thumb-2 使用的内存减少 31%，可降低系统成本；相较已有高密度代码，性能最多提高 38%，可用于延长电池寿命或丰富产品功能。原文最后说明，该技术应用于所述处理器以及所有基于 ARMv7 架构的处理器。

译注：原文最后一句未明确“该处理器（the processor）”所指对象；上述百分比为原文引用的比较数据，未补充原文未提供的测试条件。

译注：此 ARM 外部引用未取得可核验的正文，访问结果为受限响应、空的应用外壳或其他支持入口。保留官方 Kconfig 原始地址，不将外部正文记为已验证；本条译文依据已保存的 Zephyr 官方配置数据库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_ARMV6_M_ARMV8_M_BASELINE
CONFIG_ARMV7_M_ARMV8_M_MAINLINE
CONFIG_ARMV7_R
```

**定义位置（Location）**：[`arch/arm/core/Kconfig:108`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig#L108)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ARMV6_M_ARMV8_M_BASELINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV6_M_ARMV8_M_BASELINE)、[`CONFIG_ARMV7_M_ARMV8_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_M_ARMV8_M_MAINLINE)、[`CONFIG_ARMV7_R`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_R)。

<a id="CONFIG_MPU_ALLOW_FLASH_WRITE"></a>

## 30.37 `CONFIG_MPU_ALLOW_FLASH_WRITE`

原库同名定义共 2 条；本项为数据库第 12268 条记录，各定义分别保留。

**提示（Prompt）**：为 Flash 增加 MPU 写访问权限（Write Access）

**说明（Help）**

启用后，允许 MPU 对 Flash 内存进行读／写／执行（RWX）访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_MPU && CONFIG_CPU_HAS_MPU && CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_S32K1
CONFIG_FLASH_SHELL
CONFIG_SOC_FLASH_CC13XX_CC26XX
CONFIG_SOC_FLASH_CC23X0
CONFIG_SOC_FLASH_GD32
CONFIG_SOC_FLASH_GECKO
CONFIG_FLASH_MSPI_INFINEON_S28HX512T
CONFIG_FLASH_MCHP_NVMCTRL_G1
CONFIG_FLASH_MCHP_NVMCTRL_G2
CONFIG_FLASH_MCHP_NVMCTRL_G3
CONFIG_SOC_FLASH_MCUX
CONFIG_SOC_FLASH_NRF
CONFIG_SOC_FLASH_NRF_RRAM
CONFIG_SOC_FLASH_RENESAS_RA_MRAM
CONFIG_SOC_FLASH_SAM
CONFIG_SOC_FLASH_SAM0
CONFIG_SOC_FLASH_SILABS_S2
CONFIG_SOC_FLASH_SMARTBOND
CONFIG_SOC_FLASH_STM32
CONFIG_BT_SETTINGS
CONFIG_MCUMGR_GRP_IMG
CONFIG_HAWKBIT
CONFIG_UPDATEHUB
CONFIG_USB_DFU_CLASS
```

**被弱选择（Implied by）**

```text
CONFIG_OPENTHREAD
CONFIG_OPENTHREAD
CONFIG_SOC_FLASH_NRF_MRAM
CONFIG_SOC_FLASH_NRF_MRAMC
```

**定义位置（Location）**：[`arch/arm/core/mpu/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/mpu/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MPU)、[`CONFIG_CPU_HAS_MPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MPU)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_SOC_SERIES_S32K1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K1)、[`CONFIG_FLASH_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_SHELL)、[`CONFIG_SOC_FLASH_CC13XX_CC26XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_CC13XX_CC26XX)、[`CONFIG_SOC_FLASH_CC23X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_CC23X0)、[`CONFIG_SOC_FLASH_GD32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_GD32)、[`CONFIG_SOC_FLASH_GECKO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_GECKO)、[`CONFIG_FLASH_MSPI_INFINEON_S28HX512T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_MSPI_INFINEON_S28HX512T)、[`CONFIG_FLASH_MCHP_NVMCTRL_G1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_MCHP_NVMCTRL_G1)、[`CONFIG_FLASH_MCHP_NVMCTRL_G2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_MCHP_NVMCTRL_G2)、[`CONFIG_FLASH_MCHP_NVMCTRL_G3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_MCHP_NVMCTRL_G3)、[`CONFIG_SOC_FLASH_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_MCUX)、[`CONFIG_SOC_FLASH_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_NRF)、[`CONFIG_SOC_FLASH_NRF_RRAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_NRF_RRAM)、[`CONFIG_SOC_FLASH_RENESAS_RA_MRAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_RENESAS_RA_MRAM)、[`CONFIG_SOC_FLASH_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_SAM)、[`CONFIG_SOC_FLASH_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_SAM0)、[`CONFIG_SOC_FLASH_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_SILABS_S2)、[`CONFIG_SOC_FLASH_SMARTBOND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_SMARTBOND)、[`CONFIG_SOC_FLASH_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_STM32)、[`CONFIG_BT_SETTINGS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SETTINGS)、[`CONFIG_MCUMGR_GRP_IMG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_GRP_IMG)、[`CONFIG_HAWKBIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAWKBIT)、[`CONFIG_UPDATEHUB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UPDATEHUB)、[`CONFIG_USB_DFU_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DFU_CLASS)、[`CONFIG_OPENTHREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD)、[`CONFIG_SOC_FLASH_NRF_MRAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_NRF_MRAM)、[`CONFIG_SOC_FLASH_NRF_MRAMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_NRF_MRAMC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_S32K1`。

<a id="CONFIG_MPU_DISABLE_BACKGROUND_MAP"></a>

## 30.38 `CONFIG_MPU_DISABLE_BACKGROUND_MAP`

**提示（Prompt）**：禁用默认背景地址映射（Default Background Address Map）

**说明（Help）**

启用后，关闭默认 MPU 背景地址映射（Background Address Map）。SoC 定义很可能需要自行提供自定义 MPU 区域。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_MPU && CONFIG_CPU_HAS_MPU && CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_ARM_MPU_CM7_UNMAPPED_REGION
```

**定义位置（Location）**：[`arch/arm/core/mpu/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/mpu/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MPU)、[`CONFIG_CPU_HAS_MPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MPU)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ARM_MPU_CM7_UNMAPPED_REGION`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_MPU_CM7_UNMAPPED_REGION)。

<a id="CONFIG_MPU_STACK_GUARD"></a>

## 30.39 `CONFIG_MPU_STACK_GUARD`

原库同名定义共 2 条；本项为数据库第 12282 条记录，各定义分别保留。

**提示（Prompt）**：线程栈保护区（Thread Stack Guards）

**说明（Help）**

通过 MPU 启用线程栈保护区（Thread Stack Guards）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_MPU && CONFIG_CPU_HAS_MPU && CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_ARC_STACK_PROTECTION
CONFIG_ARM_STACK_PROTECTION
```

**定义位置（Location）**：[`arch/arm/core/mpu/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/mpu/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MPU)、[`CONFIG_CPU_HAS_MPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MPU)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ARC_STACK_PROTECTION`](P028_arch_arc_配置项参考.md#CONFIG_ARC_STACK_PROTECTION)、[`CONFIG_ARM_STACK_PROTECTION`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_STACK_PROTECTION)。

<a id="CONFIG_MPU_STACK_GUARD_MIN_SIZE_FLOAT"></a>

## 30.40 `CONFIG_MPU_STACK_GUARD_MIN_SIZE_FLOAT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

用于保护正在使用浮点（FP）上下文的线程栈的 ARM MPU 区域，其最小大小及适用时的对齐要求。保护区宽度设为 `128`，以容纳浮点上下文活动时 Cortex-M 异常栈帧（Exception Stack Frame）的长度。仅在浮点寄存器共享模式下才会将浮点上下文压栈，因此此选项只在选择 `FPU_SHARING` 时适用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MPU_STACK_GUARD && CONFIG_FPU_SHARING && CONFIG_ARM_MPU && CONFIG_CPU_HAS_MPU && CONFIG_ARM
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`arch/arm/core/mpu/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/mpu/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options） → 线程栈保护区（Thread Stack Guards）

**配置项引用（Symbol References）**：[`CONFIG_MPU_STACK_GUARD`](P028_arch_arc_配置项参考.md#CONFIG_MPU_STACK_GUARD)、[`CONFIG_FPU_SHARING`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU_SHARING)、[`CONFIG_ARM_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MPU)、[`CONFIG_CPU_HAS_MPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MPU)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_NEON"></a>

## 30.41 `CONFIG_NEON`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 NEON 高级单指令多数据（Advanced SIMD）协处理器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_HAS_NEON
```

**定义位置（Location）**：[`arch/arm/core/Kconfig.vfp:211`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig.vfp#L211)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_HAS_NEON`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_HAS_NEON)。

<a id="CONFIG_NULL_POINTER_EXCEPTION_DETECTION"></a>

## 30.42 `CONFIG_NULL_POINTER_EXCEPTION_DETECTION`

**提示（Prompt）**：空指针异常（Null-pointer Exception）

**说明（Help）**

提供两种实现：一种基于 DWT，另一种基于 MPU。使用此选择符号选取方案，默认禁用此功能。测试套件中会启用，并优先使用基于 DWT 的方案。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**默认值（Defaults）**

```text
CONFIG_NULL_POINTER_EXCEPTION_DETECTION_MPU if CONFIG_TEST_ARM_CORTEX_M && !CONFIG_ARM_NONSECURE_FIRMWARE && CONFIG_ARM_MPU && !CONFIG_CPU_CORTEX_M_HAS_DWT
CONFIG_NULL_POINTER_EXCEPTION_DETECTION_NONE
```

**可选项（Choices）**

```text
CONFIG_NULL_POINTER_EXCEPTION_DETECTION_NONE
CONFIG_NULL_POINTER_EXCEPTION_DETECTION_DWT
CONFIG_NULL_POINTER_EXCEPTION_DETECTION_MPU
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:418`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L418)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_NULL_POINTER_EXCEPTION_DETECTION_MPU`](P030_arch_arm_配置项参考_2.md#CONFIG_NULL_POINTER_EXCEPTION_DETECTION_MPU)、[`CONFIG_TEST_ARM_CORTEX_M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TEST_ARM_CORTEX_M)、[`CONFIG_ARM_NONSECURE_FIRMWARE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_NONSECURE_FIRMWARE)、[`CONFIG_ARM_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MPU)、[`CONFIG_CPU_CORTEX_M_HAS_DWT`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_M_HAS_DWT)、[`CONFIG_NULL_POINTER_EXCEPTION_DETECTION_NONE`](P030_arch_arm_配置项参考_2.md#CONFIG_NULL_POINTER_EXCEPTION_DETECTION_NONE)、[`CONFIG_NULL_POINTER_EXCEPTION_DETECTION_DWT`](P030_arch_arm_配置项参考_2.md#CONFIG_NULL_POINTER_EXCEPTION_DETECTION_DWT)。

<a id="CONFIG_NULL_POINTER_EXCEPTION_DETECTION_DWT"></a>

## 30.43 `CONFIG_NULL_POINTER_EXCEPTION_DETECTION_DWT`

**提示（Prompt）**：使用 DWT 检测空指针异常（Null Pointer Exception Detection）

**说明（Help）**

使用数据观察点与跟踪（DWT）单元实现空指针解引用检测（Null Pointer Dereference Detection）。

注意：非安全固件镜像不启用此功能，因为其中的空指针解引用很可能被捕获为安全故障（SecureFault）。要求 Cortex-M SoC 实现 DWT 功能，ARMv7-M 需要 1 个比较器（Comparator），ARMv8-M 需要 2 个。还要求 Cortex-M 内核处于普通模式（Normal Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_M_HAS_DWT && !CONFIG_TRUSTED_EXECUTION_NONSECURE && <choice CONFIG_NULL_POINTER_EXCEPTION_DETECTION>
```

**主动选择（Selects）**

```text
CONFIG_CORTEX_M_DWT
CONFIG_CORTEX_M_NULL_POINTER_EXCEPTION
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:437`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L437)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options） → 空指针异常（Null-pointer Exception）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M_HAS_DWT`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_M_HAS_DWT)、[`CONFIG_TRUSTED_EXECUTION_NONSECURE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRUSTED_EXECUTION_NONSECURE)、[`CONFIG_NULL_POINTER_EXCEPTION_DETECTION`](P030_arch_arm_配置项参考_2.md#CONFIG_NULL_POINTER_EXCEPTION_DETECTION)、[`CONFIG_CORTEX_M_DWT`](P029_arch_arm_配置项参考_1.md#CONFIG_CORTEX_M_DWT)、[`CONFIG_CORTEX_M_NULL_POINTER_EXCEPTION`](P029_arch_arm_配置项参考_1.md#CONFIG_CORTEX_M_NULL_POINTER_EXCEPTION)。

<a id="CONFIG_NULL_POINTER_EXCEPTION_DETECTION_MPU"></a>

## 30.44 `CONFIG_NULL_POINTER_EXCEPTION_DETECTION_MPU`

**提示（Prompt）**：使用 MPU 检测空指针异常（Null Pointer Exception Detection）

**说明（Help）**

使用内存保护单元（MPU）实现空指针解引用检测（Null Pointer Dereference Detection）。

注意：此方案与基于 DWT 的方案互斥；非安全固件镜像不启用，因为空指针解引用很可能被捕获为安全故障（SecureFault）。要求 MPU 存在且已启用，实现会消耗 1 个 MPU 区域。

在 ARMv8-M 中，使用 MPU 显式检测空指针解引用，还要求 `[0x0, CORTEX_M_NULL_POINTER_EXCEPTION_PAGE_SIZE)` 区域并非未映射，即已被某个 MPU 区域覆盖。如果未映射，仍可能通过精确总线访问故障（Precise Bus Access Fault）等方式间接检测，但无法保证。构建时会为这种情况发出提示。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_TRUSTED_EXECUTION_NONSECURE && CONFIG_ARM_MPU && <choice CONFIG_NULL_POINTER_EXCEPTION_DETECTION>
```

**主动选择（Selects）**

```text
CONFIG_CORTEX_M_NULL_POINTER_EXCEPTION
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:455`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L455)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options） → 空指针异常（Null-pointer Exception）

**配置项引用（Symbol References）**：[`CONFIG_TRUSTED_EXECUTION_NONSECURE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRUSTED_EXECUTION_NONSECURE)、[`CONFIG_ARM_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MPU)、[`CONFIG_NULL_POINTER_EXCEPTION_DETECTION`](P030_arch_arm_配置项参考_2.md#CONFIG_NULL_POINTER_EXCEPTION_DETECTION)、[`CONFIG_CORTEX_M_NULL_POINTER_EXCEPTION`](P029_arch_arm_配置项参考_1.md#CONFIG_CORTEX_M_NULL_POINTER_EXCEPTION)。

<a id="CONFIG_NULL_POINTER_EXCEPTION_DETECTION_NONE"></a>

## 30.45 `CONFIG_NULL_POINTER_EXCEPTION_DETECTION_NONE`

**提示（Prompt）**：不检测空指针异常（No Null Pointer Exception Detection）

**说明（Help）**

未启用空指针异常检测（Null Pointer Exception Detection）功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NULL_POINTER_EXCEPTION_DETECTION>
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:431`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L431)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options） → 空指针异常（Null-pointer Exception）

**配置项引用（Symbol References）**：[`CONFIG_NULL_POINTER_EXCEPTION_DETECTION`](P030_arch_arm_配置项参考_2.md#CONFIG_NULL_POINTER_EXCEPTION_DETECTION)。

<a id="CONFIG_ROMSTART_REGION_ADDRESS"></a>

## 30.46 `CONFIG_ROMSTART_REGION_ADDRESS`

**提示（Prompt）**：`rom_start` 区域基地址（Base Address）

**说明（Help）**

`rom_start` 区域起始地址，可由设备树（DT）节点的 `reg` 属性推导，也可直接指定。大多数情况下，默认值 `0x00000000` 可能可用，因为 SoC 会将启动向量（Boot Vector）所在的正确内存区域设置别名映射（Alias）：

- IMX7D：启动向量位于 OCRAM_S，实际地址 `0x00180000`，别名为 `0x0`。
- IMX6SX：启动向量位于 TCML，实际地址 `0x007F8000`，别名为 `0x0`。
- IMX8MQ：启动向量位于 TCML，实际地址 `0x007E0000`，别名为 `0x0`。
- IMX8MN：启动向量位于 ITCM，实际地址 `0x007E0000`，别名为 `0x0`。

设备树定义示例：`$(dt_nodelabel_reg_addr_hex,ocram_s_sys)`。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_ROMSTART_RELOCATION_ROM && CONFIG_ARM
```

**默认值（Defaults）**

```text
0x00000000
```

**定义位置（Location）**：[`arch/arm/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options） → 重定位 `rom_start` 区域（Relocate Region）

**配置项引用（Symbol References）**：[`CONFIG_ROMSTART_RELOCATION_ROM`](P030_arch_arm_配置项参考_2.md#CONFIG_ROMSTART_RELOCATION_ROM)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_ROMSTART_REGION_SIZE"></a>

## 30.47 `CONFIG_ROMSTART_REGION_SIZE`

**提示（Prompt）**：`rom_start` 区域大小（Region Size）

**说明（Help）**

`rom_start` 区域大小，以 KB 为单位。默认 1 KB，足以保存启动向量和 IRQ 向量（Vectors）。此设置可由设备树（DT）节点的 `reg` 属性推导，也可直接指定。对于要求将启动向量放入 OCRAM_S（`0x00180000`）的 IMX7D，示例为 `$(dt_nodelabel_reg_size_hex,ocram_s_sys,0,K)`。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_ROMSTART_RELOCATION_ROM && CONFIG_ARM
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`arch/arm/Kconfig:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/Kconfig#L92)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options） → 重定位 `rom_start` 区域（Relocate Region）

**配置项引用（Symbol References）**：[`CONFIG_ROMSTART_RELOCATION_ROM`](P030_arch_arm_配置项参考_2.md#CONFIG_ROMSTART_RELOCATION_ROM)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_ROMSTART_RELOCATION_ROM"></a>

## 30.48 `CONFIG_ROMSTART_RELOCATION_ROM`

**提示（Prompt）**：重定位 `rom_start` 区域（Relocate Region）

**说明（Help）**

将包含启动向量数据（Boot-vector Data）和 IRQ 向量的 `rom_start` 区域，重定位到 `ROMSTART_REGION_ADDRESS` 与 `ROMSTART_REGION_SIZE` 配置指定的区域。这对使用 ELF 加载器（ELF Loader）的 Linux Remoteproc 框架很有用，可将 `rom_start` 中的正确启动向量加载到正确内存位置，而不受 `zephyr,flash` 所选 ROM 区域影响。

大多数 SoC 在 `0x00000000` 为启动向量提供别名，因此相应 Linux rproc 驱动可能支持这一默认设置；若不支持，可通过附加选项指定地址。一般而言，`zephyr,flash` chosen 节点不位于启动向量内存区域时，应选择此项。虽然目标是生成正确的 `zephyr.elf`，但副作用是增大二进制文件。如果使用 `zephyr.bin` 启动次级内核，应禁用此选项。

例如在 IMX7D 上，`zephyr,flash` 可以选择 OCRAM、OCRAM_S、TCM 或 DDR 作为代码位置，但 Cortex-M 的启动向量必须位于 OCRAM_S 才能启动，其别名为 `0`，实际地址为 `0x00180000`，可用大小为 32K。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`arch/arm/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_RUNTIME_NMI"></a>

## 30.49 `CONFIG_RUNTIME_NMI`

**提示（Prompt）**：运行时挂接 NMI 处理程序（NMI Handler）

**说明（Help）**

内核提供简单的不可屏蔽中断（NMI）处理程序，被触发时只在紧循环中停留，满足 CPU 启动时必须已安装 NMI 处理程序的要求。如果需要自定义处理程序，请启用此选项，并通过 `z_arm_nmi_set_handler()` 挂接。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_REBOOT
```

**被选择（Selected by）**

```text
CONFIG_CLOCK_CONTROL_STM32_CUBE
CONFIG_COMPARATOR_RENESAS_RA_LVD
CONFIG_WDT_RENESAS_RA_NMI
CONFIG_WDT_SMARTBOND_NMI
```

**定义位置（Location）**：[`arch/arm/core/Kconfig:210`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig#L210)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_REBOOT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REBOOT)、[`CONFIG_CLOCK_CONTROL_STM32_CUBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_STM32_CUBE)、[`CONFIG_COMPARATOR_RENESAS_RA_LVD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COMPARATOR_RENESAS_RA_LVD)、[`CONFIG_WDT_RENESAS_RA_NMI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WDT_RENESAS_RA_NMI)、[`CONFIG_WDT_SMARTBOND_NMI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WDT_SMARTBOND_NMI)。

<a id="CONFIG_SLOW_FLASH_DATA"></a>

## 30.50 `CONFIG_SLOW_FLASH_DATA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

某些 SoC 访问只读数据（rodata）比获取指令慢，通常因为缺少数据缓存，因此所有访问 Flash 数据的操作都会损害性能。此选项使用汇编指令，代替字面量池（Literal Pool，即与代码交错放置的数据）。

在原文所述当前 GCC 版本 `14.x` 中，此选项与线程局部存储（Thread Local Storage，TLS）不兼容。用户可使用打过补丁的 GCC，这是推荐选项；也可通过 `CONFIG_PICOLIBC_USE_MODULE=y` 重新构建 libc，并以 `CONFIG_THREAD_LOCAL_STORAGE=n` 禁用 TLS。后一种情况下，访问 `errno` 将不再具有线程安全性（Thread Safety）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_ARMV6_M_ARMV8_M_BASELINE && CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_SILABS_SIWX91X_SLOW_FLASH_DATA
```

**定义位置（Location）**：[`arch/arm/core/Kconfig:194`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig#L194)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARMV6_M_ARMV8_M_BASELINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV6_M_ARMV8_M_BASELINE)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_SILABS_SIWX91X_SLOW_FLASH_DATA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SIWX91X_SLOW_FLASH_DATA)。

<a id="CONFIG_STACK_ALIGN_DOUBLE_WORD"></a>

## 30.51 `CONFIG_STACK_ALIGN_DOUBLE_WORD`

**提示（Prompt）**：将栈按双字对齐（Double-word Alignment，8 字节）

**说明（Help）**

为符合 ARM 过程调用标准（AAPCS），需要此对齐，但会浪费栈空间。此选项也强制 Cortex-M3 和 Cortex-M4（ARMv7-M）在异常进入（Exception Entry）时对齐栈。注意，对于 ARMv6-M、ARMv8-M 和 Cortex-M7 MCU，异常进入时的栈对齐默认启用且不可配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`arch/arm/core/Kconfig:184`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig#L184)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_SW_VECTOR_RELAY"></a>

## 30.52 `CONFIG_SW_VECTOR_RELAY`

**提示（Prompt）**：软件向量转发（Software Vector Relay）

**说明（Help）**

构建引导加载程序固件（Bootloader Firmware）时，此选项添加向量表转发处理程序和向量转发表，根据向量表指针转发中断。只有缺少 VTOR 等硬件向量表重定位机制的 Cortex-M 基线（Baseline）CPU 必须使用此功能，但其适用范围不限于这些 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_ARMV6_M_ARMV8_M_BASELINE || CONFIG_ARMV7_M_ARMV8_M_MAINLINE) && CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:367`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L367)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options） → ARM Cortex-M0/M0+/M1/M3/M4/M7/M23/M33/M55 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARMV6_M_ARMV8_M_BASELINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV6_M_ARMV8_M_BASELINE)、[`CONFIG_ARMV7_M_ARMV8_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_M_ARMV8_M_MAINLINE)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_SW_VECTOR_RELAY_CLIENT"></a>

## 30.53 `CONFIG_SW_VECTOR_RELAY_CLIENT`

**提示（Prompt）**：软件向量转发客户端（Software Vector Relay Client）

**说明（Help）**

另一镜像已启用 `SW_VECTOR_RELAY`，将把异常和硬件中断转发给本镜像。启用此选项，以确保本镜像初始化时正确设置 RAM 中的向量表指针（Vector Table Pointer）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_CPU_CORTEX_M_HAS_VTOR && (CONFIG_ARMV6_M_ARMV8_M_BASELINE || CONFIG_ARMV7_M_ARMV8_M_MAINLINE) && CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**默认值（Defaults）**

```text
y if CONFIG_BOOTLOADER_MCUBOOT && !CONFIG_CPU_CORTEX_M0_HAS_VECTOR_TABLE_REMAP
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:376`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L376)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options） → ARM Cortex-M0/M0+/M1/M3/M4/M7/M23/M33/M55 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M_HAS_VTOR`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_M_HAS_VTOR)、[`CONFIG_ARMV6_M_ARMV8_M_BASELINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV6_M_ARMV8_M_BASELINE)、[`CONFIG_ARMV7_M_ARMV8_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_M_ARMV8_M_MAINLINE)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_BOOTLOADER_MCUBOOT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOOTLOADER_MCUBOOT)、[`CONFIG_CPU_CORTEX_M0_HAS_VECTOR_TABLE_REMAP`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M0_HAS_VECTOR_TABLE_REMAP)。

<a id="CONFIG_TRAP_UNALIGNED_ACCESS"></a>

## 30.54 `CONFIG_TRAP_UNALIGNED_ACCESS`

**提示（Prompt）**：非对齐访问陷阱（Unaligned Access Trap）

**说明（Help）**

启用后，CPU 在执行半字或字访问（Halfword/Word Access）时产生用法故障（UsageFault）异常。

译注：本项标题是“非对齐访问陷阱”，但帮助原文没有写出“非对齐”限定；此处保留原文并提示该遗漏，不能据此认为所有正常对齐访问都会触发异常。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_ARMV6_M_ARMV8_M_BASELINE && (CONFIG_ARMV6_M_ARMV8_M_BASELINE || CONFIG_ARMV7_M_ARMV8_M_MAINLINE) && CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:406`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L406)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options） → ARM Cortex-M0/M0+/M1/M3/M4/M7/M23/M33/M55 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARMV6_M_ARMV8_M_BASELINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV6_M_ARMV8_M_BASELINE)、[`CONFIG_ARMV7_M_ARMV8_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_M_ARMV8_M_MAINLINE)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_VFP_DP_D16"></a>

## 30.55 `CONFIG_VFP_DP_D16`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用具有 16 个双字寄存器、支持单精度和双精度运算的向量浮点（VFP）协处理器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_HAS_VFP
CONFIG_VFP_FEATURE_SINGLE_PRECISION
CONFIG_VFP_FEATURE_DOUBLE_PRECISION
CONFIG_VFP_FEATURE_REGS_S32_D16
```

**被选择（Selected by）**

```text
CONFIG_SOC_CORTEX_R8_VIRTUAL
CONFIG_SOC_XILINX_ZYNQMP_RPU
CONFIG_SOC_VERSAL_RPU
CONFIG_SOC_R9A09G057H44GBG_CR8
CONFIG_SOC_AN536
CONFIG_SOC_S32K566_R52
CONFIG_SOC_SERIES_S32ZE
```

**定义位置（Location）**：[`arch/arm/core/Kconfig.vfp:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig.vfp#L61)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_HAS_VFP`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_HAS_VFP)、[`CONFIG_VFP_FEATURE_SINGLE_PRECISION`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_SINGLE_PRECISION)、[`CONFIG_VFP_FEATURE_DOUBLE_PRECISION`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_DOUBLE_PRECISION)、[`CONFIG_VFP_FEATURE_REGS_S32_D16`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_REGS_S32_D16)、[`CONFIG_SOC_CORTEX_R8_VIRTUAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORTEX_R8_VIRTUAL)、[`CONFIG_SOC_XILINX_ZYNQMP_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XILINX_ZYNQMP_RPU)、[`CONFIG_SOC_VERSAL_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_VERSAL_RPU)、[`CONFIG_SOC_R9A09G057H44GBG_CR8`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R9A09G057H44GBG_CR8)、[`CONFIG_SOC_AN536`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AN536)、[`CONFIG_SOC_S32K566_R52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K566_R52)、[`CONFIG_SOC_SERIES_S32ZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32ZE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_AN536`、`CONFIG_SOC_S32K566_R52`、`CONFIG_SOC_SERIES_S32ZE`。

<a id="CONFIG_VFP_DP_D16_FP16"></a>

## 30.56 `CONFIG_VFP_DP_D16_FP16`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用具有 16 个双字寄存器、支持半精度、单精度和双精度运算的向量浮点（VFP）协处理器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_HAS_VFP
CONFIG_VFP_FEATURE_HALF_PRECISION
CONFIG_VFP_FEATURE_SINGLE_PRECISION
CONFIG_VFP_FEATURE_DOUBLE_PRECISION
CONFIG_VFP_FEATURE_REGS_S32_D16
```

**定义位置（Location）**：[`arch/arm/core/Kconfig.vfp:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig.vfp#L72)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_HAS_VFP`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_HAS_VFP)、[`CONFIG_VFP_FEATURE_HALF_PRECISION`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_HALF_PRECISION)、[`CONFIG_VFP_FEATURE_SINGLE_PRECISION`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_SINGLE_PRECISION)、[`CONFIG_VFP_FEATURE_DOUBLE_PRECISION`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_DOUBLE_PRECISION)、[`CONFIG_VFP_FEATURE_REGS_S32_D16`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_REGS_S32_D16)。

<a id="CONFIG_VFP_DP_D16_FP16_FMAC"></a>

## 30.57 `CONFIG_VFP_DP_D16_FP16_FMAC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用具有 16 个双字寄存器、支持半精度、单精度和双精度运算，包括融合乘加（Fused Multiply-accumulate）的向量浮点（VFP）协处理器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_HAS_VFP
CONFIG_VFP_FEATURE_HALF_PRECISION
CONFIG_VFP_FEATURE_SINGLE_PRECISION
CONFIG_VFP_FEATURE_DOUBLE_PRECISION
CONFIG_VFP_FEATURE_FMAC
CONFIG_VFP_FEATURE_REGS_S32_D16
```

**定义位置（Location）**：[`arch/arm/core/Kconfig.vfp:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig.vfp#L84)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_HAS_VFP`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_HAS_VFP)、[`CONFIG_VFP_FEATURE_HALF_PRECISION`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_HALF_PRECISION)、[`CONFIG_VFP_FEATURE_SINGLE_PRECISION`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_SINGLE_PRECISION)、[`CONFIG_VFP_FEATURE_DOUBLE_PRECISION`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_DOUBLE_PRECISION)、[`CONFIG_VFP_FEATURE_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_FMAC)、[`CONFIG_VFP_FEATURE_REGS_S32_D16`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_REGS_S32_D16)。

<a id="CONFIG_VFP_DP_D32"></a>

## 30.58 `CONFIG_VFP_DP_D32`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用具有 32 个双字寄存器、支持单精度和双精度运算的向量浮点（VFP）协处理器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_HAS_VFP
CONFIG_VFP_FEATURE_SINGLE_PRECISION
CONFIG_VFP_FEATURE_DOUBLE_PRECISION
CONFIG_VFP_FEATURE_REGS_S64_D32
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_XC7ZXXX
CONFIG_SOC_SERIES_XC7ZXXXS
```

**定义位置（Location）**：[`arch/arm/core/Kconfig.vfp:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig.vfp#L112)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_HAS_VFP`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_HAS_VFP)、[`CONFIG_VFP_FEATURE_SINGLE_PRECISION`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_SINGLE_PRECISION)、[`CONFIG_VFP_FEATURE_DOUBLE_PRECISION`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_DOUBLE_PRECISION)、[`CONFIG_VFP_FEATURE_REGS_S64_D32`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_REGS_S64_D32)、[`CONFIG_SOC_SERIES_XC7ZXXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XC7ZXXX)、[`CONFIG_SOC_SERIES_XC7ZXXXS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XC7ZXXXS)。

<a id="CONFIG_VFP_DP_D32_FP16_FMAC"></a>

## 30.59 `CONFIG_VFP_DP_D32_FP16_FMAC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用具有 32 个双字寄存器、支持半精度、单精度和双精度运算，包括融合乘加（Fused Multiply-accumulate）的向量浮点（VFP）协处理器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_HAS_VFP
CONFIG_VFP_FEATURE_HALF_PRECISION
CONFIG_VFP_FEATURE_SINGLE_PRECISION
CONFIG_VFP_FEATURE_DOUBLE_PRECISION
CONFIG_VFP_FEATURE_FMAC
CONFIG_VFP_FEATURE_REGS_S64_D32
```

**被选择（Selected by）**

```text
CONFIG_SOC_FVP_AEMV8R_AARCH32
CONFIG_SOC_AN536
```

**定义位置（Location）**：[`arch/arm/core/Kconfig.vfp:123`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig.vfp#L123)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_HAS_VFP`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_HAS_VFP)、[`CONFIG_VFP_FEATURE_HALF_PRECISION`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_HALF_PRECISION)、[`CONFIG_VFP_FEATURE_SINGLE_PRECISION`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_SINGLE_PRECISION)、[`CONFIG_VFP_FEATURE_DOUBLE_PRECISION`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_DOUBLE_PRECISION)、[`CONFIG_VFP_FEATURE_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_FMAC)、[`CONFIG_VFP_FEATURE_REGS_S64_D32`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_REGS_S64_D32)、[`CONFIG_SOC_FVP_AEMV8R_AARCH32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FVP_AEMV8R_AARCH32)、[`CONFIG_SOC_AN536`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AN536)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FVP_AEMV8R_AARCH32`、`CONFIG_SOC_AN536`。

<a id="CONFIG_VFP_FEATURE_DOUBLE_PRECISION"></a>

## 30.60 `CONFIG_VFP_FEATURE_DOUBLE_PRECISION`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示 VFP 协处理器支持双精度运算（Double-precision Operations）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_VFP && CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_HAS_FPU_DOUBLE_PRECISION
```

**被选择（Selected by）**

```text
CONFIG_VFP_DP_D16
CONFIG_VFP_DP_D16_FP16
CONFIG_VFP_DP_D16_FP16_FMAC
CONFIG_VFP_U_DP_D16_FP16_FMAC
CONFIG_VFP_DP_D32
CONFIG_VFP_DP_D32_FP16_FMAC
CONFIG_VFP_U_DP_D32_FP16_FMAC
```

**定义位置（Location）**：[`arch/arm/core/Kconfig.vfp:168`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig.vfp#L168)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_VFP`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_HAS_VFP)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_HAS_FPU_DOUBLE_PRECISION`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU_DOUBLE_PRECISION)、[`CONFIG_VFP_DP_D16`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_DP_D16)、[`CONFIG_VFP_DP_D16_FP16`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_DP_D16_FP16)、[`CONFIG_VFP_DP_D16_FP16_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_DP_D16_FP16_FMAC)、[`CONFIG_VFP_U_DP_D16_FP16_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_U_DP_D16_FP16_FMAC)、[`CONFIG_VFP_DP_D32`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_DP_D32)、[`CONFIG_VFP_DP_D32_FP16_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_DP_D32_FP16_FMAC)、[`CONFIG_VFP_U_DP_D32_FP16_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_U_DP_D32_FP16_FMAC)。

<a id="CONFIG_VFP_FEATURE_FMAC"></a>

## 30.61 `CONFIG_VFP_FEATURE_FMAC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示 VFP 协处理器支持融合乘加运算（Fused Multiply-accumulate Operations）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_VFP && CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_VFP_SP_D16_FP16_FMAC
CONFIG_VFP_DP_D16_FP16_FMAC
CONFIG_VFP_U_DP_D16_FP16_FMAC
CONFIG_VFP_DP_D32_FP16_FMAC
CONFIG_VFP_U_DP_D32_FP16_FMAC
```

**定义位置（Location）**：[`arch/arm/core/Kconfig.vfp:181`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig.vfp#L181)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_VFP`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_HAS_VFP)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_VFP_SP_D16_FP16_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_SP_D16_FP16_FMAC)、[`CONFIG_VFP_DP_D16_FP16_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_DP_D16_FP16_FMAC)、[`CONFIG_VFP_U_DP_D16_FP16_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_U_DP_D16_FP16_FMAC)、[`CONFIG_VFP_DP_D32_FP16_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_DP_D32_FP16_FMAC)、[`CONFIG_VFP_U_DP_D32_FP16_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_U_DP_D32_FP16_FMAC)。

<a id="CONFIG_VFP_FEATURE_HALF_PRECISION"></a>

## 30.62 `CONFIG_VFP_FEATURE_HALF_PRECISION`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示 VFP 协处理器支持半精度运算，即半精度扩展（Half-precision Extension）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_VFP && CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_VFP_SP_D16_FP16
CONFIG_VFP_SP_D16_FP16_FMAC
CONFIG_VFP_DP_D16_FP16
CONFIG_VFP_DP_D16_FP16_FMAC
CONFIG_VFP_U_DP_D16_FP16_FMAC
CONFIG_VFP_DP_D32_FP16_FMAC
CONFIG_VFP_U_DP_D32_FP16_FMAC
```

**定义位置（Location）**：[`arch/arm/core/Kconfig.vfp:156`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig.vfp#L156)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_VFP`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_HAS_VFP)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_VFP_SP_D16_FP16`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_SP_D16_FP16)、[`CONFIG_VFP_SP_D16_FP16_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_SP_D16_FP16_FMAC)、[`CONFIG_VFP_DP_D16_FP16`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_DP_D16_FP16)、[`CONFIG_VFP_DP_D16_FP16_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_DP_D16_FP16_FMAC)、[`CONFIG_VFP_U_DP_D16_FP16_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_U_DP_D16_FP16_FMAC)、[`CONFIG_VFP_DP_D32_FP16_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_DP_D32_FP16_FMAC)、[`CONFIG_VFP_U_DP_D32_FP16_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_U_DP_D32_FP16_FMAC)。

<a id="CONFIG_VFP_FEATURE_REGS_S32_D16"></a>

## 30.63 `CONFIG_VFP_FEATURE_REGS_S32_D16`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示 VFP 协处理器实现 16 个双精度浮点寄存器，等效为 32 个单精度浮点寄存器（Floating-point Registers）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_VFP && CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_VFP_SP_D16
CONFIG_VFP_SP_D16_FP16
CONFIG_VFP_SP_D16_FP16_FMAC
CONFIG_VFP_DP_D16
CONFIG_VFP_DP_D16_FP16
CONFIG_VFP_DP_D16_FP16_FMAC
CONFIG_VFP_U_DP_D16_FP16_FMAC
```

**定义位置（Location）**：[`arch/arm/core/Kconfig.vfp:187`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig.vfp#L187)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_VFP`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_HAS_VFP)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_VFP_SP_D16`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_SP_D16)、[`CONFIG_VFP_SP_D16_FP16`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_SP_D16_FP16)、[`CONFIG_VFP_SP_D16_FP16_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_SP_D16_FP16_FMAC)、[`CONFIG_VFP_DP_D16`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_DP_D16)、[`CONFIG_VFP_DP_D16_FP16`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_DP_D16_FP16)、[`CONFIG_VFP_DP_D16_FP16_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_DP_D16_FP16_FMAC)、[`CONFIG_VFP_U_DP_D16_FP16_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_U_DP_D16_FP16_FMAC)。

<a id="CONFIG_VFP_FEATURE_REGS_S64_D32"></a>

## 30.64 `CONFIG_VFP_FEATURE_REGS_S64_D32`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示 VFP 协处理器实现 32 个双精度浮点寄存器，等效为 64 个单精度浮点寄存器（Floating-point Registers）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_VFP && CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_VFP_DP_D32
CONFIG_VFP_DP_D32_FP16_FMAC
CONFIG_VFP_U_DP_D32_FP16_FMAC
```

**定义位置（Location）**：[`arch/arm/core/Kconfig.vfp:193`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig.vfp#L193)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_VFP`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_HAS_VFP)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_VFP_DP_D32`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_DP_D32)、[`CONFIG_VFP_DP_D32_FP16_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_DP_D32_FP16_FMAC)、[`CONFIG_VFP_U_DP_D32_FP16_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_U_DP_D32_FP16_FMAC)。

<a id="CONFIG_VFP_FEATURE_SINGLE_PRECISION"></a>

## 30.65 `CONFIG_VFP_FEATURE_SINGLE_PRECISION`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示 VFP 协处理器支持单精度运算（Single-precision Operations）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_VFP && CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_VFP_SP_D16
CONFIG_VFP_SP_D16_FP16
CONFIG_VFP_SP_D16_FP16_FMAC
CONFIG_VFP_DP_D16
CONFIG_VFP_DP_D16_FP16
CONFIG_VFP_DP_D16_FP16_FMAC
CONFIG_VFP_U_DP_D16_FP16_FMAC
CONFIG_VFP_DP_D32
CONFIG_VFP_DP_D32_FP16_FMAC
CONFIG_VFP_U_DP_D32_FP16_FMAC
```

**定义位置（Location）**：[`arch/arm/core/Kconfig.vfp:162`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig.vfp#L162)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_VFP`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_HAS_VFP)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_VFP_SP_D16`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_SP_D16)、[`CONFIG_VFP_SP_D16_FP16`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_SP_D16_FP16)、[`CONFIG_VFP_SP_D16_FP16_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_SP_D16_FP16_FMAC)、[`CONFIG_VFP_DP_D16`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_DP_D16)、[`CONFIG_VFP_DP_D16_FP16`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_DP_D16_FP16)、[`CONFIG_VFP_DP_D16_FP16_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_DP_D16_FP16_FMAC)、[`CONFIG_VFP_U_DP_D16_FP16_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_U_DP_D16_FP16_FMAC)、[`CONFIG_VFP_DP_D32`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_DP_D32)、[`CONFIG_VFP_DP_D32_FP16_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_DP_D32_FP16_FMAC)、[`CONFIG_VFP_U_DP_D32_FP16_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_U_DP_D32_FP16_FMAC)。

<a id="CONFIG_VFP_FEATURE_TRAP"></a>

## 30.66 `CONFIG_VFP_FEATURE_TRAP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示 VFP 协处理器支持浮点异常陷入（Floating-point Exception Trapping），以便用软件实现不受支持的 VFP 指令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_VFP && CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_VFP_U_DP_D16_FP16_FMAC
CONFIG_VFP_U_DP_D32_FP16_FMAC
```

**定义位置（Location）**：[`arch/arm/core/Kconfig.vfp:199`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig.vfp#L199)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_VFP`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_HAS_VFP)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_VFP_U_DP_D16_FP16_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_U_DP_D16_FP16_FMAC)、[`CONFIG_VFP_U_DP_D32_FP16_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_U_DP_D32_FP16_FMAC)。

<a id="CONFIG_VFP_FEATURE_VECTOR"></a>

## 30.67 `CONFIG_VFP_FEATURE_VECTOR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示 VFP 协处理器支持向量运算（Vector Operations）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_VFP && CONFIG_ARM
```

**定义位置（Location）**：[`arch/arm/core/Kconfig.vfp:175`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig.vfp#L175)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_VFP`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_HAS_VFP)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_VFP_SP_D16"></a>

## 30.68 `CONFIG_VFP_SP_D16`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用具有 16 个双字寄存器、仅支持单精度运算的向量浮点（VFP）协处理器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_HAS_VFP
CONFIG_VFP_FEATURE_SINGLE_PRECISION
CONFIG_VFP_FEATURE_REGS_S32_D16
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_AM64X_R5
CONFIG_SOC_SERIES_J721E_R5
CONFIG_SOC_SERIES_J722S_R5
CONFIG_CPU_CORTEX_R52
```

**定义位置（Location）**：[`arch/arm/core/Kconfig.vfp:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig.vfp#L28)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_HAS_VFP`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_HAS_VFP)、[`CONFIG_VFP_FEATURE_SINGLE_PRECISION`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_SINGLE_PRECISION)、[`CONFIG_VFP_FEATURE_REGS_S32_D16`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_REGS_S32_D16)、[`CONFIG_SOC_SERIES_AM64X_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM64X_R5)、[`CONFIG_SOC_SERIES_J721E_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_J721E_R5)、[`CONFIG_SOC_SERIES_J722S_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_J722S_R5)、[`CONFIG_CPU_CORTEX_R52`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_R52)。

<a id="CONFIG_VFP_SP_D16_FP16"></a>

## 30.69 `CONFIG_VFP_SP_D16_FP16`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用具有 16 个双字寄存器、支持半精度和单精度运算的向量浮点（VFP）协处理器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_HAS_VFP
CONFIG_VFP_FEATURE_HALF_PRECISION
CONFIG_VFP_FEATURE_SINGLE_PRECISION
CONFIG_VFP_FEATURE_REGS_S32_D16
```

**定义位置（Location）**：[`arch/arm/core/Kconfig.vfp:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig.vfp#L38)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_HAS_VFP`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_HAS_VFP)、[`CONFIG_VFP_FEATURE_HALF_PRECISION`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_HALF_PRECISION)、[`CONFIG_VFP_FEATURE_SINGLE_PRECISION`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_SINGLE_PRECISION)、[`CONFIG_VFP_FEATURE_REGS_S32_D16`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_REGS_S32_D16)。

<a id="CONFIG_VFP_SP_D16_FP16_FMAC"></a>

## 30.70 `CONFIG_VFP_SP_D16_FP16_FMAC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用具有 16 个双字寄存器、支持半精度和单精度运算，包括融合乘加（Fused Multiply-accumulate）的向量浮点（VFP）协处理器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_HAS_VFP
CONFIG_VFP_FEATURE_HALF_PRECISION
CONFIG_VFP_FEATURE_SINGLE_PRECISION
CONFIG_VFP_FEATURE_FMAC
CONFIG_VFP_FEATURE_REGS_S32_D16
```

**定义位置（Location）**：[`arch/arm/core/Kconfig.vfp:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig.vfp#L49)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_HAS_VFP`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_HAS_VFP)、[`CONFIG_VFP_FEATURE_HALF_PRECISION`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_HALF_PRECISION)、[`CONFIG_VFP_FEATURE_SINGLE_PRECISION`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_SINGLE_PRECISION)、[`CONFIG_VFP_FEATURE_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_FMAC)、[`CONFIG_VFP_FEATURE_REGS_S32_D16`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_REGS_S32_D16)。

<a id="CONFIG_VFP_U_DP_D16_FP16_FMAC"></a>

## 30.71 `CONFIG_VFP_U_DP_D16_FP16_FMAC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用具有 16 个双字寄存器、支持半精度、单精度和双精度运算，包括融合乘加（Fused Multiply-accumulate），以及浮点异常陷入（Floating-point Exception Trapping）的向量浮点（VFP）协处理器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_HAS_VFP
CONFIG_VFP_FEATURE_HALF_PRECISION
CONFIG_VFP_FEATURE_SINGLE_PRECISION
CONFIG_VFP_FEATURE_DOUBLE_PRECISION
CONFIG_VFP_FEATURE_FMAC
CONFIG_VFP_FEATURE_REGS_S32_D16
CONFIG_VFP_FEATURE_TRAP
```

**定义位置（Location）**：[`arch/arm/core/Kconfig.vfp:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig.vfp#L97)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_HAS_VFP`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_HAS_VFP)、[`CONFIG_VFP_FEATURE_HALF_PRECISION`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_HALF_PRECISION)、[`CONFIG_VFP_FEATURE_SINGLE_PRECISION`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_SINGLE_PRECISION)、[`CONFIG_VFP_FEATURE_DOUBLE_PRECISION`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_DOUBLE_PRECISION)、[`CONFIG_VFP_FEATURE_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_FMAC)、[`CONFIG_VFP_FEATURE_REGS_S32_D16`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_REGS_S32_D16)、[`CONFIG_VFP_FEATURE_TRAP`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_TRAP)。

<a id="CONFIG_VFP_U_DP_D32_FP16_FMAC"></a>

## 30.72 `CONFIG_VFP_U_DP_D32_FP16_FMAC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用具有 32 个双字寄存器、支持半精度、单精度和双精度运算，包括融合乘加（Fused Multiply-accumulate），以及浮点异常陷入（Floating-point Exception Trapping）的向量浮点（VFP）协处理器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_HAS_VFP
CONFIG_VFP_FEATURE_HALF_PRECISION
CONFIG_VFP_FEATURE_SINGLE_PRECISION
CONFIG_VFP_FEATURE_DOUBLE_PRECISION
CONFIG_VFP_FEATURE_FMAC
CONFIG_VFP_FEATURE_REGS_S64_D32
CONFIG_VFP_FEATURE_TRAP
```

**定义位置（Location）**：[`arch/arm/core/Kconfig.vfp:136`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig.vfp#L136)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_HAS_VFP`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_HAS_VFP)、[`CONFIG_VFP_FEATURE_HALF_PRECISION`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_HALF_PRECISION)、[`CONFIG_VFP_FEATURE_SINGLE_PRECISION`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_SINGLE_PRECISION)、[`CONFIG_VFP_FEATURE_DOUBLE_PRECISION`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_DOUBLE_PRECISION)、[`CONFIG_VFP_FEATURE_FMAC`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_FMAC)、[`CONFIG_VFP_FEATURE_REGS_S64_D32`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_REGS_S64_D32)、[`CONFIG_VFP_FEATURE_TRAP`](P030_arch_arm_配置项参考_2.md#CONFIG_VFP_FEATURE_TRAP)。

<a id="CONFIG_ZERO_LATENCY_IRQS"></a>

## 30.73 `CONFIG_ZERO_LATENCY_IRQS`

**提示（Prompt）**：零延迟中断（Zero-latency Interrupts）

**说明（Help）**

内核可能保留系统中一些最高中断优先级供自身使用，这些中断不会被中断锁定（Interrupt Locking）屏蔽。连接中断时，内核会将所有中断的优先级偏移到低于这些保留级别的位置。零延迟中断（Zero-latency Interrupt）可在最高优先级设置中断，使其不受中断锁定阻塞。由于零延迟 ISR 与内核其余部分处于相同或更高优先级，因此不能使用任何内核功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_M_HAS_BASEPRI && (CONFIG_ARMV6_M_ARMV8_M_BASELINE || CONFIG_ARMV7_M_ARMV8_M_MAINLINE) && CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:331`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L331)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options） → ARM Cortex-M0/M0+/M1/M3/M4/M7/M23/M33/M55 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M_HAS_BASEPRI`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_M_HAS_BASEPRI)、[`CONFIG_ARMV6_M_ARMV8_M_BASELINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV6_M_ARMV8_M_BASELINE)、[`CONFIG_ARMV7_M_ARMV8_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_M_ARMV8_M_MAINLINE)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_ZERO_LATENCY_LEVELS"></a>

## 30.74 `CONFIG_ZERO_LATENCY_LEVELS`

**提示（Prompt）**：为零延迟保留的中断优先级数量（Number of Reserved Priority Levels）

**说明（Help）**

为零延迟中断（Zero-latency Interrupts）保留的中断优先级数量。增加此值可为零延迟中断保留多个优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZERO_LATENCY_IRQS && (CONFIG_ARMV6_M_ARMV8_M_BASELINE || CONFIG_ARMV7_M_ARMV8_M_MAINLINE) && CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:347`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L347)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options） → ARM Cortex-M0/M0+/M1/M3/M4/M7/M23/M33/M55 选项（Options） → 零延迟中断（Zero-latency Interrupts）

**配置项引用（Symbol References）**：[`CONFIG_ZERO_LATENCY_IRQS`](P030_arch_arm_配置项参考_2.md#CONFIG_ZERO_LATENCY_IRQS)、[`CONFIG_ARMV6_M_ARMV8_M_BASELINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV6_M_ARMV8_M_BASELINE)、[`CONFIG_ARMV7_M_ARMV8_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_M_ARMV8_M_MAINLINE)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<!-- kconfig-navigation -->

[上一章](P029_arch_arm_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P031_arch_arm64_配置项参考.md)
