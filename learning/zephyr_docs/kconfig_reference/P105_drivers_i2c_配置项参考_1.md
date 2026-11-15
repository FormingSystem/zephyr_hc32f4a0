---
id: learning.zephyr-docs.kconfig-reference.page-105
title: "`drivers/i2c`配置项参考（1/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第105章\_`drivers/i2c`配置项参考（1/2）

本章翻译官方 Kconfig 数据库中 `drivers/i2c` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_GPIO_I2C_SWITCH"></a>

## 105.1 `CONFIG_GPIO_I2C_SWITCH`

**提示（Prompt）**：GPIO 控制的 I²C 总线开关（Bus Switch）

**说明（Help）**

启用 GPIO 控制的 I²C 总线开关驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GPIO_I2C_SWITCH_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2c/Kconfig:306`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig#L306)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C"></a>

## 105.2 `CONFIG_I2C`

**提示（Prompt）**：集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**说明（Help）**

启用 I²C 驱动配置（Driver Configuration）

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SHIELD_ADI_LSMSPG
CONFIG_ADC_ADCXX1C
CONFIG_ADC_ADS1112
CONFIG_ADC_ADS1119
CONFIG_ADC_ADS1X1X
CONFIG_ADC_ADS7828
CONFIG_ADC_LTC2451
CONFIG_ADC_MCP3221
CONFIG_ADC_TLA202X
CONFIG_AUDIO_CODEC_AW88298
CONFIG_AUDIO_CODEC_CS35LXX_I2C
CONFIG_AUDIO_CODEC_CS43L22
CONFIG_AUDIO_CODEC_DA7212
CONFIG_AUDIO_CODEC_MAX98091
CONFIG_AUDIO_CODEC_PCM1681
CONFIG_AUDIO_TAS2563
CONFIG_AUDIO_TAS6422DAC
CONFIG_AUDIO_TLV320AIC3110
CONFIG_AUDIO_TLV320DAC
CONFIG_AUDIO_CODEC_WM8904
CONFIG_AUDIO_CODEC_WM8960
CONFIG_AUDIO_CODEC_WM8962
CONFIG_AUXDISPLAY_JHD1313
CONFIG_AUXDISPLAY_SERLCD
CONFIG_BBRAM_MICROCHIP_MCP7940N
CONFIG_CHARGER_AXP2101
CONFIG_CHARGER_BQ24190
CONFIG_CHARGER_BQ2429X
CONFIG_CHARGER_BQ2518X
CONFIG_CHARGER_BQ25713
CONFIG_CHARGER_MAX20335
CONFIG_CHARGER_NPM10XX
CONFIG_CHARGER_PCA9422
CONFIG_CHARGER_PF1550
CONFIG_SBS_CHARGER
CONFIG_CHARGER_SY6974B
CONFIG_CLOCK_CONTROL_TI_CDCE9XX
CONFIG_COUNTER_MICROCHIP_MCP7940N
CONFIG_DAC_AD569X
CONFIG_DAC_DACX0501
CONFIG_DAC_DACX3608
CONFIG_DAC_MCP4725
CONFIG_DAC_MCP4728
CONFIG_ADV7535
CONFIG_IST3931
CONFIG_SSD1327_5
CONFIG_WAVESHARE_DSI2DPI
CONFIG_EEPROM_AT24
CONFIG_EEPROM_MB85RCXX
CONFIG_SLG471X5_FPGA
CONFIG_FUEL_GAUGE_AXP2101
CONFIG_BQ27Z746
CONFIG_BQ40Z50
CONFIG_HY4245
CONFIG_LC709203F
CONFIG_FUEL_GAUGE_LTC2959
CONFIG_MAX17048
CONFIG_SBS_GAUGE_NEW_API
CONFIG_SY24561
CONFIG_GPIO_ADP5585
CONFIG_GPIO_AW9523B
CONFIG_GPIO_AXP192
CONFIG_GPIO_ITE_IT8801
CONFIG_GPIO_MCP230XX
CONFIG_GPIO_MFXSTM32L152
CONFIG_GPIO_NCT38XX
CONFIG_GPIO_NPM10XX
CONFIG_GPIO_NPM13XX
CONFIG_GPIO_NPM2100
CONFIG_GPIO_NPM6001
CONFIG_GPIO_PCA953X
CONFIG_GPIO_PCA_SERIES
CONFIG_GPIO_PCAL64XXA
CONFIG_GPIO_PCF857X
CONFIG_GPIO_PI4IOE5V6408
CONFIG_GPIO_SX1509B
CONFIG_HAPTICS_CS40LXX_I2C
CONFIG_HAPTICS_DRV2605
CONFIG_HAPTICS_TM6605
CONFIG_INPUT_ADAFRUIT_SEESAW_GAMEPAD
CONFIG_INPUT_CAP12XX
CONFIG_INPUT_CF1133
CONFIG_INPUT_CHSC5X
CONFIG_INPUT_CHSC6X
CONFIG_INPUT_CST8XX
CONFIG_INPUT_CY8CMBR3XXX
CONFIG_INPUT_FT5336
CONFIG_INPUT_FT6146
CONFIG_INPUT_GT911
CONFIG_INPUT_ILI2132A
CONFIG_INPUT_ITE_IT8801_KBD
CONFIG_INPUT_MODULINO_BUTTONS
CONFIG_INPUT_NUNCHUK
CONFIG_INPUT_PAT912X
CONFIG_INPUT_STMPE811
CONFIG_INPUT_TMA525B
CONFIG_INPUT_TSM12
CONFIG_LED_AW9523B
CONFIG_LED_AXP192_AXP2101
CONFIG_HT16K33
CONFIG_IS31FL319X
CONFIG_IS31FL3216A
CONFIG_IS31FL3733
CONFIG_LP3943
CONFIG_LP50XX
CONFIG_LP5562
CONFIG_LP5569
CONFIG_LP586X
CONFIG_MODULINO_BUTTONS_LEDS
CONFIG_NCP5623
CONFIG_LED_NPM10XX
CONFIG_LED_NPM13XX
CONFIG_PCA953X
CONFIG_PCA9633
CONFIG_TLC59108
CONFIG_MODULINO_PIXELS
CONFIG_MFD_ADP5360
CONFIG_MFD_AW9523B
CONFIG_MFD_AXP192
CONFIG_MFD_AXP2101
CONFIG_MFD_DS3231
CONFIG_MFD_ITE_IT8801
CONFIG_MFD_M5PM1
CONFIG_MFD_MAX20335
CONFIG_MFD_MAX31790
CONFIG_MFD_NCT38XX
CONFIG_MFD_NPM10XX
CONFIG_MFD_NPM13XX
CONFIG_MFD_NPM2100
CONFIG_MFD_NPM6001
CONFIG_MFD_PCA9422
CONFIG_MFD_PF1550
CONFIG_MFD_RV3028
CONFIG_MFD_RV3032
CONFIG_MFD_SC18IS606
CONFIG_MFD_TLA2528
CONFIG_TI_TDP2004
CONFIG_OTP_NPM10XX
CONFIG_PWM_ITE_IT8801
CONFIG_PWM_PCA9685
CONFIG_REGULATOR_AXP192_AXP2101
CONFIG_REGULATOR_MAX20335
CONFIG_REGULATOR_MAX20362
CONFIG_REGULATOR_MODULINO_LATCH_RELAY
CONFIG_REGULATOR_MPM54304
CONFIG_REGULATOR_NPM10XX
CONFIG_REGULATOR_NPM13XX
CONFIG_REGULATOR_NPM2100
CONFIG_REGULATOR_NPM6001
CONFIG_REGULATOR_PCA9420
CONFIG_REGULATOR_PCA9422
CONFIG_REGULATOR_PF1550
CONFIG_REGULATOR_TI_TPS6287X
CONFIG_REGULATOR_TPS55287
CONFIG_RTC_AM1805
CONFIG_RTC_BQ32002
CONFIG_RTC_DS1307
CONFIG_RTC_DS1337
CONFIG_RTC_DS3231
CONFIG_RTC_MAX31331
CONFIG_RTC_PCF85063A
CONFIG_RTC_PCF8523
CONFIG_RTC_PCF8563
CONFIG_RTC_RV8263
CONFIG_RTC_RV8803
CONFIG_RTC_RX8130CE
CONFIG_ADLTC2990
CONFIG_ADT7420
CONFIG_ADXL313
CONFIG_ADXL367
CONFIG_LTC4286
CONFIG_MAX30210
CONFIG_SENSOR_MAX32664C
CONFIG_ALS31300
CONFIG_AMS_AS5600
CONFIG_AMS_IAQ_CORE
CONFIG_CCS811
CONFIG_ENS210
CONFIG_TCS3400
CONFIG_TCS34725
CONFIG_TMD2620
CONFIG_TSL2540
CONFIG_TSL2561
CONFIG_TSL2591
CONFIG_AGS10
CONFIG_DHT20
CONFIG_AK8975
CONFIG_AKM09918C
CONFIG_BMA280
CONFIG_BMA4XX
CONFIG_BMC150_MAGN
CONFIG_BMG160
CONFIG_BMI08X
CONFIG_BMM150
CONFIG_BMP180
CONFIG_BMP388
CONFIG_XGZP68XXD
CONFIG_HMC5883L
CONFIG_MPR
CONFIG_DPS310
CONFIG_JC42
CONFIG_LTR55X
CONFIG_LTR_F216A
CONFIG_SENSOR_DS3231
CONFIG_MAX17055
CONFIG_MAX17262
CONFIG_MAX31875
CONFIG_MAX44009
CONFIG_HTU31D
CONFIG_MS5637
CONFIG_MS5837
CONFIG_MLX90394
CONFIG_MCP9600
CONFIG_PAC194X
CONFIG_TCN75A
CONFIG_NPM10XX_ADC
CONFIG_NPM13XX_CHARGER
CONFIG_NPM2100_VBAT
CONFIG_2SMPB_02E
CONFIG_PAJ7620
CONFIG_PMSA003I
CONFIG_QMI8658A
CONFIG_HS300X
CONFIG_ISL29035
CONFIG_BH1730
CONFIG_BH1750
CONFIG_BH1790
CONFIG_HM330X
CONFIG_SCD4X
CONFIG_SGP40
CONFIG_SHT3XD
CONFIG_SHT4X
CONFIG_SHTCX
CONFIG_STCC4
CONFIG_STS4X
CONFIG_SI7006
CONFIG_SI7055
CONFIG_SI7060
CONFIG_SI7210
CONFIG_LIS2DUX12
CONFIG_LIS3MDL
CONFIG_LPS22HB
CONFIG_LPS25HB
CONFIG_LPS2XDF
CONFIG_LSM303DLHC_MAGN
CONFIG_LSM6DS0
CONFIG_LSM6DSO
CONFIG_LSM6DSV16X
CONFIG_LSM6DSVXXX
CONFIG_LSM9DS0_GYRO
CONFIG_LSM9DS0_MFD
CONFIG_LSM9DS1
CONFIG_LSM9DS1_MAG
CONFIG_STTS22H
CONFIG_STTS751
CONFIG_VL53L0X
CONFIG_VL53L1X
CONFIG_VL53L5CX
CONFIG_ICM40627
CONFIG_ICM42X70
CONFIG_ICM45686
CONFIG_ICM566XX
CONFIG_ICP101XX
CONFIG_MPU6050
CONFIG_MPU9250
CONFIG_BQ274XX
CONFIG_FDC1004
CONFIG_FDC2X1X
CONFIG_INA219
CONFIG_INA2XX
CONFIG_INA3221
CONFIG_INA7XX
CONFIG_LM95234
CONFIG_OPT300X
CONFIG_TI_HDC
CONFIG_TI_HDC20XX
CONFIG_TI_HDC302X
CONFIG_TMAG5273
CONFIG_TMP007
CONFIG_TMP1075
CONFIG_TMP108
CONFIG_TMP112
CONFIG_TMP114
CONFIG_TMP11X
CONFIG_TMP435
CONFIG_TMP451
CONFIG_VCNL36825T
CONFIG_VCNL4040
CONFIG_VEML6031
CONFIG_VEML6046
CONFIG_VEML7700
CONFIG_WSEN_HIDS_2525020210002
CONFIG_WSEN_PDUS_25131308XXXXX
CONFIG_WSEN_TIDS_2521020222501
CONFIG_AMD_SB_TSI
CONFIG_AMG88XX
CONFIG_APDS9253
CONFIG_APDS9306
CONFIG_APDS9960
CONFIG_CHT8315
CONFIG_F75303
CONFIG_HP206C
CONFIG_IST8310
CONFIG_LM75
CONFIG_LM77
CONFIG_MB7040
CONFIG_NCT75
CONFIG_S11059
CONFIG_SBS_GAUGE
CONFIG_SX9500
CONFIG_TH02
CONFIG_XBR818
CONFIG_USBC_TCPC_TCPCI
CONFIG_VIDEO_GC2145
CONFIG_VIDEO_HM01B0
CONFIG_VIDEO_HM0360
CONFIG_VIDEO_IMX219
CONFIG_VIDEO_IMX335
CONFIG_VIDEO_MT9M114
CONFIG_VIDEO_OV2640
CONFIG_VIDEO_OV5640
CONFIG_VIDEO_OV5642
CONFIG_VIDEO_OV767X
CONFIG_VIDEO_OV7725
CONFIG_VIDEO_OV9655
CONFIG_VIDEO_ST_MIPID02
CONFIG_W1_DS2482_800
CONFIG_W1_DS2484
CONFIG_W1_DS2485
CONFIG_WDT_ADI_MAX42500
CONFIG_WDT_NPM10XX
CONFIG_WDT_NPM13XX
CONFIG_WDT_NPM2100
CONFIG_WDT_NPM6001
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_m2_ieee802154/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_ieee802154/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`drivers/i2c/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SHIELD_ADI_LSMSPG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHIELD_ADI_LSMSPG)、[`CONFIG_ADC_ADCXX1C`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADCXX1C)、[`CONFIG_ADC_ADS1112`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS1112)、[`CONFIG_ADC_ADS1119`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS1119)、[`CONFIG_ADC_ADS1X1X`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS1X1X)、[`CONFIG_ADC_ADS7828`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ADS7828)、[`CONFIG_ADC_LTC2451`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_LTC2451)、[`CONFIG_ADC_MCP3221`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MCP3221)、[`CONFIG_ADC_TLA202X`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_TLA202X)、[`CONFIG_AUDIO_CODEC_AW88298`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC_AW88298)、[`CONFIG_AUDIO_CODEC_CS35LXX_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AUDIO_CODEC_CS35LXX_I2C)、[`CONFIG_AUDIO_CODEC_CS43L22`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC_CS43L22)、[`CONFIG_AUDIO_CODEC_DA7212`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC_DA7212)、[`CONFIG_AUDIO_CODEC_MAX98091`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC_MAX98091)、[`CONFIG_AUDIO_CODEC_PCM1681`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC_PCM1681)、[`CONFIG_AUDIO_TAS2563`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_TAS2563)、[`CONFIG_AUDIO_TAS6422DAC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_TAS6422DAC)、[`CONFIG_AUDIO_TLV320AIC3110`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_TLV320AIC3110)、[`CONFIG_AUDIO_TLV320DAC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_TLV320DAC)、[`CONFIG_AUDIO_CODEC_WM8904`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC_WM8904)、[`CONFIG_AUDIO_CODEC_WM8960`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC_WM8960)、[`CONFIG_AUDIO_CODEC_WM8962`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC_WM8962)、[`CONFIG_AUXDISPLAY_JHD1313`](P051_drivers_auxdisplay_配置项参考.md#CONFIG_AUXDISPLAY_JHD1313)、[`CONFIG_AUXDISPLAY_SERLCD`](P051_drivers_auxdisplay_配置项参考.md#CONFIG_AUXDISPLAY_SERLCD)、[`CONFIG_BBRAM_MICROCHIP_MCP7940N`](P052_drivers_bbram_配置项参考.md#CONFIG_BBRAM_MICROCHIP_MCP7940N)、[`CONFIG_CHARGER_AXP2101`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER_AXP2101)、[`CONFIG_CHARGER_BQ24190`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER_BQ24190)、[`CONFIG_CHARGER_BQ2429X`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER_BQ2429X)、[`CONFIG_CHARGER_BQ2518X`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER_BQ2518X)、[`CONFIG_CHARGER_BQ25713`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER_BQ25713)、[`CONFIG_CHARGER_MAX20335`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER_MAX20335)、[`CONFIG_CHARGER_NPM10XX`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER_NPM10XX)、[`CONFIG_CHARGER_PCA9422`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER_PCA9422)、[`CONFIG_CHARGER_PF1550`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER_PF1550)、[`CONFIG_SBS_CHARGER`](P061_drivers_charger_配置项参考.md#CONFIG_SBS_CHARGER)、[`CONFIG_CHARGER_SY6974B`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER_SY6974B)、[`CONFIG_CLOCK_CONTROL_TI_CDCE9XX`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_TI_CDCE9XX)、[`CONFIG_COUNTER_MICROCHIP_MCP7940N`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_MICROCHIP_MCP7940N)、[`CONFIG_DAC_AD569X`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_AD569X)、[`CONFIG_DAC_DACX0501`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_DACX0501)、[`CONFIG_DAC_DACX3608`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_DACX3608)、[`CONFIG_DAC_MCP4725`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_MCP4725)、[`CONFIG_DAC_MCP4728`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_MCP4728)、[`CONFIG_ADV7535`](P077_drivers_display_配置项参考_1.md#CONFIG_ADV7535)、[`CONFIG_IST3931`](P077_drivers_display_配置项参考_1.md#CONFIG_IST3931)、[`CONFIG_SSD1327_5`](P078_drivers_display_配置项参考_2.md#CONFIG_SSD1327_5)、[`CONFIG_WAVESHARE_DSI2DPI`](P078_drivers_display_配置项参考_2.md#CONFIG_WAVESHARE_DSI2DPI)、[`CONFIG_EEPROM_AT24`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM_AT24)、[`CONFIG_EEPROM_MB85RCXX`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM_MB85RCXX)、[`CONFIG_SLG471X5_FPGA`](P095_drivers_fpga_配置项参考.md#CONFIG_SLG471X5_FPGA)、[`CONFIG_FUEL_GAUGE_AXP2101`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_FUEL_GAUGE_AXP2101)、[`CONFIG_BQ27Z746`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_BQ27Z746)、[`CONFIG_BQ40Z50`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_BQ40Z50)、[`CONFIG_HY4245`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_HY4245)、[`CONFIG_LC709203F`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_LC709203F)、[`CONFIG_FUEL_GAUGE_LTC2959`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_FUEL_GAUGE_LTC2959)、[`CONFIG_MAX17048`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_MAX17048)、[`CONFIG_SBS_GAUGE_NEW_API`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_SBS_GAUGE_NEW_API)、[`CONFIG_SY24561`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_SY24561)、[`CONFIG_GPIO_ADP5585`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_ADP5585)、[`CONFIG_GPIO_AW9523B`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_AW9523B)、[`CONFIG_GPIO_AXP192`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_AXP192)、[`CONFIG_GPIO_ITE_IT8801`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_ITE_IT8801)、[`CONFIG_GPIO_MCP230XX`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_MCP230XX)、[`CONFIG_GPIO_MFXSTM32L152`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_MFXSTM32L152)、[`CONFIG_GPIO_NCT38XX`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_NCT38XX)、[`CONFIG_GPIO_NPM10XX`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_NPM10XX)、[`CONFIG_GPIO_NPM13XX`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_NPM13XX)、[`CONFIG_GPIO_NPM2100`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_NPM2100)、[`CONFIG_GPIO_NPM6001`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_NPM6001)、[`CONFIG_GPIO_PCA953X`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_PCA953X)、[`CONFIG_GPIO_PCA_SERIES`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_PCA_SERIES)、[`CONFIG_GPIO_PCAL64XXA`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_PCAL64XXA)、[`CONFIG_GPIO_PCF857X`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_PCF857X)、[`CONFIG_GPIO_PI4IOE5V6408`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_PI4IOE5V6408)、[`CONFIG_GPIO_SX1509B`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_SX1509B)、[`CONFIG_HAPTICS_CS40LXX_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAPTICS_CS40LXX_I2C)、[`CONFIG_HAPTICS_DRV2605`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS_DRV2605)、[`CONFIG_HAPTICS_TM6605`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS_TM6605)、[`CONFIG_INPUT_ADAFRUIT_SEESAW_GAMEPAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_ADAFRUIT_SEESAW_GAMEPAD)、[`CONFIG_INPUT_CAP12XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_CAP12XX)、[`CONFIG_INPUT_CF1133`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_CF1133)、[`CONFIG_INPUT_CHSC5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_CHSC5X)、[`CONFIG_INPUT_CHSC6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_CHSC6X)、[`CONFIG_INPUT_CST8XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_CST8XX)、[`CONFIG_INPUT_CY8CMBR3XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_CY8CMBR3XXX)、[`CONFIG_INPUT_FT5336`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_FT5336)、[`CONFIG_INPUT_FT6146`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_FT6146)、[`CONFIG_INPUT_GT911`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_GT911)、[`CONFIG_INPUT_ILI2132A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_ILI2132A)、[`CONFIG_INPUT_ITE_IT8801_KBD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_ITE_IT8801_KBD)、[`CONFIG_INPUT_MODULINO_BUTTONS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_MODULINO_BUTTONS)、[`CONFIG_INPUT_NUNCHUK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_NUNCHUK)、[`CONFIG_INPUT_PAT912X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_PAT912X)、[`CONFIG_INPUT_STMPE811`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_STMPE811)、[`CONFIG_INPUT_TMA525B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_TMA525B)、[`CONFIG_INPUT_TSM12`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_TSM12)、[`CONFIG_LED_AW9523B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LED_AW9523B)、[`CONFIG_LED_AXP192_AXP2101`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LED_AXP192_AXP2101)、[`CONFIG_HT16K33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HT16K33)、[`CONFIG_IS31FL319X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IS31FL319X)、[`CONFIG_IS31FL3216A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IS31FL3216A)、[`CONFIG_IS31FL3733`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IS31FL3733)、[`CONFIG_LP3943`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LP3943)、[`CONFIG_LP50XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LP50XX)、[`CONFIG_LP5562`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LP5562)、[`CONFIG_LP5569`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LP5569)、[`CONFIG_LP586X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LP586X)、[`CONFIG_MODULINO_BUTTONS_LEDS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODULINO_BUTTONS_LEDS)、[`CONFIG_NCP5623`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NCP5623)、[`CONFIG_LED_NPM10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LED_NPM10XX)、[`CONFIG_LED_NPM13XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LED_NPM13XX)、[`CONFIG_PCA953X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PCA953X)、[`CONFIG_PCA9633`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PCA9633)、[`CONFIG_TLC59108`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TLC59108)、[`CONFIG_MODULINO_PIXELS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODULINO_PIXELS)、[`CONFIG_MFD_ADP5360`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD_ADP5360)、[`CONFIG_MFD_AW9523B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD_AW9523B)、[`CONFIG_MFD_AXP192`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD_AXP192)、[`CONFIG_MFD_AXP2101`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD_AXP2101)、[`CONFIG_MFD_DS3231`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD_DS3231)、[`CONFIG_MFD_ITE_IT8801`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD_ITE_IT8801)、[`CONFIG_MFD_M5PM1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD_M5PM1)、[`CONFIG_MFD_MAX20335`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD_MAX20335)、[`CONFIG_MFD_MAX31790`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD_MAX31790)、[`CONFIG_MFD_NCT38XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD_NCT38XX)、[`CONFIG_MFD_NPM10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD_NPM10XX)、[`CONFIG_MFD_NPM13XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD_NPM13XX)、[`CONFIG_MFD_NPM2100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD_NPM2100)、[`CONFIG_MFD_NPM6001`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD_NPM6001)、[`CONFIG_MFD_PCA9422`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD_PCA9422)、[`CONFIG_MFD_PF1550`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD_PF1550)、[`CONFIG_MFD_RV3028`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD_RV3028)、[`CONFIG_MFD_RV3032`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD_RV3032)、[`CONFIG_MFD_SC18IS606`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD_SC18IS606)、[`CONFIG_MFD_TLA2528`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD_TLA2528)、[`CONFIG_TI_TDP2004`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TI_TDP2004)、[`CONFIG_OTP_NPM10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OTP_NPM10XX)、[`CONFIG_PWM_ITE_IT8801`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PWM_ITE_IT8801)、[`CONFIG_PWM_PCA9685`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PWM_PCA9685)、[`CONFIG_REGULATOR_AXP192_AXP2101`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REGULATOR_AXP192_AXP2101)、[`CONFIG_REGULATOR_MAX20335`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REGULATOR_MAX20335)、[`CONFIG_REGULATOR_MAX20362`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REGULATOR_MAX20362)、[`CONFIG_REGULATOR_MODULINO_LATCH_RELAY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REGULATOR_MODULINO_LATCH_RELAY)、[`CONFIG_REGULATOR_MPM54304`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REGULATOR_MPM54304)、[`CONFIG_REGULATOR_NPM10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REGULATOR_NPM10XX)、[`CONFIG_REGULATOR_NPM13XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REGULATOR_NPM13XX)、[`CONFIG_REGULATOR_NPM2100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REGULATOR_NPM2100)、[`CONFIG_REGULATOR_NPM6001`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REGULATOR_NPM6001)、[`CONFIG_REGULATOR_PCA9420`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REGULATOR_PCA9420)、[`CONFIG_REGULATOR_PCA9422`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REGULATOR_PCA9422)、[`CONFIG_REGULATOR_PF1550`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REGULATOR_PF1550)、[`CONFIG_REGULATOR_TI_TPS6287X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REGULATOR_TI_TPS6287X)、[`CONFIG_REGULATOR_TPS55287`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REGULATOR_TPS55287)、[`CONFIG_RTC_AM1805`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTC_AM1805)、[`CONFIG_RTC_BQ32002`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTC_BQ32002)、[`CONFIG_RTC_DS1307`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTC_DS1307)、[`CONFIG_RTC_DS1337`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTC_DS1337)、[`CONFIG_RTC_DS3231`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTC_DS3231)、[`CONFIG_RTC_MAX31331`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTC_MAX31331)、[`CONFIG_RTC_PCF85063A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTC_PCF85063A)、[`CONFIG_RTC_PCF8523`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTC_PCF8523)、[`CONFIG_RTC_PCF8563`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTC_PCF8563)、[`CONFIG_RTC_RV8263`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTC_RV8263)、[`CONFIG_RTC_RV8803`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTC_RV8803)、[`CONFIG_RTC_RX8130CE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTC_RX8130CE)、[`CONFIG_ADLTC2990`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADLTC2990)、[`CONFIG_ADT7420`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADT7420)、[`CONFIG_ADXL313`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADXL313)、[`CONFIG_ADXL367`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADXL367)、[`CONFIG_LTC4286`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LTC4286)、[`CONFIG_MAX30210`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MAX30210)、[`CONFIG_SENSOR_MAX32664C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_MAX32664C)、[`CONFIG_ALS31300`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ALS31300)、[`CONFIG_AMS_AS5600`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMS_AS5600)、[`CONFIG_AMS_IAQ_CORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMS_IAQ_CORE)、[`CONFIG_CCS811`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CCS811)、[`CONFIG_ENS210`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ENS210)、[`CONFIG_TCS3400`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TCS3400)、[`CONFIG_TCS34725`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TCS34725)、[`CONFIG_TMD2620`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TMD2620)、[`CONFIG_TSL2540`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TSL2540)、[`CONFIG_TSL2561`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TSL2561)、[`CONFIG_TSL2591`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TSL2591)、[`CONFIG_AGS10`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AGS10)、[`CONFIG_DHT20`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DHT20)、[`CONFIG_AK8975`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AK8975)、[`CONFIG_AKM09918C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AKM09918C)、[`CONFIG_BMA280`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMA280)、[`CONFIG_BMA4XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMA4XX)、[`CONFIG_BMC150_MAGN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMC150_MAGN)、[`CONFIG_BMG160`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMG160)、[`CONFIG_BMI08X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMI08X)、[`CONFIG_BMM150`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMM150)、[`CONFIG_BMP180`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMP180)、[`CONFIG_BMP388`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMP388)、[`CONFIG_XGZP68XXD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XGZP68XXD)、[`CONFIG_HMC5883L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HMC5883L)、[`CONFIG_MPR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MPR)、[`CONFIG_DPS310`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DPS310)、[`CONFIG_JC42`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_JC42)、[`CONFIG_LTR55X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LTR55X)、[`CONFIG_LTR_F216A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LTR_F216A)、[`CONFIG_SENSOR_DS3231`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_DS3231)、[`CONFIG_MAX17055`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MAX17055)、[`CONFIG_MAX17262`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MAX17262)、[`CONFIG_MAX31875`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MAX31875)、[`CONFIG_MAX44009`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MAX44009)、[`CONFIG_HTU31D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HTU31D)、[`CONFIG_MS5637`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MS5637)、[`CONFIG_MS5837`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MS5837)、[`CONFIG_MLX90394`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MLX90394)、[`CONFIG_MCP9600`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCP9600)、[`CONFIG_PAC194X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PAC194X)、[`CONFIG_TCN75A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TCN75A)、[`CONFIG_NPM10XX_ADC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NPM10XX_ADC)、[`CONFIG_NPM13XX_CHARGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NPM13XX_CHARGER)、[`CONFIG_NPM2100_VBAT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NPM2100_VBAT)、[`CONFIG_2SMPB_02E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_2SMPB_02E)、[`CONFIG_PAJ7620`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PAJ7620)、[`CONFIG_PMSA003I`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PMSA003I)、[`CONFIG_QMI8658A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QMI8658A)、[`CONFIG_HS300X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HS300X)、[`CONFIG_ISL29035`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ISL29035)、[`CONFIG_BH1730`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BH1730)、[`CONFIG_BH1750`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BH1750)、[`CONFIG_BH1790`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BH1790)、[`CONFIG_HM330X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HM330X)、[`CONFIG_SCD4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SCD4X)、[`CONFIG_SGP40`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SGP40)、[`CONFIG_SHT3XD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHT3XD)、[`CONFIG_SHT4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHT4X)、[`CONFIG_SHTCX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHTCX)、[`CONFIG_STCC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STCC4)、[`CONFIG_STS4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STS4X)、[`CONFIG_SI7006`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SI7006)、[`CONFIG_SI7055`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SI7055)、[`CONFIG_SI7060`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SI7060)、[`CONFIG_SI7210`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SI7210)、[`CONFIG_LIS2DUX12`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS2DUX12)、[`CONFIG_LIS3MDL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS3MDL)、[`CONFIG_LPS22HB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LPS22HB)、[`CONFIG_LPS25HB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LPS25HB)、[`CONFIG_LPS2XDF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LPS2XDF)、[`CONFIG_LSM303DLHC_MAGN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM303DLHC_MAGN)、[`CONFIG_LSM6DS0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DS0)、[`CONFIG_LSM6DSO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSO)、[`CONFIG_LSM6DSV16X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSV16X)、[`CONFIG_LSM6DSVXXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSVXXX)、[`CONFIG_LSM9DS0_GYRO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM9DS0_GYRO)、[`CONFIG_LSM9DS0_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM9DS0_MFD)、[`CONFIG_LSM9DS1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM9DS1)、[`CONFIG_LSM9DS1_MAG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM9DS1_MAG)、[`CONFIG_STTS22H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STTS22H)、[`CONFIG_STTS751`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STTS751)、[`CONFIG_VL53L0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VL53L0X)、[`CONFIG_VL53L1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VL53L1X)、[`CONFIG_VL53L5CX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VL53L5CX)、[`CONFIG_ICM40627`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICM40627)、[`CONFIG_ICM42X70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICM42X70)、[`CONFIG_ICM45686`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICM45686)、[`CONFIG_ICM566XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICM566XX)、[`CONFIG_ICP101XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICP101XX)、[`CONFIG_MPU6050`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MPU6050)、[`CONFIG_MPU9250`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MPU9250)、[`CONFIG_BQ274XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BQ274XX)、[`CONFIG_FDC1004`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FDC1004)、[`CONFIG_FDC2X1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FDC2X1X)、[`CONFIG_INA219`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INA219)、[`CONFIG_INA2XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INA2XX)、[`CONFIG_INA3221`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INA3221)、[`CONFIG_INA7XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INA7XX)、[`CONFIG_LM95234`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LM95234)、[`CONFIG_OPT300X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPT300X)、[`CONFIG_TI_HDC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TI_HDC)、[`CONFIG_TI_HDC20XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TI_HDC20XX)、[`CONFIG_TI_HDC302X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TI_HDC302X)、[`CONFIG_TMAG5273`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TMAG5273)、[`CONFIG_TMP007`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TMP007)、[`CONFIG_TMP1075`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TMP1075)、[`CONFIG_TMP108`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TMP108)、[`CONFIG_TMP112`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TMP112)、[`CONFIG_TMP114`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TMP114)、[`CONFIG_TMP11X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TMP11X)、[`CONFIG_TMP435`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TMP435)、[`CONFIG_TMP451`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TMP451)、[`CONFIG_VCNL36825T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VCNL36825T)、[`CONFIG_VCNL4040`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VCNL4040)、[`CONFIG_VEML6031`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VEML6031)、[`CONFIG_VEML6046`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VEML6046)、[`CONFIG_VEML7700`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VEML7700)、[`CONFIG_WSEN_HIDS_2525020210002`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WSEN_HIDS_2525020210002)、[`CONFIG_WSEN_PDUS_25131308XXXXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WSEN_PDUS_25131308XXXXX)、[`CONFIG_WSEN_TIDS_2521020222501`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WSEN_TIDS_2521020222501)、[`CONFIG_AMD_SB_TSI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMD_SB_TSI)、[`CONFIG_AMG88XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMG88XX)、[`CONFIG_APDS9253`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_APDS9253)、[`CONFIG_APDS9306`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_APDS9306)、[`CONFIG_APDS9960`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_APDS9960)、[`CONFIG_CHT8315`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CHT8315)、[`CONFIG_F75303`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_F75303)、[`CONFIG_HP206C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HP206C)、[`CONFIG_IST8310`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IST8310)、[`CONFIG_LM75`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LM75)、[`CONFIG_LM77`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LM77)、[`CONFIG_MB7040`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MB7040)、[`CONFIG_NCT75`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NCT75)、[`CONFIG_S11059`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_S11059)、[`CONFIG_SBS_GAUGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SBS_GAUGE)、[`CONFIG_SX9500`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SX9500)、[`CONFIG_TH02`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TH02)、[`CONFIG_XBR818`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XBR818)、[`CONFIG_USBC_TCPC_TCPCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBC_TCPC_TCPCI)、[`CONFIG_VIDEO_GC2145`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_GC2145)、[`CONFIG_VIDEO_HM01B0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_HM01B0)、[`CONFIG_VIDEO_HM0360`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_HM0360)、[`CONFIG_VIDEO_IMX219`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_IMX219)、[`CONFIG_VIDEO_IMX335`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_IMX335)、[`CONFIG_VIDEO_MT9M114`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_MT9M114)、[`CONFIG_VIDEO_OV2640`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_OV2640)、[`CONFIG_VIDEO_OV5640`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_OV5640)、[`CONFIG_VIDEO_OV5642`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_OV5642)、[`CONFIG_VIDEO_OV767X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_OV767X)、[`CONFIG_VIDEO_OV7725`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_OV7725)、[`CONFIG_VIDEO_OV9655`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_OV9655)、[`CONFIG_VIDEO_ST_MIPID02`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_ST_MIPID02)、[`CONFIG_W1_DS2482_800`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_W1_DS2482_800)、[`CONFIG_W1_DS2484`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_W1_DS2484)、[`CONFIG_W1_DS2485`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_W1_DS2485)、[`CONFIG_WDT_ADI_MAX42500`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WDT_ADI_MAX42500)、[`CONFIG_WDT_NPM10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WDT_NPM10XX)、[`CONFIG_WDT_NPM13XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WDT_NPM13XX)、[`CONFIG_WDT_NPM2100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WDT_NPM2100)、[`CONFIG_WDT_NPM6001`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WDT_NPM6001)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SHIELD_ADI_LSMSPG`、`CONFIG_AUDIO_CODEC_CS35LXX_I2C`、`CONFIG_HAPTICS_CS40LXX_I2C`。

<a id="CONFIG_I2C_ALLOW_NO_STOP_TRANSACTIONS"></a>

## 105.3 `CONFIG_I2C_ALLOW_NO_STOP_TRANSACTIONS`

**提示（Prompt）**：允许最后一次事务不产生 STOP 的 I²C 传输【已弃用（DEPRECATED）】

**说明（Help）**

允许最后一条消息不产生停止条件（STOP）的 I²C 事务。此用法不受支持，可能使总线处于非预期状态。原文说明此选项将在 Zephyr 4.1 中移除。译注：这里保留所用官方快照的版本表述。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_I2C_NRFX_TWI && !CONFIG_I2C_NRFX_TWIM && !CONFIG_I2C_STM32 && !CONFIG_I2C_GD32 && !CONFIG_I2C_ESP32 && (!CONFIG_I2C_DW || CONFIG_I2C_RTS5912) && CONFIG_I2C
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**被选择（Selected by）**

```text
CONFIG_I2C_RTS5912
```

**定义位置（Location）**：[`drivers/i2c/Kconfig:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_NRFX_TWI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_NRFX_TWI)、[`CONFIG_I2C_NRFX_TWIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_NRFX_TWIM)、[`CONFIG_I2C_STM32`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_STM32)、[`CONFIG_I2C_GD32`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_GD32)、[`CONFIG_I2C_ESP32`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_ESP32)、[`CONFIG_I2C_DW`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_DW)、[`CONFIG_I2C_RTS5912`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTS5912)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_I2C_NRFX_TWI`、`CONFIG_I2C_NRFX_TWIM`。

<a id="CONFIG_I2C_AMBIQ"></a>

## 105.4 `CONFIG_I2C_AMBIQ`

**提示（Prompt）**：AMBIQ I²C 驱动

**说明（Help）**

启用 Ambiq I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMBIQ_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_AMBIQ_HAL
CONFIG_AMBIQ_HAL_USE_I2C
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.ambiq:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.ambiq#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_AMBIQ_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL)、[`CONFIG_AMBIQ_HAL_USE_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL_USE_I2C)。

