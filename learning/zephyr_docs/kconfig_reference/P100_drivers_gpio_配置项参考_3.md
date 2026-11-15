---
id: learning.zephyr-docs.kconfig-reference.page-100
title: "`drivers/gpio`配置项参考（3/3）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第100章\_`drivers/gpio`配置项参考（3/3）

本章翻译官方 Kconfig 数据库中 `drivers/gpio` 的 13 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_GPIO_TLE9104"></a>

## 100.1 `CONFIG_GPIO_TLE9104`

**提示（Prompt）**：基于 SPI 的 TLE9104 动力总成开关（Powertrain Switch）

**说明（Help）**

启用基于 SPI 的 TLE9104 动力总成开关（Powertrain Switch）的 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_TLE9104_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.tle9104:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.tle9104#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_GPIO_TLE9104_INIT_PRIORITY"></a>

## 100.2 `CONFIG_GPIO_TLE9104_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_TLE9104 && CONFIG_GPIO
```

**默认值（Defaults）**

```text
75
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.tle9104:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.tle9104#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 基于 SPI 的 TLE9104 动力总成开关（Powertrain Switch）

**配置项引用（Symbol References）**：[`CONFIG_GPIO_TLE9104`](P100_drivers_gpio_配置项参考_3.md#CONFIG_GPIO_TLE9104)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_VIRTIO"></a>

## 100.3 `CONFIG_GPIO_VIRTIO`

**提示（Prompt）**：VIRTIO GPIO 驱动

**说明（Help）**

启用 VIRTIO GPIO 设备的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_VIRTIO_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_VIRTIO
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.virtio:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.virtio#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_VIRTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIRTIO)。

<a id="CONFIG_GPIO_WCH_CH5XX"></a>

## 100.4 `CONFIG_GPIO_WCH_CH5XX`

**提示（Prompt）**：沁恒（WCH）CH5xx GPIO 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WCH_CH5XX_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.wch_ch5xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.wch_ch5xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_WCH_CH5XX_INTERRUPTS"></a>

## 100.5 `CONFIG_GPIO_WCH_CH5XX_INTERRUPTS`

**提示（Prompt）**：中断支持（Interrupt Support）

**说明（Help）**

支持在引脚状态改变（Pin Change）时触发中断（Interrupt）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_WCH_CH5XX && DT_HAS_WCH_PFIC_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.wch_ch5xx:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.wch_ch5xx#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 沁恒（WCH）CH5xx GPIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO_WCH_CH5XX`](P100_drivers_gpio_配置项参考_3.md#CONFIG_GPIO_WCH_CH5XX)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_WCH_GPIO"></a>

## 100.6 `CONFIG_GPIO_WCH_GPIO`

**提示（Prompt）**：沁恒（WCH）CH32V00x GPIO 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WCH_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.wch_ch32v00x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.wch_ch32v00x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_WCH_GPIO_INTERRUPTS"></a>

## 100.7 `CONFIG_GPIO_WCH_GPIO_INTERRUPTS`

**提示（Prompt）**：中断支持（Interrupt Support）

**说明（Help）**

支持在引脚状态改变（Pin Change）时触发中断（Interrupt）。约使用 700 字节闪存和 60 字节 RAM。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_WCH_GPIO && DT_HAS_WCH_EXTI_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.wch_ch32v00x:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.wch_ch32v00x#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 沁恒（WCH）CH32V00x GPIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO_WCH_GPIO`](P100_drivers_gpio_配置项参考_3.md#CONFIG_GPIO_WCH_GPIO)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_XEC"></a>

## 100.8 `CONFIG_GPIO_XEC`

**提示（Prompt）**：Microchip XEC GPIO 驱动

**说明（Help）**

启用 Microchip XEC GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_XEC_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.xec:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.xec#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_XLNX_AXI"></a>

## 100.9 `CONFIG_GPIO_XLNX_AXI`

**提示（Prompt）**：Xilinx AXI GPIO 驱动

**说明（Help）**

启用 Xilinx AXI GPIO v2 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XLNX_XPS_GPIO_1_00_A_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.xlnx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.xlnx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_XLNX_PS"></a>

## 100.10 `CONFIG_GPIO_XLNX_PS`

**提示（Prompt）**：Xilinx 处理器系统 MIO/EMIO GPIO 控制器驱动（Processor System GPIO Controller Driver）

**说明（Help）**

启用 Xilinx 处理器系统（Processor System）MIO/EMIO GPIO 控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XLNX_PS_GPIO_ENABLED && !CONFIG_QEMU_TARGET && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.xlnx_ps:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.xlnx_ps#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_QEMU_TARGET`](P041_boards_Kconfig_配置项参考.md#CONFIG_QEMU_TARGET)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_GPIO_XMC4XXX"></a>

## 100.11 `CONFIG_GPIO_XMC4XXX`

**提示（Prompt）**：XMC4XXX GPIO 驱动

**说明（Help）**

为 XMC4XXX 微控制器（MCU）系列启用 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_XMC4XXX_GPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.xmc4xxx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.xmc4xxx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_LPGPIO_ESP32"></a>

## 100.12 `CONFIG_LPGPIO_ESP32`

**提示（Prompt）**：ESP32 低功耗 GPIO（Low Power GPIO）

**说明（Help）**

启用 ESP32 GPIO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_LPGPIO_ENABLED && CONFIG_GPIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.esp32:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.esp32#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_RT1718S_INIT_PRIORITY"></a>

## 100.13 `CONFIG_RT1718S_INIT_PRIORITY`

**提示（Prompt）**：RT1718S GPIO 初始化优先级（Init Priority）

**说明（Help）**

RT1718S 设备驱动的初始化优先级（Initialization Priority）。原文要求其优先级低于 I2C 设备。

> 译注：本快照中，I2C 默认采用 `CONFIG_KERNEL_INIT_PRIORITY_DEVICE`，其值为 `50`；本项默认值为 `60`。这里对应 RT1718S 在 I2C 之后初始化，不能把 `lower` 直接解释为数值更小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_RT1718S && CONFIG_GPIO
```

**默认值（Defaults）**

```text
60
```

**定义位置（Location）**：[`drivers/gpio/Kconfig.rt1718s:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/Kconfig.rt1718s#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 带 GPIO 的、基于 I2C 的 RT1718S Type-C 端口控制器（TCPC）芯片

**配置项引用（Symbol References）**：[`CONFIG_GPIO_RT1718S`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_RT1718S)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<!-- kconfig-navigation -->

[上一章](P099_drivers_gpio_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P101_drivers_haptics_配置项参考.md)
