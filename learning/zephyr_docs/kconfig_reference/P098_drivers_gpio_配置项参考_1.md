---
id: learning.zephyr-docs.kconfig-reference.page-98
title: "`drivers/gpio`配置项参考（1/3）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第98章\_`drivers/gpio`配置项参考（1/3）

本章翻译官方 Kconfig 数据库中 `drivers/gpio` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_GPIO"></a>

## 98.1 `CONFIG_GPIO`

**提示（Prompt）**：通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**说明（Help）**

将 GPIO 驱动纳入系统配置（System Configuration）

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ADC_ADS131M02
CONFIG_ADC_ADS1118
CONFIG_AUDIO_CODEC_CS35L5X_RESET
CONFIG_AUDIO_CODEC_CS43L22
CONFIG_AUXDISPLAY_GPIO_7SEG
CONFIG_AUXDISPLAY_HD44780
CONFIG_AUXDISPLAY_ITRON
CONFIG_AUXDISPLAY_TM1637
CONFIG_BT_DA1453X
CONFIG_BT_AMBIQ_HCI
CONFIG_BT_AIROC
CONFIG_BT_H4_NXP_CTLR
CONFIG_BUZZER_GPIO
CONFIG_CAN_TRANSCEIVER_GPIO
CONFIG_CHARGER_GPIO
CONFIG_CHARGER_MAX20335
CONFIG_CHARGER_PF1550
CONFIG_DALI_PWM
CONFIG_SDMMC_STM32
CONFIG_DISPLAY_CHARLIEPLEX_LED_MATRIX
CONFIG_EK79007
CONFIG_HUB12
CONFIG_ILI9881C_DSI
CONFIG_NT35510
CONFIG_OTM8009A
CONFIG_STM32_LTDC
CONFIG_PHY_MICROCHIP_KSZ8081
CONFIG_PHY_MICROCHIP_KSZ9131
CONFIG_PHY_MICROCHIP_VSC8541
CONFIG_PHY_TI_DP83825
CONFIG_PHY_TI_DP83867
CONFIG_PHY_REALTEK_RTL8211F
CONFIG_PHY_MAXLINEAR_GPY111
CONFIG_ETH_W5100S
CONFIG_ETH_W5500
CONFIG_ETH_W6100
CONFIG_ETH_W6300
CONFIG_SLG47910_FPGA
CONFIG_HAPTICS_CS40L26_RESET
CONFIG_HAPTICS_CS40L26_INTERRUPT
CONFIG_HAPTICS_CS40L5X_RESET
CONFIG_HAPTICS_CS40L5X_INTERRUPT
CONFIG_HAPTICS_CS40L5X_TRIGGER
CONFIG_I2S_SILABS_SIWX91X
CONFIG_IEEE802154_RF2XX
CONFIG_INPUT_BFLB_IRX
CONFIG_INPUT_CHSC5X
CONFIG_INPUT_CHSC6X
CONFIG_INPUT_GPIO_KEYS
CONFIG_INPUT_PINNACLE
CONFIG_INPUT_RENESAS_RA_CTSU
CONFIG_INPUT_VS1838B
CONFIG_LED_GPIO
CONFIG_TLC59731_STRIP
CONFIG_WS2812_STRIP_BFLB_WO
CONFIG_LIN_TRANSCEIVER_GPIO
CONFIG_LORA_SX127X
CONFIG_LORA_SX126X
CONFIG_LORA_STM32WL_SUBGHZ_RADIO
CONFIG_LORA_RYLRXXX
CONFIG_LORA_LR11XX_NATIVE
CONFIG_LORA_SX126X_NATIVE
CONFIG_MIPI_DBI_BITBANG
CONFIG_MIPI_DBI_RPI_PICO_PIO
CONFIG_MIPI_DBI_STM32_FMC
CONFIG_ESP_HOSTED_MCU
CONFIG_TI_TDP2004
CONFIG_MODEM_CELLULAR
CONFIG_MSPI_AMBIQ_CONTROLLER
CONFIG_MSPI_CDNS
CONFIG_MSPI_EMUL
CONFIG_MUX_ADI_ADGM3121
CONFIG_REGULATOR_GPIO
CONFIG_SDHC_AMBIQ
CONFIG_SDHC_AMEBA
CONFIG_RCAR_MMC
CONFIG_SDHC_STM32_SDMMC
CONFIG_AD2S1210
CONFIG_MAX30009_TRIGGER_GLOBAL_THREAD
CONFIG_MAX30009_TRIGGER_OWN_THREAD
CONFIG_IIS328DQ
CONFIG_IIS3DWB
CONFIG_LIS2DE12
CONFIG_LIS2DU12
CONFIG_LIS2DUX12
CONFIG_LPS2XDF
CONFIG_LSM6DSO
CONFIG_LSM6DSV16X
CONFIG_LSM6DSVXXX
CONFIG_VL53L1X
CONFIG_ICM566XX_TRIGGER_GLOBAL_THREAD
CONFIG_ICM566XX_TRIGGER_OWN_THREAD
CONFIG_TMAG5273
CONFIG_S9706
CONFIG_UART_STM32_ABNORMAL_RTS_ERRATUM_WORKAROUND
CONFIG_SPI_AMBIQ_SPIC
CONFIG_SPI_AMBIQ_SPID
CONFIG_SPI_INFINEON_HAL
CONFIG_SPI_INFINEON_PDL
CONFIG_SPI_MCHP_FLEXCOM_G1
CONFIG_SPI_MCHP_SERCOM_G1
CONFIG_SPI_MSPM0
CONFIG_SPI_NRFX
CONFIG_SPI_SAM
CONFIG_SPI_SILABS_SIWX91X_GSPI
CONFIG_SPI_XMC4XXX
CONFIG_STEPPER_ADI_TMCM3216
CONFIG_UDC_MCHP_UDPHS_G1
CONFIG_UDC_AMBIQ
CONFIG_USBC_VBUS_ADC
CONFIG_VIDEO_GC2145
CONFIG_VIDEO_HM0360
CONFIG_VIDEO_MCUX_FLEXIO
CONFIG_VIDEO_OV2640
CONFIG_VIDEO_OV5640
CONFIG_VIDEO_OV767X
CONFIG_VIDEO_OV9655
CONFIG_WDT_NXP_FS26
CONFIG_WIFI_ESP_HOSTED
CONFIG_WIFI_ESWIFI
CONFIG_WIFI_AIROC
CONFIG_WIFI_ST67W611M1
```

**被弱选择（Implied by）**

```text
CONFIG_MODEM_HL7800
CONFIG_MODEM_HL78XX
CONFIG_MODEM_SIM7080
CONFIG_MODEM_ST87MXX
CONFIG_MODEM_WNCM14A2A
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_mx8_dsi_oled1a/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_mx8_dsi_oled1a/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/nxp_mx9_dsi_oled/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_mx9_dsi_oled/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/st_b_cams_imx_mb1854/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/st_b_cams_imx_mb1854/Kconfig.defconfig)。

```text
y if CONFIG_VIDEO_STM32_DCMIPP
```

