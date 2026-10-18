---
id: learning.zephyr-docs.kconfig-reference.page-99
title: "`drivers/gpio`配置项参考（2/3）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第99章\_`drivers/gpio`配置项参考（2/3）

本章翻译官方 Kconfig 数据库中 `drivers/gpio` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_GPIO_MSPM0"></a>

## 99.1 `CONFIG_GPIO_MSPM0`

**提示（Prompt）**：TI MSPM0 GPIO 驱动

**说明（Help）**

启用 TI MSPM0 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_MSPM0_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_MSPM0_DL_GPIO
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.mspm0:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.mspm0#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_USE_MSPM0_DL_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_MSPM0_DL_GPIO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_USE_MSPM0_DL_GPIO`。

<a id="CONFIG_GPIO_NCT38XX"></a>

## 99.2 `CONFIG_GPIO_NCT38XX`

**提示（Prompt）**：基于 I2C 的 NCT38XX GPIO 芯片

**说明（Help）**

启用基于 I2C 的 NCT38XX GPIO 芯片的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NCT38XX_GPIO_PORT_ENABLED && CONFIG_GPIO
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

**定义位置（Location）**：[`drivers/gpio/Kconfig.nct38xx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.nct38xx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_GPIO_NCT38XX_ALERT"></a>

## 99.3 `CONFIG_GPIO_NCT38XX_ALERT`

**提示（Prompt）**：NCT38XX GPIO 中断（Interrupt）

**说明（Help）**

在 NCT38XX 驱动中启用中断（Interrupt）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NCT38XX_GPIO_ALERT_ENABLED && CONFIG_GPIO_NCT38XX && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.nct38xx:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.nct38xx#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 基于 I2C 的 NCT38XX GPIO 芯片

**配置项引用（Symbol References）**：[`CONFIG_GPIO_NCT38XX`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_NCT38XX)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_NCT38XX_ALERT_INIT_PRIORITY"></a>

## 99.4 `CONFIG_GPIO_NCT38XX_ALERT_INIT_PRIORITY`

**提示（Prompt）**：NCT38XX GPIO 告警处理程序初始化优先级（Alert Handler Init Priority）

**说明（Help）**

NCT38XX 告警处理程序（Alert Handler）的初始化优先级（Initialization Priority）。它必须在告警 GPIO 设备初始化完成之后初始化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_NCT38XX_ALERT && CONFIG_GPIO_NCT38XX && CONFIG_GPIO
```

**默认值（Defaults）**

```text
84
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.nct38xx:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.nct38xx#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 基于 I2C 的 NCT38XX GPIO 芯片 → NCT38XX GPIO 中断（Interrupt）

**配置项引用（Symbol References）**：[`CONFIG_GPIO_NCT38XX_ALERT`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_NCT38XX_ALERT)、[`CONFIG_GPIO_NCT38XX`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_NCT38XX)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_NCT38XX_INIT_PRIORITY"></a>

## 99.5 `CONFIG_GPIO_NCT38XX_INIT_PRIORITY`

**提示（Prompt）**：NCT38XX GPIO 初始化优先级（Init Priority）

**说明（Help）**

NCT38XX GPIO 驱动的初始化优先级（Initialization Priority）。原文要求其优先级低于 `MFD_INIT_PRIORITY`。

> 译注：此处 `lower` 不应直接理解为数值更小。本快照中 `CONFIG_MFD_INIT_PRIORITY` 的默认值为 `80`，本项默认值为 `82`，对应本驱动在 MFD 之后初始化；修改配置时需保持所需的初始化先后关系。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_NCT38XX && CONFIG_GPIO
```

**默认值（Defaults）**

```text
82
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.nct38xx:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.nct38xx#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 基于 I2C 的 NCT38XX GPIO 芯片

**配置项引用（Symbol References）**：[`CONFIG_GPIO_NCT38XX`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_NCT38XX)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_NCT38XX_PORT_INIT_PRIORITY"></a>

## 99.6 `CONFIG_GPIO_NCT38XX_PORT_INIT_PRIORITY`

**提示（Prompt）**：NCT38XX GPIO 端口初始化优先级（Port Init Priority）

**说明（Help）**

NCT38XX GPIO 端口设备驱动的初始化优先级（Initialization Priority）。原文要求其优先级低于 `GPIO_NCT38XX_INIT_PRIORITY` 设备。

> 译注：本快照中父级 `CONFIG_GPIO_NCT38XX_INIT_PRIORITY` 默认值为 `82`，本端口项默认值为 `84`，对应端口在父级之后初始化。原文 `lower` 不能直接译成“数值更小”。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_NCT38XX && CONFIG_GPIO
```

**默认值（Defaults）**

```text
84
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.nct38xx:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.nct38xx#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 基于 I2C 的 NCT38XX GPIO 芯片

**配置项引用（Symbol References）**：[`CONFIG_GPIO_NCT38XX`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_NCT38XX)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_NEORV32"></a>

## 99.7 `CONFIG_GPIO_NEORV32`

**提示（Prompt）**：NEORV32 GPIO 驱动

**说明（Help）**

启用 NEORV32 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NEORV32_GPIO_ENABLED && CONFIG_SYSCON && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.neorv32:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.neorv32#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_SYSCON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYSCON)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_NPCX"></a>

## 99.8 `CONFIG_GPIO_NPCX`

**提示（Prompt）**：新唐（Nuvoton）NPCX 嵌入式控制器（Embedded Controller，EC）GPIO 驱动

**说明（Help）**

此选项启用 NPCX 系列处理器的 GPIO 驱动。原文接着说明：如果希望在 NPCX 微控制器（MCU）上使用串口（Serial Port），请选择 `y`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NPCX_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.npcx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.npcx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_NPM10XX"></a>

## 99.9 `CONFIG_GPIO_NPM10XX`

**提示（Prompt）**：nPM10xx GPIO 驱动

**说明（Help）**

启用 nPM10xx GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NPM10XX_GPIO_ENABLED && DT_HAS_NORDIC_NPM10XX_ENABLED && CONFIG_GPIO
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

**定义位置（Location）**：[`drivers/gpio/Kconfig.npm10xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.npm10xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_GPIO_NPM10XX_INIT_PRIORITY"></a>

## 99.10 `CONFIG_GPIO_NPM10XX_INIT_PRIORITY`

**提示（Prompt）**：nPM10xx GPIO 驱动初始化优先级（Initialization Priority）

**说明（Help）**

nPM10xx GPIO 驱动的初始化优先级（Initialization Priority）。数值必须大于多功能设备（MFD）的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_NPM10XX && CONFIG_GPIO
```

**默认值（Defaults）**

```text
85
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.npm10xx:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.npm10xx#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → nPM10xx GPIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO_NPM10XX`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_NPM10XX)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_NPM13XX"></a>

## 99.11 `CONFIG_GPIO_NPM13XX`

**提示（Prompt）**：nPM13xx GPIO 驱动

**说明（Help）**

启用 nPM13xx GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_NORDIC_NPM1300_GPIO_ENABLED || DT_HAS_NORDIC_NPM1304_GPIO_ENABLED) && CONFIG_GPIO
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

