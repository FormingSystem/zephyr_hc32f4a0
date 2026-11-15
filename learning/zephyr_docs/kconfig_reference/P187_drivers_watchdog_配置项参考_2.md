---
id: learning.zephyr-docs.kconfig-reference.page-187
title: "`drivers/watchdog`配置项参考（2/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第187章\_`drivers/watchdog`配置项参考（2/2）

本章翻译官方 Kconfig 数据库中 `drivers/watchdog` 的 15 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_WDT_SMARTBOND_NMI"></a>

## 187.1 `CONFIG_WDT_SMARTBOND_NMI`

**提示（Prompt）**：启用复位前不可屏蔽中断（NMI Pre-reset Interrupt）

**说明（Help）**

看门狗定时器在值为 0 时产生不可屏蔽中断（NMI），在值小于或等于 -16 时产生 WDOG（SYS）复位。可通过 `SET_FREEZE_REG[FRZ_WDOG]`／`RESET_FREEZE_REG[FRZ_WDOG]` 冻结／恢复定时器。

未设置此选项时，看门狗定时器在值为 0 时产生 WDOG（SYS）复位，且无法由软件冻结。注意，软件只能将此位置为 1；只有 WDOG（SYS）复位或软件复位才能将其清零。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WDT_SMARTBOND && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_RUNTIME_NMI
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.smartbond:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.smartbond#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → SmartBond MCU 系列看门狗驱动

**配置项引用（Symbol References）**：[`CONFIG_WDT_SMARTBOND`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_SMARTBOND)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_RUNTIME_NMI`](P030_arch_arm_配置项参考_2.md#CONFIG_RUNTIME_NMI)。

<a id="CONFIG_WDT_TCO"></a>

## 187.2 `CONFIG_WDT_TCO`

**提示（Prompt）**：Intel TCO 看门狗驱动

**说明（Help）**

启用 Intel TCO 看门狗（WDT）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_TCO_WDT_ENABLED && CONFIG_WATCHDOG
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

**定义位置（Location）**：[`drivers/watchdog/Kconfig.tco:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.tco#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_DISABLE_AT_BOOT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_DISABLE_AT_BOOT)、[`CONFIG_HAS_WDT_NO_CALLBACKS`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_NO_CALLBACKS)。

<a id="CONFIG_WDT_TI_RTI"></a>

## 187.3 `CONFIG_WDT_TI_RTI`

**提示（Prompt）**：TI K3 看门狗驱动

**说明（Help）**

启用 K3 代处理器中的看门狗定时器（Watchdog Timer，RTI 模块）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_J7_RTI_WDT_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_WDT_DISABLE_AT_BOOT
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.ti_rti:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.ti_rti#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_DISABLE_AT_BOOT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_DISABLE_AT_BOOT)。

<a id="CONFIG_WDT_TI_TPS382X"></a>

## 187.4 `CONFIG_WDT_TI_TPS382X`

**提示（Prompt）**：外部 TI TPS382x 看门狗（WDT）驱动

**说明（Help）**

为 TI TPS382x 启用看门狗（WDT）驱动。它是一个外部集成电路（IC），需要与处理器建立 GPIO 连接。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_TPS382X_ENABLED && CONFIG_GPIO && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_WDT_NO_CALLBACKS
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.ti_tps382x:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.ti_tps382x#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_NO_CALLBACKS`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_NO_CALLBACKS)。

<a id="CONFIG_WDT_XEC"></a>

## 187.5 `CONFIG_WDT_XEC`

**提示（Prompt）**：Microchip XEC 系列看门狗定时器（WDT）驱动

**说明（Help）**

为 Microchip XEC 微控制器（MCU）系列启用看门狗（WDT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_XEC_WATCHDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_WDT_DISABLE_AT_BOOT
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.xec:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.xec#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_DISABLE_AT_BOOT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_DISABLE_AT_BOOT)。

<a id="CONFIG_WDT_XEN"></a>

## 187.6 `CONFIG_WDT_XEN`

**提示（Prompt）**：Xen 域看门狗（Domain Watchdog）驱动

**说明（Help）**

启用以 Xen `SCHEDOP_watchdog` 为后端的看门狗驱动。通过 Zephyr 看门狗 API，为当前 Xen 域（Domain）提供 Xen 域看门狗定时器。Xen 提供两个域看门狗定时器槽位，映射为可配置的 Zephyr 看门狗通道。

超时由 Xen 按该域的 `on_watchdog` 策略处理，因此不支持超时前回调（Pre-timeout Callback）。Xen 接受以整秒为单位的看门狗超时值。短于一秒的超时窗口会被拒绝；较长的毫秒值则向上取整到下一整秒。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XEN && DT_HAS_XEN_WATCHDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_WDT_NO_CALLBACKS
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.xen:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.xen#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_XEN`](P031_arch_arm64_配置项参考.md#CONFIG_XEN)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_NO_CALLBACKS`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_NO_CALLBACKS)。

<a id="CONFIG_WDT_XILINX_AXI"></a>

## 187.7 `CONFIG_WDT_XILINX_AXI`

**提示（Prompt）**：Xilinx AXI Timebase 看门狗（WDT）驱动

**说明（Help）**

启用 Xilinx AXI Timebase 看门狗（WDT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XLNX_XPS_TIMEBASE_WDT_1_00_A_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.xlnx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.xlnx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_XILINX_AXI_HWINFO_API"></a>

