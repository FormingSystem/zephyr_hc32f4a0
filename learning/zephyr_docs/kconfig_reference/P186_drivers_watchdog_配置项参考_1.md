---
id: learning.zephyr-docs.kconfig-reference.page-186
title: "`drivers/watchdog`配置项参考（1/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第186章\_`drivers/watchdog`配置项参考（1/2）

本章翻译官方 Kconfig 数据库中 `drivers/watchdog` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_FWDGT_GD32"></a>

## 186.1 `CONFIG_FWDGT_GD32`

**提示（Prompt）**：GD32 自由看门狗定时器（Free Watchdog Timer，FWDGT）驱动

**说明（Help）**

为 GD32 片上系统（SoC）启用自由看门狗定时器（Free Watchdog Timer，FWDGT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GD_GD32_FWDGT_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_GD32_FWDGT
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.gd32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.gd32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_USE_GD32_FWDGT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_GD32_FWDGT)。

<a id="CONFIG_HAS_WDT_DISABLE_AT_BOOT"></a>

## 186.2 `CONFIG_HAS_WDT_DISABLE_AT_BOOT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果驱动所支持的看门狗定时器（Watchdog Timer）在系统复位后默认启用，则该驱动必须选择此隐藏符号。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WATCHDOG
```

**被选择（Selected by）**

```text
CONFIG_WDT_ANDES_ATCWDT200
CONFIG_WDT_ENE_KB1200
CONFIG_WDT_ENE_KB106X
CONFIG_WDT_GECKO
CONFIG_WDT_ITE_IT51XXX
CONFIG_WDT_ITE_IT8XXX2
CONFIG_WDT_MCHP_G1
CONFIG_WDT_MCUX_COP
CONFIG_WDT_NPCX
CONFIG_WDT_RENESAS_RA
CONFIG_WDT_RENESAS_RX_IWDT
CONFIG_WDT_RENESAS_RZ
CONFIG_WDT_RTS5912
CONFIG_WDT_SAM
CONFIG_WDT_SAM0
CONFIG_WDT_SAM4L
CONFIG_WDT_SF32LB
CONFIG_WDT_SIFIVE
CONFIG_WDT_SILABS_WDOG
CONFIG_WDT_SMARTBOND
CONFIG_WDT_TCO
CONFIG_WDT_TI_RTI
CONFIG_WDT_XEC
CONFIG_WDT_XMC4XXX
CONFIG_WDT_RTS5817
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_WDT_ANDES_ATCWDT200`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_ANDES_ATCWDT200)、[`CONFIG_WDT_ENE_KB1200`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_ENE_KB1200)、[`CONFIG_WDT_ENE_KB106X`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_ENE_KB106X)、[`CONFIG_WDT_GECKO`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_GECKO)、[`CONFIG_WDT_ITE_IT51XXX`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_ITE_IT51XXX)、[`CONFIG_WDT_ITE_IT8XXX2`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_ITE_IT8XXX2)、[`CONFIG_WDT_MCHP_G1`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_MCHP_G1)、[`CONFIG_WDT_MCUX_COP`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_MCUX_COP)、[`CONFIG_WDT_NPCX`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_NPCX)、[`CONFIG_WDT_RENESAS_RA`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_RENESAS_RA)、[`CONFIG_WDT_RENESAS_RX_IWDT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_RENESAS_RX_IWDT)、[`CONFIG_WDT_RENESAS_RZ`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_RENESAS_RZ)、[`CONFIG_WDT_RTS5912`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_RTS5912)、[`CONFIG_WDT_SAM`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_SAM)、[`CONFIG_WDT_SAM0`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_SAM0)、[`CONFIG_WDT_SAM4L`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_SAM4L)、[`CONFIG_WDT_SF32LB`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_SF32LB)、[`CONFIG_WDT_SIFIVE`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_SIFIVE)、[`CONFIG_WDT_SILABS_WDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_SILABS_WDOG)、[`CONFIG_WDT_SMARTBOND`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_SMARTBOND)、[`CONFIG_WDT_TCO`](P187_drivers_watchdog_配置项参考_2.md#CONFIG_WDT_TCO)、[`CONFIG_WDT_TI_RTI`](P187_drivers_watchdog_配置项参考_2.md#CONFIG_WDT_TI_RTI)、[`CONFIG_WDT_XEC`](P187_drivers_watchdog_配置项参考_2.md#CONFIG_WDT_XEC)、[`CONFIG_WDT_XMC4XXX`](P187_drivers_watchdog_配置项参考_2.md#CONFIG_WDT_XMC4XXX)、[`CONFIG_WDT_RTS5817`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_RTS5817)。

<a id="CONFIG_HAS_WDT_NO_CALLBACKS"></a>

## 186.3 `CONFIG_HAS_WDT_NO_CALLBACKS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

看门狗驱动不支持回调（Callbacks）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WATCHDOG
```

**被选择（Selected by）**

```text
CONFIG_WWDGT_GD32
CONFIG_WDT_MCUX_COP
CONFIG_WDT_NRF_GSWDT
CONFIG_WDT_RPI_PICO
CONFIG_WDT_SF32LB
CONFIG_WDT_SMARTBOND
CONFIG_IWDG_STM32
CONFIG_WDT_TCO
CONFIG_WDT_TI_TPS382X
CONFIG_WDT_XEN
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_WWDGT_GD32`](P187_drivers_watchdog_配置项参考_2.md#CONFIG_WWDGT_GD32)、[`CONFIG_WDT_MCUX_COP`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_MCUX_COP)、[`CONFIG_WDT_NRF_GSWDT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_NRF_GSWDT)、[`CONFIG_WDT_RPI_PICO`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_RPI_PICO)、[`CONFIG_WDT_SF32LB`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_SF32LB)、[`CONFIG_WDT_SMARTBOND`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_SMARTBOND)、[`CONFIG_IWDG_STM32`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_IWDG_STM32)、[`CONFIG_WDT_TCO`](P187_drivers_watchdog_配置项参考_2.md#CONFIG_WDT_TCO)、[`CONFIG_WDT_TI_TPS382X`](P187_drivers_watchdog_配置项参考_2.md#CONFIG_WDT_TI_TPS382X)、[`CONFIG_WDT_XEN`](P187_drivers_watchdog_配置项参考_2.md#CONFIG_WDT_XEN)。

<a id="CONFIG_IWDG_STM32"></a>

## 186.4 `CONFIG_IWDG_STM32`

**提示（Prompt）**：STM32 MCU 系列的独立看门狗（Independent Watchdog，IWDG）驱动

**说明（Help）**

为 STM32 微控制器（MCU）系列启用独立看门狗（IWDG）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_WATCHDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_WDT_NO_CALLBACKS
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.stm32:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.stm32#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_NO_CALLBACKS`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_NO_CALLBACKS)。

<a id="CONFIG_IWDG_STM32_EARLY_WAKEUP"></a>

## 186.5 `CONFIG_IWDG_STM32_EARLY_WAKEUP`

**提示（Prompt）**：STM32 IWDG 提前唤醒中断（Early Wakeup Interrupt）支持

**说明（Help）**

启用提前唤醒中断（Early Wakeup Interrupt）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.stm32:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.stm32#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → STM32 MCU 系列的独立看门狗（Independent Watchdog，IWDG）驱动

<a id="CONFIG_IWDG_STM32_EWI_TIME"></a>

## 186.6 `CONFIG_IWDG_STM32_EWI_TIME`

**提示（Prompt）**：IWDG 提前唤醒值，单位为计数节拍（Tick）

**说明（Help）**

设置 IWDG 提前唤醒中断（Early Wake-up Interrupt）的值，单位为计数节拍（Tick），表示在复位之前多长时间发生提前唤醒。如果运行时提供的重装载值（Reload Value）更小，则忽略此值；此时，中断在看门狗重新装载一个计数节拍后触发。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IWDG_STM32_EARLY_WAKEUP && CONFIG_IWDG_STM32 && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
100
```

**取值范围（Ranges）**

```text
[2, 4095]
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.stm32:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.stm32#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → STM32 MCU 系列的独立看门狗（Independent Watchdog，IWDG）驱动 → STM32 IWDG 提前唤醒中断（Early Wakeup Interrupt）支持

**配置项引用（Symbol References）**：[`CONFIG_IWDG_STM32_EARLY_WAKEUP`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_IWDG_STM32_EARLY_WAKEUP)、[`CONFIG_IWDG_STM32`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_IWDG_STM32)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_IWDG_STM32_INITIAL_TIMEOUT"></a>

## 186.7 `CONFIG_IWDG_STM32_INITIAL_TIMEOUT`

**提示（Prompt）**：IWDG 超时时间，单位为毫秒

**说明（Help）**

如果在启动时启用独立看门狗（IWDG），此项设置其初始超时时间，单位为毫秒。最小支持 1 ms。最大超时时间取决于微控制器（MCU）的低速内部时钟（LSI）频率，计算方式为：最大预分频值 256 × 最大重装载计数 4096 ÷ LSI 频率。此处将最大超时限制为安全值 26214 ms，按原文所述 STM32 MCU 中最高的 LSI 频率 40 kHz 计算。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IWDG_STM32 && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
100
```

**取值范围（Ranges）**

```text
[1, 26214]
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.stm32:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.stm32#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → STM32 MCU 系列的独立看门狗（Independent Watchdog，IWDG）驱动

**配置项引用（Symbol References）**：[`CONFIG_IWDG_STM32`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_IWDG_STM32)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WATCHDOG"></a>

## 186.8 `CONFIG_WATCHDOG`

**提示（Prompt）**：看门狗驱动（Watchdog Drivers）

**说明（Help）**

包含看门狗（Watchdog）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/watchdog/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_WDOG_CMSDK_APB"></a>

## 186.9 `CONFIG_WDOG_CMSDK_APB`

**提示（Prompt）**：ARM MCU 系列的 CMSDK APB 看门狗驱动

**说明（Help）**

为 ARM 微控制器（MCU）系列启用 CMSDK APB 看门狗（`WDOG_CMSDK_APB`）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ARM_CMSDK_WATCHDOG_ENABLED && CONFIG_RUNTIME_NMI && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.cmsdk_apb:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.cmsdk_apb#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RUNTIME_NMI`](P030_arch_arm_配置项参考_2.md#CONFIG_RUNTIME_NMI)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDOG_CMSDK_APB_START_AT_BOOT"></a>

## 186.10 `CONFIG_WDOG_CMSDK_APB_START_AT_BOOT`

**提示（Prompt）**：启动期间开启看门狗（Watchdog）

**说明（Help）**

启用后，允许看门狗（WDOG）在设备初始化期间自动启动。注意，看门狗启动后必须在计数器降至 0 之前重新装载，否则微控制器（MCU）将复位。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WDOG_CMSDK_APB && CONFIG_WATCHDOG
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.cmsdk_apb:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.cmsdk_apb#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → ARM MCU 系列的 CMSDK APB 看门狗驱动

**配置项引用（Symbol References）**：[`CONFIG_WDOG_CMSDK_APB`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDOG_CMSDK_APB)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_ADI_MAX42500"></a>

## 186.11 `CONFIG_WDT_ADI_MAX42500`

**提示（Prompt）**：ADI MAX42500 看门狗（WDT）驱动

**说明（Help）**

为 ADI MAX42500 启用看门狗（WDT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX42500_WATCHDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.adi_max42500:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.adi_max42500#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_WDT_AMBIQ"></a>

## 186.12 `CONFIG_WDT_AMBIQ`

**提示（Prompt）**：AMBIQ 看门狗（WDT）驱动

**说明（Help）**

启用 Ambiq 看门狗（WDT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMBIQ_WATCHDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_AMBIQ_HAL
CONFIG_AMBIQ_HAL_USE_WDT
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.ambiq:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.ambiq#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_AMBIQ_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL)、[`CONFIG_AMBIQ_HAL_USE_WDT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL_USE_WDT)。

<a id="CONFIG_WDT_AMEBA"></a>

## 186.13 `CONFIG_WDT_AMEBA`

**提示（Prompt）**：AMEBA 看门狗（WDT）驱动

**说明（Help）**

为 AMEBA 启用看门狗（WDT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_AMEBA_WATCHDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.ameba:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.ameba#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_ANDES_ATCWDT200"></a>

## 186.14 `CONFIG_WDT_ANDES_ATCWDT200`

**提示（Prompt）**：Andes 看门狗（Watchdog）驱动

**说明（Help）**

启用 Andes 看门狗（Watchdog）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ANDESTECH_ATCWDT200_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_WDT_DISABLE_AT_BOOT
CONFIG_COUNTER
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.andes_atcwdt200:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.andes_atcwdt200#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_DISABLE_AT_BOOT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_DISABLE_AT_BOOT)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_WDT_BEE_CORE"></a>

## 186.15 `CONFIG_WDT_BEE_CORE`

**提示（Prompt）**：Realtek Bee CORE 看门狗定时器（Watch Dog Timer）驱动

**说明（Help）**

为 Realtek Bee 系列片上系统（SoC）启用 CORE 看门狗定时器（WDT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_BEE_CORE_WDT_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAL_REALTEK_BEE_CORE_WDT
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.bee:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.bee#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAL_REALTEK_BEE_CORE_WDT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAL_REALTEK_BEE_CORE_WDT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAL_REALTEK_BEE_CORE_WDT`。

<a id="CONFIG_WDT_BFLB"></a>

## 186.16 `CONFIG_WDT_BFLB`

**提示（Prompt）**：Bouffalo Lab 看门狗（Watchdog）驱动

**说明（Help）**

为 Bouffalo Lab 片上系统（SoC）启用看门狗（Watchdog）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_WDT_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.bflb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.bflb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_CC13XX_CC26XX"></a>

## 186.17 `CONFIG_WDT_CC13XX_CC26XX`

**提示（Prompt）**：CC13xx / CC26xx MCU 系列的看门狗驱动

**说明（Help）**

为 CC13xx / CC26xx 微控制器（MCU）系列启用看门狗（Watchdog）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_CC13XX_CC26XX_WATCHDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.cc13xx_cc26xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.cc13xx_cc26xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_CC23X0"></a>

## 186.18 `CONFIG_WDT_CC23X0`

**提示（Prompt）**：CC23x0 MCU 系列的看门狗驱动

**说明（Help）**

为 CC23x0 微控制器（MCU）系列启用看门狗（Watchdog）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_CC23X0_WDT_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.cc23x0:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.cc23x0#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_CC32XX"></a>

## 186.19 `CONFIG_WDT_CC32XX`

**提示（Prompt）**：CC32xx MCU 系列的看门狗驱动

**说明（Help）**

CC32xx 微控制器（MCU）系列的看门狗（Watchdog）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_CC32XX_WATCHDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.cc32xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.cc32xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_COUNTER"></a>

## 186.20 `CONFIG_WDT_COUNTER`

**提示（Prompt）**：基于计数器的看门狗（Counter-based Watchdog）

**说明（Help）**

使用计数器设备（Counter Device）模拟看门狗。如果计数器设备支持零延迟中断（Zero Latency Interrupt，ZLI），则可在该上下文中调用超时回调（Expiration Callback）。

此看门狗可与硬件看门狗配合使用，以克服硬件限制。例如，Nordic 器件会在触发看门狗中断后的固定时间无条件复位，无法留出打印调试信息的时间。此看门狗也有限制：它不能打断相同或更高优先级的执行，因此无法完全替代硬件看门狗。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_COUNTER_WATCHDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_COUNTER
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_WDT_COUNTER_CH_COUNT"></a>

## 186.21 `CONFIG_WDT_COUNTER_CH_COUNT`

**提示（Prompt）**：支持的最大通道数量

**说明（Help）**

注意，实际通道数量受用于实现看门狗的计数器设备（Counter Device）所支持的通道数量限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WDT_COUNTER && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → 基于计数器的看门狗（Counter-based Watchdog）

**配置项引用（Symbol References）**：[`CONFIG_WDT_COUNTER`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_COUNTER)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_CRSAS_MA2"></a>

## 186.22 `CONFIG_WDT_CRSAS_MA2`

**提示（Prompt）**：CRSAS-MA2 看门狗（Watchdog）驱动

**说明（Help）**

启用 CRSAS-MA2 看门狗（Watchdog）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ARM_CRSAS_MA2_WATCHDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CLOCK_CONTROL
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.crsas_ma2:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.crsas_ma2#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_WDT_DISABLE_AT_BOOT"></a>

## 186.23 `CONFIG_WDT_DISABLE_AT_BOOT`

**提示（Prompt）**：启动时禁用看门狗定时器（Watchdog Timers）

**说明（Help）**

在 Zephyr 系统启动期间禁用看门狗定时器（Watchdog Timers）。此选项关闭时不产生作用，且仅适用于选择了 `HAS_WDT_DISABLE_AT_BOOT` 的驱动。未选择该符号的驱动必须忽略此选项。

启用后，设备树（Devicetree）中所有已启用的看门狗定时器实例，都必须由各自驱动在实例初始化期间禁用。注意，根据硬件实现，启用此选项可能导致应用无法使用某些看门狗定时器，例如定时器禁用后不能重新启用的情况。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_WDT_DISABLE_AT_BOOT && CONFIG_WATCHDOG
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_WDT_DISABLE_AT_BOOT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_DISABLE_AT_BOOT)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_DW"></a>