**定义位置（Location）**：[`drivers/gpio/Kconfig.npm13xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.npm13xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_GPIO_NPM13XX_INIT_PRIORITY"></a>

## 99.12 `CONFIG_GPIO_NPM13XX_INIT_PRIORITY`

**提示（Prompt）**：nPM13xx GPIO 驱动初始化优先级（Initialization Priority）

**说明（Help）**

nPM13xx GPIO 驱动的初始化优先级（Initialization Priority）。数值必须大于 I2C 控制器的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_NPM13XX && CONFIG_GPIO
```

**默认值（Defaults）**

```text
85
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.npm13xx:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.npm13xx#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → nPM13xx GPIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO_NPM13XX`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_NPM13XX)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_NPM2100"></a>

## 99.13 `CONFIG_GPIO_NPM2100`

**提示（Prompt）**：nPM2100 GPIO 驱动

**说明（Help）**

启用 nPM2100 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NPM2100_GPIO_ENABLED && CONFIG_GPIO
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

**定义位置（Location）**：[`drivers/gpio/Kconfig.npm2100:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.npm2100#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_GPIO_NPM2100_INIT_PRIORITY"></a>

## 99.14 `CONFIG_GPIO_NPM2100_INIT_PRIORITY`

**提示（Prompt）**：nPM2100 GPIO 驱动初始化优先级（Initialization Priority）

**说明（Help）**

nPM2100 GPIO 驱动的初始化优先级（Initialization Priority）。数值必须大于 I2C 控制器的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_NPM2100 && CONFIG_GPIO
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.npm2100:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.npm2100#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → nPM2100 GPIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO_NPM2100`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_NPM2100)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_NPM6001"></a>

## 99.15 `CONFIG_GPIO_NPM6001`

**提示（Prompt）**：nPM6001 GPIO 驱动

**说明（Help）**

启用 nPM6001 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NPM6001_GPIO_ENABLED && CONFIG_GPIO
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

**定义位置（Location）**：[`drivers/gpio/Kconfig.npm6001:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.npm6001#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_GPIO_NPM6001_INIT_PRIORITY"></a>

## 99.16 `CONFIG_GPIO_NPM6001_INIT_PRIORITY`

**提示（Prompt）**：nPM6001 GPIO 驱动初始化优先级（Initialization Priority）

**说明（Help）**

nPM6001 GPIO 驱动的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_NPM6001 && CONFIG_GPIO
```

**默认值（Defaults）**

```text
85
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.npm6001:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.npm6001#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → nPM6001 GPIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO_NPM6001`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_NPM6001)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_NRFX"></a>

## 99.17 `CONFIG_GPIO_NRFX`

**提示（Prompt）**：nRF GPIO 驱动

**说明（Help）**

为 nRF 微控制器（MCU）系列启用 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.nrfx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.nrfx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_NRFX_INTERRUPT"></a>

## 99.18 `CONFIG_GPIO_NRFX_INTERRUPT`

**提示（Prompt）**：中断支持（Interrupt Support）

**说明（Help）**

对于不需要 GPIO 中断（Interrupt）的应用程序，可通过此选项禁用 GPIO 中断支持，以显著降低内存占用（Memory Footprint）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_NRFX && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_GPIOTE
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.nrfx:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.nrfx#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → nRF GPIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO_NRFX`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_NRFX)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_NRFX_GPIOTE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_GPIOTE)。

<a id="CONFIG_GPIO_NUMAKER"></a>

## 99.19 `CONFIG_GPIO_NUMAKER`

**提示（Prompt）**：新唐（Nuvoton）NuMaker 微控制器（MCU）GPIO 驱动

**说明（Help）**

此选项启用新唐（Nuvoton）NuMaker 系列处理器的 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NUMAKER_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_NUMAKER_GPIO
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.numaker:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.numaker#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_HAS_NUMAKER_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NUMAKER_GPIO)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_GPIO_NUMICRO"></a>

## 99.20 `CONFIG_GPIO_NUMICRO`

**提示（Prompt）**：新唐（Nuvoton）NuMicro GPIO 驱动

**说明（Help）**

启用 NuMicro 系列处理器的 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NUMICRO_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.numicro:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.numicro#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_GPIO_NXP_SIUL2"></a>

## 99.21 `CONFIG_GPIO_NXP_SIUL2`

**提示（Prompt）**：NXP SIUL2 GPIO 驱动

**说明（Help）**

启用 NXP SIUL2 的 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_SIUL2_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NOCACHE_MEMORY if CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.nxp_siul2:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.nxp_siul2#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_GPIO_PCA953X"></a>

## 99.22 `CONFIG_GPIO_PCA953X`

**提示（Prompt）**：PCA953X I2C GPIO 芯片

**说明（Help）**

启用 PCA953X I2C GPIO 芯片的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_TCA9538_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.pca953x:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.pca953x#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_GPIO_PCA953X_INIT_PRIORITY"></a>

## 99.23 `CONFIG_GPIO_PCA953X_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_PCA953X && CONFIG_GPIO
```

**默认值（Defaults）**

```text
CONFIG_I2C_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.pca953x:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.pca953x#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → PCA953X I2C GPIO 芯片

**配置项引用（Symbol References）**：[`CONFIG_GPIO_PCA953X`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_PCA953X)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C_INIT_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_INIT_PRIORITY)。

<a id="CONFIG_GPIO_PCA95XX"></a>

## 99.24 `CONFIG_GPIO_PCA95XX`

**提示（Prompt）**：基于 I2C 的 PCA95XX GPIO 芯片

**说明（Help）**

启用基于 I2C 的 PCA95XX GPIO 芯片的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_PCA95XX_ENABLED && CONFIG_I2C && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.pca95xx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.pca95xx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_PCA95XX_INIT_PRIORITY"></a>

