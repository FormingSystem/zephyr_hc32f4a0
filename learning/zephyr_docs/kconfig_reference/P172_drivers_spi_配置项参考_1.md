---
id: learning.zephyr-docs.kconfig-reference.page-172
title: "`drivers/spi`配置项参考（1/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第172章\_`drivers/spi`配置项参考（1/2）

本章翻译官方 Kconfig 数据库中 `drivers/spi` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ANDES_SPI_DMA_MODE"></a>

## 172.1 `CONFIG_ANDES_SPI_DMA_MODE`

**提示（Prompt）**：SPI 使用直接内存访问（DMA）模式

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA && CONFIG_SPI_ANDES_ATCSPI200 && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.andes_atcspi200:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.andes_atcspi200#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Andes ATCSPI200 SPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_SPI_ANDES_ATCSPI200`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_ANDES_ATCSPI200)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_DSPI_MCUX_EDMA"></a>

## 172.2 `CONFIG_DSPI_MCUX_EDMA`

**提示（Prompt）**：为 DSPI 驱动启用增强型直接内存访问（EDMA）

**说明（Help）**

为 MCUX DSPI 驱动启用直接内存访问（DMA）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCUX && CONFIG_DMA_MCUX_EDMA && CONFIG_SPI_MCUX_DSPI && CONFIG_SPI
```

**定义位置（Location）**：[`drivers/spi/Kconfig.mcux_dspi:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.mcux_dspi#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → MCUX DSPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)、[`CONFIG_DMA_MCUX_EDMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_MCUX_EDMA)、[`CONFIG_SPI_MCUX_DSPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_MCUX_DSPI)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`。

<a id="CONFIG_EGIS_SPI_DMA_MODE"></a>

## 172.3 `CONFIG_EGIS_SPI_DMA_MODE`

**提示（Prompt）**：SPI 驱动使用直接内存访问（DMA）模式

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA && CONFIG_SPI_EGIS_ET171 && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.egis_et171:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.egis_et171#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → 基于 Andes ATCSPI200 的 Egis ET171 SPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_SPI_EGIS_ET171`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_EGIS_ET171)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_ESP32_SPIM"></a>

## 172.4 `CONFIG_ESP32_SPIM`

**提示（Prompt）**：ESP32 SPI 控制器（Controller）驱动

**说明（Help）**

启用 ESP32 SPI 控制器（Controller）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.esp32:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.esp32#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_ESP32_SPI_TARGET"></a>

## 172.5 `CONFIG_ESP32_SPI_TARGET`

**提示（Prompt）**：ESP32 SPI 目标模式（Target Mode）

**说明（Help）**

启用 ESP32 SPI 驱动的目标模式（Target Mode）。目标事务的时钟由外部控制器提供，因此此模式采用中断驱动，并通过专用目标硬件抽象层（Target HAL）操作 SPI 外设。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_SPIM && CONFIG_SPI
```

**主动选择（Selects）**

```text
CONFIG_SPI_PERIPHERAL
CONFIG_SPI_ESP32_INTERRUPT
```

**定义位置（Location）**：[`drivers/spi/Kconfig.esp32:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.esp32#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → ESP32 SPI 控制器（Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_ESP32_SPIM`](P172_drivers_spi_配置项参考_1.md#CONFIG_ESP32_SPIM)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_SPI_PERIPHERAL`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_PERIPHERAL)、[`CONFIG_SPI_ESP32_INTERRUPT`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_ESP32_INTERRUPT)。

<a id="CONFIG_HEAP_MEM_POOL_ADD_SIZE_SPI_RTS5817"></a>

## 172.6 `CONFIG_HEAP_MEM_POOL_ADD_SIZE_SPI_RTS5817`

**提示（Prompt）**：RTS5817 SPI 控制器驱动所需的堆（Heap）

**说明（Help）**

RTS5817 SPI 控制器驱动通过 `k_aligned_alloc()` 动态分配内存，因此此值应大于或等于应用所需的最大 SPI 缓冲区大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_RTS5817 && CONFIG_SPI
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`drivers/spi/Kconfig.rts5817:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.rts5817#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → RTS5817 SPI 控制器（Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_RTS5817`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RTS5817)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_IFX_SPI_MAX_DATA_WIDTH"></a>

## 172.7 `CONFIG_IFX_SPI_MAX_DATA_WIDTH`

**提示（Prompt）**：最大 SPI 数据宽度（位）

**说明（Help）**

SPI 事务支持的最大数据宽度（Data Width）。PSoC4 器件通常最多支持 16 位，其他器件支持 32 位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_INFINEON_SPI && CONFIG_SPI
```

**默认值（Defaults）**

```text
16 if CONFIG_SOC_FAMILY_INFINEON_PSOC4
32
```

**取值范围（Ranges）**

```text
[4, 32]
```

**定义位置（Location）**：[`drivers/spi/Kconfig.infineon:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.infineon#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_USE_INFINEON_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_SPI)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_IFX_SPI_MIN_DATA_WIDTH"></a>

## 172.8 `CONFIG_IFX_SPI_MIN_DATA_WIDTH`

**提示（Prompt）**：最小 SPI 数据宽度（位）

**说明（Help）**

SPI 事务支持的最小数据宽度（Data Width）。某些器件对最小数据宽度存在硬件限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_INFINEON_SPI && CONFIG_SPI
```

**默认值（Defaults）**

```text
4 if CONFIG_SOC_FAMILY_INFINEON_EDGE || CONFIG_SOC_FAMILY_INFINEON_PSOC4
8
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`drivers/spi/Kconfig.infineon:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.infineon#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_USE_INFINEON_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_SPI)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_IFX_SPI_OVERSAMPLE_DEFAULT"></a>

## 172.9 `CONFIG_IFX_SPI_OVERSAMPLE_DEFAULT`

**提示（Prompt）**：默认 SPI 过采样值（Oversample Value）

**说明（Help）**

生成 SPI 时钟时使用的默认过采样值（Oversample Value）。较高的值可提高时钟准确性，但会降低最大频率。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_INFINEON_SPI && CONFIG_SPI
```

**默认值（Defaults）**

```text
16 if CONFIG_SOC_FAMILY_INFINEON_PSOC4
4
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`drivers/spi/Kconfig.infineon:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.infineon#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_USE_INFINEON_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_SPI)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_MCUX_DSPI_BUFFER_SIZE"></a>

## 172.10 `CONFIG_MCUX_DSPI_BUFFER_SIZE`

**提示（Prompt）**：缓冲区大小（Buffer Size）

**说明（Help）**

数据缓冲区大小（Data Buffer Size）

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DSPI_MCUX_EDMA && CONFIG_SPI_MCUX_DSPI && CONFIG_SPI
```

**默认值（Defaults）**

```text
144
```

**定义位置（Location）**：[`drivers/spi/Kconfig.mcux_dspi:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.mcux_dspi#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → MCUX DSPI 驱动 → 为 DSPI 驱动启用增强型直接内存访问（EDMA）

