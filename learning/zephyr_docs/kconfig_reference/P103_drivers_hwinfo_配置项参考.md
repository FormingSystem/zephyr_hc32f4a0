---
id: learning.zephyr-docs.kconfig-reference.page-103
title: "`drivers/hwinfo`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第103章\_`drivers/hwinfo`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/hwinfo` 的 49 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_HWINFO"></a>

## 103.1 `CONFIG_HWINFO`

**提示（Prompt）**：硬件信息驱动（Hardware Information Drivers）

**说明（Help）**

启用硬件信息（HWINFO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_BT_BFLB
CONFIG_ETH_STM32_HAL
CONFIG_ETH_NUMAKER_DWC_ETHER_1000
CONFIG_ETH_NXP_DWC_ETHER_QOS
CONFIG_ETH_STM32_DWC_ETHER_QOS
CONFIG_ETH_STM32_DWC_ETHER_1000
CONFIG_ETH_NXP_ENET_QOS_UNIQUE_MAC_ADDRESS
CONFIG_WDT_XILINX_AXI_HWINFO_API
CONFIG_WIFI_BFLB
CONFIG_XSI_SINGLE_PROCESS
CONFIG_SHELL_BACKEND_MQTT
CONFIG_USB_DEVICE_STACK
```

**被弱选择（Implied by）**

```text
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD
CONFIG_USB_DEVICE_STACK_NEXT
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_BFLB`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_BFLB)、[`CONFIG_ETH_STM32_HAL`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_HAL)、[`CONFIG_ETH_NUMAKER_DWC_ETHER_1000`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NUMAKER_DWC_ETHER_1000)、[`CONFIG_ETH_NXP_DWC_ETHER_QOS`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_DWC_ETHER_QOS)、[`CONFIG_ETH_STM32_DWC_ETHER_QOS`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_DWC_ETHER_QOS)、[`CONFIG_ETH_STM32_DWC_ETHER_1000`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_DWC_ETHER_1000)、[`CONFIG_ETH_NXP_ENET_QOS_UNIQUE_MAC_ADDRESS`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_ENET_QOS_UNIQUE_MAC_ADDRESS)、[`CONFIG_WDT_XILINX_AXI_HWINFO_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WDT_XILINX_AXI_HWINFO_API)、[`CONFIG_WIFI_BFLB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_BFLB)、[`CONFIG_XSI_SINGLE_PROCESS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XSI_SINGLE_PROCESS)、[`CONFIG_SHELL_BACKEND_MQTT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_MQTT)、[`CONFIG_USB_DEVICE_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_STACK)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_AEAD)、[`CONFIG_USB_DEVICE_STACK_NEXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_HWINFO_AMBIQ"></a>

## 103.2 `CONFIG_HWINFO_AMBIQ`

**提示（Prompt）**：Ambiq 硬件信息（HWINFO）

**说明（Help）**

启用 Ambiq 硬件信息（HWINFO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_APOLLO4X || CONFIG_SOC_SERIES_APOLLO5X) && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
CONFIG_AMBIQ_HAL
CONFIG_AMBIQ_HAL_USE_HWINFO
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.ambiq:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.ambiq#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_APOLLO4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO4X)、[`CONFIG_SOC_SERIES_APOLLO5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO5X)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)、[`CONFIG_AMBIQ_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL)、[`CONFIG_AMBIQ_HAL_USE_HWINFO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL_USE_HWINFO)。

<a id="CONFIG_HWINFO_ANDES"></a>

## 103.3 `CONFIG_HWINFO_ANDES`

**提示（Prompt）**：Andes 系统标识（System ID）

**说明（Help）**

启用 Andes 硬件信息（HWINFO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ANDES_V5 && CONFIG_SYSCON && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.andes:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.andes#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ANDES_V5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ANDES_V5)、[`CONFIG_SYSCON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYSCON)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ANDES_V5`。

<a id="CONFIG_HWINFO_BFLB"></a>

## 103.4 `CONFIG_HWINFO_BFLB`

**提示（Prompt）**：博流（Bouffalo Lab）硬件信息驱动（HWINFO Driver）

**说明（Help）**

