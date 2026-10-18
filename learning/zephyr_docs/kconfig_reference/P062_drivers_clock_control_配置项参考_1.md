---
id: learning.zephyr-docs.kconfig-reference.page-62
title: "`drivers/clock_control`配置项参考（1/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第62章\_`drivers/clock_control`配置项参考（1/2）

本章翻译官方 Kconfig 数据库中 `drivers/clock_control` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_CLOCK_CONTROL"></a>

## 62.1 `CONFIG_CLOCK_CONTROL`

**提示（Prompt）**：时钟控制器驱动（Clock Controller Drivers）

**说明（Help）**

启用硬件时钟控制器（Hardware Clock Controller）支持。此类硬件可为其他子系统提供时钟，因此也可通过控制这些子系统的时钟提高能效（Power Efficiency）。注意，这与实时时钟（RTC）无关。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_NRF_802154_RADIO_DRIVER
CONFIG_NRF_802154_RADIO_DRIVER
CONFIG_SOC_SERIES_BL60X
CONFIG_SOC_SERIES_BL616CL
CONFIG_SOC_SERIES_BL61X
CONFIG_SOC_SERIES_BL70X
CONFIG_SOC_SERIES_BL70XL
CONFIG_SOC_SERIES_BL808
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC
CONFIG_SOC_FAMILY_LPC
CONFIG_SOC_SERIES_LPC11U6X
CONFIG_SOC_LPC51U68
CONFIG_SOC_LPC54114_M4
CONFIG_SOC_LPC54114_M0
CONFIG_SOC_LPC54628
CONFIG_SOC_SERIES_LPC84X
CONFIG_SOC_SR100
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
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC
CONFIG_SOC_FAMILY_MCXA
CONFIG_SOC_FAMILY_MCXC
CONFIG_SOC_SERIES_MCXE24X
CONFIG_SOC_SERIES_MCXE31X
CONFIG_SOC_FAMILY_MCXL
CONFIG_SOC_FAMILY_MCXN
CONFIG_SOC_FAMILY_MCXW
CONFIG_SOC_SERIES_SIM3U
CONFIG_SOC_SERIES_IMXRT10XX
CONFIG_SOC_SERIES_IMXRT118X
CONFIG_SOC_SERIES_IMXRT11XX
CONFIG_SOC_SERIES_IMXRT266X
CONFIG_SOC_MIMXRT595S_CM33
CONFIG_SOC_MIMXRT685S_CM33
CONFIG_SOC_MIMXRT685S_HIFI4
CONFIG_SOC_MIMXRT798S_CM33_CPU0
CONFIG_SOC_MIMXRT798S_CM33_CPU1
CONFIG_SOC_MIMXRT758S_CM33_CPU0
CONFIG_SOC_MIMXRT758S_CM33_CPU1
CONFIG_SOC_MIMXRT735S_CM33_CPU0
CONFIG_SOC_MIMXRT735S_CM33_CPU1
CONFIG_SOC_MIMXRT798S_HIFI4
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA
CONFIG_SOC_SERIES_K2X
CONFIG_SOC_SERIES_K32LX
CONFIG_SOC_SERIES_K6X
CONFIG_SOC_SERIES_K8X
CONFIG_SOC_SERIES_KE1XF
CONFIG_SOC_SERIES_KE1XZ
CONFIG_SOC_SERIES_KL2X
CONFIG_SOC_SERIES_KV5X
CONFIG_SOC_SERIES_KWX
CONFIG_SOC_SERIES_AMEBAD
CONFIG_SOC_SERIES_AMEBADPLUS
CONFIG_SOC_SERIES_AMEBAG2
CONFIG_SOC_SERIES_IMX6SX
CONFIG_SOC_SERIES_IMX7D
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG
CONFIG_SOC_SERIES_HYDROGEN
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH
CONFIG_SOC_SERIES_NPCM4
CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X
CONFIG_SOC_SERIES_DA1469X
CONFIG_SOC_SERIES_RX130
CONFIG_SOC_SERIES_RX140
CONFIG_SOC_SERIES_RX14T
CONFIG_SOC_SERIES_RX261
CONFIG_SOC_SERIES_RX26T
CONFIG_SOC_SERIES_RX62N
CONFIG_SOC_SERIES_RX74M
CONFIG_SOC_SERIES_RX74N
CONFIG_SOC_OPENISA_RV32M1
CONFIG_SOC_AMD_VERSALNET_RPU
CONFIG_SOC_AMD_VERSALNET_APU
CONFIG_SOC_SERIES_RTL8752H
CONFIG_SOC_SERIES_RTL87X2G
CONFIG_SOC_FAMILY_MAX32_M33
CONFIG_SOC_FAMILY_MAX32_M4
CONFIG_SOC_FAMILY_MAX32_RV32
CONFIG_SOC_SERIES_MSPM0G
CONFIG_SOC_SERIES_MSPM0L
CONFIG_SOC_AMD_VERSAL2_RPU
CONFIG_SOC_AMD_VERSAL2_APU
CONFIG_SOC_SERIES_M48X
CONFIG_SOC_SERIES_RW6XX
CONFIG_SOC_SERIES_S32K1
CONFIG_SOC_SERIES_S32K3
CONFIG_SOC_SERIES_S32ZE
CONFIG_AUDIO_DMIC_NXP_MICFIL
CONFIG_BT_AMBIQ_HCI
CONFIG_CAN_NRF
CONFIG_CAN_NXP_S32_CANXL
CONFIG_CAN_RENESAS_RZ_CANFD
CONFIG_COMPARATOR_NXP_CMP
CONFIG_COMPARATOR_NXP_HSCMP
CONFIG_COMPARATOR_NXP_LPACMP
CONFIG_COMPARATOR_NXP_LPCMP
CONFIG_COUNTER_NRFX_TIMER_USE_CLOCK_CONTROL
CONFIG_COUNTER_NXP_S32_SYS_TIMER
CONFIG_COUNTER_SMARTBOND_TIMER
CONFIG_ETH_XMC_DWC_ETHER_1000
CONFIG_ETH_NUMAKER_DWC_ETHER_1000
CONFIG_ETH_ROCKCHIP_DWC_ETHER_QOS
CONFIG_MDIO_NXP_S32_GMAC
CONFIG_I2S_NRF_TDM
CONFIG_OPAMP_MCUX_OPAMP
CONFIG_OPAMP_MCUX_OPAMP_FAST
CONFIG_XLNX_SDHC
CONFIG_UART_FOCALTECH
CONFIG_UART_RTS5912
CONFIG_UART_SF32LB
CONFIG_UART_SILABS_EUSART
CONFIG_UART_SILABS_USART
CONFIG_USB_DC_SMARTBOND
CONFIG_WDT_CRSAS_MA2
CONFIG_WDT_NXP_S32
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_RADIO_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF_802154_RADIO_DRIVER)、[`CONFIG_SOC_SERIES_BL60X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL60X)、[`CONFIG_SOC_SERIES_BL616CL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL616CL)、[`CONFIG_SOC_SERIES_BL61X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL61X)、[`CONFIG_SOC_SERIES_BL70X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70X)、[`CONFIG_SOC_SERIES_BL70XL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70XL)、[`CONFIG_SOC_SERIES_BL808`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL808)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC)、[`CONFIG_SOC_FAMILY_LPC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_LPC)、[`CONFIG_SOC_SERIES_LPC11U6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC11U6X)、[`CONFIG_SOC_LPC51U68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC51U68)、[`CONFIG_SOC_LPC54114_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC54114_M4)、[`CONFIG_SOC_LPC54114_M0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC54114_M0)、[`CONFIG_SOC_LPC54628`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC54628)、[`CONFIG_SOC_SERIES_LPC84X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC84X)、[`CONFIG_SOC_SR100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SR100)、[`CONFIG_SOC_SERIES_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C3)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_SERIES_ESP32S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC)、[`CONFIG_SOC_FAMILY_MCXA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXA)、[`CONFIG_SOC_FAMILY_MCXC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXC)、[`CONFIG_SOC_SERIES_MCXE24X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE24X)、[`CONFIG_SOC_SERIES_MCXE31X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE31X)、[`CONFIG_SOC_FAMILY_MCXL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXL)、[`CONFIG_SOC_FAMILY_MCXN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXN)、[`CONFIG_SOC_FAMILY_MCXW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXW)、[`CONFIG_SOC_SERIES_SIM3U`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SIM3U)、[`CONFIG_SOC_SERIES_IMXRT10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT10XX)、[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_SERIES_IMXRT266X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT266X)、[`CONFIG_SOC_MIMXRT595S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT595S_CM33)、[`CONFIG_SOC_MIMXRT685S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_CM33)、[`CONFIG_SOC_MIMXRT685S_HIFI4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_HIFI4)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU1)、[`CONFIG_SOC_MIMXRT758S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT758S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_CM33_CPU1)、[`CONFIG_SOC_MIMXRT735S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT735S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_CM33_CPU1)、[`CONFIG_SOC_MIMXRT798S_HIFI4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_HIFI4)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA)、[`CONFIG_SOC_SERIES_K2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K2X)、[`CONFIG_SOC_SERIES_K32LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K32LX)、[`CONFIG_SOC_SERIES_K6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K6X)、[`CONFIG_SOC_SERIES_K8X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K8X)、[`CONFIG_SOC_SERIES_KE1XF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KE1XF)、[`CONFIG_SOC_SERIES_KE1XZ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KE1XZ)、[`CONFIG_SOC_SERIES_KL2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KL2X)、[`CONFIG_SOC_SERIES_KV5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KV5X)、[`CONFIG_SOC_SERIES_KWX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KWX)、[`CONFIG_SOC_SERIES_AMEBAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAD)、[`CONFIG_SOC_SERIES_AMEBADPLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBADPLUS)、[`CONFIG_SOC_SERIES_AMEBAG2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAG2)、[`CONFIG_SOC_SERIES_IMX6SX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMX6SX)、[`CONFIG_SOC_SERIES_IMX7D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMX7D)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG)、[`CONFIG_SOC_SERIES_HYDROGEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_HYDROGEN)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH)、[`CONFIG_SOC_SERIES_NPCM4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCM4)、[`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X)、[`CONFIG_SOC_SERIES_DA1469X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_DA1469X)、[`CONFIG_SOC_SERIES_RX130`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX130)、[`CONFIG_SOC_SERIES_RX140`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX140)、[`CONFIG_SOC_SERIES_RX14T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX14T)、[`CONFIG_SOC_SERIES_RX261`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX261)、[`CONFIG_SOC_SERIES_RX26T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX26T)、[`CONFIG_SOC_SERIES_RX62N`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX62N)、[`CONFIG_SOC_SERIES_RX74M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX74M)、[`CONFIG_SOC_SERIES_RX74N`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX74N)、[`CONFIG_SOC_OPENISA_RV32M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_OPENISA_RV32M1)、[`CONFIG_SOC_AMD_VERSALNET_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSALNET_RPU)、[`CONFIG_SOC_AMD_VERSALNET_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSALNET_APU)、[`CONFIG_SOC_SERIES_RTL8752H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTL8752H)、[`CONFIG_SOC_SERIES_RTL87X2G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTL87X2G)、[`CONFIG_SOC_FAMILY_MAX32_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_M33)、[`CONFIG_SOC_FAMILY_MAX32_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_M4)、[`CONFIG_SOC_FAMILY_MAX32_RV32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_RV32)、[`CONFIG_SOC_SERIES_MSPM0G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSPM0G)、[`CONFIG_SOC_SERIES_MSPM0L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSPM0L)、[`CONFIG_SOC_AMD_VERSAL2_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSAL2_RPU)、[`CONFIG_SOC_AMD_VERSAL2_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSAL2_APU)、[`CONFIG_SOC_SERIES_M48X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M48X)、[`CONFIG_SOC_SERIES_RW6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RW6XX)、[`CONFIG_SOC_SERIES_S32K1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K1)、[`CONFIG_SOC_SERIES_S32K3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K3)、[`CONFIG_SOC_SERIES_S32ZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32ZE)、[`CONFIG_AUDIO_DMIC_NXP_MICFIL`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_NXP_MICFIL)、[`CONFIG_BT_AMBIQ_HCI`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_AMBIQ_HCI)、[`CONFIG_CAN_NRF`](P060_drivers_can_配置项参考.md#CONFIG_CAN_NRF)、[`CONFIG_CAN_NXP_S32_CANXL`](P060_drivers_can_配置项参考.md#CONFIG_CAN_NXP_S32_CANXL)、[`CONFIG_CAN_RENESAS_RZ_CANFD`](P060_drivers_can_配置项参考.md#CONFIG_CAN_RENESAS_RZ_CANFD)、[`CONFIG_COMPARATOR_NXP_CMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COMPARATOR_NXP_CMP)、[`CONFIG_COMPARATOR_NXP_HSCMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COMPARATOR_NXP_HSCMP)、[`CONFIG_COMPARATOR_NXP_LPACMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COMPARATOR_NXP_LPACMP)、[`CONFIG_COMPARATOR_NXP_LPCMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COMPARATOR_NXP_LPCMP)、[`CONFIG_COUNTER_NRFX_TIMER_USE_CLOCK_CONTROL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COUNTER_NRFX_TIMER_USE_CLOCK_CONTROL)、[`CONFIG_COUNTER_NXP_S32_SYS_TIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COUNTER_NXP_S32_SYS_TIMER)、[`CONFIG_COUNTER_SMARTBOND_TIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COUNTER_SMARTBOND_TIMER)、[`CONFIG_ETH_XMC_DWC_ETHER_1000`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_XMC_DWC_ETHER_1000)、[`CONFIG_ETH_NUMAKER_DWC_ETHER_1000`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_NUMAKER_DWC_ETHER_1000)、[`CONFIG_ETH_ROCKCHIP_DWC_ETHER_QOS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_ROCKCHIP_DWC_ETHER_QOS)、[`CONFIG_MDIO_NXP_S32_GMAC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MDIO_NXP_S32_GMAC)、[`CONFIG_I2S_NRF_TDM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2S_NRF_TDM)、[`CONFIG_OPAMP_MCUX_OPAMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPAMP_MCUX_OPAMP)、[`CONFIG_OPAMP_MCUX_OPAMP_FAST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPAMP_MCUX_OPAMP_FAST)、[`CONFIG_XLNX_SDHC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XLNX_SDHC)、[`CONFIG_UART_FOCALTECH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_FOCALTECH)、[`CONFIG_UART_RTS5912`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RTS5912)、[`CONFIG_UART_SF32LB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SF32LB)、[`CONFIG_UART_SILABS_EUSART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SILABS_EUSART)、[`CONFIG_UART_SILABS_USART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SILABS_USART)、[`CONFIG_USB_DC_SMARTBOND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DC_SMARTBOND)、[`CONFIG_WDT_CRSAS_MA2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WDT_CRSAS_MA2)、[`CONFIG_WDT_NXP_S32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WDT_NXP_S32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`、`CONFIG_SOC_FAMILY_LPC`、`CONFIG_SOC_SERIES_LPC11U6X`、`CONFIG_SOC_LPC51U68`、`CONFIG_SOC_LPC54114_M4`、`CONFIG_SOC_LPC54114_M0`、`CONFIG_SOC_LPC54628`、`CONFIG_SOC_SERIES_LPC84X`、`CONFIG_SOC_SR100`、`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32H2`、`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC`、`CONFIG_SOC_FAMILY_MCXA`、`CONFIG_SOC_FAMILY_MCXC`、`CONFIG_SOC_SERIES_MCXE24X`、`CONFIG_SOC_SERIES_MCXE31X`、`CONFIG_SOC_FAMILY_MCXL`、`CONFIG_SOC_FAMILY_MCXN`、`CONFIG_SOC_FAMILY_MCXW`、`CONFIG_SOC_SERIES_IMXRT10XX`、`CONFIG_SOC_SERIES_IMXRT118X`、`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_SERIES_IMXRT266X`、`CONFIG_SOC_MIMXRT685S_CM33`、`CONFIG_SOC_MIMXRT685S_HIFI4`、`CONFIG_SOC_MIMXRT798S_CM33_CPU0`、`CONFIG_SOC_MIMXRT798S_CM33_CPU1`、`CONFIG_SOC_MIMXRT758S_CM33_CPU0`、`CONFIG_SOC_MIMXRT758S_CM33_CPU1`、`CONFIG_SOC_MIMXRT735S_CM33_CPU0`、`CONFIG_SOC_MIMXRT735S_CM33_CPU1`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`、`CONFIG_SOC_SERIES_K2X`、`CONFIG_SOC_SERIES_K32LX`、`CONFIG_SOC_SERIES_K6X`、`CONFIG_SOC_SERIES_K8X`、`CONFIG_SOC_SERIES_KE1XF`、`CONFIG_SOC_SERIES_KE1XZ`、`CONFIG_SOC_SERIES_KL2X`、`CONFIG_SOC_SERIES_KV5X`、`CONFIG_SOC_SERIES_KWX`、`CONFIG_SOC_SERIES_AMEBAD`、`CONFIG_SOC_SERIES_AMEBADPLUS`、`CONFIG_SOC_SERIES_AMEBAG2`、`CONFIG_SOC_SERIES_IMX6SX`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG`、`CONFIG_SOC_SERIES_HYDROGEN`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`、`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`、`CONFIG_SOC_FAMILY_MAX32_M33`、`CONFIG_SOC_FAMILY_MAX32_M4`、`CONFIG_SOC_FAMILY_MAX32_RV32`、`CONFIG_SOC_SERIES_RW6XX`、`CONFIG_SOC_SERIES_S32K1`、`CONFIG_SOC_SERIES_S32K3`、`CONFIG_SOC_SERIES_S32ZE`、`CONFIG_COUNTER_NRFX_TIMER_USE_CLOCK_CONTROL`。

<a id="CONFIG_CLOCK_CONTROL_ADI_AXI_CLKGEN"></a>

## 62.2 `CONFIG_CLOCK_CONTROL_ADI_AXI_CLKGEN`

**提示（Prompt）**：亚德诺 AXI 时钟发生器驱动（Analog Devices AXI Clock Generator Driver）

**说明（Help）**

亚德诺（Analog Devices）AXI 时钟发生器内核（Clock Generator Core）的驱动，通过 Xilinx 混合模式时钟管理器（MMCM）提供软件可编程的时钟输出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_AXI_CLKGEN_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.adi_axi_clkgen:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.adi_axi_clkgen#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_ADSP"></a>

## 62.3 `CONFIG_CLOCK_CONTROL_ADSP`

**提示（Prompt）**：Intel CAVS 时钟控制（Clock Control）

**说明（Help）**

CAVS 时钟驱动（Clock Driver），允许选择时钟类型，从而选择频率。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_ADSP_SHIM_CLKCTL_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADSP_CLOCK
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.cavs:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.cavs#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_ADSP_CLOCK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADSP_CLOCK)。

<a id="CONFIG_CLOCK_CONTROL_AESC"></a>

## 62.4 `CONFIG_CLOCK_CONTROL_AESC`

**提示（Prompt）**：Aesc Silicon 时钟控制器驱动（Clock Controller Driver）

**说明（Help）**

启用 Aesc Silicon 时钟控制器（Clock Controller）驱动。参考时钟频率（Reference Clock Frequency）从节点的 `syscon` 属性引用的系统控制设备（Syscon Device）读取。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AESC_CLOCK_CONTROLLER_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SYSCON
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.aesc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.aesc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_SYSCON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYSCON)。

<a id="CONFIG_CLOCK_CONTROL_AGILEX5"></a>

## 62.5 `CONFIG_CLOCK_CONTROL_AGILEX5`

**提示（Prompt）**：Agilex5 SoCFPGA 时钟控制驱动（Clock Control Driver）

**说明（Help）**

启用 Intel Agilex5 SoCFPGA 片上系统（SoC）的时钟驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_AGILEX5_CLOCK_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.agilex5:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.agilex5#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_ALIF"></a>

## 62.6 `CONFIG_CLOCK_CONTROL_ALIF`

**提示（Prompt）**：Alif Semiconductor 时钟控制驱动（Clock Control Driver）

**说明（Help）**

启用 Alif Semiconductor 片上系统（SoC）的时钟控制（Clock Control）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ALIF_CLOCKCTRL_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.alif:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.alif#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_AMBIQ"></a>

## 62.7 `CONFIG_CLOCK_CONTROL_AMBIQ`

**提示（Prompt）**：Ambiq 时钟控制驱动（Clock Control Driver）

**说明（Help）**

启用 Ambiq 时钟控制（Clock Control）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMBIQ_CLKCTRL_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_AMBIQ_HAL
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.ambiq:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.ambiq#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_AMBIQ_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL)。

<a id="CONFIG_CLOCK_CONTROL_AMEBA"></a>

## 62.8 `CONFIG_CLOCK_CONTROL_AMEBA`

**提示（Prompt）**：Ameba 时钟控制器驱动（Clock Controller Driver）

**说明（Help）**

启用 Ameba 时钟控制器（Clock Controller）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_AMEBA_RCC_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.ameba:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.ameba#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_ARM_SCMI"></a>

## 62.9 `CONFIG_CLOCK_CONTROL_ARM_SCMI`

**提示（Prompt）**：SCMI 时钟协议控制器驱动（SCMI Clock Protocol Driver）

**说明（Help）**

启用基于系统控制与管理接口（SCMI）的时钟控制（Clock Control）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_SCMI_CLK_HELPERS && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_SOC_R8A78000_R52
CONFIG_SOC_R8A78000_A720
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.arm_scmi:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.arm_scmi#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SCMI_CLK_HELPERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_SCMI_CLK_HELPERS)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_SOC_R8A78000_R52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A78000_R52)、[`CONFIG_SOC_R8A78000_A720`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A78000_A720)。

<a id="CONFIG_CLOCK_CONTROL_AST10X0"></a>

## 62.10 `CONFIG_CLOCK_CONTROL_AST10X0`

**提示（Prompt）**：ASPEED 时钟控制驱动（Clock Control Driver）

**说明（Help）**

启用 ASPEED AST10X0 系列片上系统（SoC）的时钟驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ASPEED_AST10X0_CLOCK_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.aspeed:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.aspeed#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_BEE"></a>

## 62.11 `CONFIG_CLOCK_CONTROL_BEE`

**提示（Prompt）**：瑞昱 Bee 系列时钟控制驱动（Realtek Clock Control Driver）

**说明（Help）**

启用瑞昱（Realtek）Bee 片上系统（SoC）的时钟控制器（Clock Controller）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_BEE_CCTL_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAL_REALTEK_BEE_RCC
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.bee:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.bee#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_HAL_REALTEK_BEE_RCC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAL_REALTEK_BEE_RCC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAL_REALTEK_BEE_RCC`。

<a id="CONFIG_CLOCK_CONTROL_BEETLE"></a>

## 62.12 `CONFIG_CLOCK_CONTROL_BEETLE`

**提示（Prompt）**：BEETLE 时钟控制（Clock Control）

**说明（Help）**

启用 STM32F4 微控制器（MCU）系列中复位与时钟控制子系统（Reset & Clock Control Subsystem）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ARM_BEETLE_SYSCON_ENABLED && CONFIG_SOC_FAMILY_ARM && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.beetle:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.beetle#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ARM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ARM)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ARM`。

<a id="CONFIG_CLOCK_CONTROL_BEETLE_ENABLE_PLL"></a>

## 62.13 `CONFIG_CLOCK_CONTROL_BEETLE_ENABLE_PLL`

**提示（Prompt）**：Beetle 的锁相环（PLL）

**说明（Help）**

启用 Beetle 的锁相环（PLL）。如不确定，选择 `n`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_BEETLE && CONFIG_CLOCK_CONTROL_BEETLE && CONFIG_SOC_FAMILY_ARM && CONFIG_CLOCK_CONTROL
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.beetle:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.beetle#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → BEETLE 时钟控制（Clock Control）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_BEETLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BEETLE)、[`CONFIG_CLOCK_CONTROL_BEETLE`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_BEETLE)、[`CONFIG_SOC_FAMILY_ARM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ARM)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ARM`。

<a id="CONFIG_CLOCK_CONTROL_BOUFFALOLAB_BL60X"></a>

## 62.14 `CONFIG_CLOCK_CONTROL_BOUFFALOLAB_BL60X`

**提示（Prompt）**：博流 BL60x 时钟控制（Bouffalolab Clock Control）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_BL60X_CLOCK_CONTROLLER_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.bflb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.bflb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_BOUFFALOLAB_BL616CL"></a>

## 62.15 `CONFIG_CLOCK_CONTROL_BOUFFALOLAB_BL616CL`

**提示（Prompt）**：博流 BL616CL 时钟控制驱动（Bouffalolab Clock Control Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_BL616CL_CLOCK_CONTROLLER_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.bflb:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.bflb#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_BOUFFALOLAB_BL61X"></a>

## 62.16 `CONFIG_CLOCK_CONTROL_BOUFFALOLAB_BL61X`

**提示（Prompt）**：博流 BL61x 时钟控制驱动（Bouffalolab Clock Control Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_BL61X_CLOCK_CONTROLLER_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.bflb:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.bflb#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_BOUFFALOLAB_BL70X_L"></a>

## 62.17 `CONFIG_CLOCK_CONTROL_BOUFFALOLAB_BL70X_L`

**提示（Prompt）**：博流 BL70x(L) 时钟控制（Bouffalolab Clock Control）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_BL70X_L_CLOCK_CONTROLLER_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.bflb:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.bflb#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_BOUFFALOLAB_BL808"></a>

## 62.18 `CONFIG_CLOCK_CONTROL_BOUFFALOLAB_BL808`

**提示（Prompt）**：博流 BL808 时钟控制驱动（Bouffalolab Clock Control Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_BL808_CLOCK_CONTROLLER_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.bflb:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.bflb#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_EM32_AHB"></a>

## 62.19 `CONFIG_CLOCK_CONTROL_EM32_AHB`

**提示（Prompt）**：义隆 EM32 AHB 时钟控制（Elan Clock Control）

**说明（Help）**

启用 EM32FXXX 的高级高性能总线（AHB）时钟控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_EM32F967 && DT_HAS_ELAN_EM32_AHB_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SYSCON
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.em32:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.em32#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_EM32F967`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EM32F967)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_SYSCON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYSCON)。

<a id="CONFIG_CLOCK_CONTROL_EM32_AHB_INIT_PRIORITY"></a>

## 62.20 `CONFIG_CLOCK_CONTROL_EM32_AHB_INIT_PRIORITY`

**提示（Prompt）**：EM32 AHB 时钟控制初始化优先级（Initialization Priority）

**说明（Help）**

EM32 AHB 时钟控制（Clock Control）驱动的初始化优先级。必须在系统控制（Syscon）之后初始化。依赖 AHB 时钟控制器的其他 EM32 驱动，例如 APB 时钟控制和 GPIO，必须在此驱动之后初始化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_EM32_AHB && CONFIG_CLOCK_CONTROL_EM32_AHB && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
52
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.em32:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.em32#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_EM32_AHB`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_EM32_AHB)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_EM32_APB"></a>

## 62.21 `CONFIG_CLOCK_CONTROL_EM32_APB`

**提示（Prompt）**：义隆 EM32 APB 时钟控制（Elan Clock Control）

**说明（Help）**

启用 EM32FXXX 的高级外设总线（APB）时钟控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_EM32F967 && DT_HAS_ELAN_EM32_APB_ENABLED && CONFIG_CLOCK_CONTROL_EM32_AHB && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.em32:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.em32#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → 义隆 EM32 AHB 时钟控制（Elan Clock Control）

**配置项引用（Symbol References）**：[`CONFIG_SOC_EM32F967`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EM32F967)、[`CONFIG_CLOCK_CONTROL_EM32_AHB`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_EM32_AHB)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_EM32_APB_INIT_PRIORITY"></a>

## 62.22 `CONFIG_CLOCK_CONTROL_EM32_APB_INIT_PRIORITY`

**提示（Prompt）**：EM32 APB 时钟控制初始化优先级（Initialization Priority）

**说明（Help）**

EM32 APB 时钟控制（Clock Control）驱动的初始化优先级。其数值必须大于 `CLOCK_CONTROL_EM32_AHB_INIT_PRIORITY`，因为 APB 时钟依赖 AHB 时钟。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_EM32_APB && CONFIG_CLOCK_CONTROL_EM32_APB && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
53
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.em32:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.em32#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_EM32_APB`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_EM32_APB)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_ESP32"></a>

## 62.23 `CONFIG_CLOCK_CONTROL_ESP32`

**提示（Prompt）**：ESP32 时钟驱动（Clock Driver）

**说明（Help）**

启用 ESP32 时钟（Clock）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_CLOCK_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.esp32:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.esp32#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_CAL_CYCLES"></a>

## 62.24 `CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_CAL_CYCLES`

**提示（Prompt）**：RTC_SLOW_CLK 校准周期数（Calibration Cycles）

**说明（Help）**

启动代码初始化 `RTC_SLOW_CLK` 时，可以通过比较其频率与主晶体（Main XTAL）频率进行校准（Calibration）。此选项指定校准例程测量的 `RTC_SLOW_CLK` 周期数量。

数值越大，校准精度越高；这对于长时间处于深度休眠（Deep Sleep）的应用可能很重要。数值越小，启动时间越短。

设为 0 时，启动期间不执行时钟校准，而使用估计频率：

- 内部 RC 振荡器（Internal RC Oscillator）作为时钟源时，假定为 150000 Hz。
- 使用 32k 晶体振荡器（Crystal Oscillator）时，假定为 32768 Hz。

推荐值：

- 内部 RC 振荡器使用 1024；ESP32-S2 使用 576。
- 32k 晶体振荡器使用 3000 或更大值。更大的值有助于改善晶体启动检测。如果晶体无法启动，驱动会退回内部 RC。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_ESP32 && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
3000 if CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_EXT_CRYS || CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_EXT_OSC || CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_INT_8MD256
576 if CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_INT_RC && CONFIG_SOC_SERIES_ESP32S2
1024
```

**取值范围（Ranges）**

```text
[0, 27000] if CONFIG_SOC_SERIES_ESP32 && (CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_EXT_CRYS || CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_EXT_OSC || CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_INT_8MD256)
[0, 8190] if !CONFIG_SOC_SERIES_ESP32 && (CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_EXT_CRYS || CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_EXT_OSC || CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_INT_8MD256)
[0, 32766]
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.esp32:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.esp32#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → ESP32 时钟驱动（Clock Driver）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_ESP32`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_ESP32)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_EXT_CRYS`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_EXT_CRYS)、[`CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_EXT_OSC`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_EXT_OSC)、[`CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_INT_8MD256`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_INT_8MD256)、[`CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_INT_RC`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_INT_RC)、[`CONFIG_SOC_SERIES_ESP32S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32)。

<a id="CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC"></a>

## 62.25 `CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC`

**提示（Prompt）**：实时时钟时钟源（RTC Clock Source）

**说明（Help）**

选择用作实时时钟（RTC）时钟源的时钟。默认值来自设备树（Devicetree）的 `slow-clk-src` 属性，但可在 `prj.conf` 中覆盖。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_ESP32 && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_EXT_CRYS if 0 = 1 && !CONFIG_SOC_SERIES_ESP32C2
CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_EXT_OSC if 0 = 1 && CONFIG_SOC_SERIES_ESP32C2
CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_INT_8MD256 if 0 = 2 && !CONFIG_SOC_SERIES_ESP32C6 && !CONFIG_SOC_SERIES_ESP32H2 && !CONFIG_SOC_SERIES_ESP32C5 && !CONFIG_SOC_SERIES_ESP32C61 && !CONFIG_SOC_SERIES_ESP32P4
CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_INT_RC
```

**可选项（Choices）**

```text
CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_INT_RC
CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_EXT_CRYS
CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_EXT_OSC
CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_INT_8MD256
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.esp32:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.esp32#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → ESP32 时钟驱动（Clock Driver）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_ESP32`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_ESP32)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_EXT_CRYS`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_EXT_CRYS)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_EXT_OSC`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_EXT_OSC)、[`CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_INT_8MD256`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_INT_8MD256)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_INT_RC`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_INT_RC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32P4`。

<a id="CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_EXT_CRYS"></a>

## 62.26 `CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_EXT_CRYS`

**提示（Prompt）**：外部 32 kHz 晶体（External Crystal）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_SOC_SERIES_ESP32C2 && <choice CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC>
```

**主动选择（Selects）**

```text
CONFIG_CLOCK_CONTROL_ESP32_SYSTEM_RTC_EXT_XTAL
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.esp32:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.esp32#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → ESP32 时钟驱动（Clock Driver） → 实时时钟时钟源（RTC Clock Source）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC)、[`CONFIG_CLOCK_CONTROL_ESP32_SYSTEM_RTC_EXT_XTAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_ESP32_SYSTEM_RTC_EXT_XTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_CLOCK_CONTROL_ESP32_SYSTEM_RTC_EXT_XTAL`。

<a id="CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_EXT_OSC"></a>

## 62.27 `CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_EXT_OSC`

**提示（Prompt）**：外部 32 kHz 振荡器（External Oscillator）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC>
```

**主动选择（Selects）**

```text
CONFIG_CLOCK_CONTROL_ESP32_SYSTEM_RTC_EXT_OSC
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.esp32:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.esp32#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → ESP32 时钟驱动（Clock Driver） → 实时时钟时钟源（RTC Clock Source）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC)、[`CONFIG_CLOCK_CONTROL_ESP32_SYSTEM_RTC_EXT_OSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_ESP32_SYSTEM_RTC_EXT_OSC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CLOCK_CONTROL_ESP32_SYSTEM_RTC_EXT_OSC`。

<a id="CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_INT_8MD256"></a>

## 62.28 `CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_INT_8MD256`

**提示（Prompt）**：内部振荡器，256 分频（Internal Oscillator Divided by 256）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_SOC_SERIES_ESP32C6 && !CONFIG_SOC_SERIES_ESP32H2 && !CONFIG_SOC_SERIES_ESP32C5 && !CONFIG_SOC_SERIES_ESP32C61 && !CONFIG_SOC_SERIES_ESP32P4 && <choice CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC>
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.esp32:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.esp32#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → ESP32 时钟驱动（Clock Driver） → 实时时钟时钟源（RTC Clock Source）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32P4`。

<a id="CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_INT_RC"></a>

## 62.29 `CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_INT_RC`

**提示（Prompt）**：内部 RC 振荡器（Internal RC Oscillator）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC>
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.esp32:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.esp32#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → ESP32 时钟驱动（Clock Driver） → 实时时钟时钟源（RTC Clock Source）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC)。

<a id="CONFIG_CLOCK_CONTROL_ESP32_RTC_XTAL_CAL_RETRY"></a>

## 62.30 `CONFIG_CLOCK_CONTROL_ESP32_RTC_XTAL_CAL_RETRY`

**提示（Prompt）**：重复 32k 晶体校准的尝试次数（XTAL Calibration Attempts）

**说明（Help）**

放弃 32k 晶体（XTAL）并切换到内部 RC 之前，允许重复校准的尝试次数。如果 32k 晶体振荡器无法启动，系统转而使用内部 RC，可增大此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_EXT_CRYS && CONFIG_CLOCK_CONTROL_ESP32 && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
3 if CONFIG_SOC_SERIES_ESP32S2
1
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.esp32:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.esp32#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → ESP32 时钟驱动（Clock Driver）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_EXT_CRYS`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_EXT_CRYS)、[`CONFIG_CLOCK_CONTROL_ESP32`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_ESP32)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_SOC_SERIES_ESP32S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32S2)。

<a id="CONFIG_CLOCK_CONTROL_FIXED_RATE_CLOCK"></a>

## 62.31 `CONFIG_CLOCK_CONTROL_FIXED_RATE_CLOCK`

**提示（Prompt）**：固定时钟控制（Fixed Clock Control）

**说明（Help）**

启用设备树（Devicetree）定义的固定时钟（Fixed Clock）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_MCXL
CONFIG_SOC_AMD_VERSALNET_RPU
CONFIG_SOC_AMD_VERSALNET_APU
CONFIG_SOC_AMD_VERSAL2_RPU
CONFIG_SOC_AMD_VERSAL2_APU
CONFIG_XLNX_SDHC
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.fixed:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.fixed#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_SOC_FAMILY_MCXL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXL)、[`CONFIG_SOC_AMD_VERSALNET_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSALNET_RPU)、[`CONFIG_SOC_AMD_VERSALNET_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSALNET_APU)、[`CONFIG_SOC_AMD_VERSAL2_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSAL2_RPU)、[`CONFIG_SOC_AMD_VERSAL2_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSAL2_APU)、[`CONFIG_XLNX_SDHC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XLNX_SDHC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MCXL`。

<a id="CONFIG_CLOCK_CONTROL_FOCALTECH_FT9001"></a>

## 62.32 `CONFIG_CLOCK_CONTROL_FOCALTECH_FT9001`

**提示（Prompt）**：敦泰 FT9001 时钟电源模块驱动（FocalTech Clock Power Module，CPM）

**说明（Help）**

启用敦泰（FocalTech）FT9001 片上系统（SoC）的时钟控制（Clock Control）驱动。通过时钟电源模块（Clock Power Module，CPM）控制外设时钟；CPM 管理多个片上外设的时钟门控（Clock Gating），包括 UART、SPI、I2C、CAN、USB、密码引擎（Crypto Engine）及内存控制器（Memory Controller）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_FOCALTECH_FT9001_CPM_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.focaltech:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.focaltech#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_GD32"></a>

## 62.33 `CONFIG_CLOCK_CONTROL_GD32`

**提示（Prompt）**：GD32 时钟控制（Clock Control）

**说明（Help）**

启用兆易创新（GigaDevice）复位时钟单元（Reset Clock Unit，RCU）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GD_GD32_CCTL_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.gd32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.gd32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_IFX_CLOCK_V2"></a>

## 62.34 `CONFIG_CLOCK_CONTROL_IFX_CLOCK_V2`

**提示（Prompt）**：英飞凌 Traveo 时钟控制驱动（Infineon Clock Control Driver）

**说明（Help）**

启用英飞凌（Infineon）Traveo 系列的时钟控制（Clock Control）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_CLK_OSC_ENABLED && DT_HAS_INFINEON_CLK_PLL_ENABLED && DT_HAS_INFINEON_CAT1C_CLK_HF_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.infineon:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.infineon#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_IFX_FIXED_CLOCK"></a>

## 62.35 `CONFIG_CLOCK_CONTROL_IFX_FIXED_CLOCK`

**提示（Prompt）**：英飞凌固定时钟驱动（Infineon Fixed Clock Driver）

**说明（Help）**

启用英飞凌（Infineon）CAT1 系列的固定时钟（Fixed Clock）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_FIXED_CLOCK_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.infineon:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.infineon#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_IFX_FIXED_FACTOR_CLOCK"></a>

## 62.36 `CONFIG_CLOCK_CONTROL_IFX_FIXED_FACTOR_CLOCK`

**提示（Prompt）**：英飞凌固定比例时钟驱动（Infineon Fixed Factor Clock Driver）

**说明（Help）**

启用英飞凌（Infineon）CAT1 系列的固定时钟（Fixed Clock）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_FIXED_FACTOR_CLOCK_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.infineon:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.infineon#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_IFX_FIXED_FACTOR_CLOCK_INIT_PRIORITY"></a>

## 62.37 `CONFIG_CLOCK_CONTROL_IFX_FIXED_FACTOR_CLOCK_INIT_PRIORITY`

**提示（Prompt）**：英飞凌固定比例时钟驱动初始化优先级（Init Priority）

**说明（Help）**

英飞凌（Infineon）固定比例时钟控制（Fixed Factor Clock Control）驱动的初始化优先级。原文要求它低于固定比例时钟驱动的优先级，以确保时钟路径（Clock Path）先初始化。

译注：上游在比较双方时都使用 fixed factor clock driver，未明确区分两者；此处保留原始条件，不推定其实际指代。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_IFX_FIXED_FACTOR_CLOCK && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
29 if !CONFIG_SOC_FAMILY_INFINEON_PSOC4
31 if CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.infineon:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.infineon#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_IFX_FIXED_FACTOR_CLOCK`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_IFX_FIXED_FACTOR_CLOCK)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_CLOCK_CONTROL_IFX_PERI_CLOCK"></a>

## 62.38 `CONFIG_CLOCK_CONTROL_IFX_PERI_CLOCK`

**提示（Prompt）**：英飞凌外设分频时钟驱动（Infineon Peri Div Clock Driver）

**说明（Help）**

启用英飞凌（Infineon）CAT1 系列的外设时钟（Peripheral Clock）驱动。选择外设时钟组驱动，即 `CLOCK_CONTROL_IFX_PERI_CLOCK_V2`、`infineon,peri-clk` 时，会强制禁用此项，因为时钟组驱动自行管理 `infineon,peri-div` 子节点。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_PERI_DIV_ENABLED && !CONFIG_CLOCK_CONTROL_IFX_PERI_CLOCK_V2 && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.infineon:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.infineon#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_IFX_PERI_CLOCK_V2`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_IFX_PERI_CLOCK_V2)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_IFX_PERI_CLOCK_V2"></a>

## 62.39 `CONFIG_CLOCK_CONTROL_IFX_PERI_CLOCK_V2`

**提示（Prompt）**：英飞凌外设时钟组驱动（Infineon Peripheral Clock Group Driver）

**说明（Help）**

启用英飞凌（Infineon）微控制器（MCU）的外设时钟组（Peripheral Clock Group）驱动，对应 `infineon,peri-clk`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_PERI_CLK_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.infineon:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.infineon#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_INFINEON_CAT1"></a>

## 62.40 `CONFIG_CLOCK_CONTROL_INFINEON_CAT1`

**提示（Prompt）**：英飞凌传统 HAL CAT1 时钟控制驱动（Infineon Legacy HAL Clock Control Driver）

**说明（Help）**

启用英飞凌（Infineon）CAT1 系列的时钟控制（Clock Control）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INFINEON_CAT1 && DT_HAS_FIXED_CLOCK_ENABLED && CONFIG_USE_INFINEON_LEGACY_HAL && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.infineon:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.infineon#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_USE_INFINEON_LEGACY_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_LEGACY_HAL)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`。

<a id="CONFIG_CLOCK_CONTROL_INIT_PRIORITY"></a>

## 62.41 `CONFIG_CLOCK_CONTROL_INIT_PRIORITY`

**提示（Prompt）**：时钟控制初始化优先级（Clock Control Init Priority）

**说明（Help）**

时钟控制（Clock Control）驱动设备的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_OBJECTS
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_KERNEL_INIT_PRIORITY_OBJECTS`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_OBJECTS)。

<a id="CONFIG_CLOCK_CONTROL_IT51XXX"></a>

## 62.42 `CONFIG_CLOCK_CONTROL_IT51XXX`

**提示（Prompt）**：ITE IT51XXX 时钟控制器驱动（Clock Controller Driver）

**说明（Help）**

启用 IT51XXX 时钟控制器（Clock Controller）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT51XXX_ECPM_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.it51xxx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.it51xxx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_LITEX"></a>

## 62.43 `CONFIG_CLOCK_CONTROL_LITEX`

**提示（Prompt）**：LiteX MMCM 时钟控制（Clock Control）

**说明（Help）**

启用 LiteX 时钟控制（Clock Control）驱动，允许修改最多 7 路时钟输出的相位（Phase）、占空比（Duty Cycle）、频率（Frequency）等参数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LITEX_CLK_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.litex:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.litex#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_LPC11U6X"></a>

## 62.44 `CONFIG_CLOCK_CONTROL_LPC11U6X`

**提示（Prompt）**：LPC11U6X 复位与时钟控制（Reset and Clock Control）

**说明（Help）**

启用 LPC11U6X 微控制器（MCU）使用的复位与时钟控制（Reset and Clock Control）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPC11U6X_SYSCON_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.lpc11u6x:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.lpc11u6x#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_CLOCK_CONTROL_LPC11U6X_ENABLE_SRAM1"></a>

## 62.45 `CONFIG_CLOCK_CONTROL_LPC11U6X_ENABLE_SRAM1`

**提示（Prompt）**：SRAM1

**说明（Help）**

启用静态 RAM 区域 `SRAM1`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_LPC11U6X && CONFIG_CLOCK_CONTROL
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.lpc11u6x:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.lpc11u6x#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → LPC11U6X 复位与时钟控制（Reset and Clock Control）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_LPC11U6X`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_LPC11U6X)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_LPC11U6X_ENABLE_USB_RAM"></a>

