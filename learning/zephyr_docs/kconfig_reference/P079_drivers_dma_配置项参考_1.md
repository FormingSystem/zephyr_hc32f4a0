---
id: learning.zephyr-docs.kconfig-reference.page-79
title: "`drivers/dma`配置项参考（1/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第79章\_`drivers/dma`配置项参考（1/2）

本章翻译官方 Kconfig 数据库中 `drivers/dma` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_DMA"></a>

## 79.1 `CONFIG_DMA`

**提示（Prompt）**：直接内存访问（Direct Memory Access，DMA）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ADC_CC23X0_DMA_DRIVEN
CONFIG_ADC_ESP32_DMA
CONFIG_ADC_MCUX_LPADC_DMA_DRIVEN
CONFIG_ADC_STM32_DMA
CONFIG_AUDIO_CODEC_SF32LB
CONFIG_AUDIO_DMIC_INFINEON
CONFIG_AUDIO_DMIC_MCUX
CONFIG_CRC_STM32_DMA
CONFIG_CRYPTO_CC23X0_DMA
CONFIG_CRYPTO_SI32
CONFIG_DAI_INTEL_ALH
CONFIG_DAI_INTEL_HDA
CONFIG_DAI_INTEL_SSP
CONFIG_SDMMC_STM32
CONFIG_DISPLAY_RENESAS_LCDC
CONFIG_FLASH_SF32LB_MPI_QSPI_NOR
CONFIG_I2C_ASYNC_API
CONFIG_I2C_DW_LPSS_DMA
CONFIG_I2C_MAX32_DMA
CONFIG_I2C_SAM0_DMA_DRIVEN
CONFIG_I2C_STM32_V2_DMA
CONFIG_I2S_ESP32
CONFIG_I2S_INFINEON
CONFIG_I2S_MAX32
CONFIG_I2S_MCUX_SAI
CONFIG_I2S_MCUX_FLEXCOMM
CONFIG_I2S_SAM_SSC
CONFIG_I2S_SILABS_SIWX91X
CONFIG_I2S_STM32
CONFIG_I2S_STM32_SAI
CONFIG_I3C_STM32_DMA
CONFIG_MIPI_DBI_BFLB
CONFIG_MIPI_DBI_ESP32
CONFIG_MIPI_DBI_NXP_FLEXIO_LCDIF
CONFIG_MIPI_DBI_NXP_LCDIC_DMA
CONFIG_MSPI_DMA
CONFIG_PULSE_IO_ESP32_RMT_DMA
CONFIG_UART_BEE
CONFIG_UART_CC23X0_DMA_DRIVEN
CONFIG_UART_INFINEON_CAT1_HAL
CONFIG_UART_INFINEON_CAT1_PDL
CONFIG_UART_MAX32
CONFIG_UART_MCUX_FLEXCOMM
CONFIG_UART_NXP_LPUART_ASYNC_API_SUPPORT
CONFIG_UART_NS16550_INTEL_LPSS_DMA
CONFIG_UART_SF32LB
CONFIG_UART_SILABS_EUSART
CONFIG_UART_SILABS_USART
CONFIG_UART_STM32
CONFIG_UART_XMC4XXX
CONFIG_SPI_AMEBA_DMA
CONFIG_SPI_BEE_DMA
CONFIG_SPI_CC23X0_DMA_DRIVEN
CONFIG_SPI_GD32_DMA
CONFIG_SPI_INFINEON_DMA
CONFIG_SPI_MAX32_DMA
CONFIG_SPI_MCUX_FLEXCOMM_DMA
CONFIG_SPI_PL022_DMA
CONFIG_SPI_PW_LPSS_DMA
CONFIG_SPI_RPI_PICO_PIO_DMA
CONFIG_SPI_SAM_DMA
CONFIG_SPI_SILABS_EUSART_DMA
CONFIG_SPI_SMARTBOND_DMA
CONFIG_SPI_STM32_DMA
CONFIG_SPI_XEC_QMSPI
CONFIG_SPI_XMC4XXX_DMA
CONFIG_SPI_NXP_LPSPI_RTIO_DMA
CONFIG_UDC_SMARTBOND
CONFIG_USB_DC_SMARTBOND
CONFIG_VIDEO_ESP32
CONFIG_VIDEO_MCUX_FLEXIO
CONFIG_VIDEO_MCUX_SDMA
```

**定义位置（Location）**：[`drivers/dma/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ADC_CC23X0_DMA_DRIVEN`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_CC23X0_DMA_DRIVEN)、[`CONFIG_ADC_ESP32_DMA`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ESP32_DMA)、[`CONFIG_ADC_MCUX_LPADC_DMA_DRIVEN`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MCUX_LPADC_DMA_DRIVEN)、[`CONFIG_ADC_STM32_DMA`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_STM32_DMA)、[`CONFIG_AUDIO_CODEC_SF32LB`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC_SF32LB)、[`CONFIG_AUDIO_DMIC_INFINEON`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_INFINEON)、[`CONFIG_AUDIO_DMIC_MCUX`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_MCUX)、[`CONFIG_CRC_STM32_DMA`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_STM32_DMA)、[`CONFIG_CRYPTO_CC23X0_DMA`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_CC23X0_DMA)、[`CONFIG_CRYPTO_SI32`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_SI32)、[`CONFIG_DAI_INTEL_ALH`](P073_drivers_dai_配置项参考.md#CONFIG_DAI_INTEL_ALH)、[`CONFIG_DAI_INTEL_HDA`](P073_drivers_dai_配置项参考.md#CONFIG_DAI_INTEL_HDA)、[`CONFIG_DAI_INTEL_SSP`](P073_drivers_dai_配置项参考.md#CONFIG_DAI_INTEL_SSP)、[`CONFIG_SDMMC_STM32`](P076_drivers_disk_配置项参考.md#CONFIG_SDMMC_STM32)、[`CONFIG_DISPLAY_RENESAS_LCDC`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_RENESAS_LCDC)、[`CONFIG_FLASH_SF32LB_MPI_QSPI_NOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_SF32LB_MPI_QSPI_NOR)、[`CONFIG_I2C_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_ASYNC_API)、[`CONFIG_I2C_DW_LPSS_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_DW_LPSS_DMA)、[`CONFIG_I2C_MAX32_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_MAX32_DMA)、[`CONFIG_I2C_SAM0_DMA_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_SAM0_DMA_DRIVEN)、[`CONFIG_I2C_STM32_V2_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_STM32_V2_DMA)、[`CONFIG_I2S_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2S_ESP32)、[`CONFIG_I2S_INFINEON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2S_INFINEON)、[`CONFIG_I2S_MAX32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2S_MAX32)、[`CONFIG_I2S_MCUX_SAI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2S_MCUX_SAI)、[`CONFIG_I2S_MCUX_FLEXCOMM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2S_MCUX_FLEXCOMM)、[`CONFIG_I2S_SAM_SSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2S_SAM_SSC)、[`CONFIG_I2S_SILABS_SIWX91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2S_SILABS_SIWX91X)、[`CONFIG_I2S_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2S_STM32)、[`CONFIG_I2S_STM32_SAI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2S_STM32_SAI)、[`CONFIG_I3C_STM32_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I3C_STM32_DMA)、[`CONFIG_MIPI_DBI_BFLB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI_BFLB)、[`CONFIG_MIPI_DBI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI_ESP32)、[`CONFIG_MIPI_DBI_NXP_FLEXIO_LCDIF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI_NXP_FLEXIO_LCDIF)、[`CONFIG_MIPI_DBI_NXP_LCDIC_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI_NXP_LCDIC_DMA)、[`CONFIG_MSPI_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MSPI_DMA)、[`CONFIG_PULSE_IO_ESP32_RMT_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PULSE_IO_ESP32_RMT_DMA)、[`CONFIG_UART_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_BEE)、[`CONFIG_UART_CC23X0_DMA_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_CC23X0_DMA_DRIVEN)、[`CONFIG_UART_INFINEON_CAT1_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INFINEON_CAT1_HAL)、[`CONFIG_UART_INFINEON_CAT1_PDL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INFINEON_CAT1_PDL)、[`CONFIG_UART_MAX32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MAX32)、[`CONFIG_UART_MCUX_FLEXCOMM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MCUX_FLEXCOMM)、[`CONFIG_UART_NXP_LPUART_ASYNC_API_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NXP_LPUART_ASYNC_API_SUPPORT)、[`CONFIG_UART_NS16550_INTEL_LPSS_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NS16550_INTEL_LPSS_DMA)、[`CONFIG_UART_SF32LB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SF32LB)、[`CONFIG_UART_SILABS_EUSART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SILABS_EUSART)、[`CONFIG_UART_SILABS_USART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SILABS_USART)、[`CONFIG_UART_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_STM32)、[`CONFIG_UART_XMC4XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_XMC4XXX)、[`CONFIG_SPI_AMEBA_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_AMEBA_DMA)、[`CONFIG_SPI_BEE_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_BEE_DMA)、[`CONFIG_SPI_CC23X0_DMA_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_CC23X0_DMA_DRIVEN)、[`CONFIG_SPI_GD32_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_GD32_DMA)、[`CONFIG_SPI_INFINEON_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_INFINEON_DMA)、[`CONFIG_SPI_MAX32_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_MAX32_DMA)、[`CONFIG_SPI_MCUX_FLEXCOMM_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_MCUX_FLEXCOMM_DMA)、[`CONFIG_SPI_PL022_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_PL022_DMA)、[`CONFIG_SPI_PW_LPSS_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_PW_LPSS_DMA)、[`CONFIG_SPI_RPI_PICO_PIO_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RPI_PICO_PIO_DMA)、[`CONFIG_SPI_SAM_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_SAM_DMA)、[`CONFIG_SPI_SILABS_EUSART_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_SILABS_EUSART_DMA)、[`CONFIG_SPI_SMARTBOND_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_SMARTBOND_DMA)、[`CONFIG_SPI_STM32_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_STM32_DMA)、[`CONFIG_SPI_XEC_QMSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_XEC_QMSPI)、[`CONFIG_SPI_XMC4XXX_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_XMC4XXX_DMA)、[`CONFIG_SPI_NXP_LPSPI_RTIO_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_NXP_LPSPI_RTIO_DMA)、[`CONFIG_UDC_SMARTBOND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_SMARTBOND)、[`CONFIG_USB_DC_SMARTBOND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DC_SMARTBOND)、[`CONFIG_VIDEO_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_ESP32)、[`CONFIG_VIDEO_MCUX_FLEXIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_MCUX_FLEXIO)、[`CONFIG_VIDEO_MCUX_SDMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_MCUX_SDMA)。