<a id="CONFIG_I2C_AMBIQ_BUS_RECOVERY"></a>

## 105.5 `CONFIG_I2C_AMBIQ_BUS_RECOVERY`

**提示（Prompt）**：总线恢复（Bus Recovery）支持

**说明（Help）**

启用 AMBIQ 驱动通过 GPIO 位操作模拟（Bit Banging）实现的总线恢复支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_AMBIQ && CONFIG_I2C
```

**默认值（Defaults）**

```text
y if CONFIG_I2C_BUS_RECOVERY
```

**主动选择（Selects）**

```text
CONFIG_I2C_BITBANG
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.ambiq:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.ambiq#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → AMBIQ I²C 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_AMBIQ`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_AMBIQ)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_BUS_RECOVERY`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_BUS_RECOVERY)、[`CONFIG_I2C_BITBANG`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_BITBANG)。

<a id="CONFIG_I2C_AMBIQ_HANDLE_CACHE"></a>

## 105.6 `CONFIG_I2C_AMBIQ_HANDLE_CACHE`

**提示（Prompt）**：在 I²C 驱动中启用缓存处理（Cache Handling）

**说明（Help）**

如果上层已处理缓存（Cache），则禁用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CACHE_MANAGEMENT && CONFIG_DCACHE && CONFIG_I2C_AMBIQ && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.ambiq:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.ambiq#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → AMBIQ I²C 驱动