## 62.46 `CONFIG_CLOCK_CONTROL_LPC11U6X_ENABLE_USB_RAM`

**提示（Prompt）**：USB RAM

**说明（Help）**

启用 USB RAM。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_LPC11U6X && CONFIG_CLOCK_CONTROL
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.lpc11u6x:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.lpc11u6x#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → LPC11U6X 复位与时钟控制（Reset and Clock Control）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_LPC11U6X`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_LPC11U6X)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_LPC11U6X_PLL_SRC"></a>

## 62.47 `CONFIG_CLOCK_CONTROL_LPC11U6X_PLL_SRC`

**提示（Prompt）**：LPC11U6X 锁相环时钟源（PLL Clock Source）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_LPC11U6X && CONFIG_CLOCK_CONTROL
```

**可选项（Choices）**

```text
CONFIG_CLOCK_CONTROL_LPC11U6X_PLL_SRC_IRC
CONFIG_CLOCK_CONTROL_LPC11U6X_PLL_SRC_SYSOSC
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.lpc11u6x:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.lpc11u6x#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → LPC11U6X 复位与时钟控制（Reset and Clock Control）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_LPC11U6X`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_LPC11U6X)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_CLOCK_CONTROL_LPC11U6X_PLL_SRC_IRC`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_LPC11U6X_PLL_SRC_IRC)、[`CONFIG_CLOCK_CONTROL_LPC11U6X_PLL_SRC_SYSOSC`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_LPC11U6X_PLL_SRC_SYSOSC)。

