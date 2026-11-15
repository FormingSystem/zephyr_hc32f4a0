---
id: learning.zephyr-docs.kconfig-reference.page-144
title: "`drivers/regulator`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第144章\_`drivers/regulator`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/regulator` 的 84 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_REGULATOR"></a>

## 144.1 `CONFIG_REGULATOR`

**提示（Prompt）**：稳压／稳流器（Regulator）驱动

**说明（Help）**

在系统配置中纳入电流／电压调节器（Current/Voltage Regulator）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_NRF70_VIN_SUPPLY
CONFIG_NRF70_IOVDD_REGULATOR
CONFIG_NRF70_VIN_SUPPLY
CONFIG_NRF70_IOVDD_REGULATOR
CONFIG_ADC_MCUX_LPADC
CONFIG_AUDIO_CODEC_CS35L5X_REGULATOR
CONFIG_COMPARATOR_NXP_HSCMP
CONFIG_HAPTICS_CS40L5X_EXTERNAL_BOOST
CONFIG_RCAR_MMC
CONFIG_SDHC_TI_AM654
CONFIG_USB_BC12_NRF_USBHS
CONFIG_UDC_DWC2
CONFIG_UHC_DWC2
```

**被弱选择（Implied by）**

```text
CONFIG_SOC_SERIES_BL60X
CONFIG_SOC_SERIES_BL61X
CONFIG_SOC_SERIES_BL70X
CONFIG_SOC_SERIES_BL70XL
CONFIG_SOC_SERIES_BL808
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/mikroe_lte_iot10_click/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/mikroe_lte_iot10_click/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/mikroe_lte_iot7_click/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/mikroe_lte_iot7_click/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`drivers/regulator/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_NRF70_VIN_SUPPLY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF70_VIN_SUPPLY)、[`CONFIG_NRF70_IOVDD_REGULATOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF70_IOVDD_REGULATOR)、[`CONFIG_ADC_MCUX_LPADC`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_MCUX_LPADC)、[`CONFIG_AUDIO_CODEC_CS35L5X_REGULATOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AUDIO_CODEC_CS35L5X_REGULATOR)、[`CONFIG_COMPARATOR_NXP_HSCMP`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR_NXP_HSCMP)、[`CONFIG_HAPTICS_CS40L5X_EXTERNAL_BOOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAPTICS_CS40L5X_EXTERNAL_BOOST)、[`CONFIG_RCAR_MMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RCAR_MMC)、[`CONFIG_SDHC_TI_AM654`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SDHC_TI_AM654)、[`CONFIG_USB_BC12_NRF_USBHS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_BC12_NRF_USBHS)、[`CONFIG_UDC_DWC2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_DWC2)、[`CONFIG_UHC_DWC2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UHC_DWC2)、[`CONFIG_SOC_SERIES_BL60X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL60X)、[`CONFIG_SOC_SERIES_BL61X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL61X)、[`CONFIG_SOC_SERIES_BL70X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70X)、[`CONFIG_SOC_SERIES_BL70XL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70XL)、[`CONFIG_SOC_SERIES_BL808`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL808)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_AUDIO_CODEC_CS35L5X_REGULATOR`、`CONFIG_HAPTICS_CS40L5X_EXTERNAL_BOOST`。

<a id="CONFIG_REGULATOR_ADI_MAX20362_COMMON_INIT_PRIORITY"></a>

## 144.2 `CONFIG_REGULATOR_ADI_MAX20362_COMMON_INIT_PRIORITY`

**提示（Prompt）**：MAX20362 稳压器驱动公共部分初始化优先级

**说明（Help）**

ADI MAX20362 稳压器驱动公共部分的初始化优先级，必须大于 I²C 初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_MAX20362 && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
86
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.max20362:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.max20362#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → MAX20362 PMIC 稳压器设备驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_MAX20362`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_MAX20362)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_ADI_MAX20362_INIT_PRIORITY"></a>

## 144.3 `CONFIG_REGULATOR_ADI_MAX20362_INIT_PRIORITY`

**提示（Prompt）**：MAX20362 稳压器驱动初始化优先级

**说明（Help）**

ADI MAX20362 稳压器驱动的初始化优先级，必须大于 `REGULATOR_ADI_MAX20362_COMMON_INIT_PRIORITY`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_MAX20362 && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
87
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.max20362:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.max20362#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → MAX20362 PMIC 稳压器设备驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_MAX20362`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_MAX20362)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_ADP5360"></a>

## 144.4 `CONFIG_REGULATOR_ADP5360`

**提示（Prompt）**：ADP5360 PMIC 稳压器驱动

**说明（Help）**

启用 Analog Devices ADP5360 电源管理芯片（PMIC）稳压器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_ADP5360_REGULATOR_ENABLED && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.adp5360:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.adp5360#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_REGULATOR_ADP5360_INIT_PRIORITY"></a>

## 144.5 `CONFIG_REGULATOR_ADP5360_INIT_PRIORITY`

**提示（Prompt）**：ADP5360 稳压器驱动初始化优先级

**说明（Help）**

Analog Devices ADP5360 稳压器驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_ADP5360 && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
88
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.adp5360:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.adp5360#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → ADP5360 PMIC 稳压器驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_ADP5360`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_ADP5360)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_AXP192_AXP2101"></a>

## 144.6 `CONFIG_REGULATOR_AXP192_AXP2101`

**提示（Prompt）**：X-Powers AXP192/AXP2101 PMIC 稳压器驱动