**配置项引用（Symbol References）**：[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_I2C_AMBIQ`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_AMBIQ)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_AMBIQ_IOS"></a>

## 105.7 `CONFIG_I2C_AMBIQ_IOS`

**提示（Prompt）**：AMBIQ IOS I²C 目标设备（Target）驱动

**说明（Help）**

启用目标设备（Target）模式下的 Ambiq I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMBIQ_IOS_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_AMBIQ_HAL
CONFIG_AMBIQ_HAL_USE_IOS_I2C
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.ambiq:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.ambiq#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_AMBIQ_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL)、[`CONFIG_AMBIQ_HAL_USE_IOS_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL_USE_IOS_I2C)。

<a id="CONFIG_I2C_AMEBA"></a>

## 105.8 `CONFIG_I2C_AMEBA`

**提示（Prompt）**：AMEBA I²C 驱动

**说明（Help）**

启用 AMEBA I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_AMEBA_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.ameba:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.ameba#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_AMEBA_INTERRUPT"></a>

## 105.9 `CONFIG_I2C_AMEBA_INTERRUPT`

**提示（Prompt）**：Ameba I²C 中断（Interrupt）支持

**说明（Help）**

为 I²C 驱动启用中断（Interrupt）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_AMEBA && CONFIG_I2C
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.ameba:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.ameba#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → AMEBA I²C 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_AMEBA`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_AMEBA)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_ANDES_ATCIIC100"></a>