<a id="CONFIG_CLOCK_CONTROL_LPC11U6X_PLL_SRC_IRC"></a>

## 62.48 `CONFIG_CLOCK_CONTROL_LPC11U6X_PLL_SRC_IRC`

**提示（Prompt）**：内部 RC 振荡器（IRC）

**说明（Help）**

使用内部振荡器（Internal Oscillator）作为锁相环（PLL）的时钟源。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CLOCK_CONTROL_LPC11U6X_PLL_SRC>
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.lpc11u6x:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.lpc11u6x#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → LPC11U6X 复位与时钟控制（Reset and Clock Control） → LPC11U6X 锁相环时钟源（PLL Clock Source）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_LPC11U6X_PLL_SRC`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_LPC11U6X_PLL_SRC)。

<a id="CONFIG_CLOCK_CONTROL_LPC11U6X_PLL_SRC_SYSOSC"></a>

## 62.49 `CONFIG_CLOCK_CONTROL_LPC11U6X_PLL_SRC_SYSOSC`

**提示（Prompt）**：系统振荡器（SYSOSC）

**说明（Help）**

使用系统振荡器（System Oscillator）作为锁相环（PLL）的时钟源。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CLOCK_CONTROL_LPC11U6X_PLL_SRC>
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.lpc11u6x:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.lpc11u6x#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → LPC11U6X 复位与时钟控制（Reset and Clock Control） → LPC11U6X 锁相环时钟源（PLL Clock Source）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_LPC11U6X_PLL_SRC`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_LPC11U6X_PLL_SRC)。