**说明（Help）**

启用 AXP PMIC 稳压器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_X_POWERS_AXP192_REGULATOR_ENABLED || DT_HAS_X_POWERS_AXP2101_REGULATOR_ENABLED) && (DT_HAS_X_POWERS_AXP192_ENABLED || DT_HAS_X_POWERS_AXP2101_ENABLED) && CONFIG_REGULATOR
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

**定义位置（Location）**：[`drivers/regulator/Kconfig.axp192:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.axp192#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_REGULATOR_AXP192_AXP2101_INIT_PRIORITY"></a>

## 144.7 `CONFIG_REGULATOR_AXP192_AXP2101_INIT_PRIORITY`

**提示（Prompt）**：AXP192/AXP2101 稳压器驱动初始化优先级

**说明（Help）**

AXP192/AXP2101 稳压器驱动的初始化优先级，必须大于 `MFD_INIT_PRIORITY`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_AXP192_AXP2101 && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
86
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.axp192:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.axp192#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → X-Powers AXP192/AXP2101 PMIC 稳压器驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_AXP192_AXP2101`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_AXP192_AXP2101)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_BFLB"></a>

## 144.8 `CONFIG_REGULATOR_BFLB`

**提示（Prompt）**：Bouffalolab 电源调节（Power Regulation）驱动

**说明（Help）**

启用 Bouffalolab 电源调节支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_BFLB_AON_REGULATOR_ENABLED || DT_HAS_BFLB_RT_REGULATOR_ENABLED || DT_HAS_BFLB_SOC_REGULATOR_ENABLED) && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.bflb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.bflb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_BFLB_INIT_PRIORITY"></a>

## 144.9 `CONFIG_REGULATOR_BFLB_INIT_PRIORITY`

**提示（Prompt）**：Bouffalolab 电源调节驱动初始化优先级

**说明（Help）**

Bouffalolab 电源调节驱动的初始化优先级，必须早于时钟控制（`clock_control`）初始化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_BFLB && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
25
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.bflb:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.bflb#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → Bouffalolab 电源调节（Power Regulation）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_BFLB`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_BFLB)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_CP9314"></a>

## 144.10 `CONFIG_REGULATOR_CP9314`

**提示（Prompt）**：CP9314 开关电容转换器（Switched Cap Converter）稳压器驱动

**说明（Help）**

启用 Cirrus Logic CP9314 开关电容转换器稳压器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_CIRRUS_CP9314_ENABLED && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.cp9314:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.cp9314#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_CP9314_INIT_PRIORITY"></a>

## 144.11 `CONFIG_REGULATOR_CP9314_INIT_PRIORITY`

**提示（Prompt）**：CP9314 稳压器驱动初始化优先级

**说明（Help）**

Cirrus Logic CP9314 开关电容转换器稳压器驱动的初始化优先级，必须大于 I²C 初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_CP9314 && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.cp9314:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.cp9314#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → CP9314 开关电容转换器（Switched Cap Converter）稳压器驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_CP9314`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_CP9314)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_REGULATOR_DA1469X"></a>

## 144.12 `CONFIG_REGULATOR_DA1469X`

**提示（Prompt）**：DA1469X 稳压器驱动

**说明（Help）**

启用 SmartBond DA1469x 稳压器支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_SMARTBOND_REGULATOR_ENABLED && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.da1469x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.da1469x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_DA1469X_INIT_PRIORITY"></a>

## 144.13 `CONFIG_REGULATOR_DA1469X_INIT_PRIORITY`

**提示（Prompt）**：Renesas DA1469x 稳压器驱动初始化优先级

**说明（Help）**

Renesas DA1469x 稳压器驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_DA1469X && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
20
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.da1469x:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.da1469x#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → DA1469X 稳压器驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_DA1469X`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_DA1469X)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_ESP32"></a>

## 144.14 `CONFIG_REGULATOR_ESP32`

**提示（Prompt）**：Espressif 片上稳压器（On-chip Regulator）驱动

**说明（Help）**

启用 Espressif 片上电压调节器支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_REGULATOR_ENABLED && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.esp32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.esp32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_ESP32_INIT_PRIORITY"></a>

## 144.15 `CONFIG_REGULATOR_ESP32_INIT_PRIORITY`

**提示（Prompt）**：Espressif 稳压器驱动初始化优先级

**说明（Help）**

Espressif 稳压器驱动的初始化优先级。数值必须低于 PSRAM/MEMC 驱动等使用方，使稳压器先初始化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_ESP32 && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
20
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.esp32:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.esp32#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → Espressif 片上稳压器（On-chip Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_ESP32`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_ESP32)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_FAKE"></a>

## 144.16 `CONFIG_REGULATOR_FAKE`

**提示（Prompt）**：模拟稳压器驱动程序。

**说明（Help）**

启用基于伪函数框架（FFF）的模拟稳压器驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_FAKE_REGULATOR_ENABLED && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.fake:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.fake#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_FAKE_COMMON_INIT_PRIORITY"></a>

## 144.17 `CONFIG_REGULATOR_FAKE_COMMON_INIT_PRIORITY`

**提示（Prompt）**：模拟稳压器驱动公共部分初始化优先级

**说明（Help）**