**定义位置（Location）**：[`drivers/gpio/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ADS131M02`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS131M02)、[`CONFIG_ADC_ADS1118`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS1118)、[`CONFIG_AUDIO_CODEC_CS35L5X_RESET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AUDIO_CODEC_CS35L5X_RESET)、[`CONFIG_AUDIO_CODEC_CS43L22`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC_CS43L22)、[`CONFIG_AUXDISPLAY_GPIO_7SEG`](P051_drivers_auxdisplay_配置项参考.md#CONFIG_AUXDISPLAY_GPIO_7SEG)、[`CONFIG_AUXDISPLAY_HD44780`](P051_drivers_auxdisplay_配置项参考.md#CONFIG_AUXDISPLAY_HD44780)、[`CONFIG_AUXDISPLAY_ITRON`](P051_drivers_auxdisplay_配置项参考.md#CONFIG_AUXDISPLAY_ITRON)、[`CONFIG_AUXDISPLAY_TM1637`](P051_drivers_auxdisplay_配置项参考.md#CONFIG_AUXDISPLAY_TM1637)、[`CONFIG_BT_DA1453X`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DA1453X)、[`CONFIG_BT_AMBIQ_HCI`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_AMBIQ_HCI)、[`CONFIG_BT_AIROC`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_AIROC)、[`CONFIG_BT_H4_NXP_CTLR`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_H4_NXP_CTLR)、[`CONFIG_BUZZER_GPIO`](P058_drivers_buzzer_配置项参考.md#CONFIG_BUZZER_GPIO)、[`CONFIG_CAN_TRANSCEIVER_GPIO`](P060_drivers_can_配置项参考.md#CONFIG_CAN_TRANSCEIVER_GPIO)、[`CONFIG_CHARGER_GPIO`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER_GPIO)、[`CONFIG_CHARGER_MAX20335`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER_MAX20335)、[`CONFIG_CHARGER_PF1550`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER_PF1550)、[`CONFIG_DALI_PWM`](P074_drivers_dali_配置项参考.md#CONFIG_DALI_PWM)、[`CONFIG_SDMMC_STM32`](P076_drivers_disk_配置项参考.md#CONFIG_SDMMC_STM32)、[`CONFIG_DISPLAY_CHARLIEPLEX_LED_MATRIX`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_CHARLIEPLEX_LED_MATRIX)、[`CONFIG_EK79007`](P077_drivers_display_配置项参考_1.md#CONFIG_EK79007)、[`CONFIG_HUB12`](P077_drivers_display_配置项参考_1.md#CONFIG_HUB12)、[`CONFIG_ILI9881C_DSI`](P077_drivers_display_配置项参考_1.md#CONFIG_ILI9881C_DSI)、[`CONFIG_NT35510`](P077_drivers_display_配置项参考_1.md#CONFIG_NT35510)、[`CONFIG_OTM8009A`](P077_drivers_display_配置项参考_1.md#CONFIG_OTM8009A)、[`CONFIG_STM32_LTDC`](P078_drivers_display_配置项参考_2.md#CONFIG_STM32_LTDC)、[`CONFIG_PHY_MICROCHIP_KSZ8081`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PHY_MICROCHIP_KSZ8081)、[`CONFIG_PHY_MICROCHIP_KSZ9131`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PHY_MICROCHIP_KSZ9131)、[`CONFIG_PHY_MICROCHIP_VSC8541`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PHY_MICROCHIP_VSC8541)、[`CONFIG_PHY_TI_DP83825`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PHY_TI_DP83825)、[`CONFIG_PHY_TI_DP83867`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PHY_TI_DP83867)、[`CONFIG_PHY_REALTEK_RTL8211F`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PHY_REALTEK_RTL8211F)、[`CONFIG_PHY_MAXLINEAR_GPY111`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PHY_MAXLINEAR_GPY111)、[`CONFIG_ETH_W5100S`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_W5100S)、[`CONFIG_ETH_W5500`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_W5500)、[`CONFIG_ETH_W6100`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_W6100)、[`CONFIG_ETH_W6300`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_W6300)、[`CONFIG_SLG47910_FPGA`](P095_drivers_fpga_配置项参考.md#CONFIG_SLG47910_FPGA)、[`CONFIG_HAPTICS_CS40L26_RESET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAPTICS_CS40L26_RESET)、[`CONFIG_HAPTICS_CS40L26_INTERRUPT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAPTICS_CS40L26_INTERRUPT)、[`CONFIG_HAPTICS_CS40L5X_RESET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAPTICS_CS40L5X_RESET)、[`CONFIG_HAPTICS_CS40L5X_INTERRUPT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAPTICS_CS40L5X_INTERRUPT)、[`CONFIG_HAPTICS_CS40L5X_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAPTICS_CS40L5X_TRIGGER)、[`CONFIG_I2S_SILABS_SIWX91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2S_SILABS_SIWX91X)、[`CONFIG_IEEE802154_RF2XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IEEE802154_RF2XX)、[`CONFIG_INPUT_BFLB_IRX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_BFLB_IRX)、[`CONFIG_INPUT_CHSC5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_CHSC5X)、[`CONFIG_INPUT_CHSC6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_CHSC6X)、[`CONFIG_INPUT_GPIO_KEYS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_GPIO_KEYS)、[`CONFIG_INPUT_PINNACLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_PINNACLE)、[`CONFIG_INPUT_RENESAS_RA_CTSU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_RENESAS_RA_CTSU)、[`CONFIG_INPUT_VS1838B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_VS1838B)、[`CONFIG_LED_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LED_GPIO)、[`CONFIG_TLC59731_STRIP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TLC59731_STRIP)、[`CONFIG_WS2812_STRIP_BFLB_WO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WS2812_STRIP_BFLB_WO)、[`CONFIG_LIN_TRANSCEIVER_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIN_TRANSCEIVER_GPIO)、[`CONFIG_LORA_SX127X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORA_SX127X)、[`CONFIG_LORA_SX126X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORA_SX126X)、[`CONFIG_LORA_STM32WL_SUBGHZ_RADIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORA_STM32WL_SUBGHZ_RADIO)、[`CONFIG_LORA_RYLRXXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORA_RYLRXXX)、[`CONFIG_LORA_LR11XX_NATIVE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORA_LR11XX_NATIVE)、[`CONFIG_LORA_SX126X_NATIVE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORA_SX126X_NATIVE)、[`CONFIG_MIPI_DBI_BITBANG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI_BITBANG)、[`CONFIG_MIPI_DBI_RPI_PICO_PIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI_RPI_PICO_PIO)、[`CONFIG_MIPI_DBI_STM32_FMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI_STM32_FMC)、[`CONFIG_ESP_HOSTED_MCU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_HOSTED_MCU)、[`CONFIG_TI_TDP2004`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TI_TDP2004)、[`CONFIG_MODEM_CELLULAR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_CELLULAR)、[`CONFIG_MSPI_AMBIQ_CONTROLLER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MSPI_AMBIQ_CONTROLLER)、[`CONFIG_MSPI_CDNS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MSPI_CDNS)、[`CONFIG_MSPI_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MSPI_EMUL)、[`CONFIG_MUX_ADI_ADGM3121`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MUX_ADI_ADGM3121)、[`CONFIG_REGULATOR_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REGULATOR_GPIO)、[`CONFIG_SDHC_AMBIQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SDHC_AMBIQ)、[`CONFIG_SDHC_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SDHC_AMEBA)、[`CONFIG_RCAR_MMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RCAR_MMC)、[`CONFIG_SDHC_STM32_SDMMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SDHC_STM32_SDMMC)、[`CONFIG_AD2S1210`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AD2S1210)、[`CONFIG_MAX30009_TRIGGER_GLOBAL_THREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MAX30009_TRIGGER_GLOBAL_THREAD)、[`CONFIG_MAX30009_TRIGGER_OWN_THREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MAX30009_TRIGGER_OWN_THREAD)、[`CONFIG_IIS328DQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IIS328DQ)、[`CONFIG_IIS3DWB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IIS3DWB)、[`CONFIG_LIS2DE12`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS2DE12)、[`CONFIG_LIS2DU12`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS2DU12)、[`CONFIG_LIS2DUX12`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS2DUX12)、[`CONFIG_LPS2XDF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LPS2XDF)、[`CONFIG_LSM6DSO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSO)、[`CONFIG_LSM6DSV16X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSV16X)、[`CONFIG_LSM6DSVXXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSVXXX)、[`CONFIG_VL53L1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VL53L1X)、[`CONFIG_ICM566XX_TRIGGER_GLOBAL_THREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICM566XX_TRIGGER_GLOBAL_THREAD)、[`CONFIG_ICM566XX_TRIGGER_OWN_THREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICM566XX_TRIGGER_OWN_THREAD)、[`CONFIG_TMAG5273`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TMAG5273)、[`CONFIG_S9706`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_S9706)、[`CONFIG_UART_STM32_ABNORMAL_RTS_ERRATUM_WORKAROUND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_STM32_ABNORMAL_RTS_ERRATUM_WORKAROUND)、[`CONFIG_SPI_AMBIQ_SPIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_AMBIQ_SPIC)、[`CONFIG_SPI_AMBIQ_SPID`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_AMBIQ_SPID)、[`CONFIG_SPI_INFINEON_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_INFINEON_HAL)、[`CONFIG_SPI_INFINEON_PDL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_INFINEON_PDL)、[`CONFIG_SPI_MCHP_FLEXCOM_G1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_MCHP_FLEXCOM_G1)、[`CONFIG_SPI_MCHP_SERCOM_G1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_MCHP_SERCOM_G1)、[`CONFIG_SPI_MSPM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_MSPM0)、[`CONFIG_SPI_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_NRFX)、[`CONFIG_SPI_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_SAM)、[`CONFIG_SPI_SILABS_SIWX91X_GSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_SILABS_SIWX91X_GSPI)、[`CONFIG_SPI_XMC4XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_XMC4XXX)、[`CONFIG_STEPPER_ADI_TMCM3216`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STEPPER_ADI_TMCM3216)、[`CONFIG_UDC_MCHP_UDPHS_G1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_MCHP_UDPHS_G1)、[`CONFIG_UDC_AMBIQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_AMBIQ)、[`CONFIG_USBC_VBUS_ADC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBC_VBUS_ADC)、[`CONFIG_VIDEO_GC2145`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_GC2145)、[`CONFIG_VIDEO_HM0360`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_HM0360)、[`CONFIG_VIDEO_MCUX_FLEXIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_MCUX_FLEXIO)、[`CONFIG_VIDEO_OV2640`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_OV2640)、[`CONFIG_VIDEO_OV5640`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_OV5640)、[`CONFIG_VIDEO_OV767X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_OV767X)、[`CONFIG_VIDEO_OV9655`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_OV9655)、[`CONFIG_WDT_NXP_FS26`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WDT_NXP_FS26)、[`CONFIG_WIFI_ESP_HOSTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP_HOSTED)、[`CONFIG_WIFI_ESWIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESWIFI)、[`CONFIG_WIFI_AIROC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_AIROC)、[`CONFIG_WIFI_ST67W611M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ST67W611M1)、[`CONFIG_MODEM_HL7800`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM_SIM7080`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_SIM7080)、[`CONFIG_MODEM_ST87MXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_ST87MXX)、[`CONFIG_MODEM_WNCM14A2A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_WNCM14A2A)、[`CONFIG_VIDEO_STM32_DCMIPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_STM32_DCMIPP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_AUDIO_CODEC_CS35L5X_RESET`、`CONFIG_HAPTICS_CS40L26_RESET`、`CONFIG_HAPTICS_CS40L26_INTERRUPT`、`CONFIG_HAPTICS_CS40L5X_RESET`、`CONFIG_HAPTICS_CS40L5X_INTERRUPT`、`CONFIG_HAPTICS_CS40L5X_TRIGGER`。

<a id="CONFIG_GPIO_AD559X"></a>

## 98.2 `CONFIG_GPIO_AD559X`

**提示（Prompt）**：AD559x GPIO 驱动

**说明（Help）**

启用 AD559x GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_AD559X_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.ad559x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.ad559x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_GPIO_ADP5585"></a>

## 98.3 `CONFIG_GPIO_ADP5585`

**提示（Prompt）**：ADP5585_GPIO I2C GPIO 芯片

**说明（Help）**

启用 ADP5585 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_ADP5585_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
CONFIG_I2C
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_mx8_dsi_oled1a/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_mx8_dsi_oled1a/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/nxp_mx9_dsi_oled/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_mx9_dsi_oled/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.adp5585:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.adp5585#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_GPIO_ADP5585_INIT_PRIORITY"></a>

## 98.4 `CONFIG_GPIO_ADP5585_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_ADP5585 && CONFIG_GPIO
```

**默认值（Defaults）**

```text
70
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.adp5585:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.adp5585#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → ADP5585_GPIO I2C GPIO 芯片

**配置项引用（Symbol References）**：[`CONFIG_GPIO_ADP5585`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_ADP5585)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_ADS1X4S0X"></a>

## 98.5 `CONFIG_GPIO_ADS1X4S0X`

**提示（Prompt）**：ADS1X4S0X GPIO 驱动

**说明（Help）**

为 ADS1X4S0X 启用 GPIO 驱动。ADS1X4S0X 是多通道模拟前端（Analog Frontend，AFE）。该器件的 GPIO 端口，即 GPIO0 至 GPIO3，通过支持读写的 GPIO 控制器驱动（Controller Driver）公开。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_ADS1X4S0X_GPIO_ENABLED && CONFIG_ADC_ADS1X4S0X_GPIO && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.ads1x4s0x:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.ads1x4s0x#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_ADC_ADS1X4S0X_GPIO`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS1X4S0X_GPIO)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_ADS1X4S0X_INIT_PRIORITY"></a>

## 98.6 `CONFIG_GPIO_ADS1X4S0X_INIT_PRIORITY`

**提示（Prompt）**：驱动初始化优先级（Driver Init Priority）

**说明（Help）**

设备驱动的初始化优先级（Initialization Priority）。本驱动必须在 ADS1X4S0X 模数转换器（ADC）驱动之后初始化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_ADS1X4S0X && CONFIG_GPIO
```

**默认值（Defaults）**

```text
99
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.ads1x4s0x:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.ads1x4s0x#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → ADS1X4S0X GPIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO_ADS1X4S0X`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_ADS1X4S0X)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_AESC"></a>

## 98.7 `CONFIG_GPIO_AESC`

**提示（Prompt）**：Aesc Silicon GPIO 驱动

**说明（Help）**

启用 Aesc Silicon GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AESC_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.aesc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.aesc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_ALLWINNER"></a>

## 98.8 `CONFIG_GPIO_ALLWINNER`

**提示（Prompt）**：全志（Allwinner）GPIO 驱动

**说明（Help）**

启用用于 H618 的全志（Allwinner）GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ALLWINNER_SUNXI_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.allwinner:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.allwinner#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_ALTERA_PIO"></a>

## 98.9 `CONFIG_GPIO_ALTERA_PIO`

**提示（Prompt）**：Altera 并行 I/O（PIO）

**说明（Help）**

启用 Altera 并行 I/O（PIO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ALTR_PIO_1_0_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.altera:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.altera#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_AMBIQ"></a>

## 98.10 `CONFIG_GPIO_AMBIQ`

**提示（Prompt）**：Ambiq GPIO 驱动

**说明（Help）**

启用 Ambiq GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMBIQ_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_AMBIQ_HAL
CONFIG_AMBIQ_HAL_USE_GPIO
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.ambiq:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.ambiq#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_AMBIQ_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL)、[`CONFIG_AMBIQ_HAL_USE_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL_USE_GPIO)。

<a id="CONFIG_GPIO_AMEBA"></a>

## 98.11 `CONFIG_GPIO_AMEBA`

**提示（Prompt）**：Realtek Ameba 系列 SoC 的 GPIO 控制器驱动（Controller Driver）

**说明（Help）**

启用瑞昱（Realtek）Ameba 系列 SoC 的 GPIO 控制器驱动（Controller Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_AMEBA_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.ameba:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.ameba#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_ANDES_ATCGPIO100"></a>

## 98.12 `CONFIG_GPIO_ANDES_ATCGPIO100`

**提示（Prompt）**：Andes ATCGPIO100 GPIO 驱动

**说明（Help）**

启用 Andes ATCGPIO100 GPIO 控制器（Controller）的驱动。不确定时选择 `n`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ANDESTECH_ATCGPIO100_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.andes_atcgpio100:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.andes_atcgpio100#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_AW9523B"></a>

## 98.13 `CONFIG_GPIO_AW9523B`

**提示（Prompt）**：AW9523B GPIO 驱动

**说明（Help）**

启用 AW9523B GPIO 控制器（Controller）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AWINIC_AW9523B_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.aw9523b:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.aw9523b#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_GPIO_AXP192"></a>

## 98.14 `CONFIG_GPIO_AXP192`

**提示（Prompt）**：AXP192 GPIO 驱动

**说明（Help）**

启用 AXP192 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_X_POWERS_AXP192_GPIO_ENABLED && DT_HAS_X_POWERS_AXP192_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.axp192:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.axp192#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_GPIO_AXP192_INIT_PRIORITY"></a>

## 98.15 `CONFIG_GPIO_AXP192_INIT_PRIORITY`

**提示（Prompt）**：AXP192 GPIO 驱动初始化优先级（Initialization Priority）

**说明（Help）**

AXP192 GPIO 驱动的初始化优先级（Initialization Priority）。数值必须大于 I2C 控制器和多功能设备（MFD）驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_AXP192 && CONFIG_GPIO
```

**默认值（Defaults）**

```text
81
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.axp192:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.axp192#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → AXP192 GPIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO_AXP192`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_AXP192)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_BCM2711"></a>

## 98.16 `CONFIG_GPIO_BCM2711`

**提示（Prompt）**：BCM2711 GPIO 驱动

**说明（Help）**

启用 BCM2711 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BRCM_BCM2711_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.bcm2711:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.bcm2711#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_BD8LB600FS"></a>

## 98.17 `CONFIG_GPIO_BD8LB600FS`

**提示（Prompt）**：基于 SPI 的 BD8LB600FS GPIO 芯片

**说明（Help）**

启用基于 SPI 的 BD8LB600FS GPIO 芯片的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ROHM_BD8LB600FS_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.bd8lb600fs:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.bd8lb600fs#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_GPIO_BD8LB600FS_INIT_PRIORITY"></a>

## 98.18 `CONFIG_GPIO_BD8LB600FS_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_BD8LB600FS && CONFIG_GPIO
```

**默认值（Defaults）**

```text
75
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.bd8lb600fs:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.bd8lb600fs#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 基于 SPI 的 BD8LB600FS GPIO 芯片

**配置项引用（Symbol References）**：[`CONFIG_GPIO_BD8LB600FS`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_BD8LB600FS)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_BEE"></a>

## 98.19 `CONFIG_GPIO_BEE`

**提示（Prompt）**：Realtek Bee 系列 GPIO 驱动

**说明（Help）**

此选项启用瑞昱（Realtek）Bee SoC 的 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_BEE_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAL_REALTEK_BEE_GPIO
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.bee:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.bee#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_HAL_REALTEK_BEE_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAL_REALTEK_BEE_GPIO)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAL_REALTEK_BEE_GPIO`。

<a id="CONFIG_GPIO_BFLB_BL60X_70X"></a>

## 98.20 `CONFIG_GPIO_BFLB_BL60X_70X`

**提示（Prompt）**：博流（Bouffalo Lab）BL60x 和 BL70x GPIO 驱动

**说明（Help）**

博流（Bouffalo Lab）BL60x 和 BL70x GPIO 驱动

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_BL60X_70X_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.bflb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.bflb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_BFLB_BL61X_808"></a>

## 98.21 `CONFIG_GPIO_BFLB_BL61X_808`

**提示（Prompt）**：博流（Bouffalo Lab）BL61X 和 BL808 GPIO 驱动

**说明（Help）**

博流（Bouffalo Lab）BL61X 和 BL808 GPIO 驱动

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_BL61X_808_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.bflb:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.bflb#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_BFLB_BL61X_808_CACHE_WRITE"></a>

## 98.22 `CONFIG_GPIO_BFLB_BL61X_808_CACHE_WRITE`

**提示（Prompt）**：缓存 BL61x GPIO 写入值（Cache GPIO Writes）

**说明（Help）**

缓存最后写入 GPIO 寄存器的值，从而避免在速度受限的外设上执行一次不必要的读操作，使 GPIO 翻转速度（Toggle Speed）加倍。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_BFLB_BL61X_808 && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.bflb:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.bflb#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 博流（Bouffalo Lab）BL61X 和 BL808 GPIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO_BFLB_BL61X_808`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_BFLB_BL61X_808)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_BL61X_808_WO"></a>

## 98.23 `CONFIG_GPIO_BL61X_808_WO`

**提示（Prompt）**：博流（Bouffalo Lab）BL61x GPIO FIFO

**说明（Help）**

GPIO FIFO / WO 是 GPIO 设备的扩展，可在 16 个引脚上输出任意翻转波形（Toggle Waveform），最高速率达到 XCLK Hz，即 32 MHz 或晶体频率。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL && CONFIG_GPIO_BFLB_BL61X_808 && CONFIG_GPIO
```

**被选择（Selected by）**

```text
CONFIG_WS2812_STRIP_BFLB_WO
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.bflb:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.bflb#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 博流（Bouffalo Lab）BL61X 和 BL808 GPIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_GPIO_BFLB_BL61X_808`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_BFLB_BL61X_808)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_WS2812_STRIP_BFLB_WO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WS2812_STRIP_BFLB_WO)。

<a id="CONFIG_GPIO_BRCMSTB"></a>

## 98.24 `CONFIG_GPIO_BRCMSTB`

**提示（Prompt）**：Broadcom 机顶盒 SoC GPIO 驱动（Set-Top Box SoC GPIO Driver）

**说明（Help）**

启用 Broadcom 机顶盒（Set-Top Box）SoC GPIO 组（Bank）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BRCM_BRCMSTB_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.brcmstb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.brcmstb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_CC13XX_CC26XX"></a>

## 98.25 `CONFIG_GPIO_CC13XX_CC26XX`

**提示（Prompt）**：TI SimpleLink CC13xx / CC26xx GPIO 驱动

**说明（Help）**

启用 TI SimpleLink CC13xx / CC26xx GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_CC13XX_CC26XX_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.cc13xx_cc26xx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.cc13xx_cc26xx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_CC23X0"></a>

## 98.26 `CONFIG_GPIO_CC23X0`

**提示（Prompt）**：TI SimpleLink CC23X0 GPIO 驱动

**说明（Help）**

启用 TI SimpleLink CC23x0 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_CC23X0_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.cc23x0:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.cc23x0#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_CC32XX"></a>

## 98.27 `CONFIG_GPIO_CC32XX`

**提示（Prompt）**：TI CC32XX GPIO 驱动

**说明（Help）**

在 TI SimpleLink CC32xx 开发板上启用 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_CC32XX_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.cc32xx:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.cc32xx#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_CMSDK_AHB"></a>

## 98.28 `CONFIG_GPIO_CMSDK_AHB`

**提示（Prompt）**：ARM Cortex-M 系统设计套件（Cortex-M System Design Kit，CMSDK）AHB GPIO 控制器

**说明（Help）**

启用用于支持 ARM CMSDK GPIO 控制器（Controller）的配置选项。不确定时选择 `n`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ARM_CMSDK_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.cmsdk_ahb:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.cmsdk_ahb#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_CY8C95XX"></a>

## 98.29 `CONFIG_GPIO_CY8C95XX`

**提示（Prompt）**：CY8C95XX I2C GPIO 芯片

**说明（Help）**

启用 CY8C95XX I2C GPIO 芯片的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_CYPRESS_CY8C95XX_GPIO_PORT_ENABLED && CONFIG_I2C && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.cy8c95xx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.cy8c95xx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_CY8C95XX_INIT_PRIORITY"></a>

## 98.30 `CONFIG_GPIO_CY8C95XX_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_CY8C95XX && CONFIG_GPIO
```

**默认值（Defaults）**

```text
CONFIG_I2C_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.cy8c95xx:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.cy8c95xx#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → CY8C95XX I2C GPIO 芯片

**配置项引用（Symbol References）**：[`CONFIG_GPIO_CY8C95XX`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_CY8C95XX)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C_INIT_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_INIT_PRIORITY)。