## 186.24 `CONFIG_WDT_DW`

**提示（Prompt）**：Synopsys DesignWare 看门狗驱动

**说明（Help）**

Synopsys DesignWare 看门狗（Watchdog）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SNPS_DESIGNWARE_WATCHDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.dw:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.dw#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_ENE_KB106X"></a>

## 186.25 `CONFIG_WDT_ENE_KB106X`

**提示（Prompt）**：ENE KB106X 看门狗驱动

**说明（Help）**

此选项启用 KB106X 看门狗（Watchdog）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ENE_KB106X_WATCHDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_WDT_DISABLE_AT_BOOT
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.ene:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.ene#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_DISABLE_AT_BOOT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_DISABLE_AT_BOOT)。

<a id="CONFIG_WDT_ENE_KB1200"></a>

## 186.26 `CONFIG_WDT_ENE_KB1200`

**提示（Prompt）**：ENE KB1200 看门狗驱动

**说明（Help）**

此选项启用 KB1200 看门狗（Watchdog）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ENE_KB1200_WATCHDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_WDT_DISABLE_AT_BOOT
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.ene:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.ene#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_DISABLE_AT_BOOT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_DISABLE_AT_BOOT)。

<a id="CONFIG_WDT_ESP32"></a>

## 186.27 `CONFIG_WDT_ESP32`