模拟稳压器驱动公共部分的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_FAKE && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
75
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.fake:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.fake#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → 模拟稳压器驱动程序。

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_FAKE`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_FAKE)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_FAKE_INIT_PRIORITY"></a>

## 144.18 `CONFIG_REGULATOR_FAKE_INIT_PRIORITY`

**提示（Prompt）**：模拟稳压器驱动初始化优先级

**说明（Help）**

模拟稳压器驱动的初始化优先级，必须大于 `REGULATOR_FAKE_COMMON_INIT_PRIORITY`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_FAKE && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
76
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.fake:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.fake#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → 模拟稳压器驱动程序。

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_FAKE`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_FAKE)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_FIXED"></a>

## 144.19 `CONFIG_REGULATOR_FIXED`

**提示（Prompt）**：GPIO 控制的稳压器（GPIO-controlled Regulators）

**说明（Help）**

启用 GPIO 控制的稳压器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REGULATOR_FIXED_ENABLED && CONFIG_GPIO && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.fixed:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.fixed#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_FIXED_INIT_PRIORITY"></a>

## 144.20 `CONFIG_REGULATOR_FIXED_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_FIXED && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
75
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.fixed:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.fixed#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → GPIO 控制的稳压器（GPIO-controlled Regulators）

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_FIXED`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_FIXED)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_GD32_BLDO"></a>

## 144.21 `CONFIG_REGULATOR_GD32_BLDO`

**提示（Prompt）**：GD32 BLDO 稳压器

**说明（Help）**

启用 GD32 备份 SRAM 低压差（LDO）稳压器，即 BLDO 的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GD_GD32_BLDO_ENABLED && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.gd32:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.gd32#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_GD32_BLDO_INIT_PRIORITY"></a>

## 144.22 `CONFIG_REGULATOR_GD32_BLDO_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_GD32_BLDO && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
35
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.gd32:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.gd32#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → GD32 BLDO 稳压器

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_GD32_BLDO`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_GD32_BLDO)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_GPIO"></a>

## 144.23 `CONFIG_REGULATOR_GPIO`

**提示（Prompt）**：GPIO 控制的稳压器（GPIO-controlled Regulators）

**说明（Help）**

启用 GPIO 控制的稳压器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REGULATOR_GPIO_ENABLED && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.gpio:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.gpio#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_REGULATOR_GPIO_INIT_PRIORITY"></a>

## 144.24 `CONFIG_REGULATOR_GPIO_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_GPIO && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
75
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.gpio:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.gpio#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → GPIO 控制的稳压器（GPIO-controlled Regulators）

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_GPIO`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_GPIO)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_INFINEON_AUTANALOG_PRB"></a>

## 144.25 `CONFIG_REGULATOR_INFINEON_AUTANALOG_PRB`

**提示（Prompt）**：Infineon AutAnalog PRB 电压基准稳压器（Voltage Reference Regulator）

**说明（Help）**

启用 Infineon AutAnalog PRB 电压基准稳压器驱动。每个实例提供一路可编程电压基准输出（Vref0 或 Vref1），具有由 VBGR（0.9 V）或 VDDA（1.8 V）派生的 16 个离散电压等级。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_AUTANALOG_PRB_VREF_ENABLED && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.infineon_autanalog_prb:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.infineon_autanalog_prb#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_REGULATOR_INFINEON_AUTANALOG_PRB_INIT_PRIORITY"></a>

## 144.26 `CONFIG_REGULATOR_INFINEON_AUTANALOG_PRB_INIT_PRIORITY`

**提示（Prompt）**：Infineon AutAnalog PRB 稳压器初始化优先级

**说明（Help）**

PRB 稳压器驱动的初始化优先级，数值必须高于 PRB MFD 初始化优先级（默认 42），即更晚执行。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_INFINEON_AUTANALOG_PRB && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
43
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.infineon_autanalog_prb:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.infineon_autanalog_prb#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → Infineon AutAnalog PRB 电压基准稳压器（Voltage Reference Regulator）

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_INFINEON_AUTANALOG_PRB`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_INFINEON_AUTANALOG_PRB)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_M5PM1"></a>

## 144.27 `CONFIG_REGULATOR_M5PM1`

**提示（Prompt）**：M5Stack M5PM1 稳压器驱动

**说明（Help）**

启用 M5Stack M5PM1 的固定电压稳压器（Fixed-voltage Regulator）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_M5STACK_M5PM1_REGULATOR_ENABLED && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.m5pm1:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.m5pm1#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_REGULATOR_M5PM1_INIT_PRIORITY"></a>

## 144.28 `CONFIG_REGULATOR_M5PM1_INIT_PRIORITY`

**提示（Prompt）**：M5PM1 稳压器驱动初始化优先级

**说明（Help）**

M5PM1 稳压器驱动的初始化优先级，必须大于 MFD 初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_M5PM1 && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
81
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.m5pm1:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.m5pm1#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → M5Stack M5PM1 稳压器驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_M5PM1`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_M5PM1)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_MAX20335"></a>

## 144.29 `CONFIG_REGULATOR_MAX20335`

**提示（Prompt）**：MAX20335 PMIC 稳压器驱动

**说明（Help）**

启用 Maxim MAX20335 PMIC 稳压器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXIM_MAX20335_REGULATOR_ENABLED && CONFIG_REGULATOR
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