<a id="CONFIG_GPIO_CYW43"></a>

## 98.31 `CONFIG_GPIO_CYW43`

**提示（Prompt）**：Infineon CYW43 GPIO 驱动

**说明（Help）**

启用英飞凌（Infineon）CYW43 Wi-Fi 芯片的 GPIO 驱动，将 `WL_GPIO0` 至 `WL_GPIO2` 作为标准 Zephyr GPIO 引脚公开。引脚 `0` 对应 Pico W / Pico 2 W 的板载 LED。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_CYW43_GPIO_ENABLED && CONFIG_WIFI_AIROC && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.cyw43:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.cyw43#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_AIROC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_AIROC)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_CYW43_INIT_PRIORITY"></a>

## 98.32 `CONFIG_GPIO_CYW43_INIT_PRIORITY`

**提示（Prompt）**：CYW43 GPIO 初始化优先级（Initialization Priority）

**说明（Help）**

CYW43 GPIO 的初始化优先级（Initialization Priority）。数值必须大于 Wi-Fi 驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_CYW43 && CONFIG_GPIO
```

**默认值（Defaults）**

```text
82
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.cyw43:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.cyw43#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → Infineon CYW43 GPIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO_CYW43`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_CYW43)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_DAVINCI"></a>

## 98.33 `CONFIG_GPIO_DAVINCI`

