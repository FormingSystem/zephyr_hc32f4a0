---
id: learning.zephyr-docs.kconfig-reference.page-120
title: "`drivers/mfd`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第120章\_`drivers/mfd`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/mfd` 的 70 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ADP5360_THREAD_PRIORITY"></a>

## 120.1 `CONFIG_ADP5360_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

设置使用专用线程处理中断时，该线程的优先级。原文说明“数值越大，优先级越高”（A higher value indicates a higher priority）。译注：此处保留该配置项的原文表述，不应据此推导其他驱动或线程优先级的数值方向。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADP5360_TRIGGER_OWN_THREAD && CONFIG_MFD_ADP5360 && CONFIG_MFD
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.adp5360:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.adp5360#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → 带降压和升降压功能的 ADP5360 电池管理 PMIC（Buck and Buck Boost）

**配置项引用（Symbol References）**：[`CONFIG_ADP5360_TRIGGER_OWN_THREAD`](P120_drivers_mfd_配置项参考.md#CONFIG_ADP5360_TRIGGER_OWN_THREAD)、[`CONFIG_MFD_ADP5360`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_ADP5360)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_ADP5360_THREAD_STACK_SIZE"></a>

## 120.2 `CONFIG_ADP5360_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小（Thread Stack Size）

**说明（Help）**

选择“使用专用线程”（Use Own Thread）时，指定处理中断所用线程的栈大小，单位为字节。应确保栈足以容纳中断处理逻辑，避免栈溢出（Stack Overflow）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADP5360_TRIGGER_OWN_THREAD && CONFIG_MFD_ADP5360 && CONFIG_MFD
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.adp5360:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.adp5360#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → 带降压和升降压功能的 ADP5360 电池管理 PMIC（Buck and Buck Boost）

**配置项引用（Symbol References）**：[`CONFIG_ADP5360_TRIGGER_OWN_THREAD`](P120_drivers_mfd_配置项参考.md#CONFIG_ADP5360_TRIGGER_OWN_THREAD)、[`CONFIG_MFD_ADP5360`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_ADP5360)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_ADP5360_TRIGGER_GLOBAL_THREAD"></a>

## 120.3 `CONFIG_ADP5360_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**

使用全局线程（Global Thread）处理中断

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_ADP5360_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_MFD_ADP5360_TRIGGER
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.adp5360:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.adp5360#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → 带降压和升降压功能的 ADP5360 电池管理 PMIC（Buck and Buck Boost） → 设置中断处理选项（Interrupt Handling）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_ADP5360_TRIGGER_MODE`](P120_drivers_mfd_配置项参考.md#CONFIG_ADP5360_TRIGGER_MODE)、[`CONFIG_MFD_ADP5360_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD_ADP5360_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MFD_ADP5360_TRIGGER`。

<a id="CONFIG_ADP5360_TRIGGER_MODE"></a>

## 120.4 `CONFIG_ADP5360_TRIGGER_MODE`

**提示（Prompt）**：设置中断处理选项（Interrupt Handling）

**说明（Help）**

选择 ADP5360 MFD 驱动实现中断处理的方式，可根据应用需求选择不同的中断处理机制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MFD_ADP5360 && CONFIG_MFD
```

**默认值（Defaults）**

```text
CONFIG_ADP5360_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_ADP5360_TRIGGER_NONE
CONFIG_ADP5360_TRIGGER_GLOBAL_THREAD
CONFIG_ADP5360_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.adp5360:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.adp5360#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → 带降压和升降压功能的 ADP5360 电池管理 PMIC（Buck and Buck Boost）

**配置项引用（Symbol References）**：[`CONFIG_MFD_ADP5360`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_ADP5360)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_ADP5360_TRIGGER_NONE`](P120_drivers_mfd_配置项参考.md#CONFIG_ADP5360_TRIGGER_NONE)、[`CONFIG_ADP5360_TRIGGER_GLOBAL_THREAD`](P120_drivers_mfd_配置项参考.md#CONFIG_ADP5360_TRIGGER_GLOBAL_THREAD)、[`CONFIG_ADP5360_TRIGGER_OWN_THREAD`](P120_drivers_mfd_配置项参考.md#CONFIG_ADP5360_TRIGGER_OWN_THREAD)。

<a id="CONFIG_ADP5360_TRIGGER_NONE"></a>

## 120.5 `CONFIG_ADP5360_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ADP5360_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.adp5360:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.adp5360#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → 带降压和升降压功能的 ADP5360 电池管理 PMIC（Buck and Buck Boost） → 设置中断处理选项（Interrupt Handling）

**配置项引用（Symbol References）**：[`CONFIG_ADP5360_TRIGGER_MODE`](P120_drivers_mfd_配置项参考.md#CONFIG_ADP5360_TRIGGER_MODE)。

<a id="CONFIG_ADP5360_TRIGGER_OWN_THREAD"></a>

## 120.6 `CONFIG_ADP5360_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**

使用专用线程（Own Thread）处理中断

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_ADP5360_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_MFD_ADP5360_TRIGGER
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.adp5360:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.adp5360#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → 带降压和升降压功能的 ADP5360 电池管理 PMIC（Buck and Buck Boost） → 设置中断处理选项（Interrupt Handling）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_ADP5360_TRIGGER_MODE`](P120_drivers_mfd_配置项参考.md#CONFIG_ADP5360_TRIGGER_MODE)、[`CONFIG_MFD_ADP5360_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD_ADP5360_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MFD_ADP5360_TRIGGER`。

<a id="CONFIG_MFD"></a>

## 120.7 `CONFIG_MFD`

**提示（Prompt）**：多功能设备（Multi-function Device，MFD）驱动

**说明（Help）**

纳入多功能设备（Multi-function Device，MFD）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SHIELD_ADI_LSMSPG
CONFIG_ADC_AD559X
CONFIG_ADC_INFINEON_AUTANALOG_SAR
CONFIG_ADC_INFINEON_HPPASS_SAR
CONFIG_ADC_M5PM1
CONFIG_ADC_TLA2528
CONFIG_BBRAM_MOTOROLA_MC146818
CONFIG_CHARGER_ADP5360
CONFIG_CHARGER_AXP2101
CONFIG_CHARGER_MAX20335
CONFIG_CHARGER_PCA9422
CONFIG_CHARGER_PF1550
CONFIG_COMPARATOR_INFINEON_AUTANALOG_PTCOMP
CONFIG_COUNTER_CMOS
CONFIG_COUNTER_RV3028
CONFIG_COUNTER_RV3032
CONFIG_CRYPTO_INFINEON_MXCRYPTO
CONFIG_CRYPTO_INFINEON_MXCRYPTOLITE
CONFIG_DAC_AD559X
CONFIG_DAC_INFINEON_AUTANALOG
CONFIG_DAC_INFINEON_HPPASS_CSG
CONFIG_DAC_MAX22017
CONFIG_EEPROM_RV3028
CONFIG_ENTROPY_INFINEON_MXCRYPTO_TRNG
CONFIG_ENTROPY_INFINEON_MXCRYPTOLITE_TRNG
CONFIG_ENTROPY_MAXQ10XX_RNG
CONFIG_FUEL_GAUGE_ADP5360
CONFIG_FUEL_GAUGE_AXP2101
CONFIG_GPIO_AD559X
CONFIG_GPIO_ADP5585
CONFIG_GPIO_AW9523B
CONFIG_GPIO_AXP192
CONFIG_GPIO_BD8LB600FS
CONFIG_GPIO_ITE_IT8801
CONFIG_GPIO_M5PM1
CONFIG_GPIO_MAX22017
CONFIG_GPIO_NCT38XX
CONFIG_GPIO_NPM10XX
CONFIG_GPIO_NPM13XX
CONFIG_GPIO_NPM2100
CONFIG_GPIO_NPM6001
CONFIG_GPIO_SC18IS606
CONFIG_GPIO_TLA2528
CONFIG_GPIO_TLE9104
CONFIG_INPUT_ITE_IT8801_KBD
CONFIG_LED_AW9523B
CONFIG_LED_AXP192_AXP2101
CONFIG_LED_NPM10XX
CONFIG_LED_NPM13XX
CONFIG_MISC_MAX2221X
CONFIG_OPAMP_INFINEON_AUTANALOG_CTB
CONFIG_PWM_ITE_IT8801
CONFIG_PWM_MAX31790
CONFIG_REGULATOR_ADP5360
CONFIG_REGULATOR_AXP192_AXP2101
CONFIG_REGULATOR_INFINEON_AUTANALOG_PRB
CONFIG_REGULATOR_M5PM1
CONFIG_REGULATOR_MAX20335
CONFIG_REGULATOR_NPM10XX
CONFIG_REGULATOR_NPM13XX
CONFIG_REGULATOR_NPM2100
CONFIG_REGULATOR_NPM6001
CONFIG_REGULATOR_PCA9422
CONFIG_REGULATOR_PF1550
CONFIG_RETAINED_MEM_RV3028
CONFIG_RTC_DS3231
CONFIG_RTC_MOTOROLA_MC146818
CONFIG_RTC_RV3028
CONFIG_SENSOR_DS3231
CONFIG_MAX31790_FAN_SPEED
CONFIG_MAX31790_FAN_FAULT
CONFIG_NPM13XX_CHARGER
CONFIG_NPM2100_VBAT
CONFIG_BD8LB600FS_DIAGNOSTICS
CONFIG_USART_SAM
CONFIG_SPI_SC18IS606
CONFIG_WDT_M5PM1
CONFIG_WDT_NPM10XX
CONFIG_WDT_NPM13XX
CONFIG_WDT_NPM2100
CONFIG_WDT_NPM6001
```

**定义位置（Location）**：[`drivers/mfd/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SHIELD_ADI_LSMSPG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHIELD_ADI_LSMSPG)、[`CONFIG_ADC_AD559X`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_AD559X)、[`CONFIG_ADC_INFINEON_AUTANALOG_SAR`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_INFINEON_AUTANALOG_SAR)、[`CONFIG_ADC_INFINEON_HPPASS_SAR`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_INFINEON_HPPASS_SAR)、[`CONFIG_ADC_M5PM1`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_M5PM1)、[`CONFIG_ADC_TLA2528`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_TLA2528)、[`CONFIG_BBRAM_MOTOROLA_MC146818`](P052_drivers_bbram_配置项参考.md#CONFIG_BBRAM_MOTOROLA_MC146818)、[`CONFIG_CHARGER_ADP5360`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER_ADP5360)、[`CONFIG_CHARGER_AXP2101`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER_AXP2101)、[`CONFIG_CHARGER_MAX20335`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER_MAX20335)、[`CONFIG_CHARGER_PCA9422`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER_PCA9422)、[`CONFIG_CHARGER_PF1550`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER_PF1550)、[`CONFIG_COMPARATOR_INFINEON_AUTANALOG_PTCOMP`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR_INFINEON_AUTANALOG_PTCOMP)、[`CONFIG_COUNTER_CMOS`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_CMOS)、[`CONFIG_COUNTER_RV3028`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_RV3028)、[`CONFIG_COUNTER_RV3032`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_RV3032)、[`CONFIG_CRYPTO_INFINEON_MXCRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_INFINEON_MXCRYPTO)、[`CONFIG_CRYPTO_INFINEON_MXCRYPTOLITE`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_INFINEON_MXCRYPTOLITE)、[`CONFIG_DAC_AD559X`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_AD559X)、[`CONFIG_DAC_INFINEON_AUTANALOG`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_INFINEON_AUTANALOG)、[`CONFIG_DAC_INFINEON_HPPASS_CSG`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_INFINEON_HPPASS_CSG)、[`CONFIG_DAC_MAX22017`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_MAX22017)、[`CONFIG_EEPROM_RV3028`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM_RV3028)、[`CONFIG_ENTROPY_INFINEON_MXCRYPTO_TRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_INFINEON_MXCRYPTO_TRNG)、[`CONFIG_ENTROPY_INFINEON_MXCRYPTOLITE_TRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_INFINEON_MXCRYPTOLITE_TRNG)、[`CONFIG_ENTROPY_MAXQ10XX_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_MAXQ10XX_RNG)、[`CONFIG_FUEL_GAUGE_ADP5360`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_FUEL_GAUGE_ADP5360)、[`CONFIG_FUEL_GAUGE_AXP2101`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_FUEL_GAUGE_AXP2101)、[`CONFIG_GPIO_AD559X`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_AD559X)、[`CONFIG_GPIO_ADP5585`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_ADP5585)、[`CONFIG_GPIO_AW9523B`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_AW9523B)、[`CONFIG_GPIO_AXP192`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_AXP192)、[`CONFIG_GPIO_BD8LB600FS`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_BD8LB600FS)、[`CONFIG_GPIO_ITE_IT8801`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_ITE_IT8801)、[`CONFIG_GPIO_M5PM1`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_M5PM1)、[`CONFIG_GPIO_MAX22017`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_MAX22017)、[`CONFIG_GPIO_NCT38XX`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_NCT38XX)、[`CONFIG_GPIO_NPM10XX`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_NPM10XX)、[`CONFIG_GPIO_NPM13XX`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_NPM13XX)、[`CONFIG_GPIO_NPM2100`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_NPM2100)、[`CONFIG_GPIO_NPM6001`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_NPM6001)、[`CONFIG_GPIO_SC18IS606`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_SC18IS606)、[`CONFIG_GPIO_TLA2528`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_TLA2528)、[`CONFIG_GPIO_TLE9104`](P100_drivers_gpio_配置项参考_3.md#CONFIG_GPIO_TLE9104)、[`CONFIG_INPUT_ITE_IT8801_KBD`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_ITE_IT8801_KBD)、[`CONFIG_LED_AW9523B`](P114_drivers_led_配置项参考.md#CONFIG_LED_AW9523B)、[`CONFIG_LED_AXP192_AXP2101`](P114_drivers_led_配置项参考.md#CONFIG_LED_AXP192_AXP2101)、[`CONFIG_LED_NPM10XX`](P114_drivers_led_配置项参考.md#CONFIG_LED_NPM10XX)、[`CONFIG_LED_NPM13XX`](P114_drivers_led_配置项参考.md#CONFIG_LED_NPM13XX)、[`CONFIG_MISC_MAX2221X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MISC_MAX2221X)、[`CONFIG_OPAMP_INFINEON_AUTANALOG_CTB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPAMP_INFINEON_AUTANALOG_CTB)、[`CONFIG_PWM_ITE_IT8801`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PWM_ITE_IT8801)、[`CONFIG_PWM_MAX31790`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PWM_MAX31790)、[`CONFIG_REGULATOR_ADP5360`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REGULATOR_ADP5360)、[`CONFIG_REGULATOR_AXP192_AXP2101`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REGULATOR_AXP192_AXP2101)、[`CONFIG_REGULATOR_INFINEON_AUTANALOG_PRB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REGULATOR_INFINEON_AUTANALOG_PRB)、[`CONFIG_REGULATOR_M5PM1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REGULATOR_M5PM1)、[`CONFIG_REGULATOR_MAX20335`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REGULATOR_MAX20335)、[`CONFIG_REGULATOR_NPM10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REGULATOR_NPM10XX)、[`CONFIG_REGULATOR_NPM13XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REGULATOR_NPM13XX)、[`CONFIG_REGULATOR_NPM2100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REGULATOR_NPM2100)、[`CONFIG_REGULATOR_NPM6001`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REGULATOR_NPM6001)、[`CONFIG_REGULATOR_PCA9422`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REGULATOR_PCA9422)、[`CONFIG_REGULATOR_PF1550`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REGULATOR_PF1550)、[`CONFIG_RETAINED_MEM_RV3028`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RETAINED_MEM_RV3028)、[`CONFIG_RTC_DS3231`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTC_DS3231)、[`CONFIG_RTC_MOTOROLA_MC146818`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTC_MOTOROLA_MC146818)、[`CONFIG_RTC_RV3028`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTC_RV3028)、[`CONFIG_SENSOR_DS3231`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_DS3231)、[`CONFIG_MAX31790_FAN_SPEED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MAX31790_FAN_SPEED)、[`CONFIG_MAX31790_FAN_FAULT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MAX31790_FAN_FAULT)、[`CONFIG_NPM13XX_CHARGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NPM13XX_CHARGER)、[`CONFIG_NPM2100_VBAT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NPM2100_VBAT)、[`CONFIG_BD8LB600FS_DIAGNOSTICS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BD8LB600FS_DIAGNOSTICS)、[`CONFIG_USART_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USART_SAM)、[`CONFIG_SPI_SC18IS606`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_SC18IS606)、[`CONFIG_WDT_M5PM1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WDT_M5PM1)、[`CONFIG_WDT_NPM10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WDT_NPM10XX)、[`CONFIG_WDT_NPM13XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WDT_NPM13XX)、[`CONFIG_WDT_NPM2100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WDT_NPM2100)、[`CONFIG_WDT_NPM6001`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WDT_NPM6001)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SHIELD_ADI_LSMSPG`。

<a id="CONFIG_MFD_AD559X"></a>

## 120.8 `CONFIG_MFD_AD559X`

**提示（Prompt）**：Analog AD559x I²C/SPI 可配置 ADC/DAC/GPIO 芯片

**说明（Help）**

启用 Analog AD5592 或 Analog AD5593 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_AD559X_ENABLED && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.ad559x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.ad559x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_AD559X_BUS_I2C"></a>

## 120.9 `CONFIG_MFD_AD559X_BUS_I2C`

**提示（Prompt）**：Analog AD559x I²C 总线支持

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

**定义位置（Location）**：[`drivers/mfd/Kconfig.ad559x:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.ad559x#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → Analog AD559x I²C/SPI 可配置 ADC/DAC/GPIO 芯片

<a id="CONFIG_MFD_AD559X_BUS_SPI"></a>

## 120.10 `CONFIG_MFD_AD559X_BUS_SPI`

**提示（Prompt）**：Analog AD559x SPI 总线支持

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

**定义位置（Location）**：[`drivers/mfd/Kconfig.ad559x:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.ad559x#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → Analog AD559x I²C/SPI 可配置 ADC/DAC/GPIO 芯片

<a id="CONFIG_MFD_ADP5360"></a>

## 120.11 `CONFIG_MFD_ADP5360`

**提示（Prompt）**：带降压和升降压功能的 ADP5360 电池管理 PMIC（Buck and Buck Boost）

**说明（Help）**

启用 ADI ADP5360 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_ADP5360_ENABLED && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.adp5360:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.adp5360#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MFD_ADP5360_INIT_PRIORITY"></a>

## 120.12 `CONFIG_MFD_ADP5360_INIT_PRIORITY`

**提示（Prompt）**：MFD ADP5360 初始化优先级（Initialization Priority）

**说明（Help）**

Analog Devices ADP5360 MFD 子系统的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MFD_ADP5360 && CONFIG_MFD_ADP5360 && CONFIG_MFD
```

**默认值（Defaults）**

```text
70
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.adp5360:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.adp5360#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → 带降压和升降压功能的 ADP5360 电池管理 PMIC（Buck and Buck Boost）

**配置项引用（Symbol References）**：[`CONFIG_MFD_ADP5360`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_ADP5360)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_ADP5585"></a>

## 120.13 `CONFIG_MFD_ADP5585`

**提示（Prompt）**：Analog ADP5585 I²C 可配置 GPIO/PWM/按键扫描（KeyScan）芯片

**说明（Help）**

启用 Analog ADP5585 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_ADP5585_ENABLED && CONFIG_I2C && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.adp5585:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.adp5585#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_ADP5585_INIT_PRIORITY"></a>

## 120.14 `CONFIG_MFD_ADP5585_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MFD_ADP5585 && CONFIG_MFD
```

**默认值（Defaults）**

```text
65
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.adp5585:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.adp5585#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → Analog ADP5585 I²C 可配置 GPIO/PWM/按键扫描（KeyScan）芯片

**配置项引用（Symbol References）**：[`CONFIG_MFD_ADP5585`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_ADP5585)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_AW9523B"></a>

## 120.15 `CONFIG_MFD_AW9523B`

**提示（Prompt）**：Awinic AW9523B GPIO/LED 控制器设备驱动

**说明（Help）**

启用 Awinic AW9523B GPIO/LED 控制器设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AWINIC_AW9523B_ENABLED && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.aw9523b:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.aw9523b#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MFD_AXP192"></a>

## 120.16 `CONFIG_MFD_AXP192`

**提示（Prompt）**：AXP192 PMIC 多功能设备驱动

**说明（Help）**

启用 X-Powers AXP192 电源管理芯片（PMIC）多功能设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_X_POWERS_AXP192_ENABLED && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.axp192:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.axp192#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MFD_AXP2101"></a>

## 120.17 `CONFIG_MFD_AXP2101`

**提示（Prompt）**：AXP2101 PMIC 多功能设备驱动

**说明（Help）**

启用 X-Powers AXP2101 电源管理芯片（PMIC）多功能设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_X_POWERS_AXP2101_ENABLED && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.axp2101:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.axp2101#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MFD_AXP2101_POWER_BUTTON"></a>

## 120.18 `CONFIG_MFD_AXP2101_POWER_BUTTON`

**提示（Prompt）**：AXP2101 电源按钮（Power Button）

**说明（Help）**

启用 AXP2101 电源按钮支持。此功能基于 AXP2101 的中断请求（IRQ）支持，要求在 AXP2101 设备节点中定义 `int-gpios` 设备树属性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT && CONFIG_MFD_AXP2101 && CONFIG_MFD
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.axp2101:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.axp2101#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → AXP2101 PMIC 多功能设备驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_MFD_AXP2101`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_AXP2101)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_BD8LB600FS"></a>

## 120.19 `CONFIG_MFD_BD8LB600FS`

**提示（Prompt）**：BD8LB600FS 低侧开关（Low-side Switch）多功能设备驱动

**说明（Help）**

启用 Rohm BD8LB600FS 低侧开关多功能设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ROHM_BD8LB600FS_ENABLED && CONFIG_SPI && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.bd8lb600fs:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.bd8lb600fs#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_DS3231"></a>

## 120.20 `CONFIG_MFD_DS3231`

**提示（Prompt）**：DS3231 多功能设备驱动

**说明（Help）**

启用 Maxim DS3231 多功能设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXIM_DS3231_MFD_ENABLED && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.ds3231:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.ds3231#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MFD_INFINEON_AUTANALOG"></a>

## 120.21 `CONFIG_MFD_INFINEON_AUTANALOG`

**提示（Prompt）**：Infineon AutAnalog 多功能设备驱动

**说明（Help）**

启用 Infineon AutAnalog MFD 驱动。AutAnalog 子系统包含多个模拟外设（SAR ADC、DAC、比较器），共享中断和自主控制器（Autonomous Controller，AC）状态机等公共资源。此驱动管理共享资源，并为子外设驱动提供 API。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_AUTANALOG_ENABLED && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_INFINEON_AUTANALOG_SAR_ADC
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.infineon_autanalog:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.infineon_autanalog#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_USE_INFINEON_AUTANALOG_SAR_ADC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_AUTANALOG_SAR_ADC)。

<a id="CONFIG_MFD_INFINEON_AUTANALOG_AC_START_PRIORITY"></a>

## 120.22 `CONFIG_MFD_INFINEON_AUTANALOG_AC_START_PRIORITY`

**提示（Prompt）**：Infineon AutAnalog 自主控制器（AC）启动优先级

**说明（Help）**

通过 `SYS_INIT` 启动自主控制器（Autonomous Controller，AC）的优先级。原文要求其数值高于所有子驱动的初始化优先级，即更晚执行，以确保 AC 启动前已加载子外设配置。默认值 44 按 `MFD_INFINEON_AUTANALOG_INIT_PRIORITY`（41）加 3 选择，使其在 MFD 父设备（41）及使用自定义优先级的子驱动（DAC 为 43）之后运行，但先于其他子设备（SAR ADC）使用的默认 `KERNEL_INIT_PRIORITY_DEVICE`（50）。译注：原文“晚于所有子驱动”与随后“先于 SAR ADC”的说明存在冲突，译文保留两项表述及全部数值，没有擅自统一。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MFD_INFINEON_AUTANALOG && CONFIG_MFD
```

**默认值（Defaults）**

```text
44
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.infineon_autanalog:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.infineon_autanalog#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → Infineon AutAnalog 多功能设备驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD_INFINEON_AUTANALOG`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_INFINEON_AUTANALOG)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_INFINEON_AUTANALOG_CTB"></a>

## 120.23 `CONFIG_MFD_INFINEON_AUTANALOG_CTB`

**提示（Prompt）**：Infineon AutAnalog CTB 多功能设备驱动

**说明（Help）**

启用 Infineon AutAnalog 连续时间模块（Continuous Time Block，CTB）MFD 驱动。CTB 包含两个运算放大器（Opamp），OA0 和 OA1，共用一份组合 PDL 配置。此驱动聚合两个运放，并管理共享配置结构。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_AUTANALOG_CTB_ENABLED && CONFIG_MFD_INFINEON_AUTANALOG && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.infineon_autanalog_ctb:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.infineon_autanalog_ctb#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → Infineon AutAnalog 多功能设备驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD_INFINEON_AUTANALOG`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_INFINEON_AUTANALOG)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_INFINEON_AUTANALOG_CTB_INIT_PRIORITY"></a>

## 120.24 `CONFIG_MFD_INFINEON_AUTANALOG_CTB_INIT_PRIORITY`

**提示（Prompt）**：Infineon AutAnalog CTB MFD 初始化优先级

**说明（Help）**

CTB MFD 的初始化优先级。数值必须高于 AutAnalog MFD 初始化优先级（默认 41），即更晚执行。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MFD_INFINEON_AUTANALOG_CTB && CONFIG_MFD
```

**默认值（Defaults）**

```text
42
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.infineon_autanalog_ctb:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.infineon_autanalog_ctb#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → Infineon AutAnalog 多功能设备驱动 → Infineon AutAnalog CTB 多功能设备驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD_INFINEON_AUTANALOG_CTB`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_INFINEON_AUTANALOG_CTB)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_INFINEON_AUTANALOG_INIT_PRIORITY"></a>

## 120.25 `CONFIG_MFD_INFINEON_AUTANALOG_INIT_PRIORITY`

**提示（Prompt）**：Infineon AutAnalog MFD 初始化优先级

**说明（Help）**

AutAnalog MFD 驱动的初始化优先级。数值必须低于 `CONFIG_ADC_INIT_PRIORITY` 等子驱动初始化优先级，即更早执行，以确保子设备尝试使用 MFD 父设备前，父设备已准备就绪。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MFD_INFINEON_AUTANALOG && CONFIG_MFD
```

**默认值（Defaults）**

```text
41
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.infineon_autanalog:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.infineon_autanalog#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → Infineon AutAnalog 多功能设备驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD_INFINEON_AUTANALOG`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_INFINEON_AUTANALOG)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_INFINEON_AUTANALOG_PRB"></a>

## 120.26 `CONFIG_MFD_INFINEON_AUTANALOG_PRB`

**提示（Prompt）**：Infineon AutAnalog PRB 多功能设备驱动

**说明（Help）**

启用 Infineon AutAnalog 可编程基准模块（Programmable Reference Block，PRB）MFD 驱动。PRB 包含两个电压基准（Vref0、Vref1），共用一份组合配置。此驱动聚合两个基准，并管理共享 PDL 配置结构。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_AUTANALOG_PRB_ENABLED && CONFIG_MFD_INFINEON_AUTANALOG && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.infineon_autanalog_prb:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.infineon_autanalog_prb#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → Infineon AutAnalog 多功能设备驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD_INFINEON_AUTANALOG`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_INFINEON_AUTANALOG)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_INFINEON_AUTANALOG_PRB_INIT_PRIORITY"></a>

## 120.27 `CONFIG_MFD_INFINEON_AUTANALOG_PRB_INIT_PRIORITY`

**提示（Prompt）**：Infineon AutAnalog PRB MFD 初始化优先级

**说明（Help）**

PRB MFD 的初始化优先级。数值必须高于 AutAnalog MFD 初始化优先级（默认 41），即更晚执行。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MFD_INFINEON_AUTANALOG_PRB && CONFIG_MFD
```

**默认值（Defaults）**

```text
42
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.infineon_autanalog_prb:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.infineon_autanalog_prb#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → Infineon AutAnalog 多功能设备驱动 → Infineon AutAnalog PRB 多功能设备驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD_INFINEON_AUTANALOG_PRB`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_INFINEON_AUTANALOG_PRB)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_INFINEON_AUTANALOG_PTCOMP"></a>

## 120.28 `CONFIG_MFD_INFINEON_AUTANALOG_PTCOMP`

**提示（Prompt）**：Infineon AutAnalog PTComp 多功能设备驱动

**说明（Help）**

启用 Infineon AutAnalog 可编程阈值比较器（Programmable Threshold Comparator，PTComp）MFD 驱动。PTComp 包含两个比较器（Comp0、Comp1），共用一份组合配置。此驱动聚合两个比较器，并管理共享 PDL 配置结构。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_AUTANALOG_PTCOMP_ENABLED && CONFIG_MFD_INFINEON_AUTANALOG && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.infineon_autanalog_ptcomp:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.infineon_autanalog_ptcomp#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → Infineon AutAnalog 多功能设备驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD_INFINEON_AUTANALOG`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_INFINEON_AUTANALOG)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_INFINEON_AUTANALOG_PTCOMP_INIT_PRIORITY"></a>

## 120.29 `CONFIG_MFD_INFINEON_AUTANALOG_PTCOMP_INIT_PRIORITY`

**提示（Prompt）**：Infineon AutAnalog PTComp MFD 初始化优先级

**说明（Help）**

PTComp MFD 的初始化优先级。数值必须高于 AutAnalog MFD 初始化优先级（默认 41），即更晚执行。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MFD_INFINEON_AUTANALOG_PTCOMP && CONFIG_MFD
```

**默认值（Defaults）**

```text
42
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.infineon_autanalog_ptcomp:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.infineon_autanalog_ptcomp#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → Infineon AutAnalog 多功能设备驱动 → Infineon AutAnalog PTComp 多功能设备驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD_INFINEON_AUTANALOG_PTCOMP`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_INFINEON_AUTANALOG_PTCOMP)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_INFINEON_HPPASS"></a>

## 120.30 `CONFIG_MFD_INFINEON_HPPASS`

**提示（Prompt）**：Infineon HPPASS 多功能设备驱动

**说明（Help）**

启用 Infineon HPPASS MFD 驱动。高性能可编程模拟子系统（High Performance Programmable Analog Subsystem，HPPASS）包含 SAR ADC、比较器与斜坡发生器（Comparator and Slope Generator，CSG）等模拟外设，由自主控制器（AC）状态机协调。此驱动管理 AC、触发配置和组合 MCPASS 中断等共享资源，并为子外设驱动提供 API。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_HPPASS_ANALOG_ENABLED && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_INFINEON_HPPASS_SAR_ADC
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.infineon_hppass:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.infineon_hppass#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_USE_INFINEON_HPPASS_SAR_ADC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_HPPASS_SAR_ADC)。

<a id="CONFIG_MFD_INFINEON_HPPASS_AC_START_PRIORITY"></a>

## 120.31 `CONFIG_MFD_INFINEON_HPPASS_AC_START_PRIORITY`

**提示（Prompt）**：Infineon HPPASS AC 启动优先级（APPLICATION 级别）

**说明（Help）**

一次性 AC 启动遍历（`ifx_hppass_late_start`）在 `APPLICATION` 级别的初始化优先级。它在全部 `POST_KERNEL` 设备初始化之后运行，包括 MFD 父设备和每个 HPPASS 子驱动，从而使 AC 解锁窗口能够看到子设备的 CFG 写入。`APPLICATION` 级别内，数值越小越早执行。默认值 0 使 AC 尽早启动，以便依赖 HPPASS 已运行的应用级初始化在其后执行。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MFD_INFINEON_HPPASS && CONFIG_MFD
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 99]
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.infineon_hppass:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.infineon_hppass#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → Infineon HPPASS 多功能设备驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD_INFINEON_HPPASS`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_INFINEON_HPPASS)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_INFINEON_HPPASS_CSG"></a>

## 120.32 `CONFIG_MFD_INFINEON_HPPASS_CSG`

**提示（Prompt）**：Infineon HPPASS CSG（Comparator Slope Generator，比较器斜坡发生器）MFD 驱动

**说明（Help）**

启用 Infineon HPPASS CSG MFD 驱动。CSG 模块包含五个相同的切片（Slice），每个切片将一个 10 位、30 Msps 的 DAC 与高速比较器配对。此 MFD 管理组合比较器中断，并将其分发给各切片的比较器子设备；初始化时，还应用设备树中各切片的 `CMP_CFG` / `DAC_CFG` 配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_HPPASS_CSG_ENABLED && CONFIG_MFD_INFINEON_HPPASS && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.infineon_hppass_csg:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.infineon_hppass_csg#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → Infineon HPPASS 多功能设备驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD_INFINEON_HPPASS`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_INFINEON_HPPASS)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_INFINEON_HPPASS_CSG_INIT_PRIORITY"></a>

## 120.33 `CONFIG_MFD_INFINEON_HPPASS_CSG_INIT_PRIORITY`

**提示（Prompt）**：Infineon HPPASS CSG MFD 初始化优先级

**说明（Help）**

HPPASS CSG MFD 驱动的初始化优先级。数值必须高于 `CONFIG_MFD_INFINEON_HPPASS_INIT_PRIORITY`，即更晚执行，保证运行时 HPPASS 父设备已就绪；同时必须低于各切片比较器和 DAC 子驱动的初始化优先级，即更早执行，保证任何子设备使用切片前，其 `CMP_CFG` / `DAC_CFG` 寄存器已配置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MFD_INFINEON_HPPASS_CSG && CONFIG_MFD
```

**默认值（Defaults）**

```text
45
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.infineon_hppass_csg:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.infineon_hppass_csg#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → Infineon HPPASS 多功能设备驱动 → Infineon HPPASS CSG（Comparator Slope Generator，比较器斜坡发生器）MFD 驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD_INFINEON_HPPASS_CSG`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_INFINEON_HPPASS_CSG)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_INFINEON_HPPASS_INIT_PRIORITY"></a>

## 120.34 `CONFIG_MFD_INFINEON_HPPASS_INIT_PRIORITY`

**提示（Prompt）**：Infineon HPPASS MFD 初始化优先级

**说明（Help）**

HPPASS MFD 驱动的初始化优先级。数值必须低于 `CONFIG_ADC_INIT_PRIORITY` 等子驱动初始化优先级，即更早执行，以确保子设备尝试使用 MFD 父设备前，父设备已准备就绪。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MFD_INFINEON_HPPASS && CONFIG_MFD
```

**默认值（Defaults）**

```text
41
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.infineon_hppass:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.infineon_hppass#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → Infineon HPPASS 多功能设备驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD_INFINEON_HPPASS`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_INFINEON_HPPASS)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_INFINEON_MXCRYPTO"></a>

## 120.35 `CONFIG_MFD_INFINEON_MXCRYPTO`

**提示（Prompt）**：Infineon MXCRYPTO 多功能设备驱动

**说明（Help）**

启用 Infineon MXCRYPTO MFD 驱动。MXCRYPTO 模块是一个由真随机数发生器（TRNG）和 AES / SHA 加速功能共享的硬件加密引擎。此驱动管理共享寄存器基地址，以及用于串行化 TRNG 与加密子功能驱动访问的互斥锁（Mutex），并通过 MXCRYPTO PDL 启用模块。启用任意子功能驱动时，默认启用此驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_MXCRYPTO_ENABLED && CONFIG_MFD
```

**默认值（Defaults）**

```text
y if CONFIG_ENTROPY_INFINEON_MXCRYPTO_TRNG || CONFIG_CRYPTO_INFINEON_MXCRYPTO
```

**主动选择（Selects）**

```text
CONFIG_USE_INFINEON_MXCRYPTO_CORE
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.infineon_mxcrypto:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.infineon_mxcrypto#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_ENTROPY_INFINEON_MXCRYPTO_TRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_INFINEON_MXCRYPTO_TRNG)、[`CONFIG_CRYPTO_INFINEON_MXCRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_INFINEON_MXCRYPTO)、[`CONFIG_USE_INFINEON_MXCRYPTO_CORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_MXCRYPTO_CORE)。

<a id="CONFIG_MFD_INFINEON_MXCRYPTOLITE"></a>

## 120.36 `CONFIG_MFD_INFINEON_MXCRYPTOLITE`

**提示（Prompt）**：Infineon MXCRYPTOLITE 多功能设备驱动

**说明（Help）**

启用 Infineon MXCRYPTOLITE MFD 驱动。MXCRYPTOLITE 模块是一个由真随机数发生器（TRNG）和 AES / SHA-256 加速功能共享的硬件加密引擎。此驱动管理共享寄存器基地址，以及用于串行化 TRNG 与加密子功能驱动访问的互斥锁（Mutex）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_MXCRYPTOLITE_ENABLED && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.infineon_mxcryptolite:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.infineon_mxcryptolite#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_INFINEON_MXCRYPTOLITE_INIT_PRIORITY"></a>

## 120.37 `CONFIG_MFD_INFINEON_MXCRYPTOLITE_INIT_PRIORITY`

**提示（Prompt）**：Infineon MXCRYPTOLITE MFD 初始化优先级

**说明（Help）**

MXCRYPTOLITE MFD 驱动的初始化优先级。数值必须低于子驱动的 `CONFIG_ENTROPY_INIT_PRIORITY` 和 `CONFIG_CRYPTO_INIT_PRIORITY`，即更早执行，以确保子设备使用共享资源前，资源已准备就绪。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MFD_INFINEON_MXCRYPTOLITE && CONFIG_MFD
```

**默认值（Defaults）**

```text
40
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.infineon_mxcryptolite:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.infineon_mxcryptolite#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → Infineon MXCRYPTOLITE 多功能设备驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD_INFINEON_MXCRYPTOLITE`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_INFINEON_MXCRYPTOLITE)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_INFINEON_MXCRYPTO_INIT_PRIORITY"></a>

## 120.38 `CONFIG_MFD_INFINEON_MXCRYPTO_INIT_PRIORITY`

**提示（Prompt）**：Infineon MXCRYPTO MFD 初始化优先级

**说明（Help）**

MXCRYPTO MFD 驱动的初始化优先级。数值必须低于子驱动的 `CONFIG_ENTROPY_INIT_PRIORITY` 和 `CONFIG_CRYPTO_INIT_PRIORITY`，即更早执行，以确保子设备使用共享资源前，资源已准备就绪。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MFD_INFINEON_MXCRYPTO && CONFIG_MFD
```

**默认值（Defaults）**

```text
40
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.infineon_mxcrypto:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.infineon_mxcrypto#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → Infineon MXCRYPTO 多功能设备驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD_INFINEON_MXCRYPTO`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_INFINEON_MXCRYPTO)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_INIT_PRIORITY"></a>

## 120.39 `CONFIG_MFD_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Initialization Priority）

**说明（Help）**

多功能设备（MFD）初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MFD
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/mfd/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_ITE_IT8801"></a>

## 120.40 `CONFIG_MFD_ITE_IT8801`

**提示（Prompt）**：ITE IT8801 I/O 扩展器（IO Expander）多功能设备驱动

**说明（Help）**

启用 ITE IT8801 I/O 扩展器多功能设备驱动。此扩展器通过 I²C 总线提供 GPIO、PWM 和键盘功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT8801_MFD_ENABLED && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.it8801:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.it8801#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MFD_ITE_IT8801_ALTCTRL"></a>

## 120.41 `CONFIG_MFD_ITE_IT8801_ALTCTRL`

**提示（Prompt）**：ITE IT8801 MFD 复用控制器（Alternate Controller）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MFD_ITE_IT8801 && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.it8801:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.it8801#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → ITE IT8801 I/O 扩展器（IO Expander）多功能设备驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD_ITE_IT8801`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_ITE_IT8801)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_M5PM1"></a>

## 120.42 `CONFIG_MFD_M5PM1`

**提示（Prompt）**：M5Stack M5PM1 电源管理芯片（PMIC）

**说明（Help）**

启用 M5Stack M5PM1 多功能 PMIC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_M5STACK_M5PM1_ENABLED && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.m5pm1:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.m5pm1#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MFD_MAX20335"></a>

## 120.43 `CONFIG_MFD_MAX20335`

**提示（Prompt）**：MAX20335 PMIC 多功能设备驱动

**说明（Help）**

启用 Maxim MAX20335 PMIC 多功能设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXIM_MAX20335_ENABLED && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.max20335:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.max20335#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MFD_MAX22017"></a>

## 120.44 `CONFIG_MFD_MAX22017`

**提示（Prompt）**：Analog Devices MAX22017 DAC/GPIO 芯片

**说明（Help）**

启用 Analog Devices MAX22017 DAC/GPIO 芯片的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI && DT_HAS_ADI_MAX22017_ENABLED && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CRC
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.max22017:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.max22017#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

<a id="CONFIG_MFD_MAX2221X"></a>

## 120.45 `CONFIG_MFD_MAX2221X`

**提示（Prompt）**：Analog Devices MAX2221X 多功能设备驱动

**说明（Help）**

启用 Analog Devices MAX2221X 多功能设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI && DT_HAS_ADI_MAX2221X_ENABLED && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.max2221x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.max2221x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_MAX31790"></a>

## 120.46 `CONFIG_MFD_MAX31790`

**提示（Prompt）**：Maxim Integrated MAX31790 I²C 可配置 PWM 控制器

**说明（Help）**

启用 Maxim Integrated MAX31790 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXIM_MAX31790_ENABLED && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.max31790:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.max31790#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MFD_MAXQ10XX"></a>

## 120.47 `CONFIG_MFD_MAXQ10XX`

**提示（Prompt）**：MAXQ10xx MFD 驱动

**说明（Help）**

此选项启用 MAXQ10xx 加密芯片的多功能设备（MFD）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAXQ10XX_ENABLED && CONFIG_SPI && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.maxq10xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.maxq10xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_MAXQ10XX_INIT_PRIORITY"></a>

## 120.48 `CONFIG_MFD_MAXQ10XX_INIT_PRIORITY`

**提示（Prompt）**：MAXQ10xx 初始化优先级（Initialization Priority）

**说明（Help）**

设备驱动的初始化优先级（Initialization Priority）。设备连接在 SPI 总线上，必须在 SPI 驱动之后初始化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MFD_MAXQ10XX && CONFIG_MFD
```

**默认值（Defaults）**

```text
51
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.maxq10xx:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.maxq10xx#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → MAXQ10xx MFD 驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD_MAXQ10XX`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_MAXQ10XX)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_MCHP_SAM_FLEXCOM"></a>

## 120.49 `CONFIG_MFD_MCHP_SAM_FLEXCOM`

**提示（Prompt）**：Microchip SAM FLEXCOM 接口驱动

**说明（Help）**

启用 SAM FLEXCOM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_SAM_FLEXCOM_ENABLED && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.mchp_sam:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.mchp_sam#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_MICROCRYSTAL_RV3032_INIT_PRIORITY"></a>

## 120.50 `CONFIG_MFD_MICROCRYSTAL_RV3032_INIT_PRIORITY`

**提示（Prompt）**：RV3032 MFD 初始化优先级

**说明（Help）**

Micro Crystal RV3032C7 MFD 驱动的初始化优先级。必须先于 RTC、计数器（Counter）和传感器（Sensor）驱动初始化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MFD_RV3032 && CONFIG_MFD
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.rv3032_mfd:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.rv3032_mfd#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → RV3032 的 MFD 驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD_RV3032`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_RV3032)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_MOTOROLA_MC146818"></a>

## 120.51 `CONFIG_MFD_MOTOROLA_MC146818`

**提示（Prompt）**：MOTOROLA MC146818 多功能设备驱动

**说明（Help）**

电池备份 RAM（BBRAM）与实时时钟（RTC）所需的公共代码，很可能采用锁定机制（Locking Mechanism），使 RTC 和 BBRAM 都能安全、独立地设置或读取寄存器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MOTOROLA_MC146818_MFD_ENABLED && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.mc146818:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.mc146818#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_MOTOROLA_MC146818_INIT_PRIORITY"></a>

## 120.52 `CONFIG_MFD_MOTOROLA_MC146818_INIT_PRIORITY`

**提示（Prompt）**：MC146818 MFD 初始化优先级

**说明（Help）**

MOTOROLA MC146818 MFD 驱动的初始化优先级。原文要求其大于（Greater Than）RTC、计数器（Counter）和 BBRAM 驱动的初始化优先级。译注：本快照中此 MFD 默认值为 50，RTC 和 Counter 默认沿用值为 50 的设备初始化优先级；这不满足严格大于关系，故保留原文要求与默认值之间的差异。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MFD_MOTOROLA_MC146818 && CONFIG_MFD
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.mc146818:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.mc146818#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → MOTOROLA MC146818 多功能设备驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD_MOTOROLA_MC146818`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_MOTOROLA_MC146818)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_NCT38XX"></a>

## 120.53 `CONFIG_MFD_NCT38XX`

**提示（Prompt）**：Nuvoton NCT38xx 多功能设备驱动

**说明（Help）**

启用 Nuvoton NCT38xx Type-C 端口控制器（TCPC）多功能设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NCT38XX_ENABLED && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.nct38xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.nct38xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MFD_NPM10XX"></a>

## 120.54 `CONFIG_MFD_NPM10XX`

**提示（Prompt）**：nPM10xx PMIC 多功能设备驱动

**说明（Help）**

启用 Nordic nPM10xx PMIC 多功能设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NPM10XX_ENABLED && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.npm10xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.npm10xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MFD_NPM10XX_INIT_PRIORITY"></a>

## 120.55 `CONFIG_MFD_NPM10XX_INIT_PRIORITY`

**提示（Prompt）**：nPM10xx MFD 初始化优先级

**说明（Help）**

nPM10xx 多功能设备的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MFD_NPM10XX && CONFIG_MFD
```

**默认值（Defaults）**

```text
CONFIG_MFD_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.npm10xx:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.npm10xx#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → nPM10xx PMIC 多功能设备驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD_NPM10XX`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_NPM10XX)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_MFD_INIT_PRIORITY`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_INIT_PRIORITY)。

<a id="CONFIG_MFD_NPM13XX"></a>

## 120.56 `CONFIG_MFD_NPM13XX`

**提示（Prompt）**：nPM13xx PMIC 多功能设备驱动

**说明（Help）**

启用 Nordic nPM13xx PMIC 多功能设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_NORDIC_NPM1300_ENABLED || DT_HAS_NORDIC_NPM1304_ENABLED) && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.npm13xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.npm13xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MFD_NPM13XX_INIT_PRIORITY"></a>

## 120.57 `CONFIG_MFD_NPM13XX_INIT_PRIORITY`

**提示（Prompt）**：nPM13xx MFD 初始化优先级

**说明（Help）**

nPM13xx 多功能设备的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MFD_NPM13XX && CONFIG_MFD
```

**默认值（Defaults）**

```text
CONFIG_MFD_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.npm13xx:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.npm13xx#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → nPM13xx PMIC 多功能设备驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD_NPM13XX`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_NPM13XX)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_MFD_INIT_PRIORITY`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_INIT_PRIORITY)。

<a id="CONFIG_MFD_NPM2100"></a>

## 120.58 `CONFIG_MFD_NPM2100`

**提示（Prompt）**：nPM2100 PMIC 多功能设备驱动

**说明（Help）**

启用 Nordic nPM2100 PMIC 多功能设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NPM2100_ENABLED && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.npm2100:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.npm2100#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MFD_NPM6001"></a>

## 120.59 `CONFIG_MFD_NPM6001`

**提示（Prompt）**：nPM6001 PMIC 多功能设备驱动

**说明（Help）**

启用 Nordic nPM6001 PMIC 多功能设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NPM6001_ENABLED && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.npm6001:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.npm6001#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MFD_NPM6001_INIT_PRIORITY"></a>

## 120.60 `CONFIG_MFD_NPM6001_INIT_PRIORITY`

**提示（Prompt）**：nPM6001 MFD 初始化优先级

**说明（Help）**

nPM6001 多功能设备的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MFD_NPM6001 && CONFIG_MFD
```

**默认值（Defaults）**

```text
CONFIG_MFD_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.npm6001:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.npm6001#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → nPM6001 PMIC 多功能设备驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD_NPM6001`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_NPM6001)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_MFD_INIT_PRIORITY`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_INIT_PRIORITY)。

<a id="CONFIG_MFD_PCA9422"></a>

## 120.61 `CONFIG_MFD_PCA9422`

**提示（Prompt）**：NXP PCA9422 PMIC 多功能设备驱动

**说明（Help）**

启用 NXP PCA9422 PMIC 多功能设备驱动。该 PMIC 通过 I²C 总线提供充电器／稳压器（Charger/Regulator）功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_PCA9422_ENABLED && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.pca9422:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.pca9422#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MFD_PF1550"></a>

## 120.62 `CONFIG_MFD_PF1550`

**提示（Prompt）**：PF1550 PMIC 多功能设备驱动

**说明（Help）**

启用 NXP PF1550 PMIC 多功能设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_PF1550_ENABLED && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.pf1550:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.pf1550#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MFD_RV3028"></a>

## 120.63 `CONFIG_MFD_RV3028`

**提示（Prompt）**：Micro Crystal RV3028 RTC 多功能设备驱动

**说明（Help）**

启用 Micro Crystal RV3028 RTC 的父 MFD 驱动。此驱动管理 I²C 寄存器访问，以及 RV3028 各功能子驱动使用的共享资源。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCRYSTAL_RV3028_ENABLED && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.rv3028:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.rv3028#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MFD_RV3028_INIT_PRIORITY"></a>

## 120.64 `CONFIG_MFD_RV3028_INIT_PRIORITY`

**提示（Prompt）**：RV3028 MFD 初始化优先级

**说明（Help）**

Micro Crystal RV3028 MFD 驱动的初始化优先级。必须先于 RV3028 子驱动的初始化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MFD_RV3028 && CONFIG_MFD
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.rv3028:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.rv3028#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → Micro Crystal RV3028 RTC 多功能设备驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD_RV3028`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_RV3028)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_RV3032"></a>

## 120.65 `CONFIG_MFD_RV3032`

**提示（Prompt）**：RV3032 的 MFD 驱动

**说明（Help）**

启用 RV3032 RTC 的 MFD 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCRYSTAL_RV3032_MFD_ENABLED && CONFIG_GPIO && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**被选择（Selected by）**

```text
CONFIG_RTC_RV3032
CONFIG_RV3032_TEMP
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.rv3032_mfd:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.rv3032_mfd#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_RTC_RV3032`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTC_RV3032)、[`CONFIG_RV3032_TEMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RV3032_TEMP)。

<a id="CONFIG_MFD_SC18IS606"></a>

## 120.66 `CONFIG_MFD_SC18IS606`

**提示（Prompt）**：NXP SC18IS606 SPI/GPIO 桥接器（Bridge）

**说明（Help）**

启用 NXP SC18IS606 SPI/GPIO 桥接器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_SC18IS606_ENABLED && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.sc18is606_mfd:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.sc18is606_mfd#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MFD_TLA2528"></a>

## 120.67 `CONFIG_MFD_TLA2528`

**提示（Prompt）**：带 GPIO 的 Texas Instruments TLA2528 I²C ADC

**说明（Help）**

启用 TLA2528 的 MFD 驱动实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_TLA2528_ENABLED && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.tla2528:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.tla2528#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MFD_TLA2528_INIT_PRIO"></a>

## 120.68 `CONFIG_MFD_TLA2528_INIT_PRIO`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MFD_TLA2528 && CONFIG_MFD
```

**默认值（Defaults）**

```text
65
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.tla2528:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.tla2528#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → 带 GPIO 的 Texas Instruments TLA2528 I²C ADC

**配置项引用（Symbol References）**：[`CONFIG_MFD_TLA2528`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_TLA2528)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MFD_TLE9104"></a>

## 120.69 `CONFIG_MFD_TLE9104`

**提示（Prompt）**：Infineon TLE9104 SPI 动力总成开关（Powertrain Switch）

**说明（Help）**

启用 TLE9104 基于 SPI 的动力总成开关驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_TLE9104_ENABLED && CONFIG_SPI && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.tle9104:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.tle9104#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_NXP_LP_FLEXCOMM"></a>

## 120.70 `CONFIG_NXP_LP_FLEXCOMM`

**提示（Prompt）**：NXP 低功耗 FlexComm 接口（Low Power FlexComm Interface）驱动

**说明（Help）**

启用 Low Power FlexComm 适配层驱动（Shim Driver）。LP FlexComm 允许通过简化接口同时启用 LPUART 和 LPI2C。此驱动检查并行启用情况；若不支持该并行启用组合，则返回错误。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LP_FLEXCOMM_ENABLED && CONFIG_MFD
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mfd/Kconfig.lpflexcomm:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/Kconfig.lpflexcomm#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<!-- kconfig-navigation -->

[上一章](P119_drivers_memc_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P121_drivers_mipi_dbi_配置项参考.md)
