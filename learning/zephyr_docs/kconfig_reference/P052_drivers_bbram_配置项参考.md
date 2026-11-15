---
id: learning.zephyr-docs.kconfig-reference.page-52
title: "`drivers/bbram`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第52章\_`drivers/bbram`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/bbram` 的 17 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BBRAM"></a>

## 52.1 `CONFIG_BBRAM`

**提示（Prompt）**：电池备份 RAM 驱动（Battery-Backed RAM，BBRAM）

**说明（Help）**

启用电池备份 RAM（Battery-Backed RAM，BBRAM）驱动配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/bbram/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bbram/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_BBRAM_EMUL"></a>

## 52.2 `CONFIG_BBRAM_EMUL`

**提示（Prompt）**：电池备份 RAM 仿真驱动（BBRAM Emulated Drivers）

**说明（Help）**

启用电池备份 RAM（BBRAM）仿真驱动（Emulation Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_BBRAM_EMUL_ENABLED && CONFIG_BBRAM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bbram/Kconfig.bbram_emul:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bbram/Kconfig.bbram_emul#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池备份 RAM 驱动（Battery-Backed RAM，BBRAM）

**配置项引用（Symbol References）**：[`CONFIG_BBRAM`](P052_drivers_bbram_配置项参考.md#CONFIG_BBRAM)。

<a id="CONFIG_BBRAM_INIT_PRIORITY"></a>

## 52.3 `CONFIG_BBRAM_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

BBRAM 驱动初始化优先级（Initialization Priority）

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BBRAM
```

**默认值（Defaults）**

```text
65 if CONFIG_BBRAM_STM32
55 if CONFIG_BBRAM_MICROCHIP_MCP7940N
10
```

**定义位置（Location）**：[`drivers/bbram/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bbram/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池备份 RAM 驱动（Battery-Backed RAM，BBRAM）

**配置项引用（Symbol References）**：[`CONFIG_BBRAM`](P052_drivers_bbram_配置项参考.md#CONFIG_BBRAM)、[`CONFIG_BBRAM_STM32`](P052_drivers_bbram_配置项参考.md#CONFIG_BBRAM_STM32)、[`CONFIG_BBRAM_MICROCHIP_MCP7940N`](P052_drivers_bbram_配置项参考.md#CONFIG_BBRAM_MICROCHIP_MCP7940N)。

<a id="CONFIG_BBRAM_IT8XXX2"></a>

## 52.4 `CONFIG_BBRAM_IT8XXX2`

**提示（Prompt）**：ITE IT81202 电池备份 RAM 驱动（Battery-Backed RAM Drivers）

**说明（Help）**

启用 RISCV_ITE 处理器系列的电池备份 RAM（BBRAM）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT8XXX2_BBRAM_ENABLED && CONFIG_BBRAM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bbram/Kconfig.it8xxx2:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bbram/Kconfig.it8xxx2#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池备份 RAM 驱动（Battery-Backed RAM，BBRAM）

**配置项引用（Symbol References）**：[`CONFIG_BBRAM`](P052_drivers_bbram_配置项参考.md#CONFIG_BBRAM)。

<a id="CONFIG_BBRAM_IT8XXX2_EMUL"></a>

## 52.5 `CONFIG_BBRAM_IT8XXX2_EMUL`

**提示（Prompt）**：ITE IT81202 BBRAM 驱动仿真器（Emulator）

**说明（Help）**

启用 ITE IT81202 电池备份 RAM（BBRAM）仿真器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BBRAM_IT8XXX2 && CONFIG_EMUL && CONFIG_BBRAM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bbram/Kconfig.it8xxx2:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bbram/Kconfig.it8xxx2#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池备份 RAM 驱动（Battery-Backed RAM，BBRAM） → ITE IT81202 电池备份 RAM 驱动（Battery-Backed RAM Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BBRAM_IT8XXX2`](P052_drivers_bbram_配置项参考.md#CONFIG_BBRAM_IT8XXX2)、[`CONFIG_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EMUL)、[`CONFIG_BBRAM`](P052_drivers_bbram_配置项参考.md#CONFIG_BBRAM)。

<a id="CONFIG_BBRAM_MICROCHIP_MCP7940N"></a>

## 52.6 `CONFIG_BBRAM_MICROCHIP_MCP7940N`

**提示（Prompt）**：Microchip MCP7940N SRAM 电池备份 RAM 驱动（BBRAM Driver）

**说明（Help）**

启用 Microchip MCP7940N 基于静态 RAM（SRAM）的电池备份 RAM（Battery-Backed RAM）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_MCP7940N_ENABLED && CONFIG_BBRAM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/bbram/Kconfig.microchip:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bbram/Kconfig.microchip#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池备份 RAM 驱动（Battery-Backed RAM，BBRAM）

**配置项引用（Symbol References）**：[`CONFIG_BBRAM`](P052_drivers_bbram_配置项参考.md#CONFIG_BBRAM)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_BBRAM_MICROCHIP_MCP7940N_EMUL"></a>

## 52.7 `CONFIG_BBRAM_MICROCHIP_MCP7940N_EMUL`

**提示（Prompt）**：Microchip MCP7940N SRAM BBRAM 驱动仿真器（Emulator）

**说明（Help）**

启用 Microchip MCP7940N 基于静态 RAM（SRAM）的电池备份 RAM（Battery-Backed RAM）仿真器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BBRAM_MICROCHIP_MCP7940N && CONFIG_EMUL && CONFIG_BBRAM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bbram/Kconfig.microchip:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bbram/Kconfig.microchip#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池备份 RAM 驱动（Battery-Backed RAM，BBRAM） → Microchip MCP7940N SRAM 电池备份 RAM 驱动（BBRAM Driver）

**配置项引用（Symbol References）**：[`CONFIG_BBRAM_MICROCHIP_MCP7940N`](P052_drivers_bbram_配置项参考.md#CONFIG_BBRAM_MICROCHIP_MCP7940N)、[`CONFIG_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EMUL)、[`CONFIG_BBRAM`](P052_drivers_bbram_配置项参考.md#CONFIG_BBRAM)。

<a id="CONFIG_BBRAM_MOTOROLA_MC146818"></a>

## 52.8 `CONFIG_BBRAM_MOTOROLA_MC146818`

**提示（Prompt）**：x86 CMOS／RTC 时钟的电池备份 RAM 驱动（BBRAM Driver）

**说明（Help）**

启用摩托罗拉（Motorola）MC146818 电池备份 RAM（BBRAM）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MOTOROLA_MC146818_BBRAM_ENABLED && CONFIG_BBRAM
```

**默认值（Defaults）**

```text
y if !CONFIG_COUNTER
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/bbram/Kconfig.mc146818:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bbram/Kconfig.mc146818#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池备份 RAM 驱动（Battery-Backed RAM，BBRAM）

**配置项引用（Symbol References）**：[`CONFIG_BBRAM`](P052_drivers_bbram_配置项参考.md#CONFIG_BBRAM)、[`CONFIG_COUNTER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COUNTER)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_BBRAM_NPCX"></a>

## 52.9 `CONFIG_BBRAM_NPCX`

**提示（Prompt）**：新唐 NPCX 嵌入式控制器电池备份 RAM 驱动（Nuvoton EC BBRAM Drivers）

**说明（Help）**

启用 NPCX 处理器系列的电池备份 RAM（BBRAM）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NPCX_BBRAM_ENABLED && CONFIG_BBRAM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bbram/Kconfig.npcx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bbram/Kconfig.npcx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池备份 RAM 驱动（Battery-Backed RAM，BBRAM）

**配置项引用（Symbol References）**：[`CONFIG_BBRAM`](P052_drivers_bbram_配置项参考.md#CONFIG_BBRAM)。

<a id="CONFIG_BBRAM_NPCX_EMUL"></a>

## 52.10 `CONFIG_BBRAM_NPCX_EMUL`

**提示（Prompt）**：NPCX BBRAM 驱动仿真器（Emulator）

**说明（Help）**

启用 NPCX 电池备份 RAM（BBRAM）仿真器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BBRAM_NPCX && CONFIG_EMUL && CONFIG_BBRAM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bbram/Kconfig.npcx:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bbram/Kconfig.npcx#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池备份 RAM 驱动（Battery-Backed RAM，BBRAM） → 新唐 NPCX 嵌入式控制器电池备份 RAM 驱动（Nuvoton EC BBRAM Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BBRAM_NPCX`](P052_drivers_bbram_配置项参考.md#CONFIG_BBRAM_NPCX)、[`CONFIG_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EMUL)、[`CONFIG_BBRAM`](P052_drivers_bbram_配置项参考.md#CONFIG_BBRAM)。

<a id="CONFIG_BBRAM_NPCX_EX"></a>

## 52.11 `CONFIG_BBRAM_NPCX_EX`

**提示（Prompt）**：扩展 NPCX BBRAM 驱动支持（Extended BBRAM Support）

**说明（Help）**

为 NPCKn 处理器变体（Variant）启用扩展电池备份 RAM（BBRAM）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bbram/Kconfig.npcx:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bbram/Kconfig.npcx#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池备份 RAM 驱动（Battery-Backed RAM，BBRAM）

<a id="CONFIG_BBRAM_NPCX_STATUS_REG_WRITE_WORKAROUND"></a>

## 52.12 `CONFIG_BBRAM_NPCX_STATUS_REG_WRITE_WORKAROUND`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

针对 NPCX49nF 勘误表（Errata）rev1_5 第 2.30 项的变通措施（Workaround）。写入 `BKUP_STS` 寄存器可能禁用对全部电池备份 RAM（Battery-Backed RAM）的写入。解决方法是在每次写入该寄存器之后，再读取一次 `BKUP_STS`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BBRAM
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_SERIES_NPCX4
```

**定义位置（Location）**：[`drivers/bbram/Kconfig.npcx:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bbram/Kconfig.npcx#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池备份 RAM 驱动（Battery-Backed RAM，BBRAM）

**配置项引用（Symbol References）**：[`CONFIG_BBRAM`](P052_drivers_bbram_配置项参考.md#CONFIG_BBRAM)、[`CONFIG_SOC_SERIES_NPCX4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCX4)。

<a id="CONFIG_BBRAM_NXP_IMX_SNVS_GPR"></a>

## 52.13 `CONFIG_BBRAM_NXP_IMX_SNVS_GPR`

**提示（Prompt）**：恩智浦 i.MX SNVS 通用寄存器 BBRAM 驱动（NXP General Purpose Registers）

**说明（Help）**

启用基于恩智浦（NXP）i.MX SNVS 低功耗通用寄存器（Low-Power General Purpose Registers）的电池备份 RAM（BBRAM）驱动。该寄存器组的基地址和大小，从当前片上系统（SoC）对应的 MCUX 硬件抽象层（HAL）`SNVS_Type` 定义中获取。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_SNVS_GPR_ENABLED && CONFIG_BBRAM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bbram/Kconfig.nxp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bbram/Kconfig.nxp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池备份 RAM 驱动（Battery-Backed RAM，BBRAM）

**配置项引用（Symbol References）**：[`CONFIG_BBRAM`](P052_drivers_bbram_配置项参考.md#CONFIG_BBRAM)。

<a id="CONFIG_BBRAM_RTS5912"></a>

## 52.14 `CONFIG_BBRAM_RTS5912`

**提示（Prompt）**：瑞昱 RTS5912 电池备份 RAM 驱动（Realtek BBRAM Drivers）

**说明（Help）**

启用瑞昱（Realtek）RTS5912 处理器的电池备份 RAM（BBRAM）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_RTS5912_BBRAM_ENABLED && CONFIG_BBRAM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bbram/Kconfig.rts5912:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bbram/Kconfig.rts5912#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池备份 RAM 驱动（Battery-Backed RAM，BBRAM）

**配置项引用（Symbol References）**：[`CONFIG_BBRAM`](P052_drivers_bbram_配置项参考.md#CONFIG_BBRAM)。

<a id="CONFIG_BBRAM_SHELL"></a>

## 52.15 `CONFIG_BBRAM_SHELL`

**提示（Prompt）**：电池备份 RAM 命令行（BBRAM Shell）

**说明（Help）**

启用电池备份 RAM（BBRAM）命令行，提供读取和写入命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_BBRAM
```

**定义位置（Location）**：[`drivers/bbram/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bbram/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池备份 RAM 驱动（Battery-Backed RAM，BBRAM）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_BBRAM`](P052_drivers_bbram_配置项参考.md#CONFIG_BBRAM)。

<a id="CONFIG_BBRAM_STM32"></a>

## 52.16 `CONFIG_BBRAM_STM32`

**提示（Prompt）**：ST STM32 电池备份 RAM 驱动（BBRAM Drivers）

**说明（Help）**

启用 STM32 处理器系列的电池备份 RAM（BBRAM）驱动。STM32 BBRAM 由可用于保存用户应用数据的 32 位寄存器组成，位于备份域（Backup Domain）中；关闭 `VDD` 电源后，该域仍由 `VBAT` 供电。系统复位或器件从待机模式（Standby Mode）唤醒时，这些寄存器不会复位；备份域复位时才会复位。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_BBRAM_ENABLED && (CONFIG_COUNTER_RTC_STM32 || CONFIG_RTC_STM32) && CONFIG_BBRAM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bbram/Kconfig.stm32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bbram/Kconfig.stm32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池备份 RAM 驱动（Battery-Backed RAM，BBRAM）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER_RTC_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COUNTER_RTC_STM32)、[`CONFIG_RTC_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTC_STM32)、[`CONFIG_BBRAM`](P052_drivers_bbram_配置项参考.md#CONFIG_BBRAM)。

<a id="CONFIG_BBRAM_XEC"></a>

## 52.17 `CONFIG_BBRAM_XEC`

**提示（Prompt）**：Microchip XEC 电池备份 RAM 驱动（BBRAM Drivers）

**说明（Help）**

启用 Microchip XEC 处理器系列的电池备份 RAM（BBRAM）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_XEC_BBRAM_ENABLED && CONFIG_BBRAM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bbram/Kconfig.xec:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bbram/Kconfig.xec#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池备份 RAM 驱动（Battery-Backed RAM，BBRAM）

**配置项引用（Symbol References）**：[`CONFIG_BBRAM`](P052_drivers_bbram_配置项参考.md#CONFIG_BBRAM)。

<!-- kconfig-navigation -->

[上一章](P051_drivers_auxdisplay_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P053_drivers_biometrics_配置项参考.md)