**提示（Prompt）**：ESP32 看门狗（WDT）驱动

**说明（Help）**

为 ESP32 启用看门狗（WDT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_WATCHDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.esp32:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.esp32#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_GECKO"></a>

## 186.28 `CONFIG_WDT_GECKO`

**提示（Prompt）**：Gecko 系列看门狗（WDOG）驱动

**说明（Help）**

为 Silicon Labs Gecko 微控制器（MCU）启用看门狗（WDOG）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_GECKO_WDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_WDT_DISABLE_AT_BOOT
CONFIG_SILABS_GECKO_WDOG if CONFIG_SOC_FAMILY_SILABS_S0 || CONFIG_SOC_FAMILY_SILABS_S1
CONFIG_SILABS_SISDK_WDOG if CONFIG_SOC_FAMILY_SILABS_S2
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.gecko:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.gecko#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_DISABLE_AT_BOOT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_DISABLE_AT_BOOT)、[`CONFIG_SILABS_GECKO_WDOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_GECKO_WDOG)、[`CONFIG_SOC_FAMILY_SILABS_S0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S0)、[`CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S1)、[`CONFIG_SILABS_SISDK_WDOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_WDOG)、[`CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S0`、`CONFIG_SOC_FAMILY_SILABS_S1`、`CONFIG_SOC_FAMILY_SILABS_S2`。

<a id="CONFIG_WDT_INFINEON_CAT1"></a>

## 186.29 `CONFIG_WDT_INFINEON_CAT1`

**提示（Prompt）**：Infineon CAT1 看门狗驱动

**说明（Help）**

为 Infineon CAT1 器件启用看门狗（Watchdog）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_WATCHDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_INFINEON_WDT
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.infineon:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.infineon#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_USE_INFINEON_WDT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_WDT)。

<a id="CONFIG_WDT_INTEL_ADSP"></a>

## 186.30 `CONFIG_WDT_INTEL_ADSP`

**提示（Prompt）**：Intel ADSP 看门狗驱动

**说明（Help）**

Intel ADSP 看门狗（Watchdog）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_ADSP_WATCHDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.intel_adsp:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.intel_adsp#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_ITE_IT51XXX"></a>

## 186.31 `CONFIG_WDT_ITE_IT51XXX`

**提示（Prompt）**：ITE it51xxx 看门狗定时器（Watchdog Timer，WDT）驱动

**说明（Help）**

此选项为 ITE it51xxx 启用看门狗定时器（WDT）驱动。仅支持一个 ID 为 0 的通道，WDT 分辨率为 16 位。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT51XXX_WATCHDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_WDT_DISABLE_AT_BOOT
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.it51xxx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.it51xxx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_DISABLE_AT_BOOT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_DISABLE_AT_BOOT)。

<a id="CONFIG_WDT_ITE_IT8XXX2"></a>

## 186.32 `CONFIG_WDT_ITE_IT8XXX2`

**提示（Prompt）**：ITE it8xxx2 看门狗定时器（Watchdog Timer，WDT）驱动

**说明（Help）**

此选项为 ITE it8xxx2 启用看门狗定时器（WDT）驱动。仅支持一个 ID 为 0 的通道，WDT 分辨率为 16 位。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT8XXX2_WATCHDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_WDT_DISABLE_AT_BOOT
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.it8xxx2:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.it8xxx2#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_DISABLE_AT_BOOT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_DISABLE_AT_BOOT)。

<a id="CONFIG_WDT_ITE_PRINT_WARNING_MSG_TIME_MS"></a>

## 186.33 `CONFIG_WDT_ITE_PRINT_WARNING_MSG_TIME_MS`

**提示（Prompt）**：打印警告消息的时间间隔，单位为毫秒

**说明（Help）**