**提示（Prompt）**：DaVinci GPIO 驱动

**说明（Help）**

启用 DaVinci GPIO 控制器（Controller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_DAVINCI_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.davinci:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.davinci#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_GPIO_DEBOUNCE_EN"></a>

## 98.34 `CONFIG_GPIO_DEBOUNCE_EN`

**提示（Prompt）**：启用 Ameba GPIO 中断消抖（Interrupt Debounce）

**说明（Help）**

启用 GPIO 中断消抖（Interrupt Debounce）后，可对外部信号消抖，去除持续时间短于外部消抖时钟一个周期（约 32 µs）的伪毛刺（Spurious Glitch）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_AMEBA && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.ameba:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.ameba#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → Realtek Ameba 系列 SoC 的 GPIO 控制器驱动（Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_GPIO_AMEBA`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_AMEBA)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_DW"></a>

## 98.35 `CONFIG_GPIO_DW`

**提示（Prompt）**：DesignWare GPIO

**说明（Help）**

启用 DesignWare GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SNPS_DESIGNWARE_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL if n
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.dw:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.dw#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_GPIO_EFINIX_SAPPHIRE"></a>

## 98.36 `CONFIG_GPIO_EFINIX_SAPPHIRE`

**提示（Prompt）**：Efinix Sapphire GPIO 驱动（原提示拼作 Efinx）