启用博流（Bouffalo Lab）硬件信息驱动。将电子熔丝（eFuse）中出厂编程的 MAC 地址用作唯一设备标识（Unique Device ID）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_BFLB && CONFIG_OTP_BFLB && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.bflb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.bflb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_BFLB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_BFLB)、[`CONFIG_OTP_BFLB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OTP_BFLB)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_BFLB`。

<a id="CONFIG_HWINFO_CC13XX_CC26XX"></a>

## 103.5 `CONFIG_HWINFO_CC13XX_CC26XX`

**提示（Prompt）**：TI SimpleLink CC13xx/CC26xx 硬件信息驱动（HWINFO Driver）

**说明（Help）**

启用 TI SimpleLink CC13xx/CC26xx 硬件信息（HWINFO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_CC13X2_CC26X2 || CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7) && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.cc13xx_cc26xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.cc13xx_cc26xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_CC13X2_CC26X2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC13X2_CC26X2)、[`CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

<a id="CONFIG_HWINFO_CC13XX_CC26XX_ALWAYS_USE_FACTORY_DEFAULT"></a>

## 103.6 `CONFIG_HWINFO_CC13XX_CC26XX_ALWAYS_USE_FACTORY_DEFAULT`

**提示（Prompt）**：忽略客户配置（CCFG），始终使用出厂值（Factory Value）

**说明（Help）**

始终返回存储在工厂配置（FCFG）中的出厂预编程值，忽略客户配置（Customer Configuration，CCFG）提供的值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HWINFO_CC13XX_CC26XX && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.cc13xx_cc26xx:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.cc13xx_cc26xx#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers） → TI SimpleLink CC13xx/CC26xx 硬件信息驱动（HWINFO Driver）

**配置项引用（Symbol References）**：[`CONFIG_HWINFO_CC13XX_CC26XX`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_CC13XX_CC26XX)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)。

<a id="CONFIG_HWINFO_CC13XX_CC26XX_USE_BLE_MAC"></a>

## 103.7 `CONFIG_HWINFO_CC13XX_CC26XX_USE_BLE_MAC`

**提示（Prompt）**：使用低功耗蓝牙 MAC 地址（BLE MAC Address）

**说明（Help）**

使用长度为 6 字节的低功耗蓝牙 MAC 地址（BLE MAC Address）作为设备标识（Device ID）值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.cc13xx_cc26xx:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.cc13xx_cc26xx#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers） → TI SimpleLink CC13xx/CC26xx 硬件信息驱动（HWINFO Driver） → 选择设备标识所用的 MAC 地址类型（MAC Address Type）

<a id="CONFIG_HWINFO_CC13XX_CC26XX_USE_IEEE_MAC"></a>

## 103.8 `CONFIG_HWINFO_CC13XX_CC26XX_USE_IEEE_MAC`

**提示（Prompt）**：使用 IEEE 802.15.4 扩展地址（Extended Address）

**说明（Help）**

使用长度为 8 字节的 IEEE 802.15.4 扩展地址（Extended Address）作为设备标识（Device ID）值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.cc13xx_cc26xx:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.cc13xx_cc26xx#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers） → TI SimpleLink CC13xx/CC26xx 硬件信息驱动（HWINFO Driver） → 选择设备标识所用的 MAC 地址类型（MAC Address Type）

<a id="CONFIG_HWINFO_CC23X0"></a>

## 103.9 `CONFIG_HWINFO_CC23X0`

**提示（Prompt）**：TI CC23X0 硬件信息（HWINFO）

**说明（Help）**

启用 CC23X0 硬件信息（HWINFO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_TI_SIMPLELINK && CONFIG_SOC_SERIES_CC23X0 && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.cc23x0:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.cc23x0#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_TI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TI_SIMPLELINK)、[`CONFIG_SOC_SERIES_CC23X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC23X0)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TI_SIMPLELINK`。

<a id="CONFIG_HWINFO_ESP32"></a>

## 103.10 `CONFIG_HWINFO_ESP32`

**提示（Prompt）**：ESP32 设备标识（Device ID）

**说明（Help）**

启用 ESP32 硬件信息（HWINFO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.esp32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.esp32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_HWINFO_GD32"></a>

## 103.11 `CONFIG_HWINFO_GD32`

**提示（Prompt）**：GD32 硬件信息（HWINFO）

**说明（Help）**

启用 GD32 硬件信息（HWINFO）支持。此驱动提供：

- 通过 GD32 UID 寄存器读取 96 位设备唯一标识（Unique ID，UID）。
- 通过复位与时钟单元（RCU）的复位状态寄存器 `RCU_RSTSCK` 报告复位原因（Reset Cause）。

可报告的复位原因取决于兆易创新（GigaDevice）HAL 头文件中提供的复位标志宏，例如外部引脚复位、看门狗复位、软件复位、欠压复位（Brownout Reset）和上电复位（Power-On Reset）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_GD_GD32 && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.gd32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.gd32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_GD_GD32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_GD_GD32)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_GD_GD32`。