## 105.10 `CONFIG_I2C_ANDES_ATCIIC100`

**提示（Prompt）**：Andes ATCIIC100 I²C 驱动

**说明（Help）**

启用 Andes ATCIIC100 I²C 控制器（Controller）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ANDESTECH_ATCIIC100_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.andes_atciic100:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.andes_atciic100#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_ASYNC_API"></a>

## 105.11 `CONFIG_I2C_ASYNC_API`

**提示（Prompt）**：Ameba I²C DMA 支持

**说明（Help）**

为 I²C 驱动启用 DMQ 支持。译注：帮助原文写作 DMQ，而选项标题为 DMA；此处保留该差异。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_AMEBA && CONFIG_I2C
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.ameba:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.ameba#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → AMEBA I²C 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_AMEBA`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_AMEBA)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_I2C_BCM2711"></a>

## 105.12 `CONFIG_I2C_BCM2711`

**提示（Prompt）**：Broadcom BCM2711 I²C 控制器（Controller）

**说明（Help）**

启用 Broadcom BCM2711 I²C 控制器支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BRCM_BCM2711_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.bcm2711:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.bcm2711#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_BCM2711_BUS_RECOVERY"></a>

## 105.13 `CONFIG_I2C_BCM2711_BUS_RECOVERY`

**提示（Prompt）**：总线恢复（Bus Recovery）支持

**说明（Help）**

启用 BCM2711 驱动通过 GPIO 位操作模拟（Bit Banging）实现的总线恢复支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_BCM2711 && CONFIG_I2C
```

**默认值（Defaults）**

```text
y if CONFIG_I2C_BUS_RECOVERY
```

**主动选择（Selects）**

```text
CONFIG_I2C_BITBANG
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.bcm2711:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.bcm2711#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → Broadcom BCM2711 I²C 控制器（Controller）

**配置项引用（Symbol References）**：[`CONFIG_I2C_BCM2711`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_BCM2711)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_BUS_RECOVERY`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_BUS_RECOVERY)、[`CONFIG_I2C_BITBANG`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_BITBANG)。

<a id="CONFIG_I2C_BEE"></a>

## 105.14 `CONFIG_I2C_BEE`

**提示（Prompt）**：Realtek Bee 系列 I²C 驱动

**说明（Help）**

此选项启用 Realtek Bee 系统级芯片（SoC）的 I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_BEE_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAL_REALTEK_BEE_I2C
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.bee:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.bee#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_HAL_REALTEK_BEE_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAL_REALTEK_BEE_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAL_REALTEK_BEE_I2C`。

<a id="CONFIG_I2C_BFLB"></a>

## 105.15 `CONFIG_I2C_BFLB`

**提示（Prompt）**：Bouffalolab I²C 驱动

**说明（Help）**

Bouffalolab 平台的 I²C 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.bflb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.bflb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_BITBANG"></a>

## 105.16 `CONFIG_I2C_BITBANG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用用于软件驱动（位操作模拟，Bit Banging）I²C 支持的库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C
```

**被选择（Selected by）**

```text
CONFIG_I2C_AMBIQ_BUS_RECOVERY
CONFIG_I2C_BCM2711_BUS_RECOVERY
CONFIG_I2C_GPIO
CONFIG_I2C_ITE_IT51XXX
CONFIG_I2C_ITE_IT8XXX2
CONFIG_I2C_ITE_ENHANCE
CONFIG_I2C_LITEX
CONFIG_I2C_MCUX_FLEXCOMM_BUS_RECOVERY
CONFIG_I2C_OMAP_BUS_RECOVERY
CONFIG_I2C_RENESAS_RA_IIC_BUS_RECOVERY
CONFIG_I2C_SBCON
CONFIG_I2C_STM32_BUS_RECOVERY
CONFIG_I2C_MCUX_LPI2C_BUS_RECOVERY
```

**定义位置（Location）**：[`drivers/i2c/Kconfig:285`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig#L285)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_AMBIQ_BUS_RECOVERY`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_AMBIQ_BUS_RECOVERY)、[`CONFIG_I2C_BCM2711_BUS_RECOVERY`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_BCM2711_BUS_RECOVERY)、[`CONFIG_I2C_GPIO`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_GPIO)、[`CONFIG_I2C_ITE_IT51XXX`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_ITE_IT51XXX)、[`CONFIG_I2C_ITE_IT8XXX2`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_ITE_IT8XXX2)、[`CONFIG_I2C_ITE_ENHANCE`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_ITE_ENHANCE)、[`CONFIG_I2C_LITEX`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_LITEX)、[`CONFIG_I2C_MCUX_FLEXCOMM_BUS_RECOVERY`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_MCUX_FLEXCOMM_BUS_RECOVERY)、[`CONFIG_I2C_OMAP_BUS_RECOVERY`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_OMAP_BUS_RECOVERY)、[`CONFIG_I2C_RENESAS_RA_IIC_BUS_RECOVERY`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_RENESAS_RA_IIC_BUS_RECOVERY)、[`CONFIG_I2C_SBCON`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_SBCON)、[`CONFIG_I2C_STM32_BUS_RECOVERY`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_STM32_BUS_RECOVERY)、[`CONFIG_I2C_MCUX_LPI2C_BUS_RECOVERY`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_MCUX_LPI2C_BUS_RECOVERY)。

