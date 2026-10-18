---
id: learning.zephyr-docs.kconfig-reference.page-145
title: "`drivers/reset`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第145章\_`drivers/reset`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/reset` 的 22 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_RESET"></a>

## 145.1 `CONFIG_RESET`

**提示（Prompt）**：复位控制器驱动（Reset Controller Drivers）

**说明（Help）**

复位控制器驱动。复位节点表示一个包含复位控制器设备信息的区域。典型用法是其他节点的驱动取得复位控制器节点的引用，以及相关复位信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_SR100
CONFIG_SOC_SERIES_M48X
CONFIG_STM32_NEOCHROM_GPU2D
CONFIG_STM32N6_NPU
CONFIG_AUDIO_DMIC_STM32_DFSDM
CONFIG_AUDIO_DMIC_STM32_MDF
CONFIG_CAN_NXP_LPC_MCAN
CONFIG_COMPARATOR_NXP_HSCMP
CONFIG_COUNTER_NXP_MRT
CONFIG_COUNTER_TIMER_STM32
CONFIG_CRYPTO_STM32
CONFIG_SDMMC_STM32
CONFIG_STM32_LTDC
CONFIG_ETH_NUMAKER_DWC_ETHER_1000
CONFIG_ETH_STM32_DWC_ETHER_QOS
CONFIG_ETH_STM32_DWC_ETHER_1000
CONFIG_ETH_ROCKCHIP_DWC_ETHER_QOS
CONFIG_I2C_MCUX_FLEXCOMM
CONFIG_I3C_NPCX
CONFIG_NXP_GINT
CONFIG_IPM_MCUX
CONFIG_MIPI_DSI_STM32
CONFIG_OPAMP_MCUX_OPAMP
CONFIG_PWM_STM32
CONFIG_UART_FOCALTECH
CONFIG_UART_STM32
CONFIG_SPI_MCUX_FLEXCOMM
CONFIG_MCUX_OS_TIMER
CONFIG_VIDEO_STM32_DCMI
CONFIG_VIDEO_STM32_DCMIPP
CONFIG_VIDEO_STM32_JPEG
CONFIG_VIDEO_STM32_VENC
```

**定义位置（Location）**：[`drivers/reset/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/reset/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SR100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SR100)、[`CONFIG_SOC_SERIES_M48X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M48X)、[`CONFIG_STM32_NEOCHROM_GPU2D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STM32_NEOCHROM_GPU2D)、[`CONFIG_STM32N6_NPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STM32N6_NPU)、[`CONFIG_AUDIO_DMIC_STM32_DFSDM`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_STM32_DFSDM)、[`CONFIG_AUDIO_DMIC_STM32_MDF`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_STM32_MDF)、[`CONFIG_CAN_NXP_LPC_MCAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN_NXP_LPC_MCAN)、[`CONFIG_COMPARATOR_NXP_HSCMP`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR_NXP_HSCMP)、[`CONFIG_COUNTER_NXP_MRT`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_NXP_MRT)、[`CONFIG_COUNTER_TIMER_STM32`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_TIMER_STM32)、[`CONFIG_CRYPTO_STM32`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_STM32)、[`CONFIG_SDMMC_STM32`](P076_drivers_disk_配置项参考.md#CONFIG_SDMMC_STM32)、[`CONFIG_STM32_LTDC`](P078_drivers_display_配置项参考_2.md#CONFIG_STM32_LTDC)、[`CONFIG_ETH_NUMAKER_DWC_ETHER_1000`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NUMAKER_DWC_ETHER_1000)、[`CONFIG_ETH_STM32_DWC_ETHER_QOS`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_DWC_ETHER_QOS)、[`CONFIG_ETH_STM32_DWC_ETHER_1000`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_DWC_ETHER_1000)、[`CONFIG_ETH_ROCKCHIP_DWC_ETHER_QOS`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_ROCKCHIP_DWC_ETHER_QOS)、[`CONFIG_I2C_MCUX_FLEXCOMM`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_MCUX_FLEXCOMM)、[`CONFIG_I3C_NPCX`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_NPCX)、[`CONFIG_NXP_GINT`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_NXP_GINT)、[`CONFIG_IPM_MCUX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MCUX)、[`CONFIG_MIPI_DSI_STM32`](P122_drivers_mipi_dsi_配置项参考.md#CONFIG_MIPI_DSI_STM32)、[`CONFIG_OPAMP_MCUX_OPAMP`](P132_drivers_opamp_配置项参考.md#CONFIG_OPAMP_MCUX_OPAMP)、[`CONFIG_PWM_STM32`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_STM32)、[`CONFIG_UART_FOCALTECH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_FOCALTECH)、[`CONFIG_UART_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_STM32)、[`CONFIG_SPI_MCUX_FLEXCOMM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_MCUX_FLEXCOMM)、[`CONFIG_MCUX_OS_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_MCUX_OS_TIMER)、[`CONFIG_VIDEO_STM32_DCMI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_STM32_DCMI)、[`CONFIG_VIDEO_STM32_DCMIPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_STM32_DCMIPP)、[`CONFIG_VIDEO_STM32_JPEG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_STM32_JPEG)、[`CONFIG_VIDEO_STM32_VENC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_STM32_VENC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SR100`。

<a id="CONFIG_RESET_ARM_SCMI"></a>

## 145.2 `CONFIG_RESET_ARM_SCMI`

**提示（Prompt）**：ARM SCMI 复位驱动

**说明（Help）**

启用基于复位域管理协议（Reset Domain Management Protocol）的 ARM SCMI 复位驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_SCMI_RESET_HELPERS && CONFIG_RESET
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/reset/Kconfig.arm_scmi:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/reset/Kconfig.arm_scmi#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 复位控制器驱动（Reset Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SCMI_RESET_HELPERS`](P091_drivers_firmware_配置项参考.md#CONFIG_ARM_SCMI_RESET_HELPERS)、[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)。

<a id="CONFIG_RESET_AST10X0"></a>

## 145.3 `CONFIG_RESET_AST10X0`

**提示（Prompt）**：ASPEED 复位驱动

**说明（Help）**

此选项启用 ASPEED AST10X0 系列 SoC 的复位驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ASPEED_AST10X0_RESET_ENABLED && CONFIG_RESET
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/reset/Kconfig.aspeed:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/reset/Kconfig.aspeed#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 复位控制器驱动（Reset Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)。

<a id="CONFIG_RESET_FOCALTECH_FT9001"></a>

## 145.4 `CONFIG_RESET_FOCALTECH_FT9001`

**提示（Prompt）**：FocalTech FT9001 复位驱动

**说明（Help）**

启用 FocalTech FT9001 SoC 的复位控制驱动。此驱动通过复位控制模块（Reset Control Module）控制外设复位；该模块管理 UART、SPI、I²C、CAN、USB、加密引擎和存储器控制器等片上外设的复位信号。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_FOCALTECH_FT9001_CPM_RCTL_ENABLED && CONFIG_RESET
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/reset/Kconfig.focaltech:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/reset/Kconfig.focaltech#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 复位控制器驱动（Reset Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)。

<a id="CONFIG_RESET_GD32"></a>

## 145.5 `CONFIG_RESET_GD32`

**提示（Prompt）**：GD32 复位驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GD_GD32_RCTL_ENABLED && CONFIG_RESET
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/reset/Kconfig.gd32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/reset/Kconfig.gd32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 复位控制器驱动（Reset Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)。

