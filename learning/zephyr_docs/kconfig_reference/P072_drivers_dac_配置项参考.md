---
id: learning.zephyr-docs.kconfig-reference.page-72
title: "`drivers/dac`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第72章\_`drivers/dac`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/dac` 的 61 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_DAC"></a>

## 72.1 `CONFIG_DAC`

**提示（Prompt）**：数模转换器（Digital-to-Analog Converter，DAC）驱动

**说明（Help）**

启用数模转换器（Digital-to-Analog Converter，DAC）驱动配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_LED_DAC
```

**定义位置（Location）**：[`drivers/dac/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LED_DAC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LED_DAC)。

<a id="CONFIG_DAC_AD5529R"></a>

## 72.2 `CONFIG_DAC_AD5529R`

**提示（Prompt）**：Analog Devices AD5529R DAC 驱动

**说明（Help）**

启用 Analog Devices AD5529R 16 通道、16 位电压输出数模转换器（DAC）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_AD5529R_ENABLED && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/dac/Kconfig.ad5529r:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.ad5529r#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_DAC_AD5529R_INIT_PRIORITY"></a>

## 72.3 `CONFIG_DAC_AD5529R_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

Analog Devices AD5529R DAC 设备驱动的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DAC_AD5529R && CONFIG_DAC
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/dac/Kconfig.ad5529r:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.ad5529r#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动 → Analog Devices AD5529R DAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC_AD5529R`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_AD5529R)、[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)。

<a id="CONFIG_DAC_AD559X"></a>

## 72.4 `CONFIG_DAC_AD559X`

**提示（Prompt）**：AD559x DAC 驱动

**说明（Help）**

启用 AD559x DAC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_AD559X_DAC_ENABLED && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/dac/Kconfig.ad559x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.ad559x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_DAC_AD569X"></a>

## 72.5 `CONFIG_DAC_AD569X`

**提示（Prompt）**：Analog Devices AD5691 / AD5692 / AD5693 DAC 驱动

**说明（Help）**

启用 Analog Devices AD569X 的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ADI_AD5691_ENABLED || DT_HAS_ADI_AD5692_ENABLED || DT_HAS_ADI_AD5693_ENABLED) && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/dac/Kconfig.ad569x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.ad569x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_DAC_AD56X1"></a>

## 72.6 `CONFIG_DAC_AD56X1`

**提示（Prompt）**：Analog Devices AD56x1 DAC 驱动

**说明（Help）**

启用 Analog Devices AD56x1 DAC 的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ADI_AD5601_ENABLED || DT_HAS_ADI_AD5611_ENABLED || DT_HAS_ADI_AD5621_ENABLED) && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/dac/Kconfig.ad56x1:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.ad56x1#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_DAC_AD56X1_INIT_PRIORITY"></a>

## 72.7 `CONFIG_DAC_AD56X1_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

Analog Devices AD56x1 DAC 设备驱动的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DAC_AD56X1 && CONFIG_DAC
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/dac/Kconfig.ad56x1:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.ad56x1#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动 → Analog Devices AD56x1 DAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC_AD56X1`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_AD56X1)、[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)。

<a id="CONFIG_DAC_AD56XX"></a>

## 72.8 `CONFIG_DAC_AD56XX`

**提示（Prompt）**：Analog Devices AD56xx DAC 驱动

**说明（Help）**

启用 Analog Devices AD56xx DAC 的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ADI_AD5628_ENABLED || DT_HAS_ADI_AD5648_ENABLED || DT_HAS_ADI_AD5668_ENABLED || DT_HAS_ADI_AD5672_ENABLED || DT_HAS_ADI_AD5674_ENABLED || DT_HAS_ADI_AD5676_ENABLED || DT_HAS_ADI_AD5679_ENABLED || DT_HAS_ADI_AD5684_ENABLED || DT_HAS_ADI_AD5686_ENABLED || DT_HAS_ADI_AD5687_ENABLED || DT_HAS_ADI_AD5689_ENABLED) && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/dac/Kconfig.ad56xx:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.ad56xx#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_DAC_AD56XX_INIT_PRIORITY"></a>