**定义位置（Location）**：[`drivers/regulator/Kconfig.max20335:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.max20335#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_REGULATOR_MAX20362"></a>

## 144.30 `CONFIG_REGULATOR_MAX20362`

**提示（Prompt）**：MAX20362 PMIC 稳压器设备驱动

**说明（Help）**

启用 Analog Devices MAX20362 PMIC 稳压器设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX20362_REGULATOR_ENABLED && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.max20362:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.max20362#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_REGULATOR_MAXIM_MAX20335_COMMON_INIT_PRIORITY"></a>

## 144.31 `CONFIG_REGULATOR_MAXIM_MAX20335_COMMON_INIT_PRIORITY`

**提示（Prompt）**：MAX20335 稳压器驱动公共部分初始化优先级

**说明（Help）**

Maxim MAX20335 稳压器驱动公共部分的初始化优先级，必须大于 I²C 和 MFD 初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_MAX20335 && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
86
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.max20335:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.max20335#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → MAX20335 PMIC 稳压器驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_MAX20335`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_MAX20335)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_MAXIM_MAX20335_INIT_PRIORITY"></a>

## 144.32 `CONFIG_REGULATOR_MAXIM_MAX20335_INIT_PRIORITY`

**提示（Prompt）**：MAX20335 稳压器驱动初始化优先级

**说明（Help）**

Maxim MAX20335 稳压器驱动的初始化优先级，必须大于 `REGULATOR_MAXIM_MAX20335_COMMON_INIT_PRIORITY`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_MAX20335 && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
87
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.max20335:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.max20335#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → MAX20335 PMIC 稳压器驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_MAX20335`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_MAX20335)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_MODULINO_LATCH_RELAY"></a>

## 144.33 `CONFIG_REGULATOR_MODULINO_LATCH_RELAY`

**提示（Prompt）**：Arduino Modulino 锁存继电器（Latch Relay）

**说明（Help）**

启用 Arduino Modulino Latch Relay 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ARDUINO_MODULINO_LATCH_RELAY_ENABLED && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.modulino_latch_relay:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.modulino_latch_relay#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_REGULATOR_MODULINO_LATCH_RELAY_INIT_PRIORITY"></a>

## 144.34 `CONFIG_REGULATOR_MODULINO_LATCH_RELAY_INIT_PRIORITY`

**提示（Prompt）**：Arduino Modulino Latch Relay 驱动初始化优先级

**说明（Help）**

Arduino Modulino Latch Relay 驱动的初始化优先级，必须大于 I²C 初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_MODULINO_LATCH_RELAY && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
85
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.modulino_latch_relay:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.modulino_latch_relay#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → Arduino Modulino 锁存继电器（Latch Relay）

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_MODULINO_LATCH_RELAY`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_MODULINO_LATCH_RELAY)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_MPM54304"></a>

## 144.35 `CONFIG_REGULATOR_MPM54304`

**提示（Prompt）**：MPM54304 直流／直流降压电源模块（DC/DC Step-down Power Module）

**说明（Help）**

启用 MPM54304 DC/DC 降压电源模块支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MPS_MPM54304_ENABLED && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.mpm54304:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.mpm54304#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_REGULATOR_MPM54304_INIT_PRIORITY"></a>

## 144.36 `CONFIG_REGULATOR_MPM54304_INIT_PRIORITY`

**提示（Prompt）**：MPM54304 稳压器驱动初始化优先级

**说明（Help）**

MPS MPM54304 稳压器驱动的初始化优先级，必须大于 I²C 初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_MPM54304 && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
85
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.mpm54304:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.mpm54304#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → MPM54304 直流／直流降压电源模块（DC/DC Step-down Power Module）

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_MPM54304`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_MPM54304)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_MSPM0_VREF"></a>

## 144.37 `CONFIG_REGULATOR_MSPM0_VREF`

**提示（Prompt）**：TI MSPM0 电压基准（VREF）外设驱动

**说明（Help）**

启用 MSPM0 VREF 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR && DT_HAS_TI_MSPM0_VREF_ENABLED && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_MSPM0_DL_VREF
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.mspm0:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.mspm0#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_USE_MSPM0_DL_VREF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_MSPM0_DL_VREF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_USE_MSPM0_DL_VREF`。

<a id="CONFIG_REGULATOR_MSPM0_VREF_INIT_PRIORITY"></a>

## 144.38 `CONFIG_REGULATOR_MSPM0_VREF_INIT_PRIORITY`

**提示（Prompt）**：MSPM0 VREF 外设驱动初始化优先级

**说明（Help）**

MSPM0 VREF 外设的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_MSPM0_VREF && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.mspm0:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.mspm0#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → TI MSPM0 电压基准（VREF）外设驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_MSPM0_VREF`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_MSPM0_VREF)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_REGULATOR_NPM10XX"></a>

## 144.39 `CONFIG_REGULATOR_NPM10XX`

**提示（Prompt）**：nPM10xx 稳压器驱动

**说明（Help）**

启用 Nordic nPM10xx 稳压器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NPM10XX_REGULATOR_ENABLED && DT_HAS_NORDIC_NPM10XX_ENABLED && CONFIG_REGULATOR
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

**定义位置（Location）**：[`drivers/regulator/Kconfig.npm10xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.npm10xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_REGULATOR_NPM10XX_COMMON_INIT_PRIORITY"></a>

## 144.40 `CONFIG_REGULATOR_NPM10XX_COMMON_INIT_PRIORITY`

**提示（Prompt）**：nPM10xx 稳压器驱动公共部分初始化优先级

**说明（Help）**

Nordic nPM10xx 稳压器驱动公共部分的初始化优先级，必须大于 MFD 初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_NPM10XX && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
85
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.npm10xx:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.npm10xx#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → nPM10xx 稳压器驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_NPM10XX`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_NPM10XX)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_NPM10XX_INIT_PRIORITY"></a>

