---
id: learning.zephyr-docs.kconfig-reference.page-69
title: "`drivers/counter`配置项参考（2/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第69章\_`drivers/counter`配置项参考（2/2）

本章翻译官方 Kconfig 数据库中 `drivers/counter` 的 9 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_COUNTER_TMR_ESP32"></a>

## 69.1 `CONFIG_COUNTER_TMR_ESP32`

**提示（Prompt）**：基于通用定时器的 ESP32 计数器驱动（GP-Timer Counter Driver）

**说明（Help）**

为 ESP32 系列器件启用基于乐鑫（Espressif）通用定时器（General Purpose Timer）的计数器（Counter）驱动 API。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_COUNTER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_COUNTER_SUPPORTS_64BITS_TICKS
CONFIG_COUNTER_SUPPORTS_CAPTURE if CONFIG_SOC_ESP32_ETM_SUPPORTED
```

**定义位置（Location）**：[`drivers/counter/Kconfig.esp32_tmr:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.esp32_tmr#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_COUNTER_SUPPORTS_64BITS_TICKS`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_SUPPORTS_64BITS_TICKS)、[`CONFIG_COUNTER_SUPPORTS_CAPTURE`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_SUPPORTS_CAPTURE)、[`CONFIG_SOC_ESP32_ETM_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32_ETM_SUPPORTED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_ESP32_ETM_SUPPORTED`。

<a id="CONFIG_COUNTER_TMR_ESP32_CAPTURE"></a>

## 69.2 `CONFIG_COUNTER_TMR_ESP32_CAPTURE`

**提示（Prompt）**：ESP32 通用定时器通过 ETM 捕获计数器值（Counter Capture via ETM）

**说明（Help）**

为 ESP32 通用定时器（GP-Timer）计数器驱动启用 GPIO 边沿触发捕获（Edge-Triggered Counter Capture）。GPIO 边沿通过事件任务矩阵（Event Task Matrix，ETM）路由到定时器捕获任务，使硬件在边沿到来时锁存（Latch）计数值。仅适用于定时器和 GPIO 外设都提供 ETM 的片上系统（SoC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COUNTER_TMR_ESP32 && CONFIG_COUNTER_CAPTURE && CONFIG_SOC_ESP32_ETM_SUPPORTED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ESP32_ETM
```

**定义位置（Location）**：[`drivers/counter/Kconfig.esp32_tmr:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.esp32_tmr#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers） → 基于通用定时器的 ESP32 计数器驱动（GP-Timer Counter Driver）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER_TMR_ESP32`](P069_drivers_counter_配置项参考_2.md#CONFIG_COUNTER_TMR_ESP32)、[`CONFIG_COUNTER_CAPTURE`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_CAPTURE)、[`CONFIG_SOC_ESP32_ETM_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32_ETM_SUPPORTED)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_ESP32_ETM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP32_ETM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_ESP32_ETM_SUPPORTED`。

<a id="CONFIG_COUNTER_WUT_MAX32"></a>

## 69.3 `CONFIG_COUNTER_WUT_MAX32`

**提示（Prompt）**：MAX32xxx 唤醒定时器驱动（Wake-Up Timer Driver）

**说明（Help）**

启用 MAX32 微控制器（MCU）的唤醒定时器（Wake-Up Timer）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX32_WUT_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.max32_wut:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.max32_wut#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_XEC"></a>

## 69.4 `CONFIG_COUNTER_XEC`

**提示（Prompt）**：Microchip XEC 系列计数器驱动（Counter Driver）

**说明（Help）**

启用 Microchip XEC 微控制器（MCU）系列的计数器（Counter）驱动，将 MCU 中的基本定时器（Basic Timer）暴露为设备。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_XEC_TIMER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.xec:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.xec#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_XLNX_AXI_TIMER"></a>

## 69.5 `CONFIG_COUNTER_XLNX_AXI_TIMER`

**提示（Prompt）**：Xilinx AXI 定时器驱动（AXI Timer Driver）

**说明（Help）**

启用 Xilinx AXI Timer v2.0 IP 的计数器（Counter）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XLNX_XPS_TIMER_1_00_A_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.xlnx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.xlnx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_COUNTER_XLNX_TTC"></a>

## 69.6 `CONFIG_COUNTER_XLNX_TTC`

**提示（Prompt）**：Xilinx 三重定时器计数器驱动（Triple Timer Counter，TTC）

**说明（Help）**

启用 Xilinx 三重定时器计数器（TTC）驱动。TTC 模块中的每个定时器都被视为独立的计数器设备（Counter Device）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XLNX_TTC_COUNTER_ENABLED && CONFIG_GIC && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DYNAMIC_INTERRUPTS
```

**定义位置（Location）**：[`drivers/counter/Kconfig.xlnx_ttc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.xlnx_ttc#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_GIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GIC)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_DYNAMIC_INTERRUPTS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DYNAMIC_INTERRUPTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_GIC`。

<a id="CONFIG_COUNTER_XLNX_ZYNQMP_RTC"></a>

## 69.7 `CONFIG_COUNTER_XLNX_ZYNQMP_RTC`

**提示（Prompt）**：Xilinx ZynqMP RTC 驱动（Driver）

**说明（Help）**

启用 Xilinx Zynq UltraScale+ MPSoC 实时时钟（Real Time Clock）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XLNX_ZYNQMP_RTC_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.xlnx_zynqmp_rtc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.xlnx_zynqmp_rtc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_TIMER_DTMR_CMSDK_APB"></a>

## 69.8 `CONFIG_TIMER_DTMR_CMSDK_APB`

**提示（Prompt）**：ARM CMSDK 双定时器驱动（Cortex-M System Design Kit DTMR Timer Driver）

**说明（Help）**

将平台上的双定时器（Dualtimer，DTMR）用作定时器。启用此选项可提供该定时器支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ARM_CMSDK_DTIMER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.dtmr_cmsdk_apb:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.dtmr_cmsdk_apb#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_TIMER_TMR_CMSDK_APB"></a>

## 69.9 `CONFIG_TIMER_TMR_CMSDK_APB`

**提示（Prompt）**：ARM CMSDK 定时器驱动（Cortex-M System Design Kit Timer Driver）

**说明（Help）**

将平台上的定时器（TMR）用作定时器。启用此选项可提供这些定时器的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ARM_CMSDK_TIMER_ENABLED && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/counter/Kconfig.tmr_cmsdk_apb:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/Kconfig.tmr_cmsdk_apb#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<!-- kconfig-navigation -->

[上一章](P068_drivers_counter_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P070_drivers_crc_配置项参考.md)
