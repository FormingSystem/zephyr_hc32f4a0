---
id: learning.zephyr-docs.kconfig-reference.page-207
title: "`modules/Kconfig.nuvoton`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第207章\_`modules/Kconfig.nuvoton`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/Kconfig.nuvoton` 的 15 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_HAS_NUMAKER_ADC"></a>

## 207.1 `CONFIG_HAS_NUMAKER_ADC`

**提示（Prompt）**：NuMaker 模数转换器（ADC）

**说明（Help）**

启用新唐（Nuvoton）模数转换器（ADC）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NUMAKER_HAL
```

**被选择（Selected by）**

```text
CONFIG_ADC_NUMAKER
CONFIG_USBC_TCPC_NUMAKER
```

**定义位置（Location）**：[`modules/Kconfig.nuvoton:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.nuvoton#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → 新唐（Nuvoton）NuMaker 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_NUMAKER_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NUMAKER_HAL)、[`CONFIG_ADC_NUMAKER`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_NUMAKER)、[`CONFIG_USBC_TCPC_NUMAKER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_NUMAKER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NUMAKER_HAL`。

<a id="CONFIG_HAS_NUMAKER_CANFD"></a>

## 207.2 `CONFIG_HAS_NUMAKER_CANFD`

**提示（Prompt）**：NuMaker 灵活数据速率 CAN（CAN FD）

**说明（Help）**

启用新唐（Nuvoton）CAN FD 硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NUMAKER_HAL
```

**定义位置（Location）**：[`modules/Kconfig.nuvoton:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.nuvoton#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → 新唐（Nuvoton）NuMaker 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_NUMAKER_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NUMAKER_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NUMAKER_HAL`。

<a id="CONFIG_HAS_NUMAKER_ETH"></a>

## 207.3 `CONFIG_HAS_NUMAKER_ETH`

**提示（Prompt）**：NuMaker 以太网（ETH）

**说明（Help）**

启用新唐（Nuvoton）以太网媒体访问控制器（ETH EMAC）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NUMAKER_HAL
```

**定义位置（Location）**：[`modules/Kconfig.nuvoton:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.nuvoton#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → 新唐（Nuvoton）NuMaker 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_NUMAKER_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NUMAKER_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NUMAKER_HAL`。

<a id="CONFIG_HAS_NUMAKER_FMC"></a>

## 207.4 `CONFIG_HAS_NUMAKER_FMC`

**提示（Prompt）**：NuMaker 闪存控制器（FMC）

**说明（Help）**

启用新唐（Nuvoton）闪存控制器（FMC）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NUMAKER_HAL
```

**被选择（Selected by）**

```text
CONFIG_SOC_FLASH_NUMAKER
CONFIG_HWINFO_NUMAKER
```

**定义位置（Location）**：[`modules/Kconfig.nuvoton:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.nuvoton#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → 新唐（Nuvoton）NuMaker 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_NUMAKER_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NUMAKER_HAL)、[`CONFIG_SOC_FLASH_NUMAKER`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NUMAKER)、[`CONFIG_HWINFO_NUMAKER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_NUMAKER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NUMAKER_HAL`。

<a id="CONFIG_HAS_NUMAKER_GPIO"></a>

## 207.5 `CONFIG_HAS_NUMAKER_GPIO`

**提示（Prompt）**：NuMaker 通用输入／输出（GPIO）

**说明（Help）**

启用新唐（Nuvoton）通用输入／输出（GPIO）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NUMAKER_HAL
```

**被选择（Selected by）**

```text
CONFIG_GPIO_NUMAKER
```

**定义位置（Location）**：[`modules/Kconfig.nuvoton:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.nuvoton#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → 新唐（Nuvoton）NuMaker 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_NUMAKER_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NUMAKER_HAL)、[`CONFIG_GPIO_NUMAKER`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_NUMAKER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NUMAKER_HAL`。

<a id="CONFIG_HAS_NUMAKER_HSUSBD"></a>

## 207.6 `CONFIG_HAS_NUMAKER_HSUSBD`

**提示（Prompt）**：NuMaker 高速 USB 2.0 设备控制器（high-speed device controller）

**说明（Help）**

启用新唐（Nuvoton）高速 USB 2.0 设备控制器（device controller）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NUMAKER_HAL
```

**定义位置（Location）**：[`modules/Kconfig.nuvoton:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.nuvoton#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → 新唐（Nuvoton）NuMaker 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_NUMAKER_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NUMAKER_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NUMAKER_HAL`。

<a id="CONFIG_HAS_NUMAKER_I2C"></a>

## 207.7 `CONFIG_HAS_NUMAKER_I2C`

**提示（Prompt）**：NuMaker I2C 总线

**说明（Help）**

启用新唐（Nuvoton）I2C 硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NUMAKER_HAL
```

**被选择（Selected by）**

```text
CONFIG_I2C_NUMAKER
```

**定义位置（Location）**：[`modules/Kconfig.nuvoton:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.nuvoton#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → 新唐（Nuvoton）NuMaker 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_NUMAKER_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NUMAKER_HAL)、[`CONFIG_I2C_NUMAKER`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_NUMAKER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NUMAKER_HAL`。

<a id="CONFIG_HAS_NUMAKER_PWM"></a>

## 207.8 `CONFIG_HAS_NUMAKER_PWM`

**提示（Prompt）**：NuMaker 脉宽调制（PWM）

**说明（Help）**

启用新唐（Nuvoton）脉宽调制（PWM）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NUMAKER_HAL
```

**被选择（Selected by）**

```text
CONFIG_PWM_NUMAKER
```

**定义位置（Location）**：[`modules/Kconfig.nuvoton:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.nuvoton#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → 新唐（Nuvoton）NuMaker 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_NUMAKER_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NUMAKER_HAL)、[`CONFIG_PWM_NUMAKER`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_NUMAKER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NUMAKER_HAL`。

