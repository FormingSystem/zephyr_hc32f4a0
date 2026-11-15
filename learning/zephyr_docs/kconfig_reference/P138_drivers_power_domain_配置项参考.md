---
id: learning.zephyr-docs.kconfig-reference.page-138
title: "`drivers/power_domain`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第138章\_`drivers/power_domain`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/power_domain` 的 24 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_POWER_DOMAIN"></a>

## 138.1 `CONFIG_POWER_DOMAIN`

**提示（Prompt）**：电源域驱动（Power Domain Drivers）

**说明（Help）**

在系统配置中纳入电源域驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/power_domain/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/power_domain/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_POWER_DOMAIN_ARM_SCMI"></a>

## 138.2 `CONFIG_POWER_DOMAIN_ARM_SCMI`

**提示（Prompt）**：ARM SCMI 电源域驱动

**说明（Help）**

启用基于系统控制与管理接口（SCMI）的电源域驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_SCMI_POWER_DOMAIN_HELPERS && DT_HAS_ARM_SCMI_POWER_DOMAIN_ENABLED && CONFIG_POWER_DOMAIN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DEVICE_DEPS
```

**定义位置（Location）**：[`drivers/power_domain/Kconfig:132`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/power_domain/Kconfig#L132)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电源域驱动（Power Domain Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SCMI_POWER_DOMAIN_HELPERS`](P091_drivers_firmware_配置项参考.md#CONFIG_ARM_SCMI_POWER_DOMAIN_HELPERS)、[`CONFIG_POWER_DOMAIN`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN)、[`CONFIG_DEVICE_DEPS`](P001_kernel_配置项参考_1.md#CONFIG_DEVICE_DEPS)。

<a id="CONFIG_POWER_DOMAIN_ARM_SCMI_INIT_PRIORITY"></a>

## 138.3 `CONFIG_POWER_DOMAIN_ARM_SCMI_INIT_PRIORITY`

**提示（Prompt）**：ARM SCMI 电源域（PD）驱动初始化优先级

**说明（Help）**

ARM SCMI 电源域驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POWER_DOMAIN_ARM_SCMI && CONFIG_POWER_DOMAIN
```

**默认值（Defaults）**

```text
30
```

**定义位置（Location）**：[`drivers/power_domain/Kconfig:143`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/power_domain/Kconfig#L143)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电源域驱动（Power Domain Drivers） → ARM SCMI 电源域驱动

**配置项引用（Symbol References）**：[`CONFIG_POWER_DOMAIN_ARM_SCMI`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN_ARM_SCMI)、[`CONFIG_POWER_DOMAIN`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN)。

<a id="CONFIG_POWER_DOMAIN_GPIO"></a>

## 138.4 `CONFIG_POWER_DOMAIN_GPIO`

**提示（Prompt）**：GPIO 控制的电源域（Power Domain）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_POWER_DOMAIN_GPIO_ENABLED && CONFIG_GPIO && (CONFIG_PM_DEVICE || !CONFIG_PM_DEVICE_POWER_DOMAIN) && CONFIG_TIMEOUT_64BIT && CONFIG_POWER_DOMAIN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DEVICE_DEPS
```

**定义位置（Location）**：[`drivers/power_domain/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/power_domain/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电源域驱动（Power Domain Drivers）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE)、[`CONFIG_PM_DEVICE_POWER_DOMAIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE_POWER_DOMAIN)、[`CONFIG_TIMEOUT_64BIT`](P002_kernel_配置项参考_2.md#CONFIG_TIMEOUT_64BIT)、[`CONFIG_POWER_DOMAIN`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN)、[`CONFIG_DEVICE_DEPS`](P001_kernel_配置项参考_1.md#CONFIG_DEVICE_DEPS)。

<a id="CONFIG_POWER_DOMAIN_GPIO_INIT_PRIORITY"></a>

## 138.5 `CONFIG_POWER_DOMAIN_GPIO_INIT_PRIORITY`

**提示（Prompt）**：GPIO 电源域初始化优先级

**说明（Help）**

GPIO 电源域的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POWER_DOMAIN_GPIO && CONFIG_POWER_DOMAIN
```

**默认值（Defaults）**

```text
CONFIG_POWER_DOMAIN_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/power_domain/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/power_domain/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电源域驱动（Power Domain Drivers） → GPIO 控制的电源域（Power Domain）

**配置项引用（Symbol References）**：[`CONFIG_POWER_DOMAIN_GPIO`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN_GPIO)、[`CONFIG_POWER_DOMAIN`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN)、[`CONFIG_POWER_DOMAIN_INIT_PRIORITY`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN_INIT_PRIORITY)。

<a id="CONFIG_POWER_DOMAIN_GPIO_MONITOR"></a>

## 138.6 `CONFIG_POWER_DOMAIN_GPIO_MONITOR`

**提示（Prompt）**：检测电源轨（Power Rail）上电状态的 GPIO 监视器

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_POWER_DOMAIN_GPIO_MONITOR_ENABLED && CONFIG_GPIO && CONFIG_PM_DEVICE && CONFIG_POWER_DOMAIN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DEVICE_DEPS
```

**定义位置（Location）**：[`drivers/power_domain/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/power_domain/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电源域驱动（Power Domain Drivers）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE)、[`CONFIG_POWER_DOMAIN`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN)、[`CONFIG_DEVICE_DEPS`](P001_kernel_配置项参考_1.md#CONFIG_DEVICE_DEPS)。

<a id="CONFIG_POWER_DOMAIN_GPIO_MONITOR_INITIAL_READ"></a>

## 138.7 `CONFIG_POWER_DOMAIN_GPIO_MONITOR_INITIAL_READ`

**提示（Prompt）**：初始 GPIO 状态读取（Initial State Read）

**说明（Help）**

启用对监视外部电源域的 GPIO 引脚状态进行一次初始读取，可延迟执行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POWER_DOMAIN_GPIO_MONITOR && CONFIG_POWER_DOMAIN
```

**定义位置（Location）**：[`drivers/power_domain/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/power_domain/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电源域驱动（Power Domain Drivers） → 检测电源轨（Power Rail）上电状态的 GPIO 监视器

**配置项引用（Symbol References）**：[`CONFIG_POWER_DOMAIN_GPIO_MONITOR`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN_GPIO_MONITOR)、[`CONFIG_POWER_DOMAIN`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN)。

<a id="CONFIG_POWER_DOMAIN_GPIO_MONITOR_INIT_PRIORITY"></a>

## 138.8 `CONFIG_POWER_DOMAIN_GPIO_MONITOR_INIT_PRIORITY`

**提示（Prompt）**：GPIO 监视电源域初始化优先级

**说明（Help）**

GPIO 监视电源域的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POWER_DOMAIN_GPIO_MONITOR && CONFIG_POWER_DOMAIN
```

**默认值（Defaults）**

```text
CONFIG_POWER_DOMAIN_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/power_domain/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/power_domain/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电源域驱动（Power Domain Drivers） → 检测电源轨（Power Rail）上电状态的 GPIO 监视器

**配置项引用（Symbol References）**：[`CONFIG_POWER_DOMAIN_GPIO_MONITOR`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN_GPIO_MONITOR)、[`CONFIG_POWER_DOMAIN`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN)、[`CONFIG_POWER_DOMAIN_INIT_PRIORITY`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN_INIT_PRIORITY)。

<a id="CONFIG_POWER_DOMAIN_INIT_PRIORITY"></a>

## 138.9 `CONFIG_POWER_DOMAIN_INIT_PRIORITY`

**提示（Prompt）**：电源域初始化优先级

**说明（Help）**

电源域的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POWER_DOMAIN
```

**默认值（Defaults）**

```text
75
```

**定义位置（Location）**：[`drivers/power_domain/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/power_domain/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电源域驱动（Power Domain Drivers）

**配置项引用（Symbol References）**：[`CONFIG_POWER_DOMAIN`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN)。

<a id="CONFIG_POWER_DOMAIN_INTEL_ADSP"></a>

## 138.10 `CONFIG_POWER_DOMAIN_INTEL_ADSP`

**提示（Prompt）**：使用 Intel ADSP 电源门控（Power Gating）机制

**说明（Help）**

纳入 Intel ADSP 电源域控制机制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_ADSP_POWER_DOMAIN_ENABLED && CONFIG_POWER_DOMAIN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DEVICE_DEPS
```

**定义位置（Location）**：[`drivers/power_domain/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/power_domain/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电源域驱动（Power Domain Drivers）

**配置项引用（Symbol References）**：[`CONFIG_POWER_DOMAIN`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN)、[`CONFIG_DEVICE_DEPS`](P001_kernel_配置项参考_1.md#CONFIG_DEVICE_DEPS)。

<a id="CONFIG_POWER_DOMAIN_INTEL_ADSP_INIT_PRIORITY"></a>

## 138.11 `CONFIG_POWER_DOMAIN_INTEL_ADSP_INIT_PRIORITY`

**提示（Prompt）**：Intel ADSP 电源域初始化优先级

**说明（Help）**

Intel ADSP 电源域的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POWER_DOMAIN_INTEL_ADSP && CONFIG_POWER_DOMAIN
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEFAULT
```

**定义位置（Location）**：[`drivers/power_domain/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/power_domain/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电源域驱动（Power Domain Drivers） → 使用 Intel ADSP 电源门控（Power Gating）机制

**配置项引用（Symbol References）**：[`CONFIG_POWER_DOMAIN_INTEL_ADSP`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN_INTEL_ADSP)、[`CONFIG_POWER_DOMAIN`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN)、[`CONFIG_KERNEL_INIT_PRIORITY_DEFAULT`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEFAULT)。

<a id="CONFIG_POWER_DOMAIN_NRFS_GDPWR"></a>

## 138.12 `CONFIG_POWER_DOMAIN_NRFS_GDPWR`

**提示（Prompt）**：NRFS 全局域电源请求（Global Domain Power Request）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRFS_GDPWR_ENABLED && CONFIG_MULTITHREADING && CONFIG_POWER_DOMAIN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFS
CONFIG_NRFS_GDPWR_SERVICE_ENABLED
```

**定义位置（Location）**：[`drivers/power_domain/Kconfig.nrfs_gdpwr:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/power_domain/Kconfig.nrfs_gdpwr#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电源域驱动（Power Domain Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_POWER_DOMAIN`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN)、[`CONFIG_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS)、[`CONFIG_NRFS_GDPWR_SERVICE_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS_GDPWR_SERVICE_ENABLED)。

<a id="CONFIG_POWER_DOMAIN_NRFS_GDPWR_TIMEOUT_MS"></a>

## 138.13 `CONFIG_POWER_DOMAIN_NRFS_GDPWR_TIMEOUT_MS`

**提示（Prompt）**：GDPWR 请求超时，单位为毫秒

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POWER_DOMAIN_NRFS_GDPWR && CONFIG_POWER_DOMAIN
```

**默认值（Defaults）**

```text
500
```

**定义位置（Location）**：[`drivers/power_domain/Kconfig.nrfs_gdpwr:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/power_domain/Kconfig.nrfs_gdpwr#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电源域驱动（Power Domain Drivers） → NRFS 全局域电源请求（Global Domain Power Request）驱动

**配置项引用（Symbol References）**：[`CONFIG_POWER_DOMAIN_NRFS_GDPWR`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN_NRFS_GDPWR)、[`CONFIG_POWER_DOMAIN`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN)。

<a id="CONFIG_POWER_DOMAIN_NRFS_SWEXT"></a>

## 138.14 `CONFIG_POWER_DOMAIN_NRFS_SWEXT`

**提示（Prompt）**：NRFS SWEXT 电源域驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRFS_SWEXT_ENABLED && CONFIG_POWER_DOMAIN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFS
CONFIG_NRFS_SWEXT_SERVICE_ENABLED
```

**定义位置（Location）**：[`drivers/power_domain/Kconfig.nrfs_swext:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/power_domain/Kconfig.nrfs_swext#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电源域驱动（Power Domain Drivers）

**配置项引用（Symbol References）**：[`CONFIG_POWER_DOMAIN`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN)、[`CONFIG_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS)、[`CONFIG_NRFS_SWEXT_SERVICE_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS_SWEXT_SERVICE_ENABLED)。

<a id="CONFIG_POWER_DOMAIN_NXP_SCU"></a>

## 138.15 `CONFIG_POWER_DOMAIN_NXP_SCU`

**提示（Prompt）**：NXP SCU 管理的电源域（PD）驱动

**说明（Help）**

启用 NXP 系统控制单元（SCU）管理的电源域驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_SCU_PD_ENABLED && CONFIG_POWER_DOMAIN
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/power_domain/Kconfig:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/power_domain/Kconfig#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电源域驱动（Power Domain Drivers）

**配置项引用（Symbol References）**：[`CONFIG_POWER_DOMAIN`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN)。

<a id="CONFIG_POWER_DOMAIN_NXP_SCU_INIT_PRIORITY"></a>

## 138.16 `CONFIG_POWER_DOMAIN_NXP_SCU_INIT_PRIORITY`

**提示（Prompt）**：NXP SCU 管理的电源域驱动初始化优先级

**说明（Help）**

NXP SCU 管理的电源域驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POWER_DOMAIN_NXP_SCU && CONFIG_POWER_DOMAIN
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/power_domain/Kconfig:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/power_domain/Kconfig#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电源域驱动（Power Domain Drivers） → NXP SCU 管理的电源域（PD）驱动

**配置项引用（Symbol References）**：[`CONFIG_POWER_DOMAIN_NXP_SCU`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN_NXP_SCU)、[`CONFIG_POWER_DOMAIN`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN)。

<a id="CONFIG_POWER_DOMAIN_RASPBERRYPI_BCM283X"></a>

## 138.17 `CONFIG_POWER_DOMAIN_RASPBERRYPI_BCM283X`

**提示（Prompt）**：Raspberry Pi BCM283x 电源域驱动

**说明（Help）**

启用 Raspberry Pi BCM283x 电源域驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RASPBERRYPI_BCM283X_POWER_ENABLED && CONFIG_POWER_DOMAIN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_RASPBERRYPI_FIRMWARE
```

**定义位置（Location）**：[`drivers/power_domain/Kconfig.rpi_bcm283x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/power_domain/Kconfig.rpi_bcm283x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电源域驱动（Power Domain Drivers）

**配置项引用（Symbol References）**：[`CONFIG_POWER_DOMAIN`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN)、[`CONFIG_RASPBERRYPI_FIRMWARE`](P091_drivers_firmware_配置项参考.md#CONFIG_RASPBERRYPI_FIRMWARE)。

<a id="CONFIG_POWER_DOMAIN_RASPBERRYPI_BCM283X_INIT_PRIORITY"></a>

## 138.18 `CONFIG_POWER_DOMAIN_RASPBERRYPI_BCM283X_INIT_PRIORITY`

**提示（Prompt）**：Raspberry Pi BCM283x 电源域初始化优先级

**说明（Help）**

数值必须高于 `CONFIG_RASPBERRYPI_FIRMWARE_INIT_PRIORITY`，即更晚执行，确保此驱动初始化前 Raspberry Pi 固件接口已经就绪。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POWER_DOMAIN_RASPBERRYPI_BCM283X && CONFIG_POWER_DOMAIN
```

**默认值（Defaults）**

```text
46
```

**定义位置（Location）**：[`drivers/power_domain/Kconfig.rpi_bcm283x:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/power_domain/Kconfig.rpi_bcm283x#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电源域驱动（Power Domain Drivers） → Raspberry Pi BCM283x 电源域驱动

**配置项引用（Symbol References）**：[`CONFIG_POWER_DOMAIN_RASPBERRYPI_BCM283X`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN_RASPBERRYPI_BCM283X)、[`CONFIG_POWER_DOMAIN`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN)。

<a id="CONFIG_POWER_DOMAIN_SILABS_SIWX91X"></a>

## 138.19 `CONFIG_POWER_DOMAIN_SILABS_SIWX91X`

**提示（Prompt）**：Silabs SiWx91x 电源域驱动

**说明（Help）**

Silabs SiWx91x 电源域驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SIWX91X_POWER_DOMAIN_ENABLED && CONFIG_POWER_DOMAIN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DEVICE_DEPS
```

**定义位置（Location）**：[`drivers/power_domain/Kconfig.silabs_siwx91x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/power_domain/Kconfig.silabs_siwx91x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电源域驱动（Power Domain Drivers）

**配置项引用（Symbol References）**：[`CONFIG_POWER_DOMAIN`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN)、[`CONFIG_DEVICE_DEPS`](P001_kernel_配置项参考_1.md#CONFIG_DEVICE_DEPS)。

<a id="CONFIG_POWER_DOMAIN_SOC_PM_STATE"></a>

## 138.20 `CONFIG_POWER_DOMAIN_SOC_PM_STATE`

**提示（Prompt）**：SoC 电源管理状态电源域（PM State Power Domain）

**说明（Help）**

通用电源域控制，在电源管理（PM）子系统进入或离开某些电源状态时开启／关闭设备。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_POWER_DOMAIN_SOC_STATE_CHANGE_ENABLED && CONFIG_POWER_DOMAIN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DEVICE_DEPS
```

**定义位置（Location）**：[`drivers/power_domain/Kconfig:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/power_domain/Kconfig#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电源域驱动（Power Domain Drivers）

**配置项引用（Symbol References）**：[`CONFIG_POWER_DOMAIN`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN)、[`CONFIG_DEVICE_DEPS`](P001_kernel_配置项参考_1.md#CONFIG_DEVICE_DEPS)。

<a id="CONFIG_POWER_DOMAIN_TISCI"></a>

## 138.21 `CONFIG_POWER_DOMAIN_TISCI`

**提示（Prompt）**：TISCI 管理的电源域

**说明（Help）**

TISCI 管理的电源域控制，在 PM 子系统进入或离开某些电源状态时开启／关闭设备。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_SCI_PM_DOMAIN_ENABLED && CONFIG_POWER_DOMAIN
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/power_domain/Kconfig:108`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/power_domain/Kconfig#L108)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电源域驱动（Power Domain Drivers）

**配置项引用（Symbol References）**：[`CONFIG_POWER_DOMAIN`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN)。

<a id="CONFIG_POWER_DOMAIN_TISCI_INIT_PRIORITY"></a>

## 138.22 `CONFIG_POWER_DOMAIN_TISCI_INIT_PRIORITY`

**提示（Prompt）**：TISCI 管理的电源域初始化优先级

**说明（Help）**

TISCI 管理的电源域的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POWER_DOMAIN_TISCI && CONFIG_POWER_DOMAIN
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/power_domain/Kconfig:118`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/power_domain/Kconfig#L118)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电源域驱动（Power Domain Drivers） → TISCI 管理的电源域

**配置项引用（Symbol References）**：[`CONFIG_POWER_DOMAIN_TISCI`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN_TISCI)、[`CONFIG_POWER_DOMAIN`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN)。

<a id="CONFIG_SIWX91X_POWER_DOMAIN_INIT_PRIORITY"></a>

## 138.23 `CONFIG_SIWX91X_POWER_DOMAIN_INIT_PRIORITY`

**提示（Prompt）**：Silabs SiWx91x 电源域初始化优先级

**说明（Help）**

Silabs SiWx91x 电源域的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POWER_DOMAIN_SILABS_SIWX91X && CONFIG_POWER_DOMAIN
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/power_domain/Kconfig.silabs_siwx91x:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/power_domain/Kconfig.silabs_siwx91x#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电源域驱动（Power Domain Drivers） → Silabs SiWx91x 电源域驱动

**配置项引用（Symbol References）**：[`CONFIG_POWER_DOMAIN_SILABS_SIWX91X`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN_SILABS_SIWX91X)、[`CONFIG_POWER_DOMAIN`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN)。

<a id="CONFIG_SOC_POWER_DOMAIN_INIT"></a>

## 138.24 `CONFIG_SOC_POWER_DOMAIN_INIT`

**提示（Prompt）**：电源域初始化（Power Domain Initialization）

**说明（Help）**

SoC 的电源域初始化。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POWER_DOMAIN_TISCI && CONFIG_POWER_DOMAIN
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/power_domain/Kconfig:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/power_domain/Kconfig#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电源域驱动（Power Domain Drivers） → TISCI 管理的电源域

**配置项引用（Symbol References）**：[`CONFIG_POWER_DOMAIN_TISCI`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN_TISCI)、[`CONFIG_POWER_DOMAIN`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN)。

<!-- kconfig-navigation -->

[上一章](P137_drivers_pm_cpu_ops_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P139_drivers_ps2_配置项参考.md)