打印警告消息的时间间隔，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WDT_ITE_IT8XXX2 && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
100
```

**取值范围（Ranges）**

```text
[30, CONFIG_WDT_ITE_WARNING_LEADING_TIME_MS]
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.it8xxx2:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.it8xxx2#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → ITE it8xxx2 看门狗定时器（Watchdog Timer，WDT）驱动

**配置项引用（Symbol References）**：[`CONFIG_WDT_ITE_IT8XXX2`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_ITE_IT8XXX2)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_WDT_ITE_WARNING_LEADING_TIME_MS`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_ITE_WARNING_LEADING_TIME_MS)。

<a id="CONFIG_WDT_ITE_REDUCE_WARNING_LEADING_TIME"></a>

## 186.34 `CONFIG_WDT_ITE_REDUCE_WARNING_LEADING_TIME`

原库同名定义共 2 条；本项为数据库第 20965 条记录，各定义分别保留。

**提示（Prompt）**：缩短警告提前时间（Warning Leading Time）

**说明（Help）**

警告定时器触发后，如果看门狗定时器尚未重新装载，则将警告定时器间隔缩短为 30 ms，以便在看门狗复位前打印更多警告消息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WDT_ITE_IT51XXX && CONFIG_WATCHDOG
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.it51xxx:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.it51xxx#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → ITE it51xxx 看门狗定时器（Watchdog Timer，WDT）驱动

**配置项引用（Symbol References）**：[`CONFIG_WDT_ITE_IT51XXX`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_ITE_IT51XXX)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_ITE_REDUCE_WARNING_LEADING_TIME--record-20966"></a>

## 186.35 `CONFIG_WDT_ITE_REDUCE_WARNING_LEADING_TIME`

原库同名定义共 2 条；本项为数据库第 20966 条记录，各定义分别保留。

**提示（Prompt）**：缩短警告提前时间（Warning Leading Time）

**说明（Help）**

警告定时器触发后，如果看门狗定时器尚未重新装载，则将警告定时器间隔缩短为 `WDT_ITE_PRINT_WARNING_MSG_TIME_MS`，以便在看门狗复位前打印更多警告消息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WDT_ITE_IT8XXX2 && CONFIG_WATCHDOG
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.it8xxx2:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.it8xxx2#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → ITE it8xxx2 看门狗定时器（Watchdog Timer，WDT）驱动

**配置项引用（Symbol References）**：[`CONFIG_WDT_ITE_IT8XXX2`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_ITE_IT8XXX2)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_ITE_WARNING_LEADING_TIME_MS"></a>

## 186.36 `CONFIG_WDT_ITE_WARNING_LEADING_TIME_MS`

原库同名定义共 2 条；本项为数据库第 20967 条记录，各定义分别保留。

**提示（Prompt）**：产生看门狗事件／信号前的毫秒数

**说明（Help）**

此选项定义必须处理看门狗事件（Watchdog Event）的时间窗口。窗口结束后，立即触发看门狗复位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WDT_ITE_IT51XXX && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
500
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.it51xxx:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.it51xxx#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → ITE it51xxx 看门狗定时器（Watchdog Timer，WDT）驱动

**配置项引用（Symbol References）**：[`CONFIG_WDT_ITE_IT51XXX`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_ITE_IT51XXX)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_ITE_WARNING_LEADING_TIME_MS--record-20968"></a>

## 186.37 `CONFIG_WDT_ITE_WARNING_LEADING_TIME_MS`

原库同名定义共 2 条；本项为数据库第 20968 条记录，各定义分别保留。

**提示（Prompt）**：产生看门狗事件／信号前的毫秒数

**说明（Help）**

此选项定义必须处理看门狗事件（Watchdog Event）的时间窗口。窗口结束后，立即触发看门狗复位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WDT_ITE_IT8XXX2 && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
500
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.it8xxx2:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.it8xxx2#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → ITE it8xxx2 看门狗定时器（Watchdog Timer，WDT）驱动

**配置项引用（Symbol References）**：[`CONFIG_WDT_ITE_IT8XXX2`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_ITE_IT8XXX2)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_IWDG_WCH"></a>

## 186.38 `CONFIG_WDT_IWDG_WCH`

**提示（Prompt）**：WCH 独立看门狗（Independent Watchdog，IWDG）驱动

**说明（Help）**

启用独立看门狗（IWDG）驱动。已在 CH32V003 和 CH32V208 上测试。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WCH_IWDG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.wch:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.wch#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_LITEX"></a>

## 186.39 `CONFIG_WDT_LITEX`

**提示（Prompt）**：LiteX 看门狗（WDT）驱动

**说明（Help）**

为 LiteX 启用看门狗（WDT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LITEX_WATCHDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.litex:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.litex#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_M5PM1"></a>

## 186.40 `CONFIG_WDT_M5PM1`

**提示（Prompt）**：M5Stack M5PM1 看门狗驱动

**说明（Help）**

启用 M5Stack M5PM1 看门狗（Watchdog）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_M5STACK_M5PM1_WDT_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.m5pm1:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.m5pm1#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_WDT_M5PM1_INIT_PRIORITY"></a>

## 186.41 `CONFIG_WDT_M5PM1_INIT_PRIORITY`

**提示（Prompt）**：M5PM1 看门狗驱动初始化优先级

**说明（Help）**

M5PM1 看门狗驱动的初始化优先级，必须大于多功能器件（MFD）的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WDT_M5PM1 && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
82
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.m5pm1:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.m5pm1#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → M5Stack M5PM1 看门狗驱动

**配置项引用（Symbol References）**：[`CONFIG_WDT_M5PM1`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_M5PM1)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_MAX32"></a>

## 186.42 `CONFIG_WDT_MAX32`

**提示（Prompt）**：MAX32 看门狗（WDT）驱动

**说明（Help）**

为 MAX32 启用看门狗（WDT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX32_WATCHDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.max32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.max32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_MCHP_G1"></a>

## 186.43 `CONFIG_WDT_MCHP_G1`

**提示（Prompt）**：Microchip G1 看门狗（WDT）驱动

**说明（Help）**

为 Microchip G1 IP 启用看门狗（WDT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_WDT_G1_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_WDT_DISABLE_AT_BOOT
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.mchp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.mchp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_DISABLE_AT_BOOT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_DISABLE_AT_BOOT)。

<a id="CONFIG_WDT_MCUX_COP"></a>

## 186.44 `CONFIG_WDT_MCUX_COP`

**提示（Prompt）**：MCUX COP 驱动

**说明（Help）**

启用 MCUX COP 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_COP_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_WDT_NO_CALLBACKS
CONFIG_HAS_WDT_DISABLE_AT_BOOT
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.mcux:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.mcux#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_NO_CALLBACKS`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_NO_CALLBACKS)、[`CONFIG_HAS_WDT_DISABLE_AT_BOOT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_DISABLE_AT_BOOT)。

<a id="CONFIG_WDT_MCUX_IMX_WDOG"></a>

## 186.45 `CONFIG_WDT_MCUX_IMX_WDOG`

**提示（Prompt）**：MCUX IMX WDOG 驱动

**说明（Help）**

启用 MCUX IMX WDOG 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_WDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.mcux_imx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.mcux_imx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_WDT_MCUX_RTWDOG"></a>

## 186.46 `CONFIG_WDT_MCUX_RTWDOG`

**提示（Prompt）**：MCUX RTWDOG 驱动

**说明（Help）**

启用 MCUX RTWDOG 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_RTWDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.mcux:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.mcux#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_MCUX_WDOG"></a>

## 186.47 `CONFIG_WDT_MCUX_WDOG`

**提示（Prompt）**：MCUX WDOG 驱动

**说明（Help）**

启用 MCUX WDOG 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_KINETIS_WDOG_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.mcux:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.mcux#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_MCUX_WDOG32"></a>

## 186.48 `CONFIG_WDT_MCUX_WDOG32`

**提示（Prompt）**：MCUX WDOG32 驱动

**说明（Help）**

启用 MCUX WDOG32 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_WDOG32_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.mcux:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.mcux#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_MCUX_WWDT"></a>

## 186.49 `CONFIG_WDT_MCUX_WWDT`

**提示（Prompt）**：MCUX WWDT 驱动

**说明（Help）**

启用 MCUX WWDT 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPC_WWDT_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.mcux:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.mcux#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_MCUX_WWDT_WARNING_INTERRUPT_CFG"></a>

## 186.50 `CONFIG_WDT_MCUX_WWDT_WARNING_INTERRUPT_CFG`

**提示（Prompt）**：窗口看门狗（WWDT）超时警告中断配置

**说明（Help）**

窗口看门狗（WWDT）超时警告中断的时间，以距离超时尚余的看门狗计数节拍（Tick）数量表示。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WDT_MCUX_WWDT && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 1023]
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.mcux:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.mcux#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → MCUX WWDT 驱动

**配置项引用（Symbol References）**：[`CONFIG_WDT_MCUX_WWDT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_MCUX_WWDT)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_MSPM0"></a>