<a id="CONFIG_HWINFO_GECKO"></a>

## 103.12 `CONFIG_HWINFO_GECKO`

**提示（Prompt）**：Gecko 硬件信息（HWINFO）

**说明（Help）**

启用 Silabs Gecko 硬件信息（HWINFO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_FAMILY_SILABS_S0 || CONFIG_SOC_FAMILY_SILABS_S1) && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
CONFIG_SILABS_GECKO_RMU
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.gecko:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.gecko#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S0)、[`CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S1)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)、[`CONFIG_SILABS_GECKO_RMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_GECKO_RMU)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S0`、`CONFIG_SOC_FAMILY_SILABS_S1`。

<a id="CONFIG_HWINFO_HAS_DRIVER"></a>

## 103.13 `CONFIG_HWINFO_HAS_DRIVER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项由各个驱动启用，用于表明存在硬件信息驱动（HWINFO Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HWINFO
```

**被选择（Selected by）**

```text
CONFIG_HWINFO_AMBIQ
CONFIG_HWINFO_ANDES
CONFIG_HWINFO_BFLB
CONFIG_HWINFO_CC13XX_CC26XX
CONFIG_HWINFO_CC23X0
CONFIG_HWINFO_ESP32
CONFIG_HWINFO_GD32
CONFIG_HWINFO_GECKO
CONFIG_HWINFO_INFINEON
CONFIG_HWINFO_LITEX
CONFIG_HWINFO_MAX32
CONFIG_HWINFO_MCHP_G1
CONFIG_HWINFO_MSPM0
CONFIG_HWINFO_NATIVE
CONFIG_HWINFO_NRF
CONFIG_HWINFO_NUMAKER
CONFIG_HWINFO_NUMAKER_RMC
CONFIG_HWINFO_NVMEM
CONFIG_HWINFO_NXP_CMC
CONFIG_HWINFO_NXP_IMXRT
CONFIG_HWINFO_NXP_OTP_UID
CONFIG_HWINFO_NXP_PMC
CONFIG_HWINFO_NXP_RCM
CONFIG_HWINFO_NXP_RGM
CONFIG_HWINFO_NXP_RSTCTL
CONFIG_HWINFO_NXP_RW61X
CONFIG_HWINFO_NXP_SIM
CONFIG_HWINFO_NXP_SRC
CONFIG_HWINFO_NXP_SRC_V2
CONFIG_HWINFO_NXP_SYSCON
CONFIG_HWINFO_PSOC6
CONFIG_HWINFO_RENESAS_RA
CONFIG_HWINFO_RPI_PICO
CONFIG_HWINFO_SAM
CONFIG_HWINFO_SAM0
CONFIG_HWINFO_SAM4L
CONFIG_HWINFO_SAM_RSTC
CONFIG_HWINFO_SILABS_S2
CONFIG_HWINFO_SILABS_S3
CONFIG_HWINFO_SMARTBOND
CONFIG_HWINFO_STM32
CONFIG_HWINFO_WCH
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_AMBIQ`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_AMBIQ)、[`CONFIG_HWINFO_ANDES`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_ANDES)、[`CONFIG_HWINFO_BFLB`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_BFLB)、[`CONFIG_HWINFO_CC13XX_CC26XX`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_CC13XX_CC26XX)、[`CONFIG_HWINFO_CC23X0`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_CC23X0)、[`CONFIG_HWINFO_ESP32`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_ESP32)、[`CONFIG_HWINFO_GD32`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_GD32)、[`CONFIG_HWINFO_GECKO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_GECKO)、[`CONFIG_HWINFO_INFINEON`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_INFINEON)、[`CONFIG_HWINFO_LITEX`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_LITEX)、[`CONFIG_HWINFO_MAX32`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_MAX32)、[`CONFIG_HWINFO_MCHP_G1`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_MCHP_G1)、[`CONFIG_HWINFO_MSPM0`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_MSPM0)、[`CONFIG_HWINFO_NATIVE`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_NATIVE)、[`CONFIG_HWINFO_NRF`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_NRF)、[`CONFIG_HWINFO_NUMAKER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_NUMAKER)、[`CONFIG_HWINFO_NUMAKER_RMC`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_NUMAKER_RMC)、[`CONFIG_HWINFO_NVMEM`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_NVMEM)、[`CONFIG_HWINFO_NXP_CMC`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_NXP_CMC)、[`CONFIG_HWINFO_NXP_IMXRT`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_NXP_IMXRT)、[`CONFIG_HWINFO_NXP_OTP_UID`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_NXP_OTP_UID)、[`CONFIG_HWINFO_NXP_PMC`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_NXP_PMC)、[`CONFIG_HWINFO_NXP_RCM`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_NXP_RCM)、[`CONFIG_HWINFO_NXP_RGM`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_NXP_RGM)、[`CONFIG_HWINFO_NXP_RSTCTL`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_NXP_RSTCTL)、[`CONFIG_HWINFO_NXP_RW61X`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_NXP_RW61X)、[`CONFIG_HWINFO_NXP_SIM`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_NXP_SIM)、[`CONFIG_HWINFO_NXP_SRC`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_NXP_SRC)、[`CONFIG_HWINFO_NXP_SRC_V2`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_NXP_SRC_V2)、[`CONFIG_HWINFO_NXP_SYSCON`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_NXP_SYSCON)、[`CONFIG_HWINFO_PSOC6`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_PSOC6)、[`CONFIG_HWINFO_RENESAS_RA`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_RENESAS_RA)、[`CONFIG_HWINFO_RPI_PICO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_RPI_PICO)、[`CONFIG_HWINFO_SAM`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_SAM)、[`CONFIG_HWINFO_SAM0`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_SAM0)、[`CONFIG_HWINFO_SAM4L`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_SAM4L)、[`CONFIG_HWINFO_SAM_RSTC`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_SAM_RSTC)、[`CONFIG_HWINFO_SILABS_S2`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_SILABS_S2)、[`CONFIG_HWINFO_SILABS_S3`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_SILABS_S3)、[`CONFIG_HWINFO_SMARTBOND`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_SMARTBOND)、[`CONFIG_HWINFO_STM32`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_STM32)、[`CONFIG_HWINFO_WCH`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_WCH)。