<a id="CONFIG_DMAC_DESC_COUNT"></a>

## 79.2 `CONFIG_DMAC_DESC_COUNT`

**提示（Prompt）**：DMAC 描述符数量（Descriptor Count）

**说明（Help）**

预先分配的描述符（Descriptor）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_MCHP_DMAC_G3 && CONFIG_DMA
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/dma/Kconfig.mchp:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.mchp#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → Microchip G3 DMA 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_MCHP_DMAC_G3`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_MCHP_DMAC_G3)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMAMUX_STM32"></a>

## 79.3 `CONFIG_DMAMUX_STM32`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 DMA 请求复用器（DMAMUX）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_DMAMUX_ENABLED && CONFIG_DMA_STM32 && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.stm32:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.stm32#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_STM32`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_STM32)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMAMUX_STM32_INIT_PRIORITY"></a>

## 79.4 `CONFIG_DMAMUX_STM32_INIT_PRIORITY`

**提示（Prompt）**：STM32 DMAMUX 初始化优先级（Init Priority）

**说明（Help）**

DMAMUX 驱动设备必须在 DMA（`CONFIG_DMA_INIT_PRIORITY`）之后初始化，因此 DMAMUX 驱动设备的初始化优先级（Initialization Priority）数值应大于 DMA 的对应数值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_DMAMUX_ENABLED && CONFIG_DMA_STM32 && CONFIG_DMA
```

**默认值（Defaults）**

```text
41
```

**定义位置（Location）**：[`drivers/dma/Kconfig.stm32:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.stm32#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_STM32`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_STM32)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_64BIT"></a>

## 79.5 `CONFIG_DMA_64BIT`

**提示（Prompt）**：DMA 64 位地址支持（64-Bit Address Support）

**说明（Help）**

此选项为真时，支持 64 位 DMA 源地址和目标地址（Source and Destination Addresses）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA
```

**被选择（Selected by）**

```text
CONFIG_DMA_SEDI
```

**被弱选择（Implied by）**

```text
CONFIG_DMA_DW_AXI
```

**定义位置（Location）**：[`drivers/dma/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_DMA_SEDI`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_SEDI)、[`CONFIG_DMA_DW_AXI`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_DW_AXI)。

<a id="CONFIG_DMA_ADI_AXI_DMAC"></a>

## 79.6 `CONFIG_DMA_ADI_AXI_DMAC`

**提示（Prompt）**：Analog Devices AXI DMAC 驱动

**说明（Help）**

Analog Devices AXI DMAC 核（Core）的驱动。通过标准 Zephyr DMA 驱动 API，为 AXI-Stream 外设提供 DMA 传输（Transfer）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_AXI_DMAC_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.adi_axi_dmac:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.adi_axi_dmac#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_AMD_ACP_ATTR_MAX_BLOCK_COUNT"></a>

## 79.7 `CONFIG_DMA_AMD_ACP_ATTR_MAX_BLOCK_COUNT`

**提示（Prompt）**：最大块数量（Maximum Block Count）

**说明（Help）**

每次 DMA 传输（Transfer）所含的最大块（Block）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_AMD_ACP_HOST && CONFIG_DMA
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/dma/Kconfig.acp_host:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.acp_host#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → AMD ACP 主机 DMA 驱动（Host DMA Driver）

**配置项引用（Symbol References）**：[`CONFIG_DMA_AMD_ACP_HOST`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_AMD_ACP_HOST)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_AMD_ACP_BUFFER_ADDRESS_ALIGN"></a>

## 79.8 `CONFIG_DMA_AMD_ACP_BUFFER_ADDRESS_ALIGN`

**提示（Prompt）**：缓冲区地址对齐（Buffer Address Alignment），以字节为单位

**说明（Help）**

传给本驱动的缓冲区地址所需的对齐（Alignment），以字节为单位，用于调整内存区域的缓冲区地址。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_AMD_ACP_HOST && CONFIG_DMA
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：[`drivers/dma/Kconfig.acp_host:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.acp_host#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → AMD ACP 主机 DMA 驱动（Host DMA Driver）

**配置项引用（Symbol References）**：[`CONFIG_DMA_AMD_ACP_HOST`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_AMD_ACP_HOST)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_AMD_ACP_BUFFER_ALIGN"></a>

## 79.9 `CONFIG_DMA_AMD_ACP_BUFFER_ALIGN`

**提示（Prompt）**：缓冲区对齐（Buffer Alignment），以字节为单位

**说明（Help）**

传给本驱动的内存区域所需的对齐（Alignment），以字节为单位，用于调整内存区域的大小和基地址（Base Address）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_AMD_ACP_HOST && CONFIG_DMA
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：[`drivers/dma/Kconfig.acp_host:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.acp_host#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → AMD ACP 主机 DMA 驱动（Host DMA Driver）

**配置项引用（Symbol References）**：[`CONFIG_DMA_AMD_ACP_HOST`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_AMD_ACP_HOST)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_AMD_ACP_HOST"></a>

## 79.10 `CONFIG_DMA_AMD_ACP_HOST`

**提示（Prompt）**：AMD ACP 主机 DMA 驱动（Host DMA Driver）

**说明（Help）**

启用 AMD 音频协处理器（Audio Co-Processor，ACP）主机 DMA 驱动支持。此驱动为 AMD ACP 7.0 音频子系统的主机内存传输（Host Memory Transfer）提供 DMA 功能，支持在系统内存与 ACP 音频处理单元之间搬移音频数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA && DT_HAS_AMD_ACP_HOST_DMA_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.acp_host:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.acp_host#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_AMD_ACP_HOST_CHANNEL_COUNT"></a>

## 79.11 `CONFIG_DMA_AMD_ACP_HOST_CHANNEL_COUNT`

**提示（Prompt）**：最大通道数量（Maximum Channel Count）

**说明（Help）**

主机 DMA 通道（Host DMA Channel）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_AMD_ACP_HOST && CONFIG_DMA
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/dma/Kconfig.acp_host:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.acp_host#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → AMD ACP 主机 DMA 驱动（Host DMA Driver）

**配置项引用（Symbol References）**：[`CONFIG_DMA_AMD_ACP_HOST`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_AMD_ACP_HOST)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_AMD_ACP_SDW"></a>

## 79.12 `CONFIG_DMA_AMD_ACP_SDW`

**提示（Prompt）**：AMD ACP SoundWire DMA 驱动

**说明（Help）**

启用 AMD 音频协处理器（Audio Co-Processor，ACP）SoundWire DMA 驱动支持。此驱动为 AMD ACP 7.0 和 ACP 7.X 音频子系统的 SoundWire 接口传输提供 DMA 功能，使已连接的音频外设和编解码器（Codec）能够通过 SoundWire 总线传输音频流（Audio Streaming）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA && DT_HAS_AMD_ACP_SDW_DMA_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.acp_sdw:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.acp_sdw#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_AMD_ACP_SDW_CHANNEL_COUNT"></a>

## 79.13 `CONFIG_DMA_AMD_ACP_SDW_CHANNEL_COUNT`

**提示（Prompt）**：最大通道数量（Maximum Channel Count）

**说明（Help）**

ACP SoundWire DMA 通道（Channel）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_AMD_ACP_SDW && CONFIG_DMA
```

**默认值（Defaults）**

```text
12
```

**定义位置（Location）**：[`drivers/dma/Kconfig.acp_sdw:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.acp_sdw#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → AMD ACP SoundWire DMA 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_AMD_ACP_SDW`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_AMD_ACP_SDW)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_AMD_ACP_SDW_TRANS_SIZE"></a>

## 79.14 `CONFIG_DMA_AMD_ACP_SDW_TRANS_SIZE`

**提示（Prompt）**：DMA 传输大小（Transfer Size）

**说明（Help）**

ACP SoundWire DMA 传输大小（Transfer Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_AMD_ACP_SDW && CONFIG_DMA
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`drivers/dma/Kconfig.acp_sdw:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.acp_sdw#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → AMD ACP SoundWire DMA 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_AMD_ACP_SDW`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_AMD_ACP_SDW)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_AMD_ACP_TDM"></a>