## 72.9 `CONFIG_DAC_AD56XX_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

Analog Devices AD56xx DAC 设备驱动的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DAC_AD56XX && CONFIG_DAC
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/dac/Kconfig.ad56xx:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.ad56xx#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动 → Analog Devices AD56xx DAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC_AD56XX`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_AD56XX)、[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)。

<a id="CONFIG_DAC_DAC161S997"></a>

## 72.10 `CONFIG_DAC_DAC161S997`

**提示（Prompt）**：TI DAC161S997 DAC 驱动

**说明（Help）**

启用 TI DAC161S997 的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_DAC161S997_ENABLED && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/dac/Kconfig.dac161s997:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.dac161s997#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_DAC_DACX0501"></a>

## 72.11 `CONFIG_DAC_DACX0501`

**提示（Prompt）**：TI DACx0501 DAC 驱动

**说明（Help）**

启用 TI DACx0501 的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_DACX0501_ENABLED && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/dac/Kconfig.dacx0501:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.dacx0501#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_DAC_DACX0501_INIT_PRIORITY"></a>

## 72.12 `CONFIG_DAC_DACX0501_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

TI DACx0501 DAC 设备驱动的初始化优先级（Initialization Priority）。数值必须大于 `I2C_INIT_PRIORITY`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DAC_DACX0501 && CONFIG_DAC
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/dac/Kconfig.dacx0501:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.dacx0501#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动 → TI DACx0501 DAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC_DACX0501`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_DACX0501)、[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)。

<a id="CONFIG_DAC_DACX0508"></a>

## 72.13 `CONFIG_DAC_DACX0508`

**提示（Prompt）**：TI DACx0508 DAC 驱动

**说明（Help）**

启用 TI DACx0508 的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_TI_DAC60508_ENABLED || DT_HAS_TI_DAC70508_ENABLED || DT_HAS_TI_DAC80508_ENABLED) && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/dac/Kconfig.dacx0508:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.dacx0508#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_DAC_DACX0508_INIT_PRIORITY"></a>

## 72.14 `CONFIG_DAC_DACX0508_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

TI DACx0508 DAC 设备驱动的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DAC_DACX0508 && CONFIG_DAC
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/dac/Kconfig.dacx0508:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.dacx0508#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动 → TI DACx0508 DAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC_DACX0508`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_DACX0508)、[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)。

<a id="CONFIG_DAC_DACX311"></a>

## 72.15 `CONFIG_DAC_DACX311`

**提示（Prompt）**：TI DACx311/DACx411 DAC 驱动

**说明（Help）**

启用 TI DACx311/DACx411 芯片的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_TI_DAC8411_ENABLED || DT_HAS_TI_DAC8311_ENABLED || DT_HAS_TI_DAC7311_ENABLED || DT_HAS_TI_DAC6311_ENABLED || DT_HAS_TI_DAC5311_ENABLED) && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/dac/Kconfig.dacx311:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.dacx311#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_DAC_DACX3508"></a>

## 72.16 `CONFIG_DAC_DACX3508`

**提示（Prompt）**：TI DACx3508 DAC 驱动

**说明（Help）**

启用 TI DACx3508 的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_TI_DAC43508_ENABLED || DT_HAS_TI_DAC53508_ENABLED || DT_HAS_TI_DAC63508_ENABLED) && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/dac/Kconfig.dacx3508:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.dacx3508#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_DAC_DACX3508_INIT_PRIORITY"></a>

## 72.17 `CONFIG_DAC_DACX3508_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

TI DACx3508 DAC 设备驱动的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DAC_DACX3508 && CONFIG_DAC
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/dac/Kconfig.dacx3508:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.dacx3508#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动 → TI DACx3508 DAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC_DACX3508`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_DACX3508)、[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)。