<a id="CONFIG_RESET_INIT_PRIORITY"></a>

## 145.6 `CONFIG_RESET_INIT_PRIORITY`

**提示（Prompt）**：复位控制器驱动初始化优先级

**说明（Help）**

此选项控制复位控制器设备初始化的优先级。更高的优先级确保设备在启动周期中更早初始化。不确定时，请保持默认值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RESET
```

**默认值（Defaults）**

```text
35
```

**定义位置（Location）**：[`drivers/reset/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/reset/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 复位控制器驱动（Reset Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)。

<a id="CONFIG_RESET_INTEL_SOCFPGA"></a>

## 145.7 `CONFIG_RESET_INTEL_SOCFPGA`

**提示（Prompt）**：Intel SoC FPGA 复位驱动

**说明（Help）**

启用 Intel SoC FPGA 设备的复位驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_SOCFPGA_RESET_ENABLED && CONFIG_RESET
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/reset/Kconfig.intel_socfpga:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/reset/Kconfig.intel_socfpga#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 复位控制器驱动（Reset Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)。

<a id="CONFIG_RESET_MCHP_MSS"></a>

## 145.8 `CONFIG_RESET_MCHP_MSS`

**提示（Prompt）**：Microchip PolarFire SoC 和 PIC64GX 复位驱动