<a id="CONFIG_I2C_BUS_RECOVERY"></a>

## 105.17 `CONFIG_I2C_BUS_RECOVERY`

**提示（Prompt）**：允许 I²C 总线恢复（Bus Recovery）支持。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/i2c/Kconfig:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_CADENCE"></a>

## 105.18 `CONFIG_I2C_CADENCE`

**提示（Prompt）**：Cadence I²C 驱动

**说明（Help）**

启用 Cadence I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_CDNS_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_EVENTS
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.cdns:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.cdns#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)。

<a id="CONFIG_I2C_CADENCE_BROKEN_HOLD_BIT"></a>

## 105.19 `CONFIG_I2C_CADENCE_BROKEN_HOLD_BIT`

**提示（Prompt）**：针对 Zynq-7000 勘误（Errata）情形的规避措施

**说明（Help）**

禁止读操作后紧接重复起始条件（Repeated Start）的消息传输。还会在消息接收期间，从写地址寄存器到写控制寄存器之间禁用中断，以防传输大小寄存器发生回绕（Rollover）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_CADENCE && CONFIG_I2C
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.cdns:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.cdns#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → Cadence I²C 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_CADENCE`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_CADENCE)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_CALLBACK"></a>

## 105.20 `CONFIG_I2C_CALLBACK`

**提示（Prompt）**：I²C 异步回调（Asynchronous Callback）API

**说明（Help）**

`i2c_transfer_cb` 的 API 及实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/i2c/Kconfig:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_CC13XX_CC26XX"></a>

## 105.21 `CONFIG_I2C_CC13XX_CC26XX`

**提示（Prompt）**：TI SimpleLink CC13xx / CC26xx I²C 驱动

**说明（Help）**

启用 TI SimpleLink CC13xx / CC26xx 系列的 I²C 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_CC13XX_CC26XX_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.cc13xx_cc26xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.cc13xx_cc26xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_CC23X0"></a>

## 105.22 `CONFIG_I2C_CC23X0`

**提示（Prompt）**：TI SimpleLink CC23x0 I²C 驱动

**说明（Help）**

启用 TI SimpleLink CC23x0 系列的 I²C 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_CC23X0_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.cc23x0:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.cc23x0#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_CC32XX"></a>

## 105.23 `CONFIG_I2C_CC32XX`

**提示（Prompt）**：CC32XX I²C 驱动

**说明（Help）**

启用 CC32XX I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_CC32XX_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig:277`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig#L277)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_CODE_IN_RAM"></a>

## 105.24 `CONFIG_I2C_CODE_IN_RAM`

**提示（Prompt）**：RAM 中的代码函数（RAM Code Functions）

**说明（Help）**

将关键函数放入 RAM 段（Section），确保它们以尽可能小的延迟运行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_ITE_ENHANCE && CONFIG_I2C
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.it8xxx2:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.it8xxx2#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → ITE IT8XXX2 增强型（Enhance）I²C 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_ITE_ENHANCE`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_ITE_ENHANCE)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_CQ_MODE_MAX_PAYLOAD_SIZE"></a>

## 105.25 `CONFIG_I2C_CQ_MODE_MAX_PAYLOAD_SIZE`

**提示（Prompt）**：允许配置的大小上限为 2K 字节。

**说明（Help）**

这是命令队列（Command Queue）模式的有效载荷大小，上限为 2k 字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_ITE_ENHANCE && CONFIG_I2C
```

**默认值（Defaults）**

```text
64
```

**取值范围（Ranges）**

```text
[32, 2048]
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.it8xxx2:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.it8xxx2#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → ITE IT8XXX2 增强型（Enhance）I²C 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_ITE_ENHANCE`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_ITE_ENHANCE)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_DUMP_MESSAGES"></a>

## 105.26 `CONFIG_I2C_DUMP_MESSAGES`

**提示（Prompt）**：记录 I²C 事务（Transaction）

**说明（Help）**

将每次 I²C 事务转储到系统日志，日志级别为调试（Debug）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_I2C_LOG_LEVEL_DBG && CONFIG_I2C
```

**定义位置（Location）**：[`drivers/i2c/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_I2C_LOG_LEVEL_DBG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_LOG_LEVEL_DBG)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_DUMP_MESSAGES_ALLOWLIST"></a>

## 105.27 `CONFIG_I2C_DUMP_MESSAGES_ALLOWLIST`

**提示（Prompt）**：使用允许列表（Allowlist）记录 I²C 事务

**说明（Help）**

使用允许列表（Allowlist）指定应记录哪些设备的事务。在设备树（Devicetree）中，使用兼容字符串（Compatible String）`zephyr,i2c-dump-allowlist` 和指向待跟踪设备的句柄（Phandle）定义允许列表。设备树节点示例：

```dts
i2c-dump-allowlist {
  compatible = "zephyr,i2c-dump-allowlist";
  devices = <&display0>, <&sensor3>;
};
```

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_DUMP_MESSAGES && DT_HAS_ZEPHYR_I2C_DUMP_ALLOWLIST_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2c/Kconfig:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → 记录 I²C 事务（Transaction）

**配置项引用（Symbol References）**：[`CONFIG_I2C_DUMP_MESSAGES`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_DUMP_MESSAGES)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_DW"></a>

## 105.28 `CONFIG_I2C_DW`

**提示（Prompt）**：Design Ware I²C 支持

**说明（Help）**

启用 Design Ware I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SNPS_DESIGNWARE_I2C_ENABLED && (!n || CONFIG_CLOCK_CONTROL) && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL if n
CONFIG_PCIE if n
CONFIG_DYNAMIC_INTERRUPTS if n
CONFIG_I2C_TRANSFER_TIMEOUT_SUPPORTED
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.dw:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.dw#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_PCIE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PCIE)、[`CONFIG_DYNAMIC_INTERRUPTS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DYNAMIC_INTERRUPTS)、[`CONFIG_I2C_TRANSFER_TIMEOUT_SUPPORTED`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TRANSFER_TIMEOUT_SUPPORTED)。

<a id="CONFIG_I2C_DW_CLOCK_SPEED"></a>

## 105.29 `CONFIG_I2C_DW_CLOCK_SPEED`

**提示（Prompt）**：设置 I²C 时钟速度（Clock Speed）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_DW && CONFIG_I2C
```

**默认值（Defaults）**

```text
100 if CONFIG_I2C_RTS5912
32
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.dw:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.dw#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → Design Ware I²C 支持

**配置项引用（Symbol References）**：[`CONFIG_I2C_DW`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_DW)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_RTS5912`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTS5912)。

<a id="CONFIG_I2C_DW_EXTENDED_SUPPORT"></a>

## 105.30 `CONFIG_I2C_DW_EXTENDED_SUPPORT`

**提示（Prompt）**：扩展 DW 功能（Extended DW Features）

**说明（Help）**

此选项启用 DW I²C 控制器的 SCL/SDA 超时寄存器（Timeout Register）及一些附加功能支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_DW && CONFIG_I2C
```

**被选择（Selected by）**

```text
CONFIG_I2C_RTS5912
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.dw:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.dw#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → Design Ware I²C 支持

**配置项引用（Symbol References）**：[`CONFIG_I2C_DW`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_DW)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_RTS5912`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTS5912)。

<a id="CONFIG_I2C_DW_IC_CLK_FREQ_OPTIMIZATION"></a>

## 105.31 `CONFIG_I2C_DW_IC_CLK_FREQ_OPTIMIZATION`

**提示（Prompt）**：内核时钟频率优化（Core Clock Frequency Optimization）

**说明（Help）**

启用硬件优化，降低所需的 I²C 内核时钟频率。此功能减少生成 SCL 高电平和低电平周期所需的内部延迟周期，使控制器能够以更低的系统时钟频率（`ic_clk`）达到目标总线速度。仅当硬件 IP 支持这一特定延迟缩减功能时才应启用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_DW && CONFIG_I2C
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.dw:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.dw#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → Design Ware I²C 支持

**配置项引用（Symbol References）**：[`CONFIG_I2C_DW`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_DW)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_DW_LPSS_DMA"></a>

## 105.32 `CONFIG_I2C_DW_LPSS_DMA`

**提示（Prompt）**：使用 I²C 集成 DMA 进行异步传输（Asynchronous Transfer）

**说明（Help）**

此选项启用用于异步数据传输的 I²C DMA 功能。所有发送（Tx）操作使用 DMA 通道 0，所有接收（Rx）操作使用 DMA 通道 1。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_I2C_RTS5912 && CONFIG_I2C_DW && CONFIG_I2C
```

**主动选择（Selects）**

```text
CONFIG_DMA
CONFIG_DMA_INTEL_LPSS
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.dw:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.dw#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → Design Ware I²C 支持

**配置项引用（Symbol References）**：[`CONFIG_I2C_RTS5912`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTS5912)、[`CONFIG_I2C_DW`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_DW)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_DMA_INTEL_LPSS`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_INTEL_LPSS)。

<a id="CONFIG_I2C_DW_PM_POLICY_STATE_LOCK"></a>

## 105.33 `CONFIG_I2C_DW_PM_POLICY_STATE_LOCK`

**提示（Prompt）**：在 I²C 传输期间锁定电源管理策略（Power Management Policy）

**说明（Help）**

启用此选项可在 I²C 传输期间阻止电源管理策略状态变化。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_DW && CONFIG_I2C
```

**被选择（Selected by）**

```text
CONFIG_I2C_RTS5912
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.dw:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.dw#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → Design Ware I²C 支持

**配置项引用（Symbol References）**：[`CONFIG_I2C_DW`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_DW)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_RTS5912`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTS5912)。

<a id="CONFIG_I2C_EEPROM_TARGET"></a>

## 105.34 `CONFIG_I2C_EEPROM_TARGET`

**提示（Prompt）**：I²C 目标设备（Target）EEPROM 驱动

**说明（Help）**

启用虚拟 I²C 目标设备（Target）EEPROM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_I2C_TARGET_EEPROM_ENABLED && CONFIG_I2C_TARGET && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C_TARGET_REGSET_LIB
```

**定义位置（Location）**：[`drivers/i2c/target/Kconfig.eeprom:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/target/Kconfig.eeprom#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → I²C 目标设备（Target）驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_TARGET`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TARGET)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_TARGET_REGSET_LIB`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TARGET_REGSET_LIB)。

<a id="CONFIG_I2C_EEPROM_TARGET_RUNTIME_ADDR"></a>

## 105.35 `CONFIG_I2C_EEPROM_TARGET_RUNTIME_ADDR`

**提示（Prompt）**：在运行时（Runtime）设置 I²C 目标设备 EEPROM 地址

**说明（Help）**

启用在运行时更改虚拟 I²C 目标设备 EEPROM 的设备地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_EEPROM_TARGET && CONFIG_I2C_TARGET && CONFIG_I2C
```

**定义位置（Location）**：[`drivers/i2c/target/Kconfig.eeprom:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/target/Kconfig.eeprom#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → I²C 目标设备（Target）驱动 → I²C 目标设备（Target）EEPROM 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_EEPROM_TARGET`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_EEPROM_TARGET)、[`CONFIG_I2C_TARGET`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TARGET)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_EMUL"></a>

## 105.36 `CONFIG_I2C_EMUL`

**提示（Prompt）**：I²C 仿真器（Emulator）

**说明（Help）**

启用 I²C 仿真器驱动。这是一个不与真实硬件通信的模拟驱动，而是与仿真驱动通信，后者扮演仿真 I²C 总线上的设备。它用于测试 I²C 设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_I2C_EMUL_CONTROLLER_ENABLED && CONFIG_EMUL && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.i2c_emul:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.i2c_emul#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EMUL)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_ENE_KB106X"></a>

## 105.37 `CONFIG_I2C_ENE_KB106X`