## 144.41 `CONFIG_REGULATOR_NPM10XX_INIT_PRIORITY`

**提示（Prompt）**：nPM10xx 稳压器驱动初始化优先级

**说明（Help）**

Nordic nPM10xx 稳压器驱动的初始化优先级，必须大于 `REGULATOR_NPM10XX_COMMON_INIT_PRIORITY`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_NPM10XX && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
86
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.npm10xx:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.npm10xx#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → nPM10xx 稳压器驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_NPM10XX`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_NPM10XX)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_NPM1100"></a>

## 144.42 `CONFIG_REGULATOR_NPM1100`

**提示（Prompt）**：nPM1100 PMIC 稳压器驱动

**说明（Help）**

启用 Nordic nPM1100 PMIC 稳压器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NPM1100_ENABLED && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.npm1100:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.npm1100#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_NPM1100_INIT_PRIORITY"></a>

## 144.43 `CONFIG_REGULATOR_NPM1100_INIT_PRIORITY`

**提示（Prompt）**：nPM1100 稳压器驱动初始化优先级

**说明（Help）**

Nordic nPM1100 稳压器驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_NPM1100 && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.npm1100:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.npm1100#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → nPM1100 PMIC 稳压器驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_NPM1100`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_NPM1100)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_REGULATOR_NPM13XX"></a>

## 144.44 `CONFIG_REGULATOR_NPM13XX`

**提示（Prompt）**：nPM13xx PMIC 稳压器驱动

**说明（Help）**

启用 Nordic nPM13xx PMIC 稳压器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_NORDIC_NPM1300_REGULATOR_ENABLED || DT_HAS_NORDIC_NPM1304_REGULATOR_ENABLED) && CONFIG_REGULATOR
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

**定义位置（Location）**：[`drivers/regulator/Kconfig.npm13xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.npm13xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_REGULATOR_NPM13XX_COMMON_INIT_PRIORITY"></a>

## 144.45 `CONFIG_REGULATOR_NPM13XX_COMMON_INIT_PRIORITY`

**提示（Prompt）**：nPM13xx 稳压器驱动公共部分初始化优先级

**说明（Help）**

Nordic nPM13xx 稳压器驱动公共部分的初始化优先级，必须大于 I²C 初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_NPM13XX && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
85
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.npm13xx:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.npm13xx#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → nPM13xx PMIC 稳压器驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_NPM13XX`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_NPM13XX)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_NPM13XX_INIT_PRIORITY"></a>

## 144.46 `CONFIG_REGULATOR_NPM13XX_INIT_PRIORITY`

**提示（Prompt）**：nPM13xx 稳压器驱动初始化优先级

**说明（Help）**

Nordic nPM13xx 稳压器驱动的初始化优先级，必须大于 `REGULATOR_NPM13XX_COMMON_INIT_PRIORITY`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_NPM13XX && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
86
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.npm13xx:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.npm13xx#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → nPM13xx PMIC 稳压器驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_NPM13XX`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_NPM13XX)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_NPM2100"></a>

## 144.47 `CONFIG_REGULATOR_NPM2100`

**提示（Prompt）**：nPM2100 PMIC 稳压器驱动

**说明（Help）**

启用 Nordic nPM2100 PMIC 稳压器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NPM2100_REGULATOR_ENABLED && CONFIG_REGULATOR
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

**定义位置（Location）**：[`drivers/regulator/Kconfig.npm2100:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.npm2100#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_REGULATOR_NPM2100_COMMON_INIT_PRIORITY"></a>

## 144.48 `CONFIG_REGULATOR_NPM2100_COMMON_INIT_PRIORITY`

**提示（Prompt）**：nPM2100 稳压器驱动公共部分初始化优先级

**说明（Help）**

Nordic nPM2100 稳压器驱动公共部分的初始化优先级，必须大于 I²C 初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_NPM2100 && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
85
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.npm2100:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.npm2100#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → nPM2100 PMIC 稳压器驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_NPM2100`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_NPM2100)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_NPM2100_INIT_PRIORITY"></a>

## 144.49 `CONFIG_REGULATOR_NPM2100_INIT_PRIORITY`

**提示（Prompt）**：nPM2100 稳压器驱动初始化优先级

**说明（Help）**

Nordic nPM2100 稳压器驱动的初始化优先级，必须大于 `REGULATOR_NPM2100_COMMON_INIT_PRIORITY`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_NPM2100 && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
86
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.npm2100:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.npm2100#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → nPM2100 PMIC 稳压器驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_NPM2100`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_NPM2100)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_NPM6001"></a>

## 144.50 `CONFIG_REGULATOR_NPM6001`

**提示（Prompt）**：nPM6001 PMIC 稳压器驱动

**说明（Help）**

启用 Nordic nPM6001 PMIC 稳压器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NPM6001_REGULATOR_ENABLED && CONFIG_REGULATOR
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