## 99.25 `CONFIG_GPIO_PCA95XX_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_PCA95XX && CONFIG_GPIO
```

**默认值（Defaults）**

```text
CONFIG_I2C_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.pca95xx:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.pca95xx#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 基于 I2C 的 PCA95XX GPIO 芯片

**配置项引用（Symbol References）**：[`CONFIG_GPIO_PCA95XX`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_PCA95XX)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C_INIT_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_INIT_PRIORITY)。

<a id="CONFIG_GPIO_PCA95XX_INTERRUPT"></a>

## 99.26 `CONFIG_GPIO_PCA95XX_INTERRUPT`

**提示（Prompt）**：启用中断（Interrupt Enable）

**说明（Help）**

在 PCA95XX 驱动中启用中断（Interrupt）支持。受其设计限制，PCA95XX 无法可靠检测短脉冲中断（Short-Pulse Interrupt）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_PCA95XX && CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.pca95xx:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.pca95xx#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 基于 I2C 的 PCA95XX GPIO 芯片

**配置项引用（Symbol References）**：[`CONFIG_GPIO_PCA95XX`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_PCA95XX)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_PCAL64XXA"></a>

## 99.27 `CONFIG_GPIO_PCAL64XXA`

**提示（Prompt）**：PCAL64XXA I2C GPIO 芯片

**说明（Help）**

启用 PCAL64XXA I2C GPIO 芯片的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_NXP_PCAL6408A_ENABLED || DT_HAS_NXP_PCAL6416A_ENABLED) && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.pcal64xxa:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.pcal64xxa#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_GPIO_PCAL64XXA_INIT_PRIORITY"></a>

## 99.28 `CONFIG_GPIO_PCAL64XXA_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_PCAL64XXA && CONFIG_GPIO
```

**默认值（Defaults）**

```text
70
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.pcal64xxa:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.pcal64xxa#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → PCAL64XXA I2C GPIO 芯片

**配置项引用（Symbol References）**：[`CONFIG_GPIO_PCAL64XXA`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_PCAL64XXA)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_PCAL9722"></a>

## 99.29 `CONFIG_GPIO_PCAL9722`

**提示（Prompt）**：PCAL9722 SPI GPIO 芯片

**说明（Help）**

启用 PCAL9722 SPI GPIO 芯片的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_PCAL9722_ENABLED && CONFIG_SPI && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.pcal9722:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.pcal9722#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_PCAL9722_INIT_PRIORITY"></a>

## 99.30 `CONFIG_GPIO_PCAL9722_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

PCAL9722 设备驱动的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_PCAL9722 && CONFIG_GPIO
```

**默认值（Defaults）**

```text
70
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.pcal9722:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.pcal9722#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → PCAL9722 SPI GPIO 芯片

**配置项引用（Symbol References）**：[`CONFIG_GPIO_PCAL9722`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_PCAL9722)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_PCA_SERIES"></a>

## 99.31 `CONFIG_GPIO_PCA_SERIES`

**提示（Prompt）**：基于 I2C 的 PCA_SERIES GPIO 芯片

**说明（Help）**

启用基于 I2C 的 PCA_SERIES GPIO 芯片的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_NXP_PCA9538_ENABLED || DT_HAS_NXP_PCA9539_ENABLED || DT_HAS_NXP_PCA9554_ENABLED || DT_HAS_NXP_PCA9555_ENABLED || DT_HAS_NXP_PCA6408_ENABLED || DT_HAS_NXP_PCA6416_ENABLED || DT_HAS_NXP_PCAL9538_ENABLED || DT_HAS_NXP_PCAL9539_ENABLED || DT_HAS_NXP_PCAL6408_ENABLED || DT_HAS_NXP_PCAL6416_ENABLED || DT_HAS_NXP_PCAL6524_ENABLED || DT_HAS_NXP_PCAL6534_ENABLED) && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.pca_series:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.pca_series#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_GPIO_PCA_SERIES_CACHE_ALL"></a>

## 99.32 `CONFIG_GPIO_PCA_SERIES_CACHE_ALL`

**提示（Prompt）**：缓存全部寄存器（Cache All Registers）

**说明（Help）**

在 RAM 中缓存（Cache）全部寄存器，以加快配置，默认启用。禁用时，仅缓存输出寄存器（Output Register）；对于没有中断状态（Interrupt Status）的器件，还会缓存输入状态（Input State）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_PCA_SERIES && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.pca_series:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.pca_series#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 基于 I2C 的 PCA_SERIES GPIO 芯片

**配置项引用（Symbol References）**：[`CONFIG_GPIO_PCA_SERIES`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_PCA_SERIES)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_PCA_SERIES_INIT_PRIORITY"></a>

## 99.33 `CONFIG_GPIO_PCA_SERIES_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_PCA_SERIES && CONFIG_GPIO
```

**默认值（Defaults）**

```text
CONFIG_I2C_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.pca_series:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.pca_series#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 基于 I2C 的 PCA_SERIES GPIO 芯片

**配置项引用（Symbol References）**：[`CONFIG_GPIO_PCA_SERIES`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_PCA_SERIES)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C_INIT_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_INIT_PRIORITY)。

<a id="CONFIG_GPIO_PCA_SERIES_INTERRUPT"></a>

## 99.34 `CONFIG_GPIO_PCA_SERIES_INTERRUPT`

**提示（Prompt）**：启用中断（Interrupt Enable）

**说明（Help）**

在 PCA_SERIES 驱动中启用中断（Interrupt）支持。受其设计限制，PCA_SERIES 无法可靠检测短脉冲中断（Short-Pulse Interrupt）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_PCA_SERIES && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.pca_series:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.pca_series#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 基于 I2C 的 PCA_SERIES GPIO 芯片

**配置项引用（Symbol References）**：[`CONFIG_GPIO_PCA_SERIES`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_PCA_SERIES)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_PCF857X"></a>

## 99.35 `CONFIG_GPIO_PCF857X`

**提示（Prompt）**：PCF857X I2C GPIO 芯片

**说明（Help）**

启用 PCF857X I2C GPIO 芯片的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_PCF857X_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.pcf857x:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.pcf857x#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_GPIO_PCF857X_INIT_PRIORITY"></a>

## 99.36 `CONFIG_GPIO_PCF857X_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_PCF857X && CONFIG_GPIO
```

**默认值（Defaults）**

```text
CONFIG_I2C_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.pcf857x:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.pcf857x#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → PCF857X I2C GPIO 芯片