## 79.15 `CONFIG_DMA_AMD_ACP_TDM`

**提示（Prompt）**：AMD ACP TDM DMA 驱动

**说明（Help）**

启用 AMD ACP 统一的时分复用（TDM）DMA 驱动。通过各实例独立的寄存器表（Per-Instance Register Table），覆盖 TDM0（耳麦，Headset）、TDM1（SP 扬声器，Speaker）和 TDM2（蓝牙，Bluetooth）的 P1 DMA 实例。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMD_ACP_TDM_DMA_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.acp_tdm:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.acp_tdm#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_AMD_ACP_TDM_BUFFER_ADDRESS_ALIGN"></a>

## 79.16 `CONFIG_DMA_AMD_ACP_TDM_BUFFER_ADDRESS_ALIGN`

**提示（Prompt）**：缓冲区地址对齐（Buffer Address Alignment）

**说明（Help）**

ACP TDM 音频缓冲区要求的地址对齐（Address Alignment）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_AMD_ACP_TDM && CONFIG_DMA
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`drivers/dma/Kconfig.acp_tdm:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.acp_tdm#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → AMD ACP TDM DMA 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_AMD_ACP_TDM`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_AMD_ACP_TDM)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_AMD_ACP_TDM_BUFFER_ALIGN"></a>

## 79.17 `CONFIG_DMA_AMD_ACP_TDM_BUFFER_ALIGN`

**提示（Prompt）**：缓冲区对齐（Buffer Alignment）

**说明（Help）**

ACP TDM 音频缓冲区要求的对齐（Alignment）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_AMD_ACP_TDM && CONFIG_DMA
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：[`drivers/dma/Kconfig.acp_tdm:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.acp_tdm#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → AMD ACP TDM DMA 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_AMD_ACP_TDM`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_AMD_ACP_TDM)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_AMD_ACP_TDM_CHANNEL_COUNT"></a>

## 79.18 `CONFIG_DMA_AMD_ACP_TDM_CHANNEL_COUNT`

**提示（Prompt）**：通道数量（Channel Count）

**说明（Help）**

DMA 通道（Channel）数量，每个实例 2 个通道，共 3 个实例。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_AMD_ACP_TDM && CONFIG_DMA
```

**默认值（Defaults）**

```text
6
```

**定义位置（Location）**：[`drivers/dma/Kconfig.acp_tdm:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.acp_tdm#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → AMD ACP TDM DMA 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_AMD_ACP_TDM`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_AMD_ACP_TDM)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_AMEBA"></a>

## 79.19 `CONFIG_DMA_AMEBA`

**提示（Prompt）**：AMEBA 通用 DMA 驱动（General Purpose DMA Driver）

**说明（Help）**

AMEBA 系列的通用 DMA（General Purpose DMA）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_AMEBA_GDMA_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.ameba:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.ameba#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_AMEBA_LLI"></a>

## 79.20 `CONFIG_DMA_AMEBA_LLI`

**提示（Prompt）**：AMEBA 链表模式（Linked List Mode）

**说明（Help）**

此选项支持以链表（Linked List）形式组织的数据块（Data Block）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_AMEBA && CONFIG_DMA
```

**定义位置（Location）**：[`drivers/dma/Kconfig.ameba:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.ameba#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → AMEBA 通用 DMA 驱动（General Purpose DMA Driver）