<a id="CONFIG_HWINFO_INFINEON"></a>

## 103.14 `CONFIG_HWINFO_INFINEON`

**提示（Prompt）**：Infineon 唯一设备标识（Unique Device ID）

**说明（Help）**

启用英飞凌（Infineon）硬件信息（HWINFO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_FAMILY_INFINEON_EDGE || (CONFIG_SOC_FAMILY_INFINEON_CAT1B && !CONFIG_SOC_SERIES_CYW20829)) && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.infineon:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.infineon#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_INFINEON_CAT1B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1B)、[`CONFIG_SOC_SERIES_CYW20829`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CYW20829)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_INFINEON_CAT1B`、`CONFIG_SOC_SERIES_CYW20829`。

<a id="CONFIG_HWINFO_LITEX"></a>

## 103.15 `CONFIG_HWINFO_LITEX`

**提示（Prompt）**：LiteX 设备标识（Device ID）

**说明（Help）**

启用 LiteX 硬件信息（HWINFO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_LITEX_VEXRISCV && DT_HAS_LITEX_DNA0_ENABLED && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.litex:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.litex#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_LITEX_VEXRISCV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LITEX_VEXRISCV)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_LITEX_VEXRISCV`。

<a id="CONFIG_HWINFO_MAX32"></a>

## 103.16 `CONFIG_HWINFO_MAX32`

**提示（Prompt）**：MAX32 硬件信息（HWINFO）

**说明（Help）**