<a id="CONFIG_CLOCK_CONTROL_LPC84X"></a>

## 62.50 `CONFIG_CLOCK_CONTROL_LPC84X`

**提示（Prompt）**：LPC84X 时钟控制驱动（Clock Control Driver）

**说明（Help）**

启用 LPC84x 时钟控制（Clock Control）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPC84X_CLOCK_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.lpc84x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.lpc84x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_MAX32"></a>

## 62.51 `CONFIG_CLOCK_CONTROL_MAX32`

**提示（Prompt）**：MAX32 时钟控制驱动（Clock Control Driver）

**说明（Help）**

启用亚德诺（Analog Devices）MAX32xxx / MAX78xxx 片上系统（SoC）系列的时钟控制（Clock Control）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX32_GCR_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.max32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.max32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_MCHP_ASYNC_ON"></a>

## 62.52 `CONFIG_CLOCK_CONTROL_MCHP_ASYNC_ON`

**提示（Prompt）**：异步开启时钟（Async Clock On）

**说明（Help）**

启用异步开启（Async On）API。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_MCHP_COMMON && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.mchp:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.mchp#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_MCHP_COMMON`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_MCHP_COMMON)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_MCHP_COMMON"></a>

## 62.53 `CONFIG_CLOCK_CONTROL_MCHP_COMMON`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Microchip 时钟控制（Clock Control）驱动的共用选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL
```

**被选择（Selected by）**

```text
CONFIG_CLOCK_CONTROL_MCHP_SAM_D5X_E5X
CONFIG_CLOCK_CONTROL_MCHP_PIC32CK_SG_GC
CONFIG_CLOCK_CONTROL_MCHP_PIC32CM_JH
CONFIG_CLOCK_CONTROL_MCHP_PIC32CM_PL
CONFIG_CLOCK_CONTROL_MCHP_PIC32CZ_CA
CONFIG_CLOCK_CONTROL_MCHP_PIC32CM_SG_GC
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.mchp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.mchp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_CLOCK_CONTROL_MCHP_SAM_D5X_E5X`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_MCHP_SAM_D5X_E5X)、[`CONFIG_CLOCK_CONTROL_MCHP_PIC32CK_SG_GC`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_MCHP_PIC32CK_SG_GC)、[`CONFIG_CLOCK_CONTROL_MCHP_PIC32CM_JH`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_MCHP_PIC32CM_JH)、[`CONFIG_CLOCK_CONTROL_MCHP_PIC32CM_PL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_MCHP_PIC32CM_PL)、[`CONFIG_CLOCK_CONTROL_MCHP_PIC32CZ_CA`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_MCHP_PIC32CZ_CA)、[`CONFIG_CLOCK_CONTROL_MCHP_PIC32CM_SG_GC`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_MCHP_PIC32CM_SG_GC)。