**配置项引用（Symbol References）**：[`CONFIG_DMA_AMEBA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_AMEBA)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_AMEBA_LLI_MAX_DESC"></a>

## 79.21 `CONFIG_DMA_AMEBA_LLI_MAX_DESC`

**提示（Prompt）**：可用 DMA 描述符（Descriptor）的最大数量

**说明（Help）**

为最大数量的描述符（Descriptor）预留内存。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_AMEBA && CONFIG_DMA
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`drivers/dma/Kconfig.ameba:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.ameba#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → AMEBA 通用 DMA 驱动（General Purpose DMA Driver）

**配置项引用（Symbol References）**：[`CONFIG_DMA_AMEBA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_AMEBA)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_AMEBA_SCATTER_GATHER"></a>

## 79.22 `CONFIG_DMA_AMEBA_SCATTER_GATHER`

**提示（Prompt）**：Ameba DMA 分散/聚集（Scatter/Gather）支持

**说明（Help）**

在 Ameba SoC 上启用 DMA 分散/聚集（Scatter/Gather）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_AMEBAG2 && CONFIG_DMA_AMEBA && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.ameba:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.ameba#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → AMEBA 通用 DMA 驱动（General Purpose DMA Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_AMEBAG2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAG2)、[`CONFIG_DMA_AMEBA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_AMEBA)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_AMEBAG2`。

<a id="CONFIG_DMA_ANDES_ATCDMACX00"></a>

## 79.23 `CONFIG_DMA_ANDES_ATCDMACX00`

**提示（Prompt）**：Andes ATCDMACX00 DMA 驱动

**说明（Help）**

Andes ATCDMACX00 DMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ANDESTECH_ATCDMACX00_ENABLED && (!CONFIG_DCACHE || CONFIG_SOC_ANDES_V5_IOCP || CONFIG_NOCACHE_MEMORY) && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.andes_atcdmacx00:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.andes_atcdmacx00#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_SOC_ANDES_V5_IOCP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ANDES_V5_IOCP)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_BEE"></a>

## 79.24 `CONFIG_DMA_BEE`

**提示（Prompt）**：Realtek Bee 系列 DMA 驱动

**说明（Help）**

此选项启用瑞昱（Realtek）Bee SoC 的 DMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_BEE_DMA_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAL_REALTEK_BEE_DMA
CONFIG_SYS_MEM_BLOCKS
```

**定义位置（Location）**：[`drivers/dma/Kconfig.bee:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.bee#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_HAL_REALTEK_BEE_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAL_REALTEK_BEE_DMA)、[`CONFIG_SYS_MEM_BLOCKS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYS_MEM_BLOCKS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAL_REALTEK_BEE_DMA`。

<a id="CONFIG_DMA_BEE_LLI_POOL_COUNT"></a>

## 79.25 `CONFIG_DMA_BEE_LLI_POOL_COUNT`

**提示（Prompt）**：内存池中的链表项（LLI）数量

**说明（Help）**

指定驱动内部内存池（Memory Pool）中可用的链表项（Linked List Item，LLI）描述符总数。这些描述符用于多块 DMA 传输（Multi-Block DMA Transfer）。DMA 配置中的每个块需要一个 LLI。如果有许多 DMA 通道并发使用多块传输，或者单次传输包含大量块，则应增大此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_BEE && CONFIG_DMA
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`drivers/dma/Kconfig.bee:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.bee#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → Realtek Bee 系列 DMA 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_BEE`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_BEE)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_BEE_MAX_BLOCKS_PER_CHANNEL"></a>

## 79.26 `CONFIG_DMA_BEE_MAX_BLOCKS_PER_CHANNEL`

**提示（Prompt）**：每个通道的最大块数量（Max Blocks Per Channel）

**说明（Help）**

指定单个 DMA 通道事务（Channel Transaction）可配置的最大块（Block）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_BEE && CONFIG_DMA
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[1, 64]
```

**定义位置（Location）**：[`drivers/dma/Kconfig.bee:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.bee#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → Realtek Bee 系列 DMA 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_BEE`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_BEE)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_BFLB"></a>

## 79.27 `CONFIG_DMA_BFLB`

**提示（Prompt）**：博流（Bouffalo Lab）DMA 驱动

**说明（Help）**

博流（Bouffalo Lab）SoC 的 DMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_DMA_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.bflb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.bflb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_CHANNEL_STATUS_TIMEOUT"></a>

## 79.28 `CONFIG_DMA_CHANNEL_STATUS_TIMEOUT`

**提示（Prompt）**：通道状态超时（Channel Status Timeout）

**说明（Help）**

中止或禁用通道（Channel）的最大超时时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_DW_AXI && CONFIG_DMA
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`drivers/dma/Kconfig.dw_axi_dmac:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.dw_axi_dmac#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → DesignWare AXI DMA 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_DW_AXI`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_DW_AXI)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_DW"></a>

## 79.29 `CONFIG_DMA_DW`

**提示（Prompt）**：DesignWare DMA 驱动

**说明（Help）**

DesignWare DMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SNPS_DESIGNWARE_DMA_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.dw:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.dw#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_DW_AXI"></a>

## 79.30 `CONFIG_DMA_DW_AXI`

**提示（Prompt）**：DesignWare AXI DMA 驱动

**说明（Help）**

DesignWare AXI DMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SNPS_DESIGNWARE_DMA_AXI_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_DMA_64BIT
```

**定义位置（Location）**：[`drivers/dma/Kconfig.dw_axi_dmac:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.dw_axi_dmac#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_DMA_64BIT`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_64BIT)。

<a id="CONFIG_DMA_DW_AXI_CCU_SUPPORT"></a>

## 79.31 `CONFIG_DMA_DW_AXI_CCU_SUPPORT`

**提示（Prompt）**：缓存一致性单元（Cache Coherence Unit）支持

**说明（Help）**

硬件支持缓存一致性（Cache Coherence）时，应启用此标志。由于硬件提供此支持，不再需要软件执行缓存维护（Cache Maintenance）操作。例如，将缓存一致性单元（Cache Coherency Unit）互连配置为使 DMA 与处理器获得相同的数据视图。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_DW_AXI && CONFIG_DMA
```

**定义位置（Location）**：[`drivers/dma/Kconfig.dw_axi_dmac:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.dw_axi_dmac#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → DesignWare AXI DMA 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_DW_AXI`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_DW_AXI)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_DW_AXI_DATA_WIDTH"></a>

## 79.32 `CONFIG_DMA_DW_AXI_DATA_WIDTH`

**提示（Prompt）**：数据总线宽度（Data Bus Width）

**说明（Help）**

修改此配置，以改变 AXI 主接口（Master Interface）的数据宽度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_DW_AXI && CONFIG_DMA
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：[`drivers/dma/Kconfig.dw_axi_dmac:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.dw_axi_dmac#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → DesignWare AXI DMA 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_DW_AXI`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_DW_AXI)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_DW_AXI_LLI_SUPPORT"></a>

## 79.33 `CONFIG_DMA_DW_AXI_LLI_SUPPORT`

**提示（Prompt）**：硬件支持链表多块传输（Linked List Multi-Block Transfer）

**说明（Help）**

硬件支持链表多块传输（Linked List Multi-Block Transfer）时，可以启用此标志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_DW_AXI && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.dw_axi_dmac:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.dw_axi_dmac#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → DesignWare AXI DMA 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_DW_AXI`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_DW_AXI)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_DW_AXI_MAX_BLOCK_TS"></a>

## 79.34 `CONFIG_DMA_DW_AXI_MAX_BLOCK_TS`

**提示（Prompt）**：最大块大小（Max Block Size）

**说明（Help）**

修改此配置，以设置块大小（Block Size）的最大值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_DW_AXI && CONFIG_DMA
```

**默认值（Defaults）**

```text
32767
```

**定义位置（Location）**：[`drivers/dma/Kconfig.dw_axi_dmac:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.dw_axi_dmac#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → DesignWare AXI DMA 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_DW_AXI`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_DW_AXI)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_DW_AXI_MAX_BURST_TXN_LEN"></a>

## 79.35 `CONFIG_DMA_DW_AXI_MAX_BURST_TXN_LEN`

**提示（Prompt）**：最大突发事务长度（Max Burst Transaction Length）

**说明（Help）**

设置支持的源数据单元和目标数据单元（Source and Destination Data Unit）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_DW_AXI && CONFIG_DMA
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/dma/Kconfig.dw_axi_dmac:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.dw_axi_dmac#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → DesignWare AXI DMA 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_DW_AXI`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_DW_AXI)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_DW_AXI_MAX_DESC"></a>

## 79.36 `CONFIG_DMA_DW_AXI_MAX_DESC`

**提示（Prompt）**：分配的链表项描述符（LLI Descriptor）数量

**说明（Help）**

在静态分配的内存池（Statically Allocated Pool）中，为每个通道创建指定数量的描述符（Descriptor）。每个通道都有自己的专用内存池。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_DW_AXI && CONFIG_DMA
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/dma/Kconfig.dw_axi_dmac:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.dw_axi_dmac#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → DesignWare AXI DMA 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_DW_AXI`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_DW_AXI)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_DW_CHANNEL_COUNT"></a>

## 79.37 `CONFIG_DMA_DW_CHANNEL_COUNT`

**提示（Prompt）**：DesignWare 最大通道数量（Max Channel Count）

**说明（Help）**

DesignWare DMA 实例的通道数量（Channel Count）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_DW && CONFIG_DMA
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/dma/Kconfig.dw_common:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.dw_common#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → DesignWare DMA 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_DW`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_DW)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_DW_FIFO_PARTITION"></a>

## 79.38 `CONFIG_DMA_DW_FIFO_PARTITION`

**提示（Prompt）**：FIFO 分区（FIFO Partitioning）

**说明（Help）**

FIFO 分区（FIFO Partition）功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_DW && CONFIG_DMA
```

**定义位置（Location）**：[`drivers/dma/Kconfig.dw_common:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.dw_common#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → DesignWare DMA 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_DW`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_DW)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_DW_HOST_MASK"></a>

## 79.39 `CONFIG_DMA_DW_HOST_MASK`

**提示（Prompt）**：内存空间掩码（Memory Space Mask）

**说明（Help）**

某些 DesignWare DMAC 实例要求对源地址/目标地址应用一个掩码（Mask），以标识地址所在的内存空间（Memory Space）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_DW && CONFIG_DMA
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/dma/Kconfig.dw_common:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.dw_common#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → DesignWare DMA 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_DW`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_DW)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_DW_HW_LLI"></a>

## 79.40 `CONFIG_DMA_DW_HW_LLI`

**提示（Prompt）**：硬件支持分散/聚集（Scatter Gather）

**说明（Help）**

默认预期硬件支持硬件链表项（LLI），即分散/聚集（Scatter Gather）。未启用此项时，驱动仍会执行分散/聚集，但改由软件遍历分散/聚集列表。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_DW && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.dw_common:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.dw_common#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → DesignWare DMA 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_DW`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_DW)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_DW_LLI_POOL_SIZE"></a>

## 79.41 `CONFIG_DMA_DW_LLI_POOL_SIZE`

**提示（Prompt）**：分配池（Allocation Pool）中的 LLI 结构体数量

**说明（Help）**

静态分配池（Statically Allocated Pool）中的链表项（LLI）结构体数量。每个通道都有自己的 LLI 结构体池。如果 `dma_config()` 期间日志提示 LLI 结构体不足，应增大此值以满足需求。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_DW && CONFIG_DMA
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/dma/Kconfig.dw_common:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.dw_common#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → DesignWare DMA 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_DW`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_DW)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_DW_SUSPEND_DRAIN"></a>

## 79.42 `CONFIG_DMA_DW_SUSPEND_DRAIN`

**提示（Prompt）**：停止时应先挂起并排空通道（Suspend and Drain）

**说明（Help）**

停止 DMA 通道时，不立即停止，而是先设置 `DRAIN` 标志位并挂起（Suspend）通道，使硬件 FIFO 在通道停止之前排空（Drain）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_INTEL_ADSP_GPDMA && CONFIG_DMA_DW && CONFIG_DMA
```

**定义位置（Location）**：[`drivers/dma/Kconfig.dw_common:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.dw_common#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → DesignWare DMA 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_INTEL_ADSP_GPDMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_INTEL_ADSP_GPDMA)、[`CONFIG_DMA_DW`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_DW)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_EMUL"></a>

## 79.43 `CONFIG_DMA_EMUL`

**提示（Prompt）**：仿真 DMA 驱动（Emulated DMA Driver）【实验性】

**说明（Help）**

仿真 DMA 驱动（Emulated DMA Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_DMA_EMUL_ENABLED && CONFIG_DMA
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`drivers/dma/Kconfig.emul:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.emul#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_DMA_ESP32"></a>

## 79.44 `CONFIG_DMA_ESP32`

**提示（Prompt）**：ESP32 通用 DMA 驱动（General Purpose DMA Driver）

**说明（Help）**

ESP32 系列的通用 DMA（General Purpose DMA）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_GDMA_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.esp32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.esp32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_ESP32_MAX_DESCRIPTOR_NUM"></a>

## 79.45 `CONFIG_DMA_ESP32_MAX_DESCRIPTOR_NUM`

**提示（Prompt）**：可用 DMA 描述符（Descriptor）的最大数量

**说明（Help）**

为最大数量的描述符（Descriptor）预留内存。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_ESP32 && CONFIG_DMA
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`drivers/dma/Kconfig.esp32:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.esp32#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → ESP32 通用 DMA 驱动（General Purpose DMA Driver）

**配置项引用（Symbol References）**：[`CONFIG_DMA_ESP32`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_ESP32)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_GD32"></a>

## 79.46 `CONFIG_DMA_GD32`

**提示（Prompt）**：兆易创新（GigaDevice）GD32 DMA 驱动

**说明（Help）**

兆易创新（GigaDevice）GD32 系列微控制器（MCU）的 DMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_GD_GD32_DMA_ENABLED || DT_HAS_GD_GD32_DMA_V1_ENABLED) && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_GD32_DMA
```

**定义位置（Location）**：[`drivers/dma/Kconfig.gd32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.gd32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_USE_GD32_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_GD32_DMA)。