**配置项引用（Symbol References）**：[`CONFIG_DSPI_MCUX_EDMA`](P172_drivers_spi_配置项参考_1.md#CONFIG_DSPI_MCUX_EDMA)、[`CONFIG_SPI_MCUX_DSPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_MCUX_DSPI)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_MCUX_DSPI_EDMA_SHUFFLE_DATA"></a>

## 172.11 `CONFIG_MCUX_DSPI_EDMA_SHUFFLE_DATA`

**提示（Prompt）**：使用内部数据处理（Internal Data Process）

**说明（Help）**

发送（TX）数据需要添加命令前缀，用户可以选择不使用此功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DSPI_MCUX_EDMA && CONFIG_SPI_MCUX_DSPI && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.mcux_dspi:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.mcux_dspi#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → MCUX DSPI 驱动 → 为 DSPI 驱动启用增强型直接内存访问（EDMA）

**配置项引用（Symbol References）**：[`CONFIG_DSPI_MCUX_EDMA`](P172_drivers_spi_配置项参考_1.md#CONFIG_DSPI_MCUX_EDMA)、[`CONFIG_SPI_MCUX_DSPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_MCUX_DSPI)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_NXP_S32_SPI"></a>

## 172.12 `CONFIG_NXP_S32_SPI`

**提示（Prompt）**：NXP S32 SPI 驱动

**说明（Help）**

启用 NXP S32 SPI 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_S32_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_NOCACHE_MEMORY if CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT
```

**定义位置（Location）**：[`drivers/spi/Kconfig.nxp_s32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.nxp_s32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_NXP_S32_SPI_INTERRUPT"></a>

## 172.13 `CONFIG_NXP_S32_SPI_INTERRUPT`

**提示（Prompt）**：NXP S32 SPI 中断支持（Interrupt Support）

**说明（Help）**

启用 SPI 通信的中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_S32_SPI && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.nxp_s32:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.nxp_s32#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → NXP S32 SPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_NXP_S32_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_NXP_S32_SPI)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI"></a>

## 172.14 `CONFIG_SPI`

**提示（Prompt）**：串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**说明（Help）**

启用 SPI 硬件总线支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_NRF70_ON_SPI
CONFIG_NRF70_ON_SPI
CONFIG_SHIELD_ADI_LSMSPG
CONFIG_ADC_AD405X
CONFIG_ADC_AD4114
CONFIG_ADC_AD4130
CONFIG_ADC_AD4170
CONFIG_ADC_AD7124
CONFIG_ADC_ADC124S021
CONFIG_ADC_ADE7913
CONFIG_ADC_ADS1220
CONFIG_ADC_ADS131M02
CONFIG_ADC_ADS1X4S0X
CONFIG_ADC_ADS7052
CONFIG_ADC_ADS79XX
CONFIG_ADC_LMP90XXX
CONFIG_ADC_MAX11102_17
CONFIG_ADC_MAX1125X
CONFIG_ADC_MAX2253X
CONFIG_ADC_MCP320X
CONFIG_ADC_MCP356XR
CONFIG_ADC_ADS1118
CONFIG_AUDIO_CODEC_CS35LXX_SPI
CONFIG_AUDIO_CODEC_PCM1681
CONFIG_AUDIO_CODEC_TLV320AIC26
CONFIG_AUXDISPLAY_PT6314
CONFIG_BT_SPI
CONFIG_BT_AMBIQ_HCI
CONFIG_CAN_MCP2515
CONFIG_CAN_MCP251XFD
CONFIG_CAN_TCAN4X5X
CONFIG_DAC_AD5529R
CONFIG_DAC_AD56X1
CONFIG_DAC_AD56XX
CONFIG_DAC_DAC161S997
CONFIG_DAC_DACX0508
CONFIG_DAC_DACX311
CONFIG_DAC_DACX3508
CONFIG_DAC_LTC166X
CONFIG_HUB12
CONFIG_IT8951
CONFIG_LPM013M126
CONFIG_LS0XX
CONFIG_LT7680
CONFIG_MAX7219
CONFIG_EEPROM_AT25
CONFIG_EEPROM_MB85RSXX
CONFIG_EEPROM_FM25XXX
CONFIG_ENTROPY_MAXQ10XX_RNG
CONFIG_ETH_ADIN1140
CONFIG_ETH_ADIN2111
CONFIG_ETH_DM9051
CONFIG_ETH_ENC28J60
CONFIG_ETH_ENC424J600
CONFIG_ETH_LAN865X
CONFIG_ETH_LAN9250
CONFIG_ETH_W5100S
CONFIG_ETH_W5500
CONFIG_ETH_W6100
CONFIG_ETH_W6300
CONFIG_SPI_FLASH_AT25XV021A
CONFIG_SPI_FLASH_AT45
CONFIG_SPI_NAND
CONFIG_SPI_NOR
CONFIG_FLASH_S3AXX04
CONFIG_SLG47910_FPGA
CONFIG_HAPTICS_CS40LXX_SPI
CONFIG_IEEE802154_DW1000
CONFIG_IEEE802154_MCR20A
CONFIG_IEEE802154_RF2XX
CONFIG_INPUT_PAW32XX
CONFIG_INPUT_PMW3610
CONFIG_INPUT_XPT2046
CONFIG_LED_SCT2024
CONFIG_LPD880X_STRIP
CONFIG_LORA_SX127X
CONFIG_LORA_SX126X
CONFIG_LORA_STM32WL_SUBGHZ_RADIO
CONFIG_LORA_LR11XX_NATIVE
CONFIG_LORA_SX126X_NATIVE
CONFIG_MIPI_DBI_SPI
CONFIG_FT800
CONFIG_TMC6460_SPI
CONFIG_MUX_ADI_ADGM3121
CONFIG_RTC_DS1302
CONFIG_RTC_PCF2123
CONFIG_SPI_SDHC
CONFIG_AD2S1210
CONFIG_ADE7978
CONFIG_ADIS1647X
CONFIG_ADT7310
CONFIG_ADXL362
CONFIG_ADXL367
CONFIG_AMS_AS5048
CONFIG_BMI08X
CONFIG_BMP388
CONFIG_AFBR_S50
CONFIG_MAX31855
CONFIG_MAX31865
CONFIG_MAX6675
CONFIG_PAA3905
CONFIG_PAT9136
CONFIG_I3G4250D
CONFIG_IIS3DHHC
CONFIG_IIS3DWB
CONFIG_LIS2DUX12
CONFIG_LPS2XDF
CONFIG_LSM6DSO
CONFIG_LSM6DSV16X
CONFIG_LSM6DSVXXX
CONFIG_ICM42605
CONFIG_ICM4268X
CONFIG_ICM42X70
CONFIG_ICM45686
CONFIG_ICM566XX
CONFIG_TMAG5170
CONFIG_HX711_SPI
CONFIG_STEPPER_ADI_TMC_SPI
CONFIG_UHC_MAX3421E
CONFIG_VIDEO_ARDUCAM_MEGA
CONFIG_WDT_NXP_FS26
CONFIG_WIFI_ESP_HOSTED
CONFIG_WIFI_ESWIFI_BUS_SPI
CONFIG_WIFI_ST67W611M1
CONFIG_WIFI_WINC1500
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_m2_ieee802154/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_ieee802154/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/openthread_rcp_arduino/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/openthread_rcp_arduino/Kconfig.defconfig)。

```text
y if CONFIG_SHIELD_OPENTHREAD_RCP_ARDUINO_SPI
```

**定义位置（Location）**：[`drivers/spi/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_NRF70_ON_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF70_ON_SPI)、[`CONFIG_SHIELD_ADI_LSMSPG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHIELD_ADI_LSMSPG)、[`CONFIG_ADC_AD405X`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_AD405X)、[`CONFIG_ADC_AD4114`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_AD4114)、[`CONFIG_ADC_AD4130`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_AD4130)、[`CONFIG_ADC_AD4170`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_AD4170)、[`CONFIG_ADC_AD7124`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_AD7124)、[`CONFIG_ADC_ADC124S021`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADC124S021)、[`CONFIG_ADC_ADE7913`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADE7913)、[`CONFIG_ADC_ADS1220`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS1220)、[`CONFIG_ADC_ADS131M02`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS131M02)、[`CONFIG_ADC_ADS1X4S0X`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS1X4S0X)、[`CONFIG_ADC_ADS7052`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS7052)、[`CONFIG_ADC_ADS79XX`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS79XX)、[`CONFIG_ADC_LMP90XXX`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_LMP90XXX)、[`CONFIG_ADC_MAX11102_17`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_MAX11102_17)、[`CONFIG_ADC_MAX1125X`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MAX1125X)、[`CONFIG_ADC_MAX2253X`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MAX2253X)、[`CONFIG_ADC_MCP320X`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MCP320X)、[`CONFIG_ADC_MCP356XR`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MCP356XR)、[`CONFIG_ADC_ADS1118`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS1118)、[`CONFIG_AUDIO_CODEC_CS35LXX_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AUDIO_CODEC_CS35LXX_SPI)、[`CONFIG_AUDIO_CODEC_PCM1681`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC_PCM1681)、[`CONFIG_AUDIO_CODEC_TLV320AIC26`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC_TLV320AIC26)、[`CONFIG_AUXDISPLAY_PT6314`](P051_drivers_auxdisplay_配置项参考.md#CONFIG_AUXDISPLAY_PT6314)、[`CONFIG_BT_SPI`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SPI)、[`CONFIG_BT_AMBIQ_HCI`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_AMBIQ_HCI)、[`CONFIG_CAN_MCP2515`](P060_drivers_can_配置项参考.md#CONFIG_CAN_MCP2515)、[`CONFIG_CAN_MCP251XFD`](P060_drivers_can_配置项参考.md#CONFIG_CAN_MCP251XFD)、[`CONFIG_CAN_TCAN4X5X`](P060_drivers_can_配置项参考.md#CONFIG_CAN_TCAN4X5X)、[`CONFIG_DAC_AD5529R`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_AD5529R)、[`CONFIG_DAC_AD56X1`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_AD56X1)、[`CONFIG_DAC_AD56XX`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_AD56XX)、[`CONFIG_DAC_DAC161S997`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_DAC161S997)、[`CONFIG_DAC_DACX0508`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_DACX0508)、[`CONFIG_DAC_DACX311`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_DACX311)、[`CONFIG_DAC_DACX3508`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_DACX3508)、[`CONFIG_DAC_LTC166X`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_LTC166X)、[`CONFIG_HUB12`](P077_drivers_display_配置项参考_1.md#CONFIG_HUB12)、[`CONFIG_IT8951`](P077_drivers_display_配置项参考_1.md#CONFIG_IT8951)、[`CONFIG_LPM013M126`](P077_drivers_display_配置项参考_1.md#CONFIG_LPM013M126)、[`CONFIG_LS0XX`](P077_drivers_display_配置项参考_1.md#CONFIG_LS0XX)、[`CONFIG_LT7680`](P077_drivers_display_配置项参考_1.md#CONFIG_LT7680)、[`CONFIG_MAX7219`](P077_drivers_display_配置项参考_1.md#CONFIG_MAX7219)、[`CONFIG_EEPROM_AT25`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM_AT25)、[`CONFIG_EEPROM_MB85RSXX`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM_MB85RSXX)、[`CONFIG_EEPROM_FM25XXX`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM_FM25XXX)、[`CONFIG_ENTROPY_MAXQ10XX_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_MAXQ10XX_RNG)、[`CONFIG_ETH_ADIN1140`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ADIN1140)、[`CONFIG_ETH_ADIN2111`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ADIN2111)、[`CONFIG_ETH_DM9051`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DM9051)、[`CONFIG_ETH_ENC28J60`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ENC28J60)、[`CONFIG_ETH_ENC424J600`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ENC424J600)、[`CONFIG_ETH_LAN865X`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_LAN865X)、[`CONFIG_ETH_LAN9250`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_LAN9250)、[`CONFIG_ETH_W5100S`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_W5100S)、[`CONFIG_ETH_W5500`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_W5500)、[`CONFIG_ETH_W6100`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_W6100)、[`CONFIG_ETH_W6300`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_W6300)、[`CONFIG_SPI_FLASH_AT25XV021A`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_FLASH_AT25XV021A)、[`CONFIG_SPI_FLASH_AT45`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_FLASH_AT45)、[`CONFIG_SPI_NAND`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_NAND)、[`CONFIG_SPI_NOR`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_NOR)、[`CONFIG_FLASH_S3AXX04`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_S3AXX04)、[`CONFIG_SLG47910_FPGA`](P095_drivers_fpga_配置项参考.md#CONFIG_SLG47910_FPGA)、[`CONFIG_HAPTICS_CS40LXX_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAPTICS_CS40LXX_SPI)、[`CONFIG_IEEE802154_DW1000`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_DW1000)、[`CONFIG_IEEE802154_MCR20A`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_MCR20A)、[`CONFIG_IEEE802154_RF2XX`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_RF2XX)、[`CONFIG_INPUT_PAW32XX`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_PAW32XX)、[`CONFIG_INPUT_PMW3610`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_PMW3610)、[`CONFIG_INPUT_XPT2046`](P112_drivers_input_配置项参考_2.md#CONFIG_INPUT_XPT2046)、[`CONFIG_LED_SCT2024`](P114_drivers_led_配置项参考.md#CONFIG_LED_SCT2024)、[`CONFIG_LPD880X_STRIP`](P115_drivers_led_strip_配置项参考.md#CONFIG_LPD880X_STRIP)、[`CONFIG_LORA_SX127X`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_SX127X)、[`CONFIG_LORA_SX126X`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_SX126X)、[`CONFIG_LORA_STM32WL_SUBGHZ_RADIO`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_STM32WL_SUBGHZ_RADIO)、[`CONFIG_LORA_LR11XX_NATIVE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_LR11XX_NATIVE)、[`CONFIG_LORA_SX126X_NATIVE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_SX126X_NATIVE)、[`CONFIG_MIPI_DBI_SPI`](P121_drivers_mipi_dbi_配置项参考.md#CONFIG_MIPI_DBI_SPI)、[`CONFIG_FT800`](P123_drivers_misc_配置项参考.md#CONFIG_FT800)、[`CONFIG_TMC6460_SPI`](P123_drivers_misc_配置项参考.md#CONFIG_TMC6460_SPI)、[`CONFIG_MUX_ADI_ADGM3121`](P130_drivers_mux_配置项参考.md#CONFIG_MUX_ADI_ADGM3121)、[`CONFIG_RTC_DS1302`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_DS1302)、[`CONFIG_RTC_PCF2123`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_PCF2123)、[`CONFIG_SPI_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SPI_SDHC)、[`CONFIG_AD2S1210`](P149_drivers_sensor_配置项参考_1.md#CONFIG_AD2S1210)、[`CONFIG_ADE7978`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADE7978)、[`CONFIG_ADIS1647X`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADIS1647X)、[`CONFIG_ADT7310`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADT7310)、[`CONFIG_ADXL362`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL362)、[`CONFIG_ADXL367`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL367)、[`CONFIG_AMS_AS5048`](P150_drivers_sensor_配置项参考_2.md#CONFIG_AMS_AS5048)、[`CONFIG_BMI08X`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMI08X)、[`CONFIG_BMP388`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMP388)、[`CONFIG_AFBR_S50`](P150_drivers_sensor_配置项参考_2.md#CONFIG_AFBR_S50)、[`CONFIG_MAX31855`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX31855)、[`CONFIG_MAX31865`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX31865)、[`CONFIG_MAX6675`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MAX6675)、[`CONFIG_PAA3905`](P160_drivers_sensor_配置项参考_12.md#CONFIG_PAA3905)、[`CONFIG_PAT9136`](P160_drivers_sensor_配置项参考_12.md#CONFIG_PAT9136)、[`CONFIG_I3G4250D`](P154_drivers_sensor_配置项参考_6.md#CONFIG_I3G4250D)、[`CONFIG_IIS3DHHC`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS3DHHC)、[`CONFIG_IIS3DWB`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS3DWB)、[`CONFIG_LIS2DUX12`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DUX12)、[`CONFIG_LPS2XDF`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LPS2XDF)、[`CONFIG_LSM6DSO`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO)、[`CONFIG_LSM6DSV16X`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSV16X)、[`CONFIG_LSM6DSVXXX`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM6DSVXXX)、[`CONFIG_ICM42605`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM42605)、[`CONFIG_ICM4268X`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM4268X)、[`CONFIG_ICM42X70`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM42X70)、[`CONFIG_ICM45686`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM45686)、[`CONFIG_ICM566XX`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM566XX)、[`CONFIG_TMAG5170`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TMAG5170)、[`CONFIG_HX711_SPI`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HX711_SPI)、[`CONFIG_STEPPER_ADI_TMC_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STEPPER_ADI_TMC_SPI)、[`CONFIG_UHC_MAX3421E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UHC_MAX3421E)、[`CONFIG_VIDEO_ARDUCAM_MEGA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_ARDUCAM_MEGA)、[`CONFIG_WDT_NXP_FS26`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WDT_NXP_FS26)、[`CONFIG_WIFI_ESP_HOSTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP_HOSTED)、[`CONFIG_WIFI_ESWIFI_BUS_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESWIFI_BUS_SPI)、[`CONFIG_WIFI_ST67W611M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ST67W611M1)、[`CONFIG_WIFI_WINC1500`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_WINC1500)、[`CONFIG_SHIELD_OPENTHREAD_RCP_ARDUINO_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHIELD_OPENTHREAD_RCP_ARDUINO_SPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NRF70_ON_SPI`、`CONFIG_SHIELD_ADI_LSMSPG`、`CONFIG_AUDIO_CODEC_CS35LXX_SPI`、`CONFIG_HAPTICS_CS40LXX_SPI`、`CONFIG_SHIELD_OPENTHREAD_RCP_ARDUINO_SPI`。

<a id="CONFIG_SPI_AMBIQ_BLEIF"></a>

## 172.15 `CONFIG_SPI_AMBIQ_BLEIF`

**提示（Prompt）**：AMBIQ SPI-BLEIF 驱动

**说明（Help）**

为 Ambiq Apollox Blue 片上系统（SoC，例如 Apollo3 Blue）启用驱动。它使用内部设计的 BLEIF 模块进行 SPI 收发，该模块不同于通用 IOM 模块，始终用于蓝牙主机控制器接口（Bluetooth HCI）通信。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMBIQ_SPI_BLEIF_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_AMBIQ_HAL
CONFIG_AMBIQ_HAL_USE_BLEIF
```

**定义位置（Location）**：[`drivers/spi/Kconfig.ambiq:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.ambiq#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_AMBIQ_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL)、[`CONFIG_AMBIQ_HAL_USE_BLEIF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL_USE_BLEIF)。

<a id="CONFIG_SPI_AMBIQ_BLEIF_TIMING_TRACE"></a>

## 172.16 `CONFIG_SPI_AMBIQ_BLEIF_TIMING_TRACE`

**提示（Prompt）**：Ambiq SPI-BLEIF 时序跟踪（Timing Trace）

**说明（Help）**

SPI 收发引脚没有从芯片引出，用户无需配置。不过，芯片在其他已引出的引脚上提供了可配置的 BLEIF 时序观测功能。用户可以启用此选项，配置这些引脚以进行时序跟踪（Timing Trace）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_AMBIQ_BLEIF && CONFIG_SPI
```

**定义位置（Location）**：[`drivers/spi/Kconfig.ambiq:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.ambiq#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → AMBIQ SPI-BLEIF 驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_AMBIQ_BLEIF`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_AMBIQ_BLEIF)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_AMBIQ_HANDLE_CACHE"></a>

## 172.17 `CONFIG_SPI_AMBIQ_HANDLE_CACHE`

**提示（Prompt）**：在 SPI 驱动中启用缓存处理（Cache Handling）

**说明（Help）**

如果上层已处理缓存（Cache），则禁用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CACHE_MANAGEMENT && CONFIG_DCACHE && CONFIG_SPI_AMBIQ_SPIC && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.ambiq:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.ambiq#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → AMBIQ SPI 控制器（Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_SPI_AMBIQ_SPIC`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_AMBIQ_SPIC)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_AMBIQ_SPIC"></a>

## 172.18 `CONFIG_SPI_AMBIQ_SPIC`

**提示（Prompt）**：AMBIQ SPI 控制器（Controller）驱动

**说明（Help）**

启用 Ambiq SPI 控制器模式（Controller Mode）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMBIQ_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
CONFIG_AMBIQ_HAL
CONFIG_AMBIQ_HAL_USE_SPIC
```

**定义位置（Location）**：[`drivers/spi/Kconfig.ambiq:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.ambiq#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_AMBIQ_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL)、[`CONFIG_AMBIQ_HAL_USE_SPIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL_USE_SPIC)。

<a id="CONFIG_SPI_AMBIQ_SPID"></a>

## 172.19 `CONFIG_SPI_AMBIQ_SPID`

**提示（Prompt）**：AMBIQ SPI 设备（Device）驱动

**说明（Help）**

启用 Ambiq SPI 设备模式（Device Mode）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMBIQ_SPID_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
CONFIG_AMBIQ_HAL
CONFIG_AMBIQ_HAL_USE_SPID
```

**定义位置（Location）**：[`drivers/spi/Kconfig.ambiq:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.ambiq#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_AMBIQ_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL)、[`CONFIG_AMBIQ_HAL_USE_SPID`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL_USE_SPID)。

<a id="CONFIG_SPI_AMEBA"></a>

## 172.20 `CONFIG_SPI_AMEBA`

**提示（Prompt）**：AMEBA SPI 驱动

**说明（Help）**

启用 AMEBA SPI 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_AMEBA_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/spi/Kconfig.ameba:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.ameba#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SPI_AMEBA_DMA"></a>

## 172.21 `CONFIG_SPI_AMEBA_DMA`

**提示（Prompt）**：AMEBA SPI 直接内存访问（DMA）支持

**说明（Help）**

启用 SPI 直接内存访问（DMA）模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SPI_AMEBA_OPERATION_MODE>
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/spi/Kconfig.ameba:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.ameba#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → AMEBA SPI 驱动 → AMEBA SPI 工作模式（Operation Mode）

**配置项引用（Symbol References）**：[`CONFIG_SPI_AMEBA_OPERATION_MODE`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_AMEBA_OPERATION_MODE)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_SPI_AMEBA_INTERRUPT"></a>

## 172.22 `CONFIG_SPI_AMEBA_INTERRUPT`

**提示（Prompt）**：AMEBA SPI 中断模式（Interrupt Mode）

**说明（Help）**

启用 AMEBA SPI 驱动的中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SPI_AMEBA_OPERATION_MODE>
```

**定义位置（Location）**：[`drivers/spi/Kconfig.ameba:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.ameba#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → AMEBA SPI 驱动 → AMEBA SPI 工作模式（Operation Mode）

**配置项引用（Symbol References）**：[`CONFIG_SPI_AMEBA_OPERATION_MODE`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_AMEBA_OPERATION_MODE)。

<a id="CONFIG_SPI_AMEBA_OPERATION_MODE"></a>

## 172.23 `CONFIG_SPI_AMEBA_OPERATION_MODE`

**提示（Prompt）**：AMEBA SPI 工作模式（Operation Mode）

**说明（Help）**

选择 AMEBA SPI 驱动的工作模式（Operation Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_AMEBA && CONFIG_SPI
```

**默认值（Defaults）**

```text
CONFIG_SPI_AMEBA_POLLING
```

**可选项（Choices）**

```text
CONFIG_SPI_AMEBA_INTERRUPT
CONFIG_SPI_AMEBA_DMA
CONFIG_SPI_AMEBA_POLLING
```

**定义位置（Location）**：[`drivers/spi/Kconfig.ameba:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.ameba#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → AMEBA SPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_AMEBA`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_AMEBA)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_SPI_AMEBA_POLLING`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_AMEBA_POLLING)、[`CONFIG_SPI_AMEBA_INTERRUPT`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_AMEBA_INTERRUPT)、[`CONFIG_SPI_AMEBA_DMA`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_AMEBA_DMA)。

<a id="CONFIG_SPI_AMEBA_POLLING"></a>

## 172.24 `CONFIG_SPI_AMEBA_POLLING`

**提示（Prompt）**：AMEBA SPI 轮询模式（Polling Mode）

**说明（Help）**

启用 SPI 轮询模式（Polling Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SPI_AMEBA_OPERATION_MODE>
```

**定义位置（Location）**：[`drivers/spi/Kconfig.ameba:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.ameba#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → AMEBA SPI 驱动 → AMEBA SPI 工作模式（Operation Mode）

**配置项引用（Symbol References）**：[`CONFIG_SPI_AMEBA_OPERATION_MODE`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_AMEBA_OPERATION_MODE)。

<a id="CONFIG_SPI_ANDES_ATCSPI200"></a>

## 172.25 `CONFIG_SPI_ANDES_ATCSPI200`

**提示（Prompt）**：Andes ATCSPI200 SPI 驱动

**说明（Help）**

启用 Andes ATCSPI200 SPI 控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ANDESTECH_ATCSPI200_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.andes_atcspi200:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.andes_atcspi200#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_ASYNC"></a>

## 172.26 `CONFIG_SPI_ASYNC`

**提示（Prompt）**：异步调用支持（Asynchronous Call Support）

**说明（Help）**

启用异步 API 调用（Asynchronous API Calls）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MULTITHREADING && CONFIG_SPI
```

**主动选择（Selects）**

```text
CONFIG_POLL
```

**被选择（Selected by）**

```text
CONFIG_MCUMGR_TRANSPORT_SPI
```

**定义位置（Location）**：[`drivers/spi/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_POLL`](P002_kernel_配置项参考_2.md#CONFIG_POLL)、[`CONFIG_MCUMGR_TRANSPORT_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_SPI)。

<a id="CONFIG_SPI_BEE"></a>

## 172.27 `CONFIG_SPI_BEE`

**提示（Prompt）**：Realtek Bee 系列 SPI 驱动

**说明（Help）**

此选项为 Realtek Bee 片上系统（SoC）启用 SPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_BEE_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAL_REALTEK_BEE_SPI
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/spi/Kconfig.bee:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.bee#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_HAL_REALTEK_BEE_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAL_REALTEK_BEE_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAL_REALTEK_BEE_SPI`。

<a id="CONFIG_SPI_BEE_DMA"></a>

## 172.28 `CONFIG_SPI_BEE_DMA`

**提示（Prompt）**：BEE MCU SPI 直接内存访问（DMA）支持

**说明（Help）**

启用 SPI 的 DMA 驱动模式（DMA-driven Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_BEE && CONFIG_SPI
```

**主动选择（Selects）**

```text
CONFIG_DMA
CONFIG_SPI_BEE_INTERRUPT
CONFIG_HAL_REALTEK_BEE_DMA
```

**定义位置（Location）**：[`drivers/spi/Kconfig.bee:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.bee#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Realtek Bee 系列 SPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_BEE`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_BEE)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_SPI_BEE_INTERRUPT`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_BEE_INTERRUPT)、[`CONFIG_HAL_REALTEK_BEE_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAL_REALTEK_BEE_DMA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAL_REALTEK_BEE_DMA`。

<a id="CONFIG_SPI_BEE_DMA_BUF_COUNT"></a>

## 172.29 `CONFIG_SPI_BEE_DMA_BUF_COUNT`

**提示（Prompt）**：DMA 缓冲区内存块池（Memory Slab）的块数

**说明（Help）**

内存块池（Memory Slab）中的块数，应足以容纳所有已启用 SPI 实例的并发发送／接收（TX/RX）操作。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_BEE_DMA && CONFIG_SPI_BEE_DMA && CONFIG_SPI_BEE && CONFIG_SPI
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/spi/Kconfig.bee:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.bee#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Realtek Bee 系列 SPI 驱动 → BEE MCU SPI 直接内存访问（DMA）支持

**配置项引用（Symbol References）**：[`CONFIG_SPI_BEE_DMA`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_BEE_DMA)、[`CONFIG_SPI_BEE`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_BEE)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_BEE_DMA_BUF_SIZE"></a>

## 172.30 `CONFIG_SPI_BEE_DMA_BUF_SIZE`

**提示（Prompt）**：DMA 缓冲区内存块池的块大小

**说明（Help）**

用于 DMA 占位缓冲区（Dummy Buffer）的内存块池（Memory Slab）中，每个块的大小，单位为字节。用户缓冲区为 `NULL` 时使用这些缓冲区。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_BEE_DMA && CONFIG_SPI_BEE_DMA && CONFIG_SPI_BEE && CONFIG_SPI
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/spi/Kconfig.bee:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.bee#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Realtek Bee 系列 SPI 驱动 → BEE MCU SPI 直接内存访问（DMA）支持

**配置项引用（Symbol References）**：[`CONFIG_SPI_BEE_DMA`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_BEE_DMA)、[`CONFIG_SPI_BEE`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_BEE)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_BEE_INTERRUPT"></a>

## 172.31 `CONFIG_SPI_BEE_INTERRUPT`

**提示（Prompt）**：BEE MCU SPI 中断支持（Interrupt Support）

**说明（Help）**

启用 SPI 的中断驱动模式（Interrupt-driven Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_BEE && CONFIG_SPI
```

**默认值（Defaults）**

```text
y if CONFIG_SPI_ASYNC
```

**被选择（Selected by）**

```text
CONFIG_SPI_BEE_DMA
```

**定义位置（Location）**：[`drivers/spi/Kconfig.bee:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.bee#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Realtek Bee 系列 SPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_BEE`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_BEE)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_SPI_ASYNC`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_ASYNC)、[`CONFIG_SPI_BEE_DMA`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_BEE_DMA)。

<a id="CONFIG_SPI_BFLB"></a>

## 172.32 `CONFIG_SPI_BFLB`

**提示（Prompt）**：Bouffalolab SPI 驱动

**说明（Help）**

启用 Bouffalolab SPI 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.bflb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.bflb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_BITBANG"></a>

## 172.33 `CONFIG_SPI_BITBANG`

**提示（Prompt）**：软件模拟 SPI 控制器（Bitbang SPI Controller）驱动

**说明（Help）**

启用软件模拟 SPI 控制器（Bitbang SPI Controller）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_SPI_BITBANG_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.bitbang:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.bitbang#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_B_DMAC"></a>

## 172.34 `CONFIG_SPI_B_DMAC`

**提示（Prompt）**：RA MCU SPI 直接内存访问控制器（DMAC）支持

**说明（Help）**

为 RA8 系列的 SPI B 驱动启用直接内存访问控制器（Direct Memory Access Controller，DMAC）支持，使用 FSP 传输模块 `g_transfer_on_dmac` 执行 SPI 数据传输。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_RENESAS_RA8 && CONFIG_SPI
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_SPI_B_INTERRUPT
CONFIG_USE_RA_FSP_DMA
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_ra8:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_ra8#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Renesas RA SPI B

**配置项引用（Symbol References）**：[`CONFIG_SPI_RENESAS_RA8`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RA8)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_SPI_B_INTERRUPT`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_B_INTERRUPT)、[`CONFIG_USE_RA_FSP_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_DMA)。