**定义位置（Location）**：[`drivers/regulator/Kconfig.npm6001:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.npm6001#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_REGULATOR_NPM6001_INIT_PRIORITY"></a>

## 144.51 `CONFIG_REGULATOR_NPM6001_INIT_PRIORITY`

**提示（Prompt）**：nPM6001 稳压器驱动初始化优先级

**说明（Help）**

Nordic nPM6001 稳压器驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_NPM6001 && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
86
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.npm6001:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.npm6001#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → nPM6001 PMIC 稳压器驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_NPM6001`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_NPM6001)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_NRF54L"></a>

## 144.52 `CONFIG_REGULATOR_NRF54L`

**提示（Prompt）**：nRF54L 稳压器驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF54L_REGULATORS_ENABLED && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.nrf54l:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.nrf54l#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_NRF54L_HIBERNATE_MIN_UPTIME_MS"></a>

## 144.53 `CONFIG_REGULATOR_NRF54L_HIBERNATE_MIN_UPTIME_MS`

**提示（Prompt）**：允许系统休眠（Hibernate）之前的最短运行时间

**说明（Help）**

进入系统休眠时，调试器会断开连接。此保护机制防止 SoC 在能够连接调试器之前进入系统休眠。生产环境中，应尽量缩短此保护时间，以节省电能。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_NRF54L && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.nrf54l:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.nrf54l#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → nRF54L 稳压器驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_NRF54L`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_NRF54L)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_NRF_VREGUSB"></a>

## 144.54 `CONFIG_REGULATOR_NRF_VREGUSB`

**提示（Prompt）**：Nordic USB VBUS 稳压器驱动

**说明（Help）**

启用 Nordic USB VBUS 稳压器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_VREGUSB_REGULATOR_ENABLED && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.nrf_vregusb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.nrf_vregusb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_NRF_VREGUSB_INIT_PRIORITY"></a>

## 144.55 `CONFIG_REGULATOR_NRF_VREGUSB_INIT_PRIORITY`

**提示（Prompt）**：Nordic VBUS 稳压器驱动初始化优先级

**说明（Help）**

Nordic USB VBUS 稳压器驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_NRF_VREGUSB && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.nrf_vregusb:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.nrf_vregusb#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → Nordic USB VBUS 稳压器驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_NRF_VREGUSB`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_NRF_VREGUSB)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_REGULATOR_NXP_SPC_BANDGAP"></a>

## 144.56 `CONFIG_REGULATOR_NXP_SPC_BANDGAP`

**提示（Prompt）**：NXP SPC 带隙缓冲器（Bandgap Buffer）驱动

**说明（Help）**

启用 NXP SPC 带缓冲的带隙基准输出驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_SPC_BANDGAP_BUFFER_ENABLED && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.nxp_spc_bandgap:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.nxp_spc_bandgap#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_NXP_SPC_BANDGAP_INIT_PRIORITY"></a>

## 144.57 `CONFIG_REGULATOR_NXP_SPC_BANDGAP_INIT_PRIORITY`

**提示（Prompt）**：NXP SPC 带隙缓冲器驱动初始化优先级

**说明（Help）**

NXP SPC 带缓冲的带隙基准输出的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_NXP_SPC_BANDGAP && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
45
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.nxp_spc_bandgap:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.nxp_spc_bandgap#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → NXP SPC 带隙缓冲器（Bandgap Buffer）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_NXP_SPC_BANDGAP`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_NXP_SPC_BANDGAP)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_NXP_VREF"></a>

## 144.58 `CONFIG_REGULATOR_NXP_VREF`

**提示（Prompt）**：NXP 电压基准（VREF）外设驱动

**说明（Help）**

启用 NXP VREF 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_VREF_ENABLED && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.nxp_vref:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.nxp_vref#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_NXP_VREFV1"></a>

## 144.59 `CONFIG_REGULATOR_NXP_VREFV1`

**提示（Prompt）**：NXP 电压基准（VREF）外设驱动

**说明（Help）**

启用 NXP VREF 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_VREFV1_ENABLED && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.nxp_vrefv1:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.nxp_vrefv1#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_NXP_VREFV1_INIT_PRIORITY"></a>

## 144.60 `CONFIG_REGULATOR_NXP_VREFV1_INIT_PRIORITY`

**提示（Prompt）**：NXP VREF 外设驱动初始化优先级

**说明（Help）**

NXP VREF 外设的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_NXP_VREFV1 && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
45
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.nxp_vrefv1:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.nxp_vrefv1#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → NXP 电压基准（VREF）外设驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_NXP_VREFV1`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_NXP_VREFV1)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_NXP_VREFV1_READY_TIMEOUT_MS"></a>

## 144.61 `CONFIG_REGULATOR_NXP_VREFV1_READY_TIMEOUT_MS`

**提示（Prompt）**：NXP VREF 就绪超时（Ready Timeout，毫秒）

**说明（Help）**

等待 VREF 就绪的超时时间，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_NXP_VREFV1 && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.nxp_vrefv1:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.nxp_vrefv1#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → NXP 电压基准（VREF）外设驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_NXP_VREFV1`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_NXP_VREFV1)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_NXP_VREF_INIT_PRIORITY"></a>

## 144.62 `CONFIG_REGULATOR_NXP_VREF_INIT_PRIORITY`

**提示（Prompt）**：NXP VREF 外设驱动初始化优先级

**说明（Help）**

NXP VREF 外设的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_VREF_ENABLED && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
45
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.nxp_vref:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.nxp_vref#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_PCA9420"></a>

## 144.63 `CONFIG_REGULATOR_PCA9420`

**提示（Prompt）**：NXP PCA9420 PMIC 稳压器驱动