**配置项引用（Symbol References）**：[`CONFIG_GPIO_PCF857X`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_PCF857X)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C_INIT_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_INIT_PRIORITY)。

<a id="CONFIG_GPIO_PI4IOE5V6408"></a>

## 99.37 `CONFIG_GPIO_PI4IOE5V6408`

**提示（Prompt）**：PI4IOE5V6408 I2C GPIO 扩展器（GPIO Expander）

**说明（Help）**

启用 Diodes/Pericom PI4IOE5V6408 8 位 I2C 总线 I/O 扩展器（I/O Expander）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_DIODES_PI4IOE5V6408_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.pi4ioe5v6408:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.pi4ioe5v6408#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_GPIO_PI4IOE5V6408_INIT_PRIORITY"></a>

## 99.38 `CONFIG_GPIO_PI4IOE5V6408_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动的初始化优先级（Initialization Priority）。数值必须大于 `CONFIG_I2C_INIT_PRIORITY`，以确保 I2C 总线可用；还必须大于承载 `INT` 线路的任一 GPIO 控制器的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_PI4IOE5V6408 && CONFIG_GPIO
```

**默认值（Defaults）**

```text
70
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.pi4ioe5v6408:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.pi4ioe5v6408#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → PI4IOE5V6408 I2C GPIO 扩展器（GPIO Expander）

**配置项引用（Symbol References）**：[`CONFIG_GPIO_PI4IOE5V6408`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_PI4IOE5V6408)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_PI4IOE5V6408_POLL_PERIOD_MS"></a>

## 99.39 `CONFIG_GPIO_PI4IOE5V6408_POLL_PERIOD_MS`

**提示（Prompt）**：非中断驱动时的轮询周期（Polling Period），以毫秒为单位

**说明（Help）**

节点没有 `int-gpios` 属性时，驱动按此周期轮询芯片的输入寄存器（Input Register），以检测状态变化（Transition）。此项用于未描述可用 `INT` 线路的开发板；其他情况下忽略。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_PI4IOE5V6408 && CONFIG_GPIO
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.pi4ioe5v6408:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.pi4ioe5v6408#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → PI4IOE5V6408 I2C GPIO 扩展器（GPIO Expander）

**配置项引用（Symbol References）**：[`CONFIG_GPIO_PI4IOE5V6408`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_PI4IOE5V6408)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_PSOC6"></a>

## 99.40 `CONFIG_GPIO_PSOC6`

**提示（Prompt）**：赛普拉斯（Cypress）PSoC 6 GPIO 驱动

**说明（Help）**

启用赛普拉斯（Cypress）PSoC 6 GPIO 控制器（Controller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_CYPRESS_PSOC6_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.psoc6:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.psoc6#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_RASPBERRYPI_BCM283X"></a>

## 99.41 `CONFIG_GPIO_RASPBERRYPI_BCM283X`

**提示（Prompt）**：树莓派（Raspberry Pi）BCM283x GPIO 扩展器驱动（GPIO Expander Driver）

**说明（Help）**

启用树莓派（Raspberry Pi）BCM283x GPIO 扩展器（GPIO Expander）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RASPBERRYPI_BCM283X_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.rpi_bcm283x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.rpi_bcm283x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_RASPBERRYPI_BCM283X_INIT_PRIORITY"></a>

## 99.42 `CONFIG_GPIO_RASPBERRYPI_BCM283X_INIT_PRIORITY`

**提示（Prompt）**：树莓派（Raspberry Pi）BCM283x GPIO 扩展器驱动初始化优先级（Init Priority）

**说明（Help）**

数值必须大于 `CONFIG_RASPBERRYPI_FIRMWARE_INIT_PRIORITY`，也就是更晚初始化，以确保本驱动初始化之前固件接口（Firmware Interface）已经就绪。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_RASPBERRYPI_BCM283X && CONFIG_GPIO
```

**默认值（Defaults）**

```text
46
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.rpi_bcm283x:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.rpi_bcm283x#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 树莓派（Raspberry Pi）BCM283x GPIO 扩展器驱动（GPIO Expander Driver）

**配置项引用（Symbol References）**：[`CONFIG_GPIO_RASPBERRYPI_BCM283X`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_RASPBERRYPI_BCM283X)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_RA_HAS_VBTICTLR"></a>

## 99.43 `CONFIG_GPIO_RA_HAS_VBTICTLR`

**提示（Prompt）**：支持 VBATT 输入控制（Input Control）

**说明（Help）**

对于支持 VBATT 输入控制（Input Control）的瑞萨（Renesas）RA，启用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_RA_IOPORT && CONFIG_GPIO
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_RA4E1
CONFIG_SOC_SERIES_RA4M1
CONFIG_SOC_SERIES_RA4M2
CONFIG_SOC_SERIES_RA4M3
CONFIG_SOC_SERIES_RA4W1
CONFIG_SOC_SERIES_RA6E1
CONFIG_SOC_SERIES_RA6M1
CONFIG_SOC_SERIES_RA6M2
CONFIG_SOC_SERIES_RA6M3
CONFIG_SOC_SERIES_RA6M4
CONFIG_SOC_SERIES_RA6M5
CONFIG_SOC_SERIES_RA8D1
CONFIG_SOC_R7KA8D2KFLCAC_CM85
CONFIG_SOC_SERIES_RA8E1
CONFIG_SOC_SERIES_RA8M1
CONFIG_SOC_R7KA8M2JFLCAC_CM85
CONFIG_SOC_R7KA8P1KFLCAC_CM85
CONFIG_SOC_SERIES_RA8T1
CONFIG_SOC_R7KA8T2LFLCAC_CM85
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.renesas_ra_ioport:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.renesas_ra_ioport#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 瑞萨（Renesas）RA GPIO I/O 端口驱动（I/O Port Driver）