<a id="CONFIG_DAC_DACX3608"></a>

## 72.18 `CONFIG_DAC_DACX3608`

**提示（Prompt）**：TI DACX3608 DAC 驱动

**说明（Help）**

启用 TI DACX3608 的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_TI_DAC43608_ENABLED || DT_HAS_TI_DAC53608_ENABLED) && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/dac/Kconfig.dacx3608:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.dacx3608#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_DAC_DACX3608_INIT_PRIORITY"></a>

## 72.19 `CONFIG_DAC_DACX3608_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

TI DACX3608 DAC 设备驱动的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DAC_DACX3608 && CONFIG_DAC
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/dac/Kconfig.dacx3608:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.dacx3608#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动 → TI DACX3608 DAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC_DACX3608`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_DACX3608)、[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)。

<a id="CONFIG_DAC_EMUL"></a>

## 72.20 `CONFIG_DAC_EMUL`

**提示（Prompt）**：DAC 仿真器（Emulator）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_DAC_EMUL_ENABLED && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dac/Kconfig.dac_emul:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.dac_emul#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)。

<a id="CONFIG_DAC_ESP32"></a>

## 72.21 `CONFIG_DAC_ESP32`

**提示（Prompt）**：ESP32 DAC 驱动

**说明（Help）**

启用 ESP32 DAC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_DAC_ENABLED && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dac/Kconfig.esp32:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.esp32#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)。

<a id="CONFIG_DAC_GD32"></a>

## 72.22 `CONFIG_DAC_GD32`

**提示（Prompt）**：GD32 DAC 驱动

**说明（Help）**

启用兆易创新（GigaDevice）GD32 DAC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GD_GD32_DAC_ENABLED && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/dac/Kconfig.gd32:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.gd32#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_DAC_INFINEON_AUTANALOG"></a>

## 72.23 `CONFIG_DAC_INFINEON_AUTANALOG`

**提示（Prompt）**：Infineon AutAnalog CT DAC 驱动

**说明（Help）**

为采用 AutAnalog CT DAC 子系统的英飞凌（Infineon）微控制器（MCU）启用 CT DAC 驱动。CT DAC 是一种 12 位连续时间分段式数模转换器（Continuous-Time Segmented DAC）。本驱动支持固件通道（FW Channel，#15），可通过 Zephyr DAC API 直接写入数值；同时支持波形通道（Waveform Channel，#0–#14），可依据查找表（Lookup Table，LUT）自主输出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_AUTANALOG_CTDAC_ENABLED && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/dac/Kconfig.infineon_autanalog_ctdac:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.infineon_autanalog_ctdac#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_DAC_INFINEON_AUTANALOG_INIT_PRIORITY"></a>

## 72.24 `CONFIG_DAC_INFINEON_AUTANALOG_INIT_PRIORITY`

**提示（Prompt）**：Infineon AutAnalog DAC 初始化优先级（Init Priority）

**说明（Help）**

AutAnalog DAC 驱动的初始化优先级（Initialization Priority）。其数值必须大于 `CONFIG_MFD_INFINEON_AUTANALOG_INIT_PRIORITY`（MFD 父设备），小于 `CONFIG_MFD_INFINEON_AUTANALOG_AC_START_PRIORITY`，确保自主控制器（Autonomous Controller）启动并通过 STT 触发 DAC 之前，已加载 DAC 硬件配置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DAC_INFINEON_AUTANALOG && CONFIG_DAC
```

**默认值（Defaults）**

```text
43
```

**定义位置（Location）**：[`drivers/dac/Kconfig.infineon_autanalog_ctdac:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.infineon_autanalog_ctdac#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动 → Infineon AutAnalog CT DAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC_INFINEON_AUTANALOG`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_INFINEON_AUTANALOG)、[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)。

<a id="CONFIG_DAC_INFINEON_HPPASS_CSG"></a>