## 186.51 `CONFIG_WDT_MSPM0`

**提示（Prompt）**：MSPM0 窗口看门狗（Windowed Watchdog，WWDT）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_MSPM0_WATCHDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.mspm0:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.mspm0#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_MULTISTAGE"></a>

## 186.52 `CONFIG_WDT_MULTISTAGE`

**提示（Prompt）**：多阶段超时（Multistage Timeouts）

**说明（Help）**

启用看门狗超时的多阶段运行（Multistage Operation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_WDT_MULTISTAGE && CONFIG_WATCHDOG
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_WDT_MULTISTAGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_WDT_MULTISTAGE)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_WDT_MULTISTAGE`。

<a id="CONFIG_WDT_NPCX"></a>

## 186.53 `CONFIG_WDT_NPCX`

**提示（Prompt）**：Nuvoton NPCX 嵌入式控制器（EC）看门狗定时器驱动

**说明（Help）**

此选项为 NPCX 系列处理器启用看门狗定时器（Watchdog Timer）驱动。需要在 NPCX 微控制器（MCU）上使用看门狗时，请选择 Y。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NPCX_WATCHDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_WDT_DISABLE_AT_BOOT
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.npcx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.npcx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_DISABLE_AT_BOOT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_DISABLE_AT_BOOT)。

<a id="CONFIG_WDT_NPCX_EX"></a>

## 186.54 `CONFIG_WDT_NPCX_EX`

**提示（Prompt）**：扩展 NPCX 看门狗驱动支持

**说明（Help）**

此选项为 NPCKn 处理器变体启用扩展看门狗定时器（Watchdog Timer）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.npcx:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.npcx#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

<a id="CONFIG_WDT_NPCX_WARNING_LEADING_TIME_MS"></a>

## 186.55 `CONFIG_WDT_NPCX_WARNING_LEADING_TIME_MS`

**提示（Prompt）**：产生看门狗事件／信号前的毫秒数

**说明（Help）**

此选项定义必须处理看门狗事件（Watchdog Event）的时间窗口。窗口结束后，立即触发看门狗复位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WDT_NPCX && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
500
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.npcx:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.npcx#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → Nuvoton NPCX 嵌入式控制器（EC）看门狗定时器驱动

**配置项引用（Symbol References）**：[`CONFIG_WDT_NPCX`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_NPCX)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_NPM10XX"></a>

## 186.56 `CONFIG_WDT_NPM10XX`

**提示（Prompt）**：nPM10xx 看门狗驱动

**说明（Help）**

启用 nPM13xx 看门狗（Watchdog）驱动。

译注：官方数据库的 `CONFIG_WDT_NPM10XX` 与 `CONFIG_WDT_NPM13XX` 均使用这句帮助；在 nPM10xx 选项下，帮助中的型号与标题不一致，此处保留原文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NPM10XX_WDT_ENABLED && DT_HAS_NORDIC_NPM10XX_ENABLED && CONFIG_WATCHDOG
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

**定义位置（Location）**：[`drivers/watchdog/Kconfig.npm10xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.npm10xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_WDT_NPM10XX_INIT_PRIORITY"></a>

## 186.57 `CONFIG_WDT_NPM10XX_INIT_PRIORITY`

**提示（Prompt）**：nPM10xx 看门狗驱动初始化优先级

**说明（Help）**

nPM10xx 看门狗驱动的初始化优先级，必须大于 `MFD_NPM10XX_INIT_PRIORITY`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WDT_NPM10XX && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
85
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.npm10xx:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.npm10xx#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → nPM10xx 看门狗驱动

**配置项引用（Symbol References）**：[`CONFIG_WDT_NPM10XX`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_NPM10XX)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_NPM13XX"></a>

## 186.58 `CONFIG_WDT_NPM13XX`

**提示（Prompt）**：nPM13xx 看门狗驱动

**说明（Help）**

启用 nPM13xx 看门狗（Watchdog）驱动。

译注：官方数据库的 `CONFIG_WDT_NPM10XX` 与 `CONFIG_WDT_NPM13XX` 均使用这句帮助；在 nPM10xx 选项下，帮助中的型号与标题不一致，此处保留原文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_NORDIC_NPM1300_WDT_ENABLED || DT_HAS_NORDIC_NPM1304_WDT_ENABLED) && CONFIG_WATCHDOG
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