<a id="CONFIG_SPI_B_INTERRUPT"></a>

## 172.35 `CONFIG_SPI_B_INTERRUPT`

**提示（Prompt）**：RA MCU SPI B 中断支持（Interrupt Support）

**说明（Help）**

启用 RA 系列 SPI B 驱动的中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_RENESAS_RA8 && CONFIG_SPI
```

**被选择（Selected by）**

```text
CONFIG_SPI_B_DMAC
CONFIG_SPI_B_RA_DTC
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_ra8:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_ra8#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Renesas RA SPI B

**配置项引用（Symbol References）**：[`CONFIG_SPI_RENESAS_RA8`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RA8)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_SPI_B_DMAC`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_B_DMAC)、[`CONFIG_SPI_B_RA_DTC`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_B_RA_DTC)。

<a id="CONFIG_SPI_B_RA_DTC"></a>

## 172.36 `CONFIG_SPI_B_RA_DTC`

**提示（Prompt）**：RA MCU SPI 数据传输控制器（DTC）支持

**说明（Help）**

为 SPI 实例启用数据传输控制器（DTC）模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_RENESAS_RA8 && CONFIG_SPI
```

**默认值（Defaults）**

```text
n || n
```

**主动选择（Selects）**

```text
CONFIG_SPI_B_INTERRUPT
CONFIG_USE_RA_FSP_DTC
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_ra8:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_ra8#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Renesas RA SPI B

**配置项引用（Symbol References）**：[`CONFIG_SPI_RENESAS_RA8`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RA8)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_SPI_B_INTERRUPT`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_B_INTERRUPT)、[`CONFIG_USE_RA_FSP_DTC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_DTC)。

<a id="CONFIG_SPI_B_USE_HW_SS"></a>

## 172.37 `CONFIG_SPI_B_USE_HW_SS`

**提示（Prompt）**：RA MCU SPI B 硬件片选（Hardware Chip Select）支持

**说明（Help）**

使用片选引脚（Chip Select Pin）代替软件片选（Software Chip Select）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_RENESAS_RA8 && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_ra8:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_ra8#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Renesas RA SPI B

**配置项引用（Symbol References）**：[`CONFIG_SPI_RENESAS_RA8`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RA8)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_CC13XX_CC26XX"></a>

## 172.38 `CONFIG_SPI_CC13XX_CC26XX`

**提示（Prompt）**：TI SimpleLink CC13xx / CC26xx SPI 驱动

**说明（Help）**

启用 TI SimpleLink CC13xx / CC26xx SPI 外设支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_CC13XX_CC26XX_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/spi/Kconfig.cc13xx_cc26xx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.cc13xx_cc26xx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SPI_CC23X0"></a>

## 172.39 `CONFIG_SPI_CC23X0`

**提示（Prompt）**：TI SimpleLink CC23x0 SPI 驱动

**说明（Help）**

启用 TI SimpleLink CC23x0 SPI 外设支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_CC23X0_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/spi/Kconfig.cc23x0:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.cc23x0#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SPI_CC23X0_DMA_DRIVEN"></a>

## 172.40 `CONFIG_SPI_CC23X0_DMA_DRIVEN`

**提示（Prompt）**：TI CC23X0 SPI 设备的 DMA 支持

**说明（Help）**

SPI 的 DMA 驱动事务（DMA-driven Transactions）。DMA 驱动模式将数据传输任务从 CPU 卸载到 DMA，并减少处理 SPI 传输所需的中断次数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_CC23X0 && CONFIG_SPI
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/spi/Kconfig.cc23x0:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.cc23x0#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → TI SimpleLink CC23x0 SPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_CC23X0`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_CC23X0)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_SPI_CDNS"></a>