**说明（Help）**

启用 Efinix Sapphire GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_EFINIX_SAPPHIRE_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.efinix_sapphire:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.efinix_sapphire#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_EM32"></a>

## 98.37 `CONFIG_GPIO_EM32`

**提示（Prompt）**：ELAN EMC32Fxxx GPIO 驱动

**说明（Help）**

为 ELAN EM32F967 微控制器（Microcontroller）启用 GPIO 驱动。EM32F967 有两个 GPIO 端口（GPIOA 和 GPIOB），每个端口具有 16 个引脚。各端口支持：

- 输入/输出方向控制（Direction Control）。
- 上拉/下拉电阻（Pull-Up/Pull-Down Resistors）。
- 中断生成（Interrupt Generation），支持边沿触发和电平触发（Edge/Level Triggered）。
- 复用功能选择（Alternate Function Selection）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_EM32F967 && DT_HAS_ELAN_EM32_GPIO_ENABLED && CONFIG_CLOCK_CONTROL_EM32_AHB && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SYSCON
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.em32:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.em32#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_EM32F967`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EM32F967)、[`CONFIG_CLOCK_CONTROL_EM32_AHB`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_EM32_AHB)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_SYSCON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYSCON)。

<a id="CONFIG_GPIO_EM32_INIT_PRIORITY"></a>

## 98.38 `CONFIG_GPIO_EM32_INIT_PRIORITY`

**提示（Prompt）**：EM32 GPIO 初始化优先级（Initialization Priority）

**说明（Help）**

EM32 GPIO 驱动的初始化优先级（Initialization Priority）。数值必须大于 `CONFIG_SYSCON_INIT_PRIORITY`，因为 GPIO 驱动依赖系统控制器（Syscon）访问上拉/下拉和开漏（Open-Drain）寄存器。由于 GPIO 需要时钟门控（Clock Gating），此数值还必须大于时钟控制（Clock Control）的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_EM32 && CONFIG_GPIO
```

**默认值（Defaults）**

```text
55
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.em32:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.em32#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → ELAN EMC32Fxxx GPIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO_EM32`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_EM32)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_EMUL"></a>

## 98.39 `CONFIG_GPIO_EMUL`

**提示（Prompt）**：仿真 GPIO 驱动（Emulated GPIO Driver）

**说明（Help）**

启用仿真 GPIO 驱动（Emulated GPIO Driver）。它主要用于测试，允许实例化任意数量的仿真 GPIO 控制器。还可通过常规 GPIO 回调 API（Callback API）及 `drivers/gpio/gpio_emul.h` 中的附加 API，为仿真引脚“接线”（Wire）。每个 GPIO 实例通过设备树（Devicetree）配置，示例位于 `tests/drivers/gpio/gpio_basic_api/boards/native_sim.overlay`。不确定时选择 `N`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_GPIO_EMUL_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.emul:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.emul#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_EMUL_SDL"></a>

## 98.40 `CONFIG_GPIO_EMUL_SDL`

**提示（Prompt）**：SDL GPIO 仿真（Emulation）

**说明（Help）**

启用利用 SDL 键盘事件（Keyboard Events）的 GPIO 仿真（Emulation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_GPIO_EMUL_SDL_ENABLED && CONFIG_GPIO_EMUL && HAS_SDL && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.emul_sdl:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.emul_sdl#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 仿真 GPIO 驱动（Emulated GPIO Driver）

**配置项引用（Symbol References）**：[`CONFIG_GPIO_EMUL`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_EMUL)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_ENABLE_DISABLE_INTERRUPT"></a>

## 98.41 `CONFIG_GPIO_ENABLE_DISABLE_INTERRUPT`

**提示（Prompt）**：支持无需重新配置即可启停中断（Enable/Disable Interrupt without Reconfiguration）【实验性】

**说明（Help）**

此选项支持沿用先前配置来启用或禁用中断（Interrupt）。启停中断时仅打开或关闭中断信号，不改变挂起寄存器（Pending Register）等其他寄存器。具体驱动必须实现此功能，它才能生效。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`drivers/gpio/Kconfig:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_GPIO_ENE_KB106X"></a>

## 98.42 `CONFIG_GPIO_ENE_KB106X`

**提示（Prompt）**：ENE KB106X GPIO 驱动

**说明（Help）**

启用 KB106X GPIO 控制器（Controller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ENE_KB106X_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.ene:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.ene#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_ENE_KB1200"></a>

## 98.43 `CONFIG_GPIO_ENE_KB1200`

**提示（Prompt）**：ENE KB1200 GPIO 驱动

**说明（Help）**

启用 KB1200 GPIO 控制器（Controller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ENE_KB1200_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.ene:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.ene#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_EOS_S3"></a>

## 98.44 `CONFIG_GPIO_EOS_S3`

**提示（Prompt）**：EOS_S3 GPIO 驱动

**说明（Help）**

启用 EOS S3 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_QUICKLOGIC_EOS_S3_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.eos_s3:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.eos_s3#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_ESP32"></a>

## 98.45 `CONFIG_GPIO_ESP32`

**提示（Prompt）**：ESP32 GPIO

**说明（Help）**

启用 ESP32 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_I2C_ESP32
CONFIG_UART_ESP32
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.esp32:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.esp32#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_ESP32)、[`CONFIG_UART_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ESP32)。

<a id="CONFIG_GPIO_FXL6408"></a>

## 98.46 `CONFIG_GPIO_FXL6408`

**提示（Prompt）**：基于 I2C 的 FXL6408 GPIO 芯片

**说明（Help）**

启用基于 I2C 的 FXL6408 GPIO 芯片的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_FCS_FXL6408_ENABLED && CONFIG_I2C && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.fxl6408:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.fxl6408#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_FXL6408_INIT_PRIORITY"></a>

## 98.47 `CONFIG_GPIO_FXL6408_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_FXL6408 && CONFIG_GPIO
```

**默认值（Defaults）**

```text
CONFIG_I2C_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.fxl6408:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.fxl6408#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 基于 I2C 的 FXL6408 GPIO 芯片

**配置项引用（Symbol References）**：[`CONFIG_GPIO_FXL6408`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_FXL6408)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C_INIT_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_INIT_PRIORITY)。

<a id="CONFIG_GPIO_GD32"></a>

## 98.48 `CONFIG_GPIO_GD32`

**提示（Prompt）**：GD32 GPIO 驱动

**说明（Help）**