**提示（Prompt）**：ENE KB106X I²C 驱动

**说明（Help）**

启用 ENE KB106X I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ENE_KB106X_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.ene:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.ene#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_ENE_KB1200"></a>

## 105.38 `CONFIG_I2C_ENE_KB1200`

**提示（Prompt）**：ENE KB1200 I²C 驱动

**说明（Help）**

启用 ENE KB1200 I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ENE_KB1200_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.ene:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.ene#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_ESP32"></a>

## 105.39 `CONFIG_I2C_ESP32`

**提示（Prompt）**：ESP32 I²C 驱动

**说明（Help）**

启用 ESP32 I²C 驱动。同时启用 `CONFIG_I2C_TARGET` 时，驱动会公开 I²C 目标设备（Target）回调。目标模式依赖 SCL 时钟拉伸原因（Stretch-Cause）硬件功能，支持 ESP32-S2、ESP32-S3、ESP32-C3、ESP32-C5、ESP32-C6 和 ESP32-H2，不支持 ESP32 和 ESP32-C2。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO_ESP32
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.esp32:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.esp32#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_GPIO_ESP32`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_ESP32)。

<a id="CONFIG_I2C_ESP32_TARGET_BUF"></a>

## 105.40 `CONFIG_I2C_ESP32_TARGET_BUF`

**提示（Prompt）**：ESP32 I²C 目标设备缓冲接收（Buffered RX）大小

**说明（Help）**

启用 `CONFIG_I2C_TARGET_BUFFER_MODE` 时，ESP32 I²C 目标设备驱动所用每实例 RX 缓冲区的大小，单位为字节。写事务期间接收的字节会暂存，直到控制器发出 STOP，此时调用一次 `buf_write_received`，传入累积数据。读取从 `buf_read_requested` 提供的指针所指数据连续输出，不受此大小限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_ESP32 && CONFIG_I2C_TARGET && CONFIG_I2C_TARGET_BUFFER_MODE && CONFIG_I2C
```

**默认值（Defaults）**

```text
256
```

**取值范围（Ranges）**

```text
[32, 1024]
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.esp32:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.esp32#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → ESP32 I²C 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_ESP32`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_ESP32)、[`CONFIG_I2C_TARGET`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TARGET)、[`CONFIG_I2C_TARGET_BUFFER_MODE`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TARGET_BUFFER_MODE)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_GD32"></a>

## 105.41 `CONFIG_I2C_GD32`

**提示（Prompt）**：GigaDevice GD32 I²C 驱动

**说明（Help）**

启用 GigaDevice GD32 I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GD_GD32_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.gd32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.gd32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_GECKO"></a>

## 105.42 `CONFIG_I2C_GECKO`

**提示（Prompt）**：Gecko I²C 驱动

**说明（Help）**

启用 SiLabs Gecko I²C 总线驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_GECKO_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SILABS_GECKO_I2C
CONFIG_PINCTRL if CONFIG_SOC_FAMILY_SILABS_S2
```

**定义位置（Location）**：[`drivers/i2c/Kconfig:218`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig#L218)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SILABS_GECKO_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_GECKO_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S2`。

<a id="CONFIG_I2C_GPIO"></a>

## 105.43 `CONFIG_I2C_GPIO`

**提示（Prompt）**：GPIO 位操作模拟（Bit Banging）I²C 支持

**说明（Help）**

启用使用 GPIO 引脚、由软件驱动（位操作模拟，Bit Banging）的 I²C 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GPIO_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C_BITBANG
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.gpio:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.gpio#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_BITBANG`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_BITBANG)。

<a id="CONFIG_I2C_GPIO_CLOCK_STRETCHING"></a>

## 105.44 `CONFIG_I2C_GPIO_CLOCK_STRETCHING`

**提示（Prompt）**：GPIO 位操作模拟 I²C 时钟拉伸（Clock Stretching）支持

**说明（Help）**

启用目标设备（Target）时钟拉伸支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_GPIO && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.gpio:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.gpio#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → GPIO 位操作模拟（Bit Banging）I²C 支持

**配置项引用（Symbol References）**：[`CONFIG_I2C_GPIO`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_GPIO)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_GPIO_CLOCK_STRETCHING_TIMEOUT_US"></a>

## 105.45 `CONFIG_I2C_GPIO_CLOCK_STRETCHING_TIMEOUT_US`

**提示（Prompt）**：GPIO 位操作模拟 I²C 时钟拉伸超时（微秒）

**说明（Help）**

时钟拉伸（Clock Stretching）的超时时间，单位为微秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_GPIO && CONFIG_I2C
```

**默认值（Defaults）**

```text
100000
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.gpio:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.gpio#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → GPIO 位操作模拟（Bit Banging）I²C 支持

**配置项引用（Symbol References）**：[`CONFIG_I2C_GPIO`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_GPIO)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_IMX"></a>

## 105.46 `CONFIG_I2C_IMX`

**提示（Prompt）**：i.MX I²C 驱动

**说明（Help）**

启用 i.MX I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_FSL_IMX21_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig:269`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig#L269)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_INFINEON_BUS_RECOVERY"></a>

## 105.47 `CONFIG_I2C_INFINEON_BUS_RECOVERY`

**提示（Prompt）**：总线恢复（Bus Recovery）支持

**说明（Help）**

启用 Infineon I²C 驱动通过 GPIO 位操作模拟（Bit Banging）实现的总线恢复支持。

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
CONFIG_I2C_BITBANG
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.infineon:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.infineon#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_BITBANG`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_BITBANG)。

<a id="CONFIG_I2C_INFINEON_CAT1_HAL"></a>

## 105.48 `CONFIG_I2C_INFINEON_CAT1_HAL`

**提示（Prompt）**：基于 HAL 的 Infineon CAT1 I²C 驱动

**说明（Help）**

此选项启用 Infineon CAT1 系列基于硬件抽象层（HAL）的 I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_I2C_ENABLED && CONFIG_USE_INFINEON_LEGACY_HAL && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_INFINEON_I2C
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.infineon:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.infineon#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_USE_INFINEON_LEGACY_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_LEGACY_HAL)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_USE_INFINEON_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_INFINEON_CAT1_PDL"></a>

## 105.49 `CONFIG_I2C_INFINEON_CAT1_PDL`

**提示（Prompt）**：基于 PDL 的 Infineon CAT1 I²C 驱动

**说明（Help）**

此选项启用 Infineon CAT1 系列基于外设驱动库（PDL）的 I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_I2C_ENABLED && !CONFIG_USE_INFINEON_LEGACY_HAL && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_INFINEON_I2C
CONFIG_PINCTRL
CONFIG_I2C_TRANSFER_TIMEOUT_SUPPORTED
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.infineon:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.infineon#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_USE_INFINEON_LEGACY_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_LEGACY_HAL)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_USE_INFINEON_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_I2C_TRANSFER_TIMEOUT_SUPPORTED`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TRANSFER_TIMEOUT_SUPPORTED)。

<a id="CONFIG_I2C_INFINEON_CAT1_TARGET_BUF"></a>

## 105.50 `CONFIG_I2C_INFINEON_CAT1_TARGET_BUF`

**提示（Prompt）**：I²C 目标设备数据缓冲区长度（Buffer Length）

**说明（Help）**

作为 I²C 目标设备（Target）接收数据的缓冲区。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_INFINEON_I2C && CONFIG_I2C
```

**默认值（Defaults）**

```text
64
```

**取值范围（Ranges）**

```text
[1, 1024]
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.infineon:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.infineon#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_USE_INFINEON_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_I2C)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_INFINEON_XMC4"></a>

## 105.51 `CONFIG_I2C_INFINEON_XMC4`

**提示（Prompt）**：Infineon XMC4 I²C 驱动

**说明（Help）**

此选项启用 Infineon XMC4 系列的 I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_XMC4XXX_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.infineon_xmc4:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.infineon_xmc4#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_INFINEON_XMC4_TARGET_BUF"></a>

## 105.52 `CONFIG_I2C_INFINEON_XMC4_TARGET_BUF`

**提示（Prompt）**：I²C 目标设备数据缓冲区长度（Buffer Length）

**说明（Help）**

作为 I²C 目标设备（Target）接收数据的缓冲区。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_INFINEON_XMC4 && CONFIG_I2C
```

**默认值（Defaults）**

```text
64
```

**取值范围（Ranges）**

```text
[1, 1024]
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.infineon_xmc4:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.infineon_xmc4#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → Infineon XMC4 I²C 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_INFINEON_XMC4`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_INFINEON_XMC4)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_INIT_PRIORITY"></a>

## 105.53 `CONFIG_I2C_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

I²C 设备驱动初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`drivers/i2c/Kconfig:207`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig#L207)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_I2C_IPROC"></a>

## 105.54 `CONFIG_I2C_IPROC`

**提示（Prompt）**：Broadcom iProc I²C 控制器（Controller）

**说明（Help）**

启用 Broadcom iProc I²C 控制器支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BRCM_IPROC_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.bcm_iproc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.bcm_iproc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_IT51XXX_ALL_CH_FIFO_MODE"></a>

## 105.55 `CONFIG_I2C_IT51XXX_ALL_CH_FIFO_MODE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在控制器（Controller）角色下，较老硬件仅提供两个先入先出队列（FIFO），较新硬件则在所有通道上支持 FIFO 模式。设备树中存在 `fifo_ctrl_offset` 属性即表示所有 I²C 通道都支持 FIFO 模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.it51xxx:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.it51xxx#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → ITE IT51XXX I²C 驱动

<a id="CONFIG_I2C_IT51XXX_FIFO_MODE"></a>

## 105.56 `CONFIG_I2C_IT51XXX_FIFO_MODE`

**提示（Prompt）**：IT51XXX I²C FIFO 模式

**说明（Help）**

此选项启用先入先出队列（FIFO）模式，可缩短字节之间的时间，从而改善 I²C 事务期间的总线时钟拉伸（Clock Stretching）。I²C 控制器支持两个 32 字节 FIFO：FIFO1 支持 I²C 0，FIFO2 支持其他端口。IT51XXX 的 I²C FIFO 模式支持的 I²C API 包括 `i2c_write()`、`i2c_read()` 和 `i2c_burst_read`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_ITE_IT51XXX && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.it51xxx:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.it51xxx#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → ITE IT51XXX I²C 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_ITE_IT51XXX`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_ITE_IT51XXX)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_IT51XXX_MAX_SHARE_FIFO_SIZE"></a>

## 105.57 `CONFIG_I2C_IT51XXX_MAX_SHARE_FIFO_SIZE`

**提示（Prompt）**：允许配置的共享 FIFO 大小上限为 256 字节。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_TARGET && CONFIG_I2C_ITE_IT51XXX && CONFIG_I2C
```

**默认值（Defaults）**

```text
256
```

**取值范围（Ranges）**

```text
[16, 256]
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.it51xxx:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.it51xxx#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → ITE IT51XXX I²C 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_TARGET`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TARGET)、[`CONFIG_I2C_ITE_IT51XXX`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_ITE_IT51XXX)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_IT8XXX2_CQ_MODE"></a>

## 105.58 `CONFIG_I2C_IT8XXX2_CQ_MODE`

**提示（Prompt）**：IT8XXX2 I²C 命令队列（Command Queue）模式

**说明（Help）**

此选项启用命令队列模式，可缩短字节之间的时间，从而改善 I²C 事务期间的总线时钟拉伸（Clock Stretching）。it8xxx2 的 I²C 命令队列模式支持的 I²C API 包括 `i2c_write()`、`i2c_read()` 和 `i2c_burst_read`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_ITE_ENHANCE && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SOC_IT8XXX2_CPU_IDLE_GATING
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.it8xxx2:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.it8xxx2#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → ITE IT8XXX2 增强型（Enhance）I²C 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_ITE_ENHANCE`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_ITE_ENHANCE)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SOC_IT8XXX2_CPU_IDLE_GATING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT8XXX2_CPU_IDLE_GATING)。