## 172.41 `CONFIG_SPI_CDNS`

**提示（Prompt）**：Cadence SPI 控制器（Controller）驱动

**说明（Help）**

启用基于 Cadence IP6524 的 SPI 外设。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_CDNS_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.cdns:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.cdns#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_COMPLETION_TIMEOUT_TOLERANCE"></a>

## 172.42 `CONFIG_SPI_COMPLETION_TIMEOUT_TOLERANCE`

**提示（Prompt）**：完成超时容差（Completion Timeout Tolerance，毫秒）

**说明（Help）**

SPI 完成超时逻辑的容差值（Tolerance Value），单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI
```

**默认值（Defaults）**

```text
200
```

**定义位置（Location）**：[`drivers/spi/Kconfig:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_DW"></a>

## 172.43 `CONFIG_SPI_DW`

**提示（Prompt）**：DesignWare SPI 控制器（Controller）驱动

**说明（Help）**

启用 DesignWare SPI 控制器支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SNPS_DESIGNWARE_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL if n
```

**被选择（Selected by）**

```text
CONFIG_SPI_RTS5817
```

**定义位置（Location）**：[`drivers/spi/Kconfig.dw:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.dw#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_SPI_RTS5817`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RTS5817)。

<a id="CONFIG_SPI_DW_ACCESS_WORD_ONLY"></a>