<a id="CONFIG_CLOCK_CONTROL_MCHP_CONFIG_BOOTUP"></a>

## 62.54 `CONFIG_CLOCK_CONTROL_MCHP_CONFIG_BOOTUP`

**提示（Prompt）**：启动时钟配置（Bootup Clock Configuration）

**说明（Help）**

启用从设备树节点（Devicetree Node）读取的启动时钟配置（Bootup Clock Configuration）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_MCHP_COMMON && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.mchp:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.mchp#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_MCHP_COMMON`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_MCHP_COMMON)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_MCHP_CONFIG_RUNTIME"></a>

## 62.55 `CONFIG_CLOCK_CONTROL_MCHP_CONFIG_RUNTIME`

**提示（Prompt）**：运行时时钟配置（Runtime Clock Configuration）

**说明（Help）**

启用通过 API 进行运行时时钟配置（Runtime Clock Configuration）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_MCHP_COMMON && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.mchp:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.mchp#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_MCHP_COMMON`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_MCHP_COMMON)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_MCHP_GCLK_PINOUT"></a>

## 62.56 `CONFIG_CLOCK_CONTROL_MCHP_GCLK_PINOUT`

**提示（Prompt）**：通过 GCLK I/O 引脚输出时钟（Clock Output）

**说明（Help）**