**定义位置（Location）**：[`drivers/watchdog/Kconfig.npm13xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.npm13xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_WDT_NPM13XX_INIT_PRIORITY"></a>

## 186.59 `CONFIG_WDT_NPM13XX_INIT_PRIORITY`

**提示（Prompt）**：nPM13xx 看门狗驱动初始化优先级

**说明（Help）**

nPM13xx 看门狗驱动的初始化优先级，必须大于 `GPIO_NPM13XX_INIT_PRIORITY`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WDT_NPM13XX && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
85
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.npm13xx:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.npm13xx#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → nPM13xx 看门狗驱动

**配置项引用（Symbol References）**：[`CONFIG_WDT_NPM13XX`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_NPM13XX)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_NPM2100"></a>

## 186.60 `CONFIG_WDT_NPM2100`

**提示（Prompt）**：nPM2100 看门狗驱动

**说明（Help）**

启用 nPM2100 看门狗（Watchdog）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NPM2100_WDT_ENABLED && CONFIG_WATCHDOG
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

**定义位置（Location）**：[`drivers/watchdog/Kconfig.npm2100:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.npm2100#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_WDT_NPM2100_INIT_PRIORITY"></a>

## 186.61 `CONFIG_WDT_NPM2100_INIT_PRIORITY`

**提示（Prompt）**：nPM2100 看门狗驱动初始化优先级

**说明（Help）**

nPM2100 看门狗驱动的初始化优先级，必须大于 `GPIO_NPM2100_INIT_PRIORITY`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WDT_NPM2100 && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
85
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.npm2100:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.npm2100#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → nPM2100 看门狗驱动

**配置项引用（Symbol References）**：[`CONFIG_WDT_NPM2100`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_NPM2100)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_NPM6001"></a>

## 186.62 `CONFIG_WDT_NPM6001`

**提示（Prompt）**：nPM6001 看门狗驱动

**说明（Help）**

启用 nPM6001 看门狗（Watchdog）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NPM6001_WDT_ENABLED && CONFIG_WATCHDOG
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

**定义位置（Location）**：[`drivers/watchdog/Kconfig.npm6001:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.npm6001#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_WDT_NPM6001_INIT_PRIORITY"></a>

## 186.63 `CONFIG_WDT_NPM6001_INIT_PRIORITY`

**提示（Prompt）**：nPM6001 看门狗驱动初始化优先级

**说明（Help）**

nPM6001 看门狗驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WDT_NPM6001 && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
85
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.npm6001:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.npm6001#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → nPM6001 看门狗驱动

**配置项引用（Symbol References）**：[`CONFIG_WDT_NPM6001`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_NPM6001)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_NRFX"></a>

## 186.64 `CONFIG_WDT_NRFX`

**提示（Prompt）**：nRF WDT nrfx 驱动

**说明（Help）**

为 nRF 微控制器（MCU）系列启用 nrfx 看门狗（WDT）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_WDT_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_WDT
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.nrfx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.nrfx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_NRFX_WDT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_WDT)。

<a id="CONFIG_WDT_NRFX_NO_IRQ"></a>

## 186.65 `CONFIG_WDT_NRFX_NO_IRQ`

**提示（Prompt）**：不启用中断请求（IRQ）的 nRF WDT nrfx 驱动

**说明（Help）**

禁用驱动对看门狗（WDT）中断的使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WDT_NRFX && CONFIG_WATCHDOG
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.nrfx:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.nrfx#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → nRF WDT nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_WDT_NRFX`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_NRFX)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_NRF_GSWDT"></a>

## 186.66 `CONFIG_WDT_NRF_GSWDT`

**提示（Prompt）**：Nordic 全局软件看门狗定时器（Global Software Watchdog Timer，GSWDT）驱动

**说明（Help）**

此选项启用 Nordic 全局软件看门狗定时器（Global Software Watchdog Timer，GSWDT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_GSWDT_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MBOX
CONFIG_HAS_WDT_NO_CALLBACKS
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.nrf_gswdt:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.nrf_gswdt#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)、[`CONFIG_HAS_WDT_NO_CALLBACKS`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_NO_CALLBACKS)。

<a id="CONFIG_WDT_NUMAKER"></a>

## 186.67 `CONFIG_WDT_NUMAKER`

**提示（Prompt）**：Nuvoton NUMAKER MCU 看门狗驱动

**说明（Help）**

此选项为 Nuvoton NuMaker 系列处理器启用看门狗（Watchdog）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NUMAKER_WDT_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.numaker:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.numaker#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_NXP_EWM"></a>

## 186.68 `CONFIG_WDT_NXP_EWM`

**提示（Prompt）**：NXP 外部看门狗监视器（EWM）驱动

**说明（Help）**

启用 NXP 外部看门狗监视器（EWM）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_EWM_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.nxp_ewm:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.nxp_ewm#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_NXP_FS26"></a>

## 186.69 `CONFIG_WDT_NXP_FS26`

**提示（Prompt）**：NXP FS26 系统基础芯片（SBC）看门狗驱动

**说明（Help）**

启用 NXP FS26 系统基础芯片（SBC）看门狗驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_FS26_WDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.nxp_fs26:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.nxp_fs26#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_WDT_NXP_FS26_ERROR_COUNTER_LIMIT"></a>

## 186.70 `CONFIG_WDT_NXP_FS26_ERROR_COUNTER_LIMIT`

**提示（Prompt）**：看门狗错误计数器（Error Counter）上限

**说明（Help）**

设置看门狗错误计数器（Error Counter）的最大值。每次发生看门狗故障时，设备将该计数器加 2；每次正确刷新看门狗时，将其减 1。可选值为 2、4、6、8。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WDT_NXP_FS26 && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
6
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.nxp_fs26:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.nxp_fs26#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → NXP FS26 系统基础芯片（SBC）看门狗驱动

**配置项引用（Symbol References）**：[`CONFIG_WDT_NXP_FS26`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_NXP_FS26)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_NXP_FS26_EXIT_DEBUG_MODE"></a>

## 186.71 `CONFIG_WDT_NXP_FS26_EXIT_DEBUG_MODE`

**提示（Prompt）**：退出调试模式（DEBUG Mode）

**说明（Help）**

如果设备在调试模式（DEBUG Mode）下启动，驱动将退出该模式，以启用看门狗。否则，如果设备处于调试模式且启用了此驱动，初始化将失败。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WDT_NXP_FS26 && CONFIG_WATCHDOG
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.nxp_fs26:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.nxp_fs26#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → NXP FS26 系统基础芯片（SBC）看门狗驱动

**配置项引用（Symbol References）**：[`CONFIG_WDT_NXP_FS26`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_NXP_FS26)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_NXP_FS26_INIT_PRIORITY"></a>

## 186.72 `CONFIG_WDT_NXP_FS26_INIT_PRIORITY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

设备驱动初始化优先级。设备连接到 SPI 总线，因此必须在 SPI 驱动之后初始化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WDT_NXP_FS26 && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.nxp_fs26:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.nxp_fs26#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → NXP FS26 系统基础芯片（SBC）看门狗驱动

**配置项引用（Symbol References）**：[`CONFIG_WDT_NXP_FS26`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_NXP_FS26)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_NXP_FS26_INT_THREAD_PRIO"></a>

## 186.73 `CONFIG_WDT_NXP_FS26_INT_THREAD_PRIO`

**提示（Prompt）**：内部传入数据包处理线程（Incoming Packet Handler）的优先级

**说明（Help）**

用于中断处理的内部协作式线程（Cooperative Thread）的优先级等级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WDT_NXP_FS26 && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.nxp_fs26:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.nxp_fs26#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → NXP FS26 系统基础芯片（SBC）看门狗驱动

**配置项引用（Symbol References）**：[`CONFIG_WDT_NXP_FS26`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_NXP_FS26)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_NXP_FS26_INT_THREAD_STACK_SIZE"></a>

## 186.74 `CONFIG_WDT_NXP_FS26_INT_THREAD_STACK_SIZE`

**提示（Prompt）**：内部中断处理程序的栈大小

**说明（Help）**

用于中断处理的内部线程的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WDT_NXP_FS26 && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.nxp_fs26:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.nxp_fs26#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → NXP FS26 系统基础芯片（SBC）看门狗驱动

**配置项引用（Symbol References）**：[`CONFIG_WDT_NXP_FS26`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_NXP_FS26)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_NXP_FS26_REFRESH_COUNTER_LIMIT"></a>

## 186.75 `CONFIG_WDT_NXP_FS26_REFRESH_COUNTER_LIMIT`

**提示（Prompt）**：看门狗刷新计数器（Refresh Counter）上限

**说明（Help）**

设置看门狗刷新计数器（Refresh Counter）的最大值。每次正确刷新看门狗时，该计数器加 1。计数器达到最大值后，如果下一次刷新仍然正确，则故障错误计数器（Fault Error Counter）减 1。每次看门狗刷新错误时，刷新计数器复位为 0。可选值为 1、2、4、6。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WDT_NXP_FS26 && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
6
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.nxp_fs26:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.nxp_fs26#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → NXP FS26 系统基础芯片（SBC）看门狗驱动

**配置项引用（Symbol References）**：[`CONFIG_WDT_NXP_FS26`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_NXP_FS26)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_NXP_FS26_SEED"></a>

## 186.76 `CONFIG_WDT_NXP_FS26_SEED`

**提示（Prompt）**：看门狗种子（Watchdog Seed）

**说明（Help）**

传递给设备的种子（Seed），可用于简单看门狗（Simple Watchdog）和挑战式看门狗（Challenger Watchdog）配置。简单看门狗配置不允许使用 `0xffff` 和 `0x0000`；挑战式看门狗配置不允许使用 `0x0000`。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_WDT_NXP_FS26 && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
0x5ab2
```

**取值范围（Ranges）**

```text
[0x0, 0xffff]
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.nxp_fs26:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.nxp_fs26#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → NXP FS26 系统基础芯片（SBC）看门狗驱动

**配置项引用（Symbol References）**：[`CONFIG_WDT_NXP_FS26`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_NXP_FS26)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_NXP_FS26_SPI_8BIT_TRANSFER"></a>

## 186.77 `CONFIG_WDT_NXP_FS26_SPI_8BIT_TRANSFER`

**提示（Prompt）**：FS26 使用 8 位 SPI 传输模式

**说明（Help）**

启用后，强制 FS26 驱动使用 8 位 SPI 传输，代替默认的 32 位传输。使用不支持 32 位字宽的 SPI 控制器，例如 `SPI_RTIO`，或应用严格要求以字节为单位传输时，需要启用。禁用时，FS26 驱动继续按原始实现使用 32 位 SPI 传输。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WDT_NXP_FS26 && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y if CONFIG_SPI_RTIO
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.nxp_fs26:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.nxp_fs26#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → NXP FS26 系统基础芯片（SBC）看门狗驱动

**配置项引用（Symbol References）**：[`CONFIG_WDT_NXP_FS26`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_NXP_FS26)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_SPI_RTIO`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RTIO)。

<a id="CONFIG_WDT_NXP_S32"></a>

## 186.78 `CONFIG_WDT_NXP_S32`

**提示（Prompt）**：NXP S32 软件看门狗定时器（SWT）驱动

**说明（Help）**

启用软件看门狗定时器（Software Watchdog Timer，SWT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_S32_SWT_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CLOCK_CONTROL
CONFIG_NOCACHE_MEMORY if CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.nxp_s32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.nxp_s32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_WDT_OPENTITAN"></a>

## 186.79 `CONFIG_WDT_OPENTITAN`

**提示（Prompt）**：OpenTitan 常开（Always-On，AON）定时器

**说明（Help）**

此选项启用 OpenTitan 常开（AON）定时器中看门狗部分的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LOWRISC_OPENTITAN_AONTIMER_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_WDT_MULTISTAGE
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.opentitan:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.opentitan#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_MULTISTAGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_WDT_MULTISTAGE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_WDT_MULTISTAGE`。

<a id="CONFIG_WDT_RENESAS_RA"></a>

## 186.80 `CONFIG_WDT_RENESAS_RA`

**提示（Prompt）**：Renesas RA 系列看门狗驱动

**说明（Help）**

为 Renesas RA 微控制器（MCU）启用看门狗（Watchdog）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_WDT_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_WDT_DISABLE_AT_BOOT
CONFIG_SOC_OPTION_SETTING_MEMORY if CONFIG_SOC_SERIES_RA4M1
CONFIG_USE_RA_FSP_WDT
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.renesas_ra:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.renesas_ra#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_DISABLE_AT_BOOT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_DISABLE_AT_BOOT)、[`CONFIG_SOC_OPTION_SETTING_MEMORY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_OPTION_SETTING_MEMORY)、[`CONFIG_SOC_SERIES_RA4M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M1)、[`CONFIG_USE_RA_FSP_WDT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_WDT)。

<a id="CONFIG_WDT_RENESAS_RA_NMI"></a>

## 186.81 `CONFIG_WDT_RENESAS_RA_NMI`

**提示（Prompt）**：启用不可屏蔽中断（NMI）

**说明（Help）**

看门狗定时器在值为 0 时产生不可屏蔽中断（NMI）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WDT_RENESAS_RA && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_RUNTIME_NMI
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.renesas_ra:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.renesas_ra#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → Renesas RA 系列看门狗驱动

**配置项引用（Symbol References）**：[`CONFIG_WDT_RENESAS_RA`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_RENESAS_RA)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_RUNTIME_NMI`](P030_arch_arm_配置项参考_2.md#CONFIG_RUNTIME_NMI)。

<a id="CONFIG_WDT_RENESAS_RA_START_IN_BOOT"></a>

## 186.82 `CONFIG_WDT_RENESAS_RA_START_IN_BOOT`

**提示（Prompt）**：启动时开启看门狗（WDT）

**说明（Help）**

在启动时开启看门狗（Watchdog）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_HAS_WDT_DISABLE_AT_BOOT && CONFIG_WDT_RENESAS_RA && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.renesas_ra:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.renesas_ra#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → Renesas RA 系列看门狗驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_WDT_DISABLE_AT_BOOT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_DISABLE_AT_BOOT)、[`CONFIG_WDT_RENESAS_RA`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_RENESAS_RA)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_RENESAS_RX_IWDT"></a>

## 186.83 `CONFIG_WDT_RENESAS_RX_IWDT`

**提示（Prompt）**：Renesas RX 系列独立看门狗（Independent Watchdog）驱动

**说明（Help）**

启用 Renesas RX 系列看门狗（Watchdog）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RX_IWDT_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_WDT_DISABLE_AT_BOOT if CONFIG_WDT_RENESAS_RX_IWDT_REGISTER_START_MODE
CONFIG_USE_RX_RDP_IWDT
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.renesas_rx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.renesas_rx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_DISABLE_AT_BOOT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_DISABLE_AT_BOOT)、[`CONFIG_WDT_RENESAS_RX_IWDT_REGISTER_START_MODE`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_RENESAS_RX_IWDT_REGISTER_START_MODE)、[`CONFIG_USE_RX_RDP_IWDT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RX_RDP_IWDT)。