<a id="CONFIG_DMA_INFINEON"></a>

## 79.47 `CONFIG_DMA_INFINEON`

**提示（Prompt）**：Infineon 基于 PDL 的 DMAC 驱动（PDL-Based Driver）

**说明（Help）**

此选项启用英飞凌（Infineon）系列基于 PDL 的 DMAC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_DMAC_ENABLED && !CONFIG_USE_INFINEON_LEGACY_HAL && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_INFINEON_DMA
```

**定义位置（Location）**：[`drivers/dma/Kconfig.infineon:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.infineon#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_USE_INFINEON_LEGACY_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_LEGACY_HAL)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_USE_INFINEON_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_DMA)。

<a id="CONFIG_DMA_INFINEON_CAT1_HAL"></a>

## 79.48 `CONFIG_DMA_INFINEON_CAT1_HAL`

**提示（Prompt）**：Infineon CAT1 基于旧版 HAL 的 DMA 驱动（Legacy HAL-Based Driver）

**说明（Help）**

此选项启用英飞凌（Infineon）CAT1 系列基于旧版硬件抽象层（HAL）的 DMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_DMA_ENABLED && CONFIG_USE_INFINEON_LEGACY_HAL && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_INFINEON_DMA
```

**定义位置（Location）**：[`drivers/dma/Kconfig.infineon:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.infineon#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_USE_INFINEON_LEGACY_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_LEGACY_HAL)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_USE_INFINEON_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_DMA)。

<a id="CONFIG_DMA_INFINEON_CAT1_PDL"></a>

## 79.49 `CONFIG_DMA_INFINEON_CAT1_PDL`

**提示（Prompt）**：Infineon CAT1 基于 PDL 的 DMA 驱动（PDL-Based Driver）

**说明（Help）**

此选项启用英飞凌（Infineon）CAT1 系列基于 PDL 的 DMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_DMA_ENABLED && !CONFIG_USE_INFINEON_LEGACY_HAL && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_INFINEON_DMA
```

**定义位置（Location）**：[`drivers/dma/Kconfig.infineon:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.infineon#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_USE_INFINEON_LEGACY_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_LEGACY_HAL)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_USE_INFINEON_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_DMA)。

<a id="CONFIG_DMA_INFINEON_DESCRIPTOR_COUNT"></a>

## 79.50 `CONFIG_DMA_INFINEON_DESCRIPTOR_COUNT`

**提示（Prompt）**：每个通道可用的描述符（Descriptor）数量

**说明（Help）**

此选项决定为每个 DMA 通道分配的描述符（Descriptor）数量。必须设置为大于或等于 `1` 的值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_INFINEON_CAT1_PDL && CONFIG_DMA
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/dma/Kconfig.infineon:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.infineon#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → Infineon CAT1 基于 PDL 的 DMA 驱动（PDL-Based Driver）

**配置项引用（Symbol References）**：[`CONFIG_DMA_INFINEON_CAT1_PDL`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_INFINEON_CAT1_PDL)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_INFINEON_MDMA"></a>

## 79.51 `CONFIG_DMA_INFINEON_MDMA`

**提示（Prompt）**：Infineon M-DMA 驱动

**说明（Help）**

此选项为提供 MXSAXIDMAC IP 的英飞凌（Infineon）系列器件启用 M-DMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_MDMA_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.infineon_mdma:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.infineon_mdma#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_INFINEON_MDMA_DESCRIPTOR_COUNT"></a>

## 79.52 `CONFIG_DMA_INFINEON_MDMA_DESCRIPTOR_COUNT`

**提示（Prompt）**：每个 DMA 通道可用的描述符（Descriptor）数量

**说明（Help）**

此选项决定为每个 DMA 通道分配的描述符（Descriptor）数量，必须大于或等于 `1`。它同时限制 `dma_config()` 可接受的最大 `block_count`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_INFINEON_MDMA && CONFIG_DMA
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/dma/Kconfig.infineon_mdma:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.infineon_mdma#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → Infineon M-DMA 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_INFINEON_MDMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_INFINEON_MDMA)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_INIT_PRIORITY"></a>

## 79.53 `CONFIG_DMA_INIT_PRIORITY`

**提示（Prompt）**：DMA 初始化优先级（Init Priority）

**说明（Help）**

DMA 驱动设备的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEFAULT
```

**定义位置（Location）**：[`drivers/dma/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_KERNEL_INIT_PRIORITY_DEFAULT`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEFAULT)。

<a id="CONFIG_DMA_INTEL_ADSP_GPDMA"></a>

## 79.54 `CONFIG_DMA_INTEL_ADSP_GPDMA`

**提示（Prompt）**：Intel ADSP 通用直接内存访问驱动（General Purpose DMA Driver）

**说明（Help）**

Intel ADSP DMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_ADSP_GPDMA_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.intel_adsp_gpdma:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.intel_adsp_gpdma#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_INTEL_ADSP_GPDMA_DEBUG"></a>

## 79.55 `CONFIG_DMA_INTEL_ADSP_GPDMA_DEBUG`

**提示（Prompt）**：IP 寄存器调试转储（Debug Dump）

**说明（Help）**

转储 Intel ADSP GPDMA 寄存器以进行调试（Debug）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_INTEL_ADSP_GPDMA && CONFIG_DMA
```

**定义位置（Location）**：[`drivers/dma/Kconfig.intel_adsp_gpdma:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.intel_adsp_gpdma#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → Intel ADSP 通用直接内存访问驱动（General Purpose DMA Driver）

**配置项引用（Symbol References）**：[`CONFIG_DMA_INTEL_ADSP_GPDMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_INTEL_ADSP_GPDMA)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_INTEL_ADSP_GPDMA_HAS_LLP"></a>

## 79.56 `CONFIG_DMA_INTEL_ADSP_GPDMA_HAS_LLP`

**提示（Prompt）**：Intel ADSP GPDMA 线性链路位置功能（Linear Link Position Feature）

**说明（Help）**

Intel ADSP GPDMA 可能具有可选的线性链路位置功能（Linear Link Position Feature）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_INTEL_ADSP_GPDMA && CONFIG_DMA
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_SERIES_INTEL_ADSP_ACE
```

**定义位置（Location）**：[`drivers/dma/Kconfig.intel_adsp_gpdma:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.intel_adsp_gpdma#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → Intel ADSP 通用直接内存访问驱动（General Purpose DMA Driver）