**说明（Help）**

此选项启用 Microchip PolarFire SoC 和 PIC64GX 平台的复位驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_MPFS_RESET_ENABLED && CONFIG_RESET
```

**定义位置（Location）**：[`drivers/reset/Kconfig.mchp_mss:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/reset/Kconfig.mchp_mss#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 复位控制器驱动（Reset Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)。

<a id="CONFIG_RESET_MCHP_RSTC_G1"></a>

## 145.9 `CONFIG_RESET_MCHP_RSTC_G1`

**提示（Prompt）**：Microchip RSTC G1 复位驱动

**说明（Help）**

启用 Microchip G1 的复位驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_RSTC_G1_RESET_ENABLED && CONFIG_RESET
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/reset/Kconfig.mchp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/reset/Kconfig.mchp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 复位控制器驱动（Reset Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)。

<a id="CONFIG_RESET_MMIO"></a>

## 145.10 `CONFIG_RESET_MMIO`

**提示（Prompt）**：通用内存映射 I/O（MMIO）复位驱动

**说明（Help）**

此选项启用通用 MMIO 复位驱动，适用于只需一个内存映射复位位即可退出复位状态的 IP。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RESET_MMIO_ENABLED && CONFIG_RESET
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/reset/Kconfig.mmio:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/reset/Kconfig.mmio#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 复位控制器驱动（Reset Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)。

<a id="CONFIG_RESET_NPCX"></a>

## 145.11 `CONFIG_RESET_NPCX`

**提示（Prompt）**：Nuvoton NPCX 嵌入式控制器（EC）复位驱动

**说明（Help）**

此选项启用 Nuvoton NPCX MCU 的复位控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NPCX_RST_ENABLED && CONFIG_RESET
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/reset/Kconfig.npcx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/reset/Kconfig.npcx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 复位控制器驱动（Reset Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)。

<a id="CONFIG_RESET_NUMAKER"></a>

## 145.12 `CONFIG_RESET_NUMAKER`

**提示（Prompt）**：Nuvoton NuMaker 复位驱动

**说明（Help）**

此选项启用 Nuvoton NuMaker MCU 的复位控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NUMAKER_RST_ENABLED && CONFIG_RESET
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/reset/Kconfig.numaker:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/reset/Kconfig.numaker#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 复位控制器驱动（Reset Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)。

<a id="CONFIG_RESET_NXP_MRCC"></a>

## 145.13 `CONFIG_RESET_NXP_MRCC`

**提示（Prompt）**：NXP MRCC 复位驱动

**说明（Help）**

启用 NXP MRCC 复位控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_MRCC_RESET_ENABLED && CONFIG_RESET
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/reset/Kconfig.nxp_mrcc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/reset/Kconfig.nxp_mrcc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 复位控制器驱动（Reset Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)。

<a id="CONFIG_RESET_NXP_RSTCTL"></a>

## 145.14 `CONFIG_RESET_NXP_RSTCTL`

**提示（Prompt）**：NXP RSTCTL 复位驱动

**说明（Help）**