**配置项引用（Symbol References）**：[`CONFIG_GPIO_RA_IOPORT`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_RA_IOPORT)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_SOC_SERIES_RA4E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4E1)、[`CONFIG_SOC_SERIES_RA4M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M1)、[`CONFIG_SOC_SERIES_RA4M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M2)、[`CONFIG_SOC_SERIES_RA4M3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M3)、[`CONFIG_SOC_SERIES_RA4W1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4W1)、[`CONFIG_SOC_SERIES_RA6E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6E1)、[`CONFIG_SOC_SERIES_RA6M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M1)、[`CONFIG_SOC_SERIES_RA6M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M2)、[`CONFIG_SOC_SERIES_RA6M3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M3)、[`CONFIG_SOC_SERIES_RA6M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M4)、[`CONFIG_SOC_SERIES_RA6M5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M5)、[`CONFIG_SOC_SERIES_RA8D1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8D1)、[`CONFIG_SOC_R7KA8D2KFLCAC_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7KA8D2KFLCAC_CM85)、[`CONFIG_SOC_SERIES_RA8E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8E1)、[`CONFIG_SOC_SERIES_RA8M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8M1)、[`CONFIG_SOC_R7KA8M2JFLCAC_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7KA8M2JFLCAC_CM85)、[`CONFIG_SOC_R7KA8P1KFLCAC_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7KA8P1KFLCAC_CM85)、[`CONFIG_SOC_SERIES_RA8T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8T1)、[`CONFIG_SOC_R7KA8T2LFLCAC_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7KA8T2LFLCAC_CM85)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_R7KA8D2KFLCAC_CM85`、`CONFIG_SOC_R7KA8M2JFLCAC_CM85`、`CONFIG_SOC_R7KA8P1KFLCAC_CM85`、`CONFIG_SOC_R7KA8T2LFLCAC_CM85`。

<a id="CONFIG_GPIO_RA_IOPORT"></a>

## 99.44 `CONFIG_GPIO_RA_IOPORT`

**提示（Prompt）**：瑞萨（Renesas）RA GPIO I/O 端口驱动（I/O Port Driver）

**说明（Help）**

启用瑞萨（Renesas）RA GPIO I/O 端口驱动（I/O Port Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_GPIO_IOPORT_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.renesas_ra_ioport:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.renesas_ra_ioport#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_GPIO_RCAR"></a>

## 99.45 `CONFIG_GPIO_RCAR`

**提示（Prompt）**：瑞萨（Renesas）R-Car GPIO

**说明（Help）**

启用瑞萨（Renesas）R-Car GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RCAR_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.rcar:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.rcar#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_GPIO_RENESAS_RX"></a>

## 99.46 `CONFIG_GPIO_RENESAS_RX`

**提示（Prompt）**：瑞萨（Renesas）RX GPIO 驱动

**说明（Help）**

启用瑞萨（Renesas）RX GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RX_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.renesas_rx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.renesas_rx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_GPIO_RENESAS_RZ"></a>

## 99.47 `CONFIG_GPIO_RENESAS_RZ`

**提示（Prompt）**：瑞萨（Renesas）RZ 系列 GPIO 驱动

**说明（Help）**

启用瑞萨（Renesas）RZ 系列 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RZ_FSP_IOPORT
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.renesas_rz:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.renesas_rz#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_USE_RZ_FSP_IOPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_IOPORT)。

<a id="CONFIG_GPIO_RENESAS_RZA2M"></a>

## 99.48 `CONFIG_GPIO_RENESAS_RZA2M`

**提示（Prompt）**：瑞萨（Renesas）RZ/A2M GPIO

**说明（Help）**

启用瑞萨（Renesas）RZ/A2M GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZA2M_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.renesas_rza2m:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.renesas_rza2m#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_GPIO_RP1"></a>

## 99.49 `CONFIG_GPIO_RP1`

**提示（Prompt）**：RP1 外设控制器 GPIO 驱动（Peripheral Controller GPIO Driver）

**说明（Help）**

启用 RP1 外设控制器（Peripheral Controller）上 GPIO 组（Bank）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RASPBERRYPI_RP1_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.rp1:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.rp1#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_RPI_PICO"></a>

## 99.50 `CONFIG_GPIO_RPI_PICO`

**提示（Prompt）**：树莓派（Raspberry Pi）Pico GPIO 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RASPBERRYPI_PICO_GPIO_PORT_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PICOSDK_USE_GPIO
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.rpi_pico:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.rpi_pico#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_PICOSDK_USE_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PICOSDK_USE_GPIO)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_GPIO_RT1718S"></a>

## 99.51 `CONFIG_GPIO_RT1718S`

**提示（Prompt）**：带 GPIO 的、基于 I2C 的 RT1718S Type-C 端口控制器（TCPC）芯片

**说明（Help）**

启用基于 I2C 的 RT1718S Type-C 端口控制器（TCPC）芯片的 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RICHTEK_RT1718S_GPIO_PORT_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.rt1718s:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.rt1718s#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_RT1718S_INTERRUPT"></a>

## 99.52 `CONFIG_GPIO_RT1718S_INTERRUPT`

**提示（Prompt）**：RT1718S 告警处理程序（Alert Handler）

**说明（Help）**

启用通过芯片连接出的 GPIO 中断处理 RT1718S 告警（Alert）的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_RT1718S && CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.rt1718s:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.rt1718s#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 带 GPIO 的、基于 I2C 的 RT1718S Type-C 端口控制器（TCPC）芯片

**配置项引用（Symbol References）**：[`CONFIG_GPIO_RT1718S`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_RT1718S)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_RT1718S_PORT_INIT_PRIORITY"></a>

## 99.53 `CONFIG_GPIO_RT1718S_PORT_INIT_PRIORITY`

**提示（Prompt）**：RT1718S GPIO 端口初始化优先级（Port Init Priority）

**说明（Help）**

RT1718S GPIO 驱动的初始化优先级（Initialization Priority）。原文要求其优先级低于 I2C 及 `RT1718S_INIT_PRIORITY` 设备。

> 译注：这里的 `lower` 指初始化先后，不应直接解释为数值更小。本快照中 `CONFIG_RT1718S_INIT_PRIORITY` 默认值为 `60`，本端口项默认值为 `61`，对应 GPIO 端口在 RT1718S 设备之后初始化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_RT1718S && CONFIG_GPIO
```

**默认值（Defaults）**

```text
61
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.rt1718s:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.rt1718s#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 带 GPIO 的、基于 I2C 的 RT1718S Type-C 端口控制器（TCPC）芯片

**配置项引用（Symbol References）**：[`CONFIG_GPIO_RT1718S`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_RT1718S)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_RTS5817"></a>

## 99.54 `CONFIG_GPIO_RTS5817`

**提示（Prompt）**：RTS5817 GPIO 驱动

**说明（Help）**

启用 RTS5817 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_RTS5817_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.rts5817:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.rts5817#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_RTS5912"></a>

## 99.55 `CONFIG_GPIO_RTS5912`

**提示（Prompt）**：瑞昱（Realtek）嵌入式控制器（Embedded Controller，EC）GPIO 驱动

**说明（Help）**

启用瑞昱（Realtek）GPIO 控制器（Controller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RTS5912 && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y if DT_HAS_REALTEK_RTS5912_GPIO_ENABLED
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.rts5912:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.rts5912#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RTS5912`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTS5912)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_RV32M1"></a>