启用通过 GCLK I/O 引脚输出时钟（Clock Output）的功能。根据时钟源层级（Clock Source Hierarchy）的深度，可能增加代码体积。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_MCHP_COMMON && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.mchp:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.mchp#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_MCHP_COMMON`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_MCHP_COMMON)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_MCHP_GET_RATE"></a>

## 62.57 `CONFIG_CLOCK_CONTROL_MCHP_GET_RATE`

**提示（Prompt）**：获取时钟频率（Get Clock Rate）

**说明（Help）**

启用获取时钟频率（Clock Rate）的支持。根据时钟源层级（Clock Source Hierarchy）的深度，可能增加代码体积。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_MCHP_COMMON && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.mchp:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.mchp#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_MCHP_COMMON`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_MCHP_COMMON)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_MCHP_PIC32CK_SG_GC"></a>

## 62.58 `CONFIG_CLOCK_CONTROL_MCHP_PIC32CK_SG_GC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CK SG/GC 片上系统（SoC）系列的时钟控制器（Clock Controller）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_PIC32CK_SG_GC_CLOCK_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CLOCK_CONTROL_MCHP_COMMON
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.mchp:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.mchp#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_CLOCK_CONTROL_MCHP_COMMON`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_MCHP_COMMON)。

<a id="CONFIG_CLOCK_CONTROL_MCHP_PIC32CM_JH"></a>

## 62.59 `CONFIG_CLOCK_CONTROL_MCHP_PIC32CM_JH`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CM_JH 系列的时钟控制器（Clock Controller）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_PIC32CM_JH_CLOCK_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CLOCK_CONTROL_MCHP_COMMON
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.mchp:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.mchp#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_CLOCK_CONTROL_MCHP_COMMON`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_MCHP_COMMON)。

<a id="CONFIG_CLOCK_CONTROL_MCHP_PIC32CM_PL"></a>

## 62.60 `CONFIG_CLOCK_CONTROL_MCHP_PIC32CM_PL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CM_PL 系列的时钟控制器（Clock Controller）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_PIC32CM_PL_CLOCK_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CLOCK_CONTROL_MCHP_COMMON
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.mchp:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.mchp#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_CLOCK_CONTROL_MCHP_COMMON`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_MCHP_COMMON)。

<a id="CONFIG_CLOCK_CONTROL_MCHP_PIC32CM_SG_GC"></a>

## 62.61 `CONFIG_CLOCK_CONTROL_MCHP_PIC32CM_SG_GC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CM_SG_GC 系列的时钟控制器（Clock Controller）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_PIC32CM_SG_GC_CLOCK_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CLOCK_CONTROL_MCHP_COMMON
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.mchp:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.mchp#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_CLOCK_CONTROL_MCHP_COMMON`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_MCHP_COMMON)。

<a id="CONFIG_CLOCK_CONTROL_MCHP_PIC32CZ_CA"></a>

## 62.62 `CONFIG_CLOCK_CONTROL_MCHP_PIC32CZ_CA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CZ_CA 系列的时钟控制器（Clock Controller）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_PIC32CZ_CA_CLOCK_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CLOCK_CONTROL_MCHP_COMMON
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.mchp:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.mchp#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_CLOCK_CONTROL_MCHP_COMMON`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_MCHP_COMMON)。

<a id="CONFIG_CLOCK_CONTROL_MCHP_SAM_D5X_E5X"></a>

## 62.63 `CONFIG_CLOCK_CONTROL_MCHP_SAM_D5X_E5X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip SAM D5X/E5X 片上系统（SoC）系列的时钟控制器（Clock Controller）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_SAM_D5X_E5X_CLOCK_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CLOCK_CONTROL_MCHP_COMMON
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.mchp:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.mchp#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_CLOCK_CONTROL_MCHP_COMMON`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_MCHP_COMMON)。

<a id="CONFIG_CLOCK_CONTROL_MCHP_SET_RATE"></a>

## 62.64 `CONFIG_CLOCK_CONTROL_MCHP_SET_RATE`

**提示（Prompt）**：设置时钟频率（Set Clock Rate）

**说明（Help）**

启用设置时钟频率（Set Rate）的 API。根据时钟源层级（Clock Source Hierarchy）的深度，可能增加代码体积。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_MCHP_GET_RATE && CONFIG_CLOCK_CONTROL_MCHP_COMMON && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.mchp:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.mchp#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → 获取时钟频率（Get Clock Rate）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_MCHP_GET_RATE`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_MCHP_GET_RATE)、[`CONFIG_CLOCK_CONTROL_MCHP_COMMON`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_MCHP_COMMON)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_MCHP_SMARTFUSION2"></a>

## 62.65 `CONFIG_CLOCK_CONTROL_MCHP_SMARTFUSION2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip SmartFusion2 的只读时钟控制器（Read-Only Clock Controller）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_SMARTFUSION2_CLOCK_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.mchp:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.mchp#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_MCHP_XEC"></a>

## 62.66 `CONFIG_CLOCK_CONTROL_MCHP_XEC`

**提示（Prompt）**：Microchip XEC PCR 时钟控制驱动（Clock Control Driver）

**说明（Help）**

启用 Microchip XEC PCR 时钟（Clock）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_XEC_PCR_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.xec:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.xec#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_MCUX_CCM"></a>

## 62.67 `CONFIG_CLOCK_CONTROL_MCUX_CCM`

**提示（Prompt）**：MCUX CCM 驱动（Driver）

**说明（Help）**

启用 MCUX CCM 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_CCM_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nxp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nxp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_MCUX_CCM_REV2"></a>

## 62.68 `CONFIG_CLOCK_CONTROL_MCUX_CCM_REV2`

**提示（Prompt）**：MCUX CCM 第 2 版驱动（Rev 2 Driver）

**说明（Help）**

启用 MCUX CCM 第 2 版（Rev 2）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_CCM_REV2_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nxp:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nxp#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_MCUX_CCM_REV3"></a>

## 62.69 `CONFIG_CLOCK_CONTROL_MCUX_CCM_REV3`

**提示（Prompt）**：MCUX CCM 第 3 版驱动（Rev 3 Driver）

**说明（Help）**

启用恩智浦（NXP）i.MX CCM 第 3 版（Rev 3）时钟控制驱动。外设时钟描述符（Clock Specifier）同时编码门控（Gate）标识和时钟根（Clock Root）标识；可配置的时钟根通过控制器的设备树子节点（Devicetree Child Node）描述。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_CCM_REV3_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nxp:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nxp#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_MCUX_MCG"></a>

## 62.70 `CONFIG_CLOCK_CONTROL_MCUX_MCG`

**提示（Prompt）**：MCUX MCG 驱动（Driver）

**说明（Help）**

启用 MCUX MCG 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_KINETIS_MCG_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nxp:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nxp#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_MCUX_PCC"></a>

## 62.71 `CONFIG_CLOCK_CONTROL_MCUX_PCC`

**提示（Prompt）**：MCUX PCC 驱动（Driver）

**说明（Help）**

启用 MCUX PCC 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_KINETIS_PCC_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nxp:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nxp#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_MCUX_SCG"></a>

## 62.72 `CONFIG_CLOCK_CONTROL_MCUX_SCG`

**提示（Prompt）**：MCUX SCG 驱动（Driver）

**说明（Help）**

启用 MCUX SCG 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_KINETIS_SCG_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nxp:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nxp#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_MCUX_SCG_K4"></a>

## 62.73 `CONFIG_CLOCK_CONTROL_MCUX_SCG_K4`

**提示（Prompt）**：K4 代 SCG 的 MCUX 驱动（K4 Generation SCG Driver）

**说明（Help）**

启用 SCG K4 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_SCG_K4_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nxp:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nxp#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_MCUX_SIM"></a>

## 62.74 `CONFIG_CLOCK_CONTROL_MCUX_SIM`

**提示（Prompt）**：MCUX SIM 驱动（Driver）

**说明（Help）**

启用 MCUX SIM 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_KINETIS_SIM_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nxp:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nxp#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_MCUX_SYSCON"></a>

## 62.75 `CONFIG_CLOCK_CONTROL_MCUX_SYSCON`

**提示（Prompt）**：MCUX LPC 时钟驱动（Clock Driver）

**说明（Help）**

启用 MCUX 时钟（Clock）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPC_SYSCON_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nxp:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nxp#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_CLOCK_CONTROL_MSPM0"></a>

## 62.76 `CONFIG_CLOCK_CONTROL_MSPM0`

**提示（Prompt）**：TI MSPM0 时钟（Clock）

**说明（Help）**

启用 TI MSPM0 时钟控制使能功能（Clock Control Enabler）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MSPM0_SDK && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.mspm0:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.mspm0#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MSPM0_SDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MSPM0_SDK)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MSPM0_SDK`。

<a id="CONFIG_CLOCK_CONTROL_MT8188_INFRA_AO"></a>

## 62.77 `CONFIG_CLOCK_CONTROL_MT8188_INFRA_AO`

**提示（Prompt）**：联发科 MT8188 基础设施常开时钟控制器（MediaTek Infra Always-On Clock Controller）

**说明（Help）**

启用 MT8188 基础设施常开子系统（Infra Always-On Subsystem）中的外设门控时钟（Peripheral Gate Clocks）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MEDIATEK_MT8188_INFRACFG_AO_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.mtk:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.mtk#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_NPCM"></a>

## 62.78 `CONFIG_CLOCK_CONTROL_NPCM`

**提示（Prompt）**：NPCM 时钟控制器驱动（Clock Controller Driver）

