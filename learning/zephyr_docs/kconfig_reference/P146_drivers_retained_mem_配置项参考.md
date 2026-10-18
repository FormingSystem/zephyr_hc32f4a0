---
id: learning.zephyr-docs.kconfig-reference.page-146
title: "`drivers/retained_mem`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第146章\_`drivers/retained_mem`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/retained_mem` 的 11 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_RETAINED_MEM"></a>

## 146.1 `CONFIG_RETAINED_MEM`

**提示（Prompt）**：保留内存（Retained Memory）驱动

**说明（Help）**

启用在设备保持供电时能够保留数据的驱动支持；数据在低功耗状态下可能丢失。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_INSTRUMENTATION_DYNAMIC_TRIGGER
```

**定义位置（Location）**：[`drivers/retained_mem/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/retained_mem/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INSTRUMENTATION_DYNAMIC_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INSTRUMENTATION_DYNAMIC_TRIGGER)。

<a id="CONFIG_RETAINED_MEM_GD32_BKPSRAM"></a>

## 146.2 `CONFIG_RETAINED_MEM_GD32_BKPSRAM`

**提示（Prompt）**：GD32 备份 SRAM 保留内存

**说明（Help）**

启用 GD32 备份 SRAM 的保留内存驱动。此驱动启用 BKPSRAM 时钟门控。要启用备份 SRAM 低压差稳压器（BLDO）以实现数据保留，应使用通过设备树 `vin-supply` 属性引用的稳压器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GD_GD32_BACKUP_SRAM_ENABLED && CONFIG_RETAINED_MEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/retained_mem/Kconfig.gd32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/retained_mem/Kconfig.gd32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 保留内存（Retained Memory）驱动