## 99.56 `CONFIG_GPIO_RV32M1`

**提示（Prompt）**：RV32M1 GPIO 驱动

**说明（Help）**

启用 RV32M1 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_OPENISA_RV32M1_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.rv32m1:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.rv32m1#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_RX_IOPORT"></a>

## 99.57 `CONFIG_GPIO_RX_IOPORT`

**提示（Prompt）**：瑞萨（Renesas）RX GPIO I/O 端口驱动（I/O Port Driver）

**说明（Help）**

启用瑞萨（Renesas）RX GPIO I/O 端口驱动（I/O Port Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RX_GPIO_IOPORT_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.renesas_rx_ioport:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.renesas_rx_ioport#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_GPIO_RZT2M"></a>

## 99.58 `CONFIG_GPIO_RZT2M`

**提示（Prompt）**：瑞萨（Renesas）RZT2M GPIO

**说明（Help）**

启用瑞萨（Renesas）RZT2M GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZT2M_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.rzt2m:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.rzt2m#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_SAM"></a>

## 99.59 `CONFIG_GPIO_SAM`

**提示（Prompt）**：Atmel SAM GPIO（PORT）驱动

**说明（Help）**

启用 Atmel SAM `PORT` GPIO 控制器（Controller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.sam:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.sam#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_SAM0"></a>

## 99.60 `CONFIG_GPIO_SAM0`

**提示（Prompt）**：Atmel SAM0 GPIO（PORT）驱动

**说明（Help）**

启用 Atmel SAM0 `PORT` GPIO 控制器（Controller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM0_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.sam0:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.sam0#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_SAM4L"></a>

## 99.61 `CONFIG_GPIO_SAM4L`

**提示（Prompt）**：Atmel SAM4L GPIO（PORT）驱动

**说明（Help）**

启用 Atmel SAM4L `PORT` GPIO 控制器（Controller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM4L_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.sam:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.sam#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_SAM_PIO4"></a>

## 99.62 `CONFIG_GPIO_SAM_PIO4`

**提示（Prompt）**：Microchip SAM PIO4 GPIO 驱动

**说明（Help）**

Microchip 并行输入/输出控制器（Parallel Input/Output Controller）用于 SAMA5D2 和 SAMA7G5 SoC 系列。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_SAM_PIO4_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.sam:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.sam#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_SC18IM704"></a>

## 99.63 `CONFIG_GPIO_SC18IM704`

**提示（Prompt）**：NXP SC18IM704 GPIO 控制器驱动（Controller Driver）

**说明（Help）**

启用 NXP SC18IM704 GPIO 控制器驱动（Controller Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_SC18IM704 && DT_HAS_NXP_SC18IM704_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.sc18im704:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.sc18im704#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_SC18IM704`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_SC18IM704)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_SC18IM704_INIT_PRIORITY"></a>

## 99.64 `CONFIG_GPIO_SC18IM704_INIT_PRIORITY`

**提示（Prompt）**：SC18IM704 GPIO 初始化优先级（Init Priority）

**说明（Help）**

SC18IM704 GPIO 控制器的初始化优先级（Initialization Priority）。注意：数值必须大于父级 SC18IM704 桥接器（Bridge）的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_SC18IM704 && CONFIG_GPIO
```

**默认值（Defaults）**

```text
52
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.sc18im704:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.sc18im704#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → NXP SC18IM704 GPIO 控制器驱动（Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_GPIO_SC18IM704`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_SC18IM704)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_SC18IS606"></a>

## 99.65 `CONFIG_GPIO_SC18IS606`

**提示（Prompt）**：NXP SC18IS606 GPIO 控制器驱动（Controller Driver）

**说明（Help）**

启用 NXP SC18IS606 GPIO 控制器驱动（Controller Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_SC18IS606_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.sc18is606:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.sc18is606#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_GPIO_SC18IS606_INIT_PRIORITY"></a>

## 99.66 `CONFIG_GPIO_SC18IS606_INIT_PRIORITY`

**提示（Prompt）**：SC18IS606 GPIO 初始化优先级（Init Priority）

**说明（Help）**

SC18IS606 GPIO 控制器的初始化优先级（Init Priority）。注意：数值必须大于父级 SC18IS606 桥接器（Bridge）的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_SC18IS606 && CONFIG_GPIO
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.sc18is606:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.sc18is606#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → NXP SC18IS606 GPIO 控制器驱动（Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_GPIO_SC18IS606`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_SC18IS606)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_SEDI"></a>

## 99.67 `CONFIG_GPIO_SEDI`

**提示（Prompt）**：SEDI GPIO 驱动

**说明（Help）**

此选项启用 Intel SEDI GPIO 驱动。这是一个适配层驱动（Shim Driver），构建于 `hal-intel` 模块中的 SEDI 裸机 GPIO 驱动（Bare-Metal GPIO Driver）之上。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_SEDI_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.sedi:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.sedi#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_SF32LB"></a>

## 99.68 `CONFIG_GPIO_SF32LB`

**提示（Prompt）**：思澈（SiFli）SF32LB GPIO 驱动

**说明（Help）**

为思澈（SiFli）SF32LB 启用 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFLI_SF32LB_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.sf32lb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.sf32lb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_SHELL"></a>

## 99.69 `CONFIG_GPIO_SHELL`

**提示（Prompt）**：GPIO 命令行（Shell）

**说明（Help）**

启用 GPIO 命令行（Shell），用于测试。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/gpio/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_SHELL_BLINK_CMD"></a>

## 99.70 `CONFIG_GPIO_SHELL_BLINK_CMD`

**提示（Prompt）**：GPIO 命令行闪烁命令（Shell Blink Command）

**说明（Help）**

启用 GPIO 命令行闪烁命令（Shell Blink Command），使用户可通过命令行以 1 Hz 频率让引脚“闪烁”（Blink）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_SHELL && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → GPIO 命令行（Shell）

**配置项引用（Symbol References）**：[`CONFIG_GPIO_SHELL`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_SHELL)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_SHELL_INFO_CMD"></a>