**说明（Help）**

启用 NXP PCA9420 PMIC 稳压器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_PCA9420_ENABLED && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.pca9420:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.pca9420#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_REGULATOR_PCA9420_COMMON_INIT_PRIORITY"></a>

## 144.64 `CONFIG_REGULATOR_PCA9420_COMMON_INIT_PRIORITY`

**提示（Prompt）**：NXP PCA9420 稳压器驱动公共部分初始化优先级

**说明（Help）**

NXP PCA9420 稳压器驱动公共部分的初始化优先级，必须大于 I²C 初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_PCA9420 && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
75
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.pca9420:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.pca9420#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → NXP PCA9420 PMIC 稳压器驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_PCA9420`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_PCA9420)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_PCA9420_INIT_PRIORITY"></a>

## 144.65 `CONFIG_REGULATOR_PCA9420_INIT_PRIORITY`

**提示（Prompt）**：NXP PCA9420 稳压器驱动初始化优先级

**说明（Help）**

NXP PCA9420 稳压器驱动的初始化优先级，必须大于 `REGULATOR_PCA9420_COMMON_INIT_PRIORITY`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_PCA9420 && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
76
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.pca9420:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.pca9420#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → NXP PCA9420 PMIC 稳压器驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_PCA9420`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_PCA9420)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_PCA9422"></a>

## 144.66 `CONFIG_REGULATOR_PCA9422`

**提示（Prompt）**：NXP PCA9422 PMIC 稳压器驱动

**说明（Help）**

启用 NXP PCA9422 PMIC 稳压器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_PCA9422_REGULATOR_ENABLED && CONFIG_REGULATOR
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

**定义位置（Location）**：[`drivers/regulator/Kconfig.pca9422:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.pca9422#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_REGULATOR_PCA9422_COMMON_INIT_PRIORITY"></a>

## 144.67 `CONFIG_REGULATOR_PCA9422_COMMON_INIT_PRIORITY`

**提示（Prompt）**：NXP PCA9422 稳压器驱动公共部分初始化优先级

**说明（Help）**

NXP PCA9422 稳压器驱动公共部分的初始化优先级，必须大于 I²C 和 MFD 初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_PCA9422 && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
86
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.pca9422:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.pca9422#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → NXP PCA9422 PMIC 稳压器驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_PCA9422`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_PCA9422)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_PCA9422_INIT_PRIORITY"></a>

## 144.68 `CONFIG_REGULATOR_PCA9422_INIT_PRIORITY`

**提示（Prompt）**：NXP PCA9422 稳压器驱动初始化优先级

**说明（Help）**

NXP PCA9422 稳压器驱动的初始化优先级，必须大于 `REGULATOR_PCA9422_COMMON_INIT_PRIORITY`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_PCA9422 && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
87
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.pca9422:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.pca9422#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → NXP PCA9422 PMIC 稳压器驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_PCA9422`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_PCA9422)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_PF1550"></a>

## 144.69 `CONFIG_REGULATOR_PF1550`

**提示（Prompt）**：NXP PF1550 PMIC 稳压器驱动

**说明（Help）**

启用 NXP PF1550 PMIC 稳压器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_PF1550_REGULATOR_ENABLED && CONFIG_REGULATOR
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

**定义位置（Location）**：[`drivers/regulator/Kconfig.pf1550:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.pf1550#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_REGULATOR_RPI_PICO"></a>

## 144.70 `CONFIG_REGULATOR_RPI_PICO`

**提示（Prompt）**：Raspberry Pi Pico 稳压器驱动

**说明（Help）**

启用 Raspberry Pi Pico 稳压器支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RASPBERRYPI_CORE_SUPPLY_REGULATOR_ENABLED && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.rpi_pico:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.rpi_pico#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_RPI_PICO_INIT_PRIORITY"></a>

## 144.71 `CONFIG_REGULATOR_RPI_PICO_INIT_PRIORITY`

**提示（Prompt）**：Raspberry Pi Pico 稳压器驱动初始化优先级

**说明（Help）**

Raspberry Pi Pico 稳压器驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_RPI_PICO && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.rpi_pico:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.rpi_pico#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → Raspberry Pi Pico 稳压器驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_RPI_PICO`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_RPI_PICO)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_REGULATOR_RTS5817"></a>

## 144.72 `CONFIG_REGULATOR_RTS5817`

**提示（Prompt）**：RTS5817 稳压器驱动

**说明（Help）**

此选项启用 RTS5817 稳压器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_RTS5817_REGULATOR_ENABLED && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SYSCON
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.rts5817:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.rts5817#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_SYSCON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYSCON)。

<a id="CONFIG_REGULATOR_RTS5817_INIT_PRIORITY"></a>

## 144.73 `CONFIG_REGULATOR_RTS5817_INIT_PRIORITY`

**提示（Prompt）**：RTS5817 稳压器驱动初始化优先级

**说明（Help）**

RTS5817 稳压器驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_RTS5817 && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.rts5817:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.rts5817#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → RTS5817 稳压器驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_RTS5817`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_RTS5817)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_SF32LB_LDO"></a>

## 144.74 `CONFIG_REGULATOR_SF32LB_LDO`

**提示（Prompt）**：SiFli SF32LB 系列内部低压差（LDO）稳压器驱动

**说明（Help）**

启用 SF32LB52x 内部外设 LDO 支持：