**配置项引用（Symbol References）**：[`CONFIG_RETAINED_MEM`](P146_drivers_retained_mem_配置项参考.md#CONFIG_RETAINED_MEM)。

<a id="CONFIG_RETAINED_MEM_INIT_PRIORITY"></a>

## 146.3 `CONFIG_RETAINED_MEM_INIT_PRIORITY`

**提示（Prompt）**：保留内存设备初始化优先级

**说明（Help）**

保留内存设备的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RETAINED_MEM
```

**默认值（Defaults）**

```text
40
```

**定义位置（Location）**：[`drivers/retained_mem/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/retained_mem/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 保留内存（Retained Memory）驱动

**配置项引用（Symbol References）**：[`CONFIG_RETAINED_MEM`](P146_drivers_retained_mem_配置项参考.md#CONFIG_RETAINED_MEM)。

<a id="CONFIG_RETAINED_MEM_MUTEX_FORCE_DISABLE"></a>

## 146.4 `CONFIG_RETAINED_MEM_MUTEX_FORCE_DISABLE`

**提示（Prompt）**：禁用保留内存互斥锁（Mutex）支持

**说明（Help）**

禁用用于防止保留内存并发访问问题的互斥锁（Mutex）。仅在需要从中断服务例程（ISR）访问保留内存，或其他特殊用例中才应启用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MULTITHREADING && CONFIG_RETAINED_MEM
```

**被选择（Selected by）**

```text
CONFIG_INSTRUMENTATION_DYNAMIC_TRIGGER
```

**定义位置（Location）**：[`drivers/retained_mem/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/retained_mem/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 保留内存（Retained Memory）驱动

**配置项引用（Symbol References）**：[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_RETAINED_MEM`](P146_drivers_retained_mem_配置项参考.md#CONFIG_RETAINED_MEM)、[`CONFIG_INSTRUMENTATION_DYNAMIC_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INSTRUMENTATION_DYNAMIC_TRIGGER)。

<a id="CONFIG_RETAINED_MEM_NRF_GPREGRET"></a>

## 146.5 `CONFIG_RETAINED_MEM_NRF_GPREGRET`

**提示（Prompt）**：nRF GPREGRET 驱动

**说明（Help）**

启用基于 Nordic nRF GPREGRET 的保留内存寄存器支持驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_GPREGRET_ENABLED && CONFIG_RETAINED_MEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/retained_mem/Kconfig.nrf:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/retained_mem/Kconfig.nrf#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 保留内存（Retained Memory）驱动

**配置项引用（Symbol References）**：[`CONFIG_RETAINED_MEM`](P146_drivers_retained_mem_配置项参考.md#CONFIG_RETAINED_MEM)。

<a id="CONFIG_RETAINED_MEM_NRF_RAM_CTRL"></a>

## 146.6 `CONFIG_RETAINED_MEM_NRF_RAM_CTRL`

**提示（Prompt）**：nRF RAM 保持（Retention）驱动

**说明（Help）**

启用 Nordic RAM 保持驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_RETAINED_RAM_ENABLED && CONFIG_RETAINED_MEM_ZEPHYR_RAM && CONFIG_POWEROFF && CONFIG_HAS_NORDIC_RAM_CTRL && (!CONFIG_TRUSTED_EXECUTION_NONSECURE || CONFIG_SOC_SERIES_NRF71_TFM_RAM_CTRL_SERVICE) && CONFIG_RETAINED_MEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/retained_mem/Kconfig.nrf:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/retained_mem/Kconfig.nrf#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 保留内存（Retained Memory）驱动

**配置项引用（Symbol References）**：[`CONFIG_RETAINED_MEM_ZEPHYR_RAM`](P146_drivers_retained_mem_配置项参考.md#CONFIG_RETAINED_MEM_ZEPHYR_RAM)、[`CONFIG_POWEROFF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POWEROFF)、[`CONFIG_HAS_NORDIC_RAM_CTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_RAM_CTRL)、[`CONFIG_TRUSTED_EXECUTION_NONSECURE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRUSTED_EXECUTION_NONSECURE)、[`CONFIG_SOC_SERIES_NRF71_TFM_RAM_CTRL_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF71_TFM_RAM_CTRL_SERVICE)、[`CONFIG_RETAINED_MEM`](P146_drivers_retained_mem_配置项参考.md#CONFIG_RETAINED_MEM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NORDIC_RAM_CTRL`。

<a id="CONFIG_RETAINED_MEM_RV3028"></a>

## 146.7 `CONFIG_RETAINED_MEM_RV3028`

**提示（Prompt）**：Micro Crystal RV3028 用户 RAM 驱动

**说明（Help）**

启用 Micro Crystal RV3028 的用户 RAM 子驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCRYSTAL_RV3028_RAM_ENABLED && DT_HAS_MICROCRYSTAL_RV3028_ENABLED && CONFIG_RETAINED_MEM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/retained_mem/Kconfig.rv3028:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/retained_mem/Kconfig.rv3028#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 保留内存（Retained Memory）驱动

**配置项引用（Symbol References）**：[`CONFIG_RETAINED_MEM`](P146_drivers_retained_mem_配置项参考.md#CONFIG_RETAINED_MEM)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_RETAINED_MEM_RV3028_INIT_PRIORITY"></a>

## 146.8 `CONFIG_RETAINED_MEM_RV3028_INIT_PRIORITY`

**提示（Prompt）**：RV3028 保留内存初始化优先级

**说明（Help）**

Micro Crystal RV3028 保留内存驱动的初始化优先级，必须晚于 RV3028 MFD 父驱动的初始化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RETAINED_MEM_RV3028 && CONFIG_RETAINED_MEM
```

**默认值（Defaults）**

```text
52
```

**定义位置（Location）**：[`drivers/retained_mem/Kconfig.rv3028:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/retained_mem/Kconfig.rv3028#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 保留内存（Retained Memory）驱动 → Micro Crystal RV3028 用户 RAM 驱动

**配置项引用（Symbol References）**：[`CONFIG_RETAINED_MEM_RV3028`](P146_drivers_retained_mem_配置项参考.md#CONFIG_RETAINED_MEM_RV3028)、[`CONFIG_RETAINED_MEM`](P146_drivers_retained_mem_配置项参考.md#CONFIG_RETAINED_MEM)。

<a id="CONFIG_RETAINED_MEM_SILABS_BURAM"></a>

## 146.9 `CONFIG_RETAINED_MEM_SILABS_BURAM`

**提示（Prompt）**：Silicon Labs BURAM 驱动

**说明（Help）**

启用基于 Silicon Labs BURAM 的保留内存寄存器支持驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_BURAM_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_RETAINED_MEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/retained_mem/Kconfig.silabs:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/retained_mem/Kconfig.silabs#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 保留内存（Retained Memory）驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_RETAINED_MEM`](P146_drivers_retained_mem_配置项参考.md#CONFIG_RETAINED_MEM)。

<a id="CONFIG_RETAINED_MEM_ZEPHYR_RAM"></a>

## 146.10 `CONFIG_RETAINED_MEM_ZEPHYR_RAM`

**提示（Prompt）**：通用 Zephyr RAM 保留内存驱动

**说明（Help）**

启用 RAM 中的保留内存驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_RETAINED_RAM_ENABLED && CONFIG_RETAINED_MEM
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_INSTRUMENTATION_DYNAMIC_TRIGGER
```

**定义位置（Location）**：[`drivers/retained_mem/Kconfig.zephyr:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/retained_mem/Kconfig.zephyr#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 保留内存（Retained Memory）驱动

**配置项引用（Symbol References）**：[`CONFIG_RETAINED_MEM`](P146_drivers_retained_mem_配置项参考.md#CONFIG_RETAINED_MEM)、[`CONFIG_INSTRUMENTATION_DYNAMIC_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INSTRUMENTATION_DYNAMIC_TRIGGER)。

<a id="CONFIG_RETAINED_MEM_ZEPHYR_REG"></a>

## 146.11 `CONFIG_RETAINED_MEM_ZEPHYR_REG`

**提示（Prompt）**：通用 Zephyr 寄存器保留内存驱动

**说明（Help）**

启用保留寄存器（Retained Register）中的保留内存驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_RETAINED_REG_ENABLED && CONFIG_RETAINED_MEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/retained_mem/Kconfig.zephyr:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/retained_mem/Kconfig.zephyr#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 保留内存（Retained Memory）驱动

**配置项引用（Symbol References）**：[`CONFIG_RETAINED_MEM`](P146_drivers_retained_mem_配置项参考.md#CONFIG_RETAINED_MEM)。

<!-- kconfig-navigation -->

[上一章](P145_drivers_reset_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P147_drivers_rtc_配置项参考.md)
