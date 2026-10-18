---
id: learning.zephyr-docs.kconfig-reference.page-83
title: "`drivers/eeprom`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第83章\_`drivers/eeprom`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/eeprom` 的 23 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_EEPROM"></a>

## 83.1 `CONFIG_EEPROM`

**提示（Prompt）**：电可擦除可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）驱动

**说明（Help）**

启用 EEPROM 硬件支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/eeprom/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/eeprom/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_EEPROM_AT24"></a>

## 83.2 `CONFIG_EEPROM_AT24`

**提示（Prompt）**：Atmel AT24 及兼容器件的 I2C EEPROM 驱动

**说明（Help）**

启用与 Atmel AT24 系列兼容的 I2C EEPROM 支持。多家厂商生产与 Atmel AT24 编程模型（Programming Model）兼容的 I2C EEPROM。兼容 EEPROM 系列示例包括：

- Microchip AT24xxx。
- ST M24xxx。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_AT24_ENABLED && CONFIG_EEPROM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_EEPROM_AT2X
```

**定义位置（Location）**：[`drivers/eeprom/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/eeprom/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电可擦除可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）驱动

**配置项引用（Symbol References）**：[`CONFIG_EEPROM`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)、[`CONFIG_EEPROM_AT2X`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM_AT2X)。

<a id="CONFIG_EEPROM_AT25"></a>

## 83.3 `CONFIG_EEPROM_AT25`

**提示（Prompt）**：Atmel AT25 及兼容器件的 SPI EEPROM 驱动

**说明（Help）**

启用与 Atmel AT25 系列兼容的 SPI EEPROM 支持。多家厂商生产与 Atmel AT25 编程模型（Programming Model）兼容的 SPI EEPROM。兼容 EEPROM 系列示例包括：

- Microchip AT25xxx。
- ST M95xxx。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_AT25_ENABLED && CONFIG_EEPROM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
CONFIG_EEPROM_AT2X
```

**定义位置（Location）**：[`drivers/eeprom/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/eeprom/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电可擦除可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）驱动