**配置项引用（Symbol References）**：[`CONFIG_DMA_INTEL_ADSP_GPDMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_INTEL_ADSP_GPDMA)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_ACE)。

<a id="CONFIG_DMA_INTEL_ADSP_GPDMA_NEED_CONTROLLER_OWNERSHIP"></a>

## 79.57 `CONFIG_DMA_INTEL_ADSP_GPDMA_NEED_CONTROLLER_OWNERSHIP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏选项（Hidden Option），用于指示驱动需要向主机申请 DMA 控制器所有权（Ownership）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_INTEL_ADSP_GPDMA && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.intel_adsp_gpdma:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.intel_adsp_gpdma#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → Intel ADSP 通用直接内存访问驱动（General Purpose DMA Driver）

**配置项引用（Symbol References）**：[`CONFIG_DMA_INTEL_ADSP_GPDMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_INTEL_ADSP_GPDMA)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_INTEL_ADSP_HDA"></a>

## 79.58 `CONFIG_DMA_INTEL_ADSP_HDA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Intel ADSP HDA DMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_DMA_INTEL_ADSP_HDA_LINK_OUT || CONFIG_DMA_INTEL_ADSP_HDA_LINK_IN || CONFIG_DMA_INTEL_ADSP_HDA_HOST_OUT || CONFIG_DMA_INTEL_ADSP_HDA_HOST_IN) && CONFIG_DMA
```

**被选择（Selected by）**

```text
CONFIG_DMA_INTEL_ADSP_HDA_HOST_IN
CONFIG_DMA_INTEL_ADSP_HDA_HOST_OUT
CONFIG_DMA_INTEL_ADSP_HDA_LINK_IN
CONFIG_DMA_INTEL_ADSP_HDA_LINK_OUT
```

**定义位置（Location）**：[`drivers/dma/Kconfig.intel_adsp_hda:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.intel_adsp_hda#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_INTEL_ADSP_HDA_LINK_OUT`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_INTEL_ADSP_HDA_LINK_OUT)、[`CONFIG_DMA_INTEL_ADSP_HDA_LINK_IN`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_INTEL_ADSP_HDA_LINK_IN)、[`CONFIG_DMA_INTEL_ADSP_HDA_HOST_OUT`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_INTEL_ADSP_HDA_HOST_OUT)、[`CONFIG_DMA_INTEL_ADSP_HDA_HOST_IN`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_INTEL_ADSP_HDA_HOST_IN)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_INTEL_ADSP_HDA_HOST_IN"></a>

## 79.59 `CONFIG_DMA_INTEL_ADSP_HDA_HOST_IN`

**提示（Prompt）**：Intel ADSP HDA 主机输入（Host In）DMA 驱动

**说明（Help）**

Intel ADSP 主机（Host）HDA DMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_ADSP_HDA_HOST_IN_ENABLED && CONFIG_DMA && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DMA_INTEL_ADSP_HDA
```

**定义位置（Location）**：[`drivers/dma/Kconfig.intel_adsp_hda:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.intel_adsp_hda#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_DMA_INTEL_ADSP_HDA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_INTEL_ADSP_HDA)。

<a id="CONFIG_DMA_INTEL_ADSP_HDA_HOST_OUT"></a>

## 79.60 `CONFIG_DMA_INTEL_ADSP_HDA_HOST_OUT`

**提示（Prompt）**：Intel ADSP HDA 主机输出（Host Out）DMA 驱动

**说明（Help）**

Intel ADSP 主机（Host）HDA DMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_ADSP_HDA_HOST_OUT_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DMA_INTEL_ADSP_HDA
```

**定义位置（Location）**：[`drivers/dma/Kconfig.intel_adsp_hda:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.intel_adsp_hda#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_DMA_INTEL_ADSP_HDA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_INTEL_ADSP_HDA)。

<a id="CONFIG_DMA_INTEL_ADSP_HDA_LINK_IN"></a>

## 79.61 `CONFIG_DMA_INTEL_ADSP_HDA_LINK_IN`

**提示（Prompt）**：Intel ADSP HDA 链路输入（Link In）DMA 驱动

**说明（Help）**

Intel ADSP 链路输入（Link In）HDA DMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_ADSP_HDA_LINK_IN_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DMA_INTEL_ADSP_HDA
```

**定义位置（Location）**：[`drivers/dma/Kconfig.intel_adsp_hda:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.intel_adsp_hda#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_DMA_INTEL_ADSP_HDA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_INTEL_ADSP_HDA)。

<a id="CONFIG_DMA_INTEL_ADSP_HDA_LINK_OUT"></a>

## 79.62 `CONFIG_DMA_INTEL_ADSP_HDA_LINK_OUT`

**提示（Prompt）**：Intel ADSP HDA 链路输出（Link Out）DMA 驱动

**说明（Help）**

Intel ADSP 链路输出（Link Out）HDA DMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_ADSP_HDA_LINK_OUT_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DMA_INTEL_ADSP_HDA
```

**定义位置（Location）**：[`drivers/dma/Kconfig.intel_adsp_hda:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.intel_adsp_hda#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_DMA_INTEL_ADSP_HDA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_INTEL_ADSP_HDA)。

<a id="CONFIG_DMA_INTEL_ADSP_HDA_TIMING_L1_EXIT"></a>

## 79.63 `CONFIG_DMA_INTEL_ADSP_HDA_TIMING_L1_EXIT`

**提示（Prompt）**：Intel ADSP HDA 主机 L1 退出中断（L1 Exit Interrupt）

**说明（Help）**

用于退出 L1 的 Intel ADSP HDA 主机中断（Host Interrupt）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_DMA_INTEL_ADSP_HDA_HOST_IN || CONFIG_DMA_INTEL_ADSP_HDA_HOST_OUT) && CONFIG_DMA
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_SERIES_INTEL_ADSP_ACE
```

**定义位置（Location）**：[`drivers/dma/Kconfig.intel_adsp_hda:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.intel_adsp_hda#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_INTEL_ADSP_HDA_HOST_IN`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_INTEL_ADSP_HDA_HOST_IN)、[`CONFIG_DMA_INTEL_ADSP_HDA_HOST_OUT`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_INTEL_ADSP_HDA_HOST_OUT)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_ACE)。

<a id="CONFIG_DMA_INTEL_LPSS"></a>

## 79.64 `CONFIG_DMA_INTEL_LPSS`

**提示（Prompt）**：Intel LPSS DMA 驱动

**说明（Help）**

Intel LPSS DMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_LPSS_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DEVICE_DEPS
```

**被选择（Selected by）**

```text
CONFIG_I2C_DW_LPSS_DMA
CONFIG_SPI_PW_LPSS_DMA
```

**定义位置（Location）**：[`drivers/dma/Kconfig.intel_lpss:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.intel_lpss#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_DEVICE_DEPS`](P001_kernel_配置项参考_1.md#CONFIG_DEVICE_DEPS)、[`CONFIG_I2C_DW_LPSS_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_DW_LPSS_DMA)、[`CONFIG_SPI_PW_LPSS_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_PW_LPSS_DMA)。

<a id="CONFIG_DMA_IPROC_PAX"></a>

## 79.65 `CONFIG_DMA_IPROC_PAX`

**提示（Prompt）**：Broadcom PAX（PCIE↔AXI）DMA 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BRCM_IPROC_PAX_DMA_V1_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PCIE_ENDPOINT
```

**定义位置（Location）**：[`drivers/dma/Kconfig.iproc_pax:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.iproc_pax#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_PCIE_ENDPOINT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PCIE_ENDPOINT)。

<a id="CONFIG_DMA_IPROC_PAX_DEBUG"></a>

## 79.66 `CONFIG_DMA_IPROC_PAX_DEBUG`

**提示（Prompt）**：PAX DMA 严格调试检查（Paranoid Debug Checks）

**说明（Help）**

为每个 DMA 数据包（Packet）增加严格的缓冲区地址和大小对齐（Alignment）检查。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_DMA_IPROC_PAX || CONFIG_DMA_IPROC_PAX_V2) && CONFIG_DMA
```

**定义位置（Location）**：[`drivers/dma/Kconfig.iproc_pax:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.iproc_pax#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_IPROC_PAX`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_IPROC_PAX)、[`CONFIG_DMA_IPROC_PAX_V2`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_IPROC_PAX_V2)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_IPROC_PAX_DOORBELL_MODE"></a>

## 79.67 `CONFIG_DMA_IPROC_PAX_DOORBELL_MODE`

**提示（Prompt）**：PAX DMA 环形队列门铃模式（Ring Doorbell Mode）

**说明（Help）**

PAX DMA 硬件环形队列（Hardware Ring）以门铃模式（Doorbell Mode）运行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/dma/Kconfig.iproc_pax:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.iproc_pax#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → PAX DMA 环形队列操作模式（Ring Operation Mode）

<a id="CONFIG_DMA_IPROC_PAX_IRQ_SYNC"></a>

## 79.68 `CONFIG_DMA_IPROC_PAX_IRQ_SYNC`

**提示（Prompt）**：支持中断（Interrupt）的 PAX DMA 同步 API（Synchronous API）

**说明（Help）**

PAX DMA API 会阻塞，直到环形队列中断处理程序（Ring Interrupt Handler）发出 DMA 完成通知（Completion Alert）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/dma/Kconfig.iproc_pax:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.iproc_pax#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → PAX DMA API 模式（API Modes）

<a id="CONFIG_DMA_IPROC_PAX_POLL_MODE"></a>

## 79.69 `CONFIG_DMA_IPROC_PAX_POLL_MODE`

**提示（Prompt）**：轮询模式（Polling Mode）的 PAX DMA API

**说明（Help）**

PAX DMA API 通过轮询（Polling）检查 DMA 是否完成。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/dma/Kconfig.iproc_pax:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.iproc_pax#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → PAX DMA API 模式（API Modes）

<a id="CONFIG_DMA_IPROC_PAX_TOGGLE_MODE"></a>

## 79.70 `CONFIG_DMA_IPROC_PAX_TOGGLE_MODE`

**提示（Prompt）**：PAX DMA 环形队列切换模式（Ring Toggle Mode）

**说明（Help）**

PAX DMA 硬件环形队列（Hardware Ring）以切换模式（Toggle Mode）运行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/dma/Kconfig.iproc_pax:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.iproc_pax#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → PAX DMA 环形队列操作模式（Ring Operation Mode）

<a id="CONFIG_DMA_IPROC_PAX_V2"></a>

## 79.71 `CONFIG_DMA_IPROC_PAX_V2`

**提示（Prompt）**：Broadcom PAX（PCIE↔AXI）DMA 驱动第 2 版（Version 2）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BRCM_IPROC_PAX_DMA_V2_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PCIE_ENDPOINT
```

**定义位置（Location）**：[`drivers/dma/Kconfig.iproc_pax:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.iproc_pax#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_PCIE_ENDPOINT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PCIE_ENDPOINT)。

<a id="CONFIG_DMA_IPROC_PAX_V2_INIT_PRIORITY"></a>

## 79.72 `CONFIG_DMA_IPROC_PAX_V2_INIT_PRIORITY`

**提示（Prompt）**：Broadcom PAX v2 初始化优先级（Initialization Priority）

**说明（Help）**