启用 MAX32 硬件信息（HWINFO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_MAX32 && !CONFIG_TRUSTED_EXECUTION_NONSECURE && !CONFIG_SOC_FAMILY_MAX32_RV32 && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.max32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.max32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MAX32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32)、[`CONFIG_TRUSTED_EXECUTION_NONSECURE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRUSTED_EXECUTION_NONSECURE)、[`CONFIG_SOC_FAMILY_MAX32_RV32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_RV32)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MAX32`、`CONFIG_SOC_FAMILY_MAX32_RV32`。

<a id="CONFIG_HWINFO_MCHP_G1"></a>

## 103.17 `CONFIG_HWINFO_MCHP_G1`

**提示（Prompt）**：Microchip 硬件信息（HWINFO）

**说明（Help）**

启用 Microchip 硬件信息（HWINFO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_MICROCHIP_HWINFO_G1_ENABLED || DT_HAS_MICROCHIP_RSTC_G1_RESET_ENABLED) && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.mchp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.mchp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

<a id="CONFIG_HWINFO_MSPM0"></a>

## 103.18 `CONFIG_HWINFO_MSPM0`

**提示（Prompt）**：TI MSPM0 硬件信息（HWINFO）

**说明（Help）**

启用 TI MSPM0 硬件信息（HWINFO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MSPM0_SDK && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.mspm0:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.mspm0#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MSPM0_SDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MSPM0_SDK)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MSPM0_SDK`。

<a id="CONFIG_HWINFO_NATIVE"></a>

## 103.19 `CONFIG_HWINFO_NATIVE`

**提示（Prompt）**：用于 `native_sim` 的硬件信息驱动（HWINFO Driver）

**说明（Help）**

启用 `native_sim` 硬件信息（HWINFO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_POSIX && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.native:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.native#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

<a id="CONFIG_HWINFO_NRF"></a>

## 103.20 `CONFIG_HWINFO_NRF`

**提示（Prompt）**：nRF 设备标识（Device ID）

**说明（Help）**

启用 Nordic nRF 硬件信息（HWINFO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_NORDIC_NRF && (CONFIG_SOC_SERIES_NRF54H || CONFIG_SOC_SERIES_NRF92 || CONFIG_NRF_SOC_SECURE_SUPPORTED) && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.nrf:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.nrf#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_SOC_SERIES_NRF54H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF54H)、[`CONFIG_SOC_SERIES_NRF92`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF92)、[`CONFIG_NRF_SOC_SECURE_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF_SOC_SECURE_SUPPORTED)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_HWINFO_NUMAKER"></a>

## 103.21 `CONFIG_HWINFO_NUMAKER`

**提示（Prompt）**：NuMaker 硬件信息（HWINFO）

**说明（Help）**

启用新唐（Nuvoton）NuMaker 硬件信息（HWINFO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NUMAKER_FMC_ENABLED && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
CONFIG_HAS_NUMAKER_FMC
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.numaker:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.numaker#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)、[`CONFIG_HAS_NUMAKER_FMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NUMAKER_FMC)。

<a id="CONFIG_HWINFO_NUMAKER_RMC"></a>

## 103.22 `CONFIG_HWINFO_NUMAKER_RMC`

**提示（Prompt）**：以 RRAM 控制器（RMC）为后端的 NuMaker 硬件信息（HWINFO）

**说明（Help）**