## 72.25 `CONFIG_DAC_INFINEON_HPPASS_CSG`

**提示（Prompt）**：Infineon HPPASS CSG DAC 驱动

**说明（Help）**

启用英飞凌（Infineon）HPPASS CSG 模块的 DAC 驱动。每个实例通过 Zephyr DAC API，以直接写入模式（Direct-Write Mode）提供一个 CSG 单元（Slice）的 10 位 DAC。目前尚不支持缓冲（Buffered）、迟滞（Hysteretic）、斜坡（Slope）和查找表（LUT）等高级模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_HPPASS_CSG_DAC_ENABLED && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/dac/Kconfig.infineon_hppass_csg:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.infineon_hppass_csg#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_DAC_INFINEON_HPPASS_CSG_INIT_PRIORITY"></a>

## 72.26 `CONFIG_DAC_INFINEON_HPPASS_CSG_INIT_PRIORITY`

**提示（Prompt）**：Infineon HPPASS CSG DAC 初始化优先级（Init Priority）

**说明（Help）**

每个单元（Slice）的 DAC 子驱动的初始化优先级（Initialization Priority）。数值必须大于 `CONFIG_MFD_INFINEON_HPPASS_CSG_INIT_PRIORITY`，也就是更晚初始化，以确保本驱动运行之前 CSG 多功能设备（MFD）父设备已就绪。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DAC_INFINEON_HPPASS_CSG && CONFIG_DAC
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`drivers/dac/Kconfig.infineon_hppass_csg:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.infineon_hppass_csg#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动 → Infineon HPPASS CSG DAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC_INFINEON_HPPASS_CSG`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_INFINEON_HPPASS_CSG)、[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)。

<a id="CONFIG_DAC_INIT_PRIORITY"></a>

## 72.27 `CONFIG_DAC_INIT_PRIORITY`

**提示（Prompt）**：DAC 初始化优先级（Init Priority）

**说明（Help）**

DAC 设备驱动的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DAC
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`drivers/dac/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_DAC_LTC166X"></a>

## 72.28 `CONFIG_DAC_LTC166X`

**提示（Prompt）**：Linear Technology LTC166X DAC 驱动

**说明（Help）**

启用 Linear Technology LTC166X DAC 的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_LLTC_LTC1660_ENABLED || DT_HAS_LLTC_LTC1665_ENABLED) && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/dac/Kconfig.ltc166x:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.ltc166x#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_DAC_LTC166X_INIT_PRIORITY"></a>

## 72.29 `CONFIG_DAC_LTC166X_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

Linear Technology LTC166X DAC 设备驱动的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DAC_LTC166X && CONFIG_DAC
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/dac/Kconfig.ltc166x:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.ltc166x#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动 → Linear Technology LTC166X DAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC_LTC166X`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_LTC166X)、[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)。

<a id="CONFIG_DAC_MAX22017"></a>

## 72.30 `CONFIG_DAC_MAX22017`

**提示（Prompt）**：Analog Devices MAX22017 DAC 驱动

**说明（Help）**

启用 Analog Devices MAX22017 DAC 的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX22017_DAC_ENABLED && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/dac/Kconfig.max22017:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.max22017#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_DAC_MAX22017_INIT_PRIORITY"></a>

## 72.31 `CONFIG_DAC_MAX22017_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

Analog Devices MAX22017 DAC 设备驱动的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DAC_MAX22017 && CONFIG_DAC
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/dac/Kconfig.max22017:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.max22017#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动 → Analog Devices MAX22017 DAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC_MAX22017`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_MAX22017)、[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)。

<a id="CONFIG_DAC_MCHP_G1"></a>

## 72.32 `CONFIG_DAC_MCHP_G1`

**提示（Prompt）**：Microchip G1 DAC 驱动

**说明（Help）**