Broadcom PAX v2 的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_IPROC_PAX_V2 && CONFIG_DMA
```

**默认值（Defaults）**

```text
51
```

**定义位置（Location）**：[`drivers/dma/Kconfig.iproc_pax:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.iproc_pax#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → Broadcom PAX（PCIE↔AXI）DMA 驱动第 2 版（Version 2）

**配置项引用（Symbol References）**：[`CONFIG_DMA_IPROC_PAX_V2`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_IPROC_PAX_V2)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_MAX32"></a>

## 79.73 `CONFIG_DMA_MAX32`

**提示（Prompt）**：MAX32 微控制器（MCU）DMA 驱动

**说明（Help）**

为 MAX32 系列处理器启用 DMA 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX32_DMA_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.max32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.max32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_MAX_DESCRIPTOR"></a>

## 79.74 `CONFIG_DMA_MAX_DESCRIPTOR`

**提示（Prompt）**：`block_config`（`LDMA_Descriptor`）最大数量

**说明（Help）**

`block_config`（`LDMA_Descriptor`）最大数量

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_SILABS_LDMA && CONFIG_DMA
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`drivers/dma/Kconfig.silabs:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.silabs#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → Silabs DMA 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_SILABS_LDMA`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_SILABS_LDMA)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_MCHP_DMAC_G1"></a>

## 79.75 `CONFIG_DMA_MCHP_DMAC_G1`

**提示（Prompt）**：Microchip G1 DMA 驱动

**说明（Help）**

启用 Microchip 微控制器（MCU）的 G1 DMA 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_DMAC_G1_DMA_ENABLED && !CONFIG_DMA_64BIT && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.mchp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.mchp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_64BIT`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_64BIT)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_MCHP_DMAC_G2"></a>

## 79.76 `CONFIG_DMA_MCHP_DMAC_G2`

**提示（Prompt）**：Microchip G2 DMA 驱动

**说明（Help）**

启用 Microchip 微控制器（MCU）的 G2 DMA 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_DMAC_G2_DMA_ENABLED && !CONFIG_DMA_64BIT && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.mchp:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.mchp#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_64BIT`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_64BIT)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_MCHP_DMAC_G3"></a>

## 79.77 `CONFIG_DMA_MCHP_DMAC_G3`

**提示（Prompt）**：Microchip G3 DMA 驱动

**说明（Help）**

启用 Microchip 微控制器（MCU）的 G3 DMA 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_DMAC_G3_DMA_ENABLED && !CONFIG_DMA_64BIT && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.mchp:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.mchp#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_64BIT`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_64BIT)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_MCHP_XEC"></a>

## 79.78 `CONFIG_DMA_MCHP_XEC`

**提示（Prompt）**：Microchip XEC 系列 DMAC 驱动

**说明（Help）**

Microchip XEC 系列微控制器（MCU）的 DMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_XEC_DMAC_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.xec:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.xec#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_MCHP_XEC_DMAC_MAX_CHANNELS"></a>

## 79.79 `CONFIG_DMA_MCHP_XEC_DMAC_MAX_CHANNELS`

**提示（Prompt）**：Microchip XEC 中央 DMA（Central DMA）的最大通道数

**说明（Help）**

此 DMAC 控制器实例支持的通道（Channel）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_MCHP_XEC && CONFIG_DMA
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/dma/Kconfig.xec:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.xec#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → Microchip XEC 系列 DMAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_MCHP_XEC`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_MCHP_XEC)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_MCHP_XEC_MAX_BLOCKS_PER_CHAN"></a>

## 79.80 `CONFIG_DMA_MCHP_XEC_MAX_BLOCKS_PER_CHAN`

**提示（Prompt）**：每个通道的最大 DMA 块数量（Maximum DMA Blocks Per Channel）

**说明（Help）**

驱动从一次多块 `dma_config` 调用中缓存的 `dma_block_config` 条目的最大数量。XEC 中央 DMA（Central DMA）硬件每次只配置一个块；驱动在中断服务程序（ISR）中连接后续块：先对通道执行 `ABORT`，再根据缓存的块重写 `MSA` / `MEA` / `DEVA`，然后重新发出 `RUN`。每缓存一个块，每个通道约需 16 字节。将此值设为默认的 `1`，可逐位保持历史单块行为一致，并使 RAM 占用最低。当外设驱动需要在同一个从 `START` 到 `STOP` 的事务（Transaction）中进行乒乓（Ping-Pong）或分散式（Scatter-Style）传输时，应增大此值。例如，在 I2Cv3-NL 驱动中进行目标模式（Target Mode）的流式接收（RX），且主机可能写入大于每实例接收缓冲区的有效载荷（Payload）时。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_MCHP_XEC && CONFIG_DMA
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 16]
```

**定义位置（Location）**：[`drivers/dma/Kconfig.xec:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.xec#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → Microchip XEC 系列 DMAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_MCHP_XEC`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_MCHP_XEC)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_MCUX_EDMA"></a>

## 79.81 `CONFIG_DMA_MCUX_EDMA`

**提示（Prompt）**：MCUX DMA 驱动

**说明（Help）**

用于具有 EDMA IP 的 MCUX 系列 SoC 的第 2 版（Version 2）DMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_NOCACHE_MEMORY
```

**定义位置（Location）**：[`drivers/dma/Kconfig.mcux_edma:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.mcux_edma#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)。

<a id="CONFIG_DMA_MCUX_EDMA_DMAMUX"></a>

## 79.82 `CONFIG_DMA_MCUX_EDMA_DMAMUX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

当 EDMA 设备树（Devicetree）节点具有 `has-dmamux` 属性时自动启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA
```

**默认值（Defaults）**

```text
CONFIG_DMA_MCUX_EDMA || n
```

**定义位置（Location）**：[`drivers/dma/Kconfig.mcux_edma:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.mcux_edma#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_DMA_MCUX_EDMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_MCUX_EDMA)。

<a id="CONFIG_DMA_MCUX_EDMA_V3"></a>

## 79.83 `CONFIG_DMA_MCUX_EDMA_V3`

**提示（Prompt）**：MCUX DMA v3 驱动

**说明（Help）**

用于具有 DMA3 IP 的 MCUX 系列 SoC 的第 3 版（Version 3）DMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_NOCACHE_MEMORY
```

**定义位置（Location）**：[`drivers/dma/Kconfig.mcux_edma:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.mcux_edma#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)。

<a id="CONFIG_DMA_MCUX_EDMA_V4"></a>

## 79.84 `CONFIG_DMA_MCUX_EDMA_V4`

**提示（Prompt）**：MCUX 统一 DMA 驱动（DMA UNIFIED Driver）

**说明（Help）**

用于配备多种 EDMA IP（EDMA、DMA3、EDMA4、EDMA5）的 MCUX 系列 SoC 的第 4 版（Version 4）DMA 驱动。EDMA4 驱动兼容不同的 EDMA IP，允许在同一工程中使用不同的 EDMA IP。不过，这需要 SDK 器件头文件（Device Header）提供额外支持，因此只有新的 SoC 能够使用它。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(n || n) && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_NOCACHE_MEMORY if CONFIG_CPU_HAS_DCACHE
```

**定义位置（Location）**：[`drivers/dma/Kconfig.mcux_edma:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.mcux_edma#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_CPU_HAS_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCACHE)。

<a id="CONFIG_DMA_MCUX_LPC"></a>

## 79.85 `CONFIG_DMA_MCUX_LPC`

**提示（Prompt）**：MCUX LPC DMAC 驱动

**说明（Help）**

MCUX LPC 微控制器（MCU）的 DMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPC_DMA_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NXP_INPUTMUX
```

**定义位置（Location）**：[`drivers/dma/Kconfig.mcux_lpc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.mcux_lpc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_NXP_INPUTMUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_INPUTMUX)。

<a id="CONFIG_DMA_MCUX_LPC_NUMBER_OF_CHANNELS_ALLOCATED"></a>

## 79.86 `CONFIG_DMA_MCUX_LPC_NUMBER_OF_CHANNELS_ALLOCATED`

**提示（Prompt）**：驱动中需要为其分配内存的 DMA 通道（Channel）数量

**说明（Help）**

MCUX LPC DMA 驱动可根据此值省去部分静态数据分配，从而节省内存。因此，应用程序可将此值设为符合自身需求的数值，以节省数据内存。该值表示“预计整个运行过程中会使用的不同 DMA 通道总数，并在所有 DMA 控制器中取最大值”。默认值 `0` 表示：按照任一 DMA 控制器硬件的最大通道数，分配对应数量的通道数据结构（Channel Data Structure）。精细调整此 Kconfig 选项，每少分配 3–4 个未使用的通道，大约可节省 1 KB。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_MCUX_LPC && CONFIG_DMA
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/dma/Kconfig.mcux_lpc:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.mcux_lpc#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → MCUX LPC DMAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_MCUX_LPC`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_MCUX_LPC)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_MCUX_LPC_NUMBER_OF_DESCRIPTORS"></a>

## 79.87 `CONFIG_DMA_MCUX_LPC_NUMBER_OF_DESCRIPTORS`