## 99.71 `CONFIG_GPIO_SHELL_INFO_CMD`

**提示（Prompt）**：GPIO 命令行信息命令（Shell Info Command）

**说明（Help）**

启用 GPIO 命令行信息命令（Shell Information Command）。此命令向用户提供 GPIO 控制器保留引脚（Reserved Pin）和线路名称（Line Name）的额外信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_SHELL && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → GPIO 命令行（Shell）

**配置项引用（Symbol References）**：[`CONFIG_GPIO_SHELL`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_SHELL)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_SHELL_TOGGLE_CMD"></a>

## 99.72 `CONFIG_GPIO_SHELL_TOGGLE_CMD`

**提示（Prompt）**：GPIO 命令行翻转命令（Shell Toggle Command）

**说明（Help）**

启用 GPIO 命令行翻转命令（Shell Toggle Command）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_SHELL && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → GPIO 命令行（Shell）

**配置项引用（Symbol References）**：[`CONFIG_GPIO_SHELL`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_SHELL)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_SI32"></a>

## 99.73 `CONFIG_GPIO_SI32`

**提示（Prompt）**：Si32 微控制器（MCU）系列 GPIO 驱动

**说明（Help）**

为 Si32 微控制器（MCU）系列启用 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SI32_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.si32:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.si32#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_SIFIVE"></a>

## 99.74 `CONFIG_GPIO_SIFIVE`

**提示（Prompt）**：SiFive Freedom 处理器（Processor）GPIO 驱动

**说明（Help）**

启用 SiFive Freedom GPIO 控制器（Controller）的驱动。不确定时选择 `n`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFIVE_GPIO0_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.sifive:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.sifive#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_SILABS"></a>

## 99.75 `CONFIG_GPIO_SILABS`

**提示（Prompt）**：Silabs GPIO 驱动

**说明（Help）**

启用 Silabs GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_GPIO_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SILABS_SISDK_GPIO
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.silabs:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.silabs#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_SILABS_SISDK_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_GPIO)。

<a id="CONFIG_GPIO_SILABS_COMMON_INIT_PRIORITY"></a>

## 99.76 `CONFIG_GPIO_SILABS_COMMON_INIT_PRIORITY`

**提示（Prompt）**：通用初始化优先级（Common Initialization Priority）

**说明（Help）**

主 GPIO 控制器（Main GPIO Controller）必须先于各 GPIO 本身初始化。通常 `GPIO_INIT_PRIORITY - 1` 是合适的值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_SILABS && CONFIG_GPIO
```

**默认值（Defaults）**

```text
39
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.silabs:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.silabs#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → Silabs GPIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO_SILABS`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_SILABS)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_SILABS_SIWX91X"></a>

## 99.77 `CONFIG_GPIO_SILABS_SIWX91X`

**提示（Prompt）**：Silabs SiWx91x GPIO 驱动

**说明（Help）**

启用 Silabs SiWx91x SoC 系列的高功耗（HP）/超低功耗（ULP）GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SIWX91X_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.siwx91x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.siwx91x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_SILABS_SIWX91X_COMMON_INIT_PRIORITY"></a>

## 99.78 `CONFIG_GPIO_SILABS_SIWX91X_COMMON_INIT_PRIORITY`

**提示（Prompt）**：通用初始化优先级（Common Initialization Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_SILABS_SIWX91X && CONFIG_GPIO
```

**默认值（Defaults）**

```text
39
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.siwx91x:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.siwx91x#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → Silabs SiWx91x GPIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO_SILABS_SIWX91X`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_SILABS_SIWX91X)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_SILABS_SIWX91X_UULP"></a>

## 99.79 `CONFIG_GPIO_SILABS_SIWX91X_UULP`

**提示（Prompt）**：Silabs SiWx91x UULP GPIO 驱动

**说明（Help）**

启用 Silabs SiWx91x SoC 系列的 UULP GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SIWX91X_GPIO_UULP_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.siwx91x:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.siwx91x#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_SMARTBOND"></a>

## 99.80 `CONFIG_GPIO_SMARTBOND`

**提示（Prompt）**：瑞萨（Renesas）SmartBond™ GPIO 驱动

**说明（Help）**

为瑞萨（Renesas）SmartBond™ 微控制器（MCU）系列启用 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_SMARTBOND_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.smartbond:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.smartbond#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_SN74HC595"></a>

## 99.81 `CONFIG_GPIO_SN74HC595`

**提示（Prompt）**：将 SN74HC595 移位寄存器（Shift Register）用作 GPIO 扩展器（GPIO Expander）

**说明（Help）**

将 SN74HC595 用作 GPIO 扩展器（GPIO Expander）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_SN74HC595_ENABLED && CONFIG_SPI && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.sn74hc595:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.sn74hc595#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_SN74HC595_INIT_PRIORITY"></a>

## 99.82 `CONFIG_GPIO_SN74HC595_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_SN74HC595 && CONFIG_GPIO
```

**默认值（Defaults）**

```text
71
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.sn74hc595:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.sn74hc595#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 将 SN74HC595 移位寄存器（Shift Register）用作 GPIO 扩展器（GPIO Expander）

**配置项引用（Symbol References）**：[`CONFIG_GPIO_SN74HC595`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_SN74HC595)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_SNPS_CREG"></a>

## 99.83 `CONFIG_GPIO_SNPS_CREG`

**提示（Prompt）**：SNPS CREG GPIO

**说明（Help）**

启用 SNPS CREG GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SNPS_CREG_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.creg_gpio:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.creg_gpio#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_STELLARIS"></a>

## 99.84 `CONFIG_GPIO_STELLARIS`

**提示（Prompt）**：TI Stellaris GPIO 驱动

**说明（Help）**

启用 Stellaris GPIO 控制器（Controller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_STELLARIS_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.stellaris:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.stellaris#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_STM32"></a>

## 99.85 `CONFIG_GPIO_STM32`

**提示（Prompt）**：STM32 微控制器（MCU）系列 GPIO 驱动

**说明（Help）**

为 STM32 微控制器（MCU）系列启用 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ST_STM32_GPIO_ENABLED || DT_HAS_ST_STM32MP2_GPIO_ENABLED) && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_STM32_GPIOPORT_MGR
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.stm32:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.stm32#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_STM32_GPIOPORT_MGR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STM32_GPIOPORT_MGR)。