## 172.44 `CONFIG_SPI_DW_ACCESS_WORD_ONLY`

**提示（Prompt）**：DesignWare SPI 仅允许字访问（Word Access）

**说明（Help）**

某些情况下，例如 ARC HS Development Kit，DesignWare SPI 外设空间仅允许字访问（Word Access），字节访问（Byte Access）会引发异常。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_DW && CONFIG_SPI
```

**定义位置（Location）**：[`drivers/spi/Kconfig.dw:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.dw#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → DesignWare SPI 控制器（Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_DW`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_DW)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_DW_HSSI"></a>

## 172.45 `CONFIG_SPI_DW_HSSI`

**提示（Prompt）**：DesignWare SPI HSSI 变体（Variant）

**说明（Help）**

使用与该外设 SPI DW HSSI 变体兼容的寄存器布局（Register Layout）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_DW && CONFIG_SPI
```

**定义位置（Location）**：[`drivers/spi/Kconfig.dw:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.dw#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → DesignWare SPI 控制器（Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_DW`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_DW)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_EGIS_ET171"></a>

## 172.46 `CONFIG_SPI_EGIS_ET171`

**提示（Prompt）**：基于 Andes ATCSPI200 的 Egis ET171 SPI 驱动

**说明（Help）**

启用基于 Andes ATCSPI200 的 Egis ET171 SPI 控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_EGIS_ET171_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.egis_et171:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.egis_et171#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_EMUL"></a>

## 172.47 `CONFIG_SPI_EMUL`

**提示（Prompt）**：SPI 仿真器（Emulator）

**说明（Help）**

启用 SPI 仿真器（Emulator）驱动。它是一个模拟驱动，不与真实硬件通信，而是与仿真驱动通信；后者模拟仿真 SPI 总线上的设备。用于测试 SPI 设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_SPI_EMUL_CONTROLLER_ENABLED && CONFIG_EMUL && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.spi_emul:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.spi_emul#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EMUL)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_ESP32_INTERRUPT"></a>

## 172.48 `CONFIG_SPI_ESP32_INTERRUPT`

**提示（Prompt）**：ESP32 SPI 中断模式（Interrupt Mode）

**说明（Help）**

启用 ESP32 SPI 驱动的中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_SPIM && CONFIG_SPI
```

**被选择（Selected by）**

```text
CONFIG_ESP32_SPI_TARGET
```

**定义位置（Location）**：[`drivers/spi/Kconfig.esp32:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.esp32#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → ESP32 SPI 控制器（Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_ESP32_SPIM`](P172_drivers_spi_配置项参考_1.md#CONFIG_ESP32_SPIM)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_ESP32_SPI_TARGET`](P172_drivers_spi_配置项参考_1.md#CONFIG_ESP32_SPI_TARGET)。

<a id="CONFIG_SPI_ESP32_TARGET_MAX_BUFS"></a>

## 172.49 `CONFIG_SPI_ESP32_TARGET_MAX_BUFS`

**提示（Prompt）**：每个目标事务的最大分散／聚集缓冲区数量

**说明（Help）**

可合并到单个目标事务（Target Transaction）中的独立 `spi_buf` 段数量。目标帧在片选信号一次有效期间由控制器提供时钟，因此分散缓冲区（Scattered Buffers）会聚集为一次连续的 FIFO 传输。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_SPI_TARGET && CONFIG_ESP32_SPIM && CONFIG_SPI
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/spi/Kconfig.esp32:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.esp32#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → ESP32 SPI 控制器（Controller）驱动 → ESP32 SPI 目标模式（Target Mode）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_SPI_TARGET`](P172_drivers_spi_配置项参考_1.md#CONFIG_ESP32_SPI_TARGET)、[`CONFIG_ESP32_SPIM`](P172_drivers_spi_配置项参考_1.md#CONFIG_ESP32_SPIM)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_EXTENDED_MODES"></a>

## 172.50 `CONFIG_SPI_EXTENDED_MODES`

**提示（Prompt）**：扩展模式（Extended Modes）［实验性，EXPERIMENTAL］

**说明（Help）**

启用 SPI API 的扩展操作。目前允许选择线路模式（Line Mode）：单线、双线、四线或八线（Single/Dual/Quad/Octal）。不过，原文指出这些模式尚未真正得到支持，因为还需要通过 SPI 缓冲区提供更多功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`drivers/spi/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_SPI_GD32"></a>

## 172.51 `CONFIG_SPI_GD32`

**提示（Prompt）**：Gigadevice GD32 SPI 驱动

**说明（Help）**

启用 Gigadevice GD32 SPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GD_GD32_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/spi/Kconfig.gd32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.gd32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SPI_GD32_DMA"></a>

## 172.52 `CONFIG_SPI_GD32_DMA`

**提示（Prompt）**：GD32 MCU SPI 直接内存访问（DMA）支持

**说明（Help）**

对于在设备树节点中启用了 DMA 通道的 SPI，使用直接内存访问（DMA）传输。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_GD32 && CONFIG_SPI
```

**主动选择（Selects）**

```text
CONFIG_DMA
CONFIG_SPI_GD32_INTERRUPT
```

**定义位置（Location）**：[`drivers/spi/Kconfig.gd32:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.gd32#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Gigadevice GD32 SPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_GD32`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_GD32)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_SPI_GD32_INTERRUPT`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_GD32_INTERRUPT)。

<a id="CONFIG_SPI_GD32_INTERRUPT"></a>

## 172.53 `CONFIG_SPI_GD32_INTERRUPT`

**提示（Prompt）**：GD32 MCU SPI 中断支持（Interrupt Support）

**说明（Help）**

为 SPI 实例启用中断驱动模式（Interrupt-driven Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_GD32 && CONFIG_SPI
```

**默认值（Defaults）**

```text
y if CONFIG_SPI_ASYNC
y if CONFIG_SPI_GD32_DMA
```

**被选择（Selected by）**

```text
CONFIG_SPI_GD32_DMA
```

**定义位置（Location）**：[`drivers/spi/Kconfig.gd32:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.gd32#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Gigadevice GD32 SPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_GD32`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_GD32)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_SPI_ASYNC`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_ASYNC)、[`CONFIG_SPI_GD32_DMA`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_GD32_DMA)。

<a id="CONFIG_SPI_GRLIB_SPIMCTRL"></a>

## 172.54 `CONFIG_SPI_GRLIB_SPIMCTRL`

**提示（Prompt）**：GRLIB SPI 存储器控制器（Memory Controller）

**说明（Help）**

启用 GRLIB SPIMCTRL。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SPARC_LEON && CONFIG_SPI
```

