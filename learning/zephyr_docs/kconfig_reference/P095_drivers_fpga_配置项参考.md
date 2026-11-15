---
id: learning.zephyr-docs.kconfig-reference.page-95
title: "`drivers/fpga`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第95章\_`drivers/fpga`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/fpga` 的 12 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ALTERA_AGILEX_BRIDGE_FPGA"></a>

## 95.1 `CONFIG_ALTERA_AGILEX_BRIDGE_FPGA`

**提示（Prompt）**：Altera FPGA 驱动

**说明（Help）**

启用 Altera FPGA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_SIP_SVC_SUBSYS && CONFIG_FPGA
```

**定义位置（Location）**：[`drivers/fpga/Kconfig.altera_agilex_bridge:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fpga/Kconfig.altera_agilex_bridge#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 现场可编程门阵列（Field-Programmable Gate Array，FPGA）驱动

**配置项引用（Symbol References）**：[`CONFIG_ARM_SIP_SVC_SUBSYS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_SIP_SVC_SUBSYS)、[`CONFIG_FPGA`](P095_drivers_fpga_配置项参考.md#CONFIG_FPGA)。

<a id="CONFIG_EOS_S3_FPGA"></a>

## 95.2 `CONFIG_EOS_S3_FPGA`

**提示（Prompt）**：EOS S3 FPGA 驱动

**说明（Help）**

启用 EOS S3 FPGA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FPGA
```

**定义位置（Location）**：[`drivers/fpga/Kconfig.eos_s3:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fpga/Kconfig.eos_s3#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 现场可编程门阵列（Field-Programmable Gate Array，FPGA）驱动

**配置项引用（Symbol References）**：[`CONFIG_FPGA`](P095_drivers_fpga_配置项参考.md#CONFIG_FPGA)。

<a id="CONFIG_FPGA"></a>

## 95.3 `CONFIG_FPGA`

**提示（Prompt）**：现场可编程门阵列（Field-Programmable Gate Array，FPGA）驱动

**说明（Help）**

启用现场可编程门阵列（FPGA）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/fpga/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fpga/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_FPGA_INIT_PRIORITY"></a>

## 95.4 `CONFIG_FPGA_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

FPGA 设备驱动初始化优先级（Initialization Priority）

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FPGA
```

**默认值（Defaults）**

```text
75
```

**定义位置（Location）**：[`drivers/fpga/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fpga/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 现场可编程门阵列（Field-Programmable Gate Array，FPGA）驱动

**配置项引用（Symbol References）**：[`CONFIG_FPGA`](P095_drivers_fpga_配置项参考.md#CONFIG_FPGA)。

<a id="CONFIG_FPGA_SHELL"></a>

## 95.5 `CONFIG_FPGA_SHELL`

**提示（Prompt）**：FPGA 命令行（Shell）

**说明（Help）**

启用 FPGA 命令行（Shell）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_FPGA && CONFIG_FPGA
```

**定义位置（Location）**：[`drivers/fpga/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fpga/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 现场可编程门阵列（Field-Programmable Gate Array，FPGA）驱动

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_FPGA`](P095_drivers_fpga_配置项参考.md#CONFIG_FPGA)。

<a id="CONFIG_ICE40_FPGA"></a>

## 95.6 `CONFIG_ICE40_FPGA`

**提示（Prompt）**：Lattice iCE40 FPGA 驱动

**说明（Help）**

启用莱迪思（Lattice）iCE40 FPGA 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_LATTICE_ICE40_FPGA_ENABLED || DT_HAS_LATTICE_ICE40_FPGA_BITBANG_ENABLED) && CONFIG_SPI && CONFIG_FPGA
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_CRC
```

**定义位置（Location）**：[`drivers/fpga/Kconfig.ice40:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fpga/Kconfig.ice40#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 现场可编程门阵列（Field-Programmable Gate Array，FPGA）驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_FPGA`](P095_drivers_fpga_配置项参考.md#CONFIG_FPGA)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

<a id="CONFIG_ICE40_FPGA_BITBANG"></a>

## 95.7 `CONFIG_ICE40_FPGA_BITBANG`

**提示（Prompt）**：Lattice iCE40 FPGA GPIO 位模拟驱动（Bitbang Driver）【实验性】

**说明（Help）**

启用莱迪思（Lattice）iCE40 FPGA GPIO 位模拟驱动（Bitbang Driver）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LATTICE_ICE40_FPGA_BITBANG_ENABLED && CONFIG_ICE40_FPGA && CONFIG_FPGA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`drivers/fpga/Kconfig.ice40:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fpga/Kconfig.ice40#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 现场可编程门阵列（Field-Programmable Gate Array，FPGA）驱动 → Lattice iCE40 FPGA 驱动

**配置项引用（Symbol References）**：[`CONFIG_ICE40_FPGA`](P095_drivers_fpga_配置项参考.md#CONFIG_ICE40_FPGA)、[`CONFIG_FPGA`](P095_drivers_fpga_配置项参考.md#CONFIG_FPGA)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_ICE40_FPGA_SPI"></a>

## 95.8 `CONFIG_ICE40_FPGA_SPI`

**提示（Prompt）**：Lattice iCE40 FPGA SPI 驱动

**说明（Help）**

启用莱迪思（Lattice）iCE40 FPGA SPI 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LATTICE_ICE40_FPGA_ENABLED && CONFIG_ICE40_FPGA && CONFIG_FPGA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/fpga/Kconfig.ice40:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fpga/Kconfig.ice40#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 现场可编程门阵列（Field-Programmable Gate Array，FPGA）驱动 → Lattice iCE40 FPGA 驱动

**配置项引用（Symbol References）**：[`CONFIG_ICE40_FPGA`](P095_drivers_fpga_配置项参考.md#CONFIG_ICE40_FPGA)、[`CONFIG_FPGA`](P095_drivers_fpga_配置项参考.md#CONFIG_FPGA)。

<a id="CONFIG_MPFS_FPGA"></a>

## 95.9 `CONFIG_MPFS_FPGA`

**提示（Prompt）**：Microchip PolarFire SoC FPGA 驱动

**说明（Help）**

启用 Microchip PolarFire SoC FPGA 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI && CONFIG_FPGA
```

**定义位置（Location）**：[`drivers/fpga/Kconfig.mpfs:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fpga/Kconfig.mpfs#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 现场可编程门阵列（Field-Programmable Gate Array，FPGA）驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_FPGA`](P095_drivers_fpga_配置项参考.md#CONFIG_FPGA)。

<a id="CONFIG_SLG471X5_FPGA"></a>

## 95.10 `CONFIG_SLG471X5_FPGA`

**提示（Prompt）**：瑞萨（Renesas）SLG47105/SLG47115 GreenPAK 可配置混合信号集成电路（Configurable Mixed-Signal IC）

**说明（Help）**

启用瑞萨（Renesas）SLG47105/SLG47115 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_RENESAS_SLG47105_ENABLED || DT_HAS_RENESAS_SLG47115_ENABLED) && CONFIG_FPGA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/fpga/Kconfig.slg471x5:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fpga/Kconfig.slg471x5#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 现场可编程门阵列（Field-Programmable Gate Array，FPGA）驱动

**配置项引用（Symbol References）**：[`CONFIG_FPGA`](P095_drivers_fpga_配置项参考.md#CONFIG_FPGA)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_SLG47910_FPGA"></a>

## 95.11 `CONFIG_SLG47910_FPGA`

**提示（Prompt）**：瑞萨（Renesas）SLG47910 FPGA

**说明（Help）**

启用瑞萨（Renesas）SLG47910 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_SLG47910_ENABLED && CONFIG_FPGA
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

**定义位置（Location）**：[`drivers/fpga/Kconfig.slg47910:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fpga/Kconfig.slg47910#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 现场可编程门阵列（Field-Programmable Gate Array，FPGA）驱动

**配置项引用（Symbol References）**：[`CONFIG_FPGA`](P095_drivers_fpga_配置项参考.md#CONFIG_FPGA)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_ZYNQMP_FPGA"></a>

## 95.12 `CONFIG_ZYNQMP_FPGA`

**提示（Prompt）**：ZynqMP FPGA 驱动

**说明（Help）**

启用 ZynqMP FPGA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FPGA
```

**定义位置（Location）**：[`drivers/fpga/Kconfig.zynqmp:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fpga/Kconfig.zynqmp#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 现场可编程门阵列（Field-Programmable Gate Array，FPGA）驱动

**配置项引用（Symbol References）**：[`CONFIG_FPGA`](P095_drivers_fpga_配置项参考.md#CONFIG_FPGA)。

<!-- kconfig-navigation -->

[上一章](P094_drivers_flash_配置项参考_3.md) · [返回大纲](大纲.md) · [下一章](P096_drivers_fuel_gauge_配置项参考.md)