启用 GD32 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GD_GD32_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GD32_EXTI
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.gd32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.gd32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_GD32_EXTI`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_GD32_EXTI)。

<a id="CONFIG_GPIO_GECKO"></a>

## 98.49 `CONFIG_GPIO_GECKO`

**提示（Prompt）**：Gecko GPIO 驱动

**说明（Help）**

启用 Gecko GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_GECKO_GPIO_PORT_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SILABS_GECKO_GPIO
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.gecko:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.gecko#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_SILABS_GECKO_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_GECKO_GPIO)。

<a id="CONFIG_GPIO_GECKO_COMMON_INIT_PRIORITY"></a>

## 98.50 `CONFIG_GPIO_GECKO_COMMON_INIT_PRIORITY`

**提示（Prompt）**：通用初始化优先级（Common Initialization Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_GECKO && CONFIG_GPIO
```

**默认值（Defaults）**

```text
39
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.gecko:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.gecko#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → Gecko GPIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO_GECKO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_GECKO)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_GET_CONFIG"></a>

## 98.51 `CONFIG_GPIO_GET_CONFIG`

**提示（Prompt）**：支持获取配置函数（Get Configuration Function）【实验性】

**说明（Help）**

此选项支持获取 GPIO 的当前配置（Current Configuration）。具体驱动必须实现此功能，它才能生效。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`drivers/gpio/Kconfig:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_GPIO_GET_DIRECTION"></a>

## 98.52 `CONFIG_GPIO_GET_DIRECTION`

**提示（Prompt）**：支持查询 GPIO 方向（Query GPIO Direction）【实验性】

**说明（Help）**

如果应用程序不维护自身的 GPIO 方向状态（Direction State），则启用此项。启用后，应用程序可通过 `gpio_port_get_direction()`、`gpio_pin_is_input()` 和 `gpio_pin_is_output()` 查询 GPIO 方向。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`drivers/gpio/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_GPIO_GRGPIO2"></a>

## 98.53 `CONFIG_GPIO_GRGPIO2`

**提示（Prompt）**：GRLIB GRGPIO 第 2 修订版（Revision 2）

**说明（Help）**

启用 GRLIB GRGPIO 第 2 修订版（Revision 2）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GAISLER_GRGPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.grgpio:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.grgpio#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_HOGS"></a>

## 98.54 `CONFIG_GPIO_HOGS`

**提示（Prompt）**：GPIO 预占（GPIO Hogs）支持

**说明（Help）**

启用 GPIO 预占（GPIO Hogs）支持。GPIO 预占（GPIO Hogging）是一种通过设备树（Devicetree）自动配置 GPIO 的机制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/gpio/Kconfig:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_HOGS_INIT_PRIORITY"></a>

## 98.55 `CONFIG_GPIO_HOGS_INIT_PRIORITY`

**提示（Prompt）**：GPIO 预占初始化优先级（GPIO Hogs Init Priority）

**说明（Help）**

GPIO 预占（GPIO Hogs）的初始化优先级（Initialization Priority）。预占配置必须在 GPIO 控制器驱动之后初始化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_HOGS && CONFIG_GPIO
```

**默认值（Defaults）**

```text
41
```

**定义位置（Location）**：[`drivers/gpio/Kconfig:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → GPIO 预占（GPIO Hogs）支持

**配置项引用（Symbol References）**：[`CONFIG_GPIO_HOGS`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_HOGS)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_IMX"></a>

## 98.56 `CONFIG_GPIO_IMX`

**提示（Prompt）**：i.MX GPIO 驱动

**说明（Help）**

启用 i.MX GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_GPIO_ENABLED && (CONFIG_SOC_SERIES_IMX6SX || CONFIG_SOC_SERIES_IMX7D) && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.imx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.imx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMX6SX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMX6SX)、[`CONFIG_SOC_SERIES_IMX7D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMX7D)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMX6SX`。

<a id="CONFIG_GPIO_INFINEON"></a>

## 98.57 `CONFIG_GPIO_INFINEON`

**提示（Prompt）**：Infineon GPIO 驱动

**说明（Help）**

为使用 `infineon,gpio` 兼容标识（Compatible）的英飞凌（Infineon）微控制器（MCU）启用 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.infineon:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.infineon#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_INIT_PRIORITY"></a>

## 98.58 `CONFIG_GPIO_INIT_PRIORITY`

**提示（Prompt）**：GPIO 初始化优先级（Init Priority）

**说明（Help）**

GPIO 驱动设备的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEFAULT
```

**定义位置（Location）**：[`drivers/gpio/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_KERNEL_INIT_PRIORITY_DEFAULT`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEFAULT)。

<a id="CONFIG_GPIO_INTEL"></a>

## 98.59 `CONFIG_GPIO_INTEL`

**提示（Prompt）**：Intel SoC GPIO

**说明（Help）**

启用 Intel SoC GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.intel:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.intel#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_INTEL_CHECK_PERMS"></a>

## 98.60 `CONFIG_GPIO_INTEL_CHECK_PERMS`

**提示（Prompt）**：操作 GPIO 之前检查权限（Check Permissions）

**说明（Help）**

此选项启用检查，确保 GPIO 引脚允许被操作。只有当引脚归主机软件所有，并且其功能为 GPIO 时，驱动才允许操作该引脚。不确定时选择 `y`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_INTEL && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.intel:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.intel#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → Intel SoC GPIO

**配置项引用（Symbol References）**：[`CONFIG_GPIO_INTEL`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_INTEL)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_IPROC"></a>

## 98.61 `CONFIG_GPIO_IPROC`

**提示（Prompt）**：Broadcom iProc GPIO 控制器驱动（Controller Driver）

**说明（Help）**

此选项启用 iProc 系列 GPIO 控制器（Controller）的 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BRCM_IPROC_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.iproc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.iproc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_ITE_IT51XXX"></a>

## 98.62 `CONFIG_GPIO_ITE_IT51XXX`

**提示（Prompt）**：ITE IT51XXX GPIO 驱动

**说明（Help）**

启用 IT51XXX 系列 GPIO 控制器（Controller）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT51XXX_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.it51xxx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.it51xxx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_ITE_IT8801"></a>

## 98.63 `CONFIG_GPIO_ITE_IT8801`

**提示（Prompt）**：ITE IT8801 GPIO 设备驱动（Device Driver）

**说明（Help）**

启用 ITE IT8801 基于 I2C 的 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT8801_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.it8801:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.it8801#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_GPIO_ITE_IT8XXX2"></a>

## 98.64 `CONFIG_GPIO_ITE_IT8XXX2`

**提示（Prompt）**：ITE IT8XXX2 GPIO 驱动

**说明（Help）**

启用 ITE GPIO 控制器（Controller）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT8XXX2_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.it8xxx2:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.it8xxx2#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_ITE_IT8XXX2_V2"></a>

## 98.65 `CONFIG_GPIO_ITE_IT8XXX2_V2`

**提示（Prompt）**：ITE IT8XXX2 GPIO V2 驱动

**说明（Help）**

启用 ITE GPIO V2 控制器（Controller）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT8XXX2_GPIO_V2_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.it8xxx2:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.it8xxx2#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_KSCAN_ITE_IT8XXX2"></a>

## 98.66 `CONFIG_GPIO_KSCAN_ITE_IT8XXX2`

**提示（Prompt）**：ITE IT8XXX2 GPIO 键盘扫描驱动（KSCAN Driver）

**说明（Help）**

为 ITE IT8XXX2 芯片启用 GPIO 键盘扫描（KSCAN）驱动。IT8XXX2 支持 8 个键盘扫描输入（KSI）引脚和 18 个键盘扫描输出（KSO）引脚，它们都可配置为 GPIO 模式。`KSI[7:0]` 和 `KSO[15:0]` 由本 `GPIO_KSCAN_ITE_IT8XXX2` 驱动配置为 GPIO 模式。`KSO[17:16]` 对应 GPC5 和 GPC3 引脚，可由原有 `GPIO_ITE_IT8XXX2` 驱动配置为 GPIO 模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT8XXX2_GPIOKSCAN_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.it8xxx2:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.it8xxx2#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_LITEX"></a>

## 98.67 `CONFIG_GPIO_LITEX`

**提示（Prompt）**：LiteX GPIO 驱动

**说明（Help）**

启用 LiteX GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LITEX_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.litex:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.litex#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_LMP90XXX"></a>

## 98.68 `CONFIG_GPIO_LMP90XXX`

**提示（Prompt）**：LMP90xxx GPIO 驱动

**说明（Help）**