启用以 RRAM 控制器（RMC）为后端的新唐（Nuvoton）NuMaker 硬件信息驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NUMAKER_RMC_ENABLED && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
CONFIG_HAS_NUMAKER_RMC
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.numaker_rmc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.numaker_rmc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)、[`CONFIG_HAS_NUMAKER_RMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NUMAKER_RMC)。

<a id="CONFIG_HWINFO_NVMEM"></a>

## 103.23 `CONFIG_HWINFO_NVMEM`

**提示（Prompt）**：非易失性存储器（NVMEM）设备标识（Device ID）

**说明（Help）**

通用硬件信息后端（HWINFO Backend），从 `zephyr,hwinfo-nvmem` 设备树（Devicetree）节点描述的 NVMEM 单元（Cell）读取设备唯一标识（Unique Identifier），并可选择读取 EUI-64。一个镜像中只能链接一个硬件信息设备标识后端（Device-ID Backend）；启用本后端时，应禁用 SoC 专用后端，并在 `native_sim` 上禁用 `HWINFO_NATIVE`。提供底层存储的类别，例如 EEPROM、OTP，必须另外启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_HWINFO_NVMEM_ENABLED && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NVMEM
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.nvmem:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.nvmem#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_NVMEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NVMEM)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

<a id="CONFIG_HWINFO_NXP_CMC"></a>

## 103.24 `CONFIG_HWINFO_NXP_CMC`

**提示（Prompt）**：NXP MCX CMC 复位原因（Reset Cause）

**说明（Help）**

启用 NXP Kinetis CMC 硬件信息（HWINFO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_CMC_ENABLED && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.nxp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.nxp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

<a id="CONFIG_HWINFO_NXP_IMXRT"></a>

## 103.25 `CONFIG_HWINFO_NXP_IMXRT`

**提示（Prompt）**：NXP i.MX RT 设备标识（Device ID）

**说明（Help）**

启用 NXP i.MX RT 硬件信息（HWINFO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_IMXRT10XX || CONFIG_SOC_SERIES_IMXRT11XX || CONFIG_SOC_SERIES_IMXRT118X) && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.nxp:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.nxp#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT10XX)、[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT10XX`、`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_SERIES_IMXRT118X`。

<a id="CONFIG_HWINFO_NXP_OTP_UID"></a>

## 103.26 `CONFIG_HWINFO_NXP_OTP_UID`

**提示（Prompt）**：NXP 一次性可编程存储器（OTP）唯一芯片标识（Unique Chip Identifier）

**说明（Help）**

启用硬件信息设备标识后端（HWINFO Device-ID Backend），读取 `nxp,otp-uid` 设备树（Devicetree）节点描述的 NXP OTP 闪存区域中存储的唯一芯片标识（Unique Chip Identifier）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_OTP_UID_ENABLED && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.nxp:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.nxp#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

<a id="CONFIG_HWINFO_NXP_PMC"></a>

## 103.27 `CONFIG_HWINFO_NXP_PMC`

**提示（Prompt）**：NXP LPC PMC 复位原因（Reset Cause）

**说明（Help）**

启用 NXP LPC PMC（AOREG1）的复位原因（Reset Cause）硬件信息驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPC_PMC_HWINFO_ENABLED && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.nxp:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.nxp#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

<a id="CONFIG_HWINFO_NXP_RCM"></a>

## 103.28 `CONFIG_HWINFO_NXP_RCM`

**提示（Prompt）**：NXP Kinetis 复位原因（Reset Cause）

**说明（Help）**

启用 NXP Kinetis 复位控制模块（RCM）的硬件信息驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_RCM_HWINFO_ENABLED && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.nxp:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.nxp#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

<a id="CONFIG_HWINFO_NXP_RGM"></a>

## 103.29 `CONFIG_HWINFO_NXP_RGM`

**提示（Prompt）**：NXP MC_RGM 复位原因（Reset Cause）

**说明（Help）**

启用 NXP MC_RGM 复位生成模块（Reset Generation Module）的硬件信息驱动，用于在具有 MC_RGM 模块的 NXP 微控制器（MCU）上报告复位原因，例如 MCXE 系列。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_MC_RGM_ENABLED && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.nxp:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.nxp#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

<a id="CONFIG_HWINFO_NXP_RSTCTL"></a>

## 103.30 `CONFIG_HWINFO_NXP_RSTCTL`

**提示（Prompt）**：NXP RSTCTL 复位原因（Reset Cause）

**说明（Help）**

启用 NXP RSTCTL 硬件信息（HWINFO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_RSTCTL_HWINFO_ENABLED && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.nxp:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.nxp#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

<a id="CONFIG_HWINFO_NXP_RW61X"></a>

## 103.31 `CONFIG_HWINFO_NXP_RW61X`

**提示（Prompt）**：NXP RW61X 硬件信息（HWINFO）

**说明（Help）**

启用 NXP RW61X 硬件信息（HWINFO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RW6XX && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.nxp:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.nxp#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RW6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RW6XX)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_RW6XX`。

<a id="CONFIG_HWINFO_NXP_SIM"></a>

## 103.32 `CONFIG_HWINFO_NXP_SIM`

**提示（Prompt）**：NXP Kinetis SIM 设备标识（Device ID）

**说明（Help）**

启用 NXP Kinetis SIM 硬件信息（HWINFO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_SIM_UUID_ENABLED && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.nxp:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.nxp#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

<a id="CONFIG_HWINFO_NXP_SRC"></a>

## 103.33 `CONFIG_HWINFO_NXP_SRC`

**提示（Prompt）**：NXP SRC 复位原因（Reset Cause）

**说明（Help）**

启用 NXP i.MX SRC 硬件信息（HWINFO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCUX_SRC && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.nxp:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.nxp#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX_SRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX_SRC)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

<a id="CONFIG_HWINFO_NXP_SRC_V2"></a>

## 103.34 `CONFIG_HWINFO_NXP_SRC_V2`

**提示（Prompt）**：NXP SRC 复位原因（Reset Cause），多核设备（Multicore Devices）

**说明（Help）**

启用第 2 版多核 NXP i.MX SRC 硬件信息（HWINFO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_SRC_REV2_ENABLED && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.nxp:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.nxp#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

<a id="CONFIG_HWINFO_NXP_SYSCON"></a>

## 103.35 `CONFIG_HWINFO_NXP_SYSCON`

**提示（Prompt）**：NXP LPC 设备标识（Device ID）

**说明（Help）**

启用 NXP LPC ID 硬件信息（HWINFO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPC_UID_ENABLED && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.nxp:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.nxp#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

<a id="CONFIG_HWINFO_PSOC6"></a>

## 103.36 `CONFIG_HWINFO_PSOC6`

**提示（Prompt）**：赛普拉斯（Cypress）PSoC 6 唯一设备标识（Unique Device ID）

**说明（Help）**

启用赛普拉斯（Cypress）PSoC 6 硬件信息（HWINFO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_PSOC6_LEGACY && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.psoc6:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.psoc6#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_PSOC6_LEGACY`。

<a id="CONFIG_HWINFO_RENESAS_RA"></a>

## 103.37 `CONFIG_HWINFO_RENESAS_RA`

**提示（Prompt）**：瑞萨（Renesas）RA 设备标识（Device ID）

**说明（Help）**

启用瑞萨（Renesas）RA 硬件信息（HWINFO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.renesas_ra:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.renesas_ra#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_HWINFO_RPI_PICO"></a>

## 103.38 `CONFIG_HWINFO_RPI_PICO`

**提示（Prompt）**：树莓派（Raspberry Pi）Pico 硬件信息驱动（HWINFO Driver）

**说明（Help）**

启用树莓派（Raspberry Pi）Pico 硬件信息驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_RPI_PICO && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
CONFIG_PICOSDK_USE_FLASH
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.rpi_pico:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.rpi_pico#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RPI_PICO)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)、[`CONFIG_PICOSDK_USE_FLASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PICOSDK_USE_FLASH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RPI_PICO`。

<a id="CONFIG_HWINFO_RPI_PICO_CHIP_ID"></a>

## 103.39 `CONFIG_HWINFO_RPI_PICO_CHIP_ID`

**提示（Prompt）**：在 RP2350 上使用芯片标识（Chip ID）作为设备标识（Device ID）

**说明（Help）**

在 RP2350 上使用芯片标识（Chip ID）作为设备标识（Device ID），代替默认的闪存 RUID。对于没有闪存的 RP2350 开发板，或者希望优先使用 OTP ID 而非闪存 RUID 的情况，此选项很有用。建议新的 RP2350 设计使用此选项，但默认仍为 `n`，以免已有设备的序列号（Serial Number）发生变化。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RP2350 && CONFIG_HWINFO_RPI_PICO && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.rpi_pico:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.rpi_pico#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers） → 树莓派（Raspberry Pi）Pico 硬件信息驱动（HWINFO Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RP2350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RP2350)、[`CONFIG_HWINFO_RPI_PICO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_RPI_PICO)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_RP2350`。

<a id="CONFIG_HWINFO_SAM"></a>

## 103.40 `CONFIG_HWINFO_SAM`

**提示（Prompt）**：Atmel SAM 设备标识（Device ID）

**说明（Help）**

启用 Atmel SAM 设备标识（Device ID）的硬件信息驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ATMEL_SAM && !CONFIG_SOC_SERIES_SAM4L && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.sam:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.sam#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ATMEL_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM)、[`CONFIG_SOC_SERIES_SAM4L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAM4L)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM`。

<a id="CONFIG_HWINFO_SAM0"></a>

## 103.41 `CONFIG_HWINFO_SAM0`

**提示（Prompt）**：Atmel SAM0 设备标识（Device ID）

**说明（Help）**

启用 Atmel SAM0 硬件信息（HWINFO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ATMEL_SAM0 && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.sam0:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.sam0#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`。

<a id="CONFIG_HWINFO_SAM4L"></a>

## 103.42 `CONFIG_HWINFO_SAM4L`

**提示（Prompt）**：Atmel SAM4L 设备标识（Device ID）

**说明（Help）**

启用 Atmel SAM4L 硬件信息（HWINFO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_SAM4L && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.sam4l:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.sam4l#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_SAM4L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAM4L)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

<a id="CONFIG_HWINFO_SAM_RSTC"></a>

## 103.43 `CONFIG_HWINFO_SAM_RSTC`

**提示（Prompt）**：Atmel SAM 复位原因（Reset Cause）

**说明（Help）**

启用 Atmel SAM 复位原因（Reset Cause）的硬件信息驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ATMEL_SAM && !CONFIG_SOC_SERIES_SAM4L && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.sam_rstc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.sam_rstc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ATMEL_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM)、[`CONFIG_SOC_SERIES_SAM4L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAM4L)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM`。

<a id="CONFIG_HWINFO_SHELL"></a>

## 103.44 `CONFIG_HWINFO_SHELL`

**提示（Prompt）**：硬件信息命令行（HWINFO Shell）

**说明（Help）**

启用硬件信息命令行（HWINFO Shell），用于测试。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_HWINFO
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)。