**说明（Help）**

启用 NPCM 时钟控制器（Clock Controller）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NPCM_PCC_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.npcm:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.npcm#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_NPCX"></a>

## 62.79 `CONFIG_CLOCK_CONTROL_NPCX`

**提示（Prompt）**：NPCX 时钟控制器驱动（Clock Controller Driver）

**说明（Help）**

启用 NPCX 时钟控制器（Clock Controller）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NPCX_PCC_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.npcx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.npcx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_NPCX_ESPI_FMCLK_IN_SLEEP"></a>

## 62.80 `CONFIG_CLOCK_CONTROL_NPCX_ESPI_FMCLK_IN_SLEEP`

**提示（Prompt）**：休眠状态下保持 eSPI_SIF 模块的高速时钟（Fast Clock）

**说明（Help）**

启用后，芯片处于休眠（Sleep）或深度休眠（Deep Sleep）电源状态时，eSPI_SIF 模块的高速时钟 `FMCLK` 保持开启。eSPI 虚拟 UART 通道（Virtual UART Channel）需要此时钟；没有 FMCLK 就无法接收主机传输的数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.npcx:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.npcx#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → NPCX 时钟控制器驱动（Clock Controller Driver）

<a id="CONFIG_CLOCK_CONTROL_NPCX_EXTERNAL_SRC"></a>

## 62.81 `CONFIG_CLOCK_CONTROL_NPCX_EXTERNAL_SRC`

**提示（Prompt）**：通过片上晶体振荡器生成低频时钟（LFCLK）

**说明（Help）**

启用后，内部 32.768 kHz 低频时钟（LFCLK）由片上晶体振荡器（Crystal Oscillator，XTOSC）产生。该结构包括片上振荡器，以及连接到它的外部晶体（External Crystal）和相关无源元件（Passive Components）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_NPCX && CONFIG_CLOCK_CONTROL
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.npcx:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.npcx#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → NPCX 时钟控制器驱动（Clock Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NPCX`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NPCX)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_NPCX_SUPP_APB4"></a>

## 62.82 `CONFIG_CLOCK_CONTROL_NPCX_SUPP_APB4`

**提示（Prompt）**：表示时钟控制器支持 APB4 总线（APB4 Bus）

**说明（Help）**

NPCX 系列支持 APB4 总线（Bus）时选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_NPCX && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y if !CONFIG_SOC_SERIES_NPCX7
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.npcx:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.npcx#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → NPCX 时钟控制器驱动（Clock Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NPCX`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NPCX)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_SOC_SERIES_NPCX7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCX7)。

<a id="CONFIG_CLOCK_CONTROL_NPCX_SUPP_FIU1"></a>

## 62.83 `CONFIG_CLOCK_CONTROL_NPCX_SUPP_FIU1`

**提示（Prompt）**：表示时钟控制器支持 FIU1 总线（FIU1 Bus）

**说明（Help）**

NPCX 系列支持 FIU1 总线（Bus）时选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_NPCX && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_SERIES_NPCX4
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.npcx:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.npcx#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → NPCX 时钟控制器驱动（Clock Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NPCX`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NPCX)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_SOC_SERIES_NPCX4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCX4)。

<a id="CONFIG_CLOCK_CONTROL_NRF"></a>

## 62.84 `CONFIG_CLOCK_CONTROL_NRF`

**提示（Prompt）**：nRF 时钟控制器支持（Clock Controller Support）［已弃用，DEPRECATED］

**说明（Help）**

启用 Nordic Semiconductor nRFxx 片上系统（SoC）系列的时钟驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_CLOCK_ENABLED && CONFIG_CLOCK_CONTROL
```

**主动选择（Selects）**

```text
CONFIG_ONOFF
CONFIG_NRFX_CLOCK if !CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT
CONFIG_NRFX_CLOCK_HFCLK if !CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT
CONFIG_NRFX_CLOCK_HFCLK192M if !CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT
CONFIG_NRFX_CLOCK_HFCLKAUDIO if !CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT
CONFIG_NRFX_CLOCK_LFCLK if !CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT
CONFIG_NRFX_CLOCK_LFRC if !CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT
CONFIG_NRFX_CLOCK_XO if !CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT
CONFIG_NRFX_CLOCK_XO24M if !CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_ONOFF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ONOFF)、[`CONFIG_NRFX_CLOCK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_CLOCK)、[`CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT)、[`CONFIG_NRFX_CLOCK_HFCLK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_CLOCK_HFCLK)、[`CONFIG_NRFX_CLOCK_HFCLK192M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_CLOCK_HFCLK192M)、[`CONFIG_NRFX_CLOCK_HFCLKAUDIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_CLOCK_HFCLKAUDIO)、[`CONFIG_NRFX_CLOCK_LFCLK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_CLOCK_LFCLK)、[`CONFIG_NRFX_CLOCK_LFRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_CLOCK_LFRC)、[`CONFIG_NRFX_CLOCK_XO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_CLOCK_XO)、[`CONFIG_NRFX_CLOCK_XO24M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_CLOCK_XO24M)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_CLOCK_CONTROL_NRF54H_HFXO"></a>

## 62.85 `CONFIG_CLOCK_CONTROL_NRF54H_HFXO`

**提示（Prompt）**：NRF54H 高频晶体振荡器驱动支持（HFXO Driver Support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF54H_HFXO_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CLOCK_CONTROL_NRF_COMMON
CONFIG_CLOCK_CONTROL_NRF_ONOFF
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:351`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L351)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_CLOCK_CONTROL_NRF_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_COMMON)、[`CONFIG_CLOCK_CONTROL_NRF_ONOFF`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_ONOFF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CLOCK_CONTROL_NRF_COMMON`。

<a id="CONFIG_CLOCK_CONTROL_NRFS_AUDIOPLL"></a>

## 62.86 `CONFIG_CLOCK_CONTROL_NRFS_AUDIOPLL`

**提示（Prompt）**：NRFS 音频锁相环驱动支持（AudioPLL Driver Support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRFS_AUDIOPLL_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFS
CONFIG_NRFS_AUDIOPLL_SERVICE_ENABLED
CONFIG_CLOCK_CONTROL_NRF_COMMON
CONFIG_CLOCK_CONTROL_NRF_ONOFF
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:335`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L335)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS)、[`CONFIG_NRFS_AUDIOPLL_SERVICE_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS_AUDIOPLL_SERVICE_ENABLED)、[`CONFIG_CLOCK_CONTROL_NRF_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_COMMON)、[`CONFIG_CLOCK_CONTROL_NRF_ONOFF`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_ONOFF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CLOCK_CONTROL_NRF_COMMON`。

<a id="CONFIG_CLOCK_CONTROL_NRFS_LFCLK"></a>

## 62.87 `CONFIG_CLOCK_CONTROL_NRFS_LFCLK`

**提示（Prompt）**：nRF 低频时钟驱动支持（LFCLK Driver Support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRFS_LFCLK_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFS
CONFIG_NRFS_CLOCK_SERVICE_ENABLED
CONFIG_CLOCK_CONTROL_NRF_COMMON
CONFIG_CLOCK_CONTROL_NRF_ONOFF
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:401`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L401)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS)、[`CONFIG_NRFS_CLOCK_SERVICE_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS_CLOCK_SERVICE_ENABLED)、[`CONFIG_CLOCK_CONTROL_NRF_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_COMMON)、[`CONFIG_CLOCK_CONTROL_NRF_ONOFF`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_ONOFF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CLOCK_CONTROL_NRF_COMMON`。

<a id="CONFIG_CLOCK_CONTROL_NRFS_LFCLK_CLOCK_TIMEOUT_MS"></a>

## 62.88 `CONFIG_CLOCK_CONTROL_NRFS_LFCLK_CLOCK_TIMEOUT_MS`

**提示（Prompt）**：等待 NRFS 时钟服务回调的超时，单位为毫秒（Clock Service Callback Timeout）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_NRFS_LFCLK && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:412`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L412)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → nRF 低频时钟驱动支持（LFCLK Driver Support）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRFS_LFCLK`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRFS_LFCLK)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_NRF_ACCURACY_PPM"></a>

## 62.89 `CONFIG_CLOCK_CONTROL_NRF_ACCURACY_PPM`

**提示（Prompt）**：32kHz 时钟精度（Clock Accuracy）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_NRF && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
CONFIG_CLOCK_CONTROL_NRF_K32SRC_500PPM if CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC && CONFIG_SOC_COMPATIBLE_NRF52X
CONFIG_CLOCK_CONTROL_NRF_K32SRC_250PPM if CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC
CONFIG_CLOCK_CONTROL_NRF_K32SRC_50PPM
```

**可选项（Choices）**

```text
CONFIG_CLOCK_CONTROL_NRF_K32SRC_500PPM
CONFIG_CLOCK_CONTROL_NRF_K32SRC_250PPM
CONFIG_CLOCK_CONTROL_NRF_K32SRC_150PPM
CONFIG_CLOCK_CONTROL_NRF_K32SRC_100PPM
CONFIG_CLOCK_CONTROL_NRF_K32SRC_75PPM
CONFIG_CLOCK_CONTROL_NRF_K32SRC_50PPM
CONFIG_CLOCK_CONTROL_NRF_K32SRC_30PPM
CONFIG_CLOCK_CONTROL_NRF_K32SRC_20PPM
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → nRF 时钟控制器支持（Clock Controller Support）［已弃用，DEPRECATED］

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_CLOCK_CONTROL_NRF_K32SRC_500PPM`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_K32SRC_500PPM)、[`CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC)、[`CONFIG_SOC_COMPATIBLE_NRF52X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF52X)、[`CONFIG_CLOCK_CONTROL_NRF_K32SRC_250PPM`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_K32SRC_250PPM)、[`CONFIG_CLOCK_CONTROL_NRF_K32SRC_50PPM`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_K32SRC_50PPM)、[`CONFIG_CLOCK_CONTROL_NRF_K32SRC_150PPM`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_K32SRC_150PPM)、[`CONFIG_CLOCK_CONTROL_NRF_K32SRC_100PPM`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_K32SRC_100PPM)、[`CONFIG_CLOCK_CONTROL_NRF_K32SRC_75PPM`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_K32SRC_75PPM)、[`CONFIG_CLOCK_CONTROL_NRF_K32SRC_30PPM`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_K32SRC_30PPM)、[`CONFIG_CLOCK_CONTROL_NRF_K32SRC_20PPM`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_K32SRC_20PPM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF52X`。

<a id="CONFIG_CLOCK_CONTROL_NRF_AUXPLL"></a>

## 62.90 `CONFIG_CLOCK_CONTROL_NRF_AUXPLL`

**提示（Prompt）**：nRF 辅助锁相环驱动（Auxiliary PLL Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_AUXPLL_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:293`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L293)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_NRF_CALIBRATION_DEBUG"></a>

