---
id: learning.zephyr-docs.kconfig-reference.page-411
title: "`subsys/pm`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第411章\_`subsys/pm`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/pm` 的 35 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_HAS_PM"></a>

## 411.1 `CONFIG_HAS_PM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

提供电源管理钩子（PM hook），即用于配置低功耗状态的调用，的片上系统（SoC）必须选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_KB106X
CONFIG_SOC_SERIES_PSOC4100TP
CONFIG_SOC_FAMILY_CH32V
CONFIG_SOC_LPC55S69_CPU0
CONFIG_SOC_SERIES_MEC15XX
CONFIG_SOC_SERIES_MEC165XB
CONFIG_SOC_SERIES_MEC172X
CONFIG_SOC_SERIES_MEC174X
CONFIG_SOC_SERIES_MEC175X
CONFIG_SOC_SERIES_RP2350
CONFIG_SOC_SERIES_RA8D1
CONFIG_SOC_SERIES_RA8D2
CONFIG_SOC_SERIES_RA8E1
CONFIG_SOC_SERIES_RA8M1
CONFIG_SOC_SERIES_RA8M2
CONFIG_SOC_SERIES_RA8P1
CONFIG_SOC_SERIES_RA8T1
CONFIG_SOC_SERIES_RA8T2
CONFIG_SOC_SERIES_ESP32
CONFIG_SOC_SERIES_ESP32C2
CONFIG_SOC_SERIES_ESP32C3
CONFIG_SOC_SERIES_ESP32C5
CONFIG_SOC_SERIES_ESP32C6
CONFIG_SOC_SERIES_ESP32C61
CONFIG_SOC_SERIES_ESP32H2
CONFIG_SOC_SERIES_ESP32P4
CONFIG_SOC_SERIES_ESP32S2
CONFIG_SOC_SERIES_ESP32S3
CONFIG_SOC_SERIES_MCXA1X3
CONFIG_SOC_SERIES_MCXA1X6
CONFIG_SOC_SERIES_MCXAXX6
CONFIG_SOC_SERIES_MCXAXX4
CONFIG_SOC_SERIES_MCXAXX7
CONFIG_SOC_FAMILY_MCXC
CONFIG_SOC_SERIES_MCXE24X
CONFIG_SOC_MCXN947_CPU0
CONFIG_SOC_MCXN547_CPU0
CONFIG_SOC_MCXN236
CONFIG_SOC_FAMILY_MCXW
CONFIG_SOC_SERIES_MCXW2XX
CONFIG_SOC_SERIES_MCXW2XX
CONFIG_SOC_MCXW716C
CONFIG_SOC_MCXW727C
CONFIG_SOC_SERIES_EFM32HG
CONFIG_SOC_SERIES_EFM32TG
CONFIG_SOC_SERIES_EFM32WG
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
CONFIG_SOC_SERIES_IMXRT11XX
CONFIG_SOC_MIMXRT595S_CM33
CONFIG_SOC_MIMXRT685S_CM33
CONFIG_SOC_MIMXRT798S_CM33_CPU0
CONFIG_SOC_MIMXRT798S_CM33_CPU1
CONFIG_SOC_SERIES_KE1XF
CONFIG_SOC_SERIES_KE1XZ
CONFIG_SOC_NRF54H20_CPUAPP_COMMON
CONFIG_SOC_NRF54H20_CPURAD_COMMON
CONFIG_SOC_NRF9230_ENGB_CPUAPP
CONFIG_SOC_NRF9230_ENGB_CPURAD
CONFIG_SOC_MIMX9352_A55
CONFIG_SOC_MIMX94398_M33
CONFIG_SOC_MIMX94398_M7_0
CONFIG_SOC_MIMX94398_M7_1
CONFIG_SOC_MIMX9596_M7
CONFIG_SOC_MIMX9529_M7
CONFIG_SOC_SERIES_PSE84
CONFIG_SOC_SERIES_CYW20829
CONFIG_SOC_SERIES_PSC3
CONFIG_SOC_SERIES_CC13X2_CC26X2
CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7
CONFIG_SOC_SERIES_CC23X0
CONFIG_SOC_SERIES_IT51XXX
CONFIG_SOC_SERIES_IT8XXX2
CONFIG_SOC_SERIES_APOLLO3X
CONFIG_SOC_SERIES_APOLLO4X
CONFIG_SOC_SERIES_APOLLO5X
CONFIG_SOC_SERIES_DA1469X
CONFIG_SOC_SERIES_INTEL_ADSP_ACE
CONFIG_SOC_SERIES_INTEL_ADSP_CAVS
CONFIG_SOC_SERIES_RX130
CONFIG_SOC_FAMILY_INTEL_ISH
CONFIG_SOC_FAMILY_MAX32_M33
CONFIG_SOC_FAMILY_MAX32_M4
CONFIG_SOC_SERIES_MSPM0G
CONFIG_SOC_SERIES_MSPM0L
CONFIG_SOC_SERIES_RTS5912
CONFIG_SOC_SERIES_STM32C0X
CONFIG_SOC_SERIES_STM32C5X
CONFIG_SOC_SERIES_STM32F1X
CONFIG_SOC_SERIES_STM32F4X
CONFIG_SOC_SERIES_STM32G0X
CONFIG_SOC_SERIES_STM32G4X
CONFIG_SOC_SERIES_STM32H5X
CONFIG_SOC_SERIES_STM32L0X
CONFIG_SOC_SERIES_STM32L1X
CONFIG_SOC_SERIES_STM32L4X
CONFIG_SOC_SERIES_STM32L5X
CONFIG_SOC_SERIES_STM32U0X
CONFIG_SOC_SERIES_STM32U3X
CONFIG_SOC_SERIES_STM32U5X
CONFIG_SOC_SERIES_STM32WB0X
CONFIG_SOC_SERIES_STM32WBAX
CONFIG_SOC_SERIES_STM32WBX
CONFIG_SOC_SERIES_STM32WLX
CONFIG_SOC_SERIES_NPCK3
CONFIG_SOC_SERIES_NPCX4
CONFIG_SOC_SERIES_NPCX7
CONFIG_SOC_SERIES_NPCX9
CONFIG_SOC_SERIES_RW6XX
```

**定义位置（Location）**：[`subsys/pm/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_KB106X`](P274_soc_ene_配置项参考.md#CONFIG_SOC_SERIES_KB106X)、[`CONFIG_SOC_SERIES_PSOC4100TP`](P280_soc_infineon_配置项参考.md#CONFIG_SOC_SERIES_PSOC4100TP)、[`CONFIG_SOC_FAMILY_CH32V`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_CH32V)、[`CONFIG_SOC_LPC55S69_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S69_CPU0)、[`CONFIG_SOC_SERIES_MEC15XX`](P285_soc_microchip_配置项参考_1.md#CONFIG_SOC_SERIES_MEC15XX)、[`CONFIG_SOC_SERIES_MEC165XB`](P285_soc_microchip_配置项参考_1.md#CONFIG_SOC_SERIES_MEC165XB)、[`CONFIG_SOC_SERIES_MEC172X`](P285_soc_microchip_配置项参考_1.md#CONFIG_SOC_SERIES_MEC172X)、[`CONFIG_SOC_SERIES_MEC174X`](P285_soc_microchip_配置项参考_1.md#CONFIG_SOC_SERIES_MEC174X)、[`CONFIG_SOC_SERIES_MEC175X`](P285_soc_microchip_配置项参考_1.md#CONFIG_SOC_SERIES_MEC175X)、[`CONFIG_SOC_SERIES_RP2350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RP2350)、[`CONFIG_SOC_SERIES_RA8D1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8D1)、[`CONFIG_SOC_SERIES_RA8D2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8D2)、[`CONFIG_SOC_SERIES_RA8E1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8E1)、[`CONFIG_SOC_SERIES_RA8M1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8M1)、[`CONFIG_SOC_SERIES_RA8M2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8M2)、[`CONFIG_SOC_SERIES_RA8P1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8P1)、[`CONFIG_SOC_SERIES_RA8T1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8T1)、[`CONFIG_SOC_SERIES_RA8T2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8T2)、[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32C3)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_SERIES_ESP32S2`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_SERIES_MCXA1X3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXA1X3)、[`CONFIG_SOC_SERIES_MCXA1X6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXA1X6)、[`CONFIG_SOC_SERIES_MCXAXX6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXAXX6)、[`CONFIG_SOC_SERIES_MCXAXX4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXAXX4)、[`CONFIG_SOC_SERIES_MCXAXX7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXAXX7)、[`CONFIG_SOC_FAMILY_MCXC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXC)、[`CONFIG_SOC_SERIES_MCXE24X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE24X)、[`CONFIG_SOC_MCXN947_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN947_CPU0)、[`CONFIG_SOC_MCXN547_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN547_CPU0)、[`CONFIG_SOC_MCXN236`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN236)、[`CONFIG_SOC_FAMILY_MCXW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXW)、[`CONFIG_SOC_SERIES_MCXW2XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXW2XX)、[`CONFIG_SOC_MCXW716C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXW716C)、[`CONFIG_SOC_MCXW727C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXW727C)、[`CONFIG_SOC_SERIES_EFM32HG`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFM32HG)、[`CONFIG_SOC_SERIES_EFM32TG`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFM32TG)、[`CONFIG_SOC_SERIES_EFM32WG`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFM32WG)、[`CONFIG_SOC_SERIES_EFM32JG12B`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFM32JG12B)、[`CONFIG_SOC_SERIES_EFM32PG12B`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFM32PG12B)、[`CONFIG_SOC_SERIES_EFM32PG1B`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFM32PG1B)、[`CONFIG_SOC_SERIES_EFR32BG13P`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32BG13P)、[`CONFIG_SOC_SERIES_EFR32FG13P`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32FG13P)、[`CONFIG_SOC_SERIES_EFR32FG1P`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32FG1P)、[`CONFIG_SOC_SERIES_EFR32MG12P`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32MG12P)、[`CONFIG_SOC_SERIES_EFR32MG13P`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32MG13P)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG21`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S2_XG21)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG22`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S2_XG22)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG23`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S2_XG23)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG24`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S2_XG24)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG26`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S2_XG26)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG27`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S2_XG27)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG28`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S2_XG28)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG29`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S2_XG29)、[`CONFIG_SOC_FAMILY_SILABS_S3_SIX301`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S3_SIX301)、[`CONFIG_SOC_FAMILY_SILABS_SIWX91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_SIWX91X)、[`CONFIG_SOC_SERIES_IMXRT10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT10XX)、[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_MIMXRT595S_CM33`](P294_soc_nxp_配置项参考_2.md#CONFIG_SOC_MIMXRT595S_CM33)、[`CONFIG_SOC_MIMXRT685S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_CM33)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU1)、[`CONFIG_SOC_SERIES_KE1XF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KE1XF)、[`CONFIG_SOC_SERIES_KE1XZ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KE1XZ)、[`CONFIG_SOC_NRF54H20_CPUAPP_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPUAPP_COMMON)、[`CONFIG_SOC_NRF54H20_CPURAD_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPURAD_COMMON)、[`CONFIG_SOC_NRF9230_ENGB_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9230_ENGB_CPUAPP)、[`CONFIG_SOC_NRF9230_ENGB_CPURAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9230_ENGB_CPURAD)、[`CONFIG_SOC_MIMX9352_A55`](P294_soc_nxp_配置项参考_2.md#CONFIG_SOC_MIMX9352_A55)、[`CONFIG_SOC_MIMX94398_M33`](P294_soc_nxp_配置项参考_2.md#CONFIG_SOC_MIMX94398_M33)、[`CONFIG_SOC_MIMX94398_M7_0`](P294_soc_nxp_配置项参考_2.md#CONFIG_SOC_MIMX94398_M7_0)、[`CONFIG_SOC_MIMX94398_M7_1`](P294_soc_nxp_配置项参考_2.md#CONFIG_SOC_MIMX94398_M7_1)、[`CONFIG_SOC_MIMX9596_M7`](P294_soc_nxp_配置项参考_2.md#CONFIG_SOC_MIMX9596_M7)、[`CONFIG_SOC_MIMX9529_M7`](P294_soc_nxp_配置项参考_2.md#CONFIG_SOC_MIMX9529_M7)、[`CONFIG_SOC_SERIES_PSE84`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSE84)、[`CONFIG_SOC_SERIES_CYW20829`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CYW20829)、[`CONFIG_SOC_SERIES_PSC3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSC3)、[`CONFIG_SOC_SERIES_CC13X2_CC26X2`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC13X2_CC26X2)、[`CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7)、[`CONFIG_SOC_SERIES_CC23X0`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC23X0)、[`CONFIG_SOC_SERIES_IT51XXX`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT51XXX)、[`CONFIG_SOC_SERIES_IT8XXX2`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT8XXX2)、[`CONFIG_SOC_SERIES_APOLLO3X`](P260_soc_ambiq_配置项参考.md#CONFIG_SOC_SERIES_APOLLO3X)、[`CONFIG_SOC_SERIES_APOLLO4X`](P260_soc_ambiq_配置项参考.md#CONFIG_SOC_SERIES_APOLLO4X)、[`CONFIG_SOC_SERIES_APOLLO5X`](P260_soc_ambiq_配置项参考.md#CONFIG_SOC_SERIES_APOLLO5X)、[`CONFIG_SOC_SERIES_DA1469X`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_DA1469X)、[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE`](P281_soc_intel_配置项参考.md#CONFIG_SOC_SERIES_INTEL_ADSP_ACE)、[`CONFIG_SOC_SERIES_INTEL_ADSP_CAVS`](P281_soc_intel_配置项参考.md#CONFIG_SOC_SERIES_INTEL_ADSP_CAVS)、[`CONFIG_SOC_SERIES_RX130`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RX130)、[`CONFIG_SOC_FAMILY_INTEL_ISH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ISH)、[`CONFIG_SOC_FAMILY_MAX32_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_M33)、[`CONFIG_SOC_FAMILY_MAX32_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_M4)、[`CONFIG_SOC_SERIES_MSPM0G`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_MSPM0G)、[`CONFIG_SOC_SERIES_MSPM0L`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_MSPM0L)、[`CONFIG_SOC_SERIES_RTS5912`](P301_soc_realtek_配置项参考.md#CONFIG_SOC_SERIES_RTS5912)、[`CONFIG_SOC_SERIES_STM32C0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32C0X)、[`CONFIG_SOC_SERIES_STM32C5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32C5X)、[`CONFIG_SOC_SERIES_STM32F1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F1X)、[`CONFIG_SOC_SERIES_STM32F4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F4X)、[`CONFIG_SOC_SERIES_STM32G0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32G0X)、[`CONFIG_SOC_SERIES_STM32G4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32G4X)、[`CONFIG_SOC_SERIES_STM32H5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H5X)、[`CONFIG_SOC_SERIES_STM32L0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L0X)、[`CONFIG_SOC_SERIES_STM32L1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L1X)、[`CONFIG_SOC_SERIES_STM32L4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L4X)、[`CONFIG_SOC_SERIES_STM32L5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L5X)、[`CONFIG_SOC_SERIES_STM32U0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U0X)、[`CONFIG_SOC_SERIES_STM32U3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U3X)、[`CONFIG_SOC_SERIES_STM32U5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U5X)、[`CONFIG_SOC_SERIES_STM32WB0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WB0X)、[`CONFIG_SOC_SERIES_STM32WBAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBAX)、[`CONFIG_SOC_SERIES_STM32WBX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBX)、[`CONFIG_SOC_SERIES_STM32WLX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WLX)、[`CONFIG_SOC_SERIES_NPCK3`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_SERIES_NPCK3)、[`CONFIG_SOC_SERIES_NPCX4`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_SERIES_NPCX4)、[`CONFIG_SOC_SERIES_NPCX7`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_SERIES_NPCX7)、[`CONFIG_SOC_SERIES_NPCX9`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_SERIES_NPCX9)、[`CONFIG_SOC_SERIES_RW6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RW6XX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_CH32V`、`CONFIG_SOC_LPC55S69_CPU0`、`CONFIG_SOC_SERIES_RP2350`、`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32H2`、`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_SERIES_MCXA1X3`、`CONFIG_SOC_SERIES_MCXA1X6`、`CONFIG_SOC_SERIES_MCXAXX6`、`CONFIG_SOC_SERIES_MCXAXX4`、`CONFIG_SOC_SERIES_MCXAXX7`、`CONFIG_SOC_FAMILY_MCXC`、`CONFIG_SOC_SERIES_MCXE24X`、`CONFIG_SOC_MCXN947_CPU0`、`CONFIG_SOC_MCXN547_CPU0`、`CONFIG_SOC_MCXN236`、`CONFIG_SOC_FAMILY_MCXW`、`CONFIG_SOC_SERIES_MCXW2XX`、`CONFIG_SOC_MCXW716C`、`CONFIG_SOC_MCXW727C`、`CONFIG_SOC_FAMILY_SILABS_SIWX91X`、`CONFIG_SOC_SERIES_IMXRT10XX`、`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_MIMXRT685S_CM33`、`CONFIG_SOC_MIMXRT798S_CM33_CPU0`、`CONFIG_SOC_MIMXRT798S_CM33_CPU1`、`CONFIG_SOC_SERIES_KE1XF`、`CONFIG_SOC_SERIES_KE1XZ`、`CONFIG_SOC_NRF54H20_CPUAPP_COMMON`、`CONFIG_SOC_NRF54H20_CPURAD_COMMON`、`CONFIG_SOC_NRF9230_ENGB_CPUAPP`、`CONFIG_SOC_NRF9230_ENGB_CPURAD`、`CONFIG_SOC_SERIES_PSE84`、`CONFIG_SOC_SERIES_CYW20829`、`CONFIG_SOC_SERIES_PSC3`、`CONFIG_SOC_FAMILY_INTEL_ISH`、`CONFIG_SOC_FAMILY_MAX32_M33`、`CONFIG_SOC_FAMILY_MAX32_M4`、`CONFIG_SOC_SERIES_STM32C0X`、`CONFIG_SOC_SERIES_STM32C5X`、`CONFIG_SOC_SERIES_STM32F1X`、`CONFIG_SOC_SERIES_STM32F4X`、`CONFIG_SOC_SERIES_STM32G0X`、`CONFIG_SOC_SERIES_STM32G4X`、`CONFIG_SOC_SERIES_STM32H5X`、`CONFIG_SOC_SERIES_STM32L0X`、`CONFIG_SOC_SERIES_STM32L1X`、`CONFIG_SOC_SERIES_STM32L4X`、`CONFIG_SOC_SERIES_STM32L5X`、`CONFIG_SOC_SERIES_STM32U0X`、`CONFIG_SOC_SERIES_STM32U3X`、`CONFIG_SOC_SERIES_STM32U5X`、`CONFIG_SOC_SERIES_STM32WB0X`、`CONFIG_SOC_SERIES_STM32WBAX`、`CONFIG_SOC_SERIES_STM32WBX`、`CONFIG_SOC_SERIES_STM32WLX`、`CONFIG_SOC_SERIES_RW6XX`。

<a id="CONFIG_HAS_PM_S2RAM_CUSTOM_MARKING"></a>

## 411.2 `CONFIG_HAS_PM_S2RAM_CUSTOM_MARKING`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

默认使用 RAM 中的魔数（Magic word）标记进入挂起到 RAM（Suspend-to-RAM）状态。选中此项时，必须提供处理该标记的函数的自定义实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_PM
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_RP2350
CONFIG_SOC_NRF54H20_CPUAPP_COMMON
CONFIG_SOC_NRF9230_ENGB_CPUAPP
CONFIG_SOC_SERIES_PSC3
CONFIG_SOC_SERIES_STM32WB0X
CONFIG_SOC_SERIES_STM32WBAX
```

**定义位置（Location）**：[`subsys/pm/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management）

**配置项引用（Symbol References）**：[`CONFIG_HAS_PM`](P411_subsys_pm_配置项参考.md#CONFIG_HAS_PM)、[`CONFIG_SOC_SERIES_RP2350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RP2350)、[`CONFIG_SOC_NRF54H20_CPUAPP_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPUAPP_COMMON)、[`CONFIG_SOC_NRF9230_ENGB_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9230_ENGB_CPUAPP)、[`CONFIG_SOC_SERIES_PSC3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSC3)、[`CONFIG_SOC_SERIES_STM32WB0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WB0X)、[`CONFIG_SOC_SERIES_STM32WBAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBAX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_RP2350`、`CONFIG_SOC_NRF54H20_CPUAPP_COMMON`、`CONFIG_SOC_NRF9230_ENGB_CPUAPP`、`CONFIG_SOC_SERIES_PSC3`、`CONFIG_SOC_SERIES_STM32WB0X`、`CONFIG_SOC_SERIES_STM32WBAX`。

<a id="CONFIG_PM"></a>

## 411.3 `CONFIG_PM`

**提示（Prompt）**：系统电源管理（System Power Management）

**说明（Help）**

允许开发板在内核进入空闲（Idle）时实施额外电源管理策略。内核会告知电源管理子系统，距离下一个内核定时器到期还有多少个时钟节拍（Tick）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SYS_CLOCK_EXISTS && CONFIG_HAS_PM
```

**定义位置（Location）**：[`subsys/pm/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_HAS_PM`](P411_subsys_pm_配置项参考.md#CONFIG_HAS_PM)。

<a id="CONFIG_PM_CPU_SHELL"></a>

## 411.4 `CONFIG_PM_CPU_SHELL`

**提示（Prompt）**：CPU 电源管理命令行（Power Management shell）

**说明（Help）**

启用 CPU 电源管理命令行（Power Management shell），通过命令行接口触发 CPU 电源管理事件。支持：

- 列出设备树（Devicetree）描述的 CPU 低功耗状态。
- 检查这些状态当前是否可用。
- 使命令行线程空闲，让系统自然进入低功耗状态。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**定义位置（Location）**：[`subsys/pm/Kconfig:280`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/Kconfig#L280)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)。

<a id="CONFIG_PM_CUSTOM_TICKS_HOOK"></a>

## 411.5 `CONFIG_PM_CUSTOM_TICKS_HOOK`

**提示（Prompt）**：电源管理策略的自定义时钟节拍钩子（Custom ticks hook）

**说明（Help）**

启用策略层钩子（Policy-level hook），在 `pm_system_suspend()` 期间提供自定义的“下一事件”时钟节拍（Tick）值。适用于下一事件时间来自专有或复杂数据源，难以转换为标准电源管理（PM）策略事件列表的情况，例如：

- 硬件寄存器中保存的时间信息。
- 仅提供二进制的模块（Binary-only module）。
- 复杂调度数据结构（Scheduling data structure）。

启用后，PM 核心调用 `pm_policy_next_custom_ticks()` 获取额外的候选节拍值，并在选择最早到期时间时纳入考虑。不确定是否需要时选择 `N`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PM
```

**定义位置（Location）**：[`subsys/pm/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 系统电源管理（System Power Management）

**配置项引用（Symbol References）**：[`CONFIG_PM`](P411_subsys_pm_配置项参考.md#CONFIG_PM)。

<a id="CONFIG_PM_DEVICE"></a>

## 411.6 `CONFIG_PM_DEVICE`

**提示（Prompt）**：设备电源管理（Device Power Management）

**说明（Help）**

启用设备电源管理接口（Device power management interface）。电源管理子系统调用设备驱动实现的接口，使驱动能够执行关闭设备时钟、关闭外设等必要操作。驱动也可在这些钩子函数（Hook function）中保存和恢复状态。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_CC23X0
CONFIG_SOC_SERIES_DA1469X
CONFIG_SOC_SERIES_STM32WB0X
CONFIG_SOC_SERIES_STM32WBAX
```

**定义位置（Location）**：[`subsys/pm/Kconfig:146`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/Kconfig#L146)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_CC23X0`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC23X0)、[`CONFIG_SOC_SERIES_DA1469X`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_DA1469X)、[`CONFIG_SOC_SERIES_STM32WB0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WB0X)、[`CONFIG_SOC_SERIES_STM32WBAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBAX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32WB0X`、`CONFIG_SOC_SERIES_STM32WBAX`。

<a id="CONFIG_PM_DEVICE_DRIVER_NEEDS_DEDICATED_WQ"></a>

## 411.7 `CONFIG_PM_DEVICE_DRIVER_NEEDS_DEDICATED_WQ`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用此选项表明驱动在挂起（Suspend）期间会执行阻塞操作（Blocking operation），因此不能使用系统工作队列（System workqueue）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PM_DEVICE_RUNTIME && CONFIG_PM_DEVICE
```

**被选择（Selected by）**

```text
CONFIG_MODEM_CELLULAR
```

**定义位置（Location）**：[`subsys/pm/Kconfig:193`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/Kconfig#L193)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 设备电源管理（Device Power Management） → 设备运行时电源管理（Runtime Device Power Management）

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE_RUNTIME`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE_RUNTIME)、[`CONFIG_PM_DEVICE`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE)、[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)。

<a id="CONFIG_PM_DEVICE_POWER_DOMAIN"></a>

## 411.8 `CONFIG_PM_DEVICE_POWER_DOMAIN`

**提示（Prompt）**：电源域（Power domain）

**说明（Help）**

启用电源域（Power Domain）支持。启用后，依赖某个电源域的设备会在该域挂起（Suspend）或恢复（Resume）时收到通知。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PM_DEVICE && CONFIG_PM_DEVICE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/pm/Kconfig:162`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/Kconfig#L162)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 设备电源管理（Device Power Management）

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE)。

<a id="CONFIG_PM_DEVICE_POWER_DOMAIN_DYNAMIC"></a>

## 411.9 `CONFIG_PM_DEVICE_POWER_DOMAIN_DYNAMIC`

**提示（Prompt）**：将设备动态绑定到电源域（Power Domain）

**说明（Help）**

启用将设备动态绑定（Dynamic binding）到电源域（Power Domain）的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PM_DEVICE_POWER_DOMAIN && CONFIG_DEVICE_DEPS_DYNAMIC && CONFIG_PM_DEVICE
```

**定义位置（Location）**：[`subsys/pm/Kconfig:171`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/Kconfig#L171)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 设备电源管理（Device Power Management） → 电源域（Power domain）

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE_POWER_DOMAIN`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE_POWER_DOMAIN)、[`CONFIG_DEVICE_DEPS_DYNAMIC`](P001_kernel_配置项参考_1.md#CONFIG_DEVICE_DEPS_DYNAMIC)、[`CONFIG_PM_DEVICE`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE)。

<a id="CONFIG_PM_DEVICE_POWER_DOMAIN_DYNAMIC_NUM"></a>

## 411.10 `CONFIG_PM_DEVICE_POWER_DOMAIN_DYNAMIC_NUM`

**提示（Prompt）**：可动态绑定到电源域（Power Domain）的设备数量

**说明（Help）**

可动态绑定到电源域（Power Domain）的设备数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PM_DEVICE_POWER_DOMAIN_DYNAMIC && CONFIG_PM_DEVICE
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/pm/Kconfig:177`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/Kconfig#L177)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 设备电源管理（Device Power Management） → 电源域（Power domain） → 将设备动态绑定到电源域（Power Domain）

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE_POWER_DOMAIN_DYNAMIC`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE_POWER_DOMAIN_DYNAMIC)、[`CONFIG_PM_DEVICE`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE)。

<a id="CONFIG_PM_DEVICE_RUNTIME"></a>

## 411.11 `CONFIG_PM_DEVICE_RUNTIME`

**提示（Prompt）**：设备运行时电源管理（Runtime Device Power Management）

**说明（Help）**

启用运行时电源管理（Runtime Power Management）以节省电量。启用设备运行时 PM 后，即使 CPU 或系统仍在运行，也能根据设备使用情况挂起（Suspend）或恢复（Resume）设备。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PM_DEVICE
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_STM32WBAX
```

**定义位置（Location）**：[`subsys/pm/Kconfig:184`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/Kconfig#L184)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 设备电源管理（Device Power Management）

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE)、[`CONFIG_SOC_SERIES_STM32WBAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBAX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32WBAX`。

<a id="CONFIG_PM_DEVICE_RUNTIME_ASYNC"></a>

## 411.12 `CONFIG_PM_DEVICE_RUNTIME_ASYNC`

**提示（Prompt）**：异步设备运行时电源管理（Asynchronous device runtime power management）

**说明（Help）**

启用设备运行时电源管理中的异步操作（Asynchronous operation）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PM_DEVICE_RUNTIME && CONFIG_PM_DEVICE
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_EVENTS
```

**被选择（Selected by）**

```text
CONFIG_MODEM_PPP
```

**定义位置（Location）**：[`subsys/pm/Kconfig:200`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/Kconfig#L200)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 设备电源管理（Device Power Management） → 设备运行时电源管理（Runtime Device Power Management）

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE_RUNTIME`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE_RUNTIME)、[`CONFIG_PM_DEVICE`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)、[`CONFIG_MODEM_PPP`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_PPP)。

<a id="CONFIG_PM_DEVICE_RUNTIME_DEDICATED_WQ_INIT_PRIO"></a>

## 411.13 `CONFIG_PM_DEVICE_RUNTIME_DEDICATED_WQ_INIT_PRIO`

**提示（Prompt）**：设备运行时电源管理工作队列的初始化优先级（Initialization priority）

**说明（Help）**

设置设备运行时工作队列（Device runtime workqueue）的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PM_DEVICE_RUNTIME_USE_DEDICATED_WQ && <choice CONFIG_PM_DEVICE_RUNTIME_WQ>
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`subsys/pm/Kconfig:240`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/Kconfig#L240)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 设备电源管理（Device Power Management） → 设备运行时电源管理（Runtime Device Power Management） → 异步设备运行时电源管理（Asynchronous device runtime power management） → 设备运行时电源管理异步操作所用工作队列（Workqueue） → 使用专用工作队列（Dedicated workqueue）

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE_RUNTIME_USE_DEDICATED_WQ`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE_RUNTIME_USE_DEDICATED_WQ)、[`CONFIG_PM_DEVICE_RUNTIME_WQ`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE_RUNTIME_WQ)。

<a id="CONFIG_PM_DEVICE_RUNTIME_DEDICATED_WQ_PRIO"></a>

## 411.14 `CONFIG_PM_DEVICE_RUNTIME_DEDICATED_WQ_PRIO`

**提示（Prompt）**：设备运行时电源管理工作队列的优先级，应使用可抢占（Pre-emptible）的优先级。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PM_DEVICE_RUNTIME_USE_DEDICATED_WQ && <choice CONFIG_PM_DEVICE_RUNTIME_WQ>
```

**默认值（Defaults）**

```text
CONFIG_SYSTEM_WORKQUEUE_PRIORITY if CONFIG_PM_DEVICE_RUNTIME_USE_SYSTEM_WQ
0
```

**定义位置（Location）**：[`subsys/pm/Kconfig:235`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/Kconfig#L235)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 设备电源管理（Device Power Management） → 设备运行时电源管理（Runtime Device Power Management） → 异步设备运行时电源管理（Asynchronous device runtime power management） → 设备运行时电源管理异步操作所用工作队列（Workqueue） → 使用专用工作队列（Dedicated workqueue）

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE_RUNTIME_USE_DEDICATED_WQ`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE_RUNTIME_USE_DEDICATED_WQ)、[`CONFIG_PM_DEVICE_RUNTIME_WQ`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE_RUNTIME_WQ)、[`CONFIG_SYSTEM_WORKQUEUE_PRIORITY`](P002_kernel_配置项参考_2.md#CONFIG_SYSTEM_WORKQUEUE_PRIORITY)、[`CONFIG_PM_DEVICE_RUNTIME_USE_SYSTEM_WQ`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE_RUNTIME_USE_SYSTEM_WQ)。

<a id="CONFIG_PM_DEVICE_RUNTIME_DEDICATED_WQ_STACK_SIZE"></a>

## 411.15 `CONFIG_PM_DEVICE_RUNTIME_DEDICATED_WQ_STACK_SIZE`

**提示（Prompt）**：运行时电源管理异步工作队列栈大小（Workqueue stack size）

**说明（Help）**

定义异步操作（Asynchronous operation）所用工作队列的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PM_DEVICE_RUNTIME_USE_DEDICATED_WQ && <choice CONFIG_PM_DEVICE_RUNTIME_WQ>
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/pm/Kconfig:228`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/Kconfig#L228)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 设备电源管理（Device Power Management） → 设备运行时电源管理（Runtime Device Power Management） → 异步设备运行时电源管理（Asynchronous device runtime power management） → 设备运行时电源管理异步操作所用工作队列（Workqueue） → 使用专用工作队列（Dedicated workqueue）

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE_RUNTIME_USE_DEDICATED_WQ`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE_RUNTIME_USE_DEDICATED_WQ)、[`CONFIG_PM_DEVICE_RUNTIME_WQ`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE_RUNTIME_WQ)。

<a id="CONFIG_PM_DEVICE_RUNTIME_DEFAULT_ENABLE"></a>

## 411.16 `CONFIG_PM_DEVICE_RUNTIME_DEFAULT_ENABLE`

**提示（Prompt）**：默认启用设备运行时电源管理（Device runtime PM）

**说明（Help）**

默认在所有设备初始化时启用设备运行时电源管理（Device runtime PM），等效于为设备树（Devicetree）的全部节点添加 `zephyr,pm-device-runtime-auto` 属性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PM_DEVICE_RUNTIME && CONFIG_PM_DEVICE
```

**定义位置（Location）**：[`subsys/pm/Kconfig:250`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/Kconfig#L250)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 设备电源管理（Device Power Management） → 设备运行时电源管理（Runtime Device Power Management）

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE_RUNTIME`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE_RUNTIME)、[`CONFIG_PM_DEVICE`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE)。

<a id="CONFIG_PM_DEVICE_RUNTIME_USE_DEDICATED_WQ"></a>

## 411.17 `CONFIG_PM_DEVICE_RUNTIME_USE_DEDICATED_WQ`

**提示（Prompt）**：使用专用工作队列（Dedicated workqueue）

**说明（Help）**

启用后，电源管理子系统使用专用工作队列（Dedicated workqueue），而非系统工作队列（System work queue）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PM_DEVICE_RUNTIME_WQ>
```

**定义位置（Location）**：[`subsys/pm/Kconfig:221`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/Kconfig#L221)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 设备电源管理（Device Power Management） → 设备运行时电源管理（Runtime Device Power Management） → 异步设备运行时电源管理（Asynchronous device runtime power management） → 设备运行时电源管理异步操作所用工作队列（Workqueue）

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE_RUNTIME_WQ`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE_RUNTIME_WQ)。

<a id="CONFIG_PM_DEVICE_RUNTIME_USE_SYSTEM_WQ"></a>

## 411.18 `CONFIG_PM_DEVICE_RUNTIME_USE_SYSTEM_WQ`

**提示（Prompt）**：使用系统工作队列（System workqueue）

**说明（Help）**

启用后，电源管理子系统使用系统工作队列（System workqueue），不再定义自己的队列。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PM_DEVICE_RUNTIME_WQ>
```

**定义位置（Location）**：[`subsys/pm/Kconfig:215`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/Kconfig#L215)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 设备电源管理（Device Power Management） → 设备运行时电源管理（Runtime Device Power Management） → 异步设备运行时电源管理（Asynchronous device runtime power management） → 设备运行时电源管理异步操作所用工作队列（Workqueue）

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE_RUNTIME_WQ`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE_RUNTIME_WQ)。

<a id="CONFIG_PM_DEVICE_RUNTIME_WQ"></a>

## 411.19 `CONFIG_PM_DEVICE_RUNTIME_WQ`

**提示（Prompt）**：设备运行时电源管理异步操作所用工作队列（Workqueue）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PM_DEVICE_RUNTIME_ASYNC && CONFIG_PM_DEVICE_RUNTIME && CONFIG_PM_DEVICE
```

**默认值（Defaults）**

```text
CONFIG_PM_DEVICE_RUNTIME_USE_DEDICATED_WQ if CONFIG_PM_DEVICE_DRIVER_NEEDS_DEDICATED_WQ
CONFIG_PM_DEVICE_RUNTIME_USE_SYSTEM_WQ
```

**可选项（Choices）**

```text
CONFIG_PM_DEVICE_RUNTIME_USE_SYSTEM_WQ
CONFIG_PM_DEVICE_RUNTIME_USE_DEDICATED_WQ
```

**定义位置（Location）**：[`subsys/pm/Kconfig:210`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/Kconfig#L210)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 设备电源管理（Device Power Management） → 设备运行时电源管理（Runtime Device Power Management） → 异步设备运行时电源管理（Asynchronous device runtime power management）

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE_RUNTIME_ASYNC`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE_RUNTIME_ASYNC)、[`CONFIG_PM_DEVICE_RUNTIME`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE_RUNTIME)、[`CONFIG_PM_DEVICE`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE)、[`CONFIG_PM_DEVICE_RUNTIME_USE_DEDICATED_WQ`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE_RUNTIME_USE_DEDICATED_WQ)、[`CONFIG_PM_DEVICE_DRIVER_NEEDS_DEDICATED_WQ`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE_DRIVER_NEEDS_DEDICATED_WQ)、[`CONFIG_PM_DEVICE_RUNTIME_USE_SYSTEM_WQ`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE_RUNTIME_USE_SYSTEM_WQ)。

<a id="CONFIG_PM_DEVICE_SHELL"></a>

## 411.20 `CONFIG_PM_DEVICE_SHELL`

**提示（Prompt）**：设备电源管理命令行（Device Power Management shell）

**说明（Help）**

启用设备电源管理命令行（Device Power Management shell），通过命令行接口触发设备电源管理事件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_PM_DEVICE
```

**定义位置（Location）**：[`subsys/pm/Kconfig:260`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/Kconfig#L260)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 设备电源管理（Device Power Management）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_PM_DEVICE`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE)。

<a id="CONFIG_PM_DEVICE_SYSTEM_MANAGED"></a>

## 411.21 `CONFIG_PM_DEVICE_SYSTEM_MANAGED`

**提示（Prompt）**：由系统管理的设备电源管理（System-Managed Device Power Management）

**说明（Help）**

启用由系统管理的设备电源管理（System-managed device power management）。进入低功耗状态前，电源管理子系统挂起设备；内核从低功耗模式唤醒后，再恢复全部已挂起设备。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PM_DEVICE
```

**默认值（Defaults）**

```text
y if !CONFIG_PM_DEVICE_RUNTIME
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_STM32WBAX
```

**定义位置（Location）**：[`subsys/pm/Kconfig:267`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/Kconfig#L267)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 设备电源管理（Device Power Management）

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE)、[`CONFIG_PM_DEVICE_RUNTIME`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE_RUNTIME)、[`CONFIG_SOC_SERIES_STM32WBAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBAX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32WBAX`。

<a id="CONFIG_PM_EARLY_SYSTEM_TIMER_RESUME"></a>

## 411.22 `CONFIG_PM_EARLY_SYSTEM_TIMER_RESUME`

**提示（Prompt）**：先恢复系统定时器，再恢复设备［实验性，Experimental］

**说明（Help）**

采用实验性的系统恢复顺序：SoC 退出后处理（Exit post-ops）、系统定时器退出空闲（Idle-exit）、由系统管理的设备恢复，最后发送电源管理退出通知。如果低功耗状态曾停止系统定时器，此顺序允许设备恢复回调使用基于定时器的忙等待（Busy-wait）。只有验证平台恢复依赖关系后，才应启用。SoC 后处理不能依赖设备已恢复；定时器退出空闲不能依赖仍在挂起的设备。此外，定时器退出空闲可能在设备恢复前调用超时回调。禁用时保留旧顺序：先恢复由系统管理的设备，再执行 SoC 退出后处理，然后发送 PM 退出通知，最后让系统定时器退出空闲。在旧顺序下，设备恢复回调中的定时器忙等待可能无法工作。不确定是否需要时选择 `N`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PM
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/pm/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management）

**配置项引用（Symbol References）**：[`CONFIG_PM`](P411_subsys_pm_配置项参考.md#CONFIG_PM)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_PM_NEED_ALL_DEVICES_IDLE"></a>

## 411.23 `CONFIG_PM_NEED_ALL_DEVICES_IDLE`

**提示（Prompt）**：系统低功耗模式需要所有设备空闲（All devices idle）

**说明（Help）**

启用后，在进入系统低功耗模式前，检查没有设备处于忙碌（Busy）状态。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PM_DEVICE && !CONFIG_SMP && CONFIG_PM
```

**定义位置（Location）**：[`subsys/pm/Kconfig:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/Kconfig#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management）

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE`](P411_subsys_pm_配置项参考.md#CONFIG_PM_DEVICE)、[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_PM`](P411_subsys_pm_配置项参考.md#CONFIG_PM)。

<a id="CONFIG_PM_POLICY"></a>

## 411.24 `CONFIG_PM_POLICY`

**提示（Prompt）**：空闲状态电源管理策略（Idle State Power Management Policy）

**说明（Help）**

选择空闲状态（Idle state）的电源管理策略（Power management policy）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PM
```

**默认值（Defaults）**

```text
CONFIG_PM_POLICY_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_PM_POLICY_DEFAULT
CONFIG_PM_POLICY_CUSTOM
```

**定义位置（Location）**：[`subsys/pm/policy/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/policy/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management）

**配置项引用（Symbol References）**：[`CONFIG_PM`](P411_subsys_pm_配置项参考.md#CONFIG_PM)、[`CONFIG_PM_POLICY_DEFAULT`](P411_subsys_pm_配置项参考.md#CONFIG_PM_POLICY_DEFAULT)、[`CONFIG_PM_POLICY_CUSTOM`](P411_subsys_pm_配置项参考.md#CONFIG_PM_POLICY_CUSTOM)。

<a id="CONFIG_PM_POLICY_CUSTOM"></a>

## 411.25 `CONFIG_PM_POLICY_CUSTOM`

**提示（Prompt）**：自定义电源管理策略（Custom PM Policy）

**说明（Help）**

允许应用使用自定义实现覆盖默认电源管理策略（PM policy）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PM_POLICY>
```

**定义位置（Location）**：[`subsys/pm/policy/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/policy/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 空闲状态电源管理策略（Idle State Power Management Policy）

**配置项引用（Symbol References）**：[`CONFIG_PM_POLICY`](P411_subsys_pm_配置项参考.md#CONFIG_PM_POLICY)。

<a id="CONFIG_PM_POLICY_DEFAULT"></a>

## 411.26 `CONFIG_PM_POLICY_DEFAULT`

**提示（Prompt）**：默认电源管理策略（Default PM policy）

**说明（Help）**

选择默认电源管理策略（PM policy）。默认策略基于 CPU 在各状态的驻留时间（Residency time），以及驱动或应用施加的其他约束。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PM_POLICY>
```

**定义位置（Location）**：[`subsys/pm/policy/Kconfig:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/policy/Kconfig#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 空闲状态电源管理策略（Idle State Power Management Policy）

**配置项引用（Symbol References）**：[`CONFIG_PM_POLICY`](P411_subsys_pm_配置项参考.md#CONFIG_PM_POLICY)。

<a id="CONFIG_PM_POLICY_DEVICE_CONSTRAINTS"></a>

## 411.27 `CONFIG_PM_POLICY_DEVICE_CONSTRAINTS`

**提示（Prompt）**：各设备的电源状态约束（Power state constraints）

**说明（Help）**

允许设备列出一组电源状态（Power state）：系统转换到这些状态时，该设备会失去供电。设备需要时，可据此设置和释放电源状态约束（Constraint）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PM
```

**被选择（Selected by）**

```text
CONFIG_UART_MCUX_FLEXCOMM
```

**定义位置（Location）**：[`subsys/pm/policy/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/policy/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management）

**配置项引用（Symbol References）**：[`CONFIG_PM`](P411_subsys_pm_配置项参考.md#CONFIG_PM)、[`CONFIG_UART_MCUX_FLEXCOMM`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_MCUX_FLEXCOMM)。

<a id="CONFIG_PM_POLICY_LATENCY_STANDALONE"></a>

## 411.28 `CONFIG_PM_POLICY_LATENCY_STANDALONE`

**提示（Prompt）**：允许独立收集延迟要求（Latency requirements）

**说明（Help）**

允许在不支持电源管理（PM）的系统中，例如没有 CPU 空闲状态的系统，使用 `pm_policy_latency*` API 收集延迟要求（Latency requirements）。该 API 提供订阅机制（Subscription mechanism），因此可根据多个系统组件提出的延迟要求，进行系统级调整。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_PM
```

**定义位置（Location）**：[`subsys/pm/policy/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/policy/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management）

**配置项引用（Symbol References）**：[`CONFIG_PM`](P411_subsys_pm_配置项参考.md#CONFIG_PM)。

<a id="CONFIG_PM_PREWAKEUP_CONV_MODE"></a>

## 411.29 `CONFIG_PM_PREWAKEUP_CONV_MODE`

**提示（Prompt）**：提前唤醒的微秒到时钟节拍转换方式（Microseconds-to-ticks conversion）

**说明（Help）**

各电源状态的退出延迟（Exit latency）以微秒表示，需要转换为时钟节拍（Tick），并据此设置系统时钟，让内核在计划唤醒时间之前提前醒来。本选项指定将退出延迟从微秒转换为系统节拍时使用的舍入方式（Rounding）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PM
```

**默认值（Defaults）**

```text
CONFIG_PM_PREWAKEUP_CONV_MODE_NEAR
```

**可选项（Choices）**

```text
CONFIG_PM_PREWAKEUP_CONV_MODE_NEAR
CONFIG_PM_PREWAKEUP_CONV_MODE_CEIL
CONFIG_PM_PREWAKEUP_CONV_MODE_FLOOR
```

**定义位置（Location）**：[`subsys/pm/Kconfig:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/Kconfig#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management）

**配置项引用（Symbol References）**：[`CONFIG_PM`](P411_subsys_pm_配置项参考.md#CONFIG_PM)、[`CONFIG_PM_PREWAKEUP_CONV_MODE_NEAR`](P411_subsys_pm_配置项参考.md#CONFIG_PM_PREWAKEUP_CONV_MODE_NEAR)、[`CONFIG_PM_PREWAKEUP_CONV_MODE_CEIL`](P411_subsys_pm_配置项参考.md#CONFIG_PM_PREWAKEUP_CONV_MODE_CEIL)、[`CONFIG_PM_PREWAKEUP_CONV_MODE_FLOOR`](P411_subsys_pm_配置项参考.md#CONFIG_PM_PREWAKEUP_CONV_MODE_FLOOR)。

<a id="CONFIG_PM_PREWAKEUP_CONV_MODE_CEIL"></a>

## 411.30 `CONFIG_PM_PREWAKEUP_CONV_MODE_CEIL`

**提示（Prompt）**：向上取整（Round up）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PM_PREWAKEUP_CONV_MODE>
```

**定义位置（Location）**：[`subsys/pm/Kconfig:136`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/Kconfig#L136)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 提前唤醒的微秒到时钟节拍转换方式（Microseconds-to-ticks conversion）

**配置项引用（Symbol References）**：[`CONFIG_PM_PREWAKEUP_CONV_MODE`](P411_subsys_pm_配置项参考.md#CONFIG_PM_PREWAKEUP_CONV_MODE)。

<a id="CONFIG_PM_PREWAKEUP_CONV_MODE_FLOOR"></a>

## 411.31 `CONFIG_PM_PREWAKEUP_CONV_MODE_FLOOR`

**提示（Prompt）**：向下取整（Round down）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PM_PREWAKEUP_CONV_MODE>
```

**定义位置（Location）**：[`subsys/pm/Kconfig:139`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/Kconfig#L139)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 提前唤醒的微秒到时钟节拍转换方式（Microseconds-to-ticks conversion）

**配置项引用（Symbol References）**：[`CONFIG_PM_PREWAKEUP_CONV_MODE`](P411_subsys_pm_配置项参考.md#CONFIG_PM_PREWAKEUP_CONV_MODE)。

<a id="CONFIG_PM_PREWAKEUP_CONV_MODE_NEAR"></a>

## 411.32 `CONFIG_PM_PREWAKEUP_CONV_MODE_NEAR`

**提示（Prompt）**：取最近整数（Nearest）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PM_PREWAKEUP_CONV_MODE>
```

**定义位置（Location）**：[`subsys/pm/Kconfig:133`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/Kconfig#L133)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 提前唤醒的微秒到时钟节拍转换方式（Microseconds-to-ticks conversion）

**配置项引用（Symbol References）**：[`CONFIG_PM_PREWAKEUP_CONV_MODE`](P411_subsys_pm_配置项参考.md#CONFIG_PM_PREWAKEUP_CONV_MODE)。

<a id="CONFIG_PM_S2RAM"></a>

## 411.33 `CONFIG_PM_S2RAM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

当启用电源管理（PM），且设备树（Devicetree）启用了一个或多个挂起到 RAM（Suspend-to-RAM，S2RAM）睡眠状态时，本选项启用 SoC 专用的 S2RAM 实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/pm/Kconfig:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/Kconfig#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management）

<a id="CONFIG_PM_STATE_SET_IRQ_UNLOCKED"></a>

## 411.34 `CONFIG_PM_STATE_SET_IRQ_UNLOCKED`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果 SoC 电源管理（PM）状态实现在 `pm_system_suspend()` 期间，仍会从 `pm_state_set()` 或 `pm_state_exit_post_ops()` 解锁中断或以其他方式解除中断屏蔽，应选择此项。它为尚未迁移到由空闲路径负责恢复中断（Idle-owned IRQ restore）的平台保留旧的 PM 钩子行为。如果平台在整个 `pm_state_set()` 和 `pm_state_exit_post_ops()` 期间始终保持中断锁定，则不应选择。此选项用于支持渐进迁移；源码树中所有 SoC PM 实现迁移后，将移除该兼容选项。上述保证仅涵盖 `arch_irq_lock()` 能屏蔽的中断；`IRQ_ZERO_LATENCY` 的行为请参见零延迟中断（Zero-latency interrupt）文档。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_KB106X
CONFIG_SOC_SERIES_PSOC4100TP
CONFIG_SOC_FAMILY_CH32V
CONFIG_SOC_FAMILY_MICROCHIP_MEC
CONFIG_SOC_SERIES_RA8D1
CONFIG_SOC_SERIES_RA8D2
CONFIG_SOC_SERIES_RA8E1
CONFIG_SOC_SERIES_RA8M1
CONFIG_SOC_SERIES_RA8M2
CONFIG_SOC_SERIES_RA8P1
CONFIG_SOC_SERIES_RA8T1
CONFIG_SOC_SERIES_RA8T2
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
CONFIG_SOC_FAMILY_SILABS_S0
CONFIG_SOC_FAMILY_SILABS_S1
CONFIG_SOC_FAMILY_SILABS_S2
CONFIG_SOC_FAMILY_SILABS_S3
CONFIG_SOC_FAMILY_SILABS_SIWX91X
CONFIG_SOC_SERIES_IMXRT10XX
CONFIG_SOC_NRF54H20_CPUAPP_COMMON
CONFIG_SOC_NRF54H20_CPURAD_COMMON
CONFIG_SOC_NRF9230_ENGB_CPUAPP
CONFIG_SOC_NRF9230_ENGB_CPURAD
CONFIG_SOC_MIMX94398_M33
CONFIG_SOC_MIMX94398_M7_0
CONFIG_SOC_MIMX94398_M7_1
CONFIG_SOC_SERIES_PSE84
CONFIG_SOC_SERIES_CYW20829
CONFIG_SOC_SERIES_PSC3
CONFIG_SOC_SERIES_CC13X2_CC26X2
CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7
CONFIG_SOC_SERIES_CC23X0
CONFIG_SOC_SERIES_IT51XXX
CONFIG_SOC_SERIES_IT8XXX2
CONFIG_SOC_SERIES_APOLLO3X
CONFIG_SOC_SERIES_APOLLO4X
CONFIG_SOC_SERIES_APOLLO5X
CONFIG_SOC_SERIES_DA1469X
CONFIG_SOC_SERIES_INTEL_ADSP_ACE
CONFIG_SOC_SERIES_INTEL_ADSP_CAVS
CONFIG_SOC_FAMILY_INTEL_ISH
CONFIG_SOC_FAMILY_MAX32_M33
CONFIG_SOC_FAMILY_MAX32_M4
CONFIG_SOC_SERIES_MSPM0G
CONFIG_SOC_SERIES_MSPM0L
CONFIG_SOC_SERIES_RTS5912
CONFIG_SOC_SERIES_STM32C0X
CONFIG_SOC_SERIES_STM32F1X
CONFIG_SOC_SERIES_STM32F4X
CONFIG_SOC_SERIES_STM32G0X
CONFIG_SOC_SERIES_STM32G4X
CONFIG_SOC_SERIES_STM32H5X
CONFIG_SOC_SERIES_STM32L0X
CONFIG_SOC_SERIES_STM32L1X
CONFIG_SOC_SERIES_STM32L4X
CONFIG_SOC_SERIES_STM32L5X
CONFIG_SOC_SERIES_STM32U0X
CONFIG_SOC_SERIES_STM32U5X
CONFIG_SOC_SERIES_STM32WB0X
CONFIG_SOC_SERIES_STM32WBAX
CONFIG_SOC_SERIES_STM32WBX
CONFIG_SOC_SERIES_STM32WLX
CONFIG_SOC_SERIES_NPCK3
CONFIG_SOC_SERIES_NPCX4
CONFIG_SOC_SERIES_NPCX7
CONFIG_SOC_SERIES_NPCX9
CONFIG_SOC_SERIES_RW6XX
```

**定义位置（Location）**：[`subsys/pm/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_KB106X`](P274_soc_ene_配置项参考.md#CONFIG_SOC_SERIES_KB106X)、[`CONFIG_SOC_SERIES_PSOC4100TP`](P280_soc_infineon_配置项参考.md#CONFIG_SOC_SERIES_PSOC4100TP)、[`CONFIG_SOC_FAMILY_CH32V`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_CH32V)、[`CONFIG_SOC_FAMILY_MICROCHIP_MEC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_MEC)、[`CONFIG_SOC_SERIES_RA8D1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8D1)、[`CONFIG_SOC_SERIES_RA8D2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8D2)、[`CONFIG_SOC_SERIES_RA8E1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8E1)、[`CONFIG_SOC_SERIES_RA8M1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8M1)、[`CONFIG_SOC_SERIES_RA8M2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8M2)、[`CONFIG_SOC_SERIES_RA8P1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8P1)、[`CONFIG_SOC_SERIES_RA8T1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8T1)、[`CONFIG_SOC_SERIES_RA8T2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8T2)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_SOC_FAMILY_SILABS_S0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S0)、[`CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S1)、[`CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2)、[`CONFIG_SOC_FAMILY_SILABS_S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S3)、[`CONFIG_SOC_FAMILY_SILABS_SIWX91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_SIWX91X)、[`CONFIG_SOC_SERIES_IMXRT10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT10XX)、[`CONFIG_SOC_NRF54H20_CPUAPP_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPUAPP_COMMON)、[`CONFIG_SOC_NRF54H20_CPURAD_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPURAD_COMMON)、[`CONFIG_SOC_NRF9230_ENGB_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9230_ENGB_CPUAPP)、[`CONFIG_SOC_NRF9230_ENGB_CPURAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9230_ENGB_CPURAD)、[`CONFIG_SOC_MIMX94398_M33`](P294_soc_nxp_配置项参考_2.md#CONFIG_SOC_MIMX94398_M33)、[`CONFIG_SOC_MIMX94398_M7_0`](P294_soc_nxp_配置项参考_2.md#CONFIG_SOC_MIMX94398_M7_0)、[`CONFIG_SOC_MIMX94398_M7_1`](P294_soc_nxp_配置项参考_2.md#CONFIG_SOC_MIMX94398_M7_1)、[`CONFIG_SOC_SERIES_PSE84`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSE84)、[`CONFIG_SOC_SERIES_CYW20829`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CYW20829)、[`CONFIG_SOC_SERIES_PSC3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSC3)、[`CONFIG_SOC_SERIES_CC13X2_CC26X2`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC13X2_CC26X2)、[`CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7)、[`CONFIG_SOC_SERIES_CC23X0`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_CC23X0)、[`CONFIG_SOC_SERIES_IT51XXX`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT51XXX)、[`CONFIG_SOC_SERIES_IT8XXX2`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT8XXX2)、[`CONFIG_SOC_SERIES_APOLLO3X`](P260_soc_ambiq_配置项参考.md#CONFIG_SOC_SERIES_APOLLO3X)、[`CONFIG_SOC_SERIES_APOLLO4X`](P260_soc_ambiq_配置项参考.md#CONFIG_SOC_SERIES_APOLLO4X)、[`CONFIG_SOC_SERIES_APOLLO5X`](P260_soc_ambiq_配置项参考.md#CONFIG_SOC_SERIES_APOLLO5X)、[`CONFIG_SOC_SERIES_DA1469X`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_DA1469X)、[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE`](P281_soc_intel_配置项参考.md#CONFIG_SOC_SERIES_INTEL_ADSP_ACE)、[`CONFIG_SOC_SERIES_INTEL_ADSP_CAVS`](P281_soc_intel_配置项参考.md#CONFIG_SOC_SERIES_INTEL_ADSP_CAVS)、[`CONFIG_SOC_FAMILY_INTEL_ISH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ISH)、[`CONFIG_SOC_FAMILY_MAX32_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_M33)、[`CONFIG_SOC_FAMILY_MAX32_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_M4)、[`CONFIG_SOC_SERIES_MSPM0G`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_MSPM0G)、[`CONFIG_SOC_SERIES_MSPM0L`](P314_soc_ti_配置项参考.md#CONFIG_SOC_SERIES_MSPM0L)、[`CONFIG_SOC_SERIES_RTS5912`](P301_soc_realtek_配置项参考.md#CONFIG_SOC_SERIES_RTS5912)、[`CONFIG_SOC_SERIES_STM32C0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32C0X)、[`CONFIG_SOC_SERIES_STM32F1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F1X)、[`CONFIG_SOC_SERIES_STM32F4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F4X)、[`CONFIG_SOC_SERIES_STM32G0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32G0X)、[`CONFIG_SOC_SERIES_STM32G4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32G4X)、[`CONFIG_SOC_SERIES_STM32H5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H5X)、[`CONFIG_SOC_SERIES_STM32L0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L0X)、[`CONFIG_SOC_SERIES_STM32L1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L1X)、[`CONFIG_SOC_SERIES_STM32L4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L4X)、[`CONFIG_SOC_SERIES_STM32L5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L5X)、[`CONFIG_SOC_SERIES_STM32U0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U0X)、[`CONFIG_SOC_SERIES_STM32U5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U5X)、[`CONFIG_SOC_SERIES_STM32WB0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WB0X)、[`CONFIG_SOC_SERIES_STM32WBAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBAX)、[`CONFIG_SOC_SERIES_STM32WBX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBX)、[`CONFIG_SOC_SERIES_STM32WLX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WLX)、[`CONFIG_SOC_SERIES_NPCK3`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_SERIES_NPCK3)、[`CONFIG_SOC_SERIES_NPCX4`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_SERIES_NPCX4)、[`CONFIG_SOC_SERIES_NPCX7`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_SERIES_NPCX7)、[`CONFIG_SOC_SERIES_NPCX9`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_SERIES_NPCX9)、[`CONFIG_SOC_SERIES_RW6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RW6XX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_CH32V`、`CONFIG_SOC_FAMILY_MICROCHIP_MEC`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`、`CONFIG_SOC_FAMILY_SILABS_S0`、`CONFIG_SOC_FAMILY_SILABS_S1`、`CONFIG_SOC_FAMILY_SILABS_S2`、`CONFIG_SOC_FAMILY_SILABS_S3`、`CONFIG_SOC_FAMILY_SILABS_SIWX91X`、`CONFIG_SOC_SERIES_IMXRT10XX`、`CONFIG_SOC_NRF54H20_CPUAPP_COMMON`、`CONFIG_SOC_NRF54H20_CPURAD_COMMON`、`CONFIG_SOC_NRF9230_ENGB_CPUAPP`、`CONFIG_SOC_NRF9230_ENGB_CPURAD`、`CONFIG_SOC_SERIES_PSE84`、`CONFIG_SOC_SERIES_CYW20829`、`CONFIG_SOC_SERIES_PSC3`、`CONFIG_SOC_FAMILY_INTEL_ISH`、`CONFIG_SOC_FAMILY_MAX32_M33`、`CONFIG_SOC_FAMILY_MAX32_M4`、`CONFIG_SOC_SERIES_STM32C0X`、`CONFIG_SOC_SERIES_STM32F1X`、`CONFIG_SOC_SERIES_STM32F4X`、`CONFIG_SOC_SERIES_STM32G0X`、`CONFIG_SOC_SERIES_STM32G4X`、`CONFIG_SOC_SERIES_STM32H5X`、`CONFIG_SOC_SERIES_STM32L0X`、`CONFIG_SOC_SERIES_STM32L1X`、`CONFIG_SOC_SERIES_STM32L4X`、`CONFIG_SOC_SERIES_STM32L5X`、`CONFIG_SOC_SERIES_STM32U0X`、`CONFIG_SOC_SERIES_STM32U5X`、`CONFIG_SOC_SERIES_STM32WB0X`、`CONFIG_SOC_SERIES_STM32WBAX`、`CONFIG_SOC_SERIES_STM32WBX`、`CONFIG_SOC_SERIES_STM32WLX`、`CONFIG_SOC_SERIES_RW6XX`。

<a id="CONFIG_PM_STATS"></a>

## 411.35 `CONFIG_PM_STATS`

**提示（Prompt）**：系统电源管理统计（System Power Management Stats）

**说明（Help）**

启用系统电源管理统计（System Power Management Stats）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STATS && CONFIG_PM
```

**定义位置（Location）**：[`subsys/pm/Kconfig:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pm/Kconfig#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management）

**配置项引用（Symbol References）**：[`CONFIG_STATS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STATS)、[`CONFIG_PM`](P411_subsys_pm_配置项参考.md#CONFIG_PM)。

<!-- kconfig-navigation -->

[上一章](P410_subsys_nvmem_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P412_subsys_pmci_配置项参考.md)