启用 Microchip G1 DAC 外设的 DAC 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_DAC_G1_ENABLED && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/dac/Kconfig.mchp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.mchp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_DAC_MCHP_G1_DIFFERENTIAL"></a>

## 72.33 `CONFIG_DAC_MCHP_G1_DIFFERENTIAL`

**提示（Prompt）**：差分模式（Differential Mode）

**说明（Help）**

启用 G1 DAC 的差分模式（Differential Mode）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DAC_MCHP_G1 && CONFIG_DAC
```

**定义位置（Location）**：[`drivers/dac/Kconfig.mchp:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.mchp#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动 → Microchip G1 DAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC_MCHP_G1`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_MCHP_G1)、[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)。

<a id="CONFIG_DAC_MCHP_G1_EXTERNAL_FILTER"></a>

## 72.34 `CONFIG_DAC_MCHP_G1_EXTERNAL_FILTER`

**提示（Prompt）**：外部滤波器（External Filter）

**说明（Help）**

启用 G1 DAC 的外部滤波器（External Filter）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X && CONFIG_DAC_MCHP_G1 && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dac/Kconfig.mchp:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.mchp#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动 → Microchip G1 DAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X)、[`CONFIG_DAC_MCHP_G1`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_MCHP_G1)、[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`。

<a id="CONFIG_DAC_MCHP_G1_OVERSAMPLING_RATIO"></a>

## 72.35 `CONFIG_DAC_MCHP_G1_OVERSAMPLING_RATIO`

**提示（Prompt）**：过采样率（Oversampling Ratio）

**说明（Help）**

启用 G1 DAC 的过采样率（Oversampling Ratio）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X && CONFIG_DAC_MCHP_G1 && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dac/Kconfig.mchp:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.mchp#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动 → Microchip G1 DAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X)、[`CONFIG_DAC_MCHP_G1`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_MCHP_G1)、[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`。

<a id="CONFIG_DAC_MCHP_G1_REFRESH"></a>

## 72.36 `CONFIG_DAC_MCHP_G1_REFRESH`

**提示（Prompt）**：刷新周期（Refresh Period）

**说明（Help）**

启用 G1 DAC 的刷新周期（Refresh Period）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X && CONFIG_DAC_MCHP_G1 && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dac/Kconfig.mchp:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.mchp#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动 → Microchip G1 DAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X)、[`CONFIG_DAC_MCHP_G1`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_MCHP_G1)、[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`。

<a id="CONFIG_DAC_MCHP_G2"></a>

## 72.37 `CONFIG_DAC_MCHP_G2`

**提示（Prompt）**：Microchip G2 DAC 驱动

**说明（Help）**

启用 Microchip G2 DAC 外设的 DAC 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_DAC_G2_ENABLED && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/dac/Kconfig.mchp:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.mchp#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_DAC_MCP4725"></a>

## 72.38 `CONFIG_DAC_MCP4725`

**提示（Prompt）**：Microchip MCP4725 DAC 驱动

**说明（Help）**

启用 Microchip MCP4725 的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_MCP4725_ENABLED && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/dac/Kconfig.mcp4725:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.mcp4725#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_DAC_MCP4725_INIT_PRIORITY"></a>

## 72.39 `CONFIG_DAC_MCP4725_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

Microchip MCP4725 DAC 设备驱动的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DAC_MCP4725 && CONFIG_DAC
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/dac/Kconfig.mcp4725:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.mcp4725#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动 → Microchip MCP4725 DAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC_MCP4725`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_MCP4725)、[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)。

<a id="CONFIG_DAC_MCP4728"></a>

## 72.40 `CONFIG_DAC_MCP4728`

**提示（Prompt）**：Microchip MCP4728 DAC 驱动

**说明（Help）**

启用 Microchip MCP4728 的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_MCP4728_ENABLED && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/dac/Kconfig.mcp4728:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.mcp4728#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_DAC_MCP4728_INIT_PRIORITY"></a>