## 187.8 `CONFIG_WDT_XILINX_AXI_HWINFO_API`

**提示（Prompt）**：在 Xilinx AXI Timebase WDT 驱动中提供硬件信息（HWINFO）API

**说明（Help）**

控制 Xilinx AXI Timebase WDT 驱动是否提供硬件信息（HWINFO）API，用于判断上一次系统复位是否由看门狗（WDT）触发。如果设备或片上系统（SoC）已实现此 API，可能需要禁用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WDT_XILINX_AXI && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.xlnx:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.xlnx#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → Xilinx AXI Timebase 看门狗（WDT）驱动

**配置项引用（Symbol References）**：[`CONFIG_WDT_XILINX_AXI`](P187_drivers_watchdog_配置项参考_2.md#CONFIG_WDT_XILINX_AXI)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)。

<a id="CONFIG_WDT_XMC4XXX"></a>

## 187.9 `CONFIG_WDT_XMC4XXX`

**提示（Prompt）**：Infineon XMC4xxx MCU 系列看门狗（WDT）驱动

**说明（Help）**

为 Infineon XMC4xxx 微控制器（MCU）启用看门狗（WDT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_XMC4XXX_WATCHDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_WDT_DISABLE_AT_BOOT
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.xmc4xxx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.xmc4xxx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_DISABLE_AT_BOOT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_DISABLE_AT_BOOT)。

<a id="CONFIG_WDT_XMC4XXX_DEFAULT_TIMEOUT_MAX_MS"></a>

## 187.10 `CONFIG_WDT_XMC4XXX_DEFAULT_TIMEOUT_MAX_MS`

**提示（Prompt）**：启动时使用的默认看门狗超时时间

**说明（Help）**

启动时未禁用看门狗的情况下，使用的默认看门狗超时时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WDT_XMC4XXX && !CONFIG_WDT_DISABLE_AT_BOOT && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
20000
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.xmc4xxx:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.xmc4xxx#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → Infineon XMC4xxx MCU 系列看门狗（WDT）驱动

**配置项引用（Symbol References）**：[`CONFIG_WDT_XMC4XXX`](P187_drivers_watchdog_配置项参考_2.md#CONFIG_WDT_XMC4XXX)、[`CONFIG_WDT_DISABLE_AT_BOOT`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_DISABLE_AT_BOOT)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WDT_XT_ESP32"></a>

## 187.11 `CONFIG_WDT_XT_ESP32`

**提示（Prompt）**：ESP32 外部 32K 晶体看门狗驱动

**说明（Help）**

为 ESP32 启用看门狗（WDT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_XT_WDT_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.esp32:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.esp32#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WWDGT_GD32"></a>

## 187.12 `CONFIG_WWDGT_GD32`

**提示（Prompt）**：GD32 窗口看门狗定时器（Window Watchdog Timer，WWDGT）驱动

**说明（Help）**

为 GD32 片上系统（SoC）启用窗口看门狗定时器（Window Watchdog Timer，WWDGT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GD_GD32_WWDGT_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_WDT_NO_CALLBACKS
CONFIG_USE_GD32_WWDGT
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.gd32:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.gd32#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_HAS_WDT_NO_CALLBACKS`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_HAS_WDT_NO_CALLBACKS)、[`CONFIG_USE_GD32_WWDGT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_GD32_WWDGT)。

<a id="CONFIG_WWDG_STM32"></a>

## 187.13 `CONFIG_WWDG_STM32`

**提示（Prompt）**：STM32 MCU 系列的系统窗口看门狗（System Window Watchdog，WWDG）驱动

**说明（Help）**

为 STM32 微控制器（MCU）系列启用窗口看门狗（WWDG）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_WINDOW_WATCHDOG_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.stm32:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.stm32#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_WWDT_NUMAKER"></a>

## 187.14 `CONFIG_WWDT_NUMAKER`

**提示（Prompt）**：Nuvoton NUMAKER MCU 窗口看门狗驱动

**说明（Help）**

此选项为 Nuvoton NuMaker 系列处理器启用窗口看门狗（Window Watchdog）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NUMAKER_WWDT_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.numaker:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.numaker#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<a id="CONFIG_XILINX_WINDOW_WATCHDOG"></a>

## 187.15 `CONFIG_XILINX_WINDOW_WATCHDOG`

**提示（Prompt）**：Xilinx 窗口看门狗（Window Watchdog）驱动

**说明（Help）**

为 `versal_wwdt` IP 核启用窗口看门狗（Window Watchdog）驱动。窗口看门狗定时器（WWDT）包含第一个关闭窗口（Closed Window）和第二个开放窗口（Open Window），计数宽度为 32 位。必须在预定义的时间窗口内写入看门狗，既不能过早，也不能过晚。WWDT 必须在开放窗口内重新启动；软件尝试在开放窗口之外重新启动 WWDT 时，将触发片上系统（SoC）复位。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XLNX_VERSAL_WWDT_ENABLED && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/watchdog/Kconfig.xilinx_wwdt:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/Kconfig.xilinx_wwdt#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)。

<!-- kconfig-navigation -->

[上一章](P186_drivers_watchdog_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P188_drivers_wifi_配置项参考_1.md)