<a id="CONFIG_I2C_IT8XXX2_FIFO_MODE"></a>

## 105.59 `CONFIG_I2C_IT8XXX2_FIFO_MODE`

**提示（Prompt）**：IT8XXX2 I²C FIFO 模式

**说明（Help）**

此选项启用先入先出队列（FIFO）模式，可缩短字节之间的时间，从而改善 I²C 事务期间的总线时钟拉伸（Clock Stretching）。I²C 控制器支持两个 32 字节 FIFO：FIFO1 支持通道 A，FIFO2 支持通道 B。it8xxx2 的 I²C FIFO 模式支持的 I²C API 包括 `i2c_write()`、`i2c_read()` 和 `i2c_burst_read`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_ITE_IT8XXX2 && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.it8xxx2:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.it8xxx2#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → ITE IT8XXX2 I²C 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_ITE_IT8XXX2`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_ITE_IT8XXX2)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_ITE_ENHANCE"></a>

## 105.60 `CONFIG_I2C_ITE_ENHANCE`

**提示（Prompt）**：ITE IT8XXX2 增强型（Enhance）I²C 驱动

**说明（Help）**

此选项可启用 IT8XXX2 的增强型（Enhance）I²C，支持三个通道。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_ENHANCE_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_I2C_BITBANG
CONFIG_I2C_TRANSFER_TIMEOUT_SUPPORTED
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.it8xxx2:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.it8xxx2#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_I2C_BITBANG`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_BITBANG)、[`CONFIG_I2C_TRANSFER_TIMEOUT_SUPPORTED`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TRANSFER_TIMEOUT_SUPPORTED)。

<a id="CONFIG_I2C_ITE_IT51XXX"></a>

## 105.61 `CONFIG_I2C_ITE_IT51XXX`

**提示（Prompt）**：ITE IT51XXX I²C 驱动

**说明（Help）**

启用 IT51XXX 系列的 I²C 支持。支持九个主机（Host）和三个目标设备（Target），每个都可设置在 I²C 接口 0～8 上。三个 I²C 目标设备位于设计 A、B 和 C 上。支持用于读写的 16 字节专用 FIFO 模式。支持速度为 50 kHz、100 kHz、400 kHz 和 1 MHz。此驱动支持重复起始条件（Repeated Start）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT51XXX_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_I2C_BITBANG
CONFIG_I2C_TRANSFER_TIMEOUT_SUPPORTED
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.it51xxx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.it51xxx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_I2C_BITBANG`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_BITBANG)、[`CONFIG_I2C_TRANSFER_TIMEOUT_SUPPORTED`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TRANSFER_TIMEOUT_SUPPORTED)。

<a id="CONFIG_I2C_ITE_IT8XXX2"></a>

## 105.62 `CONFIG_I2C_ITE_IT8XXX2`

**提示（Prompt）**：ITE IT8XXX2 I²C 驱动

**说明（Help）**

启用 it8xxx2_evb 的 I²C 支持。支持速度为 100 kHz、400 kHz 和 1 MHz。此驱动支持重复起始条件（Repeated Start）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT8XXX2_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_I2C_BITBANG
CONFIG_I2C_TRANSFER_TIMEOUT_SUPPORTED
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.it8xxx2:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.it8xxx2#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_I2C_BITBANG`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_BITBANG)、[`CONFIG_I2C_TRANSFER_TIMEOUT_SUPPORTED`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TRANSFER_TIMEOUT_SUPPORTED)。

<a id="CONFIG_I2C_LITEX"></a>

## 105.63 `CONFIG_I2C_LITEX`

**提示（Prompt）**：LiteX I²C 驱动

**说明（Help）**

启用 LiteX I²C 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LITEX_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C_BITBANG
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.litex:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.litex#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_BITBANG`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_BITBANG)。

<a id="CONFIG_I2C_LITEX_LITEI2C"></a>

## 105.64 `CONFIG_I2C_LITEX_LITEI2C`

**提示（Prompt）**：LiteX LiteI2C I²C 驱动

**说明（Help）**

启用 LiteX I²C 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LITEX_LITEI2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.litex:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.litex#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_LPC11U6X"></a>

## 105.65 `CONFIG_I2C_LPC11U6X`

**提示（Prompt）**：LPC11U6X I²C 驱动

**说明（Help）**

启用 LPC11U6X 系统级芯片（SoC）的 I²C 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPC11U6X_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.lpc11u6x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.lpc11u6x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_MAX32"></a>

## 105.66 `CONFIG_I2C_MAX32`

**提示（Prompt）**：Analog Devices MAX32 I²C 驱动

**说明（Help）**

MAX32 系列的 I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX32_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.max32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.max32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_MAX32_DMA"></a>

## 105.67 `CONFIG_I2C_MAX32_DMA`

**提示（Prompt）**：MAX32 MCU I²C 驱动的 DMA 支持

**说明（Help）**

将直接存储器访问（DMA）用于 MAX32 MCU 的 I²C 控制器模式传输。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_MAX32_INTERRUPT && CONFIG_I2C_MAX32 && CONFIG_I2C
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.max32:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.max32#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → Analog Devices MAX32 I²C 驱动 → MAX32 I²C 驱动的中断（Interrupt）支持

**配置项引用（Symbol References）**：[`CONFIG_I2C_MAX32_INTERRUPT`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_MAX32_INTERRUPT)、[`CONFIG_I2C_MAX32`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_MAX32)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_I2C_MAX32_INTERRUPT"></a>

## 105.68 `CONFIG_I2C_MAX32_INTERRUPT`

**提示（Prompt）**：MAX32 I²C 驱动的中断（Interrupt）支持

**说明（Help）**

启用 MAX32 I²C 控制器模式传输的中断支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_MAX32 && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.max32:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.max32#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → Analog Devices MAX32 I²C 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_MAX32`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_MAX32)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_MCHP_DMA_DRIVEN"></a>

## 105.69 `CONFIG_I2C_MCHP_DMA_DRIVEN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 I²C 外设的 DMA 驱动传输。需要 DMA 控制器以及设备树中的 `dmas` 属性。可在阻塞（Blocking）和非阻塞（Non-blocking）模式下使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.mchp:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.mchp#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

<a id="CONFIG_I2C_MCHP_MSS"></a>

## 105.70 `CONFIG_I2C_MCHP_MSS`

**提示（Prompt）**：Microchip PolarFire SoC I²C 驱动

**说明（Help）**

启用 PolarFire SoC Icicle Kit I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_MPFS_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.mchp_mss:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.mchp_mss#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_MCHP_SERCOM"></a>

## 105.71 `CONFIG_I2C_MCHP_SERCOM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Microchip I²C SERCOM 驱动的通用选项（Common Options）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C
```

**被选择（Selected by）**

```text
CONFIG_I2C_MCHP_SERCOM_G1
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.mchp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.mchp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_MCHP_SERCOM_G1`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_MCHP_SERCOM_G1)。

<a id="CONFIG_I2C_MCHP_SERCOM_G1"></a>

## 105.72 `CONFIG_I2C_MCHP_SERCOM_G1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip SERCOM I²C g1 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_SERCOM_G1_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_I2C_MCHP_SERCOM
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.mchp:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.mchp#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_I2C_MCHP_SERCOM`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_MCHP_SERCOM)。

<a id="CONFIG_I2C_MCHP_TARGET_BUFF_SIZE"></a>

## 105.73 `CONFIG_I2C_MCHP_TARGET_BUFF_SIZE`

**提示（Prompt）**：Microchip I²C 目标设备缓冲区大小（Buffer Size）

**说明（Help）**

Microchip I²C 驱动在目标设备（Target）模式下使用的 I²C 目标设备缓冲区大小，单位为字节。如果预期 I²C 控制器会进行较大的读写传输，可增大此值；减小此值可节省内存。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_TARGET_BUFFER_MODE && CONFIG_I2C_MCHP_SERCOM && CONFIG_I2C
```

**默认值（Defaults）**

```text
64
```

**取值范围（Ranges）**

```text
[1, 512]
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.mchp:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.mchp#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_TARGET_BUFFER_MODE`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TARGET_BUFFER_MODE)、[`CONFIG_I2C_MCHP_SERCOM`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_MCHP_SERCOM)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_MCHP_TRANSFER_TIMEOUT"></a>

## 105.74 `CONFIG_I2C_MCHP_TRANSFER_TIMEOUT`

**提示（Prompt）**：Microchip 传输超时（Transfer Timeout，毫秒）

**说明（Help）**

每次 I²C 传输的超时时间，单位为毫秒。0 表示驱动应使用 `K_FOREVER`，即一直等待，直到操作能够完成。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_MCHP_SERCOM && CONFIG_I2C
```

**默认值（Defaults）**

```text
500
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.mchp:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.mchp#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_MCHP_SERCOM`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_MCHP_SERCOM)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_MCUX"></a>

## 105.75 `CONFIG_I2C_MCUX`

**提示（Prompt）**：MCUX I²C 驱动

**说明（Help）**

启用 MCUX I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_KINETIS_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig:243`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig#L243)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_MCUX_FLEXCOMM"></a>

## 105.76 `CONFIG_I2C_MCUX_FLEXCOMM`

**提示（Prompt）**：MCUX FLEXCOMM I²C 驱动

**说明（Help）**

启用 MCUX FLEXCOMM I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPC_I2C_ENABLED && CONFIG_I2C
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

**定义位置（Location）**：[`drivers/i2c/Kconfig.mcux:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.mcux#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_RESET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RESET)。

<a id="CONFIG_I2C_MCUX_FLEXCOMM_BUS_RECOVERY"></a>

## 105.77 `CONFIG_I2C_MCUX_FLEXCOMM_BUS_RECOVERY`

**提示（Prompt）**：总线恢复（Bus Recovery）支持

**说明（Help）**

启用 FLEXCOMM I²C 驱动通过 GPIO 位操作模拟（Bit Banging）实现的总线恢复支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_MCUX_FLEXCOMM && CONFIG_PINCTRL && CONFIG_I2C
```

**默认值（Defaults）**

```text
y if CONFIG_I2C_BUS_RECOVERY
y if n
```

**主动选择（Selects）**

```text
CONFIG_I2C_BITBANG
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.mcux:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.mcux#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → MCUX FLEXCOMM I²C 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_MCUX_FLEXCOMM`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_MCUX_FLEXCOMM)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_BUS_RECOVERY`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_BUS_RECOVERY)、[`CONFIG_I2C_BITBANG`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_BITBANG)。

<a id="CONFIG_I2C_MCUX_LPI2C"></a>

## 105.78 `CONFIG_I2C_MCUX_LPI2C`

**提示（Prompt）**：MCUX LPI2C 驱动

**说明（Help）**

启用 MCUX LPI2C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPI2C_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig:251`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig#L251)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_MCUX_LPI2C_BUS_RECOVERY"></a>

## 105.79 `CONFIG_I2C_MCUX_LPI2C_BUS_RECOVERY`

**提示（Prompt）**：总线恢复（Bus Recovery）支持

**说明（Help）**

启用 LPI2C 驱动通过 GPIO 位操作模拟（Bit Banging）实现的总线恢复支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_MCUX_LPI2C && CONFIG_PINCTRL && CONFIG_I2C
```

**默认值（Defaults）**

```text
y if CONFIG_I2C_BUS_RECOVERY
y if n
```

**主动选择（Selects）**

```text
CONFIG_I2C_BITBANG
```