## 72.41 `CONFIG_DAC_MCP4728_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

Microchip MCP4728 设备驱动的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DAC_MCP4728 && CONFIG_DAC
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/dac/Kconfig.mcp4728:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.mcp4728#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动 → Microchip MCP4728 DAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC_MCP4728`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_MCP4728)、[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)。

<a id="CONFIG_DAC_MCUX_DAC"></a>

## 72.42 `CONFIG_DAC_MCUX_DAC`

**提示（Prompt）**：NXP Kinetis MCUX DAC 驱动

**说明（Help）**

启用 NXP Kinetis MCUX DAC 的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_KINETIS_DAC_ENABLED && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dac/Kconfig.mcux:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.mcux#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)。

<a id="CONFIG_DAC_MCUX_DAC12"></a>

## 72.43 `CONFIG_DAC_MCUX_DAC12`

**提示（Prompt）**：NXP MCUX DAC12 驱动

**说明（Help）**

启用 NXP MCUX DAC12 的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_DAC12_ENABLED && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dac/Kconfig.mcux:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.mcux#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)。

<a id="CONFIG_DAC_MCUX_DAC32"></a>

## 72.44 `CONFIG_DAC_MCUX_DAC32`

**提示（Prompt）**：NXP Kinetis MCUX DAC32 驱动

**说明（Help）**

启用 NXP Kinetis MCUX DAC32 的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_KINETIS_DAC32_ENABLED && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/dac/Kconfig.mcux:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.mcux#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_DAC_MCUX_DAC32_TESTOUT"></a>

## 72.45 `CONFIG_DAC_MCUX_DAC32_TESTOUT`

**提示（Prompt）**：DAC 测试输出（Test Output）

**说明（Help）**

启用 DAC 测试输出（Test Output）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DAC_MCUX_DAC32 && CONFIG_DAC
```

**定义位置（Location）**：[`drivers/dac/Kconfig.mcux:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.mcux#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC_MCUX_DAC32`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_MCUX_DAC32)、[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)。

<a id="CONFIG_DAC_MCUX_GAU"></a>

## 72.46 `CONFIG_DAC_MCUX_GAU`

**提示（Prompt）**：NXP GAU DAC 驱动

**说明（Help）**

启用 NXP GAU DAC 的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_GAU_DAC_ENABLED && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dac/Kconfig.mcux:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.mcux#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)。

<a id="CONFIG_DAC_MCUX_LPDAC"></a>

## 72.47 `CONFIG_DAC_MCUX_LPDAC`

**提示（Prompt）**：NXP MCUX LPDAC 驱动

**说明（Help）**

启用 NXP MCUX LPDAC 的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPDAC_ENABLED && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/dac/Kconfig.mcux:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.mcux#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_DAC_MSPM0"></a>

## 72.48 `CONFIG_DAC_MSPM0`

**提示（Prompt）**：TI MSPM0 DAC 驱动

**说明（Help）**

启用德州仪器（Texas Instruments）MSPM0 G 系列微控制器（MCU）的数模转换器（Digital-to-Analog Converter，DAC）外设驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_MSPM0_DAC_ENABLED && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_MSPM0_DL_DAC12
```

**定义位置（Location）**：[`drivers/dac/Kconfig.mspm0:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.mspm0#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_USE_MSPM0_DL_DAC12`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_MSPM0_DL_DAC12)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_USE_MSPM0_DL_DAC12`。

<a id="CONFIG_DAC_NXP_HPDAC"></a>

## 72.49 `CONFIG_DAC_NXP_HPDAC`

**提示（Prompt）**：NXP HPDAC 驱动

**说明（Help）**

启用 NXP HPDAC 的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_HPDAC_ENABLED && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dac/Kconfig.mcux:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.mcux#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)。

<a id="CONFIG_DAC_RENESAS_RA"></a>

## 72.50 `CONFIG_DAC_RENESAS_RA`