<a id="CONFIG_WDT_RENESAS_RX_IWDT_AUTO_START_MODE"></a>

## 186.84 `CONFIG_WDT_RENESAS_RX_IWDT_AUTO_START_MODE`

**提示（Prompt）**：复位时自动启动独立看门狗（IWDT）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.renesas_rx:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.renesas_rx#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → Renesas RX 系列独立看门狗（Independent Watchdog）驱动 → 独立看门狗（IWDT）启动模式

<a id="CONFIG_WDT_RENESAS_RX_IWDT_REGISTER_START_MODE"></a>

## 186.85 `CONFIG_WDT_RENESAS_RX_IWDT_REGISTER_START_MODE`

**提示（Prompt）**：选择独立看门狗（IWDT）启动模式。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.renesas_rx:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.renesas_rx#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → Renesas RX 系列独立看门狗（Independent Watchdog）驱动 → 独立看门狗（IWDT）启动模式

<a id="CONFIG_WDT_RENESAS_RX_IWDT_USE_NMI"></a>

## 186.86 `CONFIG_WDT_RENESAS_RX_IWDT_USE_NMI`

**提示（Prompt）**：独立看门狗（IWDT）的不可屏蔽中断（NMI）

**说明（Help）**

为独立看门狗（IWDT）启用不可屏蔽中断（NMI）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WDT_RENESAS_RX_IWDT && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.renesas_rx:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.renesas_rx#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → Renesas RX 系列独立看门狗（Independent Watchdog）驱动