**配置项引用（Symbol References）**：[`CONFIG_EEPROM`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_EEPROM_AT2X`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM_AT2X)。

<a id="CONFIG_EEPROM_AT2X"></a>

## 83.4 `CONFIG_EEPROM_AT2X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel AT2x 及兼容器件的 I2C/SPI EEPROM 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EEPROM
```

**被选择（Selected by）**

```text
CONFIG_EEPROM_AT24
CONFIG_EEPROM_AT25
```

**定义位置（Location）**：[`drivers/eeprom/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/eeprom/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电可擦除可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）驱动

**配置项引用（Symbol References）**：[`CONFIG_EEPROM`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM)、[`CONFIG_EEPROM_AT24`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM_AT24)、[`CONFIG_EEPROM_AT25`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM_AT25)。

<a id="CONFIG_EEPROM_AT2X_EMUL"></a>

## 83.5 `CONFIG_EEPROM_AT2X_EMUL`

**提示（Prompt）**：Atmel AT24 I2C EEPROM 仿真器驱动（Emulator Driver）

**说明（Help）**

这是通过 I2C 连接的 Atmel AT24 系列 EEPROM 的仿真器（Emulator）。目前仅支持 8 位寻址（Addressing）。EEPROM 大小由 `size` 属性指定，更多详情参见绑定（Binding）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EMUL && CONFIG_EEPROM
```

**定义位置（Location）**：[`drivers/eeprom/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/eeprom/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电可擦除可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）驱动

**配置项引用（Symbol References）**：[`CONFIG_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EMUL)、[`CONFIG_EEPROM`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM)。

<a id="CONFIG_EEPROM_AT2X_INIT_PRIORITY"></a>

## 83.6 `CONFIG_EEPROM_AT2X_INIT_PRIORITY`

**提示（Prompt）**：AT2X EEPROM 初始化优先级（Init Priority）

**说明（Help）**

AT2X EEPROM 驱动设备的初始化优先级（Initialization Priority）。EEPROM 连接在 I2C 或 SPI 总线上，必须在 I2C/SPI 驱动之后初始化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_EEPROM_AT2X && CONFIG_EEPROM
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/eeprom/Kconfig:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/eeprom/Kconfig#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电可擦除可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）驱动

**配置项引用（Symbol References）**：[`CONFIG_EEPROM_AT2X`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM_AT2X)、[`CONFIG_EEPROM`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM)。

<a id="CONFIG_EEPROM_EMULATOR"></a>

## 83.7 `CONFIG_EEPROM_EMULATOR`

**提示（Prompt）**：闪存模拟 EEPROM 驱动（Emulated EEPROM Driver）

**说明（Help）**

启用基于闪存（Flash）的 EEPROM 模拟支持。此功能在闪存分区（Flash Partition）上模拟外部 EEPROM。通过使用比 EEPROM 区域更大的闪存区域，并且仅存储 EEPROM 数据的变化，尽可能增加 EEPROM 可执行的写入次数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_EMU_EEPROM_ENABLED && CONFIG_EEPROM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH
```

**定义位置（Location）**：[`drivers/eeprom/Kconfig.eeprom_emu:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/eeprom/Kconfig.eeprom_emu#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电可擦除可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）驱动

**配置项引用（Symbol References）**：[`CONFIG_EEPROM`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM)、[`CONFIG_FLASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH)。

<a id="CONFIG_EEPROM_FAKE"></a>

## 83.8 `CONFIG_EEPROM_FAKE`

**提示（Prompt）**：模拟 EEPROM 驱动（Fake EEPROM driver）。

**说明（Help）**

启用基于 FFF 的伪 EEPROM 驱动（Fake EEPROM Driver）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_FAKE_EEPROM_ENABLED && CONFIG_EEPROM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/eeprom/Kconfig:137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/eeprom/Kconfig#L137)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电可擦除可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）驱动

**配置项引用（Symbol References）**：[`CONFIG_EEPROM`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM)。

<a id="CONFIG_EEPROM_FM25XXX"></a>

## 83.9 `CONFIG_EEPROM_FM25XXX`

**提示（Prompt）**：FM25XXX EEPROM 驱动

**说明（Help）**

启用英飞凌（Infineon）FM25XXX SPI 铁电存储器（FRAM）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_FM25XXX_ENABLED && CONFIG_EEPROM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/eeprom/Kconfig.fm25xxx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/eeprom/Kconfig.fm25xxx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电可擦除可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）驱动

**配置项引用（Symbol References）**：[`CONFIG_EEPROM`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_EEPROM_INIT_PRIORITY"></a>

## 83.10 `CONFIG_EEPROM_INIT_PRIORITY`

**提示（Prompt）**：EEPROM 初始化优先级（Init Priority）

**说明（Help）**

EEPROM 驱动设备的初始化优先级（Initialization Priority）。除非具体驱动实现具有自己的初始化优先级，否则使用此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_EEPROM
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/x_nucleo_eeprma2/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/x_nucleo_eeprma2/Kconfig.defconfig)。

```text
75
```

**定义位置（Location）**：[`drivers/eeprom/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/eeprom/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电可擦除可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）驱动

**配置项引用（Symbol References）**：[`CONFIG_EEPROM`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_EEPROM_LPC11U6X"></a>

## 83.11 `CONFIG_EEPROM_LPC11U6X`

**提示（Prompt）**：LPC11U6x EEPROM 驱动

**说明（Help）**

启用 NXP LPC11U6x 微控制器（MCU）中片上 EEPROM（On-Chip EEPROM）的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPC11U6X_EEPROM_ENABLED && CONFIG_EEPROM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/eeprom/Kconfig.lpc11u6x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/eeprom/Kconfig.lpc11u6x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电可擦除可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）驱动

**配置项引用（Symbol References）**：[`CONFIG_EEPROM`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM)。

<a id="CONFIG_EEPROM_MB85RCXX"></a>

## 83.12 `CONFIG_EEPROM_MB85RCXX`

**提示（Prompt）**：MB85RCXX EEPROM 驱动

**说明（Help）**

启用富士通（FUJITSU）MB85RCXX I2C 铁电存储器（FRAM）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_FUJITSU_MB85RCXX_ENABLED && CONFIG_EEPROM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/eeprom/Kconfig.mb85rcxx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/eeprom/Kconfig.mb85rcxx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电可擦除可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）驱动

**配置项引用（Symbol References）**：[`CONFIG_EEPROM`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_EEPROM_MB85RSXX"></a>

## 83.13 `CONFIG_EEPROM_MB85RSXX`

**提示（Prompt）**：MB85RSXX EEPROM 驱动

**说明（Help）**

启用富士通（FUJITSU）MB85RSXX SPI 铁电存储器（FRAM）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_FUJITSU_MB85RSXX_ENABLED && CONFIG_EEPROM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/eeprom/Kconfig.mb85rsxx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/eeprom/Kconfig.mb85rsxx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电可擦除可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）驱动

**配置项引用（Symbol References）**：[`CONFIG_EEPROM`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_EEPROM_RV3028"></a>

## 83.14 `CONFIG_EEPROM_RV3028`

**提示（Prompt）**：Micro Crystal RV3028 EEPROM 驱动

**说明（Help）**

启用 Micro Crystal RV3028 的 EEPROM 子驱动（Child Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCRYSTAL_RV3028_EEPROM_ENABLED && DT_HAS_MICROCRYSTAL_RV3028_ENABLED && CONFIG_EEPROM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/eeprom/Kconfig.rv3028:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/eeprom/Kconfig.rv3028#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电可擦除可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）驱动

**配置项引用（Symbol References）**：[`CONFIG_EEPROM`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_EEPROM_SHELL"></a>

## 83.15 `CONFIG_EEPROM_SHELL`

**提示（Prompt）**：EEPROM 命令行（Shell）

**说明（Help）**

启用提供 EEPROM 相关命令的 EEPROM 命令行（Shell）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_EEPROM
```

**定义位置（Location）**：[`drivers/eeprom/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/eeprom/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电可擦除可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）驱动

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_EEPROM`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM)。

<a id="CONFIG_EEPROM_SHELL_BUFFER_SIZE"></a>

## 83.16 `CONFIG_EEPROM_SHELL_BUFFER_SIZE`

**提示（Prompt）**：EEPROM 命令行缓冲区大小（Shell Buffer Size）

**说明（Help）**

EEPROM 命令行（Shell）中读写命令使用的缓冲区（Buffer）大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_EEPROM_SHELL && CONFIG_EEPROM
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`drivers/eeprom/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/eeprom/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电可擦除可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）驱动 → EEPROM 命令行（Shell）

**配置项引用（Symbol References）**：[`CONFIG_EEPROM_SHELL`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM_SHELL)、[`CONFIG_EEPROM`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM)。

<a id="CONFIG_EEPROM_SIMULATOR"></a>

## 83.17 `CONFIG_EEPROM_SIMULATOR`

**提示（Prompt）**：EEPROM 模拟驱动（Simulated EEPROM Driver）

**说明（Help）**

启用 EEPROM 模拟驱动（Simulated EEPROM Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_SIM_EEPROM_ENABLED && CONFIG_EEPROM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_STATS
CONFIG_STATS_NAMES
```

**定义位置（Location）**：[`drivers/eeprom/Kconfig:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/eeprom/Kconfig#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电可擦除可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）驱动

**配置项引用（Symbol References）**：[`CONFIG_EEPROM`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM)、[`CONFIG_STATS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STATS)、[`CONFIG_STATS_NAMES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STATS_NAMES)。

<a id="CONFIG_EEPROM_SIMULATOR_MIN_READ_TIME_US"></a>

## 83.18 `CONFIG_EEPROM_SIMULATOR_MIN_READ_TIME_US`

**提示（Prompt）**：最小读取时间（Minimum Read Time），单位为微秒（µs）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_EEPROM_SIMULATOR_SIMULATE_TIMING && CONFIG_EEPROM
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 1000000]
```

**定义位置（Location）**：[`drivers/eeprom/Kconfig:123`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/eeprom/Kconfig#L123)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电可擦除可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）驱动 → EEPROM 模拟驱动（Simulated EEPROM Driver） → 硬件时序模拟（Hardware Timing Simulation）

**配置项引用（Symbol References）**：[`CONFIG_EEPROM_SIMULATOR_SIMULATE_TIMING`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM_SIMULATOR_SIMULATE_TIMING)、[`CONFIG_EEPROM`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM)。

<a id="CONFIG_EEPROM_SIMULATOR_MIN_WRITE_TIME_US"></a>

## 83.19 `CONFIG_EEPROM_SIMULATOR_MIN_WRITE_TIME_US`

**提示（Prompt）**：最小写入时间（Minimum Write Time），单位为微秒（µs）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_EEPROM_SIMULATOR_SIMULATE_TIMING && CONFIG_EEPROM
```

**默认值（Defaults）**

```text
100
```

**取值范围（Ranges）**

```text
[1, 1000000]
```

**定义位置（Location）**：[`drivers/eeprom/Kconfig:129`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/eeprom/Kconfig#L129)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电可擦除可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）驱动 → EEPROM 模拟驱动（Simulated EEPROM Driver） → 硬件时序模拟（Hardware Timing Simulation）

**配置项引用（Symbol References）**：[`CONFIG_EEPROM_SIMULATOR_SIMULATE_TIMING`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM_SIMULATOR_SIMULATE_TIMING)、[`CONFIG_EEPROM`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM)。

<a id="CONFIG_EEPROM_SIMULATOR_SIMULATE_TIMING"></a>

## 83.20 `CONFIG_EEPROM_SIMULATOR_SIMULATE_TIMING`

**提示（Prompt）**：硬件时序模拟（Hardware Timing Simulation）

**说明（Help）**

启用模拟的硬件时序（Simulated Hardware Timing）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EEPROM_SIMULATOR && CONFIG_EEPROM
```

**定义位置（Location）**：[`drivers/eeprom/Kconfig:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/eeprom/Kconfig#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电可擦除可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）驱动 → EEPROM 模拟驱动（Simulated EEPROM Driver）

**配置项引用（Symbol References）**：[`CONFIG_EEPROM_SIMULATOR`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM_SIMULATOR)、[`CONFIG_EEPROM`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM)。

<a id="CONFIG_EEPROM_STM32"></a>

## 83.21 `CONFIG_EEPROM_STM32`

**提示（Prompt）**：STM32 EEPROM 驱动

**说明（Help）**

启用 STM32 L0、L1 处理器系列的 EEPROM 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_EEPROM_ENABLED && CONFIG_EEPROM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_HAL_FLASH
CONFIG_USE_STM32_HAL_FLASH_EX
```

**定义位置（Location）**：[`drivers/eeprom/Kconfig.stm32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/eeprom/Kconfig.stm32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电可擦除可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）驱动

**配置项引用（Symbol References）**：[`CONFIG_EEPROM`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM)、[`CONFIG_USE_STM32_HAL_FLASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_FLASH)、[`CONFIG_USE_STM32_HAL_FLASH_EX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_FLASH_EX)。

<a id="CONFIG_EEPROM_TMP11X"></a>

## 83.22 `CONFIG_EEPROM_TMP11X`

**提示（Prompt）**：TMP116、TMP117 和 TMP119 EEPROM 驱动

**说明（Help）**

启用德州仪器（Texas Instruments）TMP116、TMP117 和 TMP119 温度传感器中片上 EEPROM（On-Chip EEPROM）的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_TMP11X_EEPROM_ENABLED && CONFIG_TMP11X && CONFIG_EEPROM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/eeprom/Kconfig.tmp11x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/eeprom/Kconfig.tmp11x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电可擦除可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）驱动

**配置项引用（Symbol References）**：[`CONFIG_TMP11X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TMP11X)、[`CONFIG_EEPROM`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM)。

<a id="CONFIG_EEPROM_XEC"></a>

## 83.23 `CONFIG_EEPROM_XEC`

**提示（Prompt）**：MCHP XEC EEPROM 驱动

**说明（Help）**

启用 Microchip XEC EEPROM 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_XEC_EEPROM_ENABLED && CONFIG_EEPROM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/eeprom/Kconfig.xec:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/eeprom/Kconfig.xec#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电可擦除可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）驱动

**配置项引用（Symbol References）**：[`CONFIG_EEPROM`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<!-- kconfig-navigation -->

[上一章](P082_drivers_edac_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P084_drivers_entropy_配置项参考.md)