**定义位置（Location）**：[`drivers/spi/Kconfig.grlib_spimctrl:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.grlib_spimctrl#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_SPARC_LEON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SPARC_LEON)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SPARC_LEON`。

<a id="CONFIG_SPI_INFINEON_DMA"></a>

## 172.55 `CONFIG_SPI_INFINEON_DMA`

**提示（Prompt）**：Infineon SPI 直接内存访问（DMA）支持

**说明（Help）**

使用 SPI 驱动时启用直接内存访问（DMA）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_INFINEON_SPI && CONFIG_SPI
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/spi/Kconfig.infineon:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.infineon#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_USE_INFINEON_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_SPI)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_SPI_INFINEON_HAL"></a>

## 172.56 `CONFIG_SPI_INFINEON_HAL`

**提示（Prompt）**：Infineon SPI 驱动

**说明（Help）**

此选项为 Infineon 系列启用基于旧版硬件抽象层（Legacy HAL）的 SPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_SPI_ENABLED && CONFIG_USE_INFINEON_LEGACY_HAL && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_INFINEON_SPI
CONFIG_PINCTRL
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/spi/Kconfig.infineon:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.infineon#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_USE_INFINEON_LEGACY_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_LEGACY_HAL)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_USE_INFINEON_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_SPI_INFINEON_PDL"></a>

## 172.57 `CONFIG_SPI_INFINEON_PDL`

**提示（Prompt）**：Infineon SPI 驱动

**说明（Help）**

此选项为 Infineon 系列启用基于外设驱动库（PDL）的 SPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_SPI_ENABLED && !CONFIG_USE_INFINEON_LEGACY_HAL && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_INFINEON_SPI
CONFIG_PINCTRL
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/spi/Kconfig.infineon:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.infineon#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_USE_INFINEON_LEGACY_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_LEGACY_HAL)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_USE_INFINEON_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_SPI_INIT_PRIORITY"></a>

## 172.58 `CONFIG_SPI_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`drivers/spi/Kconfig:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_SPI_INTERRUPT"></a>

## 172.59 `CONFIG_SPI_INTERRUPT`

**提示（Prompt）**：RA MCU SPI 中断支持（Interrupt Support）

**说明（Help）**

启用 RA 系列 SPI 驱动的中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_RENESAS_RA && CONFIG_SPI
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_ra:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_ra#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Renesas RA SPI

**配置项引用（Symbol References）**：[`CONFIG_SPI_RENESAS_RA`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RA)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_ITE_IT51XXX"></a>

## 172.60 `CONFIG_SPI_ITE_IT51XXX`

**提示（Prompt）**：ITE IT51XXX SPI 驱动

**说明（Help）**

启用 ITE IT51XXX SPI 主机（SSPI）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT51XXX_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/spi/Kconfig.it51xxx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.it51xxx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SPI_ITE_IT51XXX_FIFO_MODE"></a>

## 172.61 `CONFIG_SPI_ITE_IT51XXX_FIFO_MODE`

**提示（Prompt）**：ITE IT51XXX 共享／分组 FIFO 模式（Shared/Group FIFO Mode）支持

**说明（Help）**

启用 ITE IT51XXX 共享和分组 FIFO 模式（Shared and Group FIFO Mode）。由于硬件限制，只有同时满足以下条件时才支持 FIFO 模式：

1. 使用 SPI 模式 0，即 `CPOL = 0`、`CPHA = 0`。
2. 使用片选 0（Chip Select 0）。
3. 发送（TX）和接收（RX）事务的字节数均为偶数，且小于 FIFO 大小设置 `SPI_ITE_IT51XXX_FIFO_SIZE`。
4. 对于分组 FIFO 模式，时钟源设置为锁相环（PLL）频率。

如果事务不满足这些要求，驱动将自动切换至程序控制输入输出（PIO）模式完成传输。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_ITE_IT51XXX && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SOC_IT51XXX_CPU_IDLE_GATING
```

**定义位置（Location）**：[`drivers/spi/Kconfig.it51xxx:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.it51xxx#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → ITE IT51XXX SPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_ITE_IT51XXX`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_ITE_IT51XXX)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_SOC_IT51XXX_CPU_IDLE_GATING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT51XXX_CPU_IDLE_GATING)。

<a id="CONFIG_SPI_ITE_IT51XXX_FIFO_SIZE"></a>

## 172.62 `CONFIG_SPI_ITE_IT51XXX_FIFO_SIZE`

**提示（Prompt）**：ITE IT51XXX 共享／分组 FIFO 大小

**说明（Help）**

设置 IT51XXX FIFO 大小。按照硬件设计，可设置的最大值为 2046。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_ITE_IT51XXX_FIFO_MODE && CONFIG_SPI_ITE_IT51XXX && CONFIG_SPI
```

**默认值（Defaults）**

```text
128
```

**取值范围（Ranges）**

```text
[2, 2046]
```

**定义位置（Location）**：[`drivers/spi/Kconfig.it51xxx:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.it51xxx#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → ITE IT51XXX SPI 驱动 → ITE IT51XXX 共享／分组 FIFO 模式（Shared/Group FIFO Mode）支持

**配置项引用（Symbol References）**：[`CONFIG_SPI_ITE_IT51XXX_FIFO_MODE`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_ITE_IT51XXX_FIFO_MODE)、[`CONFIG_SPI_ITE_IT51XXX`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_ITE_IT51XXX)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_ITE_IT8XXX2"></a>

## 172.63 `CONFIG_SPI_ITE_IT8XXX2`

**提示（Prompt）**：ITE IT8XXX2 SPI 驱动

**说明（Help）**

启用 ITE IT8XXX2 SPI 主机（SSPI）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT8XXX2_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_SOC_IT8XXX2_CPU_IDLE_GATING
```

**定义位置（Location）**：[`drivers/spi/Kconfig.it8xxx2:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.it8xxx2#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_SOC_IT8XXX2_CPU_IDLE_GATING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT8XXX2_CPU_IDLE_GATING)。

<a id="CONFIG_SPI_LITEX"></a>

## 172.64 `CONFIG_SPI_LITEX`

**提示（Prompt）**：LiteX SPI 控制器（Controller）驱动

**说明（Help）**

启用 LiteX 上的 SPI 外设。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LITEX_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.litex:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.litex#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_LITEX_LITESPI"></a>

## 172.65 `CONFIG_SPI_LITEX_LITESPI`

**提示（Prompt）**：LiteX SPI LiteSPI 控制器驱动

**说明（Help）**

启用 LiteX 上的 SPI 外设。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LITEX_SPI_LITESPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.litex:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.litex#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_MAX32"></a>

## 172.66 `CONFIG_SPI_MAX32`

**提示（Prompt）**：MAX32 MCU SPI 控制器驱动

**说明（Help）**

为 MAX32 系列处理器启用 SPI 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX32_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/spi/Kconfig.max32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.max32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SPI_MAX32_DMA"></a>

## 172.67 `CONFIG_SPI_MAX32_DMA`

**提示（Prompt）**：MAX32 MCU SPI 直接内存访问（DMA）支持

**说明（Help）**

为 MAX32 MCU SPI 驱动启用直接内存访问（DMA）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_MAX32 && CONFIG_SPI
```

**主动选择（Selects）**

```text
CONFIG_DMA
CONFIG_CACHE_MANAGEMENT if CONFIG_DCACHE
CONFIG_SPI_MAX32_INTERRUPT if CONFIG_SPI_MAX32_RTIO
```

**定义位置（Location）**：[`drivers/spi/Kconfig.max32:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.max32#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → MAX32 MCU SPI 控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_MAX32`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_MAX32)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_SPI_MAX32_INTERRUPT`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_MAX32_INTERRUPT)、[`CONFIG_SPI_MAX32_RTIO`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_MAX32_RTIO)。

<a id="CONFIG_SPI_MAX32_INTERRUPT"></a>

## 172.68 `CONFIG_SPI_MAX32_INTERRUPT`

**提示（Prompt）**：MAX32 MCU SPI 中断支持（Interrupt Support）

**说明（Help）**

为 MAX32 MCU SPI 驱动启用中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_MAX32 && CONFIG_SPI
```

**被选择（Selected by）**

```text
CONFIG_SPI_MAX32_DMA
CONFIG_SPI_MAX32_RTIO
```

**定义位置（Location）**：[`drivers/spi/Kconfig.max32:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.max32#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → MAX32 MCU SPI 控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_MAX32`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_MAX32)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_SPI_MAX32_DMA`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_MAX32_DMA)、[`CONFIG_SPI_MAX32_RTIO`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_MAX32_RTIO)。

<a id="CONFIG_SPI_MAX32_RTIO"></a>

## 172.69 `CONFIG_SPI_MAX32_RTIO`

**提示（Prompt）**：MAX32 SPI 实时输入输出（RTIO）支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_SPI_ASYNC && CONFIG_SPI_MAX32 && CONFIG_SPI
```

**默认值（Defaults）**

```text
y if CONFIG_SPI_RTIO
```

**主动选择（Selects）**

```text
CONFIG_SPI_MAX32_INTERRUPT
```

**定义位置（Location）**：[`drivers/spi/Kconfig.max32:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.max32#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → MAX32 MCU SPI 控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_ASYNC`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_ASYNC)、[`CONFIG_SPI_MAX32`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_MAX32)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_SPI_RTIO`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RTIO)、[`CONFIG_SPI_MAX32_INTERRUPT`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_MAX32_INTERRUPT)。

<a id="CONFIG_SPI_MAX32_RTIO_CQ_SIZE"></a>

## 172.70 `CONFIG_SPI_MAX32_RTIO_CQ_SIZE`

**提示（Prompt）**：可用完成队列条目（Completion Queue Entries）数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_MAX32_RTIO && CONFIG_SPI_MAX32 && CONFIG_SPI
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/spi/Kconfig.max32:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.max32#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → MAX32 MCU SPI 控制器驱动 → MAX32 SPI 实时输入输出（RTIO）支持

**配置项引用（Symbol References）**：[`CONFIG_SPI_MAX32_RTIO`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_MAX32_RTIO)、[`CONFIG_SPI_MAX32`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_MAX32)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_MAX32_RTIO_SQ_SIZE"></a>

## 172.71 `CONFIG_SPI_MAX32_RTIO_SQ_SIZE`

**提示（Prompt）**：可用提交队列条目（Submission Queue Entries）数量

**说明（Help）**

SPI 使用实时输入输出（RTIO）时，每个驱动都持有一个上下文，阻塞式 API 调用通过该上下文执行 SPI 事务。使用等长缓冲区的普通 SPI 操作时，此队列的深度至少应容纳所使用的最长 `spi_buf_sets` 集合。发送／接收 SPI 缓冲区集合的长度并不总是相等时，可能需要稍大的队列深度，因为它们会被转换为普通收发操作（Transceives）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_MAX32_RTIO && CONFIG_SPI_MAX32 && CONFIG_SPI
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/spi/Kconfig.max32:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.max32#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → MAX32 MCU SPI 控制器驱动 → MAX32 SPI 实时输入输出（RTIO）支持

**配置项引用（Symbol References）**：[`CONFIG_SPI_MAX32_RTIO`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_MAX32_RTIO)、[`CONFIG_SPI_MAX32`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_MAX32)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_MCHP_DMA_DRIVEN"></a>

## 172.72 `CONFIG_SPI_MCHP_DMA_DRIVEN`

**提示（Prompt）**：Microchip SPI 直接内存访问（DMA）模式

**说明（Help）**

为 SPI 外设启用 DMA 驱动传输（DMA-driven Transfers）。要求存在 DMA 控制器，并在设备树（Device Tree）中提供 `dmas` 属性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.mchp:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.mchp#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

<a id="CONFIG_SPI_MCHP_FLEXCOM_DMA_DRIVEN"></a>

## 172.73 `CONFIG_SPI_MCHP_FLEXCOM_DMA_DRIVEN`

**提示（Prompt）**：Microchip FLEXCOM SPI 直接内存访问（DMA）模式

**说明（Help）**

为 SPI 外设启用 DMA 驱动传输（DMA-driven Transfers）。要求存在 DMA 控制器，并在设备树（Device Tree）中提供 `dmas` 属性。

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

**定义位置（Location）**：[`drivers/spi/Kconfig.mchp:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.mchp#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_SPI_MCHP_FLEXCOM_G1"></a>

## 172.74 `CONFIG_SPI_MCHP_FLEXCOM_G1`

**提示（Prompt）**：Microchip FLEXCOM SPI 驱动

**说明（Help）**

启用 Microchip FLEXCOM SPI 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_FLEXCOM_G1_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/spi/Kconfig.mchp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.mchp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_SPI_MCHP_INTER_CHARACTER_SPACE"></a>

## 172.75 `CONFIG_SPI_MCHP_INTER_CHARACTER_SPACE`

**提示（Prompt）**：Microchip SERCOM SPI 字符间隔（Inter-Character Spacing），单位为时钟周期

**说明（Help）**

SPI 总线上字符之间延迟的时钟周期数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X || CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA) && CONFIG_SPI_MCHP_SERCOM && CONFIG_SPI
```

**默认值（Defaults）**

```text
63 if CONFIG_SPI_PERIPHERAL
0
```

**取值范围（Ranges）**

```text
[0, 63]
```

**定义位置（Location）**：[`drivers/spi/Kconfig.mchp:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.mchp#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA)、[`CONFIG_SPI_MCHP_SERCOM`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_MCHP_SERCOM)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_SPI_PERIPHERAL`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_PERIPHERAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`。

<a id="CONFIG_SPI_MCHP_MSS"></a>

## 172.76 `CONFIG_SPI_MCHP_MSS`

**提示（Prompt）**：Microchip PolarFire SoC SPI 驱动

**说明（Help）**

启用 PolarFire SoC SPI 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_MPFS_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.mchp_mss:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.mchp_mss#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_MCHP_QSPI"></a>

## 172.77 `CONFIG_SPI_MCHP_QSPI`

**提示（Prompt）**：Microchip PolarFire SoC QSPI 驱动

**说明（Help）**

启用 PolarFire SoC QSPI 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_MPFS_QSPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.mchp_mss_qspi:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.mchp_mss_qspi#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_MCHP_SERCOM"></a>

## 172.78 `CONFIG_SPI_MCHP_SERCOM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Microchip SPI SERCOM 驱动的公共选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI
```

**被选择（Selected by）**

```text
CONFIG_SPI_MCHP_SERCOM_G1
```

**定义位置（Location）**：[`drivers/spi/Kconfig.mchp:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.mchp#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_SPI_MCHP_SERCOM_G1`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_MCHP_SERCOM_G1)。

<a id="CONFIG_SPI_MCHP_SERCOM_G1"></a>

## 172.79 `CONFIG_SPI_MCHP_SERCOM_G1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip SERCOM SPI 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_SERCOM_G1_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_GPIO
CONFIG_SPI_MCHP_SERCOM
```

**定义位置（Location）**：[`drivers/spi/Kconfig.mchp:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.mchp#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_SPI_MCHP_SERCOM`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_MCHP_SERCOM)。

<a id="CONFIG_SPI_MCUX_DSPI"></a>

## 172.80 `CONFIG_SPI_MCUX_DSPI`

**提示（Prompt）**：MCUX DSPI 驱动

**说明（Help）**

启用 MCUX DSPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_DSPI_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/spi/Kconfig.mcux_dspi:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.mcux_dspi#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SPI_MCUX_ECSPI"></a>

## 172.81 `CONFIG_SPI_MCUX_ECSPI`

**提示（Prompt）**：MCUX ECSPI 驱动

**说明（Help）**

启用 NXP MCUX ECSPI 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_ECSPI_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/spi/Kconfig.mcux_ecspi:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.mcux_ecspi#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SPI_MCUX_FLEXCOMM"></a>

## 172.82 `CONFIG_SPI_MCUX_FLEXCOMM`

**提示（Prompt）**：MCUX FLEXCOMM SPI 驱动

**说明（Help）**

启用 MCUX FLEXCOMM SPI 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPC_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_RESET
```

**定义位置（Location）**：[`drivers/spi/Kconfig.mcux_flexcomm:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.mcux_flexcomm#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)。

<a id="CONFIG_SPI_MCUX_FLEXCOMM_DMA"></a>

## 172.83 `CONFIG_SPI_MCUX_FLEXCOMM_DMA`

**提示（Prompt）**：MCUX FLEXCOMM SPI 直接内存访问（DMA）支持

**说明（Help）**

为在设备树节点中启用了 DMA 通道的 SPI 实例，启用直接内存访问（DMA）模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_MCUX_FLEXCOMM && CONFIG_SPI
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/spi/Kconfig.mcux_flexcomm:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.mcux_flexcomm#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → MCUX FLEXCOMM SPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_MCUX_FLEXCOMM`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_MCUX_FLEXCOMM)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_SPI_MCUX_FLEXCOMM_DMA_MAX_BLOCKS"></a>

## 172.84 `CONFIG_SPI_MCUX_FLEXCOMM_DMA_MAX_BLOCKS`

**提示（Prompt）**：MCUX FLEXCOMM SPI 可用 DMA 块数

**说明（Help）**

指定可用于 SPI 传输的 DMA 块数。必须配置足够多的 DMA 块，以处理传输缓冲区集合中的所有缓冲区。如果发送（TX）与接收（RX）缓冲区大小不同，每组都需要一个额外块。最后一个字（Word）也需要独立的块，以便用最终的单字缓冲区设置传输结束位（End of Transfer Bit），从而释放片选（CS）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_MCUX_FLEXCOMM_DMA && CONFIG_SPI_MCUX_FLEXCOMM && CONFIG_SPI
```

**默认值（Defaults）**

```text
6
```

**取值范围（Ranges）**

```text
[2, 100]
```

**定义位置（Location）**：[`drivers/spi/Kconfig.mcux_flexcomm:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.mcux_flexcomm#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → MCUX FLEXCOMM SPI 驱动 → MCUX FLEXCOMM SPI 直接内存访问（DMA）支持

**配置项引用（Symbol References）**：[`CONFIG_SPI_MCUX_FLEXCOMM_DMA`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_MCUX_FLEXCOMM_DMA)、[`CONFIG_SPI_MCUX_FLEXCOMM`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_MCUX_FLEXCOMM)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_MCUX_FLEXIO"></a>

## 172.85 `CONFIG_SPI_MCUX_FLEXIO`

**提示（Prompt）**：MCUX FlexIO SPI 驱动

**说明（Help）**

启用 MCUX FlexIO SPI 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_FLEXIO_SPI_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MCUX_FLEXIO
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/spi/Kconfig.mcux_flexio:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.mcux_flexio#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_MCUX_FLEXIO`](P123_drivers_misc_配置项参考.md#CONFIG_MCUX_FLEXIO)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SPI_MSPM0"></a>

## 172.86 `CONFIG_SPI_MSPM0`

**提示（Prompt）**：TI MSPM0 SPI

**说明（Help）**

启用 TI MSPM0 SPI 外设支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_MSPM0_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_MSPM0_DL_SPI
CONFIG_PINCTRL
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/spi/Kconfig.mspm0:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.mspm0#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_USE_MSPM0_DL_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_MSPM0_DL_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_USE_MSPM0_DL_SPI`。

<a id="CONFIG_SPI_NPCX_SPIP"></a>

## 172.87 `CONFIG_SPI_NPCX_SPIP`

**提示（Prompt）**：Nuvoton NPCX 嵌入式控制器（EC）SPI 驱动

**说明（Help）**

启用 NPCX 微控制器（MCU）上的 SPI 外设。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NPCX_SPIP_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/spi/Kconfig.npcx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.npcx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SPI_NPCX_SPIP_INTERRUPT"></a>

## 172.88 `CONFIG_SPI_NPCX_SPIP_INTERRUPT`

**提示（Prompt）**：NPCX SPIP 中断支持（Interrupt Support）

**说明（Help）**

为 NPCX 芯片的 SPI 驱动启用中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_NPCX_SPIP && CONFIG_SPI
```

**定义位置（Location）**：[`drivers/spi/Kconfig.npcx:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.npcx#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Nuvoton NPCX 嵌入式控制器（EC）SPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_NPCX_SPIP`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_NPCX_SPIP)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_NRFX"></a>

## 172.89 `CONFIG_SPI_NRFX`

**提示（Prompt）**：nRF SPI nrfx 驱动

**说明（Help）**

为 nRF 微控制器（MCU）系列启用 nrfx SPI 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_NORDIC_NRF && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/spi/Kconfig.nrfx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.nrfx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SPI_NRFX_DMM_BUFFER_SIZE"></a>

## 172.90 `CONFIG_SPI_NRFX_DMM_BUFFER_SIZE`

**提示（Prompt）**：最大传输分块大小（Maximum Transfer Chunk Size）

**说明（Help）**

限制从 DMM 内存区域分配的传输缓冲区大小。传输将拆分成此大小的数据块（Chunk）。对于同时发送和接收的 TXRX 传输，分配的总内存为分块大小的两倍。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_SPI_NRFX_SPIM || CONFIG_SPI_NRFX_SPIM_RTIO) && CONFIG_HAS_NORDIC_DMM && CONFIG_SPI_NRFX && CONFIG_SPI
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`drivers/spi/Kconfig.nrfx:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.nrfx#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → nRF SPI nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_NRFX_SPIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_NRFX_SPIM)、[`CONFIG_SPI_NRFX_SPIM_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_NRFX_SPIM_RTIO)、[`CONFIG_HAS_NORDIC_DMM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DMM)、[`CONFIG_SPI_NRFX`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_NRFX)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SPI_NRFX_SPIM`、`CONFIG_SPI_NRFX_SPIM_RTIO`、`CONFIG_HAS_NORDIC_DMM`。

<a id="CONFIG_SPI_NRFX_RAM_BUFFER_SIZE"></a>

## 172.91 `CONFIG_SPI_NRFX_RAM_BUFFER_SIZE`

**提示（Prompt）**：SPIM 外设的 RAM 缓冲区大小

**说明（Help）**

由于使用 EasyDMA，SPIM 外设无法使用任意内存位置的发送和接收缓冲区，而只能访问特定 RAM 中的缓冲区。因此，每个 SPIM 驱动实例都需要使用一个本地 RAM 中转缓冲区，将数据拆分为不超过该缓冲区大小的块进行传输。如果传输请求指定的缓冲区无法由 EasyDMA 访问，则还需在该缓冲区与本地缓冲区之间复制数据块。

此选项指定发送（TX）和接收（RX）路径上这类本地 RAM 缓冲区的大小，单位为字节。大小为 0 表示禁用此功能；此时，驱动使用者必须确保不提交使用 EasyDMA 无法访问的缓冲区的传输请求，否则传输将失败。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_SPI_NRFX_SPIM || CONFIG_SPI_NRFX_SPIM_RTIO) && !CONFIG_HAS_NORDIC_DMM && CONFIG_SPI_NRFX && CONFIG_SPI
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/spi/Kconfig.nrfx:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.nrfx#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → nRF SPI nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_NRFX_SPIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_NRFX_SPIM)、[`CONFIG_SPI_NRFX_SPIM_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_NRFX_SPIM_RTIO)、[`CONFIG_HAS_NORDIC_DMM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DMM)、[`CONFIG_SPI_NRFX`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_NRFX)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SPI_NRFX_SPIM`、`CONFIG_SPI_NRFX_SPIM_RTIO`、`CONFIG_HAS_NORDIC_DMM`。

<a id="CONFIG_SPI_NRFX_SPIM_RTIO_CQE_POOL_SIZE"></a>

## 172.92 `CONFIG_SPI_NRFX_SPIM_RTIO_CQE_POOL_SIZE`

**提示（Prompt）**：NRFX SPIM RTIO 上下文的提交队列条目（SQE）池大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_NRFX_SPIM_RTIO && CONFIG_SPI_NRFX && CONFIG_SPI
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/spi/Kconfig.nrfx:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.nrfx#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → nRF SPI nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_NRFX_SPIM_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_NRFX_SPIM_RTIO)、[`CONFIG_SPI_NRFX`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_NRFX)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SPI_NRFX_SPIM_RTIO`。

<a id="CONFIG_SPI_NRFX_SPIM_RTIO_SQE_POOL_SIZE"></a>

## 172.93 `CONFIG_SPI_NRFX_SPIM_RTIO_SQE_POOL_SIZE`

**提示（Prompt）**：NRFX SPIM RTIO 上下文的提交队列条目（SQE）池大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_NRFX_SPIM_RTIO && CONFIG_SPI_NRFX && CONFIG_SPI
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/spi/Kconfig.nrfx:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.nrfx#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → nRF SPI nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_NRFX_SPIM_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_NRFX_SPIM_RTIO)、[`CONFIG_SPI_NRFX`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_NRFX)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SPI_NRFX_SPIM_RTIO`。

<a id="CONFIG_SPI_NRFX_WAKE_TIMEOUT_US"></a>

## 172.94 `CONFIG_SPI_NRFX_WAKE_TIMEOUT_US`

**提示（Prompt）**：等待 SPI 外设唤醒的最长时间

**说明（Help）**

置位 WAKE 线后，SPI 控制器等待 SPI 外设唤醒的最长时间，单位为微秒。仅用于配置了 WAKE 线的实例，请参阅设备树属性 `wake-gpios`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_NRFX && CONFIG_SPI
```

**默认值（Defaults）**

```text
200
```

**定义位置（Location）**：[`drivers/spi/Kconfig.nrfx:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.nrfx#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → nRF SPI nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_NRFX`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_NRFX)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_NUMAKER"></a>

## 172.95 `CONFIG_SPI_NUMAKER`

**提示（Prompt）**：Nuvoton NuMaker MCU SPI 驱动

**说明（Help）**

此选项为 Nuvoton NuMaker 系列处理器启用 SPI 驱动。需要启用 NuMaker SPI 时，请选择 Y。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NUMAKER_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_NUMAKER_SPI
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/spi/Kconfig.numaker:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.numaker#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_HAS_NUMAKER_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NUMAKER_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SPI_NUMAKER_USCI"></a>

## 172.96 `CONFIG_SPI_NUMAKER_USCI`

**提示（Prompt）**：Nuvoton NuMaker MCU USCI SPI 驱动

**说明（Help）**

此选项为 Nuvoton NuMaker 系列处理器启用 USCI SPI 驱动。需要启用 NuMaker USCI SPI 时，请选择 Y。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NUMAKER_USCI_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_NUMAKER_SPI
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/spi/Kconfig.numaker:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.numaker#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_HAS_NUMAKER_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NUMAKER_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SPI_NXP_KINETIS"></a>

## 172.97 `CONFIG_SPI_NXP_KINETIS`

**提示（Prompt）**：NXP Kinetis SPI 驱动

**说明（Help）**

启用 NXP Kinetis SPI 外设支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_KINETIS_L_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.nxp_kinetis_l:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.nxp_kinetis_l#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_NXP_LPSPI"></a>

## 172.98 `CONFIG_SPI_NXP_LPSPI`

**提示（Prompt）**：NXP LPSPI 外设（Peripheral）

**说明（Help）**

启用 NXP LPSPI 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPSPI_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/spi/spi_nxp_lpspi/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/spi_nxp_lpspi/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SPI_NXP_LPSPI_CPU"></a>

## 172.99 `CONFIG_SPI_NXP_LPSPI_CPU`

**提示（Prompt）**：基于 CPU 的 NXP LPSPI 驱动

**说明（Help）**

为 LPSPI 启用普通的 CPU 驱动式 SPI 驱动。它比基于 DMA 的驱动延迟更低，但较长传输时通常带宽更低，且占用更多 CPU 时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(n || !CONFIG_SPI_NXP_LPSPI_DMA) && !CONFIG_SPI_NXP_LPSPI_CPU_RTIO && CONFIG_SPI_NXP_LPSPI && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/spi_nxp_lpspi/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/spi_nxp_lpspi/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → NXP LPSPI 外设（Peripheral）

**配置项引用（Symbol References）**：[`CONFIG_SPI_NXP_LPSPI_DMA`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_NXP_LPSPI_DMA)、[`CONFIG_SPI_NXP_LPSPI_CPU_RTIO`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_NXP_LPSPI_CPU_RTIO)、[`CONFIG_SPI_NXP_LPSPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_NXP_LPSPI)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_NXP_LPSPI_CPU_RTIO"></a>

## 172.100 `CONFIG_SPI_NXP_LPSPI_CPU_RTIO`

**提示（Prompt）**：基于 RTIO 的 NXP LPSPI 驱动

**说明（Help）**

为 LPSPI 启用原生基于实时输入输出（RTIO）的驱动。此驱动直接从中断服务程序（ISR）上下文以非阻塞、异步方式启动／恢复传输，从而优化延迟。不过，它不包含 DMA 的使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_SPI_NXP_LPSPI_DMA && CONFIG_SPI_RTIO && CONFIG_SPI_NXP_LPSPI && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/spi_nxp_lpspi/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/spi_nxp_lpspi/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → NXP LPSPI 外设（Peripheral）

**配置项引用（Symbol References）**：[`CONFIG_SPI_NXP_LPSPI_DMA`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_NXP_LPSPI_DMA)、[`CONFIG_SPI_RTIO`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RTIO)、[`CONFIG_SPI_NXP_LPSPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_NXP_LPSPI)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<!-- kconfig-navigation -->

[上一章](P171_drivers_smbus_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P173_drivers_spi_配置项参考_2.md)