启用 NXP 外设复位控制器 RSTCTL 的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_RSTCTL_ENABLED && CONFIG_RESET
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/reset/Kconfig.nxp_rstctl:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/reset/Kconfig.nxp_rstctl#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 复位控制器驱动（Reset Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)。

<a id="CONFIG_RESET_NXP_SYSCON"></a>

## 145.15 `CONFIG_RESET_NXP_SYSCON`

**提示（Prompt）**：NXP Syscon 复位驱动

**说明（Help）**

启用 NXP Syscon 复位控制器驱动。Syscon 存在于 LPC 器件及源自 LPC 的器件中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPC_SYSCON_RESET_ENABLED && CONFIG_RESET
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/reset/Kconfig.lpc_syscon:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/reset/Kconfig.lpc_syscon#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 复位控制器驱动（Reset Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)。

<a id="CONFIG_RESET_ROCKCHIP_RK3588"></a>

## 145.16 `CONFIG_RESET_ROCKCHIP_RK3588`

**提示（Prompt）**：Rockchip RK3588 CRU 复位控制器

**说明（Help）**

启用 Rockchip RK3588 CRU 的复位控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ROCKCHIP_RK3588_CRU_RST_ENABLED && CONFIG_RESET
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/reset/Kconfig.rockchip:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/reset/Kconfig.rockchip#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 复位控制器驱动（Reset Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)。

<a id="CONFIG_RESET_RPI_PICO"></a>

## 145.17 `CONFIG_RESET_RPI_PICO`

**提示（Prompt）**：Raspberry Pi 复位驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RASPBERRYPI_PICO_RESET_ENABLED && CONFIG_RESET
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/reset/Kconfig.rpi_pico:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/reset/Kconfig.rpi_pico#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 复位控制器驱动（Reset Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)。

<a id="CONFIG_RESET_RTS5817"></a>

## 145.18 `CONFIG_RESET_RTS5817`

**提示（Prompt）**：RTS5817 复位驱动

**说明（Help）**

此选项启用 RTS5817 复位控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_RTS5817_RESET_ENABLED && CONFIG_RESET
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/reset/Kconfig.rts5817:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/reset/Kconfig.rts5817#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 复位控制器驱动（Reset Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)。

<a id="CONFIG_RESET_SF32LB"></a>

## 145.19 `CONFIG_RESET_SF32LB`

**提示（Prompt）**：SF32LB 复位驱动

**说明（Help）**

启用 SF32LB 复位控制器支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFLI_SF32LB_RCC_RCTL_ENABLED && CONFIG_RESET
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/reset/Kconfig.sf32lb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/reset/Kconfig.sf32lb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 复位控制器驱动（Reset Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)。

<a id="CONFIG_RESET_STM32"></a>

## 145.20 `CONFIG_RESET_STM32`

**提示（Prompt）**：STM32 RCC 复位驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_RCC_RCTL_ENABLED && CONFIG_RESET
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/reset/Kconfig.stm32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/reset/Kconfig.stm32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 复位控制器驱动（Reset Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)。

<a id="CONFIG_RESET_SYNA_SR100"></a>

## 145.21 `CONFIG_RESET_SYNA_SR100`

**提示（Prompt）**：Synaptics SR100 复位驱动

**说明（Help）**

此选项启用 Synaptics SR100 系列 SoC 的复位驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SYNA_SR100_RESET_ENABLED && CONFIG_RESET
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/reset/Kconfig.syna_sr100:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/reset/Kconfig.syna_sr100#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 复位控制器驱动（Reset Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)。

<a id="CONFIG_RESET_WCH_CH32"></a>

## 145.22 `CONFIG_RESET_WCH_CH32`

**提示（Prompt）**：CH32 复位控制器驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WCH_CH32_RCC_RCTL_ENABLED && CONFIG_RESET
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/reset/Kconfig.wch:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/reset/Kconfig.wch#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 复位控制器驱动（Reset Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)。

<!-- kconfig-navigation -->

[上一章](P144_drivers_regulator_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P146_drivers_retained_mem_配置项参考.md)