**提示（Prompt）**：使用的 DMA 描述符（Descriptor）数量

**说明（Help）**

每个 DMA 描述符（Descriptor）可用于传输 `(1024*width)` 字节的数据。应根据应用程序传输的最大数据量增大或减小此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_MCUX_LPC && CONFIG_DMA
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`drivers/dma/Kconfig.mcux_lpc:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.mcux_lpc#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → MCUX LPC DMAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_MCUX_LPC`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_MCUX_LPC)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_MCUX_SMARTDMA"></a>

## 79.88 `CONFIG_DMA_MCUX_SMARTDMA`

**提示（Prompt）**：MCUX SmartDMA 驱动

**说明（Help）**

MCUX SmartDMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_SMARTDMA_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NXP_INPUTMUX
```

**定义位置（Location）**：[`drivers/dma/Kconfig.mcux_smartdma:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.mcux_smartdma#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_NXP_INPUTMUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_INPUTMUX)。

<a id="CONFIG_DMA_MCUX_TEST_SLOT_START"></a>

## 79.89 `CONFIG_DMA_MCUX_TEST_SLOT_START`

**提示（Prompt）**：测试槽起始编号（Test Slot Start Number）

**说明（Help）**

测试槽起始编号（Test Slot Start Number）

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_K6X || CONFIG_SOC_SERIES_KE1XF || CONFIG_SOC_SERIES_S32K3 || CONFIG_SOC_SERIES_S32ZE || CONFIG_SOC_SERIES_KE1XZ || CONFIG_SOC_SERIES_MCXE24X || CONFIG_SOC_SERIES_MCXE31X) && (CONFIG_DMA_MCUX_EDMA || CONFIG_DMA_MCUX_EDMA_V3 || CONFIG_DMA_MCUX_EDMA_V4) && CONFIG_DMA
```

**默认值（Defaults）**

```text
58 if CONFIG_SOC_SERIES_K6X
60 if CONFIG_SOC_SERIES_KE1XF
60 if CONFIG_SOC_SERIES_KE1XZ
62 if CONFIG_SOC_SERIES_S32K3 || CONFIG_SOC_SERIES_S32ZE || CONFIG_SOC_SERIES_MCXE24X || CONFIG_SOC_SERIES_MCXE31X
```

**定义位置（Location）**：[`drivers/dma/Kconfig.mcux_edma:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.mcux_edma#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_K6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K6X)、[`CONFIG_SOC_SERIES_KE1XF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KE1XF)、[`CONFIG_SOC_SERIES_S32K3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K3)、[`CONFIG_SOC_SERIES_S32ZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32ZE)、[`CONFIG_SOC_SERIES_KE1XZ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KE1XZ)、[`CONFIG_SOC_SERIES_MCXE24X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE24X)、[`CONFIG_SOC_SERIES_MCXE31X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE31X)、[`CONFIG_DMA_MCUX_EDMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_MCUX_EDMA)、[`CONFIG_DMA_MCUX_EDMA_V3`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_MCUX_EDMA_V3)、[`CONFIG_DMA_MCUX_EDMA_V4`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_MCUX_EDMA_V4)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_K6X`、`CONFIG_SOC_SERIES_KE1XF`、`CONFIG_SOC_SERIES_S32K3`、`CONFIG_SOC_SERIES_S32ZE`、`CONFIG_SOC_SERIES_KE1XZ`、`CONFIG_SOC_SERIES_MCXE24X`、`CONFIG_SOC_SERIES_MCXE31X`。

<a id="CONFIG_DMA_MCUX_USE_DTCM_FOR_DMA_DESCRIPTORS"></a>

## 79.90 `CONFIG_DMA_MCUX_USE_DTCM_FOR_DMA_DESCRIPTORS`

**提示（Prompt）**：使用 DTCM 存放 DMA 描述符（Descriptor）

**说明（Help）**

启用此选项时，DMA 传输描述符（Descriptor）位于数据紧耦合内存（Data Tightly Coupled Memory，DTCM）中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.mcux_edma:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.mcux_edma#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

<a id="CONFIG_DMA_NIOS2_MSGDMA"></a>

## 79.91 `CONFIG_DMA_NIOS2_MSGDMA`

**提示（Prompt）**：Nios-II 模块化分散/聚集 DMA 驱动（Modular Scatter-Gather DMA，MSGDMA）

**说明（Help）**

启用 Nios-II 模块化分散/聚集 DMA（Modular Scatter-Gather DMA，MSGDMA）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ALTR_MSGDMA_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.nios2_msgdma:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.nios2_msgdma#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_NPCX_GDMA"></a>

## 79.92 `CONFIG_DMA_NPCX_GDMA`

**提示（Prompt）**：NPCX GDMA 驱动

**说明（Help）**

NPCX 系列的 GDMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NPCX_GDMA_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.npcx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.npcx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_NPCX_GDMA_EX"></a>

## 79.93 `CONFIG_DMA_NPCX_GDMA_EX`

**提示（Prompt）**：扩展 NPCX GDMA 驱动支持（Extended Support）

**说明（Help）**

此选项为 NPCKn 处理器变体（Variant）启用扩展 GDMA 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.npcx:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.npcx#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

<a id="CONFIG_DMA_NXP_4CH_DMA"></a>

## 79.94 `CONFIG_DMA_NXP_4CH_DMA`

**提示（Prompt）**：NXP 四通道 DMA 驱动（4-Channel DMA Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_4CH_DMA_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.nxp_4ch_dma:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.nxp_4ch_dma#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_NXP_EDMA"></a>

## 79.95 `CONFIG_DMA_NXP_EDMA`

**提示（Prompt）**：NXP 增强型直接内存访问驱动（Enhanced Direct Memory Access，eDMA）

**说明（Help）**

启用 NXP eDMA IP 的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_EDMA_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.nxp_edma:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.nxp_edma#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_NXP_EDMA_ALIGN"></a>

## 79.96 `CONFIG_DMA_NXP_EDMA_ALIGN`

**提示（Prompt）**：传输要求的对齐（Alignment），以字节为单位

**说明（Help）**

设置传输所需的对齐（Alignment），以字节为单位。使用本驱动的组件据此调整参与传输的内存区域的地址和大小。此值必须匹配 `SSIZE` 和 `DSIZE` 的某个可用值，否则驱动在配置时会返回错误。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_NXP_EDMA && CONFIG_DMA
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/dma/Kconfig.nxp_edma:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.nxp_edma#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → NXP 增强型直接内存访问驱动（Enhanced Direct Memory Access，eDMA）

**配置项引用（Symbol References）**：[`CONFIG_DMA_NXP_EDMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_NXP_EDMA)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_NXP_EDMA_ENABLE_HALFMAJOR_IRQ"></a>

## 79.97 `CONFIG_DMA_NXP_EDMA_ENABLE_HALFMAJOR_IRQ`

**提示（Prompt）**：需要在 `CITER = BITER / 2` 时中断 CPU 则设置此项

**说明（Help）**

如果需要在 `CITER = BITER / 2` 时中断 CPU，则启用此配置。启用后，CPU 会在 `CITER = BITER` 以及 `CITER = BITER / 2` 时收到中断（Interrupt）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_NXP_EDMA && CONFIG_DMA
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/dma/Kconfig.nxp_edma:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.nxp_edma#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → NXP 增强型直接内存访问驱动（Enhanced Direct Memory Access，eDMA）

**配置项引用（Symbol References）**：[`CONFIG_DMA_NXP_EDMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_NXP_EDMA)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_NXP_GDMA"></a>

## 79.98 `CONFIG_DMA_NXP_GDMA`

**提示（Prompt）**：NXP GDMA 驱动

**说明（Help）**

NXP 通用 DMA（General DMA，GDMA）控制器的驱动。此驱动支持内存到内存（Memory-to-Memory）、内存到外设（Memory-to-Peripheral）和外设到内存（Peripheral-to-Memory）的传输。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_GDMA_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.nxp_gdma:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.nxp_gdma#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_NXP_SDMA"></a>

## 79.99 `CONFIG_DMA_NXP_SDMA`

**提示（Prompt）**：NXP SDMA 驱动

**说明（Help）**

启用 NXP SDMA IP 的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_SDMA_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.nxp_sdma:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.nxp_sdma#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_NXP_SOF_HOST_DMA"></a>

## 79.100 `CONFIG_DMA_NXP_SOF_HOST_DMA`

**提示（Prompt）**：SOF 主机组件（Host Component）使用的 NXP DMA 驱动

**说明（Help）**

启用 Sound Open Firmware（SOF）主机组件（Host Component）使用的 NXP DMA 驱动。具体而言，SOF 主机组件使用此驱动在主机内存与固件本地内存（Firmware Local Memory）之间传输数据；这两类内存无需实际的 DMA 引擎（DMA Engine）即可访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_SOF_HOST_DMA_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.nxp_sof_host_dma:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.nxp_sof_host_dma#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<!-- kconfig-navigation -->

[上一章](P078_drivers_display_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P080_drivers_dma_配置项参考_2.md)