<a id="CONFIG_GPIO_STMPE1600"></a>

## 99.86 `CONFIG_GPIO_STMPE1600`

**提示（Prompt）**：基于 I2C 的 STMPE1600 GPIO 芯片

**说明（Help）**

启用基于 I2C 的 STMPE1600 GPIO 芯片的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STMPE1600_ENABLED && CONFIG_I2C && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.stmpe1600:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.stmpe1600#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_STMPE1600_INIT_PRIORITY"></a>

## 99.87 `CONFIG_GPIO_STMPE1600_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_STMPE1600 && CONFIG_GPIO
```

**默认值（Defaults）**

```text
70
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.stmpe1600:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.stmpe1600#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 基于 I2C 的 STMPE1600 GPIO 芯片

**配置项引用（Symbol References）**：[`CONFIG_GPIO_STMPE1600`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_STMPE1600)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_SX1509B"></a>

## 99.88 `CONFIG_GPIO_SX1509B`

**提示（Prompt）**：SX1509B I2C GPIO 芯片

**说明（Help）**

启用 SX1509B I2C GPIO 芯片的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SEMTECH_SX1509B_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.sx1509b:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.sx1509b#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_GPIO_SX1509B_DEBOUNCE_TIME"></a>

## 99.89 `CONFIG_GPIO_SX1509B_DEBOUNCE_TIME`

**提示（Prompt）**：消抖时间间隔（Debounce Time Interval）

**说明（Help）**

启用消抖（Debounce）时使用的时间间隔。值 `V` 先得到 `0.5 ms * 2^V`，再按 `2 MHz / fOSC` 的比例缩放。详情参见数据手册（Datasheet）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_SX1509B && CONFIG_GPIO
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 7]
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.sx1509b:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.sx1509b#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → SX1509B I2C GPIO 芯片

**配置项引用（Symbol References）**：[`CONFIG_GPIO_SX1509B`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_SX1509B)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_SX1509B_INIT_PRIORITY"></a>

## 99.90 `CONFIG_GPIO_SX1509B_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_SX1509B && CONFIG_GPIO
```

**默认值（Defaults）**

```text
CONFIG_I2C_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.sx1509b:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.sx1509b#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → SX1509B I2C GPIO 芯片

**配置项引用（Symbol References）**：[`CONFIG_GPIO_SX1509B`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_SX1509B)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C_INIT_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_INIT_PRIORITY)。

<a id="CONFIG_GPIO_SX1509B_INTERRUPT"></a>

## 99.91 `CONFIG_GPIO_SX1509B_INTERRUPT`

**提示（Prompt）**：启用中断（Interrupt Enable）

**说明（Help）**

启用 GPIO 引脚中断（Interrupt）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_SX1509B && CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.sx1509b:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.sx1509b#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → SX1509B I2C GPIO 芯片

**配置项引用（Symbol References）**：[`CONFIG_GPIO_SX1509B`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_SX1509B)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_SY1XX"></a>

## 99.92 `CONFIG_GPIO_SY1XX`

**提示（Prompt）**：SY1XX GPIO 驱动

**说明（Help）**

启用 SY1XX GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SENSRY_SY1XX_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.sy1xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.sy1xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_TCA6424A"></a>

## 99.93 `CONFIG_GPIO_TCA6424A`

**提示（Prompt）**：TCA6424A 驱动

**说明（Help）**

启用 TCA6424A I/O 扩展器（I/O Expander）芯片的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_TCA6424A_ENABLED && CONFIG_I2C && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.tca6424a:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.tca6424a#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_TCA6424A_INIT_PRIORITY"></a>

## 99.94 `CONFIG_GPIO_TCA6424A_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_TCA6424A && CONFIG_GPIO
```

**默认值（Defaults）**

```text
CONFIG_I2C_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.tca6424a:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.tca6424a#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → TCA6424A 驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO_TCA6424A`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_TCA6424A)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C_INIT_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_INIT_PRIORITY)。

<a id="CONFIG_GPIO_TCA9554"></a>

## 99.95 `CONFIG_GPIO_TCA9554`

**提示（Prompt）**：德州仪器（Texas Instruments）TCA9554 I/O 扩展器（I/O Expander）

**说明（Help）**

启用 TCA9554 的驱动实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_TCA9554_ENABLED && CONFIG_I2C && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.tca9554:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.tca9554#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_TCA9554_INIT_PRIO"></a>

## 99.96 `CONFIG_GPIO_TCA9554_INIT_PRIO`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_TCA9554 && CONFIG_GPIO
```

**默认值（Defaults）**

```text
70
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.tca9554:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.tca9554#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 德州仪器（Texas Instruments）TCA9554 I/O 扩展器（I/O Expander）

**配置项引用（Symbol References）**：[`CONFIG_GPIO_TCA9554`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_TCA9554)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_TELINK_B91"></a>

## 99.97 `CONFIG_GPIO_TELINK_B91`

**提示（Prompt）**：泰凌（Telink）B91 GPIO 驱动

**说明（Help）**

启用 B91 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TELINK_B91_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.b91:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.b91#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_THEJAS32"></a>

## 99.98 `CONFIG_GPIO_THEJAS32`

**提示（Prompt）**：C-DAC THEJAS32 GPIO 驱动

**说明（Help）**

为 C-DAC THEJAS32 SoC 启用 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_CDAC_THEJAS32_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.thejas32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.thejas32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_TLA2528"></a>

## 99.99 `CONFIG_GPIO_TLA2528`

**提示（Prompt）**：带 GPIO 的德州仪器（Texas Instruments）TLA2528 模数转换器（ADC）

**说明（Help）**

启用 TLA2528 的 GPIO 驱动实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_TLA2528_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.tla2528:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.tla2528#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_GPIO_TLA2528_INIT_PRIO"></a>

## 99.100 `CONFIG_GPIO_TLA2528_INIT_PRIO`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动初始化优先级。实际优先级必须低于 TLA2528 多功能设备（MFD）驱动，即数值必须更大。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_TLA2528 && CONFIG_GPIO
```

**默认值（Defaults）**

```text
70
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.tla2528:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.tla2528#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 带 GPIO 的德州仪器（Texas Instruments）TLA2528 模数转换器（ADC）

**配置项引用（Symbol References）**：[`CONFIG_GPIO_TLA2528`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_TLA2528)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<!-- kconfig-navigation -->

[上一章](P098_drivers_gpio_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P100_drivers_gpio_配置项参考_3.md)