## 62.91 `CONFIG_CLOCK_CONTROL_NRF_CALIBRATION_DEBUG`

**提示（Prompt）**：校准观测功能（Calibration Instrumentation）

**说明（Help）**

启用获取调试信息（Debug Information）的功能，例如已执行或已跳过的校准次数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_NRF_DRIVER_CALIBRATION && CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC_CALIBRATION && (CONFIG_CLOCK_CONTROL_NRF_LFCLK || CONFIG_CLOCK_CONTROL_NRF) && CONFIG_CLOCK_CONTROL
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:250`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L250)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → 低频时钟校准（LF Clock Calibration）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF_DRIVER_CALIBRATION`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF_DRIVER_CALIBRATION)、[`CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC_CALIBRATION`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC_CALIBRATION)、[`CONFIG_CLOCK_CONTROL_NRF_LFCLK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_LFCLK)、[`CONFIG_CLOCK_CONTROL_NRF`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CLOCK_CONTROL_NRF_LFCLK`。

<a id="CONFIG_CLOCK_CONTROL_NRF_CALIBRATION_LF_ALWAYS_ON"></a>

## 62.92 `CONFIG_CLOCK_CONTROL_NRF_CALIBRATION_LF_ALWAYS_ON`

**提示（Prompt）**：低频时钟始终开启（LF Clock Always On）

**说明（Help）**

如果使用实时时钟（RTC）或全局实时时钟（GRTC）作为系统定时器，则低频时钟（LF Clock）始终开启，因此可以简化处理。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC_CALIBRATION && (CONFIG_CLOCK_CONTROL_NRF_LFCLK || CONFIG_CLOCK_CONTROL_NRF) && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y if CONFIG_NRF_RTC_TIMER || CONFIG_NRF_GRTC_TIMER
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:212`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L212)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → 低频时钟校准（LF Clock Calibration）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC_CALIBRATION`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC_CALIBRATION)、[`CONFIG_CLOCK_CONTROL_NRF_LFCLK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_LFCLK)、[`CONFIG_CLOCK_CONTROL_NRF`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_NRF_RTC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_RTC_TIMER)、[`CONFIG_NRF_GRTC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_GRTC_TIMER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CLOCK_CONTROL_NRF_LFCLK`。

<a id="CONFIG_CLOCK_CONTROL_NRF_CALIBRATION_MAX_SKIP"></a>

## 62.93 `CONFIG_CLOCK_CONTROL_NRF_CALIBRATION_MAX_SKIP`

**提示（Prompt）**：最大连续跳过校准次数（Maximum Calibration Skips）

**说明（Help）**

自上次校准以来，温度变化小于配置阈值时，会跳过校准（Calibration）。连续跳过次数达到配置值时，无条件执行校准。设为 0 表示无论温度如何变化，都定期执行校准。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC_CALIBRATION && (CONFIG_CLOCK_CONTROL_NRF_LFCLK || CONFIG_CLOCK_CONTROL_NRF) && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:230`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L230)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → 低频时钟校准（LF Clock Calibration）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC_CALIBRATION`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC_CALIBRATION)、[`CONFIG_CLOCK_CONTROL_NRF_LFCLK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_LFCLK)、[`CONFIG_CLOCK_CONTROL_NRF`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CLOCK_CONTROL_NRF_LFCLK`。

<a id="CONFIG_CLOCK_CONTROL_NRF_CALIBRATION_PERIOD"></a>

## 62.94 `CONFIG_CLOCK_CONTROL_NRF_CALIBRATION_PERIOD`

**提示（Prompt）**：校准检查周期，单位为毫秒（Calibration Opportunity Period）

**说明（Help）**

周期性执行校准操作（Calibration Action），先测量温度，再校准时钟。如果相对于上一次校准时测得的温度，变化未超过 `CLOCK_CONTROL_NRF_CALIBRATION_TEMP_DIFF`，且连续跳过次数未超过 `CLOCK_CONTROL_NRF_CALIBRATION_MAX_SKIP`，则可以跳过校准。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC_CALIBRATION && (CONFIG_CLOCK_CONTROL_NRF_LFCLK || CONFIG_CLOCK_CONTROL_NRF) && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
4000
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:219`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L219)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → 低频时钟校准（LF Clock Calibration）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC_CALIBRATION`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC_CALIBRATION)、[`CONFIG_CLOCK_CONTROL_NRF_LFCLK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_LFCLK)、[`CONFIG_CLOCK_CONTROL_NRF`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CLOCK_CONTROL_NRF_LFCLK`。

<a id="CONFIG_CLOCK_CONTROL_NRF_CALIBRATION_TEMP_DIFF"></a>

## 62.95 `CONFIG_CLOCK_CONTROL_NRF_CALIBRATION_TEMP_DIFF`

**提示（Prompt）**：触发校准的温度变化，单位为 0.25 度（Calibration Temperature Change）

**说明（Help）**

自上次校准以来，温度变化至少达到此值时触发校准（Calibration）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC_CALIBRATION && (CONFIG_CLOCK_CONTROL_NRF_LFCLK || CONFIG_CLOCK_CONTROL_NRF) && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:241`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L241)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → 低频时钟校准（LF Clock Calibration）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC_CALIBRATION`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC_CALIBRATION)、[`CONFIG_CLOCK_CONTROL_NRF_LFCLK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_LFCLK)、[`CONFIG_CLOCK_CONTROL_NRF`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CLOCK_CONTROL_NRF_LFCLK`。

<a id="CONFIG_CLOCK_CONTROL_NRF_DRIVER_CALIBRATION"></a>

## 62.96 `CONFIG_CLOCK_CONTROL_NRF_DRIVER_CALIBRATION`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用表示由时钟控制（Clock Control）驱动执行校准（Calibration）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT && CONFIG_MULTITHREADING && CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC_CALIBRATION && (CONFIG_CLOCK_CONTROL_NRF_LFCLK || CONFIG_CLOCK_CONTROL_NRF) && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:204`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L204)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → 低频时钟校准（LF Clock Calibration）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT)、[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC_CALIBRATION`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC_CALIBRATION)、[`CONFIG_CLOCK_CONTROL_NRF_LFCLK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_LFCLK)、[`CONFIG_CLOCK_CONTROL_NRF`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CLOCK_CONTROL_NRF_LFCLK`。

<a id="CONFIG_CLOCK_CONTROL_NRF_FLL16M"></a>

## 62.97 `CONFIG_CLOCK_CONTROL_NRF_FLL16M`

**提示（Prompt）**：nRF FLL16M 驱动支持（Driver Support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_FLL16M_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CLOCK_CONTROL_NRF_COMMON
CONFIG_CLOCK_CONTROL_NRF_ONOFF
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:344`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L344)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_CLOCK_CONTROL_NRF_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_COMMON)、[`CONFIG_CLOCK_CONTROL_NRF_ONOFF`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_ONOFF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CLOCK_CONTROL_NRF_COMMON`。

<a id="CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT"></a>

## 62.98 `CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用此选项，可强制使用时钟控制（Clock Control）驱动的另一种实现（Alternative Implementation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_COMPATIBLE_NRF && CONFIG_CLOCK_CONTROL
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_COMPATIBLE_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF`。

<a id="CONFIG_CLOCK_CONTROL_NRF_HFINT_CALIBRATION"></a>

## 62.99 `CONFIG_CLOCK_CONTROL_NRF_HFINT_CALIBRATION`

**提示（Prompt）**：内部高频时钟校准（HFINT Clock Calibration）［实验性，EXPERIMENTAL］

**说明（Help）**

每次启动高频晶体振荡器（HFXO）时，校准内部高频时钟（HFINT）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF54L_HFXO_ENABLED && !CONFIG_TRUSTED_EXECUTION_NONSECURE && (CONFIG_CLOCK_CONTROL_NRF_LFCLK || CONFIG_CLOCK_CONTROL_NRF) && CONFIG_CLOCK_CONTROL
```

**主动选择（Selects）**

```text
CONFIG_CLOCK_CONTROL_NRF_ONOFF
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:268`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L268)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_TRUSTED_EXECUTION_NONSECURE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRUSTED_EXECUTION_NONSECURE)、[`CONFIG_CLOCK_CONTROL_NRF_LFCLK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_LFCLK)、[`CONFIG_CLOCK_CONTROL_NRF`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_CLOCK_CONTROL_NRF_ONOFF`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_ONOFF)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CLOCK_CONTROL_NRF_LFCLK`。

<a id="CONFIG_CLOCK_CONTROL_NRF_HFINT_CALIBRATION_PERIOD"></a>

## 62.100 `CONFIG_CLOCK_CONTROL_NRF_HFINT_CALIBRATION_PERIOD`

**提示（Prompt）**：HFINT 时钟校准周期，单位为毫秒（Calibration Period）

**说明（Help）**

周期性执行内部高频时钟（HFINT）校准：请求高频晶体振荡器（HFXO）时钟并启动实际校准；校准完成后释放 HFXO 时钟。设为 0 可禁用周期性校准，此时只在应用自行启动 HFXO 时进行校准。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_NRF_HFINT_CALIBRATION && (CONFIG_CLOCK_CONTROL_NRF_LFCLK || CONFIG_CLOCK_CONTROL_NRF) && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
60000
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:279`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L279)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → 内部高频时钟校准（HFINT Clock Calibration）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF_HFINT_CALIBRATION`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF_HFINT_CALIBRATION)、[`CONFIG_CLOCK_CONTROL_NRF_LFCLK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_LFCLK)、[`CONFIG_CLOCK_CONTROL_NRF`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CLOCK_CONTROL_NRF_LFCLK`。

<!-- kconfig-navigation -->

[上一章](P061_drivers_charger_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P063_drivers_clock_control_配置项参考_2.md)