<a id="CONFIG_HAS_NUMAKER_RMC"></a>

## 207.9 `CONFIG_HAS_NUMAKER_RMC`

**提示（Prompt）**：NuMaker RMC

**说明（Help）**

启用新唐（Nuvoton）RMC 硬件抽象层（HAL）模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NUMAKER_HAL
```

**被选择（Selected by）**

```text
CONFIG_SOC_FLASH_NUMAKER_RMC
CONFIG_HWINFO_NUMAKER_RMC
```

**定义位置（Location）**：[`modules/Kconfig.nuvoton:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.nuvoton#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → 新唐（Nuvoton）NuMaker 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_NUMAKER_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NUMAKER_HAL)、[`CONFIG_SOC_FLASH_NUMAKER_RMC`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NUMAKER_RMC)、[`CONFIG_HWINFO_NUMAKER_RMC`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_NUMAKER_RMC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NUMAKER_HAL`。

<a id="CONFIG_HAS_NUMAKER_RTC"></a>

## 207.10 `CONFIG_HAS_NUMAKER_RTC`

**提示（Prompt）**：NuMaker 实时时钟（RTC）

**说明（Help）**

启用新唐（Nuvoton）实时时钟（RTC）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NUMAKER_HAL
```

**被选择（Selected by）**

```text
CONFIG_RTC_NUMAKER
```

**定义位置（Location）**：[`modules/Kconfig.nuvoton:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.nuvoton#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → 新唐（Nuvoton）NuMaker 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_NUMAKER_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NUMAKER_HAL)、[`CONFIG_RTC_NUMAKER`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_NUMAKER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NUMAKER_HAL`。

<a id="CONFIG_HAS_NUMAKER_SPI"></a>

## 207.11 `CONFIG_HAS_NUMAKER_SPI`

**提示（Prompt）**：NuMaker 串行外设接口（SPI）

**说明（Help）**

启用新唐（Nuvoton）串行外设接口（SPI）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NUMAKER_HAL
```

**被选择（Selected by）**

```text
CONFIG_SPI_NUMAKER
CONFIG_SPI_NUMAKER_USCI
```

**定义位置（Location）**：[`modules/Kconfig.nuvoton:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.nuvoton#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → 新唐（Nuvoton）NuMaker 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_NUMAKER_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NUMAKER_HAL)、[`CONFIG_SPI_NUMAKER`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_NUMAKER)、[`CONFIG_SPI_NUMAKER_USCI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_NUMAKER_USCI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NUMAKER_HAL`。

<a id="CONFIG_HAS_NUMAKER_TMR"></a>

## 207.12 `CONFIG_HAS_NUMAKER_TMR`

**提示（Prompt）**：NuMaker 定时器（Timer）

**说明（Help）**

启用新唐（Nuvoton）定时器（Timer）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NUMAKER_HAL
```

**被选择（Selected by）**

```text
CONFIG_USBC_TCPC_NUMAKER
```

**定义位置（Location）**：[`modules/Kconfig.nuvoton:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.nuvoton#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → 新唐（Nuvoton）NuMaker 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_NUMAKER_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NUMAKER_HAL)、[`CONFIG_USBC_TCPC_NUMAKER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_NUMAKER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NUMAKER_HAL`。

<a id="CONFIG_HAS_NUMAKER_UART"></a>

## 207.13 `CONFIG_HAS_NUMAKER_UART`

**提示（Prompt）**：NuMaker 通用异步收发器（UART）

**说明（Help）**

启用新唐（Nuvoton）通用异步收发器（Universal Asynchronous Receiver Transmitter，UART）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NUMAKER_HAL
```

**被选择（Selected by）**

```text
CONFIG_UART_NUMAKER
```

**定义位置（Location）**：[`modules/Kconfig.nuvoton:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.nuvoton#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → 新唐（Nuvoton）NuMaker 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_NUMAKER_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NUMAKER_HAL)、[`CONFIG_UART_NUMAKER`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NUMAKER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NUMAKER_HAL`。

<a id="CONFIG_HAS_NUMAKER_USBD"></a>

## 207.14 `CONFIG_HAS_NUMAKER_USBD`

**提示（Prompt）**：NuMaker USB 1.1 设备控制器（device controller）

**说明（Help）**

启用新唐（Nuvoton）USB 1.1 设备控制器（device controller）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NUMAKER_HAL
```

**定义位置（Location）**：[`modules/Kconfig.nuvoton:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.nuvoton#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → 新唐（Nuvoton）NuMaker 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_NUMAKER_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NUMAKER_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NUMAKER_HAL`。

<a id="CONFIG_HAS_NUMICRO_UART"></a>

## 207.15 `CONFIG_HAS_NUMICRO_UART`

**提示（Prompt）**：NuMicro 通用异步收发器（UART）

**说明（Help）**

启用新唐（Nuvoton）通用异步收发器（Universal Asynchronous Receiver Transmitter，UART）HAL 模块驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NUMICRO_HAL
```

**被选择（Selected by）**

```text
CONFIG_UART_NUMICRO
```

**定义位置（Location）**：[`modules/Kconfig.nuvoton:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.nuvoton#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → 新唐（Nuvoton）驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_NUMICRO_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NUMICRO_HAL)、[`CONFIG_UART_NUMICRO`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NUMICRO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NUMICRO_HAL`。

<!-- kconfig-navigation -->

[上一章](P206_modules_Kconfig.microchip_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P208_modules_Kconfig.open-amp_配置项参考.md)