**定义位置（Location）**：[`drivers/i2c/Kconfig:260`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig#L260)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → MCUX LPI2C 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_MCUX_LPI2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_MCUX_LPI2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_BUS_RECOVERY`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_BUS_RECOVERY)、[`CONFIG_I2C_BITBANG`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_BITBANG)。

<a id="CONFIG_I2C_NIOS2"></a>

## 105.80 `CONFIG_I2C_NIOS2`

**提示（Prompt）**：Nios-II I²C 驱动

**说明（Help）**

启用 Nios-II I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ALTR_NIOS2_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2c/Kconfig:290`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig#L290)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_NPCX"></a>

## 105.81 `CONFIG_I2C_NPCX`

**提示（Prompt）**：Nuvoton NPCX 嵌入式控制器（Embedded Controller，EC）I²C 驱动

**说明（Help）**

此选项启用 NPCX 系列处理器的 I²C 驱动。如需使用 NPCX MCU 上的 I²C 模块，请选 y。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NPCX_I2C_PORT_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_I2C_TRANSFER_TIMEOUT_SUPPORTED
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.npcx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.npcx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_I2C_TRANSFER_TIMEOUT_SUPPORTED`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TRANSFER_TIMEOUT_SUPPORTED)。

<a id="CONFIG_I2C_NPCX_DMA_DRIVEN"></a>

## 105.82 `CONFIG_I2C_NPCX_DMA_DRIVEN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

对于支持 DMA 模式的 I²C 外设，应通过 DMA 驱动的事务（Transaction）执行数据传输。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.npcx:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.npcx#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

<a id="CONFIG_I2C_NPCX_FIFO_DRIVEN"></a>

## 105.83 `CONFIG_I2C_NPCX_FIFO_DRIVEN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

对于支持 FIFO 模式的 I²C 外设，应通过 FIFO 驱动的事务（Transaction）执行数据传输。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.npcx:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.npcx#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

<a id="CONFIG_I2C_NPCX_INVALID_STOP_WORKAROUND"></a>

## 105.84 `CONFIG_I2C_NPCX_INVALID_STOP_WORKAROUND`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

针对 NPCXn 变体 I²C 控制器中无效停止条件（STOP Condition）问题的规避措施。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NPCX_SOC_VARIANT_NPCXN && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.npcx:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.npcx#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_NPCX_SOC_VARIANT_NPCXN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NPCX_SOC_VARIANT_NPCXN)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NPCX_SOC_VARIANT_NPCXN`。

<a id="CONFIG_I2C_NPCX_PORT_INIT_PRIORITY"></a>

## 105.85 `CONFIG_I2C_NPCX_PORT_INIT_PRIORITY`

**提示（Prompt）**：NPCX I²C 端口初始化优先级（Initialization Priority）

**说明（Help）**

NPCX 设备上 I²C 端口的初始化优先级，必须设为比控制器（`I2C_INIT_PRIORITY`）更低的优先级（Lower Priority）。译注：此处指初始化次序更靠后；本快照端口默认值为 51，控制器沿用设备初始化优先级默认值 50，不应把 lower 直接理解为数值更小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_NPCX && CONFIG_I2C
```

**默认值（Defaults）**

```text
51
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.npcx:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.npcx#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → Nuvoton NPCX 嵌入式控制器（Embedded Controller，EC）I²C 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_NPCX`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_NPCX)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_NRFX"></a>

## 105.86 `CONFIG_I2C_NRFX`

**提示（Prompt）**：nRF TWI nrfx 驱动

**说明（Help）**

启用 nRF MCU 系列的 nrfx 双线接口（TWI）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_NORDIC_NRF && CONFIG_MULTITHREADING && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_I2C_TRANSFER_TIMEOUT_SUPPORTED
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.nrfx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.nrfx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_I2C_TRANSFER_TIMEOUT_SUPPORTED`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TRANSFER_TIMEOUT_SUPPORTED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_I2C_NRFX_TWIS_BUF_SIZE"></a>

## 105.87 `CONFIG_I2C_NRFX_TWIS_BUF_SIZE`

**提示（Prompt）**：DMA 缓冲区大小，单位为字节

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_NRFX_TWIS && CONFIG_I2C_NRFX && CONFIG_I2C
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.nrfx:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.nrfx#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → nRF TWI nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_NRFX_TWIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_NRFX_TWIS)、[`CONFIG_I2C_NRFX`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_NRFX)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_I2C_NRFX_TWIS`。

<a id="CONFIG_I2C_NUMAKER"></a>

## 105.88 `CONFIG_I2C_NUMAKER`

**提示（Prompt）**：Nuvoton NuMaker I²C 驱动

**说明（Help）**

此选项启用 Nuvoton NuMaker 系列处理器的 I²C 驱动。如需启用 NuMaker I²C，请选 y。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NUMAKER_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_NUMAKER_I2C
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.numaker:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.numaker#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_HAS_NUMAKER_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NUMAKER_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_NXP_II2C"></a>

## 105.89 `CONFIG_I2C_NXP_II2C`

**提示（Prompt）**：NXP i.MX8M 串行 I²C 驱动

**说明（Help）**

启用 NXP II2C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_II2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2c/Kconfig:313`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig#L313)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_NXP_TRANSFER_TIMEOUT"></a>

## 105.90 `CONFIG_I2C_NXP_TRANSFER_TIMEOUT`

**提示（Prompt）**：传输超时（Transfer Timeout，毫秒）

**说明（Help）**

每次 I²C 传输的超时时间，单位为毫秒。0 表示驱动应使用 `K_FOREVER`，即一直等待，直到操作能够完成。同时必须启用 `FSL_FEATURE_I2C_TIMEOUT_RECOVERY`，使驱动能够完全恢复。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_MCUX_FLEXCOMM && CONFIG_I2C
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.mcux:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.mcux#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → MCUX FLEXCOMM I²C 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_MCUX_FLEXCOMM`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_MCUX_FLEXCOMM)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_OMAP"></a>

## 105.91 `CONFIG_I2C_OMAP`

**提示（Prompt）**：TI OMAP I²C 驱动

**说明（Help）**

启用 TI OMAP 系统级芯片（SoC）的 I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_OMAP_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.omap:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.omap#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_OMAP_BUS_RECOVERY"></a>

## 105.92 `CONFIG_I2C_OMAP_BUS_RECOVERY`

**提示（Prompt）**：总线恢复（Bus Recovery）支持

**说明（Help）**

启用 OMAP I²C 驱动通过位操作模拟（Bit Banging）实现的总线恢复支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_OMAP && CONFIG_I2C
```

**默认值（Defaults）**

```text
y if CONFIG_I2C_BUS_RECOVERY
```

**主动选择（Selects）**

```text
CONFIG_I2C_BITBANG
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.omap:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.omap#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → TI OMAP I²C 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_OMAP`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_OMAP)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_BUS_RECOVERY`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_BUS_RECOVERY)、[`CONFIG_I2C_BITBANG`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_BITBANG)。

<a id="CONFIG_I2C_RCAR"></a>

## 105.93 `CONFIG_I2C_RCAR`

**提示（Prompt）**：Renesas R-Car I²C 驱动

**说明（Help）**

启用 Renesas R-Car I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RCAR_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.rcar:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.rcar#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_RENESAS_RA_IIC"></a>

## 105.94 `CONFIG_I2C_RENESAS_RA_IIC`

**提示（Prompt）**：Renesas RA I²C IIC 驱动

**说明（Help）**

启用 Renesas RA I²C IIC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_IIC_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_I2C_IIC_CONTROLLER
CONFIG_USE_RA_FSP_I2C_IIC_TARGET if CONFIG_I2C_TARGET
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.renesas_ra:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.renesas_ra#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_USE_RA_FSP_I2C_IIC_CONTROLLER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_I2C_IIC_CONTROLLER)、[`CONFIG_USE_RA_FSP_I2C_IIC_TARGET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_I2C_IIC_TARGET)、[`CONFIG_I2C_TARGET`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TARGET)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_RENESAS_RA_IIC_BUS_RECOVERY"></a>

## 105.95 `CONFIG_I2C_RENESAS_RA_IIC_BUS_RECOVERY`

**提示（Prompt）**：总线恢复（Bus Recovery）支持

**说明（Help）**

启用 Renesas RA I²C IIC 驱动通过 GPIO 位操作模拟（Bit Banging）实现的总线恢复支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_RENESAS_RA_IIC && CONFIG_I2C
```

**主动选择（Selects）**

```text
CONFIG_I2C_BITBANG
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.renesas_ra:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.renesas_ra#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → Renesas RA I²C IIC 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_RENESAS_RA_IIC`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_RENESAS_RA_IIC)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_BITBANG`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_BITBANG)。

<a id="CONFIG_I2C_RENESAS_RA_SCI"></a>

## 105.96 `CONFIG_I2C_RENESAS_RA_SCI`

**提示（Prompt）**：Renesas RA SCI I²C

**说明（Help）**

启用 Renesas RA SCI I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_I2C_SCI_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_SCI_I2C
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.renesas_ra:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.renesas_ra#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_USE_RA_FSP_SCI_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_SCI_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_RENESAS_RA_SCI_B"></a>

## 105.97 `CONFIG_I2C_RENESAS_RA_SCI_B`

**提示（Prompt）**：Renesas RA SCI-B I²C

**说明（Help）**

启用 Renesas RA SCI-B I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_I2C_SCI_B_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_SCI_B_I2C
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.renesas_ra:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.renesas_ra#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_USE_RA_FSP_SCI_B_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_SCI_B_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_RENESAS_RA_SCI_B_DMAC"></a>

## 105.98 `CONFIG_I2C_RENESAS_RA_SCI_B_DMAC`

**提示（Prompt）**：RA MCU SCI-B I²C DMAC 支持

**说明（Help）**

为 RA 系列 SCI-B I²C 驱动启用直接存储器访问控制器（Direct Memory Access Controller，DMAC）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_RENESAS_RA_SCI_B && CONFIG_I2C
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_DMA
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.renesas_ra:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.renesas_ra#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → Renesas RA SCI-B I²C

**配置项引用（Symbol References）**：[`CONFIG_I2C_RENESAS_RA_SCI_B`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_RENESAS_RA_SCI_B)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_USE_RA_FSP_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_DMA)。

<a id="CONFIG_I2C_RENESAS_RA_SCI_B_DTC"></a>

## 105.99 `CONFIG_I2C_RENESAS_RA_SCI_B_DTC`

**提示（Prompt）**：发送和接收使用 DTC

**说明（Help）**

在发送（Transmission）和接收（Reception）时启用 DTC。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_RENESAS_RA_SCI_B && CONFIG_I2C
```

**默认值（Defaults）**

```text
n || n
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_DTC
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.renesas_ra:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.renesas_ra#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → Renesas RA SCI-B I²C

**配置项引用（Symbol References）**：[`CONFIG_I2C_RENESAS_RA_SCI_B`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_RENESAS_RA_SCI_B)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_USE_RA_FSP_DTC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_DTC)。

<a id="CONFIG_I2C_RENESAS_RA_SCI_DTC"></a>

## 105.100 `CONFIG_I2C_RENESAS_RA_SCI_DTC`

**提示（Prompt）**：发送和接收使用 DTC

**说明（Help）**

在发送（Transmission）和接收（Reception）时启用 DTC。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_RENESAS_RA_SCI && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_DTC
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.renesas_ra:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.renesas_ra#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → Renesas RA SCI I²C

**配置项引用（Symbol References）**：[`CONFIG_I2C_RENESAS_RA_SCI`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_RENESAS_RA_SCI)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_USE_RA_FSP_DTC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_DTC)。

<!-- kconfig-navigation -->

[上一章](P104_drivers_hwspinlock_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P106_drivers_i2c_配置项参考_2.md)