- `LDO1_1V8`：为 PSRAM（VDDSIP）提供 1.8 V。
- `LDO2_3V3`：为外设提供 3.3 V。
- `LDO3_3V3`：为外设提供 3.3 V。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFLI_SF32LB52X_LDO_ENABLED && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.sf32lb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.sf32lb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_SF32LB_LDO_INIT_PRIORITY"></a>

## 144.75 `CONFIG_REGULATOR_SF32LB_LDO_INIT_PRIORITY`

**提示（Prompt）**：SF32LB LDO 稳压器初始化优先级

**说明（Help）**

SF32LB LDO 稳压器的初始化优先级，数值必须低于依赖它的驱动，例如 PSRAM，使稳压器先初始化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_SF32LB_LDO && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
20
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.sf32lb:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.sf32lb#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → SiFli SF32LB 系列内部低压差（LDO）稳压器驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_SF32LB_LDO`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_SF32LB_LDO)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_SHELL"></a>

## 144.76 `CONFIG_REGULATOR_SHELL`

**提示（Prompt）**：稳压器命令行（Regulator Shell）

**说明（Help）**

启用稳压器 Shell 框架，以便通过 Shell 接口与稳压器交互。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_REGULATOR
```

**定义位置（Location）**：[`drivers/regulator/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_STM32_SOFTWARE_TRIM"></a>

## 144.77 `CONFIG_REGULATOR_STM32_SOFTWARE_TRIM`

**提示（Prompt）**：通过软件从 OTP 复制修调数据（Trimming Data）

**说明（Help）**

更改电压范围时，通过软件从 OTP 复制修调数据。部分系列（例如 STM32WB）更改电压范围时，硬件不会自动从 OTP 加载修调数据；此时应启用本选项，确保 VREFBUF 输出电压正确。参考手册 VREFBUF 章节中的“VREFBUF trimming”小节会说明硬件是否自动加载修调数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.stm32_vrefbuf:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.stm32_vrefbuf#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → STM32 VREFBUF 稳压器驱动

<a id="CONFIG_REGULATOR_STM32_VREFBUF"></a>

## 144.78 `CONFIG_REGULATOR_STM32_VREFBUF`

**提示（Prompt）**：STM32 VREFBUF 稳压器驱动

**说明（Help）**

启用 STM32 VREFBUF 稳压器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_VREFBUF_ENABLED && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.stm32_vrefbuf:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.stm32_vrefbuf#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_STM32_VREFBUF_INIT_PRIORITY"></a>

## 144.79 `CONFIG_REGULATOR_STM32_VREFBUF_INIT_PRIORITY`

**提示（Prompt）**：STM32 VREFBUF 稳压器驱动初始化优先级

**说明（Help）**

STM32 VREFBUF 稳压器驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_STM32_VREFBUF && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
45
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.stm32_vrefbuf:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.stm32_vrefbuf#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → STM32 VREFBUF 稳压器驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_STM32_VREFBUF`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_STM32_VREFBUF)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_THREAD_SAFE_REFCNT"></a>

## 144.80 `CONFIG_REGULATOR_THREAD_SAFE_REFCNT`

**提示（Prompt）**：线程安全的引用计数（Thread-safe Reference Counting）

**说明（Help）**

启用后，稳压器引用计数具备线程安全性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MULTITHREADING && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/regulator/Kconfig:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_REGULATOR_TI_TPS6287X"></a>

## 144.81 `CONFIG_REGULATOR_TI_TPS6287X`

**提示（Prompt）**：TPS6287x 稳压器驱动

**说明（Help）**

启用 TPS6287x 稳压器支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_TPS6287X_ENABLED && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.ti_tp6287x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.ti_tp6287x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_REGULATOR_TPS55287"></a>

## 144.82 `CONFIG_REGULATOR_TPS55287`

**提示（Prompt）**：TPS55287 稳压器驱动

**说明（Help）**

启用 TPS55287 稳压器支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_TPS55287_ENABLED && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.tps55287:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.tps55287#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_REGULATOR_TPS55287_INIT_PRIORITY"></a>

## 144.83 `CONFIG_REGULATOR_TPS55287_INIT_PRIORITY`

**提示（Prompt）**：TPS55287 稳压器驱动初始化优先级

**说明（Help）**

TPS55287 稳压器驱动的初始化优先级，必须大于或等于父 I²C 总线的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_TPS55287 && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
CONFIG_I2C_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.tps55287:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.tps55287#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → TPS55287 稳压器驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_TPS55287`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_TPS55287)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_I2C_INIT_PRIORITY`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_INIT_PRIORITY)。

<a id="CONFIG_REGULATOR_TPS6287X_INIT_PRIORITY"></a>

## 144.84 `CONFIG_REGULATOR_TPS6287X_INIT_PRIORITY`

**提示（Prompt）**：TPS6287x 稳压器驱动初始化优先级

**说明（Help）**

TPS6287x 稳压器驱动的初始化优先级，必须大于或等于父 I²C 总线的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REGULATOR_TI_TPS6287X && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
CONFIG_I2C_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/regulator/Kconfig.ti_tp6287x:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/Kconfig.ti_tp6287x#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → TPS6287x 稳压器驱动

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_TI_TPS6287X`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_TI_TPS6287X)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_I2C_INIT_PRIORITY`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_INIT_PRIORITY)。

<!-- kconfig-navigation -->

[上一章](P143_drivers_pwm_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P145_drivers_reset_配置项参考.md)