<a id="CONFIG_HWINFO_SILABS_S2"></a>

## 103.45 `CONFIG_HWINFO_SILABS_S2`

**提示（Prompt）**：Silabs Series 2 硬件信息（HWINFO）

**说明（Help）**

启用 Silabs Series 2 硬件信息（HWINFO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_SILABS_S2 && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
CONFIG_SILABS_SISDK_RMU
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.silabs:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.silabs#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)、[`CONFIG_SILABS_SISDK_RMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_RMU)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S2`。

<a id="CONFIG_HWINFO_SILABS_S3"></a>

## 103.46 `CONFIG_HWINFO_SILABS_S3`

**提示（Prompt）**：Silabs Series 3 硬件信息（HWINFO）

**说明（Help）**

启用 Silabs Series 3 硬件信息（HWINFO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_SILABS_S3 && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
CONFIG_SILABS_SISDK_EMU
CONFIG_SILABS_SISDK_SYSTEM
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.silabs:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.silabs#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S3)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)、[`CONFIG_SILABS_SISDK_EMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_EMU)、[`CONFIG_SILABS_SISDK_SYSTEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_SYSTEM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S3`。

<a id="CONFIG_HWINFO_SMARTBOND"></a>

## 103.47 `CONFIG_HWINFO_SMARTBOND`