**提示（Prompt）**：Renesas RA DAC 驱动

**说明（Help）**

启用瑞萨（Renesas）RA DAC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_DAC_ENABLED && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_DAC
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/dac/Kconfig.renesas_ra:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.renesas_ra#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_USE_RA_FSP_DAC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_DAC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_DAC_RENESAS_RA_DAVREFCR"></a>

## 72.51 `CONFIG_DAC_RENESAS_RA_DAVREFCR`

**提示（Prompt）**：数模转换参考电压（D/A Reference Voltage）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
CONFIG_DAC_RENESAS_RA_DAVREFCR_AVCC0_AVSS0
```

**可选项（Choices）**

```text
CONFIG_DAC_RENESAS_RA_DAVREFCR_NONE
CONFIG_DAC_RENESAS_RA_DAVREFCR_AVCC0_AVSS0
CONFIG_DAC_RENESAS_RA_DAVREFCR_VREFH_VREFL
```

**定义位置（Location）**：[`drivers/dac/Kconfig.renesas_ra:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.renesas_ra#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动 → Renesas RA DAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC_RENESAS_RA_DAVREFCR_AVCC0_AVSS0`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_RENESAS_RA_DAVREFCR_AVCC0_AVSS0)、[`CONFIG_DAC_RENESAS_RA_DAVREFCR_NONE`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_RENESAS_RA_DAVREFCR_NONE)、[`CONFIG_DAC_RENESAS_RA_DAVREFCR_VREFH_VREFL`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_RENESAS_RA_DAVREFCR_VREFH_VREFL)。

<a id="CONFIG_DAC_RENESAS_RA_DAVREFCR_AVCC0_AVSS0"></a>

## 72.52 `CONFIG_DAC_RENESAS_RA_DAVREFCR_AVCC0_AVSS0`

**提示（Prompt）**：使用 AVCC0/AVSS0 作为参考电压源（Reference Voltage Source）。

**说明（Help）**

选择 AVCC0/AVSS0

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DAC_RENESAS_RA_DAVREFCR>
```

**定义位置（Location）**：[`drivers/dac/Kconfig.renesas_ra:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.renesas_ra#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动 → Renesas RA DAC 驱动 → 数模转换参考电压（D/A Reference Voltage）

**配置项引用（Symbol References）**：[`CONFIG_DAC_RENESAS_RA_DAVREFCR`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_RENESAS_RA_DAVREFCR)。

<a id="CONFIG_DAC_RENESAS_RA_DAVREFCR_NONE"></a>

## 72.53 `CONFIG_DAC_RENESAS_RA_DAVREFCR_NONE`

**提示（Prompt）**：未选择参考电压（Reference Voltage）

**说明（Help）**

未选择参考电压（Reference Voltage）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DAC_RENESAS_RA_DAVREFCR>
```

**定义位置（Location）**：[`drivers/dac/Kconfig.renesas_ra:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.renesas_ra#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动 → Renesas RA DAC 驱动 → 数模转换参考电压（D/A Reference Voltage）

**配置项引用（Symbol References）**：[`CONFIG_DAC_RENESAS_RA_DAVREFCR`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_RENESAS_RA_DAVREFCR)。

<a id="CONFIG_DAC_RENESAS_RA_DAVREFCR_VREFH_VREFL"></a>

## 72.54 `CONFIG_DAC_RENESAS_RA_DAVREFCR_VREFH_VREFL`

**提示（Prompt）**：使用 VREFH/VREFL 作为参考电压源（Reference Voltage Source）。

**说明（Help）**

选择 VREFH/VREFL

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DAC_RENESAS_RA_DAVREFCR>
```

**定义位置（Location）**：[`drivers/dac/Kconfig.renesas_ra:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.renesas_ra#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动 → Renesas RA DAC 驱动 → 数模转换参考电压（D/A Reference Voltage）

**配置项引用（Symbol References）**：[`CONFIG_DAC_RENESAS_RA_DAVREFCR`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_RENESAS_RA_DAVREFCR)。