**配置项引用（Symbol References）**：[`CONFIG_WDT_RENESAS_RX_IWDT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_RENESAS_RX_IWDT)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_RENESAS_RZ"></a>

## 186.87 `CONFIG_WDT_RENESAS_RZ`

**提示（Prompt）**：Renesas RZ 看门狗驱动

**说明（Help）**

为 Renesas RZ 启用看门狗（Watchdog）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_WDT_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_WDT_DISABLE_AT_BOOT
CONFIG_USE_RZ_FSP_WDT
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.renesas_rz:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.renesas_rz#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_DISABLE_AT_BOOT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_DISABLE_AT_BOOT)、[`CONFIG_USE_RZ_FSP_WDT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_WDT)。

<a id="CONFIG_WDT_RENESAS_RZ_USE_ICU"></a>

## 186.88 `CONFIG_WDT_RENESAS_RZ_USE_ICU`

**提示（Prompt）**：看门狗产生中断请求信号（Interrupt Request Signal）

**说明（Help）**

看门狗产生中断请求信号（Interrupt Request Signal）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_RZT2M || CONFIG_SOC_SERIES_RZN2L) && CONFIG_WDT_RENESAS_RZ && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.renesas_rz:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.renesas_rz#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → Renesas RZ 看门狗驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RZT2M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2M)、[`CONFIG_SOC_SERIES_RZN2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZN2L)、[`CONFIG_WDT_RENESAS_RZ`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_RENESAS_RZ)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_RPI_PICO"></a>

## 186.89 `CONFIG_WDT_RPI_PICO`

**提示（Prompt）**：Raspberry Pi Pico 看门狗驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RASPBERRYPI_PICO_WATCHDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_WDT_NO_CALLBACKS
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.rpi_pico:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.rpi_pico#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_NO_CALLBACKS`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_NO_CALLBACKS)。

<a id="CONFIG_WDT_RTS5817"></a>

## 186.90 `CONFIG_WDT_RTS5817`

**提示（Prompt）**：Realtek RTS5817 看门狗驱动

**说明（Help）**

Realtek RTS5817 看门狗（Watchdog）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_RTS5817_WATCHDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_WDT_DISABLE_AT_BOOT
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.rts5817:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.rts5817#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_DISABLE_AT_BOOT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_DISABLE_AT_BOOT)。

<a id="CONFIG_WDT_RTS5912"></a>

## 186.91 `CONFIG_WDT_RTS5912`

**提示（Prompt）**：Realtek RTS5912 嵌入式控制器看门狗驱动

**说明（Help）**

此选项为 Realtek RTS5912 系列处理器启用看门狗（WDT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_RTS5912_WATCHDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_WDT_DISABLE_AT_BOOT
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.rts5912:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.rts5912#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_DISABLE_AT_BOOT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_DISABLE_AT_BOOT)。

<a id="CONFIG_WDT_SAM"></a>

## 186.92 `CONFIG_WDT_SAM`

**提示（Prompt）**：Atmel SAM MCU 系列看门狗（WDT）驱动

**说明（Help）**

为 Atmel SAM 微控制器（MCU）启用看门狗（WDT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM_WATCHDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_WDT_DISABLE_AT_BOOT
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.sam:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.sam#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_DISABLE_AT_BOOT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_DISABLE_AT_BOOT)。

<a id="CONFIG_WDT_SAM0"></a>

## 186.93 `CONFIG_WDT_SAM0`

**提示（Prompt）**：Atmel SAM0 系列看门狗（WDT）驱动

**说明（Help）**

为 Atmel SAM0 微控制器（MCU）启用看门狗（WDT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM0_WATCHDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_WDT_DISABLE_AT_BOOT
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.sam0:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.sam0#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_DISABLE_AT_BOOT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_DISABLE_AT_BOOT)。

<a id="CONFIG_WDT_SAM4L"></a>

## 186.94 `CONFIG_WDT_SAM4L`

**提示（Prompt）**：Atmel SAM4L MCU 系列看门狗（WDT）驱动

**说明（Help）**

为 Atmel SAM4L 微控制器（MCU）启用看门狗（WDT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM4L_WATCHDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_WDT_DISABLE_AT_BOOT
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.sam4l:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.sam4l#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_DISABLE_AT_BOOT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_DISABLE_AT_BOOT)。

<a id="CONFIG_WDT_SF32LB"></a>

## 186.95 `CONFIG_WDT_SF32LB`

**提示（Prompt）**：SF32LB 看门狗（WDT）驱动

**说明（Help）**

为 SF32LB 系列微控制器（MCU）启用看门狗（WDT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFLI_SF32LB_WDT_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_WDT_DISABLE_AT_BOOT
CONFIG_HAS_WDT_NO_CALLBACKS
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.sf32lb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.sf32lb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_DISABLE_AT_BOOT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_DISABLE_AT_BOOT)、[`CONFIG_HAS_WDT_NO_CALLBACKS`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_NO_CALLBACKS)。

<a id="CONFIG_WDT_SHELL"></a>

## 186.96 `CONFIG_WDT_SHELL`

**提示（Prompt）**：看门狗命令行（WDT Shell）

**说明（Help）**

启用看门狗命令行（WDT Shell）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_WATCHDOG
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.shell:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.shell#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_SIFIVE"></a>

## 186.97 `CONFIG_WDT_SIFIVE`

**提示（Prompt）**：SiFive 看门狗（WDT）驱动

**说明（Help）**

此选项为 SiFive Freedom 启用看门狗（WDT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFIVE_WDT_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_WDT_DISABLE_AT_BOOT
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.sifive:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.sifive#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_DISABLE_AT_BOOT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_DISABLE_AT_BOOT)。

<a id="CONFIG_WDT_SILABS_SIWX91X"></a>

## 186.98 `CONFIG_WDT_SILABS_SIWX91X`

**提示（Prompt）**：Silabs SiWx91x 看门狗驱动

**说明（Help）**

为 Silabs SiWx91x 片上系统（SoC）系列启用看门狗（Watchdog）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SIWX91X_WDT_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.silabs:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.silabs#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_SILABS_WDOG"></a>

## 186.99 `CONFIG_WDT_SILABS_WDOG`

**提示（Prompt）**：Silabs Series 3 看门狗驱动

**说明（Help）**

为 Silicon Labs Series 3 器件启用看门狗（Watchdog）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_WDOG_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_WDT_DISABLE_AT_BOOT
CONFIG_HAS_WDT_MULTISTAGE
CONFIG_SILABS_SISDK_WDOG
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.silabs:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.silabs#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_DISABLE_AT_BOOT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_DISABLE_AT_BOOT)、[`CONFIG_HAS_WDT_MULTISTAGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_WDT_MULTISTAGE)、[`CONFIG_SILABS_SISDK_WDOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_WDOG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_WDT_MULTISTAGE`。

<a id="CONFIG_WDT_SMARTBOND"></a>

## 186.100 `CONFIG_WDT_SMARTBOND`

**提示（Prompt）**：SmartBond MCU 系列看门狗驱动

**说明（Help）**

为 SmartBond 微控制器（MCU）系列启用看门狗（Watchdog）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_SMARTBOND_WATCHDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_WDT_DISABLE_AT_BOOT
CONFIG_HAS_WDT_NO_CALLBACKS if !CONFIG_WDT_SMARTBOND_NMI
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.smartbond:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.smartbond#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_DISABLE_AT_BOOT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_DISABLE_AT_BOOT)、[`CONFIG_HAS_WDT_NO_CALLBACKS`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_NO_CALLBACKS)、[`CONFIG_WDT_SMARTBOND_NMI`](P187_drivers_watchdog_配置项参考_2.md#CONFIG_WDT_SMARTBOND_NMI)。

<!-- kconfig-navigation -->

[上一章](P185_drivers_w1_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P187_drivers_watchdog_配置项参考_2.md)