**提示（Prompt）**：Smartbond 设备复位原因（Device Reset Cause）

**说明（Help）**

启用 Smartbond 复位原因（Reset Cause）的硬件信息驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_RENESAS_SMARTBOND && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.smartbond:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.smartbond#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_SMARTBOND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_SMARTBOND)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_SMARTBOND`。

<a id="CONFIG_HWINFO_STM32"></a>

## 103.48 `CONFIG_HWINFO_STM32`

**提示（Prompt）**：STM32 硬件信息（HWINFO）

**说明（Help）**

启用 STM32 硬件信息（HWINFO）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_STM32 && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.stm32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.stm32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_HWINFO_WCH"></a>

## 103.49 `CONFIG_HWINFO_WCH`

**提示（Prompt）**：沁恒（WCH）CH32V 电子签名（Electronic Signature，ESIG）

**说明（Help）**

启用沁恒（WCH）CH32V 系列电子签名（Electronic Signature，ESIG）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WCH_ESIG_ENABLED && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HWINFO_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/hwinfo/Kconfig.wch:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/hwinfo/Kconfig.wch#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_HAS_DRIVER`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO_HAS_DRIVER)。

<!-- kconfig-navigation -->

[上一章](P102_drivers_hdlc_rcp_if_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P104_drivers_hwspinlock_配置项参考.md)