为 LMP90xxx 启用 GPIO 驱动。LMP90xxx 是多通道、低功耗传感器模拟前端（Analog Frontend，AFE）。其 GPIO 端口，即 D6 至 D0，通过支持读写的 GPIO 控制器驱动（Controller Driver）公开。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_LMP90XXX_GPIO_ENABLED && CONFIG_ADC_LMP90XXX_GPIO && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_ADC_LMP90XXX_GPIO
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.lmp90xxx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.lmp90xxx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_ADC_LMP90XXX_GPIO`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_LMP90XXX_GPIO)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_LMP90XXX_INIT_PRIORITY"></a>

## 98.69 `CONFIG_GPIO_LMP90XXX_INIT_PRIORITY`

**提示（Prompt）**：驱动初始化优先级（Driver Init Priority）

**说明（Help）**

设备驱动的初始化优先级（Initialization Priority）。本驱动必须在 LMP90xxx 模数转换器（ADC）驱动之后初始化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_LMP90XXX && CONFIG_GPIO
```

**默认值（Defaults）**

```text
99
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.lmp90xxx:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.lmp90xxx#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → LMP90xxx GPIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO_LMP90XXX`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_LMP90XXX)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_LPC11U6X"></a>

## 98.70 `CONFIG_GPIO_LPC11U6X`

**提示（Prompt）**：LPC11U6x GPIO 驱动

**说明（Help）**

为 LPC11U6x 微控制器（MCU）启用 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPC11U6X_GPIO_ENABLED && CONFIG_CLOCK_CONTROL_LPC11U6X && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.lpc11u6x:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.lpc11u6x#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_LPC11U6X`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_LPC11U6X)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_M5PM1"></a>

## 98.71 `CONFIG_GPIO_M5PM1`

**提示（Prompt）**：M5Stack M5PM1 GPIO 驱动

**说明（Help）**

启用 M5Stack M5PM1 的 GPIO 控制器驱动（Controller Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_M5STACK_M5PM1_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.m5pm1:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.m5pm1#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_GPIO_M5PM1_INIT_PRIORITY"></a>

## 98.72 `CONFIG_GPIO_M5PM1_INIT_PRIORITY`

**提示（Prompt）**：M5PM1 GPIO 驱动初始化优先级（Initialization Priority）

**说明（Help）**

M5PM1 GPIO 驱动的初始化优先级（Initialization Priority）。数值必须大于多功能设备（MFD）的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_M5PM1 && CONFIG_GPIO
```

**默认值（Defaults）**

```text
82
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.m5pm1:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.m5pm1#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → M5Stack M5PM1 GPIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO_M5PM1`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_M5PM1)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_MAX14906"></a>

## 98.73 `CONFIG_GPIO_MAX14906`

**提示（Prompt）**：MAX14906 GPIO 驱动

**说明（Help）**

启用具有诊断功能（Diagnostics）的 MAX14906 四通道工业数字输入/输出（Quad Industrial Digital Input/Output）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX14906_GPIO_ENABLED && CONFIG_SPI && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.max14906:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.max14906#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_MAX14906_INIT_PRIORITY"></a>

## 98.74 `CONFIG_GPIO_MAX14906_INIT_PRIORITY`

**提示（Prompt）**：驱动初始化优先级（Driver Init Priority）

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_MAX14906 && CONFIG_GPIO
```

**默认值（Defaults）**

```text
99
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.max14906:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.max14906#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → MAX14906 GPIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO_MAX14906`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_MAX14906)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_MAX14916"></a>

## 98.75 `CONFIG_GPIO_MAX14916`

**提示（Prompt）**：MAX14916 GPIO 驱动

**说明（Help）**

启用具有诊断功能（Diagnostics）的八通道工业数字输出（Octal Industrial Digital Output）。原帮助正文将器件型号写为 `MAX1416`，而提示文本为 `MAX14916`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ADI_MAX14916_GPIO_ENABLED || DT_HAS_ADI_MAX14915_GPIO_ENABLED) && CONFIG_SPI && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.max14916:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.max14916#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_MAX14916_INIT_PRIORITY"></a>

## 98.76 `CONFIG_GPIO_MAX14916_INIT_PRIORITY`

**提示（Prompt）**：驱动初始化优先级（Driver Init Priority）

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_MAX14916 && CONFIG_GPIO
```

**默认值（Defaults）**

```text
99
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.max14916:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.max14916#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → MAX14916 GPIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO_MAX14916`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_MAX14916)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_MAX14917"></a>

## 98.77 `CONFIG_GPIO_MAX14917`

**提示（Prompt）**：MAX14917 GPIO 驱动

**说明（Help）**

启用具有诊断功能（Diagnostics）的 MAX14917 八通道工业数字输出（Octal Industrial Digital Output）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX14917_GPIO_ENABLED && CONFIG_SPI && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CRC
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.max14917:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.max14917#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

<a id="CONFIG_GPIO_MAX14917_INIT_PRIORITY"></a>

## 98.78 `CONFIG_GPIO_MAX14917_INIT_PRIORITY`

**提示（Prompt）**：驱动初始化优先级（Driver Init Priority）

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_MAX14917 && CONFIG_GPIO
```

**默认值（Defaults）**

```text
99
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.max14917:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.max14917#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → MAX14917 GPIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO_MAX14917`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_MAX14917)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_MAX22017"></a>

## 98.79 `CONFIG_GPIO_MAX22017`

**提示（Prompt）**：Analog Devices MAX22017 GPIO 支持

**说明（Help）**

启用 Analog Devices MAX22017 的 GPIO 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX22017_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.max22017:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.max22017#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_GPIO_MAX22017_INIT_PRIORITY"></a>

## 98.80 `CONFIG_GPIO_MAX22017_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

Analog Devices MAX22017 GPIO 设备驱动的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_MAX22017 && CONFIG_GPIO
```

**默认值（Defaults）**

```text
81
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.max22017:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.max22017#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → Analog Devices MAX22017 GPIO 支持

**配置项引用（Symbol References）**：[`CONFIG_GPIO_MAX22017`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_MAX22017)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_MAX22017_INT_QUIRK"></a>

## 98.81 `CONFIG_GPIO_MAX22017_INT_QUIRK`

**提示（Prompt）**：MAX22017 GPIO 中断特殊行为处理（Interrupt Quirk）

**说明（Help）**

只要中断状态寄存器（Interrupt Status Register）尚未被读取，GPIO 控制器就不会报告新的通用输入（GPI）中断。读取中断状态寄存器的动作发生在 `INT` 引脚下降沿（Falling Edge）。似乎存在这样一种情况：GPIO 控制器已检测到中断，但其 `INT` 引脚仍保持高电平，导致后续全部中断被屏蔽。为避免一直停留在这种状态，启动定时器，定期检查中断状态寄存器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_MAX22017 && CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.max22017:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.max22017#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → Analog Devices MAX22017 GPIO 支持

**配置项引用（Symbol References）**：[`CONFIG_GPIO_MAX22017`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_MAX22017)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_MAX22190_INIT_PRIORITY"></a>

## 98.82 `CONFIG_GPIO_MAX22190_INIT_PRIORITY`

**提示（Prompt）**：驱动初始化优先级（Driver Init Priority）

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_MAX2219X && CONFIG_GPIO
```

**默认值（Defaults）**

```text
99
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.max2219x:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.max2219x#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → MAX2219X GPIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO_MAX2219X`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_MAX2219X)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_MAX2219X"></a>

## 98.83 `CONFIG_GPIO_MAX2219X`

**提示（Prompt）**：MAX2219X GPIO 驱动

**说明（Help）**

启用具有诊断功能（Diagnostics）的 MAX2219X 八通道工业数字输入（Octal Industrial Digital Input）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI && (DT_HAS_ADI_MAX22190_GPIO_ENABLED || DT_HAS_ADI_MAX22199_GPIO_ENABLED) && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.max2219x:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.max2219x#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_MAX32"></a>

## 98.84 `CONFIG_GPIO_MAX32`

**提示（Prompt）**：MAX32 微控制器（MCU）系列 GPIO 驱动

**说明（Help）**

为 MAX32 微控制器（MCU）系列启用 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX32_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.max32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.max32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_MCHP_MSS"></a>

## 98.85 `CONFIG_GPIO_MCHP_MSS`

**提示（Prompt）**：Microchip PolarFire SoC GPIO 驱动