<a id="CONFIG_DAC_RENESAS_RA_DA_AD_SYNCHRONIZE"></a>

## 72.55 `CONFIG_DAC_RENESAS_RA_DA_AD_SYNCHRONIZE`

**提示（Prompt）**：数模与模数同步转换（D/A A/D Synchronous Conversion）

**说明（Help）**

- `n`：不使 DAC12 与 ADC（单元 1）的操作同步，即禁用数模转换（D/A Conversion）与模数转换（A/D Conversion）之间的干扰抑制。
- `y`：使 DAC12 与 ADC（单元 1）的操作同步，即启用数模转换（D/A Conversion）与模数转换（A/D Conversion）之间的干扰抑制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DAC_RENESAS_RA && CONFIG_DAC
```

**定义位置（Location）**：[`drivers/dac/Kconfig.renesas_ra:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.renesas_ra#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动 → Renesas RA DAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC_RENESAS_RA`](P072_drivers_dac_配置项参考.md#CONFIG_DAC_RENESAS_RA)、[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)。

<a id="CONFIG_DAC_SAM"></a>

## 72.56 `CONFIG_DAC_SAM`

**提示（Prompt）**：Atmel SAM DAC 驱动

**说明（Help）**

启用 Atmel SAM 微控制器（MCU）系列的 DAC 驱动。

> 译注：官方此处将 DAC 展开为 Digital Audio Converter（数字音频转换器），与本模块使用的 Digital-to-Analog Converter（数模转换器）名称不一致；保留这一原文差异，避免将其误认为另一个音频接口驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM_DAC_ENABLED && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/dac/Kconfig.sam:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.sam#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_DAC_SAM0"></a>

## 72.57 `CONFIG_DAC_SAM0`

**提示（Prompt）**：Atmel SAM0 系列 DAC 驱动

**说明（Help）**

启用 Atmel SAM0 微控制器（MCU）系列的数模转换（Digital-to-Analog，DAC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM0_DAC_ENABLED && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/dac/Kconfig.sam0:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.sam0#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_DAC_SAMD5X"></a>

## 72.58 `CONFIG_DAC_SAMD5X`

**提示（Prompt）**：Atmel SAMD5x 系列 DAC 驱动

**说明（Help）**

启用 Atmel SAMD5x 微控制器（MCU）系列的数模转换器（Digital-to-Analog Converter，DAC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAMD5X_DAC_ENABLED && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/dac/Kconfig.samd5x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.samd5x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_DAC_SHELL"></a>

## 72.59 `CONFIG_DAC_SHELL`

**提示（Prompt）**：DAC 命令行（Shell）

**说明（Help）**

启用 DAC 相关的命令行（Shell）命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_DAC
```

**定义位置（Location）**：[`drivers/dac/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)。

<a id="CONFIG_DAC_SILABS_VDAC"></a>

## 72.60 `CONFIG_DAC_SILABS_VDAC`

**提示（Prompt）**：Silabs VDAC 的 DAC 驱动

**说明（Help）**

启用 Silicon Labs 器件中 VDAC 硬件模块的数模转换器（Digital-to-Analog Converter）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_VDAC_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_SILABS_SISDK_VDAC
```

**定义位置（Location）**：[`drivers/dac/Kconfig.silabs:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.silabs#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_SILABS_SISDK_VDAC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_VDAC)。

<a id="CONFIG_DAC_STM32"></a>

## 72.61 `CONFIG_DAC_STM32`

**提示（Prompt）**：STM32 DAC 驱动

**说明（Help）**

启用 stm32xx DAC 的驱动实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_DAC_ENABLED && CONFIG_DAC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/dac/Kconfig.stm32:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/Kconfig.stm32#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<!-- kconfig-navigation -->

[上一章](P071_drivers_crypto_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P073_drivers_dai_配置项参考.md)