**说明（Help）**

启用 PolarFire SoC Icicle Kit GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_MPFS_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.mchp_mss:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.mchp_mss#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_MCHP_PORT_G1"></a>

## 98.86 `CONFIG_GPIO_MCHP_PORT_G1`

**提示（Prompt）**：Microchip PORT G1 GPIO 驱动

**说明（Help）**

此选项启用 PORT 外设 G1 组（Group）的 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_PORT_G1_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.mchp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.mchp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_MCP230XX"></a>

## 98.87 `CONFIG_GPIO_MCP230XX`

**提示（Prompt）**：基于 I2C 的 MCP230XX GPIO 芯片

**说明（Help）**

启用基于 I2C 的 MCP230XX GPIO 芯片的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_MICROCHIP_MCP23008_ENABLED || DT_HAS_MICROCHIP_MCP23009_ENABLED || DT_HAS_MICROCHIP_MCP23016_ENABLED || DT_HAS_MICROCHIP_MCP23017_ENABLED || DT_HAS_MICROCHIP_MCP23018_ENABLED) && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_GPIO_MCP23XXX
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.mcp23xxx:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.mcp23xxx#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)、[`CONFIG_GPIO_MCP23XXX`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_MCP23XXX)。

<a id="CONFIG_GPIO_MCP230XX_INIT_PRIORITY"></a>

## 98.88 `CONFIG_GPIO_MCP230XX_INIT_PRIORITY`

**提示（Prompt）**：MCP230XX GPIO 扩展器初始化优先级（GPIO Expander Init Priority）

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_MCP230XX && CONFIG_GPIO
```

**默认值（Defaults）**

```text
CONFIG_I2C_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.mcp23xxx:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.mcp23xxx#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 基于 I2C 的 MCP230XX GPIO 芯片

**配置项引用（Symbol References）**：[`CONFIG_GPIO_MCP230XX`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_MCP230XX)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C_INIT_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_INIT_PRIORITY)。

<a id="CONFIG_GPIO_MCP23SXX"></a>

## 98.89 `CONFIG_GPIO_MCP23SXX`

**提示（Prompt）**：基于 SPI 的 MCP23SXX GPIO 芯片

**说明（Help）**

启用基于 SPI 的 MCP23SXX GPIO 芯片的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_MICROCHIP_MCP23S08_ENABLED || DT_HAS_MICROCHIP_MCP23S09_ENABLED || DT_HAS_MICROCHIP_MCP23S17_ENABLED || DT_HAS_MICROCHIP_MCP23S18_ENABLED) && CONFIG_SPI && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO_MCP23XXX
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.mcp23xxx:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.mcp23xxx#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_GPIO_MCP23XXX`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_MCP23XXX)。

<a id="CONFIG_GPIO_MCP23SXX_INIT_PRIORITY"></a>

## 98.90 `CONFIG_GPIO_MCP23SXX_INIT_PRIORITY`

**提示（Prompt）**：MCP23SXX GPIO 扩展器初始化优先级（GPIO Expander Init Priority）

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_MCP23SXX && CONFIG_GPIO
```

**默认值（Defaults）**

```text
75
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.mcp23xxx:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.mcp23xxx#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 基于 SPI 的 MCP23SXX GPIO 芯片

**配置项引用（Symbol References）**：[`CONFIG_GPIO_MCP23SXX`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_MCP23SXX)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_MCP23XXX"></a>

## 98.91 `CONFIG_GPIO_MCP23XXX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip 23xxx I2C/SPI I/O 扩展器（I/O Expander）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO
```

**被选择（Selected by）**

```text
CONFIG_GPIO_MCP230XX
CONFIG_GPIO_MCP23SXX
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.mcp23xxx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.mcp23xxx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_GPIO_MCP230XX`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_MCP230XX)、[`CONFIG_GPIO_MCP23SXX`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_MCP23SXX)。

<a id="CONFIG_GPIO_MCUX"></a>

## 98.92 `CONFIG_GPIO_MCUX`

**提示（Prompt）**：MCUX GPIO 驱动

**说明（Help）**

启用 MCUX 引脚复用驱动（Pinmux Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_KINETIS_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.mcux:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.mcux#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_MCUX_GPIO"></a>

## 98.93 `CONFIG_GPIO_MCUX_GPIO`

**提示（Prompt）**：NXP i.MX GPIO 驱动

**说明（Help）**

为使用 `nxp,imx-gpio-v2` 兼容标识（Compatible）的 SoC 启用 NXP i.MX GPIO 驱动。此驱动处理基于 IOMUXC 的引脚复用（Pin Mux）及可选的 LPCG 时钟门控（Clock Gating）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_GPIO_V2_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.mcux_gpio:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.mcux_gpio#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_GPIO_MCUX_IGPIO"></a>

## 98.94 `CONFIG_GPIO_MCUX_IGPIO`

**提示（Prompt）**：MCUX IGPIO 驱动

**说明（Help）**

启用 MCUX IGPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_GPIO_ENABLED && CONFIG_HAS_MCUX && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.mcux_igpio:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.mcux_igpio#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`。

<a id="CONFIG_GPIO_MCUX_LPC"></a>

## 98.95 `CONFIG_GPIO_MCUX_LPC`

**提示（Prompt）**：MCUX LPC GPIO 驱动

**说明（Help）**

启用 MCUX LPC 引脚复用驱动（Pinmux Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPC_GPIO_PORT_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.mcux_lpc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.mcux_lpc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_GPIO_MCUX_RGPIO"></a>

## 98.96 `CONFIG_GPIO_MCUX_RGPIO`

**提示（Prompt）**：MCUX RGPIO 驱动

**说明（Help）**

启用 MCUX RGPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_RGPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.mcux_rgpio:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.mcux_rgpio#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_GPIO_MFXSTM32L152"></a>

## 98.97 `CONFIG_GPIO_MFXSTM32L152`

**提示（Prompt）**：基于 I2C 的 MFXSTM32L152 GPIO 芯片

**说明（Help）**

启用基于 I2C 的 MFXSTM32L152 GPIO 芯片的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_MFXSTM32L152_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.mfxstm32l152:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.mfxstm32l152#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_GPIO_MFXSTM32L152_INIT_PRIORITY"></a>

## 98.98 `CONFIG_GPIO_MFXSTM32L152_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_MFXSTM32L152 && CONFIG_GPIO
```

**默认值（Defaults）**

```text
CONFIG_I2C_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.mfxstm32l152:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.mfxstm32l152#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 基于 I2C 的 MFXSTM32L152 GPIO 芯片

**配置项引用（Symbol References）**：[`CONFIG_GPIO_MFXSTM32L152`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_MFXSTM32L152)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C_INIT_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_INIT_PRIORITY)。

<a id="CONFIG_GPIO_MMIO32"></a>

## 98.99 `CONFIG_GPIO_MMIO32`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此驱动通过与 GPIO 驱动相同的 API，访问一个简单、用途固定的 32 位内存映射 I/O 寄存器（Memory-Mapped I/O Register）。当 SoC 或开发板具有不属于 GPIO IP 模块的寄存器，但又用它们控制 Zephyr 通常要求用 GPIO 引脚指定的功能时，此驱动很有用，例如驱动 LED 或 SPI 设备的片选线（Chip-Select Line）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_MPS2
CONFIG_SOC_SERIES_MPS3
CONFIG_SOC_SERIES_MPS4
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.mmio32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.mmio32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_SOC_SERIES_MPS2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MPS2)、[`CONFIG_SOC_SERIES_MPS3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MPS3)、[`CONFIG_SOC_SERIES_MPS4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MPS4)。

<a id="CONFIG_GPIO_MMIO_LATCH"></a>

## 98.100 `CONFIG_GPIO_MMIO_LATCH`

**提示（Prompt）**：内存映射锁存器 GPIO 驱动（Memory-Mapped Latch GPIO Driver）

**说明（Help）**

启用一种通用 GPIO 控制器（Generic GPIO Controller），其实现形式为内存映射输出锁存寄存器（Memory-Mapped Output Latch Register）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GPIO_MMIO_LATCH_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.mmio_latch:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.mmio_latch#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<!-- kconfig-navigation -->

[上一章](P097_drivers_gnss_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P099_drivers_gpio_配置项参考_2.md)
